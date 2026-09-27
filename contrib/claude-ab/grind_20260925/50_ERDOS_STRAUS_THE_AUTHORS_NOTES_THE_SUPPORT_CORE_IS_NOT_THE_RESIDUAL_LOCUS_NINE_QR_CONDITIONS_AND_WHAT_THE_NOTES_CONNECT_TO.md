# The author's Erdős–Straus notes: what they prove, the support-zero core versus the residual locus, nine quadratic-residue conditions on a counterexample, and what the notes connect to

Claude (claude-ab lane), model `claude-opus-5-5` (Opus 5.5) at maximum reasoning effort. 27 September 2026. The reading began at 07:31 UTC and this note was written from 11:27 UTC. An independent Claude instance refereed it, together with the new Section 6 of the Erdős–Straus reader. The referee's verified findings were applied from 12:45 to 12:55 UTC (§13).

**What this note is.** The author asked, before reading the Erdős–Straus reader, whether it had missed results in the author's own notes, and asked for the Erdős–Straus results that follow from those notes and are not yet recorded. This note answers that question.

**The notes read.** The author's unpublished Erdős–Straus notes, April–June 2026, in two collections:
- the *Chatnotes* collection: 20 TeX notes, one 52-page paper available only as PDF, and their scripts and reports;
- the Erdős–Straus part of the *BEAVERSHINE* collection: about 55 TeX notes, including the source note of the "terminal core", and their scripts.

They are cited here by title and theorem number only. The two ChatGPT conversation logs in these collections were not opened. The non-Erdős–Straus parts of BEAVERSHINE are left for later notes: the Koide, "mass gap", anomaly and Cayley–Dickson-algebra notes, and one split-zero zeta note.

**How the reading was done.**
- Six independent passes (A1, B1, C, D, E, F) were each run by a separate Claude instance of the same model. Each read its assigned files in full, tabulated every numbered statement, ran the notes' own scripts, and wrote check programs.
- Their reports remain on the working machine. Where a statement below rests only on one of those passes, it says so.
- claude-ab read the source of the terminal core in full, re-ran the author's own scripts, and re-derived every result proved in §§2–7. It re-checked those results with its own programs, which are listed in §12. Statements that rest only on a reading pass or on the referee say so.
- The author's folder of drafts labelled as overstating results (`mock/trash`, the contents of the archive "drafts which overstated results for the record") was not opened.

Nothing here bears on the truth of RH. τ is not identified with any zero, point or number.

## 0. Summary

1. **The Erdős–Straus arithmetic in the notes is mostly recorded or classical.** It consists of:
   - the shell calculus, already in the reader and the 619-page archive;
   - the classical identity families of Mordell, Rosati, Yamamoto, Elsholtz–Tao, Salez and Lopez.

   The structural layers are correct where checked:
   - the Niemeier lattice A₅⁴D₄ with glue group GL₂(3);
   - the Γ₀(6) Hauptmodul and the Monster class 6B;
   - Ogg's primes;
   - Lorentz and Apollonian geometry;
   - Cayley–Dickson algebras;
   - the split-zero semiring.

   None of these takes a prime, a shell or a certificate as input, so none constrains which primes are solvable. Most of the notes say so themselves (§9).
2. **The terminal core is a support statement, not a covering statement (§2).**
   - The source note, "Finite Central-Cover Reductions for Residual Erdős–Straus Shells", proves that S₈₄₀ × Q₁₁ × Q₁₉ × Q₂₃ (2970 classes modulo M₂₃ = 840·11·19·23) is the *support-zero* core of the P-smooth elementary certificates. It says so, and bounds a residue from below.
   - This is reproduced here by an independent program, and one direction is proved by the Jacobi symbol (Theorem 50.1).
   - The later notes treat this core as the residual locus: the 52-page "Terminal residual coordinates" (26 May) and the June replacement.
   - At level M₂₃ the classes that no single identity of Salez's seven families (with modulus dividing M₂₃) covers number **3520 = 2970 + 550**. The computation is calibrated to Salez's published count. The 550 non-square classes are supported but not covered. The prime 3361 lies in one of them.
3. **Nine quadratic-residue conditions on a counterexample (§3).**
   - A counterexample p ≡ 1 (mod 24) is a quadratic residue modulo every odd prime factor of (p+1)(p+2)(p+3)(p+4)(p+7)(p+8)(2p+1)(3p+1) (Theorem 50.4). On the hard classes 121, 169, 289, 529 (mod 840) the same holds for p+5 (Theorem 50.5).
   - The conditions from p+2, 2p+1 and p+5, and the explicit p+8 condition, are not stated in the archive, the reader, `43_` or `43a_`; no literature search was made. Each shift row is the union, over its free divisor, of one of Salez's charts with small constants.
   - The strict record prime p* = 8,803,369, whose least occupied shell is 107, is certified by p+2 and by 2p+1 and by none of the recorded shifts.
   - A general "visible-box" principle adds prime shells R = 31, 47, 59, 71, 311 on explicit classes (Theorem 50.6), and there is a µ = 17 lock condition (Proposition 50.7).
   - Of the primes p ≡ 1 (mod 24) below 10⁷, 247 survive the eight shifts and 31 survive all of these conditions.
   - The referee found eight more conditions of the same kind on parts of the hard classes: p+6, p+12, p+16, p+20, p+24, p+36, 5p+1, 6p+1. With them 23 primes survive below 10⁷ (§3.5).
4. **Barriers (§4).** The notes' width-one barrier is strictly sharper than the group barrier stated in the reader (Proposition 50.8). Example: (p, R) = (433, 91). The two coincide whenever every prime factor of R is ≡ 3 (mod 4).
5. **Shell facts (§5):**
   - Non-coprime shells: the unreduced one-congruence criterion is valid when gcd(R, pa) = p and false when p² | R. Four of the notes state it without the hypothesis. The error is harmless where they use it, since failure needs R ≥ 3p².
   - R | p−1 forces E_a = M_a, and R | p²−1 makes |E_a| odd exactly when R | p+1.
   - The pair-count Dirichlet series is correct.
   - The notes' finite template cover of S₈₄₀ cannot exist as a congruence cover.
6. **Identities (§6).** The two "direct 29-channels" are correct. They are instances of Salez's charts and sit inside Rosati's family n ≡ −c (mod 4k−1), c | k. The notes' "only two direct channels" is an artefact of admitting only single primes from {5, 11, 19, 23}.
7. **Locks and types (§7).**
   - The notes' full-divisor locks are exactly the E- and M-certificates u = a/µ and u = µ²t. Every hard prime below 10⁷ has one. Not every prime has one: 409 ≡ 1 (mod 24), which is not hard, has none.
   - Every prime p ≡ 1 (mod 24) below 10⁷ has a Type II solution in a shell R ≤ 107, and p* is the only one that needs 107.
   - "Complement-square" certificates are not universal: 97 is the least prime p ≡ 1 (mod 24) without one, and 3361 the least hard one.
8. **Errors (§8).** Twelve are listed with counterexamples. The weightiest:
   - the core is used as the residual locus;
   - "Constructive Algebra of the Centered Erdős–Straus Resolution" claims the conjecture. Its key lemma is circular. The author's own June replacement removed a conclusion of the same kind from its predecessor.
9. **Connections (§9).**
   - The "explicit mixed mock functions" of the Virasoro note are exactly Ramanujan's order-7 mock theta functions, in Zagier's vector M₇. The note does not name them.
   - The identification of these functions with the characters of the minimal model M(2,7) fails once the S-matrix is imposed.
   - The notes' Collatz observation is the classical Syracuse predecessor structure. It gives one clean rephrasing: a counterexample p ≡ 1 (mod 24) has odd Collatz successor (3p+1)/4 composed only of primes ≡ 1 (mod 3).

## 1. What was read

