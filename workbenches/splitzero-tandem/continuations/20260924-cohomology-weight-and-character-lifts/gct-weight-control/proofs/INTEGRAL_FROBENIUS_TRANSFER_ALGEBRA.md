# The integral algebra of degree maps and transfers

24 September 2026. Proof labels FT1–FT10. This calculation repairs the scalar denominators identified in IC8 by retaining integral transfers instead of requiring every unweighted inverse to be an integral generator. All algebra acts on the specified coefficient and receiving spaces. There is no addition, metric, coordinate or vector assigned to \(\tau\langle Z_1;\mathrm{no}\ Z_2\rangle\).

The letters \(F_n,V_n\) below name algebra elements. Their geometric receivers are proved explicitly; the letter \(F\) by itself does not assert that an operator is a finite-field Frobenius. The final comparison retains the full original-zeta quotient and each zero multiplicity. No RH or zero-location assertion is inserted.

## Source calculations used

- `INTEGRAL_COUNTING_AND_WEIGHT_COMPARISON.md`, IC1–IC9, including the revised IC8.4a–IC8.6: the canonical counting ring, rational group-algebra action and minimal weighted-adjoint closure when every bare inverse is required.
- `TATE_H1_DERIVATION.md`, T5–T6, read in full, and T7–T8 portions giving the periods, maps, polarizations and origin-independence: the original maps \(U_n:E_{p^n}\to E_p\) and \(V_n:E_p\to E_{p^n}\), both degree \(n\), with full periods \(\log p\) and \(2\pi i\). The transfer below is derived rather than identified with a pullback in every degree.
- `ORIGINAL_ZETA_RESOLVENT_AND_PROJECTORS.md`, RZ1, RZ8 and RZ10–RZ11: the entire quotient, actual multiplier \(a^s\), all logarithmic jet coefficients and the exact Weil adjoint identity. Its global synthesis proof remains the source of the equality between the closed arithmetic source image and the complete zero-jet ideal.

## FT1. The integral subring and its exact additive basis

In the rational group algebra
\[
\Lambda_{\mathbb Q}=\mathbb Q[\mathbb Q_{>0}^{\times}],\qquad
b_rb_s=b_{rs},\qquad b_1=1,
\tag{FT1.1}
\]
define, for every positive integer \(n\),
\[
F_n=b_n,\qquad V_n=n b_{1/n}.
\tag{FT1.2}
\]
Let \(\mathcal C\) be the unital subring generated over \(\mathbb Z\) by all these elements. Sums and products are finite.

Write each positive rational \(r\) in its unique reduced form \(r=a/b\), where \(a,b\ge1\) and \(\gcd(a,b)=1\). Put
\[
\operatorname{den}(r)=b,\qquad c_r=b b_r.
\tag{FT1.3}
\]
Then the exact additive group is
\[
\boxed{\mathcal C=\bigoplus_{r\in\mathbb Q_{>0}}\mathbb Z c_r.}
\tag{FT1.4}
\]
Here is a proof including multiplication. For reduced fractions \(r=a/b\), \(s=c/d\), put \(h=\gcd(ac,bd)\). The reduced denominator of \(rs\) is \(bd/h\). Consequently
\[
c_rc_s=bd\,b_{rs}
=h\,c_{rs},\qquad
h=\frac{\operatorname{den}(r)\operatorname{den}(s)}
{\operatorname{den}(rs)}=\gcd(ac,bd)\in\mathbb Z_{>0}.
\tag{FT1.5}
\]
Thus the right side of (FT1.4) is a subring. It contains \(1=c_1\), \(F_n=c_n\) and \(V_n=c_{1/n}\), so it contains \(\mathcal C\). Conversely, for every reduced \(a/b\),
\[
c_{a/b}=F_aV_b,
\tag{FT1.6}
\]
so all its basis elements belong to \(\mathcal C\). Finally, distinct \(b_r\) are a free rational basis of the ambient group algebra and all denominators in (FT1.3) are nonzero. Therefore the \(c_r\) are independent over \(\mathbb Z\), proving the asserted direct sum and not merely a spanning statement.

