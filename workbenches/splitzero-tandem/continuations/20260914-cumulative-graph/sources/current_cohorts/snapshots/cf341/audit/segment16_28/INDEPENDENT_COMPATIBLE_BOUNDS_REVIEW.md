# Independent review of HC1–HC15

Review date: 2026-09-13. This review reads the TeX source directly and does not modify the reviewed module.

## Verdict and exact scope

The mathematical assertions HC1–HC15 are accepted in their declared domain: an actual zero of `g=2 xi` with `0<delta<1/2`, positive ordinate `gamma`, complete common multiplicity `m`, and integer tensor degree `k>=3`. The actual divisor `h|g`, entire quotient `v_h=g/h`, source density `|v_h(1/2+iu)|^2/(2 pi)`, source mass, complete cyclic polynomial, and raw jets remain present. The module neither constructs an off-line zero nor identifies its nonempty scalar intervals with an existence result.

One minor standalone-definition repair is recommended: define `mu_h = integral_R w_h(u) du` explicitly before HC6. The symbol first occurs at module line 99, and the cited HT1–HT7 do not themselves define it. Its meaning is unambiguous from AU.1, so this is a completeness issue, not an incorrect estimate.

An optional exact strengthening is available in HC12: `e_N = log beta_N`, not only `e_N >= log beta_N`. A proof appears below. The current weaker assertion is valid.

## Sources and coverage

All paths below are relative to the shared repository root.

* Reviewed entire file `work/rh_counterfactual_20260913/shared_thread_audit/segment55_67/actual_compatible_bounds.tex`, lines 1–368, SHA256 `6926cb527e42c20fccd87324814987e728226eec0672ac0bb973771f90c0e780`.
* Re-read entire `work/rh_counterfactual_20260913/shared_thread_audit/segment55_67/actual_holonomy_counterfactual.tex`, lines 1–339, SHA256 `74f8b45052c6f10d3d0ecd8a861336e2b66b19fd94ed26921889c22bf932c449`.
* Read entire `output/split_zero_rh_tandem_2026-09-12/current_source_20260913_deligne/sources/local_endpoint_continuations/consecutive_first_window_join_20260913.tex`, CJ.1–CJ.22 and provenance, SHA256 `e7834ff7ae2e21ff9574c784df02dbe7b37e596012f3e9af651a7c3c87f47c8e`.
* Read `output/split_zero_rh_tandem_2026-09-12/current_source_20260913_deligne/sources/local_endpoint_continuations/arithmetic_volume_upper_route_20260913.tex`, lines 1–590, covering AU.1–AU.33 in full, SHA256 `21aaedc3585887fa7d2cb3e37e68d14415829a4b213566f7a08f4619835ef38b`.
* Re-read original `output/split_zero_rh_tandem_2026-09-12/sources/web_holonomy_descent_delivery/Tau_Holonomy_Descent_Control/NOTE.tex`, lines 404–680, H24–H44; original operator domain/primitive continuation H53–H55 had already been read fully in the preceding independent HT review. SHA256 `444f82a8fa420e6f471ef448442085f3a93acb137069e1505d155faab051b881`.
* Read the original arithmetic envelope and its source constants in `.../local_endpoint_continuations/endpoint_product_dependencies_20260913/Arithmetic_Endpoint_Bounds_original_NOTE.tex`, lines 368–478, equations (24)–(32). The current review checks the inherited envelope's precise use in HC, rather than claiming a new independent certification of the preceding local zeta-mass theorem (23).

## HC1–HC5: exact products and constants

CJ.2 defines `V_N=det G_N` and not its square root. CJ.7 gives the first step with a single factor `1-d_q`; CJ.8 gives the regular step with factors `(1-d_N)(1-d_{N+1})`. Multiplying these proves the two literal products CJ.9 and CJ.10, so HC1 retains precisely the correct first-window terminal factor and the regular-window two endpoint factors. Positivity of the source and the original quartet lower bound `epsilon_N>=L>0` imply `0<d_j<1` at all used degrees. Thus no logarithm at zero occurs.

