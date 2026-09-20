"""Root replay of the independent exact tests; stdout is preserved in full."""
from pathlib import Path
import hashlib
import json
import re
import subprocess
import sys

HERE = Path(__file__).resolve().parent
script = HERE / "independent_dyson/check_exact.py"
if not script.exists():
    script = HERE / "check_exact.py"
before = hashlib.sha256(script.read_bytes()).hexdigest()
records = []
for mode, flags in (("normal", []), ("optimized", ["-O"])):
    run = subprocess.run(
        [sys.executable, "-B", "-X", "utf8"] + flags + [str(script)],
        capture_output=True, text=True, encoding="utf-8", check=True,
    )
    matches = re.findall(r"PASS (\d+) exact checks; no floating point used.", run.stdout)
    if len(matches) != 1:
        raise RuntimeError("Missing independent test completion")
    (HERE / ("INDEPENDENT_ROOT_" + mode.upper() + ".txt")).write_text(
        run.stdout, encoding="utf-8")
    records.append({"mode": mode, "checks": int(matches[0]), "exit_code": run.returncode,
                    "stdout_sha256": hashlib.sha256(run.stdout.encode()).hexdigest()})
    print(json.dumps(records[-1]), flush=True)
after = hashlib.sha256(script.read_bytes()).hexdigest()
if before != after or records[0]["stdout_sha256"] != records[1]["stdout_sha256"]:
    raise RuntimeError("Checker changed or execution modes disagree")
receipt = {"checker_sha256": after, "runs": records,
           "scope": "Exact finite tests, including repeated squared eigenvalues and rational certified heat intervals.",
           "new_negative_controls_claimed": 0}
(HERE / "INDEPENDENT_ROOT_REPLAY.json").write_text(
    json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
