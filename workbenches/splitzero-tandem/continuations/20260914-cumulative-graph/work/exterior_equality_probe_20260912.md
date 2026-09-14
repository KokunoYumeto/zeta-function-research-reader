# Exterior trace equality, the spectral projector, and quantitative coupling

Date: 2026-09-12. This is an independent finite-dimensional proof for the exterior-amplification integration. All norms and adjoints below use the original Hermitian form. No arithmetic asymptotic estimate, Lean execution, or external-source verification is asserted.

## 1. Original objects and exact domains

Let \(\mathcal C\) be a finite-dimensional complex vector space with the positive-definite Hermitian form
\[
\langle x,y\rangle_G=x^*Gy
\]
(conjugate-linear in the first variable). Let \(k\in\mathbb R\), let \(A\in\operatorname{End}_{\mathbb C}(\mathcal C)\), and set
\[
A^\sharp=G^{-1}A^*G,\qquad H=A^\sharp+A-kI_{\mathcal C}.
\]
Suppose the actual operator \(H\) has rank at most two and trace zero. Its eigenvalues, with zero eigenvalues retained, are \(+\epsilon,-\epsilon,0,\ldots,0\) for a uniquely determined \(\epsilon\geq0\).

Let \(V=\mathcal C_>\) be the direct sum of the **full generalized eigenspaces** of \(A\) for the eigenvalues satisfying \(\operatorname{Re}\lambda>k/2\). Let \(W=V^{\perp_G}\), and let \(P:\mathcal C\to\mathcal C\) be the \(G\)-orthogonal projection with image \(V\) and kernel \(W\). Let \(Q\) be the spectral projector with image \(V\) and kernel the direct sum of all the other full generalized eigenspaces of \(A\).

For specificity, this last projector is an exact polynomial in the original operator. Factor the minimal polynomial as \(m_A=m_+m_-\), where \(m_+\) contains exactly the selected eigenvalues with their original minimal-polynomial exponents and \(m_-\) contains all the remaining eigenvalues with their original exponents. The two factors are coprime. Choose polynomials \(a,b\) with
\[
a(z)m_+(z)+b(z)m_-(z)=1.
\]
Then
\[
Q=b(A)m_-(A).
\]
Indeed, the polynomial \(bm_-\) is congruent to one modulo \(m_+\) and to zero modulo \(m_-\); applying it to each full generalized eigenspace gives the asserted identity and zero maps. This also proves \(Q^2=Q\), \(AQ=QA\), and independence from the choice of the Bezout polynomials.

All block maps below use the original orthogonal direct sum \(\mathcal C=V\oplus W\), without a change in either restricted Hermitian form. Since \(A(V)\subseteq V\), define
\[
B=A|_V:V\longrightarrow V,\qquad
D=(1-P)A|_W:W\longrightarrow W,\qquad
T=PA|_W:W\longrightarrow V.
\]
Then the exact block identities are
\[
A=\begin{pmatrix}B&T\\0&D\end{pmatrix},\quad
A^\sharp=\begin{pmatrix}B^\sharp&0\\T^\sharp&D^\sharp\end{pmatrix},\quad
H=\begin{pmatrix}B^\sharp+B-kI_V&T\\T^\sharp&D^\sharp+D-kI_W\end{pmatrix}.
\tag{E1}
\]
In particular, as maps \(W\to V\),
\[
PH|_W=PA|_W=T.
\tag{E2}
\]
This equality includes the proof of the vanishing term: \(PA^\sharp|_W=((1-P)AP)^\sharp|_W=0\), because \((1-P)AP=0\).

Write
\[
L=\operatorname{Tr}_{\mathcal C}(PH)
 =\operatorname{Tr}_V(B^\sharp+B-kI_V)
 =\sum_{\operatorname{Re}\lambda>k/2}m_A^{\rm alg}(\lambda)(2\operatorname{Re}\lambda-k),
\tag{E3}
\]
where \(m_A^{\rm alg}(\lambda)\) is the original algebraic multiplicity of \(\lambda\) in \(A\). The final equality follows by taking the trace of \(B\), whose characteristic polynomial consists exactly of the selected full generalized blocks, and by \(\operatorname{Tr}B^\sharp=\overline{\operatorname{Tr}B}\). Thus \(L>0\) exactly when \(V\ne0\).

