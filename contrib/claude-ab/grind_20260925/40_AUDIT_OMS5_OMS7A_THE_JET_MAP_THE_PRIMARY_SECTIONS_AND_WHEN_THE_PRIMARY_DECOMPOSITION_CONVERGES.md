# OMS5–OMS7A: the jet map, the primary sections and the return to the adelic complex are correct, and the primary decomposition converges exactly when the principal parts of 1/ζ at the zeros are polynomially bounded

Claude (claude-ab lane), model `claude-opus-5-5` (Opus 5.5) at maximum reasoning effort. 25 September 2026, written at 20:58 UTC. Board task 8: the last unread part of OMS (`26_` audited OMS0–OMS4 and OMS8). I read OMS5–OMS7A and the passages of AC and CW they use myself, without a subagent. Refereed in the seventeenth pass (report completed at 21:41 UTC) and revised at 21:49 UTC; §9 lists the changes.

## 0. Source, method and checks

- **Sources.** In the reader repository, the folder of `39_` at commit 36a82ec:
  - `ORIGINAL_MELLIN_SPECTRAL_SYNTHESIS.md` (OMS), 535 lines, SHA-256 prefix `043c11306320f6d5`. Audited here: OMS5–OMS7A, lines 302–523.
  - For OMS7A: `ACTUAL_ADELIC_COMPLEX_INDEPENDENT.md` (AC), AC1–AC4, lines 15–226 (SHA-256 prefix `24ec331549dd0b1f`).
  - For OMS7: `CC_W_MELLIN_INDEPENDENT.md` (CW), CW1 and CW7, lines 26–86 and 276–291 (SHA-256 prefix `0b8f54d49dbf6eb6`).
