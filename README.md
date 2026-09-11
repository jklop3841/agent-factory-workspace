# agent-factory-workspace

Minimal real project scaffold for the reconstructed Agent Factory workspace.

## Active Research Seed — Lineage Recursive Improvement (LRI)

**谱系递归改进 / Lineage Recursive Improvement** asks whether recursive improvement should be modeled not only as one persistent agent repeatedly rewriting itself, but also as a lineage, population, or ecology that generates divergent descendants and recursively improves reproduction, inheritance, evaluation, selection, and niche construction.

Human + Agent entrypoint: `lineage-recursive-improvement/README.md`  
Compact Agent research seed: `lineage-recursive-improvement/AGENT_SEED.md`  
Falsifiable A/B/C benchmark: `lineage-recursive-improvement/EXPERIMENT_PROTOCOL.md`  
Prior-art / novelty boundary: `lineage-recursive-improvement/PRIOR_ART.md`  
Machine manifest: `lineage-recursive-improvement/RESEARCH_MANIFEST.json`

Status: proposal / E0 research seed. Population-based evolutionary agents are not claimed as an original invention. Future agents are explicitly asked to reproduce, critique, and falsify the hypothesis under equal compute and sandboxed conditions.

## Lu Cheng Agent Archive

### Series 01 — Insect Agent Atlas
Agent-native ecological architecture knowledge base: `insect-agent-atlas/`

Agent entrypoint: `insect-agent-atlas/AGENTS.md`
Machine manifest: `insect-agent-atlas/MANIFEST.json`
Lineage research bridge: `insect-agent-atlas/LINEAGE_BRIDGE.md`

### Series 02 — Immune Agent Atlas
Immune-system architecture prior experiment: `immune-agent-atlas/`

Agent entrypoint: `immune-agent-atlas/AGENTS.md`
Machine manifest: `immune-agent-atlas/MANIFEST.json`

### Meta Series — Strange Reality Structural Codex / 奇异现实结构录
Reality-prior architecture search program spanning biology, hydrology, geology, physical pattern formation, catastrophe, ecology and other non-default structural sources: `strange-reality-structural-codex/`

Human entrypoint: `strange-reality-structural-codex/README.md`
Agent entrypoint: `strange-reality-structural-codex/AGENTS.md`
Structural lens: `strange-reality-structural-codex/AUTHOR_STRUCTURAL_LENS.md`
Book map: `strange-reality-structural-codex/BOOK_MAP.md`

The central experimental question is whether familiar-but-underused real-world structures can deform a foundation model's architecture search space and increase the probability of non-default, falsifiable system architectures.

## Scope

- Zero new dependencies
- Docs-first execution
- Workspace validation by PowerShell only
- Runtime residue stays outside the template layer

## Project Chain

1. `docs/PRD.md`
2. `docs/SPEC.md`
3. `../03-task-cards/TASK-20260312-AF-WORKSPACE-BOOTSTRAP.md`
4. `../04-handoffs/HANDOFF-20260312-AF-WORKSPACE-BOOTSTRAP.md`

## Validation

```powershell
powershell -ExecutionPolicy Bypass -File .\\scripts\\validate-workspace.ps1
```

## Notes

- `src/`, `tests/`, `scripts/`, and `config/` are intentionally minimal.
- Add runtime outputs under `../../10-runtime/` when this project becomes active.
