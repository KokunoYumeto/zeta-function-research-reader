"""Observe fresh exact-rational source-cost jobs and both optimization modes."""
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
PREFIX = "gamma_seed_intervals_20260913_source_costs"
CHECKER = ROOT / (PREFIX + "_check.py")


def need(value, message):
    if not value:
        raise RuntimeError(message)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


jobs = []
records = []
for optimized in [False, True]:
    mode = "optimized" if optimized else "normal"
    for fault in ["none", "drop-cross-term", "unit-mass", "Q0-less-one"]:
        suffix = mode if fault == "none" else mode + "_fault_" + fault
        out = ROOT / (PREFIX + "_" + suffix + ".json")
        command = [sys.executable, "-B"] + (["-O"] if optimized else [])
        command += [str(CHECKER), "--output", str(out), "--fault", fault]
        result = subprocess.run(command, capture_output=True, text=True, timeout=30)
        expected = 0 if fault == "none" else 1
        need(result.returncode == expected, "unexpected source-cost exit status")
        receipt = json.loads(out.read_text(encoding="utf-8"))
        need(receipt["optimization_flag"] == int(optimized), "observed optimization flag mismatch")
        need(receipt["script_sha256"] == sha(CHECKER), "executed script pin mismatch")
        need(receipt["failed_fault_checks"] == expected, "fault rejection count mismatch")
        need(receipt["status"] == ("passed" if expected == 0 else "rejected"), "reported status mismatch")
        stdout, stderr = out.with_suffix(".stdout.txt"), out.with_suffix(".stderr.txt")
        stdout.write_text(result.stdout, encoding="utf-8")
        stderr.write_text(result.stderr, encoding="utf-8")
        if fault == "none":
            records.append(receipt)
        jobs.append({"mode": mode, "fault": fault, "exit_code": result.returncode,
                     "receipt": out.name, "receipt_sha256": sha(out),
                     "stdout": stdout.name, "stdout_sha256": sha(stdout),
                     "stderr": stderr.name, "stderr_sha256": sha(stderr),
                     "argument_template": ["<PYTHON>", "-B"] + (["-O"] if optimized else [])
                          + ["<WORK>/"+CHECKER.name, "--output", "<WORK>/"+out.name, "--fault", fault]})
first, second = [dict(r) for r in records]
first.pop("optimization_flag")
second.pop("optimization_flag")
need(first == second, "normal and optimized cost mathematics differs")
for name, interval in first["results"].items():
    low, high = Fraction(interval["lower"]), Fraction(interval["upper"])
    need(low < Fraction(interval["transport_lower_rational"]) <= Fraction(interval["transport_upper_rational"]) < high,
         "source-cost exact rational containment failed")
    need(high-low == Fraction(3, 10**40), "source-cost exact interval width failed")
payload = {"schema": "gamma-source-costs-replay-v1", "status": "passed", "jobs": jobs,
           "proof_fragment_sha256": sha(ROOT / (PREFIX + ".tex")), "checker_sha256": sha(CHECKER),
           "moment_input_sha256": first["input_sha256"],
           "positive_runs": 2, "negative_runs_rejected": 6, "exact_interval_checks": len(first["results"]),
           "normal_optimized_mathematical_records_identical": True,
           "new_quadrature_performed": False}
out = ROOT / (PREFIX + "_replay.json")
out.write_text(json.dumps(payload, indent=2)+"\n", encoding="utf-8")
print(json.dumps({"status": "passed", "positive_runs": 2, "negative_runs_rejected": 6,
                  "exact_interval_checks": len(first["results"]), "output": str(out)}))
