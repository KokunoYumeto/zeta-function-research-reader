"""Bind the reviewed source and verify existing checker records, without reruns.

The required source hash is supplied only after its bytes have been read and
reviewed. This script checks provenance and result consistency, not proofs.
"""
import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent


def need(value, message):
    if not value:
        raise RuntimeError(message)


def info(path):
    data = path.read_bytes()
    return {"path": path.relative_to(ROOT).as_posix(), "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}


parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--source-sha256", required=True)
args = parser.parse_args()
source = ROOT / "endpoint_product_sharpening_20260913.tex"
need(info(source)["sha256"] == args.source_sha256, "reviewed source pin changed")

primary_checker = ROOT / "endpoint_product_check_20260913.py"
primary_receipt = ROOT / "endpoint_product_replay_20260913.json"
primary = json.loads(primary_receipt.read_text(encoding="utf-8"))
need(primary["checker_sha256"] == info(primary_checker)["sha256"],
     "primary checker pin changed")
need(primary["all_accepted"], "primary replay was not accepted")
expected = {"none": 0, "mass": 6, "interior": 13, "beta": 25,
            "schur": 26, "phase": 5, "raw_factorial": 2}
groups = {}
primary_runs = []
for run in primary["runs"]:
    mode, mutation = run["mode"], run["mutant"]
    need(mode in ("normal", "optimized"), "unknown mode")
    need(mutation in expected, "unknown primary mutation")
    path = ROOT / run["record"]
    need(info(path)["sha256"] == run["record_sha256"], "primary record pin changed")
    row = json.loads(path.read_text(encoding="utf-8"))
    need(row["checker_sha256"] == primary["checker_sha256"], "record checker mismatch")
    need(row["optimized"] == (mode == "optimized"), "record mode mismatch")
    need(row["mutant"] == mutation, "record mutation mismatch")
    need(row["checks_executed"] == 415, "primary check count changed")
    need(len(row["checks"]) == 415, "missing primary check details")
    need(row["failed_count"] == expected[mutation], "primary failure count changed")
    need(sum(not c["passed"] for c in row["checks"]) == expected[mutation],
         "primary failure detail mismatch")
    need(run["checks_executed"] == row["checks_executed"], "receipt count mismatch")
    need(run["failed_count"] == row["failed_count"], "receipt failure mismatch")
    need(run["exit_code"] == int(mutation != "none"), "unexpected primary exit")
    need(run["accepted"], "primary result not accepted")
    key = (mutation, mode)
    need(key not in groups, "duplicate primary run")
    groups[key] = row
    primary_runs.append({**info(path), "mode": mode, "mutation": mutation,
                         "checks": 415, "failed": expected[mutation],
                         "exit_code": run["exit_code"]})
need(len(groups) == 14, "missing primary runs")
for mutation in expected:
    normal = groups[(mutation, "normal")]
    optimized = groups[(mutation, "optimized")]
    need(normal["checks"] == optimized["checks"], "paired primary checks differ")
    need(normal["certificates"] == optimized["certificates"],
         "paired primary certificates differ")

fixture, certificate = groups[("none", "normal")]["certificates"]
f = Fraction
x_lo, x_hi = f(certificate["x_lower"]), f(certificate["x_upper"])
bound_lo, bound_hi = f(certificate["bound_lower"]), f(certificate["bound_upper"])
R, U = f(fixture["R"]), f(fixture["U"])
def budget_ratio(x):
    return (1 + 2*x)*(1 + x)**4 / ((1 - 2*x)*(1 - x)**4)
def window_max(x):
    return (2*x)**6 / ((1 - 4*x*x)*(1 - x*x)**2)
certificate_checks = {
    "literal_budget_input": R == f(630509, 1080),
    "literal_norm_ratio": U == 60,
    "interior_optimizer_bracket": 0 < x_lo < x_hi < f(1, 2),
    "optimizer_lower_comparison": budget_ratio(x_lo) <= R,
    "optimizer_upper_comparison": R <= budget_ratio(x_hi),
    "sixth_power_lower_comparison": bound_lo**6 <= U*window_max(x_lo),
    "sixth_power_upper_comparison": U*window_max(x_hi) <= bound_hi**6,
    "displayed_EP54_lower": bound_lo == f(719736229856370310835738215, 2**88),
    "displayed_EP54_upper": bound_hi == f(719736229856370310835738217, 2**88),
}
need(all(certificate_checks.values()), "displayed rational certificate failed")

independent_receipt = ROOT / "endpoint_product_independent_receipt_20260913.json"
independent = json.loads(independent_receipt.read_text(encoding="utf-8"))
need(independent["passed"], "independent replay not accepted")
need(independent["run_count"] == 12, "independent run count changed")
for field in ("review", "checker", "receipt_builder"):
    record = independent[field]
    need(info(ROOT / record["path"])["sha256"] == record["sha256"],
         "independent artifact changed")
for record in independent["runs"]:
    need(info(ROOT / record["path"])["sha256"] == record["sha256"],
         "independent run record changed")

text = source.read_text(encoding="utf-8")
tags = re.findall(r"\\tag\{(EP\.[^}]+)\}", text)
need(len(tags) == len(set(tags)), "duplicate proof tags")
expected_tags = {f"EP.{j}" for j in range(1, 55)}
expected_tags.update("EP.38" + letter for letter in "abcdefghijk")
expected_tags.update("EP.50" + letter for letter in "abcdef")
need(expected_tags.issubset(tags), "missing reviewed proof tags")
receipt = {
    "schema": "endpoint-product-full-source-independent-review-v1",
    "reviewed_source": {**info(source), "lines": len(text.splitlines()),
                        "equation_tags": tags},
    "full_source_review": info(ROOT / "endpoint_product_full_source_review_20260913.md"),
    "scalar_review": info(ROOT / "endpoint_product_independent_review_20260913.md"),
    "balanced_source_read_in_full": info(ROOT / "endpoint_product_dependencies_20260913"
                                        / "FOUR_VOLUME_THRESHOLD.md"),
    "arithmetic_analytic_review_read_in_full": info(ROOT / "arithmetic_endpoint_analytic_independent_review_20260913.md"),
    "primary_checker_read_in_full": info(primary_checker),
    "primary_replay": info(primary_receipt),
    "primary_runs": primary_runs,
    "primary_normal_optimized_checks_and_certificates_identical": True,
    "displayed_EP54_exact_fraction_checks": certificate_checks,
    "independent_scalar_replay": info(independent_receipt),
    "source_edits_performed_by_reviewer": False,
    "primary_checker_rerun_by_reviewer": False,
    "reviewer_executed_scalar_checker": True,
    "arithmetic_constant_numerically_enclosed": False,
    "remaining_relation_volume_upper_bound_claimed": False,
    "binding_script": info(Path(__file__).resolve()),
    "passed": True,
}
output = ROOT / "endpoint_product_full_source_review_receipt_20260913.json"
output.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"receipt": info(output), "passed": True}, sort_keys=True))
