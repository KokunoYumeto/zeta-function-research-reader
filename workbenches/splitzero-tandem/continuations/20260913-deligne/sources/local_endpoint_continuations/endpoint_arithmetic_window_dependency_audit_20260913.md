# Arithmetic endpoint and exact-window proof dependency audit

Prepared 2026-09-13 for the parent source-closure lane. This is a read-only proof-source audit and a written reconstruction of the dependency maps. No supplied checker, mathematical fixture, TeX build, Lean process, source integration, or publication was run. Source files were not edited. A byte-exact snapshot of the currently observed window checker was copied into the local work directory because its mutable path exposed different versions during the read.

The source root below is `F:/user/Documents/Papors/Chatnotes/Zeta-Function-Foundation/agents/zenodo_workspace_publication/integration_20260913_next`. The arithmetic note is at `arithmetic_endpoint_review/source_stage/Tau_Arithmetic_Endpoint_Bounds/NOTE.tex`; the shorter `source_stage/Tau_Arithmetic_Endpoint_Bounds/NOTE.tex` relative to the source root does not exist. The complete parent `FOUR_VOLUME_THRESHOLD.md` and the checker both explicitly identify the longer path.

## Complete readings and immutable identities

| Witness relative to source root | Complete lines read | Bytes | SHA-256 |
|---|---:|---:|---|
| `arithmetic_endpoint_review/BALANCED_WINDOW_PROOF.md` | 1–102 | 5891 | `a3bb84329d384071b4ac4829731e26dbe2586b719548a660bae6eefb34f5e00c` |
| `arithmetic_endpoint_review/REVIEW.md` | 1–64 | 10587 | `e292811220b91aef26e6c6e398b0bd427d5bbc33271f6ed01d60bc9d9831fd47` |
| `arithmetic_endpoint_review/source_stage/Tau_Arithmetic_Endpoint_Bounds/NOTE.tex` | 1–840 | 31714 | `f776e7934f026342f48732a74f14d57470b8aae1cef76ebdee5f831bd49dedf8` |
| `FOUR_VOLUME_THRESHOLD.md` | 1–239 | 7716 | `9ff55c84d74db85306e7a68c70fe7b08d8e642e8ac1a3e6137649f68e102fc3a` |
| `window_product_review/verify_window_product.py`, intermediate byte-preserved snapshot | 1–284 | 15691 | `5e3ef70b63cfb51aae2449142fca6ea2507f313a1a9a9a63adb11c0442f5fd99` |
| `window_product_review/verify_window_product.py`, subsequently read version | 1–295 | 16488 | `7c9b0d3a241c14a2ed08efbab1e06c89b7d48fc6d67118299d32a364819bf395` |

Every reading above covered the complete body, including source-boundary paragraphs, references, and ancillary transfer statements. The checker was read initially at its mutable source path and then completely again from the hash-pinned work snapshot. The accompanying JSON records the exact paths, byte counts, line ranges, equation locators, and explicit dependency edges. The separate `endpoint_window_receipt_dependency_audit_20260913.md` and JSON record the child's complete checker/receipt/reference inspection; none of its historical execution results is represented as a fresh run by this lane.

## Written witness chain for the four-volume result

The complete arithmetic note supplies the local analytic argument. Its equations (14)–(23), lines 253–367, prove local zeta mass by the fixed Joukowski ellipse, a nonzero value at `2+iT`, and the interval derivative estimate. Equations (24)–(29), lines 372–451, carry that mass through the unchanged `g/h` density and the actual restricted convolution. Equations (30)–(34), lines 453–514, give the two exponential moments and the exact monic Legendre norm; equations (35)–(37), lines 516–567, prove the diagonal and general-window norm estimates.

`BALANCED_WINDOW_PROOF.md` supplies the explicit balanced-degree calculation at BW1–BW3, lines 19–56. Its BW4, lines 58–65, expressly imports the separately reviewed exact-window theorem. BW5–BW7, lines 66–98, compose it with the quartet lower allowance and use the overlapping volume windows.

`FOUR_VOLUME_THRESHOLD.md` itself supplies a full written derivation of the multiplication step in section 3, lines 136–171: it states the original radius identity, multiplies all factors, retains the phase, and deals with unit contractions without dividing by a vanishing factor. Its section 2, lines 63–134, repeats the balanced calculation, and section 4, lines 173–222, proves the precise overlap and limiting factor four. Thus the parent source contains a written proof of its displayed product (5), even while the originally supplied longer window-product attachment remains a separate provenance dependency.