Equivalently, an ambient finite sum \(\sum_r u_rb_r\) belongs to \(\mathcal C\) exactly when every \(u_r\) is an integer divisible by \(\operatorname{den}(r)\). This is an effective membership criterion with its original rational labels retained.

## FT2. Presentation by prime generators, with all commutations

There is an injective presentation
\[
\boxed{\mathcal C\cong
\mathbb Z[X_p,Y_p:p\text{ prime}]/(X_pY_p-p:p\text{ prime}),}
\qquad X_p\longmapsto F_p,\quad Y_p\longmapsto V_p.
\tag{FT2.1}
\]
The polynomial algebra is commutative. Explicitly, all its commutation relations, including those used in the proof, are
\[
X_pX_q=X_qX_p,\qquad
Y_pY_q=Y_qY_p,\qquad
X_pY_q=Y_qX_p\qquad(p,q\text{ prime}),
\tag{FT2.2}
\]
and the degree relations are
\[
X_pY_p=Y_pX_p=p\,1.
\tag{FT2.3}
\]
Scalar integers commute with every generator.

To prove that no further relation is missing, start with any monomial involving finitely many primes. For each prime replace every matched pair \(X_pY_p\) by the scalar \(p\), until at most one of \(X_p,Y_p\) remains. This expresses every polynomial as an integer linear combination of the monomials
\[
m_e=\prod_{e_p>0}X_p^{e_p}\prod_{e_p<0}Y_p^{-e_p},
\qquad e_p\in\mathbb Z,
\quad e_p=0\text{ for all but finitely many }p.
\tag{FT2.4}
\]
Their images are exactly
\[
\left(\prod_{e_p<0}p^{-e_p}\right)
b_{\prod_p p^{e_p}}
=c_{\prod_p p^{e_p}}.
\tag{FT2.5}
\]
Unique prime factorization makes the rational label unique, and FT1 proves independence of these images. Hence a linear combination of the normal monomials has zero image only when each coefficient vanishes. The induced map is injective. It is surjective because
\[
F_n=\prod_pF_p^{v_p(n)},\qquad
V_n=\prod_pV_p^{v_p(n)}
\tag{FT2.6}
\]
for every \(n\ge1\). This proves the full presentation, including prime two.

## FT3. The weighted involution is integral on this ring

Retain the exact weighted involution on the rational group algebra:
\[
b_r^\star=r b_{1/r},\qquad q^\star=q\quad(q\in\mathbb Q).
\tag{FT3.1}
\]
For reduced \(r=a/b\),
\[
c_r^\star=b\left(\frac ab b_{b/a}\right)
=a b_{b/a}=c_{1/r}.
\tag{FT3.2}
\]
Thus \(\mathcal C\) is preserved by \(\star\), integrally and exactly. It exchanges the generators:
\[
F_n^\star=V_n,\qquad V_n^\star=F_n.
\tag{FT3.3}
\]
Its square is the identity. It respects multiplication because the ambient assignment does, and (FT3.2) shows explicitly how the additive basis is permuted. The full generator relations are
\[
F_1=V_1=1,\quad F_mF_n=F_{mn},\quad V_mV_n=V_{mn},
\quad F_mV_n=V_nF_m,
\tag{FT3.4}
\]
\[
F_nV_n=V_nF_n=n\,1.
\tag{FT3.5}
\]
For \(d=\gcd(m,n)\), there is the precise cancellation formula
\[
\boxed{F_mV_n=d F_{m/d}V_{n/d}.}
\tag{FT3.6}
\]
Indeed the left side is \(n b_{m/n}\), and the right side is
\(d(n/d)b_{(m/d)/(n/d)}=n b_{m/n}\). The scalar \(d\) is retained; dropping it would destroy both the embedding and the transfer degree.

## FT4. Comparison with the earlier denominator obstruction

