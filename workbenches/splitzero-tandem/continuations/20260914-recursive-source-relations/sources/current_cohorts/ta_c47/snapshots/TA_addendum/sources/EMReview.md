# Independent review of the canonical metric extension

Date: 2026-09-13. This records the independent calculation supplied while
the root proof `MAIN_METRIC_EXTENSION.md` was being written. A final seal,
if appended, identifies the complete root artifact read and accepted.
The accepted input is TA1--24 with H=h kappa, both factors retaining their
full actual zero orders, and gcd(h,kappa)=1. This is local written
mathematics only; no new zero, metric, normalization, numerical certificate,
Lean execution, or remote change is asserted.

## 1. Source spaces, cutoffs, and notation

Write d=deg h, K=deg kappa, D=d+K, and take N>=D-1. The source coefficient
space is `P_N=C[s]_{<=N}` (with `P_n=0` for n<0) and its original positive form

`<F,G>_H=integral_R conjugate(F(1/2+iy))G(1/2+iy) w_H(y) dy`,

where `w_H=|g/H|^2/(2 pi)`. Let pi_H be remainder modulo H. Its canonical
least-source-norm section is R_H,N and its coefficient-quotient metric is
G_H,N. Every G without a superscript in the calculation below is in
coefficient coordinates. The source function of F is `F(D_x)F_H`.

Similarly retain R_h,N-K and G_h,N-K for the original weight
`w_h=|kappa|^2 w_H`, and R_kappa,N-d and G_kappa,N-d for
`w_kappa=|h|^2 w_H`. No weight is normalized to total mass one. Both
quotient cutoffs are sufficient because N-K>=d-1 and N-d>=K-1.

The monic polynomials give the literal isomorphism

`T:E_h direct_sum E_kappa -> E_H`,
`T(P,Q)=kappa P+h Q`.

It is well defined. If its value vanishes modulo h kappa, reduction
modulo h and then kappa, using coprimeness, forces P=Q=0 in the
respective quotient algebras. Equal dimensions then prove surjectivity.

## 2. The complete mixed block is an original source pairing

TA23 applied to both factors gives

`R_H,N T(P,Q)=kappa R_h,N-K P+h R_kappa,N-d Q`.

This uses linearity of the canonical section as well as both exact
restriction identities. Thus, suppressing the now fixed cutoffs,

`T^* G_H T = [[G_h,C],[C^*,G_kappa]]`,

where, in any specified coefficient bases,

`C_ij=integral conjugate(kappa R_h e_i)(h R_kappa e_j) w_H`,

or equivalently

`C_ij=<(R_h e_i)(D_x)F_h,(R_kappa e_j)(D_x)F_kappa>_{L^2(dx)}`.

Both source identities follow from the original Mellin transforms.
The integral retains the complex phase of `conjugate(kappa)h`, every
source mass, and all the cross terms. Neither orthogonality of the two
packet blocks nor equality of their total masses is assumed.

## 3. Resultant and Schur determinant with full multiplicities

In ascending monomial bases, the columns of T are
`kappa, s kappa, ..., s^{d-1}kappa`, followed by
`h,s h,...,s^{K-1}h`. This is the coefficient Sylvester map, with

`det T=Res(h,kappa)`

for the convention `Res(h,kappa)=product_{h(alpha)=0} kappa(alpha)`
with multiplicity and monic h. To check the convention explicitly when
both root sets are distinct, evaluate the columns at the h-roots followed
by the kappa-roots. The two diagonal evaluation blocks have determinants
`Res(h,kappa) det V_h` and `Res(kappa,h) det V_kappa`; the full evaluation
matrix has determinant
`(-1)^{dK}Res(h,kappa)det V_h det V_kappa`.
Using `Res(kappa,h)=(-1)^{dK}Res(h,kappa)` gives the stated sign.
Both sides are polynomials in the original coefficients, so the identity
holds with repeated roots as well. In particular coprimeness makes it
nonzero, without removing any multiplicity.

Let

`S=G_kappa-C^* G_h^{-1} C`.

Completing the square in the full positive form proves that S is positive
definite and

`det G_H = det G_h det S / |Res(h,kappa)|^2`.

The squared absolute determinant here is essential: the Gram pullback
is Hermitian, not a bilinear determinant transformation.

## 4. The actual quotient measured by the Schur complement

Define Gamma as the canonical quotient metric of the SAME source P_N with
weight w_H under the map `pi_kappa:P_N -> E_kappa`. Its relation space
is exactly

`ker pi_kappa=kappa P_{N-K}`.

