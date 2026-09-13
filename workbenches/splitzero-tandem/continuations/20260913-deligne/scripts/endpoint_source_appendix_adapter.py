"""Pinned, complete Markdown witnesses for the endpoint cumulative reader.

Importing this module performs no I/O.  ``prepare_endpoint_witness(builder,
spec)`` writes only below ``builder.BUILD`` and returns ``(wrapper, row)``.
The builder supplies ROOT, BUILD, run(command, receipt_path), and tex_escape.

Required spec fields: key, source (ROOT-relative), title, sha256, bytes,
source_role, location (``appendix`` or ``chapter``).  Optional fields: revision,
revision_role, link_map, required_math_nodes, required_code_blocks.
Each link_map item has old_url, new_url, expected_occurrences (the spelling
expectedoccurrences is also accepted).  Counts refer to exact Link/Image AST
targets, never to prose or code substrings.  required_math_nodes is an exact
total integer or a dict with any of total, inline, display.

The original source bytes are never rewritten.  The prepared AST differs only
at explicitly recorded header levels, header identifiers and link targets; its
exact inverse must recover the entire original AST.  A separate, reversible
writer AST holds unique slots for Math and CodeBlock nodes.  Their complete
original payloads are inserted after Pandoc writes the surrounding structure.
Retained raw TeX nodes use the same exact emission check.  Source metadata is
projected into explicit typed reader blocks with a recorded complete inverse.
No mathematical normalization, ASCII-punctuation rewrite or subsequent global
TeX replacement is performed.  Every inserted UTF-8 payload has final byte
offsets, content and a digest in the conversion receipt.
"""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import shutil
from typing import Any
from urllib.parse import urlsplit


MARKDOWN_FORMAT = (
    "markdown+tex_math_dollars+tex_math_single_backslash"
    "-inline_notes-footnotes-superscript-subscript"
)
SCHEMA = "endpoint-complete-markdown-conversion-v1"


def _sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _json_bytes(value: Any) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True,
                      separators=(",", ":")).encode("utf-8")


def _write_json(path: Path, value: Any) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n",
                    encoding="utf-8", newline="")


def _pointer(parts: tuple) -> str:
    return "".join("/" + str(x).replace("~", "~0").replace("/", "~1")
                   for x in parts)


def _nodes(value: Any, parts: tuple = (), ancestors: tuple = ()):
    """Yield each Pandoc node once, in the original ordered tree traversal."""
    if isinstance(value, dict):
        if isinstance(value.get("t"), str):
            yield parts, value, ancestors
            ancestors = ancestors + (value["t"],)
        for name, child in value.items():
            yield from _nodes(child, parts + (name,), ancestors)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from _nodes(child, parts + (index,), ancestors)


def _at(tree: Any, parts: tuple) -> Any:
    value = tree
    for part in parts:
        value = value[part]
    return value


def _set(tree: Any, parts: tuple, value: Any) -> None:
    if not parts:
        raise ValueError("The root document is never an editable AST field")
    _at(tree, parts[:-1])[parts[-1]] = copy.deepcopy(value)


def _edit(tree: Any, parts: tuple, after: Any, kind: str, edits: list) -> None:
    before = copy.deepcopy(_at(tree, parts))
    if before == after:
        return
    edits.append({"path": _pointer(parts), "parts": list(parts), "kind": kind,
                  "before": before, "after": copy.deepcopy(after)})
    _set(tree, parts, after)


def _inverse_equal(original: Any, changed: Any, edits: list) -> bool:
    restored = copy.deepcopy(changed)
    for edit in reversed(edits):
        parts = tuple(edit["parts"])
        if _at(restored, parts) != edit["after"]:
            return False
        _set(restored, parts, edit["before"])
    return restored == original


def _relative(value: str, name: str) -> str:
    """Accept portable repository locators; reject native/escaping paths."""
    if not isinstance(value, str) or not value or "\\" in value:
        raise ValueError(f"{name} must be a nonempty slash-separated relative path")
    path = PurePosixPath(value)
    if (path.is_absolute() or any(p in ("", ".", "..") for p in value.split("/"))
            or re.match(r"^[A-Za-z]:", value)
            or any(c in value for c in "\r\n\x00{}")):
        raise ValueError(f"{name} must remain inside the reader with no TeX delimiters")
    return path.as_posix()


