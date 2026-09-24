# Polynomial spectral weights in the actual sphere localization row

Complete independent derivation, 24 September 2026. Proof locators CLP0–CLP13.

## CLP0. Constructed prerequisites and precise scope

The support remains \(\tau\langle Z_1;\mathrm{no}\ Z_2\rangle\). Every scalar, polynomial, derivative, source vector and complex coordinate below belongs to the existing arithmetic coefficient receiver after the complete-history reconstruction. None is an operation on \(\tau\). The two branches retain their separate recovered counters. The winding contribution and both labelled endpoint pairs remain present.

Before this calculation, CURRENT_CC_WEIGHT_WORK.md, READ_FIRST_USER_CONSTRUCTION.md, the connected USER_ARGUMENT_RECONSTRUCTION.md and its full correction table, PC08–PC09, and the verbatim WU050–WU055 and WU061–WU063 passages were recalled or reread. The relevant source calculations are CW2–CW8, CSP3–CSP7, CDW2–CDW3 and CDW7–CDW9, and CP4–CP10. CW2 supplies the simultaneous complexes of the actual sheaf row; CDW8 proves their compatibility with the retained winding summand. The closed source and its inverse are the already proved SSI/ESI source theorem, not a newly assumed closure. CP supplies the polynomial resolution, with both its kernel and cokernel degrees. We rederive the needed fixed-parameter division, matrices and connecting maps below.

