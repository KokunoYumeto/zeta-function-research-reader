# The additive receiving sheaf of the current tau source

24 September 2026. Independent continuation of [SOURCE_TAU_SPECIALIZATION_DERIVATION.md](SOURCE_TAU_SPECIALIZATION_DERIVATION.md), ST0–ST10. This constructs the sheaf and its actual restriction, support and spectral maps from the current source operations. It does not replace that source by its additive receiver.

## SS0. Operation prerequisites and the retained corpus

The current CORPUS_AND_OPERATION_RULES.md (private construction record; not included), including its new global-argument checks, was read before the calculation. The controlling source remains [SOURCE_OPERATIONS_AND_PROOFS.md](../foundations/user_definitions_20260924/SOURCE_OPERATIONS_AND_PROOFS.md), B1–B5, together with the verbatim U01–U18 and the full-history passages cited in ST0 and AC0. In particular:

* \(Z_1/\tau\) is primitive presence with no \(Z_2\) parity or source addition.
* The original integers, their full values and the applicable \(Z_2\) data are retained after the complete arithmetic reconstruction.
* The source operations are original integer arithmetic and the supplied global multiplicative identity \(\tau\).
* Constructing an additive receiving object does not extend the domain of the source's addition. Formal receiving elements are not asserted to be copies of \(\tau\).
* A local calculation about this sheaf is not made a counterexample to the user's whole-spectrum argument.

The symbols \(0,1,\tau\) below have their unchanged source meanings when used in \(S\). Brackets such as \([1]\) explicitly denote their images in a constructed receiving ring. All sheaf cohomology in this document is ordinary sheaf cohomology of the stated topological space, with abelian receiving coefficients. No étale, prismatic, or full programme cohomology is silently identified with it.

## SS1. The exact source space and universal local receiving rings

Retain the source \(S\) and the integer-addition-compatible prime subspace of ST2:
\[
 X=X_{\mathbb Z}\cup\{\mathfrak m\},\qquad
 X_{\mathbb Z}=\{(0)\}\cup\{p\mathbb Z:p\text{ prime}\}
 \simeq\operatorname{Spec}\mathbb Z,\qquad
 \mathfrak m=\mathbb Z\subset S.
\tag{SS1.1}
\]
This notation names the actual ideal \(\mathfrak m\), not primitive \(\tau\) or the separately constructed privileged \(\eta\). The open immersion is \(j:X_{\mathbb Z}\hookrightarrow X\), and \(i:\{\mathfrak m\}\hookrightarrow X\) is the closed point inclusion. The only open neighbourhood of \(\mathfrak m\) is \(X\), and \(D(1)=X_{\mathbb Z}\). Every proper open of \(X\) is an ordinary open of \(X_{\mathbb Z}\).

Every nonempty open of \(X_{\mathbb Z}\) has the form \(D(n)\), \(n\ne0\): a proper nonempty closed subset is the finite set of prime divisors of an integer, and the generic point lies in every nonempty open. The empty open is treated separately.

The universal additive receiver constructed in ST5 is
\[
 U_S=\mathbb Z[\epsilon]/(\epsilon^2-\epsilon),\qquad
 [\tau]=1_{U_S},\quad[1]=\epsilon,\quad[n]=n\epsilon.
\tag{SS1.2}
\]
The bracket map is injective on the specified source carrier and preserves every defined source operation, as proved in ST5. It is not an identification of the source with this ring, and its new sums do not define sums of primitive \(\tau\).

At the source closed point the only denominator is \(\tau\), so its universal local receiver is \(U_S\). At an arithmetic basic open \(D(n)\), the universal ring is
\[
 U_S[[n]^{-1}]\cong\mathbb Z[1/n].
\tag{SS1.3}
\]
To prove it, \([n]=n\epsilon\) becomes invertible. The equation \(\epsilon[n]=[n]\) then gives \(\epsilon=1\). Thus the remaining ring is \(\mathbb Z[1/n]\). Conversely that ring receives the source localization by \(s/u\mapsto c(s)/c(u)\), with \(c(s)=1s\), and makes \([n]\) invertible. The two maps fix all integer fractions and are inverse. This proves both the ring identification and its universal property, without cancelling an element in the unlocalized source.

