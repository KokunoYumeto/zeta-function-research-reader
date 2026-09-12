"""Bounded source-preserving replay of the assigned finite checker."""

from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "local_replay"
OUT.mkdir(exist_ok=True)
SOURCE_ROOT = ROOT / "repository"
SOURCES = [
    SOURCE_ROOT / "formal/splitzero/SplitZeroCyclicDepth.lean",
    SOURCE_ROOT / "workbenches/tau-conormal-cyclic-formal/check_depth_models.py",
    SOURCE_ROOT / "workbenches/tau-conormal-cyclic-formal/RESEARCH_NOTE.md",
]
CHECKER = SOURCES[1]


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


before = {str(path.relative_to(SOURCE_ROOT)): digest(path) for path in SOURCES}
for path in SOURCES:
    numbered = "".join(f"{i:04d}: {line}\n" for i, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1))
    (OUT / (path.name + ".numbered.txt")).write_text(numbered, encoding="utf-8")

runs = []
for mode, flags, expected in [
    ("normal", [], 0),
    ("optimized", ["-O"], 0),
    ("negative_normal", [], 1),
    ("negative_optimized", ["-O"], 1),
]:
    cmd = [sys.executable, *flags, str(CHECKER), "--json", str(OUT / (mode + ".json"))]
    if mode.startswith("negative"):
        cmd.append("--self-test-failure")
    started = datetime.now(timezone.utc).isoformat()
    result = subprocess.run(cmd, cwd=OUT, capture_output=True, text=True, timeout=120)
    (OUT / (mode + ".stdout.txt")).write_text(result.stdout, encoding="utf-8")
    (OUT / (mode + ".stderr.txt")).write_text(result.stderr, encoding="utf-8")
    record = json.loads((OUT / (mode + ".json")).read_text(encoding="utf-8"))
    runs.append({"mode": mode, "flags": flags, "started_utc": started, "returncode": result.returncode,
                 "expected_returncode": expected, "result": record,
                 "returncode_matches": result.returncode == expected})

after = {str(path.relative_to(SOURCE_ROOT)): digest(path) for path in SOURCES}
receipt = {"python_version": sys.version, "source_sha256_before": before, "source_sha256_after": after,
           "sources_unchanged": before == after, "runs": runs,
           "all_expected_returns": all(run["returncode_matches"] for run in runs),
           "lean_executed": False}
(OUT / "replay_receipt.json").write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(receipt, indent=2, sort_keys=True))
if not receipt["all_expected_returns"] or not receipt["sources_unchanged"]:
    raise SystemExit(1)