If \(\epsilon=0\), then \(H=0\). For every eigenvector \(x\ne0\) of \(A\),
\[
0=\langle x,Hx\rangle_G=(2\operatorname{Re}\lambda-k)\langle x,x\rangle_G,
\]
so all eigenvalues have real part \(k/2\), and \(V=0\). Hence the case \(L>0\) automatically has \(\epsilon>0\). Also \(V\ne\mathcal C\) in that case, since \(P=I\) would give \(L=\operatorname{Tr}H=0\).

## 2. Exact trace maximum and equality theorem

**Theorem E4.** With these definitions and \(L>0\),
\[
0<L\leq\epsilon,
\]
and the following five statements are equivalent:

1. \(L=\epsilon\).
2. \(P=Q\).
3. \(V\) reduces \(A\): both \(V\) and \(V^{\perp_G}\) are \(A\)-invariant.
4. \(PA=AP\).
5. \(T=0\).

Moreover, each statement is equivalent to the positive \(H\)-eigenline being contained in \(V\) and the negative \(H\)-eigenline being contained in \(W\).

**Proof.** Choose vectors \(u_+,u_-\) on those two eigenlines with
\[
\langle u_+,u_+\rangle_G=\langle u_-,u_-\rangle_G=1,
\qquad \langle u_+,u_-\rangle_G=0.
\]
This records the eigenline projectors using the existing form and does not replace that form. The full operator, including its zero eigenspace, is
\[
Hx=\epsilon u_+\langle u_+,x\rangle_G-
\epsilon u_-\langle u_-,x\rangle_G.
\tag{E4a}
\]
Put \(a=\|Pu_+\|_G^2\), \(b=\|Pu_-\|_G^2\). Then
\[
L=\epsilon(a-b),\qquad 0\leq a,b\leq1.
\tag{E4b}
\]
This proves \(L\leq\epsilon\). Equality holds precisely when \(a=1\) and \(b=0\). Orthogonality of \(P\) identifies these equalities with \(u_+\in V\) and \(u_-\in W\). In that case (E4a) gives \(PH(1-P)=0\), and (E2) gives \(T=0\).

By (E1), \(T=0\), reduction of \(A\), and \(PA=AP\) are equivalent. If \(P=Q\), the identity \(AQ=QA\) already proved implies \(PA=AP\). Conversely, if \(T=0\), the decomposition in (E1) is a block diagonal decomposition of the original \(A\). The spectrum of \(B\), with multiplicities, is the selected spectrum, while the characteristic polynomial of \(D\) contains exactly the remaining factors: the full characteristic polynomial is the product of the two block characteristic polynomials. Applying the defining projector polynomial to these blocks gives \(Q=I_V\oplus0_W=P\).

Finally suppose \(T=0\). Equation (E1) shows that \(P\) commutes with \(H\). The two nonzero eigenspaces of \(H\) are one-dimensional. The restriction of an idempotent commuting with \(H\) to either such eigenspace is therefore either identity or zero. It follows that \(a,b\in\{0,1\}\). Since \(\epsilon(a-b)=L>0\), necessarily \(a=1,b=0\), and hence \(L=\epsilon\). This proves every stated implication. \(\square\)

The hypothesis \(L>0\) matters for the converse from reduction to \(L=\epsilon\). For example, an empty selected subspace has \(P=Q=0\) and reduces \(A\), while \(L=0\) may hold with \(\epsilon>0\). The theorem concerns exactly the nonempty right-half-plane subspace that appears in (E3).

## 3. Sharp quantitative trace slack

For a map \(F:W\to V\), set \(\|F\|_{\mathrm{HS},G}^2=\operatorname{Tr}_W(F^\sharp F)\). This is the Hilbert-Schmidt norm with the original restricted metrics on both its domain and codomain.

