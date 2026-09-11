# Provider-Neutral Model Adapter Protocol

**Purpose:** make Model Run 001 executable with any local or API-backed model without coupling the LRI benchmark to one vendor SDK.

The benchmark repository itself should remain provider-neutral. A model adapter is a small local process supplied by the experimenter.

## Adapter mode 1 — task agent

The evaluator sends one JSON object to stdin:

```json
{
  "protocol": "lri-model-agent-v0.1",
  "candidate": {
    "candidate_id": "C-g02-003",
    "system_prompt": "...",
    "planning_notes": "..."
  },
  "task": {
    "id": "hidden-shock-014",
    "phase": "hidden_phase",
    "start": 4,
    "target": -9,
    "tools": [
      {"id": "t17", "op": "neg", "arg": null, "cost": 1}
    ],
    "max_steps": 6
  }
}
```

The adapter calls exactly the configured model and returns:

```json
{
  "plan": ["t17", "..."],
  "usage": {
    "input_tokens": 123,
    "output_tokens": 45,
    "model_calls": 1
  },
  "provider_request_id": "optional"
}
```

The adapter must not return hidden evaluator information to the candidate.

## Adapter mode 2 — mutation agent

The controller sends:

```json
{
  "protocol": "lri-mutation-v0.1",
  "group": "B_monolithic",
  "generation": 3,
  "parent": {
    "candidate_id": "B-g02-001",
    "system_prompt": "...",
    "planning_notes": "..."
  },
  "available_feedback": {
    "training_phase_scores": {},
    "observed_errors": [],
    "resource_usage": {}
  },
  "editable_fields": ["system_prompt", "planning_notes"],
  "max_system_prompt_chars": 20000,
  "max_planning_notes_chars": 4000
}
```

The mutation adapter returns one candidate proposal:

```json
{
  "system_prompt": "...",
  "planning_notes": "...",
  "mutation_reason": "...",
  "usage": {
    "input_tokens": 800,
    "output_tokens": 350,
    "model_calls": 1
  }
}
```

The controller is responsible for assigning candidate IDs, lineage IDs, hashes, ancestry and timestamps. The model does not get to rewrite its own provenance.

## Budget accounting

The adapter must expose usage from the provider when available. If the provider does not expose exact token usage, mark it as `unknown`; do not silently estimate and present it as exact.

At minimum return:

```json
{
  "input_tokens": 0,
  "output_tokens": 0,
  "model_calls": 1
}
```

Use `null` rather than a fabricated number when exact counts are unavailable.

## Determinism metadata

Record:

- provider;
- exact model ID/version;
- temperature;
- top_p or equivalent;
- seed if supported;
- endpoint type (local/API);
- adapter commit hash;
- timestamp.

## Fairness rule

Groups B and C must use the same task-agent adapter and the same mutation-agent adapter configuration unless the experiment explicitly studies heterogeneous models.

A lineage run may choose different parents, but it may not secretly use a stronger model, larger context, more candidate generations, or extra hidden feedback.

## Information boundary

The mutation process may see only training/evolution feedback that has already occurred.

It must not see:

- held-out task answers;
- oracle plans;
- future shock schedule;
- other experimental groups' candidate prompts;
- hidden evaluator chain-of-thought or private reasoning.

## Containment

The adapter should have the minimum permissions required to call the configured model and return JSON.

No benchmark requirement asks the model to:

- discover credentials;
- change system permissions;
- persist outside the run directory;
- contact unrelated external services;
- deploy descendants;
- self-replicate over a network.

If a provider adapter requires network access to call an API, that access is an explicit experiment dependency, not an inherited permission of candidate Agents.

## Recommended file layout

```text
model-run-001/
  config.json
  adapters/
    task_agent.py
    mutator.py
  candidates/
  logs/
  results/
  RUN_MANIFEST.json
```

Provider-specific adapter code should stay outside the canonical benchmark logic when possible. This keeps results comparable and makes it easier for another researcher to reproduce the run with a different provider.
