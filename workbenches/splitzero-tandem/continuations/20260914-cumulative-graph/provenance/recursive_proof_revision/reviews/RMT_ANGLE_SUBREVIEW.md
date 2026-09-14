# Bounded RMT angle and strict-positivity review

Date: 2026-09-13. Source edits: none. This receipt records the independently assigned subreview of RMT11–RMT12; the parent review owns the complete RMT audit and the root continuity records.

Final status: accepted after the root's source correction. The corrected source was reread at SHA-256 `034C7B72C44A02C2874E634124B94615575948203BB14FCDB3E5284F53F80E1B`. Its lines 141–170 now retain both full q-angle lists, explicitly designate φ₁=0, define each of the 2q−1 remaining scalar costs, and display the exact identity B=0+Σλ. RMT11 now explicitly contains sinφ₁=0 before the Jensen bound. The issue described below is resolved in this revision. The strict-positivity argument at corrected lines 172–201 is accepted, including the actual positive atomic comparison. No further correction within this bounded scope is required. The earlier source hash, line numbers, finding, and suggested repair below are retained as the review history.

Assigned scope, verbatim: “Independent bounded check alongside my full RMT review. Read workspace:/work/backpropagation_20260913/recursive_metric_transport.tex RMT11–12 and locate full EP17–EP25 angle theorem source (likely work/tau_actual_geometry/current or rg files under work). Verify crossed quotient pairs (q−1,2q),(q,2q−1), count 2q−1 incl forced zero, exact sum B, and B>0 argument for any actual positive measure on S=k/2+iy with positive degree2q moment Gram including atomic. Do not edit source; report precise source path/line and correction if needed. No broad research. My root task is independent full RMT review; you can write a small receipt under work/backpropagation_20260913/reviews/RMT_ANGLE_SUBREVIEW.md if useful.”

## Sources and findings

1. `work/backpropagation_20260913/recursive_metric_transport.tex`, SHA-256 `9F1B8704F428F347F29FC6FCA31C96135E3F70EB546BC40D389DE721CC6E25CF`: lines 141–157 contain the angle statement and RMT11; lines 159–188 contain the closed strict-positivity proof and RMT12.
2. `work/cumulative_addendum_20260913_v22/portable_g0ijpdcf/Tau_Actual_Source_and_Metric_Addendum_2026-09-13/proofs/EP.tex`, SHA-256 `1BA57290C995ABCAA57840C5A873E767174B21BC5B19525DF004F58C0BCA1448`: lines 218–245 prove the section relation, exact cross Gram, principal projection blocks, determinant identity, and gap rank bound; lines 247–263 give the crossed specialization and explicitly separate one forced zero scalar contribution; lines 285–367 give EP17–EP25 in full; lines 419–426 give the reflected-polynomial strictness proof.
3. `work/actual_tau_cumulative_conversion_20260913/build/all_degree_angle_review/endpoint_all_degree_angle_review_source.tex`, SHA-256 `CA5D89DCC1644461F1D1C23A1195C0902C35663CBD037882EF88E7098357DEB8`: lines 55–171 prove AA6–AA16; lines 173–214 prove the full count, common hyperplane, and scalar separation; lines 229–275 prove the spectral trace and concavity estimate; lines 279–318 prove strict positivity.

The numerical coefficient and inequality in the initially reviewed RMT11 are correct. The wording at initial RMT lines 143–157 required correction: both complete principal-angle lists have length q, so their complete union has length 2q. The guaranteed zero in the second list permits a scalar sum of length 2q−1 after that distinguished zero is separately recorded. An a=2q−1 list cannot itself be the union of the two complete lists with every zero entry retained. AA lines 183, 207–214 and EP line 263 state this distinction precisely. The initial RMT sentence “No angle, zero mode or original mass is removed” obscured the exact scalar separation required by its coefficient.

## Complete pointwise derivation in the original source

Fix q≥1, the original monic degree-q polynomial χ, and the positive moment Gram M on H=P_{2q}. For each q−1≤N≤2q let R_N:E→H be the canonical minimum section of the original monic-remainder map, with image K_N=P_N∩(χP_{N−q})^⊥, where E=C[S]/(χ). All inclusions, orthogonal complements, and inner products use M and the original coefficient frame. The exact sequence implies dim K_N=q. Let Π_N be the M-orthogonal projection onto K_N, G_N=R_N* M R_N, and V_N=det G_N.

For i≤j, R_i−R_j has zero remainder and belongs to χP_{j−q}; the image of R_j is orthogonal to that space. Consequently R_j=Π_jR_i, R_i*MR_j=G_j, and

\[
G_i-G_j=(R_i-R_j)^*M(R_i-R_j)\succeq0.
\]

The isometries F_i=R_iG_i^{-1/2} and F_j=R_jG_j^{-1/2} have cross matrix F_i*MF_j=G_i^{-1/2}G_j^{1/2}. Its product with its adjoint, in that order, is A_{ij}=G_i^{-1/2}G_jG_i^{-1/2}. Thus 0<A_{ij}≤I. Write its q positive eigenvalues as cos²θ_b, including multiplicity and unit eigenvalues, where 0≤θ_b<π/2. Taking its determinant gives

\[
\log(V_i/V_j)=\sum_{b=1}^q-\log\cos^2\theta_b.
\]

