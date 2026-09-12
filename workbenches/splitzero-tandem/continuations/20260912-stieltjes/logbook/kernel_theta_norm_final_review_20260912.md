# Final independent review of the original theta norm and volume dictionary

Date: 2026-09-12. Reviewer lane: `/root/arithmetic_moment_exact`. This bounded review reads and checks KL.21–KL.32 in the authoritative local fragment, with the actual earlier kernel, source, and boundary formulas. No research source was edited. No Lean or numerical approximation is used as the proof of these identities.

## Exact editions inspected

All paths below are relative to `package:/tex`.

| File | SHA-256 of the inspected complete bytes |
|---|---|
| `kernel_layer_continuation.tex` | `d943b275867d5d216b9e6042d6f212d88c20fb06d4c60bca74bce1dc17049836` |
| `kernel_terminal_continuation.tex` | `6932e3c4d350aece95c003083d8938668d60bd81b2ebceba6eb1b78a510b2e9f` |
| `tau_boundary.tex` | `312edbd818647b27f0acc7c79dc6caff07b5cbf5ef6f13c0a851c73700518e69` |

Also read `work/pr15_norm_volume_bridge_audit_20260912.md`, including its explicit initial-stage distinction and complex cross-term calibration. This report independently verifies the current final fragment rather than treating the prior audit as a substitute for its proof.

## Result

No error was found in KL.21–KL.32. The final fragment preserves the exact initial section at correction level −1, keeps the old-row identity restricted to levels at least zero, cancels both local-unit pairs with their adjoints in the correct order, and retains the complex conjugation in

\[
\mathfrak h_{m+1}c_m=\overline{\gamma_n}.
\]

The two norm families are connected by an explicit source isometry and a proved determinant identity. The quartet-symmetry conclusion uses both stated symmetries: conjugation makes the kernel scalar real, and reflected conjugation makes its real part zero. The formulas include zero-column cases and every original multiplicity.

## 1. Source spaces and exact level map

Keep the original full polynomial

\[
h(s)=\prod_{\rho\in Z}(s-\rho)^{m_\rho},\qquad d=\deg h,
\qquad E_h=\mathbb C[s]/(h),\qquad g=2\xi.
\]

The actual source map is

\[
\mathcal T_h(P)=P(D)F_h,\qquad \mathcal MF_h=g/h,
\qquad h(D)F_h=f_0,
\]

and its polynomial inner product is the original measure

\[
d\nu_h(t)=|g(1/2+it)/h(1/2+it)|^2\,dt/(2\pi).
\]

Its full jet map is `U_upsilon rem_h`, where `upsilon=j_h(g/h)` and `epsilon=upsilon^(-1)`. At degree `N=d+m`, its kernel is exactly `h P_m` for `m>=0`; applying the source map gives `L_m=span(f_0,...,f_m)`. Thus the degree-indexed minimum `R_(d+m)` equals the original orthogonal correction

\[
\mathbf R_m=(I-P_{L_m})s_h.
\]

At `m=-1`, the domain is `P_(d-1)` and the kernel is zero. The full jet map there is a bijection, with unique inverse

\[
s_hu=\mathcal T_h\operatorname{rem}_h(\varepsilon_hu).
\]

This proves both the uniqueness of the minimum at that stage and the exact metric `G_-1=s_h^*s_h`. It introduces no negative-degree orthogonal theta polynomial. KL.21 defines determinant ratios only for `m>=0`, so their first denominator is this valid positive fixed-section metric.

## 2. Original theta norm, unit transport, and determinant quotient

The map

\[
P\longmapsto hP
\]

is an isometry from polynomials with measure `mu=|g|²dt/(2pi)` onto the specified subspace of multiples of `h` with measure `nu_h`, since the full multipliers satisfy `(g/h)hP=gP`. It shifts the degree by exactly `d`, including all multiplicities, and its source-map image is precisely `P(D)f_0`.

At `l=d+j`, the new relation vector is

\[
e_l=\mathcal T_hp_l-\mathbf R_{j-1}a_l,
\qquad a_l=U_{\upsilon_h}v_l,
\qquad v_l=[p_l]_h.
\]