This is an existing least-source-norm construction with the actual
source and a specified observation, not an arbitrary positive matrix.
It has cutoff N, not N-d, and source weight w_H, not w_kappa. Write
its canonical section as `R^{w_H}_{kappa,N}`. Put

`U=M_{h mod kappa}:E_kappa -> E_kappa`.

The exact projection identity is

`pi_kappa T(P,Q)=U Q`.

Consequently, for fixed Q, allowing P to vary is exactly allowing all old
h-jet coordinates to vary while fixing the kappa remainder to UQ. Taking
the source infimum first over full H representatives and then over P is
the same as taking it over the single complete source fibre
`{F in P_N:pi_kappa F=UQ}`. This proves

`S=U^* Gamma U`.

It is not correct to identify S with bare Gamma in T's Q coordinates;
the h-unit U is part of the exact quotient map.

There is also an explicit minimizing source map. The unique minimizing
old coefficient is

`P_*=-G_h^{-1} C Q`.

The corresponding polynomial and source function are

`R^{w_H}_{kappa,N}(UQ)=kappa R_h P_*+h R_kappa Q`,

`(R_h P_*)(D_x)F_h+(R_kappa Q)(D_x)F_kappa`.

Their squared original norm is `Q^* S Q`. Thus the calculation identifies
the minimizer, its exact source realization, its observation, and the full
relation space, not only an abstract Schur complement.

In quotient-algebra terms the second stage is
`E_H / ((kappa)/(H)) = E_kappa`. The source relation space contains all
old H relations since `(H)` is contained in `(kappa)`. More explicitly,
the orthogonal decomposition at the source level is

`kappa P_{N-K}=kappa R_h(E_h) + H P_{N-D}`,

with the two summands orthogonal for w_H by the defining minimizer
property of R_h and the identity w_h=|kappa|^2w_H. This is another
direct explanation of why the Schur minimization removes all and only
the allowed old directions and original relation directions.

Since `det U=Res(kappa,h)`, the determinant identity also gives

`det S=|Res(h,kappa)|^2 det Gamma`,
`det G_H=det G_h det Gamma`.

The cancellation in the final formula is justified only after retaining
both the Sylvester factor in T and the full h-unit in the quotient
coordinate. Neither factor was set to one.

## 5. Full physical-jet conversion and its source observation

Let `U_H=M_upsilon_H`, `U_h=M_upsilon_h`, and
`U_kappa=M_upsilon_kappa`, all multiplication by the actual full Taylor
units. The coefficient and physical-jet metrics obey

`G_H=U_H^* G_H^jet U_H`,

and the analogous identities for h and kappa at their indicated cutoffs.
The physical packet isomorphism is

`J=U_H T diag(U_h^{-1},U_kappa^{-1})`.

Its two columns are precisely the two extension-by-zero maps in the
full CRT jet decomposition: identity on the indicated old or added
block and zero on the other through every required order. This follows
from `upsilon_h=(kappa mod h)(upsilon_H mod h)` and
`upsilon_kappa=(h mod kappa)(upsilon_H mod kappa)`.

Thus the physical mixed block is
`C^jet=U_h^{-*} C U_kappa^{-1}`, and its Schur complement is

`S^jet=U_kappa^{-*} S U_kappa^{-1}`.

The actual physical kappa observation on the same extended source is

`F -> J_kappa(F(D_x)F_H)`
`   =V pi_kappa F`, where `V=M_{upsilon_H mod kappa}`.

Its kernel is still kappa P_{N-K}, and its canonical quotient metric is

`Gamma_free^jet=V^{-*} Gamma V^{-1}`.

Because U_kappa=V U, the exact Schur identity becomes
`S^jet=Gamma_free^jet`. In particular, in physical jet coordinates it
is literally the metric for fixing the added jets and leaving the old
jets free. The source remains the degree-N window generated by F_H;
it has not been replaced by the smaller window generated by F_kappa.

For completeness, in the same monomial coordinate conventions,
`|det J|=1/|Res(h,kappa)|`. Indeed the restrictions of U_H have product
determinant det U_H by CRT, whereas
`det U_h det U_kappa=det U_H Res(h,kappa)Res(kappa,h)`.
Combining with det T gives the assertion. Therefore the corresponding
physical determinant identity is

`det G_H^jet=|Res(h,kappa)|^2 det G_h^jet det Gamma_free^jet`.

These determinant statements retain full unit transformations. They do
not infer that the packet splitting is orthogonal under the canonical
source metric.

## 6. Degenerate case and scope