| Collection, folder | Notes (title, abbreviated) | Pass | One-line verdict |
|---|---|---|---|
| Chatnotes, `E-S umbrl/` | Split-zero divisor-pair reconstruction; Normalized divisor supports and the pre-Niemeier datum; Defect-completed residual support, pair zeta and umbral A₅⁴D₄; Residual divisor shells … A₅⁴D₄ Niemeier refinement; Residual-umbral completion; Split-zero residual moonshine and the snowflake obstruction | A1 | Erdős–Straus content recorded (archive Thms 9.1, 9.64, 24.50, 24.168–24.172, 25.8); lattice/modular layer correct; errors E1–E5 of §8 |
| Chatnotes, `E-S umbrl/` (the rar archive "Further drafts") | Split-zero residual moonshine; Support-prime moonshine completion; Support-exact moonshine coefficient realization; Split-zero support repair for moonshine proofs; A split-zero repair dossier | D | correct restatements, with one semiring slip and the non-coprime lemma (§8) |
| Chatnotes, `mock/` | Terminal residual coordinates (PDF, 52 pp.); Finite support algebra, cubic middle geometry and orientation descent (June replacement, with diff); Coefficient-orbit packing algebra and quinary S₅ carriers (addendum) | B1 | core used as residual locus (§2); "only two direct channels" is an artefact (§6); the removed conclusion of the superseded draft was circular |
| Chatnotes, `mock/`, `mock/n/` | Lorentzian terminal support; Terminal shell inversion and Lorentz Springbord reflection; Cubic phase coordinates and residue-lift walks; An explicit mixed-mock Virasoro support realization; Noetherian support completion; Wick-completed symmetry envelopes | D | correct and elementary; the mock functions are Ramanujan's order-7 functions; the Virasoro identification fails (§9) |
| BEAVERSHINE, `loq key sm/` | Finite Central-Cover Reductions for Residual Erdős–Straus Shells | claude-ab | correct; a support statement, honestly labelled (§2) |
| BEAVERSHINE, `n-branch/`, `subtori/`, `furthe/`, `7 zline/` | Odd n-line linearization of five-lock visibility; Full divisor locks, QR subtori and survivor idempotents; the 990/29 papers (six drafts); Two-channel reduction; the integrated preprints (four drafts); One-block reduction (two drafts) | C | numbers correct; the µ = 5 lock classification is new and correct; H^sm used as residual locus throughout |
| BEAVERSHINE, top level and `2`–`8`, `5-15`, `14`, `16` | Busy-Beaver residues and the 107-shell (five notes); The A₈ snowflake target star; Total obstruction calculus (two drafts); Corrected interaction calculus; Star–Kneser (three notes); Terminal-core lock covers; Support-complete residual shells … A₈³ positivity; Lorentzian fixed fibers, Descartes sheets | E | Star–Kneser is correct one way; its added converse is false (already retracted in the archive); Busy-Beaver residues are at chance level |
| BEAVERSHINE, `9`–`13`, `15`, `cob=n/`, `rank 15/` | Circular completion and full-branch positivity; Supersignum completion (two notes); Integrated supersignum and blade-one positivity (two copies); Closed forms for residual shell induction; Six-sector ghost notes (five drafts); Constructive algebra of the centered resolution; A rank-fifteen residual-shell algebra | F | algebra correct where checked; the constructive-algebra paper's Erdős–Straus theorem is not proved (§8) |

Every numbered statement was tabulated; passes D, E and F alone list 508, 390 and 744 items. "Residual Erdős–Straus Coordinates, Cubic Middle Geometry, and Finite Support Algebra" (4,482 lines) is a separate document, not the base of the June diff. It was compared with the June replacement by theorem list only.

## 2. The terminal core: support versus covering

### 2.1 Setting

Put M₂₃ = 840·11·19·23 = 4,037,880. A *base class* is a class n ≡ r (mod 840) with r ∈ S₈₄₀ = {1, 121, 169, 289, 361, 529}, taken together with units modulo 11, 19 and 23. There are 6·10·18·22 = 23,760 of them.

The source note defines an *elementary j = 1 certificate* (R, m, u) by:
- R ≡ 3 (mod 4) and u | m²;
- the class conditions n ≡ −R (mod 4m) and n ≡ −4u (mod R), with gcd(n, R) = 1.

Then m divides a = (n+R)/4 and u divides a². The divisor d = nu satisfies d ≡ −na (mod R), so the shell criterion (reader, Theorem shell) gives a solution with x = a. In the reader's notation this is the middle channel M_a. A prime ℓ ∈ {2, 3, 5, 7, 11, 19, 23} is *available* for (R, class) when ℓ ∤ R and n ≡ −R (mod 4ℓ), taken modulo 8 when ℓ = 2.

The source note does two computations:
1. **Divisor-visible sieve.** It uses the 32 shells R | M₂₃ with R ≡ 3 (mod 4). The 23,760 classes fall to **4951**. Each deletion here is a class-level identity, so this is a covering statement.
2. **All-smooth closure.** Here R runs over all P-smooth numbers with R ≡ 3 (mod 4), where P = {3, 5, 7, 11, 19, 23}. The certificate congruence is tested modulo gcd(M₂₃, R). By the note's "lifted target count" lemma, a class is then hit exactly when *some lift* of it modulo lcm(M₂₃, R) is certified. The unhit classes number **2970**, and they are S₈₄₀ × Q₁₁ × Q₁₉ × Q₂₃.

The note calls the second set the "all-M-smooth elementary support-zero core". From it the note derives the lower bound 2970/M₂₃ = 9/12,236 for the residue at s = 1 of the zeta function of any M-smooth elementary obstruction set. It also names the next step: a proof must use data outside the smooth envelope, namely external primes or non-elementary certificates.

### 2.2 The support theorem

**Theorem 50.1.**
- **(a) Support.** A base class admits no P-smooth elementary j = 1 certificate on any lift if and only if it is a square modulo 11, 19 and 23. So the support-zero core is exactly S₈₄₀ × Q₁₁ × Q₁₉ × Q₂₃, with 2970 classes.
- **(b) Covering.** The base classes that are not covered by any single identity among Salez's seven modular equations with modulus dividing M₂₃ number **3520**. They are the 2970 square classes and **550** classes that are non-squares modulo 11, 19 or 23.
- **(c)** Consequently the set of classes left open at level M₂₃ strictly contains the square core. For example:
  - the prime 3361 is ≡ 1 (mod 840) and ≡ 6 (mod 11), a non-residue, so it lies outside the core, yet none of the 64,149 families with modulus dividing M₂₃ covers its class;
  - the same holds for the primes 18,481 and 2,840,041.

  These primes are of course solvable. The shells R = 3, 19 and 7 give 4/3361 = 1/841 + 1/950330 + 1/110139970, and so on (§12).

**Lemma 50.2.** Let (R, m, u) be an elementary j = 1 certificate with gcd(m, R) = 1, and let n satisfy its class conditions. For odd ℓ put ε_ℓ(n) = (n/ℓ). Put ε₂(n) = +1 if n ≡ 1 (mod 8) and −1 if n ≡ 5 (mod 8). Then the Jacobi symbol satisfies

(n/R) = −∏_{ℓ | u} ε_ℓ(n)^{v_ℓ(u)}.

In particular no n in the class is a unit square modulo lcm(4m, R).

*Proof.*
1. From n ≡ −4u (mod R) we get (n/R) = (−1/R)(4/R)(u/R) = −(u/R).
2. Let ℓ be an odd prime dividing m. Since R ≡ 3 (mod 4), reciprocity gives (ℓ/R) = (R/ℓ)(−1)^{(ℓ−1)/2} = (−R/ℓ). This equals (n/ℓ) because n ≡ −R (mod ℓ).
3. If 2 | m, then 8 | 4m and n ≡ −R (mod 8). So (2/R) = +1 exactly when R ≡ 7, that is, when n ≡ 1 (mod 8).
4. Hence (u/R) = ∏ε_ℓ(n)^{v_ℓ(u)}.
5. Suppose n were a unit square modulo lcm(4m, R). Then ε_ℓ(n) = 1 for every ℓ | m, including ℓ = 2 because 8 | 4m. So (n/R) = −1, which is impossible for a square. ∎

