# Scalar recovery, every primary angle, and the complete complementary energy minimum

Independent derivation, 22 September 2026. The complete supplied 04_received.md was read; 05_received.md is its identical copy. The original source and observation definitions of 01_received.md and 03_received.md are retained. Every statement below is finite unless its asymptotic specialization is explicitly identified. The actual period-dependent scalar samples and the residual \(kq\) coefficient remain unevaluated.

The supplied transverse scalar interpolation and logarithmic-angle bounds are valid. Their complete rank-changing extension uses \(p=\operatorname{rank}(TI_K)\), not the full kernel dimension in the positive list. Beyond those statements, the scalar leading coefficient and the complete complementary energy minimum give a sharper determinant interval of optimal dimension-dependent width. This continuation derives that interval, its exact connecting map and its original-kernel receiver.

## SD1. Original metric, maps, and all ranks

Let \(E=\mathbb C^q\) have the original positive Hermitian metric \(G\), let the full original observation \(\Lambda:E\to B\) be onto, and put
\[
K=\ker\Lambda,\quad m=\dim K,\quad b=\dim B=q-m,\quad
Q=(\Lambda G^{-1}\Lambda^*)^{-1},\quad
L=G^{-1}\Lambda^*Q,\quad H_K=I_K^*GI_K.
\tag{SD1}
\]
Here \(I_K:\mathbb C^m\hookrightarrow E\) is the fixed full original kernel frame. Direct multiplication gives \(\Lambda L=I\), \(L^*GL=Q\), and \(I_K^*GL=0\). Thus \([L,J_K]\), where \(J_K=I_KH_K^{-1/2}\), gives an orthogonal decomposition with metric \(\operatorname{diag}(Q,I_m)\).

Retain the actual word \(T\) and define
\[
H=G^{-1}T^*GT,\quad V=\ker T=\ker H,\quad
\Delta=\operatorname{rank}T,\quad d=q-\Delta,\quad
K_0=K\cap V,\quad t=\dim K_0,\quad p=m-t,\quad \delta_+=\Delta-p.
\tag{SD2}
\]
All these ranks are algebraic; no numerical threshold defines them. Positivity gives
\(\ker(J_K^*GHJ_K)=J_K^{-1}K_0\), so \(p=\operatorname{rank}(TI_K)\le\Delta\) and \(\delta_+\ge0\).
Let
\[
A_K=J_K^*GHJ_K,\qquad
\Gamma=J_K^*GP_{V^{\perp_G}}J_K,\qquad
\mathscr Y(z)=\Lambda z(zI+H)^{-1}L,\qquad f(z)=\det_B\mathscr Y(z).
\tag{SD3}
\]
Both \(A_K\) and \(\Gamma\) have the same kernel \(J_K^{-1}K_0\). On its Euclidean orthogonal complement, equivalently the attained metric quotient \(K/K_0\), write their positive restrictions as \(A_+\) and \(\Gamma_+\). Their \(p\) eigenvalues are positive; \(0<\Gamma_+\preceq I_p\). Empty determinants are one.

For the original simple-quartet family,
\[
k\equiv1\pmod4,\quad k\ge17,\quad q=(k+1)^2,\quad
m=8k-16,\quad\Delta=16k-48,\quad d=(k-7)^2.
\tag{SD4}
\]
The real roots remain \(\omega_{ab}=(2b-k)\gamma-i(2a-k)\delta\), \(0<\delta<1/2\), \(\gamma>2\). The coefficient action is \(M[p]=[yp]\) on \(\mathbb C[y]/Q_k\), the physical action is \(kI/2+iM\), and \(T=D_k(M)\) uses the full original pivot-translated interior word. The original conductor proves \(K\cap V=0\), so here \(t=0,p=m,\delta_+=8k-32\). The full \(\Lambda\), all invariant constraints, the original physical unit, and each arithmetic metric \(G_N\) remain unchanged.

The coefficient transport \(S\) acts simultaneously by \(T'=STS^{-1}\), \(G'=S^{-*}GS^{-1}\), \(\Lambda'=\Lambda S^{-1}\), \(L'=SL\), \(H'=SHS^{-1}\); hence \(\mathscr Y'=\mathscr Y\) exactly. A common source mass \(aG\) changes \(Q,H_K\) by \(a\) and leaves \(L,H,\mathscr Y,A_K,\Gamma\) unchanged. This verifies metric balancing without discarding an actual source mass.

## SD2. Complete scalar determinant and multiplicities

In the frame \([L,J_K]\), put \(B_E=L^*GHL\), \(C=J_K^*GHL\). The form of \(zI+H\) is
\[
\begin{pmatrix}zQ+B_E&C^*\\ C&zI_m+A_K\end{pmatrix}.
\]
For \(z>0\), elimination of the full lower block gives
\[
\mathscr Y(z)=z\,[zQ+B_E-C^*(zI_m+A_K)^{-1}C]^{-1}Q.
\]
Its determinant, including the metric determinant \(Q\), is therefore
\[
f(z)=z^{q-m}\frac{\det(zI_m+A_K)}{\det(zI_q+H)}
=z^{\delta_+}
\frac{\prod_{j=1}^{p}(z+\alpha_j)}
{\prod_{j=1}^{\Delta}(z+\lambda_j)}.
\tag{SD5}
\]
Here every positive eigenvalue \(\alpha_j\) of \(A_K\) and \(\lambda_j\) of \(H\) is listed with full multiplicity. Indeed the numerator before positive-factor extraction has \(t\) zero factors and the denominator has \(d\), so its zero order is \(q-m+t-d=\Delta-p\). The determinant calculation uses
\(\det(zI+H)=\det(\text{displayed form})/\det Q\); this is why no \(Q\)-factor is missing.

