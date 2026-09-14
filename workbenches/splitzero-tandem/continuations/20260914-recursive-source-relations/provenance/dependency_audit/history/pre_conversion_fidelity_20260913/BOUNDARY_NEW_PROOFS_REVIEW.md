# Independent review of the new boundary proof blocks

Review date: 13 September 2026. Reviewer lane: `backprop_dependency_audit/boundary_added_proof_review`.

## Scope and durable record

The delegated instruction was: “Independently review only new equations/proofs in work/backpropagation_20260913/boundary/revised/tex against original contexts and evidence/*.diff: DS70–74, XD.u1–7, DT14–16, SC.u1–4, PC.u1–3, LC.u1, DC31–32, RCX.u1–6. Read complete inserted proof blocks (line ending diffs may be noisy, use revised sources and exact labels). Do not edit. Pay exact u-connection signs, derivative-of-period inverse, full original metric, noncommutative CB+BC, degree-correct chain map. Send concrete errors immediately to /root/backprop_boundary_wave and me; write work/backpropagation_20260913/dependency_audit/BOUNDARY_NEW_PROOFS_REVIEW.md with source hashes and precise accepted scope. Other boundary AP module is independently owned; skip it unless lane asks. User demands source proof precision, preserve domains and constants.”

The boundary lane subsequently requested inclusion of the complete new SC.u5–u7 block. That addition is included below. The user-direction record already exists at `../USER_DIRECTION_AND_OWNERSHIP.md`; the root task retains the session provenance. This report records this delegated review, its findings, and its source pins. No mathematical source was edited by this reviewer. AP, the tensor-primary boundary proof, and the rest of the historical chapters are outside the accepted scope; cited original contexts were read to check the inserted statements' actual objects and hypotheses.

The complete inserted blocks were read from the revised TeX. Their locations were checked against the eight `boundary/evidence/*.tex.diff` files and the corresponding unchanged original contexts. Additional source reading covered SP.1–SP.15 in `boundary/proofs/SPC_ORIGINAL.tex`, for the phase, Pascal matrix, boundary coefficient and ordered-period calculation used by SC.u5–u7.

## Status

All displayed algebra in the requested blocks, including SC.u5–u7, has been checked with the original signs, matrix order, domains, metrics, constants and contour orientations retained. One source-typing defect was reported immediately to both responsible lanes: the first version of DT.16 introduced `\mathcal F_a` and `\mathcal F` without defining their direct-image complexes, projection, or finite-field base. The mathematical translation identity has the correct sign, but the original version does not meet the requested explicit-object standard. The lane repaired the definitions, and the revised complete DT.16 block was reread and accepted; the final repair and source pins are recorded below.

## XD.u1–XD.u7: exact polynomial division and the connection

The source retains

\[
\chi(S)=S^q+\sum_{a=0}^{q-1}c_aS^a,\quad q\geq1,\qquad
\Phi_t(S)=\frac{S^{q+1}}{q+1}+\sum_{a=0}^{q-1}\frac{c_aS^{a+1}}{a+1}-tS,
\]

and the coefficient complex with differential (L=u\partial_S+\chi-t). Its degree-one quotient is a coefficient-vector-space quotient, with the fixed remainder frame (1,S,\ldots,S^{q-1}); it is not treated as an algebra quotient by (L). Ordinary multiplication by (S) is separately taken in (\mathbb C[S]/(\chi-t)), with the original companion matrix (A(t)).

For (0\leq b<q), monic division has quotient (Q_b^\Phi) of degree at most (b+1) and remainder (R_b^\Phi) of degree less than (q). The identity

\[
\Phi_tS^b-LQ_b^\Phi=R_b^\Phi-u(Q_b^\Phi)'
\]

has right side of degree at most (q-1), so no further twisted reduction is missing. Ordinary remainder multiplication gives (C_\chi(t)=\Phi_t(A(t))). Above degree (q), neither (-tS^{b+1}) nor the product (-tQ_b^\Phi) affects division coefficients. Descending comparison therefore makes all positive-degree coefficients of (Q_b^\Phi) independent of (t); only its constant term can depend on (t). Differentiation removes that constant. The quotient leading coefficient is (1/(q+1)), hence the derivative has coefficient ((b+1)/(q+1)) at (S^b) and no coefficients at higher degrees. Consequently the complete (B_\chi) has the stated triangular entries, (\partial_tB_\chi=0), and

\[
\operatorname{Tr}B_\chi=\frac{1+2+\cdots+q}{q+1}=\frac q2.
\]

Set (M=\partial_u-\Phi_t/u^2). On unreduced polynomial representatives,

\[
[L,\partial_u]=-\partial_S,\qquad [L,-\Phi_t/u^2]=-(\chi-t)/u,
\qquad [L,M]=-L/u.
\]

Thus (ML=L(M+1/u)). This verifies precisely the degree-zero connection (M+1/u), degree-one connection (M), and their chain identity; the sign of (1/u) is positive. Reducing (M(S^b)) gives

\[
\Omega_u=-C_\chi(t)/u^2+B_\chi/u.
\]

The fixed labelled contours have the original signs (-\ell_0+\ell_j). On a sufficiently small neighborhood of a nonzero (u_0), rays fixed in the interiors of their common decay sectors give a negative leading real exponent uniformly; the lower terms and each fixed derivative insert polynomial factors dominated by an integrable (Cr^Le^{-\alpha r^{q+1}}). Moving endpoints inside that neighborhood have connecting arcs with vanishing integrals by the same bound. Differentiating the periods therefore inserts (-\Phi_t/u^2) and gives (\Pi_u=\Pi\Omega_u), with no contour sign change.

The polynomial operators (M) and (\partial_t-S/u) commute: the (S/u^2) from differentiating (-S/u) cancels the (-S/u^2) from differentiating (-\Phi_t/u^2). The degree-zero additional (1/u) has zero commutator with the (t) operator. After reduction this gives

\[
\partial_u\Omega_t-\partial_t\Omega_u+[\Omega_u,\Omega_t]=0,
\qquad\Omega_t=-A(t)/u.
\]

The determinant coefficient is (-\operatorname{Tr}C_\chi/u^2+q/(2u)). Since the original (\mathcal F) is (\operatorname{Tr}\Phi_t(A(t))), this matches the determinant exponent exactly. Multiplication of the original (q) monomial column constants gives the power ((q+1)^{q/2-q}=(q+1)^{-q/2}), phase (e^{\pi iq/2}), gamma product and the same ordered determinant (\det W). Hence XD.u7 retains every factor of XD16–XD19.

The paragraph following XD.u7 preserves the distinct domains (E_h^{\otimes k}) and the cyclic sum algebra. Its marked-fibre injection is the original weighted map (\eta_k[P]=\upsilon_h^{\otimes k}P(\sum_i s_i)1). For any literal polynomial identity (\chi(S)P(S)=\sum_i h(s_i)Q_i), subtracting each original product differential (u\partial_iQ_i+(h(s_i)-t_i)Q_i) gives exactly (\sum_i(t_iQ_i-u\partial_iQ_i)) in the product quotient. This does not substitute a product-period family for the cyclic family.

## DS70–DS74: cochain degrees and the retained source primitive

For the ordered (k)-factor complex let (M_k=\partial_u-\sum_i\Phi_{t_i}(S_i)/u^2). Each (L_i) obeys ([L_i,M_k]=-L_i/u). Since the degree-raising exterior differential (d\) retains the original exterior signs, (M_kd=dM_k+d/u). Therefore

\[
\left(M_k+\frac{k-j-1}{u}\right)d
=d\left(M_k+\frac{k-j}{u}\right)
\]

on cochain degree (j). This proves the degree-correct DS71 chain connection, including every nontop term.

On the stated original admitted theta-source domain, (j_Er_N=I), (j_ED^{(k)}=Aj_E), and (D^{(k)}r_N=r_NA+dK_N). All these maps are parameter independent. Consequently multiplying the new (\partial_a+r_N\Omega_aj_E) by (j_E) or (r_N) gives both DS73 identities, including their derivative terms. The splitting (x=r_Nj_Ex+(x-r_Nj_Ex)) has second summand in (\ker j_E), and the connection restricts there to parameter differentiation. Its curvature is the image under (r_N(-)j_E) of XD.u6 because ((r_N\Omega_uj_E)(r_N\Omega_tj_E)=r_N\Omega_u\Omega_tj_E).

Finally,

\[
\begin{aligned}
[D^{(k)},\nabla_{a,N}^{\rm src}]
&=(r_NA+dK_N)\Omega_aj_E-r_N\Omega_aAj_E\\
&=r_N[A,\Omega_a]j_E+dK_N\Omega_aj_E.
\end{aligned}
\]

The Euler action (D^{(k)}) here has cochain degree zero; (d) is the original boundary differential. The primitive (K_N\Omega_aj_E) has the same primitive-term target as (K_N), so the displayed formula does not place a primitive in the top cochain degree. The nearby unchanged specialization map to (E[-1]) is zero in degree zero and sends (P\,dS\) to ([P]_\chi) in degree one, consistent with the shift and its stated kernel contraction.

## DT.14–DT.16: translation with its scalar retained

The original substitution (T_aP(X)=P(X+a)) is independent of (u,t), and the retained primitive gives

\[
\Phi_a(X+a)-t(X+a)=\Phi(X)-tX+h_a(t),\qquad
h_a(t)=-\Phi(-a)-ta.
\]

It follows on both terms of the polynomial complex that

\[
T_a\nabla_u^aT_a^{-1}=\nabla_u-h_a(t)/u^2.
\]

In degree zero both sides also include the same (1/u). With (f_a=e^{h_a/u}), differentiation gives ((f_a)_u=-h_af_a/u^2) and ((f_a)_t=-af_a/u). Product expansion then gives the exact (u) and (t) intertwining identities for (f_aT_a). The unchanged triangular substitution matrix (C_a) has determinant one, so differentiating (\Pi_a=f_a\Pi C_a) gives DT.15 with the same negative scalar (h_a/u^2); taking determinants retains (f_a^q).

The finite-field translation uses the specified reduction of all coefficients to (\mathbb F_Q), (p>d), the fixed nontrivial additive character (\psi), and (\ell\ne p) from the original DT.12 setup. Addition of the Artin–Schreier torsors sends the two functions ((\Phi(X)-tX)/u) and (h_a(t)/u) to their sum, which is the pulled-back translated phase. The latter character line is pulled back from the parameter base, so the projection formula supplies the displayed direct-image identity degree by degree. A source repair was requested to define these complexes and the projection explicitly; that defect and its final resolution are recorded in the status sections, rather than silently supplying missing source definitions in the acceptance statement.

## SC.u1–SC.u4: full metric and mixed curvature

The fixed inclusion (I:F\hookrightarrow E), original (G_N>0), and fixed Euclidean target metric are retained. Set (Y=\Pi I), (H=Y^*Y>0), (P=YH^{-1}Y^*), (N=1-P), (Y_a=\Pi\Omega_aI), (Z_a=NY_a). Holomorphy gives

\[
H_b=Y^*Y_b,\quad H_{\bar a}=Y_a^*Y,\quad
H_{\bar a b}=Y_a^*Y_b,\quad
(H^{-1})_{\bar a}=-H^{-1}Y_a^*YH^{-1}.
\]

The trace derivative is therefore (\operatorname{Tr}(H^{-1}Y_a^*NY_b)). Since (N=N^*=N^2), this is exactly (\operatorname{Tr}(H^{-1}Z_a^*Z_b)). Contracting with a vector ((v_u,v_t)) yields the squared norm of ((v_uZ_u+v_tZ_t)H^{-1/2}), proving the asserted nonnegative Hermitian matrix without commuting any factors. Its coefficients use the displayed holomorphic-first one-form order (db\wedge d\bar a).

At (t=0), (C_\chi(0)=\Phi(A)) preserves (I(F)), as does (A). Thus (N\Pi C_\chi(0)I=0) and (N\Pi AI=0), giving (Z_t=0) and (Z_u=u^{-1}N\Pi B_\chi I). This is exactly SC.u3, without assuming (B_\chi)-invariance in the general cyclic case.

For the original transported theta metric (\widetilde G_N=\Pi^{-*}G_N\Pi^{-1}), differentiating (\Pi^{-1}\Pi=1) gives

\[
(\Pi^{-1})_a=-\Omega_a\Pi^{-1},\quad
(\Pi^{-*})_{\bar a}=-\Pi^{-*}\Omega_a^*,\quad
(\Pi^{-*})_a=(\Pi^{-1})_{\bar a}=0.
\]

These identities yield both SC.u4 derivatives in exactly their stated order. In (Y^*\widetilde G_NY=I^*G_NI), the holomorphic metric term cancels (Y^*\widetilde G_NY_a); their adjoints cancel for the antiholomorphic derivative. The complete original source Gram remains fixed. Replacing (I) by any of the already defined neighboring inclusions gives its own same proof, not a full-determinant substitution. Zero-column and full inclusions have the stated zero normal maps and empty determinant conventions.

## SC.u5–SC.u7: the actual single-primary ideal volumes

The reviewed source SP.1–SP.15 fixes (h(s)=(s-\rho)^m), (n=m+1), (y=s-\rho), and (c=-(-\rho)^n/n). The original primitive is (y^n/n+c), and the Pascal map (P) satisfies (e_s=e_yP). The source proof translates the ordered (s)-contours by (\rho), with cancelling finite junctions and connectors bounded by a polynomial times (e^{-R^n/(n|u|)+O(R^{n-1})}). The radial gamma integral then yields (\Pi_s=e^{c/u}WD(u)P), including each phase (e^{\pi i\beta_b}), power (u^{\beta_b}), and (d_b=n^{\beta_b-1}e^{\pi i\beta_b}\Gamma(\beta_b)).

Every invariant subspace is an ideal because (A=M_s) generates the algebra. In the single-primary algebra its preimage in (\mathbb C[y]) is ((y^r)), with (r=m-p). Its literal (s)-basis inclusion (J_r) has columns (y^r,\ldots,y^{m-1}); therefore each specified inclusion is uniquely (I=J_rC_F), with (C_F) invertible and constant. Since (PJ_r) is the selection of coordinates (r,\ldots,m-1), multiplication gives the full matrix SC.u6.

For selected exponents (a+1,b+1\in\{1,\ldots,n-1\}), adding the zero (j=0) row does not change (W_r^*W_r), and

\[
\sum_{j=0}^{n-1}(\zeta^{-j(a+1)}-1)(\zeta^{j(b+1)}-1)
=n\delta_{ab}+n.
\]

The mixed character sums vanish unless (a=b). Hence (W_r^*W_r=n(I_p+\mathbf1\mathbf1^*)). The rank-one matrix (\mathbf1\mathbf1^*) has eigenvalues (p,0,\ldots,0), giving determinant (n^p(p+1)). Taking determinants of the exact congruence SC.u6 gives

\[
\det H=|\det C_F|^2n^p(p+1)e^{2p\operatorname{Re}(c/u)}
\prod_{b=r}^{m-1}|d_b|^2|u|^{2\beta_b}.
\]

Thus SC.u7 retains the inclusion determinant, the original constant (c), all gamma factors, and the original (G_{N,F}=I^*G_NI) in the comparison matrix (G_{N,F}^{-1}H). Empty products give one for (p=0). Because (D_rC_F) and the scalar exponential are invertible on the branch, the period image is precisely the fixed space (\operatorname{im}W_r); its (u)-normal derivative vanishes. This also follows from the explicit SP.9 identity (PB_hP^{-1}=\operatorname{diag}(\beta_b)), which preserves the selected ideal coordinates. It establishes this vanishing on the stated single-primary (t=0) slice only.

## PC.u1–PC.u3, LC.u1, DC31–DC32: inverse transport and original metrics

For any parameter-independent observation (T:E\to W), the exact inverse derivative proved above gives

\[
\partial_u(T\Pi^{-1})=-T\Omega_u\Pi^{-1}
=T(C_\chi/u^2-B_\chi/u)\Pi^{-1},\qquad
\ker(T\Pi^{-1})=\Pi\ker T.
\]

This proves the new observer derivatives and kernels in PC.u1 and DC31 on their original codomains. Their right inverses are the previously specified coefficient right inverses composed with (\Pi). Fixed quotient/factorization maps commute with this derivative by associativity. No additional invariance under (A_t) is assumed.

PC's critical kernel is the original ideal (E_o) at (k=1); its inclusion therefore meets the SC hypotheses. Substitution (\chi=h) is the exact variable isomorphism PC4, leaving (\upsilon_h) and every inverse-unit map in the critical target untouched. SC.u3 gives PC.u3 directly, and its mixed coefficient is zero because (Z_t(u,0)=0). For each cyclic tensor packet the same argument uses its own polynomial (\chi_{h,k}), inclusion (I_k), and observer (\mathcal C_k). The separate product period form remains the rectangular pullback by the stated weighted (\eta_k).

For (M(u,t)=\Pi A_t\Pi^{-1}), with (A_t) independent of (u), the two product terms give (M_u=\Pi[\Omega_u,A_t]\Pi^{-1}). Substituting (L_t=A_t^2-kA_t) gives the LC.u1 Laplacian derivative with the same commutator order. The metric derivatives are the SC inverse-congruence derivatives with (G=G_N). For (x=\Pi v), the literal equalities

\[
x^*\widetilde Gx=v^*Gv,\qquad
x^*\widetilde G\widetilde L_tx=v^*GL_tv
\]

retain the full original numerical-range quotient and hence the original (E_N(t)) bound pointwise in (u). This does not assert a bound for the Euclidean period-coordinate metric.

For DC32 put (M_b=T_b^*D_\nu T_b), with every actual retained (\nu_n>0). The period-coordinate form is exactly (\Pi^{-*}M_b\Pi^{-1}). Its (u) derivative is (-\Pi^{-*}M_b\Omega_u\Pi^{-1}), and its conjugate derivative is (-\Pi^{-*}\Omega_u^*M_b\Pi^{-1}). The kernel consists of those (x) with (D_\nu^{1/2}T_b\Pi^{-1}x=0), which equals (\Pi K_b) because the retained diagonal weights are strictly positive. The empty sample set gives the zero form and full kernel. These facts retain the shared and new circle terms under the already specified DC28 module map.

## RCX.u1–RCX.u6: ordered jets, forced equation and translation derivatives

The operators (\mathscr D_a=\partial_a+\Omega_a) act on the left on matrices. Their commutator is left multiplication by the XD.u6 curvature. They therefore commute, so their iterates from (I) give a well-defined (Q_{r,s}) independent of the order of (r) (u)- and (s) (t)-steps. If (\partial_u^r\partial_t^s\Pi=\Pi Q_{r,s}), one product differentiation gives (\Pi(\partial_aQ_{r,s}+\Omega_aQ_{r,s})), proving the recursive identity by induction.

Writing the original (C_\chi(t)) and (B_\chi) without changing their order, direct multiplication gives

\[
\Omega_u^2=C_\chi^2/u^4-(C_\chi B_\chi+B_\chi C_\chi)/u^3+B_\chi^2/u^2,
\qquad
\partial_u\Omega_u=2C_\chi/u^3-B_\chi/u^2.
\]

Their sum is the stated (Q_{2,0}). In particular the middle coefficient is (2C_\chi-C_\chi B_\chi-B_\chi C_\chi), with no commutativity assumption. Likewise (\partial_u\Omega_t=A_t/u^2) and (\Omega_u\Omega_t=C_\chi A_t/u^3-B_\chi A_t/u^2), proving the stated (Q_{1,1}) and its multiplication order. The (r=0) recursion is exactly the original RCX30 recursion, retaining its (3R^2/u^2) term for (q=1).

For the full metric (H=\Pi^*\Pi), holomorphy gives (H_a=H\Omega_a) and (H_{\bar a}=\Omega_a^*H). Along the stated differentiable path, including conjugate velocities in the adjoint, this is exactly (\dot H=\Omega_{\rm path}^*H+H\Omega_{\rm path}). Substitution in the original metric-variation identity therefore uses this same full Hermitian matrix.

Differentiating the retained equation (u^2\Pi_{tt}+ku\Pi_t+u\Pi R=\Pi L_t), where (R,L_t) are independent of (u), gives term by term

\[
2u\Pi_{tt}+u^2\Pi_{utt}+k\Pi_t+ku\Pi_{ut}+\Pi R+u\Pi_uR
=\Pi\Omega_uL_t.
\]

This proves RCX.u4 with every forcing term and factor present. Composition with the fixed admitted (j_E) preserves the equation; the separate original Euler commutator is exactly DS74, including its boundary primitive.

Lastly (\psi_a-\psi=p(h_a/u+\overline{h_a/u})) on (u\ne0). The first summand is holomorphic in (u,t), and the second antiholomorphic, so all mixed holomorphic–antiholomorphic derivatives vanish. The pure derivatives are

\[
\partial_u(\psi_a-\psi)=-ph_a/u^2,\quad
\partial_u^2(\psi_a-\psi)=2ph_a/u^3,\quad
\partial_u\partial_t(\psi_a-\psi)=pa/u^2,
\]

using (\partial_th_a=-a). This also checks the changed RCX38 sentence: only the fixed-(u) (t,\bar t) derivatives of total order at least two all vanish. The source no longer extends that assertion incorrectly to pure (u) derivatives.

## Final repair verification and source pins

The repaired DT.16 was read in full at revised source lines 169–203. It now explicitly fixes the specified map to the finite field, the condition p>d=q+1, the original coefficient characteristic and character, the parameter base, both literal projections, the full derived compact-support complexes, and the translation commuting with the projections. Its claimed isomorphism is explicitly in every cohomological degree. The torsor addition and base-character projection argument therefore have precisely defined objects. The previous wording “second line” was also corrected to “character line”. This closes the only reported defect.

Accepted scope: the complete new blocks DS70–74, XD.u1–7 and its following typed cyclic/product paragraph, DT.14–16, SC.u1–7 and their full proofs, PC.u1–3 and its cyclic/product continuation, LC.u1 and its metric/control continuation, DC31–32 with their weighted metric continuation, and RCX.u1–6 together with the adjusted fixed-u derivative scope after RCX38. No unresolved mathematical or object-typing defect was found in those blocks after repair. This statement does not certify unrelated original claims, AP, or the other independently owned boundary modules.

All eight evidence diffs were regenerated in memory from the exact original/revised text using the same unified-diff conventions and matched the retained evidence files. Every original, revised and diff byte SHA-256 is pinned below. No TeX was edited or Lean process launched in this review. The SP dependency pin applies only to the SP.1–SP.15 context actually read, not to an independent audit of that file’s remaining finite-field development.

SP context file `boundary/proofs/SPC_ORIGINAL.tex` SHA-256: `80dcbc843df223a8b65fd92f728deba1b28e540c748e08dabbdf47a6f28958ea`.

| File under boundary | Original SHA-256 | Revised SHA-256 | Evidence diff SHA-256 |
|---|---|---|---|
| `circle_critical_observation_diamond.tex` | `bd4590e5f9013c186e98f9b4ec5d40fe43c6e950ea20cfab4146ecf8cd773d07` | `64757a54de9b90375bed375c412c4e52686193a407058ff3694535568bfee5b3` | `cc606353cbdcece31bc2bda70ef7ed6b8384fd242d88d1a4646fc7f9b6ea9afc` |
| `deligne_exponential_determinant_extension.tex` | `6b6b194714a66be32a27c1fdb7561889a838c6914bb643775d2bc99342776ad8` | `7504884aaee5d6089dc6d515460a24b92c8c801ef9b77d10b729ffddff4cdbcc` | `d9485bf4f300405a65ab7de4f67e2edca5b194f064a55b9f4662d54e5fa1936b` |
| `deligne_split_sidebar.tex` | `af46bd3f3a309d0412c02201b5bd05cfe83d89ea585a12c6d46f20023defc3c1` | `3cc07a8e584b17264134d304366f5636851209396304017d1c4cb17b27e102a0` | `0f31b597b4dd40caca60fb60aaa2fa5f2d2970b6ae40d693f07bbcf459e71930` |
| `deligne_translation_bridge.tex` | `7dc6c73941a3ea30b141e7fb1110d6fb7b688af8a9c79a996acce31f9086611d` | `020876ad24a7ddfe121ca519ea93499e9223c0e9d7b276189bc431c198bace07` | `7694c9154898694a2d00e5dff65f87055918c30069ce779a853bf103cd111114` |
| `period_critical_kernel_bridge.tex` | `9a067d6f5f86ab0cf3d4c27dfe1155e2a155614a3ee2d2a9233ff2473a8eb586` | `61eddb83d32d930e8414cb6ad0bb1020a213511ddbaffd08dd4727a184ba32fe` | `055fe1161e9a427794fa663e53d91d82f449a4a8fd840d57fbc9919ec00ffd51` |
| `period_laplacian_control_bridge.tex` | `1a381ec28ef551f5039a185efd78847bf25f05f74bbe859460eaa53ef557c06a` | `1c47fa05f93360640a34ed11be4260080d7f3a56b3623b33f7a3908806c6a63d` | `e724dba6776c158ec6a2b3ab1d5961dab8c3d9f89d8cf5699e430b750c8fff3a` |
| `residue_constituent_extension.tex` | `9423d1afca6465862a59fc8f1234fe717c284c54bf34237aadfbb01984f3284d` | `e35b3c175434eef0315b0b8763851a5006b283c4d68250729c5dcde8412e3e61` | `448bcdf0c9c6f6dfe2710e67c1776d9144977b833f2bf104327c961d7871d171` |
| `sga_constituent_period_curvature.tex` | `17ee5443095deb79c3f57947bd22b45bc4bdea0dcb78b296001b6286b4eb610f` | `d952fb75bc886ac0838f7508f9f686e3dcafe03543e99cf738723bee9ad6d93c` | `cbc842b50663f85df580781cffbab9c1e3d5fb13a6c6154e8d12cdf91ce38d53` |
