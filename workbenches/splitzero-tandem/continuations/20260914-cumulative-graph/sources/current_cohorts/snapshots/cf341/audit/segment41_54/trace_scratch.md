# Source-only trace and rank-two audit, U0046–U0050

This scratch record belongs to the delegated subtask `/root/purity_program/audit46_50/trace_check`. Only the source file `output/tau_f1_transcript_audit_2026-09-13/sources/audit_segment_U0041_U0054.md`, lines 2482–4891, was inspected. No derivative note, purported published proof, checker report, or attachment was used as mathematical authority. The parent agent maintains the session provenance and writes the final part46_50 artifact. All findings below are deductions from the displayed source identities with their stated objects; referenced analytic results absent from this interval have not thereby been independently proved.

## Source anchors

- A1644, UUID `d448b4f7-00f5-449f-a2b0-43ebd22cc66f`: begins 2514. Original arithmetic function and multiplier: 2547–2574. Full packet algebra and extension unit: 2576–2660. Actual section and derivative extension: 2594–2615, 2664–2718. Reflection, residue, Jacobian and trace: 2866–2925. Finite cochain trace: 2936–2990. Dependency disclosure: 3015.
- A1694, UUID `1fa0ebbc-f569-40c1-b7ac-b523da19a5f0`: begins 3021. Actual spaces and theta: 3049–3073. Global retraction: 3075–3220. Finite change of representatives retains extension/trace: 3459–3495. Full positive representative-form defect: 3554–3584.
- A1721, UUID `40ab7ee4-4dcd-409c-9e0d-f211bc6aecec`: begins 3604. Actual finite source representatives: 3809–3871. Original positive-half-line control identity and bound: 3873–3950. Residue dual map: 3976–4056. Tensor and orbit control: 4058–4142. Algebraic calibrations with explicit non-arithmetic status: 4144–4214. Certification limits: 4236, 4259.
- A1771, UUID `552c8e45-2599-46da-8b95-214fa4d5ce0c`: begins 4275. Homotopy vs representative changes: 4432–4475. Actual arithmetic derivative source: 4477–4510. Nested theta relations, Gram complements: 4512–4590. Unscaled source recurrence and rows: 4626–4686. Rank-two formula: 4688–4725. Metric change: 4727–4733. Original support-layer maps: 4736–4773. Exact two-by-two control formula: 4775–4821. Duality: 4823–4835. Actual numerical source data and limitations: 4837–4882. No uniform small arithmetic excess claimed: 4890.

## 1. Residue unit, Jacobian and trace, including all multiplicities

Retain exactly the source's `g(s)=2 xi(s)`, `h_Z(t)=product_(rho in Z)(t-rho)^(m_rho)`, `E_Z=C[t]/(h_Z)`, and `epsilon_Z=j_(h_Z)(h_Z/g)`. Complete multiplicities mean that, at each rho,

\[
g(\rho+z)=z^{m_\rho}w_\rho(z),\qquad w_\rho(0)\ne0,
\]

and `h_Z/g` is a holomorphic unit on every selected local germ. The arithmetic unit is therefore well defined and invertible in E_Z. It is not the supported-zero scalar e.

For a reflection-stable packet let `iota(rho)=1-conjugate(rho)` and `f^dagger(s)=conjugate(f(1-conjugate(s)))`. Stability with matching multiplicities gives an antilinear involution on E_Z; without stability the domain issue is real, as detailed below. Define

\[
R_h(f,u)=\sum_{\rho\in Z}\operatorname{Res}_{s=\rho}
\frac{f^\dagger(s)u(s)}{h_Z(s)}\,ds.
\]

Then

\[
R_h(f,\epsilon_Zu)=\sum_{\rho\in Z}\operatorname{Res}_{s=\rho}
\frac{f^\dagger(s)u(s)}{g(s)}\,ds=\mathscr R_Z(f,u).
\]

