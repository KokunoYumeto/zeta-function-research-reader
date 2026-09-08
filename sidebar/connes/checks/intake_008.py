"""Freeze one new companion source and bounded primary axis pages."""
from pathlib import Path
import ast
import ctypes
import os
import hashlib
import json

ROOT=Path(__file__).resolve().parents[1]
tree=ast.parse((ROOT/"checks"/"verify_exact.py").read_text(encoding="utf-8"))
node=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=="install_memory_ceiling")
exec(compile(ast.Module(body=[node],type_ignores=[]),"<resource policy>","exec"))
resource=install_memory_ceiling()
import fitz

target=ROOT/"sources"/"angular_008"
target.mkdir(exist_ok=True)
source=Path(r"[local]/Documents\math\output\dbn_ns_rh_20260908\tex\ns_angular_mellin.tex")
data=source.read_bytes()
digest=hashlib.sha256(data).hexdigest()
assert digest=="59a477ff19fc593fb1f5550c98f34346f7cf5365b1fe0372e6935934e0263278"
(target/source.name).write_bytes(data)
pdf=ROOT/"sources"/"flow_007"/"navier-stokes.pdf"
pages=[24,25,26,45,46,47,48,49,50,51,124,144,145,146,147,148]
with fitz.open(pdf) as doc:
    excerpts="\n\n".join(f"=== PDF PAGE {n} ===\n"+doc[n-1].get_text(sort=True) for n in pages)
(target/"primary_axis_pages.txt").write_text(excerpts,encoding="utf-8")
receipt={"companion_path":str(source),"companion_sha256":digest,"bytes":len(data),
         "primary_pdf_sha256":hashlib.sha256(pdf.read_bytes()).hexdigest(),
         "extracted_one_based_pdf_pages":pages,"resource":resource,
         "read_status":"companion complete; primary extracted pages require content reading"}
(target/"intake_receipt.json").write_text(json.dumps(receipt,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"companion_sha256":digest,"pages":pages,"excerpt_characters":len(excerpts)}))
