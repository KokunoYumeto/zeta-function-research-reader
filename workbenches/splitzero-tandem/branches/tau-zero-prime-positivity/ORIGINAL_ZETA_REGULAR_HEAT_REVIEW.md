# Independent original-zeta derivation of regular affine heat transport

23 September 2026. This is an independent mathematical derivation for comparison with the owner's `ORIGINAL_ZETA_REGULAR_HEAT_REMAP.md`. It reads the incoming `translation_heat_intake_20260923/RECONSTRUCTION.tex`, RG1–4, CW1–11 and CT6–9, including their complete adjacent proofs. The source hash is `c8b5e84bd3e997fa1ef3767a98658a350b64715f9dc6df6d22eba03ffb5a205e`. The incoming propositions concern an entire numerator. The formulas below reconstruct their original meromorphic-zeta maps with the full fixed factor and divisor retained. Gaussian smoothing in the separate translation variable is outside this task.

## 1. Original function, parameters, and exact inverse

Keep
\[
C(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2),\qquad
q(s)=\frac1s+\frac1{s-1}-\frac12\log\pi+\frac12\psi(s/2).
\tag{RHR1}
\]
The already proved original meromorphic family is
\[
\zeta_\theta(s)=\frac8{C(s)}\int_0^\infty
e^{\theta u^2}\Phi(u)\cosh((2s-1)u)du.
\tag{RHR2}
\]
Its time-zero member is the original zeta. The complete numerator (E_\theta=C\zeta_\theta) has the stated order-one growth estimate, is reflection invariant, and is positive at every real spatial argument for real (\theta). The complete proof of these facts, the fixed divisor of (C), and their exceptional-point units is OZH1–15; that source was read in the preceding audit.

Let (a,b,c,\alpha,y,\theta) be real differentiable functions of real (t), with (\alpha>0), and set
\[
r=s-\tfrac12,
\quad\varphi_t(s)=\tfrac12+\alpha r+iy,
\quad\chi_t(s)=ar^2+ibr+c,
\quad\psi_t=\varphi_t^{-1}.
\tag{RHR3}
\]
At a fixed time the exact complex-linear map on meromorphic functions is
\[
(T_tf)(s)=e^{\chi_t(s)}\frac{C(\varphi_t(s))}{C(s)}f(\varphi_t(s)),
\]
\[
(T_t^{-1}g)(\eta)=e^{-\chi_t(\psi_t(\eta))}
\frac{C(\psi_t(\eta))}{C(\eta)}g(\psi_t(\eta)).
\tag{RHR4}
\]
The identities are meromorphic everywhere: cancellation is proved by multiplying the displayed factors. No assertion that (C) is a holomorphic unit at its zeros or poles is required. Both compositions are the identity. For the embedded sheaf (\mathcal L=C^{-1}\mathcal O\subset\mathcal M), the identity
\[
C(s)(T_tf)(s)=e^{\chi_t(s)}(Cf)(\varphi_t(s))
\tag{RHR5}
\]
proves an isomorphism (\varphi_t^*\mathcal L\to\mathcal L). It is complex-linear on sections and is linear over the local-ring identification supplied by affine pullback, not an asserted linear map over unchanged spatial coefficients.

## 2. Every exceptional valuation and jet

Fix (s_0), (\eta_0=\varphi_t(s_0)), write (x=s-s_0), (h=\eta-\eta_0=\alpha x), and retain
\[
C(\eta_0+h)=h^{e_\eta}b_\eta(h),\quad
C(s_0+x)=x^{e_s}b_s(x),\quad
f(\eta_0+h)=h^d u(h),
\tag{RHR6}
\]
where both (b)'s and (u) are nonvanishing holomorphic units and (d\in\mathbb Z). Here the fixed orders are (e_1=1), (e_{-2m}=-1) for (m\ge1), and zero elsewhere. At zero (C(0)=-1); at one (b_1(0)=1/2); at (-2m),
\[
b_{-2m}(0)=(-1)^m\frac{2m(2m+1)\pi^m}{m!}.
\tag{RHR7}
\]
Substitution in RHR4 gives the exact local expression
\[
(T_tf)(s_0+x)=x^{d+e_\eta-e_s}
\alpha^{d+e_\eta}e^{\chi_t(s_0+x)}
\frac{b_\eta(\alpha x)}{b_s(x)}u(\alpha x).
\tag{RHR8}
\]
Thus the order is (d+e_\eta-e_s), with no omitted unit. For every integer (d) and every (N\ge1), this gives an isomorphism
\[
h^d\mathcal O_h/h^{d+N}\mathcal O_h
\longrightarrow
x^{d+e_\eta-e_s}\mathcal O_x/
x^{d+e_\eta-e_s+N}\mathcal O_x.
\tag{RHR9}
\]
Indeed the affine substitution sends (h^j) to (\alpha^jx^j); multiplication by the remaining unit is invertible. On coefficient number (j\), the triangular diagonal factor is
\(
\alpha^{d+e_\eta+j}e^{\chi_t(s_0)}b_\eta(0)/b_s(0)\ne0
\).
Its inverse is RHR4, or the finite triangular coefficient recursion after inverting this constant. This proves all jets, including negative (d). In the embedded module set (d=-e_\eta); the target exponent is exactly (-e_s), as RHR5 requires.

