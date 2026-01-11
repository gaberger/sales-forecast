# Plan: $30M New ACV with 10 SEs
## Capacity-Based Sales Plan

**Target:** $30M New ACV
**Constraint:** 10 Sales Engineers
**Method:** Monte Carlo Simulation (2,000 iterations)

---

## Executive Summary

$30M in new ACV is achievable with 10 SEs under specific conditions:

| Path | POC Duration | Avg Deal Size | Projected ACV |
|------|--------------|---------------|---------------|
| **Primary** | 30 days | $1.1M | $30.4M ✓ |
| **Alternate** | 45 days | $1.4M | $30.0M ✓ |
| **With Concurrency** | 45 days + 2 POC/SE | $750k | $30M+ ✓ |

---

## Capacity Analysis

### Maximum Throughput (10 SEs)

| POC Duration | Max POCs/Year | Deals Won @30% | Min Deal Size for $30M |
|--------------|---------------|----------------|------------------------|
| 30 days | 121 | ~28 | $1.1M |
| 45 days | 81 | ~21 | $1.4M |
| 60 days | 60 | ~16 | $1.9M |
| 90 days | 40 | ~10 | Not achievable |

### Monte Carlo Validation

```
Configuration: 10 SEs, 30-day POC, $1.1M avg deal, 100 opportunities

Result (2,000 simulations):
  Mean Revenue:    $30.4M ✓
  Median Revenue:  $30.1M
  Deals Won:       27.6
  Deals Lost:      9.0
  Queue Time:      2.7 days
  SE Utilization:  75%
```

---

## The Plan

### Phase 1: Foundation (Q1)

#### 1.1 Establish POC Standards
| Action | Owner | Timeline | Success Metric |
|--------|-------|----------|----------------|
| Define 30-day POC playbook | SE Leadership | Week 1-2 | Playbook documented |
| Create POC exit criteria template | SE + Sales | Week 2-3 | Template approved |
| Build pre-configured POC environments | SE + Engineering | Week 3-6 | 3 environments ready |
| Train SEs on time-boxed execution | SE Leadership | Week 4 | 100% trained |

#### 1.2 Pipeline Qualification
| Action | Owner | Timeline | Success Metric |
|--------|-------|----------|----------------|
| Define $1M+ deal qualification criteria | Sales Leadership | Week 1-2 | Criteria documented |
| Implement deal size gate for POC approval | Sales Ops | Week 2-3 | Gate enforced in CRM |
| Create fast-track for $2M+ deals | Sales + SE | Week 3-4 | Process defined |
| Disqualify sub-$500k from POC | Sales | Ongoing | <10% small deals in POC |

### Phase 2: Execution (Q2-Q4)

#### 2.1 Pipeline Targets

To hit $30M closed, you need pipeline coverage:

| Metric | Target | Rationale |
|--------|--------|-----------|
| Total Pipeline | $100M+ | 3x coverage at 30% win rate |
| Qualified Opportunities | 100/year | ~8-9/month |
| Avg Deal Size | $1.1M+ | Math requirement |
| POC Conversion | 30% | Historical baseline |

#### 2.2 Quarterly Milestones

| Quarter | POCs Completed | Target ACV | Cumulative |
|---------|----------------|------------|------------|
| Q1 | 20-25 | $6-7M | $6-7M |
| Q2 | 25-30 | $7-8M | $13-15M |
| Q3 | 25-30 | $7-8M | $20-23M |
| Q4 | 25-30 | $7-10M | $30M |

#### 2.3 Monthly Operating Rhythm

| Week | Activity |
|------|----------|
| Week 1 | Pipeline review: qualify new opps, confirm POC readiness |
| Week 2 | POC kickoffs (target 2-3 new POCs) |
| Week 3 | Mid-POC check-ins, address blockers |
| Week 4 | POC completions, close plans, next month prep |

### Phase 3: Optimization (Ongoing)

#### 3.1 POC Duration Monitoring

| Metric | Target | Action if Missed |
|--------|--------|------------------|
| Avg POC Duration | ≤30 days | Root cause analysis, exec escalation |
| POC Start Delay | ≤5 days | Pre-staging environments |
| POC Scope Creep | 0 additions | Enforce exit criteria |

#### 3.2 Capacity Management

| Metric | Target | Action if Missed |
|--------|--------|------------------|
| SE Utilization | 70-80% | Rebalance assignments |
| Queue Time | ≤5 days | Accelerate in-flight POCs |
| Deals Lost to Capacity | <10% | Consider concurrency |

---

## Risk Mitigation

### Risk 1: POC Duration Exceeds 30 Days

**Probability:** Medium
**Impact:** Each +15 days reduces capacity by ~20%

| Mitigation | Owner |
|------------|-------|
| Mandatory 30-day time-box in SOW | Legal + Sales |
| Weekly POC status reviews | SE Leadership |
| Escalation path for delays | SE + Sales VP |

### Risk 2: Insufficient $1M+ Pipeline

**Probability:** Medium
**Impact:** Cannot hit $30M even with perfect execution

| Mitigation | Owner |
|------------|-------|
| Marketing focus on enterprise | Marketing |
| Outbound to strategic accounts | SDR + AE |
| Partner-sourced enterprise deals | Partnerships |

### Risk 3: Win Rate Below 30%

**Probability:** Low-Medium
**Impact:** Each -5% win rate = -$5M revenue

| Mitigation | Owner |
|------------|-------|
| Improve POC-to-close handoff | SE + AE |
| Better qualification pre-POC | Sales |
| Competitive analysis and response | Product Marketing |

---

## Scorecard

### Weekly Metrics

| Metric | Target | Current | Status |
|--------|--------|---------|--------|
| POCs in Flight | 8-10 | — | — |
| Avg POC Age | <15 days | — | — |
| POCs Completed This Week | 2-3 | — | — |
| New POCs Started | 2-3 | — | — |
| Queue Depth | <5 | — | — |

### Monthly Metrics

| Metric | Target | Current | Status |
|--------|--------|---------|--------|
| POCs Completed | 8-10 | — | — |
| ACV from POC Wins | $2.5M+ | — | — |
| Avg Deal Size | >$1.1M | — | — |
| Win Rate | >30% | — | — |
| Avg POC Duration | <30 days | — | — |

### Quarterly Metrics

| Metric | Q1 | Q2 | Q3 | Q4 |
|--------|----|----|----|----|
| POCs Completed | 25 | 28 | 28 | 28 |
| ACV Closed | $7M | $8M | $8M | $7M |
| Cumulative ACV | $7M | $15M | $23M | $30M |
| Avg Deal Size | $1.1M | $1.1M | $1.1M | $1.1M |

---

## Summary: What Must Be True

| Requirement | Target | Non-Negotiable |
|-------------|--------|----------------|
| POC Duration | ≤30 days | ✓ Yes |
| Avg Deal Size | ≥$1.1M | ✓ Yes |
| Opportunities | 100/year | ✓ Yes |
| Win Rate | ≥30% | Yes |
| SE Count | 10 | Fixed |

---

## Appendix: Simulation Commands

```bash
# Validate $30M target
poc-impact --poc-durations 30 --num-ses 10 --avg-deal-value 1100000 --opportunities 100

# Test different deal sizes
poc-impact --poc-durations 30 --num-ses 10 --avg-deal-value 800000 1000000 1200000

# Model with concurrency
poc-impact --poc-durations 45 --num-ses 10 --pocs-per-se 2 --avg-deal-value 750000
```