Equivalently, constructing the receiving ring commutes with these specified localizations. A ring map from either side is precisely a map preserving the source's defined operations and making the indicated denominator images invertible. This gives the same universal factorization in both directions.

At an arithmetic prime the resulting ring is \(\mathbb Z_{(p)}\), and at the arithmetic generic point it is \(\mathbb Q\). All local additions there are operations on the explicitly localized integer receiver.

## SS2. Construction and proof of the sheaf

Define \(\mathcal R\) on the complete list of opens by
\[
 \mathcal R(X)=U_S,\qquad
 \mathcal R(U)=\mathcal O_{\mathbb Z}(U)\quad
 (U\subseteq X_{\mathbb Z}),
\tag{SS2.1}
\]
where \(\mathcal R(\varnothing)\) is the zero ring. For nonempty \(U=D(n)\), this means exactly \(\mathbb Z[1/n]\). The restriction from \(X\) to \(D(n)\) is
\[
 a+b\epsilon\longmapsto a+b\quad\text{in }\mathbb Z[1/n].
\tag{SS2.2}
\]
All other restrictions are the original inclusions of the stated fraction rings. These maps are the local universal maps from SS1 and compose correctly.

Here is a direct sheaf proof. A covering of \(X\) must contain \(X\) itself, because it must cover \(\mathfrak m\). Gluing on such a covering is therefore immediate from the matching condition. For an open \(U\subseteq X_{\mathbb Z}\), every nonempty covering member contains the generic point. Matching sections in their rational stalk are thus one and the same rational number \(q\). At each arithmetic prime of \(U\), the section is regular on some covering member, so that prime does not divide the reduced denominator of \(q\). Consequently the denominator has prime factors only among the finitely many primes excluded by \(U=D(n)\). Hence \(q\in\mathbb Z[1/n]\), which gives the unique glued section. This proves the sheaf axiom on every open.

Its stalks, computed from these restriction maps, are
\[
 \mathcal R_{\mathfrak m}=U_S,\qquad
 \mathcal R_{(p)}=\mathbb Z_{(p)},\qquad
 \mathcal R_{(0)}=\mathbb Q.
\tag{SS2.3}
\]
The first equality follows because \(\mathfrak m\) has only the neighbourhood \(X\). The others follow by allowing all denominators absent from the specified arithmetic prime. These are exactly the universal additive receivers of the source stalks, not different stalks inferred only from an analogy.

The source monoid sheaf maps to \(\mathcal R\) by its actual receiving maps on each localization. On \(X\), the bracket map is faithful. On \(D(1)\), the original \(\tau,1\) distinction is identified by the explicitly nonfaithful localization \(c(s)=1s\). No source parity is assigned to \(\tau\).

## SS3. The exact product decomposition and its maps

There is a receiving-ring isomorphism
\[
 \Psi:U_S\longrightarrow\mathbb Z\times\mathbb Z,\qquad
 f(\epsilon)\longmapsto(f(1),f(0)),
\tag{SS3.1}
\]
with inverse
\[
 (a,b)\longmapsto a\epsilon+b(1_{U_S}-\epsilon).
\tag{SS3.2}
\]
Multiplication is componentwise because
\(\epsilon(1-\epsilon)=0\) and both components are idempotent. Composing the maps verifies that they are inverse on \(1_{U_S}\) and \(\epsilon\), hence on every element. These are coordinates in the receiving ring, not coordinates of primitive \(\tau\).

For a sheaf \(\mathcal F\) on \(X_{\mathbb Z}\), \(j_*\mathcal F(U)=\mathcal F(U\cap X_{\mathbb Z})\). For an abelian group or ring \(B\) on the single closed point, \(i_*B(U)=B\) when \(U=X\), and is zero when \(U\subseteq X_{\mathbb Z}\). Direct inspection of SS2 now proves the ring-sheaf isomorphism
\[
 \boxed{\mathcal R\cong j_*\mathcal O_{\mathbb Z}\times i_*\mathbb Z.}
\tag{SS3.3}
\]
On \(X\) it is \(\Psi\); on every proper open it is the identity of \(\mathcal O_{\mathbb Z}(U)\) with its product with the zero ring. The restrictions commute because restriction from \(X\) is first projection followed by the integer localization.