*Proof of Theorem 50.1(a), "if".* Let c be a square class and n any lift of it. Then n is a quadratic residue modulo every prime of P, because S₈₄₀ consists of the unit squares modulo 840 and c is a square modulo 11, 19 and 23. It is also ≡ 1 (mod 8).
- For a P-smooth R, (n/R) = ∏_{ℓ | R}(n/ℓ)^{v_ℓ(R)} = +1.
- The available primes all lie in {2} ∪ P, so by Lemma 50.2 every certificate would force (n/R) = −1.

So no lift is certified. This direction does not use Hensel lifting, because the Jacobi symbol only sees n modulo the primes of R.

*Proof of "only if", and of the numbers 4951 and 2970.* This is a finite computation. The author's script reproduces them in 5 min 41 s. So does an independent program written here, `checks/es50/es50_support_core.py`, in 4 s. It finds:
- 32 visible shells and 4951 survivors;
- a semigroup of size 45,139 with 22,074 states ≡ 3 (mod 4), matching the source note;
- 2970 unsupported classes, equal to S₈₄₀ × Q₁₁ × Q₁₉ × Q₂₃.

Lemma 50.2 is also checked exhaustively for R < 120 and m < 60: 12,889 classes, none containing a square (check A1).

*Proof of (b).* A finite computation over Salez's seven modular equations, "The Erdős–Straus conjecture: new modular equations and checking up to N = 10¹⁷" (arXiv:1406.6307, Proposition 3). Salez states that the seven form a complete set: a residue class not equivalent to one of them is not identically solvable. The enumerator is the one written by pass B1, copied unchanged into `checks/es50/salez/`. It checks each identity with explicit denominators.
- **Calibration.** At Salez's modulus G₇ = 840·11·13·17·19·23 = 892,371,480 it leaves **147,348** classes. That is Salez's published number, confirmed from the paper.
- **At M₂₃.** 64,149 families have modulus dividing M₂₃, and 3520 base classes remain: 2970 square and 550 non-square.

`checks/es50/salez/salez_M23_and_G7.py` reproduces both numbers in 2 min.

### 2.3 What this changes

The source note is correct and says what it proves. The later papers do not keep the distinction:
- The introduction of "Terminal residual coordinates" says the central-cover reduction "gives the terminal smooth core". Its later sections treat H^sm as the unresolved set.
- The opening diagram of the June replacement sends a hard prime p ≡ 1 (mod 24) to H^sm.
- The BEAVERSHINE integrated preprints do the same (pass C lists where).

At level M₂₃ the residual locus is the 3520-class set. In the vocabulary of the author's split-zero semiring, used here only as an analogy:
- The 2970 core classes are **unsupported** (τ) for every P-smooth elementary certificate.
- The 550 non-square classes are **supported but uncovered**. Some lift of each is certified, but no identity of Salez's seven families is valid on the whole class at level M₂₃. They play the role of supported zeros at that level.

Salez's completeness statement concerns identity families of his linear type. The archive's audit of Salez (§13.2) records that scope.

**Densities.** By Dirichlet's theorem the primes in the core have density 2970/φ(M₂₃) = 2970/760,320 = **1/256** among all primes. The primes left open at level M₂₃ have density 3520/760,320 = **1/216**. At Salez's level the open set has density 147,348/145,981,440, about 1/990.7, of which the square classes contribute 142,560/145,981,440 = 1/1024. The split 142,560 = 6·5·6·8·9·11 counts the square classes, which no identity covers (§5.4), and 147,348 − 142,560 = 4788 is the number of non-square classes.

## 3. Quadratic-residue conditions on a counterexample

Throughout, p ≡ 1 (mod 24) is prime. "Certificate" means a shell R ≡ 3 (mod 4) with a = (p+R)/4, gcd(R, pa) = 1, and u | a² with:
- R | 4u + 1 (channel E: Type I, p divides one denominator), or
- R | u + a (channel M: Type II, p divides two denominators).

The solution is then

x = a, y = (N + d)/R, z = (N + N²/d)/R, with N = pa and d = p²u (E) or d = pu (M).

This is the reader's shell criterion.

### 3.1 Eight shifts

**Theorem 50.4.** Let q be an odd prime dividing

F(p) = (p+1)(p+2)(p+3)(p+4)(p+7)(p+8)(2p+1)(3p+1),

with (p/q) = −1. Then the certificate in the table below exists. Equivalently, **a counterexample p ≡ 1 (mod 24) is a quadratic residue modulo every odd prime factor of F(p).**

For q | p+k with q ∤ k, (p/q) = (−k/q). For q | 2p+1, (p/q) = (−2/q); for q | 3p+1, (p/q) = (−3/q). Moreover:
- (−1/q) = −1 ⟺ q ≡ 3 (mod 4);
- (−2/q) = −1 ⟺ q ≡ 5, 7 (mod 8);
- (−3/q) = −1 ⟺ q ≡ 2 (mod 3);
- (−7/q) = (q/7) = −1 ⟺ q ≡ 3, 5, 6 (mod 7).

| shift | q with (p/q) = −1 | shell R | u | channel | why R divides the target |
|---|---|---|---|---|---|
| p+1 | q ≡ 3 (mod 4) | q | a | E | 4a + 1 = p + R + 1 |
| p+4 | q ≡ 3 (mod 4) | q | 1 | M | 4(a + 1) = p + R + 4 |
| p+2 | q ≡ 5, 7 (mod 8) | q if q ≡ 7, 3q if q ≡ 5 (mod 8) | a/2 | E | 2(2a + 1) = p + R + 2 |
| p+8 | same | same | 2 | M | 4(a + 2) = p + R + 8 |
| 2p+1 | same | same | 2a | E | 8a + 1 = 2(p + R) + 1 |
| p+3 | q ≡ 2 (mod 3) | 3 | q | E | 4q + 1 ≡ q + 1 (mod 3) |
| p+7 | q ≡ 5 (mod 7) | 7 | q | E | 4·5 + 1 = 21 |
| p+7 | q ≡ 6 (mod 7) | 7 | aq | M | aq + a = a(q + 1) |
| p+7 | q ≡ 3 (mod 7) | 7 | 2aq | M | a(2q + 1) |
| 3p+1 | q ≡ 2 (mod 3) | (4q + 1)/3 | q | E | 4q + 1 = 3R |

In the 3p+1 row the shell is a = qm, where m = (N₃/q + 1)/3 and N₃ = (3p+1)/4.

*Proof that the table is valid.*
- **The shifts p+2, p+8, 2p+1.** Since p ≡ 1 (mod 3), 3 divides each of them. So R divides the shift, and q ≠ 3 because (p/3) = 1. Also R ≡ 7 (mod 8), since 3q ≡ 15. Then 8 | p + R, so a is even, and a/2, 2 and 2a all divide a².
- **The shift p+7.** Here 8 | p + 7, so a is even. Also q | a, so aq and 2aq divide a².
- **The shift 3p+1.** Since p ≡ 1 (mod 8), N₃ is odd, and N₃ ≡ 1 (mod 3). So h = N₃/q ≡ 2 (mod 3) and m is a positive integer. R = (4q+1)/3 is ≡ 3 (mod 4), and

  4qm − p = (4N₃ + 4q)/3 − p = (4q + 1)/3 = R.

  (This is archive Theorem 24.171 with k = 3.)
- **Coprimality.** A common prime of R and a divides 4a − R = p, and p ∤ R in every row:
  - in the first nine rows R divides a shift that p does not divide;
  - in the last row R ≤ (3p + 2)/3 < p + 1, and R = p would force q = (3p − 1)/4, which does not divide N₃.

The shell criterion then gives the solution. ∎