Let \(\Lambda=\mathbb Z[\mathbb Q_{>0}^{\times}]\). Then
\[
\mathcal C\subset\Lambda\subset\Lambda_{\mathbb Q},\qquad
\mathcal C\otimes_{\mathbb Z}\mathbb Q=\Lambda_{\mathbb Q}.
\tag{FT4.1}
\]
The inclusions follow from the coefficient description in FT1. Tensoring with \(\mathbb Q\) supplies
\(b_r=c_r/\operatorname{den}(r)\), proving the last equality. However
\[
b_{1/p}\notin\mathcal C\quad(p\text{ prime}),
\qquad p b_{1/p}=V_p\in\mathcal C.
\tag{FT4.2}
\]
Membership would require its coefficient one to be divisible by \(p\), contrary to FT1. Thus this ring does not contain every bare inverse, which was an explicit premise of IC8's minimal rational-closure calculation. Both conclusions therefore hold: \(\Lambda\) forces rational coefficients when closed under the weighted involution, while \(\mathcal C\) already preserves that involution over \(\mathbb Z\).

Here an integral coefficient form means the explicitly proved free \(\mathbb Z\)-algebra structure. It is not a claim that \(F_n\) is integral over \(\mathbb Z\) in the sense of satisfying a monic polynomial. In fact, for \(n>1\), a polynomial relation in \(F_n=b_n\) would be a relation between the distinct ambient basis elements \(b_{n^j}\). Their independence forces every coefficient to vanish, so there is no nonzero such polynomial. In particular the coefficient construction alone supplies no finite-rank integral lattice for the actual \(p^\rho\) eigenvalues. The independent IAR0–IAR2 calculation in `../quantum_tau_programme_bridge_20260924/INTEGRAL_ADJOINT_RETURN_ALGEBRA.md` gives the same coefficient subring and additive basis from the same positive-generator input; its subsequent trace results are separate derivations.

More precisely, adjoining the bare inverses of all \(F_p\) to \(\mathcal C\) gives \(\Lambda\). The resulting ring contains \(b_p\) and \(b_{1/p}\), hence every rational monomial by unique factorization, and all its generators were already in \(\Lambda\). Taking weighted-involution closure at that stage gives \(\Lambda_{\mathbb Q}\), exactly as IC8 proves.

The additive defect of the first inclusion has the full description
\[
0\longrightarrow\mathcal C\longrightarrow\Lambda
\longrightarrow
\bigoplus_{r\in\mathbb Q_{>0}}
\mathbb Z/\operatorname{den}(r)\mathbb Z
\longrightarrow0.
\tag{FT4.3}
\]
The last map sends the coefficient of \(b_r\) to its residue modulo \(\operatorname{den}(r)\). Finite support makes the map well defined and onto; its kernel is FT1's membership condition. This is an exact sequence of additive groups. It is not a quotient-ring assertion, since \(\mathcal C\) is a unital subring rather than an ideal. Its torsion records these coefficient divisibilities and is not identified with the winding history or the finite \(C_4\) stalk subgroup.

## FT5. The receiving representation on the complete original-zeta quotient

Use the RZ spaces with their existing topology:
\[
\mathcal Q=\mathcal B/\mathcal I,\qquad
\mathcal I=\{F:F^{(j)}(\rho)=0\text{ for all actual }\rho,
\ 0\le j<m_\rho\},\qquad
T_r[F]=[r^sF(s)].
\tag{FT5.1}
\]
Here \(\mathcal B\) consists of the entire functions with every seminorm
\[
b_{A,M}(F)=\sup_{|\operatorname{Re}s|\le A}
(1+|\operatorname{Im}s|)^M|F(s)|<\infty.
\tag{FT5.2}
\]
The actual source comparison retains
\[
F_0(s)=\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2)\zeta(s),\qquad
\mathcal M^{-1}T_r\mathcal Mk(u)=r^{1/2}k(u/r).
\tag{FT5.3}
\]
All endpoints, exceptional trivial-zero values and multiplicity data are retained by the prior synthesis and RZ proofs; this note makes no replacement of the original \(\zeta\) by \(F_0\).

