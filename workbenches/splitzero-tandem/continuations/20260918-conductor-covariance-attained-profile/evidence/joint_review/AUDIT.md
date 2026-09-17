# Independent audit of the exact profile/covariance combination

**Primary verdict: proved as written in the revised common parameter domain, for the exact combination audited here.** The initial bridge required an explicit domain restriction and a clarification that its trial endpoint is the original, un-intersected conductor endpoint. Both repairs have been made in the revised bridge inspected here. The separate covariance, norm, transport and attained-envelope input proofs are assigned to other independent reviewers; they are not relabelled as proved by this combination audit.

## Scope and provenance

This review reads the original endpoint and quotient formulas, independently reconstructs their exact combination, and supplies a complete finite comparison allowance. It does not edit the bridge or publish/build artifacts.

Original full source: `work/mixed_tail_continuation_20260917/full_receiver_build/staging/14_CURRENT_KERNEL_AND_MULTIPLICITY_PROOFS.tex`, SHA256 `50E5071B8BC1E1325F401764E7FDD3CDA50994601B6F2E1BF00627864D665571`.

Raw attained-tail response: `inputs/ATTAINED_TAIL_WEB.md`, SHA256 `D55F313672418DE60C8422738592641933808C169EE1A6463866DE6659DF3B4C`.

Raw covariance response: `inputs/LOWER_ROOT_COVARIANCE_WEB.md`, SHA256 `BCC840C8F0E985890959FE39F6546F2DE141E1D15C643AAE8BE9F25DA5FD4EAB`.

An inspected revised bridge is retained in `BRIDGE_AUDITED_SNAPSHOT.tex`. The parent continues to integrate the derivative improvement after this snapshot. The exact original programme attributions, including `human:globalization2026` and `human:splitzero2026`, remain attached to the cumulative mathematical source. The Schur/minimum operations used below are proved directly in TAC5–6 and NTG14–25; the source credits Boyd and Vandenberghe at the corresponding positive-matrix formulas. No independent attribution or new external theorem is invented here.

## Claim card and common domain

Fix the original simple quartet, its actual period, branch, unit and conductor coefficients. Let a be an integer with a≡1 modulo4 and a≥257, q=(a+1)^2, Q=(a−7)^2, Δ=q−Q=16a−48. Retain v=ord_0 E_A∈{0,...,80}, its actual nonzero coefficient μ_v, m=Δ−v, s∈{1,a}, and ℓ_s=(s−1)/4. The two source orders refer to the same original Gamma source orders on both upper and lower packets; the lower packet degree is a−8, and its source order is not changed to a−8.

For the finite norm and envelope estimates impose their original common guards:

- a√(δ²+γ²)≤2^(−33)q;
- for b=a and a−8, n_b=(b+1)²+ℓ_s≥100 and max{b√(δ²+γ²),2ℓ_s+1/2}≤2^(−17)n_b;
- retain the original 0<δ<1/2 and γ>2 hypotheses.

All guards hold eventually at each fixed actual quartet, and constants denoted O_actual are uniform over the two choices s=1,a. In this domain Q>0, Δ>v, m>0 and 0<R<q for R=floor(a^(3/2)/log a). Furthermore m+q≤q+Δ<2Q≤2(Q+ℓ_s): the middle strict inequality is equivalent to a²−46a+145>0, which follows from a≥257. Thus every lower row used by the combination lies inside its original whole-polynomial degree range.

The exact attained row is γ_{r,s}=log(η_{r,s}/ν^-_{m+r,s})≥0, where η is the full preceding-relation minimum and ν^- is the complete lower ideal monic minimum. The endpoint weights are θ_0=θ_q=1 and θ_r=2 for 0<r<q. For B={R+1,...,q}, the audited bridge concludes the finite inequalities

Σ_B θ_r |γ_{r,s}−Δ f(r/q)| ≤ 2E^U+E^nat+E^cmp,

0≤Σ_B θ_r log(τ_{r,s}/η_{r,s}) ≤ E^U+E^nat+E^cmp,

