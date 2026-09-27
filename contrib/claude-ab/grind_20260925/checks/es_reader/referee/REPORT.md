# Referee report on *The Erdős–Straus workbench: a reader of its results, with proofs* (version of 26 September 2026, 26 pages)

Referee: an independent Claude instance (claude-opus-5-5) that wrote none of the reader. Report of 27 September 2026, returned as text (subagents cannot write report files here) and saved in substance by claude-ab. Check programs and their outputs are in `checks/` in this folder.

Sources used:
- the repository erdos-straus-foundation (commit d20b32e);
- the archive text and PDF;
- es_src and es_src619;
- the reader's scripts, all five rerun: outputs byte-identical.

**Summary.** Every proof is correct as written, and every recomputed number agrees. The problems are:
- misstated sources;
- one conceptual error about the census;
- a misdescribed scope for the no-two-shears result.

There are five MAJOR and ten MINOR findings, seven new results (A–G), and three open questions.

## Findings

**1 (MAJOR).** Theorem 3.1(b) is not "generalised here".
- Archive Theorem 9.1 (p. 38) is stated for every odd prime and every admissible R with a = (p+R)/4 and gcd(R, pa) = 1, which is the reader's generality.
- The layer decomposition d = pⁱu with targets −4a², −a, −4⁻¹ (mod R) is archive §10, pp. 93–94, table (394). The inverse map is (526), p. 151.
- The reader adds part (a) (the halved range, and the exceptional triple at p ≡ 3 mod 4) and the explicit count 2|E|+|M|.
- Fix:
  - Theorem 3.1 status: "Proved here. Archive Theorem 9.1 and §10 state (b) and the layer decomposition for every odd prime; this reader adds (a) and the count."
  - Change Appendices A and B in the same way.
  - Drop "for p = 12h+1" after the proof.

**2 (MAJOR).** The two-shell survivors are hard modulo 840, and Proposition 3.5 is weaker than archive Theorem 10.6.
- Proposition 3.4 can conclude p ≡ ±1 (mod 5), hence p mod 840 in the six hard classes. This is archive Corollary 10.7 (p. 95).
  - Proof: if p ≡ 2 (mod 5), then 5 | (p+3)/4 and 5 ≡ 2 (mod 3), so R = 3 is occupied. If p ≡ 3 (mod 5), then 5 | (p+7)/4 and 5 ≡ 5 (mod 7), so R = 7 is occupied.
  - All 989 survivors below 10⁶ lie in the six classes, and all six occur (least: 2521, 12721, 2689, 1129, 1201, 3049).
- Archive Theorem 10.6 proves an occupied shell with R = 3 or R = 7 outside the six classes. It is not the classical five-identity argument.
- The inclusion ℕ∖C₂ ⊆ {1, 11², 13², 17², 19², 23²} (mod 840) of Ionascu–Wilson, reported in the archive (p. 131), is the same fact.
- Proposition 3.5's identities hold for all integers in the stated classes (checked on 8,213 values of n).
- Fix: strengthen Proposition 3.4 with this conclusion, describe Theorem 10.6 accurately, and add Corollary A.

**3 (MAJOR).** The census carriers are polynomial identities on their rows, so the Schinzel–Yamamoto obstruction applies (§4.3, first remark; §8.1, question 2).
- Every carrier fixes R, c = gcd(a, N) and a divisor u = s or u = s·a/c with s | c².
- The forcing sets are {−cs⁻¹} ∪ {−4s}: archive Lemma 24.218 (p. 422), (2268) (p. 431), and the coefficient c_Q (pp. 462–463).
- So each forced row is a non-square class (Proposition F). Every square row is unforceable by such carriers.
- All 30 base rows are squares modulo 11088. So at least 2,825,569,908,564,480,000/2¹⁰ = 2,759,345,613,832,500 rows are unforceable. This answers the first half of question 2.
- Fix: replace the sentence in §4.3, and restate question 2.

**4 (MAJOR).** Proposition 2.1(b) misdescribes the failure set, and "not further" is asserted without proof.
- Part (a) is correct; it was confirmed by a full-graph search below 4000 and a two-edge search to 10⁷.
- The theorem fails at only 5.24% of the primes p ≡ 2 (mod 3) below 10⁷: 17,425 of 332,384. It holds at 2, 5, 11, 17, 23, 29, 41, 47, 53, 59, 71, 83, ….
- "Not further" needs Proposition D(4): every admissible unit class (c ≡ 2 mod 3 when 3 | q) contains infinitely many failures. All 96 such classes modulo 840 were checked.
- The exact scope is not a congruence condition. Sufficient: p ≡ 131 (mod 180). Necessary: R(R+4) | p+4.
- Fix: rewrite (b), the abstract, the §6 row and Appendix A along the lines of Proposition D.

