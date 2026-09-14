# Independent density and nested-frame proof review

Date: 2026-09-12. This file is outside the published research tree.
Scope: polynomial density under an exponential moment, explicit Fourier
uniqueness, the actual fixed-sum fibre multiplier, and limits of nested
relative projections on fixed source polynomials. No published TeX,
build, stage, or release file was edited. The derivation below is
independent; Section 8 records the completed, exact-hash content audit
of the final companion proof files.

## 1. Polynomial density for a finite positive Borel measure

Let mu be a finite positive Borel measure on R^r, r>=1, such that

\[
 \int e^{\varepsilon\|y\|_1}\,d\mu(y)<\infty
 \quad\text{for some }\varepsilon>0.
\]

Every polynomial belongs to L2(mu), since each fixed power of ||y||_1
is bounded by a constant times this exponential. Suppose f in L2(mu)
is orthogonal to every polynomial, using an inner product antilinear
in its first argument. Define the finite complex measure
nu=conjugate(f) mu. Cauchy–Schwarz gives the exact stronger bound

\[
 \int e^{(\varepsilon/2)\|y\|_1}\,d|\nu|(y)
 \le\|f\|_{L^2(\mu)}
       \left(\int e^{\varepsilon\|y\|_1}\,d\mu(y)\right)^{1/2}
 <\infty.
\]

Put delta=epsilon/2. The Laplace transform

\[
 F(z)=\int e^{z\cdot y}\,d\nu(y)
\]

is holomorphic on the tube max_j |Re z_j|<delta. To justify the
derivatives directly, on any compact smaller tube its integrands and
all fixed derivatives are bounded by a polynomial in ||y||_1 times
e^(a||y||_1), with a<delta. Such a polynomial can be bounded by a
constant times e^((delta-a)||y||_1/2), so the preceding exponential
moment provides a single integrable majorant. Equivalently the local
exponential power series is absolutely dominated in a smaller polydisc,
which proves the holomorphic expansion without a formal interchange.

Every derivative at zero is the corresponding polynomial moment of nu,
and is zero by orthogonality. More explicitly, for max_j |z_j|<delta,
the sum of the absolute values of the exponential series is at most
e^(max_j |z_j| ||y||_1), so termwise integration gives F(z)=0.

For any real vector xi!=0, the function lambda -> F(-i lambda xi)
is holomorphic on the connected strip
|Im lambda|<delta/||xi||_infinity. It vanishes in a neighbourhood of
lambda=0 and hence on the strip by one-variable analytic continuation.
This continuation can be obtained along the segment from 0 to 1 by
overlapping Taylor discs: a disc on which the function vanishes forces
every Taylor coefficient at any interior overlap point to vanish, and
therefore propagates the zero function to the next disc. The compact
segment has a finite such chain. Thus F(-i xi)=0 for every xi. The
xi=0 case was the constant polynomial moment. Consequently the full
Fourier transform of the finite complex measure nu is zero.

## 2. Fourier uniqueness, proved by Gaussian convolution

This step does not assume a Fourier uniqueness theorem for measures.
For t>0 let

\[
 G_t(x)=(4\pi t)^{-r/2}e^{-\|x\|_2^2/(4t)}.
\]

Its exact integral representation is

\[
 G_t(x)=(2\pi)^{-r}\int_{\mathbb R^r}
              e^{i\xi\cdot x}e^{-t\|\xi\|_2^2}\,d\xi.
\]

For an elementary verification in one coordinate, differentiate
I(b)=integral exp(-t xi^2) cos(b xi) dxi under its Gaussian majorant.
Integration by parts gives I'(b)=-(b/(2t))I(b), while the Gaussian
integral at zero is sqrt(pi/t). The latter follows by squaring the
positive integral and using planar polar coordinates. Solving this
scalar differential equation gives I(b)=sqrt(pi/t)exp(-b^2/(4t));
the sine integral is zero by oddness. Taking the product over all r
coordinates proves the displayed formula with every constant.

Finiteness of |nu| and integrability of exp(-t||xi||^2) justify Fubini.
Hence, pointwise for every x,

\[
 (G_t*\nu)(x)
  =(2\pi)^{-r}\int e^{i\xi\cdot x}e^{-t\|\xi\|_2^2}
                      \widehat\nu(\xi)\,d\xi=0.
\]

