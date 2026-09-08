# Independent review: full source momentum equation in arithmetic profiles

Date: 2026-09-08. Reviewer: full_stress_review. Bounded, read-only mathematical review; only this review file was written.

## Exact reviewed object and source scope

Target read completely: tex/satellites/29j_ns_stress_arithmetic.tex.

Initial SHA-256: 486f2e0b28292d660bb8a184707280af7f425613c34e35fd21e31da29544c399.

Reviewed SHA-256 after the domain correction: 96bfbb4f7864715e46710ba988376dcc9fbbc5f9b64cd8bebe459c8e8602a902.

The final change adds the preterminal restriction described below. Its changed text was directly reread and its hash directly checked after the parent edit.

Additional complete mathematical text read:

- tex/satellites/29i_ns_actual_witness.tex, including the actual-source substitution and the moving-label compensation.
- [local]/Documents/math/output/dbn_ns_rh_20260908/tex/ns_public_witness.tex, SHA-256 ae7775c16c2c5188d4431eaf27d6c861c7e3f69f912f03feb5466cf1ea8eac93.

The actual current primary PDF was hash checked, not treated as identical to the earlier edition:

- [local]/Documents/math/output/navier_stokes_research_2026-09-08/downloaded_public_release/navier-stokes.pdf.
- SHA-256 0e779481c4da40bd28d1e642e1d8ca57447d129610df28dfa5a11e9af8ae228f.
- Its extracted text current_pdf_extracted.txt has SHA-256 f83414ea543ffd89910b9b8a35d1680a2e3295246c91cbedf54e719a7bc316d0.
- Directly read the extracted content of Sections 3.3–3.4, the localization and force argument from the opening of Section 10 through Lemma 10.3, and the closing growth/scaling calculation (10.20)–(10.23). The source-reading receipt was consulted as a locator, not as a substitute for this content.

The earlier polynomial determinant/inverse and Schwartz theta estimates are explicit dependencies of this chapter. Their complete earlier proofs were not reaudited in this bounded review. The beginning of 29c was read to confirm the actual four-term operator, its derivative sign, and the definitions of w and m. No claim is made to have independently checked all 166 source pages, executed a Lean proof, or established the source existence theorem afresh.

## Verdict

PASS at the stated imported-source scope after the recorded domain correction. No lost coefficient, omitted quadratic interaction, sign error, or reflection error was found in the requested formulas. The input is the complete localized source witness, with source existence and all-order residual estimates retained as imported results.

### Domain correction found and verified

The estimate labeled eq:nsa-flatforce originally said only “on its stated neighborhood.” Source (10.9) is a preterminal estimate, whereas the preceding paragraph discusses the force extension through time one. Since Qν=(1−t)+|x₃/√ν|^(1/(1/2−h)) can be negative after time one, a two-sided version would be false for odd N.

The parent has now explicitly restricted this estimate to 0≤t<1 on the scaled source neighborhood and separated the smooth continuation for t≥1. I reread this correction directly. No coefficient or proof change is needed beyond that restriction.

## Direct checks and retained conventions

### Profile map and inverse

At a fixed real physical point x, real translation gives

    ∫ conjugate(H′(s+Sₐ(x))) H′(s+Sₐ(x)) ds = d_H².

The three profile components are separate coordinates in L²(ℝ;ℂ³), not functions to be summed before inversion. Thus the integral extractor gives c=Jb, and J⁻¹c=b. Conversely, membership in the specified three-dimensional image E_x recovers B exactly. The inverse divides by the strictly positive scalar d_H², never by a pointwise value of H′. The norm is precisely d_H²|Jb|², not d_H²|b|². The physical point remains explicit, so there is no implicit global inverse of the polynomial map S.

Local smoothness and the inverse's differentiation under the integral are justified by bounded shifts and polynomial derivatives on every fixed physical compact set. The connection is asserted on smooth sections of this finite-rank image bundle, not on every unrelated Schwartz-valued section.

### Connection sign, translation mixing, and flatness

Writing hₐ(s)=H′(s+Sₐ), differentiation gives

    ∂ᵢ(Tb)ₐ = Jₐᵢ H″(s+Sₐ)(Jb)ₐ
               + hₐ((∂ᵢJ)b+J∂ᵢb)ₐ.

The operator R_ab sends h_b to h_a because its shift is S_a−S_b. Consequently Γ_i R removes precisely h_a((∂ᵢJ)b)_a. The subtraction of J_ai ∂_s removes the H″ term, leaving T∂ᵢb. This verifies both minus signs and the order Γ_i=(∂ᵢJ)J⁻¹.

Differentiating the inverse matrix gives

    ∂ᵢΓⱼ = (∂ᵢ∂ⱼJ)J⁻¹ − ΓⱼΓᵢ,

and hence ∂ᵢΓⱼ−∂ⱼΓᵢ=[Γᵢ,Γⱼ], with the sign printed in the chapter. Iterated conjugation proves flatness on E, including derivatives of the variable shifts. Ignoring those shift derivatives would not be justified; the chapter does not ignore them.

### Stress columns and complete source increment

With (div R)_k=Σ_i∂ᵢR_ki, every column is separately encoded and recovered. Therefore Σ_i D_i T(R_.i)=T(div R). The cylindrical-to-Cartesian conversion O R_cyl Oᵀ correctly retains derivatives of the moving frame when the physical divergence is taken.

The scalar product rule is D_i(fB)=(∂ᵢf)B+fD_iB for a physical scalar f, since the spectral translations do not change f(x). In particular, for divergence-free w,

    Σ_i D_i(w_i W)=T(Σ_i w_i∂ᵢw)=T(div(w⊗w)).

