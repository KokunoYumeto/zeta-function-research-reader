# Endpoint restriction join: independent proof review

## Assignment and continuity

This is the review lane of `gamma_endpoint_window_bridge`, assigned on 13 September 2026. The parent owns publication and cumulative integration. This lane changes only files with its `endpoint_restriction_join_review_20260913` prefix. It does not edit the sealed arithmetic volume proof, the incoming source, or the primary join.

Assignment, verbatim:

> Independent mathematical review while I write standalone endpoint_restriction_join_20260913.tex. Full-read sealed work/arithmetic_volume_upper_route_20260913.tex and actual newNOTE at output/split_zero_rh_tandem_2026-09-12/sources/web_endpoint_restriction_delivery/Tau_Endpoint_Restriction_Control/NOTE.tex. Derive/review explicit actual gaps forpairs(q-1,2q-1),(q,2q). ProposedAU extension: Q_s=sum_{l=0}^s h_l x^(s-l) works any s>=0, so remcoefficient norm Bq=((1+r)/(1-r))^q holdsallN; C_N=U_k(T) A_N² Bq²/(T a_k(T)), source G_(q-1)<=C_N G_N, hence g0first1/C2q-1,second1/C2q; allactualoriginalS/mass preserved. Strongerfinite source comparator g=1/Tr((L_i)^-1 U_j), L_i=J_i (H_i^upper)^-1 J_i*, U_j=J_j (H_j^nu)^-1 J_j*, positivityprovesU_j<=Tr(...)L_i. Need full independence review, explicit finite errors trace certificates, exact relationship restriction vs EW Π_iΠ_j spectra, and caution about arbitraryN main estimates. Onlynew work/endpoint_restriction_join_review_20260913.{md,tex,py,json}. Do not editsealedfiles orprimarydraft; send concrete corrections/strongerresults early. No web needed for ouroriginalproofs, no checkerreplay handledintake. Then fullyreview mydraftonceavailable.

Complete reads: arithmetic volume source AU.1--AU.49 (including its benchmark and proof), SHA256 `21aaedc3585887fa7d2cb3e37e68d14415829a4b213566f7a08f4619835ef38b`; incoming restriction NOTE, every section and equation 1--65, SHA256 `ff4cc53cb4d3b10a9547a8a2365db7fd5d874bf1ecf7dd8542b8d1f05f433ef6`. The first batched output truncated; bounded disjoint follow-up reads covered both sources completely.

The complete EW projection section, EW.25--EW.28 including its proof, was also read at source SHA256 `e8d6152532c98532a062b5840834d934b28f29490ec926f47c2bce1af3493854`. This third read was scoped to the exact section being joined; it is not represented as a new full reading of all EW sections.

The inherited analytic envelope is used with its stated source proof and original constants. This review proves the finite comparison and transport consequences; it does not replay the checker or claim a new numerical enclosure of actual quartet data. An independent child reviews the trace-error calculation while this lane proves the polynomial and projection maps.

## 1. The arbitrary-degree remainder bound

Let q>=1, let chi_T(x)=product_(a=1)^q(x-z_a) be the exact transformed monic relation, and retain every root with its full multiplicity. Suppose |z_a|<=r<1. Write

\[
E(t)=\prod_a(1-z_at)=\sum_{a=0}^q(-1)^a e_at^a,
\qquad E(t)^{-1}=\sum_{l\ge0}h_lt^l.
\]

For every integer s>=0 define Q_s(x)=sum_(l=0)^s h_l x^(s-l). Multiplying the formal identity E(t)E(t)^(-1)=1 through order s proves that the coefficient of x^(q+s-a) in chi_T Q_s vanishes for 1<=a<=s, and its leading coefficient is one. Thus chi_T Q_s-x^(q+s) has degree at most q-1. This is exactly the monic quotient and remainder identity for every s>=0, with no restriction s<=q-1.

Coefficient convolution gives ||chi_T||_1<= (1+r)^q and ||Q_s||_1<=sum_(l=0)^s binom(q+l-1,l)r^l. Since the sole coefficient of chi_T Q_s at degree >=q is its leading coefficient one, its remaining coefficient norm is exactly ||chi_T Q_s||_1-1. Therefore

