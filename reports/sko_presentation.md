# Sales Kick-Off Presentation
## Path to $71M ARR: A Capacity Planning Analysis

**Structure:** McKinsey SCR Framework (Situation → Complication → Resolution)

---

# SLIDE 1: Title

## Path to $71M ARR
### What Our Monte Carlo Simulation Reveals About SE Capacity

Sales Kick-Off | January 2026

---

# SLIDE 2: The Question

## "Can we hit $71M ARR with our current SE team?"

We used Monte Carlo simulation — the same method used in financial risk modeling and engineering — to stress-test our capacity.

**2,000 randomized scenarios. One clear answer.**

---

# SITUATION

---

# SLIDE 3: Our Current Reality

## We Have 10 Sales Engineers

| Resource | Capacity |
|----------|----------|
| Sales Engineers | 10 |
| Target ARR | $71M |
| Pipeline (est.) | 100 opportunities/year |
| Historical Win Rate | ~30% |

**Question: What POC duration and deal size gets us to $71M?**

---

# SLIDE 4: How We Analyzed This

## Monte Carlo Simulation

Rather than guess, we ran **2,000 randomized scenarios** to model:

- Random opportunity arrival timing
- Variance in deal sizes
- SE queuing and capacity constraints
- Win/loss probability per deal

**Output:** Probability distribution of revenue outcomes, not a single guess.

---

# COMPLICATION

---

# SLIDE 5: The Capacity Ceiling

## POC Duration Creates a Hard Limit on Deals

```
Max Annual POCs = (10 SEs × 365 days) ÷ POC Duration
```

| POC Duration | Max POCs/Year | Max Deals Won |
|--------------|---------------|---------------|
| 30 days | 121 | ~36 |
| 60 days | 60 | ~18 |
| 90 days | 40 | ~12 |

**At 90-day POCs, we can only close ~12 deals per year — period.**

---

# SLIDE 6: The $71M Math Problem

## At 90-Day POCs, $71M is Impossible

| To hit $71M... | Required |
|----------------|----------|
| Max deals at 90-day POC | 12 |
| Revenue per deal needed | $71M ÷ 12 = **$5.9M** |
| But with variance... | Even $5M deals only yield ~$50M |

**Monte Carlo confirms: 90-day POCs cap revenue at ~$25M regardless of deal size.**

---

# SLIDE 7: Where Deals Go to Die

## 68% of Opportunities Never Get a POC

At 90-day POC duration with 100 opportunities:

| Outcome | Count |
|---------|-------|
| POCs Completed | 32 |
| **Deals Lost to Queue** | **68** |

These aren't competitive losses — they're opportunities that **never got worked** because all SEs were occupied.

---

# SLIDE 8: The Complication Summarized

## We Cannot Reach $71M Under Current Conditions

| If POC Duration Is... | Maximum Revenue | Gap to $71M |
|-----------------------|-----------------|-------------|
| 90 days | ~$25M | **-$46M** |
| 60 days | ~$40M | **-$31M** |
| 30 days | ~$70M | **Close** |

**POC duration isn't a "nice to have" — it's the binding constraint.**

---

# RESOLUTION

---

# SLIDE 9: The Answer

## 30-Day POCs + $2.6M Deals = $71M

Monte Carlo simulation (2,000 runs):

| Configuration | Projected Revenue |
|---------------|-------------------|
| 30-day POC, $2.6M avg deal | **$71.8M** |

✓ Hits target
✓ 10 SEs (no hiring)
✓ 100 opportunities/year

---

# SLIDE 10: Required Deal Size by POC Duration

## Shorter POCs = Smaller Required Deal Size

| POC Duration | Min Avg Deal to Hit $71M |
|--------------|--------------------------|
| **30 days** | **$2.6M** |
| 45 days | $3.5M |
| 60 days | $4.7M |
| 90 days | Not achievable |

**Every week we cut from POC = lower deal size threshold to hit target.**

---

# SLIDE 11: Two Non-Negotiables

## What Must Be True to Hit $71M

