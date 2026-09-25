# Continuous duals of the actual sphere coefficient and support complexes

Independent mathematical derivation, 24 September 2026. Proof locators CDI0–CDI12.

The complete source `../tau_weight_cohomology_20260924/CC_SPHERE_PULLBACK_AND_NORMAL_DIRECTION.md`, CSP0–CSP13, was read, including the pole orientation calculation and its localization cone. The exact source-image theorem SSI1–SSI7 and independent ESI0–ESI12 supply the closedness and continuous source inverse used below. This calculation takes the stated coefficient complexes as actual inputs; it constructs their continuous duals and all transposed maps. It does not identify the resulting complexes with an unconstructed Verdier dual sheaf or assume arithmetic purity.

Every vector-space operation below is on the reconstructed arithmetic coefficient spaces. The support notation \(Z_0,Z_1,\ldots,\tau\) is unchanged. No addition, numerical coordinate, distance, or numerical weight is assigned to \(\tau\).

## CDI0. Exact input and dual conventions

Retain the CSP coefficient spaces
\[
S=\{f\in\mathcal S(\mathbb R):f(-x)=f(x),\ f(0)=0,\ \int_{\mathbb R}f=0\},
\qquad V_\pm=S\oplus E_\pm,\quad E_\pm=\mathbb C^2,
\]
\[
A=\left\{a\in C^\infty(\mathbb R_{>0}):
\sup_{u>0}(u^N+u^{-N})|(u\partial_u)^ja(u)|<\infty
\text{ for all }N,j\ge0\right\},
\]
\[
\Sigma f(u)=2\sum_{n\ge1}f(nu),\quad Ra(u)=u^{-1}a(u^{-1}),
\quad r_+(f,e)=\Sigma f,\quad r_-(h,e)=R\Sigma h=\Sigma\widehat h.
\tag{CDI0.1}
\]
The original Fourier convention is \(\widehat h(t)=\int h(x)e^{-2\pi ixt}dx\). Let
\[
J=\Sigma S\subset A,\qquad Q=A/J,\qquad q:A\to Q.
\tag{CDI0.2}
\]
The exact-image theorem proves that \(J\) is closed and that \(\Sigma:S\to J\) is a topological isomorphism. All spaces in (CDI0.1) and (CDI0.2) are therefore Hausdorff Fréchet spaces with their stated subspace, finite-product, and quotient topologies. In particular no closure of zero remains in \(Q\).

