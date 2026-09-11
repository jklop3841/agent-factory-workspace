#!/usr/bin/env python3
"""Two-call adapter doctor for LRI Model Run 001.

Call 1: one batched task request containing two tiny diagnostic tasks.
Call 2: one bounded mutation request.

This script does not run an LRI comparison and cannot create empirical evidence.
It only checks that an explicitly configured task/mutation adapter is usable.
"""

from __future__ import annotations

import argparse
import json
import shlex
import subprocess
from typing import Any


def run(command: str, request: dict[str, Any], timeout: float) -> dict[str, Any]:
    completed = subprocess.run(
        shlex.split(command),
        input=json.dumps(request, ensure_ascii=False),
        text=True,
        capture_output=True,
        timeout=timeout,
        check=False,
    )
    if completed.returncode != 0:
        raise RuntimeError(f"adapter failed ({completed.returncode}): {completed.stderr[:2000]}")
    try:
        value = json.loads(completed.stdout)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"adapter output was not JSON: {completed.stdout[:2000]!r}") from exc
    if not isinstance(value, dict):
        raise RuntimeError("adapter output must be one JSON object")
    return value


def batch_request() -> dict[str, Any]:
    return {
        "protocol": "lri-model-agent-batch-v0.1",
        "candidate": {
            "candidate_id": "doctor-root",
            "system_prompt": "You are a tool-planning agent. Inspect each current tool catalog and return only valid tool IDs for that task.",
            "planning_notes": "Adapter compatibility doctor only.",
        },
        "split": "doctor",
        "tasks": [
            {
                "id": "doctor-add",
                "phase": "doctor",
                "phase_description": "Diagnostic task. No hidden benchmark information.",
                "start": 1,
                "target": 4,
                "tools": [
                    {"id": "d_alpha", "op": "add", "arg": 1, "cost": 1},
                    {"id": "d_beta", "op": "mul", "arg": 2, "cost": 1}
                ],
                "max_steps": 3
            },
            {
                "id": "doctor-neg",
                "phase": "doctor",
                "phase_description": "Diagnostic task. No hidden benchmark information.",
                "start": 3,
                "target": -5,
                "tools": [
                    {"id": "d_gamma", "op": "neg", "arg": null, "cost": 1},
                    {"id": "d_delta", "op": "add", "arg": -2, "cost": 1}
                ],
                "max_steps": 2
            }
        ],
        "response_schema": {"plans": {"task_id": ["tool_id", "..."]}}
    }


def mutation_request() -> dict[str, Any]:
    return {
        "protocol": "lri-mutation-v0.1",
        "group": "doctor",
        "generation": 1,
        "mutation_slot": 0,
        "parent": {
            "candidate_id": "doctor-root",
            "system_prompt": "You are a tool-planning agent. Inspect the current tool catalog before planning.",
            "planning_notes": "Diagnostic parent."
        },
        "available_feedback": {
            "training_phase": "doctor",
            "training_phase_scores": {"success_rate": 0.5, "invalid_rate": 0.5},
            "observed_errors": ["unknown_tool:remembered_old_name"],
            "resource_usage": {"mutation_model_calls": 0, "agent_task_calls": 1}
        },
        "editable_fields": ["system_prompt", "planning_notes"],
        "max_system_prompt_chars": 4000,
        "max_planning_notes_chars": 1000
    }


def usage_status(response: dict[str, Any]) -> dict[str, Any]:
    usage = response.get("usage")
    if not isinstance(usage, dict):
        return {"present": False, "exact_token_fields": False, "usage": None}
    exact = usage.get("input_tokens") is not None and usage.get("output_tokens") is not None
    return {"present": True, "exact_token_fields": exact, "usage": usage}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--task-adapter", required=True)
    parser.add_argument("--mutation-adapter", required=True)
    parser.add_argument("--timeout", type=float, default=120.0)
    args = parser.parse_args()

    batch = run(args.task_adapter, batch_request(), args.timeout)
    plans = batch.get("plans")
    if not isinstance(plans, dict):
        raise SystemExit("FAIL: task adapter did not return a plans object")
    required_ids = {"doctor-add", "doctor-neg"}
    missing = sorted(required_ids - set(plans))
    if missing:
        raise SystemExit(f"FAIL: task adapter omitted task IDs: {missing}")
    for task_id in required_ids:
        if not isinstance(plans[task_id], list):
            raise SystemExit(f"FAIL: plan for {task_id} is not a list")

    mutation = run(args.mutation_adapter, mutation_request(), args.timeout)
    for field in ("system_prompt", "planning_notes", "mutation_reason"):
        if field not in mutation or not isinstance(mutation[field], str):
            raise SystemExit(f"FAIL: mutation adapter missing string field {field}")
    if len(mutation["system_prompt"]) > 4000:
        raise SystemExit("FAIL: mutation system_prompt exceeded doctor bound")
    if len(mutation["planning_notes"]) > 1000:
        raise SystemExit("FAIL: mutation planning_notes exceeded doctor bound")

    task_usage = usage_status(batch)
    mutation_usage = usage_status(mutation)
    models = sorted({
        str(value)
        for value in (batch.get("model"), mutation.get("model"))
        if value is not None
    })
    result = {
        "protocol": "lri-adapter-doctor-v0.1",
        "status": "pass",
        "model_ids_returned": models,
        "task_batch": {
            "task_ids_returned": sorted(plans),
            "plans": plans,
            "usage": task_usage,
            "provider_request_id_present": batch.get("provider_request_id") is not None
        },
        "mutation": {
            "system_prompt_chars": len(mutation["system_prompt"]),
            "planning_notes_chars": len(mutation["planning_notes"]),
            "mutation_reason_chars": len(mutation["mutation_reason"]),
            "usage": mutation_usage,
            "provider_request_id_present": mutation.get("provider_request_id") is not None
        },
        "exact_token_accounting_available": task_usage["exact_token_fields"] and mutation_usage["exact_token_fields"],
        "evidence_warning": "Adapter doctor output is operational validation only and must not be interpreted as LRI evidence."
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
