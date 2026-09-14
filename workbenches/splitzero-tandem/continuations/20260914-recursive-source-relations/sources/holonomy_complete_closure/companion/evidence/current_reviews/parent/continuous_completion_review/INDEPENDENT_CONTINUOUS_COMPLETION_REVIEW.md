# Independent review: original continuous relation completion

Date: 2026-09-13. Scope: CR1--14 in the parent's
`period_laplacian/CONTINUOUS_RELATION_COMPLETION.md`, including the subsequently
written CR12a--c pullback construction. This is a written mathematical review,
not a numerical or Lean certificate. Only this new independent review
directory is written. No source, owner, public, or remote artifact is edited.
No new model examples are needed.

## Disposition and the actual positivity issue

Accept CR1--11 and CR13--14 with the exact domains and positive-support maps
specified there. Accept the revised unconditional CR12a--c and CR12.
The original HCD2 assumption is a uniformly positive finite phase family;
it is not, by itself, a proof of that assumption for every one-fold phase.
Full-order cancellation proves positivity at a sampled selected root, not
positivity of every sampled weight or invertibility of every finite
one-fold source Gram. The pullback construction resolves that distinction
without adding a hypothesis or choosing a new source norm.

For the actual source one can also prove, without uniform phase positivity,
that every finite averaged pullback form is positive definite, and that
these average forms decrease to zero. The full graph closure of the
original class map is `H x E`. Proofs and qualifications follow.

## 1. Continuous measure, density, and domains

Retain the original full-order packet `h`, tensor degree `k>=1`,
`g=2 xi`, `c=k/2`, `S(u)=c+iu`, and

`w_h(u)=|(g/h)(1/2+iu)|^2/(2 pi)`, `m=w_h^{*k}`, `dnu=m(u)du`.

HD1 and P54 provide the positive exponential moments for this actual
measure; P54 also provides the pointwise exponential bound needed for
sampling. No mass normalization occurs: `nu(R)=mu_h^k`. The quotient
`g/h` is entire and nonzero after full-order removal. Its real-line zeros
are isolated, so `w_h>0` almost everywhere. For `k>=2`, integrating the
positive-almost-everywhere product in convolution proves `m(u)>0` for
every real `u`. The inherited boundedness/integrability makes those
convolution integrals finite. In every case `nu` is atomless and positive
on every set of positive Lebesgue measure.

For either `eta=nu` or `eta=|chi(S)|^2 nu`, a smaller positive exponential
exponent absorbs the fixed polynomial factor. Every polynomial is in
`L^2(eta)`. With inner product `integral conjugate(f) g d eta`, orthogonality
of `f` to all `S`-polynomials gives zero moments of
`sigma=conjugate(f) eta` in `u`, since `u=(S-c)/i` is invertible.
Cauchy--Schwarz supplies the exponentially weighted finite variation
needed in CR4. Hence `F(z)=integral exp(izu) d sigma(u)` is holomorphic
in the stated strip; dominated differentiation on each smaller strip is
valid for every order. All derivatives at zero vanish. The identity
theorem gives `F=0` on the strip.

The Gaussian uniqueness argument in CR4--5 has the correct Fourier signs:
`gamma_t(x-u)` contributes `exp(-i zeta x) exp(i zeta u)`, so its integral
against `sigma` is zero. Finite variation permits Fubini; compactly
supported continuous test functions are uniformly approximated by their
Gaussian convolutions. Thus `sigma=0`, hence `f=0` almost everywhere.
This proves both polynomial-density assertions without a moment-problem
uniqueness hypothesis being silently added.

Put `H=L^2(nu)` and `H_chi=L^2(|chi(S)|^2 nu)`. The map

`U_chi:H_chi -> H`, `f -> chi(S) f`

is a linear onto isometry. The inverse `v/chi(S)` belongs to `H_chi`
because its weighted squared norm is exactly `||v||_H^2`. The finitely
many real zeros of `chi(S)` have zero `nu`-mass; inverse values there are
irrelevant to both equivalence classes. This is not an assertion that
unweighted multiplication by `chi` is bounded `H -> H`. Its weighted
domain is essential and is exactly the inherited norm of its relation
image, so it does not replace the source metric.

Density in `H_chi` and this onto isometry prove
`closure_H(chi C[S])=H`. Completing the two terms of the inclusion
complex `[chi C[S] -> C[S]]` in their inherited `H` norms therefore gives
`[H --I--> H]`, whose degree-minus-one contraction is `I`. The original
algebraic quotient `E=C[S]/(chi)` maps to its zero completed quotient with
kernel all of `E`. In particular completion does not identify the
original algebraic quotient with zero before the stated map.

