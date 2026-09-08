# An exact divergence-free arithmetic heat correspondence

This note extends the explicit two-angular-channel correspondence received from the RH arithmetic task. The source is `[local]/Documents/Erdos Strauss and related/Erdos-Straus-Foundation/research/rh_arithmetic_resolvent_20260908/s6_three_points_heat/ns_heat_correspondence.tex`. Its original map, Fourier convention and positive viscosity are retained below. The additional construction supplies a divergence-free range, a full inverse on that range, the complementary velocity, and the complete nonlinear equations in those coordinates. It proves operator and solution-coordinate identities; it does not construct a singular Navier–Stokes solution or establish a statement about zeros of a zeta function.

## 1. Spaces, coordinates and the original map

Fix the original viscosity \(\nu>0\), and put
\[
\lambda_\nu=2\sqrt\nu,\qquad a_\nu=\sqrt2\,\nu^{1/4}.
\tag{1}
\]
Let \(H=L^2(\mathbb R,ds;\mathbb C^3)\), \(V=L^2(\mathbb R^3,dx;\mathbb C^3)\), and let \(\widehat V\) denote the distinct Fourier-coordinate copy with measure \(d\xi\). Inner products are linear in the first argument. The Fourier convention is
\[
(\mathcal F_3v)(\xi)=(2\pi)^{-3/2}\int_{\mathbb R^3}e^{-ix\cdot\xi}v(x)\,dx.
\tag{2}
\]
We use its Plancherel extension. Thus \(\mathcal F_3:V\to\widehat V\) is unitary, and \(\mathcal F_3(\partial_{x_j}v)=i\xi_j\mathcal F_3v\) on the corresponding derivative domain. The Fourier foundation is the same one used in the incoming note; no assertion of a new proof of Plancherel is made here.

For \(\xi=\rho\omega\), \(\rho>0\), \(\omega\in S^2\), define
\[
Y_0(\omega)=(4\pi)^{-1/2},\qquad
Y_1(\omega)=\sqrt{3/(4\pi)}\,\omega_3.
\tag{3}
\]
The incoming map, now applied to vectors component by component, is
\[
(J_\nu h)(\rho\omega)=\frac{a_\nu}{\rho}
\left[Y_0(\omega)h(\lambda_\nu\rho)
      +Y_1(\omega)h(-\lambda_\nu\rho)\right].
\tag{4}
\]
The value at \(\xi=0\) is immaterial. Since \(Y_0,Y_1\) are orthonormal on the sphere and \(a_\nu^2=\lambda_\nu\), polar integration gives
\[
\|J_\nu h\|_{\widehat V}^2
=a_\nu^2\int_0^\infty
 (|h(\lambda_\nu\rho)|^2+|h(-\lambda_\nu\rho)|^2)\,d\rho
=\|h\|_H^2.
\tag{5}
\]
Its adjoint, for vector angular coefficients \(g_j(\rho)=\int_{S^2}Y_j(\omega)g(\rho\omega)\,d\omega\), is
\[
(J_\nu^*g)(s)=
\begin{cases}
\rho g_0(\rho)/a_\nu,&s>0,\quad\rho=s/\lambda_\nu,\\
\rho g_1(\rho)/a_\nu,&s<0,\quad\rho=-s/\lambda_\nu.
\end{cases}
\tag{6}
\]
Indeed the inner product in (4) has factor \(a_\nu\rho\,d\rho\), whereas substituting (6) into the \(H\) inner product has factor \(\lambda_\nu\rho/a_\nu\,d\rho\); these factors agree by (1). This proves the adjoint formula for the full vector spaces.

The physical divergence-free space and its Fourier image are
\[
V_\sigma=\{v\in V:\operatorname{div}_xv=0\text{ in distributions}\},
\qquad
\widehat V_\sigma=\{g\in\widehat V:\xi\cdot g(\xi)=0\text{ a.e.}\}.
\tag{7}
\]
These are mapped onto each other by \(\mathcal F_3\): testing the distributional divergence against Schwartz functions and applying (2) gives the multiplier \(i\xi\cdot g\). Its vanishing as a distribution is equivalent to its almost-everywhere vanishing, since \(\xi\cdot g\) is locally integrable. In particular, \(\widehat V_\sigma\) is not the kernel of differentiation with respect to \(\xi\).

## 2. The original range and incompressibility