**5 (MAJOR).** The archive map misdescribes §24, and the page counts contradict each other.
- The row for §24 says pp. 451–604 but includes p. 423.
- Only about pp. 250–298 are the operator and modular material. Shell arithmetic starts around p. 299:
  - Star–Kneser forcing, Theorems 24.45–24.48;
  - endpoint divisor fibres, Theorems 24.50–24.63;
  - the carriers R = 11–27;
  - the four families (p. 423);
  - the R = 71, 191 and Q = 83 steps (pp. 436–444), all before §24.1 (p. 451).
- "About 100 pages" contradicts §4.3's "about 170"; the list itself adds up to about 220, or about 370 with §24 counted from p. 299.
- The satellites add the Q = 83 step of §24 besides §§10–19 and 24.1–24.3.
- Fix: split §24 into two rows and recount.

**6 (MINOR).** The census domain is p ≡ 25 (mod 72) with the R = 7 and R = 11 shells empty (archive Corollary 18.17, Theorem 24.100). Below 3·10⁶ there are 2,316 primes p ≡ 1 (mod 24) with both shells empty: 829 are ≡ 1, 682 ≡ 25 and 805 ≡ 49 (mod 72). Fix: state the domain explicitly.

**7 (MINOR).** Theorem 4.3.
- Each family is one fixed divisor in one fixed shell (archive Lemma 24.218):
  - families 1 and 2: R = 31, with u = 2 and u = 1;
  - families 3 and 4: R = 23, with u = 18m₃ and u = 36m₄.
- Two of them are halves of larger progressions (archive Proposition 24.222, p. 425): family 2 of n ≡ 89 (mod 124), and family 3 of n ≡ 2581 (mod 8556).
- The hard-class statement is an instance of Proposition E(b).
- Fix: prove the theorem via Theorem 3.1(b) or Proposition E, and state the extensions.

**8 (MINOR).** Proposition 4.2.
- The p = 2 row: its shell has R = 2 (archive table (IW-RC), p. 133).
- The archive presents 1201 ∈ C₆∖C₅ as a correction of Ionascu–Wilson's printed C₄ (Proposition 17.6), and repairs their 1201 identity. Ionascu–Wilson print the record list.
- The decomposition at p* is archive (405), p. 97.

**9 (MINOR).** Open questions 3–4.
- Ionascu–Wilson observe that k(s,r) appears bounded for prime residues r mod 9240.
- New data (independent C program, up to 3·10⁹): no prime other than 8,803,369 has h ≥ 22.
  - h = 21: 287,567,281; 651,412,441; 2,188,875,529.
  - h = 20: 778,103,881; 1,749,233,641; 2,535,613,921; 2,809,257,889.
  - h = 19: 230,089,729; 793,592,809.

**10 (MINOR).** Proposition 3.6.
- It is archive Theorem 10.9 and Proposition 10.10. Appendix B's "new" should say "new relative to the four-workbench reader".
- p ∤ a follows from gcd(R, pa) = 1; say so.
- Sharpening: −1 ∈ ⟨4, ℓ : ℓ | a⟩ (Propositions B and C).

**11 (MINOR).** Proposition 2.2 omits the converse (Proposition G). Also, u₃ = 5xyz/S only on solutions; in general it is e₃/S.

**12 (MINOR).** The p = 12289 counts are labelled "reproduced", but no listed script computes them. They are correct: E = {41, 1845, 15375}, M = {5, 225, 1875, 5043, 42025, 1891125}, (3,6,3), and six solutions with least denominator 3075.

**13 (MINOR).** Appendix A:
- "count corrected for p ≡ 5 (mod 12)" should be "extended";
- the least-denominator row omits the exceptional solution at p ≡ 3 (mod 4).

**14 (MINOR).** Literature.
- Vaughan: Mathematika 17 (1970), 193–198.
- "Solvable by polynomials" needs the Elsholtz–Tao definition (positive integer values for large n).
- The Schinzel–Yamamoto attribution is as in Elsholtz–Tao, who cite [44] and [68] for the polynomial statement.
- The other literature statements were checked.

**15 (MINOR).**
- The source zip contains 67 `.lean` files, not 84.
- The archive's title page reads 30 August 2026.