\[
\|\operatorname{rem}_{\chi_T}x^{q+s}\|_1
\le (1+r)^q\sum_{l=0}^s\binom{q+l-1}{l}r^l-1
\le \left(\frac{1+r}{1-r}\right)^q.
\]

The last inequality follows by summing q geometric series; it retains their original r and all q factors. For degrees below q the remainder has coefficient norm one. By linearity and the triangle inequality, ||rem_(chi_T) f||_1<=B_q(r)||f||_1 for every polynomial f, where B_q(r)=((1+r)/(1-r))^q. The r=0 case is included: high-degree remainders vanish and low-degree remainders retain norm one.

Use the exact original chart Psi_T P(x)=P(c+iTx), its inverse, and target measure T m_k(Tx)dx. Its mass is mu_h^k. The relation multiplication is Psi_T(chi Q)=(iT)^q chi_T Psi_T Q, with all raw derivatives multiplied by (iT)^d. Monic division commutes with this chart. The AU Legendre proof holds for every N>=0 and yields ||f||_1<=A_N||f||_(L2[-1,1]). The original arithmetic remainder has degree <=q-1, so the AU moment bound U_k(T) is independent of N. Hence for every N>=q-1,

\[
\|\operatorname{rem}_{\chi}P\|_{H_{q-1}^S}^2
\le C_N\|P\|_{H_N^S}^2,
\quad C_N=\frac{U_k(T)A_N^2 B_q(r)^2}{T a_k(T)}.
\]

Apply this to the actual least lift R_N x. Its remainder is the unique degree-below-q lift of x, so G_(q-1)<=C_N G_N. Degree inclusion gives G_N<=G_i<=G_(q-1) for q-1<=i<=N. Inversion on positive forms consequently gives

\[
C_N^{-1}K_N\preceq K_i\preceq K_N.
\]

Taking i=N forces C_N>=1. Thus the actual original pairs (q-1,2q-1) and (q,2q) have positive gaps C_(2q-1)^(-1) and C_(2q)^(-1), respectively. This proves concrete arithmetic inequalities from the stated analytic constants, with no unspecified gap substituted as an assumption. The extension of C_N to arbitrary N retains its exponential A_N; the AU central-degree asymptotic estimate is not automatically an arbitrary-N asymptotic estimate.

## 2. A strictly stronger trace comparator

Let L_i and U_j be positive forms in the same original quotient coordinates with

\[
0<L_i\preceq K_i\preceq K_j\preceq U_j.
\]

The actual source inequalities H_i<=H_i^upper and H_j^nu<=H_j give such forms by inversion and congruence:

\[
L_i=J_i(H_i^{upper})^{-1}J_i^*,\qquad
U_j=J_j(H_j^{nu})^{-1}J_j^*.
\]

Set tau=Tr(L_i^(-1)U_j). The Hermitian matrix L_i^(-1/2)U_jL_i^(-1/2) has q positive eigenvalues all at least one. Thus tau>=q, and each eigenvalue is at most tau-q+1 because its other q-1 eigenvalues contribute at least q-1. Conjugating back gives

\[
U_j\preceq(\tau-q+1)L_i,
\qquad K_i\succeq\frac{1}{\tau-q+1}K_j.
\]

This improves the proposed 1/tau bound while using the same finite data. For q=1 they coincide. The coefficient tau-q+1 is optimal from the facts A>=I and Tr A=tau alone: A=diag(tau-q+1,1,...,1) attains it. It remains a comparison coefficient for the original source; no eigenvalues of the arithmetic action are replaced by those of this positive matrix.

A certified upper rational tau_plus>=tau>=q gives the rational gap (tau_plus-q+1)^(-1). This preserves positivity and direction. An upper bound for tau alone does not enclose the positive trace moments of the actual restriction operator; those require their own complete finite enclosure below.

## 3. Exact map to the endpoint-window projections

Fix q-1<=i<=j and use the common original Hilbert space P_j with its original polynomial norm. Write ell_i=L_(i,j)R_i:E_i->P_j and ell_j=R_j:E_j->P_j, where E_a=(E,G_a). These are isometric embeddings. Let Pi_a be the orthogonal endomorphism projection of P_j onto ell_a E_a, and let P_(i,j) project onto the complete lower polynomial space P_i.

