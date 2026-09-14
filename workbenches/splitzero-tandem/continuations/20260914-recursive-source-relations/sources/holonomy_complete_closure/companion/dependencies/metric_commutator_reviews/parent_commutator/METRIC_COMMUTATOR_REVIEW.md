# Independent review of the actual-metric commutator transfer

## Captured source and finding

The complete `ACTUAL_METRIC_COMMUTATOR_TRANSFER.md` was read and copied without modification to `ACTUAL_METRIC_COMMUTATOR_TRANSFER_CAPTURE.md`: 4,413 bytes, SHA256 `055d9ab41d454ff8b196d83e061df3e37c9bd50cbd87636e207f3bc7c7f2bfe2`.

**No mathematical correction was found.** The adjoint order in the unconjugated difference, the direction of the square-root isometry, the plus sign in the Hermitian error, the positive-sum Sylvester solution, and the allowance `alpha^-1` are correct. The proof keeps the two given metrics throughout. It does not conclude that their norms agree on all vectors when their control radii agree.

All nine finite methods passed in ordinary and optimized Python. Each of three substantive mutations failed its intended equality, without errors, in both modes. The paired machine receipts are byte-identical. Runs were sequential.

All 28 previously sealed SC artifacts and all 20 previously sealed quotient-compensation artifacts verified unchanged before, during and after the replay. The inherited seals are `946124f26860a285691780949bcb6967c280c8bb18956f0e86c1accfd93d77da` and `2d3c57653a9fd5806f21fa9d8dfbfdffe13446487de3fce7040ff827e72ba87b`. Bytecode generation was disabled. No owner file was edited.

## Complete written proof review

### The two actual adjoints and the unconjugated difference

Let `T^dagger=G^-1 T*G`. The `H=GC` adjoint is `C^-1 T^dagger C`, with exactly this factor order. Consequently

`C X_H=T^dagger C+CT=X_G+T^dagger B+BT`.

Subtracting `C X_G` gives `T^dagger B-BT^dagger`, not its negative. Multiplication by `C^-1` gives the displayed `X_H-X_G=C^-1[T^dagger,B]`.

This is an identity in the original coefficient space. By itself it is not a comparison of the norms taken in different metrics. The next explicit map supplies that comparison.

### The square-root isometry and the Hermitian error

The actual positive comparison has a unique positive `G`-self-adjoint square root `S`. Since `S*G=GS` and `S²=C`, one has `S*GS=GC=H`. Thus `S` maps `(E,H)` isometrically to `(E,G)` and has inverse `S^-1`. No source metric, mass, or coefficient frame has been replaced.

Conjugation through this map gives

`Y_H=S X_H S^-1=S^-1 T^dagger S+STS^-1`.

For `Z=[S,T]S^-1=STS^-1-T`, its `G`-adjoint is

`Z^dagger=S^-1[T^dagger,S]=S^-1 T^dagger S-T^dagger`.

Therefore `Y_H-X_G=Z+Z^dagger`, with a **plus** sign. Both control radii are now evaluated in one explicitly related observation: `epsilon_H=||Y_H||_G` and `epsilon_G=||X_G||_G`. The operator-norm reverse triangle inequality gives the first bound, and equality of an operator's norm and its adjoint norm gives the second:

`|epsilon_H-epsilon_G| <= ||Z+Z^dagger||_G <= 2||Z||_G`.

The retained Hermitian sum can be strictly smaller than the latter allowance. It is not being replaced by the size of the whole generator.

### The Sylvester solution and the general norm allowance

The identity

`S[S,T]+[S,T]S=[S²,T]=[C,T]=[B,T]`

is obtained by expanding all four products. For `K=[B,T]`, define

`Y=integral_0^infinity exp(-rS) K exp(-rS) dr`.

Positive `G`-self-adjointness of `S` gives `||exp(-rS)||_G<=exp(-r sqrt(alpha))`. Thus the integral converges absolutely in operator norm. Writing its integrand as `E(r)`, direct differentiation gives `E'(r)=-S E(r)-E(r) S`, retaining both minus signs. Integration therefore yields `SY+YS=K`: the value at zero is `K`, and the term at infinity is zero. In a spectral calculation of the same operator, every scalar denominator is `s_i+s_j>0`; this proves uniqueness. Hence this integral is the already displayed commutator `[S,T]`.

Submultiplicativity and integration give

`||[S,T]||_G <= ||[B,T]||_G/(2 sqrt(alpha))`.

