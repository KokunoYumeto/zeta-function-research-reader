# First-pass mathematical audit of the Yang–Mills workbench (with its Navier–Stokes and S⁶ side material)

Prepared by Claude (model `claude-opus-5-5`, Opus 5.5), 26 September 2026, for the public reader of the workbench's results. Read-only work: nothing in the repository was edited, committed or pushed. Quotations are under 15 words. "My check" means a computation in this folder; "by hand" means a derivation done while reading and written out here.

---

## 0. Sources and method

**Repository.** KokunoYumeto/yang-mills-interacting-workbench, `origin/main` = `fa79faff2cd697e16cfa3a7953f36810c22c8922` (21 Sep 2026), the commit the survey and the audit notes `21_`, `28_`, `34_` read. It was read with `git show`, `git ls-tree`, `git grep` and `git archive` (all read-only). The clone has no checked-out working tree; that state predates this audit.

**Inventory and earlier audits (cited, not redone).**
- Inventory: `workbench_survey/WORKBENCH_SURVEY.md` §§2–4 (IDs YM-01…YM-13, NS-00…NS-06, S6-1…S6-5, OV-xx).
- `34_AUDIT_YM_THEOREM_14_2…` (Theorem 14.2, YM-09).
- `21_…PART1…` §2 (NS → YM, YM-10) and §3 (heat Gram lemma, YM-12 T1–T3).
- `28_…PART2…` §1 (Keller maps and flows, Lemma 28.1), §2 (material tensor, YM-08) and §3 (S⁶ period block, Lemma 28.2, YM-11).

**Read in full for this audit.**
- `yang-mills/consolidation/20260921-fifth-reference/README.md` (127 lines).
- `…/package/workbench/yang-mills/continuations/20260921-fifth-reference-return/FIFTH_REFERENCE.md` (F1–F42, 441 lines).
- `…/HEAT_AND_COMPLEMENT.md` (H1–H34, 391 lines).
- `yang-mills/sources/ym_spatial_continuum_astra_20260908/spatial_continuum.md` L8268–8436 (§27, §28).
- `navier-stokes/continuations/20260919-vacuum-hydrodynamics/README.md` (182 lines).
- `…/SLAB_COMPARATORS.md` §§1–2 (L1–140).
- `s6/27_s6_key_advances_frozen_2026-09-06.tex` §1 and §§4–5 (L25–80, L196–325).
- `RH_HEAT_TRANSFER.md` L20–40 and T7 (L236–300).
- `yang-mills/research-control/RESEARCH_NOTE.md` L183–249 and `check.py` L225–250.

**Read in part.**
- 17 Sep reader `consolidation/20260917/reader/yang_mills_quartic_cube_reader.tex`: L505–540 and Appendix B, R24–R31 (L1670–1830).
- `consolidation/20260917/VALIDATION.md` L1–40.
- `consolidation/20260921/README.md` L1–80.
- `yang-mills/README.md` L1–67; `WORKBENCH.md` L7–23; `README.md` L19–35; `navier-stokes/README.md` L1–35.

**Checks written for this audit.** All scripts and outputs are in this folder; every script ran in under 2 minutes.

| File | What it does | Result |
|---|---|---|
| `check_ym01_arithmetic.py` → `_OUTPUT.txt` | Recomputes α₅, the threshold, d₅, w_*, monotonicity, the majorant identity and the lattice-unit values from the ten rational inputs of F26 only (exact rationals, 60-digit mpmath) | all PASS |
| `check_ym01_second_order.py` → `_OUTPUT.txt` | Recomputes the **second-order inputs m₂, t₂** from scratch: character algebra plus explicit SU(2) coefficient matrices, trace norms by SVD, and the lattice sum around the anchor edge | all PASS (see §1.4) |
| `check_misc.py` → `_OUTPUT.txt` | YM-05 and YM-02 constants; §27 face count by enumeration; NS-04 (a), (b) symbolically; S6-5 (and the S6-1 dimension count); overlap identities | 54/54 PASS |
| `fifth_verify_OUTPUT.txt` | The workbench's fast replay `verify.py --verify-receipt verification.json`, run on a scratch copy | PASS: 51 named checks and 11 false-formula controls; receipt byte-identical; 3.8 s |
| `fifth_producer_OUTPUT.txt` | The workbench's **full 662-row fifth-coefficient producer** (`evaluate_fifth_bounds.py --workers 2`) on the scratch copy | 51 s; all 662 regenerated rows byte-identical to the published rows |
| `fifth_full_replay_OUTPUT.txt` | The workbench's **complete polynomial/dual-certificate auditor** (`audit_spin_channels.py`), plus the anchor assembly, word tensors and return bounds (`--verify-existing`) | auditor 20 s, output byte-identical to `generated/spin_audit.json`; the other three PASS. (The first producer attempt in this log did not run because `/usr/bin/time` is missing; the log is annotated. The real run is in `fifth_producer_OUTPUT.txt`.) |
| `fc_disk_checker_OUTPUT.txt` | The workbench's `check_fixed_coupling_analytic_disk_obstruction.py` | PASS, 0.03 s |

The publication README says the producer and auditor were **not** rerun at publication (fifth-reference README L117). They are rerun here. This shows that the recorded certificates are reproducible. It does not independently verify the mathematics inside those programs (§1.4).

---

## 1. YM-01: the gap bound Δ_L ≥ κ d₅(ξ)

### 1.1 Objects (FIFTH_REFERENCE.md F1–F4; README L9–19)

