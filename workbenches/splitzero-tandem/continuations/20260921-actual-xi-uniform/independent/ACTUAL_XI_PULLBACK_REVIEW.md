# Independent mathematical review of the actual Xi-jet certificate

The full certificate executable `certify_actual_xi_pullback.py` was read, its formulas were checked against AUH1–30 and RPZ2–9, and it was replayed with one worker at 768 bits into `ACTUAL_XI_PULLBACK_REPLAY.json`.

The reviewed executable SHA-256 is `ec837285acdd27f84f12929f7a33d08532c0199bd1dff618dcd972b48ff71a08`. The replay receipt SHA-256 is `1d5e151158b62bfc181c92be72cbf71436afe53d24521386daf7d7391d356d8c`. It records the AUH source hash `95e75e4804b240f3cfbbc7f3929bc4ab4a74ccbf337a8932c2927b9a9967457f` and the original period-kernel hash `bb50ba841052d305fc1a66bbfab9095af816f4c8b05eb3f5a1fa578dab883bbe`.

The replay is a separate execution of the same enclosing algorithm. The mathematical review below independently checks its identities; no distinct numerical algorithm is claimed.

## XIR1. Completed-function and derivative conventions

The executable constructs the local power series

\[
 X(s)=\frac{s(s-1)}2\exp\!\left(-\frac s2\log\pi\right)
                  \Gamma(s/2)\zeta(s)=\xi(s).
\]

The factor one half is necessary because the original programme defines `g = 2 xi`. At the evaluated complex intervals the Gamma and zeta factors are analytic, with none of their displayed poles present. For the formal input `q = acb_series([s, 1], 3)`, the output coefficient at index one is `xi'(s)`, and the index-two coefficient is `xi''(s)/2`. Thus `xi_prime = X[1]` and `xi_second = 2*X[2]` have exactly the stated scaling. This is the power-series coefficient convention; it is not a finite-difference derivative.

## XIR2. The two-node remainder and actual divided-unit formula

Let `w = delta + i gamma`, `lambda = w^2`, `d = 4 i delta gamma`, and `fp = 2 xi(1/2+w)`. Reality and reflection give `fm = conjugate(fp)` and `lambda_minus = conjugate(lambda)`. Therefore

\[
 \ell_1=\frac{f_+-f_-}{4i\delta\gamma}
         =\frac{\Im f_+}{2\delta\gamma},\qquad
 \ell_0=\Re f_+-\ell_1\Re\lambda.
\]

These are precisely the two expressions evaluated in `xi_data`. Their dependence on the same underlying real parameters is preserved as a mathematical identity; evaluating their component intervals separately may widen the enclosure but cannot remove an actual value.

Differentiating `F(w^2) = 2 xi(1/2+w)` gives

\[
 F'(\lambda)=\frac{\xi'(1/2+w)}{w},\qquad
 a_+=\frac{F'(\lambda)-\ell_1}{d}.
\]

Thus `(X[1]/wp - l1)/dd` is the exact quotient value from AUH5–6. There is neither a missing factor two nor a replacement by the zero-residual-only formula `xi'/(w d)`. Since the certified real part of `a_+` is positive, its actual first-chart phase `x = Im(a_+)/Re(a_+)` is well defined.

## XIR3. Original period, coefficients and tails

The period code retains exactly

\[
 (\mathcal R_n)_{ar}=
 \sum_{2p+4h=5n+r+1-a}
 \frac{(\beta/3)^p\eta^h(-5)^{p+h-n}(a/5)_{p+h-n}}{p!h!}.
\]

The recurrence `poch[ell] = -poch[ell-1]*(a+5*(ell-1))` equals `(-5)^ell (a/5)_ell`, including its sign. The arrays `aa` and `bb` contain exactly `(beta/3)^p/p!` and `eta^h/h!`. The index restrictions and `ell >= 0` are the original ones.

At the retained quartet, `K = 11/2`, `T = 6 K^5/5`, and `C = 4 K^3` satisfy the RPZ5 majorant assumptions. The three omitted-tail bounds in the executable are RPZ6, with 650 included terms and the same complete first- and second-derivative tails. The Horner recurrences update the second derivative before the first and the first before the value, so each update uses its required preceding-stage values.

The real period interval is centered at the exact decimal in RPZ4 and has enclosing radius `1e-15`. Its centered Taylor enclosure uses the complete second-derivative bound over a convex interval containing every integration segment. Adding a symmetric complex box of modulus-bound radius to each entry is an enclosure, even though the original period entries on this real interval are real. The full matrix inverse is taken after all tails are included.

Consequently the four factors computed by `evaluate` concern the complete original period matrix throughout that interval, including its unique certified point. They are not evaluations of a tail-deleted period polynomial.

## XIR4. Unit conjugation and the correct zeroth moment

The actual first-chart matrix is `W = I + i x J`, where `J = diag(1,-1,-1,1)`. Its displayed inverse `(I - i x J)/(1+x*x)` is exact. The code uses `W^-1 V R^-1 D_j R V^-1 W` with the original order of every factor and all four diagonal phases.

