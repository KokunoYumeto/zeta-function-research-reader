# Adversarial review of one retained arithmetic realization

Date: 2026-09-13. Task: `/root/independent_review`. This is a bounded mathematical assembly review, not a claim that RH or its negation has been established. The companion `divisor_transition_review.md` gives the independently checked divisor transitions.

The parent assignment is to construct one object from the actual programme, including the original source, supported zeros, the balanced kernel and diagonal, coherent observations, all finite divisors, full tensor packets, canonical source metrics, and the proved restrictions. The assembly must use these actual objects and morphisms. An arbitrary system of matrices satisfying selected inequalities is not an equivalent construction.

## 1. The exact universal arrow that retains the original preimage

Let

\[
U=\{s\in\mathbb C:0<\Re s<1,\ \Re s\ne1/2\},\qquad
\mathcal N_U=(\mathcal O_\mathbb C/(g))|_U,\qquad g=2\xi.
\]

The open set is preserved by conjugation and by s↦1−s. It is not the absolute pointed base. In particular its absence of points carrying the zero divisor cannot identify a supported amplitude zero with the base element tau.

Use the actual balanced complex, with the original two actions on its incoming legs,

\[
C_\tau=[\mathcal V_+\oplus\mathcal V_-\xrightarrow{d}\mathcal B],
\quad d(\phi,\psi)=\Theta(\phi-\widehat\psi),
\quad t|_{V_+}=D,\quad t|_{V_-}=1-D.
\]

The terms have cochain degrees zero and one. The original Fourier transform is A-linear from V_- to V_+, because its exact intertwining relation is Fourier D=(1−D) Fourier. Write Mel:mathcal B→mathcal O for the balanced Mellin map. The actual map

\[
\pi_U:C_\tau|_U\longrightarrow\mathcal N_U[-1],
\qquad\pi_U^0=0,\qquad\pi_U^1(F)=[\operatorname{Mel}F]\bmod g
\]

is a cochain map, since Mel d=g(H_phi−H_Fourierpsi). It is termwise onto: the source test F_0(x)=exp(−(log x)^2) has nowhere-vanishing Mellin transform H_0(s)=sqrt(pi)exp(s²/4), so a local class [a] is lifted by aH_0^(−1) tensor F_0. Its literal kernel is

\[
\mathcal R_U=
[\mathcal V_+|_U\oplus\mathcal V_-|_U
\xrightarrow{d}\operatorname{Mel}^{-1}(g\mathcal O_U)],
\qquad
0\to\mathcal R_U\to C_\tau|_U\xrightarrow{\pi_U}\mathcal N_U[-1]\to0.
\tag{AR1}
\]

This is the actual preimage extension, not just its cohomology groups. It differs from the kernel of C_tau→[O→g O], whose degree-zero term also imposes H=0 after removal of the diagonal. The two kernels are related by the written map [O→g O]→N[-1]; they must not be asserted literally equal.

The degree-zero kernel of d consists exactly of pairs (Fourier psi,psi), because Theta is injective. The quotient of the degree-one term of R_U by the image of d is exactly ker(beta)=K_U. Thus

\[
H^0\mathcal R_U\simeq\mathcal V_+|_U,\qquad
H^1\mathcal R_U\simeq\mathcal K|_U.
\tag{AR2}
\]

For the latter equality, a balanced quotient class is in K precisely when any representative has Mellin transform in gO; changing a representative by a theta boundary preserves this condition. These descriptions also cover points where g is a unit. At such points N=0 but the kernel and diagonal are still retained.

There is a precise universal property, stronger than merely naming the quotient. For every coherent O_U-module E, composition with pi_U gives a natural bijection

\[
\operatorname{Hom}_{\mathcal O_U}(\mathcal N_U,E)
\xrightarrow{\sim}
\operatorname{Hom}_{\mathrm{Ch}(\mathcal O_U)}(C_\tau|_U,E[-1]).
\tag{AR3}
\]

