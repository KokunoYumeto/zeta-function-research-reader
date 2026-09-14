# Independent full proof review: recursive metric transport RMT1–RMT18

Status: **accepted at the corrected source pin below**. The independent review found one literal angle-list count problem in the initial wording. The corrected source explicitly retains both complete q-entry geometric lists and writes the designated forced zero separately from the 2q−1 scalar slots. The resulting inequalities, the strict moment positivity proof, the nonlinear path radius and the simultaneous endpoint interval are valid.

Reviewed RMT source: `work/backpropagation_20260913/recursive_metric_transport.tex`, SHA256 `034c7b72c44a02c2874e634124b94615575948203bb14fcdb3e5284f53f80e1b`. The final bounded reread verified the explicit full angle lists, expanded strict-positivity derivation and Borel-minor proof now present in that source.

Complete input sources read:

- `output/Deligne_Mixed_Control_Continuation_2026-09-13/sources/AW.tex`, SHA256 `c79e76c087efd59871e3234ff44fb18964515dbd34f0318dffba6b3f1440f6ec`.
- `output/Deligne_Mixed_Control_Continuation_2026-09-13/sources/SP.tex`, SHA256 `180cd8a83a59e692fc0fa16a6622794927360df42317dc9d0ec3bdd6dbd7cd1a`.
- `work/cumulative_addendum_20260913_v22/portable_g0ijpdcf/Tau_Actual_Source_and_Metric_Addendum_2026-09-13/proofs/EP.tex`, SHA256 `1ba57290c995abcaa57840c5a873e767174b21bc5b19525df004f58c0bca1448`.

The original marked-product note and the complete SP proof were also read in the preceding independent review. A separately delegated full angle/positivity derivation was read and accepted in `work/backpropagation_20260913/reviews/RMT_ANGLE_SUBREVIEW.md`, which pins the same final RMT revision. The present receipt proves the propagation step and its precise connections to those inputs. No arithmetic moment value, sampled-source positivity certificate, or numerical enclosure is asserted to have been newly computed by this review.

## R1. Original measures, common space and exact input arrows

Retain the original h,k,χ of degree q≥1, H=P_{2q}, the original line S=k/2+iy and its ordered monomial row v. The arithmetic density is the original convolution of |(2ξ/h)(1/2+iy)|²/(2π). In particular g=2ξ, the full quotient g/h and the convolution order are unchanged.

From the original Gamma identity and Γ(1/2)=√π,

\[
c_{1/4}=2^{1/2}\Gamma(1/2)=\sqrt{2\pi},
\qquad r_{1/4}^{*k}(y)
=\frac{(\sqrt{2\pi})^k}{c_{k/4}}
\frac{|\Gamma(k/4+iy/2)|^2}{2\pi}.
\]

This is AW3 and EP3 with frequency u_AW=y. Its mass is (2π)^{k/2}; no factor has been removed. AW's interpolation parameter t becomes x. These assignments are identity maps on the original coefficient space and do not alter any deformation variable in the separate boundary family.

Thus the common Grams in RMT4, SP1, AW3 and EP4 coincide. AW's B_N has target P_N, while RMT's B_N has target H. Their precise relationship is B_N^{RMT}=I_NB_N^{AW}. Substitution gives

\[
I_N^*M_xI_N=M_N^{AW},\qquad
(B_N^{RMT})^*M_xB_N^{RMT}=(B_N^{AW})^*M_N^{AW}B_N^{AW}.
\]

Hence the source and relation projections coincide exactly. The quotient is the same algebra E=C[S]/(χ), in its original q remainder coordinates; the map J_N is unchanged. Their canonical quotient Grams and volumes coincide by the displayed minimum-lift formula, or by uniqueness of the lift orthogonal to the same relation space. This proves all source identifications needed to combine the three bounds.

For a specified positive atomic comparison on this same line, with weights w_ℓ>0 at its original nodes y_ℓ, M=Σ_ℓ w_ℓv(y_ℓ)^*v(y_ℓ). Its stipulated positive degree-2q Gram implies positive squared norm for every nonzero polynomial in H. Convex interpolation with another positive moment Gram preserves both the moment representation and positive definiteness. Every proof below therefore applies to such a specified sampled source. This does not assert that an arbitrary positive Hermitian matrix is a moment Gram, nor that a sample count or positivity certificate has been obtained without its original sampled-source proof.

