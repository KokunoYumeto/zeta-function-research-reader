"""Complete FS source intake only: no source changes or proof acceptance."""
from __future__ import annotations
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE.parents[2]
SOURCE = BASE.parent / "tau_four_window_spectral_sharpness_20260913.md"
EXPECTED_SHA = "11c26c3bcfce135e1882190af9dc3a8f1e4e6487fd282cc252fa441fdf90651c"

def pin(path: Path) -> dict:
    raw = path.read_bytes()
    return {"path": str(path), "bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()}

raw = SOURCE.read_bytes()
text = raw.decode("utf-8")
assert len(raw) == 18872 and hashlib.sha256(raw).hexdigest() == EXPECTED_SHA
assert len(text.splitlines()) == 440

def location(match: re.Match) -> dict:
    start, end = match.span()
    return {"source_line_one_based": text.count("\n", 0, start) + 1,
            "char_start": start, "char_end_exclusive": end,
            "byte_start": len(text[:start].encode("utf-8")),
            "byte_end_exclusive": len(text[:end].encode("utf-8")),
            "source": match.group(0)}

tags = [{**location(match), "tag": match.group(1)}
        for match in re.finditer(r"\\tag\{([^}]+)\}", text)]
assert [row["tag"] for row in tags] == [f"FS{i}" for i in range(1, 36)]
inline_math = [{**location(match), "payload": match.group(1)}
               for match in re.finditer(r"\\\((.*?)\\\)", text, re.S)]
display_math = [{**location(match), "payload": match.group(1)}
                for match in re.finditer(r"\\\[(.*?)\\\]", text, re.S)]
assert len(inline_math) == text.count(r"\(") == text.count(r"\)") == 188
assert len(display_math) == text.count(r"\[") == text.count(r"\]") == 39
assert "```" not in text and "~~~" not in text
codes = []
for match in re.finditer(r"`([^`\n]+)`", text):
    payload = match.group(1)
    classification = "sha256_literal" if re.fullmatch(r"[a-f0-9]{64}", payload) else "source_relative_path_literal"
    assert classification == "sha256_literal" or payload == "work/tau_arithmetic_determinant_transport_20260913.tex"
    codes.append({**location(match), "code": payload,
                  "classification": classification, "action": "Retain complete literal payload unchanged."})
assert len(codes) == 2 and [row["source_line_one_based"] for row in codes] == [5, 5]
headings = [{**location(match), "level": len(match.group(1)), "title": match.group(2)}
            for match in re.finditer(r"^(#{1,6})\s+(.+)$", text, re.M)]
assert len(headings) == 7
absolute_candidates = [location(match) for match in re.finditer(r"\b[A-Za-z]:[\\/]|/(?:Users|home)/", text)]
assert not absolute_candidates

read_notes = [
    "Title, date, and complete source-consultation paragraph read. The stated 190-line AT consultation is preserved as the original historical scope; this intake does not upgrade that source-reading claim.",
    "Entire original-space, positive-metric, projection, relation-flag, eigenspace, and multiplicity section read, including q=1 and the two complete tables.",
    "Entire separate-spectra trace calculation and its scoped equality fixtures read, including the empty sum at q=1 and original difference spectrum.",
    "All literal polynomial incidence, simple-spectrum obstruction, every rank case, compactness argument, ordered spectral gaps, and nonscalar strictness paragraphs read.",
    "Entire explicit polynomial basis, isomorphism and inverse, arbitrary positive mass, complete coefficient norm and Gram blocks, and transformed relation projections read.",
    "Entire fixed-spectrum endomorphism, original-coordinate formula, exact trace, sharp supremum, q=1 specialization, difference spectrum, and positive metric paths read.",
    "Entire original moment integral, vertical-line identity, explicit failure of its moment constraints in both q cases, and final scope paragraph read.",
]
sections = []
for index, (heading, note) in enumerate(zip(headings, read_notes)):
    next_line = headings[index + 1]["source_line_one_based"] if index + 1 < len(headings) else 441
    sections.append({"first_line_one_based": heading["source_line_one_based"],
                     "last_line_one_based": next_line - 1,
                     "heading": heading["title"], "classification": "retain complete", "read_scope": note})
assert [line for row in sections for line in range(row["first_line_one_based"], row["last_line_one_based"] + 1)] == list(range(1, 441))

receipt = {
    "schema": "complete-fs-proof-preparation-intake-v1",
    "created_utc": datetime.now(timezone.utc).isoformat(),
    "status": "source-prepared-awaiting-owner-mathematical-review-record",
    "scope": "All 440 original lines read for complete source preparation, classification, and exact notation inventory. Mathematical correctness and final mathematical acceptance are not certified by this intake. No source changes, mathematical re-audit, fixture execution, adapter conversion, or rendered-page inspection were performed.",
    "source": pin(SOURCE), "source_line_count": 440,
    "headings": headings, "complete_line_coverage": sections,
    "tag_count": len(tags), "tags": tags,
    "inline_math_count": len(inline_math), "inline_math": inline_math,
    "display_math_count": len(display_math), "display_math": display_math,
    "total_math_span_count": len(inline_math) + len(display_math),
    "inline_code_count": len(codes), "inline_code": codes,
    "code_classification_counts": {"source_relative_path_literal": 1, "sha256_literal": 1, "mathematical_expression": 0},
    "fenced_code_block_count": 0, "mathematical_ascii_mapping_needed": False,
    "mathematical_code_transcriptions_needed": [],
    "automated_drive_and_user_home_absolute_path_candidates": absolute_candidates,
    "complete_read_private_absolute_path_or_unc_findings": [],
    "private_or_operative_internal_coordination_findings": [],
    "public_derivative_required": False, "proposed_source_transformations": [],
    "classification": "Complete public mathematical calculation, already using inline/display LaTeX, with relative source provenance retained. No publication deletion or notation transcription is proposed.",
    "publication_context_notes": [
        {"source_line_one_based": 5, "classification": "Retain the original relative source path, its hash, the 190-line consultation statement, and the historical no-edit/no-Lean scope."},
        {"classification": "The phrase 'requested simple-spectrum obstruction' occurs inside the mathematical argument and contains no operative delegation instruction; retain its complete paragraph."},
        {"classification": "References to normalization inside an explicitly specified metric concern the original mathematical coordinate calculation; this intake preserves them verbatim and does not reinterpret or change the mathematics."},
    ],
    "mathematical_acceptance_certified": False,
    "source_unchanged_after_intake": SOURCE.read_bytes() == raw,
}
assert receipt["source_unchanged_after_intake"]
(HERE / "SOURCE_INTAKE.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="")
report = "\n".join([
    "# Complete FS1–FS35 source preparation", "",
    "The complete original has been read and inventoried. No source transformation is proposed. Final mathematical acceptance remains with the separate owner review.", "",
    f"Source: `{SOURCE}`", "",
    f"Bytes: 18872. SHA256: `{EXPECTED_SHA}`.", "",
    "- All 440 lines were read, covering the complete strictness proof, positive-metric family, exact trace/spectrum, and original moment-Gram comparison.",
    "- All 35 tags FS1–FS35 occur once in order.",
    "- There are 188 inline and 39 displayed LaTeX spans, totaling 227. Their complete payloads and exact source positions are recorded in SOURCE_INTAKE.json.",
    "- The only two Code spans are the relative AT source path and its SHA256. No mathematical ASCII/Code mapping or fenced code block is present.",
    "- No private absolute path, private transcript body, or operative internal delegation instruction was found. Preserve all original source-reading and scope statements.",
    "- The original remains byte-for-byte unchanged. No mathematical re-audit or final mathematical acceptance is claimed.", "",
    receipt["scope"], "",
])
(HERE / "SOURCE_INTAKE.md").write_text(report, encoding="utf-8", newline="")
print(json.dumps({"status": receipt["status"], "source": receipt["source"],
                  "receipt": pin(HERE / "SOURCE_INTAKE.json"),
                  "report": pin(HERE / "SOURCE_INTAKE.md")}, ensure_ascii=False))