Indeed a cochain map to E[-1] has only a degree-one map f:mathcal B→E, and the cochain equation is exactly f d=0. It therefore descends uniquely through H¹C_tau=M. OCQ.9–12 prove that every map from M to a coherent E vanishes on K and factors uniquely through beta:M→N. Conversely every map N→E produces the displayed cochain map. These constructions are inverse and compatible with restrictions. Consequently pi_U is initial among the actual maps from C_tau|U to a coherent sheaf placed in degree one. It is a universal arrow with its entire kernel attached.

This property does not extend to every bounded derived coherent target. OCQ.21–25 compute nonzero Ext¹(K,O) and an explicit nonsplit extension. A derived comparison that deletes those classes is not the same object. Similarly, derived tensoring of the whole C_tau with a finite spectral thickening must retain the diagonal term: the finite-thickening equivalence in DP.2 concerns M→N, not an assertion that all of C_tau has become N[-1].

## 2. A single tensor source from which the finite data are recovered

The most economical genuine envelope is the tensor differential graded algebra of the *raw original complex*, followed by its specified analytic observations. Let

\[
C^{\rm raw}_\tau=[V_+\oplus V_-\xrightarrow{d}\mathscr B],
\qquad
\mathbb T_\Theta=T_\mathbb C(C^{\rm raw}_\tau)
=\bigoplus_{k\ge0}(C^{\rm raw}_\tau)^{\otimes_\mathbb C k}.
\tag{AR4}
\]

This is an algebraic direct sum. The tensor differential is the original signed differential

\[
d(x_1\otimes\cdots\otimes x_k)
=\sum_i(-1)^{\sum_{j<i}|x_j|}
x_1\otimes\cdots\otimes dx_i\otimes\cdots\otimes x_k.
\]

The primitive A-action is

\[
t(x_1\otimes\cdots\otimes x_k)
=\sum_i x_1\otimes\cdots\otimes tx_i\otimes\cdots\otimes x_k.
\tag{AR5}
\]

It commutes with d because t does so on the original complex; the verification is termwise. It is a derivation for concatenation. The universal property is explicit: for any unital differential graded complex algebra R with a degree-zero derivation T commuting with its differential, every cochain map f:C_tau^raw→R satisfying f(tx)=T f(x) extends uniquely to a unital differential graded algebra map F:T_Theta→R intertwining the derivations. On a pure tensor its forced value is f(x_1)...f(x_k). The signed Leibniz rule proves differential compatibility, the ordinary derivation rule proves the t relation, and pure tensors span the algebra, proving uniqueness. This is a constructed universal envelope of the original theta complex, not a free replacement for its differential.

The original support masks and proper-source labels remain a diagram of subcomplexes of C_tau^raw. Tensor (AR4) is applied to their actual inclusions and original transition maps. The cochain isomorphism (phi,psi)↦(phi−Fourier psi,Fourier psi) displays the joint-face diagonal. Its plus-only image is (u,0), and its minus-only image is (−v,v); the diagonal is not copied into each one-leg face. All original maps lift labelwise as tau↦tau and (S,x)↦(S,f(x)). This keeps the supported zero (S,0) distinct from tau.

In tensor degree k, the top cochain space of (AR4) is exactly mathscr B^(tensor k), and its top cohomology is Q^(tensor k). To check the latter directly, the image of the preceding tensor differential is the sum of the subspaces having one factor in Theta V; successive quotients over the field C identify the quotient with (B/Theta V)^(tensor k). Thus the original full tensor arithmetic observation is already inside the one dg algebra.

Equip that top cochain space with its *original* pre-Hilbert form

\[
\langle F,G\rangle_k=\int_{(0,\infty)^k}\overline{F(\mathbf x)}G(\mathbf x)\,d\mathbf x,
\tag{AR6}
\]

on finite tensor sums. The function embedding is injective, and the form is positive definite: a nonzero smooth function cannot have zero L² norm. Its tensor-product formula follows by Fubini from rapid endpoint decay. This is a marked measured dg source. The form is used on the original source; it is not declared to descend to its theta quotient.

The analytic observation in tensor degree one is exactly (AR1), obtained by balancing the original A-action and sheafifying. For tensor degree k one can likewise balance the primitive sum action (AR5) degreewise. There is no claim that this produces an O_U-algebra using the ordinary tensor product over O_U: independent spectral variables are tensor products over C, and their sum action is primitive. Tensoring the packet factors over A or O would impose equal spectral variables and change the programme. If the complete assembly is written as a category representation, these are separate typed objects joined by their actual balancing maps, rather than an invented monoidal identification.

