# Independent derivation of every finite-cutoff pair spectrum

## Reading and source-use ledger

The complete `REAL_PAIR_ALL_CUTOFFS.tex` (RPAC1–15), `REAL_PAIR_COLLISION.tex`, and `REAL_PAIR_ES_RETURN.tex` were read, together with the complete `certify_real_pair.py`, its saved `REAL_PAIR_CERTIFICATE.json`, `check_real_pair_collision.py`, and `check_real_pair_root.py`. RPCJ1–12 supply the original analytic object, the exact moment derivatives, the unchanged weights and center, and the actual constants. RPCJ14–23 supply the prior degree-three calculation against which this calculation is checked. RPE1–4 identify the certified original point and the interval inputs. The receipt records SHA-256 source versions. These files are programme derivations, not a relabeling of human literature. Their existing human citations remain with the cumulative article; this review introduces no new literature claim.

## Reciprocal expansion without dropping higher original coefficients

Let `tau=z-z_*` in the unchanged inverse-period coordinate. Every original coefficient `g_j(tau)` is analytic. With `Q(x)=c+d x+e x²` and `P(x)=c3+d2 x+e1 x²+f x³`, coefficientwise substitution gives

\[
\tau^{-2}g(\tau x,z_*+\tau)=Q(x)+\tau P(x)+O(\tau^2).
\]

For any specified coefficient of `x`, only finitely many original `g_j` occur. Terms with `j>=4` contain the factor `tau^(j-2)` after this substitution; their constant and first coefficients in `tau` are zero. Consequently they first enter the stated remainder. This is an exact coefficient argument retaining the original higher moments, not a truncation of the symbol in the theorem.

Because `c>0`, `Q` is invertible as a formal power series in `x`. Its reciprocal and first derivative give

\[
\tau^{n+2}h_n(z_*+\tau)=H_n+\tau K_n+O(\tau^2),\quad
H_n=[x^n]Q^{-1},\quad K_n=-[x^n]P Q^{-2}.
\]

The expression on the left extends analytically to `tau=0`: the exact reciprocal recurrence, after multiplication by `tau^(n+2)`, has analytic coefficients and denominator `g_0/tau²`, which is nonzero at zero. Thus the displayed coefficientwise remainder is a genuine local analytic remainder for each fixed finite cutoff.

The explicit formula, with every coefficient and sign retained, is

\[
H_n=\sum_{k=0}^{\lfloor n/2\rfloor}
\frac{(-1)^{n-k}\binom{n-k}{k}d^{n-2k}e^k}{c^{n-k+1}}.
\]

It follows by expanding `1/(c+d x+e x²)` as a geometric series: to obtain degree `n` from `n-k` factors, choose exactly `k` quadratic factors and `n-2k` linear factors. All terms contributing that degree are present. If `V_n=sum_(j=0)^n H_j H_(n-j)` for `n>=0` and `V_n=0` for `n<0`, then

\[
K_n=-c_3V_n-d_2V_{n-1}-e_1V_{n-2}-fV_{n-3}.
\]

## Complete resonance classification

Set `lambda=|B|/|A|>0` and `theta=R/(2|A||B|)` using the original derivatives; Cauchy–Schwarz gives `-1<=theta<=1`. The original coefficients obey `d=-2 i c lambda theta` and `e=-c lambda²`. The generating identity

\[
\frac1{1-2\theta y+y^2}=\sum_{n\ge0}U_n(\theta)y^n
\]

at `y=i lambda x` proves `H_n=(i lambda)^n U_n(theta)/c`. The generating identity follows by multiplying the recurrence `U_0=1`, `U_1=2 theta`, `U_n=2 theta U_(n-1)-U_(n-2)` by `y^n` and summing. For `theta=cos(phi)`, `0<phi<pi`, the recurrence and its first two values show

\[
U_n(\cos\phi)=\frac{\sin((n+1)\phi)}{\sin\phi}.
\]

The sine addition identity proves the recurrence on the right. At the endpoints the same recurrence gives `U_n(1)=n+1` and `U_n(-1)=(-1)^n(n+1)`. Hence, for every `D>=1`, resonance occurs exactly at the `D` distinct values `theta=cos(k pi/(D+1))`, `1<=k<=D`. This proves the entire zero set: there are no endpoint zeros and the interior sine numerator vanishes exactly at the listed points.

No two consecutive `H_n` can vanish. Indeed, the recurrence `c H_n+d H_(n-1)+e H_(n-2)=0` and `e!=0` would propagate two zeros backwards to `H_0=1/c`, a contradiction.

For later constants one has the exact Cassini identity

\[
H_n^2-H_{n-1}H_{n+1}=\frac{e^n}{c^{n+2}},\qquad H_{-1}=0.
\]

Its initial case is `H_0²=1/c²`. Substituting the recurrence into two successive left sides proves that the latter is `e/c` times the former. Induction proves the identity at every degree. At `H_D=0`, its `n=D-1` case yields

\[
|H_{D-1}|^2=\frac{|e|^{D-1}}{c^{D+1}}.
\]

This also directly proves nonzero `H_(D-1)` on resonance.

## Forward rank, exterior constants, and every singular value

Put `N=D+1`. For `D>=2`, at the collision the entire nonzero part of the forward matrix occupies rows `0,...,D-2` and columns `2,...,D`. Call this square block `C_(D,s)`. Its entries are the full `g_(j-i+2)(z_*) rho_(j+2)/rho_i` for `j>=i` and zero otherwise, `0<=i,j<=D-2`. It is upper triangular with nonzero diagonal `e rho_(i+2)/rho_i`. Thus the original matrix has rank `D-1`, and

