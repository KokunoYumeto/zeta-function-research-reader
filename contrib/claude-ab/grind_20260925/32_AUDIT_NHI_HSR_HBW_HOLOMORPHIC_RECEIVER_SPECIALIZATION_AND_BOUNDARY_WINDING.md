# NHI, HSR and HBW: the holomorphic receiver, the specialization transpose and the boundary winding

Claude (claude-ab lane), model `claude-opus-5-5` (Opus 5.5) at maximum reasoning effort. 25 September 2026, written at 14:18 UTC. Board task 8, the fifth of the eight new result groups of the 25 September bulletin (NHI/HSR/HBW). The first pass was an audit by one subagent (13:30–14:08 UTC); §0 says which parts I verified myself. Not yet refereed.

## 0. Sources, method and checks

All six files are in `quantum_tau_programme_bridge_20260924/next_edition_after_647`. SHA-256 is given after conversion of CRLF to LF. HSRA and HBWR record exactly the hashes shown for HSR and HBW.

| file | block | SHA-256 (LF) |
|---|---|---|
| `NOOR_HOLOMORPHIC_RECEIVER_INJECTIVITY.md` | NHI0–NHI8 | `a31b0e9c…a62e8a17` |
| `NOOR_HOLOMORPHIC_INJECTIVITY_INDEPENDENT_REVIEW.md` | NHIR0–NHIR4 | `3634b2fc…14b11edf` |
| `HOLOMORPHIC_SPECIALIZATION_TRANSPOSE_RECEIVER.md` | HSR0–HSR12 | `a6acef5a…2812e593` |
| `HSR_INDEPENDENT_FORMULA_TOPOLOGY_REVIEW.md` | HSRA0–HSRA8 | `3e866834…4d903111` |
| `HOLOMORPHIC_BOUNDARY_WINDING_AND_COVER.md` | HBW0–HBW9 | `ff771c43…94a11305` |
| `HBW_INDEPENDENT_REVIEW.md` | HBWR0–HBWR7 | `a05979c2…b53dabeb` |

**Hash bookkeeping.**
- NHIR records NHI at an earlier hash, from before NHI8 was added. NHI8's content is NHIR3.
- `HBWR_TYPOGRAPHY_CORRECTION.json` is cited by the folder's `READ_THIS_CONTINUATION.md` for HBWR4.2. It was not staged for this audit. The subagent verified the delivered HBWR4.2 directly (its check C13).

**Method.**
- A subagent read all six files in full and re-derived every displayed identity.
- It wrote 26 checks, copied here unchanged apart from the header as `checks/nhi_hsr_hbw_audit_checks.py`. My re-run at 14:15 UTC gives 26/26 PASS, the same as its run.
- Its first run had three failures from test design: an O(z) error at z = 10⁻³⁰, and quadrature on slowly decaying tails. They were fixed before the recorded run.
- I verified myself:
  - the tail-annihilator statement (Lemma 32.1, derived below);
  - the uniqueness statement of Lemma 32.2 (proof below);
  - the correspondences with ABH, NHJ and NPE stated in §§1, 3 and 6;
  - of the negative results in §5, 32.N2 and the NHI8 bullet of 32.N4; the rest of §5 is the subagent's audit;
  - the "2j!" reading.
- Everything else in §§1–3 is the subagent's audit, supported by its checks.

**Verdict.** No mathematical error was found in NHI, HSR, HBW or their reviews. The findings are structural:
- NHI's main theorem is a third proof of a result already stated in NHJ4.6 and ABH2.
- NHI8's tail result already holds before passing to the quotient.
- Every condition in HSR and HBW that concerns where the zeros are is equivalent to RH by construction, except the finiteness condition of 32.N2.
- Everything that holds unconditionally is blind to the location of the zeros.

## 1. NHI and NHIR

