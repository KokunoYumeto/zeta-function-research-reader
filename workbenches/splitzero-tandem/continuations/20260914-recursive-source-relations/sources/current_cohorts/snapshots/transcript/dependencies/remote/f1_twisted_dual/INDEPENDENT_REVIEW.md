# Independent review of the tau-weight reflection transport

Date: 2026-09-13. Read `F1_REFLECTION_WEIGHT_TRANSPORT.md` completely,
RW1--23 and its source/scope paragraphs. Also read the complete controlling
tau-base note, the complete original exponential comparison, and the full
DS/XD source notes during the adjoining independent scaling calculation.
This review does not change the root note, execute its finite fixtures,
or claim a new Lean or primary-literature audit.

**Disposition: accept RW1--23 as stated. No required mathematical correction
found.** The following checks specify the exact scope of that acceptance.

## Reflection and differential types

The retained assumptions are the actual symmetry-stable packet,
`conjugate(chi)=chi`, `chi(k-S)=epsilon chi(S)`, `epsilon=(-1)^q`.
Under `r(u,t)=(-epsilon u,epsilon t)`, direct differentiation gives

`D_r(epsilon RP)=u RP'+(epsilon chi-t)RP=R D_{u,t}P`.

Thus the degree-zero and degree-one coefficient maps are respectively
`epsilon R` and `R`, not two identical maps. The displayed finite R matrix
is exactly substitution by `k-S`, preserves degree below q, and squares
to the identity. Its companion relation is
`R A(t)R=kI-A(epsilon t)`. These statements use all polynomial
coefficients and do not require distinct roots. Coefficient conjugation
adds precisely the stated conjugate parameter map for the actual dagger.

## Potential constant, connection, and contours

Differentiating `Phi(k-S)` gives `-epsilon chi(S)`, while its value at
`S=0` is `Phi(k)`. Hence RW10 retains the correct full constant.
Since `dt'=epsilon dt` and `u'=-epsilon u`, the pulled-back t-connection
is `partial_t+A(epsilon t)/u`. Its commutator with the coefficient
reflection is `kR/u`, so the scalar logarithmic derivative must be
`-k/u`. The actual factor `exp((Phi(k)-kt)/u)` has exactly that derivative.

RW12 is horizontal for the stated t-connection on `u!=0`; it is not an
assertion about an unspecified u-connection or a value of that exponential
at `u=0`. Under the reflected oriented contour, `dS_old=-dS_new`, so the
minus in RW13 is necessary and correct. The potential identity transfers
rapid decay, without dropping `Phi(k)`, changing an orientation, or
identifying the reflected contour with an unproved standard-cycle basis.

## Regular flow and its endpoints

For `C_a(u,t):H_{u,t+ua}->H_{u,t}`, the reflected source endpoint is

`r(t+ua)=epsilon t+epsilon ua=t'-u'a`.

Thus it is `C_{-a}(u',t')` that has the matching domain and codomain.
Differentiating `B_a=R C_a(u,t)R` gives

`B_a'=-kB_a+B_a A(epsilon t+epsilon ua)`.

The same equation and initial identity hold for
`exp(-ka)C_{-a}(-epsilon u,epsilon t)`, proving RW16 with exactly its
sign. This argument divides by no parameter; the finite matrix identity
therefore holds at `u=t=0`. It is distinct from evaluating RW12 there.
The product and inverse formulas RW15 have the correct shifted basepoints.
The adjoining scaling proof provides the entire finite-matrix construction
and distinguishes it from a numerically evaluated nonpolynomial cochain map.

## Twisted dual and the actual tau-base moment line

The source moment representation is `U_p:L_k -> L_k`, multiplier `p^k`.
Forward dilation `L_p=U_{1/p}`, `a=log p` with the positive real logarithm,
therefore has multiplier `exp(-ka)`. The factor in RW16 agrees with this
already specified line; it is not inferred from finite-field cardinality
or chosen to normalize a metric.

For a coefficient column functional, the semilinear twisted dual is

`ell(t) -> exp(-ka) C_a(u,t)^{-T} ell(t+ua)`.

Evaluation against `C_a(u,t)v(t+ua)` gives RW20 exactly. Composition is
correct because `(AB)^{-T}=A^{-T}B^{-T}`, with the same shifted parameter
as RW15. Its derivative at zero is
`u partial_t+A(t)^T-kI`. At the special fibre, taking inverse dilation
gives `p^k(p^A)^{-T}`, precisely the tau-base right-adjoint action obtained
by precomposition with the inverse source action. This verifies the
representation transported to the dual; it does not assume an additional
global identification with the original unit-bearing arithmetic pairing.

## Residue pairing and arithmetic-unit scope

The difference of the fractions in RW22 starts at degree at most `S^-2`,
so the residue matrix is t-independent. Its anti-triangular unit
antidiagonal gives the stated determinant, and multiplication by S in
`C[S]/(chi-t)` gives `A(t)^T S=S A(t)`. Transposing
`R A(t)=(kI-A(epsilon t))R` and multiplying by S proves

`A(t)^T(R^T S)+(R^T S)A(epsilon t)=k R^T S`.

This checks RW23 without a transpose-order or parameter-sign loss.
The pairing is the specified complex-bilinear polynomial residue pairing.
The original arithmetic denominator g requires its full Taylor unit and
the actual cyclic inclusion eta; the root note explicitly retains both.
Its identification of the moment-weight action is therefore legitimate
without a claim that this unit is globally invertible on every deformed
fibre. No positive Hermitian metric, positive residue sign, or metric upper
estimate is inferred from RW19--23.

The accepted result is a concrete reflection/weight transport on the
original deformation over the tau-base program. It does not delete a
support mask, pass to the generic support skeleton, omit nilpotent jets,
or substitute finite-field Frobenius for the original theta action.

## Review provenance

Reviewed root note SHA-256:
`111F4C3EA74FA3985352D4A29A65826EE10C883C18DE20230F54A7B9F15472F2`.

Controlling tau-base source:
`workspace:/output/split_zero_rh_tandem_2026-09-12/sources/Tau_Base_Cohomology_2026-09-12/NOTE.md`,
SHA-256 `D03E71AD18F187BD89880CB8CA6FC9C5D6F260B3DE8E8E5702C27DB97E7B63C3`.
Its equations (27)--(43) supply the actual adjunction, moment line,
scaling, and unit-bearing residue morphism. The independently written
scaling note in sibling `f1_scaling_frobenius` pins all other full source
reads and proves the flow underlying RW14. This review adds no numerical
fixture result; those checks are the parent's separate activity.
