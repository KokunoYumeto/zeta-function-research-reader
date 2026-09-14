# Later control continuation audit: U0049–U0054

## Scope, coverage and source pins

This bounded audit read every line 3596–7811 of `output/tau_f1_transcript_audit_2026-09-13/sources/audit_segment_U0041_U0054.md`, in order, including every retained user and assistant message. Segment SHA256: `4f6b4fd318308e561710bb24cd0f35b1b70b6507ba6be54b6f6d9b044ddbd1c4`. Locators below are one-based lines in that file, not lines in an inferred ZIP. The complete `output/split_zero_rh_tandem_2026-09-12/sources/Tau_Base_Cohomology_2026-09-12/NOTE.md` was also read. Its verified SHA256 is `d03e71ad18f187bd89880cb8ca6fc9c5d6f260b3de8e8e5702c27db97e7b63c3`.

Supplementary checking read the sum-connection `NOTE.tex` at `output/split_zero_rh_tandem_2026-09-12/sources/web_sum_connection_delivery/Tau_Sum_Connection_Control/NOTE.tex`, lines 176–287, 391–421 and 659–694. This is a bounded proof-window check of the Fisher identity, original relation derivative and explicitly stated transfer gap; it is not a claim to have audited that entire package or executed its regression suite. Earlier retraction, inverse-range and packet-section results cited by these episodes remain dependency inputs for the parent audit.

The original object is the four-point chart with `+,- < eta < sigma`, the functor

\[
\mathsf A_\tau(F)=[F_+\oplus F_-\xrightarrow{r_+-r_-}F_\eta]
\]

in degrees zero and one, its separately computed restriction to sigma, and

\[
K_\tau(W)=[I_\eta(W)\longrightarrow I_+(W)\oplus I_-(W)]\simeq S_\eta W[1].
\]

Tau Base (21)–(25), (27)–(31), (38)–(48) retain the two-leg complex, supported copies of `Q`, the adjoint, residue jets and tensor products. No message in the audited six episodes replaces this pushforward with the generic stalk or proves failure of the entire original programme. Later concentration on the one-leg complex has an exact relation to the joint complex, calculated below.

## Episode ledger

### LC49: U0049 → A1721, source boundary and control machinery

- User, line 3596, node `a9162d93-9cf1-4d45-b6f1-9fd92ae43471`, chain 3577: “then let us make the machinery for the deligne like control”.
- Progress A1696, line 3600, node `63828eab-7482-48e8-93d0-4fc0f615a74e`, chain 3580.
- Final A1721, line 3604, node `40ab7ee4-4dcd-409c-9e0d-f211bc6aecec`, chain 3634; response ends at line 4262.

The requested calculation is source-side Deligne-like norm, duality and tensor control on the original arithmetic classes. The response expands the cutoff/moment commutator of the inherited continuous retraction, constructs finite representatives `R=s_Z-Theta b` with exactly unchanged `qR=sigma_Z` and `J_ZR=1`, and computes

\[
B=DR-RA=\Theta K,\quad G=R^*R>0,\quad
W=A^*G+GA-G=-(R^*B+B^*R).
\]

At line 3905 it explicitly says: “The boundary expression \([x\overline F H]_0^\infty\) vanishes by their stated decay.” This is an analytic endpoint boundary justified by the original test space, not a claim that the cohomological relation `B` has zero Hilbert pairing. Indeed the following subsection explicitly retains `⟨Rv,Bv⟩` and the difference of the two theta primitives in `H^0`.

The residue calculation `A^*S+SA=S` gives the exact metric transfer

\[
G^{\mathrm D}=S^*G^{-1}S,\qquad
W^{\mathrm D}=-S^*G^{-1}WG^{-1}S.
\]

This proves upper-to-lower transport, retaining the original weight-one action. It does not itself supply an upper arithmetic estimate. The tensor computation retains `W_n` as the sum of all `n` factor contributions, hence a copied error costs `n epsilon`. Its orbit-Gram construction has an exact endpoint identity; the endpoint has not been shown to be small on the actual arithmetic family.

The fixed cutoff example `r=s_0=1/4`, the nilpotent block and the off-line diagonal block are explicitly auxiliary calibrations. Their role is stated; the text does not identify them with actual zero packets or change `g=2xi` to those examples. The malformed opening display `A^*GA+ (not used)` is a presentation defect, immediately replaced by the correct infinitesimal identity, not a substantive mathematical obstruction.

