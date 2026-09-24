# Independent verification of the original-zeta Jacobian bridge

24 September 2026. Check locators JTC1–JTC6. This checks the complete JTB2–JTB7 argument in ORIGINAL_ZETA_JACOBIAN_TRACE_BRIDGE.md against the independently constructed GZR pairing. It is a mathematical check of the stated receiving maps, not a new assertion about primitive \(Z_1/\tau\).

## JTC1. Entire multiplier and Euler-summation sign

Write \(h=s-1\) with the original Stieltjes convention
\[
\zeta(1+h)=h^{-1}+\gamma-\gamma_1h+\gamma_2h^2/2+\cdots.
\]
Then
\[
A_\zeta(1+h)=h^2\zeta'(1+h)=-1-\gamma_1h^2+\gamma_2h^3+\cdots.
\]
In particular \(A_\zeta(1)=-1\) and \(A_\zeta'(1)=0\), proving both endpoint coefficients in JTB3.1.

The remainder sign in JTB2.2 is negative. For a direct independent check, Euler summation first gives
\[
\zeta(s)=\frac1{s-1}+\frac12
-s\int_1^\infty\widetilde B_1(x)x^{-s-1}\,dx
\quad(\Re s>1).
\]
Integrate using \(\widetilde B_2'(x)=2\widetilde B_1(x)\) on each integer interval. The internal endpoint contributions cancel, and \(\widetilde B_2(1)=B_2=1/6\). Thus the first integration step gives
\[
\zeta(s)=\frac1{s-1}+\frac12+\frac{s}{12}
-\frac{s(s+1)}2\int_1^\infty\widetilde B_2(x)x^{-s-2}\,dx.
\]
Repeating in pairs gives exactly JTB2.2, with the rising factorial, \(B_{2k}/(2k)!\), and the displayed negative remainder. Its integral and every differentiated integral converge uniformly on any fixed strip contained in \(\Re s>1-2K\). This proves the required polynomial growth of the entire \(A_\zeta\). Multiplication by it preserves both \(\mathcal B\) and every full original zero order.

## JTC2. Two divisions at the original pole

Put \(g_0=G(1)\), \(g_1=G'(1)\), and \(b_1=8F_*'(1)\), with \(8F_*(1)=1\). First division of \(A_\zeta G\) gives
\[
\frac{A_\zeta(s)G(s)+8F_*(s)g_0}{s-1}.
\]
Its value at one is \(-g_1+b_1g_0\). The second division therefore gives exactly
\[
\zeta'(s)G(s)+\frac{8F_*(s)}{(s-1)^2}
\bigl[g_0+(s-1)(g_1-b_1g_0)\bigr].
\]
No endpoint sign is reversed. Expansion \(8F_*(1+h)=1+b_1h+4F_*''(1)h^2+\cdots\) yields the constant
\[
-\frac12G''(1)+b_1G'(1)
+(4F_*''(1)-b_1^2-\gamma_1)G(1),
\]
as in JTB3.4. The two principal-part terms are cancelled only by the two explicitly displayed correction coefficients. The original values at zero and the trivial zeros remain JTB3.5.

## JTC3. Absolute interchange of the entire logarithmic derivative

The genus-one pairing of terms is essential:
\[
\frac1{s-\rho}+\frac1\rho=\frac{s}{\rho(s-\rho)}.
\]
On \(\Re s=-1,2\), the actual zeros satisfy \(|s-\rho|\ge1\). The retained estimate \(n(R)\le C(R+2)^{3/2}\), with multiplicities, gives
\[
\sum_{|\rho|\le 2R}\frac{m_\rho}{|\rho|}=O(R^{1/2}),
\qquad
\sum_{|\rho|>2R}\frac{m_\rho}{|\rho|^2}=O(R^{-1/2}).
\]
For \(R=|s|+2\), the total sum of absolute values of the paired genus-one terms is therefore \(O(R^{3/2})\) on both edges. Multiplying by an arbitrary \(\Phi\in\mathcal B\) gives an integrable majorant, so exchanging the original vertical integrals with the zero sum is valid. Each individual paired term has contour difference \(\Phi(\rho)\). The absolute convergence of \(\sum_\rho m_\rho|\Phi(\rho)|\) follows from the same zero count and rapid strip decrease.

The original multiplier derivative
\[
\frac1s+\frac1{s-1}-\frac12\log\pi+\frac12\psi(s/2)
\]
has cancelling residues at zero and residue \(+1\) at one. It has no further poles inside this strip. Consequently subtraction from the full \(F_*'/F_*\) identity gives precisely
\[
\mathfrak C(\Phi\,\zeta'/\zeta)
=\sum_\rho m_\rho\Phi(\rho)-\Phi(1).
\]
Thus the original pole sign in JTB4.1 is correct; no unproved choice of heights or sum of \(1/\zeta'(\rho)\) is needed.

## JTC4. The pole correction in the global Weil factorization

Division of the actual entire representative by the original \(\zeta\) gives
\[
\frac{\mathscr J_\zeta G(s)}{\zeta(s)}
=\frac{\zeta'(s)}{\zeta(s)}G(s)
+s\pi^{-s/2}\Gamma(s/2)
\left[\frac{G(1)}{s-1}+G'(1)-b_1G(1)\right].
\]
Multiplication by \((CF)(1-s)=\overline{F(1-\bar s)}\) gives from the first term
\[
W([F],[G])-G(1)\overline{F(0)}.
\]
In the second term \(s\Gamma(s/2)=2\Gamma(1+s/2)\) removes the zero-endpoint pole, while the full coefficient at \(s=1\) is \(1\). Its residue is therefore
\[
+G(1)\overline{F(0)}.
\]
The two contributions cancel with the stated signs. Polynomial strip bounds for the retained Gamma expression and rapid decrease of the other factors justify the separate contour calculation. Hence
\[
W(x,y)=B_\zeta(\mathcal J_\zeta y,Cx)
\]
holds for the whole quotient, not only finite primary subspaces.

## JTC5. Exact primary rank, kernel, and covariance

With the original germ \(\zeta(\rho+t)=t^mu_\rho(t)\),
\[
\zeta'(\rho+t)=mt^{m-1}u_\rho(t)+t^mu_\rho'(t).
\]
Its multiplication on \(\mathbb C[t]/(t^m)\) is
\[
P(t)\longmapsto m u_\rho(0)P(0)t^{m-1}.
\]
Its rank is exactly one. For \(m>1\) its kernel is \((t)\) and its square is zero; for \(m=1\) it is the nonzero scalar \(\zeta'(\rho)\). Full original zero jets separate \(\mathcal Q\), so the stated global kernel is exactly the subspace whose value coordinate is zero at every actual zero. The nondegeneracy of GZR and the surjectivity of conjugation \(C\) identify that kernel with the second-slot radical of the Weil form. The existing Hermitian symmetry of the Weil form identifies both radicals. No assertion that the range is a closed or unrestricted product of socles follows.

The operator \(\mathcal J_\zeta=(L-1)^{-2}M_{(s-1)^2\zeta'}\) commutes with \(L\) and \(T_a\): the multiplier does so, and the inverse of the commuting invertible operator \(L-1\) does so. GZR7 gives the dual identities
\[
\mathscr D_\zeta T_a=aT_a^\vee\mathscr D_\zeta,\qquad
\mathscr D_\zeta L=(1-L^t)\mathscr D_\zeta.
\]
The conjugation and the factor \(a\) are therefore placed correctly in JTB7.2–JTB7.3. The raw comparison factor is exactly four, since each raw Mellin image contributes the retained factor two and the contour pairing is bilinear.

## JTC6. Result and one typographical correction

The mathematical identities and arguments in JTB2–JTB7 pass these independent checks. In JTB6.4 the displayed residue ends with a comma followed by \(ds\); it should have the differential \(\,ds\). This is a typesetting correction, not an altered residue or sign. The proof does not establish positivity, purity, or a topological isomorphism from \(\mathcal Q\) onto its continuous dual.