Expanding the transformed residual produces both u_iD_iW and w_iD_iV, the entire self-interaction, the pressure increment, and the unchanged viscous term −νΣ_iD_i²W. There is no discarded linearized term or factor 2. The source's exact increment identity in Section 3.3 and correction cycle in Section 3.4 agree with this expansion at source viscosity one; the earlier retained spatial scaling supplies general ν.

The source averaged covariance is computed before evaluation of its auxiliary torus variable. The chapter converts and evaluates the physical tensor before T, and explicitly refrains from commuting averaging with the polynomial coordinates. Separating a selected covariance from the actual quadratic tensor leaves the remaining tensor columns in the full increment identity. Thus the chapter transports the actual residual/cancellation identity, but does not claim to reproduce every source induction estimate.

For the actual cutoff potentials, curl(χA)=χ curl A+∇χ×A. The extra term remains in T w and therefore in every linear and quadratic interaction. Local finiteness before terminal time matches source (9.21); the terminal all-order estimate is imported rather than inferred from formal summation.

### Actual force image

Source (10.4)–(10.5) includes the cutoff derivatives and permits nonzero divergence of the force. Source Lemma 10.3 places the extended force in C_c^∞(ℝ³×(0,∞)), supported in K×[0,2]. The viscosity transformation retains this as K_ν×[0,2].

Multiplication by J and the real-shifted H′ sends that force to a compactly space-time-supported Schwartz-valued function. The polynomial weight inequality follows from

    1+|s| ≤ (1+|a|)(1+|s+a|).

For the preterminal flat-force estimate, each fixed derivative of T f contains finitely many derivatives of f. Source (10.9) bounds all of these by the same arbitrarily chosen Qν^N, with ν-dependent constants. All remaining coefficients and shifts are bounded on the fixed neighborhood. This proves the estimate on the now explicit preterminal domain.

### Actual growth and energy constants

At (r,0,0) the stated first two rows of J give (Ju)_1=u_3/2 and (Ju)_2=u_2+3ru_3. Their shifts are both zero. Therefore V_2−6rV_1=u_2H′ as an equality of complete functions, not just a projected coefficient.

The source relation (10.21), after its viscosity map (10.22), supplies u_2=√ν τ^(−1/2−h)(e_0+R_*(τ)). Thus the exact squared norm is ντ^(−1−2h)(e_0+R_*)²d_H². The remainder is a real scalar, since it is defined from the real source component.

Cauchy–Schwarz for the coefficient row (−6r,1) gives √(1+36r²). Using r²=2νX_inτ produces exactly √(1+72νX_inτ). The factor 1/2 is precisely e_0+R_*≥e_0/2 under C_*τ^(2h)≤e_0/2. No source factor has disappeared.

The integrated norm bound is d_H M_ν ||u_ν||₂ ≤ d_H M_ν E_ν. It uses the actual global energy inequality, not an assumed asymptotic for total energy. Coexistence of this integrated bound and the displayed spatial-supremum concentration is valid and is not a claim of divergence at a fixed material label.

### Fourier constants and the complete reflected K input

For the minus transform Ff(ω)=∫f(s)e^(−iωs)ds,

    F²g(ω)=2πg(−ω),     F(H′)(ω)=iω FH(ω).

Since H=Fg_0 and g_0 is even, FH′=2πiωg_0(ω). Real translation contributes exp(iωS_a), with the plus sign printed in the chapter.

For K_0=F(wg_0), the double transform is 2πw(−ω)g_0(ω), not 2πw(ω)g_0(ω). The reflected input is correct. It preserves the derivative multiplier at frequency 3 and both higher translated channels. Differentiating K_0 in the spectral output supplies iω; it does not require differentiating w in the Fourier input.

## Limits of this review

This review supplies no newly evaluated numerical certificate count, no full-source or Lean validation, and no RH endpoint claim. The final proposed continuation—actual corrected nonlinear radial fluxes under the Mellin map—is described as the next calculation, not replaced by the exterior heat profile. The parent independently owns the symbolic checker and reader build.

## Bounded final binding refresh

Current reviewed proof SHA-256: acf284b71028f4742457b2ea565b6f647e8744bef2f3133bcc370cc68d2a5e7d.

On the parent's subsequent bounded validation assignment, I reread the complete current 29j. Relative to the domain-corrected revision above, its closing next-action text now points to the completed angular-Mellin section (29k, sec:ns-angular-mellin) and the fixed-axis derivative section (29l, sec:ns-axis-arithmetic-jet). The old proposal to calculate those fluxes next has been replaced by those reader cross-references. No displayed identity, source assumption, coefficient, domain, or estimate changed. The earlier verdict remains PASS. The preceding “next calculation” wording in this review is retained as the historical description of the earlier version, not the present reader status.

At the parent's request I reran the existing symbolic checker, sequentially with the axis checker and without modifying either script:

    python -X utf8 -B certificates\rh_counterexample_20260908\verify_ns_stress_arithmetic.py

It exited zero with exact_algebra_checks_pass, check_count=92, all_passed=true, and elapsed_seconds=6.842325899997377. Its current receipt binds exactly the current proof hash above. These are the same 92 existing finite regression checks, not 92 new theorems and not a certification of the entire analytical proof or imported source existence.

- Checker SHA-256: b6a60d847eaf179acce25ebfc2dd16dd2b8e67d5f899ed4d934c09e7d17d27f7.
- Receipt: certificates/rh_counterexample_20260908/ns_stress_arithmetic_checks.json.
- Receipt SHA-256: 463e1bd1e24c931133e3424ea77cae9aa81c84baba379b4a1c6100f27cc2952c.

No TeX edit, PDF build, literature-index change, source-provenance rebuild, or publication was performed in this refresh.
