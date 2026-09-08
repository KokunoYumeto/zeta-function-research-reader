# Independent review: actual angular momentum and nonlinear arithmetic Mellin equation

Date: 2026-09-08. Reviewer: full_stress_review. This is a bounded mathematical review of the complete new TeX proof. No TeX, source manuscript, public record, or numerical artifact was changed by this reviewer.

## Identity and exact scope

Complete reviewed file:

[local]/Documents/math/output/dbn_ns_rh_20260908/tex/ns_angular_mellin.tex

SHA-256: 59a477ff19fc593fb1f5550c98f34346f7cf5365b1fe0372e6935934e0263278.

The proof was read from beginning to end, including the projection section, complete stress and cutoff-sum formulas, Mellin boundaries, arithmetic trace, all inverse series, corrected-field circle asymptotic, and local zero factorization.

The actual 166-page primary source is the released Navier–Stokes PDF at:

[local]/Documents/math/output/navier_stokes_research_2026-09-08/downloaded_public_release/navier-stokes.pdf

SHA-256 directly checked: 0e779481c4da40bd28d1e642e1d8ca57447d129610df28dfa5a11e9af8ae228f.

Read through its extracted text, SHA-256 f83414ea543ffd89910b9b8a35d1680a2e3295246c91cbedf54e719a7bc316d0. For this review directly read Theorem 3.1, the original similarity-coordinate definitions, the beginning of Section 5 specifying axisymmetric slow corrections, and the complete Proposition 9.9 proof (including its Step 5). Sections 3.3–3.4 and the actual source localization/force/growth/scaling (10.4)–(10.11), (10.20)–(10.23) had been directly read in the immediately preceding full-stress review. The complete ns_public_witness.tex, SHA-256 ae7775c16c2c5188d4431eaf27d6c861c7e3f69f912f03feb5466cf1ea8eac93, was also read in that review.

The source existence and all-order source induction remain imported. This review is not an independent validation of all 166 pages or of the Lean development. No new numerical checker count is claimed.

## Verdict

PASS at the explicitly retained source-dependent scope. No mathematical correction was found. The input is the actual corrected, localized velocity and its complete nonlinear fluxes; the exterior heat profile is not substituted. The projection's kernel, a section, full stress terms, measure factors, shifted moments, inverse order, and actual concentrating-circle remainder are all retained.

## Check-by-check reasoning

### Cartesian angular averaging and the axis

The angular moment is the Cartesian expression x₁u₂−x₂u₁. Its average, and the averages defining P,Q,F, are smooth rotation-invariant scalar functions of the first two Cartesian variables. Restriction to the real radial axis is smooth and even. Taylor expansion with differentiated remainder gives the asserted smooth half-line dependence on σ=r²/2, also after all fixed parameter derivatives.

B,Q,F vanish at the Cartesian origin in those variables and their odd radial powers average to zero. Their first possible order is r²=2σ.

For P, the quadratic term is

    (x₁a+x₂b)(x₁b−x₂a)
      = ab(x₁²−x₂²)+(b²−a²)x₁x₂,

where a,b are the two constant velocity components on the axis. Both angular averages vanish. The averaged constant term is zero, and odd powers again vanish. Therefore the first possible order is r⁴, proving P=O(σ²), not merely O(σ). This uses no hidden assumption of axisymmetry of the full velocity and no unsupported polar regularity.

### Projection, section, kernel, and full correlations

For RB=[B/(2σ)](−x₂,x₁,0), the cylindrical azimuthal component is B/r, so ΠRB=B exactly. The factor 2 is required by 2σ=r². Since B(0)=0, its quotient by σ has the smooth extension ∫₀¹B′(aσ)da. Its Cartesian divergence vanishes by cancellation of the two derivatives; compact support and smoothness survive.

Writing u=RB+w gives u_r=w_r, u_z=w_z and u_θ=B/r+w_θ. Direct multiplication yields exactly

    P=rB⟨w_r⟩+r²⟨w_rw_θ⟩,
    Q=B⟨w_z⟩+r⟨w_zw_θ⟩.

