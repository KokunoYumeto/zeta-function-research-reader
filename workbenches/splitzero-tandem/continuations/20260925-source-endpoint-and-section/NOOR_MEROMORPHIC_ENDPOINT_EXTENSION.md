# The retained endpoint extension and the full cover action

25 September 2026. Complete derivation NPE0–NPE10. Pending independent review.

## NPE0. Construction stage and the choice under examination

The supporting datum remains \(\tau\langle Z_1;\mathrm{no}\ Z_2\rangle\). Every coefficient operation in this proof follows the complete-history arithmetic reconstruction. No addition, coordinate, parity, numerical value or metric is assigned to that supporting datum. The analytic endpoint \(s=0\) below is an endpoint of the original coefficient variable; it is not an identification of that endpoint with \(\tau\). The two branch counters remain separate.

The foundation audit asks whether the entire-source requirement omits the pole already present in the exact Noor correction. We construct a larger meromorphic source with its original entire source as a specified subspace, prove both maps, and retain its residue. We do not replace the original source or declare its extension class zero.

Use the complete original Fréchet space
\[
\mathcal B=\{F\in\mathcal O(\mathbb C):q_{A,N}(F)<\infty\text{ for all }A>0,N\ge0\},\qquad
q_{A,N}(F)=\sup_{|\Re s|\le A}(1+|\Im s|)^N|F(s)|.
\tag{NPE0.1}
\]
Its closed ideal \(I\) consists of the full vanishing jets at the actual nontrivial zeros of original \(\zeta\), through order \(m_\rho-1\); \(Q=\mathcal B/I\). Retain the original multiplier and exceptional values:
\[
F_0(s)=\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2)\zeta(s),\qquad
F_0(0)=F_0(1)=\frac18,\qquad F_0(-1)=F_0(2)=\frac\pi{24},
\]
\[
F_0(-2j)=\frac{j(2j+1)(-1)^j\pi^j}{2j!}\zeta'(-2j)\quad(j\ge1).
\tag{NPE0.2}
\]
Thus the entire multiplier keeps its exact comparison with original zeta, including its pole and trivial zeros. No completed function replaces zeta. The original arithmetic remains
\[
\zeta(s)=1+\sum_{n\ge2}n^{-s}=\prod_p(1-p^{-s})^{-1},\qquad
-\frac{\zeta'(s)}{\zeta(s)}=\sum_p\sum_{k\ge1}(\log p)p^{-ks}\quad(\Re s>1).
\tag{NPE0.3}
\]
The entire source and its full ideal are those already proved in GSP1 and NHJ0. No location of an actual nontrivial zero is assumed.

## NPE1. The actual meromorphic source and its residue

Fix \(t>0\), put \(g_t(s)=e^{ts^2}\), and retain the full meromorphic correction
\[
h_t(s)=\frac{8g_t(s)F_0(s)}s
=\frac{8e^{ts^2}}s\left(\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2)\zeta(s)\right).
\tag{NPE1.1}
\]
It has exactly one pole, simple at zero, of residue \(1\). Indeed \(g_t(0)=1\) and \(8F_0(0)=1\); the remaining numerator is entire. At every actual nontrivial zero it vanishes to the same full order as \(F_0\), since that zero is not zero and the other factors are nonzero there.

Define the space of actual meromorphic functions
\[
E=\mathcal B+\mathbb C h_t,
\qquad (F,c)\longmapsto F+ch_t,
\tag{NPE1.2}
\]
with the product topology transported from \(\mathcal B\oplus\mathbb C\). The expression is unique: taking residues recovers \(c\), then subtraction recovers \(F\). It is therefore a complete Hausdorff locally convex space. Its continuous residue map gives a strict exact sequence
\[
0\longrightarrow\mathcal B\longrightarrow E
\xrightarrow{\operatorname{res}_0}\mathbb C\longrightarrow0.
\tag{NPE1.3}
\]
Here exactness follows from the unique expression and openness from the product projection. The section \(c\mapsto ch_t\) is continuous as a vector-space section; equivariance is a separate calculation below.

