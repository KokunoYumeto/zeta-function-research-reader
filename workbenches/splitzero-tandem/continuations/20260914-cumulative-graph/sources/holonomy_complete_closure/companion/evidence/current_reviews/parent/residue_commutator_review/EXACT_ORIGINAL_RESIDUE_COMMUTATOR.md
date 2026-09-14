# Exact norm of the original residue commutator

This is a local, independent finite-dimensional review of the residue term in
`period_laplacian/ACTUAL_METRIC_COMMUTATOR_TRANSFER.md`. It preserves the two
actual positive source Grams and the original residue operator. It neither
selects a replacement metric nor supplies an evaluated arithmetic estimate or
a uniform source bound. The accompanying small exact fixtures are synthetic
algebraic checks, not evaluations of the theta or sampled source data.

## Objects and conventions

Let `G` and `H` be the two positive Hermitian Grams on the same finite complex
source `E`, and put

`B = G^{-1}(H-G)`, `C = I+B = G^{-1}H`.

Use the convention `<u,v>_G = u*Gv` (conjugate-linear in the first argument),
and let `dagger` denote the corresponding adjoint. Then

`GB = H-G = B*G`, so `B^dagger = B`.

Keep `x=e_0`, the original constant/unit vector, and the original complex
linear coefficient functional `ell`. Set

`y=G^{-1}ell*`, so `ell(v)=<y,v>_G` and `R=x y^dagger = e_0 ell`.

No norm of `x` or `y` is set to one. In particular, `||x||_G^2=e_0*G e_0`
and `||y||_G^2=ell G^{-1}ell*` retain the source masses. The full complex row
`ell` is retained, without removing its phase or any relative coefficient
phases. Neither `A` nor a defining source polynomial needs distinct roots.

To avoid confusing a scalar trace with the source generator called `T` in
the cited note, the scalar below is called `T_res` (it is the `T` of the
quadratic norm formula).

## Rank-two factorization, including the signs

Define maps from auxiliary `C^2` to `E` by the columns

`U=[Bx,x]`, `V=[y,-By]`.

Since `B` is self-adjoint,

`UV^dagger v = Bx <y,v>_G - x <By,v>_G`

`             = Bx ell(v) - x ell(Bv) = [B,R]v`.

Thus `K=[B,R]=UV^dagger`, with rank at most two. This auxiliary factorization
does not identify, replace, or normalize either source metric.

Introduce the exact scalar moments

`a=||Bx||_G^2`, `c=||x||_G^2`, `d=||y||_G^2`, `f=||By||_G^2`,

`p=<x,Bx>_G`, `r=<y,By>_G`.

Self-adjointness gives `conj(p)=<Bx,x>_G=<x,Bx>_G=p` and likewise
`conj(r)=r`. These two moments are real, even for complex source data. Hence

`P=U^dagger U = [[a,p],[p,c]]`,

`Q=V^dagger V = [[d,-r],[-r,f]]`.

In particular, the two off-diagonal entries of `Q` have minus signs. Direct
multiplication, with no cross term discarded, gives

`T_res = tr(PQ) = ad+cf-2pr`,

`Delta = det(PQ) = (ac-p^2)(df-r^2)`.

Equivalently,

`T_res = ||Bx||_G^2 ||y||_G^2 + ||x||_G^2 ||By||_G^2`

`        - 2 <x,Bx>_G <y,By>_G`,

`Delta = (||Bx||_G^2 ||x||_G^2 - <x,Bx>_G^2)`

`        (||y||_G^2 ||By||_G^2 - <y,By>_G^2)`.

The subtraction is essential; replacing it by addition is already wrong
for a nonzero commuting example in the fixtures.

## Exact operator-norm formula

The nonzero eigenvalues, with algebraic multiplicity, of

`K^dagger K = V P V^dagger`

are those of `P V^dagger V = PQ`, by the standard `AB`/`BA` nonzero-spectrum
identity. For completeness, that identity follows from
`det(I+s AB)=det(I+s BA)` for rectangular compatible maps, or from the maps
`A` and `B` on their generalized eigenspaces at each nonzero eigenvalue.
It does not require either map to have full rank.

Although `PQ` need not be Hermitian, its characteristic polynomial equals
that of the positive semidefinite matrix `P^{1/2} Q P^{1/2}`: apply the same
determinant identity in size two to `P^{1/2}` and `P^{1/2}Q`. This also holds
when `P` is singular. Consequently its two eigenvalues are real and
nonnegative, and are exactly

`lambda_+/- = (T_res +/- sqrt(T_res^2-4 Delta))/2`.

It follows in particular that `T_res>=0`, `Delta>=0`, and
`T_res^2-4 Delta>=0`. Independently, the two factors of `Delta` are
nonnegative Gram determinants by Cauchy--Schwarz, and
`T_res=tr(K^dagger K)` is the squared Hilbert--Schmidt norm.

