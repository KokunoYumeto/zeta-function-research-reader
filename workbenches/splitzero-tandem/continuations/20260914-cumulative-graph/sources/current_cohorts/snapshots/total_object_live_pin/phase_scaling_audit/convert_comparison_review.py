from pathlib import Path
import re

folder = Path(__file__).resolve().parent
source = (folder / "comparison_review.md").read_text(encoding="utf-8")
body = source[source.index("## 1. Original spaces"):source.index("The entire original H note was read.")]
lines = []
for line in body.splitlines():
    if line.startswith("### "):
        line = r"\subsubsection{" + line[4:] + "}"
    elif line.startswith("## "):
        heading = re.sub(r"^\d+\.\s*", "", line[3:])
        line = r"\subsection{" + heading + "}"
    lines.append(line)
body = "\n".join(lines) + "\n"
body = re.sub(r"PC\.(\d+)", lambda m: "PSC." + str(int(m.group(1)) + 8), body)
body = ("% Complete original-source gluing comparison and residue calculation.\n"
        "% Derived from comparison_review.md; source provenance is recorded there.\n"
        "% Tags PSC.9--PSC.64. This file has no preamble or nested inputs.\n\n"
        + body)
target = folder / "phase_gluing_residue.tex"
target.write_text(body, encoding="utf-8")
tags = re.findall(r"\\tag\{(PSC\.\d+)\}", body)
assert tags == [f"PSC.{i}" for i in range(9, 65)], tags
assert r"\begin{document}" not in body
assert r"\input{" not in body
assert not re.search(r"^#{1,6} ", body, re.M)
print(f"Wrote {target}: {len(body.encode('utf-8'))} bytes, {len(tags)} unique tags")