- **Box.** Vertices {−L,…,L}³ with L ≥ 2 (an open box, no periodic identification). Links e are positively oriented nearest-neighbour edges inside the box. Plaquettes p = (n; i, j) with i < j are the elementary faces inside the box, M = |P_L| of them. By enumeration (my check), M = 12L²(2L+1): 240 faces for L = 2.
- **Configuration space and Hilbert space.** One SU(2) matrix U_e per link. The space is L² of the product Haar probability measure on SU(2)^E. The **physical space** is the subspace invariant under all vertex gauge transformations, boundary vertices included.
- **Hamiltonian (F2):** H_L = κK + κξ(2M − S), where
  - the **electric term** is κK, with K = −Σ_{e,a} X²_{e,a}, the sum of the link Casimirs. X_{e,a} differentiates U_e along e^{tT_a}, T_a = −iσ_a/2. On the Fourier block with link spins j = (j_e), K acts as c_j = Σ_e j_e(j_e+1);
  - the **plaquette (magnetic) term** is κξ(2M − S), with S = Σ_p W_p and W_p the trace of the ordered product of the four links around p. Since κξ = 1/(2g²a), this equals (1/(2g²a))Σ_p(2 − W_p) ≥ 0;
  - κ = 2g²/a and ξ = 1/(4g⁴). Here a > 0 is the lattice spacing and g > 0 the bare coupling.
  - The normalisation is the workbench's own. F8 records the conversion to Schütte–Zheng–Hamer's convention (g_C = 2^{3/4}g; H_ours = √2·H_C plus a constant). Numerical thresholds such as g² ≥ 3.68 are therefore in this normalisation and must be converted before comparison with other literature.
- **Domain, ground state and gap.** H_L is self-adjoint with compact resolvent (F2–F3). The ground state ψ_L > 0 is unique (identity F3). **Δ_L** is the distance from the ground energy E_{0,L} to the rest of the spectrum of H_L on the physical space.
  - At ξ = 0 the physical gap is exactly 3κ: one plaquette excited in the fundamental representation, four links of Casimir 3/4. On the full, non-gauge-invariant space it would be (3/4)κ (§3).
- **The "vacuum source"** (README L19; F14; F33–F34). Write ψ = e^v/‖e^v‖ with ∫v dU = 0. The eigen-equation Hψ = E₀ψ is equivalent (my derivation, matching F33–F34) to
  - Kv = ξS + Q_HΓ(v,v), with Γ(f,h) = Σ_{e,a}(X_{e,a}f)(X_{e,a}h), P_H the Haar mean and Q_H = I − P_H;
  - E₀ = 2κMξ − κP_HΓ(v,v);
  - equivalently v = ξv₁ + B(v,v), with B = K⁻¹Q_HΓ and v₁ = (1/3)Σ_pW_p (each W_p has Casimir 3).
  - Its formal power series v = Σ_n ξⁿv_n has v_n = Σ_{i+j=n} B(v_i, v_j). The **fifth reference** is q₅ = Σ_{i≤5} ξ^i v_i. The exponential ansatz is credited to Schütte, Zheng and Hamer (coupled-cluster method).

### 1.2 The statement (F37; README L60–68)

For every L ≥ 2, every a > 0 and every 0 < ξ ≤ α₅:

  Δ_L ≥ κ·d₅(ξ),  d₅(x) = (3/2)(1 + √𝒟₅(x)) + Σ_{i=1}^{5}((3/2)m_i − 6t_i)x^i,

together with the Poincaré-type form q_{H−E₀}(ψf) ≥ κd₅(ξ)·Var_{ψ²}(f) on the whole physical form domain. The ingredients are:
- ℓ₅(x) = Σ(m_i + 4t_i)x^i;
- δ₅(x) = Σ_{i+j≥6} b_{ij}x^{i+j}, summed over ordered pairs with i, j ≤ 5, where b_{ij} = 3(m_it_j + m_jt_i);
- 𝒟₅ = (1 − ℓ₅)² − (8/3)δ₅;
- α₅ = the first positive root of 𝒟₅;
- (m_i, t_i) = the ten rational bounds of F26.

**In the coupling.** ξ ≤ α₅ ⟺ g⁴ ≥ 1/(4α₅) ⟺ **g² ≥ 1/(2√α₅) ≈ 3.683551983985727304439** (F29). The bound is uniform in the box size and in the spacing, and it holds on the whole physical space.

### 1.3 Proof architecture, step by step, with verdicts

