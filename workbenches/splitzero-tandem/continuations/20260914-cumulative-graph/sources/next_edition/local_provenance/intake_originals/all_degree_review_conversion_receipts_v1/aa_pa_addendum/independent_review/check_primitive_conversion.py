"""Independent byte, complete-AST and literal checks of the final conversion."""
from __future__ import annotations
import copy
import hashlib
import json
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE.parents[1]
PINNED_FILES = []

def pin(path: Path) -> dict:
    raw = path.read_bytes()
    return {"path": str(path), "bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()}

def read(path: Path):
    PINNED_FILES.append(pin(path))
    return json.loads(path.read_bytes())

def check_pin(row: dict) -> Path:
    path = Path(row["path"])
    actual = pin(path)
    assert actual["bytes"] == row["bytes"] and actual["sha256"] == row["sha256"], path
    PINNED_FILES.append(actual)
    return path

def walk(value):
    if isinstance(value, dict):
        if "t" in value:
            yield value
        for child in value.values():
            yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)

def literals(value):
    return [[node["t"], node["c"]] for node in walk(value)
            if node.get("t") in {"Math", "Code", "CodeBlock", "RawInline", "RawBlock"}]

def math(value):
    return [node["c"] for node in walk(value) if node.get("t") == "Math"]

def codes(value):
    return [node["c"] for node in walk(value) if node.get("t") == "Code"]

def apply_ast_edits(start, edits, reverse=False, path_key="path"):
    result = copy.deepcopy(start)
    for edit in reversed(edits) if reverse else edits:
        parts = edit[path_key]
        holder = result
        for part in parts[:-1]:
            holder = holder[part]
        old, new = (edit["after"], edit["before"]) if reverse else (edit["before"], edit["after"])
        assert holder[parts[-1]] == old, parts
        holder[parts[-1]] = copy.deepcopy(new)
    return result

independent_path = HERE / "PRIMITIVE_NOTATION_MAP.json"
independent = read(independent_path)
assert pin(independent_path)["sha256"] == "dc79f42243f3750cd0bcb102196c35297c0a769b949bf181a654d71ba7e7382a"
map_path = BASE / "aa_pa_addendum/public_provenance/PRIMITIVE_NOTATION_AND_AST_INVERSE.json"
public_map = read(map_path)
assert pin(map_path)["bytes"] == 138565
assert pin(map_path)["sha256"] == "93447b347a6b6533e249b68850b17666d18bc76c8cfed10554853b3fee2bf85c"
receipt_path = BASE / "receipts/angle_primitive_acceptance.json"
receipt = read(receipt_path)
adapter_receipt_path = BASE / receipt["adapter_row"]["conversion_receipt"]
adapter = read(adapter_receipt_path)
assert pin(adapter_receipt_path)["sha256"] == receipt["adapter_row"]["conversion_receipt_sha256"]

source_paths = {key: check_pin(receipt[key]) for key in ("original_source", "raw_snapshot", "public_source", "raw_original_ast", "public_original_ast", "adapter", "wrapper", "independent_complete_typing_inventory")}
raw = source_paths["original_source"].read_bytes()
public = source_paths["public_source"].read_bytes()
assert raw == source_paths["raw_snapshot"].read_bytes()
assert raw == check_pin(independent["original_source"]).read_bytes()
assert public == check_pin(independent["public_source"]).read_bytes()
assert len(raw) == 5785 and len(public) == 5828
assert receipt["adapter"]["sha256"] == adapter["adapter_sha256"] == "1adac7ea485573981ef3a37cbae04ccc2ab52e91058fe5df80f7c531d6a85023"
for value, expected in ((public_map["original_source"], receipt["original_source"]),
                        (public_map["typed_source"], receipt["public_source"])):
    assert value["bytes"] == expected["bytes"] and value["sha256"] == expected["sha256"]

edits = public_map["typing_byte_edits"]
assert len(edits) == 26 == len(independent["edits"])
assert receipt["publication_and_typing_byte_edits"] == edits
for proposed, accepted in zip(edits, independent["edits"]):
    for key, value in accepted.items():
        assert proposed[key] == value, (key, accepted["expression_index_one_based"])
    a, b = proposed["source_start_byte"], proposed["source_end_byte"]
    assert raw[a:b] == proposed["before"].encode("utf-8")
    assert hashlib.sha256(raw[a:b]).hexdigest() == proposed["before_sha256"]
    c, d = proposed["public_start_byte"], proposed["public_end_byte"]
    assert public[c:d] == proposed["after"].encode("utf-8")
    assert hashlib.sha256(public[c:d]).hexdigest() == proposed["after_sha256"]

forward = raw
for edit in reversed(edits):
    a, b = edit["source_start_byte"], edit["source_end_byte"]
    forward = forward[:a] + edit["after"].encode("utf-8") + forward[b:]
