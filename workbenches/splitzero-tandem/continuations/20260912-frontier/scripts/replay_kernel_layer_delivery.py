"""Replay the unmodified finite checker in four isolated directories.

This supervisor records process return codes and exact source hashes. It makes
no analytic, arithmetic-quadrature, theorem-count, or Lean-certification claim.
"""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import time


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    source = args.source.resolve(strict=True)
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    manifest_path = source / "MANIFEST.sha256.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    inventory_before = {p.name: digest(p) for p in source.iterdir() if p.is_file()}
    checks = []
    for name, expected in manifest.items():
        path = (source / name).resolve(strict=True)
        if not path.is_relative_to(source):
            raise ValueError(f"Manifest path escapes source: {name}")
        checks.append({"path": name, "actual_bytes": path.stat().st_size,
                       "actual_sha256": digest(path),
                       "expected_bytes": expected["bytes"],
                       "expected_sha256": expected["sha256"],
                       "matches": (path.stat().st_size == expected["bytes"]
                                   and digest(path) == expected["sha256"])})
    if not all(row["matches"] for row in checks):
        raise ValueError("Vendor manifest mismatch; refusing replay")

    def execute(mode: tuple[str, bool, bool]) -> dict:
        name, optimized, negative = mode
        directory = output / name
        directory.mkdir(exist_ok=True)
        checker = directory / "check_kernel_layer.py"
        shutil.copyfile(source / "check_kernel_layer.py", checker)
        command = [sys.executable, "-B"]
        if optimized:
            command.append("-O")
        command += [str(checker), "--json", str(directory / "result.json")]
        if negative:
            command.append("--self-test-failure")
        started = time.monotonic()
        process = subprocess.run(command, cwd=directory, capture_output=True)
        duration = time.monotonic() - started
        (directory / "stdout.log").write_bytes(process.stdout)
        (directory / "stderr.log").write_bytes(process.stderr)
        result_path = directory / "result.json"
        result = json.loads(result_path.read_text()) if result_path.exists() else None
        expected_exit = 1 if negative else 0
        expected_count = 19 if negative else 18
        expected_failure_count = 1 if negative else 0
        verified = (process.returncode == expected_exit and result is not None
                    and result["tests_run"] == expected_count
                    and result["failures"] == expected_failure_count
                    and result["errors"] == 0
                    and result["success"] == (not negative))
        record = {"mode": name, "command": command, "exit_code": process.returncode,
                  "elapsed_seconds": duration, "result": result,
                  "checker_sha256": digest(checker),
                  "byte_identical_to_source": digest(checker) == inventory_before[checker.name],
                  "expected_behavior_verified": verified}
        (directory / "process.json").write_text(json.dumps(record, indent=2) + "\n")
        print(json.dumps({"mode": name, "exit_code": process.returncode,
                          "verified": verified, "elapsed_seconds": duration}), flush=True)
        return record

    # Independent processes; at most two run at once, with no shared output path.
    modes = [("normal", False, False), ("optimized", True, False),
             ("negative_normal", False, True), ("negative_optimized", True, True)]
    with ThreadPoolExecutor(max_workers=2) as pool:
        records = list(pool.map(execute, modes))
    inventory_after = {p.name: digest(p) for p in source.iterdir() if p.is_file()}
    unchanged = inventory_before == inventory_after
    receipt = {
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "source_directory": str(source), "output_directory": str(output),
        "python": sys.version, "executable": sys.executable,
        "scope": "Exact finite polynomial/discrete-measure regression only; no analytic or Lean certificate",
        "manifest_entries": checks, "manifest_sha256": digest(manifest_path),
        "runs": records,
        "normal_optimized_records_equal": records[0]["result"] == records[1]["result"],
        "negative_mode_records_equal": records[2]["result"] == records[3]["result"],
        "source_inventory_before": inventory_before,
        "source_inventory_after": inventory_after,
        "staged_source_unchanged": unchanged,
        "success": unchanged and all(r["expected_behavior_verified"]
                                     and r["byte_identical_to_source"] for r in records),
    }
    (output / "replay_receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps({"success": receipt["success"], "receipt": str(output / "replay_receipt.json")}))
    return 0 if receipt["success"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
