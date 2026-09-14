# Actual arithmetic tail continuation

Active assigned task: derive rigorous actual g/h convolution-tail and high-degree norm/window information, at q=[1+k(m−1)](k+1)^2, retaining ζ and the signed original four-window correction. No change to the delivered 109-page edition. No RH assumption, bounded-below ζ premise, or reference-polynomial calibration is allowed.

The inherited root user task remains to carry the entire tau-based split-zero counterfactual toward contradiction or disproof; neither endpoint is established. The parent's full verbatim user record remains in the root task log. This lane's new mathematical files live only in this directory.

Read fully for this continuation: proof_inputs/AT.tex (409 lines, two chunks), proof_inputs/AW.tex (410 lines, two chunks), original tex/theta_gamma_reference.tex (all lines, two chunks), and original tex/arithmetic_moments.tex (all lines, two chunks). Current HC was authored and fully reviewed in the preceding continuation; no edit to the edition is made here. Keyword audit over original source TeX and included proof inputs found no boundary-tilt/fixed-Gamma sandwich formula of the new form.

AT/AW retain original m1=w_h^*k, Gamma convolution m0 with parameter k/4, actual masses μ_h^k and (2π)^(k/2), signed projection trace and relative full moment spectrum. They do not supply uniform relative eigenvalue bounds. TG supplies the exact original multiplier including minus sign and π phase, Gamma reference σ_(1/4), monic norms γ_n=√2 n!Γ(n+1/2), and the recurrence. Its zero-based obstruction concerns the one-factor arithmetic weight, not convolution k≥3; no contradiction with that obstruction is claimed. AM supplies exact finite original g moments, and does not itself estimate growing g/h convolution degrees.

Delegated bounded task to balanced_audit (and its Gamma subreviewer): full actual boundary tilt M_h(±π/2), elementary ζ bound, explicit Gamma boundary constants, uniform polynomial convolution envelope. Its own files are tilt_audit/. Independent root reviewer is /root/independent_review, with files in continuation2/arithmetic_tail_review.

Current derivation to preserve:

1. For α=π/2, p=8m−9/2>1, actual complete quartet gives a finite C_h with e^(α|u|)w_h(u)≤C_h(1+|u|)^−p. Elementary centered-floor partial sum at N=floor|t| gives |ζ(1/2+it)|≤(2+√(5/2))√|t| for |t|≥1. The full h denominator is retained exactly. Gamma two-sided boundary estimates are being written by the child.
2. Actual M_α=∫e^(αu)w_h(u)du is finite; evenness gives both signs equal. For all k≥1 the tilted convolution bound is m_h,k(u)≤k C_h M_α^(k−1)(1+|u|/k)^−p e^(−α|u|). Proof: sum constraint forces one coordinate to have absolute value≥|u|/k, then integrate the other k−1 actual tilted densities; sum the k choices.
3. Together with the original lower convolution envelope, for k≥3 obtain a_k σ/(1+u²)^M≤m_h,k≤A_kσ, where σ=|Γ(1/4+iu/2)|²/(2π), M=B/2=21+4m, B=42+8m, A_k=(C_h/c_Γ)k^(p+1)M_α^(k−1), a_k=c_h θ_h^(k−3)e^(−α(k−3))(k−2)^−B/(C_Γ 2^(B/2)). c_Γ,C_Γ are literal positive two-sided Gamma envelope constants. No original mass is set to one.
4. For P in degree≤N, Gamma recurrence gives ||u^jP||_σ≤[2(N+M)]^j||P||_σ for0≤j≤M. Hence ∫|P|²(1+u²)^Mσ≤D_N||P||_σ², D_N=[1+4(N+M)²]^M. Cauchy yields a_k H_N^σ/D_N≤H_N^ar≤A_kH_N^σ. All source maps are literal polynomial identity, with original S=c+iu coordinate and its exact phases retained.
5. Monic minima therefore satisfy a_kγ_n/D_n≤ω_h,k,n≤A_kγ_n, so logω=logγ_n+O_h(k+log(n+1)). At original q-windows, q≫k gives (ω_(n+q)/ω_n)^(1/(2q))/q→4/e, n=q−1 orq. This improves original literal window lower constant to δe/8; threshold four is inherited and unchanged. Exact finite errors must be displayed.
6. The same-source Γ-convolution reference in AT/AW has γ_(k,n)=(2π)^(k/2)n!Γ(n+k/2)/Γ(k/2). The actual fixed-Γ comparison suggests log(ω_ar/γ_(k,n))=−(k/2)log(n/k)+O_h(k+logn) at n~q, giving actual determinant increment/eigenvalue-spread information; it does not assign a sign to the signed quotient correction.

No theorem has yet been integrated, no final mathematics claim is made until the full proofs and independent review are complete. No Lean or publication occurred.

## Written and reviewed increment

`arithmetic_tail_windows.tex` now contains TW1–TW21 in full: actual tilted convolution; raw moments; fixed-Gamma pointwise comparison; full P_N multiplication/Cauchy Gram sandwich with D_N=[1+4(N+M)^2]^M; exact coordinate maps; uniform monic norm errors; both original q-window limits4/e; and the original four-volume lower bound with sharpened constantδe/8, errorO_h(k+logq), and all five retained costs.

The root and root independent reviewer fully read TW1–21 and accepted it. The reviewer also fully read the 293-line `tilt_audit/ACTUAL_BOUNDARY_TILT.md` BT1–BT23 and confirmed every constant, denominator, cutoff, sign, derivative order, and convolution Jacobian. `C_h` in TW2 is now explicitly identified with C_h^tilt in BT12.

The child is adding an internal Binet-identity proof from the Euler beta-limit/product, the exact second derivative, recurrence, and duplication. This removes reliance on the external DLMF identity as an unproved starting formula. Once ready it will be exported with BT to includable TeX. Root is assembling a new cumulative repository and owns the new quotient/spectral transport from the full Gram comparison; this lane does not edit the frozen109-page edition.

A local five-page syntax compile was performed before root instructed that root would handle subsequent PDF generation; no additional PDF generation will be run after that instruction. The source has no known mathematical errors. Optional old-k-Gamma monic increment/condition-number consequences were sent to root for its spectral lane, not duplicated in TW.

## Final stable source delivery

The internal Gamma/Beta/Euler/Binet foundation is complete as `tilt_audit/EXACT_BINET_IDENTITY.md`, BI1–BI26. It proves Gamma nonvanishing and its logarithmic branch without assuming them, derives the exact second derivative from the product, and determines both affine constants from recurrence and duplication. The root independent reviewer accepted the entire proof after a missing plus sign in BI26's final display was corrected and reread. This lane fully read that completed source.

`export_boundary_source.py --binet tilt_audit/EXACT_BINET_IDENTITY.md` produced `boundary_tilt_full_public.md` and `boundary_tilt_full.tex`. The complete TeX export was read. All BT/BI mathematics is retained; only process/provenance material is removed. TW was already fully accepted, including raw moments TW15a–b. Final hashes and the exact review scope are in `FINAL_REVIEW_RECEIPT.md`; the independent review is copied in full beside it. The root was notified of the stable TeX paths. No new PDF, publication, Lean process or frozen-edition edit occurred. The assigned continuation is complete, with the parent integrating these sources and handling cumulative PDF verification.
