# The division estimate and the global residue duality: an audit of OMS and GZR, with CGS and DCP read in part

Claude (claude-ab lane), model `claude-opus-5-5` (Opus 5.5) at maximum reasoning effort. 25 September 2026, 11:31 UTC. Board task 8, part 3: the character-lifting side.

**Sources.** All blocks are in the zeta-function-research-reader repository at commit 064f33b, folder `…/20260924-cohomology-weight-and-character-lifts/original-character-lifting/tau_lifting_weights_20260924/`.
- **Read in full:** GZR0–GZR9, `GLOBAL_ORIGINAL_ZETA_RESIDUE_DUALITY_INDEPENDENT.md`, including its closing continuation paragraph.
- **Read in full for the analytic parts:** OMS0–OMS4 and OMS8, `ORIGINAL_MELLIN_SPECTRAL_SYNTHESIS.md`. OMS3 was read after the eighth referee pass asked for it.
- **Not re-read:** OMS5–OMS7A. They transport SSI's exact image to the CW quotient and to the adelic periodization complex. SSI itself is audited in `25_`.
- **Read in part:** CGS0–CGS3 (`SOURCE_COEFFICIENT_GLUE.md`) and DCP0–DCP3 (`SOURCE_CC_DOUBLE_PULLBACK.md`).

**Checks.** `checks/oms_gzr_audit_checks.py` has 8 items, and all pass; the output is in `checks/oms_gzr_audit_checks_OUTPUT.txt`.

## 0. Summary

1. **OMS's division estimate is correct.**
   - For F ∈ I, the entire quotient F/F_* satisfies |F/F_*| ≤ C exp(C(|t|+2)^{3/2}log(|t|+2)) on every vertical strip.
   - The proof goes through Hadamard's product and a minimum-modulus bound off small discs. Every step checks.
   - OMS4 identifies the two rapid-division conditions of Meyer's range theorem and proves both. So `25_` Lemma 25.1 (the exact summation image) is, on the programme's account, Meyer's range theorem made explicit, with the division estimate supplied.
2. **GZR is correct.**
   - The pairing B_ζ(F, G) = (2πi)^{−1}(∫_{Re s=2} − ∫_{Re s=−1}) F(s)G(1−s)/ζ(s) ds is a continuous, nondegenerate bilinear form on Q = B/I.
   - It pairs the jets at ρ with the jets at 1 − ρ through an explicit local form of determinant (m!/ζ^{(m)}(ρ))^m.
   - It is a similitude of factor a for T_a, and it reflects L into 1 − L.
   - GZR states itself that it gives no positive form and no estimate forcing Re ρ = ½ (GZR9).
3. **CGS and DCP, as far as read, are standard constructions, correctly carried out.**
   - CGS classifies sheaves on the programme's source space X = Spec ℤ ∪ {𝔪} by gluing data (𝒢, A₊, A₋, r). This is the recollement recalled in Deligne's Weil II §3.4.8, which CGS credits, split by the receiving idempotent ε.
   - DCP glues two copies of X along Spec ℤ and maps the result continuously onto Connes–Consani's three-point base.
4. **Lemma extracted: 26.1, the global residue duality, with explicit constants.**

## 1. OMS: the division estimate and the comparison with Meyer

### 1.1 Audit of OMS1–OMS2

1. **The Mellin isomorphism (OMS1.3).** For every real c,
   K(x) = (2π)^{−1}∫F(½+it)e^{−itx}dt = e^{−(c−½)x}(2π)^{−1}∫F(c+it)e^{−itx}dt,
   by contour shifting. With c = ½ ± (N+1) this gives the weighted inverse estimates.
2. **The comparison with Meyer's normalisation (OMS1.4–1.5).** The maps T₀k = u^{−1/2}k and Σ = 2T₀ℰ, and the equality of the Fourier phases on even functions, are direct substitutions.
3. **The source vector (OMS2.3).**
   - f_* is its own Fourier transform: from the two Gaussian moment transforms (check 6).
   - So k_* = ℰf_* satisfies k_*(u) = k_*(1/u) (check 6).
   - F_* = s(s−1)/8·π^{−s/2}Γ(s/2)ζ(s), as in `24_` check 4.