The radius identity and spectral lower bound are explicitly upstream mathematical inputs, with proofs in the original Toda/exterior family. Neither the endpoint arithmetic note nor a finite fixture proves the entire upstream construction. The checker identifies the original TVB proof and PR23/PR24 notes by explicit paths, listed in the JSON; this audit does not replace those proofs by their checksums. The parent's independent lanes own their full closure.

## Exact map from the arithmetic source to the two finite quotient types

Put `c=k/2`, `H=L²(R,m_(h,k)(u)du)`, and retain

\[
\mathcal V_{h,k}:\mathbb C[S]\longrightarrow\mathscr B^{\widehat\otimes k},
\qquad \mathcal V_{h,k}P=P(D_1+\cdots+D_k)F_h^{\otimes k}.
\]

The supplied Mellin/Fourier realization sends this vector isometrically to `u↦P(c+iu)` in `H`: its squared norm is exactly NOTE (11). No probability rescaling occurs; the constant vector has squared norm `mu_h^k`. The map retains the actual polynomial `h`, the entire quotient `v_h=g/h`, and the Taylor unit in NOTE (9)–(10).

For `P_n=C[S]_{≤n}`, with `P_a=0` for `a<0`, the leading-coordinate exact sequence is

\[
0\to P_{n-1}\to P_n\xrightarrow{\operatorname{lc}_n}\mathbb C\to0.
\]

Surjectivity is witnessed by `S^n`; the kernel consists exactly of polynomials of degree at most `n-1`. Its Hilbert quotient norm at `1` is the infimum in NOTE (12), namely `omega_(h,k,n)`. Under the coordinate substitution the leading coefficient is `i^n`; its modulus is one, and the original phase is retained in the source polynomial.

For a nonempty monic relation `chi` of degree `q`, Euclidean division gives the second exact sequence, for `n≥q-1`,

\[
0\to P_{n-q}\xrightarrow{\times\chi}P_n\xrightarrow{\pi_\chi}\mathbb C[S]/(\chi)\to0.
\]

Injectivity follows because multiplication by a nonzero polynomial is injective. The kernel of the quotient map consists exactly of multiples of `chi`, and degree additivity places their multipliers in `P_(n-q)`. Every residue class has its unique representative of degree at most `q-1`, which proves surjectivity on the displayed domain. The resulting metric is the minimum source norm on each residue class. The exact commutative maps into jets and cohomology remain NOTE (10): `J^(k)V=eta pi_chi` and `q^(k)V=sigma_h^tensor(k) eta pi_chi`.

The associated-degree morphism is, for **n≥q**,

\[
\overline{\times\chi}:P_{n-q}/P_{n-q-1}\xrightarrow{\sim}P_n/P_{n-1},
\qquad [P]\mapsto[\chi P].
\]

It is well-defined because a lower-degree multiplier yields degree at most `n-1`. Since `chi` is monic, the leading coefficients on both sides coincide. Identifying either one-dimensional quotient by that coefficient proves injectivity and surjectivity. At `n=q-1`, its proposed source is `P_-1/P_-2=0`, whereas its proposed target is one-dimensional; the literal unqualified sentence after NOTE (13), lines 237–240, therefore fails at that endpoint. The quotient exact sequence itself remains valid there, with zero relation space. The correction required by REVIEW line 43 is exact and necessary.

For `n≥q≥1`, the arithmetic quotient map cannot descend through the leading-coordinate quotient by keeping the same source map: `1∈P_(n-1)` has leading-coordinate image zero but arithmetic image `[1]≠0`. The two exact sequences and the proved associated-degree morphism give their actual relation; no claim of unrelatedness is made. At every original support label `lambda`, their split lifts use `(lambda,P)↦(lambda,[P])`; a relation maps to `(lambda,0)` and the externally absent input maps to `tau`.

For the interval estimate, restriction gives an isometry

\[
H\longrightarrow L^2([-L,L],m\,du)\oplus L^2(\mathbb R\setminus[-L,L],m\,du),
\quad f\mapsto(f|_{[-L,L]},f|_{\mathbb R\setminus[-L,L]}).
\]

Its inverse extends each component by zero and adds them. Equality of squared norms follows by additivity of the original integral over the two disjoint measurable sets. Discarding the nonnegative outside squared norm proves an inequality on the original source; the original function is recovered by that inverse map.

## Audit of the analytic constants and the balanced calculation

