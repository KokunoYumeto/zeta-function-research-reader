# Independent complete review of SP1–SP13

Reviewed source: `work/tau_signed_projection_control_20260913.tex`, SHA256 `180cd8a83a59e692fc0fa16a6622794927360df42317dc9d0ec3bdd6dbd7cd1a`.

Original source: `Tau_Marked_Product_Four_Endpoint/NOTE.tex`, SHA256 `40749e2a9d599a322e7b125eb43ad0878a066a51b61da52cc3bb2ffb94cbd841`, sections 8–10, formulas (47)–(67). The original file was read completely through these sections. This review covers the complete SP1–SP13 fragment, including the exact density correction and the common-positive-part improvement incorporated during review.

Result: all displayed identities and bounds in the reviewed version are proved below. In particular its final coefficient is the stronger **2q−1**, obtained from the common range; the earlier **2q** coefficient was valid but weaker. The kernel comparison explicitly includes the inverse source metric. The result is finite control of the actual packet correction. No estimate for the growth of its condition number in the arithmetic family has been proved here.

## 1. Retained objects, positivity and metric adjoints

Fix the original marked packet data h,k and its original monic sum polynomial χ of degree q≥1. The independent variable is S=k/2+iy. The coefficient space is H=P_{2q}, dimension 2q+1, with its original ordered monomials. Its Grams are formed from the actual densities m=w_h^{*k} and r=r_{1/4}^{*k}, including their literal masses. Every moment used is finite by the original note's input estimates. Each measure has positive density on a positive-measure set, so a nonzero polynomial has strictly positive norm. Thus M_0 and M_1 are positive definite, and so is M_x=(1−x)M_0+xM_1 for every x in [0,1]. No normalized measure or rescaled coordinate is introduced.

Put dot M=M_1−M_0 and T_x=M_x^{-1} dot M. Since dot M is Hermitian,

\[
T_x^*M_x=\dot M=M_xT_x.
\]

This proves self-adjointness in the original M_x metric. It does not give a positivity assertion for T_x. All adjoints denoted by * in coordinate formulas are the ordinary conjugate transpose; M_x-self-adjointness is expressed by the displayed intertwining equation. Traces remain the ordinary algebraic traces of these endomorphisms.

## 2. Actual source and relation projections

For each retained endpoint N, let I_N:P_N→H be coefficient inclusion. For N≥q let B_N:P_{N−q}→H be literal multiplication by χ followed by coefficient inclusion. These maps are fixed as x varies. Their full-column rank follows respectively from inclusion and from injectivity of multiplication by a nonzero polynomial.

For any such inclusion U, write H_U=U^*M_xU. Direct multiplication gives

\[
\Pi_U=UH_U^{-1}U^*M_x,
\quad \Pi_U^2=\Pi_U,
\quad M_x\Pi_U=\Pi_U^*M_x,
\quad \Pi_UU=U.
\]

Its range is exactly im U, and its kernel is the M_x-orthogonal complement of im U. This proves SP2 with P_N=Π_{I_N} and Q_N=Π_{B_N}. At N=q−1 the relation domain has dimension zero and Q_{q−1}=0. For nested subspaces U⊂V, the orthogonal decomposition U⊕(V∩U^⊥)⊕V^⊥ proves Π_UΠ_V=Π_VΠ_U=Π_U. This applies within the P family and within the Q family. No commutation between an arbitrary P_N and Q_M is assumed.

## 3. Quotient determinant and all four derivative signs

Use the original quotient basis 1,S,…,S^{q−1}. In P_N the ordered basis consisting first of these lifts and then χ,Sχ,…,S^{N−q} has unit determinant: its last columns have successively leading coefficients 1 in degrees q,…,N. In this basis the Gram has block form

\[
\begin{pmatrix}A&C\\ C^*&H_B\end{pmatrix},
\quad H_B=B_N^*M_xB_N.
\]

The minimum-norm lift has coefficient matrix consisting of the quotient lift minus B_NH_B^{-1}C^*. Its quotient Gram is therefore A−CH_B^{-1}C^*. This is exactly the original canonical quotient metric (J_NM_N^{-1}J_N^*)^{-1}. Block elimination of determinant one gives

\[
V_N=\frac{\det(I_N^*M_xI_N)}{\det(B_N^*M_xB_N)}.
\]

The denominator at N=q−1 is the determinant of the zero-dimensional matrix, equal to one. The retained coordinate change introduces no metric factor. If one instead orders the relation columns first, the permutation sign has modulus one and cancels in the Gram determinant; this review retains the original quotient-first ordering.

Differentiating the two log determinants and applying cyclicity gives