Every relation in D_i is also a relation in D_j, and R_j is orthogonal to D_j. Consequently P_(i,j)R_j is orthogonal to D_i and lies in P_i, hence lies in ell_i E_i. Direct calculation of its quotient coordinate in the original monic basis gives

\[
P_{i,j}\ell_j=\Pi_i\ell_j=\ell_i T_{i,j},
\qquad T_{i,j}=K_iG_j:E_j\longrightarrow E_i.
\]

The difference ell_i x-ell_j x is an original relation in D_j, so Pi_j ell_i=ell_j. Combining the identities proves the precise endomorphism similarities

\[
(\Pi_i\Pi_j)|_{\ell_i E_i}=\ell_i T_{i,j}\ell_i^{-1},
\qquad
(\Pi_j\Pi_i)|_{\ell_j E_j}=\ell_j T_{i,j}\ell_j^{-1}.
\]

Here each occurrence of T on the right is its underlying endomorphism on the displayed fixed vector space E, with the indicated source metric. Positivity of K_i and G_j makes its q eigenvalues g_a strictly positive. The full products on P_j have these eigenvalues and dim(P_j)-q zero eigenvalues. Indeed the range of Pi_i Pi_j is ell_i E_i, and its restriction there is invertible; its kernel is ker Pi_j, giving a direct sum decomposition. The corresponding assertion for Pi_j Pi_i follows by reversing the pair.

For completeness, choose an orthonormal eigenbasis x_a in E_i for T, with T x_a=g_a x_a, and set u_a=ell_i x_a and v_a=ell_j x_a/sqrt(g_a). Then u_a and v_a are individually orthonormal families and <u_a,v_b>=delta_ab sqrt(g_a). If g_a=1, u_a=v_a. If g_a<1, set w_a=(v_a-sqrt(g_a)u_a)/sqrt(1-g_a); the pairs (u_a,w_a) are mutually orthonormal. On their two-dimensional span,

\[
\Pi_i=\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad
\Pi_j=\begin{pmatrix}g_a&\sqrt{g_a(1-g_a)}\\
\sqrt{g_a(1-g_a)}&1-g_a\end{pmatrix}.
\]

Their difference has eigenvalues +/-sqrt(1-g_a). On the common orthogonal complement both projections vanish, and g_a=1 contributes zero. Thus for every integer m>=1 the exact trace morphism is

\[
\operatorname{Tr}_{P_j}|\Pi_i-\Pi_j|^{2m}
=2\sum_a(1-g_a)^m
=2\operatorname{Tr}_{E}(H_{i,j}^m),\qquad H_{i,j}=I-T_{i,j}.
\]

It also proves ||Pi_i-Pi_j||_1=2sum_a sqrt(1-g_a). The restriction loss and every positive trace certificate are therefore literal spectral observations of the same original endpoint-window projection pair. This constructs their relation on the full source and its original quotient, rather than only matching their determinant formulas.

## 4. Complete finite matrix errors and logarithmic certificates

Use positive definite rational Hermitian brackets, all in the original quotient coordinates,

\[
0<L_i\preceq K_i\preceq U_i,\qquad
0<L_j\preceq K_j\preceq U_j,\qquad K_i\preceq K_j.
\]

In particular L_i<=U_j. Put

\[
H_*=I-L_iU_j^{-1},\quad t_m^*=\operatorname{Tr}(H_*^m),\quad
d=\operatorname{Tr}(U_iL_j^{-1})-\operatorname{Tr}(L_iU_j^{-1}).
\]

All these are finite rational quantities. The eigenvalues of a positive pair (A,B) are those of B^(-1/2) A B^(-1/2). In increasing order, their a-th member obeys

\[
\lambda_a(A,B)=\min_{\dim W=a}\ \max_{0\ne x\in W}
\frac{x^*Ax}{x^*Bx}.
\]

To prove this formula first take B=I and choose an orthonormal eigenbasis for A. The span of the first a eigenvectors attains the indicated maximum lambda_a. Every a-dimensional W intersects the span of eigenvectors numbered a,...,q, since the two dimensions sum to q+1. A nonzero vector in that intersection has Rayleigh quotient at least lambda_a. This proves both inequalities. The invertible map x=B^(-1/2)y proves the general case and preserves subspace dimensions.

