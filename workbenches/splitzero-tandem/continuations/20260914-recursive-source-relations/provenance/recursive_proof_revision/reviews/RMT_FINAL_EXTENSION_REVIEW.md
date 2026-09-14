# Independent final review of RMT1–RMT22 and the incoming signed control

Date: 13 September 2026.

RMT status: accepted at SHA-256 **236ec474c8f82e7f8ba0f3cde278f814d986a52de912d9a59c79208291cc9dd8**. The complete final root source was read, including RMT10a, RMT10b, both five-entry minima, the complete positivity and angle argument, and the new RMT19–RMT22 construction. No source edit was made by this reviewer. The previous RMT_REVIEW.md and RMT_ANGLE_SUBREVIEW.md remain unchanged as receipts for the earlier three-bound source.

The incoming ISM source was read completely twice, including its final two-leg coefficient-carrier addition, at SHA-256 **c1586e0c88a35df242ddd139c047b2ea9d2b17dff3b3a745d041e2912f4a3baf**. ISM1–ISM41 and the full complex-kernel formula ISM42 are accepted. The single-coordinate specialization ISM43 needs the coordinate typing repair described below before the entire ISM body can receive final acceptance. This does not affect RMT, whose ISM dependence is ISM14–ISM37.

Complete supporting source bodies read in this review:

- output/Deligne_Mixed_Control_Continuation_2026-09-13/sources/AW.tex, SHA-256 c79e76c087efd59871e3234ff44fb18964515dbd34f0318dffba6b3f1440f6ec.
- output/Deligne_Mixed_Control_Continuation_2026-09-13/sources/SP.tex, SHA-256 180cd8a83a59e692fc0fa16a6622794927360df42317dc9d0ec3bdd6dbd7cd1a.
- work/cumulative_addendum_20260913_v22/portable_g0ijpdcf/Tau_Actual_Source_and_Metric_Addendum_2026-09-13/proofs/EP.tex, SHA-256 1ba57290c995abcaa57840c5a873e767174b21bc5b19525df004f58c0bca1448.

The companion ISM_FINAL_INDEPENDENT_REVIEW.md records a separately delegated full ISM check. This review asserts written mathematical verification. It does not assert a new numerical moment evaluation, quadrature certificate, Lean compilation, or PDF layout check.

## 1. Exact common source, sections and signs

The common space is H=P_{2q}, with the original ascending monomials in S=k/2+iy. The densities, g=2xi, h, tensor order k, cyclic polynomial chi, and all original masses stay fixed. The reference identity

\[
r_{1/4}^{*k}=\frac{c_{1/4}^{\,k}}{c_{k/4}}r_{k/4},
\qquad c_a=2^{1-2a}\Gamma(2a),\qquad
c_{1/4}=\sqrt{2\pi}
\]

agrees literally with AW3 and EP3. No source rescaling is implicit in the metric comparisons.

For each of the four degrees, B_N is injective on its nonzero relation domain by monic polynomial division. Its padded matrix is exactly I_N B_N^{AW}. Thus the expressions for the source projection P_N and relation projection Q_N in RMT5 coincide with the AW/SP maps on H, with no changed codomain or adjoint convention. At N=q−1 the relation domain is zero and Q_{q−1}=0.

The canonical section rho_N=C−B_N(B_N^*M B_N)^{-1}B_N^*M C has remainder identity and relation orthogonality. These two facts show

\[
\mathcal P_N=\rho_NE\mathbin{\perp_M}\operatorname{ran}B_N,
\qquad
\Pi_N=\rho_NG_N^{-1}\rho_N^*M=P_N-Q_N.
\]

The inverse of rho_N onto its range is the remainder map restricted to that range. This establishes an identity of operators and an exact range isomorphism, rather than only a trace identity.

Differentiating the remainder identity and relation orthogonality gives the ISM18 formula for rho_N'; both derivative cross terms in G_N' vanish. Jacobi differentiation then gives

\[
(\log V_N)'=\operatorname{Tr}(C_x\Pi_N).
\]

Adding the four original signs proves

