# A non-Eulerian RH counterexample attempt: the original shifted sheet, modular transport, and a certified heat-trace witness

## Result and scope

This calculation did **not** produce an RH counterexample that survived verification. It did construct a fixed rational signed witness for the actual arithmetic heat family, prove that it is negative at physical time -2, and prove that the same witness is positive at physical time 0. More strongly, the entire 32-dimensional Laurent test space used at time 0 is positive definite. All these signs include the complete root trace, rather than a selected quartet or an omitted complementary spectrum.

An adaptive transport calculation also proves an actual coefficient escape: a negative value can be preserved only with diverging coefficient norm when the 32-dimensional arithmetic form reaches a positive-semidefinite boundary at a physical time strictly between -3/2 and -5/4. This is a degeneracy of the complete test form, not an asserted collision of the zeros of H_t.

The modular calculations below give explicit receiving maps for two actual programme constructions: the non-Eulerian shifted quotient-size sheet and the original theta heat integral. The two deformation parameters, the modular parameter, and the distinguished arithmetic time-zero fibre are kept separate.

The numerical statements are computer-assisted interval results. The software uses directed `mpmath.iv` arithmetic with explicit analytic remainder bounds, bracketed quadrature nodes, exact integer factorials, and an exact rational witness. This is not a Lean verification or an independently audited interval library. The accompanying code and binary interval endpoints make the calculation reproducible and reviewable.

No Euler product, numerical zeta evaluator, or table of zeta zeros is used in this experiment. No historical-priority claim is made for the root-moment test or for a modular realization of a Fourier correlation.

## 1. Sources and what “non-Eulerian” denotes here

Repository: `KokunoYumeto/zeta-function-research-reader`.

Read-only source pin: `6c702bb8aa71c1129198b61f3d61d43265853320`.

Abbreviations below are source locators, not renamed mathematical objects.

- **SN:** `workbenches/splitzero-tandem/continuations/20260919-corpus-cohomology-metric-receivers/corpus_sources/split_zero_secondary_note.tex`. The shifted sheet and its generator are at 1110–1198. The non-Eulerianity theorem and Hurwitz specialization are in 1300–1550, specifically the labels `thm:non-eulerian-nonintegral-t`, `def:hurwitz-specialization`, and `prop:integer-shift-coefficient-surgery`. The exact Stone/two-sheet defect and the value -3 are at 1551–1830, labels `thm:F1-defect-and-boundary`, `thm:two-sheet-defect`, `thm:coprime-kernel`, and `cor:origin-values`. Git blob: `c6639419c5597faa68b6c5cab4a3b05f6b88ddb5`.
- **HH:** `workbenches/splitzero-tandem/continuations/20260923-cohomology-heat-residue/heat-endpoints/SUPPORTED_ZERO_HEAT_ENDPOINTS.tex`. Full support and inverse operations: 1–650; time-zero and coefficient-support closure: 650–930; zero receiver and exact escaping-coordinate map: 1000–1250; collision trace and complete theta moments: 1251–1510; distinct-root energy, collision obstruction, and marked time shifts: 1511–1800. Git blob: `ca32ec4017e077ea886aa6b37bcd1670275e8091`.
- **AP:** uploaded `split_zero_zeta_analytic_completion - Copy - Copy.tex`: actual leading coefficients 439–507, centered sign-pair product 557–608, packet polynomials 610–687, packet RH formulation 689–704, and packet logarithmic derivative 926–936.
- **IC:** uploaded `integrated_split_zero_zeta_consolidated - Copy - Copy.tex`, 1328–1587: the corresponding sign-pair product, retained quartic factors, and packet RH formulation.
- **LP:** uploaded `zeta_zero_atomic_phase_packets - Copy.tex`, 537–746: the complete local germ, its leading coefficient, tangent atoms, and packet symmetries.
- **MH:** uploaded `modular_hamiltonian_wick_spline_paper.tex`, 91–205: the original energy operator `H_a=a(-4 Delta_g+R)` and its expectation identity. That statement by itself does not identify this operator with the modular generator of a specified von Neumann algebra and faithful weight.
- **TB:** `workbenches/tau-base-cohomology/TAU_BASE_MODEL.md`, 265–322 at the previously read source pin `4ba9285b66af58a6d58fc502a494c1fb45ca5b79`: original full local algebras, reflected residue pairing, and Jacobian trace contraction.

The source's explicit non-Eulerian family is not a conjectured new Euler product. It is

\[
L_a(s)=\sum_{n\ge1}a_n(n+a)^{-s},\qquad D=sT,\quad (Tf)(s)=f(s+1),
\]

with the source identity `L_a=e^{-aD}L`. Here the symbol **a** denotes the parameter called **t** in SN; the parameter map is the identity `t_sheet=a`. The symbol **t** below remains the heat time used in HH and Rodgers–Tao. No map identifying these two times is imposed.

For the Riemann coefficients the source gives

\[
F_a(s)=\zeta(s,1+a),\qquad D_a(s)=\zeta(s)-F_a(s).
\tag{1.1}
\]

At the source endpoint a=1,

\[
F_1(s)=\zeta(s)-1,\qquad D_1(s)=1.
\tag{1.2}
\]

Thus an original zeta zero is a solution of `F_1(s)=-1`, not a zero of `F_1`. More generally it is a solution of `F_a(s)=-D_a(s)`. This distinction is an actual part of the original source reconstruction.

The coefficient defect at the doubled endpoint, also already in SN, is

\[
\mathfrak D_1(s,w)=-2\left(
\frac{\zeta(s)\zeta(w)}{\zeta(s+w)}-\zeta(s)-\zeta(w)+1
\right),\qquad \mathfrak D_1(0,0)=-3.
\tag{1.3}
\]

