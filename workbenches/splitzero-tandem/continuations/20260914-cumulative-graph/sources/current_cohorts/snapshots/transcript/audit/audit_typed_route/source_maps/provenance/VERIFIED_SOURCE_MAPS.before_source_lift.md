# Verified typed maps in the original τ-base construction

This is an independent source-map verification for the transcript continuation audit. It reads the entire primary note and the entire canonical source route. It does not claim to audit the whole shared transcript or the analytic arithmetic estimates. It does not duplicate the homotopy-fibre/right-adjoint continuation assigned elsewhere.

## Source pins and exact scope

1. `output/split_zero_rh_tandem_2026-09-12/sources/Tau_Base_Cohomology_2026-09-12/NOTE.md`, 25,512 bytes, SHA-256 `d03e71ad18f187bd89880cb8ca6fc9c5d6f260b3de8e8e5702c27db97e7b63c3`. All 611 lines read. Equation locators below refer to this body.
2. `work/f1_geometry_current_source_route_20260913.md`, SHA-256 `a8cdd18817a2c3596778c60a04ef9d76125a03ae5404759835a2bc2b18fa4c74`. Entire body read. Its dependencies were not thereby deemed independently reread.
3. `output/split_zero_rh_tandem_2026-09-12/tex/support_diagrams.tex`, SHA-256 `7586ac17247456a55bdacfcf8b46c196c29eafd3b57846a71792e918704e069b`. Entire body read to check the kernel types and support-index transport. Its labels D1–D8 are used below.

The primary note explicitly works in the algebraic category
\[
\mathcal A=\operatorname{Fun}(P,\operatorname{Vect}_{E}),\qquad E=\mathbb C,
\quad +<\eta<\sigma,\quad -<\eta<\sigma.
\]
The topology is the upper-set topology; diagrams are covariant. The calculations below keep that category, its arrows, and its cohomological degrees. The source does not replace the Schwartz topology by a theorem about its continuous dual: it calculates an algebraic right adjoint, and says so.

## 1. The structural map does not perform Boolean localization

Primary equations (2)–(3), lines 33–45, use the blueprint map
\[
\jmath_R:\mathbf F_{1,\tau}=\{\tau,1\}\longrightarrow B_R,
\qquad \jmath_R(\tau)=\tau,\quad\jmath_R(1)=1_R^\bullet.
\]
The only additional additive relation imposed by the source blueprint is that its empty sum represents τ. The target retains that relation, its own addition relations, and its original multiplicative monoid, so the displayed map preserves all source relations. Every proper prime contains τ and excludes the unit. Its inverse image is consequently exactly \(\{\tau\}\). This proves the structural map to the one-point base.

Primary equations (6)–(7), lines 64–80, concern a separate map \(\chi_R:G(R)\to\mathbb B\), with \(\chi_R(\tau)=0\), \(\chi_R(r^\bullet)=1\), and localization at \(e=0_R^\bullet\). Inverting the idempotent e gives e=1; then \(er^\bullet=e\) gives \(r^\bullet=1\). No cancellation with τ occurs. The source already proves this localization, and does not use it as the definition of the structural base pushforward.

The canonical route supplies the exact comparison for every \(G(R)\)-semimodule M:
\[
\Phi:\mathbb B\otimes_{G(R)}M\longrightarrow eM,
\qquad b\otimes m\longmapsto b\cdot em.
\]
Here \(eM\) is a Boolean semimodule under its original addition. For a supported scalar a, \(ea=e\), so both sides of the balancing relation map to \(b\cdot em\); for a=τ both map to the global zero. Additivity in m follows from distributivity of e. Additivity in b uses \(em+em=em\). Its inverse is
\[
\Psi:eM\longrightarrow\mathbb B\otimes_{G(R)}M,
\qquad l\longmapsto1\otimes l.
\]
Indeed \(\Phi\Psi(l)=el=l\), and
\(\Psi\Phi(1\otimes m)=1\otimes em=\chi_R(e)\otimes m=1\otimes m\); tensors with Boolean coefficient 0 vanish. Both formulas commute with every split-linear map. The comparison is therefore a natural isomorphism, not a claimed lack of relation between the two constructions.