The restriction map and its exact kernel are
\[
 r:\mathcal R\longrightarrow j_*\mathcal O_{\mathbb Z},
\qquad
 \ker r=i_*\mathbb Z=(1_{U_S}-\epsilon)\mathcal R.
\tag{SS3.4}
\]
There is the canonical additive and \(\mathcal R\)-linear section
\[
 s_+:\ j_*\mathcal O_{\mathbb Z}\longrightarrow\mathcal R,
\qquad a\longmapsto(a,0)\text{ on }X,
\tag{SS3.5}
\]
which is the identity on proper opens. It preserves multiplication but is not globally unital: it sends the unit to \(\epsilon\), not to \(1_{U_S}\). The boundary inclusion \(b\mapsto(0,b)\) is likewise the inclusion of an idempotent corner. Thus
\[
 0\longrightarrow i_*\mathbb Z\longrightarrow\mathcal R
 \xrightarrow r j_*\mathcal O_{\mathbb Z}\longrightarrow0
\tag{SS3.6}
\]
is a canonically split sequence of abelian sheaves and \(\mathcal R\)-modules. No section preserving the source integer inclusion is falsely called a globally unital map.

For completeness a different unital ring-sheaf section of \(r\) does exist: on \(X\), \(a\mapsto(a,a)\), and on proper opens the identity. Compatibility follows from first projection. It does **not** preserve the specified source integer inclusion \(n\mapsto(n,0)\). The two maps differ by the explicit boundary component \((0,a)\). The source-compatible cohomological splitting used below is SS3.5, not this altered source map.

The inverse-image sheaves are
\[
 j^{-1}\mathcal R=\mathcal O_{\mathbb Z},\qquad
 i^{-1}\mathcal R=U_S\cong\mathbb Z\times\mathbb Z.
\tag{SS3.7}
\]
In particular the closed stalk is the whole product, not merely the support summand. If one specifies the closed receiving ring to be \(\mathbb Z\) through second projection \(U_S\to\mathbb Z\), the module pullback is
\[
 i^*\mathcal M=\mathbb Z\otimes_{U_S}\mathcal M_{\mathfrak m}
 \cong(1-\epsilon)\mathcal M_{\mathfrak m}.
\tag{SS3.8}
\]
This construction is distinct from the inverse image in SS3.7 and will agree with the support part for \(\mathcal R\).

## SS4. Global cohomology on \(X\), and the arithmetic open

For **any** sheaf of abelian groups \(\mathcal F\) on \(X\),
\[
 \Gamma(X,\mathcal F)=\mathcal F_{\mathfrak m}.
\tag{SS4.1}
\]
There is only one neighbourhood in the stalk limit. Since exactness of sheaves of abelian groups is tested on stalks, this proves that \(\Gamma(X,-)\) is an exact functor. Hence
\[
 H^q(X,\mathcal F)=0\quad(q>0)
\tag{SS4.2}
\]
for this precise topological site. This does not identify it with a different arithmetic, étale, or derived programme site.

We also need the arithmetic-open calculation, which is supplied explicitly. On \(U=X_{\mathbb Z}\), let \(\mathcal Q\) have value \(\mathbb Q\) on every nonempty open and zero on the empty open. For every ordinary prime \(p\), put \(D_p=\mathbb Q/\mathbb Z_{(p)}\), and define
\[
 \mathcal P(V)=\bigoplus_{\substack{p\in V\\p\text{ closed}}}D_p
\quad(V\subseteq U),
\tag{SS4.3}
\]
with restriction the coordinate projection. All sums of sections here have finite support.

These are sheaves. For \(\mathcal Q\), every nonempty open intersection contains the generic point, so matching sections are one rational number. For \(\mathcal P\), every open of \(U\) is quasi-compact: choose one nonempty member of any cover; its complement in the given open contains only finitely many closed points, so finitely many further members cover those. Compatible finite-support sections therefore glue with finite support. Both \(\mathcal Q\) and \(\mathcal P\) are flabby: nonempty restriction in \(\mathcal Q\) is identity, and a finite tuple in \(\mathcal P\) extends by zero in additional coordinates.