The largest eigenvalue of `K^dagger K` is `lambda_+`; any additional source
eigenvalues are zero. Therefore the requested exact norm is

**`||[B,R]||_G^2 = (T_res + sqrt(T_res^2-4 Delta))/2`.**

All square roots in this identity are the nonnegative real square roots.

### Degenerate cases are part of the formula

- If `K=0`, then `T_res=0` and `Delta=0`; the formula returns zero. This
  includes `B=0`, scalar `B`, commuting non-scalar `B`, and the abstract
  algebraic cases `x=0` or `ell=0`. The original source unit is not replaced
  by zero in the application.
- If `Delta=0` and `T_res>0`, the singular-value squares are `T_res` and
  zero, so `K` has rank one and its norm is `sqrt(T_res)`. There is no
  division by a Gram determinant, vector norm, or mass.
- If `Delta>0`, `K` has rank two. When the discriminant is zero, both
  nonzero singular-value squares are `T_res/2`, with multiplicity two;
  that repeated value must not be discarded.
- In a one-dimensional (`q=1`) source, both `B` and `R` are scalar
  endomorphisms, so `[B,R]=0`. More explicitly, write `B=bI`, with `b`
  real. Then `a=b^2c`, `p=bc`, `f=b^2d`, and `r=bd`, giving
  `T_res=Delta=0`, for arbitrary original masses and complex `ell`.
  There is no exception requiring a preferred basis or normalized unit.

Repeated roots of the defining source polynomial cause no obstruction:
the proof only uses the original vector space, functional, and Grams. It
does not diagonalize the source generator `A` or use a simple-root residue
expansion. Repeated roots of the singular-value quadratic are explicitly
retained above.

## Arbitrary coordinate covariance

For any invertible complex coordinate matrix `W`, adopt old coordinates
`v=W v'`. Then the same original objects have matrices

`G'=W*GW`, `H'=W*HW`, `B'=W^{-1}BW`,

`x'=W^{-1}x`, `ell'=ell W`, `y'=(G')^{-1}(ell')*=W^{-1}y`.

The last equality follows by substituting the displayed congruence for
`G'`; it is not a new choice of residue representative. Hence

`R'=W^{-1}RW`, `[B',R']=W^{-1}[B,R]W`,

`U'=W^{-1}U`, `V'=W^{-1}V`.

Directly, `(U')^dagger_{G'}U'=U^dagger_G U=P`, and the same statement holds
for `Q`. Thus all six moments, `T_res`, `Delta`, both singular-value
squares, and the stated norm are invariant. This includes nonunitary and
complex changes of coordinates; `x'` need not still be the first coordinate
column, because it is the same original unit expressed in the new frame.

## Insertion into actual-metric transfer

Use the retained comparison lower bound `C>=_G alpha I`, with the same
already admitted `alpha>0`, and the original generator
`T_gen=A+tR-kI/2`. The reviewed transfer note gives

**`|epsilon_H(t)-epsilon_G(t)| <= alpha^{-1}
||[B,A]+t[B,R]||_G`.**

The exactly evaluable residue contribution itself is

`||t[B,R]||_G = |t| sqrt((T_res+sqrt(T_res^2-4 Delta))/2)`.

If a separated allowance is wanted, the triangle inequality gives the
weaker consequence

`|epsilon_H(t)-epsilon_G(t)| <= alpha^{-1}(`

`    ||[B,A]||_G + |t| sqrt((T_res+sqrt(T_res^2-4 Delta))/2))`.

The primary retained quantity remains the full
`||[B,A]+t[B,R]||_G`. It keeps cancellation between the generator and
residue commutators and can be strictly smaller, including zero when the
two separately nonzero commutators cancel. The residue formula is exact;
neither the transfer upper bound nor its triangle-inequality separation is
asserted to be an equality.

This structural evaluation procedure is not an evaluated source arithmetic
allowance, a uniform estimate, a replacement-metric argument, or a public
publication claim. No Lean execution is claimed.

## Independent exact fixture scope

`verify_residue_commutator.py` runs small checks sequentially using exact
SymPy arithmetic only. Every finite example checks positive actual `G,H`,
`B^dagger=B`, the original `R=x ell`, the signed factorization, all moments,
the full characteristic polynomial of `K^dagger K` with zero multiplicities,
the quadratic formula, and the corresponding rank. The examples cover
`q=1`, non-scalar commuting comparison, nonzero rank one, complex rank two
with unequal masses, zero comparison, repeated singular values, a repeated
source root, and a nonunitary complex coordinate transformation. An exact
`C[z]/(z^2)` fixture also checks nonzero `[B,A]` and `[B,R]` cancelling at
`t=1`. These are regression checks for this proof, not claims about evaluated
arithmetic in the publication's source family.