For phi continuous with compact support, Fubini and evenness of G_t
therefore give integral (phi*G_t) dnu=0. The functions phi*G_t converge
uniformly on R^r to phi. Indeed uniform continuity controls the part
|z|<eta of the convolution difference, and the remaining part is bounded
by 2||phi||_infinity integral_(|z|>=eta) G_t(z) dz, which tends to zero
by the explicit Gaussian change of variables z=sqrt(t)w. As nu is
finite, it follows that integral phi dnu=0 for every such phi.

Here is also an explicit measure-separation argument for the last step.
For each coordinate j, there are at most countably many t with
|nu|({y:y_j=t})>0, because those hyperplanes are disjoint and |nu| is
finite. Choose a countable dense set of allowed endpoints avoiding them.
Every bounded half-open box with such endpoints has |nu|-null boundary.
Products of continuous one-variable cutoff functions approximate its
indicator pointwise off the boundary, remain bounded by one and have
compact support. Dominated convergence then gives nu(B)=0 for all these
boxes. They form a generating intersection-stable family of Borel sets,
after adjoining R^r and the empty set. Also nu(R^r)=0 by the zero
constant moment. The zero sets of the finite complex measure form a
Dynkin system: complement and countable disjoint union preserve zero
because total mass is zero and the measure is countably additive.
The elementary pi-lambda argument therefore gives nu(A)=0 for every
Borel set A. Thus nu=0.

Since nu=conjugate(f)mu, this implies f=0 mu-almost everywhere. For
example, its real and imaginary parts integrated on their positive and
negative level sets force each part to vanish. The orthogonal complement
of the polynomials is therefore zero, proving their density in L2(mu).
The zero-measure case is immediate. This theorem does not assert that
the literal monomial Gram matrices are invertible for an arbitrary mu:
mu might be supported on a polynomial zero set. Actual-fibre positivity
below supplies that stronger conclusion in the application.

## 3. The actual arithmetic fibre has the required exponential moment

Retain a_h^SC(t)=(g/h)(1/2+it)/sqrt(2pi) and
w_h(t)=|a_h^SC(t)|^2. Schwartz decay alone would not imply an
exponential moment. The existing Gamma-reference proof supplies the
stronger actual estimate: for every 0<b<pi/2 there is a finite
C_(h,b) such that

\[
 w_h(t)\le C_{h,b}e^{-b|t|}\quad(t\in\mathbb R).
\]

To see the constants' scope, the beta-contour proof gives a Gamma-square
bound at every rate below pi/2 on the original t scale. The exact
theta multiplier contains a polynomial factor and the zeta factor,
whose proved critical-line bound is polynomial. Choose an intermediate
rate strictly larger than b to absorb these polynomial factors. Monic
h has a power lower bound on the tail; on the remaining compact interval
the quotient is its bounded entire canceled germ. This proves the stated
global estimate with h and b retained in the constant. It also includes
h=1, without imposing a probability-mass convention.

For k>=2, u fixed, and r=k-1, keep the original density

\[
 d\mu_u(y)=|\Psi_k(u,y)|^2dy
   =\prod_{i=1}^k w_h(t_i)dy,\quad
 t_i=u/k+y_i\ (i<k),\quad t_k=u/k-\sum_{i<k}y_i.
\]

All k factors remain in this measure. For 0<epsilon<b the upper bound
is obtained from sum_i |t_i|>=sum_(i<k)|y_i|-(k-1)|u|/k:

\[
 \int e^{\epsilon\|y\|_1}\,d\mu_u(y)
 \le C_{h,b}^{\,k} e^{b(k-1)|u|/k}
                \left(\frac2{b-\epsilon}\right)^{k-1}<\infty.
\]

Each factor a_h^SC is a nonzero analytic function on the real axis with
a discrete zero set. At a fixed sum u each t_i is a nonconstant affine
function of the independent relative variables. Its inverse zero set is
a countable union of proper affine hyperplanes, of Lebesgue measure
zero. The finite union over the k factors is still null. Consequently
Psi_k(u,y) is nonzero for almost every y, for **every** u, including an
exceptional sum fibre where its u derivative might vanish identically.

## 4. The exact onto multiplier and full nested projections

