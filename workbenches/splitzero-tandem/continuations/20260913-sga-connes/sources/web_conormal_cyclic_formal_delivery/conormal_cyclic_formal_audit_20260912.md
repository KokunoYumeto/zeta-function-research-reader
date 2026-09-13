# Conormal and cyclic formal continuation: exact source and execution audit

Audit date: 12 September 2026. This report reads the delivered mathematical report, every one of the eight added source files, the inherited quotient implementation and checking parser, and the exact completed GitHub job. It performs no local Lean, Lake or Elan execution. Repository and CI facts below are observed facts at the retrieval time recorded in `LOCAL_STAGING_PROVENANCE.json`; later changes to the open pull request do not alter this pinned edition.

## 1. Pinned contribution and preserved evidence

The source is [draft PR 21](https://github.com/KokunoYumeto/zeta-function-research-reader/pull/21), at implementation commit `2abc351424ba87aeda948a5cfb846e15ed9373d1`, based on `4c5ce7a8575fa8b95df272116eb5783b2309cdb7`. The observed PR is open, draft and unmerged. The source tree comparison establishes exactly eight additions, zero modifications and zero deletions. All 2,030 inherited Git blobs agree with the base tree; the head contains 2,038 blobs. This is a byte-preservation result. It does not extend the mathematical audit to every inherited reader page.

The exact eight source files are retained below `sources/web_conormal_cyclic_formal_delivery/repository/`:

| Repository path | Role |
| --- | --- |
| `.github/workflows/splitzero-conormal-cyclic.yml` | Actual CI commands and pinned environment |
| `formal/splitzero/CONORMAL_CYCLIC_TARGETS.json` | Exact selected declaration names |
| `formal/splitzero/SplitZeroConormalTower.lean` | Original quotient derivative and cyclic comparison |
| `formal/splitzero/SplitZeroCyclicDepth.lean` | All finite-index degree bound and attainment |
| `formal/splitzero/check_conormal_cyclic.py` | Source scan, audit source construction and inherited report parser |
| `workbenches/tau-conormal-cyclic-formal/COORDINATION.md` | Dated source and scope record |
| `workbenches/tau-conormal-cyclic-formal/RESEARCH_NOTE.md` | Complete accompanying written argument |
| `workbenches/tau-conormal-cyclic-formal/check_depth_models.py` | Eight finite regression methods |

Each file was fetched as a Git blob, base64 decoded, and checked against its Git blob SHA1 with the literal `blob <byte-count>\0` header. Its bytes, SHA256, original path and Git blob identifier appear in `LOCAL_STAGING_PROVENANCE.json`. Thirteen additional inherited files are retained under `inherited_dependencies/` with separate `DEPENDENCY_SOURCE_PROVENANCE.json`; these are dependency witnesses, and are not counted among the eight additions.

The completed verification is [run 34717443909, job 103617105475](https://github.com/KokunoYumeto/zeta-function-research-reader/actions/runs/34717443909/job/103617105475). Both API responses identify the exact implementation commit above and report `completed` / `success`. The job ran from `2026-09-12T20:33:26Z` to `2026-09-12T20:39:34Z`. The downloaded raw job log contains 137,155 bytes. The exact raw API responses, both recursive Git trees, the raw job log, a timestamp-stripped reading copy, parsed JSON reports and a read-only verification receipt are retained under `evidence/`.

The timestamp-stripped copy preserves one line per original log line. The following locators are therefore valid in both log editions:

| Lines | Observed evidence |
| --- | --- |
| 107 and 119 | Checkout identifies the exact implementation commit |
| 243–245 and 273–275 | Twenty-five inherited harness tests pass in normal and optimized Python |
| 304–306 and 318–320 | Eight new finite methods pass in both Python modes |
| 322–325 | Both deliberate-failure invocations produce the specified failure |
| 341 | Original SplitZero core blob `ff991f7383922e71cdf0e4a3bc85e89e18f808ef`, 7,366 bytes, verified |
| 345 | Lean 4.31.0, Lean commit `68218e876d2a38b1985b8590fff244a83c321783` |
| 411–412 | Both new modules reached the separate strict source-check loop |
| 465–608 | Parsed 29-target new transitive report, including exact source SHA256 values |
| 609–816 | Successful 40-target frontier report |
| 817–1159 | Successful 68-target boundary-integration report |
| 1160–1354 | Successful 38-target boundary report |
| 1355–1767 | Successful 87-target tau recovery report |
| 1781–2136 | Successful 73-target derived report |
| 2137 | Structural checker reports 28 selected declarations and only standard axioms |

The new 29-target report is checked twice at different levels: the actual remote workflow accepted it, and this audit imported the exact inherited Python `audit` function and applied it to the downloaded raw Lean reports. Every expected name occurs exactly once, no unexpected name is accepted, and every axiom set is contained in `{propext, Classical.choice, Quot.sound}`. The parsed new JSON report agrees with those raw reports and its two source SHA256 values agree with the downloaded module bytes. The 68-target report's complete name set agrees with the exact inherited `BOUNDARY_INTEGRATION_TARGETS.json`. Counts include definitions and supporting declarations, may overlap between audits, and are not counts of independent mathematical discoveries.

## 2. What the workflow actually checks

The workflow installs `leanprover/lean4:v4.31.0` from the unchanged toolchain file. Its `lakefile.toml` requires Mathlib commit `fabf563a7c95a166b8d7b6efca11c8b4dc9d911f`, and the workflow explicitly compares the checked-out Mathlib HEAD to that value after `lake update`. It pins the checkout action and elan installer revision. The inherited `prepare.py` verifies the original SplitZero core Git blob before materializing it.

The existing default Lake targets are built. The generated tau recovery, boundary, boundary-integration and frontier module lists are then checked explicitly. Both new modules are checked separately with `lake env lean --trust=0 -DwarningAsError=true`, writing their `.olean` outputs. A failure in either source sets the step's exit status to failure. The next step imports the union of the old and new module lists in one Lean environment and executes the selected transitive reports with the same strict flags. Shell `set -euo pipefail` makes failure of Lean in the reporting pipeline visible despite the use of `tee`.

The new preflight removes nested Lean comments and rejects the tokens `sorry`, `admit`, `axiom`, `unsafe`, `implemented_by`, and `native_decide` in the resulting source text. It also checks the manifest's module names and target names, rejects empty or duplicate target entries, hashes both source modules, writes their module list, and constructs the `#print axioms` source. The inherited parser requires exact equality of the observed and expected report-name sets, rejects duplicate reports, and rejects every axiom outside the three-element allowed set. These are source and selected-transitive-report checks; no analytic theorem gains a certificate merely because its prose is stored alongside these files.

The exact workflow's remote runner uses two Lean threads and `maxJobs=2`. This audit records that remote setting without adopting it as a local resource policy. No local Lean run was started.

## 3. The original derivative: exact types and complete mathematical verification

Let \(R,A\) be commutative rings, let \(A\) be an \(R\)-algebra, let \(I\subseteq A\) be an ideal, and let \(D:A\to A\) be an \(R\)-derivation. Write

\[
L_r=\operatorname{Res}_R(I^r)\subseteq_R A,
\qquad q_r:A\longrightarrow A/L_r.
\]

`level` at line 20 is exactly this restricted-scalar submodule. There is no closure operation and no derivative-stability hypothesis on \(I\).

For every \(r\ge0\), \(D(I^{r+1})\subseteq I^r\). For \(r=0\), \(I^0=A\), so the assertion holds. Suppose the assertion has been proved at \(r\). An element of \(I^{r+2}=I^{r+1}I\) is an additive combination of products \(ab\) with \(a\in I^{r+1}\) and \(b\in I\). The Leibniz identity is

\[
D(ab)=aD(b)+bD(a).
\]

The first term belongs to \(I^{r+1}\) because it is a multiple of \(a\); the induction hypothesis puts \(D(a)\) in \(I^r\), and therefore the second term belongs to \(II^r=I^{r+1}\). Additivity proves the induction step. The actual proof at lines 24–44 uses ideal-product induction with precisely these two terms. It assumes neither squarefreeness nor characteristic zero.

The induced coefficient-linear map is

\[
\delta_r:A/L_{r+1}\longrightarrow_R A/L_r,
\qquad q_{r+1}(x)\longmapsto q_r(Dx).
\]

Changing \(x\) by \(z\in I^{r+1}\) changes \(Dx\) by \(Dz\in I^r\), so the displayed map is well-defined. `descended` at line 47 reuses the merged `SplitZero.RelationLayer.derivative`, whose literal implementation is `U.mapQ W D hD`. Its representative equation is `descended_mk` at line 52.

The quotient transition is

\[
p_r:A/L_{r+1}\longrightarrow_R A/L_r,
\qquad q_{r+1}(x)\longmapsto q_r(x).
\]

The inclusion \(I^{r+1}\subseteq I^r\) proves well-definedness. `projection` at line 57 uses the inherited `transport`, whose literal implementation is `U.mapQ W LinearMap.id h`. Both composites from \(A/L_{r+2}\) to \(A/L_r\) send the representative \(x\) to \(q_r(Dx)\). Every quotient element has a representative, hence

\[
p_r\circ\delta_{r+1}=\delta_r\circ p_{r+1}.
\]

This is `tower_square` at line 65. The exact relation between the different source and target quotients is thus an implemented commuting square, with the representative maps specified above.

For \(z\in I\) and \(a\in A\), the first Leibniz term \(zD(a)\) belongs to \(I\). Therefore

\[
\delta_1(q_2(za))=q_1(aD(z)).
\]

This is `conormal_product` at line 74. For arbitrary \(u,x\in A\), both terms remain at the target level:

\[
\delta_r(q_{r+1}(ux))=q_r(uD(x))+q_r(xD(u)).
\]

This is `multiplier_rule` at line 89. It holds for every \(u\); being an arithmetic Taylor unit is a specialization, not an extra assumption built into the formal statement. The statement proves an equality in \(A/L_r\). It does not assume a cyclic-image condition on its second term.

## 4. Cyclic evaluation and its exact algebra comparison

Fix \(S\in A\) and let \(v_S:R[X]\to_R A\) be the coefficient-linear map underlying polynomial evaluation. The source defines

\[
K_r=v_S^{-1}(L_r),\qquad
C_r=R[X]/K_r.
\]

`cyclicLevel` at line 106 is exactly the submodule `comap` above. In particular, it pulls back the actual ideal power \(I^r\) at every \(r\). It never constructs \(K_1^r\).

The checked injection is

\[
\alpha_r:C_r\longrightarrow_R A/L_r,
\qquad [P]\longmapsto[P(S)].
\]

If two image classes agree, \(P(S)-Q(S)\in I^r\). Evaluation is additive, so \((P-Q)(S)\in I^r\); this means \(P-Q\in K_r\), which is precisely equality of the two source classes. This proves injectivity without requiring injectivity of \(v_S\) on \(R[X]\). The proof is implemented at lines 120–130 by the two quotient equality criteria. Its image is exactly the coefficient submodule of classes represented by polynomials in \(S\).

There is also an exact algebra map connecting the implemented module carrier to the ordinary quotient algebra. Let

\[
\mathfrak K_r=(I^r).\operatorname{comap}(\operatorname{aeval}_S)
\]

as an ideal of \(R[X]\). Membership of \(P\) in its underlying \(R\)-submodule is the same statement \(P(S)\in I^r\), so this submodule equals \(K_r\). The maps from the submodule quotient to the underlying module of \(R[X]/\mathfrak K_r\), and back, send the class of \(P\) to the class of the same \(P\). They are well-defined by that membership equality and inverse because every class has a representative. The same construction identifies \(A/L_r\) with the underlying \(R\)-module of the ideal quotient \(A/I^r\). Under these explicit identity-on-representative identifications, the algebra homomorphism

\[
\bar\alpha_r:R[X]/\mathfrak K_r\longrightarrow_{R\text{-alg}} A/I^r,
\quad[P]\longmapsto[P(S)]
\]

has underlying linear map exactly `evaluation`. It is multiplicative because \((PQ)(S)=P(S)Q(S)\), fixes the coefficient image, and sends \([1]\) to \([1]\). These equations give the full typed bridge. The new Lean file bundles the linear map; this algebra-homomorphism packaging and the carrier identifications in this paragraph are written mathematics, not extra Lean declarations in this run.

Now assume the explicit algebraic condition \(D(S)=1\). An \(R\)-derivation annihilates coefficient images. Induction using Leibniz gives \(D(S^n)=nS^{n-1}\), including \(n=0\), and finite additivity gives

\[
D(P(S))=P'(S).
\]

`polynomial_chain_rule` at line 132 proves this by the exact Mathlib `map_aeval` identity. If \(P\in K_{r+1}\), the ideal-power theorem gives \(D(P(S))\in I^r\), so \(P'\in K_r\). Consequently

\[
\partial_r:C_{r+1}\longrightarrow_R C_r,
\quad[P]\longmapsto[P']
\]

is well-defined. It is `cyclicDerivative` at line 139. Both paths from \(C_{r+1}\) to \(A/L_r\) send \([P]\) to \([P'(S)]\), proving the implemented equation

\[
\delta_r\alpha_{r+1}=\alpha_r\partial_r.
\]

This is `cyclic_square` at line 156. Combining the two preceding proved identities gives `cyclic_unit_rule` at line 168:

\[
\delta_r([uP(S)])=[uP'(S)]+[P(S)D(u)].
\]

Its source representative is in \(A\), and its two summands are classes in the ambient target \(A/I^r\). The declaration requires no claim that \(P(S)D(u)\) is represented by a polynomial in \(S\).

For the intended specialization \(A=\mathbb C[s_1,\ldots,s_k]\), \(k\ge1\), put \(S=\sum_i s_i\) and \(D=(1/k)\sum_i\partial_{s_i}\). Then \(D(S)=(1/k)\sum_i1=1\). This elementary specialization proves the required condition over \(\mathbb C\), retaining the original factor \(1/k\). The particular multivariable instance, its relation ideal, Taylor units, and supported diagrams are not new bundled instantiations in these two modules. The separate scaling operator on the analytic source keeps its own definition; no equality with this polynomial sum-direction derivation is asserted by the certificate.

## 5. Full ideal, empty packet, and the supported lift

`top_level_zero` at line 97 proves

\[
q_r^{\top}(x)=0\quad(r\ge0,\ x\in A),
\qquad q_r^{\top}:A\to A/\operatorname{Res}_R(\top^r).
\]

Indeed \(\top^r=\top\), including \(r=0\), and every representative belongs to the relation submodule. Since every quotient element has a representative, the quotient is the zero module. The unique map from it to the zero module and the map sending zero to its zero class are inverse linear maps. This gives the exact quotient-to-zero identification, rather than an informal dimension argument.

For the empty packet \(h=1\) and \(k\ge1\), each polynomial generator \(h(s_i)\) is the literal element \(1\). Hence \(I=(1,\ldots,1)=P\), and all positive powers equal \(P\). Thus the generic full-ideal theorem applies. The preimage under polynomial evaluation of the entire ring is all of \(\mathbb C[X]\); the cyclic quotient is zero as well. These are direct written specializations of the generic checked statement. No positive-degree remainder basis is invoked at \(d=0\).

The supported lift of the quotient-to-zero map remains explicitly

\[
G(q)(\tau)=\tau,\qquad G(q)(x^\bullet)=0^\bullet=e.
\]

After applying the inverse linear identification of the zero quotient with \(0\), this gives the bijection of supported carriers \(G(P/I^r)\cong G(0)=\{\tau,e\}\). The inverse sends \(\tau\) to external absence and \(e\) to the supported zero class. Both composites fix each of these two constructors, so they remain distinct. This written constructor calculation explains exactly how the vanishing arithmetic module relates to its supported lift. The new `top_level_zero` declaration itself concerns underlying quotient modules; the established SplitZero library supplies the supported constructors. Neither the analytic theta seed nor its mass appears in the theorem statement, and no new vanishing assertion about those analytic objects follows from it.

## 6. Degree theorem, nilpotency bridge and collision formula

The companion `SplitZeroCyclicDepth.lean` works with an arbitrary finite index type \(\iota\). Its `Admissible` predicate is the existence of quotient and remainder functions \(q,t:\iota\to\mathbb N\) with

\[
a_i=m_iq_i+t_i,\quad t_i<m_i,\quad\sum_iq_i<r.
\]

For positive \(m_i\), Euclidean division proves its equivalence with \(\sum_i\lfloor a_i/m_i\rfloor<r\). `degree_le` assumes only the specified bound \(m_i\le M\) and admissibility. Its admissibility witnesses already imply \(m_i>0\) through \(0\le t_i<m_i\), and \(r>0\) through \(0\le\sum_iq_i<r\). The declaration concludes

\[
\sum_i a_i\le\sum_i(m_i-1)+(r-1)M.
\]

To prove this, \(t_i<m_i\) gives \(t_i\le m_i-1\), while \(\sum_iq_i<r\) gives \(\sum_iq_i\le r-1\). Therefore

\[
\sum_i(m_iq_i+t_i)
\le\sum_i(Mq_i+m_i-1)
=M\sum_iq_i+\sum_i(m_i-1)
\le M(r-1)+\sum_i(m_i-1).
\]

For attainment the declaration supplies an index \(j\in\iota\) with \(m_i\le m_j\) for every \(i\). Its explicit exponent function is

\[
a_i=(m_i-1)+\begin{cases}m_i(r-1)&i=j,\\0&i\ne j.\end{cases}
\]

Use \(q_j=r-1\), all other \(q_i=0\), and \(t_i=m_i-1\). This is admissible and has degree \(\sum_i(m_i-1)+(r-1)m_j\). `attained_maximum` at line 97 and `floor_attained_maximum` at line 106 prove admissibility, exact attained degree and the universal upper bound. The supplied index \(j\) records nonemptiness when attainment is asserted. Bounds and Euclidean equivalence make sense for an empty finite type; the file does not claim an attained positive-index maximum for an empty tuple or define a maximum of an empty root set.

The numerical definition `localOrder` at line 117 is the ceiling plus one; `localOrder_step` at line 119 proves that this number increases by the supplied \(M\) when the positive depth increases by one. There is no polynomial quotient, multiplication operator, nilpotency predicate, Chinese-remainder map or \(\chi_r\) declaration in that Lean file.

The exact written bridge to nilpotency is as follows. In

\[
B_{\mathbf m,r}=\mathbb C[y_i:i\in\iota]/(y_i^{m_i}:i\in\iota)^r,
\]

the relation ideal is a monomial ideal generated by \(\prod_i y_i^{m_iq_i}\) with \(\sum_iq_i=r\). A monomial \(y^a\) belongs to it precisely when some such generator divides it. This is equivalent to being able to choose \(q_i\le\lfloor a_i/m_i\rfloor\) with sum \(r\), and hence equivalent to \(\sum_i\lfloor a_i/m_i\rfloor\ge r\): for the reverse direction, allocate \(r\) units successively among these finite nonnegative capacities. Monomials are a vector-space basis of the polynomial ring; a monomial ideal is the span of its divisible monomials. Consequently the complementary monomials with floor-sum \(<r\) give a basis of the quotient.

For a nonempty finite index set and positive multiplicities, set

\[
L_r=1+\sum_i(m_i-1)+(r-1)\max_i m_i,
\qquad N=\sum_i y_i.
\]

Every monomial in \(N^{L_r}\) has total degree \(L_r\), greater than the proved ceiling, and is therefore zero in the quotient. The attaining exponent at degree \(L_r-1\) survives. Its coefficient in \(N^{L_r-1}\) is the exact nonzero characteristic-zero integer

\[
\frac{(L_r-1)!}{\prod_i a_i!}.
\]

Distinct surviving basis monomials are linearly independent. Thus \(N^{L_r-1}\ne0\), and its nilpotency index is exactly \(L_r\). This is a complete written consequence of the checked combinatorial maximum and the explicitly proved quotient-basis map. It is not an additional kernel-checked polynomial theorem.

For the original nonempty packet polynomial \(h=\prod_\rho(s-\rho)^{m_\rho}\), the local decomposition at a root tuple uses \(y_i=s_i-\rho_i\) and the literal factorization \(h(\rho_i+y_i)=y_i^{m_i}u_i(y_i)\), with \(u_i(0)\ne0\). In the local finite quotient each \(u_i\) is invertible, so its relation ideal is exactly the ideal generated by the \(y_i^{m_i}\). The decomposition over all root tuples transports multiplication by \(S=\sum_i s_i\) to \(\lambda+N\), where \(\lambda=\sum_i\rho_i\). The least exponent annihilating all components with the same \(\lambda\) is their maximum. Distinct \(\lambda\)-primary factors are relatively prime. Therefore

\[
\ker(\mathbb C[X]\xrightarrow{P\mapsto P(S)}P/I^r)
=(\chi_r),
\]
\[
\chi_r(X)=\prod_\lambda(X-\lambda)^{\ell_{\lambda,r}},
\quad
\ell_{\lambda,r}=
\max_{\rho_1+\cdots+\rho_k=\lambda}
\left(1+\sum_i(m_{\rho_i}-1)+(r-1)\max_i m_{\rho_i}\right).
\]

This identifies the implemented pullback quotient \(C_r\) with the underlying coefficient module of \(\mathbb C[X]/(\chi_r)\) by the map sending each polynomial class to itself. It is well-defined and inverse by the displayed kernel equality. The invariant target contains every polynomial in \(S\), and its inclusion in the full quotient is injective; therefore restricting the target to variable-permutation invariants leaves this kernel unchanged. These polynomial/localization/CRT identifications are complete written arguments in the source and audited here at their actual types, with no claim that the new Lean file contains them.

For one tuple the slope \(\max_i m_i\) is at most its depth-one order \(1+\sum_i(m_i-1)\). It follows that \(\ell_{\lambda,r}\le r\ell_{\lambda,1}\), hence \(\chi_r\mid\chi_1^r\). The explicit quotient map

\[
\mathbb C[X]/(\chi_1^r)\twoheadrightarrow\mathbb C[X]/(\chi_r),
\quad[P]\longmapsto[P],
\]

is well-defined by this divisibility and is onto because every target polynomial class has the same representative in the source. Its kernel is the ideal \((\chi_r)/(\chi_1^r)\). For \(h=(s-\rho)^2\), \(k=2\), the two exponents are exactly \(2r+1\) and \(3r\), so this kernel has dimension \(r-1\) for \(r>1\). This proves the exact morphism relating the two quotients instead of drawing an unrelatedness conclusion from unequal exponents.

## 7. Retraction, including its retained multiplier and complement

The source gives a written proof of the module retraction. On a \(\lambda\)-primary space \(M\), let \(N=S-\lambda\), \(N^\ell=0\), and let \(w\) be the retained arithmetic unit's component. Its exact order gives \(N^{\ell-1}w\ne0\). Choose a coefficient functional \(\theta\) detecting this vector. Define

\[
\pi_0(v)=\sum_{j=0}^{\ell-1}\theta(N^{\ell-1-j}v)X^j
\pmod {X^\ell}.
\]

The constant term of \(\pi_0(Nv)\) is zero because \(N^\ell=0\). Its coefficient of \(X^j\), \(j\ge1\), is the coefficient of \(X^{j-1}\) in \(\pi_0(v)\); hence \(\pi_0(Nv)=X\pi_0(v)\). Put \(c=\pi_0(w)\). Its constant term is the nonzero scalar \(\theta(N^{\ell-1}w)\). Writing \(c=c_0(1+n)\) with \(n\in(X)\), the literal inverse is \(c_0^{-1}\sum_{j=0}^{\ell-1}(-n)^j\). Then \(\pi=c^{-1}\pi_0\) satisfies

\[
\pi(P(N)w)=P(X)\pmod {X^\ell}.
\]

For the injection \(\eta:P\mapsto P(N)w\), this is \(\pi\eta=1\). The exact inverse pair for the resulting module decomposition is

\[
v\longmapsto(\pi v,v-\eta\pi v),
\qquad(c,z)\longmapsto\eta c+z,
\quad z\in\ker\pi.
\]

Both composites are the identity by \(\pi\eta=1\), and the two maps commute with \(S\) because \(\pi\) and \(\eta\) do. If the original Hermitian form is retained, its value is

\[
\langle\eta c+z,\eta c'+z'\rangle
=\langle\eta c,\eta c'\rangle+\langle\eta c,z'\rangle
+\langle z,\eta c'\rangle+\langle z,z'\rangle.
\]

No term has been removed. This specifies the exact module and metric comparison furnished by the splitting. The retraction is written and audited mathematics; it is not a new Lean declaration in the checked modules.

## 8. Earlier uncompiled paste mapped to the checked source

The earlier full conormal pasted note remains preserved byte-for-byte as `sources/web_conormal_tower_paste/CONORMAL_TOWER_SOURCE.md`. Its embedded draft is extracted, with an explicit text-only extraction, to `evidence/EARLIER_UNCOMPILED_TOWER_DRAFT.lean`; the checked-source comparison is `evidence/EARLIER_DRAFT_TO_CHECKED_SOURCE.diff`. The extraction selects the code block containing `namespace SplitZero.ConormalTower`, not the earlier one-line interface illustration. The old paste remains a historical uncompiled witness. The following successor declarations are now supported by the exact completed remote run:

| Earlier draft declaration | Checked source line | Selected transitive report? |
| --- | ---: | --- |
| `level` | 20 | Yes |
| `deriv_mem_pow` | 24 | Yes |
| `descended` | 47 | Yes |
| `descended_mk` | 52 | Yes |
| `projection` | 57 | Yes |
| `projection_mk` | 62 | No; compiled in the complete module |
| `tower_square` | 65 | Yes |
| `conormal_product` | 74 | Yes |

The entire new ConormalTower file has 19 declarations. Sixteen are selected by its manifest; `projection_mk`, `evaluation_mk`, and `cyclicDerivative_mk` are the three additional compiled simp declarations. The CyclicDepth file has 13 selected declarations. Thus the reported selected total is exactly \(16+13=29\), while both full source files were checked.

The earlier note's other mathematics retains its written status: the monic freeness and graded-layer coordinates; the rank \(d^k-b^k\) and kernel \((k-1)d^k+b^k\) of the contracted conormal row; the dual-number first-jet algebra map; the all-coordinate jet kernel \(kbd^{k-1}\); symmetric conormal ranks; the product-Jacobian rank and nilradical; and the arithmetic residue trace. None of those assertions is a new declaration in these two files. Their earlier finite Wolfram execution report is also not retroactively reproduced by this GitHub run. The exact derivative theorem now supplies checked general infrastructure for those written calculations without changing their individual certification status.

## 9. Historical corrections and inherited audit scope

The source's first correction is verified against actual commit `600ab7a527f7a626c162bf0199d093d454b86c14`: its patch adds \(d\ge1\) to the monic-freeness argument and writes the empty-packet \(I=P\) case explicitly, preserving analytic amplitude and mass. GitHub's compare endpoint shows that commit is an ancestor of the exact checked head: merge base equals the correction commit and `behind_by=0`. The actual source patch and ancestry response are retained.

The second correction is verified against commit `7aec03a93b66d3d97fbf6f7042f58bb2c1019543`. Its patch changes the previous reader's 66-target account to the completed 68-target account, cites the successful corrected run, records the combined 40/68 integration, and keeps the frontier workflow active on relevant main pushes and pull requests. Its ancestry response likewise has the correction commit as merge base with `behind_by=0`. More directly, the newly downloaded job contains the full successful 68-target report, and this audit matches every report name to the inherited 68-target manifest. This is execution evidence, not merely an inherited prose correction.

Neither the existence of those ancestors nor the preservation of all old Git blobs independently checks the entire 292-page and 433-page publications. The note correctly retains that reading limitation. Its statement that it could not open the delivered cyclic ZIP is also preserved as dated provenance. The present parent integration's separate verified 43-member/24-method cyclic-delivery receipt closes that archive-replay task at its own source edition; it must be cited separately and must not be attributed to this remote Lean job.

## 10. Integration result and exact remaining certificate boundary

The checked contribution supplies the generic all-order ideal derivative, original quotient transitions, an injective cyclic comparison at every retained depth, the commuting derivative square, the full multiplier correction, the full-ideal vanishing statement, and the exact finite-index degree maximum with attainment. Its source and completed-run claims withstand the bounded audit above.

The new finite checker independently exercises explicit monomial quotient multiplication and the stated algebraic calibration packets. Its normal and optimized successful records agree: eight methods, 361 assertion invocations, no errors or failures. Each deliberate-failure run executes nine methods with exactly one failure and returns exit code one. The independent replay and complete method-by-method scope are recorded in `work/cyclic_depth_certificate_independent_review_20260912.md` and its linked receipt. The direct nilpotent-multiplication range is \(k\in\{1,2,3\}\), multiplicities in \(\{1,2,3\}^k\), and depths \(1,2,3\): 117 inputs. Collision-polynomial helpers use the predicted orders, so their exact divisibility calculations are not an independent ambient minimal-polynomial construction. The empty-packet test has positive \(k\); its supported-zero checks use a local marker fixture rather than importing the original SplitZero carrier. These remain finite regression checks with their actual domains retained.

The algebraic nilpotency, collided minimal polynomial, module splitting, particular Taylor-unit instantiation, supported-diagram instantiation, first-jet algebra packaging, conormal ranks and arithmetic trace calculations retain their complete written proof routes. The analytic convolution norm, differentiated moments, canonical arithmetic metric, rank-two spectral control and any tensor-uniform small-control estimate are outside these two Lean modules. This statement of scope does not discard a connection: Sections 3–7 provide the explicit quotient, evaluation, derivative, ideal-annihilator and module-splitting morphisms that join the new certificate to the current mathematical construction.
