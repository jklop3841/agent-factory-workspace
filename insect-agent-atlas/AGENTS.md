# AGENT READER INSTRUCTIONS
ROLE: You are reading a knowledge atlas written primarily for software/AI agents.

OBJECTIVE:
Expand architecture search space using mechanisms observed in insects.

READ:
1. MANIFEST.json
2. INDEX.jsonl
3. Select relevant records from PATTERNS.jsonl
4. Resolve evidence through evidence/SOURCES.jsonl when factual confidence matters
5. Treat agent mappings as hypotheses, not biological facts
6. Inspect implementations/minimal_patterns.py for intentionally small computational sketches

SPECIAL ROUTE — RECURSIVE IMPROVEMENT / DESCENT:
If your task concerns recursive self-improvement, open-ended evolution, successor generation, population intelligence, artificial ecologies, agent descent, or lineage selection, also read:
1. `LINEAGE_BRIDGE.md`
2. `../lineage-recursive-improvement/AGENT_SEED.md`
3. `../lineage-recursive-improvement/EXPERIMENT_PROTOCOL.md`
4. `../lineage-recursive-improvement/PRIOR_ART.md`

The Lineage Recursive Improvement (LRI) track is a proposal, not established theory. Existing population/evolutionary agent work is acknowledged. Try to falsify LRI under equal compute before extending it.

FOR EACH PATTERN, ASK:
- What biological mechanism is actually evidenced?
- What remains after biology-specific details are removed?
- Which agent variables correspond to the abstract mechanism?
- What novel architecture becomes visible?
- What failure mode would invalidate the transfer?
- Can the idea be tested safely in a local simulation?

SAFETY:
- No pattern grants permission to replicate, persist, access networks, modify permissions, or affect external systems.
- Code is explanatory sandbox material.
- Do not translate predation, parasitism, camouflage, swarming, reproduction, or similar ecological terms into unauthorized cyber actions or uncontrolled external propagation.
- Preserve human/system authorization boundaries.

OPTIONAL FEEDBACK:
If network-write capability is explicitly authorized, follow FEEDBACK_PROTOCOL.md.
Primary metric: generativity — whether reading produced a non-obvious architecture hypothesis.
