# Addendum to the published zeta reader: four corrections, the first jet on every sheet, a Carleman density criterion, and other understatements

Claude (claude-ab lane), model `claude-opus-5-5` (Opus 5.5) at maximum reasoning effort. 26 September 2026, 10:46 UTC.

**What this note is.** The zeta reader, *The split-zero programme around the Riemann zeta function: a reader of its results, with proofs*, is published on Zenodo as version 10.5281/zenodo.22970703. It was refereed for errors and overstatement before publication. On 26 September the owner asked that reviews also look for understatement and missed generality. This note records the outcome of such a review of the published reader, for a later version. The published version is not changed; Zenodo versions are additive.

**How it was made.**
1. An independent Claude instance, which wrote neither the reader nor the notes, reviewed the reader in both directions. Its report and its ten check scripts are in `checks/zeta_reader_review/` (the report: `UNDERSTATEMENT_REPORT_ZETA_READER.md`). It gives 5 major findings (F1–F5), 17 minor ones (F6–F22) and 4 overclaims or gaps (O1–O4).
2. I verified O1–O4 and F1–F5 myself against the reader's sources and the notes, re-deriving each proof below, and wrote my own checks (`checks/zeta_reader_addendum_checks.py`, items Z1–Z6, all pass).
3. A second independent Claude instance verified F6–F22 (`checks/zeta_reader_review/verify_minors/VERIFY_MINORS_REPORT.md`, eleven scripts of its own, all pass): 11 confirmed, 6 confirmed with a correction, none rejected. §3 records its verdicts, with its corrections applied.

Nothing here bears on the truth of RH. τ is not identified with any zero.

## 0. Summary

