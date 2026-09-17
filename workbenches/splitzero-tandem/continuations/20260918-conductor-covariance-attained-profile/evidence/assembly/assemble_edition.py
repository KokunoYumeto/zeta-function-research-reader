"""Build additive TeX sources after the root agent has sealed the mathematics.

No TeX process is launched by this script. All predecessors and fragments are
read-only inputs. Cumulative byte recovery is checked before any result is saved.
"""
from __future__ import annotations

import argparse
import collections
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
import re

HERE = Path(__file__).resolve().parent
TASK = HERE.parent
WORKSPACE = TASK.parents[1]
STAGING = WORKSPACE / "work/mixed_tail_continuation_20260917/full_receiver_build/staging"
FRAGMENTS = [
    ("01_WEIGHTED_CONDUCTOR_FORWARD.tex", WORKSPACE / "snapshots/weighted_conductor/WEIGHTED_CONDUCTOR_FORWARD.tex"),
    ("02_LRC_TRANSPORT_COMPLETE.tex", TASK / "transport/LRC_TRANSPORT_COMPLETE.tex"),
    ("03_LRC11_LRC12_FULL_PROOF.tex", TASK / "equilibrium/quantile/LRC11_LRC12_FULL_PROOF.tex"),
    ("04_EQUILIBRIUM_NORM_PROOF.tex", TASK / "equilibrium/EQUILIBRIUM_NORM_PROOF.tex"),
    ("05_GPA_ATTAINED_TAIL_PROOF.tex", TASK / "attained_tail/gpa/GPA_ATTAINED_TAIL_PROOF.tex"),
    ("06_ATTAINED_FIBRE_AND_PROFILE_PROPAGATION.tex", TASK / "attained_tail/ATTAINED_FIBRE_AND_PROFILE_PROPAGATION.tex"),
    ("07_LRC_SCALAR_RECONSTRUCTION.tex", TASK / "asymptotics/LRC_SCALAR_RECONSTRUCTION.tex"),
    ("08_ALL_NONZERO_ROW_ENVELOPE.tex", TASK / "attained_tail/ALL_NONZERO_ROW_ENVELOPE.tex"),
    ("09_PROFILE_COVARIANCE_BRIDGE.tex", TASK / "PROFILE_COVARIANCE_BRIDGE.tex"),
    ("10_ELLIPTIC_DERIVATIVE_PROOF.tex", TASK / "joint_review/elliptic/ELLIPTIC_DERIVATIVE_PROOF.tex"),
    ("11_FINITE_COMPARISON.tex", TASK / "joint_review/FINITE_COMPARISON.tex"),
    ("12_RECEIVER_UPDATES.tex", TASK / "RECEIVER_UPDATES.tex"),
]
BASE_NAMES = [
    "09_UPDATED_JOINT_NOTE.tex",
    "10_UPDATED_SIGNED_RETURN.tex",
    "14_CURRENT_KERNEL_AND_MULTIPLICITY_PROOFS.tex",
]
PRESENTATION_REPAIRS = {
    "01_WEIGHTED_CONDUCTOR_FORWARD.tex": [
        (r" w(t)=-i\arctan t=\tfrac12\log\frac{1-it}{1+it},\qquad", r"\begin{gathered}" + "\n" + r" w(t)=-i\arctan t=\tfrac12\log\frac{1-it}{1+it},\qquad", "Open a gathered display for WCF5."),
        (r" g(t)=t^{-v}e^{-4w(t)}E_A(w(t)),\quad", r" g(t)=t^{-v}e^{-4w(t)}E_A(w(t)),\\", "Break WCF5 between the analytic function and its zero value."),
        (r" g(0)=(-i)^v\mu_v/v!,\quad g(t)=\sum_{j\ge0}g_jt^j.", r" g(0)=(-i)^v\mu_v/v!,\quad g(t)=\sum_{j\ge0}g_jt^j." + "\n" + r"\end{gathered}", "Close the gathered WCF5 display."),
    ],
    "02_LRC_TRANSPORT_COMPLETE.tex": [
        (r"\operatorname{diag}(\rho_i)_{i=0}^D^{-1}", r"\bigl[\operatorname{diag}(\rho_i)_{i=0}^D\bigr]^{-1}", "Group the indexed diagonal matrix before the inverse superscript, repairing an invalid double superscript."),
        (r" t^vg_\flat(t)=H_\flat(t):=", r"\begin{gathered}" + "\n" + r" t^vg_\flat(t)=H_\flat(t):=", "Open a gathered display for LT8."),
        (r" \quad |\Re\lambda_{uw}|\le4\delta<2,", r" \\ |\Re\lambda_{uw}|\le4\delta<2,", "Break LT8 before the parameter bounds."),
        (r" \quad |\alpha_{uw}|,|\beta^{\flat}_{uw}|\le F_0.", r" \quad |\alpha_{uw}|,|\beta^{\flat}_{uw}|\le F_0." + "\n" + r"\end{gathered}", "Close the gathered LT8 display."),
        (r" a=4l+1\ge9,\quad q=(a+1)^2,\quad Q=(a-7)^2=q',\quad", r" a=4l+1\ge9,\quad q=(a+1)^2,\quad Q=(a-7)^2=q',\\", "Break the long first parameter row of XIM1."),
    ],
    "04_EQUILIBRIUM_NORM_PROOF.tex": [
        ("of \\(\\sin\\theta\\cos\\theta/\n\\sqrt{\\cos^2\\theta+s^2\\sin^2\\theta}\\) give", "of\n\\[\n\\frac{\\sin\\theta\\cos\\theta}{\\sqrt{\\cos^2\\theta+s^2\\sin^2\\theta}}\n\\]\ngive", "Display the long elliptic integrand instead of an unbreakable inline formula."),
    ],
    "05_GPA_ATTAINED_TAIL_PROOF.tex": [
        (r" \nu^+_{r,s}=\min_{f\text{ monic},\,\deg f=r}", r"\begin{gathered}" + "\n" + r" \nu^+_{r,s}=\min_{f\text{ monic},\,\deg f=r}", "Open a gathered display for the two original monic minima ATG26."),
        (r"       \int|\chi_j(c_++iy)f(c_++iy)|^2dm_s(y),\qquad", r"       \int|\chi_j(c_++iy)f(c_++iy)|^2dm_s(y),\\", "Put the two ATG26 minima on separate rows."),
        (r"       \int|\chi_{j-8}(c_-+iy)f(c_-+iy)|^2dm_s(y).", r"       \int|\chi_{j-8}(c_-+iy)f(c_-+iy)|^2dm_s(y)." + "\n" + r"\end{gathered}", "Close the gathered ATG26 display."),
    ],
    "07_LRC_SCALAR_RECONSTRUCTION.tex": [
        ("\x0crac{m^2}{8n^2}", r"\frac{m^2}{8n^2}", "Repair the form-feed escape corruption of the fraction control sequence."),
        (r" a\equiv1\pmod4,\quad s\in\{1,a\},\quad", r"\begin{gathered}" + "\n" + r" a\equiv1\pmod4,\quad s\in\{1,a\},\quad", "Open a gathered display for scalar source parameters."),
        (r" q=(a+1)^2,\quad Q=(a-7)^2,\quad \Delta=q-Q=16a-48,", r" q=(a+1)^2,\quad Q=(a-7)^2,\\ \Delta=q-Q=16a-48,", "Break the long scalar parameter display."),
        (r" \quad \ell_s=(s-1)/4.", r" \quad \ell_s=(s-1)/4." + "\n" + r"\end{gathered}", "Close the scalar parameter display."),
    ],
    "09_PROFILE_COVARIANCE_BRIDGE.tex": [
        (r" a\sqrt{\delta^2+\gamma^2}\le2^{-33}q,\qquad", r"\begin{gathered}" + "\n" + r" a\sqrt{\delta^2+\gamma^2}\le2^{-33}q,\qquad", "Open a gathered display for PCB0."),
        (r" n_b=(b+1)^2+\ell_s\ge100,\quad", r" n_b=(b+1)^2+\ell_s\ge100,\\", "Break PCB0 before the root-radius guard."),
        (r"       \le2^{-17}n_b\quad(b=a,a-8).", r"       \le2^{-17}n_b\quad(b=a,a-8)." + "\n" + r"\end{gathered}", "Close the gathered PCB0 display."),
        (r" \left|\sum_{r\in B}\vartheta_r\gamma_{r,s}", r"\begin{gathered}" + "\n" + r" \left|\sum_{r\in B}\vartheta_r\gamma_{r,s}", "Open a gathered display for PCB7."),
        (r" \quad G(n,r)=2n\psi(r/n).", r" \\ G(n,r)=2n\psi(r/n)." + "\n" + r"\end{gathered}", "Put the definition of G on a separate PCB7 row."),
    ],
    "12_RECEIVER_UPDATES.tex": [
        (r" -E_Q^-\le\delta V_Q\le E_Q^+,\qquad", r"\begin{gathered}" + "\n" + r" -E_Q^-\le\delta V_Q\le E_Q^+,\qquad", "Open a gathered display for DRU10."),
        (r" E_Q^-=O_{\mathrm{actual}}(k^2\log k),\qquad", r" E_Q^-=O_{\mathrm{actual}}(k^2\log k),\\", "Break DRU10 before the upper allowance."),
        (r"            +O_{\mathrm{actual}}(k\log q_k).", r"            +O_{\mathrm{actual}}(k\log q_k)." + "\n" + r"\end{gathered}", "Close the gathered DRU10 display."),
    ],
}


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def pin(path: Path, data: bytes) -> dict:
    return {"path": str(path), "bytes": len(data), "sha256": sha(data)}