def _root_path(root: Path, relative: str) -> Path:
    resolved = (root / relative).resolve()
    try:
        resolved.relative_to(root)
    except ValueError as exc:
        raise ValueError("A source path resolves outside the reader root") from exc
    return resolved


def _public_url(value: str) -> None:
    if (not isinstance(value, str) or not value or "\\" in value
            or any(c in value for c in "\r\n\x00")):
        raise ValueError("Link aliases require a public URL or a portable relative locator")
    parsed = urlsplit(value)
    if parsed.scheme:
        if parsed.scheme.lower() not in {"https", "http", "mailto"}:
            raise ValueError("A source alias has an unsupported or native URL scheme")
        if parsed.scheme.lower() in {"https", "http"} and not parsed.netloc:
            raise ValueError("A public HTTP source alias requires its host")
    elif parsed.netloc:
        raise ValueError("Protocol-relative/native source aliases are not portable")
    elif parsed.path:
        _relative(parsed.path, "link alias path")
    elif not parsed.fragment:
        raise ValueError("An empty local source alias is not a complete target")


def _payloads(tree: Any, node_type: str) -> list:
    return [copy.deepcopy(node["c"]) for _, node, _ in _nodes(tree)
            if node["t"] == node_type]


def _node_index(tree: Any, node_type: str) -> list:
    return [{"index": index, "path": _pointer(path),
             "ancestors": list(ancestors), "c": copy.deepcopy(node["c"]),
             "c_sha256": _sha(_json_bytes(node["c"]))}
            for index, (path, node, ancestors) in enumerate(
                (row for row in _nodes(tree) if row[1]["t"] == node_type))]


def _counts(math_nodes: list) -> dict:
    result = {"total": len(math_nodes), "inline": 0, "display": 0}
    for kind, _ in math_nodes:
        if kind == {"t": "InlineMath"}:
            result["inline"] += 1
        elif kind == {"t": "DisplayMath"}:
            result["display"] += 1
        else:
            raise ValueError("Unsupported Math constructor; exact source emission is required")
    return result


def _verify_required_counts(spec: dict, counts: dict, code_count: int) -> None:
    required = spec.get("required_math_nodes")
    if required is not None:
        if isinstance(required, int) and not isinstance(required, bool):
            required = {"total": required}
        if not isinstance(required, dict) or not required:
            raise ValueError("required_math_nodes must be an integer or nonempty count dict")
        for key, expected in required.items():
            if (key not in counts or not isinstance(expected, int)
                    or isinstance(expected, bool) or expected < 0):
                raise ValueError("Only nonnegative exact total/inline/display counts are accepted")
            if counts[key] != expected:
                raise RuntimeError(f"Source Math count mismatch for {key}: {counts[key]} != {expected}")
    if "required_code_blocks" in spec:
        expected = spec["required_code_blocks"]
        if (not isinstance(expected, int) or isinstance(expected, bool)
                or expected < 0 or code_count != expected):
            raise RuntimeError("Complete source CodeBlock count differs from its declared count")


def _attribute_id(node: dict) -> str | None:
    """Known Pandoc Attr-bearing nodes; CodeBlock Attr remains untouched."""
    kind, contents = node["t"], node.get("c")
    if kind == "Header":
        attr = contents[1]
    elif kind in {"Code", "CodeBlock", "Div", "Span", "Link", "Image", "Table", "Figure"}:
        attr = contents[0]
    else:
        return None
    if isinstance(attr, list) and len(attr) == 3 and isinstance(attr[0], str):
        return attr[0]
    return None


