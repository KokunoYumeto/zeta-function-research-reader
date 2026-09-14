# Independent complete review of the complex gamma fibre transport

Date: 13 September 2026. Reviewer lane: `gamma_phase_transport_review`.

## Scope, source pins, and disposition

I read the complete new proof `work/gamma_phase_fibre_transport_20260913.tex`, initially GP.1–GP.25 and then the expanded GP.1–GP.27 version. The expanded version read during the review had SHA256 `0148db49930b71cb1c986aa7ac7425e8b331f70d526c7885adeb23df98115e92`. The root author is correcting the prose type errors identified below; the final exact source pin and correction verification are recorded at the end of this review.

I also read the complete delivered `sources/web_gamma_convolution_delivery/Tau_Gamma_Convolution_Descent/RESEARCH_NOTE.md`, SHA256 `886c82e2562d9b4846adb44640d28a34552e38eb2518a3cd47f90dbbedd95e5b`; the complete retained `tex/theta_gamma_reference.tex`, SHA256 `a379a1e19de4ce885680e14bda466a37b4c1eb25228c19b931d573f58be167f9`; and TVB's source construction, Mellin domains, exact quotient sequence, and signed primitive through TVB.9 in `work/toda_cv_exact_bridge_20260912.tex`, SHA256 `97652a43445708c0e6d2a959f45aed8a4f2a7f73f9cd4b6cd57e67b8fedb408e`. No full re-review of TVB.10–TVB.44 is claimed here. The DLMF generating-function locator was opened directly and agrees with the stated specialization [DLMF 18.23.7](https://dlmf.nist.gov/18.23.E7).

The displayed transport, fibre projection, strict variance, complex coefficient, source Gram, quotient section, determinant, and signed primitive formulas are mathematically correct. I found three precise prose typing errors in the changing draft, and then one incorrect intermediate moment list in the added calibration. None requires changing those displayed formulas:

1. After GP.18, the draft described a source Gram as a map `E → Herm(E)`. A fixed Gram is an element of `Herm(E)` and induces a linear map `E → E^vee` to the conjugate dual. The operation taking an observation map to its Gram has type `Hom_C(E,H) → Herm(E)`. The author corrected this and displayed the common tilt in all three observation maps.
2. After GP.24, the draft composed “inverse addition” with inverse Mellin while declaring the graph as domain. The graph-to-source arrow is addition; its inverse has the opposite domain. The intervening multiplication by the original gamma factors must also occur. The exact corrected composition is given below.
3. Near the support conclusion, the draft grouped norm and trace with “quadratic types.” Norm itself is not a quadratic map, and trace is linear. Squared norm and the Gram operation are quadratic over the underlying real vector spaces. The precise types are supplied below.
4. In the later GP.29 calibration derivation, the stated reference moments of orders zero, two, four, and six were `1/4,1,10,184`. The correct moments of the displayed original Laplace function `(1/4)sec(theta)^4` are `1/4,1,14,376`. The displayed GP.29 matrices, determinants, and companion checker already used the correct values. I sent the exact correction and independently differentiated the Laplace function; the order-eight moment is `16064`.

The expanded standalone TeX also introduced `\mathscr` without initially adding `mathrsfs`; this is a compilation dependency, not a mathematical defect. I sent each finding to the author immediately. This review writes no changes into the root proof or the cumulative release directory. No Lean execution is used or claimed.

## 1. Original measure and pointwise fibre definitions: GP.1–GP.5

Write `r(t)=r_lambda(t)`, `r_k(u)=r_lambda^{*k}(u)` and `c=c_lambda`. Gamma has no zeros or poles on `lambda+it/2` for real `t` and `lambda>0`; therefore `r` is strictly positive. TG.7–TG.8 proves

\[
\int_{\mathbb R}e^{iyt}r(t)\,dt
=2^{1-2\lambda}\Gamma(2\lambda)\cosh(y)^{-2\lambda}.
\]

Taking the kth power and using Fourier uniqueness yields

\[
r_k(u)=\frac{c^k}{c_{k\lambda}}r_{k\lambda}(u),\qquad
\int r_k=c^k.
\]

In particular, no factor `k`, `sqrt(k)`, or probability-mass divisor belongs in the original sum measure. The real coordinate is literally `u=t_1+...+t_k`, and the arithmetic polynomial is evaluated at `S=k/2+iu`. The contour argument in TG justifies every fixed exponential moment on `|theta|<pi/2`; raising the transform to the kth power gives GP.2 with the original mass `c^k`.

