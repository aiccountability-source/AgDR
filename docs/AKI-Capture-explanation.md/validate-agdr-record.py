#!/usr/bin/env python3
"""AgDR v0.2 Record Validator - validates records against canonical JSON Schemas."""
import json, sys
from pathlib import Path

try:
      import jsonschema
except ImportError:
      print("Install jsonschema: pip install jsonschema"); sys.exit(1)

SCHEMA_DIR = Path(__file__).parent.parent / "specs" / "v0.2" / "schemas"

def validate_record(record):
      errors = []
      required = ["record_id","spec_version","ctx","reasoning_trace","output","ppp_triplet","human_delta_chain","merkle_hash","signature","timestamp_ns","committed"]
      for f in required:
                if f not in record: errors.append(f"Missing: {f}")
                      if record.get("spec_version") != "0.2": errors.append("spec_version must be 0.2")
                            if record.get("committed") is not True: errors.append("committed must be True")
                                  ppp = record.get("ppp_triplet", {})
            for p in ["provenance","place","purpose"]:
                      if not ppp.get(p): errors.append(f"PPP missing: {p}")
                            return errors

if __name__ == "__main__":
      if len(sys.argv) < 2: print("Usage: python validate-agdr-record.py <record.json>"); sys.exit(1)
            with open(sys.argv[1]) as f: record = json.load(f)
                  errors = validate_record(record)
    if errors:
              print(f"INVALID - {len(errors)} error(s):"); [print(f"  - {e}") for e in errors]; sys.exit(1)
else:
        print(f"VALID - AgDR v0.2 record: {record.get('record_id')}"); sys.exit(0)
