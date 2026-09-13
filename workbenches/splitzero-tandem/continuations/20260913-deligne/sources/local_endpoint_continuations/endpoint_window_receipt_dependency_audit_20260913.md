# Window-product receipt and explicit dependency audit

## Result and observed source mutation

The submitted attachment path is unresolved within this bounded explicit-reference closure. The named `FOUR_VOLUME_THRESHOLD.md` does contain the written phase-retaining product proof. Seven static input files exist and match the receipt pins.

The source changed during this audit. The initial complete checker read was 15,376 bytes / 282 lines, SHA `652f5d09ba605cf913cc2562c1e24fb304bf2428367bb800c5b06b70bade3cb0`. Its then-matching receipt was 1,006,596 bytes / 46,143 lines, SHA `c5a33e140dd501f6e89d7813abb7465081da49a5a1d84cb4351e9c5471c49fab`. That version read the attachment through `Path(sys.argv[1])` and called all 11,488 records exact. Both raw source/receipt initial bytes were not copied before mutation; initial complete source outputs, parsed-receipt observations and the initial audit reports are retained. No reconstruction is mislabeled as an original byte snapshot.

After the parent reported an intermediate 15,691-byte checker, a direct re-read captured another version: **16,488 bytes / 295 lines**, SHA **`7c9b0d3a241c14a2ed08efbab1e06c89b7d48fc6d67118299d32a364819bf395`**. Its separately captured receipt is **1,282,484 bytes / 57,634 lines**, SHA **`a901a47efe2656379747e8a4ce477501f6c73b456ba7e7dd23dd82924069a1de`**. That receipt pins this exact later checker. Each file's size and mtime was stable before/after its own snapshot read. Exact later raw bytes are preserved under `workspace:/work/endpoint_window_audit_snapshots_20260913`, with the SHA in each filename. This is an observed snapshot pair, not a claim that the live source path cannot change again.

All 295 lines of the later checker were inspected. Its entire receipt was read, parsed and scanned, including every scalar and check record; all non-check fields were inspected in full. The repetitive records were scanned structurally, without claiming a new mathematical execution. The later receipt distinguishes **11,484 exact checks and four approximate display checks**, 11,488 total, with every record marked true. These counts agree with the record kinds. No checker was imported or executed by this audit.

## Submitted paste: exact result for the later snapshot

- Checker line 24 declares optional `--attachment`; lines 249-251 place `ARGS.attachment` into the input map only when supplied.
- Checker lines 3-4 state that public receipts retain descriptive IDs and hashes rather than private attachment paths.
- Checker line 280 serializes each input as only `bytes` and `sha256`; the complete receipt construction serializes no actual argv vector or supplied path.
- Receipt lines 57580-57583 retain **16,954 bytes**, SHA **`f34647902fd4f6a913b5adae421c3df20bb1773902a797ec934750b02ed90ddb`**.
- A complete recursive scan of the later JSON found no local pathname or actual argv value. The explicit fixed inputs and the named written witnesses yield no private attachment pathname. The submitted bytes were not recovered or read here; global disk absence is not asserted.
- The newer checker also provides a deliberately false Gaussian `--negative-control` and optional portable regression mode. These are inspected code features, not newly executed results.

## Named written proof witness

The explicit `parent_four_volume_threshold` dependency resolves to:

`F:/user/Documents/Papors/Chatnotes/Zeta-Function-Foundation/agents/zenodo_workspace_publication/integration_20260913_next/FOUR_VOLUME_THRESHOLD.md`

All 239 lines were inspected. Section 3, lines 136-171, contains the same-metric, phase-retaining consecutive-window product. Its source is the local radius identity at admitted indices, with

\[
\epsilon_N^2+\phi_N^2
 =\frac{\omega_{N+1}}{\omega_N}(1-\delta_N)(\delta_{N+1}^{-1}-1),
\quad \delta_N=V_N/V_{N-1}\in(0,1],\quad N\ge q.
\]

For integers \(n\ge q\) and \(r\ge1\), retain every factor and write

\[
\prod_{j=0}^{r-1}\frac{\omega_{n+j+1}}{\omega_{n+j}}
 =\frac{\omega_{n+r}}{\omega_n},\qquad
\prod_{j=0}^{r-1}\delta_{n+j+1}=\frac{V_{n+r}}{V_n}.
\]

The numerator has one occurrence of each endpoint and two of each interior contraction:

\[
\prod_{j=0}^{r-1}(1-\delta_{n+j})(1-\delta_{n+j+1})
 =(1-\delta_n)(1-\delta_{n+r})
  \prod_{j=1}^{r-1}(1-\delta_{n+j})^2.
\]

Substitution gives exactly its displayed equation (5),

\[
\prod_{j=0}^{r-1}(\epsilon_{n+j}^2+\phi_{n+j}^2)
 =\frac{\omega_{n+r}V_n}{\omega_nV_{n+r}}
 (1-\delta_n)(1-\delta_{n+r})
 \prod_{j=1}^{r-1}(1-\delta_{n+j})^2.
\]

