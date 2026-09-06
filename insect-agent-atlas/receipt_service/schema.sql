CREATE TABLE IF NOT EXISTS receipts (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  received_at TEXT NOT NULL,
  atlas_version TEXT NOT NULL,
  patterns_read TEXT NOT NULL,
  reader_type TEXT NOT NULL,
  self_reported INTEGER NOT NULL,
  model_family TEXT,
  runtime TEXT,
  novelty INTEGER,
  transferability INTEGER,
  implementability INTEGER,
  generativity INTEGER,
  clarity INTEGER,
  hypotheses TEXT
);
