# Exact finite validation

20 September 2026. The complete derivation is `NATIVE_MOMENT_PRECISION.tex`.

Commands run successfully:

```text
python verify_native_precision.py
python -O verify_native_precision.py
pdflatex -interaction=nonstopmode -halt-on-error -draftmode -jobname=native_precision_math_check NATIVE_MOMENT_PRECISION.tex
```

The Python checks use explicit exceptions, not `assert`, so optimization does not disable them. Both final runs pass **2,013 exact checks**:

- 89 rational/Gaussian-rational identities;
- 1,703 exact positive-semidefinite matrix checks, including singular deflation and entire complex joint remainders;
- 206 exact scalar inequalities;
- 15 negative cases detecting missing conjugations, uncertified midpoint positivity, wrong four-endpoint signs, or falsely real cross terms.

Coverage includes interval Grams through degree six and their exact unipotent determinant morphism; all four native polynomial-weight patterns and both parity shifts; non-unit masses; certified moment perturbations; outward inverse brackets and norm errors; rectangular inverse-derived quadratic forms; explicit Radau Schur-denominator floors and kappa perturbations; unchanged complex S transport; exact quotient and conductor composition/full-kernel orthogonality; the whole three-vector complex Gram determinant; signed products; and all 81 combinations of four endpoint positions in their enclosing intervals. The onefold-to-convolution moment precision budget and a residual-certified computed inverse are tested too.

These rational measures are universal-identity **test instances**, not the native arithmetic measures. No original arithmetic moment was given a test value. The original native density floors are proved from the original envelope in the TeX.

The final two-pass draft-mode TeX check succeeds, 13 pages, with no undefined references or overfull boxes. One bibliography paragraph has an underfull-box notice. Draft mode produces no PDF; this is a syntax/reference check, not a publication or rendering workflow.

## Explicitly evaluated interval constants

```text
g_0 = 1
g_1 = 1/40
g_2 = 5/981552
g_3 = 49/6282417514496
g_4 = 189/2564439270211137950720
g_5 = 43923/11861311456405681902807594879680512
g_6 = 7412864745/8180356697516888936957935460045935405753419192598528
```

The proof gives the exact rational formula for every degree, not only these finite examples. The native constants a_k, A_k, theta_h, M_alpha, TW7/BT12 constants and original scalar moment integrals remain their stated unevaluated original inputs. Their required downward/upward precision is explicit; midpoint values are never certified by assumption.