## R2. Original metric derivative and the four signs

Put dot M=M_1−M_0 and C_x=M_x^{-1}dot M. Both M_x and dot M are Hermitian, so C_x^*M_x=M_xC_x=dot M. Thus C_x is self-adjoint in the original M_x metric; it need not be positive.

For a fixed full-column-rank map U, U(U^*M_xU)^{-1}U^*M_x is the orthogonal projection onto its image. Indeed it is idempotent, fixes U pointwise, and satisfies M_xΠ=Π^*M_x. Multiplication by the nonzero monic χ is injective, so the relation Grams are invertible at all nonzero relation dimensions. At N=q−1 their domain is zero and their determinant is one.

In the basis of original quotient lifts followed by the monic relation columns, the change-of-basis determinant is one. Block elimination identifies the minimum quotient Gram with its Schur complement, giving

\[
V_N=\frac{\det(I_N^*M_xI_N)}{\det(B_N^*M_xB_N)},
\qquad
(\log V_N)'=\operatorname{Tr}((P_N-Q_N)C_x).
\]

In relation-first order the determinant-line sign is (−1)^{q(N−q+1)}; its phase and its conjugate cancel in the Gram determinant, so this equation preserves the actual volume. It does not discard an unpaired sign.

Adding the four logarithms with their exact signs gives

\[
\begin{aligned}
\mathcal B'
&=\operatorname{Tr}((P_{q-1}+P_q-P_{2q-1}-P_{2q}
-Q_q+Q_{2q-1}+Q_{2q})C_x)\\
&=\operatorname{Tr}((U_x-W_x)C_x).
\end{aligned}
\]

This is RMT7. Cyclicity of trace is sufficient; no commutation among the source, relation and derivative operators is used.

## R3. Ordered full-relative-spectrum estimate

D=M_0^{-1}M_1 satisfies D^*M_0=M_0D=M_1 and has positive eigenvalues b_1≤⋯≤b_{2q+1}. Factorization M_x=M_0((1−x)I+xD) gives

\[
C_x=((1-x)I+xD)^{-1}(D-I).
\]

For an eigenvalue b>0, its corresponding eigenvalue is f_x(b)=(b−1)/(1−x+xb). The denominator is positive for the entire interval. Its b-derivative is (1−x+xb)^{-2}>0, so all eigenvalues retain their ordering. Furthermore f_x(b) is the x-derivative of log(1−x+xb). This proves ∫c_j=log b_j and ∫d_x=log κ, including b_j=1.

The nested relation flag has dimensions 1,q,q+1 and the source flag has corresponding increments q,1,q−1,1. Consequently both U_x and W_x have spectrum 0 with multiplicity q, 1 with multiplicity 2, and 2 with multiplicity q−1. Each is the sum of orthogonal spectral projections of ranks q+1 and q−1.

For a rank-r orthogonal projection Π and an eigenbasis e_j of C_x, set t_j=⟨e_j,Πe_j⟩. Then 0≤t_j≤1 and Σt_j=r. Hence Σ_{j≤r}c_j≤Tr(ΠC_x)≤Σ_{j≥2q+2−r}c_j: the extremal sums are obtained by assigning total mass r to the respective smallest or largest coefficients, and exchanging any mass with an out-of-order coefficient can only improve the relevant extremum. Applying this to the two spectral projections gives, for Z=U_x or W_x,

\[
\sum_{j=1}^{q+1}c_j+\sum_{j=1}^{q-1}c_j
\le\operatorname{Tr}(ZC_x)
\le\sum_{j=q+1}^{2q+1}c_j+\sum_{j=q+3}^{2q+1}c_j.
\]

Subtracting upper and lower bounds and writing the cancellation of c_{q+1} yields exactly

\[
|\mathcal B'|\le c_{q+2}-c_q
+2\sum_{j=1}^{q-1}(c_{2q+2-j}-c_j)=E_q(x).
\]

