# Independent audit of the theta/Gamma reference calculation

Date: 2026-09-12. Scope: the exact Gamma measure, its monic polynomials,
the actual theta multiplier, determinant quotients, parameter connection,
and original-coordinate/confluent-jet maps. This report initially records
an independent derivation; the final fragment hash and content-level audit
are appended after the parent finishes the fragment. No zeta asymptotic or
zero-location statement follows from the finite calibrations below.

## 1. The measure and its Fourier transform

For **every real lambda > 0**, retain the measure

    d sigma_lambda(t) = |Gamma(lambda + i t/2)|^2 dt/(2 pi).

The beta integral with r = exp(x) gives

    |Gamma(lambda + i u)|^2
      = Gamma(2 lambda) integral_R exp(i u x)
          [2 cosh(x/2)]^(-2 lambda) dx.

This is the beta integral with its entire Jacobian retained: the original
integrand r^(lambda+i u-1)(1+r)^(-2 lambda) dr becomes
exp(i u x) exp(lambda x)(1+exp x)^(-2 lambda) dx. The last real factor is
[2 cosh(x/2)]^(-2 lambda).

The function f(x) = [2 cosh(x/2)]^(-2 lambda) and its first two derivatives
are integrable, so two integrations by parts make its Fourier transform
integrable. Fourier inversion therefore applies with no distributional
delta substitution. With t = 2u, it yields exactly

    integral_R exp(i y t) d sigma_lambda(t)
      = 2^(1-2 lambda) Gamma(2 lambda) cosh(y)^(-2 lambda).

In particular, the mass is C_lambda = 2^(1-2 lambda) Gamma(2 lambda).
The factor 2 comes from dt = 2 du; it must remain in the measure.

For completeness, f extends holomorphically to |Im x| < pi, using the
branch of its power positive on the real axis. On any horizontal line
strictly inside this strip it decays as exp(-lambda |Re x|). Shifting the
Fourier contour upward or downward by a with 0 < a < pi gives a bound
C_a exp(-a |u|) for its Fourier transform. Thus the displayed transform
extends holomorphically to |Im y| < pi/2. Substitution y = -iv gives

    integral_R exp(v t) d sigma_lambda(t)
      = C_lambda cos(v)^(-2 lambda),  |v| < pi/2.

All polynomial moments exist. Uniform exponential domination on compact
subsets of this strip justifies each derivative and coefficient extraction
used below.

## 2. The generating function, monicity, norms and recurrence

For real z near zero, the proposed generating function satisfies

    F_lambda(z,t)
      = (1-iz)^(-lambda+i t/2) (1+iz)^(-lambda-i t/2)
      = (1+z^2)^(-lambda) exp(t arctan z).

Use the branches analytic at z=0. Multiplying two such functions and using
the preceding moment generating function, together with the exact cosine
addition formula, gives

    integral F_lambda(z,t) F_lambda(w,t) d sigma_lambda(t)
      = C_lambda (1-z w)^(-2 lambda).

Indeed cos(arctan z + arctan w) equals
(1-z w)/sqrt((1+z^2)(1+w^2)); the factors of 1+z^2 and 1+w^2 cancel in
this calculation without changing either original measure or generating
function. The identity holds in a complex neighborhood of (0,0), because
the above domination applies there.

Writing F = sum P_n z^n shows that P_n has leading coefficient 1/n!,
and coefficient extraction gives

    integral P_n P_m d sigma_lambda
      = delta_nm 2^(1-2 lambda) Gamma(n+2 lambda)/n!.

Consequently b_n = n! P_n is monic and its actual squared norm is

    gamma_(n,lambda) = 2^(1-2 lambda) n! Gamma(n+2 lambda).

Differentiation of the same generating function gives

    (1+z^2) partial_z F = (t-2 lambda z) F,

so b_0=1, b_1=t, and, for n>=1,

    b_(n+1) = t b_n - n(n+2 lambda-1) b_(n-1).

