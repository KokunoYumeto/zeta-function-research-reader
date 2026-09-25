# Independent review of the retained meromorphic endpoint extension

25 September 2026. Complete mathematical review and further derivation NER0–NER11. The reviewed source is `NOOR_MEROMORPHIC_ENDPOINT_EXTENSION.md`, NPE0–NPE10, including the subsequently added uniqueness proof for its full-ideal pushout section and the final invariant-slice theorem. Its reviewed SHA256 is `da8a4d25c22391e32fddc44fac98d12de515679f2d5b013ee33639c6200134ed`. Exact source hashes and reading coverage are in `argument_reconstruction/NOOR_ENDPOINT_EXTENSION_REVIEW_RECEIPT.json`.

## NER0. Scope and actual source prerequisites

The supporting datum remains \(\tau\langle Z_1;\mathrm{no}\ Z_2\rangle\). The complex variable \(s\), residue at \(s=0\), functions, quotients and all scalar operations below belong to the coefficient system after complete-history arithmetic reconstruction. They assign no coordinate, arithmetic value, metric, parity or retracted addition to the supporting datum. Separate branch histories remain separate.

This review read the complete NPE0–10 source, and checked its operations against the already completely read NHJ0–9, NHD0–10, NHR0–9 and ABH0–8/AHR0–9 sources. NPE3's final uniqueness paragraph and NPE10 were separately read after insertion. NER1–10 do not need the NCI closed-span identity. The complete incoming NCI0–8 proof was then read and checked for the final NER11 receiving comparison. The review does not newly claim a complete reading of GSP, CQF or ACC: the full meromorphic construction and the topological comparisons used here are proved below directly from the source seminorms. The exact original half-Mellin comparison is rederived where needed.

The human Hardy input is S. Waleed Noor, *A Hardy space analysis of the Báez-Duarte criterion for the RH*, [arXiv:1809.09577v4](https://arxiv.org/abs/1809.09577v4), canonical source ID `PUBUNIT-803463A3EF787AE3E69C519B`. Its original-author TeX SHA256 is `bc3075483547782dce36bf55a6349899a26766fcfc8ae9f265079ec74601f2d3`. The preceding AHR review read its lines 114–387; no additional whole-paper reading is claimed here. The source's underlying cited books have not been newly read.

The single source typography issue found was a missing backslash before `quad` in NPE0.3. It has no mathematical effect, was reported to the parent, and its correction was verified before final source hashing. All judgments here concern the actual original functions and the displayed maps, not a declared identification with a geometric weight filtration.

## NER1. The meromorphic source and the residue are well defined

Retain the complete Fréchet source
\[
\mathcal B=\{F\in\mathcal O(\mathbb C):q_{A,N}(F)<\infty\},
\qquad q_{A,N}(F)=\sup_{|\Re s|\le A}(1+|\Im s|)^N|F(s)|,
\tag{NER1.1}
\]
for all \(A>0,N\ge0\). Its original closed ideal \(I\) imposes every derivative through order \(m_\rho-1\) at each actual nontrivial zero of original \(\zeta\). The complete original multiplier and its correction are
\[
F_0(s)=\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2)\zeta(s),\quad
R_t(s)=8e^{ts^2}F_0(s),\quad h_t(s)=R_t(s)/s,
\quad t>0.
\tag{NER1.2}
\]
Here \(R_t\in I\subset\mathcal B\), \(R_t(0)=1\), and
\(R_t'(0)=8F_0'(0)\). In particular \(h_t\) has one simple pole, of residue one, at zero. All its other points are regular. At a nontrivial zero \(\rho\), the multiplier \(8e^{ts^2}/s\) is a holomorphic unit, so the exact vanishing order is the original \(m_\rho\). The factor in (NER1.2) remains the complete original comparison: it does not replace \(\zeta\) or discard the pole, Gamma factor or trivial zeros.

Consequently
\[
E=\mathcal B+\mathbb C h_t,\quad f=F+ch_t,
\quad\operatorname{res}_0 f=c
\tag{NER1.3}
\]
is a space of actual meromorphic functions, with unique coordinates. The transported product topology is Hausdorff and complete. Its residue sequence is strict exact, since it becomes the product inclusion and projection in those coordinates. Its continuous vector-space section is \(c\mapsto ch_t\); this statement does not include equivariance.

For \(u,t>0\),
\[
h_u-h_t=8F_0(s)\frac{e^{us^2}-e^{ts^2}}s\in I.
\tag{NER1.4}
\]
The numerator has a zero of order at least two at zero. Outside a fixed disk both Gaussian terms decay faster than every vertical power on every fixed strip; division by \(s\) preserves those estimates there. Inside the disk the removable function is bounded. The full factor \(F_0\) preserves all original zero jets. Thus the product coordinates at the two parameters differ by the continuous shear \((F,c)\mapsto(F+c(h_t-h_u),c)\), whose inverse has the opposite difference. The actual space and topology are therefore parameter-independent, and the entire difference remains recorded.

