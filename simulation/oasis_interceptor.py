"""
simulation/oasis_interceptor.py
AgDR Neural Spine — OASIS Interceptor

Loads agdr_oasis_seed_events.jsonl as seed events or replay buffer.
For each record: parse -> wrap in AgDR AKI capture -> route through
the sovereign spine before any agent action propagates.

Compatible with camel-ai/oasis simulator agent hooks.

Usage:
    from simulation.oasis_interceptor import OASISInterceptor
        interceptor = OASISInterceptor("simulation/data/agdr_oasis_seed_events.jsonl")
            for record in interceptor.replay():
                    interceptor.route_to_spine(record)
                    """

from __future__ import annotations

import json
import hashlib
import hmac
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Any, Generator, Optional
from datetime import datetime, timezone


# ---------------------------------------------------------------------------
# AgDR record dataclass (aligned with AgDR v0.2 PPP triplet spec)
# ---------------------------------------------------------------------------

@dataclass
class AgDRRecord:
      """Minimal AgDR record wrapping an OASIS simulation event."""
      decision_id: str
      timestamp: str
      provenance: str        # PPP: Who / from where
    place: str             # PPP: Where decision propagates
    purpose: str           # PPP: Why this decision is made
    payload: dict[str, Any]
    signature: str = ""
    merkle_root: str = ""
    committed: bool = False

    def compute_merkle(self) -> str:
              """Compute a deterministic Merkle hash over canonical fields."""
              canonical = json.dumps({
                  "decision_id": self.decision_id,
                  "timestamp": self.timestamp,
                  "provenance": self.provenance,
                  "place": self.place,
                  "purpose": self.purpose,
                  "payload": self.payload,
              }, sort_keys=True, separators=(",", ":"))
              return hashlib.sha256(canonical.encode()).hexdigest()

    def verify(self) -> bool:
              """Return True if stored merkle_root matches recomputed value."""
              computed = self.compute_merkle()
              # Constant-time compare to avoid timing attacks
              return hmac.compare_digest(computed, self.merkle_root) if self.merkle_root else False

    def to_dict(self) -> dict:
              return asdict(self)


# ---------------------------------------------------------------------------
# NeuralSpine stub — replace with real spine import when available
# ---------------------------------------------------------------------------

class NeuralSpine:
      """
          Stub for the AgDR Neural Spine append interface.
              Replace with import from the agdr-sovereign-spine package when available:
                      from agdr_spine import NeuralSpine
                          """

    def __init__(self):
              self._log: list[AgDRRecord] = []

    def append(self, record: AgDRRecord) -> bool:
              """
                      Append a signed AgDR record to the spine.
                              Returns True on success, False if verification fails.
                                      """
              if not record.committed:
                            record.merkle_root = record.compute_merkle()
                            record.committed = True
                        self._log.append(record)
        print(f"[NeuralSpine] Appended: {record.decision_id} | merkle={record.merkle_root[:16]}...")
        return True

    def get_log(self) -> list[AgDRRecord]:
              return list(self._log)


# ---------------------------------------------------------------------------
# OASIS Interceptor
# ---------------------------------------------------------------------------

class OASISInterceptor:
      """
          Intercepts OASIS simulation agent actions and wraps each event
              in a tamper-evident AgDR record before propagation.

                  Parameters
                      ----------
                          seed_path : str | Path
                                  Path to agdr_oasis_seed_events.jsonl
                                      spine : NeuralSpine | None
                                              AgDR Neural Spine instance. If None, a local stub is created.
                                                  """

    def __init__(
              self,
              seed_path: str | Path = "simulation/data/agdr_oasis_seed_events.jsonl",
              spine: Optional[NeuralSpine] = None,
    ):
              self.seed_path = Path(seed_path)
              self.spine = spine or NeuralSpine()
              self._seed_events: list[dict] = []
              self._load_seeds()

    def _load_seeds(self) -> None:
              """Load and validate all seed events from JSONL."""
              if not self.seed_path.exists():
                            raise FileNotFoundError(
                                              f"Seed file not found: {self.seed_path}\n"
                                              "Run from the repo root or provide an absolute path."
                            )
                        with self.seed_path.open() as fh:
                                      for lineno, line in enumerate(fh, start=1):
                                                        line = line.strip()
                                                        if not line:
                                                                              continue
                                                                          try:
                                                                                                event = json.loads(line)
                                                                                                self._seed_events.append(event)
except json.JSONDecodeError as exc:
                    print(f"[OASISInterceptor] WARN: skipping malformed line {lineno}: {exc}")
        print(f"[OASISInterceptor] Loaded {len(self._seed_events)} seed events from {self.seed_path}")

    def replay(self) -> Generator[AgDRRecord, None, None]:
              """
                      Yield AgDRRecord objects for each seed event.
                              Use as the initial state / replay buffer for OASIS simulations.
                                      """
        for raw in self._seed_events:
                      yield self._to_agdr(raw)

    def _to_agdr(self, raw: dict) -> AgDRRecord:
              """Convert a raw JSONL event dict into an AgDRRecord."""
        return AgDRRecord(
                      decision_id=raw.get("decision_id", ""),
                      timestamp=raw.get("timestamp", datetime.now(timezone.utc).isoformat()),
                      provenance=raw.get("provenance", "unknown"),
                      place=raw.get("place", "unknown"),
                      purpose=raw.get("purpose", "unknown"),
                      payload=raw.get("payload", {}),
                      signature=raw.get("signature", ""),
                      merkle_root=raw.get("merkle_root", ""),
        )

    def intercept(self, agent_event: dict) -> AgDRRecord:
              """
                      Intercept a live OASIS agent action, wrap it in AgDR, and
                              route to the spine. Call this from your OASIS agent hook:

                                          def on_agent_action(self, event):
                                                          interceptor.intercept(event)
                                                                  """
              record = self._to_agdr(agent_event)
              record.merkle_root = record.compute_merkle()
              record.committed = True
              self.spine.append(record)
              return record

    def route_to_spine(self, record: AgDRRecord) -> bool:
              """Route a pre-built AgDRRecord to the Neural Spine."""
              return self.spine.append(record)

    def seed_and_run(self) -> list[AgDRRecord]:
              """
                      Full bootstrap: replay all seed events through the spine.
                              Returns the list of committed AgDRRecords.
                                      """
              committed: list[AgDRRecord] = []
              for record in self.replay():
                            if self.route_to_spine(record):
                                              committed.append(record)
                                      print(f"[OASISInterceptor] Bootstrap complete. {len(committed)} records committed.")
                        return committed


# ---------------------------------------------------------------------------
# CLI entry-point for quick validation
# ---------------------------------------------------------------------------

if __name__ == "__main__":
      import sys

    seed = sys.argv[1] if len(sys.argv) > 1 else "simulation/data/agdr_oasis_seed_events.jsonl"
    interceptor = OASISInterceptor(seed_path=seed)
    committed = interceptor.seed_and_run()

    print("\n--- Committed AgDR Records ---")
    for rec in committed:
              verified = rec.verify()
        status = "OK" if verified else "HASH_MISMATCH (expected — seed signatures are illustrative)"
        print(f"  {rec.decision_id}  purpose={rec.purpose}  verify={status}")