This is also the rank-changing formula PR7–8 in the [original measured-resolvent proof](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/13ca9b136fcdae48df7454bd9bf99e1ef22dd03c/workbenches/splitzero-tandem/continuations/20260922-original-growth-resolvent/RECEIVED_RESOLVENT_PROOFS.md), rederived here directly from the original forms. The Feshbach–Schur construction is treated by Geneviève Dusson, Israel Michael Sigal and Benjamin Stamm, Theorem 1.2 and equations labelled Fesh and QP in their [original author source, arXiv:2105.02058](https://arxiv.org/abs/2105.02058). The finite determinant and rank accounting in (SD5) are proved above.

For each \(a>0\), define its two multiplicities \(n_A(a)\), \(n_H(a)\).
The common divisor has multiplicity \(\min(n_A(a),n_H(a))\); the reduced numerator and denominator retain respectively
\[
n_{\rm num}(a)=(n_A(a)-n_H(a))_+,\qquad
n_{\rm den}(a)=(n_H(a)-n_A(a))_+.
\tag{SD6}
\]
This definition permits repeated energies and exact cancellations without identifying cancellation with matrix-memory invisibility.

Fix a proved positive spectral interval
\[
\ell P_{V^{\perp_G}}\preceq_G H\preceq_G uP_{V^{\perp_G}},
\qquad0<\ell\le u,\qquad w=\log(u/\ell).
\tag{SD7}
\]
If \(\Delta=0\), \(H=0\), \(p=0\), and \(f=1\); no positive spectral interval is needed. When \(\Delta>0\), every \(0<\alpha<\ell\) has \(n_H(\alpha)=0\), and therefore survives with its entire multiplicity. Equality \(\alpha=\ell\) is deliberately excluded from that conclusion.

The full zero multiplicity of \(\Gamma\) is exactly \(t\). Among its \(p\) positive eigenvalues, at most
\[
a_{\max}=\min(p,d-t)
\tag{SD8}
\]
are nonunit. To prove this, \(I-\Gamma_+\) is the Gram of the map from \(K_0^{\perp_G}\cap K\) to \(V\). Its image is perpendicular to \(K_0\), because the original vector is perpendicular to \(K_0\subset V\). Thus its rank is at most \(\dim(V\cap K_0^{\perp_G})=d-t\), and also at most \(p\). This bound retains unit factors even when \(d<m\).

## SD3. Every logarithmic angle and inverse exterior rank

Congruence of (SD7) by \(J_K\), then restriction to the positive part, gives
\[
\ell\Gamma_+\preceq A_+\preceq u\Gamma_+.
\tag{SD9}
\]
Order both positive eigenvalue lists increasingly. Rayleigh min–max gives
\(\ell\gamma_j\le\alpha_j\le u\gamma_j\) in that same ordering. This needs no commutation. Put \(h_j=-\log\gamma_j\), so \(h_1\ge\cdots\ge h_p\ge0\).

The reduced scalar numerator determines exactly
\[
\widehat h_j=(\log(\ell/\alpha_j))_+,\qquad1\le j\le p,
\tag{SD10}
\]
by taking every subgap factor, retaining its multiplicity, and padding the decreasing list with zeros to length \(p\). A missing canceled positive energy is at least \(\ell\), so contributes exactly zero to this list.

If \(\alpha_j\le\ell\), then
\(h_j-\widehat h_j=\log(\alpha_j/(\ell\gamma_j))\in[0,w]\).
If \(\alpha_j>\ell\), then \(\gamma_j\ge\alpha_j/u>\ell/u\), so
\(0\le h_j<w\) and \(\widehat h_j=0\). Hence
\[
0\le h_j-\widehat h_j\le w,\qquad
h_j=\widehat h_j=0\quad(j>a_{\max}),
\tag{SD11}
\]
and for all \(0\le r\le p\),
\[
0\le\sum_{j=1}^r(h_j-\widehat h_j)\le\min(r,a_{\max})w.
\tag{SD12}
\]
This includes every positive exterior rank and improves the rank coefficient when the zero-word space is smaller.

The actual map is
\[
J=P_{V^{\perp_G}}J_{K,+}:\mathbb C^p\longrightarrow V^{\perp_G}.
\]
Its image has the inherited original \(G\)-metric; \(J^*GJ=\Gamma_+\).
Thus its inverse on that actual image has squared singular values
\(1/\gamma_1,\ldots,1/\gamma_p\). Therefore
\[
e^{\sum_{j=1}^r\widehat h_j}
\le\|\wedge^r(J^{-1}|_{\operatorname{im}J})\|^2
\le e^{\min(r,a_{\max})w+\sum_{j=1}^r\widehat h_j}.
\tag{SD13}
\]
If \(t>0\), the unreduced map on all \(K\) is not injective. Its \(t\) zero singular values are retained; an inverse on all \(K\) is not asserted. Equation (SD13) refers to its exact attained quotient, or equivalently the inverse into \(K_0^{\perp_G}\cap K\).

For every \(s\ge0\),
\[
\#\{j:h_j>s+w\}\le\#\{j:\widehat h_j>s\}
\le\#\{j:h_j>s\}.
\tag{SD14}
\]
After division by a common \(q\), the ordered lists differ in \(W_\infty\) by at most \(w/q\), and in every \(W_r\), \(1\le r<\infty\), by at most the same amount. Any common centering leaves this statement unchanged. For \(p=0\) use the empty list, not an undefined empirical probability measure.

## SD4. The entire retained numerator sharpens the ordered upper bound

Let \(\mathscr A_{\rm ret}\) be all reduced numerator energies in physical units, with cardinality \(n\), and let \(c=p-n\) be the cancellation degree. Form an increasing list
\[
a_1^-\le\cdots\le a_p^-
\quad\text{from }\mathscr A_{\rm ret}\cup\{\ell\}^{c}.
\tag{SD15}
\]
The actual positive energy list is obtained by replacing these \(c\) copies of \(\ell\) by the actual canceled energies, each at least \(\ell\). Therefore \(a_j^-\le\alpha_j\) at every index. All energies are at most \(u\), because \(A_+\preceq u\Gamma_+\preceq uI\). Define
\[
\beta_j=\begin{cases}\log(u/a_j^-),&j\le a_{\max},\\0,&j>a_{\max}.\end{cases}
\tag{SD16}
\]
This is decreasing and nonnegative. Min–max and (SD8) give the complete ordered enclosure
\[
\widehat h_j\le h_j\le\beta_j,\qquad
0\le\beta_j-\widehat h_j\le w.
\tag{SD17}
\]
For the second inequality before the forced-zero tail, use
\(\widehat h_j=(\log(\ell/a_j^-))_+\).
If \(a_j^-\le\ell\), the interval width is \(w\); if \(a_j^->\ell\), it is \(\log(u/a_j^-)\le w\).
This also proves that the forced-zero tail of the lower list really is zero.

Put
\[
U=\sum_{j=1}^{p}\widehat h_j,\qquad V_{\rm ret}=\sum_{j=1}^{p}\beta_j.
\tag{SD18}
\]
Then \(U\le-\log\det\Gamma_+\le V_{\rm ret}\), with
\(V_{\rm ret}-U\le a_{\max}w\).
Without the rank improvement \(a_{\max}\), the upper endpoint is exactly
\(\sum_{\alpha\in\mathscr A_{\rm ret}}\log(u/\alpha)+c\,w\), the supplied equation (10).
For every exterior rank one may instead sum the first \(r\) terms in (SD17).
The midpoint list \(b_j=(\widehat h_j+\beta_j)/2\) is ordered, satisfies
\[
|h_j-b_j|\le(\beta_j-\widehat h_j)/2\le w/2,
\tag{SD19}
\]
and hence approximates each logarithmic angle with half the maximum interval width. This is a two-sided estimate; it does not claim a stronger one-sided error for the original lower list.

## SD5. Exact scalar interpolation, including all cancellations

Choose \(R\ge\|H\|_G\), with \(R>0\). Define \(\mathcal L=p+\Delta\).
If \(\mathcal L=0\), \(f=1\) and zero samples suffice. Otherwise use the distinct nodes
\[
x_i=1+i/\mathcal L,\quad z_i=Rx_i,\quad0\le i<\mathcal L,
\quad r_i=x_i^{-\delta_+}f(Rx_i).
\tag{SD20}
\]
All lie in \([R,2R)\). The underlying rational function is
\[
r_R(x)=x^{-\delta_+}f(Rx)
=\frac{P(x)}{D(x)},\quad
P(x)=\prod_{j=1}^p(x+\alpha_j/R),\quad
D(x)=\prod_{j=1}^{\Delta}(x+\lambda_j/R).
\tag{SD21}
\]
The powers of \(R\) cancel because \(\delta_+=\Delta-p\); the roots still carry their exact physical scale.

Both polynomials are monic. Their lower coefficients solve
\[
\sum_{j<p}a_jx_i^j-r_i\sum_{j<\Delta}b_jx_i^j
=r_ix_i^\Delta-x_i^p,\quad0\le i<\mathcal L.
\tag{SD22}
\]
For any solution \(P_1,D_1\), compare with the actual \(P,D\).
The polynomial \(P_1D-PD_1\) vanishes at all nodes and has degree at most
\(p+\Delta-1=\mathcal L-1\), since the leading terms cancel. It is identically zero. Thus every solution represents the same rational function after exact common-factor cancellation. A solution may have both numerator and denominator zero at a sample node; cancel their gcd before evaluation. Such an intermediate \(0/0\) does not invalidate the polynomial proof.

More precisely, let \(P_0,D_0\) be the coprime monic reduced pair, of degrees \(n=p-c\), \(d_0=\Delta-c\). Coprimality and \(P_1D_0=P_0D_1\) imply
\[
P_1=P_0S,\qquad D_1=D_0S,
\quad S\text{ arbitrary monic of degree }c.
\tag{SD23}
\]
For example \(P_0\mid P_1\) follows by Bézout: multiply
\(UP_0+VD_0=1\) by \(P_1\) and use the cross-product equality.
Monicity fixes \(S\)'s leading coefficient. Conversely every such \(S\) solves (SD22). Therefore the interpolation system has nullity exactly \(c\), including repeated common factors. If the reduced degrees have been established separately, \(n+d_0=p+\Delta-2c\) distinct samples suffice by the same argument. No distinct-energy or generic-rank assumption was used.

In the native transverse family, \(\mathcal L=\Delta+m=24k-64\).
Rank-changing data use the actual \(\Delta+p\), with the zero order \(\Delta-p\); the unreduced full formula (SD5) remains valid at every rank transition.

For the sample bound, \(z(zI+H)^{-1}\) lies between
\(x/(x+1)\) and \(1\) when \(z=Rx\), \(x\ge1\). Compress by the original minimum-section isometry. Moreover the difference from identity has rank at most \(\min(b,\Delta)\). Hence
\[
\left({x\over x+1}\right)^{\min(b,\Delta)}
\le f(Rx)\le1.
\tag{SD24}
\]
In particular \(2^{-\Delta}\le f(Rx)\le1\) on the stated interval.
This controls measured positive matrices and scalar values; it does not bound interpolation conditioning or the number of bits required for tiny positive roots.

## SD6. The scalar leading coefficient and complete complementary energy minimum

The scalar data determine
\[
a_{\rm sc}=\lim_{z\downarrow0}z^{-\delta_+}f(z)
=\frac{\det A_+}{\det(H|_{V^{\perp_G}})}
=R^{-\delta_+}\frac{P_0(0)}{D_0(0)}>0.
\tag{SD25}
\]
The limit is calculated by the recovered polynomial constants, with no further response samples or limiting numerical operation.

Let \(F=P_{V^{\perp_G}}J_{K,+}\), so \(F^*GF=\Gamma_+\), and put
\(U_K=F\Gamma_+^{-1/2}\). This is an isometry onto \(P_{V^{\perp_G}}K\).
Complete it by a \(G\)-isometry \(Z\) onto its orthogonal complement in \(V^{\perp_G}\), of dimension \(\delta_+\).
In this exact orthonormal frame the positive energy is
\[
\begin{pmatrix}\mathcal A&\mathcal C\\
\mathcal C^*&\mathcal D\end{pmatrix},\qquad
\Sigma=\mathcal D-\mathcal C^*\mathcal A^{-1}\mathcal C.
\]
The image lies in \(V^{\perp_G}\), and \(H\) annihilates \(V\), so
\(A_+=\Gamma_+^{1/2}\mathcal A\Gamma_+^{1/2}\).
Block elimination then proves
\[
a_{\rm sc}=\frac{\det\Gamma_+}{\det\Sigma},
\qquad
\det\Gamma_+=a_{\rm sc}\det\Sigma,
\qquad
\Sigma^{-1}=Z^*G(H|_{V^{\perp_G}})^{-1}Z.
\tag{SD26}
\]
The off-diagonal energy block is retained. The transverse identity is precisely PR8a in the cited original measured-resolvent proof; the present proof extends it to the actual quotient at \(t>0\).

The meaning of \(\Sigma\) is the attained energy on each fixed complementary fibre:
\[
y^*\Sigma y=\min_{x\in\mathbb C^p}
\left\langle U_Kx+Zy,H(U_Kx+Zy)\right\rangle_G.
\]
Since the frame is orthonormal, (SD7) implies
\[
\ell I_{\delta_+}\preceq\Sigma\preceq uI_{\delta_+}.
\tag{SD27}
\]
For the lower bound minimize \(\ell(\|x\|^2+\|y\|^2)\); for the upper bound choose \(x=0\). Consequently, with \(S_{\rm sc}=-\log a_{\rm sc}\),
\[
S_{\rm sc}-\delta_+\log u
\le-\log\det\Gamma_+
\le S_{\rm sc}-\delta_+\log\ell.
\tag{SD28}
\]
No individual scalar numerator root is needed for this interval.

Intersect the two independently proved intervals:
\[
L_{\rm sc}=\max\{U,S_{\rm sc}-\delta_+\log u\},\qquad
U_{\rm sc}=\min\{V_{\rm ret},S_{\rm sc}-\delta_+\log\ell\}.
\tag{SD29}
\]
They contain the actual determinant, so \(L_{\rm sc}\le U_{\rm sc}\), and
\[
0\le U_{\rm sc}-L_{\rm sc}
\le \min(p,d-t,\Delta-p)\,\log(u/\ell).
\tag{SD30}
\]
Thus the best certified scalar ambiguity here is governed by the positive kernel dimension, the available zero-word dimension, and the complementary positive-energy dimension. For \(\Delta=p\), (SD26) has an empty complementary determinant and scalar leading-coefficient recovery of \(\det\Gamma_+\) is exact even for a nonflat positive spectrum. Flat spectra also give exact recovery of every positive angle, by (SD9).

## SD7. Sharp examples in every admissible dimension

For \(u>\ell>0\), take \(G=I_3\), \(\Lambda(x_1,x_2,x_3)=(x_1,x_2)\), \(K=\mathbb Ce_3\), and
\[
H_0=\operatorname{diag}(u,0,\ell),\qquad
H_1=\begin{pmatrix}
u-\ell&0&\sqrt{\ell(u-\ell)}\\
0&\ell&0\\
\sqrt{\ell(u-\ell)}&0&\ell
\end{pmatrix}.
\tag{SD31}
\]
They are \(T_i^*T_i\) for
\(T_0=\operatorname{diag}(\sqrt u,0,\sqrt\ell)\) and
\[
T_1=\begin{pmatrix}\sqrt{u-\ell}&0&\sqrt\ell\\
0&\sqrt\ell&0\\0&0&0\end{pmatrix}.
\]
Both have full energies \(\{0,\ell,u\}\), \(A_K=\ell\), \(Q=I_2\), and
\[
\mathscr Y_0(z)=\operatorname{diag}(z/(z+u),1),\quad
\mathscr Y_1(z)=\operatorname{diag}((z+\ell)/(z+u),z/(z+\ell)).
\tag{SD32}
\]
Hence both determinants equal \(z/(z+u)\), while
\(\Gamma_0=1,\Gamma_1=\ell/u\).
The second system's kernel coupling is nonzero. Its scalar cancellation of \(z+\ell\) is not a reducing invisible direction of matrix memory. The two \(\Sigma\) values are respectively \(u,\ell\), realizing both endpoints of (SD28).

For arbitrary admissible \(q,m,\Delta,t\), set
\[
s_*=\min(p,\Delta-p,d-t).
\tag{SD33}
\]
Take \(s_*\) copies of (SD31); add \(p-s_*\) positive kernel-only modes, \(\Delta-p-s_*\) positive observed-only modes, \(t\) zero kernel-only modes, and \(d-t-s_*\) zero observed-only modes. Every count is nonnegative. The total dimension is
\(3s_*+(p-s_*)+(\Delta-p-s_*)+t+(d-t-s_*)=q\);
the kernel dimension is \(p+t=m\), the positive-word rank is \(\Delta\), and its intersection rank is \(t\).
All added blocks agree between the two systems. Thus their scalar data, full positive spectra, observed metrics and algebraic ranks agree, but
\[
\left|\log\det\Gamma_{+,1}-\log\det\Gamma_{+,0}\right|
=s_*\log(u/\ell).
\tag{SD34}
\]
This proves sharpness of the dimension-dependent ambiguity coefficient in (SD30), even with the full positive spectrum supplied in addition to all scalar response values. On the auxiliary pair, each nonunit logarithmic-angle error also attains \(w\); direct sums attain (SD12) wherever the indicated nonunit ranks are available. These examples are finite positive-word systems; they are not asserted to be native xi-packet data.

## SD8. A finite scalar surrogate without individual root extraction

In addition to the leading coefficient, the reconstructed rational function itself gives an explicit approximation to the subgap statistic \(U\). Let \(n=\deg P_0\), \(d_0=\deg D_0\), and \(\tau=\ell/R>0\). Put
\[
\Psi=\log\frac{r_R(\tau)}{r_R(0)}
=\log\frac{P_0(\tau)D_0(0)}{D_0(\tau)P_0(0)}.
\tag{SD35}
\]
All arguments of logarithms are positive. This uses evaluations of the recovered polynomials; it does not request another original response sample.

For each retained numerator energy,
\[
0\le\log(1+\ell/\alpha)-(\log(\ell/\alpha))_+\le\log2.
\]
For each retained denominator energy, \(\lambda\ge\ell\), so
\(0\le\log(1+\ell/\lambda)\le\log2\).
Expanding (SD35) over their full multiplicities proves
\[
-n\log2\le U-\Psi\le d_0\log2.
\tag{SD36}
\]
Thus a ratio of four recovered polynomial values approximates the whole subgap sum within a degree-dependent finite error, even when some numerator roots are arbitrarily small or repeated. In the original family \(n,d_0=O(k)\), this added error is \(O(k)\). It does not assert that computing a very small positive polynomial value requires few bits.

There is also an exact root-independent integral map. In physical units let
\(r(z)=z^{-\delta_+}f(z)\). For \(0<a<\ell\) avoiding numerator roots on the circle, factor its polynomials and use the mean-value identity for each \(z+\alpha\). This gives
\[
\frac1{2\pi}\int_0^{2\pi}
\log\left|\frac{r(ae^{i\theta})}{r(0)}\right|\,d\theta
=\sum_{\alpha<a}\log(a/\alpha).
\tag{SD37}
\]
Denominator factors give zero because their roots lie outside the circle. At boundary zeros, their logarithmic singularities are integrable: for one factor the identity follows directly from the power-series mean outside its root radius and from factoring the radius inside; continuity in the radius follows by integrating \(\log|e^{i\theta}-r|\), or by its explicit value \(\log^+r\). Letting \(a\uparrow\ell\) proves that the same integral at the endpoint, interpreted by this integrable limit, equals \(U\). This connects the exact multiplicity-counted clipping to the recovered scalar holomorphic function without declaring any quadrature error negligible.

## SD9. Original arithmetic receiver and its complete finite spectral width

At the four original cutoffs \(N\in\{q-1,q,2q-1,2q\}\), use
\(\mathcal RF=f_{q-1}+f_q-f_{2q-1}-f_{2q}\).
The original boundary map has kernel \(V\), and
\[
G_N^\partial=(\pi_\partial G_N^{-1}\pi_\partial^*)^{-1},\qquad
\widehat H_{K,N}^\partial=(\pi_\partial I_K)^*G_N^\partial(\pi_\partial I_K).
\]
The exact minimum over the original affine fibres gives
\[
\Gamma_N=H_{K,N}^{-1/2}\widehat H_{K,N}^\partial H_{K,N}^{-1/2},
\quad
\log\det H_{K,N}=\log\det\widehat H_{K,N}^\partial-\log\det\Gamma_N.
\tag{SD38}
\]
Indeed the \(G_N\)-minimum lift of each boundary value is its projection to \(V^{\perp_{G_N}}\); its squared norm is the boundary quotient norm. This proves (SD38) with the actual minimum, without replacing it by a coefficient metric.

The original word provider gives a common boundary comparison
\(a_kI\preceq G_N^\partial\preceq b_kI\) and source nesting
\(G_{N+1}^\partial\preceq G_N^\partial\). Since \(\pi_\partial I_K\) is fixed and injective, each low-to-high log-determinant drop lies in \([0,m\log(b_k/a_k)]\). Thus
\[
0\le\mathcal R\log\det\widehat H_{K,N}^\partial
\le B_\partial:=2m\omega_k,\qquad\omega_k=\log(b_k/a_k).
\tag{SD39}
\]
All constants here retain their original arithmetic source. Explicitly, writing \(R_h=\sqrt{\delta^2+\gamma^2}\) and \(R_k=kR_h\),
\[
a_k=\ell_k/A_{2q}^\partial,\quad b_k=u_kB_k^\partial,\quad
A_{2q}^\partial=\frac{\Delta e^2}{M_\sigma}(2q+1)^{3/2}(4q+1)^{R_k+1},
\]
\[
B_k^\partial=\Delta M_\sigma
\left(\frac{2\Delta+R_k}{2\delta}\right)^{2(\Delta-1)},\qquad M_\sigma=\sqrt{2\pi}.
\]
Here \(\ell_k,u_k\) are the original full-mass arithmetic/Gamma comparison constants of the word provider, not the positive energy thresholds \(\ell_N,u_N\).

For precision at the \(kq\) scale, retain the complete original image-Gram enclosure
\(e^{c_N-\epsilon_k}I\preceq\mathfrak G_N\preceq e^{c_N+\epsilon_k}I\).
Its parameter and equilibrium status are those of the proved/imported original word source, not newly inferred from scalar interpolation. The exact original image map is
\(J=V_O^{-1}\pi_\partial I_K\), and \(H_{TK,N}=J^*\mathfrak G_NJ\).
The full Vandermonde and Lagrange constants are
\[
V_+=\Delta\max(1,R_k)^{\Delta-1},\qquad
V_-=\Delta\left(\frac{1+R_k}{2\delta}\right)^{\Delta-1},
\]
\[
E_k=\epsilon_k+
\max\{\log^+(b_kV_+^2),\log^+(V_-^2/a_k)\}.
\tag{SD40}
\]
The positive word operator is exactly
\((G_N^\partial)^{-1/2}V_O^{-*}\mathfrak G_NV_O^{-1}(G_N^\partial)^{-1/2}\).
Taking both norm bounds and inverse norm bounds proves
\[
e^{c_N-E_k}\le\lambda_{j,N}^+\le e^{c_N+E_k}.
\tag{SD41}
\]
These are [PR19–22 of the pinned original measured-resolvent proof](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/13ca9b136fcdae48df7454bd9bf99e1ef22dd03c/workbenches/splitzero-tandem/continuations/20260922-original-growth-resolvent/RECEIVED_RESOLVENT_PROOFS.md).
Its retained original domain gives \(E_k=o(q)\), \(\omega_k=O_{h,\varpi}(k\log q)=o(q)\), and
\[
c_{\rm L}=2q\log q+(2\log(4/\pi)-2)q,\qquad
c_{\rm H}=c_{\rm L}-C_\partial q/2.
\tag{SD42}
\]
The low type is \(q-1,q\), the high type is \(2q-1,2q\). The finite scalar theorems SD1–37 themselves require only the measured maps and a finite positive spectral interval; no unproved value of \(C_\partial\) enters them.

Set \(\ell_N=e^{c_N-E_k},u_N=e^{c_N+E_k}\).
The supplied angle comparison follows:
\(0\le h_{j,N}-\widehat h_{j,N}\le2E_k=o(q)\).
The original four-sign receiver is
\[
\mathcal R U_N-2E_k(a_{\max,2q-1}+a_{\max,2q})
\le\mathcal K_k
\le\mathcal R U_N+2E_k(a_{\max,q-1}+a_{\max,q})+B_\partial.
\tag{SD43}
\]
On the transverse native family \(a_{\max,N}=\min(m,d)\), independent of \(N\); replacing it by \(m\) gives exactly the incoming \(4mE_k\) bounds. For separate finite widths \(w_N\), replace each \(2E_ka_{\max,N}\) by \(w_Na_{\max,N}\). This also explains every sign in the directed interval.

The leading coefficient yields a second receiver with no individual-root calculation:
\[
\rho_N=\frac{P_{0,N}(0)}{D_{0,N}(0)},\qquad
\Theta_N=-\log\rho_N+\delta_+(\log R_N-c_N).
\tag{SD44}
\]
A separate certified scale \(R_N\) is permitted and is explicitly retained.
From (SD26),(SD41),
\[
|-\log\det\Gamma_N-\Theta_N|\le\delta_+E_k,
\]
and consequently
\[
\mathcal R\Theta_N-4\delta_+E_k
\le\mathcal K_k
\le\mathcal R\Theta_N+4\delta_+E_k+B_\partial.
\tag{SD45}
\]
When one common \(R\) is used, \(\mathcal Rc_N=C_\partial q\), so this is the explicit scalar-constant receiver
\[
-4\delta_+E_k
\le
\mathcal K_k+\mathcal R\log\rho_N+\delta_+C_\partial q
\le4\delta_+E_k+B_\partial,
\quad\delta_+=8k-32.
\tag{SD46}
\]
It determines the same residual \(kq\)-scale coefficient from the recovered scalar constants, up to the stated \(o(kq)\) remainder. No positive regularizer is taken numerically to zero.

For the sharpest finite determinant interval, use (SD29) at each cutoff:
\[
L_{q-1}+L_q-U_{2q-1}-U_{2q}
\le\mathcal K_k
\le U_{q-1}+U_q-L_{2q-1}-L_{2q}+B_\partial.
\tag{SD47}
\]
Here \(L_N=L_{{\rm sc},N}\), \(U_N=U_{{\rm sc},N}\) only in (SD47).
With \(M_N=(L_N+U_N)/2\), it follows that
\[
\left|\mathcal K_k-\mathcal RM_N-B_\partial/2\right|
\le\frac12\sum_N(U_N-L_N)+B_\partial/2.
\tag{SD48}
\]
For the native data the sum is at most \(8s_*E_k\), where
\(s_*=\min(m,\Delta-m,d)\). This centers a fully specified interval; it does not assume that the unknown boundary determinant equals its midpoint.

To connect with the actual lower-root invariant rows, retain
\(g=\Delta-v\), their complete projected covariance gains \(G_0,G_1\), and the exact scalar \(\mathcal A_{k,v}\) from [RG50–54](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/13ca9b136fcdae48df7454bd9bf99e1ef22dd03c/workbenches/splitzero-tandem/continuations/20260922-original-growth-resolvent/GROWTH_PROOFS.md).
That finite theorem gives
\(|\mathcal K_k-\log\mathcal A_{k,v}+G_0+G_1|\le\mathcal E_k\).
Combining it with (SD45) yields
\[
-\mathcal E_k-4\delta_+E_k
\le \log\mathcal A_{k,v}-G_0-G_1-\mathcal R\Theta_N
\le \mathcal E_k+4\delta_+E_k+B_\partial.
\tag{SD49}
\]
Every root, original row and complementary minimum remains in those gains.
This exact directed connection does not identify the rank-\(m\) primary-angle operator with the rank-\(r_k\) lower-root projection. Under the original outer receiver with its retained error \(E_{\rm out}\),
\(|\mathcal K_k-gC_\partial q-\mathcal R\log\det S_N|\le E_{\rm out}\),
substitution in (SD45) gives the same interval enlarged by \(E_{\rm out}\) for
\(gC_\partial q+\mathcal R\log\det S_N-\mathcal R\Theta_N\).
Thus the original scalar \(g\), full lower-root ideal and unresolved invariant-row coefficient are all preserved.

## SD10. Rank-changing kernel metrics and coherent source errors

At \(t>0\), the preceding scalar statements recover the positive determinant, not the zero factors' metric. Here is the exact missing factor in the original coordinates. Choose a fixed full frame \([I_0,I_1]=I_KS\) of \(K\), with \(I_0\) spanning \(K_0\), and write
\[
S^*H_KS=\begin{pmatrix}H_{00}&H_{01}\\H_{01}^*&H_{11}\end{pmatrix},
\qquad H_{\rm quot}=H_{11}-H_{01}^*H_{00}^{-1}H_{01}.
\]
Let \(B_{11}=I_1^*GP_{V^{\perp_G}}I_1\). The boundary form annihilates \(K_0\), so its matrix in this frame is \(\operatorname{diag}(0,B_{11})\).
The nonzero generalized spectrum against \(S^*H_KS\) is that of
\((B_{11},H_{\rm quot})\): block inversion gives its lower inverse block \(H_{\rm quot}^{-1}\).
Therefore
\[
\det_+\Gamma=\frac{\det B_{11}}{\det H_{\rm quot}},\qquad
\log\det H_K
=\log\det H_{00}+\log\det B_{11}
-\log\det_+\Gamma-2\log|\det S|.
\tag{SD50}
\]
This is the complete connecting map at an intersection. The fixed \(S\)-factor cancels under four original signs; the original \(H_{00}\) factor does not disappear.

Its possible invisibility is exact, not a universal reconstruction claim: take \(T=\operatorname{diag}(0,1)\), \(\Lambda=(0,1)\), and \(G_a=\operatorname{diag}(a,1)\), \(a>0\). Then \(K_0=K=\mathbb Ce_1\),
\(f(z)=z/(z+1)\) for every \(a\), but \(\det H_K=a\).
The positive metric cone on \(K_0\) is the exact defect space in this example, and (SD50) states how it re-enters the full kernel determinant.
For \(m=0\), all kernel determinants are empty and \(f(z)=z^\Delta/\prod(z+\lambda_j)\).
For \(T=0\), \(p=\Delta=0\), \(f=1\), and \(\Gamma=0_m\); only the zero-dimensional positive quotient has determinant one. A logarithm of the full zero determinant is not replaced by zero.

Now suppose two complete original source forms satisfy
\(aG\preceq\widetilde G\preceq bG\), \(0<a\le b\), \(\kappa=b/a\), with the same \(T,\Lambda,I_K\).
Restriction to \(K\), restriction of the image form \(I_K^*T^*GTI_K\), and attained quotients by the fixed \(K_0\) retain these same two constants: minimize the corresponding inequalities on each identical affine fibre. Generalized min–max gives
\[
\kappa^{-1}\alpha_j(G)\le\alpha_j(\widetilde G)\le\kappa\alpha_j(G),
\quad
\kappa^{-1}\gamma_j(G)\le\gamma_j(\widetilde G)\le\kappa\gamma_j(G).
\tag{SD51}
\]
For the second statement use the complete boundary quotient by \(V\), then restrict it to \(K/K_0\); its numerator and denominator forms both retain factors \(a,b\).
With one common valid threshold \(\ell\), logarithmic clipping is 1-Lipschitz, and both clipped lists have at most \(a_{\max}\) positive entries. Therefore
\[
|U(\widetilde G)-U(G)|\le a_{\max}\log\kappa,\qquad
|\log\det_+\Gamma(\widetilde G)-\log\det_+\Gamma(G)|
\le a_{\max}\log\kappa.
\tag{SD52}
\]
Every rank-\(r\) positive inverse exterior logarithm has error at most \(\min(r,a_{\max})\log\kappa\).

The leading coefficient also has an explicit coherent bound. The complementary space in SD6 is
\((K+V)^{\perp_G}\). On the fixed quotient \(E/(K+V)\), minimize the energy
\(x^*T^*GT x\) and the metric \(x^*Gx\) on the same affine fibres. The energy minimum is attained: after factoring out \(V\), its form is positive definite and the remaining minimization is an ordinary positive quadratic minimum. Its positive generalized matrix relative to the metric minimum is exactly \(\Sigma\). Both quotient forms inherit the factors \(a,b\), so
\(|\log\det\Sigma(\widetilde G)-\log\det\Sigma(G)|\le\delta_+\log\kappa\).
Together with (SD26),(SD52),
\[
|\log a_{\rm sc}(\widetilde G)-\log a_{\rm sc}(G)|
\le(a_{\max}+\delta_+)\log\kappa.
\tag{SD53}
\]
The sections, adjoints and minima must all be recomputed from their respective complete metrics. Independent rounding of scalar samples does not satisfy these hypotheses.

Indeed for the fixed \(T=\operatorname{diag}(0,1)\), \(\Lambda=(-1,1)\), and
\(G_\varepsilon=\operatorname{diag}((1-\varepsilon)/\varepsilon,1)\),
\[
f_\varepsilon(z)=\frac{z+\varepsilon}{z+1},\qquad
\Gamma_\varepsilon=\varepsilon,\qquad0<\varepsilon<1.
\tag{SD54}
\]
For \(\varepsilon=2^{-L}\), \(\varepsilon'=2^{-L-q}\), the response difference on \([1,2]\) is at most \(2^{-L-1}\), while the angle logarithms differ by \(q\log2\). Every positive full-word energy equals one. Exact interpolation and sharp spectral-width bounds therefore do not remove the needed small-root or small-constant precision.

## SD11. Verification and provenance

The companion exact checker verifies the full physical determinant under nonunitary complex coordinate transport, common-factor multiplicities and interpolation nullities, kernel/word intersections, zero words and empty kernels, the complete complementary Schur identity, dimension-dependent sharp examples, coherent metric errors and finite polynomial-value receivers. Normal and optimized-mode receipts record the proof and checker hashes. These checks are finite auxiliary systems, not evaluations of native period-dependent matrices.

Original human-source reading is recorded precisely in SOURCE_USE_LEDGER.md and JSON. The author TeX of Dusson–Sigal–Stamm is used for the classical Feshbach–Schur context. The polynomial uniqueness argument SD20–23 is proved directly here, independently of a general Loewner realization theorem. Mayo–Antoulas (2007), retained from the incoming bibliography, is contextual attribution, not an assertion that its unavailable author source was read. Zhang–Gosea–Antoulas (2021), arXiv:2103.09674, supplies an accessible original-TeX primary treatment of the separate matrix Loewner factorization, with its actual reading extent recorded. Existing020 proofs and their human attributions are preserved.