The maps
\[
 0\longrightarrow\mathcal O_{\mathbb Z}
 \longrightarrow\mathcal Q
 \xrightarrow d\mathcal P\longrightarrow0,\qquad
 d(q)_p=q\bmod\mathbb Z_{(p)}
\tag{SS4.4}
\]
are exact on every open. Only denominator primes give nonzero residues, so \(d(q)\) has finite support. Its kernel on \(V=D(n)\) is precisely \(\mathbb Z[1/n]\). For surjectivity, a class in \(D_p\) has a representative \(a/p^k\): for a fraction \(a/(p^kb)\), with \(p\nmid b\), choose \(c\) such that \(cb\equiv a\pmod{p^k}\); the difference from \(c/p^k\) belongs to \(\mathbb Z_{(p)}\). For a finite tuple of such classes, sum their representatives. Each representative is integral at the other primes, so this rational number has exactly the prescribed residue tuple.

Thus SS4.4 is a flabby resolution whose global section sequence is also exact. It follows that
\[
 H^0(U,\mathcal O_{\mathbb Z})=\mathbb Z,\qquad
 H^q(U,\mathcal O_{\mathbb Z})=0\quad(q>0).
\tag{SS4.5}
\]
The same proof applies on every \(D(n)\), with \(\mathbb Z[1/n]\) in degree zero.

Here the cohomological fact used about a flabby resolution is the usual derived-functor calculation, not a purity premise. One proof is to embed a flabby sheaf in an injective sheaf. Sections of its quotient lift globally: first choose local lifts and well-order a cover; at each step their difference on an overlap lies in the flabby kernel and extends to the new open, so subtract that extension before gluing; at a limit stage use the sheaf gluing axiom. The same construction on smaller opens shows that the quotient is flabby. Induction in an injective resolution makes the global section complex exact in positive degrees. This proves the acyclicity used in the displayed resolution.

## SS5. Local cohomology, restriction and every connecting map

For the closed set \(Z=\{\mathfrak m\}\), define the supported-section functor
\[
 \Gamma_Z(X,\mathcal F)=
 \ker\bigl(\mathcal F(X)\to\mathcal F(U)\bigr),
\quad U=X_{\mathbb Z}.
\tag{SS5.1}
\]
This constructs the operation whose derived functors are being calculated. The usual restriction exact triangle is obtained by applying an injective or flabby resolution to the supported-section kernel. Since flabby restrictions are onto, the resulting sequence of complexes is short exact and gives
\[
 R\Gamma_Z(X,\mathcal F)\longrightarrow
 R\Gamma(X,\mathcal F)\longrightarrow
 R\Gamma(U,\mathcal F|_U)\longrightarrow
 R\Gamma_Z(X,\mathcal F)[1].
\tag{SS5.2}
\]
This also proves the long exact sequence used below; it is not an assumed geometric specialization triangle.

For \(\mathcal R\), the middle and open terms have already been computed:
\[
 R\Gamma(X,\mathcal R)=U_S[0]\cong(\mathbb Z\oplus\mathbb Z)[0],
 \qquad
 R\Gamma(U,\mathcal R|_U)=\mathbb Z[0].
\tag{SS5.3}
\]
The arrow is exactly first projection. Its kernel is the second summand and its cokernel is zero. Consequently
\[
 \boxed{
 H_Z^0(X,\mathcal R)=(1-\epsilon)U_S\cong\mathbb Z,\qquad
 H_Z^q(X,\mathcal R)=0\quad(q>0).
 }
\tag{SS5.4}
\]
Equivalently \(R\Gamma_Z(X,\mathcal R)\) is represented by the two-term complex
\[
 [\,U_S\xrightarrow{\pi_+}\mathbb Z\,]
\quad\text{in degrees }0,1.
\tag{SS5.5}
\]
Its arithmetic component is the contractible complex
\([\,\mathbb Z\xrightarrow{\mathrm{id}}\mathbb Z\,]\), and its other component is \(\mathbb Z\) in degree zero. A contracting homotopy on that first component sends its degree-one element back to the same degree-zero integer. Thus the vanishing has an explicit chain-level calculation.

The exact section \(s_+(a)=(a,0)\) lifts every open global class. The connecting map
\[
 \partial:\mathbb Z=H^0(U,\mathcal O_{\mathbb Z})
 \longrightarrow H_Z^1(X,\mathcal R)
\]
is zero. This follows both from the target calculation and directly from the displayed section and homotopy. All higher connecting maps vanish because the already calculated source or target groups are zero. This proves an actual lifting statement from the sheaf's original source-induced restriction map.