## 2. The global pushforward and its canonical derived restriction

Primary equations (17)–(20), lines 200–242, are correct with their displayed domains and signs.

For x in P, \(P_x(y)=E\) when \(x\leq y\), and 0 otherwise, with identity maps on nonzero arrows. A natural transformation \(P_x\to F\) is determined by the image v of 1 at x; at y above x its value must be \(r_{xy}v\). Conversely those values are natural. Thus
\[
\operatorname{Hom}_{\mathcal A}(P_x,F)=F_x.
\]
Evaluation is exact because kernels and cokernels in the diagram category are computed at each point. This proves projectivity of \(P_x\).

The source resolution is
\[
0\longrightarrow P_\eta\xrightarrow{\delta}P_+\oplus P_-
\xrightarrow{\varepsilon}\mathbf E\longrightarrow0,
\quad\delta(v)=(v,-v),\quad\varepsilon(u,v)=u+v.
\]
At + its sequence is \(0\to0\to E\xrightarrow{1}E\to0\), and at − it is the same sequence in the second summand. At η and σ its sequence is \(0\to E\to E^2\to E\to0\), with kernel of addition exactly \(\{(v,-v):v\in E\}\). Restriction maps commute with both displayed maps because each nonzero component is an identity. This checks exactness and naturality on every point and arrow.

Compatible global sections of F are determined by \((u,v)\in F_+\oplus F_-\) with \(r_+u=r_-v\). Their η-value is this common vector and their σ-value is its image under \(r_{\eta\sigma}\). Hence \(\Gamma(P,F)=\operatorname{Hom}(\mathbf E,F)\), and the resolution computes
\[
\mathsf A_\tau(F)=R\Gamma(P,F)\simeq C_F,
\quad C_F^0=F_+\oplus F_-,\quad C_F^1=F_\eta,
\quad d_F(u,v)=r_+u-r_-v.
\]
The convention is the displayed resolution coboundary by precomposition. The degrees and the differential are those of the source, not an identification with \(F_\sigma\).

Put \(r=r_{\eta\sigma}\). The two maps \(c_+,c_-:C_F\to F_\sigma[0]\) have degree-zero parts
\[
c_+^0(u,v)=rr_+u,\qquad c_-^0(u,v)=rr_-v,
\]
and degree-one parts 0. They are chain maps because the target has no term in degree 1. With degree −1 homotopy h defined by \(h^1=r:F_\eta\to F_\sigma\),
\[
(c_+-c_-)^0=h^1d_F,
\qquad (c_+-c_-)^1=0=d_{F_\sigma}h^1.
\]
They therefore give a single canonical derived morphism
\(\operatorname{res}_\sigma:\mathsf A_\tau(F)\to F_\sigma[0]\).
Its action on a global compatible section is its actual σ-value. This proves the comparison, including its sign, without substituting the target for the source.

## 3. The actual arithmetic cohomology and its three support fibres

Primary equations (10)–(15), (21)–(25), retain
\[
V=\{\phi\in\mathcal S(\mathbb R):\phi\text{ even},\ \phi(0)=0,
\ \widehat\phi(0)=0\},\qquad
\widehat\phi(\xi)=\int_{\mathbb R}\phi(x)e^{-2\pi i x\xi}\,dx,
\]
\[
\mathscr B=\left\{F\in C^\infty(\mathbb R_{>0}):
\sup_{x>0}x^b|(-x\partial_x)^kF(x)|<\infty
\text{ for all }b\in\mathbb Z,k\geq0\right\},
\]
\[
\Theta\phi(x)=\sum_{n\ne0}\phi(nx),\quad
JF(x)=x^{-1}F(1/x),\quad J\Theta=\Theta\mathcal F.
\]
Its joint diagram is \((V,V,\mathscr B,0)\), with differential
\[
d(\phi,\psi)=\Theta\phi-J\Theta\psi
=\Theta(\phi-\widehat\psi).
\]
Consequently its image is exactly \(\Theta V\): one inclusion follows from Fourier invariance of V, and the reverse inclusion follows by using \((\phi,0)\). Fourier invariance follows from evenness and \(\mathcal F^2\phi(x)=\phi(-x)\), which exchanges the two vanishing moments and gives \(\mathcal F^2=1\) on V. Using the source's established injectivity of Θ gives
\[
\ker d=\{(\widehat\psi,\psi):\psi\in V\},\qquad
H^1C_{\mathcal T}=Q=\mathscr B/\Theta V.
\]
This verifier does not replace the source's Mellin/Poisson proof of injectivity by an independent analytic claim. The algebraic identification just made uses that named source result at its exact place.

