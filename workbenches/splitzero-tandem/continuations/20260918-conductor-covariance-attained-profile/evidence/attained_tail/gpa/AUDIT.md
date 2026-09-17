# Attained-tail GPA root/Gamma audit

**Primary verdict: proved as written on the retained original root-comparison domain.** Equation (8) follows from all-direction inequalities before minimization, and its logarithmic constants are uniform on the entire numerical range (7). The complete additive proof is [GPA_ATTAINED_TAIL_PROOF.tex](GPA_ATTAINED_TAIL_PROOF.tex), equations ATG1–28. It preserves the original source mass, root lists, centres, phases, coefficient spaces, and both source orders.

The displayed numerical inequalities (7) supplement the original domain: they do not replace `j = 4l + 1`, `0 < delta < 1/2`, `gamma > 2`, and the actual conductor condition `0 <= v <= Delta`. In particular, the finite Gamma recurrence uses the integer `ell_j = (j-1)/4`; the lower monic degree uses `m = Delta-v >= 0`. These are already original hypotheses, not new restrictions on the original task.

## Claim card

- Root counts: `q = (j+1)^2`, `q' = (j-7)^2`; original centres `c+ = j/2` and `c- = j/2-4`.
- Sources: exactly `s = 1,j`, with `M_s = (2 pi)^(s/2)` and `beta_s = M_s/(sqrt(2) Gamma(s/2))`.
- Degrees: `b+ = r`, `b- = m+r`, throughout `0 <= r <= q+32j`; the requested attained tail is a subrange.
- Entire coefficient spaces: complex polynomials of degree at most the indicated degree, with no zero-location or parity condition.
- Exact conclusion: each original norm lies between `beta_s exp(b^-_{n,b,s})` and `beta_s exp(b^+_{n,b,s})` times the power-exponential norm at `Q=n+ell_s`; the exact monic coordinate map transfers both inequalities to the minima.
- Error: `b^± = O_{delta,gamma}(log q)` uniformly over both sources, both root counts, and both moving degrees. ATG25 gives explicit finite bounds.
- Evidence: a complete analytic proof from the exact source measure, original root lists, and elementary polynomial norm identities. No numerical extrapolation or unproved comparison is used.

## Exact constants

All symbols below are defined in ATG1–3. With `h=1/q`, `theta=pi/2`, `Q=n+ell_s`, and the unchanged common GPA error `E_j`,

\[
b^-_{n,b,s}=-E_j+\log L_h-K_{b,Q}\log(1+h/\vartheta),
\qquad
b^+_{n,b,s}=E_j+\rho_{\ell_s}+\log U_h
 +K_{b,Q}\log\frac1{1-h/\vartheta}.
\]

\[
E_j=\frac{qj^2(\delta^2+\gamma^2)}{\epsilon^2q^2-j^2(\delta^2+\gamma^2)}
 +\log(1+K_q),\qquad \epsilon=2^{-32},
\]

\[
K_q=\frac{\sqrt{2\pi}\,\Gamma(3/4)^2}{\pi}
 \frac{(2q+1)^2}{q}e^{-2q},\quad
K_{b,Q}=2Q+1+2b+2\sqrt{b(b+2Q)},
\]

\[
L_h=\frac\pi{\Gamma(3/4)^2}(\sin h)^{3/2},\qquad
U_h=\frac{\Gamma(1/4)^2}{2\pi}(\sin h)^{-1/2},
\]

\[
\rho_0=0,\qquad
\rho_\ell=\frac{\ell(16\ell^2-12\ell-1)}{12\epsilon^2q^2}
 +\log(1+K_q)\quad(\ell>0).
\]

Thus the constants needed in the pasted proof are exactly `b^+_{q,r,s}` and `b^-_{q',m+r,s}`. The common scale is always the original upper `q`, including in the lower-root application. No lower-root substitution changes the cutoff or `h`.

## Dependency graph

1. OSP3 root lists and the original centres → ATG6–7 exact polynomial/phase maps.
2. Euler integrals and the finite Gamma recurrence → ATG8–13 full mass, exact source multiplier, interval density lower bound, and mass-to-density ratio.
3. Legendre Rodrigues identity → ATG14 all-direction inner-interval polynomial estimate.
4. Root pairing and ATG14 → ATG15–18 full original-root norm comparison, including the entire inner interval.
5. Exact positive source factors and the same inner-interval estimate → ATG19 full-form Gamma-order comparison.
6. Rotated Euler integrals and the exact reflection product → ATG20 global Gamma density sandwich, including zero.
7. Laguerre Rodrigues identity → ATG21–23 dilation norm and exact rate-change map.
8. Steps 4–7 → ATG4 with all finite constants in ATG3.
9. Original numerical domain → ATG24 degree and exponent admissibility; ATG25 uniform logarithmic bounds.
10. Exact affine-fibre bijections → ATG27 monic minima, and only then ATG28 same-source mass cancellation.