| Step | Content (locator) | Nature | Verdict |
|---|---|---|---|
| S1 | Fourier-algebra norm ‖f‖_X = Σ_j‖A_j(f)‖₁, submultiplicative; ‖A_j(X_{e,a}f)‖₁ ≤ j_e‖A_j(f)‖₁ (F4–F5) | analytic; standard (Eymard's Fourier algebra A(G), credited) | correct |
| S2 | **Gauge-invariance Casimir bound** (F7): on every nonzero physical block, Σ_f j_f ≥ 4j_e for each link e. Hence c_j ≥ 6j_e, Σ_e j_e ≤ (2/3)c_j and c_j ≥ 3 on the nonconstant physical space | analytic, combinatorial | **correct; re-derived by hand.** It uses the singlet (triangle) inequality at both ends of e, and at the outer ends of the neighbouring links. The cubic lattice is bipartite, so there are no triangles and each further link is counted at most twice |
| S3 | Local labelled norms ‖·‖_loc, m, t (sup over an anchor link of weighted ℓ¹ sums over labels containing it, F6); bilinear estimate ‖B(f,h)‖_loc ≤ 3(m(f)t(h) + m(h)t(f)) ≤ (2/3)‖f‖‖h‖ (F9); ‖2B(q,·)‖ ≤ m(q) + 4t(q) and ‖2Γ(v,h)‖_X ≤ 4t(v)‖Kh‖_X (F10) | analytic | **correct; re-derived by hand.** K⁻¹ cancels the output Casimir weight. An anchor in S ∪ S′ lies in S or in S′. The constants follow from S2 |
| S4 | Finite coefficient bounds (m_i, t_i), i ≤ 5 (F11–F26) | **finite computation** (§1.4) | order 1 checked by hand; order 2 recomputed independently; orders 3–4 inherited; order 5 producer and auditor rerun byte-identically, logic read but not re-implemented |
| S5 | The residual R₅ = ξv₁ + B(q₅,q₅) − q₅ contains exactly the degrees 6–10 (F27). ‖R₅‖_loc ≤ δ₅ and ‖J₅‖ ≤ ℓ₅ < 1, with J₅ = 2B(q₅,·) (F28) | algebra + S3 | **correct**: R₅ follows from v_n = Σ_{i+j=n}B(v_i,v_j) (my derivation); no degree is dropped |
| S6 | w = v − q₅ solves (I − J₅)w = R₅ + B(w,w). A Neumann inverse plus a binary-tree (Catalan) series gives ‖w‖_loc ≤ w_* = (3/4)(1 − ℓ₅ − √𝒟₅) for |ξ| ≤ α₅, **endpoint included** (F30–F32) | analytic majorant argument | **correct.** w_* is the small root of (2/3)w² − (1 − ℓ)w + δ = 0 (my check A7). At ξ = α₅, θ = 8δ/(3(1−ℓ)²) = 1 and the tail is summable (Cat_n/4ⁿ ~ n^{−3/2}); ‖J₅‖ ≤ ℓ₅(α₅) ≈ 0.896 < 1 there (my check A3) |
| S7 | v = q₅ + w solves Kv = ξS + Q_HΓ(v,v). e^v is a positive eigenfunction, hence the ground state (F33–F34, via F3) | analytic | **correct.** Any positive eigenfunction is the bottom of the spectrum by F3, so no separate identification argument is needed |
| S8 | **Spectral return** (F35–F37). A physical eigenvector with eigenvalue λ > 0 of H − E₀, divided by ψ and with its Haar mean removed, gives h ≠ 0 with (K − λ/κ)h = Q_H·2Γ(v,h). If λ/κ < 3, then (1 − λ/(3κ))‖Kh‖_X ≤ 4t(v)‖Kh‖_X ≤ χ‖Kh‖_X, with χ = 4Σt_ix^i + (2/3)w_*. Hence λ ≥ 3κ(1 − χ) = κd₅. If λ/κ ≥ 3 the bound is trivial, since d₅ ≤ 3 | analytic | **correct; re-derived by hand**, including the ground-state transform e^{−v}(H − E₀)e^{v} = κ(K − 2Γ(v,·)) and d₅ = 3(1 − χ) (my check A4). h is smooth, so Σc_j‖A_j(h)‖₁ < ∞ (F36 remark) |
| S9 | 0 ≤ χ < 1/2 on [0, α₅]; w_* is increasing, so d₅ is decreasing and d₅(α₅) > 3/2 (F35 remark) | analytic + arithmetic | correct: w_*′ ≥ 0 because √𝒟 ≤ 1 − ℓ (by hand); d₅(α₅) = 1.54530… (my check A5) |

**Is the chain from the finite computations to all L ≥ 2 complete as written? Yes, given the inputs (m_i, t_i).** L-uniformity enters in two places, both of which I checked:
- (i) Each v_n is a sum over plaquette multisets of **universal cluster functions**. B(f,h) vanishes unless the labels share a link, and K⁻¹ acts only on the links of the label. A multiset inside a box therefore gives the same function as in the infinite lattice. A boundary box contains a subset of the anchored multisets, so the infinite-lattice anchored sums bound every box (F25 L258; H6 L352–354).
- (ii) S3–S9 use only local norms and the sup-over-links quantity t(v), which is L-uniform. L enters only qualitatively, through the finiteness of Σc_j‖A_j(h)‖₁.

One bookkeeping point matters and is handled. The Fourier-algebra norm is **not** invariant under reversing link orientations, since partial transposition changes trace norms (F3; the executable checks 16 → 8). Translates of a cluster in the lattice appear in all reflected orientations, so each representative's bound must hold for all eight axis reflections. F13 takes that maximum. My order-2 recomputation shows that the effect is real and that the source handles it conservatively (§1.4).

**Verdict on YM-01.** The analytic architecture is a complete, correct and fairly standard strong-coupling argument: an exponential vacuum ansatz, a Banach fixed point in a local weighted Fourier-algebra norm, and a perturbative gap return. It is written out in F1–F42 with all steps present. The theorem is **proved, conditional only on the correctness of the finite coefficient bounds (m_i, t_i) for i = 3, 4, 5.**
- The i = 3, 4, 5 bounds are produced by exact-arithmetic programs, which I reran with byte-identical output but did not independently re-implement.
- i = 1 is verified by hand and i = 2 by an independent recomputation.
- The workbench itself says no Lean or external analytical certification is claimed (README L117; F-intro L3).

### 1.4 The finite computations

| Input | Source | Status in this audit |
|---|---|---|
| (m₁, t₁) = (64/3, 16/3) | v₁ = (1/3)ΣW_p; ‖W_p‖_X = 8 (F12 with l = 4, k = 1, d = 2); 4 plaquettes per link, Σj_e = 2, j_e = 1/2 | **verified by hand**: 4·2·(8/3) and 4·(1/2)·(8/3). ‖W_p‖_X = 8 and ‖χ₁(U_p)‖_X = 27 verified numerically (second-order check) |
| (m₂, t₂) = (5834/39, 137/6) | 16 Sep `LINEARIZED_RETURN.md` L19 (L3); 17 Sep reader md L479 | **recomputed independently (`check_ym01_second_order.py`)**, from B(W_p,W_p) = −χ₁(U_p)/8 and B(W_p,W_q) = (1/6)P₀ − (1/26)P₁ for adjacent p ≠ q (both derived by hand from 2Γ(f,h) = (c_f + c_h)fh − K(fh), F17), using explicit SU(2) coefficient tensors and SVD trace norms over all 42 adjacent pairs whose label contains the anchor. Exact values: m(v₂) = 134.067…, t(v₂) = 19.795…, ‖v₂‖_loc = 212.33…. The source's values are **valid upper bounds**. Using the reflection maximum (‖P₀‖, ‖P₁‖) = (16, 48) for all 42 pairs (14 of them actually have (8, 24√3)) reproduces **m₂ = 5834/39 and ‖v₂‖_loc = 236 exactly**. t₂ = 137/6 additionally bounds the shared-link spin-1 channel by the product norm 64 instead of 48, which is conservative |
| (m₃, t₃), (m₄, t₄) | inherited from the 16–17 Sep continuations (the 17 Sep VALIDATION reports the fourth source rerun with 1,056 named checks; two descriptions agree on 78 representatives and 8,621 anchored multisets) | **not re-derived**. Pinned by hash in the fast replay (676 inherited inputs). Consistency: (3/2)m₄ − 6t₄ equals the 17 Sep R29 constant exactly (my check) |
| (m₅, t₅) = (1638684, 190128) | this continuation: 662 representatives, 124,864 anchored multisets, 6,240 projection constraints, 5,726 rational primal/dual certificates (F14–F25) | producer and auditor **rerun here, byte-identical**. The logic (signed spin-channel recurrence F16–F18, LP duality F21, anchored transport F25) was read; it is not independently re-implemented |

**Sensitivity** (my check A10). At ξ = α₅ the fifth-order term x⁵(m₅ + 4t₅) contributes 0.0051 to ℓ₅(α₅) ≈ 0.896, and the fourth-order term contributes 0.0087. The fifth-order bounds enter δ₅ more strongly, through b₁₅.
- If m₅ and t₅ were both underestimated by a factor of 2, α₅ would drop to 0.017905 (threshold g² ≈ 3.737) and d₅(1/64) to 1.8946.
- With a factor of 1.1: α₅ = 0.018362 (g² ≈ 3.690) and d₅(1/64) = 1.9056.
- The qualitative theorem (a box-uniform gap above 1.89κ at g² ≥ 4, threshold below 3.74) is therefore robust to such errors. The displayed digits (3.6836, 1.9068) are not: they rest on the exact fifth-order computation.

### 1.5 Elementary consequences quoted (all verified, `check_ym01_arithmetic_OUTPUT.txt`)

- **α₅** ∈ (0.018424953576117616681, 0.018424953576117616682): exact bisection from the F26 rationals gives 0.01842495357611761668188…, inside the source's bracket. 𝒟₅(18/1000) > 0 > 𝒟₅(19/1000), and ℓ₅ < 1 on [0, 19/1000], so the root is unique there.
- **Threshold.** 1/(2√α₅) = 3.683551983985727304439114…, inside the F29 bracket. "g² ≥ 1/(2√α₅)" is exactly ξ ≤ α₅.
- **g² = 4** (ξ = 1/64): d₅ = 1.9068301567…, so **Δ_L > 1.9068κ**. Since d₅ decreases in ξ, this holds for all g² ≥ 4. Also w_* = 0.005751… < 0.005752.
- **g² = 3.7**: d₅ = 1.62072… (> 1.6207). **g² = 15/4**: d₅ = 1.69935… (> 1.6993). The w_* values match the F38 table.
- All coefficients (3/2)m_i − 6t_i are ≥ 0 (the i = 1 coefficient is exactly 0). d₅(0) = 3 and d₅(α₅) = 1.5453… > 3/2.
- **In lattice units** (my arithmetic), aΔ_L ≥ 2g²d₅: 11.38 at the edge of the domain and 15.25 at g² = 4. The leading strong-coupling value is 6g². This is the familiar picture of a large gap in lattice units at strong bare coupling.

### 1.6 What YM-01 is, and is not

- It is a **finite-regulator, strong-coupling** theorem: fixed lattice spacing, any box size, bare coupling above a threshold. Continuum physics needs a → 0 with g → 0 (asymptotic freedom), which is the opposite regime. The workbench says the standing path a_n = a₀2⁻ⁿ eventually leaves the domain (§4). **Nothing about the continuum mass gap follows from YM-01, and the workbench claims nothing.**
- Context, for readers; this is not a novelty assessment, and the workbench disclaims priority (F-intro L3):
  - mass gaps at strong coupling for lattice gauge theories are classical in the Euclidean setting (Osterwalder–Seiler, Ann. Phys. 110 (1978) 440–471, cited from memory and not re-checked here);
  - the coupled-cluster exponential ansatz is standard in Hamiltonian lattice work (credited).
- What the workbench adds is an **explicit, box-uniform, whole-physical-space bound for the Kogut–Susskind SU(2) Hamiltonian on open boxes, with explicit constants, a closed coupling threshold, and the endpoint included.**
- The Riemann, Jacobian and S⁶ material plays **no role** in YM-01 (F-intro L3; README L123).

---

## 2. YM-05, YM-02, YM-03

### 2.1 YM-05 (17 Sep): Δ_L > 1.6584κ for g² ≥ 15/4

- **Statement** (reader L517–534; Appendix B R24–R31): Δ_L ≥ κd_[4](ξ) for L ≥ 2, a > 0, 0 < ξ ≤ α_[4], with 0.018104972231644127075 < α_[4] < …076. Hence g² ≥ 3.715960362535435237 suffices, and g² ≥ 15/4 gives Δ_L > 1.6584κ.
- **Proof.** It is the **same architecture as YM-01** with the fourth reference q₄ in place of q₅. R24 is the residual with degrees 5–8; R25–R28 the correction; R29–R30 the return.
- **My checks** (`check_misc_OUTPUT.txt`), from the same m_i, t_i (i ≤ 4): α_[4] = 0.01810497223164412707541…, inside the bracket; d_[4](4/225) = 1.658436 > 1.6584; d_[4](1/64) = 1.898118 > 1.89811; p₄ = (3/2)m₄ − 6t₄ matches R29 exactly.
- **Relation to YM-01.** α₅ > α_[4], and YM-01 gives 1.6993κ at g² ≥ 15/4. So **YM-05's conclusion is implied by YM-01**, whatever the status of YM-05's own write-up.
- **The qualification** (`yang-mills/README.md` L29). The 17 Sep argument "retains its existing analytical-review qualification". Per VALIDATION L19 it was reviewed separately, "No missing implication was found", and it is not Lean-formalized. The 21 Sep heat edition "does not recertify the earlier stronger interval". A reader can state YM-05 as superseded by YM-01.

### 2.2 YM-02 (HEAT_AND_COMPLEMENT.md, 21 Sep, fifth-reference edition)

**Statements.**
- (H13) For every L ≥ 2 and τ ≥ 0, the connected plaquette heat correlation Ĉ_pq(τ;ξ) = ⟨r_p, e^{−τA/κ}r_q⟩ satisfies ‖Ĉ − C₀ − ξ²C₂ − ξ⁴C₄‖_row ≤ (67896/169)e^{−13τ/8}(55|ξ|)⁶/(1 − (55|ξ|)²) for |ξ| < 1/55. Here r_p = (W_p − ⟨W_p⟩)ψ.
- (H28, H5 table) After letting the whole complementary physical space relax, the plaquette-family energy and state Gram change by factors in (1999/2000, 1] and [1, 2001/2000) for g² ≥ 13, and by 1/25000 for g² ≥ 16, uniformly in L and a.
- (H34 and after) A fixed-spacing infinite-volume limit of the heat semigroup on cylinder observables, with a unique invariant state and generator A_∞ ≥ κd₅(ξ) on the centred space, for ξ < 1/55.

**What I checked.**
- **The parity step for H13 (by hand).** The staggered centre map U_{(n,i)} ↦ (−1)^{Σ_{j<i}n_j}U_{(n,i)} multiplies every W_p by −1. The two signs on the i-links cancel and the two on the j-links give −1. It preserves Haar, K and gauge action. So H(ξ) ≅ H(−ξ) + const, the connected two-point function is even in ξ, and the Cauchy remainder starts at ξ⁶. Correct.
- **Constants** (my check): 1/55 < α₅; d₅(1/55) = 1.63763 > 13/8, equivalent to χ(1/55) < 11/24; (1 + 255·11/24)/(13/24)² = 67896/169; the signed time integral H17 in closed form; e^{−13/12} < 339/1000; C_J = 5156090136/3570125; d₅ at g² = 13 is 2.904718 > 29047/10000 (the d_ph used in H30).
- **H9 by hand**: ‖Γ(h,G_z)‖_X ≤ 3·16·(2/3)‖Kh‖_X = 32‖Kh‖_X.
- The workbench's `return_bounds.py` reproduces the H5 table (e.g. at g² = 13: 0.99904…, 0.000436, 0.000450).

**What I did not re-derive.**
- The 255 in H11: the mean-return bookkeeping.
- The inherited degree-2 and degree-4 row-bound table (H19; 199 supports, 559 marked contributions).
- The Lumer–Phillips generation step (H5–H6), which reads correctly but was not checked in detail.
- The infinite-volume paragraph after H34, which is a compact outline (cylinder convergence, Markov extension, density).

**Verdict.** The constants and the logical structure are correct as far as checked. H13 follows from F31 and H11 by a standard Cauchy estimate. H28 is exact linear algebra (Schur complement over the complementary space) plus the H20 Gram bounds. Classify as **proved in writing, with finite checks; the infinite-volume statement is outline-level.**

### 2.3 YM-03 (21 Sep heat/volume edition, `consolidation/20260921/`)

- **Statements** (README L39–80): the same type of results with weaker constants. A row remainder with radius R₀ = 3/256, prefactor 512 and decay 3/2 (a second bound has radius 45/4096). A fixed-spacing spatial-volume limit (U9). Full-complement energy retained above 999/1000 at g² ≥ 16.
- README L51 states the limit is "not a limit as the lattice spacing tends to zero".
- **Relation.** YM-02 **supersedes YM-03 quantitatively**: radius 1/55 > 3/256; 1/25000 < 1/1000 at g² ≥ 16. YM-03's proof does not use the fifth-order catalogue, so it is an independent, weaker route.
- **Status.** Statements read; the five proof manuscripts were **not** audited here.

---

## 3. YM-07 §27: exact collapse of the finite-box weak-coupling disk at fixed coupling

**Precise statement** (`spatial_continuum.md` L8275–8359). Take the same Hamiltonian, written H = (2g²/a)(H₀ − ξW_L) + (M_L/(g²a))I, where H₀ = ΣE_e acts on the **full** L²(SU(2)^E) (no gauge projection) and W_L = Σ_pW_p. Then:
- ‖ξW_L‖ = 2|ξ|M_L, attained at U ≡ I (FC4);
- the nonzero spectrum of H₀ starts at 3/4 (FC5);
- on |z| = 3/8, ‖(H₀ − z)⁻¹‖ ≤ 8/3;
- the global operator-norm Neumann series therefore certifies invertibility on that circle, and the rank-one Riesz projection, **only for |ξ| < 3/(16M_L) = 1/(64L²(2L+1))** (FC8);
- along L = j² this radius is ~ 1/(128j⁶), so at any fixed g it eventually excludes ξ = 1/(4g⁴) (FC9).

**Scope** (the section's own words, L8354–8358). It is an obstruction to "this volume-uniform perturbative certification route". It does not show that the true analyticity radius is that small, and it proves neither a mass gap nor its absence.

**Terminology note for readers.** "Weak-coupling disk" here means small |ξ|, i.e. a weak plaquette term, which is **large** g, the strong-coupling regime of YM-01. The two results concern the same parameter.

**Check.**
- FC1 face count by enumeration for L = 2…6 (my check; the workbench checker uses the closed formula).
- FC3 decomposition and FC6 ratio by hand; FC8 and FC9 by hand and by rational arithmetic. The workbench checker passes.
- **Correct.**

**Why it matters for the reader.** At L = 2 the certified disk is already |ξ| < 1/1280, far inside ξ ≤ α₅ ≈ 0.0184. §27 explains why YM-01 needs local norms: the global operator norm of the plaquette term grows with the number of faces, while the local norms in F6 do not.

---

## 4. What the workbench says it does not prove (with locators)

- **Continuum mass gap.**
  - Top README L35: "They do not constitute a claimed solution" of the interacting 4-D problem.
  - WORKBENCH L21: the continuum/mass-gap question "remains unresolved in this collection".
  - `yang-mills/README.md` L29: neither edition "establishes a four-dimensional continuum field or a finite positive continuum mass". L59: "do not establish or refute" the 4-D continuum mass gap.
- **The standing continuum path** (fifth-reference README L125; H7 L369–370). a_n = a₀2⁻ⁿ, g_n² = 1/c_n, c_n = g₀⁻² + βn log 2, so ξ_n = c_n²/4.
  - The source domain requires c_n ≤ 2√α₅ (⟺ ξ_n ≤ α₅) and the heat circle requires c_n < 2/√55 (⟺ ξ_n < 1/55). Both equivalences were verified.
  - For β > 0, "the path eventually leaves both". The estimates "do not establish a nontrivial four-dimensional continuum field or a finite positive continuum mass".
- **Certification.**
  - Fifth-reference README L117: "No Lean or independent external analytical certification is claimed".
  - F-intro L3 disclaims review, formal proof, priority and "a continuum mass gap".
  - PUBLIC_VALIDATION scope: `continuum_mass_gap_established: false`, `analytic_arguments_formalized: false`, `external_analytical_review: false` (reproduced in my fast replay).
  - `research-control/state.json`: `continuum_gap_proved: false`.
- **Missing material.**
  - The sixth-source catalogue "remains missing" (H7 L374).
  - The 19 Sep spatial tables and final execution package "were not supplied" (WORKBENCH L13).
  - The "uncertified full-L2 tensor contraction calculation" is excluded (`yang-mills/README.md` L67).
- **Cross-programme.**
  - RH_HEAT_TRANSFER L31–32: a zeta-to-gauge map "is not asserted". T7 L299–300: "no identification of arithmetic zeta zeros with physical spectral points".
  - Survey §2c lists the Fabel/NS disclaimers (FABEL_CORRECTIONS L66; addendum L195).

---

## 5. Navier–Stokes material

### 5.1 NS-00 (imported source; not audited)

- **What the workbench records.** The OpenAI manuscript *Finite Time Blowup for Navier–Stokes*, Theorem 1.1 (paraphrase, per survey NS-00). For every ν > 0 there are a compactly supported smooth force and zero initial velocity giving a smooth solution on [0,1) with bounded energy and lim sup_{t↑1}‖u(t)‖_∞ = ∞. The manuscript's Cor. 10.6 gives the same on 𝕋³.
- **Status.** It is **imported**. The YM repository holds an independent LaTeX transcription (Zenodo 22852310) and a 208-page reconstruction reader. The NS README L31 says "complete independent analytic and Lean validation remains unfinished" and that the collection is not a claim of discovery.
- Nothing in this audit verifies Theorem 1.1. Every downstream use (the NS → YM edge of `21_` §2; the zeta NS satellites) is conditional on it.

### 5.2 NS-04 (vacuum hydrodynamics, 19 Sep; README L23–156)

**(a) Exact nonlinear Einstein constraint data with a left inverse on marked data. Verified.**
- *Construction.* V ranges over compactly supported smooth divergence-free fields on ℝ³, with strain S_V.
  - The tensor L_bV on ℝ⁴ = ℝ_w × ℝ³ is built from the strain and b(w) (L27–33).
  - Its constant-background shift is Ā = −a_*diag(−3,1,1,1) + β_*L_bV, with −3 on the w-slot (L122 gives Ā_ww = 3a_* > 0).
  - The Lichnerowicz equation −6Δ₄φ + κ_*φ³ − qφ⁻⁵ = 0 with q = |Ā|² and φ → 1 at infinity.
  - The data (h, K) = (φ²δ, φ⁻²Ā + (τ_*/4)φ²δ).
- *Result.* These are vacuum constraint data in 4 spatial dimensions with Λ = −6/L². The volume-weighted tracefree E-block at w = 0 returns β_*S_V, and the Newton decoder returns V. So 𝒟∘ℰ = id **on marked data** (L84 limits injectivity to that).
- *My symbolic check* (`check_misc.py`, an explicit V = curl A). L_bV is tracefree and divergence-free in all four components; |L_bV|² = b′²|S|² + b²|ΔV|²/2; ⟨diag(−3,1,1,1), L_bV⟩ = 0, so q ≥ κ_*; ΔV_i = 2∂_jS_ij (the decoder); φ⁴TF_E(K^♯) = β_*S at w = 0.
- *By hand.* The n = 4 conformal exponents (6, φ³, φ⁻⁵) and the φ³ coefficient (3/4)τ_*² − 2Λ = 12a_*² = κ_*.
- *Existence and uniqueness.* The barrier argument (subsolution 1, supersolution (‖q‖_∞/κ_*)^{1/8}, monotone solves) is the standard one and reads correctly. The existence proof itself was not re-checked beyond the barrier inequalities.
- *What it is.* An exact **encoding of a velocity snapshot** into gravitational constraint data. It is not a dynamical correspondence: L117–122 show that inserting the NS time as Einstein time gives a nonzero defect.

**(b) Homogeneous Kasner bijection onto P_w < 1/4. Verified.**
- *Definitions* (L88–104). For constant tracefree S, B = −2νS/c², χ = √(1 + (4/3)trB²), P_w = 1/4 − 3/(4χ), P_⊥ = I/4 + (I/4 + B)/χ.
- *My symbolic check with generic S.* tr P = tr P² = 1; the displayed inverse returns S; the derivative at 0 is −2νS/c².
- *Surjectivity* (by hand; numeric round trip on 200 random block-Kasner data). The inverse B = (3P_⊥ + (P_w − 1)I)/(1 − 4P_w) is tracefree, and 1 + (4/3)trB² = 9/(1 − 4P_w)² on the Kasner set, so χ = 3/(1 − 4P_w) and the forward map returns (P_w, P_⊥).
- *Range.* The Kasner conditions force P_w ≥ −1/2, so the image is P_w ∈ [−1/2, 1/4).
- **Correct.**

**(c) The Rindler response.** Not audited. By its own account the pole collision location is **numerical, not interval certified** (L145–152).

**(d) Slab-stress regularity theorem for a modified equation** (SLAB_COMPARATORS §2, L92–139). NS with an added positive Fourier multiplier from an elliptic slab extension has a unique global smooth solution. The multiplier's symbol m(k) is squeezed by tanh bounds (S5), and the total damping satisfies d(k) ≥ c_*k³ at high frequency.
- The proof uses Gagliardo–Nirenberg with exponent 3/5, then Young and Grönwall on ‖∇U‖², then a mild-solution continuation. It reads correctly.
- This is the **standard hyperdissipative mechanism**: dissipation of order |k|^{2α} with α ≥ 5/4 gives global regularity, and here 2α = 3. The source says so and claims no priority (L101, citing Tao 2009).
- It concerns a **modified** equation, not NS.
- **Correct as a statement; standard.**

---

## 6. S⁶ reader (`s6/27_…tex`, 325 lines)

The five advances (paraphrase). Proofs are cited to the Zenodo archive 10.5281/zenodo.22678442, which is not in git.

| ID | Statement | Proof in git | Audit here |
|---|---|---|---|
| S6-1 | For the analytic fibration f: X → ℙ¹ with multiple fibres 3S₁, 4S₂: ω_X ≅ 𝒪_X(−2S₂), ω_X^{−2} ≅ f*𝒪(p₂), f_*𝒪_X(kS₂) = 𝒪(⌊k/4⌋p₂). The anticanonical ring is ℂ[U,V] with deg U = 1, deg V = 2, and the degree-2 map recovers the fibration (L33–74) | no (workbench Thm 53.17, pp. 699–700; `analytic_canonical_ring.tex`) | not audited. **Internal consistency only** (my check): h⁰(ω^{−m}) = ⌊2m/4⌋ + 1 = ⌊m/2⌋ + 1 equals dim ℂ[U,V]_m for m ≤ 60 |
| S6-2 | The period constant gives a nonzero Kodaira–Spencer class KS(∂_c) ≠ 0 | no (Thm 53.18) | not audited |
| S6-3 | Finite fillings: product covers of degrees 9 and 8; the central attachment kernel is ≅ ℤ; normal-line trivialization | no | not audited |
| S6-4 | For N ⊃ R = A₅^{⊥4} ⊥ D₄ with [N:R] = 72: value-group inclusions diag(1,4,1), diag(1,1,3), total quotient ℤ/12; det Q_𝕆(λ; y) = λ³ − λ(y,y) + 2F(y) | no (higher-rung paper §§9–11) | not audited. Arithmetic only: [N:R] = √(6⁴·4) = 72 (N unimodular), and ℤ/4 × ℤ/3 ≅ ℤ/12 |
| S6-5 | Λ_cyc ∩ ℒ(N) = Λ_cyc ∩ ℒ(Le) = ℐ = {√2(a,a,a): a ∈ D₄}, with Gram 6G_{D₄}, det 5184, min 12. τ(√2(a,a,a)) = 2√2·P(a), P(a) = a₀(a₀² − 3(a₁²+a₂²+a₃²)). The values generate 4√2ℤ, but 12√2 is not attained | **partly**: the mod-3 argument is at L289–292 | **checked** (below) |

**S6-5 check.**
- *Gram, det, min.* ⟨√2(a,a,a), √2(b,b,b)⟩ = 6⟨a,b⟩, so the Gram is 6G_{D₄}, det = 6⁴·4 = 5184, min = 6·2 = 12.
- *The cubic.* a lies in the quaternion subalgebra, which is associative, so τ = Re((qq)q) = 2√2·Re(a³). Re(a³) = a₀(a₀² − 3|v|²) was verified with an explicit quaternion product.
- *The generated group.* On D₄, P is always even: if a₀ is odd then |v|² is odd. P(1,1,0,0) = −2. So the generated group is 2√2·2ℤ = 4√2ℤ (brute force over |a_i| ≤ 6 confirms gcd 2).
- *12√2 not attained.* P ≡ a₀³ (mod 3), so 3 | P forces 3 | a₀, and then 9 | P. P = 6 is impossible. The argument does not even need D₄; no integer solution exists in |a_i| ≤ 8.
- **Correct.**
- Not checked: the literal intersection claim Λ_cyc ∩ ℒ(N) = ℐ, which needs Wilson's construction and the fixed embedding ℒ.

**Own scope** (L315–320). These advances do not certify every global step of the S⁶ claim or give a CDP20 counterexample, and "No interacting quantum-field-theory mass-gap conclusion follows". It is "not independent expert adjudication or Lean formalization". Attribution wording differs across files (survey §10 D2). The TeX says the construction was "circulated by Levent Alpöge with Fable"; ATTRIBUTION says "produced with Claude". A reader should follow ATTRIBUTION.md, which the workbench designates as the clarification.

---

## 7. Overlaps

| Edge | What is shared | Type | Audit status |
|---|---|---|---|
| YM ↔ zeta, heat Gram lemma (RH_HEAT_TRANSFER T1–T5; zeta HM6–HM14, HM19–HM24) | One Hilbert-space lemma: a relative column error δ gives the Gram sandwich (1−δ)²Φ*Φ ⪯ Φ_J*Φ_J ⪯ (1+δ)²Φ*Φ; the YM instance takes δ from e^{−Ta₀} | **proved shared lemma** (two instances); no arithmetic content transferred | `21_` §3, Lemma 21.5: **C** (δ ≤ 1 needed; the source assumes δ < 1) |
| YM ↔ zeta, T7 "inverse-power conductor observability" (RH_HEAT_TRANSFER L247–300) | Left inverse W = (G⁽¹⁾)⁻¹R* on the 240 plaquette columns at L = 2, g² ≥ 20; observation fraction > 150/221 | **proved shared linear-algebra pattern** (zeta IK9–IK12), instantiated; T7 L299–300 excludes any zeta-zero identification | arithmetic checked here: (3/10)²/(51/50) = 3/34 and (3/34)/(13/100) = 150/221, using c*G₁G₀⁻¹G₁c ≥ λ_min(G₁)²‖c‖²/λ_max(G₀). The Gram bounds A23/A25 are not re-derived |
| YM ↔ zeta, AMT7–10 and OK1–2 (`research-control/RESEARCH_NOTE.md` L22 (L184–191) and L25 (L219–225)) | Composed minimum-lift identity S_{Λ₂Λ₁,Q} = S_{Λ₁,Q}S_{Λ₂,Q₁}; Pythagorean identity for the Q-minimum section | **identity** (standard finite-dimensional Schur-complement algebra), instantiated on YM spaces; "arithmetic constants … not assigned to Yang–Mills" (L245) | both identities verified on random exact rational matrices (my check) |
| YM ↔ Jacobian map (Fabel files; YM-08, YM-09) | F → incompressible flow → material tensor K_τ → lattice local-energy weights → trial states; Theorem 14.2 | **proved map** at each algebraic step; the YM end is finite-regulator weak coupling | `28_` §§1–2 (**C**); `34_`: **Cc**, conditional on the fixed-box weak-coupling limits. Q_j is the free two-gluon threshold and "does not bear on the mass gap" |
| YM ↔ S⁶ (magnetic background; YM-11) | The imaginary period block B of Π(z); only D = det B enters on the non-wrapping patch | **proved map / identity**; the S⁶ identification "is not an input" | `28_` Lemma 28.2: **C** |
| YM ↔ NS (NS profile as curvature source; YM-10) | Reducible SU(2) connection A_i = λu_iT; curvature masses; a zero-quotient diagonal with g → 0 | **proved map** + **dependency** on imported NS rate bounds | `21_` §2: **Cc**. Scope limit 21.4: at fixed coupling nothing follows |
| YM ↔ Collatz (research-control `check.py` L238–243) | X_v(q) − X_u(q) = (q−3)(q+4)/32 and X_u(3) = X_v(3) = 19/32, from an external Collatz note | **regression fixture** only; `state.json` says regression-only | identity verified (my check). It carries no YM content |
| YM-01 ↔ everything above | none | none: F-intro L3 and README L123 state that the Riemann, Jacobian and S⁶ inputs are not hypotheses of the fifth-source calculation | confirmed by reading F1–F42: no cross-programme object appears |

---

## 8. Not checked in this pass

- **The fifth-order coefficient logic** (F14–F25). I did not re-implement the signed spin-channel recurrence, the 6,240 projection constraints, the LP duality certificates or the anchored transports. I only reran the workbench's own producer and auditor, with byte-identical results.
- **Orders 3 and 4** (m₃, t₃, m₄, t₄). They are inherited from 16–17 Sep and pinned by hash; not re-derived.
- **The heat part.** The constant 255 in H11; the inherited degree-2/4 row-bound table (H19); Lumer–Phillips details; the infinite-volume paragraph after H34.
- **YM-03's five proof manuscripts; YM-04** (19 Sep, with unreplayed components); **YM-06** (14–16 Sep); **YM-13** research-control beyond L19–L25.
- **NS-04.** The Lichnerowicz existence proof beyond its barrier inequalities; (c) Rindler/Bessel; the H² → H^s bootstrapping in (d).
- **NS-00 to NS-03, NS-05, NS-06**: not audited.
- **S⁶.** S6-1 to S6-4 (proofs on Zenodo only). The literal-intersection part of S6-5.
- **The 17 Sep YM-05 write-up itself** beyond R24–R31. It is implied by YM-01 anyway.
- **External literature** (Osterwalder–Seiler; Schütte–Zheng–Hamer; Eymard; Lumer–Phillips; Tao 2009) was not re-read. No web access was used.

---

## 9. Results that stand without the workbench's vocabulary (reader candidates, one line each)

1. **Strong-coupling gap (YM-01).** For the SU(2) Kogut–Susskind Hamiltonian on any open cubic box {−L,…,L}³ (L ≥ 2) and any spacing a, the gauge-invariant spectral gap is at least κd₅(1/(4g⁴)) whenever g² ≥ 3.6836 (e.g. > 1.9068·2g²/a for g² ≥ 4). Proved in writing, conditional on computer-generated coefficient bounds that reproduce exactly.
2. **Box-uniform vacuum.** In the same range, the ground state is e^v with v = Σ_{i≤5}ξ^iv_i + w, and the correction w is explicitly bounded uniformly in the box (F31).
3. **Gauge-invariance Casimir inequality.** On the cubic lattice, every gauge-invariant Fourier block satisfies c_j ≥ 6j_e for every link, so the physical electric gap is 3 (F7). A short standalone combinatorial lemma.
4. **Trace norm of a trace word.** The coefficient matrix of tr(U₁^{±1}⋯U_l^{±1}) in d-dimensional representation variables has trace norm d^{l−k}, where 2k is the number of cyclic sign changes (F12). Standalone linear algebra; checked for the plaquette (8) and its spin-1 character (27).
5. **Box-uniform heat remainder (YM-02, H13).** Connected plaquette heat correlations equal their ξ⁰, ξ², ξ⁴ terms up to an explicit remainder of order (55|ξ|)⁶e^{−13τ/8}, uniformly in the box (|ξ| < 1/55).
6. **Near-completeness of plaquette response vectors (YM-02, H28).** For g² ≥ 13, relaxing the entire complementary physical space changes the plaquette-family energy by less than 1/2000 (1/25000 for g² ≥ 16), uniformly in box and spacing.
7. **Negative result (§27).** The global operator-norm Neumann argument certifies analyticity of the ground-state projection only for |ξ| < 1/(64L²(2L+1)), which shrinks with the box. Box-uniform results need local norms.
8. **Encoding a velocity field in gravitational initial data (NS-04a).** Every compactly supported divergence-free velocity field gives exact vacuum constraint data (4+1 dimensions, Λ = −6/L²), and the field is recovered by an explicit left inverse on marked data.
9. **Strain ↔ Kasner exponents (NS-04b).** An explicit smooth bijection between tracefree 3×3 strains and block-Kasner exponent data with p_w < 1/4, linear to first order.
10. **A modified NS equation is globally regular (NS-04d).** Adding the damping of an elliptic slab extension gives global smooth solutions. Standard hyperdissipation mechanism; not NS itself.
11. **A value-group versus value distinction (S6-5).** On {√2(a,a,a): a ∈ D₄} the octonionic cubic takes values generating 4√2ℤ but never 12√2, because a₀(a₀² − 3|v|²) = 6 has no integer solution (3 | P forces 9 | P).
12. **Conditional, not a mass-gap statement (from `34_`).** Theorem 14.2's low-mode sequence reproduces the free two-gluon threshold of a shrinking-coupling box. A reader should present it as such, if at all.
