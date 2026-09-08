"""Integrate reviewed proof drafts into the standalone mathematical fragment."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
manuscript = ROOT / "tex" / "connes_quotient_heat_transport.tex"
value = manuscript.read_text(encoding="utf-8")

def insert(draft_name, label, before, prefix=""):
    global value
    draft = ROOT / "checks" / draft_name
    if label in value or not draft.exists():
        return
    assert value.count(before) == 1, before
    body = draft.read_text(encoding="utf-8")
    body = "\n".join(line for line in body.splitlines() if not line.startswith("%"))
    value = value.replace(before, prefix + body
                          + "\n\n" + before, 1)

insert("source_algebra_draft.tex", "sec:cq-sourcealgebra",
       "Even when $W_k$ is not closed")
insert("moebius_heat_draft.tex", "sec:cq-moebius",
       r"\section{The inverse-root cover, the branch locus, and arithmetic fibres}",
       "\\section{Arithmetic traces and their exact Mellin obstructions}\n"
       "\\label{sec:cq-arithmetic}\n")
insert("arithmetic_principal_parts_draft.tex", "eq:cq-principalparts",
       r"\subsection{An exact arithmetic inverse for every heated Hermite trace}")
insert("analytic_quotient_topology_draft.tex", "thm:cq-jet-topology",
       r"\subsection{Exact derivative domains inside the analytic relation}")
insert("new_mellin_image/mellin_characterization_draft.tex",
       "sec:cq-Schwartz-Mellin-image",
       r"\subsection{An exact arithmetic inverse for every heated Hermite trace}")
insert("exponential_trace_domain_draft.tex", "sec:cq-exponential-trace",
       r"\subsection{An exact arithmetic inverse for every heated Hermite trace}")
insert("arithmetic_mellin_heat_draft.tex", "sec:cq-meromorphic-arithmetic-heat",
       r"\section{The inverse-root cover, the branch locus, and arithmetic fibres}")
insert("heat_persistent_core_draft.tex", "sec:cq-persistent-heat-core",
       r"\section{The inverse-root cover, the branch locus, and arithmetic fibres}")
insert("xi4_heat_return_draft.tex", "sec:cq-xi4-heat-returns",
       r"\section{The inverse-root cover, the branch locus, and arithmetic fibres}")
insert("../sources/source_sobolev_followup/sobolev_comparison.tex",
       "sec:cq-sobolev-comparison",
       r"\section{Proof scope and reproducibility}")
insert("bilaplacian_source_residue_draft.tex",
       "sec:cq-bilaplacian-source",
       r"\section{Proof scope and reproducibility}")
insert("moving_finite_jets_draft.tex",
       "sec:cq-moving-finite-jets",
       r"\section{Proof scope and reproducibility}")
insert("modular_cartan_heat_draft.tex",
       "sec:cq-cartan-heat",
       r"\section{Proof scope and reproducibility}")
insert("ns_cartan_006/diffusion_splitting_integrated_draft.tex",
       "sec:cq-spatial-diffusion-splitting",
       r"\section{Proof scope and reproducibility}")
insert("ns_flow_transfer_007.tex",
       "sec:cq-NS-profile-transfer",
       r"\section{Proof scope and reproducibility}")
insert("ns_actual_witness_007.tex",
       "sec:cq-NS-actual-witness",
       r"\section{Proof scope and reproducibility}")
insert("flow_quotient_007/flow_quotient_draft.tex",
       "sec:cq-flow-source-quotient",
       r"\section{Proof scope and reproducibility}")
insert("source_spectral_strength_007.tex",
       "sec:cq-source-spectral-strength",
       r"\section{Proof scope and reproducibility}")
value = "\n".join(line for line in value.splitlines() if not line.startswith("%")) + "\n"
manuscript.write_text(value, encoding="utf-8")
print("Reviewed available proof drafts integrated into the standalone fragment.")
