# Add-only integration patch audit

**Pass.** All 15 sections of the delivered `INTEGRATION.patch` are structurally add-only, and all 15 reconstructed payloads exactly match their mapped raw members. There are zero byte discrepancies and no patch/raw snapshot discrepancy.

The patch is 304893 bytes, SHA-256 `2a858e01f833145783e3e482e8b90af86c60d08089d1ea01a2bb941cb65d98be`. It contains 4249 LF bytes and no CR bytes. Reconstructed payloads total 296600 bytes.

## Exact parsing and comparison

`audit_patch.py` splits only at literal LF and recognizes diff headers only at physical line start. It consumes each complete section in sequence. Every section has identical old/new target names under `workbenches/tau-holonomy-descent-control/`, `new file mode 100644`, an all-zero old index, `--- /dev/null`, and a matching `+++ b/...` header. Every old hunk range is `0,0`, every new hunk starts at line 1, every consumed payload line starts with `+`, and every declared new-line count equals the number consumed. No context, removal, binary, rename, copy, or unexplained metadata remains. Targets are unique, canonical relative paths, with no Windows case collision.

Reconstruction removes exactly the initial `+` from each payload line. The explicit missing-final-newline marker removes exactly its preceding serialization LF. No other byte, whitespace, text encoding, or line ending is changed. The omitted new count in the `reader.css` hunk `@@ -0,0 +1 @@` is interpreted as one.

| Raw member with no final newline | Patch marker line | Added file line |
|---|---:|---:|
| `INTAKE.json` | 121 | 46 |
| `VALIDATION.json` | 2204 | 82 |
| `checks/negative-controls.json` | 2313 | 32 |

Each complete payload was compared using byte equality with the raw member obtained by removing the exact workbench prefix. All 15 comparisons pass. For each payload, the audit also computes SHA-1 of `b"blob " + decimal_byte_count + b"\0" + payload`; all 15 results begin with the patch's declared new index prefix.

`PATCH_AUDIT.json` records all 15 target-to-raw mappings, section and hunk line numbers, declared and consumed hunk counts, byte counts, SHA-256 values, full computed Git blob SHA-1 values, newline markers, exact discrepancy arrays, and input stability hashes. The reconstructed files are retained under `reconstructed/` inside this audit directory.

## Supplied receipt and scope

`checks/patch-check.json` lists the same 15 unique targets and declares 15 additions, zero modifications, and zero deletions. Those structural claims agree with the audit. Its list order differs from patch section order; both sets are identical. The receipt's historical isolated-application claim was not rerun.

The patch, supplied receipt, and 15 raw members were hashed before and after the audit. All 17 inputs are unchanged. All writes were confined to this audit directory. No Git application, current-tree patching, remote operation, delivered test or script execution, reader/browser operation, or predecessor replay occurred. The parent's manifest audit and new finite suite are outside this report's coverage.

Report SHA-256: `28627f1404a9fd9912898b90034f13723e43d46689f6e38a2a1a8116b1ef6485`.

Parser SHA-256: `9f4283c41c1e32d5e735b3dd5df91488d83bd9b9b32f93fb2624d98d9bfa9463`.
