"""Prepare complete read proofs with the receiving fragment's exact references."""
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
source=ROOT/"sources"/"flow_007"/"ns_public_witness.tex"
value=source.read_text(encoding="utf-8")
first=value.index(r"\subsection*{The precise imported witness")
value=(r"\subsection{The actual cutoff-summed source witness and its arithmetic image}"
       "\n"+r"\label{sec:cq-NS-actual-witness}"+"\n\n"+value[first:])
value=value.replace(r"\subsection*{",r"\subsubsection{")
start=value.index("We now use the particular field")
end=value.index("Use a star",start)
value=value[:start]+r"""We now use the particular field constructed in the
166-page revision of \cite{cqNS2026}. The original
cutoff-summed fields, the smooth extension of the force,
and their all-order estimates are the imported source input.
Its actual closing equations (9.21), (10.4)--(10.14) and
(10.20)--(10.23) were read directly. The complete companion
specialization \cite{cqNSWitness} was also read; all arithmetic,
flow, energy and terminal maps used here have their proofs below.
No independent verification of every lemma in the public
166-page existence proof is claimed.

"""+value[end:]
value=value.replace(r"\cite{openaiNS2026}",r"\cite{cqNS2026}")
value=value.replace(r"\ref{sec:naf}",r"\ref{sec:cq-NS-profile-transfer}")
value=value.replace(r"\eqref{naf:d}",r"\eqref{eq:cq-NS-profile-norm-constants}")
value=value.replace(r"\eqref{naf:accel}",r"\eqref{eq:cq-NS-profile-acceleration}")
value=value.replace(r"\eqref{naf:laplace}",r"\eqref{eq:cq-NS-material-viscous-residual}")
value=value.replace(r"\R",r"\mathbb R")
value=value.replace(r"\C",r"\mathbb C")
value=value.replace("{nw:","{eq:cq-nw:")
value=value.replace(
 "Retain $S=(F_1/2,F_2,F_3)$ and $J=DS$ in the physical Cartesian",
 r"Write $S=\mathbf S=(F_1/2,F_2,F_3)$ and $J=J_S=DS$ in the physical Cartesian")
needle="all stages and the finite initialization."
value=value.replace(needle,needle+r"""
With the source's own radial-time coordinate denoted $q_{\rm src}$
to distinguish it from our material label $q$, its exact sums are
\[
\begin{aligned}
 A_*&=A_{*,0}+\sum_{j\geq1}\chi(a_jq_{\rm src})A_{*,j},\\
 B_*e_\theta&=B_{*,0}e_\theta+
                        \sum_{j\geq1}\chi(a_jq_{\rm src})B_{*,j},\\
 p_{*,\mathrm{loc}}&=p_{*,0}+
                        \sum_{j\geq1}\chi(a_jq_{\rm src})p_{*,j}.
\end{aligned}
\]
The displayed $a_j,\chi$ and all finite-state representatives
are the actual choices in source (9.21); the subscript star
marks viscosity one and introduces no replacement of them.
""")
out=ROOT/"checks"/"ns_actual_witness_007.tex"
out.write_text(value,encoding="utf-8")
print("Complete actual-witness proof prepared with original constants and source references.")
