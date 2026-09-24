# The complete continuous dual of the actual supported coefficient complex

24 September 2026. Independent calculation ASD0–ASD14. All duals below are continuous duals of the original coefficient topologies. The proved comparison retains the original supported quotient, its full multiplicity jets, the four original endpoint lines, and both complete extra closed coefficient copies.

## ASD0. Controlling definitions, mathematical source, and scope

The source definitions are B1–B5 and their proved consequences P1–P5 in [SOURCE_OPERATIONS_AND_PROOFS.md](../foundations/user_definitions_20260924/SOURCE_OPERATIONS_AND_PROOFS.md), with the user's verbatim U01–U18 in USER_DEFINITIONS_VERBATIM.md (private construction record; not included). The current CORPUS_AND_OPERATION_RULES.md (private construction record; not included) was read. Before interpreting the pairing calculation below, the complete corpus passages USR-9ad1c0a2d09dba92, USR-f55d16feb948d8c2, and USR-6152e3bc6302258c were reread in its retained private record. They supply the user's full-system argument and the requested global quotient and Deligne comparison; they are not replaced by a truncated prime system.

The source remains \(Z_0\) absence, primitive \(Z_1/\tau\) without parity or source addition, and the original integer layer with the user's specified \(Z_2\) data. Source zero has no source parity. Every sum, integral, scalar, continuous functional, or complex below is an operation in an already constructed receiving space after the retained global arithmetic reconstruction. No dualization creates source addition on \(\tau\).

