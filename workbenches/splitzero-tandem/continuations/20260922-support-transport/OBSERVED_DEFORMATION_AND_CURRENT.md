# The support deformation after the original observation

22 September 2026. Result SZ-20260922-028, DF1–DF16.

The new idempotent deformation has an exact receiver through the original minimum section. Its collision point moves by a computable original-kernel return. The imaginary part of that displacement records the trace of the signed current. The real part moves the eigenvalues while preserving the full current. We calculate the resulting algebra, eigenline defect and metric cost, keeping the full original arithmetic operator distinguished from its boundary term.

## 1. The original family and its complete compression

Use all original objects, metrics and area guards of ST1–ST6. Let \(P_e=ee^\dagger\). The new source construction is
\[
F(s)=R+sP_e,\qquad M(s)=C+F(s),\qquad s\in\mathbb C.
\tag{DF1}
\]
It is the family of [ID1–ID24](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/6af54ea3c8ef99127af327f3103e086c68d482c2/workbenches/splitzero-tandem/branches/identity-absorber-square/IDEMPOTENT_DEFORMATION.md). The source arithmetic operator is exactly \(M(0)\). The derivation of its receiver below does not identify other parameters with arithmetic multiplication. Since \(R^2=0\), \(P_eR=0\), \(RP_e=R\), and \(P_e^2=P_e\), one has \(F(s)^2=sF(s)\).

Compression uses the unchanged original \(J\):
\[
F_B(s)=J^\dagger F(s)J=(\epsilon v+su)u^*,\qquad
M_B(s)=J^\dagger M(s)J=C_B+F_B(s),\quad C_B=C_B^*.
\tag{DF2}
\]
Set \(\lambda(s)=as+\epsilon r\). Multiplication proves
\[
\boxed{F_B(s)^2=\lambda(s)F_B(s),\qquad
J^\dagger F(s)(I-P_B)F(s)J=(\alpha s-\epsilon r)F_B(s).}
\tag{DF3}
\]
The first identity uses \(u^*(\epsilon v+su)=\epsilon r+sa\); the second is the complete multiplicativity defect ST9 together with \(F^2=sF\). Thus both the supported and hidden terms are retained. The exact original current frame gives
\[
F_B(s)\big|_{g,h}=\begin{pmatrix}\lambda(s)&0\\ \epsilon\sqrt{\mathfrak d}&0\end{pmatrix}.
\tag{DF4}
\]
It vanishes on the orthogonal complement of this plane. All entries follow from ST13 and \(\epsilon v+su=(\lambda(s)/\sqrt a)g+\epsilon\sqrt{\mathfrak d/a}\,h\).

## 2. The exact family of algebras and its eigenline defect

Over \(\mathbb C[s]\), the full unital observed algebra is faithfully
\[
\mathbb C[s,z]/\bigl(z(z-\lambda(s))\bigr)
\longrightarrow\operatorname{End}(B)\otimes\mathbb C[s],
\quad z\mapsto F_B(s),\quad1\mapsto I_B.
\tag{DF5}
\]
Monic division leaves a unique remainder \(A(s)+B(s)z\). Its operator value on \(h\) gives \(A(s)=0\), and the \(h\)-component of its value on \(g\) gives \(\epsilon\sqrt{\mathfrak d}B(s)=0\), hence \(B(s)=0\). This proves the exact kernel and freeness of rank two over the base. The supported representation uses \(\Pi_{\rm range}\) as unit and the same proof. The original measured support remains the different operator \(A=J^\dagger\Pi J\); its full defect and weights are ST5–ST19.

The map of parameter lines \(s\mapsto t=as+\epsilon r\) is an affine isomorphism, with inverse \(s=(t-\epsilon r)/a\), because \(a\ge\Theta_N>0\). Thus DF5 is exactly the pullback of the source family \(\mathbb C[t,z]/z(z-t)\) by this stated map. It is not the pullback by the identity parameter map unless its explicitly computed coefficients agree. At the literal native parameter \(s=0\), the observed fibre is \(\mathbb C[z]/z(z-\epsilon r)\). Its nilpotent collision is instead at
\[
\boxed{s_*=-\epsilon r/a.}
\tag{DF6}
\]
At this point,
\[
\widetilde R=F_B(s_*)=R_B-\frac{\epsilon r}{a}uu^*
=\epsilon\sqrt{\mathfrak d}\,hg^*,\qquad
\widetilde R^2=0,\quad\widetilde R\ne0.
\tag{DF7}
\]
In particular its dual-number representation is faithful and its active amplitude is the exact observed area amplitude \(\epsilon\sqrt{\mathfrak d}\).

