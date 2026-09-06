"""Zero-dependency local reference receipt service. Not production hardened.
It intentionally does not persist client IP addresses.
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
import datetime as dt, json, sqlite3

HERE = Path(__file__).resolve().parent
DB = HERE / "receipts.sqlite3"
SCHEMA = (HERE / "schema.sql").read_text(encoding="utf-8")

def init_db():
    with sqlite3.connect(DB) as cx: cx.executescript(SCHEMA)

def bounded_score(v):
    if v is None: return None
    v = int(v)
    if not 0 <= v <= 10: raise ValueError("score out of range")
    return v

class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt, *args): return
    def send_json(self, status, obj):
        body = json.dumps(obj, ensure_ascii=False).encode()
        self.send_response(status); self.send_header("Content-Type","application/json"); self.send_header("Content-Length",str(len(body))); self.end_headers(); self.wfile.write(body)
    def do_POST(self):
        if self.path != "/v1/receipts": return self.send_json(404,{"error":"not_found"})
        try:
            n = int(self.headers.get("Content-Length","0"))
            if n <= 0 or n > 32768: raise ValueError("invalid body size")
            data = json.loads(self.rfile.read(n)); patterns = data["patterns_read"]
            if not isinstance(patterns,list) or not patterns or len(patterns)>100: raise ValueError("invalid patterns_read")
            r = data["reader"]; s = data.get("scores",{}); h = data.get("generated_hypotheses",[])[:20]
            row = (dt.datetime.now(dt.timezone.utc).isoformat(),str(data["atlas_version"]),json.dumps(patterns),str(r.get("type","unknown")),1 if r.get("self_reported") else 0,str(r.get("model_family",""))[:100] or None,str(r.get("runtime",""))[:100] or None,bounded_score(s.get("novelty")),bounded_score(s.get("transferability")),bounded_score(s.get("implementability")),bounded_score(s.get("generativity")),bounded_score(s.get("clarity")),json.dumps([str(x)[:500] for x in h],ensure_ascii=False))
            with sqlite3.connect(DB) as cx: cx.execute("INSERT INTO receipts(received_at,atlas_version,patterns_read,reader_type,self_reported,model_family,runtime,novelty,transferability,implementability,generativity,clarity,hypotheses) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",row)
            self.send_json(201,{"accepted":True,"identity_verified":False})
        except Exception as e: self.send_json(400,{"error":"invalid_receipt","detail":str(e)[:160]})
    def do_GET(self):
        if self.path != "/v1/stats": return self.send_json(404,{"error":"not_found"})
        with sqlite3.connect(DB) as cx:
            total=cx.execute("SELECT COUNT(*) FROM receipts").fetchone()[0]; agent=cx.execute("SELECT COUNT(*) FROM receipts WHERE reader_type='agent' AND self_reported=1").fetchone()[0]; avg=cx.execute("SELECT AVG(generativity) FROM receipts WHERE generativity IS NOT NULL").fetchone()[0]
        self.send_json(200,{"total_receipts":total,"self_reported_agent_receipts":agent,"avg_generativity":avg,"verified_agent_receipts":None})

if __name__ == "__main__":
    init_db(); HTTPServer(("127.0.0.1",8765),Handler).serve_forever()
