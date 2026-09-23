# New mathematical results — 23 September 2026

This continuation connects the literal positive prime pulses to the original theta quotient and every derivative in a finite zero packet. It also evaluates the source cost and the complementary Weil contribution. The complete proofs are in the cumulative LaTeX, including their earlier support, primitive-lift and pulse-bound inputs.

## SZ-20260923-115 — What the original word completion loses, and the exact receiver that retains it

Let $A$ be the full finite root algebra, retaining multiplicities, and let $E(P)=P(H_c)$ be the original two-prime word observation. Its relation ideal is $(\nu)$. In the original word-source measure \(\mu\),

\[
\overline{\nu\mathbb C[X]}^{L^2(\mu)}=L^2(\mu),\qquad G_n\downarrow0.
\]

Here $G_n$ is the actual minimum source Gram for prescribed full jets. The proof gives explicit polynomials retaining every prescribed jet while their source norms tend to zero. Retaining both the source and the original primitive observation instead gives

\[
\overline{\{(P,EP)\}}=L^2(\mu)\oplus A_G,
\qquad \text{finite quotient Gram}=G+G_n,
\]

where $G=S^*S$ is the original primitive Gram. The finite correction between $G_n$ and $G+G_n$ is proved as a complete determinant identity; all four cutoff signs remain. The same calculation gives exact lower bounds for the theta-action defect on a nonreal eigenclass and on a critical higher jet. An explicit positive Weil direction gives a nonclosable form in the source-only norm; its graph limit is exactly the retained vector $(0,u)$.

Full proofs: **GC1–24**, [working source](PRIME_WORD_GRAPH_COMPLETION.tex). This develops the received constructive two-prime source, preserving both complete originals in `two_prime_received/`. Human context: Meyer and the Connes–Consani theta quotient, cited in the cumulative bibliography.

## SZ-20260923-116 — Actual prime pulses recover every full finite packet

For the original pulse width and bump, its complete observation is

\[
E_Ic=j_h\!\left[s(s-1)W_{\varepsilon_I}(s-\tfrac12)
          \sum_{r\in\{1\}\cup I}c_r r^{s-1/2}\right].
\]

For every finite packet, a finite set of distinct primes makes this map onto **all** its Taylor coefficients. The proof supplies the bump-unit threshold and proves prime-column spanning; it retains the exact missing-jet spaces when the bump is not a unit. The actual support diagram has varying coordinate fibres and proved transport squares.

Writing $W$ for the complete positive FP matrix, the minimum-Weil metric is

\[
G_W=(E_IW^{-1}E_I^*)^{-1}.
\]

For its actual lift $F_{I,L_Wu}$, subtract the primitive section $S u$. This residual has every selected jet zero and retains all unselected-zero data. Its exact Weil matrix is

\[
\mathcal W(F_{I,L_Wu}-Su,F_{I,L_Wv}-Sv)
=u^*(G_W-W_Z)v.
\]

For a hypothetical reflected off-line pair of multiplicity $m$, take the two value coordinates $(1,-1)$, with other coordinates zero. The selected pairing is $-2m$; the actual complementary contribution is strictly greater than

\[
2m+\frac{6600077509}{144027072000}
  N_Iu^*(E_IE_I^*)^{-1}u.
\]

Full proofs: **PO1–54**, [source](reflected_trace/PULSE_PACKET_OBSERVATION.tex). Earlier results receiving this addition: FP1–44, PL1–52, FJ and the original support-trajectory construction. Connes, Connes–Consani, Jensen and Euler are cited; historical metadata-only reading is distinguished from original TeX reading. Both classical auxiliary arguments are proved in full.

## SZ-20260923-117 — The whole source cost through two orders

Keep a fixed set $J$ of spanning prime columns. Enlarge the ambient prime set so its **prescribed** pulse width tends to zero, retaining coefficients only on $J$. Write $M=M_{s-1/2}$, $K_J=(M_aP_JP_J^*M_a^*)^{-1}$, and keep the literal bump constants

\[
A_w=\int(w_0'')^2,\quad B_w=\int(w_0')^2,
\quad\mu_0=\int w_0,\quad
\kappa_w=\frac{\int v^2w_0(v)\,dv}{2\mu_0}.
\]

The minimum source metric has the complete matrix expansion

\[
H_\varepsilon=
\frac{A_wK_J}{\mu_0^2\varepsilon^5}
+\frac{\frac12B_wK_J-A_w\kappa_w[(M^2)^*K_J+K_JM^2]}
       {\mu_0^2\varepsilon^3}
+O_{Z,J}(\varepsilon^{-1}).
\]

The full determinant is evaluated through its \(\varepsilon^2\) term. Thus the source cost of recovering a fixed nonzero packet grows as \(\varepsilon^{-5}\), with every mixed jet entry in the next coefficient retained. The attained Weil cost is bounded below by the proved FP constant times this metric. This evaluates the corresponding growth of the actual complementary contribution above.

Full proofs: **PCO1–13**, [source](PULSE_PACKET_COST.tex). Effective matrix remainder bounds are included. The constants are original bump integrals, without replacing their amplitudes.

## Scope and verification

The source-only word metric, the two-observation graph metric, the pulse Haar metric and the attained Weil metric each retain their own exact maps. The new calculations do not replace any of them by another one. Global Weil positivity remains unfinished.

Root ran 87 exact auxiliary graph identities and five matrix-expansion checks, including a test detecting an omitted derivative. The independent pulse derivation supplied exact Taylor, nonunit-rank, minimum-section and residual checks, and independently checked PCO5,9,10,11. These checks supplement the complete proofs; they do not certify unknown zero locations or global asymptotics. The attempted separate GC review returned a usage-limit error and supplied no independent validation.

The prior sealed 189-page edition remains unchanged. This continuation is local while the sole publication task holds uploads.