For every nonzero x, the inequalities for numerator and denominator give

\[
\frac{x^*L_ix}{x^*U_jx}\le
\frac{x^*K_ix}{x^*K_jx}\le
\frac{x^*U_ix}{x^*L_jx}.
\]

Taking the displayed extrema proves the ordered generalized-eigenvalue inequalities. Write alpha_a=lambda_a(L_i,U_j) and beta_a=lambda_a(K_i,K_j). Then 0<alpha_a<=beta_a<=1, because L_i<=U_j and K_i<=K_j. The trace identity sum lambda_a(A,B)=Tr(AB^(-1)) follows by similarity to the Hermitian matrix. Taking sums of the two extremal inequalities proves

\[
0\le\sum_a(\beta_a-\alpha_a)\le d.
\]

Choose the explicit reference gap

\[
g=\frac{1}{\operatorname{Tr}(L_i^{-1}U_j)-q+1},\qquad r=1-g.
\]

Section 2 proves 0<g<=alpha_a<=beta_a<=1. A larger certified reference gap may also be obtained directly by a positive-semidefinite certificate for L_i-gU_j; its same proof replaces g throughout. If r=0, every alpha_a=beta_a=1, H_actual=H_*=0, and all losses vanish. Suppose 0<r<1. Since the derivative of x^m on [0,r] is bounded by m r^(m-1), integration of that derivative gives, for m>=1,

\[
0\le (1-\alpha_a)^m-(1-\beta_a)^m
\le m r^{m-1}(\beta_a-\alpha_a).
\]

Taking sums yields the complete rational moment enclosure

\[
a_m:=\max\{0,t_m^*-mr^{m-1}d\}
\le s_m:=\operatorname{Tr}(H_{i,j}^m)\le t_m^*\le q r^m.
\]

The upper matrix in this proof is the reference pair L_i,U_j. It is important that the gap g is certified for this pair: a sharper gap known only for the actual pair need not bound alpha_a and cannot be inserted in the error factor r without a further reference-pair certificate.

The scalar identity -log(1-x)=sum_(m>=1)x^m/m on 0<=x<1 follows by integrating the convergent geometric series on [0,x]; its terms are nonnegative. With L=log(V_i/V_j), taking the finite eigenvalue sum gives L=sum_(m>=1)s_m/m. The remaining tail satisfies

\[
\sum_{m=p+1}^\infty\frac{x^m}{m}
\le\frac{x^{p+1}}{(p+1)(1-x)}
\le\frac{x^{p+1}}{(p+1)g}\qquad(0\le x\le r).
\]

Therefore the entirely rational certificate, for every integer p>=1, is

\[
\sum_{m=1}^p\frac{a_m}{m}\le L\le
\sum_{m=1}^p\frac{t_m^*}{m}+
\frac{t_{p+1}^*}{(p+1)g}.
\]

The width of these two displayed endpoints is at most

\[
\frac{d(1-r^p)}{g}+\frac{q r^{p+1}}{(p+1)g}.
\]

Indeed t_m^*-a_m<=m r^(m-1)d, and sum_(m=1)^p r^(m-1)=(1-r^p)/g. The final tail uses t_(p+1)^*<=q r^(p+1). This bounds the finite matrix error and the positive series tail separately with their literal constants.

The incoming NOTE's sharper coefficient is

\[
c_p(r)=\sum_{l=0}^\infty\frac{r^l}{p+1+l}
=\frac{-\log g-\sum_{m=1}^pr^m/m}{r^{p+1}}
\le\frac{1}{(p+1)g}.
\]

Since x^(p+1) sum_(l>=0) x^l/(p+1+l)<=c_p(r)x^(p+1), replacing 1/((p+1)g) in the upper endpoint by c_p(r) preserves its proof and improves it. To enclose c_p rationally, enclose log g. For a positive rational x write exactly x=2^e y, with integer e and 1<=y<2, and set t=(y-1)/(y+1). Then 0<=t<1/3 and integration of 2/(1-t^2) gives

\[
\log y=2\sum_{a=0}^{M-1}\frac{t^{2a+1}}{2a+1}+E_M,
\quad 0\le E_M\le\frac{2t^{2M+1}}{(2M+1)(1-t^2)}.
\]

