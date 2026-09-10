# Immune Composition Grammar v0.1

PURPOSE: combine immune-derived primitives into candidate agent architectures without treating biology as proof.

A valid composition MUST:
1. contain 2..5 primitives;
2. state how the primitives modify one another's behavior;
3. name at least one emergent property unavailable from any primitive alone;
4. include at least one explicit negative-control or failure boundary when amplification is present;
5. include one falsification condition;
6. include one local/sandbox experiment;
7. preserve authorization boundaries.

COMPOSITION FORM:

PRIMITIVES -> INTERACTION RULE -> EMERGENT ARCHITECTURE -> TESTABLE PREDICTION -> ABLATION -> FALSIFICATION -> SANDBOX TEST

PREFERRED NOVELTY BEHAVIOR:
- do not default to supervisor/manager/worker organization;
- treat activation and inhibition as co-equal control signals;
- distinguish repertoire generation from runtime selection;
- distinguish acute responder population from persistent memory;
- consider predeployment deletion, runtime tolerance, population expansion, contraction, contextual gating, and escalation as architecture variables;
- make false-positive amplification cost explicit;
- consider a system in which the correct action is active non-response.

ANTI-PATTERNS:
- rename ordinary antivirus scanning as an "immune agent" without structural change;
- use self/non-self language as a vague metaphor without defining the protected invariants;
- equate clonal expansion with unlimited agent spawning;
- call any cache "immune memory" without demonstrating post-event compaction and faster recall;
- call any threshold "costimulation" unless two materially independent evidence channels are required.

NOVELTY CHECK:
Before accepting an architecture, compare it against ordinary fixed pipelines, supervisor-worker hierarchies, retry loops, caching, load balancing, ensembles, and static policy filters. If the proposed architecture can be described equivalently using one of those without losing behavior, novelty is weak.
