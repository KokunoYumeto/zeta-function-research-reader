# Independent layer, primitive, and antidual audit — 12 September 2026

Scope: mathematical verification of §§3, 4, and 6 of
`output/split_zero_rh_tandem_2026-09-12/sources/web_kernel_layer_delivery/Tau_Kernel_Layer_Integration/RESEARCH_NOTE.md`,
against `tex/coherent_tensor_integration.tex` in the same output package.
Source and integrated TeX were read directly. Neither was edited. This
audit checks the finite algebra and the actual primitive using the original
analytic identities already proved in CT.1–2; it does not independently
reprove all analytic input or execute Lean. The parent audit owns the full
source review and fresh fixture runs.

Result: no mathematical correction found in the assigned claims. The
following derivations record the signs and types explicitly.

## 1. Coordinate dictionary

Let `r=d^k`, `q=|Sigma_(N+1)|`. The source supplement uses

\[
K_N=G_N^{-1}:E^{\mathrm{anti}}\longrightarrow E.
\]

In fixed monomial coordinates the antidual is represented by columns
`lambda`, with pairing `x* lambda`. This source `K_N` is the inverse
**actual** metric, including the local arithmetic unit. For `k=1` it is
`mathcal C_(h,N)` in CT.3, not the bare remainder kernel called `K_N`
there. The exact relation is

\[
K_N^{\mathrm{source}}
=U_{\upsilon_h}K_N^{\mathrm{CT.3}}U_{\upsilon_h}^{*}.
\]

Thus all layer columns `a_beta=upsilon_h^tensor k [p_beta]` include the
unit. This is consistent with CT.2 and CT.11–13. In these coordinates

\[
\mathscr E_N:\mathbb C^q\to\mathcal E_N,\quad
U_N:\mathbb C^q\to E,\quad
F_N:E^{\mathrm{anti}}\to\mathbb C^q,
\]

where the last map is represented by the declared rows; composition
`F_N G_N` is a map from `E` to the layer coordinate space. Matrix adjoints
use the stated Hilbert structure on the function space and the coordinate
pairings. The source's displayed notation `F_N:E->C^q` uses the fixed
coordinate identification; its compositions are correct. `D_N,H_N` are
`q` by `q`; `G_N,K_N,V_N,W_N` are `r` by `r`; `Y_N,C_N` map `E` to
the actual function layer.

## 2. Actual relation basis and positive Gram matrix

Write `f_beta=mathcal T(p_beta)` and

\[
e_\beta=f_\beta-R_Na_\beta,\qquad |\beta|=N+1.
\]

The full jet is zero because `J R_N=I`. Since the full jet multiplier
is a unit, the numerator is in the original ideal
`(h(s_1),...,h(s_k))`; its total degree is at most `N+1`.
Each `f_beta` is orthogonal to every old polynomial image: an old
product-basis multi-index `alpha` has `|alpha|<=N`, so at least one
coordinate satisfies `alpha_i<beta_i` and its product inner product is
zero. Both `f_beta` and `R_Na_beta` are orthogonal to `L_N`. Therefore
`e_beta` is in `E_N=L_(N+1) intersect L_N^perp`.

The degree-`N+1` coefficients of the `e_beta` equal those of the monic
product polynomials `p_beta`. They are independent. To express any
element of `E_N`, subtract its degree-`N+1` combination of the `e_beta`.
The remainder belongs to both `L_N` and `E_N`, hence has zero norm and
is zero. This proves the asserted isomorphism, without a dimension-only
argument.

The cross terms `f_beta* R_N` vanish. Thus, retaining the original
positive norms,

\[
\mathscr E_N^*\mathscr E_N
=D_N+U_N^*G_NU_N=H_N,\qquad
\mathscr E_N^*R_N=-U_N^*G_N.
\]

For nonzero `c`, `c*H_Nc=c*D_Nc+(U_Nc)*G_N(U_Nc)>0` because every
diagonal entry of `D_N` is the actual positive `kappa_beta`.

The maps `E_N -> L_(N+1)/L_N`, `e -> [e]`, and
`[z] -> (I-P_N)z` are inverse: adding a vector of `L_N` does not change
the latter, and the orthogonal decomposition establishes both composites.
This matches CT.14–16, including the supported-zero transition.

## 3. Primitive and its two signs

Fixed-order monic division of the displayed numerator gives

\[
p_\beta-\sum_{|\alpha|\le N}
 p_\alpha\frac{a_\alpha^*G_Na_\beta}{\kappa_\alpha}
=\sum_{i=1}^kh(s_i)Q_{i,\beta},
\qquad \deg Q_{i,\beta}\le N+1-d.
\]

Each division removes a selected monomial factor of degree `d` and
introduces only smaller powers in the same variable, so the total-degree
bound is preserved through the declared division order. The final
remainder is zero because its full jet is zero and the unit is invertible.

In the original complex `[V -> B]`, in degrees `0,1`, define

\[
\Psi_{i,\beta}=(-1)^{i-1}Q_{i,\beta}(D_1,\ldots,D_k)
 (F_h^{\otimes(i-1)}\otimes\phi_*\otimes
  F_h^{\otimes(k-i)}).
\]

Only the degree-zero factor has nonzero differential. The preceding
`i-1` factors have degree one, so the tensor differential contributes
`(-1)^(i-1)`. CT.2 gives `Theta phi_*=h(D)F_h`. The product of the two
signs is `+1`, giving exactly

\[
d\Psi_{i,\beta}=\mathcal T(h(s_i)Q_{i,\beta}),\qquad
d\sum_i\Psi_{i,\beta}=e_\beta.
\]