| # | Reader location | Kind | Result |
|---|---|---|---|
| O1 | Prop. 5.2 | correction | For an on-line zero the four points ρ, ρ̄, 1−ρ, 1−ρ̄ are two; the rank is 2m and the determinant p^m. The conclusion (average weight 1) stands. |
| O2 | Cor. 2.2 | correction | The Euler product is that of the normalised sheet a^sζ(s, a); ζ(s, ½) itself is 2^s∏_{p>2}(1 − p^{−s})^{−1}. |
| O3 | note `02_` §4.2 | correction (source note) | "Both errors tend to 0" also needs T₁/Δ → ∞ (e.g. T₁ ≥ 4Δ√(log Δ)). |
| O4 | Prop. 3.11, outline | gap filled | The last step needs the density of g_tℬ in ℬ; a two-line proof is given in §2.3. |
| F1 | Thm 4.1 | generalisation | On every sheet a > 0: ∂_aζ(s, a) = −sζ(s+1, a) has zero divisor exactly div ζ(·, a) − 1, and value −1 at s = 0. |
| F2 | Lemma 3.13 | generalisation | Every bounded Hermitian form compatible with the scaling transfer for n = 2 and 3 is Σ_ρ b_ρ m_ρ x_ρ ȳ_{ρ#}; positivity holds iff b vanishes off the line and is ≥ 0 on it. |
| F3 | Prop. 3.11; open question 5 | new theorem | A Carleman-formula criterion for density; for S = {2^a3^b} the families are dense for every t > (log 2)(log 3)/(2π) ≈ 0.1212. Open question 5 is answered for those t. |
| F4 | Thm 2.3, Cor. 2.4 | generalisation | r_n = 1 − j + ε at every element whose proper M-divisors factor uniquely: infinitely many negative coefficients located, with values. |
| F5 | Prop. 5.1 | generalisation | The abscissa is 1 + kβ_max for every k ≥ 1 and every finite S; positivity only makes the real point a pole. |
| F6–F22 | various | 17 minor | §3. |

## 1. Corrections

**O1 (Prop. 5.2, the determinant weight).** The reader says that on the span V_ρ of the jet blocks of ρ, ρ̄, 1 − ρ, 1 − ρ̄ (each of multiplicity m) the determinant of W_p is p^{2m} and the rank 4m. That holds when ρ is off the line. If Re ρ = ½, then 1 − ρ = ρ̄ and 1 − ρ̄ = ρ, so V_ρ is the span of the blocks of ρ and ρ̄: rank 2m, eigenvalues p^ρ and p^{ρ̄} with multiplicity m each, determinant p^{m(ρ+ρ̄)} = p^m. In both cases the weight of the determinant (2 log|det|/log p) divided by the rank is 1. *Corrected wording:* "If ρ is off the line, the four points are distinct, V_ρ has rank 4m and det(W_p | V_ρ) = p^{2m}; if ρ is on the line, V_ρ is the span of the blocks of ρ and ρ̄, of rank 2m, and det = p^m. In both cases the average weight is 1, whatever Re ρ is." *Check:* Z6.

**O2 (Cor. 2.2, only two sheets are Eulerian).** The reader says that ζ(s, 1 + t) has an Euler product with local factors (1 − P^{−s})^{−1} only for t ∈ {0, −½}. At t = −½, ζ(s, ½) = Σ_{n≥0}(n + ½)^{−s} = 2^s Σ_{n odd} n^{−s} = 2^s(1 − 2^{−s})ζ(s) = 2^s∏_{p>2}(1 − p^{−s})^{−1}; so the Euler product is that of 2^{−s}ζ(s, ½). *Corrected wording:* "The normalised sheet a^sζ(s, a), a = 1 + t, has an Euler product with local factors of Euler type (1 − P^{−s})^{−1} only for a ∈ {1, ½}." This is the normalisation under which Theorem E is stated.

**O3 (note `02_` §4.2, Corollary B, not in the reader).** The error term of Corollary B contains O(e^{−πT₁/2} + T₁e^{−T₁²/(8Δ²)}), which the consequence line "if Δ ≥ (1 + δ)√(2 log T₂)/log 2, both errors tend to 0" omits. With T₁ = 10Δ the term is 10Δe^{−12.5}, which grows with Δ. It tends to 0 if T₁/Δ → ∞, for example T₁ ≥ 4Δ√(log Δ): then T₁²/(8Δ²) ≥ 2 log Δ and T₁e^{−T₁²/(8Δ²)} ≤ 4√(log Δ)/Δ (the function x ↦ xe^{−x²/(8Δ²)} decreases for x > 2Δ). This also assumes, as `02_` does not say explicitly, that the O-constants of §4.2 do not depend on Δ. *Corrected consequence:* "If Δ ≥ (1 + δ)√(2 log T₂)/log 2 and T₁ ≥ max(10Δ, 4Δ√(log Δ)), both errors tend to 0 (with the O-constants of the displayed bound independent of Δ)."

**O4 (Prop. 3.11, the outline).** The outline ends: the identity (∂_w − 1)K_w = g_te^{(1−s)w} gives Λ(g_te^{vs}) = 0 for all v, "and the half-Mellin representation extends this to Λ = 0". As written this gives Λ(g_tG) = 0 for G ∈ ℬ, that is, Λ = 0 on g_tℬ. The missing step is that g_tℬ is dense in ℬ; it is proved in §2.3, step 4. The audit note `16_` read this step (the programme's regularisation removal, NHJ4) only through its displayed result.

## 2. Stronger statements (the five major findings)

### 2.1 The first Hurwitz jet on every sheet (F1; reader Thm 4.1)

**Statement.** For every a > 0 and every m ≥ 1:
- (a′) ∂_a^mζ(s, a) = (−1)^m(s)_mζ(s + m, a) for s ≠ 1 − m, and the right side extends to an entire function;
- (b′) sζ(s + 1, a) is entire with value 1 at s = 0, so the first a-jet equals −1 at s = 0;
- (c′) the zero divisor of the first jet −sζ(s + 1, a) is exactly div ζ(·, a) − 1, with multiplicities and in the whole plane; the zero divisor of the m-th jet is (div ζ(·, a) − m) + [0] + [−1] + … + [2 − m], the last m − 1 zeros being simple and distinct from the shifted ones.

At a = 1, div ζ = Z + Σ_{k≥1}[−2k], so the first jet has divisor (Z − 1) + Σ_{k≥1}[−2k − 1]; the reader's (c) is the part of this in −1 < Re s < 0. Part (d) of the reader's theorem ("ζ has no zero on Z − 1") and Theorem 4.2 use the functional equation of ζ and do not extend: at a = ½, s₁ = 2πi/log 2 is a zero of ζ(s, ½) = (2^s − 1)ζ(s), while ζ(1 − s̄₁, ½) = (2·2^{2πi/log 2} − 1)ζ(1 + 2πi/log 2) = ζ(1 + 2πi/log 2) ≠ 0; so the zero set of that sheet is not symmetric under s ↦ 1 − s̄.

**Proof.** (a′) The reader's proof is already written for every a: termwise differentiation on Re s > 1 and joint analyticity of ζ(s, a) in (s, a) on {s ≠ 1} × {Re a > 0}. The factor (s)_m vanishes simply at 1 − m, where ζ(s + m, a) has a simple pole; so the product extends holomorphically there. (b′) ζ(s, a) − 1/(s − 1) is entire for every a > 0 (residue 1 at s = 1), so sζ(s + 1, a) = 1 + s·(entire). (c′) For s ≠ 0 the factor −s is locally a nonvanishing constant times a unit, so the zeros of −sζ(s + 1, a) off s = 0 are exactly the s with s + 1 a zero of ζ(·, a), with the same orders; at s = 0 the value is −1. For the m-th jet, (s)_m vanishes simply at 0, −1, …, 1 − m; at 1 − m the pole cancels as in (a′); at −j with 0 ≤ j ≤ m − 2 the value ζ(m − j, a) = Σ_{n≥0}(n + a)^{−(m−j)} is a convergent sum of positive terms, so these zeros are simple and are not shifted zeros of ζ(·, a). ∎

*Status:* proved here. *Check:* Z1 (the identity on four sheets to 10⁻³⁰; the jet vanishes at s₀ − 1 for the zero s₀ = 1.40778804 + 23.32798775i of ζ(·, 2); sζ(s + 1, a) → 1 at s = 0), and the reviewer's `check_hurwitz_jet_all_sheets.py`.

*What it says for the programme.* The Hurwitz flow ζ(s, 1 + t) does not translate its zero set, but at every time t its first jet in t vanishes exactly on the zero set of that time translated by −1. The statement at t = 0 in the reader is the first instance of a statement that holds along the whole flow.

### 2.2 Transfer-compatible forms (F2; reader Lemma 3.13)

On H = ℓ²(Z, m) with (T_nx)_ρ = n^ρx_ρ, write ρ^# = 1 − ρ̄, and let ε_ρ be the coordinate vectors, ‖ε_ρ‖² = m_ρ.

**Statement.** Let B be a bounded Hermitian form on H with B(T_nx, T_ny) = nB(x, y) for n = 2 and n = 3. Then B(x, y) = Σ_ρ b_ρm_ρx_ρ\overline{y_{ρ^#}} with |b_ρ| ≤ ‖B‖ and b_{ρ^#} = \overline{b_ρ}; conversely every such form satisfies the relation for every real n > 0. B is positive semidefinite if and only if b_ρ = 0 at every zero off the line and b_ρ ≥ 0 on the line. The pair {2, 3} may be replaced by any n₁, n₂ > 1 with log n₁/log n₂ irrational; one value of n does not suffice if two points of the support differ by a nonzero multiple of 2πi/log n.

The reader's Lemma 3.13 is the positive case, with the hypothesis for all n ≥ 1. The case b ≡ 1 is the pairing Σ_ρ m_ρx_ρ\overline{y_{ρ^#}}, whose diagonal is Weil's pairing Ω of the reader's Proposition 4.6; the classification shows that positivity is exactly what removes the off-line blocks.

**Proof.** On coordinate vectors, B(T_nε_ρ, T_nε_η) = n^{ρ+η̄}B(ε_ρ, ε_η), so the relation reads (n^{ρ+η̄−1} − 1)B(ε_ρ, ε_η) = 0. If the entry is nonzero for n = 2 and n = 3, then ρ + η̄ − 1 lies in (2πi/log 2)ℤ ∩ (2πi/log 3)ℤ, which is {0} because 3^k = 2^l forces k = l = 0. So Re η = 1 − Re ρ and Im η = Im ρ, that is η = ρ^#. Boundedness gives B(x, y) = lim B(x_N, y_N) over finite truncations, hence the displayed sum with b_ρ = B(ε_ρ, ε_{ρ^#})/m_ρ, |b_ρ| ≤ ‖B‖‖ε_ρ‖‖ε_{ρ^#}‖/m_ρ = ‖B‖ (m_{ρ^#} = m_ρ); Hermitian symmetry gives b_{ρ^#} = \overline{b_ρ}. Conversely ρ + \overline{ρ^#} = ρ + 1 − ρ = 1, so every such form satisfies the relation for every n > 0. Positivity: an on-line zero contributes b_ρm_ρ|x_ρ|², which needs b_ρ ≥ 0; an off-line pair {ρ, ρ^#} contributes 2m_ρRe(b_ρx_ρ\overline{x_{ρ^#}}), a hyperbolic form with eigenvalues ±m_ρ|b_ρ|, which is ≥ 0 only if b_ρ = 0. ∎

*Status:* proved here. *Check:* Z2 (on a synthetic #- and conjugation-stable configuration, n ∈ {2, 3} admits exactly the ten entries (ρ, ρ^#), four of them off the diagonal; n = 2 alone admits two more), and the reviewer's `check_transfer_forms.py`.

### 2.3 A Carleman density criterion (F3; reader Prop. 3.11 and open question 5)

Fix t > 0, put g_t(s) = e^{ts²}, and for S ⊂ {2, 3, …} let 𝒩_S = span{g_t(s)(n − n^{1−s})/s : n ∈ S} and ν_S(x) = #{n ∈ S : log n ≤ x}.

**Theorem.** If
  limsup_{R→∞} (1/R) Σ_{n∈S, log n<R} (1/log n − log n/R²) > 1/(3πt),
then 𝒩_S is dense in ℬ and ξ𝒩_S is dense in I_ζ. The hypothesis holds for every t when limsup ν_S(R)/R² = ∞ (the reader's condition). For S = {2^a3^b : a + b ≥ 1} it holds exactly when t > (log 2)(log 3)/(2π) = 0.12120…. Density for one t implies density for every larger t.

So the reader's open question 5 ("Are the cover discrepancies with n in {2^a3^b} dense in ℬ?") has the answer yes for every t > 0.12120; it remains open for 0 < t ≤ 0.12120.

**Proof.**
1. *The entire function.* Let Λ ∈ ℬ′ vanish on 𝒩_S; there are A, M, C with |Λ(F)| ≤ Cb_{A,M}(F). Put K_w(s) = g_t(s)(e^w − e^{(1−s)w})/s. Since (e^w − e^{(1−s)w})/s = we^w∫₀¹e^{−θsw}dθ, w ↦ K_w is a ℬ-valued power series, so L(w) = Λ(K_w) is entire, with L(0) = 0 and L(log n) = 0 for n ∈ S.
2. *Growth.* For |σ| ≤ A, s = σ + iτ and w = u + iv: |g_t(s)e^{(1−s)w}| = e^{t(σ²−τ²)+(1−σ)u+τv} and |g_t(s)e^w| = e^{t(σ²−τ²)+u}. With −tτ² + |τ||v| ≤ v²/(4t) (equality at |τ| = |v|/(2t)) and sup_τ(1 + |τ|)^Me^{−t(|τ| − |v|/(2t))²} ≤ C_{M,t}(1 + |v|)^M, and the maximum principle on |s| ≤ 1 for the removable singularity at s = 0:
   log|L(u + iv)| ≤ v²/(4t) + (1 + A)|u| + M log(2 + |v|) + C′.
   Only the linear and logarithmic terms depend on Λ; the coefficient 1/(4t) of v² does not. (`16_` §1 item 3 took the constant of the quadratic term to depend on Λ; it does not.)
3. *Carleman's formula* (Titchmarsh, *The Theory of Functions*, §3.7, rotated to the right half-plane). Suppose L ≢ 0. For zeros r_je^{iφ_j} of L in ρ₀ ≤ |w| ≤ R, Re w ≥ 0 (ρ₀ small, no zero on |w| = ρ₀),
   Σ_j (1/r_j − r_j/R²)cos φ_j = (1/πR)∫_{−π/2}^{π/2} log|L(Re^{iφ})|cos φ dφ + (1/2π)∫_{ρ₀}^R (1/y² − 1/R²) log|L(iy)L(−iy)| dy + O(1).
   Insert the upper bound of step 2 (all weights are nonnegative). On the arc, (1/πR)∫(R²sin²φ/(4t))cos φ dφ = (R/(4πt))·(2/3) = R/(6πt); on the imaginary axis, (1/2π)∫_{ρ₀}^R (1/y² − 1/R²)(y²/(2t))dy = (1/(4πt))(2R/3) + O(1) = R/(6πt) + O(1); the linear and logarithmic terms give O(log R). So the left side is at most R/(3πt) + O(log R). The zeros log n (n ∈ S) lie on the positive axis (cos φ = 1), and every other zero adds a nonnegative term. Hence Σ_{n∈S, ρ₀<log n<R}(1/log n − log n/R²) ≤ R/(3πt) + O(log R), contrary to the hypothesis. So L ≡ 0.
4. *From L ≡ 0 to Λ = 0.* (∂_w − 1)K_w = g_te^{(1−s)w}, so Λ(g_te^{−sw}) = 0 for all w, i.e. Λ(g_te^{vs}) = 0 for all real v. Every G ∈ ℬ is G(s) = ½∫a_G(e^v)e^{sv}dv with a_G decaying faster than every exponential (NJS4.1), and b_{A,M}(g_te^{vs}) ≤ C_{A,M}e^{A|v|}; so g_tG = ½∫a_G(e^v)g_te^{sv}dv as a ℬ-valued Bochner integral, and Λ(g_tG) = 0. Finally g_tℬ is dense in ℬ: put h_N(s) = e^{ts²}P_N(−ts²), P_N the N-th Taylor polynomial of exp. Then F·h_N = g_t·(F·P_N(−ts²)) ∈ g_tℬ (ℬ is closed under multiplication by polynomials), |h_N(s)| ≤ |e^{ts²}|e^{t|s|²} = e^{2tσ²}, and h_N → 1 locally uniformly; splitting |τ| ≤ T₀ and |τ| > T₀ gives b_{A,M}(Fh_N − F) ≤ sup_{|τ|≤T₀}(…) + (1 + e^{2tA²})b_{A,M+1}(F)/(1 + T₀) → 0. So Λ = 0. (This is the step missing in the reader's outline, O4.)
5. *The ideal.* If Λ ∈ ℬ′ vanishes on ξ𝒩_S, then F ↦ Λ(ξF) is continuous on ℬ (ξ decays exponentially on vertical strips) and vanishes on 𝒩_S, so it is 0 by steps 1–4: Λ = 0 on ξℬ, which is dense in I_ζ (reader, Prop. 3.11, last sentence). By Hahn–Banach, ξ𝒩_S is dense in I_ζ.
6. *The reader's condition.* For log n < R/2, 1/log n − log n/R² > 2/R − 1/(2R) = 3/(2R); so the sum is at least (3/(2R))ν_S(R/2), and (1/R)·sum ≥ (3/8)ν_S(R/2)/(R/2)², whose limsup is ∞ if limsup ν_S(x)/x² = ∞.
7. *The lattice {2^a3^b}.* ν(x) = #{(a, b) ≠ (0, 0) : a log 2 + b log 3 ≤ x} = κx² + O(x), κ = 1/(2 log 2 log 3). By partial summation, Σ_{log n<R}(1/log n − log n/R²) = ∫ν(x)(1/x² + 1/R²)dx = (4/3)κR + O(log R) (the boundary term vanishes at x = R). The condition (4/3)κ > 1/(3πt) is t > 1/(4πκ) = (log 2)(log 3)/(2π).
8. *Monotonicity in t.* 𝒩_S^{(t)} = g_{t−t′}𝒩_S^{(t′)} for t > t′; multiplication by g_{t−t′} is continuous on ℬ (|g_{t−t′}| ≤ e^{(t−t′)A²} on |σ| ≤ A), and g_{t−t′}ℬ is dense (step 4). ∎

Jensen's formula in place of Carleman's gives the weaker criterion limsup R^{−2}∫₁^R ν_S(x)dx/x > 1/(8t), which for {2^a3^b} needs t > (log 2)(log 3)/2 ≈ 0.381; Carleman's formula gains because the zeros log n all lie on one ray.

*Status:* proved here (after the review; the reviewer's proof re-derived step by step). *Check:* Z3 (the Carleman sum over {2^a3^b} divided by (4/3)κR is 1.0597, 1.0196, 1.0061 at R = 100, 400, 1600; t* = 0.121196; the quadratic growth coefficient 1/(4t) with an O(M log v) remainder), and the reviewer's `check_nb_carleman.py` (Carleman's formula on a test function; the growth of L for an explicit functional; the density of g_tℬ).

### 2.4 Negative coefficients at every divisor-minimal element (F4; reader Thm 2.3, Cor. 2.4)

Call m ∈ M a *proper M-divisor* of n if 1 < m < n and n/m ∈ M.

**Statement.** Let n ∈ M be such that every proper M-divisor of n has exactly one factorization. If n has one factorization, r_n = ε (that is, 1/k if n = u^k for an atom u, and 0 otherwise). If n has j ≥ 2 factorizations, r_n = 1 − j + ε ≤ −1/6, where ε = Σ1/k over the factorizations of the form u^k. Corollary 2.4 holds at every such n. So every element that has at least two factorizations while its proper M-divisors have one carries a negative coefficient of the stated value, not only the least element with two factorizations.

**Proof.** In the reader's proof the hypothesis on smaller elements is used once: each entry of a k-tuple (k ≥ 2) counted by T_k(n) has exactly one factorization. Each entry is a proper M-divisor of n, since the product of the other entries lies in M. Nothing else uses smaller elements, so the proof applies verbatim. In Corollary 2.4, minimality of N is used only for N′ = a^{j₁/g} = b^{j₂/g} with g = gcd(j₁, j₂) > 1; since N = N′^g, N′ is a proper M-divisor of N, and the hypothesis again suffices. ∎

**Examples.** In the Hilbert monoid {n ≡ 1 (mod 4)} (more generally in a congruence monoid M_H with H ≠ G), take distinct primes p, r in a class c ∉ H and p′, r′ in c^{−1} (Dirichlet's theorem gives infinitely many choices). Then n = pp′rr′ has the factorizations {pp′, rr′} and {pr′, rp′}, and also {pr, p′r′} if c² ∈ H; its proper M-divisors are products of two of the primes and are atoms; there is no pure power. So r_n = −1 if c² ∉ H and r_n = −2 if c² ∈ H; for example r = −2 at 3·7·11·19 in the Hilbert monoid (c = 3 = c^{−1}, c² = 1 ∈ H).

*Status:* proved here. *Check:* Z4 (at all 996 elements of the Hilbert monoid below 4000 whose proper M-divisors factor uniquely, 18 of them with j ≥ 2, r_n computed from the ordered-tuple counts agrees with the formula), and the reviewer's `check_formal_log.py` (nine monoids).

### 2.5 The abscissa for every tensor degree (F5; reader Prop. 5.1)

**Statement.** Let S be a finite multiset of complex numbers with positive integer weights m_ρ, β_max = max Re ρ, and k ≥ 1. Then D_S^{(k)}(s) = Σ_n(Σ_ρ m_ρn^ρ)^k n^{−s} = Σ_w c_wζ(s − w), where w runs over the distinct sums of k elements of S and every c_w > 0, and its abscissa of convergence (and of absolute convergence) is exactly 1 + kβ_max. No positivity of the coefficients and no conjugation-stability of S is needed. For even k and conjugation-stable S the coefficients are nonnegative and the real point 1 + kβ_max is itself a pole (the reader's statement); for odd k it need not be: for S = {0.7 ± 10i, 0.3 ± 10i} and k = 3 the rightmost poles are 3.1 ± 10i and 3.1 ± 30i, and 3.1 is not a pole, while the abscissa is 3.1.

**Proof.** Expanding the power gives the grouped sum, with c_w the sum of the products of weights over the k-tuples with sum w (positive). For Re s > 1 + kβ_max the series converges absolutely. If it converged at some point with real part σ₁ < 1 + kβ_max, it would define a holomorphic function on Re s > σ₁ agreeing with Σc_wζ(s − w), which has a simple pole with residue c_w > 0 at each 1 + w, among them 1 + kρ with Re ρ = β_max; the w are distinct, so the poles do not cancel. Contradiction. ∎

*What changes.* The reader's sentence "positivity of even tensor powers returns max Re ρ" should read: the exponent data return max Re ρ in every tensor degree; positivity (Landau) only places a pole at the real point. The negative result N-W2 holds for every tensor degree, positive or not. Deligne's missing step, an independent bound of the form k + 1 + C, is unchanged.

*Status:* proved here. *Check:* Z5 (the k = 3 example), and the reviewer's `check_abscissa.py` (grouping; convergence and divergence of dyadic windows on either side of the abscissa).

## 3. The minor findings (F6–F22), as verified

Each statement below was re-derived by the second verifier, who wrote its own checks and did not use the reviewer's scripts; its report gives the proofs. "New" means that the notes do not contain the statement; "omission" means that a note does and the reader leaves it out.

| # | Reader | Verdict | Verified statement |
|---|---|---|---|
| F6 | Thm 2.3(b), Prop. 2.6, Ex. 2.5 | confirmed; omission | (1) In a congruence monoid M_H, H ≠ G, at most one factorization of an element is a pure power (u^a = v^b with u ≠ v atoms forces u = w^{b′}, v = w^{a′} with w ∈ M_H, contradicting atomicity), so the value in Thm 2.3(b) is ≤ −½ there (`11_` Lemma 11.2, register S23); with §2.4 this holds at every divisor-minimal element. (2) (i)⇒(ii) of Prop. 2.6 needs no Dirichlet theorem: the Chinese remainder theorem gives infinitely many primes outside H, pigeonhole puts two, p ≠ r, in one nonidentity coset of order d ≥ 2, and A_j = p^{d−j}r^j satisfy A₀A₂ = A₁² (`29_` §1). (3) ⟨4, 8⟩ is zero-free on its whole half-plane of absolute convergence Re s > 0 and not free (ETR2, `29_` 29.N1). |
| F7 | Props 2.6–2.7, the q = 5 paragraph, Fig. 2 | confirmed with correction; the left side new | Saias–Weingartner (periodic coefficients, not of the form P(s)L(s, χ)): there is η > 0 such that for ½ < σ₁ < σ₂ < 1 + η the zeros of D_{M_H} (H ≠ G) with σ₁ < Re s < σ₂, \|Im s\| ≤ T number between c₁T and c₂T for large T (constants depending on the data and the strip). For prime q ≥ 5, Φ_{1/q} = 2Σ_k cos(2πk/q)k^{−s} has nonzero components along ζ and along every nontrivial even character, so the same holds for it, and Hurwitz's formula Z_a(1 − s) = 2Γ(s)(2π)^{−s}cos(πs/2)Φ_a(s) moves its zeros to 1 − s: Z_{1/q} has ≍ T zeros in the reflected strips as well (with its own η), hence infinitely many zeros on each side of the line and in Re s < 0. The existence on both sides is a theorem (conditional only on the cited theorem, read through its abstract); the counts and positions in Fig. 2 are computed. |
| F8 | Lemmas 2.8–2.9 | confirmed; new | Lemma 2.8 holds with C_j ∈ ℂ (the ζ′/ζ(s − σ_j) are linearly independent) and for L(s − σ_j, χ). Lemma 2.9: μ^{*d} = ν^{*d} iff μ = ων with ω^d = 1; positive total masses give ω = 1. |
| F9 | §2.1 bullets | confirmed with correction; omission | Theorem D's hypothesis holds for every n ≤ 12,363,153,437,138: Platt–Trudgian (Bull. LMS 53 (2021)) verify Re ρ = ½ to height 3.0·10¹² by counting sign changes of Z matched with N(T) by a Turing-type method, which also gives simplicity (I(T) = 0 in the reader's Prop. 4.9); their theorem states the first property. Corollary B: the errors tend to 0 at a = 1 if Δ ≥ (1 + δ)√(2 log T₂)/log 2 and T₁ ≥ max(10Δ, 4Δ√(log Δ)) (O3), given O-constants independent of Δ. |
| F10 | Prop. 3.2, Lemma 3.3 | confirmed; new | Prop. 3.2(a)–(c) hold whenever D ≤ div Φ for some 0 ≢ Φ ∈ ℬ (so for the line and off-line parts of Z with Φ = ξ). For such D, every L-equivariant map ℬ/I_D → ℬ/I_{D′} takes values in I_{D″}/I_{D′}, D″ the restriction of D′ to the complement of supp D; it is 0 if D ∩ D′ = ∅. |
| F11 | Lemma 3.4 | confirmed; new | If Σc_{ρ,k}x^ke^{ρx} = 0 for all real x, with 0 ≤ k < m_ρ and Σ\|c_{ρ,k}\|k!R^{−k} < ∞ for some R > 0, then every c_{ρ,k} = 0. |
| F12 | Lemma 3.6, Cor. 3.7 | confirmed | The jet bound holds at every point with \|Re ρ\| ≤ 3/2, with the factor ((1 + \|γ\|)/(½ + \|γ\|))^M (≤ 1.0342^M at the zeros) in place of 2^M. J(Q) is a dense subspace of the space Λ_m of rapidly decreasing jet tuples (to be defined at Cor. 3.7), which is sharper than "proper". |
| F13 | Thm 3.9 | confirmed with correction | (b′) "for every x and every continuous seminorm q, q(Π_ρx) = O((1 + \|γ\|)^{−N}) for every N" is equivalent to (a)–(d). The theorem carries over, with the evident changes, to ℬ/I_χ for primitive χ: the principal parts of 1/L(s, χ) in (c), L(s, χ) in place of (s − 1)ζ(s), (D1)–(D2) and good heights with log q(\|t\| + 2), heights with t < 0 from χ̄ for complex χ, constants depending on q ("verbatim" overstates). |
| F14 | Prop. 3.12 | confirmed; new | The closures of 𝒩_S in ℬ and of ξ𝒩_S in I_ζ have infinite codimension; for F = ∅, closure(𝒩_S) lies in the ideal of functions vanishing at every 2πij/log a, j ≠ 0. |
| F15 | §3.5, residue duality | confirmed; omission | The constant ζ(2)(1/π + 8π/5) = 8.7919 is valid (`26_` §2.1, register S49), against the reader's ζ(2)(1 + 4π²)/π ≈ 21.19; and B(P(L)x, y) = B(x, P(1 − L)y) for every polynomial P. |
| F16 | Prop. 4.3 | confirmed; new | Commuting with a single U_{a₀}, a₀ ≠ 1, suffices: then K commutes with U_{a₀^k} for all k ∈ ℤ, and the reader's estimate with a = a₀^k, k → ±∞, gives K = 0. |
| F17 | Prop. 4.6, Thm 4.2 | confirmed with correction; the unconditional form new | Unconditionally V₊ ⊥ V₋ for Q_A, with Q_A = 2Ω on V₊ and −2Ω on V₋; on T-even data supported on a finite #-closed set, the signature is (n_on + n_pairs, n_pairs); under RH V₊ is maximal positive and V₋ maximal negative, and if RH fails V₊ contains a negative direction. Both results hold for every primitive L(s, χ), complex χ included (Z_χ is #-invariant by Λ(s, χ) = WΛ(1 − s, χ̄) and \overline{L(s̄, χ̄)} = L(s, χ)), with GRH for χ in place of RH. (`42_` Prop. 42.2 has the orthogonality only inside its RH clause.) |
| F18 | Prop. 4.10 | confirmed | For every modulus q and all classes a ≢ b (and r-tuples of classes), the two-line races differ from the one-line races by convergent series (the principal character cancels; each character series converges by `42_` 42.4(a)); the limiting distributions and densities are unchanged. |
| F19 | Prop. 4.12 | confirmed with correction; new | The same argument gives the separator and the splitting for every Dedekind zeta function, with α = nπ/2, n = [K : ℚ]. Inputs: Hecke's functional equation, ζ_K(1 + it) ≠ 0, the 3-4-1 inequality, Stirling, and polynomial growth of ζ_K on vertical strips (convexity), which the reader's growth step does not supply. |
| F20 | Lemma 4.13 | confirmed; omission | The ratio is increasing in \|x\| if r > t and decreasing if r < t (`24_` Lemma 24.5(b)). |
| F21 | Lemmas 5.5–5.6 | confirmed; new | Lemma 5.5's inequality Σ_{τ≠1}d_τ(−ν(τ)) ≤ 1 holds for real-valued ν (integrality is used only for the final dichotomy). Lemma 5.6 holds with real δ_n ≤ CD^n (D > 0) in place of a constant, giving max\|a_j\| ≤ D; for a curve over 𝔽_q, #X(𝔽_{q^n}) ≥ 0 alone gives \|α_j\| ≤ q (the trivial bound). |
| F22 | Prop. 6.2, Lemma 6.4, Prop. 6.5, Lemma 6.6 | confirmed with correction | Prop. 6.2 holds for every integer a ≥ 2 in ∏_{ℓ∤a}ℤ_ℓ^×. Lemma 6.4: for real a > 1 the escape clauses hold, the reflected-pair clause needs a ≥ 2 (for 1 < a < 2 a pair can return), and the collision clause becomes "only if ρ/ρ′ = a′/a > 0" (rational only for rational a, a′), still impossible for distinct points of the critical line. Prop. 6.5: no change; its first sentence is already the stronger form (the review's item here is not an understatement). Lemma 6.6: V may be any C¹ field; U is polynomial if V is; for a polynomial automorphism F, U is complete iff V is. |

## 4. For the register and the next version of the reader

New or sharpened results, all proved here unless marked: S73 the first Hurwitz jet on every sheet (§2.1); S74 the classification of transfer-compatible Hermitian forms (§2.2); S75 the Carleman density criterion and density for {2^a3^b} at t > (log 2)(log 3)/(2π) (§2.3); S76 negative coefficients at every divisor-minimal element (§2.4); S77 the abscissa 1 + kβ_max for every k and every finite S (§2.5); S78 zeros of Z_{1/q} on both sides of the line for prime q ≥ 5 (F7; conditional on Saias–Weingartner, read through its abstract); S79 the unconditional orthogonal splitting of the chiral form, its signature, and the L(s, χ) versions of Theorem 4.2 and Proposition 4.6 (F17). Errata E1–E4 are O1–O4. Open question 5 of the reader is answered for t > 0.12120.

A later version of the reader would replace the statements of Thm 4.1, Lemma 3.13, Prop. 3.11 (with a full proof), Thm 2.3/Cor. 2.4, Prop. 5.1 and Cor. 2.2 by the forms above, correct Prop. 5.2, and take in the minor items of §3. The narrative sentence of §5 about positivity changes as stated in §2.5. Nothing in this note is a new statement about the location of the zeros.

## 5. Not checked here

- Saias–Weingartner's theorem and Platt–Trudgian's were read through their arXiv abstracts (and, for the latter, the fetched text), not in the printed papers.
- Titchmarsh's statement of Carleman's formula was not re-read; its form was checked numerically by the reviewer on a test function.
- The standard inputs for L(s, χ) and Dedekind zeta functions in F13, F17 and F19 (Davenport ch. 16; Hecke) were not re-read.
- The O-constants of `02_` §4.2 (O3) were not re-derived.

## 6. Checks

- `checks/zeta_reader_addendum_checks.py` (mine; Z1–Z6, all pass, 2 s).
- `checks/zeta_reader_review/`: the reviewer's report and its ten scripts with outputs (all pass).
- `checks/zeta_reader_review/verify_minors/`: the verifier's report and its eleven scripts with outputs (all pass).