def _prepare_ast(original: dict, spec: dict) -> tuple:
    prepared = copy.deepcopy(original)
    edits, anchors, link_rows = [], [], []
    namespace = "endpoint-" + spec["key"] + "--"
    header_ids, other_ids = [], []
    for path, node, _ in _nodes(original):
        identity = _attribute_id(node)
        if identity:
            (header_ids if node["t"] == "Header" else other_ids).append(identity)
        if node["t"] == "Header":
            level, attr, _ = node["c"]
            if not isinstance(level, int) or not 1 <= level <= 5:
                raise RuntimeError("Source headings must support an exact one-level demotion within levels 1..6")
            if not attr[0]:
                raise RuntimeError("Every source Header requires its Pandoc-generated or explicit identifier")
            anchors.append({"source_id": attr[0], "converted_id": namespace + attr[0],
                            "source_path": _pointer(path), "source_level": level,
                            "converted_level": level + 1})
    if len(set(header_ids)) != len(header_ids):
        raise RuntimeError("Duplicate source Header identifiers prevent an identifier bijection")
    # Non-header anchors need a separate, explicit extension: silently retaining
    # their global names would violate namespace isolation or CodeBlock.c equality.
    if other_ids:
        raise RuntimeError("Non-Header identifiers require an explicit complete anchor policy: "
                           + ", ".join(sorted(set(other_ids))))
    id_map = {row["source_id"]: row["converted_id"] for row in anchors}
    if len(set(id_map.values())) != len(id_map):
        raise RuntimeError("The simultaneous source Header identifier map is not injective")

    aliases, alias_rows = {}, []
    for item in spec.get("link_map", []):
        old, new = item["old_url"], item["new_url"]
        if not isinstance(old, str) or not old or old in aliases:
            raise ValueError("Each link_map old_url must be nonempty and unique")
        _public_url(new)
        if old.startswith("#") and old[1:] in id_map:
            raise ValueError("An explicit alias overlaps the simultaneous Header identifier map")
        if "expected_occurrences" in item and "expectedoccurrences" in item:
            if item["expected_occurrences"] != item["expectedoccurrences"]:
                raise ValueError("Conflicting alias occurrence spellings")
        expected = item.get("expected_occurrences", item.get("expectedoccurrences"))
        if not isinstance(expected, int) or isinstance(expected, bool) or expected < 0:
            raise ValueError("Every link alias needs an exact nonnegative expected_occurrences")
        row = {"old_url": old, "new_url": new, "expected_occurrences": expected,
               "observed_occurrences": 0, "node_paths": []}
        aliases[old] = row
        alias_rows.append(row)

    for path, node, _ in _nodes(original):
        if node["t"] == "Header":
            _edit(prepared, path + ("c", 0), node["c"][0] + 1, "heading_level", edits)
            old_id = node["c"][1][0]
            _edit(prepared, path + ("c", 1, 0), id_map[old_id], "header_identifier", edits)
        elif node["t"] in {"Link", "Image"}:
            target = node["c"][2][0]
            new_target, kind = target, "unchanged"
            if target in aliases:
                alias = aliases[target]
                new_target, kind = alias["new_url"], "explicit_source_link_alias"
                alias["observed_occurrences"] += 1
                alias["node_paths"].append(_pointer(path))
            elif target.startswith("#"):
                if target[1:] not in id_map:
                    raise RuntimeError("An internal source target has no Header or explicit alias: " + target)
                new_target, kind = "#" + id_map[target[1:]], "internal_header_target"
            _edit(prepared, path + ("c", 2, 0), new_target, kind, edits)
            if new_target.startswith("#") and new_target[1:] not in set(id_map.values()):
                raise RuntimeError("A prepared internal target has no converted Header: " + new_target)
            if new_target.lower().startswith(("sandbox:", "file:")):
                raise RuntimeError("A source download/native link needs an explicit portable alias: " + target)
            link_rows.append({"path": _pointer(path), "node_type": node["t"],
                              "original_target": target, "prepared_target": new_target,
                              "operation": kind})
    for row in alias_rows:
        if row["observed_occurrences"] != row["expected_occurrences"]:
            raise RuntimeError("Explicit source link occurrence count mismatch: " + row["old_url"])
    if not _inverse_equal(original, prepared, edits):
        raise RuntimeError("Reversing the declared edits does not reconstruct the complete original AST")
    return prepared, edits, anchors, link_rows, alias_rows