These constants, signs, and the factor t/2 in the Gamma argument all agree
with the parent calculation.

## 3. The actual theta weight and all packet roots

The original identity 2xi(s)=s(s-1) pi^(-s/2) Gamma(s/2) zeta(s), evaluated
at s=1/2+it, gives exactly

    a(t) = -pi^(-1/4) (t^2+1/4)
           exp(-it log(pi)/2) zeta(1/2+it),
    |2xi(1/2+it)|^2 dt/(2pi) = |a(t)|^2 d sigma_(1/4)(t).

The sign in a, the factor pi^(-1/4), and its oscillatory phase are retained.
The last equality concerns positive measures; the preceding amplitude
identity retains the corresponding original complex amplitude.

An elementary integrability bound suffices. On Re s>0, s!=1, continuation
of the floor-integral formula from Re s>1 gives

    zeta(s)=s/(s-1)-s integral_1^infinity {x} x^(-s-1) dx.

The integral is absolutely convergent and locally uniformly holomorphic
in this half-plane. On the critical line |s/(s-1)|=1 and |{x}|<=1 give

    |zeta(1/2+it)| <= 1 + 2 sqrt(t^2+1/4).

Thus |a(t)| is bounded by a polynomial of degree three. The Gamma
exponential moments prove the finiteness of every actual theta moment.

For a monic packet h of degree d whose complete multiplicities occur among
the zeros of g=2xi, g/h is the entire canceled quotient. The line amplitude
is a(t)/h(1/2+it); at a critical packet root this notation means its unique
analytic germ after cancellation, equivalently (g/h)(1/2+it) divided by
the nonvanishing Gamma factor. No root or repeated jet is removed from
the finite packet algebra. Outside a sufficiently large compact interval,
|h(1/2+it)| is bounded below by a positive constant times |t|^d. On the
remaining compact interval the canceled quotient is continuous. Therefore
all packet-weight moments exist as well. The nonzero entire function g/h
has only isolated zeros; its line density is positive almost everywhere.
Every finite Gram matrix of linearly independent polynomials is positive
definite, including packets containing critical multiple zeros.

## 4. Every determinant constant

Put e_j=b_j/sqrt(gamma_j). This is a specified invertible diagonal change
from the original monic family; the original gamma_j remain in the norm
formula. For either actual density w=|a|^2 or packet density
w=|a/h(1/2+it)|^2, let

    J_N[i,j] = integral conjugate(e_i(t)) e_j(t) w(t) d sigma_(1/4)(t),
    D_N = det J_N,  D_(-1)=1.

Let M_N be the corresponding monomial Gram matrix. The coefficient matrix
of e_0,...,e_N has determinant product_(j=0)^N gamma_j^(-1/2). Hence

    D_N = det M_N / product_(j=0)^N gamma_j.

Completing the square for a monic degree-n polynomial, or taking the Schur
complement of M_(n-1) in M_n, proves its minimal squared norm is
det M_n/det M_(n-1). Positivity proved above makes every denominator
nonzero. Consequently, for all n>=0,

    norm_n = gamma_n D_n/D_(n-1).

The actual theta norm is mathfrak h_n; the packet norm is kappa_n, using
the corresponding D sequence separately. For the original theta measure,

    mathfrak h_(n+1)/mathfrak h_n
      = (n+1)(n+1/2) D_(n+1)D_(n-1)/D_n^2.

The same formula holds for packet kappa with its own determinant sequence.
No equality between those two determinant sequences is assumed.

## 5. Parameter connection with every lower coefficient

The exact generating identity is

    F_(1/4)(z,t)=(1+z^2)^(1/2) F_(3/4)(z,t).

Coefficient extraction yields

    b_n^(1/4) = sum_(k=0)^floor(n/2)
      [n!/(n-2k)!] binom(1/2,k) b_(n-2k)^(3/4).

Multiplication by (1+z^2)^(-1/2) gives the inverse formula with
binom(-1/2,k). These finite triangular maps have diagonal entries one,
are inverse in every finite degree, and retain every lower-degree term.