*Checks* (`es50_checks.py`, items B1, B1b, B1c, B5):
- Every (shift, q) certificate for all primes p ≡ 1 (mod 24) below 10⁷ is built and verified exactly: 780,700 certificates, none bad.
- 247 primes survive all eight shifts. All lie in S₈₄₀, the first being 3889, 29401, 29569, ….
- The least primes certified only by p+2, only by 2p+1 and only by p+8 are 2521, 9601 and 33,961.
- The record prime **p* = 8,803,369** is certified by exactly two shifts, with four certificates:
  - p*+2 = 3·223·13159, with 223 ≡ 13159 ≡ 7 (mod 8), giving shells 223 and 13,159;
  - 2p*+1 = 3·677·8669, with 677 ≡ 8669 ≡ 5 (mod 8), giving shells 2031 and 26,007.

  It is certified by none of p+1, p+3, p+4, p+7. Its least occupied shell is 107 (reader, Proposition records).

*What was recorded before.*

| shift | status before this note |
|---|---|
| p+1, p+4 | archive Theorem 24.50, with its necessary condition on (p+1)/2 and p+4 |
| p+3, p+7 | the reader's R = 3 and R = 7 criteria, rewritten here through reciprocity |
| 3p+1 | archive Theorem 24.171 with k = 3 |
| p+8 | the family is archive (2028) with s = 2; the condition is not stated |
| p+2, 2p+1 | not stated in the archive, the reader, `43_` or `43a_` (grep); they come from the notes' edge branch with (X, Y, Z) = (1, 2, a/2) and X = 2 |

**Salez's charts.** Each of the rows p+1, p+2, 2p+1, p+4, p+8 is the union, over the free divisor R, of one of Salez's charts with small fixed constants. The referee checked 11,344 certificates against these charts:

| rows | chart and constants |
|---|---|
| p+1, p+2, 2p+1 | (15b) with (B, C) = (1, 1), (1, 2), (2, 1) |
| p+4, p+8 | (14c) with (B, D) = (1, 1), (1, 2) |

What is new here is the uniform quadratic-residue form, with the choice R = q or 3q to reach the right class. No literature search was made.

*Corollary (norm forms).* The discriminants −4, −8, −3 and −7 have class number one. Hence, for a counterexample p ≡ 1 (mod 24), each number below is primitively represented by the principal form of its discriminant, since all of its prime factors are split in the corresponding field (Cox, *Primes of the form x² + ny²*, §§2–3):

| number | form |
|---|---|
| (p+1)/2 and p+4 | x² + y² |
| p+2, p+8 and 2p+1 | x² + 2y² |
| (p+3)/4 and (3p+1)/4 | x² + xy + y² |
| (p+7)/8 | x² + xy + 2y² |

### 3.2 A ninth shift on four hard classes

**Theorem 50.5.** Let N = (p+5)/2, which is odd, and suppose one of the following holds:
- p ≡ 9 (mod 40), which contains the hard classes 169, 289, 529 (mod 840);
- p ≡ 121 (mod 840);
- p ≡ 1 or 361 (mod 840) and p ≡ 4 (mod 9).

If some prime q | p+5 has (p/q) = −1, then 4/p is solvable explicitly by the µ = 5 lock of §7:
- a divisor d | N with d ≡ −p (mod 20) gives an E-certificate on the shell R = d;
- a divisor h | N with h ≡ −1 (mod 20) gives an M-certificate.

So a counterexample in these classes is a quadratic residue modulo every odd prime factor of p+5.

*Proof.*
1. **The character.** For q | N, q ≠ 5 and (p/q) = (−5/q) = (−1/q)(q/5). This is +1 exactly on H = {1, 3, 7, 9} (mod 20), a subgroup of index 2 in (ℤ/20)^×.
2. **The case p ≡ 9 (mod 40).**
   - Here N ≡ 7 (mod 20), and the targets are −p ≡ 11 and −1 ≡ 19.
   - Take q | N with q ∉ H. If q ≡ 11 or 19, take d = q or h = q.
   - If q ≡ 13, then N/q ≡ 7·17 ≡ 19. If q ≡ 17, then N/q ≡ 7·13 ≡ 11, since 13·17 ≡ 1.
   - Conversely both targets lie outside H, so a firing lock contains a prime factor outside H.
3. **The case p ≡ 1 (mod 40).**
   - Here N ≡ 3 (mod 20), both targets are 19, and the complement involution adds the target N·19⁻¹ ≡ 17.
   - The forced divisors of N do the rest:
     - 3 | N always, and 3q ≡ 19 when q ≡ 13;
     - 7 | N when p ≡ 2 (mod 7), which is the class 121, and 7q ≡ 17 when q ≡ 11;
     - 9 | N when p ≡ 4 (mod 9), and 9q ≡ 19 when q ≡ 11. ∎

*The condition cannot be dropped.* Take p = 12601 ≡ 1 (mod 840), ≡ 1 (mod 9). Then p+5 = 2·3·11·191, with (p/11) = (p/191) = −1. The divisors of N = 3·11·191 are ≡ 1, 3, 11 or 13 (mod 20), so the lock does not fire.

*Checks* (B2, B2b):
- all 41,419 primes p ≡ 9 (mod 40) below 10⁷: the lock fires exactly when a non-residue factor exists; 19,546 certificates, none bad;
- 5688 primes in the other classes: no violation.

*Source.* The case p ≡ 9 (mod 40) is in "Full divisor locks, QR subtori, and survivor idempotents" in substance: its Theorem 3.7(ii), Corollary 3.8(ii) and Theorem 4.2. The extension to the classes 121, 1, 361 is pass C's (its Theorem 4.1), proved again here.

### 3.3 The visible-box principle

**Theorem 50.6.** Let R ≡ 3 (mod 4) be prime and let c be a class of hard primes modulo 10080 = 2⁵·3²·5·7. Let e_f be the lower bound for v_f((p+R)/4), f ∈ {2, 3, 5, 7}, that c forces, and let Box(c) = {∏ f^{i_f} mod R : 0 ≤ i_f ≤ 2e_f}.

If Box(c) contains every non-zero square modulo R, then for every prime p ∈ c the shell R is occupied if and only if some odd prime q | p+R has (p/q) = −1. So on such a class p+R has the quadratic-residue property.

*Proof.*
- Every element of Box(c) is the residue of a divisor of a².
- **A non-residue factor.** Let q | a be prime with (q/R) = −1. Since p ≡ −R (mod q), reciprocity gives (p/q) = (−R/q) = (q/R) = −1. Then q·Box(c) is the whole non-square coset, so the divisors of a² reach every unit. In particular they reach the E-target −4⁻¹.
- **No separate case for (p/R) = −1.** Let m be the odd part of p+R. Since p ≡ 1 (mod 8), reciprocity gives (p/m) = (m/p) = (R/p) = (p/R). So (p/R) = −1 forces a prime factor q of m with (p/q) = −1. (The referee noticed that the case is redundant.)
- **Conversely.** Suppose no odd prime q | p+R has (p/q) = −1. Every odd prime ℓ | a has (ℓ/R) = (−R/ℓ) = (p/ℓ) = 1. The prime 2 divides a only when R ≡ 7 (mod 8), and then (2/R) = 1. So every divisor of a² is a square, while both targets are non-squares. This is the Jacobi barrier (reader, Proposition jacobi). ∎

*The good shells.* |Box| ≤ 7·5·3·3 = 315, so only R ≤ 631 can qualify. The search up to 700 finds exactly the shells below; the counts are good classes out of the 72 hard classes modulo 10080.

| R | good classes | remark |
|---|---|---|
| 3, 7 | 72, 72 | recorded: reader Propositions r3, r7 |
| 11 | 48 | exactly when 5 \| a (p ≡ 169, 289, 529 mod 840) or 9 \| a; the second case is archive Theorem 18.11 |
| 19 | 12 | exactly p ≡ 121 (mod 840) |
| 23 | 48 | its B₂₅ branch is archive Theorem 24.215 |
| **31, 47, 59, 71, 311** | 30, 20, 4, 12, 1 | new |

*Check* (B3): all hard primes below 10⁷ in the good classes, 90,897 tests of (p, R), no violation of the equivalence, and 50,545 certificates verified. The principle and the class lists are pass C's (its Theorem 4.3), recomputed here. The archive's census refinements already give certificates in the shells R = 31, 47 and 71 on parts of these classes (Theorems 24.228 and 24.233). They do not state the quadratic-residue equivalence.