Keep \(u_+,u_-\) as above and set
\[
c=\langle Pu_+,Pu_-\rangle_G,
\qquad M=\begin{pmatrix}a&c\\\overline c&b\end{pmatrix}.
\tag{E5}
\]
The matrix \(M\) is the compression of the original orthogonal projection \(P\) to \(E=\operatorname{span}(u_+,u_-)\), expressed in that specified eigenbasis. For \(z=(z_+,z_-)\),
\[
z^*Mz=\|P(z_+u_++z_-u_-)\|_G^2,
\qquad
z^*(I_2-M)z=\|(1-P)(z_+u_++z_-u_-)\|_G^2.
\tag{E6}
\]
Both matrices are positive semidefinite. In particular,
\[
ab-|c|^2\geq0,
\qquad (1-a)(1-b)-|c|^2\geq0.
\tag{E7}
\]

**Theorem E8.** The exact identity is
\[
\boxed{\quad
\epsilon^2-L^2-\|T\|_{\mathrm{HS},G}^2
 =\epsilon^2\bigl(\det M+\det(I_2-M)\bigr).
\quad}
\tag{E8}
\]
Consequently,
\[
\boxed{\quad
\epsilon^2-L^2\geq\|T\|_{\mathrm{HS},G}^2,
\qquad
\epsilon-L\geq\frac{\|T\|_{\mathrm{HS},G}^2}{\epsilon+L}.
\quad}
\tag{E9}
\]

**Proof.** By (E2) and selfadjointness of \(H\),
\[
\begin{aligned}
\|T\|_{\mathrm{HS},G}^2
 &=\operatorname{Tr}_V\bigl(PH(1-P)HP|_V\bigr)\\
 &=\operatorname{Tr}_{\mathcal C}(PH^2P)
   -\operatorname{Tr}_{\mathcal C}\bigl((PHP)^2\bigr).
\end{aligned}
\tag{E10}
\]
Formula (E4a) gives \(H^2x=\epsilon^2u_+\langle u_+,x\rangle_G+\epsilon^2u_-\langle u_-,x\rangle_G\). Thus the first trace on the right is \(\epsilon^2(a+b)\). The compressed operator is the difference of the two rank-one maps generated by \(Pu_+\) and \(Pu_-\), with coefficient \(\epsilon\). Squaring these maps and taking their traces gives
\[
\operatorname{Tr}_{\mathcal C}\bigl((PHP)^2\bigr)
 =\epsilon^2(a^2+b^2-2|c|^2).
\]
For clarity, the cross trace used here is
\(\operatorname{Tr}((v\langle v,\cdot\rangle_G)(w\langle w,\cdot\rangle_G))=|\langle v,w\rangle_G|^2\), directly by composition of the two rank-one maps. Therefore
\[
\|T\|_{\mathrm{HS},G}^2
 =\epsilon^2(a+b-a^2-b^2+2|c|^2).
\tag{E11}
\]
Subtract this expression and \(L^2=\epsilon^2(a-b)^2\) from \(\epsilon^2\). The result is
\[
\epsilon^2(1-a-b+2ab-2|c|^2)
 =\epsilon^2\bigl((ab-|c|^2)+((1-a)(1-b)-|c|^2)\bigr),
\]
which is exactly (E8). Inequalities (E7) prove its nonnegativity, and division by the positive number \(\epsilon+L\) proves the second inequality in (E9). \(\square\)

Equality in the first inequality of (E9) holds precisely when \(M\) has eigenvalues zero and one. Indeed, its eigenvalues \(\mu_1,\mu_2\) lie in \([0,1]\), and the two nonnegative determinants both vanish precisely when \(\mu_1\mu_2=0\) and \((1-\mu_1)(1-\mu_2)=0\). This is equivalent to the two eigenvalues being zero and one. It also means that \(E\) reduces \(P\) and that \(P|_E\) has rank one: a compression eigenvector with eigenvalue zero satisfies \(\|Px\|^2=0\), while a compression eigenvector with eigenvalue one satisfies \(\|(1-P)x\|^2=0\), by (E6). The reverse implication follows by restricting a rank-one orthogonal projection on \(E\).