The same formula at t=1/3 gives an enclosure of log 2. Multiplying its interval by e reverses its endpoints when e<0; adding the log y interval then encloses log x. In particular an enclosure log g in [ell_minus,ell_plus] of width epsilon gives

\[
c_p(r)\le c_p^+(r):=
\frac{-\ell_- -\sum_{m=1}^pr^m/m}{r^{p+1}}.
\]

The extra upper error is at most epsilon t_(p+1)^*/r^(p+1)<=q epsilon. All signs, powers, and the original dimension remain in this bound. The r=0 case is already exact and does not divide by r.

For a fixed admitted pair, suppose certified brackets shrink entrywise to their actual positive matrices. Matrix inversion is continuous there, as follows directly from the cofactor formula and a determinant bounded away from zero. Thus d tends to zero. Also Tr(L_i^(-1)U_j)-q+1 tends to a finite positive number at least one, so the reference gaps remain bounded away from zero. Given any positive target width, first make d/g sufficiently small and then increase p to make the displayed geometric tail small; the logarithmic enclosure can be refined independently. This proves convergence for the fixed original pair with its actual matrices. It gives no uniform growing-degree estimate without controlling those explicit quantities as the degree grows.

For coefficient or source errors, the required brackets are concrete images of source brackets. If 0<H_N^-<=H_N<=H_N^+ with the actual quotient map J_N, inversion and congruence give

\[
J_N(H_N^+)^{-1}J_N^*\preceq K_N\preceq
J_N(H_N^-)^{-1}J_N^*.
\]

Their positivity follows from surjectivity of J_N. If coefficients of the actual relation also require enclosure, they must enter these same quotient maps, or one must first use the exact quotient-first triangular basis [1,S,...,S^(q-1),chi,S chi,...] and enclose its transformed Gram. Replacing the actual chi by a rounded polynomial would instead change J_N and does not prove these inequalities for the requested object.

## 5. Explicit growth of the extended scalar bound

The exact formula for A_N gives, for q>=1,

\[
\frac{C_{2q}}{C_{2q-1}}
=\frac{4q+1}{4q-1}
\left(\frac{4^{2q+1}-1}{4^{2q}-1}\right)^2
\le\frac53\left(\frac{21}{5}\right)^2
=\frac{147}{5}<32.
\]

Here (4q+1)/(4q-1)=1+2/(4q-1)<=5/3 and
(4^(2q+1)-1)/(4^(2q)-1)=4+3/(4^(2q)-1)<=21/5. The original two determinant losses each have q eigenvalues and are bounded by q log of their respective comparison constants. Hence, with the exact AU.31 function mathcal U_k,

\[
\mathcal B_{h,k}\le q\log C_{2q-1}+q\log C_{2q}
\le2\mathcal U_k+q\log32.
\]

This bounds the actual four-volume quantity. Its explicit right side has leading term 2(alpha D+log256)q^2. Using q=[1+k(m-1)](k+1)^2 shows that its ratio to q log k grows; this displayed scalar majorant does not establish a competing upper bound at the endpoint's q log k scale. It remains an actual all-finite-degree certificate, and the full matrix comparator retains more directional information.

## 6. Empty packet and declared comparison domain

The inverse and positive-gap calculations in this review all have q>=1. The actual quartet application has q=[1+k(m-1)](k+1)^2 and k>=3, so this domain is satisfied. For the empty packet h=1, the arithmetic quotient is zero and its quotient volumes are empty determinants one. Both loss operators and both projection differences are zero; all trace sums and the four-volume loss vanish. No q-by-q positive inverse or expression 1/(tau-q+1) is introduced to manufacture a rank in this case. The original analytic density and its mass remain present in the source.

## 7. Constructing rational source and quotient brackets

This supplies the finite algebra behind the entry-enclosure interface in Section 4. Suppose a Hermitian source matrix M has a rational Hermitian center M_0 and symmetric nonnegative rational radii epsilon_ab with |(M-M_0)_ab|<=epsilon_ab. For any positive rational weights w_a define the diagonal rational matrix

\[
\Delta_{aa}=\sum_b\epsilon_{ab}\frac{w_b}{w_a}.
\]