For the + singleton mask the differential is Θ. For the − singleton mask it is \(-J\Theta=-\Theta\mathcal F\). Each is injective, and each has image \(\Theta V\), so its \(H^0\) is 0 and its \(H^1\) is Q. The inclusions from either singleton to the joint mask are coordinate inclusions in degree 0 and identity in degree 1; they are chain maps since the joint differential restricts to the indicated signed singleton differential. Their induced \(H^1\) maps are the identity of Q. The empty support diagram is zero.

Thus the entire \(H^1\) support diagram has zero bottom fibre and Q at all three nonempty masks, with identity transitions among nonempty comparable masks. Its reconstruction is exactly
\[
M=\widetilde H^1_\tau
=\{\tau\}\sqcup\coprod_{\varnothing\ne A\subseteq\{+,-\}}\{A\}\times Q.
\]
The linear map induced by \(\operatorname{res}_\sigma\) on \(H^1\) is \(Q\to H^1(0[0])=0\) at each nonempty mask. Reconstructing that same-mask diagram map gives
\[
\epsilon_M:M\longrightarrow eM,
\quad\tau\longmapsto\tau,\quad(A,q)\longmapsto(A,0).
\]
This is the precise typed reading of the source's statement immediately after (25), at lines 283–288. It is not a degree-one map to the unshifted linear stalk treated as if that stalk had nonzero \(H^1\). The supported skeleton is obtained by the explicit support reconstruction. Its fibres are
\[
\epsilon_M^{-1}(\tau)=\{\tau\},\qquad
\epsilon_M^{-1}(A,0)=\{A\}\times Q\quad(A\ne\varnothing).
\]
Every arithmetic amplitude remains in its recorded fibre. The projection and its section \((A,0)\mapsto(A,0)\) prove the relation to the boundary skeleton exactly.

## 4. The right adjoint is computed algebraically on that same chart

Primary equations (26)–(30), lines 294–347, give the correct right-adjoint object.

Define \(I_x(W)(y)=W\) if \(y\leq x\) and 0 otherwise. A map \(F\to I_x(W)\) is uniquely determined by \(\ell:F_x\to W\): its y-component for \(y\leq x\) is \(\ell r_{yx}\), and its other components are 0. These components are natural on every arrow. Therefore
\[
\operatorname{Hom}_{\mathcal A}(F,I_x(W))=\operatorname{Hom}_E(F_x,W).
\]
Every vector space is injective: a linear map defined on a subspace extends after extending a basis of that subspace to a basis of the whole space. Evaluation at x is exact, so \(I_x(W)\) is injective in \(\mathcal A\).

The source complex is
\[
K_\tau(W)^{-1}=I_\eta(W),\quad
K_\tau(W)^0=I_+(W)\oplus I_-(W),\quad
d_K=(+\mathrm{res},-\mathrm{res}).
\]
A bounded complex of injectives calculates the derived Hom from a sheaf here. Evaluation of its Hom complex gives
\[
R\operatorname{Hom}_{\mathcal A}(F,K_\tau(W))
=\left[\operatorname{Hom}_E(F_\eta,W)
\xrightarrow{\ell\mapsto(\ell r_+,-\ell r_-)}
\operatorname{Hom}_E(F_+,W)\oplus\operatorname{Hom}_E(F_-,W)\right],
\]
in degrees −1 and 0. The ordinary Hom complex from \(C_F\) to \(W[0]\) has exactly these terms. For a degree −1 map ℓ its differential is \(-(-1)^{-1}\ell d_F=\ell d_F\), giving exactly the displayed pair. This proves the chain isomorphism in (28), naturally in F and W, and hence the stated adjunction.