**Actual stopping point.** Line 4259: “The uniform sublinear error estimate for the **actual arithmetic tensor family** is not proved here.” The answer builds the machinery the user requested; it does not finish the subsequent bound. The matrix certificate interface certifies supplied matrices with supplied error enclosures; no arithmetic integral or uniform family has been enclosed by that interface here.

**Later completion.** A1771 fixes the actual theta derivative filtration and derives its rank-two defect. A1829 supplies canonical full-jet interpolation, same-metric reflection and joint tensor corrections. Thus the later work does not merely leave the machinery at the orbit-metric stage.

**Concrete continuation.** Use the canonical representatives from A1829, calculate their arithmetic full-jet moment matrices and signed boundary forms with the inverse interpolation matrix retained, then estimate their relative extremum as `k,M` vary. Do not infer the missing smallness from `qB=0`, the fixed-cutoff inverse bound, or a calibration certificate.

### LC50: U0050 → A1771, homotopy freedom and the original theta recurrence

- User, line 4263, node `95ddc7db-1037-4e47-b839-13eaeece6695`, chain 3635: “The other session is working on this. It may not have everything that it needs, but it's still trying to work. Consider corrections if they are required and continue.”
- Progress A1722, line 4267, node `ce1a8f2e-af6c-4022-8160-af9a12024a25`, chain 3637; A1735, line 4271, node `3e321a1f-89f3-42a8-86a4-d6e948dde8b2`, chain 3656.
- Final A1771, line 4275, node `552c8e45-2599-46da-8b95-214fa4d5ce0c`, chain 3721; response ends at line 4891.

The response checks both homotopy equations and gives the entire continuous family

\[
H_\alpha(b)=(\kappa b+\alpha(qb),\mathcal F^{-1}\alpha(qb)),\qquad
\alpha\in\operatorname{Hom}_{\mathrm{cont}}(Q,V).
\]

It lifts the family through support synchronization and retains `Hom(H^1,H^0)`; line 4430 states: “synchronization supplies the common target; it does not remove the \(H^0\)-class.” The zero composite `L -> gamma L -> d gamma L=0` establishes exactly why changing this homotopy cannot change the source boundary or control matrix. It then continues through the effective operation `R_T=R+Theta T`, with `K_T=K+D_VT-TA`.

The calculation fixes the actual theta seed `phi_*=(4pi^2 x^4-6pi x^2)e^{-pi x^2}`, `f_j=D^j Theta phi_*`, `L_n=span(f_0,...,f_n)`, and the orthogonal representative `R_n=(1-P_n)s_Z`. Every unscaled orthogonal norm `mathfrak h_n=||u_n||^2` remains. Integration by parts gives the three-term recurrence, including the negative coefficient `-mathfrak h_n/mathfrak h_{n-1}`, and then

\[
W_n=\mathfrak h_{n+1}(r_{n+1}^*r_n+r_n^*r_{n+1}),\qquad
G_n-G_{n+1}=\mathfrak h_{n+1}r_{n+1}^*r_{n+1}.
\]

The derivative is typed `Q_{V_n}->Q_{V_{n+1}}`. Its nonzero class at the old relation level is explicitly `-[u_{n+1}]r_n`, and the next transport makes it that receiving fibre's supported zero. The response proves the relation-layer isomorphism rather than dismissing this as zero after quotient.

The least relative excess is reduced to an explicit two-by-two spectral calculation using `r_nG_n^{-1}r_n^*`, `r_{n+1}G_n^{-1}r_{n+1}^*` and the mixed coefficient. Line 4821 stresses that “the inverse \(G_n^{-1}\) remains”. This is an exact finite reduction, not the evaluation or asymptotic control of those three quantities for arbitrary actual packets.

**Numerical and boundary scope.** The actual first four seed norms are evaluated; a double theta sum is integrated only after moving `(0,1)` to `(1,infinity)` by the original inversion. The displayed integer-tail estimate is explicitly distinguished at line 4882 from validated rounding and inverse-matrix errors. It is not a certificate for a nonempty packet's relative excess.