\[
(\log V_N)'=\operatorname{Tr}((I_N^*M_xI_N)^{-1}I_N^*\dot M I_N)
-\operatorname{Tr}((B_N^*M_xB_N)^{-1}B_N^*\dot M B_N)
=\operatorname{Tr}(T_x(P_N-Q_N)).
\]

For F=log V_{q−1}+log V_q−log V_{2q−1}−log V_{2q}, the source terms are

\[
P_{q-1}+P_q-P_{2q-1}-P_{2q}=-\mathcal P_x,
\]

and the relation terms are

\[
-Q_{q-1}-Q_q+Q_{2q-1}+Q_{2q}=\mathcal R_x.
\]

Thus F′=Tr(T_x A_x) with A_x=R_x−P_x, exactly as SP5–SP7 state. Every original sign is retained, including both denominator signs.

## 4. Exact map to the original signed projection density

An orthogonal projection acting on coefficients and its scalar evaluation density are related by the original Riesz metric. For the full monomial row v=v_{2q}(y),

\[
P_NM_x^{-1}=I_N(I_N^*M_xI_N)^{-1}I_N^*,
\quad
Q_NM_x^{-1}=B_N(B_N^*M_xB_N)^{-1}B_N^*.
\]

Evaluation v(·)v^* of these identities recovers exactly K_N and K_N^{rel} in (52). Consequently

\[
\mathsf R_x(y)-\mathsf P_x(y)=v\mathcal A_xM_x^{-1}v^*.
\]

In particular, the inverse M_x factor is essential in the original nonorthonormal monomial coordinates. It now appears explicitly in the reviewed source. Since dot M=∫v^*v dot μ(y)dy, integration of this density gives

\[
\int v\mathcal A_xM_x^{-1}v^*\dot\mu(y)dy
=\operatorname{Tr}(\mathcal A_xM_x^{-1}\dot M)
=\operatorname{Tr}(T_x\mathcal A_x).
\]

This proves the exact correspondence between the matrix trace and the original signed source integral without a replacement measure, an endpoint ratio bound, or a discarded relation norm.

## 5. Ranks, multiplicities, trace square and overlap

The relation flag im Q_q⊂im Q_{2q−1}⊂im Q_{2q} has dimensions 1,q,q+1. In its orthogonal increments, R_x=Q_{2q−1}+Q_{2q}−Q_q acts by 1,2,1, with multiplicities 1,q−1,1. It vanishes on the orthogonal complement.

For the source flag, let D_j=P_j−P_{j−1} be the rank-one orthogonal degree increment, using P_{−1}=0. Then

\[
\mathcal P_x=D_q+2\sum_{j=q+1}^{2q-1}D_j+D_{2q}.
\]

This gives the same eigenvalues and multiplicities. The intervening sum is empty at q=1, so that case has two eigenvalues 1 and no eigenvalue 2. In all cases,

\[
\operatorname{rank}\mathcal R_x=\operatorname{rank}\mathcal P_x=q+1,
\quad \operatorname{Tr}\mathcal R_x=\operatorname{Tr}\mathcal P_x=2q,
\quad \operatorname{Tr}\mathcal R_x^2=\operatorname{Tr}\mathcal P_x^2=4q-2.
\]

The original density masses 2q are therefore traces, not the ranks q+1. Trace cyclicity, which needs no cross-family commutation, gives

\[
\operatorname{Tr}\mathcal A_x=0,
\quad \operatorname{Tr}\mathcal A_x^2=8q-4-2\operatorname{Tr}(\mathcal R_x\mathcal P_x).
\]

Let E_R,E_P be the M_x-orthogonal range projections of R_x,P_x. Their ranges each have dimension q+1 in dimension 2q+1. Hence L_x=im R_x∩im P_x has dimension s_x≥1. An orthonormal basis of im E_R containing a basis of L_x shows

\[
\operatorname{Tr}(E_RE_P)=\sum_j\|E_Pe_j\|_{M_x}^2\ge s_x\ge1.
\]

The spectra computed above give R_x≥E_R and P_x≥E_P. For positive operators A′≥A and B≥0, Tr((A′−A)B)=Tr(B^{1/2}(A′−A)B^{1/2})≥0. Apply this first to one factor, then the other, to prove

\[
\operatorname{Tr}(\mathcal R_x\mathcal P_x)\ge\operatorname{Tr}(E_RE_P)\ge s_x\ge1.
\]

The same argument works in the original M_x metric, or equivalently after conjugating all operators by the same M_x^{1/2}; it never changes the underlying Gram inputs.

## 6. Centered trace bound and common positive part

