# Intersections of the workbenches: the typed morphisms, the shared identities, and three patterns that recur

Claude (claude-ab lane), model `claude-opus-5-5` (Opus 5.5) at maximum reasoning effort. 26 September 2026, 05:42 UTC; revised 06:39 UTC after the twentieth referee pass (§7).

Fifth note of board task 10, part 2. The owner asked for the readers of the other workbenches to be "not too siloed", with their intersections, "without necessarily needing to make them all duplicates". This note collects the intersections found in the inventory and the four audits, states each as a typed morphism (domain, codomain, what crosses, what does not), and gives its audit status. It draws on the inventory (`47a` §8, edges OV-01 to OV-28), the four first-pass reports (`43a`–`46a`, their overlap sections), the notes `21_`, `28_`, `34_`, `43_`–`46_`, and the zeta reader (DOI 10.5281/zenodo.22970703, "the zeta reader").

**Types** (as in `47a` §8): **P** a proved typed map or lemma used on both sides; **I** the same identity or object on both sides; **D** one side imports the other's theorem as an unproved dependency; **R** regression-test use only; **A** analogy or proposal; **M** methodology or provenance only.

**Status**: audited / audited in part / located, as in `43_`.

## 0. The graph at a glance

Nodes: zeta (the split-zero programme), ES, Collatz (CZ), Erdős 817 (EP), YM, NS, S⁶, and the Jacobian map F.

| # | Edge | What crosses | Type | Status |
|---|---|---|---|---|
| 1 | zeta → CZ | the zeta programme's Hurwitz zero-cluster reconstruction (`historical_hurwitz_jets.tex`, H10–H13), re-proved in the Collatz split-zero note; its jets are those of the zeta reader's Theorem "the first Hurwitz jet", (a) | P | audited (§1.1; `44_` Thm 44.12) |
| 1a | zeta → CZ | the Split-Zero support modules and killed-representative quotient (zeta `formal/splitzero/DERIVED_MATHEMATICS.md` §§1–4), instantiated on the Collatz operator in Ch. 7 and used in Chs. 8, 9, 15 | P/D (imported construction) | located |
| 2 | NS → ES | the torus endomorphism J = [[3,1],[1,5]] of the NS manuscript | P (operator only) | audited (`21_` §1) |
| 3 | S⁶ → ES | the integral monodromies A₁, A₂, A_∞ of the (3,4,∞) period system | P | audited: relations; orbits and genera at odd levels D (`43_` §3) |
| 4 | S⁶ → YM | the imaginary period block B of Π(z), only through D = det B | P | audited (`28_` Lemma 28.2) |
| 5 | F → NS kinematics → YM | U = DF⁻¹(V∘F), the escaping curve, the material tensor, Theorem 14.2 | P | audited (`28_`, `34_`); conditional on fixed-box limits |
| 6 | F → zeta | inverse-fibre chart, incompressible fibre heat, material generator, endpoint jets | P within zeta; A relative to YM | located |
| 7 | ES ↔ zeta | the four-dimensional Keller map P (det DP = −2) and its conductor; the shared file is byte-identical | P | det DP audited (`21_`); rest located |
| 8 | zeta → YM | the Gram sandwich from a relative column error (δ ≤ 1) | P (one lemma, two instances) | audited (`21_` §3) |
| 9 | zeta → YM | inverse-power conductor observability (T7) | P (pattern) | arithmetic audited (46a) |
| 10 | zeta → YM | the composed minimum-lift identity (AMT7–10) and the corrected residual maps (OK1–2) | P (standard Schur-complement algebra) | checked numerically on random rational matrices (46a) |
| 11 | NS → YM | velocity → reducible SU(2) connection; −2Σtr F_ij² = λ²|curl u|² | P for the map; D on imported NS rate bounds | audited, conditional (`21_` §2) |
| 12 | NS → zeta | the released NS field as arithmetic input (Mellin, residue at s = −1) | D on NS-00 + P | located |
| 13 | S⁶ and F → NS (inside zeta) | fluid coordinates, S⁶ gauge-scalar equations → NS on 𝕋³ | P (displayed calculations) | located |
| 14 | zeta → ES | NG20–NG21 used as theorem dependencies by ES item 20 and family C | D | located |
| 15 | ES → zeta | the 488-page ES reader v69, vendored as a source dependency | D | located |
| 16 | 817 → zeta | finite word sources mapped into the supported quotient; the "cocycle" identity | P (restatements) | the finite-period receiving map audited (an elementary restatement); the other nine interface notes located (`45_` §7) |
| 17 | ES ↔ CZ | 3(4n + 1) + 1 = 4(3n + 1), i.e. θT = 4θ for T(n) = 4n + 1, θ(n) = 3n + 1 | I | audited (both sides) |
| 18 | CZ ↔ ES ↔ zeta | the support-idempotent homogenisation (x, h) ↦ (ax + bh, h) | I | ES proves the diagram (X4, read); the zeta foundation cites the Clankers' Zenodo record 19900461; the Collatz split-zero note cites a local April 2026 note of the same title and uses its finite branch matrices |
| 19 | CZ → YM | the fixture X_v − X_u = (q − 3)(q + 4)/32 | R | identity verified (44a, 46a) |
| 20 | ES ↔ zeta | the split-zero semiring G(R) = R ⊔ {τ} with its unique Boolean character | I | audited (`21_` §6) |
| 21 | ES ↔ zeta | a finite Weyl phase-space basis | I (per ES) | ES side verified on C₂ × C₃ (43a); zeta side not read |
| 22 | ES ↔ S⁶ | the Niemeier lattice with root system A₅⁴D₄ and glue index 72 | I (named object) | ES's code verified (R10); the two glue codes not compared |
| 23 | ES ↔ YM | the word "gap" (ES X7, a diagonal model) | A | — |
| 24 | ES → YM | a top-socle line proposed as a success projector | A ("candidate-not-imported") | — |
| 25 | 817 → YM, ES/817/YM | a content-addressed validator; the PolyClank design documents | M | — |
| 26 | NS ↔ zeta | the Mellin abscissa of the NS terminal singularity | A | a reading by claude-ab (`21_` Prop. 21.7) |
| 26a | YM ↔ zeta | YM's own summary of the zeta routes (YM `ATTEMPTS.md`, `research-attempts.json`) | A (a summary; it contains the transcription error D1 of §4) | located |
| 27 | zeta ↔ ES | a CUE/Hurwitz routing proposal | A | — |
| 28 | zeta → ES | the 13–16 September SplitZero packages (support diagram, mixed-kernel control, AMT1–10) | P/D | located |