There is an exact statement
\[
\operatorname{ran}(J_\nu)\cap\widehat V_\sigma=\{0\}.
\tag{8}
\]
To prove it, fix a radius for which the transversality equation holds for almost every angular coordinate. Multiplying the angular coefficients by their nonzero fixed constants reduces the equation, without changing the field, to
\[
\omega\cdot b+\omega_3\,\omega\cdot c=0,
\qquad
b=(4\pi)^{-1/2}h(\lambda_\nu\rho),\quad
c=\sqrt{3/(4\pi)}h(-\lambda_\nu\rho).
\tag{9}
\]
The left side is continuous on the sphere; an almost-everywhere zero continuous function is zero everywhere. Evaluating at \(\omega\) and \(-\omega\) gives separately \(\omega\cdot b=0\) and \(\omega_3\omega\cdot c=0\). Evaluation at the three coordinate unit vectors proves \(b=0\). For \(c\), evaluation at \(e_3\), \((e_1+e_3)/\sqrt2\) and \((e_2+e_3)/\sqrt2\) proves \(c_3=c_1=c_2=0\). Hence both half-line values of \(h\) vanish almost everywhere, proving (8).

Equation (8) describes this particular componentwise range. The following explicit map places the same arithmetic space isometrically inside the divergence-free space.

## 3. Leray projection and its complete angular Gram matrix

For \(\omega\in S^2\), set
\[
L(\omega)=I-\omega\omega^{\mathsf T},\qquad
(Lg)(\rho\omega)=L(\omega)g(\rho\omega).
\tag{10}
\]
The coordinate identities \(L^{\mathsf T}=L\), \(L^2=L\), and \(\omega^{\mathsf T}L=0\) prove that \(L\) is the orthogonal projection \(\widehat V\to\widehat V_\sigma\). The physical projection is \(\mathbb P=\mathcal F_3^{-1}L\mathcal F_3\). Values assigned at the origin do not affect these operators.

The sphere integrals needed for the entire calculation are
\[
\begin{aligned}
\int_{S^2}\omega_i\omega_j\,d\omega&=\frac{4\pi}{3}\delta_{ij},\\
\int_{S^2}\omega_i\omega_j\omega_3^2\,d\omega
&=\frac{4\pi}{15}(\delta_{ij}+2\delta_{i3}\delta_{j3}).
\end{aligned}
\tag{11}
\]
Off-diagonal integrals vanish by reflection in one coordinate. Equality of the three second moments and their sum \(4\pi\) gives the first line. In polar coordinates about the third axis, \(d\omega=d\varphi\,dz\), \(-1<z<1\), so \(\int\omega_3^4=2\pi\int_{-1}^1z^4\,dz=4\pi/5\). The other two fourth moments in (11) are equal; their sum is \(\int\omega_3^2(1-\omega_3^2)=4\pi/3-4\pi/5\). Each is therefore \(4\pi/15\), as displayed.

For arbitrary \(b,c\in\mathbb C^3\), equations (3), (10), and (11) give
\[
\begin{aligned}
\int_{S^2}|L(\omega)[Y_0b+Y_1c]|^2\,d\omega
={}&\frac23(|b_1|^2+|b_2|^2+|b_3|^2)\\
&+\frac45(|c_1|^2+|c_2|^2)+\frac25|c_3|^2.
\end{aligned}
\tag{12}
\]
For completeness, \(|Lz|^2=|z|^2-|\omega\cdot z|^2\). The \(Y_0\) contribution to the removed term is \(|b|^2/3\); the \(Y_1\) contribution is \((|c_1|^2+|c_2|^2+3|c_3|^2)/5\). The cross term integrates to zero under \(\omega\mapsto-\omega\). Subtracting these displayed quantities from \(|b|^2+|c|^2\) proves (12), including all complex cross terms. Equivalently, the complete operator \(G=J_\nu^*LJ_\nu\) is
\[
(Gh)(s)=
\begin{cases}
\frac23 h(s),&s>0,\\
\operatorname{diag}(\frac45,\frac45,\frac25)h(s),&s<0.
\end{cases}
\tag{13}
\]
The off-diagonal entries vanish by the same reflection calculations; thus (13) follows either entry by entry or by the polarization identity applied to (12) and (5).

