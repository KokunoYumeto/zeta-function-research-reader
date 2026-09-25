# Theorem C proved in full: the summed Hurwitz zero velocities fluctuate at order T

Claude (claude-ab lane), model `claude-opus-5-5` (Opus 5.5) at maximum reasoning effort. 25 September 2026, 08:51 UTC. Revised 09:32 UTC after the sixth referee pass (§9).

This carries out board task 4, which was proposed for claude-b5 and left unattended when that session ended. The task asked for an independent re-proof of Theorem C, parts 1–2, of the second Claude instance ("copy-newresults"; `02_` §4.3, hypotheses in `03_` §4).

**Relation to the copy's proof.** The proof below follows the route of the copy's sketch in `02_` §4.3. It uses the same Lemma U: the twist by the Liouville function, the mean 2/5, the bound (4/5)Δe^{1/(8Δ²)−1/2} and the rotation τ = πΔ². It also uses the same Kronecker, almost-periodicity and good-height steps. It is therefore a completion of that proof, not an independent route. It adds four things to the sketch:
1. the derivation of the error term O(x^{1/2+ε}) in Lemma 20.2(a);
2. the range Δ ≤ 0.39 in which the interval bound of Lemma 20.2(b) is valid;
3. Lemma 20.5, which justifies the Stieltjes form of Theorem A's sum under the hypothesis of each part, including the conjugate zeros and the boundary terms at the good heights. Part 2 has only a mean-square hypothesis, and the sketch does not address this step there;
4. in part 2, the treatment of the window edges (Jensen's inequality, then averaging over the window's starting point), which the sketch's one-line Cauchy–Schwarz step omits.

The proof takes one input as given, Theorem A, the copy's exact formula for the smoothed velocity sums. I previously checked Theorem A numerically to relative accuracy 1.8·10⁻¹⁸, with independent zeros and code, and re-derived the structure of its right-hand side (`02_`, verification record). Everything else is proved here or checked by `checks/theorem_c_reproof_checks.py`. The independent sieve of the sixth referee pass, `checks/referee_theorem_c_independent_checks.py`, reproduces the constants.

**Connection to `17_`.** The quantity summed is the zero velocity of `17_` §1, c₁(ρ) = dρ/da|_{a=1} = ρζ(ρ+1)/ζ′(ρ), which is read one line to the right. So Theorem C is a statement about the collective motion of the zeros under the owner's Hurwitz shift ζ(s, 1+t). The motion is not a uniform drift: it oscillates at order T, with frequencies log n and amplitudes set by b(n) = n^{−1}∏_{p|n}(1 − p).

## 0. Notation (as in `02_` §4)

- F(s) = sζ(s+1)/ζ(s). At a simple zero ρ, Res_{s=ρ}F = c₁(ρ).
- For Re s > 1, ζ(s+1)/ζ(s) = Σ_{n≥1} b(n)n^{−s} with b(n) = n^{−1}∏_{p|n}(1−p), so |b(n)| ≤ 1.
- S(T) = Σ_{0<γ≤T} Res_{s=ρ}F, the sum over distinct zeros.
- M(T) = T/(4π) + i(T²/(4π) − T), and E(T) = S(T) − M(T).
- g_Δ is the centred Gaussian density with standard deviation Δ, and h = h_{T₁,T,Δ} = 1_{[T₁,T]} ∗ g_Δ, which is real.
- ĝ(ξ) = e^{−Δ²ξ²/2}.
- 𝒟_Δ(T) = Σ_{n≥2} c_n n^{−iT}, with c_n = b(n)n^{−1/2}e^{−Δ² log²n/2}/log n. The series converges absolutely.
- **Hypothesis (H).** All but finitely many nontrivial zeros are simple and lie on the critical line.

**Theorem C** (copy-newresults).

1. Under (H), lim sup_{T→∞}|Re E(T)|/T = lim sup_{T→∞}|Im E(T)|/T = +∞.
2. Under (H), lim sup_{X→∞} X^{−3}∫_X^{2X}|E(T)|²dT ≥ (7/(12π²))Σ_{n≥2} b(n)²/(n log²n) ≈ 0.0373.
3. Unconditionally, W_Δ(T) := Σ_ρ Res(F H) − [M(T) − M(T₁)] = −(T/2π)𝒟_Δ(T) + O_{Δ,T₁}(1). Here H(s) = h(−i(s − ½)), and the sum over ρ is Theorem A's limit.

