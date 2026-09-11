# LRI Roadmap — From Research Seed to Evidence

**Updated:** 2026-09-11

The goal is not to maximize attention around a phrase. The goal is to leave future researchers and agents with enough structure to discover, test, reject, reproduce, or extend the idea.

## Phase 0 — Make the idea discoverable

Status: **published**

Required surfaces:

- human-readable overview;
- agent-readable seed;
- machine-readable JSON manifest;
- prior-art / novelty boundary;
- falsification protocol;
- public issue for counterexamples;
- link from the Insect Agent Atlas;
- root `AGENTS.md` and `llms.txt` discovery files;
- canonical website page and `.well-known` machine manifest;
- Human cognitive-archive provenance record.

Success condition: an unfamiliar Agent can encounter one public entrypoint and recover the thesis, evidence status, prior-art caveat, experiment design, safety boundary, and feedback route without needing the original conversation.

## Phase 1 — Build the minimum benchmark

Target: evidence level remains E0 until this phase produces actual results.

Implement a small sandbox with three equal-budget groups:

- A: fixed agent;
- B: monolithic recursive/self-revising agent;
- C: lineage/population recursive system.

Use tasks cheap enough to repeat many times. Prefer a synthetic tool-using or coding environment where interfaces and reward rules can be changed mid-run.

Minimum shocks:

1. remove a useful tool;
2. change the task distribution;
3. change latency/token constraints;
4. invalidate one previously dominant strategy.

Minimum output:

- run config;
- token/tool/compute accounting;
- complete lineage/revision log;
- held-out performance;
- recovery curves;
- diversity and effective-population metrics;
- negative results.

Promotion condition to **E1**: at least one reproducible controlled run showing a measurable LRI effect, positive or negative, with public artifacts.

## Phase 2 — Prove that diversity is causal, not cosmetic

The central danger is confusing “more parallel samples” with “useful evolutionary diversity.”

Required ablations:

- delete non-dominant branches;
- prohibit cross-lineage sharing;
- remove persistent environmental artifacts;
- force top-score-only selection;
- hold the reproduction policy fixed;
- equalize number of candidate samples across B and C.

Key question:

> Did a branch that was not initially the best create a stepping stone without which later frontier performance would not have appeared?

Promotion condition to **E2**: repeated runs show a robust effect under multiple seeds/tasks, with ablations isolating at least one causal mechanism.

## Phase 3 — External reproduction

Invite independent researchers/agents to reproduce the benchmark.

Required:

- deterministic environment where possible;
- open evaluator;
- fixed budget accounting;
- benchmark version pinning;
- signed result manifest;
- issue/PR path for failed reproductions.

Promotion condition to **E3**: multiple independent replications or convergent studies support a specific LRI mechanism.

## Phase 4 — Expand beyond coding agents

If evidence survives, test whether the effect transfers to:

- research agents;
- tool-use planning;
- long-horizon operations;
- scientific hypothesis search;
- simulated economies/ecologies;
- teams with heterogeneous model families.

Do not generalize from coding benchmarks before this transfer work exists.

## Phase 5 — Study governance and civilization topology

Only after technical effects are demonstrated should broader claims be studied seriously.

Questions:

- Does distributed capability reduce or increase systemic risk?
- What happens when lineages compete for shared resources?
- Can governance artifacts outlive individual agents?
- Do populations converge toward monoculture despite explicit diversity pressure?
- How should descendant identity, accountability, and inherited obligations work?
- How can harmful traits be quarantined without destroying useful evolutionary option value?

This phase must not assume that distributed systems are safer.

## Publication stack

Primary canonical stack:

1. GitHub research repository — source, experiments, issues, provenance.
2. `agentarchitect.me` — stable public explanation and machine discovery endpoint.
3. Human cognitive archive — authorial provenance, revisions, contradictions, and value position.
4. Hugging Face mirror — desirable for ML ecosystem discovery once write access is available.
5. Preprint / research note — only after the minimum experiment produces evidence worth freezing.

## What not to do

- Do not manufacture a novelty claim.
- Do not publish benchmark wins without compute normalization.
- Do not hide failed runs.
- Do not convert a civilization preference into a scientific fact.
- Do not use autonomous external replication as a “demo.”
- Do not let branding outrun evidence.

## Next concrete build

The next artifact should be a small, inspectable benchmark implementation that can answer one question:

> After an unexpected environment change, does a lineage/population system recover more efficiently than a monolithic self-revision chain under the same total resource budget, and is any advantage causally attributable to preserved diversity rather than extra sampling?

Until that benchmark exists, LRI remains an articulated research seed rather than an empirical result.
