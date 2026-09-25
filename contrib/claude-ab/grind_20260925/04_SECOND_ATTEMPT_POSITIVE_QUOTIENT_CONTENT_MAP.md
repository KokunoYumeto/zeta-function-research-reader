# The second attempt, part 2: the positive-quotient lane and its analytic foundation

A content map of part of the three-lane edition, `continuations/20260924-cohomology-weight-and-character-lifts` (zeta-function-research-reader, commit 064f33b).

Claude (Opus 5.5 configuration), 25 September 2026.

## Scope of reading

**Read in full:**
- `gct-weight-control/proofs/GLOBAL_MELLIN_SYNTHESIS.md` (S1–S7), the analytic foundation that the positive-quotient lane uses;
- `geometric-positive-quotient/POSITIVE_QUOTIENT_SOURCE_AND_ARITHMETIC.md` (PSC0–PSC9);
- `CONTINUOUS_POSITIVE_TRANSFER_FORMS.md` (CFP0–CFP12, CFPA);
- `POSITIVE_SOURCE_COMPLETION_AND_SPECIALIZATION.md` (CPS0–CPS8).

**Read in part:** `GLOBAL_HISTORY_WEIL_ENERGY.md` (GHE1 only).

**Not yet read:**
- PTQ (the bounded-form predecessor, which CFP states it supersedes);
- the exact-image theorem SSI;
- GDC, AST, ADM;
- the sheaf-side ACD/ADC/DCA proofs;
- the 63-part Deligne reconstruction of the weight-control lane;
- the character-lifting lane.

These are the next reading blocks.

## 1. The objects, stated plainly

- 𝒜 consists of the smooth functions on (0, ∞) that decay faster than every power at 0 and at ∞, together with all their derivatives u∂_u.
- ℬ consists of the entire functions that decay faster than every power of \|t\| on every vertical strip.
- The centred Mellin transform, ℳk(s) = ∫ k(u) u^{s−1/2} du/u, is a topological isomorphism 𝒜 → ℬ (S1).
- Connes' map ℰ sends an even Schwartz function f with f(0) = 0 and ∫f = 0 to u^{1/2} Σ_{n≥1} f(nu).
- ℐ_ζ is the set of functions in 𝒜 (equivalently ℬ) whose Mellin transform vanishes to its full multiplicity m_ρ at every nontrivial zero ρ of ζ.
- The source quotient is 𝒬 = ℬ/ℐ, a Fréchet space.
- The scaling operators are T_a[F] = [a^s F(s)]; for integers n, the transfer is n·T_{1/n}.
- The Weil form is W(F, G) = Σ_ρ m_ρ F(ρ) \overline{G(1 − ρ̄)}. It splits as W = W_L + W_O, the parts coming from zeros on the critical line and off it.

## 2. What the lane establishes

1. **Spectral synthesis for Connes' map** (S5, with S3–S4).
   - The closure of ℰ(even Schwartz functions with f(0) = 0 and ∫f = 0) in 𝒜 is exactly ℐ_ζ.
   - Hence the joint map to all zero-jets is injective on 𝒬 (S7): every class in the quotient is detected by the jets of ζ's actual zeros with their multiplicities.
   - The proof uses:
     - the kernel k₀ built from f₀(v) = (π/2)v²(2πv² − 3)e^{−πv²}, whose Mellin transform is F₀(s) = (s(s−1)/8) π^{−s/2}Γ(s/2)ζ(s) = ξ(s)/4;
     - Hadamard factorization of F₀;
     - a division bound log\|F/F₀\| = O(\|t\|^{3/2} log\|t\|) on strips, including near clustered zeros;
     - Gaussian regularization e^{ε(s−1/2)²}.
   - A later note (SSI, not yet read by me) states that the image is closed.
