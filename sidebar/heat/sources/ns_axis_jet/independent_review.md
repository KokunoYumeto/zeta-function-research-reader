# Independent review: exact fixed-axis arithmetic jet

Date: 2026-09-08. Reviewer: full_stress_review. Read-only mathematical review; this record is the only file written by the reviewer.

## Exact object and verdict

Complete target read:

tex/satellites/29l_ns_axis_arithmetic_jet.tex

SHA-256: e43586e0f117344e45536bc8792228e386f2ba65f83bfc74f54264398762a2ac.

Verdict: PASS at the explicit imported-source scope. No mathematical correction was found. The source's exact axis datum, zero higher-order axis data, cutoff realization, and unchanged viscosity scaling imply the claimed exact jet. The derivative of the original arithmetic trace, not merely of its inverse, has the displayed singularity. The Mellin residue independently matches it.

This is not a certification of the entire source existence theorem, an RH disproof, or a claim that the growing residue is a nontrivial zero of ζ.

## Primary source and reading

The current 166-page primary manuscript is:

[local]/Documents/math/output/navier_stokes_research_2026-09-08/downloaded_public_release/navier-stokes.pdf

SHA-256: 0e779481c4da40bd28d1e642e1d8ca57447d129610df28dfa5a11e9af8ae228f.

The directly read extracted text current_pdf_extracted.txt has SHA-256 f83414ea543ffd89910b9b8a35d1680a2e3295246c91cbedf54e719a7bc316d0.

This review directly read the following relevant source content, rather than inferring it from a summary:

- Source pp.45–49: the coefficient construction, complete formulas (5.1)–(5.7), Lemma 5.1 and its proof, and the opening of the radial extension/moment construction. In particular the lemma explicitly prescribes all three zero positive-order axis values and says the leading axis traces are unchanged.
- Source pp.60–62: Proposition 5.5 and its complete proof, including the unchanged order-zero term, physical potential cutoffs, derivative corrections, common supports, and local finiteness.
- Source pp.144–147: the axis datum (B.3), coefficient-space argument, and the statement and initial proof formulas of Proposition B.2. The relevant statements are the integral based at zero and Φ(0,η)=1 in (B.12).
- Source p.37: the actual leading-profile assembly's displayed axis datum. This confirms directly that continuation into the outer profile has not introduced an additional multiplicative axis amplitude.
- Source pp.114–118, including Proposition 9.9 and (9.21), and the final localization (10.4), were directly read during the immediately preceding independent reviews against this same source hash. They establish the locally finite actual sum, vanishing annular representatives near the axis, and the cutoff equal to one near the singular point. Those reads are recorded in FULL_STRESS_REVIEW.md and ANGULAR_MELLIN_REVIEW.md.

The Euler–Maclaurin identity and remainder in the existing satellite 29g, around eq:nh-EM and its ensuing endpoint-derivative argument, were directly read and checked. The reviewed proof cites that complete local derivation as well as its historical source; it does not rely only on a formal asymptotic mnemonic.

No numerical process, Lean invocation, browser operation, source edit, or new symbolic-check count was used for this review.

## Source-to-axis chain

### The exact coefficient and all positive orders

Source (5.1) has

    uθ,n = r q^(−A−1/2+2nh) ϕ_n/C,
    A=1/2+h.

Consequently uθ,n/r=q^(−1−h+2nh)ϕ_n/C, with the exact power and unchanged C printed in the chapter.

Lemma 5.1 prescribes ϕ_n(0,η)=0 for every n≥1, not merely a small bound. The radial extensions preserve the inner solution and their moment corrections are away from that inner interval. Proposition 5.5 preserves order zero and realizes positive orders through χ(c_nq). At fixed preterminal z,t, q>0 and c_n→∞, so only finitely many such terms are active locally.

The q coordinate depends on z,t, not on r. Thus no radial derivative of χ(c_nq) enters the azimuthal quotient's evaluation at r=0. Cutoff differentiation in the Stokes streamfunction affects the radial and axial components, not this azimuthal quotient. For each active positive-order azimuthal term the smooth axis value is exactly zero.

### Leading axis datum and preservation in the actual field

Source (B.3) gives ϕ_*(η)=exp(Λ∫₀^η ζ_*(w)dw); hence ϕ_*(0)=1. Proposition B.2 gives ϕ=ϕ_*Φ and Φ(0,η)=1. Source p.37 prints this same axis datum in the assembled leading profile, so its value is not altered by a later outer matching or amplitude convention.

The finite initialization and all later annular correction representatives vanish on an axis neighborhood at each t<1. Since locally only finitely many stages are present, their derivatives vanish on a common neighborhood for each such time. The remaining azimuthal base potential's curl has no azimuthal component. The final cutoff is identically one near the origin for sufficiently late preterminal times, so its derivative corrections vanish there.

At z=0, the original similarity equations imply η=0 and q=τ exactly. Therefore the smooth quotient of the actual complete field satisfies

    (uθ,*/r)(0,0,1−τ)=τ^(−1−h)/C

for the source-determined small-τ interval. This is an equality of the realized field's axis trace, not a statement about a truncated approximation. The absence of a remainder at this axis value is justified by the exact zero of every positive-order coefficient, rather than by discarding its asymptotic error at nonzero X_in.

## Viscosity, angular measure, and fixed-axis jet