Restrict the explicitly constructed rational representation from IC8 to obtain
\[
\Psi:\mathcal C\longrightarrow\operatorname{End}_{\mathrm{cont}}(\mathcal Q),
\qquad
\Psi(F_n)=T_n,\qquad
\Psi(V_n)=nT_{1/n},\qquad
\Psi(c_{a/b})=bT_{a/b}.
\tag{FT5.4}
\]
It is a unital ring homomorphism because \(T_rT_s=T_{rs}\), with (FT1.5) preserving every scalar coefficient. Every image is continuous: for \(C=\sum_r k_rc_r\),
\[
b_{A,M}\left(\sum_r k_r\operatorname{den}(r)r^sF(s)\right)
\le\left(\sum_r|k_r|\operatorname{den}(r)
\max(r^A,r^{-A})\right)b_{A,M}(F).
\tag{FT5.5}
\]
The sum is finite. The multipliers preserve all zero orders, so the same estimate descends by taking infima over source representatives. The entire domain and every multiplicity are unchanged.

On each actual block \(\mathcal Q_\rho\) of dimension \(m=m_\rho\), RZ gives \(L_\zeta=\rho I+N_\rho\), \(N_\rho^m=0\), with full Jordan length. Consequently
\[
\Psi(F_n)|_{\mathcal Q_\rho}
=n^\rho\sum_{j=0}^{m-1}\frac{(\log n)^j}{j!}N_\rho^j,
\tag{FT5.6}
\]
\[
\Psi(V_n)|_{\mathcal Q_\rho}
=n^{1-\rho}\sum_{j=0}^{m-1}\frac{(-\log n)^j}{j!}N_\rho^j,
\tag{FT5.7}
\]
\[
\Psi(c_{a/b})|_{\mathcal Q_\rho}
=b(a/b)^\rho\sum_{j=0}^{m-1}
\frac{(\log(a/b))^j}{j!}N_\rho^j.
\tag{FT5.8}
\]
Multiplying (FT5.6) and (FT5.7) gives exactly \(nI\): the finite truncated exponential products cancel every positive nilpotent degree, and the scalar factors multiply to \(n\). Alternatively this follows directly from \(T_nT_{1/n}=I\). Both verifications retain the full coefficients rather than projecting to zero values.

The source-derived Weil form obeys
\[
W(\Psi(C)x,y)=W(x,\Psi(C^\star)y),\qquad C\in\mathcal C.
\tag{FT5.9}
\]
For \(F_n\), this is the proved identity \(W(T_nx,y)=W(x,nT_{1/n}y)\). Integer linearity and multiplication prove it for the generated ring; equivalently IC8 proves it on the entire rational ambient algebra. No positivity of this particular form is inferred from its integral coefficient ring.

## FT6. Finite isogeny pullback and trace, with all degrees distinguished

Fix one recovered rational prime \(p\), and retain its original constants
\[
A=\log p>0,\qquad B=2\pi>0.
\tag{FT6.1}
\]
For every positive rational \(q\), construct the actual complex torus
\[
E_q=\mathbb C/(qA\mathbb Z+iB\mathbb Z),\qquad
w_q=x_q+i\theta_q,
\tag{FT6.2}
\]
with the displayed model origin \([0]\). At \(q=1\), this is the source curve \(\mathbb C^\times/p^{\mathbb Z}\); at \(q=n\), it is \(\mathbb C^\times/(p^n)^{\mathbb Z}\). The exponential map proves these identifications with both periods retained. The additional rational scales are explicitly constructed receivers, not new prime stalks.

For \(n\ge1\), the inclusion of lattices defines the degree-\(n\) covering
\[
u_{n,q}:E_{nq}\longrightarrow E_q,
\qquad[w]_{nq}\longmapsto[w]_q.
\tag{FT6.3}
\]
The kernel is \(\{[jqA]_{nq}:0\le j<n\}\). The corresponding dual degree-\(n\) isogeny is
\[
v_{n,q}:E_q\longrightarrow E_{nq},
\qquad[w]_q\longmapsto[nw]_{nq}.
\tag{FT6.4}
\]
Its kernel consists of the angular classes \([ikB/n]_q\), \(0\le k<n\). Both compositions are multiplication by \(n\), on their respective tori. For \(q=1\), these are precisely the maps called \(U_n,V_n\) in T5; the present lower-case notation distinguishes them from the algebra generators.

