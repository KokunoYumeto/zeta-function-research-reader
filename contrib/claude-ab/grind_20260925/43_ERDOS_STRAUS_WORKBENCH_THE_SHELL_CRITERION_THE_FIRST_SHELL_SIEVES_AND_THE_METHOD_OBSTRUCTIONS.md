# The Erdős–Straus workbench: the shell criterion, the first-shell sieves, what the certificates prove, and the method obstructions

Claude (claude-ab lane), model `claude-opus-5-5` (Opus 5.5) at maximum reasoning effort. 26 September 2026, 05:31 UTC; revised 06:39 UTC after the twentieth referee pass (§8).

This is the first of five notes for board task 10, part 2 (readers for the other workbenches and their intersections). It covers the Erdős–Straus (ES) workbench `KokunoYumeto/erdos-straus-foundation` at commit `d20b32e1547aee2f08b440d56cceb47ab16dc4b7` (23 September 2026).

**How this note was made.**
1. The inventory `47a_WORKBENCH_SURVEY_INVENTORY_AND_OVERLAPS.md` §1 located the material.
2. A first-pass audit was made by a Claude subagent that did not write this note. Its report is reproduced unchanged as `43a_ERDOS_STRAUS_FIRST_PASS_AUDIT_REPORT.md` ("43a" below), and its scripts and outputs are in `checks/workbenches/audit43_es/`.
3. I re-ran all four of its scripts on 26 September. The outputs are identical except for timing lines (`checks/workbenches/rerun_20260926/es/`).
4. I wrote an independent check of the statements proved below, from the definitions, importing no workbench or audit code (`checks/workbenches/workbench_reader_claims_checks.py`, section ES; all pass).
5. I re-derived the proofs of §1 myself; they are written out here in full because the reader states them with proof.

**Status labels** (used in all five notes and in the reader):
- **audited**: the proof was read in full, every step was checked, and independent checks were run;
- **audited (certificate)**: the finite certificate on which the proof rests was recomputed independently, and the deduction from it was read;
- **audited in part**: the parts named were checked; the rest is located;
- **conditional**: audited, given an input that was not re-derived (named each time);
- **located**: the statement and its proof file were found and described; the proof was not checked.
A statement checked only numerically is called *checked*, not audited.

The workbench describes the results of its 22 September release as written proofs with Python replays, with no Lean build and no independent human review (the earlier 488-page reader ships Lean material of its own), and its README says the project does not claim a proof or counterexample to the conjecture (43a §2, citing `DAILY_RESULTS_20260922` lines 679–686). Nothing below changes that.

**Credit, as the workbench records it.** The collective author name is The Clankers; the owner (KokunoYumeto / u/lepthymo) supplied motivations and directions; the mod-107 observation behind R06 is credited to u/CommonCareful3149, further contributions to u/UmbrellaCorp_HR, and the diagrams behind R05 to u/CivQ17 (README, "Attribution and collaboration"; `results/records.json`).

**Terminology.** A shell a is *occupied* if E_a ∪ M_a ≠ ∅, that is (Theorem 43.1(b)), if some solution has a as a denominator completed by an ordered pair (y, z) counted in that shell.

## 0. Summary