## 6. Original coordinates, monic phases and complete confluent jets

The algebra isomorphism is

    Psi:C[s] -> C[t],  Psi(p)(t)=p(1/2+it).

On the monic degree-n affine space the monic polynomial is i^(-n)Psi(p).
The degree-dependent phase must not be called a linear map on all C[s]:
the linear map is Psi, with separate diagonal phases on a chosen monic
basis. If c_s and c_t are monomial coefficient vectors of degree at most
N, then c_t=A_N c_s, with

    A_N[l,j] = binom(j,l) (1/2)^(j-l) i^l  (l<=j),
    A_N[l,j] = 0  (l>j).

For the same measure expressed on the line, M_s=A_N^* M_t A_N and
|det A_N|=1. Thus the affine translation and phases preserve the monic
norms while every original Gram entry is retained by this congruence.

For a root rho of multiplicity m, set t_rho=-i(rho-1/2). For every retained
normalized derivative 0<=j<m,

    (Psi p)^[j](t_rho)=i^j p^[j](rho).

If R_s and R_t are the full confluent monomial-evaluation matrices, and
D_jet has entries i^j for every such row, then

    R_t A_N = D_jet R_s,
    K_t = D_jet K_s D_jet^*,
    K_s = R_s M_s^(-1) R_s^*, K_t = R_t M_t^(-1) R_t^*.

The second formula follows by inverting the full Gram congruence. No
diagonal-only approximation occurs.

The monic transformed packet is h_t=i^(-d)Psi(h), so Psi(h)=i^d h_t.
Consequently Psi induces the algebra isomorphism C[s]/(h) -> C[t]/(h_t).
On coefficient vectors of degree below d this is A_(d-1). If S_h and T_h
are the original s and t multiplication matrices, respectively, then

    A_(d-1) S_h = (1/2 I+i T_h) A_(d-1).

For every original polynomial unit u modulo h, its multiplication matrix
is carried to multiplication by Psi(u) modulo h_t through the same exact
conjugacy. The denominator replacement h_line -> h_t changes the
amplitude g/h_line by the retained phase i^d. Equality of norms follows
from its modulus one; no claim of equality of the two amplitudes is made.

## 7. Independent finite calibration

Script: `checks/theta_gamma_reference_independent.py`.

The script performs **344 exact checks** over rational polynomial data:
lambda=1/4, 3/4 and 5/4; monic degrees 0 through 10; all corresponding
orthogonality pairs; both complete parameter connections; a positive
polynomial weight (1+t^2)^2 through degree 6; every determinant/norm
quotient; original s Gram congruences; complete confluent evaluation and
kernel maps; the finite packet generator and polynomial-unit conjugacy;
and analytic cancellation of a double critical calibration root together
with a four-point off-line conjugation/reflection orbit.

These calibration roots are expressly not claims about roots of xi. The
moments in the checker are divided by C_lambda with this exact original
mass explicitly recorded; multiplying back restores every original norm.

Normal and optimized Python runs both pass 344/344 checks. The negative
control changes only the expected sign of the lambda=1/4, degree-one norm;
normal and optimized negative runs both exit 1 and report exactly that one
failed equality. Results use explicit conditions and remain active under
`python -O`.

Receipts:

- `checks/theta_gamma_reference_independent.json`
- `checks/theta_gamma_reference_independent_optimized.json`
- `checks/theta_gamma_reference_independent_negative.json`
- `checks/theta_gamma_reference_independent_negative_optimized.json`

The analytic identities in Sections 1–6 were independently derived above.
The finite checks supplement those proofs and do not assert an actual
theta determinant asymptotic or a zero-location result.

## 8. Content-level audit of the parent fragment TG.1–TG.28

The complete fragment `tex/theta_gamma_reference.tex` was read after its
first full draft was written. The following checks refer to its actual
equations and proof text, not to a task description.