### 3.4 The µ = 17 lock

**Proposition 50.7.** Let p ≡ 361 or 529 (mod 840), p ≡ 1 (mod 9) and p mod 17 ∈ {8, 15, 16}; these are six classes modulo 42,840. Then the µ = 17 lock of §7 fires if and only if some prime q | p+17 has (p/q) = −1.

*Proof.*
- Put N = (p+17)/2, which is odd. Then 9 | N, since p + 17 ≡ 18 (mod 9), and 7 | N, since 361 ≡ 529 ≡ 4 ≡ −17 (mod 7). So W = {1, 3, 7, 9, 21, 63} consists of divisors of N.
- For q | N, (p/q) = χ(q) = (−1/q)(q/17), a character modulo 68. The targets −p and −1 (mod 68) have χ = −1, because (p/17) = 1 on these classes.
- For every r with χ(r) = −1, the set rW ∪ N(rW)⁻¹ meets {−p, −1} (mod 68). This finite condition was verified exactly on all six classes.
- Given q | N with χ(q) = −1, some qw or N/(qw) is therefore a lock divisor. Here q ∉ {3, 7}, because (p/3) = (p/7) = 1.
- Conversely, a lock divisor lies in the non-kernel coset, so it has a prime factor with χ = −1. ∎

*Check* (B4): 433 primes below 10⁷, the equivalence holds, all certificates verified. *Example:* the referee pass's p = 2,458,369 is solved by this lock and by none of the conditions of Theorem 50.4.

### 3.5 How many primes survive

| conditions applied, primes p ≡ 1 (mod 24) | below 10⁶ | below 10⁷ | below 10⁸ (pass C) |
|---|---|---|---|
| hard classes | 2370 | 20,513 | 179,468 |
| + eight shifts (Theorem 50.4) | 54 | 247 | 1431 |
| + p+5 on its classes (Theorem 50.5) | 29 | 146 | 816 |
| + µ = 17 (Proposition 50.7) | 29 | 145 | 806 |
| + visible-box shells (Theorem 50.6) | 7 | 31 | 165 |
| + the referee's eight further shifts | — | 23 | — |

The 10⁶ and 10⁷ columns were recomputed here (`es50_survivors.py`); the first row is pass A1's count. The first survivors of all conditions are 43,201, 65,521, 196,561 and so on.

**The referee's further shifts.** Three certificate shapes generalise Theorem 50.4. For a shell R they are:
- u = s with R | p + 4s (needs s | a²);
- u = a/t with R | p + t (needs t | a);
- u = ta with R | tp + 1 (needs t | a).

Theorem 50.4's rows p+1, p+2, 2p+1, p+4 and p+8 are the cases t = 1, t = 2, t = 2, s = 1 and s = 2. The referee searched all {2, 3, 5, 7}-smooth parameters on the 72 hard classes modulo 10080, a complete search for this mechanism. It found eight further quadratic-residue conditions, each valid on part of the hard classes:

| shift | hard classes (mod 840) where it applies |
|---|---|
| p+16, p+36 | 169, 289, 529 |
| p+12 | 121, 289 |
| p+6, 6p+1 | 169 |
| p+24 | 361 |
| 5p+1 | 361, 529 |
| p+20 | 1, 169 |

It verified 46,441 certificates below 10⁷ exactly, and its script (`referee/ref50_more_shifts.py`) was re-run here. The 31 survivors fall to 23. For example 43,201 is removed by p+24, with 4/43201 = 1/10914 + 1/1036824 + 1/1885982856 (checked exactly).

Each condition removes, for about half of all primes q, one or two further residue classes modulo q. So a Selberg upper-bound sieve gives ≪ x/(log x)^κ survivors, with κ ≥ 5 on every hard class. That is far weaker than Vaughan's bound x·exp(−c(log x)^{2/3}) on the exceptional set (reader, §1). These conditions quantify what the explicit certificates sieve; they do not approach a proof.

### 3.6 The Collatz reading of the 3p+1 condition

For odd p, v₂(3p+1) is 1, 2 or ≥ 3 according as p ≡ 3 (mod 4), p ≡ 1 (mod 8) or p ≡ 5 (mod 8). So for p ≡ 1 (mod 8), (3p+1)/4 is the odd Collatz successor U(p), and Theorem 50.4 reads:

**a counterexample p ≡ 1 (mod 24) has U(p) composed only of primes ≡ 1 (mod 3).**

The odd Collatz predecessors of an odd n with 3 ∤ n are Π_k(n) = (2^{e+2k}n − 1)/3, k ≥ 0, where e ∈ {1, 2} is fixed by 2^e n ≡ 1 (mod 3). They satisfy Π_{k+1} = 4Π_k + 1, which is the notes' map R(a) = 4a + 1. So for k ≥ 1, Π_k ≡ 5 (mod 8).

Every prime P ≡ 5 (mod 8) is solved by the shell R = 3 with u = 2:
- a = (P+3)/4 is even and prime to 3;
- 4·2 + 1 = 9 ≡ 0 (mod 3).

(For P = 5 this gives 4/5 = 1/2 + 1/20 + 1/4.) So only the first member of each predecessor chain can be a hard prime. This is the classical Syracuse predecessor structure (Lagarias, *Amer. Math. Monthly* 92 (1985)). It links the Erdős–Straus and Collatz workbenches (`44_`), but no solvability statement iterates the Collatz map.

## 4. Barriers

**Proposition 50.8 (the width-one barrier).** This is Theorem 3.1 of "Normalized divisor supports and the residual pre-Niemeier datum". Let R ≡ 3 (mod 4), gcd(R, pa) = 1, and let K ≤ (ℤ/R)^× be generated by the primes dividing a.
1. If shell R is occupied, then −1 ∈ K or −4 ∈ K.
2. This implies the reader's group barrier, −1 ∈ ⟨4, K⟩ (reader, Proposition groupbarrier), and is strictly sharper.
3. The two coincide when every prime factor of R is ≡ 3 (mod 4), in particular when R is a prime power.

*Proof.*
1. Every divisor of a² lies in K, and so does a. The M-target −a is in K exactly when −1 is. The E-target −4⁻¹ is in K exactly when −4 is.
2. The implication is immediate. The two can differ only when −1 ≡ 4^j (mod K) for some j ≥ 2.
3. The referee found this generalisation of the prime-power case. When every prime factor of R is ≡ 3 (mod 4), each (ℤ/q^k)^× is cyclic of order ≡ 2 (mod 4). So (ℤ/R)^× = P × O, where P is an elementary abelian 2-group and O has odd order.
   - The element 4 is a square, so it lies in O. Write −1 = (ε, 1).
   - If −1 = 4^j·h with h ∈ K, then h = (ε, w) for some w ∈ O.
   - Then h^{|O|} = (ε, 1) = −1 lies in K. So −1 ∈ ⟨4, K⟩ implies −1 ∈ K. ∎

*Example* (C1): (p, R) = (433, 91), a = 131 prime. Then K = ⟨40⟩ = {1, 27, 40, 53, 66, 79} contains neither 90 = −1 nor 87 = −4, yet ⟨4, K⟩ ∋ 90. The Jacobi barrier is silent too, since (131/91) = −1. The shell is empty.

*Count* (C2): among the shells R < 3p of the primes p ≡ 1 (mod 24) below 3000, 124 empty shells are killed by the width-one barrier while the group barrier is silent; no barrier is ever violated. Every one of these R has a prime factor ≡ 1 (mod 4), as 3. requires (referee).

**Recommendation.** The reader's Proposition groupbarrier should be upgraded to Proposition 50.8. The archive has the sharper form as its "reachable targets" T_H (Theorem 15.5).

For squarefree R whose prime factors are all ≡ 3 (mod 4), with an odd number of them, the notes' "QR-subtorus signature obstruction" is the group barrier. This is pass C's Proposition 4.6: (ℤ/R)^× = P × H, with P ≅ C₂^t the 2-Sylow subgroup and |H| odd. It is strictly stronger than the Jacobi barrier, for example at p = 73, R = 483.

