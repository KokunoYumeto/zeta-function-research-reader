# The actual archimedean form on short-support primitives

<!-- original-zeta-reconstruction-start -->
**Original-zeta receiving calculation.** The working meromorphic function is the original Riemann zeta, with its full Gamma/endpoints multiplier and its full trivial-zero and pole divisor retained. [TF1–42](FAITHFUL_THETA_COMPLETION_RETURN.md) proves the original labelled theta inverse and the actual heat-image defect. [UZ1–53](FAITHFUL_UNCOMPLETED_ZETA_HEAT.md) proves every exceptional-point fibre, jet, original-zeta heat term and reflection orientation. [OZC1–48](ORIGINAL_ZETA_COMPACT_WEIL_RECONSTRUCTION.md) rederives the compact contour and interval operator directly from zeta, including the left-cutoff Gamma boundary, and specifies exactly which compensated pairing the bounds concern. [OZH1–49](ORIGINAL_ZETA_HEAT_CONTACT_RECONSTRUCTION.md) rederives the actual meromorphic heat, rational signed trace, compact-test domain, contact drift and full causal arithmetic variation. The raw full divisor and the compensated Weil receiver are linked by their displayed correction, not identified. In particular the fixed-test trivial-zero sum converges exactly at translations at least 1/32 and equals the earlier R term; at zero translation it requires the proved cutoff compensation. [OZK1–38](ORIGINAL_ZETA_CAUCHY_RECONSTRUCTION.md) reconstructs the original signed Cauchy trace, its full Gamma correction, resonant finite parts, every finite matrix and its index, and the complete local heat jets. Its invertible map retains the raw trace and correction separately. These complete receiving proofs govern the interpretation of the retained auxiliary calculations below.
<!-- original-zeta-reconstruction-end -->


This proof gives an explicit rational lower bound, an exact bilinear
representation of its positive remainder, and an exact localization
on primitive functions retaining all cross terms. It uses the original minus-sign
Mellin convention and HA13. No historical novelty claim is made for
short-support Weil positivity or for the endpoint-annihilating
differential operator.

## PS1. Original tests, correlations and the archimedean form

Let \(f,g\in C_c^\infty(\mathbb R;\mathbb C)\), and retain the conventions

\[
f^\#(u)=\overline{f(-u)},\qquad
h_{f,g}=f^\#*g,\qquad
M_f(s)=\int_{\mathbb R}f(u)e^{-(s-1/2)u}\,du.
\tag{PS1}
\]

The inner product is \(\langle f,g\rangle=\int\overline{f(u)}g(u)\,du\), conjugate-linear
in its first argument. Define the translation \(\tau_a f(u)=f(u-a)\).
Changing variables in the convolution gives

\[
h_{f,g}(a)=\langle\tau_a f,g\rangle,
\quad h_{f,g}(-a)=\langle f,\tau_a g\rangle,
\quad h_{f,g}(0)=\langle f,g\rangle.
\tag{PS2}
\]

For the diagonal correlation, \(h(-a)=\overline{h(a)}\) and
\(|h(a)|\le h(0)=\|f\|^2\) by Cauchy–Schwarz. If the two functions
are supported in one interval of length \(\ell>0\), their correlation
vanishes outside \([-\ell,\ell]\). This statement does not depend on
the center of the interval.

Use precisely the archimedean functional proved in [HA13, complete public proof](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/76f421965914beb133df797835f940849844dc4f/workbenches/splitzero-tandem/branches/tau-zero-prime-positivity/HEAT_CAUCHY_ARITHMETIC_DERIVATION.md):

\[
\begin{aligned}
\mathcal A(f,g):=A_\infty(h_{f,g})
={}&-(\gamma+\log\pi)\langle f,g\rangle\\
&+\int_0^\infty
\frac{e^{-x}\langle f,g\rangle
-\tfrac12e^{-x/4}(h_{f,g}(x/2)+h_{f,g}(-x/2))}
{1-e^{-x}}\,dx.
\end{aligned}
\tag{PS3}
\]