The same inequality can be expressed by exact commutators on \(\mathcal C\):
\[
[P,A]=\begin{pmatrix}0&T\\0&0\end{pmatrix},\qquad
[P,H]=\begin{pmatrix}0&T\\-T^\sharp&0\end{pmatrix},
\]
so
\[
\epsilon^2-L^2\geq\|[P,A]\|_{\mathrm{HS},G}^2
 =\tfrac12\|[P,H]\|_{\mathrm{HS},G}^2.
\tag{E12}
\]

## 4. Exact morphism from the projector difference to the coupling

Because \(Q\) has image \(V\) and restricts to identity on \(V\), there is a unique linear map \(X:W\to V\) such that
\[
Q=\begin{pmatrix}I_V&X\\0&0\end{pmatrix},\qquad
Q-P=\begin{pmatrix}0&X\\0&0\end{pmatrix}.
\tag{E13}
\]
The equation \(AQ=QA\), with (E1), yields the **exact Sylvester morphism**
\[
\mathscr S_{B,D}:\operatorname{Hom}_{\mathbb C}(W,V)
   \longrightarrow\operatorname{Hom}_{\mathbb C}(W,V),
\qquad \mathscr S_{B,D}(X)=BX-XD=T.
\tag{E14}
\]
It is an isomorphism. Here is an explicit proof and inverse retaining the original metrics. Set
\(\beta=\min_{\lambda\in\sigma(B)}\operatorname{Re}\lambda\) and
\(\delta=\max_{\mu\in\sigma(D)}\operatorname{Re}\mu\). By the full spectral selection, \(\beta>k/2\geq\delta\). The original operator exponentials have polynomial-times-exponential bounds because each nilpotent part in each generalized eigenspace has finite order. More explicitly, with the spectral projectors \(\Pi^B_\lambda,\Pi^D_\mu\) and their nilpotency orders \(\nu^B_\lambda,\nu^D_\mu\), the exact formulas are
\[
e^{-tB}=\sum_{\lambda\in\sigma(B)}e^{-t\lambda}
 \sum_{j=0}^{\nu^B_\lambda-1}\frac{(-t)^j}{j!}
 (B-\lambda I)^j\Pi^B_\lambda,
\]
\[
e^{tD}=\sum_{\mu\in\sigma(D)}e^{t\mu}
 \sum_{\ell=0}^{\nu^D_\mu-1}\frac{t^\ell}{\ell!}
 (D-\mu I)^\ell\Pi^D_\mu.
\tag{E15}
\]
These formulas follow by expanding the exponential of scalar plus nilpotent on every generalized eigenspace; every sum in the nilpotent part terminates at the displayed order. Consequently the following integral converges in the original operator norm, for every \(Y:W\to V\):
\[
\mathscr S_{B,D}^{-1}(Y)=\int_0^\infty e^{-tB}Y e^{tD}\,dt.
\tag{E16}
\]
Differentiating the integrand and integrating its derivative from zero to infinity proves
\[
B\left(\int_0^\infty e^{-tB}Y e^{tD}dt\right)
-\left(\int_0^\infty e^{-tB}Y e^{tD}dt\right)D=Y.
\]
There is no upper-end boundary term, by \(\beta-\delta>0\) and the finite polynomial factors in (E15). If \(BZ-ZD=0\), differentiation shows that \(e^{-tB}Ze^{tD}\) is constantly \(Z\), while the same decay shows its limit is zero. Thus \(Z=0\), proving uniqueness and the asserted isomorphism.

Equip \(\operatorname{Hom}(W,V)\) with its original Hilbert-Schmidt norm, and define its actual positive smallest singular value
\[
s_{B,D}=\min_{\|Y\|_{\mathrm{HS},G}=1}
\|BY-YD\|_{\mathrm{HS},G}>0.
\tag{E17}
\]
The minimum exists because the unit sphere is compact, and is positive because (E14) is injective. The identity (E13) gives \(\|X\|_{\mathrm{HS},G}=\|Q-P\|_{\mathrm{HS},G}\). Combining (E9), (E14), and (E17) proves
\[
\boxed{\quad
\epsilon^2-L^2\geq\|T\|_{\mathrm{HS},G}^2
\geq s_{B,D}^2\|Q-P\|_{\mathrm{HS},G}^2.
\quad}
\tag{E18}
\]
Thus the difference between the algebraic spectral projector and the orthogonal projection is related to the trace defect by a proved, invertible, typed map.

