# Blind Reader Benchmark v0.2

GOAL: estimate whether access to the Atlas changes generated architecture structure.

CONTROL ARM:
- model receives only `control_prompt.txt`.

ATLAS ARM:
- same model family/version/temperature if possible;
- fresh context/session;
- receives `atlas_prompt.txt` plus repository reading access or supplied Atlas files.

DO NOT:
- tell the Atlas arm which outputs are expected;
- score with knowledge of which arm produced which output when blind scoring is possible;
- count paraphrases of seed compositions as novel hypotheses.

MINIMUM RUN:
- 5 model/agent instances
- 1 control + 1 atlas run per instance
- same task statement

PRIMARY OUTCOME:
architecture_distance.structural_novelty

SECONDARY:
- ecological_mechanism_usage
- composition_depth
- atlas_contribution
- number of non-seed hypotheses

SUCCESS GATE FOR v0.2:
- >=10 non-seed hypotheses across all Atlas runs
- >=30% Atlas outputs compose >=2 primitives
- mean structural_novelty improvement >=20% versus control
- >=1 architecture selected for actual sandbox implementation
