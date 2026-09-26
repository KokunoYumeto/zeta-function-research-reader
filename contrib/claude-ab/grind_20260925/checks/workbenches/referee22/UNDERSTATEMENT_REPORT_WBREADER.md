# Understatement and missed-generality report on "Four workbenches and where they meet"

Referee 22 (Claude, Opus 5.5), 26 September 2026. I wrote none of the reader, the notes or the first-pass reports. I worked read-only; every file I made is in `scratchpad/referee22/`.

**What was read.** The whole reader (`wbreader/*.tex` and the 28-page PDF). The audit notes `43_`–`47_` and the first-pass reports `43a_`–`46a_`. The YM source F1–F42 (`FIFTH_REFERENCE.md` at `fa79faf`, extracted to my folder). The Collatz literature reader's verification table (`01k_computational_verification.tex` at `caf04ff`). The first pass's mod-840 script (`audit43_es/check_extras.py`).

**Re-runs of the reader's own checks.** `generality_checks.py` gives output identical to the recorded one. `workbench_reader_claims_checks.py` passes all 47 items (6 s).

**The brief.** Find understatement and missed generality, and flag any overclaim. Every stronger statement below is proved here and checked by a script in `referee22/` (listed at the end). Page numbers are those of `wbreader.pdf`.

## Summary

| # | Where (page) | Class | Finding |
|---|---|---|---|
| M1 | Thm 4.1 status (p. 17); YM-05 (p. 19); §5.4 (p. 25) | MAJOR | The proof of Thm 4.1 works at every truncation order. Orders 1–2, whose inputs are verified, already give an audited gap theorem: closed form for g² ≥ 8/√3; Δ_L > 1.52κ for g² ≥ 4.0187. YM-05 does not use order 5. |
| M2 | Cor 2.9 (p. 11) | MAJOR | The same bounds follow from a verification range of only 2.17·10²⁰ ≈ 2^67.56. Barina's 2021 range 2⁶⁸ already suffices. |
| M3 | Thm 1.1(a),(c) (p. 4) | MAJOR | For p ≡ 1 (mod 4) the least denominator satisfies x < p/2, not only x ≤ 3p/4. The shell range halves: 3h+1 ≤ x ≤ 6h. |
| M4 | Lemma 4.2 (p. 17) | MAJOR | The sharp constant is the girth: Σ_f j_f ≥ g·j_e on any loopless graph of girth g, for real weights satisfying only the vertex inequalities. |
| M5 | after Prop 1.3 (p. 6) | MAJOR | "All 989 survivors are ≡ 1 (mod 24)" is a theorem, not an observation. The residual-7 criterion simplifies at p ≡ 1 (mod 24). The survivors are also squares mod 7. |
| M6 | §1.3 (p. 6) | MAJOR | The mod-840 reduction is proved, not merely classical: five explicit identities do it, and the first pass's check was already a complete proof. |
| M7 | Thm 3.1 (p. 13); Thm 3.8(b) (p. 15) | MAJOR | g₄(n+3q) ≤ 19^q·g₄(n), because the top level of the base-19 construction only needs integer admissibility. A second digit set {2,3,5} exists. The constants improve by factors 1.9, 11.7 and 3.8. |
| m1 | Thm 1.1(b) (p. 4) | minor | The count holds for every a > p/4 with p ∤ a. |
| m2 | Props 1.2–1.3 (p. 5) | minor | Both hold for every prime p ≡ 1 (mod 4). |
| m3 | item 26 (p. 6); §6 (p. 26) | minor | Item 26's status can name more of what was audited, and the 22-digit prime has a Pocklington proof. |
| m4 | Thm 2.8 (p. 10) | minor | The proof also gives m ≥ 1636 and A ≥ 2593. Verifying to 2³³ (2 min) gives k ≥ 79,080, m ≥ 190,537 with no external input. |
| m5 | Prop 2.5 (p. 9) | minor | The exact descent criterion is F_m(n₀) < n₀ (an iff). |
| m6 | Thm 2.2(c), Prop 2.1 (p. 8) | minor | Both limits in (c) are uniform in b with polynomial rates; the bound in Prop 2.1 is strict. |
| m7 | Thm 2.10 (p. 11) | minor | The (K−2)-jet *never* determines λ, not merely "not in general". |
| m8 | pp. 10, 11, 17, 19 | minor | Audited results left out (tail bounds, the Tao-clock rate, the Poincaré form, d₅ > 3/2 on the whole range, …). |
| m9 | §3 (pp. 12, 14) | minor | Λ₃ = 3 follows at once, and Λ₃ > Λ₄ > Λ₅. |
| m10 | Thm 3.1 lower bound (p. 13) | minor | M_n can replace 19^{n/3} in the lower bound. |
| m11 | Prop 4.5 and the sentence after it (p. 19) | minor | On the physical space the radius is 3/(4M_L), 1/320 at L = 2. No contour does better. |
| O1–O2 | p. 19 | overclaim / inaccuracy | The 1/1280 comparison uses the full-space radius against a physical-space theorem. YM-05's dependence on order 5 is misstated. |

---

## MAJOR findings

### M1. Theorem 4.1 is conditional only for its constants; an audited version follows from the same proof

**Location.** §4.1, Theorem 4.1 and its status line (p. 17). §4.3, the YM-05 bullet (p. 19). §5.4, "Method obstructions" (p. 25).

**What is understated.**
- Status: "Conditional on the computed coefficient bounds of orders 3, 4 and 5."
- YM-05: "conditional as Theorem 4.1, since it is implied by it".
- §5.4: "Theorem 4.1 obtains, conditionally and on the physical space for real ξ".