An explicit bound on the inverse is also available with all original operator norms retained. Write
\[
\kappa_{B,D}=\int_0^\infty
 \|e^{-tB}\|_{\mathrm{op},G}\|e^{tD}\|_{\mathrm{op},G}\,dt<\infty.
\]
The ideal inequality \(\|RY S\|_{\mathrm{HS}}\leq\|R\|_{\mathrm{op}}\|Y\|_{\mathrm{HS}}\|S\|_{\mathrm{op}}\) follows by diagonalizing the positive operators \(R^\sharp R\) and \(SS^\sharp\) in their respective existing Hermitian spaces and bounding their largest eigenvalues. Applying it under (E16) yields
\[
\|Q-P\|_{\mathrm{HS},G}
\leq\kappa_{B,D}\|T\|_{\mathrm{HS},G}
\leq\kappa_{B,D}\sqrt{\epsilon^2-L^2}.
\tag{E19}
\]
If desired, (E15) gives the fully specified finite upper bound
\[
\kappa_{B,D}\leq
\sum_{\lambda,\mu}
\sum_{j=0}^{\nu^B_\lambda-1}
\sum_{\ell=0}^{\nu^D_\mu-1}
\frac{(j+\ell)!\,
 \|(B-\lambda I)^j\Pi^B_\lambda\|_{\mathrm{op},G}
 \|(D-\mu I)^\ell\Pi^D_\mu\|_{\mathrm{op},G}}
{j!\,\ell!\,(\operatorname{Re}\lambda-\operatorname{Re}\mu)^{j+\ell+1}}.
\tag{E20}
\]
The scalar integral used is \(\int_0^\infty t^n e^{-at}dt=n!/a^{n+1}\) for \(a>0\), proved by the substitution \(v=at\) and \(n\) integrations by parts beginning with \(\int_0^\infty e^{-v}dv=1\). Every denominator in (E20) is positive. No bound on nonnormal operator norms has been replaced by a bound on eigenvalue real parts.

## 5. Sharp original two-dimensional family

Fix \(k\in\mathbb R\), \(\ell>0\), and \(t\in\mathbb C\). On \(\mathbb C^2\) with its specified form \(G=I_2\), define
\[
A=\begin{pmatrix}k/2+\ell/2&t\\0&k/2-\ell/2\end{pmatrix},
\qquad H=A^*+A-kI_2=\begin{pmatrix}\ell&t\\\overline t&-\ell\end{pmatrix}.
\tag{E21}
\]
Here \(H^2=(\ell^2+|t|^2)I_2\), so \(\epsilon=\sqrt{\ell^2+|t|^2}\). The selected full generalized spectral subspace is exactly \(V=\mathbb C(1,0)\), since the two eigenvalues \(k/2\pm\ell/2\) are distinct. The original orthogonal projection is \(P=\operatorname{diag}(1,0)\). Hence
\[
L=\ell,\qquad T=t:\mathbb C\to\mathbb C,
\qquad Q=\begin{pmatrix}1&t/\ell\\0&0\end{pmatrix},
\qquad s_{B,D}=\ell.
\tag{E22}
\]
The formula for \(Q\) is also obtained directly from the polynomial \((A-(k/2-\ell/2)I_2)/\ell\); thus its stated kernel is the full other eigenspace, with no orthogonality assumption. Direct calculation gives
\[
\epsilon^2-L^2=|t|^2
=\|T\|_{\mathrm{HS},G}^2
=s_{B,D}^2\|Q-P\|_{\mathrm{HS},G}^2.
\tag{E23}
\]
Both quantitative constants in (E18) are attained by this family, including every \(t\ne0\). The equality theorem gives \(L=\epsilon\) precisely when \(t=0\), exactly when \(P=Q\) and the selected subspace reduces \(A\).

## 6. Critical generalized blocks at the trace maximum

The equality theorem also constrains every full critical generalized block, including its original nilpotent structure.

