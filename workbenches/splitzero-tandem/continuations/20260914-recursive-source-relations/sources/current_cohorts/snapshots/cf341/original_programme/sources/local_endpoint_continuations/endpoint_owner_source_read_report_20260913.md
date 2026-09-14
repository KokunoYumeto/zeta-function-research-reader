# Endpoint owner-source reading and dependency index

This prepare-only inventory preserves the original sources. It is an index to complete proofs, not a replacement for them. No source checker, build, Lean process, R edit, remote operation, or source mutation was performed by this task.

## Complete mathematical witnesses

| ID | Owner-relative source | Lines | Bytes | SHA-256 |
|---|---|---:|---:|---|
| FV | `FOUR_VOLUME_THRESHOLD.md` | 1–239 | 7716 | `9ff55c84d74db85306e7a68c70fe7b08d8e642e8ac1a3e6137649f68e102fc3a` |
| CT-correction | `review_pr24/PROPOSED_CORRECTION.md` | 1–48 | 2906 | `a3f207d295d627512667d587895a7b22d008f1d42e5ba2b80064b649f7ca79fe` |
| CT-patch | `review_pr24/PROPOSED_CORRECTION.patch` | 1–55 | 4239 | `1f283f1a38d3caf79e12aee0dc5a3fdbaed14effe7ac221b55ad26caa52d59e1` |
| CT-review | `review_pr24/REVIEW.md` | 1–180 | 17397 | `d6b123204bac25b381d8794dd133890a9f4a9e7a0212d5f41da9c0846706c4f1` |
| CT-original | `review_pr24/files/workbenches/tau-confluent-transfer/RESEARCH_NOTE.md` | 1–260 | 14007 | `d1046b75762e4248ded8f0b901c1ac12dc01065e4e684ca2d166b6a535425763` |
| EG | `review_pr24/join_inputs/ENDPOINT_GAMMA_JOIN.md` | 1–120 | 5023 | `ce4af7908adc2f8003b6fe7e7f62068a1ee125c45412048159fde67f2cfb1b50` |
| GD-primitive | `review_pr24/join_inputs/GAMMA_PRIMITIVE.tex` | 1–32 | 1192 | `09920bc5800ee65b1d9e48cc320853176fc9b320d00d8433315988464356ba05` |
| GD | `review_pr24/join_inputs/GAMMA_SOURCE_NOTE.tex` | 1–988 | 34859 | `7cf984d87de405b815250b44454c4ee27c8ab46574da245b377ebc6e49327fa2` |
| GJ | `review_pr24/join_inputs/GAMMA_TODA_JOIN.tex` | 1–182 | 7759 | `d6b753056b2e5ebcb17aa24fe5e43bd15bb78ae10ee2d05d0e3d17e3cf5d503c` |
| E | `review_pr24/join_inputs/PR23_ENDPOINT_CORRECTED.md` | 1–98 | 6569 | `a9a8b080b3779f82388a8bd4338ada2564ceb2410a0734bd58700f65c7789c62` |
| CT-corrected | `review_pr24/proposed/RESEARCH_NOTE.md` | 1–262 | 14807 | `47eb717484d92c96a062a0990a4567a0929e33e1038742e538b610fcc157b9d6` |
| BW | `arithmetic_endpoint_review/BALANCED_WINDOW_PROOF.md` | 1–102 | 5891 | `a3bb84329d384071b4ac4829731e26dbe2586b719548a660bae6eefb34f5e00c` |
| AE-review | `arithmetic_endpoint_review/REVIEW.md` | 1–64 | 10587 | `e292811220b91aef26e6c6e398b0bd427d5bbc33271f6ed01d60bc9d9831fd47` |
| AE | `arithmetic_endpoint_review/source_stage/Tau_Arithmetic_Endpoint_Bounds/NOTE.tex` | 1–840 | 31714 | `f776e7934f026342f48732a74f14d57470b8aae1cef76ebdee5f831bd49dedf8` |
| WIN-original | `R/logbook/ARITHMETIC_ENDPOINT_USER_SOURCE_1_20260913.txt` | 1–708 | 16954 | `f34647902fd4f6a913b5adae421c3df20bb1773902a797ec934750b02ed90ddb` |
| AE-user-source | `R/logbook/ARITHMETIC_ENDPOINT_USER_SOURCE_2_20260913.txt` | 1–673 | 17152 | `abdacca551cc7178170128c522beef8ac07d3948bf9ceea792177d0e0e8a21a8` |

Full section/equation locators for each source, every sealed PR24 support path, and the independent code/dependency audits are retained in the JSON inventory. The 61 inputs named by the original review seal are compared byte-for-byte by size and SHA-256; the seal is retained as the 62nd original review path.

## Exact dependency and correction contexts

