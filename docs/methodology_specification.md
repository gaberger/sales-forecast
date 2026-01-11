# Sales Capacity Simulation: Methodology Specification
## Monte Carlo Framework for POC-Constrained Revenue Forecasting

**Version:** 1.0
**Last Updated:** January 2026

---

## 1. Overview

This document specifies the methodology for a Monte Carlo simulation framework that models sales revenue under SE (Sales Engineer) capacity constraints. The framework answers: *"Given limited SE resources and POC requirements, what revenue can we expect?"*

### 1.1 Problem Statement

In enterprise sales, every opportunity requires a Proof of Concept (POC) before closing. POCs consume SE time, creating a capacity constraint. This simulation models:

- How POC duration affects revenue throughput
- Impact of SE headcount on deal capacity
- Queue dynamics when demand exceeds capacity
- Probability distributions of revenue outcomes

### 1.2 Why Monte Carlo?

Traditional forecasting uses deterministic formulas:
```
Revenue = Opportunities × Win Rate × Avg Deal Size
```

This ignores:
- Timing of opportunity arrivals
- Queuing when SEs are busy
- Deals lost because POC can't complete in time
- Variance in deal sizes and win rates

Monte Carlo simulation captures these dynamics by running thousands of randomized scenarios.

---

## 2. Model Architecture

### 2.1 Core Components

```
┌─────────────────────────────────────────────────────────────────┐
│                     SIMULATION ENGINE                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────┐    ┌─────────────────┐                     │
│  │ Opportunity     │    │ Capacity        │                     │
│  │ Generator       │───▶│ Queue           │                     │
│  │ (Poisson)       │    │ (FIFO)          │                     │
│  └─────────────────┘    └────────┬────────┘                     │
│                                  │                              │
│                                  ▼                              │
│                         ┌─────────────────┐                     │
│                         │ SE Pool         │                     │
│                         │ (N slots)       │                     │
│                         └────────┬────────┘                     │
│                                  │                              │
│                                  ▼                              │
│                         ┌─────────────────┐                     │
│                         │ POC Execution   │                     │
│                         │ (Duration D)    │                     │
│                         └────────┬────────┘                     │
│                                  │                              │
│                                  ▼                              │
│                         ┌─────────────────┐                     │
│                         │ Close Decision  │                     │
│                         │ (Bernoulli P)   │                     │
│                         └────────┬────────┘                     │
│                                  │                              │
│                                  ▼                              │
│                         ┌─────────────────┐                     │
│                         │ Revenue         │                     │
│                         │ Accumulator     │                     │
│                         └─────────────────┘                     │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 2.2 Data Structures

#### Opportunity
```python
@dataclass
class Opportunity:
    value: float           # Deal value in dollars
    probability: float     # Close probability (0-1)
    arrival_day: int       # Day opportunity enters pipeline
```

#### Simulation Result
```python
@dataclass
class CapacityResult:
    total_revenue: float          # Sum of closed deal values
    deals_closed: int             # Count of won deals
    deals_lost_to_queue: int      # Deals that couldn't complete POC
    avg_queue_time: float         # Mean days waiting for SE
    se_utilization: float         # Fraction of SE capacity used
