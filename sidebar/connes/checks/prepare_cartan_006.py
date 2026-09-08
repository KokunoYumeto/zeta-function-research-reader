"""Freeze the supplied Cartan input and prepare the reviewed spatial notation."""
from pathlib import Path
import hashlib
import json
import shutil

ROOT=Path(__file__).resolve().parents[1]
source=Path(r"[local]/Documents\Papors\Chatnotes\transcripts\New folder\modular_cartan_realform_bridge_20260719.tex")
dest=ROOT/"sources"/"cartan_006"
dest.mkdir(exist_ok=True)
frozen=dest/source.name
if frozen.exists():
    assert frozen.read_bytes()==source.read_bytes()
else:
    shutil.copyfile(source,frozen)
draft=ROOT/"checks"/"ns_cartan_006"/"diffusion_splitting_draft.tex"
value=draft.read_text(encoding="utf-8")
value=value.replace(r"\begin{proposition}",r"\begin{cqproposition}")
value=value.replace(r"\end{proposition}",r"\end{cqproposition}")
# Preserve all operators and coefficients; avoid colliding with the
# antiunitary J in the preceding subsection.
value=value.replace("J",r"\mathcal I ")
(draft.parent/"diffusion_splitting_integrated_draft.tex").write_text(value,encoding="utf-8")
new_pdf=Path(r"[local]/Documents\math\output\navier_stokes_research_2026-09-08\downloaded_public_release\navier-stokes.pdf")
actual=hashlib.sha256(new_pdf.read_bytes()).hexdigest()
assert actual=="0e779481c4da40bd28d1e642e1d8ca57447d129610df28dfa5a11e9af8ae228f"
receipt={"cartan_sha256":hashlib.sha256(frozen.read_bytes()).hexdigest(),
         "cartan_read_lines":["1-240","311-455"],
         "new_ns_pdf_sha256":actual,"new_ns_pdf_bytes":new_pdf.stat().st_size,
         "old_revision_retained":True,"full_revision_equivalence_claimed":False,
         "formal_kernel_verification_performed":False}
(dest/"source_receipt.json").write_text(json.dumps(receipt,indent=2)+"\n",encoding="utf-8")
print(json.dumps(receipt))

readme=ROOT/"README.md"
text=readme.read_text(encoding="utf-8")
text=text.replace("Bibliographic dependencies are the four entries",
                  "Bibliographic dependencies are the entries")
text=text.replace(
    "A fresh bounded audit of Connes's Selecta primary text confirms that its explicit topologies belong to the adele ring, a weighted Hilbert completion, and Bruhat–Schwartz test functions. None defines the entire-function topology used for the arithmetic quotient.",
    "A bounded inspection of Connes's Selecta primary text locates explicit topologies on the adele ring, a weighted Hilbert completion, and Bruhat–Schwartz test functions. Its inspected passages and explicit term searches did not locate a definition of the entire-function topology used for the arithmetic quotient; this is a bounded source finding, not an exhaustive absence theorem.")
readme.write_text(text,encoding="utf-8")
provenance_script=ROOT/"checks"/"record_provenance.py"
text=provenance_script.read_text(encoding="utf-8")
text=text.replace(
    "The fresh complete Selecta audit finds that its topological-ring phrase concerns adeles, its weighted Hilbert norms concern a separate completion, and its inductive-limit topology concerns Bruhat–Schwartz functions; none defines H_{<=1} or tau.",
    "The bounded Selecta inspection locates the adele topological-ring phrase, weighted Hilbert norms, and Bruhat–Schwartz inductive-limit topology. Explicit term searches and inspected passages did not locate the CCM entire-function topology tau; this is not an exhaustive absence proof. Corrected extraction counts and verified page locators are in checks/ns_cartan_006/topology_locator_correction.md.")
provenance_script.write_text(text,encoding="utf-8")

manuscript=ROOT/"tex"/"connes_quotient_heat_transport.tex"
text=manuscript.read_text(encoding="utf-8")
start=r"\section{The Cartan construction and an exact antiunitary reversal}"
end=r"\subsection{The retained spatial pullback, exact diffusion leakage, and feedback}"
if start in text and end in text:
    a=text.index(start)
    b=text.index(end,a)
    text=text[:a]+(ROOT/"checks"/"modular_cartan_heat_draft.tex").read_text(encoding="utf-8").strip()+"\n\n"+text[b:]
    a=text.index(end)
    b=text.index(r"\section{Proof scope and reproducibility}",a)
    next_section=text.find(r"\section{The published fluid input",a)
    if next_section!=-1:
        b=min(b,next_section)
    text=text[:a]+value.strip()+"\n\n"+text[b:]
    manuscript.write_text(text,encoding="utf-8")
