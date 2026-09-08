"""Synchronize the four current proof drafts without deleting earlier sections."""
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
manuscript=ROOT/"tex"/"connes_quotient_heat_transport.tex"
text=manuscript.read_text(encoding="utf-8")
sections=[
 (r"\section{The published fluid input and its complete arithmetic profile map}","ns_flow_transfer_007.tex"),
 (r"\subsection{The actual cutoff-summed source witness and its arithmetic image}","ns_actual_witness_007.tex"),
 (r"\section{The actual source quotient of a flow-driven arithmetic profile}","flow_quotient_007/flow_quotient_draft.tex"),
 (r"\section{The exact strength of the frozen source spectral information}","source_spectral_strength_007.tex"),
 (r"\section{Proof scope and reproducibility}",None)]
for j in range(len(sections)-1):
    start,draft=sections[j]
    end=sections[j+1][0]
    a=text.index(start)
    b=text.index(end,a)
    body=(ROOT/"checks"/draft).read_text(encoding="utf-8").strip()
    text=text[:a]+body+"\n\n"+text[b:]
manuscript.write_text(text,encoding="utf-8")
print("Current complete proofs synchronized.")