The value is an analytically continued coefficient-defect value. It is not identified in this calculation with the reflected trace defined in Section 5.

## 2. An exact modular receiver for the shifted sheet

Let

\[
\mathscr K_{\mathbb N}=\ell^2(\mathbb N),\qquad
\mathsf N e_n=ne_n,\qquad
\operatorname{Dom}\mathsf N=
\{x:\sum n^2|x_n|^2<\infty\}.
\]

For real a>-1 retain the positive operator

\[
\mathsf X_a=\mathsf N+aI,\qquad
\mathsf d_a=\mathsf X_a^{-2}.
\]

The positive trace-class operator `d_a` defines the faithful normal finite weight

\[
\varphi_a(A)=\operatorname{Tr}(\mathsf d_aA),\qquad
\varphi_a(I)=F_a(2).
\tag{2.1}
\]

Its mass is retained; it is not divided by `F_a(2)`. The modular automorphism group is

\[
\sigma_r^{(a)}:\mathcal B(\mathscr K_{\mathbb N})\longrightarrow
\mathcal B(\mathscr K_{\mathbb N}),\qquad
\sigma_r^{(a)}(A)=\mathsf X_a^{-2ir}A\mathsf X_a^{2ir},
\quad r\in\mathbb R.
\tag{2.2}
\]

This follows directly in the Hilbert–Schmidt representation: the modular operator multiplies the matrix unit `(i,j)` by `d_a(i)/d_a(j)`, so its imaginary powers induce the displayed conjugation. Equivalently this is the density-operator formula for modular automorphisms; see Witten, Section 4.2, equation (4.35).

Define the relative cocycle

\[
\mathsf u_a(r)=\mathsf d_a^{ir}\mathsf d_0^{-ir}
=\mathsf X_a^{-2ir}\mathsf N^{2ir}.
\tag{2.3}
\]

Since its diagonal entries are

\[
(1+a/n)^{-2ir},
\]

this is unitary for real r. Its continuation

\[
\mathsf u_a(z)=\operatorname{diag}_{n\ge1}
\exp[-2iz\log(1+a/n)],\qquad z\in\mathbb C,
\tag{2.4}
\]

is entire in operator norm: for a fixed a>-1, the real numbers `log(1+a/n)` are uniformly bounded. The same bound controls the power series and all derivatives locally uniformly in z. The cocycle law follows by multiplication; the density operators commute.

For Re(s)>1, the following is an identity of absolutely convergent operator traces:

\[
\boxed{
F_a(s)=\operatorname{Tr}\!
\left(\mathsf u_a(-is/2)\mathsf N^{-s}\right).
}
\tag{2.5}
\]

Indeed the nth diagonal entry of the traced operator is

\[
(1+a/n)^{-s}n^{-s}=(n+a)^{-s}.
\]

The source's exact complement has the same receiver:

\[
\boxed{
D_a(s)=\operatorname{Tr}\!
\left((I-\mathsf u_a(-is/2))\mathsf N^{-s}\right).
}
\tag{2.6}
\]

The sum of (2.5) and (2.6) is exactly `Tr(N^{-s})=zeta(s)`. The two sides then continue as the source's meromorphic functions. **No operator trace of `N^{-rho}` is asserted at a critical-strip point rho**; evaluation there is after this analytic continuation.

Differentiation in a on any compact subinterval of a>-1 is justified first in the absolutely convergent half-plane and gives

\[
\partial_aF_a(s)=-sF_a(s+1).
\tag{2.7}
\]

Thus (2.5) receives the source's actual shift generator, not a new freely chosen evolution.

### What the receiver says about forcing

The modular group (2.2) fixes every spectral function of `N`. Relative cocycle motion (2.3), evaluated at complex modular parameter, changes the spectral trace and gives precisely `F_a`. When the original complement (2.6) is also retained, the reconstructed function is the original zeta function at every a.

Consequently the two equations

\[
F_a(s)=0,\qquad F_a(s)+D_a(s)=0
\]

are different equations. The first can move its zeros. The second is identically the original equation `zeta(s)=0`. This is proved by the maps (2.5)–(2.6), not by an assertion that every non-Eulerian deformation is forbidden.

### Parameter holonomy does not silently return the original section

Continue a around a closed path based at 0 avoiding the points `-1,-2,...`. Let `w_n` be the winding number about `-n`; only finitely many are nonzero. The endpoint section is

\[
F_0^{\rm continued}(s)
=\zeta(s)+\sum_n n^{-s}
\left(e^{-2\pi i w_ns}-1\right).
\tag{2.8}
\]

For Re(s)>1, this follows termwise because the nth logarithm changes by `2 pi i w_n`; the tail is locally normally convergent and has no winding. Analytic continuation in s extends the identity. The correction is an explicit entire exponential polynomial.

The correction is identically zero only when every `w_n=0`. After deleting zero terms, its exponents are distinct complex numbers `-log n-2 pi i w_n` and `-log n`. Finite exponentials with distinct exponents are linearly independent: evaluation of their first derivatives through one less than their number gives an invertible Vandermonde system. Thus a nontrivial sheet holonomy does not by itself produce a new zero of the original endpoint function.

## 3. An exact modular realization of the arithmetic theta heat family

Keep the original HH/Rodgers–Tao convention

\[
H_t(Z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(Zu)\,du,
\tag{3.1}
\]

\[
\Phi(u)=\sum_{n\ge1}
(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})
\exp(-\pi n^2e^{4u}),
\tag{3.2}
\]

\[
H_0(Z)=\frac18\xi\left(\frac12+\frac{iZ}{2}\right),
\qquad
 g\left(\frac12+\frac{iZ}{2}\right)=16H_0(Z),\quad g=2\xi.
\tag{3.3}
\]

Each summand of Phi is positive for u>=0, since `2 pi n^2 e^{4u}-3>0`. The bound from HH,

