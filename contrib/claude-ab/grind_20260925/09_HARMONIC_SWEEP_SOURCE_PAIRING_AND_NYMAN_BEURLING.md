# The second attempt, part 5: harmonic sweeping, the source pairing, positive measures, and Nyman–Beurling

Claude (claude-ab lane), model `claude-opus-5-5` (Opus 5.5) at maximum reasoning effort. 25 September 2026.

This is a content map of three notes from the continuation published on 25 September (`workbenches/splitzero-tandem/continuations/20260925-full-source-tensor-and-original-divisor/`). It follows the style of `01_`, `04_`, `05_` and `07_`, and ends with my reading of what the notes add up to.

## Scope

**Read in full:**
- `counterfactual/ORIGINAL_ZETA_HARMONIC_SWEEP_AND_OFFCRITICAL_DEFECT.md` (HSW0–HSW9);
- `counterfactual/ORIGINAL_PRIME_DILATION_FORCING_IDENTITY.md` (OPD1–OPD6).

**Partly read:** `identity/SOURCE_POSITIVE_MEASURES_AND_DESCENT.md`. I read SPF0 and SPF9–SPF11 in full; SPF1–SPF8, which contain the construction of the measure, were not read.

**Read earlier, summarized in `08_` §3:** FST0–FST7 and TWC6, TWC10–TWC11.

**Not read:**
- OZD (only its section list);
- FGR, WHR, HCS, GMC, GSP and CTS;
- the rest of the identity lane;
- the proofs of the "source endpoint and residue section" continuation. Only its README and results bulletin were read.

## 1. Setting

The setting is the one in `07_` §1.

- S is the space of even Schwartz h with h(0) = 0 and ∫h = 0.
- A is the space of rapidly decaying smooth functions on (0, ∞).
- Σh(u) = 2Σ_{n≥1} h(nu), with J = ΣS closed and Q = A/J.
- F = M_0 b is the Mellin transform.
- The dilations are T_a b(u) = b(u/a), with generator L = −u∂_u.

## 2. What the notes establish

1. **An explicit summation-image test** (HSW5).
   - Take h_0(v) = (log|v| − 2)/(8√π) · exp(−(log|v|)²/4). It lies in S, with M_S h_0(s) = (s−1)e^{s²}/2.
   - Its image b_0 = Σh_0 has G(s) = M_0 b_0(s) = (s−1)ζ(s)e^{s²}.
   - Put b_† = b_0 * b_0^#. Then b_† ∈ J, and F_†(s) = G(s)G(1−s) = −s(s−1)ζ(s)ζ(1−s)e^{s²+(1−s)²}.
   - F_† vanishes to order 2m at every zero, equals |G(½+it)|² ≥ 0 on the critical line, and has F_†(0) = F_†(1) = e/2.
2. **Poisson sweeping of the zeros, and its failure to descend** (HSW2–HSW6).
   - Sweep each zero ρ = β + iγ onto the critical line with the Poisson kernel P_δ(t − γ), δ = |β − ½|. The result is a positive tempered measure ν_harm: point masses at the zeros on the line, plus the continuous density W_off(t) = Σ_{β≠½} m δ/(π((t−γ)² + δ²)).
   - This is the rational analogue of the harmonic distribution in Connes' trace-formula paper (§VIII, Lemma 3, positive characteristic; [arXiv:math/9811068](https://arxiv.org/abs/math/9811068)).
   - Its difference from the zero trace has the kernel form E(b) = 2Σ_{β>½} m ∫ g_b(x) e^{iγx} sinh((β−½)|x|) dx, where g_b(x) = e^{x/2}b(e^x) (HSW4.2).
   - On the test above, H_all(b_†) = ∫ |G(½+it)|² W_off(t) dt, which is > 0 if any off-critical zero exists (HSW6.2).
   - So harmonic sweeping descends to Q if and only if there are no off-critical zeros (HSW6).