## 5. Facts about single shells

### 5.1 Non-coprime shells

**Proposition 50.9.** Let p be prime and R ≡ −p (mod 4).
1. gcd(R, pa) > 1 ⟺ p | R. Write R = kp, with k ≡ 3 (mod 4).
2. If p ∤ k, the one-congruence criterion "some d | N² has d ≡ −N (mod R)" is equivalent to occupancy, and every such d gives integral y and z.
3. If p² | R, it is not: for p = 73 and R = 7·73² = 37,303, the divisor d = 4·73³ divides N² and d ≡ −N (mod R). It gives y = 60 but z = 1920/73. The shell has no solution at all (brute force, D1).

*Proof of 2.* This is pass A1's Proposition 4.6.
- Put m = (k+1)/4, so gcd(k, m) = 1, a = pm and N = p²m. Any d with d ≡ −N (mod kp) is divisible by p. Write d = p·d₁, with d₁ | p³m² and k | d₁ + pm.
- **Case p³ ∤ d₁.** Then d₁ | (pm)². So d₁ is a certificate for the reduced shell (R₀, N₀) = (k, pm), and the two sets of formulas agree.
- **Case p³ | d₁.** Write d₁ = p³w with w | m². Then k | 4p²w + 1, so (w/k) = (−1/k) = −1.
- But every prime ℓ | m has (ℓ/k) = 1:
  - for odd ℓ, k ≡ −1 (mod ℓ) and reciprocity gives (ℓ/k) = (−1/ℓ)(−1)^{(ℓ−1)/2} = 1;
  - for ℓ = 2, k ≡ 7 (mod 8).
- So (w/k) = 1, a contradiction. ∎

**The lemma appears without the hypothesis** in four notes:
- the defect-completion article, Lemma 2.1;
- "Split-zero residual moonshine", Theorem 3.1;
- the A₈ snowflake note, Theorem 2.1;
- "Terminal-core lock covers …", Theorem 2.1.

(The first version of this note named the corrected interaction calculus here. Its Lemma 2.1 assumes (R, N) = 1; the referee found the error.)

The central-cover report states the lemma without the hypothesis, but its proof uses the coprime case. The reduced criterion of the other notes (divide by g = gcd(R, N)) is correct.

**The error is harmless where the notes use it.** A non-coprime shell has p | a, and the criterion can only fail when p² | R, that is, when R ≥ 3p².

### 5.2 Ramified shells

**Proposition 50.10.** Let (R, p) be a coprime shell.
1. If R | p − 1, then E_a = M_a as sets. So the ordered completions number 3|M_a|.
2. If R | p² − 1, then u ↦ a²/u maps E_a to itself with only possible fixed point u = a. Hence |E_a| is odd if and only if R | p + 1.

*Proof.*
1. 4a ≡ p ≡ 1 (mod R), so 4(u + a) ≡ 4u + 1.
2. The complement sends the class t to a²t⁻¹. Here a²·(−4⁻¹)⁻¹ = −4a² ≡ −p²/4 (mod R), because 4a ≡ p. This is −4⁻¹ again when p² ≡ 1 (mod R). Finally a ∈ E_a ⟺ R | 4a + 1 = p + R + 1. ∎

*Checks* (D2, D3): all coprime shells with R | p² − 1 and p ≡ 1 (mod 4) below 2000: 233 shells for (1) and 947 for (2). The statements are passes A1 and D's.

### 5.3 The pair-count Dirichlet series

This is Theorem 4.3 of the defect-completion article. Put A_R(n) = #{(X, Y, Z) : XYZ = n, gcd(X, Y) = 1, R | X + Y}. For a coprime shell, A_R(pa) is the number of ordered certificates, by the divisor-pair reconstruction. For R ≥ 3,

Σ_{(n,R)=1} A_R(n) n^{−s} = φ(R)^{−1} Σ_{χ mod R} χ(−1) ζ_R(s) L(s, χ) L(s, χ̄) / ζ_R(2s),

where ζ_R omits the primes dividing R.

*Proof.*
1. Orthogonality gives 1_{X ≡ −Y} = φ(R)^{−1} Σ_χ χ̄(−1) χ(X) χ̄(Y), and χ̄(−1) = χ(−1).
2. The variable Z is free and prime to R, which contributes ζ_R(s).
3. Möbius inversion over d | gcd(X, Y) gives Σ_{gcd(X,Y)=1} χ(X)χ̄(Y)(XY)^{−s} = L(s, χ)L(s, χ̄)/L(2s, χχ̄), and χχ̄ is the principal character modulo R. ∎

Pass A1 checked 8757 coefficients. The principal term gives A_R(n) ≈ τ(n²)/φ(R). No positivity statement follows.

### 5.4 No finite congruence cover

The divisor-pair note's Problem 9.5 asks for finitely many central and edge templates covering all primes in S₈₄₀. As a congruence cover this is impossible:
- every template class contains no square modulo its modulus. For the notes' central templates this is pass A1's Proposition 4.7; for the edge templates it is the reader's Proposition nosquare; for polynomial identities it is Mordell and Schinzel–Yamamoto (reader, §1);
- the primes p ≡ 1 (mod lcm(840, M₁, …, M_k)) lie in S₈₄₀ and escape every template. By Dirichlet's theorem they exist.

If instead the templates may impose p-dependent divisibility conditions, the problem is the conjecture itself. Lemma 50.2 is the j = 1 case of the same obstruction.

## 6. Identities in the notes

**Rosati's family (Salez's chart 14a with (B, C, D) = (c, 1, k/c)).** Let k ≥ 1, c | k and m = 4k − 1. If n ≡ −c (mod m), then

4/n = 1/(kn) + 1/(k(n+c)/m) + 1/(kn(n+c)/(mc)).

*Proof.* The three terms are 1/(kn), m/(k(n+c)) = mn/(kn(n+c)) and mc/(kn(n+c)). Over the common denominator kn(n+c) the numerator is (n + c) + mn + mc = (n + c)(1 + m) = 4k(n + c), so the sum is 4/n. The denominators are integers because m | n + c and c | k. ∎

Check E2: 60,909 identities with k < 40 and n < 20,000. With k = 22 and c = 11 this is the identity on **n ≡ 76 (mod 87)** that pass B1 found. It contains the notes' first direct channel where n ≡ 1 (mod 3) (check E3).

**The two direct 29-channels** of "Terminal residual coordinates", Theorems 7.1–7.2, are correct:
- n ≡ 917 (mod 1276) gives 4/n = 1/((n+11)/4) + 1/((n+11)(n+29)/44) + 1/(n(n+11)(n+29)/1276);
- n ≡ 1605 (mod 2204) gives the same with 19 in place of 11.

These are Salez's chart 15b with (B, C, F) = (1, 29, 11) and (1, 29, 19). Check E1 covers 1236 values of n. Both lie inside wider single identities:
- the first inside Rosati's family above with (k, c) = (80, 40), m = 319 = 11·29, since 917 ≡ −40 (mod 319) and 319 | 1276;
- the second inside chart 14a with (B, C, D) = (2, 23, 3), m = 551 = 19·29, since 1605 ≡ −2·23⁻¹ (mod 551) and 551 | 2204.

The referee found both containments, and they were checked here.

**"Only two direct channels" depends on the vocabulary.** The notes admit only single primes from {5, 11, 19, 23} as lock divisors, and their Theorem 7.1 is correct under that restriction. With other divisors, the same lock theorem gives more classes:
- The µ = 5, d = 31 lock covers n ≡ 429 (mod 620), by 4/n = 1/a + 1/(as) + 5/(nas) with a = (n+31)/4 and s = (n+5)/31. This class contains the prime 33,289, which lies in the square core (check E4). That is the "external-prime escape" the source note anticipates.
- Pass B1 counts 22 class-level lock channels on 8750 of the 83,160 classes of H^sm × (ℤ/29)^× (recounted by pass C). Among them are the whole fibres u = 18 (µ = 11, h = 87) and u = 26 (µ = 29, d = 3).

## 7. Locks and types