For the actual source, let (m=\operatorname{ord}_{\eta_0}E_\theta\ge0). Then (d=m-e_\eta), so the target raw order is (m-e_s). A moving numerator zero at a fixed zero or pole of (C) can therefore change or cancel the target raw divisor order. The identity retains both factors and their units even when their net order is zero. It would be incorrect to insist that the raw pole at one or every raw trivial zero remains simple after an arbitrary affine displacement.

## 3. The conjugated original generator and its complete residual

Define the original covariant spatial derivative and heat generator by
\[
\nabla_s=\partial_s+q(s),\qquad
\mathcal H_C=\tfrac14\nabla_s^2
=\tfrac14\{\partial_s^2+2q\partial_s+q'+q^2\}.
\tag{RHR10}
\]
Every (q) term is the full expression RHR1. From RHR4–5, direct product differentiation gives
\[
\nabla_s(T_tf)=T_t\{\alpha\nabla_\eta f+\chi_s f\},
\]
\[
\nabla_s^2(T_tf)=T_t\{\alpha^2\nabla_\eta^2f
+2\alpha\chi_s\nabla_\eta f+(\chi_{ss}+\chi_s^2)f\}.
\tag{RHR11}
\]
For a time-dependent source (f_\theta), let (R_C=\partial_\theta f-\mathcal H_Cf). Then
\[
\begin{aligned}
T_t^{-1}(\partial_t-\mathcal H_C)(T_tf_\theta)
={}&\theta'R_C+\frac{\theta'-\alpha^2}{4}\nabla_\eta^2f\cr
&+\big[(\alpha'-a\alpha)r+i(y'-\alpha b/2)\big]\nabla_\eta f\cr
&+\big[(a'-a^2)r^2+i(b'-ab)r+c'-a/2+b^2/4\big]f.
\end{aligned}
\tag{RHR12}
\]
To see all original-zeta terms, expand (\nabla_\eta f=f'+q(\eta)f) and (\nabla_\eta^2f=f''+2q(\eta)f'+(q'(\eta)+q(\eta)^2)f). The time derivative of (C(\varphi_t(s))) is included in the term (\partial_t\varphi_t\,\nabla_\eta f), not omitted. This proves the formula as a meromorphic identity at exceptional points as well.

The conditions for carrying every solution of the original equation to another solution are exactly
\[
\theta'=\alpha^2,\quad\alpha'=a\alpha,\quad y'=\alpha b/2,
\quad a'=a^2,\quad b'=ab,\quad c'=a/2-b^2/4.
\tag{RHR13}
\]
Sufficiency follows from RHR12. For necessity apply the residual to the three original meromorphic solutions (C^{-1}), (\eta C^{-1}), and ((\eta^2+\theta/2)C^{-1}). Their numerator functions are respectively constant, affine, and quadratic caloric solutions, so successively every coefficient in RHR12 must vanish. This is a classification for all solutions in the stated class, not a necessity claim obtained from the single special zeta solution alone.

On the regular interval containing zero where (Q(t)=1-a_0t>0), the full solution is
\[
a=a_0/Q,\quad b=b_0/Q,\quad\alpha=\alpha_0/Q,
\quad y=y_0+\alpha_0b_0t/(2Q),
\]
\[
\theta=\theta_0+\alpha_0^2t/Q,
\quad c=c_0-\tfrac12\log Q-b_0^2t/(4Q).
\tag{RHR14}
\]
Differentiating these expressions and using ((t/Q)'=Q^{-2}) verifies all six equations. The initial source time and all initial factors remain parameters; these maps do not by themselves assert preservation of the original arithmetic initial datum.

Under RHR13 the residual quotient is exactly
\[
\frac{(\partial_t-\mathcal H_C)(T_tf)}{T_tf}
=\alpha^2(R_C/f)\circ\varphi_t.
\tag{RHR15}
\]
Consequently a source double-pole contact coefficient (-m(m-1)/4) remains that same coefficient after pullback. If the target is exceptional for (C), (m) is the numerator order, not necessarily the raw target order (m-e_s). This also follows directly from RHR10: the singular part of ((\nabla f)/f) is ((\operatorname{ord}f+\operatorname{ord}C)/x). Substituting the raw order alone would lose the fixed-factor correction.

## 4. Local units, their curvature, and every marked residue

Write (\chi_t(s_0+x)=\chi_0+\chi_1x+ax^2), and use the units in RHR6. The target raw unit from RHR8 is
\[
\widetilde u(x)=\alpha^{d+e_\eta}e^{\chi_0+\chi_1x+ax^2}
\frac{b_\eta(\alpha x)}{b_s(x)}u(\alpha x).
\tag{RHR16}
\]
For a nonzero unit (v), put (c_v=v'(0)/v(0)) and (\kappa_v=(\log v)''(0)). Derivatives of RHR16 give
\[
c_{\widetilde u}=\chi_1+\alpha(c_u+c_{b_\eta})-c_{b_s},
\]
\[
\boxed{\kappa_{\widetilde u}
=2a+\alpha^2(\kappa_u+\kappa_{b_\eta})-\kappa_{b_s}.}
\tag{RHR17}
\]
At ordinary points of (C), the additional terms are precisely (\alpha^2q'(\eta_0)-q'(s_0)). Thus CT8's formula for the numerator does not give the raw original-zeta unit curvature unless these terms are retained. At exceptional points the regular unit derivatives in RHR17 replace the singular logarithmic derivatives, with the integer orders separately recorded in RHR8.

For any independent marking order (n\ge1), define
\[
\lambda_n(g)=\operatorname{Res}_{h=0}\frac{g(h)}{h^n u(h)}dh,
\qquad
\widetilde\lambda_n(g)=\operatorname{Res}_{x=0}
\frac{g(x)}{x^n\widetilde u(x)}dx.
\]
Substituting (h=\alpha x) gives
\[
\boxed{\widetilde\lambda_n(g)=
e^{-\chi_0}\alpha^{n-d-e_\eta-1}
\lambda_n\!\left(
e^{-\chi_1h/\alpha-ah^2/\alpha^2}
\frac{b_s(h/\alpha)}{b_\eta(h)}g(h/\alpha)\right).}
\tag{RHR18}
\]
All functions inside are taken modulo (h^n). The three powers of (\alpha) arise from (x^{-n}), the raw unit coefficient (\alpha^{d+e_\eta}), and (dx=dh/\alpha). This proves the formula for every integer raw order (d). The marking (n), source order (d), numerator order (d+e_\eta), and target raw order (d+e_\eta-e_s) are not identified. Removing the (b_s/b_\eta) ratio would change the original functionals even at ordinary points where those factors are nonconstant units.

## 5. Complete signed divisors and affine test pullback

Write (D_C=\operatorname{div}C=[1]-\sum_{m\ge1}[-2m]). Since the exponential is everywhere nonzero, RHR4 gives the locally finite divisor identity
\[
\operatorname{div}(T_t\zeta_\theta)
=\varphi_t^*\operatorname{div}\zeta_\theta
+\varphi_t^*D_C-D_C
=\varphi_t^*\operatorname{div}E_\theta-D_C.
\tag{RHR19}
\]
At coincident points the orders add exactly as in RHR8; the underlying factor record keeps each original index and its unit before addition.

Let (R(s)) be rational with (R(s)=O(s^{-2})). Initially suppose its poles avoid the actual divisors being evaluated. Define
\[
\mathscr E_C(R)=R(1)-\sum_{m\ge1}R(-2m),
\qquad
\mathscr R_\theta(R)=\sum_{\operatorname{div}\zeta_\theta}d_\rho R(\rho).
\tag{RHR20}
\]
The moving-zero sum converges absolutely by the order-one zero count; the fixed series converges by the quadratic test decay. Affine pullback retains that decay. Evaluation of RHR19 consequently proves
\[
\boxed{\widetilde{\mathscr R}(R)
=\mathscr R_\theta(R\circ\psi_t)
+\mathscr E_C(R\circ\psi_t)-\mathscr E_C(R).}
\tag{RHR21}
\]
Equivalently its compensated moving-divisor receiver is
\[
\widetilde{\mathscr R}(R)+\mathscr E_C(R)
=\sum_{E_\theta(\rho)=0}m_\rho R(\psi_t(\rho)).
\tag{RHR22}
\]
These are different, specified receivers of the same retained divisor data. Neither the fixed trivial zeros nor the pole at one are discarded from the original signed trace.

## 6. Resonances and the exact rational residue correction

When a rational test pole coincides with a divisor point (p), define its chosen local evaluation by the Laurent constant
\[
\operatorname{FP}_pR=[(s-p)^0]R(s).
\tag{RHR23}
\]
Retain all higher principal coefficients too. This is a specified extension of divisor evaluation, not a limit through singular test parameters. The affine substitution (h=\alpha x) preserves the Laurent constant, so RHR21–22 continue to hold with every evaluation replaced by FP at the finitely many collisions. The original series away from that finite set remains absolutely convergent.

Let (\widetilde l=(T_t\zeta_\theta)'/(T_t\zeta_\theta)), let (P_R) be the finite set of poles of (R), and put (R_2=\lim_{s\to\infty}s^2R(s)). The full residue formula, including collisions, is
\[
\boxed{\begin{aligned}
\widetilde{\mathscr R}^{\rm FP}(R)
={}&-\sum_{p\in P_R}\operatorname{Res}_{s=p}(R(s)\widetilde l(s))
+2aR_2\cr
&+\sum_{p\in P_R\cap\operatorname{supp}\operatorname{div}(T_t\zeta_\theta)}
\operatorname{ord}_p(T_t\zeta_\theta)\operatorname{FP}_pR.
\end{aligned}}
\tag{RHR24}
\]
The last finite sum uses the net signed order at a coincident point. With no test/divisor collision it is empty. The term (2aR_2) is necessary even when all poles are disjoint.

Here is a direct proof. The original numerator logarithmic derivative has its normally convergent genus-one paired series, and
\[
\widetilde l(s)=\chi_s(s)+\alpha(l_\theta+q)(\varphi_t(s))-q(s).
\tag{RHR25}
\]
The complete fixed-factor series is
\[
q(s)=\frac1{s-1}-\frac{\gamma+\log\pi}{2}
+\sum_{m\ge1}\left(\frac1{2m}-\frac1{s+2m}\right).
\tag{RHR26}
\]
Each paired series converges normally on small circles about the finite test-pole set after its finitely many singular terms are separated. A constant times (R) has zero total finite residue because (R=O(s^{-2})). A divisor summand (d/(s-\rho)) contributes (-dR(\rho)) to the sum of residues at the test poles if (\rho\notin P_R). If (\rho\in P_R), that same total is zero by the residue theorem for the rational function (R/(s-\rho)). The missing value is exactly (d\operatorname{FP}_\rho R), yielding the last line of RHR24. Finally
\[
\sum_{p\in P_R}\operatorname{Res}_p(R\chi_s)=2aR_2,
\tag{RHR27}
\]
since (\chi_s=2as+(ib-a)) and the coefficient of (s^{-1}) at infinity is (2aR_2). These facts prove RHR24 with every sign and collision contribution. The same argument yields the source and fixed-factor FP formulas in RHR21, with no growth correction for their order-one logarithmic derivatives.

For explicit local evaluation, if (R=\sum_{j=-M}^\infty r_jx^j) and (\widetilde l=d/x+\sum_{j\ge0}u_jx^j), then
\[
\operatorname{Res}_p(R\widetilde l)=dr_0+\sum_{j=1}^{M}r_{-j}u_{j-1}.
\tag{RHR28}
\]
Thus the finite-pole formula still receives the full regular-unit jets at a collision. RHR23 does not declare those higher coefficients absent.

## 7. The Cauchy receiver and its growth term

Define reflection (s^\#=1-\bar s). Real parameters with (\alpha>0) give (\varphi_t(s^\#)=\varphi_t(s)^\#), and the quadratic gauge satisfies (\overline{\chi_t(1-\bar s)}=\chi_t(s)). The reflected symmetry therefore applies to the full numerator (C(T_t\zeta_\theta)). For the original raw function it is a twisted symmetry with multiplier (C(s)/\overline{C(1-\bar s)}), not an unchanged scalar reflection law.

Put (\widetilde L=\widetilde l+q) and (L_\theta=l_\theta+q). RHR25 proves
\[
\widetilde L(s)=2a(s-\tfrac12)+ib+\alpha L_\theta(\varphi_t(s)).
\tag{RHR29}
\]
For test poles outside the numerator divisor, with (w+\bar z-1\ne0), the full logarithmic receiver is
\[
\mathscr K_{\log}(z,w)
=\frac{\widetilde l(w)+q(w)+\overline{\widetilde l(z)+q(z)}}{w+\bar z-1}
=\alpha^2\mathscr K_\theta(\varphi_tz,\varphi_tw)+2a.
\tag{RHR30}
\]
Indeed (\varphi_tw+\overline{\varphi_tz}-1=\alpha(w+\bar z-1)); the two imaginary linear-gauge contributions cancel, and the quadratic ones sum to (2a(w+\bar z-1)). At a pole of (C), the sum (\widetilde l+q) is interpreted by its actual meromorphic sum before evaluation, not by evaluating two singular terms separately.

For the actual Cauchy test
\[
R_{z,w}(s)=-\frac1{(s-(1-\bar z))(s-w)},
\quad R_{z,w}\circ\psi_t=\alpha^2R_{\varphi_tz,\varphi_tw},
\tag{RHR31}
\]
the compensated divisor receiver is therefore exactly
\[
\mathscr K_{\rm div}(z,w)
=\widetilde{\mathscr R}(R_{z,w})+\mathscr E_C(R_{z,w})
=\alpha^2\mathscr K_\theta(\varphi_tz,\varphi_tw)
=\mathscr K_{\log}(z,w)-2a.
\tag{RHR32}
\]
The rational test has (R_2=-1), agreeing with the growth correction in RHR24. If the test poles hit only the fixed divisor of (C), the separate raw and fixed terms in this formula use RHR23 and cancel to the regular numerator receiver. If a test pole hits a moving numerator zero, the usual Cauchy kernel has a pole; only the explicitly prescribed FP trace is supplied by RHR24. One must not call that a regular value of the original kernel.

## 8. What the sign correction can and cannot change

On finite Cauchy combinations the difference of the two compensated receivers is
\[
2a\left|\sum_jc_j\right|^2.
\tag{RHR33}
\]
It comes from polynomial growth, not a changed moving-zero divisor. On the full rational test space the source's evaluation map together with (\ell_\infty(F)=\lim sF(s)) has dense image in (\mathbb C\oplus\ell^2(\mathcal Z_\theta,m)): orthogonality to the zero-infinity-coefficient tests forces every positive derivative of the Cauchy transform at the chosen pole to vanish, so that transform is constant on the connected complement of the discrete zero set and each residue vanishes. The square-denominator zero-count estimate justifies normal convergence and differentiation. Thus the same density proof remains applicable after the exact affine test pullback; its infinity coefficient is multiplied by (\alpha).

The reflected moving-divisor form is the involution pairing on that weighted sequence space. A two-point reflection orbit contributes one negative direction, and a fixed orbit contributes a positive direction. Adding (\nu|\ell_\infty|^2) adds one negative direction exactly when (\nu<0), as a direct-sum form. Density realizes every finite negative subspace in the rational image, while the negative spectral subspace supplies the upper bound. For the gauge correction in source coordinates, (\nu=2a/\alpha^2). Hence a positive quadratic-gauge correction does not remove a pre-existing negative direction on the complete rational domain. This index statement concerns the explicitly compensated reflected form. It is not a claim of Hermiticity or positivity for the uncompensated full original-zeta signed divisor, whose adjoint defect was proved in OZC17–20.

Every displayed linear map has its fixed-label lift on the actual carrier: nonzero amplitudes remain top-supported; every admitted lower zero is fixed. Independent coefficient functions on lower support points remain separate coordinates. The changes of trace receiver act on their stated scalar or vector values and do not identify supported zero with absence. These comparisons do not supply the missing global positivity estimate for the original arithmetic data.

## Audit status

The incoming RG residual, its regular clocks, the numerator Cauchy correction, and the numerator marked-unit formulas are correct. Their original-zeta reconstruction requires exactly the (C\circ\varphi/C) factor, the full generator RHR10–12, the signed-divisor correction RHR21, the polynomial-growth and collision terms RHR24, and the unit/marked-residue factors RHR17–18. This file was derived independently before reading the owner's new remap manuscript. No owner source, publication, or administrative file was edited.
