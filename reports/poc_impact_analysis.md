# POC Duration Impact on Revenue
## Sales Capacity Planning Analysis

**Prepared for:** Sales Kick-Off
**Date:** January 2026
**Method:** Monte Carlo Simulation (5,000 iterations)

---

## Executive Summary

Our analysis reveals that **POC duration is the single largest controllable lever for revenue growth** — more impactful than hiring additional SEs. With 10 SEs handling 100 opportunities per year:

| POC Duration | Annual Revenue | Revenue vs 30-day POC |
|--------------|---------------|----------------------|
| 30 days      | **$2.77M**    | Baseline             |
| 90 days      | $968k         | -65%                 |
| 150 days     | $608k         | -78%                 |
| 300 days     | $304k         | -89%                 |

**Key insight:** Reducing POC duration from 90 to 30 days delivers **$1.8M additional revenue** — equivalent to hiring 20 more SEs without changing POC duration.

---

## Methodology

### Monte Carlo Simulation

We used Monte Carlo simulation, a computational technique that models uncertainty by running thousands of randomized scenarios. This approach is used in finance (portfolio risk), engineering (reliability analysis), and operations research (capacity planning).

#### How It Works

```
For each of 5,000 simulation runs:
  1. Generate ~100 opportunities (Poisson arrival process)
  2. Assign each a random value (~$100k avg) and close probability (~30% avg)
  3. Queue opportunities to available SE capacity
  4. For each completed POC, randomly determine if deal closes
  5. Sum closed revenue, track lost deals and queue times

Aggregate across all runs → probability distribution of outcomes
```

#### Why Monte Carlo?

| Traditional Forecast | Monte Carlo Forecast |
|---------------------|---------------------|
| Single point estimate | Full probability distribution |
| "We'll close $2M" | "80% chance of $1.5M-$2.5M" |
| Ignores capacity constraints | Models queuing and bottlenecks |
| Assumes average case | Captures best/worst scenarios |

#### Model Parameters

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Time horizon | 365 days | Annual planning cycle |
| Opportunities/year | 100 | Based on pipeline data |
| Average deal value | $100,000 | Historical average |
| Deal value std dev | $50,000 | Observed variance |
| Average close probability | 30% | Historical win rate |
| Number of SEs | 10 | Current headcount |

---

## Key Findings

### Finding 1: POC Duration Creates a Capacity Ceiling

With fixed SE headcount, POC duration determines maximum throughput:

```
Annual POC Capacity = (SEs × 365 days) ÷ POC Duration

10 SEs at 30-day POCs  → 121 POCs/year (exceeds demand)
10 SEs at 90-day POCs  → 40 POCs/year  (60% of opps lost)
10 SEs at 300-day POCs → 12 POCs/year  (88% of opps lost)
```

**At 90+ day POC durations, we are structurally unable to service demand.**

### Finding 2: Deals Lost to Queue, Not Competition

| POC Duration | Deals Won | Deals Lost to Capacity | Loss Rate |
|--------------|-----------|----------------------|-----------|
| 30 days      | 27.5      | 9.0                  | 25%       |
| 90 days      | 9.6       | 68.2                 | 88%       |
| 150 days     | 6.1       | 79.9                 | 93%       |
| 300 days     | 3.0       | 90.1                 | 97%       |

These aren't competitive losses — they're opportunities that **never got a POC** because all SEs were occupied.

### Finding 3: Queue Time Destroys Deal Viability

| POC Duration | Avg Queue Time | Impact |
|--------------|---------------|--------|
| 30 days      | 2.8 days      | Minimal — deals stay warm |
| 90 days      | 55.7 days     | Champions leave, budgets shift |
| 150 days     | 83.6 days     | Deal likely dead before POC starts |
| 300 days     | 96.2 days     | 3+ months waiting — competitor wins |

*Note: Our model assumes queued deals still close at stated probability. Reality is worse — extended queues reduce close rates.*

### Finding 4: Concurrent POCs Multiply Capacity

If SEs can run multiple POCs in parallel (common for less hands-on evaluations):

| POCs per SE | Revenue (90-day POC) | vs Baseline |
|-------------|---------------------|-------------|
| 1           | $975k               | —           |
| 2           | $1.87M              | +91%        |
| 3           | $2.30M              | +135%       |

