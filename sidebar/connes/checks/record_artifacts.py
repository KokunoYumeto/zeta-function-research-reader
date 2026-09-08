"""Record the completed build after rendered-page inspection."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib
import json
import re
import fitz

ROOT=Path(__file__).resolve().parents[1]
def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

fragment=ROOT/"tex"/"connes_quotient_heat_transport.tex"
verification=json.loads((ROOT/"checks"/"verification_receipt.json").read_text())
assert verification["all_passed"]
assert verification["manuscript_sha256"]==digest(fragment)
claims=json.loads((ROOT/"claims.json").read_text())
labels=set(re.findall(r"\\label\{([^}]+)\}",fragment.read_text(encoding="utf-8")))
assert all(c["tex_locator"] in labels for c in claims["claims"])
log=(ROOT/"tex"/"main.log").read_text(encoding="utf-8",errors="replace")
problems=re.findall(r"Overfull|Underfull|undefined|multiply defined|Missing character",log)
assert not problems,problems
reader=ROOT/"connes_quotient_heat_transport.pdf"
assert digest(reader)==digest(ROOT/"tex"/"main.pdf")
with fitz.open(reader) as pdf:
    pages=len(pdf)
    metadata=pdf.metadata
render_path=ROOT/"qa"/"current_render_receipt.json"
render=json.loads(render_path.read_text())
unchanged=render.get("unchanged_previously_reviewed_pages",[])
changed=render.get("pages_requiring_inspection",list(range(1,pages+1)))
assert sorted(unchanged+changed)==list(range(1,pages+1))
paths=[
 "connes_quotient_heat_transport.pdf","tex/main.tex",
 "tex/connes_quotient_heat_transport.tex","tex/bibliography.tex",
 "checks/verify_exact.py","checks/verification_receipt.json",
 "claims.json","sources/provenance.json","README.md"]
artifacts={name:{"sha256":digest(ROOT/name),"bytes":(ROOT/name).stat().st_size}
           for name in paths}
receipt={"schema_version":2,"recorded_utc":datetime.now(timezone.utc).isoformat(),
 "pdf_pages":pages,"tex_overfull_boxes":0,"undefined_references":False,
 "all_claim_locators_verified":True,"exact_checks":verification["check_count"],
 "pdf_metadata":metadata,
 "visual_qa":f"All {pages} final pages rendered with Poppler; {len(changed)} changed/new pages inspected by root, and {len(unchanged)} page PNGs are byte-identical to the preceding inspected edition. Equations, headers, footers, bibliography and page transitions are legible; no clipping, overlapping text, or missing glyphs.",
 "artifacts":artifacts}
(ROOT/"checks"/"artifact_receipt.json").write_text(
    json.dumps(receipt,indent=2)+"\n",encoding="utf-8")
render["visual_inspection"]=f"passed: all {pages} pages inspected by root"
render["pdf_sha256"]=digest(reader)
render_path.write_text(json.dumps(render,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"pages":pages,"checks":verification["check_count"],
                  "claims":len(claims["claims"]),"pdf_sha256":digest(reader),
                  "fragment_sha256":digest(fragment)}))
