# Exact commutator transfer between the two actual source metrics

This calculation uses the original theta quotient Gram `G` and its actual
periodized/sampled Gram `H` in FC1–23. It does not select a replacement metric
or discard either observation. All assertions below are pointwise in the
existing finite source and its retained parameter. Independent finite review
is separate; no new arithmetic estimate or Lean execution is asserted here.

Write the existing positive metric comparison as

`C = G^{-1}H = I+B`,  `alpha I <=_G C <=_G beta I`,

with the already admitted `alpha=1-eta_per-eta_tail>0` and
`beta=1+eta_per`. Adjoint `dagger` and operator norms in this note use `G`.
Keep `T=A+tR-kI/2`, `R=e_0 ell`, the original unit and coefficient functional.
The two original control operators and radii are

`X_G=T^dagger+T`, `X_H=C^{-1}T^dagger C+T`,
`epsilon_G=||X_G||_G`, `epsilon_H=||X_H||_H`.

These definitions directly give the previously retained identity

`C X_H = X_G + T^dagger B + B T`.

Subtract `C X_G`, without commuting any factors, to obtain the sharper exact
form

**`X_H-X_G = C^{-1}[T^dagger,B]`.**

Thus a scalar metric rescaling contributes zero to this difference. The size
of the generator alone does not measure the actual metric-transfer error.

## The exact isometry and the Hermitian error

Let `S=C^{1/2}` be the unique positive `G`-self-adjoint square root of this
actual comparison. The map `S:(E,H)->(E,G)` is an isometry because
`S* G S=G S^2=G C=H` in the original matrix coordinates.
Its inverse is `S^{-1}`. Both original metrics and their source maps remain
specified; this is an explicit comparison morphism between them.

Conjugating only for this comparison gives

`Y_H=S X_H S^{-1}=S^{-1}T^dagger S+S T S^{-1}`,

`Y_H-X_G = Z+Z^dagger`,  `Z=[S,T]S^{-1}`.

The order in the second summand follows from
`Z^dagger=S^{-1}[T^dagger,S]`. Consequently the exact operator-norm
reverse triangle inequality proves

**`|epsilon_H-epsilon_G| <= ||Z+Z^dagger||_G <= 2||[S,T]S^{-1}||_G`.**

The first retained expression can be strictly sharper than dropping its
cross term. It is expressed wholly in the two actual Grams and generator.

## A scalar allowance depending on the actual commutator

The matrix `Y=[S,T]` satisfies the exact Sylvester equation

`S Y+Y S=[C,T]=[B,T]`.

Since `S>=_G sqrt(alpha) I`, the same equation has the convergent solution

`Y=integral_0^infty exp(-rS)[B,T]exp(-rS) dr`.

Indeed, differentiating the integrand and integrating retains its value
`[B,T]` at `r=0` and its zero limit at infinity. Uniqueness follows in a
`G`-orthonormal spectral frame from the strictly positive sums of the two
eigenvalues of `S`. This frame calculation does not change either metric.
The spectral bound for its exponential gives

`||[S,T]||_G <= ||[B,T]||_G/(2 sqrt(alpha))`,

and `||S^{-1}||_G<=alpha^{-1/2}`. Hence

**`|epsilon_H-epsilon_G| <= alpha^{-1}||[B,T]||_G`.**

In particular,

**`epsilon_G(t) <= epsilon_H(t)+alpha^{-1}||[B,A]+t[B,R]||_G`.**

Every rank-one term remains explicit:

`[B,R]x = (B e_0)ell(x)-e_0 ell(Bx)`.

There is no division by a unit norm or source mass. The usual rough bound
`||[B,T]||_G<=2||B||_G||T||_G` remains available, but the displayed actual
commutator is the quantity to calculate first. This improves the structural
dependence, not a claimed numerical or uniform arithmetic upper bound.

## Coordinate covariance and zero-error cases

For an arbitrary invertible coordinate map `U`, the same original objects
transform by `G'=U*GU`, `H'=U*HU`, `T'=U^{-1}TU`,
`B'=U^{-1}BU`, and `S'=U^{-1}SU`. The last matrix is positive and
self-adjoint in `G'`, so uniqueness identifies it as the correct square
root there. All commutators transform by the same similarity, and every
norm and stated bound is unchanged.

If `[B,T]=0`, taking `G`-adjoints also gives `[T^dagger,B]=0`. Thus
`X_H=X_G`, `Y_H=X_G`, and `epsilon_H=epsilon_G` exactly, including
nonidentity comparisons commuting with the original generator. This is an
identity on the actual finite source, not a declaration that its two norms
are the same on all vectors.

For the FC sampled boundary expression for `epsilon_H`, the last boxed bound
is another route back to the original theta control and hence to its existing
parabola. It retains the required source discrepancy through the actual
commutator, instead of assigning it the size of every generator component.