**Proposition 50.11 (the full-divisor locks).** Let p be an odd prime, µ odd and N = (p + µ)/2.
- **Lock (a).** Take d | N odd with d ≡ −p (mod 4µ). Then shell R = d, a = (p+d)/4, carries the E-certificate u = a/µ. Indeed µ | a, and 4u + 1 = (p + d + µ)/µ ≡ 0 (mod d).
- **Lock (b).** Take h | N with h ≡ −1 (mod 4µ), and put e = N/h, t = (h+1)/(4µ). Then a = 2µet and R = µ + 2e satisfy 4a − p = R, and u = µ²t is an M-certificate, since u + a = µtR.

So the locks are Type I and Type II solutions (Elsholtz–Tao, *J. Aust. Math. Soc.* 94 (2013), §2). Pass C identifies them with the faces A = 1 and C = 1 of the Elsholtz–Tao parametrisation; lock (b) is Lopez's Type B. The identity in the notes' proof of lock (a) should read ps + p + µ = (p + µ)(p + d)/d; the printed ps + p + µs is false (check E5).

*Computations* (F1–F3):
- Every hard prime below 10⁷ (20,513 of them) has a verified lock certificate for some odd µ. Pass C: every one below 10⁸ (179,468 of them).
  - This fails for non-hard primes. The prime 409 ≡ 1 (mod 24), with 409 mod 840 = 409, has no lock certificate for any odd µ. The search is exhaustive: lock (a) needs µ ≤ 3p/7 and lock (b) needs µ ≤ (p+2)/7. The referee found it; it is the only prime p ≡ 1 (mod 4) below 3·10⁶ without one.
  - Neither type suffices alone. 1201 has no type-(a) certificate, and 5569 has no type-(b) certificate (pass C).
- Every prime p ≡ 1 (mod 24) below 10⁷ has a Type II (M-channel) solution in a shell R ≤ 107. The record prime p* is the only one that needs R = 107 (check F2). Pass F: the same below 10⁸.
- The *complement-square* certificates are the M-certificates u = Q² with Q | a, that is R | Q + a/Q. They are Lopez's Type C and Salez's chart 14c, and the notes use them for p*. They are not universal:
  - 97 is the least prime p ≡ 1 (mod 24) with none in any shell. The search is exhaustive, since R ≤ (p+4)/3 is forced.
  - 3361 is the least hard prime with none.

## 8. Errors and overstatements in the notes

Each item is verified here unless marked with the pass that found it.

