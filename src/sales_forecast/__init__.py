"""Sales pipeline forecasting using Monte Carlo simulation."""

from sales_forecast.models import Deal, Pipeline
from sales_forecast.simulation import Simulation, SimulationResult

__all__ = ["Deal", "Pipeline", "Simulation", "SimulationResult"]
__version__ = "0.1.0"