For bounded coefficient complexes the same result follows by taking the finite total complexes, preserving the original differential of W. An explicit convention is
\[
K_\tau(W)^n=I_\eta(W^{n+1})\oplus I_+(W^n)\oplus I_-(W^n),
\quad d(s,u,v)=(-d_Ws,\ \mathrm{res}_+s+d_Wu,
\ -\mathrm{res}_-s+d_Wv).
\]
Its square is zero: the first component is \(d_W^2s\), and each other component cancels its two restriction-of-\(d_Ws\) terms, leaving \(d_W^2u\) or \(d_W^2v\). This is the signed totalization of the displayed two-term adjoint.

At +, −, η, σ, respectively, the W-vector-space stalk complexes are
\[
[W\xrightarrow{1}W],\quad[W\xrightarrow{-1}W],\quad W[1],\quad0.
\]
The inclusion \(S_\eta W[1]\to K_\tau(W)\), identity at η and zero at the other points, is natural: at each arrow entering η its source is zero; at arrows leaving η its target is zero; all other squares have a zero entry on the source side. It induces an isomorphism in cohomology at every stalk, since the ± complexes have invertible differentials. Hence
\[
K_\tau(W)\simeq S_\eta W[1]
\]
by an explicit quasi-isomorphism. In particular \(K_\tau(W)_\sigma=0\) does not imply that the right adjoint is zero, nor that its Hom from the arithmetic sheaf is zero. Its degree −1 Hom cohomology is
\[
\{\ell:\mathscr B\to W:\ell\Theta V=0\}
\cong\operatorname{Hom}_E(Q,W).
\]
The inverse correspondence sends a quotient functional \(\lambda:Q\to W\) to \(\lambda\circ q\); the forward correspondence sends ℓ to \([F]\mapsto\ell(F)\). Equality of values on representatives is exactly \(\ell\Theta V=0\).

This verifies the target of the full finite-jet/residue morphism (43), whose source has been retained as \(\overline{A_Z}\) and whose codomain is \(H^{-1}R\operatorname{Hom}_{\mathcal A}(\mathcal T,K_\tau(\mathcal L_1))\). The source's surjective \(J_Z:Q\to A_Z\) and perfect finite residue pairing are the specified reasons its precomposition map is injective. Neither a continuous-dual identification nor involutive Verdier duality is supplied by this algebraic adjunction.

## 5. Exact categorical and all-support kernels

