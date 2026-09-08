"""Offline receipt handling shared by the byte-preserved mathematical bodies."""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import platform
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PROVENANCE = json.loads((HERE / "provenance.json").read_text(encoding="utf-8"))
ACTIVE = None


def begin(case_id):
    global ACTIVE
    if not __debug__:
        raise RuntimeError("Optimized Python would disable some original assertions.")
    ACTIVE = next(case for case in PROVENANCE["cases"] if case["id"] == case_id)
    script = ROOT / ACTIVE["path"]
    data = script.read_bytes()
    start = b"# BEGIN UNCHANGED MATHEMATICAL BODY\n"
    end = b"\n# END UNCHANGED MATHEMATICAL BODY\n"
    body = data.split(start, 1)[1].split(end, 1)[0]
    if len(body) != ACTIVE["mathematical_body_bytes"] or hashlib.sha256(body).hexdigest() != ACTIVE["mathematical_body_sha256"]:
        raise AssertionError("The mathematical source body differs from its retained provenance.")


def finish(case_id, checks, auxiliary=None):
    if ACTIVE is None or ACTIVE["id"] != case_id:
        raise AssertionError("Uninitialized mathematical case.")
    if len(checks) != ACTIVE["expected_count"]:
        raise AssertionError((case_id, len(checks), ACTIVE["expected_count"]))
    for check in checks:
        if check.get("passed") is False or check.get("status") in ("fail", "failed"):
            raise AssertionError(check)
    output = Path(os.environ["WEB_AUDIT_OUTPUT_DIR"]).resolve()
    output.mkdir(parents=True, exist_ok=True)
    import sympy
    receipt = {
        "schema": "portable-web-audit-case-v1",
        "case": case_id,
        "status": "passed",
        "executed_count": len(checks),
        "scope": ACTIVE["scope"],
        "original_receipt_context": ACTIVE["original_receipt_context"],
        "python_version": platform.python_version(),
        "sympy_version": sympy.__version__,
        "portable_script_sha256": hashlib.sha256((ROOT / ACTIVE["path"]).read_bytes()).hexdigest(),
        "source_script_sha256": ACTIVE["source_script"]["sha256"],
        "unchanged_mathematical_body_sha256": ACTIVE["mathematical_body_sha256"],
        "source_snapshot_role": "Historical source hashes are retained in provenance.json; they are not reread or recertified by this execution.",
        "checks": checks,
        "auxiliary_noncounted_results": auxiliary or [],
    }
    (output / (case_id + ".json")).write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"case": case_id, "status": "passed", "executed_count": len(checks)}))
