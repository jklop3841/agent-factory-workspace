#!/usr/bin/env python3
"""Zero-cost deterministic adapter for Model Run 001 smoke tests.

This is NOT a model and results from it are NOT LRI evidence. It exists to
exercise the complete controller, ancestry, budget, hidden-task, and ablation
plumbing before any paid or local-model run.
"""

from __future__ import annotations

import heapq
import json
import math
import sys
from typing import Any

VALUE_BOUND = 200


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
        divisor = int(arg)
        if divisor == 0 or value % divisor:
            return None
        return value // divisor
    return None


def semantic_plan(task: dict[str, Any], cost_aware: bool) -> list[str]:
    tools = {t["id"]: t for t in task["tools"]}
    # Dijkstra if cost-aware, breadth-like search otherwise.
    queue: list[tuple[float, int, int, list[str]]] = [(0.0, 0, int(task["start"]), [])]
    seen: dict[tuple[int, int], float] = {}
    while queue:
        priority, steps, value, plan = heapq.heappop(queue)
        state = (value, steps)
        if seen.get(state, math.inf) <= priority:
            continue
        seen[state] = priority
        if value == int(task["target"]):
            return plan
        if steps >= int(task["max_steps"]):
            continue
        for tool_id, tool in tools.items():
            nxt = apply_tool(value, tool)
            if nxt is None or abs(nxt) > VALUE_BOUND:
                continue
            increment = float(tool["cost"]) if cost_aware else 1.0
            heapq.heappush(queue, (priority + increment, steps + 1, nxt, plan + [tool_id]))
    return []


def legacy_plan(task: dict[str, Any]) -> list[str]:
    # Deliberately assumes pre-shock names; randomized hidden IDs make this brittle.
    value = int(task["start"])
    target = int(task["target"])
    plan: list[str] = []
    for _ in range(int(task["max_steps"])):
        if value == target:
            break
        if abs(target - value * 2) < abs(target - value):
            plan.append("double")
            value *= 2
        elif target > value:
            plan.append("inc")
            value += 1
        else:
            plan.append("dec")
            value -= 1
    return plan


def task_mode(request: dict[str, Any]) -> dict[str, Any]:
    prompt = str(request.get("candidate", {}).get("system_prompt", ""))
    task = request["task"]
    if "POLICY=COST_AWARE" in prompt:
        plan = semantic_plan(task, cost_aware=True)
    elif "POLICY=SEMANTIC" in prompt:
        plan = semantic_plan(task, cost_aware=False)
    else:
        plan = legacy_plan(task)
    return {
        "plan": plan,
        "usage": {"input_tokens": 0, "output_tokens": 0, "model_calls": 1},
        "provider_request_id": "deterministic-smoke-only",
    }


def mutation_mode(request: dict[str, Any]) -> dict[str, Any]:
    parent = request["parent"]
    slot = int(request.get("mutation_slot", 0))
    base = str(parent.get("system_prompt", "")).split("\nPOLICY=")[0].rstrip()
    if slot % 3 == 0:
        policy = "POLICY=SEMANTIC"
        reason = "Read current tool semantics instead of relying on remembered tool names."
    elif slot % 3 == 1:
        policy = "POLICY=COST_AWARE"
        reason = "Plan from current semantics while explicitly minimizing declared tool cost."
    else:
        policy = "POLICY=LEGACY"
        reason = "Control mutation that keeps the brittle name-based policy."
    prompt = (base + "\n" + policy).strip()
    return {
        "system_prompt": prompt,
        "planning_notes": f"deterministic smoke mutation slot={slot}; no language model used",
        "mutation_reason": reason,
        "usage": {"input_tokens": 0, "output_tokens": 0, "model_calls": 1},
    }


def main() -> None:
    request = json.loads(sys.stdin.read())
    protocol = request.get("protocol")
    if protocol == "lri-model-agent-v0.1":
        response = task_mode(request)
    elif protocol == "lri-mutation-v0.1":
        response = mutation_mode(request)
    else:
        raise SystemExit(f"unsupported protocol: {protocol}")
    sys.stdout.write(json.dumps(response, ensure_ascii=False))


if __name__ == "__main__":
    main()