assert forward == public
inverse = public
for edit in reversed(edits):
    a, b = edit["public_start_byte"], edit["public_end_byte"]
    inverse = inverse[:a] + edit["before"].encode("utf-8") + inverse[b:]
assert inverse == raw

raw_ast = read(source_paths["raw_original_ast"])
public_ast = read(source_paths["public_original_ast"])
patches = public_map["complete_raw_to_typed_ast_edits"]
assert len(patches) == 8
assert apply_ast_edits(raw_ast, patches) == public_ast
assert apply_ast_edits(public_ast, patches, reverse=True) == raw_ast
assert literals(raw_ast) == public_map["whole_original_literal_sequence"]
assert literals(public_ast) == public_map["whole_typed_literal_sequence"]
assert len(literals(raw_ast)) == 30 and len(literals(public_ast)) == 39

# A fresh read-only parse binds both recorded ASTs to the actual original and
# typed source bytes; this executes no source code, generator or adapter.
pandoc = shutil.which("pandoc")
assert pandoc
parse_checks = []
for key, wanted in (("original_source", raw_ast), ("public_source", public_ast)):
    command = [pandoc, str(source_paths[key]), "-f", adapter["markdown_format"], "-t", "json"]
    run = subprocess.run(command, capture_output=True, check=True)
    parsed = json.loads(run.stdout)
    assert parsed == wanted
    parse_checks.append({"source": pin(source_paths[key]), "parser": pandoc,
                         "format": adapter["markdown_format"], "exit_code": run.returncode,
                         "full_AST_equal": True})

raw_math = math(raw_ast)
public_math = math(public_ast)
assert len(raw_math) == 7 and len(public_math) == 33
assert len(codes(raw_ast)) == 6 and codes(raw_ast) == codes(public_ast)
assert [node[-1] for node in codes(public_ast)] == [row["payload"] for row in independent["retained_code"]]
existing = [row for row in independent["math_expressions"] if row["action"] == "retain unchanged"]
assert len(existing) == len(public_map["every_original_well_delimited_source_span"]) == 7
for row, preserved, old_c in zip(existing, public_map["every_original_well_delimited_source_span"], raw_math):
    assert row["source_start_byte"] == preserved["source_start_byte"]
    assert row["source_end_byte"] == preserved["source_end_byte"]
    assert row["before"] == preserved["complete_original_delimited_span"]
    assert old_c == preserved["complete_original_AST_Math_payload"]
    shift = sum(len(edit["after"].encode()) - len(edit["before"].encode())
                for edit in edits if edit["source_end_byte"] <= row["source_start_byte"])
    assert public[row["source_start_byte"] + shift:row["source_end_byte"] + shift] == row["before"].encode()
expected_math = []
old_index = 0
for row in independent["math_expressions"]:
    if row["action"] == "retain unchanged":
        expected_math.append(raw_math[old_index])
        old_index += 1
    else:
        expected_math.append([{"t": "InlineMath"}, row["typed_math_payload"]])
assert expected_math == public_map["expected_complete_math_sequence_from_original_source_byte_order"] == public_math

adapter_original = read(BASE / adapter["artifacts"]["original_ast"])
prepared = read(BASE / adapter["artifacts"]["prepared_ast"])
writer = read(BASE / adapter["artifacts"]["writer_ast"])
assert adapter_original == public_ast
assert apply_ast_edits(adapter_original, adapter["prepared_edits"], path_key="parts") == prepared
assert apply_ast_edits(prepared, adapter["prepared_edits"], reverse=True, path_key="parts") == adapter_original
assert apply_ast_edits(prepared, adapter["writer_edits"], path_key="parts") == writer
assert apply_ast_edits(writer, adapter["writer_edits"], reverse=True, path_key="parts") == prepared
assert math(adapter_original) == math(prepared) == expected_math
assert codes(adapter_original) == codes(prepared) == codes(writer) == codes(raw_ast)
assert len(adapter["writer_edits"]) == 33 and len(adapter["literal_emission_spans"]) == 33
assert adapter["retained_source_raw_tex_nodes"] == []
generated_path = BASE / adapter["generated_tex"]["path"]
generated = generated_path.read_bytes()
assert len(generated) == adapter["generated_tex"]["bytes"]
assert hashlib.sha256(generated).hexdigest() == adapter["generated_tex"]["sha256"] == receipt["adapter_row"]["converted_sha256"]
PINNED_FILES.append(pin(generated_path))
literal_checks = []
previous_end = 0
for index, (literal, expected) in enumerate(zip(adapter["literal_emission_spans"], expected_math)):
    assert literal["node_type"] == "Math" and literal["original_c"] == expected
    a, b = literal["fragment_start_byte"], literal["fragment_end_byte"]
    c, d = literal["payload_start_byte"], literal["payload_end_byte"]
    assert previous_end <= a <= c <= d <= b
    assert generated[c:d] == literal["payload"].encode("utf-8") == expected[1].encode("utf-8")
    assert hashlib.sha256(generated[c:d]).hexdigest() == literal["payload_sha256"]
    assert generated[a:b] == (literal["opening"] + literal["payload"] + literal["closing"]).encode("utf-8")
    assert hashlib.sha256(generated[a:b]).hexdigest() == literal["fragment_sha256"]
    previous_end = b
    literal_checks.append({"index": index, "original_c": expected,
                           "fragment_start_byte": a, "fragment_end_byte": b,
                           "payload_start_byte": c, "payload_end_byte": d,
                           "fragment_sha256": literal["fragment_sha256"],
                           "payload_sha256": literal["payload_sha256"], "exact_bytes_equal": True})