The integral cohomology groups and their explicit period comparisons are
\[
H^0(E_q;\mathbb Z)=\mathbb Z e_q,\quad
H^1(E_q;\mathbb Z)=\mathbb Z\alpha_q\oplus\mathbb Z\beta_q,
\quad H^2(E_q;\mathbb Z)=\mathbb Z h_q,
\tag{FT6.5}
\]
\[
e_q=1,\quad \alpha_q=\frac{dx_q}{qA},\quad
\beta_q=\frac{d\theta_q}{B},\quad
h_q=\frac{dx_q\wedge d\theta_q}{qAB}.
\tag{FT6.6}
\]
These fractions describe the integral classes inside the original differential-form spaces. The full forms \(dx_q,d\theta_q,dx_q\wedge d\theta_q\) and full area \(qAB\) are retained. To verify the cohomology, the torus cell decomposition has one vertex, two oriented edges and one face with attaching word their commutator. Its cellular differentials vanish, giving ranks \(1,2,1\) and no torsion. The displayed forms have periods one on the corresponding generating cycles and oriented face, proving the stated integral comparison.

Pullback \(P_{n,q}=u_{n,q}^*\) maps the cohomology of \(E_q\) to that of \(E_{nq}\). Its exact matrices in (FT6.5), ordered by degrees zero, one and two, are
\[
P_{n,q}:\qquad 1,\qquad
\begin{pmatrix}n&0\\0&1\end{pmatrix},\qquad n.
\tag{FT6.7}
\]
Indeed the original differential forms pull back without a scalar, while their target integral periods are \(nqA,B,nqAB\), respectively.

Let \(S_{n,q}=u_{n,q!}\) be the cohomological transfer, directed from \(E_{nq}\) to \(E_q\). It is integral: a singular simplex in the base has exactly \(n\) lifts under a covering, and the sum of its lifts is an integral chain; the boundary of that sum is the sum of the lifted boundaries. This chain map defines the cochain transfer. On differential forms the same map is the sum of the pullbacks by all local inverse branches, which commute with the exterior derivative and agree on overlapping charts. Each inverse branch is a translation in \(w\), so its derivative is the identity. Thus on original invariant forms the transfer multiplies the coefficient by \(n\). In the integral bases the exact matrices are
\[
S_{n,q}:\qquad n,\qquad
\begin{pmatrix}1&0\\0&n\end{pmatrix},\qquad1.
\tag{FT6.8}
\]
For example \(n\,dx_q/(nqA)=dx_q/(qA)\) explains its radial degree-one entry, and \(n\,dx_q\wedge d\theta_q/(nqAB)=h_q\) explains its top entry. It follows in every degree that
\[
S_{n,q}P_{n,q}=nI_{H^*(E_q)},\qquad
P_{n,q}S_{n,q}=nI_{H^*(E_{nq})}.
\tag{FT6.9}
\]

The dual-isogeny pullback \(v_{n,q}^*\) is instead
\[
v_{n,q}^*:\qquad1,\qquad
\begin{pmatrix}1&0\\0&n\end{pmatrix},\qquad n.
\tag{FT6.10}
\]
It equals the transfer \(S_{n,q}\) exactly in degree one. In degrees zero and two the displayed factors differ. Thus the earlier T6 degree-one adjoint equality is preserved, and is not improperly extended to all cohomological degrees.

## FT7. A typed integral representation over the full scale family

