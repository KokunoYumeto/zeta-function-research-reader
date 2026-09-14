# Independent review of the full low-endpoint transport

Status: accepted. No mathematical correction required in LET1–21.

The reviewed source is `next_bulk_density/future_hankel/LOW_ENDPOINT_TRANSPORT.tex`, SHA256 `a31250b693b9e687481bc7bfa7638707013930c4bfb9b6a8f39c201779d02a44`. All 348 source lines were read. This is a source-level mathematical review; no build, visual inspection, or publication was performed. Original source bytes were preserved.

The exact source definitions and finite bounds used below were compared with BRD23–24 (Gamma source), CTR1–16 and CTR23–54 (coefficient spaces, source maps, original high-endpoint transport and moment calculation), and GSR1–8 (all four original Gamma endpoint identities). BRD was already independently accepted; this review did not rerun its full audit.

## 1. Original objects and the scalar coefficient map

Keep k=4l+1, e=1+k(m−1), q=e(k+1)^2, c=k/2, d=δ², g=γ², ε=2^-10. The root displacements are exactly ζ_ab=(2a−k)δ+i(2b−k)γ, with multiplicity e. Thus their total number is q and |ζ_ab|≤k√(d+g). LET4 gives k√(d+g)/q≤ε/2 and t_(l−1)/q≤ε. Neither bound changes the original coordinate S=c+iy.

On the compact bulk B, T_pow:u↦(iy)^q u and T_χ:u↦χ(c+iy)u are injective maps from C into L²(B,σ(y)dy). The multiplier U=χ(c+iy)/(iy)^q and its inverse are bounded because both numerator and denominator are continuous and nonzero there. Direct multiplication proves UT_pow=T_χ and UM_f=M_fU. These maps retain f and χ literally. The scalar argument has no r≥l requirement: it compares two positive integrals on the one-dimensional coefficient space.

For a≤ψ≤b, both ∫F₀e^ψdw/∫F₀dw and ∫e^ψdw/∫dw lie in [e^a,e^b]. Their quotient lies in [e^(a−b),e^(b−a)]. This proves LET6 directly even when l>1.

## 2. Density expansion and numerator sign

Since iy−ζ=iy(1+iζ/y), absolute convergence gives log(|χ(c+iy)|²/|y|^(2q))=2e Re Σ_ab log(1+iζ_ab/y). The root permutation (a,b)↦(k−a,k−b) cancels all odd powers. The exact second-power sum is e Re Σζ_ab²=qk(k+2)(d−g)/3. For τ=k²(d+g)/y²<1, the remaining even terms have modulus at most qΣ_(j≥2)τ^j/j≤qτ²/[2(1−τ)]. Consequently LET7 and its coefficient a_k=k(k+2)(d−g)/(3q) are correct, with all root multiplicities retained.

Because z^-2 lies between 64^-2 and ε^-2, osc ψ≤E₀=|a_k|(ε^-2−64^-2)+2δ_χ. LET6 gives |d_χ|≤E₀. The exact multiplication polynomial gives |f(c+iy)|²/|y|^(2l)=Π_(j<l)(1+t_j²/y²). Each factor is at least one. Summing t_j²=(2j+1/2)² gives S₂=l(16l²−12l−1)/12, and log(1+x)≤x gives 0≤d_f≤Δ_f=S₂/(q²ε²). The correction from f therefore belongs only on the upper side.

## 3. All four scalar tails

The original density satisfies C_L e^(-π|y|)≤σ(y)≤C_U e^(-|y|), with C_L=π/Γ(3/4)², C_U=Γ(1/4)²/(2π√cos1), and C_U/C_L=1/√cos1. These constants agree with the Euler contour and reflection proofs in BRD23–24.

Pairing ζ with −ζ gives |χ(c+iy)|²≤(y²+k²(d+g))^q. On 1≤z≤2, it gives |χ(c+iqz)|²≥q^(2q)(3/4)^q; |f(c+iqz)|²≥q^(2l). On |z|≤ε, the corresponding upper bounds are q^(2q)(2ε²)^q and q^(2l)(2ε²)^l. Before the harmless enlargement by 8^(2q), the actual inner/bulk ratio for s=0,l is bounded by

2ε(C_U/C_L)(4/3)^q e^(2πq)(2ε²)^(q+s).

Since (2ε²)·8²=2^-13 and (2ε²)^s≤1, this implies LET12. For the reference powers the same calculation, without the (4/3)^q factor and with ε^(2q+2s), gives the stated smaller constant. The insertion of 8^(2q) does not invoke a high-rank polynomial estimate: the coefficient is exactly the constant one.

