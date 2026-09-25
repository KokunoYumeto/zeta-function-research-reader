# Equivariant full-source return and the exact mixed tensor class

25 September 2026. Independent verification and derivation FEM0–FEM10.

## FEM0. Scope, sources and exact operation domains

This note independently verifies the full derived coefficient comparison in [FSC6](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260925-full-source-tensor-and-original-divisor/counterfactual/DERIVED_RETURN_FULL_SOURCE_CORRESPONDENCE.md), then calculates the operator structure it transports. It also constructs a particular connecting class in the actual mixed tensor row of [DER7–DER9](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260925-full-source-tensor-and-original-divisor/counterfactual/DIAGONAL_EXTRAORDINARY_RETURN.md). That row is not silently identified with the original \(\tau\) specialization map or with Deligne's support cross.

The spaces and morphisms remain
\[
X=U\cup\{\mathfrak m_+,\mathfrak m_-\},\quad U=\operatorname{Spec}\mathbb Z,
\quad f:X\to Y=\{c_+,c_-,\eta\},
\]
\[
q:Y^2\to Y,\qquad q(++ )=c_+,\quad q(--)=c_-,
\quad q=\eta\ \text{at the other seven points},
\]
\[
\mathcal Z=\{(x,y,z):f(z)=q(f(x),f(y))\},\quad
a(x,y,z)=(x,y),\quad b(x,y,z)=z,
\]
\[
v=q(f\times f):X^2\to Y,\qquad g=fb=va:\mathcal Z\to Y.
\]
The complete topology, fibre descriptions and nonexistence of a particular single-valued lift were verified in FSC0–FSC5. No such single-valued map is used below.

