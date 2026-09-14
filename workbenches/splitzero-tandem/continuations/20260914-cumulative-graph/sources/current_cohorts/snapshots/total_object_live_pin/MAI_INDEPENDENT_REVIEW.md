# Independent review of the mixed amplification identity

Date: 2026-09-13. Reviewed the complete `mixed_amplification_identity.tex`, MAI1–8 including MAI6a, and reread every correction. Current reviewed SHA-256: `27CBD90F0A711689BD3D1E888345CD7C196F241C6966694EC1EFD9349DC38796`. The previous fully read edition had SHA-256 `BFAA30CE1F81305B16E4FE040CA61300E5EAE7EC58EC7F68A8A4860B6C2FE25A`; its only subsequent change is the verified wording that the formula holds on every nonzero graded piece, including j=0.

Parent assignment retained verbatim:

> Review new root-owned total_object/mixed_amplification_identity.tex MAI1–8 complete proof connecting SAMEclass throughmixedcoefficient invariantretract, tensor, MWgraded/Tate scalar correction, PAMoriginalsourceboundary. Read referencedMW/PAMsymbols enough tocheck exact basisindex, scalar/types,same-objectnonzero and Fourier sign. It does notassertpurity/no conditionaltheorems. Sendconcreteerroror finalhashapproval. Rootwillintegrateaftermainmixedproofsarrive.

Verdict: pass. No mathematical correction remains. No owned source was edited by this reviewer. This receipt concerns the mathematical module, not its eventual cumulative integration or rendered PDF.

The original terminal jet v_rho is nonzero with full local order, and its coefficient insertion has the exact trace retraction. The coefficient signed Frobenius fixes its image. Tensoring over C retains both retraction and nonvanishing. MAI4 follows with the original arithmetic exponent and real logarithm. The current source explicitly retains n>=1 and the odd prime-power coefficient parameter q0 coprime to n, separately from the real Tate-scaling parameter q>1.

MW assigns the local index m-1-2r. Tensor indices add, so the original terminal tensor lies in index -k(m-1). On every nonzero graded piece, including index zero, the added F tensor acts by q^(k rho+j/2), while Gamma inverse contributes q^(-j/2). The complete nilpotent exponential is retained in the ordered identity before passage to the grading. It induces the identity on associated graded. Thus MAI5 and MAI6 are exact, including their scalar correction; they do not supply an arithmetic purity bound.

MAI6a is the essential same-class identification. The sum k rho in the chosen quartet occurs only on the all-rho tensor block. With K=k(m-1), the top power of the sum of the original nilpotents has coefficient K!/((m-1)!)^k on the product of terminal monomials. Multiplication by the full arithmetic unit has value ((g/h0)(rho))^k on that terminal product; all higher local unit terms kill it. Therefore

    eta_k(v_k) = c_(h0,k) v_rho^(tensor k),
    I_k(v_k)   = c_(h0,k) u_rho^(tensor k),
    c_(h0,k)   = K!/((m-1)!)^k * ((g/h0)(rho))^k != 0.

The common full packet H=lcm(h,h0) and the literal AG divisor identities identify the original u_rho in both presentations. No scalar is suppressed and no larger packet is silently substituted for the original class.

The corrected initial choice fixes 0<delta<1/2 and gamma>0 once, with the original reflection/conjugation maps supplying the other quadrants. For the phase observation, k>=2, N>=q_k-1, L>0 and 0<=theta<2pi are explicit, and R_k is exactly R_(N,theta). On its twisted domain, the modes are L^(-1/2) exp(-i u_n r), u_n=(2pi n+theta)/L. Thus D_(L,theta)-k rho has multiplier -k delta+i(u_n-k gamma). Parseval proves MAI8; membership in the H1 domain gives convergence of its weighted numerator, and the nonzero arithmetic observation gives its positive denominator. The boundary remains the actual theta relation described by PAM and PSC.

The child `cr_spectral_check` independently checked MAI5–8 against MW15, MW18–19 and PAM8–10. Its three domain/wording recommendations were applied and directly verified by the parent reviewer. The final source now also says that the identity holds on every chosen nonzero graded piece, including j=0. That final wording was reread and introduces no mathematical change. Nothing remains outstanding in this bounded review.

This review uses the previous complete MW, PAM/PSC, PS and AG map readings recorded in this lane. It makes no RH conclusion and does not infer a pure lisse-sheaf realization from the added complex matrices.