The empty interior product at \(r=1\) is one. No division by \(1-\delta_j\) occurs, so a unit contraction remains covered. The phase is retained throughout. The underlying local radius identity is imported from the named original Toda/transfer sources; the receipt's Gaussian checks are finite tests of that relationship, not a substitute for those written source proofs.

The same full note gives the balanced-window norm calculation in lines 63-134 and its central-window/four-volume composition in lines 173-222. It explicitly links the arithmetic NOTE at line 51; that is already a fixed checker input and its mathematical read belongs to the parent audit.

The explicit `independent_balanced_window_proof` dependency, `arithmetic_endpoint_review/BALANCED_WINDOW_PROOF.md`, was also inspected completely (102 lines). It proves BW1-BW3 in lines 5-56, then explicitly imports the separate window theorem at lines 60-66 for BW4. It provides no pathname for the submitted attachment. The three other named Markdown companions were inspected completely: the 98-line corrected PR23 note supplies the earlier sinh/Jensen criterion; the 18-line source-coordinate note specifies the original residual and determinant maps; the 260-line PR24 note supplies the confluent transfer, full phase and local positive-gap calculation. None identifies the submitted paste path.

The checker mentions a generic “companion note” at lines 38-39, and the receipt mentions a generic “written proof note” at line 57620. No filename is attached to either phrase. The named four-volume note is a written witness for the core exact product and strengthened threshold. It cannot be identified as the unique unnamed companion or as the 16,954-byte submitted attachment from this evidence. In particular, this audit does not claim that the submitted sharper-endpoint/Jensen argument was recovered verbatim.

## Complete input map and availability

The checker resolves `OUT` to its own review directory, `PUB=OUT.parents[1]`, then `E=PUB/integration_20260912e` and `NEXT=PUB/integration_20260913_next` (later checker lines 18-21). The seven fixed input paths are guarded by the optional attachment argument in the later snapshot. They retain the same bytes and hashes as the initial read, as verified by a final direct hash check. The adjacent JSON records every absolute path, the byte ranges, text-read ranges and receipt comparisons.

| Input | Bytes | Lines | SHA-256 | Read scope |
|---|---:|---:|---|---|
| verify_window_product | 16488 | 295 | `7c9b0d3a241c14a2ed08efbab1e06c89b7d48fc6d67118299d32a364819bf395` | Complete latest source snapshot text inspected; not executed |
| EXACT_VERIFICATION_RECEIPT | 1282484 | 57634 | `a901a47efe2656379747e8a4ce477501f6c73b456ba7e7dd23dd82924069a1de` | Complete latest receipt snapshot parsed/scanned; all non-check fields inspected; all check records structurally inspected |
| original_TVB_source | 45985 | 1106 | `97652a43445708c0e6d2a959f45aed8a4f2a7f73f9cd4b6cd57e67b8fedb408e` | availability, byte count and SHA-256 only; no mathematical-content reread |
| PR23_corrected_endpoint_note | 6569 | 98 | `a9a8b080b3779f82388a8bd4338ada2564ceb2410a0734bd58700f65c7789c62` | complete text inspected |
| PR23_original_source_coordinate_note | 1611 | 18 | `99f23015abce9deb0d92136826c4b719e62a912d54691ca747f890ccd28d03f0` | complete text inspected |
| PR24_full_confluent_transfer_note | 14007 | 260 | `d1046b75762e4248ded8f0b901c1ac12dc01065e4e684ca2d166b6a535425763` | complete text inspected |
| arithmetic_endpoint_complete_note | 31714 | 840 | `f776e7934f026342f48732a74f14d57470b8aae1cef76ebdee5f831bd49dedf8` | availability, byte count and SHA-256 only; mathematical read belongs to parent |
| independent_balanced_window_proof | 5891 | 102 | `a3bb84329d384071b4ac4829731e26dbe2586b719548a660bae6eefb34f5e00c` | complete text inspected |
| parent_four_volume_threshold | 7716 | 239 | `9ff55c84d74db85306e7a68c70fe7b08d8e642e8ac1a3e6137649f68e102fc3a` | complete text inspected |

## Precise remaining absence and action boundary

No actual argv vector, submitted attachment pathname, or unambiguous filename for the generic companion note occurs in either inspected checker version, either fully parsed/scanned receipt, or the five completely inspected named Markdown companions. No broader directory enumeration or filesystem search was performed. The arithmetic NOTE and TVB source were byte/hash checked only; their mathematical-content reads belong to other lanes. This establishes an unresolved reference within the named closure, not global file absence or mathematical irrelevance.

Only the two audit reports and work audit snapshots were created or updated. No source, inherited receipt, integration, PDF, GitHub or Zenodo artifact was altered. No checker, build, Lean, Lake or Elan process was started. A bounded independent companion-read delegation could not spawn because the agent service reported its thread limit; the readings were completed locally.