\[
\mathcal A_x=\Pi_{q-1}+\Pi_q-\Pi_{2q-1}-\Pi_{2q}
             =U_x-W_x,\qquad
\mathcal B'=\operatorname{Tr}(C_x\mathcal A_x).
\]

This verifies RMT6–RMT7 and the ISM-to-RMT correspondence. The density map is v A M^{-1}v^*, with the inverse metric on the written side. Integration against the original signed measure gives exactly the same derivative. Cyclicity of trace is sufficient throughout; none of U,W,C is assumed to commute with the other two.

## 2. The full spectrum, exact trace norm and centered square

D=M_0^{-1}M_1 is positive self-adjoint in M_0 because M_0D=M_1. Factoring M_x=M_0((1−x)I+xD) gives

\[
C_x=((1-x)I+xD)^{-1}(D-I).
\]

Its eigenvalues are c_j=(b_j−1)/(1−x+xb_j). Their b-derivative is (1−x+xb_j)^{-2}>0, so their order is the original order of all b_j. Every denominator is positive, including at both endpoints. Integrating c_j gives log b_j, and integrating their width d_x gives log kappa.

The original relation flag has dimensions 1,q,q+1. On its consecutive orthogonal pieces, U acts by 1,2,1,0 with dimensions 1,q−1,1,q. The source flag gives W the same eigenvalue list 0^[q],1^[2],2^[q−1]. Thus both have rank q+1, trace 2q and trace square 4q−2. Their decomposition into spectral projections of ranks q+1 and q−1 gives, by the complete AW projection-trace proof,

\[
|\mathcal B'|
\le E_q=c_{q+2}-c_q+
2\sum_{j=1}^{q-1}(c_{2q+2-j}-c_j).
\]

The full c_{q+1} contributions cancel only after the upper and lower sums are formed. Integrating every displayed summand gives RMT15, including the coefficient 1+2(q−1)=2q−1.

Set A=U−W. Then Tr A=0 and

\[
\operatorname{Tr}(A^2)=8q-4-2\operatorname{Tr}(UW)\ge0.
\]

The square is inside the trace; the final source states this unambiguously. Let P_L be the original metric projection onto the intersection of the two ranges, of dimension s. Since the nonzero spectra of U,W are at least one, both dominate P_L. Consequently U−P_L,W−P_L are positive with trace 2q−s. Their difference is A, and therefore

\[
\|A\|_1\le4q-2s,\qquad
\|A\|_1\le\sqrt{(2q+1)\operatorname{Tr}(A^2)}.
\]

The second inequality is Cauchy–Schwarz on all real eigenvalues of A. Center C at the midpoint of its spectral interval. Each diagonal Rayleigh quotient of that centered operator has absolute value at most d_x/2 in an M_x-orthonormal eigenbasis of A. Multiplication by each absolute eigenvalue and summation proves

\[
|\mathcal B'|\le T_q:=\frac{d_x}{2}\|A\|_1\le O_q.
\]

This checks the direction of both inequalities in RMT10a. O_q remains a retained majorant of T_q, even though it cannot improve a pointwise minimum which already includes the exact T_q. Retaining both expressions preserves their distinct calculated data.

For RMT10b, M_xC_x=dot M=dot M^* proves M_x-self-adjointness. The map L↦M_x^{1/2}LM_x^{-1/2} is an algebra isomorphism on End(H), sends this self-adjoint subspace to Hermitian matrices, and preserves trace and products. Therefore

\[
\Sigma_x=\operatorname{Tr}(C_x^2)
 -\frac{(\operatorname{Tr}C_x)^2}{2q+1}
=\left\|C_x-\frac{\operatorname{Tr}C_x}{2q+1}I\right\|_{\rm HS,M_x}^2.
\]

Using Tr A=0 and Hilbert–Schmidt Cauchy–Schwarz proves

\[
|\mathcal B'|\le
\sqrt{\Sigma_x\operatorname{Tr}(A^2)}=S_q.
\]

Every quantity here is real. The original metric is used in both factors. No positivity of C_x or pairwise commutation has been introduced.

## 3. Full angle lists and strict actual-moment positivity

