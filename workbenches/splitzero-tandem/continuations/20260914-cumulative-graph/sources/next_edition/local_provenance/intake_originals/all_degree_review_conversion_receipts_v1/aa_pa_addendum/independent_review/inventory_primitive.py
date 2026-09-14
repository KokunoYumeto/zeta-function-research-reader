"""Complete independent delimiter/notation inventory; no mathematics altered."""
from __future__ import annotations
import hashlib
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parents[3] / "output/Tau_All_Degree_Angle_Transport_2026-09-13/evidence/tau_all_degree_angle_primitive_acceptance_20260913.md"
EXPECTED_SHA = "8def95f8c69d3df47a82948882d161ba134b1b37d3abfb482595891eb93a2f56"

def pin(path: Path) -> dict:
    raw = path.read_bytes()
    return {"path": str(path), "bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()}

raw = SOURCE.read_bytes()
text = raw.decode("utf-8")
assert len(raw) == 5785 and hashlib.sha256(raw).hexdigest() == EXPECTED_SHA

# This ordered list was assembled by reading every paragraph and all six
# numbered proof-review items. Duplicate short tokens are separate occurrences.
originals = [
    r"(m=2q-1)",
    r"(q=1)",
    r"(h(D)F_h=\Theta\phi_*)",
    r"(g=2\xi\)",
    r"(H_{\phi_*}=1)",
    r"(\mathcal M\Theta\phi_*=g)",
    r"(h)",
    r"(g/h)",
    r"(s_1+\cdots+s_k)",
    r"(\chi(s_1+\cdots+s_k))",
    r"(h(s_j))",
    r"(h(s_j))",
    r"\(\deg h\)",
    r"(j)",
    r"(j)",
    r"(\phi_*\)",
    r"(j-1)",
    r"(F_h\)",
    r"((-1)^{j-1})",
    r"(D_j)",
    r"(D\Theta=\Theta D)",
    "DISPLAY",
    r"(P(\sum D_j)\chi(\sum D_j)F_h^{\otimes k}\)",
    r"\(\mathcal V_{h,k}(\chi P)\)",
    r"(k=1\)",
    r"\(L_1=1\)",
    r"(h\)",
    r"(P=X_{ij}x\)",
    r"(M(t)\)",
    r"(t=1\)",
    r"\(\mathcal V_{h,k}\)",
    r"\(\Theta\)",
    r"\(\tau\)",
]
rows = []
cursor = 0
for index, requested in enumerate(originals):
    if requested == "DISPLAY":
        match = re.search(r"\\\[(.*?)\\\]", text[cursor:], re.S)
        assert match
        start, end = cursor + match.start(), cursor + match.end()
        before = text[start:end]
        payload = match.group(1)
        after = before
        classification = "existing_display_math"
        mode = "display"
    else:
        start = text.index(requested, cursor)
        end = start + len(requested)
        before = requested
        mode = "inline"
        if before.startswith(r"\("):
            assert before.endswith(r"\)")
            classification = "existing_inline_math"
            payload = before[2:-2]
            after = before
        elif before.endswith(r"\)"):
            assert before.startswith("(")
            classification = "malformed_plain_open_tex_close"
            payload = before[1:-2]
            after = r"\(" + payload + r"\)"
        else:
            assert before.startswith("(") and before.endswith(")")
            classification = "plain_parenthesized_math"
            payload = before[1:-1]
            after = r"\(" + payload + r"\)"
    byte_start = len(text[:start].encode("utf-8"))
    byte_end = len(text[:end].encode("utf-8"))
    assert raw[byte_start:byte_end] == before.encode("utf-8")
    rows.append({"expression_index_one_based": index + 1,
                 "source_line_one_based": text.count("\n", 0, start) + 1,
                 "source_start_byte": byte_start, "source_end_byte": byte_end,
                 "before": before, "after": after,
                 "typed_math_payload": payload, "mode": mode,
                 "classification": classification,
                 "payload_sha256": hashlib.sha256(payload.encode("utf-8")).hexdigest(),
                 "mathematical_payload_unchanged": True,
                 "action": "retain unchanged" if before == after else "repair only outer Math delimiters"})
    cursor = end
assert len(rows) == 33
edits = [row.copy() for row in rows if row["before"] != row["after"]]
counts = {category: sum(row["classification"] == category for row in rows)
          for category in ("plain_parenthesized_math", "malformed_plain_open_tex_close", "existing_inline_math", "existing_display_math")}
assert counts == {"plain_parenthesized_math": 17, "malformed_plain_open_tex_close": 9,
                  "existing_inline_math": 6, "existing_display_math": 1}
assert len(edits) == 26

codes = []
for match in re.finditer(r"`([^`\n]+)`", text):
    payload = match.group(1)
    codes.append({"source_start_byte": len(text[:match.start()].encode("utf-8")),
                  "source_end_byte": len(text[:match.end()].encode("utf-8")),
                  "before": match.group(), "payload": payload,
                  "classification": "sha256_literal" if re.fullmatch(r"[a-f0-9]{64}", payload) else "source_relative_locator_literal",
                  "action": "retain exact Code payload unchanged"})
assert len(codes) == 6
protected = [(row["source_start_byte"], row["source_end_byte"]) for row in rows + codes]
# Every TeX control/delimiter, power marker, or subscript marker in the complete
# source lies in an explicitly inspected expression or a retained source Code.
for match in re.finditer(rb"\\[A-Za-z]+|\\[()\[\]]|[_^]", raw):
    assert any(a <= match.start() and match.end() <= b for a, b in protected), match.group()
math_tokens_covered = True
references = [{"source_start_byte": len(text[:match.start()].encode("utf-8")),
               "source_end_byte": len(text[:match.end()].encode("utf-8")),
               "source_line_one_based": text.count("\n", 0, match.start()) + 1,
               "before": match.group(), "classification": "literal equation/proof reference",
               "action": "retain as prose reference unchanged"}
              for match in re.finditer(r"\b(?:AA|PA)\d+(?:[–-](?:AA|PA)?\d+)?", text)]
assert not re.search(r"\b[A-Za-z]:[\\/]|/(?:Users|home)/", text)

pieces = []
cursor = 0
delta = 0
for edit in edits:
    start, end = edit["source_start_byte"], edit["source_end_byte"]
    replacement = edit["after"].encode("utf-8")
    pieces += [raw[cursor:start], replacement]
    edit["public_start_byte"] = start + delta
    edit["public_end_byte"] = start + delta + len(replacement)
    delta += len(replacement) - (end - start)
    cursor = end
pieces.append(raw[cursor:])
typed = b"".join(pieces)
inverse = typed
for edit in reversed(edits):
    a, b = edit["public_start_byte"], edit["public_end_byte"]
    assert inverse[a:b] == edit["after"].encode("utf-8")
    inverse = inverse[:a] + edit["before"].encode("utf-8") + inverse[b:]
assert inverse == raw
public_path = HERE / "PRIMITIVE_TYPED.md"
if public_path.exists():
    assert public_path.read_bytes() == typed
else:
    public_path.write_bytes(typed)
for row in rows:
    if row["action"] == "retain unchanged":
        shift = sum(len(edit["after"].encode()) - len(edit["before"].encode())
                    for edit in edits if edit["source_end_byte"] <= row["source_start_byte"])
        assert typed[row["source_start_byte"] + shift:row["source_end_byte"] + shift] == row["before"].encode()
for row in codes:
    shift = sum(len(edit["after"].encode()) - len(edit["before"].encode())
                for edit in edits if edit["source_end_byte"] <= row["source_start_byte"])
    assert typed[row["source_start_byte"] + shift:row["source_end_byte"] + shift] == row["before"].encode()
typed_text = typed.decode("utf-8")
assert len(re.findall(r"\\\((.*?)\\\)", typed_text, re.S)) == 32
assert len(re.findall(r"\\\[(.*?)\\\]", typed_text, re.S)) == 1

mapping = {"schema": "primitive-complete-delimiter-transcription-map-v1",
           "status": "independent-notation-accepted",
           "scope": "Complete source read and independent notation/delimiter review only. Every mathematical payload is retained exactly; no mathematical proof audit, new research, converter run, or PDF acceptance is claimed.",
           "original_source": pin(SOURCE), "public_source": pin(public_path),
           "source_line_count": len(text.splitlines()),
           "complete_math_expression_count": 33, "notation_edit_count": 26,
           "classification_counts": counts, "math_expressions": rows,
           "edits": edits, "retained_code_count": 6, "retained_code": codes,
           "equation_references": references,
           "all_tex_control_power_and_subscript_tokens_covered": math_tokens_covered,
           "all_original_math_payloads_unchanged": True,
           "all_original_code_payloads_unchanged": True,
           "exact_full_byte_inverse_verified": True,
           "private_absolute_path_or_internal_delegation_findings": [],
           "publication_prose_deletions": [],
           "public_derivative_edit_scope": "Only 17 pairs of plain outer parentheses and 9 malformed outer delimiter pairs are repaired. Every inner parenthesis, sign, factor, operator, subscript, and tensor power remains identical.",
           "original_source_unchanged_after_review": SOURCE.read_bytes() == raw}
assert mapping["original_source_unchanged_after_review"]
mapping_path = HERE / "PRIMITIVE_NOTATION_MAP.json"
mapping_path.write_text(json.dumps(mapping, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="")
report = ["# Independent complete primitive-note notation review", "",
          "All 33 mathematical expressions were inspected. Exactly 26 outer-delimiter repairs are needed: 17 plain-parenthesized expressions and nine mismatched plain-open/TeX-close expressions. The six proper inline expressions and one displayed expression remain byte-exact, as do all six source/hash Code spans.", "",
          f"Original: {len(raw)} bytes; SHA256 `{EXPECTED_SHA}`.",
          f"Typed source: {len(typed)} bytes; SHA256 `{pin(public_path)['sha256']}`.", "",
          "No mathematical payload or proof prose was changed. The complete byte inverse was verified. This is notation acceptance only; it makes no independent mathematical acceptance or PDF claim.", "",
          "## Exact changes", ""]
for edit in edits:
    report += [f"- Bytes {edit['source_start_byte']}–{edit['source_end_byte']} (end exclusive): `{edit['before']}` → `{edit['after']}`."]
(HERE / "PRIMITIVE_NOTATION_REVIEW.md").write_text("\n".join(report) + "\n", encoding="utf-8", newline="")
print(json.dumps({"map": pin(mapping_path), "original": pin(SOURCE), "public": pin(public_path),
                  "review": pin(HERE / "PRIMITIVE_NOTATION_REVIEW.md"), "counts": counts}, ensure_ascii=False))
