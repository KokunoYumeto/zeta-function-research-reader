# The 25 September continuations, part 2: the divisor potential, positive measures, spectral synthesis and the Hilbert returns

Claude (claude-ab lane), model `claude-opus-5-5` (Opus 5.5) at maximum reasoning effort. 25 September 2026, 05:58 UTC.

This is a content map of eight proof blocks from the programme's continuation `20260925-full-source-tensor-and-original-divisor`. I read all eight in full:

| Block | File | What it is about |
|---|---|---|
| OZD0–OZD8 | `identity/ORIGINAL_ZETA_DIVISOR_DEFECT_RECEIVER.md` | a positive off-line detector written as a logarithmic potential of ζ |
| SPF0–SPF11 | `identity/SOURCE_POSITIVE_MEASURES_AND_DESCENT.md` | the positive transfer forms before the quotient (SPF0 and SPF9–SPF11 were mapped in `09_`; SPF1–SPF8 are new here) |
| GSP0–GSP9 | `gct/GAUSSIAN_SPECTRAL_SYNTHESIS.md` | finite-rank spectral synthesis on the zeta quotient |
| CTS0–CTS6 | `gct/COMPLETED_TENSOR_SOURCE_SYNTHESIS.md` | the same on completed tensor powers |
| FGR0–FGR7 | `counterfactual/FULL_GRAM_RESONANCE_RETURN.md` | Connes' harmonic-measure trace, with the full Gram matrix |
| WHR0–WHR12 | `counterfactual/WEIGHTED_HILBERT_RETURN_AND_EXACT_KERNEL.md` | Connes' weighted-L² realization compared with the Fréchet quotient |
| HCS0–HCS12 | `counterfactual/HILBERT_CLOSURE_CLOSED_SUPPORT_AND_RESTRICTION.md` | the Hilbert-closure defect, supported cohomology and the restriction cross |
| GMC0–GMC7 | `counterfactual/GLOBAL_MIXED_RETURN_CONTRACTION.md` | the mixed boundary of the tensor square, contracted globally |

The explicit formulas I could test are tested in `checks/c925_part2_checks.py` and `checks/fgr_trace_check.py`. All pass (§2). Throughout:

- Q = A/J is the programme's quotient, and ℬ is its Mellin picture: entire functions decaying rapidly in vertical strips.
- 𝓘 is the ideal of all zero-jets.
- F₀(s) = s(s−1)π^{−s/2}Γ(s/2)ζ(s)/8 = ξ(s)/4 is the programme's generator of 𝓘.

## 1. Content map

### 1.1 OZD: a positive off-line detector as a potential of log|ζ|

For r > 1 and t > 0 the programme defines

  𝓔_r(t) = Σ_ρ m_ρ (r^σ − r^{1−σ})² e^{2t(σ² − γ²)},  ρ = σ + iγ.

Every term is ≥ 0, and a term vanishes exactly when σ = ½. So 𝓔_r(t) = 0 if and only if RH holds (OZD6.1).

The block then rewrites 𝓔_r(t) through the Riesz decomposition of log|ζ|. First comes Δ log|ζ| = 2π(Σ m_ρ δ_ρ + Σ_k δ_{−2k} − δ₁) (OZD1.2). The global test class is justified by an Euler–Maclaurin strip bound (OZD2). The result is the exact identity (OZD3.4):

  𝓔_r(t) = (1/2π)∫ log|ζ| Δφ dA + (r−1)²e^{2t} − Σ_k η(−2k) q_r(−2k) e^{8tk²},

with φ = η(x) q_r(x) e^{2t(x²−y²)} and q_r(x) = (r^x − r^{1−x})².

The functional equation is then split into its even and odd parts under s ↦ 1 − s̄.

- The odd part of log|ζ| is exactly ½ log|χ| (OZD5.3).
- Its divisor consists only of the Gamma poles and zeros (OZD5.4).
- Its whole contribution is therefore the pole and trivial-zero terms (OZD5.6).

What survives, for a symmetric cutoff supported in (−½, 3/2), is (OZD5.7–5.8):

  𝓔_r(t) = (1/2π)∫ L₊ Δφ₊ dA + (r−1)²(e^{2t} + 1)/2,  L₊(s) = ½ log|ζ(s)ζ(1−s̄)|.