**Actual stopping point.** Line 4890: “A uniform small arithmetic excess has not yet been proved.” This is successful continuation through homotopy classification and an exact source recurrence, followed by a still-open quantitative calculation. The obstruction only says homotopy changes cannot change `B`; it does not say original theta-boundary changes, or the programme, fail.

**Later completion and next derivation.** A1829 supplies the full-jet inverse-moment metric and its convergent tail, making the earlier inverse-conditioning issue explicit. The next work is the arithmetic asymptotic or certified finite evaluation of that retained two-row expression, not a new homotopy parameter search.

### LC51: U0051 → A1829, canonical full-jet moment problem and joint tensors

- User, line 4892, node `e8523a76-cc80-41ad-a0f0-f5ed9ad6ff3b`, chain 3722: “The other session is continuing to try and formalize. This can happen, of course, while you also continue to work on pushing this through the program further. So continue doing that as you are.”
- Progress A1773, line 4896, node `11e00aa0-8036-4382-a795-16e531c812af`, chain 3725; A1779, line 4900, node `560d9cac-da7f-4022-9dcc-22095069129f`, chain 3732.
- Final A1829, line 4904, node `aff5580e-a451-48c3-85f4-f19487a5d35e`, chain 3826; response ends at line 5583.

The response acknowledges the previous metric-freedom calculation, then fixes the original `L_n` instead of optimizing unrestricted metrics. Its exact source remains `T_h(P)=P(D)F_h`, `M F_h=g/h`, with `T_h(hP)=Theta(P(D)phi_*)` and the arithmetic jet unit `upsilon_h=j_h(g/h)`. The polynomial family is therefore an explicitly mapped presentation of the original quotient, not a replacement family. The full-jet kernel is precisely `h P_n` in the one-factor source, and the original relation ideal in the tensor source.

It proves the constrained minimum formula

\[
d\nu_h(t)=\left|\frac{g(1/2+it)}{h(1/2+it)}\right|^2\frac{dt}{2\pi},\quad
G_{h,n}=(J_{h,n+d}M_{h,n+d}^{-1}J_{h,n+d}^*)^{-1}.
\]

The packet inclusions retain their arithmetic units and every nilpotent jet; the exact multiplication `P -> (H/h)P` is an isometry between the two specified measures. The reflection acts on the same canonical metric and pairs the generalized control eigenvalues with their negatives. This completes a compatibility issue left by transferring an upper bound to a different dual metric in A1721; it still supplies no small upper bound.

The density calculation proves the original `D^n f_0` family dense in `L^2(dx)`, hence `G_{h,n}->0`, but simultaneously proves every nonzero dual row diverges against `G_{h,n}^{-1}`. The exact Hilbert quotient map is `Q -> H/closure(Theta V)=0`; this map is explicitly distinguished from the original Frechet quotient `Q`. Its supported lift sends a class to `e`, not to `tau`. This is an exact obstruction to reading arithmetic purity off absolute Hilbert decay, with the original class and its jet still present. It is not failure of `A_tau` or `K_tau`.

The joint total-degree source and ideal are explicitly constructed. The next relation layer has dimension `binom(M+k,k-1)`, and the actual maps `Y_{k,M}, C_{k,M}` give

\[
W_{k,M}=-(Y_{k,M}^*C_{k,M}+C_{k,M}^*Y_{k,M}),\quad
G_{k,M}-G_{k,M+1}=Y_{k,M}^*Y_{k,M}.
\]

All tensor primitive signs are retained. This is a real change to admitted original boundaries, not the unsupported inference that a smaller Gram matrix has smaller relative defect.

**Actual stopping point.** Line 5580: “No uniform sublinear excess has been established in this continuation.” The eigenline diagnostic remains exactly `k(2Re rho-1)` independently of the chosen positive metric. The source equations and moment problem are completed; the arithmetic extremal estimate is not.

**Later completion and next derivation.** A1859 gives finite highest-layer coordinates, a proved finite bound and a signed symmetry restriction. The surviving task is bounding the actual recurrence coefficients and full-jet interpolation increments together; independent positivity of the measure, shrinking Gram matrices, or the bare existence of the moment inverse are insufficient.

### LC52: U0052 → A1859, finite bound and signed symmetric summand