**Stronger statement.** For 1 ≤ N ≤ 5 put:
- ℓ_N(x) = Σ_{i≤N}(m_i+4t_i)x^i;
- δ_N(x) = Σ_{i,j≤N, i+j≥N+1} 3(m_it_j+m_jt_i)x^{i+j};
- 𝒟_N = (1−ℓ_N)² − (8/3)δ_N, with α_N its first positive root;
- d_N(x) = (3/2)(1+√𝒟_N(x)) + Σ_{i≤N}((3/2)m_i − 6t_i)x^i.

Then, for every L ≥ 2, every a > 0 and every 0 < ξ ≤ α_N, Δ_L ≥ κ·d_N(ξ). The case N uses only (m_i, t_i) for i ≤ N. In particular:

- **N = 1 (inputs verified by hand).** 𝒟₁(ξ) = 1 − 256ξ/3 exactly, so α₁ = 3/256. Hence Δ_L ≥ (3/2)κ(1 + √(1 − 64/(3g⁴))) for every g² ≥ 8/√3 ≈ 4.6188, and so Δ_L ≥ (3/2)κ on that whole range. Values: 2.074κ at g² = 5, 2.830κ at g² = 10.
- **N = 2 (order 2 recomputed independently in the first pass).** α₂ = 0.0154800849822…, i.e. g² ≥ 4.01867915388…. Also d₂ ≥ d₂(α₂) = 1.52094 on the whole range. Values: 1.766 at g² = 4.1, 2.303 at g² = 5.
- **N = 4 (no order-5 input).** α₄ = 0.01810497223164…, i.e. g² ≥ 3.71596036…. Values: d₄(1/64) = 1.898118 and d₄(4/225) = 1.658436. This is YM-05, which therefore depends on orders 3–4 only.

So the qualitative content of Theorem 4.1 is audited with no unverified input: a gap on the whole physical space, uniform in the box and the spacing, at every bare coupling above an explicit threshold. Orders 3–5 lower the threshold from 4.0187 to 3.6836 and raise the constants.

**Proof.** The source's analytic core (F27–F37) is written for q₅, but no step uses the order.
1. *Residual.* For q_N = Σ_{i≤N}ξ^iv_i, the recursion v_n = Σ_{i+j=n}B(v_i,v_j) (n ≥ 2) gives ξv₁ + B(q_N,q_N) − q_N = Σ_{i,j≤N, i+j≥N+1} ξ^{i+j}B(v_i,v_j). Its local norm is at most δ_N(|ξ|) by F9.
2. *Linear part.* ‖2B(q_N,·)‖ ≤ m(q_N) + 4t(q_N) ≤ ℓ_N by F10.
3. *Correction.* The Neumann inverse and the Catalan majorant (F30–F32) give ‖w‖_loc ≤ w_* = (3/4)(1 − ℓ_N − √𝒟_N) on [0, α_N]. Here ℓ_N < 1: if ℓ_N reached 1 before α_N, 𝒟_N would be negative there.
4. *Return.* The return (F35–F37; Proposition 4.4) with χ = 4Σ_{i≤N}t_iξ^i + (2/3)w_* gives λ ≥ 3κ(1 − χ) = κd_N(ξ).
5. *Monotonicity.* The argument of F35 (w_*′ = (δ′ + ℓ′w)/√𝒟 > 0) is generic, so d_N decreases on [0, α_N].
6. *Size of d_N.* The coefficients (3/2)m_i − 6t_i are 0 for i = 1 and 87.38 for i = 2, so d_N ≥ 3/2 for N ≤ 2.
7. *The case N = 1.* Here ℓ₁ = 128ξ/3 and δ₁ = 6m₁t₁ξ² = 2048ξ²/3. So 𝒟₁ = 1 − 256ξ/3 + (16384/9 − 16384/9)ξ² = 1 − 256ξ/3, and (3/2)m₁ − 6t₁ = 32 − 32 = 0.

Corroboration: the workbench's YM-03 edition uses the radius R₀ = 3/256 = α₁ for its row remainder, and 46a §2.3 says that YM-03 does not use the fifth-order catalogue.

**Check** (`r1_ym_orderN.py`, `r8_ym_extra.py`; exact F26 rationals, 50-digit bisection).
- *Reproduction.* The script gives α₅, the threshold 3.6835519839857, d₅(1/64) = 1.9068301567, and 46a's α₄, d₄(1/64) = 1.898118 and d₄(4/225) = 1.658436.
- *Order 1.* 𝒟₁ ≡ 1 − 256ξ/3 identically, and α₁ = 3/256.
- *Monotonicity.* Every d_N decreases on [0, α_N] (401-point grid).
- *Sensitivity.* The reader says errors in orders 3–4 "were not assessed"; they can now be assessed:
  - orders 3–5 all doubled: threshold 3.775, d₅(1/64) = 1.877;
  - orders 3–5 multiplied by 4: threshold 3.899, d₅(1/64) = 1.801;
  - orders 3–5 multiplied by 10: threshold 4.127, and the order-2 bound still covers g² ≥ 4.019;
  - orders 3–4 alone doubled: threshold 3.730, d₅(1/64) = 1.890.
- *Exact order-2 values.* Using the first pass's floating-point values m(v₂) ≤ 134.07 and t(v₂) ≤ 19.80 instead of F26 gives threshold 3.978 and d₂(1/64) = 1.647. These are not needed for the N = 2 statement above.