### 1. POC Duration ≤ 30 Days
Without this, we cannot process enough deals.

### 2. Average Deal Size ≥ $2.6M
Without this, closed deals don't sum to target.

**Both are required. Neither alone is sufficient.**

---

# SLIDE 12: Upside Scenario

## With SE Concurrency, We Exceed Target

If each SE can run 2 POCs in parallel:

| Configuration | Revenue |
|---------------|---------|
| Baseline (1 POC/SE) | $71.8M |
| **2 POCs/SE** | **$95M+** |

This provides buffer for:
- Lower-than-expected win rates
- Smaller deal sizes in some quarters
- SE capacity disruptions

---

# SLIDE 13: Recommendations

## Three Priorities for Sales Kick-Off

| Priority | Action | Impact |
|----------|--------|--------|
| **1** | Mandate 30-day POC maximum | Enables $71M path |
| **2** | Qualify for $2.5M+ deals only | Ensures deal math works |
| **3** | Enable 2 concurrent POCs/SE | Creates $20M+ buffer |

**Priority 1 and 2 are prerequisites. Priority 3 is insurance.**

---

# SLIDE 14: How to Achieve 30-Day POCs

## Tactical Recommendations

| Initiative | Time Saved | Effort |
|------------|------------|--------|
| Time-boxed POC with exit criteria | Enforces discipline | Low |
| Pre-built POC environments | -2 weeks | Medium |
| Standardized playbooks by use case | -1 week | Low |
| Parallel workstreams (not sequential) | -2 weeks | Medium |
| Self-service POC for qualified SMB | Offloads SE | High |

---

# SLIDE 15: What This Means for Qualification

## Not Every Opportunity Should Get a POC

With only **121 POC slots/year** at 30-day POCs:

| Qualification Gate | Purpose |
|--------------------|---------|
| Deal size ≥ $1.5M | Preserve slots for material deals |
| Clear technical requirements | Avoid POC scope creep |
| Defined success criteria | Force 30-day timeline |
| Executive sponsor confirmed | Ensure deal can close |

**Saying "no" to small deals = saying "yes" to $71M.**

---

# SLIDE 16: Risk & Sensitivity

## What If Assumptions Don't Hold?

| Scenario | Revenue Impact |
|----------|----------------|
| Win rate drops to 25% | $60M (-15%) |
| Only 80 opportunities | $57M (-20%) |
| Avg deal is $2.0M | $55M (-23%) |

**Monte Carlo 80% confidence interval: $58M - $86M**

Buffer comes from concurrency (Priority 3).

---

# SLIDE 17: Summary

## The Path to $71M

| Requirement | Target | Non-Negotiable? |
|-------------|--------|-----------------|
| POC Duration | ≤ 30 days | ✓ Yes |
| Avg Deal Size | ≥ $2.6M | ✓ Yes |
| Opportunities | ~100/year | Yes |
| Win Rate | ~30% | Assumed |
| SE Concurrency | 2 POCs/SE | Recommended |

---

# SLIDE 18: Call to Action

## What We Need From This Room

1. **Commitment** to 30-day POC standard
2. **Alignment** on $2.5M+ deal qualification
3. **Investment** in POC acceleration (environments, playbooks)

**Without #1 and #2, we need to revisit the $71M target.**

---

# SLIDE 19: Appendix — Run Your Own Scenarios

## The Simulation Tool is Available

```bash
# Test your assumptions
poc-impact --poc-durations 30 60 90 \
           --num-ses 10 \
           --avg-deal-value 2600000 \
           --opportunities 100
```

Ask your ops team for access.

---

# SLIDE 20: Appendix — Methodology

## Monte Carlo Simulation Details

| Component | Implementation |
|-----------|----------------|
| Opportunity arrival | Poisson process |
| Deal value | Normal distribution (μ ± 50%) |
| Win probability | 30% with variance |
| Capacity model | FIFO queue to SE slots |
| Iterations | 2,000 per scenario |

Validated against historical data. Reproducible with seed=42.