For a Hausdorff locally convex space \(E\), write \(E'\) for its continuous complex-linear dual. Two topologies will remain explicit:
\[
E'_\sigma=(E',\sigma(E',E)),\qquad
E'_\beta=(E',\beta(E',E)).
\tag{CDI0.3}
\]
The first is convergence on every finite set of vectors; the second is uniform convergence on every bounded subset of \(E\). No algebraic dual of discontinuous functionals is substituted for either. For a continuous map \(f:E\to F\), its ordinary transpose is \(f':F'\to E'\), \(f'\lambda=\lambda\circ f\). It is continuous for both topologies: finite evaluation sets pull back to finite sets, and continuous linear maps take bounded sets to bounded sets.

For a cochain complex \(C\), define
\[
(C^\vee)^n=(C^{-n})',\qquad
d_{C^\vee}^n\lambda=(-1)^{n+1}\lambda\circ d_C^{-n-1}.
\tag{CDI0.4}
\]
This is the usual Hom differential. The evaluation map in the order \(C^\vee\otimes C\to\mathbb C\) satisfies the cochain identity: the two terms \((-1)^{n+1}\lambda(dc)\) and \((-1)^n\lambda(dc)\) cancel. A degree-zero chain map transposes without an additional sign. Weak or strong topologies on each dual coefficient produce the same underlying vector complex; their cohomology topologies will be distinguished below.

## CDI1. Explicit source splittings and the exact continuous transpose

Define continuous sections onto the actual closed image:
\[
s_+(j)=(\Sigma^{-1}j,0)\in V_+,
\qquad
s_-(j)=(\widehat{\Sigma^{-1}j},0)\in V_-.
\tag{CDI1.1}
\]
Poisson and \(\widehat{\widehat f}=f\) on \(S\) give \(r_\pm s_\pm=1_J\). Hence
\[
V_\pm\xrightarrow{\sim}E_\pm\oplus J,
\qquad v\longmapsto\bigl(v-s_\pm r_\pm v,\ r_\pm v\bigr)
\tag{CDI1.2}
\]
are continuous isomorphisms. Their inverses are \((e,j)\mapsto e+s_\pm j\); the first coordinate on the right of (CDI1.2) lies in the actual endpoint kernel.

Put \(W=V_+\oplus V_-\), \(d(v_+,v_-)=r_+v_+-r_-v_-\), and \(Z=\ker d\). The common-restriction description is
\[
Z\xrightarrow{\sim}J\oplus E_+\oplus E_-,
\quad (v_+,v_-)\longmapsto(r_+v_+,e_+,e_-).
\tag{CDI1.3}
\]
Its inverse sends \((j,e_+,e_-)\) to \((s_+j+e_+,s_-j+e_-)\). These are the exact Fourier-graph coordinates of CSP4.5, with all four endpoint lines retained.

The map \(t:J\to W\), \(t(j)=(s_+j,0)\), satisfies \(dt=1\). Therefore
\[
W\xrightarrow{\sim}Z\oplus J,
\quad w\longmapsto(w-t(dw),dw),
\qquad (z,j)\longmapsto z+t(j).
\tag{CDI1.4}
\]
This explicit splitting will be used on the domain side. It does not assert that the closed inclusion \(J\hookrightarrow A\) has a continuous projection or that \(q\) has a continuous section.

The continuous transpose of
\(0\to J\to A\xrightarrow q Q\to0\)
is algebraically exact:
\[
0\longrightarrow Q'\xrightarrow{q'}A'
\xrightarrow{\operatorname{res}_J}J'\longrightarrow0.
\tag{CDI1.5}
\]
Indeed \(q'\) is injective because \(q\) is onto. Its image is
\[
J^\perp=\{\lambda\in A':\lambda(j)=0\text{ for every }j\in J\},
\tag{CDI1.6}
\]
since a continuous functional constant on quotient fibers factors continuously through the quotient topology. Finally every continuous complex-linear functional on the subspace \(J\) extends continuously to \(A\) by the complex Hahn–Banach theorem: continuity bounds it by a continuous seminorm induced from \(A\), and Hahn–Banach gives an extension with that bound. This proves surjectivity in (CDI1.5), not merely density of its image.

The corresponding exact identities are
\[
\ker d'=J^\perp=q'Q',\qquad
\operatorname{im}d'=Z^\perp\subset W',
\tag{CDI1.7}
\]
where \(d'\lambda=(r_+'\lambda,-r_-'\lambda)\). To prove the second equality completely, a continuous \(\phi\in W'\) vanishing on \(Z\) gives the continuous functional \(j\mapsto\phi(tj)\) on \(J\). Extend it to \(\lambda\in A'\) by (CDI1.5); (CDI1.4) gives \(\phi=d'\lambda\). Conversely every \(d'\lambda\) vanishes on \(Z\). Likewise
\[
\ker r_\pm'=q'Q',\qquad
\operatorname{im}r_\pm'=E_\pm^\perp\subset V_\pm'.
\tag{CDI1.8}
\]
Thus every transpose image needed for the coefficient cohomology is calculated exactly.

## CDI2. The dual global and costalk complexes

The global CSP complex is
\[
D^0=W\xrightarrow{\ d\ }D^1=A\xrightarrow{\ 0\ }D^2=A.
\tag{CDI2.1}
\]
Its continuous dual, with the convention (CDI0.4), is
\[
(D^\vee)^{-2}=A'
\xrightarrow{\ 0\ }(D^\vee)^{-1}=A'
\xrightarrow{\lambda\mapsto(r_+'\lambda,-r_-'\lambda)\ }
(D^\vee)^0=V_+'\oplus V_-'.
\tag{CDI2.2}
\]
The minus sign in the second chart comes from the original chart difference, not from an added dualization convention: the Hom differential at degree \(-1\) has sign \(+1\).

Equations (CDI1.7) give all groups and their evaluation pairings:
\[
H^{-2}(D^\vee)=A',\qquad
H^{-1}(D^\vee)=q'Q'\cong Q',\qquad
H^0(D^\vee)=W'/Z^\perp\cong Z'.
\tag{CDI2.3}
\]
The last map is restriction to \(Z\); it is onto because the projection in (CDI1.4) supplies a continuous extension of every functional on \(Z\). For representatives the exact pairings are
\[
\langle\lambda,a\rangle=\lambda(a)\quad(H^{-2},H^2),
\]
\[
\langle q'\mu,[a]\rangle=\mu([a])\quad(H^{-1},H^1),
\]
\[
\langle[\phi],z\rangle=\phi(z)\quad(H^0,H^0).
\tag{CDI2.4}
\]
The middle expression is independent of a representative because \(q'\mu\) vanishes on \(J\); the last is independent because boundaries are exactly \(Z^\perp\).

At each pole, the costalk complex is
\[
L_p^0=V_p\xrightarrow{\ r_p\ }L_p^1=A\xrightarrow{\ 0\ }L_p^2=A,
\quad p\in\{+,-\}.
\tag{CDI2.5}
\]
Its dual is
\[
(L_p^\vee)^{-2}=A'\xrightarrow{0}(L_p^\vee)^{-1}=A'
\xrightarrow{r_p'}(L_p^\vee)^0=V_p',
\tag{CDI2.6}
\]
Its coefficient degrees are \(-2,-1,0\), and its cohomology is
\[
H^{-2}(L_p^\vee)=A',\qquad
H^{-1}(L_p^\vee)=q'Q'\cong Q',\qquad
H^0(L_p^\vee)=V_p'/E_p^\perp\cong E_p'.
\tag{CDI2.7}
\]
The pairings are evaluation on the original costalk groups \(A,Q,E_p\), with both positive local complex orientations retained as in CSP6.

If one wants a complex indexed in degrees \(0,1,2\), the precisely specified shift is \(D^\vee[-2]\): its term of degree \(i\) is \((D^{2-i})'\), and its differential has no additional sign because the shift is even. It pairs with \(D\) in complementary degrees summing to two. This is a shift of the constructed coefficient complex; calling it a shifted complex does not establish a sheaf-duality comparison.

## CDI3. Separated perfect continuous-dual pairings and their topologies

For each Hausdorff locally convex space \(E\) in the cohomology list \(Z,Q,A,E_\pm\), the evaluation pairing \(E'\times E\to\mathbb C\) is separated in both arguments. A nonzero vector is separated by a continuous functional using Hahn–Banach and a continuous seminorm nonzero on that vector; a nonzero functional is nonzero on some vector by its definition. The dual groups in (CDI2.3) and (CDI2.7) are the **entire continuous duals** of the respective primal groups. This is the precise sense of a perfect continuous-dual pairing used here. It does not mean that every discontinuous algebraic functional is continuous, and does not assert a Hilbert inner product or positivity.

Equipped with the weak dual topology, the second dual in the opposite direction is also exactly the original vector space. Indeed a continuous linear \(\Lambda:E'_\sigma\to\mathbb C\) is bounded by finitely many evaluation seminorms \(|\lambda(e_i)|\). It vanishes on the common kernel of those evaluations, factors through their finite-dimensional image, and is a linear combination of them. Hence \(\Lambda(\lambda)=\lambda(e)\) for one \(e\in E\), unique by separation. Thus
\[
(E'_\sigma)'=E
\tag{CDI3.1}
\]
as vector spaces with the specified evaluation map. The pairing is separately continuous. No claim of joint continuity or an isomorphism between the original topology on \(E\) and a bidual topology is required by this argument.

For weak dual coefficient topologies, all cohomology identifications in CDI2 are topological identifications with the respective weak duals. For \(q'Q'\subset A'\), evaluation at \(a\) is exactly evaluation at \(q(a)\), and every element of \(Q\) has a representative, so the induced weak topology is exactly \(\sigma(Q',Q)\). For the degree-zero quotients, the explicit topological splittings (CDI1.2) and (CDI1.4) transpose to finite direct-product splittings of weak duals; quotienting by the entire complementary dual factor gives precisely \((E_p)'_\sigma\) or \(Z'_\sigma\).

For clarity, the surjection \(A'_\sigma\to J'_\sigma\) in (CDI1.5) is also a quotient map. A basic weak neighborhood constrains a functional on a finite-dimensional subspace \(L\subset A\). The possible restrictions to \(J\) are determined solely by its values on \(L\cap J\). Restriction \(L'\to(L\cap J)'\) is an open surjective finite-dimensional map. Any two compatible continuous functionals on \(J\) and \(L\) combine to a continuous functional on \(J+L\): a finite-dimensional complement of \(J\cap L\) in \(L\) maps homeomorphically onto its finite-dimensional image in the Hausdorff quotient \(A/J\), yielding a topological direct sum with \(J\). Hahn–Banach then extends the combined functional to \(A\). This proves that images of basic weak neighborhoods are weak neighborhoods. Thus (CDI1.5) is exact with its stated weak subspace and quotient topologies.

For strong duals the following statements are proved without any bounded-lifting assumption. The decompositions (CDI1.2) and (CDI1.4) are topological finite direct sums, so their strong duals also split. In particular the degree-zero dual cohomology is exactly \(Z'_\beta\), respectively \((E_p)'_\beta\), and the degree-minus-two group is \(A'_\beta\). All dual differential images are closed in both weak and strong coefficient topologies, since they are the annihilators of the displayed closed kernels and those annihilators are intersections of evaluation kernels.

The degree-minus-one group with its topology inherited from \(A'_\beta\) is the vector space \(Q'\) with the exact seminorm family
\[
p_B^{\rm induced}(\mu)=\sup_{a\in B}|\mu(q(a))|,
\qquad B\subset A\text{ bounded}.
\tag{CDI3.2}
\]
The canonical map
\[
Q'_\beta\longrightarrow (J^\perp,\text{subspace topology from }A'_\beta),
\quad\mu\longmapsto q'\mu
\tag{CDI3.3}
\]
is a continuous bijection. Each image \(q(B)\) is bounded in \(Q\), proving continuity. This proof does not identify (CDI3.2) with uniform convergence on **all** bounded subsets of \(Q\). A proof that bounded subsets of \(Q\) have bounded lifts would give that additional identification, but no such unproved assertion is used. Likewise the strong-topology surjection \(A'_\beta\to J'_\beta\) is algebraically onto and continuous by the proved extension theorem; no strong open-mapping claim is inserted. These precise strong seminorms coexist with the full weak-topology duality already proved.

## CDI4. Transpose of the two-support localization map

Write \(L=L_+\oplus L_-\), with
\[
L^0=W,\qquad L^1=A^2,\qquad L^2=A^2,
\quad d_L^0(v_+,v_-)=(r_+v_+,r_-v_-),\quad d_L^1=0.
\]
The actual CSP support-to-global map has
\[
k^0=1_W,\qquad k^1(b_+,b_-)=b_+-b_-,
\qquad k^2(c_+,c_-)=c_++c_-.
\tag{CDI4.1}
\]
Its continuous transpose is the chain map \(k^\vee:D^\vee\to L^\vee\) with
\[
(k^\vee)^0=1_{W'},\qquad
(k^\vee)^{-1}\lambda=(\lambda,-\lambda),\qquad
(k^\vee)^{-2}\lambda=(\lambda,\lambda).
\tag{CDI4.2}
\]
The dual supported differential is
\[
d_{L^\vee}^{-1}(\lambda_+,\lambda_-)
=(r_+'\lambda_+,r_-'\lambda_-).
\tag{CDI4.3}
\]
Substitution gives \(d_{L^\vee}^{-1}(\lambda,-\lambda)=d_{D^\vee}^{-1}\lambda\), proving the only nonzero chain compatibility directly.

The induced maps on cohomology are therefore
\[
A'\longrightarrow A'^2:\lambda\mapsto(\lambda,\lambda)
\quad\text{in degree }-2,
\]
\[
Q'\longrightarrow Q'^2:\mu\mapsto(\mu,-\mu)
\quad\text{in degree }-1,
\]
\[
Z'\longrightarrow E_+'\oplus E_-':
\phi\longmapsto(\phi|_{E_+},\phi|_{E_-})
\quad\text{in degree }0.
\tag{CDI4.4}
\]
Each is precisely adjoint to its primal support-to-global map under CDI2's evaluation. For one pole alone, the transpose map from the global dual has degrees \((0,-1,-2)\):
\[
k_+^\vee=(\operatorname{pr}_{V_+'},+1,+1),\qquad
k_-^\vee=(\operatorname{pr}_{V_-'},-1,+1).
\tag{CDI4.5}
\]
Thus the two degree-one signs differ, while both positive local orientation classes have the same degree-two sign.

## CDI5. The full dual localization row and cone signs

Let \(O=A[\text{degree }0]\oplus A[\text{degree }1]\) be the annular model, with zero differential. Reversing the CSP7.6 localization row by the continuous transpose gives the following algebraically exact row:
\[
\begin{aligned}
0\to A'&\xrightarrow{\lambda\mapsto(\lambda,\lambda)} A'^2
\xrightarrow{(\lambda_+,\lambda_-)\mapsto-\lambda_++\lambda_-}A'
\xrightarrow{0}Q'\\
&\xrightarrow{\mu\mapsto(\mu,-\mu)}Q'^2
\xrightarrow{(\mu_+,\mu_-)\mapsto q'(\mu_++\mu_-)}A'
\xrightarrow{r'}Z'\xrightarrow{\operatorname{res}}E_+'\oplus E_-'\to0.
\end{aligned}
\tag{CDI5.1}
\]
Here \(r:Z\to A\) is the common restriction, and in (CDI1.3) its transpose is
\[
r'\lambda=(\lambda|_J,0,0).
\tag{CDI5.2}
\]
Exactness can be checked without a general topological exactness axiom. The first two nonzero maps are diagonal and signed difference, hence have the displayed kernels and images. The next zero map has kernel all of \(A'\), exactly the preceding image. The kernel of the sum on \(Q'^2\) is its anti-diagonal. The image of that sum composed with \(q'\) is \(J^\perp\), the kernel of \(r'\). Hahn–Banach makes \(r'\) onto the \(J'\)-summand of \(Z'\), which is exactly the kernel of endpoint restriction. That restriction is onto by the direct-sum decomposition of \(Z\). All arrows are continuous for both dual topologies; the weak topologies are the exact subspace and quotient topologies proved in CDI3. Strong algebraic exactness does not assert the additional strong quotient identifications excluded in CDI3.

One can check every cone sign directly too. Put \(E=\operatorname{Cone}(k)\) with the standard differential
\(d_E(x,y)=(d_Dx+ky,-d_Ly)\). Its coefficient degrees from CSP7.3 are
\[
E^{-1}=W,\quad E^0=W\oplus A^2,\quad
E^1=A\oplus A^2,\quad E^2=A.
\]
By (CDI0.4), its dual differentials are exactly
\[
(E^\vee)^{-2}=A'\longrightarrow(E^\vee)^{-1}=A'\oplus A'^2,
\quad \lambda\longmapsto(0,-\lambda,-\lambda),
\]
\[
(\lambda,\mu_+,\mu_-)\longmapsto(d'\lambda,\lambda,-\lambda)
\quad\text{from degree }-1\text{ to }0,
\]
\[
(\phi,\nu_+,\nu_-)\longmapsto
-\phi+(r_+'\nu_+,r_-'\nu_-)
\quad\text{from degree }0\text{ to }1.
\tag{CDI5.3}
\]
The last target is \(W'\). In particular the diagonal in the first line has a negative sign from the Hom differential in degree \(-2\), while the diagonal cohomology map in (CDI4.2) has a positive sign; these are different maps.

The transpose of the CSP7.4 annular inclusion is a quasi-isomorphism \(E^\vee\to O^\vee\). In degree zero it sends
\((\phi,\nu_+,\nu_-)\mapsto\nu_++\nu_-\); in degree minus one it sends
\((\lambda,\mu_+,\mu_-)\mapsto-\mu_++\mu_-\).
To prove this, a degree-zero cocycle has \(\phi=(r_+'\nu_+,r_-'\nu_-)\). Its displayed image is zero precisely when \(\nu_-=-\nu_+\), in which case it is the boundary of \((\nu_+,0,0)\) in degree minus one. Every target value has a cocycle representative by taking \(\nu_+=\nu\), \(\nu_-=0\), and the required \(\phi\). A degree-minus-one cocycle has \(\lambda=0\), while the other coordinates are arbitrary. Its displayed image vanishes precisely on the diagonal, which is the image of degree minus two in (CDI5.3). It is onto by taking \(\mu_+=0\). The other two degrees have zero cohomology by injectivity of the first differential and surjectivity of the last. These choices are continuous finite operations, so the annular dual comparison is valid with either topology.

For a general chain map with the present Hom convention, the exact relation between the two cone presentations is
\[
\operatorname{Cone}(k)^\vee
\xrightarrow{\sim}\operatorname{Cone}(k^\vee)[-1],
\qquad (\phi,\psi)\longmapsto\bigl((-1)^{n+1}\psi,\phi\bigr)
\text{ in degree }n.
\tag{CDI5.4}
\]
Indeed the differential of the left side is
\((d_{D^\vee}\phi,d_{L^\vee}\psi+(-1)^{n+1}k^\vee\phi)\); the target shifted-cone differential is
\((\alpha,\beta)\mapsto(-d_{L^\vee}\alpha-k^\vee\beta,d_{D^\vee}\beta)\).
Substitution of the displayed sign proves equality. This accounts for the localization-cone shift without suppressing a boundary sign.

## CDI6. Ordinary transposes, contragredients, and original spectral jets

For \(a>0\), use the CSP actions
\[
T_ab(u)=b(u/a),
\]
\[
\rho_+(a)(f,c_0,c_1)=(f(\cdot/a),c_0,ac_1),
\qquad
\rho_-(a)(h,d_0,d_1)=(a h(a\cdot),ad_0,d_1).
\tag{CDI6.1}
\]
The combined sphere-cover action on \(D\), extended from the recovered integer covers to the indicated real coefficient action as in CSP8, is
\[
\mathsf B_a^0=\rho_+(a)\oplus\rho_-(a),\qquad
\mathsf B_a^1=T_a,\qquad \mathsf B_a^2=aT_a.
\tag{CDI6.2}
\]
The same degree factors occur on each costalk, and on \(O\) the degree-zero and degree-one actions are \(T_a\) and \(aT_a\). A nonintegral \(a\) here does not designate a holomorphic map \(z\mapsto z^a\).

The ordinary transpose \((\mathsf B_a^i)'\) satisfies the adjoint identity
\(\langle(\mathsf B_a^i)'\lambda,x\rangle=\langle\lambda,\mathsf B_a^ix\rangle\).
For an invariant evaluation pairing one must instead use the contragredient
\[
\mathsf B_a^\vee|_{(D^\vee)^{-i}}=(\mathsf B_{a^{-1}}^i)'.
\tag{CDI6.3}
\]
Then \(\langle\mathsf B_a^\vee\lambda,\mathsf B_ax\rangle=\langle\lambda,x\rangle\). Its exact coefficient actions, in degrees \(0,-1,-2\), are
\[
\rho_+(a^{-1})'\oplus\rho_-(a^{-1})',\qquad
(T_{a^{-1}})',\qquad a^{-1}(T_{a^{-1}})'.
\tag{CDI6.4}
\]
In particular the four dual endpoint characters are \(1,a^{-1},a^{-1},1\). In the common-restriction coordinates (CDI1.3), the other degree-zero dual summand \(J'\) carries \((T_{a^{-1}}|_J)'\). Every transposed support and localization map intertwines these actions because its primal map intertwines (CDI6.2); direct substitution in CDI4–CDI5 verifies the factors.

Retain the CSP Mellin comparison including its scalar:
\[
\Theta b(s)=\frac12\int_0^\infty b(u)u^s\frac{du}{u},\qquad
\Theta T_ab(s)=a^s\Theta b(s),\qquad \Theta J=\mathcal I.
\tag{CDI6.5}
\]
Thus \([b]\mapsto[\Theta b]\) identifies \(Q\) with \(\mathcal B/\mathcal I\). For every actual nontrivial zero \(\rho\) and \(0\le j<m_\rho\), its continuous jet functional is
\[
\delta_{\rho,j}([b])=(\Theta b)^{(j)}(\rho).
\tag{CDI6.6}
\]
Using the raw transform instead would multiply this functional by 2; that factor is not suppressed in (CDI6.5).

Leibniz's rule gives the full triangular matrices
\[
T_a'\delta_{\rho,j}
=a^\rho\sum_{\ell=0}^j\binom j\ell(\log a)^{j-\ell}\delta_{\rho,\ell},
\]
\[
(T_{a^{-1}})'\delta_{\rho,j}
=a^{-\rho}\sum_{\ell=0}^j\binom j\ell(-\log a)^{j-\ell}\delta_{\rho,\ell}.
\tag{CDI6.7}
\]
The contragredient of the normal action \(aT_a\) has instead
\[
a^{-\rho-1}\sum_{\ell=0}^j\binom j\ell(-\log a)^{j-\ell}\delta_{\rho,\ell}.
\tag{CDI6.8}
\]
These formulas are valid for every actual zero with its full multiplicity. They retain the extra geometric degree factor and do not assume \(\Re\rho=1/2\).

## CDI7. Mirrors, orientation, and the reflected degree characters

Let \(\varepsilon=+1\) for the holomorphic sphere swap \(w(z)=-1/z\), and \(\varepsilon=-1\) for the antiholomorphic swap \(\alpha(z)=-1/\overline z\). Both use the actual source coefficient comparison of CSP9. In degrees \(0,1,2\), their global maps are
\[
M_\varepsilon=(\text{chart swap},-R,\varepsilon R).
\tag{CDI7.1}
\]
Since these are involutions, their ordinary transpose and contragredient coincide. On \(D^\vee\), in degrees \(0,-1,-2\), their exact maps are
\[
M_\varepsilon^\vee=(\text{dual chart swap},-R',\varepsilon R').
\tag{CDI7.2}
\]
The two supported copies have degree-minus-one action
\((\lambda_+,\lambda_-)\mapsto(R'\lambda_-,R'\lambda_+)\)
and degree-minus-two action
\((\lambda_+,\lambda_-)\mapsto(\varepsilon R'\lambda_-,\varepsilon R'\lambda_+)\).
The annular dual has degree-zero action \(R'\) and degree-minus-one action \(-\varepsilon R'\). Thus (CDI4.2)'s anti-diagonal and diagonal intertwine these maps: in degree minus one, the swap sends \((\lambda,-\lambda)\) to \((-R'\lambda,R'\lambda)\), precisely the image of \(-R'\lambda\); in degree minus two, the image of \(\varepsilon R'\lambda\) is the required diagonal. The signed annular maps in CDI5 agree too.

Raw Mellin reflection, or its retained scalar version, gives
\(\Theta Rb(s)=\Theta b(1-s)\). Hence
\[
R'\delta_{\rho,j}=(-1)^j\delta_{1-\rho,j}.
\tag{CDI7.3}
\]
The actual global degree-one mirror is its negative, so its dual acts by
\((-1)^{j+1}\delta_{1-\rho,j}\). The degree-two mirror has the factor \(\varepsilon(-1)^j\). The functional equation preserves the exact multiplicity between \(\rho\) and \(1-\rho\), since its multiplier is holomorphic and nonzero there.

The degree character changes the reflection center of the represented exponents. For a coefficient carrying \(a^kT_a\), the exact identity is
\[
(a^kT_a)R=a^{2k+1}R(a^{-k}T_{a^{-1}}).
\tag{CDI7.4}
\]
It follows immediately from \(T_aR=aRT_{a^{-1}}\), retaining both powers \(a^k\). The exponents paired by this reflection are \(\rho+k\) and \(1-\rho+k\), whose sum is \(2k+1\). In the unshifted coefficient this is 1; in the actual normal direction \(k=1\), it is 3. For the invariant-pairing contragredient, transposition at the inverse parameter gives
\[
\mathsf B_a^\vee M_\varepsilon^\vee
=a^{-(2k+1)}M_\varepsilon^\vee\mathsf B_{a^{-1}}^\vee
\tag{CDI7.5}
\]
on a degree with that factor. Its exponent pair sums to \(-(2k+1)\). On the degree-zero graph and endpoint coordinates \(k=0\); the source formulas (CDI6.1) verify the same factor \(a\) directly before transposing. Neither mirror allows the normal factor to be omitted, and the antiholomorphic sign \(\varepsilon=-1\) remains independent of these positive dilation characters.

## CDI8. Finite full-zero blocks inside the actual quotient

An exact finite-block comparison with the dual can be constructed without asserting global self-duality. Write \(\mathcal Q=\mathcal B/\mathcal I\) using (CDI6.5). The full zero-jet map is injective by the definition of \(\mathcal I\), with the closed-image theorem already identifying it with the actual source quotient.

For completeness, each individual full jet block has an actual representative. Use the retained auxiliary entire function
\[
F_*(s)=\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2)\zeta(s)\in\mathcal B.
\tag{CDI8.1}
\]
It has precisely the nontrivial-zero divisor and all its multiplicities; its endpoint values are \(F_*(0)=F_*(1)=1/8\), and its values at the cancelled trivial-zero locations are those retained in SSI3 and CSP11. For \(m=m_\rho\), let
\[
A_\rho(s)=F_*(s)/(s-\rho)^m.
\tag{CDI8.2}
\]
Taylor division makes it entire with \(A_\rho(\rho)\ne0\). It belongs to \(\mathcal B\): outside a compact neighborhood of \(\rho\), division costs at most a fixed polynomial factor on any strip; inside, holomorphicity gives a finite bound. For \(0\le j<m\), let \(P_{\rho,j}(t)\) be the Taylor polynomial through degree \(m-1\) of \(t^j/A_\rho(\rho+t)\), and set
\[
\psi_{\rho,j}(s)=A_\rho(s)P_{\rho,j}(s-\rho).
\tag{CDI8.3}
\]
This is in \(\mathcal B\), has jet \(t^j\) modulo \(t^m\) at \(\rho\), and vanishes with the full required order at every other nontrivial zero. This is a comparison construction using the full factor in (CDI8.1), not a replacement for original zeta in the forthcoming residue formula.

Define \(\mathcal Q_{\rm fin}\) as those classes whose full zero-jet family has finite support. Equations (CDI8.2)–(CDI8.3), together with injectivity of the joint jet map, prove the exact vector-space identification
\[
\mathcal Q_{\rm fin}\cong
\bigoplus_{\rho}\mathbb C[t]/(t^{m_\rho}).
\tag{CDI8.4}
\]
Let
\[
\mathscr D_{\rm fin}=\operatorname{span}_{\mathbb C}
\{\delta_{\rho,j}:\rho\text{ actual nontrivial zero},\ 0\le j<m_\rho\}
\subset\mathcal Q'.
\tag{CDI8.5}
\]
The individual jets are continuous, so the displayed inclusion really is in the continuous dual. No statement that \(\mathcal Q_{\rm fin}\) is dense in \(\mathcal Q\) is used.

## CDI9. The original-zeta residue map and its full determinant

For \([G]\in\mathcal Q_{\rm fin}\), define a functional on \(\mathcal Q\) by
\[
\iota([G])([F])=
\sum_{\rho}\operatorname{Res}_{s=\rho}
\frac{F(s)G(1-s)}{\zeta(s)}\,ds.
\tag{CDI9.1}
\]
Only finitely many residues are nonzero: the potentially nonzero poles are at the reflections of the finite support of the zero jets of \(G\). Changing either representative by an element of \(\mathcal I\) makes every residue zero. Each residue is a finite linear combination of the continuous jets of \(F\); consequently (CDI9.1) is a well-defined continuous functional. Its denominator is the original zeta, not (CDI8.1).

Write \(\sigma=1-\rho\), \(m=m_\rho=m_\sigma\), and
\[
\zeta(\rho+t)=t^m u(t),\qquad u(0)\ne0.
\tag{CDI9.2}
\]
Pair the monomial jet \(t^i\) at \(\rho\) with the monomial jet \((s-\sigma)^j\) at \(\sigma\). Reflection substitutes \(-t\) in the latter. The exact local matrix is
\[
P_{ij}=(-1)^j[t^{m-1-i-j}]\frac1{u(t)},
\qquad 0\le i,j<m,
\tag{CDI9.3}
\]
where a coefficient with negative index is zero. The matrix is anti-triangular. Its anti-diagonal entries are \((-1)^j/u(0)\); the reversal permutation has sign \((-1)^{m(m-1)/2}\), while the product of those entry signs has the same sign. Hence
\[
\boxed{\det(P)=u(0)^{-m}\ne0.}
\tag{CDI9.4}
\]
Every nilpotent order is included. Equations (CDI8.3) and (CDI9.4) prove the vector-space isomorphism
\[
\boxed{\iota:\mathcal Q_{\rm fin}\xrightarrow{\sim}\mathscr D_{\rm fin}.}
\tag{CDI9.5}
\]
This statement does not choose a topology on \(\mathcal Q_{\rm fin}\) or assert continuity of a map extending to all of \(\mathcal Q\).

There is, however, a proved complete weak-dual detection statement:
\[
\overline{\mathscr D_{\rm fin}}^{\sigma(\mathcal Q',\mathcal Q)}
=\mathcal Q'.
\tag{CDI9.6}
\]
To prove it without reflexivity, fix \(\lambda\in\mathcal Q'\) and finitely many classes \(q_1,\ldots,q_r\). Consider the linear image
\(L=\{(d(q_1),\ldots,d(q_r)):d\in\mathscr D_{\rm fin}\}\subset\mathbb C^r\).
Any coefficient vector \(c\) annihilating \(L\) makes \(\sum c_iq_i\) annihilated by every full zero jet, hence zero in \(\mathcal Q\). It follows that \(\sum c_i\lambda(q_i)=0\). Finite-dimensional linear algebra now puts \((\lambda(q_i))_i\) in \(L\), so some \(d\in\mathscr D_{\rm fin}\) agrees **exactly** with \(\lambda\) on all the chosen vectors. This proves density for every weak neighborhood. It proves no strong-dual density assertion.

## CDI10. The residue factor and the normal-dual factor remain distinct

The residue comparison has the exact covariance
\[
\boxed{\iota(T_aG)=a(T_{a^{-1}})'\iota(G).}
\tag{CDI10.1}
\]
Indeed its integrand changes by \(a^{1-s}\) when \(G(1-s)\) is replaced by \((T_aG)(1-s)\). Pulling out the scalar \(a\) leaves \(a^{-s}F(s)\), which is exactly the contragredient transpose in (CDI10.1). The equality holds for the full finite residue sum and all its jets, not only for simple zeros.

More generally, with
\(P(F,G)=\iota(G)(F)\), the full character law is
\[
P(a^kT_aF,a^\ell T_aG)=a^{k+\ell+1}P(F,G)
\tag{CDI10.2}
\]
whenever the second argument has finite zero-jet support. This follows by multiplying the integrand by \(a^{k+s}a^{\ell+1-s}\).

The contragredient of the actual normal representation \(Q(-1)\), whose action is \(aT_a\), was independently calculated in (CDI6.4) as
\[
\mathsf N_a^\vee=a^{-1}(T_{a^{-1}})'.
\tag{CDI10.3}
\]
Therefore the same residue map from the unshifted coefficient has the precise comparison
\[
\iota(T_aG)=a^2\mathsf N_a^\vee\iota(G).
\tag{CDI10.4}
\]
The coefficient-dual character \(a(T_{a^{-1}})'\) in (CDI10.1) and the normal contragredient in (CDI10.3) differ by \(a^2\). They cannot be identified by dropping the geometric degree or the inverse in the dual action. Equations (CDI7.4) and (CDI10.2) are consistent: unshifted paired exponents sum to 1; two normal exponents sum to 3. These are exact morphism and pairing identities. They are not positivity statements, and the bilinear residue pairing has not been declared Hermitian.

## CDI11. Actual receiving result

The continuous duals of the specified global, pole-costalk, and localization complexes now have full formulas, all their images and kernels, and perfect separated continuous-dual pairings on every cohomology degree. Closedness of \(J\) and the actual inverse \(\Sigma^{-1}\) enter exactly through CDI1; they ensure that the original quotient and its continuous dual are separated and that no image closure is substituted in the transpose calculation.

The transpose localization map has the anti-diagonal in degree minus one and diagonal in degree minus two; the complete cone and long-row signs are CDI5. The antiholomorphic sphere operation retains its negative degree-two orientation. The ordinary transpose, invariant-pairing contragredient, and original-zeta residue correspondence remain separate exact maps with their full degree characters.

This is a completed duality calculation for the actual finite coefficient models. It does not identify the continuous-dual coefficient complex with the derived sheaf Hom into a dualizing complex, and does not supply an unproved comparison to Deligne's finite-rank étale obstruction receiver. The concrete comparison now available for that further calculation is the entire weak continuous dual in CDI2–CDI5, together with the explicitly reflected finite-jet subspace, nonzero local determinant, and weak-dual density in CDI8–CDI10. No operation or metric on the support \(\tau\) was used.

## CDI12. Independent verification of RD0–RD9

After completing CDI0–CDI11, the full independent root derivation `ORIGINAL_ZETA_RESIDUE_DUAL_AND_SUPPORT_MAPS.md`, RD0–RD9, was read and checked. The reviewed file SHA256 is `65ae37a4303a76dae2fa5d79820201858bce8773afae7138e5b7175586671641`. Its local determinant, explicit inverse, weak-density argument, original-zeta reflection law, and complete normal-action factor require no mathematical correction.

RD1's recursion is the Taylor inversion of the nonvanishing local unit \(A_\rho\). Its isolator has jet 1 at precisely the chosen full block and the required zero jet at all other blocks. Multiplication by the stated finite polynomials preserves \(\mathcal B\). This agrees with CDI8, which supplies the same global block construction independently.

RD2 uses Taylor-coefficient functionals \(\delta_{\rho,j}^{\rm coeff}=F^{(j)}(\rho)/j!\), whereas (CDI6.6) used unscaled derivatives. Its formula
\[
P_{\rho,j}(t)=[t^{m-1-j}u_\rho(t)]_{<m}
\]
does give the exact coefficient functional: subtraction of its omitted Taylor terms leaves a multiple of \(t^m\); division by \(t^m u_\rho(t)\) therefore gives \(t^{-j-1}\) plus a holomorphic germ. The residue is \(F^{(j)}(\rho)/j!\). Thus the factorial conventions in RD2 and RD5.4 agree, and the unscaled formulas in CDI6.7 are their exact multiples by \(j!\).

For RD3, a class supported at \(\sigma=1-\rho\) with local polynomial \(P(-t)\) has reflected germ \(P(t)\) at \(\rho\). It therefore maps under \(\iota\) to the specified original-zeta functional \(\lambda_{\rho,P}\), giving an actual inverse on every finite sum of block functionals. The determinant is exactly (CDI9.4), including cancellation of the two anti-diagonal signs, rather than a determinant modulo a nonzero unspecified constant. RD4 is exactly the finite-evaluation interpolation argument proved in CDI9; the resulting net is pointwise convergent, with no strong-topology or equicontinuity claim.

The second identity in RD5.2 retains the original variable before taking residues: multiplication of the first argument by \(s\) and of the reflected second argument by \(1-s\) sums to multiplication by 1. Hence \(\iota L=(1-L')\iota\). The full factor in RD5.5 is \(a^{k+\ell+1}\), as independently proved in CDI10. For two normal-direction arguments it is \(a^3\); for one normal and one unshifted argument it is \(a^2\). In particular RD5.5 correctly preserves the \(a^2\) comparison with the contragredient of an already normal-shifted coefficient. The cochain degree-character distinction is not lost.

RD6's original-zeta symmetry factor and its minus sign can be checked before any simplification. Set \(\sigma=1-\rho\). The functional equation gives
\[
t^m u_\rho(t)=\chi(\rho+t)(-t)^m u_\sigma(-t),
\]
which is precisely its local-unit identity. In a residue, substitute \(s=1-z\), so \(ds=-dz\). The denominator becomes \(\zeta(1-z)=\zeta(z)/\chi(z)\). Thus the reflected integrand is
\[
-\frac{\chi(z)G(z)F(1-z)}{\zeta(z)}\,dz,
\]
with all derivatives of the displayed \(\chi\)-germ retained. This is RD6.3, including the orientation sign. No claim that its global meromorphic multiplier preserves \(\mathcal B\) is needed. The separately recalled trace form in RD6.4 sees only the constant Taylor coefficient on each block: multiplication by a germ \(h(t)\) on \(\mathbb C[t]/(t^m)\) is triangular with diagonal \(h(0)\), so its trace is \(m h(0)\). In contrast the residue matrix retains all the jets. For the displayed full trace sum, absolute convergence follows from rapid decay of the two \(\mathcal B\) factors on the strip of zeros and the retained zero-count bound \(n(R)=O(R^{3/2})\) from S2. Taking a decay exponent with the product power greater than \(3/2\) proves convergence by dyadic shells. These statements add no positivity assertion.

RD7 uses the actual topological comparison \(\kappa([b])=[\tfrac12\mathcal M_0b]\); its transpose preserves that same factor \(1/2\). Its support-map transposes coincide with CDI4–CDI5: anti-diagonal for the degree-one difference, diagonal for the degree-two sum, and \(-\lambda_++\lambda_-\) for the angular boundary. The weak density passes through \(\kappa'\) because a topological isomorphism induces a weak-dual topological isomorphism.

Finally RD8 retains the correct raw inverse factor \(1/(2\zeta)\), the full trivial-zero derivatives, and both endpoint values. Its expansion of \(A_\rho\) is the Taylor convolution of the complete multiplier in \(F_0\) with \(\zeta(s)/(s-\rho)^m\), so
\(a_j=\sum_{h=0}^j C^{(h)}(\rho)\zeta^{(m+j-h)}(\rho)/(h!(m+j-h)!)\)
is exact. The original local residue uses \(u_\rho\) of \(\zeta\), not this auxiliary multiplier. RD9 keeps the continuous-dual receiver distinct from the not-yet-constructed Deligne support-duality comparison. This matches the exact scope of CDI11.