## 2. The same finite canonical forms and the full graph

For `N>=q-1`, multiplication by the literal nonzero `chi` is injective
on `P_{N-q}` and has image `B_N=ker J_N`. At `N=q-1` this is the zero
relation space. Polynomial evaluation in `H` is injective because a
nonzero polynomial has only finitely many real-line zeros and the density
is positive almost everywhere. Thus every finite original `M_N` is
positive definite.

Let `s:E -> P_{q-1}` be the fixed remainder section and let `Pi_N` be
orthogonal projection in the actual `H` norm onto `B_N`. Then

`R_N=(I-Pi_N)s`, `J_N R_N=I_E`, `G_N=R_N^* R_N`.

The adjoint in this Gram uses the fixed coefficient inner product on
`E` and the actual `H` inner product. Every lift is `s x+b`, `b in B_N`;
orthogonal decomposition gives unique minimality. In coefficient
coordinates the unique minimizer is exactly

`G_N=(J_N M_N^{-1}J_N^*)^{-1}`,
`R_N=M_N^{-1}J_N^*G_N`.

All inverses here are legitimate: `M_N>0` and `J_N` is onto. No phase
positivity enters these continuous-source formulas.

The `B_N` increase and have dense union. Therefore `Pi_N -> I_H`
strongly. Applying this to the finitely many fixed columns of `s` gives
`R_N -> 0` in the operator norm from any fixed finite norm on `E` to
`H`, and hence `G_N -> 0` in every fixed coordinate matrix norm. The
minimum decreases when relations are enlarged, proving `G_N downarrow 0`
in Loewner order. Each finite `G_N` remains positive definite, and
`det G_N -> 0` since `q>=1`. No cutoff or tensor-degree rate follows.

For every `x in E`, `(R_N x,J R_N x) -> (0,x)`. Thus the closure of
`graph J` contains `{0} x E`. It also contains `(p,Jp)` for every
polynomial `p`, and is a closed linear subspace. Adding `(0,x-Jp)`
shows it contains `(p,x)` for every polynomial `p` and every `x`.
Polynomial density now proves the exact stronger assertion

**`closure(graph(J:C[S] subset H -> E)) = H x E`.**

This is full nonclosability, not just an unbounded-evaluation example.
It is compatible with `J_N R_N=I_E` at every finite cutoff. Under every
fixed invertible coefficient change `x=W x'`, the exact maps become
`G_N'=W*G_NW`, `R_N'=R_NW`, `J_N'=W^{-1}J_N`; all claims persist.

## 3. Unconditional finite phase pullback, including singular phases

Fix the original `L>0`, put `u_n(theta)=(2 pi n+theta)/L`, and retain
`nu_n(theta)=(2 pi/L)m(u_n(theta))`. Let

`I_theta={n:nu_n(theta)>0}`,
`H_theta=ell^2(I_theta,nu_theta)`,
`T_theta P=(P(c+iu_n(theta)))_{n in I_theta}`.

The pointwise exponential estimate P54/CQ5 and its lattice sum CQ6
prove every finite polynomial evaluation is in this original Hilbert
space, including when `k=1`. Zero-weight coordinates are null classes,
never inverted evaluation functionals. Define

`Q_{N,theta}=T_theta(P_N)/T_theta(B_N)`

with the quotient norm inherited from `H_theta`. Both images are
finite-dimensional and closed, whether or not `T_theta` is injective.
The map

`rho_{N,theta}:E -> Q_{N,theta}`, `[P] -> [T_theta P]`

is well defined and onto. Its exact kernel is

**`ker rho_{N,theta}=J_N(ker(T_theta|P_N))`.**

Indeed `T_theta P=T_theta b`, for some `b in B_N`, exactly when
`P-b` is a sampling-null polynomial with the same class. Conversely
such a null representative maps to zero. The unique pullback form is

`x*G_{N,theta}x=min_{b in B_N}||T_theta(sx+b)||^2`.

The minimum exists because it is distance to a closed finite-dimensional
relation image. Its minimizing observed vector is unique, although a
minimizing coefficient polynomial need not be. Its radical is the exact
displayed kernel. If `M_{N,theta}>0`, this is precisely the usual positive
canonical Gram `(J_N M_{N,theta}^{-1}J_N^*)^{-1}`. At a singular phase
that inverse expression is not asserted.

