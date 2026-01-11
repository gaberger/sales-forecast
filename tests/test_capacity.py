"""Tests for capacity-constrained simulation."""

import pytest

from sales_forecast.capacity import (
    CapacitySimulation,
    Opportunity,
    compare_poc_durations,
)


class TestCapacitySimulation:
    def test_single_se_single_opp(self) -> None:
        """Single SE with one opportunity that fits in horizon."""
        sim = CapacitySimulation(
            num_ses=1,
            poc_duration_days=30,
            time_horizon_days=365,
            seed=42,
        )
        opp = Opportunity(value=100000, probability=1.0, arrival_day=0)
        result = sim.run_single(opportunities=[opp])

        assert result.deals_closed == 1
        assert result.total_revenue == 100000
        assert result.deals_lost_to_queue == 0
        assert result.avg_queue_time == 0

    def test_opportunity_exceeds_horizon(self) -> None:
        """POC that can't complete before horizon ends is lost."""
        sim = CapacitySimulation(
            num_ses=1,
            poc_duration_days=100,
            time_horizon_days=365,
            seed=42,
        )
        # Arrives on day 300, POC would end on day 400 > 365
        opp = Opportunity(value=100000, probability=1.0, arrival_day=300)
        result = sim.run_single(opportunities=[opp])

        assert result.deals_closed == 0
        assert result.deals_lost_to_queue == 1
        assert result.total_revenue == 0

    def test_queue_time_when_se_busy(self) -> None:
        """Opportunities queue when all SEs are busy."""
        sim = CapacitySimulation(
            num_ses=1,
            poc_duration_days=30,
            time_horizon_days=365,
            seed=42,
        )
        opps = [
            Opportunity(value=100000, probability=1.0, arrival_day=0),
            Opportunity(value=100000, probability=1.0, arrival_day=10),  # Arrives while SE busy
        ]
        result = sim.run_single(opportunities=opps)

        # Second opp arrives day 10, but must wait until day 30 when SE is free
        # Queue time = 30 - 10 = 20 days
        assert result.avg_queue_time == 10  # Average of 0 and 20

    def test_multiple_ses_parallel_pocs(self) -> None:
        """Multiple SEs can run POCs in parallel."""
        sim = CapacitySimulation(
            num_ses=2,
            poc_duration_days=30,
            time_horizon_days=365,
            seed=42,
        )
        opps = [
            Opportunity(value=100000, probability=1.0, arrival_day=0),
            Opportunity(value=100000, probability=1.0, arrival_day=0),  # Same day, second SE
        ]
        result = sim.run_single(opportunities=opps)

        assert result.deals_closed == 2
        assert result.avg_queue_time == 0  # No queuing with 2 SEs

    def test_zero_probability_never_closes(self) -> None:
        """Deal with 0% probability never closes but uses SE capacity."""
        sim = CapacitySimulation(
            num_ses=1,
            poc_duration_days=30,
            time_horizon_days=365,
            seed=42,
        )
        opp = Opportunity(value=100000, probability=0.0, arrival_day=0)
        result = sim.run_single(opportunities=[opp])

        assert result.deals_closed == 0
        assert result.total_revenue == 0
        assert result.deals_lost_to_queue == 0  # POC completed, just didn't close

    def test_se_utilization_calculation(self) -> None:
        """SE utilization correctly reflects time spent on POCs."""
        sim = CapacitySimulation(
            num_ses=1,
            poc_duration_days=100,
            time_horizon_days=365,
            seed=42,
        )
        opp = Opportunity(value=100000, probability=1.0, arrival_day=0)
        result = sim.run_single(opportunities=[opp])

        # 100 days / 365 days = 27.4% utilization
        assert 0.27 < result.se_utilization < 0.28

    def test_reproducibility_with_seed(self) -> None:
        """Same seed produces same results."""
        sim1 = CapacitySimulation(
            num_ses=10,
            poc_duration_days=90,
            time_horizon_days=365,
            seed=42,
        )
        sim2 = CapacitySimulation(
            num_ses=10,
            poc_duration_days=90,
            time_horizon_days=365,
            seed=42,
        )

        result1 = sim1.run(n_simulations=100)
        result2 = sim2.run(n_simulations=100)

        assert result1.revenue_mean == result2.revenue_mean

    def test_longer_poc_reduces_throughput(self) -> None:
        """Longer POCs should result in fewer deals closed."""
        short_sim = CapacitySimulation(
            num_ses=10,
            poc_duration_days=30,
            time_horizon_days=365,
            opportunities_per_year=100,
            seed=42,
        )
        long_sim = CapacitySimulation(
            num_ses=10,
            poc_duration_days=300,
            time_horizon_days=365,
            opportunities_per_year=100,
            seed=42,
        )

        short_result = short_sim.run(n_simulations=500)
        long_result = long_sim.run(n_simulations=500)

        assert short_result.avg_deals_closed > long_result.avg_deals_closed
        assert short_result.revenue_mean > long_result.revenue_mean


class TestComparePocDurations:
    def test_returns_results_for_each_duration(self) -> None:
        """compare_poc_durations returns results for each requested duration."""
        results = compare_poc_durations(
            poc_durations=[30, 90],
            num_ses=5,
            n_simulations=100,
            seed=42,
        )

        assert 30 in results
        assert 90 in results
        assert results[30].poc_duration == 30
        assert results[90].poc_duration == 90

    def test_shorter_poc_more_revenue(self) -> None:
        """Shorter POC durations should yield more revenue."""
        results = compare_poc_durations(
            poc_durations=[30, 300],
            num_ses=10,
            n_simulations=500,
            seed=42,
        )

        assert results[30].revenue_mean > results[300].revenue_mean