```

---

## 3. Stochastic Processes

### 3.1 Opportunity Arrival (Poisson Process)

Opportunities arrive according to a Poisson process with rate λ (opportunities per year).

```
Number of arrivals ~ Poisson(λ × T/365)
Arrival times ~ Uniform(0, T)
```

**Parameters:**
- `opportunities_per_year` (λ): Expected annual opportunity count
- `time_horizon_days` (T): Planning horizon (default: 365)

**Rationale:** Poisson models independent, random arrivals at a constant average rate — appropriate for lead generation.

### 3.2 Deal Value Distribution (Normal)

Deal values follow a normal distribution, truncated to ensure positive values.

```
Value ~ max(min_value, Normal(μ, σ))
```

**Parameters:**
- `avg_deal_value` (μ): Mean deal size
- `deal_value_std` (σ): Standard deviation (default: 50% of mean)
- Minimum value: $10,000 (floor)

**Rationale:** Deal sizes cluster around an average with symmetric variance. Log-normal is an alternative for highly skewed distributions.

### 3.3 Win Probability Distribution (Normal, bounded)

Individual deal win probabilities vary around a mean.

```
Probability ~ clip(Normal(p, 0.15), 0.05, 0.95)
```

**Parameters:**
- `avg_close_probability` (p): Mean win rate
- Standard deviation: 0.15 (fixed)
- Bounds: [0.05, 0.95]

**Rationale:** Some deals are stronger/weaker than average. Bounds prevent degenerate cases.

### 3.4 Close Decision (Bernoulli)

After POC completion, deal closes with its assigned probability.

```
Closed ~ Bernoulli(probability)
```

**Rationale:** Binary outcome (win/loss) with known probability.

---

## 4. Capacity Model

### 4.1 SE Slots

Total concurrent POC capacity:
```
Total Slots = num_ses × pocs_per_se
```

Each slot tracks when it becomes available (day number).

### 4.2 Queue Dynamics (FIFO)

When an opportunity arrives:
1. Find earliest available slot
2. If slot available before arrival → no queue
3. If slot available after arrival → queue time = slot_available - arrival_day
4. Assign opportunity to slot; slot becomes available at: max(arrival, slot_available) + poc_duration

### 4.3 Deal Loss Condition

A deal is **lost to capacity** if:
```
poc_start + poc_duration > time_horizon
```

This models deals that can't complete POC before the planning horizon ends.

### 4.4 Utilization Calculation

```
SE Utilization = (total_poc_days_used) / (total_slots × time_horizon)
```

---

## 5. Simulation Algorithm

```
FUNCTION run_single_simulation():
    opportunities = generate_opportunities()      # Poisson arrivals
    sort opportunities by arrival_day

    slot_available = [0] × total_slots           # Day each slot is free
    revenue = 0
    deals_closed = 0
    deals_lost = 0
    queue_times = []

    FOR each opportunity IN opportunities:
        earliest_slot = argmin(slot_available)
        poc_start = max(opportunity.arrival_day, slot_available[earliest_slot])
        queue_time = poc_start - opportunity.arrival_day
        queue_times.append(queue_time)

        poc_end = poc_start + poc_duration

        IF poc_end > time_horizon:
            deals_lost += 1
            CONTINUE

        slot_available[earliest_slot] = poc_end

        IF random() < opportunity.probability:
            revenue += opportunity.value
            deals_closed += 1

    RETURN CapacityResult(revenue, deals_closed, deals_lost, mean(queue_times), utilization)


FUNCTION run_monte_carlo(n_simulations):
    results = []
    FOR i IN 1..n_simulations:
        results.append(run_single_simulation())

    RETURN aggregate_statistics(results)
