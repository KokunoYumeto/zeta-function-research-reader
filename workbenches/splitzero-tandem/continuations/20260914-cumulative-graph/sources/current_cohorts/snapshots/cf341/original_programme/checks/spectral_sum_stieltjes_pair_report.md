# Exact symmetric-square parity calibration

The new checker is `scripts/check_spectral_sum_stieltjes_pair.py`. It
independently constructs the original symmetric-square algebra and both
proposed parity quotients, then compares their complete maps in exact
coordinates. It also computes the norm of one declared two-variable
Gaussian density before and after the full matrix-weight and half-line
transformations. No Python `assert`, floating-point calculation,
quadrature, or Lean execution is used.

## Algebra construction and retained data

Start from the original power basis of `E_h=C[s]/h`. Its symmetric tensor
basis consists of `s^i tensor s^j+s^j tensor s^i` for `i<j` and one copy
of `s^i tensor s^i` for `i=j`. All orbit sums are unscaled. Their embedding
in the full tensor square and an explicit coefficient extraction map are
retained; their tensor-coordinate Gram is diagonal with entries two for
off-diagonal orbits and one for diagonal orbits.

The original sum, difference-square, and reflection operators are computed
directly in that basis. Their reflection eigenspaces provide an independent
dimension check for the proposed parity carriers. Separately, the script
expands the original polynomial `h((1+Z+r)/2)` and constructs the exact
polynomials `A0(x,Delta), A1(x,Delta)`, with `x=-Z^2` and `Delta=r^2`.
The even quotient has ideal `(A0,x Delta A1)`; the odd quotient has ideal
`(A0,Delta A1)`. Groebner remainders supply full quotient bases; no radical
or squarefree quotient is used in constructing them.

Both quotient bases are mapped into the original symmetric square by
their actual polynomials in the original operators. The combined map is
checked invertible, with its exact determinant recorded. The checks retain
the factor `x` in the even ideal, both reflection eigenspaces, every original
operator, and the complete module maps

```text
alpha: Bo -> Be, p -> x p
beta:  Be -> Bo, p -> p
```

The compositions equal the original x multiplication on each carrier.
The injection, surjection, kernel, cokernel, and relative-coordinate actions
are all tested through their explicit matrices. The cokernel retains the
exact polynomial

```text
A0(0,Delta)=(-1)^D H(-Delta/4),
```

including its coefficient `4^(-D)`. The kernel of beta is represented by
`p -> p Delta A1`. Its inherited multiplication is tested separately:

```text
p star q = p q c(Delta),
c(Delta)=(-1)^(D+1) Delta H'(-Delta/4)/2.
```

Thus its module identification with `C[Delta]/A0(0,Delta)` is not presented
as an ordinary algebra identification. The original sum-kernel injection
and sum-cokernel projection are also computed in the unscaled tensor basis.

The full original paired-packet coordinate `x_h=-Delta/4` is retained as
well. Both defect maps into and out of `A_H=C[x_h]/H` are tested, including
the factor `-4` in the relative-coordinate action and the inherited
multiplier `2(-1)^D x_h H'(x_h)`. The full even observation unit has defect
action `V(x_h)^2` on both kernel and cokernel. For the declared unit in
these fixtures this is `(1-x_h/2)^2`; every derivative modulo H remains
in that multiplication matrix. The determinant identity for the exact
sequence and the symmetric-square unit determinant are also checked.

The script separately builds the paper's literal three-group orbit basis
from `a_i=x_h^i` and `b_i=(s-1/2)x_h^i`: the a–a orbits, b–b orbits, and
mixed a–b orbits. It constructs `T_s` and its inverse using the actual
orbit Gram factors one and two, proves their two matrix products are the
identity, and checks `|det T_s|=1`. The full change between this source
basis and the Groebner parity bases is retained. The source metric,
generator, weight blocks and determinant equality are checked in this
literal basis as well. Both original polynomial primitive identities
are independently expanded with all factors one-half and both signs.

## Polynomial fixtures

| Fixture | H(y) | Even dimension | Odd dimension |
| --- | --- | --- | --- |
| simple_positive | y-1 | 2 | 1 |
| central_length_two | y | 2 | 1 |
| simple_mixed | (y+1)(y-1/4) | 6 | 4 |
| repeated_off_line | (y+1)^2 | 6 | 4 |
| central_length_four | y^2 | 6 | 4 |
| repeated_and_positive | (y+1)^2(y-1/4) | 12 | 9 |

