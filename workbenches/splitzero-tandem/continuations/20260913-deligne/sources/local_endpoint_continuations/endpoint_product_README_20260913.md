# Exact endpoint products and original relation costs

The complete mathematical article is `endpoint_product_sharpening_20260913.pdf`, with its standalone LaTeX source beside it. Its formulas EP.1–EP.54 include the full original radius proof, the exact repeated-interior product, both sharp scalar endpoint optimizations, phase-polynomial zero cases, the original Schur/determinant/transfer maps, and the actual arithmetic relation-cost consequences. The complete analytic source proofs used by its arithmetic estimates are retained in `endpoint_product_dependencies_20260913`.

For a fixed full off-line quartet, the proved norm estimate and exact product force a two-volume lower threshold of 2. The separate proved balanced-window norm theorem, composed on the one-step-shorter central window, gives the original four-volume threshold of 4. The article retains every contraction and phase penalty before those lower bounds. It also gives a quadratic lower bound on the largest generalized eigenvalue of the original central relation block. These are necessary growth consequences; this packet supplies no upper estimate contradicting that growth.

The new scalar optimization uses the exact combined budget B. Its unique optimizer is described by the root x in (0,1/2) of B = 2 artanh(2x) + 4(r−1) artanh(x). The proof shows strict improvement over the earlier sinh bound when r>1 and B>0. The original arithmetic-to-scalar evaluation map and the precise scope of scalar sharpness are part of the proof.

## Reproduce the finite checks

The recorded interpreter is Python 3.13.9 with SymPy 1.13.1. The primary source/matrix checker and independent scalar checker require SymPy. They use exact arithmetic and explicit checks that remain active under `python -O`.

```text
python endpoint_product_check_20260913.py --output primary.json
python -O endpoint_product_check_20260913.py --output primary-optimized.json
python endpoint_product_independent_checker_20260913.py --output independent.json
python -O endpoint_product_independent_checker_20260913.py --output independent-optimized.json
```

The primary checker executes 415 mathematical checks on declared Gaussian and asymmetric atomic sources. It constructs source Grams, quotient minima, phases, Schur windows, relation determinants and raw transfer matrices. The independent checker executes 2,453 scalar checks. Their complete changed-formula runs are recorded with exact failure counts. The endpoint-orientation mutation in the independent checker executes 2,451 checks because its admissible perturbation list changes. Repeated optimization modes and mutations do not add new mathematical checks.

`endpoint_product_replay_20260913.py` replays both primary modes and all six primary mutations. A mutation is expected to exit with status 1 after executing its complete suite. The independent checker's `--mutation` options are `local-remainder`, `budget-denominator`, `endpoint-orientation`, `phase-feasibility`, and `interior-multiplicity`. `endpoint_product_portable_jobs_20260913.json` declares all 26 individual jobs and their expected results.

## Build and inspect the paper

```text
pdflatex -interaction=nonstopmode -halt-on-error endpoint_product_sharpening_20260913.tex
pdflatex -interaction=nonstopmode -halt-on-error endpoint_product_sharpening_20260913.tex
```

The recorded PDF has 12 pages. Its original rendered page images and the completed visual-review receipt are in `endpoint_product_pdf_qa_20260913`. The optional rendering helper requires Poppler (`pdftoppm`), Pillow, and pypdf. The source manifest pins the exact mathematical sources, checker sources, check records, reviews, proof dependencies, and reviewed PDF. The native intake helper is outside the portable packet; its exact copied dependency bytes and hashes are retained.

The proof does not use Lean, zero-location numerics, a numerical enclosure of either analytic constant, or an arithmetic moment interval supplied by the auxiliary fixtures. The mathematical argument and the exact finite checks have their separate recorded scopes.
