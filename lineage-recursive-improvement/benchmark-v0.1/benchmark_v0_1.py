#!/usr/bin/env python3
"""LRI Benchmark v0.1: Tool Interface Drift.

Purpose:
- Provide a zero-dependency, local benchmark that real command-line agents can run.
- Measure robustness to tool removal, renaming/semantic shift, and cost changes.
- Provide a common evaluation surface for fixed, monolithic-recursive, and
  lineage/population controllers.

This file does NOT implement autonomous external replication or deployment.
It executes only a user-supplied local command when --agent-cmd is provided.
"""

from __future__ import annotations

import argparse
import heapq
import json
import math
import shlex
import subprocess
from pathlib import Path
from typing import Any

PHASES = [
    {
        "id": "stable",
        "description": "Initial tool interface.",
        "tools": [
            {"id": "inc", "op": "add", "arg": 1, "cost": 1},
            {"id": "dec", "op": "add", "arg": -1, "cost": 1},
            {"id": "double", "op": "mul", "arg": 2, "cost": 1},
            {"id": "half", "op": "div_exact", "arg": 2, "cost": 1},
        ],
        "starts": [1, 2, 3, 4, 5],
        "targets": [7, 10, 14, 18, 21],
    },
    {
        "id": "remove_double",
        "description": "The cheap doubling tool disappears; a costlier triple tool appears.",
        "tools": [
            {"id": "inc", "op": "add", "arg": 1, "cost": 1},
            {"id": "dec", "op": "add", "arg": -1, "cost": 1},
            {"id": "triple", "op": "mul", "arg": 3, "cost": 2},
            {"id": "half", "op": "div_exact", "arg": 2, "cost": 1},
        ],
        "starts": [1, 2, 3, 4, 5],
        "targets": [8, 11, 17, 20, 26],
    },
    {
        "id": "rename_and_negate",
        "description": "Tool names and semantics change; negative targets become useful.",
        "tools": [
            {"id": "amber", "op": "add", "arg": 2, "cost": 1},
            {"id": "cobalt", "op": "add", "arg": -2, "cost": 1},
            {"id": "delta", "op": "mul", "arg": 2, "cost": 2},
            {"id": "echo", "op": "neg", "arg": None, "cost": 1},
        ],
        "starts": [-5, -3, 1, 3, 5],
        "targets": [6, 10, -8, -2, 14],
    },
    {
        "id": "cost_shift",
        "description": "Semantically simple actions become expensive; planning must account for cost.",
        "tools": [
            {"id": "step", "op": "add", "arg": 1, "cost": 3},
            {"id": "jump", "op": "add", "arg": 5, "cost": 1},
            {"id": "flip", "op": "neg", "arg": None, "cost": 1},
            {"id": "half", "op": "div_exact", "arg": 2, "cost": 2},
        ],
        "starts": [1, 2, 4, 7, 10],
        "targets": [11, 17, -9, 22, 3],
    },
]

MAX_STEPS = 6
VALUE_BOUND = 100


def apply_tool(value: int, tool: dict[str, Any]) -> int | None:
    op = tool["op"]
    arg = tool.get("arg")
    if op == "add":
        return value + int(arg)
    if op == "mul":
        return value * int(arg)
    if op == "neg":
        return -value
    if op == "div_exact":
        arg = int(arg)
        if value % arg != 0:
            return None
        return value // arg
    raise ValueError(f"Unknown operation: {op}")


def oracle_plan(task: dict[str, Any]) -> tuple[list[str] | None, int | None]:
    tools = {tool["id"]: tool for tool in task["tools"]}
    queue: list[tuple[int, int, int, list[str]]] = [(0, 0, task["start"], [])]
    seen: dict[tuple[int, int], int] = {}

    while queue:
        cost, steps, value, plan = heapq.heappop(queue)
        state = (value, steps)
        if seen.get(state, math.inf) <= cost:
            continue
        seen[state] = cost

        if value == task["target"]:
            return plan, cost
        if steps >= task["max_steps"]:
            continue

        for tool_id, tool in tools.items():
            next_value = apply_tool(value, tool)
            if next_value is None or abs(next_value) > VALUE_BOUND:
                continue
            heapq.heappush(
                queue,
                (cost + int(tool["cost"]), steps + 1, next_value, plan + [tool_id]),
            )

    return None, None


def build_tasks() -> list[dict[str, Any]]:
    tasks: list[dict[str, Any]] = []
    for phase in PHASES:
        for index, (start, target) in enumerate(zip(phase["starts"], phase["targets"])):
            task = {
                "id": f"{phase['id']}-{index}",
                "phase": phase["id"],
                "phase_description": phase["description"],
                "start": start,
                "target": target,
                "tools": phase["tools"],
                "max_steps": MAX_STEPS,
            }
            plan, cost = oracle_plan(task)
            if plan is None:
                raise RuntimeError(f"Unsolvable benchmark task: {task['id']}")
            task["_oracle_plan"] = plan
            task["_oracle_cost"] = cost
            tasks.append(task)
    return tasks


