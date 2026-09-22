# The collision comparison for the full original arithmetic resolvent

22 September 2026. This calculation applies the measured collision data to the full observed arithmetic operator. It preserves the selfadjoint part, the observation metric, the actual spectral coordinate and all four source cutoffs. The new estimate concerns exterior spectral coordinates; it does not evaluate the native phase integral on its remaining frequency region.

## 1. Original objects and source identities

At a literal original cutoff \(N\in\{q-1,q,2q-1,2q\}\), retain the positive source metric \(G_N\), onto observation \(\Lambda\), and minimum isometry
\[
Q_B=(\Lambda G_N^{-1}\Lambda^*)^{-1},\qquad
L=G_N^{-1}\Lambda^*Q_B,\qquad J=LQ_B^{-1/2}.
\tag{CRX1}
\]
A dagger on the source uses \(G_N\); a star on the observed space uses the Euclidean coordinates given by this exact isometry. In the original decomposition \(M=C+\epsilon fe^\dagger\), retain \(C=C^\dagger\), the orthonormal source vectors \(e,f\), and \(\epsilon>0\). Put
\[
u=J^\dagger e,\quad v=J^\dagger f,\quad
a=u^*u,\quad d=v^*v,\quad r=u^*v,\quad
D=ad-|r|^2\ge\Theta_N>0,\quad \alpha=1-a.
\tag{CRX2}
\]
These are the original [ST5–6 and ST13–20](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/4ba9285b66af58a6d58fc502a494c1fb45ca5b79/workbenches/splitzero-tandem/continuations/20260922-support-transport/SUPPORT_SPECTRUM_AND_TERMINAL_MASS.md#L44) data, with their finite native guards. The actual terminal-cardinal estimates retain the five-orbit and admitted-period domain specified there. The finite matrix proof below uses the displayed positive-area data and applies throughout that established domain.

Write
\[
C_B=J^\dagger CJ=C_B^*,\qquad
M_B(s)=C_B+(\epsilon v+su)u^*,\quad
s_*=-\epsilon r/a,
\]
\[
b=\epsilon\sqrt D>0,\quad c=\frac{|r|}{\sqrt D},\quad
\beta_r=\Im r,\quad M_\theta=M_B(\theta s_*),\quad0\le\theta\le1.
\tag{CRX3}
\]
The symbol \(\beta_r\) denotes the imaginary part of the retained cross-Gram entry. It is not the source leverage called \(\beta\) in NV. The complex parameter \(s\), straight-segment parameter \(\theta\), and spectral coordinate \(\zeta\) have separate roles. The underlying metric is fixed at this particular cutoff throughout the \(s\)-deformation.

The exact collision and rank-one determinant/inverse identities are [OC1–17](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/c9df443d9e1df000dfbb083943f97197e746eb08/workbenches/splitzero-tandem/branches/identity-absorber-square/OBSERVED_COLLISION.md#L128). The complete local proof source was read, together with [OSP1–51](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/c9df443d9e1df000dfbb083943f97197e746eb08/workbenches/splitzero-tandem/branches/identity-absorber-square/OBSERVED_SUPPORT_PROPAGATION.md). CRX4–12 prove the quantitative consequence, rather than assuming a resolvent estimate for the nonnormal full operator.

## 2. A singular-value bound from the actual current

In the original orthonormal observed frame
\(g=u/\sqrt a\), \(h=(v-(r/a)u)/\sqrt{D/a}\), direct multiplication gives
\[
W_\theta=i(M_\theta-M_\theta^*)
=\begin{pmatrix}-2\epsilon(1-\theta)\beta_r&-ib\\ib&0\end{pmatrix}
\quad\hbox{on }\operatorname{span}\{g,h\},
\tag{CRX4}
\]
and zero on its orthogonal complement. The same \(C_B\) remains in every full \(M_\theta\); its contribution to this displayed difference cancels by selfadjointness. The two eigenvalues of CRX4 are
\(-x_\theta\pm\sqrt{b^2+x_\theta^2}\), where \(x_\theta=\epsilon(1-\theta)\beta_r\). Thus
\[
h_\theta:=\tfrac12\|W_\theta\|
=\tfrac12\left(\sqrt{b^2+x_\theta^2}+|x_\theta|\right)
\le b/2+\epsilon|\beta_r|\le b(1/2+c),\qquad h_1=b/2.
\tag{CRX5}
\]
The first inequality follows from \(\sqrt{b^2+x^2}\le b+|x|\), proved by squaring the nonnegative sides.

For every unit observed vector \(x\),
\[
\Im\langle x,(\zeta I-M_\theta)x\rangle
=\Im\zeta+\tfrac12\langle x,W_\theta x\rangle.
\]
Cauchy–Schwarz and the triangle inequality imply
\[
\| (\zeta I-M_\theta)x\|
\ge |\Im\zeta|-h_\theta.
\]
If this right side is positive, the square finite matrix is injective and therefore invertible. Taking the infimum over all unit \(x\) proves
\[
\boxed{\|G_\theta(\zeta)\|\le\frac1{|\Im\zeta|-h_\theta},
\qquad G_\theta=(\zeta I-M_\theta)^{-1}.}
\tag{CRX6}
\]
The estimate holds for every real part of \(\zeta\). It uses neither normality nor a norm bound on \(C_B\). In particular a large or noncommuting \(C_B\) has not been deleted from the inverse.

## 3. Evaluated collision error and marked resolvent receivers

Retain a positive exterior margin \(\varrho>0\) in the original spectral units:
\[
|\Im\zeta|\ge(1/2+\varrho)b,\qquad
c\le\varrho/4.
\tag{CRX7}
\]
Then CRX6 applies to the whole segment. The exact inverse identity, obtained by multiplying both inverses into their defining matrices, is
\[
G_1-G_0=s_*G_1uu^*G_0.
\]
Since \(|s_*|\|uu^*\|=\epsilon|r|=bc\), CRX5–7 give
\[
\boxed{
b\|G_1-G_0\|
\le\frac{c}{\varrho(\varrho-c)}
\le\frac{4c}{3\varrho^2}.
}
\tag{CRX8}
\]
The collision inverse has denominator at least \(b\varrho\); the native inverse has denominator at least \(b(\varrho-c)\). Both denominators, and the physical spectral coordinate, remain in the first bound. For any two original marked vectors \(x,y\), CRX8 gives the explicit receiver
\[
|x^*(G_1-G_0)y|
\le\|x\|\,\|y\|\frac{c}{b\varrho(\varrho-c)}.
\tag{CRX9}
\]
There is no identification of these two vector phases. The sharper exact ordered-pair identity in OC15 remains applicable when the two actual scalar factors are available.

Let \(p_\theta(\zeta)=\det(\zeta I-M_\theta)\), and put \(m_0=u^*G_0u\). Multilinearity in the columns gives
\(p_\theta/p_0=1-\theta s_*m_0\): all terms taking two rank-one perturbation columns vanish. The actual scalar satisfies
\[
|s_*m_0|\le\epsilon|r|\|G_0\|
\le\frac{c}{\varrho-c}\le\frac13.
\]
The logarithm based at \(\theta=0\) is therefore the absolutely convergent series
\(-\sum_{j\ge1}(\theta s_*m_0)^j/j\) along this entire original deformation segment. It has no winding ambiguity or determinant zero there. Summing absolute values and using \(1/j\le1\) proves
\[
\boxed{
\left|\operatorname{Log}\frac{p_1(\zeta)}{p_0(\zeta)}\right|
\le\frac{c}{\varrho-2c}\le\frac{2c}{\varrho}.
}
\tag{CRX10}
\]
Both the real logarithmic-volume error and the continuously followed determinant-phase error obey CRX10. This is a quantitative evaluation of the collision transfer error; it is not an evaluation of either determinant separately.

## 4. Native source bounds and all four cutoffs

The contraction \(0\prec U^*U\preceq I_2\) implies
\(|r|^2\le(1-a)(1-d)\le\alpha\), by the determinant of its positive semidefinite complement. Consequently
\[
\boxed{c_N\le\sqrt{\alpha_N/\Theta_N}.}
\tag{CRX11}
\]
This gives a finite sufficient check for CRX7: require \(\sqrt{\alpha_N/\Theta_N}\le\varrho_N/4\), using the already defined original finite quantities. The retained native estimates
\(\alpha_N\le\exp[-2q\psi((N+1-q)/q)+O_{h,\varpi}(k\log(q+2))]\) and
\(-\log\Theta_N=O_{h,\varpi}(k\log(q+2))\) yield the evaluated transfer rate
\(c_N\le\exp[-q\psi((N+1-q)/q)+O_{h,\varpi}(k\log(q+2))]\).
The effective bounds are CRX8–11 themselves; this asymptotic does not replace any finite guard.

At the four actual cutoffs choose exterior coordinates \(\zeta_N\) satisfying CRX7 separately, or use a single physical \(\zeta\) whose imaginary part meets all four inequalities. Define the original signed return on these scalar logarithmic transfers by
\(\mathcal R f=f_{q-1}+f_q-f_{2q-1}-f_{2q}\). Then
\[
\boxed{
\left|\mathcal R\operatorname{Log}\frac{p_{*,N}(\zeta_N)}{p_{0,N}(\zeta_N)}\right|
\le\sum_{N\in\{q-1,q,2q-1,2q\}}
\frac{c_N}{\varrho_N-2c_N}
\le\sum_N\frac{2}{\varrho_N}\sqrt{\frac{\alpha_N}{\Theta_N}}.
}
\tag{CRX12}
\]
This follows by applying the four signs and then the triangle inequality. No pair of cutoff metrics, source columns, or source functions has been identified. Each \(p_{*,N}\) uses its own collision \(s_{*,N}\) and keeps its entire original \(C_{B,N}\).

The guard in CRX7 specifies exactly the exterior region proved here. Frequencies failing that guard remain a separate part of the original phase calculation. In particular CRX12 is not integrated over an unbounded interval with a frequency-independent error, and the original interior frequency contribution is not discarded. The calculation establishes an exponentially controlled full-operator collision transfer on its stated exterior region. The actual native marked phase remains an arithmetic datum.

## 5. Provenance and reproducibility

OC1–17 and OSP1–51 were read in full. ST supplies the original source and metric bounds. The new matrix inequalities, determinant identity and logarithm estimate are proved above. No historical novelty of these linear-algebra operations is claimed. Edition 029's complete source collection retains the predecessor definitions, proofs, authorship and human citations.
