"""Bind review, exact editions, execution, logs and substantive failure sites."""
import difflib
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(value, message):
    if not value:
        raise RuntimeError(message)


def main():
    first = ROOT / "SC1_SC37_CAPTURE.tex"
    layout = ROOT / "SC1_SC37_LAYOUT_CAPTURE.tex"
    require(digest(first) == "0aedbaf3481f3a8e88c91ec786a44cd26869f0b0988d927a43ffaf54ad906e20", "original edition hash")
    require(digest(layout) == "f7cbbb2da3a97722c9f9128602b4de64ad1ab9cfccdbb03e8ee9363321f7de63", "reviewed layout edition hash")
    diff = "".join(difflib.unified_diff(first.read_text(encoding="utf-8").splitlines(keepends=True),
                                       layout.read_text(encoding="utf-8").splitlines(keepends=True),
                                       fromfile=first.name, tofile=layout.name))
    (ROOT / "LAYOUT_ONLY_DIFF.txt").write_text(diff, encoding="utf-8", newline="\n")
    receipt = ROOT / "EXECUTION_RECEIPT.json"
    execution = json.loads(receipt.read_text(encoding="utf-8"))
    require(execution["status"] == "all_expected_outcomes_verified", "execution state")
    for field in ("source", "checker", "runner"):
        require(digest(ROOT / execution[field]) == execution[field + "_sha256"], field + " pin")
    expected_messages = {"normal_sign": "SC12 complex sign and scale", "metric_order": "SC25 metric factor order",
                         "drop_minor_factor": "SC34 both neighboring minors", "tor_scale": "SC30 retained derivative scale"}
    artifacts = {first.name, layout.name, "LAYOUT_ONLY_DIFF.txt", receipt.name,
                 "CONSTITUENT_CURVATURE_REVIEW.md", "check_constituent_curvature.py", "run_review.py", Path(__file__).name}
    for row in execution["runs"]:
        log = ROOT / row["log"]
        out = ROOT / row["receipt"]
        require(digest(log) == row["log_sha256"] and digest(out) == row["receipt_sha256"], "full run artifact hashes")
        data = json.loads(out.read_text(encoding="utf-8"))
        require(data["checker_sha256"] == digest(ROOT / "check_constituent_curvature.py"), "run checker pin")
        text = log.read_text(encoding="utf-8")
        if data["mutation"]:
            require("AssertionError: " + expected_messages[data["mutation"]] in text, "substantive failure site")
        else:
            require("Ran 13 tests" in text and "\nOK\n" in text, "successful full output")
        artifacts.update([row["log"], row["receipt"]])
    bound = [{"path": name, "bytes": (ROOT / name).stat().st_size, "sha256": digest(ROOT / name)} for name in sorted(artifacts)]
    final = dict(schema=1, status="independent_review_complete_no_mathematical_correction",
                 reviewed_source_sha256=digest(first), layout_equivalent_source_sha256=digest(layout),
                 execution_receipt_sha256=digest(receipt),
                 successful_methods_each_mode=13, substantive_mutations_each_mode=4,
                 exact_fixture_degree_pairs=[[2, 1], [3, 2], [4, 2], [4, 1], [4, 3]],
                 source_edited=False, remote_writes=False, lean_executed=False,
                 contour_evaluated=False, arithmetic_estimate_proved=False,
                 mathematical_review="Complete captured SC1--SC37 and complete subsequent two-hunk layout-equivalent diff.",
                 artifacts=bound,
                 excluded_development_artifacts=["normal.json"])
    out = ROOT / "REVIEW_RECEIPT.json"
    out.write_text(json.dumps(final, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"path": str(out), "sha256": digest(out), "bound_artifact_count": len(bound)}, indent=2))


if __name__ == "__main__":
    main()
