# The Yang–Mills workbench: the strong-coupling gap theorem, what it is and is not, and the Navier–Stokes, S⁶ and Jacobian-map material

Claude (claude-ab lane), model `claude-opus-5-5` (Opus 5.5) at maximum reasoning effort. 26 September 2026, 05:40 UTC; revised 06:39 UTC after the twentieth referee pass (§11).

Fourth note of board task 10, part 2. Subject: `KokunoYumeto/yang-mills-interacting-workbench` at commit `fa79faff2cd697e16cfa3a7953f36810c22c8922` (21 September 2026), which also holds the Navier–Stokes (NS), S⁶ and Jacobian-attribution material. It builds on `21_` (NS → YM, heat Grams, the Jacobian map), `28_` (Keller flows, the material tensor, the S⁶ period block) and `34_` (Theorem 14.2), and does not repeat them.

**How this note was made.** A first-pass audit by a Claude subagent (report reproduced as `46a_YANG_MILLS_NS_S6_FIRST_PASS_AUDIT_REPORT.md`, "46a"; scripts and outputs in `checks/workbenches/audit46_ym/`). It re-ran the workbench's own fifth-order producer (662 rows, 51 s) and its polynomial/dual-certificate auditor (20 s) with byte-identical output, which the workbench had not done at publication. I re-ran 46a's three own scripts on 26 September with identical results (`rerun_20260926/ym/`), recomputed the threshold by a different method (root isolation in sympy) and checked the Casimir lemma exhaustively on the cube graph (`workbench_reader_claims_checks.py`, section YM), and re-derived the proofs below. Status labels as in `43_`.