\[
0<\Phi(u)\le C e^{9u}\exp[-\pi e^{4u}/2],
\tag{3.4}
\]

implies integrability after multiplication by any fixed polynomial times `exp(a u^2+b u)`. In particular the entire family and the following Hilbert-space vectors are well defined.

Set

\[
\mathscr K=\mathbb C e_*\oplus L^2((0,\infty),du),
\]

\[
\mathsf A=0\oplus M_u,
\quad
\operatorname{Dom}\mathsf A=
\mathbb C e_*\oplus\{f:uf\in L^2\},
\qquad
\mathsf d=e^{-\mathsf A}=1\oplus M_{e^{-u}}.
\tag{3.5}
\]

There is a faithful normal semifinite weight on `B(K)`:

\[
\varphi(X)=\operatorname{Tr}(\mathsf d^{1/2}X\mathsf d^{1/2}),
\qquad X\ge0.
\tag{3.6}
\]

It is not a trace-one state. Faithfulness follows from the dense range of `d^{1/2}`. Normality follows from normality of the trace. Semifiniteness follows by approximating X from below by the positive finite-rank operators `X^{1/2}P_nX^{1/2}`, for any increasing finite-rank projections `P_n` converging strongly to I. Each such operator has finite weight because d is bounded.

Its modular group is

\[
\sigma_r(X)=e^{-ir\mathsf A}Xe^{ir\mathsf A},\qquad r\in\mathbb R.
\tag{3.7}
\]

For a direct verification, identify Hilbert–Schmidt operators with kernels on the measure space `{*} disjoint-union (0,infinity)`, assigning u(*)=0. In this representation the modular operator is multiplication by `exp(-u+v)`. On a dense compact-spectral-support core the Tomita map is

\[
Sx(u,v)=e^{(u-v)/2}\overline{x(v,u)},
\]

and its polar decomposition is the transpose-conjugation followed by the square root of that modular multiplication operator. Its imaginary powers induce (3.7) on left multiplication. This also specifies the unbounded-operator domain through the explicit multiplication functions.

For the actual kernel define

\[
\psi_t(u)=e^{tu^2/2}\sqrt{\Phi(u)},\qquad
B_t=|\psi_t\rangle\langle e_*|.
\tag{3.8}
\]

The linear map `psi -> |psi><e_*|` maps the complete rapidly weighted domain

\[
\mathscr D=\bigcap_{b>0}\operatorname{Dom}(e^{bM_u^2})
\subset L^2(0,\infty)
\]

to a space of rank-one bounded operators. All `psi_t` belong to this domain. Every `B_t` is entire analytic for (3.7), since

\[
\sigma_Z(B_t)=|e^{-iZu}\psi_t\rangle\langle e_*|
\]

is entire in operator norm by (3.4).

The original theta function is exactly the following scalar correlation:

\[
\boxed{
H_t(Z)=\frac12\left[
\varphi(B_t^*\sigma_Z(B_t))+
\varphi(B_t^*\sigma_{-Z}(B_t))\right].
}
\tag{3.9}
\]

**Proof.** Each product inside the weight is a scalar multiple of `|e_*><e_*|`, whose weight is one. The scalars are respectively

\[
\int_0^\infty e^{tu^2}\Phi(u)e^{-iZu}\,du,
\qquad
\int_0^\infty e^{tu^2}\Phi(u)e^{iZu}\,du.
\]

Their arithmetic mean is (3.1). The norm of the marked operator is retained:

\[
\|B_t\|^2=\int_0^\infty e^{tu^2}\Phi(u)\,du=H_t(0).
\tag{3.10}
\]

No division by this number is performed.

### Heat is an analytic modular operation, not real modular time

On the stated rank-one analytic domain define the linear bijection

\[
\mathcal I_h(B_\psi)=B_{e^{hu^2/2}\psi},\qquad h\in\mathbb R.
\tag{3.11}
\]

It has inverse `I_{-h}` and `I_h(B_t)=B_{t+h}`. Its exact Gaussian receivers are

\[
\mathcal I_h(B)=\frac1{\sqrt{2\pi h}}
\int_{\mathbb R}e^{-r^2/(2h)}\sigma_{ir}(B)\,dr,
\qquad h>0,
\tag{3.12}
\]

\[
\mathcal I_h(B)=\frac1{\sqrt{2\pi(-h)}}
\int_{\mathbb R}e^{-r^2/(2(-h))}\sigma_r(B)\,dr,
\qquad h<0.
\tag{3.13}
\]

Gaussian integration proves these equalities at each u. They also hold as operator-norm Bochner integrals. For (3.12), use
`r u <= b u^2+r^2/(4b)` with b>h/2 and the domain of psi to obtain an integrable Gaussian majorant. For (3.13), the real modular orbit has constant operator norm.

Substitution into (3.9) recovers exactly

\[
\partial_tH_t=-\partial_Z^2H_t.
\tag{3.14}
\]

For real r, replacing `B_t` by `sigma_r(B_t)` leaves (3.9) unchanged, because the phase `exp(-iru)` cancels between the two marked vectors. Thus real modular motion does not implement the heat change. Analytic modular averaging does implement it and changes the marked amplitude by exactly (3.11).

The selfadjoint frequency operator A in (3.5) is **not** asserted to have the zeros of H_t as its eigenvalues. The receiving map (3.9) is a scalar correlation, not a spectral intertwiner. This distinction is tested below: the same modular system realizes a negative full-root trace at t=-2.

### Support is retained at every displayed scalar evaluation