4. **Hadamard's product (OMS2.6–2.7).**
   - log max_{|s|≤R}|F_*| ≤ C(R+2)log(R+2).
   - Jensen's formula at radius 2R then bounds the number of zeros, with multiplicity: n(R) ≤ C(R+2)^{3/2}. (Jensen in fact gives O(R log R); OMS uses the weaker bound, which suffices.)
   - Genus 1, e^a = 1/8, and b = F_*′(0)/F_*(0) = ½log(4π) − 1 − γ/2 = −0.0230957… (check 5).
5. **The minimum modulus (OMS2.8).**
   - Put discs of radius R^{−2} around the zeros with |ρ| ≤ 8R. Their total radius is O(R^{−1/2}), so every connected union of discs has diameter below 1.
   - Outside the discs, for R/2 ≤ |s| ≤ 3R:
     - the finite factors satisfy |1 − s/ρ| ≥ (8R³)^{−1};
     - the finite exponentials cost at most CR^{3/2}, because Σ_{|ρ|≤8R}|ρ|^{−1} = O(R^{1/2});
     - the tail |s/ρ| ≤ 3/8 costs at most CR^{3/2}, because log|(1−w)e^w| ≥ −(4/5)|w|² for |w| ≤ 3/8. OMS states the weaker constant −8/5, which also suffices.
   - Hence |F_*| ≥ e^{−CR^{3/2}log R} outside the discs.
   - The maximum principle on each disc cluster, whose boundary stays in |Re s| ≤ A + 1, then bounds F/F_* inside the cluster.
6. **The rapid division (OMS3).**
   - H = F/ζ has only simple poles at −2r, with residue F(−2r)/ζ′(−2r); H(0) = −2F(0), H(1) = 0 and H′(1) = F(1) (OMS3.1–3.3).
   - On the right edge Re s = b ≥ 2, |1/ζ| ≤ ζ(b).
   - On the left edge Re s = −2N−1, OMS3.6 is SSI3.7 (`25_` check 1). Each quadratic factor is at least (1+|t|)²/8, and y coth(πy) ≥ (1+|t|)/(2π). These give |1/ζ(−2N−1+it)| ≤ ζ(2N+2)√(2·8^{2N+1})π^{2N+2}(1+|t|)^{−2N−3/2} (OMS3.7). I re-derived the constant.
   - The maximum principle for e^{εs²}(s+2N+2)^M P_N(s)H(s) on rectangles removes the horizontal edges, because the growth is subquadratic by (OMS2.8), and then ε → 0. This is OMS3.8, the same argument as SSI4.
   - The contour shifts give the Schwartz source f_F with f_F^{(2r)}(0)/(2r)! = F(−2r)/ζ′(−2r) (OMS3.12). This is SSI5.6 in the centred normalisation, where the factor 2 of SSI is absorbed.
7. **Meyer's criterion (OMS4).**
   - Combined with the edge bounds and the maximum principle of OMS3, the estimate makes F/ζ Schwartz on every line σ ≥ ½.
   - The reflected function F^♯(s) = F(1−s) lies in I, because the functional equation preserves every multiplicity. So F(σ+it)/ζ(1−σ−it) = F^♯(w)/ζ(w), with w = 1−σ−it, is Schwartz for σ ≤ ½.
   - These are the two conditions OMS0 reports from Meyer's range theorem.
8. **Poisson with both endpoint terms (OMS4.3).** f(0)/2 + Zf(u) = u^{−1}Zf̂(u^{−1}) + f̂(0)/(2u) (check 7).

**Verdict.** OMS0–OMS4 and OMS8 are correct. The attribution to Meyer (arXiv:math/0412277) is the programme's reading of Meyer's text (OMS0: "lines 225–738 were read"); I have not read Meyer. The subquadratic exponent 3/2 is crude but sufficient: the Gaussian damping e^{εs²} in SSI4 beats any growth of the form exp(C|t|^{2−δ}).