The complete-order packet division makes `v_h=g/h` entire and nonidentically zero. Since the reciprocal gamma factor is holomorphic near the real line and nonvanishing there, `A` is real-line analytic and nonidentically zero. Its real zeros are a discrete, hence countable, subset. Boundedness of `B=|A|^2` gives `|A|<=sqrt(C_h)` and `|a|<=C_h^{k/2}`. Thus `a`, `|a|^2`, and all their fixed polynomially weighted tilted observations used in the proof belong to their asserted spaces.

For each fixed `u`, the density in GP.5 is positive and integrates to `r_k(u)>0`. Its division by that mass defines a probability measure on this particular fibre; this does not change either original ambient measure. In the `(t_1,...,t_{k-1},u)` coordinate order the underlying linear change of variables has determinant one. For bounded `F`, GP.5 consequently defines `CF(u)` at every `u`; in the general Hilbert-space statement it defines a version almost everywhere.

Disintegration gives

\[
\int_{\mathbb R^k}|Uf|^2\,d\nu
=\int_{\mathbb R}|f(u)|^2r_k(u)\,du,
\qquad CUf=f.
\]

With the pairing conjugate-linear in its first argument,

\[
\langle Uf,F\rangle_\nu
=\int\overline{f(u)}\,CF(u)r_k(u)du
=\langle f,CF\rangle_{\nu_\Sigma}.
\]

This proves `C=U*`, and `P=UC` is the orthogonal projection onto the original sum subspace.

For `k>=2`, the zeros of any factor `A(t_i)` restrict to countably many proper affine hyperplanes of the `(k-1)`-dimensional fibre, including the last coordinate `t_k=u-sum_(i<k)t_i`. Their union has zero fibre Lebesgue measure. The product squared amplitude is therefore positive almost everywhere on every fixed fibre, proving `b_k(u)>0` at every real `u`. Jensen gives `|a_k|^2<=b_k<=C_h^k`. For `k=1`, the asserted almost-everywhere positivity is sufficient and the discrete actual zeros are retained.

## 2. All Hilbert domains and adjoints: GP.6–GP.8

The arithmetic measures are `|a|^2 dnu` and `b_k dnu_Sigma`. The two unitary comparisons are, with their specified targets,

\[
T:L^2(|a|^2d\nu)\longrightarrow L^2(d\nu),\quad TF=aF,
\]
\[
T_\Sigma:L^2(b_kd\nu_\Sigma)\longrightarrow L^2(d\nu_\Sigma),
\quad T_\Sigma f=\sqrt{b_k}\,f.
\]

Their inverse expressions are division by `a` and `sqrt(b_k)` away from null zero sets. For instance, for `H` in the unweighted target,

\[
\int |H/a|^2|a|^2d\nu=\int|H|^2d\nu.
\]

This proves the inverse lies in the weighted domain even when division is an unbounded multiplier on the unweighted space. There is no lower bound on `a` or `b_k` hidden in surjectivity.

The arithmetic inclusion `U_h f=f(sum t_i)` is an isometry because its squared norm disintegrates to `int |f|^2 b_k dnu_Sigma`. Its adjoint is

\[
C_h^{\rm sum}F=\frac{C(|a|^2F)}{b_k}.
\]

Here the numerator has a valid `C`-domain for every arithmetic `F`: boundedness of `|a|^2` implies

\[
\int \bigl||a|^2F\bigr|^2d\nu\le C_h^k\int|aF|^2d\nu<\infty.
\]

Weighted conditional Cauchy–Schwarz proves

\[
|C(|a|^2F)|^2\le b_k C(|a|^2|F|^2),
\]

and integrating after division by `b_k` proves the adjoint is bounded into the asserted arithmetic sum space.

The transported sum inclusion and its adjoint are exactly

\[
Jf=a\,U(f/\sqrt{b_k}),\qquad
J^*H=\frac{C(\overline aH)}{\sqrt{b_k}}.
\]

The conjugate in the second expression is necessary: with the declared pairing, direct substitution gives

\[
\langle Jf,H\rangle_\nu
=\int\frac{\overline{f(u)}}{\sqrt{b_k(u)}}C(\overline aH)(u)r_k(u)du.
\]