def _project_metadata(prepared: dict) -> tuple:
    """Render every metadata field explicitly without changing prepared data."""
    projected = copy.deepcopy(prepared)
    edits, mapping, blocks = [], [], []

    def render(name: str, value: dict, source_path: tuple) -> list:
        kind = value.get("t")
        label = {"t": "Para", "c": [{"t": "Strong", "c": [
            {"t": "Str", "c": "Source metadata: " + name + " (" + str(kind) + ")"}]}]}
        if kind == "MetaInlines":
            body = [{"t": "Para", "c": copy.deepcopy(value["c"])}]
        elif kind == "MetaBlocks":
            body = copy.deepcopy(value["c"])
        elif kind == "MetaString":
            body = [{"t": "Para", "c": [{"t": "Str", "c": value["c"]}]}]
        elif kind == "MetaBool":
            body = [{"t": "Para", "c": [{"t": "Str", "c": "true" if value["c"] else "false"}]}]
        elif kind == "MetaList":
            body = [{"t": "OrderedList", "c": [[1, {"t": "Decimal"}, {"t": "Period"}],
                [render(str(i), child, source_path + ("c", i))
                 for i, child in enumerate(value["c"])]]}]
        elif kind == "MetaMap":
            body = []
            for child_name, child in value["c"].items():
                body.extend(render(child_name, child, source_path + ("c", child_name)))
        else:
            raise RuntimeError("Unsupported metadata constructor cannot be silently omitted: " + str(kind))
        mapping.append({"source_path": _pointer(source_path), "field": name,
                        "constructor": kind, "complete_original_value": copy.deepcopy(value),
                        "complete_rendered_blocks": copy.deepcopy([label] + body)})
        return [label] + body

    for field, value in prepared.get("meta", {}).items():
        blocks.extend(render(field, value, ("meta", field)))
    if blocks:
        _edit(projected, ("meta",), {}, "writer_metadata_retained_in_explicit_body", edits)
        _edit(projected, ("blocks",), blocks + prepared["blocks"],
              "writer_prepend_complete_typed_metadata", edits)
    if not _inverse_equal(prepared, projected, edits):
        raise RuntimeError("Explicit metadata projection does not invert to complete prepared data")
    return projected, edits, mapping, len(blocks)


def _writer_ast(prepared: dict, key: str, digest: str) -> tuple:
    projected, edits, metadata_mapping, metadata_block_count = _project_metadata(prepared)
    writer = copy.deepcopy(projected)
    slots = []
    literal_kinds = {"Math", "CodeBlock", "RawInline", "RawBlock"}
    original_literals = [row for row in _nodes(prepared) if row[1]["t"] in literal_kinds]
    projected_literals = [row for row in _nodes(projected) if row[1]["t"] in literal_kinds]
    if [(n["t"], n["c"]) for _, n, _ in original_literals] != [
            (n["t"], n["c"]) for _, n, _ in projected_literals]:
        raise RuntimeError("Metadata projection changed or reordered source literal nodes")
    prefix = "ENDPOINTSOURCE" + _sha((key + ":" + digest).encode("utf-8"))[:24].upper()
    if prefix in json.dumps(prepared, ensure_ascii=False):
        raise RuntimeError("Writer slot namespace occurs in the complete original content")
    for (path, node, ancestors), (source_path, _, source_ancestors) in zip(
            projected_literals, original_literals):
        kind = node["t"]
        payload = node["c"][1]
        if not isinstance(payload, str):
            raise RuntimeError("A literal source node has a non-string payload")
        if kind == "CodeBlock":
            if any(a in {"Header", "Link", "Image", "Note", "Table", "Figure"} for a in ancestors):
                raise RuntimeError("Literal source code inside a TeX macro argument requires a dedicated renderer")
            if r"\end{verbatim}" in payload:
                raise RuntimeError("A literal source code body contains its TeX environment terminator")
            opening, closing = "\\begin{verbatim}\n", "\n\\end{verbatim}"
            replacement_type = "RawBlock"
        elif kind == "Math":
            math_kind = node["c"][0]["t"]
            opening, closing = ((r"\(", r"\)") if math_kind == "InlineMath"
                                else (r"\[", r"\]"))
            replacement_type = "RawInline"
        else:
            opening, closing, replacement_type = "", "", kind
        token = prefix + "SLOT" + str(len(slots)) + "END"
        replacement = {"t": replacement_type, "c": ["latex", token]}
        _edit(writer, path, replacement, "writer_only_literal_slot", edits)
        slots.append({"index": len(slots), "path": _pointer(source_path),
                      "writer_path": _pointer(path), "node_type": kind,
                      "ancestors": list(source_ancestors), "writer_ancestors": list(ancestors),
                      "original_c": copy.deepcopy(node["c"]), "token": token,
                      "opening": opening, "payload": payload, "closing": closing,
                      "payload_sha256": _sha(payload.encode("utf-8")),
                      "payload_bytes": len(payload.encode("utf-8"))})
    if not _inverse_equal(prepared, writer, edits):
        raise RuntimeError("Writer slots do not invert to the complete prepared AST")
    return writer, slots, edits, prefix, metadata_mapping, metadata_block_count