assert len(adapter["code_layout"]) == 6
code_checks = []
for layout, original_c in zip(adapter["code_layout"], codes(raw_ast)):
    payload = original_c[-1]
    assert layout["original_rendered_text"] == payload
    assert layout["after"] == r"\nolinkurl{" + payload + "}"
    assert generated.count(layout["after"].encode("utf-8")) == 1
    code_checks.append({"original_c": original_c, "generated_tex": layout["after"], "exactly_one_occurrence": True})
for original_pin in PINNED_FILES:
    assert pin(Path(original_pin["path"])) == original_pin

result = {
    "schema": "independent-final-primitive-source-and-AST-readiness-review-v1",
    "created_utc": datetime.now(timezone.utc).isoformat(),
    "status": "PASS",
    "scope": "Bounded independent byte, complete raw/public AST inverse, adapter AST inverse, and exact generated literal check. Fresh Pandoc parses are read-only. No source conversion/generator, mathematical checker, TeX compiler, mathematical re-audit or PDF visual inspection was executed.",
    "public_notation_AST_map": pin(map_path), "local_conversion_receipt": pin(receipt_path),
    "adapter_conversion_receipt": pin(adapter_receipt_path),
    "independent_notation_map": pin(independent_path),
    "original_source": pin(source_paths["original_source"]),
    "typed_source": pin(source_paths["public_source"]),
    "generated_tex": pin(generated_path),
    "byte_edit_count": 26, "byte_forward_and_inverse_exact": True,
    "complete_raw_public_AST_edit_count": 8,
    "complete_raw_public_AST_forward_and_inverse_exact": True,
    "fresh_full_AST_parse_checks": parse_checks,
    "unchanged_existing_math_count": 7, "typed_expression_count": 26,
    "complete_math_count": 33, "inline_math_count": 32, "display_math_count": 1,
    "code_count": 6, "complete_code_c_unchanged_across_raw_public_prepared_writer_ASTs": True,
    "complete_prepared_AST_forward_and_inverse_exact": True,
    "complete_writer_AST_forward_and_inverse_exact": True,
    "literal_checks": literal_checks, "code_checks": code_checks,
    "all_input_pins_unchanged_after_review": True, "input_pins": PINNED_FILES,
    "findings": [], "mathematical_acceptance_certified": False, "PDF_visual_acceptance": False,
}
out = HERE / "PRIMITIVE_FINAL_READINESS_REVIEW.json"
out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="")
report = "\n".join([
    "# Independent final primitive conversion review", "", "Status: **PASS**.", "",
    "The exact 5,785-byte original and 5,828-byte typed source match the independently reviewed pins. All 26 edits equal the independent delimiter map, and the complete byte transformation is invertible in both directions.", "",
    "All eight full raw-to-public AST patches were applied forward and backward and matched the complete recorded trees. Fresh read-only Pandoc parses of both source files agree with those trees. The prepared and writer AST patches were also independently verified in both directions.", "",
    "All seven originally delimited mathematical expressions remain unchanged. All 26 newly delimited payloads agree exactly with the independent transcription inventory, giving 32 inline and one displayed Math node in source order. The existing display's original list indentation remains in the Markdown bytes; its unchanged Pandoc Math payload is checked separately at the AST and generated-byte levels.", "",
    "All 33 generated mathematical payloads and their complete delimited fragments match their exact receipt byte intervals and hashes. All six complete Code payloads are unchanged across the AST stages and appear once each in the generated nolinkurl forms. No protected mathematical payload, sign, grouping, factor, or proof prose was rewritten.", "",
    result["scope"], "",
])
(HERE / "PRIMITIVE_FINAL_READINESS_REVIEW.md").write_text(report, encoding="utf-8", newline="")
print(json.dumps({"status": "PASS", "review": pin(out), "readable_review": pin(HERE / "PRIMITIVE_FINAL_READINESS_REVIEW.md")}, ensure_ascii=False))