All F_h below are marked vectors already determined in the top cochain generator B by the actual inverse Mellin integral. The finite source and metric data are recovered from these vectors by polynomial action and restriction of (AR6). Thus they are not independent freely chosen matrices added to (AR4).

## 3. All divisors: the coefficient chart that remains valid

Let D_g be the directed poset of monic finite effective divisors of the actual zero divisor of g, invariant under the original required reflection/conjugation symmetries. It contains 1. Its order is ordinary divisibility; the least common multiple gives an upper bound, with each root order still at most its actual order in g.

For h in D_g the entire quotient v_h=g/h and original F_h satisfy

\[
\mathcal MF_h=v_h,\qquad h(D)F_h=\Theta\phi_*.
\]

The uniformly valid torsion chart is

\[
\tau_h:E_h=\mathbb C[s]/(h)\xrightarrow{\sim}Q[h(D)],
\qquad[P]\longmapsto[P(D)F_h].
\tag{AR7}
\]

Its inverse is the connecting map delta_h in BK.11: h(D)P(D)F_h=Theta(P(D)phi_*) and H_(P(D)phi_*)=P, so delta_h tau_h=identity. Since j_h g=0, BK.11 also gives surjectivity. The coherent image of this chart is

\[
[P]\longmapsto[(g/h)P]\in\mathcal N[h].
\tag{AR8}
\]

At a root with g=u z^m and h=v z^r, it is multiplication by the retained unit u/v times z^(m−r), an isomorphism from O/(z^r) to the annihilator of h in O/(g). It remains valid for partial multiplicities.

In contrast, upsilon_h=j_h(g/h) is not generally a unit in E_h for partial divisors. With g=z^m and h=z^r, r<m, it has a positive vanishing order, and can even be zero. The normalized full-order chart sigma_h using upsilon_h^(−1), and the unitful cyclic injection formulated through it, cannot be applied to all h. The complete-order invariant divisors are cofinal in D_g, so all finite information can also be recovered using only that cofinal subsystem; but partial quotients must still use the exact maps (AR7)–(AR8), not an inverse of a nonunit.

If h'=rh, the original integral and differential identities give