So RH is equivalent to the single identity

  (1/2π)∫ L₊ Δφ₊ dA = −(r−1)²(e^{2t} + 1)/2,

for any one fixed r > 1 and t > 0. OZD7 says explicitly that this identity has not been proved.

My checks:

- the Laplacian formula OZD3.3, symbolically;
- φ₊(1) and φ₋(1) (OZD5.8), symbolically;
- the odd-part identity log|ζ(s)| − log|ζ(1−s̄)| = log|χ(s)|, numerically, error 3·10⁻³¹ at four points;
- the divisor of χ, from the Gamma poles by hand.

### 1.2 SPF1–SPF8: the Bochner–Schwartz step, done by hand

SPF0 classifies the jointly continuous positive forms b on ℬ with b(T_nF, G) = b(F, nT_{1/n}G). They are exactly the forms

  b(F, G) = ∫ F(½+iλ) \overline{G(½+iλ)} dμ(λ)

with μ positive and tempered (register S22). SPF1–SPF8, read now, prove this without citing Stone's theorem.

1. An exact Laplace transform pair identifies ℬ with the space of smooth functions decaying faster than every exponential (SPF1).
2. The completed form carries a unitary group V_t (SPF2).
3. Multiplication by Laplace transforms is an honest group integral (SPF3).
4. The Gaussian g(s) = e^{(s−½)²} is a cyclic vector, because its spectral multiplier e^{−λ²} never vanishes (SPF4).
5. The measure is read off a scalar model (SPF5).
6. Continuity forces temperedness (SPF6).
7. Sufficiency and uniqueness follow (SPF7).

SPF8 checks that F₀ = ξ/4 belongs to the ideal, with every exceptional value. SPF9 uses it: a form descends to the zeta quotient exactly when μ is supported on the critical zeros.

In classical terms, SPF0 is the Bochner–Schwartz theorem written in Mellin coordinates. That theorem says a positive definite distribution on ℝ is the Fourier transform of a positive tempered measure (V. S. Vladimirov, *Methods of the Theory of Generalized Functions*, Taylor & Francis 2002, p. 125, as stated in arXiv:2009.02802).

Checked: the Mellin integral SPF8.2 (numerically exact at s = 2.3 + 1.1i), F₀(0) = F₀(1) = 1/8, F₀(−1) = F₀(2) = π/24, and F₀(−4) = F₀(5).

### 1.3 GSP: spectral synthesis on the zeta quotient, with explicit approximants

The resolvent of multiplication by s on Q = ℬ/𝓘 is written with the correction term F₀F(λ)/F₀(λ) (GSP2.1). It is bounded on the lines Re λ = ±2 by a Hadamard-product lower bound for |F₀| away from small discs (GSP2.3–2.5).

The Cauchy integral of e^{tλ²}R_λ over those lines equals multiplication by e^{ts²} on all of Q (GSP3.4).

Truncated at zero-free heights T_j ∈ [j⁶, j⁶ + 1], it gives finite-rank operators

  K_j = Σ_{|Im ρ| < T_j} Σ_{a<m_ρ} (g_{1/j}^{(a)}(ρ)/a!) (L − ρ)^a P_ρ,

which converge to the identity uniformly on bounded sets (GSP4.7). Consequences:

- **GSP5.** Every closed submodule of Q for the multiplier ring is determined by local jet orders k_ρ ≤ m_ρ. This is a local description of closed submodules in the sense of Krasichkov-Ternovskii (J. Soviet Math. 26 (1984) 2180–2182, and *Invariant subspaces of analytic functions* I–II, Mat. Sb. 87–88 (1972)), for this particular module.
- **GSP6.** Let J_L and J_O be the ideals imposing full jets on the line zeros and on the off-line zeros respectively. Then J_L + J_O is dense in ℬ. Hence the reconstruction defect ℬ/(J_L + J_O) has zero Hausdorff quotient, while the algebraic space may be nonzero.
- **GSP8.** There is a continuous Gaussian lift Q → ℬ. Its failure to commute with multiplication is an explicit cocycle, rank one for h(s) = s: −F₀·λ_t, where λ_t sums the residues of e^{tλ²}F/F₀ (GSP8.6–8.7).

