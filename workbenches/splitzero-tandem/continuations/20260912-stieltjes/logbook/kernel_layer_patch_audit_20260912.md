# Kernel-layer delivery: independent patch and provenance audit

The complete `INTEGRATION.patch` (1,059 lines), `MANIFEST.sha256.json`, `PATCH_RECEIPT.json`, `SOURCE_REVIEW_RECEIPT.json`, `HANDOFF.md`, and sibling `LOCAL_STAGING_PROVENANCE.json` were read. All 31 vendor-manifest entries verified against freshly read byte lengths and SHA256 hashes. The manifest covers every included file except itself. All 32 archive members, including the manifest, verified against the original ZIP, the staging provenance, and the staged bytes. The staged delivery remained byte-identical throughout the audit.

The strict patch parser reconstructed seven additions inside the new isolated directory `work/kernel_layer_patch_audit_20260912/reconstructed`. Every resulting file is byte-identical to its independently included archive member. The parser accepts only the observed single-hunk, add-only format, checks every declared line count, requires mode `100644`, rejects unsafe or unexpected paths, and retains original LF bytes. No Git command, source checker, Lean process, or live-repository patch application was executed by this audit.

## Exact source editions

The current delivery is:

- Original ZIP: `corpus:Chatnotes\CHat translates and clean\Noether Multilingual\Tau_Kernel_Layer_Integration_2026-09-12 (1).zip`.
- ZIP size: 69,914 bytes; SHA256 `ebd927c8a9afa90600f5320bd4189ecb48085889835205057b1bfafdb68d23d2`.
- Staged root: `package:\sources\web_kernel_layer_delivery\Tau_Kernel_Layer_Integration`.
- Manifest SHA256: `3f87e01b421ae8f42a115b2d84afb0c08407bfbf0b343a212af73e79ae201a91`.
- Patch size: 48,527 bytes; SHA256 `141db775d2c0ecb81822909af247a611a0a941301016db06738c15239093ffa0`.

The `a753...` archive named in `SOURCE_REVIEW_RECEIPT.json` is the earlier PR14 input archive. It is a different object from the current `ebd927...` delivery. Fresh local hashing resolved it to `Tau_Coherent_Interpolation_Control_2026-09-12.zip`, 408,883 bytes, SHA256 `a753df8341d05b2fccb6487b1dabc0044153a6c1abcf35092504aadb95c51d26`.

## Complete patch map

Every target below has the prefix `workbenches/tau-kernel-layer-integration/`. The target basename maps to the identically named file in the staged root above. The JSON receipt records the complete absolute included and reconstructed paths, bytes, SHA256 hashes, and Git blob hashes.

| Added file | Hunk lines | Bytes | SHA256 |
|---|---:|---:|---|
| `README.md` | 17 | 1,303 | `73093bc353f7f19c3e21143b287619fd24d290d48c2d30d936bac07437acbb2b` |
| `RESEARCH_NOTE.md` | 361 | 18,984 | `5b8b596d57f820c3ba9c1894967a8ac18a90f6462971095ab59ac31e1c0ad3ae` |
| `HANDOFF.md` | 31 | 3,807 | `b435ed45aebd61b8c92f9e58ac3cb606404b490022aa958cfef2bebdd56db154` |
| `check_kernel_layer.py` | 327 | 14,571 | `bc603e2ebda6104e10e5b48b0de56a7430a0c3276aa2023b2603040eee1cc410` |
| `SOURCE_REVIEW_RECEIPT.json` | 46 | 1,452 | `33af4eca28953273251b802fda961edbf4302e1a206d3ba6081efb11aa0471f8` |
| `KERNEL_LAYER_RECEIPT.json` | 44 | 1,304 | `2c95ad1e07d19d9b211b53aaa94cf6f080d70f421e21f3909dc610462d6d7316` |
| `CROSSCHECK_RECEIPT.json` | 198 | 4,296 | `f1114abcd90042d5d7332442fa2073f0a1998fe2b79fa062455925ced5f3fb52` |