Use D1–D8 with \(M=\mathcal T(L,V)\), \(N=\mathcal T(L',W)\), and a split-linear map
\[
F=\mathcal T(\alpha,f),\qquad F(l,x)=(\alpha(l),f_lx).
\]
The target's global zero is \((\bot',0)\), while its support skeleton consists of all \((k,0)\). Consequently
\[
F(l,x)=0_N\iff \alpha(l)=\bot'\text{ and }f_lx=0,
\]
\[
F(l,x)\in eN\iff f_lx=0.
\]
Writing \(L_0=\alpha^{-1}(\bot')\), these equalities give
\[
\ker_{G(R)}F=\mathcal T(L_0,(\ker f_l)_{l\in L_0}),
\]
\[
F^{-1}(eN)=\mathcal T(L,(\ker f_l)_{l\in L})
=M\times_N eN.
\]
The original transition maps restrict to these kernels: naturality gives \(f_k\rho_{lk}x=\rho'_{\alpha(l),\alpha(k)}f_lx=0\). Also \(L_0\) is closed under joins because α preserves joins. Therefore both displayed carriers are subsemimodules. Any map with the corresponding vanishing property has its image in the indicated carrier and hence factors uniquely through the inclusion. This proves the two universal properties, not just set identities. Their exact comparison is the inclusion induced by \(L_0\hookrightarrow L\).

For \(\epsilon_M\) above, α is the identity and every fibre map is the zero map \(Q\to0\). Its bottom fibre is zero. Thus
\[
\ker_{G(E)}\epsilon_M=\{\tau\},\qquad
M\times_{eM}eM=M.
\]
A trivial categorical kernel here cannot establish disappearance of supported arithmetic cohomology: the second displayed object is the entire original arithmetic carrier. The formula states the scope of the trivial-kernel result exactly.

The quotient q at a fixed nonempty mask has source \(\mathscr B\), boundary subspace \(\Theta V\), and target Q. Its supported form sends \((A,F)\) to \((A,[F])\). In the all-support sense its kernel fibre is \(\Theta V\), while every boundary maps to \((A,0)\), never τ. This follows from \([F]=0\iff F\in\Theta V\). More generally, a cochain map has
\[
\ker H(f)=\{z\in\ker d_C:fz\in\operatorname{im}d_D\}/\operatorname{im}d_C.
\]
The map sends the class of z to its cohomology class. It is well-defined because boundaries map to boundaries, onto because every cohomology class has a cycle representative, and injective because the zero class is precisely a boundary. This is D7, and reconstructing it at every label gives the all-support object in D8.

## 6. Dual support arrows: the exact reversal and its limit

Primary equation (31), lines 349–356, retains the correct map for every inclusion \(A\subseteq B\):
\[
\rho_{AB}^{\vee}:\operatorname{Hom}_E(H_B,W)
\longrightarrow\operatorname{Hom}_E(H_A,W),\quad
\ell\longmapsto\ell\rho_{AB}.
\]
For \(A\subseteq B\subseteq C\),
\(\rho_{AB}^{\vee}(\rho_{BC}^{\vee}\ell)=\ell\rho_{BC}\rho_{AB}=\ell\rho_{AC}\), proving functoriality on \(L^{\mathrm{op}}\). The identity arrow acts as the identity. Thus the exact dual-index diagram exists.

It is not a covariant diagram on the original inclusion-ordered L with the same arrow directions. The source does not assert that it is. A further reconstruction into split semimodules must declare its index semilattice. For the finite Boolean lattice in this source, \(L^{\mathrm{op}}\) itself has join given by intersection and bottom \(\{+,-\}\). Applying D1–D5 to this opposite lattice is valid and keeps the dual arrows, but its bottom fibre is then \(\operatorname{Hom}_E(H_{\{+,-\}},W)\), not the original empty-mask fibre. In degree 1 this is \(\operatorname{Hom}_E(Q,W)\). D1–D5 explicitly allow such nonzero bottom fibres. Thus an argument that applies a theorem requiring a singleton bottom fibre to this reconstructed dual has changed a hypothesis and must calculate the actual bottom fibre. The original dual map (43), formed label by label with precomposition, does not require that unsupported identification.

## 7. A completed exact jet map that makes the eigenline wording precise

Primary (40), (44)–(45), and (49) retain full nilpotent jets. The phrase “residue-value eigenvector” in (49) is read through the following exact maps, so it does not discard the nilpotents of (40).

At an actual zero ρ of multiplicity m, keep the original coordinate \(z=s-\rho\) and factor
\[
g(\rho+z)=u(z)z^m,\qquad u(0)\ne0.
\]
Then \(A_\rho=\mathcal O_\rho/(g)=\mathcal O_\rho/(z^m)\), with the identity on germs giving the latter equality of ideals because u is a unit. Its reduction map is
\[
q_\rho:A_\rho\longrightarrow E,\qquad [h]\longmapsto h(\rho).
\]
The endomorphism \(J_g\) of (44) factors as an actual quotient followed by an injection:
\[
A_\rho\xrightarrow{q_\rho}E\xrightarrow{t_\rho}A_\rho,
\quad t_\rho(c)=c[g'],\qquad J_g=t_\rho q_\rho.
\]
Indeed
\[
g'=u'(z)z^m+m u(z)z^{m-1}
\equiv m u(0)z^{m-1}\pmod{z^m}.
\]
Writing \(h=h(0)+z\widetilde h\), multiplication by \([g']\) kills the second summand, so \([g'h]=h(0)[g']\), proving factorization. Since \(m u(0)\ne0\), \([g']\ne0\); therefore \(t_\rho\) is injective. Its image is exactly
\[
\operatorname{Ann}_{A_\rho}(z)=E z^{m-1}.
\]
To verify this equality, multiply \(\sum_{j=0}^{m-1}c_jz^j\) by z. The product is zero modulo \(z^m\) exactly when \(c_0=\cdots=c_{m-2}=0\). This includes m=1, when the annihilator is all of \(A_\rho=E\). Consequently
\[
\ker J_g=\ker q_\rho=zA_\rho,
\qquad\operatorname{im}J_g=\operatorname{Ann}_{A_\rho}(z).
\]

The actual scaling operator remains
\[
U_a=a^\rho\sum_{j=0}^{m-1}\frac{(\log a)^j}{j!}N^j,
\qquad N[z^j]=[z^{j+1}],\qquad a>0.
\]
Reduction gives \(q_\rho U_a=a^\rho q_\rho\), since every j>0 term has zero constant coefficient. Multiplication of \(t_\rho(c)\), which lies in \(Ez^{m-1}\), by a j>0 term is zero, so \(U_at_\rho(c)=t_\rho(a^\rho c)\). Both maps are equivariant. Thus the residue-value representation and its socle image inside the full jet are linked by the explicit nonzero map \(t_\rho\). When \(m>1\), the constant lift 1 of a residue value is not generally an eigenvector of \(U_a\) for \(a\ne1\), because its z coefficient is \(a^\rho\log a\ne0\). The socle image \(t_\rho(1)\) is an actual eigenvector. No full jet was replaced by its reduction in proving that fact.

The tensor of r copies of this explicit eigenvector is nonzero in \(A_\rho^{\otimes_E r}\): the coefficient of \((z^{m-1})^{\otimes r}\) is \((m u(0))^r\ne0\). Its action on that finite tensor quotient is exactly \(a^{r\rho}\). Its precise relation to primary (47) is the equivariant surjection
\[
Q^{\otimes_E r}\xrightarrow{(\operatorname{pr}_\rho J_Z)^{\otimes r}}
A_\rho^{\otimes_E r}.
\]
Here \(Z\) contains ρ, \(J_Z:Q\to A_Z\) is the source's full jet quotient, and \(\operatorname{pr}_\rho\) is its block projection. Each map is equivariant by the full jet scaling formula (40). The first is surjective by the source's jet-surjectivity result, the block projection is surjective, and their tensor is surjective because each simple target tensor has a tensor of preimages and such tensors span the target. This proves the exact relation to \(Q^{\otimes r}\).

The construction here does not provide an equivariant lift of the socle eigenline to Q or of its tensor to \(Q^{\otimes r}\). A linear section of the jet quotient would not establish such a lift without an equivariance calculation. Accordingly, wording of primary (49) that is read as asserting an eigenvector inside \(Q^{\otimes r}\) requires that additional map; the completed calculation in this report establishes the eigenvector in the explicitly named finite quotient. On this quotient the tensor modulus expression is
\[
\log\frac{|a^{r\rho}|^2}{a^r}=r(2\operatorname{Re}\rho-1)\log a
\qquad(a>1),
\]
with its original action and coefficient line. This is an identity on the actual eigenline embedded in \(A_\rho^{\otimes r}\), which is a quotient of the tensor cohomology in (47); it proves no upper bound on that identity. At every nonempty supported mask, \(q_\rho\), \(t_\rho\), and \(J_g\) lift by retaining the mask, so a killed nilpotent maps to the supported zero of its mask.

## Audit uses

The source already contains the structural base, global pushforward, derived restriction, right adjoint, full supported Q, dual-index arrows, and the finite-jet morphism into that right adjoint. A passage that calls any of these missing must be tested against the equation locators above. The algebraic calculation does not supply analytic bounds; that limitation has the exact scope stated in the primary note. A boundary-stalk vanishing or a trivial categorical kernel does not reach the original supported Q, because the explicit maps above retain the whole Q fibre. A duality argument must retain the dual arrow direction, its coefficient line, and its actual algebraic category. A tensor argument can use the exact socle embedding into the finite tensor quotient above while retaining every nilpotent in that ambient jet object; it must retain the displayed quotient map from the full tensor cohomology and may not infer a source eigenvector from this quotient eigenvector.