Its numerator is monic of degree `d+j`, has zero full jet, and is therefore divisible by the original monic `h`. The quotient is monic of degree `j`. The source image lies in `f_j+L_(j-1)` and is orthogonal to `L_(j-1)` by KL.7. Uniqueness of orthogonal projection consequently proves `e_l=u_j` exactly, including its coefficient one. Since the new degree polynomial is orthogonal to every old polynomial, its Hilbert norm gives

\[
\mathfrak h_j=\kappa_l+a_l^*\mathbf G_{j-1}a_l.
\]

At `j=0`, the quotient is the constant polynomial one, so `e_d=f_0=u_0`; this establishes the initial identity without extrapolating a negative theta level.

In the unchanged remainder basis,

\[
\mathbf G_{j-1}=U_\varepsilon^*K_{l-1}^{-1}U_\varepsilon,
\qquad K_{l-1}=\sum_{i<l}v_iv_i^*/\kappa_i.
\]

Thus

\[
\begin{aligned}
a_l^*\mathbf G_{j-1}a_l
&=v_l^*U_\upsilon^*U_\varepsilon^*
 K_{l-1}^{-1}U_\varepsilon U_\upsilon v_l\\
&=v_l^*K_{l-1}^{-1}v_l.
\end{aligned}
\]

Both cancellations follow from `U_epsilon U_upsilon=I`; no unit is assumed to be unitary. This is the required congruence, not an unjustified similarity or scalar cancellation.

The update `K_l=K_(l-1)+v_lv_l^*/kappa_l` gives

\[
r_j=\frac{\det\mathbf G_j}{\det\mathbf G_{j-1}}
=\frac{\det K_{l-1}}{\det K_l}
=\frac{\kappa_l}{\kappa_l+v_l^*K_{l-1}^{-1}v_l}
=\frac{\kappa_{d+j}}{\mathfrak h_j}.
\]

The fixed unit contributes identical positive determinant factors in numerator and denominator. Every denominator is positive. If `v_l=0`, this formula simply gives `r_j=1`, so the proof retains that case. Dividing adjacent identities and multiplying the finite chain proves KL.25 with the stated orientation of both ratios.

## 3. Coherence between packets

For any two full packets `h,H`, KL.28 follows because the two source constructions calculate the identical packet-independent `mathfrak h_j` in `mu`. When `h|H`, let `q=H/h`. Multiplication `P↦qP` gives the exact source equality

\[
(g/H)qP=(g/h)P.
\]

Because both packets include complete multiplicities, `q` has no zero at the old centres. At each old centre, its jet multiplies `epsilon_h` to `epsilon_H`; at an added centre, `qP` vanishes to that centre's full order. The full jet map therefore identifies this multiplication with the CRT inclusion retaining the old jets and inserting zero jets at every added centre.

For `deg P<deg h`, the degree of `qP` is below `deg H`. It is the unique full remainder for the inserted reference jet, proving `s_H iota_(hH)=s_h`. Since the correction subspace `L_j` is independent of the packet,

\[
\mathbf R_{H,j}\iota_{hH}
=(I-P_{L_j})s_H\iota_{hH}
=(I-P_{L_j})s_h=\mathbf R_{h,j}.
\]

At `j=-1`, `L_-1=0`, giving exactly the same fixed-section equality. This supplies the typed source map underlying the numerical equality KL.28.

## 4. Row formulas, exact endpoint restriction, and conjugation

For `m>=0`, set `n=d+m+1`, `kappa=kappa_(n-1)`, `Htheta=mathfrak h_(m+1)`, `K=K_(n-1)`, and `G=mathbf G_m`. The rows are

\[
d_j=\mathfrak h_j^{-1}u_j^*s_h.
\]

The numerator of `s_h` has degree below `d`, while `u_j` has monic numerator `hQ_j` of degree `d+j`. Hence the coefficient at degree `d+m=n-1` in `R_m=s_h-Σ_(j<=m)u_jd_j` is exactly `-d_m`. Comparing it with the leading coefficient in the constrained polynomial expansion gives

\[
d_m=-\frac{v_{n-1}^*K^{-1}U_\varepsilon}{\kappa}.
\]

For the next row, `u_(m+1)=e_n` and KL.10 give