**Running 2 POCs concurrently ≈ cutting POC duration in half** from a capacity perspective.

### Finding 5: Hiring Alone Can't Solve Long POCs

Attempting to fix a 300-day POC problem with headcount:

| SEs  | Revenue (300-day POC) | Revenue (30-day POC) |
|------|----------------------|---------------------|
| 10   | $304k                | $2.77M              |
| 20   | $617k                | $2.85M*             |
| 30   | $920k                | $2.87M*             |

*Diminishing returns — demand is satisfied*

**To match 30-day POC revenue with 300-day POCs, you'd need 90+ SEs.**

---

## Recommendations

### Tier 1: Reduce POC Duration (Highest Impact)

| Initiative | Expected Impact | Effort |
|------------|----------------|--------|
| **Standardized POC environments** — Pre-built, one-click deployment | -30 to -60 days | Medium |
| **Time-boxed POCs** — 30-day maximum with clear success criteria | Forces discipline | Low |
| **Parallel workstreams** — Run integration + testing concurrently | -20 to -40 days | Medium |
| **POC-in-a-box** — Self-service evaluation for qualified prospects | Offloads SE time | High |

**Target: Reduce average POC from current baseline to 45 days or less.**

### Tier 2: Increase Effective Capacity

| Initiative | Expected Impact | Effort |
|------------|----------------|--------|
| **POC concurrency** — Enable SEs to run 2 POCs simultaneously | +91% throughput | Low |
| **Tiered POC model** — Light-touch for SMB, full for Enterprise | Right-size effort | Medium |
| **SE specialization** — Experts run POCs faster in their domain | -20% duration | Medium |

### Tier 3: Reduce Demand on POC Capacity

| Initiative | Expected Impact | Effort |
|------------|----------------|--------|
| **Stricter qualification** — Only POC-ready opportunities get SEs | Fewer wasted POCs | Low |
| **Video/recorded POCs** — Reusable content for common use cases | Deflects 10-20% | Medium |
| **Partner-led POCs** — Certified partners handle mid-market | Expands capacity | High |

---

## Revenue Impact Summary

### Conservative Scenario
Reduce POC duration from 90 → 60 days

- **Current:** $968k/year
- **Projected:** ~$1.6M/year
- **Gain:** +$632k (+65%)

### Moderate Scenario
Reduce POC duration from 90 → 45 days + 1.5 POCs/SE concurrency

- **Current:** $968k/year
- **Projected:** ~$2.4M/year
- **Gain:** +$1.43M (+148%)

### Aggressive Scenario
Reduce POC duration from 90 → 30 days + 2 POCs/SE concurrency

- **Current:** $968k/year
- **Projected:** ~$2.9M/year
- **Gain:** +$1.93M (+200%)

---

## Appendix: Model Validation

### Assumptions & Limitations

1. **Constant arrival rate** — Reality has seasonality (Q4 surge)
2. **Fixed close probability** — Doesn't decay with queue time
3. **Uniform POC duration** — Some POCs naturally shorter/longer
4. **No SE specialization** — All SEs assumed interchangeable

### Sensitivity Analysis

The core finding (POC duration dominates) is robust across parameter ranges:

| If opportunities/year... | 30-day POC | 90-day POC | Ratio |
|-------------------------|-----------|-----------|-------|
| 50 (low)                | $1.4M     | $850k     | 1.6x  |
| 100 (baseline)          | $2.8M     | $970k     | 2.9x  |
| 150 (high)              | $2.9M     | $980k     | 3.0x  |

Even at low opportunity volume, shorter POCs significantly outperform.

---

## How to Run Your Own Scenarios

```bash
# Install the simulation tool
pip install -e .

# Compare POC durations
poc-impact --poc-durations 30 60 90 120 --num-ses 10 -n 5000

# Test concurrent POCs
poc-impact --poc-durations 90 --num-ses 10 --pocs-per-se 2

# Custom parameters
poc-impact --poc-durations 45 --num-ses 15 --opportunities 120 --avg-deal-value 150000
```

---

*Analysis performed using Monte Carlo simulation with NumPy/SciPy. Source code available in this repository.*
