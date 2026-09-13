# Exact arithmetic coefficient and theta-generating join

`gamma_exact_coefficient_join_20260913.tex` is a complete standalone proof chapter with equations GC.1–GC.59. It proves the original-coordinate finite coefficient formulas and every tilt derivative, the supplied Zeta-owner analytic generating join and its full branches, and the original section-change cochain with its tensor signs. The chapter explicitly credits the supplied generating identities. All source masses, affine coordinates, complex amplitudes, local units, support labels and empty-quotient endpoints remain specified.

The chapter compiles with:

```text
pdflatex -interaction=nonstopmode -halt-on-error gamma_exact_coefficient_join_20260913.tex
```

The recorded standalone build has 12 pages. The final visual receipt identifies the exact PDF and source hashes. It records actual contact-sheet inspection of all pages, native inspection of the generating and quotient formulas, and the one harmless underfull paragraph in the TeX log. The cumulative reader has its own build and visual verification.

The independent written reviews are:

- `gamma_exact_generating_join_independent_review_20260913.md`: full analytic branch, domination and generating-coefficient proof.
- `gamma_exact_coefficient_join_typing_review_20260913.md`: original analytic source, coefficient indices, complete local units, cochain signs, support lifts, determinant induction and finite checker inspection.
- `gamma_convolution_bound_review_20260913.md`: the source delivery's packet and shifted multiplier bounds, quotient dimensions and exact tilted tail.

The checker uses Python 3 with SymPy 1.14.0 and no other nonstandard Python library:

```text
python gamma_exact_coefficient_join_check_20260913.py --json check-normal.json
python -O gamma_exact_coefficient_join_check_20260913.py --json check-optimized.json
```

Each positive run executes 143 finite exact identities. Run the same checker with each `--mutant` value: `coefficient-factorial`, `initial-mass`, `coordinate-sign`, `determinant-phase`, `derivative-degree`, `cochain-sign`. Each such run must exit 1, and precisely one of those same 143 records must fail. These are mutations of mathematical formulas; no unconditional false startup guard is counted as a formula test.

`replay_gamma_exact_coefficient_join_20260913.py` runs all fourteen modes and verifies the exact counts and exits. Keep it beside the checker and TeX. It accepts `--output-directory` and an optional `--dependency-path` for a directory containing the pinned SymPy installation; otherwise the selected Python's installed SymPy is used. A local sibling directory named `kernel_layer_replay_dependencies_20260912`, if present, is the task's pinned dependency directory. The checker can also be run directly in a virtual environment containing SymPy 1.14.0.

The recorded replay lives in `gamma_exact_coefficient_join_build_20260913/checks`. All 28 result/log files and the replay receipt are preserved. The independent replay-review script verifies those actual records and log hashes, and distinguishes inspecting an execution record from launching an additional execution.

Supplementary reviewer scripts retain separate scopes. The typing-fixture script has 37 exact checks and two rejected wrong-sign formulas in both normal and optimized Python. The Toda-index fixture has 32 checks and uses assertions; its receipt concerns normal execution only. Neither is described as an arithmetic zero-packet certificate.

The original web delivery is separately preserved under `sources/web_gamma_convolution_delivery`; its complete 988-line source was audited before integration. That source's own 17-method regression suite and startup-guard controls remain separately scoped in the source audit and source replay receipt. The new checker does not overwrite or relabel those records.

No Lean execution, actual zero-location certification, growing-degree upper bound, or arithmetic interval certificate is claimed by this chapter's finite tests. The complete written analytic and algebraic proofs supply the general results. Certified seed moments and finite metric error-transfer results are separate companion chapters.