For each fixed `x`, the minimum equals the infimum over a countable dense
set of complex rational relation coefficients. The norm at each such
coefficient is measurable in `theta`, so the infimum is measurable;
polarization makes all matrix entries measurable. Testing the particular
original lift `R_N x` and unfolding the literal phase measure gives

`integral x*G_{N,theta}x dtheta/(2 pi)`

` <= integral ||T_theta R_N x||^2 dtheta/(2 pi)`

` = integral_R |R_Nx(c+iu)|^2 m(u)du = x*G_Nx`.

The normalization is exact: `(2 pi/L)dtheta/(2 pi)=du` on each lattice
interval. The integrals are finite. Off-diagonal entries are integrable
by the positive-form inequality `|G_ij|<=sqrt(G_ii G_jj)` and
Cauchy--Schwarz in the actual phase measure. Thus for every original
`k>=1` and every `N>=q-1`, without universal phase invertibility,

**`0 <= bar G_N := integral G_{N,theta} dtheta/(2 pi) <= G_N`,**

**`D_N:=G_N-bar G_N >= 0`.**

### Exact relation-gap version without coefficient inverse assumptions

Let `Pi_{N,theta}` be orthogonal projection in `H_theta` onto
`T_theta(B_N)`. Since `T_theta R_N x` and `T_theta s x` differ by
that relation image, the minimizing observed lift is
`(I-Pi_{N,theta})T_theta R_N x`. Orthogonal decomposition gives

`x*D_Nx = integral ||Pi_{N,theta}T_theta R_N x||^2 dtheta/(2 pi)`.

This is an exact positive original-relation norm at every phase; it
specializes to HCD13 on the admitted positive family. For an explicit
measurable coefficient formula only, let `B` contain the literal relation
columns, `F_theta=B*M_{N,theta}B`, and
`d_theta=B*M_{N,theta}R_N`. Then the projected relation is
`T_theta B F_theta^+ d_theta`, where `+` is the finite Moore--Penrose
pseudoinverse. Here `d_theta` lies in the range of `F_theta`: a vector in
`ker F_theta` gives the zero observed relation and hence pairs to zero
with `T_theta R_N`. Thus this expression is precisely the projection,
not a modified quotient. Pseudoinverse is Borel measurable, for example
as the limit of `(F_theta^2+epsilon I)^{-1}F_theta`. Its observed
squared norm is bounded by that of `T_theta R_N`, so the integral exists
even if the chosen coefficient representative is not uniformly bounded.
At `B_N=0` the projection is zero and `D_N=0`.

The mean-zero coefficient contraction and coefficientwise averaging of
arbitrary fields in HCD5--16 still use the HCD2 uniform-equivalence
hypothesis. The unconditional argument above does not silently extend
those stronger coefficient-field assertions beyond their stated domain.

### What is unconditional about one-fold positivity

For `k=1`, the zeros of the actual nonzero entire `g/h` on the sampled
vertical line form a discrete, hence countable, set. Their phases modulo
`2 pi` form a countable set. Outside it every lattice weight is positive;
a nonzero polynomial cannot vanish at all the infinitely many distinct
sample points. Therefore `M_{N,theta}>0` for almost every phase,
simultaneously for all finite `N`. For `k>=2` the same statement holds
at every phase by everywhere-positive convolution.

Consequently, for every nonzero fixed `x`, `x*G_{N,theta}x>0` almost
everywhere and its integral is positive. This proves the additional
actual-source statement

**`bar G_N>0` at every finite cutoff, and `bar G_N downarrow 0`.**

Monotonicity follows phasewise by enlarging relations; the limit follows
from `bar G_N<=G_N`. Also `0<=D_N<=G_N` implies `D_N->0`. No
monotonicity of `D_N`, no zero limit for `G_N^{-1}D_N`, and no uniform
positive lower bound in `theta` is inferred. In particular positivity
almost everywhere does not supply the HCD2 uniform lower constant.

## 4. Fixed-phase limits, full primary kernels, and surviving masses

The exponential sampled moment proof applies on `I_theta`, and also
after multiplying the measure by `|chi|^2`. Thus the sampled polynomial
vectors are dense. The image of multiplication by `chi` is exactly the
closed subspace vanishing at

`Z_theta={n in I_theta:chi(c+iu_n(theta))=0}`.

Division by `chi` on the complementary positive atoms proves the reverse
inclusion isometrically in the weighted domain. Restriction to `Z_theta`
is the orthogonal quotient map, with squared norm
`sum_{n in Z_theta} nu_n(theta)|v_n|^2`. No weight or phase is removed.

