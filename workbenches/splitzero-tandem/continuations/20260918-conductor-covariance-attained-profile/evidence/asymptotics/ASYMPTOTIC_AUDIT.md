# LRC16–30 independent audit

**Primary verdict: proved as written on the stated actual simple-quartet domain.** The scalar conclusions and all displayed action signs survive reconstruction. The accompanying TeX expands the abbreviated derivations and makes the finite row-domain implication explicit. The fixed polynomial denoted by `h` in the action remainder is now defined, and the exact action step cites TAC14/CAI15 directly rather than leaving its WCF27 reference unresolved in the nominated source set.

## Exact claim card

The objects are the original simple-quartet grids of degrees `a` and `a−8`, with fixed actual conductor, unit, period and branch; `a ≡ 1 mod 4`, `q=(a+1)^2`, `Q=(a−7)^2`, `Δ=16a−48`, `v=ord_0 E_A≤80`, `m=Δ−v`, and source orders **exactly** `s=1,a`. The lower source is not replaced by order `a−8`. Its four coefficient cutoffs remain `N−v`, where `N=q−1,q,2q−1,2q`.

The audited conclusions are LRC16–30, in particular the literal lower covariance coefficient `+128 q log a`, the complete native return coefficient `−128 q log a`, the uniform original prefix centre with error `O_actual(q)`, and `J_a−δ_ar,a,1=C_B q²+8q log a+O_actual,h(q)`. The signed arithmetic correction, full low quotient metric, all source masses, both half-lines, relation cross blocks, and actual minima remain.

Full derivations: [LRC_SCALAR_RECONSTRUCTION.tex](LRC_SCALAR_RECONSTRUCTION.tex), equations LRS1–31. No theorem is made true by adding an assumed missing analytic bound. The scalar norm input is proved in the independently assigned equilibrium fragment, and the original quotient transport is proved in the independently assigned transport fragment.

## Evidence and dependency graph