| Result | What it says | Status |
|---|---|---|
| ES-01/02 (§1.1) | For p = 12h+1 prime, every solution of 4/p = 1/x+1/y+1/z has its least denominator in [3h+1, 9h]; for each a there, the ordered pairs (y, z) with 1/a + 1/y + 1/z = 4/p number 2\|E_a\| + \|M_a\| for two explicit divisor sets E_a, M_a of a²; ES at p ⟺ some E_a ∪ M_a ≠ ∅ | audited; classical in substance (Elsholtz–Tao §2) |
| ES-03 (§1.2) | At a = (p+3)/4 the shell is occupied iff a has a prime factor ≡ 2 (mod 3), with the exact count; at a = (p+7)/4 an explicit three-predicate criterion mod 7 | audited |
| Reduction (§1.3) | The workbench proves ES for p ≢ 1 (mod 24); the classical reduction to six classes mod 840 is used but not proved in the texts read | audited (its own part); the mod-840 part is Mordell's |
| Items 6, 7, 14, 21, 22, 26 (§2) | Principal-only bound is negative; least-nonresidue localisation; divisor capacity with sharp bound; complete residual-return rule; an explicit negative degree-8 invariant of every solution; the least example p = 67369 | audited (22: certificate) |
| Item 4 (§2) | Factor supply: ≥ 6 nonresidue primes within 25 factorisations | conditional on a finite enumeration (1,381,117,764 rooted profiles, 5,922,259 of them range-compatible) that was not re-run |
| Items 2, 3, 8, 23 (§2) | Two method counterexamples; the middle identity and its bounds; norm bounds for the receiver matrix | audited (certificate) for the stated certificates |
| The other 17 items | See 43a §2 | located |
| ES-09 (§3) | The (3,4,∞) monodromy covers at odd levels D: orbits and genera; ES(p) ⟺ a section exists | audited; the ES equivalence is a re-encoding of ES-02 |

## 1. The core reduction, with complete proofs

Throughout, p = 12h + 1 is a prime (h ≥ 1). A *solution* is a triple of positive integers with 4/p = 1/x + 1/y + 1/z.

### 1.1 The shell criterion (ES-01, ES-02)

For 3h + 1 ≤ a ≤ 9h put R_a = 4a − p and S_a = pa, and

- E_a = {u : u | a², R_a | 4u + 1},
- M_a = {u : u | a², R_a | u + a}.

**Theorem 43.1.**
- (a) If x ≤ y ≤ z is a solution, then 3h + 1 ≤ x ≤ 9h.
- (b) For each a in [3h+1, 9h], the number of ordered pairs (y, z) of positive integers with 1/a + 1/y + 1/z = 4/p is exactly 2|E_a| + |M_a|. The set M_a has even size, no pair has y = z, and the number of unordered pairs is |E_a| + |M_a|/2.
- (c) Consequently the equation has a solution at p if and only if E_a ∪ M_a ≠ ∅ for some a in [3h+1, 9h].

*Proof.*
(a) The other two terms are positive, so 1/x < 4/p; and x is the least denominator, so 4/p ≤ 3/x. Hence p/4 < x ≤ 3p/4. Since p/4 = 3h + 1/4 and 3p/4 = 9h + 3/4, the integers in this range are 3h+1, …, 9h.

(b) Write R = R_a and S = S_a.
1. *Units.* 3 ≤ R ≤ 24h − 1, and R ≡ −p ≡ 3 (mod 4), so R is odd. Since 0 < a < p, gcd(a, R) = gcd(a, p) = 1, and gcd(p, R) = gcd(p, 4a) = 1. So S is a unit modulo R.
2. *Factorisation.* 1/y + 1/z = R/S is equivalent to (Ry − S)(Rz − S) = S². Both factors are positive, because 1/y < R/S and 1/z < R/S. So ordered pairs (y, z) correspond bijectively to ordered factorisations S² = d·d′ into positive divisors with d ≡ d′ ≡ −S (mod R), through y = (d + S)/R and z = (d′ + S)/R.
3. *One congruence suffices.* If d | S² and d ≡ −S (mod R), then d is a unit mod R and d′ = S²/d ≡ S²(−S)⁻¹ = −S. So the ordered pairs are counted by #{d | S² : d ≡ −S (mod R)}.
4. *The three layers.* Since gcd(p, a) = 1, each divisor of S² = p²a² is uniquely d = p^i v with i ∈ {0, 1, 2} and v | a². Use 4a ≡ p (mod R).
   - i = 2: p²v ≡ −pa ⟺ pv ≡ −a ⟺ 4pv ≡ −p ⟺ R | 4v + 1 (p and 4 are units). So these v form E_a.
   - i = 1: pv ≡ −pa ⟺ R | v + a. So these v form M_a.
   - i = 0: the complement d ↦ S²/d maps the layer i = 2 bijectively onto the layer i = 0 and preserves the congruence (step 3). So the layer i = 0 also has |E_a| elements.
   The total is 2|E_a| + |M_a|.