Both windows have length `q`. Their union counted with multiplicity has endpoint weights one at `q-1,2q-1`, weight two internally, and total weight `2q`. Hence HC2 has the correct monic norm quotient and no factor of two is missing.

Let `C=C_h^win`, `W=(omega_{2q-1} omega_{2q})/(omega_{q-1} omega_q)`, and `L=mathcal L`. For each index, the sum of HC4's two logarithms equals

`log(1+phi_N^2/L^2) + log((epsilon_N^2+phi_N^2)/(L^2+phi_N^2)) = log(epsilon_N^2+phi_N^2) - 2 log L`.

Multiplication by the weights and summation therefore subtracts `4q log L`. The two final constant terms in HC4 satisfy

`4q log(Cq) + 4q log(2L/(delta k q)) - 4q log L = 4q log(2C/(delta k)) = -4q log(D_h k)`.

Together with HC2 this proves exactly `R_k=B_k-4q log(D_h k)`. All five pieces are nonnegative: the contraction logarithms, the squared phases, `epsilon_N>=L`, the two CJ.18 norm-window bounds, and `2L/(delta kq)>=1`, respectively.

CJ.18 applies with `(n,r)=(q-1,q)` and `(q,q)`, because `q>= (k+1)^2`, `q-1>=k`, and `q<=2(q-1)`. It supplies `W <= (Cq)^(4q)`. Finally `C>=27` and `0<delta<1/2` give `0<D_h<1/108`, with the exact inherited constants of HC3.

## HC6–HC8: the extra degree and both upper estimates

The actual roots in the original `S` chart are `lambda_ab=c+(2a-k)delta+i(2b-k)gamma`, with every multiplicity `ell_k`. Under `f(x)=P(c+iTx)`, their images satisfy `|z_ab|<=k sqrt(delta^2+gamma^2)/T=r`. The maps on source and quotient coefficients commute with remainder, since `P-rem_chi P` is divisible by `chi` and substitution maps `chi` to `(iT)^q chi_T`. No roots are removed.

In the degree-`q-1` coefficient basis the substitution matrix has diagonal `(iT)^j`, `0<=j<q`. Its determinant is `(iT)^(q(q-1)/2)`. Transport of the quotient metric is inverse congruence, so its determinant is multiplied by `T^(-q(q-1))`. Separately, an order-`d` raw derivative is multiplied by `(iT)^d`. These are different coordinate statements and both are correct; the common coefficient-metric determinant factor cancels in the displayed volume ratios. The source substitution sends its measure to `T m_{h,k}(Tx) dx`, whose mass remains `mu_h^k`.

The Legendre coefficient bound follows from the original Rodrigues product-rule identity

`P_j(x)=2^(-j) sum_{a=0}^j binom(j,a)^2 (x-1)^(j-a)(x+1)^a`.

The coefficient l1 norm of each product is at most `2^j`; hence `||P_j||_coeff,1 <= sum_a binom(j,a)^2 = binom(2j,j) <=4^j`. Its squared integral is `2/(2j+1)`. Cauchy–Schwarz bounds each Legendre expansion coefficient by `sqrt((2j+1)/2)||f||_2`; bounding that square root by its value at `N` and summing the geometric series yields exactly the stated `A_N`.

For every integer `s>=0`, the quotient of `x^(q+s)` by `chi_T` is `Q_s=sum_{j=0}^s h_j x^(s-j)`, where `sum h_j t^j=prod_a(1-z_a t)^(-1)`. Indeed the formal inverse identity cancels every coefficient of degree `q,...,q+s-1` in `chi_T Q_s`, and the leading coefficient is one. Therefore `chi_T Q_s=x^(q+s)-rem`, so `||rem||_coeff,1=||chi_T Q_s||_coeff,1-1`. The triangle inequality and complete homogeneous coefficient bound give precisely HC's remainder estimate. It holds at `s=q`; no new analytic hypothesis is required to extend AU's degree `2q-1` calculation to degree `2q`.