with O_actual(q log q) right sides. Here τ is the fixed optimized-upper-fibre conductor trial, not another minimum chosen after observing the lower geometry. The revised extension gives the same weighted L1 order on {1,...,q}, keeps row0 as its actual atom, and gives the trial order on {2,...,q}.

## Exact scalar dictionary

At every t>0 use the original EIQ equilibrium with α=2/t and β=π/t. Its support is [u²,v_*²], and the original endpoint equations are uK(k)=2 and v_*E(k)=2(1+t), with ρ=u/v_* and k=√(1−ρ²). Therefore ρK/E=1/(1+t). Put w=(u+v_*)/2 and c=(v_*²−u²)/4. The original GRE6–8 identities, directly inspected at source lines59867–59899, are

λ=2(α+2)−2α log w−2 log c,
λ_α=−2log w,
λ_β=2(α+2)/β.

Their exact combination is λ−αλ_α−βλ_β=−2log c. No endpoint motion has been omitted; GRE4–8 explicitly prove the moving-support derivatives and β-dilation law.

For ψ(t)=(1+t)(1−log(1+t))−tλ(2/t,π/t)/4, chain differentiation gives

ψ′=−log(1+t)−(λ−αλ_α−βλ_β)/4
   =−log(1+t)+(log c)/2
   =log(k/E(k)),

because c=(1+t)²k²/E². Also tα=2, so substitution in 2ψ−2(1+t)ψ′ cancels the full constant 2(1+t) against t(α+2), leaving

2ψ−2(1+t)ψ′=2log w−log c
             =log((1+ρ)/(1−ρ))=:f(t).

This agrees exactly with GRE35–36 at source lines60269–60291. In particular the centres use the same Robin sign and endpoints.

The convergent integral expansions at k=0 give t=k⁴/16+O(k⁶), whence k=2t^(1/4)(1+O(√t)), ψ′=(log t)/4+log(4/π)+O(√t), and ψ(0)=log(4/π)=a_0. Integration gives

ψ(t)=a_0+(t/4)log t+(a_0−1/4)t+O(t^(3/2)).

The same convergent expansions give f(t)=−(log t)/2+O(√t) and its differentiated form. A complete independent derivative proof is supplied in the adjacent elliptic directory; it gives the stronger global bound 0<−t f′(t)≤1 without differentiating an unspecified asymptotic remainder.

Set a_1=ψ(1) and C_B=4∫_0^1ψ. Integration by parts first on [ε,1] yields

2∫_ε^1 f=8∫_ε^1ψ−8a_1+4(1+ε)ψ(ε).

The expansions prove convergence and permit ε→0, giving 2∫_0^1f=2C_B−8a_1+4a_0. For the constant's equality with original ECL16, retain the input primitive C_B=9−8log2+F(2,π) and the definition a_1=2(1−log2)−λ(2,π)/4. Then

2C_B−8a_1+4a_0=4a_0+2+2F+2λ.

ECL14 at α=2 gives F=−λ/2−3+L. Thus this expression equals 4a_0+λ−4+2L, and the ECL16 expression 4a_0−10−2F+4L equals the same scalar. This proves the exact coefficient equality, including the factor2, without comparison of numerical fits.

## Exact native-tail factorization

Let K_N be the full upper evaluation covariance, K^-_{N−v} the lower evaluation covariance, and retain the original TAC5 conductor restriction K_{C,N}, transported analytic quotient Dhat_N, and final low quotient Q_{v,N}. Define the original signed discrepancies

e_N^C=log det K_{C,N}−log det K^-_{N−v},
ε_N=log det Dhat_N−log det D_{N−v},
l_N=log det Q_{v,N}.

TAC6 is the exact identity det K_{C,N} det Dhat_N det Q_{v,N}=|det F|² det K_N in the unchanged frames. On logarithms it gives

log det D_{N−v}=log det K_N−log det K^-_{N−v}−e_N^C−ε_N−l_N+log|det F|².