The space and topology do not depend on \(t>0\). For \(u,t>0\),
\[
h_u-h_t=8F_0(s)\frac{e^{us^2}-e^{ts^2}}s\in I\subset\mathcal B.
\tag{NPE1.4}
\]
The quotient is entire because its numerator vanishes to order at least two at zero. On each vertical strip both Gaussians decrease faster than every vertical power; outside a fixed disk division by \(s\) preserves that bound, and inside the disk the removable function is bounded. Multiplication by \(F_0\), itself in \(\mathcal B\), preserves every required bound. The full zero jets are retained by the explicit \(F_0\) factor. The coordinate change is \((F,c)\mapsto(F+c(h_t-h_u),c)\), continuous with its displayed continuous inverse. This proves equality of the actual spaces and equivalence of their specified topologies without discarding the difference.

## NPE2. Exact cover action and cocycle

For every recovered integer \(n\ge1\), the original coefficient action is
\[
(U_nF)(s)=n^{1-s}F(s),\qquad U_mU_n=U_{mn}.
\tag{NPE2.1}
\]
It and its inverse preserve \(\mathcal B\) continuously, since their absolute values are bounded on each fixed strip. On the actual pole,
\[
U_nh_t=nh_t-\delta_{n,t},\qquad
\delta_{n,t}(s)=8g_t(s)F_0(s)\frac{n-n^{1-s}}s\in I.
\tag{NPE2.2}
\]
The quotient is entire with value \(n\log n\) at zero; its strip growth is bounded away from a disk and controlled inside by removable division. These facts prove membership in \(\mathcal B\), and the full \(F_0\) factor proves membership in \(I\). The exact endpoint value is
\[
\delta_{n,t}(0)=n\log n.
\tag{NPE2.3}
\]
Thus \(U_n\) extends continuously to \(E\). Relative to (NPE1.2) its matrix and residue action are
\[
U_n^E(F,c)=(U_nF-c\delta_{n,t},nc),\qquad
\operatorname{res}_0(U_n^Ef)=n\operatorname{res}_0(f).
\tag{NPE2.4}
\]
The residue line consequently carries the character \(\chi(n)=n\), derived from multiplication of the Laurent expansion. This is an arithmetic coefficient character, not an assigned geometric weight of \(\tau\).

The discrepancies obey the complete cocycle identity
\[
\delta_{mn,t}=m\delta_{n,t}+U_n\delta_{m,t}
=n\delta_{m,t}+U_m\delta_{n,t}.
\tag{NPE2.5}
\]
For example the first right side is \(m(nh_t-U_nh_t)+U_n(mh_t-U_mh_t)=mnh_t-U_{mn}h_t\). This proves the action identity in the product coordinates and keeps its sign.

## NPE3. The extension is nonsplit equivariantly; its full-ideal pushout splits

For every recovered \(n>1\), no linear section of the residue in (NPE1.3) intertwines \(U_n^E\) and multiplication by \(n\). A section would send \(1\) to \(h_t+F\), with \(F\in\mathcal B\), and equivariance would require
\[
(U_n-n)F=\delta_{n,t}.
\tag{NPE3.1}
\]
The left side has value zero at zero because \(U_nF(0)=nF(0)\). The right side has nonzero value \(n\log n\) by (NPE2.3). This contradiction proves the claim even without continuity of the proposed section. It does not contradict the nonequivariant vector-space splitting.

The original ideal is closed in \(E\), is invariant, and is contained in its entire subspace. Its actual quotient therefore has the explicit topological isomorphism
\[
E/I\longrightarrow Q\oplus\mathbb C_\chi,
\qquad [F+ch_t]\longmapsto([F],c).
\tag{NPE3.2}
\]
Well-definedness, injectivity and surjectivity follow from the unique residue; openness follows from the product quotient \(\mathcal B\oplus\mathbb C\to Q\oplus\mathbb C\). Formula (NPE2.2) shows that this isomorphism intertwines the diagonal action \(([F],c)\mapsto([U_nF],nc)\). Its section is independent of \(t\) because (NPE1.4) lies in \(I\).