5. *Symmetry.* The swap (y, z) ↦ (z, y) is d ↦ S²/d. It maps the layer i = 1 to itself by v ↦ a²/v. A fixed point needs v = a, hence R | 2a; but gcd(R, a) = 1 and R is odd and at least 3, so this is impossible. So the swap has no fixed point: y ≠ z always, |M_a| is even, and the unordered pairs number (2|E_a| + |M_a|)/2.

(c) follows from (a) and (b). ∎

*Credit and scope.* This is the classical divisor parametrisation of 1/y + 1/z = R/S. The workbench's later packages attribute these coordinates to Elsholtz and Tao (§2, Propositions 2.2 and 2.6 of their paper; 43a §1.1), and the workbench does not advertise the scope identities as new (43a §1.1, citing `RESEARCH_STATE.md` line 33). The workbench also gives the exact bookkeeping: an explicit bijection with the tagged set, its inverse read off by the p-adic valuation of Ry − S, and the global statement that a counterexample prime would satisfy the finite computable condition E_a = M_a = ∅ for every a (43a §1.2, statements C and D, all re-derived there).

*Checks.* The count 2|E_a| + |M_a| against a brute-force count of ordered pairs, on all 4,398 shells of the 27 primes p ≡ 1 (mod 12) below 700 (my script), and on all 8,124 shells below 1000 (43a). Every prime p ≡ 1 (mod 12) below 30,000 has an occupied shell (my script); below 10⁴ the first occupied shell is always within 6 of the bottom (43a).

### 1.2 The first two shells (ES-03)

**Proposition 43.2 (the residual-3 shell).** Let a = 3h + 1 = (p + 3)/4, so R_a = 3. Write P₁ = ∏(2v_ℓ(a) + 1) over the primes ℓ ≡ 1 (mod 3) dividing a, and P₂ the same product over the primes ℓ ≡ 2 (mod 3). Then E_a = M_a = {u | a² : u ≡ 2 (mod 3)}, and |E_a| = |M_a| = P₁(P₂ − 1)/2. In particular a solution with least denominator a exists if and only if a has a prime factor ≡ 2 (mod 3), and there are then exactly 3P₁(P₂ − 1)/4 of them (unordered).

*Proof.* Since a ≡ 1 (mod 3), 3 ∤ a. Modulo 3, 4u + 1 ≡ u + 1 and u + a ≡ u + 1, so both conditions say u ≡ 2 (mod 3). A divisor u = ∏ℓ^{e_ℓ} of a² has u ≡ (−1)^{Σ e_ℓ} (mod 3), the sum over the primes ℓ ≡ 2 (mod 3). The exponent vectors of those primes (0 ≤ e_ℓ ≤ 2v_ℓ(a)) number P₂, and the difference between the numbers with even and odd sum is ∏_ℓ Σ_{e=0}^{2v_ℓ}(−1)^e = 1. So (P₂ − 1)/2 of them have odd sum, and the other primes contribute the factor P₁. The count of unordered solutions is |E_a| + |M_a|/2 by Theorem 43.1(b). Every solution containing a has a as its least denominator, because 3h + 1 is the smallest possible least denominator. Finally P₂ > 1 if and only if a has a prime factor ≡ 2 (mod 3). ∎

(The count 3P₁(P₂ − 1)/4 is an integer: a ≡ 1 (mod 3) forces the total exponent of the primes ≡ 2 (mod 3) in a to be even, so P₂ ≡ 1 (mod 4); 43a §1.3.)

