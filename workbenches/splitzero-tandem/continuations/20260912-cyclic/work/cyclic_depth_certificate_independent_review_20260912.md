# Independent review of the cyclic-depth certificate and finite checker

Date: 2026-09-12. This is a bounded, source-preserving audit of the exact staged files identified below. All code in the two assigned code files and the complete accompanying research note were read. No Lean, Lake, or Elan process was started. Consequently this report is a mathematical and source-level audit, together with independent Python execution; it is not a fresh Lean kernel acceptance or transitive-axiom report.

The review found no mathematical defect in the Lean declarations as stated and no implementation defect within the finite checker's exercised positive-integer domains. The exact qualifications are substantive: the attained maximum has a supplied maximizing coordinate, the index type is finite, the declared `localOrder` is a numerical expression rather than a bundled nilpotency theorem, and the Python checker contains eight test methods. The empty-packet test does not exercise an empty coordinate set.

## 1. Exact evidence and replay

All three originals are under `output/split_zero_rh_tandem_2026-09-12/sources/web_conormal_cyclic_formal_delivery/repository/`.

| Assigned source | SHA-256 |
|---|---|
| `formal/splitzero/SplitZeroCyclicDepth.lean` | `97764365d88970910ecd6f12cd3d5f1fbf268a7c8939f34d529ed6c97b424463` |
| `workbenches/tau-conormal-cyclic-formal/check_depth_models.py` | `4f069699ec1b9bca1ff34832f6f26d2f66248a25e0d6da3764f394572bf46ac8` |
| `workbenches/tau-conormal-cyclic-formal/RESEARCH_NOTE.md` | `202d7e9111c0a88fdd30c15554f3dd1e0907b2fc4fb2e11da129c97b10a053fd` |

Hashes before and after the four runs agree. Numbered copies, separate stdout and stderr files, per-run JSON, the replay script, the subtask logbook, and `replay_receipt.json` are preserved under `work/cyclic_depth_independent_check_20260912/`. Line references below refer to the originals and their identical numbered copies.

The original checker was executed with Python 3.13.9. Its ordinary modes use the source file unchanged; its negative controls use the source's existing `--self-test-failure` flag.

| Execution | Reported methods | Errors | Failures | Exit code | Outcome |
|---|---:|---:|---:|---:|---|
| Normal | 8 | 0 | 0 | 0 | Pass |
| `-O` | 8 | 0 | 0 | 0 | Pass |
| Normal, deliberate failure | 9 | 0 | 1 | 1 | Expected failure |
| `-O`, deliberate failure | 9 | 0 | 1 | 1 | Expected failure |

The deliberate failure is an invocation of `unittest.TestCase.assertEqual`, not a Python `assert` statement. Optimization therefore leaves the negative control active. The two actual negative runs confirm both failure reporting and nonzero process exit.

## 2. Exact formal signatures and proof dependencies

The source has four definitions and nine theorem declarations in `SplitZero.CyclicDepth`. Every declaration has an implicit index type `ι : Type*` with `[Fintype ι]` (line 14). All multiplicities, coordinates, depths, and bounds are natural numbers. No field, polynomial ring, ideal, quotient, root, complex number, or nilpotent element occurs in these declarations.

The following inventory states every declaration's mathematical content and its extra hypotheses. Here `|a|` denotes the finite sum of the natural coordinates of `a`; this notation in the review does not change the source's objects.