def _expand_slots(converted: str, slots: list, prefix: str) -> tuple:
    encoded = converted.encode("utf-8")
    positions = []
    for slot in slots:
        token = slot["token"].encode("ascii")
        if encoded.count(token) != 1:
            raise RuntimeError("Pandoc suppressed or duplicated a complete source literal slot: "
                               + slot["path"])
        positions.append(encoded.index(token))
    if positions != sorted(positions):
        raise RuntimeError("Pandoc reordered the original source Math/CodeBlock traversal")
    chunks, spans, cursor, length = [], [], 0, 0
    for position, slot in zip(positions, slots):
        prefix_bytes = encoded[cursor:position]
        chunks.append(prefix_bytes)
        length += len(prefix_bytes)
        opening = slot["opening"].encode("utf-8")
        payload = slot["payload"].encode("utf-8")
        closing = slot["closing"].encode("utf-8")
        fragment = opening + payload + closing
        spans.append({k: copy.deepcopy(v) for k, v in slot.items() if k != "token"})
        spans[-1].update({"fragment_start_byte": length,
                          "payload_start_byte": length + len(opening),
                          "payload_end_byte": length + len(opening) + len(payload),
                          "fragment_end_byte": length + len(fragment),
                          "fragment_sha256": _sha(fragment)})
        chunks.append(fragment)
        length += len(fragment)
        cursor = position + len(slot["token"].encode("ascii"))
    chunks.append(encoded[cursor:])
    final = b"".join(chunks)
    if prefix.encode("ascii") in final:
        raise RuntimeError("An unresolved source emission slot remains in the final TeX")
    for span in spans:
        if final[span["payload_start_byte"]:span["payload_end_byte"]] != span["payload"].encode("utf-8"):
            raise RuntimeError("A generated source literal payload failed its exact byte-span check")
        if _sha(final[span["fragment_start_byte"]:span["fragment_end_byte"]]) != span["fragment_sha256"]:
            raise RuntimeError("A generated source literal frame failed its exact byte-span check")
    return final, spans


def _roundtrip_report(source_math: list, parsed_math: list) -> dict:
    report = {"original_ordered_math_c": source_math,
              "parsed_ordered_math_c": parsed_math,
              "ordered_math_c_equal": source_math == parsed_math,
              "original_count": len(source_math), "parsed_count": len(parsed_math)}
    differences = []
    for index in range(max(len(source_math), len(parsed_math))):
        before = source_math[index] if index < len(source_math) else None
        after = parsed_math[index] if index < len(parsed_math) else None
        if before != after:
            edge_only = (before is not None and after is not None
                         and before[0] == after[0]
                         and before[1].strip() == after[1].strip())
            differences.append({"index": index, "source_c": before, "parsed_c": after,
                                "parser_difference_only_at_payload_edge_whitespace": edge_only})
    report["differences"] = differences
    report["comparison_scope"] = (
        "The LaTeX re-reader is audited without using its result to rewrite any source or output. "
        "It can trim delimiter-adjacent whitespace or parse retained raw TeX as additional Math. "
        "The exact final payload byte-span audit separately proves complete Math.c payload emission.")
    return report