- **TG.1–TG.6:** the original theta amplitude and exact sign, phase and
  constant agree with Section 3 above. Both weighted multiplication maps
  are onto the stated L2 spaces; the inverses are well-defined equivalence
  classes off discrete null sets. The diagram through multiplication by
  the unchanged h is exact. Entire cancellation at critical packet roots
  is specified before forming the weight.
- **TG.7–TG.14:** the beta Jacobian, Fourier inversion constants, contour
  shift direction and strip width, generating integral, derivative
  domination, monic factors, squared norms, and recurrence signs agree
  with the independent derivation. For positive u, shifting the x contour
  upward gives exp(-cu), as stated. The t=2u Jacobian gives the factor two
  in the Fourier transform and sqrt(2) at lambda=1/4.
- **TG.15–TG.19:** both B and J metrics are retained by full invertible
  congruence. The direct floor-integral bound supplies integrability.
  The determinant norm proof preserves the original monic s-to-t phase.
  The ratio r_m uses gamma_(d+m)/gamma_m with precisely the factorial and
  Gamma quotient displayed in TG.18. Its m=0 case uses D_(-1)=1. The
  allowance in TG.19 follows from KL.32 with the original theta norm
  quotient, under exactly the two packet symmetries stated there.
- **TG.20–TG.22:** the phase congruence is Delta* B Delta because the
  inner product conjugates its first argument. Inverting T* B T=diag(kappa)
  gives B^(-1)=T diag(kappa^(-1)) T*, so the entire remainder kernel
  C B^(-1) C* is exactly the earlier kernel, including off-diagonal
  entries and repeated jets. Direct comparison with KL.27 confirms that
  the metric is G_(N-d), including N=d-1 giving the original G_(-1).
  The unit placement U_epsilon* K^(-1) U_epsilon is unchanged. The
  normalized derivative factor in TG.22 is i^(j-ell), as required.
- **TG.23–TG.24:** both finite parameter maps have inverse unit-triangular
  coefficient matrices. The full Gram and jet transformations give the
  same kernel. The separate Hilbert-space map uses the displayed Gamma
  quotient; its exact norm and inverse follow by cancellation of its
  squared modulus, with the polynomial map retaining its different
  stated domain and codomain.
- **TG.25–TG.28:** the source theorem's printed hypotheses were checked
  against the locally downloaded primary PDF, printed pages 67–70
  (`lms_full_page3.png` through `lms_full_page6.png`). Definition 2.1
  permits every alpha>0, including alpha=1. Theorems 2.3 and 2.4 have
  the indicated full-weight requirements. The local zero form implies
  positive-measure intervals on which the amplitude ratio is arbitrarily
  small. The logarithmic estimate has the correct inequality direction:
  division of a negative upper bound by Q(t)<=Q(T_j)+1 makes that bound
  at most -j. Thus changing only a null set of values does not repair
  either displayed hypothesis. This argument uses Hardy's established
  infinite-critical-zero theorem as the explicitly identified literature
  input; it does not claim a new proof of Hardy's theorem. It applies
  to the displayed hypotheses, and does not rule out the broader variants
  mentioned after Theorem 2.4 or other asymptotic methods.

The Romik section-3 opening and Appendix A.2 were also read from the
downloaded primary text. They use P_n^(3/4)(x;pi/2), with the xi expansion
evaluating x=t/2, exactly as retained in TG.23. The cited DLMF formulas
were checked in the downloaded primary pages; the independently derived
constants agree after the explicitly retained t=2x and n! factors.

One presentational correction was reported to the parent: TG.15 contained
the literal text `,quad` in place of `,\quad`. No mathematical correction
to TG.1–TG.28 was needed. The parent's correction is present in the
reviewed source bytes, whose SHA256 is
`008fb6b2688a8052800c04834cc810674446a3c3d4ae6ff5f8dc5cf4dbfadacf`.
This review applies to exactly that fragment. The parent is still writing
the source-route inventory, so this review does not certify the separate
publication package or the existence of every referenced route file.
