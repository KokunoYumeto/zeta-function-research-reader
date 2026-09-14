# Bounded full-read transcript audit: lines 2401–4802

Source: `output/tau_f1_transcript_audit_2026-09-13/sources/audit_segment_U0055_U0067.md`.

**Coverage:** Read every line in the assigned range, inclusively, in these sequential, untruncated tool-output chunks: 2401–2700, 2701–3000, 3001–3300, 3301–3600, 3601–3900, 3901–4200, 4201–4500, 4501–4802. No search-only substitute was used. This is a transcript-evidence audit, not an independent proof audit; no arithmetic/Gamma/interpolation calculation was redone.

**Boundary limitation:** Line 2401 begins with a closing display delimiter inside an earlier assistant response. Definitions and hypotheses introduced before 2401—including the reference gamma density, its mass constant, the polynomial convention, and that response's original §1 arithmetic maps—were not read in this lane. Claims below retain this limitation and do not infer additional content from the missing beginning. The report ends at line 4802, after the relation-moment continuation's final paragraph.

## User input actually present in this range

- U0059, lines 2939–2941, verbatim: “the formalization session has been working - including a check for delignes work again (which you have in workspace I think latex) - continue pushing through ”. This requests continuing the work with awareness of the parallel formalization and another Deligne check.
- U0060, lines 3527–3529, verbatim: “alright nice work keep it up”. This requests continuation.
- U0061, lines 4173–4175, verbatim: “on the matter the othjer ones work too so cotinue with thsk work”. This requests continuation while other work proceeds.

There is no new explicit user exclusion, normalization permission, replacement-metric permission, upload direction, or permission gate in the assigned range. The detailed preservation restrictions below are recorded in assistant mathematics, rather than quoted as new user instructions. Historical text is evidence of intent, not a replacement for current higher-priority instructions.

## Original objects and exact morphisms retained

1. The tensor coordinate remains the sum `u=t_1+...+t_k`, with arithmetic coordinate `S=k/2+iu`; the auxiliary reference parameter `k lambda` does not replace arithmetic weight `k` (2409–2418).
2. The gamma sum-coordinate inclusion `U_Sigma f(t)=f(sum t_i)` and its explicit fibre-integral adjoint `C_Sigma` satisfy `C_Sigma U_Sigma=1`. The splitting retains the entire normal part `ker C_Sigma`; its inverse is `(f,n) -> U_Sigma f+n`. A normal component reaches its own supported zero while its retained complement remains available (2420–2483). The transcript gives the exact polynomial projection coefficients and residual squared norms, including factorials, at 2485–2526.
3. The actual complex multiplier is `A_{h,lambda}=v_h(1/2+it)/Gamma(lambda+it/2)`, with `B=|A|^2`, and the unchanged measure satisfies `w_h=B r_lambda` and `m_{h,k}=w_h^{*k}=r_{lambda,k} C_Sigma(B^{tensor k})`. The complex phase stays in the Mellin image; the calculation does not replace its jet map or unit (2528–2572).
4. The repeated preserved source is `C_+=[V ->Theta B]`, `Q=B/Theta V`, `D=-x partial_x`, `g=2 xi`, `h(s)=product(s-rho)^{m_rho}`, and `v_h=g/h`. Its norm is exactly `integral |P(k/2+iu)|^2 m_{h,k}(u) du`, with literal mass `mu_h^k`. The observation is `J^(k) V_{h,k}=eta_{h,k} pi_chi`, where `eta[P]=upsilon_h^{tensor k}P(A_k)1` and `upsilon_h=j_h(g/h)` (2989–3079; 3561–3631). Full Taylor units, nilpotent jets, the infinite arithmetic target, the supported scalar `e=0^bullet`, and external absence `tau` remain attached.
5. The leading-coefficient quotient `P_n/P_{n-1}` defining the monic norm is related to the arithmetic quotient by the displayed exact sequence with multiplication by the same monic `chi`; these two quotients are not identified without their map (3063–3079).

## Gamma comparison and its precisely limited consequence

