"""Bind existing normal/optimized endpoint-product audit results without reruns."""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent
STEM = "endpoint_product_independent_"
DATE = "_20260913"
EXPECTED = {
    "none": (2453, 0),
    "local-remainder": (2453, 1),
    "budget-denominator": (2453, 218),
    "endpoint-orientation": (2451, 120),
    "phase-feasibility": (2453, 8),
    "interior-multiplicity": (2453, 3),
}


def info(path):
    data = path.read_bytes()
    return {"path": path.name, "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}


def need(value, message):
    if not value:
        raise RuntimeError(message)


checker = ROOT / (STEM + "checker" + DATE + ".py")
checker_hash = info(checker)["sha256"]
run_rows = []
for mutation, (count, failed) in EXPECTED.items():
    pair = []
    for optimized in (False, True):
        mode = "optimized" if optimized else "normal"
        suffix = mode if mutation == "none" else mutation.replace("-", "_") + "_" + mode
        path = ROOT / (STEM + suffix + DATE + ".json")
        value = json.loads(path.read_text(encoding="utf-8"))
        need(value["checker_sha256"] == checker_hash, "checker source changed")
        need(value["mutation"] == mutation, "wrong mutation record")
        need(value["python_optimized"] == optimized, "wrong optimization mode")
        need(value["check_count"] == count, "unexpected check count")
        need(value["failed_count"] == failed, "unexpected failure count")
        need(value["passed_count"] == count - failed, "incorrect successful count")
        need(value["passed"] == (failed == 0), "incorrect pass status")
        need(len(value["records"]) == count, "missing per-check records")
        need(sum(not row["passed"] for row in value["records"]) == failed,
             "inconsistent failures")
        pair.append(value)
        run_rows.append({**info(path), "mutation": mutation,
                         "optimized": optimized, "checks": count,
                         "failed": failed, "expected_exit_code": int(failed > 0)})
    need(pair[0]["records"] == pair[1]["records"],
         "normal and optimized per-check records differ")

receipt = {
    "schema": "endpoint-product-independent-replay-receipt-v1",
    "review": info(ROOT / (STEM + "review" + DATE + ".md")),
    "checker": info(checker),
    "receipt_builder": info(Path(__file__).resolve()),
    "normal_optimized_record_equality": True,
    "all_expected_controls_rejected": True,
    "run_count": len(run_rows),
    "runs": run_rows,
    "passed": True,
}
output = ROOT / (STEM + "receipt" + DATE + ".json")
output.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"receipt": info(output), "passed": True, "run_count": len(run_rows)},
                 sort_keys=True))
