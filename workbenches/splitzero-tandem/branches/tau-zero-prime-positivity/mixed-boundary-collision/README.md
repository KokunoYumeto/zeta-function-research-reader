# Collision coefficients, mixed boundaries and their exact completion return

This edition publishes the complete local collision calculation and integrates it into the programme's cumulative **Split Zero and the Arithmetic Trace** source. The cumulative manuscript develops the support-sensitive coefficient geometry, prime spectra and boundary cohomology, the original-zeta Mellin and trace maps, marked metrics and jets, prime-word actions, and the heat/residue constructions. This addition supplies the actual adelic receiving proofs, collision-prism coefficients, tensor filtrations and local completion maps. It does not replace the programme by this latest calculation.

Start with the [13-page research reader](MIXED_BOUNDARY_COLLISION_READER.pdf), with [editable LaTeX](MIXED_BOUNDARY_COLLISION_READER.tex), [complete BCE1–45 proof](MIXED_BOUNDARY_COLLISION_EXTENSION.tex), and [reproducible diagrams](MIXED_BOUNDARY_COLLISION_FIGURE.tex). The [cumulative entry point](MAIN.tex) includes the full receiving chapters and bibliography; its complete local input dependencies accompany it. Compile that entry point from this directory. The earlier collection's compiled reader is retained separately; this edition does not describe it as containing the new chapter.

## What the new calculation establishes

The coefficient algebra is the original `C = Z_3[epsilon,T]/(epsilon^2, T^2-6 epsilon)`, with `z=epsilon T` and `F(T)=9cz`. The existing adelic boundary characters and the specified collision Frobenius are compared by explicit maps; they are not declared identical.

| Stable result | Full proof | Contribution and retained limit |
|---|---|---|
| SZ-20260923-965 | [CFF5–22](collision_boundary/original_sources/COLLISION_FROBENIUS_FILTRATION_AND_SUPPORT.tex) | Cotangent Frobenius, its injection defect `27c v2`, and the exact integral extension with quotient `Z/9`. |
| SZ-20260923-966 | [CF23–64](collision_boundary/original_sources/COLLISION_FILTRATION_APPENDIX.tex) | All tensor degrees and powers, integral diagonal forms, dual/mixed maps and the retained factorial contribution. |
| SZ-20260923-967 | [CFF28–35, including CFF34a–b](collision_boundary/original_sources/COLLISION_FROBENIUS_FILTRATION_AND_SUPPORT.tex) | Full supported-cohomology receiver, exact Bockstein image, and the contractible case where that image vanishes. |
| SZ-20260923-968 | [BCE1–28](MIXED_BOUNDARY_COLLISION_EXTENSION.tex) | Integral boundary characters, tensor cokernels, the connecting class of exact order three, its torsion detector, and the cotangent receiver that kills it wherever its chain lift exists. |
| SZ-20260923-969 | [BCE29–41](MIXED_BOUNDARY_COLLISION_EXTENSION.tex) | The actual ideal `(3+epsilon)`, Breuil–Kisin twist and local divided-Frobenius complex; the earlier class is an explicit boundary there, while different filtration defects survive. |
| SZ-20260923-970 | [BCE42–45](MIXED_BOUNDARY_COLLISION_EXTENSION.tex) | Completion with transported filtration preserves the computed local cohomology, with explicit return and chain homotopy. Recomputing the filtration from the quotient loses the precisely computed group `Q_m`. |

These are local integral coefficient, cohomology and prism calculations. They neither identify the local complex with absolute syntomic cohomology nor establish arithmetic purity, positivity of the original Weil pairing or RH. The support labels `e` and `tau` remain distinct throughout their specified maps.

## Complete proofs and human sources

The [source bank](collision_boundary/original_sources/) preserves the sealed reader, original proof files and independent derivations. Every Markdown derivation has a complete editable LaTeX counterpart. [Conversion checks](LATEX_CONVERSION.json) record all retained mathematical expressions and equation tags; these are source-conversion checks, not new kernel certification.

The cumulative receiving chapter contains the full [ABR](collision_boundary/ABR.tex), [GBC](collision_boundary/GBC.tex) and [GSB](collision_boundary/GSB.tex) arguments, the [DP1–43 prism derivation](collision_boundary/DP.tex), [CFF](collision_boundary/CFF.tex), [CF](collision_boundary/CF.tex) and [BCE](collision_boundary/BCE.tex), alongside the existing [all-prime boundary calculation](45_boundary_tensor_weights.tex) and [full finite-support receiver](15_full_finite_support_recollement.tex). Readers do not have to reconstruct these inputs from a result code alone.

Human foundations include [Connes's trace-formula paper](https://arxiv.org/abs/math/9811068v1), [Connes–Consani–Marcolli on the adelic Weil proof](https://arxiv.org/abs/math/0703392v1), [Bhatt–Scholze on prisms](https://arxiv.org/abs/1905.08229v4), and [Bhatt–Lurie on absolute prismatic cohomology](https://arxiv.org/abs/2201.06120v1). Exact source labels and the scope of their use remain in the reader and [bibliography](collision_boundary/bibliography.tex). The programme calculations are derived comparisons using those human sources, not replacements for or claims of authorship of their theorems.

## Verification and reproducibility

[Source integration](SOURCE_INTEGRATION.json) records the original and integrated manuscript hashes, complete input dependencies, ordered equation tags and the mathematical owner's separately attributed validation. The owner compiled the complete temporary manuscript to 457 pages with no unresolved references or duplicate labels; the added chapters had no overfull boxes. Twelve existing overfull boxes elsewhere were retained, not silently repaired. That temporary validation PDF is not included as a publication reader.

The publisher rebuilt the standalone reader solely to make its two programme-source links work online; [the build record](READER_BUILD.json) describes that repair. The original sealed PDF and TeX remain in the source bank. No new Lean execution or independent reproof of every earlier chapter is claimed. [The machine-readable result index](RESULT_INDEX.json) and [source manifest](SOURCE_MANIFEST.json) identify this edition's actual files and scope.
