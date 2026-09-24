# The positive transfer quotient, its full source, and the retained arithmetic defect

24 September 2026. Complete derivation PSC0–PSC9.

## PSC0. Actual prerequisites and the attempted construction

The support remains \(\tau\langle Z_1;\mathrm{no}\ Z_2\rangle\). Arithmetic and coefficient operations here follow the complete-history reconstruction; no addition, numerical value, parity, midpoint or coordinate is assigned to the support. The two branch histories remain separate. The corpus corrections concerning source maps, quotienting, retained counting data and admissibility were reread before this construction, including the complete direct global-quotient argument. The current workflow expressly requests the canonical quotient of a calculated pairing defect and its induced trace and transfer. This note carries out that step and computes the data needed to reconstruct the original source.

Use the proved entire strip-polynomial multiplier ring \(M\), its rapid-strip ideal \(\mathcal B\), full original-zero ideal \(\mathcal I\), and quotient \(\mathcal Q=\mathcal B/\mathcal I\). GTAH0–GTAH1 and RTT5–RTT6 give
\[
E:\mathcal Q\longrightarrow H=\ell^2(\mathscr Z,m_\rho),\quad E[F]_\rho=F(\rho),
\quad W(x,y)=\langle x,Jy\rangle,
\quad (Jx)_\rho=x_{\rho^\#},\quad\rho^\#=1-\overline\rho.
\tag{PSC0.1}
\]
The inner product is linear in its first argument. Every multiplicity \(m_\rho\) is retained. The actual global full-jet isolators \(e_{\rho,j}\in\mathcal Q\) are given by RD1. No density of finite-support classes in the original Fréchet topology is assumed. Finite value vectors are in \(E\mathcal Q\), which is dense in \(H\).

For \(a>0\), the coefficient operators are \(T_a x_\rho=a^\rho x_\rho\) and \(U_a=aT_{1/a}\). For a recovered positive integer \(a=n\), GTR constructs the actual degree-\(n\) cover and its transfer; no nonintegral cover is asserted. GTAH proves
\[
D_a=T_a^*-U_a,\qquad
(D_a x)_\rho=e^{-i\Im\rho\log a}
(a^{\Re\rho}-a^{1-\Re\rho})x_\rho.
\tag{PSC0.2}
\]
RTT supplies the continuous injective anti-linear map \(A:H\to\mathcal H_{\rm res}\), with
\[
(\widehat\iota Ay)(F)=\langle EF,Jy\rangle,\qquad S=AE.
\tag{PSC0.3}
\]
ECR and ECI construct the actual cyclic extension-class maps to these spaces. Their full original factors and degree actions are retained below.

## PSC1. The canonical projector is constructed from the measured defect

Partition the actual divisor, without asserting either part empty, as
\[
\mathscr Z_{\rm line}=\{\rho\in\mathscr Z:\Re\rho=1/2\},
\qquad\mathscr Z_{\rm off}=\{\rho\in\mathscr Z:\Re\rho\ne1/2\}.
\tag{PSC1.1}
\]
Both subsets are preserved by conjugation and \(\#\), with their original multiplicities. Let \(H_{\rm line}\), \(H_{\rm off}\) be the corresponding closed coordinate subspaces and \(P_{\rm line}\), \(P_{\rm off}\) their orthogonal projections. These are observations on the complete arithmetic receiver, not alternative definitions of its original divisor.

For any fixed recovered \(a>1\), put \(B_a=D_a^*D_a\). This is bounded and positive, with exact diagonal coefficient
\[
b_a(\rho)=(a^{\Re\rho}-a^{1-\Re\rho})^2.
\tag{PSC1.2}
\]
Its zero coefficients are exactly the line subset. Thus
\[
\ker B_a=H_{\rm line},\qquad
\overline{\operatorname{ran}B_a}=H_{\rm off},\qquad
P_{\rm line}=\operatorname*{s-lim}_{R\to+\infty}e^{-RB_a}.
\tag{PSC1.3}
\]
For the range assertion, every finite vector supported off the line is an image: divide its finitely many nonzero coordinates by their strictly positive \(b_a(\rho)\). Such vectors are dense in \(H_{\rm off}\). Conversely every image is supported there. For the strong limit, the exponential is the norm-convergent power series of the bounded operator, hence has coefficient \(e^{-Rb_a(\rho)}\). For each \(x\in H\),
\[
\|(e^{-RB_a}-P_{\rm line})x\|^2
=\sum_{\rho\in\mathscr Z_{\rm off}}m_\rho
e^{-2Rb_a(\rho)}|x_\rho|^2\longrightarrow0.
\tag{PSC1.4}
\]
Dominated convergence applies with the actual summable majorant \(m_\rho|x_\rho|^2\). This constructs the projector globally, without a numerical zero-height cutoff, a spectral gap, or simplicity. The outcome is independent of the chosen recovered \(a>1\), since its diagonal zero set is the same.

All \(T_a,U_a,J\) commute with these two projections. On \(H_{\rm line}\), direct substitution gives
\[
(T_a|_{H_{\rm line}})^*=U_a|_{H_{\rm line}},\qquad
U_aT_a=aI,\qquad W|_{H_{\rm line}}=\langle\ ,\ \rangle.
\tag{PSC1.5}
\]
The complete degree factor remains \(a\). We have constructed the positive receiver on the quotient \(H/H_{\rm off}\simeq H_{\rm line}\), together with its section as the orthogonal subspace of \(H\). The quotient does not erase the retained complementary space.

## PSC2. The full source quotient and its higher jets

Human-source attribution: the topological inverse used here is the classical open mapping theorem for Fréchet spaces. See Terence Tao, [245B, Notes11: The strong and weak topologies](https://terrytao.wordpress.com/2009/02/21/245b-notes-11-the-strong-and-weak-topologies/), §1, Remark1 (21 February2009), explicitly recording the Fréchet extension, and [Notes9, Theorem3](https://terrytao.wordpress.com/2009/02/01/245b-notes-9-the-baire-category-theorem-and-its-banach-space-consequences/) for the Banach proof. The present proof checks the closedness and completeness required for its application; the cited Remark records the extension rather than supplying a full Fréchet proof.

For either subset \(T=\mathscr Z_{\rm line}\) or \(T=\mathscr Z_{\rm off}\), define actual closed \(M\)-submodules
\[
\mathcal I_T^{\rm jet}=\{F\in\mathcal B:\operatorname{ord}_\rho F\ge m_\rho\ (\rho\in T)\},
\qquad
\mathcal I_T^{\rm val}=\{F\in\mathcal B:F(\rho)=0\ (\rho\in T)\}.
\tag{PSC2.1}
\]
Closedness follows by intersecting the kernels of the continuous derivative evaluations. Their continuity follows from Cauchy's estimate on a fixed circle around each specified point, inside a bounded real strip. Multiplication by each \(h\in M\) preserves these kernels and is continuous on \(\mathcal B\), by its polynomial strip bounds and the defining seminorms of \(\mathcal B\). Put
\[
Q_T^{\rm jet}=\mathcal B/\mathcal I_T^{\rm jet},\qquad
Q_T^{\rm val}=\mathcal B/\mathcal I_T^{\rm val}.
\tag{PSC2.2}
\]
These are Fréchet quotient spaces, and the exact sequence
\[
0\longrightarrow\mathcal I_T^{\rm val}/\mathcal I_T^{\rm jet}
\longrightarrow Q_T^{\rm jet}\longrightarrow Q_T^{\rm val}
\longrightarrow0
\tag{PSC2.3}
\]
retains every higher jet as its stated kernel. It is a strict sequence by the open mapping theorem applied to the displayed Fréchet quotients.

The original \(\mathcal I\) is contained in both ideals of (PSC2.1). Hence the original \(\mathcal Q\) maps onto both spaces. The precise kernel of the map to the positive value receiver is
\[
\ker(P_{\rm line}E)=\mathcal I_{\mathscr Z_{\rm line}}^{\rm val}/\mathcal I.
\tag{PSC2.4}
\]
The induced map \(Q_{\mathscr Z_{\rm line}}^{\rm val}\to H_{\rm line}\) is continuous, injective and has dense image, because every finite line-value vector has an original full-jet isolator representative. Its norm completion is exactly \(H_{\rm line}\). No assertion that the Fréchet topology equals the value norm topology is made. The analogous statements hold for the off-line subset.

The induced source operations \(T_a,U_a,L\), conjugation and \(K_1F(s)=\overline{F(1-\overline s)}\) are well-defined on each of the jet and value quotients; their defining ideals are invariant. Every original multiplicity is retained in the value norm, even after the nonconstant jet coordinates pass into (PSC2.3).

## PSC3. Exact reconstruction of the full source from the two observations

Write \(J_L=\mathcal I_{\mathscr Z_{\rm line}}^{\rm jet}\), \(J_O=\mathcal I_{\mathscr Z_{\rm off}}^{\rm jet}\). Then
\[
J_L\cap J_O=\mathcal I.
\tag{PSC3.1}
\]
Retain the actual reconstruction defect module
\[
C_{\rm rec}=\mathcal B/(J_L+J_O).
\tag{PSC3.2}
\]
This is an algebraic quotient equipped, when used topologically, with its quotient locally convex topology; no closedness of the sum or Hausdorff property is asserted. There is a completely explicit exact sequence of \(M\)-modules
\[
0\longrightarrow\mathcal Q
\xrightarrow{\Delta}Q_{\mathscr Z_{\rm line}}^{\rm jet}\oplus Q_{\mathscr Z_{\rm off}}^{\rm jet}
\xrightarrow{d}C_{\rm rec}\longrightarrow0,
\tag{PSC3.3}
\]
where \(\Delta[F]=([F]_{J_L},[F]_{J_O})\) and \(d([f],[g])=[f-g]\). Independence of representatives follows from the denominator of (PSC3.2); surjectivity follows by using \(([f],0)\). Injectivity of \(\Delta\) is (PSC3.1). If \(f-g=l+o\), with \(l\in J_L,o\in J_O\), then \(F=f-l=g+o\) is an original representative mapping to the given pair. This proves exactness at the middle and the complete inverse on compatible pairs.

Thus the original full-jet source is exactly the algebraic fibre product over \(C_{\rm rec}\), with explicit inverse. The maps in (PSC3.3) are continuous. The inverse onto the image of \(\Delta\) is continuous exactly when \(J_L+J_O\) is closed. Indeed closedness makes \(C_{\rm rec}\) Fréchet and \(\ker d\) a closed Fréchet subspace of the product, so the open mapping theorem applies to the bijection \(\Delta:\mathcal Q\to\ker d\). Conversely, a continuous inverse makes its image complete in the induced Hausdorff locally convex topology, hence closed. The preimage of that closed image under \(f\mapsto([f]_{J_L},0)\) is precisely \(J_L+J_O\), proving closedness.

The exact closure of the image is also calculable:
\[
\overline{\Delta(\mathcal Q)}
=\ker\!\left(
Q_{\mathscr Z_{\rm line}}^{\rm jet}\oplus Q_{\mathscr Z_{\rm off}}^{\rm jet}
\longrightarrow \mathcal B/\overline{J_L+J_O}\right),
\tag{PSC3.3a}
\]
where the map is again the difference. Containment follows by continuity. For the reverse, write \(f-g=\lim(l_j+o_j)\) in the Fréchet space, with \(l_j\in J_L,o_j\in J_O\). Then \(F_j=f-l_j\) has first observation exactly \([f]_{J_L}\), and its second tends to \([g]_{J_O}\), since \(F_j-g-o_j\to0\). This proves the formula. No arbitrary-subset interpolation or closedness assumption is made. The kernel discarded by the positive jet quotient has its further exact description
\[
0\longrightarrow J_L/\mathcal I
\xrightarrow{[F]\mapsto[F]_{J_O}} Q_{\mathscr Z_{\rm off}}^{\rm jet}
\longrightarrow C_{\rm rec}\longrightarrow0.
\tag{PSC3.4}
\]
Its image is \((J_L+J_O)/J_O\), which proves the assertion. The same construction with value ideals has intersection \(\mathcal I_{\mathscr Z}^{\rm val}\), retaining the separate passage from the original jets to the value observation.

These formulas preserve both source observations and their compatibility data. They do not replace the full source by a freely chosen direct sum. If either divisor subset is empty, its ideal is \(\mathcal B\), and the formulas correctly give the corresponding zero quotient and zero reconstruction defect.

## PSC4. Original and compressed residue maps

On the original source define actual maps to the already constructed strong residue space by
\[
S_L=AP_{\rm line}E,\qquad S_O=AP_{\rm off}E,\qquad S=S_L+S_O.
\tag{PSC4.1}
\]
They are continuous and anti-linear, and their kernels are exactly the respective value ideals modulo \(\mathcal I\), by injectivity of \(A\). Evaluation against \(F\in\mathcal Q\) gives
\[
\widehat{\mathcal R}(F,S_TG)=W_T(F,G)
=\sum_{\rho\in T}m_\rho F(\rho)\overline{G(\rho^\#)}.
\tag{PSC4.2}
\]
The sum converges absolutely by Cauchy–Schwarz and is bounded on each bounded test set by the corresponding full \(E\)-norm bound. Both subsets are \(\#\)-stable. Consequently
\[
W=W_L+W_O,\qquad W_L(F,F)=\sum_{\rho\in\mathscr Z_{\rm line}}m_\rho|F(\rho)|^2\ge0,
\tag{PSC4.3}
\]
and all cross pairings between their Hilbert subspaces vanish.

For every actual off-line orbit \(\{\rho,\rho^\#\}\), the original isolators give
\[
W_O(e_{\rho,0}-e_{\rho^\#,0},e_{\rho,0}-e_{\rho^\#,0})=-2m_\rho,
\quad
W_O(e_{\rho,0},e_{\rho^\#,0})=m_\rho.
\tag{PSC4.4}
\]
These are statements about each orbit in the actual set, not a claim that such an orbit exists. They prove that quotienting by \(H_{\rm off}\) is a compression of the original Weil form, not its descent unless the discarded subspace is zero. More generally, the radical of \(W\) on \(H\) is zero: \(W(x,Jx)=\|x\|^2\). A sesquilinear form descends through a quotient exactly when its kernel pairs to zero with every vector, as follows by changing either representative. This gives the exact descent test without identifying the quotient's new positive form with the old form.

The projector construction in PSC1 yields an actual residue-space limit
\[
A e^{-RB_a}EG\longrightarrow S_LG
\quad\hbox{in the strong residue topology for every }G\in\mathcal Q.
\tag{PSC4.5}
\]
Indeed (PSC1.4) is norm convergence in \(H\), and \(A\) is continuous into that topology. Finite original isolators also give explicit source representatives for each value approximation:
\[
G_{R,E_0}=\sum_{\rho\in E_0}e^{-Rb_a(\rho)}G(\rho)e_{\rho,0},
\qquad E_0\subset\mathscr Z\text{ finite}.
\tag{PSC4.6}
\]
Their value vectors converge to \(e^{-RB_a}EG\) in \(H\), so their actual residue images converge to the left side of (PSC4.5). No convergence in the original full-jet source topology is asserted, and the omitted higher jets remain exactly (PSC2.3). This is a convergent global construction, not a bounded numerical test.

## PSC5. The original arithmetic formula and the exact discarded contribution

Human-source attribution: the explicit formula is due to A. P. Guinand, *A summation formula in the theory of prime numbers*, Proc. London Math. Soc. (2)50 (1949),107–119, and André Weil, *Sur les formules explicites de la théorie des nombres premiers*, Comm. Sém. Math. Univ. Lund (1952),252–265. The inspected native-TeX witness is Alain Connes, [arXiv:2602.04022v1](https://arxiv.org/abs/2602.04022v1), “Riemann’s formula, von Mangoldt paper”, equations `mellin`, `bombieriexplicit`, `bombieriexplicit1`, `bombieriexplicit2` (lines463–482). The historical originals are credited through that witness; no new reading of those originals is claimed. The full logarithmic-coordinate transport and admissible-test estimates used in this programme remain in GIQ9 and the earlier complete trace derivation.

Take actual \(F,G\in\mathcal B\) and retain
\[
A_{F,G}(s)=F(s)\overline{G(1-\overline s)},\qquad
A(s)=\int_{\mathbb R}v(u)e^{-(s-1/2)u}\,du,
\quad\widehat v(y)=A(1/2+iy).
\tag{PSC5.1}
\]
GIQ9 proves that the inverse test \(v\) is in the complete admissible logarithmic test space, by the original inverse-Mellin, reflection and convolution estimates. The full original formula is
\[
W_L(F,G)+W_O(F,G)
=A(0)+A(1)+\mathcal A_\infty(v)-P_{\rm hist}(v),
\tag{PSC5.2}
\]
where no term is changed:
\[
\mathcal A_\infty(v)=\frac1{2\pi}\int_{\mathbb R}\widehat v(y)
\left(\Re\frac{\Gamma'(1/4+iy/2)}{\Gamma(1/4+iy/2)}-\log\pi\right)dy,
\]
\[
P_{\rm hist}(v)=\sum_{n\ge2}\frac{\log L_n-\log L_{n-1}}{\sqrt n}
\bigl(v(\log n)+v(-\log n)\bigr),\qquad L_n=\operatorname{lcm}(1,\ldots,n).
\tag{PSC5.3}
\]
Thus the positive compression has the exact arithmetic expression
\[
W_L(F,G)=A(0)+A(1)+\mathcal A_\infty(v)-P_{\rm hist}(v)-W_O(F,G).
\tag{PSC5.4}
\]
The discarded term is explicitly the complete off-line sum, not an endpoint, completion multiplier, or adjustment to the prime counter. In particular both endpoints remain \(A(0)=F(0)\overline{G(1)}\) and \(A(1)=F(1)\overline{G(0)}\).

At every finite trivial-divisor cutoff \(b\ge1\), preserve
\[
V_{\zeta,b}=W_L+W_O+\sum_{r=1}^b A(-2r)-A(1),\qquad
G_b=\mathcal A_\infty(v)+A(0)+\sum_{r=1}^b A(-2r),
\]
\[
V_{\zeta,b}=G_b-P_{\rm hist}(v),\qquad
V_{L,b}=G_b-P_{\rm hist}(v)-W_O,
\tag{PSC5.5}
\]
where \(V_{L,b}=W_L+\sum_{r=1}^bA(-2r)-A(1)\). Here \(A(-2r)=F(-2r)\overline{G(1+2r)}\). No divergent infinite trivial-zero sum or new zeta function is introduced.

The exact morphism back to the original Weil functional is addition of the retained functional \(W_O\), as proved term by term in (PSC5.2). Formula (PSC4.4) proves that this functional is zero on all original pairs exactly when the actual off-line divisor is empty. This calculates the precise information needed to reconstruct the original trace after positive compression.

## PSC6. Exact transport from the original extension-class generator

ECR1 and ECI12 give \(\mathscr C=M/\mathfrak a\simeq Me_0\), \(g_t(s)=e^{ts^2}\), and \(b_t[h]=[g_th]\). Define
\[
S_{L,t}=AP_{\rm line}Eb_t,\quad S_{O,t}=AP_{\rm off}Eb_t,
\qquad Sb_t=S_{L,t}+S_{O,t}.
\tag{PSC6.1}
\]
These are algebraic-domain anti-linear maps to the strong residue space; no topology on the ambient Ext group is assumed. Every required source estimate is already proved in ECR1–ECR3. For \(T\) equal to either subset, the resulting exact trace is
\[
W_{T,t}(h,k)=\sum_{\rho\in T}m_\rho
e^{t\{\rho^2+(1-\rho)^2\}}h(\rho)\overline{k(\rho^\#)}.
\tag{PSC6.2}
\]
Its original source test is the entire function
\(e^{t\{s^2+(1-s)^2\}}h(s)\overline{k(1-\overline s)}\); substituting it into PSC5 retains every original arithmetic term. On the line its coefficient is \(e^{2t(1/4-(\Im\rho)^2)}\), which follows by direct substitution without dropping the factor \(e^{t/2}\).

The measured defect is entirely retained on the complementary value receiver:
\[
\|D_aEb_t(h)\|^2
=\sum_{\rho\in\mathscr Z_{\rm off}}m_\rho
e^{2t\{(\Re\rho)^2-(\Im\rho)^2\}}
b_a(\rho)|h(\rho)|^2.
\tag{PSC6.3}
\]
Every coefficient is the one proved in ECR5, and the line terms are zero. For \(h=1\), this is the original actual extension generator. The separator \(c\) of FOD satisfies \([c]=1\) in \(\mathscr C\), so it fixes both terms of (PSC6.1) and (PSC6.3). Its annihilation of the distinct normal class is transported by \(Uc=c(s+1)\), as proved in ECI9. On the original value space it acts as the identity on both pieces, supplying no separation between them. Its induced value action equals \(P_{\rm line}\) exactly when \(H_{\rm off}=0\), since \(I-P_{\rm line}=P_{\rm off}\). This proves the precise comparison without presupposing an off-line zero.

## PSC7. The exact space of full-jet holomorphic projectors

Define multiplier ideals \(\mathfrak a_T\subset M\) by full order \(m_\rho\) at every \(\rho\in T\). Then \(\mathfrak a_{\rm line}\cap\mathfrak a_{\rm off}=\mathfrak a\). The space of multipliers realizing the full-jet line projector is precisely
\[
\mathscr P=\{p\in M:p\in\mathfrak a_{\rm off},\ 1-p\in\mathfrak a_{\rm line}\}.
\tag{PSC7.1}
\]
This is an explicitly defined space of coefficient maps to investigate, not an assumed source splitting. Its elements are exactly the solutions to \(p+(1-p)=1\) with the two indicated ideal memberships. Therefore it is nonempty exactly when \(\mathfrak a_{\rm line}+\mathfrak a_{\rm off}=M\), and any two of its elements differ by \(\mathfrak a\). Each represents the same idempotent in \(M/\mathfrak a\), since \(p^2-p\) vanishes to full order on both subsets. These statements follow directly from the displayed ideal equalities.

Every \(p\in\mathscr P\) constructs the full source splitting, with inverse
\[
([f]_{J_L},[g]_{J_O})\longmapsto[pf+(1-p)g]_{\mathcal I}.
\tag{PSC7.2}
\]
It is independent of representatives because \(pJ_L\subset\mathcal I\) and \((1-p)J_O\subset\mathcal I\). Its two compositions are identities by the full-jet conditions, and it is continuous because multiplication is continuous. This proves that its existence forces \(C_{\rm rec}=0\), with the actual splitting exhibited. Neither \(\mathscr P\ne\varnothing\) nor \(C_{\rm rec}=0\) is assumed here.

For each \(T\), \(\mathcal I_T^{\rm jet}=\mathcal B\cap\mathfrak a_T\). Thus the maps \(Q_T^{\rm jet}\to M/\mathfrak a_T\) induced by inclusion and \(M/\mathfrak a_T\to Q_T^{\rm jet}\) induced by multiplication by \(g_t\) are injective, with both composites multiplying by \(g_t\). The proof is ECR1's strip bound and local-unit argument at the specified subset. This proves the relation between the source and multiplier versions of the reconstruction problem, without declaring their defect quotients equal.

## PSC8. A global estimate forced by a holomorphic projector

Every actual \(p\in\mathscr P\) has constants \(C>0\) and an integer \(N\ge0\), depending on that entire multiplier, such that for every \(\rho\in\mathscr Z_{\rm line}\) and \(\eta\in\mathscr Z_{\rm off}\) with \(|\rho-\eta|\le1\),
\[
1\le C(1+|\Im\rho|)^N|\rho-\eta|.
\tag{PSC8.1}
\]
Proof: on \(|\Re s|\le3\), polynomial strip growth bounds \(|p(s)|\) by \(C_0(1+|\Im s|)^N\). Every unit-radius circle centered on the segment from \(\rho\) to \(\eta\) stays in this strip, and its imaginary height differs from \(\Im\rho\) by at most two. Cauchy's derivative formula therefore bounds \(|p'|\) on the segment by \(C(1+|\Im\rho|)^N\), with \(C\) increased by the explicit bounded-height comparison. Integrating \(p'\) along the segment and using \(p(\rho)=1,p(\eta)=0\) proves (PSC8.1). If the two points are farther than one, their separation already exceeds one. The result treats every actual pair; it assumes no existence of a near pair or off-line zero.

Consequently a bounded Hilbert projector alone supplies neither this necessary entire-function estimate nor the full-jet interpolation of PSC7. The exact morphisms relating these constructions are PSC2, PSC3 and PSC7. The heat projector in PSC1 is constructed without this assumption, and its actual residue realization is PSC4.5–PSC4.6. This records the additional structure precisely and retains the reconstruction defect rather than discarding it.

## PSC9. Relation to the lifting goal and completed outcome of the attempt

FOD7 and NEA10 prove the specified derived original-quotient-source lifting vanishing while retaining the normal extension. Deligne's actual invariant-cycle cross instead has obstruction image \(\operatorname{im}\partial/\partial j(K)\), as established in DC5.3–DC5.4 from the full localization and inertia sequences. Neither this image quotient nor its duality weights is replaced here by a Hilbert quotient.

The present calculation implements the requested next attempt on the exact residue/positivity receiver. It constructs its canonical positive transfer quotient by a global operator limit; supplies its actual source quotient and all higher-jet kernels; reconstructs the full source as an explicit fibre product; and calculates the exact original-zeta arithmetic contribution that the compression discards. The additional full-jet multiplier problem is the concrete space \(\mathscr P\), with its source map and proved estimate. No arbitrary splitting or lossless normalization is presumed.

The original source and off-line contribution are retained for the next Deligne specialization/duality comparison. Their formulas quantify over the complete actual divisor. They neither posit an alternative arithmetic nor use a numerical sample to prove a global assertion. The measured defect's vanishing remains the active target, and is not inferred from the positive quotient obtained by removing its range.

Proof sources actually used: GTAH0–GTAH7, RTT5–RTT7 and RD1; ECR0–ECR7 and ECI0–ECI13 at their accepted versions; GIQ9's full original explicit formula and source-domain proof; FOD7, NEA10 and DC3.7–DC7 for the exact lifting comparison. Human-source identities and prior reading coverage are retained in the CC and original Deligne ledgers; no new whole-paper reading is claimed by this derivation.