def prepare_endpoint_witness(builder, spec: dict) -> tuple[str, dict]:
    """Convert one complete pinned Markdown source; return its wrapper and row."""
    required = {"key", "source", "title", "sha256", "bytes", "source_role", "location"}
    missing = required.difference(spec)
    if missing:
        raise ValueError("Missing endpoint source spec fields: " + ", ".join(sorted(missing)))
    key = spec["key"]
    if not isinstance(key, str) or not re.fullmatch(r"[a-z][a-z0-9_]*", key):
        raise ValueError("Source key must be lowercase ASCII letters, digits and underscores")
    if spec["location"] not in {"appendix", "chapter"}:
        raise ValueError("Source location must be appendix or chapter")
    if any(not isinstance(spec[field], str) or not spec[field] for field in ("title", "source_role")):
        raise ValueError("Source title and source_role must be nonempty plain text")
    revision_text = str(spec.get("revision", spec["sha256"]))
    if not revision_text or any(c in revision_text for c in "{}\\\r\n\x00"):
        raise ValueError("Source revision must be safe literal text for a breakable revision locator")
    if not re.fullmatch(r"[0-9a-f]{64}", spec["sha256"]):
        raise ValueError("Source sha256 must be an exact lowercase SHA-256")
    if not isinstance(spec["bytes"], int) or isinstance(spec["bytes"], bool) or spec["bytes"] < 0:
        raise ValueError("Source bytes must be an exact nonnegative integer")
    root = Path(builder.ROOT).resolve()
    build = Path(builder.BUILD).resolve()
    try:
        build.relative_to(root)
    except ValueError as exc:
        raise ValueError("Builder BUILD must be inside its independent reader ROOT") from exc
    source_relative = _relative(spec["source"], "source")
    path = _root_path(root, source_relative)
    original_bytes = path.read_bytes()
    digest = _sha(original_bytes)
    if len(original_bytes) != spec["bytes"] or digest != spec["sha256"]:
        raise RuntimeError("The complete source witness differs from its pinned bytes or SHA-256")
    # Validate UTF-8 independently; Pandoc performs the syntax parse.  A BOM is
    # accepted but remains part of the immutable source byte/hash witness.
    original_bytes.decode("utf-8-sig", errors="strict")
    pandoc = shutil.which("pandoc")
    if not pandoc:
        raise RuntimeError("pandoc not found")
    names = {name: build / f"endpoint_{key}_{suffix}" for name, suffix in {
        "original_ast": "original_ast.json", "prepared_ast": "prepared_ast.json",
        "writer_ast": "writer_ast.json", "emitted": "writer_slots.tex",
        "converted": "source.tex", "roundtrip_ast": "latex_roundtrip_ast.json",
        "conversion": "conversion.json", "pandoc_log": "pandoc.log",
        "roundtrip_log": "latex_roundtrip.log"}.items()}
    for output_path in names.values():
        resolved_output = output_path.resolve()
        try:
            resolved_output.relative_to(build)
        except ValueError as exc:
            raise ValueError("A generated source artifact resolves outside BUILD") from exc
        if resolved_output == path or (output_path.exists() and path.samefile(output_path)):
            raise ValueError("A generated source artifact aliases the immutable original witness")
    if len({value.resolve() for value in names.values()}) != len(names):
        raise ValueError("Two generated source artifacts resolve to the same path")
    build.mkdir(parents=True, exist_ok=True)
    relative = lambda p: p.relative_to(root).as_posix()
    parsed = builder.run([pandoc, source_relative, "--from=" + MARKDOWN_FORMAT,
                          "--to=json"], names["original_ast"])
    original = json.loads(parsed)
    if not isinstance(original, dict) or not isinstance(original.get("blocks"), list):
        raise RuntimeError("Pandoc did not return a complete document AST")
    raw_nodes = []
    for node_path, node, ancestors in _nodes(original):
        if node["t"] in {"RawInline", "RawBlock"}:
            if node["c"][0] not in {"tex", "latex"}:
                raise RuntimeError("A non-LaTeX raw source block would be dropped by the writer: " + _pointer(node_path))
            raw_nodes.append({"path": _pointer(node_path), "ancestors": list(ancestors),
                              "node_type": node["t"], "c": copy.deepcopy(node["c"])})
    _write_json(names["original_ast"], original)
    original_math = _payloads(original, "Math")
    original_code = _payloads(original, "CodeBlock")
    math_counts = _counts(original_math)
    _verify_required_counts(spec, math_counts, len(original_code))
    prepared, edits, anchors, links, aliases = _prepare_ast(original, spec)
    if original_math != _payloads(prepared, "Math"):
        raise RuntimeError("The complete ordered Math.c lists changed in the prepared AST")
    if original_code != _payloads(prepared, "CodeBlock"):
        raise RuntimeError("The complete ordered CodeBlock.c lists changed in the prepared AST")
    _write_json(names["prepared_ast"], prepared)
    writer, slots, writer_edits, slot_prefix, metadata_mapping, metadata_block_count = _writer_ast(prepared, key, digest)
    _write_json(names["writer_ast"], writer)
    builder.run([pandoc, relative(names["writer_ast"]), "--from=json", "--to=latex",
                 "--no-highlight", "--wrap=none", "--output", relative(names["emitted"])],
                names["pandoc_log"])
    emitted_text = names["emitted"].read_bytes().decode("utf-8")
    code_layout = []
    def breakable_code(match):
        token = match.group(1)
        plain = re.sub(r"\\([_#%&$])", r"\1", token)
        if "\\" in plain or "{" in plain or "}" in plain:
            return match.group(0)
        after = r"\nolinkurl{" + plain + "}"
        code_layout.append({"before": match.group(0), "after": after,
                            "original_rendered_text": plain})
        return after
    emitted_text = re.sub(r"\\texttt\{((?:\\.|[^{}])*)\}", breakable_code, emitted_text)
    final_bytes, literal_spans = _expand_slots(emitted_text, slots, slot_prefix)
    names["converted"].write_bytes(final_bytes)
    # Content substitutions end above.  The following read and comparisons are
    # evidence collection only; they cannot alter the final source TeX.
    roundtrip = {"status": "not_attempted"}
    converted_headers = []
    try:
        reparsed = builder.run([pandoc, relative(names["converted"]), "--from=latex",
                                "--to=json"], names["roundtrip_log"])
        latex_ast = json.loads(reparsed)
        _write_json(names["roundtrip_ast"], latex_ast)
        roundtrip = _roundtrip_report(original_math, _payloads(latex_ast, "Math"))
        roundtrip["status"] = "parsed_and_compared"
        roundtrip["ast"] = relative(names["roundtrip_ast"])
        roundtrip["parsed_code_blocks"] = _node_index(latex_ast, "CodeBlock")
        roundtrip["ordered_codeblock_c_equal"] = original_code == _payloads(latex_ast, "CodeBlock")
        roundtrip["code_comparison_scope"] = (
            "CodeBlock Attr and delimiter-adjacent newlines can change in the LaTeX re-reader. "
            "Every complete original code payload, including terminal newlines, is verified by final byte spans.")
        converted_headers = _node_index(latex_ast, "Header")
    except (RuntimeError, json.JSONDecodeError) as exc:
        roundtrip = {"status": "latex_reader_could_not_parse",
                     "exception_class": type(exc).__name__,
                     "log": relative(names["roundtrip_log"]),
                     "source_payload_byte_span_audit_passed": True}
    if path.read_bytes() != original_bytes:
        raise RuntimeError("The pinned original source changed during conversion")
    if names["converted"].read_bytes() != final_bytes:
        raise RuntimeError("The final TeX changed after its exact payload span audit")

    source_record = {"path": source_relative, "sha256": digest, "bytes": len(original_bytes),
                     "source_role": spec["source_role"], "location": spec["location"],
                     "revision": spec.get("revision", digest),
                     "revision_role": spec.get("revision_role", "Complete source witness SHA-256")}
    receipt = {
        "schema": SCHEMA, "code_layout": code_layout, "source": source_record, "source_unchanged_after_conversion": True,
        "adapter_sha256": _sha(Path(__file__).read_bytes()), "markdown_format": MARKDOWN_FORMAT,
        "pandoc_ast_api_version": original.get("pandoc-api-version"),
        "top_level_source_blocks": len(original["blocks"]),
        "top_level_prepared_blocks": len(prepared["blocks"]),
        "full_original_ast_sha256": _sha(_json_bytes(original)),
        "full_prepared_ast_sha256": _sha(_json_bytes(prepared)),
        "full_writer_ast_sha256": _sha(_json_bytes(writer)),
        "prepared_edits": edits, "prepared_edit_inverse_restores_complete_original_ast": True,
        "writer_edits": writer_edits, "writer_edit_inverse_restores_complete_prepared_ast": True,
        "complete_typed_metadata_body_projection": metadata_mapping,
        "metadata_projection_prepended_block_count": metadata_block_count,
        "header_identifier_bijection": anchors, "link_targets": links, "explicit_link_aliases": aliases,
        "source_heading_index": _node_index(original, "Header"),
        "prepared_heading_index": _node_index(prepared, "Header"),
        "converted_heading_index": converted_headers,
        "source_math_index": _node_index(original, "Math"),
        "prepared_math_index": _node_index(prepared, "Math"),
        "math_node_counts": math_counts, "ordered_original_prepared_math_c_equal": True,
        "original_prepared_math_equal": True,
        "prepared_generated_math_equal": True,
        "prepared_generated_math_equality_scope": (
            "Every original/prepared Math.c type and full payload is emitted once in source order "
            "with its exact inline/display delimiters and verified final UTF-8 byte spans. "
            "This claim does not substitute the LaTeX re-reader's whitespace-changing representation."),
        "source_codeblock_index": _node_index(original, "CodeBlock"),
        "ordered_original_prepared_codeblock_c_equal": True,
        "retained_source_raw_tex_nodes": raw_nodes,
        "all_retained_raw_tex_payloads_emitted_once_with_exact_byte_spans": True,
        "literal_emission_spans": literal_spans, "all_slots_emitted_once_in_source_order": True,
        "all_complete_literal_payload_byte_spans_equal_original": True,
        "literal_payload_scope": (
            "Exact UTF-8 encodings of the complete original Pandoc Math.c and CodeBlock.c text values. "
            "Original Markdown file bytes, fences and line endings are separately retained by source hash. "
            "Raw TeX source nodes are retained separately and may contain additional mathematics."),
        "heading_math_scope": (
            "Primary headings contain the complete original Math payloads. "
            "Pandoc handles secondary PDF bookmark text using its raw-inline fallback."),
        "generated_latex_roundtrip": roundtrip,
        "generated_tex": {"path": relative(names["converted"]), "bytes": len(final_bytes),
                          "sha256": _sha(final_bytes)},
        "artifacts": {name: relative(value) for name, value in names.items()
                      if name != "roundtrip_ast" or roundtrip["status"] == "parsed_and_compared"},
        "source_math_or_code_executed": False,
    }
    _write_json(names["conversion"], receipt)
    esc = builder.tex_escape
    wrapper = (
        "\\begingroup\n\\sloppy\n\\small\n"
        + ("\\let\\split\\aligned\n\\let\\endsplit\\endaligned\n" if key == "volume_connection_original" else "")
        + ("\\clearpage\n" if spec["location"] == "appendix" else "")
        + "\\section{" + esc(spec["title"]) + "}\n"
        + "\\noindent\\textbf{Source role.} " + esc(spec["source_role"]) + "\\par\n"
        + "\\noindent\\textbf{Exact revision.} \\nolinkurl{" + revision_text + "}\\par\n"
        + "\\noindent\\textbf{Complete source.} \\path{" + source_relative + "}\\par\n"
        + "\\noindent\\textbf{Source SHA-256.} \\nolinkurl{" + digest + "}\\par\\medskip\n"
        + "\\input{" + relative(names["converted"]) + "}\n\\endgroup\n")
    row = {
        "key": key, "pr": spec.get("pr"), "title": spec["title"],
        "source": source_relative, "sha256": digest, "bytes": len(original_bytes),
        "revision": source_record["revision"], "revision_role": source_record["revision_role"],
        "source_role": spec["source_role"], "location": spec["location"],
        "source_format": "complete pinned Markdown mathematical witness",
        "complete_source_preserved": True, "source_pin_verified": True,
        "converted": relative(names["converted"]), "converted_sha256": _sha(final_bytes),
        "conversion_receipt": relative(names["conversion"]),
        "conversion_receipt_sha256": _sha(names["conversion"].read_bytes()),
        "all_prepared_math_spans_preserved_exactly": True,
        "inline_math_nodes": math_counts["inline"], "display_math_nodes": math_counts["display"],
        "source_code_blocks": len(original_code), "source_code_blocks_preserved": True,
        "lean_source_blocks": sum("lean" in item[0][1] for item in original_code),
        "source_code_execution": "No source code or mathematical checker is executed by this adapter.",
        "prepared_edit_inverse_restores_complete_original_ast": True,
        "all_complete_literal_payload_byte_spans_equal_original": True,
        "latex_roundtrip_status": roundtrip["status"],
        "latex_roundtrip_ordered_math_c_equal": roundtrip.get("ordered_math_c_equal"),
        "header_identifier_bijection": anchors, "explicit_link_aliases": aliases,
    }
    return wrapper, row