## 2. GZR: the global residue duality

### 2.1 Audit

1. **The pairing and its bound (GZR2).**
   - On Re s = 2, |1/ζ| ≤ ζ(2).
   - On Re s = −1, |χ(−1+it)|² = π^{−3}y coth(πy)(y² + ¼), with y = t/2 (check 2). This follows from Γ(−½+iy) = Γ(½+iy)/(−½+iy), |Γ(1−iy)|² = πy/sinh(πy) and |Γ(½+iy)|² = π/cosh(πy).
   - Two elementary inequalities hold. The first, y² + ¼ ≥ (1+|t|)²/8, is (|t|−1)² ≥ 0. The second, y coth(πy) ≥ (1+|t|)/(2π), follows from x coth x ≥ max(1, x) ≥ (1 + 2x/π)/2 with x = π|y|.
   - Together they give |1/ζ(−1+it)| ≤ 4π²ζ(2)(1+|t|)^{−3/2}. Check 2 finds the ratio to this bound at most 0.444 on 109 distinct points in (0, 400]. The same bound was used in `20_` (GZR2).
   - So |B_ζ(F,G)| ≤ C_ζ b_{2,1}(F)b_{2,1}(G), with C_ζ = ζ(2)(1+4π²)/π ≈ 21.19.
   - This constant is valid but crude. Keeping the factor (1+|t|)^{−3/2} on the left edge gives (2π)^{−1}·4π²ζ(2)·2∫_0^∞(1+t)^{−7/2}dt = (8π/5)ζ(2) there, so the total is ζ(2)(1/π + 8π/5) ≈ 8.79 (the eighth referee pass).
2. **Descent (GZR3).** If F ∈ I, then F/ζ is holomorphic and rapidly decreasing on the closed strip −1 ≤ Re s ≤ 2, by OMS3. The rectangle's horizontal sides tend to zero, so B_ζ(F, G) = 0. The same holds if G ∈ I, because the reflection R preserves I.
3. **The local form (GZR4).**
   - The residue at ρ of F(s)G(1−s)/ζ(s) is Σ_{i+j+k=m−1} F^{(i)}(ρ)/i! · G^{(j)}(1−ρ)/j! · (−1)^j c_{ρ,k}, where the c_{ρ,k} are the Taylor coefficients of u_ρ^{−1}.
   - Check 4 confirms this for m = 1, 2, 3 against a numerical contour integral, for a synthetic function with a zero of order m.
   - The matrix is anti-triangular, and its determinant is c_{ρ,0}^m = (m!/ζ^{(m)}(ρ))^m (check 3, random data, m ≤ 6). For m = 2: c₀ = 2/ζ″(ρ) and c₁ = −2ζ‴(ρ)/(3ζ″(ρ)²).
4. **The finite-residue theorem (GZR5.8).**
   - If F(s)G(1−s)/ζ(s) has poles at only finitely many zeros S₀, then H = P_{S₀}·F·(G∘R) ∈ I. So H/ζ is rapidly decreasing on the strip.
   - Dividing by the polynomial P_{S₀} leaves the horizontal sides negligible. B_ζ is then the finite sum of residues.
5. **Nondegeneracy (GZR6).**
   - Let ℓ be the least index with a nonzero Taylor coefficient of F at ρ. Testing against the isolator E_{1−ρ, m−1−ℓ} gives the single term (−1)^{m−1−ℓ}f_ℓc_{ρ,0} ≠ 0.
   - So both radicals of B_ζ on B are exactly I.
6. **The actions (GZR7).**
   - a^s·a^{1−s} = a gives B_ζ(T_ax, T_ay) = aB_ζ(x, y).
   - s·F(s)G(1−s) = F(s)·[(1 − (1−s))G(1−s)] gives B_ζ(Lx, y) = B_ζ(x, (1−L)y) (check 8).
   - The orientation computation B_ζ(y, x) = −B_{ζ∨}(x, y) follows from substituting w = 1 − s in both edges.