The algebraic defect is also explicit before specializing. Write \(b_0=\epsilon\sqrt{\mathfrak d}\), a nonzero constant for the fixed original data. On the plane, the eigenline modules of DF4 are \(\mathbb C[s]h\) and \(\mathbb C[s](\lambda(s)g+b_0h)\). Their sum has cokernel
\[
\boxed{\bigl(\mathbb C[s]g\oplus\mathbb C[s]h\bigr)
/\bigl(\mathbb C[s]h+\mathbb C[s](\lambda(s)g+b_0h)\bigr)
\cong\mathbb C[s]/(s-s_*).}
\tag{DF8}
\]
The quotient sends \(Ag+Bh\) to \(A\bmod\lambda(s)\). Its kernel is exactly the displayed sum; surjectivity is witnessed by \(g\). Since \(\lambda(s)=a(s-s_*)\) with \(a\ne0\), the quotient is the stated one. This is the space defined by the collision obstruction, transported through the original observation. At \(s_*\) the two eigenlines meet in \(\mathbb Ch\), while the nonzero Jordan map DF7 remains.

## 3. Exact metric cost and the current carried by the displacement

For \(s\ne s_*\), the two supported spectral idempotents are
\(E_1(s)=F_B(s)/\lambda(s)\), \(E_0(s)=\Pi_{\rm range}-E_1(s)\). Multiplication using DF3 proves all idempotent identities. Their exact norms are
\[
\boxed{\|E_1(s)\|=\|E_0(s)\|
=\sqrt{1+\frac{\epsilon^2\mathfrak d}{|as+\epsilon r|^2}},\qquad
\|F_B(s)-F_B(s_*)\|=a|s-s_*|.}
\tag{DF9}
\]
In the orthonormal frame DF4, \(E_1\) has first column \((1,b_0/\lambda)^T\) and second column zero. The only nonzero row of \(E_0\) is \((-b_0/\lambda,1)\). This proves both norms. The last identity follows from \(F_B(s)-F_B(s_*)=(s-s_*)uu^*\), whose norm is \(a|s-s_*|\). This is a metric calculation at the shifted original collision, including \(\mathfrak d\) and \(a\).

The complete observed arithmetic current of the deformed full operator is
\[
W_B(s)=i(M_B(s)-M_B(s)^*)=W_B(0)-2\Im(s)uu^*,
\]
\[
W_B(s)\big|_{g,h}=\begin{pmatrix}
-2\Im\lambda(s)&-i\epsilon\sqrt{\mathfrak d}\\
i\epsilon\sqrt{\mathfrak d}&0
\end{pmatrix}.
\tag{DF10}
\]
The Hermitian \(C_B\) cancels exactly. Its two active eigenvalues are
\[
-\Im\lambda(s)\ \pm\sqrt{(\Im\lambda(s))^2+\epsilon^2\mathfrak d},
\quad\det(W_B(s)|_{g,h})=-\epsilon^2\mathfrak d.
\tag{DF11}
\]
Expanding the characteristic polynomial proves both assertions. Thus the determinant of the active current is independent of the entire complex deformation, while its trace is \(-2\Im\lambda(s)\). For real \(s\), the whole current is unchanged, not only its determinant.

The exact obstruction to a real collision is
\[
\boxed{\Im s_*=-\frac{\epsilon\Im r}{a}
=\frac{\operatorname{tr}W_B(0)}{2a}.}
\tag{DF12}
\]
Consequently a real \(s\) reaches the collision if and only if the actual current trace is zero. The nearest real parameter is \(s_{\mathbb R}=-\epsilon\Re r/a\). For every real \(s\),
\[
|\lambda(s)|^2=a^2(s-s_{\mathbb R})^2+\epsilon^2(\Im r)^2.
\]
If \(\Im r\ne0\), the maximum over the real line of the idempotent norm DF9 is therefore exactly \(\sqrt{1+\mathfrak d/(\Im r)^2}\), attained at \(s_{\mathbb R}\). If \(\Im r=0\), the real path reaches the nonzero nilpotent fibre and the idempotent norms diverge as its parameter approaches that point. Both cases preserve the original measured columns. The obstruction defines this precise shifted family rather than ending the calculation.

