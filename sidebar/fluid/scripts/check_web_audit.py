"""Replay the complete portable web audit in a fresh allowlisted directory.

Requires Python 3.10+ and SymPy; validated with Python 3.13.9 / SymPy 1.13.1.
Run from any working directory: python scripts/check_web_audit.py
The only persistent output is research/web_audit_replay.json, or --output PATH.
The ten saved external-source checks remain historical, never executed counts.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import time

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = "research/web_audit_integration.json"
PROVENANCE = "scripts/web_audit/provenance.json"

# The child has only the fresh subset and the explicitly installed Python
# runtime as filesystem inputs. SymPy is imported through the isolated runtime.
# Network and child process operations are denied before executing check code.
CHILD = r'''
import os, pathlib, runpy, sys
stage = pathlib.Path(sys.argv[1]).resolve()
script = pathlib.Path(sys.argv[2]).resolve()
allowed = (stage, pathlib.Path(sys.prefix).resolve(), pathlib.Path(sys.base_prefix).resolve())
def audit(event, args):
    if event.startswith("socket.") or event.startswith("subprocess.") or event in ("os.system", "os.exec", "os.posix_spawn", "os.spawn"):
        raise PermissionError("Offline check forbids network/process event: " + event)
    if event == "open" and isinstance(args[0], (str, bytes, os.PathLike)):
        candidate = pathlib.Path(os.fsdecode(args[0])).resolve()
        if not any(candidate == base or candidate.is_relative_to(base) for base in allowed):
            raise PermissionError("Check tried to open a file outside the fresh subset and Python runtime")
sys.addaudithook(audit)
sys.path.insert(0, str(script.parent))
runpy.run_path(str(script), run_name="__main__")
'''


def safe_member(base, name):
    relative = Path(name)
    if relative.is_absolute() or ".." in relative.parts:
        raise ValueError("Invalid allowlist path: " + name)
    path = (base / relative).resolve()
    if not path.is_relative_to(base.resolve()):
        raise ValueError("Allowlist path escaped its root: " + name)
    return path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "research/web_audit_replay.json")
    args = parser.parse_args()
    manifest = json.loads((ROOT / MANIFEST).read_text(encoding="utf-8"))
    provenance = json.loads((ROOT / PROVENANCE).read_text(encoding="utf-8"))
    entries = manifest["public_files"]
    names = [item["path"] for item in entries]
    if len(names) != len(set(names)) or len(names) != manifest["public_file_count"]:
        raise AssertionError("Allowlist count or uniqueness mismatch.")
    output_path = args.output.resolve()
    if output_path == (ROOT / MANIFEST).resolve():
        raise ValueError("The replay output must not overwrite the integration manifest.")
    receipts = []
    start = time.monotonic()
    with tempfile.TemporaryDirectory(prefix="web-audit-fresh-") as temporary:
        stage = Path(temporary).resolve()
        for item in entries:
            # Replay receipts are output, and are never mathematical input.
            if item["role"] == "generated_replay_receipt":
                continue
            source = safe_member(ROOT, item["path"])
            data = source.read_bytes()
            if "sha256" in item and hashlib.sha256(data).hexdigest() != item["sha256"]:
                raise AssertionError("Allowlist hash mismatch: " + item["path"])
            target = safe_member(stage, item["path"])
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
        outputs = stage / "executed_receipts"
        outputs.mkdir()
        env = dict(os.environ)
        for key in ("PYTHONPATH", "PYTHONHOME", "PYTHONSTARTUP", "PYTHONOPTIMIZE"):
            env.pop(key, None)
        env["WEB_AUDIT_OUTPUT_DIR"] = str(outputs)
        for case in provenance["cases"]:
            script = safe_member(stage, case["path"])
            result = subprocess.run(
                [sys.executable, "-B", "-I", "-c", CHILD, str(stage), str(script)],
                cwd=stage, env=env, text=True, encoding="utf-8", errors="replace",
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False,
            )
            if result.returncode:
                sys.stderr.write(result.stdout + result.stderr)
                raise RuntimeError("Portable mathematical case failed: " + case["id"])
            receipt = json.loads((outputs / (case["id"] + ".json")).read_text(encoding="utf-8"))
            if receipt["executed_count"] != case["expected_count"] or receipt["status"] != "passed":
                raise AssertionError("Case receipt mismatch: " + case["id"])
            receipts.append(receipt)
            print(f"PASS {case['id']}: {receipt['executed_count']} executed checks", flush=True)
    count = sum(receipt["executed_count"] for receipt in receipts)
    if count != manifest["check_counts"]["executed_total_with_overlap"]:
        raise AssertionError("Executed total mismatch.")
    receipt = {
        "schema": "portable-web-audit-replay-v1",
        "status": "passed",
        "executed_count_with_intentional_overlap": count,
        "executed_core_algebra": 250,
        "executed_separate_ipm_review": 17,
        "executed_exact_threshold": 1,
        "frozen_historical_source_checks_not_reexecuted": 10,
        "fresh_subset": True,
        "fresh_subset_input_files": sum(item["role"] != "generated_replay_receipt" for item in entries),
        "network_and_subprocess_denied_in_check_processes": True,
        "file_opens_restricted_to_fresh_subset_and_python_runtime": True,
        "lean_lake_elan_started": False,
        "external_source_snapshots_read": False,
        "wall_seconds": round(time.monotonic() - start, 3),
        "provenance_sha256": hashlib.sha256((ROOT / PROVENANCE).read_bytes()).hexdigest(),
        "integration_manifest_sha256": hashlib.sha256((ROOT / MANIFEST).read_bytes()).hexdigest(),
        "wrapper_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "scope": provenance["scope"],
        "cases": receipts,
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(f"PASS web audit: {count} executed checks with overlap; 10 source checks remain historical.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