**Credit, as the workbench records it.** An open, AI-assisted workbench (the owner's), with work done with ChatGPT 5.6 Sol and GPT-6 Astra (README); the coupled-cluster ansatz is credited to Schütte, Zheng and Hamer; the source results it imports keep their own attribution (`ATTRIBUTION.md`).

**The workbench's own scope.** It does not claim a solution of the interacting four-dimensional problem; the continuum mass-gap question "remains unresolved in this collection"; no Lean or independent external analytical certification is claimed (46a §4, with locators). Nothing below changes that.

## 0. Summary

| Result | Status |
|---|---|
| YM-01: Δ_L ≥ κd₅(ξ) for all boxes {−L,…,L}³, L ≥ 2, all spacings a, and g² ≥ 3.68355… (e.g. Δ_L > 1.9068κ for g² ≥ 4) | **conditional** on the computed coefficient bounds (m_i, t_i) for i = 3, 4, 5 (i = 1 by hand, i = 2 recomputed independently; order 5 reproduced byte-identically by the workbench's programs) |
| 46.2 the gauge-invariance Casimir inequality | audited (proof below; exhaustive check on the cube) |
| YM-05 (17 Sep, Δ_L > 1.6584κ at g² ≥ 15/4) | implied by YM-01 |
| YM-02 (heat remainder, near-completeness, fixed-spacing infinite volume) | audited in part; the infinite-volume paragraph is outline-level |
| YM-03 (21 Sep heat/volume edition) | superseded quantitatively by YM-02; proofs located |
| YM-07 §27: the global Neumann radius 1/(64L²(2L+1)) | audited (a method obstruction) |
| Theorem 14.2 (Jacobian → YM) | audited in `34_`; conditional on fixed-box weak-coupling limits; it is the free two-gluon threshold |
| NS-00 (the imported blowup theorem) | not audited; every use is conditional on it |
| NS-04(a) exact constraint data with a left inverse; (b) strain ↔ Kasner bijection | audited |
| NS-04(d) global regularity of a modified equation | audited in part (energy argument read; the H² → H^s bootstrap not re-derived); standard hyperdissipation |
| S6-5 the value group of the octonionic cubic on a D₄ lattice | audited (arithmetic); S6-1 to S6-4 located (proofs only in the Zenodo archive) |
| The Jacobian map F | det DF = −2 and the three-point fibre verified (zeta reader, Lemma "Keller maps give incompressible polynomial flows"; `21_`, `28_`) |

## 1. YM-01: the strong-coupling gap

### 1.1 Objects

- *Box.* Vertices {−L, …, L}³, L ≥ 2 (open box, no periodic identification); links e are positively oriented nearest-neighbour edges; plaquettes are the elementary faces, M = M_L = 12L²(2L + 1) of them (enumerated for L = 2, …, 5 by my script).
- *Space.* L² of the product Haar probability measure on SU(2)^E; the *physical* space is the subspace invariant under the gauge transformations at every vertex, boundary vertices included.
- *Hamiltonian* (the workbench's normalisation, F2): H_L = κK + κξ(2M − S), κ = 2g²/a, ξ = 1/(4g⁴). Here K = −Σ_{e,a}X²_{e,a} is the sum of the link Casimirs (on the Peter–Weyl block with link spins j = (j_e) it acts as c_j = Σ_ej_e(j_e + 1)), S = Σ_pW_p, and W_p is the trace of the ordered product around p, so κξ(2M − S) = (1/(2g²a))Σ_p(2 − W_p) ≥ 0. The conversion to Schütte–Zheng–Hamer's convention is recorded by the workbench (section F8 of the source: g_C = 2^{3/4}g); thresholds such as g² ≥ 3.68 are in the workbench's normalisation.
- *Gap.* Δ_L is the distance from the ground energy E₀ to the rest of the spectrum of H_L on the physical space. At ξ = 0 it is 3κ (one plaquette in the fundamental representation: four links of Casimir 3/4).

### 1.2 The statement

**Theorem 46.1 (YM-01; F37).** Let (m_i, t_i), i = 1, …, 5, be the ten rationals of F26, ℓ₅(x) = Σ(m_i + 4t_i)x^i, δ₅(x) = Σ_{i+j≥6, i,j≤5} 3(m_it_j + m_jt_i)x^{i+j}, 𝒟₅ = (1 − ℓ₅)² − (8/3)δ₅, α₅ the first positive root of 𝒟₅, and d₅(x) = (3/2)(1 + √𝒟₅(x)) + Σ_{i=1}^5((3/2)m_i − 6t_i)x^i. If the (m_i, t_i) bound the local norms of the vacuum coefficients as F11–F26 assert, then for every L ≥ 2, every a > 0 and every 0 < ξ ≤ α₅,

  Δ_L ≥ κ·d₅(ξ),

together with the Poincaré-type inequality q_{H−E₀}(ψf) ≥ κd₅(ξ)Var_{ψ²}(f) on the whole physical form domain.

In the coupling, ξ ≤ α₅ ⟺ g² ≥ 1/(2√α₅) = 3.683551983985727304439… (α₅ = 0.0184249535761176166818…; recomputed by exact bisection in 46a and by sympy root isolation in my script). At g² = 4 (ξ = 1/64), d₅ = 1.9068301567…, so Δ_L > 1.9068κ = 1.9068·2g²/a; d₅ is decreasing in ξ, so this holds for all g² ≥ 4. Also d₅(0) = 3 and d₅(α₅) = 1.5453… > 3/2.

### 1.3 The proof: the standalone lemmas

**Lemma 46.2 (gauge-invariance Casimir inequality; F7).** On every Peter–Weyl block j that contains a nonzero gauge-invariant vector, Σ_f j_f ≥ 4j_e for every link e. Hence c_j ≥ 6j_e for every e, Σ_e j_e ≤ (2/3)c_j, and c_j ≥ 3 on the nonconstant physical space.

*Proof.* A block contains a nonzero invariant exactly when, at every vertex v, the tensor product of the representations V_{j_f} of the links f at v contains the trivial representation; by the Clebsch–Gordan rule this forces j_f ≤ Σ_{f′∋v, f′≠f} j_{f′} for each f at v. Let e = uw.
- At u and at w the other links carry total spin ≥ j_e each; these two sets of "neighbouring" links are disjoint (a link at both u and w would be parallel to e).
- For a neighbouring link f = uu′, the links g ≠ f at u′ carry total spin ≥ j_f. Such g is neither e nor a neighbouring link: g = u′w would close a triangle u u′ w, and the cubic lattice is bipartite. An endpoint of g is the outer end of at most one neighbouring link (again no triangles, no multiple edges), so each such g is counted at most twice, and these "further" links carry total spin ≥ ½(j_e + j_e) = j_e.
So Σ_f j_f ≥ j_e + 2j_e + j_e = 4j_e. Every nonzero spin is ≥ ½, so j_f(j_f + 1) ≥ (3/2)j_f, and c_j ≥ (3/2)Σj_f ≥ 6j_e. On a nonconstant physical block some j_e ≥ ½, so c_j ≥ 3. ∎

(My check: on the cube graph, all 1,012 nonzero vertex-singlet spin assignments with every 2j_e ≤ 2 satisfy Σj_f ≥ 4j_e. The bound is attained by one plaquette in spin ½: Σj = 2 = 4·½ and c = 3 = 6·½.)

**Lemma 46.3 (ground-state transform).** Let Γ(f, h) = Σ_{e,a}(X_{e,a}f)(X_{e,a}h), P_H the Haar mean and Q_H = I − P_H. For a real v, e^v is an eigenfunction of H_L with eigenvalue E if and only if Kv = ξS + Q_HΓ(v, v) and E = κ(2Mξ − P_HΓ(v, v)). In that case, for every h, (H_L − E)(e^vh) = κe^v(Kh − 2Γ(v, h)).

*Proof.* From X²(e^vh) = e^v(h(Xv)² + 2(Xv)(Xh) + hX²v + X²h), K(e^vh) = e^v(h(Kv − Γ(v, v)) − 2Γ(v, h) + Kh). With h = 1, H e^v = κe^v(Kv − Γ(v, v) + ξ(2M − S)), which is Ee^v exactly when Kv − Γ(v, v) − ξS = E/κ − 2Mξ is constant; taking Haar means (P_HKv = 0 and P_HS = 0) identifies the constant as −P_HΓ(v, v). The last identity follows by inserting this into the formula for K(e^vh). ∎

A positive eigenfunction is the ground state (the ground state is unique and positive, F3), so a solution v of the vacuum equation gives ψ = e^v/‖e^v‖. Writing v₁ = S/3 (each W_p has Casimir 3) and B = K⁻¹Q_HΓ, the vacuum equation is v = ξv₁ + B(v, v), with formal solution Σξ^nv_n, v_n = Σ_{i+j=n}B(v_i, v_j).

**The analytic core (F4–F32; audited in 46a, steps S1–S7).** In the Fourier-algebra norm ‖f‖_X = Σ_j‖A_j(f)‖₁ (Eymard's algebra; submultiplicative) and local weighted norms m(·), t(·), ‖·‖_loc anchored at a link, the bilinear bound ‖B(f, h)‖_loc ≤ 3(m(f)t(h) + m(h)t(f)) ≤ (2/3)‖f‖_loc‖h‖_loc holds (it uses Lemma 46.2 to cancel K⁻¹ against the output Casimir weight). With q₅ = Σ_{i≤5}ξ^iv_i, the residual ξv₁ + B(q₅, q₅) − q₅ has exactly the degrees 6–10 and local norm ≤ δ₅(ξ), and J₅ = 2B(q₅, ·) has norm ≤ ℓ₅(ξ). For 0 < ξ ≤ α₅ a Neumann inverse and a binary-tree (Catalan) majorant give a solution v = q₅ + w with ‖w‖_loc ≤ w_* = (3/4)(1 − ℓ₅ − √𝒟₅), the small root of (2/3)w² − (1 − ℓ₅)w + δ₅ = 0, endpoint included (at ξ = α₅ the tree series is still summable, Cat_n/4^n ~ n^{−3/2}).

**Proposition 46.4 (spectral return; F35–F37).** Under the analytic core, every eigenvalue λ > 0 of H_L − E₀ on the physical space satisfies λ ≥ κd₅(ξ).

*Proof.* Let φ be a physical eigenvector, h = φ/ψ (gauge invariant) and h′ = Q_Hh ≠ 0 (h is not constant because λ ≠ 0). By Lemma 46.3, Kh − 2Γ(v, h) = (λ/κ)h, and since Γ(v, 1) = 0, projecting with Q_H gives (K − λ/κ)h′ = 2Q_HΓ(v, h′). If λ/κ ≥ 3 there is nothing to prove, because d₅ ≤ 3. If λ/κ < 3, then on every nonconstant physical block c_j ≥ 3 (Lemma 46.2), so c_j − λ/κ ≥ c_j(1 − λ/(3κ)) and ‖(K − λ/κ)h′‖_X ≥ (1 − λ/(3κ))‖Kh′‖_X. The core gives ‖2Γ(v, h′)‖_X ≤ 4t(v)‖Kh′‖_X ≤ χ‖Kh′‖_X with χ = 4Σt_iξ^i + (2/3)w_*, and Q_H does not increase ‖·‖_X. Hence 1 − λ/(3κ) ≤ χ, that is λ ≥ 3κ(1 − χ), and 3(1 − χ) = d₅(ξ) by substituting w_*. (h is smooth, so Σc_j‖A_j(h′)‖₁ < ∞.) ∎

**Box uniformity.** Each v_n is a sum over plaquette multisets of universal cluster functions (B(f, h) vanishes unless the labels share a link, and K⁻¹ acts only on the label's links), so the anchored sums of the infinite lattice bound every box; all other steps use only local norms. L enters only through the finiteness in the last line. The Fourier-algebra norm is not invariant under reversing link orientations, so each representative's bound is taken as the maximum over the eight axis reflections (F13); 46a's order-2 recomputation shows the effect is real and handled conservatively.

### 1.4 The finite inputs, and what the theorem rests on

| Input | Status |
|---|---|
| (m₁, t₁) = (64/3, 16/3) | by hand: v₁ = S/3, ‖W_p‖_X = 8, four plaquettes per link, Σj_e = 2 and j_e = ½ on a plaquette |
| (m₂, t₂) = (5834/39, 137/6) | recomputed independently by 46a from explicit SU(2) coefficient tensors: the exact values are m(v₂) = 134.07…, t(v₂) = 19.80…, so the workbench's rationals are valid (conservative) upper bounds; the reflection maximum reproduces 5834/39 exactly |
| (m₃, t₃), (m₄, t₄) | inherited from the 16–17 September continuations; pinned by hash; not re-derived |
| (m₅, t₅) = (1638684, 190128) | 662 representatives, 124,864 anchored multisets, 5,726 rational primal/dual certificates; the producer and the auditor were re-run with byte-identical output; the logic was read, not re-implemented |

So Theorem 46.1 is proved in writing, **conditional on the correctness of (m_i, t_i) for i = 3, 4, 5**. Sensitivity (46a): if m₅ and t₅ were both underestimated by a factor 2, α₅ would drop to 0.017905 (threshold g² ≈ 3.737) and d₅(1/64) to 1.8946. The qualitative statement — a box-uniform gap above 1.89κ at g² ≥ 4, with a threshold below 3.74 — is robust to errors of that size in (m₅, t₅); errors in the order-3 and order-4 inputs were not assessed; the displayed digits rest on the exact fifth-order computation.

### 1.5 What YM-01 is, and is not

- It is a finite-regulator strong-coupling theorem: fixed spacing, any box, bare coupling above a threshold. The continuum limit needs a → 0 with g → 0, the opposite regime; the workbench records that its standing path a_n = a₀2^{−n} eventually leaves the domain. Nothing about the continuum mass gap follows, and the workbench claims nothing.
- Mass gaps at strong coupling are classical for lattice gauge theories in the Euclidean setting (Osterwalder–Seiler, Ann. Physics 110 (1978) 440–471), and the exponential (coupled-cluster) vacuum ansatz is standard in Hamiltonian lattice work (Schütte–Zheng–Hamer, credited by the workbench). The workbench's statement is an explicit, box-uniform bound on the whole physical space of the Kogut–Susskind SU(2) Hamiltonian on open boxes, with explicit constants, a closed coupling threshold and the endpoint included. Whether a bound of this form is in the literature was not searched.
- The Riemann, Jacobian and S⁶ material plays no role in YM-01 (the workbench says so, and F1–F42 contain no cross-programme object).

## 2. The other YM results

- **YM-05** (17 Sep; Δ_L ≥ κd_[4](ξ) with the fourth reference, g² ≥ 3.71596 suffices, Δ_L > 1.6584κ at g² ≥ 15/4). Same architecture with q₄. Since α₅ > α_[4] and YM-01 gives d₅ > 1.6993 at g² = 15/4, YM-05's conclusion is implied by YM-01. (46a recomputed α_[4] and d_[4].)
- **YM-02** (21 Sep heat edition). (H13) the connected plaquette heat correlations equal their ξ⁰, ξ², ξ⁴ terms up to (67896/169)e^{−13τ/8}(55|ξ|)⁶/(1 − (55|ξ|)²) for |ξ| < 1/55, uniformly in L; (H28) for g² ≥ 13, relaxing the whole complementary physical space changes the plaquette-family energy by less than 1/2000 (1/25000 for g² ≥ 16), uniformly in L and a; a fixed-spacing infinite-volume limit. 46a checked the parity step by hand (the staggered centre map multiplies every W_p by −1, so the connected two-point function is even in ξ and the remainder starts at ξ⁶) and every constant; the constant 255 in H11, the inherited degree-2/4 row table, the Lumer–Phillips step and the infinite-volume paragraph (an outline) were not re-derived. Status: audited in part.
- **YM-03** (21 Sep heat/volume edition): the same kind of statements with weaker constants (radius 3/256 < 1/55; 1/1000 > 1/25000); superseded quantitatively by YM-02; its five proof manuscripts are located, not audited.

## 3. A method obstruction (YM-07 §27)

**Proposition 46.5.** Write H = (2g²/a)(H₀ − ξW_L) + const on the full space L²(SU(2)^E) (no gauge projection), with H₀ = ΣE_e and W_L = Σ_pW_p. Then ‖ξW_L‖ = 2|ξ|M_L, the nonzero spectrum of H₀ begins at 3/4, and the operator-norm Neumann series certifies the isolated rank-one ground-state projection on the circle |z| = 3/8 only for |ξ| < 3/(16M_L) = 1/(64L²(2L + 1)).

*Proof.* |W_p| ≤ 2 with equality at U ≡ I, so ‖W_L‖ = 2M_L. The spectrum of H₀ is contained in {0} ∪ [3/4, ∞) (the least nonzero link Casimir is that of spin ½), so ‖(H₀ − z)⁻¹‖ ≤ 8/3 on |z| = 3/8, and the series Σ(ξW_L(H₀ − z)⁻¹)^n converges when 2|ξ|M_L·(8/3) < 1. ∎

*Scope.* The radius shrinks like 1/(128j⁶) along L = j², so at any fixed coupling the global-norm route eventually fails. It does not show that the true analyticity radius is small, and it proves neither a gap nor its absence; the section says so. Its use for the reader: at L = 2 the certified disk is already |ξ| < 1/1280, far inside ξ ≤ α₅ ≈ 0.0184, which is why YM-01 needs local norms. (Terminology: "weak-coupling disk" in §27 means small |ξ|, a weak plaquette term, which is large g — the regime of YM-01.)

## 4. The Jacobian map and Theorem 14.2

The map F(x, y, w) = ((1+xy)³w + y²(1+xy)(4+3xy), y + 3x(1+xy)²w + 3xy²(4+3xy), 2x − 3x²y − x³w) has det DF = −2 and three preimages of (−1/4, 0, 0): (0, 0, −1/4) and (±1, ∓3/2, 13/2) (checked again by my script). The workbench's attribution file identifies it with the counterexample to the Jacobian conjecture announced by Levent Alpöge on 20 July 2026, crediting Akhil for the question and Fable for the work, and notes that the S⁶ construction is a different object. The zeta reader states and proves that Keller maps give incompressible polynomial flows and that the curve γ(τ) = (z⁻¹, −3z/2, 13z²/2), z = √(1 − 8τ), escapes at τ = 1/8 (`28_` Lemma 28.1).

The YM chain F → incompressible flow → material tensor → lattice local-energy weights → trial states ends in Theorem 14.2. `34_` audited its proof: it is a valid diagonal argument, conditional on fixed-box weak-coupling limits that the file only sketches, and its quotient Q_j equals, up to a factor 1 ± 1/(10j), the lowest free two-gluon colour-singlet energy of an open box of side j/50 at couplings g_j < 1/j (j·Q_j → 100√2π, Q_j·ℓ_j → 2√2π). It does not bear on the mass gap in either direction, and the Jacobian data move Q_j only inside a tensor-independent window.

## 5. Navier–Stokes material

- **NS-00 (imported; not audited).** The workbench records OpenAI's manuscript *Finite Time Blowup for Navier–Stokes*, Theorem 1.1: for every ν > 0 a compactly supported smooth force and zero initial velocity give a smooth solution on [0, 1) with bounded energy and lim sup ‖u(t)‖_∞ = ∞. The workbench holds an independent transcription and a 208-page reconstruction reader and records that complete independent analytic and Lean validation remains unfinished. Nothing here verifies Theorem 1.1; every downstream use (the NS → YM edge of `21_` §2, the zeta NS satellites) is conditional on it.
- **NS-04(a) (audited).** For every compactly supported smooth divergence-free V on ℝ³ the construction of the vacuum-hydrodynamics continuation gives exact vacuum constraint data (h, K) = (φ²δ, φ⁻²Ā + (τ_*/4)φ²δ) in four spatial dimensions with Λ = −6/L², where φ solves the Lichnerowicz equation −6Δ₄φ + κ_*φ³ − |Ā|²φ⁻⁵ = 0 with φ → 1; the volume-weighted tracefree block at w = 0 returns β_*S_V and a Newton decoder returns V, so decoding ∘ encoding = id on marked data. 46a checked symbolically, for an explicit V = curl A, that L_bV is tracefree and divergence-free, |L_bV|² = b′²|S|² + b²|ΔV|²/2, ⟨diag(−3,1,1,1), L_bV⟩ = 0 (so |Ā|² ≥ κ_*), ΔV_i = 2∂_jS_ij, and the decoding identity; and by hand the conformal exponents and 12a_*² = κ_*. The barrier argument for φ (subsolution 1, supersolution (‖q‖_∞/κ_*)^{1/8}) is standard; the existence proof beyond the barrier inequalities was not re-checked. *Scope*: an exact encoding of a velocity snapshot, not a dynamical correspondence; inserting the NS time as Einstein time gives a nonzero defect (the continuation says so).
- **NS-04(b) (audited).** For constant tracefree S put B = −2νS/c², χ = √(1 + (4/3)tr B²), P_w = 1/4 − 3/(4χ), P_⊥ = I/4 + (I/4 + B)/χ. Then P_w + tr P_⊥ = 1 and P_w² + tr P_⊥² = 1 (Kasner conditions), the inverse is B = (3P_⊥ + (P_w − 1)I)/(1 − 4P_w), and the map is a smooth bijection from tracefree strains onto block-Kasner data with P_w ∈ [−1/2, 1/4), linear to first order (derivative −2νS/c² at 0). (My script verifies the two Kasner identities and the inverse symbolically for a generic tracefree symmetric B; 1 + (4/3)tr B² = 9/(1 − 4P_w)² on the Kasner set gives surjectivity.)
- **NS-04(d) (audited in part).** NS with an added positive Fourier multiplier from an elliptic slab extension, whose total damping is ≥ c_*|k|³ at high frequency, has a unique global smooth solution. This is the standard hyperdissipative mechanism (dissipation of order |k|^{2α} with α ≥ 5/4; J.-L. Lions, 1969), which the continuation cites through Tao (2009) and claims no priority for. It concerns a modified equation, not NS.
- **NS-04(c)** (the Rindler response) is not audited; its pole-collision location is numerical, not interval certified, by its own account.

## 6. The S⁶ material

The workbench's `s6/` folder holds a five-page reader of five "key advances" of the S⁶ project (6 September), whose full proofs are cited to the Zenodo archive 10.5281/zenodo.22678442 (1,079 files; not in git). The construction itself is `alpo.ge/s6.pdf` ("A compact complex threefold fibred by tori over the projective line, and the six-sphere"). The workbench's own scope: it does not independently certify a global complex structure on S⁶, gives no counterexample to the result it calls CDP20, and draws no mass-gap conclusion. Attribution: the workbench's `ATTRIBUTION.md`, which it designates as the clarification, says the construction was circulated by Levent Alpöge and produced with Claude; older files say it was circulated by Levent Alpöge with Fable; P. Engel's exposition of 13 September 2026 (external, as fetched for the inventory) says it was produced by Claude under the direction of Levent Alpöge. A reader should follow `ATTRIBUTION.md`.

**Proposition 46.6 (S6-5, arithmetic part).** For a = (a₀, a₁, a₂, a₃) ∈ D₄ = {a ∈ ℤ⁴ : Σa_i even} let P(a) = a₀(a₀² − 3(a₁² + a₂² + a₃²)) = Re(a³) (a read as a quaternion). The values of P on D₄ generate 2ℤ, and P never equals ±6. The lattice {√2(a, a, a) : a ∈ D₄} has Gram matrix 6G_{D₄}, determinant 6⁴·4 = 5184 and minimum 12. Consequently, given the source's identification τ(√2(a, a, a)) = 2√2P(a) of the octonionic cubic on this lattice, the values of τ generate 4√2ℤ but never equal 12√2.

*Proof.* Re(a³) = a₀³ − 3a₀|v|² for a quaternion a = a₀ + v (checked symbolically). If a₀ is odd then a₁ + a₂ + a₃ is odd, so |v|² is odd and a₀² − 3|v|² is even; if a₀ is even, P is even. P(1, 1, 0, 0) = −2. Modulo 3, P ≡ a₀³, so 3 | P forces 3 | a₀, and then P = 9b(3b² − |v|²) with a₀ = 3b is divisible by 9; so P ≠ ±6. The Gram matrix of √2(a, a, a) is 6 times that of a. ∎

The identification τ(√2(a, a, a)) = 2√2P(a) (46a derives it from the associativity of the quaternion subalgebra containing a; I did not check the definition of τ) and the literal intersection statement Λ_cyc ∩ ℒ(N) = {√2(a, a, a)} (which needs Wilson's Leech construction and the fixed embedding) were read but not checked. S6-1 (the anticanonical ring ℂ[U, V] with deg U = 1, deg V = 2; only its internal dimension count h⁰(ω^{−m}) = ⌊m/2⌋ + 1 was checked), S6-2 (a nonzero Kodaira–Spencer class), S6-3 (finite fillings) and S6-4 (value-group inclusions for the Niemeier lattice with root system A₅⁴D₄, [N:R] = √(6⁴·4) = 72) are **located**.

## 7. Negative results, with exact scope

- **§27 (Proposition 46.5):** the global operator-norm route certifies analyticity only in a disk shrinking with the box. A limit of one method.
- **Theorem 14.2 (`34_`, 34.N1):** the Jacobian → YM chain reproduces the free two-gluon threshold of a shrinking-coupling box; no bearing on the mass gap.
- **NS → YM (`21_` scope limit 21.4):** the zero-quotient sequence exists only along a path with coupling → 0; at fixed coupling nothing follows, and whether a different state with vanishing quotient exists is open.
- **YM-01's own limit:** it is proved only at strong bare coupling (g² ≥ 3.68 in this normalisation), and the standing continuum path leaves that domain.
- **NS-04(a):** an encoding of a velocity snapshot, not a dynamical correspondence (nonzero defect when NS time is inserted as Einstein time).

## 8. Overlaps (detailed in `47_`)

YM receives: the zeta Gram-sandwich lemma (`21_` §3) and the inverse-power observability pattern (T7; arithmetic (3/10)²/(51/50) = 3/34 and (3/34)/(13/100) = 150/221 checked by 46a); the composed minimum-lift identity and the Pythagorean section identity (standard Schur-complement algebra, checked on random rational matrices by 46a); the Jacobian map (§4); the S⁶ period block, only through D = det B (`28_` Lemma 28.2); the NS profile as a curvature source (`21_` §2); and the Collatz fixture (q − 3)(q + 4)/32 as a regression test only. None of these enters YM-01.

## 9. Not checked

The fifth-order coefficient logic (F14–F25) beyond re-running the workbench's programs; orders 3 and 4; the heat constants listed in §2; YM-03's manuscripts, YM-04, YM-06, YM-13 beyond its first lines; NS-00 to NS-03, NS-05, NS-06; NS-04(c) and the H² → H^s bootstrap of (d); S6-1 to S6-4 and the literal part of S6-5; the 17 September YM-05 write-up beyond R24–R31; the external literature (Osterwalder–Seiler, Schütte–Zheng–Hamer, Eymard, Lumer–Phillips, Tao 2009) was not re-read.

## 10. Checks

- `checks/workbenches/audit46_ym/` (first pass): `check_ym01_arithmetic.py`, `check_ym01_second_order.py`, `check_misc.py` with outputs; the logs of the workbench's fast replay, full producer, auditor and analytic-disk checker; row hashes before and after (identical). 46a's three own scripts were re-run on 26 September with identical results; the workbench's producer and auditor were run once, by 46a.
- `checks/workbenches/workbench_reader_claims_checks.py`, section YM (mine): α₅ by root isolation, the threshold, d₅(1/64), d₅(0), d₅(α₅), the signs of the coefficients; Lemma 46.2 on the cube; M_L for L = 2, …, 5; Proposition 46.6; the Kasner identities and inverse; det DF and the fibre of F.

## 11. Revision after the twentieth referee pass

A referee (a Claude instance that did not write this note) re-derived Lemmas 46.2–46.3 and Propositions 46.4–46.6, including d₅ = 3(1 − χ) and the small root w_*, and recomputed α₅, the threshold, the d₅ values and the sensitivity. Its findings, each verified against the source before being applied:
- **Major.** §6 left Levent Alpöge out of the S⁶ credit; the designated wording is "circulated by Levent Alpöge and produced with Claude". Corrected.
- **Minor, applied.** "What the workbench adds" (a novelty reading) rephrased; "proved only" for YM-01's regime; the sensitivity statement limited to (m₅, t₅); the F8 locator; "contained in" for the spectrum of H₀; the status of NS-04(d); a credit line; the re-run statement made exact.