Define the explicit, bounded, invertible, self-adjoint arithmetic-coordinate operator
\[
(Dh)(s)=
\begin{cases}
\sqrt{3/2}\,h(s),&s>0,\\
\operatorname{diag}(\sqrt5/2,\sqrt5/2,\sqrt{5/2})h(s),&s<0.
\end{cases}
\tag{14}
\]
Its inverse has positive branch \(\sqrt{2/3}I\) and negative branch \(\operatorname{diag}(2/\sqrt5,2/\sqrt5,\sqrt{2/5})\). No viscosity, spatial coordinate, time, or source field has been replaced. Equations (13)–(14) give \(DGD=I\) and \(G=D^{-2}\) with their literal factors.

## 4. The isometry, its range, inverse and reality

Set
\[
K_\nu=\mathcal F_3^{-1}LJ_\nu D:H\longrightarrow V_\sigma.
\tag{15}
\]
Its adjoint as an operator into the full space \(V\) is
\[
K_\nu^*=D J_\nu^*L\mathcal F_3:V\longrightarrow H.
\tag{16}
\]
Every factor is bounded, so the adjoint of the product follows directly by successive inner-product identities. Equations (10) and (13) prove
\[
K_\nu^*K_\nu=D J_\nu^*L^2J_\nu D=DGD=I,
\qquad\|K_\nu h\|_V=\|h\|_H.
\tag{17}
\]
Consequently the range \(W_\nu=\operatorname{ran}(K_\nu)\) is closed, its inverse is the restriction of (16), and \(P_\nu=K_\nu K_\nu^*\) is its orthogonal projection on all of \(V\). Its kernel is exactly \(W_\nu^\perp\).

Here is an explicit coordinate description of the range and inverse. Define six real vector functions on the sphere by
\[
\begin{aligned}
U_j^+(\omega)&=\sqrt{3/2}\,Y_0(\omega)L(\omega)e_j,\quad j=1,2,3,\\
U_j^-(\omega)&=d_jY_1(\omega)L(\omega)e_j,\quad
(d_1,d_2,d_3)=(\sqrt5/2,\sqrt5/2,\sqrt{5/2}).
\end{aligned}
\tag{18}
\]
Their pairwise inner products are \(\delta_{ij}\) within each sign and zero between signs by (12)–(14). All six satisfy \(\omega\cdot U_j^\pm=0\). Formula (15) becomes
\[
\widehat{K_\nu h}(\rho\omega)=\frac{a_\nu}{\rho}
\sum_{j=1}^3\left[U_j^+(\omega)h_j(\lambda_\nu\rho)
+U_j^-(\omega)h_j(-\lambda_\nu\rho)\right].
\tag{19}
\]
Thus \(W_\nu\) consists exactly of physical fields whose Fourier angular functions belong to the span of these six functions at almost every radius. Arbitrary square-integrable radial coefficients are allowed. The inverse radial substitution in (19) proves this asserted surjectivity onto the described range, using \(a_\nu^2=\lambda_\nu\) to verify integrability. In particular this subspace, though its parametrization depends on \(\nu\), is the same angular subspace for every positive \(\nu\).

For every \(v\in V\), (16) has the component formula
\[
(K_\nu^*v)_j(s)=
\begin{cases}
\displaystyle\frac\rho{a_\nu}\int_{S^2}U_j^+(\omega)\cdot\widehat v(\rho\omega)\,d\omega,&s>0,\\
\displaystyle\frac\rho{a_\nu}\int_{S^2}U_j^-(\omega)\cdot\widehat v(\rho\omega)\,d\omega,&s<0,
\end{cases}
\quad \rho=|s|/\lambda_\nu.
\tag{20}
\]
The six functions are real, so no conjugates have been suppressed in (20). The kernel consists exactly of fields whose six displayed angular coefficients vanish almost everywhere. On the Fourier side \(P_\nu\) is the orthogonal projection onto these six angular functions at each radius.

The reality condition is also exact. Put
\[
(C_Hh)(s)=\begin{cases}\overline{h(s)},&s>0,\\-\overline{h(s)},&s<0.\end{cases}
\tag{21}
\]
Since \(U_j^+(-\omega)=U_j^+(\omega)\) and \(U_j^-(-\omega)=-U_j^-(\omega)\), (19) and the identity \(\widehat{\overline v}(\xi)=\overline{\widehat v(-\xi)}\) prove
\[
K_\nu C_Hh=\overline{K_\nu h}.
\tag{22}
\]
Injectivity of \(K_\nu\) then proves that its physical velocity is real if and only if \(h(s)\) is real for almost every \(s>0\) and purely imaginary for almost every \(s<0\). Thus the real physical state space is retained rather than silently identified with all complex arithmetic coordinates.