Here \(\gamma\) is Euler's constant. This is a Hermitian sesquilinear
form on the stated smooth test space. The cancellation of the
numerator at \(x=0\) makes the integral converge; smoothness suffices.
No sign convention for an archimedean geometric distribution is
substituted for PS3: its sign is the archimedean term appearing
positively in the original spectral explicit formula.

## PS2. Exact bilinear short-support identity

For \(\ell>0\), set

\[
\begin{aligned}
C(\ell)={}&-\gamma-\log\pi
-\log(1-e^{-2\ell})\\
&+\int_0^{2\ell}\frac{e^{-x}-e^{-x/4}}{1-e^{-x}}\,dx,
\qquad
w(x)=\frac{e^{-x/4}}{1-e^{-x}}.
\end{aligned}
\tag{PS4}
\]

For \(f,g\) supported in one interval of length \(\ell\), the following
is an equality, not merely an inequality:

\[
\boxed{\mathcal A(f,g)=C(\ell)\langle f,g\rangle
+\frac12\int_0^{2\ell}w(x)
\langle\tau_{x/2}f-f,\tau_{x/2}g-g\rangle\,dx.}
\tag{PS5}
\]

To prove it, split PS3 at \(2\ell\). Above that point the two
correlations vanish, while

\[
\int_{2\ell}^\infty\frac{e^{-x}}{1-e^{-x}}\,dx
=-\log(1-e^{-2\ell}).
\]

Below that point use the unitary translation identity

\[
\langle\tau_a f-f,\tau_a g-g\rangle
=2\langle f,g\rangle-h_{f,g}(a)-h_{f,g}(-a).
\]

