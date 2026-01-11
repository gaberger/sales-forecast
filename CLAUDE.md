# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Sales pipeline forecasting using Monte Carlo simulation. Models uncertainty in deal outcomes to generate probability distributions of expected revenue.

## Commands

```bash
# Install package with dev dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Run tests with coverage
pytest --cov=sales_forecast --cov-report=term-missing

# Run a single test
pytest tests/test_simulation.py::TestSimulation::test_reproducibility

# Lint
ruff check src/ tests/

# Type check
mypy src/

# Run forecast CLI
sales-forecast <pipeline.json> [-n simulations] [--seed N] [--json]
```

## Architecture

```
src/sales_forecast/
├── models.py      # Deal and Pipeline data classes
├── simulation.py  # Monte Carlo engine (Simulation, SimulationResult)
└── cli.py         # Command-line interface
```

**Core flow**: Pipeline (list of Deals) → Simulation.run() → SimulationResult with statistics

**Simulation approach**: For each iteration, randomly sample whether each deal closes based on its probability, sum closed deal values. Repeat N times to build outcome distribution.

## Pipeline JSON Format

```json
{
  "deals": [
    {"name": "Acme Corp", "value": 50000, "probability": 0.8, "days_to_close": 15}
  ]
}
```

Required fields: `name`, `value`, `probability`. Optional: `days_to_close` (default: 30).