The same spectral lower bound gives `||S^-1||_G<=alpha^-1/2`. Combining these with the preceding Hermitian-error bound leaves precisely

`|epsilon_H-epsilon_G| <= alpha^-1 ||[B,T]||_G`.

This is the **general written argument**, not an extrapolation from the finite fixtures. Its `alpha` is the admitted actual `1-eta_per-eta_tail`; neither discrepancy term is removed. No numerical value or uniform arithmetic estimate for that actual discrepancy is supplied by this review.

### Original generator, unit and rank-one term

Since the centering term is scalar,

`[B,T]=[B,A]+t[B,R]`.

The complex parameter is `t`, not its conjugate; the conjugate appears only when taking adjoints. For the original `R=e0 ell`, the exact action is

`[B,R]x=(B e0)ell(x)-e0 ell(Bx)`.

Both terms and both original maps remain. No unit vector length or total source mass is divided out. This supplies the final one-sided estimate for the original theta radius from the actual `H` radius.

### Arbitrary coordinates and zero-error comparisons

Under the stated invertible coordinate map, direct multiplication gives `C'=U^-1CU`, `B'=U^-1BU` and `(T')^dagger=U^-1T^dagger U`. The matrix `U^-1SU` squares to `C'`; its positivity and self-adjointness are measured in `G'=U*GU`. Uniqueness therefore identifies it as the actual square root in those coordinates. Every displayed identity transforms by the same similarity. The coordinate map is an isometry between the two representations of each original metric, so the norm bounds are unchanged.

If `[B,T]=0`, the unique Sylvester solution gives `[S,T]=0`. Taking the appropriate `G`-adjoints also gives `[T^dagger,B]=[T^dagger,S]=0`. Thus `X_H=X_G` and `Y_H=X_G`, which proves equality of the two radii despite the metrics themselves being different. This handles nonscalar commuting comparisons as well as scalar rescalings.

## Exact finite verification

The checker constructs positive square roots with specified positive rational eigenvalues. In the original fixture coordinates, `G=7 V*V`, `S=V^-1 D V`, `C=S²` and `H=GC`. The original mass-seven observation is explicitly `sqrt(7)V`. Positivity and the admitted bounds are checked against the actual eigenvalues of `D²`.

Two fixtures use the original increasing-power companion matrix of `(S-1)²(S+2)²`, with both double-root blocks retained. A nonscalar positive comparison commutes with the centered companion generator at `t=0`. The literal `t e0 ell` term, with complex nonzero `t`, produces the separate noncommuting fixture. The source Gram contains nonidentity weights and complex cross terms. Neither repeated factor is replaced by a square-free factor.

A separate two-dimensional finite-control fixture supplies exactly evaluable norms. It is explicitly not an asserted arithmetic packet. In its retained observation,

- `epsilon_G=2`;
- `epsilon_H=34/15`;
- `||Z+Z^dagger||_G=4/15`;
- `2||Z||_G=4/3`;
- `||[B,T]||_G=1`;
- `||[S,T]||_G=1/2` and `||S^-1||_G=4/3`.

Thus the Hermitian error is a strictly sharper allowance in an exact example, and the reverse triangle bound is attained there. The final general commutator allowance also holds in this fixture. The general result nevertheless rests on the written integral proof above. The finite bound fixtures use an explicit zero tail discrepancy; they do not assert that the actual arithmetic tail discrepancy vanishes.

A fourth fixture uses a nonidentity scalar rescaling and an arbitrary retained rank-one parameter. Its control error is exactly zero while its two metrics remain different.

Nine methods verify: the exact source and inherited pins; positive actual Grams and square root; both adjoints and the unconjugated identity; the isometry and full Hermitian error; Sylvester multiplication and the exact positive-sum integral entries; the exact norm witness; arbitrary non-unit complex coordinate covariance; nonscalar/scalar zero-error cases; and the original unit, rank-one terms, centering and source mass.

Three mutations reverse the adjoint commutator, replace the Hermitian sum by its difference, or change the positive-sum Sylvester denominator. They fail the intended equations rather than deliberately raising an unrelated exception. `EXECUTION_RECEIPT.json` binds all ordinary/optimized records and complete logs.

## Scope

This review makes no owner-source edits, remote writes, Lean executions, contour evaluations, boundary-sampling claim, or new arithmetic estimate. It does not duplicate the owner's separate LC review. The result is an independently checked pointwise comparison of the two metrics actually specified by the source.
