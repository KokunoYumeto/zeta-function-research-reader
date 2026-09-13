"""Verify staged PR15 bytes/API evidence without invoking Lean or editing sources."""
from __future__ import annotations

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
HEAD = "21970bbf4760d0bbca512a4a7996a2e38f968947"
EXPECTED = {
    "SplitZeroBoundaryControl.lean": "78bd445b8efcde4e8e58bc489a574195f3606df9335eaeff659d0dac419343f7",
    "SplitZeroControlCompression.lean": "9149de8bbaaf132569b5b61ec9e07b058d5d295e8f9a305fd70651831191aa10",
    "SplitZeroKrylovStep.lean": "9f4902c3376bc3c3b92e3eedb4a67ca6a05b06dc2a0cea1fd2e558a0a2f2d225",
    "SplitZeroRelationLayer.lean": "719da6c00cc0e9fd828bc53753980314e2a442c27cb96ccede84c80b4c9c0578",
    "SplitZeroSupportChange.lean": "e245230b06d099fcf4c41948813a7f4d278379287506eca4293f28aa18957a26",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def read_json(name: str):
    return json.loads((ROOT / name).read_text(encoding="utf-8-sig"))


def hashes(path: Path):
    data = path.read_bytes()
    return {
        "path": path.relative_to(ROOT).as_posix(),
        "bytes": len(data),
        "sha256": hashlib.sha256(data).hexdigest(),
        "git_blob_sha1": hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest(),
    }


def main() -> None:
    pr = read_json("pr.json")
    changed = read_json("pr_files.json")
    run = read_json("actions_run.json")
    job = read_json("actions_job.json")
    require(pr["head"]["sha"] == HEAD, "PR head changed")
    require(len(changed) == 13 and all(f["status"] == "added" for f in changed), "PR change scope differs")
    source_records = []
    for entry in changed:
        path = ROOT / "files" / entry["filename"]
        record = hashes(path)
        require(record["git_blob_sha1"] == entry["sha"], "Git blob mismatch: " + entry["filename"])
        if path.name in EXPECTED:
            require(record["sha256"] == EXPECTED[path.name], "PR-body SHA256 mismatch: " + path.name)
        record["remote_path"] = entry["filename"]
        record["raw_url"] = "https://raw.githubusercontent.com/KokunoYumeto/zeta-function-research-reader/" + HEAD + "/" + entry["filename"]
        source_records.append(record)
    context_inventory = {f["name"]: f for f in read_json("formal_directory.json")}
    context_records = []
    for path in sorted((ROOT / "context/formal/splitzero").iterdir()):
        if not path.is_file():
            continue
        record = hashes(path)
        require(path.name in context_inventory, "Unexpected context file")
        require(record["git_blob_sha1"] == context_inventory[path.name]["sha"], "Context Git blob mismatch: " + path.name)
        context_records.append(record)
    spec = read_json("files/formal/splitzero/BOUNDARY_TARGETS.json")
    names = [n for ns in spec.values() for n in ns]
    require(len(spec) == 5 and len(names) == 38 and len(set(names)) == 38, "Boundary manifest scope differs")
    require(run["id"] == 34705607593 and run["head_sha"] == HEAD, "Wrong workflow run")
    require(run["status"] == "completed" and run["conclusion"] == "success", "Workflow run unsuccessful")
    require(job["id"] == 103584974563 and job["run_id"] == run["id"] and job["head_sha"] == HEAD, "Wrong job")
    require(job["status"] == "completed" and job["conclusion"] == "success", "Job unsuccessful")
    require(all(s["status"] == "completed" and s["conclusion"] == "success" for s in job["steps"]), "Step unsuccessful")
    previous_counts = {
        "tau": sum(map(len, read_json("context/formal/splitzero/TAU_RECOVERY_TARGETS.json").values())),
        "derived": sum(map(len, read_json("context/formal/splitzero/DERIVED_TARGETS.json").values())),
        "structural": len(re.findall(r"^#print axioms ", (ROOT / "context/formal/splitzero/Audit.lean").read_text(), re.M)),
    }
    require(previous_counts == {"tau": 87, "derived": 73, "structural": 28}, "Prior manifest scope differs")
    receipt = {
        "schema": "splitzero-pr15-source-status-audit/1",
        "verified_at_utc": datetime.now(timezone.utc).isoformat(),
        "repository": "KokunoYumeto/zeta-function-research-reader",
        "head_commit": HEAD,
        "pr": {"number": 15, "state": pr["state"], "draft": pr["draft"], "base_ref": pr["base"]["ref"], "base_commit": pr["base"]["sha"]},
        "execution_evidence": {
            "origin": "GitHub Actions; primary REST run/job status and exact workflow source inspected",
            "run_id": run["id"], "job_id": job["id"], "head_sha": HEAD,
            "run_conclusion": run["conclusion"], "job_conclusion": job["conclusion"],
            "steps": [{k: s[k] for k in ("number", "name", "status", "conclusion")} for s in job["steps"]],
            "raw_job_log_retrieved": False,
            "raw_log_access": "Public job-log endpoint returned HTTP403: Must have admin rights to Repository",
            "artifact_count": 0,
            "local_lean_executed": False,
            "local_transitive_axiom_log_replay": False,
        },
        "source_audit": {
            "all_five_new_lean_sources_read_completely": True,
            "full_research_note_read": True,
            "source_git_blobs_verified": len(source_records),
            "new_lean_sha256_matched_pr_body": 5,
            "selected_boundary_declarations": len(names),
            "selected_boundary_modules": len(spec),
            "boundary_manifest": spec,
            "prior_manifest_counts": previous_counts,
            "declaration_counts_are_not_theorem_or_discovery_counts": True,
            "source_scope_findings": [
                "Finite raw Krylov expansion constructs the escape law and BoundaryControl.Data.",
                "Boundary rank-two form and rank-one Gram downdate are formally derived.",
                "Generalized-eigenvalue/Loewner norm identification is a written proof; Lean checks constituent compression identities.",
                "Reflection, relative Gram-determinant identity/inequality, theta density and arithmetic integer-tail bound are written, outside the new 38-target manifest.",
                "Actual theta range, integration by parts, arbitrary-stage Gram expansion and specific support-changing homotopy are not bundled analytic Lean instantiations.",
                "Inherited VALIDATION.json is an older structural certificate for commit8196e4f4..., not a PR15 certificate.",
            ],
        },
        "sources": source_records,
        "context_sources": context_records,
        "api_snapshots": [hashes(ROOT / n) for n in ["pr.json", "pr_files.json", "actions_run.json", "actions_job.json", "formal_directory.json", "log_artifact_access.json"]],
    }
    (ROOT / "SOURCE_STATUS_RECEIPT.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"head": HEAD, "source_blobs_verified": len(source_records), "context_blobs_verified": len(context_records), "boundary_declarations": len(names), "run": run["conclusion"], "job": job["conclusion"], "local_lean": False, "receipt": str(ROOT / "SOURCE_STATUS_RECEIPT.json")}, indent=2))


if __name__ == "__main__":
    main()