Under the actual source scaling, r_*=r/√ν and uθ,ν(r,0,t)=√ν uθ,*(r_*,0,t). The two factors √ν cancel in the quotient uθ,ν/r. Passing to its smooth extension at r=0 is justified before the terminal limit. Thus its exact axis value is independent of the fixed positive ν; this is not a replacement of ν by one.

On the full axis neighborhood the actual remaining field is axisymmetric. With the normalized angular mean and σ=r²/2,

    B_ν(σ,0,t)=r uθ,ν=2σ(uθ,ν/r).

Therefore B_ν(0,0,t)=0 and

    ∂σB_ν(0,0,1−τ)=2τ^(−1−h)/C.

The factor 2 comes from r²=2σ; the normalized angular average contributes no further 2π. This is a derivative at the fixed physical axis, not evaluation on a τ-dependent radial path.

## Arithmetic endpoint map with actual differentiability

For compactly supported smooth a with a(0)=0, direct differentiation of the two dilations gives

    ψ_a^(j)(0)=(1−2^(−j−1))(1−2^(h+j)) a^(j)(0).

The second dilation cancels the integral exactly, and ψ_a(0)=0. Hence the corresponding arithmetic trace has no x^−1 or endpoint-constant term.

For f_j(v)=v^j ψ_a^(j)(v), local finiteness gives

    x^j (A_h a)^(j)(x)=Σ_{n≥1}f_j(nx),  x>0.

Integration by parts j times proves ∫f_j=(-1)^j j!∫ψ_a=0. The boundary factors vanish at zero and by compact support at infinity. Leibniz's rule gives f_j^(r)(0)=0 for r<j, and r!ψ_a^(r)(0)/(r−j)! for r≥j.

The existing Euler–Maclaurin identity has remainder at most

    ||B_(2M)||∞ x^(2M−1) ||f_j^(2M)||₁/(2M)!.

After dividing by x^j and choosing 2M−1>j, this tends to zero. Terms with negative powers of x have zero coefficients. The only possible constant Bernoulli term for j≥1 has 2k−1=j; its value is

    −B_(j+1) ψ_a^(j)(0)/(j+1).

For even j≥2 it is absent, agreeing with the vanishing odd Bernoulli number. For j=0 the constant is −ψ_a(0)/2=0.

This argument is applied separately to every differentiated series, not obtained by differentiating an uncontrolled asymptotic remainder. Every derivative on x>0 has a finite limit at zero. The fundamental theorem of calculus, using boundedness of the next derivative, identifies these limits successively as genuine derivatives of the extension. Thus the smooth endpoint claim is established.

For j=1, B₂=1/6 and the formula is

    −(1/12)(3/4)(1−2^(h+1))a′(0)
      = (2^(h+1)−1)a′(0)/16.

Both the sign and denominator 16 are correct. The coefficient is positive for the fixed source h>0.

Parameter derivatives have the same compact-support and smoothness hypotheses uniformly on each compact preterminal parameter set. Applying the argument to those differentiated inputs proves the compatibility needed to differentiate the exact endpoint identity in time. No uniform bound as t↑1 is claimed or needed.

## The resulting singularity

Substituting the actual ∂σB_ν gives

    ∂x A_hB_ν(0,0,1−τ)
      = (2^(h+1)−1)/(8C) · τ^(−1−h).

The trace value at x=0 is still exactly zero. Its first derivative is the displayed positive divergent quantity. The C¹ seminorm on every fixed interval [0,ε] dominates the absolute endpoint derivative, so a continuous terminal extension in that C¹ topology is excluded.

Time differentiation has no extra minus sign: d_t(1−t)^−α=α(1−t)^−α−1. Therefore the retained rising factorial (1+h)_m and exponent −1−h−m are correct for every finite m, on the open preterminal interval.

The chapter retains the section and zero-angular-moment kernel of the full velocity map. Thus the jet is a component of a specified full correspondence, not an assertion that B alone satisfies a closed scalar Navier–Stokes substitute.

## Mellin pole and compensation

For each fixed preterminal parameter, subtracting B_σ(0)σ from B on [0,b] leaves O(σ²). This makes the first remainder integral holomorphic for Re s>−2, while the integral from b to infinity is entire. The explicit term

    B_σ(0)b^(s+1)/(s+1)

has residue B_σ(0), with the positive sign printed. The same construction applies to the now proved smooth arithmetic trace.

The full arithmetic multiplier is

    W_h(s)=ζ(s)(1−2^(s−1))(1−2^(h−s)).

Using ζ(−1)=−1/12 gives

    W_h(−1)=(2^(h+1)−1)/16>0.

Thus the meromorphic continuation of M(A_hB)=W_h MB has at s=−1 the residue

    (2^(h+1)−1)/(8C) · τ^(−1−h),

identical to the direct endpoint calculation. W_h is holomorphic and nonzero at this point, so it cannot cancel this genuine simple pole. Its positive sign requires both dilation factors; the negative value of ζ(−1) alone would give the wrong inference.

This is a pole of the corrected-field Mellin transform and its arithmetic trace. It is not a pole of ζ at −1, and it is not a nontrivial ζ zero. The chapter states this scope accurately.

## Review outcome

No changes requested. The exact source conditions needed for the axis identity are evidenced, all viscosity/angular/radial constants are retained, the endpoint differentiability is proved rather than assumed, and the Mellin residue has the same coefficient and sign. Complete source existence remains imported.