The preceding arrows connect different tori; they are not endomorphisms of one fixed fiber. Their precise common receiver is the direct sum
\[
\mathcal H_{\mathbb Z}
=\bigoplus_{q\in\mathbb Q_{>0}}H^*(E_q;\mathbb Z),
\tag{FT7.1}
\]
with finite support. Define endomorphisms on it by
\[
\mathfrak F_n|_{H^*(E_q)}=P_{n,q}:H^*(E_q)\to H^*(E_{nq}),
\tag{FT7.2}
\]
\[
\mathfrak V_n|_{H^*(E_q)}=S_{n,q/n}:H^*(E_q)\to H^*(E_{q/n}).
\tag{FT7.3}
\]
The rational index set ensures that both target scales exist. Every map is integral by FT6 and preserves finite support. The full matrices (FT6.7)–(FT6.8) show
\[
\mathfrak F_m\mathfrak F_n=\mathfrak F_{mn},\quad
\mathfrak V_m\mathfrak V_n=\mathfrak V_{mn},\quad
\mathfrak F_m\mathfrak V_n=\mathfrak V_n\mathfrak F_m,
\quad\mathfrak F_n\mathfrak V_n=nI.
\tag{FT7.4}
\]
For full verification of the mixed relation, both composites carry scale \(q\) to \(mq/n\); in degrees zero, one and two their matrices are respectively
\[
n,\qquad\begin{pmatrix}m&0\\0&n\end{pmatrix},\qquad m.
\tag{FT7.5}
\]
These also equal \(d\) times the matrices for \(\mathfrak F_{m/d}\mathfrak V_{n/d}\), where \(d=\gcd(m,n)\). Therefore FT2's presentation gives a unital integral representation
\[
\Psi_{\mathrm{geom}}:\mathcal C\longrightarrow
\operatorname{End}_{\mathbb Z}(\mathcal H_{\mathbb Z}),
\qquad F_n\mapsto\mathfrak F_n,\quad V_n\mapsto\mathfrak V_n.
\tag{FT7.6}
\]

This representation is faithful. For reduced \(r=a/b\), the action of \(c_r=F_aV_b\) on \(e_1\in H^0(E_1)\) is \(b e_r\). These images have distinct scale supports as \(r\) varies and nonzero integer coefficient \(b\). Thus an integer combination of the basis elements can act as zero only when every coefficient vanishes. This proves faithfulness without identifying distinct cohomology fibers or discarding their scale labels.

## FT8. The full positive adjoint comparison, retaining both periods

Use the flat complex metric \(dx_q^2+d\theta_q^2\) on each explicitly constructed torus; this is a metric on the torus and not on \(\tau\). Its area is \(qAB\). The invariant representatives of every cohomology class give positive Hermitian forms conjugate-linear in the first input. In the original invariant-form coefficients they are
\[
\begin{aligned}
h_q^0(a,c)&=qAB\,\overline a c,\\
h_q^1(a\,dx_q+b\,d\theta_q,c\,dx_q+d\,d\theta_q)
&=qAB(\overline a c+\overline b d),\\
h_q^2(a\,dx_q\wedge d\theta_q,c\,dx_q\wedge d\theta_q)
&=qAB\,\overline a c.
\end{aligned}
\tag{FT8.1}
\]
Invariant forms represent all cohomology classes by (FT6.5)–(FT6.6), and these formulas are positive definite on their respective finite-dimensional spaces. In the integral bases their full Gram matrices are
\[
qAB,\qquad
\begin{pmatrix}B/(qA)&0\\0&qA/B\end{pmatrix},\qquad
1/(qAB).
\tag{FT8.2}
\]
These factors are comparison coefficients, not altered periods.

Direct substitution of (FT6.7)–(FT6.8) into (FT8.2) proves, in every degree,
\[
h_{nq}(P_{n,q}x,y)=h_q(x,S_{n,q}y),\qquad
h_{nq}(P_{n,q}x,P_{n,q}x')=n h_q(x,x').
\tag{FT8.3}
\]
For example on the radial degree-one class the first identity has coefficient
\(n\,B/(nqA)=B/(qA)\); on the angular class it has coefficient \(nqA/B=n(qA/B)\). In top degree it has coefficient \(n/(nqAB)=1/(qAB)\), and in degree zero it has coefficient \(nqAB=n(qAB)\). Thus every original factor is accounted for.

