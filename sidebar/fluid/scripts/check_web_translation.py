"""Replay the original eleven translation checks in a fresh offline subset.

The original checker is unchanged. Its complete proof is staged at the
original relative filename, so no source workspace or external file is read.
Run from any working directory with Python and SymPy 1.13.1.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
PROVENANCE = "scripts/web_audit/translation_provenance.json"
CHILD = r'''
import os,pathlib,runpy,sys
stage=pathlib.Path(sys.argv[1]).resolve()
script=pathlib.Path(sys.argv[2]).resolve()
allowed=(stage,pathlib.Path(sys.prefix).resolve(),pathlib.Path(sys.base_prefix).resolve())
def audit(event,args):
    if event.startswith("socket.") or event.startswith("subprocess.") or event in ("os.system","os.exec","os.posix_spawn","os.spawn"):
        raise PermissionError("Offline translation replay forbids: "+event)
    if event=="open" and isinstance(args[0],(str,bytes,os.PathLike)):
        candidate=pathlib.Path(os.fsdecode(args[0])).resolve()
        if not any(candidate==base or candidate.is_relative_to(base) for base in allowed):
            raise PermissionError("File open outside fresh subset and Python runtime")
sys.addaudithook(audit)
if not __debug__:
    raise RuntimeError("Original assertions must remain enabled")
runpy.run_path(str(script),run_name="__main__")
'''


def member(base, relative):
    name = Path(relative)
    if name.is_absolute() or ".." in name.parts:
        raise ValueError("Invalid relative member")
    target = (base / name).resolve()
    if not target.is_relative_to(base.resolve()):
        raise ValueError("Member escapes root")
    return target


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT/"research/web_translation_replay.json")
    args = parser.parse_args()
    provenance_bytes = (ROOT/PROVENANCE).read_bytes()
    provenance = json.loads(provenance_bytes)
    script_entry = next(x for x in provenance["source_files"] if x["portable_path"].endswith("/replay_translation.py"))
    receipt_entry = next(x for x in provenance["source_files"] if x["portable_path"].endswith("/translation_receipt.json"))
    proof_entry = provenance["proof"]
    inputs = {proof_entry["path"]: proof_entry, script_entry["portable_path"]: script_entry,
              receipt_entry["portable_path"]: receipt_entry}
    data = {}
    for relative, entry in inputs.items():
        raw = member(ROOT, relative).read_bytes()
        if len(raw) != entry["bytes"] or hashlib.sha256(raw).hexdigest() != entry["sha256"]:
            raise AssertionError("Frozen translation input differs: "+relative)
        data[relative] = raw
    with tempfile.TemporaryDirectory(prefix="web-translation-fresh-") as temporary:
        stage = Path(temporary).resolve()
        for relative, destination in provenance["replay_layout"].items():
            target = member(stage, destination)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data[relative])
        script = member(stage, provenance["replay_layout"][script_entry["portable_path"]])
        env = dict(os.environ)
        for key in ("PYTHONPATH","PYTHONHOME","PYTHONSTARTUP","PYTHONOPTIMIZE"):
            env.pop(key, None)
        completed = subprocess.run([sys.executable,"-B","-I","-c",CHILD,str(stage),str(script)],
            cwd=stage, env=env, text=True, encoding="utf-8", errors="replace",
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
        if completed.returncode:
            raise RuntimeError(completed.stdout+completed.stderr)
        replay = json.loads(script.with_name("translation_receipt.json").read_bytes())
    original = json.loads(data[receipt_entry["portable_path"]])
    if replay["count"] != provenance["expected_count"] or not replay["all_passed"]:
        raise AssertionError("Translation replay count or status mismatch")
    if replay["proof_sha256"] != proof_entry["sha256"] or replay["script_sha256"] != script_entry["sha256"]:
        raise AssertionError("Replayed proof/script hash mismatch")
    for key in ("scope","count","all_passed","checks","proof_sha256","script_sha256"):
        if replay[key] != original[key]:
            raise AssertionError("Original result content differs: "+key)
    result = {
        "schema":"portable-web-translation-replay-v1","status":"passed",
        "executed_count":replay["count"],"fresh_subset":True,
        "original_mathematical_script_byte_preserved":True,
        "original_check_results_agree":True,
        "network_and_subprocess_denied_in_check_process":True,
        "file_opens_restricted_to_fresh_subset_and_python_runtime":True,
        "source_workspace_read":False,"lean_used":False,
        "proof_sha256":proof_entry["sha256"],
        "source_script_sha256":script_entry["sha256"],
        "wrapper_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "provenance_sha256":hashlib.sha256(provenance_bytes).hexdigest(),
        "scope":provenance["scope"],"limitations":provenance["limitations"],
        "original_replay":replay,"navier_stokes_disproof_established":False,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"status":"passed","executed_count":replay["count"],
        "fresh_subset":True,"proof_sha256":proof_entry["sha256"]}))


if __name__ == "__main__":
    main()
