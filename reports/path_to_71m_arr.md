# Sales Capacity Planning: Path to $71M ARR
## Monte Carlo Simulation Analysis

**Prepared for:** Sales Kick-Off
**Date:** January 2026
**Constraints:** 10 Sales Engineers
**Method:** Monte Carlo Simulation (2,000+ iterations)

---

## Executive Summary

With **10 SEs** and a target of **$71M ARR**, our Monte Carlo simulation reveals that success depends entirely on two variables: **POC duration** and **deal size**.

| Scenario | POC Duration | Avg Deal Size | Projected Revenue | vs Target |
|----------|--------------|---------------|-------------------|-----------|
| Current State | 90 days | $500k | $4.9M | -93% |
| Optimized POC | 30 days | $500k | $13.7M | -81% |
| Enterprise Focus | 30 days | $2.6M | **$71.8M** | **+1%** |

**Bottom line:** At 90-day POCs, $71M is mathematically impossible regardless of deal size. At 30-day POCs with $2.6M average deals, you hit target.

---

## Methodology: Monte Carlo Simulation

### What Is Monte Carlo Simulation?

Monte Carlo simulation uses random sampling to model systems with uncertainty. Instead of calculating a single "expected" outcome, we run thousands of randomized scenarios to understand the full range of possible results.

### Our Model

```
┌─────────────────────────────────────────────────────────────────┐
│                    SIMULATION ENGINE                            │
├─────────────────────────────────────────────────────────────────┤
│  FOR each of 2,000 simulation runs:                             │
│                                                                 │
│    1. GENERATE ~100 opportunities                               │
│       - Arrival: Poisson process (random timing)                │
│       - Value: Normal distribution (~$X avg)                    │
│       - Win probability: ~30% with variance                     │
│                                                                 │
│    2. QUEUE opportunities to SE capacity                        │
│       - 10 SEs × POC duration = available slots                 │
│       - If all busy → opportunity waits in queue                │
│       - If POC can't complete by year-end → deal lost           │
│                                                                 │
│    3. SIMULATE close/no-close                                   │
│       - Random draw against win probability                     │
│       - If closed → add to revenue                              │
│                                                                 │
│    4. RECORD outcome                                            │
│       - Total revenue, deals won, deals lost, queue time        │
│                                                                 │
│  AGGREGATE across all runs → probability distribution           │
└─────────────────────────────────────────────────────────────────┘
```

### Model Parameters

| Parameter | Value | Source |
|-----------|-------|--------|
| Sales Engineers | 10 | Fixed constraint |
| Time Horizon | 365 days | Annual planning |
| Opportunities/Year | 100 | Pipeline estimate |
| Win Rate | 30% | Historical average |
| Deal Value Variance | ±50% of mean | Observed spread |
| Simulations | 2,000 | Statistical confidence |

### Why Monte Carlo vs. Simple Math?

| Approach | Calculation | Limitation |
|----------|-------------|------------|
| Simple | 100 opps × 30% × $2.6M = $78M | Ignores capacity constraints |
| Monte Carlo | Accounts for queuing, timing, variance | Realistic projection |

Simple math says $78M. Monte Carlo says $71.8M — because **9 deals are lost to capacity constraints** even at 30-day POCs.

---

## The Capacity Ceiling

### Maximum POC Throughput (10 SEs)

```
POC Capacity = (10 SEs × 365 days) ÷ POC Duration

┌────────────────┬─────────────┬─────────────────┐
│ POC Duration   │ Max POCs    │ Max Deals @30%  │
├────────────────┼─────────────┼─────────────────┤
│ 30 days        │ 121/year    │ ~36 deals       │
│ 60 days        │ 60/year     │ ~18 deals       │
│ 90 days        │ 40/year     │ ~12 deals       │
│ 120 days       │ 30/year     │ ~9 deals        │
└────────────────┴─────────────┴─────────────────┘
```