At the complex collision, the relation to the original current is
\[
W_B(s_*)=i(\widetilde R-\widetilde R^*),\qquad
W_B(s_*)-W_B(0)=2\epsilon(\Im r)gg^*,
\]
\[
\frac{\|W_B(s_*)-W_B(0)\|}{\epsilon\sqrt{\mathfrak d}}
\le2\sqrt{\alpha/\Theta_N},\qquad
\left|\widehat y^*[W_B(s_*)-W_B(0)]\widehat y\right|
\le2\epsilon|r|\eta_N^2.
\tag{DF13}
\]
The first line follows from DF7 and DF10; the norm of \(gg^*\) is one. ST6 gives the relative bound, and ST13 gives the terminal bound. Thus the deformation identifies exactly the missing off-diagonal current of TR20 as the collision-fibre current. The terminal difference is absolutely \(e^{-2q\psi(t_N)+O(k\log(q+2))}\). The collision fibre is tied to the native fibre by a proved small terminal correction, not by a declaration of equality.

## 4. Original scale and four-cutoff receiver

The shifted collision retains the exact estimate
\[
\log\|\widetilde R_N\|=\log\epsilon_N+\tfrac12\log\mathfrak d_N
=q\psi(t_N)+O_{h,\varpi}(k\log(q+2)),
\]
\[
\boxed{\mathcal R\log\|\widetilde R_N\|
=2[\psi(0)-\psi(1)]q+O_{h,\varpi}(k\log(q+2)).}
\tag{DF14}
\]
Here the return uses exactly \(N=q-1,q,2q-1,2q\) with signs \(+,+,-,-\), and the two monic endpoints are kept explicitly. ST6 bounds the logarithmic area correction; the endpoint modulus of the original elliptic profile, proved in RC8–10, gives the stated \(O(\log q)\) changes under the two shifts by \(1/q\). Moreover \(|s_*|\le\epsilon\sqrt\alpha/\Theta_N=e^{O(k\log(q+2))}\), while the active nilpotent amplitude grows at \(e^{q\psi+O(k\log q)}\). These are scale statements with the original parameters retained. They do not set the collision displacement or its imaginary part to zero.

ST18 and the companion finite mixed-probe proof carry the same support and orientation data through the full original observation. DF13 identifies the residual signed terminal pairing with a precise point of the new algebraic family, up to its proved negligible correction. Evaluating its particular sign still requires that original marked pairing. The present result supplies the transported family, its exact obstruction module, metric cost, current determinant and four-cutoff amplitude; it does not infer spectral reality for \(C_B+F_B(s)\) from the boundary algebra alone. The full \(C_B\) remains in DF2.


## 5. Correction propagated to the earlier denominator return

The new arrival identifies a constant-name error in the published027 RD15. Put \(a_0=\psi(0)\), \(a_1=\psi(1)\). The established kernel-volume constant is \(C_\partial=2J(1)\), whereas the boundary-amplitude return in DF14 has coefficient \(2(a_0-a_1)\). The exact relation, obtained by integrating the already proved RC10 and using \(J(0)=0\), is
\[
J(t)=4\int_0^t\psi(s)\,ds-2(1+t)\psi(t)+2a_0,
\]
\[
\boxed{C_\partial=8\int_0^1\psi(s)\,ds+4a_0-8a_1.}
\tag{DF15}
\]
Thus the full profile, with its integral retained, connects the two coefficients. The established values are \(C_\partial=1.35428198782529213288\ldots\), \(2(a_0-a_1)=0.350091046500433050\ldots\). The earlier interval certificate for the first remains in024 CK14 and025 IR6; the second is evaluated by the same original RC7–10 elliptic formulas.

The original denominator estimate RD14 has \(\log\mathfrak A_N=2q\psi(t_N)+O(k\log q)\). Substituting all four literal arguments \(0,1/q,1,1+1/q\), with the endpoint bounds proved in RC8–10, gives the corrected return
\[
\boxed{\mathcal R\log\mathfrak A_N=4(a_0-a_1)q+O(k\log q).}
\tag{DF16}
\]
Its numerical coefficient is \(0.700182093000866100\ldots\). RD15's expression \(2C_\partial q\) is withdrawn under the established kernel-volume notation. The separate denominator rates, their finite inequalities and all TR coherence estimates remain unchanged. The kernel return remains \(mC_\partial q+o(kq)\). The preceding sealed edition is preserved as provenance; this successor supplies the corrected active equation and its exact connection to the older profiles.