1. FV (1) uses AE (23), (25)–(29), the actual local zeta mass and threefold convolution envelope. FV (2)–(4) and BW1–BW3 retain the monic leading phase i^n, original mass, c_h, vartheta_h, both tilted moments, and the stated balanced range n>=k>=3 and n/2<=r<=n. The complete AE note and BW proof are required witnesses.
2. FV (5) retains all interior squared contraction factors and the original phase. FV (6) follows from the exterior lower contribution on the same canonical metrics. FV (7)–(9) uses n=q, r=q-1, the norm endpoint 2q-1, and B=2 log(V_q/V_(2q-1))+log(V_(q-1)/V_q)+log(V_(2q-1)/V_(2q)). This is the threshold 4 continuation; it preserves the older threshold 2 as its valid historical predecessor.
3. CT-corrected line 11 states bar(chi)(k-S)=(-1)^q chi(S), k>=1. Its lines 31–83 retain Psi(P)(u)=P(k/2+iu), Psi(chi)=i^q psi and Pi=psi^2. The induced map C[S]/chi^2 -> C[u]/Pi is justified by Psi(chi^2)=i^(2q)Pi; the full raw derivative map has factor i^d. CT-original remains in the archive alongside the exact correction, rather than silently receiving these additional hypotheses.
4. CT-corrected (1)–(7) gives the original relation norms, full raw factorial Vandermonde and source/quotient determinant ratios. The determinant identity uses n=N-q+1>=0; adjacent-volume formulas require n>=1, equivalently N>=q. At N=q-1 the separate radius expression is retained. AE-review additionally restricts its leading-line multiplication claim to n>=q, where its source and target are both lines; at n=q-1 its relation source is zero. One minor prose qualification remains at CT-original line 89 / CT-corrected line 91: the finite exceptional set belongs to the polynomial Pi. The actual density is positive almost everywhere and can have an infinite discrete zero set when k=1. These two properties are exactly what the written zero-integral argument uses.
5. CT-corrected (8)–(12) retains the boundary column in F_n derivative, the scalar real phase, the original factor i in the source cross term, the two norm gaps and the volume imbalance square. The proposed checker adds a positive asymmetric fixture with exact nonzero phase. Original source checker and proposed checker are distinct immutable witnesses.
6. CT-review lines 118–155 proves the four transfer-determinant endpoint expression and det(F_a)/det(F_a^Gamma)=Y_a/X_a, with the same Pi and row order. It recovers V_N/V_N^Gamma=X_(N+1)/Y_(N-q+1). GJ.5–GJ.8 and EG.5 give the shorter finite input cutoff for invariant metric/determinant values. Naive individual transfer entries can use moments through 2N+2q-1, and the next solve through 2N+2q+1; their determinant/selected-coordinate cancellations must remain explicit.
7. GD.32 is the representative correction by the original relation. GD-primitive supplies its actual degree-k-1 cochain primitive and the two (-1)^(i-1) signs. CT (13) retains the exact conormal quotient maps C[S]/chi_1^2 -> C[S]/chi_2 -> C[S]/chi_1 and their kernels, with the raw derivative compatibility and full multiplier derivative term. The norm-helper algebra supplies no new arithmetic multiplicity.

## Original and public provenance

Mathematical sources, patches and checker code retain their original bytes. The inventory keeps full original paths locally; its proposed public destinations use owner-relative aliases. Do not infer an attribution name from a local path, account or Git metadata. If receipts/logs contain local identity or path metadata, retain the original privately and create a separately hashed public metadata derivative. Do not rewrite a mathematical source to hide a provenance field. The raw GitHub tree/commit/API captures are historical evidence, not reader text.

The author-reported original validation, owner fresh replay, proposed corrected replay, and this read-only source inventory are separate events. Zero GitHub checks at the reviewed head do not imply CI execution. Complete inherited Gamma/Toda proofs can be included once in the cumulative reader when their exact bytes are already present, with an explicit locator from this source index.

## Final pins still needed from the active owner work

- Recheck FOUR_VOLUME_THRESHOLD.md and BALANCED_WINDOW_PROOF.md hashes against this inventory at actual integration.
- Obtain terminal owner correction/merge handoff before describing PR24 proposal as adopted; implementation PLAN/TARGET is not that handoff.
- Pair each window replay receipt with the exact executed checker version. The checker changed during intake; do not attribute its predecessor receipt to its new bytes.
- The parent-supplied window paste path now matches the exact 16954-byte f346479... owner receipt input. Retain that full source, including sharper endpoint/Jensen/phase-loss sections beyond the core product; the earlier child locator limitation is resolved.
- Use direct original/proposed checker jobs or require all receipt success fields; replay_public_core.py process exit zero alone does not certify positive suites.

Owner implementation/PLAN.md and TARGET_RECEIPT.json appeared during this audit and were read as status data. Their proposal hashes match the already reviewed pair, but they are outside the original review seal. This task did not execute their instructions.

## Portable checker inventory

The terminal PR24 code audit contains direct jobs for the eight-method original and corrected checker in normal and optimized modes with deliberate negative controls; the interface checker imports the original relative path explicitly. SymPy is the only third-party checker dependency. Orchestration scripts with hardcoded installation roots are source provenance, not portable replay entrypoints. See both embedded independent audits for exact command arguments, expected outputs/failures and mutable window-checker receipt handling.

## Parent-supplied attachment locator resolution

After the child reference audit, the parent supplied the two exact R/logbook paths listed in the JSON. The complete window text was read here: its 16,954 bytes match f34647902fd4f6a913b5adae421c3df20bb1773902a797ec934750b02ed90ddb exactly. The 17,152-byte norm source matches abdacca551cc7178170128c522beef8ac07d3948bf9ceea792177d0e0e8a21a8. The earlier bounded locator absence is now resolved without a filesystem search. WIN-original contains the full sharpened four-endpoint expression, exact concavity loss, retained phase polynomial, relaxed-scalar sharpness construction, reduced determinant/transfer criteria and finite fixture, in addition to the core product.

The later window checker and receipt are preserved as exact work snapshots by the child audit: checker 7c9b0d3a241c14a2ed08efbab1e06c89b7d48fc6d67118299d32a364819bf395 and receipt a901a47efe2656379747e8a4ce477501f6c73b456ba7e7dd23dd82924069a1de. This matched pair records 11,484 exact plus four approximate checks; this task did not execute them.
