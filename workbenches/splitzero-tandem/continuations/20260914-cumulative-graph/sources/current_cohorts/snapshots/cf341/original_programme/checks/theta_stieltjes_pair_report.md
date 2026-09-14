# Exact calibration of the two Stieltjes spaces

The checker is `scripts/check_theta_stieltjes_pair.py`. It uses no Python
`assert` statements, floating-point arithmetic, numerical quadrature, or
Lean execution. All model moments and matrix calculations are exact over
the rational numbers with the imaginary unit where the original vertical
coordinate requires it.

The declared base moment data are those of the variance-one Gaussian:
`E[t^(2j)]=(2j-1)!!`, `E[t^(2j+1)]=0`, retaining masses `1` and `7/3` in
the different fixtures. The Stieltjes variable is the actual `x=t^2`,
while the complex-algebra coordinate remains `x=-(s-1/2)^2`.

The Gaussian Gram data and the even residue-unit data are independently
prescribed finite inputs. The formal polynomial `g_model=h*v` tests the
unit/sign identity; it does not generate the Gaussian density by the
analytic formula `|g_model/h|^2 dt/(2 pi)`. Consequently this suite tests
the finite algebraic identities, including original coordinates and full
jets, but does not verify the analytic coupling of the actual theta
density and its unit. That coupling is proved in the source TeX, not by
these fixtures. No arithmetic moment enclosure or RH claim is made here.

## Independent constructions

The first construction forms the entire Hermitian moment matrix directly
in the original powers `1,s,...,s^N`, substituting `s=1/2+i*t` into each
entry. Its residue map reduces the full nonconstant even-unit multiples
modulo the original monic `h`. The constrained minimum is then calculated
from these matrices. Its jet identity, original Gram and orthogonality to
every relation basis vector are checked directly.

The second construction independently obtains monic polynomials from
Gram–Schmidt for the moments of `lambda` and `x lambda`, using the original
positive masses. It forms both complete residue kernels modulo `H`,
including the nonconstant unit. These two kernels are compared with the
transported inverse metric from the first construction. The two algorithms
therefore begin in different bases and use different moment matrices.

The local branch tests work directly in truncated polynomial algebras.
They verify both substitutions between the original local parameter `w`
and `eta=-2 alpha w-w^2`, the finite square root and its inverse, both
branch idempotents, their full matrix inverse and determinant, and every
retained local jet power. These checks cover orders one through four at
`alpha=1`, `alpha=i/2`, and `alpha=3/5+4i/5`.

## Fixtures

| Name | H(x) | V(x) | Mass | Source degrees |
| --- | --- | --- | --- | --- |
| double_off_line | (x+1)^2 | 1+x/2 | 7/3 | 3,4,5 |
| double_and_critical | (x+1)^2(x-1/4) | 1+x/2 | 1 | 5,6 |
| even_zero_frontier | x-1 | 1+x/2 | 7/3 | 1,2,3 |
| odd_zero_frontier | x-3 | 1+x/2 | 1 | 2,3,4 |

The names describe only the finite polynomial spectra. No point in these
fixtures is asserted to be a zero of the actual theta function. The first
two retain the entire double root, and the mixed fixture also retains its
positive Stieltjes root. The last two have respectively a zero even and
zero odd next residue column; their unchanged kernel and vanishing full
weight form are checked exactly.

## Source crosswalk

- SP.3–7: original monic h, both original-coordinate inverses, orientation
  through D=4, full algebra multiplication generator and its characteristic
  polynomial.
- SP.8–9: both full local branches, retained nilpotents, all local powers,
  complementary idempotents, inverse branch matrix and determinant.
- SP.11: the nonconstant unit multiplication and its determinant; the
  original `(-1)^D` sign in h and in the formal Phi/H expression.
- SP.18–20: original monic vertical polynomials, both Stieltjes families,
  Christoffel numerator, norm and exact variance-one Gaussian norm formulas.
- SP.22–24: direct full-jet constrained minimum versus the two kernels,
  unit covariance, kernel/metric transport, every determinant factor,
  original weight and its off-diagonal block.
- SP.24–26: the relative squared trace and the complete characteristic
  identity `det(lambda I-G^-1 W)=det(lambda^2 I-Ge^-1 off Go^-1 off*)`,
  preserving all zero eigenvalue multiplicities without dividing by lambda.
- SP.27: every adjacent source-stage rank-one update and determinant ratio,
  the unchanged parity block, and both zero-frontier cases.
- SP.32–35: both full kernel compatibility identities with their parity
  signs, the exact rank-one norm and complete relative characteristic
  polynomial, and the determinant-energy identity. The derivative cost is
  computed independently in the original source: form `sR-RA`, project it
  orthogonally off the original admitted relations using the full source
  Gram at degree N+1, and compute `Tr(G^-1 C* M_(N+1) C)`. This exact value
  is compared with the displayed half-line formula. New zero columns retain
  determinant ratio one and positive derivative cost; predecessor zero
  columns retain zero derivative cost and a strict metric contraction.

The suite rejects positive in place of negative X, removal of 1/2,
inversion of the coordinate transport, omitted unit, erased mass, the
wrong odd weight, the wrong Christoffel signs, erased polynomial parity
signs, omitted global unit signs, and deletion of the repeated-jet data.
Deleting the repeated data is checked to cause the predicted rank loss,
not merely a different value of one matrix entry.

## Reproduction and evidence

From the package root, use the following commands with Python and SymPy:

```text
python scripts/check_theta_stieltjes_pair.py --output checks/theta_stieltjes_pair.json
python -O scripts/check_theta_stieltjes_pair.py --output checks/theta_stieltjes_pair_optimized.json
python scripts/check_theta_stieltjes_pair.py --self-test-failure --output checks/theta_stieltjes_pair_negative.json
python -O scripts/check_theta_stieltjes_pair.py --self-test-failure --output checks/theta_stieltjes_pair_negative_optimized.json
```

The two ordinary runs must return zero; each has 892 passing records:
769 exact checks and 123 rejected incorrect variants. The two deliberate
failure runs must return one, adding a false 893rd record after the same
892 passing records. Comparing the `records` arrays verifies equality
between ordinary and optimized execution without conflating timestamps
or runtime metadata. These are finite records, not counts of theorems.

The final JSON receipts record the checker and mathematical-source hashes.
The independent formula/source review is in
`work/theta_stieltjes_formula_independent_audit_20260913.md` in the parent
math workspace. Its role is a source proof audit; these exact tests remain
supplementary finite calibration.
