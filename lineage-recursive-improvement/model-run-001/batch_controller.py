#!/usr/bin/env python3
"""Batch-evaluation variant of the Model Run 001 controller.

It preserves the same A/B/C topology and mutation logic from controller.py but
evaluates all tasks in one phase/split with one adapter request per candidate.
This reduces model-call overhead without changing the local evaluator.

Use the same batch-capable task adapter for B and C. The batch mode is an
experiment-efficiency optimization, not an LRI mechanism.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import controller as core


def summarize_rows(rows: list[dict[str, Any]]) -> dict[str, Any]:
    tool_counts: dict[str, int] = {}
    old_name_reuse = 0
    total_steps = 0
    for row in rows:
        evaluation = row["evaluation"]
        plan = row.get("plan", [])
        valid_tool_ids = set(row.get("valid_tool_ids", []))
        for tool_id in plan if isinstance(plan, list) else []:
            if tool_id in {"inc", "dec", "double", "half"} and tool_id not in valid_tool_ids:
                old_name_reuse += 1
        for op in evaluation.get("used_ops", []):
            tool_counts[op] = tool_counts.get(op, 0) + 1
        total_steps += int(evaluation.get("steps", 0))

    successes = [row for row in rows if row["evaluation"]["success"]]
    invalid_count = sum(row["evaluation"].get("invalid") is not None for row in rows)
    total_op_uses = sum(tool_counts.values())
    mean_eff = (
        sum(float(row["evaluation"].get("cost_efficiency", 0.0)) for row in successes) / len(successes)
        if successes
        else 0.0
    )
    descriptor = {
        "tool_usage": {k: round(v / total_op_uses, 6) for k, v in sorted(tool_counts.items())}
        if total_op_uses
        else {},
        "invalid_action_rate": round(invalid_count / len(rows), 6) if rows else 0.0,
        "mean_plan_length": round(total_steps / len(rows), 6) if rows else 0.0,
        "mean_cost_efficiency": round(mean_eff, 6),
        "shock_reuse_old_names_rate": round(old_name_reuse / max(1, total_steps), 6),
    }
    metrics = {
        "tasks": len(rows),
        "successes": len(successes),
        "success_rate": round(len(successes) / len(rows), 6) if rows else 0.0,
        "invalid_rate": descriptor["invalid_action_rate"],
        "mean_cost_efficiency_on_success": descriptor["mean_cost_efficiency"],
        "mean_plan_length": descriptor["mean_plan_length"],
    }
    return {"metrics": metrics, "behavior_descriptor": descriptor}


def evaluate_candidate_batch(
    candidate: dict[str, Any],
    phase: dict[str, Any],
    adapter_cmd: str,
    timeout: float,
    budget: core.Budget,
    split: str,
) -> dict[str, Any]:
    tasks = phase["tasks"]
    budget.check("task")
    request = {
        "protocol": "lri-model-agent-batch-v0.1",
        "candidate": {
            "candidate_id": candidate["candidate_id"],
            "system_prompt": candidate["system_prompt"],
            "planning_notes": candidate.get("planning_notes", ""),
        },
        "tasks": [core.public_task(task) for task in tasks],
        "split": split,
        "response_schema": {"plans": {"task_id": ["tool_id", "..."]}},
        "rules": [
            "Return exactly one plan per supplied task ID.",
            "Do not infer or request hidden oracle fields.",
        ],
    }

    rows: list[dict[str, Any]] = []
    try:
        response = core.run_command(adapter_cmd, request, timeout)
        budget.record_task(response.get("usage"))
        plans = response.get("plans", {})
        if not isinstance(plans, dict):
            plans = {}
        batch_error = None
    except Exception as exc:
        budget.record_task(None)
        response = {}
        plans = {}
        batch_error = str(exc)

    for task in tasks:
        plan = plans.get(task["id"], []) if batch_error is None else []
        if batch_error is None:
            evaluation = core.evaluate_plan(task, plan)
            error = None
        else:
            evaluation = {
                "success": False,
                "invalid": "adapter_error",
                "steps": 0,
                "cost": None,
                "cost_efficiency": 0.0,
                "used_ops": [],
            }
            error = batch_error
        rows.append(
            {
                "task_id": task["id"],
                "plan": plan,
                "valid_tool_ids": [tool["id"] for tool in task["tools"]],
                "response_meta": {
                    "provider_request_id": response.get("provider_request_id"),
                    "model": response.get("model"),
                },
                "evaluation": evaluation,
                "error": error,
            }
        )

    summary = summarize_rows(rows)
    return {
        "metrics": summary["metrics"],
        "behavior_descriptor": summary["behavior_descriptor"],
        "rows": rows,
        "batch_evaluation": True,
        "batch_model_calls": 1,
    }


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--group", choices=["A_fixed", "B_monolithic", "C_lineage"], required=True)
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--training", type=Path, required=True)
    parser.add_argument("--heldout", type=Path, required=True)
    parser.add_argument("--task-adapter", required=True)
    parser.add_argument("--mutation-adapter", required=True)
    parser.add_argument("--archive-policy", choices=["diversity", "score_only"], default="diversity")
    parser.add_argument("--prune-before-phase")
    parser.add_argument("--out-dir", type=Path, default=Path("results"))
    parser.add_argument("--timeout", type=float, default=120.0)
    args = parser.parse_args()

    config = load_json(args.config)
    if config.get("evaluation", {}).get("batch_tasks") is not True:
        raise SystemExit("batch_controller requires config.evaluation.batch_tasks=true")

    # Reuse the exact core topology/selection/mutation implementation, replacing
    # only the task-evaluation transport.
    core.evaluate_candidate = evaluate_candidate_batch
    result = core.run_group(args, config, load_json(args.training), load_json(args.heldout))
    print(
        json.dumps(
            {
                "group": result["group"],
                "evaluation_mode": "batch",
                "budget": result["budget"],
                "candidates": result["candidates_generated_including_root"],
                "final_active_candidates": result["final_active_candidates"],
                "result_file": str(args.out_dir),
            },
            indent=2,
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
