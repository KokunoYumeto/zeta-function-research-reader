# Deligne mixed duality and the recovered arithmetic base

Independent derivation, 24 September 2026. Proof locators MDB0–MDB11.

## MDB0. Sources, scope, and distinct objects

The source is Pierre Deligne, [La conjecture de Weil. II](https://www.numdam.org/item/PMIHES_1980__52__137_0/), Publications Mathématiques de l'IHÉS 52 (1980), 137–252. Canonical disk-index records: PUBUNIT-3D90B487DBD1CC3A259C6455 and PUBUNIT-574B0214207BBB2BDABCFFF9. The available supplied reading witness is the French transcription [S20_FR_record_export.tex](https://www.numdam.org/item/PMIHES_1980__52__137_0/), SHA256 d6836ae15d98f2b27eb98c9bd039a7d921679becd9fa47ff4717410289dbd351. It is a transcription, not Deligne-authored TeX. Neither it nor its original page records have been edited.

Actual reading: §§6.1–6.2 in full, printed pp.243–251, TeX lines3427–3741, including all examples, proofs, and the added note. The §6.2.1–6.2.7 portion was reread without tool-output truncation. Weight conventions §§1.2.1–1.2.7, the local inertia statement §1.7.1, §§1.8.9–1.8.10 with their proofs, theorem and proof §3.3.1, and §§3.4.1–3.4.9 were also read. The existing DELIGNE_WEIGHT_SOURCE_READING.json and DELIGNE_FULL_READING_LOG.md were consulted first. No transfer of §§6.2.8–6.2.13 to the user's construction is asserted by this note.

For the supporting geometry, original-author source actually read: Alain Connes and Caterina Consani, [The Absolute Twistor Line and the Geometry of the compactified Spec Z](https://arxiv.org/html/2609.00299v1), local CC.tex, lines489–613 and773–902, together with the exact programme reconstruction CG1–CG4.

The input is the already reconstructed complete winding datum and arithmetic
\[
L=G/H,\qquad G\simeq\mathbb Z\times C_4,\quad H=\{0\}\times C_4,\qquad
R=\operatorname{End}_{\mathrm{Ab}}(L).
\tag{MDB0.1}
\]
No selected observed prime is an initial input. The supporting point remains
\[
\tau\langle Z_1;\text{no }Z_2\rangle.
\tag{MDB0.2}
\]
No arithmetic operation, coordinate, metric, or Frobenius is assigned to that point. Its supplied stalk data and the recovered ring have separately typed operations.

This note constructs the support, scheme, topos, and stalk maps that are actually available. It applies Deligne's formalism to schemes and sheaves in its domain; it does not manufacture an arithmetic scheme structure on the singleton support.

## MDB1. The recovered ring and its arithmetic base maps

For a cyclic generator \(u\) of the complete group \(L\), every endomorphism has the unique form
\[
[n](u^m)=u^{nm}.
\tag{MDB1.1}
\]
Replacing \(u\) by \(u^{-1}\) preserves both this endomorphism and its integer \(n\). Pointwise multiplication in \(L\) supplies endomorphism addition, and composition supplies multiplication:
\[
[m]+[n]=[m+n],\qquad [m][n]=[mn],\qquad
\mathbf1_R=\operatorname{id}_L=[1].
\tag{MDB1.2}
\]
Thus \(\mathbb Z\to R,\ n\mapsto[n]\), is a canonical unital ring isomorphism: (MDB1.1) proves bijectivity and (MDB1.2) proves preservation of operations. The identity endomorphism is not the supporting point.

Put \(\Sigma=\operatorname{Spec}R\). The ring isomorphism gives an isomorphism of schemes \(\Sigma\simeq\operatorname{Spec}\mathbb Z\), not only of point sets: inverse-image ideals identify points, and localization of the ring isomorphism identifies all structure-sheaf stalks. The generic stalk is \(\operatorname{Frac}R\simeq\mathbb Q\); the stalk at \(pR\) is \(R_{pR}\simeq\mathbb Z_{(p)}\), with residue field \(R/pR\simeq\mathbb F_p\). These are arithmetic-scheme stalks, not coordinates on \(\tau\).

Choose a coefficient prime \(\ell\) after this reconstruction and set
\[
S=\operatorname{Spec}R[1/\ell],\qquad
s_p=\operatorname{Spec}(R/pR),\quad
i_p:s_p\hookrightarrow S\ (p\neq\ell),\qquad E=\overline{\mathbb Q}_\ell.
\tag{MDB1.3}
\]
The map \(i_p\) is the proper finite closed immersion induced by reduction modulo \(p\). Its norm is the recovered quotient cardinality \(N(s_p)=p\). The omitted coefficient prime remains explicit in the original zeta:
\[
\zeta(s)=(1-\ell^{-s})^{-1}\prod_{p\neq\ell}(1-p^{-s})^{-1},
\qquad \operatorname{Re}s>1.
\tag{MDB1.4}
\]
Two distinct coefficient-prime opens cover \(\Sigma\), but their coefficient fields differ; the open cover alone does not glue their coefficient categories.

For a complete branch isomorphism \(B:L\to L'\),
\[
C_B:R\xrightarrow{\sim}R',\quad f\mapsto BfB^{-1},
\qquad
\operatorname{Spec}(C_B^{-1}):\Sigma\xrightarrow{\sim}\Sigma'
\tag{MDB1.5}
\]
are the actual arithmetic comparisons. The identity \(B(x^n)=B(x)^n\) proves \(C_B([n])=[n]\). Consequently the scheme map sends \(pR\) to \(pR'\), preserves residue fields and norms, and restricts to the coefficient opens. This construction is on the groupoid of branch isomorphisms; a general noninvertible homomorphism has not been declared to induce endomorphism conjugation.

In particular the source involution induces inversion on \(L\). Its conjugation is the identity on \(R\), hence on \(\Sigma\), every local ring, and every residue field. This computes its action on the recovered base without discarding its action on the retained source stalk.

## MDB2. Actual support and stalk maps in the CC geometry

The unfolded topological source is
\[
X=\{+,-,\eta\},\quad
\Omega_+=\{+,\eta\},\quad
\Omega_-=\{-,\eta\},\quad \Omega=\{\eta\}.
\tag{MDB2.1}
\]
Together with the empty and full opens these are its topology. The unique dense singleton is \(\{\eta\}\); therefore any homeomorphism fixes \(\eta\). The source involution exchanges \(+\) and \(-\).

Let \(T=\{\tau\}\), with its singleton topology. Identify its supporting role with the generic open by
\[
j_\tau:T\hookrightarrow X,\qquad j_\tau(\tau)=\eta.
\tag{MDB2.2}
\]
For a sheaf \(\mathcal F\) on \(X\),
\[
j_\tau^{-1}\mathcal F=\mathcal F_\eta=\mathcal F(\Omega).
\tag{MDB2.3}
\]
The stalk is the neighbourhood colimit, and \(\Omega\) is its least neighbourhood, proving the last equality.

On the supplied nonabsorbing monomial carrier the generic stalk is \(G\), with full chart restrictions
\[
\rho_+(T^mJ_+^k)=T^mJ^k,\qquad
\rho_-(T^mJ_-^k)=T^m(\epsilon J)^k.
\tag{MDB2.4}
\]
The separate source absorbing element remains outside this group. On the pointed multiplicative carrier it maps to the separate absorbing element, never to the supporting point.

Taking the specified monomial group, its finite-order subgroup, the quotient, and its endomorphisms gives
\[
j_\tau^{-1}\mathcal O\longmapsto
G\longmapsto(G,H,G/H)\longmapsto R\longmapsto\operatorname{Spec}R.
\tag{MDB2.5}
\]
The first step is the supplied nonabsorbing monomial carrier, not an equivalence between the whole spherical-algebra structure and a group. Both restrictions, the subgroup, quotient map, and phase data remain retained.

There is an actual continuous map
\[
c_\Sigma:|\Sigma|\to T,\qquad x\mapsto\tau.
\tag{MDB2.6}
\]
Continuity follows because the only opens of \(T\) are empty and full. Composing with \(j_\tau\) gives a continuous map \(|\Sigma|\to X\) with image \(\eta\). Every nonempty source open in (MDB2.1) has full preimage.

Its geometric morphism of topological sheaf topoi has
\[
c_\Sigma^{-1}M=\underline M_\Sigma,\qquad
c_{\Sigma,*}\mathcal F=\Gamma(\Sigma,\mathcal F),
\tag{MDB2.7}
\]
where the underline means the sheaf associated to the constant presheaf. The adjunction is the constant-presheaf/sheafification adjunction; inverse image preserves finite limits. Global sections form a value attached to the support, not arithmetic on the point. These are topos maps, not scheme maps to an unspecified \(\operatorname{Spec}(\tau)\).

The parity statement is also exact. Let \(Q_2=\{\mathrm{even},\mathrm{odd}\}\) with fixed-point-free exchange \(\sigma\). Equivariance of a point-label means \(P(\alpha x)=\sigma P(x)\). At \(\eta\) it would require \(P(\eta)=\sigma P(\eta)\), impossible. The nontrivial stalk (MDB2.4) and its action remain present.

## MDB3. Étale topoi, arithmetic Frobenius, and geometric stalks

The recovered scheme has the canonical geometric morphism
\[
\epsilon_S:S_{\mathrm{\acute et}}\to S_{\mathrm{Zar}}.
\tag{MDB3.1}
\]
Its direct image satisfies \((\epsilon_{S,*}\mathcal F)(U)=\mathcal F(U)\) for a Zariski open \(U\), regarded as an étale scheme over \(S\); inverse image is the associated extension to the étale site. Composing with the support map gives
\[
\pi_\tau:S_{\mathrm{\acute et}}\to\operatorname{Sh}(T)\simeq\operatorname{Sets},
\qquad
\pi_{\tau,*}\mathcal F=\Gamma(S_{\mathrm{\acute et}},\mathcal F).
\tag{MDB3.2}
\]
For abelian coefficients the derived direct image is étale derived global sections. This construction has not supplied a residue norm or arithmetic Frobenius at \(T\), or made \(T\) an arithmetic scheme to which Deligne's exceptional inverse image applies.

For each \(p\neq\ell\), choose a geometric point
\[
\overline s_p=\operatorname{Spec}\overline{\mathbb F}_p\to s_p\to S.
\tag{MDB3.3}
\]
For an ordinary or finite-coefficient étale sheaf, its inverse-image functor is the actual stalk
\[
\mathcal F\longmapsto\mathcal F_{\overline s_p}
=\underset{(U,\overline u)}{\operatorname{colim}}\mathcal F(U),
\tag{MDB3.4}
\]
over étale neighbourhoods with a lift of the specified geometric point. For an \(\ell\)-adic sheaf represented over the ring of integers \(\mathcal O\) of a finite extension \(E_0/\mathbb Q_\ell\) by a compatible lattice system \((\mathcal F_a)_{a\geq1}\) with coefficients \(\mathcal O/\varpi^a\), the construction instead means
\[
\mathcal F_{\overline s_p}
=\left(\varprojlim_a\ \varinjlim_{(U,\overline u)}\mathcal F_a(U)\right)
\otimes_{\mathcal O} E_0,
\tag{MDB3.4a}
\]
followed by scalar extension to \(E=\overline{\mathbb Q}_\ell\) when that is the coefficient field in use. The finite-coefficient stalks are taken before the inverse limit; exchanging them is not asserted. This is independent of a choice of lattice after tensoring with \(E_0\), because two lattices in the same finite-dimensional representation are commensurable. Restricting first to \(s_p\) retains the action of
\[
\operatorname{Gal}(\overline{\mathbb F}_p/\mathbb F_p)\simeq\widehat{\mathbb Z}.
\tag{MDB3.5}
\]
Indeed finite extensions are the fields with \(p^r\) elements, whose cyclic Galois groups are generated by the \(p\)-power map. Their compatible inverse limit gives (MDB3.5); finite étale algebras are products of such fields. This constructs the usual equivalence with continuous Galois sets and, through inverse systems of finite coefficients, the corresponding \(\ell\)-adic representations.

Geometric Frobenius \(F_p\) is the inverse of the \(p\)-power arithmetic Frobenius. Over \(\mathbb F_q\), a point of residue degree \(d\) has \(F_x=F_q^d\) and \(N(x)=q^d\). This is action on the geometric fibre; the underlying one-point scheme \(s_p\) stays fixed.

The arithmetic generic point has the separate map
\[
\overline\eta_R=\operatorname{Spec}\overline{\mathbb Q}\to S.
\tag{MDB3.6}
\]
It is not \(\tau\). Its stalk and Galois action have the analogous étale-neighbourhood construction. The map \(\operatorname{Spec}\mathbb Q\to S\) is not a finite-type open immersion: every nonempty open of \(S\) contains all but finitely many closed primes. A finite-type six-functor theorem cannot be applied to this map merely by naming it as an open immersion.

Deligne §6.1.1(b) keeps the characteristic-zero objects that have spread out over some \(\mathbb Z[1/n]\), with morphisms identified after further shrinking. It does not identify their arithmetic data with an unadorned generic vector space.

## MDB4. Full dualizing complexes and their natural maps

For a finite-type \(\mathbb F_p\)-scheme with structure map \(b_X:X\to s_p\), Deligne §6.2.1 defines
\[
K_X=Rb_X^!E,\qquad D_XK=R\mathcal Hom_X(K,K_X).
\tag{MDB4.1}
\]
For the same scheme viewed over \(S\) by \(a_X=i_pb_X\), §6.2.7 defines
\[
K'_X=Ra_X^!E,\qquad D'_XK=R\mathcal Hom_X(K,K'_X).
\tag{MDB4.2}
\]
The superscript exclamation mark denotes exceptional inverse image, not \(Ra_{X,!}\).

For a finite-type morphism \(f:X\to Y\) over the common base, transitivity gives \(K_X=Rf^!K_Y\). The duality maps are
\[
D_Xf^*\simeq Rf^!D_Y,\qquad D_XRf^!\simeq f^*D_Y,
\tag{MDB4.3}
\]
\[
D_YRf_!\simeq Rf_*D_X,\qquad D_YRf_*\simeq Rf_!D_X.
\tag{MDB4.4}
\]
They also hold with prime notation when both complexes are relative to \(S\).

To display why these maps have precisely these domains, for test objects \(M\) on \(X\), \(N\) on \(Y\), tensor-Hom adjunction, exceptional-image adjunction, and the projection formula give
\[
\begin{aligned}
R\operatorname{Hom}_X(M,D_Xf^*N)
&=R\operatorname{Hom}_X(M\otimes f^*N,K_X)\\
&=R\operatorname{Hom}_Y(Rf_!(M\otimes f^*N),K_Y)\\
&=R\operatorname{Hom}_Y((Rf_!M)\otimes N,K_Y)\\
&=R\operatorname{Hom}_Y(Rf_!M,D_YN)\\
&=R\operatorname{Hom}_X(M,Rf^!D_YN).
\end{aligned}
\tag{MDB4.5}
\]
Naturality and Yoneda give the first identity (MDB4.3); biduality gives the second. Similarly,
\[
\begin{aligned}
R\operatorname{Hom}_Y(N,D_YRf_!M)
&=R\operatorname{Hom}_Y(N\otimes Rf_!M,K_Y)\\
&=R\operatorname{Hom}_X(f^*N\otimes M,K_X)\\
&=R\operatorname{Hom}_X(f^*N,D_XM)\\
&=R\operatorname{Hom}_Y(N,Rf_*D_XM)
\end{aligned}
\tag{MDB4.6}
\]
proves (MDB4.4), using biduality for its other identity. The adjunctions, projection formula, and biduality are the cohomological formalism invoked in Deligne §6.2.1, not new hypotheses about \(\tau\).

The associated trace is the counit
\[
Rf_!K_X=Rf_!Rf^!K_Y\longrightarrow K_Y.
\tag{MDB4.7}
\]
Its target retains the Tate line and degree. A scalar-valued pairing requires a specified comparison with that line.

## MDB5. Arithmetic and finite-field duality: the complete shift and twist

The arithmetic base has
\[
K'_S=E,
\tag{MDB5.1}
\]
because its structural morphism to \(\operatorname{Spec}\mathbb Z[1/\ell]\) is the recovered isomorphism. Deligne §6.2.7, specialized to its closed point, gives
\[
Ri_p^!E=E(-1)[-2].
\tag{MDB5.2}
\]
This is codimension-one cohomological purity, or the Gysin isomorphism for the regular closed point. Its construction in this specific arithmetic trait can be made explicit, so that the formula is not a new assumption about the recovered base.

Take the strict henselian discrete valuation ring
\[
A=\mathcal O^{\mathrm{sh}}_{S,\overline s_p},\qquad K=\operatorname{Frac}(A).
\tag{MDB5.2a}
\]
It has residue field \(\overline{\mathbb F}_p\) and uniformizer \(p\). The localization triangle computes its support complex as
\[
R\Gamma_{\overline s_p}(\operatorname{Spec}A,E)
=\operatorname{Cone}\!\left(E\longrightarrow R\Gamma(K,E)\right)[-1].
\tag{MDB5.2b}
\]
The initial \(E\) is \(R\Gamma(\operatorname{Spec}A,E)\): a strictly henselian local scheme is acyclic for these constant finite étale coefficient systems. Inverse limits with surjective coefficient transitions, then scalar extension, give the stated \(\ell\)-adic formula.

The named local input is the tame-inertia theorem recorded by Deligne §1.7.1, printed p.170:
\[
1\longrightarrow P\longrightarrow I
\longrightarrow\prod_{r\neq p}\mathbb Z_r(1)\longrightarrow1,
\qquad
t_\ell:I\longrightarrow\mathbb Z_\ell(1)
\text{ has pro-prime-to-}\ell\text{ kernel}.
\tag{MDB5.2c}
\]
The kernel has no positive-degree cohomology for finite \(\ell\)-primary coefficients, by averaging over its finite quotients. The remaining procyclic group has cohomological dimension one. For example, a temporary choice of topological generator gives the length-one completed group-ring resolution with differential \(\gamma-1\); its resulting degree-one space is intrinsically the dual of the Tate line, independently of that generator. Consequently
\[
H^0(K,E)=E,\quad
H^1(K,E)=\operatorname{Hom}_{\mathrm{cont}}(\mathbb Z_\ell(1),E)=E(-1),
\quad H^{j>1}(K,E)=0.
\tag{MDB5.2d}
\]
These statements follow first with finite coefficients and then by the compatible inverse limits, whose cohomology transition maps are surjective. The degree-zero restriction in (MDB5.2b) is the identity. Its long exact sequence therefore gives
\[
H^j_{\overline s_p}(\operatorname{Spec}A,E)=
\begin{cases}E(-1),&j=2,\\0,&j\neq2.\end{cases}
\tag{MDB5.2e}
\]

The specific isomorphism, including its sign, comes from Kummer theory. For every positive \(a\),
\[
H^1(K,\mu_{\ell^a})=K^\times/(K^\times)^{\ell^a}
\xrightarrow{\ \operatorname{ord}_p\ }\mathbb Z/\ell^a,\qquad [p]\mapsto1.
\tag{MDB5.2f}
\]
Every unit of \(A\) is an \(\ell^a\)-th power: take a root in the separably closed residue field and lift it by Hensel's lemma, using invertibility of \(\ell\). This proves the displayed valuation isomorphism and shows that replacing \(p\) by a unit multiple gives the same Kummer class. Use the localization boundary with the convention that \(\partial[p]\) is the positive divisor class corresponding to valuation one. Its compatible limit is
\[
\operatorname{cl}(p)\in H^2_{\overline s_p}(A,E(1)),
\qquad
E\xrightarrow{\sim}H^2_{\overline s_p}(A,E(1)),\quad
1\mapsto\operatorname{cl}(p).
\tag{MDB5.2g}
\]
It descends from the original arithmetic trait, so geometric Frobenius fixes this class with its \(E(1)\) coefficient. Thus the untwisted group in (MDB5.2e) has Frobenius \(p\), exactly the action on \(E(-1)\). The class gives the Frobenius-equivariant isomorphism
\[
E_{s_p}(-1)[-2]\xrightarrow{\sim}Ri_p^!E_S
\tag{MDB5.2h}
\]
because both sides have only degree-two cohomology and the map there is the generator isomorphism just constructed.

The adjoint ambient Gysin morphism is
\[
Ri_{p,*}E_{s_p}(-1)[-2]\longrightarrow E_S.
\tag{MDB5.2i}
\]
This distinguishes extraordinary inverse image \(Ri_p^!\) from direct image with proper support \(i_{p,!}=i_{p,*}\). The latter is not the costalk complex.

The composite \(a_X=i_pb_X\), transitivity, and the invertible Tate line now give
\[
\begin{aligned}
K'_X
&=Rb_X^!Ri_p^!E\\
&=Rb_X^!(E(-1)[-2])\\
&=K_X(-1)[-2],
\end{aligned}
\qquad
\boxed{D'_XK=D_XK(-1)[-2].}
\tag{MDB5.3}
\]
For \(X\) smooth of pure dimension \(d\) over \(\mathbb F_p\), this is
\[
K_X=E(d)[2d],\qquad K'_X=E(d-1)[2d-2].
\tag{MDB5.4}
\]
At a finite-field point these are \(E\) and \(E(-1)[-2]\); for a smooth curve they are \(E(1)[2]\) and \(E\). Both descriptions keep the structural base map.

The actual stalk/costalk identities are
\[
D'_{s_p}i_p^*\simeq Ri_p^!D'_S,\qquad
D'_{s_p}Ri_p^!\simeq i_p^*D'_S.
\tag{MDB5.5}
\]
Replacing arithmetic-relative finite-point duality by finite-field duality gives
\[
\boxed{
D_{s_p}i_p^*\simeq(Ri_p^!D'_S)(1)[2],\qquad
D_{s_p}Ri_p^!\simeq(i_p^*D'_S)(1)[2].
}
\tag{MDB5.6}
\]
These follow from (MDB4.3) and \(D'_{s_p}=D_{s_p}(-1)[-2]\). Removing the final factors would change the comparison.

For the actual lisse Tate complex \(E(r)[m]\) on \(S\), both restrictions can be calculated:
\[
i_p^*(E(r)[m])=E(r)[m],\qquad
Ri_p^!(E(r)[m])=E(r-1)[m-2].
\tag{MDB5.7}
\]
The first is pullback; the second tensors (MDB5.2) with the pulled-back invertible local system and shifts. Their nonzero cohomology occurs in degrees \(-m\) and \(2-m\), respectively. A stalk has not been identified with its costalk.

## MDB6. Weights with every Tate and cohomological factor

Fix a field isomorphism \(\iota:E\to\mathbb C\), as in Deligne §1.2.6. For a nonzero eigenvalue \(\alpha\) of geometric Frobenius at a point of norm \(q\), its \(\iota\)-weight is
\[
w_q(\alpha)=2\log_q|\iota\alpha|.
\tag{MDB6.1}
\]
For a sheaf, pointwise purity of integer weight \(w\) means the corresponding equality at every closed point and every complex embedding of the algebraic eigenvalues. The \(\iota\)-version works with the fixed isomorphism and allows real weights. Mixedness requires a finite filtration with pointwise pure quotients, not an arbitrary assignment to the support.

The Tate sheaf \(E(1)\) has geometric Frobenius \(q^{-1}\). Indeed arithmetic Frobenius raises an \(\ell\)-power root of unity to its \(q\)-th power; geometric Frobenius acts inversely. Thus \(E(r)\) has weight \(-2r\). With cohomological shifts
\(\mathcal H^i(K[m])=\mathcal H^{i+m}K\), Deligne §6.2.2 defines
\[
K\in D_{\leq w}
\quad\Longleftrightarrow\quad
\mathcal H^iK\text{ is mixed with pointwise weights }\leq i+w
\text{ for every }i.
\tag{MDB6.2}
\]
There is consequently an exact shift rule
\[
K\in D_{\leq w}
\ \Longleftrightarrow\
K(r)[m]\in D_{\leq w+m-2r}.
\tag{MDB6.3}
\]
To check it, the \(i\)-th sheaf on the right has weights at most
\((i+m+w)-2r=i+(w+m-2r)\). Apply the inverse shift and twist for the converse.

The full duality obeys
\[
D_X(K(r)[m])=(D_XK)(-r)[-m].
\tag{MDB6.4}
\]
This follows by moving the invertible Tate line and cohomological shift through derived Hom. Deligne §6.2.4 defines pure weight \(w\) by **both**
\[
K\in D_{\leq w},\qquad D_XK\in D_{\leq-w}.
\tag{MDB6.5}
\]
Applying (MDB6.3) to (MDB6.4) shows that a pure \(K(r)[m]\) has complex weight \(w+m-2r\). In particular
\[
K(N)[2N]\text{ has the same complex weight as }K,
\quad
D_XK(-1)[-2]\text{ has the same complex weight as }D_XK.
\tag{MDB6.6}
\]
The cancellation concerns the weight only; it does not remove either factor from the object.

For (MDB5.7), the stalk sheaf \(E(r)\) has weight \(-2r\) in degree \(-m\), and the costalk sheaf \(E(r-1)\) has weight \(2-2r\) in degree \(2-m\). Each gives complex weight \(m-2r\). This checks the arithmetic/finite-field compatibility of Deligne §6.2.7 with no suppressed twist.

On a smooth \(d\)-dimensional scheme with lisse cohomology sheaves, the full dual satisfies
\[
\mathcal H^i(D_XK)
=\bigl(\mathcal H^{-i-2d}K\bigr)^\vee(d).
\tag{MDB6.7}
\]
It follows from \(K_X=E(d)[2d]\), since taking the dual of a bounded complex of locally free finite-rank coefficients reverses cohomological degrees. At a closed point \(x\), put \(q=N(x)\), including its full residue degree over the base field. An eigenvalue \(\alpha\) in degree \(j\) then corresponds to
\[
q^{-d}\alpha^{-1}
\quad\text{in degree }-j-2d.
\tag{MDB6.8}
\]
The upper bound on this dual eigenvalue converts to the lower bound on \(\alpha\). Equations (MDB6.2), (MDB6.5), and (MDB6.8) show that under these smoothness and lisse-cohomology hypotheses, purity of \(K\) is equivalent to pointwise purity of each \(\mathcal H^jK\) of weight \(w+j\), exactly §6.2.5(b).

For an arbitrary complex on a singular or ramified situation, purity still means (MDB6.5). The stronger cohomology-sheaf conclusion is not asserted outside the hypotheses just used.

## MDB7. Precisely which weight bounds are functorial

First, subobjects and quotients of a Frobenius module retain subsets of the eigenvalues; an extension has the union of the two multisets, because in a basis respecting the subobject its matrix is block upper triangular. Thus upper weight bounds survive subquotients, finite filtrations, and extensions. The same statements follow stalkwise for mixed sheaves.

Ordinary pullback preserves pointwise weights and upper complex bounds. At a closed point \(x\) over \(y\) with residue extension degree \(d\), the pulled-back eigenvalue is \(\alpha^d\), while \(N(x)=N(y)^d\). Hence
\[
2\log_{N(x)}|\iota(\alpha^d)|
=2\log_{N(y)^d}|\iota\alpha|^d
=2\log_{N(y)}|\iota\alpha|.
\tag{MDB7.1}
\]
Pullback is exact for these coefficient sheaves, so it preserves the finite mixed filtration and the inequalities in (MDB6.2).

Deligne's fundamental theorem §3.3.1 says that \(R^a f_!\mathcal F\) has weights at most \(v+a\) when \(\mathcal F\) has weights at most \(v\). The passage to complexes in §6.2.3 uses the cohomology spectral sequence
\[
R^a f_!\mathcal H^bK\ \Longrightarrow\
\mathcal H^{a+b}(Rf_!K).
\tag{MDB7.2}
\]
The transcription writes this page as \(E_1^{ab}\); the calculation does not depend on the naming of its starting page. The weights of the displayed term are at most
\[
a+(b+w)=(a+b)+w.
\tag{MDB7.3}
\]
Every subsequent page and the filtration on the abutment consist of subquotients and extensions of terms of the relevant total degree. The preceding eigenvalue argument therefore proves
\[
Rf_!:D_{\leq w}(X)\longrightarrow D_{\leq w}(Y).
\tag{MDB7.4}
\]
The deep geometric input is the already proved theorem §3.3.1. Its source proof reduces to relative curves, proper smooth families, controlled boundary monodromy, and the preceding purity theorem; it is not deduced here from formal adjunction alone.

Define lower complex weights through the full dualizing complex:
\[
K\in D_{\geq w}(X)
\quad\Longleftrightarrow\quad
D_XK\in D_{\leq-w}(X).
\tag{MDB7.5}
\]
The exact maps (MDB4.3)–(MDB4.4) then give
\[
Rf_*:D_{\geq w}(X)\to D_{\geq w}(Y),\qquad
Rf^!:D_{\geq w}(Y)\to D_{\geq w}(X).
\tag{MDB7.6}
\]
For the first, \(D_YRf_*K=Rf_!D_XK\), to which (MDB7.4) applies. For the second, \(D_XRf^!K=f^*D_YK\), to which the pullback result applies.

When \(f\) is proper, \(Rf_!=Rf_*\). Applying (MDB7.4) to \(K\) and \(D_XK\), and using (MDB4.4), proves the full §6.2.6 conclusion:
\[
K\text{ pure of weight }w
\quad\Longrightarrow\quad
Rf_*K\text{ pure of weight }w.
\tag{MDB7.7}
\]
The arithmetic-base version uses the prime dualities and the unchanged weight calculation (MDB6.6), as in §6.2.7.

These conclusions do not say that arbitrary \(Rf_*\) preserves the same upper weight bound, or arbitrary \(f^*\) preserves both dual bounds. Section6.1's mixedness stability is a stability of the mixed category; the numerical bound and its direction come from the specific calculations above.

On the actual recovered base, \(i_p\) is proper. Hence the actual object \(i_{p,*}E\) is pure of weight zero for arithmetic duality. One can verify the full dual directly:
\[
D'_S i_{p,*}E
=i_{p,*}D'_{s_p}E
=i_{p,*}E(-1)[-2].
\tag{MDB7.8}
\]
The sole nonzero dual cohomology sheaf has weight \(2\) in degree \(2\), so the upper complex bound is still zero. This is an application on the constructed base, not a proposed object replacing its geometry.

## MDB8. The mixed-weight filtration, functoriality, and strictness

For this section the additional sources actually read are Deligne §§3.4.1–3.4.9 in full, printed pp.207–210, TeX lines2310–2393, and §§1.8.9–1.8.10 with their proofs, printed pp.177–178, TeX lines1278–1319. The upstream étale descent and fundamental-group facts named below remain named inputs to his construction.

Section3.4.1(ii) applies to a **lisse**, \(\iota\)-mixed sheaf \(\mathcal F_0\) on a scheme of finite type over \(\mathbb F_q\), with integral pointwise weights. It constructs a unique finite increasing filtration by lisse subsheaves
\[
\cdots\subset W_{n-1}\mathcal F_0
\subset W_n\mathcal F_0\subset\cdots
\tag{MDB8.1}
\]
whose \(n\)-th graded quotient is pointwise \(\iota\)-pure of weight \(n\). Existence of this global filtration is a theorem, not a consequence merely of naming the eigenvalue-weight subspaces at one point.

Its source proof uses the exact extension sequence in §3.4.2:
\[
0\longrightarrow
H^0(X,\mathcal Hom(\mathcal F,\mathcal G))_F
\longrightarrow
\operatorname{Ext}^1(\mathcal F_0,\mathcal G_0)
\longrightarrow
H^1(X,\mathcal Hom(\mathcal F,\mathcal G))^F.
\tag{MDB8.2}
\]
The subscript is coinvariants and the superscript is invariants. For a geometrically split extension, two splittings differ by a section of \(\mathcal Hom\); the obstruction to a Frobenius-invariant splitting is its class modulo \(F-1\). This proves the left term and exactness there, while pullback to the geometric scheme gives the right map.

For pure inputs of weights \(\beta,\gamma\) on a smooth base, \(\mathcal Hom(\mathcal F,\mathcal G)\) has weight \(\gamma-\beta\). Section3.4.3 applies the source's §3.3.5 strengthened by §3.3.10: the weights on its \(H^1\) have the form \(\gamma-\beta+1+n\), where \(n\) is a nonnegative integer. Thus eigenvalue \(1\), of weight zero, can occur in the right term of (MDB8.2) only when
\(\beta-\gamma\) is a positive integer. Including the left term allows \(\beta=\gamma\). Thus §3.4.4 gives
\[
\operatorname{Ext}^1(\mathcal F_0,\mathcal G_0)\neq0
\quad\Longrightarrow\quad
\beta\equiv\gamma\pmod{\mathbb Z},\qquad \beta\geq\gamma.
\tag{MDB8.3}
\]
This implication is the quoted proved extension theorem, with its smooth/lisse scope retained.

Induction on the number of pure successive quotients now puts extensions in weight order. In detail, for
\(0\to\mathcal F'_0\to\mathcal F_0\to\mathcal F''_0\to0\),
with \(\mathcal F'_0\) pure of weight \(\beta\), the inverse image of
\(W_{\beta-1}\mathcal F''_0\) is an extension which splits by (MDB8.3), applied successively to its lower-weight quotients. Its lift gives \(W_n\mathcal F_0\) for \(n<\beta\); for \(n\geq\beta\), take the inverse image of \(W_n\mathcal F''_0\). For the decomposition by \(b\in\mathbb R/\mathbb Z\), put \(b=[\beta]\). Every summand \(\mathcal F''_0(b')\), \(b'\neq b\), has a split inverse-image extension by \(\mathcal F'_0\), using (MDB8.3) successively. Lift these summands; take the entire inverse image of \(\mathcal F''_0(b)\) for the \(b\)-summand. The lifts are unique: a difference between two lifts is a morphism between disjoint weight sets, hence zero by generalized Frobenius eigenspaces at each closed point. This proves both constructions in §3.4.7 on its smooth open stratum.

Here is the full extension from that stratum used in §3.4.8. We use \(Z_0\) for the closed complement in this paragraph; it is a scheme symbol, not the user's \(Z_0\) absence label. Let
\[
j:U_0\hookrightarrow X_0,\qquad i:Z_0=X_0\setminus U_0\hookrightarrow X_0
\tag{MDB8.3a}
\]
be complementary open and closed immersions. Replacing the scheme by its reduction does not change its étale topos. A constructible mixed sheaf has a dense smooth open on which its defining finite pure filtration has lisse terms. This gives the open to which §3.4.7 applies; the complement has smaller dimension.

The following gluing formula first concerns coefficient sheaves on the geometric schemes \(X=X_0\otimes\overline{\mathbb F}_q\), \(U\), and \(Z\), with the same letters \(i,j\) for the base-changed immersions. A Weil sheaf adds its rational-coefficient Frobenius isomorphism to these underlying geometric sheaves. No extension of that action to a continuous representation of the profinite arithmetic fundamental group is assumed. The gluing data are the triple
\[
(\mathcal F_U,\mathcal F_Z,s),
\qquad
s:\mathcal F_Z\longrightarrow i^*j_*\mathcal F_U.
\tag{MDB8.3b}
\]
Its reconstructed geometric sheaf is the following fibre product, with every object now on \(X\):
\[
\mathcal F=
j_*\mathcal F_U
\times_{\,i_*i^*j_*\mathcal F_U}
i_*\mathcal F_Z.
\tag{MDB8.3c}
\]
The first arrow into the middle object is the adjunction unit for \(i^*\dashv i_*\); the second is \(i_*s\). The functors \(i^*,j^*\) are exact and therefore preserve this fibre product. On \(U\), the two closed-support terms restrict to zero and \(j^*j_*\mathcal F_U=\mathcal F_U\). On \(Z\), the first arrow becomes the identity of \(i^*j_*\mathcal F_U\), so the fibre product is \(\mathcal F_Z\). Conversely, the adjunction maps from any sheaf \(\mathcal F\) into these two direct images give a map to (MDB8.3c); it is an isomorphism on geometric stalks on \(U\) and \(Z\), hence an isomorphism. Compatible pairs of morphisms of the two restrictions induce exactly the morphisms of these fibre products. This proves the asserted triple equivalence. For adic coefficients the underlying geometric construction is coefficientwise and compatible with transition maps, then passes to rational coefficients, in the order in (MDB3.4a). Since \(i,j\) are defined over the finite field, their functors and the adjunction maps are compatible with Frobenius pullback. Frobenius-compatible input triples therefore give a Frobenius isomorphism on the fibre product, proving the same equivalence for Weil sheaves. This argument does not require a Frobenius-stable integral lattice.

Induction on dimension has constructed the decomposition by weight congruence classes on both restrictions:
\[
\mathcal F_U=\bigoplus_b\mathcal F_U(b),\qquad
\mathcal F_Z=\bigoplus_b\mathcal F_Z(b).
\tag{MDB8.3d}
\]
There are finitely many nonzero summands. The boundary theorem needed to glue them is Deligne §1.8.9: \(j_*\) preserves mixedness, a pointwise upper weight bound, and integrality of pointwise weights. The theorem and its proof, printed pp.177–178, have been read here; this remains a named earlier theorem of the source, not a result newly deduced from the singleton support. Applying its integrality assertion after the constant rank-one twist that shifts \(b\) into \(\mathbb Z\), and undoing that twist, proves
\[
\text{every pointwise weight of }i^*j_*\mathcal F_U(b)
\text{ belongs to }b.
\tag{MDB8.3e}
\]
The twisting operation here is the source's operation on Weil sheaves; it has not introduced an operation on \(\tau\). At each closed point, the specialization map in (MDB8.3b) intertwines Frobenius. Generalized eigenspaces with weights in distinct classes modulo \(\mathbb Z\) have distinct eigenvalues. Thus every component
\(\mathcal F_Z(b)\to i^*j_*\mathcal F_U(b')\), \(b'\neq b\), is zero on closed stalks, hence zero. Therefore \(s\) has the block form \(\bigoplus_b s_b\). Define
\[
\mathcal F(b)=
j_*\mathcal F_U(b)
\times_{\,i_*i^*j_*\mathcal F_U(b)}
i_*\mathcal F_Z(b).
\tag{MDB8.3f}
\]
Finite direct sums commute with the additive direct-image functors and with these fibre products. Equations (MDB8.3c)–(MDB8.3f) consequently give
\(\mathcal F=\bigoplus_b\mathcal F(b)\). Restriction to \(U_0\) and \(Z_0\) proves that the weights of \(\mathcal F(b)\) lie in \(b\). Its uniqueness and functoriality follow from the same Frobenius decomposition on closed stalks. This completes the general decomposition in §3.4.1(i), including its boundary specialization map.

For the lisse integral-weight filtration in §3.4.1(ii), first suppose \(X_0\) is connected and normal. The homomorphism
\[
\pi_1(U,\bar u)\longrightarrow\pi_1(X,\bar u)
\tag{MDB8.3g}
\]
is surjective on each geometric connected component, where \(X=X_0\otimes\overline{\mathbb F}_q\), \(U=U_0\otimes\overline{\mathbb F}_q\). Normality is preserved by this separable algebraic base extension. Indeed, any connected finite étale cover of a connected normal scheme is normal and connected, hence irreducible; its restriction to a nonempty dense open remains connected. The finite-quotient characterization of surjectivity for profinite groups gives (MDB8.3g). The same argument applies componentwise when necessary, retaining the Frobenius permutation of those components.

Write \(V\) for the representation of the geometric group \(\pi_1(X,\bar u)\) defining the underlying lisse sheaf \(\mathcal F\). Its restriction to \(\pi_1(U,\bar u)\) factors through (MDB8.3g). Each subrepresentation \(W_n(j^*\mathcal F_0)_{\bar u}\subset V\) is therefore already stable under \(\pi_1(X,\bar u)\): the surjection has the same image on \(V\), and its kernel acts trivially on \(V\) and on each subspace. This gives the lisse geometric subobject. The filtration on \(U_0\) is already a filtration of Weil sheaves, so its subobjects are Frobenius-stable. Extension across the normal scheme by \(j_*\) is compatible with Frobenius pullback; it extends those isomorphisms and their inverses. Thus each extended subobject has its Weil structure on \(X_0\). No continuous arithmetic \(\pi_1(X_0)\)-representation is asserted. The concrete Weil-sheaf formulas are
\[
\mathcal F_0=j_*j^*\mathcal F_0,\qquad
W_n\mathcal F_0=j_*W_n(j^*\mathcal F_0),\qquad
\operatorname{Gr}_n^W\mathcal F_0
=j_*\operatorname{Gr}_n^W(j^*\mathcal F_0).
\tag{MDB8.3h}
\]
For the first equality, a lisse geometric sheaf extending across a normal scheme has the same invariant sections on the connected dense part of each strict local neighbourhood. The preceding subrepresentation argument applies to all the subobjects and quotients in the filtration. In that subcategory, \(j_*\) is the inverse of restricting geometric representations that factor through \(\pi_1(X)\), with their compatible Weil isomorphisms retained, so it is exact there. This proves the last equality in (MDB8.3h); it does not assert that \(j_*\) is exact on arbitrary sheaves on \(U\).

Set \(\mathcal G=\operatorname{Gr}_n^W\mathcal F_0\). It is lisse on \(X_0\) and pure of weight \(n\) on \(U_0\). To check the boundary weights, the two injections
\[
\mathcal G\hookrightarrow j_*j^*\mathcal G,\qquad
\mathcal G^\vee\hookrightarrow j_*j^*\mathcal G^\vee
\tag{MDB8.3i}
\]
follow from lisseness and density. Apply §1.8.9 to the two right sides: their pointwise weights are at most \(n\) and \(-n\), respectively. Subobjects inherit these upper bounds. Eigenvalues on \(\mathcal G^\vee\) are the inverses of eigenvalues on \(\mathcal G\), so the second upper bound says that \(\mathcal G\) has weights at least \(n\). Thus it is pure of weight exactly \(n\) everywhere. This is the complete two-bound deduction of §1.8.10 used in §3.4.8.

For completeness the descent reduction in that paragraph can be made explicit. Over a finite field the scheme is excellent; the disjoint union of the normalizations of the irreducible components of \(X_{0,\mathrm{red}}\) gives a finite proper surjection
\[
a:Y_0\longrightarrow X_{0,\mathrm{red}}
\tag{MDB8.3j}
\]
with \(Y_0\) normal. We use the upstream proper-descent theorem for constructible étale coefficient sheaves and lisse local systems, applied on the geometric schemes coefficientwise and compatibly for adic systems: sheaves with compatible descent isomorphisms on a proper surjective cover descend effectively; the descended morphisms and their lisse property are detected by that descent. After passing to rational coefficients, Frobenius isomorphisms compatible with descent descend as morphisms, as do their inverses. This supplies the Weil structure without assuming a Frobenius-stable lattice or a continuous arithmetic fundamental-group representation. This is the descent input invoked by Deligne, not a new six-functor theorem proved in this note.

Apply the normal construction to \(a^*\mathcal F_0\). On
\(Y_0\times_{X_0}Y_0\), the two pullbacks of \(W_n(a^*\mathcal F_0)\) sit inside the same pullback of \(\mathcal F_0\). At every closed geometric point, both are the generalized Frobenius sum of weights at most \(n\). Finite residue extension replaces \(\alpha\) by \(\alpha^d\) and \(q\) by \(q^d\), preserving its weight. The two subobjects therefore agree on all closed stalks and hence as constructible subsheaves. Their identification is the identity in the common ambient sheaf, so the cocycle condition on the triple fibre product holds identically. These are the actual descent maps.

An explicit descended subobject is
\[
W_n\mathcal F_0=
\ker\!\left(
\mathcal F_0\longrightarrow
a_*\bigl(a^*\mathcal F_0/W_n(a^*\mathcal F_0)\bigr)
\right).
\tag{MDB8.3k}
\]
The arrow is the adjunction unit followed by the quotient map. On the underlying geometric sheaves, proper base change for this finite map identifies its stalk at \(\bar x\) with the map from \((\mathcal F_0)_{\bar x}\) into the product of the corresponding quotients over the finitely many geometric points of \(Y_{\bar x}\). The compatibility just proved identifies all these subspaces of \((\mathcal F_0)_{\bar x}\), so the kernel is exactly that subspace. In particular its pullback is the constructed \(W_n(a^*\mathcal F_0)\). Effective descent gives the lisse geometric subobject and lisse graded quotients. Frobenius preserves the quotient arrow and its kernel because the morphism \(a\) is defined over the finite field and the filtration upstairs has its Weil structure. Hence the descended kernel and quotients retain their Weil structures. Exhaustiveness and finiteness descend from the finite filtration on \(Y_0\), and purity of each graded quotient descends because every point is covered and the residue-power calculation preserves weights. Equations (MDB8.3g)–(MDB8.3k) complete the general filtration argument; there is no unresolved gluing step here.

The geometric semisimplicity assertion §3.4.1(iii) has a short additional proof (§3.4.5). Let \(X_0\) be normal and \(\mathcal F_0\) lisse pure of weight \(\beta\). Passing to a dense smooth open does not change the image of its geometric monodromy, by (MDB8.3g) and the same normality argument after base extension. On the geometric scheme let \(\mathcal F'\) be the sum of all irreducible lisse subobjects of \(\mathcal F\). It is a semisimple subobject of finite rank. Frobenius permutes those irreducible subobjects, so their sum is stable and descends to a Weil subobject \(\mathcal F'_0\). Put \(\mathcal F''_0=\mathcal F_0/\mathcal F'_0\); subobjects and quotients of a pure sheaf are pure of the same weight. Section3.4.3 says that the extension
\[
0\longrightarrow\mathcal F'_0
\longrightarrow\mathcal F_0
\longrightarrow\mathcal F''_0
\longrightarrow0
\tag{MDB8.3l}
\]
is geometrically split, since both end terms have weight \(\beta\). If \(\mathcal F''\neq0\), its finite-dimensional monodromy representation has an irreducible subrepresentation (take a nonzero invariant subspace of minimum dimension). A geometric splitting lifts it to an irreducible subobject of \(\mathcal F\) outside \(\mathcal F'\), contrary to the definition of that sum. Therefore \(\mathcal F''=0\), proving geometric semisimplicity. Arithmetic Frobenius need not be semisimple: the coinvariant term in (MDB8.2) can still record equal-weight extensions. The distinction is retained in §6.2.13's use of this result.

The functoriality and strictness can be proved explicitly on its fibres. At a closed geometric point \(x\), let \(V_\alpha\) be the generalized Frobenius eigenspace of \(\alpha\). The constructed filtration has
\[
(W_n\mathcal F_0)_x
=\bigoplus_{w_{N(x)}(\alpha)\leq n}V_\alpha.
\tag{MDB8.4}
\]
A Frobenius-intertwining map \(h:V\to V'\) sends \(V_\alpha\) into \(V'_\alpha\), because
\((F'-\alpha)^rh(v)=h(F-\alpha)^rv\).
Consequently it preserves the decomposition by exact weights.

More precisely, let \(z=h(v)\in W_nV'\). Decompose \(v=v_{\leq n}+v_{>n}\) into its generalized eigenvalue-weight parts. The image of the second summand has weights \(>n\); since \(h(v)\) lies in the disjoint sum of weights \(\leq n\), that second image is zero. Hence \(z=h(v_{\leq n})\). The reverse containment is immediate. Thus
\[
\boxed{h(W_nV)=\operatorname{im}h\cap W_nV'.}
\tag{MDB8.5}
\]
This is strictness, not just preservation.

For lisse sheaves, the images, kernels, and relevant intersections are lisse. Equality of their fibres at every closed geometric point implies equality of sheaves: a nonzero constructible quotient would have nonempty constructible support, which on a finite-type scheme over a finite field contains a closed point. Therefore every morphism in §3.4.1(ii) satisfies
\[
h(W_n\mathcal F_0)
=\operatorname{im}h\cap W_n\mathcal G_0.
\tag{MDB8.6}
\]
In particular each \(W_n\) and each \(\operatorname{Gr}_n^W\) is exact on short exact sequences in this lisse integral-weight category. This follows directly by applying strictness to the injection and surjection.

Under base pullback in this finite-field setting, formula (MDB7.1) preserves the weights; pulling back (MDB8.1) gives lisse pure graded quotients. Uniqueness therefore identifies the pulled-back filtration with the weight filtration of the pulled-back sheaf. The norm-preserving branch scheme isomorphism (MDB1.5) induces such comparisons on each finite-field fibre, in both directions. On the arithmetic scheme \(S\) itself, an isomorphism transports any already specified weight filtration and all of its maps, preserving the residue norms and hence the pointwise weight conditions. This statement does not extend the finite-field existence theorem to an unspecified global filtration on every arithmetic sheaf over \(S\).

These facts are used on lisse strata or lisse cohomology sheaves where their hypotheses hold. Section6.1's assertion that \(R^if_*\mathcal F\) is mixed does not itself assert lisseness or supply a global weight filtration of the form (MDB8.1) without those hypotheses. Section6.2.13 invokes §3.4.1(iii)'s geometric semisimplicity under its stated conditions; it is not an assertion that arithmetic Frobenius is always diagonalizable.

## MDB9. The degree factor at a recovered prime and the exact purity circle

At the actual recovered closed point \(s_p\), let \(V\) be a finite-dimensional Frobenius representation, placed in cohomological degree zero. Finite-field and arithmetic-relative duality are
\[
D_{s_p}V=V^\vee,\qquad
D'_{s_p}V=V^\vee(-1)[-2].
\tag{MDB9.1}
\]
A Frobenius eigenvalue \(\alpha\) on \(V\) is therefore sent to
\[
\alpha^{-1}\text{ in degree }0
\quad\text{and}\quad
p\alpha^{-1}\text{ in degree }2,
\tag{MDB9.2}
\]
respectively. The factor \(p\) is the action on the Tate line \(E(-1)\), and degree \(2\) comes from \([-2]\). For nontrivial Jordan data, duality takes the full transpose inverse operator, multiplied by \(p\); no nilpotent contribution is removed by writing its eigenvalue formula.

If \(A\) is an arbitrary bounded Frobenius complex, the arithmetic-point formula is
\[
\mathcal H^{2-i}(D'_{s_p}A)
=(\mathcal H^i A)^\vee(-1).
\tag{MDB9.3}
\]
In the situation of Deligne's proved proper-image proposition §6.2.6 with \(f:X\to s_p\) proper, put \(A=Rf_*K\), a complex on the finite-field point \(s_p\). Its pure weight \(w\) follows from (MDB7.7), with that proposition's input and properness hypotheses retained; this is not an assumption about an unconstructed programme receiver. The target point is essential: an arbitrary ordinary stalk restriction from a more general target does not automatically preserve the dual lower bound. The upper bound on an eigenvalue \(\alpha\) of \(\mathcal H^iA\) is
\[
|\iota\alpha|\leq p^{(i+w)/2}.
\tag{MDB9.4}
\]
The upper bound on the dual complex, applied in the degree \(2-i\) prescribed by (MDB9.3), is
\[
|p/\iota\alpha|\leq p^{(2-i-w)/2}.
\tag{MDB9.5}
\]
Dividing the full displayed factors gives the opposite inequality
\[
|\iota\alpha|\geq p^{(i+w)/2}.
\tag{MDB9.6}
\]
Together they give the exact circle
\[
|\iota\alpha|=p^{(i+w)/2}.
\tag{MDB9.7}
\]
For a closed point of norm \(q=p^d\), the same proof replaces \(p\) by \(q\) everywhere, including the Tate factor. This is the full arithmetic-base version of Deligne's two-bound mechanism.

The degree-one, weight-zero case retains the factor \(p\) and the same cohomological degree after duality, because \(2-1=1\). For the complex realization \(V_{\mathbb C}=V\otimes_{E,\iota}\mathbb C\), define its degree-weighted conjugate-dual object to be \(\overline{V_{\mathbb C}}^{\,\vee}\otimes\mathbb C(-1)\), where the realized Tate line has Frobenius \(p\). This is a contravariant functor on Frobenius representations, not an asserted isomorphism from \(V_{\mathbb C}\) to its conjugate dual. The full operator on the resulting object is
\[
p(\overline F^{-1})^{\,t},
\tag{MDB9.8}
\]
so the scalar action is \(a\mapsto p/\overline a\). Here complex conjugation is explicitly on the chosen complex realization; it is not asserted to be a canonical involution of every \(\ell\)-adic coefficient object.

This gives the exact scalar comparison with the programme's previously calculated arithmetic character action
\[
a=p^\rho\longmapsto p/\overline a=p^{1-\overline\rho}.
\tag{MDB9.9}
\]
The fixed-character equation is
\[
a=p/\overline a
\ \Longleftrightarrow\ |a|^2=p.
\tag{MDB9.10}
\]
This comparison preserves all degree and duality factors. It compares formulas on character values; it does not assert that the programme's analytic zero-jet quotient has already been realized as a constructible \(\ell\)-adic complex with the proper direct image in (MDB9.3)–(MDB9.7).

## MDB10. The exact weight-descent defect of the actual geometric-stalk map

On the constructed arithmetic scheme \(S\), take the two actual lisse sheaves \(E\) and \(E(1)\). Restrict each to the same \(s_p\) and then the same geometric point \(\overline s_p\). Their underlying geometric stalks are one-dimensional \(E\)-vector spaces. They are isomorphic after choosing a basis of the Tate line, but their geometric Frobenius operators and weights are
\[
\begin{array}{c|c|c}
\text{sheaf at }s_p&F_p&\text{weight}\\
\hline
E&1&0\\
E(1)&p^{-1}&-2 .
\end{array}
\tag{MDB10.1}
\]
These are the original Tate objects on the same recovered base, not an arbitrary matrix construction.

Any Frobenius-equivariant map between the two lines has, after a chosen vector-space identification, scalar \(c\) satisfying
\[
c=p^{-1}c.
\tag{MDB10.2}
\]
Since \(p>1\), the scalar is zero. Thus a vector-space isomorphism of their geometric stalks cannot lift to an isomorphism of the arithmetic fibre representations. There is no isomorphism-invariant weight function on bare vector-space stalks whose pullback gives both weights in (MDB10.1): one vector-space isomorphism class would have to receive both zero and minus two.

The exact categorical comparison is
\[
U_p:\operatorname{Rep}_{E}\bigl(\operatorname{Gal}
(\overline{\mathbb F}_p/\mathbb F_p)\bigr)
\longrightarrow\operatorname{Vect}_{E},\qquad
(V,F)\longmapsto V.
\tag{MDB10.3}
\]
On this point-category, \(U_p\) is faithful, exact, tensor, and conservative on existing morphisms. It is faithful because distinct equivariant maps are distinct underlying maps; exactness and tensor compatibility are computed on the vector spaces; if an equivariant map is bijective, its inverse also intertwines the action. It is not full by (MDB10.2). Isomorphism of two images does not supply a morphism upstairs. These statements are not extended to an arbitrary single-stalk functor on all sheaves over \(S\).

Because \(U_p\) is exact, applying it term by term to bounded complexes sends quasi-isomorphisms to quasi-isomorphisms and defines the exact derived functor
\[
U_p:D^b\!\left(\operatorname{Rep}_{E}(\operatorname{Gal}(\overline{\mathbb F}_p/\mathbb F_p))\right)
\longrightarrow D^b(\operatorname{Vect}_{E}).
\tag{MDB10.3a}
\]
On these finite-dimensional coefficient categories tensor products are exact, so this extension also retains the tensor and shift identifications used next. With \(V\) placed in degree zero, the duality comparison survives with all of its data:
\[
U_p(D'_{s_p}V)
=U_p(V)^\vee\otimes U_p(E(-1))[-2].
\tag{MDB10.4}
\]
Thus forgetting Frobenius does not destroy vector-space duality or the existence of the Tate line as a line. It removes the Frobenius action needed to read its arithmetic weight. Retaining that action, or retaining the full specified Tate object instead of identifying all underlying lines, retains the distinction.

This proves a precise descent obstruction for this particular actual receiver. It does not say that the user's full supporting datum must use this forgetful map, or that every possible enriched supporting construction loses weights.

## MDB11. What transfers through the available maps

The constructed chain has the following types:
\[
\text{CC generic stalk with }(G,H,\alpha)
\longmapsto L
\longmapsto R=\operatorname{End}(L)
\longmapsto\Sigma
\supset S
\longleftarrow s_p
\longleftarrow\overline s_p.
\tag{MDB11.1}
\]
The supporting maps \(|\Sigma|\to T\hookrightarrow X\) exist topologically, with the sheaf morphisms (MDB2.7) and (MDB3.2). The residue maps, étale stalks, Frobenius action, and duality on the recovered arithmetic schemes exist as calculated. None of these arrows assigns a number or metric to the supporting point.

The constant coefficient object \(E_S\) is an actual pure weight-zero complex: every local Frobenius acts by one, and \(D'_SE_S=E_S\). Its local Euler factors at all \(p\neq\ell\) are
\[
\det(1-p^{-s}F_p\mid E_{\overline s_p})^{-1}
=(1-p^{-s})^{-1}.
\tag{MDB11.2}
\]
Together with the explicitly retained coefficient-prime factor (MDB1.4), they give the original \(\zeta(s)\). Thus the reconstructed ring, its prime spectrum, and these local pure coefficient data are already genuine receivers, with the full original Euler factors.

What is functorial is now explicit: norm-preserving scheme isomorphisms transport pointwise weights, and preserve the strict mixed-weight filtration in the category where Deligne constructs it; pullback preserves upper bounds; compactly supported direct image preserves upper bounds by §3.3.1 and its spectral sequence; duality transports those to lower bounds; proper direct image preserves both bounds. The exact circle follows for the proper arithmetic cohomology to which those statements apply.

The topological or unringed topos map to \(T\) is not, by its construction alone, a new morphism in Deligne's finite-type arithmetic six-functor category. Its existing derived global-section functor has not been proved to identify the analytic original-zeta zero-jet receiver with such a proper arithmetic image. The map (MDB10.3) gives the exact weight information lost by its further geometric-stalk observation; adding that action is the specified data required to retain the weight.

These are statements about the maps actually constructed, with their precise preserved data and defect. They do not close other constructions on the enriched support. The full scalar connection to the programme's \(a\mapsto p/\overline a\) is (MDB9.8)–(MDB9.10), including the Tate degree factor that a comparison must preserve.