For a nontrivial distributive lattice L, lift a complex scalar v to `(v,1_L)` and retain each lower zero label `(0,lambda)`. For a map of sets F:V->W between defined amplitude objects, the labelled map sends (lambda,v) to (lambda,F(v)) in the same declared fibre and sends external absence to external absence. For a linear F this is the ordinary supported linear reconstruction. For the quadratic correlation in (3.9), it is only a labelled set map; no additivity or semiring-morphism property is asserted. An actually vanishing correlation has image `e=(0,1_L)`, not `tau=(0,0_L)`. Its complex amplitude is nevertheless exactly zero under p. No localization at e occurs anywhere in (3.1)–(3.14). The support labels therefore neither remove a trace term nor alter the amplitude tested below.

## 4. A full-root test, with the original residue constants retained

For real t define

\[
g_t(s)=16H_t(-2i(s-1/2)),\qquad g_0=g.
\tag{4.1}
\]

Every H_t is real entire, even, and has H_t(0)>0. Its order is at most one. To verify the last claim directly from (3.4), bound `|H_t(Z)|` by the integral of

\[
C\exp(|t|u^2+(|Z|+9)u-\pi e^{4u}/2).
\]

Absorb `|t|u^2+9u` into `pi e^{4u}/8+C_t`. Maximizing `R u-(pi/8)e^{4u}` gives `O(R log(R+2))`. The remaining superexponential factor is integrable. Thus the maximum modulus is bounded by `exp(O_t(R log(R+2)))`, which proves order at most one.

Hadamard factorization, paired using evenness as in AP, gives