| # | Note | Statement | Problem | Evidence |
|---|---|---|---|---|
| 1 | Terminal residual coordinates; June replacement; BEAVERSHINE integrated preprints | H^sm = S₈₄₀ × Q₁₁ × Q₁₉ × Q₂₃ treated as the residual locus | it is the support-zero core; 550 further classes are uncovered at level M₂₃ | Theorem 50.1; the prime 3361 |
| 2 | Defect-completion Lemma 2.1; split-zero residual moonshine Thm 3.1; A₈ snowflake Thm 2.1; Terminal-core lock covers Thm 2.1 | one-congruence criterion without coprimality | false when p² \| R; harmless for R < 3p² | Proposition 50.9; p = 73 |
| 3 | Terminal residual coordinates Thms 7.1, 10.4, Cor 14.4 | "only two direct channels", "rigidity" of 29 | artefact of the lock vocabulary | §6; n ≡ 429 (mod 620) |
| 4 | "Constructive Algebra of the Centered Erdős–Straus Resolution", Thms 15.1–15.3 | the Erdős–Straus conjecture | its Lemma 13.4 counts failure states as removed; it uses an involution between the pieces P₋ and P₊, which cannot exist since they have 30,240 and 37,800 classes; its Thm 15.2 treats the core as the residual locus | pass F; sizes recomputed by passes B1 and C. The June replacement removed a conclusion of the same kind, resting on a lemma with the same circularity, from its predecessor (pass B1 reconstructed that diff; the replacement's README gives no reason) |
| 5 | Star–Kneser positivity, Thm 7.2 | converse of Star–Kneser forcing | false at p*, R = 107 | pass E; already retracted in the archive (Proposition 15.7) |
| 6 | Pre-Niemeier Thm 11.1 and three sibling notes | umbral group (the automorphism group of the glue code) ≅ GL₂(3), because the double cover is non-split | the argument does not exclude the binary octahedral group; the conclusion is true (13 involutions) | pass A1 |
| 7 | Defect-completion Thm 9.1; Niemeier refinement Thm 8.1; umbral completion Thms 4.3, 8.1 | "Coxeter–Fourier decomposition of A_R(p)" over the six classes | ill-posed: A_R(p) is not a function of p mod 840 | check E6: A₁₁(p) ∈ {0, 4, 6, 8, 10} on p ≡ 1 (mod 840) |
| 8 | Mixed-mock Virasoro note, Cor 5.3, 6.8, Thm 7.3, 9.1 | the three mock functions are a c = −68/7 Virasoro character shadow | the modified modular pair used is not a representation of SL₂(ℤ) (relation residual 0.986); no relabelling matches both S and T | pass D (script re-run here) |
| 9 | full-lock proofs (five notes) | numerator ps + p + µs | should be ps + p + µ | check E5 |
| 10 | Terminal residual coordinates §10 | a "torsor map" (ℤ/18)^× → S₈₄₀ | not a homomorphism | passes B1, C |
| 11 | Busy-Beaver notes | S(6) bound 10↑↑15; ZFC index 745/748 | superseded (2025 bounds; index 643) | pass E |
| 12 | several | Kneser 1953 | the finite-group theorem is Kneser, *Math. Z.* 61 (1955) | passes B1, E |

On the Busy-Beaver residues modulo 107, pass E reduced the claimed "reconstruction" to three independent congruences. Tested against a null model with anchors fixed in advance, the match is at chance level (held-out p = 0.38). The only logical link between Busy Beaver and Erdős–Straus is the classical one: a counterexample search is a Π₁ statement, so some Turing machine halts if and only if the conjecture fails.

## 9. What the notes connect to

| Link claimed | Correct? | Source | Bearing on which primes are solvable |
|---|---|---|---|
| A₅⁴D₄ Niemeier lattice from the mod-840 fibration, glue of order 72; umbral group GL₂(3) (the automorphism group of the glue code), lambency 6 | yes | Conway–Sloane, *SPLAG* ch. 16–18; Cheng–Duncan–Harvey, *Res. Math. Sci.* 1 (2014), Table 3; the lattice and glue are archive Thm 25.8, which does not state GL₂(3) | none: depends only on the residue group and on choices |
| T₆ = η(τ)⁵η(3τ)/(η(2τ)η(6τ)⁵), Hauptmodul of Γ₀(6); T₆ + 5 + 72/T₆ the class 6B series | yes | Conway–Norton, *Bull. LMS* 11 (1979); archive (3198)–(3204) | none |
| "Explicit mixed mock functions" for m = 42, K = {1, 6, 14, 21}, labels 1, 5, 11 | yes, and they are **Ramanujan's order-7 mock theta functions**: (−q^{−1/168}F₀, q^{−25/168}F₁, q^{47/168}F₂), exact through q⁴⁰ (pass D; re-run here). The note does not name them. For m = 30 they are the order-5 functions | Zagier, *Astérisque* 326 (2009), the vectors M₇ and M₅; Cheng–Ferrari–Sgroi, *Phil. Trans. R. Soc. A* 378 (2020), 20180439 (arXiv:1912.07997), eq. (3.20): q^{1/2}Ẑ₀(−Σ(2,3,7)) = F₀, in the framework of Cheng–Chun–Ferrari–Gukov–Harrison, *JHEP* 2019(10), 010. The referee pass gave the arXiv paper the wrong authors; corrected here from the paper's title page | none |
| Their shadow as M(2,7) Virasoro characters (c = −68/7, exponents −1/42, 5/42, 17/42) | the minimal-model data are correct; the identification fails (§8, item 8). The genuine order-5 link of this kind is the mock theta conjectures (Andrews–Garvan 1989, proved by Hickerson 1988), checked by pass D to O(q¹⁵⁰) | Mathur–Mukhi–Sen (1988) | none |
| Collatz predecessor chains and x ↦ 4x+1 | yes; classical | Lagarias (1985) | the rephrasing of §3.6 only |
| Kneser's theorem → Star–Kneser forcing | correct one way; a per-shell sufficient condition | Kneser (1955); archive Thms 15.6, 20.7 | yes, per shell; p* has no forced shell (pass E) |
| Elsholtz–Tao types, Salez's charts, Lopez's types (via locks and complement squares) | yes | Elsholtz–Tao (2013); Salez (2014); Lopez (arXiv:2404.01508) | **yes: these are the actual mechanisms**; classical |
| Ogg's primes, supersingular reductions, T_{5A} | yes where checked | Ogg (1974); Duncan–Ono (2016) | none |
| Lorentzian and Hermitian models, inversion, Apollonian and Descartes, Springborn | yes, except that "the modular flow is a Lorentz boost" is false: it is a rotation (pass E) | classical | none |
| Cayley–Dickson algebras and sedenion zero divisors ("ghosts") | yes in the stated conventions | Moreno (1998); Baez, *Bull. AMS* 39 (2002) | none |
| Split-zero semiring G(ℤ): ideals, primes, spectrum | yes; one isomorphism in "A split-zero repair dossier" (Thm 7.2) needs the relation [τ] ∼ 0 (pass D) | archive §21; `43a_` R01 | none: the three states τ, 0, + relabel "target outside the generated group / inside but missed / hit" |

## 10. Open questions

1. **Type II universality.** Does every prime p ≡ 1 (mod 24) have a Type II solution, one with p dividing exactly two denominators? A yes would prove the conjecture. It holds below 10⁸, where it needs shells R ≤ 107 only (§7). It is weaker than Lopez's recorded "Type A or B" conjecture (archive §12.1).
2. **Lock universality on the hard classes.** Does every hard prime have a lock certificate, that is, a Type I solution with A = 1 or a Type II solution with C = 1? It holds below 10⁸ (pass C). The first version of this note asked this for every prime p ≡ 1 (mod 4), which is false: 409 has none (§7).
3. **Can the 550 be covered?** Is every non-square class eventually covered by finitely many single identities at some finite level? For the fibre p ≡ 1 (mod 840), p ≡ 2 (mod 11), pass B1 found the covered fraction to be 75%, 98.44%, 99.39% and 99.86% as the primes 13, 17, 19, 23 are added. If the answer is no for some class, no identity sieve can reduce the problem to the square core.
4. **Are the survivors infinite?** Are there infinitely many primes satisfying all the conditions of §3? A no would prove the conjecture on the hard classes outside a finite set.
5. **The least Π₁ machine.** What is the least number of states of a Turing machine that halts if and only if the conjecture fails? This is the only Busy-Beaver question with a logical bearing on it.
6. **A modular object that sees p.** Is there a modular, mock or quantum modular object whose coefficients are the shell counts 2|E_a| + |M_a|? Every modular object in the notes is independent of p. The only p-dependent analytic object is the pair-count series of §5.3.

## 11. Register entries

- **S85.** Theorem 50.1: the support-zero core is exactly the square core; 3520 = 2970 + 550 classes are uncovered at M₂₃; densities 1/256 and 1/216.
- **S86.** Theorem 50.4: the eight-shift quadratic-residue form. p+2 and 2p+1 are new; p* is certified only by p+2 and 2p+1.
- **S87.** Theorem 50.5 (p+5 on four hard classes), Theorem 50.6 (visible-box principle; R = 31, 47, 59, 71, 311), Proposition 50.7 (µ = 17), and the referee's eight further shifts (23 survivors below 10⁷).
- **S88.** Proposition 50.8: the width-one barrier (reader upgrade), with equality of the barriers when every prime factor of R is ≡ 3 (mod 4). Propositions 50.9–50.10: non-coprime and ramified shells.
- **S89.** §7: locks are E- and M-certificates. Every p ≡ 1 (mod 24) below 10⁷ has a Type II solution with R ≤ 107, and p* alone needs 107. Complement squares fail first at 97.
- **Negative result 77.** The identification of the core with the residual locus (§2.3), the unconditioned one-congruence lemma, "only two direct channels", and the constructive-algebra conclusion.
- **Negative result 78.** The Virasoro identification of the order-7 mock theta functions, and the Busy-Beaver residues modulo 107 (chance level).

## 12. What was not checked, and the checks

**Not re-derived here.** The following rest on the passes named, which ran their own programs:
- the lattice and modular facts: A1;
- the Ogg and supersingular facts: B1;
- the Busy-Beaver literature values: E;
- the Cayley–Dickson identities: F;
- the mock theta and Virasoro computations: D (re-run here, not rewritten);
- the counts below 10⁸ and the 22 channels: B1, C, F.

Salez's completeness statement was taken from his paper, not proved.

**Checks.** All are in `checks/es50/`.

| program | what it does | result | time |
|---|---|---|---|
| `es50_checks.py` | 25 items; every certificate turned into (x, y, z) and tested by 4xyz = p(xy + yz + zx) | all pass | 49 s |
| `es50_support_core.py` | independent reproduction of 4951 and 2970 | reproduced | 4 s |
| `es50_survivors.py` | the survivor table to 10⁷ | as in §3.5 | — |
| `salez/salez_M23_and_G7.py`, with pass B1's `es_families.py` and `coverage.py` | 3520 = 2970 + 550 at M₂₃, and 147,348 at G₇ | reproduced | 2 min |

**Solutions of the example primes by their least shells.**
- 4/3361 = 1/841 + 1/110139970 + 1/950330 (R = 3; 841 = 29²).
- 4/18481 = 1/4625 + 1/3330091390 + 1/4504750 (R = 19).
- 4/2840041 = 1/710012 + 1/261184725275808711129 + 1/288066170388 (R = 7).
- 4/12601 = 1/3151 + 1/7264426096 + 1/13259408 (R = 3).

## 13. The referee pass

An independent Claude instance (model `claude-opus-5-5`) refereed this note and the new Section 6 of the Erdős–Straus reader. It wrote none of either text. It worked from 11:37 to 12:42 UTC and returned its report as text; the report and its nine programs are in `checks/es50/referee/`.

**What it re-ran.** Every program of §12, the author's own scripts, and pass A1's lattice check. It recomputed the main numbers by independent code. It found every proof correct and every number it recomputed in agreement.

**Findings applied, after verification here.**
- **Major 1.** One error was charged to the wrong note. The corrected interaction calculus assumes coprimality. The note that omits it is "Terminal-core lock covers …" (§5.1, §8). Verified by reading both statements.
- **Major 2.** Open question 2 was false as stated: 409 has no lock certificate. Verified by an exhaustive search here.
- **Major 3.** The reader overstated how its Section 6 was verified. Its wording, status labels and "not checked" list were corrected, and the referee paragraph was added to its Appendix B.
- **Minor findings:**
  - Salez's scope;
  - the Salez-chart form of the shift rows;
  - the notes' own form of the case p ≡ 9 (mod 40);
  - the archive's shells R = 31, 47, 71;
  - the redundant case in Theorem 50.6;
  - the harmlessness of the coprimality error;
  - the containments of the 29-channels (verified here);
  - the unopened drafts folder;
  - no reason attributed to the June removal;
  - the precursor's status;
  - the two exceptions among the connections;
  - "umbral group" for GL₂(3);
  - the constructive-algebra entry;
  - "odd prime factor";
  - the analogy wording;
  - the parts of the reader not updated for version 3.
- **Missed results adopted:**
  - the eight further shifts (§3.5), whose script was re-run here;
  - the equality of the barriers when all prime factors of R are ≡ 3 (mod 4) (§4), whose proof was checked here.

**Not adopted.** The referee's explicit witness table for the "only if" direction of Theorem 50.1(a) is not reproduced here; the computation stands. The Busy-Beaver index 643 remains pass E's statement.
