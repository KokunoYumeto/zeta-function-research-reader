# Accepted actual Taylor-unit formal gauge

The mathematical object is the original finite arithmetic packet of the
two-leg theta complex over the tau base, with all zero multiplicities and the
complete Taylor unit `upsilon_h = j_h(g/h)` retained. This note constructs the
map carrying that unit into the formal exponential family; it is not an
RH-equivalent criterion or a replacement metric.

## Exact accepted artifacts

- `ACTUAL_TAYLOR_UNIT_FORMAL_GAUGE.md`: SHA256
  `9ded2486160b76bf65f92d44b73cdd0c59a3ca7e5334f88682e10592d5a45b2f`.
- `INDEPENDENT_REVIEW.md`: SHA256
  `e32e978870e65ea375040762432a3cfe479068ebe6cfd800086a2d35d55da6d0`.
- `check_unit_gauge.py`: SHA256
  `8b475de68e1136e2ba8890bdf68c7b4ad7b4cc77a392d696003d6823b640d276`.
- `CHECK_NORMAL.json` and `CHECK_OPTIMIZED.json`: each 752 bytes, SHA256
  `c27e89d8082b3154ca7269da7d70882c7b00036e76a95aa65bb53b26382d5ebe`.

Root authored and checked UG1--19 and read the full independent review and
its final acceptance. The two review comments were resolved: the completed
external product now has its explicit signed contraction on cofinal rectangular
truncations; the dagger statement has its original reflection-stable domain.
Neither comment remains outstanding.

## Completed mathematics

For the unique full Taylor representative `nu` of `j_h(g/h)`, the extra pole
module `C[s,nu^-1]/C[s]` has invertible multiplication by `h`. Its explicit
ordered formal inverse gives a contraction for `u*d_s+h-t`. The resulting
localization arrow is a quasi-isomorphism with a displayed deformation retract.
Multiplication by `nu` conjugates the differential exactly to
`u*d_s+h-t-u*nu'/nu`. The scaling operator `u*d_t-s` commutes with this gauge.

On the special fibre the induced map is multiplication by the original full
unit, not the identity. Its completed external product, followed by the original
cyclic inclusion, is exactly the arithmetic map `eta`. Residue transport retains
the complete inverse unit, the support labels and the original weight line.
The supported zero `e` has not been inverted or identified with `tau`.

## Checks and scope

Four exact rational-polynomial fixtures passed in both normal Python and `-O`,
covering repeated roots, nonconstant units and the constant-unit endpoint.
The checks cover the gauge identity, scaling commutators, two-sided pole
inverse, chain contraction, polynomial image and retract. The three deliberate
mutations `wrong_gauge_sign`, `wrong_inverse_order`, and `nonunit` each failed
with exit 1 in both modes. The independent reviewer performed proof review,
not an independent fixture replay.

The result is coefficientwise formal near `(u,t)=(0,0)`. It does not claim
global analytic invertibility of `g/h`, convergence of the pole contraction at
nonzero complex `u`, purity, positivity, a tensor-growth bound, RH, or new Lean
execution. Its finite entire scaling formula is in the explicitly transported
frame; no global analytic localization equivalence is substituted for the
formal calculation.

This accepted proof belongs to the next cumulative source cut. It has not been
retroactively inserted into the frozen 715- or 765-page publication editions.