The inverse retains w, with its stated zero angular-momentum average. There is no claim that B alone reconstructs u or closes the nonlinear dynamics. In particular the nonzero mean transport and both quadratic correlations remain present.

### Complete Cartesian equation and stress torque

The product rule gives

    Δ(x₁u₂−x₂u₁)=x₁Δu₂−x₂Δu₁+2(∂₁u₂−∂₂u₁).

Thus the viscous correction is −2νω_z. The pressure contribution is −(x₁∂₂−x₂∂₁)p=−∂_θp. The two coordinate derivatives in material transport cancel as u₁u₂−u₂u₁. This verifies the full unaveraged equation and its signs.

Angular averaging removes angular derivatives by periodicity, including the actual pressure torque. The resulting radial diffusion is B_rr−B_r/r=2σB_σσ, and radial convection is ∂_σP since (1/r)∂_r=∂_σ. These identities give the printed PDE with unchanged viscosity and both fluxes. Axis smoothness extends it to σ=0; P=O(σ²) in particular gives ∂_σP(0)=0.

For an arbitrary Cartesian stress with row convention (div T)_i=Σ_j∂_jT_ij,

    x₁∂_jT_2j−x₂∂_jT_1j
      =∂_j(x₁T_2j−x₂T_1j)−(T_21−T_12).

The nonsymmetric extra torque therefore has the negative sign printed. When T is symmetric, the flux vector has radial component r T_θr and axial component r T_θz; its averaged divergence is precisely ∂_σ⟨r²T_θr⟩+∂_z⟨rT_θz⟩. The source's original residual sign still determines which side of the equation receives this quantity. No unproved identification of auxiliary and physical averages occurs.

### Actual cutoff sum, not an exterior or leading-only input

Source (9.21) forms the summed potentials and direct azimuthal components. Source (10.4) cuts off the potentials before curl. Linearity gives the chapter's localized positive-stage increment curl(c χ(a_jq)A_j)+c χ(a_jq)b_j, with all derivatives of both cutoffs retained.

For t<1, the source concentration coordinate q satisfies q≥1−t>0 and is independent of θ. Source local finiteness therefore applies on every compact circle, and every derivative is represented by the same locally finite sum in a neighborhood. The displayed ordered double sums for P and Q contain every diagonal term and both orders of each unequal pair. Finite initialization is part of the base rather than silently omitted.

The chapter appropriately does not exchange the terminal limit with an uncontrolled infinite sum. Source residual flatness and existence enter through the actual realized field.

### Mellin convergence and shifted viscosity

With dσ=r dr and the normalized angular average already fixed, the lower-axis orders give holomorphy of B̂,Q̂,F̂ for Re s>−1 and of P̂ for Re s>−2. Compact support controls the upper endpoint. Logarithmic powers from complex differentiation are integrable on compact substrips.

For Re s>0 all three printed lower boundary terms vanish. Two integrations by parts give

    ∫2σB″ σ^(s−1)dσ = 2s(s−1) B̂(s−1),

whereas one integration gives ∫P′σ^(s−1)dσ=−(s−1)P̂(s−1). Thus the viscosity coefficient is exactly 2νs(s−1) and every s→s−1 shift is necessary. No factor from r dr is missing.

The Mellin inverse follows from g(u)=e^(cu)a(e^u), c>0. Its derivatives decay exponentially as u→−∞ and vanish for sufficiently large positive u. Thus g is Schwartz. The sign c−iη in the forward transform and e^(iη logσ) in the inverse agree. The Gaussian-regularized inversion argument retains 1/(2π) and has the stated integrable domination.

### Trapezoidal estimate and the arithmetic multiplier