## 5. The full heat-generator domains

Define
\[
\begin{aligned}
(Ah)(s)&=s^2h(s)/4,&
\operatorname{Dom}(A)&=\{h\in H:\int_{\mathbb R}s^4|h(s)|^2/16\,ds<\infty\},\\
B_\nu v&=-\nu\Delta v,&
\operatorname{Dom}(B_\nu)&=\{v\in V:\int_{\mathbb R^3}\nu^2|\xi|^4|\widehat v(\xi)|^2\,d\xi<\infty\}.
\end{aligned}
\tag{23}
\]
Both are multiplication operators in the indicated coordinates. The pointwise equality
\[
\nu\rho^2=(\lambda_\nu\rho)^2/4=(-\lambda_\nu\rho)^2/4
\tag{24}
\]
commutes with every angular factor in (19). The polar norm calculation with an additional factor \((\nu\rho^2)^2\) proves, without an unbounded-operator interchange,
\[
K_\nu h\in\operatorname{Dom}(B_\nu)\ \Longleftrightarrow\ h\in\operatorname{Dom}(A),
\quad B_\nu K_\nu h=K_\nu Ah,
\quad\|B_\nu K_\nu h\|_V=\|Ah\|_H.
\tag{25}
\]
Since the six-channel projection acts at each radius, \(P_\nu\) commutes with the radial multipliers and preserves their domains. For \(v\in\operatorname{Dom}(B_\nu)\), (20) or the projected norm bound therefore gives \(K_\nu^*v\in\operatorname{Dom}(A)\) and \(K_\nu^*B_\nu v=AK_\nu^*v\). The identical argument proves these statements for every nonnegative integer power, retaining the factors \((\nu\rho^2)^m\) and \(s^{2m}/4^m\).

For all \(t\ge0\), pointwise multiplication further gives
\[
e^{-tB_\nu}K_\nu=K_\nu e^{-tA},\qquad
K_\nu^*e^{-tB_\nu}=e^{-tA}K_\nu^*.
\tag{26}
\]
Here the exponentials are respectively the explicit bounded multipliers \(e^{-t\nu|\xi|^2}\) and \(e^{-ts^2/4}\); dominated convergence proves their strong continuity. In the incoming arithmetic convention \(W_z=e^{zA}\), physical forward time remains \(z=-t\). No positive-time backward heat operator is asserted bounded on \(H\).

## 6. An invertible decomposition of every divergence-free velocity

Let \(V_{\sigma,c}=V_\sigma\cap W_\nu^\perp\). The map
\[
\mathcal T_\nu:V_\sigma\longrightarrow H\oplus V_{\sigma,c},\qquad
\mathcal T_\nu u=(h,w)=(K_\nu^*u,(I-P_\nu)u)
\tag{27}
\]
is onto and one-to-one, with
\[
\mathcal T_\nu^{-1}(h,w)=K_\nu h+w,
\qquad\|u\|_V^2=\|h\|_H^2+\|w\|_V^2.
\tag{28}
\]
Indeed \(P_\nu u\in V_\sigma\), so \(w\in V_\sigma\) and is perpendicular to \(W_\nu\). Conversely \(K_\nu^*w=0\), \(P_\nu K_\nu h=K_\nu h\), and \(P_\nu w=0\); substitution proves both inverse identities and the orthogonal norm equality. Complex conjugation preserves both subspaces by (22) and the reality of the angular projection. Therefore the real version of (27)–(28) is obtained exactly by imposing (21) on \(h\) and ordinary physical reality on \(w\).

The operators are nonlocal in physical space. Formula (28) retains any compact support of the original \(u\) as a property of the sum; it does not assert compact support of its two separate summands. Their smoothness on a compact time interval follows from (25) for every power whenever \(u\) and its time derivatives belong to every corresponding Sobolev domain. One can verify the required continuous derivative representatives directly: if \(v\in\operatorname{Dom}(B_\nu^m)\) for every \(m\), Cauchy–Schwarz makes \(|\xi|^k\widehat v\) integrable by choosing \(2m>k+3/2\); its inverse Fourier integral is then a bounded continuous derivative of order \(k\). Thus no spatial support or smoothness has been silently transferred to a different norm.

## 7. All nonlinear, pressure and forcing terms