The internal local-cohomology sheaves satisfy
\[
 \mathcal H_Z^0(\mathcal R)=i_*\mathbb Z,\qquad
 \mathcal H_Z^q(\mathcal R)=0\quad(q>0).
\tag{SS5.6}
\]
Their stalks outside \(Z\) vanish by restricting to the open complement. At \(\mathfrak m\), their only neighbourhood is \(X\), giving exactly SS5.4. In the customary notation for the supported right adjoint, this says \(i^!\mathcal R=\mathbb Z[0]\), in contrast with \(i^{-1}\mathcal R=U_S\) in SS3.7. There is no hidden degree shift or Tate twist.

The same computation proves \(R^qj_*\mathcal O_{\mathbb Z}=0\) for \(q>0\). At an arithmetic stalk use the cofinal neighbourhoods \(D(n)\) and SS4.5; at \(\mathfrak m\) use \(U\) itself and SS4.5. Hence the sheaf-level triangle is the actual split
\[
 i_*\mathbb Z[0]\longrightarrow\mathcal R[0]
 \longrightarrow j_*\mathcal O_{\mathbb Z}[0]\longrightarrow
 i_*\mathbb Z[1],
\tag{SS5.7}
\]
with zero last arrow and the maps of SS3.

## SS6. The two components of the receiving spectrum and the exact map back

Let
\[
 Y=\operatorname{Spec}U_S.
\]
The ring product SS3.1 gives two complete components:
\[
 Y=Y_+\sqcup Y_-,\qquad
 Y_+\simeq\operatorname{Spec}\mathbb Z,\quad
 Y_-\simeq\operatorname{Spec}\mathbb Z.
\tag{SS6.1}
\]
Here \(Y_+=D(\epsilon)\), \(Y_-=D(1-\epsilon)\). To verify that these exhaust the prime spectrum, in a prime ideal one of the two orthogonal idempotents must lie in the ideal, since their product is zero; they cannot both lie in it, since their sum is the unit. The remaining component is a prime ideal in its copy of \(\mathbb Z\).

For every ordinary ring prime \(\mathfrak p\subset\mathbb Z\), including \(\mathfrak p=(0)\), write
\[
 \mathfrak q_{+,\mathfrak p}=\mathfrak p\times\mathbb Z,\qquad
 \mathfrak q_{-,\mathfrak p}=\mathbb Z\times\mathfrak p.
\tag{SS6.2}
\]
Contracting along the source receiving map \(S\to U_S\) gives
\[
 f(\mathfrak q_{+,\mathfrak p})=\mathfrak p\subset S,
 \qquad
 \boxed{f(\mathfrak q_{-,\mathfrak p})=\mathfrak m
 \text{ for every }\mathfrak p.}
\tag{SS6.3}
\]
Indeed the original integer \(n\) maps to \((n,0)\), so it lies in \(\mathfrak q_{+,\mathfrak p}\) exactly when \(n\in\mathfrak p\), while every original integer lies in every \(\mathfrak q_{-,\mathfrak p}\). The formal image of \(\tau\) is the global ring unit \((1,1)\), which belongs to neither kind of prime. Thus each contraction is an actual compatible source prime, as required.

The map \(f:Y\to X\) is continuous:
\[
 f^{-1}(D(n))=D_Y(n\epsilon)
 =D_{\mathbb Z}(n)\subset Y_+\quad(n\ne0),
\qquad
 f^{-1}(X)=Y.
\tag{SS6.4}
\]
These are all the needed basic opens. On \(Y_+\), \(f\) is the homeomorphism onto \(X_{\mathbb Z}\). Its entire fibre at \(\mathfrak m\) is the second copy \(Y_-\), with its generic point, every arithmetic closed point, their specializations, and their residue fields retained.

This continuous surjection is not a topological quotient: \(f^{-1}(\{\mathfrak m\})=Y_-\) is open, but \(\{\mathfrak m\}\) is not open in \(X\). This states its actual topology rather than pretending that collapsing the second component would automatically reproduce the source topology.

