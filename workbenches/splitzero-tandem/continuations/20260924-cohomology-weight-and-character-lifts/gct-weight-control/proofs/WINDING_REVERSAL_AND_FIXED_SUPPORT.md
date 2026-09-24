# Winding reversal, exchanged data, and the fixed supporting point

24 September 2026. Proof locators WR1–WR9. This note receives the question whether reversing a winding based at the common supporting point creates handedness, and whether that would contradict the point's proved absence of an exchanged parity label. It computes the actual source involution and its receiving maps. The support is always \(\tau\langle Z_1;\mathrm{no}\ Z_2\rangle\), in the precise exchanged-point-label sense proved below. No arithmetic, coordinate, metric or vector is assigned to that support. The stalk group is not identified with a fundamental group.

## Original source actually read

Alain Connes and Caterina Consani, [The Absolute Twistor Line and the Geometry of the compactified Spec Z, arXiv:2609.00299v1](https://arxiv.org/html/2609.00299v1), original author file `CC.tex`, SHA-256 `57a10dcef5cd758e6b2f1c54b1c0a11b0fb093638f74fb1be515ec3bc7080ba4`.

Passages read for this calculation: lines 314–326, equation `F2`, retains \(\epsilon^2=1\); lines 492–612, especially `opens1`, `opens`, `eq:restriction_maps`, give the topology, generic group and both twisted restrictions; lines 765–852, definition `def:alpha_symmetry`, give the actual action on points and sections with its chart compatibility; lines 875–904 give the invariant base and the generic-point isotropy. These author passages supply the source data. All group, character and descent calculations below are proved here.

For the final arithmetic comparison we use the already proved original-zeta action from `ORIGINAL_ZETA_RESOLVENT_AND_PROJECTORS.md`, RZ8–RZ11, and `INTEGRAL_FROBENIUS_TRANSFER_ALGEBRA.md`, FT5. The comparison retains the degree factor \(n\) and every multiplicity jet. It does not identify the source's signed involution with an unweighted analytic inverse.

## WR1. The common supporting point and the full generic data

The underlying unfolded space and its chart overlap are
\[
X=\{+,-,\eta\},\qquad
\Omega_+=\{+,\eta\},\quad
\Omega_-=\{-,\eta\},\quad
\Omega_+\cap\Omega_-=\{\eta\}.
\tag{WR1.1}
\]
The nonempty proper opens are exactly these three sets. The involution exchanges the two closed points. A homeomorphism must fix \(\eta\), because its singleton is the unique dense singleton; the singleton of either closed point is closed. Hence its fixed-point set on \(X\) is exactly \(\{\eta\}\).

The group of nonabsorbing generic monomials, retaining all source commutations, is
\[
G=\langle T,J,\epsilon:
TJ=JT,\ T\epsilon=\epsilon T,\ J\epsilon=\epsilon J,
\ J^2=\epsilon,\ \epsilon^2=1\rangle.
\tag{WR1.2}
\]
The separate absorbing section of the pointed source is outside this group. It is neither removed from that pointed source nor identified with the supporting point in this calculation.

Every group element has a unique expression
\[
g=T^mJ^k,\qquad m\in\mathbb Z,\quad k\in\mathbb Z/4\mathbb Z.
\tag{WR1.3}
\]
To prove uniqueness as well as existence, the relations give a homomorphism \(G\to\mathbb Z\times C_4\), sending \(T\) to \((1,0)\), \(J\) to \((0,1)\) and \(\epsilon\) to \((0,2)\). Its inverse sends \((m,k)\) to \(T^mJ^k\); it is well defined because \(J^4=1\). Both composites fix the specified generators, so both are identities.

The actual restrictions are also retained:
\[
\rho_+(T^mJ_+^k)=T^mJ^k\quad(m\ge0),\qquad
\rho_-(T^mJ_-^k)=T^m(\epsilon J)^k\quad(m\le0).
\tag{WR1.4}
\]
The finite subgroup is \(H=\langle J\rangle\cong C_4\). The complete winding quotient and its kernel are
\[
1\longrightarrow H\longrightarrow G
\xrightarrow{q}L_{\mathrm w}=G/H\longrightarrow1,
\qquad L_{\mathrm w}\cong\mathbb Z.
\tag{WR1.5}
\]
No element of this exact sequence is identified with \(\eta\).

## WR2. The full involution, its fixed elements and its two comparison maps

On the group write \(\alpha\) for the source's \(\alpha^*\). Its exact formulas are
\[
\alpha(T)=\epsilon T^{-1},\qquad
\alpha(J)=J^{-1}=\epsilon J,\qquad
\alpha(\epsilon)=\epsilon.
\tag{WR2.1}
\]
For every element in (WR1.3),
\[
\alpha(T^mJ^k)=\epsilon^mT^{-m}J^{-k}
=T^{-m}J^{2m-k},
\qquad \alpha(m,k)=(-m,2m-k).
\tag{WR2.2}
\]
Applying this coordinate rule twice gives \((m,k)\), including the full residue modulo four, proving the involution property.

Its fixed subgroup is exactly
\[
\boxed{G^\alpha=\{1,\epsilon\}.}
\tag{WR2.3}
\]
Indeed equality of the winding coordinates in \((m,k)=(-m,2m-k)\) gives \(m=0\). The remaining condition is \(2k=0\) modulo four, so \(k=0\) or \(k=2\). Conversely both displayed elements are fixed. Together with the separate fixed absorbing section, this recovers the source's pointed invariant base \(\{0,1,\epsilon\}\) at the monomial level. This does not turn those sections into three underlying supporting points.

The product with the reversed datum and the quotient by the original datum are respectively
\[
N(g):=g\alpha(g)=\epsilon^m,
\tag{WR2.4}
\]
\[
D(g):=\alpha(g)g^{-1}
=T^{-2m}J^{2m-2k}
=T^{-2m}\epsilon^{m-k}.
\tag{WR2.5}
\]
Both are group homomorphisms, because the source group is abelian. Their exact images and kernels are
\[
\operatorname{im}N=\{1,\epsilon\},\qquad
\ker N=\langle T^2,J\rangle,
\tag{WR2.6}
\]
\[
\ker D=\{1,\epsilon\},\qquad
\operatorname{im}D=\langle T^2,\epsilon\rangle.
\tag{WR2.7}
\]
The norm assertions follow directly from whether \(m\) is even. For the second image, (WR2.5) has even winding exponent and even \(J\)-exponent. Conversely \(D(J)=\epsilon\) and \(D(T)=\epsilon T^{-2}\), so their products generate both \(\epsilon\) and \(T^2\). The kernel is precisely the fixed subgroup already proved.

These formulas keep a small remaining quotient explicit:
\[
\ker N/\operatorname{im}D\cong C_2,
\qquad [J]\text{ generates it},\quad [J]^2=[\epsilon]=1.
\tag{WR2.8}
\]
Every element of \(\ker N\) has the form \(T^{2a}J^k\); quotienting by \(T^2\) and \(\epsilon=J^2\) leaves exactly \(k\) modulo two. This proves the quotient, without identifying it with an unstated cohomology or loop space.

## WR3. Handedness of winding and parity of the winding count

The involution induces inversion on \(L_{\mathrm w}\): in exponent coordinates, \(m\mapsto-m\). On its nonzero winding elements, a choice of the positive source chart defines the exchanged label
\[
o(m)=
\begin{cases}\mathrm{right},&m>0,\\
\mathrm{left},&m<0.
\end{cases}
\qquad o(-m)=\operatorname{flip}(o(m)).
\tag{WR3.1}
\]
Reversing the initial chart exchanges the two names. Thus the two-state information is the two possible orientations, with no assertion that one of the names is intrinsically preferred. The sign of a nonzero winding changes under reversal.

There is also the count-parity map already derived from the signed product:
\[
\delta:L_{\mathrm w}\longrightarrow\{1,\epsilon\},\qquad
\delta(m)=\epsilon^m,
\quad\ker\delta=2L_{\mathrm w}.
\tag{WR3.2}
\]
It is well defined because the product \(g\alpha(g)\) is independent of the finite \(J\)-label. Unlike (WR3.1), its value satisfies
\[
\delta(-m)=\epsilon^{-m}=\epsilon^m=\delta(m).
\tag{WR3.3}
\]
Thus the source gives two explicitly related observations: reversal exchanges the orientation, and it preserves whether the integer winding count is even or odd. Both take two possible values, but their involution actions are different. These equations specify the distinction rather than erasing either symmetry.

The zero-winding fiber still contains the four finite-order states \(1,J,\epsilon,J^3\). The states \(1,\epsilon\) are fixed, while \(J,J^3\) are exchanged. Therefore zero winding alone is not an assertion that every remaining phase datum is fixed.

The connection with counting is also exact on the full signed lift. Write \(A_G=\alpha\) as a permutation of \(G\), and define the permutations
\[
S(g)=Tg,\qquad E(g)=\epsilon g.
\tag{WR3.4}
\]
These last two maps are translations of the stalk group, not group homomorphisms fixing its identity. The map \(S\) uses the positive chart's primitive generator; reversing the chosen chart changes that oriented choice. Direct substitution gives
\[
A_G S A_G(g)=\alpha(T\alpha(g))
=\epsilon T^{-1}g=E S^{-1}(g),
\tag{WR3.5}
\]
\[
E^2=I,\qquad ES=SE,\qquad EA_G=A_GE.
\tag{WR3.6}
\]
The first equality uses \(\epsilon^2=1\), the second the source commutation of \(T,\epsilon\), and the third \(\alpha(\epsilon)=\epsilon\). Thus the full signed counting/reversal relation is \(A_GSA_G=ES^{-1}\); its factor \(E\) has not been suppressed.

Pass through the retained quotient \(q:G\to L_{\mathrm w}\), on which \(E\) becomes the identity because \(\epsilon\in H\). In winding exponent coordinates the induced permutations are
\[
S_{\mathrm w}(m)=m+1,\qquad R_{\mathrm w}(m)=-m,
\qquad R_{\mathrm w}S_{\mathrm w}R_{\mathrm w}=S_{\mathrm w}^{-1}.
\tag{WR3.7}
\]
All three identities follow by evaluating at \(m\); for the last, \(m\mapsto-m\mapsto-m+1\mapsto m-1\). This is the quotient comparison of the full lifted relation, not a replacement of (WR3.5).

Let \(\pi_{\mathrm{par}}(g)=g\alpha(g)=\epsilon^m\). The exact observation identities are
\[
\pi_{\mathrm{par}}(Sg)=\epsilon\pi_{\mathrm{par}}(g),
\qquad \pi_{\mathrm{par}}(A_Gg)=\pi_{\mathrm{par}}(g),
\qquad \pi_{\mathrm{par}}(Eg)=\pi_{\mathrm{par}}(g).
\tag{WR3.8}
\]
The first follows from \((Tg)\alpha(Tg)=\epsilon g\alpha(g)\), the second from \(\alpha(g)g=g\alpha(g)\), and the third from \(\epsilon\alpha(\epsilon)=1\). Therefore a one-step advance in the complete winding history flips the parity observation; reversing the entire history preserves that observation while exchanging the nonzero-winding handedness (WR3.1).

This also types the user's half-turn counting picture precisely at the observation level: \(S\) lifts the order-two flip on \(\{1,\epsilon\}\), but \(S\) itself retains the winding history and has infinite order. Indeed \(S^ng=T^ng\), which equals \(g\) only for \(n=0\), by the unique coordinate in (WR1.3). Thus no identification of the full counting step with an order-two geometric self-map has been inserted. The source involution \(A_G\) and the counting translation \(S\) have the exact relation (WR3.5), rather than being declared the same map.

## WR4. The exact forgetful map and the obstruction to label descent

Form the set of decorated support data
\[
\mathcal E=\{\eta\}\times G,
\qquad \widetilde\alpha(\eta,g)=(\eta,\alpha(g)).
\tag{WR4.1}
\]
This product records a point with a stalk element. It is not a claim that the stalk is the fundamental group or that the product is the whole source sheaf. The actual operation of forgetting the stalk label is
\[
\pi:\mathcal E\longrightarrow\{\eta\},\qquad
\pi(\eta,g)=\eta.
\tag{WR4.2}
\]
It is equivariant, since
\[
\pi\widetilde\alpha(\eta,g)=\eta
=\alpha\pi(\eta,g).
\tag{WR4.3}
\]
Its source fixed set is \(\{\eta\}\times\{1,\epsilon\}\), by WR2; its entire target is fixed. In particular two exchanged decorations can have the same fixed support, as this explicit map proves.

Let \(\mathcal E_{\ne0}\) be the subset with nonzero winding. The handedness label \(o\) from (WR3.1) is an equivariant map from \(\mathcal E_{\ne0}\) to the free two-element exchange set \(Q_2\). It cannot factor through \(\pi\). If \(o=\bar o\circ\pi\), then for any element \(e\) of this subset,
\[
o(\widetilde\alpha e)=\bar o(\eta)=o(e),
\tag{WR4.4}
\]
whereas equivariance requires \(o(\widetilde\alpha e)=\operatorname{flip}(o(e))\ne o(e)\). This is a contradiction. The full two-to-one reversal orbit map on \(\mathcal E_{\ne0}\) consequently carries orientation data that the further map to the support does not retain.

Equivalently, an exchanged point-label directly at the support would require
\[
P(\alpha\eta)=\operatorname{flip}(P(\eta)),\quad
\alpha\eta=\eta,
\quad\text{hence }P(\eta)=\operatorname{flip}(P(\eta)),
\tag{WR4.5}
\]
which is impossible in \(Q_2\). This derives the support's \(\mathrm{no}\ Z_2\) exchange-label property. It neither removes the nontrivial action on its stalk nor removes the quotient stack's \(C_2\) stabilizer noted in the original source, lines 895–898. In particular an invariant parity observation such as (WR3.2) is not an exchanged point-label of the kind ruled out by (WR4.5).

## WR5. Rank-one characters and the complete signed duality

Every complex rank-one character \(\chi:G\to\mathbb C^\times\) is determined by
\[
a=\chi(T)\in\mathbb C^\times,\qquad
\omega=\chi(J),\quad\omega^4=1,\qquad
\chi(\epsilon)=\omega^2,
\tag{WR5.1}
\]
and has the full formula
\[
\chi(T^mJ^k)=a^m\omega^k.
\tag{WR5.2}
\]
The group presentation proves both existence for every displayed parameter pair and uniqueness. The support of this character datum remains \(\eta\).

Precomposition by the source involution gives
\[
\boxed{\chi\circ\alpha:
(a,\omega)\longmapsto(\omega^2a^{-1},\omega^{-1}).}
\tag{WR5.3}
\]
The ordinary dual character is \(\chi^{-1}\), with parameters \((a^{-1},\omega^{-1})\). Their exact comparison is
\[
(\chi\circ\alpha)(T^mJ^k)
=(\omega^2)^m\chi(T^mJ^k)^{-1}.
\tag{WR5.4}
\]
In particular the signed factor is not removed. For a character preserving the source's complex base sign \(\epsilon\mapsto-1\), one has \(\omega=+i\) or \(-i\), and the formula is \((a,\omega)\mapsto(-a^{-1},\omega^{-1})\).

The abstract characters fixed by (WR5.3) are exactly
\[
a\in\{1,-1\},\qquad \omega\in\{1,-1\}.
\tag{WR5.5}
\]
Indeed fixedness requires \(\omega=\omega^{-1}\), hence \(\omega^2=1\), and then \(a^2=\omega^2=1\). Both conditions are sufficient. Thus no base-sign-preserving character with \(\omega^2=-1\) is fixed by this operation, even though its underlying supporting point is fixed.

For completeness, combining source reversal with complex conjugation gives
\[
\overline{\chi\circ\alpha}:
(a,\omega)\longmapsto(\omega^2/\overline a,\omega).
\tag{WR5.6}
\]
Here \(|\omega|=1\), so \(\overline{\omega^{-1}}=\omega\) and \(\overline{\omega^2}=\omega^2\). Fixedness now requires \(|a|^2=\omega^2\). When \(\omega^2=1\), this is exactly \(|a|=1\); when \(\omega^2=-1\), there is no solution. These are statements about fixed character data, not about which characters may exist over the fixed supporting point. Every nonzero \(a\) in (WR5.1) still defines a valid abstract character.

The existence of an equivariant fiber does not require fixing one character. For any character \(\chi\), define on \(\mathbb C^2\)
\[
R_\chi(g)=\begin{pmatrix}\chi(g)&0\\0&(\chi\circ\alpha)(g)\end{pmatrix},
\qquad S=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\tag{WR5.7}
\]
Then \(S^2=I\) and direct multiplication proves
\[
S R_\chi(g)S^{-1}=R_\chi(\alpha(g)).
\tag{WR5.8}
\]
This is a representation of the actual semidirect product \(G\rtimes\langle\alpha\rangle\) on a fiber over the fixed support, with its exchanged summands retained. It is not asserted to be the full arithmetic cohomology or a source of zeta zeros. It proves that fixed support and exchanging fiber data coexist under the actual source group law, rather than under an unrelated model.

## WR6. The exact degree-weighted arithmetic character comparison

On the positive rational multiplicative group the actual spectral characters are
\[
\lambda_\rho(r)=r^\rho=\exp(\rho\log r),\qquad r>0,
\tag{WR6.1}
\]
with the real logarithm. Their degree-weighted conjugate dual is
\[
\lambda_\rho^{\dagger}(r)
=\frac{r}{\overline{\lambda_\rho(r)}}
=r^{1-\overline\rho}
=\lambda_{\rho^\#}(r),\qquad
\rho^\#=1-\overline\rho.
\tag{WR6.2}
\]
This formula retains the arithmetic degree character \(r\mapsto r\); it is not the unweighted reciprocal in (WR5.3).

There is a full signed comparison on each prime and each retained phase sector, rather than an assertion that the two dualities are unrelated. Fix a recovered prime norm \(p\), and for each of the four possible \(\omega\) consider characters \(\chi_{a,\omega}\) as in (WR5.2). Define the compensating character
\[
\mu_{p,\omega}(T)=p\omega^2,\qquad
\mu_{p,\omega}(J)=1,\qquad
\mu_{p,\omega}(\epsilon)=1.
\tag{WR6.3}
\]
Its values satisfy every group relation, so it is a well-defined character. Multiplying the full reversed-conjugate character by this character gives
\[
\mathfrak D_p\chi_{a,\omega}
:=\mu_{p,\omega}\,\overline{\chi_{a,\omega}\circ\alpha},
\qquad
\boxed{\mathfrak D_p(a,\omega)=(p/\overline a,\omega).}
\tag{WR6.4}
\]
Indeed the value at \(T\) is
\((p\omega^2)(\omega^2/\overline a)=p\omega^4/\overline a=p/\overline a\), while the value at \(J\) is \(\omega\). Thus both the degree factor and the signed compensation are displayed. The operation preserves each phase sector, including both base-sign-preserving sectors \(\omega=\pm i\). It squares to the identity because
\(p/\overline{p/\overline a}=a\), with the same \(\omega\).

For a lifted arithmetic character \(a=p^\rho\), (WR6.4) yields exactly \(p^{\rho^\#}\). Its fixed-character equation is
\[
a=p/\overline a\quad\Longleftrightarrow\quad |a|^2=p.
\tag{WR6.5}
\]
Substituting the actual arithmetic parameter gives
\[
|p^\rho|^2=p^{2\operatorname{Re}\rho}=p
\quad\Longleftrightarrow\quad\operatorname{Re}\rho=\tfrac12.
\tag{WR6.6}
\]
This calculation identifies precisely where the purity circle belongs: it is the fixed locus of the degree-weighted duality on character data. All those character data, whether individually fixed or exchanged, can have the same underlying support \(\eta\) through WR4. Fixedness of that support is therefore not the fixed-character equation (WR6.5).

The angular and radial effects can also be read without changing the scale. For a character value \(a=r e^{i\theta}\), with \(r>0\) and \(\theta\) taken modulo \(2\pi\),
\[
 a^{-1}=r^{-1}e^{-i\theta},\qquad
 \mathfrak D_p(a)=\frac{p}{\overline a}
                 =\frac{p}{r}e^{i\theta}.
\tag{WR6.7}
\]
These are coordinates of the complex character value, not of the supporting point. Unweighted inversion reverses the phase, while conjugation followed by degree-weighted inversion leaves the phase unchanged and exchanges the two radii \(r\) and \(p/r\). For the actual arithmetic value, retaining its original scale and imaginary part gives
\[
 p^\rho=p^{\operatorname{Re}\rho}
       e^{i(\operatorname{Im}\rho)\log p},\qquad
 p^{1-\overline\rho}=p^{1-\operatorname{Re}\rho}
       e^{i(\operatorname{Im}\rho)\log p}.
\tag{WR6.8}
\]
Thus the two operations whose factors were retained in WR6.4 have an explicitly calculated effect. The arithmetic reflection tests equality of these radii; it is not merely the reversal of clockwise versus counterclockwise phase. No radius or distance to \(\tau\) is introduced by this character calculation.

## WR7. The complete original-zeta action and all reversed multiplicity data

On the actual quotient \(\mathcal Q=\mathcal B/\mathcal I\) of RZ, the arithmetic operators are
\[
T_n[F]=[n^sF(s)],\qquad
\mathcal M^{-1}T_n\mathcal Mk(u)=n^{1/2}k(u/n).
\tag{WR7.1}
\]
The full source multiplier remains
\[
F_0(s)=\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2)\zeta(s),
\tag{WR7.2}
\]
with its endpoint and exceptional-point comparisons in the full synthesis proof. The working zeta is the original function; none of its original zeros or poles is replaced by a location assumption.

The reflected Weil form has the exact adjoint identity
\[
W(T_nx,y)=W(x,nT_{1/n}y),
\tag{WR7.3}
\]
and the degree relation \(W(T_nx,T_ny)=nW(x,y)\). The scalar \(n\) is present. On a full actual block \(\mathcal Q_\rho\), of multiplicity \(m_\rho\), the operators are
\[
T_n|_{\mathcal Q_\rho}
=n^\rho\sum_{j=0}^{m_\rho-1}
\frac{(\log n)^j}{j!}N_\rho^j,
\tag{WR7.4}
\]
\[
nT_{1/n}|_{\mathcal Q_\rho}
=n^{1-\rho}\sum_{j=0}^{m_\rho-1}
\frac{(-\log n)^j}{j!}N_\rho^j.
\tag{WR7.5}
\]
Here \(N_\rho^{m_\rho}=0\), with its original Jordan length. These are the full truncated exponential identities on the proved quotient, not only eigenvalue formulas.

The conjugate-linear reflection \(F^\#(s)=\overline{F(1-\overline s)}\) maps the \(\rho\)-block to the \(\rho^\#\)-block and changes the sign of the nilpotent coordinate. On the specified RZ jet classes the precise assertion is
\[
[E_{\rho,j}]^\#=(-1)^j[E_{\rho^\#,j}],\qquad
(N_\rho x)^\#=-N_{\rho^\#}x^\#.
\tag{WR7.6}
\]
These are identities in the quotient \(\mathcal Q\). The sign follows directly from \((s-\rho)^\#=-(s-\rho^\#)\), together with the reflected zero-isolation property of the specified classes. Thus reversal changes character and jet data in a specified way while preserving the supporting role. No assumption that those data must all be fixed has been made.

## WR8. The precise result for the proposed contradiction

Reversing a nonzero winding does create the opposite handedness in the sense of (WR3.1). It does not assign that handedness to the supporting point: the exact equivariant map (WR4.2) forgets it, and the attempted descent is contradicted by (WR4.4). The generic support's absence of an exchanged point-label and the stalk's possession of exchanged data are therefore compatible features of the actual source construction.

An actual off-critical zero, if present, would give degree-weighted character data exchanged by (WR6.2), with the full multiplicity action (WR7.4)–(WR7.5). It would not produce an exchanged label on \(\eta\) unless an additional map descending that label to the support had been constructed. WR4 proves that the direct forgetful projection cannot provide such a descent. This establishes the precise extent of this proposed support-based contradiction; it does not exclude a different arithmetic obstruction involving the retained fiber and its pairing.

The resulting positive mathematical connection is the exact diagram of operations already proved: source signed reversal on \(G\), its exchange on winding orientation, its invariant winding parity, the equivariant map to the parityless support, and the signed degree-weighted character comparison (WR6.3)–(WR6.6). The relevant purity equation has not been discarded; it is identified exactly as the character fixed-locus equation while the support remains fixed throughout.

## WR9. All translated reversal returns and their exact square

There is also a complete return-map calculation within the retained stalk data. Regard the set \(G\) as a left \(G\)-torsor: \(a\) acts on \(h\) by \(ah\), freely and transitively. This is the set of choices of a stalk datum, not a coordinate system on \(\eta\). A reversal-compatible map of this torsor means a map \(R:G\to G\) satisfying
\[
 R(ah)=\alpha(a)R(h)\qquad(a,h\in G).
\tag{WR9.1}
\]
Every such map is uniquely of the form
\[
 R_g(h)=g\alpha(h),\qquad g=R(1)\in G.
\tag{WR9.2}
\]
Indeed set \(h=1\) in WR9.1 and use the commutativity of \(G\). Conversely substitution proves WR9.1 for each displayed \(R_g\). Each is bijective, with the explicit inverse
\[
 R_g^{-1}(h)=\alpha(g)^{-1}\alpha(h).
\tag{WR9.3}
\]
Thus every member of this entire family is invertible; this is not deduced from a picture of a loop. These maps are semilinear torsor maps, not asserted to be group homomorphisms or sheaf-algebra automorphisms.

For \(g=T^mJ^k\), applying the return twice gives exactly
\[
 R_g^2(h)=g\alpha(g)h=\epsilon^m h.
\tag{WR9.4}
\]
Since \(\epsilon\ne1\) in the retained \(C_4\) subgroup, this is the identity precisely when \(m\) is even. For odd \(m\), the square is the nontrivial central translation by \(\epsilon\), while the fourth power is the identity. The signed square therefore detects winding parity without destroying invertibility, and without changing the underlying supporting point.

Every map \(h\mapsto ah\) is a change of the chosen element of the same torsor. Conjugating the return by this map gives
\[
 L_aR_gL_a^{-1}(h)
   =a g\alpha(a)^{-1}\alpha(h)
   =R_{\,gD(a)^{-1}}(h),
\qquad D(a)=\alpha(a)a^{-1}.
\tag{WR9.5}
\]
The set of such changes is all equivariant torsor bijections: a bijection commuting with the left \(G\)-action is determined by its value at \(1\), and because \(G\) is abelian has this displayed translation form. Thus WR9.5 describes the full equivalence relation, not only some allowed changes.

For the returns whose square is the identity, the parameter \(g\) lies in \(\ker N=\langle T^2,J\rangle\). Modulo the changes in WR9.5, WR2.8 computes precisely two classes, represented by
\[
 R_1(h)=\alpha(h),\qquad R_J(h)=J\alpha(h).
\tag{WR9.6}
\]
They are distinct because \(J\notin\operatorname{im}D=\langle T^2,\epsilon\rangle\). Both square to the identity since \(J\alpha(J)=1\). For returns whose square is translation by \(\epsilon\), the parameters instead form \(T\ker N\), and there are again precisely two classes, represented by
\[
 R_T(h)=T\alpha(h),\qquad R_{TJ}(h)=TJ\alpha(h).
\tag{WR9.7}
\]
Both square to \(\epsilon h\), and their equivalence classes are distinct by the same quotient calculation. This retains all four possibilities of the signed return calculation.

Their fixed decorations can be computed too. The equation \(R_g(h)=h\) is equivalent to \(g=D(h)^{-1}\). It has a solution exactly when \(g\in\operatorname{im}D\), and then its solution set is a coset of \(\ker D=\{1,\epsilon\}\), containing exactly two elements. In particular
\[
 \operatorname{Fix}(R_1)=\{1,\epsilon\},\qquad
 \operatorname{Fix}(R_J)=\operatorname{Fix}(R_T)
        =\operatorname{Fix}(R_{TJ})=\varnothing.
\tag{WR9.8}
\]
Thus the second involutive return has only exchanged decorations even though its square is the identity; the two order-four returns have no fixed decoration either. These are exact calculations in the retained fiber.

Projection of every one of these returns through \(\{\eta\}\times G\to\{\eta\}\) is still the identity on the support. Consequently a detectable change in the return, even one that changes its square, is explicitly compatible with the same parityless supporting point. This classifies the translated reversals on the actual stalk torsor. It does not assume that the programme's arithmetic cohomological return is one chosen representative, nor identify these torsor maps with a previously unspecified topological fundamental group.