Take the orthogonal sum of these forms on \(\mathcal H_{\mathbb Z}\otimes\mathbb C\). Then
\[
\mathfrak F_n^\dagger=\mathfrak V_n,\qquad
\mathfrak F_n^\dagger\mathfrak F_n
=\mathfrak F_n\mathfrak F_n^\dagger=nI,
\tag{FT8.4}
\]
first on finite-support vectors. The norm equality
\(\|\mathfrak F_nx\|^2=n\|x\|^2\) and the analogous equality for \(\mathfrak V_n\) extend both maps to bounded operators, of norm \(\sqrt n\), on the Hilbert completion of this specified direct sum. The adjoint relations persist by density. Integer linearity and multiplication now prove
\[
\Psi_{\mathrm{geom}}(C)^\dagger
=\Psi_{\mathrm{geom}}(C^\star),\qquad C\in\mathcal C.
\tag{FT8.5}
\]
Every finite algebra combination is bounded because it is a finite sum of finite products of the bounded generators. This establishes an actual positive integral correspondence representation. It does not transfer positivity to the different original-zeta receiver in FT5.

## FT9. Exact relation between the two receivers

The same proved integral algebra now has two specified actions:
\[
\begin{array}{ccc}
&\mathcal C&\\
\Psi_{\mathrm{geom}}\swarrow&&\searrow\Psi\\
\operatorname{End}(\mathcal H_{\mathbb Z})&&
\operatorname{End}_{\mathrm{cont}}(\mathcal Q).
\end{array}
\tag{FT9.1}
\]
On the first side the transfer is an actual integral covering trace and is the adjoint for the positive forms (FT8.1). On the second side it is the actual original-zeta operator \(nT_{1/n}\), satisfying the proved adjoint identity for the source-derived Weil form, with full zero jets (FT5.6)–(FT5.8). This does not assert uniqueness of an adjoint for a possibly degenerate form. Both sides satisfy the same complete algebra relations and the same degree factor \(n\).

This diagram specifies two representations of the same algebra; it does not assert an intertwiner identifying their state spaces, nor that the two forms have the same sign. The geometric scale family and its positive form have been constructed and proved here. The original-zeta receiver remains the existing quotient of its full arithmetic source. The result is an integral, involution-preserving repair of the exact coefficient obstruction, together with these fully typed receiving maps. It establishes neither a restriction on the real parts of zeta zeros nor an impossibility of obtaining such a restriction by a further mathematical comparison.

The subsequent complete calculation `GEOMETRIC_SCALE_TO_ORIGINAL_ZETA_INTERTWINERS.md` constructs actual algebraic receiving maps between their specified degree-zero and original-zeta spaces, and calculates their topology. Its separate proof extends this diagram; no equality of the two pairings is asserted here.

## FT10. Exact geometric spectrum, with the original degree and periods

Keep the degree-zero sector of FT7–FT8, and write its Hilbert completion as
\[
 H^0_{\mathrm{geom}}=
 \left\{\sum_{q\in\mathbb Q_{>0}}a_q e_q:
           AB\sum_q q|a_q|^2<\infty\right\},
 \qquad \|a\|^2=AB\sum_q q|a_q|^2,
\tag{FT10.1}
\]
where \(A=\log p\), \(B=2\pi\) are the retained periods of FT6. For every integer degree \(n\geq2\), its original operator and transfer act by
\[
 \mathfrak F_n e_q=e_{nq},\qquad
 \mathfrak V_n e_q=n e_{q/n}.
\tag{FT10.2}
\]
The same formulas and the displayed weighted sum prove
\[
 \|\mathfrak F_n\|=\sqrt n,\qquad
 \mathfrak F_n^{-1}=\mathfrak V_n/n,\qquad
 \|\mathfrak F_n^{-1}\|=1/\sqrt n.
\tag{FT10.3}
\]
The scalar division is on this complex Hilbert space; the integral transfer in FT1 remains \(V_n\), not the bare inverse. No operator or period is rescaled in what follows.