For degree below `q`, `|v(u/T)| <= ||v||_coeff,1 max(1,|u/T|^(q-1))`. Squaring and integrating gives `U_k(T)||v||_coeff,1^2` with the original `mu_h^k` plus the moment of order `2q-2`. Restriction of the unchanged source norm to `[-T,T]` gives `T a_k(T)||f||_2^2`. Composing the maps yields the two HC6 Hermitian comparisons. Applying the same inequality to a nonzero degree-below-`q` polynomial proves `C_N>=1`. Taking determinants multiplies its logarithm by exactly `q`, proving HC7. Its exact ratio `rho_q` is `A_{2q}^2/A_{2q-1}^2`.

For the scalar estimate, `mu_h <= (M_h(b)+M_h(-b))/2 <= X` follows by integrating `cosh(bu)>=1`. Thus `U_k(T)<=3X^k`, since `bT>=2q` makes the factorial ratio at most one. Direct calculation gives

`A_{2q-1}^2 <= (2q/9)256^q`, and `A_{2q}^2 <= (40q/9)256^q`.

The second factor is twenty times the first upper bound; it is not a bound on the exact ratio `rho_q`. This validates the text's explicit avoidance of the false `rho_2<20` statement. The derivative bound for `log((1+r)/(1-r))` gives `log B_q(r)^2 <=16 k R_0/(3D)`.

Substitution gives the complete useful estimate

`C_{2q-1} <= [2/(3c_h D)] (XK)^k exp(alpha D q + alpha k) 256^q (1+(D+1)q)^B exp(16kR_0/(3D))`.

Replacing its leading constant by `C_env>=1` and taking `q log` is exactly `U_k`. The degree-`2q` bound has the additional factor twenty. Adding the two window estimates proves HC8, including `2U_k+q log20`.

## HC9–HC11: the interval assertions have their stated scope

Set `t=4q log(D_h k)`. Monotonicity gives `B_k>=0`, HC5 gives `B_k>=t`, and HC8 gives `B_k<=Uhat_k`. Subtracting `t` proves HC9, and subtracting the literal Gamma-reference four-volume logarithm proves HC10. No sign of the latter subtraction has been inserted.

The width in either interval is `Uhat_k-max(0,t)`. Every nonquadratic term in `U_k` is nonnegative. Since `a>1`, `q>2k`, and `D_h<1`,

`Uhat_k >=2a q^2 >4qk >=max(0,4q log(D_h k))`.

The final inequality uses `log(D_h k)<=log k<k`, and also covers a negative logarithm. Thus the asserted strict positive width holds for every declared `k>=3`. For a fixed packet and fixed `b`, `k/q ->0`, `log q/q ->0`, and `log k/q ->0`. Dividing by `q^2` leaves exactly `2(alpha D+log256)` in HC11. This establishes compatibility of these scalar bounds only; it is not a construction of a point in the zeta zero divisor. The module explicitly states this limitation.

## HC12–HC14: domains, constants, and the exact rank-one strengthening

All objects in HC12 use the same fixed `L,theta,N`. In the original polynomial realization, multiplying the least coefficient lift `C_N v` by `S` has degree at most `N+1` and remainder `Av`. Its actual periodized realization is `D_{L,theta}R_Nv`. Minimizing on this same affine quotient fibre gives

`A* G_{N+1} A <= R_N* D_{L,theta}* D_{L,theta} R_N`.

The original smooth columns lie in the twisted `H^2` domain by HT, so the displayed operator product is legitimate; equivalently it is its squared-norm quadratic form. Since `G_N<=beta_N G_{N+1}`, congruence by `A` and then by `G_N^(-1/2)`, followed by trace, gives