The receiving sheaf is exactly its direct image:
\[
 \boxed{f_*\mathcal O_Y=\mathcal R.}
\tag{SS6.5}
\]
On \(X\), both sides have sections \(\mathbb Z\times\mathbb Z\). On \(U'\subseteq X_{\mathbb Z}\), its inverse image is the same open in \(Y_+\) and contains none of \(Y_-\), giving \(\mathcal O_{\mathbb Z}(U')\). All restriction maps agree. The adjoint \(f^{-1}\mathcal R\to\mathcal O_Y\) gives an exact morphism of ringed spaces. At a plus prime, the stalk map is the corresponding arithmetic localization. At a minus prime it is
\[
 U_S\cong\mathbb Z\times\mathbb Z
 \xrightarrow{\pi_-}\mathbb Z
 \longrightarrow\mathbb Z_{(\mathfrak p)},
\tag{SS6.6}
\]
where \(\mathbb Z_{((0))}=\mathbb Q\).

The stalk \(\mathcal R_{\mathfrak m}=U_S\) is not a local ring: it has the two nonzero complementary idempotents. In a local ring one of \(e,1-e\) must be a unit, forcing the other to be zero, so that situation cannot occur. Thus \((X,\mathcal R)\) is the constructed ringed receiving space; it is not asserted to be a scheme with this structure sheaf. The actual affine scheme is \(Y\), and the map and all its fibres are displayed rather than erased.

The added receiving primes of \(Y_-\) must be distinguished from original integer primes. The original source integer \(n\) has image \(n\epsilon=(n,0)\), which is zero on the entire minus component. The ordinary ring scalar \(n1_{U_S}=(n,n)\) can distinguish its different primes. The latter uses the newly constructed receiving ring's integer scalar operation and is not the source integer embedding. No expression counting copies of primitive \(\tau\) has been defined. This distinction explains exactly why the additional ring primes occur and why contraction groups them over one source point.

The higher direct images \(R^qf_*\mathcal O_Y\) vanish for \(q>0\): on the preimages of \(X\) and of the arithmetic basic opens, use SS4's explicit acyclicity for each of the one or two copies. Consequently SS6.5 also identifies the complete derived direct image on this structure sheaf.

## SS7. What the splitting says for coefficients and independent Frobenius

The global idempotent \(\epsilon\) decomposes every sheaf of \(\mathcal R\)-modules as
\[
 \mathcal M=\epsilon\mathcal M\oplus(1-\epsilon)\mathcal M.
\tag{SS7.1}
\]
This follows on each section from \(m=\epsilon m+(1-\epsilon)m\), zero intersection, and compatibility with restrictions. The second summand is supported at \(\mathfrak m\), because \(1-\epsilon=0\) on \(X_{\mathbb Z}\). It is therefore \(i_*B\), where \(B=((1-\epsilon)\mathcal M)_{\mathfrak m}\).

For a general \(\mathcal M\), it does **not** follow that
\(\epsilon\mathcal M=j_*j^{-1}\mathcal M\). There can be extra data in its \(\mathfrak m\)-stalk and in the restriction map. The exact comparison is
\[
 \epsilon\mathcal M\longrightarrow j_*j^{-1}\mathcal M,
\tag{SS7.2}
\]
with its actual kernel and cokernel supported at \(\mathfrak m\); away from that point it is the identity. Because the only neighbourhood of \(\mathfrak m\) is \(X\), these groups are explicitly the kernel and cokernel of
\[
 (\epsilon\mathcal M)(X)\longrightarrow
 \Gamma(X_{\mathbb Z},j^{-1}\mathcal M).
\tag{SS7.3}
\]
For the particular structure sheaf \(\mathcal M=\mathcal R\), this map is an isomorphism on the epsilon component by SS3.3, so these extra groups are zero. The scope of the proved lifting must not be enlarged by omitting SS7.2 for other coefficients.

Let a specified independent Frobenius or idèle action \(F\) on the receiving sheaf or complex preserve the source action, hence commute with \(\epsilon\). Then it preserves both parts of SS7.1, their inclusion and their projection. For \(\mathcal R\)'s split restriction complex SS5.5, the lift through the epsilon summand is equivariant and the support connecting map remains zero. This is a proved consequence of the source-induced idempotent, not an assigned numerical weight of primitive \(\tau\).