Increasing finite relation images have union equal to the evaluated
polynomial relation space. Their distances therefore decrease to distance
to its closure, including singular finite phase Grams. For every class
`x`, this proves

`x*G_{N,theta}x downarrow sum_{n in Z_theta}nu_n(theta)|x(S_n(theta))|^2`.

Polarization gives the matrix limit CR13 in the same fixed coefficient
frame. Let `p_theta` be the squarefree product of the displayed roots.
The exact limiting radical is `(p_theta)/(chi)`. In a sampled primary
block `C[epsilon]/(epsilon^r)`, only the constant coefficient is received
and the full ideal `(epsilon)/(epsilon^r)` stays in the kernel. Every
unsampled primary block stays entirely in the kernel. This uses the
full original `chi`; it does not replace its multiplicities by a reduced
polynomial upstream.

At `k=1`, the original cyclic minimal polynomial has ideal `(chi)=(h)`.
If `a_h` is the original leading coefficient, `chi=h/a_h` identifies the
monic ideal generator, without replacing the density `|g/h|^2/(2 pi)`.
For an actual selected root `rho` of complete order `r`, write
`h=(S-rho)^r h_0`, with the unchanged `h_0(rho)!=0`. Then

`(g/h)(rho)=g^{(r)}(rho)/(r! h_0(rho)) != 0`,

`nu_n(theta)=|g^{(r)}(rho)|^2/(L (r!)^2 |h_0(rho)|^2)>0`

whenever `S_n(theta)=rho`. Thus no sampled root of the actual one-fold
`chi` loses its receiving line to a zero weight. This does not say that
every phase samples such a root or that every other atom has positive
weight. It is the exact narrower positivity needed for CR14.

If a displayed sampled root exists, take the original unit class `x=1`
(or any class evaluating to one there). Since `G_{N,theta}>=K_theta`,
its numerator is at least the retained positive mass. Its continuous
denominator is positive at every finite cutoff and tends to zero by
CR11. This proves the quotient ratio in CR14 tends to infinity. If
`Z_theta` is empty there is no such lower bound and no relative rate is
asserted. No sampled root is invented.

Only finitely many phases can sample a root of the fixed `chi`: each
root on `Re S=c` specifies its unique phase `L Im rho mod 2 pi`.
The completed quotient field is therefore zero almost everywhere. Its
measurable realization is the range in ordinary `ell^2(Z)` of the diagonal
projection with entries
`1_{nu_n(theta)>0} 1_{chi(S_n(theta))=0}`. Its direct integral is the
zero Hilbert space, and the induced map from the whole original `E`
has kernel `E`. Individual exceptional weighted fibres are not erased
pointwise. The retained marked map is `(label,v)->(label,0)`, with
`tau->tau`; represented zero is not external absence.

## 5. Read scope and provenance pins

Read completely: the original and revised root note; the current HD source;
the completed-phase density review; the continuous-descent review; and the
complete delivered periodized-source research note. Source SHA-256 pins:

- `source-workspace/work/holonomy_degree_cost_20260913.tex`:
  `9A1BA6CD7E8BEE67C6D7868C74F2CF4F9D8C11FA255D9D278C7A2420CF0DACA6`.
  This current version includes HD10. The parent's earlier `56c05d...`
  pin concerns its earlier HD1--9 snapshot, not this current file.
- `source-workspace/work/holonomy_completed_quotient_density_review_20260913.md`:
  `20FC066345E4AD5860C0EEB02BB7E446A69CA0826CC8D8F2196B517BA91EA753`.
- `source-workspace/work/holonomy_continuous_descent_review_20260913.tex`:
  `E283A93B513CB99398CE5F43BBF230D1494BFB55D59243916B1E017852B376C6`.
- `source-workspace/output/split_zero_rh_tandem_2026-09-12/sources/web_periodized_source_delivery/Tau_Periodized_Source_Control/RESEARCH_NOTE.md`:
  `F903AE8473EFDFCDE0F45A83878837289D2B0604C1A34903276D7C840FE972B9`.

Key source proof locations are HD1--5 and HD6--10; HCD2 for the uniform
phase assumption, HCD9--16 for its positive-family gap formulas,
HCD17--29 for sampled support, completion and marked maps; CQ4--8 for
actual exponential sampled tails, CQ14--22 for the quotient and primary
kernel, CQ23--25 for exact one-fold root masses, CQ26--29 for the
direct integral; and P8--10, P26a--b, P53--58 in the delivered note.

This review makes no evaluated arithmetic enclosure, uniform source or
tensor-degree estimate, public-publication, or proof-assistant claim.