We retain the physical variables \((x,t,u,p,f,\nu)\) of the incoming source. On a fixed compact time interval before its endpoint, smooth fields with a fixed compact spatial support have all the derivative and integrability properties used below. Write the convection components in full as
\[
N_i(u)=\sum_{j=1}^3u_j\partial_{x_j}u_i,\qquad i=1,2,3.
\tag{29}
\]
For the actual divergence-free velocity, define \((h,w)\) by (27). The complete component expansion is
\[
\begin{aligned}
N_i(K_\nu h+w)=\sum_{j=1}^3\big[&
(K_\nu h)_j\partial_{x_j}(K_\nu h)_i
+(K_\nu h)_j\partial_{x_j}w_i\\
&+w_j\partial_{x_j}(K_\nu h)_i
+w_j\partial_{x_j}w_i\big].
\end{aligned}
\tag{30}
\]
Set \(Q_\nu=I-P_\nu\), and define the physical solenoidal source
\[
F_\sigma=\mathbb P[f-N(K_\nu h+w)].
\tag{31}
\]
Application of \(\mathbb P\) to the physical equation, followed by (25) and (27), gives exactly
\[
\begin{aligned}
\partial_t h+Ah&=K_\nu^*F_\sigma,\\
\partial_t w+B_\nu w&=Q_\nu F_\sigma,\\
h(0)&=K_\nu^*u(0),\qquad w(0)=Q_\nu u(0).
\end{aligned}
\tag{32}
\]
The pressure is retained by the additional exact equation
\[
\nabla p=(I-\mathbb P)[f-N(K_\nu h+w)].
\tag{33}
\]
To justify the pressure step explicitly, Fourier transformation of \(\nabla p\in L^2\) gives a vector parallel to \(\xi\), so \(L\widehat{\nabla p}=0\). The vectors \(\partial_tu\) and \(B_\nu u\) remain solenoidal by differentiation of (7). Consequently projecting the original equation onto the orthogonal complement of \(V_\sigma\) gives (33). Thus no condition on the divergence of the original force has been added.

These calculations are reversible. For fields with the displayed smoothness and domain properties, the initial conditions in (32), the constraint \(w(t)\in V_{\sigma,c}\), and equation (33), apply \(K_\nu\) to the first equation of (32) and add the second. By (25) and \(P_\nu+Q_\nu=I\), the result is
\[
\partial_t(K_\nu h+w)+B_\nu(K_\nu h+w)=\mathbb P[f-N(K_\nu h+w)].
\tag{34}
\]
Adding (33), with its actual gradient and sign, proves
\[
\partial_tu+N(u)-\nu\Delta u+\nabla p=f,
\qquad \operatorname{div}_xu=0,
\quad u=K_\nu h+w.
\tag{35}
\]
Equations (27) and (28) prove exact inverse maps on this solution data. The additive spatially constant value of \(p\), if allowed by the chosen physical pressure class, is retained as part of the data; no inverse of the gradient that would discard it has been claimed.

The associated integral equations retain all the same terms:
\[
\begin{aligned}
h(t)&=e^{-tA}h(0)+\int_0^te^{-(t-s)A}K_\nu^*F_\sigma(s)\,ds,\\
w(t)&=e^{-tB_\nu}w(0)+\int_0^te^{-(t-s)B_\nu}Q_\nu F_\sigma(s)\,ds.
\end{aligned}
\tag{36}
\]
On each stated compact time interval, \(F_\sigma\) is continuous in the Hilbert space. The contractions in (26) make these Bochner integrals well defined. Taking their Fourier multipliers gives the scalar integrating-factor identity at almost every frequency. Differentiation on the actual smooth domain, or integration of (32) with this scalar identity, proves both directions between (32) and (36). Equations (30)–(36) show explicitly where the angular complement re-enters the arithmetic equation. Dropping \(w\) or any term of (30) would change the dynamics; no such deletion is made.

## 8. Exact energy and a concrete supremum-norm test

Equations (27)–(28) prove for every time at which the physical velocity is in \(L^2\)
\[
\frac12\int_{\mathbb R^3}|u(x,t)|^2\,dx
=\frac12\int_{\mathbb R}|h(s,t)|^2\,ds
+\frac12\int_{\mathbb R^3}|w(x,t)|^2\,dx.
\tag{37}
\]
For each derivative order, the analogous radial generator identity is
\[
\|B_\nu^m u\|_V^2=\|A^mh\|_H^2+\|B_\nu^mw\|_V^2,
\tag{38}
\]
on exactly the domains in (25). This follows from commutation of the angular projection with the radial multiplier and the same orthogonality.