Here `h(s)=(-1)^D H(-(s-1/2)^2)` in every fixture. The names describe
only these polynomial spectra. No selected model centre is asserted to be
an actual zero of the theta function. The central fixtures demonstrate
that the algebra maps and dimension formulas remain valid when `H(0)=0`,
even though the actual packet studied in the paper excludes that case.
The repeated fixtures reject deletion of the original nilpotents in both
the one-factor algebra and its full symmetric-square sum operator.

## Original constrained minima

The simple-positive, simple-mixed, and repeated-off-line fixtures also use
a full original source of symmetric polynomials of total degree `2(d-1)`.
Their Gram matrices are computed directly from the original two-variable
Gaussian moments and original unscaled orbit sums. The full residue map
uses the independently prescribed observation unit
`v(s)=1+(s-1/2)^2/2` in each tensor factor. This unit is invertible in all
three specified fixtures and commutes with the original reflection.

The convention is `J=U2 Jraw`. Therefore the original minimum representative
satisfies `Jraw R=U2^(-1)`. If the same constraint is instead expressed with
a numerator unit epsilon, that unit is `U2^(-1)`, not `U2`.

These residue-unit data are independently prescribed finite inputs; this
polynomial v does not generate the Gaussian density. The finite minimum
tests therefore calibrate the algebraic identities and coordinate types,
not the analytic coupling of the actual theta density with its unit.

The script verifies the full source jet identity, original representative
Gram, and orthogonality to every admitted relation. It then transports that
metric using the complete parity embedding, retaining its determinant.
The even–odd cross Gram vanishes, and the original weight
`W=S*G+GS-2G` becomes the rectangular off-diagonal form

```text
[[0, beta* Go-Ge alpha],
 [(beta* Go-Ge alpha)*, 0]].
```

The entire relative characteristic polynomial is compared with

```text
lambda^D det(lambda^2 I - Go^(-1) off* Ge^(-1) off).
```

This retains all zero eigenvalue multiplicities without dividing by lambda.

## One coupled Gaussian norm in all coordinates

The norm-pushforward tests use exactly `w(t)=exp(-t^2/2)` in both original
variables. The total mass is `2 pi`. This is a coherent declared Gaussian
model throughout the original coordinates, the summed/relative coordinates,
and the half-line coordinates; no independent unit is involved in these
norm comparisons.

The substitution `u=t1+t2`, `v=t1-t2` retains the Jacobian `1/2`. The
relative matrix weight is computed from the exact v-integral as

```text
W_ac(u)=sqrt(pi) exp(-u^2/4) (-1)^(a+c) 2^(a+c) (2(a+c)-1)!!.
```

For relative powers zero through two it gives exactly

```text
[[1, -2, 12], [-2, 12, -120], [12, -120, 1680]]
```

times the retained scalar density. The unscaled relative columns
`1, Delta+2, Delta^2+12 Delta+12` produce diagonal entries `1,8,384`.

For the even/odd sum split, `x=u^2` carries the density to
`sqrt(pi) exp(-x/4) dx/sqrt(x)` and its x multiple. Their moments are
computed from their exact gamma integrals and compared with the independent
variance-two Gaussian moments. An additional factor one-half is rejected.

For every original total degree M from zero through six, the script builds
the full coordinate change from unscaled symmetric monomials to

```text
Delta^a x^b,        2a+2b <= M,
Z Delta^a x^b,      2a+2b+1 <= M.
```

It checks every reconstructed polynomial, the invertible coordinate map,
and the entire source Gram before and after the matrix/parity transformation.
Thus the total-degree restrictions, mixed relative moments, and odd x
weight are checked together. The arithmetic theta density is not substituted
by this model in the mathematical proof.

## Execution

From the package root:

```text
python scripts/check_spectral_sum_stieltjes_pair.py --output checks/spectral_sum_stieltjes_pair.json
python -O scripts/check_spectral_sum_stieltjes_pair.py --output checks/spectral_sum_stieltjes_pair_optimized.json
python scripts/check_spectral_sum_stieltjes_pair.py --self-test-failure --output checks/spectral_sum_stieltjes_pair_negative.json
python -O scripts/check_spectral_sum_stieltjes_pair.py --self-test-failure --output checks/spectral_sum_stieltjes_pair_negative_optimized.json
```

The ordinary and optimized runs each pass 644 records: 583 exact checks and
61 rejected incorrect variants. The two deliberate-failure runs return one,
adding a false 645th record after the same 644 passing records. The `records`
arrays agree exactly across ordinary and optimized execution. These are finite
records, not theorem counts or certificates for analytic input.

The JSON receipts record exact source and checker hashes. The independent
algebra/checker audit is in the parent workspace at
`work/symmetric_parity_formula_audit_20260912.md`.
