"""Reproducible complete Markdown-to-LaTeX transport; no proof abridgment."""
from pathlib import Path
import hashlib
import json
import subprocess

HERE = Path(__file__).resolve().parent
source = HERE / "independent_dyson/INDEPENDENT_PROOF.md"
if not source.exists():
    source = HERE / "INDEPENDENT_PROOF.md"
converted = subprocess.run(
    ["pandoc", "--from=markdown+tex_math_single_backslash",
     "--to=latex", "--wrap=none", str(source)],
    capture_output=True, text=True, encoding="utf-8", check=True,
).stdout
header = r"""\documentclass[11pt]{article}
\usepackage{amsmath,amssymb,amsthm}
\usepackage[hidelinks]{hyperref}
\providecommand{\tightlist}{\setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}
\providecommand{\passthrough}[1]{#1}
\begin{document}
"""
footer = r"""
\section*{Human-source context and the receiving calculation}
The trace-action context is Alain Connes and Walter D. van Suijlekom,
\emph{Quadratic Forms, Real Zeros and Echoes of the Spectral Action},
\href{https://arxiv.org/abs/2511.23257v1}{arXiv:2511.23257v1},
section \emph{Spectral action and divided differences},
source labels lem:sa and prop:der-sa.
The theta heat context is Alain Connes, \emph{Heat Expansion and Zeta},
\href{https://arxiv.org/abs/2402.13082v1}{arXiv:2402.13082v1},
equation ft. Root read both complete original TeX sources; the
independent derivation above did not inspect them and is not a separate
human authority. The finite trace and Duhamel identities used here are
proved in full above; no priority claim is made for these general
finite-matrix formulas.
In the receiving arithmetic construction, $A$ is the attained polynomial
compression, $Q=A-M$ is its outgoing rank-one relation, and $M$ is
multiplication in the original cyclic quotient. The metric is the
least-source-norm metric $G$, not a replacement metric. Therefore
ID6--ID7 apply to the same finite arithmetic allowance
$\kappa=\epsilon^2$. They calculate curvature at $t=0$; they neither
replace the full $t=1$ heat difference nor prove decay as the
arithmetic degree grows. The complete construction and maps remain in
NH1--NH36 and HM1--HM19 in this edition.
\end{document}
"""
target = HERE / "INDEPENDENT_HEAT_CURVATURE.tex"
data = (header + converted + footer).encode()
if (HERE / "transaction/PLAN.json").exists():
    if not target.exists() or target.read_bytes() != data:
        raise RuntimeError("Refusing change after publication freeze")
target.write_bytes(data)
receipt = {
    "source": source.name,
    "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
    "target": target.name,
    "target_sha256": hashlib.sha256(data).hexdigest(),
    "complete_source_converted": True,
    "conversion": "Pandoc markdown+tex_math_single_backslash to LaTeX; full source retained",
    "added_context": "Point-of-use human sources and exact original arithmetic receiving objects.",
}
(HERE / "INDEPENDENT_CONVERSION.json").write_text(
    json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
print(json.dumps(receipt))