In NOTE (15), the Joukowski semiaxes are `65/16,63/16`, so the transformed real strip is `[-55/16,71/16]`. For `|T|≥10` the pole is outside. The fractional-part formula (16), followed by the stated reflection and gamma inputs on the other half-strip, gives exponent at most `79/16<5`, and the chosen common exponent `6` is sufficient. The unit discs about `[-1,1]` lie in the ellipse because their union lies in the rectangle `|Re z|≤2,|Im z|≤1` and `(32/65)^2+(16/63)^2<1`. The derivative bound consequently retains radius exactly one.

At `r_*=(3+sqrt(13))/2`, `theta=1-log(r_*)/log(8)>1/3`. From `c_*≤m_T^theta M_T^(1-theta)`, with `0<c_*<1≤M_T`, one gets `m_T≥c_*^3 M_T^-2`. A one-sided interval of length `m_T/(2M_T)≤1/2` fits inside `[-1,1]`, even at an endpoint maximum; on it the value is at least `m_T/2`. Its integral lower bound is `m_T^3/(8M_T)`, producing power `6·7=42` and the constant in (22). Compact completion proves (23) for all real `T`.

The identity `g=h v_h`, including at the selected centers, gives (25) without evaluating an unresolved quotient at a zero. Positivity almost everywhere of the nonzero entire restriction makes `w_h*w_h` positive at every real point. Translation continuity in `L¹` and boundedness give continuity, so the actual minimum `b_h` on `[-1,1]` is positive. Restricting the convolution to that interval yields (28); restricting the remaining `k-3` variables yields (29) with `vartheta_h^(k-3)` and the full original mass. This argument requires `k≥3` exactly as written.

Both actual Laplace moments are retained in (31)–(32). The Legendre polynomial has leading coefficient `(2n)!/(2^n(n!)²)` and squared norm `2/(2n+1)`; subtracting the scaled extremizer from a competitor leaves an orthogonal lower-degree polynomial. The source phase `i^n` therefore gives the same displayed squared minimum (33). Combining its interval lower bound with the trial upper moment proves (37), hence BW1.

For `n≥k≥3` and `n/2≤r≤n`, put `L=n`. Before taking the root, the factor 2 from the two exponential moments cancels the factor 2 in the Legendre lower bound. The factorial and Legendre terms have the exact elementary rearrangement

\[
\left[\frac{(4n)^{2(n+r)}4^n}{n^{2n}}\right]^{1/(2r)}
=4n\,8^{n/r}.
\]

The remaining positive scalar is `((2n+1)/(c_h n))^(1/(2r))`. It is at most `max(1,3/c_h)` because `(2n+1)/n≤3` and `0<1/(2r)≤1`. Now `8^(n/r)≤64`, `X_h^(k/(2r))≤X_h`, `vartheta_h^(-(k-3)/(2r))≤K_h`, `b^(-(n+r)/r)≤max(1,b^-3)`, and `exp(pi(n+k-3)/(4r))≤exp(pi)`. Finally `log(2n)/n` decreases for `n≥3`; since `2r≥n`, the polynomial factor is at most `6^(B_h/3)`. This proves the literal BW2–BW3 constant `256 exp(pi) max(1,3/c_h) X_h K_h max(1,b^-3) 6^(B_h/3)` with its exact original objects.

No defect was found in this chain or in the older diagonal constant. The standard reflection/gamma/Legendre sources remain the explicit classical inputs identified by the documents. This lane read their use in full; it did not relabel another lane's primary-literature browsing as its own.

## Exact product-to-volume morphism and endpoint placement

On the original canonical family, the radius identity used at `N≥q` is

\[
\epsilon_N^2+\phi_N^2=
\frac{\omega_{N+1}}{\omega_N}(1-\delta_N)
\frac{1-\delta_{N+1}}{\delta_{N+1}},
\qquad \delta_N=V_N/V_{N-1}\in(0,1].
\]

For `n≥q` and integer `r≥1`, multiplication yields the monic-norm ratio `omega_(n+r)/omega_n`. Its denominator contraction product is `prod_(j=1)^r delta_(n+j)=V_(n+r)/V_n`. The numerator has one occurrence of `1-delta_n`, one of `1-delta_(n+r)`, and two of every interior factor. Therefore

\[
\prod_{j=0}^{r-1}(\epsilon_{n+j}^2+\phi_{n+j}^2)
=\frac{\omega_{n+r}V_n}{\omega_nV_{n+r}}
(1-\delta_n)(1-\delta_{n+r})
\prod_{j=1}^{r-1}(1-\delta_{n+j})^2.
\]

This equality is precisely the parent section 3 written proof and the scalar identity checked in finite cases. It never divides by `1-delta`. With `lambda_N=omega_N/V_N`, every right-hand factor after `lambda_(n+r)/lambda_n` lies in `[0,1]`. Since `epsilon_N≥0`,