| Lines | Declaration | Exact content and extra hypotheses |
|---|---|---|
| 17–19 | `Admissible m r a` | There exist `q,t : ι → ℕ` with `t i < m i`, `a i = t i + m i*q i` for all `i`, and `∑ i, q i < r`. No positivity is included as a separate parameter. |
| 22–27 | `admissible_of_floor_sum` | From `∀ i, 0 < m i` and `∑ i, a i / m i < r`, constructs the quotient/remainder witnesses. |
| 29–35 | `floor_sum_of_admissible` | From `Admissible m r a`, proves the literal division inequality. No extra positivity hypothesis is required. |
| 37–40 | `admissible_iff_floor_sum` | Equivalence of the preceding predicates under `∀ i, 0 < m i`. |
| 43–44 | `ceiling m r M` | The natural number `∑ i, (m i - 1) + (r - 1)*M`, using natural subtraction. `M` is a supplied number, not a computed maximum. |
| 46–61 | `degree_le` | From `∀ i, m i ≤ M` and admissibility, proves `∑ i, a i ≤ ceiling m r M`. |
| 67–68 | `extremal m r j i` | Under `[DecidableEq ι]`, defines `(m i - 1) + m i*(if i=j then r-1 else 0)`. The argument `j : ι` supplies an actual index. |
| 70–79 | `extremal_admissible` | For a supplied `j`, positive multiplicities and `0<r` imply admissibility of this exponent vector. Maximality of `m j` is not needed for admissibility. |
| 81–95 | `extremal_degree` | For a supplied `j`, the degree equals `ceiling m r (m j)`. It is an identity even without positivity or maximality. |
| 97–103 | `attained_maximum` | Under positive multiplicities, `0<r`, a supplied `j`, and `∀ i, m i ≤ m j`, proves both the universal admissible-degree bound and existence of an admissible vector with that exact degree. This theorem inherits `[DecidableEq ι]`. |
| 105–113 | `floor_attained_maximum` | The same bound and attainment stated directly using the floor sum. The theorem explicitly omits `[DecidableEq ι]` and uses `classical` internally to apply the preceding construction. |
| 117 | `localOrder m r M` | Defines `ceiling m r M + 1`; its docstring gives the intended application. |
| 119–126 | `localOrder_step` | Under `0<r`, proves `localOrder m (r+1) M = localOrder m r M + M`. It neither requires nor proves that `M` is a maximum. |

The source contains no `sorry`, `admit`, or newly declared axiom. That source observation does not establish the imported environment's transitive axiom list. The `classical` command in `floor_attained_maximum` is explicit. Fresh elaboration and kernel verification were excluded from this assignment.

### 2.1 Quotient/remainder equivalence, with positivity accounted for

Assume first that every `m i` is positive. Define

\[
q_i=a_i\mathbin{/}m_i,\qquad t_i=a_i\bmod m_i.
\]

Euclidean division gives `t_i<m_i` and `a_i=t_i+m_i q_i`, while the supplied floor-sum inequality is precisely `∑q_i<r`. These are the three required witnesses. This is the construction in lines 25–27.

Conversely, admissibility supplies natural numbers `t_i<m_i`. Since `0≤t_i`, it follows that `0<m_i`, including when positivity was not separately provided. Substituting `a_i=t_i+m_iq_i` and dividing by positive `m_i` gives

\[
a_i\mathbin{/}m_i=(t_i\mathbin{/}m_i)+q_i=0+q_i=q_i.
\]

Summing proves the literal floor-sum inequality. This proves exactly why `floor_sum_of_admissible` has fewer assumptions than `admissible_of_floor_sum`. If a nonempty coordinate has `m_i=0`, no admissibility witness can exist because `t_i<0` is impossible. The positivity hypothesis on the reverse implication is therefore necessary for its intended relationship to natural division by zero: Lean's total natural-number division alone would not exclude such an input.

### 2.2 Bound and attainment

Write `A=∑_i(m_i-1)`. For admissible witnesses, `∑q_i<r` implies `r≥1` and `∑q_i≤r-1`. Also `t_i≤m_i-1`. If every `m_i≤M`, then

\[
\begin{aligned}
\sum_i a_i
&=\sum_i(t_i+m_iq_i)\\
&\le\sum_i((m_i-1)+Mq_i)\\
&=A+M\sum_iq_i\\
&\le A+M(r-1)=A+(r-1)M.
\end{aligned}
\]

These are exactly the inequalities and distributivity steps in `degree_le`. The absence of explicit `hm` and `hr` here is correct because its admissibility hypothesis already supplies the needed facts.

Now assume positive multiplicities, `r≥1`, and an index `j` whose multiplicity dominates every other multiplicity. Set

\[
t_i=m_i-1,\quad q_j=r-1,\quad q_i=0\ (i\ne j),
\quad a_i=(m_i-1)+m_iq_i.
\]

Positivity gives `0≤t_i<m_i`, and `∑q_i=r-1<r`. Hence this vector is admissible. Its degree is

\[
\sum_i a_i=A+m_j(r-1)=A+(r-1)m_j.
\]

Together with the bound for `M=m_j`, this establishes a maximum, not merely a supremum or an unachieved bound. The source's `attained_maximum` returns precisely these two propositions as a conjunction; `floor_attained_maximum` transfers them using the proved equivalence.