- At `lambda=1/4`, the complete amplitude includes `-pi^(-1/4)(t^2+1/4) exp(-it log(pi)/2) zeta(1/2+it)/h(1/2+it)`. For fixed `h`, degree `d>=3`, the response defines `T_h=max(1,2 max_rho |rho-1/2|)` and a finite constant
  `C_h=max{sup_{|t|<=T_h}|A|^2, (25*2^(2d)/sqrt(pi))*T_h^(6-2d)}` (2574–2624).
- It states `0<B_{h,1/4;k}(u)<=C_h^k` for `k>=2`, hence `m_{h,k}<=C_h^k r_{1/4,k}`. A full nonreal quartet has degree `4m>=4`. Smaller degrees use the explicit gamma-shift amplitude with `L>=max(0,3-d)` while retaining the identical original `w_h` (2624–2647).
- For the empty seed `h=1`, the bounded reference gives `B_{1,13/4}<=1024/sqrt(pi)`. Its analytic source is nonzero, but its finite arithmetic quotient is zero (2649–2655).
- Actual expansion coefficients are defined by integrals of `w_h`. The generating series is coefficientwise formal: no radius of convergence is assumed. The displayed tensor expansion is in its stated `L^2` space. The original degree-`N` source and relation Grams are determined by coefficients through `2N` at every `k`; the normal density residual has its full norm retained (2657–2753).
- The source/relation determinant corrections yield `V_N=V_N^Gamma T_N`, an actual representative correction in the original relation space, and `G_N <= C_h^k G_N^Gamma`, `0<T_N<=C_h^(kq)` (2755–2833). Here this gamma-envelope `C_h` must not silently be conflated with the later norm-window constant having the same printed symbol.
- The recurrence correction `Q_N=X_{N+2}X_N/X_{N+1}^2`, the ratio `T_{N-1}/T_{N+1}`, and the unchanged reference relation determinant containing `chi` remain in the allowance bound. **A one-sided bound on each `T_N` does not control its consecutive ratio; gamma comparison alone claims no subcubic upper estimate** (2835–2891).
- The actual-moment tail bound has `a,b>0`, `a+b<pi/2`, integer `r>=0`, `T>=0`, and retains `2 C_h^k c_lambda^k r! a^(-r) exp(-bT) cos(a+b)^(-2k lambda)`. Compact quadrature still requires a validated enclosure; displayed seed values are numerical, not interval certificates. A negative fourth expansion coefficient is explicitly retained (2893–2927).

## Actual arithmetic norm bound and corrected four-volume threshold

- The endpoint continuation states, for **fixed packet `h` retaining all selected zero orders**, `(omega_{h,k,2n}/omega_{h,k,n})^(1/(2n)) <= C_h n` for `n>=k>=3`. The constant is independent of `n,k`, and its quartet-window use is `q_k<=N<2q_k` (2953–2981).
- Its stated analytic route is a local zeta mass bound with exponent **42** on every real centre `T` (3081–3167), then the actual density envelope with `B_h=42+2 deg h` and
  `m_{h,k}(u)>=c_h vartheta_h^(k-3) exp[-pi(|u|+k-3)/2] (1+|u|+k-3)^(-B_h)`, `k>=3` (3169–3219). The original entire identity `g=h v_h` handles selected centres. Restriction to a positive contribution does not change or normalize the measure.
- The upper estimate uses fixed `0<b<pi/2`, both original Laplace values `M_h(±b)`, and trial `(S-k/2)^j`; the operator remains multiplication by `S`. The lower estimate retains the exact monic Legendre norm and phase `i^n`. The finite ratio bound is displayed at 3221–3279. The continuation does not present its sufficient constant as numerically certified (3282–3300).
- The earlier endpoint theorem retains its phase/volume structure, two telescopes, and zero-contraction case, selecting an existing canonical metric (3302–3329). For a packet **consisting exactly of** `1/2 ± delta ± i gamma`, `delta,gamma>0`, with common multiplicity `m`, it uses
  `q_k=[1+k(m-1)](k+1)^2`,
  `L_{h,k}=2 delta [1+k(m-1)](k+1) floor((k+1)^2/4)`
  and `L_{h,k}/q_k>=delta k/2` (3331–3352).
