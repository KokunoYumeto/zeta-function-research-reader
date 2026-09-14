# Independent analytic audit of the arithmetic sum connection

Date: 2026-09-12. The complete delivered `NOTE.tex`, `RESEARCH_NOTE.md`, published-delivery metadata and the complete private pasted request were read. The calculations below independently verify the amplitude, phase, mass, Jacobian, differential energy, matrix connection, gauge covariance and graph domain. They also state two precise presentation corrections and the exact two-branch map needed when transporting the delivery's hypotheses to a positive half-line. No delivered source or main/frozen paper was edited.

## Source hashes and scope

| Object | SHA-256 | Complete reading |
|---|---|---|
| `sources/web_sum_connection_delivery/Tau_Sum_Connection_Control/NOTE.tex` | `11870208e3a08df186e42629ae1a6c956faaf28f79dfce0dc2f2d44dc64b4687` | Sections 1–8, all displayed formulas and proofs, calibrations and reference/reading record. |
| `sources/web_sum_connection_delivery/Tau_Sum_Connection_Control/RESEARCH_NOTE.md` | `c24b120fdd6ba6549e7f63dd9f2ae269e51123fe0e097b7b976f842bba3729d9` | Complete parallel mathematical source. |
| Private request receipt | `0ef90b907bb88195ddfc3e9ce0c377f559e3ca905830248341a819b9244d2a3e` | Complete private pasted final request; its content and private path are not required in a public package. |

The delivered metadata identifies draft PR20, base commit `33b29f706008124886614ba4bd55bffc489df9e2`, head commit `2144c358c2b41aa235b15cf0fa472289aec8673f`, five added files and no modified existing file. These are recorded as delivered metadata, not a claim of independent network verification. The analytic audit uses the full supplied mathematical sources above.

The actual source theorem supplies `F_h` in the stated test space with Mellin transform `v_h=g/h`, `g=2xi`, including its full packet orders. This audit uses that previously constructed source as input and proves the analytic consequences below. It does not relabel the delivery's finite tests or approximate seed integrals as an analytic certificate.

## 1. The original test space gives every required regularity statement

Let `D=−x d/dx` and

\[
\mathscr B=\{F\in C^\infty(0,\infty):
\sup_{x>0}x^b|D^jF(x)|<\infty\text{ for every }b\in\mathbb Z,j\ge0\}.
\]

For `F in B`, set `q=log x` and `f(q)=e^(q/2)F(e^q)`. Direct differentiation gives

\[
f^{(j)}(q)=e^{q/2}\sum_{\ell=0}^j
\binom j\ell(1/2)^{j-\ell}(-1)^\ell D^\ell F(e^q).
\]

For q positive, choosing any integer b greater than `A+1/2` bounds each summand by a constant times `e^(−Aq)`. For q negative, choosing an integer b less than `−A` bounds it by a constant times `e^((A+1/2)q)`, after increasing A if necessary. Thus every derivative decays faster than every fixed exponential at both endpoints; multiplying by any polynomial in q preserves these bounds. In particular f is Schwartz and square-integrable.

Logarithmic multiplication preserves the original test space directly:

\[
D^j((\log x)F)=(\log x)D^jF-jD^{j-1}F
\]

for j positive, with the evident j=0 formula. The inequality `|log x|≤x+x^(−1)` for x>0 and the original adjacent integer weights prove every required seminorm bound. Iteration handles all powers of log x and finite products of coordinate logarithms. Applying polynomials in D also preserves B by its definition.

Use the exact Fourier convention

\[
(\mathcal F_+f)(t)=(2\pi)^{-1/2}\int_{\mathbb R}f(q)e^{itq}\,dq.
\]

The logarithmic change of variables is unitary from `L²(dx)` to `L²(dq)`, and Mellin–Fourier Plancherel therefore gives