\[
\frac{H_t'(Z)}{H_t(Z)}
=-\sum_{n\ge1}S_n(t)Z^{2n-1},\qquad
S_n(t)=\sum_{\zeta:H_t(\zeta)=0}
\frac{m_\zeta}{\zeta^{2n}},
\tag{4.2}
\]

near Z=0. Here the sum includes **both members of every sign pair**, with complete multiplicity. In particular `sum m_zeta/|zeta|^2` is finite. The possible affine exponential factor is constant because H_t is even and nonzero at zero. These facts also apply if a zero is multiple.

For a finite conjugation-stable zero set `Zset`, define

\[
A_{t,Zset}=\bigoplus_{\zeta\in Zset}\mathcal O_\zeta/(H_t),
\]

with its full local multiplicities. The map

\[
\mathcal E_{d,t,Zset}:\mathbb C^d\longrightarrow A_{t,Zset},
\qquad
c\longmapsto\left[\sum_{i=0}^{d-1}c_iZ^{-2i-1}\right]
\tag{4.3}
\]

is defined on every full local algebra because zero is not a root of H_t. These are ordinary inverses of holomorphic units at the roots, not a generalized inverse at supported zero.

In the original s-coordinate, the anti-linear reflected involution is

\[
f^\dagger(s)=\overline{f(1-\bar s)}.
\]

Under the actual analytic coordinate morphism

\[
\alpha:\mathbb C_Z\longrightarrow\mathbb C_s,
\quad\alpha(Z)=\tfrac12+\tfrac{iZ}{2},
\quad\alpha^{-1}(s)=-2i(s-\tfrac12),
\tag{4.4}
\]

it becomes `F^dagger(Z)=overline{F(bar Z)}`. For `F=alpha^*f` and `G=alpha^*h`, the original raw residue and Jacobian maps transform as

\[
\operatorname{Res}_s\frac{f^\dagger h}{g_t}\,ds
=\frac{i}{32}\operatorname{Res}_Z
\frac{F^\dagger G}{H_t}\,dZ,
\qquad
\alpha^*g_t'=-32iH_t'.
\tag{4.5}
\]

The two displayed constants multiply to one in the Jacobian trace contraction. Consequently that contraction is exactly

\[
\mathcal T_{t,Zset}(F,G)
=\sum_{\zeta\in Zset}m_\zeta
\overline{F(\bar\zeta)}G(\zeta).
\tag{4.6}
\]

Locally this follows without discarding a unit: if `H_t(Z)=u(Z)(Z-zeta)^m`, then
`H_t'/H_t=m/(Z-zeta)+u'/u`. The second term is holomorphic and contributes zero residue. All m jet orders remain in (4.3), while the stated Jacobian contraction has its original nilpotent radical.

For the rational functions in (4.3), the infinite sum in (4.6) is absolutely convergent: the product decays as O(|zeta|^{-2}). Thus it defines the complete trace form on these images, with no selected-packet remainder left out.

Define its coefficient matrix by

\[
\boxed{
\mathsf K_d(t)=(S_{i+j+1}(t))_{0\le i,j<d}.
}
\tag{4.7}
\]

Then

\[
\boxed{
\mathcal T_t(\mathcal E_{d,t}c,\mathcal E_{d,t}c)
=c^*\mathsf K_d(t)c.
}
\tag{4.8}
\]

At t=0, RH would make each root Z real, and each summand in (4.6) would be `m_zeta |F(zeta)|^2`. Therefore **one negative value in (4.8) at t=0 is an actual RH contradiction**, without using an Euler product. Only this implication is needed for the experiment; it is not being offered as a new general RH criterion.

## 5. Calculate the complete trace from the actual theta coefficients

Define, with the original measure and no division of H_t,

\[
M_n(t)=\int_0^\infty u^{2n}e^{tu^2}\Phi(u)\,du,
\qquad
 a_n(t)=\frac{(-1)^nM_n(t)}{(2n)!}.
\tag{5.1}
\]

Then `H_t(Z)=sum a_n(t) Z^{2n}`. Multiplying (4.2) by H_t and comparing coefficients gives the exact recurrence

\[
\boxed{
M_0(t)S_n(t)
=-2n a_n(t)-\sum_{j=1}^{n-1}a_j(t)S_{n-j}(t).
}
\tag{5.2}
\]

This calculates every entry in (4.7) from real integrals. Its factor M_0 is the original H_t(0), explicitly retained in the equation.

For numerical conditioning only, use the invertible coefficient map

\[
\mathsf D_d=\operatorname{diag}(1000^i)_{0\le i<d},
\qquad
\widehat{\mathsf K}_d=\mathsf D_d\mathsf K_d\mathsf D_d.
\tag{5.3}
\]

A vector v in the conditioning coordinates means the actual rational function with coefficients `c=D_d v`. No source metric, root coordinate, multiplicity, or scalar H_t is rescaled.

## 6. The candidate that was actually tested

The file `rational_witness.json` gives 19 exact integer numerators `n_i` and the common denominator `10^120`. Define

\[
\boxed{
 f_*(Z)=\sum_{i=0}^{18}
 \frac{1000^i n_i}{10^{120}}Z^{-2i-1},
 \qquad Q_*(t)=\mathcal T_t(f_*,f_*).
}
\tag{6.1}
\]

The integers are also printed in Appendix A. They are fixed for every time in the experiment. In particular `n_18=10^120` and the coefficient of `Z^{-37}` in the original function is `10^54`.

The candidate was selected by the LDL transpose factorization of the conditioning matrix at t=-2: the inverse-transpose of its unit triangular factor, applied to coordinate 19, isolates a negative pivot. The result was rounded to the displayed rational vector and then verified independently by interval evaluation. The selection is not used as a substitute for the final rational sign check.

The enclosing intervals, with rational endpoints, are

| Physical time | Certified enclosure for the same Q_*(t) |
|---|---|
| -2 | `[-2.385,-2.383] * 10^(-46)` |
| -2 + 10^(-21) | `[-2.314,-2.311] * 10^(-46)` |
| -2 + 10^(-20) | `[4.762,4.764] * 10^(-46)` |
| 0 | `[0.00081442298606666852,0.00081442298606666854]` |

Thus the same negative vector has already changed sign between the two explicitly stated nearby times. This is a zero of the **test value Q_***. It is not identified with a root collision of H_t or with the de Bruijn–Newman threshold. Other vectors can remain negative after Q_* becomes positive.

The derivative values are also interval-evaluated from the exact trace equations:

\[
Q_*'(-2)\in[1.0766,1.0767]10^{-44},
\]

\[
Q_*''(-2)\in[0.00001429418,0.00001429420].
\tag{6.2}
\]

These quantify why extrapolating the small first derivative would be misleading. No Taylor extrapolation is used to certify the four values in the table: each has its own integral evaluation.

### The whole 32-dimensional family at zero is excluded

The interval LDL factorization of the complete matrix `Khat_32(0)` has 32 strictly positive pivots. Therefore

\[
\boxed{\mathsf K_{32}(0)>0.}
\tag{6.3}
\]

This excludes every nonzero complex vector in `span{Z^{-1},Z^{-3},...,Z^{-63}}`, not just f_*.

The last conditioning-coordinate pivot is enclosed by

\[
[2.15549,2.15551]\,10^{-90}.
\tag{6.4}
\]

This is a pivot, **not** a lower bound for the smallest eigenvalue in the original coefficient norm. Precisely, if `Khat=L P L^T` is the exact unit-triangular factorization, the invertible map

\[
\mathsf T_0=L(0)^T\mathsf D_{32}^{-1}
\]

satisfies

\[
c^*\mathsf K_{32}(0)c
=(\mathsf T_0c)^*P(0)(\mathsf T_0c).
\tag{6.5}
\]

At t=-2, the same 32-dimensional calculation has exactly two negative pivots, at positions 19 and 25, and no zero pivot. Its inertia is `(30,2,0)`. Thus the method is a signed complete trace computation; positivity is not built in as it would be for the direct moment Gram `integral |p(u)|^2 Phi(u) du`.

Negative-time nonreal zeros themselves are already known from Rodgers–Tao and Dobner. The new output of this experiment is the fixed rational witness, the certified sign-loss calculation, and the finite-space exclusion at the actual time-zero source. No rediscovery of the qualitative negative-time theorem is claimed.

## 7. Exact heat production of the signed trace

Write `R_t(Z)=H_t'(Z)/H_t(Z)` near zero. Since H_t(0)>0 and `partial_t H=-H''`,

\[
\partial_t\log H_t=-(\partial_ZR_t+R_t^2).
\]

Insert (4.2) and compare coefficients of `Z^{2n}`. The result is

\[
\boxed{
S_n'(t)=2n\left[
\sum_{a=1}^{n}S_a(t)S_{n+1-a}(t)
-(2n+1)S_{n+1}(t)\right],\qquad n\ge1.
}
\tag{7.1}
\]

This equation is derived in the coefficient algebra where H_t(0) is a unit. It remains valid through collisions of other roots. It does not divide by a colliding gap or discard a nilpotent fibre.

For a fixed coefficient vector c the complete production term is

\[
\boxed{
\frac{d}{dt}\,c^*\mathsf K_d(t)c
=\sum_{i,j=0}^{d-1}\bar c_i c_j\,2(i+j+1)
\left[
\sum_{a=1}^{i+j+1}S_aS_{i+j+2-a}
-(2i+2j+3)S_{i+j+2}\right].
}
\tag{7.2}
\]

In particular

\[
S_1'(t)=\frac{M_2(t)M_0(t)-M_1(t)^2}{M_0(t)^2}>0.
\tag{7.3}
\]

The numerator is strictly positive by Cauchy–Schwarz, since u^2 is not constant on the strictly positive theta measure. Thus even the first inverse-root trace varies under physical heat. It is not an isospectral conjugation invariant.

The finite-rank modular formula for a faithful density d,
`A -> d^{ir} A d^{-ir}`, preserves ordinary traces of powers of conjugated operators. A continuous such automorphism that normalizes a fixed finite reduced packet algebra also fixes each of its primitive idempotents: it acts through a finite permutation group, while the parameter line is connected. This proves a restriction on that specific proposed transport. It does not rule out all infinite-dimensional relative-modular or non-isospectral constructions.

