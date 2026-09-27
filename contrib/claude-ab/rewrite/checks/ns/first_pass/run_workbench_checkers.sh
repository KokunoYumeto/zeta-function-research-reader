#!/usr/bin/env bash
# Re-run the workbench's own finite checkers on scratch copies (read-only use of the sources).
# 1. the source bundle's nine replay programs (scripts/replay_checks.py) and the additional-replay driver;
# 2. the vacuum-hydrodynamics continuation's verify_recovered_formulas.py;
# 3. a hash check of all 119 bundle members against navier_stokes_primary_manifest.json;
# 4. a content comparison of the regenerated receipts with the shipped ones.
set -u
WB=$(cd "${WB:-navier-stokes}" && pwd)   # the YM repository folder navier-stokes/ at fa79faf
OUT=$(cd "${OUT:-.}" && pwd)
SCR=$OUT/scratch
rm -rf "$SCR/bundle_run" && mkdir -p "$SCR/bundle_run"
( cd "$SCR/bundle_run" && unzip -q -o "$WB/navier_stokes_source_bundle.zip" )
cp -r "$SCR/bundle_run" "$SCR/bundle_pristine_tmp"
echo "== bundle member hashes vs primary manifest (pristine extraction, before any replay)"
python3 - <<EOF
import json, hashlib, os
d = json.load(open("$WB/navier_stokes_primary_manifest.json"))
ok = sum(hashlib.sha256(open(os.path.join("$SCR/bundle_pristine_tmp", f["path"]), "rb").read()).hexdigest() == f["sha256"] for f in d["files"])
print("members matching manifest sha256: %d of %d" % (ok, len(d["files"])))
EOF
echo "== python / sympy / mpmath versions"
python3 -c "import sys, sympy, mpmath; print(sys.version.split()[0], sympy.__version__, mpmath.__version__)"
echo "== bundle replay_checks.py (nine programs)"
( cd "$SCR/bundle_run" && python3 scripts/replay_checks.py ) 2>&1
echo "== bundle replay_additional_checks.py"
( cd "$SCR/bundle_run" && python3 scripts/replay_additional_checks.py ) 2>&1
echo "== regenerated receipts vs shipped receipts (parsed-JSON comparison; shipped files use CRLF)"
python3 - <<EOF
import json, os
base = "$SCR/bundle_pristine_tmp"; run = "$SCR/bundle_run"
names = ["proof_sources/profiles/exact_checks.json", "proof_sources/base_heat/identity_check_results.json",
         "proof_sources/oscillations/exact_checks_results.json", "proof_sources/mean_corrections/exact_checks.json",
         "proof_sources/stage9/exact_checks.json", "proof_sources/profile_assembly_audit/exact_assembly_checks.json",
         "proof_sources/stage_inputs_audit/exponent_checks.json", "proof_sources/stage_inputs_audit/maps_covariance/exact_checks.json",
         "proof_sources/stage_inputs_audit/radial_fiveeq/exact_checks.json"]
for n in names:
    a = json.load(open(os.path.join(base, n))); b = json.load(open(os.path.join(run, n)))
    print(("same content  " if a == b else "CONTENT DIFFERS  ") + n)
EOF
rm -rf "$SCR/bundle_pristine_tmp"
echo "== continuation verify_recovered_formulas.py (run on a copy)"
cp "$WB/continuations/20260919-vacuum-hydrodynamics/verify_recovered_formulas.py" "$SCR/verify_recovered_formulas_copy.py"
( cd "$SCR" && python3 verify_recovered_formulas_copy.py ) 2>&1