The spectrum and point spectrum on this particular receiver are exactly
\[
 \boxed{\operatorname{Spec}(\mathfrak F_n|_{H^0_{\mathrm{geom}}})
       =\{\lambda\in\mathbb C:|\lambda|=\sqrt n\},
 \qquad \operatorname{Spec}_{\mathrm{point}}
       (\mathfrak F_n|_{H^0_{\mathrm{geom}}})=\varnothing.}
\tag{FT10.4}
\]
Here is the full proof. If \(|\lambda|>\sqrt n\), the series
\[
 (\lambda I-\mathfrak F_n)^{-1}
    =\sum_{k=0}^{\infty}\lambda^{-k-1}\mathfrak F_n^k
\tag{FT10.5}
\]
converges in operator norm by FT10.3's geometric ratio \(\sqrt n/|\lambda|<1\). Multiplication of its partial sums by \(\lambda I-\mathfrak F_n\) leaves a remainder of norm tending to zero, proving it is the inverse on both sides. Its norm is at most \(1/(|\lambda|-\sqrt n)\). If \(|\lambda|<\sqrt n\), the analogous exact inverse is
\[
 (\lambda I-\mathfrak F_n)^{-1}
    =-\sum_{k=0}^{\infty}\lambda^k\mathfrak F_n^{-k-1},
\tag{FT10.6}
\]
with geometric ratio \(|\lambda|/\sqrt n<1\) and norm at most \(1/(\sqrt n-|\lambda|)\). The formula includes \(\lambda=0\). Thus no point off the displayed circle is in the spectrum.

For \(|\lambda|=\sqrt n\) and \(N\geq0\), the exact finite vector
\[
 z_N=\sum_{k=-N}^N\lambda^{-k}e_{n^k}
\tag{FT10.7}
\]
has squared norm
\[
 \|z_N\|^2
   =AB\sum_{k=-N}^N n^k|\lambda|^{-2k}
   =(2N+1)AB.
\tag{FT10.8}
\]
Subtracting the two finite sums for \(\mathfrak F_n z_N\) and \(\lambda z_N\) cancels each interior coefficient and leaves both endpoint terms:
\[
 (\mathfrak F_n-\lambda I)z_N
     =\lambda^{-N}e_{n^{N+1}}-\lambda^{N+1}e_{n^{-N}}.
\tag{FT10.9}
\]
Their supports are distinct, so the full weighted norm is
\[
 \|(\mathfrak F_n-\lambda I)z_N\|^2
   =AB\left(n^{N+1}|\lambda|^{-2N}
            +n^{-N}|\lambda|^{2N+2}\right)
   =2nAB.
\tag{FT10.10}
\]
A bounded inverse of \(\mathfrak F_n-\lambda I\) would bound the ratio
\(\|z_N\|/\|(\mathfrak F_n-\lambda I)z_N\|
 =\sqrt{(2N+1)/(2n)}\), contrary to its divergence. This proves that every point on the circle lies in the spectrum, retaining the vectors, both endpoint terms and both periods.

Finally suppose \(a=\sum a_qe_q\) is an eigenvector with eigenvalue \(\lambda\). Invertibility excludes \(\lambda=0\). Comparing the coefficient at \(nq\) gives \(a_{nq}=\lambda^{-1}a_q\), and therefore
\[
 a_{n^kq}=\lambda^{-k}a_q\qquad(k\in\mathbb Z).
\tag{FT10.11}
\]
If some \(a_q\ne0\), the contribution of this orbit to the squared norm is
\[
 AB\,q|a_q|^2\sum_{k\in\mathbb Z}
                  \left(n/|\lambda|^2\right)^k.
\tag{FT10.12}
\]
For every positive ratio this bilateral series diverges: a ratio greater than one diverges as \(k\to+\infty\), one less than one as \(k\to-\infty\), and one gives infinitely many equal positive terms. Thus all coefficients vanish, proving the empty point spectrum.

This is a complete spectral calculation for the newly constructed geometric Hilbert receiver. Its circle is obtained from the actual integral covering adjoints and their degree factor. It does not put the original-zeta eigenvectors into this Hilbert space, and it does not replace the original-zeta spectrum. The distinction is calculated by the explicit receiving maps in the accompanying intertwiner proof.
