# Original-degree deficit receiving precision

Scope: complete ODD1–14 read; HMR36–45 and TWA1–6, TWA14–15 use sites read. No unchanged original body was re-audited or edited. No PDF build or Lean run.

Read source: `degree_preserving_deficit.tex`, SHA256 `dc0aeda684190d00be5828944784e86113144d7f3ae058cdec6a4a5389ea7d78`.

`ODD_SIGNED_RECEIVING.tex` proves the additional degree-specific finite bound and the sharper signed lower constant in full. ORP1–9 are suggested local identifiers; the receiving owner should assign its own noncolliding labels.

## Exact use sites

- HMR44: retain the prior DMR rate as provenance and replace the current evaluated conclusion by ORP1–7. For all four original degrees the rate is O(log k/k + (k log k/q)^eta); the simple-zero case remains O((log k/k)^(5/7)). For multiplicity at least two, record the signed q log k constants from ORP7, rather than only the symmetric absolute constant in ODD12.
- HMR43 and HMR45: retain the exact four deficits and full kernel/boundary split; add the evaluated asymmetric interval from ORP3–4 and its translated full Gamma interval ORP8.
- TWA15: retain the exact Xi interval. Add the evaluated consequence ORP9 and the multiplicity-specific ORP7 conclusion. Its proof is the same original Schur quotient; no new receiver is required.
- TWA23: replace an unevaluated arithmetic allowance by ORP9 where a fully explicit bound is being claimed, while keeping the complete M_k − R_k^sigma expression.
- TWA24 and TWA30: use R_k^0 − R_k^sigma + ORP9, equivalently −T_k + ORP9 on a class where that signed determinant is defined. The q log k estimate belongs to Delta^Gamma + T, not to Delta^Gamma by itself.
- The actual HC residual equation: use the second line of ORP8, preserving D_h, q and the independent nonnegative residual. A bound for its Gamma part must still come from the actual Gamma calculation.

## Edge cases and precision

1. All new finite estimates require k >= 3, as does ODD; k = 1,2 retain their original finite source calculations.
2. The m >= 2 q log k constants cannot be extended to m = 1 by reusing the cubic-degree estimate.
3. TWA6 concerns adjacent monic deficit differences and retains degrees q−2 and 2q−2. ODD's aggregate deficit bound supplies no new smaller exact value for those differences; avoid replacing the existing exact minima by a weaker allowance.
4. The strongest lower signed constant obtained from ODD7 is −(64m+245), whereas the upper is 128m+490. Using the common 2Xi_{2q} estimate loses this asymmetry.
5. The finite evaluated bounds are weaker than a known exact Xi sum. Preserve both presentations with their explicit inequality; do not claim the evaluated sum tightens an already known exact deficit.
6. Kernel and boundary rank-zero cases retain empty determinant one. The existing full Schur/frame proof covers them and the same signed argument applies.

## Installed successor review — 2026-09-14

Accepted the newly installed ODD mathematical spans in `root/signed_receiving_successor`. This review read the entire `spans/HMR44_REPLACEMENT.tex`, the installed TWA15/TWA15a changes, R66d1a and R66ex3a with their exact input definitions, and the final HMR45 receiving paragraph. It did not review unchanged bodies or certify the independent GSR/JQR proof; the short TWA32 statement was read only to check HMR45's description of its current receiving bound.

Reviewed pins:

- `spans/HMR44_REPLACEMENT.tex`: `26d474e9e72fb87b27791f8a04fcd235fc73482c7dda6699ca0e7cdd93c7bacf`.
- `HMR.tex`: `0f8ffe053fa8e6b7c18993ad0d38874eaaf8ace12b2d8701ed4249d554254290`.
- `TWA.tex`: `cc96bf2b591a710cd5e7889f82063079d3f866bb1a86dfa6447518d30854f5ac`.
- `R63_R66.tex`: `ee712ad9bf458d6e81513508b5b7e7581ed51ff85aa69377a94473865f3a1083`.

The installed degree-specific majorant has the exact `(N+1)/q` and `2MN/(kq)` factors and the unchanged cutoff remainder. It equals ORP1 with `T_k^{deg}` denoting the original ODD scalar. Its common majorant and both cutoff branches are correct, including equality at z=1. All four endpoint dimensions, the k>=3 domain and the m=1 versus m>=2 distinction remain explicit.

The lower and upper signed constants are respectively `-(64m+245)` and `128m+490`. R66ex3a correctly adds the two allowances to give width constant `192m_h+735`. The monotone interval inclusions have the correct directions and preserve every known exact deficit. The use of `p_h,m_h` in R66 avoids confusing the original tail exponent and quartet multiplicity with the independent finite-series degree p. No mathematical lexical conflict was found in the requested spans.

HMR45 correctly retains the full reference correction: exact `-T + [-d0-d1,d2+d3]` is contained in `[-T-Dminus,-T+Dplus]`, and replacing the exact reference value by its own enclosure yields `[-Dminus-Tupper,Dplus-Tlower]`. The q log k estimate is applied to `Delta^Gamma+T=delta^sigma`. No sign or asymptotic endpoint is inserted for T.