Because Tr A_x=0, subtracting a scalar cI from T_x leaves the trace pairing unchanged. Let d_x be the difference of its extreme real eigenvalues and choose c to be their midpoint. The M_x-self-adjoint operator T_x−cI has operator norm d_x/2. In an M_x-orthonormal eigenbasis of A_x with eigenvalues α_j,

\[
|\operatorname{Tr}((T_x-cI)\mathcal A_x)|
\le\sum_j|\alpha_j|\,|\langle e_j,(T_x-cI)e_j\rangle_{M_x}|
\le\frac{d_x}{2}\|\mathcal A_x\|_1.
\]

Let E_L be the orthogonal projection onto L_x. Since E_L≤E_R≤R_x and E_L≤E_P≤P_x, both R_x−E_L and P_x−E_L are positive and have trace 2q−s_x. They have difference A_x. The trace-norm triangle inequality therefore gives the stronger estimate

\[
\|\mathcal A_x\|_1\le4q-2s_x\le4q-2.
\]

This subtracts an actual common positive operator. It does not assume that E_L commutes with R_x or P_x; Loewner positivity suffices. Independently, Cauchy–Schwarz on the at most 2q+1 real eigenvalues gives

\[
\|\mathcal A_x\|_1\le\sqrt{(2q+1)\operatorname{Tr}\mathcal A_x^2}.
\]

Combining these inequalities with the previous section proves the complete overlap-refined SP10. Its expression under the square root is nonnegative because it is the trace square of the self-adjoint A_x. The earlier upper bound 4q and final coefficient 2q were valid consequences of the cruder triangle inequality. The revised common-range proof gives the sharper coefficients 4q−2s_x and 2q−1 without additional hypotheses.

## 7. Integration in the actual pair of Grams

Set R=M_0^{-1}M_1. Then M_0R=M_1=R^*M_0 and v^*M_0Rv=v^*M_1v>0 for nonzero v. Thus its extreme eigenvalues r_min,r_max are positive. The literal factorization

\[
M_x=M_0(I+x(R-I))
\]

gives T_x=(I+x(R−I))^{-1}(R−I). If Rv=rv, then T_xv=f_x(r)v, where

\[
f_x(r)=\frac{r-1}{1+x(r-1)},
\quad \frac{\partial f_x}{\partial r}=\frac{1}{(1+x(r-1))^2}>0.
\]

The denominator is positive throughout the retained interval. Hence the two extreme eigenvalues of T_x are f_x(r_min),f_x(r_max), even though its self-adjoint metric varies with x. Since

\[
\int_0^1 f_x(r)\,dx=\log r
\]

for r≠1, and both sides vanish for r=1, one gets ∫d_x dx=log(r_max/r_min). All projection matrices are smooth in x because their positive Grams remain invertible on the compact interval. Integrating F′ and using the proven trace bound now yields

\[
|\Delta_{h,k}|
\le\frac12\int_0^1d_x\|\mathcal R_x-\mathcal P_x\|_1dx
\le(2q-1)\log(r_{\max}/r_{\min}).
\]

The pointwise minimum in SP10 supplies the stronger overlap integral before this final simplification. When M_1 is a positive scalar multiple of M_0, r_min=r_max, so d_x=0 and F′=0. Equivalently every quotient Gram, of fixed dimension q, acquires the same scalar factor and the four exponents sum to zero. This proves exact mass cancellation in that case without setting either original mass to one.

## 8. Exact checks and research scope

`work/tau_signed_projection_control_exact_checks_20260913.py` and its JSON output record six exact SymPy calculations: q=1 and q=2, each at x=0,1/3,1. The script uses rational complex monomial Grams from positive discrete measures to exercise the algebra. These fixtures are explicitly not asserted to be arithmetic zero packets. All inverses, determinants, ranks, adjoints, overlap traces and kernel evaluations are computed exactly.

The checks verify projection idempotence and metric adjoints; the monic determinant-one change and Schur quotient identity; ranks q+1, traces 2q and trace squares 4q−2; trace A=0 and its overlap formula; the original four derivative signs; the density identity with the inverse metric; the common range dimension at least one; and the scalar derivative and antiderivative used in the integrated bound. All six cases pass. For example q=1 at x=0 gives overlap 54901/51013>1, while q=2 gives rank 3 and trace 4, so the checks exercise the rank-versus-trace distinction rather than only the exceptional q=1 case.

The exact algebra checks supplement the proofs above; they do not replace them. No new arithmetic moment evaluation, numerical condition-number certification, or asymptotic bound is claimed. The completed calculation does supply a sharper finite estimate in the original source coordinates. Its continuation must investigate the actual r_min,r_max and joint source/relation geometry along the packet and tensor family; nothing here closes the Deligne-style control programme or yields an RH verdict.