**Theorem E24.** Suppose \(L>0\) and \(L=\epsilon\). For every eigenvalue \(\lambda\) of the original operator \(A\) with \(\operatorname{Re}\lambda=k/2\), let
\[
Z_\lambda=\ker(A-\lambda I)^{\nu_\lambda}
\]
be its full generalized eigenspace, where \(\nu_\lambda\) is its original exponent in the minimal polynomial. Then
\[
H Z_\lambda=0,\qquad
A|_{Z_\lambda}=\lambda I_{Z_\lambda},\qquad
A^\sharp|_{Z_\lambda}=(k-\lambda)I_{Z_\lambda}=\overline\lambda I_{Z_\lambda}.
\tag{E24}
\]
In particular, \(Z_\lambda\) reduces \(A\), its spectral projector equals its \(G\)-orthogonal projection, and the original eigenvalue \(\lambda\) is semisimple. Consequently, the presence of even one critical-line Jordan chain of length greater than one implies the strict inequality
\[
\epsilon>L
\tag{E25}
\]
whenever \(L>0\).

**Proof.** At equality, Theorem E4 gives \(P=Q\), \(u_+\in V\), and \(u_-\in W\). Hence the restriction of the original Hermitian defect to the original orthogonal complement is
\[
H|_W:w\longmapsto-\epsilon u_-\langle u_-,w\rangle_G.
\tag{E26}
\]
It is negative semidefinite and has rank one. Every critical generalized eigenspace is in \(\ker Q=W\), by the defining polynomial for \(Q\). This conclusion uses the proved equality \(P=Q\); it makes no claim that the original unselected spectral subspace was orthogonal before that equality was proved.

Fix such a \(\lambda\), and let \(R_\lambda\) be the original \(G\)-orthogonal projection onto \(Z_\lambda\). The subspace \(Z_\lambda\) is \(A\)-invariant. With \(A_\lambda=A|_{Z_\lambda}\), its compressed Hermitian form is therefore
\[
R_\lambda H|_{Z_\lambda}
=A_\lambda^\sharp+A_\lambda-kI_{Z_\lambda}.
\tag{E27}
\]
The adjoint on the right uses the original form restricted to \(Z_\lambda\); (E27) follows from the defining adjoint identity for two vectors in that subspace. The trace is
\[
\operatorname{Tr}_{Z_\lambda}(R_\lambda H|_{Z_\lambda})
=2\operatorname{Re}\operatorname{Tr}A_\lambda-k\dim Z_\lambda
=(2\operatorname{Re}\lambda-k)\dim Z_\lambda=0.
\tag{E28}
\]
Here \(A_\lambda=\lambda I+N_\lambda\) with \(N_\lambda\) nilpotent, so \(\operatorname{Tr}A_\lambda=\lambda\dim Z_\lambda\). To justify the nilpotent trace directly, choose a basis compatible with the filtration \(\ker N_\lambda^j\); the map \(N_\lambda\) lowers that filtration and its matrix has zero diagonal.

Choose any \(G\)-orthonormal basis \(z_1,\ldots,z_r\) of \(Z_\lambda\), solely to evaluate the trace in its existing form. Equations (E26) and (E28) give
\[
0=\sum_{j=1}^r\langle z_j,H z_j\rangle_G
=-\epsilon\sum_{j=1}^r|\langle u_-,z_j\rangle_G|^2.
\tag{E29}
\]
Since \(\epsilon>0\), every displayed square is zero. Formula (E26) now gives \(H z_j=0\) for every basis vector, and hence \(H Z_\lambda=0\).

The defining equation \(H=A^\sharp+A-kI\) implies, for every \(z\in Z_\lambda\),
\[
A^\sharp z=kz-Az\in Z_\lambda.
\tag{E30}
\]
Thus \(Z_\lambda\) is invariant under both \(A\) and \(A^\sharp\). Its orthogonal complement is \(A\)-invariant: if \(w\perp_G Z_\lambda\) and \(z\in Z_\lambda\), then
\(\langle z,Aw\rangle_G=\langle A^\sharp z,w\rangle_G=0\).
It is also \(A^\sharp\)-invariant by the corresponding identity with \(A\) and \(A^\sharp\) exchanged. This proves the asserted reduction and shows that the restricted adjoint in (E27) is the actual restriction of \(A^\sharp\).

