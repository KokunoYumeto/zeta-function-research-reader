"""Execute the independent shell fixture in four modes and retain exact receipts."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys

work = Path(__file__).resolve().parent
stem = work / "kernel_layer_shell_negative_20260912"
script = stem.with_suffix(".py")
records = {}
for mode, optimized, negative in [("normal", False, False), ("optimized", True, False),
                                  ("negative_normal", False, True), ("negative_optimized", True, True)]:
    output = Path(str(stem) + "_" + mode + ".json")
    log = Path(str(stem) + "_" + mode + ".log")
    command = [sys.executable] + (["-O"] if optimized else []) + [str(script), "--json", str(output)]
    if negative:
        command.append("--self-test-failure")
    run = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=False)
    log.write_bytes(run.stdout)
    expected_exit = 1 if negative else 0
    if run.returncode != expected_exit:
        raise RuntimeError(f"Unexpected exit in {mode}: {run.returncode}; expected {expected_exit}")
    result = json.loads(output.read_bytes())
    if (result["tests_run"], result["failures"], result["errors"], result["success"]) != (
            17 if negative else 16, 1 if negative else 0, 0, not negative):
        raise RuntimeError(f"Unexpected test result in {mode}")
    records[mode] = {"command": command, "exit_code": run.returncode, "expected_exit_code": expected_exit,
                     "result_path": str(output), "result_sha256": hashlib.sha256(output.read_bytes()).hexdigest(),
                     "log_path": str(log), "log_sha256": hashlib.sha256(run.stdout).hexdigest(), "result": result}


def mathematical_record(result):
    return {key: value for key, value in result.items() if key != "python_optimization"}


normal_equal = mathematical_record(records["normal"]["result"]) == mathematical_record(records["optimized"]["result"])
negative_equal = mathematical_record(records["negative_normal"]["result"]) == mathematical_record(records["negative_optimized"]["result"])
if not (normal_equal and negative_equal):
    raise RuntimeError("Ordinary and optimized exact mathematical records differ")
receipt = {
    "scope": "Single finite shell-rank fixture for KL.11-KL.18 with original measure and right inverse; no arithmetic or Lean certification",
    "script_path": str(script), "script_sha256": hashlib.sha256(script.read_bytes()).hexdigest(),
    "runner_path": str(Path(__file__)), "runner_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "python_executable": sys.executable,
    "normal_optimized_mathematical_records_identical": normal_equal,
    "negative_normal_optimized_mathematical_records_identical": negative_equal,
    "negative_control": "The intentionally false equality rank(projected actual derivative)=rank(raw homogeneous shell) is rejected as 0 != 1 in both Python modes.",
    "records": records,
}
receipt_path = Path(str(stem) + "_receipt.json")
receipt_path.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"receipt": str(receipt_path), "script_sha256": receipt["script_sha256"],
                  "ranks": records["normal"]["result"]["ranks"],
                  "modes": {name: {"exit_code": item["exit_code"], "tests_run": item["result"]["tests_run"],
                                   "failures": item["result"]["failures"], "errors": item["result"]["errors"]}
                            for name, item in records.items()}}, indent=2))
