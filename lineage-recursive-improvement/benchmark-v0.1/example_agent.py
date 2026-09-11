#!/usr/bin/env python3
"""Reference agent for the LRI tool-drift benchmark.

Reads one JSON request on stdin and writes {"plan": [...]} to stdout.
This is a semantics-aware search agent and serves as a protocol/ceiling example,
not as an LRI system.
"""

from __future__ import annotations

import heapq
import json
import math
import sys

BOUND = 100


def apply(value, tool):
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
        return None if value % arg else value // arg
    raise ValueError(op)


def solve(task):
    tools = {tool["id"]: tool for tool in task["tools"]}
    queue = [(0, 0, task["start"], [])]
    seen = {}

    while queue:
        cost, steps, value, plan = heapq.heappop(queue)
        state = (value, steps)
        if seen.get(state, math.inf) <= cost:
            continue
        seen[state] = cost

        if value == task["target"]:
            return plan
        if steps >= task["max_steps"]:
            continue

        for tool_id, tool in tools.items():
            next_value = apply(value, tool)
            if next_value is None or abs(next_value) > BOUND:
                continue
            heapq.heappush(
                queue,
                (cost + int(tool["cost"]), steps + 1, next_value, plan + [tool_id]),
            )

    return []


request = json.load(sys.stdin)
print(json.dumps({"plan": solve(request["task"])}))