For the far tails D_s=2q+2s≤5q. The inequality log(z/64)≤(z−64)/64 gives the exact integral bound 64^(D_s)e^(-64q)/(q−D_s/64), with denominator at least 59q/64. Here a_k<0 follows from d<1/4 and g>4. Thus ψ_χ(qz)≥a_k−δ_χ(1) on [1,2] and ψ_χ(qz)≤δ_χ(64) on the far region. These are precisely the signs used in LET14. The multiplication by f contributes the far factor exp(Δ_(f,s)(64)); it contributes no adverse bulk factor because |f|²≥q^(2l).

The total logarithmic correction is at most

(7/60+1/24+1/24+1/8192)q=(1/5+1/8192)q<q/4.

Indeed −a_k≤qτ₁(k+2)/(3k)≤7q/60; each δ bound is q/24; and S₂≤4l³, 2l≤q give Δ_(f,l)(64)≤q/8192. With π<4 and log2<1, 64−2π−5log64>26>20. Therefore the original far ratio is at most 128e^(-19q)/(59q√cos1), which is at most the chosen κ_F. Both reference correction factors are one, so the same κ_F applies to them. All factors of two and the Jacobian dy=q dz agree in the ratio.

The inner base decays exponentially: log(4/3)<1/3, log2>2/3 and π<22/7 imply log((4/3)2^-13e^(2π))<−43/21<−2. Hence every one of the four scalar logarithmic tail corrections is in [0,L₁], exactly as LET16 states.

## 4. Exact low ratio and the original moment indices

Write the four full integrals as H=H^B exp(t_H). The exact full-minus-bulk decomposition is

log r_χ − log(m_(2q+2l)/m_(2q))
= d_χ+d_f+t_(χ,f)−t_(χ,0)−t_(pow,l)+t_(pow,0).

The two positive and two negative tail terms together lie in [−2L₁,2L₁]. This proves LET17–18 with a₀=E₀+2L₁, b₀=a₀+Δ_f. The literal power moments are m_(2q+2l) and m_(2q), not moments in a rescaled y/2 coordinate. CTR50–53 use the same σ(y), and the mass √(2π) appears in both moments before cancellation.

The explicit bounds |a_k|≤|d−g|/(3e), δ_χ≤2(d+g)²/(3e³k²ε⁴), and Δ_f≤1/(16e²kε²) follow from q=e(k+1)² and S₂≤k³/16. At fixed δ,γ,m these prove O(1) for m=1 and O(k^-1) for m≥2, including the exponentially small tails. These are errors in the logarithm of the actual scalar moment ratio, with asymmetric finite endpoints retained.

## 5. Four-endpoint Gamma identity and arithmetic receiver

GSR3–8 give r_(q−1)=0, r_q=1, r_(2q−1)=q, r_(2q)=q+1, and A_N=log D_(l,N)−log R_N. The empty relation determinant at q−1 is one; the relation determinant at q is r_χ. The four source-mass contributions q log β_k cancel with the actual signs (1,1,−1,−1). Therefore

T_k=P_k−log r_χ+log R_(2q−1)+log R_(2q),

with exactly the P_k in LET19. No endpoint or mass factor is omitted.

CTR48 applies to the high ranks q and q+1, which both satisfy r≥l. Their errors add to [−A,B], where A=2lE₀+2(L_q+L_(q+1)) and B=A+(2q+1)Δ_f. The low error is [−a₀,b₀] and occurs with a minus sign. Defining W_k as LET19 therefore gives T_k−W_k∈[−A−b₀,B+a₀]. Since R_k^0−R_k^σ=−T_k, both intervals in LET20 follow with exactly their printed signs.

The moment matrices retain the original mass: M_(a,r)=√(2π)Q_(a,r), and det M_(a,r)=(√(2π))^r det Q_(a,r). Numerator and denominator have the same r, so their displayed mass factors cancel. The fixed coefficient transformation P(S)↦P(c+iy) has J_(h,j)=binom(j,h)c^(j−h)i^h and |det J|=1; this proves the precise transport to the real Hankel determinant in CTR36. Thus W_k depends only on q,l and the unchanged σ. The packet parameters δ,γ remain in the finite error bounds, threshold and original maps.

At fixed parameters, A,B=O(k/e); a₀,b₀=O(1/e) with smaller remainder terms. Thus the complete Gamma error is O(k)=o(q), and O(1) for fixed m≥2. No value of W_k is asserted or needed for this verified reduction.

Finally δ_σ∈[−a_−,a_+] and Δ_Γ=δ_σ−T_k imply

B₀−W_k−B−a₀−a_− ≤ B_ar ≤ B₀−W_k+A+b₀+a_+.

This is exactly LET21. Subtracting the unchanged 4q log(D_h k) shifts both endpoints equally. No unsigned estimate has replaced the Gamma sign.

## Review conclusion

All LET1–21 statements are accepted in the displayed original-parameter domain. A separate independent scalar reviewer also checked LET1–18 and found no defect. The current result supplies a complete finite low-endpoint transfer and the signed whole Gamma receiver. Evaluation of W_k remains the explicit next calculation; this receipt does not assign it a value or claim a Riemann-hypothesis conclusion.