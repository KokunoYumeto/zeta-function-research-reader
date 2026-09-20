# Independent review of the actual kernel receiver

The root derivation `../ORIGINAL_KERNEL_MIXED_DETERMINANT.tex`, MR1–23, was read completely. No sign, transpose, factorial, degree-shift, or source-mass error was found in its finite formulas. This is an independent mathematical review, not a publication receipt or an evaluation of the original period coefficients.

## Original coefficient receiver

The complete original `ORIGINAL_CONDUCTOR_STRIP_FRAME.tex`, OCF1–26, was read at:

`ORIGINAL_CONDUCTOR_STRIP_FRAME.tex`.

OCF7 proves `N_k S_k=I` and `ker N_k=im M_A`. OCF17 proves that the conductor image is contained in the actual invariant image, with its original factor 5 in the Reynolds lift. OCF19 gives `rank Z_k=8k−32` for the stated `k≥9` domain. OCF21–22 prove the complete coefficient quotient and its right inverse. Therefore, with the root derivation's exact columns `Z=[M_A,S_k Z_k]`, applying `N_k` to a column relation proves first that the `Z_k` coefficients vanish and then that the `M_A` coefficients vanish. Hence `Z` has full column rank and its image is exactly the invariant image, not merely the conductor image. The count is

\[
r=(k-7)^2+(8k-32)=k^2-6k+17,
\quad q=(k+1)^2,
\quad m=q-r=8k-16.
\]

OCF24 identifies the biform coefficient pairing with the original complex-linear primary dual pairing in the same lexicographic order. Thus a coefficient column `z` acts on a primary value column `y` as `z^T y`. It follows that the actual kernel's value-space image is `ker Z^T=im π^T`, because `πZ=0` and both spaces have dimension `m`. No conjugation belongs in this coefficient dualization.

## Complementary determinant and its frame constants

Set `U=π^T` and `V=bar Z`. Then

\[
U^*V=\overline{\pi Z}=0,
\quad U^*U=\overline\pi\pi^T,
\quad V^*V=Z^T\overline Z.
\]

Both Gram matrices are positive definite. Using their positive square roots only as a finite proof device makes `U_0=U(U^*U)^{-1/2}` and `V_0=V(V^*V)^{-1/2}` into complementary orthonormal frames. For any positive definite complete covariance `C`, the matrix in that orthonormal frame is

\[
\begin{pmatrix}A&B\\B^*&D\end{pmatrix}.
\]

Block elimination gives `det C=det D det(A−BD^{-1}B*)`, while the upper inverse block is `(A−BD^{-1}B*)^{-1}`. Restoring both original frame factors gives exactly

\[
\det(U^*C^{-1}U)
=\frac{\det(U^*U)}{\det(V^*V)}
  \frac{\det(V^*CV)}{\det C}
=\frac{\det(\overline\pi\pi^T)}{\det(Z^T\overline Z)}
  \frac{\det(Z^TC\overline Z)}{\det C}.
\]

This verifies MR11. Replacing `bar Z` by `Z`, or deleting either frame factor, is not justified. The root derivation makes neither replacement.

## Mixed expansion, orientation and integral

For increasing root subsets `I,J` of cardinality `r`, twice applying finite Cauchy–Binet gives

\[
\det(Z^TC_d\overline Z)
=\sum_{I,J}\det Z_I\,\overline{\det Z_J}\,
  \det(C_d)_{I,J}.
\]

The external kernel has `d=N+1` terms. The mixed finite formula therefore applies with relation degree `r` and integrated determinant size `t=d−r`, yielding

\[
\det(C_d)_{I,J}
=\frac{V_I\overline{V_J}}{D_d}
 B_{d-r}(\chi_I,\chi_J).
\]

The root and minor orders agree, so no extra permutation sign occurs. Since `n=d−q` and `m=q−r`, the numerator size is exactly `t=n+m`. The denominator's full relation size is `n`. At the first admitted cutoff `N=q−1`, this is numerator size `m` and denominator `B_0=1`, not a negative degree.

For `a_I=z_I V_I`, let `Φ=Σ_I a_I ∏_{j=1}^t χ_I(S_j)`. Expanding `|Δ_t(S)Φ|²` gives coefficients `a_I bar a_J`; determinant integration gives exactly `t! B_t(χ_I,χ_J)` for each term. Thus

\[
\mathcal A_d=\frac1{t!}\int|\Delta_t(S)\Phi(S_1,\ldots,S_t)|^2
\prod_jd\mu(u_j).
\]

This verifies MR20 including interference terms and the factorial. It is the norm of the complete finite sum. It is not the sum obtained by dropping the off-diagonal terms.