\[
\min_{n\le N<n+r}\epsilon_N^{2r}
\le\prod_{j=0}^{r-1}\epsilon_{n+j}^2
\le\prod_{j=0}^{r-1}(\epsilon_{n+j}^2+\phi_{n+j}^2)
\le\lambda_{n+r}/\lambda_n.
\]

This proves BW4 on its actual domain. A unit contraction makes an adjacent factor of the product vanish; nonnegativity then forces its corresponding `epsilon` and phase both to vanish. No logarithm of zero is taken. The upstream exterior lower allowance `L_(h,k)>0` for a quartet forces `L^(2r)≤lambda_(n+r)/lambda_n` directly. Combined with BW2, this gives `log(V_n/V_(n+r))≥2r log(L/(Cbal_h n))`.

For the stated exact quartet, retain the supplied `q_k=[1+k(m-1)](k+1)^2` and `L_(h,k)=2 delta[1+k(m-1)](k+1) floor((k+1)^2/4)`. The elementary integer inequality `4 floor((k+1)^2/4)≥k(k+1)` proves `L/q≥delta k/2`. On `n=q,r=q-1`, the radius indices are exactly `q,…,2q-2`, with norm endpoint `2q-1`. Since `q≥k≥3`, this is a balanced window. Writing `C_k=log(V_q/V_(2q-1))` gives BW6. The identity

\[
\log\frac{V_{q-1}V_q}{V_{2q-1}V_{2q}}
=2C_k+\log\frac{V_{q-1}}{V_q}+\log\frac{V_{2q-1}}{V_{2q}}
\]

retains both nonnegative endpoint costs. It proves BW7 after dividing by `q_k log k` and using `(q_k-1)/q_k→1` and fixed `h,delta,Cbal_h`. The earlier threshold two remains the consequence of the earlier sinh estimate; the stronger join has its distinct written source. No upper volume estimate is generated by the product identity or the monic bound.

## Exact jet transport and the second required source qualification

Define the coefficient algebra isomorphism

\[
T:\mathbb C[S]\longrightarrow\mathbb C[u],\qquad (TP)(u)=P(c+iu),
\quad T^{-1}Q(S)=Q((S-c)/i).
\]

For `psi(u)=i^(-q)chi(c+iu)`, `Tchi=i^q psi`, so `T` maps the ideal `(chi)` bijectively onto `(psi)`. It induces `[P]_chi↦[P(c+iu)]_psi`. At a center `S_0=c+iu_0`, repeated differentiation gives `(TP)^(d)(u_0)=i^d P^(d)(S_0)` for every raw derivative order `d`. This is the exact diagonal row transport of the full confluent jets; raw derivatives keep their factorials, and no derivative is silently replaced by a divided derivative.

Let `bar chi` mean conjugation of coefficients. If the actual packet satisfies `bar chi(k-S)=(-1)^q chi(S)`, then on real `u`,

\[
\overline{\psi(u)}=i^q\bar\chi(c-iu)
=i^q(-1)^q\chi(c+iu)=i^{-q}\chi(c+iu)=\psi(u).
\]

Thus `psi` has real coefficients (a polynomial agreeing with its coefficient conjugate on the real line has identical coefficients), and `|chi(c+iu)|²=psi(u)²`. This proves exactly the dagger-stability specialization needed for the doubled-node `2q`-jet formula NOTE (41). The raw NOTE section 8, lines 633–641, omits this hypothesis; REVIEW line 45 correctly supplies it.

For an arbitrary packet the same exact substitution and quotient isomorphism remain valid. The actual relation weight is `psi(u) bar psi(u)` on real `u`, where `bar psi` denotes coefficient conjugation, and its polynomial extension has the roots of both factors with their multiplicities added at coincident roots. This is the actual degree-`2q` polynomial controlling its Christoffel/confluent transfer. A doubled-root specialization to `psi²` needs the proved symmetry above; the general factor-product map supplies the precise continuation when it is absent. No generalized determinant theorem is asserted here without its full transfer proof.

## Exact retained-boundary maps

NOTE (43)–(46), lines 666–721, has an exact Hilbert-space interpretation. Put `r=j-i`, let `T:C^r→H_j` have the actual monic source columns of degrees `i+1,…,j`, let `F:C^r→E` be their residue classes, and let `R_i:E→H_i` be the canonical least-norm lift. The new-source columns are orthogonal to `H_i`, so `T*R_i=0`; their Gram is `Omega`, and `R_i*R_i=G_i`. For `b=T-R_iF`, the quotient is zero, `b*R_i=-F*G_i`, and `b*b=Omega+F*G_iF`.