Conditional Cauchy–Schwarz also gives

\[
|C(\overline aH)|^2\le b_k C(|H|^2),
\quad\|J^*H\|^2\le\|H\|^2.
\]

Together with `C(|a|^2 Uf)=b_k f`, this proves `J*J=I`. The product expression using the inverse square-root multiplier is read on the dense truncation domain and extended by this isometry. It is not a statement that every intermediate unweighted multiplier is bounded.

It follows that the transported projection is

\[
Q=JJ^*,\qquad QH=aU\left(\frac{C(\overline aH)}{b_k}\right).
\]

This is also `TP_hT^{-1}` with `P_h=U_h C_h^sum`. The formula gives the exact arrow between the two metric presentations while retaining the original complex phase in `T`.

## 3. Fibre angle, conjugations, and trace scope: GP.9–GP.11

Applying `U*=C` to `Jf` gives `a_k f/sqrt(b_k)`. Define `gamma=a_k/sqrt(b_k)` and `N=(I-P)J`. Orthogonality yields

\[
J=UM_\gamma+N,\qquad U^*N=0,
\]
\[
N^*N=J^*(I-P)J=I-M_\gamma^*M_\gamma
=M_{1-|\gamma|^2}=M_{d_k/b_k}.
\]

On one fibre, `e_0=1` and `v=a/sqrt(b_k)` both have norm one, and `gamma=<e_0,v>`. In the explicitly specified orthonormal comparison frame `e_0,e_1`, where `e_1=(v-gamma e_0)/sqrt(1-|gamma|^2)`, the coordinates of `v` are `(gamma,sqrt(1-|gamma|^2))`. Hence the rank-one matrix is

\[
Q_u=vv^*=
\begin{pmatrix}
|\gamma|^2&\gamma\sqrt{1-|\gamma|^2}\\
\overline\gamma\sqrt{1-|\gamma|^2}&1-|\gamma|^2
\end{pmatrix}.
\]

The draft's two off-diagonal conjugations are correct. Let `t=|gamma|^2`. Since `P_u` and `Q_u` are rank-one projections and `Tr(P_u Q_u)=t`,

\[
\operatorname{Tr}(P_u-Q_u)^2=2-2t.
\]

Their commutator has off-diagonal entries `gamma sqrt(1-t)` and `-bar(gamma)sqrt(1-t)`, so its Hilbert–Schmidt square is `2t(1-t)`. For `t=1`, the two ranges coincide and both formulas give zero; for `t=0`, the ranges are orthogonal and the projection-distance square is two while the commutator vanishes. These endpoint distinctions are retained.

These are traces inside an individual conditional fibre Hilbert space. They do not assert global trace-class membership on the direct integral. The finite-rank fibre formulas remain valid even though the full projection difference may have infinite global Hilbert–Schmidt norm.

Finally, for two independent points of the same conditional fibre, expanding the square gives

\[
\tfrac12\iint|a(t)-a(s)|^2d\nu_u(t)d\nu_u(s)
=\int|a|^2d\nu_u-\left|\int a\,d\nu_u\right|^2.
\]

Both unit conditional masses and the complex conjugate cross terms are necessary. This is precisely `d_k(u)`.

## 4. Strict quartet variance and its actual tail constant: GP.12–GP.13

For the original `lambda=1/4`, cancellation of the gamma factor in the completed xi formula leaves

\[
A(t)=-\pi^{-1/4}(t^2+1/4)e^{-it\log\pi/2}
\frac{\zeta(1/2+it)}{h(1/2+it)}.
\]

On `s=1/2+it`, `|s/(s-1)|=1` and `int_1^infty x^{-3/2} dx=2`, so the stated continuation identity proves `|zeta(s)|<=1+2sqrt(t^2+1/4)<=2(1+|t|)`. For `|t|>=T_h`, every actual monic root factor has modulus at least `|t|/2`; multiplicities give `|h|>=(|t|/2)^d`. For `|t|>=1`,

\[
(t^2+1/4)^2\le25t^4/16,
\qquad 4(1+|t|)^2\le16t^2.
\]

Multiplying these exact estimates gives

\[
|A(t)|^2\le25\,2^{2d}\pi^{-1/2}|t|^{6-2d}.
\]

For a full quartet, `d>=4`, so `A(t)` tends to zero at both ends. The proof keeps the factor 25, every power of two, the square-root pi, and the entire degree.