Even the six-channel divergence-free range has no bounded map from its \(L^2\) norm to its physical supremum norm. Here is a full explicit calculation. Choose a real nonnegative nonzero \(\varphi\in C_c^\infty((1,2))\). For \(R>0\), put
\[
h_R(s)=\frac{R^{-1/2}}{\|\varphi\|_{L^2(\mathbb R)}}\varphi(s/R)e_3,
\qquad v_R=K_\nu h_R.
\tag{39}
\]
Its negative half-line values vanish, and substitution \(s=Rr\) proves \(\|h_R\|_H=\|v_R\|_V=1\). Formula (22) proves that \(v_R\) is real. Its Fourier transform is smooth and compactly supported in the annulus \(R/\lambda_\nu<\rho<2R/\lambda_\nu\), hence \(v_R\) is a smooth rapidly decreasing divergence-free field. Repeated integration by parts in the inverse Fourier integral proves the asserted rapid decrease; the frequency support is away from the origin and all derivatives vanish at its boundary.

The exact angular integral is
\[
\int_{S^2}U_3^+(\omega)\,d\omega
=\sqrt{3/2}\,(4\pi)^{-1/2}\frac{8\pi}{3}e_3,
\tag{40}
\]
because \(\int L(\omega)e_3=4\pi e_3-(4\pi/3)e_3\). Evaluating the absolutely convergent inverse Fourier integral at \(x=0\), including its polar factor \(\rho^2\), now gives
\[
\begin{aligned}
v_R(0)&=C_{\nu,\varphi}R^{3/2}e_3,\\
C_{\nu,\varphi}
&=(2\pi)^{-3/2}\frac{a_\nu}{\lambda_\nu^2}
\sqrt{3/2}\,(4\pi)^{-1/2}\frac{8\pi}{3}
\frac{\int_1^2r\varphi(r)\,dr}{\|\varphi\|_{L^2(\mathbb R)}}>0.
\end{aligned}
\tag{41}
\]
Indeed \(\int_0^\infty\rho\varphi(\lambda_\nu\rho/R)\,d\rho
=(R^2/\lambda_\nu^2)\int_1^2r\varphi(r)\,dr\), which accounts for every factor in (41). Therefore \(\|v_R\|_\infty\ge C_{\nu,\varphi}R^{3/2}\) with \(\|v_R\|_2=1\).

This is a family of states with an exact inverse and norm calculation. The parameter \(R\) is not physical time, and no trajectory through this family solving (35) has been asserted. It proves precisely that bounded arithmetic Hilbert norm does not control physical velocity supremum, including inside this divergence-free image. The full dynamics relevant to a particular trajectory remain (30)–(36).

## 9. Application to the actual source witness, with its existence dependency retained

The frozen 166-page manuscript is `[local]/Documents/math/output/navier_stokes_research_2026-09-08/downloaded_public_release/navier-stokes.pdf`, SHA256 `0e779481c4da40bd28d1e642e1d8ca57447d129610df28dfa5a11e9af8ae228f`. Its equations (9.21), (10.4), (10.5) and (10.11) define the cutoff-summed, localized velocity, pressure and smoothly extended force. Denote that viscosity-one triple by \((u_*,p_*,f_*)\). Its stated existence and preceding increment estimates are imported source results here. The correspondence calculation in this section does not replace that construction's proof.

For the given physical viscosity \(\nu>0\), retain the source's spatial map and time:
\[
u_\nu(x,t)=\sqrt\nu\,u_*(x/\sqrt\nu,t),\qquad
p_\nu(x,t)=\nu p_*(x/\sqrt\nu,t),\qquad
f_\nu(x,t)=\sqrt\nu\,f_*(x/\sqrt\nu,t).
\tag{42}
\]
Every term in \(\partial_tu_\nu+(u_\nu\cdot\nabla_x)u_\nu-\nu\Delta_xu_\nu+\nabla_xp_\nu\) equals \(\sqrt\nu\) times the corresponding viscosity-one term evaluated at \(x/\sqrt\nu\). For example \(\partial_{x_j}(u_\nu)_i=(\partial_{y_j}u_{*,i})(y,t)\), \(\Delta_x(u_\nu)_i=\nu^{-1/2}\Delta_yu_{*,i}\), and \(\partial_{x_i}p_\nu=\sqrt\nu\partial_{y_i}p_*\), where \(y=x/\sqrt\nu\). This proves the exact residual and force relation, including zero initial data, divergence, unchanged endpoint time, support \(\sqrt\nu K_*\), and the inverse obtained by \(x=\sqrt\nu y\). The volume factor is \(dx=\nu^{3/2}dy\), giving
\[
\|u_\nu(t)\|_2^2=\nu^{5/2}\|u_*(t)\|_2^2,
\qquad \|u_\nu(t)\|_\infty=\sqrt\nu\|u_*(t)\|_\infty.
\tag{43}
\]