- User, line 5584, node `af10d798-2756-445d-9e9b-5c7b064cade9`, chain 3827: “Yeah, let's push that.”
- Progress A1831, line 5588, node `fe850773-525d-45f2-a728-1fbb3b854c75`, chain 3830.
- Final A1859, line 5592, node `f39f3d53-73e5-40f4-bdf0-25c37492dba8`, chain 3887; response ends at line 6332.

The response constructs and inverts the map `b_M=T_+-R_MF` from the next homogeneous polynomial space to the actual next theta-relation layer. It computes the exact Gram `Omega+F^*G_MF`, retains every raw norm and actual measure mass, and proves the Woodbury metric update. The inverse metric obeys

\[
\mathcal C_{M+1}=\mathcal C_M+F\Omega^{-1}F^*,\quad
\mathcal Z_M=A_k\mathcal C_M+\mathcal C_MA_k^*-k\mathcal C_M
=F\Omega^{-1}E_+^*+E_+\Omega^{-1}F^*.
\]

The recurrence retains `Re b_n=1/2` and potentially nonzero `Im b_n`; it does not silently impose an even measure for an arbitrary reflection-stable packet. It proves the finite upper and lower estimate `epsilon_{k,M} <= 2 sqrt(Gamma_{k,M} lambda_{k,M})`. Line 6013 explicitly limits this: “Its constants have not yet been bounded sublinearly in tensor degree.” The sharper signed finite matrix is retained after Cauchy–Schwarz, so discarded phases are not silently identified with the original form.

The signed cochain idempotent `(1/k!) sum sign(pi)T_pi` cancels the Koszul sign in top degree and selects ordinary symmetric tensors. It keeps every repeated eigenvector `v^{tensor k}`, unscaled orbit sums, all factorial orbit masses, and the complement with its exact trace. The smaller module is a computed direct summand, not a deletion of off-line spectral witnesses.

The Gaussian repeated-root comparison is explicitly a calibration. The arithmetic measure remains `|2xi/h|^2 dt/(2pi)` throughout the proposed application; the literal Gaussian mass `sqrt(2pi)` is retained in the test. The response also reports a smaller-degree example where enlarging the correction space increases the relative excess. This is a legitimate counterexample to a naive monotonicity claim, not to all possible arithmetic asymptotics.

**Actual stopping point.** Line 6327 again states that uniform sublinear excess for the actual arithmetic family “has not been proved here.” The finite bound meets part of the requested push; its constants and signed cancellation have not been estimated in the required limit.

**Later completion and next derivation.** A1912 transforms this same matrix problem to a sum-coordinate matrix weight, preserving the relative fibres. One must estimate the actual signed frontier matrix or the combined arithmetic `Gamma lambda` cost after that exact transformation. The Gaussian improvement cannot supply that estimate.

### LC53: U0053 → A1912, exact sum descent but no improvement of the constant

- User, line 6333, node `bbd82b42-aa50-4eeb-abf3-27b7320953d3`, chain 3888: “Okay, yeah, continue.”
- Progress A1860, line 6337, node `275efe72-c7eb-4763-82d1-9bf3ce0e3186`, chain 3890.
- Final A1912, line 6341, node `64c5b883-17ba-441a-b5c9-bfa6ff1ef787`, chain 3986; response ends at line 7043.

The response performs an exact change of presentation using `S=sum s_i`, not a replacement of `g`. In the symmetric square it keeps `Delta=(s_1-s_2)^2`, proves the invariant quotient `(H_0,Delta H_1)` including collisions, and supplies its original theta primitives with both tensor signs. The real change of variables retains Jacobian `1/2` and the relation `Delta=-v^2` in every matrix-weight entry.

The scalar convolution is only the `(0,0)` entry. Every relative-coordinate moment remains in the full positive matrix `mathsf W(u)`. The triangular square-completion map is invertible, but its coefficient `m_0^{-1}b` need not be polynomial. The response explicitly keeps the exact image of the original filtered polynomials instead of enlarging to arbitrary sections. This avoids an otherwise serious source substitution.

The coordinate congruences `M'=T^*MT`, `J'=U^{-1}JT`, `G'=U^*GU`, `W'=U^*WU`, `R'=RU` prove that the generalized control constants are unchanged. Line 6788 says precisely: “The new operation has not manufactured a smaller constant.” This is an explicit preservation theorem, not the bound requested by the wider programme.

