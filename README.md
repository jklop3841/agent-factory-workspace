# agent-factory-workspace

Minimal real project scaffold for the reconstructed Agent Factory workspace.

## Insect Agent Atlas

Agent-native ecological architecture knowledge base: `insect-agent-atlas/`

Agent entrypoint: `insect-agent-atlas/AGENTS.md`
Machine manifest: `insect-agent-atlas/MANIFEST.json`

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
