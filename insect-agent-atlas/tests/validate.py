from pathlib import Path
import json
ROOT = Path(__file__).resolve().parents[1]
manifest = json.loads((ROOT/"MANIFEST.json").read_text(encoding="utf-8"))
patterns = [json.loads(x) for x in (ROOT/"PATTERNS.jsonl").read_text(encoding="utf-8").splitlines() if x.strip()]
index = [json.loads(x) for x in (ROOT/"INDEX.jsonl").read_text(encoding="utf-8").splitlines() if x.strip()]
sources = [json.loads(x) for x in (ROOT/"evidence/SOURCES.jsonl").read_text(encoding="utf-8").splitlines() if x.strip()]
assert manifest["pattern_count"] == 12
assert len(patterns) == len(index) == 12
ids = {p["id"] for p in patterns}
assert len(ids) == 12 and ids == {i["id"] for i in index}
source_ids = {s["id"] for s in sources}
for p in patterns: assert set(p["evidence_ids"]) <= source_ids
print("PASS: atlas structure and cross-references validated")