Fix any real `u` and `k>=2`. If `d_k(u)=0`, the variance identity makes `a` constant almost everywhere on that fibre. Since `a` is continuous and the conditional density is positive on every nonempty open fibre set, it is constant everywhere on the fibre. For `k=2`, this makes `A(t)A(u-t)` constant. Its limit is zero as `t` tends to infinity, whereas some real `t` avoids both discrete zero sets and gives a nonzero product. For `k>2`, first fix the middle `k-2` coordinates at nonzeros of `A`, and apply the same argument to the first and last coordinates. Thus the constant would have to be both zero and nonzero, a contradiction.

This proves `d_k(u)>0` at every real `u`. Division by the already proved strictly positive `b_k(u)` gives `|gamma_k(u)|<1`. No statement about the unselected zero locations is used, and no uniform positive lower bound is inferred from this pointwise strictness.

## 5. Complete complex coefficient transform: GP.14–GP.17

The reference polynomials have real coefficients. TG.9–TG.12 proves their generating function and the exact squared norm `c_lambda n!(2lambda)_n`. The classical locator specializes with `x=t/2` and `phi=pi/2`; the monic conversion is multiplication by `n!`.

Polynomial completeness is valid in the declared finite gamma measure. For an `L^2` vector `F` orthogonal to all polynomials, the complex measure `F r(t)dt` has finite total variation by Cauchy–Schwarz. For any sufficiently small positive `a`,

\[
\int e^{a|t|}|F(t)|r(t)dt
\le\|F\|_{L^2(r)}\left(\int e^{2a|t|}r(t)dt\right)^{1/2}<\infty.
\]

Its Fourier transform is consequently holomorphic in a strip containing the real axis. All derivatives at zero vanish by the orthogonality. The identity theorem makes the transform vanish on the strip, and Fourier uniqueness makes the complex measure zero. Since `r>0`, `F=0` almost everywhere. The same proof applies to the sum reference with mass `c_lambda^k`.

For the complex coefficients, first-antilinear orthogonality gives exactly

\[
\mathfrak a_j=\frac{\langle b_j,A\rangle}{c_\lambda j!(\alpha)_j}
=\frac{\int b_j(t)A(t)r_\lambda(t)dt}{c_\lambda j!(\alpha)_j}.
\]

There is no conjugate on `A` in this coefficient. The finite addition formula gives

\[
\int b_n^{(k\lambda)}(u)a_k(u)r_k(u)du
=\sum_{n_1+\cdots+n_k=n}\frac{n!}{\prod_i n_i!}
\prod_i\int b_{n_i}^{(\lambda)}(t)A(t)r_\lambda(t)dt
=c_\lambda^k n!e_{k,n}.
\]

The sum-polynomial squared norm is `c_lambda^k n!(k alpha)_n`; division and completeness prove the first part of GP.16. Parseval then gives

\[
\|Ca\|^2=c_\lambda^k\sum_{n\ge0}\frac{n!}{(k\alpha)_n}|e_{k,n}|^2.
\]

Fubini gives `||a||^2=mu_h^k`. Subtracting the orthogonal sum component therefore yields the exact second part of GP.16, with its original mass factor. The series is convergent because it is the norm of a Hilbert projection. No product of infinite series was exchanged with an integral: every coefficient pairing used a finite identity.

For real admitted `theta` and a polynomial `F(S)`, the squared amplitude of `a U(e^(theta u/2)F)` is bounded by `C_h^k e^(theta u)|F(k/2+iu)|^2`. Exponential integrability gives its finite norm. Conditional expectation commutes with this function of the sum, so its orthogonal components are exactly the two terms of GP.17. The same argument at a compactly narrower theta strip dominates any fixed number of theta derivatives by the remaining exponential margin.

## 6. Positivity, exact matrix types, and quotient section: GP.18–GP.23

The degree restriction `N>=q-1` is essential: it makes the quotient map from `P_N(S)` onto `C[S]/(chi)`. Its kernel is exactly the injective multiplication image `chi P_(N-q)(S)`, by monic division. At `N=q-1` that boundary space is zero.

For each fixed theta, the three linear observation maps from `E` to the common Hilbert target are

\[
L_hF=aU(e^{\theta u/2}F),\qquad
L_{\rm coh}F=U(e^{\theta u/2}a_kF),\qquad
L_{\rm rel}F=(I-P)aU(e^{\theta u/2}F).
\]