The finite sum-line module dual is computed by the `SI-A` resolution, retaining the full resolvent and every nilpotent ladder. Its scalar trace is a further observation. The displayed `RHom_{C[S]}(B_k,-)` belongs to a restriction-of-scalars category; it is not identified in this episode with the original chart functor `K_tau`. Tau Base already supplies a finite-jet morphism to the `K_tau` dual. Reattaching the new dual through that original finite-jet morphism is the concrete task, rather than calling the two right adjoints identical or unrelated.

**Actual stopping point.** Line 7038: “A uniform sublinear tensor excess has not yet been established.” The response leaves explicit arithmetic convolution mass, relative covariance and full-jet interpolation as the unestimated quantities. The finite pushforward's lack of an identified Deligne Lefschetz-pencil realization is stated with exact scope; no general failure theorem follows.

**Later completion and next derivation.** A1959 differentiates the actual sum amplitude, proves a mass-retaining scalar contraction, computes the full matrix connection and normal part, and adds the missing frame derivative `C^{-1}C'`. Those are genuine later completions of part of the analytic work. The still-missing estimate is on the original degree-constrained relative image, not on the unrestricted direct-sum space produced by pointwise square completion.

### LC54: U0054 → A1959, real Fisher estimate; missing transfer to the arithmetic extremal form

- User, line 7044, node `9cde09a7-2e48-4d0c-aa8b-4d54a316f9b9`, chain 3987: “ok the formalizing is in progress - you work on this”.
- Progress A1914, line 7048, node `c84c5062-8d5b-45fb-8eea-c0f4c924908e`, chain 3990; A1936, line 7052, node `951e58ad-9a13-43d3-847c-6b57a8616eef`, chain 4024.
- Final A1959, line 7056, node `ac351c92-ca3e-47a6-9014-85f239a2760e`, chain 4075; response ends with the segment at line 7811.

The source amplitude is the actual `a_h(t)=(g/h)(1/2+it)/sqrt(2pi)`, with unchanged mass `mu_h=||F_h||^2`. Reflection gives fixed real or imaginary phase, justifying the exact Fisher identity without requiring a bounded logarithmic derivative at zeros. In centered sum coordinates the Jacobian is one. The response proves

\[
\mathcal I_{h,k}+4\int\|n_k(u)\|^2du
=\frac{\mu_h^{k-1}}{k}\mathcal I_h.
\]

The proof retains all diagonal terms, computes all distinct-index cross terms as `mu_h^{k-2}|int conjugate(a_h)a_h'|^2=0`, and retains the normal residual by orthogonal decomposition. The endpoint zero is justified by Schwartz decay after the exact Mellin–Fourier transform. The mass is never set to one. This is a completed analytic calculation on the actual arithmetic seed family.

Line 7333 states: “The scalar calculation is only the constant relative column.” The full relative family then has exact matrices `mathsf W=j^*j`, `mathsf B=j^*j'`, `mathsf T=(j')^*j'`, connection `Gamma=mathsf W^{-1}mathsf B`, normal map `N=(1-Pi)j'`, and full energy

\[
\|\partial_u(j_uc)\|^2
=(c'+\Gamma c)^*\mathsf W(c'+\Gamma c)+c^*N^*Nc.
\]

The connection formula correctly retains the extra `C^{-1}C'` under a changing frame and the potentially noncommuting product `mathsf W' mathsf W^{-1} mathsf W'`. Neither matrix term is bounded on the whole degree-constrained source in this response.

The exact observable dictionary is

\[
\mathscr U_kD^{(k)}=(k/2+iu)\mathscr U_k,\quad
\partial_u\mathscr U_k=i\mathscr U_k\mathscr L_k,\quad
\mathscr L_k=\frac1k\sum\log x_i,\quad
[D^{(k)},\mathscr L_k]=-1.
\]

Thus the new differential estimate concerns a conjugate observable, not the original generator defect `W_M`. The response does not conflate them; it exhibits their exact commutator and filtered graph. It also calculates the response of actual theta relations: `J_h(log x Theta phi)=j_h(g')j_h(H_phi)`, the complete conormal thickening `P/I^2`, its derivative map, the local arithmetic unit correction, and higher relation layers. These carry the original multiplicities and lead to the same residue trace contraction as Tau Base (44)–(45).