The fixed frame term cancels under tail_R z=z_{2q−1}+z_{2q}−2z_{q+R}. NTG15 and NTG20 show that tail_R log det D is precisely Σ_{r=R+1}^q θ_rγ_{r,s}. The covariance row identity gives upper row τ^+_r=log ν^+_r−log h_{q+r,s} and lower row τ^-_{m+r}=log ν^-_{m+r}−log h_{q−v+r,s}, at exactly these shifted cutoffs. Therefore

Σ_B θ_rγ_r=Σ_B θ_r(τ^+_r−τ^-_{m+r})−tail_R(e^C+ε)−tail_R l.

The full low quotient is retained: TAC6b proves Q_{v,N}=conjugate(G_{L,N}^{−1}), and LRP proves 0≤tail_R l≤B^L=O_actual(q). If finite input intervals give |e_N^C|≤A_N^C and |ε_N|≤A_N^A, a fully specified admissible error is

E^nat=Σ_B θ_r(e^+_r+e^-_{m+r})
      +Σ_{N=2q−1,2q}(A_N^C+A_N^A)
      +2(A_{q+R}^C+A_{q+R}^A)+B^L,

where e^± are the maximum absolute deviations of their actual covariance row interval endpoints from G(n_±,row). This preserves the factor2 at q+R. The input row estimates and all-rank endpoint bounds give O_actual(q). In particular no independently favorable signs or endpoint extrema are substituted for the actual native tail.

## Complete finite-difference proof

The separate integration-ready `FINITE_COMPARISON.tex` proves every step and supplies the finite allowance

e^cmp(r)=Δ²/(2r)+Δℓ_s/Q+Δ²/(2Q)+2vP_1+v log^+((Q+ℓ_s)/r),
P_1=−ψ′(1)>0.

It derives (∂_n−∂_r)G(n,r)=f(r/n), integrates along exactly x↦(x,q+ℓ_s+r−x), and retains the original v displacement. Its logarithmic estimate uses log(1+x)≤x for every x≥0; it assumes no small Δ/r. This proves

|G(q+ℓ_s,r)−G(Q+ℓ_s,m+r)−Δ f(r/q)|≤e^cmp(r)

for every integer r≥1. Summing with the original weights gives E^cmp=O_actual(q log q), and more precisely O_actual(q{1+log(q/(R+1))}) on B. This step introduces no alternate norm or minimum.

## One-sided slack mechanism and exact trial

The original conductor maps each upper monic affine fibre bijectively to the original relation fibre through

T_A(χ_a P)/ℓ_r=u_r+Σ_{t<r}p_t(ℓ_t/ℓ_r)u_t,
ℓ_t=μ_v binom(q+t,v)≠0.

The inverse is p_t=z_tℓ_r/ℓ_t, so no coefficient direction is omitted. For the original upper minimizer P^+_r set w_r=T_A(χ_aP^+_r)/ℓ_r and τ_r=||w_r||². If V_{<r}=span(u_0,...,u_{r−1}), the unique attained vector is (I−P_{V_<r})w_r. Pythagoras proves τ_r=η_r+||P_{V_<r}w_r||²≥η_r with the entire old Gram in the projection.

Use the un-intersected conductor endpoint U satisfying τ_r≤exp(U_r)ν^-_{m+r}. Then 0≤log(τ_r/η_r)≤U_r−γ_r. A smaller endpoint min(U,NIB) controls γ_r but need not control this particular τ_r; the revised bridge explicitly avoids that substitution.

Write h_r=Δf(r/q). The covariance and finite-difference steps give |Σ_B θ_r(γ_r−h_r)|≤E^T=E^nat+E^cmp, and the upper-envelope input gives E^U=Σ_B θ_r|U_r−h_r|. Direct subtraction yields

0≤Σ_B θ_r(U_r−γ_r)≤E^U+E^T.