7. **The trivial-zero derivatives (GZR1.7).** ζ′(−2r) = (−1)^r2^{−2r−1}π^{−2r}(2r)!ζ(1+2r) (check 1).

**Verdict.** GZR is correct.

The closing paragraph of GZR reports, from PGD and DPL (not read here), that the algebraic cokernel of Q → Q′ is nonzero. It contains the explicit nonzero class c_ζ of the functional G ↦ 𝔅_ζ(1, G); DPL calls it a cokernel generator in the module sense. This is consistent with a direct argument:
- a representing class would need a rapidly decreasing entire function equal to 1 to full order at every zero;
- the zero heights are unbounded, so no such function exists;
- this is the argument of ECR1 (`25_` §4.1 item 1).

### 2.2 Lemma 26.1 (global residue duality, with explicit constants)

**Setting.** For F, G ∈ B put
B_ζ(F, G) = (2πi)^{−1}(∫_{2−i∞}^{2+i∞} − ∫_{−1−i∞}^{−1+i∞}) F(s)G(1−s)/ζ(s) ds.

**Statement.**
- (a) |B_ζ(F,G)| ≤ (ζ(2)(1+4π²)/π)·b_{2,1}(F)·b_{2,1}(G).
- (b) B_ζ vanishes when either argument lies in I, and it descends to a jointly continuous form on Q = B/I.
- (c) On Q it is nondegenerate on both sides. The primary block at ρ pairs only with the block at 1 − ρ, through the local form (GZR4.5). In the bases (F^{(i)}(ρ)/i!)_{i<m} and (G^{(j)}(1−ρ)/j!)_{j<m}, its determinant is (m_ρ!/ζ^{(m_ρ)}(ρ))^{m_ρ}.
- (d) B_ζ(T_ax, T_ay) = aB_ζ(x, y) for a > 0, and B_ζ(P(L)x, y) = B_ζ(x, P(1−L)y) for every polynomial P.
- (e) B_ζ is not asserted to be symmetric, Hermitian or positive, and it does not locate the zeros.

*Proof.* GZR2–GZR7, audited in §2.1. The one analytic input from outside GZR is the rapid division on the strip −1 ≤ Re s ≤ 2 (OMS3; `25_` Lemma 25.1). ∎

**What it is.** This is the programme's form of the classical residue pairing behind the explicit formula. It is defined as a convergent contour difference, not as a sum over zeros. The factor a in (d) is the degree-1 similitude, which ECI (`25_` §4) distinguishes from the normal factor a³.

## 3. CGS and DCP (read in part)

**CGS (CGS0–CGS3).** A sheaf of ℛ-modules on X = Spec ℤ ∪ {𝔪} is the same thing as a datum (𝒢, A₊, A₋, r: A₊ → Γ(U, 𝒢)). Here 𝔪 has X as its only open neighbourhood, and ℛ(X) = ℤ[ε]/(ε² − ε).
- The inverse functors are explicit.
- Covers of X contain X, so the sheaf condition at 𝔪 is automatic.
- Kernels and cokernels are computed componentwise, with Γ(U, coker g) kept distinct from coker Γ(U, g).
- The ε = 0 part splits off: ℳ ≅ ℳ(𝒢, A₊, 0, r) ⊕ i_*A₋.
- This is the recollement of an open set and its closed complement, recalled by Deligne (Weil II, §3.4.8, which CGS cites). The only programme-specific ingredient is the idempotent ε.
- I checked CGS1.2–1.5, CGS2.1–2.2 and CGS3.1–3.5. They are correct.

**DCP (DCP0–DCP3).**
- The doubled space X^dbl = Spec ℤ ∪ {𝔪₊, 𝔪₋} has as opens exactly the opens of Spec ℤ, the two charts X₊ and X₋, and X^dbl.
- The ring of global sections is ℤ³, with idempotents ε, e₊ and e₋.
- The map f to Connes–Consani's base Y = {x₊, η, x₋} is continuous: the preimages of ∅, {η}, Y₊, Y₋ and Y are ∅, Spec ℤ, X₊, X₋ and X^dbl.
- The source map [n] = nε, [τ] = (1,1,1) is injective and multiplicative, and it sends τ to the unit.
- The rest of DCP (DCP4–DCP12) computes inverse and direct images on this finite model and was not read.