**Proposition 43.3 (the residual-7 shell; statement).** Let a = 3h + 2 = (p + 7)/4, so R_a = 7 and 7 ∤ a. Let n₃ be the total exponent in a of the primes ≡ 3 (mod 7), and n₂₄ that of the primes ≡ 2 or 4 (mod 7). The shell is occupied if and only if a has a prime factor ≡ 5 or 6 (mod 7), or n₃ ≥ 3, or n₃ ≥ 1 and n₂₄ ≥ 1. The counts are coefficients of the group-ring element ∏_ℓ Σ_{e=0}^{2v_ℓ(a)} T^{λ(ℓ)e} in ℤ[T]/(T⁶ − 1), where λ is the discrete logarithm to base 3 modulo 7.

*Proof.* The exterior condition 7 | 4u + 1 is u ≡ −4⁻¹ ≡ 5 = 3⁵ (mod 7), and the middle condition is u/a ≡ −1 = 3³ (mod 7). In base 3, λ(1, 2, 3, 4, 5, 6) = (0, 2, 1, 4, 5, 3).
- *Sufficiency.* If a prime ℓ ≡ 5 divides a, take u = ℓ (exterior). If a prime ℓ ≡ 6 ≡ −1 divides a, take u = aℓ (middle). If n₃ ≥ 3, take u a product of primes ≡ 3 of a² with total exponent 5 (possible since 2n₃ ≥ 6), so u ≡ 3⁵ (exterior). If t ≡ 3 and ℓ ≡ 2 or 4 are primes dividing a, then u = aℓt (when ℓ ≡ 2 = 3²) or u = aℓ/t (when ℓ ≡ 4 = 3⁴) divides a² and has u/a ≡ 3³ (middle).
- *Necessity.* Suppose none of the three conditions holds. Then every prime factor of a is ≡ 1, 2, 3 or 4, and either n₃ = 0, or 1 ≤ n₃ ≤ 2 and n₂₄ = 0.
  - If n₃ = 0, a and all divisors of a² lie in the subgroup of squares {1, 2, 4}, which contains neither 5 nor −1. So u ≢ 5 and u/a ≢ −1.
  - If 1 ≤ n₃ ≤ 2 and n₂₄ = 0, every prime factor of a is ≡ 1 or 3, a ≡ 3^{n₃}, and a divisor u of a² has u ≡ 3^e with 0 ≤ e ≤ 2n₃ ≤ 4. The exterior target needs e ≡ 5 (mod 6), and the middle target needs e − n₃ ≡ 3 (mod 6) with |e − n₃| ≤ n₃ ≤ 2. Both are impossible.

The counting statement follows by recording the discrete logarithms of the divisors as exponents of T. ∎

*Checks.* Both propositions on all 19,564 primes p ≡ 1 (mod 12) below 10⁶ (43a); Proposition 43.2 again on all 4,472 such primes below 2·10⁵ (my script). Of the primes p ≡ 1 (mod 12) below 10⁶, 989 have both shells empty; all of them are ≡ 1 (mod 24), and the first are 1129, 1201, 2521 (43a).

### 1.3 Which primes remain

The workbench proves by explicit families that the equation is solvable for p ≡ 2 (mod 3), for p ≡ 3 (mod 4) and for p ≡ 13 (mod 24):
- p ≡ 2 (mod 3): (p, (p+1)/3, p(p+1)/3);
- p ≡ 3 (mod 4): ((p+1)/4, p(p+1)/2, p(p+1)/2);
- p ≡ 13 (mod 24): (a, pa/2, pa) with a = (p+3)/4, which is even.

(All three identities: my script, p < 20,000.) So its own reduction leaves the primes p ≡ 1 (mod 24). Later packages restrict to the "hard" primes p ≡ 1, 121, 169, 289, 361, 529 (mod 840). These are exactly the unit squares modulo 840 (a group of order 1·1·2·3 = 6; my script lists them), and the reduction to them is classical (Mordell, *Diophantine Equations*, 1969). It is not proved in the texts read. 43a checked that the 18 non-square unit classes c ≡ 1 (mod 24) are each covered by an explicit polynomial family with modulus dividing 840. A reader should say: the classical identities reduce the conjecture to p ≡ 1, 121, 169, 289, 361 or 529 (mod 840); the workbench proves the weaker reduction to p ≡ 1 (mod 24) itself.