The polynomial generators commute with the differential, as in CT.2.
No primitive has been moved to an unspecified completion.

## 4. Boundary coordinates

Projection onto the layer is `mathscr E_N H_N^-1 mathscr E_N*`, hence

\[
Y_N=-\mathscr E_NH_N^{-1}U_N^*G_N.
\]

In the representative expansion, multiplying `p_alpha` by the summed
generator `s_1+...+s_k` has top-degree term
`sum_i p_(alpha+e_i)`. All remaining terms have degree at most `N`.
Thus the coefficient of `p_beta` in `D^(k)R_Nu` is

\[
\sum_{i:\beta_i>0}
\frac{a_{\beta-\mathbf e_i}^*G_Nu}
 {\kappa_{\beta-\mathbf e_i}}=(F_N)_\beta G_Nu.
\]

`R_NAu` has degree at most `N`. Subtracting
`mathscr E_N F_N G_Nu` from the actual boundary gives an old-degree
zero-jet vector, hence a vector of `L_N`. Consequently

\[
C_N=(I-P_N)B_N=\mathscr E_NF_NG_N.
\]

Substitution into CT.16 gives the positive endpoint sign:

\[
W_N=G_N(U_NF_N+F_N^*U_N^*)G_N.
\]

The minus in `Y_N` cancels the minus in the source boundary identity.

## 5. Antidual reflection, metric, generator, and defect

Suppress `N` and write the original involution as `j(x)=C bar x`.
Its identities from CT.16a are

\[
C\overline C=I,\quad C^*GC=\overline G,\quad
AC=C(kI-\overline A),\quad C^*WC=-\overline W.
\]

For the conjugate-linear functional `ell_lambda(x)=x*lambda`, the
induced reflection is defined by
`ell_(j#lambda)(x)=overline{ell_lambda(jx)}`. Direct evaluation gives

\[
\overline{(C\overline x)^*\lambda}
=x^*C^T\overline\lambda,
\qquad j^\#\lambda=C^T\overline\lambda.
\]

Its square is the identity, since
`C^T bar(C^T)=(bar C C)^T=I`. Inverting the metric identity, using
`C^-1=bar C` and `(C*)^-1=C^T`, gives exactly

\[
(C^T)^*KC^T=\overline C K C^T=\overline K.
\]

The Riesz coordinate maps respect these reflections:

\[
G C=C^T\overline G,\qquad
K C^T=C\overline K.
\]

Since `V=KWK`, insert the inverse factors between the three terms:

\[
\begin{aligned}
\overline C V C^T
&=(\overline C K C^T)
 ((C^T)^{-1}W\overline C^{-1})
 (\overline C K C^T)\\
&=\overline K(C^*WC)\overline K
=-\overline V.
\end{aligned}
\]

Thus the supplement's reflection signs and transpose are correct even
for nonreal, nonunitary coordinate matrices `C`.

For the natural weight-`k` antidual action `A^D=kI-A*`, its metric
defect is

\[
(A^{\mathrm D})^*K+KA^{\mathrm D}-kK
=(kI-A)K+K(kI-A^*)-kK=-V.
\]

Transposing `AC=C(kI-bar A)` gives
`A^D C^T=C^T A^T=C^T(kI-overline{A^D})`, so the antidual generator
also has the exact stated reflection type.

The coordinate change `u=K lambda` gives
`u*Gu=lambda*Klambda` and `u*Wu=lambda*Vlambda`. Equivalently

\[
W-\lambda G=G(V-\lambda K)G,
\quad
\det(W-\lambda G)=(\det G)^2\det(V-\lambda K).
\]

This proves both the two-sided order equivalence and retention of all
generalized eigenvalue multiplicities. The defect for `A^D` has the
additional minus already computed above.

## 6. Positive matrix certificate

Interpret the displayed matrix norm as the operator norm for the fixed
coordinate Euclidean structures. Put `DeltaA=A-Ahat`, `DeltaK=K-Khat`.
The exact perturbation is

\[
\begin{aligned}
V-\widehat V={}&\widehat A\Delta K+\Delta K\widehat A^*
 -k\Delta K+\Delta A\widehat K+\widehat K\Delta A^*\\
&+\Delta A\Delta K+\Delta K\Delta A^*.
\end{aligned}
\]

Submultiplicativity and the adjoint norm identity give

\[
\|V-\widehat V\|\le
(2\|\widehat A\|+k)\eta_K
 +2\eta_A(\|\widehat K\|+\eta_K)=\eta_V.
\]

All matrices being ordered are Hermitian: `Khat` is explicitly required
Hermitian, hence so is `Vhat`. For either choice of sign and `epsilon>=0`,

\[
\epsilon K\pm V\succeq
\epsilon\widehat K\pm\widehat V
 -(\epsilon\eta_K+\eta_V)I.
\]

Also `K succeq Khat-eta_K I`. The two displayed sufficient conditions
in (25) therefore prove actual positivity of `K` and both desired bounds.
The proof retains the mixed perturbation `2 eta_A eta_K`; no missing
cross term or sign error occurs. The certificate requires genuine input
enclosures and asserts no enclosure of the infinite arithmetic moments.

## Handoff

No source correction is requested. When integrating the supplement, use
an explicit local alias for its inverse actual metric to prevent the
existing CT.3 bare-kernel notation from being mistaken for it. This is a
notation crosswalk, not a change to the source mathematics. The detailed
antidual pairing above can be used if the cumulative reader expands the
source's short reflection paragraph.