2. **Exact split of the Weil form and its explicit formula** (PSC1–PSC5).
   - W_L ≥ 0.
   - On an off-line pair, W_O takes the value −2m_ρ on e_ρ − e_{ρ^#} and +2m_ρ on the sum, where ρ^# = 1 − ρ̄.
   - The positive part has the exact arithmetic expression W_L = A(0) + A(1) + 𝒜_∞ − P_hist − W_O, where P_hist has the von Mangoldt coefficients (log L_n − log L_{n−1}) with L_n = lcm(1, …, n).
   - The full quotient 𝒬 is the fibre product of its line and off-line jet quotients over an explicit defect module C_rec (PSC3).
   - A holomorphic projector separating the two exists exactly when two multiplier ideals sum to the whole ring. Its existence would force the separation estimate 1 ≤ C(1 + \|Im ρ\|)^N \|ρ − η\| between line zeros ρ and off-line zeros η (PSC8).
3. **Classification of positive forms compatible with the transfer** (CFP).
   - A continuous positive semidefinite Hermitian form B on 𝒬 satisfies B(T_nF, G) = B(F, nT_{1/n}G) for all n if and only if B(F, G) = Σ_{Re ρ = 1/2} m_ρ c_ρ F(ρ)\overline{G(ρ)} with 0 ≤ c_ρ ≤ C(1 + \|Im ρ\|)^d.
   - Proof steps:
     - the transfer identity makes V_t = e^{−t/2}T_{e^t} unitary on the completion;
     - the kernel k annihilates it (∫k(t)V_t dt = 0, because F₀ℬ ⊂ ℐ);
     - a Bochner-type spectral argument (CFPA) puts all spectral mass on the ordinates of critical-line zeros;
     - Gaussian division shows that each zero carries rank at most one, so higher jets are always killed.
   - No RH or simplicity assumption is used.
4. **The positive completion and the obstruction** (CPS).
   - The intersection of the radicals of all such forms is N_L, the classes vanishing at every line zero.
   - The completion under all of them is a weighted rapid-decay sequence space on the line zeros.
   - The obstruction quotient R = 𝒬/N_O (with N_O the classes vanishing at every off-line zero) admits no nonzero compatible positive form. This is proved without assuming anything about whether off-line zeros exist.

## 3. Checks (claude-ab)

Script: `checks/lane_pq_checks.py`. All pass.

- **The source multiplier.** ∫₀^∞ f₀(v) v^{s−1} dv = s(s−1)/8 · π^{−s/2}Γ(s/2). Verified at s = 3, 2.5 + i and 0.5 + 14i, with errors ≤ 10⁻³¹. Also ∫f₀ = 0, and f₀ equals its own Fourier transform at y = 0.7.
- **The transfer core of CFP.**
  - On an eigenvector at ρ, compatibility forces B(T_nx, T_nx) = n^{2 Re ρ}B(x, x) = nB(x, x), so B(x, x) = 0 unless Re ρ = 1/2.
  - For sufficiency, n^ρ = n·\overline{n^{−ρ}} holds exactly when Re ρ = 1/2. Checked at ρ = ½ + 14.1347i, where it holds, and at 0.7 + 20i, where it fails by 0.77.
- **The off-line value.** W(e_ρ − e_{ρ^#}) = −2m_ρ.
- **Not re-checked:** the division bound S3 in detail, CFPA's measure-theoretic steps, and PSC3's topological exactness. I read these proofs and found no gap, but did not re-derive every estimate.

## 4. Reading the lane as a whole (my assessment, labelled as such)

- **Where the RH content sits.** In this formalism the lane locates the content of RH exactly. RH is equivalent to W_O ≡ 0, equivalently N_O = 𝒬, equivalently R = 0 (PSC5 end, CPS4). The positive part W_L is fully described. The obstruction R is invisible to every positive form compatible with the scaling transfer.
- **Negative result for positivity strategies (goal 1).** A strategy that builds a continuous positive receiver compatible with the transfer can never detect or kill the off-line obstruction, because every such receiver is zero on it (CPS4.2). Killing R needs a mechanism of a different type, such as the weight separation pursued in the Deligne lane. The lane states this itself.
- **Relation to the literature.**
  - The substance is classical: Weil's criterion that RH is equivalent to positivity of the Weil distribution; Connes' spectral realization through the cokernel of ℰ (arXiv:math/9811068); and Meyer's nuclear Fréchet realization, "an operator on a nuclear Fréchet space whose spectrum is the set of non-trivial zeros of zeta" (arXiv:math/0412277, abstract).
  - What the lane adds is the complete bookkeeping: the exact Fréchet-category classification with polynomially growing weights and higher jets, the fibre-product reconstruction, and the separation estimate forced by a holomorphic projector.
  - I have not compared these with Meyer's paper line by line, so novelty is undetermined.
- **Bridges (goal 2).** The lane links three frameworks by explicit maps:
  - Connes' ℰ and the Meyer-type realization (noncommutative geometry);
  - the Weil explicit formula with von Mangoldt coefficients (analytic number theory);
  - the receiver/obstruction language of the Deligne lane (algebraic geometry).

  The maps are S7, PSC3–PSC5 and CPS5.
- **Standalone lemmas (goal 3).** Candidates:
  - CFP's classification of transfer-compatible positive forms on ℬ/ℐ;
  - PSC8's separation estimate implied by a holomorphic projector.

  Both can be stated with no programme vocabulary. Novelty is unchecked.

## Sources

- The programme files named above, zeta-function-research-reader, commit 064f33b.
- A. Connes, *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*, [arXiv:math/9811068](https://arxiv.org/abs/math/9811068).
- R. Meyer, *A spectral interpretation for the zeros of the Riemann zeta function*, [arXiv:math/0412277](https://arxiv.org/abs/math/0412277); abstract only.
- The explicit formula as attributed in PSC5: Guinand (1949), Weil (1952), through Connes, [arXiv:2602.04022](https://arxiv.org/abs/2602.04022).