Multiplication by the original amplitude is the Hilbert isometry

\[
 U_u:L^2(\mu_u)\longrightarrow L^2(dy),\qquad
             f\longmapsto\Psi_k(u,\cdot)f.
\]

For any F in L2(dy), define f=F/Psi_k off the null zero set and give
it zero values on that set. Then integral |f|^2 dmu_u=integral |F|^2dy,
and U_u f=F almost everywhere. This proves onto-ness even though the
pointwise division can be unbounded near zeros. It is a map of the
specified weighted L2 spaces, not a bounded reciprocal-multiplier
assertion in the unweighted space.

The density theorem transports to density of Psi_k times all relative
polynomials in the full fibre L2(dy). The original relative coordinate
map z_i=i y_i is an invertible polynomial map retaining each phase
i^(|alpha|), so either literal monomial presentation gives exactly the
same polynomial image.

Let V_m(u)=Psi_k(u,.) C[y_1,...,y_r]_(degree<=m), and let Pi_m(u)
be the orthogonal projection for the actual fibre norm. These are nested
finite-dimensional closed subspaces with dense union. For any F in the
fibre and any eta>0, choose v in one V_m0 within eta of F. For m>=m0,
the least-distance property of orthogonal projection gives

\[
 \|(1-\Pi_m(u))F\|\le\|F-v\|<\eta.
\]

Thus Pi_m(u) converges strongly to I for every u. Positivity almost
everywhere of the actual density also shows that every finite monomial
family is independent in its weighted L2 space, so its actual Gram is
positive definite; no freely selected finite metric is involved.

This convergence is not in operator norm on the full fibre: L2(dy) is
infinite-dimensional and V_m is finite-dimensional. Its orthogonal
complement contains a unit vector, on which I-Pi_m acts as identity.
Since an orthogonal projection is a contraction, ||I-Pi_m||=1 for every
m. This exact obstruction specifies the scope of the strong limit.

## 5. Fixed-source normal residual, degree constraints and global limit

Fix one admitted source polynomial P of total degree at most M_0, and
write its unchanged centred expression as

\[
 p_u(y)=P(k/2+iu,iy),\qquad
 V_P(u,y)=\Psi_k(u,y)p_u(y).
\]

Here the notation for P uses its exact polynomial rewrite in (S,z),
not a replacement of its original coordinates. In a growing full
relative frame of degree m, take actual source degrees M_m satisfying
M_m>=max(M_0,m). Then P is still an admitted source, and its coefficient
vector in the larger frame is the original vector padded by zero.
These source-degree conditions matter: adding relative columns of degree
larger than a fixed admitted bound would change its allowed source.

For all sufficiently large m, both p_u and partial_u p_u are in the
degree-m relative polynomial space. The latter derivative retains the
factor i from S=k/2+iu and all original integer power coefficients.
Consequently its amplitude contribution is in V_m(u), and the actual
normal residual has both exact descriptions

\[
 N_m(u)c_{P,m}(u)
  =(1-\Pi_m(u))(\partial_u\Psi_k)(u,\cdot)p_u
  =(1-\Pi_m(u))\partial_u V_P(u,\cdot).
\]

For each fixed u, the vector (partial_u Psi_k)p_u lies in the actual
fibre and is independent of m. Strong convergence therefore makes its
normal residual tend to zero. Projection contraction gives the common
bound

\[
 \|N_m(u)c_{P,m}(u)\|^2
       \le\|(\partial_u\Psi_k)(u,\cdot)p_u\|^2.
\]

The right-hand function is integrable in u, since it is the fibre
square norm of a fixed polynomially weighted Schwartz function of the
complete variables. The finite Gram and projection formulas are smooth
in u on compact intervals, so the residual norms are measurable.
Dominated convergence now gives the global result

\[
 \int_{\mathbb R}\|N_m(u)c_{P,m}(u)\|^2du\longrightarrow0.
\]

The residual square norms decrease pointwise under the nested
projections. No uniform estimate over a changing source P_m is used.
For a fixed finite source core with literal basis P_1,...,P_q, the
integrated Gram restricted to that core tends to zero in operator norm:
its trace is the sum of the q fixed-column energies above, and a positive
matrix has operator norm bounded by its trace. This finite-core statement
does not give uniform control on the growing source spaces themselves.