def tex_find(pattern: str, text: str) -> list[str]:
    uncommented = re.sub(r"(?<!\\)%[^\n]*", "", text)
    return re.findall(pattern, uncommented)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seal", required=True, help="Literal root mathematical source-seal record")
    parser.add_argument("--wcf-source", type=Path, help="Publisher's cited derivative of the preserved original WCF input")
    parser.add_argument("--extra-bibliography", type=Path, action="append", default=[], help="Exact supplied human bibliography entries")
    args = parser.parse_args()
    (HERE / "sealed_inputs").mkdir(parents=True, exist_ok=True)
    (HERE / "cumulative").mkdir(parents=True, exist_ok=True)
    (TASK / "build").mkdir(parents=True, exist_ok=True)
    parts = [r"""
\clearpage
\section*{Continuation of 18 September 2026}
\addcontentsline{toc}{section}{Continuation of 18 September 2026}
The following sections give the complete new weighted-conductor,
transport, equilibrium, attained-fibre, covariance and joint-return
calculations. Original coordinates, source orders, masses, conductor
coefficients and endpoint signs are retained throughout. Older equation
names identify their complete proofs in the accompanying cumulative
sources. The programme origin and deposited attribution remain those
documented in \cite{human:globalization2026,human:splitzero2026}; this
continuation was derived and checked with AI assistance within that
programme. Mathematical human-source citations remain attached to their
actual uses.
"""]
    inputs = []
    formatting_derivation = []
    for name, path in FRAGMENTS:
        if name.startswith("01_") and args.wcf_source:
            path = args.wcf_source.resolve()
        data = path.read_bytes()
        content = data.decode("utf-8-sig")
        for before, after, reason in PRESENTATION_REPAIRS.get(name, []):
            count = content.count(before)
            if count == 0 and "\n" in before:
                before = before.replace("\n", "\r\n")
                after = after.replace("\n", "\r\n")
                count = content.count(before)
            if count != 1:
                raise ValueError(f"Expected one presentation repair target in {name}, found {count}: {before}")
            content = content.replace(before, after)
            formatting_derivation.append({"snapshot": name, "before": before, "after": after, "reason": reason, "occurrences": count})
        if r"\begin{document}" in content or r"\end{document}" in content:
            raise ValueError(f"Unexpected document wrapper in {path}")
        if name.startswith("03_"):
            parts.append(r"""
\section{Quantile discrepancy and the original full-polynomial norms}
\label{sec:dual-web-equilibrium}
""")
        parts.append(f"\n% BEGIN SEALED ADDITIVE INPUT {name}\n% SHA256 {sha(data)}\n")
        parts.append(content)
        parts.append(f"\n% END SEALED ADDITIVE INPUT {name}\n")
        (HERE / "sealed_inputs" / name).write_bytes(data)
        inputs.append({**pin(path, data), "snapshot": f"sealed_inputs/{name}", "rendered_fragment_sha256": sha(content.encode("utf-8"))})
    body = "".join(parts).encode("utf-8")
    body_text = body.decode("utf-8")
    labels = tex_find(r"\\label\{([^}]+)\}", body_text)
    duplicates = sorted(k for k, n in collections.Counter(labels).items() if n > 1)
    if duplicates:
        raise ValueError(f"Duplicate labels in additive body: {duplicates}")
    citations = sorted({key.strip() for group in tex_find(r"\\cite(?:\[[^\]]*\])*\{([^}]+)\}", body_text) for key in group.split(",")})
    bib_source = STAGING / BASE_NAMES[-1]
    bib_data = bib_source.read_bytes()
    bib_text = bib_data.decode("utf-8-sig")
    entries = {}
    pattern = r"(\\bibitem(?:\[[^\]]*\])?\{([^}]+)\}[\s\S]*?)(?=\\bibitem|\\end\{thebibliography\})"
    bibliography_sources = [(bib_source, bib_data, bib_text)]
    bibliography_appends = {}
    for extra_path in args.extra_bibliography:
        extra_path = extra_path.resolve()
        extra_data = extra_path.read_bytes()
        extra_text = extra_data.decode("utf-8-sig")
        append_pattern = r"(% BEGIN WCF_BIB_APPEND ([^\r\n]+)\r?\n[\s\S]*?% END WCF_BIB_APPEND \2)"
        for match in re.finditer(append_pattern, extra_text):
            bibliography_appends[match.group(2)] = match.group(1)
        if r"\end{thebibliography}" not in extra_text:
            extra_text += "\n\\end{thebibliography}\n"
        bibliography_sources.append((extra_path, extra_data, extra_text))
    for entry_source, entry_data, entry_text in bibliography_sources:
        for match in re.finditer(pattern, entry_text):
            key = match.group(2)
            if key in entries and entries[key].strip() != match.group(1).strip():
                raise ValueError(f"Different bibliography entries for {key} in {entry_source}")
            entries[key] = match.group(1)
    for key, span in bibliography_appends.items():
        if key not in entries:
            raise ValueError(f"Bibliography append target absent: {key}")
        entries[key] += "\n" + span + "\n"
    if "human:dlmf1" in entries:
        entries["human:dlmf1"] = entries["human:dlmf1"].replace(r"\bibitem{human:dlmf1}", r"\bibitem[H25]{human:dlmf1}")
    missing = sorted(set(citations) - entries.keys())
    if missing:
        raise ValueError(f"Missing bibliography entries: {missing}")
    bibliography = ("\\begin{thebibliography}{H99}\n" + "\n".join(entries[key] for key in citations) + "\\end{thebibliography}\n").encode("utf-8")
    inherited_key_sets = [{match.group(2) for match in re.finditer(pattern, (STAGING / name).read_text(encoding="utf-8-sig"))} for name in BASE_NAMES]
    missing_per_base = [set(citations) - keys for keys in inherited_key_sets]
    if not all(keys == missing_per_base[0] for keys in missing_per_base):
        raise ValueError("Cumulative sources need different additional bibliography entries")
    new_citation_keys = sorted(missing_per_base[0])
    new_bibliography = ("\n\\begin{thebibliography}{H99}\n" + "\n".join(entries[key] for key in new_citation_keys) + "\\end{thebibliography}\n").encode("utf-8") if new_citation_keys else b""
    preamble = r"""\documentclass[11pt,a4paper]{article}
\usepackage{fontspec}
\setmainfont{Latin Modern Roman}
\usepackage[margin=23mm]{geometry}
\usepackage{amsmath,amssymb,amsthm,mathtools,mathrsfs,amscd}
\usepackage{longtable,booktabs}
\usepackage[unicode,hidelinks]{hyperref}
\providecommand{\C}{\mathbb C}
\providecommand{\R}{\mathbb R}
\newtheorem{theorem}{Theorem}[section]
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{corollary}[theorem]{Corollary}
\newtheorem{definition}[theorem]{Definition}
\newtheorem{remark}[theorem]{Remark}
\allowdisplaybreaks
\emergencystretch=3em
\hypersetup{pdftitle={Conductor Transport, Attained Profiles and the Covariance Return},pdfauthor={Split-Zero research programme}}
\title{Conductor Transport, Attained Profiles\\and the Covariance Return\\[0.6em]\large Complete additive proof supplement}
\author{Split-Zero research programme}
\date{18 September 2026}
\begin{document}
\maketitle
\noindent
This volume records the full continuation proofs integrated into the
three cumulative source editions of 18 September 2026. It accompanies
the accepted complete proof corpus and preserves its human-source and
programme provenance. It has no newly assigned deposited DOI.
\tableofcontents
""".encode("utf-8")
    supplement = preamble + body + b"\n\\clearpage\n" + bibliography + b"\\end{document}\n"
    (HERE / "DUAL_WEB_FULL_BODY.tex").write_bytes(body)
    (HERE / "DUAL_WEB_REFERENCES.tex").write_bytes(bibliography)
    (HERE / "DUAL_WEB_NEW_REFERENCES.tex").write_bytes(new_bibliography)
    (HERE / "DUAL_WEB_PROOF_SUPPLEMENT.tex").write_bytes(supplement)
    begin = b"\n% BEGIN DUAL WEB CONTINUATION 20260918\n"
    end = b"\n% END DUAL WEB CONTINUATION 20260918\n"
    inserted = begin + body + new_bibliography + end
    cumulative = []
    for name in BASE_NAMES:
        original_path = STAGING / name
        original = original_path.read_bytes()
        marker = b"\\end{document}"
        if original.count(marker) != 1:
            raise ValueError(f"Expected one final document marker in {name}")
        offset = original.index(marker)
        operations = []
        for key, span in bibliography_appends.items():
            key_bytes = key.encode("utf-8")
            entry_pattern = rb"\\bibitem(?:\[[^\]]*\])?\{" + re.escape(key_bytes) + rb"\}[\s\S]*?(?=\\bibitem|\\end\{thebibliography\})"
            matches = list(re.finditer(entry_pattern, original))
            if len(matches) != 1:
                raise ValueError(f"Expected unique inherited entry for {key} in {name}")
            operations.append((matches[0].end(), ("\n" + span + "\n").encode("utf-8"), f"human bibliography locator append: {key}"))
        operations.append((offset, inserted, "complete shared dual-web continuation and new human reference"))
        pieces = []
        byte_cursor = 0
        output_bytes = 0
        insertion_records = []
        for original_offset, payload, purpose in sorted(operations):
            unchanged = original[byte_cursor:original_offset]
            pieces.extend([unchanged, payload])
            output_bytes += len(unchanged)
            insertion_records.append({"original_byte_offset": original_offset, "successor_byte_offset": output_bytes, "bytes": len(payload), "sha256": sha(payload), "purpose": purpose})
            output_bytes += len(payload)
            byte_cursor = original_offset
        pieces.append(original[byte_cursor:])
        derivative = b"".join(pieces)
        recovered = derivative
        for record in reversed(insertion_records):
            start = record["successor_byte_offset"]
            assert sha(recovered[start:start+record["bytes"]]) == record["sha256"]
            recovered = recovered[:start] + recovered[start+record["bytes"]:]
        assert recovered == original
        target = HERE / "cumulative" / name
        target.write_bytes(derivative)
        cumulative.append({
            "predecessor": pin(original_path, original),
            "successor": pin(target, derivative),
            "insertion_byte_offset": offset,
            "insertion_bytes": len(inserted),
            "insertion_sha256": sha(inserted),
            "reversible_insertions": insertion_records,
            "exact_predecessor_byte_recovery": True,
            "identical_full_body_sha256": sha(body),
            "compiled": False,
        })
    manifest = {
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "root_mathematical_seal": args.seal,
        "inputs": inputs,
        "body": pin(HERE / "DUAL_WEB_FULL_BODY.tex", body),
        "supplement": pin(HERE / "DUAL_WEB_PROOF_SUPPLEMENT.tex", supplement),
        "bibliography_source": pin(bib_source, bib_data),
        "additional_bibliography_sources": [pin(path, data) for path, data, text in bibliography_sources[1:]],
        "citation_keys": citations,
        "inherited_human_entries_preserved_with_exact_locator_insertions": True,
        "new_human_entry_display_label": {"human:dlmf1": "H25"} if "human:dlmf1" in entries else {},
        "new_cumulative_bibliography_keys": new_citation_keys,
        "bibliography": pin(HERE / "DUAL_WEB_REFERENCES.tex", bibliography),
        "cumulative": cumulative,
        "frozen_predecessors_changed": False,
        "compilation_performed": False,
        "formatting_derivation": formatting_derivation,
        "presentation_changes": ["Added title, provenance paragraph, contents and section heading for the two subsection-only analytic fragments; sealed input snapshots remain byte-exact. Only explicitly recorded formatting repairs modify their rendered derivatives.", "Assigned H25 display label to new human:dlmf1 entry; preserved its key and complete entry text.", "Added exact cited-WCF bibliography locator spans inside inherited human:dlmf18 and human:dlmf5 entries, with reversible insertion provenance."],
    }
    (HERE / "INSERTION_MANIFEST.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"body_sha256": sha(body), "supplement_bytes": len(supplement), "citation_keys": citations, "successor_sources": len(cumulative)}))


if __name__ == "__main__":
    main()
