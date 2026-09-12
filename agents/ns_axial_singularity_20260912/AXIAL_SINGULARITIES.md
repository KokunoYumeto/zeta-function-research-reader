# Sharp complex radius of the actual source axial trace

12 September 2026. Local mathematical continuation; not a public upload.

## Source, coordinates, and result

The starting source is the complete `../ns_axis_lagrange_20260909/AXIAL_COEFFICIENTS.md`,
SHA-256 `a17d1d4266dc965f2789a9e4080f0a8789c2537f62bace585b50eecbca087bad`,
Sections 1–2 and their residue proof. That note derives the actual released
Navier–Stokes manuscript's Appendix B axial data, pp. 144–147, and retains the
original fixed parameters

    0<h<1/100, A=1/2+h, D=1/2-h, 0<j0<=1/20, nu>0, tau=1-t>0.

The source existence theorem and cutoff-to-axis identification are inherited,
not re-proved by this continuation. The mathematical input used below is the
explicit germ, whose identities are proved in the cited note:

    x=z/(sqrt(nu) tau^D),     z=sqrt(nu) tau^D x,
    x=f(eta)=eta(1-eta^2)^(-D),
    W(x)=(1-eta(x)^2)^A(4eta(x)+j0),
    w0(z,t)=sqrt(nu) tau^(-A) W(x).                         (1)

The logarithm of `1-eta^2` equals zero at eta=0 and eta(x) is the inverse
germ with eta(0)=0, eta'(0)=1. We introduce only the exact abbreviations

    p=2D=1-2h, q=2h=1-p, B=p^p q^q,
    R=B^(-1/2)=p^(-D)q^(-h).                              (2)

Here q is an abbreviation used only in this note, NOT the source time
coordinate q of the preceding note; that source coordinate remains
`q_source=tau/(1-eta^2)`. No physical coordinate, viscosity, time exponent,
or field amplitude has been normalized away.

**Result.** For every allowed real h and j0, the Taylor series of W has
exact radius R. Four genuine square-root boundary singularities of its
analytic continuation from that disk occur at

    x_(epsilon,sigma)=epsilon R exp(-i sigma pi D),
    epsilon,sigma in {-1,+1}.                             (3)

Its physical axial Taylor radius is exactly

    rho(tau)=sqrt(nu) tau^D R.                            (4)

These are statements about the analytic germ of the actual axial trace at
each fixed preterminal time. They do not assert a complex singularity of
the full cutoff field, which has additional variables and cutoff functions.
They do not give a zero of zeta, a sign for the full Weil form, or a
counterexample to RH.

## 1. Exact gamma identities, including every zero

Write W=sum a_n x^n. The source coefficient formulas give a0=j0, a1=4 and

    a_(2j)=j0 (-1)^j A/j binom(pj-D,j-1),
    a_(2j+1)=4 (-1)^j/j binom(pj,j-1),       j>=1.         (5)

The binomial here is its finite-product polynomial. With the entire
reciprocal gamma function rgamma, an equivalent formula valid for EVERY
j>=1 is

    a_(2j)=j0 A (-1)^j Gamma(pj+A)/Gamma(j+1)
                                  *rgamma(2-qj-D),
    a_(2j+1)=4 (-1)^j Gamma(pj+1)/Gamma(j+1)
                                  *rgamma(2-qj).          (6)

The gamma numerators have positive arguments. To prove (6), initially use
the gamma recurrence for a binomial away from denominator poles, then
extend using the entire reciprocal gamma function and the finite-product
identity. Consequently no division by a zero gamma or a zero sine occurs.
The exact finite-index zero conditions are

    a_(2j)=0 iff qj+D is an integer >=2,
    a_(2j+1)=0 iff qj is an integer >=2.                  (7)