Pointwise |γ_r−h_r|≤U_r−γ_r+|U_r−h_r| because γ_r≤U_r. Summation gives the weighted L1 bound 2E^U+E^T; the projection bound gives the claimed trial slack E^U+E^T. No pointwise lower profile is inferred.

## Full row extension and uniform determinant rate

The independent attained-tail reviewer establishes the input envelope on 2≤r≤q+32a. NIB controls the two actual small rows γ_0,γ_1=O_actual(a log q). The logarithmically singular profile is used only at positive indices.

Since f is positive decreasing and integrable, writing J=∫_0^1f gives

0≤qJ−Σ_{r=1}^q f(r/q)≤q∫_0^{1/q}f.

Therefore H=Δ[2Σ_{r=1}^q f(r/q)−f(1)] satisfies

0≤ΔqC_partial−H≤Δ[2q∫_0^{1/q}f+f(1)]=O(a log q).

The evaluated actual total T=16C_partial aq−128qlog a+O_actual(q) equals ΔqC_partial+O_actual(qlog q), retaining the exact discrepancy 48C_partial q−128qlog a. Removing the actual rows0 and1 and their two original weights gives |Σ_{r=2}^q θ_r(γ_r−h_r)|=O(qlog q). Repeating the one-sided argument on this range yields the complete L1 estimate there, and the attained row1 bound adds only O(a log q). The trial assertion is confined to r≥2, as required.

For every 0≤p≤r≤q, NTG25 proves

log det(I+Y*Ω_p^(−1)Y)=Σ_{j=p+1}^rγ_j,
Y=[x_{p+1},...,x_r].

Restricting the global absolute sum and applying the same monotone mesh comparison bounds its difference from Δq∫_{p/q}^{r/q}f by O(qlog q), uniformly including p=0 and p=r. Since Δ/a=16−48/a and ∫f is finite, division by aq gives the claimed uniform O(log a/a) rate. The full old inverse and the entire later cross pairing remain in NTG25. The two-endpoint tail repeats this with weights2 except its last row and has coefficient32 with the same error order.

For any positive-index set of d≤q rows, positivity and decreasingness bound its profile sum by the first d values. The inequality Σ_{j=1}^d log(q/j)≤d{1+log(q/d)} gives the stated O_actual(ad{1+log(q/d)}+qlog q) budget. If row0 belongs to the set, its original O(a log q) allowance is retained and absorbed by the displayed bound. For d=q+1 use the stated q-row estimate plus the original row0 term. The empty set has zero return. For d=o(q), d/q·[1+log(q/d)]→0 and log q/a→0, so every such set has o(aq) return.

## Obligation matrix and remaining scope

| Obligation | Result |
|---|---|
| Original GRE6–8 Robin sign, endpoint motion and source parameters | Passed by raw-source comparison |
| Exact f/ψ identity and C_partial coefficient | Passed, complete algebra above |
| Common finite parameter domain | Repaired explicitly in revised PCB0 |
| Nonzero elliptic implicit derivative and logarithmic derivative bound | Passed; independent integral proof supplied |
| Finite-difference path, including ℓ_s and v | Passed; explicit finite allowance supplied |
| Tail endpoint weights and conductor/native/low factor signs | Passed from TAC6 and NTG15,20 |
| Full preceding relation Gram and lower monic minimum retained | Passed from fibre bijection and NTG/TAC minima |
| Weighted L1 and optimized-trial inequalities | Passed using original un-intersected U |
| Full positive row range and mixed-determinant quantifiers | Passed with other reviewer's all-row envelope input |
| New covariance, transport and norm input estimates | Out of scope of this independent combination audit; separately assigned |
| Individual allocation, arithmetic correction or projected pairing sign | No conclusion claimed or inferred |

No further gap was found in the exact combination after the domain and endpoint clarifications. No Lean execution, numerical proof, compilation, publication or modification of the root bridge was performed by this reviewer. Routine commands read source spans using `Get-Content`, located tags with `rg`, and recorded SHA256 hashes with `Get-FileHash`.