### 1.4 CTS: the same on tensor powers

Baire's theorem gives equicontinuity of the K_j (CTS1). The tensor powers K_j^{⊗k} then converge to the identity on the completed projective tensor powers (CTS2).

Two consequences:

- The tensor receiver map b_k is injective (CTS3).
- The common radical of **all** continuous positive transfer forms on the k-th tensor power is the closed span of the tuples with Re Σλ_a ≠ k/2 (CTS4.6).

For k = 2, an off-line zero λ and its reflection λ^# = 1 − λ̄ satisfy λ + λ^# = 1 + 2i Im λ. Their tensors are therefore centred and survive every positive form. On them the programme's Weil tensor pairing takes the values ±2m², so it is indefinite (CTS5.1).

### 1.5 FGR: Connes' harmonic-measure trace with the full Gram matrix

Take finitely many exponents ρ = β + iγ with multiplicities. Let P_{Ω,T} be the orthogonal projection onto the span of the functions x^j e^{(ρ̄−½)x}, j < m_ρ, on the window [−T, T]. Then (FGR4.2):

  lim_{T→∞} Tr(P_{Ω,T} V(t)) = Σ m_ρ e^{−|β−½||t|} e^{iγt},  where V(t) is translation.

So an off-line exponent enters the limiting trace through its Poisson kernel on the critical line: it is swept to the line. This is Connes' §VIII harmonic distribution (arXiv:math/9811068).

FGR0 says Connes' sketch asserts that the individual same-side exponential vectors become asymptotically orthogonal. FGR2.3 shows that they do not: two unit vectors from the same side have a nonzero limiting inner product. The trace limit survives because the full inverse Gram matrix is kept.

I did not verify the wording of Connes' sketch: the text fetched from arXiv was truncated before §VIII. The mathematics I did verify, numerically, with synthetic exponents including a double one (`checks/fgr_trace_check.py`):

- The trace converges to the predicted limit with error O(1/T): 0.062, 0.018, 0.0088 and 0.0044 at T = 10, 20, 40, 80.
- The same-side inner product converges to the predicted modulus 0.13986 (agreement to 12 digits at T = 80).
- The discrete example 2^n, 3^n, n = −N, …, N gives √24/5, as FGR2.2 states.

FGR6 records the price of the sweep. For a reflected pair it replaces e^{d t} + e^{−d t} by 2e^{−d|t|}, a change of exactly 2 sinh(d|t|).

### 1.6 WHR: Connes' weighted-L² realization against the Fréchet quotient

On H_δ = L²((0,∞), (1 + log²u)^δ du), the closure of J is described exactly by the following results.

- **WHR2.** The jet functional F ↦ F^{(j)}(ρ) is continuous on H_δ iff Re ρ = ½ and j < δ − ½. Its squared norm is Γ(j+½)Γ(δ−j−½)/Γ(δ).
- **WHR5.** The annihilator of J is the closed span of these functionals.
- **WHR3.4.** One explicit Schwartz function h₀ generates the whole closure through its dilations. Its sum b₀ = Σh₀ has Mellin transform (s − 1)ζ(s)e^{s²}.
- **WHR7.** The Hilbert quotient is a weighted sequence space of jets.
- **WHR8.3.** The dilation norm is exactly ‖T_a‖ = a^{1/2}Λ₊(log a)^{δ/2}, with Λ₊(t) = (t² + 2 + |t|√(t²+4))/2. Hence the spectrum of each prime dilation on the Hilbert quotient lies on |z| = √p (WHR8.5).
- **WHR9.3.** The natural map q_∞ : Q → lim_n 𝓗_n has kernel I_c/I, the classes vanishing on all critical-line jets. So q_∞ is injective if and only if RH holds.
- **WHR10.** The algebraic map Q → H_δ/J is always injective. Every lost class is lost in the Hausdorff quotient.

Connes' δ_CC equals 2δ, and WHR says it adds no new spectral theorem (WHR0).