\[
\det C_{D,s}=e^{D-1}\frac{\rho_{D-1}\rho_D}{\rho_0\rho_1}.
\]

All entries with coefficient indices `3,...,D`, and therefore all original higher moments entering them, stay in this block. For `D=1`, the limiting forward matrix is zero, of rank zero; use the empty block and empty product of value one only for determinant/exterior conventions.

For invertible `B`, singular-value decomposition gives the exact complementary identity

\[
\|\wedge^r B^{-1}\|=\frac{\|\wedge^{N-r}B\|}{|\det B|}.
\]

Indeed both sides equal the reciprocal product of the `r` smallest positive singular values of `B`. Here `det B=g_0^N` exactly. For `r>=2`, `0<=N-r<=D-1`, so the limiting exterior numerator is strictly positive by the proved rank. Continuity therefore gives

\[
\lim_{\tau\to0}|\tau|^{2(D+1)}\|\wedge^r B_{D,s}^{-1}\|
=\frac{\|\wedge^{D+1-r}B_{D,s}(z_*)\|}{c^{D+1}}>0.
\]

At `r=2` this becomes

\[
E_2=\frac{|e|^{D-1}\rho_{D-1}\rho_D}
{c^{D+1}\rho_0\rho_1},
\]

including `D=1`, when `E_2=c^(-2)`.

If `H_D!=0`, multiply the inverse by `tau^(D+2)`. Exactly its `(0,D)` entry tends to `H_D rho_D/rho_0`; every other entry tends to zero. Thus the first inverse singular value has pole `D+2` and constant `L_1=|H_D|rho_D/rho_0`. The exact exterior norm equals the product of the two largest inverse singular values, so dividing its limit by `L_1` proves that the second has pole `D` and constant

\[
L_2=\frac{|e|^{D-1}\rho_{D-1}}
{c^{D+1}|H_D|\rho_1}.
\]

If `H_D=0`, multiply by `tau^(D+1)`. For `D>=2` the only remaining entries are the full corner block

\[
N_{D,s}=\begin{pmatrix}
H_{D-1}\rho_{D-1}/\rho_0&K_D\rho_D/\rho_0\\
0&H_{D-1}\rho_D/\rho_1
\end{pmatrix}.
\]

Its two nonzero singular values are the limiting first two inverse singular values after this multiplication. Its determinant is nonzero by the no-consecutive-zero proof; both poles are therefore `D+1`. At `D=1` the actual full `2x2` limit is `[[H_0,K_1 rho_1/rho_0],[0,H_0]]`, which agrees with the displayed formula after setting `D=1`, but occupies the full matrix. The Cassini identity gives `|det N_(D,s)|=E_2`, confirming the exterior constant, including `D=1`.

Let the positive singular values of the complete forward block be `gamma_1>=...>=gamma_(D-1)>0`. Singular values depend continuously on matrix entries. Therefore in either case the remaining inverse singular values, in decreasing order, tend exactly to `gamma_(D-1)^(-1),...,gamma_1^(-1)`. There are none when `D=1`. This proves all inverse exponents: `(D+2,D,0,...,0)` off resonance and `(D+1,D+1,0,...,0)` on resonance. For `D=0`, the original scalar inverse is `1/g_0`; its only pole is `2` with constant `1/c`.

All these statements hold for complex approaches in the original `z` coordinate. Multiplication by the indicated integral power of `tau` has the stated entrywise limit; taking norms replaces the power by its absolute value. For `u=1/z`, `tau=-(u-u_*)/(u u_*)` exactly, so a pole of exponent `p` has its original-coordinate constant multiplied by `|u_*|^(2p)`.

## Existing degree-three result recovered exactly

`H_3=-d(d²-2ce)/c^4=-Delta/c^4`, recovering RPCJ16. The full coefficient before imposing resonance is `K_3=Knum/c^4+4c3 Delta/c^5`, where `Knum=2c d e1+2c3 d e+(2ce-3d²)d2-c²f`. On resonance `Delta=0`, this is exactly RPCJ18. Retaining the denominator correction before imposing resonance avoids an invalid general extension of that resonance formula.

## Bounded interval verification at the certified original pair

`check_real_pair_all_cutoffs.py` reads the saved full-series certificate's balls for `c`, `|B|²`, and `R`, verifies the certificate's recorded source hash, and propagates them with 256-bit Arb arithmetic. It does not replace the root box by its center. It proves

\[
\frac{9977939}{10000000}<\theta<\frac{9977941}{10000000}.
\]

For each integer `D=1,...,100`, it evaluates the sine identity above as a real interval and proves `|U_D(theta)|>7/25`. Independently, for every one of the `sum_(D=1)^100 D=5050` Chebyshev roots, it proves

\[
\left|\theta-\cos\frac{k\pi}{D+1}\right|>\frac{39}{2000000}.
\]

The smallest root separation occurs at `(D,k)=(94,2)`; the smallest certified `|U_D|` lower bound occurs at `D=46`. The machine-readable receipt saves every interval and every tested cutoff. It certifies nonresonance exactly for `1<=D<=100`. The all-degree theorem classifies resonance; it does not assert that this particular exact pair avoids resonance at every larger degree.

## Validation and integration boundary

The checker passed 96 exact scalar identities and all 5050 certified root comparisons. RPAC1–15 were read in full and agree with the independent derivation, including the strict lower bound in RPAC15. The checker verifies the reciprocal and Chebyshev coefficients through degree 12, the complete first correction through degree 10, the arbitrary-degree Cassini induction identity, weighted forward determinants for degrees 2 through 8, and the exact degree-three compatibility. These finite symbolic checks support the complete induction and analytic proofs written above. The mathematical proof is not inferred from a finite sample of degrees.