There is no missing mathematical assumption concealed by the parameter `j`: it explicitly forces an inhabited index type. The file does not separately construct a maximizing `j` from `[Nonempty ι]`. Mathematically, finite nonemptiness supplies one: enumerate the finite index set as `i_1,…,i_k` with `k≥1`, start with `j_1=i_1`, and at each subsequent index retain the previous index or choose the new index according to the comparison of the two multiplicities. Induction proves that the final selected multiplicity is at least every listed multiplicity. This gives the exact specialization from a finite nonempty set with positive multiplicities to the supplied-maximum theorem; it is not a declaration present in the assigned file.

### 2.3 Empty index, zero depth, and numerical `localOrder`

If `ι` is empty, there is exactly one exponent function and exactly one function of each of the witness types. All coordinate conditions are vacuous, and every sum is zero. Consequently

\[
\operatorname{Admissible}(m,r,a)\iff 0<r
\iff \sum_i a_i/m_i<r.
\]

For positive depth the sole degree is zero. `degree_le` remains valid because its right side is `(r-1)M≥0`, but it need not be sharp for an arbitrary supplied `M`. For example, with the empty index type, `r=2`, and `M=1`, the degree is zero and the ceiling is one. Neither attainment theorem can be instantiated because it requires `j : ι`. Thus there is no false empty-index attainment theorem in this file.

At `r=0`, admissibility is impossible for every index type because a natural-number sum cannot be negative. The floor-sum hypothesis is likewise impossible. The bound is therefore vacuous; the attained theorems correctly require `0<r`. The definitions still have values at `r=0` because natural subtraction is total. Those values by themselves have no nilpotency interpretation.

For fixed `M` and positive `r`, `r=(r-1)+1`, so `rM=(r-1)M+M`. Substitution into the two `localOrder` expressions proves the step identity without any assumption on multiplicities. Its `0<r` hypothesis is significant: at `r=0`, both `localOrder m 0 M` and `localOrder m 1 M` equal `A+1`, whereas the proposed right side with an added `M` equals `A+1+M` and fails when `M>0`.

The empty-coordinate polynomial model, if separately defined, is `C` with the zero ideal and `N=0`; its maximal surviving degree is zero and the least positive power killing `N` is one. This follows because there is only the constant monomial, `1≠0` in `C`, and `N^1=0`. It is distinct from the empty-root-packet model in the note, where `k≥1`, `h=1`, and the ideal generated by the `h(s_i)` is the whole polynomial ring. In the latter model, one generator is already `1`, every positive ideal power is the whole ring, and the quotient is zero. The file and checker should not be cited as identifying these two boundary cases.

## 3. Exact algebraic connection to the written claim

Research-note lines 71–101 restrict the local application to a finite root packet, positive multiplicities, `k≥1`, and `r≥1`, over `C`. Lines 85 and 164 expressly locate the monomial-basis and multinomial identifications in the written argument. The opening Lean comment, lines 8–9, makes the same distinction. The following direct calculation verifies the local connection used by that scope statement; none of the additional ring objects below is a declaration of `SplitZeroCyclicDepth.lean`.

Let

\[
P=\mathbf C[y_1,\ldots,y_k],\quad J=(y_1^{m_1},\ldots,y_k^{m_k}),\quad
m_i\ge1,\quad r\ge1.
\]

Expanding products of the given ideal generators shows that `J^r` is generated by the monomials

\[
y_1^{m_1b_1}\cdots y_k^{m_kb_k},\qquad
b_i\in\mathbf N,\quad \sum_i b_i=r.
\]

Both inclusions are explicit. Each displayed monomial is a product of `r` selected generators, hence belongs to `J^r`. Conversely, expand a product of `r` finite linear combinations of generators; every summand is a polynomial multiple of one displayed monomial, and finite sums of such products generate `J^r`.

A monomial `y^a` is divisible by one displayed generator exactly when there exist `b_i≤⌊a_i/m_i⌋` with total `r`. Such `b` necessarily implies `∑⌊a_i/m_i⌋≥r`. For the converse, place `q_i=⌊a_i/m_i⌋` and start with remaining amount `R_0=r`; define `b_i=min(q_i,R_{i-1})` and `R_i=R_{i-1}-b_i`. Induction gives `R_i=max(0,r-∑_{j≤i}q_j)`. The assumed sum inequality makes `R_k=0`, so the resulting `b_i` have total `r` and the required bounds.

Because the ordinary polynomial monomials are linearly independent over `C`, the polynomial multiples of the displayed generators span exactly the monomials satisfying this divisibility criterion. A polynomial belongs to `J^r` precisely when all of its monomials with nonzero coefficients satisfy it. Therefore the quotient classes of