The function `bilinear(y,y)/2` equals `y1*y4 - y2*y3`, so no extra polar-form factor enters the factor values. For real quartet, unit chart and period, the exact original reflection is

\[
 f_4(0)=-\overline{f_1(0)},\qquad
 f_3(0)=-\overline{f_2(0)}.
\]

The product of the four factors is therefore

\[
 \mu_0=f_1f_2f_3f_4=|f_1f_2|^2
 =\bigl((\Re f_1)^2+(\Im f_1)^2\bigr)
  \bigl((\Re f_2)^2+(\Im f_2)^2\bigr).
\]

This is exactly `mu0_ref` in the reviewed executable. A product of the four individual squared moduli would instead give `mu0^2`; that obsolete unused computation has been removed from the reviewed version.

## XIR5. The actual interval conclusions

The replay passes all assertions and reproduces the saved enclosures. At the retained quartet its values include

\[
\begin{aligned}
 \ell_0&\in[0.976258272977427887322701492160654697595967977
                                      \pm1.27\,10^{-46}],\\
 \ell_1&\in[0.0189324105204302311806687369138406180692390525
                                      \pm1.62\,10^{-47}],\\
 x&\in[0.0102105673314144832079374086644740910297551937
                                      \pm3.73\,10^{-47}],\\
 \mu_0&\in[0.0073504214\pm9.54\,10^{-11}].
\end{aligned}
\]

The last enclosure holds throughout the full original real period interval. In particular, the asserted strict bound

\[
 0.0073504212<\mu_0<0.0073504216
\]

is valid. Every original factor is also separately enclosed away from zero. Therefore `E_A(0)` is nonzero and its exact local spectral order is `v = 0` for this actual Xi-derived quotient extension at every period in that interval.

The geometric certificate's unit phase is negative and near `-1.46681744046`, whereas the phase just enclosed is positive and near `0.0102105673314`. The exact sign separation alone proves that this Xi-jet graph does not reach that certified geometric phase at the retained quartet.

## XIR6. The whole quartet-parameter rectangle is covered

The second computation evaluates the entire real rectangle

\[
 |\delta-1/4|\le10^{-8},\qquad |\gamma-3|\le10^{-8}
\]

through interval arguments of the same analytic functions. It is not a finite grid. Its output proves `ell0 > 0.975` and `ell1 > 0.0188`, so the two residual equations of AUH3 cannot hold anywhere in that rectangle. The original arithmetic simple-quartet locus is therefore disjoint from it.

The saved rectangle enclosure actually proves more directly

\[
 \Re\xi(1/2+\delta+i\gamma)
   \in[0.403525\pm6.87\,10^{-7}]\subset(0.4,\infty).
\]

It follows that this Xi value is nonzero at every point of the rectangle. Exact reflection and conjugation give the same positive real part at each of the other three original labels. Hence none of the four marked Xi values vanishes anywhere in the rectangle. This stronger observation is already a consequence of the saved enclosure and requires no new numerical assertion.

The four conductor factors and the stated `mu0` enclosure were evaluated at the exact retained quartet, with the period interval varying. They have not been certified on this entire two-parameter quartet rectangle. The two domain statements remain distinct in this review.

## XIR7. Every fixed finite original cutoff has a nonzero determinant

For any cutoff `D >= 0`, set `N = D+1`. The unchanged old weighted conductor is

\[
 B_{D,s}=\operatorname{diag}(\rho)^{-1}T_D(g_{\rm cond})
                                      \operatorname{diag}(\rho),
 \qquad g_{\rm cond}(0)=\mu_0.
\]

Its original upper-triangular diagonal consists of `N` copies of `mu0`. The two positive diagonal-weight determinants cancel with their actual inverses, so

\[
 \det B_{D,s}=\mu_0^N,
 \qquad (0.0073504212)^N<|\det B_{D,s}|
 \quad\text{throughout the certified period interval}.
\]

The bound holds for each finite cutoff and both retained original Gamma orders. Thus no fixed-cutoff singularity of this actual pullback occurs in that interval. This is not a cutoff-independent inverse-norm estimate: the full higher coefficients and original weights still govern those norms.

## XIR8. Source identity and mathematical limits

The original `g = 2 xi` convention and unit are accepted782 PQO1–3. The complete local divided-quotient proof is AUH1–10. The exact conductor composition is AUH20–26, based on PCL1–10. The complete original period bounds are RPZ5–9. Human interval-arithmetic provenance is Fredrik Johansson's Arb, arXiv:1611.02831v1, retained by the root certificate. Riemann's completion and the original programme's Apostol/DLMF source attribution remain in AUH's references.

The conclusion is local and exact: the retained geometric singular member is excluded from this actual Xi-jet pullback, and the stated small quartet rectangle contains no actual simple quartet. No global arithmetic exclusion or RH conclusion is established by these interval calculations.
