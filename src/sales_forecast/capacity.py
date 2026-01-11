"""Capacity-constrained simulation modeling SE resources and POC duration impact."""

from dataclasses import dataclass, field

import numpy as np
from numpy.typing import NDArray


@dataclass
class Opportunity:
    """An opportunity requiring a POC before it can close.

    Attributes:
        value: Deal value in dollars
        probability: Probability of closing after POC completes
        arrival_day: Day the opportunity arrives in the pipeline
    """

    value: float
    probability: float
    arrival_day: int


@dataclass
class CapacityResult:
    """Results from a capacity-constrained simulation.

    Attributes:
        total_revenue: Total revenue closed within the time horizon
        deals_closed: Number of deals that closed
        deals_lost_to_queue: Deals that couldn't complete POC in time
        avg_queue_time: Average days waiting for an available SE
        se_utilization: Fraction of SE capacity utilized
    """

    total_revenue: float
    deals_closed: int
    deals_lost_to_queue: int
    avg_queue_time: float
    se_utilization: float


@dataclass
class CapacitySimulationResult:
    """Aggregated results across multiple simulation runs."""

    outcomes: list[CapacityResult]
    poc_duration: int
    num_ses: int

    @property
    def revenue_mean(self) -> float:
        return float(np.mean([o.total_revenue for o in self.outcomes]))

    @property
    def revenue_median(self) -> float:
        return float(np.median([o.total_revenue for o in self.outcomes]))

    @property
    def revenue_std(self) -> float:
        return float(np.std([o.total_revenue for o in self.outcomes]))

    @property
    def revenue_percentiles(self) -> dict[int, float]:
        revenues = [o.total_revenue for o in self.outcomes]
        pcts = [10, 25, 50, 75, 90]
        return dict(zip(pcts, np.percentile(revenues, pcts), strict=True))

    @property
    def avg_deals_closed(self) -> float:
        return float(np.mean([o.deals_closed for o in self.outcomes]))

    @property
    def avg_deals_lost(self) -> float:
        return float(np.mean([o.deals_lost_to_queue for o in self.outcomes]))

    @property
    def avg_queue_time(self) -> float:
        return float(np.mean([o.avg_queue_time for o in self.outcomes]))

    @property
    def avg_utilization(self) -> float:
        return float(np.mean([o.se_utilization for o in self.outcomes]))