- The resulting earlier threshold is `B_{h,k}>=2q_k arsinh(delta k/(2C_h))`, hence `liminf B_{h,k}/(q_k log k)>=2`. It explicitly claims **no** contradictory upper estimate (3354–3395).
- **This threshold is subsequently strengthened to four in the same assigned range.** The updated input is the consecutive identity
  `(epsilon_N^2+phi_N^2) Lambda_N = Lambda_{N+1}(1-delta_N)(1-delta_{N+1})`,
  `Lambda_N=omega_N/V_N`, `delta_N=V_N/V_{N-1}` (4202–4217).
  The phase is retained. The first admitted degree `N=q-1` has a separate source identity; no inverse at degree `q-2` is introduced (4218). For the exact quartet packet, the stated inherited result is separately
  `log(V_q/V_{2q})>=2q log(D_h k)` and
  `log(V_{q-1}/V_{2q-1})>=2q log(D_h k)` (4220–4228).
  Thus “two” is an earlier weaker bound, not the current strongest threshold within this range. This lane does not supply the definition of the inherited positive `D_h` from its referenced attachment.

## Exact relation/restriction maps and finite certificates

- The full-jet update `K_j=K_i+F Omega^(-1)F*` gives `V_i/V_j=det(I+Omega^(-1)F*G_i F)`. The actual relation map `bfrak=T_new-R_iF` has Gram `Omega+F*G_iF`; its representative corrections are original theta boundaries reaching the receiving fibre's supported zero (3399–3503).
- With original monic coordinates, `K_N=B_N O_N^(-1)B_N*`, `G_N=K_N^(-1)`, `R_N=O_N^(-1)B_N*G_N`, `omega_0=mu_h^k`. Source inclusion gives the contraction `I_{i,j}` and metric adjoint `T_{i,j}=K_iG_j`; the transcript proves `L R_i T=P R_j` and `T_{i,j}T_{j,l}=T_{i,l}` (3633–3742).
- The action defect is explicitly `A T-T A=H_i T-T H_j`, with `H_N=G_N^(-1)(A*G_N+G_N A-kG_N)`. Restriction eigenspaces are **not presumed invariant under `A`** (3744–3776).
- The difference of representatives is an actual `chi P_{j-q}` relation and has Gram `G_i-G_j` (3778–3831). Return eigenvalues `0<g_a<=1` are squared singular values, and `log(V_i/V_j)=-sum log(g_a)` (3833–3897).
- From the earlier threshold at least one of the two blocks' `2q_k` eigenvalues has `g_a<=exp[-arsinh(delta k/(2C_h))]`. For its eigenvector, the retained and complementary source fractions are exactly `g_a` and `1-g_a`. Its earlier arithmetic coordinate is `g_av`, so recovering `v` uses `T^(-1)`; its arithmetic class survives. **The implication has no converse** because nilpotent/metric effects can also cause restriction loss (3901–3933).
- A positive Cauchy–Binet expansion retains complete source wedges, literal total determinants, admitted dependent supported zeros, and the rectangular arithmetic inclusion through `wedge^q eta`; it does not invert a determinant of rectangular `eta` (3935–4009).
- The trace-series finite enclosure uses `H=I-T`, `s_m=Tr(H^m)`, and an actual gap inequality `K_i>=g_0K_j`, `0<g_0<=1`. For each fixed pair its finite bounds converge. **Finite positive-gap existence is not uniform control as `k` grows** (4011–4106).
- The later cost operator is an endomorphism of the specified object: `Q=T I`, `Z=Q^(-1)-I=(K_j-K_i)G_i=F Omega^(-1)F*G_i`, positive self-adjoint in original `G_i`. Its eigenvalues obey `g_a=1/(1+lambda_a)` and `V_i/V_j=det(I+Z)` (4232–4341). Its displayed action commutator retains the transport of `H_j`; cost eigenspaces likewise are not presumed `A`-invariant (4343–4368).
- The two traces are the complete sums `t_1=sum b_n*G_i b_n/omega_n` and `t_2=sum |b_n*G_i b_m|^2/(omega_n omega_m)`. The independent-pair quantity `A_2=(t_1^2-t_2)/2` is the squared Hilbert–Schmidt norm of the actual second exterior source map. **Cross-pairings cannot be omitted, and this is not another cost-free spectral exterior amplification** (4370–4436).
- For `q>=2`, `d=sqrt((q t_2-t_1^2)/(q-1))`, `a=(t_1+(q-1)d)/q`, `b=(t_1-d)/q`. The transcript proves the spectral cap `lambda<=a`, derives a gap `1/(1+a)` without assuming uniform size, and gives the sharp two-trace bound `log(V_i/V_j)<=log(1+a)+(q-1)log(1+b)`, including its interpolation remainder, equality cases, `q=1`, and empty-module cases (4473–4584). Its third-trace correction is `-C_3/[3(1+a)^3]`, with `C_3=Tr((aI-Z)(Z-bI)^2)>=0` (4586–4620).
- The simpler certificate is `(V_i/V_j)<=(1+t_1)(1+2A_2/((q-1)t_1))^(q-1)` for `t_1>0`. The rank-one case `A_2=0` classifies this particular map; it does not identify higher support fibres or turn scalar support into a dimension count (4622–4657).
- The product/window composition uses the existing canonical family and a fixed `C_h^win`, independent of `k`, on either original length-`q` block. The inherited per-block lower budget forces `(D_h k)^(2q)<=(1+a)(1+b)^(q-1)` and the displayed independent-pair lower consequence; it is **not** a lower bound on every eigenvalue (4659–4721).
- **The actual trace and independent-pair sums are identified, but their required uniform growth bounds along the quartet family are explicitly not proved** (4723–4736). The direct source route requires moments through `2j`, potentially `4q`, and does not claim these high-degree arithmetic inputs already controlled (4795–4797).

