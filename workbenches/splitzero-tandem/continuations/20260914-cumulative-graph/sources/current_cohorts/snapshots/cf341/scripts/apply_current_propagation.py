"""Install complete reviewed revisions, preserving every preceding presentation.

This local collection step follows assemble_continuation.py. A standalone reader
already contains the revised TeX and does not need to execute either collector.
All three disjoint mathematical lanes must be ready before any target is edited.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import shutil

ROOT = Path(__file__).resolve().parents[1]
TOTAL = ROOT.parents[1] / "work/rh_counterfactual_20260913/total_object"
LANES = ("propagation_metric", "propagation_support", "propagation_boundary")


def sha(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def read(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def preserve(source, target):
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        if sha(target) != sha(source):
            raise RuntimeError(f"Refusing to replace preserved input: {target}")
    else:
        shutil.copy2(source, target)


def main():
    plans = []
    targets = set()
    lane_records = []
    for lane_name in LANES:
        lane = TOTAL / lane_name
        manifest_path = lane / "PROPAGATION_MANIFEST.json"
        manifest = read(manifest_path)
        if manifest.get("status") != "ready":
            raise RuntimeError(f"Mathematical lane is not ready: {lane_name}")
        review = Path(manifest["review"])
        if not review.is_absolute():
            review = lane / review
        if not review.is_file():
            raise RuntimeError(f"Missing full mathematical review: {review}")
        lane_records.append({"lane": lane_name, "manifest_sha256": sha(manifest_path),
                             "review": str(review), "review_sha256": sha(review)})
        for entry in manifest["entries"]:
            relative = Path(entry["target"])
            destination = (ROOT / relative).resolve()
            if not destination.is_relative_to((ROOT / "tex").resolve()):
                raise RuntimeError(f"Revision target is outside the reader TeX: {relative}")
            key = relative.as_posix()
            if key in targets:
                raise RuntimeError(f"Competing whole-file mathematical revisions: {key}")
            targets.add(key)
            source = Path(entry["source"])
            if not source.is_absolute():
                source = lane / source
            if sha(source) != entry["new_sha256"]:
                raise RuntimeError(f"Reviewed source bytes changed: {source}")
            current = sha(destination)
            if current not in (entry["old_sha256"], entry["new_sha256"]):
                raise RuntimeError(f"Unexpected preceding presentation: {destination}")
            history = ROOT / "provenance/preceding_341_presentations" / relative
            if current == entry["new_sha256"] and not history.is_file():
                raise RuntimeError(f"Revised target lacks its preserved predecessor: {destination}")
            if history.exists() and sha(history) != entry["old_sha256"]:
                raise RuntimeError(f"Preserved predecessor changed: {history}")
            plans.append((lane_name, entry, source, destination, history, current))

    old_manifest_path = ROOT / "provenance/PROOF_INPUT_MANIFEST.json"
    continuation_path = ROOT / "provenance/CONTINUATION_INPUT_MANIFEST.json"
    old_manifest = read(old_manifest_path)
    continuation = read(continuation_path)
    old_by_path = {Path(row["included_copy"]).as_posix(): row for row in old_manifest}
    new_by_path = {Path(row["included"]).as_posix(): row
                   for row in continuation["entries"]}
    # Prepare every exact historical source needed by the integrity verifier.
    for lane_name, entry, source, destination, history, current in plans:
        key = Path(entry["target"]).as_posix()
        row = new_by_path.get(key)
        if row is not None and "original_copy" not in row:
            original = Path(row["source"])
            if sha(original) != row["source_sha256"]:
                raise RuntimeError(f"Original authored source changed before preservation: {original}")

    for lane_name in LANES:
        lane = TOTAL / lane_name
        def ignore(directory, names):
            return [name for name in names if name in ("build", "__pycache__")
                    or name.endswith((".pdf", ".png", ".aux", ".log", ".toc", ".out"))]
        shutil.copytree(lane, ROOT / "propagation_sources" / lane_name,
                        dirs_exist_ok=True, ignore=ignore)

    changes = []
    for lane_name, entry, source, destination, history, current in plans:
        key = Path(entry["target"]).as_posix()
        if current == entry["old_sha256"]:
            preserve(destination, history)
        revision_copy = ROOT / "propagation_sources" / lane_name / "installed" / key
        revision_copy.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, revision_copy)
        shutil.copy2(source, destination)
        if sha(destination) != entry["new_sha256"]:
            raise RuntimeError(f"Revised file copy failed: {destination}")
        record = {**entry, "lane": lane_name,
                  "preserved_previous": history.relative_to(ROOT).as_posix(),
                  "included_revision_source": revision_copy.relative_to(ROOT).as_posix()}
        changes.append(record)
        row = old_by_path.get(key)
        if row is not None:
            row["preceding_included_sha256"] = entry["old_sha256"]
            row["included_sha256"] = entry["new_sha256"]
            row["current_revision"] = revision_copy.relative_to(ROOT).as_posix()
            row["transformation"] = (
                "Original cross-reference namespacing followed by complete mathematical "
                "backward/forward propagation; exact previous presentation and authored "
                "source retained. See CURRENT_PROPAGATION_MANIFEST.json.")
        row = new_by_path.get(key)
        if row is not None:
            if "original_copy" not in row:
                original_copy = ROOT / "provenance/propagation_original_inputs" / (row["code"] + ".tex")
                preserve(Path(row["source"]), original_copy)
                row["original_copy"] = original_copy.relative_to(ROOT).as_posix()
            row["preceding_included_sha256"] = entry["old_sha256"]
            row["included_sha256"] = entry["new_sha256"]
            row["current_revision"] = revision_copy.relative_to(ROOT).as_posix()
            row["transformation"] = (
                "Complete mathematical backward/forward propagation after the preceding "
                "assembly transformation. Original authored source and preceding included "
                "presentation retained. See CURRENT_PROPAGATION_MANIFEST.json.")

    old_manifest_path.write_text(json.dumps(old_manifest, indent=2), encoding="utf-8")
    continuation_path.write_text(json.dumps(continuation, indent=2), encoding="utf-8")
    result = {"at": datetime.now(timezone.utc).isoformat(), "lanes": lane_records,
              "entries": changes, "frozen_editions_changed": False,
              "scope": "Current mathematical presentations and their actual downstream uses; "
                       "not an assertion that the research goal or RH is resolved."}
    (ROOT / "provenance/CURRENT_PROPAGATION_MANIFEST.json").write_text(
        json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps({"revised_complete_files": len(changes),
                      "lanes": LANES, "preserved_predecessors": len(changes)}, indent=2))


if __name__ == "__main__":
    main()
