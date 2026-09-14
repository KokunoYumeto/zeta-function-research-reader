# Independent proof review of the period critical-kernel bridge

Accepted on 2026-09-13 after a complete mathematical reading of PC1–41 and a second complete reading incorporating the coordinate corrections. The final descended-jet and section-intertwining paragraph was then read against the final source bytes. No unresolved mathematical issue remains in the reviewed statements and formulas.

Source: `work/period_critical_kernel_bridge_20260913.tex`

Accepted source SHA256: `93a9d828e86608699b83cf331f77f77ae5062505293f6f7e30e69db77af4c5f9`.

Reviewer role: independent single-packet arithmetic-unit and tensor-map review. The proof-bearing dependencies read were the full relevant arguments in `tex/arithmetic_input.tex` (A5–A13), `tex/coherent_tensor_integration.tex` (CT.1–CT.5), `tex/toda_cv_exact_bridge.tex` (the original source construction and TVB.1–TVB.3), and the retained PR27 `HOCHSCHILD_COMPARISON.md` (H16–H25, including both kernel proofs). The three TeX dependency paths are relative to `output/split_zero_rh_tandem_2026-09-12`; the retained PR27 source is under the owner's `integration_20260913_next/pr27_review/source/workbenches/tau-specialization-curvature-formal` directory. This review involved no tests, Lean, remote operations, or edits to the mathematical source.

## Corrections verified in the accepted source

The first complete reading identified a literal tensor-domain mismatch: the one-factor comparison has domain E = C[S]/h(S), whereas the original arithmetic tensor algebra is B_k = E_h tensor k, with E_h = C[s]/h(s). PC29 now supplies the variable isomorphism iota_k = iota_1 tensor k and defines bar-alpha_k = iota_k inverse composed with alpha_k. Consequently both PC31's critical projection and PC33's completed comparison compose with their exact domains. The original weighted inclusion is retained through eta_k = eta_h tensor k composed with bar-alpha_k.

PC15 and PC31 now specify the identity e_c = pi_c(e_0) of the actual CRT ideal E_c, its transported units upsilon_c and epsilon_c, and the evaluation alpha_c,k[P] = P(A_c^[k]) e_c tensor k. This preserves the original ideal as the tensor target, including its identity and its nilpotent factors.

The final PC6 paragraph distinguishes J_h: B -> E_h from its descended map bar-J_h: Q -> E_h. It proves bar-J_h q = J_h, bar-J_h sigma_h = I, and the section intertwining D_Q sigma_h = sigma_h M_s through the already proved source identity and the surjectivity of eta_h. The later jet recovery uses this descended map. The reported missing TeX backslashes and the period-integral differential were corrected as well.

## Mathematical checks

1. **Single packet and source section, PC1–PC8.** Pullback of (h(s_1)) along S -> s_1 gives chi_h,1 = h(S) with every original multiplicity. At each selected root, complete division of the zero order makes the constant coefficient of g/h nonzero. The recursive inverse in PC3 verifies every retained Taylor coefficient. Thus eta_h = M_upsilon iota_1 is an invertible module map, with the displayed multiplicative rule. Monic division P = P_0 + hT gives the literal primitive Theta(T(D) phi_*), proving q T_h = sigma_h eta_h pi_h. The raw observer is j_E = eta_h inverse J_h, so j_E r_N = I while J_h r_N = eta_h. The full-jet Gram is exactly eta_h inverse-adjoint G_N eta_h inverse.

2. **Critical kernel and recovery, PC9–PC15.** The reciprocal critical-line multiplier at an off-critical root is a continuous Schwartz multiplier and preserves the relation closure. It annihilates the image of the entire generalized block by the stated intertwining. On critical blocks the derivative observer retains its factors i^(-j)/j!, and multiplication by the explicitly transported inverse unit recovers all polynomial jets. This proves R_c C_h = pi_c and ker C_h = E_o.

3. **Completed tensor map, PC28–PC34.** The corrected bar-alpha maps are well typed. The composition R_c tensor k composed with i_c tensor k is the identity on the finite-dimensional critical tensor space, and extends through the specified projective completion. It therefore proves injectivity and a continuous retraction for the actual finite image; arbitrary tensor exactness is unnecessary. Combining this retraction with the polynomial cyclic injection gives precisely ker C_k = (chi_c,k)/(chi_h,k), of dimension q_k - r_k.

4. **Collision jets and sector criterion, PC30–PC36 and the closing cases.** In every tuple algebra, the multinomial term of degree sum(m_rho_i - 1) has the nonzero coefficient explicitly displayed in PC30. Its maximum over equal sums gives the complete minimal polynomial. PC35 is a well-defined injection and surjection onto the local kernel ideal: its multiplier is x^r times the retained unit a_lambda. This keeps all m_lambda - r_lambda jets with their S = lambda + x action, including r_lambda = 0 and r_lambda = m_lambda. Mixed packets have a critical tuple and a repeated off-critical tuple whose sum has real part different from k/2, proving 0 < r_k < q_k. All-critical and empty-critical cases have their stated zero-curvature endpoints.

5. **Period action and curvature, PC16–PC27 and PC37–PC41.** The period derivative is -Pi A_t/u in the fixed coefficient frame. Invertibility transports the exact kernel to Pi F. Cancellation using C A = M C gives the displayed rank-one action defect. The ideal basis proves both the nonzero top-coefficient functional and e_0 outside the proper kernel. The projector differentiation therefore yields N Y' = -(t/u) z L and normal acceleration -z(0)L/u. Direct differentiation of the Gram determinant gives the complete curvature coefficient |t|^2 ||z||^2 L H inverse L* / |u|^2, with the stated Chern orientation and quadratic vanishing. The moving theta metric has the explicitly cancelling derivative terms. The two Schur-complement identities give PC41, including the empty predecessor when the kernel dimension is one and the constant-frame congruence for an arbitrary specified inclusion.

Acceptance applies to the exact source hash above and to the written mathematical proof. This record makes no claim of a test replay or PDF rendering review.