The human sources are Alain Connes and Caterina Consani, [*Schemes over \(\mathbb F_1\) and zeta functions*, §5, arXiv:0903.2024v3](https://arxiv.org/abs/0903.2024v3), with the later signed-chart comparison in [arXiv:2609.00299v1](https://arxiv.org/abs/2609.00299v1), and Pierre Deligne, [*La conjecture de Weil. II*, §3.6](https://www.numdam.org/item/PMIHES_1980__52__137_0/), as reconstructed with exact hypotheses in DC. Original-author TeX coverage is the previously recorded CC source reading; the Deligne witness is the recorded French transcription. This note is a local derivation on the constructed receiver, not a new claim to have read those entire original sources.

The row being tested is the actual one
\[
0\longrightarrow\mathscr F_J\longrightarrow\mathscr F
\longrightarrow j_!\underline Q\longrightarrow0.
\tag{CLP0.1}
\]
It is not the continuous-to-algebraic dual comparison cone of CP. Its full normal kernel is \(J(-1)\). No quotient of that kernel is substituted for it. Every spectral parameter used for the two principal cases is an actual nontrivial zero \(\rho\) of the original \(\zeta\), or its stated shift \(\rho+1\); no RH location is assumed.

## CLP1. Original source, complete transform and topology

Let
\[
S=\{f\in\mathcal S(\mathbb R;\mathbb C):f(-v)=f(v),\ f(0)=0,
\ \int_{\mathbb R}f(v)\,dv=0\},\qquad V_\pm=S\oplus E_\pm,
\quad E_\pm=\mathbb C^2,
\]
\[
A=\{b\in C^\infty(\mathbb R_{>0}):
\sup_{u>0}(u^N+u^{-N})|(u\partial_u)^jb(u)|<\infty
\text{ for every }N,j\ge0\}.
\tag{CLP1.1}
\]
The endpoint labels are value at zero and integral, in that order on each chart. Keep
\[
\Sigma f(u)=2\sum_{n\ge1}f(nu),\qquad Rb(u)=u^{-1}b(u^{-1}),
\qquad \widehat f(v)=\int_{\mathbb R}f(x)e^{-2\pi ixv}\,dx,
\]
\[
r_+(f,c_0,c_1)=\Sigma f,\qquad
r_-(h,d_0,d_1)=R\Sigma h=\Sigma\widehat h.
\tag{CLP1.2}
\]
The last identity retains the complete preceding Poisson formula
\[
\Sigma\widehat h(u)=u^{-1}\Sigma h(u^{-1})+u^{-1}h(0)
-\int_{\mathbb R}h.
\tag{CLP1.3}
\]
The two terms vanish on \(S\); the independent endpoint summands \(E_\pm\) are not deleted. The exact source theorem gives \(J=\Sigma S\) closed in \(A\), with a continuous inverse \(H=\Sigma^{-1}:J\to S\). Thus \(Q=A/J\) is the actual Fréchet quotient.

The half-Mellin comparison and its inverse are
\[
\Theta b(s)=\frac12\int_0^\infty b(u)u^s\frac{du}{u},\qquad
\Theta^{-1}F(u)=\frac{u^{-1/2}}\pi
\int_{\mathbb R}F(1/2+it)u^{-it}\,dt.
\tag{CLP1.4}
\]
They identify \(A\) with the entire strip-Schwartz space
\[
\mathcal B=\{F\text{ entire}:b_{M,N}(F)=
\sup_{|\Re s|\le M}(1+|\Im s|)^N|F(s)|<\infty
\text{ for all }M,N\ge0\}.
\]
The rapid endpoint seminorms and integration by parts in \(\log u\) prove absolute convergence and all differentiated convergence in (CLP1.4); Fourier inversion and contour shifts give the inverse. Let \(\mathscr Z\) be the actual nontrivial-zero divisor of the original \(\zeta\), with orders \(m_\rho\). Then the exact source theorem gives
\[
\Theta J=\mathcal I=\{F\in\mathcal B:F^{(j)}(\rho)=0
\ (\rho\in\mathscr Z,\ 0\le j<m_\rho)\},
\qquad \Theta Q=\mathcal Q=\mathcal B/\mathcal I.
\tag{CLP1.5}
\]
All subsequent equations in \(A,J,Q\) may be transported by these specified topological isomorphisms.

For \(\Re s>1\), absolute summation gives
\[
\Theta\Sigma f(s)=\zeta(s)\int_0^\infty f(v)v^s\frac{dv}{v},
\quad \mathcal M_0\Sigma f=2\Theta\Sigma f,
\]
\[
\zeta(s)=1+\sum_{n\ge2}n^{-s}=\prod_p(1-p^{-s})^{-1},
\qquad -\frac{\zeta'}{\zeta}(s)=\sum_p\sum_{k\ge1}(\log p)p^{-ks}.
\tag{CLP1.6}
\]
The unit and every prime-power repetition are retained. The fixed source
\[
f_0(v)=\frac\pi2v^2(2\pi v^2-3)e^{-\pi v^2}
\]
belongs to \(S\), and its complete transform is
\[
F_0(s)=\Theta\Sigma f_0(s)
=\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2)\zeta(s)
=C_0(s)\zeta(s).
\tag{CLP1.7}
\]
The two Gaussian Mellin integrals before the Gamma recurrence are
\[
\frac\pi2\left[
2\pi\cdot\frac12\pi^{-(s+4)/2}\Gamma((s+4)/2)
-3\cdot\frac12\pi^{-(s+2)/2}\Gamma((s+2)/2)\right],
\tag{CLP1.8}
\]
multiplied by the original \(\zeta(s)\). They yield exactly (CLP1.7). This entire function belongs to \(\mathcal I\), and its zero divisor is exactly \(\mathscr Z\), with full multiplicities. Its exceptional values are
\[
F_0(0)=F_0(1)=\frac18,
\]
\[
F_0(-2k)=\frac{k(2k+1)(-1)^k\pi^k}{2\,k!}\zeta'(-2k)
=\frac{(1+2k)(2k)}8\pi^{-(1+2k)/2}
\Gamma((1+2k)/2)\zeta(1+2k)\ne0\quad(k\ge1).
\tag{CLP1.9}
\]
The pole at one, Gamma poles and trivial-zero derivatives have thus been compared, not removed from the original function.

## CLP2. The actual simultaneous complexes and cover generator

Put \(Y=\mathbb P^1(\mathbb C)\), \(U=\mathbb C^\times\),
\(j:U\hookrightarrow Y\), \(i:\{0,\infty\}\hookrightarrow Y\), and \(W=V_+\oplus V_-\). The actual sheaf is
\[
\mathscr F=\underline A_Y\times_{i_*A^2}i_*W,
\tag{CLP2.1}
\]
with map \((b,v_+,v_-)\mapsto(b|_0-r_+v_+,b|_\infty-r_-v_-)\). Replacing the interior coefficient by \(J\) gives \(\mathscr F_J\); its quotient is \(j_!\underline Q\) because it has zero pole stalks and the interior quotient vanishes near each pole. This proves stalkwise exactness of (CLP0.1).

CW2's simultaneous contractions give the following degreewise exact row of global complexes:
\[
\begin{array}{c|ccc}
&D_J&D_F&D_G\\ \hline
0&W&W&0\\
1&J&A&Q\\
2&J(-1)&A(-1)&Q(-1).
\end{array}
\qquad d^0=d=r_+-r_-,\qquad d^1=0.
\tag{CLP2.2}
\]
The maps in degree zero are the identity and zero; the other two rows are inclusion and quotient. For specificity, before contraction each column is
\(B\oplus W\to B^2\to B\), with
\(d^0(b,v)=(b-r_+v_+,b-r_-v_-)\). The projection in degrees zero and one is
\((b,v)\mapsto v\), \((b_+,b_-)\mapsto b_--b_+\), and the section is
\(v\mapsto(r_-v_-,v)\), \(b\mapsto(-b,0)\). The homotopy on degree one is \((b_+,b_-)\mapsto(b_-,0)\). Substitution proves \(ps=1\), \(1-sp=dh+hd\). These formulas commute with \(J\to A\to Q\); hence (CLP2.2) represents the actual sheaf maps simultaneously.

For \(a>0\), the primal coefficient maps are
\[
T_a b(u)=b(u/a),\quad
\rho_+(a)(f,c_0,c_1)=(f(\cdot/a),c_0,ac_1),
\]
\[
\rho_-(a)(h,d_0,d_1)=(a h(a\cdot),ad_0,d_1).
\tag{CLP2.3}
\]
They form multiplicative groups and satisfy \(r_\pm\rho_\pm(a)=T_ar_\pm\), by summation and \(\widehat{a h(a\cdot)}=\widehat h(\cdot/a)\). For the actual integer sphere cover \(z\mapsto z^n\), \(n\ge1\), its action on (CLP2.2) is
\[
(\rho_+(n)\oplus\rho_-(n),\ T_n,\ nT_n).
\tag{CLP2.4}
\]
The last factor is the positive complex-oriented degree, equivalently the winding-period factor. CDW8 retains precisely this normal summand. The same formulas with \(a>0\) define an action on the coefficient complexes: the group law follows from (CLP2.3), the first differential intertwines the first two components, and the differential into the third is zero. No nonintegral sphere cover is asserted.

Differentiating the coefficient action at \(a=e^h\), \(h=0\), gives the continuous chain operator
\[
t^0=G=G_+\oplus G_-,\qquad t^1=L=-u\partial_u,
\qquad t^2=L+1,
\]
\[
G_+(f,c_0,c_1)=(-v\partial_vf,0,c_1),\quad
G_-(h,d_0,d_1)=(h+v\partial_vh,d_0,0).
\tag{CLP2.5}
\]
The derivative exists in every source seminorm by Taylor's integral remainder for dilations; two extra derivatives bound its second-order remainder uniformly on compact \(h\)-intervals. Under \(\Theta\), \(L\) is multiplication by \(s\). The symbol \((-1)\) in (CLP2.2) means the retained action \(aT_a\), so its generator is \(s+1\). These are the actual geometric generators on the finite coefficient models, not a degree-independent replacement.

## CLP3. Symmetric source section and exact decomposition

The two continuous source sections are
\[
s_+(b)=(Hb,0,0),\qquad s_-(b)=(\widehat{Hb},0,0),
\quad r_\pm s_\pm=1_J.
\]
Define
\[
\sigma:J\to W,\qquad
\sigma b=\frac12(s_+b,-s_-b),\qquad d\sigma=1_J,
\quad p_Z=1_W-\sigma d,
\tag{CLP3.1}
\]
and \(Z=\ker d\). The full inverse source theorem proves continuity. Intertwining of \(r_\pm\) and injectivity on the source summands give \(\rho(a)\sigma=\sigma T_a\), and hence \(G\sigma=\sigma L\). Thus
\[
W\xrightarrow{\sim}Z\oplus J,\quad
w\mapsto(p_Zw,dw),\qquad (z,b)\mapsto z+\sigma b
\tag{CLP3.2}
\]
is a continuous equivariant isomorphism. The endpoint summands lie entirely in \(Z\), and
\[
Z\simeq J\oplus E_+\oplus E_-,
\quad b,e_+,e_-\mapsto(s_+b+e_+,s_-b+e_-).
\tag{CLP3.3}
\]
The endpoint eigenvalues of \(G\) are \((0,1,1,0)\), in the original order.

Consequently the row (CLP2.2) has an actual decomposition into three rows of complexes: the identity row on \(Z[0]\); the row
\[
0\to[J\xrightarrow{1}J]\to[J\xrightarrow{\iota}A]
\to Q[-1]\to0
\tag{CLP3.4}
\]
in degrees zero and one; and the actual normal row
\[
0\to J(-1)[-2]\to A(-1)[-2]\to Q(-1)[-2]\to0.
\tag{CLP3.5}
\]
These follow by substituting (CLP3.2), not by splitting \(A\to Q\). The differential in the left complex of (CLP3.4) is the identity, so that complex is contracted by the identity from degree one to degree zero. The quotient map \([J\to A]\to Q[-1]\) is a quasi-isomorphism, but no equivariant section \(Q\to A\) has been selected.

## CLP4. The full two-term spectral functor

Work over \(R=\mathbb C[t]\), with the degreewise chain operator (CLP2.5), and put
\[
P(t)=(t-\lambda)^r,\qquad r\ge1.
\]
The resolution \(0\to R\xrightarrow{P}R\to R/(P)\to0\), with free terms in degrees minus one and zero, gives
\[
K_P(C)^k=C^k\oplus C^{k-1},\qquad
\delta(x,y)=(dx,Px-dy),\qquad
K_P(C)\simeq\operatorname{RHom}_R(R/(P),C).
\tag{CLP4.1}
\]
To check the sign, write the usual Hom differential as \(d_Cf-(-1)^kf d_R\) and change its second coordinate \(b\) to \(y=(-1)^kb\). Direct calculation gives \(\delta^2=0\) because \(P\) commutes with \(d\).

For any complex the complete cohomology formula is
\[
0\to H^{k-1}(C)/PH^{k-1}(C)
\xrightarrow{[y]\mapsto[(0,y)]}H^kK_P(C)
\xrightarrow{[(x,y)]\mapsto[x]}H^k(C)[P]\to0.
\tag{CLP4.2}
\]
Indeed a cycle satisfies \(dx=0\), \(Px=dy\); a class killed by \(P\) admits such a \(y\). If \(x=du\), subtraction of \(\delta(u,0)\) leaves \((0,y-Pu)\); its ambiguities are exactly ordinary boundaries and \(P\) times closed elements. This proves exactness including the cokernel term.

For \(C=D_J,D_F\), the terms of \(K_P(C)\) in degrees zero through three are
\[
W,\quad B\oplus W,\quad B(-1)\oplus B,\quad B(-1),
\quad B=J\text{ or }A,
\]
\[
w\mapsto(dw,P(G)w),\quad
(b,w)\mapsto(0,P(L)b-dw),\quad
(c,b)\mapsto P(L+1)c.
\tag{CLP4.3}
\]
For \(D_G\), they are \(0,Q,Q(-1)\oplus Q,Q(-1)\), with maps
\[
q\mapsto(0,P(L)q),\qquad(c,q)\mapsto P(L+1)c.
\tag{CLP4.4}
\]
These complexes form a degreewise exact row. Its connecting map is calculated by lifting a cycle to the middle complex and applying the displayed differential, with a positive inclusion into the first complex. All degrees and signs below use this convention.

## CLP5. Fixed-parameter division, jets, endpoints and source matrices

For \(\nu\in\mathbb C\), write \(z=s-\nu\), \(m_\nu=\operatorname{ord}_\nu F_0\), and \(d_\nu=\min(r,m_\nu)\); set \(m_\nu=0\) off the actual zero divisor. Multiplication by \(z^r\) is injective on \(\mathcal B\) and \(\mathcal I\), since they consist of entire functions. The exact continuous jet identifications are
\[
\mathcal B/z^r\mathcal B\xrightarrow{\sim}\mathbb C[z]/(z^r),
\quad F\mapsto\sum_{j<r}\frac{F^{(j)}(\nu)}{j!}z^j,
\]
\[
\mathcal I/z^r\mathcal I\xrightarrow{\sim}\mathbb C[z]/(z^r),
\quad F\mapsto\sum_{j<r}\frac1{j!}
\left(\frac F{F_0}\right)^{(j)}(\nu)z^j.
\tag{CLP5.1}
\]
The quotient \(F/F_0\) is entire for \(F\in\mathcal I\); its value at a zero is interpreted by full analytic division. The kernels are exactly the displayed polynomial images. Division by \(s-\nu\) on the closed value-zero subspace is continuous: outside a fixed disk the denominator is bounded away from zero; inside it, the integral formula \(H(s)/(s-\nu)=\int_0^1H'(\nu+t(s-\nu))dt\) and a Cauchy estimate on a larger fixed disk bound every strip seminorm. Iteration proves the order-\(r\) statement. Evaluation of \(F/F_0\)'s jets is also continuous by division by the nonzero local unit after its fixed order of vanishing. Finite Taylor interpolation with \(e^{(s-\nu)^2}\) times a polynomial proves the first surjectivity; \(F_0\) times a polynomial proves the second. All image subspaces in (CLP5.1) are therefore closed.

In these exact coordinates the inclusion \(\mathcal I\to\mathcal B\) induces
\[
\mathsf T_r(\nu)_{ij}=
\begin{cases}F_0^{(i-j)}(\nu)/(i-j)!,&i\ge j,\\0,&i<j,
\end{cases}\qquad 0\le i,j<r.
\tag{CLP5.2}
\]
It is multiplication by the full Taylor series of \(F_0\) modulo \(z^r\). Write \(F_0(\nu+z)=z^{m_\nu}b_\nu(z)\), with \(b_\nu(0)\ne0\). The local unit is invertible modulo \(z^r\), so the matrix has kernel and cokernel dimensions \(d_\nu\), rank \(r-d_\nu\), and determinant \(F_0(\nu)^r\). No derivative of its unit has been dropped.

For the full quotient, not an assumed infinite direct sum of blocks,
\[
\dim\ker(L-\nu)^r|_Q=\dim Q/(L-\nu)^rQ=d_\nu.
\tag{CLP5.3}
\]
Here is a proof retaining its topology. If \(m_\nu=0\),
\[
[F]\longmapsto\left[
\frac{F(s)-F_0(s)F(\nu)/F_0(\nu)}{s-\nu}\right]
\tag{CLP5.4}
\]
is a continuous inverse of \(L-\nu\) on \(\mathcal Q\), by the preceding division estimate; multiplication in either order gives the identity modulo \(\mathcal I\). If \(m=m_\nu>0\), put
\[
B_\nu=F_0/(s-\nu)^m,\qquad
\Pi_\nu F=B_\nu\sum_{j<m}\frac{(F/B_\nu)^{(j)}(\nu)}{j!}(s-\nu)^j.
\tag{CLP5.5}
\]
The ratio is used only near \(\nu\), where \(B_\nu\ne0\). This is a continuous finite operator. Its output has the input's full jet at \(\nu\) and vanishes to the full original order at every other zero. It induces a projection \(\overline\Pi_\nu\) on \(\mathcal Q\), commuting with \(L\), whose image is the genuine \(m\)-dimensional zero block. On the closed complement \(Q_0\), an inverse of \(L-\nu\) is
\[
[F]\mapsto(1-\overline\Pi_\nu)[F/(s-\nu)].
\tag{CLP5.6}
\]
Every representative has its full \(m\)-jet zero; changing it by \(\mathcal I\) changes the quotient only in the projected zero block. Division and finite interpolation give continuity with the quotient topology. On the finite image, \(L-\nu\) is multiplication by \(z\) modulo \(z^m\). Its \(r\)-th power has kernel and cokernel dimensions \(d_\nu\), proving (CLP5.3). In particular all polynomial images used here are closed.

The finite kernel has the especially useful actual basis
\[
q_{\nu,j}=\left[\frac{F_0(s)}{(s-\nu)^j}\right],
\qquad1\le j\le d_\nu,
\tag{CLP5.7}
\]
and the quotient \(Q/(L-\nu)^rQ\) is the ordinary Taylor jet modulo \(z^{d_\nu}\). Independence of (CLP5.7) follows from its distinct orders \(m-j\); these vectors span by (CLP5.3).

Finally put \(E_\lambda\) equal to the sum of the endpoint lines with eigenvalue \(\lambda\). It is zero except at \(\lambda=0,1\), where it has dimension two. Then
\[
Z[P]=E_\lambda,\qquad
Z/PZ\simeq J/(L-\lambda)^rJ\oplus E_\lambda,
\qquad\dim Z/PZ=r+\dim E_\lambda.
\tag{CLP5.8}
\]
A repeated root of \(P\) does not increase the dimension of a scalar endpoint line. Both endpoint lines of eigenvalue zero and both of eigenvalue one remain in this formula.

## CLP6. Every spectral cohomology group and every connecting map

Write \(Q_0[P]=\ker P(L)|_Q\), \(Q_0/P=Q/P(L)Q\),
\(Q_1[P]=\ker P(L+1)|_{Q(-1)}\), and \(Q_1/P=Q(-1)/P(L+1)Q(-1)\). The subscripts in this paragraph record the stated scalar shift, not a new quotient of \(\tau\). Direct substitution in (CLP4.3)–(CLP4.4) gives the complete table:
\[
\begin{array}{c|ccc}
k&H^kK_P(D_J)&H^kK_P(D_F)&H^kK_P(D_G)\\ \hline
0&E_\lambda&E_\lambda&0\\
1&Z/PZ&Z/PZ\oplus Q_0[P]&Q_0[P]\\
2&0&Q_0/P&Q_0/P\oplus Q_1[P]\\
3&J(-1)/P(L+1)J&A(-1)/P(L+1)A&Q_1/P.
\end{array}
\tag{CLP6.1}
\]
Every other degree is zero. These are specified maps and splittings, proved next, rather than a dimension-only assertion.

In degree zero, a cycle is exactly \(w\in Z\) killed by \(P(G)\), so (CLP5.8) applies. In degree one a middle cycle \((b,w)\) satisfies \(P(L)b=dw\). The map and inverse giving the displayed direct sum are
\[
[(b,w)]\mapsto([w-\sigma P(L)b],[b]),
\]
\[
([z],q)\mapsto[(b,z+\sigma P(L)b)],\qquad [b]=q.
\tag{CLP6.2}
\]
The first component belongs to \(Z\); the second is killed by \(P\). Changing \(z\) by \(Pz_0\) changes the cycle by \(\delta(z_0)\). Changing the lift \(b\) by \(j\in J\) changes it by
\(\delta(\sigma j)=(j,\sigma P(L)j)\). Thus (CLP6.2) is well-defined, and the two maps are inverse. The left complex has no \(Q\) term: subtraction of \(\delta(\sigma b)\) reduces its cycles to \((0,z)\). This proves the first two columns in degree one.

In degree two of either entire-function column, a cycle \((c,b)\) has \(P(L+1)c=0\), so \(c=0\). Its boundaries have second component \(P(L)b_0-dw\). Hence its cohomology is zero for \(B=J\), and \(A/(P(L)A+J)=Q_0/P\) for \(B=A\). In the quotient column, a cycle is \((c,q)\) with \(c\in Q_1[P]\) and arbitrary \(q\); the only boundaries are \((0,P(L)q_0)\). We use the order \(([q],c)\) in (CLP6.1). Degree three is directly the corresponding cokernel of \(P(L+1)\). This proves all entries without omitting either derived degree.

In degree zero the inclusion is the identity. In degree one the two maps are
\[
Z/PZ\longrightarrow Z/PZ\oplus Q_0[P]\longrightarrow Q_0[P],
\qquad z\mapsto(z,0),\quad(z,q)\mapsto q.
\tag{CLP6.3}
\]
In degree two the map out of \(D_F\) is
\[
Q_0/P\longrightarrow Q_0/P\oplus Q_1[P],\qquad y\mapsto(y,0).
\tag{CLP6.4}
\]
The connecting maps in degrees zero, one and three vanish. Degree zero has zero source; degree one has zero target by the calculation above; degree three has zero target beyond the complex. A direct degree-one correction is useful: an initial lift \((b,0)\) of \(q\in Q_0[P]\) has boundary \((0,P(L)b)\) in degree two of \(K_P(D_J)\), and
\[
(0,P(L)b)=\delta(0,-\sigma P(L)b).
\tag{CLP6.5}
\]
Subtracting that primitive produces the plus sign in the corrected cycle \((b,\sigma P(L)b)\). Its class is independent of the chosen representative but is not a selected entire representative of \(q\).

The sole potentially nonzero connecting map is
\[
\boxed{\beta^2_P:Q_0/P\oplus Q_1[P]
\longrightarrow J(-1)/P(L+1)J,
\qquad ([y],q)\longmapsto[P(L+1)b],\quad[b]=q.}
\tag{CLP6.6}
\]
To prove its sign and formula, lift the quotient cycle \((q,y)\) to \((b,a)\in A(-1)\oplus A\). Its differential is \((0,P(L+1)b)\), independent of \(a\), and this is the included left cycle. Changing \(b\) by \(j\in J\) changes the answer by \(P(L+1)j\). Thus it is well-defined. It vanishes on the full \(Q_0/P\) summand, and is injective on \(Q_1[P]\): if \(P(L+1)b=P(L+1)j\), injectivity on entire functions gives \(b=j\), hence \(q=0\).

The last exact row is therefore
\[
0\to Q_1[P]\xrightarrow{\beta^2_P}
J(-1)/P(L+1)J\xrightarrow{\overline\iota}
A(-1)/P(L+1)A\xrightarrow{\overline q}Q_1/P\to0.
\tag{CLP6.7}
\]
Indeed the kernel of \(\overline\iota\) consists exactly of classes \([P(L+1)b]\) with \([b]\in Q_1[P]\), and the cokernel is the quotient \(Q_1/P\). This is the genuine normal row, with its entire original kernel retained.

For \(\mu=\lambda-1\), identify the two middle terms in (CLP6.7) by (CLP5.1). Then \(\overline\iota\) is exactly \(\mathsf T_r(\mu)\), \(\overline q\) is reduction of the ordinary jet to degree below \(d_\mu\), and
\[
\beta^2_P(q_{\mu,j})=[F_0(s)(s-\mu)^{r-j}],
\qquad1\le j\le d_\mu.
\tag{CLP6.8}
\]
In the \(F/F_0\)-jet coordinate its value is \(z^{r-j}\). These monomials span the full kernel of \(\mathsf T_r(\mu)\), proving exactness and the rank \(d_\mu\) explicitly.

All finite identifications and maps are continuous. For the only apparently chosen lift in (CLP6.2), restrict \(b\) to the finite actual block given by (CLP5.5), whose representatives are explicit continuous functions of its finite coordinates. Independence of arbitrary representatives was already proved. The cokernel identifications use closed finite-jet kernels and continuous division. No topological direct-sum assumption about all zeros is needed.

## CLP7. The original-zero parameter: the precise separated normal lift

Take an actual nontrivial zero \(\rho\), multiplicity \(m\), put \(\lambda=\rho\), and let \(d=\min(r,m)\). The known open strip \(0<\Re\rho<1\) gives \(m_{\rho-1}=0\), and \(\rho\notin\{0,1\}\). The complete dimensions in degrees zero through three are
\[
\begin{array}{c|rrrr}
&0&1&2&3\\ \hline
K_P(D_J)&0&r&0&r\\
K_P(D_F)&0&r+d&d&r\\
K_P(D_G)&0&d&d&0.
\end{array}
\tag{CLP7.1}
\]
Every connecting map vanishes. The degree-one map is the split surjection (CLP6.3), with its full \(r\)-dimensional kernel \(J/(L-\rho)^rJ\). Degree two is the identity on \(Q/(L-\rho)^rQ\). Degree three is the isomorphism
\[
J(-1)/(L+1-\rho)^rJ\xrightarrow{\sim}
A(-1)/(L+1-\rho)^rA,
\tag{CLP7.2}
\]
whose exact matrix is \(\mathsf T_r(\rho-1)\), including all original factors.

Here is its inverse, with no discarded multiplier. Put \(\mu=\rho-1\) and
\[
H_0(s)=\frac1{F_0(s)}
=\frac{8\pi^{s/2}}{s(s-1)\Gamma(s/2)\zeta(s)}
\quad\text{near }\mu.
\tag{CLP7.3}
\]
It is holomorphic there because \(F_0(\mu)\ne0\). The inverse matrix is lower triangular, with entry
\[
\bigl(\mathsf T_r(\mu)^{-1}\bigr)_{ij}
=\frac{H_0^{(i-j)}(\mu)}{(i-j)!}\quad(i\ge j).
\tag{CLP7.4}
\]
Multiplying the two truncated series gives the jet of \(F_0H_0=1\), proving both inverse identities. Explicitly a normal cokernel class \([F]\) lifts to
\[
\left[F_0(s)\sum_{j<r}\frac{(F/F_0)^{(j)}(\mu)}{j!}(s-\mu)^j\right]
\in\mathcal I/(s-\mu)^r\mathcal I.
\tag{CLP7.5}
\]
Only the germ of \(F/F_0\) at \(\mu\) is used; the output is \(F_0\) times a polynomial, hence lies in the actual source. This class is the unique inverse image under (CLP7.2), not a canonical global representative in \(A\to Q\).

The full derivative in (CLP7.4) is, for \(k\ge0\),
\[
\frac{H_0^{(k)}(\mu)}{k!}
=8\sum_{k_1+\cdots+k_5=k}
\frac{(s^{-1})^{(k_1)}(\mu)}{k_1!}
\frac{((s-1)^{-1})^{(k_2)}(\mu)}{k_2!}
\frac{(\pi^{s/2})^{(k_3)}(\mu)}{k_3!}
\frac{(\Gamma(s/2)^{-1})^{(k_4)}(\mu)}{k_4!}
\frac{(\zeta(s)^{-1})^{(k_5)}(\mu)}{k_5!}.
\tag{CLP7.6}
\]
Thus both endpoint factors, every Gamma and original-zeta reciprocal derivative, the power of \(\pi\), and the scalar eight remain. The reciprocal Gamma derivative is of the displayed composite \(s\mapsto\Gamma(s/2)^{-1}\), so its chain-rule factors are included rather than changed to derivatives in a different coordinate.

At this parameter the actual normal quotient has neither a polynomial kernel nor a polynomial cokernel. Equivalently
\[
K_{(t-\rho)^r}(Q(-1))\simeq0,
\qquad K_{(t-\rho)^r}(J(-1))
\xrightarrow{\sim}K_{(t-\rho)^r}(A(-1)).
\tag{CLP7.7}
\]
This is a genuine spectral separation on the actual normal row, proved globally by (CLP5.4), and its nonzero cokernel inverse is (CLP7.5). It retains all of \(J(-1)\); it does not assert that this full source has only high-weight quotients.

For an explicit degree-one lift, take \(q_{\rho,j}\) from (CLP5.7), let
\[
a_j=\Theta^{-1}(F_0/(s-\rho)^j),\qquad
g_j=(-v\partial_v-\rho)^{r-j}f_0.
\]
Then \(P(L)a_j=\Sigma g_j\), so its spectral lift is
\[
\left[\left(a_j,\frac12((g_j,0,0),(-\widehat g_j,0,0))\right)\right]
\in H^1K_P(D_F),\quad1\le j\le d.
\tag{CLP7.8}
\]
The inverse Mellin integral is (CLP1.4), including its \(u^{-1/2}/\pi\) factor; its integrand is entire even if \(\rho\) lies on the integration line, because the zero has order at least \(j\). The source derivative preserves \(S\), by evenness, the value condition and integration by parts for the integral. Thus every term of this representative belongs to the original source.

## CLP8. The shifted actual-zero parameter: a nonzero higher boundary

Now take \(\lambda=\rho+1\), with the same actual \(\rho,m,r,d\). The original quotient has no character at \(\lambda\), while the genuine normal quotient has its original-zero block there. Thus
\[
\begin{array}{c|rrrr}
&0&1&2&3\\ \hline
K_P(D_J)&0&r&0&r\\
K_P(D_F)&0&r&0&r\\
K_P(D_G)&0&0&d&d.
\end{array}
\tag{CLP8.1}
\]
The degree-one map is an isomorphism. The entire nontrivial tail is
\[
0\to Q(-1)[(t-\rho-1)^r]
\xrightarrow{\beta^2_P}J(-1)/(L-\rho)^rJ
\xrightarrow{\mathsf T_r(\rho)}A(-1)/(L-\rho)^rA
\to Q(-1)/(L-\rho)^rQ\to0.
\tag{CLP8.2}
\]
The injective boundary has rank \(d\), and its exact basis values are
\[
\boxed{\beta^2_P(q_{\rho,j})=[F_0(s)(s-\rho)^{r-j}],
\qquad1\le j\le d.}
\tag{CLP8.3}
\]
No value on the critical line has been distinguished in this calculation. The image is nonzero at every actual zero, with every multiplicity retained. If \(r\le m\), its rank is \(r\) and the middle matrix is zero modulo \((s-\rho)^r\). If \(r>m\), its rank is \(m\) and the middle matrix has rank \(r-m\). Both cases follow from the full unit calculation (CLP5.2).

The representative producing (CLP8.3) is especially direct: in degree two of \(K_P(D_G)\) use \((q_{\rho,j},0)\); lift it to \((a_j,0)\) with \(a_j\) from (CLP7.8). Its differential in degree three is
\[
P(L+1)a_j=(L-\rho)^ra_j
=\Sigma(-v\partial_v-\rho)^{r-j}f_0.
\tag{CLP8.4}
\]
This is an actual element of \(J(-1)\), followed by its indicated cokernel class. Formula (CLP1.7) supplies its full Mellin multiplier, including \(1/8\), rather than a bare divisor label.

The original geometric \(\delta^2:H^2(D_G)\to H^3(D_J)\) still has zero target. The spectral boundary (CLP8.3) instead lands in the additional derived degree
\(H^3K_P(D_J)=\operatorname{coker}P|_{J(-1)}\). Taking the two-term spectral functor has retained the Ext degree of the actual normal extension. This specifies exactly why the two boundaries differ; no failure of the earlier geometric degree-one lift is inferred.

## CLP9. Full finite action matrices and all weights actually obtained

For the ordinary quotient kernel basis (CLP5.7), the full action is
\[
T_aq_{\nu,j}=a^\nu\sum_{k=0}^{j-1}
\frac{(\log a)^k}{k!}q_{\nu,j-k},\qquad a>0.
\tag{CLP9.1}
\]
Indeed multiply its representative by \(a^s=a^\nu e^{(s-\nu)\log a}\). The terms of order at least \(j\) have the full factor \(F_0\) and lie in \(\mathcal I\); all terms of lower order are displayed. On the normal block multiply the entire matrix by the retained factor \(a\).

In the normal boundary case (CLP8.3), put \(b_j=[F_0(s)(s-\rho)^{r-j}]\). Then both source and image have exactly
\[
q_{\rho,j}\longmapsto a^{\rho+1}
\sum_{k=0}^{j-1}\frac{(\log a)^k}{k!}q_{\rho,j-k},
\qquad
b_j\longmapsto a^{\rho+1}
\sum_{k=0}^{j-1}\frac{(\log a)^k}{k!}b_{j-k}.
\tag{CLP9.2}
\]
Thus the positive boundary commutes with every term, including all nilpotents. At the actual integer cover these scalars are \(n^{\rho+1}\), not \(n^\rho\). Positive-real formulas describe the specified coefficient extension only.

For the full \(r\)-dimensional ordinary source cokernel at \(\nu\), use the coordinate \(p(z)=(F/F_0)(\nu+z)\bmod z^r\); its action is multiplication by
\[
a^\nu\sum_{k=0}^{r-1}\frac{(\log a)^k}{k!}z^k.
\tag{CLP9.3}
\]
The ordinary target cokernel uses the jet of \(F\) and has the same multiplication. The matrix \(\mathsf T_r(\nu)\) commutes with it because both are multiplication by the displayed truncated series. On a normal cokernel centered at \(\mu=\lambda-1\), (CLP9.3) has scalar \(a^{\mu+1}=a^\lambda\). In particular the nonzero normal cokernels in (CLP7.2) have the same scalar \(a^\rho\) as the original-zero classes; their isomorphism does not create a new common modulus.

The degree-one lift (CLP6.2) is equivariant, since \(\sigma\), \(P\), and the quotient maps intertwine the action. Its kernel \(J/(L-\lambda)^rJ\) has the scalar \(a^\lambda\) in (CLP9.3), and its \(Q_0[P]\) summand has the same scalar when nonzero. This is an explicit split lift with overlapping source and kernel characters, not a lift whose entire kernel has a separated weight interval.

For \(a>1\), define the logarithmic-modulus weight of a nonzero scalar by
\[
w_a(\alpha)=\frac{2\log|\alpha|}{\log a}.
\tag{CLP9.4}
\]
For actual zeros \(\rho\), the ordinary blocks have \(0<2\Re\rho<2\), while the normal zero blocks have \(2<2\Re\rho+2<4\). This separation is exactly the one used in (CLP7.7), with the stronger operator inverse (CLP5.4). In (CLP8.3), the source and image both have weight \(2\Re\rho+2\); hence their nonzero map is fully compatible with their equal weights. The entire \(J(-1)\) has quotient jets at every center \(\mu\), with scalar \(a^{\mu+1}\), as (CLP5.1) and (CLP9.3) prove. It has no bound restricting all such quotients to the normal-zero interval. None of these assertions installs an arithmetic purity premise or proves \(\Re\rho=1/2\).

For completeness, every entry of \(\mathsf T_r(\nu)\) at a regular point retains the full product derivative
\[
\frac{F_0^{(k)}(\nu)}{k!}
=\frac18\sum_{k_1+\cdots+k_5=k}
\frac{s^{(k_1)}(\nu)}{k_1!}
\frac{(s-1)^{(k_2)}(\nu)}{k_2!}
\frac{(\pi^{-s/2})^{(k_3)}(\nu)}{k_3!}
\frac{(\Gamma(s/2))^{(k_4)}(\nu)}{k_4!}
\frac{\zeta^{(k_5)}(\nu)}{k_5!}.
\tag{CLP9.5}
\]
At an actual zero, writing \(\zeta(\rho+z)=z^m u_\rho(z)\) gives
\(b_\rho(z)=C_0(\rho+z)u_\rho(z)\); all derivatives of this unit remain in (CLP5.2). The completion factor has never replaced the original \(\zeta\).

## CLP10. Exceptional locations, endpoints and exact mirror transport

The general table (CLP6.1) also covers every \(\lambda\in\mathbb C\). Its dimensions are
\[
\begin{array}{c|ccc}
k&D_J&D_F&D_G\\ \hline
0&e_\lambda&e_\lambda&0\\
1&r+e_\lambda&r+e_\lambda+d_\lambda&d_\lambda\\
2&0&d_\lambda&d_\lambda+d_{\lambda-1}\\
3&r&r&d_{\lambda-1},
\end{array}
\quad e_\lambda=\begin{cases}2,&\lambda=0\text{ or }1,\\0,&\text{otherwise}.\end{cases}
\tag{CLP10.1}
\]
At \(\lambda=0,1\), both \(d_\lambda\) and \(d_{\lambda-1}\) vanish, since \(F_0(0)=F_0(1)=1/8\) and \(-1\) is not in the nontrivial divisor. The normal diagonals are exactly \(F_0(-1)=\pi/24\) at \(\lambda=0\), and \(F_0(0)=1/8\) at \(\lambda=1\). The first value follows directly from \(\Gamma(-1/2)=-2\sqrt\pi\), \(\zeta(-1)=-1/12\), and (CLP1.7), or from \(F_0(-1)=F_0(2)\). The two endpoint lines contribute two dimensions to both \(Z[P]\) and \(Z/PZ\), with actions respectively \(1\) or \(a\); they are never assigned multiplicity \(r\). At every cancellation point \(-2k\), or its normal translate \(1-2k\), the relevant full source value is (CLP1.9), not zero. This proves that no endpoint or cancelled trivial zero produces an extra \(Q\)-block.

Higher exceptional derivatives are also retained by analytic product coefficients. If \(\nu=-2k\), write the actual Laurent series
\(C_0(\nu+z)=c_{-1}/z+\sum_{j\ge0}c_jz^j\), and
\(\zeta(\nu+z)=\sum_{j\ge1}\zeta^{(j)}(\nu)z^j/j!\). Then
\[
\frac{F_0^{(l)}(\nu)}{l!}
=c_{-1}\frac{\zeta^{(l+1)}(\nu)}{(l+1)!}
+\sum_{j=0}^{l-1}c_j\frac{\zeta^{(l-j)}(\nu)}{(l-j)!}.
\tag{CLP10.2}
\]
At one, use \(C_0(1+z)=\sum_{j\ge1}a_jz^j\) and
\(\zeta(1+z)=z^{-1}+\sum_{j\ge0}\gamma_jz^j\), giving
\[
\frac{F_0^{(l)}(1)}{l!}=a_{l+1}+\sum_{j=1}^{l}a_j\gamma_{l-j}.
\tag{CLP10.3}
\]
At zero the factor \(s\Gamma(s/2)\) has its removable analytic value two, while all other factors are holomorphic; its Taylor series in the unchanged coordinate supplies (CLP9.5) after that explicitly stated analytic extension. These formulas keep every pole-cancellation derivative in the source matrices and their inverse matrices wherever invertible.

The two actual sphere swaps act in global degrees zero, one and two by
\[
M^0(v_+,v_-)=(v_-,v_+),\qquad M^1=-R,
\qquad M^2=\epsilon R,
\quad\epsilon=+1\text{ holomorphic},\ -1\text{ antiholomorphic}.
\tag{CLP10.4}
\]
The exchanged endpoint labels remain attached to their chart coordinates. Since \(H R=\widehat H\) on \(J\), direct substitution gives
\[
M^0\sigma b=\sigma(-Rb),\qquad
p_ZM^0=M^0p_Z.
\tag{CLP10.5}
\]
Thus the exact decomposition (CLP3.4)–(CLP3.5) respects both mirrors, with common-restriction action \(R\) on the \(J\) coordinate of \(Z\), and the separate signs just displayed. The operator identity \(LR=R(1-L)\) shows that the linked degrees zero and one reflect \(t\) to \(1-t\), whereas the normal degree two generator \(L+1\) reflects \(t\) to \(3-t\).

Consequently a single global polynomial \((t-\lambda)^r\) does not transform into one common \((t-(1-\lambda))^r\) in all three degrees. The exact target uses
\[
P_{\rm low}(t)=(t-(1-\lambda))^r
\text{ on degrees }0,1,\qquad
P_{\rm normal}(t)=(t-(3-\lambda))^r
\text{ on degree }2.
\tag{CLP10.6}
\]
These still define a chain polynomial operator, since the only linked differential is between degrees zero and one. Equivalently use the proved direct decomposition and the two specified polynomials on its summands. The exact spectral chain map is
\[
(x,y)\longmapsto(M^kx,(-1)^rM^{k-1}y)
\quad\text{in degree }k.
\tag{CLP10.7}
\]
Indeed \(MP=(-1)^rP_{\rm target}M\) on each relevant coefficient, and substitution into (CLP4.1) gives the chain identity. The factor \((-1)^r\) is the monic-polynomial factor on the second spectral coordinate; it is separate from the geometric signs \(-R,\epsilon R\). Applied to the degree-two boundary it gives exactly
\(\epsilon R\) on its first-coordinate source and \((-1)^r\epsilon R\) on its degree-three second-coordinate image, consistent with (CLP6.6). The ordinary parameter \(\rho\) is sent to \(1-\rho\) in the low sector; the normal parameter \(\rho+1\) is sent to \(2-\rho=(1-\rho)+1\). All multiplicities and orientation signs are preserved.

## CLP11. The lifting result and its exact weight scope

The ordinary geometric map \(H^1(D_F)\to H^1(D_G)\) is the identity of \(Q\); its connecting map into \(J(-1)\) is zero. The present calculation constructs its entire derived polynomial version. For \(P=(t-\rho)^r\), the degree-one spectral map is a split surjection with explicitly computed kernel \(J/(L-\rho)^rJ\), and the lift is (CLP6.2) or the actual source formula (CLP7.8). Its cohomology class is independent of representatives after the stated symmetric source section is fixed. Its full set of lifts differs by the displayed kernel. No unique cochain representative is asserted.

The separated original and normal zero ranges prove the actual normal comparison (CLP7.7), with the complete inverse (CLP7.3)–(CLP7.6). This is a source-level spectral lift through the real row \(J(-1)\to A(-1)\to Q(-1)\), with its kernel preserved. It is not a declaration that all quotient characters of \(J(-1)\) are separated: the explicit finite cokernels (CLP5.1) prove otherwise and calculate their receiving maps.

The nonzero higher boundary at \(\lambda=\rho+1\) is exactly (CLP8.3), with its original-source representative (CLP8.4) and complete cover matrix (CLP9.2). It obstructs lifting that particular normal polynomial-kernel class in \(H^2K_P(D_G)\) through the spectral map \(H^2K_P(D_F)\). It does not obstruct the ordinary degree-one cohomology lift or the existence of individual representatives in the ordinary quotient. Its nonzero value occurs at every actual zero, including any on the critical line, so it is not an RH-violation criterion.

Deligne's DC5–DC7 mechanism kills a specified geometric connecting image by upper and lower bounds on the actual source and obstruction receiver, retaining his inertia coinvariant and normal duality terms. Here every corresponding arrow has been calculated on (CLP0.1). The low spectral lift, the separated normal comparison, and the nonzero shifted higher boundary are distinct proved maps in that one row. Their precise relation is the full exact sequence (CLP6.7), not an assumed identification with Deligne's inertia cross. The calculation preserves the original arithmetic and all original zeros. It establishes no new bound on \(\Re\rho\), and it does not mark the broader requested common-weight conclusion as proved.

## CLP12. The global derived connecting class before any finite spectral test

The decomposition in CLP3 gives a simultaneous chain-level comparison of the actual row, not only its fixed-parameter cohomology. Define complexes
\[
\widetilde D_J=Z[0]\oplus J(-1)[-2],\qquad
\widetilde D_F=Z[0]\oplus Q[-1]\oplus A(-1)[-2],
\]
\[
\widetilde D_G=Q[-1]\oplus Q(-1)[-2],
\tag{CLP12.1}
\]
all with zero differentials. Their short exact row has the identity on \(Z\) in degree zero, the identity on \(Q\) in degree one, and the actual normal inclusion and quotient in degree two. The maps from (CLP2.2) are
\[
\begin{array}{c|ccc}
&D_J\to\widetilde D_J&D_F\to\widetilde D_F&D_G\to\widetilde D_G\\ \hline
0&p_Z&p_Z&0\\
1&0&q&1_Q\\
2&1_J&1_A&1_Q.
\end{array}
\tag{CLP12.2}
\]
Each is a chain map: \(p_Z\) has target in degree zero and \(q d=0\). The horizontal squares commute in every degree. The kernels of the first two vertical maps are respectively \([\sigma J\xrightarrow{d}J]\) and \([\sigma J\xrightarrow{d}J]\), where \(d\sigma=1\); the third vertical map is the identity. The first two kernels are therefore explicitly contracted by \(\sigma\). This proves that all three vertical maps are continuous equivariant quasi-isomorphisms. It does not provide an equivariant section of \(A\to Q\).

In the derived category of the specified \(R=\mathbb C[t]\)-modules, the actual localization triangle is consequently the direct sum of the split identity triangle on \(Z[0]\), the split identity triangle on \(Q[-1]\), and the triangle of the actual extension
\[
\mathfrak e:\quad0\to J(-1)\xrightarrow\iota A(-1)
\xrightarrow q Q(-1)\to0.
\tag{CLP12.3}
\]
Write its extension class as
\[
e\in\operatorname{Ext}^1_R(Q(-1),J(-1)),\qquad
e:Q(-1)\longrightarrow J(-1)[1].
\tag{CLP12.4}
\]
The complete derived connecting morphism is zero on \(Q[-1]\) and is
\[
e[-2]:Q(-1)[-2]\longrightarrow J(-1)[-1]
\subset\widetilde D_J[1]
\tag{CLP12.5}
\]
on the normal summand. This is a global statement about the whole original modules, established by the simultaneous quasi-isomorphisms (CLP12.2). It uses no density assertion for finite spectral blocks.

The class \(e\) is nonzero. For any actual zero \(\rho\), the entire representative \(F_0/(s-\rho)\) has order \(m_\rho-1\) there, so its quotient class is nonzero. In the normal module it satisfies
\[
(t-(\rho+1))[F_0/(s-\rho)]=[F_0]=0.
\tag{CLP12.6}
\]
An \(R\)-linear section of (CLP12.3) would send that class to an entire function \(F\) with \((s-\rho)F=0\), forcing \(F=0\), which cannot map back to the nonzero class. Thus the extension is not split, and its Yoneda class is nonzero. Nonemptiness of the actual zero divisor is the established original-zeta fact used in CW8; that proof also obtains it from the full order-one source factorization, its reflection identity, and \(F_0(0)=1/8\ne F_0(2)=\pi/24\). No hypothetical zero is used.

The exact relationship of the global class to (CLP6.6) is pullback along an actual polynomial vector. An element \(q_0\in Q(-1)[P]\) defines the homomorphism
\[
f_{q_0}:R/(P)\to Q(-1),\qquad[H(t)]\mapsto H(t)q_0.
\]
The pullback extension has middle module
\[
E_{q_0}=\{(b,\overline H)\in A(-1)\oplus R/(P):
q(b)=H(t)q_0\}.
\tag{CLP12.7}
\]
Choose \(b\) lifting \(q_0\). The lift \((b,1)\) of the generator obeys the relation
\(P(t)(b,1)=(P(L+1)b,0)\). Applying the two-term free resolution therefore represents its extension class by
\[
f_{q_0}^*e=[P(L+1)b]
\in\operatorname{Ext}^1_R(R/(P),J(-1))
=J(-1)/P(L+1)J.
\tag{CLP12.8}
\]
Changing \(b\) by an element of \(J\) changes this relation by \(P\) times that element, so this is exactly the positive class (CLP6.6). This proves the requested receiving map from the global extension to every finite spectral boundary, including its nonzero values at \(\rho+1\).

The zero Postnikov class in CDW7 concerns the different triangle separating the degree-zero direct image \(\Omega\) from its winding summand \(\mathscr W[-1]\). The horizontal coefficient extension (CLP12.3) within that retained winding summand is not that Postnikov class. Equations (CLP12.2) and (CLP12.5) prove the relation: the direct-image splitting retains the entire horizontal extension, whose class is \(e\ne0\), while the ordinary degree-one localization boundary and the vertical Postnikov class are zero in their own specified triangles.

## CLP13. Actual coherent-family separation and its contracting inverse

PGF0–PGF9 were read in full for this extension of the calculation. PGF2 and PGF6 construct holomorphic families of the precise source quotients used in (CLP5.1), with uniform division estimates on compact parameter sets and explicit Gaussian and \(F_0\)-polynomial interpolation sections. Their actual inclusion matrix is the complete \(\mathsf T_r(\lambda)\) of (CLP5.2). Let \(\mathcal O\) denote the sheaf of holomorphic functions on the parameter plane, and define the original and normal family cokernels by
\[
\mathscr C_r=\operatorname{coker}
(\mathcal O^r\xrightarrow{\mathsf T_r(\lambda)}\mathcal O^r),
\qquad
\mathscr C_r^+=\operatorname{coker}
(\mathcal O^r\xrightarrow{\mathsf T_r(\lambda-1)}\mathcal O^r).
\tag{CLP13.1}
\]
The second is the pullback of the first by \(\lambda\mapsto\lambda-1\). It is exactly the normal matrix of (CLP6.7), because its generator is \(L+1\); no additional sheaf is chosen to manufacture its support. The parameter plane is a plane of recovered coefficient eigenvalues, not coordinates or a distance on \(\tau\).

Both matrix sheaf maps in (CLP13.1) are injective. Multiplying a germ in the kernel by the adjugate kills each component by respectively \(F_0(\lambda)^r\) or \(F_0(\lambda-1)^r\). Those are nonzero germs in the integral domain of holomorphic germs, so each component vanishes. Thus both displayed maps extend to length-one locally free resolutions of their cokernels. Their supports are exactly
\[
\operatorname{Supp}\mathscr C_r=\mathscr Z
\subset\{0<\Re\lambda<1\},\qquad
\operatorname{Supp}\mathscr C_r^+=\mathscr Z+1
\subset\{1<\Re\lambda<2\}.
\tag{CLP13.2}
\]
Invertibility off those sets follows from the determinant; nonzero stalks on them follow from the following exact local calculation.

At \(\rho\), put \(x=\lambda-\rho\), retain the jet variable \(h=s-\lambda\), and put \(y=x+h=s-\rho\). Write
\[
F_0(\rho+y)=y^m b_\rho(y),\quad
b_\rho(y)=C_0(\rho+y)\frac{\zeta(\rho+y)}{y^m},\qquad b_\rho(0)\ne0.
\tag{CLP13.3}
\]
The original matrix is multiplication by \((x+h)^m b_\rho(x+h)\) on \(\mathbb C\{x\}[h]/(h^r)\). Multiplication by the full unit \(b_\rho(x+h)\), with inverse its full reciprocal jet, is the exact domain comparison with multiplication by \((x+h)^m\). It follows that
\[
(\mathscr C_r)_\rho\simeq
\mathbb C\{x,h\}/(h^r,(x+h)^m)
\simeq\mathbb C\{y,h\}/(y^m,h^r).
\tag{CLP13.4}
\]
The coordinate maps are \(y=x+h\) and \(x=y-h\); they preserve the original coordinate formulas. The monomials \(y^ih^j\), \(0\le i<m\), \(0\le j<r\), form a basis, so the length is \(mr\). The parameter operator \(x=y-h\) has exact nilpotence exponent \(m+r-1\), because its power one below that has the nonzero term
\[
(y-h)^{m+r-2}
=(-1)^{r-1}\binom{m+r-2}{m-1}y^{m-1}h^{r-1}.
\tag{CLP13.5}
\]
All other terms in that power vanish in (CLP13.4). The normal stalk at \(\rho+1\) has the identical module, now with \(x=\lambda-(\rho+1)\), \(h=s-(\lambda-1)\), and the same \(y=x+h=s-\rho\).

The arithmetic generator is not this parameter operator \(x\). The coefficient action on the original family is multiplication by
\[
a^{\lambda+h}=a^\rho\exp((\log a)y),
\tag{CLP13.6}
\]
so its nilpotent part is multiplication by \(y\), whose exact exponent is \(m\), not \(m+r-1\). Explicitly
\[
y^ih^j\longmapsto a^\rho
\sum_{k=0}^{m-1-i}\frac{(\log a)^k}{k!}y^{i+k}h^j.
\tag{CLP13.7}
\]
On the normal family, the actual normal coefficient action is also \(a^{\lambda+h}\), but now its scalar is \(a^{\rho+1}\); replace only that scalar in (CLP13.7). This follows from \(s+1=\lambda+h\), retaining the normal factor. These actions commute with the original unit comparison. Therefore all finite-length original stalks have scalar weights \(2\Re\rho\in(0,2)\), and all normal stalks have scalar weights \(2\Re\rho+2\in(2,4)\), with their full nilpotents and all parameter extensions present.

Specialization keeps the higher boundary. Applying the fibre functor to the proved free normal resolution gives
\[
0\to\operatorname{Tor}^{\mathcal O}_1(\mathscr C_r^+,\mathbb C_\lambda)
\to\mathbb C[h]/h^r\xrightarrow{\mathsf T_r(\lambda-1)}
\mathbb C[h]/h^r\to\mathscr C_r^+\otimes\mathbb C_\lambda\to0.
\tag{CLP13.8}
\]
The actual isomorphism from \(Q(-1)[P]\) to its first term is precisely the positive boundary (CLP6.6), in the coordinates (CLP5.1); its basis is (CLP6.8). The final term is \(Q(-1)/P(L+1)Q\). Each has dimension \(\min(r,m_{\lambda-1})\), while the local family length is \(r m_{\lambda-1}\). The family sheaf injection has zero kernel; its specialized kernel is this Tor group. These are different operations with their exact connecting map retained.

There is now a full derived separation result for these actual families. For all integers \(r,q\ge1\),
\[
\boxed{\mathbf R\mathcal Hom_{\mathcal O}(\mathscr C_r,\mathscr C_q^+)
\simeq0,\qquad
\mathbf R\mathcal Hom_{\mathcal O}(\mathscr C_q^+,\mathscr C_r)
\simeq0.}
\tag{CLP13.9}
\]
We prove it with an explicit contraction, rather than only invoking disjoint support. Resolve \(\mathscr C_r\) by its two free terms in degrees minus one and zero. After the second-coordinate sign convention of (CLP4.1), internal Hom into \(\mathscr C_q^+\) is the two-term complex
\[
(\mathscr C_q^+)^r\xrightarrow{\mathsf T_r(\lambda)^{\mathsf T}}
(\mathscr C_q^+)^r
\tag{CLP13.10}
\]
in degrees zero and one. Equivalently its differential sends a map \(\phi:\mathcal O^r\to\mathscr C_q^+\) to \(\phi\mathsf T_r(\lambda)\).

On the open set \(\Re\lambda>1\), which contains the whole support of the target family, this matrix is invertible. Its inverse is the transpose of the complete lower-triangular matrix with coefficients
\[
\frac1{k!}\left(\frac{d}{ds}\right)^k
\left[\frac{8\pi^{s/2}}{s(s-1)\Gamma(s/2)\zeta(s)}\right]_{s=\lambda},
\quad 0\le k<r.
\tag{CLP13.11}
\]
Here \(F_0\) has no zeros, and all displayed reciprocal factors are holomorphic on this open set. On the complementary open set \(\mathbb C\setminus(\mathscr Z+1)\), the target sheaf is zero. Define the inverse there as the unique endomorphism of the zero sheaf. The two definitions agree on the overlap and therefore glue to an inverse sheaf endomorphism of (CLP13.10). If \(h\) denotes this inverse from degree one to degree zero, then \(dh=1\) in degree one and \(hd=1\) in degree zero. Thus it is an explicit contracting homotopy.

For the reverse Hom, resolve \(\mathscr C_q^+\). Its differential is precomposition with \(\mathsf T_q(\lambda-1)\) on \(\mathscr C_r\)-valued maps. On \(0<\Re\lambda<1\), containing the whole support of \(\mathscr C_r\), its inverse uses the complete coefficients (CLP13.11) evaluated at \(s=\lambda-1\), with \(q\) in place of \(r\). These are exactly (CLP7.3)–(CLP7.6), on their full open zero-free domain. Glue with the zero map off \(\mathscr Z\) as before. This contracts the reverse Hom complex and proves both statements in (CLP13.9).

The contractions commute with the specified arithmetic action. On the free jet source the action is multiplication by \(a^{\lambda+h}\), and both \(\mathsf T_r\) and its inverse are multiplication by full series in the same jet variable. On the target the analogous coefficient action commutes with holomorphic scalar entries. Hence precomposition with the inverse commutes with the induced Hom action \(\phi\mapsto U_{\rm target}\phi U_{\rm source}^{-1}\). The same argument applies to the normal source. Thus no unproved differentiation of a discontinuous functional, finite-block density, or arbitrary classification of characters is used.

Taking derived global sections of the zero internal Hom complexes gives
\[
\operatorname{Ext}^k_{\mathcal O}(\mathscr C_r,\mathscr C_q^+)=0,
\qquad\operatorname{Ext}^k_{\mathcal O}(\mathscr C_q^+,\mathscr C_r)=0
\quad(k\ge0).
\tag{CLP13.12}
\]
This uses the explicit length-one locally free resolutions and their internal Hom computation; no additional vanishing theorem for coherent cohomology is needed. Applying \(\mathbf R\mathcal Hom(\mathscr C_r,-)\) to the actual normal free resolution consequently makes the source-to-target map
\[
\mathbf R\mathcal Hom(\mathscr C_r,\mathcal O^q)
\xrightarrow{\ (\mathsf T_q(\lambda-1))_*\ }
\mathbf R\mathcal Hom(\mathscr C_r,\mathcal O^q)
\tag{CLP13.13}
\]
a quasi-isomorphism: its cone is the first zero complex in (CLP13.9). This is the derived family version of the actual normal spectral lift in (CLP7.7).

The exact scope of this separation is now fixed by (CLP13.1), (CLP13.8) and (CLP13.13): it controls the original and normal cokernel families of the actual source-inclusion matrices. It preserves the nonzero global normal extension (CLP12.3), and the higher boundary on its own normal support (CLP8.3). It does not give a separated bound for every quotient of \(J(-1)\), identify these coherent families with Deligne's étale inertia groups, or change the real parts of the original zeros. Both the family vanishing and its surviving shifted boundary are consequences of the same original localization row.