Minor wording suggestion only: the inherited sentence “where T is its four explicit positive determinants” should read “where T is the signed sum of logarithms of its four explicit positive determinants.” The surrounding formulas already use the correct scalar, so this does not affect mathematical acceptance of the new ODD spans.

### Final delta acceptance

Read and accepted the final additional formulas and their proofs at TWA15a, TWA23a and TWA24a. The evaluated bounds are exactly `max{-qEplus,-Dminus}` and `min{qEminus,Dplus}`. The exact interval is correctly contained in this evaluated interval. Adding the complete fixed-Gamma functional gives TWA23a; adding the original signed difference of Gamma residuals gives TWA24a. The latter applies its q log k estimate to `Delta^Gamma-(R0-Rsigma)=delta^sigma`, equivalently `Delta^Gamma+T` on the stated tensor class. All signs and inclusion directions are correct.

The suggested HMR45 wording correction is present and preserves the four original signs. Final accepted file pins for these changed spans:

- `TWA.tex`: `7e23d48f9f251bd0a065547226f76a21751a25a8bab87a237b5d1028cdff0b90`.
- `HMR.tex`: `e645576fff6e7c32af8bd02ee36a46972f486c369eab009444c98fe437aef6b2`.

The earlier R63/R66 and HMR44-span acceptance remains unchanged. This final pass checked only the specified additional delta and the wording repair.

## Bounded joint-Schur dictionary — 2026-09-14

Read the incoming NOTE's exact two-reference multiplication and raw-jet definitions, joint full-jet section, signed-return section and finite-enclosure/arithmetic-return section. Compared only those constructions against GCR21–27 and GSR3–8/GSR20. No full-package review, mixed-word rank review, closed free-boundary-determinant review or PDF build was performed.

Incoming NOTE SHA256: `8fad99f7931cfe16f1fbde79ed76f2cd29f866f4522142e508a1cb26a5eaa7cb`.

The comparison is proved in full in `JOINT_SCHUR_DICTIONARY.tex`, SHA256 `8d27adb40ae68fc9dac5463f255de8a79d93d83160f0ffdae139791cb5ad724f`:

- Raw jet = diag(r!) times divided jet; both full Leibniz multiplication matrices and the exact remainder observation are conjugated by the displayed invertible map.
- NOTE's X and Y are mapped by their actual positive metric square roots to GCR24's Hermitian factors. Their product is GCR23's full mixed 2l determinant, including the positive cross term.
- NOTE's log gain d and positive quantity beta satisfy `log d_GCR = d_note − beta_note = 2log|det U_f| − log D_GSR + log R_GSR`. Thus its signed return is exactly `R0−Rsigma = −T`.
- The finite trace certificate has the correct sign order and converges at fixed input in the two stated metrics. The full tail inequality is proved in the dictionary.
- The accepted exact GSR low endpoints give a stricter certificate with only the two high trace remainders; JOD9–10 retains every original low determinant and full multiplication-unit factor.
- JOD11 propagates the actual asymmetric arithmetic bound through the original Gamma and HC residual equations, including the nonnegative HC residual and unchanged q. The m=1 branch retains its actual 5/7 rate; the multiple-zero q log k constants are not extended to it.

The note's reuse of d_N for a logarithm, where GCR uses d_N for a positive determinant, requires the explicit dictionary. It is accounted for here without identifying those two scalar definitions.

### Joint receiver final delta acceptance

Accepted the requested new spans of `root/joint_schur_intake/SIGNED_RETURN_RECEIVER.tex`, SHA256 `2a22fa6d6f7bc7f861e8e142d2027bcd1391e013a01ea775b24a3bf0b156969d`: JSR24a–24b, their actual arithmetic use in JSR25 and JSR28, and the finite tolerance choice and width conclusion JSR27. JSR20–23 definitions were consulted only to verify the exact deficit and trace allowance symbols used in those new spans. The rest of the file was not re-reviewed.

- JSR24a is exactly JOD9–10 with `det M_f=det U_f`. Its four-unit logarithm coefficient, both source determinant signs, `+log rchi`, `−2l log s_k`, and both high trace signs are correct. The interval is contained in the note's original interval and its width is the sum of only the two high endpoint widths.
- JSR24b preserves the original coefficient Gram: `P_d^* H_d P_d = diag(gamma)` gives the displayed inverse-congruence order. Multiplication F_q has domain P_q and codomain P_{q+l}; its full chi coefficient column gives exactly the original positive integral ratio rchi, with no missing mass or factorial.
- JSR25 correctly uses the sharper trace interval and the separate original negative/positive arithmetic deficit sums. Its second line uses the proved explicit Dminus/Dplus outer bounds. JSR28 subtracts the complete HC threshold with the correct signs and intersects the lower endpoint with zero.
- JSR27 chooses an admitted order for each of exactly four matrices, Z and Y at the two high endpoints. Each contributes at most 1/4, so total trace width is at most one. Existence follows from the already proved finite-dimensional positive spectral tail convergence. Since q log k tends to infinity, this bounded trace width disappears on that scale; the exact Dminus and Dplus limits add to 192m+735. Thus the exact-deficit interval has the stated limsup bound, and the explicit-majorant interval has the stated limit. No centre value or tensor-uniform order bound is inferred.

No corrections are required. No original files were edited and no build was run in this delta check.