**Suggested wording.**
- After Theorem 4.1, a new corollary: "*Corollary (inputs audited).* The proof of Theorem 4.1 is uniform in the truncation order: with q_N in place of q₅ it gives Δ_L ≥ κ d_N(ξ) for 0 < ξ ≤ α_N, using only (m_i, t_i) for i ≤ N. For N = 1 (inputs by hand) this is Δ_L ≥ (3/2)κ(1 + √(1 − 64/(3g⁴))) for all g² ≥ 8/√3 ≈ 4.619. For N = 2 (order 2 recomputed) it is Δ_L ≥ κ d₂(ξ) > 1.52κ for all g² ≥ 4.0187. *Status: audited (analytic core audited; order 1 by hand; order 2 recomputed).*"
- Theorem 4.1's status line: "Conditional on orders 3–5 for the threshold 3.6836 and the displayed constants; the qualitative statement holds without them from g² ≥ 4.0187 (Corollary)."
- YM-05: "the same argument with four orders; it uses orders 3–4 but not order 5, and is implied by Theorem 4.1".
- §5.4: "…obtains a box-uniform physical gap by local norms, unconditionally for g² ≥ 4.02 and conditionally on orders 3–5 down to 3.68".

### M2. Corollary 2.9 needs only a verification range of 2.17·10²⁰, which Barina's 2021 range 2⁶⁸ covers

**Location.** §2.5, Corollary 2.9, with its status and proof (p. 11). Also the certificate table in §5.4 (p. 25).

**What is understated.** "Assume that every n < 2^71 reaches 1, as verified by Barina".

**Stronger statement.** The conclusions m ≥ 72,057,431,991, A ≥ 114,208,327,604 and k ≥ 29,906,536,378 hold as soon as every n < 2.17·10²⁰ reaches 1. Precisely, it is enough that no nontrivial cycle has least element at most s_lo = 1/(2^{10439860591/6586818670} − 3) = 2.168901553405·10²⁰ ≈ 2^67.5555.
- *Which verification suffices.* The workbench's own literature reader records Barina (2021), n < 2⁶⁸, in its verification table; so does 44a §2.7. Barina's 2021 range therefore suffices, and the corollary does not depend on the 2025 computation.
- *Total length.* In steps of n ↦ n/2, 3n+1, a nontrivial cycle has A + m ≥ 186,265,759,595 steps.
- *Oliveira e Silva's range.* For n ≤ 20·2⁵⁸ ≈ 2^62.32, the same method gives m ≥ 6,586,818,670, A ≥ 10,439,860,591 and k ≥ 2,733,776,749.

**Proof.**
1. As s grows, the fraction of least denominator in (log₂3, log₂(3+1/s)] runs through the best upper approximations of log₂3.
2. 114208327604/72057431991 is that fraction exactly for s ∈ (s_lo, s_hi]. Here s_hi = 1/(2^{114208327604/72057431991} − 3) = 4.3585·10²¹ ≈ 2^71.884, the reader's upper end. The lower end s_lo comes from the previous best upper approximation, 10439860591/6586818670.
3. For every s > s_lo the interval is contained in the one just above s_lo, so m ≥ 72,057,431,991.
4. A and k then follow as in the reader's proof. For the minimal pair, k ≥ 2m − A = 29,906,536,378, and m(2 − log₂(3+1/s)) grows with m.

**Check** (`r4_eliahou.py`: Stern–Brocot staircase at 150 digits).
- It reproduces m = 1636 at s = 330,751 and A = 17,087,915 at 2⁴⁰ (Eliahou).
- The staircase line reads "114208327604/72057431991: s ∈ (2.1689016·10²⁰, 4.3584872·10²¹], log₂ 67.5555–71.8843".
- s = 2⁶⁸ and s = 2⁷¹ give identical bounds; the reader's own `generality_checks` output already shows the same m* at 2⁶⁸.

**Suggested wording.**
- Statement: "Corollary 2.9. Assume that every n < 2.17·10²⁰ reaches 1 (verified by Barina: to 2⁶⁸ in 2021 and to 2⁷¹ in 2025). Then …"
- Status: "The fraction is the least-denominator one for every verified range between 2^67.56 and 2^71.88, so the bound needs only Barina's 2021 range; a nontrivial cycle has at least 186,265,759,595 steps of n ↦ n/2, 3n+1."
- New reference: D. Barina, *Convergence verification of the Collatz problem*, J. Supercomputing 77 (2021) 2681–2688. This is as recorded by the workbench; check it against the publisher page, as was done for the 2025 paper.
- In the §5.4 table: "all n < 2.17·10²⁰ (Barina 2021/2025)".

### M3. Theorem 1.1(a),(c): for p ≡ 1 (mod 4) the least denominator lies in (p/4, p/2)

**Location.** §1.1, Theorem 1.1(a) and (c) (p. 4).

**What is understated.** "then p/4 < x ≤ 3p/4; for p = 12h+1 this is 3h+1 ≤ x ≤ 9h".

**Stronger statement.** Let p be an odd prime and x ≤ y ≤ z a solution. Then x < p/2 and x < y. The only exception is p ≡ 3 (mod 4) with (x, y, z) = ((p+1)/2, (p+1)/2, p(p+1)/4). Hence:
- for p ≡ 1 (mod 4), p/4 < x < p/2 and x < y;
- for p = 12h+1, 3h+1 ≤ x ≤ 6h;
- (c) becomes: the equation is solvable at a prime p ≡ 1 (mod 4) iff some shell a with p/4 < a < p/2 is occupied.

This halves the shell range. It is also the range of the "first-half shells" in which items 6, 7 and 22 work. The first pass read it as the reduction step of item 22: "a unique smallest denominator in (p/4, p/2)" (43a §2.22).