There is no dependency from the GPA proof back to the attained-tail equilibrium asymptotic or native-row profile.

## Obligation matrix

| Obligation | Result | Decisive evidence |
|---|---|---|
| Upper as well as lower root count | Passed | OSP20–26 already quantifies over both; ATG15–18 proves both directly. |
| Moving degrees beyond four GPA endpoints | Passed | All-direction inner-region proof needs only `b<=2q`; ATG24 proves this for `r,m+r`. |
| Exact source order `s=j` | Passed | `j=4l+1`; ATG10 proves every finite recurrence factor and full constant. |
| Complete original mass | Passed | ATG8–13 proves and retains `M_s,beta_s`; only matched ratio ATG28 cancels `beta_s`. |
| Entire real line | Passed | ATG16–19 retains both inner integrals; ATG20 includes zero. |
| Every coefficient direction | Passed | ATG14 is an orthonormal-basis estimate for arbitrary complex polynomials; all subsequent estimates apply before minimizing. |
| Exact monic fibre transport | Passed | ATG7 gives a bijection and explicit inverse, retaining phase and centre. |
| Signed rate change | Passed | ATG22 keeps the scalar `u^(-2Q-1)` before taking two-sided bounds. |
| Uniform logarithmic errors | Passed | ATG25 gives explicit finite bounds, including both source orders and all `b,Q<=2q`. |
| Smallest degrees | Passed | Norm/dilation estimates include `b=0`; no division by `b` or parity hypothesis appears here. |
| Equilibrium estimate, row envelope, weighted profile | Out of scope | Audited by other agents; this audit neither assumes nor proves them. |

## Source locators and provenance

Authoritative frozen provider:

`PROJECT_ROOT/work/mixed_tail_continuation_20260917/full_receiver_build/staging/14_CURRENT_KERNEL_AND_MULTIPLICITY_PROOFS.tex`

- OSP1–26: source lines 10488–10848, complete root lists, mass, coefficient-space comparison.
- OFV1–7: source lines 12203–12329, original-order recurrence and full-form argument.
- GPA1–23: source lines 25306–25700, exact comparison and its four-endpoint application.
- SHA256 observed during audit: `50E5071B8BC1E1325F401764E7FDD3CDA50994601B6F2E1BF00627864D665571`.

Authoritative supplied claim:

`PRIVATE_INPUT_ROOT/LOCAL_RECORD_69689187cc3d4126/pasted-text.txt`, section 3, equations (7)–(8).

- SHA256: `D55F313672418DE60C8422738592641933808C169EE1A6463866DE6659DF3B4C`.
- The exact supplied text is copied locally as `PASTED_PROOF_VERBATIM.txt`.

Read-only checks used `Get-Content`, `rg -n`, and `Get-FileHash`. A static balance check of the additive TeX found brace balance zero, no negative brace depth, and all 28 ATG tags. No TeX, Lean, Lake, or Elan process was started. No frozen file was edited.

The independent child audit `gamma_check` reconstructed the exact Gamma mass and recurrence, both global density constants, and the original monic recurrence/norms. It found no missing factor, phase, mass, or source-order restriction. The full root/inner-region proof was separately reconstructed in this audit.

That agent also independently inspected ATG13–28 in the completed additive proof and found no concrete algebra, domain, constant, or minimization error. Human-source citations are placed at the actual uses: Askey and Roy, DLMF (5.2.1), (5.5.1), and (5.5.3), using `human:dlmf5`; and Koornwinder, Wong, Koekoek, Swarttouw, and Reinhardt, DLMF Table 18.3.1, (18.5.5), Table 18.5.1, and (18.5.12), using `human:dlmf18`. These reuse the existing inspected source dictionary and read receipts in HPS and the frozen provider; no broader attribution or independently inspected Ismail-book claim is made. The complete calculations remain beside the citations.

## Remaining gap

There is no remaining root/Gamma comparison gap in equation (8) under its retained original hypotheses. For a fully standalone presentation, the displayed numerical domain must be accompanied by those original hypotheses and the constants ATG3; this additive proof supplies them. The equilibrium and attained-row consequences are separate parts of the parent audit.
