"""Monte Carlo simulation engine for sales forecasting."""

from dataclasses import dataclass

import numpy as np
from numpy.typing import NDArray

from sales_forecast.models import Pipeline


@dataclass
class SimulationResult:
    """Results from a Monte Carlo simulation run.

    Attributes:
        outcomes: Array of simulated total revenue outcomes
        mean: Mean of all outcomes
        median: Median of all outcomes
        std: Standard deviation of outcomes
        percentiles: Dict mapping percentile (e.g., 10, 50, 90) to value
    """

    outcomes: NDArray[np.float64]
    mean: float
    median: float
    std: float
    percentiles: dict[int, float]

    def confidence_interval(self, confidence: int = 90) -> tuple[float, float]:
        """Return the confidence interval bounds.

        Args:
            confidence: Confidence level (e.g., 90 for 90% CI)

        Returns:
            Tuple of (lower_bound, upper_bound)
        """
        lower_pct = (100 - confidence) // 2
        upper_pct = 100 - lower_pct
        return (self.percentiles[lower_pct], self.percentiles[upper_pct])


class Simulation:
    """Monte Carlo simulation for sales pipeline forecasting."""

    def __init__(self, pipeline: Pipeline, seed: int | None = None) -> None:
        """Initialize the simulation.

        Args:
            pipeline: The sales pipeline to simulate
            seed: Random seed for reproducibility
        """
        self.pipeline = pipeline
        self.rng = np.random.default_rng(seed)

    def run(self, n_simulations: int = 10000) -> SimulationResult:
        """Run Monte Carlo simulation.

        For each simulation, independently sample whether each deal closes
        based on its probability, then sum the values of closed deals.

        Args:
            n_simulations: Number of simulation iterations

        Returns:
            SimulationResult with statistics about the outcomes
        """
        n_deals = len(self.pipeline.deals)
        if n_deals == 0:
            return SimulationResult(
                outcomes=np.array([0.0]),
                mean=0.0,
                median=0.0,
                std=0.0,
                percentiles={5: 0.0, 10: 0.0, 25: 0.0, 50: 0.0, 75: 0.0, 90: 0.0, 95: 0.0},
            )

        # Extract deal values and probabilities as arrays
        values = np.array([deal.value for deal in self.pipeline.deals])
        probabilities = np.array([deal.probability for deal in self.pipeline.deals])

        # Generate random outcomes: shape (n_simulations, n_deals)
        # Each cell is True if that deal closes in that simulation
        random_draws = self.rng.random((n_simulations, n_deals))
        deal_closes = random_draws < probabilities

        # Calculate total revenue for each simulation
        outcomes = (deal_closes * values).sum(axis=1)

        # Calculate statistics
        percentile_values = [5, 10, 25, 50, 75, 90, 95]
        percentiles = dict(
            zip(percentile_values, np.percentile(outcomes, percentile_values), strict=True)
        )

        return SimulationResult(
            outcomes=outcomes,
            mean=float(np.mean(outcomes)),
            median=float(np.median(outcomes)),
            std=float(np.std(outcomes)),
            percentiles=percentiles,
        )
