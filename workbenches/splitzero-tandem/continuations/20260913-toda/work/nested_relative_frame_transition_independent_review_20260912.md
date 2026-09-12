# Independent proof review: nested relative-frame transitions

Date: 2026-09-12. Reviewer: `paired_checker_review`.

## Read scope and outcome

I read the complete standalone draft `work/nested_relative_frame_transition_20260912.tex`, including the later additions NT.18a and NT.20a, the ambient-extension composition, the corrected paired-vector notation, and the final NT.31–37 fixture appendix. I checked all NT.1–30 identities, their domains, source inclusions, inverses, signs, degree bounds and endpoint statements. The earlier complete FC source supplies the original amplitude, Schwartz estimates, Mellin identification and arithmetic Hermite observation that this continuation explicitly retains. The finite normal-injectivity argument is checked again in NT.17.

No mathematical defect was found. Two initial presentation defects were reported and were corrected by the author: the standalone preamble lacked `\rank`, and the paired coefficient vector reused `q_M`, already assigned to the integer source dimension. The final draft defines `\rank` and calls the paired vector `\boldsymbol\eta_M`. This reviewer made no source or cumulative-TeX edits.

An independent child reviewer, `nested_graph_spotcheck`, separately read NT.15–20 and NT.24–28, checked the FC.15 factor against the original FC source, and found no mathematical error. Its inverse and paired-Gram calculations agree with the calculations recorded below. This review does not certify any direct limit or inverse growth claim; those are not claims of this draft.

## Original source inclusion: NT.1–4

The retained relative coordinates are the independent variables `z_i=s_i-S/k`, for `i<k`, with `z_k=-Σ_{i<k}z_i`. Together with `S`, they form an invertible linear coordinate system on the original polynomial ring: `s_i=z_i+S/k` for `i<k` and `s_k=S/k-Σ_{i<k}z_i`. Thus independence of the relative polynomials over the constants also proves their independence as coefficients of powers of the independent variable `S`.

The larger family is independent and homogeneous. Projecting the equation `θ^M_α=Σβ θ^L_β E_{βα}` onto each homogeneous degree shows that all coefficients of a different degree vanish; independence within each degree proves this separately. Hence the support of `E` respects the literal relative degrees. If `Ec=0`, the same polynomial identity gives `Σα θ^M_α c_α=0`, so `c=0` and `E` is injective.

For an admitted smaller column `(α,n)`, a nonzero entry of `F` can only be in a larger column `(β,n)` with the same relative degree. Its bound is retained because `n≤M−ℓ^M_α≤L−ℓ^L_β`. Expanding the original polynomial proves `P^L_{Fp}=P^M_p` without altering any `S^n` coefficient. Consequently `C_LF=EC_M`; differentiation, with constant `E,F`, gives `C_L'F=EC_M'`, including the literal coefficient `in(k/2+iu)^{n−1}`. The coordinate-system argument proves `F` injective. No truncation or projection replaces this inclusion.

## Weighted connection and exact normal transfer: NT.5–12

Each `j_a` is an injective map from the stated finite coefficient space into the original ambient fibre. Its weight `W_a=j_a^*j_a` is positive, smooth and locally uniformly bounded above and below. The coefficient inverse used in `R=W_M^{-1}E^*W_L` is therefore well defined. From `j_M=j_LE` and constant `E`, both `W_M=E^*W_LE` and `B_M=E^*B_LE` follow. In particular `RE=I`, `Q=ER` is a projection, and

\[
Q^*W_L=W_LEW_M^{-1}E^*W_L=W_LQ.
\]

The projections in the fibre satisfy `Π_LΠ_M=Π_MΠ_L=Π_M` because their ranges are nested. Thus `Π_L−Π_M` is the orthogonal projection onto `V_L∩V_M^⊥`.

The identity `Γ_M=RΓ_LE` proves `E^*W_LK=0` for `K=Γ_LE−EΓ_M`. Using the original identity `j_aΓ_a=Π_a j_a'` gives the exact ambient map

\[
A=j_LK=(\Pi_L-\Pi_M)j_M'.
\]

Splitting `I−Π_M=(Π_L−Π_M)+(I−Π_L)` therefore proves

\[
N_M=A+N_LE,
\qquad A^*N_LE=0.
\]

Taking its Gram yields `𝒩_M=E^*𝒩_LE+Δ`, with `Δ=A^*A=K^*W_LK`. Expansion of `K` and the identity `E^*W_LΓ_LE=W_MΓ_M` give exactly the second formula for `Δ` in NT.10. Since `W_L` is positive and `j_L` is injective, all three null conditions in NT.11 are equivalent. The image of `K` has dimension at most `r_L−r_M`; this and its domain dimension give the stated rank bound.