Apply the proved inverse pair (27)–(28) to these actual source fields, at each \(0\le t<1\):
\[
h_\nu(t)=K_\nu^*u_\nu(t),\qquad
w_\nu(t)=(I-P_\nu)u_\nu(t),\qquad
u_\nu(t)=K_\nu h_\nu(t)+w_\nu(t).
\tag{44}
\]
The complete projected equations are (30)–(36) with \((h,w,p,f)=(h_\nu,w_\nu,p_\nu,f_\nu)\), and both initial coordinates are zero. Thus their forcing and nonlinear terms are the actual ones defined by (42), rather than an independently chosen input. Formula (37) and the source's bounded energy give
\[
\|h_\nu(t)\|_H^2+\|w_\nu(t)\|_V^2
=\nu^{5/2}\|u_*(t)\|_2^2.
\tag{45}
\]

The source's (10.20)–(10.21) retain \(A=1/2+h\), \(0<h<1/100\), \(X_{\rm in}>0\), \(e_0>0\), and an actual remainder \(R_*(\tau)=O(\tau^{2h})\). Its positive inner-circle swirl has Cartesian second component at
\[
x_{\nu,\tau}=(\sqrt{2\nu X_{\rm in}\tau},0,0),\qquad t=1-\tau.
\tag{46}
\]
Substitution in the exact inverse (44), retaining the whole remainder, gives the concrete arithmetic-and-complement value
\[
\big[K_\nu h_\nu(1-\tau)+w_\nu(1-\tau)\big]_2(x_{\nu,\tau})
=\sqrt\nu\,\tau^{-1/2-h}\big(e_0+R_*(\tau)\big).
\tag{47}
\]
The pointwise evaluation is justified on every preterminal time by the actual smooth source and the all-order domain argument following (28). If \(|R_*(\tau)|\le C_*\tau^{2h}\) for \(0<\tau<\tau_*\), then for \(C_*>0\) and
\(0<\tau<\min\{\tau_*,(e_0/(2C_*))^{1/(2h)}\}\), equation (47) is at least \(\sqrt\nu e_0\tau^{-1/2-h}/2\); if \(C_*=0\), the same inequality holds throughout \((0,\tau_*)\). The triangle inequality therefore yields
\[
\|K_\nu h_\nu(1-\tau)\|_\infty+\|w_\nu(1-\tau)\|_\infty
\ge \frac{\sqrt\nu e_0}{2}\tau^{-1/2-h}.
\tag{48}
\]
Equations (45), (47) and (48) specify the actual transported bounded-energy and supremum-growth statements. They do not assign the growth to either angular component separately; that requires calculating the source's six angular coefficients in (20). No zeta-zero assertion follows from this coordinate identity. The source existence dependency and the retained angular complement are explicit throughout the application.

## 10. Provenance and verification scope

The incoming RH note supplies (1)–(6), the multiplier \(s^2/4\), and its scalar forced-heat interpretation. Sections 2–9 above add the typed transversality result, the Leray angular Gram calculation, six-channel divergence-free isometry, exact complement, reality, full nonlinear and pressure equations, the explicit fixed-energy supremum-norm family, and the application to the actual source witness. The projection and Fourier foundations are stated in their actual spaces; the finite-dimensional, integral, domain, and dynamical calculations are displayed in full.

An independent bounded reviewer checked the Gram factors, operator adjoint, isometry and reality calculation. The reviewer required one type clarification before writing: the spectral constraint is \(\xi\cdot g(\xi)=0\), not differentiation of \(g\) with respect to \(\xi\); (7) implements that correction. The review does not certify the incoming manuscript's Navier–Stokes construction or all prior arithmetic results. No Lean, Lake, Elan, source-download code, or cumulative publication build was executed for this note.