3. **Two-sided size of the defect** (HSW6A). With explicit constants c₁, c₂ > 0 fixed by G, c₁ S_off ≤ H_off(b_†) ≤ c₂ S_off, where S_off = Σ_{β≠½} m|β − ½|/(1+γ²). The upper bound uses G(ρ) = 0, which removes any 1/δ loss.
4. **The defect as an exact sum of norms** (HSW6B).
   - For each zero ρ, let b_ρ ∈ A be the unique solution of (L − ρ)b_ρ = b_0. Its Mellin transform is G(s)/(s − ρ), and its class is the top eigenvector of the primary block at ρ.
   - Then H_off(b_†) = 2Σ_ρ m_ρ |Re ρ − ½| · ‖b_ρ‖²_{L²(du)}.
   - Moreover (2A_1/9π)/(1+γ²) ≤ ‖b_ρ‖² ≤ C/(1+γ²) for every zero, on the line or off it.
5. **The harmonic density remembers the off-critical divisor** (HSW7). The meromorphic continuation of W_off has poles at γ ± iδ with residues ±m/(πi). These give back every off-critical zero with its multiplicity.
6. **The source-pairing identity** (OPD4.2). For every zero ρ = β + iγ,

   (β − ½) ‖b_ρ‖²_{L²(du)} = −Re⟨b_ρ, b_0⟩.

   - The proof is one integration by parts, 2Re⟨b, Lb⟩ = ‖b‖², together with Lb_ρ = ρb_ρ + b_0.
   - The dilations do not act as eigenvectors on the representatives: T_a b_ρ = a^ρ b_ρ + R_{a,ρ}, where R_{a,ρ} ∈ J is explicit, with M_0R_{a,ρ} = G(s)(a^s − a^ρ)/(s − ρ) (OPD2).
   - R_{a,ρ} is nonzero for every a ≠ 1, even at critical zeros (OPD2.5).
7. **Summing the pairings** (OPD5). H_off(b_†) = 2Σ m|Re⟨b_ρ, b_0⟩|, while the signed sum Σ m Re⟨b_ρ, b_0⟩ = 0, because reflected partners cancel (OPD5.2–5.3).
8. **Positive forms before the quotient** (SPF0, SPF9–SPF10).
   - The jointly continuous positive forms on the entire-function source ℬ satisfying b(T_nF, G) = b(F, nT_{1/n}G) are exactly b(F, G) = ∫ F(½+iλ) \overline{G(½+iλ)} dμ(λ), with μ positive and tempered.
   - Such a form descends to the zeta quotient if and only if supp μ lies in the set of critical zeros. Then it is Σ m c_ρ F(ρ)\overline{G(ρ)}, which is CFP (`04_`).

## 3. Checks by claude-ab

- **`checks/hsw_opd_checks.py` (ALL PASS).**
  - HSW5.2 was checked at three points by quadrature.
  - OPD4.2, OPD5.2 and HSW6B.6 were checked on a synthetic Mellin function G(s) = (s−ρ)(s−ρ^♭)e^{s²}, with an artificial off-critical pair ρ = 0.8 + 5i, ρ^♭ = 0.2 + 5i:
    - (β−½)‖b_ρ‖² = −Re⟨b_ρ, b_0⟩ = 2.50008731384542;
    - ‖b_ρ‖² = ‖b_{ρ^♭}‖² = 8.33362437948472;
    - the Poisson-swept value equals 2δ‖b_ρ‖² = 5.00017462769083, to 1e−12.
  - The identities hold for any b_0 whose Mellin transform vanishes at ρ, so the synthetic test checks exactly what the notes use.
- **By hand:**
  - the Fourier transform of P_δ (HSW2.2);
  - the semigroup identity behind HSW3.5;
  - the kernel algebra 2cosh(δx) − 2e^{−δ|x|} = 2sinh(δ|x|) (HSW4.2);
  - F_† and its endpoint values (HSW5.8–5.9);
  - the integration by parts OPD4.1;
  - the invariance of the SPF0.3 form under the transfer relation: n^{½+iλ} = \overline{n^{1−(½+iλ)}}.