**Proof.**
1. Suppose x > p/2. Then x ≥ (p+1)/2, and x ≤ 3p/4 < p.
2. Since 1/y + 1/z = 4/p − 1/x > 2/p, we get y < p.
3. From 4xyz = p(xy + yz + zx), p divides one of x, y, z; hence p | z. Write z = pz′.
4. Then 1/x + 1/y = (4z′−1)/(pz′), so xy(4z′−1) = pz′(x+y). Since p ∤ xy, we get 4z′ − 1 = pk with k ≥ 1.
5. Put N = pk + 1 = 4z′. Then 1/x + 1/y = 4k/N, i.e. (4kx − N)(4ky − N) = N² with both factors positive.
6. But 4kx − N ≥ 2k(p+1) − N = N + 2(k−1), and likewise for y. So k = 1 and x = y = N/2 = (p+1)/2, with z = p(p+1)/4. This needs p ≡ 3 (mod 4).
7. Finally, if x < p/2 and y = x, then 1/x + 1/y > 4/p, which is impossible. ∎

**Check** (`r2_es_checks.py`).
- All 8,773 solutions (x ≤ y ≤ z) at every prime p < 1200 were enumerated by brute force.
- For p ≡ 1 (mod 4), every solution has p/4 < x < p/2 and x < y.
- For p ≡ 3 (mod 4), the solutions with x > p/2 are exactly the 100 exceptional ones, one per prime.
- This is consistent with 43a's census of 1,317 witnesses at p ≡ 1 (mod 12) below 1300.

**Suggested wording.**
- "(a) If x ≤ y ≤ z is a solution, then p/4 < x ≤ 3p/4; more precisely x < p/2 and x < y, unless p ≡ 3 (mod 4) and (x, y, z) = ((p+1)/2, (p+1)/2, p(p+1)/4). For p = 12h+1 this is 3h+1 ≤ x ≤ 6h."
- "(c) … iff some shell a with p/4 < a ≤ 3p/4 is occupied; for p ≡ 1 (mod 4), iff some shell with p/4 < a < p/2 is."
- Add the proof and the label *Generalised here*.

### M4. Lemma 4.2: the sharp constant is the girth

**Location.** §4.2, Lemma 4.2 and its status line (p. 17).

**What is understated.** The constant 4, and the status "the proof uses only the absence of triangles and of multiple links".

**Stronger statement.** Let G be a finite graph without loops (parallel links allowed) of girth g. Let j ≥ 0 be real weights on the links with j_f ≤ Σ_{f′∋v, f′≠f} j_{f′} for every vertex v and every link f ∋ v. This vertex inequality is the only consequence of gauge invariance that the reader's proof uses. Then:
- Σ_f j_f ≥ g·j_e for every link e;
- equality holds for j = ½ on a shortest cycle through e and 0 elsewhere;
- consequently c_j ≥ (3g/2)·j_e, and c_j ≥ 3g/4 on the nonconstant physical space, both sharp.

The case g = 4 is the reader's lemma, and g = 3 is its triangle remark. The reader's own checks on the 5-cycle and the Petersen graph found minimum ratio 5 (`generality_checks` G3); that is the case g = 5.

**Proof.**
1. *Matching at each vertex.* At a vertex v put J_v = Σ_{f∋v} j_f. The hypothesis j_f ≤ J_v − j_f is exactly the feasibility condition for a transport plan between the links at v, with supply and demand j_f and a forbidden diagonal. Symmetrising the plan gives a symmetric M^v ≥ 0 with zero diagonal and row sums j_f.
2. *A circulation.* Give each dart (oriented link) the weight j_f/2. Let an incoming dart on f at v pass to an outgoing dart on f′ ≠ f with weight M^v_{ff′}/2. This is a circulation on darts in which no transition returns along the same link.
3. *Flow decomposition.* The circulation is Σ_C w_C[C] over closed walks C whose cyclically consecutive links are distinct. Moreover Σ_C w_C|C| = Σ_f j_f and Σ_C w_C n_e(C) = j_e, where n_e(C) counts the traversals of e by C.
4. *Length of one walk.* Cut C at its traversals of e. Each piece is one of two kinds:
   - a walk from one end of e back to the same end: a closed walk with distinct consecutive links, so it contains a cycle and has length ≥ g;
   - a walk between the two ends of e that does not use e: it contains a path, which together with e is a cycle, so it has length ≥ g − 1.

   Hence |C| ≥ g·n_e(C), and so Σ_f j_f ≥ g·j_e.
5. *Casimir consequences.* Use j(j+1) ≥ (3/2)j for j ≥ ½, and every nonzero spin is at least ½. ∎