**Actual stopping point.** Line 7790: “It is not yet a uniform sublinear bound for every relative polynomial direction in \(W_M\).” This statement has exact mathematical content. Neither the full-matrix energy identity nor the conormal map supplies a quantitative comparison between all admissible coefficient functions and the inverse full-jet interpolation metric. The only displayed numerical arithmetic evaluation is for `h=1`; line 7807 expressly says it is not “a substitute for a nonempty arithmetic packet.”

**Later completion.** None occurs inside this audited segment. The supplementary source windows confirm that the final note itself states the same transfer gap. Any later completion must be matched to its actual subsequent turns; it cannot be inferred from a later ZIP title.

**Concrete continuation.** Retain the exact least-norm coefficient lift `C_{k,M}=M_{k,M}^{-1}J_{k,M}^*G_{k,M}`. Substitute its actual coefficients into both terms of the full derivative energy, retaining the normal matrix and the frame derivative. Evaluate the corresponding finite quadratic forms and the original signed `W_{k,M}` in the same quotient coordinates; control the change between them using the original theta boundary equation. Track `mu_h^{k-1}`, all packet-unit jets, the polynomial degree, tensor degree and inverse interpolation matrix. An estimate of `I_{h,k}` alone, or a proof that the two differential pieces are retained, does not complete this calculation.

## Two completed source-comparison calculations for the audit

### A. The one-leg complex is an explicit equivariant retract of the original joint pushforward

Let `F` denote the original even Fourier involution on `V`, so `F^2=1`. In the original coordinates put

\[
C_\tau=[V\oplus V\xrightarrow{\Theta(\phi-\mathcal F\psi)}\mathscr B],
\qquad C_+=[V\xrightarrow\Theta\mathscr B].
\]

Define degree-zero and degree-one maps

\[
i^0(v)=(v,0),\quad i^1(F)=F;\qquad
p^0(\phi,\psi)=\phi-\mathcal F\psi,\quad p^1(F)=F.
\]

The equations `d_tau i^0=i^1 Theta` and `Theta p^0=p^1 d_tau` follow directly from the displayed original differential; therefore these are chain maps, and `pi=1`. Their complementary map in degree zero is

\[
(1-ip)^0(\phi,\psi)=(\mathcal F\psi,\psi),
\]

and in degree one is zero. Its image is the full original kernel, not a vanished subspace. Explicit mutually inverse chain maps are

\[
C_\tau\longrightarrow C_+\oplus V[0],\quad
(\phi,\psi)\longmapsto(\phi-\mathcal F\psi,\psi),
\]

\[
C_+\oplus V[0]\longrightarrow C_\tau,\quad
(v,w)\longmapsto(v+\mathcal Fw,w),
\]

with the identity on the degree-one copy of `mathscr B`. Every component is continuous in the original Schwartz topology. Under Tau Base (34), the joint action is `(U_a phi,aU_{1/a}psi)`. Since `mathcal F(aU_{1/a}psi)=U_a mathcal Fpsi`, the first factor has exactly `U_a`, and the retained second factor has exactly `aU_{1/a}`. Thus this is an equivariant chain splitting with the full action, not a replacement by identical actions on both legs.

In the split reconstruction, the actual map from the single `+` support fibre to the joint fibre inserts the supported zero in the minus leg. It is the existing support transport and preserves the nonempty mask. External absence maps to external absence. No assertion that this linear direct-sum description erases other support fibres is made.

Consequently every one-leg `H^1=Q` calculation has the identity comparison to the original `H^1 A_tau(T)=Q`, while the original `H^0=V` remains in the explicit complementary complex. Applying the original adjunction to this actual split complex gives

\[
R\operatorname{Hom}_E(C_\tau,W)
\cong R\operatorname{Hom}_E(C_+,W)\oplus\operatorname{Hom}_E(V,W)[0].
\]

In degree minus one the comparison is precisely `Hom(Q,W)`, hence the finite-jet dual maps in these episodes land in the same original `H^{-1}RHom_A(T,K_tau(W))` from Tau Base (28),(43). This proves the relevant source and adjoint comparison rather than calling the two presentations unrelated.