All its differences are nonnegative. Its integral is the full AW13 expression L_q(D); each ratio in that expression is bounded by κ, with total coefficient 1+2(q−1)=2q−1. This proves RMT8, the first bound of RMT9, and RMT15.

## R4. Actual overlap and measurability of the common range

The ranks of U_x and W_x are q+1 in dimension 2q+1, so their common range has dimension s_x≥1. Their eigenvalues give Tr U_x=Tr W_x=2q and Tr U_x²=Tr W_x²=4q−2. By trace cyclicity,

\[
\operatorname{Tr}((U_x-W_x)^2)=8q-4-2\operatorname{Tr}(U_xW_x).
\]

Each operator dominates its own range projection. If E_x projects onto their common range, it follows that U_x−E_x and W_x−E_x are positive with trace 2q−s_x. Their difference is U_x−W_x. Therefore

\[
\|U_x-W_x\|_1\le4q-2s_x.
\]

Cauchy–Schwarz on its 2q+1 real eigenvalues also gives

\[
\|U_x-W_x\|_1
\le\sqrt{(2q+1)(8q-4-2\operatorname{Tr}(U_xW_x))}.
\]

The square-root argument is nonnegative because it equals (2q+1) times the trace square of the self-adjoint difference. Since the difference has trace zero, replace C_x in its trace pairing by C_x−(c_1+c_{2q+1})I/2. That centered operator has norm d_x/2 in M_x. In an orthonormal eigenbasis of U_x−W_x, summing its diagonal Rayleigh quotients proves

\[
|\mathcal B'|\le(d_x/2)\|U_x-W_x\|_1\le O_q(x).
\]

This proves the second RMT9 bound and RMT10. It retains the actual cross-pairing Tr(U_xW_x).

There is no hidden continuity assumption on the intersection dimension. The matrices U_x and W_x are continuous, indeed smooth, because their fixed subspace Grams are invertible throughout the compact interval. Their common dimension has the explicit formula

\[
s_x=2(q+1)-\operatorname{rank}[\,U_x\ W_x\,].
\]

For a finite continuous matrix function, rank≥r is the finite union of the open sets where one of its r×r minors is nonzero. Thus its rank, and hence s_x, is Borel measurable and bounded. The square root, traces and minimum operations in O_q are therefore measurable and bounded. Pointwise inequalities do not require choosing a measurable eigenbasis or a continuous common-range projection.

## R5. Complete crossed angle lists and the corrected scalar count

Let R_i:E→H denote the canonical minimum section and L_i=im R_i. For i≤j, projection of R_i to L_j gives R_j, since both have the same remainder and their difference is an original relation. Thus

\[
R_i^*M_xR_j=G_j,
\qquad G_i-G_j=(R_i-R_j)^*M_x(R_i-R_j)\succeq0.
\]

The isometries F_i=R_iG_i^{-1/2} give cross-Gram squared singular values equal to the eigenvalues of G_i^{-1/2}G_jG_i^{-1/2}. These numbers are strictly positive and at most one. Write them as cos² θ_ν with 0≤θ_ν<π/2. Their determinant gives log(V_i/V_j)=Σ_ν−log cos²θ_ν.

For a nonzero angle, the exact two-dimensional difference of projections has matrix

\[
\begin{pmatrix}\sin^2\theta&-\sin\theta\cos\theta\\
-\sin\theta\cos\theta&-\sin^2\theta\end{pmatrix},
\]

with eigenvalues ±sin θ. Its trace pairing with C_x has absolute value at most d_x sin θ, by the two extreme Rayleigh bounds. At a zero angle the common direction contributes zero and remains part of the geometric list.

For the crossed pairs (q−1,2q) and (q,2q−1), both complete angle lists have q entries. In the second pair both q-dimensional minimum spaces lie in P_{2q−1}∩(χP_0)^⊥, of dimension 2q−1. Their intersection therefore has dimension at least one; designate a zero angle φ_1=0. The corrected RMT11 retains the entire θ_1,…,θ_q and φ_1,…,φ_q lists and defines a=2q−1 scalar entries from all θ_i and φ_j with j≥2. Its displayed equations keep the contribution of φ_1 explicitly as zero. Every further zero remains in those a slots.

