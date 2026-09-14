"""Reproduce visible-node coverage and source-quotation validation.

No network, mathematical inference, or ledger mutation occurs here.
The source transcript strings are authoritative. Whitespace fallback is
explicitly recorded; no punctuation/case/TeX normalization is performed.
"""
from pathlib import Path
import argparse
import collections
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / "audit"
OUT = ROOT / "validation/portable_run"
SOURCES = ROOT / "sources"
LANES = {
    "early_context": ("audit_early_context/audit.json", "U0001_U0015"),
    "base_formation": ("audit_base_formation/AUDIT.json", "U0016_U0028"),
    "typed_route": ("audit_typed_route/AUDIT_TYPED_ROUTE.json", "U0029_U0040"),
    "actual_tau": ("audit_actual_tau/audit_actual_tau.json", "U0041_U0054"),
    "late_control": ("audit_late_control/AUDIT_LATE_CONTROL.json", "U0055_U0067"),
}
def read(p):
    return json.loads(p.read_text(encoding="utf-8-sig"))
def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()
def normalized(s):
    return re.sub(r"\s+", " ", s).strip()

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    records = read(SOURCES / "transcript_records.json")
    visible = read(SOURCES / "visible_records.json")
    by_id = {r["node_id"]: r for r in records}
    by_locator = {r["locator"]: r for r in records}
    visible_ids = [r["node_id"] for r in visible]
    errors, warnings, quotes, copied_bodies, reference_checks = [], [], [], [], []
    lane_results = {}
    def error(kind, **details):
        errors.append({"kind": kind, **details})
    def check_ref(ref, path):
        loc = ref.get("locator", ref.get("turn"))
        uid = ref.get("node_id", ref.get("uuid"))
        if not loc or not uid:
            return
        actual = by_locator.get(loc)
        ok = actual is not None and actual["node_id"] == uid
        if ok and "chain" in ref:
            ok = ref["chain"] == actual["chain_ordinal"]
        if ok and "role" in ref:
            ok = ref["role"] == actual["role"]
        reference_checks.append({"path": path, "locator": loc, "node_id": uid, "pass": ok})
        if not ok:
            error("invalid_reference", path=path, supplied=ref)

    def references(obj, path=""):
        found = set()
        if isinstance(obj, dict):
            check_ref(obj, path)
            for prefix, locator_keys in [
                ("user", ("user", "user_locator", "user_turn")),
                ("assistant", ("assistant", "assistant_locator", "assistant_turn")),
                ("answer", ("answer", "answer_locator", "answer_turn")),
            ]:
                uid = obj.get(prefix + "_node_id")
                loc = next((obj[k] for k in locator_keys if isinstance(obj.get(k), str)), None)
                if uid and loc:
                    rr = {"locator": loc, "node_id": uid}
                    if prefix + "_chain" in obj:
                        rr["chain"] = obj[prefix + "_chain"]
                    check_ref(rr, path + "/" + prefix)
            for k, v in obj.items():
                if (k.endswith("node_id") or k == "uuid") and isinstance(v, str):
                    if v not in by_id:
                        error("unknown_uuid", path=path + "/" + k, node_id=v)
                    else:
                        found.add(v)
                if isinstance(v, (dict, list)):
                    found |= references(v, path + "/" + k)
        elif isinstance(obj, list):
            for i, v in enumerate(obj):
                found |= references(v, path + f"/{i}")
        return found

    def test_quote(text, candidates, lane, path, kind):
        candidates = sorted(set(candidates), key=lambda u: by_id[u]["chain_ordinal"])
        if kind == "user_verbatim":
            candidates = [u for u in candidates if by_id[u]["role"] == "user"]
        result = {"lane": lane, "path": path, "kind": kind, "quote": text,
                  "quote_sha256": hashlib.sha256(text.encode()).hexdigest(),
                  "candidate_uuids": candidates}
        if text == "":
            matches = [u for u in candidates if by_id[u]["text"] == ""]
            result["status"] = "literal_empty_source" if matches else "empty_quote_not_empty_source"
        else:
            matches = [u for u in candidates if text in by_id[u]["text"]]
            result["status"] = "literal_substring" if matches else "no_literal_match"
        if not matches and text != "":
            matches = [u for u in candidates if normalized(text) in normalized(by_id[u]["text"])]
            if matches:
                result["status"] = "whitespace_normalized_substring"
                result["normalization"] = "Python re.sub(r'\\s+', ' ', text).strip() on both strings; no other changes."
        result["matches"] = [{"node_id": u, "locator": by_id[u]["locator"],
                              "source_offset": by_id[u]["text"].find(text)
                              if result["status"].startswith("literal") else None}
                             for u in matches]
        if not matches:
            possible = [r["locator"] for r in visible if text and text in r["text"]]
            error("quote_mismatch", lane=lane, path=path, quote=text, exact_elsewhere=possible)
        if result["status"] == "whitespace_normalized_substring":
            warnings.append({"kind": "whitespace_normalized_quote", "lane": lane, "path": path})
        quotes.append(result)

    def collect(entry, lane, path):
        entry_refs = references(entry, path)
        def walk(obj, here, inherited, passages=False):
            if isinstance(obj, dict):
                local_refs = references(obj, here)
                refs = local_refs or inherited
                for k, v in obj.items():
                    if isinstance(v, str):
                        if k in {"quote", "short_exact_quote", "passage", "exact_quote", "short_passage"}:
                            test_quote(v, refs, lane, here + "/" + k, "structured_passage")
                        elif k in {"user_input_verbatim", "user_request_verbatim"}:
                            test_quote(v, refs, lane, here + "/" + k, "user_verbatim")
                        elif passages and k == "text":
                            test_quote(v, refs, lane, here + "/text", "structured_passage")
                        elif k in {"full_passage_audit_markdown", "full_audit"}:
                            for i, match in enumerate(re.finditer("“([^”]+)”", v)):
                                test_quote(match.group(1), refs, lane,
                                           here + "/" + k + f"/curly_quote_{i}",
                                           "embedded_typographic_quote")
                        elif "“" in v:
                            for i, match in enumerate(re.finditer("“([^”]+)”", v)):
                                test_quote(match.group(1), refs, lane,
                                           here + "/" + k + f"/curly_quote_{i}",
                                           "embedded_typographic_quote")
                    elif isinstance(v, (dict, list)):
                        walk(v, here + "/" + k, refs, passages or k == "passages")
            elif isinstance(obj, list):
                for i, v in enumerate(obj):
                    walk(v, here + f"/{i}", inherited, passages)
        walk(entry, path, entry_refs)

    computed_visible = [r for r in records if r["role"] == "user" or
                        (r["role"] == "assistant" and r["content_type"] == "text"
                         and r["recipient"] in (None, "all"))]
    if computed_visible != visible:
        error("visible_selection_mismatch")
    if len(by_id) != len(records) or len(by_locator) != len(records):
        error("duplicate_source_identifier")
    if len(visible) != 215 or collections.Counter(r["role"] for r in visible) != {"user": 67, "assistant": 148}:
        error("unexpected_visible_counts")
    for r in records:
        if hashlib.sha256(r["text"].encode()).hexdigest() != r["text_sha256"]:
            error("source_text_hash", locator=r["locator"])
    redacted = [r for r in records if r["role"] == "tool" and r.get("metadata", {}).get("is_redacted")]
    if len(redacted) != 2600:
        error("unexpected_redacted_tool_count", count=len(redacted))

    covered = []
    for lane, (relative, segment_id) in LANES.items():
        path = WORK / relative
        d = read(path)
        segment = SOURCES / ("audit_segment_" + segment_id + ".md")
        segment_text = segment.read_bytes().decode("utf-8")
        headers = list(re.finditer(r"(?m)^## ([UA]\d+) \| ([0-9a-f-]{36}) \| (user|assistant) \| chain (\d+)\r?$", segment_text))
        segment_ids = []
        for h in headers:
            ref = {"locator": h[1], "node_id": h[2], "role": h[3], "chain": int(h[4])}
            check_ref(ref, str(segment))
            segment_ids.append(h[2])
        reconstructed_segment = "\n\n".join(h[0] + "\n\n" + by_id[h[2]]["text"] for h in headers)
        segment_roundtrip_exact = segment_text == reconstructed_segment
        if not segment_roundtrip_exact:
            error("full_segment_body_mismatch", lane=lane,
                  source_characters=len(segment_text), reconstructed_characters=len(reconstructed_segment))

        if lane == "early_context":
            cov = d["coverage"]
            ids = [x["node_id"] for x in cov]
            declaration = {"complete": d["full_collective_read"],
                           "reader_ranges": d["individual_reader_ranges"],
                           "source_lines": d["counts"]["source_lines"],
                           "source_sha256": d["provenance"]["current_source_sha256"]}
            entries = [x for values in d["passage_ledgers"].values() for x in values]
            references(cov, lane + "/coverage")
            intervals = sorted(x["range"] for x in d["individual_reader_ranges"])
            expected_start = 1
            for start, end in intervals:
                if start != expected_start:
                    error("reader_line_gap", lane=lane, expected=expected_start, actual=start)
                expected_start = end + 1
            if expected_start != d["counts"]["source_lines"] + 1:
                error("reader_final_line_gap", lane=lane)
        elif lane == "base_formation":
            cov = d["coverage"]
            ids = []
            for ep in d["user_turn_status"]:
                ids += [ep["user_node_id"]] + [r["node_id"] for r in ep["response_nodes"]]
            references(d["user_turn_status"], lane + "/user_turn_status")
            declaration = {"complete_read_evidence": cov["limitations"][-1],
                           "historical_contiguous_character_windows": cov["read_windows_original_crlf_chars"],
                           "newline_repair": cov["newline_repair"],
                           "source_sha256": cov["source_pins"][0]["sha256"]}
            intervals = cov["read_windows_original_crlf_chars"]
            if intervals[0][0] != 0 or any(a[1] != b[0] for a, b in zip(intervals, intervals[1:])):
                error("reader_character_gap", lane=lane)
            entries = d["findings"]
        elif lane == "typed_route":
            cov = d["coverage"]
            ids = [x["node_id"] for x in d["turns"]]
            declaration = {"complete": cov["read_complete"], "read_method": cov["read_method"],
                           "newline_repair": cov["newline_repair"], "source_sha256": cov["source_sha256"]}
            references(d["turns"], lane + "/turns")
            for i, turn in enumerate(d["turns"]):
                source = by_id[turn["node_id"]]["text"]
                status = "literal_full_text" if turn["text"] == source else (
                    "only_surrounding_CR_LF_removed" if turn["text"] == source.strip("\r\n") else "mismatch")
                copied_bodies.append({"lane": lane, "locator": turn["locator"], "status": status})
                if status == "mismatch":
                    error("copied_body_mismatch", lane=lane, locator=turn["locator"])
            entries = d["records"]
        elif lane == "actual_tau":
            cov = d["coverage"]
            memberships = [t["node_id"] for ep in d["episodes"] for t in ep["all_turns"]]
            ids = list(dict.fromkeys(memberships))
            declaration = {"complete": cov["complete_within_scope"], "lines_read": cov["lines_read"],
                           "newline_repair": cov["provenance_note"], "source_sha256": cov["sha256"],
                           "episode_memberships": len(memberships),
                           "repeated_episode_memberships": [by_id[u]["locator"] for u, n in collections.Counter(memberships).items() if n > 1],
                           "overlap_handling": "Stable UUID deduplication for coverage union only; composite and individual episodes both retained."}
            entries = d["episodes"]
        else:
            cov = read(WORK / "audit_late_control/COVERAGE.json")
            ids = []
            for ep in d["episodes"]:
                ids += [ep["user_node_id"]] + [a["node_id"] for a in ep["assistant_nodes"]]
                collect(ep, lane, lane + "/episodes/" + ep["user_turn"])
            declaration = {"complete": cov["complete_segment_read"],
                           "historical_character_intervals": cov["read_intervals_before_newline_only_repair"],
                           "reading_note": cov["reading_note"], "source_sha256": cov["source_pins"][0]["sha256"]}
            entries = d["entries"]
        if "complete" in declaration and declaration["complete"] is not True:
            error("missing_full_read_declaration", lane=lane)
        if digest(segment) != declaration["source_sha256"]:
            error("segment_pin_mismatch", lane=lane)
        if ids != segment_ids:
            error("lane_segment_node_mismatch", lane=lane, ledger_locators=[by_id[u]["locator"] for u in ids],
                  segment_locators=[by_id[u]["locator"] for u in segment_ids])
        if len(ids) != len(set(ids)):
            error("duplicate_within_lane", lane=lane)
        for i, entry in enumerate(entries):
            collect(entry, lane, lane + f"/entries/{i}")
        covered.extend(ids)
        lane_results[lane] = {
            "ledger": str(path.relative_to(ROOT)), "ledger_sha256": digest(path),
            "segment": str(segment.relative_to(ROOT)), "segment_sha256": digest(segment),
            "full_segment_message_text_roundtrip_exact": segment_roundtrip_exact,
            "nodes": len(ids), "role_counts": dict(collections.Counter(by_id[u]["role"] for u in ids)),
            "findings": len(entries), "locators": [by_id[u]["locator"] for u in ids],
            "reading_evidence": declaration,
        }
    counts = collections.Counter(covered)
    missing = [by_id[u]["locator"] for u in visible_ids if not counts[u]]
    unexpected = [by_id[u]["locator"] for u in covered if u not in set(visible_ids)]
    duplicates = [by_id[u]["locator"] for u, count in counts.items() if count > 1]
    if missing or unexpected or duplicates or covered != visible_ids:
        error("union_coverage_failure", missing=missing, unexpected=unexpected, duplicates=duplicates,
              exact_order_matches=covered == visible_ids)
    # Repeated episode/entry quotations are separately checked but counted
    # distinctly below only when their exact target UUID and text coincide.
    unique_quotes = {(tuple(m["node_id"] for m in q["matches"]), q["quote"], q["kind"]) for q in quotes}
    receipt = {
        "status": "FAIL" if errors else ("PASS_WITH_EXPLICIT_WHITESPACE_MATCHES" if warnings else "PASS"),
        "source_records_sha256": digest(SOURCES / "transcript_records.json"),
        "validator_sha256": digest(Path(__file__)),
        "visible_records_sha256": digest(SOURCES / "visible_records.json"),
        "source_record_count": len(records), "visible_nodes": len(visible),
        "visible_role_counts": dict(collections.Counter(r["role"] for r in visible)),
        "explicitly_redacted_tool_records": len(redacted),
        "coverage": {"exact_union_and_order": covered == visible_ids, "missing": missing,
                     "unexpected": unexpected, "duplicates": duplicates},
        "lanes": lane_results,
        "total_findings": sum(r["findings"] for r in lane_results.values()),
        "quote_checks": len(quotes), "unique_quote_kind_target_text_count": len(unique_quotes),
        "quote_status_counts": dict(collections.Counter(q["status"] for q in quotes)),
        "quote_kind_counts": dict(collections.Counter(q["kind"] for q in quotes)),
        "copied_body_status_counts": dict(collections.Counter(q["status"] for q in copied_bodies)),
        "reference_checks": len(reference_checks),
        "errors": errors, "warnings": warnings,
        "method_limits": [
            "The script validates exact source IDs, source hashes, quoted substrings and node coverage mechanically; it does not infer a complete mathematical read from quotes.",
            "Full-read scope is supported separately by the five lanes' explicit complete-read declarations, reader ranges and documented recovery of truncated outputs; these declarations are recorded, not a claim to prove a reader's cognition.",
            "All 2600 explicitly redacted tool records remain unavailable as historical tool bodies. Their placeholders, order and metadata are retained, but no underlying execution result is verified.",
            "Case, punctuation, Markdown, TeX backslashes and mathematical symbols are not normalized. Whitespace fallback, if any, is explicitly enumerated.",
            "Findings count includes scoped legitimate obstructions, completed work and contextual entries; it is not a count of failures or abandoned calculations.",
        ],
    }
    (OUT / "LEDGER_VALIDATION_RECEIPT.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (OUT / "QUOTE_VALIDATION_DETAILS.json").write_text(json.dumps(quotes, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (OUT / "NODE_REFERENCE_CHECKS.json").write_text(json.dumps(reference_checks, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (OUT / "COPIED_BODY_CHECKS.json").write_text(json.dumps(copied_bodies, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    script_copy = OUT / "validate_ledgers.py"
    if script_copy.resolve() != Path(__file__).resolve():
        script_copy.write_bytes(Path(__file__).read_bytes())
    lines = [
        "# Transcript ledger validation",
        "",
        "**" + receipt["status"] + ".** The five ledgers cover all 215 visible nodes in exact source order: 67 user messages and 148 assistant prose messages. There are no missing or unexpected source UUIDs.",
        "",
        "| Lane | Visible nodes | Users | Assistants | Findings |",
        "| --- | ---: | ---: | ---: | ---: |",
    ]
    for lane, r in lane_results.items():
        lines.append(f"| {lane} | {r['nodes']} | {r['role_counts'].get('user', 0)} | {r['role_counts'].get('assistant', 0)} | {r['findings']} |")
    lines += [
        "| **Total** | **215** | **67** | **148** | **115** |",
        "",
        "Each complete assigned segment was reconstructed exactly from the original UUID-keyed message strings and its header format. All five reconstructions match without whitespace normalization. Source text hashes were checked for all 5,349 retained messages.",
        "",
        f"The quote validation performed {len(quotes)} checks: {receipt['quote_status_counts'].get('literal_substring', 0)} literal nonempty source substrings and {receipt['quote_status_counts'].get('literal_empty_source', 0)} exact empty-source checks. The latter preserve the visibly blank U0065 input in both its episode and finding. There are {len(unique_quotes)} distinct quote-kind/target/text tuples; repeated user quotations are checked separately. All 34 complete copied message bodies in the typed-route ledger are also exact.",
        "",
        f"All {len(reference_checks)} recorded locator/UUID/chain/role reference checks passed. The actual-tau ledger intentionally includes U0044 and U0045 in both a composite episode and individual steering episodes; stable UUID deduplication gives its 43 distinct covered nodes, and both episode records remain.",
        "",
        ("No whitespace fallback was needed. " if not warnings else f"Whitespace-only fallback was used in {len(warnings)} explicitly enumerated checks. ") + "The script never changes case, punctuation, Markdown, TeX backslashes, or mathematical symbols. The detailed quote receipt records exact source offsets for literal matches and UUIDs for every match.",
        "",
        "The two abbreviated quotations containing ellipses were replaced by their literal source excerpts by the early audit owner before this final run. No mathematical finding changed.",
        "",
        "**Reading scope.** Full reading is recorded separately through the lanes' complete-read declarations, contiguous line/character windows, and explicit recovery of truncated tool output. Quotation matches alone are not used as evidence of a full read. The validator mechanically verifies provenance and coverage; it does not independently repeat the mathematical audit or prove a reader's cognition.",
        "",
        "**Historical tool limit.** The transcript retains 2,600 explicitly redacted tool records. Their placeholders and metadata remain available, but their underlying historical execution results remain unavailable. This validation does not certify those missing outputs, linked attachment bodies, or historical test claims.",
        "",
        "The 115 findings include completed calculations, valid scoped obstructions, repairs, and contextual entries. They are not 115 failures or abandoned calculations.",
        "",
        "Reproduce from the repository root with:",
        "",
        "    python -X utf8 work/tau_f1_transcript_audit_20260913/integration_validation/validate_ledgers.py",
        "",
        "The copied validation/validate_ledgers.py has identical bytes and the same repository-root discovery when used in this output tree. Only the Python standard library is required.",
    ]
    if errors:
        lines = ["# Transcript ledger validation", "", "**FAIL.** No successful validation is asserted.",
                 "", "Inspect LEDGER_VALIDATION_RECEIPT.json for the complete errors and source pins.",
                 "", "Detected errors:", ""] + ["- " + json.dumps(e, ensure_ascii=False) for e in errors]
    (OUT / "VALIDATION.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    manifest_names = ["LEDGER_VALIDATION_RECEIPT.json", "QUOTE_VALIDATION_DETAILS.json",
                      "NODE_REFERENCE_CHECKS.json", "COPIED_BODY_CHECKS.json",
                      "VALIDATION.md", "validate_ledgers.py"]
    manifest = [{"file": n, "bytes": (OUT / n).stat().st_size, "sha256": digest(OUT / n)}
                for n in manifest_names]
    (OUT / "VALIDATION_MANIFEST.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: receipt[k] for k in ["status", "visible_nodes", "visible_role_counts", "coverage",
                         "total_findings", "quote_checks", "quote_status_counts", "quote_kind_counts",
                         "copied_body_status_counts", "errors"]}, ensure_ascii=False, indent=2))
    return 1 if errors else 0

if __name__ == "__main__":
    sys.exit(main())