### B. The announced global logarithmic-relation map and its exact full-jet image

Use the original `L F(x)=(log x)F(x)` on `mathscr B`. This is a continuous endomorphism: differentiating `L F` finitely many times produces the original derivatives of `F` times `log x` or constants; for every integer weight `b`, `|log x|x^b` is bounded by a constant times `x^{b-1}+x^{b+1}`. The seminorms in Tau Base (11) therefore control all resulting terms. Define

\[
\nu:V\longrightarrow Q,\qquad \nu(\phi)=q(L\Theta\phi).
\]

This is a continuous linear map using the original quotient topology. In original unshifted coordinates,

\[
U_aL=(L-\log a)U_a,\quad U_a\Theta=\Theta U_a,\quad q\Theta=0.
\]

For each `phi` their direct substitution gives

\[
U_a\nu(\phi)=qU_aL\Theta\phi
=qL\Theta U_a\phi-(\log a)q\Theta U_a\phi
=\nu(U_a\phi).
\]

Similarly `DL=LD-1` and `DTheta=Theta D_V` imply `D_Q nu=nu D_V`. Thus A1936's announced global map has a complete equivariance proof without discarding the commutator; the commutator term is an actual original theta relation before its quotient.

For a finite packet `h=prod(s-rho)^{m_rho}` with complete actual orders, the original Mellin identity gives

\[
J_h\nu(\phi)=j_h(g')j_h(H_\phi).
\]

For every polynomial `P`, the actual source `phi=P(D_V)phi_*` lies in `V`, since differentiation preserves both zero moments, and `H_phi=P`. Polynomial reduction is onto `E_h`; hence the exact image, not just an inclusion, is

\[
\boxed{J_h\nu(V)=j_h(g')E_h.}
\]

At a selected root write the original germ as `g=u_rho(z)z^{m_rho}`, with the original nonzero unit `u_rho`. Differentiation gives

\[
g'=m_\rho u_\rho(z)z^{m_\rho-1}+u_\rho'(z)z^{m_\rho}
\equiv m_\rho u_\rho(0)z^{m_\rho-1}\pmod{z^{m_\rho}}.
\]

Therefore multiplication by `g'` has image the full one-dimensional socle `C z^{m_rho-1}` in each local factor. Its kernel is `(z)` in that factor, including the case `m_rho=1`, when `(z)=0` and the image is the whole factor. On the complete packet its rank is exactly the number of distinct selected roots and its kernel dimension is `sum_rho(m_rho-1)`. No nilpotent jet has been declared absent: the derivative reads its socle through a fully specified contraction.

Finally Tau Base (42) gives, for this exact image,

\[
R_Z(f,J_h\nu(P(D_V)\phi_*))
=\sum_{\rho\in Z}\operatorname{Res}_\rho f^\dagger P\frac{g'}g\,ds
=\sum_{\rho\in Z}m_\rho\overline{f(1-\bar\rho)}P(\rho).
\]

The second equality follows from `g'/g=m_rho/z+u_rho'/u_rho`; the unit term is holomorphic and has zero residue. This completes the global equivariance and the exact arithmetic image behind the final episode's trace formula. It does not establish a positivity or tensor-growth bound.

## Integration judgment and priority

These six episodes contain substantial mathematical continuation, including analytic work on the original theta source. Their repeated endpoint is an uncompleted arithmetic uniform estimate. A passage-by-passage audit should identify that endpoint without relabelling legitimate computations or precisely scoped obstructions as abandonment of all mathematics.

The main redo request should resume the final filtered matrix-weight comparison, with `A_tau`, `K_tau`, the actual `g=2xi`, the arithmetic unit, all local jets, supported relation layers and original actions attached. The following shortcuts are specifically excluded by the calculations already present: treating a theta boundary as an orthogonal vector; choosing an arbitrary favourable metric; reading purity from `G_n->0`; promoting an auxiliary Gaussian example; dropping the complement of the signed symmetric projector; replacing the full relative matrix by its scalar convolution entry; assigning unit mass; or replacing the conjugate logarithmic observable by `D^(k)`.

The tractable comparison calculations above can be integrated immediately. The harder continuation is the explicit all-direction arithmetic interpolation estimate left at A1959, not a new generic RH equivalence or an unspecified purity assumption.