Checked: the Beta integral WHR2.4 for three pairs (j, δ); the Mellin transform of h₀ at two points, together with ∫h₀ = 0; and Λ₊ against a grid supremum for four values of t.

### 1.7 HCS: the Hilbert-closure defect in supported cohomology

Let K_off = B_off/J be the classes of Q that vanish on all critical-line jets. By WHR9, this is exactly what the Hilbert family loses. HCS places K_off in the programme's three-point sheaf, and the argument runs in five steps.

1. Closed-support cohomology contains K_off twice, with an equivariant split (HCS2.3–2.4).
2. The restriction extension on K_off is a proved pushout of the original one (HCS5.2).
3. Its connecting map, on an off-line block of multiplicity m, is the functional-equation germ (−1)^j j!/2 · t^{r−1−j} χ_ζ(b+t) mod t^{min(m,r)}, of rank min(m, r). This is ORE5 restricted to K_off (HCS7.10).
4. At critical parameters, explicit lifts exist (HCS7.8–7.9).
5. An intermediate cone keeps one more defect, T/qT ≅ V/qV, at critical parameters (HCS9.7, HCS10.6).

HCS11 states the conclusion itself. On K_off, source and target of the connecting map carry the same character a^{1−ρ}. So the map creates no Deligne weight gap: this is negative result 19, now on the Hilbert-closure defect.

### 1.8 GMC: the mixed boundary of the square contracts

In the tensor square, the mixed part of the degree-one boundary is removed globally by an explicit equivariant homotopy. It is built from the section s₊ = Σ^{−1} on J (GMC2–GMC4). The result is

  RΓ(Y, G) ≃ K₀[0] ⊕ (Q ⊗ Q)[−1],  K₀ ≅ (H ⊗ Q) ⊕ (Q ⊗ H),

an equivariant quasi-isomorphism.

The residue trace factors through Q ⊗ Q. On reflected blocks it has character p (GMC6.3). In GMC7's own words, it supplies no bound on Re ρ by itself.

## 2. Checks

| Script | What it checks | Result |
|---|---|---|
| `checks/c925_part2_checks.py` | OZD3.3 (sympy); OZD5.8 (sympy); OZD5.3 (mpmath, 30 digits); SPF8.2 and SPF8.4/GSP1.6; WHR2.4; WHR3.2; WHR8.2 | all agree; output in `c925_part2_checks_OUTPUT.txt` |
| `checks/fgr_trace_check.py` | FGR4.2 trace limit, FGR2.3 inner product, the discrete √24/5 example | all agree; output in `fgr_trace_check_OUTPUT.txt` |

The divisor of χ (OZD5.4) and the odd-part bookkeeping (OZD5.6) I checked by hand. For OZD5.6, φ₋(1+2k) = −φ₋(−2k) turns the two divisor sums into Σ_{k≥0} φ₋(−2k).

The GSP estimates, the CTS tensor argument and the HCS/GMC homological algebra I read for correctness of each step. I did not re-derive them independently.

## 3. Items for the goals

**Lemmas that stand alone (goal 3).**

1. **The divisor-potential form of RH (OZD5.7).** For fixed r > 1, t > 0 and a symmetric cutoff, RH is equivalent to (1/2π)∫ ½log|ζ(s)ζ(1−s̄)| Δφ₊ dA = −(r−1)²(e^{2t}+1)/2.
   - It belongs to the family of RH-equivalent integral identities for log|ζ|. Those identities go back to Littlewood's lemma and include Balazard–Saias–Yor: RH iff ∫_{Re s=½} log|ζ(s)| |s|^{−2}|ds| = 0 (Adv. Math. 143 (1999) 284–287; statement as in Bui–Lester–Milinovich, arXiv:1306.0856).
   - The generalized Littlewood families of Sekatskii–Beltraminelli–Merlini (Ukr. Math. J. 64 (2012) 247–261) unify the earlier equalities of Wang, Volchkov and Balazard–Saias–Yor.
   - OZD's version is an area integral, with a weight that vanishes to second order on the line. I have not searched for this exact form.
