# September 12 calculations: what was checked

This edition joins nine research contributions to the living zeta repository. Their purpose and mathematical objects are explained in [Research programmes](RESEARCH_PROGRAMMES.md). The full notes, equations, source citations and executable tests remain separate and readable; the earlier six-reader edition is unchanged.

## Content review and executable evidence

| Contribution | Review and reproducible evidence |
|---|---|
| [CUE research map](CUE_RESEARCH_MAP.md), PR #1 | Editorial map read; its eight referenced theorem labels checked against the existing source. This contributes navigation rather than a new theorem. |
| [Unified Flow](workbenches/unified-flow/), PR #2 | Complete horizon/probe derivation and checker read; 28 elementary checks passed normally and with optimized Python, with identical output. |
| [Rees and actual quotient calculations](workbenches/split-support-rees-trace/), PR #3 | Four complete notes and four checkers read. Normal/optimized runs agreed: 2,085 Rees conditions, 1,452 actual-comparison conditions, 5,443 finite congruence comparisons, and 101 origin-ladder checks. These are finite instances, not counts of proved general theorems. |
| [Tau-base comparison](workbenches/tau-base-cohomology/), PR #8 | Complete analytic and algebraic arguments read. Base checker: 79 named records in six suites; finite comparison: ten test methods. Both normal/optimized runs and deliberate-failure controls checked. |
| [Chain descent](workbenches/tau-chain-descent/), PR #9 | Complete argument read, including its exact extension unit and reflection-stable residue interface. Twelve test methods passed normally and optimized; failure controls failed as intended. |
| [Global retraction](workbenches/tau-global-retraction/), PR #10 | Complete continuous-retraction proof reviewed independently twice; twelve finite methods and failure controls replayed. The infinite-dimensional estimates are supported by the written argument, not certified by those finite tests. See the [Meyer source comparison](workbenches/tau-global-retraction/MEYER_SOURCE_COMPARISON.md). |
| [Homotopy/control](workbenches/tau-homotopy-control/), PR #11 | Complete argument and sixteen finite methods reviewed; positive runs agreed normally/optimized and failure controls failed. |
| [Formal tau recovery](workbenches/tau-formal-recovery/), PR #12 | Seven Lean sources read, their hashes matched to the successful exact-head build, and 87 selected axiom reports reparsed. Details below. |
| [Orthogonal boundaries](workbenches/tau-orthogonal-boundary-control/), PR #13 | Complete Gram, rank-two, density and graph argument read; thirteen finite methods replayed normally/optimized, including deliberate-failure controls. |

These reviews are tool-assisted checks, not independent human peer review. The finite symbolic replays used Python 3.13.9 and SymPy 1.13.1 where applicable. The authors' original environment records are preserved rather than overwritten.

## The precise Lean certificate

PR #12 head `5d2772ea0a16d177ac3e01ff70394b90ba95a232` passed [Actions run 34686934725, job 103535438942](https://github.com/KokunoYumeto/zeta-function-research-reader/actions/runs/34686934725/job/103535438942). The seven module sources and the selected axiom reports were independently matched to that run. Those reports use only the recorded standard Lean axioms. The certificate covers the declarations named in the package, not every analytic or arithmetic claim in the surrounding programme.

A one-line Windows test-fixture repair now explicitly writes UTF-8 with LF newlines. The unchanged original harness had two newline-related failures on Windows; the repaired harness passes all 18 tests both normally and optimized. This changes no Lean declaration. The earlier PR #11 report of an uncompiled draft remains historical, with a dated link to the later successful source version.

## Precision corrections included in this edition

- The fixed-N origin ladder states its range $0\leq m<N$; its Taylor-polynomial inverse uses $m\geq1$, with $m=0$ handled by the identity comparison.
- Same-packet residue duality repeats the inherited condition that the packet is stable under $\rho\mapsto1-\overline\rho$, retaining full multiplicities. This does not restrict the preceding general Gram construction.
- The continuous contraction is explicitly in complexes of locally convex complex vector spaces after forgetting $\mathbb C[t]$-linearity. Its actual scaling defect remains displayed.
- Mellin transformation of arbitrary Hilbert-space vectors means its $L^2$ extension. The completed jet graph is a closed linear relation, with its explicit nonclosability witness, not an operator graph over the original Hilbert space.

These changes preserve the equations and proof data. They do not supply the still-missing relative weight estimate. In particular, small absolute Gram and control matrices do not by themselves imply a small relative control norm, positivity of the Weil form, or RH.

## Versions and reproducibility

[WORKBENCHES.json](WORKBENCHES.json) gives the exact contribution heads, merge commits, source paths, dependencies and local reproduction entrypoints. Each workbench retains its author's validation record and citations. The source archive accompanying the calculation reader contains the authored notes and checking code, not the private literature library or session logs.