For an original coefficient function `c`, the terms `j_M∇_Mc`, `Ac`, and `N_LEc` lie respectively in `V_M`, `V_L∩V_M^⊥`, and `V_L^⊥`. Their sum is the directly differentiated original amplitude. This proves both NT.12 energies and retains the complete coefficient derivative. In particular the positive transfer is an orthogonal projection of the original derivative, with the complementary normal component still present.

## Literal finite-source matrices: NT.13–14

The domains of `mathbf N_a` and `mathbf T_a` are `C^{q_a}` in the literal coefficient basis from NT.3; their codomain is the same `𝒦=L²(du;𝓗)`. The source identity `C_LF=EC_M` gives

\[
\mathbf N_M=\mathbf A_{LM}+\mathbf N_LF,
\qquad \mathbf T_LF=\mathbf T_M+\mathbf A_{LM}.
\]

The three cross-Grams in NT.14 vanish pointwise by the ranges just proved. Integrating these identities yields each displayed source Gram without changing the measure or the source basis. The zeroth-order Gram is finite by the polynomially weighted original amplitude estimates; the derivative Grams are finite by those estimates after differentiation and projection contraction. Hence all adjoints and integrals used here have their declared finite domains.

The two tangential Grams differ by the same `H^{tr}_{LM}` that appears with the opposite sign between the normal Grams. Their sum is exactly `H_M^∂=F^*H_L^∂F`. This is the original derivative norm on the included original polynomial, not a comparison between independently chosen vectors at the two levels.

## Graph unitary and both inverse identities: NT.15–16

Put `P_a=Πhat_a` and let

\[
S_a:\operatorname{ran}P_a\oplus\ker P_a\longrightarrow\mathscr K,
\qquad S_a(t,n)=t+n.
\]

This is a unitary with inverse `z↦(P_az,(I−P_a)z)`. The stated map is exactly `𝒰_LM=S_L^{-1}S_M`. Since `P_Lt=t` and `P_Mn=0`, this gives the first formula in NT.15. Conversely `S_M^{-1}S_L` gives `(P_Mt_L,(I−P_M)t_L+n_L)` because `P_Mn_L=0`. These formulas prove both inverse orders on the entire stated orthogonal direct sums, not only on finite graphs.

The finite actual graph is a subspace of the smaller direct sum. Its image is exactly the graph over `Fp`, because `P_Lmathbf N_Mp=mathbf A_LMp` and the NT.14 tangential identity supplies the first component. Addition on either graph is the same original differentiated amplitude. The larger full finite graph may contain additional source vectors; NT.16 correctly identifies only the included smaller graph.

## Finite normal injectivity, inverse and ambient extension: NT.17–18a

The original amplitude has infinitely many unremoved critical-line zeros after deleting the finite packet. Its full zero order `ℓ_T` and coefficient `c_T` are retained. If `N_a(u)c=0`, the projection formula gives `Ψ'ϑ_c=Ψϑ_d`, with `d=Γ_ac`. The identity holds everywhere on the fibre because both representatives are smooth and equal almost everywhere.

At a point with `t_1=T` and all other factors nonzero, vary `t_1=T+δ` and compensate in the final coordinate so that the original sum stays fixed. The original derivative is still the fixed-relative-coordinate derivative. Its first product term has the leading coefficient `(ℓ_T/k)c_TA_b δ^{ℓ_T−1}`; every other term retains the factor of order `ℓ_T`. The asserted smooth identity therefore forces `ϑ_c` to vanish at that point.

For `k≥3`, the other factors are nonzero on a dense subset of each hyperplane. Polynomial continuity gives vanishing on the entire hyperplane, and its distinct `y_1=T−u/k` values for infinitely many `T` force the polynomial to be zero. For `k=2`, excluding `𝒵_h+𝒵_h` guarantees that all second factors `a(u−T)` are nonzero, yielding infinitely many distinct univariate roots. This sumset is countable. Therefore each finite frame has positive normal Gram almost everywhere. A nonzero admitted vector polynomial has a nonzero component and hence only finitely many common real zeros. Its integrated normal Gram is strictly positive, proving injectivity on the entire finite source, including nonzero arithmetic relations.

Write `B=mathbf N_LF:C^{q_M}→𝒦` and `H=B^*B=F^*H_L^NF>0`. The claimed normal transition maps `mathbf N_Mp` to `Bp`. Its inverse is the typed map

\[
\operatorname{ran}B\longrightarrow\operatorname{ran}\mathbf N_M,
\qquad r_L\longmapsto\mathbf N_MH^{-1}B^*r_L.
\]

