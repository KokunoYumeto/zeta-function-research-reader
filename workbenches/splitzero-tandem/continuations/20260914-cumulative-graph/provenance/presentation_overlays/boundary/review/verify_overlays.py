"""Independent, read-only source audit; write only this review's receipt.

This does not use the proposal author's content_tokens function or trust its
boolean claims. Byte comparisons prove the entire-source forward/inverse map.
Lexical edit checking limits display changes to an explicit presentation grammar.
"""
from pathlib import Path
import difflib
import hashlib
import json
import re

BASE = Path(__file__).resolve().parent.parent
REVIEW = BASE / "review"
PROPOSAL = BASE / "OVERLAY_PROPOSALS.json"


def digest(data):
    return hashlib.sha256(data).hexdigest()


def lex(display):
    # Preserve all control sequences, all braces, signs and individual digits.
    # Only literal whitespace between TeX tokens is omitted from this comparison;
    # full bytes are checked separately, and matrix bytes are retained exactly.
    return re.findall(r"\\(?:begin|end)\{[^{}]+\}|\\[A-Za-z@]+|\\[^A-Za-z@]|[^\s]", display)


def matrix_blocks(display):
    return re.findall(r"\\begin\{bmatrix\}.*?\\end\{bmatrix\}", display, re.S)


def content_tokens(display):
    # An entire matrix, with original row/column separators, is an indivisible
    # token. Presentation controls can therefore never erase matrix structure.
    pieces = re.split(r"(\\begin\{bmatrix\}.*?\\end\{bmatrix\})", display, flags=re.S)
    result = []
    for piece in pieces:
        if piece.startswith(r"\begin{bmatrix}"):
            result.append(piece)
        else:
            result.extend(t for t in lex(piece) if t not in {
                r"\begin{aligned}", r"\end{aligned}", "&", r"\\", r"\quad", r"\qquad"
            })
    return result


manual_findings = {
    "SC.u5": "All five equalities retained in order: Pi_s, W_jb, D(u)_bb, beta_b, d_b. The -1, beta_b-1, b+1, n denominators, c/u exponent, pi-i factors and Gamma(beta_b) are identical.",
    "LC.u1": "All four derivatives, the two leading minus signs, Pi inverse-adjoint and inverse factors, factor order, commutator brackets, u/bar-u subscripts and t subscripts are identical.",
    "DC32": "Gram expression, kernel equality and both derivatives retained in order. Both derivative minus signs, factor order, inverse-adjoints, nu subscripts and observation superscripts are identical.",
    "APU9": "Both connection definitions, both Omega definitions and the full boxed scope retained. The two 2-by-2 matrices are byte-identical, including each entry and every row/column separator; the -1/u prefactor and all signs are retained.",
    "untagged": "All six equality signs retained: n=m+1, h(s), y, both consecutive Phi_h expressions, and c. Powers m/n, every rho sign, (-rho)^n, denominators n and the additive c are identical."
}

proposal_bytes = PROPOSAL.read_bytes()
proposal = json.loads(proposal_bytes)
assert len(proposal["records"]) == 5
receipts = []
for record in proposal["records"]:
    before_path = Path(record["before"]["path"])
    after_path = Path(record["after"]["path"])
    before = before_path.read_bytes()
    after = after_path.read_bytes()
    old = record["old_display"].encode("utf-8")
    new = record["new_display"].encode("utf-8")
    for label, data in (("before", before), ("after", after)):
        assert digest(data) == record[label]["sha256"], (label, "hash mismatch")
        assert len(data) == record[label]["bytes"], (label, "size mismatch")
    assert before.count(old) == 1
    assert after.count(new) == 1
    forward = before.replace(old, new, 1)
    inverse = after.replace(new, old, 1)
    assert forward == after
    assert inverse == before
    old_s, new_s = old.decode("utf-8"), new.decode("utf-8")
    before_tokens, after_tokens = lex(old_s), lex(new_s)
    edits = []
    for opcode, i, j, k, l in difflib.SequenceMatcher(None, before_tokens, after_tokens, autojunk=False).get_opcodes():
        if opcode == "equal":
            continue
        removed, added = before_tokens[i:j], after_tokens[k:l]
        # Exhaustive whitelist: no deletion/replacement of mathematical tokens.
        permitted = (
            opcode == "insert" and all(t in {r"\begin{aligned}", r"\end{aligned}", "&"} for t in added)
        ) or (
            opcode == "replace" and removed in ([r"\quad"], [r"\qquad"]) and added == [r"\\"]
        )
        assert permitted, (before_path.name, opcode, removed, added)
        edits.append({"removed": removed, "added": added})
    assert before_tokens.count(r"\begin{aligned}") == 0
    assert after_tokens.count(r"\begin{aligned}") == 1
    assert after_tokens.count(r"\end{aligned}") == 1
    old_matrices, new_matrices = matrix_blocks(old_s), matrix_blocks(new_s)
    assert old_matrices == new_matrices
    tokens_old, tokens_new = content_tokens(old_s), content_tokens(new_s)
    assert tokens_old == tokens_new
    tag_old = re.findall(r"\\tag\{([^{}]+)\}", old_s)
    tag_new = re.findall(r"\\tag\{([^{}]+)\}", new_s)
    assert tag_old == tag_new
    assert tag_old == ([record["display_tag"]] if record["display_tag"] else [])
    assert old_s.count("=") == new_s.count("=")
    receipts.append({
        "file": before_path.name,
        "tag": record["display_tag"],
        "before_sha256": digest(before),
        "after_sha256": digest(after),
        "inverse_sha256": digest(inverse),
        "full_file_exact_forward": True,
        "full_file_exact_inverse": True,
        "outside_display_bytes_identical": True,
        "only_allowed_presentation_edits": True,
        "ordered_content_tokens_identical": True,
        "content_token_sha256": digest(json.dumps(tokens_old, ensure_ascii=False).encode("utf-8")),
        "matrix_count": len(old_matrices),
        "matrix_bytes_and_row_column_separators_identical": True,
        "equality_count": old_s.count("="),
        "tag_identical": True,
        "manual_review": manual_findings[record["display_tag"] or "untagged"],
        "presentation_edits": edits,
    })
result = {
    "status": "PASS",
    "scope": "Five before/after full-source files and their complete proposed displays; mathematical content preservation and exact inverse only.",
    "proposal_sha256": digest(proposal_bytes),
    "review_script_sha256": digest(Path(__file__).read_bytes()),
    "method": "Independent exact byte forward/inverse checks, exhaustive lexical edit whitelist, matrix byte checks, matrix-aware ordered content-token equality, and manual reading of every full display.",
    "records": receipts,
    "all_five_preserve_every_mathematical_token_and_tag": True,
    "all_five_exact_byte_inverses": True,
    "independent_APU9_matrix_box_audit": {
        "status": "PASS",
        "reviewer": "matrix_box_audit",
        "findings": "Both bmatrix blocks identical; each has two column separators and one row separator. Connection definitions and -1/u prefactor unchanged. One outer boxed display retains both definitions and both matrices; tag APU9 remains outside the box. No defects."
    },
    "active_files_read_or_modified": False,
    "pdf_build_or_visual_review_performed": False,
}
output = REVIEW / "PROOF_PRESERVATION_RECEIPT.json"
output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "receipt": str(output), "sha256": digest(output.read_bytes()), "files": len(receipts)}))
