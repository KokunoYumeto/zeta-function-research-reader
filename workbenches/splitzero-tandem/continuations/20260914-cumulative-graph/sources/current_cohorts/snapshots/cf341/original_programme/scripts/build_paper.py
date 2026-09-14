"""Build the standalone reader from owned TeX and hash-verified source notes."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / "build"
PDF = ROOT / "Split_Zero_Cohomology_and_Arithmetic_Weight_Control.pdf"
REQUIRED = (
    "split_zero_carriers.tex", "historical_packet_ghost.tex", "historical_hurwitz_jets.tex",
    "historical_support_branches.tex",
    "support_diagrams.tex",
    "arithmetic_input.tex", "arithmetic_moments.tex", "tau_chain.tex",
    "tau_boundary.tex", "kernel_resolvent.tex", "kernel_convergence.tex",
    "kernel_terminal_continuation.tex",
    "metric_departure.tex", "coherent_tensor_integration.tex", "joint_density_dissipation.tex",
    "kernel_layer_continuation.tex", "kernel_layer_projective_comparison.tex",
    "frontier_energy_dissipation.tex", "symmetric_spectral_cost.tex", "arithmetic_frontier_parity.tex",
    "quartet_dissipation_continuation.tex",
    "theta_stieltjes_pair.tex",
    "theta_gamma_reference.tex",
    "spectral_sum_stieltjes_pair.tex",
    "sum_connection_stieltjes.tex", "conormal_finite_weyl.tex",
    "nested_relative_frame_transition.tex","nested_relative_frame_density.tex","nested_normal_observation.tex","cyclic_sum_conormal.tex", "cyclic_sum_metric_connection.tex",
    "exterior_trace_equality_continuation.tex", "cyclic_control_determinant_increments.tex", "toda_cv_exact_bridge.tex", "toda_theta_input_tail.tex", "toda_exterior_equality_calibration.tex", "gamma_exact_coefficient_join.tex", "gamma_seed_intervals.tex", "gamma_seed_source_costs.tex", "gamma_finite_metric_transfer.tex", "gamma_phase_fibre_transport.tex", "gamma_endpoint_window_bridge.tex", "endpoint_arithmetic_intake.tex", "arithmetic_endpoint_leading_line_transport.tex", "endpoint_product_sharpening.tex", "endpoint_four_volume_threshold.tex", "endpoint_balanced_window.tex", "endpoint_pr24_current_corrected.tex", "arithmetic_volume_upper_route.tex", "endpoint_reflected_relation_fibre_product.tex", "au_weight_optimizer.tex", "relation_moment_comparison_proof.tex", "consecutive_first_window_join.tex", "endpoint_restriction_join.tex", "deligne_split_sidebar.tex", "deligne_exponential_determinant_extension.tex", "deligne_translation_bridge.tex", "deligne_primary_source_correction.tex", "sga_constituent_period_curvature.tex", "cumulative_sga_public_correction_wrapper.tex", "connes_pr27_intake.tex", "period_critical_kernel_bridge.tex", "period_laplacian_control_bridge.tex", "periodized_source_reader_scope.tex", "endpoint_periodized_original.tex", "periodized_source_intake_proofs.tex", "periodized_source_density_review.tex", "periodized_curvature_control_bridge.tex", "circle_critical_observation_diamond.tex", "residue_constituent_public_intake_wrapper.tex", "endpoint_residue_original.tex", "residue_constituent_extension.tex", "jet_topology.tex", "research_conclusion.tex",
)
SOURCES = [
    (8, "tau-base-cohomology/FINITE_OPERATOR_COMPARISON.md", "Finite operator comparison"),
    (9, "tau-chain-descent/RESEARCH_NOTE.md", "Chain descent"),
    (10, "tau-global-retraction/RESEARCH_NOTE.md", "Global retraction"),
    (11, "tau-homotopy-control/RESEARCH_NOTE.md", "Homotopy control"),
    (13, "tau-orthogonal-boundary-control/RESEARCH_NOTE.md", "Orthogonal boundary control"),
    (17, "tau-spectral-sum/RESEARCH_NOTE.md", "Spectral-sum descent and the complete relative arithmetic fibre"),
    (None, "formal/splitzero/DERIVED_MATHEMATICS.md", "Derived Split-Zero mathematics"),
]
MAIN_REVISION = "14c69d604044b848d64318751a7bee19edfd9aba"
TEX_SOURCES = [{
    "pr": 14,
    "stage": "web_pr14_delivery",
    "archive_entry": "Tau_Coherent_Interpolation_Control/NOTE.tex",
    "title": "Coherent arithmetic interpolation and joint tensor boundary control",
    "revision": "3bff1b2bd87dfa2592f65c5ccc231f6ee9541dfc",
    "source_sha256": "01a4fa76072ca4f3d8266c9fdbf61c816e53d09c673f8b8776b981b736c09e26",
}, {
    "pr": None,
    "key": "kernel_layer",
    "stage": "web_kernel_layer_delivery",
    "archive_entry": "Tau_Kernel_Layer_Integration/NOTE.tex",
    "title": "Full-jet interpolation kernels and the actual next relation layer",
    "revision": "3bff1b2bd87dfa2592f65c5ccc231f6ee9541dfc",
    "revision_role": "Arithmetic source baseline PR 14",
    "source_sha256": "be8485471fc7dac41d97e4a9fd52413da14e83fbc42c6c55c01a5f0908caa06c",
    "revision_receipt_name": "HANDOFF.md",
    "receipt_format": "text",
    "receipt_expected_strings": [
        "3bff1b2bd87dfa2592f65c5ccc231f6ee9541dfc",
        "21970bbf4760d0bbca512a4a7996a2e38f968947",
    ],
    "additional_revisions": [{
        "role": "Cited existing PR 15 formal baseline",
        "revision": "21970bbf4760d0bbca512a4a7996a2e38f968947",
    }],
    "related_receipts": [{
        "name": "PATCH_RECEIPT.json",
        "expected_fields": {"remote_branch_modified": False,
                            "checked_against_live_repository_checkout": False,
                            "modified_existing_files": 0, "deleted_files": 0},
    }],
    "attribution": (
        "Complete TeX witness from the dated kernel-layer supplement, delivered "
        "12 September 2026. Its handoff identifies PR 14 as the arithmetic source "
        "and the existing PR 15 revision as its formal baseline. The supplement's "
        "add-only patch was verified locally; its receipt records no remote branch "
        "modification. These NOTE bytes are identified by the source and archive "
        "hashes below; neither baseline revision is represented as their Git head."
    ),
}, {
    "pr": None,
    "key": "symmetric_frontier",
    "stage": "web_symmetric_frontier_delivery",
    "archive_entry": "Tau_Symmetric_Frontier_Control/NOTE.tex",
    "title": "Arithmetic frontier estimates and symmetric tensor control",
    "revision": "3bff1b2bd87dfa2592f65c5ccc231f6ee9541dfc",
    "revision_role": "Recorded add-only patch base, PR 14",
    "source_sha256": "734b6c935892ebd9d18b506f6b592f1ca3489afcb95d5c669a489f4ca04656cf",
    "delivery_expected_fields": {
        "base_commit": "3bff1b2bd87dfa2592f65c5ccc231f6ee9541dfc",
        "remote_write": False, "modified_files": [], "deleted_files": [],
        "local_apply_check_passed": True, "byte_comparison_passed": True,
    },
    "attribution": (
        "Complete TeX witness from the dated symmetric-frontier continuation, "
        "delivered 12 September 2026. Its delivery receipt records an add-only "
        "local patch based on PR 14, with no remote write. The exact revision "
        "below is that patch base; it is not a new remote head for this NOTE. "
        "The source and archive hashes identify the complete delivered witness."
    ),
}, {
    "pr": None,
    "key": "spectral_sum_full",
    "stage": "web_sum_connection_delivery",
    "archive_entry": "Tau_Sum_Connection_Control/sources/Tau_Spectral_Sum_Descent/NOTE.tex",
    "title": "Complete spectral-sum descent: relative arithmetic fibres, dual resolution and all nilpotents",
    "revision": "33b29f706008124886614ba4bd55bffc489df9e2",
    "revision_role": "Associated public PR 17 note revision; full delivered TeX identified by its separate hash",
    "source_sha256": "a3becf8455ddf96e8e382762acbc0e9d0548ea7342c01d70aecdad744ae79552",
    "revision_receipt_name": "HANDOFF.md",
    "receipt_format": "text",
    "receipt_expected_strings": [
        "# Bounded formalization handoff",
        "Free sum-action resolution.",
        "The new script has 24 tests",
    ],
    "attribution": (
        "Complete spectral-sum TeX witness retained inside the sum-connection "
        "delivery archive. The earlier public PR 17 Markdown note is separately "
        "preserved in this reader. This longer witness includes the original "
        "sum-action resolution, linear dual and antidual comparison, Ext and "
        "resolvent calculations, full matrix weight and constrained minimum. "
        "The associated public revision below is not a Git identity assigned "
        "to these longer TeX bytes; the source and archive hashes identify them."
    ),
}, {
    "pr": 20,
    "key": "sum_connection",
    "stage": "web_sum_connection_delivery",
    "archive_entry": "Tau_Sum_Connection_Control/NOTE.tex",
    "title": "Arithmetic sum density, the full relative connection and conormal derivatives",
    "revision": "2144c358c2b41aa235b15cf0fa472289aec8673f",
    "revision_role": "Verified public PR 20 head; the complete delivered witness has the separate hash below",
    "source_sha256": "11870208e3a08df186e42629ae1a6c956faaf28f79dfce0dc2f2d44dc64b4687",
    "delivery_expected_fields": {
        "pull_request": 20,
        "head_commit": "2144c358c2b41aa235b15cf0fa472289aec8673f",
        "base_commit": "33b29f706008124886614ba4bd55bffc489df9e2",
        "changed_files": 5, "existing_files_modified": 0,
    },
    "attribution": (
        "Complete TeX proof witness delivered in the sum-connection archive on "
        "12 September 2026. The verified PR 20 head contains its shorter public "
        "note and checker. This full NOTE is identified by its own source and "
        "archive hashes, and is not assigned the public note's Git blob. "
        "The local conormal continuation proves the input-constant to socle map "
        "with its full multiplicities. The local connection continuation supplies "
        "the exact projected derivative pair for the graph map. The reproduced "
        "source witness is preserved with its original statements."
    ),
}]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def tex_escape(value: str) -> str:
    table = {"&": r"\&", "%": r"\%", "$": r"\$", "#": r"\#",
             "_": r"\_", "{": r"\{", "}": r"\}"}
    return "".join(table.get(c, c) for c in value)


def run(cmd: list[str], receipt: Path) -> str:
    result = subprocess.run(cmd, cwd=ROOT, stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT, text=True, encoding="utf-8",
                            errors="replace")
    receipt.write_text(result.stdout, encoding="utf-8")
    if result.returncode:
        raise RuntimeError(f"Command failed ({result.returncode}); see {receipt}")
    return result.stdout


def protect_ascii_math(text: str) -> tuple[str, int]:
    """Keep source prose adjoint stars literal instead of Markdown emphasis."""
    lines = text.splitlines(keepends=True)
    fenced = False
    displayed = False
    changes = 0
    output = []
    for line in lines:
        if line.lstrip().startswith(("~~~", chr(96) * 3)):
            fenced = not fenced
            output.append(line)
            continue
        if line.count("$$") % 2:
            displayed = not displayed
            output.append(line)
            continue
        if (not fenced and not displayed and not line.startswith("    ")
                and "$" not in line and r"\(" not in line and chr(96) not in line):
            # In R*B, b_m*], and R_m*f, the star is the source's
            # mathematical adjoint/multiplication punctuation, not emphasis.
            line, n = re.subn(r"(?<=[A-Za-z0-9_)])\*(?=[A-Za-z0-9_(\[\]])", r"\*", line)
            changes += n
        output.append(line)
    return "".join(output), changes


def prepare_tex_source(spec: dict) -> tuple[str, dict]:
    """Keep the complete delivered proof body and audit every math span."""
    stage = ROOT / "sources" / spec["stage"]
    path = stage / spec["archive_entry"]
    provenance_path = stage / "LOCAL_STAGING_PROVENANCE.json"
    provenance = read_json(provenance_path)
    digest = sha256(path)
    entries = provenance.get("files", provenance.get("entries", []))
    def verified_entry(entry_name: str) -> dict:
        matches = [item for item in entries
                   if item.get("archive_entry", item.get("entry")) == entry_name]
        entry_path = stage / entry_name
        if (len(matches) != 1
                or matches[0]["sha256"].lower() != sha256(entry_path)
                or matches[0]["bytes"] != entry_path.stat().st_size):
            raise RuntimeError(f"Archive entry failed its staging hash or byte count: {entry_name}")
        return matches[0]
    matches = [verified_entry(spec["archive_entry"])]
    if (len(matches) != 1 or matches[0]["sha256"].lower() != digest
            or spec["source_sha256"] != digest):
        raise RuntimeError(f"Delivered TeX source hash mismatch: {path}")
    delivery_path = path.parent / spec.get("revision_receipt_name", "GITHUB_DELIVERY.json")
    verified_entry(delivery_path.relative_to(stage).as_posix())
    if spec.get("receipt_format") == "text":
        delivery = {}
        delivery_text = delivery_path.read_text(encoding="utf-8-sig")
        if not all(value in delivery_text for value in spec["receipt_expected_strings"]):
            raise RuntimeError("Source lineage text differs from its pinned revisions")
    else:
        delivery = read_json(delivery_path)
        expected = spec.get("delivery_expected_fields",
                            {"head_sha": spec["revision"], "pull_request": spec["pr"]})
        if any(delivery.get(key) != value for key, value in expected.items()):
            raise RuntimeError("Delivered source revision or publication scope differs from its receipt")
    related_receipts = []
    for item in spec.get("related_receipts", []):
        related_path = path.parent / item["name"]
        verified_entry(related_path.relative_to(stage).as_posix())
        related = read_json(related_path)
        if any(related.get(key) != value for key, value in item["expected_fields"].items()):
            raise RuntimeError("Related receipt scope differs from its pinned fields")
        related_receipts.append({"path": related_path.relative_to(ROOT).as_posix(),
                                 "sha256": sha256(related_path),
                                 "verified_fields": item["expected_fields"]})
    archive = Path(provenance.get("archive", provenance.get("source_archive", provenance.get("archive_name"))))
    if not archive.is_absolute():
        archive = stage / archive
    archive_verified = False
    if archive.is_file():
        if sha256(archive) != provenance["archive_sha256"]:
            raise RuntimeError("Original delivered archive hash mismatch")
        with zipfile.ZipFile(archive) as zipped:
            if zipped.read(spec["archive_entry"]) != path.read_bytes():
                raise RuntimeError("TeX witness differs from its original archive entry")
        archive_verified = True
    source = path.read_text(encoding="utf-8-sig")
    if source.count(r"\begin{document}") != 1 or source.count(r"\end{document}") != 1:
        raise RuntimeError("Delivered TeX witness must have exactly one document body")
    preamble, remainder = source.split(r"\begin{document}", 1)
    original_body, trailing = remainder.split(r"\end{document}", 1)
    if trailing.strip():
        raise RuntimeError("Unexpected source content after the document body")
    # The inspected source preamble contains only engine/style/font commands
    # and the tightlist fallback already supplied in main.tex.
    if re.search(r"\\(?:newcommand|renewcommand|DeclareMathOperator|newtheorem)\b", preamble):
        raise RuntimeError("New source preamble definitions require explicit integration")
    body = original_body.replace(r"\maketitle", "", 1)
    body = re.sub(r"\\(section|subsection)(?=\*?[\[{])",
                  lambda m: "\\" + {"section": "subsection", "subsection": "subsubsection"}[m.group(1)],
                  body)
    key = spec.get("key", f"pr_{spec['pr']}")
    removed_presentation = []
    if key in ("exterior_trace", "toda_volume"):
        local_toc = "{\n\\setcounter{tocdepth}{3}\n\\tableofcontents\n}"
        if body.count(local_toc) != 1:
            raise RuntimeError("Expected one exact source-local presentation TOC for " + key)
        body = body.replace(local_toc, "", 1)
        removed_presentation.append("Source-local tableofcontents wrapper omitted; full original witness retained and cumulative contents supply navigation.")
    for label in re.findall(r"\\label\{([^}]+)\}", body):
        body = body.replace(r"\label{" + label + "}", r"\label{" + key + ":" + label + "}")
        body = body.replace(r"\ref{" + label + "}", r"\ref{" + key + ":" + label + "}")
        body = body.replace(r"\hyperref[" + label + "]", r"\hyperref[" + key + ":" + label + "]")
    body = re.sub(
        r"\\texttt\{((?:\\.|[^{}])*)\}",
        lambda m: m.group(0) if r"\{" in m.group(1) or r"\}" in m.group(1)
        else r"\nolinkurl{" + re.sub(r"\\([_#%&$])", r"\1", m.group(1)) + "}",
        body,
    )
    # Two newly delivered displays exceed the common reader measure.
    # Change only the surrounding font size; every math span remains exact.
    layout_wrappers = []
    if key in ("spectral_sum_full", "sum_connection"):
        prefix = (r"\[V=\{" if key == "spectral_sum_full" else r"\[\mu_1\approx")
        size = r"\footnotesize" if key == "spectral_sum_full" else r"\small"
        matches = [m for m in re.finditer(r"\\\[.*?\\\]", body, re.S)
                   if m.group(0).startswith(prefix)]
        if len(matches) != 1:
            raise RuntimeError("Expected one original wide source display for " + key)
        display = matches[0].group(0)
        body = body.replace(display, r"\begingroup" + size + "\n" + display
                            + "\n" + r"\endgroup", 1)
        layout_wrappers.append({"display_prefix": prefix, "font": size,
                                "mathematical_bytes_changed": False})
    math_pattern = r"\\\[(.*?)\\\]|\\\((.*?)\\\)"
    before_math = re.findall(math_pattern, original_body, flags=re.S)
    after_math = re.findall(math_pattern, body, flags=re.S)
    if before_math != after_math:
        raise RuntimeError("Delivered TeX math spans changed during body extraction")
    converted = BUILD / f"source_{key}.tex"
    converted.write_text(body, encoding="utf-8")
    title = f"PR {spec['pr']}: {spec['title']}" if spec["pr"] else spec["title"]
    attribution = spec.get("attribution") or (
        "Complete TeX witness delivered with "
        r"\href{https://github.com/KokunoYumeto/zeta-function-research-reader/pull/"
        + str(spec["pr"]) + r"}{web pull request \#" + str(spec["pr"])
        + "}; the associated Git revision is recorded in its delivery receipt."
    )
    appendix = (
        r"\SourceChronology{" + tex_escape(title) + "}{" + attribution + "}{"
        + spec["revision"] + "}{" + spec["archive_entry"] + "}\n"
        + (r"\noindent\textbf{Revision scope.} " + tex_escape(spec["revision_role"])
           + r"\par" + "\n" if spec.get("revision_role") else "")
        + "".join(r"\noindent\textbf{" + tex_escape(item["role"]) + r".} \nolinkurl{"
                  + item["revision"] + r"}\par" + "\n"
                  for item in spec.get("additional_revisions", []))
        + r"\noindent\textbf{Source SHA-256.} \nolinkurl{" + digest + "}\n"
        + r"\par\noindent\textbf{Original archive.} \nolinkurl{" + archive.name + "}\n"
        + r"\par\noindent\textbf{Archive SHA-256.} \nolinkurl{" + provenance["archive_sha256"] + "}\n"
        + r"\par\medskip\input{" + converted.relative_to(ROOT).as_posix() + "}\n"
    )
    row = {
        "pr": spec["pr"], "title": spec["title"], "revision": spec["revision"],
        "source": path.relative_to(ROOT).as_posix(), "sha256": digest,
        "source_format": "complete delivered TeX witness",
        "layout_wrappers": layout_wrappers,
        "staging_manifest_verified": True,
        "staging_provenance": provenance_path.relative_to(ROOT).as_posix(),
        "staging_provenance_sha256": sha256(provenance_path),
        "archive": str(archive), "archive_sha256": provenance["archive_sha256"],
        "archive_entry": spec["archive_entry"], "archive_entry_verified_now": archive_verified,
        "revision_receipt": delivery_path.relative_to(ROOT).as_posix(),
        "revision_receipt_sha256": sha256(delivery_path),
        "declared_published_markdown_blob": delivery.get("published_note_blob"),
        "revision_role": spec.get("revision_role", "Associated published PR revision"),
        "additional_revisions": spec.get("additional_revisions", []),
        "related_receipts": related_receipts,
        "source_lines": len(source.splitlines()), "complete_body_lines": len(original_body.splitlines()),
        "complete_body_sha256": hashlib.sha256(original_body.encode("utf-8")).hexdigest(),
        "presentation_changes": removed_presentation,
        "display_math_spans": sum(bool(a) for a, b in before_math),
        "inline_math_spans": sum(bool(b) for a, b in before_math),
        "all_math_spans_preserved_exactly": True,
        "math_tags": re.findall(r"\\tag\{([^}]+)\}", original_body),
        "preamble_handling": "Engine and style preamble omitted; no custom mathematical definitions present.",
        "title_handling": "maketitle omitted; the original body title retained as a subsection.",
        "converted": converted.relative_to(ROOT).as_posix(),
    }
    return appendix, row


from cyclic_source_appendix_adapter import (TEX_SPEC, EXTERIOR_TEX_SPEC,
    PASTED_SPEC, PR21_MARKDOWN_SPEC, prepare_pasted_witness)
TEX_SOURCES.extend([TEX_SPEC, EXTERIOR_TEX_SPEC])
from toda_source_appendix_adapter import TODA_TEX_SPEC, PARENT_JOIN_SPEC
TEX_SOURCES.append(TODA_TEX_SPEC)
from gamma_source_appendix_adapter import GAMMA_MARKDOWN_SPEC


def make_appendices() -> list[dict]:
    from endpoint_reader_source_dispatch import prepare_endpoint_sources
    return prepare_endpoint_sources(sys.modules[__name__])


def warning_scan(log: str) -> dict:
    return {
        "latex_warnings": re.findall(r"^.*(?:LaTeX|Package .*?) Warning:.*$", log, re.M),
        "font_warnings": re.findall(r"^.*Font Warning:.*$", log, re.M),
        "missing_characters": re.findall(r"^Missing character:.*$", log, re.M),
        "overfull_boxes": re.findall(r"^Overfull .*?(?=\n\n|\Z)", log, re.M | re.S),
        "underfull_count": len(re.findall(r"^Underfull ", log, re.M)),
        "undefined_controls": re.findall(r"^.*Undefined control sequence.*$", log, re.M),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prepare-only", action="store_true",
                        help="Convert source appendices without compiling unfinished fragments.")
    args = parser.parse_args()
    BUILD.mkdir(parents=True, exist_ok=True)
    sources = make_appendices()
    if args.prepare_only:
        print(json.dumps({"prepared_source_notes": len(sources), "compiled": False}))
        return
    missing = [name for name in REQUIRED if not (ROOT / "tex" / name).is_file()]
    if missing:
        raise RuntimeError(f"Mathematics fragments not yet complete: {missing}")
    xelatex = shutil.which("xelatex")
    if not xelatex:
        raise RuntimeError("xelatex not found")
    inputs = [ROOT / "tex" / "main.tex"] + [ROOT / "tex" / name for name in REQUIRED]
    inputs.append(ROOT / "build/source_appendices.tex")
    for source in sources:
        for field in ("converted", "wrapper"):
            if source.get(field):
                inputs.append(ROOT / source[field])
    inputs = list(dict.fromkeys(inputs))
    input_hashes_before = {p.relative_to(ROOT).as_posix(): sha256(p) for p in inputs}
    for pass_number in range(1, 4):
        run([xelatex, "-interaction=nonstopmode", "-halt-on-error", "-file-line-error",
             "-output-directory=build", "-jobname=reader", "tex/main.tex"],
            BUILD / f"xelatex-pass-{pass_number}.txt")
    log = (BUILD / "reader.log").read_text(encoding="utf-8", errors="replace")
    warnings = warning_scan(log)
    fatal = warnings["undefined_controls"] or warnings["missing_characters"]
    if fatal:
        (BUILD / "build_receipt.json").write_text(
            json.dumps({"status": "needs-typesetting-repair", "warnings": warnings}, indent=2),
            encoding="utf-8")
        raise RuntimeError("Unresolved controls or missing glyphs; see build_receipt.json")
    if input_hashes_before != {p.relative_to(ROOT).as_posix(): sha256(p) for p in inputs}:
        raise RuntimeError("A mathematics input changed during compilation; rebuild its final revision")
    import fitz
    generated = BUILD / "reader.pdf"
    with fitz.open(generated) as document:
        pages = len(document)
        page_sizes = sorted({(round(page.rect.width, 3), round(page.rect.height, 3))
                             for page in document})
    shutil.copy2(generated, PDF)
    receipt = {
        "status": "compiled",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "pdf": str(PDF), "pdf_sha256": sha256(PDF), "pdf_bytes": PDF.stat().st_size, "pages": pages,
        "page_sizes_points": page_sizes, "source_notes": sources,
        "tex_inputs": {p.relative_to(ROOT).as_posix(): sha256(p) for p in inputs},
        "warnings": warnings,
        "visual_review": "not yet performed by this build script",
        "engine": run([xelatex, "--version"], BUILD / "xelatex-version.txt").splitlines()[0],
    }
    (BUILD / "build_receipt.json").write_text(json.dumps(receipt, indent=2), encoding="utf-8")
    print(json.dumps({"pdf": str(PDF), "pages": pages,
                      "warnings": {key: len(val) if isinstance(val, list) else val
                                   for key, val in warnings.items()}}))


if __name__ == "__main__":
    main()