Substitution of `r_L=Bp` proves one inverse order. Every `r` in the smaller image has unique form `mathbf N_Mp`, so substitution proves the other order. Its exact norm loss is `||mathbf A_LMp||²` by the orthogonal sum in NT.14. No bound uniform in a level is required or asserted.

The later ambient extension is

\[
V_{LM}=B(H_M^N)^{-1}\mathbf N_M^*
       =(I-P_L)\Pi_M^N.
\]

Both factors on the right are orthogonal projections. Thus `||V_LM||≤1`; its restriction to the finite smaller image equals the original normal transition. At equal levels its value is the finite-image projection, as stated. For three levels, direct multiplication cancels `(H_L^N)^{-1}mathbf N_L^*mathbf N_L=I` in the middle, proving `V_TL V_LM=V_TM` on all of `𝒦`. This does not replace the explicitly stated equal-level ambient projection by the ambient identity.

## Arithmetic observation and target metrics: NT.19–20a

The matrix `mathsf J_a^log` has domain `C^{q_a}` and target the full finite Hermite algebra `𝔄_h`. Its columns follow by differentiating the entire representative `U θ_α S^n` before taking its Hermite class. The equalities `δS=1` and `δz_i=0` leave the exact derivative coefficient `n`; the derivative of the full unit is `[δU]=βυ`. This procedure makes no assertion that `δ` descends as a derivation of the quotient.

Because the original polynomial is unchanged by `F`, differentiation before quotienting proves `mathsf J_L^log F=mathsf J_M^log`. Evaluating the two observation maps on `r=mathbf N_Mp` gives

\[
\mathsf{Obs}_L^{\log}\mathcal Q_{LM}r
=\mathsf J_L^{\log}Fp
=\mathsf J_M^{\log}p
=\mathsf{Obs}_M^{\log}r.
\]

Their source path retains graph addition, the factor `−i` in the inverse original Mellin isometry, and the complete arithmetic jet. The empty packet's algebra is the zero target and is handled by its unique map.

For two declared positive target matrices in the same literal basis, `D=(G_M^tar)^{-1}G_L^tar` satisfies `D^*G_M^tar=G_M^tar D=G_L^tar` by taking its adjoint explicitly. Substitution of the unchanged arithmetic coordinate vector `mathsf J_M^log p` gives both quadratic-form equalities in NT.20a. The draft assigns no unjustified sign to their difference. The target comparison does not modify the previously computed source or normal Grams.

## Variable coefficient inclusions: NT.21–23

The formula `E^G=G_L^{-1}EG_M` follows directly from the same ambient frame equation. Differentiating that equation gives

\[
B_M^G=(E^G)^*B_L^GE^G+(E^G)^*W_L^G(E^G)'.
\]

Multiplication by the actual inverse weight proves the first NT.22 identity. In the full expression `(E^G)'+Γ_L^GE^G−E^GΓ_M^G`, differentiation of the inverse `G_L^{-1}` cancels the `G_L^{-1}G_L'` connection contribution; the derivative of `G_M` cancels the corresponding smaller connection contribution. The remaining matrix is exactly `G_L^{-1}KG_M`. Its ambient image is `AG_M`, and the normal and transition Grams have the stated transformations.

The same cancellation with `C_a^G=G_a^{-1}C_a` proves that the actual tangential, normal and transfer amplitudes on the original source coefficient vector are unchanged. All the finite matrices and inverse-on-image maps are therefore the same original maps after their explicit coefficient transport. Smooth gauges need not preserve polynomial coefficients; the draft correctly preserves the transported original filtered source instead of declaring a new polynomial source.

## Nested chains and both paired branches: NT.24–28

Inserting `E_TM=E_TL E_LM` into the definition of `K_TM` and adding the two cancelling middle terms gives `K_TM=K_TL E_LM+E_TL K_LM`. Multiplication by `j_T` gives the stated ambient sum. Its two summands lie in `V_T∩V_L^⊥` and `V_L∩V_M^⊥`, so their cross-Gram vanishes. This proves the exact pointwise and integrated telescoping identities, with `F_LM` introduced by `C_LF_LM=E_LMC_M`.

Graph composition follows from `S_T^{-1}S_L S_L^{-1}S_M=S_T^{-1}S_M`. Normal composition follows from `(I-P_T)(I-P_L)=I-P_T`, and the intermediate source image lies inside the next map's declared domain.

On the two quadratic branches, `v=√x>0`. The matrices `M_a` are invertible of size `2r_a`; `mathscr K_LM` has size `2r_L×2r_M`. The identity `M_L diag(E,E)=diag(E,E)M_M` proves the weight congruence and cancels the two moving-basis derivative contributions in the paired connection difference. The original negative branch contributes `−K(-v)/(2v)`, with its sign retained.

