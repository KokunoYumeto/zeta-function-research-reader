"""Read-only audit of the delivered add-only unified diff; never applies it.

The accepted grammar is the actual unquoted-ASCII-path, regular-new-file,
LF-delimited Git unified-diff format of this input. Unknown metadata, quoted
paths, context/removal lines, binary sections, and noncontiguous hunks fail
closed. This is deliberately not a general patch applier. Payloads are bytes:
no Unicode, line-ending, whitespace, or terminal-newline normalization occurs.
All generated artifacts stay next to this script, under patch_audit/.
"""

from __future__ import annotations

from datetime import datetime, timezone
from hashlib import sha1, sha256
from pathlib import Path, PurePosixPath
import difflib
import json
import re
import sys


RAW = Path("workspace:/output/split_zero_rh_tandem_2026-09-12/sources/web_holonomy_descent_delivery/Tau_Holonomy_Descent_Control")
OUT = Path(__file__).resolve().parent
PREFIX = "workbenches/tau-holonomy-descent-control/"
PATCH = RAW / "INTEGRATION.patch"
RECEIPT = RAW / "checks/patch-check.json"
EXPECTED_COUNT = 15

DIFF = re.compile(rb"diff --git a/([^\s]+) b/([^\s]+)")
MODE = re.compile(rb"new file mode (100644|100755)")
INDEX = re.compile(rb"index (0{7,40})\.\.([0-9a-f]{7,40})")
HUNK = re.compile(rb"@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@(?: .*)?")
NO_NEWLINE = b"\\ No newline at end of file"


class AuditError(Exception):
    def __init__(self, message: str, line: int | None = None):
        self.message = message
        self.line = line
        super().__init__(message)


def require(condition: bool, message: str, line: int | None = None) -> None:
    if not condition:
        raise AuditError(message, line)


def byte_lines(data: bytes) -> list[bytes]:
    """Split only at literal LF, retaining it; bytes.splitlines is unsuitable."""
    if not data:
        return []
    parts = data.split(b"\n")
    lines = [part + b"\n" for part in parts[:-1]]
    if parts[-1]:
        lines.append(parts[-1])
    return lines


def control(line: bytes, line_number: int) -> bytes:
    require(line.endswith(b"\n"), "Patch control line lacks its physical LF terminator", line_number)
    return line[:-1]


def safe_relative(target: str) -> str:
    require(target.startswith(PREFIX), "Target is outside the exact permitted patch prefix")
    relative = target[len(PREFIX):]
    require(bool(relative), "Target has no raw member suffix")
    require("\\" not in target and ":" not in target and '"' not in target, "Unsupported or unsafe path syntax")
    require(all(ord(c) >= 32 and ord(c) < 127 for c in target), "Non-ASCII/control path syntax is unsupported")
    path = PurePosixPath(relative)
    require(not path.is_absolute(), "Absolute target suffix")
    require(all(part not in ("", ".", "..") for part in relative.split("/")), "Noncanonical target suffix")
    require(path.as_posix() == relative, "Target suffix is not canonical POSIX syntax")
    return relative


def confined(root: Path, relative: str) -> Path:
    resolved_root = root.resolve()
    candidate = (root / relative).resolve()
    require(candidate.is_relative_to(resolved_root), "Resolved member escapes intended directory")
    return candidate


def digest(data: bytes) -> dict:
    return {"bytes": len(data), "sha256": sha256(data).hexdigest()}


def exact_discrepancies(payload: bytes, actual: bytes) -> list[dict]:
    """Return a complete byte edit description, with no truncated differences."""
    if payload == actual:
        return []
    changes = []
    for operation, a0, a1, b0, b1 in difflib.SequenceMatcher(None, payload, actual, autojunk=False).get_opcodes():
        if operation != "equal":
            changes.append({
                "operation_from_reconstruction_to_raw": operation,
                "reconstructed_byte_range_half_open": [a0, a1],
                "raw_byte_range_half_open": [b0, b1],
                "reconstructed_hex": payload[a0:a1].hex(),
                "raw_hex": actual[b0:b1].hex(),
            })
    return changes