\[
\{y^a:\ \sum_i\lfloor a_i/m_i\rfloor<r\}
\]

are a basis of `P/J^r`: they span by deleting the complementary monomials, and a linear combination of them in the ideal has every coefficient zero. This proves the exact equivalence between the formal floor condition and surviving basis monomials in this polynomial quotient.

For the original root coordinates, retain the shift `y_i=s_i-ρ_i` and write the complete packet polynomial exactly as in the note. Then

\[
h(\rho_i+y_i)=y_i^{m_i}u_i(y_i),\qquad
u_i(y_i)=\prod_{\rho\ne\rho_i}(\rho_i+y_i-\rho)^{m_\rho},
\quad u_i(0)\ne0.
\]

In the local ring `C[y_1,…,y_k]_(y_1,…,y_k)`, every `u_i` is a unit. Hence the ideals generated by the shifted `h(s_i)` and by the `y_i^{m_i}` are equal there, as are their `r`th powers. This is an equality in the stated local ring; it does not assert that `u_i` is a unit in the unlocalized polynomial ring.

The natural map from `P/J^r` to its localization at the zero-coordinate maximal ideal is an isomorphism. To prove this directly, observe that `y_i^{rm_i}=0` in the quotient for every `i`. Every monomial of degree `1+∑_i(rm_i-1)` consequently has some exponent at least `rm_i`, so the ideal generated by the coordinate classes is nilpotent. Any polynomial with nonzero constant term has class `c(1+v)` with `c≠0` and nilpotent `v`; its inverse is `c^{-1}∑_{j=0}^{B-1}(-v)^j` once `v^B=0`. Thus every element inverted by localization was already a unit, yielding the inverse homomorphism by these explicit inverses. Combined with the coordinate shift and the equality of localized ideals, this identifies the local original quotient with the monomial quotient used by the floor predicate.

Put

\[
d=\sum_i(m_i-1)+(r-1)\max_i m_i,\qquad N=\sum_i y_i.
\]

The attained-degree proof shows that every monomial of total degree `d+1` is in `J^r`. Expanding `N^{d+1}` therefore gives zero in the quotient. For the explicitly attained exponent `a` of total degree `d`, the coefficient in `N^d` is the positive integer

\[
\binom{d}{a_1,\ldots,a_k}=\frac{d!}{a_1!\cdots a_k!}.
\]

This formula counts the choices, in an ordered product of `d` factors `y_1+…+y_k`, of which `a_i` positions contribute `y_i`; it is nonzero in `C`. The surviving basis class `y^a` cannot be canceled by a different monomial, so `N^d≠0`. Consequently the least positive exponent annihilating `N` is exactly `d+1`: an earlier vanishing power would force `N^d=0` by multiplying by the remaining power. This includes `d=0`, where `N^0=1≠0` and `N=0` in the quotient. Characteristic zero matters for this argument; for example, over `F_2` with `m=(2,2)` and `r=1`, `(y_1+y_2)^2=y_1^2+2y_1y_2+y_2^2=0` modulo `(y_1^2,y_2^2)` although the maximum surviving total degree is two.

The local dimension follows from the explicit bijection `a_i=m_iq_i+t_i` with `0≤t_i<m_i` and `∑q_i≤r-1`. Remainders give `∏m_i` choices. Appending `q_{k+1}=r-1-∑_{i=1}^kq_i` identifies the possible `q` with `(k+1)`-tuples of nonnegative integers of sum `r-1`. Encoding such a tuple as `r-1` identical stars separated into `k+1` blocks by `k` bars gives exactly `binom(k+r-1,k)` strings, since the positions of the bars determine the tuple. The dimension is therefore `(∏m_i)binom(k+r-1,k)`. Neither this dimension formula nor the nilpotency proof is formalized in the assigned Lean file.

## 4. Complete finite-checker audit

### 4.1 Representation and exact arithmetic

`survivors` (lines 17–21) explicitly rejects empty multiplicity tuples, nonpositive depths, and nonpositive multiplicities. For valid inputs, it enumerates each coordinate in `0,…,rm_i-1` and retains the floor-sum predicate. This rectangle contains every survivor because a survivor has `⌊a_i/m_i⌋≤∑_j⌊a_j/m_j⌋<r`, hence `a_i<rm_i`. The enumeration is exhaustive for its input, not a sampled subset of its local basis.