Their total cost is B, and the two exact projection-difference estimates add with the four original signs. For f(z)=√(1−e^{−z}), direct differentiation on z>0 gives

\[
f''(z)=-\frac{e^{-z}(2-e^{-z})}{4(1-e^{-z})^{3/2}}<0.
\]

Continuity extends concavity to zero. Jensen on the retained a slots now gives

\[
|\mathcal B'|\le d_x\left(\sin\varphi_1+\sum_{\nu=1}^{a}f(\lambda_\nu)\right)
\le a\sqrt{1-e^{-\mathcal B/a}}\,d_x=A_q(x).
\]

This proves RMT11 with its corrected count. The initial wording claiming a complete 2q−1 geometric list while also retaining every zero was inaccurate; the corrected source removes that ambiguity without changing the bound.

## R6. Strict positivity for the original moment source, including atomic samples

The two nested quotient Gram inequalities above give both crossed determinant ratios at least one. If B=0, each ratio must be one. Since all eigenvalues of G_j^{-1/2}G_iG_j^{-1/2} are at least one, determinant one makes all of them one, hence G_i=G_j. The squared-norm identity then makes R_i=R_j as maps to the same H.

For the first crossed pair, the domain P_{q−1} has no relation and its minimum section is the literal remainder section. Equality with R_{2q} puts 1 in L_{2q}, which is orthogonal to χP_q. If χ(S)=Σ_{j=0}^q a_jS^j, define