\[
a_h(t)=\frac{v_h(1/2+it)}{\sqrt{2\pi}}=\mathcal F_+f_h(t),
\qquad
\mu_h=\int|a_h|^2dt=\int_0^\infty|F_h|^2dx.
\]

The same change followed by Fourier transformation shows that a_h and every derivative are Schwartz. In particular a_h, a_h', and their polynomially weighted derivatives satisfy all integrability and endpoint requirements in sections 2–4. All factors `sqrt(2pi)` and the unaltered mass remain.

Finite tensor source functions `P(D_1,...,D_k)F_h^(tensor k)` and their logarithmic multiples lie in the algebraic tensor span of B, so the graph argument needs no assertion about an unspecified completion topology: that finite span is an explicit sufficient domain inside the delivery's completed tensor test space.

## 2. Fixed phase and the actual Fisher energy

Define `p^dagger(s)=overline{p(1−overline s)}`. Dagger-stability of the full packet gives

\[
h^\dagger(s)=\prod_\rho(1-s-\overline\rho)^{m_\rho}
=(-1)^d h(s).
\]

The functional equation and reality of the coefficients of g give `g^dagger=g`, hence `v_h^dagger=(-1)^d v_h`. On the integration line, `1−overline s=s`; therefore

\[
\overline{a_h(t)}=(-1)^d a_h(t),\qquad
\overline{a_h'(t)}=(-1)^d a_h'(t).
\]

Thus a_h is real for even d and purely imaginary for odd d, with that same fixed phase for its derivative. Writing `w_h=|a_h|²`, one obtains off its isolated zeros

\[
w_h'=2\overline{a_h}a_h'\in\mathbb R,\qquad
\frac{|w_h'|^2}{w_h}=4|a_h'|^2.
\]

The quotient is irrelevant on the null zero set; the smooth amplitude expression defines the integrable quantity without a bounded logarithmic score. Mellin differentiation and Plancherel prove the full equality

\[
\mathcal I_h=4\|a_h'\|_2^2
=4\int_0^\infty(\log x)^2|F_h(x)|^2dx<\infty.
\]

Schwartz decay and the fixed phase also give `integral conjugate(a_h)a_h' = (1/2)integral w_h'=0`. This is the actual cancellation of the distinct-index product terms; it is not an assumption about an arbitrary complex amplitude.

## 3. Centred coordinate determinant, positivity and exact tensor energy

Keep the coordinate order `(u,y_1,...,y_(k−1))` and the original order `(t_1,...,t_k)`. The inverse matrix has first column all `1/k`, upper relative block `I_(k−1)` and last relative row all −1. Move its first column to the last position, with sign `(-1)^(k−1)`. Its determinant is then the Schur complement `1/k+(k−1)/k=1`. Consequently the original signed determinant is `(-1)^(k−1)` and its absolute value is exactly one. For k=2 the further substitution `v=2y_1` produces precisely `dt_1dt_2=du dv/2`.

The function `Psi_k=product_i a_h(u/k+y_i)` is Schwartz on the full `(u,y)` space because the original tensor product is Schwartz and the coordinate map is invertible and linear. Every derivative and polynomial relative multiplier is Schwartz as well. On a fixed u-fibre, every zero of a factor belongs to an affine hyperplane of measure zero: each `t_i=u/k+y_i` is a nonconstant linear function of y when k≥2. Their countable union is null. Thus the fibre density is positive almost everywhere and integrable; its integral m_k(u) is strictly positive for every real u.

Comparing with the usual convolution coordinates `t_1,...,t_(k−1)` at fixed u gives exactly `m_k=w_h^(star k)`; the translation to y has determinant one. Fubini yields the full mass `integral m_k=mu_h^k`. Differentiated Schwartz bounds justify fibre differentiation to every order and the integration of products below.

At fixed y,

\[
\partial_u\Psi_k=\frac1k\sum_i
a_h'(t_i)\prod_{j\ne i}a_h(t_j).
\]

The k diagonal squared terms integrate to `mu_h^(k−1)||a_h'||²` each. Each ordered distinct-index term integrates to `mu_h^(k−2)|integral conjugate(a_h)a_h'|²=0`. The Jacobian gives no further factor. Therefore

\[
\int\!\|\partial_u\Psi_k\|_{L^2(dy)}^2du
=\frac{\mu_h^{k-1}}{k}\|a_h'\|_2^2
=\frac{\mu_h^{k-1}}{4k}\mathcal I_h.
\]

The fibre line has squared norm m_k and projection `Pi_0 Z=Psi_k <Psi_k,Z>/m_k`, with the inner product antilinear in the first variable. Product fixed phase proves `<Psi_k,partial_u Psi_k>=m_k'/2` is real. Thus

\[
n_k=\partial_u\Psi_k-\frac{m_k'}{2m_k}\Psi_k,
\qquad
\|\partial_u\Psi_k\|^2=\frac{|m_k'|^2}{4m_k}+\|n_k\|^2.
\]

The right-hand summands are nonnegative and their sum has finite integral already proved above. Integration proves the exact delivery identity

\[
\boxed{\mathcal I_{h,k}+4\int\!\|n_k\|^2du
=\frac{\mu_h^{k-1}}{k}\mathcal I_h.}
\]

This calculation retains both derivative components, the mass power and every factor four. The scalar result corresponds to the constant relative column with coefficient identically one. Arbitrary polynomial coefficients also have a derivative term, which is retained by the full connection below.

## 4. Full relative polynomial frame and differential domain

The relative polynomial ring is `C[z_1,...,z_(k−1)]`, with `z_k=−sum_(i<k)z_i`. Linear independence of a relative family means independence in this ring. For the full degree-M source, take a homogeneous monomial basis, or a degree-compatible basis of the stated invariant subspace. The linear coordinate isomorphism `s_i=S/k+z_i` preserves total degree; hence the exact coefficient constraints are `deg f_alpha≤M−deg theta_alpha`. An arbitrary independent family gives its specified subspace only, not automatically all numerators. This is the reading of the source's explicit degree-compatible choice.

Let `j_u c=Psi_k sum_alpha theta_alpha(iy)c_alpha`. Each column and its u derivatives are Schwartz in the full variables, so u maps smoothly into bounded operators from the fixed finite coefficient space to `H=L²(dy)`. Fibre integrals and their derivatives are justified by the same bounds. A nonzero coefficient vector gives a nonzero polynomial on the real relative slice, outside a set of measure zero. This and the positive fibre density prove `W=j* j>0` for every u. Its inverse is smooth on R, although no global boundedness of that inverse is implied.

In the original frame,

\[
B=j^*j',\quad T=(j')^*j',\quad W'=B+B^*,\quad B=B^*=W'/2.
\]

The Hermitian assertion follows because `conjugate(Psi_k) partial_u Psi_k` is real, leaving the ordinary Hermitian polynomial Gram integrand. It holds with complex relative polynomial coefficients too.

The projection `Pi=jW^(−1)j*` is self-adjoint and idempotent by direct multiplication. Then

\[
\Gamma=W^{-1}B,\quad N=(1-\Pi)j',\quad
j\Gamma=\Pi j',\quad j^*N=0.
\]

For locally absolutely continuous coefficient sections c, the exact weak derivative identity is

\[
(jc)'=j(c'+\Gamma c)+Nc.
\]

On every compact u interval, W and its inverse are bounded, so this statement agrees with the ordinary coefficient Sobolev formulation. The global domain is precisely the sections for which `jc in L²(du;H)` and this weak derivative is in L². Equivalently, their two orthogonal components have finite summed energy

\[
\int(c'+\Gamma c)^*W(c'+\Gamma c)\,du
+\int c^*\mathcal N c\,du<\infty,
\]

where

\[
\mathcal N=N^*N=T-B^*W^{-1}B
=T-\tfrac14W'W^{-1}W'\succeq0.
\]

Multiplying out also proves `Gamma*W+W Gamma=W'`. No order of the noncommuting matrices has been exchanged.

For every original polynomial coefficient c_P, the amplitude jc_P and its derivative are Schwartz. The two projected pieces are consequently L², by the orthogonal norm identity, even if inverse W prevents one from asserting separate global Schwartz bounds for those pieces. Their sum is the original Schwartz derivative. This proves the precise domain needed for the source graph and explains why no independent arithmetic jet is assigned to an arbitrary normal section.

## 5. Full gauge covariance, including its extra derivative

Let C(u) be any specified smooth invertible matrix, `j^C=jC`, and `c^C=C^(−1)c`. The represented amplitude is unchanged. Differentiation gives every transformed integral, in its original order:

\[
W^C=C^*WC,\qquad
B^C=C^*BC+C^*WC',
\]
\[
T^C=C^*TC+C^*B^*C'+(C')^*BC+(C')^*WC'.
\]

Since the image subspace of jC equals that of j, `Pi^C=Pi`. Therefore

\[
\Gamma^C=C^{-1}\Gamma C+C^{-1}C',\qquad
N^C=NC,\qquad \mathcal N^C=C^*\mathcal N C,
\]

and `nabla^C c^C=C^(−1)nabla c`. These equations prove the transformed energy identity and equality of the exact graph domains even for C with unbounded global growth: the domain is the image of the original section domain under C inverse, not a separately chosen set of polynomial or arbitrary measurable sections.

The original identity `B=W'/2` is frame-specific. After an arbitrary varying frame,

\[
B^C-\tfrac12(W^C)'=\tfrac12(C^*WC'-(C')^*WC).
\]

For the exact witness `C=e^(iu)I`, one has `W^C=W`, `B^C=B+iW`, and `Gamma^C=Gamma+iI`. Thus reimposing `Gamma^C=(W^C)^(−1)(W^C)'/2` would drop a real derivative term. The delivery does not make that error; the extra formulas here make its scope explicit.

## 6. Mellin operator, logarithmic conjugate and graph arithmetic jet

On the original test domain, integration by parts with the proven endpoint decay gives `M(D_iF)=s_i M(F)`. Differentiation under the Mellin integral gives `partial_(s_i)M(F)=M((log x_i)F)`. In the centred real coordinates `partial_u=(1/k)sum_i partial_(t_i)`, so

\[
\mathscr U_kD^{(k)}=(k/2+iu)\mathscr U_k,\qquad
\partial_u\mathscr U_k=i\mathscr U_k\mathscr L_k,
\quad \mathscr L_k=\frac1k\sum_i\log x_i.
\]

The original physical commutator is checked before quotienting:

\[
D_i((\log x_j)F)=(\log x_j)D_iF-\delta_{ij}F,
\qquad [D^{(k)},\mathscr L_k]F=-F.
\]

All operations preserve the finite tensor test domain already specified. The maximal Hilbert domain of L_k is `{F: L_k F in L²}`, and its unitary image is the weak Sobolev domain `{f:partial_u f in L²}`; the factor is `L_k=U_k^(−1)(−i partial_u)U_k`. The scaling realization has domain `{F:u U_kF in L²}`. The commutator is asserted on the common invariant test domain, not on an unspecified domain of two unbounded compositions.

For the actual source polynomial P, put `c_P=(f_alpha(k/2+iu))`. Its derivative is `i f_alpha'(k/2+iu)` in each coefficient; this factor i is retained. The graph map is

\[
\mathscr D_M(P)=(j\nabla c_P,Nc_P).
\]

Both entries lie in L² and are pointwise orthogonal. Therefore Add is an isometric injection on this graph: if the sum is zero, each component has zero norm. Its sum equals `partial_u U_k T_h^(k)P=i U_k L_k T_h^(k)P`. Applying `−i U_k^(−1)` returns an actual finite sum of B tensor functions. Thus applying the original full jet J is well-defined on the combined graph and gives exactly the source composite in equation4.11. No value of either separated projected section at a complex packet point is assumed.

### Precise diagram correction

The shorthand arrow in source equation8.2, labelled only `partial_u` with target G_M, has an incorrect displayed codomain: the derivative is the amplitude sum, whereas G_M consists of ordered pairs. The exact graph-valued map on the original filtered image is

\[
v\longmapsto(\Pi\partial_uv,(1-\Pi)\partial_uv).
\]

Its composition with Add is the bare derivative. Conversely the same two orthogonal projections recover the pair from every amplitude in the actual derivative image. This proves an isometric correspondence, repairs that arrow's type, and uses precisely the maps already established in source4.9–4.11. No change to the source theorem is required.

## 7. The exact two-branch transport under the delivered hypotheses

Dagger-stability proves fixed phase; it does not by itself prove `w_h(−t)=w_h(t)`. The earlier SP and SSP quartet packet has additional reflection symmetry giving that evenness. For a general homogeneous relative frame under a quartet packet, global reflection gives

\[
W(-u)=R^*W(u)R,\qquad R_{\alpha\alpha}=(-1)^{\deg\theta_\alpha},
\]

by substituting y to −y in the defining fibre integral. It gives ordinary matrix evenness for the k=2 symmetric Delta-power frame, where every relative degree is even. It need not give ordinary evenness for a general mixed-parity relative frame.

Here is the exact positive-half-line map without adding either symmetry hypothesis. For x>0 put `W_+=W(sqrt x)`, `W_−=W(−sqrt x)` and

\[
f(\sqrt x)=A(x)+i\sqrt xB(x),\qquad
f(-\sqrt x)=A(x)-i\sqrt xB(x).
\]

The inverse is `A=(f_++f_−)/2`, `B=(f_+−f_−)/(2i sqrt x)`. The norm is exactly the L² norm of `(A,B)` against the positive block matrix measure

\[
\frac{dx}{2\sqrt x}
\begin{pmatrix}
W_++W_-&i\sqrt x(W_+-W_-)\\
-i\sqrt x(W_+-W_-)&x(W_++W_-)
\end{pmatrix}.
\]

This follows by expanding the two original positive quadratic forms and keeping their two Jacobians. The block matrix is positive because it is congruent by the displayed invertible branch map to `diag(W_+,W_−)`. If W is even, the off-diagonal blocks vanish and the measure is exactly `Lambda direct-sum xLambda`, with `dLambda=W(sqrt x)dx/sqrt x`, recovering SSP.27. Thus the delivery's original hypotheses have an exact typed map to the half-line model; any further even decomposition has its explicit symmetry hypothesis.

## 8. Analytic interface to conormal differentiation

The logarithmic multiplier preserves the actual test space, so differentiating `M Theta phi=g H_phi` is justified and gives `g'H_phi+gH_phi'` before jets. Since h divides g with the selected complete orders, full jets remove the second term and retain `j_h(g')j_h(H_phi)`. The tensor analogue uses `partial_S^rel=(1/k)sum partial_(s_i)` on the entire actual multiplier `U P`, including the derivative of U. This is the analytic domain justification of source5.1 and5.11; the detailed finite conormal module and test audit is handled in the parallel algebra lane.

One local wording correction is useful: if `h=z^m e(z)` with e(0) nonzero, then modulo z^m,

\[
h'(z)a(z)=m e(0)a(0)z^{m-1}.
\]

Thus the conormal derivative reads the constant coefficient a(0) and produces the top nilpotent direction with its factor m and unit e(0). The source sentence saying it “detects the z^(m−1) coefficient” should be read or replaced by this exact formula. The displayed image dimension5.9 and derivative row5.6 are unaffected.

## 9. A further strict result for the actual arithmetic residual

The actual arithmetic amplitude has an unremoved real-line zero after every fixed finite packet: Hardy's theorem supplies infinitely many critical-line zeros, while h removes only finitely many of them. The original source and reading receipt for this use of Hardy are recorded in `work/theta_norm_literature_route_20260912.json` and the complete TG source audit. Choose one such zero T and retain its full order ell≥1, so

\[
a_h(T+\delta)=c\delta^\ell+O(\delta^{\ell+1}),\qquad
a_h'(T+\delta)=\ell c\delta^{\ell-1}+O(\delta^\ell),\qquad c\ne0.
\]

**Theorem.** For the actual a_h and every integer k≥2,

\[
\int_{\mathbb R}\|n_k(u)\|^2du>0,
\qquad
\mathcal I_{h,k}<\frac{\mu_h^{k-1}}k\mathcal I_h.
\]

For every k≥3 the stronger statement `||n_k(u)||>0` holds for every real u.

**Proof.** First choose real numbers `b_2,...,b_k` away from the discrete zero set of a_h, and put `u_0=T+sum_(i=2)^k b_i`. At the corresponding fibre point use the path

\[
t_1=T+\delta,\quad t_i=b_i\ (2\le i<k),\quad t_k=b_k-\delta.
\]

It lies in the same original sum fibre u_0. Let `A=product_(i=2)^k a_h(b_i)`, which is nonzero. The amplitude and its derivative at fixed relative coordinates have expansions

\[
\Psi_k=cA\delta^\ell+O(\delta^{\ell+1}),\qquad
\partial_u\Psi_k=\frac\ell k cA\delta^{\ell-1}+O(\delta^\ell).
\]

The derivative formula is the original sum of k product derivatives: its i=1 term has the displayed nonzero leading coefficient, while every other term retains the factor `a_h(T+delta)` and therefore has order at least ell. Since `m_k'(u_0)/(2m_k(u_0))` is finite, subtraction of that constant times Psi_k gives

\[
n_k(u_0,\mathbf y(\delta))
=\frac\ell k cA\delta^{\ell-1}+O(\delta^\ell).
\]

Its leading coefficient is nonzero. Thus n_k is nonzero at nearby points of this path and, by its continuous amplitude expression, on a nonempty open set of the full relative fibre. Its squared fibre norm is strictly positive. The H-valued functions Psi_k and partial_u Psi_k are continuous in u by the proved Schwartz bounds, and m_k is positive and smooth. Consequently n_k is continuous as an H-valued function near u_0. Its squared norm stays positive on some u interval, proving strictly positive integrated energy. The strict Fisher inequality follows from the already proved exact identity.

For k≥3, this construction is possible for every prescribed u_0. Choose `b_3,...,b_(k−1)` away from zeros when that list is nonempty. Then choose b_2 outside both the discrete zero set and its translate-reflection that would make `b_k=u_0−T−sum_(i=2)^(k−1)b_i` a zero. The union of those two discrete sets cannot exhaust R. Thus all the other factors can be made nonzero with the prescribed sum, and the preceding fibre proof gives `||n_k(u_0)||>0` at that arbitrary u_0.

For the quartet packet and k=2, the pointwise scope cannot be extended to every u: evenness of a_h gives

\[
\partial_u\Psi_2(0,y)=\tfrac12\bigl(a_h'(y)a_h(-y)+a_h(y)a_h'(-y)\bigr)=0.
\]

Also m_2 is even, so `m_2'(0)=0` and `n_2(0)=0` exactly. This preserves the actual zero fibre while proving positive total relative energy. No Gaussian comparison, bounded score, or assumed lower bound for the positive residual is used.

### The full finite normal matrix is strictly positive for k≥3

**Theorem.** Keep any finite linearly independent S-independent relative polynomial frame from section4. For the actual arithmetic amplitude, every integer k≥3 and every real u,

\[
\boxed{\mathcal N(u)=N_u^*N_u>0.}
\]

This is strict positivity of the entire finite matrix. It does not specify a positive lower bound uniform in u, degree, packet or frame.

**Proof.** Fix u and suppose `N_u c=0`. By the exact projection equation, `j_u'c=j_u d` with the finite coefficient vector `d=Gamma_u c`. Let `theta_c` and `theta_d` be the two corresponding relative polynomials evaluated at iy. Equality in the fibre Hilbert space gives

\[
(\partial_u\Psi_k)\theta_c=\Psi_k\theta_d.
\]

Both sides are smooth functions of y; equality almost everywhere therefore implies equality everywhere. For each unremoved real-line zero T of a_h, consider the affine relative hyperplane `t_1=u/k+y_1=T`. It has dimension k−2≥1. On it, each of the other original coordinates is a nonconstant affine function of the remaining independent y variables. Consequently the points where any of the other amplitude factors vanish form a countable union of proper affine hyperplanes of measure zero in this hyperplane. Its complement is nonempty and dense, and it is open near each of its points because the zero set is discrete.

At any such point p, use the same transverse path `t_1=T+delta`, `t_k=b_k−delta`, with other coordinates fixed. The expansion from the preceding theorem gives left-hand leading term

\[
\frac\ell k c_T A\,\theta_c(p)\,\delta^{\ell-1},
\]

where `c_T=a_h^(ell)(T)/ell!` and A is the nonzero product of the other amplitudes. The right side has order at least ell, since theta_d is a polynomial. Thus `theta_c(p)=0`. It vanishes on the dense subset just described and hence on the entire real hyperplane. A complex polynomial vanishing there has factor `y_1−(T−u/k)`: divide in y_1 and note that the remainder polynomial in the other real variables vanishes identically.

Hardy's infinitely many critical zeros leave infinitely many distinct T after the finite packet. Thus theta_c is divisible by infinitely many distinct parallel linear factors. Its degree in y_1 is finite, so it must be the zero polynomial. Independence of the relative frame gives c=0. This proves that N_u is injective. For every nonzero vector c its Gram quadratic form is `||N_u c||²>0`, proving the displayed strict positive definiteness with all finite directions retained.

Under an arbitrary smooth invertible frame C, the exact congruence `mathcal N^C=C*mathcal N C` preserves this result. The k=2 quartet fibre u=0 remains outside the theorem: there `j_0'=0` for every S-independent relative frame and therefore `mathcal N(0)=0` exactly.

### Two factors and every original finite polynomial direction

The independent review supplies the following stronger two-factor scope. Write `Z_h={T in R:a_h(T)=0}`, an infinite discrete and therefore countable set. If `u notin Z_h+Z_h`, then for every T in Z_h the partner `a_h(u−T)` is nonzero. The same smooth equality `Psi' theta_c=Psi theta_d` and the full-order transverse expansion force the univariate polynomial theta_c to vanish at `y_1=T−u/2` for every T. These are infinitely many distinct points, so theta_c=0 and c=0. Consequently

\[
\mathcal N_2(u)>0\quad(u\notin\mathcal Z_h+\mathcal Z_h).
\]

The exceptional sum set is countable. Thus the full finite normal matrix is positive definite almost everywhere for every k≥2, and everywhere for k≥3. In the quartet case, zero lies in the exceptional sum set and the proved zero matrix at u=0 remains.

For a nonzero actual source polynomial P in the declared finite relative frame, its vector coefficient polynomial c_P(u) is nonzero away from a finite set: one of its polynomial components is nonzero and has finitely many real roots. Therefore `c_P*mathcal N c_P>0` almost everywhere. Also `||N_uc_P||≤||j'_uc_P||`, and the latter is a polynomial multiple of differentiated Schwartz columns. This proves

\[
0<\int_{\mathbb R}c_P(u)^*\mathcal N(u)c_P(u)\,du<\infty.
\]

Both quadratic branches retain this strictness. The paired normal matrix is the invertible congruence of `diag(mathcal N(sqrt x),mathcal N(−sqrt x))/(2sqrt x)`, so it is positive definite for every x>0 at k≥3 and almost everywhere at k=2. The squared images of the countable exceptional set are countable. The exact gauge identity `N^C c_P^C=N c_P` proves equality of the original normal energies under all declared frame changes, with the transformed source coefficient image retained.

## 10. Cumulative TeX integration and independent branch-domain review

The complete source core and new branch-domain proof in `tex/sum_connection_stieltjes.tex`, FC.1–FC.20, were read independently at SHA-256 `b1aebc203b56a3c8e2e97dc0fa793a1ebda060b4c5e667ce1c9b4f33befae725`. No mathematical correction was found. In particular:

- The branch map M has the exact inverse in section7 above, giving the full positive H with no evenness assumption.
- Writing `K=diag(2sqrt x,−2sqrt x)` and `Gamma_b=diag(Gamma(sqrt x)/(2sqrt x),−Gamma(−sqrt x)/(2sqrt x))`, the paired connection is `A=M^(−1)Gamma_b M+M^(−1)M'`. Direct multiplication gives `M^(−1)M'=diag(0,1/(2x))` and `J=M^(−1)KM=[[0,2ix],[-2i,0]]` on the coefficient blocks. Thus `J²=4xI` and `J*HJ=4xH`, proving the exact factor4x in FC.15.
- The block density `D=diag(W_+,W_−)/(2sqrt x)` satisfies `Gamma_b*D+D Gamma_b=D'+D/(2x)`. The term `D/(2x)` is the derivative of the inverse Jacobian factor. Congruence by M gives `A*H+HA=H'+H/(2x)`, so subtracting `I/(4x)` from A gives the compatible density connection. These signs and constants are exact.
- On each branch, finite original norm and derivative energy imply ordinary coefficient H¹ near u=0 because W has positive upper/lower bounds and Gamma is bounded there. The branch coefficients therefore have finite one-sided limits. Their union has an L² weak derivative precisely when the limits coincide: otherwise integration by parts yields the nonzero jump times a delta distribution. This proves the full FC.18 joining condition and its converse; no condition at zero is required for the L² map alone.
- The original sum matrix and the transported derivative have commutator iI, conjugating the original `[Dsum,L_k]=−I`. The variable-frame terms commute with the branch scalar multiplication before conjugation, so none is discarded in this calculation.
- Under the stated even specialization, the paired energy reduces to both original Stieltjes measures. For `rho_k(x)=m(sqrt x)/sqrt x`, substitution gives `m'(u)=rho_k+2x rho_k'` and the exact radial drift `rho_k/(2x)` in FC.20, with the full normal integral retained.

The full new strict proofs from section9 were then appended, by this reviewer as author, as FC.21–FC.27. The combined file after that append has SHA-256 `639fc202b30a5504a6b280f0b8dd155daaa48d12f3e9da80fe9ac30c524c744a`. The preceding FC.1–FC.20 text was not edited. Authorship and independent review scopes are separate: the audit agent independently reviewed the new strict theorems and the parent reviews the final TeX extension; this reviewer does not call its own appended text an independent review.

**Audit conclusion:** the actual amplitude/Fisher equality, centred Jacobian, mass-retaining tensor identity, full relative matrix connection, normal form, gauge covariance and combined graph arithmetic jet all hold under the delivery's stated source hypotheses. The complete proofs above preserve their constants and domains. The two bounded presentation corrections and the additional symmetry scope for half-line decomposition have exact replacement maps. The actual arithmetic normal residual and full finite normal matrix also obey the strict theorems just proved. The scalar `1/k` identity is not transferred to the original finite Weil weight without the still-retained full matrix and interpolation comparison.