On \(Z_\lambda\) put \(N=A_\lambda-\lambda I\). It is nilpotent by the definition of this full generalized eigenspace, and (E30) gives
\[
N^\sharp=kI-A_\lambda-\overline\lambda I
=\lambda I-A_\lambda=-N,
\tag{E31}
\]
because \(\lambda+\overline\lambda=k\). A nilpotent skew-adjoint map on a positive-definite Hermitian space is zero, as the following calculation proves. If \(N\ne0\), take its nilpotency order \(r\geq2\), choose \(v\) with \(N^{r-1}v\ne0\), and set \(y=N^{r-1}v\), \(z=N^{r-2}v\). Then \(Nz=y\ne0\) and \(Ny=0\), whereas
\[
\|y\|_G^2=\langle Nz,y\rangle_G
=\langle z,N^\sharp y\rangle_G
=-\langle z,Ny\rangle_G=0,
\tag{E32}
\]
contradicting positive definiteness. Consequently \(N=0\), proving (E24).

Because \(Z_\lambda\) reduces \(A\), the original orthogonal direct sum \(\mathcal C=Z_\lambda\oplus Z_\lambda^{\perp_G}\) gives a block diagonal matrix for \(A\). The complement contains exactly the other generalized eigenspaces: its characteristic polynomial is the quotient of the full characteristic polynomial by that of the full \(\lambda\)-generalized block, so it has no eigenvalue \(\lambda\). The polynomial spectral projector for \(\lambda\) is therefore identity on \(Z_\lambda\) and zero on its orthogonal complement. It equals \(R_\lambda\), as claimed. Finally, (E4) already proves \(L\leq\epsilon\); (E24) rules out equality whenever a critical Jordan chain of length greater than one is present. This gives (E25). \(\square\)

Distinct critical eigenspaces are also mutually orthogonal in the original form. For \(x\in Z_\lambda\), \(y\in Z_\mu\), (E24) gives
\[
\overline\lambda\langle x,y\rangle_G
=\langle Ax,y\rangle_G
=\langle x,A^\sharp y\rangle_G
=\overline\mu\langle x,y\rangle_G.
\]
If \(\lambda\ne\mu\), the inner product vanishes. Therefore the full critical subspace \(Z=\bigoplus_{\operatorname{Re}\lambda=k/2}Z_\lambda\) is an original orthogonal sum, reduces \(A\), and has the exact diagonal action \(\sum_\lambda\lambda R_\lambda\), with \(H|_Z=0\). The shifted operator \(A|_Z-(k/2)I_Z\) is skew-adjoint. This describes the full critical block and its projectors, retaining all its original eigenvalues and multiplicities.

## 7. Integration scope

Equations (E3), (E4), (E8), (E18), and (E24) may be applied directly whenever the exterior-amplification construction supplies its actual finite Hermitian form, its original multiplication operator, and its proved rank-two trace-zero Hermitian defect. All constants \(G,k,\epsilon,L,s_{B,D}\) remain attached to that specific construction and degree. The proof establishes an equality classification, an exact projector morphism, a sharp quantitative slack identity, and strictness in the presence of a retained critical Jordan chain. It supplies no uniform estimate for \(s_{B,D}\), \(\kappa_{B,D}\), or \(\epsilon\) as arithmetic parameters change; such an estimate would require a further calculation on those original varying objects.

Independent algebra check: the determinant-slack calculation (E8)--(E11), its equality classification, and the sharp family (E21)--(E23) were separately recomputed by the bounded `determinant_slack_check` agent. That agent then independently checked all steps of (E24)--(E32), including the passage from zero compressed trace to ambient annihilation and the use of full primary spaces in identifying the projectors. Both derivations agreed with the formulas above. The projector conclusion applies to each full primary space, including every Jordan block at its eigenvalue; it asserts nothing about arbitrary coordinate projectors onto individually selected copies of a repeated eigenspace. These are second mathematical derivations, not Lean or numerical certificates.