`||R_N A G_N^(-1/2)||_HS^2 <= beta_N J_N^D`.

The Hilbert–Schmidt triangle inequality for the exact boundary `D R_N-R_N A` now gives the factor `(1+sqrt(beta_N))^2`. HT14 supplies its lower bound `L^2/2`. The boundary products vanish in integration by parts because both endpoints have multiplier `exp(-i theta)`, of modulus one; thus `||Df||^2=c^2||f||^2+||f'||^2`. Since `R_N*R_N=G_N`, summing over a coefficient orthonormal basis gives `J_N^D>=c^2q>0`.

Degree monotonicity makes every eigenvalue of `G_{N+1}^(-1/2)G_NG_{N+1}^(-1/2)` at least one. Their product is `V_N/V_{N+1}`, proving `e_N>=log beta_N`. Rearranging the energy inequality gives `sqrt(beta_N)>=L/sqrt(2J_N^D)-1`; combining this with `beta_N>=1` proves exactly HC12's logarithm and its factor two.

In fact the original kernel update strengthens this equality. Write `b=b_{N+1}`, `omega=omega_{N+1}`, and `t=b*G_N b>=0`. Sherman–Morrison gives

`G_{N+1}=G_N-G_N b b* G_N/(omega+t)`.

Thus `G_N-G_{N+1}` has rank at most one. Its congruence by `G_{N+1}^(-1/2)` shows the comparison matrix is identity plus one positive rank-one operator. All but at most one eigenvalue equal one, so its determinant is its largest eigenvalue, and `e_N=log beta_N`. This is an exact strengthening available within the existing source, not a correction required for validity.

Telescoping the two literal windows proves HC13 with weights one/two/one. For HC14, the source comparison follows from original H39–H41: for any fixed source degree and positive allowed `a`, `delta_L=kappa_{a,N}/(exp(aL)-1)`, so choosing `L>=a^(-1)log(1+kappa_{a,N}/eta)` supplies `delta_L<=eta`. Restriction to smaller polynomial sources and minimization preserve `(1-eta)G_N<=G_{N,theta}<=(1+eta)G_N`. Each endpoint log determinant changes within `[q log(1-eta),q log(1+eta)]`; summing two numerator changes and subtracting two denominator changes gives exactly `2q log((1+eta)/(1-eta))`.

For the averaged metrics, the original H28 and H33 prove `(1-eta^2)G_N<=Gbar_N<=G_N`, with averaging of metrics and not of inverses. The identical endpoint calculation gives `2q log(1/(1-eta^2))`. The module maintains this distinction and does not infer a rank-two formula for the averaged metric. For fixed eta these errors are of order q, while the stated scalar bound width is of positive quadratic order.

## HC15: finite comparison and moment cutoffs

The measure `nu_k` is exactly AU.11, with the original positive factor `c_h theta_h^(k-3) exp(-alpha(k-3))`; it is not given unit mass. It is dominated by `m_{h,k}(u)du`. Thus every unchanged polynomial quadratic form dominates its comparison form. Minimization over identical affine remainder fibres gives `G_N>=G_N^nu>0`, so each determinant ratio in HC15 is at least one. Direct cancellation gives the asserted exact error. The original low-degree Gram at `N=q` uses moments through `2q`; the comparison at `N=2q` uses moments through `4q`. Both cutoffs are correct, including the extra endpoint degree.

The conclusion that these retained, unevaluated positive errors provide no additional displayed inequality opposing HC5 is accurate as a statement about the supplied estimates. It does not establish an impossibility of obtaining stronger future arithmetic estimates.

## Review workflow receipt

No generic positive measure was substituted for the original arithmetic source in this review. No finite numerical sample is used to certify an analytic claim. No Lean, Lake, or Elan process was started. The reviewed module was not edited. A separately delegated bounded check of HC6–HC8 repeats the coefficient-map, remainder, and scalar-constant algebra in `hc_polynomial_check/`.