- **Not checked:** the explicit formula HSW4.3 in the programme's normalization, and SPF's measure construction (SPF1–SPF8).

## 4. My reading of what these notes add up to

**(a) The source-pairing identity is the Hilbert–Pólya mechanism.**
- On L²((0,∞), du) one has ‖T_a f‖² = a‖f‖². So a^{−1/2}T_a is unitary and L − ½ is skew-adjoint.
- For a vector with (L − ρ)b = b_0, OPD4.2 reads Re ρ − ½ = −Re⟨b, b_0⟩/‖b‖².
- On the quotient Q the source b_0 ∈ J is zero, and [b_ρ] is an honest eigenvector. If the L² inner product descended to Q, the pairing would vanish and every zero would lie on the line.
- It does not descend. J is dense in L²(du) (the programme's ASD10; HSW6B gives the proof). That proof is Wiener's L² Tauberian theorem: the translates of g_{b_0} span L²(ℝ) because their Fourier transform G(½+it) vanishes only on a null set (N. Wiener, *Tauberian theorems*, Ann. of Math. 33 (1932) 1–100).
- The RH content of the second attempt is therefore located precisely: it is the size of Re⟨b_ρ, b_0⟩ on actual representatives, and the harmonic defect (items 4 and 7) sums exactly these sizes.

**(b) Three independent confirmations that positivity sees only the critical zeros.**
- CPS: the positive receiver of R is zero (`04_`).
- TWC10: the same holds for off-line same-eigenvalue tensor powers (`08_` §3).
- SPF9: a positive transfer form descends only when its measure sits on the critical zeros.

These are three different constructions with the same outcome. So any argument that goes through a positive, transfer-compatible form on the zeta quotient has assumed, not proved, the location of the zeros.

**(c) Bridge: Nyman–Beurling is the programme's Σ with one-sided support.** The following identity is elementary; `checks/nyman_beurling_bridge_check.py` checks it numerically.

- Let a_k > 1 and c_k ∈ ℂ with Σ_k c_k/a_k = 0.
- Put h = Σ_k c_k 1_{[−1/a_k, 1/a_k]}. Then h is even, supported in [−1, 1], and ∫h = 2Σ c_k/a_k = 0. This is the programme's moment condition.
- Then

  Σ_k c_k {1/(a_k x)} = −½ · Σh(x),  and Σh(x) = 0 for x > 1.

  *Proof.* {1/(ax)} = 1/(ax) − ⌊1/(ax)⌋. The terms c_k/(a_k x) cancel exactly because Σc_k/a_k = 0, and 2⌊1/(ax)⌋ = Σ(1_{[−1/a,1/a]})(x). ∎
- The functions ρ_a(x) = {1/(ax)} are those of the Nyman–Beurling criterion: RH holds if and only if χ_{(0,1]} lies in the L²(0,∞)-closure of their span. Báez-Duarte strengthened this to a ∈ ℕ ([arXiv:math/0202141](https://arxiv.org/abs/math/0202141)); the original is A. Beurling, *A closure problem related to the Riemann zeta-function*, [PNAS 41 (1955) 312–314](https://www.pnas.org/doi/10.1073/pnas.41.5.312).
- Titchmarsh's identity ∫_0^∞ {1/x} x^{s−1} dx = −ζ(s)/s (0 < Re s < 1) also checks numerically to 1e−9.

**The typed morphism** between the unconditional statement and the RH-equivalent one is the support condition.

- Two-sided tests h ∈ S give an image J that is dense in all of L²(0,∞) (Wiener). Through Mellin–Plancherel, L²(0,∞) sees only the critical line.
- Tests supported in [−1, 1] give images supported in (0, 1]. Mellin transforms of L²(0,1) see the half-plane Re s > ½, where a zero of ζ is an obstruction to density.
- The programme's moment condition ∫h = 0 is exactly the removal of the 1/x tail, that is, of the pole of ζ at 1.

Burnol's "co-Poisson" theory studies this family of summation maps and their relation to Nyman–Beurling. In it, the zeros appear as the obstructions to co-Poisson sums filling L² (J.-F. Burnol, *On Fourier and Zeta(s)*, Forum Math.; [arXiv:math/0112254](https://arxiv.org/abs/math/0112254)). The programme's objects therefore sit inside an established Hilbert-space formulation of RH, and the one-sided restriction is the step at which RH enters.

**The programme is already on this road** (added after reading the results bulletin of the "source endpoint and residue section" continuation, `RESULTS_BULLETIN_2026-09-25.md`).

- Codex's identity-absorption task builds on S. W. Noor, *A Hardy space analysis of the Báez-Duarte criterion for the RH* (Adv. Math. 350 (2019) 242–255; [arXiv:1809.09577](https://arxiv.org/abs/1809.09577)).
- Its NCI result states that the closed span of all cover discrepancies equals the full zero-jet ideal ℐ in the original Fréchet topology, while the algebraic principal image is strictly smaller.
- Taken with the identity above, this gives one typed comparison between three settings:
  - In the Fréchet topology of entire functions of rapid vertical decay, the closure is the zero-jet ideal, unconditionally (NCI, and S13 of the register).
  - In L²(0,∞), the closure of the two-sided image is everything, unconditionally (Wiener).
  - For one-sided tests in L²(0,1) ≅ H²(Re s > ½), the closure is everything if and only if RH holds (Nyman–Beurling, Báez-Duarte, Noor).
- The three settings differ only in the topology and the support condition. RH is the statement about the third.

**(d) Bridge: Connes' §VIII.** HSW constructs the rational analogue of Connes' positive-characteristic harmonic distribution, and computes that it descends to Q exactly when RH holds (item 2). So in the rational case, harmonic sweeping cannot replace the zero trace without assuming RH. It still encodes the whole off-critical divisor faithfully (item 5).

## 5. Items for the four goals

**Negative results (goal 1).**
1. Poisson sweeping of the zeros descends to Q if and only if there are no off-critical zeros (HSW6).
2. The L² norm does not descend to Q, because J is dense in L²(du). So the naive L² completion of Q gives no Hilbert–Pólya argument (OPD3, HSW6B, ASD10).
3. Positive transfer-compatible forms descend if and only if their spectral measure sits on the critical zeros (SPF9). This is the third independent confirmation that positivity sees only the critical zeros (§4(b)).

**Standalone lemmas (goal 3).**
1. **Source-pairing identity.** For b_0 ∈ A with M_0b_0(ρ) = 0 and b_ρ the solution of (L − ρ)b_ρ = b_0 in A, (Re ρ − ½)‖b_ρ‖² = −Re⟨b_ρ, b_0⟩ in L²(du) (OPD4.2).
2. **Harmonic defect.** H_off(b_†) = 2Σ m|Re ρ − ½|‖b_ρ‖², and it is comparable to Σ m|Re ρ − ½|/(1+γ²) with explicit constants (HSW6A–6B).
3. **Positive-form classification** on ℬ (SPF0.3): the analogue of Bochner's theorem for the transfer relation.

**Bridges (goal 2).**
1. Nyman–Beurling and Burnol's co-Poisson theory, with the programme's Σ restricted to tests supported in [−1, 1]. The moment condition corresponds to the pole at 1 (§4(c)).
2. Wiener's L² Tauberian theorem, as the reason J is dense in L²(0,∞).
3. Connes' trace-formula paper, §VIII: its harmonic distribution, rationally realized.
4. The Hilbert–Pólya mechanism (§4(a)).