This is precisely the pushout of (NPE1.3) along the original quotient \(q:\mathcal B\to Q\). Its universal property can be checked directly: a continuous map from \(E\) agreeing on \(\mathcal B\) with a map through \(q\) annihilates \(I\), and so factors uniquely through \(E/I\) with its quotient topology. Hence the extension class becomes zero under this particular pushout while its full representative in \(I\) remains recorded. This is not a vanishing statement about the distinct original geometric lifting class.

The equivariant residue section in (NPE3.2) is unique, already for each recovered n>1. The difference of two sections would be a class \([F]\in Q\) with \((U_n-n)[F]=0\). At every actual nontrivial zero \(\rho\), the multiplier \(n^{1-s}-n\) is nonzero because \(|n^{1-\rho}|=n^{1-\Re\rho}<n\). Thus it is a holomorphic unit in a neighborhood of that zero. Multiplying a germ by such a unit preserves its full vanishing order: its reciprocal has a convergent Taylor series and recovers every derivative through order \(m_\rho-1\). The condition \((n^{1-s}-n)F\in I\) therefore gives \(F\in I\). This proves uniqueness while retaining every multiplicity. It is an exact separation of the residue character from the original full-jet coefficient characters, after the complete arithmetic is available; it is not an initialization of the arithmetic from one chosen degree or a purity theorem for its interior zeros.

## NPE4. The endpoint gives an exact two-dimensional infinitesimal representation

For \(f\in E\), write its Laurent expansion as
\[
f(s)=\frac c s+a_0+a_1s+\cdots.
\]
Both \(c\) and \(a_0\) are continuous on \(E\): in product coordinates,
\(c=\operatorname{res}_0f\) and \(a_0=F(0)+8cF_0'(0)\), retaining the full derivative of (NPE0.2). The map
\[
j:E\longrightarrow\mathbb C^2,\qquad j(f)=(a_0,c)
\tag{NPE4.1}
\]
is onto. The residue is realized by \(h_t\); an entire element with any specified value at zero is a scalar multiple of \(e^{s^2}\in\mathcal B\). Its kernel is the original entire subspace \(\{F\in\mathcal B:F(0)=0\}\).

Multiplying the complete Laurent expansion by
\(n^{1-s}=n\sum_{k\ge0}(-\log n)^ks^k/k!\) gives
\[
j(U_n^Ef)=
\begin{pmatrix}n&-n\log n\\0&n\end{pmatrix}j(f)
=n\bigl(I-(\log n)N\bigr)j(f),\qquad
N=\begin{pmatrix}0&1\\0&0\end{pmatrix},\quad N^2=0.
\tag{NPE4.2}
\]
The matrix product for \(m,n\) is exactly the matrix for \(mn\) because \(\log(mn)=\log m+\log n\) and \(N^2=0\). Its trace is \(2n\), determinant \(n^2\), and its off-diagonal entry is nonzero for \(n>1\). Thus those two scalar invariants do not erase or detect the surviving nilpotent action. The map \(a+b\epsilon\mapsto aI+bN\) from \(\mathbb C[\epsilon]/(\epsilon^2)\) to \(\operatorname{End}(\mathbb C^2)\) is an injective algebra homomorphism: multiplication is the displayed rule using \(N^2=0\), and the two matrices \(I,N\) are linearly independent. This is an explicitly derived coefficient realization of dual-number arithmetic, with no operation assigned to \(\tau\) and no novelty claim for the matrix algebra itself.

## NPE5. The exact dual extension and the Hardy-boundary term

Every continuous complex-linear functional on \(E\) is uniquely a pair
\[
\widetilde\Lambda(F+ch_t)=\Lambda(F)+c\alpha,
\qquad (\Lambda,\alpha)\in\mathcal B'\oplus\mathbb C.
\tag{NPE5.1}
\]
This identification is also a strong-dual topological isomorphism: product-bounded source sets project to bounded sets in each factor, and each factor's bounded sets embeds in the product. Transposing (NPE2.4) gives
\[
(U_n^E)'(\Lambda,\alpha)=(U_n'\Lambda,n\alpha-\Lambda(\delta_{n,t})).
\tag{NPE5.2}
\]
The zero-residue-coordinate lift \(\sigma_t\Lambda=(\Lambda,0)\) therefore has the exact equivariance discrepancy \((0,-\Lambda(\delta_{n,t}))\). On \(I^\perp\) this discrepancy is zero, in agreement with the split quotient (NPE3.2). In the full dual it must be retained.