The inequality 2xy<=t x^2+t^(-1)y^2, obtained by squaring sqrt(t)x-y/sqrt(t), gives

\[
\begin{split}
|z^*(M-M_0)z|
&\le\sum_{a,b}\epsilon_{ab}|z_a||z_b|\\
&\le\frac12\sum_{a,b}\epsilon_{ab}
\left(\frac{w_b}{w_a}|z_a|^2+
\frac{w_a}{w_b}|z_b|^2\right)
=z^*\Delta z.
\end{split}
\]

Thus M_0-Delta<=M<=M_0+Delta. Every quantity in the two comparison matrices is rational. Positive definiteness of the lower matrix is checked by exact Hermitian elimination: split off a positive first pivot d, and the triangular congruence eliminates its off-diagonal row and column leaving its Schur complement. The identity of quadratic forms is d|x+d^(-1)b^*y|^2+y^*(C-bb^*/d)y. Induction proves that positive successive pivots imply positivity, and conversely positivity forces each pivot and Schur complement positive. This describes the exact certificate, not a report that an unprovided numerical matrix has passed it.

When the actual relation chi has nonrational coefficients, use the exact polynomial coefficient matrix

\[
\mathcal A_N=[1,S,\ldots,S^{q-1},\chi,S\chi,\ldots,S^{N-q}\chi]
:\mathbb C^q\oplus\mathbb C^{N-q+1}\longrightarrow\mathcal P_N.
\]

For N=q-1, the relation block in this list is empty and its coefficient summand is C^0; the matrix then consists of the first q monomials alone. For every N>=q-1 the displayed matrix is triangular with diagonal one because chi is monic, hence invertible. Monic division gives J_N mathcal A_N=[I_q,0]. Its exact transformed source is M_N=mathcal A_N^*H_N mathcal A_N. In this coordinate system the original quotient kernel therefore has the exact expression

\[
K_N=[I_q,0]\,M_N^{-1}\,[I_q,0]^*.
\]

Certified intervals for the original source entries and the original coefficients of chi give intervals for M_N by its literal finite matrix products; interval addition, multiplication, and conjugation contain their actual results. A rational complex radius is obtained by summing the real and imaginary radii. Choose conjugate center entries and symmetric enlarged radii, apply the preceding Delta construction, and test its lower positive pivots. The two rational inverse compressions with [I_q,0] then give the L_N,U_N of Section 4. Their positivity follows because the coordinate projection is onto: for nonzero x, [I_q,0]^*x is nonzero and the positive inverse quadratic form on it is strictly positive.

This construction uses the actual basis mathcal A_N to prove the identities even when only intervals for its entries are numerical inputs. It does not replace chi by a rational center polynomial. The arithmetic quotient coordinates remain exactly its original ordered remainder coefficients, and every source entry still contains its original mass and phase. With the degree and positive rational weights fixed, entry refinement makes Delta tend to zero. Since the actual M_N is positive, positive lower pivots eventually exist; the finite matrix-error certificates then converge by the proof in Section 4.

## 8. The balanced product forces a small return in both endpoint pairs

For the primary draft's additional EP integration, the source definitions and radius/product proofs EP.1--14 and the entire arithmetic section EP.39--50f were read, including all phase/contraction penalties and the balanced norm constant. These were targeted reads, not a new full reading of the entire EP article.

Write q=[1+k(m-1)](k+1)^2, k>=3, and retain the original positive quartet lower radius

\[
L_{h,k}=2\delta[1+k(m-1)](k+1)
\left\lfloor\frac{(k+1)^2}{4}\right\rfloor,
\qquad L_{h,k}/q\ge\delta k/2.
\]

The balanced EP product gives, for the actual central pair (q,2q-1),

\[
C_{mid}=\log(V_q/V_{2q-1})
\ge2(q-1)\log\frac{L_{h,k}}{C_h^{bal}q}+P_{mid},
\]

where its complete original penalty is

\[
\begin{split}
P_{mid}={}&-\log(1-d_0)-\log(1-d_{q-1})
-2\sum_{a=1}^{q-2}\log(1-d_a)\\
&+\sum_{a=0}^{q-2}\log(1+\phi_{q+a}^2/L_{h,k}^2),
\qquad d_a=V_{q+a}/V_{q+a-1}.
\end{split}
\]