\[
\chi^{\#_k}(S)=\sum_{j=0}^q\overline{a_j}(k-S)^j.
\]

The original line obeys conjugate S=k−S. Thus χ^{#_k}(S)=conjugate χ(S) at each point of the original measure, including each atom. Its degree is q. Consequently χχ^{#_k} belongs to χP_q⊂H, and the orthogonality would imply

\[
0=\langle1,\chi\chi^{\#_k}\rangle_{M_x}
=\int|\chi(S)|^2d\mu_x.
\]

The last integral is strictly positive because χ is a nonzero polynomial in H and the actual moment Gram is positive definite. This contradiction proves B(x)>0 for every x. For an atomic measure the same proof reads Σ_ℓw_ℓ|χ(S_ℓ)|²>0; no absolute-continuity assumption is used. For a general coefficient matrix lacking the original-line moment identity, this particular reflected-polynomial implication has not been asserted.

All quotient Grams are smooth positive matrices on [0,1], so B is continuous. Positivity and compactness supply a strictly positive minimum on this fixed path. They supply no estimate uniform over varying h,k or q.

## R7. Pointwise minimum, finite integrals and the nonlinear coordinate

Put a=2q−1 and f_a(B)=a√(1−e^{−B/a}). On the fixed path this is a positive bounded continuous function with positive minimum. The three established bounds concern the same |B′|. Therefore

\[
|B'|\le m(x):=\min\{E_q,O_q,f_a(B)d_x\}.
\]

The function m is measurable, bounded and nonnegative. Integrating |B′| gives |B(1)−B(0)|≤J_q=∫m. A pointwise minimum is at most each term separately, so J_q≤min{L_q(D),∫O_q,∫A_q}. This proves RMT13–RMT15 with every coefficient unchanged.

For B>0 define H_a(B)=2 arcosh(exp(B/(2a))) using the nonnegative real inverse branch. Differentiating cosh(H_a(B)/2)=exp(B/(2a)) gives

\[
H_a'(B)=\frac{1}{a\sqrt{1-e^{-B/a}}}=\frac1{f_a(B)}>0.
\]

If z>0, the function K_a(z)=2a log cosh(z/2) satisfies exp(K_a(z)/(2a))=cosh(z/2), so H_a(K_a(z))=z on that branch. Conversely K_a(H_a(B))=B by the defining equality. At zero both extend continuously with value zero. This proves RMT16 and the claimed monotonic inverse.

The chain rule and positivity of f_a(B) imply

\[
\left|\frac d{dx}H_a(B(x))\right|
\le\frac{m(x)}{f_a(B(x))}
=\min\{E_q/f_a(B),O_q/f_a(B),d_x\}.
\]

The order of a finite minimum is preserved under division by this positive common denominator. All three functions are measurable and bounded by the previous sections; the minimum is also at most d_x. Thus the integral is exactly I_q as defined in RMT13, and integration gives

\[
|H_a(B(1))-H_a(B(0))|\le I_q\le\int_0^1d_xdx=\log\kappa.
\]

This proves RMT17. It preserves the additional full-spectrum and actual-overlap terms inside the nonlinear path radius. It does not replace the integral by an unproved estimate of those quantities.

## R8. Simultaneous endpoint interval and edge cases

Writing H_0=H_a(B(0)), the preceding inequality and nonnegativity give max{0,H_0−I_q}≤H_a(B(1))≤H_0+I_q. Apply the increasing K_a to obtain the nonlinear lower and upper bounds. Independently, the additive bound gives B(0)−J_q≤B(1)≤B(0)+J_q and strict positivity gives B(1)>0. Taking the maximum of the three valid lower bounds and the minimum of the two valid upper bounds yields exactly RMT18. Because the actual B(1) satisfies every constituent inequality, the resulting interval is nonempty. Its lower endpoint can be zero even though B(1)>0.

For q=1, a=1; the crossed pairs are (0,2) and (1,1). The entire second pair has one zero angle. The first supplies the one scalar slot. E_1=c_3−c_1=d_x, the multiplicity-two source/relation eigenspaces are zero-dimensional, and all empty sums are correctly zero. The formulas reproduce AW's q=1 nonlinear coordinate with the additional applicable pointwise overlap comparison.

If M_1=cM_0 with c>0, every b_j equals c. All c_j(x) coincide, giving d_x=E_q=O_q=A_q=0. The denominator f_a(B) is still positive for the actual moment path, so I_q=J_q=0 without a 0/0 expression. Every quotient Gram scales by 1−x+xc in its fixed dimension q. The four determinant powers have signs +,+,−,− and sum to zero, proving B(x)=B(0). RMT18 then gives the singleton endpoint B(0). This treats c=1 and q=1 without a separate convention.

## R9. Original class maps, primitives and support scope

The argument changes scalar estimates, not any map. For each actual cutoff, J_N:P_N→E and B_N:P_{N−q}→H remain the original remainder and monic relation maps. The arithmetic observation σ_h^{⊗k}η_{h,k}J_N has its original target Q^{⊗k}, with the complete tensor Taylor unit in η. For two canonical sections, the exact difference is R_i−R_j=B_jX_{ij}, with X_{ij}=(B_j^*M_xB_j)^{-1}B_j^*M_xR_i. EP32 proves both this formula and its retained squared norm.

EP33–EP36 retain the original h(D)F_h=Θφ_0, the monic tensor division χ(Σs_i)=Σ_jh(s_j)L_j and its full coefficient polynomials. The degree-(k−1) theta primitive with coefficient (−1)^{j−1} has differential equal to the original realization of χX_{ij}; the tensor differential supplies the same sign and cancels it termwise. None of these maps or coefficients depends on choosing the minimum of the three scalar bounds. At a fixed retained support label the lifted linear map sends represented zero to represented zero in that same label and external absence to external absence.

The reviewed RMT text makes no statement that a primitive is killed in an arbitrary additional quotient W, no identification of all source kernels, and no identification of different support labels. Its finite observation has the specified domain P_N and codomain E followed by the original injective packet observation; any extension of the ambient cochain category would require its own exact maps. The support-preservation paragraph therefore has the stated finite scope.

## Acceptance and retained limitation

Every displayed RMT1–RMT18 identity and inequality follows from the exact common-source identifications and proofs above. The one discovered count ambiguity has been repaired at the pinned source. In particular, the proof is valid for the original positive moment path and for the specified positive atomic path once its actual degree-2q Gram positivity is supplied by its source certificate. It is not a positivity claim for an arbitrary coefficient form.

The result gives two calculated path radii and their simultaneous endpoint interval. It proves no bound on their growth with the original arithmetic packet or tensor order and makes no RH conclusion. No numerical quadrature or new sampled-source certificate was run or claimed in this review.
