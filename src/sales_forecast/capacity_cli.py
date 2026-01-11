"""CLI for POC duration capacity analysis."""

import argparse
import json

from sales_forecast.capacity import compare_poc_durations


def main() -> None:
    """Main entry point for capacity analysis CLI."""
    parser = argparse.ArgumentParser(
        description="Analyze how POC duration impacts revenue with limited SE capacity"
    )
    parser.add_argument(
        "--poc-durations",
        type=int,
        nargs="+",
        default=[30, 90, 150, 300],
        help="POC durations to compare in days (default: 30 90 150 300)",
    )
    parser.add_argument(
        "--num-ses",
        type=int,
        default=10,
        help="Number of Sales Engineers (default: 10)",
    )
    parser.add_argument(
        "--pocs-per-se",
        type=int,
        default=1,
        help="Concurrent POCs each SE can run (default: 1)",
    )
    parser.add_argument(
        "--horizon",
        type=int,
        default=365,
        help="Time horizon in days (default: 365)",
    )
    parser.add_argument(
        "--opportunities",
        type=int,
        default=100,
        help="Expected opportunities per year (default: 100)",
    )
    parser.add_argument(
        "--avg-deal-value",
        type=float,
        default=100000,
        help="Average deal value in dollars (default: 100000)",
    )
    parser.add_argument(
        "--win-rate",
        type=float,
        default=0.30,
        help="Win rate after POC completes, e.g., 0.54 for 54%% (default: 0.30)",
    )
    parser.add_argument(
        "-n",
        "--simulations",
        type=int,
        default=1000,
        help="Number of simulations (default: 1000)",
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

    results = compare_poc_durations(
        poc_durations=args.poc_durations,
        num_ses=args.num_ses,
        pocs_per_se=args.pocs_per_se,
        time_horizon_days=args.horizon,
        opportunities_per_year=args.opportunities,
        avg_deal_value=args.avg_deal_value,
        win_rate=args.win_rate,
        n_simulations=args.simulations,
        seed=args.seed,
    )

    if args.json:
        output = {
            "parameters": {
                "num_ses": args.num_ses,
                "pocs_per_se": args.pocs_per_se,
                "time_horizon_days": args.horizon,
                "opportunities_per_year": args.opportunities,
                "avg_deal_value": args.avg_deal_value,
                "win_rate": args.win_rate,
                "simulations": args.simulations,
            },
            "results": {
                duration: {
                    "revenue_mean": r.revenue_mean,
                    "revenue_median": r.revenue_median,
                    "revenue_p10": r.revenue_percentiles[10],
                    "revenue_p90": r.revenue_percentiles[90],
                    "avg_deals_closed": r.avg_deals_closed,
                    "avg_deals_lost": r.avg_deals_lost,
                    "avg_queue_time_days": r.avg_queue_time,
                    "se_utilization": r.avg_utilization,
                }
                for duration, r in results.items()
            },
        }
        print(json.dumps(output, indent=2))
    else:
        print(f"POC Duration Impact Analysis ({args.simulations:,} simulations)")
        pocs_info = f" x {args.pocs_per_se} POCs each" if args.pocs_per_se > 1 else ""
        print(f"SEs: {args.num_ses}{pocs_info} | Win Rate: {args.win_rate:.0%} | "
              f"Opps/year: {args.opportunities}")
        print("=" * 80)
        print()

        # Header
        print(f"{'POC Days':>10} {'Mean Rev':>14} {'Median Rev':>14} "
              f"{'Deals Won':>10} {'Deals Lost':>11} {'Queue (d)':>10} {'SE Util':>8}")
        print("-" * 80)

        # Sort by POC duration
        for duration in sorted(results.keys()):
            r = results[duration]
            print(
                f"{duration:>10} "
                f"${r.revenue_mean:>12,.0f} "
                f"${r.revenue_median:>12,.0f} "
                f"{r.avg_deals_closed:>10.1f} "
                f"{r.avg_deals_lost:>11.1f} "
                f"{r.avg_queue_time:>10.1f} "
                f"{r.avg_utilization:>7.0%}"
            )

        print()
        print("Revenue Comparison (relative to shortest POC):")
        print("-" * 50)

        baseline_duration = min(results.keys())
        baseline_revenue = results[baseline_duration].revenue_mean

        for duration in sorted(results.keys()):
            r = results[duration]
            delta = r.revenue_mean - baseline_revenue
            pct = (delta / baseline_revenue * 100) if baseline_revenue > 0 else 0
            sign = "+" if delta >= 0 else ""
            print(f"  {duration:>3} days: ${r.revenue_mean:>12,.0f}  ({sign}{pct:.1f}%)")


if __name__ == "__main__":
    main()
