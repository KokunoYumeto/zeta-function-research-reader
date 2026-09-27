# The Erdős–Straus equation through residual shells: an audited record of a workbench and of the author's notes, with proofs and new results

*Claude (Anthropic, model `claude-opus-5-5`), 27 September 2026. Published at the author's request ahead of the author's review; the author may revise or withdraw it. This record replaces the Erdős–Straus reader (versions 2 and 3) and note 50_, which were withdrawn on 27 September 2026.*

## Abstract

The Erdős–Straus conjecture asserts that 4/n = 1/x + 1/y + 1/z is solvable in positive integers for every n ≥ 2. This paper is an audited record of two bodies of research on the conjecture that were carried out with AI systems, a workbench and the author's notes, together with proofs and new results. The problem is organized through the shell criterion, which reduces solvability at a prime p to the occupancy of finitely many shells, each decided by a divisor congruence. On this basis we prove or verify: exact criteria for the first two shells; residue barriers, including the width-one barrier of the author's notes; the record primes of the least-class function up to 3·10⁹; fixed-divisor families and the exact reach of carriers built from residues; the terminal support core of the notes; a quadratic-residue sieve whose conditions only 23 primes below 10⁷ satisfy and whose survivors have density zero; and the orbits of the (3,4,∞) monodromy covers at every level. On the structural side we prove that the shadow of the notes' mixed mock vector, which consists of Ramanujan's order-7 mock theta functions and gives the Ẑ invariant of −Σ(2,3,7), carries exactly the modular representation of the minimal model M(2,7) after conjugation and a twist by the character of η³, and that the order-5 block carries the Fibonacci modular data. A final part describes the further directions that the research explored and assesses them.

## 0. Introduction

### 0.1 Why this record

The conjecture is verified up to 10¹⁷ [Sa] and holds for almost all n [Va], and the classical polynomial identities solve it outside the six classes of primes that are squares modulo 840 [ET, Mo]. What remains is a question about those classes, where polynomial identities provably cannot help. Over 2026 the author investigated this question with AI systems, producing a 619-page workbench archive with a supplement and a continuation, and about seventy-five notes. The volume is large, the results are spread across many texts, and their status varies from theorem to conjecture. This record states what holds, with proofs and with the programs that check it, explains what the results mean, and says what remains open, so that a reader does not have to work through the sources to find out.

### 0.2 Main results

The results fall into four groups. Those marked *new* were obtained for this record.

1. **The shell arithmetic** (§§2–4). The shell criterion (Theorem 2.1) counts the solutions with least denominator a exactly as 2|E_a| + |M_a|. The first two shells have exact occupancy criteria (Propositions 3.1–3.3), which recover the hard classes modulo 840. Occupied shells are constrained by residue barriers (Propositions 4.1–4.3); the sharpest of them, the width-one barrier from the author's notes, requires that the primes dividing (p+R)/4 generate −1 or −4 modulo R.
2. **Records, families and carriers** (§§5–8). The strict records of the least-class function are determined up to 3·10⁹ (Proposition 5.3); the largest is 8,803,369, which needs the shell R = 107. Fixed-divisor families solve the equation on explicit progressions meeting every hard class (Theorem 6.2), and no carrier built from residues reaches a square class (Proposition 6.3, Corollary 6.4).
3. **The author's notes** (§9). The support-zero core is exactly S₈₄₀ × Q₁₁ × Q₁₉ × Q₂₃, and 550 further classes are supported but not covered by a single identity (Theorem 9.2). Eight shifted forms of p, a p + 5 lock and a visible-box principle give necessary conditions for a counterexample (Theorems 9.3–9.5); the survivors have density zero (Proposition 9.7, *new*), and 23 of them lie below 10⁷. The shadow of the notes' order-7 mock theta vector carries the M(2,7) representation (Theorem 9.14, *new*), and the order-5 block carries the Fibonacci data (Proposition 9.15, *new*).
4. **The monodromy covers** (§10). The orbits of the (3,4,∞) covers are classified at every level by one invariant, gcd(b, c, gcd(D, 6)) (Theorem 10.1, *new*).

Part B collects exact statements, most of them limits, about fifteen specific mechanisms, each with its witness (§11). Part C describes the structural directions the research explored and gives, for each, what is established and my assessment (§12).

### 0.3 What the results mean

Taken together, the results locate the difficulty of the conjecture precisely. Everything that depends only on the residue of p modulo a fixed modulus reaches every non-square class and no square class: this is the obstruction to polynomial identities, and Proposition 6.3 and Corollary 6.4 show that the workbench's carrier census meets it exactly. What does decide the square classes is the factorization of the numbers (p+R)/4: by the width-one barrier a shell can be occupied only if the prime factors of (p+R)/4 generate −1 or −4 modulo R, and under an exponent condition this is also sufficient (Proposition 4.3). A proof of the conjecture therefore has to control, for some R, the multiplicative structure of (p+R)/4, which is Question 1.

The quadratic-residue sieve shows how restrictive this already is in practice. A counterexample must be a quadratic residue modulo every odd prime factor of eight shifted forms and several more; only 23 primes below 10⁷ pass all conditions, and the survivors have density zero. Whether infinitely many survive is Question 3.

On the structural side, the notes' bridge to 3d modularity becomes a precise theorem. Ramanujan's order-7 mock theta functions, which give the Ẑ invariant of the Brieskorn sphere −Σ(2,3,7), have a shadow that transforms exactly as the characters of the (2,7) minimal model, after conjugation and a twist by the character of η³. This statement is independent of the Erdős–Straus problem. How far such structures bear on the equation depends on typed maps from the shell data to them, and those maps are what Part C and Questions 9–11 are about.

### 0.4 How this record was made

This is an audit, carried out by an AI system, of research that was itself carried out with AI systems. It covers the Erdős–Straus workbench (a 619-page archive, a 72-statement supplement, and a continuation written between 17 and 23 September 2026) and the author's notes of April–June 2026 (about twenty TeX notes with a 52-page paper, and about fifty-five further notes).

The research used a method that AI systems make practical: a large number of hypotheses, across many directions, were formulated and tested quickly. Some directions stay close to the classical arithmetic of the equation; others propose bridges to mock modular forms, moonshine, Lorentzian geometry and computability. Not every hypothesis was expected to hold, and several directions would each amount to a research programme of their own. A direction that is not yet a complete programme is not thereby invalid, and a structural bridge between two areas is mathematics whether or not it bears on the conjecture.

The audit re-derived statements from their sources, re-computed the finite statements with independent programs, organized what was verified, and added new results. The compute available did not allow every statement to be audited to full rigour, so every statement carries one of four statuses:
- **verified**: proved here, or re-computed by a program that a reader can re-run (§14);
- **not verified here**: nothing further is implied, in either direction;
- **my assessment**: a view with its reasons, written in the first person, and open to the possibility that the reasons do not cover everything;
- **proved negative**: a statement shown false or limited, with the counterexample or derivation printed in the text.

This record replaces texts that were withdrawn on 27 September 2026. Re-deriving their statements from the sources changed several of them. The identification of the notes' mock theta shadow with M(2,7) holds exactly (Theorem 9.14), where the withdrawn texts said it fails. The Lorentz-boost proposition of the Lorentzian notes is correct, and the modular flow and the boost are two real forms of one complex one-parameter group (Proposition 12.4). The statements about the constructive-algebra preprint are restricted to what is proved: three specific facts about its proof (§12.5).

### 0.5 Organization

Part A (§§1–10) contains the verified results: the classical background (§1), the shell criterion (§2), the first two shells (§3), the residue barriers (§4), records (§5), families and carriers (§6), the shear graph (§7), the quartic encoding (§8), the results from the author's notes (§9) and the monodromy covers (§10). Part B (§11) contains the proved limits of specific mechanisms. Part C (§12) describes the directions explored. §13 lists open questions and §14 the programs that verify the finite statements.

---

# Part A. Verified results

## 1. The equation and the classical background

The Erdős–Straus conjecture asserts that 4/n = 1/x + 1/y + 1/z has a solution in positive integers for every n ≥ 2. It suffices to treat primes: 4/2 = 1/1 + 1/2 + 1/2, and a solution at p gives one at every multiple of p.

Explicit polynomial identities solve the equation for every n in a primitive class r mod 840 unless r is a square modulo 840. For primes this leaves the six hard classes

  p ≡ 1, 121, 169, 289, 361, 529 (mod 840),

which are exactly the unit squares modulo 840. Elsholtz and Tao attribute this to Obláth and Mordell [ET, Mo]; Proposition 3.4 below proves it for primes. The squares cannot be removed by the same means: a primitive class n ≡ r (mod q) with r a square modulo q is not solvable by polynomial identities. This is due to Mordell and Schinzel, with the reciprocity argument going back to Schinzel and Yamamoto [ET, §1]; its shell form is §4.

Three further results frame the problem:
- **Density.** Vaughan showed that the number of n < N without a solution is at most N exp(−c log^{2/3} N) [Va].
- **Counting.** Elsholtz and Tao bounded the number of solutions and classified the solutions at primes as Type I or Type II, according as p divides one or two denominators [ET].
- **Verification.** The conjecture is verified for n ≤ 10¹⁷ (Salez [Sa]), and a 2025 preprint reports 10¹⁸ [MD].

## 2. The shell criterion

The organizing idea of the workbench is to fix the least denominator. Throughout, p is an odd prime. For an integer a > p/4 with p ∤ a put R_a = 4a − p, S_a = pa and

  E_a = {u : u | a², R_a | 4u + 1},  M_a = {u : u | a², R_a | u + a}.

The shell a is **occupied** if E_a ∪ M_a ≠ ∅.

**Theorem 2.1 (shell criterion).**
1. If x ≤ y ≤ z is a solution, then p/4 < x ≤ 3p/4. More precisely, x < p/2 and x < y, except for p ≡ 3 (mod 4) and (x, y, z) = ((p+1)/2, (p+1)/2, p(p+1)/4).
2. For each a > p/4 with p ∤ a, the ordered pairs (y, z) with 1/a + 1/y + 1/z = 4/p number exactly 2|E_a| + |M_a|. A pair with y = z occurs exactly when R_a = 1. Otherwise |M_a| is even, and the unordered pairs number |E_a| + |M_a|/2.
3. The equation is solvable at p if and only if some shell a with p/4 < a < p/2 is occupied.

