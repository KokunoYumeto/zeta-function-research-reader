# Unified Flow with a black hole in the equations

11 September 2026. Working derivation and research interfaces; not an independent mathematical review.

## 1. Physical systems and source history

Choose an eternal, uncharged, nonrotating four-dimensional Schwarzschild black hole of mass M>0, in Einstein gravity with Newton constant G. A static laboratory is held at areal radius R>r_h. Quantum fields are treated as test fields in Hartle–Hawking equilibrium. This has incoming as well as outgoing thermal excitations, not the state of an isolated evaporating black hole. Backreaction of the entire equilibrium bath is not being solved. Comparisons between nearby stationary masses below are separate variations. [1–3]

Keep three probes distinct:

* A free, real, minimally coupled massless scalar in four dimensions, measured by a monopole Unruh–DeWitt detector. Its actual radial scattering problem is specified in Section 5.
* A massless conformal scalar on the two-dimensional radial metric, measured by a derivative-coupled two-level detector. This explicitly omits the angular potential and the dilaton factors of literal spherical reduction. Its peak is exactly calculable. [4]
* A massless complex Dirac field confined to a round test shell of radius R, propagation speed c, zero chemical potential and the round-sphere spin structure. Populate its positive particle and antiparticle excitations at the local equilibrium temperature. This is a thermal surface probe, not an asserted microscopic model of the horizon.

Section 9 adds a separately identified interacting sigma-model probe rather than inventing an interaction beta function for the free Dirac field.

Historical sources: `206.tex`, lines 1585–1709, contains the detector-to-scale calculation; `A figment of acceleration.pdf`, extracted text lines 212–276, proposes the Hartle–Hawking/modular/spectral-entropy application; `OLDER notes that have stuff on Ricci flow.txt`, lines 67–107, contains Schwarzschild thermodynamic comparisons. The old entropy-quantization postulate is not assumed. Those originals are not republished here, and their theorem headings are not verification certificates. CONTRIBUTIONS.md records the user-attested Gemini 2.5 Pro origin of modular action.

## 2. Geometry, thermal state, and exact clock conversions

Retain all dimensional constants. Put

$$r_h=\frac{2GM}{c^2},\quad f(r)=1-\frac{r_h}{r},\quad N=\sqrt{f(R)},\quad \ell_P^2=\frac{G\hbar}{c^3}.$$

The metric and laboratory clock are

$$ds_{\mathrm{geom}}^2=-f(r)c^2dt^2+f(r)^{-1}dr^2+r^2d\Omega_2^2,\qquad d\tau_R=Ndt.$$

Contraction of a momentum with the Killing field and the static unit tangent gives the energy map

$$E_\infty=NE_R.$$

Surface gravity in acceleration units, with Killing time normalized at infinity, is

