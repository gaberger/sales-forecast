# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Sales pipeline forecasting using Monte Carlo simulation. Two simulation modes:
1. **Basic**: Model deal close probability to forecast revenue distribution
2. **Capacity**: Model SE resource constraints and POC duration impact on revenue

## Commands

```bash
# Install
pip install -e ".[dev]"

# Run tests
python -m pytest

# Lint and type check
ruff check src/ tests/
mypy src/

# Basic forecast from pipeline JSON
sales-forecast <pipeline.json> [-n simulations] [--seed N] [--json]

# POC duration impact analysis
poc-impact --poc-durations 30 90 150 300 --num-ses 10 [-n simulations]
```

## Architecture

```
src/sales_forecast/
├── models.py       # Deal, Pipeline dataclasses
├── simulation.py   # Basic Monte Carlo (Simulation, SimulationResult)
├── capacity.py     # Capacity-constrained simulation (CapacitySimulation)
├── cli.py          # sales-forecast CLI
└── capacity_cli.py # poc-impact CLI
```

### Basic Simulation
Pipeline (list of Deals) → `Simulation.run()` → revenue distribution based on close probabilities

### Capacity Simulation
Models SE resource constraints:
- Opportunities arrive over time (Poisson process)
- Each requires a POC of fixed duration
- POCs require an available SE (queue if all busy)
- After POC completes, deal closes with given probability
- Tracks: revenue, deals closed, deals lost to queue, SE utilization

## Pipeline JSON Format

```json
{"deals": [{"name": "Acme", "value": 50000, "probability": 0.8}]}
```
