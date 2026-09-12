# Toda–CV bridge: complete source and cumulative integration

The complete standalone source is `toda_cv_exact_bridge_20260912.tex`, dated 13 September 2026. Its final mathematical source SHA256 is `97652a43445708c0e6d2a959f45aed8a4f2a7f73f9cd4b6cd57e67b8fedb408e`. Preserve that original file in full.

It contains all TVB.1–TVB.44, including TVB.34a–b and TVB.38a–c. The file is a proof contribution. Its included source hashes identify the exact delivered Toda note and the complete parent join. They do not assert that the numerical seed outputs are interval certificates or that the source Lean draft was compiled.

## Body extraction and macros

For the cumulative proof fragment, extract everything after the standalone `\maketitle` and before `\end{document}`. Preserve the entire body, including its source provenance, proofs, domain clauses, exceptional dimensions and closing crosswalk. Prepend the cumulative chapter heading “The exact bridge from cyclic interpolation volumes to the two Toda flows”. Demote each original body `\section{...}` to `\subsection{...}`. There are no original subsection commands needing another level.

The source uses these six local presentation macros. Either provide exactly these definitions within a local group around the fragment or expand each control sequence token by the mapping below. A token-aware replacement must not replace a prefix inside a longer command.

| Source command | Exact expansion |
|---|---|
| `\C` | `\mathbb C` |
| `\R` | `\mathbb R` |
| `\tr` | `\operatorname{Tr}` |
| `\Span` | `\operatorname{span}` |
| `\im` | `\operatorname{im}` |
| `\Alt` | `\operatorname{Alt}` |

The source preamble additionally loads `amsmath`, `amssymb`, `amsthm`, `mathtools`, `mathrsfs`, `geometry` and `hyperref`. The body needs the mathematical facilities and `\mathscr` from `mathrsfs`; its standalone page geometry and title setup should not replace the cumulative page settings. No theorem environments are used in this body despite the standalone preamble defining three available environments. All displayed tags are explicit.

Record the extracted/expanded fragment hash separately from the full original source hash. Changes of section level and macro expansion are presentation transforms; preserve the original body and all equations in the source archive.

## Exact mathematical additions

The two separate curvature costs are TVB.21, with their shared term `alpha_(N+1) delta_N` retained. TVB.19 identifies the complete next polynomial boundary as `chi r_m`, proving its norm `nu_m = omega_(N+1) + b_(N+1)* G_N b_(N+1)`. TVB.26 recovers the signed imaginary cross phase from the derivative of the exact source/relation determinant quotient. TVB.34a gives the loss directly in the actual volumes and identifies equality as their arithmetic midpoint together with zero cross phase. TVB.34b is the corresponding omitted-determinant and positive-minor identity. TVB.38a–c give every minor sign and the explicit conjugate-linear isomorphism from the projected endpoint relation to the exterior source vector, including its original norm factor and alternating-tensor factorial. TVB.39–44 reproduce and prove the supplied parent join, retaining the spectral-subspace coupling through an invertible Sylvester map.

The empty packet uses `chi=1`, `q=0`, the empty determinant `V_N=1` and the two-element split carrier. The first positive-dimensional admitted degree has the explicitly declared scalar convention `delta_(q-1)^end=0`, leverage one, and zero incoming boundary cost. It never uses `V_(q-2)`, an inverse of `K_(q-2)`, or `nu_(-1)`.

## Verification scope

Two successful isolated XeLaTeX passes compile the completed standalone file to 13 pages under `toda_cv_bridge_preview_20260913/`. The final log has no overfull, missing-character, undefined-control-sequence or warning lines. This is compilation evidence only; it is not a visual approval of the eventual cumulative PDF. The parent’s cumulative build and full visual inspection remain the publication evidence for that edition.

An independent algebra reviewer checked the complete Toda and CV sources, the scalar loss/telescope, endpoint minor signs and map, varying-measure derivatives, and the exterior bound at arbitrary real tilt. Its concrete presentation/domain repairs were incorporated. A separate root-appointed reviewer is checking the complete final source and will record its final hash in `toda_cv_exact_bridge_independent_review_20260913.md`.

No local Lean execution, source-checker duplication, remote mutation, or modification of the frozen cyclic edition occurred in this contribution.

Final domain clarification: the seed Mellin integral is stated on Re s > -2, and the nonempty Sylvester Hom unit sphere is justified by C_- being nonzero when L > 0. No displayed identity or other mathematical scope changed.