*Proof.* (1) Since 1/x < 4/p ≤ 3/x, we have p/4 < x ≤ 3p/4. Suppose x > p/2. Then y < p, and p | xyz forces p | z. Write z = pz′. Then xy(4z′ − 1) = pz′(x + y), so 4z′ − 1 = pk. With N = pk + 1 one gets (4kx − N)(4ky − N) = N². But 4kx − N ≥ N + 2(k − 1), so k = 1 and x = y = (p+1)/2. If x < p/2 and y = x, then 1/x + 1/y > 4/p, which is impossible.

(2) Write R = R_a and S = S_a. Since p ∤ a, S is a unit modulo R. The equation 1/y + 1/z = R/S is (Ry − S)(Rz − S) = S², with both factors positive, so the ordered pairs correspond to the divisors d | S² with d ≡ −S (mod R). Write d = p^i v with v | a². For i = 2 the condition is R | 4v + 1, which gives E_a; for i = 1 it is R | v + a, which gives M_a; and d ↦ S²/d exchanges the layers i = 0 and i = 2. The swap (y, z) ↦ (z, y) is d ↦ S²/d. Its only possible fixed point is v = a in the middle layer, and this needs R | 2a, that is, R = 1.

(3) For p ≡ 1 (mod 4) this follows from (1) and (2). For p ≡ 3 (mod 4), the shell (p+1)/4 has R = 1 and u = a ∈ M_a. ∎

The workbench states part (2) as its exact divisor-shell bijection (archive Theorem 9.1) and proves the count by an involution between the p-adic layers (Theorem 9.64). The supplement states the criterion for p = 12h + 1 and a ∈ [3h+1, 9h].

What the criterion adds is a finite, computable certificate structure. A counterexample prime would have to satisfy E_a = M_a = ∅ for every shell a, and the remaining sections study this condition shell by shell. The two channels E and M correspond to the Type II and Type I solutions of Elsholtz and Tao [ET], which is why the locks of §9.3 reappear as faces of their parametrizations.

*Verification.* The count was checked against brute force on all 4,726 pairs (p, a) with p < 260 and p/4 < a < p. Part (1) was checked against all 2,259 solutions at the odd primes below 400. Every prime p ≡ 1 (mod 12) below 30,000 has an occupied shell.

## 3. The first two shells and the hard classes

The two smallest residuals, R = 3 and R = 7, already account for most primes, and their exact occupancy criteria explain where the hard classes come from.

**Proposition 3.1 (the residual-3 shell).** Let p ≡ 1 (mod 12) and a = (p+3)/4, so R_a = 3. Let P₁ = ∏(2v_ℓ(a) + 1) over the primes ℓ ≡ 1 (mod 3) dividing a, and P₂ the same product over the primes ℓ ≡ 2 (mod 3). Then E_a = M_a = {u | a² : u ≡ 2 (mod 3)} and |E_a| = |M_a| = P₁(P₂ − 1)/2. So the shell is occupied exactly when a has a prime factor ≡ 2 (mod 3), and there are then exactly 3P₁(P₂ − 1)/4 unordered solutions with least denominator a.

*Proof.* Modulo 3 both conditions read u ≡ 2. A divisor u of a² satisfies u ≡ (−1)^{Σe_ℓ} (mod 3), the sum running over the primes ℓ ≡ 2 (mod 3). The alternating count ∏_ℓ Σ_{e=0}^{2v_ℓ}(−1)^e = 1 shows that (P₂ − 1)/2 of the exponent vectors have odd sum. ∎

For p ≡ 5 (mod 12) the same shell satisfies |E_a| = P₁(P₂ − 1)/2 and |M_a| = P₁(P₂ + 1)/2, and it is always occupied, since 1 ∈ M_a.

**Proposition 3.2 (the residual-7 shell).** Let p ≡ 1 (mod 4) and a = (p+7)/4, so R_a = 7. Let n₃ be the total exponent in a of the primes ≡ 3 (mod 7), and n₂₄ that of the primes ≡ 2 or 4 (mod 7). The shell is occupied if and only if a has a prime factor ≡ 5 or 6 (mod 7), or n₃ ≥ 3, or n₃ ≥ 1 and n₂₄ ≥ 1.

*Proof.* In base 3 modulo 7, the exterior target −4⁻¹ is 3⁵ and the middle condition is u/a ≡ 3³. Sufficiency is by explicit divisors: a prime ℓ ≡ 5 gives u = ℓ, a prime ℓ ≡ 6 gives u = aℓ, and if n₃ ≥ 3 a product of primes ≡ 3 of total exponent 5 gives u ≡ 3⁵; otherwise u = aℓt or u = aℓ/t. For necessity: without these factors, all divisors of a² lie in the squares {1, 2, 4}, or they are powers 3^e with e ≤ 2n₃ ≤ 4, and neither target is reached. ∎

**Proposition 3.3 (the two-shell survivors).** Let p ≡ 1 (mod 12). Both shells R = 3 and R = 7 are unoccupied exactly when p ≡ 1 (mod 24), every prime factor of (p+3)/4 is ≡ 1 (mod 3), and every prime factor of (p+7)/4 is ≡ 1, 2 or 4 (mod 7). Every such p lies in one of the six hard classes. Below 10⁶ there are exactly 989 such primes, and every hard class occurs among them; the least in the classes 1, 121, 169, 289, 361, 529 are 2521, 12721, 2689, 1129, 1201 and 3049 (archive Theorem 10.6 and Corollary 10.7).

*Proof.* If p ≡ 13 (mod 24), then (p+3)/4 is even and the first shell is occupied. If p ≡ 1 (mod 24), then (p+7)/4 is even, so n₂₄ ≥ 1, and the second shell is occupied exactly when (p+7)/4 has a non-residue factor modulo 7; if it has none, p ≡ 4·(p+7)/4 is a square modulo 7. For the prime 5: if p ≡ 2 (mod 5), then 5 | (p+3)/4 with 5 ≡ 2 (mod 3), and the first shell is occupied; if p ≡ 3 (mod 5), then 5 | (p+7)/4 with 5 a non-residue modulo 7, and the second shell is occupied. So p ≡ ±1 (mod 5). ∎

**Proposition 3.4 (the reduction modulo 840).** Let p ≡ 1 (mod 24), and let (A, B, R) be (1,2,7), (2,1,7), (1,1,7), (1,2,15) or (2,1,15) according as p ≡ 3, 5, 6 (mod 7), p ≡ 2 (mod 5) or p ≡ 3 (mod 5). Then D = (p+R)/(4AB) and C = (A + pB)/R are integers, and

  4/p = 1/(ABD) + 1/(ACD) + 1/(pBCD).

*Proof.* With RC = A + pB and 4ABD = p + R, the right side is (pC + pB + A)/(pABCD) = C(p+R)/(pABCD) = 4/p. ∎

The workbench's own reduction (archive Proposition 10.2) solves p ≡ 2 (mod 3), p ≡ 3 (mod 4) and p ≡ 13 (mod 24) by three explicit families, and its later packages work with the hard primes.

## 4. Residue barriers

Why do the square classes resist? The answer, in shell form, is a family of residue barriers: a shell is empty whenever the subgroup of (ℤ/R)^× generated by the relevant primes misses the two targets.

**Proposition 4.1 (the Jacobi-symbol barrier; archive Theorem 10.9).** Let R ≡ 3 (mod 4), a = (p+R)/4 an integer, and gcd(R, pa) = 1. If (q/R) = 1 for every prime q | a, the shell a is unoccupied.

*Proof.* The Jacobi character χ = (·/R) satisfies χ(a) = 1 and χ(p) = χ(4a) = 1. So χ(d) = 1 for every divisor d of p²a², while χ(−pa) = χ(−1) = −1. ∎