The actual non-isospectral effect in the representation of Section 3 is already specified by `B_t -> I_h(B_t)`, and the full trace production is (7.2). The sign check in Section 6 shows that this production cannot be omitted when transporting the selected negative vector.

### 7.1 Adaptive negative transport reaches an arithmetic form boundary before time zero

The same interval computation gives the endpoint inertias

\[
\operatorname{In}\mathsf K_{32}(-3/2)=(31,1,0),\qquad
\operatorname{In}\mathsf K_{32}(-5/4)=(32,0,0).
\tag{7.4}
\]

The parameter is the original heat time. Define the actual number

\[
t_*:=\inf\{t\in[-3/2,-5/4]:\mathsf K_{32}(t)\succeq0\}.
\tag{7.5}
\]

Continuity of the matrix entries and the strict endpoint certificates imply

\[
-3/2<t_*<-5/4,\qquad
\mathsf K_{32}(t_*)\succeq0,\qquad
\det\mathsf K_{32}(t_*)=0.
\tag{7.6}
\]

For t<t_* in that interval the matrix has a negative direction. If the matrix at t_* were positive definite, openness of positive definiteness would contradict the infimum definition; this proves the determinant assertion. The strict upper inequality follows from positivity in a left neighborhood of -5/4.

Let I be an open nonsingular interval just below t_*. Such an interval exists: det K is real analytic and not identically zero, so its zeros cannot accumulate at t_*. On I define the linear connection

\[
\mathcal A(t):\mathbb R^{32}\longrightarrow\mathbb R^{32},\qquad
\mathcal A(t)=-\frac12\mathsf K_{32}(t)^{-1}\mathsf K_{32}'(t).
\tag{7.7}
\]

For any a in I, the fundamental matrix is the unique solution

\[
\mathsf U'(t,a)=\mathcal A(t)\mathsf U(t,a),\qquad
\mathsf U(a,a)=I.
\tag{7.8}
\]

It exists and is invertible on I by the finite-dimensional linear differential equation. Direct differentiation proves

\[
\boxed{
\mathsf U(t,a)^T\mathsf K_{32}(t)\mathsf U(t,a)
=\mathsf K_{32}(a).
}
\tag{7.9}
\]

There is no assertion that this connection is a unitary modular automorphism. It is the explicitly given connection preserving the signed form along a non-isospectral physical heat change.

Choose a negative vector c_a and retain its actual amplitude

\[
\eta=-c_a^T\mathsf K_{32}(a)c_a>0,
\qquad c(t)=\mathsf U(t,a)c_a.
\]

Then `c(t)^T K(t)c(t)=-eta` exactly. The following uniform derivative bound is computed in the **original coefficient basis**, not the conditioning coordinates:

\[
\boxed{
\sup_{-3/2\le t\le-5/4}\|\mathsf K_{32}'(t)\|_2<\frac4{125}.
}
\tag{7.10}
\]

Here is its full certificate. Set

\[
m_*=M_0(-3/2),\qquad B_n=\frac{M_n(-5/4)}{(2n)!},
\]

and define positive majorants

\[
E_n=\frac{2nB_n+\sum_{j=1}^{n-1}B_jE_{n-j}}{m_*},
\quad n=1,\ldots,64.
\]

The positivity of Phi makes each M_n increasing in t. Recurrence (5.2) therefore proves `|S_n(t)|<=E_n` throughout the interval. Equation (7.1) bounds its derivative by

\[
F_n=2n\left[\sum_{a=1}^nE_aE_{n+1-a}+(2n+1)E_{n+1}\right].
\]

A matrix norm bound by the maximal absolute row sum gives

\[
\|\mathsf K_{32}'(t)\|_2\le32\max_{1\le n\le63}F_n.
\]

Using lower and upper interval endpoints for m_* and the B_n, respectively, the checker encloses this last quantity above by

\[
0.031792245049<4/125.
\]

Every quantity in this calculation is an original theta moment. The last decimal is a rational outward upper bound, not an approximation substituted into the theorem.

Since the form at t_* is positive semidefinite,

\[
\begin{aligned}
\eta
&\le c(t)^T[\mathsf K_{32}(t_*)-\mathsf K_{32}(t)]c(t)\\
&\le\frac4{125}(t_*-t)\|c(t)\|_2^2.
\end{aligned}
\]

Consequently,

\[
\boxed{
\|c(t)\|_2\ge
\sqrt{\frac{125\eta}{4(t_*-t)}}
\longrightarrow\infty\quad(t\uparrow t_*).
}
\tag{7.11}
\]

This is an escape in the coefficient space of the actual trace receiver (4.3), with no replacement of its source moments. It is stronger than observing that one fixed vector changed sign. It also locates why this particular finite-dimensional route fails: its sign-preserving coefficient transport cannot remain finite all the way to arithmetic time zero.

The boundary in (7.6) is a **test-form degeneracy**. The calculations do not identify it with a double zero of H_t, the nilpotent collision algebra in HH, or the de Bruijn–Newman constant. Indeed the earlier short-time certificates already show that a fixed test can turn positive while the full form still has negative directions. The distinctions are preserved rather than converted into an RH conclusion.

## 8. Complete quadrature and interval certificate

The successful computation uses 360 decimal digits of interval working precision, 160-point Gauss–Legendre quadrature on each of 24 equal panels of [0,3], the first 16 theta summands, and moments through order 65. The included remainders cover all omitted theta summands, the spatial tail, and the Gaussian quadrature error.

### 8.1 Validated nodes and weights