The two latter ranges are orthogonal and add to the former. Thus `M_h=L_h^*L_h=M_coh+M_rel`. A fixed `M` is an element of `Herm(E)`; its induced linear map to the conjugate dual is `x ↦ (y ↦ y*Mx)`. This is distinct from the Gram operation on `Hom_C(E,H)`, which is quadratic as a map of real vector spaces.

For coherent positivity, put `f=A r_lambda`. This is a nonzero `L^1` complex function. Its kth convolution cannot be zero in `L^1`, because the Fourier convolution identity would give `(f-hat)^k=0` pointwise, then `f-hat=0`, and finally `f=0` by Fourier uniqueness. The numerator of `a_k` is exactly this convolution. Hence the positive coherent density is positive on a set of positive Lebesgue measure. A nonzero polynomial in the unchanged affine coordinate has only finitely many real zeros, so its coherent integral is positive. For an actual quartet and `k>=2`, the relative density is positive at every real `u` by the preceding strict variance argument, proving strict positivity of its every finite polynomial Gram.

For any positive definite source matrix `M` and any initial section `R_0`, define

\[
R_M=R_0-B_\chi(B_\chi^*MB_\chi)^{-1}B_\chi^*MR_0.
\]

Injectivity of `B_chi` makes its Gram positive definite whenever the boundary is nonempty. This formula preserves `pi R_M=I` and gives `B_chi^*MR_M=0`. If another section had both properties, its difference from `R_M` would lie in the boundary and be M-orthogonal to that same boundary, hence be zero. This proves existence, uniqueness, and the exact least-norm property, including all complex conjugations.

Taking `R_0=R_coh` and using `B_chi^*M_coh R_coh=0` gives GP.20 and `R_h=R_coh-B_chi K`. Expanding in the coherent metric,

\[
R_h^*M_{\rm coh}R_h
=G_{\rm coh}+K^*B_\chi^*M_{\rm coh}B_\chi K,
\]

because the two cross terms separately vanish. Adding `R_h^*M_rel R_h` proves the displayed two-positive-term identity. Neither term should be absorbed or discarded: the first is the cost of moving the coherent least section by the actual boundary correction, and the second is the relative observation of the resulting arithmetic least section.

For the quartet regime, `M_rel` is positive definite and `R_h` is injective since `pi R_h=I`. Consequently `R_h^*M_rel R_h` is positive definite on a nonzero quotient, proving strict positivity of `G_h-G_coh`. At `N=q-1`, `K=0` and the second term remains; for `q=0`, both sections have zero-dimensional domain and their determinants equal one by the empty determinant convention. No analytic seed dimension is inserted.

Writing `D=G_h-G_coh`, the conjugation in GP.22 gives

\[
G_h=G_{\rm coh}^{1/2}(I+E_q)G_{\rm coh}^{1/2},\qquad
E_q=G_{\rm coh}^{-1/2}DG_{\rm coh}^{-1/2}.
\]

Taking determinants proves GP.23. These square roots specify exact invertible comparison maps of the finite metrics; they do not replace the original source matrix or quotient coordinate system.

## 7. Reconstructed graph, original jets, and signed primitive: GP.24–GP.27

Define the gamma multiplier

\[
\mathfrak G_\lambda H(\mathbf t)
=\prod_i\frac{\Gamma(\lambda+it_i/2)}{\sqrt{2\pi}}H(\mathbf t).
\]

Its squared modulus is the product gamma density, so it is an isometry from `H=L^2(nu)` to `L^2(d^kt)`. Gamma is nonvanishing on this line; division also proves onto-ness. The normalized original Mellin map sends `V P` to `mathfrak G_lambda(aUP)`, with every original gamma factor, phase, and `sqrt(2pi)` retained.

Let

\[
\mathfrak L_NP=(U(a_kP),(I-P)aUP),\qquad
\mathcal G_N=\operatorname{im}\mathfrak L_N.
\]

The exact graph-to-reconstructed-image map is

\[
\operatorname{add}_N:\mathcal G_N\longrightarrow aU(E),
\qquad(v,w)\longmapsto v+w.
\]

It is onto by construction. Its two components lie in orthogonal subspaces, so their sum can be zero only when both are zero. Moreover `aUP=0` forces `P=0` by strict positivity of the original source norm. Thus the full chain from the polynomial to its graph and reconstructed image is invertible on the stated finite-dimensional images.