Indeed, for any polynomial representative e(s) of epsilon_Z, `e(s)-h_Z(s)/g(s)` is divisible by h_Z in each local germ. Dividing that difference by h_Z introduces no pole, and hence changes none of the displayed residues.

For `J_g=M_(j_h g')`,

\[
\mathscr R_Z(f,J_gu)
=\sum_{\rho\in Z}\operatorname{Res}_{\rho}
f^\dagger(s)u(s)\frac{g'(s)}{g(s)}\,ds
=\sum_{\rho\in Z}m_\rho\overline{f(\iota\rho)}u(\rho).
\]

The last equality follows from the full local formula `g'/g=m_rho/z+w'_rho/w_rho`. On `C[z]/(z^(m_rho))`, multiplication by any a has every diagonal entry equal to a(0), in the unchanged ordered basis `1,z,...,z^(m_rho-1)`. Its trace is `m_rho a(0)`. Thus the last display equals `Tr(M_(f^dagger u)|E_Z)`, with exactly the source's multiplicities and factor 2.

The uncontracted residue form is nondegenerate. To prove this, take a nonzero local class a whose first nonzero coefficient has degree k<m. Multiply it by `z^(m-1-k)` and a nonzero scalar if needed: the residue against `1/(z^m w(z))` is nonzero. CRT permits this test on just that local summand. The dagger involution is bijective, so either argument is nondegenerate. This establishes an actual duality rather than positivity.

The Jacobian contraction has an exact radical. In the rho summand,

\[
j_{z^{m_\rho}}g'=m_\rho w_\rho(0)z^{m_\rho-1}.
\]

For m=1 this is a unit; for m>1 its multiplication kernel is the ideal (z). Consequently

\[
\ker J_g=\operatorname{Nil}(E_Z),\qquad
\operatorname{rad}\mathscr Q_Z=\operatorname{Nil}(E_Z),
\quad \mathscr Q_Z(f,u)=\mathscr R_Z(f,J_gu).
\]

This proves the exact relation to the reduced algebra: `mathscr Q_Z` is the pullback under `E_Z -> product_rho C` of the weighted reflection pairing. If c roots are fixed by iota and p two-element iota-orbits occur, then its inertia is `(c+p,p,d-c-2p)`, where `d=deg h_Z`; the last entry is `sum_rho(m_rho-1)`. On a fixed root the block is `(m_rho)`. On an orbit `{rho,iota rho}` the block is exactly `[[0,m_rho],[m_rho,0]]`, with m_(iota rho)=m_rho. These are statements about this specified trace form, not a proof that all actual roots are fixed.

### The missing hypothesis in later shorthand

A1644 explicitly says reflection-stable packet at lines 2868–2873. A1721 first allows an actual finite packet at 3809–3815 and then writes a residue self-duality at 3978–4010 without restating that restriction. A1771 inherits the same issue at 4823–4835. A self-pairing on E_Z and `S_Z^*=-S_Z` require reflection stability and matching full multiplicities.

For an arbitrary packet the correct exact morphism still exists: dagger is an antilinear isomorphism `E_(iota Z) -> E_Z`, and

\[
E_Z\longrightarrow E_{\iota Z}^{\#}\otimes\mathcal L_1,
\quad u\longmapsto\bigl(f\longmapsto
\sum_{\rho\in Z}\operatorname{Res}_{\rho}(f^\dagger u/g)\,ds\bigr)
\]

is an isomorphism. Its matrix S satisfies

\[
A_{\iota Z}^*S+SA_Z=S.
\]

This follows term by term from `(t f)^dagger=(1-t)f^dagger`. Thus the exact duality for an arbitrary packet relates the two reflected packet spaces; it does not fail altogether. For a stable packet the spaces coincide, yielding the source's identity. Using `g^dagger=g`, reflection changes the residue sign, giving `S^*=-S`; the extra Jacobian satisfies `J_g^*S=-SJ_g`, hence `SJ_g` is Hermitian, as is independently evident from the weighted reflection trace above.

## 2. Positive metric control and duality are algebraically correct

Retain `D=-x d/dx` on `L^2((0,infinity),dx)`, the actual representative R with `J_ZR=1`, `A=M_t`, and `B=DR-RA`. Set `G=R^*R` and `W=-(R^*B+B^*R)`. The source's decay gives

\[
\langle DF,H\rangle+\langle F,DH\rangle=\langle F,H\rangle.
\]

Since R is injective, G is strictly positive. Substitution gives, in the original packet coordinates,

\[
W=A^*G+GA-G.
\]

No cohomological vanishing of B implies that its cross pairings vanish. The retained measure dx is precisely responsible for the coefficient 1. The even-extension norm is twice the positive-half-line squared norm, as stated at 3884–3886.

For stable Z and nondegenerate S, `G^D=S^*G^(-1)S` is positive. From `A^*S+SA=S` one obtains

\[
A^*G^{\mathrm D}+G^{\mathrm D}A-G^{\mathrm D}
=-S^*G^{-1}WG^{-1}S.
\]

One explicit multiplication proof uses `SA=(I-A^*)S` and its adjoint `A^*S^*=S^*(I-A)`; the left side is `S^*[G^(-1)-AG^(-1)-G^(-1)A^*]S`, which is the right side. Therefore upper control transfers to lower control on the dual metric; it supplies no numerical smallness by itself.

The tensor and orbit identities at 4090–4139 are valid differentiation identities. On a retained eigenvector of A of eigenvalue rho, any positive metric satisfying the original control identity obeys

\[
\frac{v^*Wv}{v^*Gv}=2\Re\rho-1.
\]

An orbit window cannot reduce this quantity. The source's nilpotent calibration is also exact: with its original `A=[[1/2,1],[0,1/2]]` and G=I, the displayed G_T and W_T have determinant equation

\[
\det(W_T-\lambda G_T)
=T^2\bigl((1+T^2/12)\lambda^2-1\bigr).
\]

Thus its generalized eigenvalues are exactly those printed at 4183–4187. This calibration concerns retained nilpotent growth and does not evaluate an arithmetic packet bound.

## 3. The rank-two formula genuinely uses the arithmetic source

The source is not an arbitrary model matrix: `phi_*=(4 pi^2 x^4-6 pi x^2)e^(-pi x^2)`, `f_0=Theta phi_*`, `M f_0=2 xi`, `f_j=D^j f_0`, and the actual finite section satisfies

\[
Ds_Z-s_ZA=f_0\ell_Z,
\]

with the full extension functional `ell_Z`; for one simple zero it is `1/(2 xi'(rho))`. These exact constants enter the row recurrence and must not be replaced.

All f_j are linearly independent because the Mellin transform of a dependence is `2 xi(s)P(s)=0`; the entire function `2 xi` is not identically zero. The Gram matrices H_n and projections P_n at 4531–4540 are therefore defined, and `R_n=(1-P_n)s_Z` retains both `qR_n=sigma_Z` and `J_ZR_n=1`.

The unscaled Gram-Schmidt vectors u_n are real functions with coefficient one on f_n. Reality is essential to justify the full diagonal coefficient 1/2 from integration by parts, which alone gives its real part. For k<n-1, the coefficient of u_k in Du_n vanishes because

\[
\langle u_k,Du_n\rangle
=\langle u_k,u_n\rangle-\langle Du_k,u_n\rangle=0.
\]

The coefficient on u_(n+1) is 1 by the unchanged leading coefficient. Reality and the integration identity give 1/2 on u_n. The coefficient on u_(n-1) is `-h_n/h_(n-1)` by applying the same identity to u_(n-1),u_n. This proves the recurrence in 4646–4661 with every h_n retained.

Pairing `Ds_Z=s_ZA+u_0 ell_Z` against u_n gives exactly

\[
\frac{\mathfrak h_{n+1}}{\mathfrak h_n}r_{n+1}
=r_n(\tfrac12 I-A)+r_{n-1}-\mathbf1_{n=0}\ell_Z,
\qquad r_{-1}=0,
\]

for the source's `r_n=h_n^(-1)u_n^*s_Z`. In particular the extension functional is not absent from the estimate.

The source proof of

\[
W_n=\mathfrak h_{n+1}
(r_{n+1}^*r_n+r_n^*r_{n+1})
\]

is correct: in `Theta K_n=f_0 ell_Z-DP_ns_Z+P_ns_ZA`, the first and third terms are orthogonal to R_n; the component of `DP_ns_Z` outside L_n is precisely `u_(n+1)r_n`. Pairing it with R_n supplies the displayed h_(n+1)r_(n+1) factor. Likewise orthogonal removal of that component proves

\[
G_n-G_{n+1}=\mathfrak h_{n+1}r_{n+1}^*r_{n+1}.
\]

At the original relation level, `D` maps `Q_(V_n)` to `Q_(V_(n+1))`, and the retained derivative defect is `-[u_(n+1)]r_n(v)` before transport. The exact relation-layer isomorphism `[z] -> (1-P_n)z` in 4760–4768 identifies its amplitude with the one-dimensional orthogonal layer. These are actual maps; they do not make the Hilbert cross pairing vanish.

## 4. New exact invariant trace and packet-mass obstruction

This section is a new deduction, not a claim quoted from the transcript.

Fix n. Write d=deg h_Z and retain all original matrices. Define the endomorphism `L_n=G_n^(-1)W_n`; it is self-adjoint for the positive inner product with Gram matrix G_n. Cyclicity of trace gives

\[
\operatorname{Tr}L_n
=\operatorname{Tr}(G_n^{-1}A^*G_n)+\operatorname{Tr}A-d
=2\Re\operatorname{Tr}A-d
=\sum_{\rho\in Z}m_\rho(2\Re\rho-1).
\tag{T}
\]

The rank-two expression independently gives

\[
\operatorname{Tr}L_n=2\mathfrak h_{n+1}\Re\mathsf c_n,
\qquad \mathsf c_n=r_nG_n^{-1}r_{n+1}^*.
\tag{C}
\]

Thus this real part is an invariant spectral trace divided by the unchanged h_(n+1), not a freely tunable metric quantity.

For a reflection-stable packet, full multiplicities pair under rho -> 1-conjugate(rho); the right side of (T) vanishes. Hence `Re c_n=0` for every n. The source's exact least excess becomes

\[
\epsilon_n=\mathfrak h_{n+1}
\sqrt{\mathsf a_n\mathsf b_n-(\Im\mathsf c_n)^2},
\]

and its nonzero generalized eigenvalues are `+epsilon_n,-epsilon_n`, unless both vanish. No matrix, metric, coordinate, unit or representative has been replaced in this computation.

There is a stronger obstruction retaining every off-centre root's multiplicity. Let E_+ be the direct sum of the original CRT generalized eigenspaces with `Re rho>1/2`. Choose any full-column-rank injection I_+ whose image is E_+, with `AI_+=I_+A_+`. Define in the original coordinates

\[
G_+=I_+^*G_nI_+,
\qquad P_+=I_+G_+^{-1}I_+^*G_n.
\]

Then P_+ is the G_n-orthogonal projection onto E_+, because `P_+^2=P_+`, `im P_+=im I_+`, and `P_+^*G_n=G_nP_+`. Exact compression gives

\[
\begin{aligned}
\operatorname{Tr}(P_+L_n)
&=\operatorname{Tr}(G_+^{-1}I_+^*W_nI_+)\\
&=\operatorname{Tr}(G_+^{-1}(A_+^*G_++G_+A_+-G_+))\\
&=2\sum_{\Re\rho>1/2}m_\rho(\Re\rho-1/2).
\end{aligned}
\tag{P}
\]

The rank-two expression factors the Hermitian form through the two-dimensional exchange form `h_(n+1)[[0,1],[1,0]]`. Therefore L_n has at most one strictly positive eigenvalue lambda_+ and at most one strictly negative eigenvalue lambda_-; missing eigenvalues are assigned 0 for the following inequalities. If v is a nonzero eigenvector for either nonzero eigenvalue, its spectral projection is

\[
E_v=v(v^*G_nv)^{-1}v^*G_n.
\]

For every G_n-orthogonal projection P,

\[
0\le\operatorname{Tr}(PE_v)
=\frac{v^*G_nPv}{v^*G_nv}\le1.
\]

Consequently `Tr(P_+L_n)<=lambda_+`. Repeating the construction on the invariant CRT sum E_- for `Re rho<1/2` gives `Tr(P_-L_n)>=lambda_-`. In combination with (P),

\[
\lambda_+\ge2\sum_{\Re\rho>1/2}m_\rho(\Re\rho-1/2),
\qquad
-\lambda_-\ge2\sum_{\Re\rho<1/2}m_\rho(1/2-\Re\rho).
\tag{M}
\]

For a reflection-stable packet `lambda_+=-lambda_-=epsilon_n`, while the two sums on the right are equal. Therefore the exact arithmetic rank-two construction satisfies, for every n,

\[
\boxed{\epsilon_n\ge
\sum_{\rho\in Z}m_\rho\lvert\Re\rho-\tfrac12\rvert.}
\tag{R}
\]

This is stronger than the individual eigenline lower bound. It preserves nilpotent multiplicities because E_+,E_- include the complete generalized eigenspaces. Counterfactually, any fixed reflection-stable packet containing an off-centre root imposes this strictly positive n-independent floor on the displayed actual control errors. Increasing the source relation level alone cannot evade it. Conversely, no smallness of these errors is supplied by this derivation or by the source interval, so (R) proves no location claim for actual zeros.

## 5. Exact limits of this interval's evidence

The source interval gives enough algebra to verify the displayed identities above, including actual constants and source maps. The range theorem, existence and full analytic properties of s_Z, complete analytic estimates behind the global retraction, and purported checker/publication contents are partly cited to external files not included in this inspection. Their mention is not an independent proof here. The numeric theta norm values at 4870–4873 and integer-tail value at 4879 are reported with an explicit rounding limitation at 4882; no certified arithmetic G_n inverse or uniform relative excess is thereby supplied. The source itself disclaims a uniform estimate at 4259 and 4890.

## Follow-up QA of the parent proof, part46_50.md lines 481–634

The invariant-subspace and multiplicity proof is mathematically valid as written. Recommended explicit TeX conventions: handle the empty packet separately (all sums, spaces, projections, control endomorphisms and excess are zero); use P_±=0 directly when E_±=0, avoiding an unnecessary inverse display on a zero-dimensional space; set Π_±=0 when its corresponding nonzero eigenvalue is absent; state tensor k≥1. The statement that the control has exactly one positive and one negative eigenvalue requires a reflection-stable packet containing an off-centre root. For an arbitrary packet, only the separate positive and negative mass bounds hold, and a one-sided packet can have rank-one semidefinite control. These recommendations were sent to the parent. The TeX file had not yet been written at the latest read-only check.

### Completed TeX module QA

Read `multiplicity_boundary_floor.tex` in full, lines 1–836, without editing it. The original constants, recurrences, factor maps, invariant trace, full multiplicity projection argument, reflected-packet inequality, pair/quartet coefficients and tensor Rayleigh identity are correct. Automated reference inventory found 47 BF labels and all 41 equation tags BF.01–BF.41, with no undefined references, duplicate labels or missing tags. Two minor notation recommendations were sent: qualify BF.29 for nonzero E_± and specify that the zero-dimensional extension of BF.30 concerns its first/last expressions; define the Fourier convention and the domains of L, d_leg and gamma in the homotopy paragraph. Empty packets, missing spectral projections, reflected multiplicities and k≥1 are otherwise handled explicitly. No module edits made.