The coefficient construction is the original Connes–Consani diagram and its source-faithful extension, as proved in [DCP](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/original-character-lifting/tau_lifting_weights_20260924/SOURCE_CC_DOUBLE_PULLBACK.md). Human sources remain Alain Connes and Caterina Consani, [*Schemes over \(\mathbb F_1\) and zeta functions*, arXiv:0903.2024v3, §5](https://arxiv.org/abs/0903.2024v3), and Ralf Meyer, [*A spectral interpretation for the zeros of the Riemann zeta function*, arXiv:math/0412277v3](https://arxiv.org/abs/math/0412277v3), with the full original-zeta comparison in [OMS](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/original-character-lifting/tau_lifting_weights_20260924/ORIGINAL_MELLIN_SPECTRAL_SYNTHESIS.md). Deligne's distinct lifting cross, with its precise twists and weight inequalities, is recorded from his original [*La conjecture de Weil. II*, §3.6](https://www.numdam.org/item/PMIHES_1980__52__137_0/) in [ORE7](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/original-character-lifting/tau_lifting_weights_20260924/ORIGINAL_RESTRICTION_EXTENSION_AND_DELIGNE_CROSS.md).

The complete corrected \(Z_0,Z_1/\tau,Z_2\) definitions and corpus rules (private construction record; not distributed) remain controlling. No source addition, parity, count or weight is assigned to primitive \(\tau\). Polynomial operations occur only in the stated receiving coefficient modules. Every tensor product in the new finite-support argument is algebraic. No inference about a completed tensor product is made.

## FEM1. Verification of the canonical derived unit

Let \(o=(0)\in U\) be the arithmetic generic point. Every nonempty open of \(U\) contains \(o\); the only opens of \(X\) additionally containing \(\mathfrak m_\pm\) contain all of \(U\). Hence every nonempty open of \(X\) contains \(o\). A nonempty product-open neighbourhood in \(X^n\) consequently contains \((o,\ldots,o)\).

The point \((o,o,o)\) belongs to \(\mathcal Z\). If a relative open of \(\mathcal Z\) is nonempty, choose one of its points and an ambient product-open neighbourhood contained in the ambient open defining it. That neighbourhood contains the generic triple, which is also in \(\mathcal Z\). Thus every nonempty open of \(\mathcal Z\) contains that same generic triple. Every nonempty open of \(X^2\) likewise contains \((o,o)\). Any two nonempty opens of either space intersect. Therefore the sheaf of locally constant functions into a vector space \(V\), with \(V\) viewed as a discrete coefficient set, has exactly \(V\) as its sections on every nonempty open: different local values cannot occur on overlapping nonempty opens. It is the point direct image \(i_*V\) from the specified generic point.

For any point inclusion \(i_x\), not just a closed point,
\[
\operatorname{Hom}(\mathcal H,i_{x*}V)
=\operatorname{Hom}_k(\mathcal H_x,V).
\]
The stalk functor is exact, and the vector-space dual-valued Hom on the right is exact in \(\mathcal H_x\): a map out of a subspace extends after choosing a vector-space complement. Thus \(i_{x*}V\) is an injective object of the algebraic category of sheaves of \(k=\mathbb C\) vector spaces.

Retain the evaluation injectives on \(Y\):
\[
I_\eta(V)=(V\xrightarrow1V\xleftarrow1V),\quad
I_+(V)=(V\to0\leftarrow0),\quad
I_-(V)=(0\to0\leftarrow V).
\]
The inverse images of \(I_\eta(V)\) by \(v\) and \(g\) are the generic-point constant sheaves just computed. The inverse images of \(I_\pm(V)\) are the closed skyscrapers at
\[
(\mathfrak m_\pm,\mathfrak m_\pm)\in X^2,\qquad
(\mathfrak m_\pm,\mathfrak m_\pm,\mathfrak m_\pm)\in\mathcal Z.
\]
These fibre points are closed. The assertion is a sheaf isomorphism: the adjunction to the indicated point direct image is identity on that stalk, and both sheaves have zero stalks elsewhere.

All three inverse-image types on \(\mathcal Z\) are therefore injective. Their direct images along \(a\) equal the corresponding inverse images on \(X^2\). For a nonempty open \(O\subset X^2\), its inverse image under \(a\) is nonempty because \(a\) is onto, and constant sections are \(V\), with identity restriction. For either skyscraper, the two point-inclusion composites through \(a\) are literally equal. The canonical unit is identity under these descriptions, and all higher direct images vanish for these injectives.

For a receiving sheaf
\(\mathcal G=(V_+\xrightarrow{s_+}B\xleftarrow{s_-}V_-)\), the full functorial resolution is
\[
0\to\mathcal G\to
I^0\mathcal G:=I_\eta(B)\oplus I_+(V_+)\oplus I_-(V_-)
\xrightarrow{\delta}
I^1\mathcal G:=I_+(B)\oplus I_-(B)\to0.
\tag{FEM1.1}
\]
Its closed components are \(x\mapsto(s_\pm x,x)\) and
\((b,x)\mapsto b-s_\pm x\); at \(\eta\) the augmentation is identity and the target is zero. These formulas prove exactness, functoriality, and compatibility with every restriction.

Applying \(g^{-1}\) to FEM1.1 gives an injective resolution of \(g^{-1}\mathcal G\). Applying \(a_*\) to it gives, term by term and with the same maps, \(v^{-1}\) of FEM1.1. Thus the canonical unit is a quasi-isomorphism
\[
\boxed{\eta_{\mathcal G}:v^{-1}\mathcal G
 \xrightarrow{\ \simeq\ }Ra_*g^{-1}\mathcal G.}
\tag{FEM1.2}
\]
This proves FSC6 in the specified category.

For a bounded complex \(\mathcal G^\bullet\), the explicit total complex is
\[
T^n=I^0(\mathcal G^n)\oplus I^1(\mathcal G^{n-1}),\qquad
d_T(x,y)=(I^0(d_{\mathcal G})x,\ \delta x-I^1(d_{\mathcal G})y).
\tag{FEM1.3}
\]
Functoriality gives \(\delta I^0d=I^1d\,\delta\), hence \(d_T^2=0\). The augmentation is a quasi-isomorphism by the exact two-term columns, and the complex is bounded with injective terms after \(g^{-1}\). The same termwise unit proves FEM1.2 for this full complex. No degree or sign is omitted.

## FEM2. A continuous section and faithful transport of actual morphisms

There is a continuous section
\[
i:Y\to X,\qquad i(\eta)=o,\quad i(c_\pm)=\mathfrak m_\pm
\]
of \(f\). To prove continuity, a nonempty open of \(X\) contained in \(U\) has inverse image \(\{\eta\}\); \(X_\pm\) has inverse image \(U_\pm\); and the empty and full opens have their corresponding inverse images. These are all opens of \(X\).

Consequently
\[
\ell=(i\times i)\Delta_Y:Y\to X^2,\qquad v\ell=\operatorname{id}_Y.
\tag{FEM2.1}
\]
Inverse image is exact and its composition isomorphism gives
\[
\ell^{-1}v^{-1}=\operatorname{id}
\]
on sheaves and on their bounded derived categories. Thus \(v^{-1}\) has a specified left inverse on morphisms. If a derived morphism \(\alpha\) becomes zero after \(v^{-1}\), applying \(\ell^{-1}\) gives \(\alpha=0\). Together with FEM1.2, this proves split faithful transport of morphisms from the stated receiving category through the correspondence.

The section selects the original generic point solely to construct this left inverse. It does not replace any fibre \(U\), identify distinct arithmetic primes, or construct a map \(X^2\to X\) satisfying the impossible requirements in FSC2. Both the full fibres and the specified section remain present.

In particular, a supplied exact coefficient sequence and its connecting morphism are transported with their full maps. A splitting after \(v^{-1}\) of an extension from \(Y\) would pull back by \(\ell^{-1}\) to a splitting of that extension. Thus nonvanishing of an existing extension class in this category is not changed by merely renaming it as a source-correspondence return.

## FEM3. The exact operator and source actions transported

Let an operator \(T\) be an endomorphism of a sheaf or a bounded sheaf complex on \(Y\). Functoriality of FEM1.1 makes every square with \(T\), \(\delta\), \(g^{-1}\), \(a_*\), and \(v^{-1}\) commute. Hence
\[
\eta_{\mathcal G}\,v^{-1}T
=(Ra_*g^{-1}T)\,\eta_{\mathcal G}.
\tag{FEM3.1}
\]
The same proof applies simultaneously to any supplied family of commuting operators and to every relation between their products. No averaging or newly assumed semisimplicity is required.

For the full original coefficient sheaf, these include all real dilations
\[
T_a b(u)=b(u/a),\qquad
\rho_+(a)(h,c_0,c_1)=(h(\cdot/a),c_0,ac_1),
\]
\[
\rho_-(a)(h,d_0,d_1)=(a h(a\cdot),ad_0,d_1),
\tag{FEM3.2}
\]
with the same actions on the complete extra closed copies. They intertwine \(r_\pm\) and \(T_a\). Every original prime operator is the actual substitution \(a=p\).

The supplied source action is separate:
\[
[\tau](v,w)=(v,w),\qquad [n](v,w)=(nv,0)
\]
at the full closed stalk, and \([n]b=nb\), \([\tau]b=b\) at the arithmetic coefficient stalk. It satisfies the supplied source multiplication and the supplied integer-layer addition, while preserving the distinction between \(\tau\) and integer \(1\) on the extra component. Naturality transports these exact endomorphisms as well. On a tensor product, the two source-factor actions remain separate; a simultaneous integer action has generic scalar \(n^2\). Spectral simultaneous dilation has the different factor \(a\) on the residue target. No equality of those actions is inserted.

The chart mirror also has an exact source return. Let \(\sigma:X\to X\) exchange \(\mathfrak m_+,\mathfrak m_-\) and fix \(U\), and let \(w\) exchange the two closed points of \(Y\). The equality
\[
q(w\times w)=wq
\]
follows at the two equal corners and at each of the other seven points. Thus
\(\sigma_{\mathcal Z}(x,y,z)=(\sigma x,\sigma y,\sigma z)\) preserves \(\mathcal Z\), intertwines \(a,b,g,v\), and intertwines the section \(\ell\). These are homeomorphisms with inverse themselves. The inverse-image and direct-image comparison for these homeomorphisms is the termwise identification on the same inverse-image opens, so FEM1.2 respects the supplied mirror maps.

The unshifted operator relation is retained:
\[
T_aR=aRT_{a^{-1}},\qquad M_0Rb(s)=M_0b(1-s).
\tag{FEM3.3}
\]
No \(a^{-1/2}\) modification is made. On a two-factor coefficient it becomes
\((T_a\otimes T_a)(R\otimes R)
=a^2(R\otimes R)(T_{a^{-1}}\otimes T_{a^{-1}})\).
The original residue pairing transforms to its companion denominator, not automatically to itself:
\[
B_\zeta(Rx,Ry)=B_\zeta(y,x)=-B_{\zeta^\vee}(x,y),
\quad \zeta^\vee(s)=\zeta(1-s).
\tag{FEM3.4}
\]
The first equality is substitution in the original integrand, and the second is the already proved reflected contour orientation. Both companion maps are transported by FEM3.1.

For a finite-dimensional actual coefficient subquotient with generator \(L\), FEM3.1 intertwines each polynomial in \(L\), every full generalized eigenspace, and its nilpotents. A chosen union of primary factors is a polynomial projector by Bézout applied to the finite minimal polynomial. The same polynomial therefore transports its exact image and kernel. This transports an existing finite numerical weight truncation; it does not prove a previously unknown bound on its characters.

## FEM4. The actual mixed tensor row and its embedding

Retain the raw generator
\[
L_A=-u\frac{d}{du},\qquad M_0L_Aa(s)=sM_0a(s).
\tag{FEM4.1}
\]
Integration by parts proves the second identity: the boundary term
\(u^sa(u)\) vanishes at both ends for every fixed \(s\), by the defining rapid bounds of \(A\). The operator preserves \(A\), \(J\), and the original quotient \(Q\). On tensors write
\[
L_{\rm tot}=L\otimes1+1\otimes L.
\]
The exact algebraic tensor row is
\[
0\to M=(J\otimes Q)\oplus(Q\otimes J)
\longrightarrow Q_\Delta=(A\otimes A)/(J\otimes J)
\xrightarrow{\vartheta}Q\otimes Q\to0.
\tag{FEM4.2}
\]
All its maps were constructed in DER8. Its generator and simultaneous dilation are the actual tensor actions; its source scalar actions are those of FEM3.

There is the following further exact injection:
\[
\iota:Q_\Delta\longrightarrow(Q\otimes A)\oplus(A\otimes Q),
\quad
[a\otimes b]\longmapsto([a]\otimes b,\ a\otimes[b]).
\tag{FEM4.3}
\]
It is well defined because \(J\otimes J\) maps to zero in both coordinates. Before the quotient its kernel is
\((J\otimes A)\cap(A\otimes J)=J\otimes J\), proved by a vector-space complement of \(J\). Therefore it is injective. Every original operator in FEM3 and the generator commute with this map. No direct-product presentation of all zeta jets has been substituted for \(Q\).

## FEM5. Finite tensor support and the actual absence of finite characters in Q_Delta

Here is the needed algebraic tensor statement with its proof. Let \(U,V\) be vector spaces with operators \(L_U,L_V\), and let
\(W\subset U\otimes V\) be finite-dimensional and invariant under
\(L_U\otimes1+1\otimes L_V\). Define \(V_0\) to be the span of all slices
\[
(\phi\otimes1)w,\qquad \phi\in U^*,\ w\in W .
\]
It is finite-dimensional because a basis of \(W\) consists of finite sums of simple tensors. It is the smallest subspace for which \(W\subset U\otimes V_0\).

Let \(\pi_0:V\to V/V_0\). For \(w\in W\), both
\((1\otimes\pi_0)(L_U\otimes1)w\) and
\((1\otimes\pi_0)(L_U\otimes1+1\otimes L_V)w\) vanish. Their difference is
\((1\otimes\pi_0L_V)w=0\). Applying every \(\phi\) shows \(L_VV_0\subset V_0\). Interchanging the factors proves the corresponding assertion for the finite left support. Therefore a nonzero finite-dimensional invariant tensor space requires a nonzero finite-dimensional invariant space in both factors.

There is also a group version. If \(W\) is invariant under simultaneous invertible actions \(T_g\otimes S_g\), its finite right support satisfies \(S_gV_0=V_0\): the right support of \((T_g\otimes S_g)W=W\) is exactly \(S_gV_0\), since \(T_g\) is invertible. The left support is likewise invariant.

The actual space \(A\) has no nonzero finite-dimensional \(L_A\)-invariant subspace. If it had one, the restriction of \(L_A\) to that complex vector space would have an eigenvector \(a\ne0\), with
\(-ua'(u)=\lambda a(u)\). Differentiating \(u^\lambda a(u)\) gives zero, hence
\(a(u)=c u^{-\lambda}\). The function belongs to \(A\) only if \(c=0\): for an integer \(N>\Re\lambda\), \(u^N|a(u)|\) is unbounded as \(u\to\infty\) when \(c\ne0\). This contradicts the chosen eigenvector.

For clarity, a fixed actual prime operator also has no nonzero finite-dimensional invariant subspace in \(A\). Any such space would contain an eigenvector \(T_pa=c a\). Since \(T_p\) is injective on \(A\), \(c\ne0\). Iterating \(a(u/p)=c a(u)\) gives \(a(p^nu)=c^{-n}a(u)\). Choosing \(N\) with \(p^N>|c|\), the defining bound for \(u^Na(u)\), applied at \(p^nu\), forces \(a(u)=0\) for every \(u\). This contradiction proves the fixed-prime assertion too.

Apply the tensor-support result to the two summands in FEM4.3. Neither \(Q\otimes A\) nor \(A\otimes Q\) has a nonzero finite-dimensional \(L_{\rm tot}\)-invariant subspace. Projection of an invariant subspace of their direct sum to either summand is again finite and invariant, so both projections vanish. The injection FEM4.3 therefore proves
\[
\boxed{(Q_\Delta)_{\rm finite\ character}=0.}
\tag{FEM5.1}
\]
Here the notation means the union of finite-dimensional invariant subspaces for the specified generator. It is a receiving-algebra definition, not the user's source integer-amount datum.

In particular, for every nonzero polynomial \(q(X)\),
\[
\ker(q(L_{\rm tot}):Q_\Delta\to Q_\Delta)=0.
\tag{FEM5.2}
\]
Indeed a vector killed by a polynomial of degree \(r\) has its \(L_{\rm tot}\)-orbit in the span of its first \(r\) iterates; this is a finite-dimensional invariant space. The constant-polynomial case is immediate. The same assertions hold for \(M\subset Q_\Delta\), and the fixed-prime tensor argument gives the analogous injectivity for polynomials in \(T_p\).

This proof uses finite tensor supports at its first step. Completed tensors can have infinite rank, so no conclusion about them follows from FEM5.1.

## FEM6. The resulting exact connecting map

Apply \(q(L_{\rm tot})\) to FEM4.2. For \(v\in\ker q(L_{\rm tot})\subset Q\otimes Q\), choose a lift \(e\in Q_\Delta\). Then \(q(L_{\rm tot})e\in M\), and define
\[
\delta_q(v)=[q(L_{\rm tot})e]\in M/q(L_{\rm tot})M.
\tag{FEM6.1}
\]
Changing \(e\) by \(m\in M\) changes this representative by \(q(L_{\rm tot})m\), so it is lift independent. This is the actual connecting map of the two-term complexes \([\,\cdot\xrightarrow q\cdot\,]\), not an assumed extension class.

It is injective. If its value is zero, write \(q e=q m\) for some \(m\in M\); then \(q(e-m)=0\) in \(Q_\Delta\). FEM5.2 gives \(e=m\), hence \(v=\vartheta(e)=0\). More completely, the exact sequence starts
\[
0\to\ker(q:Q\otimes Q\to Q\otimes Q)
 \xrightarrow{\delta_q}M/qM
 \longrightarrow Q_\Delta/qQ_\Delta
 \longrightarrow (Q\otimes Q)/q(Q\otimes Q)\to0.
\tag{FEM6.2}
\]
Exactness of the subsequent maps follows directly by lifting representatives through the surjection \(\vartheta\).

Every simultaneous dilation \(T_a\otimes T_a\) commutes with \(q(L_{\rm tot})\), so choosing its action on a lift in FEM6.1 proves \(\delta_q\) intertwines every real and prime operator. It likewise intertwines the supplied independent source scalar actions.

Let \(\mathcal R=R\otimes R\) be the raw coefficient mirror. Then
\(L_{\rm tot}\mathcal R=\mathcal R(2-L_{\rm tot})\).
For \(q(X)=(X-\lambda)^r\), put \(q^\vee(X)=(X-(2-\lambda))^r\). Direct multiplication gives
\[
q^\vee(L_{\rm tot})\mathcal R
=(-1)^r\mathcal R q(L_{\rm tot}),
\]
hence the exact mirror comparison of connecting maps is
\[
\delta_{q^\vee}(\mathcal Rv)
=(-1)^r\mathcal R\,\delta_q(v).
\tag{FEM6.3}
\]
The full sign is retained. This is an action statement on the actual tensor row.

## FEM7. A complete representative at actual original-zeta primary blocks

Choose actual nontrivial zeros \(\rho,\sigma\) of the original \(\zeta\), with multiplicities \(m,n\). Let \(E_{\rho,0}\), \(E_{\sigma,0}\) be the entire original Mellin isolators already constructed by [RZ](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/gct-weight-control/proofs/ORIGINAL_ZETA_RESOLVENT_AND_PROJECTORS.md): each has jet \(1\) at its named primary block and all jets zero at every other zero. Set
\[
a_\rho=M_0^{-1}E_{\rho,0},\qquad
a_\sigma=M_0^{-1}E_{\sigma,0}\in A,
\quad x_\rho=[a_\rho],\quad x_\sigma=[a_\sigma]\in Q.
\tag{FEM7.1}
\]
These are explicitly unshifted representatives. They are not the earlier representatives whose unshifted Mellin transform is \(2E\); no factor four is hidden in the two-factor expression.

Retain
\[
u_k=(L_A-\rho)^k a_\rho,\qquad
v_l=(L_A-\sigma)^l a_\sigma,\qquad
\lambda=\rho+\sigma,\qquad r=m+n-1.
\]
For \(k\geq m\), \(u_k\in J\), and for \(l\geq n\), \(v_l\in J\). Indeed their original Mellin transforms are
\((s-\rho)^kE_{\rho,0}(s)\) and
\((s-\sigma)^lE_{\sigma,0}(s)\), which have every required original-zero jet equal to zero; the exact global image theorem OMS puts them in \(J\). All nontrivial-zero multiplicities, and the original Mellin return's endpoint and Gamma terms, remain those of that theorem.

On the actual primary tensor \(Q_\rho\otimes Q_\sigma\), the nilpotent part of \(L_{\rm tot}-\lambda\) is
\(N_\rho\otimes1+1\otimes N_\sigma\). Its \(r\)-th power is zero, while its \((r-1)\)-st power on \(x_\rho\otimes x_\sigma\) is
\[
\binom{m+n-2}{m-1}\,
N_\rho^{m-1}x_\rho\otimes N_\sigma^{n-1}x_\sigma\ne0.
\tag{FEM7.2}
\]
The binomial expansion proves both statements; the displayed tensor is nonzero because both primary top jets are nonzero. Thus the original tensor retains its exact maximal nilpotent length.

For \(q(X)=(X-\lambda)^r\), expand on its actual lift:
\[
q(L_{\rm tot})(a_\rho\otimes a_\sigma)
=\sum_{k=0}^{r}\binom rk u_k\otimes v_{r-k}.
\tag{FEM7.3}
\]
If \(k\geq m\), the first factor belongs to \(J\); if \(k<m\), then \(r-k\geq n\), so the second belongs to \(J\). Under the exact mixed-subspace identification, the complete representative in FEM6.1 is therefore
\[
\boxed{
\delta_q(x_\rho\otimes x_\sigma)=
\left[
\left(
 \sum_{k=m}^{r}\binom rk u_k\otimes[v_{r-k}],
 \quad
 \sum_{k=0}^{m-1}\binom rk [u_k]\otimes v_{r-k}
\right)
\right]\in M/qM.}
\tag{FEM7.4}
\]
Every binomial coefficient, exponent and original representative has been retained. The class is nonzero by FEM6.1's injectivity and the nonzero input tensor. Its lift independence was proved there; no particular choice of entire isolators is made part of its definition.

The full prime action on the finite tensor is
\[
p^{\rho+\sigma}
 \sum_{a=0}^{m-1}\sum_{b=0}^{n-1}
 \frac{(\log p)^{a+b}}{a!\,b!}\,
 N_\rho^a\otimes N_\sigma^b.
\tag{FEM7.5}
\]
FEM6 equivariance transports exactly this matrix to the connecting class. Its numerical character weight is \(2\Re(\rho+\sigma)\), with all nilpotents unchanged. For the reflected pair \(\sigma=1-\rho\), the character is \(p\) and this weight is two regardless of whether either zero is on the critical line. Thus these classes can be nonzero even when RH holds. They are not counterexamples to RH or a contradiction in the source definitions.

## FEM8. Its exact place in the full global returned complex

The generic connecting class must also be returned through the full sheaf of DER, not used as a substitute for it. Write
\[
G=R^1q_*(F\boxtimes F),\qquad
G_\pm=(W_\pm\otimes Q)\oplus(Q\otimes W_\pm),\qquad
G_\eta=Q_\Delta.
\]
The actual global complex is
\[
[\,G_+\oplus G_-\xrightarrow{d_G=\sigma_+-\sigma_-}Q_\Delta\,],
\quad
\sigma_\pm(u,v)=-(r_\pm\otimes1)u+(1\otimes r_\pm)v.
\tag{FEM8.1}
\]
Its image is \(M\). The original summation is a topological isomorphism \(S\to J\), so its actual section into the full plus stalk is
\[
s_+(j)=(\Sigma^{-1}j,0,0,0_{\rm extra})\in W_+,\qquad r_+s_+=\operatorname{id}_J.
\]
It is continuous and intertwines all real dilations and the supplied source scalars, by the original restriction identities and uniqueness of \(\Sigma^{-1}\).

For \(m=(m_1,m_2)\in(J\otimes Q)\oplus(Q\otimes J)\), define
\[
S(m)=
\bigl(- (s_+\otimes1)m_1,\ (1\otimes s_+)m_2;\ 0,0\bigr)
\in G_+\oplus G_- .
\tag{FEM8.2}
\]
Both signs are forced by FEM8.1. Substitution proves \(d_GS(m)=m\). It intertwines \(L_{\rm tot}\) and every simultaneous dilation. As this section chooses the plus chart, no mirror invariance of that particular section is asserted.

For the representative \(m=q(L_{\rm tot})e\) of FEM6, the identity
\[
q(L_{\rm tot})e=d_GS(m)
\tag{FEM8.3}
\]
is its exact cancellation by a global boundary in the complete complex. It does not give a finite-character lift inside the single generic stalk \(Q_\Delta\); it constructs the required other cochain component.

More completely let \(K_0=\ker d_G=(H\otimes Q)\oplus(Q\otimes H)\). There is an equivariant algebraic quasi-isomorphism
\[
[\,G_+\oplus G_-\xrightarrow{d_G}Q_\Delta\,]
 \longrightarrow K_0[0]\oplus(Q\otimes Q)[-1]
\tag{FEM8.4}
\]
whose degree-zero map is \(p_0=\operatorname{id}-Sd_G\), with \(d_G\) regarded as a map to its exact image \(M\), and whose degree-one map is \(\vartheta\). The first map lands in \(K_0\) because \(d_Gp_0=0\), and it is identity on \(K_0\). The chain identity follows from \(\vartheta d_G=0\). Its kernel is
\([S(M)\xrightarrow{d_G}M]\), and \(S\) is the inverse differential, so that kernel is contractible. These identities prove the quasi-isomorphism and retain the whole lower group \(K_0\).

This assertion is algebraic. Continuity of the displayed factor \(s_+\) does not by itself identify all subspace, quotient and completed-tensor topologies on \(M\) and \(Q_\Delta\); no such identification is needed for FEM8.4. Thus the generic class in FEM7 is explicitly not a global weight obstruction. The full global map and its exact boundary have both been calculated.

## FEM9. What the source return transports toward lifting

FEM1–FEM3 prove that the actual full-source correspondence transports existing sheaf complexes, their exact maps, source actions, all real and prime operators, companion mirror relations, and connecting classes. FEM2 supplies a left inverse on receiving derived morphisms. This is an exact coefficient comparison through the full arithmetic source, not a new purity assumption.

FEM4–FEM7 calculate the finite-character defect of one actual intermediate generic row, with an injective connecting map and its full original-zeta representative. FEM8 then calculates its different behaviour in the complete returned global complex: the exact section \(S\) supplies the global boundary, and the quotient is the full \(Q\otimes Q\), with all lower cohomology retained. This is why a generic nonzero extension class must not be promoted to a global or source obstruction.

The finite numerical characters are preserved throughout, including \(p^\rho\), every \(\log p\) nilpotent coefficient, the reflected character \(p^{1-\rho}\), and the product character \(p\). The demonstrated transport and global cancellation do not alone impose \(2\Re\rho=1\). The distinction from Deligne's actual exact weight truncation is given by these explicit maps: extracting finite-character vectors is not exact on FEM4.2, whereas the full global complex contains the additional boundary that cancels its connecting class. No claim about completed tensors, an unconstructed Frobenius action, a primitive weight on \(Z_1/\tau\), or the truth or falsity of RH is made.

## FEM10. Independent verification of the full global contraction

The complete separate proof [GMC0–GMC7](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260925-full-source-tensor-and-original-divisor/counterfactual/GLOBAL_MIXED_RETURN_CONTRACTION.md) was read and checked against FEM8. Its summation inverse has the correct domain \(J\), and GMC2 derives equivariance using its injectivity on the original Schwartz summand. GMC3's first section component has the required minus sign, while its second has the required plus sign. Substitution gives \(d_MS=\operatorname{id}\) in both ordered summands of \(M\).

GMC4's surjective cochain map has the exact kernel \([S(M)\to\iota(M)]\), whose inverse differential is the displayed homotopy. Thus it is an equivariant quasi-isomorphism and retains both \(H\otimes Q\) and \(Q\otimes H\), including all endpoints and extra closed copies in \(H\). GMC5's boundary identity is exactly FEM8.3, so it is compatible with the nonzero generic class FEM7.4. It does not require that class to vanish in \(M/qM\). GMC6's residue map factors through the same \(\vartheta\) with coefficient \(+1\), and its prime matrix retains both full nilpotent series. No discrepancy in these formulas was found.

The category qualifications in GMC3–GMC7 are necessary and retained: the theorem concerns algebraic tensors and a global complex of coefficient vector spaces, and the chosen plus section is not asserted to preserve the mirror. FSC6 acts on bounded sheaf complexes; it does not automatically turn this global quasi-isomorphism into a sheaf splitting of \(G\). If this already global coefficient complex is itself supplied to FSC6 as a constant sheaf complex, the exact functor \(W\mapsto I_\eta(W)\) constructs that input and sends each displayed cochain map and homotopy to an actual sheaf map. This retains its global-coefficient type and makes no claim that the resulting constant sheaf is the original returned sheaf \(G\). The original sheaf-level return remains the separate DER/FSC calculation.


## Publication source and dependency links

The source geometry is Alain Connes and Caterina Consani, *Schemes over F1 and zeta functions*, [arXiv:0903.2024v3, §5](https://arxiv.org/abs/0903.2024v3). The weight-control comparison is Pierre Deligne, *La conjecture de Weil. II*, Publications mathematiques de l'IHES52 (1980),137-252, [§§3.3.11 and3.6](https://www.numdam.org/item/PMIHES_1980__52__137_0/). Deligne material was read through the identified French transcription and separately recorded peer source-page checks, not Deligne-authored TeX. These sources are not asserted to contain the new programme derivations. The [preceding complete proof and reading record](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/BUILD_AND_REVIEW.md) records inherited source versions and actual inspection limits. The investigator's corrected construction remains attributed in the original text above.