def parse_section(lines: list[bytes], first_line: int) -> tuple[dict, bytes]:
    """A section boundary is recognized only at physical line start."""
    require(len(lines) >= 6, "Section is too short for the accepted new-file grammar", first_line)
    header = DIFF.fullmatch(control(lines[0], first_line))
    require(header is not None, "Invalid or unsupported diff header", first_line)
    left, right = (part.decode("ascii") for part in header.groups())
    require(left == right, "Diff header paths differ", first_line)
    relative = safe_relative(right)
    mode = MODE.fullmatch(control(lines[1], first_line + 1))
    require(mode is not None, "Missing regular new-file mode or unexpected metadata", first_line + 1)
    index = INDEX.fullmatch(control(lines[2], first_line + 2))
    require(index is not None, "Index does not advertise an all-zero old object and a SHA-1 new object", first_line + 2)
    old_hash, new_hash_prefix = (part.decode("ascii") for part in index.groups())
    require(control(lines[3], first_line + 3) == b"--- /dev/null", "Old-file header is not /dev/null", first_line + 3)
    require(control(lines[4], first_line + 4) == b"+++ b/" + right.encode("ascii"), "New-file header differs from diff target", first_line + 4)

    cursor = 5
    chunks: list[bytes] = []
    hunks = []
    newline_markers = []
    total_added = 0
    terminal_no_newline = False
    while cursor < len(lines):
        line_number = first_line + cursor
        require(not terminal_no_newline, "More hunk data follows a no-final-newline marker", line_number)
        match = HUNK.fullmatch(control(lines[cursor], line_number))
        require(match is not None, "Expected a hunk header; unknown metadata or trailing data present", line_number)
        old_start = int(match.group(1))
        old_count = int(match.group(2)) if match.group(2) is not None else 1
        new_start = int(match.group(3))
        new_count = int(match.group(4)) if match.group(4) is not None else 1
        require(old_start == 0 and old_count == 0, "Hunk is not an insertion into an empty old file", line_number)
        require(new_count > 0, "Zero-length hunks are outside this nonempty-addition grammar", line_number)
        require(new_start == total_added + 1, "New-file hunk coordinate is not contiguous", line_number)
        hunk_record = {"header_line": line_number, "old_start": old_start, "old_count": old_count, "new_start": new_start, "new_count": new_count, "added_lines_consumed": 0, "context_lines": 0, "removed_lines": 0}
        cursor += 1
        for offset in range(new_count):
            current_line = first_line + cursor
            require(cursor < len(lines), "Hunk ended before its declared added-line count", current_line)
            raw = lines[cursor]
            require(raw.startswith(b"+"), "Non-addition payload line in add-only hunk", current_line)
            require(raw.endswith(b"\n"), "Payload line lacks physical LF and explicit newline-marker encoding", current_line)
            chunks.append(raw[1:])
            total_added += 1
            hunk_record["added_lines_consumed"] += 1
            cursor += 1
            if cursor < len(lines) and lines[cursor].startswith(b"\\"):
                marker_line = first_line + cursor
                require(control(lines[cursor], marker_line) == NO_NEWLINE, "Unknown backslash control line", marker_line)
                require(offset == new_count - 1, "No-final-newline marker precedes remaining declared payload", marker_line)
                # Remove the LF inserted by patch serialization, and nothing else.
                chunks[-1] = chunks[-1][:-1]
                newline_markers.append({"patch_line": marker_line, "new_file_line": total_added, "removed_hex": "0a"})
                terminal_no_newline = True
                cursor += 1
                require(cursor == len(lines), "No-final-newline marker is not terminal in section", marker_line)
        hunks.append(hunk_record)

    require(bool(hunks), "No payload hunk found", first_line)
    payload = b"".join(chunks)
    blob_sha1 = sha1(b"blob " + str(len(payload)).encode("ascii") + b"\0" + payload).hexdigest()
    row = {
        "patch_target": right,
        "raw_relative_path": relative,
        "patch_lines_inclusive": [first_line, first_line + len(lines) - 1],
        "new_file_mode": mode.group(1).decode("ascii"),
        "old_index": old_hash,
        "new_index_prefix": new_hash_prefix,
        "old_file_header": "/dev/null",
        "new_file_header": "b/" + right,
        "add_only_structure_valid": True,
        "hunks": hunks,
        "total_added_lines": total_added,
        "no_final_newline_markers": newline_markers,
        "payload_ends_with_lf": payload.endswith(b"\n"),
        "reconstructed": digest(payload),
        "reconstructed_git_blob_sha1": blob_sha1,
        "new_index_prefix_matches_reconstructed_blob": blob_sha1.startswith(new_hash_prefix),
    }
    return row, payload


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    before: dict[str, dict] = {}

    def read_input(path: Path) -> bytes:
        data = path.read_bytes()
        before[path.as_posix()] = digest(data)
        return data

    patch_bytes = read_input(PATCH)
    receipt_bytes = read_input(RECEIPT)
    report = {
        "format_version": 1,
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "status": "fail",
        "raw_root": RAW.as_posix(),
        "output_root": OUT.as_posix(),
        "patch": {"path": PATCH.as_posix(), **digest(patch_bytes), "lf_count": patch_bytes.count(b"\n"), "cr_count": patch_bytes.count(b"\r"), "ends_with_lf": patch_bytes.endswith(b"\n")},
        "supplied_receipt": {"path": RECEIPT.as_posix(), **digest(receipt_bytes)},
        "parser": {"path": Path(__file__).resolve().as_posix(), **digest(Path(__file__).read_bytes()), "method": "Strict anchored unified-diff state machine; exact byte reconstruction; no patch application", "newline_policy": "Split only on literal LF; retain all payload bytes; an explicit no-newline marker removes exactly the prior serialization LF", "scope": "15 unquoted-ASCII-path regular-file additions; unfamiliar grammar fails closed"},
        "rows": [],
        "errors": [],
        "operations": {"git_apply": False, "current_tree_patch": False, "remote": False, "delivered_script_execution": False, "tests": False, "browser_or_reader": False, "predecessor_replay": False, "raw_writes": False},
    }
    receipt = json.loads(receipt_bytes)
    report["supplied_receipt"]["claims"] = receipt
    lines = byte_lines(patch_bytes)
    starts = [index for index, line in enumerate(lines) if line.startswith(b"diff --git ")]
    if not starts or starts[0] != 0:
        report["errors"].append({"kind": "patch_structure", "message": "Patch has no initial line-anchored diff header or has a preamble"})
    if len(starts) != EXPECTED_COUNT:
        report["errors"].append({"kind": "section_count", "expected": EXPECTED_COUNT, "actual": len(starts)})
    targets = []
    for number, start in enumerate(starts, 1):
        end = starts[number] if number < len(starts) else len(lines)
        try:
            row, payload = parse_section(lines[start:end], start + 1)
            row["section_number"] = number
            targets.append(row["patch_target"])
            destination = confined(OUT / "reconstructed", row["raw_relative_path"])
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(payload)
            row["reconstructed"]["path"] = destination.as_posix()
            require(destination.read_bytes() == payload, "Saved reconstruction differs from parser payload")
            raw_member = confined(RAW, row["raw_relative_path"])
            row["raw_member_path"] = raw_member.as_posix()
            require(raw_member.is_file(), "Mapped raw member is missing or not a regular file")
            actual = read_input(raw_member)
            row["raw"] = digest(actual)
            row["raw"]["ends_with_lf"] = actual.endswith(b"\n")
            row["exact_bytes_match"] = payload == actual
            row["exact_discrepancies"] = exact_discrepancies(payload, actual)
            report["rows"].append(row)
            if not row["exact_bytes_match"]:
                report["errors"].append({"kind": "payload_mismatch", "section": number, "target": row["patch_target"], "exact_discrepancies": row["exact_discrepancies"]})
            if not row["new_index_prefix_matches_reconstructed_blob"]:
                report["errors"].append({"kind": "index_prefix_mismatch", "section": number, "target": row["patch_target"], "declared_prefix": row["new_index_prefix"], "computed_git_blob_sha1": row["reconstructed_git_blob_sha1"]})
        except (AuditError, UnicodeDecodeError, OSError) as error:
            report["errors"].append({"kind": "section_error", "section": number, "patch_line": getattr(error, "line", start + 1), "message": str(error)})

    claims = receipt.get("isolated_application_verified")
    valid_claims = isinstance(claims, list) and all(isinstance(path, str) for path in claims)
    claims = claims if valid_claims else []
    receipt_comparison = {
        "declared_status_is_pass": receipt.get("status") == "pass",
        "declared_added_files_is_15": type(receipt.get("added_files")) is int and receipt.get("added_files") == EXPECTED_COUNT,
        "declared_modified_files_is_zero": type(receipt.get("modified_files")) is int and receipt.get("modified_files") == 0,
        "declared_deleted_files_is_zero": type(receipt.get("deleted_files")) is int and receipt.get("deleted_files") == 0,
        "declared_path_list_valid": valid_claims,
        "declared_path_count": len(claims),
        "parsed_path_count": len(targets),
        "declared_path_list_has_no_duplicates": len(set(claims)) == len(claims),
        "parsed_path_list_has_no_duplicates": len(set(targets)) == len(targets),
        "parsed_paths_have_no_windows_case_collisions": len({path.casefold() for path in targets}) == len(targets),
        "only_in_receipt": sorted(set(claims) - set(targets)),
        "only_in_patch": sorted(set(targets) - set(claims)),
        "same_order": claims == targets,
        "comparison_policy": "Set equality with uniqueness and cardinality; receipt order is not patch application order",
        "historical_isolated_application_rerun": False,
    }
    report["receipt_comparison"] = receipt_comparison
    required_flags = [key for key, value in receipt_comparison.items() if isinstance(value, bool) and key not in ("same_order", "historical_isolated_application_rerun")]
    if any(not receipt_comparison[key] for key in required_flags) or len(claims) != EXPECTED_COUNT or receipt_comparison["only_in_receipt"] or receipt_comparison["only_in_patch"]:
        report["errors"].append({"kind": "receipt_claim_mismatch", "details": receipt_comparison})

    stability = []
    for filename, previous in before.items():
        path = Path(filename)
        current = digest(path.read_bytes())
        same = current == previous
        stability.append({"path": filename, "before": previous, "after": current, "unchanged": same})
        if not same:
            report["errors"].append({"kind": "input_changed_during_audit", "path": filename, "before": previous, "after": current})
    report["input_stability"] = stability
    report["summary"] = {
        "line_anchored_diff_sections": len(starts),
        "successfully_reconstructed_sections": len(report["rows"]),
        "add_only_sections": sum(row["add_only_structure_valid"] for row in report["rows"]),
        "exact_payload_matches": sum(row["exact_bytes_match"] for row in report["rows"]),
        "matching_git_blob_index_prefixes": sum(row["new_index_prefix_matches_reconstructed_blob"] for row in report["rows"]),
        "payload_bytes_total": sum(row["reconstructed"]["bytes"] for row in report["rows"]),
        "explicit_no_final_newline_markers": sum(len(row["no_final_newline_markers"]) for row in report["rows"]),
        "inputs_rechecked_for_stability": len(stability),
        "all_inputs_unchanged": all(row["unchanged"] for row in stability),
        "error_count": len(report["errors"]),
    }
    report["status"] = "pass" if not report["errors"] and len(report["rows"]) == EXPECTED_COUNT else "fail"
    report_path = OUT / "PATCH_AUDIT.json"
    report_path.write_bytes((json.dumps(report, indent=2, ensure_ascii=False) + "\n").encode("utf-8"))
    print(json.dumps({"status": report["status"], "summary": report["summary"], "report": report_path.as_posix(), "report_sha256": sha256(report_path.read_bytes()).hexdigest(), "errors": report["errors"]}, ensure_ascii=False))
    return 0 if report["status"] == "pass" else 1


if __name__ == "__main__":
    sys.exit(main())