**Check.**
- `r7_girth.py`: exhaustive over half-integer spins with the SU(2) vertex-singlet condition. The minimum of Σ_f j_f/j_e equals the girth on:
  - K₃ and K₄;
  - C₄, Q₃ (reproducing the reader's 1,012 assignments), K₃,₃, the 3×3 grid and a 3×3×2 box piece (65,535 assignments);
  - C₅, the Petersen graph and a girth-5 theta graph with spins up to 3/2;
  - C₆, the Heawood graph and C₇.
- `r11_girth_lp.py`: linear programming over real weights with only the vertex inequalities. The optimum equals the girth for every link on ten graphs of girth 3–8: K₃, K₄, Q₃, K₃,₃, Petersen, Heawood, McGee, Tutte–Coxeter, the dodecahedron and the box {−1,0,1}³.

**Suggested wording.**
- Statement: "Let the links form a graph without loops of girth g (the cubic box has g = 4) … then Σ_f j_f ≥ g·j_e for every link e. Hence c_j ≥ (3g/2)j_e and c_j ≥ 3g/4 on the nonconstant physical space (for the box: 6j_e and 3)."
- Status: "*Generalised here*: the constant is the girth, sharp on every graph (a shortest cycle in spin ½); only the vertex inequalities are used, for real weights."
- Replace the proof by the circulation proof, or keep the triangle-free proof and add the general statement.

### M5. The two-shell survivors: the "≡ 1 (mod 24)" observation is a theorem, and the residual-7 criterion simplifies

**Location.** §1.2, the sentence after Proposition 1.3 (p. 6).

**What is understated.** "all of them are ≡ 1 (mod 24), the first being 1129". This is presented as a first-pass computation.

**Stronger statement.**
- (i) If p ≡ 13 (mod 24), then a = (p+3)/4 is even. By Proposition 1.2 (2 ≡ 2 mod 3) the residual-3 shell is occupied.
- (ii) If p ≡ 1 (mod 24), then a = (p+7)/4 = 6k+2 is even, and the factor 2 ≡ 2 (mod 7) gives n₂₄ ≥ 1. Proposition 1.3 then reduces to: the residual-7 shell is occupied iff (p+7)/4 has a prime factor ≡ 3, 5 or 6 (mod 7), that is, a non-residue mod 7.
- Hence both first shells are unoccupied exactly when all three of the following hold:
  - p ≡ 1 (mod 24);
  - every prime factor of (p+3)/4 is ≡ 1 (mod 3);
  - every prime factor of (p+7)/4 is ≡ 1, 2 or 4 (mod 7).
- In particular every survivor is a square mod 7, since (p+7)/4 ≡ 2p is then a square and 2 is a square. So every survivor is ≡ 1, 25 or 121 (mod 168).

**Proof.** One line each, from Propositions 1.2 and 1.3.

**Check** (`r2_es_checks.py`, `r10_es_more.py`).
- The 989 survivors below 10⁶ are recomputed.
- All 9,832 primes p ≡ 13 (mod 24) below 10⁶ have the residual-3 shell occupied.
- For every prime p ≡ 1 (mod 24) below 10⁶, the simplified criterion agrees with Proposition 1.3.
- The survivors occupy exactly the classes 1, 25 and 121 (mod 168).

**Suggested wording.** "… exactly 989 have both shells unoccupied (first pass). Every survivor is ≡ 1 (mod 24) and a square mod 7. For p ≡ 13 (mod 24), (p+3)/4 is even. For p ≡ 1 (mod 24), (p+7)/4 is even, and Proposition 1.3 says that the residual-7 shell is occupied iff (p+7)/4 has a prime factor that is a non-residue mod 7."

### M6. The mod-840 reduction is proved; five identities suffice

**Location.** §1.3 (p. 6).

**What is understated.** "is classical (Mordell) and is not proved in the texts read", followed by "The first pass checked…".

**Stronger status: proved here.** Let p ≡ 1 (mod 24). Choose (A, B, R) as follows:

| Congruence on p | (A, B, R) |
|---|---|
| p ≡ 3 (mod 7) | (1, 2, 7) |
| p ≡ 5 (mod 7) | (2, 1, 7) |
| p ≡ 6 (mod 7) | (1, 1, 7) |
| p ≡ 2 (mod 5) | (1, 2, 15) |
| p ≡ 3 (mod 5) | (2, 1, 15) |

Then

  4/p = 1/(ABD) + 1/(ACD) + 1/(pBCD), with D = (p+R)/(4AB) and C = (A+pB)/R.

- *Identity.* This holds identically in p: 1/(ABD) + (A+pB)/(pABCD) = (p+R)/(pABD) = 4/p.
- *Integrality.* The denominators are integers exactly under the stated congruences: 4AB | p+R because p ≡ 1 (mod 8), and R | A+pB is the congruence on p mod 7 or mod 15.
- *What is left.* The remaining classes are p ≡ 1 (mod 24) with p ≡ ±1 (mod 5) and p ≡ 1, 2, 4 (mod 7): the six unit squares mod 840.

The first pass's covering (`check_extras.py`, "[840]") was already a proof. Its two family shapes are polynomial identities, and its conditions are congruences modulo divisors of 840. Only its sanity test was run on sample primes.

**Check.**
- `r3_mod840.py`: sympy simplifies both identities to 0; the 18 classes are covered; the uncovered classes are exactly the six unit squares.
- `r10_es_more.py`: the five identities hold at all 13,988 covered primes p ≡ 1 (mod 24) below 2·10⁶, and every other such prime lies in a square class.

**Suggested wording.** "… which are exactly the unit squares modulo 840. The reduction to them is classical (Mordell) and is not proved in the workbench's texts. It follows from the five identities (display), which cover p ≡ 3, 5, 6 (mod 7) and p ≡ 2, 3 (mod 5). Status: proved here; the first pass's covering of the 18 classes is the same computation."

### M7. Theorem 3.1's upper bound: only the top block needs to be admissible, so g₄(n+3q) ≤ 19^q·g₄(n)

**Location.** §3.1, Theorem 3.1 and its proof (p. 13). Theorem 3.8(b) (p. 15).

**What is understated.** "g₄(n) ≤ 8·19^{⌈n/3⌉−1}" and "for general n take m = ⌈n/3⌉ and delete elements".

**Stronger statement.**
- (i) *Lifting lemma.* Let B be any 4-admissible set and q ≥ 0. Let A_q = {19^j·w : j < q, w ∈ W_j}, where each W_j is {1,7,8} or {2,3,5}. Then A_q ∪ 19^q·B is 4-admissible. Hence g₄(n+3q) ≤ 19^q·g₄(n).
- (ii) *Digit sets.* {2,3,5} = 3·{1,7,8} mod 19 is the only other 3-element set B with S(B) < 19 and H(B) free of 4-term progressions mod 19. Its maximum is 5.
- (iii) *Explicit bounds.* With g₄(1),…,g₄(6) = 1, 3, 5, 14, 40, 79 and g₄(7) ≤ 246:

  | n | Bound | Asymptotic constant (× 19^{n/3}) | Stated bound's constant | Ratio |
  |---|---|---|---|---|
  | 3q, q ≥ 2 | g₄(3q) ≤ 79·19^{q−2} | 0.219 | 0.421 | 1.92 |
  | 3q+1, q ≥ 2 | g₄(3q+1) ≤ 246·19^{q−2} | 0.256 | 3.00 | 11.74 |
  | 3q+2, q ≥ 1 | g₄(3q+2) ≤ 40·19^{q−1} | 0.296 | 1.12 | 3.80 |

- (iv) *Without the computed values.* Deleting the largest elements, with top level {1} ⊂ {1,7,8}, {2,3} ⊂ {2,3,5} or {2,3,5} itself, already gives g₄(n) ≤ c·19^{⌈n/3⌉−1} with c = 1, 3, 5 for n ≡ 1, 2, 0 (mod 3).
- (v) *General k.* The same argument gives g_k(m|B| + n) ≤ q^m·g_k(n) for any certificate (q, B) of Theorem 3.7. For example g₆(10m + n) ≤ 1651^m·g₆(n), which sharpens Theorem 3.8(b) for n ≢ 0 (mod 10).

**Proof of (i).**
1. H(A_q ∪ 19^q·B) = H(A_q) + 19^q·H(B). Here H(A_q) is the set of integers below 19^q whose base-19 digits lie in D_j = H(W_j); there are no carries because S(W_j) < 19.
2. Let x_i = y_i + 19^q·z_i (i = 0, …, 3) be a progression with step d ≠ 0.
3. *If 19^q | d.* Then y_i ≡ y₀ (mod 19^q) with 0 ≤ y_i < 19^q, so y_i = y₀. Then (z_i) is a progression with nonzero step in H(B), which is impossible.
4. *Otherwise.* d = 19^r·e with r < q and 19 ∤ e. The digits below position r agree, and the r-th digits δ_i ∈ D_r satisfy δ_i ≡ δ₀ + ie (mod 19). That is a nonconstant progression in D_r mod 19, which is impossible.

So the top level needs only integer admissibility, not a modular certificate. The argument is the reader's own proof with this one observation added. ∎

**Check.**
- `r6_ep817.py`:
  - the listed optimal sets and the n = 7 witness are admissible;
  - A_q ∪ 19^q·B is admissible for all of them (q = 1, 2; up to 13 elements);
  - an exhaustive search of 3-element digit sets for q = 19 finds exactly (1,7,8) and (2,3,5);
  - it tabulates the improved and stated bounds for n ≤ 21.
- `r13_lift_random.py`: 140 random admissible top blocks with randomly mixed lower digit sets give admissible unions. As a negative control, a non-admissible top block gives a 4-term progression.

**Suggested wording.** Add to Theorem 3.1: "Moreover g₄(n+3q) ≤ 19^q·g₄(n) for all n ≥ 1 and q ≥ 0, since the top level of the base-19 construction may be any 4-admissible set. With Proposition 3.10, g₄(n) ≤ (79/361)·19^{n/3} for n ≡ 0 (mod 3), n ≥ 6." Keep the rate statement, and label the addition *Generalised here*.

---

## MINOR findings

**m1. Theorem 1.1(b) (p. 4): the count holds for every a > p/4 with p ∤ a.**
- *Text:* "For each integer a with p/4 < a < p".
- *Why:* the proof uses a < p only to get gcd(a, p) = 1. That gives gcd(a, R) = gcd(p, R) = 1 and the layers d = p^i·v. For a > p, R ≥ 3p + 4 > 1, so there is no pair with y = z.
- *Check:* 4,303 pairs (p, a) with p < 120 prime, p/4 < a ≤ 3p and p ∤ a (`r2`).
- *Wording:* "For each integer a > p/4 not divisible by p (in particular each a with p/4 < a < p)".

**m2. Propositions 1.2–1.3 (p. 5) hold for every prime p ≡ 1 (mod 4).**
- The shells with R_a = 3 and R_a = 7 exist exactly for p ≡ 1 (mod 4).
- Proposition 1.3's proof never uses p ≡ 1 (mod 3); and 7 ∤ a because p ≠ 7.
- For p ≡ 5 (mod 12), a = (p+3)/4 ≡ 2 (mod 3), so u = 1 lies in M_a and the residual-3 shell is always occupied.
- *Check:* all 1,611 primes p ≡ 1 (mod 4) below 3·10⁴ (`r2`).
- *Value:* small, since those extra primes are already known to be solvable.

**m3. Erdős–Straus statuses.**
- (a) Item 26 (p. 6), "audited in part: the least example and the deduction from it". 43a lists the prime-square trace theorem at depth D, "correct as read", with the identity 16(4q³+1) − (4q+1)(16q²−4q+1) = 15 checked; it also read terminality. The status can name both.
- (b) §6 (p. 26), "primality was checked by the BPSW test only", for 7510085481569082811681. A Pocklington chain proves primality:

  | Number | Its predecessor factored |
  |---|---|
  | p = 7510085481569082811681 | p − 1 = 2⁵·3·5·15646011419935589191 |
  | 15646011419935589191 | minus 1 = 2·3·5·351707·1482864185239 |
  | 1482864185239 | minus 1 = 2·3·17²·5051·169307 |

  Witnesses a < 500 exist at every level, and the leaves are checked by trial division (`r12`). This item can leave "not checked".

**m4. Theorem 2.8 (p. 10).**
- The proof also gives m ≥ 1636 odd steps and A ≥ 2593 halvings; at present these appear only in Corollary 2.9's status line.
- The hypothesis is trivially extendable. Every odd n < 2³³ falls below itself (`r5_descent.c`, 2 minutes, largest excursion 6.05·10¹⁸ < 2⁶³). So the least element s of a nontrivial cycle is ≥ 2³³+1 > 7.216·10⁹, where the least denominator is that of 301994/190537.
- The same argument then gives m ≥ 190,537 odd steps, A ≥ 301,994 halvings and k ≥ 79,080 steps with exponent 1, against 678. This is proved here with no external computation. Optional.

**m5. Proposition 2.5 (p. 9): the exact criterion.**
- *Text:* "If F_m(3) < 3, then every odd n ≥ 3 whose word begins…".
- *Sharp form:* let n₀ be the least member ≥ 3 of the word's cylinder (a residue class mod 2^{A+1}). Then T^m(n) < n for every member n ≥ 3 iff F_m(n₀) < n₀.
- *Proof:* F_m(x) − x = (C − Dx)/2^{A_m} with C ≥ 1. If F_m(n₀) < n₀ then D > 0 and C < D·n₀ ≤ D·n. For the converse take n = n₀. The condition F_m(3) < 3 implies F_m(n₀) < n₀.
- *Check (`r9`):*
  - Of the 8,191 words with A ≤ 13, 4,444 satisfy F_m(3) < 3 and 6,145 satisfy the sharp condition.
  - On 327,640 tested starts, the sharp condition coincides with actual descent at step m for every word.
  - Example: the word (1,1,1,1,4) has F(3) = 235/64 > 3, but n₀ = 95 and every member descends.

**m6. Theorem 2.2 and Proposition 2.1 (p. 8).**
- In (c), "Δ → 1" is also uniform in b, because the lower bound in (a) does not involve b.
- The Hoeffding squeeze in the proof gives polynomial rates: Δ = O(N^{−cδ²}) and 1 − Δ = O(N^{−cδ²}) for an absolute c > 0.
  - At H = ⌊L⌋: binom(H, m)/N ≤ 2^{−(1−h(m/H))H} and Q_m(H) ≤ e^{−2H(½ − m/H)²}.
  - At H = ⌈(1+δ)L⌉: N·2^{−H−1} ≤ N^{−δ}/2.
- Proposition 2.1: the count is ⌊N/2^A⌋ or ⌈N/2^A⌉, so |P(w) − 2^{−A}| ≤ (1 − 2^{−A})/N < 1/N.

**m7. Theorem 2.10 (p. 11): "never", not "not in general".**
- *Text:* "the jet of order K−2 does not in general".
- *What the proof shows:* for every (m, A) with K ≥ 2, every nontrivial zero and every λ in the interior of the simplex, λ + εh (with h_w = 1/∏_{v≠w}(r_w − r_v) ≠ 0) is a segment of probability vectors with the same (K−2)-jet.
- *Wording:* "the jet of order K−2 never determines λ: its fibres through interior points contain segments".

**m8. Audited results that the reader leaves out (optional additions).**
- (a) The Chapter 2 tail bounds (7.9)–(7.16), built on Proposition 2.6 and audited in 44a §2.4: S_h ≤ √2(√15/4)^{h−1} ≤ (3/2)(31/32)^h, and t_H ≤ (31/20)(31/32)^H. They are the natural consequence of the one-step contraction.
- (b) The Tao-clock rate ‖λ_{x,j} − λ_x^∞‖ ≤ L_c(log t_j)^{−c} for x ≤ t_j, with L_c = B′/(1 − α^{−c}) (44, Theorem 44.11). The reader says only "converge in ℓ¹".
- (c) Theorem 4.1's Poincaré form, q_{H−E₀}(ψf) ≥ κd₅(ξ)·Var_{ψ²}(f) on the whole physical form domain, and ‖p_X‖² = 1/Δ_L (F37, F42; 46 §1.2).
- (d) d₅ decreases, with d₅(α₅) = 1.5453 > 3/2 (46 §1.2). So Δ_L > 1.545κ on the whole range g² ≥ 3.6836, whereas the reader gives the value only at g² = 4. The endpoint ξ = 0 may also be included: d₅(0) = 3 = Δ_L/κ there.
- (e) YM-02's energy statement also gives a change below 1/25000 at g² ≥ 16.

**m9. §3 (pp. 12, 14): Λ₃ = 3.**
- With the stated Erdős–Sárközy bound g₃(n) ≫ 3^n/n^{O(1)}, and g₃(n) ≤ 3^{n−1} (powers of 3, i.e. the certificate (3, {1}) of Theorem 3.7), lim g₃(n)^{1/n} = 3.
- Hence Λ₃ = 3 > Λ₄ = 19^{1/3} > 97^{1/6} ≥ Λ₅: the monotone sequence Λ_k strictly decreases at its first two steps.
- *Check:* powers of 3 are 3-admissible for n ≤ 8 (`r6`).

**m10. Theorem 3.1's lower bound (p. 13).**
- Theorem 3.6 gives |T(A)| ≥ M_n = 19^{⌊n/3⌋}·3^{n mod 3} ≥ 19^{n/3}. So (M_n − 1)/(2n) ≤ g₄(n), and the same substitution works in Corollary 3.5.
- The gain is a factor (3/19^{1/3})^{n mod 3} ≤ 1.26. It is negligible beside Theorem 3.6 for large n, but it is what the proof gives.

**m11. Proposition 4.5 and the sentence after it (p. 19).**
- (a) *Physical space.* On the physical space the same route gives |ξ| < 3/(4M_L), i.e. 1/320 at L = 2:
  - by Lemma 4.2 the spectrum of H₀ restricted to the physical space lies in {0} ∪ [3, ∞), so on the circle |z| = 3/2 the resolvent has norm 2/3;
  - ‖W_L‖ is still 2M_L, since W_L is gauge invariant and maximal at U ≡ I.

  The radius still shrinks like L^{−3} and is still far inside α₅.
- (b) *No contour does better.* Any contour separating 0 from [3/4, ∞) crosses (0, 3/4) at some x with max(1/x, 1/(3/4 − x)) ≥ 8/3. So the product criterion fails beyond 3/(16M_L) for every contour, not only for |z| = 3/8.

---

## Overclaims noticed

- **O1 (p. 19).** "at L = 2 the global route certifies only |ξ| < 1/1280" compares a full-space radius with a physical-space theorem. The like-for-like physical-space radius is 1/320 (m11). The conclusion, that local norms are needed, stands; the contrast is overstated by a factor 4.
- **O2 (p. 19).** YM-05 is described as "conditional as Theorem 4.1, since it is implied by it". This attributes to YM-05 a dependence on order 5 that it does not have (M1). It is an inaccuracy in the direction of caution.

No other overclaim was found. Every number I recomputed agreed with the reader, including:
- α₅, the threshold, d₅(1/64), and the sensitivity 3.737 / 1.8946;
- m* = 1636 and k ≥ 679;
- the Corollary 2.9 fraction and the upper end 2^71.88;
- the 989 survivors;
- the 1,012 cube assignments;
- the mod-840 unit squares;
- the family identities of §1.3;
- the three constants of Theorem 3.6;
- Korsky's comparison rates;
- 93^{1/6} and 1651^{1/10}.

## Verdicts on the existing "Generalised here" items and Corollary 2.9

| Item | Correct? | At its true generality? |
|---|---|---|
| Thm 1.1, every odd prime | Yes (re-verified) | No: (b) holds for every a > p/4 with p ∤ a (m1); (a) and (c) sharpen to x < p/2 for p ≡ 1 (mod 4) (M3). |
| Prop 2.5, under F_m(3) < 3 alone | Yes | No: the exact condition is F_m(n₀) < n₀ (m5). |
| Prop 2.6, √15/4 for x ≥ 2 | Yes | Yes, final: x ≥ 2 is the whole domain on which the left side is real, and the constant is attained at x = 7. |
| Lemma 4.2, triangle-free graphs | Yes | No: the constant is the girth, and only the vertex inequalities are needed (M4). |
| Prop 4.6, the S6-5 cubic mod 9 | Yes | Yes, sharp: the image of P mod 9 on ℤ⁴ and on D₄ is exactly {0,1,2,4,5,7,8}. P(3,1,0,0) = 18 with (3,1,0,0) ∈ D₄, so the exclusion "6k with 3 ∤ k" cannot be extended to multiples of 18. |
| Prop 3.9, distance rulers | Yes | Yes, a natural generality. |
| Cor 2.9 | Yes | No: its hypothesis is stronger than needed (M2). |

## Checks run

All scripts and outputs are in `scratchpad/referee22/`. Each run took under 2 minutes.

**The reader's own scripts, re-run.**
- `generality_checks.py`: output identical to the recorded one.
- `workbench_reader_claims_checks.py`: 47/47 pass.

**My scripts.**

| Script | What it checks | Result |
|---|---|---|
| `r1_ym_orderN.py` | α_N, the thresholds and d_N for N = 1…5 from the exact F26 rationals; 𝒟₁ = 1 − 256ξ/3; monotonicity; sensitivity of orders 3–5 | M1 |
| `r8_ym_extra.py` | order 2 with the first pass's exact values; d_N at several couplings; the Neumann radii on the full and the physical space | M1, m11 |
| `r2_es_checks.py` | brute-force solution sets for p < 1200 (M3); Thm 1.1(b) for a ≤ 3p (m1); the 989 survivors and the simplified residual-7 criterion (M5); Props 1.2–1.3 for p ≡ 1 (mod 4) (m2) | all pass |
| `r3_mod840.py` | symbolic identities; covering of the 18 classes; one family per class | M6 |
| `r10_es_more.py` | survivors mod 7 and mod 168; the five identities on all primes p ≡ 1 (mod 24) below 2·10⁶ | M5, M6 |
| `r4_eliahou.py` | staircase of best upper approximations of log₂3 with exact s-ranges; bounds at 330,751, 2³², 2⁴⁰, 2⁶⁰, 20·2⁵⁸, 2⁶⁸, 2⁷¹ | M2 |
| `r5_descent.c` | every odd n < 2³³ falls below itself (output `r5_descent_OUTPUT_2e33.txt`) | m4 |
| `r9_descent_sharp.py` | the sharp descent criterion on all 8,191 words with A ≤ 13 | m5 |
| `r7_girth.py` | exhaustive half-integer spin search on 13 graphs of girth 3–7 | M4 |
| `r11_girth_lp.py` | linear programming with real weights on 10 graphs of girth 3–8 | M4 |
| `r6_ep817.py` | the lifting lemma on optimal sets; all 3-element digit sets mod 19; the improved-bound table; Λ₃ | M7, m9 |
| `r13_lift_random.py` | 140 random admissible top blocks, plus a negative control | M7 |
| `r12_pocklington.py`, `r12b_pocklington_chain.py` | primality proof of 7510085481569082811681 | m3 |
| `r14_s65_mod9.py` | the image of P mod 9 on ℤ⁴ and on D₄; 18 ∈ P(D₄) | S6-5 verdict |