## NER2. Cover action, exact cocycle and endpoint detection

For recovered positive integers, \(U_nf(s)=n^{1-s}f(s)\). This multiplier and its reciprocal are bounded on each vertical strip, hence preserve \(\mathcal B\) continuously. Direct multiplication gives
\[
U_nh_t=nh_t-\delta_{n,t},\quad
\delta_{n,t}=R_t(s)\frac{n-n^{1-s}}s\in I,
\quad\delta_{n,t}(0)=n\log n.
\tag{NER2.1}
\]
The divided function has removable value \(n\log n\), and the preceding strip/division argument proves its product belongs to \(\mathcal B\). Its full factor \(F_0\) puts it in \(I\). Thus the entire action, not only its residue, is
\[
U_n^E(F,c)=(U_nF-c\delta_{n,t},nc).
\tag{NER2.2}
\]
The residue line has the exact coefficient character \(\chi(n)=n\). Composition retains the cocycle with both orders:
\[
\delta_{mn,t}=m\delta_{n,t}+U_n\delta_{m,t}
=n\delta_{m,t}+U_m\delta_{n,t}.
\tag{NER2.3}
\]
For example substitute \(\delta_{m,t}=mh_t-U_mh_t\) into the first expression; its middle terms cancel, leaving \(mnh_t-U_{mn}h_t\). This also verifies the signs in the block action (NER2.2).

An equivariant section for any recovered \(n>1\) would have value \(h_t+F\) at one, and would require
\((U_n-n)F=\delta_{n,t}\). Evaluation at zero gives zero on the left and \(n\log n\ne0\) on the right. Therefore the residue sequence has no such section, even allowing discontinuous linear sections. The obstruction is detected by the continuous source map \(\operatorname{ev}_0\), not by an arithmetic operation on \(\tau\).

## NER3. Full-ideal pushout, topology and unique equivariant section

The subspace \(I\subset E\) is closed, because it is \(I\oplus\{0\}\) in product coordinates, and is invariant. The map
\[
E/I\longrightarrow Q\oplus\mathbb C_\chi,
\qquad[F+ch_t]\longmapsto([F],c),\qquad Q=\mathcal B/I,
\tag{NER3.1}
\]
is well-defined and bijective by residue uniqueness. It is a topological isomorphism: the continuous quotient map from \(\mathcal B\oplus\mathbb C\) is open, since the quotient map on its first factor and identity on its second are open. Its kernel is exactly \(I\oplus\{0\}\). Equation (NER2.1) makes the induced action diagonal, since \(\delta_{n,t}\in I\). The residue section \(c\mapsto[ ch_t]\) is equivariant and independent of \(t\) by (NER1.4).

This quotient is the continuous linear pushout of the residue sequence along \(q:\mathcal B\to Q\). To verify the full universal property, take continuous linear maps from \(E\) and \(Q\) into another locally convex space agreeing on the embedded \(\mathcal B\). The map from \(E\) annihilates \(I\), so has a unique continuous factor through the quotient \(E/I\). Its restriction to \(Q\) is the prescribed map because that copy is generated by the image of \(\mathcal B\). Equivariance is preserved when the incoming maps intertwine the actions. This proves the claimed pushout in the stated category.

The added uniqueness proof in NPE3 is correct. A difference between two equivariant residue sections is a class \([F]\in Q\) with \((n^{1-s}-n)F\in I\). For each actual nontrivial zero \(0<\Re\rho<1\),
\[
|n^{1-\rho}|=n^{1-\Re\rho}<n\qquad(n>1),
\]
so \(n^{1-s}-n\) is a holomorphic unit near \(\rho\). Division by its full local Taylor series proves that every required derivative of \(F\) vanishes, hence \(F\in I\). Thus the difference is zero. This keeps full multiplicities; it does not require a simplicity or spectral-gap assumption. It is separation of this residue character from the actual coefficient jets after arithmetic is available, not a proof of interior purity.

## NER4. The other pushout is exactly the endpoint Jordan extension

Let \(\mathcal B_0=\ker(\operatorname{ev}_0:\mathcal B\to\mathbb C)\). Evaluation is continuous and onto: \(a e^{s^2}\) has value \(a\) and belongs to \(\mathcal B\). It is equivariant for the character \(\chi(n)=n\). The quotient \(E/\mathcal B_0\) is therefore the pushout of the same original residue sequence along \(\operatorname{ev}_0\), by precisely the quotient universal-property proof in NER3.

