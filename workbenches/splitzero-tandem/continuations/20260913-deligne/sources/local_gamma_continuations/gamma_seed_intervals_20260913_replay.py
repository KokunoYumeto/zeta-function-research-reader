"""Bounded fresh normal/optimized replay and exact endpoint validation."""
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
PREFIX = "gamma_seed_intervals_20260913"
CHECKER = ROOT / (PREFIX + "_check.py")
PROOF = ROOT / (PREFIX + ".tex")


def need(value, message):
    if not value:
        raise RuntimeError(message)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    jobs = []
    modes = {}
    for optimized in [False, True]:
        mode = "optimized" if optimized else "normal"
        for fault in ["none", "endpoint-factor", "reference-mass", "fourth-sign", "tail-omission"]:
            suffix = mode if fault == "none" else mode + "_fault_" + fault
            path = ROOT / (PREFIX + "_" + suffix + ".json")
            argv = [sys.executable, "-B"] + (["-O"] if optimized else [])
            argv += [str(CHECKER), "--output", str(path), "--fault", fault]
            completed = subprocess.run(argv, capture_output=True, text=True, timeout=60)
            stdout = ROOT / (PREFIX + "_" + suffix + ".stdout.txt")
            stderr = ROOT / (PREFIX + "_" + suffix + ".stderr.txt")
            stdout.write_text(completed.stdout, encoding="utf-8")
            stderr.write_text(completed.stderr, encoding="utf-8")
            need(completed.returncode == (0 if fault == "none" else 1), "unexpected exit status")
            receipt = json.loads(path.read_text(encoding="utf-8"))
            need(receipt["optimization_flag"] == int(optimized), "actual execution mode mismatch")
            need(receipt["script_sha256"] == sha(CHECKER), "executed checker hash mismatch")
            need(receipt["status"] == ("passed" if fault == "none" else "rejected"), "fault status mismatch")
            need(receipt["failed_fault_checks"] == int(fault != "none"), "fault rejection count mismatch")
            need(receipt["incomplete_gamma_recurrence_checks"] == 512, "incomplete-gamma check coverage changed")
            if fault == "none":
                modes[mode] = receipt
            jobs.append({"mode": mode, "fault": fault, "exit_code": completed.returncode,
                         "receipt": path.name, "receipt_sha256": sha(path),
                         "stdout": stdout.name, "stdout_sha256": sha(stdout),
                         "stderr": stderr.name, "stderr_sha256": sha(stderr),
                         "argument_template": ["<PYTHON>", "-B"] + (["-O"] if optimized else [])
                             + ["<WORK>/"+CHECKER.name, "--output", "<WORK>/"+path.name, "--fault", fault],
                         "status": receipt["status"]})
    left = dict(modes["normal"])
    right = dict(modes["optimized"])
    left.pop("optimization_flag")
    right.pop("optimization_flag")
    need(left == right, "normal and optimized mathematical records differ")
    endpoint_checks = []
    for key, data in left["results"].items():
        low, high = Fraction(data["lower"]), Fraction(data["upper"])
        dyadic_low, dyadic_high = Fraction(data["exact_lower_dyadic"]), Fraction(data["exact_upper_dyadic"])
        need(low == Fraction(data["lower_rational"]) and high == Fraction(data["upper_rational"]), "rational decimal map mismatch")
        need(low < dyadic_low <= dyadic_high < high, "exact endpoint inclusion failed")
        need(high-low == Fraction(3, 10**40), "published interval width mismatch")
        endpoint_checks.append({"quantity": key, "width_exact": str(high-low), "strict_inclusion": True})
    payload = {"schema": "gamma-seed-replay-v1", "status": "passed", "jobs": jobs,
               "checker_sha256": sha(CHECKER), "proof_sha256": sha(PROOF),
               "normal_optimized_mathematical_records_identical": True,
               "positive_runs": 2, "negative_runs_rejected": 8,
               "endpoint_checks": endpoint_checks,
               "scope": "Fresh subprocess observation with exact mode fields; nine scalar enclosures, four infinite theta moments; no truncation-agreement certificate."}
    output = ROOT / (PREFIX + "_replay.json")
    output.write_text(json.dumps(payload, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({"status": "passed", "positive_runs": 2, "negative_runs_rejected": 8,
                      "exact_interval_checks": len(endpoint_checks), "output": str(output)}))


if __name__ == "__main__":
    main()
