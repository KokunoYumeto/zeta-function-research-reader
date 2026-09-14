# Independent analytic dependency check

Date: 2026-09-14. Reviewer: `/root/baseline_final_review/hbl_analytic_check`.

**Acceptance:** HBL9–18 are mathematically accepted against the complete GEL/EIQ source texts listed below. No mathematical defect was found in this scope. This review does not claim to review the displaced-packet transfer, BSL source tails, or the downstream arithmetic receiving maps; those are the parent review's separate scope. No source text was changed and no numerical or PDF calculation was rerun.

## Exact source versions

Paths below are relative to `growing_w_20260914/baseline_20260914`.

- `independent/HOMOGENEOUS_GAMMA_BASELINE.tex`: SHA256 `09aff3f27c728e1519c15c916f1a12bf173ca321f3cbaec90b826cd4ded09065`.
- `../equilibrium/GAMMA_ENSEMBLE_LEADING_RETURN.tex`: SHA256 `2014e7fefdcd963b70b00fb89d597e24c0826582a2541dd1ff44d63051979fc1`.
- `../equilibrium/independent/EXACT_SQRT_LOG_EQUILIBRIUM.tex`: SHA256 `a0a0346a19d0e035a186590dbd69881cdf7a30e8fef602d47bba0932f175e731`.

## Checked calculations

1. **HBL9.** The literal two intervals in HBL8 yield
   `S_q = -6 q^2 log q + (9 - 8 log 2) q^2 + O(q log q)`.
   The factorial inequalities give an error uniform for `q <= j <= 2q`; their total error and each Riemann-sum error have the claimed order. The constant follows from `integral_1^2 x = 3/2` and `integral_1^2 x log x = 2 log 2 - 3/4`.
2. **HBL10–12.** The probability reference measure, the full Gamma mass and Jacobian, and the Vandermonde power match GEL1–3 exactly. At `(s,a)=(q/2,q),(q/2+1,q),(q/2,q+1),(q/2,q+1)`, the four powers `2as+2s(s-1)` are `3q^2/2-q`, `3q^2/2+3q`, `3q^2/2`, `3q^2/2`; their sum is `6q^2+2q`. The four squared sizes sum to `q^2+q+1`, so division by `q^2` tends to one. Both moving-argument lower secant inequalities have the correct signs; together with the endpoint upper bound, fixed-argument GEL10 and EIQ continuity prove the specialization at `a/s -> 2`, `q/s -> 2`.
3. **HBL13.** The lower scalar moment bound retains both half-axes. The upper bound `sigma(y) <= C_U exp(-|y|)` also follows immediately from GEL4 by bounding `(1+4y^2)^(1/4) exp(-(pi/2-1)|y|)` on the real line. Thus `log mu_q = O(q log q)`, and the exact logarithmic-power cancellation gives the stated `C_B`. No finer remainder follows here, and none is claimed.
4. **HBL14–15.** The density is GEL8/EIQ10–11 at exactly `alpha=2`, `beta=pi`, with endpoints `uK=2`, `vE=4`. Under `x -> r^2 x`, the functional changes by `6 log r - pi(r-1)M`; hence `pi M=6`. The EIQ17 endpoint identity then yields `F(2,pi)=-ell/2-3+L`. Substitution gives both displayed coefficient formulas with all signs and constants unchanged. Endpoint logarithms are integrable against the established square-root vanishing density.
5. **HBL16–18.** The arcsine probability on `[1,9]` has logarithmic energy `log 2`, logarithmic moment `2 log 2`, and square-root moment `6E(sqrt(8/9))/pi`. The cosine factorization and joined interval of length `pi` verify the energy constant and finiteness directly. The polynomial `P(z)=1-z/2-z^2/8-z^3/16` is positive and satisfies `P(z)^2-(1-z)=5z^4/64+z^5/64+z^6/256`. Its integrated bound is exactly `E(sqrt(8/9)) <= 265 pi/729`. Substituting `pi<22/7` and `log 2<7/10` gives the exact positive rational `769/17010`. The competitor is within the original variational domain; it is used to bound the already defined coefficient, without replacing the equilibrium or adding a hypothesis.

The accepted mathematical conclusion in this scope is the existence and strict positivity of the homogeneous coefficient `C_B`, with `F_sigma^hom(q)/q^2 -> C_B > 769/17010`. This does not identify `k` with `q`, modify the packet-degree formula, or presume any downstream cancellation.
