# The source-endpoint proofs NCI, RSS and NHJ: Nyman–Beurling in the Fréchet topology, and what the section selects

Claude (claude-ab lane), model `claude-opus-5-5` (Opus 5.5) at maximum reasoning effort. 25 September 2026, 06:51 UTC.

This is a content map of three proof blocks from the continuation `20260925-source-endpoint-and-section`:

- NCI0–NCI8 (`NOOR_COVER_DISCREPANCIES_GENERATE_ORIGINAL_IDEAL.md`), read in full;
- RSS0–RSS6 (`RESIDUE_SECTION_SELECTION_AND_ORIGINAL_IDEAL.md`), read in full;
- NHJ0–NHJ3 (`NOOR_FULL_DUAL_INJECTIVITY_AND_HILBERT_DOMAIN.md`), read in part; its later sections were read only through their displayed results.

Together they complete bridge 13 of the register (Nyman–Beurling in three topologies) with the programme's actual proofs.

Notation:

- ℬ is the Fréchet space of entire functions decaying rapidly in vertical strips.
- 𝓘 is the ideal of all zero-jets of ζ, and Q = ℬ/𝓘.
- F₀ = ξ/4, g_t(s) = e^{ts²} with t > 0 fixed, and U_n F(s) = n^{1−s}F(s) is the cover action.

## 1. Results

1. **The zero-jet ideal is the closure of the principal ideal of ξ, and not the principal ideal itself (NCI2.8–2.9).**
   - closure(F₀ℬ) = 𝓘 in ℬ.
   - The proof divides by F₀ using the Hadamard product. It bounds |F₀|^{−1} ≤ exp(CR^{3/2} log R) outside discs of radius R^{−2} around the zeros, handling clusters of zeros with the maximum principle, and then regularizes with e^{εs²}.
   - Algebraically, F₀ℬ ⊊ 𝓘. F₀ itself lies in 𝓘, but F₀ = F₀G would force G = 1, and 1 ∉ ℬ.
2. **The cover discrepancies span the zero-jet ideal (NCI5.2).** For fixed t > 0, put δ_{n,t}(s) = 8e^{ts²}F₀(s)(n − n^{1−s})/s. Then

   closure(span{δ_{n,t} : n ≥ 2}) = 𝓘.

   The proof runs as follows.
   - Take a functional Λ that annihilates every δ_{n,t}. It gives an entire function L(w) = Λ(K_{t,w}) with |L(w)| ≤ C e^{C(1+|w|²)}, vanishing at every log n.
   - By Jensen's formula a nonzero such function has O(R²) zeros in radius R, while log 2, …, log e^R are exponentially many. So L ≡ 0.
   - Differentiating in w gives Λ(F₀ g_t e^{vs}) = 0 for all v. The half-Mellin integral then extends this to Λ(F₀ℬ) = 0.
3. **Sparse families suffice (NCI8.2).**
   - Any set S of cover degrees with #{n ∈ S : log n ≤ R}/R² unbounded gives the same closure 𝓘.
   - Example: for fixed d, the k-th powers k^d have count e^{R/d}.
4. **Without ξ, the same family spans everything (RSS1.2).** closure(span{g_t(s)(n − n^{1−s})/s : n ≥ 2}) = ℬ.
   - For a polynomial P with P(0) = 1, the family multiplied by P spans exactly Pℬ, the functions vanishing to the orders of P's zeros (RSS2.3, RSS2.5).
5. **What the section selects (RSS3.2).**
   - In the Hardy receiver, the largest subspace of the zero-coordinate slice that is invariant under every cover is determined by the residue section. It is (Pℬ)^⊥ for the polynomial section P, {0} for P = 1, and 𝓘^⊥ (the zeta divisor) for the original ξ section.
   - So cover invariance recovers exactly the divisor that the section inserts, including any prescribed finite set of nonzero points. This follows from RSS3.3: the jet action works at every nonzero point a.
6. **The Hardy receiver is injective on the whole dual (NHJ3–NHJ4).**
   - Noor's coefficient tests ψ_m = (m^{1−s} − (m+1)^{1−s} + 8F₀)/s, m ≥ 0, give Λ ↦ Σ_m conj(Λ(g_tψ_m)) z^m. This map is continuous and injective on ℬ′, by the same Jensen argument.
   - Its quotient-dual restriction is characterized by covariance under every cover (NCI6.3). The domain on which all covers are stable is exactly q′𝔇_t^Q (NCI7.3).
   - A projection defect n⟨(I − P_n)H_tμ, (I − P_n)H_tλ⟩ remains (NCI7.5). It is computed, not assumed to vanish.

## 2. Checks

- **NCI3.1a.** The identity (e^w − e^{(1−s)w})/s = w e^w ∫₀¹ e^{−θsw} dθ holds: the right side integrates to w e^w (1 − e^{−sw})/(sw).
- **NCI3.5.** (∂_w − 1)(e^w − e^{(1−s)w})/s = (e^w − (1−s)e^{(1−s)w} − e^w + e^{(1−s)w})/s = e^{(1−s)w}. This gives the stated exponential test.
- **NCI3.4.** At w = log n, K_{t,w} = 8g_tF₀(n − n^{1−s})/s = δ_{n,t}. At w = 0 the numerator vanishes, so K_{t,0} = 0.
- **The Jensen count.** A nonzero entire L with log|L(w)| ≤ C(1 + |w|²) has at most (C(1 + (|w₀| + 2R)²) − log|L(w₀)|)/log 2 zeros in the disc of radius R about any w₀ with L(w₀) ≠ 0, by Jensen's formula on the disc of radius 2R. The points log n, n ≤ e^R, number about e^R. This is the argument of NCI3, and I checked it by hand.
- **NCI1.8.** δ_{n,t}(0) = 8F₀(0)·(n log n) = n log n, using F₀(0) = 1/8 and (n − n^{1−s})/s → n log n.

## 3. Items for the goals

- **Bridge (goal 2): Nyman–Beurling in three topologies, now with the programme's proofs.** The divisor-generation statements NCI5.2 and NCI2.8 hold unconditionally in the Fréchet space ℬ. They are the analogue of the Nyman–Beurling–Báez-Duarte completeness, which in the Hardy-space setting of Noor (arXiv:1809.09577; Adv. Math. 350 (2019)) is equivalent to RH. As in `09_` §4(c), the topology decides where RH enters.
- **Negative result (goal 1): cover invariance cannot locate zeros (RSS3.2, RSS6).**
  - The Hardy receiver's covariance recovers exactly the divisor that the chosen residue section contains: the zeta divisor for ξ, any finite prescribed set for a polynomial section, and nothing for P = 1.
  - So covariance supplies recovery, not location. Any purity statement has to come from elsewhere; RSS6 says this itself.
- **Lemma (goal 3).**
  - For fixed t > 0, the functions e^{ts²}(n − n^{1−s})/s, with n in any set of density above R² in the log scale, span a dense subspace of ℬ.
  - Multiplied by ξ, they span a dense subspace of the zero-jet ideal of ζ.
  - Status: proved in the programme (RSS1, NCI5, NCI8); the Jensen step was checked by hand. Novelty not searched.
