# Independent arithmetic-tail review

Date: 2026-09-13. Reviewer task: `/root/independent_review`.

## Assigned scope

Parent assignment, verbatim: "Independent review this turn: counterfactual_frontier is proving actual g/h boundary tilt and fixed-one-factor Gamma comparison, yielding sharper exact monic norms. Read inherited actual source and find any prior result duplicating proposed sharp norm asymptotic; inspect math announced below. Coordinate directly with counterfactual_frontier to review once file ready. Proposed m_k sandwiched a_k σ/(1+u²)^M ≤ m_k ≤ A_k σ with fixed σ=|Γ(1/4+iu/2)|²/(2π), log constants O_h(k+logk). Then monic norms ω_k,n between a_k γ_n/[C(n+M)^{2M}] and A_k γ_n. Check Cauchy duality derivation, uniformly n∼q, original masses. Own continuation2/arithmetic_tail_review. Prove/reject exact inequalities, no generic objections."

Read-only review of author sources; only this assigned review directory is written. Root retains responsibility for global manuscript edits and the full user-input provenance log. No RH conclusion is inferred.

## Read coverage and current conclusions

- Fully read inherited `original_programme/tex/theta_gamma_reference.tex`, lines 1–516. Exact fixed-Gamma norms and recurrence are TG.11–14, lines 156–189. Actual one-factor determinant identities are TG.15–19, lines 195–302. The source explicitly does not infer arithmetic norm asymptotics from xi expansion coefficients; lines 410–416. The deep-zero obstruction in TG.26–28 concerns the one-factor arithmetic multiplier; it does not apply to a strictly positive convolution merely by renaming it.
- Fully read inherited `original_programme/work/toda_theta_input_tail_20260912.tex`. It gives the original mass and tilted Mellin/Fourier maps, a complete analytic seed tail certificate, and only the first tensor recurrence coefficient. It expressly does not certify a growing packet determinant or all-k bound from its four scalar intervals.
- Fully read `original_programme/work/theta_norm_literature_20260912.md` and current `tex/modules/HC.tex`, all 390 lines.
- Read original arithmetic endpoint proof `sources/web_arithmetic_endpoint_delivery/Tau_Arithmetic_Endpoint_Bounds/NOTE.tex`, lines 250–451 in full: local zeta mass propagation, original g/h factor, positive compact double convolution, three-factor lower bound, and all-k envelope. The new lower comparison uses this proved original envelope with its original c_h, vartheta_h, B=42+8m and k≥3.
- Fully read `continuation2/arithmetic_tail/tilt_audit/gamma_bound_review.md`. It proves the exact Gamma upper constant from Binet's integral, including its remainder bound, and retains t≠0 for the singular power bound.
- Independently rederived the full finite Gram Cauchy inequality and checked both scalar comparison constants as announced by the author. They pass.
- Delegated the bounded duplicate-result audit to `cr_spectral_check`; report `prior_result_audit.md`. Its read coverage is explicitly bounded there. Initial finding: old CJ norms have O_h(n) error, not the new O_h(k+log(n+1)) error.
- Requested and fully read the complete new TeX draft from `/root/counterfactual_frontier`; its TW1–21 proof and added TW15a–b raw moments pass. Fully read BT1–23 and the complete CA1–29; those proofs pass. Exact source hashes and two corrected CA typing details are in `FINAL_REVIEW.md`.
- Fully read the subsequent internal Binet derivation BI1–26 (308 lines). Its Euler integral limit, locally uniform logarithmic product/nonvanishing proof, Beta Jacobians, duplication, second derivative identity, and two affine constants all pass. Sent one concrete final-display typo to its author: BI26 needed a plus sign before the remainder integral. The author corrected it; independently reread line 299 and appended final SHA-256 and approval to `FINAL_REVIEW.md`. The bounded review is complete with no remaining corrections.

## Exact checks already sent to author and root

The polynomial Cauchy estimate is valid for every complex polynomial of degree at most N. The weighted-shift bound for the fixed Gamma recurrence is valid and yields D_N=[1+4(N+M)^2]^M. The resulting comparison is a full Gram comparison on the original coordinate space, not only an estimate of a selected trial polynomial. Thus minimizing over the identical affine monic space proves the proposed monic norm bounds. The original source mass remains mu_h^k and the reference mass is sqrt(2pi).

For the two literal q-windows n=q−1,q, the Gamma product gives root/q→4/e. The assertion does not extend to arbitrary comparable n with the same constant: if n/q→theta>0, the constant is exp((theta+1)log(theta+1)−theta log theta−1). Nor does this error estimate alone prove the consecutive recurrence asymptotic omega_(n+1)/omega_n∼n².

## Primary source verification

The reviewer opened NIST DLMF 5.9 (Binet integral 5.9.10_2) and 18.22 (Meixner–Pollaczek recurrence 18.22.8) on 2026-09-13, in addition to reading the complete local derivation that fixes the original variable and all factors. External links: <https://dlmf.nist.gov/5.9.E10_2>, <https://dlmf.nist.gov/18.22.E8>.

## Last bounded addition

Parent assigned review of CA17a–b and updated CA21 using accompanying AGT. Fully read `output/Tau_All_Degree_Angle_Transport_2026-09-13/proofs/AGT.tex`, 365 lines, AGT1–19. The crossed pairs force one zero angle in the common (2q−1)-dimensional ambient orthogonal complement. The 2q−1-slot bound, transforms with denominator/coefficient 4q−2, positive moment witness on fixed-sigma interpolation, and CA21 substitutions all pass. Sent one wording clarification about the reciprocal derivative's factor o(t); no formula correction was required. Parent applied the wording clarification at CA236–237; independently reread and recorded final CA hash EE8FB79B97F2BFD367D9758661BA067DE98C4AE2A8AA97FB147B5DC34557DA35. The final bounded review is complete with no remaining corrections. Exact read hashes and full calculation are in the final review addendum.