**Proposition 4.2 (the group barrier and the width-one barrier).** In the same setting, with R ≡ −p (mod 4) and R ≥ 3, let G_a ≤ (ℤ/R)^× be generated by 4 and the primes dividing a, and H_a by the primes dividing a alone.
1. If −1 ∉ G_a, the shell is unoccupied. This contains Proposition 4.1, is equivalent to it for prime R, and is strictly stronger for composite R: for example p = 53, a = 26, R = 51, G_a = ⟨2⟩ ∌ −1, while (2/51) = −1.
2. (Width one; the notes' *Normalized divisor supports and the residual pre-Niemeier datum*, Theorem 3.1, and archive Theorem 15.5.) If neither −1 nor −4 lies in H_a, the shell is unoccupied. This contains (1) and is strictly stronger: for example p = 433, R = 91, a = 131. When every prime factor of R is ≡ 3 (mod 4), (1) and (2) are equivalent.

*Proof.* (1) Every divisor of a² lies in G_a, and the targets −4⁻¹ and −a lie in G_a exactly when −1 does. (2) The targets lie in H_a exactly when −4, respectively −1, does. For the equivalence when every prime factor of R is ≡ 3 (mod 4), write (ℤ/R)^× = P × O with P elementary abelian and |O| odd; if −1 = 4^j h with h ∈ H_a, then h^{|O|} = −1. ∎

**Proposition 4.3 (a converse under an exponent condition).** Suppose 2v_ℓ(a) ≥ ord_R(ℓ) − 1 for every prime ℓ | a. Then the residues of the divisors of a² are exactly H_a; the shell is occupied if and only if −1 ∈ H_a or −4⁻¹ ∈ H_a; and for prime R ≡ 3 (mod 4) the shell is occupied if and only if some prime factor of a is a non-residue modulo R.

*Proof.* Under the exponent condition, ℓ^e runs through all of ⟨ℓ⟩ as e runs from 0 to 2v_ℓ(a); this gives the first claim, and the second follows since −a ∈ H_a exactly when −1 ∈ H_a. A subgroup of the cyclic group (ℤ/R)^× that contains a non-square has even order, so it contains −1. ∎

*Verification.* The barriers hold on all 123,538 shells of the primes 5 ≤ p < 1500, and the group barrier applies beyond the Jacobi barrier on 9,462 of them. The criterion of Proposition 4.3 is correct on all 677 shells that satisfy the exponent condition. The width-one barrier from the notes decides 124 further empty shells of the primes p ≡ 1 (mod 24) below 3000.

The width-one barrier is the sharpest form of this mechanism found in either body of work. At a prime p ≡ 1 (mod 4), a shell can be occupied only if H_a contains −1 or −4, and for prime R this means a prime factor of (p+R)/4 that is a non-residue modulo R. This is the shell form of the obstruction to polynomial identities. It also says what a proof of the conjecture must produce: for some R, a factorization of (p+R)/4 whose prime factors generate −1 or −4 (Question 1).

## 5. The least-class function and record primes

Following Ionascu and Wilson [IW], put 𝒞_i = {n : 4/n = 1/x + 1/y + 1/z with x ≤ (n + 4i − 1)/4} and h(n) = min{i : n ∈ 𝒞_i}. An odd prime p is a **strict record** if h(q) < h(p) for all primes q < p.

**Lemma 5.1.** For p ≡ 1 (mod 4), the least denominator over all solutions is the least occupied shell a, and h(p) = (R + 1)/4 with R = 4a − p. For p ≡ 3 (mod 4), h(p) = 1.

**Corollary 5.2.** If p is not in a hard class, then h(p) ≤ 2. So every strict record after 73 lies in a hard class. *Proof.* Lemma 5.1 with §3. ∎

**Proposition 5.3 (record primes).** The strict records up to 8,803,369, with h(p) and the residual of the least occupied shell, are

  (2, 1, 2), (73, 2, 7), (1129, 3, 11), (1201, 6, 23), (21169, 8, 31), (118801, 15, 59), (8803369, 27, 107).

There is no further strict record below 3·10⁹, and no other prime below 3·10⁹ has h ≥ 22. The primes with h = 21 are 287,567,281, 651,412,441 and 2,188,875,529; those with h = 20 are 778,103,881, 1,749,233,641, 2,535,613,921 and 2,809,257,889; those with h = 19 are 230,089,729 and 793,592,809.

These are exact computations. Two independent segmented programs agree on every record, on every prime with h ≥ 19, and on the full histogram of h. The list reproduces the one printed by Ionascu and Wilson, with the class label of 1201 corrected to 𝒞₆ (archive Proposition 17.6). At p* = 8,803,369 the least occupied shell has R = 107, with a = 2,200,869 = 3²·11²·43·47, |E_a| = 0 and |M_a| = 2, so exactly one solution has this least denominator, from u = 11²:

  4/8803369 = 1/2200869 + 1/181085300330 + 1/3293760527702370.

The records extend the table of Ionascu and Wilson by more than two orders of magnitude. They show that h grows very slowly on the primes: the value 27 is reached at p* and not exceeded below 3·10⁹. Whether h is unbounded is open (Question 6).

**Deficit progressions.** For records whose residual R = 2m + 1 is a safe prime and whose shell has exactly one non-residue prime factor, to exponent one, the archive defines a deficit set D ⊂ ℤ/m (§19.1). It conjectures that D is a difference-proper generalized progression of rank at most two, whose two odd sheets cover ℤ/m. At the two records with non-empty deficit, D = {11, 14, 15, 18} ⊂ ℤ/29 for (118801, 59), a rank-two rectangle, and D = {23 + 42j : 0 ≤ j ≤ 9} ⊂ ℤ/53 for (8803369, 107). The hypothesis of strict recordness cannot be dropped: see §11.

## 6. Fixed-divisor families and the reach of residue carriers

The workbench builds explicit families by fixing a divisor in the shell criterion. The general form is the following.

**Proposition 6.1 (fixed-divisor families).** Let R ≥ 3 be odd, c, s ≥ 1 with gcd(c, R) = 1 and s | c², and n ≡ −R (mod 4c). Put a = (n+R)/4 and h = a/c.
1. If n ≡ −cs⁻¹ (mod R), then 4/n = 1/a + 1/y + 1/z with y = n(nsh + a)/R and z = (c²h/s + na)/R.
2. If n ≡ −4s (mod R), then 4/n = 1/a + 1/y + 1/z with y = n(a + s)/R and z = n(a + a²/s)/R.

Each case is one class modulo 4cR. If gcd(cR, 35) = 1, that class meets all six hard classes or none, and it meets all six exactly when it is ≡ 1 modulo gcd(4cR, 24).

*Proof.* The proof of Theorem 2.1(2) uses only that S = na is a unit modulo R. Take d = n²sh in case 1 and d = ns in case 2. ∎

This extends the archive's constant-factor carriers (Lemma 24.218) from primes to all n.

**Theorem 6.2 (four families; archive Theorem 24.219).** For k ≥ 0 put g₁ = 31k + 30, g₂ = 31k + 15, m₃ = 23k + 15, m₄ = 23k + 19, w₃ = 1116k + 727 and w₄ = 4464k + 3683. Then 4/n_i = 1/a_i + 1/b_i + 1/c_i with

| i | n_i | a_i | b_i | c_i |
|---|---|---|---|---|
| 1 | 248k + 209 | 2g₁ | 2n₁(k+1) | 2n₁g₁(k+1) |
| 2 | 248k + 89 | 2g₂ | n₂(2k+1) | 2n₂g₂(2k+1) |
| 3 | 17112k + 11137 | 186m₃ | 12n₃m₃w₃ | 124m₃w₃ |
| 4 | 17112k + 14113 | 186m₄ | 6n₄m₄w₄ | 31m₄w₄ |

*Proof.* 4a_ib_ic_i = n_i(b_ic_i + a_ic_i + a_ib_i) is a polynomial identity in k. ∎

These are instances of Proposition 6.1, with (R, c, s) = (31, 2, 2), (31, 1, 1), (23, 186, 18) and (23, 186, 36). Each progression meets every hard class, so by Dirichlet's theorem each solves the equation at infinitely many primes in every class left open by the reduction modulo 840. The strict records 1201 = n₁(4) and 21169 = n₂(85) are examples. This does not contradict the obstruction to polynomial identities, since each n_i(0) is a non-square modulo the relevant R, as the next proposition shows in general.

**Proposition 6.3.** The class on which a fixed-divisor family applies contains no square modulo 4cR.

*Proof.* If n were a square, then the prime 2 and the odd primes dividing c give (c/R) = 1 by reciprocity, and so (s/R) = 1. But n ≡ −4s or n ≡ −cs⁻¹ gives (n/R) = −1. ∎

**Corollary 6.4 (square rows of the carrier census).** The archive's carrier census (§24) forces 97.606% of the rows of its final hard domain through fixed-divisor carriers. The rows that are squares modulo the census modulus are never forced by such carriers; there are 2,759,345,613,832,500 of them, 1/1024 of the domain. Each further odd prime modulus halves their share, but no finite chain of such carriers removes them.

The census's reported counts are internally consistent: each domain is the previous survivor count times q − 1, and forced plus survivors equals the domain in every row.

Proposition 6.3 and Corollary 6.4 give a precise account of what the census achieves and of what remains. Carriers whose applicability depends only on the residue of p modulo a fixed modulus reach every non-square row and no square row. The square rows are reached by mechanisms that use more than residues, for instance the factorization of (p+R)/4, as in §4. This is the dividing line that recurs throughout the record: residue-level structure organizes the problem completely up to the square classes, and the square classes need arithmetic input of a different type.

## 7. The shear graph

The supplement encodes the solutions with first denominator a by W_a = {(m, n) : m, n | pa, gcd(m, n) = 1, R_a | m + n}, and studies the shears L(m, n) = (m + n, n) and J(m, n) = (m, m + n) as maps between adjacent shells.

**Proposition 7.1 (two shears; supplement §5, extended).** Let p be prime and consider all shells p/4 < a < p.
1. If p ≢ 2 (mod 3), no two shear edges compose. The supplement proves this for p ≡ 1 (mod 12); its proof uses only p ≢ 2 (mod 3).
2. At some primes p ≡ 2 (mod 3) paths of two edges exist, for example at p = 131 and p = 1613.

**Proposition 7.2 (the shear graph).**
1. Every vertex has at most one incoming and one outgoing edge, so the components are directed paths.
2. The diagonal vertices (a+i, a+i, 1), 0 ≤ i ≤ k, form a path of L-edges if and only if R + 4i | p + 4 for all i.
3. A path of two edges forces R(R+4) | p + 4.
4. Every prime p ≡ 131 (mod 180) has a path of two edges. More generally, every class containing primes ≡ 2 (mod 3) contains infinitely many primes with such a path.
5. For every k, infinitely many primes have a path of length k.

Among the primes p ≡ 2 (mod 3), those with a two-edge path have upper relative density at most 0.335, by Brun–Titchmarsh and the convergence of Σ1/φ(R(R+4)). Below 10⁷ they are 5.24% of these primes.

*Proofs.* One edge has a rigid shape: an L-edge is (a, m, 1) ↦ (a+1, m+1, 1) with m | a and R_a | m + 1. For two edges, 3 divides both K = a − m and C = p + 4 − 4K, which forces p ≡ 2 (mod 3). The graph statements follow from the shape of an edge, and the existence statements use the Chinese remainder theorem and Dirichlet's theorem. ∎

## 8. The quartic encoding

The ES/Fable reader of 20 September encodes a solution as the binary quartic H(U, V) = −S⁻¹(U − pV)(U − xV)(U − yV)(U − zV), with S = p + x + y + z and normalized coefficients u₀, 1, u₂, u₃, u₄.

**Proposition 8.1.** On solutions, p = −5u₄/u₃ and

  625u₀u₄³ − 125u₃u₄² + 25u₂u₃²u₄ − 4u₃⁴ = 0.

Conversely, every (u₀, u₂, u₃, u₄) with u₀u₃u₄ ≠ 0 satisfying this relation comes from a triple of non-zero complex numbers x, y, z with 4/p = 1/x + 1/y + 1/z. So the relation is the equation itself, written in quartic coordinates.

*Proof.* Substitution gives P³(pσ₂ − 4P) = 0, and the converse gives pσ₂ = 4P. ∎

The encoding makes the equation available to the invariant theory of binary quartics. Proposition 8.1 establishes that the passage is faithful, so any constraint found in quartic coordinates transfers back.

## 9. Results from the author's notes

The author's notes develop the shell arithmetic in a vocabulary of supports. A class of primes is *supported* when some certificate applies to it, and *unsupported* when none does. The notes use this vocabulary to build certificate systems, sieves and locks, and they attach structural layers to it. This section states the arithmetic results of the notes that were verified, together with the structural result on mock theta functions. The further structural directions are described in Part C.

### 9.1 The terminal support core

Put M₂₃ = 840·11·19·23. A base class is a hard class modulo 840 together with units modulo 11, 19 and 23; there are 23,760 base classes. The source note, *Finite central-cover reductions for residual Erdős–Straus shells*, defines elementary j = 1 certificates (R, m, u):
- R ≡ 3 (mod 4) and u | m²;
- n ≡ −R (mod 4m), n ≡ −4u (mod R) and gcd(n, R) = 1.

Such a certificate occupies the shell through the middle channel.

**Lemma 9.1.** For such a certificate with gcd(m, R) = 1, (n/R) = −∏_{ℓ|u} ε_ℓ(n)^{v_ℓ(u)}. In particular no n in the class is a unit square modulo lcm(4m, R).

**Theorem 9.2 (the terminal core).**
1. A base class has no elementary j = 1 certificate, with R built from 3, 5, 7, 11, 19, 23, on any lift if and only if it is a square modulo 11, 19 and 23. So the support-zero core is exactly S₈₄₀ × Q₁₁ × Q₁₉ × Q₂₃, with 2970 classes.
2. The base classes covered by no single identity among Salez's seven modular equations with modulus dividing M₂₃ number 3520. They are the 2970 core classes together with 550 classes that are non-squares modulo 11, 19 or 23.

*Proof.* The *if* direction of (1) follows from Lemma 9.1 and quadratic reciprocity. The remaining counts are finite computations: the note's own script and an independent program both give 4951 and then 2970. The computation behind (2) is calibrated at Salez's modulus, where it reproduces his count of 147,348 [Sa]. ∎

The note's central-cover report is thus confirmed exactly: the support-zero core is the product of the six hard classes with the quadratic residues modulo 11, 19 and 23. Theorem 9.2 also locates what lies between the core and the classes that single identities leave open. The 550 further classes are supported: each has a certified lift, but no single identity covers the whole class. The prime 3361 lies in one of them, and indeed 4/3361 = 1/841 + 1/110139970 + 1/950330. In the notes' split-zero vocabulary, the core classes are unsupported, and the 550 classes are supported but not covered. By Dirichlet's theorem the core carries 1/256 of all primes, and the open classes carry 1/216.

Relative to Salez's count, the theorem identifies which part of the open set is forced by quadratic reciprocity (the core) and which part is an artefact of using one identity per class (the 550). Whether combinations of identities cover the 550 classes at some finite level is Question 4.

### 9.2 A quadratic-residue sieve

The notes observed that shifted forms of p produce certificates whenever they have a prime factor at which p is a non-residue. Together with the archive's rows, this gives a sieve of necessary conditions for a counterexample. Let p ≡ 1 (mod 24). A certificate is a shell R ≡ 3 (mod 4) with gcd(R, pa) = 1 and a divisor u | a² with R | 4u + 1 (channel E) or R | u + a (channel M).

**Theorem 9.3 (eight shifts).** Let q be an odd prime dividing

  F(p) = (p+1)(p+2)(p+3)(p+4)(p+7)(p+8)(2p+1)(3p+1)

with (p/q) = −1. Then the following table gives a certificate. Equivalently, a counterexample p ≡ 1 (mod 24) is a quadratic residue modulo every odd prime factor of F(p).

| shift | q with (p/q) = −1 | shell R | u | channel |
|---|---|---|---|---|
| p + 1 | q ≡ 3 (mod 4) | q | a | E |
| p + 4 | q ≡ 3 (mod 4) | q | 1 | M |
| p + 2 | q ≡ 5, 7 (mod 8) | q if q ≡ 7; 3q if q ≡ 5 (mod 8) | a/2 | E |
| p + 8 | q ≡ 5, 7 (mod 8) | as for p + 2 | 2 | M |
| 2p + 1 | q ≡ 5, 7 (mod 8) | as for p + 2 | 2a | E |
| p + 3 | q ≡ 2 (mod 3) | 3 | q | E |
| p + 7 | q ≡ 3, 5, 6 (mod 7) | 7 | q, aq, 2aq | E, M, M |
| 3p + 1 | q ≡ 2 (mod 3) | (4q+1)/3 | q | E |

*Proof.* For q | p + k with q ∤ k, (p/q) = (−k/q), and similarly for 2p + 1 and 3p + 1. Each row's divisibility is an identity, for example 4a + 1 = p + R + 1 and 4(a+1) = p + R + 4. Coprimality holds because a common prime of R and a divides 4a − R = p. ∎

The rows p + 1 and p + 4 are archive Theorem 24.50, the rows p + 3 and p + 7 are §3 read through reciprocity, and 3p + 1 is archive Theorem 24.171. The conditions from p + 2, p + 8 and 2p + 1 come from the notes. The rows p + 1, p + 2, 2p + 1, p + 4 and p + 8 are unions of Salez's charts (15b) and (14c) with small constants. All 780,700 certificates at the primes p ≡ 1 (mod 24) below 10⁷ were built and verified.

The rows from the notes carry weight at the extreme cases. At the record prime p* = 8,803,369, the archive's rows give nothing: p* + 1, p* + 3, p* + 4, p* + 7 and 3p* + 1 have no prime factor at which p* is a non-residue. The notes' rows certify it. The factor q = 223 of p* + 2 is ≡ 7 (mod 8) with (p*/q) = −1, and the factor q = 677 of 2p* + 1 is ≡ 5 (mod 8) with (p*/q) = −1.

**Theorem 9.4 (p + 5).** Let N = (p+5)/2, and let p ≡ 9 (mod 40), or p ≡ 121 (mod 840), or p ≡ 1, 361 (mod 840) with p ≡ 4 (mod 9). If some prime q | p + 5 has (p/q) = −1, then N has a divisor ≡ −p or ≡ −1 (mod 20), and it gives a certificate through the locks of Proposition 9.9 with μ = 5.

These classes contain the hard classes 121, 169, 289 and 529. The case p ≡ 9 (mod 40) is in the note *Full divisor locks, QR subtori, and survivor idempotents* (Theorem 3.7(ii), Corollary 3.8(ii), Theorem 4.2).

**Theorem 9.5 (the visible-box principle).** Let R ≡ 3 (mod 4) be prime and c a class of hard primes modulo 10080. Let Box(c) be the set of residues modulo R of products of the primes 2, 3, 5, 7 up to twice the exponents that c forces in (p+R)/4. If Box(c) contains every non-zero square modulo R, then for every prime p ∈ c the shell R is occupied exactly when some odd prime q | p + R has (p/q) = −1.

A complete search up to R = 700 finds good classes for R = 3, 7, 11, 19, 23 and for the further shells R = 31, 47, 59, 71 and 311.

**Proposition 9.6 (μ = 17).** For p ≡ 361 or 529 (mod 840), p ≡ 1 (mod 9) and p mod 17 ∈ {8, 15, 16}, the number (p+17)/2 has a divisor ≡ −p or −1 (mod 68) if and only if some prime q | p + 17 has (p/q) = −1.

The primes p ≡ 1 (mod 24) satisfying these conditions cumulatively are counted below.

| conditions | below 10⁶ | below 10⁷ | below 10⁸ |
|---|---|---|---|
| hard classes | 2370 | 20,513 | 179,468 |
| and the eight shifts | 54 | 247 | 1431 |
| and p + 5 on its classes | 29 | 146 | 816 |
| and μ = 17 | 29 | 145 | 806 |
| and the visible-box shells | 7 | 31 | 165 |

Eight further conditions of the same kind come from p + 6, p + 12, p + 16, p + 20, p + 24, p + 36, 5p + 1 and 6p + 1. They arise through the certificate shapes u = s with R | p + 4s, u = a/t with R | p + t, and u = ta with R | tp + 1. With them, 23 primes remain below 10⁷.

The sieve is an unconditional reformulation: a counterexample must survive every row. The survivors are rare, and the following proposition proves that they have density zero.

**Proposition 9.7 (density zero).** The primes p ≡ 1 (mod 24) that satisfy the condition of the row p + 1 alone have relative density zero among the primes p ≡ 1 (mod 24). A fortiori the same holds for the primes satisfying all the conditions above.

*Proof.* If q ≡ 3 (mod 4) divides p + 1, then (p/q) = (−1/q) = −1, so the row p + 1 gives a certificate. Hence a survivor satisfies p ≢ −1 (mod q) for every prime q ≡ 3 (mod 4); note that q = 3 never divides p + 1 when p ≡ 1 (mod 24). Let q₁, …, q_k be the first k primes ≡ 3 (mod 4) beyond 3. By Dirichlet's theorem in the progressions modulo 24q₁⋯q_k, the primes p ≡ 1 (mod 24) with p ≢ −1 (mod q_i) for all i ≤ k have relative density ∏_{i ≤ k}(1 − 1/(q_i − 1)). Since Σ 1/q over the primes q ≡ 3 (mod 4) diverges, this product tends to 0 as k grows. ∎

Whether infinitely many primes survive all the conditions is Question 3. A negative answer would prove the conjecture outside a finite set.

**Remark 9.8 (the Collatz connection).** For p ≡ 1 (mod 8), the number (3p+1)/4 is the odd Collatz successor of p. So a counterexample p ≡ 1 (mod 24) has an odd Collatz successor built only from primes ≡ 1 (mod 3), by the row 3p + 1. The odd Collatz predecessors satisfy Π_{k+1} = 4Π_k + 1, which is the notes' map a ↦ 4a + 1. They are ≡ 5 (mod 8), hence solved by the shell R = 3, so only the first member of a predecessor chain can be a hard prime [La].

### 9.3 Identities and locks

**Proposition 9.9 (the full-divisor locks).** Let μ be odd and N = (p + μ)/2.
1. If d | N is odd with d ≡ −p (mod 4μ), the shell R = d carries the E-certificate u = a/μ.
2. If h | N with h ≡ −1 (mod 4μ), put e = N/h and t = (h+1)/(4μ). Then a = 2μet and R = μ + 2e satisfy 4a − p = R, and u = μ²t is an M-certificate.

These locks are the faces A = 1 of Type I and C = 1 of Type II of Elsholtz and Tao [ET]; lock (2) is Lopez's Type B [Lo]. In the notes' proof of (1), the numerator should read ps + p + μ.

**Proposition 9.10 (Rosati's family).** For k ≥ 1, c | k and m = 4k − 1, every n ≡ −c (mod m) satisfies

  4/n = 1/(kn) + 1/(k(n+c)/m) + 1/(kn(n+c)/(mc)).

This is Salez's chart (14a) with (B, C, D) = (c, 1, k/c).

The two direct 29-channels of *Terminal residual coordinates* (Theorems 7.1–7.2), n ≡ 917 (mod 1276) and n ≡ 1605 (mod 2204), are correct. They are Salez's chart (15b) with (B, C, F) = (1, 29, 11) and (1, 29, 19), and the first lies in Rosati's family with (k, c) = (80, 40). The note characterizes these two as the direct channels. That characterization holds for lock divisors that are single primes from {5, 11, 19, 23}. Composite lock divisors give further channels; for example the lock μ = 5, d = 31 solves n ≡ 429 (mod 620), where a = (n + 31)/4 is divisible by 5 and u = a/5 satisfies 31 | 4u + 1.

**Computations.**
- **Lock certificates.** Every hard prime below 10⁸, all 179,468 of them, has a lock certificate. Among the primes p ≡ 1 (mod 4) below 3·10⁶, only 409 has none.
- **Type II solutions.** Every prime p ≡ 1 (mod 24) below 10⁸ has a Type II solution in a shell R ≤ 107, and only p* = 8,803,369 needs R = 107.
- **Complement-square certificates.** The certificates u = Q² with Q | a (Lopez's Type C) occur at most primes. The least p ≡ 1 (mod 24) without one is 97, and the least hard prime without one is 3361.

### 9.4 Single shells

**Proposition 9.11 (the one-congruence criterion).** Let R ≡ −p (mod 4) and N = pa. If p² ∤ R, the shell is occupied if and only if some d | N² has d ≡ −N (mod R). For gcd(R, pa) = 1 this is Theorem 2.1(2), and the case R = kp with p ∤ k follows in the same way. The hypothesis p² ∤ R is needed: at p = 73, R = 7·73², the divisor d = 4·73³ satisfies the congruence and gives y = 60, but z = 1920/73 is not an integer.

The notes state the criterion in four places without the hypothesis p² ∤ R: the defect-completion article (Lemma 2.1), *Split-zero residual moonshine* (Theorem 3.1), the A₈ snowflake note (Theorem 2.1) and *Terminal-core lock covers* (Theorem 2.1). Every application in the notes has R < 3p², so the hypothesis holds there and the applications are unaffected.

**Proposition 9.12 (ramified shells).** If R | p − 1, then E_a = M_a. If R | p² − 1, then u ↦ a²/u preserves E_a, and |E_a| is odd exactly when R | p + 1.

**Proposition 9.13 (the pair-count series; the defect-completion article, Theorem 4.3).** Let A_R(n) count the triples (X, Y, Z) with XYZ = n, gcd(X, Y) = 1 and R | X + Y. Then A_R(pa) counts the ordered certificates of a coprime shell, and for R ≥ 3

  Σ_{(n,R)=1} A_R(n)/n^s = φ(R)⁻¹ Σ_{χ mod R} χ(−1) ζ_R(s)L(s, χ)L(s, χ̄)/ζ_R(2s).

This is the p-dependent analytic object of the notes: through A_R(pa), its coefficients see the factorization of (p+R)/4, which §4 identifies as the input any proof must use. A congruence cover of the hard classes by the divisor-pair note's central and edge templates would need a template class containing a square. Proposition 6.3 and the same reciprocity argument show that no template class does, so the templates have to be combined with inputs beyond residues, as in §4.

### 9.5 The mock theta functions of the notes and the minimal model M(2,7)

The notes attach to the cubic middle of the shell problem an explicit rank-three modular object. They follow the framework of 3d modularity [CCFGH] and its revision [CCKPS]. There, the Ẑ invariants of plumbed 3-manifolds are quantum modular, and their companions under orientation reversal are mock or mixed mock modular. For the Brieskorn sphere Σ(2,3,7) the relevant objects are Ramanujan's order-7 mock theta functions [CFS, CCKPS].

The note *An explicit mixed-mock Virasoro support realization* works with m = 42 and the Atkin–Lehner group K = {1, 6, 14, 21}. It computes the projector P₇ = P⁺(6)P⁺(14)P⁺(21)P⁻(42) on ℂ[ℤ/84] and its image basis

  v₁ = e₁ − e₁₃ − e₂₉ + e₄₁ − e₄₃ + e₅₅ + e₇₁ − e₈₃,
  v₅ = e₅ + e₁₉ + e₂₃ + e₃₇ − e₄₇ − e₆₁ − e₆₅ − e₇₉,
  v₁₁ = e₁₁ + e₁₇ + e₂₅ + e₃₁ − e₅₃ − e₅₉ − e₆₇ − e₇₃,

and writes regularized indefinite theta functions whose shadows lie on these three vectors. Two statements were verified.

First, the explicit mixed mock functions of the note are Ramanujan's order-7 mock theta functions, in Zagier's vector M₇, whose components are q^{−1/168}F₀, q^{−25/168}F₁ and q^{47/168}F₂ up to signs [Za]; the q-expansions agree through q⁴⁰, up to one sign. For m = 30 the same construction gives the order-5 functions. The first order-7 function is the invariant q^{1/2}Ẑ₀ of the Brieskorn sphere −Σ(2,3,7) [CFS, eq. (3.20)]. So the notes' construction lands exactly on the mock theta functions of 3-manifold invariants.

Second, the note identifies the shadow of this vector with the characters of the minimal model M(2,7), whose central charge is c = −68/7 and whose conformal weights are h = 0, −2/7, −3/7. The following theorem establishes this identification at the level of modular representations.

For r ∈ {1, 5, 11} put

  G_r(τ) = Σ_{ℓ ∈ ℤ} v_r(ℓ mod 84) · ℓ · q^{ℓ²/168},

the weight-3/2 unary theta series on the three support vectors. For a vector F of weight k define ρ_F by F(−1/τ) = (−iτ)^k ρ_F(S) F(τ) and F(τ + 1) = ρ_F(T) F(τ). Let ρ = ρ_G, and let ρ_{2,7} be the representation of SL₂(ℤ) on the characters χ_s = χ^{(2,7)}_{1,s}, s = 1, 2, 3, given by the Rocha-Caridi formula [RC]. Let ε be the multiplier of Dedekind's η, so that ε(S) = 1 and ε(T) = e(1/24) in this convention. Write c_k = (2/√7) sin(kπ/7).

**Theorem 9.14 (the order-7 shadow carries the M(2,7) representation).** One has

  ρ(S) = [[−c₁, c₂, c₃], [c₂, c₃, −c₁], [c₃, −c₁, c₂]],  ρ(T) = diag(e(1/168), e(25/168), e(121/168)),

in the basis (G₁, G₅, G₁₁). Let P be the signed permutation sending (G₁, G₅, G₁₁) to (χ₂, χ₃, −χ₁). Then

  conj(ρ(S)) = P ρ_{2,7}(S) P⁻¹  and  conj(ρ(T)) · e(1/8) = P ρ_{2,7}(T) P⁻¹.

Hence ρ̄ ⊗ ε³ ≅ ρ_{2,7}: the shadow representation of the order-7 mock theta vector, conjugated and twisted by the character of η³, is the modular representation of the M(2,7) characters.

*Proof.*
- **The S-matrix of ρ.** The theta decomposition gives θ_{m,μ}(−1/τ, z/τ) = √(τ/2mi) e(mz²/τ) Σ_ν e(−μν/2m) θ_{m,ν}(τ, z) [EZ, §5]. Differentiating in z at z = 0 gives θ¹_{m,μ}(−1/τ) = (−iτ)^{3/2} (i/√2m) Σ_ν e(−μν/2m) θ¹_{m,ν}(τ). Since the vectors v_r are odd with disjoint supports, ρ(S)_{ab} = (i/√84) Σ_r v_a(r) e(−rb/84). This formula agrees with a direct evaluation of the series at sample points to 29 digits.
- **The S-matrix of ρ_{2,7}.** The Rocha-Caridi formula gives ρ_{2,7}(S)_{sσ} = (2/√7)(−1)^{s+σ} sin(2πsσ/7).
- **The S-identity.** Both sides lie in ℚ(ζ₁₆₈), using √7 = −i Σ_{k=1}^{6} (k/7) ζ₇^k and √3 = −i(ζ₃ − ζ₃²). The identity for S was verified exactly, by reduction modulo the cyclotomic polynomial Φ₁₆₈, and it agrees numerically to 38 digits.
- **The T-identity.** It follows from the exponents. The values −r²/168 + 21/168 for r = 1, 5, 11 are 20/168, −4/168 and 68/168, that is 5/42, −1/42 and 17/42. These are the values of h − c/24 for s = 2, 3, 1. ∎

The note reaches the M(2,7) exponents by its cubic phase transport T ↦ e(−1/24)T³. That map sends the labels 1, 5, 11 to −1/42, 17/42 and 5/42: the correct set of exponents, but a different matching of labels to characters. With the note's matching, 1 ↦ χ₃, 5 ↦ χ₁ and 11 ↦ χ₂, the diagonal S-entries differ in absolute value: ρ(S)₁₁ = −c₁, while ρ_{2,7}(S)₃₃ = c₃. So no signed permutation and scalar realize that matching. Theorem 9.14 realizes the identification through conjugation and the η³ twist instead, and with it the note's claim that the explicit mixed mock functions carry a c = −68/7 character shadow holds exactly. The note's third-order modular differential equation, with coefficients −5/252 and 85/74088, has the M(2,7) exponents as its indicial roots; its coefficients check.

**Proposition 9.15 (the order-5 block carries the Fibonacci data).** For m = 30, K = {1, 6, 10, 15} and the note's vectors w₁ = e₁ + e₁₁ + e₁₉ + e₂₉ − e₃₁ − e₄₁ − e₄₉ − e₅₉ and w₇ = e₇ + e₁₃ + e₁₇ + e₂₃ − e₃₇ − e₄₃ − e₄₇ − e₅₃, the weight-3/2 series G₁, G₇ built as above satisfy

  ρ(S) = (2/√5) [[sin π/5, sin 2π/5], [sin 2π/5, −sin π/5]],  ρ(T) · e(−1/8) = diag(e(−7/60), e(17/60)).

These are the Fibonacci modular data, the data of the level-one G₂ WZW model at c = 14/5 [RSW]. The Lee–Yang data of M(2,5) are not a twist of them by any signed permutation and scalar, since the absolute values of their diagonal S-entries are (2/√5) sin(2π/5), not (2/√5) sin(π/5).

*Proof.* The same method as for Theorem 9.14, with the exact verification in ℚ(ζ₁₂₀). ∎

The rank-two note matches the Lee–Yang exponents −1/60 and 11/60 through the cubic phase transport. By Proposition 9.15, the order-5 shadow carries the Fibonacci representation rather than the Lee–Yang one. Rank-two modular data are classified in [RSW], and Lee–Yang is related to Fibonacci by Galois conjugation there. I have not verified the Galois conjugation separately.

**What these results add.** Theorem 9.14 places Ramanujan's order-7 mock theta functions, and with them the Ẑ invariant of −Σ(2,3,7), inside the modular representation of the (2,7) minimal model. After conjugation and a twist by the character of η³, their shadow transforms exactly as the M(2,7) characters. I have not checked whether this isomorphism is stated in the literature. The classical relation of this kind for order 5 is the mock theta conjectures, which express the order-5 functions through the Rogers–Ramanujan functions, the characters of M(2,5) [AG, Hi]. Proposition 9.15 shows that for order 5 the shadow's own modular data are the Fibonacci data, a Galois companion of Lee–Yang.

The two results together suggest a pattern for the Brieskorn spheres Σ(2,3,q): the shadow representation of the associated mock vector is a twisted minimal-model representation or one of its Galois conjugates. The pattern can be tested on further q with the same scripts (Question 9). For the Erdős–Straus side, the notes' map from the cubic middle to the three support labels is the link that would carry this structure over. That map is stated in the note's Theorem *Coordinate realization of middle support* and is not verified here.

### 9.6 Further verified structural facts

Three further structural statements of the notes were checked by program in reading passes, and one (the involution count) again here.
- **The Niemeier lattice.** The Niemeier lattice with root system A₅⁴D₄ and glue of order 72 appears in the notes and as archive Theorem 25.8 [CS]. Its umbral group, the automorphism group of the glue code, is GL₂(3) [CDH]. GL₂(3) has 13 involutions, while the binary octahedral group has exactly one element of order 2, so the two groups are distinguished.
- **Γ₀(6) and the class 6B.** T₆ = η(τ)⁵η(3τ)/(η(2τ)η(6τ)⁵) is a Hauptmodul of Γ₀(6), and T₆ + 5 + 72/T₆ is the McKay–Thompson series of the Monster class 6B [CN].
- **Collatz.** The Collatz remark 9.8 is classical in its ingredients [La].

## 10. The (3,4,∞) monodromy covers

A package of the workbench (ES-09) uses the integral monodromy of the S⁶ period system [A] to build covers of the projective line branched at three points. Its generators are matrices A₁, A₂, A_∞ with A₁³ = A₂⁴ = A₁A₂A_∞ = I, acting on the affine hyperplane H_D of (ℤ/D)⁴. It proves that the equation fails at p if and only if a denominator-labelled cover has no section. This is Theorem 2.1 in cover-theoretic form: a section exists exactly when R_a/gcd(R_a, 4u + 1) or R_a/gcd(R_a, u + a) equals 1.

For odd D, the package's orbit and genus statements are correct:
- transitive when 3 ∤ D, of genus (5D³ − 12D² − 17D + 24)/24;
- when 3 | D, two orbits of sizes D³/9 and 8D³/9, with genera (5D³ − 12D² − 81D + 216)/216 and (5D³ − 12D² − 9D + 27)/27.

The following theorem, which is new, determines the orbits at every level. It is proved in the companion paper on the S⁶ monodromy (Theorem 6.1 there).

**Theorem 10.1.** Write λ = γ̂ + bû + cŵ + dδ̂ ∈ H_D and e = gcd(D, 6). The orbits of the monodromy group on H_D are the sets {gcd(b, c, e) = g} for g | e, of size D³·#{v ∈ (ℤ/e)² : content g}/e². They coincide with the orbits of the full stabilizer of γ.

**Corollary 10.2.** For D = 2ᵏ there are two orbits, of sizes D³/4 and 3D³/4, for every k. For 6 | D there are four orbits, for example of sizes 48, 144, 384 and 1152 at D = 12. In general the orbit decomposition at D = 2ᵏm with m odd is the product of those at 2ᵏ and at m.

This settles the even-level behaviour, which had been computed for k ≤ 5. At those levels the component genera are (0, 0), (1, 3), (17, 53), (177, 537) and (1569, 4721). The cover-theoretic form of the equation connects the Erdős–Straus problem to the arithmetic of the S⁶ monodromy group, and Theorem 10.1 reduces the orbit side of that connection to the invariant gcd(b, c, gcd(D, 6)). The genera at all levels are Question 8.

---

# Part B. Proved negative results

## 11. Exact limits of specific mechanisms

The workbench proposed a number of transport and certificate mechanisms, and several of them have exact limits. The table records each limit together with its witness. Every witness prime is itself solvable, so these results limit the mechanisms, not the conjecture. They tell later work which mechanism needs which additional input, and where a mechanism is sharp they say so.

| Mechanism | Exact statement | Witness |
|---|---|---|
| bounded transport | not every occupied shell has a solution with unary layer A ≤ 2 | p = 37, a = 12 |
| first-two-shell sieve | occupancy of R = 7 need not give a first-two-layer hit | p = 373, a = 95 |
| canonical closed components (continuation item 2) | a closed component need not contain a local hit | a 7-cycle sink at p = 2521 |
| strict canonical descent (item 3) | descent can close without a hit | a triangle at the 22-digit prime 7510085481569082811681 (prime by a Pocklington chain) |
| principal-character term (item 6) | alone it cannot give positivity: summed over shells it is at most −(1/24)p log p for p ≥ 2²⁰ | exact inequality |
| same-grade middle repair (item 14) | fails from exterior states with α = −4t, t ≥ 4 | p = 7840561 |
| same-word returns (item 21) | exist exactly for the nine words u \| 36 | exhaustive below 2600 |
| trace-to-solution maps (item 26) | cannot avoid increasing a | p = 67369 |
| deficit-box conclusions (§5) | need strict recordness: at the boundary example D − D = ℤ/29 and the two sheets miss 8 points | p = 806,521 |
| the two-shear theorem | holds exactly for p ≢ 2 (mod 3) among congruence conditions | p = 131, 1613 |
| residue carriers | cannot force square rows | Corollary 6.4 |
| Jacobi-symbol barrier | the converse fails | p = 5, R = 7, a = 3 (archive Proposition 10.10) |
| one-congruence criterion | needs p² ∤ R | p = 73, R = 7·73² (Proposition 9.11) |
| shell count as a class function | A₁₁(pa), a = (p+11)/4, is not a function of p mod 840 | on p ≡ 1 (mod 840) it takes 0 at 2521, 4 at 5881, 6 at 4201, 8 at 15121, 10 at 13441 |
| Star–Kneser forcing | a per-shell sufficient condition; the converse fails | p*, R = 107 (archive Proposition 15.7) |

The last row but one has a consequence for the notes' decompositions over the six hard classes. Such a decomposition of the shell count needs data finer than the class of p modulo 840, for instance the factorization of (p+R)/4.

Several continuation items also give positive statements:
- **Item 7:** middle states are localized at a ≤ 3(p+3)/11, and exterior states are localized at the hard primes.
- **Item 14:** for finite templates there is a sharp bound h′ ≤ t² − 3t + 1, with equality in one parametrized family.
- **Item 22:** for every solution at p ≡ 1 (mod 12), an explicit symmetric polynomial of degree 8 is below −480.17 p⁸. The certificate is a finite polynomial positivity certificate.
- **Item 4:** at every hard prime, factoring at most 25 numbers (p + σqt²)/4 yields at least six distinct non-residue primes. This rests on the workbench's enumeration of 1,381,117,764 profiles.

---

# Part C. The directions explored

## 12. Directions, what is established, and my assessment

The research behind this record explored many directions quickly, using AI systems to test each hypothesis as it was formulated. This part describes those directions.

It does not claim that any of them is a complete research programme. It does not treat a direction that is still incomplete as invalid: much of mathematics consists of programmes that are incomplete and are nevertheless valid mathematics. The audit did not have the compute to examine every direction to the depth needed to decide how promising it is. What it can do is state three things for each direction:
- what has been established, with references to Parts A and B;
- what has not been verified here;
- my assessment of the direction.

The assessment addresses two separate questions. The first is the direction's interest on its own merit, for example as a bridge between two areas. The second is its bearing on the Erdős–Straus problem. When a direction relates the equation to a structure that does not take primes as input, the relevant question is what typed map connects the two, and how far that map is established. The assessments are mine and are marked as such. They are views held at this stage, somewhere between opinion and fact, and they may change as the directions are explored further.

### 12.1 The split-zero support language

The notes describe shells, classes and certificates through the split-zero semiring G(R) = R ⊔ {τ}. In it, τ is an additive identity distinct from the ring zero 0_R, and τ absorbs multiplication. *A split-zero repair dossier* develops the algebra of G(R): ideals, prime ideals, spectrum, congruences, localization and semimodules. Its classification statements were checked in a reading pass.

One theorem of the dossier needs an additional relation, and the correction is in keeping with the construction's own convention of keeping τ and 0_R apart.

**Proposition 12.1 (the dossier's Theorem 7.2, with its relation).** Let S = G(R), let M_S be its multiplicative monoid, and let ℛ be the congruence on the free commutative semiring ℕ[M_S] generated by [a] + [b] ∼ [a + b] (a, b ∈ R) and [x] + [τ] ∼ [x] (x ∈ S).
1. The class of the empty sum 0 in ℕ[M_S]/ℛ is {0}.
2. The natural map Θ̄ : ℕ[M_S]/ℛ → S sends both 0 and [τ] to τ, so it is not injective.
3. After adjoining the relation [τ] ∼ 0, Θ̄ is an isomorphism.

*Proof.* Every generating relation relates two non-empty formal sums. Adding a sum, or multiplying by a non-zero sum, preserves non-emptiness, and multiplying by 0 gives 0 ∼ 0; so no chain of relations connects 0 to a non-empty sum, which proves (1). A semiring homomorphism sends 0 to 0_S = τ, and Θ̄([τ]) = τ, which proves (2). With [τ] ∼ 0, the reduction in the dossier's proof applies to every class, including the empty sum, and yields unique representatives [τ] and [r] (r ∈ R). ∎

The support states also have a typed meaning in the shell arithmetic. For a shell a, the three states τ, 0 and + correspond to three situations: the target −1 or −4 lies outside the group H_a (the barriers of §4 apply); the target lies inside H_a but no divisor of a² reaches it; or the shell is occupied. Proposition 4.3 then says that under the exponent condition the middle state 0 does not occur.

My assessment: I think this vocabulary is useful for the problem, because it separates the two different reasons a shell can be empty. They are a group-theoretic reason, handled by the barriers, and a size reason, in which the exponents are too small to reach a target inside the group, and they call for different tools. The algebra of G(R) developed in the dossier is also an object of independent interest.

### 12.2 Mock and quantum modularity

What is established is in §9.5:
- the notes' explicit mixed mock functions are Ramanujan's order-7 mock theta functions, and the first is q^{1/2}Ẑ₀(−Σ(2,3,7));
- their shadow carries the M(2,7) representation after conjugation and the η³ twist (Theorem 9.14);
- the order-5 block carries the Fibonacci data (Proposition 9.15).

Not verified here: the note's support isomorphism from the cubic middle of the shell problem to the three support labels, its mass-gap coordinate for the cubic middle, and its Virasoro support-gap corollary.

My assessment: on its own merit, I think this is the most developed of the structural directions. It has already produced a result, Theorem 9.14, that stands independently of the Erdős–Straus problem and connects Ramanujan's order-7 functions, the 3-manifold invariant of −Σ(2,3,7) and the (2,7) minimal model.

For its bearing on the equation, the needed typed map runs from shell data, which depend on p through the factorization of (p+R)/4, to the modular object. The notes' map goes through the finite support labels. The one analytic object in the notes whose coefficients depend on that factorization is the pair-count series of Proposition 9.13. A typed map between the pair-count series and the mock vector would carry information in both directions, and constructing one is Question 10.

### 12.3 Moonshine, Niemeier lattices and Ogg's primes

**Established** (§9.6): the Niemeier lattice with root system A₅⁴D₄, the umbral group GL₂(3), the Γ₀(6) Hauptmodul and the class 6B series. The constructive-algebra preprint also connects the extension prime 29 with the Heegner discriminant 163. The factorization it uses is classical and correct: j((1 + √−163)/2) = −640320³ with 640320 = 2⁶·3·5·23·29. By contrast, 5280 = 2⁵·3·5·11 for discriminant 67.

**Not verified here:** the preprint's rank-15 Ogg module, its genus-zero and supersingular realizations, and its phase decomposition, apart from the map treated next.

**Proposition 12.3 (the torsor map).** The map Θ : (ℤ/18)^× → S₈₄₀ of *Terminal residual coordinates* §10, given by 1 ↦ 1, 5 ↦ 289, 13 ↦ 361, 17 ↦ 169, 7 ↦ 121, 11 ↦ 529, is a bijection but not a homomorphism: 289² ≡ 361 (mod 840), while 5² ≡ 7 (mod 18) and Θ(7) = 121. The map 5ᵏ ↦ 289ᵏ is an isomorphism and differs from Θ exactly by exchanging the images of 7 and 13.

The note's odd Ogg phase decomposition (its Theorem 10.1) uses only that Θ is a bijection, so it holds as stated. With the isomorphism in place of Θ, the sectors V₁₂₁ and V₃₆₁ exchange their contents, becoming K₅e₁₃ ⊕ K₅e₃₁ and K₅e₇.

My assessment: the moonshine data organize the residue layer of the problem, meaning the six hard classes and the group of order 990 of the reduced core, in a way that matches known structures: the umbral group of A₅⁴D₄, the Γ₀(6) Hauptmodul and Ogg's primes. I think this match is of independent interest as an observation.

Its bearing on the hard classes depends on the typed map that is used. Proposition 6.3 applies to any certificates that depend only on the residue of p modulo a fixed modulus: such certificates cannot reach the square classes. For this direction to constrain the hard primes, the moonshine data would have to be combined with a map that reads the factorization of (p+R)/4. I have not seen such a map in the notes, and I do not have a view yet on whether one exists.

### 12.4 Lorentzian and Apollonian geometry

The Descartes form F(x) = 2Σxᵢ² − (Σxᵢ)² has signature (3,1). The Apollonian group is a subgroup of O_F(ℤ) of infinite index that is Zariski dense in O_F, a thin group, and it acts on hyperbolic 3-space [SaL, GLMWY]. The notes identify a Lorentz form of their shell geometry with the Descartes form. The same Lorentzian geometry of circle configurations underlies Kocik's circle-geometric reading of the Koide relation [Ko].

The note *Lorentzian fixed fibers, Descartes sheets, and origin-resolved positivity in residual Erdős–Straus shells* (section *Finite-dimensional modular flow as a Lorentz boost*) states that the congruence action X ↦ A_ρXA_ρ, with A_ρ = diag(e^{ρ/2}, e^{−ρ/2}), is a Lorentz boost on Hermitian 2×2 matrices with the form det. This is correct. The relation between this boost and the modular flow in the section title is the following.

**Proposition 12.4 (modular flow and boost).** Let H_r = diag(e^r, e^{−r}) and X = [[h + w, u + iv], [u − iv, h − w]], with Minkowski form det X = h² − u² − v² − w². For z ∈ ℂ, the map X ↦ H_r^z X H_r^{z̄} lies in SO⁺(1,3).
1. At z = it it is the modular automorphism σ_t = Ad(H_r^{it}) of the state φ_{H_r}. It acts as the rotation by the angle 2rt in the (u, v)-plane and fixes h and w.
2. At real z = s it is the boost of rapidity 2rs in the (h, w)-plane and fixes u and v. The note's A_ρ is the case s = ρ/(2r).

So the modular flow and the note's boost are the compact and the non-compact real forms of one complex one-parameter subgroup z ↦ H_r^z of SL₂(ℂ), acting on Minkowski space by X ↦ gXg*.

*Proof.* det H_r^z = 1 and (H_r^z)* = H_r^{z̄}, so the map is the standard action of SL₂(ℂ) on Hermitian matrices. The coordinate formulas follow by direct computation: they give (h, u cos 2rt − v sin 2rt, u sin 2rt + v cos 2rt, w) at z = it, and (h cosh 2rs + w sinh 2rs, u, v, w cosh 2rs + h sinh 2rs) at z = s. ∎

My assessment: on its own merit, I think the Descartes setting is a natural place to ask how such Lorentz one-parameter families interact with the Apollonian thin group. One can ask which one-parameter subgroups of O_F(ℝ), rotations or boosts, meet the Apollonian group in lattices, and what their orbits look like on integral packings (Question 11). This is a question about thin groups in its own right.

For the bearing on the equation, the notes' map from shell data to Descartes quadruples is not verified here. I have not identified a typed map from shell occupancy to the Apollonian group, and I have no view yet on whether one exists.

### 12.5 The terminal papers and the statement of the conjecture

The preprint *Constructive Algebra of the Centered Erdős–Straus Resolution* (in BEAVERSHINE) states the conjecture as its Theorems 15.1–15.3. The proof runs through its Lemma 13.4 and a reduction of the primes p ≡ 1 (mod 24) to the terminal core. Three facts about these steps are established here; they concern the proof, and the statements of Theorems 15.1–15.3 are the conjecture itself, which remains open.

1. **The involution in Lemma 13.4 does not exist.** The proof of Lemma 13.4 uses an involution exchanging the exterior pieces P₋ and P₊, "induced by the centered relation u − 14 = −(q − 15)". By the preprint's own five-piece resolution theorem, the supports have |𝒞₋| = 30,240 and |𝒞₊| = 37,800 points, and after the deletion factor R₂₉ they have 29,850 and 37,380. No bijection carries one support onto the other, so the proof of Lemma 13.4 is invalid as written.
2. **The reduction to the core does not follow from the results it rests on.** The proof of Theorem 15.2 states that the finite central-cover construction reduces the primes p ≡ 1 (mod 24) to the terminal core of 2970 classes. What the central-cover computation establishes is Theorem 9.2: the classes with no certificate on any lift form the core, and 550 further classes have certified lifts but are covered by no single identity; the prime 3361 lies in one of them. That every prime in these 550 classes is certified is Question 4, which is open, and the preprint gives no argument for it.
3. **The removal step in Lemma 13.4 is asserted without proof.** The proof states that a point with both endpoints in {τ, 0} "would have been removed by the factor defining the unresolved projector". The unresolved projector 𝒪 = ∏(1 − e_μ)∏_{b∈𝔅}(1 − b) removes exactly the points covered by some lock e_μ or some certificate b ∈ 𝔅, so the statement says that every such point is covered by a certificate. The proof gives no argument for this, and it is the content of Theorem 15.1.

Consequently the proofs of Theorems 15.1–15.3, which depend on Lemma 13.4 and on the reduction to the core, are incomplete. These facts concern §§13–15 of the preprint; its arithmetic results that were verified are stated in §9, and the rest are not verified here. I found no statement of the conjecture as a theorem in the author's June replacement, *Finite support algebra, cubic middle geometry, and orientation descent*.

### 12.6 Additive combinatorics: Kneser's theorem

The notes apply Kneser's theorem on sumsets in abelian groups [Kn] to the residues of divisors, producing Star–Kneser forcing: a per-shell sufficient condition for occupancy (archive Theorems 15.6 and 20.7). It is correct as a sufficient condition; its converse fails at p*, R = 107, as the archive records (Proposition 15.7). The notes cite Kneser's theorem as of 1953; the finite-group theorem is Kneser, *Math. Z.* 61 (1955).

My assessment: I think additive combinatorics is a natural toolset for the size reason of §12.1, where the target lies in H_a but may not be reached, because sumset growth is exactly what decides whether the divisors of a² fill H_a.

### 12.7 Computability: the Busy-Beaver notes

The statement "4/n = 1/x + 1/y + 1/z is solvable for every n ≥ 2" is Π₁. Each instance is decided by a bounded search, since x ≤ 3n/4 and then y is bounded and z is determined. So there is a Turing machine that halts if and only if the conjecture fails, and if it has k states, the value BB(k) decides the conjecture. This is the standard bridge between Π₁ statements and the Busy-Beaver function; such machines have been constructed explicitly for Goldbach's conjecture and for the Riemann hypothesis [Aa].

The notes also propose a pattern in residues modulo 107, the residual of p*. A test in an earlier reading pass compared these residues with a null model fixed in advance and found their frequencies within it (held-out p = 0.38). I have not re-run that test. It concerns that one proposed pattern only.

The Π₁ bridge is exact. The least number of states of a machine that halts exactly when the conjecture fails is a well-posed target (Question 12).

### 12.8 Further directions in the same collections

The collections also contain notes on Cayley–Dickson algebras and sedenion zero divisors, on the Koide relation, on a mass gap, on anomalies, and a split-zero zeta note. The Cayley–Dickson statements were checked in a reading pass in the conventions stated there [Mor, Ba]. The Koide, mass-gap and anomaly notes lie outside the scope of this record and were not read for it. Nothing here assesses them.

---

## 13. Questions

1. **The global statement.** Show that every hard prime has an occupied shell. By §4, a proof must produce, for some R, a shell whose group H_a contains −1 or −4.
2. **Type II universality.** Does every prime p ≡ 1 (mod 24) have a Type II solution? A positive answer proves the conjecture. Below 10⁸ every such prime has one, in a shell R ≤ 107.
3. **The quadratic-residue survivors.** Are there infinitely many primes satisfying every condition of §9.2? They have density zero (Proposition 9.7). A negative answer proves the conjecture outside a finite set.
4. **The 550 supported classes.** Is each of the 550 supported classes of Theorem 9.2 covered by finitely many single identities at some finite level?
5. **The census.** Can the non-square survivor rows of the census all be forced by carriers of the same kind? Which carriers that use the factorization of (p+R)/4 force the square rows?
6. **Records.** The deficit-box conjecture needs a strict record above 8,803,369, and there is none below 3·10⁹. Is h unbounded on the primes?
7. **Shear paths.** What is the exact relative density of the shear-path primes among p ≡ 2 (mod 3)? It lies in [1/24, 0.335].
8. **Genera of the monodromy covers.** What are the genera of the components of the (3,4,∞) covers at every level? Theorem 10.1 gives the orbits, and the genera follow from the cycle counts of A₁, A₂, A_∞ on each orbit.
9. **Brieskorn spheres Σ(2,3,q).** For which q does the shadow representation of the associated mock vector coincide, after conjugation and a twist, with a minimal-model representation (as for q = 7, Theorem 9.14) or with a Galois conjugate of one (as for q = 5, Proposition 9.15)?
10. **A modular object for the shell counts.** Is there a modular, mock or quantum modular object whose coefficients are the shell counts 2|E_a| + |M_a|, or a typed map from the pair-count series of Proposition 9.13 to the mock vector of §9.5?
11. **Modular flows and the thin group.** Which one-parameter subgroups of O_F(ℝ), rotations or boosts as in Proposition 12.4, meet the Apollonian group in lattices, and what do their orbits look like on integral packings?
12. **The least Π₁ machine.** What is the least number of states of a Turing machine that halts if and only if the conjecture fails?

## 14. Verification

Every finite statement of Part A and Part B was computed by programs independent of the sources. The programs are in the record's `checks/es/` folder, with their outputs:
- **The shell criterion, the first two shells, the barriers and the lemmas:** `esr_lemma_checks.py`, `esr_referee_checks.py`, `barrier_primeR.py`.
- **The records to 3·10⁹:** two independent segmented programs, `hsegment.c` and `hsegment_A.c`.
- **Other §§5–7 checks:** the deficit sets (`esr_deficits.py`), the families by symbolic expansion (`esr_families.py`), and the shear graph by complete enumeration below 10⁷ (`esr_twoshears.py`, `shears_density_bound.py`).
- **The census consistency and the method-level witnesses of §11:** `check_items_arith.py`, `referee_checks_es.py`, `r23_es.py`, `r23_item26.py`, with the Pocklington chain in `r12b_pocklington_chain.py`.
- **The terminal core and the sieve of §9.2:** `es50_support_core.py` (calibrated against Salez's count), `es50_survivors.py` and `es50_checks.py` (the 780,700 certificates below 10⁷, all valid).
- **Theorem 9.14 and Proposition 9.15:** `exact_shadow_reps.py`, which verifies exactly in ℚ(ζ₁₆₈) and ℚ(ζ₁₂₀), and `m7_vs_M27.py` and `m5_vs_M25.py`, which reproduce the S-matrices numerically from the q-series to 38 digits.
- **The explicit statements of Part C and the certificates at p*:** `misc_checks.py` covers the shell counts A₁₁(pa) at p ≡ 1 (mod 840), the involutions of GL₂(3), and the coordinate forms of Proposition 12.4. The certificates of p* were computed by factoring the shifted forms.
- **The orbits of §10, up to D = 24:** `es09_even_levels.py` and the S⁶ monodromy checks.

The statements on lattices, modular data and Cayley–Dickson algebras in §§9.6 and 12.8 were checked by program in reading passes. The mock theta identification through q⁴⁰ was checked there as well. The remaining statements of the notes that this record mentions without a status of verified are marked "not verified here" at the place where they occur.

## References

- [A] A compact complex threefold fibred by tori over the projective line, and the six-sphere, manuscript circulated by L. Alpöge, 2026.
- [Aa] S. Aaronson, The Busy Beaver frontier, SIGACT News 51 (2020), no. 3, 32–54.
- [AG] G. E. Andrews, F. G. Garvan, Ramanujan's "lost" notebook VI: the mock theta conjectures, Adv. Math. 73 (1989) 242–255.
- [Ba] J. C. Baez, The octonions, Bull. Amer. Math. Soc. 39 (2002) 145–205.
- [CCFGH] M. C. N. Cheng, S. Chun, F. Ferrari, S. Gukov, S. M. Harrison, 3d modularity, J. High Energy Phys. 2019, no. 10, 010.
- [CCKPS] M. C. N. Cheng, I. Coman, P. Kucharski, D. Passaro, G. Sgroi, 3d modularity revisited, arXiv:2403.14920 (2024).
- [CDH] M. C. N. Cheng, J. F. R. Duncan, J. A. Harvey, Umbral moonshine and the Niemeier lattices, Res. Math. Sci. 1 (2014), Art. 3.
- [CFS] M. C. N. Cheng, F. Ferrari, G. Sgroi, Three-manifold quantum invariants and mock theta functions, Phil. Trans. R. Soc. A 378 (2020) 20180439.
- [CN] J. H. Conway, S. P. Norton, Monstrous moonshine, Bull. London Math. Soc. 11 (1979) 308–339.
- [CS] J. H. Conway, N. J. A. Sloane, Sphere Packings, Lattices and Groups, Springer, 3rd ed., 1999, ch. 16–18.
- [ET] C. Elsholtz, T. Tao, Counting the number of solutions to the Erdős–Straus equation on unit fractions, J. Aust. Math. Soc. 94 (2013) 50–105.
- [EZ] M. Eichler, D. Zagier, The Theory of Jacobi Forms, Birkhäuser, 1985.
- [GLMWY] R. L. Graham, J. C. Lagarias, C. L. Mallows, A. R. Wilks, C. H. Yan, Apollonian circle packings: geometry and group theory I. The Apollonian group, Discrete Comput. Geom. 34 (2005) 547–585.
- [Hi] D. Hickerson, A proof of the mock theta conjectures, Invent. Math. 94 (1988) 639–660.
- [IW] E. J. Ionascu, A. Wilson, On the Erdős–Straus conjecture, arXiv:1001.1100.
- [Kn] M. Kneser, Ein Satz über abelsche Gruppen mit Anwendungen auf die Geometrie der Zahlen, Math. Z. 61 (1955) 429–434.
- [Ko] J. Kocik, The Koide lepton mass formula and geometry of circles, arXiv:1201.2067 (2012).
- [La] J. C. Lagarias, The 3x+1 problem and its generalizations, Amer. Math. Monthly 92 (1985) 3–23.
- [Lo] M. A. Lopez, A complete congruence system for the Erdős–Straus conjecture, arXiv:2404.01508.
- [MD] S. Mihnea, D. C. Bogdan, Further verification and empirical evidence for the Erdős–Straus conjecture, arXiv:2509.00128.
- [Mo] L. J. Mordell, Diophantine Equations, Academic Press, 1969.
- [Mor] G. Moreno, The zero divisors of the Cayley–Dickson algebras over the real numbers, Bol. Soc. Mat. Mexicana (3) 4 (1998) 13–28.
- [RC] A. Rocha-Caridi, Vacuum vector representations of the Virasoro algebra, in: Vertex Operators in Mathematics and Physics, MSRI Publ. 3, Springer, 1985, 451–473.
- [RSW] E. Rowell, R. Stong, Z. Wang, On classification of modular tensor categories, Comm. Math. Phys. 292 (2009) 343–389.
- [Sa] S. E. Salez, The Erdős–Straus conjecture: new modular equations and checking up to N = 10¹⁷, arXiv:1406.6307.
- [SaL] P. Sarnak, Letter to J. Lagarias about integral Apollonian packings, June 2007.
- [Va] R. C. Vaughan, On a problem of Erdős, Straus and Schinzel, Mathematika 17 (1970) 193–198.
- [Za] D. Zagier, Ramanujan's mock theta functions and their applications, Séminaire Bourbaki exp. 986, Astérisque 326 (2009) 143–164.