Its substitution separates the remaining constant multiple of
\(\langle f,g\rangle\), which is exactly the integral in PS4, and leaves the
positive-weight integral in PS5. The latter converges at zero:
\(\|\tau_a f-f\|\le |a|\|f'\|\), obtained by the fundamental theorem
of calculus and Minkowski's inequality. Thus the bilinear
integrand is \(O(x^2)w(x)=O(x)\) there.

In particular, taking the diagonal gives

\[
\mathcal A(f,f)=C(\ell)\|f\|^2
+\frac12\int_0^{2\ell}w(x)
\|\tau_{x/2}f-f\|^2\,dx
\ge C(\ell)\|f\|^2.
\tag{PS6}
\]

The remainder is explicitly a Gram integral of translation
differences. Consequently the same local lower bound holds as
a matrix inequality on every finite family supported in that
one common interval. The equality also proves directly that the
proposed \(C(\ell)\) has the correct tail sign and every factor of
two from the original HA13 coordinate.

## PS3. The rational lower bound 55/192

For \(x>0\) put \(q=e^{-x/4}\in(0,1)\). The integrand in PS4 is

\[
\frac{e^{-x}-e^{-x/4}}{1-e^{-x}}
=-\frac{q(1+q+q^2)}{1+q+q^2+q^3}\ge-\frac34.
\tag{PS7}
\]

The final inequality is equivalent to \(q+q^2+q^3\le3\), which holds
term by term. Its limit at zero is \(-3/4\), so the integral has no
unaccounted singular endpoint. Therefore it is at least
\(-3\ell/2\).

The elementary inequalities used next can all be retained
without decimal approximations. First \(\gamma\le1\): the decreasing
sequence \(H_n-\log n\) has limit \(\gamma\) and starts at one. Its
decrease follows from \(\log(1+1/n)\ge1/(n+1)\), by integration of
\(1/x\) on \([1,1+1/n]\). Its lower bound follows by comparing the
harmonic sum with the same integral, so this passage to the
limit is valid. Second \(\pi\le4\), for example from containment of
the unit disc in the square of side two. Third,

\[
\log x\ge\frac{2(x-1)}{x+1}\quad(x\ge1),
\]

because the derivative of their difference is
\((x-1)^2/[x(x+1)^2]\ge0\) and the difference is zero at one. At
\(x=2\) this yields \(\log2\ge2/3\), hence \(\log4\ge4/3\).

Finally \(1-e^{-2\ell}\le2\ell\) follows by integrating \(e^{-x}\le1\).
Combining all these inequalities in the correct direction gives

\[
\begin{aligned}
C(\ell)
&\ge-1-\log4-\log(2\ell)-\frac32\ell\\
&=-1+\log\frac1{8\ell}-\frac32\ell\\
&\ge-1+\log4-\frac3{64}
\ge\frac13-\frac3{64}=\frac{55}{192}
\qquad(0<\ell\le1/32).
\end{aligned}
\tag{PS8}
\]

Thus the actual archimedean form satisfies the proved bound

\[
\boxed{\mathcal A(f,f)\ge\frac{55}{192}\|f\|^2}
\tag{PS9}
\]

for any smooth \(f\) supported in an interval of length at most
\(1/32\). No endpoint-vanishing condition is required for this
archimedean assertion. A smooth function supported in a
zero-length interval is zero and satisfies it trivially.

## PS4. Endpoint-annihilating primitives and the whole Weil form

Retain the original differential operator

\[
T=\frac{d^2}{du^2}-\frac14,
\qquad f=Tg,\quad g\in C_c^\infty(\mathbb R).
\tag{PS10}
\]

Two integrations by parts, with no boundary terms, give

\[
M_{Tg}(s)=\bigl((s-1/2)^2-1/4\bigr)M_g(s)
=s(s-1)M_g(s).
\tag{PS11}
\]

Thus both endpoint values vanish exactly, while \(T\) does not
enlarge the support. Its squared norm, with complex-valued
functions permitted, is exactly

\[
\begin{aligned}
\|Tg\|^2
&=\|g''\|^2-\frac12\Re\langle g'',g\rangle
+\frac1{16}\|g\|^2\\
&=\|g''\|^2+\frac12\|g'\|^2+\frac1{16}\|g\|^2.
\end{aligned}
\tag{PS12}
\]

For a compact test \(f\) write its original reflected Weil form
as

\[
\mathcal Q(f,g)=\sum_\rho m_\rho
\overline{M_f(\rho^\#)}M_g(\rho)
=M_{f^\#*g}(0)+M_{f^\#*g}(1)
+\mathcal A(f,g)-P_{\rm fin}(f^\#*g).
\tag{PS13}
\]

The complete underlying formula is [SZW24–26 and SZW33–38](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/76f421965914beb133df797835f940849844dc4f/workbenches/splitzero-tandem/branches/tau-zero-prime-positivity/SUPPORTED_ZERO_PRIME_WEIL_DERIVATION.md).
The sum converges by the original strip zero count and rapid
Mellin decay; the displayed identity is SZW25 with its original
constants. Its two endpoint values for \(f=Tg\) are zero by PS11
and the convolution identity. If \(g\) is supported in an
interval of length \(\ell\le1/32\), the correlation of \(Tg\) is
supported in \([-\ell,\ell]\). Since \(\ell<\log2\), every prime term
\(h(\pm\log n)\) with \(n\ge2\) vanishes exactly. Consequently the whole
spectral form in PS13, with endpoints retained and evaluated,
equals the archimedean form and satisfies

\[
\boxed{\mathcal Q(Tg,Tg)\ge\frac{55}{192}
\left(\|g''\|^2+\frac12\|g'\|^2
+\frac1{16}\|g\|^2\right).}
\tag{PS14}
\]

The inequality is strict for \(g\ne0\), since its right side is
strictly positive. This proves the proposed primitive estimate
with the exact positive sign in the original full spectral
form. In the support-resolved SZW identity the endpoint
amplitude in every boundary coordinate is zero for these tests;
the labels themselves remain present. No support element is
identified with a scalar zero by this computation.

For precision, every compact smooth test with both endpoint
moments zero does have a unique compact smooth primitive in
this sense. An explicit inverse, preserving the containing
support interval, is

\[
g(u)=-\int_{\mathbb R}e^{-|u-v|/2}f(v)\,dv.
\tag{PS15}
\]

The kernel \(-e^{-|u|/2}\) has first derivative jump one and
satisfies \(TK=\delta_0\) in distributions. Thus \(Tg=f\), and convolution
with smooth compact \(f\) gives a smooth function. If
\(\operatorname{supp}f\subset[a,b]\), then for \(u>b\) its value is
\(-e^{-u/2}M_f(0)=0\), and for \(u<a\) it is
\(-e^{u/2}M_f(1)=0\). Hence \(\operatorname{supp}g\subset[a,b]\).
The difference of two compact primitives solves the homogeneous
equation and is a linear combination of \(e^{u/2}\) and \(e^{-u/2}\);
compact support forces both coefficients to vanish. This proves
the stated exact inverse and uniqueness, not only existence of
some endpoint-null images of \(T\).

## PS5. Exact bilinear localization of the primitive

Let \(g\) now be an arbitrary compact smooth function. Choose a
finite smooth partition of unity \(\chi_j\) on a neighborhood of
its support, with each \(\chi_j\) supported in an interval \(I_j\)
of length at most \(1/32\). Such a partition follows by covering
the compact support by finitely many shorter open intervals,
choosing nonnegative bumps positive on a smaller cover, and
dividing by their positive sum on a neighborhood of the
support; an auxiliary cutoff inside that neighborhood makes
each resulting function compact smooth. Put

\[
g_j=\chi_jg,\qquad f_j=Tg_j.
\tag{PS16}
\]

These formulas retain the derivatives of the partition:

\[
f_j=\chi_jTg+2\chi_j'g'+\chi_j''g,
\qquad g=\sum_jg_j,\qquad Tg=\sum_jf_j.
\tag{PS17}
\]

The last equality uses \(\sum_j\chi_j=1\), \(\sum_j\chi_j'=\sum_j\chi_j''=0\) near
\(\operatorname{supp}g\); outside that support all the derivatives of \(g\)
vanish. It is therefore an equality of the original tests, not
a replacement by the functions \(\chi_jTg\) alone.

Each piece has both endpoint moments zero and the stated short
support. For the exact finite Hermitian matrix

\[
q_{jk}=\mathcal Q(f_j,f_k),
\]

sesquilinearity and the finite convolution expansion give

\[
\begin{aligned}
\mathcal Q(Tg,Tg)
&=\sum_{j,k}q_{jk}
=\sum_j q_{jj}+2\Re\sum_{j<k}q_{jk},\\
q_{jk}
&=\mathcal A(f_j,f_k)-P_{\rm fin}(f_j^\#*f_k),\\
q_{jj}
&\ge\frac{55}{192}
\left(\|g_j''\|^2+\frac12\|g_j'\|^2
+\frac1{16}\|g_j\|^2\right).
\end{aligned}
\tag{PS18}
\]

The endpoint terms vanish also for each cross pair, since both
primitive factors have their two endpoint moments zero. The
prime term vanishes for each diagonal, but is retained in every
off-diagonal entry. The exact support relation is

\[
\operatorname{supp}(f_j^\#*f_k)\subset I_k-I_j.
\tag{PS19}
\]

Thus distinct windows can have nonzero prime correlations even
though each window separately has none. PS18 does not infer a
sign for the entire matrix from the positive diagonal terms.

The bilinear primitive and convolution maps also retain their
exact coefficients:

\[
\langle Tg_j,Tg_k\rangle
=\langle g_j'',g_k''\rangle
+\frac12\langle g_j',g_k'\rangle
+\frac1{16}\langle g_j,g_k\rangle,
\tag{PS20}
\]

\[
(Tg_j)^\#*(Tg_k)
=T^2(g_j^\#*g_k),\qquad
T^2=D^4-\frac12D^2+\frac1{16}.
\tag{PS21}
\]

For PS20 integrate the two cross terms by parts separately.
For PS21 use that \(T\) has real even coefficients, commutes with
reflection, and may act on either factor of a smooth compact
convolution. Its Mellin multiplier is correspondingly
\(s^2(s-1)^2\). Equations PS17–PS21 are the exact bilinear
localization; no partition-derivative or inter-window term is
removed.

When several pieces are supported in the same one interval of
length \(\ell\le1/32\), PS5 applies to their whole Gram matrix,
not just its diagonal. For separated windows the exact entries
remain those in PS18–PS19; they are not covered by a common
short-interval lower bound. This specifies precisely the local
estimate and the remaining arithmetic interactions.

## PS6. Original-source reading and comparison

The original author source used for the operator comparison is:
Alain Connes and Caterina Consani, [*Weil positivity and Trace formula: the archimedean place*, arXiv:2006.13771v1](https://arxiv.org/src/2006.13771v1),
`sources/weil/2006.13771v1/weil-compo.tex`.

Original file SHA256:
`B01D353B0423B6FEDEE373C3C33FE3678EEA733F62049810750F6C64EF20F3FC`.
Intact `2006.13771v1.tar` archive SHA256:
`771A004B70FB0C36CAE11351BD29CEC50B3DA13896BB1EF5015BBDD68BEADB6D`.

Actual reading coverage for this derivation:

- lines 95–139: original explicit-formula convention, endpoint
  vanishing, the stated local positivity and its historical
  attribution, and the introductory theorem;
- lines 663–842: Section `sectsupport`, including `boaskac`,
  `vanishing1`, `vanishing2`, `thmqkey1`, `Qprime`, `remQprime`
  and `qeasy`, with their proofs.

No PDF was read. The author archive remains intact. These
locators record bounded reading, not an exhaustive reading of
the paper. Its local operator method and small-support
positivity are prior mathematical work; the elementary bound
PS8 is derived directly from the programme's proved HA13
formula and does not claim to replace those stronger results.

The coordinate and sign map to the source operator is explicit.
Under \(u=\log\rho\), its
\(Q_{\mathrm{CC}}=-(\rho\partial_\rho)^2+1/4\) becomes \(-D^2+1/4=-T\).
Thus applying our \(T\) to a primitive corresponds to applying
their \(Q_{\mathrm{CC}}\) to the negative of that primitive. On a convolution
square the two minus signs cancel, giving exactly PS21. The
source's support-preserving endpoint-vanishing lemma therefore
has the same receiving condition, with this sign retained.
PS15 is an independent additive-coordinate inverse verifying
that comparison directly.

The symbol \(\tau\) in that author's archimedean distribution is a
source-specific distribution; it is not identified with the
programme's unsupported element. The present proof uses HA13,
PS1 and PS3 to fix its arithmetic sign and all constants.

The concluding bound is an established statement about the
short-support diagonal pieces and the common-window matrices.
The exact cross-window form in PS18 remains in the global
calculation. Nothing here assigns its sign or proves RH from
the local estimate alone.


## Proved compact-interval and finite-translation bounds

The complete [compact-interval proof](FIRST_PRIME_FULL_WEIL_COERCIVITY.md), FC1–43, proves full Weil coercivity with constant 11509/600000 through support diameter 19/25, including prime 2 and both original endpoint moments. [FW1–21](FIRST_PRIME_WINDOW_BOUND.md) proves the every-rank matrix bound for centre diameter 583/800 and a strict two-test margin through the next prime gap. The same unchanged test now satisfies its required strict correlation bound for every positive translation through log 256, by [FP1–25](FINITE_PRIME_WINDOW_EXTENSION.md) and the complete [rational prime-power certificate, FPC1–14](FINITE_PRIME_WINDOW_COEFFICIENT_CERTIFICATE.md). [PT1–40](PRIME_TWO_HEAT_TAIL_DERIVATION.md) calculates the surviving mixed channel and proves a strictly negative full actual right heat derivative on the stated short interval after the prime-2 atom ends. These are exact portions of the original bound, retaining supported zero and every original arithmetic coefficient. The uniform inequality beyond log 256 remains unproved.