The second dilation gives ∫ψ=∫φ−(1/2)∫φ(x/2)dx=0, and ψ(0)=0 because a(0)=0. On an interval of length x, the quadratic kernel (v−nx)((n+1)x−v) is at most x²/4. The summed trapezoidal identity gives xΣ_{n≥1}ψ(nx) equal to half the sum of these kernel integrals. Dividing by x yields exactly

    |A_h a(x)| ≤ x||ψ″||₁/8.

There is no missing endpoint term or factor 2. This establishes the claimed Mellin domain Re s>−1 for the trace. The locally finite sum is smooth for x>0 and vanishes above a fixed upper support bound.

For Re s>1 absolute Fubini is valid and each dilation contributes its exact b^(−s). The multiplier is therefore

    W_h(s)=ζ(s)(1−2^(s−1))(1−2^(h−s)).

Only ζ has a pole, and its pole at one is canceled by the first factor. Thus W_h is entire. The identity theorem extends the equality on the stated connected half-plane. The exterior profile's gamma factor is not present here unless supplied by that particular input, exactly as the chapter explains.

### Ordered inverse maps and equation at multiplier zeros

At each x>0 the arithmetic inversion double sum is finite. The divisor identity Σ_{d|m}μ(d)=δ_{m1} gives ψ exactly. Both dyadic formulas telescope:

    Σ_{j=0}^J2^(−j)ψ(x/2^j)
      =φ(x)−2^(−J−1)φ(x/2^(J+1)),
    −Σ_{k=1}^K2^(−kh)φ(x/2^k)
      =a(x)−2^(−Kh)a(x/2^K).

Their endpoint remainders vanish. Each differentiated summand has the additional dyadic derivative factor, giving the claimed local uniform differentiated convergence. The order is important: first recover ψ by the finite arithmetic sum at each argument, then recover φ, then a. No unrestricted triple-sum interchange is made.

Multiplying the Mellin equation by W_h(s) gives the inverse-retaining equation exactly. Further multiplication by W_h(s−1) gives the printed division-free shifted relation on Re s>0. Each shifted actual transform is holomorphic there. At a zero of W_h(s−1), the cross-multiplied identity alone can lose pointwise information; the chapter explicitly retains the prior inverse formula and does not claim otherwise.

### Source-specific full-circle growth

This extension from the positive x₁ axis to a circle is supported by the source, not inferred from a single-angle asymptotic. Section 5 explicitly constructs axisymmetric slow corrections, and Proposition 9.9 Step 5 fixes X_in∈(0,X_a), where all annular corrections vanish. The remaining cutoff-summed slow field is independent of θ in its cylindrical components. The localization cutoff is axisymmetric and equals one on the entire sufficiently small sampled circle. Consequently the same actual swirl and the same remainder hold around that circle.

Under the original viscosity scaling, r=√(2νX_inτ), u_θ=√ν τ^(−1/2−h)(e_0+R_*). Their product is exactly

    B(νX_inτ,0,1−τ)=ν√(2X_in)τ^(−h)(e_0+R_*).

The angular mean contributes no additional 2π because it is normalized and the sampled value is independent of θ. The parameter h and the remainder are the chosen source ones. The proof correctly avoids claiming that the un-inverted arithmetic trace has this same pointwise blowup rate: the inverse series is not asserted uniformly bounded in this moving-axis limit.

### Local zero product

On h<Re s<1 neither dilation factor vanishes. Multiplication of the complete local Taylor factors gives the stated addition of finite orders m+n, and exactly m when the actual corrected-field Mellin factor is nonzero. At slices where an input moment is identically zero, its product is identically zero; no finite multiplicity is asserted by the chapter's “if that factor has order n” clause. No nonvanishing of these actual moments and no off-critical ζ zero has been assumed.

## Final scope

This establishes an independently reviewed exact projected nonlinear equation and a recoverable arithmetic image of the actual source concentration. It does not alone establish RH falsity, a new zero of ζ, a uniform inverse bound at the concentrating axis, or a closed scalar PDE for B without its retained velocity kernel and flux data.