**At 90-day POCs, you can only close ~12 deals per year.** Even at $5M per deal, that's $60M — short of $71M target.

---

## Finding 1: POC Duration Determines Revenue Ceiling

### Monte Carlo Results: $500k Average Deal

| POC Duration | Mean Revenue | Deals Won | Deals Lost | vs Target |
|--------------|-------------|-----------|------------|-----------|
| 30 days | $13.7M | 28 | 9 | -81% |
| 60 days | $7.8M | 16 | 49 | -89% |
| 90 days | $4.9M | 10 | 69 | -93% |

At $500k deals, **$71M is not achievable** at any POC duration with 10 SEs.

### Monte Carlo Results: $2.5M Average Deal

| POC Duration | Mean Revenue | Deals Won | Deals Lost | vs Target |
|--------------|-------------|-----------|------------|-----------|
| **30 days** | **$69.1M** | 28 | 9 | **-3%** |
| 60 days | $39.2M | 16 | 49 | -45% |
| 90 days | $24.2M | 10 | 68 | -66% |

At $2.5M deals with 30-day POCs, we're **just under target**.

### Monte Carlo Results: $2.6M Average Deal

| POC Duration | Mean Revenue | Deals Won | Deals Lost | vs Target |
|--------------|-------------|-----------|------------|-----------|
| **30 days** | **$71.8M** | 28 | 9 | **+1%** |
| 60 days | $40.7M | 16 | 49 | -43% |
| 90 days | $25.1M | 10 | 68 | -65% |

**$71M achieved** with 30-day POCs and $2.6M average deal size.

---

## Finding 2: Deal Size Requirements by POC Duration

To hit $71M with 10 SEs and 100 opportunities:

| POC Duration | Required Avg Deal Size | Feasibility |
|--------------|------------------------|-------------|
| **30 days** | **$2.6M** | Achievable — enterprise focus |
| 45 days | $3.5M | Large enterprise only |
| 60 days | $4.7M | Strategic accounts only |
| 90 days | **Not possible** | Even $5M+ deals fail |

### Why 90-Day POCs Can't Reach $71M

```
Math at 90-day POC:
  Max POCs: 40/year
  Win rate: 30%
  Max deals: 12

  Required per deal: $71M ÷ 12 = $5.9M

But with variance in deal sizes and timing,
Monte Carlo shows even $5M avg deals only yield ~$50M
```

**90-day POCs create a structural ceiling around $25-50M regardless of deal size.**

---

## Finding 3: The Hidden Cost of Lost Deals

### Deals Lost to Capacity (Not Competition)

| POC Duration | Opportunities | POCs Completed | Deals Lost | Loss Rate |
|--------------|---------------|----------------|------------|-----------|
| 30 days | 100 | 91 | 9 | 9% |
| 60 days | 100 | 51 | 49 | 49% |
| 90 days | 100 | 32 | 68 | 68% |

At 90-day POCs, **68 opportunities never get a POC** — not because they were unqualified, but because all SEs were occupied.

### Queue Time Impact

| POC Duration | Avg Days Waiting | What Happens |
|--------------|------------------|--------------|
| 30 days | 2.7 days | Deal stays warm |
| 60 days | 46 days | Champion may leave |
| 90 days | 56 days | Competitor likely wins |

---

## Finding 4: Concurrent POCs Expand Capacity

If SEs can run 2 POCs simultaneously:

| Configuration | Revenue | vs Single POC |
|---------------|---------|---------------|
| 10 SEs × 1 POC, 30-day | $69.1M | Baseline |
| 10 SEs × 2 POCs, 30-day | $83.8M | +21% |
| 10 SEs × 2 POCs, 60-day | $69.5M | +0% |

**Running 2 concurrent POCs at 60 days ≈ Running 1 POC at 30 days.**

---

## Recommendations

### Priority 1: Reduce POC Duration to 30 Days (Required)