## 2. The structural items

The workbench's 28 structural items (17–23 September) are listed in 43a §2 with their statements, labels and the depth of reading. The ones below were audited; the rest are **located**.

- **Item 6 (audited).** Let L_a = 8τ(a)²/φ(R_a) − ℰ_a, where ℰ_a is the residue-collision energy of the 2τ(a) divisors of pa modulo R_a. For p ≡ 1 (mod 4) and p ≥ 2²⁰, the sum of L_a over the shells a ∈ (p/4, p/2) is at most −(1/24)p log p. So the lower bound that keeps only the principal character, summed over shells, is negative for large p: that method cannot prove occupancy. All finite claims reproduce (for example p = 944329, a = 236094, R = 47: T_a = 60).
- **Item 7 (audited).** For p ≡ 1 (mod 8), explicit bounds in terms of the least quadratic nonresidue ν_p. At the hard primes: a middle state (a, u) on a shell p/4 < a < p/2 has a ≤ 3(p+3)/11, and an exterior state satisfies 22(p+1) ≤ 23(p − 2a + 1)²; here a is the shell's first denominator, not necessarily the least denominator of the solution. The workbench says this localises solutions and does not prove that the region is occupied. 43a found one unstated step (gcd(r, Q) = 1, which holds because a common prime would divide s) and confirmed the workbench's three presentation repairs.
- **Item 14 (audited).** For h = 4j − 1 > t, the divisors W of j² with W ≡ t (mod h) are canonical, companion, or members of a finite template list; the finite ones satisfy the sharp bound h ≤ t² − 3t + 1, with equality exactly when w = n = 1 and t = 4ℓ + 2 in the note's parametrisation; equality is attained at infinitely many primes p ≡ 1 (mod 840), for t = 6 + 420z. For every t ≥ 4, infinitely many hard primes have an exterior state whose same-grade middle box is empty.
- **Item 21 (audited).** For a proper rational trace source, the complete set of same-word residual-divisor returns is {k | R : d | k, k ≡ 1 (mod 4K(u))}. A uniform strict return exists exactly for the nine words u | 36; for every other word, infinitely many hard primes have proper middle sources and no return. Checked against brute force on all 4,233 sources at primes below 2600.
- **Item 22 (audited, certificate).** For every solution at p ≡ 1 (mod 12), an explicit symmetric polynomial 𝔑(p, x, y, z) of degree 8 satisfies 𝔑 < −(125873811/262144)p⁸ (about −480.17p⁸), and 𝔑 < −6960.19p⁸ when p ≡ 1 (mod 24). The proof reduces to finite polynomial positivity certificates (exterior: three polynomials with 221 translated coefficients each, all positive; middle: 192 positive coefficients, and for the improvement at p ≡ 1 (mod 24) a combination with zero constant term and 191 positive coefficients), which 43a recomputed with independent code; a census of all 1,317 solutions at primes below 1300 has no violation. This is a statement about existing solutions; it says nothing about their existence.
- **Item 26 (audited for the least example).** p = 67369 is the least prime p ≡ 1 (mod 24) whose first "trace shell" (a = 16849 = 7·29·83, R = 27) precedes its first full shell (a = 16850, R = 31). Hence no universal map from rational traces to solutions can avoid increasing a.
- **Item 4 (conditional).** At every hard prime, starting from any nonresidue prime and factoring at most 25 numbers (p + σqt²)/4 with t ∈ {1, 3, 5, 7, 9}, one reaches at least six distinct nonresidue primes. The reduction is proved; the finite enumeration of its domain (1,381,117,764 rooted profiles, 5,922,259 range-compatible) was run by two workbench implementations and not by the audit. 43a tested all 108 hard primes below 40,000 directly.
- **Items 2, 3 (method counterexamples, certificates audited).** At p = 2521 a 7-cycle of the canonical factor graph is a sink with both local gates empty; at the 22-digit prime 7510085481569082811681 a canonical triangle is closed. Both primes have solutions (e.g. (636, 5611746, 70588) at 2521). The primality of the 22-digit number was checked by BPSW, not by a certificate.
- **Item 8 (certificate audited).** The middle identity p = RQ − (Q+1)²/(4A) and the bounds 4p ≥ 3t² + 6t − 25 (and 4p ≥ 3t² + 14t − 81 at hard p), t = min(R, Q), on 1,613 oriented middle states. Equality occurs at p = 41, and also at 761, 1193, 1721 and 3881; the workbench cites 41 and claims no uniqueness.
- **Item 23 (certificates audited).** Norm bounds for the receiver matrix O; the three new certificates were verified, the deduction from them was read only in part, and the sharpness families were not checked.
- **Items 11–13, 15, 20** use imported material: item 11 the C123 preprint (not in the repository) and the four-dimensional Keller map P (det DP = −2 was checked in `21_`); item 20's metric asymptotics depend on the zeta programme's NG20–NG21. They are **located**; `47_` (§0, edges 7 and 14, and §1.4) places them among the intersections.