For \(f=F+ch_t=c/s+a_0+O(s)\),
\[
a_0=F(0)+cR_t'(0)=F(0)+8cF_0'(0).
\tag{NER4.1}
\]
The quotient isomorphism is
\[
E/\mathcal B_0\longrightarrow\mathbb C^2,
\qquad[f]\longmapsto(a_0,c).
\tag{NER4.2}
\]
It has kernel exactly \(\mathcal B_0\), and is onto by independently specifying the residue and the value of an entire Gaussian multiple. A continuous linear right inverse is
\((a_0,c)\mapsto(a_0-cR_t'(0))e^{s^2}+ch_t\), so the quotient topology is the usual finite-dimensional topology.

Multiplying the complete Laurent series by \(n e^{-s\log n}\) gives
\[
(a_0,c)\longmapsto(na_0-n(\log n)c,nc),\qquad
J_n=\begin{pmatrix}n&-n\log n\\0&n\end{pmatrix}.
\tag{NER4.3}
\]
This is the nonsplit pushout detected by evaluation in NER2. Its nilpotent matrix \(N=\left(\begin{smallmatrix}0&1\\0&0\end{smallmatrix}\right)\) has \(N^2=0\), and \(J_n=n(I-(\log n)N)\). Both multiplication and the signs check: \(J_mJ_n=J_{mn}\), trace \(2n\), determinant \(n^2\). The algebra homomorphism \(a+b\epsilon\mapsto aI+bN\) is injective because \(I,N\) are linearly independent. Thus two explicit pushouts of the same retained sequence have been calculated: the full-ideal pushout splits uniquely; the evaluation pushout has a nonzero endpoint extension. Neither is assumed to identify the original geometric lifting class.

## NER5. An exact further comparison of the middle source and both inclusions

The larger meromorphic source has an additional useful description. Multiplication by the actual coefficient variable defines an equivariant topological isomorphism
\[
\boxed{m_s:E\longrightarrow\mathcal B,\qquad f\longmapsto sf.}
\tag{NER5.1}
\]
This statement is about the middle spaces; the original inclusion is retained below. For continuity, \(s(F+ch_t)=sF+cR_t\), and
\(q_{A,N}(sF)\le(A+1)q_{A,N+1}(F)\). The second summand is a fixed member of \(\mathcal B\). Injectivity follows from equality of actual meromorphic functions away from zero. The inverse is explicitly
\[
H\longmapsto H/s
=\frac{H-H(0)R_t}{s}+H(0)h_t.
\tag{NER5.2}
\]
The first term is entire. Its continuity into \(\mathcal B\) follows from the following division estimate, which also proves its required strip decay. For \(K\in\mathcal B\) with \(K(0)=0\), outside \(|s|<1\) one has \(|K(s)/s|\le|K(s)|\). On \(|s|\le1\), the maximum principle applied to the entire \(K(s)/s\) on the radius-two disk gives
\[
|K(s)/s|\le\tfrac12\sup_{|z|=2}|K(z)|
\le\tfrac12q_{2,0}(K).
\]
Thus
\[
q_{A,N}(K/s)\le q_{A,N}(K)+2^{N-1}q_{2,0}(K).
\tag{NER5.3}
\]
Both \(H\mapsto H(0)\) and \(H\mapsto H-H(0)R_t\) are continuous, so (NER5.2) is a continuous inverse. Finally \(sU_nf=U_n(sf)\) is equality of actual meromorphic products, proving equivariance.

The exact transported residue sequence is therefore
\[
\begin{array}{ccccccccc}
0&\to&\mathcal B&\to&E&\xrightarrow{\operatorname{res}_0}&\mathbb C_\chi&\to&0\\
&&\Vert&&\downarrow m_s&&\Vert\\
0&\to&\mathcal B&\xrightarrow{m_s}&\mathcal B&\xrightarrow{\operatorname{ev}_0}&\mathbb C_\chi&\to&0.
\end{array}
\tag{NER5.4}
\]
Indeed \((sf)(0)=\operatorname{res}_0 f\), and the original entire subspace maps to \(s\mathcal B=\mathcal B_0\), with equality proved by (NER5.3). Consequently (NER5.1) does not turn the original inclusion into the identity or discard the endpoint. It identifies precisely which inclusion and quotient are changed by adjoining the pole.

The ideal comparison is equally explicit:
\[
m_s(I)=sI=I\cap\mathcal B_0.
\tag{NER5.5}
\]
The forward containment is immediate. Conversely divide an element of \(I\) with value zero at zero by \(s\). Equation (NER5.3) keeps it in \(\mathcal B\), and division by the nonvanishing local function \(s\) at every nontrivial zero preserves all its vanishing jets, so it remains in \(I\).

Multiplication by \(s\) consequently induces a topological automorphism on \(Q\), with exact inverse
\[
[H]\longmapsto\left[\frac{H-H(0)R_t}{s}\right].
\tag{NER5.6}
\]
Well-definedness follows from the same division argument for differences in \(I\), since \(R_t\in I\). Continuity follows from the quotient topology and (NER5.3). The two compositions are identity: the product differs from \(H\) by \(H(0)R_t\in I\), while applying the inverse to \(sF\) simply returns \(F\). Every original derivative is retained by this map:
\[
(sF)^{(j)}(\rho)=\rho F^{(j)}(\rho)+jF^{(j-1)}(\rho),
\tag{NER5.7}
\]
with the second term absent for \(j=0\). Its inverse is the full Leibniz expansion of multiplication by \(1/s\), through every order \(j<m_\rho\). It is not a scalar-only replacement of that triangular jet action.

There is also a direct quotient map
\[
\mathcal B/(sI)\longrightarrow Q\oplus\mathbb C,
\qquad[H]\longmapsto([H],H(0)).
\tag{NER5.8}
\]
Its kernel is (NER5.5). It is onto because, for a representative \(F\) of a class and prescribed \(c\), the element \(F+(c-F(0))R_t\) has that class and value. The constructed quotient inverse is continuous: the formula on \(\mathcal B\oplus\mathbb C\) annihilates the representative ambiguity modulo \(sI\), so descends continuously by the product quotient. Under (NER5.1), the class of \(F+ch_t\) maps in these coordinates to \(([sF],c)\), not \(([F],c)\). The automorphism (NER5.6) is the exact comparison with NPE3.2.

Finally the endpoint quotient in NER4 transports to \(\mathcal B/s^2\mathcal B\): multiplication by \(s\) sends \(\mathcal B_0=s\mathcal B\) to \(s^2\mathcal B\), and \(sf=c+a_0s+O(s^2)\). The Taylor map
\(H\mapsto H(0)+H'(0)\epsilon\) identifies this quotient algebra with \(\mathbb C[\epsilon]/(\epsilon^2)\), including its product rule. It is onto by using \((a+bs)e^{s^2}\); its kernel is \(s^2\mathcal B\), by twice applying (NER5.3). This proves that the specific nilpotent endpoint action is the exact two-jet quotient after the meromorphic comparison. It does not assert that \(E\) itself is closed under pointwise multiplication: two simple poles can produce a double pole.

## NER6. Strong dual, signs and exact prequotient covariance

The product decomposition gives the strong-dual topological isomorphism
\[
E'_\beta=\mathcal B'_\beta\oplus\mathbb C,\quad
\widetilde\Lambda(F+ch_t)=\Lambda(F)+c\alpha.
\tag{NER6.1}
\]
Indeed projections of a bounded product set are bounded, and each factor's bounded sets embed in the product. Evaluating this functional on (NER2.2) proves, without a conjugation in the complex-linear transpose,
\[
(U_n^E)'(\Lambda,\alpha)
=(U_n'\Lambda,n\alpha-\Lambda(\delta_{n,t})).
\tag{NER6.2}
\]
The negative sign is necessary. It is zero on \(I^\perp\), exactly as the split pushout predicts.

Let \(\phi_0=-1/s\), \(\phi_m=(m^{1-s}-(m+1)^{1-s})/s\) for \(m\ge1\). The meromorphic tests \(G_{t,m}=g_t\phi_m\) have residue \(-1\), and the complete entire tests are \(F_{t,m}=G_{t,m}+h_t\). Thus
\[
\mathcal M_t(\Lambda,\alpha)(z)
=\sum_{m\ge0}\overline{\widetilde\Lambda(G_{t,m})}z^m
=\mathcal H_t\Lambda(z)-\frac{\overline\alpha}{1-z}.
\tag{NER6.3}
\]
This is conjugate-linear. The original polynomial bound for \(F_{t,m}\) in every source seminorm, together with the constant residue coordinate, implies that \(\sum G_{t,m}\bar z^m\) is a bounded family in \(E\) on every compact subdisk. Therefore the map is continuous from the full strong dual to the compact-open holomorphic topology.

Telescoping, with \(\phi_0\) included in the initial block, gives exactly
\[
\sum_{a=0}^{n-1}G_{t,nm+a}=U_n^EG_{t,m},\quad
\mathscr W_n^*\mathcal M_t=\mathcal M_t(U_n^E)'.
\tag{NER6.4}
\]
The continuity of coefficient-block summation on holomorphic disk functions follows from Cauchy's estimate on any radius \(R\) satisfying \(r^{1/n}<R<1\), exactly as in NHJ7. Substitution of (NER6.2) into (NER6.3) recovers the positive discrepancy
\[
\mathscr W_n^*\mathcal H_t\Lambda-\mathcal H_tU_n'\Lambda
=\frac{\overline{\Lambda(\delta_{n,t})}}{1-z}.
\tag{NER6.5}
\]
Thus both the old entire-source and new meromorphic-source signs agree with the same actual representative identity.

The source isomorphism in NER5 also has an explicit dual comparison. If \(\eta\in\mathcal B'\) and \(\widetilde\Lambda=\eta\circ m_s\), its product coordinates are
\[
\Lambda(F)=\eta(sF),\qquad\alpha=\eta(R_t).
\tag{NER6.6}
\]
The tests transported by \(m_s\) are \(sG_{t,0}=-g_t\) and
\(sG_{t,m}=g_t(m^{1-s}-(m+1)^{1-s})\) for \(m\ge1\). These are entire functions of the original source. Formula (NER6.6) records the exact change of observation; it does not conflate it with the earlier \(F_{t,m}\) observation.

## NER7. Independent all-source injectivity check

Suppose \(\mathcal M_t\widetilde\Lambda=0\). The source-valued meromorphic family
\[
V_w(s)=\frac{g_t(s)e^{(1-s)w}}s
=\frac{g_t(s)(e^{(1-s)w}-8e^wF_0(s))}s+e^wh_t(s)
\tag{NER7.1}
\]
belongs to \(E\). Its residue is \(e^w\); its first displayed coordinate is entire. It is an entire \(E\)-valued family. To check the growth needed below, write \(s=x+iy,w=a+ib\). On each fixed strip the first numerator exponential is bounded by
\(e^{tA^2+(1+A)|a|}e^{-ty^2+by}\).
Completing that quadratic bounds every vertical polynomial by a polynomial in \(|b|\) times \(e^{b^2/(4t)}\). The fixed \(F_0\) term and residue coordinate have exponential \(w\)-growth. On a fixed disk the removable entire quotient is bounded by its surrounding-circle values. The same estimates after differentiation prove source-valued holomorphy and yield
\[
L(w):=\widetilde\Lambda(V_w),\qquad |L(w)|\le C e^{C(1+|w|^2)}.
\tag{NER7.2}
\]
The first \(n\) coefficient sum is \(-\widetilde\Lambda(V_{\log n})\), so \(L(\log n)=0\) for every recovered positive integer. Jensen's formula at a point where a purported nonzero \(L\) does not vanish bounds its zero count in a radius-\(R\) disk by \(O(R^2)\). The distinct points \(\log n\) for \(n\le e^{R/2}\) lie in the disk for all sufficiently large \(R\) and contradict that bound. Hence \(L=0\).

The exact derivative as a source identity is
\[
(\partial_w-1)V_w=-g_te^{(1-s)w}\in\mathcal B.
\tag{NER7.3}
\]
Thus \(\Lambda(g_te^{vs})=0\) for all \(v\in\mathbb C\). To pass to all of \(\mathcal B\), fix \(F\in\mathcal B\), choose real \(u>t\), and set \(H=e^{(u-t)s^2}F\). Its inverse and forward half-Mellin formulas retain the exact constants
\[
a_H(x)=\frac{x^{-1/2}}\pi\int_{\mathbb R}H(1/2+iy)x^{-iy}\,dy,
\quad H(s)=\frac12\int_{\mathbb R}a_H(e^v)e^{sv}\,dv.
\tag{NER7.4}
\]
These constants follow by Fourier inversion: the Fourier transform with exponent \(+iyv\) of \(a_H(e^v)e^{v/2}\) is \(2H(1/2+iy)\). Rapid strip decay permits shifting the vertical integration line to any fixed real coordinate; its horizontal edge integrals tend to zero. Choosing that coordinate arbitrarily far to either side proves that \(a_H(e^v)\) decays faster than every exponential in \(|v|\). Therefore multiplying the second formula by \(g_t\) gives a source-seminorm convergent integral, because
\(q_{A,N}(g_te^{vs})\le C_{A,N,t}e^{A|v|}\) for real \(v\).
It follows that \(\Lambda(e^{us^2}F)=0\) for all real \(u>t\).

For fixed \(F\), this scalar function of \(u\) is holomorphic on \(\Re u>0\): on a compact parameter subset the real part of \(us^2\) is a uniformly negative quadratic in \(y\) plus a bounded linear term on each strip, controlling all derivatives and Taylor remainders. The identity theorem gives vanishing throughout that half-plane. The exact integral-remainder estimate
\[
q_{A,N}((e^{us^2}-1)F)
\le u e^{A^2}(A^2+1)q_{A,N+2}(F),\qquad0<u\le1,
\]
then permits \(u\downarrow0\), giving \(\Lambda(F)=0\). Now (NER7.1) yields \(L(w)=e^w\alpha\); hence \(\alpha=0\). This proves injectivity of the entire meromorphic-source dual receiver, without an ideal annihilator or finite-jet hypothesis. It also proves
\(\mathcal H_t(\mathcal B')\cap\mathbb C(1-z)^{-1}=\{0\}\)
by (NER6.3).

## NER8. Maximal Hardy graph, invariance and the retained degree defect

The precise Hilbert domain is
\[
\widetilde{\mathfrak D}_t
=\{(\Lambda,\alpha):\mathcal H_t\Lambda-\overline\alpha/(1-z)\in H^2\}.
\tag{NER8.1}
\]
There is no assertion of Hardy regularity for an arbitrary source-dual element. The graph is closed in \(E'_\beta\times H^2\): convergence in each factor gives convergence of every test value and every Hardy coefficient, so their equalities persist in the limit. The graph map is injective by NER7.

Its graph topology is complete. A strong Cauchy net in \(\mathcal B'\) has a pointwise linear limit and converges uniformly on every bounded source set. On each convergent source sequence and its limit, which form a compact bounded set, this makes the limit a uniform limit of continuous functions. It is sequentially continuous, hence continuous because \(\mathcal B\) is metrizable. This proves completeness of \(\mathcal B'_\beta\), and hence of \(E'_\beta\). A closed graph in its product with the complete Hilbert space is complete.

The exact covariance (NER6.4), with bounded \(W_n^*:H^2\to H^2\), proves invariance of the entire graph domain under each \((U_n^E)'\). Its projection to \(\mathcal B'\) is injective: two allowed coordinates for the same \(\Lambda\) would differ by a constant coefficient sequence in \(\ell^2\), which is possible only for zero difference. On its zero-coordinate slice the domain is exactly the previous \(\mathfrak D_t^{\mathcal B}\). Formula (NER6.2) says that a member of that slice remains in it under the \(n\)-th action exactly when \(\Lambda(\delta_{n,t})=0\). No NCI closed-span assertion is used here.

For \(C=\mathcal M_t\) restricted to this domain,
\[
n\|C\widetilde\Lambda\|^2-
\|C(U_n^E)'\widetilde\Lambda\|^2
=n\|(I-P_n)C\widetilde\Lambda\|^2.
\tag{NER8.2}
\]
Indeed Noor's raw cover repeats each coefficient \(n\) times, so \(W_n^*W_n=nI\), while its reverse composition is \(W_nW_n^*=nP_n\), with \(P_n\) block averaging. Substitute the exact covariance and evaluate this reverse product. The source extension removes the representative covariance discrepancy but retains the full unilateral degree defect; it does not supply an invertible positive-adjoint action by fiat.

## NER9. Evaluations, all zero jets and original-zeta orthogonality

Evaluation at any \(s\ne0\) is continuous on \(E\), with product coordinates \((\operatorname{ev}_s|_{\mathcal B},h_t(s))\). For \(\Re s>1/2\), the original coefficient function
\(g_s(z)=\sum_{m\ge0}\overline{\phi_m(s)}z^m\)
belongs to \(H^2\): integrate the derivative of \(x^{1-s}\) over \([m,m+1]\) to obtain
\[
|\phi_m(s)|\le |1-s|\,|s|^{-1}m^{-\Re s}\quad(m\ge1).
\]
The constant coefficient is \(-1/\bar s\), and at \(s=1\) all positive-index coefficients vanish. Directly evaluating the actual meromorphic tests proves
\[
\mathcal M_t\operatorname{ev}_s=\overline{e^{ts^2}}g_s,
\quad (U_n^E)'\operatorname{ev}_s=n^{1-s}\operatorname{ev}_s.
\tag{NER9.1}
\]
For example \(s=1\) gives \(-e^t\), with nonzero boundary coordinate \(h_t(1)=e^t\). This is a concrete member of the enlarged Hardy graph outside its zero-coordinate slice.

In \(1/2<\Re s<1\), NHR3's exact original-zeta pairing, with inner product linear in its first argument, gives
\[
\langle h_k,\mathcal M_t\operatorname{ev}_s\rangle
=e^{ts^2}(1-k^{1-s})\frac{\zeta(s)}s.
\tag{NER9.2}
\]
The conjugated scalar in (NER9.1) loses its conjugation here because it multiplies the second inner-product argument. The cover factor cannot vanish in this strip, since \(|k^{1-s}|=k^{1-\Re s}>1\), and both \(e^{ts^2}\) and \(s\) are nonzero. Thus the evaluation image is orthogonal to all \(h_k\) exactly when original \(\zeta(s)=0\). Also \(h_t(s)=0\) exactly at the same zeros there, because every other complete factor in (NER1.2) is a holomorphic unit on this open strip. This checks the asserted equivalence and its exact domain, including why it does not extend unchanged through exceptional points.

For an actual nontrivial zero \(\rho\) and \(0\le j<m_\rho\), the derivative functional on \(E\) has boundary coordinate \(h_t^{(j)}(\rho)=0\). Its received coefficients are
\[
\overline{(g_t\phi_m)^{(j)}(\rho)}
=\overline{\sum_{a=0}^j\binom ja
g_t^{(a)}(\rho)\phi_m^{(j-a)}(\rho)}.
\tag{NER9.3}
\]
This retains all lower derivatives, binomial factors and original zero multiplicities. On the right-off-line branch it is the corresponding finite combination of actual Hardy jets; elsewhere this identity is an analytic disk receiver, with no additional Hardy membership claimed.

## NER10. Review outcome and directly relevant stronger consequences

The reviewed NPE construction is mathematically consistent in its stated coefficient category. The residue, cocycle, pushout topology, unique split section, endpoint matrix, transpose signs, all-source injectivity, closed Hardy graph, raw degree defect and original-zeta pairing pass this independent verification. No off-line-zero existence, RH, simplicity or missing purity was assumed.

Two directly relevant further consequences were proved in this review. NER4 identifies the endpoint Jordan representation as the actual nonsplit pushout along evaluation at zero. NER5 gives the exact equivariant topological isomorphism of the meromorphic middle space with the original entire source, while retaining the changed inclusion \(\mathcal B\xrightarrow{m_s}\mathcal B\), the endpoint quotient, both ideal maps and every transformed jet. Its two-jet quotient gives a direct algebraic realization of the displayed dual-number action. This examines the effect of the chosen source extension itself rather than varying a Gaussian parameter and assuming a new geometry.

These comparisons leave the mathematical scope exact: the full-ideal pushout splits uniquely, the endpoint-evaluation pushout does not split, and the Hardy receiver retains its unilateral projection defect. Neither pushout has been identified with Deligne's geometric lifting sequence, and no original lifting-vanishing or RH conclusion follows merely from the coefficient comparisons. The review supplies complete maps for the next source-geometric comparison without inserting that conclusion as a hypothesis.

## NER11. Final complete-ideal generation and the largest invariant slice

The final source adds NPE10 using the independently completed NCI0–8 proof in `NOOR_COVER_DISCREPANCIES_GENERATE_ORIGINAL_IDEAL.md`. That entire proof was read for this addition. Its exact theorem is
\[
\overline{\operatorname{span}\{\delta_{n,t}:n\ge2\}}^{\mathcal B}=I
\quad\text{for each fixed }t>0.
\tag{NER11.1}
\]
Here is the complete structure of its verification, retaining the analytic input on which its division step depends. NCI2 starts from the already established full Hadamard product
\[
F_0(s)=e^{a+bs}\prod_\rho(1-s/\rho)e^{s/\rho},\quad
e^a=1/8,\quad b=F_0'(0)/F_0(0),\quad
\sum_{|\rho|\le R}m_\rho\le C(R+2)^{3/2}.
\tag{NER11.2}
\]
The product repeats each zero through its full order. These exact product/growth inputs are those stated and sourced by NCI2.1; this review does not claim to reread their entire earlier S2 derivation. The new estimates following from them are independently checked as follows. Around all zeros of modulus at most \(8R\), use disks of radius \(R^{-2}\). Their total radii are \(O(R^{-1/2})\). Every connected disk cluster consequently has diameter less than one for sufficiently large \(R\). For \(R/2\le|s|\le3R\) outside those disks, each finite product factor satisfies \(|1-s/\rho|\ge(8R^3)^{-1}\); the sum of its logarithmic lower bounds is at least \(-CR^{3/2}\log R\). The retained finite exponential terms are bounded below by \(-3R\sum_{|\rho|\le8R}m_\rho/|\rho|\ge-CR^{3/2}\). Partial summation of the displayed count bounds the tail square sum by \(CR^{-1/2}\), and \(|s/\rho|\le3/8\) there gives \(\log|(1-w)e^w|\ge-8|w|^2/5\). The complete tail thus contributes at least \(-CR^{3/2}\). The leading exponential contributes at least \(-|a|-3|b|R\). These estimates prove the retained-product lower bound
\[
|F_0(s)|^{-1}\le \exp(CR^{3/2}\log R)
\tag{NER11.3}
\]
on the stated complement, with no suppression of a genus-one factor.

For \(F\in I\), its quotient \(H=F/F_0\) is entire because every required zero order was retained. On a fixed strip and a large annulus, the bound outside disk clusters follows from (NER11.3) and the source bound of \(F\). Within a cluster that meets the original strip, its boundary stays in the strip enlarged by one, and in the annulus enlarged from \([R,2R]\) to \([R/2,3R]\). The maximum principle on the entire quotient extends the boundary bound throughout that cluster. Its components are finite unions of disks; no smooth-boundary or simple-connectivity assumption is needed. This proves the fixed-height bound
\[
\sup_{|x|\le A}|H(x+iy)|
\le C_{A,F}\exp\{C(|y|+2)^{3/2}\log(|y|+2)\}.
\tag{NER11.4}
\]
Accordingly \(e^{\varepsilon s^2}F/F_0\in\mathcal B\) for every \(\varepsilon>0\), and multiplying it by the full \(F_0\) gives \(e^{\varepsilon s^2}F\to F\) in every original seminorm by the already proved Gaussian remainder estimate. Thus \(\overline{F_0\mathcal B}=I\). This is a closure statement. It is not an algebraic equality: \(F_0\in I\) cannot equal \(F_0G\) with \(G\in\mathcal B\), since that would force the forbidden constant function \(G=1\).

To check the generating family, let \(\Lambda\in\mathcal B'\) annihilate all \(\delta_{n,t}\), and set
\[
K_w(s)=R_t(s)\frac{e^w-e^{(1-s)w}}s,
\qquad L(w)=\Lambda(K_w).
\tag{NER11.5}
\]
Its removable value is \(K_w(0)=we^w\). The equivalent exact expression
\(K_w=we^wR_t\int_0^1e^{-\theta sw}\,d\theta\)
confirms that no pole is introduced. The same Gaussian strip and removable-division estimates used in NER7 make it an entire source family with \(|L(w)|\le Ce^{C(1+|w|^2)}\). It vanishes at every \(\log n\), since \(K_{\log n}=\delta_{n,t}\), with \(K_0=0\). Jensen's argument used in NER7 gives \(L=0\). The exact differentiated identity has the positive sign
\[
(\partial_w-1)K_w=8g_tF_0e^{(1-s)w}.
\tag{NER11.6}
\]
Therefore \(\Lambda(F_0g_te^{vs})=0\) for every \(v\in\mathbb C\). Multiplication by \(F_0\) is continuous on \(\mathcal B\), so apply the complete half-Mellin and parameter-continuation proof of NER7 to the functional \(F\mapsto\Lambda(F_0F)\). It vanishes on all of \(\mathcal B\). Thus the continuous annihilator of the discrepancy span equals that of \(F_0\mathcal B\), which equals \(I^\perp\) by the closure just proved. Hahn–Banach separation of closed subspaces now proves (NER11.1) in the original topology.

Define \(\sigma_t\Lambda=(\Lambda,0)\) in the actual dual coordinates (NER6.1). Every invariant linear subspace contained in \(\sigma_t\mathcal B'\) must satisfy, for each of its vectors, \(\Lambda(\delta_{n,t})=0\) for all \(n\ge2\), by the final coordinate of (NER6.2). Continuity and (NER11.1) therefore force \(\Lambda\in I^\perp\). Conversely \(U_nI\subset I\), so this annihilation is preserved under \(U_n'\), and the scalar coordinate stays zero by (NER6.2). Hence the largest such invariant subspace is exactly
\[
\boxed{\sigma_t(I^\perp).}
\tag{NER11.7}
\]
Intersecting with the Hardy graph gives exactly
\[
\boxed{\sigma_t(\mathfrak D_t^{\mathcal B}\cap I^\perp)
=\sigma_t(q'\mathfrak D_t^Q).}
\tag{NER11.8}
\]
The forward inclusion follows from (NER11.7) and the precise zero-coordinate slice identity. For the reverse inclusion, the entire extended Hardy graph is invariant by (NER6.4), while ideal annihilation ensures that every iterate stays in that slice. These two facts prove maximality by inclusion. They require no assertion of surjectivity from \(Q'\) to a Hardy space and no claim that its inverse-cover action preserves the Hilbert domain.

This verifies the final NPE10 exactly. The stable slice recovers the full original \(Q'\), with its full nontrivial-zero multiplicities, not just the further specialization dual. The separate boundary coefficient \(d_r(\rho)\), the original Weil pairing and the unilateral projection term in (NER8.2) have not been annihilated by this result.