A unital ring-sheaf endomorphism over the identity on \(X\) that fixes the source receiving map is necessarily the identity on \(\mathcal R\). On \(X\) it fixes \(\epsilon\) and the global unit, hence every element of \(U_S\). On each arithmetic \(D(n)\), it fixes every integer and every allowed inverse, hence every element of \(\mathbb Z[1/n]\). This proves the claim on all opens. Nontrivial numerical Frobenius actions therefore require their stated coefficient objects or geometric correspondences; they are not manufactured by calling source multiplication a unital ring endomorphism.

At the coefficient-module level the exact situation is different and is already classified by the split. Over \(\mathbb C\), on the two components of
\(\mathcal R\otimes_{\mathbb Z}\mathbb C\), any two specified invertible coefficient actions commute with the source idempotent. They can have different numerical eigenvalues while the section and all connecting maps still split. More generally the actual \(Q\) and \(\mathcal B_{\rm pr}\) actions of ST6.3 can be retained as independently named coefficient actions. This observation is a classification of the constructed receiver, not an arbitrary-parameter counterexample to the user's full geometric programme.

Source integer multiplication on the sheaf is multiplication by \([n]=n\epsilon\); it acts by \(n\) on the arithmetic part and by zero on the supported part. The independent idèle boundary action in ABR19 is instead \(\operatorname{diag}(1,b)\). Their exact coexistence and the norm/power-map comparison are ST6–ST7a. In particular no logarithmic Frobenius weight is assigned to the zero scalar operator on the supported source corner, and no invertible geometric action is identified with that zero operator.

## SS8. Relation to the cited geometric programmes

The source calculation begins with the user's current \(Z_0,Z_1,Z_2,\tau\) definitions and the completed integer layer. The arithmetic open, the extra source point, the universal receiving spectrum and the supported sheaf have each been constructed from those inputs. The original source \(S\) and its monoid sheaf remain in the diagram; no ring operation from \(\mathcal R\) has been made a new source operation.

The exact geometric distinction used in the comparison is also present in Alain Connes and Caterina Consani, [*On the Jacobian of \(\overline{\operatorname{Spec}\mathbb Z}\)*](https://arxiv.org/abs/2602.15941v1), original [Jacobian.tex](https://arxiv.org/abs/2602.15941v1), lines 2501–2550: their number-field spectral action is idèle translation, whereas their function-field comparison uses arithmetic Frobenius. ST7 proves the connecting power-map, pullback and norm formulas; SS7 preserves both actions instead of replacing one by the other.

Pierre Deligne's lifting argument in [*La conjecture de Weil. II*](https://www.numdam.org/item/PMIHES_1980__52__137_0/), §3.6.1–§3.6.3, kills a geometric support obstruction by separated Frobenius weights. Here the actual source-induced additive sheaf has its support obstruction killed by the explicit idempotent splitting, and SS5 computes the full local cohomology and connecting maps. This is a proved lifting statement for this sheaf. Neither this splitting, which does not involve numerical weights, nor the topology's exact global-sections functor proves that a different cohomology theory has only weight one.

The explicit remaining comparison is not hidden: other programme coefficient complexes enter through SS7.2 and the independently specified geometric action. The current result does not assert that their restriction maps, or Deligne's entire proper specialization complex, are this structure-sheaf sequence. All the kernels, additional receiving primes, source localization fibres and support maps needed to compare them are retained.

## SS9. Exact conclusions

The universal additive receiving sheaf of the current source is
\[
 \mathcal R=j_*\mathcal O_{\mathbb Z}\times i_*\mathbb Z.
\]
Its closed stalk is \(U_S=\mathbb Z\times\mathbb Z\); its supported part is only the second copy. Its local cohomology at the added source point is \(\mathbb Z\) in degree zero and zero in higher degrees. Every connecting map for this restriction sequence is zero, with an explicit equivariant additive section.

The affine receiving spectrum contains two entire copies of \(\operatorname{Spec}\mathbb Z\). One maps identically to the source arithmetic open; the other, with all its primes retained, contracts to the added source point. The direct image of its structure sheaf is exactly \(\mathcal R\).

These are actual sheaf and source-specialization results. No source addition on \(\tau\), no source parity for it, no erasure of the added ring primes, and no RH or purity assertion has been introduced.