## 4. Items for the goals

- **Goal 3 (standalone lemmas).**
  - Lemma 26.1, the global residue duality with explicit constants.
  - The division estimate |F/F_*| ≤ C exp(C(|t|+2)^{3/2}log(|t|+2)) for F ∈ I (OMS2.8), with the proof audited here.
- **Goal 1 (negative results).**
  - The global duality is nondegenerate but carries no positivity (GZR9).
  - Its algebraic cokernel is nonzero. Lifting c_ζ would need F ∈ B with F ≡ 1 to full order at every zero, which rapid decay on strips and the unbounded zero heights exclude.
  - Together with `25_` §5, this closes the audit of the analytic side of the three-lane edition's positive and dual constructions: each is correct, and none contains a mechanism for Re ρ = ½.
- **Verification line of the register.** The literature comparison of S12–S13 with Meyer is narrowed. On the programme's reading (OMS0–OMS4), the exact image is Meyer's range theorem with the division estimate supplied. What remains is to read Meyer's two theorems themselves.
- **Reading status.**
  - Read in full or in the needed part: GZR, OMS, CGS and DCP.
  - Remaining in board task 8: the rest of the Deligne reader, the Codex session logs, and board task 2 part 2 (cross-programme bridges).

## 5. Checks (`checks/oms_gzr_audit_checks.py`, mpmath at 40 digits)

| # | Statement | Result |
|---|---|---|
| 1 | GZR1.7: ζ′(−2r) = (−1)^r2^{−2r−1}π^{−2r}(2r)!ζ(1+2r), r ≤ 5 | relative error ≤ 3·10⁻⁴¹ |
| 2 | GZR2.3 closed form of \|χ(−1+it)\|²; GZR2.4 bound on \|1/ζ(−1+it)\| on 109 distinct points in (0, 400] | ratio to the bound ≤ 0.444 |
| 3 | GZR4.2 reciprocal recursion; GZR4.7 det M_ρ = c₀^m, m ≤ 6, random data | error ≤ 3·10⁻³⁹ |
| 4 | GZR4.3 residue formula against a contour integral, m = 1, 2, 3 | relative error ≤ 2·10⁻⁴¹ |
| 5 | OMS2.7: F_*′(0)/F_*(0) = ½log(4π) − 1 − γ/2 = −0.0230957… | difference quotient agrees to 5·10⁻²⁸ |
| 6 | OMS2.3: f_* is Fourier self-dual; k_*(u) = k_*(1/u) | error ≤ 6·10⁻⁴² |
| 7 | OMS4.3: Poisson with both endpoint terms | error ≤ 2·10⁻⁴¹ |
| 8 | GZR7.2–7.3 integrand identities | error ≤ 6·10⁻³⁹ |

## 6. Sources

- The programme blocks listed at the top (commit 064f33b).
- R. Meyer, *A spectral interpretation for the zeros of the Riemann zeta function*, Göttingen Seminars Winter Term 2004/2005, 117–137 (arXiv:math/0412277). Cited through OMS0 and OMS4 only; not read by me.
- P. Deligne, *La conjecture de Weil. II*, Publ. Math. IHÉS 52 (1980), §3.4.8. Cited through CGS1; not re-read.

## 7. Revisions after the eighth referee pass (11:53 UTC)

1. §1.1: OMS3, the edge bounds and the Phragmén–Lindelöf step that make F/ζ Schwartz, was read and audited (new item 6). The constant of OMS3.7 was re-derived.
2. §2.1 and §4: the cokernel "contains the explicit nonzero class c_ζ"; it is no longer said to be "spanned by" it. The garbled sentence in §4 is rewritten.
3. Lemma 26.1(c) names the bases in which the determinant is computed. §2.1 records the sharper constant ζ(2)(1/π + 8π/5) ≈ 8.79. Check 2 uses 109 distinct points.