For i≤j, canonical orthogonality gives rho_j=Pi_j rho_i, the cross Gram rho_i^*M rho_j=G_j and

\[
G_i-G_j=(\rho_i-\rho_j)^*M(\rho_i-\rho_j)\succeq0.
\]

The isometric frames rho_iG_i^{-1/2} and rho_jG_j^{-1/2} have squared cross singular values equal to the eigenvalues of G_i^{-1/2}G_jG_i^{-1/2}. They are in (0,1], so each full list has q angles in [0,pi/2). A unit cross singular value is exactly a common vector of the two minimum spaces. Each nonzero angle theta gives the signed two-dimensional projection-difference block with eigenvalues plus and minus sin theta; its trace pairing with C has absolute value at most d sin theta.

The crossed pairs are (q−1,2q) and (q,2q−1). Both q-dimensional minimum spaces of the second pair lie in P_{2q−1} intersected with the orthogonal complement of the nonzero relation line chi P_0, a space of dimension 2q−1. Hence a common vector exists and one angle phi_1 is zero. Both full q-entry geometric lists remain present. RMT's scalar list contains the q theta costs and the q−1 phi costs with indices 2 through q, with phi_1 explicitly displayed separately as zero. Every additional zero stays in that scalar list. Thus

\[
\mathcal B=0+\sum_{\nu=1}^{2q-1}\lambda_\nu
\]

exactly. The second derivative of f(z)=sqrt(1−e^{-z}) is

\[
f''(z)=-\frac{e^{-z}(2-e^{-z})}{4(1-e^{-z})^{3/2}}<0
\quad(z>0).
\]

Continuity extends concavity to zero. Jensen on the retained 2q−1 slots proves RMT11 with a=2q−1. This agrees with EP's inherited general-window method and its precise crossed-count refinement; it does not give that method new priority.

The actual positive moment path yields strict B>0. If B=0, each crossed determinant ratio is one. Since its relative positive Gram eigenvalues are at least one, all equal one and the two section maps coincide. In particular rho_{q−1}=rho_{2q} puts the original constant 1 in the space orthogonal to chi P_q. The original line has conjugate S=k−S, and