There are zero modifications, zero deletions, zero renames, and seven distinct target paths. The vendor `PATCH_RECEIPT.json` counts agree with this independent reconstruction. The local audit establishes exact output bytes and patch structure; it does not establish applicability against a particular live repository checkout.

The seven-file patch omits `index.html`, `NOTE.tex`, and `INTEGRATION.patch`, although its added README directs readers to these files. It also omits the mode logs that the README says are included. These files are present in the complete ZIP and are covered by the verified manifest. Thus applying only the patch would leave that workbench's reader navigation and log claims incomplete. A publication integrator should carry the complete required assets or revise those README references in its own integration scope; the preserved delivery bytes were not changed here.

## Exact already-staged PR14 dependency

The earlier checker exists at:

`package:\sources\web_pr14_delivery\Tau_Coherent_Interpolation_Control\check_interpolation_control.py`

Its size is 11,062 bytes; SHA256 is `4d7c78bd36037ee5dd7d69ade773c9860b979e6bb39a2e556df339666033773f`; computed Git blob SHA1 is `d7d6d87c3e6bb51898b082985433c3afcceb7655`.

The sibling `RESEARCH_NOTE.md` has size 28,460 bytes; SHA256 `d3e808adea130c3e967b84a82def531e2984ce2c7a593bbc31cddf4504124ad0`; Git blob SHA1 `4ec40c15397128552bc276ec903fe59c89657d4e`.

Both computed Git blob hashes exactly match the current layer delivery's source receipt and PR14's staged `GITHUB_DELIVERY.json`. That local metadata records head `3bff1b2bd87dfa2592f65c5ccc231f6ee9541dfc`. The independent locator subagent also checked all 30 upstream staged files against their staging provenance. No current remote commit claim is inferred from these local hashes; no remote request was needed to resolve the exact checker bytes for the parent's replay.

## Formal versus written scope carried by the delivery

`HANDOFF.md:5` reports PR15 head `21970bbf4760d0bbca512a4a7996a2e38f968947` and explicitly says the supplement does not expand its existing five-module receipt. `RESEARCH_NOTE.md:9` identifies the reported formal scope as support-changing, relation-layer, finite-Krylov, and rank-two interfaces; it excludes theta analytics, all-degree orthogonal-polynomial construction, and the new tensor-kernel calculations from that receipt. `HANDOFF.md:23` locates the written statements and proofs at equations (9)–(28) and retains the concrete theta-range, test-space integration-by-parts, and all-degree arithmetic-moment instantiations. `README.md:17` makes no new Lean-execution or arithmetic-interval claim.

These are precisely located claims in byte-verified source documents. This patch audit neither inspected PR15's actual formal sources nor revalidated its remote head nor ran Lean. The parent owns that separate audit. Likewise the vendor's upstream nineteen-test, current eighteen-test, and twenty-four-cross-comparison receipts are carried as source records here; the parent independently replays the checkers. None of these numbers is a count of mathematical theorems.

## Reproduction and audit limits

Run these scripts in order with local Python:

```powershell
& 'runtime:research-python\python.exe' 'workspace:\work\kernel_layer_patch_audit_20260912\audit_patch_bytes.py'
& 'runtime:research-python\python.exe' 'workspace:\work\kernel_layer_patch_audit_20260912\audit_upstream_reference.py'
```

Both completed with exit status zero. On repetition, the first script verifies existing reconstruction bytes and refuses to overwrite a differing file. Only audit-owned output files are written. An initial development run of the upstream-reference helper encountered the earlier provenance file's different field names; the helper was corrected to the observed schema and rerun successfully. That was an audit-helper schema correction, with no source-byte or mathematical failure.

The authoritative machine record is [kernel_layer_patch_audit_20260912.json](workspace:/work/kernel_layer_patch_audit_20260912.json). It gives full per-file evidence and all negative scope declarations. This audit certifies byte integrity, preserved staging, and exact patch mapping only.