The arithmetic graph observation is therefore, with arrows in their required order,

\[
J^{(k)}\circ\mathcal M_{\rm unit}^{-1}
\circ\mathfrak G_\lambda\circ\operatorname{add}_N.
\]

On `mathfrak L_N P` it equals `eta_(h,k) pi P`. The corresponding quotient observation replaces `J^(k)` by `q^(k)` and yields `sigma_h^{tensor k} eta_(h,k) pi P`. The inverse of addition has domain `aU(E)` and codomain `G_N`; it does not occur in this graph-to-jet composition. At nonzero theta, the common exponential multiplication on both graph components is undone before the original inverse Mellin map. This keeps the original analytic domain and avoids assigning a jet to an arbitrary relative measurable vector.

For the signed relation primitive, successive monic division in the fixed variable order gives

\[
\chi(s_1+\cdots+s_k)=\sum_i h(s_i)Q_i(s_1,\ldots,s_k).
\]

The final remainder vanishes in the tensor remainder basis by the defining cyclic annihilator. The original seed `phi_0=(4pi^2x^4-6pi x^2)e^(-pi x^2)` is even and vanishes at zero. Its real-line integral is `4pi^2·3/(4pi^2)-6pi·1/(2pi)=3-3=0`. With `y=pi x^2`,

\[
\mathcal M\phi_0(s)=\pi^{-s/2}
\bigl(2\Gamma(s/2+2)-3\Gamma(s/2+1)\bigr)
=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2).
\]

The integral initially has domain `Re s>-2`, as in TVB; use `Re s>1` for the absolutely convergent theta sum. Its Mellin transform there is `2 zeta(s) M phi_0(s)=g(s)`, and analytic continuation plus Mellin injectivity gives `h(D)F_h=Theta phi_0` in the original rapidly decreasing space.

Each GP.26 summand has one degree-zero `phi_0` factor and `k-1` degree-one `F_h` factors. The tensor differential acting on the ith position has sign `(-1)^(i-1)`, cancelling the displayed prefactor. Commutation of Euler differentiation with theta then gives exactly

\[
d\mathcal P_\chi F
=\sum_iQ_i(D)F(\textstyle\sum D_j)h(D_i)F_h^{\otimes k}
=\mathcal V(\chi F).
\]

The Euler operator preserves all source domains: the value at zero remains zero; integration by parts gives `int D phi=int phi`; Schwartz decay and evenness are preserved; and on `mathscr B` it preserves every original rapid-decay seminorm. Therefore the cochain is an actual domain element. Inserting the map `-K:C_chi→E_partial` proves

\[
d[-\mathcal P_\chi K]=\mathcal V[-B_\chi K]
=\mathcal V(R_h-R_{\rm coh}).
\]

This verifies the second minus sign as well as the tensor sign. When the boundary is empty, this map is zero. The full jet unit `upsilon_h^{tensor k}` in GP.25 is retained; replacing it by one would change the asserted arithmetic map.

The fixed-support lift of a linear map is `(ell,x)↦(ell,Lx)`, with external absence mapped to external absence. Every actual polynomial relation consequently maps to the supported zero under its original quotient, while its positive source norm and its explicit boundary cochain remain available. The scalar observations have separate precise types: `||·||:H→R_>=0` is a norm; `||·||^2` is a quadratic form; `Gram:Hom_C(E,H)→Herm(E)` is quadratic over real scalars; `Tr:End_C(E)→C` is complex-linear; and `Tr` restricted to Hermitian matrices is real-linear. Their compositions, including `Tr(R*R)`, have the corresponding derived types.

## 8. Independent exact regression fixtures

The subordinate independent review `work/gamma_phase_fibre_projection_fixture_review_20260913.md` supplies a complex finite-fibre fixture and a finite quotient fixture with nonzero `K`. Its reviewed scope is GP.6–GP.11 and GP.20–GP.23. It does not claim these finite fixtures instantiate an actual zeta packet.

Here is an additional finite coefficient fixture calculated independently during this review. It checks the algebraic coefficient and Parseval formulas, which also hold for polynomial amplitudes because every polynomial gamma moment is finite. It is not used as an example of the separate bounded-amplitude or actual-quartet theorem. Retain `lambda=1`, `alpha=2`, `c_lambda=1/2`, `k=2`, and