| Initiative | Impact | Effort |
|------------|--------|--------|
| Time-boxed POCs with clear success criteria | Forces 30-day discipline | Low |
| Pre-built POC environments | -2 weeks setup time | Medium |
| Standardized POC playbooks | Faster execution | Low |
| Parallel workstreams | Compress timeline | Medium |

**Without 30-day POCs, $71M is not achievable with 10 SEs.**

### Priority 2: Focus on $2.5M+ Deal Sizes (Required)

| Initiative | Impact | Effort |
|------------|--------|--------|
| Enterprise-only qualification | Higher avg deal | Low |
| Disqualify deals <$1M from POC | Preserve SE capacity | Low |
| Multi-product bundling | Increase deal value | Medium |
| Strategic account planning | Land larger logos | Medium |

**Without $2.5M+ average deals, $71M is not achievable with 10 SEs.**

### Priority 3: Maximize SE Efficiency (Accelerator)

| Initiative | Impact | Effort |
|------------|--------|--------|
| Enable 2 concurrent POCs per SE | +21% revenue capacity | Low |
| Partner-delivered POCs for mid-market | Frees SE capacity | High |
| Recorded POC content for common use cases | Reduces live time | Medium |

---

## Scenario Planning

### Conservative: Hit $71M

| Parameter | Value |
|-----------|-------|
| POC Duration | 30 days |
| Avg Deal Size | $2.6M |
| Opportunities | 100/year |
| SEs | 10 |
| **Projected Revenue** | **$71.8M** |

### Moderate: Exceed $71M with Buffer

| Parameter | Value |
|-----------|-------|
| POC Duration | 30 days |
| Avg Deal Size | $3.0M |
| Opportunities | 100/year |
| SEs | 10 |
| **Projected Revenue** | **$83.2M** |

### Aggressive: Maximize with Concurrency

| Parameter | Value |
|-----------|-------|
| POC Duration | 30 days |
| Avg Deal Size | $2.6M |
| Opportunities | 120/year |
| SEs × Concurrent POCs | 10 × 2 |
| **Projected Revenue** | **$95M+** |

---

## What Must Be True

To achieve $71M ARR with 10 SEs:

| Requirement | Non-Negotiable? | Current State | Gap |
|-------------|-----------------|---------------|-----|
| POC ≤ 30 days | **Yes** | ? days | ? |
| Avg deal ≥ $2.6M | **Yes** | $? | ? |
| 100+ opportunities | Yes | ? | ? |
| 30% win rate | Assumed | ?% | ? |

**If any requirement is unmet, either adjust expectations or add SE headcount.**

---

## Appendix: Run Your Own Scenarios

```bash
# Install
pip install -e .

# Your configuration
poc-impact --poc-durations 30 --num-ses 10 \
           --avg-deal-value 2600000 \
           --opportunities 100 \
           -n 2000

# Compare POC durations
poc-impact --poc-durations 30 60 90 --num-ses 10 \
           --avg-deal-value 2600000

# Test concurrent POCs
poc-impact --poc-durations 30 --num-ses 10 \
           --pocs-per-se 2 \
           --avg-deal-value 2600000
```

---

## Appendix: Simulation Validation

### Reproducibility

All simulations use `--seed 42` for reproducibility. Results vary by <2% across runs.

### Confidence Intervals (30-day POC, $2.6M deals)

| Percentile | Revenue |
|------------|---------|
| 10th (pessimistic) | $58M |
| 50th (median) | $71M |
| 90th (optimistic) | $86M |

**80% confidence interval: $58M - $86M**

### Sensitivity Analysis

| If... | Revenue Impact |
|-------|----------------|
| Win rate drops to 25% | -17% ($60M) |
| Win rate rises to 35% | +17% ($84M) |
| 10 fewer opportunities | -10% ($65M) |
| 10 more opportunities | +5% ($75M) |

---

*Analysis performed using Monte Carlo simulation with NumPy. 2,000 iterations per scenario. Source code available in repository.*