@dataclass
class CapacitySimulation:
    """Simulate revenue impact of POC duration with limited SE capacity.

    Models a scenario where:
    - Opportunities arrive over time
    - Each opportunity requires a POC before it can close
    - POCs require an available SE for the full duration
    - When all SEs are busy, opportunities queue
    - After POC completes, deal closes with given probability
    """

    num_ses: int
    poc_duration_days: int
    time_horizon_days: int = 365
    seed: int | None = None
    pocs_per_se: int = 1  # How many concurrent POCs each SE can run

    # Pipeline generation parameters
    opportunities_per_year: int = 100
    avg_deal_value: float = 100000.0
    deal_value_std: float = 50000.0
    avg_close_probability: float = 0.3

    _rng: np.random.Generator = field(init=False, repr=False)

    def __post_init__(self) -> None:
        self._rng = np.random.default_rng(self.seed)

    @property
    def total_poc_slots(self) -> int:
        """Total concurrent POC capacity = SEs × POCs per SE."""
        return self.num_ses * self.pocs_per_se

    def _generate_opportunities(self) -> list[Opportunity]:
        """Generate random opportunities arriving throughout the time horizon."""
        # Number of opportunities follows Poisson distribution
        expected_opps = self.opportunities_per_year * (self.time_horizon_days / 365)
        n_opps = self._rng.poisson(expected_opps)

        opportunities = []
        for _ in range(n_opps):
            # Arrival uniformly distributed across time horizon
            arrival = self._rng.integers(0, self.time_horizon_days)

            # Deal value: lognormal to avoid negative values
            value = max(10000, self._rng.normal(self.avg_deal_value, self.deal_value_std))

            # Close probability: beta distribution centered on avg
            prob = min(0.95, max(0.05, self._rng.normal(self.avg_close_probability, 0.15)))

            opportunities.append(Opportunity(value=value, probability=prob, arrival_day=arrival))

        # Sort by arrival day
        return sorted(opportunities, key=lambda o: o.arrival_day)

    def run_single(self, opportunities: list[Opportunity] | None = None) -> CapacityResult:
        """Run a single simulation.

        Args:
            opportunities: Optional list of opportunities. If None, generates random ones.

        Returns:
            CapacityResult with revenue and capacity metrics
        """
        if opportunities is None:
            opportunities = self._generate_opportunities()

        # Track when each POC slot becomes available (day number)
        # Total slots = num_ses * pocs_per_se
        slot_available_day: NDArray[np.int64] = np.zeros(self.total_poc_slots, dtype=np.int64)

        total_revenue = 0.0
        deals_closed = 0
        deals_lost = 0
        queue_times: list[int] = []
        total_se_days_used = 0

        for opp in opportunities:
            # Find earliest available slot
            earliest_slot = int(np.argmin(slot_available_day))
            earliest_available = int(slot_available_day[earliest_slot])

            # When can POC start?
            poc_start = max(opp.arrival_day, earliest_available)
            queue_time = poc_start - opp.arrival_day
            queue_times.append(queue_time)

            # When does POC complete?
            poc_end = poc_start + self.poc_duration_days

            # Can the POC complete within our time horizon?
            if poc_end > self.time_horizon_days:
                deals_lost += 1
                continue

            # Assign slot for the POC duration
            slot_available_day[earliest_slot] = poc_end
            total_se_days_used += self.poc_duration_days

            # Does the deal close?
            if self._rng.random() < opp.probability:
                total_revenue += opp.value
                deals_closed += 1

        # Calculate SE utilization (based on total slot capacity)
        max_se_days = self.total_poc_slots * self.time_horizon_days
        utilization = total_se_days_used / max_se_days if max_se_days > 0 else 0

        return CapacityResult(
            total_revenue=total_revenue,
            deals_closed=deals_closed,
            deals_lost_to_queue=deals_lost,
            avg_queue_time=float(np.mean(queue_times)) if queue_times else 0.0,
            se_utilization=utilization,
        )

    def run(self, n_simulations: int = 1000) -> CapacitySimulationResult:
        """Run multiple simulations and aggregate results.

        Args:
            n_simulations: Number of simulation iterations

        Returns:
            CapacitySimulationResult with aggregated statistics
        """
        outcomes = [self.run_single() for _ in range(n_simulations)]

        return CapacitySimulationResult(
            outcomes=outcomes,
            poc_duration=self.poc_duration_days,
            num_ses=self.num_ses,
        )


def compare_poc_durations(
    poc_durations: list[int],
    num_ses: int = 10,
    pocs_per_se: int = 1,
    time_horizon_days: int = 365,
    opportunities_per_year: int = 100,
    avg_deal_value: float = 100000.0,
    n_simulations: int = 1000,
    seed: int | None = None,
) -> dict[int, CapacitySimulationResult]:
    """Compare revenue impact across different POC durations.

    Args:
        poc_durations: List of POC durations to compare (in days)
        num_ses: Number of Sales Engineers available
        pocs_per_se: Number of concurrent POCs each SE can run
        time_horizon_days: Time horizon for simulation (default: 1 year)
        opportunities_per_year: Expected opportunities per year
        avg_deal_value: Average deal value
        n_simulations: Number of Monte Carlo iterations
        seed: Random seed for reproducibility

    Returns:
        Dict mapping POC duration to simulation results
    """
    results = {}

    for duration in poc_durations:
        sim = CapacitySimulation(
            num_ses=num_ses,
            poc_duration_days=duration,
            pocs_per_se=pocs_per_se,
            time_horizon_days=time_horizon_days,
            opportunities_per_year=opportunities_per_year,
            avg_deal_value=avg_deal_value,
            seed=seed,
        )
        results[duration] = sim.run(n_simulations)

    return results