\[
A(t)=b_0(t)+i b_1(t)+(2-i)b_2(t),\qquad
b_0=1,\ b_1=t,\ b_2=t^2-2.
\]

Then `mathfrak A(z)=1+2iz+(12-6i)z^2`. Its square has coefficient list

\[
(e_{2,0},\ldots,e_{2,4})
=(1,4i,20-12i,24+48i,108-144i).
\]

Dividing term by term by `(4)_n` gives the exact sum expansion coefficients

\[
\left(1,i,1-\frac35i,\frac15+\frac25i,
\frac9{70}-\frac6{35}i\right).
\]

The one-factor amplitude norm is

\[
\mu=\tfrac12\bigl(1+2|i|^2+12|2-i|^2\bigr)=\frac{63}{2}.
\]

The five terms `n! |e_(2,n)|^2/(4)_n` are exactly

\[
1,\quad4,\quad\frac{272}{5},\quad144,\quad\frac{6480}{7}.
\]

The retained product reference mass is `c_lambda^2=1/4`, so

\[
\|Ca\|^2=\frac{39519}{140},\qquad
\|a\|^2=\frac{3969}{4},\qquad
\|(I-P)a\|^2=\frac{24849}{35}.
\]

The last equality follows by exact rational subtraction. A direct finite SymPy calculation performed during this review agreed with every displayed coefficient and fraction. This is finite symbolic regression evidence; it does not certify an analytic zeta integral. Useful negative controls are removal of the `c_lambda^k` factor, replacement of `e_(k,n)` by a real part, omission of `n!`, or deletion of the cross contribution `2·(2i)·(12-6i)` in the cubic coefficient.

## 9. Review of the subsequently added calibration GP.28–GP.29

I read the complete newly added section and the complete companion `work/gamma_phase_fibre_transport_check_20260913.py`. The source explicitly declares this amplitude to be an auxiliary polynomial calibration, with finite fixed gamma moments, and does not apply the bounded-quartet theorem to it. That scope is mathematically appropriate.

Retain `lambda=1`, `k=2`, `c_lambda=1/2`, `c_lambda^2=1/4`, and `A(t)=1+it/2`. The one-factor second monic polynomial is `t^2-2`. The sum-reference recurrence at parameter `alpha_k=4` gives

\[
b_2^{(2)}(u)=u^2-4,\qquad
b_3^{(2)}(u)=u^3-14u,\qquad
b_4^{(2)}(u)=u^4-32u^2+72.
\]

The original conditional product-polynomial formula therefore yields

\[
C(t_1t_2)=\frac15(u^2-4),\qquad
C(t_1^2)=C(t_2^2)=\frac3{10}(u^2-4)+2,
\]
\[
C(t_1^2t_2^2)=\frac3{70}(u^4-32u^2+72)
+\frac65(u^2-4)+4.
\]

The first formula has coefficient `(2)_1^2/(4)_2=4/20=1/5`. The second has coefficient `(2)_2/(4)_2=6/20=3/10`. For the fourth-degree product the leading coefficient is `(2)_2^2/(4)_4=36/840=3/70`; expanding `(b_2(t_1)+2)(b_2(t_2)+2)` gives the two lower-degree contributions with their original coefficients. Thus this is a complete polynomial calculation.

Since

\[
a(t_1,t_2)=1+\tfrac i2(t_1+t_2)-\tfrac14t_1t_2,
\]

conditional integration gives

\[
a_2(u)=\frac65+\frac i2u-\frac1{20}u^2.
\]

Similarly, `|a|^2=(1+t_1^2/4)(1+t_2^2/4)` and the preceding conditional moments give

\[
b_2(u)=\frac{54}{35}+\frac{39}{280}u^2+\frac3{1120}u^4.
\]

The full squared complex conditional amplitude is

\[
|a_2(u)|^2=\frac{36}{25}+\frac{13}{100}u^2+\frac1{400}u^4.
\]

Subtracting coefficient by coefficient gives

\[
d_2(u)=\frac{18}{175}+\frac{13}{1400}u^2+\frac1{5600}u^4>0.
\]

Every GP.28 coefficient, including the imaginary linear amplitude and the positive constant in the variance, therefore checks directly.

The original sum Laplace function has series