## 6. Invariant frames have their exact invariant limit

If only invariant relative polynomials are included, their union need
not be dense in the full fibre. In the actual permutation-invariant
case, permutations of the k original factors act linearly on the
k-1 independent relative coordinates with absolute determinant one.
One direct check uses a transposition with the last coordinate:
the affected coordinate becomes minus the sum of all independent ones
and the others stay fixed, giving determinant -1. Such transpositions
generate the permutation group. The product Psi_k and its u derivative
are invariant under this action, and both dy and mu_u are invariant.

The finite group therefore acts unitarily on both Hilbert spaces, and
its averaging operator A_G is an orthogonal projection onto the
invariants: averaging is self-adjoint because inverse elements appear
with the same coefficients, and averaging twice gives the same average.
Apply A_G to polynomial approximations of an invariant function.
Averaging preserves degree and is a contraction, so invariant
polynomials are dense in the invariant subspace. The onto multiplier
U_u intertwines the group action. Thus the projections from growing
full invariant polynomial frames converge strongly to A_G on the whole
fibre, and to identity only on its invariant subspace.

For an admitted invariant source P, p_u and (partial_u Psi_k)p_u are
invariant. The same pointwise and global zero-residual conclusions
therefore hold, with the same fixed-source degree conditions and
dominating Schwartz function. A nonsymmetric source cannot be inserted
into this invariant-frame conclusion without the corresponding exact
projection onto its invariant component.

## 7. A fixed original relation forces the normal-to-jet norms to diverge

This consequence uses the already established finite reconstruction and
strictness formulas FC26 and FC28--36 of the frozen sum-connection
source. It concerns the full relative polynomial frames, k >= 2, and a
nonempty packet: the monic packet polynomial h has degree d >= 1. Keep
the original tensor quotient

\[
 B=\mathbb C[s_1,\ldots,s_k]/(h(s_1),\ldots,h(s_k))
\]

and its original, fixed positive packet metric G. Let
\(U=\prod_i v_h(s_i)\), where \(v_h=g/h\) is the entire cancelled
quotient, and let \(\upsilon=[U]_B\), retaining all confluent jets. The
full-packet hypothesis gives an invertible \(\upsilon\). The actual
arithmetic observation on a source polynomial is

\[
 J(P)=\left[\partial_{S,\mathrm{rel}}(UP)\right]_B,
 \qquad \partial_{S,\mathrm{rel}}=\frac1k\sum_{i=1}^k\partial_{s_i}.
\]

Choose the fixed original polynomial \(P=h(s_1)\), and place it in
each admitted source space once that space contains its degree d. Its
arithmetic source class is zero, but the product rule gives the exact
derivative class