\[
F_h=r(D)F_{h'},\qquad
\tau_{h'}\circ([P]\mapsto[rP])=\tau_h.
\tag{AR9}
\]

The injection is A-linear, not a unital algebra map. The map E_h'→E_h given by reduction is a different, oppositely directed unital algebra map; it must not be confused with torsion inclusion. Exact sequences and both arrows can be retained in a presented category, but they have different universal meanings.

The colimit with the injections in (AR9) is the actual polynomial-torsion submodule of Q: for an arbitrary polynomial p, the A-linear connecting map in BK.11 identifies Q[p] with ker(M_g:E_p→E_p). At a root where p has order n and g has order m this kernel is z^(max(n−m,0)) O/(z^n), killed by z^(min(n,m)); if m=0 it is zero. Thus each torsion element is killed by a finite divisor of g, and enlarging to a symmetry-stable divisor retains it. The universal property is the ordinary explicit directed-union property: a compatible family of linear maps out of the actual finite submodules gives a unique map out of their union. No new element or unidentified limiting spectral mass is introduced.

This colimit is taken only over the injective torsion subsystem. An indiscriminate colimit over all quotient and observation arrows is invalid for the intended retention. The category of coherent quotients includes the terminal zero quotient N→0, and its colimit is zero. Identifying each source vector with all its quotient images would therefore delete the very data to be retained. One representation keeps those quotient arrows as part of its structure; it does not make them all identities in a colimit.

## 4. Full tensor packets are necessary for compatible assembly

For each h,k retain the full ambient coefficient algebra

\[
E_h^{\otimes k}=\mathbb C[s_1,\ldots,s_k]/(h(s_1),\ldots,h(s_k)),
\quad S=s_1+\cdots+s_k.
\tag{AR10}
\]

The original source map P↦P(D_1,...,D_k)F_h^(tensor k) and observation tau_h^(tensor k) give the full diagram. Its kernel is the displayed ideal: quotienting independently by each h(s_i) gives the tensor coefficient algebra, and the tensor product of the injective maps (AR7) remains injective over C.

When h'=rh, transport in the ambient tensor algebra and source is multiplication by

\[
R(\mathbf s)=\prod_{i=1}^k r(s_i).
\tag{AR11}
\]

The source metric is exactly preserved with the corresponding degree shift, since v_h(s_i)=r(s_i)v_h'(s_i) before absolute squares. In several variables the shift in total polynomial degree is k deg r. This relation follows by the literal source equality, not by constructing an arbitrary metric isometry.

The canonical sum-cyclic subspace C[S]1 is a marked subobject of (AR10). It is *not* generally preserved by (AR11). There is an actual obstruction already for k=2: enlarge a full reflection-stable h by another actual reflection orbit. An old pair (rho,1−rho) and a new pair (sigma,1−sigma) both have total S=1. The product r(s_1)r(s_2) is nonzero at the old pair and zero at the new pair. No polynomial in S has those values. There are distinct actual reflected zero orbits available; the argument does not postulate hypothetical coefficient values. Therefore a directed system containing only each h's distinguished cyclic quotient is not the original arithmetic system.

Two correct choices are to retain the full ambient tensor packets with their cyclic embeddings, or to include every transported cyclic generator R as a marked generator. A formal injection given by chi_h',k/chi_h,k between abstract cyclic quotients does not establish commutation with the actual observation.

For general h, additive root collisions also determine the cyclic annihilator exactly. Write h=product_rho(s−rho)^(r_rho). For a tuple boldrho, the sum nilpotent has index

\[
L_{\boldsymbol\rho}=1+\sum_i(r_{\rho_i}-1).
\]

Indeed the term of top degree sum_i(r_rhoi−1) is the nonzero monomial product_i z_i^(r_rhoi−1) with coefficient (sum_i(r_rhoi−1))!/product_i(r_rhoi−1)!, and every term of the next degree is zero. For each distinct sum lambda, the nilpotence order in the cyclic generator is the maximum of L_boldrho over all tuples with that sum. Thus

\[
\chi_{h,k}(S)=\prod_{\lambda\in\{\sum_i\rho_i\}}
(S-\lambda)^{\max_{\sum_i\rho_i=\lambda}L_{\boldsymbol\rho}}.
\tag{AR12}
\]

This uses a maximum, not a sum over colliding tuples. The full ambient tensor still contains every tuple block. In a complete quartet of common order m it reduces to the already proved rectangular grid and exponent 1+k(m−1), because the real and imaginary coordinates distinguish the grid points and all tuple nilpotence indices are equal.

## 5. The finite source metrics must remain filtered

For a fixed h,k, pull back (AR6) to each finite polynomial subspace. For the canonical sum source this is the actual form

\[
\langle P,Q\rangle_{h,k}
=\int_\mathbb R\overline{P(k/2+iu)}Q(k/2+iu)m_{h,k}(u)\,du.
\]

The degree cutoff N and the literal remainder map determine H_N,K_N,G_N,R_N uniquely by the proved inverse-Gram formulas. These form one filtered measured representation. Degrees, full relation kernels, canonical lifts, and the differences between lifts must remain visible; taking an unqualified limit or identifying the metrics at different degrees discards arithmetic data.

There is a precise reason a Hilbert quotient is not an acceptable total object. The ideal chi C[S] is dense in the completed source L²(m_h,k), provided the original exponential moments hold, as they do here. To prove this, let f be orthogonal to that ideal. The complex measure

\[
d\nu(u)=\overline{f(u)}\chi(k/2+iu)m_{h,k}(u)\,du
\]

has an exponential moment in a nonzero strip: Cauchy–Schwarz bounds its integral with exp(b|u|) by ||f|| times the square root of integral |chi|²exp(2b|u|)m_h,k, finite for sufficiently small b>0. Orthogonality makes all polynomial moments of nu zero. Its Fourier–Laplace transform is holomorphic on that strip, every derivative at zero vanishes, and hence the identity theorem and Fourier uniqueness give nu=0. Since chi is nonzero except at finitely many real ordinates and m_h,k is positive almost everywhere, f=0. This proves density.

Consequently the quotient by the *closed* relation subspace is zero even when the finite algebraic quotient E is nonzero. Completing first and then killing the closed relation space would erase every finite arithmetic packet; it would not be an RH contradiction. The measured algebraic source and each finite minimum problem avoid that collapse.

## 6. What must be internal, and what the assembled object can decide

The following are properties already forced by the construction and its proved maps; they must not be appended as new admissibility assumptions:

- The density is exactly |(2xi)/h|²/(2pi), its k-fold convolution retains mass mu_h^k, and both Gamma comparisons have their original distinct masses. All Gram matrices are the integrals of these fixed functions.
- Every h is an actual divisor with its specified order. Complete-order charts have the proved Taylor unit, and partial charts use (AR7). The analytic unit in g=u z^m is never silently replaced by its constant term.
- The top-cohomology observation is the actual quotient of the original tensor theta complex. A relation is accompanied by its explicit theta primitive and lands at the supported zero in the same label. K and the diagonal are retained through (AR1).
- Primitive D, actual dilation, the reflected dual character, all nilpotent terms, the residue pairing, and the derivative trace are the previously proved operations on those exact spaces. The actual dilation need not equal scalar a^s on all of M; their difference takes values in K.
- The arithmetic tail bounds, full Gram inequalities, original trace floors, exact contraction penalties, crossed-pair angle constraints, and compulsory old-reference spectral spread are consequences for the indicated complete quartet subobjects. They are not free inequalities defining a larger surrogate set of possible matrices.
- No positive weight-one polarization, self-adjointness of the finite arithmetic action, vanishing of a source boundary, or uniform bounded condition number is inserted. Such an insertion would replace the mathematics required for an RH contradiction.

The coherent offcritical quotient N_U is the distinguished obstruction *inside* the total realization. The entire total realization is already defined from g and the original Schwartz spaces, whether or not N_U vanishes. K is nonzero independently of RH, and the diagonal also persists. Thus neither nonvanishing of the total object nor failure of one comparison proves RH false; conversely its existence cannot contradict a hypothetical zero. To obtain a contradiction one must prove that its distinguished actual N_U must vanish using the internal structure; to disprove RH one must construct a nonzero actual local block or a certified zero of g in U. The present assembly retains the available restrictions and obstructions but does not supply either missing conclusion.

## 7. Recommended presentation and exact scope

Use the single marked dg source (AR4), its measured top cochains, and its actual coherent universal arrow (AR1) as the anchor. All finite packets are the specified polynomial images of its canonical marked elements F_h, and all finite metrics are restrictions/minima of one original source form. If a category presentation is desired, its generators are exactly these source inclusions, tensor maps, polynomial actions, divisor multiplications, quotient maps, sheaf restriction/balancing maps, and coherent observation; its relations are the concrete equalities proved above and in the retained source. The representation is determined by the one original theta complex and its Mellin realization, together with the fixed g and L² integral. A map out of this envelope is determined by its map on the original measured complex and must preserve the displayed marked maps; the tensor and coherent universal properties (AR3)–(AR5) prove the uniqueness statements.

Do not claim a free universal property for all metrics or arbitrary forms: the integral is fixed data, and only maps preserving that specified data belong to the structured morphism class. Likewise do not claim that an ordinary O_U tensor algebra alone contains independent tensor spectra. The resulting object is one structured realization whose charts, extensions, and restrictions are recovered by actual morphisms, rather than a product of independent proposed RH criteria.

Source coverage in this bounded review: fully read OCQ.1–35 (585 lines); fully read DP.1–8; read DC.17–23 and its full adjacent proofs (lines 274–418); read BK.1–4 and BK.10–11, with earlier original full source audits available. The current review reuses the independently checked arithmetic-tail, Gram, angle, and cochain modules documented in `continuation2/arithmetic_tail_review/FINAL_REVIEW.md`. It does not claim a new complete audit of every source dependency.