The human geometric source is Alain Connes and Caterina Consani, [*Schemes over \(\mathbb F_1\) and zeta functions*, arXiv:0903.2024v3, §5](https://arxiv.org/abs/0903.2024v3). Its original author TeX, announc3.tex lines1376–1667, was read in the earlier DCP calculation; it supplies the two charts, restriction, Fourier identity, and mirror. The exact source-space entry and faithful coefficient extension were proved in [SOURCE_CC_DOUBLE_PULLBACK.md](SOURCE_CC_DOUBLE_PULLBACK.md), DCP0–DCP12.

The analytic inputs are the original-space closed-image and inverse theorems in [ORIGINAL_MELLIN_SPECTRAL_SYNTHESIS.md](ORIGINAL_MELLIN_SPECTRAL_SYNTHESIS.md), OMS1–OMS5, and SSI0–SSI10 cited there. Their human analytic source is Ralf Meyer, [*A spectral interpretation for the zeros of the Riemann zeta function*, arXiv:math/0412277v3](https://arxiv.org/abs/math/0412277v3), with his exact source and reading coverage recorded in OMS0. The present note uses the actual proved image equality, not an assumed spectral synthesis statement.

[COMPLETE_COMPARISON_TRIANGLE_FORMALITY.md](COMPLETE_COMPARISON_TRIANGLE_FORMALITY.md), CTF0–CTF8, was read, including its distinction between the algebraic full adelic complex and the Fréchet CC complex. The latter, not an unstated topology on the former, is continuously dualized here. The existing reflected Weil form in [the retained complete ORIGINAL_ZETA_RESOLVENT_AND_PROJECTORS.md](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/gct-weight-control/proofs/ORIGINAL_ZETA_RESOLVENT_AND_PROJECTORS.md), RZ10–RZ11, was also read in full and is retained in ASD11. The external programme file actually read and this retained copy were verified byte-identical: SHA256 f3553e1362b4c2c1c1556098b55ee153be9fc716a9d4c35baedcf39bd28ad755.

Pierre Deligne's [*La conjecture de Weil. II*, §3.6, printed pp.212–214](https://www.numdam.org/item/PMIHES_1980__52__137_0/), is the human source of the target supported-cohomology argument. The local reading for this calculation was the explicitly identified transcription sources/S20_FR_record_export.tex, lines2466–2559, not an author TeX file. Section3.6.1(6)–(8) uses a genuine perfect duality with a Tate twist to identify its supported group; Lemmas3.6.2 and3.6.3 then give separate weight bounds. ASD13 compares the actual morphisms below to that mechanism without declaring an unproved Verdier duality.

## ASD1. Original spaces and all original factors

Set
\[
 S=\{h\in\mathcal S(\mathbb R;\mathbb C):
 h(-v)=h(v),\ h(0)=0,\ \int_{\mathbb R}h(v)\,dv=0\},
\]
\[
 A=\{b\in C^\infty(\mathbb R_{>0};\mathbb C):
 p_{N,j}(b)=\sup_{u>0}(u^N+u^{-N})
 |(u\partial_u)^jb(u)|<\infty\quad(N,j\ge0)\}.
 \tag{ASD1.1}
\]
These are the original Fréchet spaces; \(S\) has its closed-subspace Schwartz topology and \(A\) its displayed seminorms. The two labelled chart spaces are
\[
 V_+=S\oplus\mathbb C^2_{c_0,c_1},\qquad
 V_-=S\oplus\mathbb C^2_{d_0,d_1}.
\]
Keep
\[
 \Sigma h(u)=2\sum_{n\ge1}h(nu),\qquad
 Rb(u)=u^{-1}b(u^{-1}),\qquad
 \widehat h(t)=\int_{\mathbb R}h(v)e^{-2\pi ivt}\,dv ,
 \tag{ASD1.2}
\]
\[
 r_+(h,c_0,c_1)=\Sigma h,\qquad
 r_-(h,d_0,d_1)=R\Sigma h=\Sigma\widehat h.
 \tag{ASD1.3}
\]
The last equality follows from the complete Poisson identity
\[
 \Sigma\widehat h(u)=u^{-1}\Sigma h(u^{-1})
       +u^{-1}h(0)-\int_{\mathbb R}h(v)\,dv.
 \tag{ASD1.4}
\]
Its two last terms vanish on this explicitly specified \(S\); the separate endpoint lines are still retained.

Write
\[
 J=\Sigma S,\qquad \pi:A\longrightarrow Q=A/J .
 \tag{ASD1.5}
\]
The cited inverse-source theorem proves that \(J\) is closed and \(\Sigma:S\to J\) is a topological isomorphism. In particular \(Q\) is Hausdorff Fréchet, and \(\pi\) is an open quotient map: for open \(O\subset A\), \(\pi^{-1}\pi(O)=O+J\) is open.

For the entire Mellin space \(\mathcal B\) in OMS1.2, retain
\[
 \mathcal M_0b(s)=\int_0^\infty b(u)u^s\,\frac{du}{u},\qquad
 \mathcal M_0\Sigma h(s)=
 2\zeta(s)\int_0^\infty h(v)v^s\,\frac{dv}{v}.
 \tag{ASD1.6}
\]
The latter identity is initially absolute on \(\Re s>1\); its continuation, endpoint terms, and original trivial-zero residues are those proved in SSI/OMS. The exact topological identification is
\[
 Q\simeq\mathcal B/I_\zeta,\qquad
 I_\zeta=\{F:F^{(r)}(\rho)=0\
 (\rho\text{ an actual nontrivial zero of }\zeta,\ 0\le r<m_\rho)\}.
 \tag{ASD1.7}
\]
This uses the original \(\zeta\) and actual multiplicities.

The previous centered receiver has not been silently substituted:
\[
 \mathcal T k(u)=2u^{-1/2}k(u),\qquad
 \mathcal T^{-1}b(u)=\tfrac12u^{1/2}b(u),\qquad
 \mathcal M_0\mathcal Tk=2F_k,\qquad \Sigma=\mathcal T\mathcal E.
 \tag{ASD1.8}
\]
Every dual comparison uses the transpose of this same map, including its factor2 and half-power.

## ASD2. Continuous duals, quotient exactness, and the precise topology

For a Hausdorff locally convex complex space \(E\), let \(E'\) be its continuous complex-linear dual. Unless a stronger topology is explicitly named, give \(E'\) the weak-* topology \(\sigma(E',E)\). This is a topology on the dual of the original space, not a change to the original topology on \(E\). For continuous \(T:E\to F\), define
\[
 T':F'\to E',\qquad T'\lambda=\lambda\circ T.
 \tag{ASD2.1}
\]
It is weak-* continuous because evaluation at \(e\) becomes evaluation at \(Te\). It is also continuous for the strong dual topologies: for a bounded set \(B\subset E\),
\[
 \sup_{e\in B}|T'\lambda(e)|
 =\sup_{f\in T(B)}|\lambda(f)|,
 \tag{ASD2.2}
\]
and \(T(B)\) is bounded. Thus every transpose constructed below is strong-dual continuous as well.

Here is the exact quotient fact used in all subsequent rows. For a closed linear subspace \(J\subset E\) with its subspace topology and quotient \(q:E\to E/J\),
\[
 0\longrightarrow(E/J)'
 \xrightarrow{q'}E'\xrightarrow{\operatorname{res}}J'
 \longrightarrow0
 \tag{ASD2.3}
\]
is algebraically exact and strictly exact for weak-* topologies.

Indeed \(q'\) is injective. Its image is precisely
\(J^\perp=\{\lambda\in E':\lambda(J)=0\}\): an annihilating functional factors uniquely through \(E/J\), and the factor is continuous by the quotient topology. The weak-* topology on this image agrees with \(\sigma((E/J)',E/J)\), since each quotient vector has a representative in \(E\). The annihilator is weak-* closed. Every continuous functional on \(J\) extends continuously to \(E\) by the complex Hahn–Banach theorem, proving surjectivity of restriction.

For completeness, restriction is an open map in these weak-* topologies. Let \(O\) be a basic zero-neighbourhood in \(E'\), specified by inequalities on a finite-dimensional subspace \(F\subset E\). The image of \(O\) under restriction is exactly the set of \(\psi\in J'\) whose restriction to \(F\cap J\) extends to a functional \(\ell\in F^*\) satisfying those inequalities. The restriction map \(F^*\to(F\cap J)^*\) is a surjective finite-dimensional linear map, hence open; this makes that set weak-* open in \(J'\). To justify the asserted equality, start with a continuous Hahn–Banach extension \(\lambda_0\) of \(\psi\). The difference \(\ell-\lambda_0|_F\) vanishes on \(F\cap J\), so it is a functional on the finite-dimensional image of \(F\) in the Hausdorff locally convex quotient \(E/J\). It is continuous there and has a continuous Hahn–Banach extension to \(E/J\). Add its pullback to \(\lambda_0\). The resulting extension has restriction \(\psi\) and the prescribed \(F\)-values. This proves the equality and openness.

No strong-dual quotient or completeness conclusion is silently substituted for ASD2.3. The statements proved here are strict weak-* exactness, algebraic exactness of continuous duals, and strong continuity of each displayed transpose. Where a row has an explicit continuous splitting, its dual splitting is also strong continuous, directly by ASD2.2.

Applied to ASD1.5, this gives the full spectral dual
\[
 \boxed{Q'\xrightarrow[\pi']{\ \sim\ }J^\perp\subset A'.}
 \tag{ASD2.4}
\]
It contains every continuous distribution on the original strong test space that annihilates the exact summation image. It is not restricted to finite sums of zero evaluations.

## ASD3. The entire faithful CC complex and its dual differential

Use the order \(+\), then \(-\). The original cochain complex is
\[
 D^0=V_+\oplus V_-,\qquad D^1=A,\qquad
 d_D(v_+,v_-)=r_+v_+-r_-v_-.
 \tag{ASD3.1}
\]
Let
\[
 V_{\rm extra}=V_+^{\,{\rm extra}}\oplus V_-^{\,{\rm extra}}.
\]
DCP8 proves the source-faithful coefficient sheaf has the global complex
\[
 D_{\rm full}=D\oplus V_{\rm extra}[0].
 \tag{ASD3.2}
\]
Every extra term is the entire space \(S\oplus\mathbb C^2\), not its endpoint quotient.

The dual cochain convention is
\[
 (C^\vee)^n=(C^{-n})',\qquad
 d_{C^\vee}^{\,n}=(-1)^{n+1}(d_C^{-n-1})'.
 \tag{ASD3.3}
\]
It comes from the Hom differential into \(\mathbb C[0]\), and its square is zero because consecutive original differentials compose to zero. Thus the full dual has exactly degrees \(-1,0\):
\[
 (D_{\rm full}^\vee)^{-1}=A',\qquad
 (D_{\rm full}^\vee)^0=V_+'\oplus V_-'\oplus V_{\rm extra}',
\]
\[
 d^\vee\lambda=(r_+'\lambda,\,-r_-'\lambda,\,0).
 \tag{ASD3.4}
\]
There is no further differential sign: at degree \(-1\) the sign in ASD3.3 is \(+1\). On individual coordinates,
\[
 r_+'\lambda=(\Sigma'\lambda,0,0),\qquad
 r_-'\lambda=(\Sigma'R'\lambda,0,0).
 \tag{ASD3.5}
\]
All dual endpoint coordinates therefore remain independent in degree0.

Parametrize the original degree-zero cohomology using the first Schwartz coordinate:
\[
 H_0=\ker d_D
 =\{((h,c_0,c_1),(\widehat h,d_0,d_1)):h\in S\}
 \simeq S\oplus\mathbb C^4,
\qquad H=H_0\oplus V_{\rm extra}.
 \tag{ASD3.6}
\]
The DCP parametrization by the second coordinate gives the same subspace by Fourier involution; no chart has been discarded. The dual complex satisfies
\[
 \boxed{H^{-1}(D_{\rm full}^\vee)=Q',\qquad
 H^0(D_{\rm full}^\vee)=H',}
 \tag{ASD3.7}
\]
and has no other cohomology.

To prove the first equality, ASD3.4 vanishes exactly when \(\lambda\) annihilates \(J\), giving ASD2.4. For the second, restrict a degree-zero functional to \(H\). Restriction is onto by Hahn–Banach; more explicitly the continuous projection in ASD4 gives a continuous section of this restriction. Its kernel is exactly the image of ASD3.4. If \(\phi\) vanishes on \(H_0\), it factors through \(d_D:D^0\to J\). The factor is continuous: a continuous section of this surjection is \(j\mapsto((\Sigma^{-1}j,0,0),0)\). Extend that functional on \(J\) continuously to \(A\) by Hahn–Banach. Its transpose image is \(\phi\). A functional annihilating \(H\) also vanishes on all extra copies, so the same argument proves the complete assertion.

This identifies cohomology with its weak-* quotient topology. The restriction to \(H\) has an explicit continuous dual section, so its final quotient identification is strong-dual continuous in both directions too; no statement about the strong topology on \(A'/Q'\) is needed.

## ASD4. Exact dual of the already constructed global comparison

CTF2 constructs the continuous cochain map
\[
 \Pi_D^0((h,c),(g,d))
 =\left(\left(\tfrac{h+\widehat g}{2},c\right),
         \left(\tfrac{\widehat h+g}{2},d\right)\right),
 \qquad \Pi_D^1=\pi.
 \tag{ASD4.1}
\]
It takes values in \(H_0[0]\oplus Q[-1]\) and is the identity on cohomology. Its kernel is the exact complex
\[
 \{((h,0),(-\widehat h,0)):h\in S\}
 \xrightarrow{\ d_D\ }J,\qquad h\longmapsto2\Sigma h,
 \tag{ASD4.2}
\]
whose inverse is
\[
 j\longmapsto
 \left(\left(\tfrac12\Sigma^{-1}j,0\right),
       \left(-\tfrac12\widehat{\Sigma^{-1}j},0\right)\right).
 \tag{ASD4.3}
\]
Both factors \(2\) and \(1/2\) remain.

Its exact continuous transpose is a quasi-isomorphism
\[
 \Pi_{D,{\rm full}}^\vee:
 Q'[1]\oplus H_0'[0]\oplus V_{\rm extra}'[0]
 \longrightarrow D_{\rm full}^\vee.
 \tag{ASD4.4}
\]
In degree \(-1\) it is \(\pi'\); in degree0 it is \((\Pi_D^0)'\) together with identity on \(V_{\rm extra}'\). A functional \(\alpha=(u,\alpha_0,\alpha_1,\beta_0,\beta_1)\) on the \(S\oplus\mathbb C^4\) coordinates of \(H_0\) is sent to
\[
 (\Pi_D^0)'\alpha
 =
 \left(
  (\tfrac12u,\alpha_0,\alpha_1),\
  (\tfrac12\widehat{\phantom h}'u,\beta_0,\beta_1)
 \right),
 \quad
 (\widehat{\phantom h}'u)(g)=u(\widehat g).
 \tag{ASD4.5}
\]
Substitution in ASD4.1 proves this formula. The degree-zero restriction back to \(H_0'\) is identity. The degree \(-1\) image is exactly ASD2.4. These facts prove the quasi-isomorphism directly.

Equivalently, dualize the degreewise exact sequence with kernel ASD4.2. Hahn–Banach makes each dual restriction onto. Its last complex is the transpose of the topological isomorphism \(2\Sigma\), and is exact. This gives another complete proof of ASD4.4 without an asserted section \(Q\to A\).

The extra identity cone in CTF7 has \(V_{\rm extra}\) in degrees \(-1,0\), with differential \(+\mathrm{id}\). Its dual therefore has \(V_{\rm extra}'\) in degrees \(0,1\), with differential \(-\mathrm{id}\). Its contracting map from degree1 to degree0 is \(-\mathrm{id}\), since both \(dh\) and \(hd\) are identity on their respective degrees. This contracts only the dual of the extra identity comparison cone. It does not remove \(V_{\rm extra}'[0]\) from ASD3.2–ASD3.7.

The full adelic exterior complex in CTF is explicitly algebraic. No continuous dual of its infinite direct sums is asserted without a chosen topology. ASD4.4 is the actual continuous CC-side comparison, and the transpose of ASD1.8 is
\[
 \mathcal T'\lambda(k)=\lambda(2u^{-1/2}k(u)),
 \qquad
 (\mathcal T^{-1})'\mu(b)=\mu(\tfrac12u^{1/2}b(u)).
 \tag{ASD4.6}
\]
They are continuous inverse maps and restrict to the corresponding annihilators by \(\mathcal T(\mathcal ES)=J\). Thus the same original spectral quotient is retained in the continuous comparison.

## ASD5. Single-support and both-support duals, with all signs

For either closed source point, the faithful single-support complex is
\[
 K_{\pm,{\rm full}}=[V_\pm\oplus V_\pm^{\,{\rm extra}}
       \xrightarrow{(v,w)\mapsto r_\pm v}A]
 \quad\text{in degrees }0,1.
 \tag{ASD5.1}
\]
Its dual is
\[
 [A'\xrightarrow{\lambda\mapsto(r_\pm'\lambda,0)}
       V_\pm'\oplus(V_\pm^{\,{\rm extra}})']
 \quad\text{in degrees }-1,0.
 \tag{ASD5.2}
\]
The same annihilator and Hahn–Banach argument gives
\[
 H^{-1}(K_{\pm,{\rm full}}^\vee)=Q',\qquad
 H^0(K_{\pm,{\rm full}}^\vee)
 =(\mathbb C^2)' \oplus(V_\pm^{\,{\rm extra}})'.
 \tag{ASD5.3}
\]
Here the first summand consists of the corresponding labelled endpoint duals.

The primal plus-support map to \(D_{\rm full}\) is inclusion on its two degree-zero copies and identity on degree1. The minus-support map is the corresponding inclusion on degree0 and minus identity on degree1. Therefore their duals, directed from \(D_{\rm full}^\vee\), are the corresponding projections in degree0, and respectively \(+\mathrm{id}\) and \(-\mathrm{id}\) in degree \(-1\). These signs make the differential squares commute by direct substitution in ASD3.4 and ASD5.2.

For both closed points the faithful supported complex is
\[
 K_{\rm full}^0=V_+\oplus V_-\oplus V_{\rm extra},\qquad
 K_{\rm full}^1=A\oplus A,
\]
\[
 d_K(v_+,v_-,w)=(r_+v_+,r_-v_-).
 \tag{ASD5.4}
\]
Its dual is
\[
 (K_{\rm full}^\vee)^{-1}=A'\oplus A',\qquad
 (K_{\rm full}^\vee)^0=V_+'\oplus V_-'\oplus V_{\rm extra}',
\]
\[
 d_K^\vee(\lambda_+,\lambda_-)
 =(r_+'\lambda_+,r_-'\lambda_-,0).
 \tag{ASD5.5}
\]
Consequently
\[
 H^{-1}(K_{\rm full}^\vee)=Q'\oplus Q',\qquad
 H^0(K_{\rm full}^\vee)
 =(\mathbb C^4\oplus V_{\rm extra})'.
 \tag{ASD5.6}
\]
The supported-to-global map \(K_{\rm full}\to D_{\rm full}\) is identity in degree0 and \((b_+,b_-)\mapsto b_+-b_-\) in degree1. Its dual is identity in degree0 and
\[
 \lambda\longmapsto(\lambda,-\lambda)
 \tag{ASD5.7}
\]
in degree \(-1\). In particular the dual signs are determined by the original Cech orientation rather than chosen to improve a weight statement.

## ASD6. The complete continuous-dual localization row

Put \(E=\mathbb C^4\oplus V_{\rm extra}\). The actual primal localization row from DCP7 and DCP9 is
\[
 0\to E\xrightarrow{\iota}H\xrightarrow{\operatorname{res}}A
 \xrightarrow{\partial}Q\oplus Q\xrightarrow{\delta}Q\to0,
 \tag{ASD6.1}
\]
where, using ASD3.6,
\[
 \operatorname{res}(h,c_0,c_1,d_0,d_1,w)=\Sigma h,\qquad
 \partial b=(\pi b,\pi b),\qquad
 \delta(q_+,q_-)=q_+-q_-.
 \tag{ASD6.2}
\]
Its dual is the exact reversed row
\[
 \boxed{
 0\to Q'\xrightarrow{\delta'}Q'\oplus Q'
 \xrightarrow{\partial'}A'
 \xrightarrow{\operatorname{res}'}H'
 \xrightarrow{\iota'}E'\to0,
 }
 \tag{ASD6.3}
\]
with every map explicit:
\[
 \delta'\lambda=(\lambda,-\lambda),\qquad
 \partial'(\lambda_+,\lambda_-)=\pi'(\lambda_++\lambda_-),
\]
\[
 \operatorname{res}'\lambda=(\Sigma'\lambda,0,0,0,0,0),
 \qquad
 \iota'(u,c_0',c_1',d_0',d_1',w')
 =(c_0',c_1',d_0',d_1',w').
 \tag{ASD6.4}
\]
For example, the kernel of \(\partial'\) is the anti-diagonal because \(\pi'\) is injective. The image of \(\partial'\) is \(J^\perp\), which is the kernel of \(\Sigma'\). Hahn–Banach and the topological isomorphism \(\Sigma:S\to J\) prove that \(\Sigma':A'\to S'\) is onto. This identifies the image of \(\operatorname{res}'\) with the kernel of \(\iota'\). Finally \(\iota'\) is onto and split by appending zero in its \(S'\) coordinate.

All kernels are weak-* closed and all maps onto their images have the quotient topology, by ASD2 and the explicitly split finite-coordinate maps. Thus ASD6.3 is a strictly exact row in the declared weak-* category, not only a sequence of abstract dual vector spaces. Each map is also strong-dual continuous.

The condensed spectral part is the completely split row
\[
 0\to Q'\xrightarrow{\lambda\mapsto(\lambda,-\lambda)}
 Q'\oplus Q'\xrightarrow{(\lambda_+,\lambda_-)\mapsto\lambda_++\lambda_-}
 Q'\to0.
 \tag{ASD6.5}
\]
A section of its last arrow is \(\lambda\mapsto(\lambda/2,\lambda/2)\).
A retraction of its first arrow is
\((\lambda_+,\lambda_-)\mapsto(\lambda_+-\lambda_-)/2\).
All four constants and signs are retained. These are precisely the transposes of the primal half-sum retraction and half-difference section.

A functional therefore lifts from either spectral summand through the dual row exactly as these maps prescribe. This row does not annihilate \(Q'\): its first arrow is injective and the displayed quotient is again the same \(Q'\).

## ASD7. Source actions, prime actions, and the complete mirror

The receiving ring is the actual global \(\mathbb Z^3\) of DCP1:
\[
 \epsilon=(1,0,0),\quad e_+=(0,1,0),\quad e_-=(0,0,1).
\]
The source action is
\[
 [\tau]=(1,1,1),\qquad[n]=(n,0,0)=n\epsilon .
 \tag{ASD7.1}
\]
On the original \(D\) and on \(Q\), \((r,b_+,b_-)\) acts by \(r\); on the two extra copies it acts respectively by \(b_+\) and \(b_-\). On continuous duals define the receiving-ring action by transpose:
\[
 (c\lambda)(v)=\lambda(cv).
 \tag{ASD7.2}
\]
The ring is commutative, so this is a left module action: \(c_1(c_2\lambda)(v)=\lambda(c_2c_1v)\). It preserves all the supplied source multiplications and integer-input additions. In particular \(\tau\) acts by identity everywhere, and integer \(n\) acts by \(n\) on the original dual component and by zero on each extra dual component. Hahn–Banach separates a nonzero vector of either extra Fréchet space, so those dual copies are nonzero. Thus the full dual action still distinguishes \(\tau\) from integer \(1\), and distinguishes any two integers on the original nonzero components.

This transpose action does not invert a source integer. In particular it does not attempt to invert the source zero.

The separate invertible real dilation action is
\[
 T_ab(u)=b(u/a),\quad
 \rho_+(a)(h,c_0,c_1)=(h(\cdot/a),c_0,ac_1),
\]
\[
 \rho_-(a)(h,d_0,d_1)=(a h(a\cdot),ad_0,d_1),\qquad a>0.
 \tag{ASD7.3}
\]
It commutes with the source action. For this group action the contragredient dual action is
\[
 T_a^\vee=(T_{a^{-1}})',\qquad
 \rho_\pm^\vee(a)=(\rho_\pm(a^{-1}))'.
 \tag{ASD7.4}
\]
It makes evaluation invariant:
\((T_a^\vee\lambda)(T_av)=\lambda(v)\).
At a rational prime the original operator is \(T_p\), with no additional scale removed.

For chart functionals the complete formulas are
\[
 \rho_+^\vee(a)(u,\alpha_0,\alpha_1)
 =\bigl(h\mapsto u(h(a\cdot)),\alpha_0,a^{-1}\alpha_1\bigr),
\]
\[
 \rho_-^\vee(a)(v,\beta_0,\beta_1)
 =\bigl(h\mapsto v(a^{-1}h(\cdot/a)),a^{-1}\beta_0,\beta_1\bigr).
 \tag{ASD7.5}
\]
The original four endpoint characters \(1,a,a,1\) consequently become
\(1,a^{-1},a^{-1},1\) on their dual lines. The extra dual copies carry the same full contragredient actions on both their Schwartz and endpoint coordinates. They have not been reduced to four characters.

The mirror on \(D_{\rm full}\) swaps the chart and extra pairs in degree0 and is \(-R\) in degree1. Its dual therefore swaps the same dual pairs in degree0 and is \(-R'\) in degree \(-1\). On \(K_{\rm full}^\vee\) it swaps chart and extra pairs in degree0 and is
\[
 (\lambda_+,\lambda_-)\longmapsto(R'\lambda_-,R'\lambda_+)
 \tag{ASD7.6}
\]
in degree \(-1\). The ring involution exchanges \(e_+\) and \(e_-\), fixes \(\epsilon\), and hence fixes every source \([n]\) and \([\tau]\). Formula ASD7.2 shows that these dual mirror maps are semilinear for exactly that ring involution.

On ASD6.5 the first \(Q'\) has mirror \(-R'\), the middle has the exchanged \(R'\), and the final \(Q'\) has mirror \(R'\). Thus
\[
 (\lambda,-\lambda)\longmapsto(-R'\lambda,R'\lambda)
   =\delta'(-R'\lambda),
\]
and the sum is sent to \(R'(\lambda_++\lambda_-)\).
The section \((\lambda/2,\lambda/2)\) and retraction
\((\lambda_+-\lambda_-)/2\) are mirror-equivariant with these precise endpoint actions. Their dilation and source equivariance follows directly from the componentwise formulas.

## ASD8. Exactly which character reflection supplies

Let \(\chi\) denote the separately specified numerical character
\(\chi(a)=a\) of the receiving dilation group. The original reflection relation is
\[
 T_aR=aRT_{a^{-1}},\qquad R^2=1.
 \tag{ASD8.1}
\]
For \(b\in A\), both sides of the first equation evaluate to
\(a u^{-1}b(a/u)\). It descends to \(Q\) because \(RJ=J\).

Let \(Q^{\rm inv}\) denote the same topological vector space as \(Q\), with group action \(a\mapsto T_{a^{-1}}\). Then
\[
 R:Q\longrightarrow\chi\otimes Q^{\rm inv}
 \quad\text{is a continuous equivariant isomorphism}.
 \tag{ASD8.2}
\]
Indeed \(RT_a=aT_{a^{-1}}R\), obtained from ASD8.1 by replacing \(a\) by \(a^{-1}\) and rearranging. Its inverse is \(R\) between these specified actions. This is an exact relation to the inverted representation.

On the continuous dual with its contragredient action, transposition gives instead
\[
 T_a^\vee R'=a^{-1}R'T_{a^{-1}}^\vee.
 \tag{ASD8.3}
\]
To verify the order, \(T_a^\vee R'=(RT_{a^{-1}})'\), and
\(RT_{a^{-1}}=a^{-1}T_aR\). Taking transpose yields ASD8.3. Hence
\[
 R':Q'\longrightarrow\chi^{-1}\otimes(Q')^{\rm inv}
 \tag{ASD8.4}
\]
is the corresponding equivariant isomorphism. The Cech orientation multiplies both instances of \(R'\) by \(-1\); it does not change the factor \(a^{-1}\).

ASD8.2 is not a map to \(Q'\); ASD8.4 is not a map from \(Q\). The morphisms between a space and its continuous dual must actually be constructed, as in ASD10–ASD11 below. Merely reversing a prime operator is not taking the continuous dual.

There are three explicitly different operations:
\[
 \begin{array}{c|c}
 \text{operation}&\text{effect on a scalar eigencharacter }a^\rho\\
 \hline
 \text{contragredient continuous dual}&a^{-\rho}\\
 \text{tensor with }\chi&a^{\rho+1}\\
 \text{reflection of the original Mellin coordinate}&a^{1-\rho}.
 \end{array}
 \tag{ASD8.5}
\]
The numerical convention \(w=2\Re\rho\) gives \(-w\), \(w+2\), and \(2-w\), respectively, on such receiving characters. This assigns no weight or parity to primitive \(\tau\).

In geometric-Frobenius notation the scalar at a prime of an actual Tate twist \((-1)\) is \(p\), so its character agrees with \(\chi(p)\). Here \(\chi\otimes Q'\) is a fully defined representation operation. Its equality with a geometric Tate-twisted dualizing object has not been proved by ASD8.1. An even cochain shift, for example \(C^\vee[-2]\), changes degrees but supplies no factor \(a\): by definition
\((C[-2])^n=C^{n-2}\) and its differential sign is unchanged. For the actual complex its groups are
\[
 H^1(D_{\rm full}^\vee[-2])=Q',\qquad
 H^2(D_{\rm full}^\vee[-2])=H',
 \tag{ASD8.6}
\]
whereas \(D_{\rm full}\) has \(H\) in degree0 and \(Q\) in degree1. This displays the degrees before any claimed dualizing identification.

## ASD9. Full multiplicity jets and the entire spectral dual

For every actual nontrivial zero \(\rho\) and \(0\le r<m_\rho\), define
\[
 \ell_{\rho,r}([b])
 =\frac{(\mathcal M_0b)^{(r)}(\rho)}{r!}.
 \tag{ASD9.1}
\]
This is a continuous element of \(Q'\) by ASD1.7 and the quotient topology. Let
\[
 j_\rho(q)=\sum_{r=0}^{m_\rho-1}\ell_{\rho,r}(q)t_\rho^r,\qquad
 A_\rho=\mathbb C[t_\rho]/(t_\rho^{m_\rho}),\quad
 N_\rho v=t_\rho v.
\]
The exact intertwining and its two distinct transpose formulas are
\[
 j_\rho T_a
 =a^\rho\sum_{k=0}^{m_\rho-1}\frac{(\log a)^k}{k!}N_\rho^k j_\rho,
\]
\[
 T_a'\ell_{\rho,r}
 =a^\rho\sum_{k=0}^{r}
       \frac{(\log a)^{r-k}}{(r-k)!}\ell_{\rho,k},
\qquad
 T_a^\vee\ell_{\rho,r}
 =a^{-\rho}\sum_{k=0}^{r}
       \frac{(-\log a)^{r-k}}{(r-k)!}\ell_{\rho,k}.
 \tag{ASD9.2}
\]
All logarithmic nilpotent terms remain. The first transpose is precomposition with \(T_a\); the second is the contragredient group action and precomposes with \(T_{a^{-1}}\).

Likewise
\[
 R'\ell_{\rho,r}=(-1)^r\ell_{1-\rho,r},\qquad
 (-R)'\ell_{\rho,r}=(-1)^{r+1}\ell_{1-\rho,r}.
 \tag{ASD9.3}
\]
These follow by differentiating the original identity
\(\mathcal M_0Rb(s)=\mathcal M_0b(1-s)\). They preserve every actual multiplicity. The real conjugation symmetry is different and is not silently inserted into ASD9.3.

The finite jet functionals are independent, and each finite joint jet map is onto. One direct construction retains the complete original source transform
\[
 f_*(v)=\frac{\pi}{2}v^2(2\pi v^2-3)e^{-\pi v^2},\qquad
 F_*(s)=\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2)\zeta(s),
 \qquad
 G_*(s)=\mathcal M_0\Sigma f_*(s)=2F_*(s).
 \tag{ASD9.4}
\]
OMS proves its zero divisor is exactly the actual nontrivial-zero divisor, including multiplicities; its values at \(0,1,-2r\) retain the original multiplier and exceptional-point calculation. For a finite set \(P\) of these zeros, divide \(G_*\) by the finite polynomial
\(\prod_{\rho\in P}(s-\rho)^{m_\rho}\). The result is entire, belongs to \(\mathcal B\), and is nonzero at each \(\rho\in P\). Multiplying it by a Hermite interpolation polynomial prescribes arbitrary full jets at those points. To verify the interpolation, its Taylor series at each point is a unit in the finite Taylor algebra, so divide the prescribed jet by that unit, and solve the simultaneous polynomial congruences at the distinct points. The ideals of distinct linear factors are coprime by the Euclidean algorithm, which proves the finite polynomial interpolation. Multiplication and division by the displayed finite polynomials preserve rapid decrease on strips outside a fixed compact set; holomorphic divisibility controls that compact set. Thus the construction remains in the exact \(\mathcal B\) domain and gives the asserted finite right inverse. All other-zero jets remain zero.

The full dual is characterized without declaring every functional a finite sum:
\[
 \boxed{
 Q'=\overline{\operatorname{span}\{\ell_{\rho,r}\}}^{\,\sigma(Q',Q)}.
 }
 \tag{ASD9.5}
\]
For a direct proof, let \(L\) be the displayed span. Its common annihilator in \(Q\) is zero by ASD1.7. If \(L\) were not weak-* dense, there would be a weak-* neighbourhood separating one functional from its closure. A weak-* continuous linear functional is a finite linear combination of evaluations at vectors of \(Q\): this follows because its continuity bounds it by finitely many such evaluations, so it vanishes on their common kernel and factors through their finite-dimensional image. Finite-dimensional separation would therefore produce a nonzero \(q\in Q\) annihilated by all of \(L\), a contradiction. This proves ASD9.5. It is a density statement for the full continuous dual, not an unproved unrestricted product decomposition of \(Q\).

Combining ASD6 with ASD9 gives its exact effect on every zero and derivative:
\[
 \ell_{\rho,r}\xmapsto{\delta'}
       (\ell_{\rho,r},-\ell_{\rho,r}),\qquad
 (\ell_{\rho,r},0)\xmapsto{\partial'}
       \pi'\ell_{\rho,r}.
 \tag{ASD9.6}
\]
The continuous transpose maps and ASD9.5 extend these identities to the entire dual in precisely the weak-* sense already proved.

## ASD10. The original test-space pairing and its exact receiving image

There is a concrete, continuous bilinear pairing on the original \(A\):
\[
 B_A(b,c)=\int_0^\infty b(u)c(u)\,du.
 \tag{ASD10.1}
\]
It uses the displayed \(du=u\,du/u\), not a dropped Haar factor. For example
\[
 |B_A(b,c)|\le
 p_{2,0}(b)p_{2,0}(c)
 \int_0^\infty(u^2+u^{-2})^{-2}\,du,
 \tag{ASD10.2}
\]
and the last integral is finite at both endpoints. This also proves that
\[
 \mathfrak I_A:A\to A',\qquad \mathfrak I_A(b)(c)=B_A(b,c)
 \tag{ASD10.3}
\]
is strong-dual continuous: on a bounded family of \(c\)'s the second seminorm in ASD10.2 is uniformly bounded. It is injective, since \(\mathfrak I_A(b)(\overline b)=\int|b|^2du\) and \(\overline b\in A\).

Direct changes of variables give
\[
 B_A(T_ab,T_ac)=aB_A(b,c),\qquad
 B_A(Rb,Rc)=B_A(b,c),
\]
\[
 \mathfrak I_A(T_ab)=aT_a^\vee \mathfrak I_A(b),\qquad
 \mathfrak I_A(Rb)=R'\mathfrak I_A(b).
 \tag{ASD10.4}
\]
This constructs an actual map \(A\to\chi\otimes A'\), with the same factor \(a\) that occurs in the reflection relation.

This particular pairing does not descend to \(A/J\). The original \(g=\Sigma f_*\) from ASD9.4 is a nonzero real member of \(J\), and
\[
 B_A(g,g)=\int_0^\infty g(u)^2du>0.
 \tag{ASD10.5}
\]
It is finite by ASD10.2 and positive because a continuous nonzero real function is nonzero on an interval. Nonzeroness follows also from \(\Sigma\)'s injectivity and \(f_*\ne0\). Thus it would assign a nonzero value to a pair of zero quotient classes. This proves only the precise failure of ASD10.1 to descend; it is not a statement that quotient pairings do not exist. The actual existing quotient pairing is included in ASD11.

The exact receiving replacement is ASD2.4, the annihilator \(J^\perp\). In fact this annihilator has no nonzero element of the form \(\mathfrak I_A(b)\):
\[
 \mathfrak I_A(A)\cap J^\perp=\{0\}.
 \tag{ASD10.6}
\]
Here is a proof using the entire original image, not a finite test. The image \(J\) is dense in \(L^2(\mathbb R_{>0},du)\). It contains every \(T_ag\), because \(T_a\Sigma h=\Sigma(h(\cdot/a))\) and the latter source remains in \(S\). To prove their dense span, set
\[
 U_f(x)=e^{x/2}f(e^x),\qquad U_g(x)=e^{x/2}g(e^x).
\]
The substitution \(u=e^x\) gives
\(\|U_f\|_{L^2(dx)}=\|f\|_{L^2(du)}\), and, with every factor retained,
\[
 U_{T_ag}(x)=a^{1/2}U_g(x-\log a),\qquad
 \widehat{U_g}(t)
 =\mathcal M_0g(1/2-it)=2F_*(1/2-it).
 \tag{ASD10.7}
\]
In this line the Fourier transform is \(\int h(x)e^{-itx}dx\), so its inverse has factor \(1/(2\pi)\); this is the logarithmic-variable transform, separately specified from the original real Fourier phase in ASD1.2. The function \(U_g\) is Schwartz because \(g\in A\).

If \(f\) is orthogonal in \(L^2(du)\) to every \(T_ag\), ASD10.7 says that \(U_f\) is orthogonal to every translate of \(U_g\). Define, for real \(v\),
\[
 C(v)=\int_{\mathbb R}U_f(x)\overline{U_g(x-v)}\,dx,
 \qquad \widetilde U_g(x)=\overline{U_g(-x)}.
\]
Then \(C=U_f*\widetilde U_g\) is the zero continuous function, and its Fourier transform in the convention of ASD10.7 is exactly
\(\widehat C(t)=\widehat{U_f}(t)\overline{\widehat{U_g}(t)}\).
Plancherel, or first the convolution formula for Schwartz approximations of \(U_f\) followed by \(L^2\) convergence, proves this identity in \(L^2\); \(\widehat{U_g}\) is bounded and \(\widetilde U_g\) is integrable. The entire nonzero function \(2F_*\) has only isolated zeros, so \(\widehat{U_g}(t)\ne0\) for almost every real \(t\). Hence \(\widehat{U_f}=0\) almost everywhere, and \(f=0\). This proves the density assertion.

Finally \(J\) is stable under complex conjugation. If \(\mathfrak I_A(b)\) annihilates \(J\), then \(\int b\overline j\,du=0\) for all \(j\in J\), so \(b=0\) by that density. This proves ASD10.6. The original Fréchet topology is stronger than the Hilbert topology just used for this exact comparison: \(J\) remains closed in \(A\), as already proved. No Hilbert quotient has replaced \(Q\), and no positivity of the spectral quotient has been asserted.

## ASD11. The already constructed Weil form really maps into this dual

The existing RZ10–RZ11 form is retained. For \(F=\mathcal M_0b\), \(G=\mathcal M_0c\), define
\[
 W_{\rm val}([b],[c])
 =\sum_{\rho}m_\rho\,
       \overline{F(\rho^\#)}G(\rho),\qquad
 \rho^\#=1-\overline\rho .
 \tag{ASD11.1}
\]
The sum is over distinct actual original nontrivial zeros, and the multiplicity is written explicitly. It is conjugate-linear in the first variable and linear in the second. The proved bound
\(\sum_{|\rho|\le R}m_\rho\le C(R+2)^{3/2}\), together with rapid decrease on the full strip containing \(0<\Re\rho<1\), gives
\[
 |W_{\rm val}([F],[G])|
 \le C_W q_{1,2}([F])q_{1,2}([G]).
 \tag{ASD11.2}
\]
For clarity, the estimate before taking quotient infima is obtained by bounding each summand by
\(b_{1,2}(F)b_{1,2}(G)(1+|\Im\rho|)^{-4}\) and summing over dyadic height ranges. Membership in \(I_\zeta\) changes no value in ASD11.1, so separate infima over representatives prove ASD11.2. This proves an actual continuous quotient form.

Consequently
\[
 \mathfrak W:\overline Q\longrightarrow Q',
 \qquad \mathfrak W(\overline q)(r)=W_{\rm val}(q,r)
 \tag{ASD11.3}
\]
is a complex-linear continuous map from the conjugate complex vector space. It is strong-dual continuous by ASD11.2 and bounded-set control. Its image lies in the already computed \(Q'=J^\perp\) after composition with \(\pi'\). Thus ASD10's failed integral descent does not erase this distinct existing morphism.

The complete dilation identity is
\[
 W_{\rm val}(T_aq,T_ar)=a W_{\rm val}(q,r),\qquad
 \mathfrak W(\overline{T_aq})
 =aT_a^\vee\mathfrak W(\overline q).
 \tag{ASD11.4}
\]
Termwise, the exponent is
\(\overline{\rho^\#}+\rho=(1-\rho)+\rho=1\).
Absolute convergence justifies the calculation. This is a genuine map
\(\overline Q\to\chi\otimes Q'\), not a change of the source meaning of \(\tau\).

The same actual form is reflection-invariant:
\[
 W_{\rm val}(Rq,Rr)=W_{\rm val}(q,r),\qquad
 \mathfrak W(\overline{Rq})=R'\mathfrak W(\overline q).
 \tag{ASD11.4a}
\]
To check the first equality, its summand is
\(m_\rho\overline{F(1-\rho^\#)}G(1-\rho)\). Set \(\sigma=1-\rho\); then \(1-\rho^\#=\sigma^\#\) and \(m_\sigma=m_\rho\), giving exactly ASD11.1. The second equality follows by replacing the second argument of the first by \(Rr\). For the oriented cohomology mirror \(w=-R\), the corresponding formula is
\(\mathfrak W(\overline{wq})=(-R)'\mathfrak W(\overline q)\); both signs remain.

Its exact kernel is
\[
 \ker\mathfrak W
 =\{\overline{[F]}:F(\rho)=0
       \text{ for every actual nontrivial zero }\rho\}.
 \tag{ASD11.5}
\]
One inclusion follows directly from the sum. For the reverse inclusion, the finite-jet representatives constructed in ASD9, with all other-zero jets zero, allow \(G\) whose only nonzero zero value is \(G(\sigma)=1\). The sum then reads
\(m_\sigma\overline{F(\sigma^\#)}\). Vanishing for every \(\sigma\) proves all the required value vanishings. Thus all higher multiplicity jets remain in the original \(Q\), even though this particular ordinary value-trace form has that radical. Neither simplicity of zeros nor positivity is assumed.

The comparison with the original centered receiver retains the coefficient2:
\[
 W_{\rm val}(\overline{\mathcal T}q,
             \overline{\mathcal T}r)
 =4\,W_{\rm cen}(q,r).
 \tag{ASD11.6}
\]
Indeed both Mellin functions acquire the factor2 in ASD1.8. If the original centered form is transported as a form on the raw space, its formula is
\(W_{\rm transported}=\tfrac14W_{\rm val}\).
Both maps are now explicit; no factor has disappeared.

For the zero-value functionals the row in ASD6 transports this form concretely:
\[
 \mathfrak W(\overline q)
 \xmapsto{\delta'}
 \bigl(\mathfrak W(\overline q),-\mathfrak W(\overline q)\bigr),
\]
\[
 \bigl(\mathfrak W(\overline q),0\bigr)
 \xmapsto{\partial'}\pi'\mathfrak W(\overline q).
 \tag{ASD11.7}
\]
All continuous-dual target spaces and transposes in this formula have been constructed. These are valid irrespective of the sign of the form.

## ASD12. The dual diagram is not obtained by reversing a sheaf restriction silently

The original restriction maps point from chart sections \(V_\pm\) to the common open sections \(A\). Their transposes point from \(A'\) to \(V_\pm'\). This reversal is part of the derived dual calculation:
\[
 V_\pm\xrightarrow{r_\pm}A
 \quad\rightsquigarrow\quad
 A'\xrightarrow{r_\pm'}V_\pm'.
 \tag{ASD12.1}
\]
It is a covariant section diagram, rather than the same sheaf with renamed coefficients. The actual whole-space gluing on dual sections is the cokernel map
\[
 A'\xrightarrow{(r_+',-r_-',0)}
 V_+'\oplus V_-'\oplus V_{\rm extra}'
 \longrightarrow H'\longrightarrow0.
 \tag{ASD12.2}
\]
Its exactness was proved in ASD3 using Hahn–Banach. This is the explicit continuous-dual gluing correspondence. The kernel of its first map is \(Q'\), not zero. On every nonempty arithmetic open the original restrictions were identities on \(A\), so the transposed extension maps remain identities on \(A'\); all arithmetic prime points in the source fibre remain present.

Thus the transpose construction retains precisely the extra derived term that would be lost by treating dualization as a pointwise replacement of a coefficient sheaf without its direction or complex. It has not constructed a geometric dualizing sheaf or an \(i^!\)-to-\(i^*\) Verdier comparison. It has constructed all displayed transposes, the full dual cohomology, and their exact relation to the original localization maps.

## ASD13. What this contributes to the requested supported-obstruction calculation

The concrete global result is the exact row ASD6.3 and the complete complexes ASD3–ASD5. They carry the full original \(Q'\), every original multiplicity jet, the four endpoint dual lines, the two entire faithful closed dual copies, the source integer action, each prime dilation, and the chart mirror with its orientation sign.

Deligne's §3.6.1(8) identifies the supported obstruction group with
\[
 H^{2N-i-1}(X_s)^\vee(-N).
\]
The duality and twist are geometric ingredients of his diagram; Lemma3.6.3 then gives its lower weight bound. The class-to-be-lifted group has the separate upper bound in Lemma3.6.2. Exactness of the weight truncation eliminates the incompatible supported image.

Here the actual transpose of the supported-to-global map is the injective anti-diagonal \(Q'\to Q'\oplus Q'\), and the actual next map is the sum into \(J^\perp\subset A'\). These maps are already globally split as in ASD6.5. Their corresponding finite zero jets have exactly the same contragredient characters \(p^{-\rho}\) on both sides; no weight displacement has been inserted into the localization arrow. The character \(a\) is present in the original reflection relation and in the genuine pairing maps ASD10.4 and ASD11.4. These statements calculate the factor precisely, but neither a cochain degree shift nor reflection alone adds a geometric Tate twist to the supported row.

The actual stronger correspondence now available is
\[
 Q'=J^\perp\subset A',
 \qquad
 \overline Q\xrightarrow{\mathfrak W}\chi\otimes Q',
 \qquad
 Q\xrightarrow{R}\chi\otimes Q^{\rm inv},
\]
with the distinct domains, full maps, and exact kernel of \(\mathfrak W\) proved above. This gives a specified receiving target for further actual coefficient pairings. It does not replace them by an assumed perfect, positive, or finite-dimensional duality.

### The completed full-jet continuation received by this dual row

The companion [GLOBAL_ORIGINAL_ZETA_RESIDUE_DUALITY_INDEPENDENT.md](GLOBAL_ORIGINAL_ZETA_RESIDUE_DUALITY_INDEPENDENT.md), GZR2–GZR8, now constructs the stronger continuous nondegenerate bilinear pairing on this same entire quotient:
\[
 B_\zeta([F],[G])=\frac1{2\pi i}
 \left(\int_{2-i\infty}^{2+i\infty}
       -\int_{-1-i\infty}^{-1+i\infty}\right)
 \frac{F(s)G(1-s)}{\zeta(s)}\,ds.
 \tag{ASD13.1}
\]
Both edge integrals run upward. Its original denominator, all multiplicities, convergence, quotient descent, and nondegeneracy are proved there; this is no longer a prospective pairing. GZR8 supplies strong-continuous injective maps with weak-* dense images
\[
 \mathcal D_Lx(y)=B_\zeta(x,y),\qquad
 \mathcal D_Ry(x)=B_\zeta(x,y),\qquad
 \mathcal D_{L,R}:Q\longrightarrow\chi\otimes Q'.
 \tag{ASD13.2}
\]
The target \(Q'=J^\perp\) and all its supported transpose maps are exactly the ones constructed above. These stronger maps do not erase a higher-jet radical: their kernels are zero. They do not assert surjectivity onto the continuous dual, positivity, or a geometric dualizing identification. Their mirror comparison is the exact GZR7.5–GZR7.7 relation with the companion denominator \(\zeta(1-s)\), including its minus sign and full functional multiplier, not an asserted invariance of \(B_\zeta\) itself.

The further [ORIGINAL_ZETA_JACOBIAN_TRACE_BRIDGE.md](ORIGINAL_ZETA_JACOBIAN_TRACE_BRIDGE.md), JTB2–JTB7, constructs the original derivative operator
\[
 \mathcal J_\zeta=(L-1)^{-2}
       M_{(s-1)^2\zeta'(s)}:Q\to Q
\]
with its complete endpoint-corrected representative, and proves
\[
 W_{\rm val}(x,y)=B_\zeta(\mathcal J_\zeta y,Cx),
 \qquad (CF)(s)=\overline{F(\bar s)}.
 \tag{ASD13.3}
\]
Consequently the exact factorization into the present continuous-dual receiver is
\[
 \mathfrak W(\overline x)
   =\mathcal J_\zeta'\mathcal D_R(Cx).
 \tag{ASD13.4}
\]
Indeed evaluation of its right-hand side at \(y\) gives
\(\mathcal D_R(Cx)(\mathcal J_\zeta y)
=B_\zeta(\mathcal J_\zeta y,Cx)\), which is ASD13.3. Thus the exact higher-jet loss of the value-trace form is retained as a constructed derivative factor, while the full residue pairing supplies the stronger dual injections. ASD6.3 receives both maps without changing a support label or a differential sign. The complete companion proofs are the cited sources for these new statements; the proof of ASD13.4 itself is the displayed evaluation.

Nothing here assigns a weight to source \(Z_1/\tau\), retracts the user's global arithmetic reconstruction, or uses an arbitrary receiver as a counterexample to that reconstruction. The calculation proves the full dual correspondence and its exact supported maps. Numerical purity and RH do not follow from the calculation alone, and no such conclusion is asserted.

### Reading and dependency record for this derivation

- Current source rules and B1–B5/P1–P5 reread; the three complete global corpus arguments listed in ASD0 reread before ASD10's interpretation.
- DCP3, DCP7–DCP12 read completely for the restriction, support, faithful extra-copy, and mirror formulas; their previous complete source reading is retained.
- CTF0–CTF8 read completely, with ASD4 applying CTF2–CTF4 and the exact extra identity-cone sign from CTF7.
- OMS1's original spaces and Mellin isomorphism, OMS2's original \(f_*,F_*\) formulas, and the already proved full image theorem are explicitly the receiving inputs. No new claim of a complete fresh reading of all OMS is made.
- RZ10–RZ11 read completely and actually applied in ASD11, preserving the form, radical, and similitude rather than asserting absence of quotient pairings.
- The complete retained RZ copy and the external file actually read were compared by SHA256 and are identical, with the hash in ASD0. For the final continuation, GZR7–GZR8 and JTB0–JTB6 plus the opening definitions and covariance of JTB7 were read. No complete fresh reading or independent verification of both entire companion manuscripts is claimed by this source-use entry.
- Deligne transcription lines2466–2559 read completely; source kind retained as transcription. Human theorem attribution is to Pierre Deligne. CC Fourier localization is attributed to Alain Connes and Caterina Consani; the analytic image theorem's provenance is retained from Meyer and the cited programme derivations.

## ASD14. The actual residue chain map and its entire cone

This continuation uses the same source prerequisites as ASD0, with no change to \(Z_0,Z_1,Z_2,\tau\), the source ring action, or the original coefficient topologies. The pairing here is the constructed original-\(\zeta\) pairing GZR2–GZR8, rather than the test-space integral ASD10.1. Its strong-continuous injective left map and its exact similitude are
\[
 \mathcal D_L:Q\to Q',\qquad
 \mathcal D_L(x)(y)=B_\zeta(x,y),\qquad
 \mathcal D_LT_a=aT_a^\vee\mathcal D_L.
 \tag{ASD14.1}
\]
Its image is weak-* dense, as proved in GZR8. These properties hold on the complete original quotient with every multiplicity; they are not finite-packet assumptions.

### ASD14.1. Construct and verify the chain map

Write \(P=D_{\rm full}^0=V_+\oplus V_-\oplus V_{\rm extra}\), and retain
\[
 D_{\rm full}=[P\xrightarrow{d}A],\qquad
 d(v_+,v_-,w)=r_+v_+-r_-v_-.
\]
Set
\[
 T=\chi\otimes D_{\rm full}^\vee[-2].
\]
Here \(\chi(a)=a\) changes the receiving real-group action only; it does not change the source-ring action. By ASD3.3 and the even shift, the only nonzero terms and differential of \(T\) are
\[
 T^1=\chi\otimes A',\qquad T^2=\chi\otimes P',\qquad
 d_T^1=d' :\lambda\mapsto(r_+'\lambda,-r_-'\lambda,0).
 \tag{ASD14.2}
\]
Define
\[
 \Psi_\zeta:D_{\rm full}\longrightarrow T,\qquad
 \Psi_\zeta^0=0,\qquad
 \boxed{\Psi_\zeta^1=\pi'\mathcal D_L\pi:A\to A'.}
 \tag{ASD14.3}
\]
Thus its actual evaluation formula is
\[
 (\Psi_\zeta^1b)(c)
 =\frac1{2\pi i}
 \left(\int_{2-i\infty}^{2+i\infty}
       -\int_{-1-i\infty}^{-1+i\infty}\right)
 \frac{(\mathcal M_0b)(s)(\mathcal M_0c)(1-s)}
      {\zeta(s)}\,ds .
 \tag{ASD14.4}
\]
Both edges retain their upward orientation, original denominator, full Mellin transforms, and all the factors in ASD1.6–ASD1.8. This is a continuous map from the original \(A\) to its strong dual and hence to its weak-* dual: \(\pi\) is continuous, \(\mathcal D_L\) is strong continuous, and \(\pi'\) is strong continuous by ASD2.2.

There are exactly two nontrivial cochain equations to check. First
\[
 \Psi_\zeta^1d=\pi'\mathcal D_L(\pi d)=0
   =d_T^0\Psi_\zeta^0,
\]
since \(d(P)=J=\ker\pi\). Second
\[
 d_T^1\Psi_\zeta^1=d'\pi'\mathcal D_L\pi=0.
\]
Indeed \(\pi'\lambda\) annihilates \(J=d(P)\), so \(d'\pi'\lambda=0\). This proves the chain map on the stated complexes, rather than only on their cohomology.

Let \(\rho_D(a)\) be the original action ASD7.3 and let
\(\rho_T(a)=a\rho_D^\vee(a)\) on the shifted dual. In degree1,
\[
 \Psi_\zeta^1 T_a
 =\pi'\mathcal D_LT_a\pi
 =a\pi'T_a^\vee\mathcal D_L\pi
 =aT_a^\vee\Psi_\zeta^1.
 \tag{ASD14.5}
\]
Here the \(T_a\) between \(\mathcal D_L\) and \(\pi\) is its induced quotient operator; equivariance of \(\pi\) proves both transpose identities. In degree0 both sides are zero. Thus this is equivariance for every positive real \(a\), including every original prime \(p\), with no factor removed.

It is also linear for the source receiving ring \(\mathbb Z^3\). An element \((r,b_+,b_-)\) acts by the same scalar \(r\) on \(A\) and \(A'\), so ASD14.3 commutes with it. In degree0 the zero map commutes with every action, including the separate \(b_+\) and \(b_-\) actions on the full extra copies. Consequently all supplied source multiplications and integer-input additions are preserved. In particular the chain map has introduced neither addition on source \(\tau\) nor an identification of \(\tau\) with source integer \(1\).

### ASD14.2. Compute every cone degree and its cohomology

Use the original CTF convention
\[
 K_\zeta^n=T^n\oplus D_{\rm full}^{n+1},\qquad
 d_{K_\zeta}(v,c)=(d_Tv+\Psi_\zeta c,-dc).
\]
Substitution of every degree gives the exact four-term complex
\[
 \boxed{
 P\xrightarrow{-d}A
   \xrightarrow{\Psi_\zeta^1}\chi\otimes A'
   \xrightarrow{d'}\chi\otimes P'
 }
 \quad\text{in degrees }-1,0,1,2.
 \tag{ASD14.6}
\]
The first minus sign is the shifted-source sign. The final differential is \(+d'\), with its internal chart signs in ASD14.2; the dual convention and shift add no further sign.

Write \(H=\ker d=H_0\oplus V_{\rm extra}\), as in ASD3.6. The cohomology, with its exact action, is
\[
 \boxed{
 \begin{aligned}
 H^{-1}(K_\zeta)&=H,\\
 H^0(K_\zeta)&=0,\\
 H^1(K_\zeta)&=\chi\otimes\bigl(Q'/\mathcal D_LQ\bigr),\\
 H^2(K_\zeta)&=\chi\otimes H',\\
 H^n(K_\zeta)&=0\qquad(n\notin\{-1,0,1,2\}).
 \end{aligned}}
 \tag{ASD14.7}
\]
Here the tensor notation retains the numerical action; as vector spaces the third and fourth entries are \(Q'/\mathcal D_LQ\) and \(H'\).

The degree \(-1\) statement is the definition of \(H\). For degree0, both \(\pi'\) and \(\mathcal D_L\) are injective, whence
\(\ker\Psi_\zeta^1=\ker\pi=J=\operatorname{im}(-d)\).
For degree1, ASD2.4 and ASD3.4 give
\[
 \ker d'=\pi'Q',\qquad
 \operatorname{im}\Psi_\zeta^1=\pi'\mathcal D_LQ,
\]
where the second equality uses the surjectivity of \(\pi\). The injective map \(\pi'\) therefore supplies exactly the third quotient in ASD14.7. Finally ASD3.7 identifies the cokernel of \(d'\) with \(H'\), proving the fourth entry. No other degrees occur.

For the weak-* topologies in ASD2, \(\pi':Q'\to J^\perp\) is a homeomorphism onto its image, and \(\mathcal D_LQ\) is dense in \(Q'\). Hence
\[
 \bigl(H^1(K_\zeta)\bigr)_{\rm Hausdorff}=0
 \quad\text{in this specified weak-* quotient topology}.
 \tag{ASD14.8}
\]
This is the quotient by the closure of zero. It does not prove that the algebraic cokernel \(Q'/\mathcal D_LQ\) vanishes, and it does not prove that \(\mathcal D_LQ\) is closed or onto. No corresponding strong-dual density or strong-quotient conclusion is asserted. The original source spaces \(P,A,Q\) still have their original topologies.

The full faithful closed copies are explicit in the cone:
\[
 K_\zeta=K_{\zeta,\epsilon}
 \oplus V_{\rm extra}[1]
 \oplus(\chi\otimes V_{\rm extra}')[-2].
 \tag{ASD14.9}
\]
Indeed \(d\) kills the source extra copies, \(\Psi_\zeta\) has only the overlap component, and \(d'\) has zero extra component. Thus all these displayed extra differentials are zero. Their degree \(-1\) and degree2 cohomology has not been contracted. The four original endpoint lines are likewise present in \(H_0\subset H^{-1}\) and their full duals in \(\chi H_0'\subset H^2\). This cone is not the extra identity cone from ASD4, and the identity-cone contraction cannot remove its terms.

### ASD14.3. The exact companion mirror identity

Define \(\Psi_{\zeta^\vee}\) by the same construction, using the companion \(B_{\zeta^\vee}\) whose denominator is \(\zeta(1-s)\). GZR7 proves
\[
 B_\zeta(Rx,Ry)=-B_{\zeta^\vee}(x,y).
 \tag{ASD14.10}
\]
Replacing \(y\) by \(Ry\) and evaluating gives
\[
 \mathcal D_L^\zeta R=-R'\mathcal D_L^{\zeta^\vee}.
 \tag{ASD14.11}
\]
This is an identity between the two constructed pairing maps, not a self-reflection assertion.

Let \(w_D\) be the original Cech mirror, with \(w_D^0\) the chart and extra-copy swaps and \(w_D^1=-R\). On \(T=\chi D_{\rm full}^\vee[-2]\), denote by \(w_T=w_D^\vee\) its shifted dual mirror: it is \(-R'\) in degree1 and the corresponding dual chart and extra swaps in degree2. The even shift introduces no new sign. Then
\[
 \boxed{\Psi_\zeta w_D=-w_T\Psi_{\zeta^\vee}.}
 \tag{ASD14.12}
\]
In degree1 its left side is
\[
 \pi'\mathcal D_L^\zeta\pi(-R)
 =-\pi'\mathcal D_L^\zeta R\pi
 =\pi'R'\mathcal D_L^{\zeta^\vee}\pi
 =R'\Psi_{\zeta^\vee}^1.
\]
Its right side is \(-(-R')\Psi_{\zeta^\vee}^1\), the same expression. In the remaining source degree both sides vanish. This verifies every sign.

The character twist is necessary in checking compatibility with the full unshifted prime/reflection relation. On the contragredient dual before twisting,
\[
 \rho_D^\vee(a)w_D^\vee
   =a^{-1}w_D^\vee\rho_D^\vee(a^{-1}).
\]
Consequently on \(T\)
\[
 \rho_T(a)w_T
 =a\rho_D^\vee(a)w_T
 =w_T\rho_D^\vee(a^{-1})
 =a\,w_T\rho_T(a^{-1}).
 \tag{ASD14.13}
\]
The original source complex has the same final relation
\(\rho_D(a)w_D=a\,w_D\rho_D(a^{-1})\).
Thus ASD14.12 is compatible with prime inversion and the exact factor \(a\). No geometric Tate identification is needed to prove this representation identity, and none is inferred from it.

The corresponding actual cone map is
\[
 \mathcal W:K_{\zeta^\vee}\longrightarrow K_\zeta,\qquad
 (v,c)\longmapsto(-w_Tv,w_Dc).
 \tag{ASD14.14}
\]
For its target differential the first coordinate is
\(-w_Td_Tv+\Psi_\zeta w_Dc\).
By ASD14.12 it equals
\(-w_T(d_Tv+\Psi_{\zeta^\vee}c)\); the second coordinate is
\(-w_Ddc\). These are precisely the coordinates of
\(\mathcal Wd_{K_{\zeta^\vee}}(v,c)\).
Thus it is a cochain isomorphism. Applying the companion version twice yields identity because both mirrors square to identity and the two target signs multiply to \(+1\). It intertwines the original real actions with the same inversion and factor \(a\) in ASD14.13, and is semilinear for the receiving ring involution exchanging \(e_+,e_-\). That involution fixes every original source integer and \(\tau\).

ASD14 constructs a genuine full-coefficient dual comparison and computes its entire cone. Its nonzero \(H,H'\) terms, exact possibly nonzero algebraic dual cokernel, and companion mirror are displayed. It is not asserted to be a Verdier isomorphism, a self-mirror pairing, a closed-image theorem for \(\mathcal D_L\), or a numerical weight bound.

## Explicit global continuation: finite lifting and a nonzero remainder

The earlier uncertainty about algebraic surjectivity is now resolved by GLOBAL_POLYNOMIAL_DUAL_DEFECT.md PGD1–PGD6, independently checked in PGC0–PGC7: the actual algebraic cokernel is nonzero. Its explicit class c_zeta is the original-zeta contour functional with the constant arithmetic function 1 in the first slot. A lift would require a rapidly decreasing entire representative to equal 1 at all actual zeros, which the proved unbounded zero heights exclude. PGD constructs an injected rational-function line, entire representatives retaining all Hermite pole corrections, and the whole real/prime orbit. This is a receiving cokernel class, not primitive tau or a claimed off-critical zero.

SCL0–SCL9 and DPL0–DPL9 prove every nonzero polynomial in the actual cokernel generator invertible. Thus all finite-dimensional invariant dual spaces lift uniquely, continuously and with the original real/prime action. DPL gives explicit extension splittings and computes every degree of the cyclic derived Hom into the actual cone. These results retain its H and H′ terms, all faithful closed copies and support labels. The weak-* Hausdorff quotient remains zero alongside the now proved nonzero algebraic quotient. Current source Z_0, Z_1/tau and Z_2 are unchanged. Complete proofs and exact human citations are in the linked continuation files; the full geometric weight-separation goal remains active.

## Full global prime action and actual supported placement

The new complete proofs GGT0–GGT8, FPO0–FPO8 and UOS0–UOS9 (including UOS8A) strengthen the preceding global remainder calculation. The original-zeta Gaussian trace has a TlogT leading term only at the identity scale and at most order T at every other fixed positive scale. Testing a proposed finite relation against every inverse scale proves all coefficients zero. Consequently the entire finite group algebra C[R_+^×], including the Laurent algebra of all original primes, injects into the original multiplier quotient and linearly into the actual comparison cokernel. This computes relations after the actual zero-jet quotient, not only among entire functions before quotienting.

UOS constructs the full chain map into the actual dual-supported comparison cone. It sends c_r to (c_r,0), acts identically on H, and restricts χH′ to χE′ with every endpoint and extra closed copy retained. Its companion mirror is c_r→−r c_(1/r) with the companion denominator; the oriented global-dual mirror has the opposite sign. The ordinary Fourier restriction still has its explicit section. Thus the new classes are relative residue-representation classes with proved supported placement, not a claimed failure of that existing Fourier lift. The source Z_0, Z_1/tau and integer Z_2 have not changed, and the full numerical weight-separation target remains active.

The original Connes–Consani explicit formula has been applied with a proved cutoff extension; the exact archimedean comparison is W_R(f_T,x)=A_T(x)+1, retaining the endpoint at zero and every finite trivial-zero contour correction. Complete human citations, author-source archive and bounded reading coverage are recorded with these proofs. All complete proof bodies and inspected reproducible diagrams are in the cumulative TeX.

## Exact original character lifting and its full supported return

MCL0–MCL11 now computes the original transpose A′→S′ on every actual zero and all its Mellin jets. A target jet of order j needs generalized-character length exactly m+j+1 at a zero of multiplicity m. The full Euler-distribution classification proves minimality against the whole original continuous dual; two actual primes remove the single-prime character aliases. Every prime logarithm and the full Gamma/Fourier return remain. This is an actual continuous lift, with a nonzero class only when its original annihilator must be preserved.

RPC0–RPC8 constructs the original restriction's actual pushout by the residue image, proves its precise cochain location and a single coherent real/prime-equivariant section on all locally finite classes. ORE0–ORE10 calculates the unmodified connecting class, including its full Gamma germ and rank min(m,r), then proves its place in every degree of the full supported derived comparison. The degree-two map is (eta,e)↦(−delta_q(eta)/2,e). Thus its image in C_zeta/qC_zeta is zero, while the full supported map retains its Y/qY component. Both assertions follow from the constructed maps; no cone degree or extra coefficient is discarded.

These results refine the meaning of the prior finite-lift statement without withdrawing its proved scope. Fixed-annihilator splitting is stronger than the surjectivity in Deligne's invariant-cycle theorem. The original longer-chain map is already surjective. The present numerical character truncation retains its same-character extension whenever it retains the target; it is not Deligne's independently proved geometric weight gap. Complete proofs, independent checks and inspected reproducible diagrams have been inserted into the cumulative TeX. The actual tau weight-separation goal remains active.