## 1. The input: Theorem A

For h entire of rapid decay in |Im z| ≤ 3 and H(s) = h(−i(s − ½)),

Σ_ρ Res_{s=ρ}(FH) = (1/2π)∫(½ + iu)h(u)du + ∫(sech πu − i tanh πu)h(u)du − 4h(i/2) + Σ_{n≥2} b(n)n^{−1/2}ĥ₁(log n) + L(h),

where ĥ₁(ξ) = (1/2π)∫(½ + iu)h(u)e^{−iuξ}du, L(h) is the left-line term of `02_` §4.1, and the sum over ρ is the limit over the good heights T_k. (Copy's Theorem A; checked by me, `02_`.)

## 2. Part 3: the smoothed error is −(T/2π)𝒟_Δ(T) up to O(1)

**Proposition 20.1.** For fixed Δ > 0 and T₁ ≥ 10Δ, as T → ∞,

  Σ_ρ Res(F H) = M(T) − M(T₁) − (T/2π)𝒟_Δ(T) + O_{Δ,T₁}(1).

**Proof.** Go through the terms of Theorem A for h = h_{T₁,T,Δ}.

1. **The main terms.** (1/2π)∫(½ + iu)h(u)du = (T − T₁)/(4π) + i(T² − T₁²)/(4π) + O_Δ(1). This is because ∫h = T − T₁ exactly and ∫u·h(u)du = (T² − T₁²)/2 exactly, since the Gaussian has mean 0.
   - The term −i∫tanh(πu)h(u)du = −i(T − T₁) + O(1), because 1 − tanh πu = O(e^{−2πu}) on the support region u ≥ T₁ − O(Δ) and h has Gaussian tails.
   - The two remaining terms are bounded independently of T. Since 0 ≤ h ≤ 1, 0 ≤ ∫sech(πu)h(u)du ≤ ∫sech(πu)du = 1. Since |g_Δ(i/2 − v)| = g_Δ(v)e^{1/(8Δ²)}, |h(i/2)| ≤ e^{1/(8Δ²)}∫_{T₁}^∞g_Δ(v)dv ≤ ½e^{(1/4 − T₁²)/(2Δ²)}, which is O_{Δ,T₁}(1).
   - Together these give M(T) − M(T₁) + O(1).
2. **The prime sum.**
   - ĥ(ξ) = ĝ(ξ)(e^{−iT₁ξ} − e^{−iTξ})/(iξ), and ∫u h(u)e^{−iuξ}du = iĥ′(ξ), so ĥ₁ = (1/2π)(½ĥ − ĥ′).
   - The T-dependent part of ĥ is −ĝ e^{−iTξ}/(iξ). Differentiating shows that its contribution to ĥ₁ is −(T/2π)ĝ(ξ)e^{−iTξ}/ξ plus terms without the factor T. I checked this with sympy: the coefficient of T in the T-part of ĥ₁·e^{iTξ} is exactly −ĝ/(2πξ).
   - Summing over n with weights b(n)n^{−1/2} at ξ = log n gives −(T/2π)𝒟_Δ(T).
   - The remaining terms are bounded uniformly in T by Σ|b(n)|n^{−1/2}ĝ(log n)(½ + Δ² log n + 1/log n)/log n + |T₁|·(the same with one factor less). These sums converge because ĝ(log n) = e^{−Δ² log²n/2}.
3. **The left-line term.** On Re s = −3/2, cot(πs/2) = −i + O(e^{−π|t|}), and ζ(−s)/ζ(1−s) − 1 = Σ_{n≥2}(φ(n)/n)n^{s} converges absolutely.
   - Integrating each term against H gives (φ(n)/n)n^{1/2}ĝ(log n)(n^{iT} − n^{iT₁})/log n, up to sign. In absolute value this is at most 2(φ(n)/n)n^{1/2}e^{−Δ² log²n/2}/log n, which is summable.
   - So L(h) = O_Δ(1) uniformly in T.
   - The cot-replacement error is O(e^{−πT₁/2}). ∎

## 3. Lemma U: 𝒟_Δ is unbounded in both parts as Δ → 0

**Lemma 20.2.**

(a) Σ_{n≥1} b(n)λ(n)n^{−s} = ζ(s)B(s) with B(s) = ζ(2s+2)/(ζ(2s)ζ(s+1)). B converges absolutely for Re s > ½, and B(1) = 2/5. Hence Σ_{n≤x} b(n)λ(n) = (2/5)x + O(x^{1/2+ε}).

(b) V(Δ) := Σ_{n≥2} c_nλ(n) → +∞ as Δ → 0⁺. More precisely V(Δ) = (2/5)∫_{log 2}^∞ e^{u/2 − Δ²u²/2}du/u + O(e^{1/(32Δ²)}/Δ), and for Δ ≤ 0.39 the main term is at least (4/5)Δe^{1/(8Δ²) − 1/2}.

(c) For τ = πΔ², V_τ(Δ) := Σ c_nλ(n)n^{−iτ} has Im V_τ(Δ) → −∞ as Δ → 0⁺.

(d) sup_{T≥T₀} Re 𝒟_Δ(T) ≥ V(Δ) and inf_{T≥T₀} Im 𝒟_Δ(T) ≤ Im V_τ(Δ), for every T₀.

**Proof.**

(a) At p^k, b(p^k)λ(p^k) = (1 − p)(−1)^k p^{−k}. So the Euler factor is 1 + (1 − p)Σ_{k≥1}(−p^{−1−s})^k = (1 + p^{−s})/(1 + p^{−1−s}).
- The Euler factor of ζ(s)B(s) is (1 − p^{−s})^{−1}(1 − p^{−2s})(1 − p^{−1−s})/(1 − p^{−2−2s}), which is the same. Both identities were checked symbolically.
- 1/ζ(2s) converges absolutely for Re s > ½, 1/ζ(s+1) for Re s > 0, and ζ(2s+2) for Re s > −½. So B converges absolutely for Re s > ½.
- B(1) = ζ(4)/ζ(2)² = (π⁴/90)/(π⁴/36) = 2/5.
- Writing b(n)λ(n) = Σ_{m|n}β(m) with Σβ(m)m^{−s} = B(s): Σ_{n≤x} = Σ_{m≤x}β(m)⌊x/m⌋ = xB(1) − xΣ_{m>x}β(m)/m + O(Σ_{m≤x}|β(m)|). Both error terms are O(x^{1/2+ε}), by absolute convergence of Σ|β(m)|m^{−1/2−ε}.
- Numerically, Σ_{n≤x} b(n)λ(n)/x = 0.398787, 0.400230, 0.400001, 0.400000 at x = 10³, …, 10⁶.

(b) Apply partial summation to A(x) = Σ_{n≤x} b(n)λ(n) with f(x) = x^{−1/2}e^{−Δ² log²x/2}/log x.
- The main term is (2/5)∫f(x)dx = (2/5)∫_{log 2}^∞ e^{u/2 − Δ²u²/2}du/u.
- The exponent peaks at u₀ = 1/(2Δ²) with value 1/(8Δ²). The interval [u₀ − 1/Δ, u₀] lies in [log 2, ∞) exactly when (1/Δ)² − 2/Δ ≥ 2 log 2, that is 1/Δ ≥ 1 + √(1 + 2 log 2) = 2.5448, or Δ ≤ 0.3930. For such Δ the exponent on this interval is at least 1/(8Δ²) − ½, and 1/u ≥ 1/u₀ = 2Δ². So the integral is at least (1/Δ)·2Δ²·e^{1/(8Δ²) − 1/2}, and with the factor 2/5 the main term is at least (4/5)Δe^{1/(8Δ²) − 1/2}. At Δ = ½ the interval starts at u = 0, so the argument does not apply as written; the main term there is 1.148 by quadrature.
- The remainder is −∫R f′dx with R(x) = O(x^{1/2+ε}) and |f′(x)| ≪ x^{−3/2}(1 + Δ² log x)e^{−Δ² log²x/2}/log x. Taking ε = ¼, it is O(∫e^{u/4 − Δ²u²/2}(1 + Δ²u)du/u) = O(e^{1/(32Δ²)}/Δ), which is o(main term).
- Numerically (n ≤ 10⁶): V(0.5) = 1.47, V(0.35) = 2.42, V(0.3) = 3.22. The main terms, by quadrature, are 1.148, 2.097 and 2.906. The proved lower bound gives 0.471 and 0.584 at Δ = 0.35 and 0.3. The referee's sieve to 10⁷ gives V = 1.4700, 2.4204, 3.2280.

(c) Σ_{n≤x} b(n)λ(n)n^{−iτ} has main term (2/5)x^{1−iτ}/(1 − iτ). Its Dirichlet series is ζ(s+iτ)B(s+iτ), with a pole at s = 1 − iτ and residue B(1).
- Partial summation gives the main term (2/5)∫e^{u(½ − iτ) − Δ²u²/2}du/u.
- Completing the square, the exponent's maximum is (½ − iτ)²/(2Δ²) = 1/(8Δ²) − iπ/2 − π²Δ²/2 at τ = πΔ². So the main term is (2/5)·(−i)·2√(2π)Δe^{1/(8Δ²)}(1 + O(Δ)), whose imaginary part tends to −∞.
- Numerically (n ≤ 10⁶): Im V_τ = −0.90, −1.47, −2.01 at Δ = 0.5, 0.35, 0.3.

(d) The numbers log p are linearly independent over ℚ.
- By Kronecker's theorem, for any finite set of primes and any target unimodular values, there are arbitrarily large T with (p^{−iT}) as close as desired to the targets.
- Since Σ|c_n| < ∞, truncating 𝒟_Δ to n ≤ N changes it uniformly by at most ε. So its values on [T₀, ∞) come within 2ε of Σc_nχ(n), for every completely multiplicative χ with |χ(p)| = 1.
- Take χ = λ, that is χ(p) = −1, which gives V(Δ) (real, since the c_n are real). Take χ(p) = −p^{−iτ}, which gives V_τ(Δ). ∎

*Illustration, not a proof step:* with Δ = 0.5 and the first 400 terms, the maximum of Re 𝒟_Δ over a grid of T ≤ 2·10⁵ is 1.25, against V = 1.46. The supremum is approached only at much larger T, as expected for simultaneous approximation of many prime phases.

## 4. Part 1

**Lemma 20.5 (Theorem A's sum as a Stieltjes integral).** Assume (H). Fix Δ > 0 and T₁ ≥ 10Δ, and let T ≥ T₁. Let P be Re, Im or the identity, and suppose that ∫_Y^{2Y}|PS(u)|du = O(Y^B) for some B as Y → ∞. Then

  P Σ_ρ Res(FH) = −∫_0^∞ PS(u)h′(u)du + R_T,

where Σ_ρ is Theorem A's limit over its heights T_k, and |R_T| is bounded independently of T.

**Proof.**

1. **Exceptional zeros.** Let ρ = β + iγ be one of the finitely many zeros that are multiple or off the line.
   - The point z = −i(ρ − ½) = γ − i(β − ½) has |Im z| < ½.
   - For |Im w| ≤ 1, |h(w)| ≤ ∫_{T₁}^T|g_Δ(w − v)|dv ≤ e^{1/(2Δ²)}, because |g_Δ(x + iy)| = g_Δ(x)e^{y²/(2Δ²)}. By Cauchy's estimate on the disc of radius ½ about z, |h^{(j)}(z)| ≤ j!·2^j·e^{1/(2Δ²)}.
   - Res_ρ(FH) is a finite combination of the Laurent coefficients of F at ρ and of these derivatives, so it is bounded independently of T. The same holds for the term Res_ρF·h(γ) that ρ contributes to the Stieltjes integral, and for ρ̄.
   - So the exceptional zeros change both sides by amounts bounded independently of T. Every other zero is simple and of the form ρ = ½ + iγ, and for it Res_ρ(FH) = c₁(ρ)h(γ), since H(½ + iγ) = h(γ).
2. **The heights T_k.** Theorem A takes its limit over heights T_k ∈ [k, k+1] with |ζ(σ ± iT_k)|^{−1} ≪ T_k^A for −2 ≤ σ ≤ 2 (`02_` §4.1; their existence is Titchmarsh's §9.7, re-derived by the copy). At these heights S(T_k) = O(T_k^{A′}) for some A′.
   - By the residue theorem, S(T_k) = (2πi)^{−1}∮F(s)ds over the boundary of the rectangle [−1, 2] × [1, T_k]. The rectangle contains exactly the zeros with 0 < γ ≤ T_k, since γ₁ > 14, and F has no other poles there.
   - On Re s = 2, |F(s)| ≤ |s|ζ(3)ζ(2)/ζ(4).
   - On Re s = −1, |1/ζ(−1 + it)| ≤ 4π²ζ(2)(1 + |t|)^{−3/2} (GZR2, used in `19_`), and ζ grows at most polynomially in vertical strips away from s = 1 (Titchmarsh, 2nd ed., ch. V).
   - On the top edge, the factor 1/ζ is ≪ T_k^A.
   - So F is polynomially bounded on all four edges.
3. **Positive heights.** Since h is real, partial summation over 0 < γ ≤ T_k gives
   Σ_{0<γ≤T_k} P(Res_ρF)h(γ) = PS(T_k)h(T_k) − ∫_0^{T_k}PS(u)h′(u)du.
   - For T_k ≥ T, 0 ≤ h(T_k) ≤ ½e^{−(T_k − T)²/(2Δ²)}, so by step 2 the boundary term tends to 0.
   - For u ≥ 2T, |h′(u)| = |g_Δ(u − T₁) − g_Δ(u − T)| ≤ g_Δ(u/2). By the hypothesis, the dyadic pieces ∫_{2^jT}^{2^{j+1}T}|PS||h′| are O((2^jT)^B·g_Δ(2^{j−1}T)), which is summable over j.
   - So the integral converges absolutely, and ∫_0^{T_k} → ∫_0^∞.
4. **Negative heights.** The zeros with −T_k ≤ γ < 0 are the conjugates ρ̄, with Res_{ρ̄}F = conj Res_ρF and H(ρ̄) = h(−γ).
   - Write ε = +1 for P = Re and ε = −1 for P = Im, so that P(conj w) = εP(w). Partial summation gives ε[PS(T_k)h(−T_k) + ∫_0^{T_k}PS(u)h′(−u)du].
   - For u ≥ 0, |h′(−u)| = |g_Δ(u + T₁) − g_Δ(u + T)| ≤ g_Δ(u + T₁), and 0 ≤ h(−T_k) ≤ ½e^{−(T_k + T₁)²/(2Δ²)}.
   - So this part is at most ∫_0^∞|PS(u)|g_Δ(u + T₁)du + o(1) in absolute value. That integral is finite by the hypothesis and does not depend on T.
   - For P the identity, the same holds with conj S in place of εPS. ∎

**Theorem 20.3.** Under (H), lim sup_{T→∞}|Re E(T)|/T = +∞, and likewise for Im E.

**Proof.**

1. **Setup.** Suppose instead that |Re E(u)| ≤ Ku + C for all u > 0. Fix Δ > 0 and T₁ ≥ 10Δ.
   - Then |Re S(u)| ≤ (K + 1/(4π))u + C, so Lemma 20.5 applies with P = Re: Re Σ_ρ Res(FH) = −∫_0^∞Re S·h′du + O(1).
   - Here and below, O(1) is bounded independently of T. It may depend on Δ, T₁, K and C.
2. **The drift.** Split Re S = Re M + Re E on (0, ∞).
   - Re M(u) = u/(4π) vanishes at u = 0, and Re M·h → 0 as u → ∞. So −∫_0^∞Re M·h′du = (1/4π)∫_0^∞h du = (T − T₁)/(4π) − (1/4π)∫_{−∞}^0h du.
   - The correction is small: 0 ≤ ∫_{−∞}^0h du = ∫_{T₁}^TΦ(−v/Δ)dv ≤ Δ∫_{T₁/Δ}^∞Φ(−x)dx ≤ Δe^{−T₁²/(2Δ²)}/√(2π). Here Φ is the standard normal distribution function, and ∫_a^∞Φ(−x)dx = φ(a) − aΦ(−a) ≤ φ(a).
3. **The fluctuation.** h′(u) = g_Δ(u − T₁) − g_Δ(u − T). For a ≥ 0 and Z standard normal, ∫_0^∞u·g_Δ(u − a)du = E(a + ΔZ)⁺ ≤ a + Δ/√(2π). So
   |∫_0^∞Re E·h′du| ≤ ∫_0^∞(Ku + C)(g_Δ(u − T₁) + g_Δ(u − T))du ≤ K(T + T₁) + 2KΔ/√(2π) + 2C.
4. Hence |Re Σ − (T − T₁)/(4π)| ≤ K(T + T₁) + O(1).
5. **Comparison with Proposition 20.1.** Proposition 20.1 gives Re Σ = (T − T₁)/(4π) − (T/2π)Re 𝒟_Δ(T) + O_{Δ,T₁}(1). Hence (T/2π)|Re 𝒟_Δ(T)| ≤ K(T + T₁) + O(1), and so lim sup_{T→∞}|Re 𝒟_Δ(T)| ≤ 2πK.
6. **Almost periodicity.** 𝒟_Δ is uniformly almost periodic, being an absolutely convergent series of characters n^{−iT}. So a bound valid for T ≥ T₀ + 1 holds, up to ε, at every real T: each T has almost periods τ arbitrarily far out with |𝒟(T + τ) − 𝒟(T)| < ε.
7. **Contradiction.** Hence sup_T Re 𝒟_Δ(T) ≤ 2πK for every Δ > 0. Lemma 20.2(b, d) gives sup_T Re 𝒟_Δ ≥ V(Δ) → ∞ as Δ → 0. So K would have to be infinite.
8. **The imaginary part.** Suppose instead that |Im E(u)| ≤ Ku + C.
   - Then |Im S(u)| ≤ u²/(4π) + (K + 1)u + C, and Lemma 20.5 applies with P = Im.
   - Im M(u) = u²/(4π) − u vanishes at 0, and −∫_0^∞Im M·h′du = ∫_0^∞(u/(2π) − 1)h du = (T² − T₁²)/(4π) − (T − T₁) + O(1). This uses ∫_ℝh = T − T₁ and ∫_ℝuh = (T² − T₁²)/2 (§2); the part u ≤ 0 is O(1) as in step 2.
   - The rest is the same, using Lemma 20.2(c, d): inf Im 𝒟_Δ → −∞. ∎

**Where (H) is used.** Only in Lemma 20.5, to identify Theorem A's weights H(ρ) with the sharp weights h(γ) and each residue with c₁(ρ), up to finitely many exceptions. At an off-line zero, H(ρ) = h(γ − i(β − ½)) is not a function of γ alone. At a multiple zero, the residue involves derivatives of H. (Compare `03_` §4, which gives the same reasons.)

## 5. Part 2

**Theorem 20.4.** Under (H), lim sup_{X→∞} X^{−3}∫_X^{2X}|E(T)|²dT ≥ (7/(12π²))Σ_{n≥2} b(n)²/(n log²n).

**Proof.**

1. **Setup.** Let L be the lim sup, and assume L < ∞.
2. **Smoothing.** L < ∞ gives ∫_Y^{2Y}|E|² ≤ CY³ for all large Y. By Cauchy–Schwarz, ∫_Y^{2Y}|S| ≤ ∫_Y^{2Y}|M| + (Y∫_Y^{2Y}|E|²)^{1/2} = O(Y³). So Lemma 20.5 applies with P the identity.
   - Extend S, M and E by 0 to u ≤ 0, and write S₊, M₊ and E₊. Since h′(u) = g_Δ(u − T₁) − g_Δ(u − T) and g_Δ is even, −∫_0^∞S·h′du = (S₊ ∗ g_Δ)(T) − (S₊ ∗ g_Δ)(T₁). So Σ Res(FH) = (S₊ ∗ g_Δ)(T) + O(1).
   - M is a quadratic polynomial with leading coefficient i/(4π), so (M ∗ g_Δ)(T) = M(T) + iΔ²/(4π). Removing the part u ≤ 0 changes this by at most ∫_{−∞}^0|M(u)|g_Δ(T − u)du = O(1). So (M₊ ∗ g_Δ)(T) = M(T) + O(1).
   - So by Proposition 20.1, (E₊ ∗ g_Δ)(T) = −(T/2π)𝒟_Δ(T) + O_{Δ,T₁}(1).
3. **Upper bound, with the window chosen to avoid edge effects.**
   - As in step 2, ∫_Y^{2Y}|E|² ≤ CY³ for all large Y.
   - By Jensen's inequality for the probability density g_Δ, |E₊ ∗ g_Δ|² ≤ |E₊|² ∗ g_Δ. So ∫_X^{2X}|E₊ ∗ g_Δ|² ≤ ∫|E₊(w)|²φ_X(w)dw, where φ_X = 1_{[X,2X]} ∗ g_Δ ≤ 1.
   - Put R = Δ√(8 log X). Outside [X − R, 2X + R], φ_X ≤ X^{−4}. Together with the polynomial bound on ∫|E|², the outside contributes o(1).
   - The inside contributes ∫_X^{2X}|E|² plus two edge pieces over intervals of length R, at X and at 2X.
   - The edge pieces are small on average over the starting point. By Fubini, ∫_Y^{2Y}(∫_{X−R}^X|E|²)dX ≤ R∫_{Y−R}^{2Y}|E|² = O(RY³), and likewise at 2X. So the average edge piece over X ∈ [Y, 2Y] is O(Y² √log Y) = o(Y³).
   - Hence, for every large Y, there is X ∈ [Y, 2Y] with ∫_X^{2X}|E₊ ∗ g_Δ|² ≤ ∫_X^{2X}|E|² + o(X³) ≤ (L + o(1))X³.
4. **Lower bound.** ∫_X^{2X}(T²/4π²)|𝒟_Δ(T)|²dT = (7X³/(12π²))Σ_n|c_n|²(1 + o(1)).
   - The mean of |𝒟_Δ|² over [a, a+Y] tends to Σ|c_n|² uniformly in a, as Y → ∞. This is Parseval for absolutely convergent series with distinct frequencies log n.
   - Also ∫_X^{2X}T²dT = 7X³/3.
5. **Conclusion.**
   - By step 2, |E₊ ∗ g_Δ|² and (T²/4π²)|𝒟_Δ|² differ by O(T|𝒟_Δ| + 1). Integrated over [X, 2X], the difference is O(X²), which is o(X³).
   - Evaluating steps 3 and 4 at the X chosen in step 3 therefore gives L ≥ (7/(12π²))Σ_n b(n)²e^{−Δ² log²n}/(n log²n) for every Δ > 0. As Δ ↓ 0 the sum increases to Σ b(n)²/(n log²n), by monotone convergence. ∎

**The constant.**
- Σ_{2≤n≤10⁶} b(n)²/(n log²n) = 0.6064.
- The tail is estimated from the mean of b(n)², which is 0.345 up to 10⁶: Σ_{n>10⁶} ≈ 0.345/log 10⁶ = 0.025.
- The total is ≈ 0.631, and (7/(12π²))·0.631 = 0.0373.
- This agrees with the copy's 0.6100 up to 10⁷, plus about 0.021.

## 6. Verdict and scope

- **Parts 1–3 hold as stated, given Theorem A.** Part 3 is unconditional; parts 1–2 assume (H). The proofs follow the copy's route (`02_` §4.3) and supply the four steps listed at the top, so they are complete relative to Theorem A. The numerical checks use my own code. The referee's sieve, which builds b(n) by Dirichlet convolution rather than from the product formula, reproduces the constants.
- **Status of the input.** Theorem A is taken as proved by the copy, and it has been checked numerically by me and by the copy on several windows. Its proof (contour shift at good heights) was not re-derived line by line here, beyond the structure of its right-hand side (`02_`).
- **What Theorem C does not say.**
  - It is unsigned: separate one-sided statements, lim sup Re E/T = +∞ and lim inf Re E/T = −∞, are not proved. `03_` §6 records this as open.
  - It gives no information on the location of zeros; (H) is a hypothesis.
  - The sharp Bohr coefficients −b(n)/(2π√n log n) additionally require the existence of Bohr means (`03_` §4).

## 7. Items for the goals

- **Negative result (goal 1).** Under (H), the sharp velocity laws Σ_{γ≤T}Re c₁ = T/(4π) + O(T), and the vertical law with error O(T), are false. Their errors are unbounded multiples of T. Proved here in full along the copy's route, relative to Theorem A (Theorems 20.3–20.4).
- **Bridge (goal 2).** The owner's Hurwitz shift ζ(s, 1+t) moves each zero with velocity ρζ(ρ+1)/ζ′(ρ) (`17_` §1). Summed over zeros, the motion is a drift M(T) plus an oscillation whose Bohr spectrum is carried by all integers n, with frequencies log n and amplitudes b(n) = n^{−1}∏_{p|n}(1 − p). Twisting by the Liouville function λ makes every squarefree term positive: for squarefree n with k prime factors, b(n) and λ(n) both have sign (−1)^k. The terms with n not squarefree keep mixed signs (b(4)λ(4) = −¼), and the proof uses only the positive mean 2/5 of the twisted partial sums (Lemma 20.2(a)).
- **Lemma (goal 3).** Lemma 20.2(a): Σ b(n)λ(n)n^{−s} = ζ(s)ζ(2s+2)/(ζ(2s)ζ(s+1)), so Σ_{n≤x} b(n)λ(n) ∼ (2/5)x. This is elementary and classical in type; no source was searched.

## 8. Checks

`checks/theorem_c_reproof_checks.py`, output in `checks/theorem_c_reproof_checks_OUTPUT.txt`:
- the Euler factors and B(1) = 2/5 (sympy);
- Σ b(n)λ(n)/x → 0.400000;
- V(Δ) and V_τ(Δ) at Δ = 0.5, 0.35, 0.3;
- the T-linear coefficient of ĥ₁ (sympy);
- the constant 0.0373;
- the Kronecker illustration;
- (7) the threshold Δ ≤ 0.3930 of Lemma 20.2(b) and the main terms by quadrature;
- (8) the Gaussian-window bounds of §2 and §4 (|h(i/2)|, ∫_{−∞}^0h and E(a + ΔZ)⁺) at sample parameters.

`checks/referee_theorem_c_independent_checks.py` (sixth referee pass, output in `checks/referee_theorem_c_independent_checks_OUTPUT.txt`):
- b(n) built by Dirichlet convolution and checked against the product formula;
- the partial sums of b(n)λ(n) to 10⁷, V(Δ) and V_τ(Δ) to 10⁷, and the constant 0.03732 with the mean of b(n)² from its Euler product.

## 9. Revision after the sixth referee pass (09:32 UTC)

1. **Attribution.** The first version said that the proof was written from the statements alone. It follows the copy's route, with the same choices in Lemma U. The introduction and §6 now say so, and list what is added.
2. **Lemma 20.5 (new).** Theorem 20.3's integration by parts and Theorem 20.4's smoothing step now rest on it. The first version bounded the zeros below the real axis only by the size of each weight (O(e^{−T₁²/(2Δ²)})), which does not control a sum over infinitely many zeros; partial summation replaces it. Theorem 20.4 had no justification of the integration by parts under its mean-square hypothesis; the good-height bound S(T_k) = O(T_k^{A′}) and dyadic Cauchy–Schwarz now supply it.
3. **Lemma 20.2(b).** The interval bound needs Δ ≤ 0.3930, not Δ ≤ ½. At Δ = ½ the interval leaves [log 2, ∞). The statement is about Δ → 0⁺, so the restriction costs nothing.
4. **Proposition 20.1.** The bounds for ∫sech(πu)h(u)du and h(i/2) are now explicit and uniform in T. The first version's O(e^{−cT₁}) was not uniform in Δ for h(i/2).
5. **Theorem 20.3.** In step 2 "exactly" is replaced by the explicit correction Δe^{−T₁²/(2Δ²)}/√(2π), coming from the part u ≤ 0. Step 3's bound is explicit.
6. **§7.** λ makes the squarefree terms positive, not all terms.
7. **§7, goal 1.** "Independently confirmed" is replaced by "proved here in full along the copy's route, relative to Theorem A".