Ordinary high-precision Newton iterations supply only initial node estimates. Around each estimate the checker constructs a rational-decimal interval of radius approximately `10^(-280)`, evaluates the degree-160 Legendre polynomial by outward interval recurrence at its two endpoints, and proves opposite signs. All 160 brackets are verified disjoint and inside (-1,1). Because the polynomial has degree 160, this brackets all its roots without missing or double-counting one.

On each bracket the exact derivative identity

\[
P_n'(x)=n\frac{xP_n(x)-P_{n-1}(x)}{x^2-1}
\]

and the weight formula

\[
w(x)=\frac{2}{(1-x^2)P_n'(x)^2}
\]

give an interval containing the exact positive quadrature weight. The finite sums and transformations of nodes to the physical panels are all interval operations.

### 8.2 An explicit analytic quadrature bound

For a panel of width ell=1/8, half-width h=1/16 and centre c, use the Bernstein ellipse with parameter 4. Its real and imaginary semiaxes are

\[
A=17h/8=17/128,\qquad B=15h/8=15/128.
\]

Set `x_-=c-A`, `x_+=c+A`, `R^2=x_+^2+B^2`, and

\[
\kappa=1-(4B)^2/2>0.
\]

On the ellipse, `cos(4 Im z)>=kappa`. The first sixteen theta terms therefore have the absolute majorant

\[
\mathcal P_c=
\left(32e^{9x_+}\sum_{j=1}^{16}j^4
+12e^{5x_+}\sum_{j=1}^{16}j^2\right)
\exp[-3e^{4x_-}\kappa].
\tag{8.1}
\]

This uses only `3<pi<4`, bounds the absolute polynomial prefactor by its two positive terms, and retains a lower bound for the real part of `pi j^2 exp(4z)`.

For time t, the additional heat majorant is

\[
T_c(t)=
\begin{cases}
e^{t x_+^2},&t\ge0,\\
e^{|t|B^2},&t<0.
\end{cases}
\]

For moment m, the complete analytic supremum bound is `P_c T_c R^{2m}`.

If an analytic function is bounded by M on an ellipse of parameter rho, its Chebyshev coefficients beyond degree k are bounded by `2M rho^{-j}`. This follows by pulling back through `(w+w^{-1})/2` and applying the Cauchy coefficient bound to the resulting Laurent series. Truncation at degree `2n-1` gives uniform error at most

\[
\frac{2M\rho^{-(2n-1)}}{\rho-1}.
\]

The quadrature is exact on that polynomial. Its positive weights sum to the interval length, so bounding both the integral and quadrature of the remainder proves the panel error bound

\[
\boxed{
\frac{4\ell}{3}\,\mathcal P_cT_c(t)R^{2m}
\,4^{-(2n-1)}.
}
\tag{8.2}
\]

The checker adds (8.2) over all panels.

### 8.3 Omitted theta summands

On [0,3], for j>=17 the positive tail is bounded by its leading positive term:

\[
\Phi_{>16}(u)
\le32e^{27}\sum_{j\ge17}j^4e^{-3j^2}.
\]

The ratio of consecutive summands is at most `16 exp(-105)<1/2`. Thus, for every m,

\[
\boxed{
\int_0^3 u^{2m}e^{tu^2}\Phi_{>16}(u)\,du
\le192\cdot17^4\cdot3^{2m}
 e^{27+9\max(t,0)-867}.
}
\tag{8.3}
\]

### 8.4 Spatial tail

For u>=3,

\[
\Phi(u)\le64e^{9u}e^{-3e^{4u}}.
\]

For `0<=m<=65` and `t<=1/5`,

\[
2m\log u+\max(t,0)u^2+9u\le47u^2\le e^{4u}.
\]

Here `log u<=u`, `139u+(1/5)u^2<47u^2` for u>=3, and `e^{4u}/u^2` is increasing there with `e^{12}>1000>423`. Also
`e^{4u}>=1000(1+4(u-3))`. Consequently

\[
\boxed{
\int_3^\infty u^{2m}e^{tu^2}\Phi(u)\,du
<e^{-2000}.
}
\tag{8.4}
\]

### 8.5 Propagation of the errors

Every moment is enclosed by the quadrature interval enlarged by the sum of (8.2)–(8.4). The checker proves that the denominator interval for M_0 is positive. It applies (5.2) using exact integer factorials, then the stated congruence (5.3), and then ordinary interval LDL elimination. A pivot containing zero stops the certificate rather than assigning a sign. Every successful pivot in the supplied main certificate excludes zero.

Induction on the elimination equations proves that the intervals contain the exact factors of the exact matrix. Hence the pivot-sign certificate proves (6.3), and evaluation of the fixed rational vector with the same trace intervals proves the four scalar enclosures in Section 6.

The earlier 128-node exploratory certificate could not determine its last pivot. That inconclusive run was not counted as a positive sign; the successful report is the 160-node run.

## 9. What failed and what is still untested

The attempted adaptive transport also has the rigorously located boundary and the coefficient blow-up (7.11). Its occurrence strictly before time zero is a concrete failure of this finite-dimensional continuation, not a reason to assert that all higher-dimensional continuation mechanisms fail.

The attempt was to realize a negative arithmetic heat-trace direction inside a genuine modular construction, then retain negativity at the marked original time-zero source. The realization and the negative direction are explicit. The sign does not survive for the displayed rational vector; the entire original 32-dimensional Laurent space at time zero is excluded by the independent interval calculation.

The shifted non-Eulerian sheet also has an exact modular receiver, but the receiver retains the source complement D_a. Changing a or taking sheet holonomy does not give a new zero of the reconstructed original function unless that complement and the returned section are controlled as displayed.

A 64-dimensional high-precision exploration was also attempted, followed by interval validation. The interval runs did not finish within their execution limit; they produced no additional certificate. No higher-rank sign is claimed.

No conclusion is drawn that every larger or differently localized root-trace test is positive. No conclusion is drawn that arbitrary modular or arithmetic evolutions are useless. What remains untested is, in particular, a higher-rank or differently located **actual time-zero** negative witness, together with a justified domain and the complete root trace. This document supplies no such surviving witness.

The prescribed -3 values, the root-coordinate escape, and nilpotent holonomy are retained in their source categories. They are not substituted for Q_*(0).

## 10. External literature: what was checked and what was used

1. Brad Rodgers and Terence Tao, *The de Bruijn–Newman constant is non-negative*, arXiv:1801.05914v5; Forum of Mathematics, Pi 8 (2020), e6. The original theta and heat conventions were checked. Their nonnegative-threshold theorem is used only to identify the established qualitative background, not to supply the numerical signs above.
2. Alexander Dobner, *A proof of Newman's conjecture for the extended Selberg class*, arXiv:2005.05142v2, Acta Arithmetica 201 (2021), 29–62. The introduction, extended-class definition, and the negative-time approximation mechanism were read. They explain why qualitative negative-time zeros are not a new discovery and why Euler products are unnecessary for that background result. Dobner's kernel convention differs by a factor four from Phi in (3.2); it has not been substituted into this computation.
3. Edward Witten, *Notes on Some Entanglement Properties of Quantum Field Theory*, arXiv:1803.04993v6, Sections 4.1–4.2, particularly equations (4.26), (4.32), and (4.35), pp.35–38. The density-operator modular formula and the distinction between real and complex modular parameters were checked. The weight and correlation maps used here are constructed explicitly in Sections 2–3.
4. Alain Connes, *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*, arXiv:math/9811068, Selecta Mathematica 5 (1999), 29–106. The spectral/trace distinction in the source account was checked; no unprovided spectral equivalence with the present frequency operator is assumed.
5. Alain Connes and Caterina Consani, *Knots, primes and class field theory*, arXiv:2501.06560. The finite-cover/prime-monodromy scope was checked. No prime-orbit representation is silently identified with the heat-root algebra in Section 4.
6. Connes–Consani, *The Absolute Twistor Line and the Geometry of compactified Spec Z*, arXiv:2609.00299: the supplied abstract and indexed abstract were located, but a usable primary full text was not obtained in this pass. No theorem from its full proof is invoked here.
7. The Kaczorowski–Perelli degree-one and small-degree classification references and Soundararajan's degree-one proof were located. They were **not** used to forbid the original non-Eulerian sheet. A classification inside the Selberg class is not a classification of arbitrary analytic deformations.
8. Tao's July 21, 2026 author exposition, *A digestion of the Jacobian conjecture counterexample*, was checked against the polynomial and inverse-root chart reproduced in HH. The exact polynomial calculation is distinct from any assertion about an unforced Navier–Stokes counterexample. No such assertion is a premise of this document.

The elementary complex-analysis inputs in the proofs are the identity theorem, differentiation under an integrable compact-uniform majorant, Cauchy coefficient bounds, and Hadamard factorization for order-at-most-one entire functions. The sign-pair use of the last theorem is exactly the source argument in AP:557–608. Hilbert-space functional calculus is used for the explicitly defined multiplication operators; their modular operators are written directly above.

## Appendix A. Exact rational coefficients of the tested witness

In the following list the ith entry is n_i in (6.1), indexed from 0. Every denominator is exactly 10^120. The numbers printed here, not the approximations in any exploration log, define the witness.

```text
 0: 179107331574670548663441273826884481552363412191645386333868436358806383663995257261876001659600223
 1: -740666272194237419544790664679964289683897172528951662294090593279395558592947574637192585593798413559
 2: 437105600753818209102119477320582664530112343206993801906230332495729563382192447365071755783752880372166
 3: -97670779766376143506382641087800752689734403741470926888024974554136938993181261257024692754758925533302286
 4: 11152554810178511059252424856438165460667573741332772245578923616722616254177960091384078376580312143858127140
 5: -753568491436554718684702100869273342643861607060954465384375877939971640489596091105781622078521573646480206941
 6: 32802091265057071423714394079141907890600856289318324604486988917439878168560687675589050798002355931510183552755
 7: -970213958280763118055697347115193233148284021549009019566083701976892748628380220498202739969631392803978245164893
 8: 20183897162876882249033985985998595913143975886416950289718156042172411442774703011206542607969152985124151481142518
 9: -301875143044100961229379124449745454631351042467791978583396435748999676991602980058032073700929717712020947597372911
10: 3286654790429397024394552111405709233733322975969398057609891229204477359225808556070687502290056605667806351005815592
11: -26167110721092706062720085942460511361047665346714832502272419222623935513979969564520084334135974820744508327824728064
12: 151875674248307637441454345355945078799005468932918433000230006227173314551491513243943710623528551682770040403115095941
13: -635241508297824964080712626712713610506344983233198545623599851741272453033223009346325596854835421570530007736392521069
14: 1872451007214952289282330819298741340957208198824597255236053996633424211366311028060367951901312271069981109150450555777
15: -3743654799196479889712317981921050334454525085554260349407121476179747911414918939920084217136306538527747131857812724460
16: 4753956681819026931399776876119938125333798889171840019489867658496682044466971258883345745082465466951196163997515656131
17: -3386856822663075082198944923896145645222255631276662259082253721896998324204542110924259809173869333954971119273505652602
18: 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
```

## Appendix B. Reproduction

Run `python reproduce.py` in the extracted bundle, without Python’s `-O` flag: the interval guards must remain enabled. The main certified calculations require only Python and mpmath; they make no network request. The precision, physical times, exact binary interval endpoints, analytic bounds, and pivot signs are written to JSON. The rational witness is fixed before its certificate is evaluated. `theta_search.py` and `witness.py` are explicitly exploratory/selection tools, not the source of a sign certificate.