If kappa=1, K=0 and E_kappa is zero. All second blocks, residue-free
observations, and their relation-quotient spaces have dimension zero;
their determinants are one. The assertion reduces to the identity on
the old h packet. At the smallest cutoff N=d-1, interpret the empty
second polynomial source as `P_{-1}=0`. No inverse of a nonexisting
positive-dimensional block is required.

Every matrix here is an actual finite-dimensional canonical source or
quotient metric, with strict positivity from the original source norm.
This proof makes no inference about a completed boundary range, no
uniform estimate as the cutoff or packet varies, and no new zero
existence claim. All repeated-root and mass data remain in the stated
polynomials, full units, source sections, and integrals.

## 7. Full review of the root EM1--12 proof

The complete root `MAIN_METRIC_EXTENSION.md` was read after it became
available, including the actual arithmetic projection, moment-determinant
calculation, mixed-cost statement, K=0 case, and provenance/scope. Its
displayed equations EM1--12 agree with the preceding independent
derivation. The following additional root calculations were checked.

In EM6, J_H is the actual full jet map on the H-torsion submodule of
the original theta quotient. Restriction of those jets to the kappa
block, followed by the original sigma_kappa, is a projection onto its
kappa-primary submodule. Its kernel is exactly the h-primary submodule,
because the packet factors are coprime with their full orders. On a
source P(D_x)F_H the kappa observation is precisely
`(upsilon_H mod kappa)[P]_kappa`. Thus the projection has exactly the
source and unit coordinates used for Gamma and its physical version;
no other arithmetic cohomology group has been substituted.

The root's direct proof of det T uses the monic division basis
`[1,...,s^{d-1},h,...,h s^{K-1}]`. Its coefficient change has determinant
one, and T has diagonal blocks `M_{kappa mod h}` and identity in this
basis. The former has determinant Res(h,kappa), including each root
order. This independently verifies the sign convention in EM7 without
a simple-root assumption or a choice of determinant normalization.

For the root's moment determinants, define Delta_f,n on the n source
monomials and use Delta_f,0=1. At an onto cutoff n-1, so n>=deg f,
the monic basis of low quotient powers followed by f times relation
powers has change-of-basis determinant one. The relation Gram is the
original weight `|f|^2 w_f=w_1`, and its dimension is n-deg f.
Taking the Gram Schur complement therefore proves exactly

`det G_f,n-1^coef=Delta_f,n/Delta_1,n-deg f`.

For H at N and h at N-K, both relation dimensions are N-D+1.
Their full common denominators cancel, giving the moment ratio in EM11.
Alternatively, the relation kernel in EM4 has basis kappa times
`1,...,s^{N-K}` and weight `|kappa|^2 w_H=w_h`. Its Gram determinant
is Delta_h,N-K+1, directly proving the same formula for det Gamma_N.
Both routes retain the original w_1 seed and all unnormalized masses.
The minimal cutoff N=D-1 uses a zero-dimensional original relation
space and determinant one, not a negative-index determinant.

Finally the operator `B^{-1}C^*A^{-1}C` in EM12 is self-adjoint and
nonnegative for the existing B form because its B-pairing is given by
the Hermitian nonnegative matrix `C^*A^{-1}C`. Strict positivity of
the actual Schur complement S gives every eigenvalue strictly below
one. Thus the product of the exact 1-minus-eigenvalue factors is the
displayed determinant ratio, and
`Q^*(B-S)Q=(A^{-1}CQ)^*A(A^{-1}CQ)` is the precise original source
cost of the optimizing old component. No Euclidean self-adjointness
or vanishing of C is silently assumed.

Two local notation clarifications were reported before the final seal:
the determinants of U_h and U_kappa must be multiplied as scalars,
rather than writing a matrix product of potentially different sizes;
and the generic moment-ratio formula uses the onto cutoff n>=deg f.
Every substantive calculation and every actual application already
satisfies these conventions.

## Final independent acceptance

The revised determinant-product phrase and the explicit condition
n>=deg f were reread on 2026-09-13. Both local notation comments above
are resolved; they remain recorded only as the review history.

The exact accepted root proof is `MAIN_METRIC_EXTENSION.md`, SHA-256:

`8963772b34c853ed6e3a7931830934c1928f8864a8e667d0cf63ec19c0b4dc6a`.

Final disposition: accept EM1--12 and all accompanying scope statements,
with no outstanding mathematical correction. The review verifies the
actual mixed source Gram, the quotient and its exact minimizer behind
the Schur complement, the full resultant and physical-unit conversions,
the original moment-determinant formula, the mixed source cost, and the
empty-added-packet case. It certifies written mathematics only, with
no numerical or Lean replay, no new zero-location or existence claim,
and no uniform estimate beyond the displayed exact finite identities.
