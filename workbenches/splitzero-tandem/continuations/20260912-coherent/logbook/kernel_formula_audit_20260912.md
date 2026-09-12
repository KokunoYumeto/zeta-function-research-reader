# Independent audit of the retained Mellin resolvent formulas

Audited on 2026-09-12: `output/split_zero_rh_tandem_2026-09-12/tex/kernel_resolvent.tex`, initial SHA256 `0277B4F2ABD543EF6BA970ED743EFF51017AD2DCE27DE3804FCD3E787D73D049`. Read the complete section, and checked its kernel and metric conventions against `tex/tau_boundary.tex`. The added KR.13a formula and explicit tail-domain sentence were reviewed in the revised whole-source SHA256 `3FEA5A11EE0143E6174AD8DEFACF195DCD15E2ABD76BFF552C1E0D780258F123`. The final source, with the nonzero-eigenvalue wording corrected and independently re-read, has SHA256 `2A0D5007F13EA0D1DF6AB095536ED43B9C697AA165730A098C791DD38EEB7E8A`. No cumulative source edits were made by this auditor.

**Conclusion:** no sign, conjugation, domain, or packet-multiplicity error was found in KR.1–KR.21. These are analytic/algebraic proof checks, not numerical validation of the arithmetic moments and not an RH estimate.

## Eigenvector conjugation and endpoint weights

In KR.10 the conjugation is necessary and correct. At a node `lambda + conjugate(lambda) = 1`, conjugating KR.1 and using `b_k + conjugate(b_k) = 1` gives

```
lambda conjugate(q_k(lambda))
 = -conjugate(q_{k+1}(lambda))
   + b_k conjugate(q_k(lambda))
   + a_k conjugate(q_{k-1}(lambda)).
```

After division by `sqrt(kappa_k)`, this is precisely the row equation of `B_n` on `x_k=conjugate(q_k(lambda))/sqrt(kappa_k)`. The last row uses `q_n(lambda)=0`. Thus the last-to-first squared-coordinate ratio is `kappa_0 |q_{n-1}(lambda)|^2/kappa_{n-1}`, giving the first weight equality in KR.10. The Christoffel–Darboux polynomial identity at `w=lambda` has factor `z-lambda`; its canceled value is `q_n'(lambda) conjugate(q_{n-1}(lambda))/kappa_{n-1}=1/omega`. Taking its squared modulus gives the second equality with every positive constant retained.

## Quadrature and the complete packet

KR.8 holds through degree `2n-1`: division by the unchanged monic `q_n` leaves a product with degree at most `n-1`; conjugation on `s=1/2+it` is the polynomial involution `P(s) -> conjugate(P(1-conjugate(s)))`, so the needed bilinear orthogonality follows from the conjugate-linear-first Hermitian orthogonality. The Lagrange polynomial Gram is therefore exactly `diag(omega_j)`. Its complete residue columns are `L_j(A)c`, which proves KR.9 without evaluating a rational function at an intersecting packet centre.

When the stated nonintersection holds, each `A-lambda_j I` and `q_n(A)` is invertible modulo the original `h`, including its nilpotent local factors. Substituting KR.10 gives the factor `1/kappa_{n-1}` in KR.12. The identity `A X_j=lambda_j X_j+c` gives the stated weight form with a plus sign. Congruence by `q_n(A)` carries both forms simultaneously and yields KR.13. No packet coordinate or local multiplicity is discarded. The index `m=n-1-d` includes `m=-1`, which was explicitly defined in the preceding section.

## Genuine tail and the unbounded operator domain

The tail argument is valid. Every polynomial basis vector belongs to `Dom M` because all arithmetic polynomial moments are finite. Consequently `P_n Dom M` is contained in `Dom M`, and

```
Q_n Dom M = Dom M intersect Q_n L^2(nu_Z).
```

For the self-adjoint multiplication operator `T=(M-I/2)/i`, the sole coupling between these two summands is bounded and has finite rank by the recurrence. Subtracting its self-adjoint off-diagonal part leaves the same domain, is self-adjoint, and reduces both summands. Its tail restriction is self-adjoint on the displayed tail domain. This proves existence and the norm bound for the genuine tail resolvent. The revised source explicitly includes the preceding domain equality before the bounded off-diagonal subtraction, as suggested during the initial audit.

With the conjugate-linear first convention, `Re <v,(z-M_tail)^(-1)v> = (Re z-1/2) ||(z-M_tail)^(-1)v||^2`, so the Schur-complement real-part argument retains the correct sign on both half-planes. In KR.18, `z-M` has upper coupling `+sqrt(a_n)` and lower coupling `-sqrt(a_n)`, hence the finite and tail Schur corrections both have a plus sign. This proves KR.15 and the nonvanishing denominator.

## Endpoint cofactors and the complete remainder

For `zI-B_n`, the superdiagonal is `+sqrt(a_k)` and the subdiagonal is `-sqrt(a_k)`. The upper-right inverse entry therefore has sign `(-1)^(n-1)`, while the lower-left inverse entry has positive sign. The product of their magnitudes is `kappa_{n-1}/kappa_0`. This verifies both entries of KR.20, including `n=1`.

The negative rank-one inverse correction in KR.19 contributes one further minus sign. After pairing with `sqrt(kappa_0)e_0` and using `a_n kappa_{n-1}=kappa_n`, its remainder is exactly the first KR.16 expression with factor `(-1)^n kappa_n`. KR.15 then gives the second expression. Independently, the monic polynomial reflection identity gives `q_n(s)^2=(-1)^n |q_n(s)|^2` on the retained vertical line; the polynomial-division derivation in the source agrees. The bound KR.21 follows using `|z-s| >= |Re z-1/2|` and does not remove any arithmetic factor.

The initial observation and terminal observation are related by the stated Schur maps and remainder; the proof does not identify them or import a terminal asymptotic from convergence of the initial transform.

## Added KR.13a scalar formula

Write `u=S_n^(-1/2)c` and `v=S_n^(-1/2)r_n`. The Hermitian matrix is exactly `[v,u][u*;v*]`. Reversing the rectangular factors gives `[[gamma_n,beta_n],[alpha_n,conjugate(gamma_n)]]`, exactly the displayed matrix. Its characteristic roots are `Re gamma_n +/- sqrt(alpha_n beta_n-(Im gamma_n)^2)`. Cauchy–Schwarz makes the radicand nonnegative. Taking the greatest absolute value gives KR.13a.

The formula includes rank one and zero. In particular, if `v` is a purely imaginary multiple of `u`, the Hermitian matrix is zero even though the two-by-two reversed product may be a nonzero nilpotent; both roots are still zero and the formula remains correct. The final source now explicitly compares the **nonzero eigenvalues on both sides**, with multiplicities. Comparing all eigenvalues of the two-by-two matrix against only the nonzero eigenvalues of the original would have introduced extra zeros when the packet has dimension one. This accepted wording clarification does not change KR.13a or its characteristic polynomial. The final source has no outstanding correction from this audit.
