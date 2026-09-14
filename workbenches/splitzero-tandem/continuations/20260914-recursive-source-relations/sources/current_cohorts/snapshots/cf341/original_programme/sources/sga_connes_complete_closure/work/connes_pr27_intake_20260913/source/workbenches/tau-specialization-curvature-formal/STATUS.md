# Verified specialization, curvature, and Laplacian checkpoint

## Observed execution

GitHub Actions run [34735210715](https://github.com/KokunoYumeto/zeta-function-research-reader/actions/runs/34735210715), job `103665300994`, succeeded for source commit `25960903723954d6118b1aa76a817cb6a7f452f0`. The decoded job log was read after completion. The checkpoint completed on 13 September 2026 at approximately 03:23 UTC.

All five new modules and four inherited restriction modules passed individual `lean --trust=0 -DwarningAsError=true` checks. Joint imports and exact-target audits passed for **38 selected new declarations** (29 specialization/curvature and nine Laplacian/intertwiner declarations), plus **33 inherited declarations** (26 restriction/certificate and seven matrix-spectrum declarations). Every reported transitive dependency is in `propext`, `Classical.choice`, `Quot.sound`; no custom axiom, `sorryAx`, or `Lean.ofReduceBool` was accepted.

The new exact checker suites passed **17 and ten test methods**, respectively, under normal Python and `python -O`, with byte-identical successful records for each pair of runs. Both deliberate negative controls failed in both modes. The unchanged 16-method restriction suite, its rational certificate example, and its zero-mode checker also passed fresh normal/optimized replays. The zero-mode replay retained the cost spectrum `0, 19/4, 83/10` and return spectrum `1, 4/23, 10/93`.

Lean remains pinned to **4.31.0** and Mathlib to `fabf563a7c95a166b8d7b6efca11c8b4dc9d911f`. The original split-zero core was recovered and its exact Git blob `ff991f7383922e71cdf0e4a3bc85e89e18f808ef` and 7,366-byte length were verified by the unchanged preparer. This run did not rebuild every unrelated SplitZero module or claim a new audit of the full programme.

## Verified new source blobs

| Source | Git blob |
|---|---|
| `SplitZeroRelationCurve.lean` | `fa7b7f509f3704c95088fee6d6dd79c27ed3c868` |
| `SplitZeroSpecializationChart.lean` | `cacc81a5ec27a62628dd56ffd61af80ba83cdb75` |
| `SplitZeroActionHull.lean` | `e9846ae0461129f0a24acd77b00388da92969f62` |
| `SplitZeroCurvatureRestriction.lean` | `f9e8ba333d75ad05ba9662c19f2bd5fd1cdd9ab5` |
| `SplitZeroLaplacianControl.lean` | `b22728cbb659e697b1e1296f753f75adac82b712` |

The checker blobs are `04e726461ce30d320ab788bc32597968b96379d1` and `0aca68ffe6f49a47222a790096e77614e071e026`. The workflow blob is `509ea6454f48c65b0919b91310f2b0d41ab3c7bb`.

## Written proof versus formal scope

`HOCHSCHILD_COMPARISON.md` gives the exact original theta/Hochschild trace factorization, Gaussian Laplacian identity, full-to-critical quotient map and its finite generalized-block kernel, and a support-retaining repair of the printed zero-Fourier-mode assertion. The Schwartz-space, closure, heat-limit, and Scaling Site arguments there are written proofs, not new Lean certificates.

`RESEARCH_NOTE.md` gives the local-to-global specialization description, cyclic gcd calculation of the least invariant enlargement, signed metric-pole curvature current, and the bridge from curvature jets to the existing finite trace certificate. The formal modules prove their stated finite/local algebraic and scalar-analysis portions, not a full coherent-sheaf or distribution-current library.

`LAPLACIAN_PARABOLA.md` adds a written quantitative consequence: the original two-sided control bound encloses the full Laplacian numerical range in an explicit parabola. Its completing-square estimate is not added to the selected Lean scope.

The source-level analytic arguments require independent mathematical review. The literature was read for the complete Connes–Consani chapter, pp. 83–101, not the full proceedings volume. Neither the code nor these notes assert a uniform arithmetic upper-volume estimate, an invariant positive metric, spectral simplicity, or RH.

## Coordination and preservation

The integration branch retains every PR26 addition at `e382e4f61aa4a61b621a8f064dfefc1ab80640d8` and current-main publication commit `1f7e7c02343884a17df9873566e81a9083c70951`. It changes no inherited proof, dependency pin, frozen reader, or publication source. Only the dedicated branch is advanced; main and the earlier PR branches are not rewritten or merged.

The post-checkpoint additions of these status and research notes do not change the five verified source blobs above. A later workflow run is not silently substituted for the observed successful checkpoint.