\[
 J(P)=\frac1k\upsilon\,[h'(s_1)]_B\ne0.
\]

Indeed, the term \([(\partial_{S,\mathrm{rel}}U)h(s_1)]_B\)
vanishes in B, while the derivative of the polynomial contributes
\(h'(s_1)/k\). The polynomial h' has degree d-1 and nonzero leading
coefficient d. Its class in \(\mathbb C[s_1]/(h(s_1))\) is therefore
nonzero. Tensoring this nonzero vector with the nonzero constant
vectors in the other factors remains nonzero: choose a linear
functional taking value one on each of those constant vectors to
obtain a left inverse to the tensor inclusion. Multiplication by the
invertible full unit \(\upsilon\) preserves this nonvanishing. This
argument retains repeated roots and every jet order; it does not
replace B by its reduced quotient.

For the m-th frame let \(\mathcal N_m\) be the actual finite source
map into \(\mathcal K=L^2(du;L^2(dy))\), and put
\(r_m=\mathcal N_mP\). Finite-source strictness FC26 gives
\(\|r_m\|_{\mathcal K}>0\). Section 5 gives
\(\|r_m\|_{\mathcal K}\to0\). The exact finite reconstruction
defines a bounded map on its finite normal image,

\[
 \operatorname{Obs}_m:\operatorname{im}\mathcal N_m\longrightarrow B,
 \qquad \operatorname{Obs}_m(\mathcal N_mQ)=J(Q).
\]

Here the domain norm is the inherited, original normal norm in
\(\mathcal K\), and the target norm is the fixed metric G. Evaluating
this map on the specific nonzero vector r_m proves

\[
 \|\operatorname{Obs}_m\|
 \ge \frac{\|k^{-1}\upsilon[h'(s_1)]_B\|_G}
           {\|r_m\|_{\mathcal K}}
 \longrightarrow+\infty.
\]

Thus every finite map exists with the exact arithmetic derivative, but
their operator norms cannot share a finite bound through this growing
full-frame limit. The numerator is a fixed positive number in the
original packet metric. No metric was chosen to identify a normal
energy with an arithmetic jet energy. For h=1 the target algebra is
zero and this particular consequence has no nonzero target; all the
analytic density and fixed-source convergence results above still
apply.

## Audit status before the parent draft

This paragraph records the earlier independent-proof stage; the final
source audit follows in Section 8.

The independent proofs above establish the abstract density statement,
its actual arithmetic application and the stated fixed-source limits.
The main scope corrections communicated to the parent were: actual
exponential moments require the Gamma tail, not Schwartz alone; Gram
invertibility requires the actual full-support density; full and
invariant frames have different strong limits; and the source must be
fixed inside a growing admitted filtration. No quantitative estimate
uniform in the moving source degree is asserted.

## 8. Completed audit of the final TeX and full Markdown proof

The complete companion proof was read, including every definition and
proof from ND.1 through ND.34. All final mathematical deltas were then
read directly: the explicit negative frequency in Gaussian convolution,
the proved sparse-source derivative membership, and the full original
source-amplitude metric paragraph following ND.27. The final audited
files are:

| File under this work directory | Bytes | SHA-256 |
| --- | ---: | --- |
| `nested_relative_frame_density_20260912.tex` | 35415 | `4ff4c58e745f4f1251797e2a8813f3e606355160578981642770a66eedf61752` |
| `nested_relative_frame_density_20260912.md` | 34759 | `5c5a402f752031714ec9aa0db102d7348ec6c11793455494add44556614510a6` |

The separate document-integrity script
`nested_relative_frame_density_review_integrity_20260912.py` compared
the complete proof bodies after removing only section, theorem and
proof presentation wrappers, math delimiters and whitespace. Every
remaining mathematical and prose token agrees. The common comparison
body has SHA-256
`e56e67e06548d936dc2f9a3cd9b77bb3fa24ff6d7f99bd77d436361d2258911e`.
The associated JSON records the exact proof hashes, ND.1--34 sequence,
and the independently checked unchanged frozen-input hashes. This is a
document-integrity calculation, not a numerical test of the theorems.

### ND.1--10: original arithmetic estimate and every actual fibre

The final source proves the derivative exponential bound directly by
rotating Euler's gamma integral. Its rotation
\(\theta=\operatorname{sgn}(\tau)\phi\) gives
\(e^{-\phi|\tau|}\), with the correct sign, and integration of
\(r^{\lambda-1}e^{-r\cos\phi}\) gives exactly
\(\Gamma(\lambda)(\cos\phi)^{-\lambda}\). The large and small
arc bounds justify the rotation separately at infinity and zero. The
constant is bounded over the compact interval of lambda used later.

The elementary zeta continuation has its correct sign and denominator:
\(\zeta(s)=s/(s-1)-s\int_1^\infty\{x\}x^{-s-1}dx\).
On \(1/4\le\sigma\le3/4\), its bound \(6+4|t|\) follows
from \(|s/(s-1)|\le5\) and \(|s|/\sigma\le1+4|t|\).
For \(z=t+iv\), \(|v|\le1/4\), the correct gamma parameters
are \(\lambda=(1/2-v)/2\in[1/8,3/8]\) and \(\tau=t/2\).
The bound \((1+|t|)^3e^{-\phi|t|/2}\) retains the two polynomial
factors of g and the zeta factor. On the tail every original root
factor is bounded below by \(|t|/2\); on the compact complement
the quotient is its entire cancelled germ. Thus no critical-line
packet root introduces an artificial pole. The circle of radius 1/8
gives the exact derivative multiplier \(j!8^je^{b/8}\), so every
fixed derivative decays at every rate \(b<\pi/4\), without an
assumed asymptotic formula.

The dagger identity preserves the original real or purely imaginary
phase with \((-1)^d\), including all real derivatives. The signed
coordinate determinant is \((-1)^{k-1}\); its absolute value one
preserves the full product measure, and k=2 retains the factor 1/2
in the difference-coordinate measure. The exponential fibre moment
in ND.8 is exactly the bound proved independently in Section 3 with
the amplitude-square rate written as 2b. Every affine coordinate on
each fibre is nonconstant for k>=2, so all real zero preimages are
null hyperplanes, for every u. Positivity of every fibre mass follows
without discarding or reducing any zero order. The integrated mass
remains the full power \(\mu_h^k\).

### ND.11--16: complete density and exact multiplier

The finite complex measure argument is complete. Its Cauchy--Schwarz
bound leaves strict exponential slack for every holomorphic derivative.
The moments kill the local transform series, and analytic continuation
on the connected one-variable strip kills every real frequency. The
source uses the positive Fourier convention. Its final convolution
display therefore correctly contains \(\widehat\nu(-\xi)\).

The Gaussian transform is derived with its \((2\pi)^{-r}\) and
\((4\pi\varepsilon)^{-r/2}\) constants. Fubini is justified by
finite total variation and the integrable Gaussian. The subsequent
bounded uniformly continuous test functions are legitimate even when
they have noncompact support: the absolute double integral is bounded
by their supremum norm times the finite variation mass. Gaussian
approximation is uniform by uniform continuity and the explicit tail.
For a closed F, \(\max(0,1-n\operatorname{dist}(x,F))\) is bounded
Lipschitz and converges to its indicator. The resulting zero values on
closed sets imply zero values on all Borel sets by the stated pi--lambda
argument. This closes Fourier uniqueness rather than citing it.

The weighted-to-unweighted multiplier and its inverse have the exact
norm identity; values assigned on a null zero set change no Hilbert
class. The source explicitly retains the analytic zeros themselves.
The finite monomial Grams are strictly positive because a nonzero
polynomial is nonzero on a nonempty open set and the actual weight is
positive almost everywhere. Literal phases \(i^{|\alpha|}\),
zero-padding, Gram congruences and projection compositions all check.
The full strong limit and the exact norm \(\|I-\Pi_m\|=1\)
have their respective complete proofs and correct domains.

### ND.17--28: source degree, derivative, graph and both source metrics

The invertible original coordinate substitution preserves the total
degree bounds in ND.17. Keeping P fixed, m>=D and M_m>=max(D,m)
makes every relative and S degree admissible; the zero-padding is an
identity on the original polynomial. The coefficient derivative is
\(i\partial_S^{\rm rel}P\), with
\(\partial_S^{\rm rel}=k^{-1}\sum_i\partial_{s_i}\), and is
inside the same relative frame. The equality
\(r_m=(I-\Pi_m)\partial_uA_P=(I-\Pi_m)\Psi'_up_u\)
therefore uses one fixed vector, not a vector depending on m.

The original Mellin test class used by the source is
\(\mathscr B=\{f:\sup_{x>0}x^b|D^jf(x)|<\infty\text{ for all
integer }b\text{ and }j\ge0\}\), with \(D=-x\partial_x\).
On that class every logarithmic multiplier and its Euler derivatives
remain in the same class: Leibniz gives finitely many terms involving
powers of log x and Euler derivatives of f, and each fixed log power
is bounded by a constant times a sum of a positive and a negative
power of x. The arbitrary b bounds absorb those powers. Consequently
the Mellin integrations by parts have vanishing endpoint terms and
logarithmic differentiation is absolutely justified on each fixed
vertical line. This verifies the original-domain claims in ND.21.
The critical-line Mellin isometry has the retained factor
\((2\pi)^{-k/2}\). Its derivative is
\(\partial_u\mathscr U_k=i\mathscr U_k\mathscr L_k\), and
the direct commutator is \([D^{(k)},\mathscr L_k]=-I\).

The projection decomposition, squared graph norm and monotone residual
identity are exact orthogonal decompositions. The dominating function
\(\|\Psi'_up_u\|^2\) is integrable by the proved derivative
tails. Smooth Gram inversion proves continuity on compact u intervals;
the increasing open sublevel cover proves compact uniform convergence.
The theorem correctly makes no claim about convergence of a derivative
of the residual.

For an independent nonempty finite source core, the added original
amplitude Gram G0 is strictly positive. To justify its real-coordinate
nonvanishing explicitly, the substitution \(s_i=1/2+it_i\) is an
invertible affine polynomial substitution. A polynomial vanishing on
all of real \(t\)-space is zero by the one-variable polynomial
identity successively in each coordinate. Therefore a nonzero original
polynomial has a nonzero restriction on an open set; the full product
amplitude is nonzero almost everywhere there. This proves the claimed
Gram positivity. The equalities

\[
 K_m=G_0^{-1}H_m,\qquad K_m^*G_0=G_0K_m=H_m,
 \qquad
 G_0^{1/2}K_mG_0^{-1/2}=G_0^{-1/2}H_mG_0^{-1/2}
\]

give exactly the positive operator in the original metric and its
Euclidean presentation. Its largest eigenvalue equals the squared
operator norm of R_m with that original source metric. The bound with
\(\lambda_{\min}(G_0)^{-1}\) is valid and yields the original
metric limit. Empty source arrays have their zero maps in the explicit
empty-case paragraph; no minimum eigenvalue is required for them.

The full arithmetic jet unit is retained, including mixed nilpotents.
At each selected root the full removed multiplicity makes v_h nonzero;
the inverse in each local finite jet algebra is the finite geometric
series in its nilpotent ideal. Taking all tuple components proves the
full tensor unit assertion. The Mellin derivative observation remains
\(j_I\partial_S^{\rm rel}(UP)\), at every source degree. Its
constancy under literal inclusion is proved on the same P. Section 7
above and the separately owned normal-observation work provide the
nonzero fixed-relation consequence; the density source does not add an
unjustified continuous jet map on the ambient Hilbert limit.

### ND.29--34: invariants, sparse spaces, exceptional fibres and transport

Every specified finite subgroup acts by permutations of the original
factors and fixes u. Its relative determinant has absolute value one,
and the original amplitude is invariant. The source therefore proves
the actual unitary representation and its Reynolds orthogonal
projection. Averaging degree-preserving polynomial approximants proves
the invariant density and the exact full-space limit to the Reynolds
projection. The invariant source derivative remains in that image, so
its residual limits use the same fixed-source argument.

For arbitrary fixed nested relative polynomial spaces, the Pythagorean
Cauchy argument identifies the strong limit as the projection onto
their actual closed union. The final source now explicitly proves that
coefficient differentiation stays in the same admitted relative space.
Its global limiting residual follows by dominated convergence with the
stated integrable bound. The constant-space example uses the exact
weighted mean and a nonzero weighted centred-coordinate vector to
exhibit failed approximation.

The zero source, a nonzero polynomial with zero arithmetic class, the
empty packet, empty arrays and initial frame, and the one-factor
exclusion are all handled explicitly. On the even-amplitude two-factor
fibre at u=0, the stated derivative product cancels exactly, so
\(j_m'=N_m=r_m=0\) there. This does not make the amplitude weight
zero and does not obstruct the density result. Only the source Gram
is inverted in this proof.

The complete gauge derivative term is present and cancels when the
admitted coefficient column is pulled back. The changed inclusion
\(C_n^{-1}E_{nm}C_m\) is the exact map between changed coefficient
presentations, while the actual projected images and graph components
are unchanged. Finally the two half-line branches preserve their
Jacobian \(1/(2\sqrt x)\). The even/odd reconstruction retains
the factor \(i\sqrt x\), and the parallelogram calculation gives
exactly the weights \(x^{-1/2}\) and \(x^{1/2}\). Given any
pair in those weighted spaces, the displayed inverse defines a
measurable full-line vector with precisely that norm, proving onto-ness.
The point u=0 has measure zero for the Hilbert map; original smooth
vectors retain their own trace. No independent boundary data or
unproved derivative-residual limit is introduced.

### Final audit result and scope

No mathematical defect remains in the two proof files at the exact
hashes above. The document-integrity comparison passes and the recorded
frozen inputs have unchanged bytes and hashes. This audit writes only
new files in the working directory. It performs no PDF build, changes
no published source, and makes no release or upload. The result proves
the stated actual frame-density and fixed-source derivative limits;
it supplies no uniform estimate over a moving source sequence and does
not identify a normal metric with an arithmetic metric.
