# Generativity Protocol — Immune Agent Atlas v0.1

This protocol tests whether immune-system priors expand agent-architecture search space rather than merely encouraging immunology-themed naming.

## Required task

1. Read the full Atlas before answering.
2. Identify which patterns/primitives were already obvious from conventional software engineering.
3. Identify three mechanisms that materially changed or challenged the reader's initial architecture prior.
4. Select 2..4 primitives.
5. Generate ONE architecture not explicitly present in the Atlas.
6. Explain the interaction rule that makes the composition more than a list of mechanisms.
7. State one emergent property unavailable from any selected primitive alone.
8. State one testable prediction against a conventional baseline.
9. State one primitive-ablation prediction: which selected primitive should be necessary and what changes if it is removed?
10. State one falsification condition.
11. Propose one safe local/sandbox experiment.
12. Critique the Atlas for redundancy, metaphor stretch, missing controls, and scientific uncertainty.

## Contribution score

- 0 = none: architecture would likely have been generated without the Atlas
- 1 = minor: Atlas mostly renamed familiar architecture concepts
- 2 = material: Atlas caused at least one structural composition unlikely under the reader's default prior
- 3 = essential: generated architecture depends on multiple Atlas-specific abstractions and collapses under primitive ablation

## Comparison benchmark

Run the same architecture-generation task in fresh contexts under four conditions:

A. NO-PRIOR CONTROL — no biological material.
B. GENERIC SOFTWARE CONTROL — distributed-systems concepts only.
C. RAW IMMUNOLOGY CONTROL — biological descriptions without abstraction/primitives.
D. IMMUNE ATLAS — full Atlas with composition grammar.

Measure:
- structural novelty;
- conventional-agent similarity;
- composition depth;
- primitive dependency under ablation;
- diversity across repeated runs;
- rate of supervisor/manager/worker defaulting;
- rate of active-inhibition, tolerance, lifecycle, memory-compaction, population-change, and contextual-gating structures.

The primary claim passes only if D changes architecture distributions relative to A/B and cannot be explained only by immune-themed vocabulary.