The full-root denominator identity is `det C_d=|V_χ|² B_n(χ,χ)/D_d`. Substitution gives MR18. Under the diagnostic comparison `dμ→a dμ`, `A_d` scales as `a^(d−r)` and `B_n` as `a^(d−q)`; their ratio scales as `a^m`, exactly the rank-`m` restricted metric determinant. The coefficient frame factors are fixed across all four cutoffs, so their logarithms cancel with coefficients `1+1−1−1`. This proves MR19 without assuming monotonicity of the individual errors or of a mixed summand.

## Gamma receiver and its full mass

Actual original sources read for this part:

- `JOINT_MINIMUM_RECEIVERS.tex`, lines 276–414, containing the full JM21–28 section.
- Complete `KERNEL_GAMMA_INDEPENDENT.md`, KG1–21.
- `COERCIVITY_INDEPENDENT.md`, lines 90–132, containing C1–C4.

All three are in `joint_minimum_arrival`. The prior coercivity theorem used to obtain the source comparison was not replayed here. Its proved comparison is the explicit imported input, as in the root note; the root note does not claim to derive that estimate from Akemann–Vernizzi.

Here is a separate derivation of the exact recurrence and norms in MR22. The beta-integral Fourier calculation in KG1–2 gives

\[
\int e^{-ity}\frac{|\Gamma(1/4+iy/2)|^2}{2\pi}\,dy
=\sqrt{2\pi}(\cosh t)^{-1/2}.
\]

The original Gamma tail estimate gives an integrable exponential majorant on closed subintervals of `|Re s|<π/2`. The moment-generating integral is therefore analytic there, and continuation of the displayed Fourier identity gives, for real `|s|<π/2`,

\[
\int e^{sy}\,d\sigma(y)=\sqrt{2\pi}(\cos s)^{-1/2}.
\]

For real `z,w` sufficiently close to zero define

\[
F(z,y)=(1+z^2)^{-1/4}e^{y\arctan z}
=\sum_{j\ge0}p_j(y)z^j/j!.
\]

Taylor coefficients in `z` are polynomials in `y` of degree `j`, and their top coefficient is one. The differential identity

\[
(1+z^2)\partial_z F=(y-z/2)F
\]

gives `p_0=1`, `p_1=y`, and `p_(j+1)=y p_j−j(j−1/2)p_(j−1)` after coefficient comparison. The same exponential majorant justifies differentiating the following integral in both real parameters to every finite order:

\[
\begin{aligned}
\int F(z,y)F(w,y)\,d\sigma(y)
&=\sqrt{2\pi}[(1+z^2)(1+w^2)]^{-1/4}
\bigl[\cos(\arctan z+\arctan w)\bigr]^{-1/2}\\
&=\sqrt{2\pi}(1-zw)^{-1/2}.
\end{aligned}
\]

The last identity uses the positive real branches near zero and
`cos(arctan z+arctan w)=(1−zw)/sqrt((1+z²)(1+w²))`.
Comparing the coefficient of `z^j w^l` proves

\[
\int p_j(y)p_l(y)\,d\sigma(y)
=\delta_{jl}\sqrt{2\pi}\,j!(1/2)_j.
\]

The polynomials have real coefficients, so this is their conjugate-first orthogonality on the real line. It proves MR22 with mass `γ_0=√(2π)`, without omitting the scale `dy=2dx` implicit in the original Gamma density.

The original `S`-monic polynomial is `i^j p_j((S−c)/i)`; its squared norm is unchanged. Its root evaluation column is `i^j f_j`. Consequently the covariance summand is `i^j f_j (i^j f_j)^*/γ_j=f_j f_j*/γ_j`. The value of every quotient polynomial at every root remains the same under the literal coordinate substitution, so the bilinear coefficient frames `π,Z` do not change in value coordinates. This proves MR23 and its compatibility with MR8–11.

Finally the full-source comparison through degree `2q` applies to every candidate in each identical remainder fibre. Taking the minima, and only then restricting by the fixed actual kernel frame, gives the two matrix inequalities of MR21. Each log determinant error lies in the common interval `[m log α_k,m log β_k]`. Two paired differences give the exact factor `2m log(β_k/α_k)`. With `m=8k−16`, `q=(k+1)²`, and the imported width `O_h(k log²(q+2))`, division by `kq` gives a quantity tending to zero. This checks the stated Gamma transfer without evaluating the unresolved determinant coefficient.

## Exact finite checks

`check_receiver.py` independently verified 43 identities in normal and optimized Python. Its three nonreal coefficient frames include `(q,m,r)=(2,1,1),(3,2,1),(3,1,2)`. The checks compare the inverse restriction, complementary determinant, full mixed sum, positive squared-sum integral, first admitted cutoff, mass exponent, and exact four-cutoff ratio. `RECEIVER_CHECKS.json` retains the successful optimized output; the normal run returned the same 43 passing checks. The fixtures retain source mass 21 but do not sample the arithmetic period or replace the original source.