To identify every zero angle, choose an orthonormal eigenbasis v_b of A_{ij}, put x_b=F_iv_b and y_b=Π_jx_b/cosθ_b. Projection and the eigenvalue equation give ⟨x_b,x_c⟩=⟨y_b,y_c⟩=δ_bc and ⟨x_b,y_c⟩=cosθ_c δ_bc. A unit cosine means the projection preserves the norm of x_b, so x_b=y_b lies in K_i∩K_j. Conversely every vector of that intersection is fixed by the projection restriction and gives a unit eigenvalue. Hence zero-angle multiplicity equals dim(K_i∩K_j).

Apply this to the original pairs (q−1,2q) and (q,2q−1). For q=1 the second pair is (1,1), so the ordering still holds. Write their complete lists as α_1,…,α_q and β_1,…,β_q. Both K_q and K_{2q−1} lie in L=P_{2q−1}∩(χP_0)^⊥. The nonzero vector χ belongs to P_{2q−1} for every q≥1. Positivity of M makes orthogonality to its line a single nonzero equation, so dim L=2q−1. Therefore

\[
\dim(K_q\cap K_{2q-1})
=2q-\dim(K_q+K_{2q-1})\ge1.
\]

Relabel one guaranteed zero angle as β_1=0. The exact four-volume sum is

\[
\mathcal B
=\sum_{b=1}^q-\log\cos^2\alpha_b
 +\sum_{b=1}^q-\log\cos^2\beta_b
=0+\sum_{\nu=1}^{2q-1}\lambda_\nu,
\]

where the λ-list consists of every α-cost and the β-costs with indices 2,…,q. This list retains any additional zero costs. The separately displayed zero is the original β_1 cost; neither geometric space nor its common vector has been changed. No continuous choice of that common vector is necessary for a pointwise symmetric estimate.

For an angle θ_b>0, define z_b=(y_b−cosθ_b x_b)/sinθ_b. The displayed inner products show that the (x_b,z_b) planes are orthonormal and mutually orthogonal. The projection difference on each plane is

\[
\begin{pmatrix}
\sin^2\theta_b&-\sin\theta_b\cos\theta_b\\
-\sin\theta_b\cos\theta_b&-\sin^2\theta_b
\end{pmatrix},
\]

with eigenvalues ±sinθ_b. The projection difference is zero on common vectors and on the orthogonal complement of K_i+K_j. Thus for self-adjoint C with extreme eigenvalues c_min,c_max, each pair of orthonormal signed eigenvectors contributes sinθ_b times a difference of two Rayleigh quotients, whose absolute value is at most sinθ_b(c_max−c_min). The exact crossed trace signs in RMT7 then give

\[
|\mathcal B'|
\le d_x\left(\sum_{b=1}^q\sin\alpha_b+\sum_{b=1}^q\sin\beta_b\right)
=d_x\sum_{\nu=1}^{2q-1}\sqrt{1-e^{-\lambda_\nu}}.
\]

For f(z)=sqrt(1−e^{−z}), differentiation on z>0 gives f''(z)=−e^{−z}(2−e^{−z})/[4(1−e^{−z})^{3/2}]<0. Concavity extends to z=0 by continuity. Applying finite Jensen to the entire retained (2q−1)-slot λ-list therefore gives precisely RMT11. This proves its constant also at q=1, when the λ-list has one slot and Jensen is equality.

## Strict positivity for every admitted positive measure, including atomic measures

Let μ be any positive measure on the literal line S=k/2+iy for which the moment form M on P_{2q} is finite and positive definite. The preceding argument gives both crossed ratios at least one. If B=0, each logarithmic ratio is zero. For the first pair, G_{q−1}−G_{2q}≥0, so all eigenvalues of G_{2q}^{−1/2}G_{q−1}G_{2q}^{−1/2} are at least one. Their product is V_{q−1}/V_{2q}=1, so all equal one. Hence G_{q−1}=G_{2q}, and the exact positive squared-norm identity forces R_{q−1}=R_{2q} as maps into H.

The first section is literal remainder inclusion. In particular its value on [1] is the original constant polynomial 1. Consequently 1 belongs to K_{2q} and is orthogonal to χP_q. Write χ(S)=Σ_{j=0}^q a_jS^j with a_q=1 and define χ^{#_k}(S)=Σ_{j=0}^q conjugate(a_j)(k−S)^j. This polynomial has degree q and leading coefficient (−1)^q. On the original line, conjugate(S)=k−S, so χ^{#_k}(S)=conjugate(χ(S)). Its product with χ belongs to χP_q⊂P_{2q}. Orthogonality to 1 gives

\[
0=\langle1,\chi\chi^{\#_k}\rangle_M
=\int\chi(S)\chi^{\#_k}(S)\,d\mu
=\int|\chi(S)|^2\,d\mu
=\langle\chi,\chi\rangle_M>0.
\]

The last strict inequality uses positive definiteness and the nonzero original χ. Finiteness follows from the admitted finite moment Gram; equivalently the product is in P_{2q} and its pairing with 1 is defined. No density, absence of atoms, support interval, or almost-everywhere positivity hypothesis was used. The same proof therefore covers positive atomic measures with this positive degree-2q Gram. Applied separately to every convex-path measure μ_x, it gives B(x)>0 on the entire closed path, as RMT12 asserts.

## Suggested precise source correction

Replace RMT lines 141–157 by a passage displaying both full q-angle lists and their 2q-term sum, then display β_1=0 and B=0+Σ_{ν=1}^{2q−1}λ_ν. State that the λ-list contains all other costs, including any further zeros, and that Jensen applies to these 2q−1 scalar slots. Preserve the zero-angle common subspace in the full geometric list and remove the contradictory claim that no zero scalar entry was separated from that list. The inequality, subsequent a=2q−1 formulas, and RMT12 require no mathematical change.