\[
\frac14\sec^4\theta
=\frac14+\frac12\theta^2+\frac7{12}\theta^4
+\frac{47}{90}\theta^6+\frac{251}{630}\theta^8+O(\theta^{10}).
\]

Multiplication by the factorials gives moments of orders `0,2,4,6,8` equal to `1/4,1,14,376,16064`. In particular, the two initially transcribed values `10,184` must not be retained in the reader. This correction is independent of the matrices because the Laplace derivatives give it before any quotient calculation.

Substituting the correct moments gives exactly

\[
\int b_2 r_{1,2}=\frac9{16},\qquad
\int u^2b_2r_{1,2}=\frac92,
\]
\[
\int |a_2|^2r_{1,2}=\frac{21}{40},\qquad
\int u^2|a_2|^2r_{1,2}=\frac{21}{5}.
\]

All odd moments vanish because the reference and the displayed squared-amplitude weights are even. In the original monomial frame `(1,S)` with `S=1+iu`, the `(0,1)` entry is consequently the mass itself, and the `(1,1)` entry is the mass plus the weighted second moment. Since `chi(S)=(S-1)^2-2` has degree two and `N=1`, the boundary is empty and the original quotient section is the identity in these coordinates. This proves

\[
G_h=\frac1{16}\begin{pmatrix}9&9\\9&81\end{pmatrix},\qquad
G_{\rm coh}=\frac1{40}\begin{pmatrix}21&21\\21&189\end{pmatrix},
\]
\[
G_h-G_{\rm coh}=\frac1{80}\begin{pmatrix}3&3\\3&27\end{pmatrix}.
\]

Their exact determinants are, respectively, `81/32`, `441/200`, and `9/800`, as displayed in GP.29. The positive first leading minor and positive determinant prove strict positivity of the relative quotient contribution in this calibration.

The checker independently derives the one-factor and sum moments by formal differentiation of the exact Laplace series, constructs the density coefficients by independent product-moment equations, verifies nine complex-amplitude moments and nine squared-amplitude moments, and checks the source/relation sections for `N=1,2,3,4`. Its source has no Python `assert` statement: each explicit Boolean result contributes to the returned failure count and exit code. Its 61 checks consist of eight finite-fibre checks, eighteen moment comparisons, three global/coordinate identities, and thirty-two quotient checks. It correctly records that these are finite exact regressions, with no analytic zeta interval or asymptotic certificate claimed.

I reviewed the checker rather than duplicating the root author's already completed 61-check execution. The separate subordinate fixture executed 37 different exact identities and its complete report was read during this review. My direct independent Laplace-series calculation confirmed the corrected five-moment list above. These scopes distinguish a full proof read, a code review, and executed finite checks.

## Final pin and correction verification

The final reviewed GP.1–GP.29 source has SHA256 `9f6f62da311c0f6c76761ee74e234b3c77d9441e2136908857208e798ac81e76`. I reread its first 329 lines and the complete updated ending, including GP.28–GP.29, and checked each identified repair against that source. The corrected Gram/conjugate-dual types are at lines 330–339; the graph observation has the correctly ordered addition, gamma multiplication, and inverse Mellin composition at lines 434–445; the separate norm, trace, and Gram types appear at lines 516–524; and the corrected moment list is at line 561. The standalone preamble now includes `mathrsfs` at line 3. The remaining intervening quotient equations are the same equations checked above and by the independent fixture reviewer. No unresolved mathematical error remains in the reviewed source.

The complete root checker read for this review has SHA256 `1f866c9033cd7c14e72e2260f533544ea02ea33733ff2a69c5af6e08f9548945`. The subordinate full fixture review has SHA256 `d49d3619454df7d0b9222fe99f13a46de4deb59233671247e2007469838da3c5`; its exact 37-identity checker has SHA256 `e2cf0a3f4a6ff87db683abd918e9740e328d39ad47085b629fac8a9f696fc7a2`, and its completed ordinary-run result has SHA256 `702b90216ebe2221e0cc8ca827c74b0f34c86a09d32756af3c436f0d59fa4b37`.

Disposition: the full GP.1–GP.29 proof, at the stated final pin, passes this independent mathematical review. This does not claim that the finite fixtures prove a growing-degree zeta estimate, nor that the review performed Lean verification, certified numerical zeta integration, or visual PDF QA. The exact newly proved maps and strict quartet contribution stand with the scope and complete calculations recorded above.
