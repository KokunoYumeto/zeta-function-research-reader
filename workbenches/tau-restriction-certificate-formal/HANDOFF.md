# Handoff to the arithmetic and formalization collaborators

Work here is additive to PR25 at 66fac5e7885a40cd4873e74b754907320f05b067. Do not duplicate or alter the frozen Gamma/publication cut. PR26 records actual execution status.

The source's T=K_iG_j is now represented with its two-metric adjoint equation, composition, inverse, action defect, source restriction and original relation Gram. The difference L R_i-R_j is retained before its image becomes the receiving supported zero. No source arithmetic unit or monic norm is normalized away.

New certificate: H=I-T, s_m=Tr(H^m), P_p=sum_(m=1..p)s_m/m. When s_p<1,

`P_p <= log(V_i/V_j) <= P_p + (P_(2p)-P_p)/(1-s_p)`.

Its proof starts from the proved logarithm series. The tail after 2p is at most x^p times the tail after p, and x_a^p<=s_p. The fixed finite-dimensional stopping test eventually succeeds. The certificate uses only original matrix powers; the explicit spectral witness is used to prove validity, not as a computed input. It avoids separately estimating g_min but does not remove arithmetic inversion error or asymptotic conditioning.

For interval use, obtain upper bounds bar_s_m through 2p with bar_s_p<1. Sum the tail block m=p+1..2p directly; do not subtract independently bounded prefixes. The resulting upper formula is monotone in those bounds. This is compatible with a future certified Gram/error pipeline, but no unprovided Gamma source theorem or moment cutoff is presumed here.

The source's older threshold-two conclusion must be composed with the current per-block factor-four continuation: each of the two original q-dimensional endpoint blocks has logloss>=2q log(D_h k). Thus EACH return operator has some squared restriction factor <=(D_h k)^(-2). Those eigenvectors need not be A-invariant. The exact quotient still preserves their full arithmetic class.

A fixed margin s_p<=theta<1 under this hypothesis can force p of order k^2. Keep that cost explicit when designing a uniform estimate. The remaining research problem is an actual arithmetic upper bound on these original restrictions, not finite existence of the certificate.

The full proof and scope distinction are in RESEARCH_NOTE.md. The original sharp c_p(r) certificate is retained too; the adaptive one is an alternative when a separate gap is unavailable, not a claim to dominate it at every fixed truncation order.