\[
\chi^{\#_k}(S)=\sum_j\overline{a_j}(k-S)^j
\]

belongs to P_q and equals conjugate chi(S) on that line. Orthogonality would force the positive squared norm of the nonzero chi to vanish:

\[
0=\langle1,\chi\chi^{\#_k}\rangle
=\int|\chi(S)|^2d\mu_x>0.
\]

The argument covers positive atomic moment measures with the retained positive P_{2q} Gram because the same identity holds at each atom. It does not assign this moment identity to an arbitrary positive coefficient matrix.

## 4. Both five-entry minima and the nonlinear interval

All five nonnegative bounds E,T,O,S,A bound the same |B'|. On the actual moment path,

\[
z_x=a\sqrt{1-e^{-\mathcal B(x)/a}}>0.
\]

The quotient Grams, projections, B, and all spectral functions except the integer intersection dimension are continuous. The formula s_x=2(q+1)−rank[U_x W_x] makes s_x Borel: each rank superlevel set is a finite union of nonvanishing-minor sets. Thus all the minimum integrands are measurable. Strict positivity and compactness give a positive lower bound for z_x on this fixed path; every denominator in I_q is legitimate and all integrands are bounded.

Let m(x)=min{E_q,T_q,O_q,S_q,A_q}. Then J_q=int m bounds |B_1−B_0|. Since a finite minimum is no larger than any of its entries, J_q is bounded by every integral in RMT14. This proves the enlarged five-entry formula without replacing any source quantity.

For H_a(B)=2 arcosh(exp(B/(2a))) on B>0, differentiating its defining cosh identity gives H_a'(B)=1/z. Both inverse composites equal the identity for K_a(v)=2a log cosh(v/2), with continuous value zero at zero. Therefore

\[
|(H_a\circ B)'|\le m(x)/z_x
=\min\{d_x,E_q/z_x,T_q/z_x,O_q/z_x,S_q/z_x\}.
\]

Integration proves RMT17 and I_q≤int d_x=log kappa. Applying the increasing inverse K_a to the interval for H_a(B_1), and intersecting with the additive J_q interval, proves every lower and upper entry of RMT18.

For q=1 the second crossed pair is (1,1), its full angle is zero, a=1, the spectral sums are empty, and E_1=d_x. For M_1=cM_0 with c>0, every eigenvalue of C_x coincides. Thus d,E,T,O,S,A,I,J all vanish; each quotient determinant scales by (1−x+xc)^q and the four powers cancel. The final scalar paragraph lists the new T and S explicitly, and returns B_1=B_0 without a zero denominator.

## 5. Complete signed finite construction and residual

RMT19 uses B_x^circ=(1−x)I+xD and the positive scalar alpha_x=(lambda_min(B_x^circ)+lambda_max(B_x^circ))/2. It is ISM29's a_x, without collision with the angle count a. H_x^circ=I−B_x^circ/alpha_x has eigenvalues

\[
\zeta_j(x)=1-\frac{1-x+xb_j}{\alpha_x}.
\]

The extreme values are opposite and their absolute value is

\[
\frac{x(b_n-b_1)}{2(1-x)+x(b_1+b_n)}
\le\vartheta=\frac{b_n-b_1}{b_n+b_1}<1.
\]

The derivative of the left side in x is 2(b_n−b_1)/(2(1−x)+x(b_1+b_n))^2≥0, proving the bound on the complete closed interval. All eigenvectors may be taken M_0-orthogonal, and remain M_x-orthogonal because B_x^circ acts on each by the positive scalar 1−x+xb_j. This establishes self-adjointness of every real function of D in both metrics.

The finite geometric-sum identity gives exactly

\[
C_x-C_x^{[L]}=(H_x^\circ)^{L+1}C_x=R_x^{[L]},
\qquad
E_x^{[L]}=R_x^{[L]}-
\frac{\operatorname{Tr}R_x^{[L]}}nI.
\]

No convergence argument is needed to obtain this finite equality. The residual's full eigenvalues are delta_j=zeta_j^{L+1}c_j. Centering therefore gives the exact square

\[
\operatorname{Tr}((E_x^{[L]})^2)
=\sum_j\delta_j^2-\frac{(\sum_j\delta_j)^2}{n}
\le\vartheta^{2L+2}K_D,
\quad
K_D=\sum_j\left(\frac{|b_j-1|}{\min(1,b_j)}\right)^2.
\]

The final inequality uses 1−x+xb_j≥min(1,b_j) for each retained eigenvalue. All constants are finite at the original fixed endpoint forms.

Both U,W dominate their range projections. Those ranges have a common vector, so the trace product of the range projections is at least one, by summing squared projection lengths in an orthonormal basis of the first range. Positivity of product traces then gives Tr(UW)≥1 and

\[
\operatorname{Tr}((U-W)^2)\le8q-6.
\]

Since Tr(U−W)=0, the trace-mean part of R makes no contribution to the derivative, giving the signed identity

\[
\mathcal B'=\operatorname{Tr}(C_x^{[L]}(U-W))
             +\operatorname{Tr}(E_x^{[L]}(U-W)).
\]

Both factors in the second trace are self-adjoint in the same original metric. Hilbert–Schmidt Cauchy–Schwarz, followed by integration, gives exactly

\[
j_L-e_L\le\mathcal B(1)-\mathcal B(0)\le j_L+e_L,
\qquad
0\le e_L\le\vartheta^{L+1}\sqrt{K_D(8q-6)}\longrightarrow0.
\]

This verifies the signs, square-root factor and exponent L+1 of RMT20–RMT21. The center keeps the actual signed correlation. The displayed integrals are exact quantities; a numerical approximation to j_L would additionally require its quadrature error. The source states this limitation explicitly and makes no uncomputed numerical claim.

Each of the four lower entries in RMT22 is separately at most the actual B_1, and each of its three upper entries is separately at least B_1. Taking their maximum and minimum therefore preserves a nonempty interval. In the scalar case H_x^circ and E vanish, C_x^[L] is scalar, and its pairing with U−W has trace zero, so j_L=e_L=0. The interval returns the unchanged value. This proves RMT22 at all admitted q, L and fixed endpoint forms.

## 6. Incoming source secants, full primitive and the coordinate repair

ISM7's two squared boundary terms have the correct signs. Indeed rho_1=rho_0+Delta and the canonical cross terms vanish in M_0, giving rho_1^*M_0rho_1=G_0+Delta^*M_0Delta. Similarly rho_0^*M_1rho_0=G_1+Delta^*M_1Delta. Substitution proves both scaled secants exactly. Positive source order then descends to the four quotient Grams. The four log inequalities give the supplied 2q coefficient, and the AW/SP common-source spectrum refines it to 2q−1.

For nested sections, the same cross-Gram identity gives Tr(Pi_iPi_j)=Tr(G_i^{-1}G_j), and Tr((Pi_i−Pi_j)^2)=2Tr(I−G_i^{-1}G_j). ISM23 expands the sum of two signed differences with its actual cross term 2Tr(A_0A_1), without replacing its sign by an assumption. The Hilbert–Schmidt triangle inequality gives the coarser 4(ell_0+ell_1) majorant while preserving the exact expression. These identities establish all incoming metric inputs used above.

The multivariate division in ISM38–ISM39 is valid over the polynomial ring in the other variables because each h(s_i) is monic. Successive division preserves every earlier degree restriction. The final remainder lies in the tensor monomial basis, and its zero class forces that remainder to be zero. In the degree k−1 primitive, there are exactly i−1 preceding degree-one factors, so the displayed coefficient (−1)^{i−1} cancels the tensor differential's same sign. Degree-zero D operators commute with that differential. This proves dK_v=V((rho_1−rho_0)v) with the original full relations.

The final two-leg maps have types j_±:[V→B]→[V⊕Vhat→B] and p in the reverse direction. Their degree-one maps are identity and their degree-zero formulas satisfy pj_+=pj_−=1. The difference j_+−j_− maps v to the full diagonal (v,Fv), retained as a genuine degree-zero kernel. Tensoring these cochain maps preserves all differential signs and transports the original primitive.

For a declared subcomplex C_lambda of the fixed full coefficient carrier, ISM42 correctly identifies

\[
\ker\left(C_\lambda^k/dC_\lambda^{k-1}
      \longrightarrow C_{\rm full}^k/dC_{\rm full}^{k-1}\right)
\cong
\frac{dC_{\rm full}^{k-1}\cap C_\lambda^k}
     {dC_\lambda^{k-1}}.
\]

The map and inverse both use the same representative; well-definedness is exactly the common boundary equivalence relation. Thus a full-source primitive need not vanish at an arbitrary proper source.

The subsequent ISM43 text still sets B_lambda=C_lambda^1 after introducing C_full=T^{tensor k, direct-sum I}. For k=1 this B_lambda is a subspace of B^{direct-sum I}, whereas the displayed map and target use single-copy V/W and B/Theta V. At the reviewed hash this is a domain mismatch. The exact repair is to specify the singleton carrier I={i_0}, A={i_0} for that single-copy formula, or to define the i_0-coordinate slice via its literal injection. For arbitrary A the full kernel map is componentwise (V/W)^A with zero insertion into the fixed carrier, with the quotient source image (Theta W)^A and the target (B/Theta V)^{direct-sum I}. If the top carrier is a general declared subspace, take its intersection with the inserted (Theta V)^A before asserting the full (V/W)^A domain. At empty A the fibre is zero and the outer support label remains fixed. This is a repair of the typed specialization; the general ISM42 kernel theorem already contains the valid exact statement.

## Final acceptance scope

Every RMT1–RMT22 claim at the pinned root hash is accepted. The exact trace norm, centered variance, full spectrum, overlap and angle bound concern the same signed derivative; both five-entry minima and the finite signed residual propagate correctly into the original endpoint. The construction gives convergent fixed-source control, with every endpoint metric, quotient map, mass and tensor coefficient retained. It gives no uniform growing-packet estimate and no RH conclusion. Final whole-body ISM acceptance awaits the explicit carrier repair to ISM43, to be recorded by a bounded reread without rewriting the historical receipts.