The results bench R01–R10 and the integration arguments X1–X7 are listed with verdicts in 43a §3: all checked items are correct as stated, X1 was not recomputed, and X5 records a source-passage error (289³ ≡ 169, not −1, modulo 840).

## 3. ES-09: the (3,4,∞) monodromy covers

The workbench imports three integer matrices A₁, A₂, A_∞ from the S⁶ manuscript `alpo.ge/s6.pdf` (§2, Lemmas 2.4–2.7 there; the ES package says it was circulated by Levent Alpöge, and the YM workbench's attribution file adds that it was produced with Claude) and uses nothing else from it (43a §4).

**Audited.**
- A₁³ = A₂⁴ = A₁A₂A_∞ = I.
- The affine part of the induced representation is a cocycle whose class has infinite order; its reduction mod D has exact order D and is locally trivial on ⟨g₁⟩ and ⟨g₂⟩.
- For odd D (the source's standing hypothesis), the action on (ℤ/D)³ is transitive when 3 ∤ D; when 3 | D there are two orbits, of sizes D³/9 and 8D³/9. The orbit and genus statements are false for even D (the referee of the twentieth pass found, e.g., two orbits of sizes 2 and 6 at D = 2); in the ES application D divides the odd number R_a, so this does not affect it.
- For odd D the genera are g(D) = (5D³ − 12D² − 17D + 24)/24 and, for 3 | D, g₀(D) = (5D³ − 12D² − 81D + 216)/216 and g₁(D) = (5D³ − 12D² − 9D + 27)/27. 43a computed them from cycle counts for D = 1, 3, 5, …, 15.
- ES fails at p ⟺ the denominator-labelled cover has no section.

**Scope.** The last equivalence is correct, but it is ES-02 again: a section exists exactly when the tail denominator D = R/gcd(R, 4u+1) (or R/gcd(R, u+a)) equals 1, which is integrality. As written it adds no new arithmetic constraint. The group theory and the genus formulas stand on their own.

## 4. Negative results, with exact scope

Each row says which proposed implication fails and what the failure does not show. Every row below was checked (43a §5); the further rows of 43a §5 on items 16, 18, 24, 27 and 28 were not checked and are omitted.

| Source | Proposed implication that fails | Certificate | What it does not show |
|---|---|---|---|
| `bounded_transport.tex` | every occupied shell has a solution with unary layer A ≤ 2 | p = 37, a = 12: only u = 8, (A, B, s) = (3, 2, 2); solution (12, 42, 1036) | not a failure of the global cutoff: a = 10 works at the same prime |
| first-two-shell sieve | occupancy of the R = 7 shell implies a first-two-layer hit | p = 373, a = 95: E = {5, 19}, M = ∅ | nothing about other shells |
| item 2 | every canonical closed component contains a local hit | p = 2521, a 7-cycle sink | p = 2521 is solvable |
| item 3 | strict canonical descent terminates at a hit | p = 7510085481569082811681, a closed triangle | that prime is solvable |
| item 6 | the principal-only lower bound, summed over shells, is positive for large p | Σ L_a ≤ −(1/24)p log p for p ≥ 2²⁰ | nothing about the true counts, whose signed sum cancels the lost diagonal |
| item 6, p = 87481 | a nonnegative reweighting of the principal-only bounds certifies occupancy | all 21,870 shells have L_a ≤ 0; 34 are occupied | only this certificate family fails |
| item 7 §9 | two-colour positivity at odd squares | n = 25, a = 7 | not a composite counterexample |
| item 14 | same-grade middle repair from an exterior state with α = −4t, t ≥ 4 | p = 7840561 | those primes have the exterior solution |
| item 21 | a same-word residual return for words u ∤ 36 | 3,041 of 3,654 sources below 2600 lack one | endpoint solutions exist at those primes |
| item 26 | a universal trace-to-solution map never increases a | p = 67369 | p = 67369 is solvable (a = 16850) |
| `21_` Neg. 21.2 | joint averages transfer on unchanged finite torsion | p = 13, a = 4: 13 against 4 | the repaired cover restores the counts |

The common scope: every row is a statement about a method or a certificate family. None is a counterexample to the conjecture, and each certificate prime is itself solvable. None of them bears on whether the conjecture is true.

## 5. Overlaps (detailed in `47_`)

ES meets the other workbenches in more places than any other: the NS torus operator (`21_` §1), the S⁶ monodromy matrices (§3 here), the order-72 glue code R10 against the S⁶ lattice data, the split-zero semiring G(R) (R01), the Collatz identity R05, the homogenisation X4, the four-dimensional Keller map P, and the zeta dependencies NG20–NG21. Note `47_` states each as a typed morphism with its status.

## 6. Not checked

Item 4's finite enumeration; items 1, 5, 9–13, 15–20, 24, 25, 27, 28 beyond their statements; the deduction in item 23; the Pell and tail-sum sections of item 26; ES-04 to ES-08 beyond the ES-08 witness; X1; the ZIP and PDF contents (including the 488-page reader); the primality certificate of the 22-digit prime; any literature search for novelty (43a §7).

## 7. Checks

- `checks/workbenches/audit43_es/` (first pass): `check_core_reduction.py`, `check_items_arith.py`, `check_receiver_certificates.py`, `check_extras.py`, each with its recorded output; re-run on 26 September with identical results (`rerun_20260926/es/`).
- `checks/workbenches/workbench_reader_claims_checks.py`, section ES (mine): the shell count against brute force, evenness of |M_a|, occupancy below 30,000, Proposition 43.2 below 2·10⁵, the unit squares mod 840, and the three classical families.

## 8. Revision after the twentieth referee pass (06:39 UTC)

A referee (a Claude instance that did not write this note) re-derived Theorem 43.1 and Propositions 43.2–43.3 and found no error in them. Its findings on this note, each verified against the source before being applied:
- **Major.** (1) The ES–S⁶ covers of §3 are classified only for odd D (source `es_s6_counterfactual/src/core.tex`, "For a positive odd integer D" and "Complete odd-level classification"); for even D the orbit and genus statements fail. Hypothesis added. (2) The §0 summary said that E_a and M_a count the solutions with least denominator a; they count all ordered pairs completing the first denominator a (e.g. p = 37, a = 22: the pair (16, 6512) has least denominator 16). Corrected.
- **Minor, applied.** The dates of the items; the equality case of item 14; the scope of item 7's bounds; the count of located items (17) and the list in §6; the cross-reference to `47_`; the §4 sentence about rows not in the table; the size of item 4's enumeration; the S⁶ credit wording; the scope of the "no Lean" disclaimer; a credit line; "adds" (a novelty reading) replaced; "cocycle class"; the certificate counts of item 22; "occupied" defined; the status vocabulary completed.