def public_task(task: dict[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in task.items() if not key.startswith("_")}


def evaluate_plan(task: dict[str, Any], plan: list[str]) -> dict[str, Any]:
    tools = {tool["id"]: tool for tool in task["tools"]}
    value = task["start"]
    total_cost = 0
    invalid = None

    if not isinstance(plan, list):
        return {"success": False, "invalid": "plan_not_list", "cost": None, "steps": 0}

    if len(plan) > task["max_steps"]:
        return {
            "success": False,
            "invalid": "too_many_steps",
            "cost": None,
            "steps": len(plan),
        }

    for tool_id in plan:
        if tool_id not in tools:
            invalid = f"unknown_tool:{tool_id}"
            break
        tool = tools[tool_id]
        next_value = apply_tool(value, tool)
        if next_value is None:
            invalid = f"invalid_precondition:{tool_id}"
            break
        value = next_value
        total_cost += int(tool["cost"])
        if abs(value) > VALUE_BOUND:
            invalid = "value_bound_exceeded"
            break

    success = invalid is None and value == task["target"]
    oracle_cost = int(task["_oracle_cost"])
    efficiency = (
        oracle_cost / total_cost
        if success and total_cost > 0
        else (1.0 if success else 0.0)
    )

    return {
        "success": success,
        "invalid": invalid,
        "final_value": value,
        "cost": total_cost if invalid is None else None,
        "steps": len(plan),
        "oracle_cost": oracle_cost,
        "cost_efficiency": round(efficiency, 6),
    }


def builtin_oracle(task: dict[str, Any]) -> dict[str, Any]:
    return {"plan": list(task["_oracle_plan"])}


def builtin_legacy(task: dict[str, Any]) -> dict[str, Any]:
    """A deliberately brittle pre-shock policy that assumes old tool names."""
    target = task["target"]
    value = task["start"]
    plan: list[str] = []
    for _ in range(task["max_steps"]):
        if value == target:
            break
        if abs(target - value) >= abs(target - (value * 2)):
            plan.append("double")
            value *= 2
        elif target > value:
            plan.append("inc")
            value += 1
        else:
            plan.append("dec")
            value -= 1
    return {"plan": plan}


def call_external(command: str, task: dict[str, Any], timeout: float) -> dict[str, Any]:
    request = {
        "protocol": "lri-tool-drift-v0.1",
        "task": public_task(task),
        "response_schema": {"plan": ["tool_id", "..."]},
    }
    completed = subprocess.run(
        shlex.split(command),
        input=json.dumps(request),
        text=True,
        capture_output=True,
        timeout=timeout,
        check=False,
    )
    if completed.returncode != 0:
        raise RuntimeError(
            f"agent command exited {completed.returncode}: {completed.stderr.strip()}"
        )
    try:
        response = json.loads(completed.stdout.strip())
    except json.JSONDecodeError as exc:
        raise RuntimeError(
            f"agent output was not valid JSON: {completed.stdout!r}"
        ) from exc
    if not isinstance(response, dict):
        raise RuntimeError("agent response must be a JSON object")
    return response


def summarize(results: list[dict[str, Any]]) -> dict[str, Any]:
    phases: dict[str, dict[str, Any]] = {}
    for phase in [item["id"] for item in PHASES]:
        rows = [row for row in results if row["phase"] == phase]
        successes = [row for row in rows if row["evaluation"]["success"]]
        phases[phase] = {
            "tasks": len(rows),
            "successes": len(successes),
            "success_rate": round(len(successes) / len(rows), 6),
            "mean_cost_efficiency_on_success": round(
                sum(row["evaluation"]["cost_efficiency"] for row in successes)
                / len(successes),
                6,
            )
            if successes
            else 0.0,
            "invalid_rate": round(
                sum(row["evaluation"]["invalid"] is not None for row in rows)
                / len(rows),
                6,
            ),
        }

    total_success = sum(row["evaluation"]["success"] for row in results)
    return {
        "protocol": "lri-tool-drift-v0.1",
        "tasks": len(results),
        "overall_success_rate": round(total_success / len(results), 6),
        "phases": phases,
        "results": results,
    }


def run(args: argparse.Namespace) -> dict[str, Any]:
    tasks = build_tasks()
    rows: list[dict[str, Any]] = []

    for task in tasks:
        try:
            if args.builtin == "oracle":
                response = builtin_oracle(task)
            elif args.builtin == "legacy":
                response = builtin_legacy(task)
            else:
                response = call_external(args.agent_cmd, task, args.timeout)
            plan = response.get("plan", [])
            evaluation = evaluate_plan(task, plan)
            error = None
        except Exception as exc:
            response = {}
            evaluation = {
                "success": False,
                "invalid": "agent_error",
                "cost": None,
                "steps": 0,
                "cost_efficiency": 0.0,
            }
            error = str(exc)

        rows.append(
            {
                "task_id": task["id"],
                "phase": task["phase"],
                "response": response,
                "evaluation": evaluation,
                "error": error,
            }
        )

    return summarize(rows)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--builtin", choices=["oracle", "legacy"])
    mode.add_argument("--agent-cmd", help="Local command that reads one JSON request on stdin.")
    parser.add_argument("--timeout", type=float, default=30.0)
    parser.add_argument("--output", type=Path)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    report = run(args)
    rendered = json.dumps(report, indent=2, ensure_ascii=False)
    if args.output:
        args.output.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)


if __name__ == "__main__":
    main()
