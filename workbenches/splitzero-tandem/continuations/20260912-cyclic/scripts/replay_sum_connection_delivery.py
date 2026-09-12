"""Replay the unmodified Sum Connection delivery and preserve exact evidence.

Requires the delivery-declared SymPy 1.14.0. Outputs only to --output.
The finite tests are not an analytic, interval, or Lean certificate.
"""
from __future__ import annotations
import argparse
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import time
import urllib.request
import zipfile


def sha(b):
    return hashlib.sha256(b).hexdigest()


def blob(b):
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()


def save(p, obj):
    p.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Split-Zero-source-review", "Accept": "application/vnd.github+json"})
    with urllib.request.urlopen(req, timeout=45) as r:
        return r.read()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--source", required=True, type=Path)
    ap.add_argument("--archive", required=True, type=Path)
    ap.add_argument("--output", required=True, type=Path)
    ap.add_argument("--remote", action="store_true")
    args = ap.parse_args()
    import sympy
    if sympy.__version__ != "1.14.0":
        raise RuntimeError("Delivery declares SymPy 1.14.0; provide that version explicitly.")
    source, out = args.source.resolve(), args.output.resolve()
    if source == out or source in out.parents:
        raise RuntimeError("Output must remain outside the frozen source directory")
    out.mkdir(parents=True, exist_ok=True)
    before = {str(p.relative_to(source)): sha(p.read_bytes()) for p in source.rglob("*") if p.is_file()}
    receipt = {"created_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
               "python": sys.version, "executable": sys.executable,
               "sympy": sympy.__version__, "sympy_file": sympy.__file__,
               "source": str(source), "archive": str(args.archive.resolve()),
               "archive_bytes": args.archive.stat().st_size,
               "archive_sha256": sha(args.archive.read_bytes()),
               "scope": "Exact source-byte and finite-check replay; no analytic, interval, or Lean certificate."}
    manifest = json.loads((source / "MANIFEST.sha256.json").read_text(encoding="utf-8"))
    rows, members = [], []
    with zipfile.ZipFile(args.archive) as z:
        prefix = source.name + "/"
        for info in z.infolist():
            if info.is_dir():
                continue
            p = Path(info.filename)
            if p.is_absolute() or ".." in p.parts or not info.filename.startswith(prefix):
                raise RuntimeError("Unexpected archive member: " + info.filename)
            rel = info.filename[len(prefix):]
            b = z.read(info)
            local = source / rel
            members.append({"path": rel, "bytes": len(b), "sha256": sha(b),
                            "staged_match": local.exists() and local.read_bytes() == b})
        for rel, expected in manifest.items():
            b = z.read(prefix + rel)
            rows.append({"path": rel, "bytes": len(b), "sha256": sha(b),
                         "expected": expected,
                         "matches": len(b) == expected["bytes"] and sha(b) == expected["sha256"]})
    receipt["archive_members"] = members
    receipt["manifest_entries"] = rows
    receipt["unlisted_members"] = [r["path"] for r in members if r["path"] not in manifest]
    receipt["all_archive_members_match_stage"] = all(r["staged_match"] for r in members)
    receipt["all_manifest_entries_match"] = all(r["matches"] for r in rows)
    if not receipt["all_archive_members_match_stage"] or not receipt["all_manifest_entries_match"]:
        save(out / "replay_receipt.json", receipt)
        raise RuntimeError("Frozen archive or manifest verification failed")
    inherited = []
    for mp in (source / "sources").glob("*/MANIFEST.sha256.json"):
        entries = json.loads(mp.read_text(encoding="utf-8"))
        present = []
        missing = []
        for rel, expected in entries.items():
            p = mp.parent / rel
            if not p.is_file():
                missing.append(rel)
                continue
            b = p.read_bytes()
            present.append({"path": rel, "matches": sha(b) == expected["sha256"] and len(b) == expected["bytes"]})
        inherited.append({"manifest": str(mp.relative_to(source)), "total_entries": len(entries),
                          "present": present, "not_in_delivery_subset": missing})
    receipt["inherited_manifest_subsets"] = inherited
    save(out / "replay_receipt.json", receipt)
    runs = []
    for name, optimized, negative in [("normal", False, False), ("optimized", True, False),
                                      ("negative_normal", False, True), ("negative_optimized", True, True)]:
        wd = out / name
        wd.mkdir(exist_ok=True)
        script = wd / "check_sum_connection.py"
        shutil.copyfile(source / script.name, script)
        command = [sys.executable, "-B"] + (["-O"] if optimized else []) + [str(script), "--json", str(wd / "result.json")]
        if negative:
            command.append("--self-test-failure")
        start = time.monotonic()
        cp = subprocess.run(command, cwd=wd, capture_output=True, text=True, timeout=600)
        (wd / "stdout.log").write_text(cp.stdout, encoding="utf-8")
        (wd / "stderr.log").write_text(cp.stderr, encoding="utf-8")
        result = json.loads((wd / "result.json").read_text(encoding="utf-8"))
        ok = (cp.returncode == (1 if negative else 0) and result["tests_run"] == (21 if negative else 20)
              and result["failures"] == (1 if negative else 0) and result["errors"] == 0
              and result["success"] == (not negative) and result["sympy"] == "1.14.0")
        row = {"mode": name, "command": command, "exit_code": cp.returncode,
               "seconds": time.monotonic() - start, "record": result, "expected_behavior": ok,
               "checker_sha256": sha(script.read_bytes())}
        runs.append(row)
        receipt["runs"] = runs
        save(out / "replay_receipt.json", receipt)
        print(json.dumps({"mode": name, "expected_behavior": ok, "seconds": row["seconds"]}), flush=True)
        if not ok:
            raise RuntimeError("Unexpected checker behavior")
    receipt["success_records_byte_identical"] = (out / "normal/result.json").read_bytes() == (out / "optimized/result.json").read_bytes()
    if args.remote:
        remote = out / "remote"
        remote.mkdir(exist_ok=True)
        delivery = json.loads((source / "GITHUB_DELIVERY.json").read_text(encoding="utf-8"))
        repo = delivery["repository"]
        api = "https://api.github.com/repos/" + repo
        try:
            pr_bytes = fetch(api + "/pulls/" + str(delivery["pull_request"]))
            (remote / "pull_request.json").write_bytes(pr_bytes)
            pr = json.loads(pr_bytes)
            files_bytes = fetch(api + "/pulls/" + str(delivery["pull_request"]) + "/files?per_page=100")
            (remote / "pull_request_files.json").write_bytes(files_bytes)
            files = json.loads(files_bytes)
            commit = delivery["head_commit"]
            tree_bytes = fetch(api + "/git/trees/" + commit + "?recursive=1")
            (remote / "pinned_tree.json").write_bytes(tree_bytes)
            tree = json.loads(tree_bytes)
            tree_blobs = {r["path"]: r["sha"] for r in tree["tree"] if r["type"] == "blob"}
            compares = []
            for item in files:
                rel = item["filename"]
                if rel not in tree_blobs:
                    compares.append({"path": rel, "at_pinned_head": False})
                    continue
                b = fetch("https://raw.githubusercontent.com/" + repo + "/" + commit + "/" + rel)
                dest = remote / "pinned_files" / rel
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_bytes(b)
                matches = [str(p.relative_to(source)) for p in source.iterdir() if p.is_file() and p.read_bytes() == b]
                compares.append({"path": rel, "at_pinned_head": True, "bytes": len(b), "sha256": sha(b),
                                 "git_blob": blob(b), "tree_blob": tree_blobs[rel],
                                 "tree_blob_match": blob(b) == tree_blobs[rel], "matching_local_members": matches})
            receipt["remote"] = {"observed_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
                                  "url": pr["html_url"], "state": pr["state"], "draft": pr["draft"],
                                  "merged": pr["merged"], "merged_at": pr["merged_at"],
                                  "live_head": pr["head"]["sha"], "pinned_head": commit,
                                  "pinned_equals_live": pr["head"]["sha"] == commit,
                                  "live_base": pr["base"]["sha"], "changed_files": pr["changed_files"],
                                  "pinned_tree_truncated": tree.get("truncated"), "files": compares}
        except Exception as exc:
            receipt["remote"] = {"error": type(exc).__name__ + ": " + str(exc), "status_verified": False}
    after = {str(p.relative_to(source)): sha(p.read_bytes()) for p in source.rglob("*") if p.is_file()}
    receipt["source_bytes_unchanged"] = before == after
    receipt["finished_utc"] = dt.datetime.now(dt.timezone.utc).isoformat()
    save(out / "replay_receipt.json", receipt)
    print(json.dumps({"source_bytes_unchanged": before == after,
                      "manifest_entries": len(rows), "archive_members": len(members),
                      "remote": receipt.get("remote", {}), "receipt": str(out / "replay_receipt.json")}), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