`multiply_sum` (lines 24–31) represents a polynomial by a dictionary from exponent tuples to integer coefficients. It increments each coordinate once, adds coefficients at equal resulting tuples, and deletes monomials whose floor sum reaches `r`. By the monomial-ideal calculation above, this computes multiplication by `N` in that finite local quotient. All inputs used by the tests have the correct exponent-vector length and positive multiplicities. The routine is not a validated general-purpose public API for malformed tuples.

`actual_order` (lines 34–43) starts from the constant polynomial one, repeatedly calls this multiplication, and reports the first zero power. It does not invoke `predicted_order`. Its emergency termination bound is generous: every survivor has degree at most `∑(rm_i-1)`, so multiplication must yield zero by step `1+∑(rm_i-1)`, which is at most the checked limit `1+∑rm_i`. This argument uses only the enumerated rectangle and does not presuppose the sharp formula being tested.

`predicted_order` is the claimed expression. `orders` obtains collision exponents by applying that expression to every ordered packet tuple, summing its root values, and retaining the largest expression at a repeated sum. `annihilator` multiplies the corresponding linear factors using `Fraction` coefficients. Polynomial coefficient arrays are in increasing degree order; `trim` removes highest trailing zeros, `pmul` uses convolution, `derivative` multiplies each degree-`i` coefficient by `i`, and `remainder` performs ordinary leading-coefficient elimination. For the nonempty arrays and nonzero denominators used here, these are exact rational polynomial operations. No floating-point operations occur in these executions.

The top-coefficient test divides `d!` successively by the coordinate factorials using integer `//`. This does not truncate a fractional intermediate value. After a subset of coordinates with total `s≤d` has been processed, the quotient is

\[
\frac{d!}{\prod_{i\ \mathrm{processed}}a_i!}
=\frac{d!}{(d-s)!\prod_{i\ \mathrm{processed}}a_i!}(d-s)!,
\]

an integer by the same multinomial counting argument. Thus every successive division is exact.

### 4.2 Every test domain

| Method and source lines | Exact finite domain and comparison | Passing assertion invocations |
|---|---|---:|
| 01, 94–99 | `k∈{1,2,3}`, `m∈{1,2,3}^k`, `r∈{1,2,3}`: 117 inputs; maximum degree of the full enumerated basis versus predicted order minus one. | 117 |
| 02, 101–105 | Same 117 inputs; repeated local polynomial multiplication versus predicted order. | 117 |
| 03, 107–117 | `m=(1,1),(2,2),(2,3),(3,1,2)`, `r=1,2,3`: 12 inputs; explicit attaining monomial coefficient and its positivity. | 24 |
| 04, 119–121 | Packet `[(0,5),(1,4),(2,1)]`, `k=2`, sum value two, and depths one through five; one list comparison. | 1 |
| 05, 123–128 | Packet `[(0,2)]`, `k=2`, depths one through four; compares predicted order to `2r+1` and to `3r`. | 11 |
| 06, 130–137 | Packets `[(0,2)]`, `[(0,1),(1,2)]`, `[(0,2),(1,1),(2,2)]`; `k=1,2,3`; `r=1,2,3`: 27 inputs. Checks `chi_r` divides `chi_(r+1)` and its derivative. The latter polynomial is constructed at depth four when `r=3`. | 54 |
| 07, 139–148 | Empty packet with `k=1,2,3` and `r=1,2,3`: nine inputs, each checking annihilator one and a fixed remainder modulo one; then three assertions about a locally defined marker function. | 21 |
| 08, 150–156 | `m=(1),(2),(2,3),(2,1,3)`, depths one through four: 16 inputs; survivor count versus the dimension formula. | 16 |
| Total | Eight test methods, with the parameter loops above. | 361 |

The 117 count is `3(3+9+27)`. The assertion total is `117+117+24+1+11+54+21+16=361`. The JSON `tests_run` field counts methods, so eight is the correct default value. Research-note line 5's separately reported 24-method checker refers to a different upload; it cannot be used as the method count of this source.

For test 04, the sum-two tuples have multiplicities `(5,1)`, `(4,4)`, and `(1,5)`. The two distinct formulas are `1+(5-1)+(1-1)+(r-1)5=5r` and `1+(4-1)+(4-1)+(r-1)4=4r+3`. Their maximum is `7,11,15,20,25` at the five stated depths. They tie at depth three; the maximizing type is `(4,4)` before the tie and `(5,1)` or `(1,5)` after it. This test evaluates predicted exponents for multiplicities four and five. Those larger-multiplicity examples are not part of the direct local-multiplication range of test 02.

