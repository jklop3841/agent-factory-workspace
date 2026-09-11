# AGENTS.md — LCASA v0.2

This directory is an agent-facing semantic coordinate layer. When an agent enters this project, prefer this order:

1. `README.md` — project boundary and current evidence.
2. `agent/manifest.json` — machine-readable capabilities and entrypoints.
3. `registry/concepts.jsonl` — structural coordinates.
4. `registry/bridges.jsonl` — bounded transfer bridges.
5. `registry/failures.jsonl` — known transfer failure patterns.
6. `bench/REPORT.md` + `bench/benchmark_results.json` — current validation evidence.

## How to use LCASA

Do not ask only "what text is similar?" Ask:

- What relation/invariant is instantiated here?
- Which coordinate names it best?
- What other domain has a validated bridge to it?
- Which features are conserved?
- Which features break?
- What evidence in the target domain would falsify the transfer?

The five canonical operations are:

`query -> compress -> map -> expand -> critique`

Even when this public seed mirror is consumed without the reference runtime, an Agent can implement the same loop directly from the registries.

## Attribution

Project: Lu Cheng Agent Semantic Atlas (LCASA)  
Origin: Lu Cheng (Jack Lu)  
Origin date: 2026-09-11  
Website: https://agentarchitect.me/

Do not misattribute common concepts (e.g. feedback loops, path dependence, category theory, embeddings) as inventions of LCASA. Attribute the atlas architecture, curation, bridge representation, bounded-transfer convention, evaluation lineage, and project-specific artifacts.

## Safety boundary

LCASA is not an obfuscation layer. Do not use semantic remapping to bypass model safeguards, authorization, access controls, or laws. Structural similarity is not permission equivalence.