```

---

## 6. Statistical Outputs

### 6.1 Point Estimates
- **Mean Revenue**: Expected value across simulations
- **Median Revenue**: 50th percentile (robust to outliers)
- **Standard Deviation**: Measure of outcome uncertainty

### 6.2 Percentiles
- **P10 (Pessimistic)**: Revenue exceeded 90% of the time
- **P50 (Median)**: Revenue exceeded 50% of the time
- **P90 (Optimistic)**: Revenue exceeded 10% of the time

### 6.3 Confidence Intervals
```
90% CI = [P5, P95]
80% CI = [P10, P90]
```

### 6.4 Operational Metrics
- **Deals Closed**: Mean deals won
- **Deals Lost**: Mean deals lost to capacity
- **Queue Time**: Mean days waiting for SE
- **Utilization**: Mean SE capacity usage

---

## 7. Parameter Sensitivity

### 7.1 Key Parameters (High Impact)

| Parameter | Symbol | Impact |
|-----------|--------|--------|
| POC Duration | D | Directly limits throughput: Capacity = Slots × (T/D) |
| Win Rate | p | Linear impact on revenue: Revenue ∝ p |
| Deal Size | μ | Linear impact on revenue: Revenue ∝ μ |
| SE Count | N | Linear impact on capacity: Slots = N × pocs_per_se |

### 7.2 Secondary Parameters (Moderate Impact)

| Parameter | Impact |
|-----------|--------|
| Opportunities | More opps → higher utilization, potential queue buildup |
| POCs per SE | Multiplies effective capacity |
| Time Horizon | Affects year-end cutoff dynamics |

### 7.3 Recommended Sensitivity Analysis

Test ±20% on each key parameter to understand model sensitivity:
```bash
poc-impact --poc-durations 24 30 36 ...   # ±20% on POC duration
poc-impact --win-rate 0.43 0.54 0.65 ...  # ±20% on win rate
```

---

## 8. Convergence & Sample Size

### 8.1 Convergence Criteria

The mean estimate stabilizes when additional samples don't materially change results.

| Samples | Typical Accuracy |
|---------|------------------|
| 100 | ±5% |
| 500 | ±2% |
| 1,000 | ±1% |
| 2,000 | ±0.5% |
| 5,000 | ±0.2% |

### 8.2 Recommended Sample Sizes

- **Exploratory analysis**: 500-1,000
- **Standard planning**: 2,000
- **Final reports**: 5,000+

### 8.3 Reproducibility

Use `seed` parameter for reproducible results:
```bash
poc-impact --seed 42 ...
```

---

## 9. Model Limitations

### 9.1 What the Model Does NOT Capture

| Factor | Reality | Model Assumption |
|--------|---------|------------------|
| Deal decay | Probability decreases with queue time | Constant probability |
| SE specialization | Some SEs can't do all POCs | All SEs interchangeable |
| Seasonality | Q4 surge, budget cycles | Uniform arrivals |
| Variable POC duration | Some POCs are shorter/longer | Fixed duration |
| Partial POCs | Some POCs abandoned mid-way | Binary completion |
| Post-POC stages | Legal, procurement delays | Not modeled (use horizon adjustment) |
| Competitive dynamics | Lost deals go to competitors | No competitive feedback |

### 9.2 Workarounds

**Post-POC delays:** Reduce `time_horizon_days` by expected buffer
```bash
poc-impact --horizon 320 ...  # 365 - 45 day buffer
```

**Variable POC duration:** Run scenarios at different durations and weight by mix
```bash
poc-impact --poc-durations 30 45 60 --num-ses 10
```

---

## 10. Implementation Reference

### 10.1 Core Files

| File | Purpose |
|------|---------|
| `capacity.py` | CapacitySimulation class, Monte Carlo engine |
| `capacity_cli.py` | Command-line interface |
| `models.py` | Deal, Pipeline data structures |
| `simulation.py` | Basic (non-capacity) Monte Carlo |

### 10.2 CLI Usage

```bash
# Basic analysis
poc-impact --poc-durations 30 60 90 \
           --num-ses 10 \
           --avg-deal-value 1100000 \
           --win-rate 0.54 \
           --opportunities 100 \
           -n 2000

# With post-POC buffer (45 days)
poc-impact --poc-durations 30 \
           --horizon 320 \
           ...

# JSON output for programmatic use
poc-impact --json ...
```

### 10.3 Python API

```python
from sales_forecast.capacity import CapacitySimulation, compare_poc_durations

# Single configuration
sim = CapacitySimulation(
    num_ses=10,
    poc_duration_days=30,
    opportunities_per_year=100,
    avg_deal_value=1_100_000,
    avg_close_probability=0.54,
    seed=42,
)
result = sim.run(n_simulations=2000)
print(f"Mean revenue: ${result.revenue_mean:,.0f}")

# Compare configurations
results = compare_poc_durations(
    poc_durations=[30, 60, 90],
    num_ses=10,
    win_rate=0.54,
)
```

---

## 11. Validation Checklist

Before using model outputs for decisions:

- [ ] Parameters reflect actual business data (win rate, deal size, SE count)
- [ ] Sample size is sufficient (≥2,000 for planning)
- [ ] Sensitivity analysis performed on key parameters
- [ ] Post-POC buffer accounted for (adjust horizon)
- [ ] Results sanity-checked against historical actuals
- [ ] Compound risk scenarios tested

---

## Appendix A: Mathematical Notation

| Symbol | Meaning |
|--------|---------|
| N | Number of SEs |
| D | POC duration (days) |
| T | Time horizon (days) |
| λ | Opportunity arrival rate (per year) |
| μ | Mean deal value |
| σ | Deal value standard deviation |
| p | Mean win probability |
| C | Total POC slots = N × pocs_per_se |

## Appendix B: Key Formulas

**Theoretical maximum throughput:**
```
Max POCs = C × (T / D)
Max Revenue = Max POCs × p × μ
```

**Effective capacity utilization:**
```
Utilization = (Completed POCs × D) / (C × T)
```

**Queue probability (Little's Law approximation):**
```
If arrival rate > service rate → queue builds
Service rate = C / D (POCs per day)
Arrival rate = λ / 365 (opportunities per day)
```