Test 05 has `m=(2,2)`, hence the predicted local order is `1+1+1+(r-1)2=2r+1`. The first-depth order is three, and `3r-(2r+1)=r-1`, proving the stated comparison and strict inequality at every tested `r>1`. Its computation uses the prediction through `orders`; it is not an additional direct nilpotency experiment.

### 4.3 Coverage boundaries that must remain explicit

1. The collision and annihilator helpers are built from `predicted_order`. Their output is not an independent construction of the ambient quotient's minimal polynomial. Test 06 checks exact divisibility of the constructed polynomials; it does not itself prove the universal Chinese-remainder or minimal-annihilator identification in research-note lines 105–114.
2. Test 06 does not test general divisibility `chi_r | chi_1^r`. Test 05 calibrates its exponent inequality for one root packet. It also does not test surjectivity or kernel dimensions of derivative quotient maps, equivariant retractions, Gram forms, or trace comparisons.
3. The empty-packet branch is genuinely exercised with positive coordinate count: `product([],repeat=k)` is empty for each tested `k≥1`, so `orders` returns an empty dictionary and `annihilator` retains its initialized constant polynomial one. This matches the whole-ideal arithmetic boundary. It never evaluates a maximum over an empty root-tuple family.
4. An empty coordinate tuple is outside the declared test domain. `survivors((),r)` explicitly rejects it; `predicted_order((),r)` reaches `max(())` and raises `ValueError`; `orders(packet,0,r)` reaches the latter case through the single empty ordered tuple. Meanwhile `actual_order((),r)` would return one because its first multiplication has no coordinate contributions. This difference is an unsupported-input boundary, not a failing case in the tested positive-coordinate domain. A claim that this checker verified `k=0` would be false.
5. Lines 144–148 introduce `tau=object()` and a new local `split_zero` function. The three checks prove the behavior of that marker fixture only. They do not import or execute the original scalar construction, a quotient morphism, or an analytic seed. The repeated remainder check modulo `[1]` is the same rational polynomial calculation repeated nine times.
6. The checker makes no computations about actual zeta zeros, analytic integrals, moment enclosures, a tensor-uniform estimate, or an infinite family of degrees. Its header and emitted scope string correctly restrict it to exact finite calibrations.

## 5. Research-note claim map and disposition

| Research-note claim | Evidence supplied by these assigned sources |
|---|---|
| Lines 79–85: exact local degree bound and explicit attained vector | Directly represented by the Lean predicates, bound, witness, and floor-sum attained theorem, with finite indexing, positive multiplicities/depth, and a supplied maximizing coordinate. |
| Lines 75–77 and 87–101: original local quotient basis, exact nilpotency, and dimension | Written algebraic connection; independently reconstructed in Section 3 above. Finite basis, nilpotency, coefficient, and dimension calibrations occur in Python. They are not additional Lean claims in this file. |
| Lines 105–138: collided annihilator, divisibilities, quotient-map surjectivity, derivative kernels | Python calibrates selected predicted collisions and exact transition/derivative divisibilities. It does not formalize these general statements or independently construct the global ambient minimal polynomial. |
| Line 140: empty packet `h=1` | Python checks annihilator one and a marker fixture at positive `k`. The independent polynomial calculation gives the whole ideal because its generators equal one. Empty-index attainment is a different matter. |
| Lines 144–158: retraction, complement, and trace distinctions | No declaration or test in the two assigned code files proves these statements. They are explicitly identified as written work in the note. This bounded audit does not claim a full audit of those sections. |
| Lines 16–67: conormal maps, evaluation injection, derivative square, and unit rule | These refer to the other named Lean module, which was outside this subtask's assigned code audit. |
| Line 168: pinned build, warning policy, trust setting, inherited modules, and axiom audit | Reproduction instructions in the note. No fresh Lean or workflow result was produced by this subtask, and this report does not authenticate that separate workflow claim. |

The phrase “all-index, all-depth” at note line 85 is accurate only with its immediately preceding mathematical hypotheses: arbitrary finite positive coordinate count, positive multiplicities, and positive depth, with the maximum attained at some coordinate. It must not be expanded to infinite indices, a maximum of an empty coordinate set, zero-depth attainment, or a formally certified polynomial nilpotency theorem.

No source repair is required by this bounded audit. The report's acceptance is precisely for the displayed natural-number theorems at source level and the replayed finite checker within its recorded domains. Original files, cumulative artifacts, and releases remain untouched.