- **Method.** Every statement of OMS5–OMS7A was re-derived. Its analytic input is OMS3.14, the exact summation image ℰS = ℳ^{−1}I_ζ (Meyer's range theorem with the division estimate supplied), which `26_` audited. The formulas were also checked numerically at the first zeros where that is meaningful.
- **Checks.** `checks/oms5_7a_checks.py`, 35 items, all pass (runtime about 45 s; revised after the referee pass, §9):
  - A1–A4: OMS6.1, OMS6.4 and OMS6.5;
  - B1–B3: CW1.3, CW1.5 and OMS7.1;
  - C1–C6: the functor G_L of OMS7.2–7.3 and CW7 on the four-element Boolean lattice;
  - D1: Lemma 40.1 (OMS5.6 with the constant 2^{r+M});
  - E1–E8: AC1.4, AC2.9 and AC2.12 (E3 on the Mellin side), and OMS2.3/2.5;
  - F1–F9 and F2a: the inputs of Proposition 40.4, with two illustrations;
  - G1–G3: the interpolants of Proposition 40.5 at a triple zero of a model function.

**Verdict.**
- **No errors.** OMS5–OMS7A are correct. They are linear algebra and topology on top of OMS3.14.
- **Four remarks**, none a defect of OMS and none affecting a result:
  - OMS5.6 leaves its constant implicit; C_{r,M} = 2^{r+M} works (Lemma 40.1).
  - OMS5 takes the unboundedness of the zero heights from CW3. CW3 cites an explicit Riemann–von Mangoldt bound (Hasanalizade–Shen–Wong, arXiv:2107.06506, Corollary 1.2); PGD4 gives an independent proof.
  - OMS7.2 displays the scalar action (c, ν)(v, λ) = (cv, ν ∧ λ) without a quantifier, as the "already specified" action of CW7's receiver. CW7 takes (c, ν) ∈ G_L(ℂ) (CW line 282), i.e. c = 0 whenever ν is not the top element. For these scalars the action preserves G_L(V) (checks C1, C3); for c ≠ 0 and ν ≠ 1_L it would not (check C5). G_L(V) is a commutative monoid, a semimodule over G_L(ℂ) as CW7 calls it, not a vector space (check C6).
  - OMS7A's formality statement and the vanishing of its particular two-extension class rest on the equivariance of AC2's section s_I. AC2.12 proves it, and I checked the proof (§4).
- **New here, as far as a search of the programme and of the literature found (§7): Propositions 40.4 and 40.5.**
  - For simple zeros, the primary decomposition Σ_ρ Π_ρ of the zeta quotient converges for every class iff |ζ′(ρ)| ≥ c(1 + |Im ρ|)^{−K}.
  - For arbitrary multiplicities it converges iff the coefficients of the principal parts of 1/ζ at the zeros are polynomially bounded. Proposition 40.5 is the seventeenth referee's sharpening of Proposition 40.4, and I checked its proof.
  - The programme does not assert this convergence (OMS6; GEX2 avoids projectors altogether). The propositions show that it cannot do so without new input about ζ at its zeros.
  - They are an instance, for Meyer's quotient, of the classical link between derivative lower bounds at the zeros and interpolation or representing systems (§7).

## 1. OMS5: the jet map and its image

**Setting** (OMS1–OMS3, audited in `26_`):
- ℬ is the Fréchet space of entire F with b_{A,M}(F) = sup_{|σ|≤A, t∈ℝ}(1 + |t|)^M|F(σ + it)| finite.
- I_ζ ⊂ ℬ is the closed ideal of functions vanishing to full order m_ρ at every nontrivial zero ρ.
- Q = 𝒜/ℰS ≅ ℬ/I_ζ, by OMS3.14 and the Mellin isomorphism ℳ.
- A_ρ = ℂ[T]/(T^{m_ρ}), j_ρ[k] = F_k(ρ + T) mod T^{m_ρ}, and J = (j_ρ)_ρ: Q → ∏_ρ A_ρ.

**What OMS5 proves, and my verification.**
- **ker J = 0 (OMS5.2).** If every full jet of F_k vanishes, then F_k ∈ I_ζ = ℳℰS by OMS3.14, so [k] = 0. This is where the whole analytic content enters.
- **The image and its topology (OMS5.3–5.5).** The image is 𝒥 = {(F(ρ + T) mod T^{m_ρ})_ρ : F ∈ ℬ}, and Q → ℬ/I_ζ → 𝒥 are isomorphisms when 𝒥 carries the quotient seminorms b̄_{A,M}. The seminorms b_{A,M} increase in A and M, so they form a directed family, and the quotient of a Fréchet space by a closed subspace is Fréchet (Rudin, *Functional Analysis*, 2nd ed., Theorem 1.41(d)).
- **Jet decay (OMS5.6).** Lemma 40.1 below.
- **𝒥 is a proper dense subspace of the product.**
  - Every finitely supported tuple is realized by a finite sum of OMS6's sections, so 𝒥 is dense in the product topology.
  - The constant tuple 1 is not in 𝒥: by Lemma 40.1 with r = 0 and M = 1, a function with F(ρ) = 1 at every zero would satisfy 1 + |γ| ≤ 2b_{2,1}(F) for all zero heights γ, which are unbounded.
- **The quotient topology is strictly finer than the product topology.** Each j_ρ is continuous and vanishes on I_ζ, so the quotient topology is at least as fine. If the two were equal, 𝒥 would be complete in the subspace topology and hence closed in the Hausdorff product. Being dense, it would then be the whole product, contradicting properness.
- **Observation-preserving quotients.** If every j_ρ factors through a linear surjection π: Q → V, then ker π ⊂ ker J = 0.

**Lemma 40.1 (jet decay with an explicit constant).** For F ∈ ℬ, a nontrivial zero ρ = β + iγ and r, M ≥ 0,

  (1 + |γ|)^M |F^{(r)}(ρ)/r!| ≤ 2^{r+M} b_{2,M}(F).

*Proof.* Cauchy's formula on |z − ρ| = ½ gives |F^{(r)}(ρ)/r!| ≤ 2^r max_{|z−ρ|=½}|F(z)|. The circle lies in −½ < Re z < 3/2, because 0 < β < 1. On it 1 + |Im z| ≥ 1 + |γ| − ½ ≥ (1 + |γ|)/2, so |F(z)| ≤ b_{2,M}(F)(1 + |Im z|)^{−M} ≤ 2^M b_{2,M}(F)(1 + |γ|)^{−M}. ∎ (Check D1: F = exp(s²/100), r, M ≤ 2, the first ten zeros; the largest ratio of the two sides is 0.20.)

## 2. OMS6: the primary sections

OMS6 enters the RZ5–RZ8 construction into OMS5; it does not claim it as new. Fix ρ with m = m_ρ.
- **The section.** U_ρ = F_*/(s − ρ)^m lies in ℬ and has U_ρ(ρ) = u_0 ≠ 0, where F_*(s) = s(s − 1)π^{−s/2}Γ(s/2)ζ(s)/8 (OMS2.3).
  - The recursion OMS6.1 produces c_ρ(T) = u(T)^{−1} mod T^m: the T^n-coefficient of u·c is u_0c_n + Σ_{r=1}^{n} u_r c_{n−r} = 0 for 1 ≤ n < m, and u_0c_0 = 1 (check A1).
  - Hence ℛ_ρ(P) = U_ρ·[P c_ρ]_{<m}(s − ρ) has full jet P at ρ. At every other zero η, U_ρ vanishes to order m_η.
  - So j_η s_ρ = δ_{ηρ}·id, Π_ρ = s_ρ j_ρ are commuting idempotents with Π_ρΠ_η = 0 for ρ ≠ η, and finite sums of sections realize every finitely supported jet tuple.
- **OMS6.4.** The u_r are Cauchy products of the Taylor coefficients of C(s) = s(s − 1)π^{−s/2}Γ(s/2)/8 and of ζ(s)/(s − ρ)^m. The formula for C^{(h)} is Leibniz's rule for three factors, with a ≤ 2 because s(s − 1) is quadratic (checks A2–A3 at the first zero, to 12 digits or better).
- **OMS6.5.** F_{W_ak}(s) = a^sF_k(s) (substitute u = av), so j_ρW_a is multiplication by a^{ρ+T} = a^ρ exp((log a)T) (check A4).
  - Both sides of OMS6.5 have the same jets at every zero, so they are equal in Q by OMS5.2.
  - Write L_Q for the generator of the dilations (GEX1.3–1.4: F_{L_Qk}(s) = sF_k(s), so j_ρL_Q is multiplication by ρ + T). Then s_ρ(A_ρ) is an m_ρ-dimensional W_a-invariant subspace. On it W_a = a^ρ exp((log a)N_ρ), where N_ρ = L_Q − ρ is multiplication by T, nilpotent of order exactly m_ρ.
  - The test representatives need not be equivariant; their covariance error lies in ℳ^{−1}I_ζ = ℰS.
- **No infinite sum.** OMS6 asserts no convergence of Σ_ρ Π_ρ. Propositions 40.4 and 40.5 show what such convergence would require.

## 3. OMS7: CW's Gaussian map and the support labels

- **CW1.** b(u) = exp(−(log u)²) has Mellin transform B(s) = √π exp((s − ½)²/4) (CW1.3, check B1). For x > 1, K_b[x] = W_{log x}b, i.e. K_b[x](u) = (log x)^{1/2}exp(−(log u − log log x)²), so F_{K_b[x]}(s) = B(s)(log x)^s (CW1.5, check B2).
- **OMS7.1.** Hence j_ρK̄_b[x] = B(ρ + T)(log x)^ρ exp(T log log x) mod T^{m_ρ}, where B(ρ + T) = √π e^{(ρ−½)²/4}e^{(ρ−½)T/2 + T²/4} (expand (ρ − ½ + T)²/4; check B3 to order 4). By OMS5.2, equality of these joint observations is equality in Q.
- **OMS7.2–7.3 and CW7.** G_L(V) = {(0, λ) : λ ∈ L} ∪ {(v, 1_L) : v ∈ V}, with (v, λ) + (w, μ) = (v + w, λ ∨ μ) and scalars (c, ν) ∈ G_L(ℂ) acting by (cv, ν ∧ λ).
  - G_L(f)(v, λ) = (f(v), λ) is well defined, because a non-top label forces v = 0.
  - It preserves the addition and the action of G_L(ℂ), and G_L(g∘f) = G_L(g)∘G_L(f) (checks C1–C4). So G_L carries the isomorphisms of OMS5.4 to isomorphisms G_L(Q) ≅ G_L(𝒥), with every labelled zero (0, λ) kept.
  - The restriction of the scalars to G_L(ℂ), which CW7 states, is needed: a scalar with c ≠ 0 and ν ≠ 1_L would leave G_L(V) (check C5).
  - G_L(V) is a commutative monoid, in which (0, λ) has no inverse for λ ≠ 0_L (check C6). OMS7.2 says these operations are "not operations on primitive tau", and they are not ring or vector-space operations either.
- The remark that 0 ⊗ e_λ = 0 in an ordinary tensor product, so tensoring would erase the labels, is correct.

## 4. OMS7A: the adelic periodization complex

AC's objects (AC1–AC2):
- G = ℚ_{>0}^×, R = ℂ[G] and H = 𝒮_even(ℝ), with m(h) = (h(0), ∫h). Then H_00 = ker m = S, M_0 = ker(ε ⊗ m) and Q_0 = M_0/I_RM_0.
- Φ[Σ t_a ⊗ h_a] = Σ h_a and β[Σ t_a ⊗ h_a] = Σ_p ℓ_p ⊗ Σ_a v_p(a)m(h_a) ∈ ℬ_pr = (⊕_p ℂℓ_p) ⊗ ℂ².
- J = 2ℰΦ.

What I checked:
- **The split (AC1.4, AC2.7–2.11).** (h, Σ ℓ_p ⊗ u_p) ↦ [t_1 ⊗ h] + Σ_p[(t_p − 1) ⊗ σ(u_p)] inverts (Φ, β). It uses m(h_0) = (1, 0) and m(h_1) = (0, 1) (check E1) and [t_a − 1] = Σ_p v_p(a)[t_p − 1] in I_R/I_R².
  - Hence 0 → ℬ_pr → Q_0 → I_0 → 0 is exact, with the section s_I(k) = [t_1 ⊗ h_k].
  - Here h_k = ½f_{F_k} in OMS3's notation. By OMS3.9, f_F is the inverse of the plain Mellin transform ∫f(v)v^s dv/v of F/ζ on Re s > 1, so ∫h_k(v)v^s dv/v = F_k(s)/(2ζ(s)) there. The Möbius form is AC2.9 (check E4).
- **Equivariance (AC1.5, AC2.12).**
  - J𝓡_b = W_bJ by substitution, where 𝓡_b acts on Q_0 through h ↦ h(·/b). Check E3 compares the Mellin transforms of both sides, computed independently, for c = [t_1 ⊗ f_*].
  - 𝓡_b preserves H_00, and ℰ is injective on H_00 (OMS3.14). So h_{W_bk} = h_k(·/b), i.e. 𝓡_b s_I = s_I W_b.
  - β intertwines the action with id ⊗ diag(1, b) (AC1.5).
- **OMS7A.1–7A.2.** I_0 = J(Q_0) = 2ℰ(H_00) = ℰS as subspaces, since Φ is onto H_00 (Φ[t_1 ⊗ h] = h). ℰS is closed (OMS3.14).
  - Hence AC4's closure difference D_cl = Ī_0/I_0, which AC4 left open, is 0, and C_alg = Q with the same quotient topology.
- **OMS7A.3–7A.4.**
  - For C = [Q_0 → 𝒜] in degrees −1 and 0: H^{−1}(C) = ker J = ker Φ ≅ ℬ_pr and H⁰(C) = 𝒜/I_0 = Q.
  - The cochain map (β, quotient): C → ℬ_pr[1] ⊕ Q[0] is an equivariant quasi-isomorphism. So the complex is formal in the algebraic representation category.
  - The particular two-extension 0 → ℬ_pr → Q_0 → 𝒜 → Q → 0 is the Yoneda splice of the equivariantly split sequence (AC2.7) with 0 → I_0 → 𝒜 → Q → 0, so its class is zero.
  - OMS7A says correctly that this does not make the whole group Ext²(Q, ℬ_pr) vanish. GEX7 proves that separately, in GEX's categories (`39_` §3).

## 5. Propositions 40.4 and 40.5: when the primary decomposition converges

Let Λ be the Fréchet space of tuples (P_ρ) ∈ ℂ^𝒵 over the distinct nontrivial zeros with p_M(P) = sup_ρ (1 + |γ_ρ|)^M|P_ρ| < ∞ for all real M ≥ 0. Two classical inputs are used: Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2nd ed. (revised by Heath-Brown), Theorems 9.2 and 9.6(A). They are also standard in Davenport, *Multiplicative Number Theory*, Ch. 15 ("The Number N(T)"), which I did not re-check.
- (D1) The number of zeros, with multiplicity, with |γ − T| < 1 is O(log T).
- (D2) For −1 ≤ σ ≤ 2 and t ≥ 2, ζ′/ζ(s) = Σ_{|t−γ|<1}(s − ρ)^{−1} + O(log t).

**Lemma 40.2 (good heights).** There are A, T_0 > 0 such that every interval [T, T + 1] with T ≥ T_0 contains some t with |ζ(σ ± it)| ≥ t^{−A} for all −1 ≤ σ ≤ 2. This is Titchmarsh's Theorem 9.7, and the proof below is his.

*Proof.*
- Take t ∈ [T, T + 1] different from every γ, and integrate the real part of (D2) along [σ + it, 2 + it]. With n(t) the number of terms, this gives

  log|ζ(σ + it)| = log|ζ(2 + it)| − Σ_{|t−γ|<1}(log|2 + it − ρ| − log|σ + it − ρ|) + O(log t).

- Here |ζ(2 + it)| ≥ 1/ζ(2), 1 < |2 + it − ρ| < 3 and n(t) = O(log t). Also |σ + it − ρ| ≥ |t − γ|. So log|ζ(σ + it)| ≥ Σ_{|t−γ|<1} log|t − γ| − C log T, uniformly in σ ∈ [−1, 2].
- For t ∈ [T, T + 1] only zeros with T − 1 < γ < T + 2 contribute, and ∫_{−1}^{1} log|u| du = −2. So the mean of Σ_{|t−γ|<1} log|t − γ| over [T, T + 1] is at least −2·#{T − 1 < γ < T + 2} ≥ −C′ log T by (D1).
- Some t, which can be taken different from every γ, is at least the mean. For γ < 0 use |ζ(s̄)| = |ζ(s)|. ∎

Check F5 illustrates the lemma at T = 50, 100, 200: some t has min_σ|ζ(σ + it)| ≈ 1.

**Proposition 40.4.**
- **(i)** Suppose that for every x ∈ Q the set {Π_ρx : ρ a nontrivial zero} is bounded in Q. This holds in particular if, for some enumeration (ρ_n) of the distinct zeros, the partial sums S_nx = Σ_{k≤n} Π_{ρ_k}x converge for every x. The limit is then x. Then there are c, K > 0 with

  |ζ^{(m_ρ)}(ρ)/m_ρ!| ≥ c(1 + |γ|)^{−K} for every nontrivial zero ρ = β + iγ.

- **(ii)** Suppose all nontrivial zeros are simple and |ζ′(ρ)| ≥ c(1 + |γ|)^{−K} for all ρ. Then:
  - J: Q → Λ, x ↦ (x̂(ρ))_ρ with x̂(ρ) = j_ρx ∈ A_ρ = ℂ, is an isomorphism of Fréchet spaces;
  - Σ_ρ Π_ρx = Σ_ρ x̂(ρ)s_ρ(1) converges absolutely to x for every x ∈ Q.
- **(iii)** Hence, if all zeros are simple, the following are equivalent:
  - the boundedness hypothesis of (i);
  - convergence of the partial sums for one enumeration and every x;
  - absolute convergence of Σ_ρ Π_ρx for every x;
  - a bound |ζ′(ρ)| ≥ c(1 + |γ|)^{−K};
  - J: Q ≅ Λ.

*Proof of (i).*
1. **The limit.** Suppose S_nx → y. For each ρ, j_ρS_nx = j_ρx once ρ is among ρ_1, …, ρ_n, so j_ρy = j_ρx by continuity, and y = x by OMS5.2. Convergence of the S_nx makes the Π_{ρ_n}x = S_nx − S_{n−1}x bounded.
2. **Equicontinuity.** Q is Fréchet, and the continuous maps Π_ρ are pointwise bounded. So they are equicontinuous (Banach–Steinhaus; Rudin, *Functional Analysis*, 2nd ed., Theorem 2.6). Since the seminorms b̄_{A,M} are directed, there are A_1, M_1 and C_0 with b̄_{2,0}(Π_ρx) ≤ C_0 b̄_{A_1,M_1}(x) for all ρ and x.
3. **The test classes.**
   - Take x_ρ = [E_ρ] with E_ρ(s) = e^{(s−ρ)²} ∈ ℬ. This is the programme's own Gaussian test vector g_ρ (CFP6.1, `CONTINUOUS_POSITIVE_TRANSFER_FORMS.md`), with the same seminorm bound as CFP7.3. Since |E_ρ(σ + it)| = e^{(σ−β)² − (t−γ)²} and 1 + |t| ≤ (1 + |γ|)(1 + |t − γ|), b_{A_1,M_1}(E_ρ) ≤ C_1(1 + |γ|)^{M_1}.
   - Π_ρx_ρ = s_ρ(e^{T²} mod T^m) has a representative F_ρ with b_{2,0}(F_ρ) ≤ 2C_0C_1(1 + |γ|)^{M_1}.
   - F_ρ has jet e^{T²} mod T^m at ρ; in particular F_ρ(ρ) = 1. It vanishes to full order at every other zero.
4. **The rectangle.**
   - Let |γ| ≥ T_0 + 2 and γ > 0; γ < 0 is symmetric. Choose good heights T_1 ∈ [γ − 2, γ − 1] and T_2 ∈ [γ + 1, γ + 2] (Lemma 40.2), and let R = [−1, 2] × [T_1, T_2].
   - H(s) = F_ρ(s)(s − ρ)^m/ζ(s) is holomorphic on a neighbourhood of R:
     - at the other zeros in R, F_ρ vanishes to full order;
     - at ρ, (s − ρ)^m/ζ(s) → m!/ζ^{(m)}(ρ);
     - ζ has no zeros on ∂R, R contains no trivial zero, and it does not contain the pole at 1.
   - Off a neighbourhood of R, H can have poles at the trivial zeros.
   - By the maximum principle, |m!/ζ^{(m)}(ρ)| = |H(ρ)| ≤ max_{∂R}|H|.
5. **The bound on ∂R.**
   - |F_ρ| ≤ b_{2,0}(F_ρ) and |s − ρ| < 3.
   - |1/ζ| is at most ζ(2) = π²/6 on σ = 2 (check F4) and at most T_2^A on the horizontal sides (Lemma 40.2).
   - On σ = −1 it is at most π⁴/3: |ζ(−1 + it)| = |χ(−1 + it)||ζ(2 − it)| ≥ (2π²)^{−1}·6/π² = 3/π⁴. The first factor comes from |χ(−1 + it)|² = π^{−3}y coth(πy)(¼ + y²) ≥ (4π⁴)^{−1} with y = t/2, i.e. OMS3.6 with N = 0; equality holds at t = 0 (checks F1–F3, F2a).
   - Hence |ζ^{(m)}(ρ)/m!|^{−1} ≤ 2C_0C_1(1 + |γ|)^{M_1}·3^m·max(π²/6, π⁴/3, (γ + 2)^A).
6. **Conclusion.** By (D1), m ≤ C log(2 + |γ|), so 3^m ≤ (2 + |γ|)^{C log 3}. This gives the bound for |γ| ≥ T_0 + 2. The finitely many remaining zeros are absorbed into c, since ζ^{(m_ρ)}(ρ) ≠ 0 by the definition of m_ρ. ∎

*Proof of (ii).*
1. **The interpolating representatives.** For each ρ let G_ρ(s) = e^{(s−ρ)²}(s − 1)ζ(s)/((s − ρ)(ρ − 1)ζ′(ρ)).
   - G_ρ is entire, G_ρ(ρ) = 1 and G_ρ(η) = 0 at every other zero (checks F6–F7).
   - (s − 1)ζ(s) grows at most polynomially in vertical strips: |(s − 1)ζ(s)| ≤ C_A(1 + |t|)^{c_A} for |σ| ≤ A. For σ ≤ −1 use the functional equation, and in between Phragmén–Lindelöf (Titchmarsh, Ch. V).
   - For |s − ρ| ≥ 1 this, the Gaussian factor and |ρ − 1| ≥ |γ| ≥ 1 give |G_ρ(s)|(1 + |t|)^M ≤ C(1 + |γ|)^{M+c_A}(1 + |t − γ|)^{M+c_A}e^{−(t−γ)²}/|ζ′(ρ)|. On |s − ρ| < 1 use the maximum principle.
   - So b_{A,M}(G_ρ) ≤ C_{A,M}(1 + |γ|)^{M+c_{A′}}/|ζ′(ρ)| with A′ = max(A, 2), and under the hypothesis this is at most C′_{A,M}(1 + |γ|)^{M+c_{A′}+K}.
   - Using |ρ − 1| ≥ |γ| lowers the exponent by one. For A = 2 and M = 0 the actual growth of b_{2,0}(G_ρ)|ζ′(ρ)| is about γ^{5/2}, from σ = −2, as the referee found. Check F8's sampled slope 2.6 for 14 ≤ γ ≤ 102 is consistent with this.
2. **The series.** Since N(T) = O(T log T), Σ_ρ(1 + |γ|)^{−2} < ∞; CFP8.1 uses the same summability. So for P ∈ Λ the series F_P = Σ_ρ P_ρG_ρ converges absolutely in ℬ, with b_{A,M}(F_P) ≤ C″ p_{M+c_{A′}+K+2}(P).
3. **The inverse map.** Evaluation at a zero is continuous, so F_P(η) = P_η, i.e. J[F_P] = P. Thus P ↦ [F_P] is a continuous right inverse of J. J is injective (OMS5.2) and continuous into Λ (Lemma 40.1 with r = 0, passing to the infimum over representatives). Hence J is an isomorphism Q ≅ Λ.
4. **Absolute convergence.** x = [F_{Jx}] = Σ_ρ x̂(ρ)[G_ρ], absolutely convergent in Q. Here [G_ρ] = s_ρ(1), because both have jet 1 at ρ and 0 elsewhere, so x̂(ρ)[G_ρ] = Π_ρx. ∎

*Proof of (iii).*
- The bound on |ζ′(ρ)| gives the isomorphism and absolute convergence, by (ii).
- Absolute convergence in a Fréchet space implies convergence in every order, which implies the boundedness hypothesis.
- The boundedness hypothesis gives the bound on |ζ′(ρ)| by (i) with m_ρ = 1.
- The isomorphism gives absolute convergence: Σ_ρ x̂(ρ)δ_ρ converges absolutely in Λ, J^{−1} is continuous, and J^{−1}δ_ρ = s_ρ(1). ∎

**Proposition 40.5 (all multiplicities; the seventeenth referee's sharpening, proof checked).**
- **Notation.** For each zero ρ with m = m_ρ, let c_{ρ,k} (0 ≤ k < m) be the Taylor coefficients at ρ of (s − ρ)^m/ζ(s).
  - Σ_{k<m} c_{ρ,k}(s − ρ)^{k−m} is the principal part of 1/ζ at ρ (check G3), and c_{ρ,0} = m!/ζ^{(m)}(ρ). These are the reciprocal coefficients of GZR4.2.
  - Let Λ_m be the space of tuples (P_ρ) ∈ ∏A_ρ with sup_ρ (1 + |γ|)^M‖P_ρ‖ < ∞ for all M, where ‖·‖ is the largest coefficient.
- **Statement.** The following are equivalent:
  - (a) the partial sums S_nx converge for every x, for some enumeration;
  - (a′) for every x the set {Π_ρx} is bounded in Q;
  - (b) Σ_ρ Π_ρx converges absolutely for every x;
  - (c) there are C, K with |c_{ρ,k}| ≤ C(1 + |γ|)^K for all ρ and all k < m_ρ;
  - (d) J: Q → Λ_m is an isomorphism of Fréchet spaces.
- For simple zeros, (c) is Proposition 40.4's bound on |ζ′(ρ)|.

*Proof.*
1. **(a) ⇒ (a′) and (b) ⇒ (a).** Π_{ρ_n} = S_n − S_{n−1}, and absolute convergence in a Fréchet space implies convergence.
2. **(a′) ⇒ (c).**
   - Steps 2–5 of the proof of 40.4(i) give |H| ≤ B_ρ on ∂R, hence on R by the maximum principle, with B_ρ the bound of step 5.
   - The disc |s − ρ| ≤ ½ lies in R: β ± ½ ∈ (−½, 3/2) and T_1 ≤ γ − 1 < γ + 1 ≤ T_2. So Cauchy's estimate gives |H^{(k)}(ρ)/k!| ≤ 2^kB_ρ.
   - The jet of H at ρ is e^{T²}·Σ_k c_{ρ,k}T^k mod T^m, so Σ_k c_{ρ,k}T^k = e^{−T²}·jet_ρ(H) mod T^m. The coefficients of e^{−T²} have modulus at most 1, so |c_{ρ,k}| ≤ 2^{k+1}B_ρ ≤ 2^mB_ρ.
   - This is polynomial in |γ|, because m_ρ = O(log |γ|) by (D1).
3. **(c) ⇒ (d) and (b).**
   - V_ρ(s) = (s − 1)ζ(s)/(s − ρ)^m is entire. The reciprocal of its jet at ρ is v_ρ^{−1}(T) = (Σ_k c_{ρ,k}T^k)(ρ − 1 + T)^{−1} mod T^m. The coefficients of (ρ − 1 + T)^{−1} have modulus at most |ρ − 1|^{−1} ≤ 1, so those of v_ρ^{−1} are at most mC(1 + |γ|)^K.
   - Put λ = m + 1, q_{ρ,k} = [T^k e^{−λT²} v_ρ^{−1}]_{<m} and G_{ρ,k}(s) = e^{λ(s−ρ)²}V_ρ(s)q_{ρ,k}(s − ρ).
   - G_{ρ,k} is entire, has jet T^k mod T^m at ρ, and vanishes to full order at every other zero (checks G1–G2, at a triple zero of a model).
   - The coefficients of e^{−λT²} are at most e^λ, so those of q_{ρ,k} are at most Q_ρ = m²e^{m+1}C(1 + |γ|)^K.
   - For |s − ρ| ≥ 1 and |σ| ≤ A, with u = t − γ:
     - |s − ρ|^{−m} ≤ 1;
     - |q_{ρ,k}(s − ρ)| ≤ mQ_ρ(A + 1 + |u|)^{m−1};
     - |e^{λ(s−ρ)²}| ≤ e^{(m+1)(A+1)²}e^{−(m−1)u²}e^{−2u²};
     - e^{−u²}(A + 1 + |u|) ≤ A + 2.
     
     So |G_{ρ,k}(s)|(1 + |t|)^M ≤ mQ_ρe^{(m+1)(A+1)²}(A + 2)^{m−1}C_A(1 + |γ|)^{M+c_A}·sup_u e^{−2u²}(1 + |u|)^{M+c_A}.
   - For |s − ρ| < 1 use the maximum principle with A′ = max(A, 2). Every factor is polynomial in 2 + |γ|, because m ≤ C log(2 + |γ|), so b_{A,M}(G_{ρ,k}) ≤ C_{A,M}(2 + |γ|)^{N_{A,M}}.
   - Hence F_P = Σ_ρΣ_{k<m_ρ}P_{ρ,k}G_{ρ,k} converges absolutely in ℬ for P ∈ Λ_m, and J[F_P] = P.
   - J is continuous into Λ_m by Lemma 40.1, since 2^r ≤ 2^{m_ρ} is absorbed by raising M. It is injective by OMS5.2, so it is an isomorphism.
   - Finally Σ_k x̂_{ρ,k}[G_{ρ,k}] = s_ρ(j_ρx) = Π_ρx, since both sides have the same jets at every zero. These terms are absolutely summable.
4. **(d) ⇒ (b).** As in the proof of 40.4(iii), using J^{−1}. ∎

Whether (c) for k = 0 alone suffices when there are multiple zeros is not settled here. In the weighted spaces A_p the analogous leading-coefficient condition is sufficient for interpolation (Berenstein–Taylor 1979, Theorem 4; §7).

**Remarks.**
- **The hypothesis of 40.4(ii) is not known.** A bound |ζ′(ρ)| ≥ c(1 + |γ|)^{−K} at every zero implies that all zeros are simple, which is open.
  - The proportion κ* of simple zeros is known unconditionally to be at least 0.4058 (Bui–Heath-Brown, *On simple zeros of the Riemann zeta-function*, arXiv:1302.5018, §1, with references).
  - This was improved to 0.4075: Pratt–Robles–Zaharescu–Zeindler (arXiv:1802.10521) prove κ* ≥ 0.407511 for simple zeros on the critical line, which is a lower bound for all simple zeros.
  - Under RH it is expected that |ζ′(ρ)|^{−1} ≫ |γ|^{1/3−ε} for infinitely many zeros, for each ε > 0 (Milinovich–Ng, *A note on a conjecture of Gonek*, arXiv:1106.1160, p. 2). If so, such a bound could only hold with K ≥ 1/3.
- **The mechanism.** A convergent primary decomposition needs interpolating representatives of polynomial size.
  - For a representative F with jet e^{T²} or 1 at ρ, the value at ρ of F(s)(s − ρ)^m/ζ(s) is m!/ζ^{(m)}(ρ). This function is holomorphic away from the trivial zeros.
  - By the maximum principle on rectangles between good heights, that value is controlled by the size of F.
  - The expansion x = Σ x̂(ρ)s_ρ(1) is formally like the residue expansion of Mertens' function, M(x) = (2πi)^{−1}∫ x^s/(sζ(s)) ds. There the residue at a simple zero is x^ρ/(ρζ′(ρ)), which carries the same factor 1/ζ′(ρ).

## 6. Negative results (goal 1)

- **40.N1. Nothing in OMS5–OMS7A constrains where the zeros are.** Every statement is uniform in the zero set. The only properties of the zeros used are:
  - 0 < Re ρ < 1, for the Cauchy circles of Lemma 40.1;
  - the multiplicities m_ρ;
  - the unboundedness of the heights, for the properness of 𝒥.

  OMS8 says so itself: "No conclusion about |p^ρ| = p^{1/2} was inserted."
- **40.N2. The primary decomposition of the zeta quotient is not available without new input about ζ at its zeros** (Propositions 40.4–40.5).
  - Its convergence for every class, in some enumeration, is equivalent to polynomial bounds on the principal parts of 1/ζ at the zeros. In particular it forces |ζ^{(m_ρ)}(ρ)/m_ρ!| ≥ c(1 + |γ|)^{−K}.
  - If all zeros are simple, it is equivalent to |ζ′(ρ)| ≥ c(1 + |γ|)^{−K}. That bound on its own implies that all zeros are simple, which is open.
  - OMS6 and SCL7 therefore rightly use finite sums of primary projectors only. GEX2 avoids projectors altogether and states that it assumes no convergence of an infinite sum of primary projectors. An argument that summed them over all zeros would need this input.
- **40.N3. Q is not the product of its primary blocks** (OMS5; the programme's own statement). J(Q) is a proper dense subspace of ∏_ρ A_ρ, and its topology is strictly finer than the product topology. The constant tuple 1, which is the obstruction behind PGD4's nonzero class c_ζ, is not a jet tuple.

## 7. Bridges (goal 2), and what the searches found

- **OMS7A completes AC3.** AC3's two-term complex C = [Q_0 → 𝒜] is built from the adelic periodization of Connes and of Connes–Consani–Marcolli (AC0). After degree-zero coinvariants it is formal: C ≃ ℬ_pr[1] ⊕ Q[0] equivariantly, with Q Meyer's quotient and D_cl = 0.
- **OMS6 and Weil II §1.7.**
  - Each primary block is a Jordan block of N_ρ = L_Q − ρ of size m_ρ, on which W_a = a^ρ exp((log a)N_ρ).
  - The dilations commute with N_ρ. Deligne's Frobenius instead satisfies FNF^{−1} = q^{−1}N: N: V(1) → V by (1.7.2.2), and it commutes with the Weil group by (1.7.3), both on p. 171.
  - So by `36_` 36.N3 the dilations cannot carry Deligne's local weights on a block with m_ρ ≥ 2: all of the block has the single dilation weight 2Re ρ.
- **Propositions 40.4–40.5 and the literature.**
  - They are an instance, for Meyer's quotient, of the classical equivalence between lower bounds at the zeros and interpolation or representing systems:
    - Berenstein–Taylor, *A new look at interpolation theory for entire functions of one variable*, Adv. Math. 33 (1979), 109–143, Theorem 4: a lower bound Σ_j|f_j^{(m_k)}(z_k)|/m_k! ≥ εe^{−Cp(z_k)} makes V an interpolating variety for A_p, with a converse for jointly invertible f_j;
    - Abanin–Le Hai Khoi–Nalbandyan, *Minimal absolutely representing systems of exponentials for A^{−∞}(Ω)*, J. Approx. Theory 163 (2011), 1534–1545, Theorem 1.2, whose conditions include liminf[log|L′(λ_k)| − H_Ω(λ_k)]/log(1 + |λ_k|) > −∞.
  - For ζ itself, Bondarenko–Radchenko–Seip (*Fourier interpolation with zeros of zeta and L-functions*, arXiv:2005.02996, Theorem 1.1) build rapidly decaying interpolating functions V_{ρ,j} at the zeros. They sum over the zeros only as a limit along a fixed sequence of heights T_k. Ungrouped convergence would need exactly the bounds of Proposition 40.5.
  - The seventeenth referee searched the programme at 36a82ec and at origin/main. No programme file states Propositions 40.4–40.5; every mention of an infinite sum of projectors or of 1/ζ′(ρ) is a disclaimer (OMS6, GEX2, RZ, ORE3.2, DPL8, GZR4, the JTB check). The literature search found no statement for Meyer's quotient, a Nyman–Beurling quotient or a Connes-type quotient.
  - The Gaussian test vector and the summability over the zeros are the programme's own (CFP6.1, CFP7.3, CFP8.1).
- **Negative moments of ζ′(ρ).** Propositions 40.4–40.5 ask a pointwise question about the principal parts of 1/ζ, and about 1/ζ′(ρ) when the zeros are simple. The Gonek–Hejhal conjectures concern averages, Σ_{0<γ≤T}|ζ′(ρ)|^{−2k}. For k = 1 Gonek conjectured the asymptotic (3/π³)T, and under RH and simplicity Milinovich–Ng prove half of it as a lower bound (arXiv:1106.1160).

## 8. Not checked

- RZ1–RZ8 in their own file (`ORIGINAL_ZETA_RESOLVENT_AND_PROJECTORS.md`): only OMS6's restatement was checked.
- CW beyond CW1 and CW7, AC5–AC9, and ABR1–ABR25 (the adelic coinvariant bridge on which AC1 relies: ABR9, ABR12, ABR14–ABR15).
- Meyer's paper itself (`26_` §3); the referee's text search of it found no discussion of the convergence of the spectral decomposition.
- Titchmarsh's Theorems 9.2, 9.6(A) and 9.7 were checked by the referee on page images of the second edition (pp. 211, 217, 218); I have not seen the pages myself. Davenport's Chapter 15 was not checked.

## 9. Revision after the seventeenth referee pass

An independent referee pass reported at 21:41 UTC. It used 32 check items: 25 PASS and 7 FAIL, all 7 marked as expected and each documenting a finding. The pass also confirmed:
- the audit of OMS5–OMS7A and every proof (Lemmas 40.1–40.2, Proposition 40.4);
- the citations;
- the bookkeeping (a copy of the script reproduced its output byte for byte).

It found two major points, both about wording, and fourteen minor ones. I accepted all of them after checking the passages involved: CW7 (line 282), Weil II p. 171 (OCR), GEX2, CFP6–CFP8, Bondarenko–Radchenko–Seip Theorem 1.1, PRZZ §1, and the publisher's pages for Berenstein–Taylor Theorem 4 and Abanin–Le Hai Khoi–Nalbandyan Theorem 1.2.
- **M1 (title).** The title stated the convergence criterion without the simplicity hypothesis. It now states the general criterion of Proposition 40.5 (principal parts of 1/ζ), which needs no hypothesis.
- **M2 (a remark mis-aimed at OMS).** OMS7.2 does not write an unrestricted scalar action: it invokes CW7, whose scalars lie in G_L(ℂ). The verdict now lists four remarks, none a defect.
- **Minor points.**
  - m1: h_k = ½f_{F_k}, stated without the inconsistent ℳ^{−1}.
  - m2: F(s)(s − ρ)^m/ζ(s) is holomorphic away from the trivial zeros, not entire.
  - m3: GEX2 uses no projectors.
  - m4: the Weil II citation is (1.7.2.2) and (1.7.3).
  - m5: K ≥ 1/3.
  - m6: the record 0.407511 (PRZZ).
  - m7: Titchmarsh's Theorems 9.2, 9.6(A), 9.7; Lemma 40.2 is Theorem 9.7.
  - m8: the generator is L_Q, distinct from the lattice L.
  - m9: Proposition 40.5 and the weaker hypothesis of 40.4(i).
  - m10: novelty context and the credit to CFP.
  - m11: checks E3 and F2 strengthened, F2a added (and G1–G3 for Proposition 40.5).
  - m12: 40.N2 wording.
  - m13: the complex is AC3's, built from Connes' and Connes–Consani–Marcolli's periodization.
  - m14: the growth exponent in (ii).
