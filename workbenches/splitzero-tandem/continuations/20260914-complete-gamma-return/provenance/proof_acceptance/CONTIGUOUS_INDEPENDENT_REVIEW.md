# Independent review of the exact contiguous Hankel fragment

Reviewed source: `independent_contiguous.tex`.

Final source SHA-256: `e01021c3b9b659cd897cc95179391b3bde0de63397405426fef2cda420e81196`.

Status: **HCT1–39 accepted within their stated finite, exact scope. No unresolved mathematical, sign, or indexing findings.**

The reviewer read the complete fragment and independently checked its derivations. After the two changes listed below, the reviewer checked only the changed passages and recomputed the source hash; the hash matches the value above. This receipt records a mathematical review, not a compilation or publication action.

## Accepted scope

- HCT1–6 retain the original Gamma weight, its square pushforward, the mass `gamma_0 = sqrt(2*pi)`, and every moment scale. The Fourier calculation, exponential generating function, polynomial norms, and full-line recurrence have the correct constants, domains, and signs.
- HCT7–16 correctly derive the monic determinant formula, constant term, Christoffel and inverse connections, norm shift, and coupled discrete Toda identities, including the `n = 0` boundary convention.
- HCT17 has the correct orientation for the stated column polynomial sequences: `J_a = L_a U_a` and `J_(a+1) = U_a L_a`. The intertwining identities are row-finite polynomial identities and do not assert an unproved infinite-dimensional operator extension or finite endpoint truncation.
- HCT18–24 correctly identify both parity polynomial families and preserve `gamma_0**n` in each determinant. The exact starting values are `c_n^(0) = (2n+1)(2n+1/2)` and `d_n^(0) = 2n(2n-1/2)`. The auxiliary `e_n` recurrence proves positivity using positive sums, products, and quotients. Initial indices through `N+A` suffice for all requested indices `n <= N`, `a <= A`.
- HCT25–30 have the correct Desnanot–Jacobi sign, positive second shift difference, Toda quotient, and telescoping indices. Strictness is correctly restricted where `n >= 1`; no unsupported sign is assigned to the degree difference `log c_n^(a)`.
- HCT31–39 retain both original full matrices and their parity sectors. The paired product is exactly `Z_a = H_n^(a) H_(n+1)^(a) (H_n^(a+1))^2` for the stipulated fixed ranks `q = 2n`, `q+1`. Its degree comparison, shift ratio at `a = q, q+l`, curvature, and finite shift identity are correct. The mass cancels in this ratio because its total matrix dimension is unchanged. The general index budget can use `N = n`, `A = q+l` for HCT37.

These conclusions concern exact finite identities at the stated original parameters. They do not establish a growth rate or a large-rank limit, and the fragment does not claim either.

## Resolved findings

1. HCT4 now explicitly states `|z| < 1` and specifies the branches analytic at zero. Its generating-function calculation is therefore accompanied by its convergence domain and branch choice.
2. The final proof paragraph now says to **add** HCT27 for the four blocks, exponentiate for HCT38, and telescope for HCT39. This corrects the former instruction to multiply logarithmic equalities. The formulas themselves required no changes.

Both corrected passages were verified in the source with the hash recorded above.

The separate supporting exact-arithmetic receipt is `CONTIGUOUS_EXACT_CHECK.json`; its producing agent reports 157 passing rational determinant-versus-recurrence checks, with the source mass retained. Those computations were not rerun by this reviewer.