\[
Htheta\,d_{m+1}=u_{m+1}^*s_h
=u_{m+1}^*R_m=-a_n^*G,
\]

so

\[
d_{m+1}=-\frac{v_n^*K^{-1}U_\varepsilon}{Htheta}.
\]

The second identity also calculates `d_0` from the fixed section when `m=-1`. The first identity does **not** extend to `m=-1`: the top coefficient of the reference numerator is then the original extension row `ell_Z`, not a negative theta row. The final fragment preserves this distinction by introducing all of KL.29–KL.30 with `m>=0`, whereas KL.24 explicitly includes `j=0` by its own valid proof. Thus it does not identify the tail convention `d_-1=0` with an illicit leading coefficient formula.

The inverse metric is

\[
G^{-1}=U_\upsilon K U_\upsilon^*.
\]

Substituting the two rows cancels both unit pairs and gives

\[
\begin{aligned}
d_mG^{-1}d_m^*&=\frac{v_{n-1}^*K^{-1}v_{n-1}}{\kappa^2}
=\frac{\alpha_n}{\kappa},\\
d_{m+1}G^{-1}d_{m+1}^*&=\frac{v_n^*K^{-1}v_n}{Htheta^2}
=\frac{\kappa\beta_n}{Htheta^2},\\
d_mG^{-1}d_{m+1}^*&=\frac{v_{n-1}^*K^{-1}v_n}{\kappa Htheta}
=\frac{\overline{\gamma_n}}{Htheta}.
\end{aligned}
\]

Here KT.3 defines `gamma_n=v_n^*K^(-1)v_(n-1)/kappa`, and the Hilbert form is conjugate-linear in the first argument. The order in KL.30 is consequently exact, including the conjugation.

## 5. Reflected energy and the complete two-volume formula

The preceding kernel update gives `alpha_n=1-r_m`: if `x=v_(n-1)^*K_(n-2)^(-1)v_(n-1)/kappa_(n-1)`, then the inverse rank-one update gives `alpha_n=x/(1+x)` while `r_m=1/(1+x)`. At `m=0`, the matrix `K_(n-2)=K_(d-1)` is positive and invertible, so this uses precisely the valid initial metric, not an earlier undefined one.

The succeeding update gives

\[
\beta_n=\frac{\kappa_n}{\kappa_{n-1}}
\frac{1-r_{m+1}}{r_{m+1}}.
\]

Insert KL.25 to obtain

\[
\alpha_n\beta_n
=\frac{\mathfrak h_{m+1}}{\mathfrak h_m}
(r_m^{-1}-1)(1-r_{m+1}).
\]

A packet invariant under `rho↦1−conjugate(rho)` has `Re Tr A=d/2` with every full multiplicity. KT.4 therefore gives `Re gamma_n=0` and

\[
\epsilon_m^2=\alpha_n\beta_n-|\gamma_n|^2.
\]

Using the proven scalar row product yields exactly KL.31, with the subtraction `mathfrak h_(m+1)^2 |c_m|²`. That term was not dropped under reflection alone.

If the packet is also conjugation-stable, `h` has real coefficients and the measure `nu_h` is even under `t↦−t`. The monomial Gram entries are real by conjugating and changing `t` to `−t`. The unique monic orthogonality solution therefore has real coefficients. Its remainder vectors, their finite kernel sum, and the inverse kernel are all real in the original remainder basis. This makes `gamma_n` real; reflection has already made its real part zero. Thus `gamma_n=0`, and the positive factor `Htheta` in KL.30 gives `c_m=0`, proving KL.32.

The norm, determinant, and cross-term formulas never divide by a row, jet column, `alpha_n`, `beta_n`, or boundary energy. If a column is zero, the corresponding volume ratio equals one, and both expressions for the relevant energy remain valid. This also verifies the explicit zero-column scope.

Finally the source convention `delta_m=det G_(m+1)/det G_m` is exactly `delta_m=r_(m+1)`, with `delta_-1=r_0`; this is the index map stated at the end of the fragment. The fragment draws no asymptotic conclusion from a finite identity. Its final statement that further arithmetic information is needed for a vanishing estimate matches the proof's actual scope.
