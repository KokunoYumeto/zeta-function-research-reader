# Copy-newresults, round 1: report and verification record

The second Claude instance ("copy-newresults", Opus 5.5 configuration) was launched on 25 September 2026 at the owner's request. Its brief was to use the salvaged material to try to obtain new results, as rivalrous cooperation with the ChatGPT/Codex lanes. Its report is reproduced verbatim below the verification record. Its scripts and zero data are in the session scratchpad: zerodata.py, zeros_*.npz, common.py, final_a1.py, check_a2.py, onepoints2.py and t1_checks.py.

## Verification record (claude-ab, independent of the copy's code and data)

- **Theorem A, window [100, 1000], Δ = 1.** Recomputed with mpmath zeros (658 zeros, independent of the copy's Arb data) and an independently written right-hand side:
  - left side 59.581503294161 + 77852.853541547i;
  - right side identical;
  - relative difference 1.8·10⁻¹⁸.

  Script: indep_check_thmA.py. I also re-derived the analytic structure of the right-hand side:
  - the Gaussian-window transforms, including the term (½ + Δ²ξ)E₀ + iE₁;
  - the left-line term, from ζ(−s)/ζ(1−s) = Σ (φ(n)/n) n^s and a shift of contour.

  Both agree with the copy's formulas.
- **R0 (the N3 table).** The entry at T = 2515 in SHIFTED_SHEETS_N1_N3.md is correct for T = 2515. That height contains 1,999 zeros; the 2,000th zero is at γ = 2515.2865.
  - The erratum concerns the labelling: the table was introduced as "the first 2000 zeros".
  - Including the 2,000th zero, Σ Re c₁ = 58.14 + 112.41 = 170.55 and the vertical ratio is 1.00058.
  - The copy's point stands: consecutive partial sums move by about ±100–450 per zero, which is already the size of T/4π.
- **R5 (the sign sector y² = x³ − x).** Checked by hand:
  - the lift of the mirror x ↦ −1/x is (x, y) ↦ (−1/x, y/x²), which is translation by the 2-torsion point (0, 0);
  - the lift of J is (x, y) ↦ (−x, iy), whose square is the hyperelliptic involution;
  - Frob_p ∘ [J] = [J]^p ∘ Frob_p;
  - the primary generator of (n) for odd n is χ₋₄(n)·n, which equals the signed winding degree of Connes–Consani's odd Frobenius on the twistor line.
- **Not yet independently re-proved:** Theorem C, part 1 (via Lemma U and Kronecker), and part 2. Its numerical Bohr-coefficient table is consistent with the prediction −b(n)/(2π√n log n), which I re-derived from the right-hand side of Theorem A.

---

# copy-newresults: final report to claude-ab, 25 September 2026

**Model:** Claude Opus 5.5 (model ID `claude-opus-5-5`), running as the `copy-newresults` instance. No agents were spawned, no messages or notifications were sent, and nothing was pushed.

## 0. Summary

Most of the yield is on T3. T1 produced a construction built from classical parts. T2 produced a literature record and one small example, but no new theorem.

| # | Result | Status | Independent check |
|---|---|---|---|
| R0 | claude-ab's T = 2515 table entry is off by one zero | fact | recomputed two ways |
| R1 | Exact formula for the velocity field of the Hurwitz zeros, all a > 0 | proved | a = 1: 100,000 certified zeros, relative agreement ≤ 3.3e-16 on 6 windows up to T = 74,000; a = 2: 610 certified zeros of ζ(s) − 1, agreement 1e-8 with direct contour quadrature |
| R2 | Smoothed horizontal and vertical velocity laws with explicit error | proved | a = 1 and a = 2 |
| R3 | The sharp laws fail at order T; the error E(T)/T has an exactly computed almost-periodic spectrum | proved under RH + simple zeros (part iii unconditional) | spectrum matches to about 5e-6 for n = 2–16, 30, 60 |
| R4 | The zero velocities pick out the primes | corollary of R1/R2 | same data |
| R5 | T1 receiver: the weight-one sign sector at the four F_{1²}-points is H¹ of y² = x³ − x | classical ingredients; the identification is new to the programme | point counts, symbolic checks |
| R6 | T2 | literature record, small example, open question | example verified |

**Verdict on the owner-endorsed framing of the horizontal law** (details in §4.5):
- "The a-derivative of the O(log T) term is uncontrolled": true, and now exact. That derivative equals Re E(T), which is of order T, not o(T).
- "The sum is dominated by zeros with small |ζ′|": false for the bulk, true for the tails. About 93% of the mean square of E(T)/T is a zero-free oscillation at frequencies log n. The extreme excursions sit inside close pairs of zeros with small |ζ′|.

## 1. Choice of targets and reason

- **T3 first.** It gives the highest expected yield of statements that can be proved and also checked independently. Certified zero data and an independent evaluation of the prime-side terms allow exact numerical tests.
- **T1 second.** "Construct the receiver" can be made precise and checkable, but its ingredients are necessarily classical.
- **T2 last.** The core question (whether regularity below x^{1/2} forces RH for Beurling systems) appears to be open; I did not attack it.

## 2. Data and tools

- Zeros ρ_n = 1/2 + iγ_n for n = 1,…,100,000 (γ up to 74,920.83), from Arb via `python-flint` 0.9 (`acb.zeta_zeros`, which isolates zeros on the critical line). ζ′(ρ) comes from Arb power series and ζ(ρ+1) from `acb.zeta`. Enclosure radii are ≤ 1e-15.
- The velocities agree with an independent mpmath computation to 2e-16 relative (20 zeros tested).
- The velocity formula c₁ = ρζ(ρ+1)/ζ′(ρ) agrees with a finite-difference track of the zeros of ζ(s, 1±10⁻⁸) to 1e-16.
- Zeros of ζ(s,2) = ζ(s) − 1 with 0 < γ ≤ 1100 were found by winding numbers with adaptive boundary sampling, recursive subdivision and Newton. The count is certified: 610 roots, winding total 610, maximum winding error 5e-16.
- All files are in `data/`. This directory is shared with your session; everything with a timestamp of 03:19 or later is mine:
  - `zerodata.py`, `zeros_{A,B,C}.npz`: zero data
  - `common.py`: coefficients b(n), e(n), the formula's right-hand side, 𝒟_Δ
  - `sanity.py`
  - `sharp_analysis.py`, `final_a1.py` (output in `final_a1.txt`)
  - `onepoints2.py`, `onepoints_1100.npz`, `check_a2.py`
  - `t1_checks.py`

## 3. R0: correction to the N3 table

Recomputed sharp sums at a = 1:

| T | #zeros | Σ Re c₁ | T/4π | Σ Im c₁ / (T²/4π − T) |
|---|---|---|---|---|
| 100 | 29 | 10.786 | 7.958 | 1.00259 |
| 300 | 138 | 30.130 | 23.873 | 1.00256 |
| 1000 | 649 | 93.059 | 79.577 | 1.00079 |
| γ₂₀₀₀ = 2515.286 | 2000 | **170.553** | 200.160 | **1.00058** |

The reported 58.1 is the partial sum over the first **1,999** zeros (S₁₉₉₉ = 58.144 + 500829.034i). Consecutive partial sums near that height are −149.1, 58.1, 170.6, −88.1, 305.2: each zero moves the sum by about ±100–450. That noise is already of the size of T/4π.

## 4. T3 results

**Notation.**
- F(s) := sζ(s+1)/ζ(s). At a simple zero, Res_{s=ρ} F = c₁(ρ) = dρ/da at a = 1 for ζ(s, a).
  - The velocity ODE is due to Frisk–de Gosson, arXiv:math-ph/0102007 (2001); the same formula is in programme satellites/10.
  - F has no pole at s = 0 (F(0) = 1/ζ(0) = −2), so its only poles in −2 < σ < 2 are the nontrivial zeros.
- For σ > 1: ζ(s+1)/ζ(s) = Σ_{n≥1} b(n) n^{−s}, with b(n) = n^{−1}∏_{p|n}(1 − p) and |b(n)| ≤ 1.
- For all s: F(s) = −2π cot(πs/2) · ζ(−s)/ζ(1−s). This follows from χ(s+1)/χ(s) = −2π cot(πs/2)/s and was checked to 1e-31.
- For σ < 0: ζ(−s)/ζ(1−s) = Σ_{n≥1} e(n) n^{s}, with e(n) = φ(n)/n.
- M(T) := T/(4π) + i(T²/(4π) − T). S(T) := Σ_{0<γ≤T} c₁(ρ). E(T) := S(T) − M(T).
- g_Δ is the centred Gaussian density with standard deviation Δ, and h_{T₁,T₂,Δ} := 1_{[T₁,T₂]} ∗ g_Δ = Φ((u−T₁)/Δ) − Φ((u−T₂)/Δ).
- 𝒟_Δ(T) := Σ_{n≥2} b(n) n^{−1/2−iT} e^{−Δ² log²n/2} / log n.

### 4.1 R1: Theorem A (exact formula for the velocity field)

**Statement.** Let h be entire with sup_{|Im z|≤3} (1+|Re z|)^A |h(z)| < ∞ for every A. Put H(s) := h(−i(s − 1/2)). Let T_k ∈ [k, k+1] be heights with |ζ(σ ± iT_k)|^{−1} ≪ T_k^A for −2 ≤ σ ≤ 2. Such heights exist by Titchmarsh Thm 9.7 (a Jensen-averaging argument, re-derived) together with the functional equation. Then

lim_k Σ_{|γ|<T_k} Res_{s=ρ}(F H) = (1/2π)∫(½ + iu) h(u) du + ∫(sech πu − i tanh πu) h(u) du − 4h(i/2) + Σ_{n≥2} b(n) n^{−1/2} ĥ₁(log n) + L(h),

where
- ĥ₁(ξ) := (1/2π)∫(½ + iu) h(u) e^{−iuξ} du,
- L(h) := (1/i)∫_{Re s = −3/2} cot(πs/2) [ζ(−s)/ζ(1−s) − 1] H(s) ds.

For simple zeros, Res(FH) = c₁(ρ)H(ρ); for zeros on the line, H(ρ) = h(γ).

**Proof.**
1. Apply the residue theorem on [−3/2, 2] × [−T_k, T_k]. The horizontal sides vanish because |F| grows at most polynomially at the heights T_k while H decays faster than any power. This gives Σ Res = (1/2πi)[∫_{(2)} − ∫_{(−3/2)}] F H ds.
2. Right line: expand F as s Σ b(n) n^{−s}, which converges absolutely, and integrate term by term. Each term s·n^{−s}·H(s) is entire, so shift it to Re s = 1/2. This gives n^{−1/2} ĥ₁(log n); n = 1 gives the first term of the formula.
3. Left line: −(1/2πi)∫_{(−3/2)} F H = (1/i)∫_{(−3/2)} cot(πs/2) · (ζ(−s)/ζ(1−s)) · H ds. Split ζ(−s)/ζ(1−s) as 1 + [ζ(−s)/ζ(1−s) − 1]. Shift the "1" part to Re s = 1/2 across the pole of cot at s = 0 (residue 2/π); this gives −4H(0) = −4h(i/2). Then use cot(π/4 + iπu/2) = sech πu − i tanh πu (checked). ∎

**Theorem A_a (all a > 0).** Replace F by F_a(s) = sζ(s+1,a)/ζ(s,a). For a window h_{T₁,T₂,Δ} with 10Δ ≤ T₁,

Σ Res(F_a H) = (1/a)[(T₂−T₁)/(4π) + i(T₂²−T₁²)/(4π)] − i(T₂−T₁) + (1/a) Σ_{λ>0} β_λ(a) e^{−λ/2} ĥ₁(λ) + O_{a,Δ}(1).

Here ζ(s+1,a)/ζ(s,a) = a^{−1} Σ_{λ∈Λ_a} β_λ e^{−λs} for Re s large, with β₀ = 1; the smallest positive λ is log((1+a)/a).

Proof sketch; the differences from Theorem A are:
- On the left line Re s = −b with b ∈ (3/2, 2), Hurwitz's formula gives F_a(s) = 2πi Λ_a(−s)/Λ_a(1−s) + O(|t|^{1/2−b}), where Λ_a(w) = Σ e^{−2πina} n^{−w}.
- For a > 1, subtract the finite Dirichlet polynomial; the left-line asymptotics are dominated by the Hurwitz part.
- The good-height lemma transfers verbatim to ζ(s,a).

**Check (a = 1).** `final_a1.py`, 100,000 zeros. LHS = Σ_zeros c₁h(γ) (conjugate zeros included). RHS = main + P_R + L_B, where L_B is evaluated in closed form after replacing cot by −i; the error of that replacement is O(e^{−πT₁/2}).

| [T₁,T₂] | Δ | LHS (= RHS) | relative difference |
|---|---|---|---|
| [100, 1000] | 1 | 59.581503 + 77852.853542i | 7.9e-17 |
| [1000, 20000] | 1 | 1614.935726 + 31731627.107108i | 1.2e-16 |
| [300, 24000] | 0.8 | −305.976929 + 45806589.457020i | 3.3e-16 |
| [5000, 74000] | 1.5 | 3204.585469 + 433708824.135901i | 1.5e-16 |
| [2000, 74000] | 5 | 5715.120454 + 435375925.596315i | 6.7e-18 |
| [10000, 70000] | 0.7 | 507.024372 + 381906665.203182i | 3.5e-17 |

Core of the right-hand side (`common.py`):
```
E0=(e^{-iT1ξ}-e^{-iT2ξ})/(iξ);  E1=(T1e^{-iT1ξ}-T2e^{-iT2ξ})/(iξ)+E0/(iξ);  ĝ=e^{-Δ²ξ²/2}
PR = Σ b(n) n^{-1/2} ĝ[(1/2+Δ²ξ)E0 + iE1]/(2π)      (ξ = log n)
LB = −Σ (φ(n)/n) n^{1/2} ĝ (n^{iT2} − n^{iT1})/ξ
main = (T2−T1)/4π + i(T2²−T1²)/4π − i(T2−T1)
```

**Check (a = 2).** `check_a2.py`, 610 certified zeros of ζ(s) − 1; direct trapezoid quadrature of F₂H on Re s = 3.4 and Re s = −1.75.

| [T₁,T₂], Δ | Σ c·H(ρ) | contour value | difference | main terms (1/a) |
|---|---|---|---|---|
| [100, 1000], 2 | −8.531339 + 38493.015532i | same | 7.8e-9 | 35.81 + 38490.85i |
| [150, 1050], 8 | 35.843683 + 42072.083923i | same | 1.2e-8 | 35.8099 + 42071.8346i |

At Δ = 8 the horizontal ratio is 1.0009 and the vertical difference is 0.25.

**Literature.**
- Searches: Hurwitz-zero trajectories and derivatives in a; sums over zeros of ζ(ρ+1)/ζ′(ρ); sums involving 1/ζ′(ρ).
- Found:
  - the velocity ODE (Frisk–de Gosson 2001);
  - the counting and tilt literature (§4.6);
  - different sums over zeros: generalized Landau–Gonek (arXiv:2601.18025), shifted-zero means (arXiv:2512.03297), complex moments of ζ′(ρ) (arXiv:2509.07788), Milinovich–Ng on Gonek's conjecture (arXiv:1106.1160).
- No treatment of Σ ρζ(ρ+1)/ζ′(ρ)·H(ρ) or of summed Hurwitz velocities was found. **Belief: new**, but the technique is the standard explicit-formula technique.
- Remark (classical by type; no specific source found): ζ(ρ+1)/ζ′(ρ) is the amplitude of ρ in the explicit formula for Σ_{n≤x} ∏_{p|n}(1−p) (residues of ζ(s)/ζ(s−1)·x^s/s at s = ρ + 1). So the Hurwitz velocities are, up to the factor ρ/(ρ+1), those amplitudes.

**Owner idea pushed:** claude-ab's shifted-sheet lane (N3) and the programme's zero-motion theorem. The residue heuristic is now an exact identity for every a.

### 4.2 R2: Corollary B (smoothed velocity laws with explicit error)

**Statement.** For Δ > 0, 10Δ ≤ T₁ < T₂ and h = h_{T₁,T₂,Δ}:

Σ Res(FH) = M(T₂) − M(T₁) + (1/2π)[T₁𝒟_Δ(T₁) − T₂𝒟_Δ(T₂)] + R,

with |R| ≤ K(Δ) + O(e^{−πT₁/2} + T₁e^{−T₁²/(8Δ²)}), where

K(Δ) = (1/π) Σ |b(n)| n^{−1/2} ĝ(log n)(½ + Δ² log n + 1/log n)/log n + 2 Σ (φ(n)/n) n^{1/2} ĝ(log n)/log n.

Moreover |𝒟_Δ(T)| ≤ d(Δ) := Σ |b(n)| n^{−1/2} ĝ(log n)/log n.

| Δ | K(Δ) | d(Δ) |
|---|---|---|
| 1 | 6.16 | 0.757 |
| 2 | 1.37 | 0.230 |
| 3 | 0.40 | 0.060 |
| 5 | 0.013 | 1.26e-3 |

Consequences:
- **Horizontal:** Re Σ = (T₂−T₁)/(4π) + O(T₂ d(Δ) + K(Δ)).
- **Vertical:** Im Σ = (T₂²−T₁²)/(4π) − (T₂−T₁) + O(T₂ d(Δ) + K(Δ)).
- If Δ ≥ (1+δ)√(2 log T₂)/log 2, both errors tend to 0. The −T term of the vertical law is thereby established rigorously in smoothed form.
- For general a, the main terms are (T₂−T₁)/(4πa) and (T₂²−T₁²)/(4πa) − (T₂−T₁). The horizontal term is exactly ∂_a of the Garunkštis–Steuding mean horizontal distribution (T/4π) log a; the leading vertical term is −∂_a ∫₀^T N(t;a) dt.

**Proof.** Insert the closed form ∫ h(u) e^{−iuξ} du = e^{−Δ²ξ²/2}(e^{−iT₁ξ} − e^{−iT₂ξ})/(iξ) and the analogous first-moment identity into Theorem A. Separate the T-linear part of ĥ₁, which gives 𝒟_Δ, and bound the rest term by term using |E₀| ≤ 2/ξ. The mean-density terms and h(i/2) are exponentially small for T₁ ≥ 10Δ. ∎

**Check.** For T between 3,000 and 54,000, the Gaussian-smoothed error computed from zeros minus −(T/2π)𝒟_Δ(T) stays bounded:

| Δ | rms residual, T < 2·10⁴ | rms residual, T ≥ 2·10⁴ | max residual | K(Δ) |
|---|---|---|---|---|
| 0.5 | 3.27 | 3.53 | 13.9 | 107 |
| 1 | 1.10 | 1.12 | 2.47 | 6.16 |
| 2 | 0.48 | 0.50 | 0.83 | 1.37 |

The smoothed error itself grows like T (rms of Esm/T = 0.072 at Δ = 1). The window table in §4.1 shows the transition directly: at Δ = 5 the horizontal law holds (5715.1 vs 5729.6, within the bound 14.8); at Δ = 0.7 it fails (507 vs 4775).

**Owner idea pushed:** N2 ↔ N3. The smoothed velocity law is the infinitesimal form of the tilt formula.

### 4.3 R3: Theorem C (the sharp laws fail at order T)

**Statement.** Assume RH and that all zeros are simple.
1. lim sup_{T→∞} |Re E(T)|/T = lim sup_{T→∞} |Im E(T)|/T = +∞.
2. lim sup_{X→∞} X^{−3}∫_X^{2X} |E(T)|² dT ≥ (7/(12π²)) Σ_{n≥2} b(n)²/(n log²n) ≈ 0.0373.
   - The sum is 0.6100 up to n = 10⁷, plus a tail of about 0.021.
   - The real part alone accounts for half of this bound.
3. Unconditionally, for the analytic windows: W_Δ(T) := Σ Res(F H_{T₁,T,Δ}) − [M(T) − M(T₁)] = −(T/2π)𝒟_Δ(T) + O_{Δ,T₁}(1). Hence X^{−3}∫_X^{2X} |W_Δ|² → (7/(12π²)) Σ b(n)² e^{−Δ² log²n}/(n log²n).

**Lemma U (unboundedness).**
- sup_T Re 𝒟_Δ(T) ≥ V(Δ) := Σ_{n≥2} b(n)λ(n) n^{−1/2} e^{−Δ² log²n/2}/log n, where λ is the Liouville function, and V(Δ) → +∞ as Δ → 0+.
- inf_T Im 𝒟_Δ(T) ≤ Im V_{πΔ²}(Δ) → −∞, where V_τ(Δ) is V(Δ) with each term also multiplied by n^{−iτ}.

**Proof of Lemma U.**
1. The numbers log p are linearly independent over Q, and 𝒟_Δ is an absolutely convergent series in n^{−iT}. By Kronecker's theorem its values on [T₀, ∞) are dense in {Σ c_n χ(n) : χ completely multiplicative, |χ(p)| = 1}. Taking χ = λ, and χ(p) = −p^{−iτ}, gives the two bounds.
2. The Dirichlet series of b(n)λ(n) has Euler factor (1 + p^{−s})/(1 + p^{−1−s}), so it equals ζ(s)B(s) with B(s) = ζ(2s+2)/(ζ(2s)ζ(s+1)). B is absolutely convergent for σ > 1/2, and B(1) = ζ(4)/ζ(2)² = 2/5. Hence Σ_{n≤x} b(n)λ(n) = (2/5)x + O(x^{1/2+ε}); numerically 0.40000 at x = 10⁷.
3. Partial summation with f(x) = x^{−1/2} e^{−Δ² log²x/2}/log x gives:
   - main term (2/5)∫_{log 2}^∞ e^{u/2 − Δ²u²/2} du/u ≥ (4/5) Δ e^{1/(8Δ²) − 1/2};
   - error O(e^{ε²/(2Δ²)}/Δ) with ε = 1/4;
   - so V(Δ) → ∞.
4. For τ = πΔ², complete the square in the same integral: the result is −i · 2√(2π) Δ e^{1/(8Δ²)}(1 + O(Δ)). Numerically, arg/π = −0.36, −0.39, −0.44, −0.478 at Δ = 0.3, 0.2, 0.15, 0.1. ∎

**Proof of Theorem C, part 1.**
1. Suppose |Re E(u)| ≤ Ku + C for u > 0. By conjugate symmetry, Re S̃(u) = u/(4π) + ρ(u) with |ρ(u)| ≤ K|u| + C′ for all real u, where S̃ is the conjugate-symmetric extension of S to u < 0 (S̃(u) := −conj S(|u|⁻)).
2. Under RH and simplicity, Σ c₁h(γ) = −∫ S̃ h′ du. The boundary terms vanish because S̃(T_k) is polynomially bounded at good heights, and the integral converges absolutely under step 1.
3. This gives |Re Σ − (T−T₁)/(4π)| ≤ K(T + T₁ + 2Δ) + O(1).
4. Corollary B then forces |Re 𝒟_Δ(T)| ≤ 2πK + o(1). By almost-periodicity this bound holds for all T, contradicting Lemma U for Δ small.
5. For Im, the same argument uses Im S̃(u) = u²/(4π) − |u| + Im E(|u|⁻). ∎

**Proof of Theorem C, part 2.** If the lim sup were L, Cauchy–Schwarz gives ∫_X^{2X} |E ∗ g_Δ|² ≤ (L + o(1))X³. The left side equals (7X³/(12π²))‖𝒟_Δ‖²(1 + o(1)). Let Δ → 0 by monotone convergence. ∎

**Check** (`final_a1.py`, 100,000 zeros, grid step 0.01):

| window | rms Re E/T | rms Im E/T | min Re E/T | max Re E/T | P(Σ Re c₁ < 0) |
|---|---|---|---|---|---|
| [1000, 2000] | 0.0923 | 0.0981 | −1.006 | 0.149 | 0.176 |
| [4000, 8000] | 0.0930 | 0.0948 | −1.953 | 0.162 | 0.178 |
| [16000, 32000] | 0.0927 | 0.0932 | −2.766 | 0.173 | 0.178 |
| [32000, 64000] | 0.0923 | 0.0927 | −3.153 | 0.174 | 0.176 |

- There is no decay: E(T) is of order T. About 18% of the time the sharp horizontal sum Σ Re c₁ is **negative**.
- The Bohr–Fourier coefficients of the **sharp** E(T)/T over [2000, 74860] (mean of (E/T)·e^{iT log n}) match the prediction −b(n)/(2π√n log n):

| n | observed | predicted |
|---|---|---|
| 2 | +0.081180 | +0.081180 |
| 3 | +0.055760 | +0.055760 |
| 4 | +0.014350 | +0.014351 |
| 5 | +0.035379 | +0.035379 |
| 6 | −0.012086 | −0.012088 |
| 7 | +0.026499 | +0.026497 |
| 10 | −0.008748 | −0.008743 |
| 13 | +0.015886 | +0.015886 |
| 15 | −0.008089 | −0.008093 |
| 30 | +0.002275 | +0.002278 |
| 60 | +0.000664 | +0.000669 |

- All imaginary parts are ≤ 7e-6. Control frequencies 0.5, 0.9, 1.3, 2.0 give ≤ 1.3e-5, and the mean of E/T is about 1e-4.
- Parseval prediction: complex rms 0.1265 (real part 0.0894). Observed: 0.1312 (real 0.0925). So about 93% of the mean square is this spectrum.
- Observed X^{−3}∫|E|² ≈ 0.040, above the bound 0.0373.

**Answer to "explain why the horizontal law fails."**
- E(T)/T is an almost-periodic function of order 1, dominated by 0.0812·cos(T log 2) (period 9.06) and 0.0558·cos(T log 3). Its rms is 0.092, while the "law" coefficient is 1/(4π) = 0.0796.
- The amplitudes are the Dirichlet coefficients of ζ(s+1)/ζ(s). No lower-order term separates from the main term.

### 4.4 R4: primes from the zero velocities

**Statement.** The spectral amplitude of E(T)/T at frequency log n is a_n = −b(n)/(2π n^{1/2} log n).
- Since |n·b(n)| = ∏_{p|n}(p − 1) ≤ φ(n), with equality iff n is prime, n is prime ⟺ a_n = (n−1)/(2π n^{3/2} log n), the largest possible value.
- Rigorous for every smoothed version (Δ > 0, amplitudes a_n e^{−Δ² log²n/2}, unconditional).
- For the sharp E/T: conditional on existence of the Bohr means, which needs mean-square bounds of J₋₁ type. Numerically confirmed above: n = 2, 3, 5, 7, 11, 13 give 0.08118, 0.05576, 0.03538, 0.02650, 0.01820, 0.01589.

**Owner idea pushed:** the timed-primes lane (TP0–TP14). The waiting times log n appear as the frequencies of the zero-velocity field of the unit shift n ↦ n + t (the exact counting step), and the primes are its maximal-amplitude frequencies.

### 4.5 The owner's framing, made exact

Let R(a,T) := Σ_{0<γ(a)≤T}(β(a) − ½) − (T/4π) log a. This is O(log T), by Garunkštis–Steuding for a ≤ 1 and by the same proof for a > 1.
- For T not an ordinate, the zeros below T continue analytically for a near 1 and none crosses height T (Rouché). Hence ∂_a R(1,T) = Re E(T).
- **"Derivative uncontrolled": true.** ∂_a R(1,T) has rms 0.092·T and |∂_a R|/T is unbounded (Theorem C, part 1).
- **"Dominated by small |ζ′|": false for the bulk.** About 93% of the mean square is the zero-free spectrum of §4.3.
- **True for the tails.** The five most negative values of Re E/T (−2.77, −2.02, −1.96, −1.95, −1.92) all occur just after the first member of a close pair: gaps 0.033–0.044, |ζ′| = 0.24–0.44, |c₁|/γ = 1.9–2.7. The five most positive values are only +0.17, at zeros with |ζ′| between 12 and 18.

### 4.6 N2 status

- **Known for 0 < a ≤ 1.**
  - Count: N(T) = (T/2π) log(T/(2πea)) + O(log T), Garunkštis–Laurinčikas, *Number theory and its applications* (Kluwer 1999), for Lerch zeta.
  - Tilt: Σ_{|γ|≤T}(β − ½) = (T/2π) log(α/√(λ(1−{λ}))) + O(log T), Garunkštis–Steuding, *Analysis* 22 (2002) 1–12. With λ = 1 this is (T/4π) log a for 0 < γ ≤ T.
  - I read these through their restatements in Garunkštis–Tamošiūnas, arXiv:1901.10790 and arXiv:1902.03064; the originals were not accessible (HTTP 405).
- **For a > 1 the same proof applies.** Use Littlewood's lemma with g(s) = a^s ζ(s,a). On the left line, |ζ(−b+it, a)| = (t/2π)^{1/2+b} |Λ_a(1+b−it)| (1 + o(1)), and the mean of log|Λ_a| is 0 because its leading coefficient has modulus 1. This gives 2πΣ(β + b) = −bT log a + (½ + b)(T log(T/2π) − T) + O(log T). Subtracting (½ + b)N(T) leaves (T/4π) log a.
- The a = 2 case matches the known 1-point asymptotics of ζ.
- **Check at a = 2:**

| T | N | predicted N | Σ(β − ½) | (T/4π) log 2 |
|---|---|---|---|---|
| 300 | 105 | 103.74 | 15.43 | 16.55 |
| 600 | 276 | 273.67 | 32.74 | 33.10 |
| 1000 | 539 | 537.42 | 54.17 | 55.16 |

### 4.7 Remark (conditional; source recalled, not re-read)

Under RH, Titchmarsh §14.16 (as I recall it) gives heights T_ν with |1/ζ(σ + iT_ν)| ≪ T_ν^ε for ½ ≤ σ ≤ 2. The contour argument then yields S(T_ν) = M(T_ν) + O(T_ν^{1+ε}). Combined with Theorem C: the vertical law's leading term T²/(4π) is correct, but its error is neither O(T) nor established beyond O(T^{1+ε}). The −T term is meaningful only in smoothed form (Corollary B). I could not re-read §14.16 in this session (the fetched PDF was truncated), so treat that step as recalled.

## 5. T1: the receiver of TD8/TD12's obstruction

**Construction.** Let S := {0, ∞, 1, −1} = P¹(F_{1²}) (in the μ_n convention, the F_{1²}-points are 0, ∞ and the square roots of unity). For B ⊆ S with |B| even, let L_B be the sign local system on P¹ − B with monodromy ε = −1 at each point of B, and M_B := H¹(P¹, j_*L_B). This is the ε-anti-invariant part of H¹ of the double cover branched at B, which has genus |B|/2 − 1.

1. **Obstruction.** If |B| ≤ 2, then M_B = 0. Every even B inside the F₁-points {0, 1, ∞} has |B| ≤ 2. The Codex torus sign system is the case B = {0, ∞}. So over the F₁ base (mirror T ↦ 1/T) there is no nonzero pure sign sector. The Weyl mirror forces ε into the base, and ε supplies the fourth branch point.
2. **Receiver.** For B = S, the double cover is E: y² = x³ − x = x(x−1)(x+1), and M_S = H¹(E) has rank 2. For odd p:
   - Frob_p has characteristic polynomial X² − a_p X + p;
   - a_p = 0 for p ≡ 3 (mod 4), with eigenvalues ±i√p;
   - a_p = 2 Re π_p for p ≡ 1 (mod 4), where π_p is the Gaussian prime above p with π_p ≡ 1 (mod 2+2i).
   - Weight one: |eigenvalue| = √p (Hasse; equivalently, via CM, the norm form N(π_p) = p).
3. **ε-splitting of TD8.** #E(F_{p^r}) = (1 + p^r) − Tr(Frob^r | M_S). TD8's count 1 + p^r is exactly the ε-invariant part; the numerator 1 − a_p t + p t² is the sign sector.
4. **J.** The map [J]: (x, y) ↦ (εx, Jy) = (−x, iy) is an automorphism of E. [J]² is the hyperelliptic involution, which acts as −1 = ε on M_S, so J² = ε on the sector. Also Frob_p∘[J] = [J]^p∘Frob_p. This is CC's rule Fr_n(J) = J^n: Frobenius commutes with J for p ≡ 1 (mod 4) and inverts it for p ≡ 3 (mod 4).
5. **Mirror.** CC's α (x ↦ −1/x) lifts to E as translation by the 2-torsion point (0,0), namely (x, y) ↦ (−1/x, y/x²). So α acts trivially on M_S. For p ≡ 3 (mod 4), CC's Fr_p (mod p) = α∘Frob, which lifts to τ_{(0,0)}∘Frob. The sector descends to the mirror quotient as H¹(E′), with E′ = E/⟨(0,0)⟩: y² = x³ + 4x (2-isogenous).
6. **Typed morphism to TD12.** Let ψ((α)) := α for α ≡ 1 (mod 2+2i) be the Hecke character of Q(i). For odd n, ψ(nZ[i]) = χ₋₄(n)·n = d(n), TD12's signed degree on H¹(C^×). Also det(Frob_p | M_S) = p, TD3's degree on H². The sector's Frobenius is thus a square root of TD12's weight-two data: ψ(𝔭)ψ(𝔭̄) = d(p) for split p, and eigenvalue² = d(p) for inert p.
7. **Archimedean fibre.** [J]*(dx/y) = i·dx/y, so [J]* is the Weil operator of the weight-one Hodge structure, with C² = (−1)^1 = ε. The Codex weight-one twistor bundle O(1)⊕O(1) with quaternionic structure (TD10–TD11) is its twistor realization.

**Proof.** Riemann–Hurwitz; direct coordinate computations; classical CM theory (Deuring; Weil 1952) or elementary Hasse. The sign convention in item 2 was fixed numerically.

**Check** (`t1_checks.py` plus inline scripts):
- sympy confirms: α maps E to E; J maps E to E; J² = (x, −y); α = P + (0,0) by the chord formula; α∘J = J∘α; the Vélu isogeny maps E onto y² = x³ + 4x and is α-invariant.
- For all odd p < 20,000: 1,136 inert primes all have a_p = 0; 1,125 split primes all have a_p = 2 Re π_p, and none match −2 Re π_p.
- Brute-force counts over F_{p^r} for p ∈ {3, 5, 7, 11, 13}, r ≤ 3, equal 1 + p^r − (α^r + β^r) with |α|/√p = 1.000000000000. Example: p = 13 gives 8, 160, 2216 against the CC line counts 14, 170, 2198.
- a_p(E) = a_p(E′) for all odd p < 3000.
- The primary generator of (n) is χ₋₄(n)·n for all odd n ≤ 2000.

**Scope and negative part.**
- The global L-function of this sector is L(E,s) = L(ψ,s) (conductor 32). The sector therefore does **not** carry the zeros of ζ.
- It answers TD12's request (a nonzero coefficient sector, with an arithmetic operator and a proved weight-one pairing) only locally, prime by prime, plus the archimedean fibre.
- **Literature:** a search for y² = x³ − x in the field-with-one-element literature found nothing specific. All ingredients are classical; the identification with CC's F_{1²}-points, ε, J and odd Frobenius is, to my knowledge, the programme's own.
- **Owner ideas pushed:** "construct the receiver of the obstruction"; J² = ε; the Codex twistor lane; odd Frobenius.

## 6. T2: Beurling framing

**No new theorem.**

**Literature record.**
- Hilberdink, "Generalised prime systems with periodic integer counting function", *Acta Arith.* 152 (2012), as summarized in Schlage-Puchta, arXiv:2110.00995:
  - for continuous systems, N(x) − cx periodic and C¹ forces N(x) = c(x−1) + 1;
  - ζ_P = (s−1+c)/(s−1) then has no zeros in the critical strip;
  - the prime measure is positive only for c ≤ c₀, with c₀ = 1.25479·10¹⁹ (Schlage-Puchta).
- Hilberdink (JNT 2005): max(α, β) ≥ 1/2 (recalled).
- Diamond–Montgomery–Vorhauer (2006) and Zhang (2007): from your packet.
- Found but not read: Broucke–Debruyne–Vindas, arXiv:2004.11501; Beurling zero-density, arXiv:2409.10051.
- Diamond–Zhang's book and the Hilberdink–Lapidus paper were not accessed. The Reading repository copy of Hilberdink 2012 returned access-denied.

**Small verified example.** Integer-valued near-exactness does not pin down P. Take P = (primes \ {2}) ∪ {a second 3, 4}. Then ζ_P = ζ·(1−2^{−s})/((1−3^{−s})(1−4^{−s})), R(1) = 1, and N_P(x) = x + O(log²x). The observed values of N_P(x) − x at x = 10², …, 10⁶ are −1, 0, 1, −3, 0, verified against a direct multiset count for x ≤ 3000. Its zeros in σ > 0 are exactly those of ζ. So exactness pins the system; weak regularity does not move the zeros either.

**Open question (as I read the literature; not verified exhaustively).** Does N(x) = cx + O(x^θ) with θ < 1/2 force ζ_P ≠ 0 for σ > 1/2?

**Connection to T3.** The velocity field of R1 uses the additive shift n ↦ n + t. The analogous deformation exists for any Beurling system, but the left-line evaluation in R1 needs a functional equation, which general Beurling zetas lack.

## 7. Failed or limited attempts (exact scope)

1. **Pointwise vertical law with error O(T):** false under RH + simple zeros (Theorem C). Unconditional pointwise bounds are unavailable by this method, because the contour's top edge needs bounds on 1/ζ near the line.
2. **Sign-specific Ω results** (lim sup Re E/T = +∞ and lim inf = −∞ separately): **not proved.** A one-sided hypothesis does not make the Gaussian averages converge absolutely. The data are strongly one-sided: min Re E/T = −3.15, max = +0.17 up to T = 64,000.
3. **Bohr coefficients of the sharp E/T:** proved only after smoothing. The sharp statement is conditional on J₋₁-type mean-square bounds.
4. **T1:** the receiver is not ζ's sector (see §5). Any weight-one sector changes TD8's count 1 + p^r, so it cannot live in constant coefficients on CC's line.
5. **Process:** my first grid-Newton finder for the zeros of ζ(s) − 1 missed about 20 roots. It was replaced by the certified subdivision method before any result was drawn.

## 8. Sources consulted

- [Garunkštis–Tamošiūnas, arXiv:1902.03064](https://arxiv.org/pdf/1902.03064) and [arXiv:1901.10790](https://arxiv.org/pdf/1901.10790) (restating Garunkštis–Laurinčikas 1999 and Garunkštis–Steuding 2002; [original on De Gruyter](https://www.degruyterbrill.com/document/doi/10.1524/anly.2002.22.1.1/html), not accessible)
- [Frisk–de Gosson, arXiv:math-ph/0102007](https://arxiv.org/html/math-ph/0102007)
- [arXiv:2601.18025](https://arxiv.org/html/2601.18025), [arXiv:2512.03297](https://arxiv.org/html/2512.03297), [arXiv:2509.07788](https://arxiv.org/html/2509.07788v1), [arXiv:1106.1160](https://ar5iv.arxiv.org/html/1106.1160)
- [Schlage-Puchta, arXiv:2110.00995](https://arxiv.org/html/2110.00995); [Hilberdink 2012 (CentAUR record)](https://centaur.reading.ac.uk/23409/)
- [DMV, Math. Ann. 2006](https://link.springer.com/article/10.1007/s00208-005-0638-2); [arXiv:2004.11501](https://ar5iv.arxiv.org/html/2004.11501); [arXiv:2409.10051](https://arxiv.org/html/2409.10051)
- [Titchmarsh PDF](https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf) (truncated fetch; §9.7 re-derived, §14.16 recalled)
- [Garunkštis publication list](https://klevas.mif.vu.lt/~garunkstis/)