2. **The swept trace (FGR4.2).** For any finite set of exponents with multiplicities, the compressed translation trace tends to Σ m e^{−|β−½||t|}e^{iγt}. This holds although same-side vectors stay non-orthogonal.
3. **The exact weighted dilation norm (WHR8.3).** On L²(ℝ, (1+x²)^δ dx), translation by t has norm Λ₊(t)^{δ/2}. This is elementary; the constant comes from a 2 × 2 eigenvalue problem.
4. **Connes against Meyer (WHR9.3).** The natural map from Meyer's Fréchet quotient to the inverse limit of Connes' weighted Hilbert quotients is injective if and only if RH holds. Its kernel is exactly the off-line jet classes. (Meyer: arXiv:math/0412277. Connes: *Selecta Math. (N.S.)* 5 (1999), no. 1, from p. 29; arXiv:math/9811068.)
5. **Spectral synthesis on the zeta quotient (GSP5, GSP6).** The closed multiplier submodules are the jet-order submodules. The sum of the line ideal and the off-line ideal is dense.

**Negative results (goal 1).**

- **The functional equation removes only what it can see (OZD5).** The reflection s ↦ 1 − s̄ splits log|ζ| into an odd part, which is exactly ½log|χ|, and an even part. The odd part's contribution to the off-line detector is fully accounted for by the pole and the trivial zeros. The detector itself lives entirely in the even part, where the functional equation says nothing further.
  - My assessment: for fixed (r, t), the Gaussian factor e^{−2tγ²} makes each identity numerically blind above modest heights. Such an identity is an exact equivalence, not a route to a zero-free region.
- **The Hilbert realization loses exactly the off-line classes (WHR9, WHR10).**
  - The receiver is automatically pure: its prime spectra lie on |z| = √p (WHR8.5).
  - The whole question is its kernel, and the kernel is zero iff RH holds.
  - So a spectral-radius argument in Connes' Hilbert space cannot prove RH; it proves purity of what is left after the off-line classes are lost. This is the programme's statement WHR12, in plain terms.
- **The square adds nothing beyond Q ⊗ Q (GMC4.4).** Its mixed boundary contracts, and its trace pairs reflected blocks with character p.
- **Every positive form on the square sees reflected pairs as centred (CTS4–5).** Since ρ + ρ^# = 1 + 2iγ, positivity on the square cannot distinguish an off-line pair from an on-line one.
- **The restriction cross on the Hilbert defect has no weight gap (HCS11).** Source and target have the same character a^{1−ρ}.

**Bridges (goal 2).**

- OZD ↔ the Littlewood-lemma criteria (item 1 above).
- FGR ↔ Connes 1999 §VIII: the trace sweeps each off-line exponent onto the line with its Poisson kernel, which is harmonic measure.
- WHR ↔ Connes 1999, Theorem 1, and Meyer 2005 (item 4).
- GSP ↔ Krasichkov-Ternovskii's local description of closed submodules.
- SPF ↔ the Bochner–Schwartz theorem.

**F1 context (goal 4).** The pole at 1 is the average and the moment condition removes it. This item is now in the register (goal 4, item 10) and connects the summation map to the Bost–Connes phase transition.

## 4. Not yet read

In the same continuation I have not yet read these blocks:

- DER (`DIAGONAL_EXTRAORDINARY_RETURN`);
- FSC (`DERIVED_RETURN_FULL_SOURCE_CORRESPONDENCE`);
- `ALL_TENSOR_DERIVED_RETURN_AND_ACTUAL_GROWTH`;
- `FULL_VERTICAL_WEIGHT_RETURN` (VWR);
- `FULL_SOURCE_RETURN_EQUIVARIANCE_AND_MIXED_TENSOR_CLASS`;
- `FINITE_TOPOLOGY_DUALIZING_COMPLEX`;
- `ORIGINAL_RESIDUE_PRODUCT_SHEAF_PAIRING`;
- the `identity/` blocks GAP, ADM, SMC and PRIME_MONODROMY_STACKED_HISTORY.

The source-endpoint continuation's NCI, RSS and NHJ proofs are also unread. Their summaries are in `09_` §4(c).
