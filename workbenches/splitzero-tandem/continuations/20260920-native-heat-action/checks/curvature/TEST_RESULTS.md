# Exact test receipt — 20 September 2026

Both completed runs exited with code 0:

```text
python -u check_exact.py
python -O -u check_exact.py
```

Both reported `PASS 2014 exact checks; no floating point used.`
The checks use SymPy 1.13.1, integer and rational complex arithmetic, and
explicit `RuntimeError` failures, so optimization does not disable them.
No sampled exponential or numerical tolerance is used.

Each run reported:

```text
PASS  102  DS10 contains independent enclosure
PASS   12  DS11 contains independent enclosure
PASS    1  DS12 adjoint transport
PASS    7  DS12 positive heat coefficient transport
PASS   56  Dyson matrix word coefficients
PASS   56  Dyson trace word coefficients
PASS    6  a1 antiadjoint identity
PASS    1  curvature antiadjoint total weight
PASS   10  curvature coefficients contain no floats
PASS    1  curvature confluent squared nodes retained
PASS   10  curvature exact heat-series coefficient
PASS    1  curvature leading coefficient
PASS    1  curvature metric selfadjointness
PASS    1  curvature next coefficient
PASS    1  curvature square-zero fixture
PASS  608  exact tail ratio
PASS   46  finite positive tail below geometric bound
PASS   46  first omitted tail index
PASS  608  geometric ratio majorant
PASS   72  heat coefficients rational real
PASS    7  holomorphic coefficient similarity invariance
PASS   18  independent exponential tail ratio
PASS   72  n(2n-1) coefficient bound
PASS    6  nilpotent path square
PASS  246  ordered simplex moments
PASS    2  positive rank-one norm square
PASS    2  rank-one relation square zero
PASS    6  real-parameter a1
PASS    2  row column zero
PASS    3  sharp curvature threshold sign
PASS    2  specified metric selfadjointness
PASS    1  transport metric differs from original
PASS    1  untransported metric changes positive action
PASS 2014 exact checks; no floating point used.
```

## Independence of the tests

- Ordered simplex moments are evaluated by expanding gap monomials in
  ordered-time variables and integrating their powers; the routine does
  not use the factorial formula that it checks.
- Dyson coefficients are compared as full matrices, using matrix
  polynomial multiplication on one side and gap-word enumeration on the
  other. Trace comparisons are checked separately.
- The DS10 and DS11 intervals contain independent certified enclosures
  formed from the two separate exponential series with a dimension-based
  absolute tail. Those enclosures do not use DS8.
- The metric transport test deliberately chooses a transported metric
  different from the original source metric and verifies that replacing
  it by the original metric changes the positive heat coefficient.
- Curvature coefficients through degree ten in heat time are compared
  against direct degree-two-in-parameter matrix polynomial multiplication
  in the original nonidentity metric. Eigenvalues `2, -2, 0` include both
  opposite eigenvalues and repeated squared eigenvalues.
- The fixtures are synthetic finite examples, not original arithmetic
  examples or evidence for a cutoff asymptotic.

## Test-development record

The DS3–DS12 test set first passed 1,985 checks. While adding the curvature
test, a Python integer-division expression introduced an unwanted float
into that new test; its exact equality check failed. Replacing that
expression by `sympy.Rational` corrected the test, and explicit no-float
checks were added. The mathematical formulas required no correction.
The complete 2,014-check set then passed in both regular and optimized
Python, as recorded above.
