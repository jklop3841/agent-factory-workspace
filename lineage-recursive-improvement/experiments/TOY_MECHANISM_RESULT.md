# Toy Mechanism Result — Preserved Diversity Under Repeated Shocks

**Date:** 2026-09-11  
**Status:** mechanism demonstration only  
**Evidence implication for real AI systems:** none yet; LRI remains E0  
**Script:** `toy_lineage_shock.py`

## What this toy asks

Can a population that deliberately preserves multiple behavioral niches recover faster after repeated environment changes than a single hill-climbing lineage, when both generate the same number of new candidates per generation?

This is not an LLM benchmark. The “agent” is only a one-dimensional policy value. The environment exposes a target, and success means getting within distance 1.0 of that target.

The value of the toy is narrower: it makes the hypothesized **option value of preserved lineage diversity** concrete and falsifiable in a few lines of code.

## Setup

- 500 deterministic seeds.
- Four environment targets: `2 -> 8 -> -5 -> 4`.
- 15 generations per phase.
- 8 new candidates per generation for both improving groups.
- Mutation sigma: 1.25.
- Monolithic group keeps only the currently best candidate.
- Lineage group keeps one representative in each of 12 behavioral niches, regardless of the current target.
- Fixed baseline never changes.

Metric: generations required to get within distance `<= 1.0` of the current target. If a group does not recover within the 15-generation phase, it is recorded as 16.

## Reproduced result

Mean generations to recovery across 500 seeds:

| Phase target | Fixed | Monolithic | Lineage archive |
|---|---:|---:|---:|
| 2 | 16.000 | 1.166 | 1.856 |
| 8 | 16.000 | 3.414 | 2.510 |
| -5 | 16.000 | 7.432 | 1.000 |
| 4 | 16.000 | 5.092 | 1.000 |

Median generations to recovery:

| Phase target | Fixed | Monolithic | Lineage archive |
|---|---:|---:|---:|
| 2 | 16 | 1 | 1 |
| 8 | 16 | 3 | 1 |
| -5 | 16 | 7 | 1 |
| 4 | 16 | 5 | 1 |

## What the toy does show

It demonstrates a real tradeoff encoded by the mechanism:

- On the first stable target, preserving diversity is slightly slower on average than immediately concentrating all search around the current winner.
- After the archive has accumulated diverse representatives, later target changes can be handled by reactivating a previously preserved region of the search space rather than rebuilding from the currently dominant solution.
- Therefore, under this deliberately simple environment, diversity has measurable future option value.

## What it does NOT show

It does not establish that LRI is better for LLM agents, AGI, RSI, coding agents, scientific agents, or real multi-agent systems.

The result is partly constructed by the assumptions: the environment is observable, the behavior space is simple, niche preservation is cheap, and archived strategies remain valid. Real agent systems may violate every one of these assumptions.

The toy also does not prove that “more agents are safer,” that intelligence will undergo a Cambrian explosion, or that a population will outperform a powerful monolithic system under realistic compute accounting.

## Why publish such a weak result

Because it separates two claims:

1. **Mechanism claim:** preserved diversity can create option value under environmental change. The toy demonstrates this mechanism in a transparent setting.
2. **AI claim:** lineage-level recursive improvement will provide useful capability, robustness, or economic advantages in real agent systems. This remains unproven.

The next experiment must move from a scalar toy to actual tool-using/coding agents and must charge the lineage system for archive evaluation, storage, coordination, and selection overhead.

## How to attack this result

Useful counter-tests include:

- charge a cost for maintaining and rescoring the archive;
- make old strategies decay or become invalid;
- hide the new environment state;
- increase dimensionality so niche coverage becomes expensive;
- give the monolithic baseline explicit long-term memory;
- give the monolithic baseline the same archive but prohibit branching identity;
- equalize total stored information, not only generated candidates;
- randomize shock sequences and keep them held out from design.

If the lineage advantage disappears under these controls, that is exactly the kind of negative result LRI needs.