For j>A/q in the even case, and j>1/q in the odd case, reflection gives
the stronger identities with positive, finite gamma envelopes:

    a_(2j)=(-1)^(j+1) E_j cos((2j-1)pi h),
    E_j=(j0 A/pi) Gamma(pj+A)Gamma(qj-A)/Gamma(j+1)>0,

    a_(2j+1)=(-1)^(j+1) O_j sin(2pi h j),
    O_j=(4/pi) Gamma(pj+1)Gamma(qj-1)/Gamma(j+1)>0.         (8)

Indeed `1/Gamma(2-u)=-Gamma(u-1)sin(pi u)/pi` when u>1,
including the integers by continuity; for the even case put u=qj+D and
use sin(pi(qj+D))=cos((2j-1)pi h). At integer u>=2 the positive gamma
factor is finite and the sine is EXACTLY zero. The threshold excludes
u=1, where a formal zero-times-pole would otherwise be misleading. Formula
(6), not that ill-defined product, handles this and every smaller index.

The imported classical reflection identity is NIST DLMF §5.5(ii), equation
[5.5.3](https://dlmf.nist.gov/5.5.E3). Its section and formula, including
the excluded integer arguments, were read. The continuation step just
given is part of the present proof.

## 2. Sharp envelope, powers, and phases

For fixed h (no uniform h->0 assertion), positive-real Stirling gives

    Gamma(cj+b)=sqrt(2pi) exp(-cj)(cj)^(cj+b-1/2)
                                *(1+O_h(1/j)), c>0.     (9)

This is the only imported asymptotic theorem: DLMF §5.11(i),
[5.11.3–4](https://dlmf.nist.gov/5.11.E3), restricted to the positive
real axis. For a fixed real shift b, (9) follows from that formula by
expanding log(1+b/(cj)); its order-zero exponential shift cancels.
Applying (9) to the two positive gamma products in (8) yields

    E_j=C_e B^j j^(-3/2)(1+O_h(1/j)),
    C_e=j0 A sqrt(2/pi) p^h q^(-1-h),

    O_j=C_o B^j j^(-3/2)(1+O_h(1/j)),
    C_o=4 sqrt(2/pi) p^(1/2)q^(-3/2).                    (10)

For clarity, in Gamma(pj+b)Gamma(qj+c)/Gamma(j+1) the power of j is
b+c-3/2, its positive constant is
sqrt(2pi)p^(b-1/2)q^(c-1/2), and its exponential is B^j.
The pairs are (b,c)=(A,-A) and (1,-1), respectively. This proves
every constant in (10), without fitting numerical samples.

One additional term, useful for checking the large-order calculation, is

    E_j=C_e B^j j^(-3/2)(1+c_e/j+O_h(j^(-2))),
    c_e=(11-2q-7q^2)/(24pq),
    O_j=C_o B^j j^(-3/2)(1+c_o/j+O_h(j^(-2))),
    c_o=(13-13q+q^2)/(12pq).                             (10a)

To derive it, retain the `1/(12z)` term of Stirling and expand the
fixed shifts. With B2(b)=b^2-b+1/6, the coefficient in the positive
product with shifts (b,c) is
`B2(b)/(2p)+B2(c)/(2q)-1/12`. Substituting the two shift pairs just
listed and p=1-q gives (10a). This is an expansion of the envelope,
not a division by any possibly zero trigonometric phase.

Equations (8) and (10) are the sharp asymptotics. The errors belong to
the positive ENVELOPES, so they remain valid even when the coefficient
vanishes. One must not write a ratio asymptotic dividing by its sine or
cosine on a zero subsequence. Nor does a uniform lower bound hold for
every nonzero coefficient when h is an arbitrary irrational number.

## 3. Exact radius for every allowed real h

The upper bound from (8)–(10) implies both parity limsups are at most
sqrt(B). To prove the reverse bound without any rationality assumption,
use for arbitrary theta and delta

    |sin(delta)| <= |sin(theta)|+|sin(theta+delta)|.        (11)

This follows by expanding sin((theta+delta)-theta). Take delta=pi q;
then 0<q<1/50, so |sin(delta)|>0. In every pair of successive j's,
at least one of either shifted sine sequence in (8) has absolute value
at least sin(pi q)/2. Thus each parity has infinitely many indices on
which its coefficient is bounded below by a fixed positive multiple of
B^j j^(-3/2). Taking roots proves

    limsup_j |a_(2j)|^(1/(2j))=sqrt(B),
    limsup_j |a_(2j+1)|^(1/(2j+1))=sqrt(B).               (12)

Cauchy–Hadamard now gives the exact radius (2). This proof includes
rational h with infinitely many zero coefficients. It uses no genericity
condition. Since 0<p,q<1, R>1, and R tends to 1 as h decreases to zero;
the excluded endpoint h=0 has different coalescing branch geometry and
is not obtained by a uniform-in-h use of (10).

## 4. Access to the critical points on the original inverse branch

It is important not merely to find critical points on an unrelated sheet.
We first verify that eta itself is holomorphic throughout |x|<R. The
residue/Lagrange argument in the source note gives

    [x^(2j+1)]eta(x)=(-1)^j/(2j+1) binom(pj+D,j),
    [x^(2j)]eta(x)=0.                                   (13)

For j>D/q the first coefficient equals

    (-1)^j/(pi(2j+1))
      *Gamma(pj+D+1)Gamma(qj-D)/Gamma(j+1)
      *sin(pi(qj-D)).                                   (14)

The same positive-real gamma calculation gives an O_h(B^j j^(-3/2))
upper bound. The inverse power series therefore converges on |x|<R.
Its initial inverse identity continues along any path on which f has
nonzero derivative, by uniqueness of analytic continuation of that germ.

Put r=q^(-1/2)>1. Starting at eta=0, travel along the imaginary axis to
eta=ir, and then along the upper circle |eta|=r to either endpoint +r
or -r. No point eta=+1 or -1 is met. On the imaginary segment,

    |f(iv)|=v(1+v^2)^(-D), 0<=v<=r,

which is increasing because its derivative is
`(1+v^2)^(-D-1)(1+qv^2)>0`; its endpoint modulus is smaller than R.
On the circular arcs, for eta=r exp(i theta),

    |f(eta)|=r |1-r^2 exp(2i theta)|^(-D) < R            (15)

except at theta=0,pi, because
`|1-r^2 exp(2i theta)|^2=(r^2-1)^2+4r^2 sin^2(theta)`.
The endpoint modulus is
`r(r^2-1)^(-D)=q^(-h)p^(-D)=R`.

The conjugate lower-half-plane paths give the other two approaches.
All image paths before their endpoints lie strictly INSIDE the inverse
power-series disk. Local inverses along these paths are the continuation
of the original germ: the disk's holomorphic eta(x) and each successive
local inverse agree on their overlap, starting at zero. Thus their
limits are the actual values eta=epsilon r of that branch.

Let sigma record the endpoint logarithm

    Log(1-eta^2) -> log(p/q)+i sigma pi.

The four endpoints of the image paths are precisely (3). They are
distinct for 0<D<1/2. This proves accessibility on the original branch,
not just the existence of critical values somewhere on a logarithmic
cover. We do not require a classification of every other continuation
sheet or every possible boundary point.

## 5. The square root does not cancel in W

On each endpoint's local logarithm branch, d_c=1-eta_c^2=-p/q is nonzero.
Direct differentiation gives

    f'(eta)=(1-eta^2)^(-D-1)(1-q eta^2),
    f''(eta_c)=-2q eta_c d_c^(-D-1),
    f''(eta_c)/x_c=2q^2/p !=0.                           (16)

Consequently

    1-x/x_c=-(q^2/p)(eta-eta_c)^2+O((eta-eta_c)^3).       (17)

For a proof of the local square-root inversion rather than a formal
assertion, factor the right side as `(eta-eta_c)^2 H(eta)` with H
holomorphic and H(eta_c)=-q^2/p. A nonvanishing holomorphic H has a
local holomorphic square root. The function
`(eta-eta_c)sqrt(H(eta))` has nonzero derivative at eta_c, hence has a
holomorphic local inverse. Composing that inverse with sqrt(1-x/x_c)
proves the convergent Puiseux expansion. With the square root asymptotic
to the positive one along the circle approach, its leading term is

    eta(x)=epsilon/sqrt(q)+kappa_(epsilon,sigma)
                       sqrt(1-x/x_c)+O(1-x/x_c),
    kappa_(epsilon,sigma)=-i epsilon sigma sqrt(p)/q.     (18)

The sign follows because the approach to eta_c has imaginary part of
sign -epsilon sigma; (17) is positive real to leading order on that
circular approach. Squaring kappa gives -p/q^2 as required.

For F(eta)=(1-eta^2)^A(4eta+j0), use A+D=1 and eta_c^2=1/q:

    F'(eta_c)=d_c^(-D)(-8/q-2A j0 eta_c)
             =-(2/q)d_c^(-D)(4+epsilon A j0 sqrt(q)).    (19)

This is NONZERO throughout the source parameter interval: A<51/100,
j0<=1/20, sqrt(q)<1, so A j0 sqrt(q)<51/2000<4. Substitution in (18)
therefore gives the genuine branch expansion

    W(x)=F(eta_c)+F'(eta_c) kappa_(epsilon,sigma)
                      sqrt(1-x/x_c)+O(1-x/x_c),         (20)

with every leading coefficient specified and nonzero. In particular a
holomorphic extension through x_c would be impossible: its derivative
along this branch has a nonzero inverse-square-root leading term.
This gives a geometric proof that these four radius-R points are actual
singularities, compatible with the phases and j^(-3/2) powers of (8)–(10).
No transfer theorem is needed to obtain the coefficient asymptotics.

## 6. Exact physical derivative growth and scope

Restoring (1) gives all derivative values

    partial_z^n w0(0,t)=n! nu^((1-n)/2) tau^(-A-nD) a_n,
    limsup_n |partial_z^n w0(0,t)/n!|^(1/n)
                                =1/(sqrt(nu) tau^D R).  (21)

The four complex physical locations are
`z_c=sqrt(nu) tau^D epsilon R exp(-i sigma pi D)`. Their moduli shrink
like the ORIGINAL tau^D as tau decreases to zero, and the branch-value
amplitude is still multiplied by sqrt(nu) tau^(-A). The all-order
factorial derivative growth and its exact moving radius are properties
of this source trace, not an independently proved global blowup theorem.

## Reading and verification record

The existing canonical index was queried for `Gamma Stirling` in both
research and modern local layers, and `Enumerative Combinatorics` in the
research layer. The routed Ribeiro–Yakubovich source
`PUBUNIT-A405A8CE82D0693D16FA5014`, arXiv:2112.10561, has a vertical-strip
Stirling passage in §1.2, TeX lines 559–579. That complete relevant
passage and the section structure were read; its regime is not the
positive-real regime needed here, so it was NOT silently substituted
for (9). DLMF supplies the exact imported positive-real asymptotic above.
The Stanley hit `PUBUNIT-4BF2B5664C54337A26C7F5DC` routes the Lagrange
source used in the preceding note; this continuation reads and uses that
note's full residue proof rather than claiming a new full-book reading.

`TOPIC_ROUTE.json` records source classes and exact reading boundaries.
`check_axial_singularities.py` independently checks finite polynomial
coefficients against reciprocal gamma and reflection, includes genuine
zero and cancellation indices, checks envelope convergence without
dividing by trigonometric factors, checks the critical Taylor data and
the path geometry, and preserves all physical scaling symbols. Numerical
checks are regressions, not proofs for the interval of h. The complete
all-real-h proof is (6)–(21). No Lean certification is claimed.