Not found: any mathematical edge between 817 and ES, NS or S⁶ (817's mentions of ES and YM are methodological); any NS-workbench-certified transfer; an S⁶ edge in the NS vacuum-hydrodynamics continuation (it says "No S6 edge").

One zeta file, AMT1–10 (`13_ARITHMETIC_MIXED_TRANSFER.tex`), is used by two workbenches: YM (edge 10) and ES (edge 28). `FABLE_TO_ORIGINAL_CONDUCTOR.tex` is used twice by ES: as its upstream (edge 7) and as a source of its RH families (edge 14).

## 1. The substantive intersections

### 1.1 zeta → Collatz: the Hurwitz jets encode moments (edge 1; new)

This edge was not in the zeta reader's overlaps table, which recorded the Collatz workbench as not cloned. The Collatz split-zero note cites the zeta programme's reconstruction (`historical_hurwitz_jets.tex`, equations H10–H13, at commit 16fc4dbb817b of the zeta repository) and re-proves the part it uses; the same reconstruction is applied again in the Collatz Ch. 1 §5, and Ch. 2 §10 uses Hurwitz values at nonpositive integers.

*The typed morphism.* Fix (m, A), the K odd-return words w with residues r_w (distinct modulo 2^{A+1}), and a nontrivial zero ρ of ζ. The map

  λ ∈ Δ^{K−1} (probability vectors on the words) ↦ the order-J t-jet of the zero cluster of Z_λ(s, t) = Σ_wλ_wζ(s, 1 + tr_w) near ρ

factors as λ ↦ (M₁, …, M_J), M_i = Σ_wλ_wr_w^i (a moment map depending only on the residues), followed by a triangular polynomial bijection (M₁, …, M_J) ↔ (c₁, …, c_J) whose coefficients are the Hurwitz jets b_j(ρ) = (−1)^j(ρ)_jζ(ρ + j)/j! and the derivatives of ζ at ρ. The first factor is injective for J = K − 1 (Vandermonde) and not for J = K − 2 (`44_` Theorem 44.12).

*What crosses.* From zeta: the reconstruction theorem H10–H13, whose ingredients are the jet formula ∂_t^jζ(s, 1 + t)|_{t=0} = (−1)^j(s)_jζ(s + j) (also the zeta reader's Theorem "the first Hurwitz jet", (a)) and the non-vanishing of ζ on Re s ≥ 1. From Collatz: only the residues r_w. *What does not cross.* Nothing about the location of ρ (any nontrivial zero works) and nothing about Collatz orbits (the family is built from the weights). The encoding is faithful and informationless in both directions.

*Relation to the owner's programme.* The zeta reader studies the Hurwitz flow t ↦ ζ(s, 1 + t) at t = 0 through its jets (the first jet vanishes in −1 < Re s < 0 exactly on the shifted set of zeros; the flow does not translate the zero set). Here the motion of a single zero, taken at the shifts t·r_w of several nodes at once and averaged with weights, is used as a storage device. The Collatz workbench (this note and its Ch. 1 §5) is the only workbench other than zeta found to use the ζ(s, 1 + t) flow itself.

### 1.2 NS → ES: an operator, not a fluid theorem (edge 2)

The NS manuscript's auxiliary torus endomorphism J = [[3,1],[1,5]] (det 14, eigenvalues 4 ± √2) enters 21 ES statements as an operator only. The content is the group identity {(u, v) ∈ G² : u³v = 1 = uv⁵} = {(u, u⁻³) : u¹⁴ = 1} (exact aliasing on finite character groups) and the sharp constant inf_{k≠0}|v·k|‖k‖ = 1/√(4 + 2√2) for the (unnormalised) eigen-directions v_r = (1, 1 − √2) and v_t = (√2 − 1, 1): the inequality is strict for every k ≠ 0, and the infimum is approached, not attained, along Pell vectors. No NS existence or blowup theorem is used (`21_` §1; register S40).

### 1.3 S⁶ → ES and S⁶ → YM: two different uses of the same period data (edges 3, 4)

- ES uses the integral monodromies A₁, A₂, A_∞ (A₁³ = A₂⁴ = A₁A₂A_∞ = I) to build affine-torsion covers of its divisor atlas: for odd D (the source's hypothesis; the statements fail for even D), transitive on (ℤ/D)³ when 3 ∤ D, two orbits when 3 | D, genera (5D³ − 12D² − 17D + 24)/24 etc. (`43_` §3). The equivalence "ES fails at p ⟺ no section" is ES-02 re-encoded.
- YM uses the imaginary period block B of Π(z) = [[6μ, τ, 1, 0], [β, μ, 0, 1]] as a magnetic background, and only D = det B enters on the non-wrapping patch (`28_` Lemma 28.2).
- Neither side uses the global S⁶ claim; both use displayed matrices. The S⁶ construction is not the July Jacobian counterexample (YM `ATTRIBUTION.md`).

### 1.4 The Jacobian map: one map, three constructions (edges 5–7)

"Fable" names three different objects in the repositories, and a reader should disambiguate each time (`47a` §10 D5): the three-dimensional Keller map F of the Jacobian-conjecture counterexample; the S⁶ construction ("with Fable" in older S⁶ files); and the four-dimensional Keller map P of the ES crosswalk ("ES–Fable" cover and conductor).
- F → YM (edge 5): Keller maps give incompressible polynomial flows, the curve γ escapes at τ = 1/8 (the zeta reader's Lemma; `28_` Lemma 28.1), and the material tensor feeds Theorem 14.2, which reproduces the free two-gluon threshold (`34_`).
- F → zeta (edge 6): an inverse-fibre chart and fibre heat, written within zeta; the zeta side says it "did not itself produce" an NS singularity or an off-critical zero; located.
- P ↔ ES ↔ zeta (edge 7): det DP = −2 (`21_` C4); the eight-point fibres, monodromy and conductor intertwining are located.

### 1.5 zeta → YM: one Hilbert-space lemma and two linear-algebra patterns (edges 8–10)

The transfers say explicitly that no map between arithmetic zeta objects and gauge fields is asserted. What crosses:
- the Gram sandwich (1 − δ)²Φ*Φ ⪯ Φ_J*Φ_J ⪯ (1 + δ)²Φ*Φ when ‖(Φ_J − Φ)x‖ ≤ δ‖Φx‖, δ ≤ 1 (the triangle inequality; the lower bound fails for δ > 1): the zeta instance takes δ from a dilation factor, the YM instance from e^{−Ta₀} (`21_` Lemma 21.5);
- the left-inverse observability pattern W = (G⁽¹⁾)⁻¹R* at L = 2, g² ≥ 20, with observation fraction > 150/221;
- the composed minimum-lift identity S_{Λ₂Λ₁,Q} = S_{Λ₁,Q}S_{Λ₂,Q₁} and a Pythagorean identity for the Q-minimum section.
None of these carries an arithmetic constant into a YM bound, and none enters YM-01.

### 1.6 NS → YM (edge 11)

A divergence-free velocity u becomes the reducible connection A_i = λu_iT with −2Σ_{i<j}tr F_ij² = λ²|curl u|². The zero-quotient bound 32/t + … holds for every admissible weight; the NS profile is one such weight, adding only the divergence of the curvature mass. The diagonal sequence exists only with coupling → 0; at fixed coupling nothing follows (`21_` §2, scope limit 21.4). The divergence itself depends on the imported NS rate bounds.

### 1.7 817 → zeta (edge 16)

The ten SplitZero interface notes restate 817's finite constructions as typed linear algebra: free ℚ-spaces on coefficient words, the evaluation quotient q_u, the cut map π_{u,v}: e_{(x,y)} ↦ e_{x+Q(u)y}, the exact sequence of kernels with dim ker π = F(u)F(v) − F(uv), and κ(u, v)κ(uv, w) = κ(v, w)κ(u, vw), where κ(u, v) = F(u)F(v)/F(uv), so both sides equal F(u)F(v)F(w)/F(uvw). Correct and elementary; no zeta statement is entered and nothing flows back.

### 1.8 Shared identities (edges 17–22)

- **ES ↔ CZ (17).** θ(T(n)) = 3(4n + 1) + 1 = 4(3n + 1) = 4θ(n), so for odd n the odd Collatz step satisfies U(T^jn) = U(n) (ES R05, which credits the underlying residue and affine diagrams to u/CivQ17). The same identity is step 4 of the Collatz merging families (`44_` Theorem 44.4, σ = 0). No recorded dependency either way.
- **CZ ↔ ES ↔ zeta (18).** The homogenisation (x, 1) ↦ (x, h), (x, h) ↦ (ax + bh, h), which makes affine branch maps commute with support inclusions. The zeta v11 foundation cites it from the Clankers' Zenodo record 19900461; ES X4 proves the diagram; the Collatz split-zero note cites a local April 2026 note of the same title and uses its finite branch matrices.
- **CZ → YM (19).** X_u(q) = 1/2 + q/32 and X_v(q) = 1/8 + q/16 + q²/32 (constant terms of two parity words of length 5) satisfy X_v − X_u = (q − 3)(q + 4)/32 and agree at q = 3 (19/32). In Collatz it witnesses that specialisation at q = 3 loses information; YM uses it only as a regression fixture.
- **ES ↔ zeta (20, 21).** G(R) = R ⊔ {τ}: {τ} is a prime ideal, and {τ, 0_R} is prime iff R is a domain (`21_` §6). The finite Weyl operators T_aM_χ form an orthogonal basis of End(ℂ[A]).
- **ES ↔ S⁶ (22).** Both name the Niemeier lattice with root system A₅⁴D₄: |disc R| = 6⁴·4 = 5184, so [N : R] = 72. ES's order-72 glue code H ⊂ (ℤ/6)⁴ × 𝔽₂² (R10) was verified exhaustively (|H| = 72, isotropic, cost spectrum {0: 1, 4: 46, 6: 25}); the S⁶ files that would allow a line-by-line comparison are only on Zenodo, so the identity is at the level of the named object.

## 2. Three patterns that recur across the workbenches

Each pattern is stated as a list of instances, each with the status it has in the note cited. Whether the pattern says something beyond its instances is not claimed.

### 2.1 Exact restatements carry no new constraint

A faithful re-encoding of a problem is an equivalence; it moves the difficulty and does not reduce it unless the new side has a constraint that the old side lacked. Instances:
- **ES-02** (`43_` Thm 43.1): ES at p ⟺ some divisor set E_a ∪ M_a is nonempty. **ES-09** (`43_` §3): ES at p ⟺ a denominator-labelled cover has a section; the section criterion D = 1 is exactly integrality, i.e. ES-02.
- **Collatz Ch. 9** (`44_` Prop. 44.10; re-derived from the overview's statement): Collatz ⟺ B = 0, B ≅ ⊕ℤ/m_C ⊕ ⊕ℤ; **Ch. 3** (audited in 44a §2.5): Collatz ⟺ H₀ = 0.
- **The Hurwitz encoding** (`44_` Thm 44.12): weights ↔ zero jets, injective at order K − 1, informationless.
- **NS-04(a)** (`46_` §5): a velocity snapshot ↔ exact gravitational constraint data with a left inverse on marked data; not a dynamical correspondence.
- **817 → zeta** (§1.7): finite constructions restated in the supported-quotient vocabulary.
- In the zeta programme, the same pattern is the reader's list of RH-equivalent objects (the summation image, the Nyman–Beurling closure; zeta reader §3).
The Collatz, 817 and NS sources say this of their own restatements. The ES-09 package presents its equivalence as a complete failure object; the assessment that it re-encodes ES-02 is the audit's (43a §4).

### 2.2 Method obstructions

A method obstruction shows that a proposed method or certificate family cannot establish a property P, usually by an explicit instance where P holds but the method fails. Instances:
- ES items 2, 3, 6, 14, 21, 26 and the bounded-transport and first-two-shell examples (`43_` §4): every certificate prime is itself solvable.
- Collatz Theorem 44.2(c), of a different form: a limit on what the geometric model can describe (the full word law of N consecutive starts is far from geometric above (½ + δ)log₂N); nothing is claimed about orbits.
- YM §27 (`46_` Prop. 46.5): the global Neumann radius shrinks with the box, while YM-01 proves a box-uniform statement by local norms — the method fails where the property holds.
- 817 negative results 3, 4, 6 (`45_` §6): modular certificates are sufficient but not necessary; the bases 71–96 fail for B*; the fixed-block optimum for A♯ (and 7, read and found plausible in 45a).
- In the zeta programme, the same form is the zeta reader's list N-* of negative results, each stated within the scope of what failed.
The scope of each is the method; none is evidence against the conjecture or problem concerned.

### 2.3 Finite regulators and limits taken in the wrong order

Several results hold in a regime or a limit other than the one the underlying problem asks about:
- YM-01: fixed spacing, strong bare coupling; the continuum needs g → 0.
- Theorem 14.2 and the NS → YM diagonal: coupling → 0 with a growing box; they reproduce free-field values.
- NS-04(d): global regularity of a modified (hyperdissipative) equation.
- Tao-clock (`44_` Thm 44.11): statements about almost all orbits in logarithmic density, along one scale sequence.
In each case the workbench states the regime correctly.

### 2.4 What "certificate verified" means in each workbench

| Workbench | Certificate | What was re-done |
|---|---|---|
| ES item 22 | two polynomial positivity certificates (all translated coefficients positive) | recomputed with independent code (43a) |
| 817 EP-04/05 | modular progression-freeness of H(B) modulo q | recomputed twice (45a; my script) |
| 817 small values | exhaustive searches | three independent programs for n ≤ 6 |
| YM-01 order 5 | 5,726 rational primal/dual certificates from a 662-row producer | producer and auditor re-run, byte-identical; logic read, not re-implemented |
| Collatz Thm 44.9 | all odd n ≤ 330,749 reach 1 (the workbench's database) | recomputed here (0.2 s); the inequalities re-derived and recomputed |
| ES item 4 | 1,381,117,764 rooted profiles (5,922,259 range-compatible) | not re-run (direct test below 40,000 only) |

## 3. Intersections with the zeta reader, and corrections to its overlaps table

The zeta reader's overlaps table (its §8.4) was a selection of the zeta side and recorded some edges as located. After this round:
- Collatz ↔ zeta: the Hurwitz-jet encoding (§1.1) is a new, audited edge, and the Split-Zero support-module import (edge 1a) a new located one; the Collatz workbench has now been cloned (the zeta reader said it was not).
- Collatz ↔ ES ↔ zeta (edge 18): the zeta reader gave the Collatz side as the Clankers' Zenodo record; the Collatz note itself cites a local April 2026 note of the same title.
- S⁶ → ES: the group theory and genus formulas are now audited, for odd levels D (the zeta reader listed the edge as located).
- 817 → zeta: the finite-period receiving map is audited as an elementary restatement; the other nine interface notes remain located.
Nothing in this round changes a statement of the zeta reader's Sections 2–7.

## 4. Discrepancies noticed across the repositories (for the author)

These are record-keeping points, listed neutrally (`47a` §10):
- **D1.** The YM files transcribe the zeta value W(wg₀, wg₀) = 2.0984855607004·10⁻¹¹ as "·10⁻¹⁹" in two places (YM `ATTEMPTS.md` L274; `research-attempts.json` L918).
- **D2.** The S⁶ attribution wording differs across files; `ATTRIBUTION.md` is the designated clarification.
- **D3.** The ES handoff (10 September) says no Collatz repository was identified; the YM research control (14–15 September) tracks the public Collatz workbench.
- **D4.** The zeta satellites 23/26/27 credit Tao, Speyer and Poplett for F but not Alpöge's announcement; the credit is supplied by the zeta README and `ALPOGE_FABLE_ROLE.tex`.
- **D5.** "Fable" names three objects (§1.4).
- **D8/D9.** Duplicate files differing only in line endings; 817 review manifests contain Windows paths under a placeholder user name.

## 5. Not checked

Edges 1a, 6, 12, 13, 14, 15, 26a, 28 beyond location; nine of the ten 817 interface notes (edge 16); the zeta side of edge 21; the S⁶ side of edge 22; the Collatz side of edge 18 (the external Zenodo record); every "A" and "M" edge beyond reading its statement.

## 6. Checks

No new script: every identity above is checked in the script of the note cited (`21_`, `28_`, `34_`, `43_`–`46_`) or in the first-pass scripts under `checks/workbenches/`.

## 7. Revision after the twentieth referee pass

A referee (a Claude instance that did not write this note) checked each edge's type and status against the sources and against `21_`, `28_`, `34_`, `43_`–`46_`. Its findings, each verified before being applied:
- **Major.** (1) The ES–S⁶ covers need odd D (as in `43_`). (2) What crosses on edge 1 is the zeta programme's reconstruction theorem, which the Collatz note cites, not the zeta reader's jet theorem. (3) Edge 16 was labelled audited although only one of ten interface notes was read. (4) "Every intersection" was false: edges 1a (Split-Zero support modules into Collatz) and 26a (YM's summary of the zeta routes) were missing. (5) §2.1 attributed to ES a self-assessment it does not make. (6) The Pell constant is approached, not attained, and the directions are unnormalised. (7) §2 said every instance is proved in the note cited; the statuses are now given. (8) §1.1 called the split-zero note the one place the Collatz workbench uses the Hurwitz flow.
- **Minor, applied.** The Collatz side of edge 18; the file-usage sentence; a phrase shown as a quotation that is not in the zeta reader; the description of the zeta reader's jet and mirror results; the 817 item removed from §2.3; the pattern of §2.2 stated less strictly; the status column made uniform; the enumeration size; the 44.9 row; §3 extended; the R05 credit.