## Historical corrections and evidence limits

- The Deligne comparison records an inherited transcription error: old French TeX had `<=2` where the current page record has **`<2`** in Lemma 3.2.10; strictness is needed to obtain the subsequent integral-weight bound `<=1`. It also records a corruption of the explicit squared-eigenvalue step in 3.2.13. The older files were not overwritten (3505–3509).
- The relevant extra estimate precedes tensor amplification; determinant/exterior maps alone do not supply it. Finite-field purity assumptions are not imported onto the characteristic-zero base (3511–3513).
- The corrected cost of a second exterior operation remains retained (3397; 4165); no second cost-free iteration is claimed. The actual source `wedge^2 Phi` calculation does not contradict that restriction (4434–4436).
- The mass-seven Gaussian examples, including repeated roots and nonzero nilpotent action, are declared finite polynomial calibrations, **not zeta packets** (4110–4161; 4738–4789). Their improved upper bounds neither certify an off-line zero nor give an RH counterexample. In particular, nontrivial restriction loss alone has no off-line-zero converse.
- The transcript reports passing finite regression suites, normal/optimized runs, manifest checks, and tested local integration patches. It expressly distinguishes these from Lean certificates, certified arithmetic moment enclosures, and uniform purity/volume estimates (2929–2935; 3517–3523; 4163–4169; 4791–4799). No new Lean execution or remote branch change is claimed for these continuations.

## Scope of failure of implication

This range records substantial exact arithmetic-source maps and estimates plus strengthened necessary consequences of a hypothetical off-line quartet. It records neither an actual off-line zero nor an upper bound incompatible with the quartet's required volume growth. The strongest threshold here is four; the missing step here is uniform control of the displayed original arithmetic volume/trace quantities. Failure of the one-sided gamma comparison or of a fixed finite certificate to supply that bound proves only that particular lack of implication. It does not prove RH false, make the original objects unrelated, or justify replacing their metrics, jets, source mass, quotient relations, or supported-zero data.
