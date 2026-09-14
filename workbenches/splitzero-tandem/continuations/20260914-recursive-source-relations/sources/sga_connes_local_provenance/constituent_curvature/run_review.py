"""Run modest exact fixtures sequentially, retaining all output and receipts."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parent
CHECKER = ROOT / "check_constituent_curvature.py"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(ok, text):
    if not ok:
        raise RuntimeError(text)


def main():
    runs = []
    for mutation in (None, "normal_sign", "metric_order", "drop_minor_factor", "tor_scale"):
        receipt_bytes = []
        for optimized in (False, True):
            name = (mutation or "normal") + ("_optimized" if optimized else "_ordinary")
            receipt = ROOT / (name + ".json")
            log = ROOT / (name + ".log")
            command = [sys.executable] + (["-O"] if optimized else []) + [str(CHECKER), "--receipt", str(receipt)]
            if mutation:
                command += ["--mutation", mutation]
            start = time.monotonic()
            with log.open("w", encoding="utf-8", newline="\n") as output:
                result = subprocess.run(command, stdout=output, stderr=subprocess.STDOUT, check=False, timeout=240)
            data = json.loads(receipt.read_text(encoding="utf-8"))
            require(result.returncode == (1 if mutation else 0), name + ": exit code")
            require(data["errors"] == 0, name + ": unexpected error")
            require(data["failures"] == (1 if mutation else 0), name + ": assertion failures")
            require(data["methods"] == (1 if mutation else 13), name + ": method count")
            receipt_bytes.append(receipt.read_bytes())
            record = dict(name=name, command=command, exit_code=result.returncode,
                          elapsed_seconds=round(time.monotonic() - start, 3),
                          receipt=receipt.name, receipt_sha256=sha(receipt),
                          log=log.name, log_sha256=sha(log), methods=data["methods"],
                          failures=data["failures"], errors=data["errors"])
            runs.append(record)
            print(name + ": expected outcome; " + str(record["elapsed_seconds"]) + "s", flush=True)
        require(receipt_bytes[0] == receipt_bytes[1], (mutation or "normal") + ": ordinary/optimized receipt mismatch")
    result = dict(schema=1, status="all_expected_outcomes_verified", sequential=True,
                  python=sys.version, source="SC1_SC37_CAPTURE.tex", source_sha256=sha(ROOT / "SC1_SC37_CAPTURE.tex"),
                  checker=CHECKER.name, checker_sha256=sha(CHECKER),
                  runner=Path(__file__).name, runner_sha256=sha(Path(__file__)),
                  ordinary_and_optimized_receipts_identical=True,
                  successful_methods_per_mode=13, substantive_mutations_per_mode=4,
                  runs=runs,
                  scope="Finite exact rational/complex fixtures and ODE-implied period jets only. No contour evaluations, arithmetic estimates, or Lean execution.")
    out = ROOT / "EXECUTION_RECEIPT.json"
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("Complete: " + str(out), flush=True)


if __name__ == "__main__":
    main()