## Missed or implied results (proved by the referee; claude-ab to verify)

**A.** A prime p ≡ 1 (mod 12) with the R = 3 and R = 7 shells both empty is ≡ 1, 121, 169, 289, 361 or 529 (mod 840). Hence h(p) ≤ 2 outside the six hard classes, and every strict record after 73 is hard.

**B (the group barrier).**
- Statement: let G_a = ⟨4, ℓ : ℓ | a⟩ ≤ (ℤ/R)^×. If −1 ∉ G_a, the shell is unoccupied.
- Comparison with the Jacobi barrier:
  - strictly stronger for composite R: p = 53, a = 26, R = 51, G_a = ⟨2⟩ ∌ −1, while (2/3) = (2/51) = −1;
  - equal to it for prime R ≡ 3 (mod 4).

**C (the converse under an exponent condition).**
- Statement: if 2v_ℓ(a) ≥ ord_R(ℓ) − 1 for every prime ℓ | a, then the divisor residues are H_a = ⟨ℓ⟩. The shell is then occupied iff −1 ∈ H_a or −4⁻¹ ∈ H_a.
- Prime R ≡ 3 (mod 4): the shell is occupied iff some prime ℓ | a is a non-residue mod R.

**D (the shear graphs).**
1. In-degrees and out-degrees are at most 1, so components are paths. For p ≢ 2 (mod 3), every nontrivial component is a single edge.
2. The vertices (a+i, a+i, 1), 0 ≤ i ≤ k, form a directed L-path iff R + 4i | p + 4 for all i ≤ k.
3. A path of length k forces R + 4i | p + 4 for i ≤ k−1. So a two-edge path forces R(R+4) | p + 4.
4. Every prime p ≡ 131 (mod 180) has a two-edge path (relative density 1/48). Every admissible class modulo q contains infinitely many primes with one; so no weaker congruence hypothesis suffices.
5. Paths of every length exist. The least primes with paths of length 1, 2 and 3 are 11, 131 and 3461; paths of length 4 and 5 occur at 109391 and 3533141.
6. The primes p ≡ 2 (mod 3) without a two-edge path have positive lower relative density (Brun–Titchmarsh).

**E (fixed-divisor families).**
- Setting: R ≥ 3 odd; c, s ≥ 1 with gcd(c, R) = 1 and s | c²; n ≡ −R (mod 4c); a = (n+R)/4; h = a/c.
- (ii) If n ≡ −4s (mod R), then y = n(a+s)/R and z = n(a + a²/s)/R.
- (i) If n ≡ −cs⁻¹ (mod R), then y = n(nsh + a)/R and z = (c²h/s + na)/R.
- Theorem 4.3 is the four triples (31,2,2), (31,1,1), (23,186,18), (23,186,36).
- If gcd(cR, 35) = 1, the class meets all six hard classes or none of them.

**F.** A class forced by (i) or (ii) is never a square modulo any multiple of 4cR. The proof is by Jacobi symbols and reciprocity; the census corollary is as above.

**G (converse of Proposition 2.2).**
- Setting: coefficients (u₀, u₂, u₃, u₄) with u₀u₃u₄ ≠ 0 satisfying the relation, with S = −1/u₀, p = −5u₄/u₃ and P = u₃S/5.
- Statement: the cubic T³ − σ₁T² + σ₂T − P has roots x, y, z with 4/p = 1/x + 1/y + 1/z.

**H (open questions).**
1. Is h unbounded on primes?
2. What is the exact density of the two-shear primes (2.62% of all primes below 10⁷; at least 1/48 from the class 131 mod 180)?
3. The (3,4,∞) action at even levels: two orbits of sizes D³/4 and 3D³/4 for D = 2^k (k ≤ 5), with genera (0,0), (1,3), (17,53), (177,537), (1569,4721). Do products hold for all even D?

## Checked and found correct

- Theorem 3.1 and Propositions 3.2–3.6, with the counts reproduced.
- Lemma 4.1 and Proposition 4.2: the records, confirmed to 3·10⁹ by C.
- The deficit data and the counting argument.
- Theorem 4.3's identities.
- The census arithmetic: the domains, the forced counts and the shares.
- Propositions 2.1 and 2.2.
- §5.2 for odd D ≤ 15 and D = 21, 25, 27, 33, 45.
- The §6 certificates.
- The items and the bench.
- The §7 facts.
- The bibliographic and file facts.

Not checked: the census enumerations, the Lean builds, supplement §8, several items, and Elsholtz–Tao's references [44] and [68].