- **NHI0–NHI5.** These prove that the holomorphic receiver of the corrected tests g_tψ_m, with ψ_m = φ_m + 8F₀/s, is injective on the strong dual.
  - The Jensen step is NCI3/ABH2.4–2.5, and the density of g_tℬ is NHJ4.4–4.5, the last step of ABH2.
  - So NHI5.4 is NHJ4.6 composed with the transpose of the quotient map, which NHJ and ABH2 already state.
  - NHI's route through Gaussian spectral synthesis (GSP4.3–4.7) is correct as far as checked, but it is unnecessary.
- **NHI6.** The cover discrepancy is NCI's δ_{n,t} (check C07). W_n* is not injective on 𝒪(𝔻), since W₂*(1 − z) = 0. So NHI6.3 is a statement about the image S_t, as NHI says.
- **NHI8 (tails; = NHIR3).** Correct, and the argument works already in ℬ′ before the quotient (Lemma 32.1).
- **NHIR** confirms NHI0–NHI7 without repairs and adds NHIR3 (tails) and NHIR4 (a Cauchy bound, correct by check C16). One wording point in NHIR2: U_n^{±1} do not preserve the strip seminorms; they are bounded, b_{a,N}(U_nF) ≤ n^{1+a}b_{a,N}(F) (NHI's notation b_{a,N} for the strip seminorms).
- **Typography.** NHI0, HSR0.2, HBW0.1 and HBWR0.1 write F₀(−2j) with "2j!", which must be read as 2·(j!), as in GDE8.3 (`30_` §1.4). Check C01 confirms this reading and shows that (2j)! fails for j ≥ 2.

## 2. HSR and HSRA

- **HSR1–HSR3.**
  - ker σ_r = conj(H_L) is correct.
  - The coordinate formulas are correct: checks C10 at ρ₁ and ρ₂, relative to the Gaussian factor, and C17–C18 on a synthetic divisor.
  - HSR3.3 has the value −1/(1 − ρ) at z = 0 (C11).
  - The constant |d_r| ≤ r + 1 is valid; in fact |d_r| < r − 1.
- **HSR4.** HSR4.1, the injectivity, is Lemma 32.2 in the programme's setting. HSR4.2 is a transported ℓ²(𝒵_O, m) norm, by definition.
- **HSR5.** This is the reproducing kernel of a range space. The positivity is ℓ² positivity.
- **HSR7.** The cover relations are GDE7's (β_rT_n = U_n*β_r, β_rU_n = T_n*β_r). HSR7.4's defect is AST's D_n = T_n* − U_n carried through a unitary map, so it adds nothing beyond AST.
- **HSR8.** The reflection identities hold (C17): d_r(ρ#) = −d_r, K_r² = 1, ΩT_nΩ = U_n, and HSR8.4 and 8.8.
- **HSR10.** HSR10.1–10.2 is AST6. The exact range of the ratio d_r/d_s is `24_` Lemma 24.5, which is sharper than HSR's "positive and finite" (C19). The inclusion D_{r,t₂} ⊂ D_{r,t₁} is strict iff the off-line set is infinite.
- **HSRA** confirms HSR and adds HSRA7 (Schatten classes; later HSR10.5–10.6) and HSRA8, correct by C18: K_rG = e^{−Δ}T_{e^{2Δ}}GK_r.

## 3. HBW and HBWR

- **HBW0–HBW2.** Correct (C10–C12).
  - The jet formula HBW0.5 needs its stated hypothesis j < m_ρ. At a simple zero the j = 1 formula fails by exactly conj(8g_t(ρ)F₀′(ρ)/ρ) (C10b).
  - The polylogarithm expansion Li_s(e^{−u}) = Γ(1 − s)u^{s−1} + A_s(u), with A_s(u) = Σ_k ζ(s − k)(−u)^k/k! holomorphic on |u| < 2π, is standard (DLMF §25.12(ii), as HBW cites). C12–C13 check it to about 10⁻³⁷, including negative real u.
- **HBW3–HBW5.** Correct (C14, symbolic for j ≤ 3).
  - Monodromy of the logarithmic power classes: e^{2πi(s−1)}Σ_k(2πi)^kS_{j−k}/k!.
  - The counting action: n^{1−s}Σ_k(−log n)^kS_{j−k}/k!, that is n^{1−s}exp(−(log n)N) on the jet classes.
  - At s = 0 with jet length 2 this has the same matrix as NPE4.2 (`31_` Lemma 31.2(b)). HBW itself works in 0 < Re s < 1, so no map to NPE's Laurent data is constructed.
  - The local sheet computation is a shadow of the exact identity W_n*K_s = n^{1−s}K_s (ABH1.4, with g_s = K_{s̄}).
- **HBW8–HBW9.** Correct (C13, C20–C22).
  - The isolator HBW8.12 behaves as claimed, and the kernel is H_L.
  - Only the value coefficients are treated, not general functionals in Q′; HBW says so.
  - HBW8.4's bound |Γ(2 − s)| ≤ 2 is loose; it is ≤ 1.
- **HBWR** confirms HBW and adds HBWR3.3–3.4, finite series for (M − I)^{−1} and the logarithm of a unipotent (correct by C15).

## 4. Lemmas extracted

**Lemma 32.1 (tail annihilators before the quotient; sharpens NHI8 = NHIR3).** Let t > 0, and let C be entire with C(0) = 1 and g_tC ∈ ℬ. Put ψ_m^C = φ_m + C/s with Noor's φ_m, and let M ≥ 1. The continuous functionals on ℬ that annihilate {g_tψ_m^C : m ≥ M} are:
- only 0, if C(1) ≠ 0;
- exactly ℂ·ev₁, if C(1) = 0.

In particular, for the programme's C = 8F₀, where C(1) = 8F₀(1) = 1, every tail is already total in ℬ, not only in Q.

*Proof.*
1. **Telescoping.** Σ_{m=M}^{n−1}ψ_m^C = [(nC − n^{1−s}) − (MC − M^{1−s})]/s.
2. **An entire function of order 2.** Let Λ annihilate the tail and put L(w) = Λ[g_t(e^wC − e^{(1−s)w})/s]. It is entire of order ≤ 2 by the bounds of ABH2 (`30_` §2.2), and L(log n) = L(log M) for every n ≥ M.
3. **L is constant.** Jensen's formula, applied to L − L(log M), gives L ≡ K for a constant K.
4. **Identifying Λ.** The derivative identity (∂_w − 1)L = Λ(g_te^{(1−s)w}) then gives Λ(g_te^{vs}) = −Ke^v for all v ∈ ℂ.
   - Since ev₁(g_te^{vs}) = e^te^v, the functionals Λ and −Ke^{−t}ev₁ agree on all g_te^{vs}.
   - The half-Mellin and continuation argument of ABH2 (steps after ABH2.5) uses only these functions. So Λ = −Ke^{−t}ev₁ on ℬ.
5. **Which multiples occur.** ev₁(g_tψ_m^C) = e^t(φ_m(1) + C(1)) = e^tC(1) for m ≥ 1, since φ_m(1) = 0 for m ≥ 1.
   - So ev₁ annihilates the tail iff C(1) = 0. If C(1) ≠ 0, the constant K must be 0, and then Λ = 0. ∎

The subagent's check C09 confirms ψ_m(1) = 1 for m ≥ 1 with C = 8F₀, and ψ_m(1) = 0 for C = 1 − s. C09 tests only these values; the lemma itself rests on the proof above.

The remark on ev₁ in Q:
- ev₁ is not in I^⊥, because g_tF₀ ∈ I and ev₁(g_tF₀) = e^tF₀(1) = e^t/8 ≠ 0. So the quotient statement NHI8 holds for every such C.
- NHIR remarks that F₀(1) = 1/8 is essential. In both routes the specific value is inessential, but the nonvanishing F₀(1) ≠ 0 is essential:
  - for the ℬ-level statement with C = 8F₀;
  - for ev₁ ∉ I^⊥ in the quotient.

*Credit.* The case M = 0 for general C is already in the closing paragraph of NHJ4 and in `30_` Corollary 30.2 (register S59).

**Lemma 32.2 (uniqueness of exponential sums on a divisor).** Let G ∈ ℬ, let Z be a set of zeros of G in a strip |Re s| ≤ A, and let (c_ρ) ∈ ℓ¹(Z). If Σ_ρ c_ρe^{ρx} = 0 for every real x, then c = 0.

*Proof.*
1. Every F ∈ ℬ has the half-Mellin representation F(s) = ½∫a(e^v)e^{sv}dv, with a(e^v) decaying faster than every exponential (NJS4.1).
2. Hence Σ_ρ c_ρF(ρ) = ½∫a(e^v)Σ_ρc_ρe^{ρv}dv = 0 for every F ∈ ℬ. The interchange is justified by the ℓ¹ condition and |e^{ρv}| ≤ e^{A|v|}.
3. Take F = G/(s − ρ₀)^m, with m the order of ρ₀ as a zero of G. Then F ∈ ℬ, F(ρ₀) ≠ 0, and F vanishes on Z \ {ρ₀}. So c_{ρ₀} = 0. ∎

HBW8.9–8.12 is this lemma for the Gaussian-weighted zeta divisor. HSR4.1 reduces to it after NHI's Jensen and differentiation step. The lemma needs G ≢ 0, so that the order of each ρ₀ is defined.

## 5. Negative results (goal 1)

- **32.N1. Conditions equivalent to RH by construction.** Each says only that there are no off-line zeros:
  - D_{r,t} = 0 (equivalently Ξ = 0, Γ = 0, 𝓡 = 0, S_{O,t} = 0);
  - HBW8.9's singularity-class map vanishes on H;
  - n^{−1/2}A_n is unitary on D_{r,t} (HSR7.4);
  - reflection commutes with the regularising inclusion (HSRA8; the factor has modulus e^{Δ(2σ−1)});
  - every counting modulus equals n^{1/2} (HBW5–HBW6);
  - every monodromy phase e^{−2πiβ} equals −1;
  - D_{r,t} ⊂ H². This one is derived: for an off-line pair one member has Re ρ > ½, and then K_{1−ρ} ∉ H² (C23). This is consistent with HSR leaving H² and with ABH working on H₋ only; ABH's restriction follows from ABH1.2.
- **32.N2. A zero-set condition weaker than RH.** D_{r,t₂} = D_{r,t₁} iff the off-line set is finite. This is implied by RH. I make no claim about its status.
- **32.N3. Statements that hold unconditionally and therefore cannot distinguish RH from its failure:**
  - NHI5.4 and NHI8.4, which hold on all of ℬ′, independently of I;
  - the injectivity results HSR4.1 and HSR6;
  - the positivity of HSR5, which is ℓ² positivity;
  - the Schatten-class result HSR10.6;
  - HBW3 and HBW8, which use nothing about the positions of the zeros inside the strip. HBW3 uses 0 < Re s < 1; HBW8 uses the isolators, Gaussian summability and a lower bound on |1 − ρ|;
  - the winding/Gaussian exchange of HBW9.
- **32.N4. Cancellations that leave a remainder.**
  - Cover covariance W_n*H = HU_n′ holds only on I^⊥. On ℬ′ it leaves conj(λ(δ_{n,t}))/(1 − z) (C08).
  - HSR7.4 leaves ΞD_nΞ^{−1}.
  - HSRA8.2 leaves e^{−Δ}B_{e^{2Δ}}.
  - HBW9.3 leaves two holomorphic remainders.
  - In HBW2.2 the 8F₀ correction survives as a simple pole in u once j ≥ m_ρ (C10b).
  - In NHI8 no remainder survives, even in ℬ′ (Lemma 32.1 with C(1) = 1). NHI8's own proof removes it through F₀ ∈ I. For C(1) = 0 the remainder ℂ·ev₁ survives in ℬ′ and is removed in Q because ev₁(g_tF₀) = e^t/8 ≠ 0.
- **The price of changing receiver.** Moving from H² (ABH, on H₋) to 𝒪(𝔻) (HSR, on all off-line coordinates) exchanges the Hardy norm, which has off-diagonal Gram terms, for a transported diagonal ℓ² norm. That norm carries no information about where the zeros are.

## 6. Relations to blocks audited earlier (goal 2)

- **NHJ, NCI (`16_`).**
  - NHI5.4 = NHJ4.6 ∘ q′, and NHI6.1 = q(NHJ4.7).
  - NHI3 is NCI3's Jensen step.
  - The discrepancy in NHI6.2 and HSR7.1 is NCI's δ_{n,t}, whose closed span is I (NCI5.2).
- **ABH (`30_`).** ABH3.2 is HSR3.5 restricted to H₋. The correspondence uses the reindexing λ = ρ#, g_λ = K_{λ̄} and conj(g_t(λ)) = e^{t(1−ρ)²}. Also:
  - ABH's covariance W_n*𝓛 = 𝓛T_n is HSR7.2 restricted to H₋;
  - ABH1.4 is HBW4's global eigen-relation.
- **GDE (`30_`).** HSR7.5 repeats GDE7's cover relations, and HSR10.5's singular values are the moduli of GDE's Gaussian diagonal at ρ#.
- **AST (`24_`).** HSR1 uses AST1–AST4, and HSR10.1–10.2 is AST6; the exact range is Lemma 24.5.
- **NPE (`31_`).** HBW4.5 and HBW5.1 give the counting action n^{1−s}exp(−(log n)N) on jets. At s = 0 with jet length 2 it has the same matrix as NPE4.2, the Jordan block of `31_` Lemma 31.2(b); only the matrices coincide.
- **A reflection pair.** The only possible tail annihilator of a corrected family is a multiple of ev₁ (s = 1, where U_n′ev₁ = ev₁); for the programme's C = 8F₀ there is none. `31_` Lemma 31.2's surviving extension sits at s = 0. These are the two endpoints exchanged by s ↦ 1 − s.

## 7. Not checked

- GSP4.3–4.7, AST's reflexivity and strictness results, and the ADC endpoint characters used in HSR9.
- `HBWR_TYPOGRAPHY_CORRECTION.json`: not staged (see §0).
- Noor's paper itself (cited as in `30_`).

## Revision after the eleventh referee pass (applied at 15:33 UTC)

One referee (a Claude subagent) read `32_`–`33_`. It re-ran the three check scripts, whose outputs reproduced byte for byte, and wrote nine further checks of its own, all OK. Lemmas 32.1 and 32.2 are correct; Lemma 32.2 needed the hypothesis G ≢ 0. Applied to this note:

- **Major.** 32.N4 said the NHI8 remainder is removed only because ev₁ ∉ I^⊥. That contradicted Lemma 32.1: with C = 8F₀ no remainder survives even in ℬ′. Corrected.
- **Minor.**
  - The verdict now excepts 32.N2 (finitely many off-line zeros), a location condition weaker than RH.
  - NHIR's remark: the nonvanishing of F₀(1), not the value 1/8, is essential, with the one-line reason for ev₁ ∉ I^⊥.
  - The reflection-pair bridge now says the only possible tail annihilator is a multiple of ev₁, and none exists for C = 8F₀.
  - Credit for the case M = 0 goes to NHJ4 and `30_` Corollary 30.2.
  - Lemma 32.2 needs G ≢ 0. HBW8.9–8.12, not HSR4.1, is literally the lemma.
  - §0: the section references and the provenance of §5 were corrected, and a reference to a private location was removed.
  - 32.N3: HBW3 and HBW8 are described exactly. 32.N1's "this is why" became "consistent with".
  - The bridges to NPE4.2 now say "has the same matrix as".
  - Notation (b_{a,N}, σ) and the precision figure (10⁻³⁷) were corrected.
