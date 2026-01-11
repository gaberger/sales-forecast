"""Tests for Monte Carlo simulation."""

import numpy as np
import pytest

from sales_forecast.models import Deal, Pipeline
from sales_forecast.simulation import Simulation


class TestDeal:
    def test_valid_deal(self) -> None:
        deal = Deal(name="Test", value=1000, probability=0.5)
        assert deal.name == "Test"
        assert deal.value == 1000
        assert deal.probability == 0.5

    def test_invalid_probability_high(self) -> None:
        with pytest.raises(ValueError, match="Probability must be between 0 and 1"):
            Deal(name="Test", value=1000, probability=1.5)

    def test_invalid_probability_negative(self) -> None:
        with pytest.raises(ValueError, match="Probability must be between 0 and 1"):
            Deal(name="Test", value=1000, probability=-0.1)

    def test_invalid_value(self) -> None:
        with pytest.raises(ValueError, match="Deal value must be non-negative"):
            Deal(name="Test", value=-1000, probability=0.5)


class TestPipeline:
    def test_total_value(self) -> None:
        pipeline = Pipeline(
            deals=[
                Deal(name="A", value=1000, probability=0.5),
                Deal(name="B", value=2000, probability=0.8),
            ]
        )
        assert pipeline.total_value() == 3000

    def test_weighted_value(self) -> None:
        pipeline = Pipeline(
            deals=[
                Deal(name="A", value=1000, probability=0.5),
                Deal(name="B", value=2000, probability=0.8),
            ]
        )
        assert pipeline.weighted_value() == 1000 * 0.5 + 2000 * 0.8

    def test_from_list(self) -> None:
        data = [
            {"name": "A", "value": 1000, "probability": 0.5},
            {"name": "B", "value": 2000, "probability": 0.8},
        ]
        pipeline = Pipeline.from_list(data)
        assert len(pipeline.deals) == 2
        assert pipeline.deals[0].name == "A"


class TestSimulation:
    def test_empty_pipeline(self) -> None:
        pipeline = Pipeline(deals=[])
        sim = Simulation(pipeline, seed=42)
        result = sim.run(n_simulations=100)
        assert result.mean == 0.0
        assert result.median == 0.0

    def test_certain_deal(self) -> None:
        """A deal with probability 1.0 should always close."""
        pipeline = Pipeline(deals=[Deal(name="Sure Thing", value=1000, probability=1.0)])
        sim = Simulation(pipeline, seed=42)
        result = sim.run(n_simulations=1000)
        assert result.mean == 1000.0
        assert result.std == 0.0

    def test_impossible_deal(self) -> None:
        """A deal with probability 0.0 should never close."""
        pipeline = Pipeline(deals=[Deal(name="No Chance", value=1000, probability=0.0)])
        sim = Simulation(pipeline, seed=42)
        result = sim.run(n_simulations=1000)
        assert result.mean == 0.0
        assert result.std == 0.0

    def test_reproducibility(self) -> None:
        """Same seed should produce same results."""
        pipeline = Pipeline(
            deals=[
                Deal(name="A", value=1000, probability=0.5),
                Deal(name="B", value=2000, probability=0.3),
            ]
        )
        sim1 = Simulation(pipeline, seed=42)
        sim2 = Simulation(pipeline, seed=42)
        result1 = sim1.run(n_simulations=1000)
        result2 = sim2.run(n_simulations=1000)
        assert result1.mean == result2.mean
        assert np.array_equal(result1.outcomes, result2.outcomes)

    def test_mean_converges_to_weighted_value(self) -> None:
        """With enough simulations, mean should approach weighted value."""
        pipeline = Pipeline(
            deals=[
                Deal(name="A", value=1000, probability=0.5),
                Deal(name="B", value=2000, probability=0.8),
                Deal(name="C", value=500, probability=0.3),
            ]
        )
        sim = Simulation(pipeline, seed=42)
        result = sim.run(n_simulations=100000)
        expected = pipeline.weighted_value()
        # Mean should be within 1% of weighted value
        assert abs(result.mean - expected) / expected < 0.01

    def test_confidence_interval(self) -> None:
        pipeline = Pipeline(
            deals=[
                Deal(name="A", value=1000, probability=0.5),
                Deal(name="B", value=2000, probability=0.5),
            ]
        )
        sim = Simulation(pipeline, seed=42)
        result = sim.run(n_simulations=10000)
        low, high = result.confidence_interval(90)
        assert low < result.median < high
        assert low == result.percentiles[5]
        assert high == result.percentiles[95]
