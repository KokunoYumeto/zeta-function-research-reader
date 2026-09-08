"""Freeze the exact new source objects and read the primary closing clauses."""
from pathlib import Path
import hashlib
import json
import shutil
import ast
import ctypes
import os

ROOT=Path(__file__).resolve().parents[1]
tree=ast.parse((ROOT/"checks"/"verify_exact.py").read_text(encoding="utf-8"))
node=next(n for n in tree.body if isinstance(n,ast.FunctionDef)
          and n.name=="install_memory_ceiling")
exec(compile(ast.Module(body=[node],type_ignores=[]),"<resource policy>","exec"))
resource=install_memory_ceiling()
import fitz

dest=ROOT/"sources"/"flow_007"
dest.mkdir(exist_ok=True)
base=Path(r"[local]/Documents\math\output\dbn_ns_rh_20260908")
items=[
 (base/"tex"/"ns_arithmetic_flow.tex","82e369b60c195d06d3bc4a07b47e2b2ec764c1b9e36bc3a5982179ff87cca7cc"),
 (base/"tex"/"ns_public_witness.tex","ae7775c16c2c5188d4431eaf27d6c861c7e3f69f912f03feb5466cf1ea8eac93"),
 (base/"tex"/"heat_connection.tex",None),
 (Path(r"[local]/Documents\math\output\navier_stokes_research_2026-09-08\downloaded_public_release\navier-stokes.pdf"),
  "0e779481c4da40bd28d1e642e1d8ca57447d129610df28dfa5a11e9af8ae228f")]
records=[]
for path,expected in items:
    actual=hashlib.sha256(path.read_bytes()).hexdigest()
    if expected:
        assert actual==expected,(path,actual)
    frozen=dest/path.name
    if frozen.exists():
        assert frozen.read_bytes()==path.read_bytes()
    else:
        shutil.copyfile(path,frozen)
    records.append({"filename":path.name,"sha256":actual,"bytes":path.stat().st_size})
with fitz.open(dest/"navier-stokes.pdf") as pdf:
    selected=[6,7,115,118,119,120,121,124,125]
    value="\n".join(f"\n--- PRINTED/PDF PAGE {n} ---\n"+pdf[n-1].get_text()
                    for n in selected)
    (dest/"primary_closing_pages.txt").write_text(value,encoding="utf-8")
(dest/"intake_receipt.json").write_text(json.dumps(
    {"sources":records,"primary_pages_extracted":selected,"resource":resource,
     "entire_companion_flow_and_witness_read":True,
     "heat_connection_read_lines":"171–245",
     "full_166_page_proof_independently_verified":False},indent=2)+"\n")
print(json.dumps({"sources":records,"primary_page_extract":str(dest/"primary_closing_pages.txt")}))