1. **Internal exact source conventions:** EIQ1–5, EIQ30–31, ECL6, ECL11, ECL13–16. These fix the potential, endpoint modulus, Robin sign, energy sign, dilation and original outer coefficient.
2. **Internal finite norm proof:** equilibrium/EQUILIBRIUM_NORM_PROOF.tex, EQ12–13, EQ17, EQ27, EQ28–36, plus its independent quantile proof. These establish LRC14–15 and the unbounded-alpha uniformity required by LRC18.
3. **Exact linear algebra:** original full source Gram and relation ideal → LRS2 Schur determinant → LRS3 exact row; all off-diagonal relation blocks enter the Schur minimum.
4. **External classical formula, checked at source:** [DLMF 5.11.1 and 5.11(ii)](https://dlmf.nist.gov/5.11#ii) provide the positive-real Stirling remainder. LRS6–7 first cancel the original mass and Gamma-order factors exactly and only then use this formula. The finite Taylor estimate is proved locally, rather than importing a fixed-shift asymptotic for growing `ell_s`.
5. **Internal exact equilibrium identities:** LRS8–9 prove the Robin displacement; LRS12–16 prove the derivative, primitive, small endpoint expansion and coefficient identity.
6. **Elementary finite sum:** LRS17–18 compare the exact endpoint-weighted rows with their integral using monotonicity. This works at zero without a bounded derivative.
7. **Original finite cutoffs:** LRS19–22 evaluate precisely the displaced lower interval and upper natural interval.
8. **Internal exact quotient transport:** transport/LRC_TRANSPORT.tex, LRC8–10 and LT26–28, with its complete analytic quotient identification, establish all-cutoff `O(q)` determinant discrepancies. TAC9–10 and LRP10–13 retain the low metric and its monotonicity.
9. **Exact original endpoint operations:** LRS23–27 prove the uniform prefix and correlated remaining tail, with finite directed discrepancy errors; LRS28 proves the growing-prefix asymptotic.
10. **Internal complete action:** CAI28–35, TAC13–15 and LRP18 establish LRS29–31. The independent action-sign review is recorded in [action/ACTION_AUDIT.md](action/ACTION_AUDIT.md).

No dependency points to the new conclusion as its own evidence. Symbolic diagnostics mentioned by the supplied attachment were not used as proof.

## Obligation matrix

| Obligation | Result | Exact evidence |
|---|---|---|
| Determinant numerator/denominator orientation | Passed | LRS2–3 prove the Schur determinant and its empty-product endpoint |
| Original complex coordinate and Vandermonde | Passed | Unit-modulus changes retained; only endpoint subtraction cancels Vandermonde |
| Relation rows inside the proved polynomial range | Passed | LRS1 derives `m+q≤2n_-` from the original LRC13 guards |
| Growing Gamma order and original mass | Passed | LRS6 exact cancellation, LRS7 finite Taylor remainder |
| Small relation ranks | Passed | Scalar moment interval plus positive-real Stirling in LRS11 |
| Unbounded equilibrium alpha | Passed | EQ28–36 and LRS8–9; no bounded-parameter substitution |
| Summation remainder `O(q)` | Passed | LRS11 bounds summed explicitly; endpoint quadrature LRS17 |
| Primitive and endpoint sign | Passed | LRS12–16, with EIQ/ECL conventions retained |
| Literal lower interval | Passed | LRS19 uses `m,m+q`; no natural lower interval substitution |
| `+128 q log a` | Passed | LRS20–21 derive `m² log(n/m)/2` with its positive sign |
| Source-order `aq` term | Passed | LRS22 and exact identity `2C_B−4a_1=C_Gamma` |
| Uniform original prefix | Passed | LRS23–26; final row has weight two, including `R=0` |
| Low quotient and discrepancy signs | Passed | TAC9–10, LRP10–13, LRS25 |
| Correlated `−128 q log a` total/tail | Passed | LRS24, LRS27 use the same exact factorization |
| Prefix leading `8 a^(5/2)` | Passed | LRS28 includes an explicit double-integral error estimate |
| Complete action `+8 q log a` | Passed | CAI35 and exact `q=(a+1)^2`; independent action audit |
| Individual kernel allocation or arithmetic residual evaluation | Out of scope and not asserted | LRC30 remains an allocation identity; signed residual retained |

## Finite row-domain point resolved without a new assumption

The lower sum requires rows through `m+q`, while LRC18 was established through `2n`. It is necessary to prove these ranges are compatible. The original radius satisfies `R_b≥1/2`. LRC13 therefore forces `n≥65536`. At degree `a−8`, any permitted `a≤41` would instead give `n≤1166`; hence `a≥45`. For such `a`, `q−3Δ=a²−46a+145>0`, which proves `m+q≤2n_-`. The finite domain is already sufficient; no added asymptotic hypothesis is needed.

## Uniform-prefix point needed by later work

The scalar prefix is exactly `tau_0+2 sum_(r=1)^R tau_r`; the lower prefix is `tau_m+2 sum_(r=1)^R tau_(m+r)`. Its integral centre is therefore the integral plus **one extra final reference row**. Both scalar errors are uniformly `O(q)` for every `0≤R<q`.

At the metric level, only endpoint errors at `q−1,q,q+R` are needed. The all-cutoff transport has ambient dimension `D+1=O(q)` and retained rank `Q` for the literal covariance, and rank `m` for the analytic attained quotient. It gives uniform `O(q)` bounds at these exact endpoints. The nonnegative low-prefix return is bounded by its complete LRP return, which is `O(q)`. Applying the original endpoint factorization proves LRC26 with these actual metrics. This justifies its later use as a uniform prefix estimate, rather than only a statement at a single chosen cutoff.

## Source revisions and command record

The following SHA-256 hashes identify the audited raw sources, read on 2026-09-18:

| Source | SHA-256 |
|---|---|
| Attachment `LOCAL_RECORD_09b0993e0db94f74/pasted-text.txt` | `BCC840C8F0E985890959FE39F6546F2DE141E1D15C643AAE8BE9F25DA5FD4EAB` |
| `full_receiver_build/staging/14_CURRENT_KERNEL_AND_MULTIPLICITY_PROOFS.tex` | `50E5071B8BC1E1325F401764E7FDD3CDA50994601B6F2E1BF00627864D665571` |
| `receiving/FULL_TAIL_RETURN_PROPAGATION.tex` | `8951AA99AB5DDB04F5D6A3A208B5AEA2051E968B2A6CEA927D37234EE3957C16` |
| `low_return/LOW_RETURN_PROPAGATION.tex` | `6B588CD9682EE345FAF82DBC346EE23D762E2BA55C6B7D77AA8AA0858F3D410A` |

Read commands used `Get-Content` and bounded `rg` searches for EIQ/ECL/AKS/TAC/LRP/CAI/FTR labels; hashes used `Get-FileHash -Algorithm SHA256`. A direct DLMF read checked the positive-real remainder at 5.11(ii). All generated files are under the assigned asymptotics directory. No source mutation, compilation, Lean execution, numerical-period evaluation or publication was performed.

## Remaining mathematical scope

There is no unresolved scalar or sign gap in LRC16–30 after the supplied analytic norm and transport proofs are included. The original individual flag allocations, independent proper-source absolute value, signed arithmetic residual, retained-class action and projected pairing remain unevaluated by this result. They are not consequences claimed by LRS1–31.