Substituting the exact definitions and cancelling `M_L^{-1}` against its adjacent factors gives

\[
\mathscr K_{LM}^*H_L\mathscr K_{LM}
=\frac{M_M^*\operatorname{diag}(\Delta_{LM}(v),\Delta_{LM}(-v))M_M}{8v^3}.
\]

The denominator contains the weight Jacobian `2v` and the square of the derivative factor `2v`. Multiplication by `4x=4v²` therefore gives exactly the normal-form difference. Weighted orthogonality follows branch by branch from `E^*W_LK=0`. The coefficient derivative inclusion in NT.28 and the FC.15 factor `4x` show that tangential gain equals normal loss in the same complete original energy.

For variable frames, the paired inclusion itself depends on `x`. Differentiating `mathscr E=M_L^{-1}diag(E^G(v),E^G(-v))M_M` proves that the transition includes `mathscr E'`. The chain rule gives the original opposite branch derivatives. The factor `H/(2x)` in the density compatibility identity remains the derivative of the same original Jacobian. None of these paired identities assumes evenness of the weight.

## Zero fibres and derivative domains: NT.29–30

An empty smaller frame or source is covered by its zero-dimensional maps. Equal frames give the identity weighted coefficient projection and hence zero transition. For an unequal frame, the exact zero condition is `Kc=0`, already proved equivalent to zero transition quadratic form; no unwarranted strict transition positivity is inferred from strict finite normal positivity.

For the quartet packet at `k=2`, evenness of the amplitude makes the original fibre derivative zero at `u=0`. Thus the fixed-frame connection, normal maps and transfer all vanish there. Smooth gauge terms can make the transformed connection nonzero while the tensorial transition and normal map still vanish. This is compatible with positive integrated normal Grams and their finite inverses.

For NT.29, the forward inclusion follows from equality of the original amplitudes and derivatives. Conversely, the constant left inverse `(E^*E)^{-1}E^*` takes a locally absolutely continuous larger coefficient into a smaller one. The fixed closed subspace condition, initially almost everywhere, holds everywhere for the continuous representative. The original amplitude equality then proves both finite norm and finite derivative energy. This verifies both directions on the full stated derivative domains.

Near zero, the original weight has positive upper and lower bounds and the original connection is bounded. The finite open-branch norm and covariant derivative energy imply ordinary coefficient `H¹` control on each side. The two finite endpoint traces therefore exist. Integration by parts gives a jump distribution with the difference of these traces; their equality is precisely what removes it. Multiplication by an injective constant `E` preserves and reflects equality of those traces, proving the paired inclusion's exact endpoint correspondence. Smooth invertible gauges through zero have one common value and preserve the same condition. Gauges defined only away from zero correctly retain the original products `G(±v)c^G(±v)` in the matching condition.

## Consistency read of the appended NT.31–37 fixture

The appended fixture has its own independent proof/checker review and manifest. I also read the complete final appendix and performed a separate exact consistency calculation from its original `j_L(u)`, constant `E`, and original coefficient curve `c(u)=(1+iu,u²−i)^T`. I formed `j_M=j_LE`, differentiated these original matrices, and constructed the two orthogonal projections directly as `J(J^*J)^{-1}J^*` and `(JE)((JE)^*(JE))^{-1}(JE)^*` at `u=1`. This computation did not define the projector difference or the original derivative by the appendix's proposed numerical values.

All 17 inspected consistency statements passed in SymPy 1.13.1: the smaller weight difference, both displayed weight commutators, the explicit rank-one projector difference, both normal-component matrices, their two Grams, the directly differentiated original vector and its norm, the three-vector sum, the displayed tangential and surviving-normal vectors, each of the three rational energies, and their sum. In particular the original derivative has squared norm `441`, and the independent component norms are exactly

\[
\frac{217065}{497},\qquad \frac{58496}{51191},\qquad \frac{320}{103},
\qquad
\frac{217065}{497}+\frac{58496}{51191}+\frac{320}{103}=441.
\]

This consistency check found no discrepancy in the appendix. It is supplementary to the separately recorded fixture certification, and does not make an arithmetic-density identification.

## Final certification

The revised NT.1–30 proof, including NT.18a and NT.20a, is mathematically approved within its explicit finite-level scope. Its original coefficients, measures, full source relations, normal terms and derivative domains are retained. No source edits were made by either independent reviewer. The final complete source read and checked has SHA256 `08100877c442d1d46a8c21158bd504a5a763528b1a4af53c962b83bff2a7f1c7`. That source includes the separately certified NT.31–37 fixture, for which the supplementary consistency checks above also passed.
