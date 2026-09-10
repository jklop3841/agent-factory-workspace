from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]

def jl(rel):
    return [json.loads(x) for x in (ROOT / rel).read_text(encoding="utf-8").splitlines() if x.strip()]

m = json.loads((ROOT / "MANIFEST.json").read_text(encoding="utf-8"))
patterns = jl("PATTERNS.jsonl")
primitives = jl("primitives/PRIMITIVES.jsonl")
comps = jl("compositions/COMPOSITIONS.jsonl")

assert m["version"] == "0.2.0"
assert len(patterns) == m["pattern_count"] == 12
assert len(primitives) == m["primitive_count"] == 18
assert len(comps) == m["seed_composition_count"] == 8

pattern_ids = {p["id"] for p in patterns}
primitive_ids = {p["id"] for p in primitives}

for p in primitives:
    assert set(p["source_patterns"]) <= pattern_ids

for c in comps:
    assert set(c["source_patterns"]) <= pattern_ids
    assert set(c["primitives"]) <= primitive_ids
    assert 2 <= len(c["primitives"]) <= 5

print("PASS: v0.2 composition/generativity structure validated")
