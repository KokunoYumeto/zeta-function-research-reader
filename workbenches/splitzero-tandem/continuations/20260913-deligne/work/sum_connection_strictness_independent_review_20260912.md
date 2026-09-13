# Independent review of actual sum-connection strictness

Date: 2026-09-12. This bounded review covers Section 9 of
`work/sum_connection_analytic_audit_20260912.md`, including its appended
full finite normal-matrix theorem. It also reads the exact coordinate,
amplitude, projection and energy definitions in Sections 2–3 of
`sources/web_sum_connection_delivery/Tau_Sum_Connection_Control/RESEARCH_NOTE.md`.
The preceding regularity and finite-frame arguments in the audit were
read to check the dependencies. No TeX or main file was edited, no
literature search or Lean run was made, and no implementation-mirroring
test was substituted for the proof.

Historical reviewed whole-audit SHA256 (before the parent's later additions):
`e76330f4bb3e6b9b8ed1ec73cb37c865923819d266a558053551d3beaf93ff93`.

Reviewed delivery SHA256:
`c24b120fdd6ba6549e7f63dd9f2ae269e51123fe0e097b7b976f842bba3729d9`.

The complete new subsection FC.21–FC.27 of
`tex/sum_connection_stieltjes.tex` was subsequently read at whole-file
SHA256
`639fc202b30a5504a6b280f0b8dd155daaa48d12f3e9da80fe9ac30c524c744a`.
Its required exact frame and paired-matrix definitions FC.5–FC.6 and
FC.14 were also checked. This review does not replace the root's separate
review of all preceding FC.1–FC.20.

**Result: both the scalar strictness theorem and the full finite-matrix
theorem pass. No mathematical correction is required.** The proof keeps
the multiplicity, the actual Plancherel amplitude, the factor 1/k, the
original mass, the relative coordinates, and the exceptional k=2 fibre.

## 1. Exact objects and hypotheses used

In this source the amplitude is

\[
 a_h(t)=\frac{(g/h)(1/2+it)}{\sqrt{2\pi}},\quad
 t_i=u/k+y_i,\quad y_k=-\sum_{i<k}y_i,\quad
 \Psi_k(u,y)=\prod_{i=1}^k a_h(t_i).
\]

The entire canceled quotient g/h is nonzero, and the previously proved
source theorem makes this amplitude and all its derivatives Schwartz.
Its real zero set E is discrete and countable. The explicitly identified
Hardy theorem leaves infinitely many distinct real zeros after any finite
full packet. Each has a finite positive order. This review uses that
identified literature theorem and does not claim a new proof of Hardy.

The fibre mass m_k is positive and smooth for every u. Its positivity is
an integral statement: the product density is positive off a countable
union of proper affine hyperplanes. Its derivative is justified by the
Schwartz bounds. Thus m_k'/(2m_k) is finite at every fixed u and bounded
on each sufficiently small compact u interval. No global bound on this
ratio or on a logarithmic score is required.

The scalar normal residual is the smooth representative

\[
 n_k(u,y)=\partial_u\Psi_k(u,y)
             -\frac{m_k'(u)}{2m_k(u)}\Psi_k(u,y),
 \qquad
 \partial_u\Psi_k=\frac1k\sum_i a_h'(t_i)\prod_{j\ne i}a_h(t_j).
\]

The fixed-phase packet hypothesis is retained for the Fisher equality
and this real projection coefficient. For a finite relative polynomial
frame, the domain consists of polynomials independent of S, with
independence taken in C[z_1,...,z_(k-1)] after z_k=-sum_(i<k) z_i.
Thus theta_c(iy) is a polynomial in the independent real variables y,
and a zero polynomial implies a zero coefficient vector c.

## 2. Multiplicity and the transverse expansion

Fix a real zero T of order ell and write
a_h(T+delta)=c_T delta^ell+O(delta^(ell+1)), where
c_T=a_h^(ell)(T)/ell! is nonzero. Its derivative is
ell c_T delta^(ell-1)+O(delta^ell). Choose other coordinates b_i away
from E, and put u_0=T+sum_(i=2)^k b_i. The path

\[
 t_1=T+\delta,\qquad t_i=b_i\ (2\le i<k),\qquad
 t_k=b_k-\delta
\]

keeps the original sum u_0 fixed. It moves the relative point by
y_1 -> y_1+delta, while y_i for 2<=i<k stay fixed. The derivative
partial_u being evaluated along this path still means differentiation
at fixed relative coordinates, hence it remains the displayed (1/k)
sum of k product derivatives. It is not the derivative along the path.

With A=product_(i=2)^k a_h(b_i), the i=1 summand has leading term
(ell/k)c_T A delta^(ell-1). Every other summand retains the factor
a_h(T+delta), and its remaining factors and derivatives stay bounded;
it therefore has order at least ell. Consequently

\[
 \Psi_k=c_TA\delta^\ell+O(\delta^{\ell+1}),\qquad
 \partial_u\Psi_k=\frac\ell k c_TA\delta^{\ell-1}
                         +O(\delta^\ell).
\]

The projection term is only O(delta^ell), so it cannot cancel this
nonzero leading coefficient. This argument works for every positive
multiplicity. For ell>1 it uses nearby nonzero delta, not the value at
the zero itself. For ell=1 it already gives a nonzero value at delta=0.

## 3. Pointwise values, fibre measure, and integration in u

The preceding expansion yields an actual point where the smooth
representative of n_k is nonzero. Continuity then supplies a relative
ball on which its modulus has a strictly positive lower bound. That ball
has positive (k-1)-dimensional Lebesgue measure. Thus a nonzero value
on a path is not being mistaken for positive fibre norm: the additional
continuity argument supplies the required full-dimensional set.

Schwartz domination on compact u intervals implies that Psi_k and its
u derivative are continuous as L2(dy)-valued functions. Multiplication
by the smooth local scalar m_k'/(2m_k) preserves that continuity. Hence
u -> ||n_k(u)||^2 is continuous near the chosen u_0 and positive on an
interval about it. The integrated residual is therefore strictly
positive. Its finiteness was already established by the exact orthogonal
energy identity. Subtracting this positive finite term gives exactly

\[
 \mathcal I_{h,k}
       <\frac{\mu_h^{k-1}}k\mathcal I_h.
\]

For k>=3 and a prescribed u_0, choose b_3,...,b_(k-1) outside E.
Then choose b_2 outside E and outside
u_0-T-sum_(i=3)^(k-1)b_i-E. The two excluded sets are discrete and
cannot exhaust R. This makes the final b_k nonzero as well. The argument
therefore gives ||n_k(u_0)||>0 for every prescribed real u_0.

Under quartet amplitude evenness, at k=2 the two terms in
partial_u Psi_2(0,y) cancel exactly, and m_2'(0)=0. Thus n_2(0)=0.
The same cancellation holds more generally for either definite amplitude
parity a_h(-t)=epsilon a_h(t), epsilon=+1 or -1; the parity of its
derivative is -epsilon. This observation does not enlarge the stated
packet hypothesis or discard the actual zero fibre.

## 4. The complete finite normal matrix

Fix u and k>=3. If N_u c=0 then j_u'c=j_u d with
d=Gamma_u c, a finite vector at this fixed u. Thus

\[
 (\partial_u\Psi_k)\theta_c(iy)=\Psi_k\theta_d(iy)
\]

in L2(dy). Both sides are smooth. A continuous function that vanishes
almost everywhere must vanish everywhere, since any nonzero value
would give a ball of positive measure where its modulus is bounded away
from zero. Hence this is a pointwise identity of the displayed smooth
representatives; no point evaluation of an arbitrary L2 class is used.

For each unremoved zero T, the relative hyperplane
y_1=T-u/k has dimension k-2>=1. Each other original t_i is a
nonconstant affine function on it. The zeros of their amplitude factors
form a countable union of proper affine subspaces of measure zero in
this hyperplane. The complement is dense, and is open near each of its
points because the zero set E is discrete.

At any such point p, multiply the exact transverse expansion of
Section 2 by the Taylor expansion of theta_c. Its leading coefficient
on the left is

\[
 \frac\ell k c_T A\theta_c(ip)
\]

at order ell-1. The right side has order at least ell. Thus theta_c(ip)
vanishes. Continuity gives its vanishing on the whole real hyperplane.
Division of the polynomial theta_c(iy) in y_1 leaves a remainder in
the other variables; that remainder vanishes on all real points and is
the zero complex polynomial. Therefore y_1-(T-u/k) divides it. In
the original relative z coordinates the corresponding factor is
z_1-i(T-u/k), through the invertible map z_i=i y_i.

There are infinitely many distinct T, while the degree in y_1 is
finite. These infinitely many distinct factors force theta_c to be the
zero polynomial, hence c=0. N_u is injective. For every nonzero c,
c*mathcal N(u)c=||N_uc||^2>0. This proves strict positivity of the
entire finite matrix. The argument does not supply a uniform positive
eigenvalue bound in u, degree, packet, or choice of frame. The previously
proved congruence C*mathcal N C transports the result under every
specified smooth invertible frame change.

## 5. Additional exact k=2 consequence supplied to the parent

There is a further pointwise statement compatible with the exceptional
quartet fibre. Since E is countable, E+E is countable. Fix u outside
E+E. For every T in E, the other coordinate u-T lies outside E.
If N_2(u)c=0, the same transverse argument gives

\[
 \theta_c(i(T-u/2))=0
\]

for every one of the infinitely many distinct zeros T. Here theta_c
is a univariate polynomial. It must vanish identically, proving
mathcal N_2(u)>0 for all u outside E+E, and in particular for almost
every real u. This additional theorem was independently derived in the
review and sent to the parent. The reviewed Markdown source hash above
does not contain this added paragraph; the subsequently reviewed TeX
does contain it, with its full proof, in FC.24. Under quartet symmetry E=-E, so
0 belongs to E+E and the exact zero matrix at u=0 is retained.

## 6. The new actual-polynomial, two-branch and gauge consequences

The complete TeX extension FC.21–FC.27 retains the scalar and matrix
proofs above and adds three consequences in FC.26. Each is valid on its
stated domain.

First, a nonzero admitted source polynomial P has a unique expansion
sum theta_alpha(z) f_alpha(S) in the independent relative frame. At
least one f_alpha is a nonzero polynomial. The substitution S=k/2+iu
is an invertible affine polynomial map, so that coefficient remains a
nonzero polynomial in u. It has only finitely many real roots, and the
common zero set of the complete vector c_P is a subset of that finite
set. For almost every u the vector is nonzero and mathcal N(u) is
strictly positive definite. Hence its quadratic integrand is positive
almost everywhere. Its integral is finite because the orthogonal
projection is a contraction:

\[
 \|N_uc_P(u)\|\le\|j_u'c_P(u)\|.
\]

The expression on the right is the fibre norm of a finite sum of
products of a derivative of the Schwartz amplitude, a relative
polynomial, and a polynomial in u. It is Schwartz in the complete
(u,y) coordinates and square-integrable. This proves the exact
strict statement in FC.26, including both inequalities:

\[
 0<\int_{\mathbb R}c_P(u)^*\mathcal N(u)c_P(u)\,du<\infty.
\]

Second, FC.14 defines, for v=sqrt(x)>0,

\[
 \mathsf Q(x)=\mathsf M(x)^*
       \frac{\operatorname{diag}(\mathcal N(v),\mathcal N(-v))}{2v}
       \mathsf M(x),\qquad
 \mathsf M(x)=\begin{pmatrix}I&ivI\\ I&-ivI\end{pmatrix}.
\]

The matrix M is invertible for every x>0 and 1/(2v) is positive.
For k>=3 both diagonal blocks are positive definite at every such x,
which proves Q(x)>0. For k=2 they are positive definite whenever neither
v nor -v belongs to E+E. The exceptional positive x belong to the
image of that countable set under the square map, and therefore form
a countable null set. This proves the almost-everywhere assertion,
retaining both branches and their common original Jacobian factor.

Third, the gauge equations N^C=NC and c_P^C=C^(-1)c_P give
N^C c_P^C=Nc_P pointwise. Their squared norms and integrals are
identical. The congruence mathcal N^C=C*mathcal N C also retains
strict positive definiteness on every fibre where it holds. No
polynomial or global growth property is required of C^(-1)c_P:
its domain is precisely the stated image of the original admitted
coefficient vector, and its normal energy equals the original finite
energy. Thus no domain enlargement is hidden in the gauge conclusion.

Finally FC.27 correctly retains the quartet k=2 fibre u=0. The original
S-independent frame has j_0'=0 because partial_u Psi_2(0,y)=0, hence
N_0=0 and mathcal N(0)=0. This is consistent with every almost-everywhere
and integrated assertion above.

## Scope conclusion

The reviewed scalar and matrix strictness proofs are valid for the
actual source-defined amplitude, with the stated packet and frame
hypotheses. Full zero orders and all positive-measure steps are retained.
The only external zero-existence input is the explicitly identified
Hardy theorem. No numerical evidence, bounded-score assumption, Gaussian
replacement, uniform matrix coercivity estimate, or inference to the
finite Weil defect is included in this review.