Keep the original Noor coefficients
\[
\phi_0(s)=-1/s,\qquad \phi_m(s)=\frac{m^{1-s}-(m+1)^{1-s}}s\quad(m\ge1).
\]
The corrected entire tests and uncorrected meromorphic tests are, respectively,
\[
F_{t,m}=g_t\phi_m+h_t\in\mathcal B,
\qquad G_{t,m}=g_t\phi_m=F_{t,m}-h_t\in E.
\tag{NPE5.3}
\]
Each \(G_{t,m}\) has residue \(-1\), including \(m=0\). In product coordinates its entire part is \(F_{t,m}\); NHJ1's polynomial-in-m seminorm bound proves convergence on the disk of
\[
\mathcal M_t(\Lambda,\alpha)(z)
=\sum_{m\ge0}\overline{\widetilde\Lambda(G_{t,m})}z^m
=\mathcal H_t\Lambda(z)-\frac{\overline\alpha}{1-z}.
\tag{NPE5.4}
\]
This is continuous from the full strong dual into the compact-open holomorphic topology. Indeed the series of tests over each compact subdisk is bounded in \(E\), by that polynomial bound and the geometric sum of residue coordinates.

The meromorphic tests obey the exact identity before any quotient:
\[
\sum_{a=0}^{n-1}G_{t,nm+a}=U_n^E G_{t,m}.
\tag{NPE5.5}
\]
Telescoping the powers proves it for \(m\ge1\); for \(m=0\), both sums include \(\phi_0=-1/s\) and equal \(-g_t n^{1-s}/s\). Hence
\[
\boxed{\mathscr W_n^*\mathcal M_t=\mathcal M_t(U_n^E)'},
\tag{NPE5.6}
\]
where \(\mathscr W_n^*\) is the original coefficient-block sum on disk-holomorphic functions. Its continuity is proved by NHJ7's Cauchy estimate. Substituting (NPE5.2) into (NPE5.4) recovers exactly NHJ7.3, with the positive discrepancy \(\overline{\Lambda(\delta_{n,t})}/(1-z)\). Thus the entire-source formula and the meromorphic-source formula are connected by explicit maps, including the full pole term.

## NPE6. The larger analytic receiver is still injective

Suppose \(\mathcal M_t\widetilde\Lambda=0\). For \(w\in\mathbb C\), the meromorphic source element
\[
V_w(s)=\frac{g_t(s)e^{(1-s)w}}s
=\frac{g_t(s)(e^{(1-s)w}-8e^wF_0(s))}s+e^wh_t(s)
\tag{NPE6.1}
\]
has residue \(e^w\). The first term is entire, since its numerator vanishes at zero. The seminorm estimate used in NHJ3, including removable division, gives entire dependence on \(w\) and, for every fixed continuous functional,
\[
L(w):=\widetilde\Lambda(V_w),\qquad
|L(w)|\le C\exp(C(1+|w|^2)).
\tag{NPE6.2}
\]
For completeness the controlling exponential at \(s=x+iy,w=a+ib\) is bounded on \(|x|\le A\) by
\(e^{tA^2+(1+A)|a|}e^{-ty^2+by}\); completing the quadratic bounds every vertical power by a polynomial in \(|b|\) times \(e^{b^2/(4t)}\). On a fixed disk the entire divided term is bounded by its boundary values. The term \(e^wh_t\) has only exponential dependence on \(w\). These estimates also hold after every fixed derivative in \(w\), proving source-valued holomorphy.

The first n zero coefficients of \(\mathcal M_t\) sum to \(-\widetilde\Lambda(V_{\log n})\). Thus \(L(\log n)=0\) for every recovered positive integer. Jensen's formula centered at a point where a nonzero L does not vanish would bound its zeros in a radius-R disk by \(O(R^2)\), from (NPE6.2). The distinct points \(\log n\), \(n\le e^{R/2}\), lie in that disk for sufficiently large R and outnumber that bound. Consequently \(L=0\).

The exact derivative identity in E is
\[
(\partial_w-1)V_w=-g_t(s)e^{(1-s)w}\in\mathcal B.
\tag{NPE6.3}
\]
It gives \(\Lambda(g_te^{vs})=0\) for every complex v. This forces \(\Lambda=0\) on the original B, with the following complete continuation. For \(F\in\mathcal B\) and real \(u>t\), put \(H=e^{(u-t)s^2}F\). The exact inverse half-Mellin formula
\[
a_H(x)=\frac{x^{-1/2}}\pi\int_{\mathbb R}H(1/2+iy)x^{-iy}dy,\qquad
H(s)=\frac12\int_{\mathbb R}a_H(e^v)e^{sv}dv
\tag{NPE6.4}
\]
has \(a_H(e^v)\) decreasing faster than every exponential, by shifting the integration line to any fixed real coordinate using the rapid strip bounds. Hence multiplying its second formula by \(g_t\) converges in every B seminorm: \(q_{A,N}(g_te^{vs})\le C_{A,N,t}e^{A|v|}\). Application of \(\Lambda\) gives \(\Lambda(e^{us^2}F)=0\). That scalar function of u is holomorphic on \(\Re u>0\); compact subsets have a uniformly negative vertical quadratic dominating every derivative. The identity theorem extends its vanishing to that half-plane. Finally
\[
q_{A,N}((e^{us^2}-1)F)\le u e^{A^2}(A^2+1)q_{A,N+2}(F)\quad(0<u\le1)
\]
by the integral remainder. Letting u decrease to zero proves \(\Lambda(F)=0\). Now (NPE6.1) gives \(L(w)=e^w\alpha\), so \(\alpha=0\). We have proved injectivity on all \(E'_\beta\), not only a quotient or a finite-jet subspace.

In particular \(\mathcal H_t(\mathcal B')\cap\mathbb C(1-z)^{-1}=\{0\}\). Any equality \(\mathcal H_t\Lambda=\overline\alpha/(1-z)\) would be a zero of the just-proved injective \(\mathcal M_t\). No information has been deleted by retaining the residue coordinate.

## NPE7. The maximal Hardy graph on the extended source

Define its exact domain
\[
\widetilde{\mathfrak D}_t
=\{(\Lambda,\alpha):\mathcal H_t\Lambda-\overline\alpha/(1-z)\in H^2\}.
\tag{NPE7.1}
\]
The graph in \(E'_\beta\times H^2\) is closed: convergence in the source dual gives convergence of each test value, and convergence in Hardy norm gives convergence of each Hardy coefficient. Their matching equalities therefore persist at the limit. Its operator is injective by NPE6. Its graph topology is complete because \(E'_\beta=\mathcal B'_\beta\oplus\mathbb C\) is complete (NHJ6's direct strong-Cauchy proof applies to B), and a closed subspace of its product with H² is complete.

Equation (NPE5.6), and boundedness of the original raw-cover adjoint on H², prove invariance of this entire graph domain under every \((U_n^E)'\). Its projection into B' is injective: if both \((\Lambda,\alpha)\) and \((\Lambda,\beta)\) belong, then \((\overline\alpha-\overline\beta)/(1-z)\in H^2\). The coefficients of that function are constant, whose squared sum is finite only when \(\alpha=\beta\). Thus the boundary coordinate is unique whenever it exists; it has not been freely subtracted from an arbitrary Hardy vector.

The old full prequotient Hardy domain is recovered exactly on the zero-coordinate slice:
\[
\widetilde{\mathfrak D}_t\cap(\mathcal B'\oplus\{0\})
=\mathfrak D_t^{\mathcal B}\oplus\{0\}.
\tag{NPE7.2}
\]
For \((\Lambda,0)\) in that slice, its n-th cover remains in the same slice exactly when \(\Lambda(\delta_{n,t})=0\), by (NPE5.2). This recovers the entire-source obstruction without confusing it with invariance of the larger graph.

The exact degree identity on this extended graph is also retained. Writing \(C=\mathcal M_t\) on its H² domain and taking the usual inner product linear in the first variable, the raw identities \(W_n^*W_n=nI\), \(W_nW_n^*=nP_n\) give
\[
n\|C\widetilde\Lambda\|^2-\|C(U_n^E)'\widetilde\Lambda\|^2
=n\|(I-P_n)C\widetilde\Lambda\|^2.
\tag{NPE7.3}
\]
Indeed insert (NPE5.6) and evaluate the reverse product \(W_nW_n^*\). Covariance is now exact before quotienting, while the unilateral projection term remains. No degree is removed or rescaled.

## NPE8. The added mode has explicit evaluations and original-zeta pairing

For every \(s\ne0\), evaluation \(\operatorname{ev}_s:E\to\mathbb C\) is continuous. Its product coordinates are \((\operatorname{ev}_s|_{\mathcal B},h_t(s))\). For \(\Re s>1/2\), let
\[
g_s(z)=\sum_{m\ge0}\overline{\phi_m(s)}z^m.
\]
This belongs to H²: for \(m\ge1\), integrating the derivative of \(x^{1-s}\) bounds \(|\phi_m(s)|\le |1-s|\,|s|^{-1}m^{-\Re s}\); the constant coefficient is finite, and at \(s=1\) the positive-index coefficients are zero. Consequently
\[
\mathcal M_t\operatorname{ev}_s=\overline{g_t(s)}g_s,
\qquad \operatorname{ev}_s\in\widetilde{\mathfrak D}_t,
\qquad (U_n^E)'\operatorname{ev}_s=n^{1-s}\operatorname{ev}_s.
\tag{NPE8.1}
\]
For example s=1 gives the nonzero constant Hardy function \(-e^t\), with residue-coordinate \(h_t(1)=e^t\). It demonstrates concretely that the enlarged graph is not its zero-coordinate slice and does not itself impose the zeta divisor.

In the open strip \(1/2<\Re s<1\), the full original pairing from NHR is
\[
\langle h_k,\mathcal M_t\operatorname{ev}_s\rangle
=g_t(s)(1-k^{1-s})\frac{\zeta(s)}s,\qquad k\ge2.
\tag{NPE8.2}
\]
The Gaussian has the displayed sign of conjugation because the inner product is conjugate-linear in its second argument. The factor \(1-k^{1-s}\) cannot vanish in this strip: the modulus of \(k^{1-s}\) is \(k^{1-\Re s}>1\). The other two displayed factors are nonzero there. It follows directly that this evaluation receiver is orthogonal to every original \(h_k\) exactly when \(\zeta(s)=0\). Also its residue-coordinate \(h_t(s)\) is zero exactly at such a zero, by the original multiplier and its nonzero completion factors in the strip. Thus the enlarged source preserves the actual distinction between cover covariance and the original-zeta orthogonality equation, through explicit maps rather than a chosen identification.

For full zero jets, NPE1.1 retains their order: the functional \(F\mapsto F^{(j)}(\rho)\), extended by evaluating actual meromorphic derivatives, has residue-coordinate \(h_t^{(j)}(\rho)=0\) for every \(0\le j<m_\rho\). Its uncorrected-test receiver is exactly the original differentiated Noor kernel with the complete Leibniz derivatives of \(g_t\). No multiplicity direction is removed by this statement.

## NPE9. Result, source use and continuation

This calculation performs the proposed foundational change explicitly: the pole already present in the original correction is retained as a source extension. The larger analytic receiver is injective and exactly covariant before quotienting. Its maximal Hardy graph is invariant. The entire-source subspace, its discrepancy, the full ideal pushout and the original-zeta orthogonality remain separately recoverable. The same-degree two-dimensional endpoint action records a nonzero square-zero component even though its trace and determinant do not depend on that component.

The next source-level test has now been completed independently and read in full: NCI0–8 proves that the discrepancies generate the whole original full-jet ideal after closure in its original topology. NPE10 receives that exact theorem into the present extension. NPE1–8 need only the proved inclusion of each discrepancy in I and remain valid independently of that further identification.

Programme inputs read for the current continuation are NHJ0–9, ABH0–8/AHR0–9, GDE0–13, GSP0–9 (GSP1–2 reread here), and the completed CQF0–10/ACC0–9 comparisons. The latter distinguish an equivariant section from specialization-surjectivity; NPE3 makes that distinction concrete for this endpoint extension. The source identities used here are all stated with their proof or exact receiving map. The meromorphic extension and dual comparison are programme derivations, not a claim of a new human-source theorem.

Human source for the original coefficients and pairing: S. Waleed Noor, [A Hardy space analysis of the Báez-Duarte criterion for the RH, arXiv:1809.09577v4](https://arxiv.org/abs/1809.09577v4), through the retained author-TeX reading ledger and complete NHR derivation. The original source geometry remains Connes–Consani, [arXiv:0903.2024v3 §5](https://arxiv.org/abs/0903.2024v3). The target comparison remains Deligne, [Weil II §3.6](https://numdam.org/item/PMIHES_1980__52__137_0/). No new entire-paper reading is claimed. This coefficient extension is not identified with Deligne's geometric weight filtration, and no RH resolution or original lifting vanishing is asserted.

## NPE10. The full original quotient is exactly the stable zero-coordinate slice

NCI5.2 proves, on precisely the B and I used here,
\[
\overline{\operatorname{span}\{\delta_{n,t}:n\ge2\}}^{\mathcal B}=I.
\tag{NPE10.1}
\]
It uses global Gaussian division with all multiplicities, entire sampling at every log n, and the exact half-Mellin integral. Consequently the largest linear subspace of the slice \(\sigma_t\mathcal B'\subset E'\) invariant under every \((U_n^E)'\) is
\[
\sigma_t(I^\perp)=\{(\Lambda,0):\Lambda\in I^\perp\}.
\tag{NPE10.2}
\]
Indeed invariance forces the last coordinate \(-\Lambda(\delta_{n,t})\) in (NPE5.2) to vanish for every n. Continuity and (NPE10.1) imply \(\Lambda(I)=0\). Conversely this annihilation is preserved by every U_n', since U_n preserves all original zero orders, and (NPE5.2) keeps the last coordinate zero. These arguments also prove maximality by inclusion, without an assumed splitting of a source quotient.

Intersecting with the actual Hardy graph gives the exact largest all-cover-invariant subspace contained in its zero-coordinate slice:
\[
\sigma_t\bigl(\mathfrak D_t^{\mathcal B}\cap I^\perp\bigr)
=\sigma_t\bigl(q'\mathfrak D_t^Q\bigr).
\tag{NPE10.3}
\]
For the forward implication use (NPE10.2) and the exact slice identity (NPE7.2). For the reverse implication the whole extended Hardy graph is invariant by (NPE5.6), while the ideal annihilation keeps each image in the same slice. The source topology and graph norm are still the stated ones; no surjectivity from the entire Q' to a Hardy space has been inferred.

Thus retaining the pole gives exact covariance on a larger, injectively observed source. Requiring the zero-coordinate slice to persist under the complete cover family recovers the original full-jet zeta quotient inside it. Both constructions and their comparison are now proved. Neither property by itself removes the unilateral projection in (NPE7.3), and neither discards the full jets or the separate endpoint character.