Every d_a is in (0,1): positivity gives its lower bound, while the positive radius L_(h,k) and the exact radius identity EP.11 exclude d_a=1. Thus all displayed terms are well-defined and nonnegative. The balanced norm bound and its literal constant C_h^bal are the stated analytic input of EP.50a--50b; this review adds the exact spectral consequence to that already proved product, not a replacement analytic estimate.

Kernel addition in the original monic basis gives

\[
K_{2q-1}-K_q=\sum_{a=q+1}^{2q-1}\frac{b_ab_a^*}{\omega_a},
\qquad \operatorname{rank}(K_{2q-1}-K_q)\le q-1.
\]

Consequently the positive Hermitian representative of T_(q,2q-1) differs from the identity by a matrix of rank at most q-1. It has at least one exact eigenvalue one. List the other q-1 eigenvalues as gamma_1,...,gamma_(q-1), retaining any additional ones in this list. Their product is exp(-C_mid). If gamma_min is their minimum, then gamma_min^(q-1)<=product gamma_a, so

\[
\gamma_{min}\le
\left(\frac{C_h^{bal}q}{L_{h,k}}\right)^2
\exp\!\left(-\frac{P_{mid}}{q-1}\right).
\]

Since K_(q-1)<=K_q, the Rayleigh quotient for (K_(q-1),K_(2q-1)) is at most that for (K_q,K_(2q-1)) on every nonzero vector. Since K_(2q)>=K_(2q-1), the same is true for (K_q,K_(2q)) compared with the central pair. Taking the minimum Rayleigh quotient shows that the minimum return eigenvalue in each of the two original endpoint pairs is at most gamma_min. Each pair therefore has a positive return eigenvalue at most

\[
\min\left\{1,
\left(\frac{C_h^{bal}q}{L_{h,k}}\right)^2
e^{-P_{mid}/(q-1)}\right\}
\le\min\left\{1,\frac{4(C_h^{bal})^2}{\delta^2k^2}\right\}.
\]

The projection bridge in Section 3 turns each such eigenvector into its original higher-degree minimum representative whose lower-degree portion has squared norm ratio equal to that eigenvalue. The complementary portion has the remaining squared norm ratio. Its old coordinate is T x, and recovering the exact original coordinate x uses the invertible T, with the difference of complete representatives in the original relation space.

Finally the exact positive decomposition of the original four-volume loss is

\[
\mathcal B_{h,k}=2C_{mid}
+\log(V_{q-1}/V_q)+\log(V_{2q-1}/V_{2q}).
\]

Both endpoint terms are nonnegative. Substitution gives the full finite lower bound 4(q-1)log(L_(h,k)/(C_h^bal q))+2P_mid plus the two displayed endpoint terms. Since L_(h,k)/q>=delta k/2, division by q log k and (q-1)/q->1 prove the lower asymptotic threshold four. This retains the complete finite penalty formula before taking its consequence. It does not change the scalar upper estimate in Section 5 into one with a smaller asymptotic order.

## Pending primary-draft review

All derivations above have been sent to the parent as concrete integration input. The primary join draft is not yet present on disk. This lane has not run numerical fixture tests; the independent source replay belongs to the separate intake lane.

The independent `trace_error_audit` lane separately derived the full gap and trace-error results, then read Sections 2 and 4 of this actual Markdown at SHA256 `3292e1c6aaef9b40b27c49f1cac986832583c5cbdd18892802489c96c2c720d8`. It found no mathematical or textual error. Its scope included the q=1 boundary, ordered generalized-eigenvalue proof, trace error direction, reference-gap requirement, both width terms, every coefficient and power in c_p, the negative binary-exponent sign in rational logarithm bounds, the q times logarithm-error bound, fixed-pair convergence, and the actual quotient-map/source-bracket paragraph. This paragraph records that completed cross-review and changes no reviewed mathematical statement.

The same independent lane read the complete newly added Section 7 at SHA256 `94d3fb8c6c47b93700ffcd64f02af2ef7a38f04ae1e654fc29c19c4eb262f696`. It verified every formula and requested two explicit boundary clarifications: the relation block at N=q-1 is empty, and positive rational weights are held fixed during refinement. Both clarifications are now present above. It found no other issue.