$$\kappa=\frac{c^2f'(r_h)}2=\frac{c^2}{2r_h}=\frac{c^4}{4GM}.$$

Euclidean regularity fixes the thermal circle:

$$\hbar\beta_H=\frac{2\pi c}{\kappa}=\frac{4\pi r_h}{c},\qquad k_BT_H=\frac{\hbar c}{4\pi r_h}.$$

The proper thermal period is redshifted by N, so

$$\boxed{\beta_R=N\beta_H,\quad T_R=T_H/N,\quad \beta_RE_R=\beta_HE_\infty.}$$

These are the Tolman/KMS relations for the chosen state. [1–3]

The accelerometer reading follows from u^t=1/N and Gamma^r_tt=c^2ff'/2:

$$a_{\mathrm{stat}}=\frac{c^2f'(R)}{2N}=\frac{GM}{R^2N}.$$

Define the acceleration-valued thermal scale and retain the conversion factor:

$$a_{\mathrm{KMS}}:=\frac{2\pi ck_BT_R}{\hbar}=\frac\kappa N,\qquad
\boxed{a_{\mathrm{stat}}=(r_h/R)^2a_{\mathrm{KMS}}.}$$

The ratio tends to one near the horizon and is 1/4 at R=2r_h. Thus the local Rindler limit is visible without replacing the exact Schwarzschild relation.

The proper distance on a static slice is

$$\rho(R)=\sqrt{R(R-r_h)}+r_h\log\frac{\sqrt R+\sqrt{R-r_h}}{\sqrt{r_h}},\qquad \frac{d\rho}{dR}=\frac1N.$$

For delta=R-r_h small,

$$\rho=2\sqrt{r_h\delta}\left[1+\frac{\delta}{6r_h}+O(\delta^2/r_h^2)\right],\qquad
k_BT_R=\frac{\hbar c}{2\pi\rho}\left[1+O(\rho^2/r_h^2)\right].$$

The leading local temperature at a fixed proper distance is independent of M.

## 3. The modular action in this physical state

Let alpha_t be Killing-time evolution and fix

$$\sigma_{s_{\mathrm{TT}}}=\alpha_{-\hbar\beta_Hs_{\mathrm{TT}}}.$$

Retain both the reversed coordinate u=-s_TT and its action-valued counterpart J=hbar(u-u_0). Then

$$\boxed{\frac{du}{dt}=\frac1{\hbar\beta_H},\quad
\frac{du}{d\tau_R}=\frac1{\hbar\beta_R},\quad
\frac{dJ}{d\tau_R}=k_BT_R,\quad \frac{dJ}{dt}=k_BT_H.}$$

This measures thermal energy scale per unit proper time. Comparison using the same elapsed Killing time removes the laboratory radius. It is not heat generation: the equilibrium state is invariant under its own modular dynamics.

For finitely many exterior modes, take H_infinity=sum epsilon_j n_j and rho=exp(-beta_H H_infinity)/Z. Then K=-log rho=beta_H H_infinity+log Z; substitution into rho^(is) A rho^(-is) proves the clock relation, with the additive log Z retained in entropy. The continuum exterior uses the algebraic KMS formulation, not a fictitious trace-class density matrix for a type-III local algebra.

## 4. A closed-form black-hole detector channel

For the conformal radial scalar, use

$$r_*=r+r_h\log(r/r_h-1),\quad w_-=t-r_*/c,\quad w_+=t+r_*/c,$$

$$U=-L e^{-\kappa w_-/c},\quad V=L e^{\kappa w_+/c}.$$

With retained field coefficient A_phi, the HHI two-point function is

$$W(x,x')=-A_\phi\log\frac{(U-U'-i0)(V-V'-i0)}{L_0^2}.$$

The additive infrared constant disappears after derivative coupling. At fixed R let p_R=kappa/(cN)=2pi/(hbar beta_R). Direct differentiation gives

$$\partial_\tau\partial_{\tau'}W=-\frac{A_\phi p_R^2}{2}\operatorname{csch}^2\frac{p_R(\tau-\tau'-i0)}2.$$

For H_int=g_d chi m dphi/dtau, stationary leading-order perturbation theory yields

$$\mathcal R_+(\omega)=C_d\frac{\omega}{e^{\hbar\beta_R\omega}-1},\qquad
C_d=\frac{4\pi A_\phi g_d^2|m_{eg}|^2}{\hbar^2}.$$

The Fourier integral is

$$\int_{\mathbb R} e^{-i\omega s}\operatorname{csch}^2\frac{p_R(s-i0)}2\,ds
=-\frac{8\pi\omega}{p_R^2(e^{2\pi\omega/p_R}-1)},\qquad\omega>0.$$

Closing clockwise in the lower half-plane sums the double poles at -2pi i n/p_R+i0, n>=1. The residues form the geometric series giving the displayed sign and coefficient. [4]

Absorbed power in a scanned family of initially ground-state detectors with fixed C_d is

$$P_R(\omega)=C_d\frac{\hbar\omega^2}{e^{\hbar\beta_R\omega}-1}.$$

The invertible coordinate x=hbar beta_R omega gives the positive maximum condition

$$(2-x)e^x=2,\qquad k_*=2+W_0(-2e^{-2})=1.593624260040040\ldots.$$

Uniqueness follows because 2(1-e^(-x))-x has positive initial derivative, strictly negative second derivative, and becomes negative; the power tends to zero at both endpoints. The other real Lambert branch gives the endpoint x=0.

Consequently

$$\boxed{\mu_R=\frac{k_*}{\beta_R}=\frac{k_*\hbar c}{4\pi r_hN},\qquad
\mu_\infty=N\mu_R=\frac{k_*\hbar c}{4\pi r_h}.}$$

This is not equilibrium net detector power: excitation and de-excitation balance once the detector equilibrates. It is not a universal peak for every black-hole detector or for outgoing Hawking luminosity.

## 5. The four-dimensional field and its remaining numerical calculation

The original four-dimensional scalar has unit-Klein–Gordon-normalized in/up modes satisfying

$$\frac{d^2u_{\nu\ell}}{dr_*^2}+\left[\frac{\nu^2}{c^2}-f(r)\left(\frac{\ell(\ell+1)}{r^2}+\frac{r_h}{r^3}\right)\right]u_{\nu\ell}=0.$$

The in solution is incoming from past null infinity; the up solution is incoming from the past horizon. Their incoming KG flux fixes normalization. Let J_R(nu) be the sum over their squared normalized amplitudes, including ell,m, at the laboratory. This is a specified scattering boundary-value problem. [3]

$$W_R(s)=\int_0^\infty J_R(\nu)\left[(1+n_H(\nu))e^{-i\nu s/N}+n_H(\nu)e^{i\nu s/N}\right]d\nu,$$

$$n_H(\nu)=(e^{\hbar\beta_H\nu}-1)^{-1}.$$

For monopole coupling,

$$\mathcal R_{+,4}(\omega)=\frac{2\pi g_d^2|m_{eg}|^2N}{\hbar^2}
\frac{J_R(N\omega)}{e^{\hbar\beta_R\omega}-1}.$$

A smooth positive power maximum obeys

$$\boxed{\frac1\omega+N\frac{J_R'(N\omega)}{J_R(N\omega)}
=\frac{\hbar\beta_R}{1-e^{-\hbar\beta_R\omega}}.}$$

A linear density recovers the k_* equation. Curvature scattering can alter it. This pass has not computed J_R numerically. Nevertheless the exact detailed-balance ratio fixes the same thermal clock:

$$\mathcal R_{+,4}(E)/\mathcal R_{-,4}(E)=e^{-\beta_RE}.$$

Thus the physically meaningful thermal measurement survives without assuming the flat-space peak.

## 6. Carry the selected scale into horizon entropy and area

Use Einstein black-hole entropy, not single-mode entropy:

$$S_{\mathrm{BH}}=\frac{k_BA_H}{4\ell_P^2},\quad A_H=4\pi r_h^2,\quad
\sigma:=S_{\mathrm{BH}}/k_B=\frac{4\pi GM^2}{\hbar c}.$$

With E_P=sqrt(hbar c^5/G),

$$\boxed{\mu_\infty=\frac{k_*E_P}{4\sqrt{\pi\sigma}},\quad
\mu_R=\frac{k_*E_P}{4N\sqrt{\pi\sigma}},\quad
\frac{dJ}{dt}=\frac{E_P}{4\sqrt{\pi\sigma}}.}$$

Larger entropy means lower thermal energy and slower modular-action rate at infinity. No arbitrary cutoff occurs in this relation; k_* retains the specified detector observable.

Direct differentiation gives T_H dS_BH=c^2 dM. If a small neutral energy epsilon is absorbed and retained by the hole,

$$\delta S_{\mathrm{BH}}/k_B=\beta_H\epsilon.$$

For epsilon=k_*/beta_H,

$$\boxed{\delta S_{\mathrm{BH}}/k_B=k_*,\qquad \delta A_H=4k_*\ell_P^2.}$$

This is a first-law response, not an area quantum. Actual absorption is required; the existence of a detector response is not a flux into the hole.

The finite stationary-endpoint difference is also explicit:

$$\frac{S(M+\epsilon/c^2)-S(M)}{k_B}=\beta_H\epsilon+\frac{4\pi G\epsilon^2}{\hbar c^5}.$$

Using the initial peak energy gives

$$\boxed{\Delta S_{\mathrm{BH}}/k_B=k_*+k_*^2/(4\sigma).}$$

For a finite faithful thermal reference state, relative entropy gives D(rho||rho_0)=beta_H Delta<E_infinity>-Delta S_field/k_B. Its first variation vanishes at rho=rho_0. This makes the field entanglement first law and the horizon first law share the same modular-energy variation; it does not identify their absolute entropies.

## 7. A specified gravitational action

The equilibrium Schwarzschild Euclidean action, including its asymptotic boundary subtraction, obeys

$$I_E/\hbar=\beta_HMc^2-\sigma=\sigma,$$

using the Smarr identity Mc^2=2T_HS_BH. During one thermal Killing-time interval Delta t=hbar beta_H, the modular-action clock accumulates Delta J=hbar. Hence

$$\boxed{I_E=\sigma\,\Delta J_{\mathrm{thermal}}.}$$

Entropy, rather than a coefficient chosen to be one, is the proportionality. No Wheeler–DeWitt CA identity is asserted.

For a Euclidean opening angle 2pi n, the integrated conical curvature is 4pi(1-n)A_H. Multiplication by the Einstein coefficient -c^3/(16pi G) gives

$$I_E(n)=nI_E(1)+(n-1)\frac{\hbar A_H}{4\ell_P^2}+O((n-1)^2).$$

Therefore

$$\left.(n\partial_n-1)\frac{I_E(n)}\hbar\right|_{n=1}=\frac{A_H}{4\ell_P^2}.$$

This is the semiclassical conical/replica entropy map. Terms linear in the circle length cancel. Renormalized matter adds the corresponding field contribution to generalized entropy, rather than allowing an arbitrary field entropy to stand in for the gravitational term. [5]

## 8. Fully specified fermion: spectrum, purification, entropy, zeta

The round-shell spectral triple is

$$\mathcal A=C^\infty(S^2),\quad\mathcal H=L^2(S^2,S;R^2g_{\mathrm{unit}}),\quad D_R=R^{-1}D_1.$$

Its self-adjoint intrinsic Dirac eigenvalues are plus/minus n/R, n>=1, multiplicity 2n per sign. [6] In the angular-momentum representation D_R=(sigma dot L_ang/hbar+1)/R, where L_ang=-i hbar r cross grad. Coupling orbital angular momentum with spin 1/2 gives those eigenvalue branches.

Fill the negative sea as a reference and use positive particle/antiparticle excitations of one complex massless Dirac field. The one-particle excitation operator H_1,R=hbar c|D_R| has energy E_n,R=hbar c n/R with multiplicity 4n. This fixes the thermal excitation vacuum energy as reference zero; it does not erase a Casimir contribution to gravitational stress.

$$x:=\frac{\beta_R\hbar c}{R}=\frac{4\pi r_hN}{R},\quad
Z_R=\prod_{n\ge1}(1+e^{-xn})^{4n},\quad p_n=(1+e^{xn})^{-1}.$$

The logarithm of Z converges exponentially for every R>r_h. A mode purification and its actual fermionic canonical transformation are

$$|\mathrm{TFD}_n\rangle=\frac{|00\rangle+e^{-xn/2}|11\rangle}{\sqrt{1+e^{-xn}}},$$

$$b_R=\cos\theta_n a_R-\sin\theta_n a_L^\dagger,\quad
b_L=\cos\theta_n a_L+\sin\theta_n a_R^\dagger,\quad
\tan\theta_n=e^{-xn/2}.$$

Fix |11>=a_R^dagger a_L^dagger|00>. Both b operators annihilate the displayed pair and obey the canonical anticommutators. The right reduced modular Hamiltonian is K=sum xn n_operator+log Z_R.

For h(y)=log(1+e^(-y))+y/(1+e^y),

$$\boxed{S_{\mathrm{surf}}/k_B=4\sum_{n\ge1}n h(nx).}$$

The thermal spectral cutoff is now an identified inverse length:

$$\Lambda_{\mathrm{length}}=\frac1{\beta_R\hbar c}=\frac1{4\pi r_hN},\quad
S_{\mathrm{surf}}/k_B=\operatorname{Tr}f_{\mathrm{ent}}(D_R^2/\Lambda_{\mathrm{length}}^2),\quad
f_{\mathrm{ent}}(y)=h(\sqrt y).$$

The cutoff energy is k_BT_R, while the detector energy is k_*k_BT_R. This applies the fermionic entropy/spectral-action connection with an actual operator and multiplicities. [7]

Expanding the two terms of h into alternating exponentials and integrating gives, for Re z>0,

$$\int_0^\infty y^{z-1}h(y)dy=\Gamma(z)(z+1)(1-2^{-z})\zeta(z+1).$$

The sphere excitation spectral zeta is 4(R/(hbar c))^z zeta(z-1), Re z>2. Consequently

$$\boxed{\int_0^\infty x^{z-1}\frac{S(x)}{k_B}dx
=4\Gamma(z)(z+1)(1-2^{-z})\zeta(z+1)\zeta(z-1),\quad\Re z>2.}$$

The operator-specific zeta factor is retained separately from the universal entropy-kernel factor.

The Riemann-sum limit x^2 S(x)/k_B -> 4 integral y h(y)dy = 9 zeta(3), together with x~2pi rho/r_h, yields

$$\boxed{S_{\mathrm{surf}}/k_B\sim\frac{9\zeta(3)}{16\pi^3}\frac{A_H}{\rho^2}.}$$

This is an area-like thermal surface entropy, not a derivation of the coefficient 1/(4 ell_P^2). No distance is chosen to force that match. For contrast, the bulk four-component massless Dirac thermal-atmosphere approximation has s/k_B=(7pi^2/45)(k_BT/(hbar c))^3 and yields S_atm/k_B~7A_H/(720pi epsilon^2). It is a different system and approximation.

### 8.1 Entropy minimum and the actual optical map

At fixed M, b=R/r_h gives x=4pi sqrt(b-1)/b^(3/2) and

$$\frac{d\log x}{db}=\frac{3-2b}{2b(b-1)},\qquad h'(y)=-\frac{ye^y}{(1+e^y)^2}.$$

Therefore S_surf has a unique minimum at R=3r_h/2. This has a concrete relation to the photon sphere, not just a matching number. For an equatorial null geodesic with affine parameter lambda_g, retain E_aff=f c^2 dt/dlambda_g and L_aff=r^2 dphi/dlambda_g. Its radial equation is

$$(dr/d\lambda_g)^2+L_{\mathrm{aff}}^2 f(r)/r^2=E_{\mathrm{aff}}^2/c^2.$$

The circular-null-orbit condition differentiates f/r^2, giving (3r_h-2r)/r^4. The shell's redshifted energies have

$$x(R)^2=(\beta_H\hbar c)^2 f(R)/R^2,\quad
E_{n,\infty}^2=(\hbar cn)^2 f(R)/R^2.$$

Both involve the same optical function, with their different constants retained. Its maximum makes thermal occupation smallest in the surface probe. The shell states are not being identified with photon trajectories; the exhibited map is the optical potential. Novelty is unassessed.

### 8.2 Realizing the detector energy in this shell

For n=1, choose the unique root 1<b_*<3/2 of

$$k_*^2b_*^3-16\pi^2b_*+16\pi^2=0.$$

Since x(b) increases from zero to 8pi/(3sqrt(3))>k_* on this interval, existence and uniqueness follow. Numerically b_*=1.0169122985309438...; a second root R/r_h=7.32761482574454... lies outside the photon sphere. At either location the four lowest excitations have E=mu_R and

$$p_*=(1+e^{k_*})^{-1}=0.168874599760851\ldots,\quad
S_*/k_B=h(k_*)=0.454097251779957\ldots.$$

The binary mode entropy and the horizon response k_* are different observables, now both calculated. All higher shell modes remain in the entropy sum.

## 9. An interacting family with its beta function actually specified

A separate two-dimensional O(3) sigma probe has n:Sigma->S^2 and

$$I_\sigma/\hbar=\frac{Q}{4\pi\alpha'}\int(\partial n)^2
=\frac1{2g_\sigma}\int(\partial n)^2,\qquad g_\sigma=\frac{2\pi\alpha'}Q.$$

Q is target radius squared. Choose M_0=10^30 kg, R_0=2r_h(M_0), Q_0=R_0^2, alpha'=10^(-4)R_0^2, and mu_0=k_*k_BT_H(M_0)/N(M_0,R_0). Equality of the two sphere radii at this reference is a calibration, not a dynamical identity.

At one loop with no target flux or dilaton gradient, [8]

$$\frac{dQ}{d\ell}=\alpha',\quad\frac{dg_\sigma}{d\ell}=-\frac{g_\sigma^2}{2\pi},\quad
Q=Q_0+\alpha'\ell,\quad g_\sigma=\frac{g_0}{1+g_0\ell/(2\pi)}.$$

These solve the truncated equations exactly. The physical approximation requires alpha'/Q small. The actual lab scale map is

$$\boxed{\ell=\log(\mu_R/\mu_0)=-\frac12\log(\sigma/\sigma_0)-\log(N/N_0).}$$

For a parameter lambda indexing stationary experiments,

$$\ell'=-M'/M-N'/N,\quad
 g_\sigma''=\frac{g_\sigma^3}{2\pi^2}(\ell')^2-\frac{g_\sigma^2}{2\pi}\ell''.$$

At fixed M, ell_R=-r_h/[2R(R-r_h)] and ell_RR=r_h(2R-r_h)/[2R^2(R-r_h)^2].

For the same target g_Q=Q g_unit, Ric(g_Q)=g_unit. The Ricci parameter, Dirac family on volume-unitarily identified Hilbert spaces, and their derivatives are

$$dt_g=-\frac{\alpha'}2d\ell,\quad dQ/dt_g=-2,\quad
D_Q=Q^{-1/2}D_1,\quad dD_Q/d\ell=-\frac{\alpha'}{2Q}D_Q.$$

No eigenvalue crosses zero for Q>0: integer spectral flow is zero even though eigenvalue scales change.

Retain any weighted volume V_0>0 and set exp(-f)=V_0/(4pi Q). Then gradient f=0, scalar curvature=2/Q and

$$\boxed{\mathcal F=\frac{2V_0}Q,\quad
\frac{d\mathcal F}{dt_g}=\frac{4V_0}{Q^2},\quad
\mathcal F'=-\frac{2V_0\alpha'}{Q^2}\ell'.}$$

The conjugate heat condition gives f_tg=-2/Q; the integral 2 integral |Ric|^2 exp(-f)dV is 4V_0/Q^2. This instantiates the Perelman identity with actual fields and measure. [9]

## 10. The differential kernel and what its parameters mean

At each stationary (M,R), retain

$$r_h=2GM/c^2,\ N=\sqrt{1-r_h/R},\ \sigma=\pi r_h^2/\ell_P^2,$$
$$\beta_R=N\beta_H,\ \mu_R=k_*/\beta_R,\ \mu_\infty=N\mu_R,$$
$$d\tau_R=Ndt,\ ds_{\mathrm{TT}}=-dt/(\hbar\beta_H),\ dJ=dt/\beta_H=d\tau_R/\beta_R,$$
$$x=4\pi r_hN/R,\ S_{\mathrm{surf}}/k_B=4\sum n h(nx),\ Q=Q_0+\alpha'\ell.$$

Across stationary experiments, prime denotes d/dlambda:

$$\sigma'/\sigma=2M'/M,\quad
N'/N=\frac1{2f}\left(\frac{r_hR'}{R^2}-\frac{r_hM'}{RM}\right),$$
$$\ell'=-M'/M-N'/N,\quad x'/x=M'/M+N'/N-R'/R,$$
$$S_{\mathrm{surf}}'=-4k_Bx'x\sum_{n\ge1}\frac{n^3e^{nx}}{(1+e^{nx})^2},$$
$$Q'=\alpha'\ell',\quad D_Q'=-\frac{\alpha'\ell'}{2Q}D_Q,\quad\mathcal F'=-\frac{2V_0\alpha'}{Q^2}\ell'.$$

Lambda is not silently identified with the proper time of a moving detector. The physical systems, scale calibration and approximation order remain attached to these equations.

## 11. A concrete nonstationary detector, rather than instantaneous substitution

Fix M and choose

$$R(t)=2r_h+(r_h/10)\tanh(t/\mathcal T),\quad\mathcal T=100r_h/c.$$

Then 1.9r_h<R<2.1r_h, |R_t|<=.001c and cf>.47c, proving timelikeness. The proper clock and null-coordinate functions are explicit:

$$\tau(t)=\int_0^t q(t')dt',\quad q=\sqrt{f-R_t^2/(c^2f)},$$
$$z_\pm(\tau)=\frac\kappa c[t(\tau)\pm r_*(R(t(\tau)))/c],\quad
z_\pm'=\frac\kappa{cq}(1\pm R_t/(cf)).$$

The conformal derivative-coupling kernel becomes

$$\mathcal A(\tau,\tau')=-\frac{A_\phi}{4}\sum_{\pm}
\frac{z_\pm'(\tau)z_\pm'(\tau')}{\sinh^2[(z_\pm(\tau)-z_\pm(\tau')-i0)/2]}.$$

This retains the entire trajectory. It approaches the respective static thermal kernels at early and late times.

For F=exp(z), write its Schwarzian as

$$\{F,\tau\}=F'''/F'-\frac32(F''/F')^2
=z'''/z'-\frac32(z''/z')^2-\frac12(z')^2.$$

Taylor expansion gives

$$\frac{F'(\tau+s/2)F'(\tau-s/2)}{[F(\tau+s/2)-F(\tau-s/2)]^2}
=\frac1{s^2}+\frac16\{F,\tau\}+O(s^2).$$

The numerator is F'^2+s^2(F'F'''-F''^2)/4+O(s^4); the denominator is s^2F'^2[1+s^2F'''/(12F')+O(s^4)]. Their quotient proves the coefficient. The expression is unchanged by F->-L/F, covering the outgoing Kruskal coordinate too. Thus

$$\mathcal A(\tau+s/2,\tau-s/2)
=-A_\phi\left[\frac2{(s-i0)^2}+\frac{\{e^{z_+},\tau\}+\{e^{z_-},\tau\}}6+O(s^2)\right].$$

For static z'=p_R the constant term is A_phi p_R^2/6, matching the exact csch kernel. For the moving trajectory this computes the higher-derivative correction to local correlations, not a full Planckian transition rate.

Choose chi(tau)=exp[-1/(1-(tau/tau_s)^2)] inside |tau|<tau_s=10r_h/c and zero outside. The leading transition probability is

$$\frac{g_d^2|m_{eg}|^2}{\hbar^2}\int d\tau d\tau'\,\chi(\tau)\chi(\tau')
e^{-iE(\tau-\tau')/\hbar}\mathcal A(\tau,\tau').$$

All data are specified. This distributional integral has not been numerically evaluated here. It is an explicit next calculation rather than an assumed instantaneous Hawking temperature for arbitrary motion.

## 12. Remaining physical interfaces

The exact four-dimensional scattering density still needs computation. Identifying field entropy with the gravitational area term needs a regulator and renormalized gravitational action, not a fitted distance. Identifying the O(3) target geometry with the physical shell through time needs actual coupled equations, not their equality at one calibration point. The untwisted round Dirac spectrum has eta=0; nonzero anomaly inflow needs specified chiral/gauge/bulk-boundary data. Those directions remain open rather than being silently removed or claimed complete.

The results above are concrete equilibrium, spectral, and probe calculations. They do not establish that these probes together constitute one self-consistent quantum-gravity solution. No novelty, Lean verification, or independent second review is claimed.

## Primary references

1. R. M. Wald, *The Thermodynamics of Black Holes*, https://arxiv.org/abs/gr-qc/9912119 .
2. K. Sanders, *On the construction of Hartle–Hawking–Israel states across a static bifurcate Killing horizon*, https://arxiv.org/abs/1310.5537 .
3. L. Hodgkinson, J. Louko, A. C. Ottewill, *Static detectors and circular-geodesic detectors on the Schwarzschild black hole*, https://arxiv.org/abs/1401.2667 .
4. E. Tjoa, R. B. Mann, *Unruh–DeWitt detector in dimensionally-reduced static spherically symmetric spacetimes*, https://arxiv.org/abs/2202.04084 .
5. A. Lewkowycz, J. Maldacena, *Generalized gravitational entropy*, https://arxiv.org/abs/1304.4926 .
6. R. Camporesi, A. Higuchi, *On the eigenfunctions of the Dirac operator on spheres and real hyperbolic spaces*, https://arxiv.org/abs/gr-qc/9505009 .
7. A. H. Chamseddine, A. Connes, W. D. van Suijlekom, *Entropy and the spectral action*, https://arxiv.org/abs/1809.02944 .
8. A. A. Tseytlin, *On sigma model RG flow, central charge action and Perelman's entropy*, https://arxiv.org/abs/hep-th/0612296 .
9. G. Perelman, *The entropy formula for the Ricci flow and its geometric applications*, https://arxiv.org/abs/math/0211159 .
