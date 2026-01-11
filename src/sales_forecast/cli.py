"""Command-line interface for sales forecasting."""

import argparse
import json
import sys
from pathlib import Path

from sales_forecast.models import Pipeline
from sales_forecast.simulation import Simulation


def main() -> None:
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(
        description="Monte Carlo simulation for sales pipeline forecasting"
    )
    parser.add_argument(
        "pipeline_file",
        type=Path,
        help="JSON file containing pipeline deals",
    )
    parser.add_argument(
        "-n",
        "--simulations",
        type=int,
        default=10000,
        help="Number of simulations to run (default: 10000)",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=None,
        help="Random seed for reproducibility",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output results as JSON",
    )

    args = parser.parse_args()

    # Load pipeline from JSON file
    try:
        with open(args.pipeline_file) as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: File not found: {args.pipeline_file}", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON: {e}", file=sys.stderr)
        sys.exit(1)

    # Create pipeline and run simulation
    pipeline = Pipeline.from_list(data["deals"])
    simulation = Simulation(pipeline, seed=args.seed)
    result = simulation.run(n_simulations=args.simulations)

    if args.json:
        output = {
            "simulations": args.simulations,
            "pipeline_total": pipeline.total_value(),
            "pipeline_weighted": pipeline.weighted_value(),
            "forecast": {
                "mean": result.mean,
                "median": result.median,
                "std": result.std,
                "p10": result.percentiles[10],
                "p50": result.percentiles[50],
                "p90": result.percentiles[90],
            },
        }
        print(json.dumps(output, indent=2))
    else:
        low, high = result.confidence_interval(90)
        print(f"Sales Pipeline Forecast ({args.simulations:,} simulations)")
        print("=" * 50)
        print(f"Pipeline Total Value:    ${pipeline.total_value():>14,.2f}")
        print(f"Weighted Pipeline Value: ${pipeline.weighted_value():>14,.2f}")
        print()
        print("Forecast Results:")
        print(f"  Mean:                  ${result.mean:>14,.2f}")
        print(f"  Median:                ${result.median:>14,.2f}")
        print(f"  Std Dev:               ${result.std:>14,.2f}")
        print()
        print("Percentiles:")
        print(f"  10th (pessimistic):    ${result.percentiles[10]:>14,.2f}")
        print(f"  50th (median):         ${result.percentiles[50]:>14,.2f}")
        print(f"  90th (optimistic):     ${result.percentiles[90]:>14,.2f}")
        print()
        print(f"90% Confidence Interval: ${low:,.2f} - ${high:,.2f}")


if __name__ == "__main__":
    main()