The range is exactly `D_j∩D_i^perp`: both summands are orthogonal to old relations, while their residues cancel. The leading-degree columns of `T` are monic with distinct highest degrees, and `R_iF` has degrees at most `i`, so `b` is injective by its highest coefficients. Subtracting the matching highest-degree combination from any element of `D_j∩D_i^perp` leaves an old relation still orthogonal to `D_i`, hence zero. This proves surjectivity, including all original boundary subspaces.

Projecting `R_i` away from this new boundary gives

\[
R_j=R_i-b(b^*b)^{-1}b^*R_i
=R_i+b(\Omega+F^*G_iF)^{-1}F^*G_i.
\]

The plus sign in (46) is therefore correct. The resulting kernel update is `K_j=K_i+F Omega^-1 F*`; the determinant lemma gives (44). The displayed matrix `I+Omega^-1 F*G_iF` is similar, by conjugation with `Omega^(1/2)`, to the positive Hermitian matrix `I+Omega^-1/2 F*G_iF Omega^-1/2`. Its eigenvalues are `1+lambda_a>0`, proving the real logarithmic costs in (47). Applying `log(1+x)≤x` to each `lambda_a≥0` proves (48). These are exact volume representations and do not themselves bound the arithmetic growth of those costs.

## Finite receipt, absent attachment locator, and mutable checker

The intermediate checker identifies its submitted window source only as `Path(sys.argv[1])`, line 244. The subsequently read 16,488-byte version accepts the same private intake source through the optional `--attachment` argument and `ARGS.attachment`; it has a separate portable mode omitting local input pins. Its `input_pins` construction records the file's byte count and SHA-256, while `sha` opens the file only to hash its bytes. It does not parse or verify the supplied derivation. The fixture calculations use internally constructed scalar and Gaussian data; in intake mode the parent source hash is checked against a literal pin. The precise map here is

`local path → existing byte sequence → (length, SHA-256)`

alongside

`declared finite fixture data → symbolic/rational calculations → labelled pass/fail records`.

The receipt combines those two outputs. The first map binds bytes if they are available; it neither embeds them nor recovers their path. The second proves the declared finite computations and does not quantify over all degrees, all actual arithmetic packets, or the analytic density. Its code therefore cannot stand in for the written source when a referenced derivation is absent. The original submitted attachment's exact identity is recorded by the receipt as 16,954 bytes and SHA-256 `f34647902fd4f6a913b5adae421c3df20bb1773902a797ec934750b02ed90ddb`; the literal attachment pathname is not stored in the explicitly inspected code/receipt closure. This states the bounded locator result, not filesystem-wide absence.

The child first read a 15,376-byte checker with SHA-256 `652f5d09ba605cf913cc2562c1e24fb304bf2428367bb800c5b06b70bade3cb0`. The intermediate 15,691-byte snapshot has SHA-256 `5e3ef70b63cfb51aae2449142fca6ea2507f313a1a9a9a63adb11c0442f5fd99` and explicitly splits exact checks from four approximate ten-decimal display comparisons. The initial receipt inspected by the child records 11,488 check objects with `label,passed`, rather than that later `kind` field. These are separate source/evidence versions.

A subsequent stable-during-read child snapshot pairs the 16,488-byte checker SHA-256 `7c9b0d3a241c14a2ed08efbab1e06c89b7d48fc6d67118299d32a364819bf395` with the 1,282,484-byte receipt SHA-256 `a901a47efe2656379747e8a4ce477501f6c73b456ba7e7dd23dd82924069a1de`. The latter's `script_sha256` matches that checker; it records 11,488 total checks, comprising 11,484 exact and four approximate display checks. This lane subsequently read all 295 lines of that checker. The receipt still contains only the eight named input identities and no attachment argument pathname. These observations establish the precise repaired provenance pairing visible during the audit; they do not constitute a checker execution by this lane or freeze a still-active owner directory. The parent must bind its actual integration to the selected immutable snapshot. Exact snapshots and later observation details are in the child's companion audit.

Integration should preserve the complete arithmetic note, balanced proof, parent four-volume proof, and the full explicitly required Toda/jet witnesses, while transporting both domain corrections transparently into the cumulative presentation. The missing original pasted attachment requires its own exact content locator or an explicit provenance entry recording that its bytes have not been recovered in this bounded lane. Retaining the already written parent product proof gives a concrete proof witness for equation (5); it does not counterfeit recovery of the original longer pasted calculation.
