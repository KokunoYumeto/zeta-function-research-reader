# Actual Taylor-unit gauge: analytic pole classes and their connection

13 September 2026. This continues UG1--19 on the original arithmetic packet.
The cumulative-reader owner supplied the exact weighted-residue sequence and
the connection on simple-pole lifts. This note proves those constructions in
full, calculates their entire finite scaling transport and dual, and compares
them with the already proved formal contraction. It does not substitute a new
source, a new metric, a simple-root packet, or an assumed arithmetic bound.

## 1. Original input and the fixed nonzero-parameter complex

Keep the monic polynomial h of degree d>0 with every selected actual zero order,
g=2 xi, and the unique polynomial nu of degree less than d representing the
complete Taylor unit upsilon_h=j_h(g/h). Thus gcd(h,nu)=1, and no factor of h
or Taylor coefficient of its unit has been removed. Let P_nu be the set of
distinct zeros of nu, and r its cardinality; r=0 when nu is constant. The
multiplicities of nu are retained in nu itself throughout the gauge.

Fix the original primitive Phi with Phi'=h and its specified additive constant.
For u in C* and t in C define

    D = u d/ds + h(s)-t,
    w(s;u,t) = exp((Phi(s)-t s)/u),
    B = C[s],    B_loc = C[s,nu^-1],    M = B_loc/B.                 (AP1)

Use complexes [B --D--> B ds] and [B_loc --D--> B_loc ds] in degrees 0,1.
The equation w D F = u (w F)' is literal, with the constant in Phi retained.
Although w is entire and nowhere zero in s, it is not asserted rational.
The quotient M consists exactly of finite sums of principal parts at P_nu:
partial fractions gives existence and uniqueness, with the polynomial part
discarded only in this explicitly specified quotient.

## 2. The entire additional pole cohomology is calculated

Define, for [F] in M,

    Res_w[F] = (Res_{s=p} w(s) F(s) ds)_{p in P_nu}.               (AP2)

Adding a polynomial changes none of these residues. Also Res_w D=0 by AP1,
since a derivative of a meromorphic Laurent series has zero residue.

The exact sequence is

    0 --> M --D--> M --Res_w--> C^{P_nu} --> 0.                   (AP3)

Here is a proof of every assertion. If F has pole order n>=1 at p and leading
term c(s-p)^(-n), D F has leading pole term -u n c(s-p)^(-n-1).
Multiplication by h-t has pole order at most n, so it cannot cancel this term.
Thus D[F]=0 in M implies that F has no poles, and [F]=0. This proves injectivity.

For each p, the rational function 1/(w(p)(s-p)) has residue vector equal to
the p-th coordinate vector. It is analytic at every other point of P_nu.
This proves surjectivity without suppressing the factor w(p).

Suppose Res_w[F]=0. In a disk at p containing no other point of P_nu, the
Laurent series of wF has finitely many negative terms and no (s-p)^(-1) term.
Integrating term by term therefore gives a meromorphic primitive H_p, with
no logarithm. Put Q_p=H_p/(u w). Then D Q_p=F locally. Let Q be the rational
function obtained by summing the finite principal parts of the Q_p at all p.
The difference Q-Q_p is holomorphic at p, so DQ-F is holomorphic there.
This rational function has no other possible finite poles, hence is a
polynomial. Therefore D[Q]=[F] in M, which proves exactness in the middle.
Changing any integration constant changes only a holomorphic local function
and does not change this construction of the principal part.

All higher pole orders are explicitly observed, rather than ignored:

    Res_p w(s)/(s-p)^n ds = w^{(n-1)}(p)/(n-1)!,
    D(s-p)^(-n) = -u n(s-p)^(-n-1)
       + sum_{j=0}^d h^{(j)}(p)/j! (s-p)^(j-n) - t(s-p)^(-n).     (AP4)

These formulas give the triangular reduction of each higher pole while
retaining every derivative of h and every derivative of w that contributes.
They explain why there is one quotient coordinate per distinct pole point;
they do not replace h by its radical or discard its nilpotent zero jets.

## 3. The original arithmetic classes inject into the analytic extension

The polynomial complex has H^0=0 and H^1 of dimension d, with basis
1,s,...,s^(d-1). Indeed, for a nonzero polynomial of degree n, the highest term
of DF has degree n+d, with unchanged leading coefficient. Successive subtraction
of such leading terms reduces every polynomial uniquely to degree less than d.
Write this unchanged remainder module as H_pol.

The same highest-pole argument shows H^0 of the localized complex is zero:
a rational solution of DF=0 has no finite pole, and then the preceding
polynomial argument applies. The short exact sequence of the three complexes,
together with AP3, gives

    0 --> H_pol --i--> H_loc --Res_w--> C^{P_nu} --> 0.            (AP5)

One can check injectivity without a long exact sequence. If a polynomial F
equals DQ for rational Q, the leading-pole calculation forces Q to be a
polynomial. Thus no original polynomial cohomology class becomes a boundary.
The kernel and surjectivity assertions follow from AP3 by subtracting DQ
and retaining the resulting polynomial.

An explicit basis of H_loc is

    1,s,...,s^(d-1),    r_p=1/(s-p) for p in P_nu.                (AP6)

For existence, subtract sum_p (Res_w F)_p r_p/w(p). The remainder has zero
weighted residues, and AP3 reduces it modulo D to a polynomial, then to
degree less than d. For independence, applying AP2 to a linear combination
forces every pole coefficient to vanish because w(p)!=0; injectivity in AP5
then gives independence of the polynomial coefficients. Hence dim H_loc=d+r.
The original d-dimensional arithmetic fibre, with all repeated roots of h,
is present as the explicitly injected summand of this vector-space basis.

## 4. Actual parameter connection and both explicit residue frames

The differential operator L=u d/dt-s commutes with D:

    [u d/dt,D]=-u,    [-s,u d/ds]=u,    [-s,h-t]=0.               (AP7)

It therefore descends as a connection operator on the analytic family over
C* x C, not as an unsupported multiplication endomorphism on the fixed
de Rham quotient. Let A(t) be the original companion matrix of h-t in the
polynomial frame, and let e_0 be its constant-polynomial column. Set

    P=diag(p)_{p in P_nu},    B_0=(e_0 ... e_0),
    A_ext(t) = [ A(t)  B_0 ; 0  P ].                            (AP8)

Here each pole basis vector satisfies the exact identity

    L r_p = -s/(s-p) = -p r_p-1.                               (AP9)

For the last polynomial vector, reduction of s^d uses D(1)=h-t, so the
polynomial block is exactly the already specified A(t), without a derivative
correction. Thus in the full frame AP6 the connection is

    L = u d/dt - A_ext(t).                                     (AP10)

All coefficients depend holomorphically on (u,t) for u!=0. In fact A_ext
itself has no singular u coefficient; this statement about the matrix does
not identify its rank-(d+r) frame with the formal cohomology at u=0.

Put W=diag(w(p;u,t)). The residue map in AP6 is the rectangular matrix

    Res_w = [0 W],    u dW/dt = -P W.                          (AP11)

For parameter-dependent representatives direct differentiation proves

    u d/dt Res_w[F] = Res_w[(u d/dt-s)F].                      (AP12)

Thus the quotient connection in weighted-residue coordinates is u d/dt.
The ordinary simple-pole coefficients instead have u d/dt-P. Their exact
transition is multiplication by W, not deletion of an exponential phase.

For completeness use the second frame r_p/w(p). Its residue coordinates
are the standard coordinate vectors, and

    L(r_p/w(p)) = -1/w(p).                                    (AP13)

The pole diagonal becomes zero while its coupling to the original polynomial
class is -e_0/w(p). This is the same connection under the explicit diagonal
frame map diag(I_d,W^-1); no factor has been set to one in the original frame.

## 5. Entire finite scaling and its retained extension term

Let C_a(u,t) be the original polynomial scaling transport, satisfying

    dC_a/da = -C_a A(t+ua),    C_0=I_d.                        (AP14)

It is the previously proved entire solution, including its full higher terms.
Define an integral along the straight segment from 0 to a in the complex
a-plane (equivalently the primitive of its entire integrand):

    K_a = - integral_0^a C_b(u,t) B_0 exp(-(a-b)P) db,
    C_ext,a = [ C_a K_a ; 0 exp(-aP) ].                        (AP15)

Differentiating the integral gives K'_a=-C_a B_0-K_a P and K_0=0.
Consequently

    dC_ext,a/da = -C_ext,a A_ext(t+ua),    C_ext,0=I_(d+r).      (AP16)

Existence and uniqueness for this finite polynomial-coefficient matrix ODE
prove that these are the actual entire finite connection transports. The
block integral retains the coupling into the original polynomial class.
Both diagonal blocks are invertible, and the inverse has upper-right block
-C_a^-1 K_a exp(aP). The groupoid law is

    C_ext,a(u,t) C_ext,b(u,t+ua) = C_ext,a+b(u,t).               (AP17)

It follows either by the shifted ODE and uniqueness, or from the commuting
operator's formal flow exp(aL)F=e^(-as)F(u,t+ua,s). The latter is coefficientwise
in a when F is rational; no claim that e^(-as)F is itself a rational function
at a nonzero complex a is needed. The finite matrix ODE supplies its entire
cohomological continuation.

The residue quotient has the exact transport identity

    [0 W(u,t)] C_ext,a(u,t) = [0 W(u,t+ua)],                    (AP18)

because w(p;u,t+ua)=w(p;u,t)e^(-ap). In weighted residues the entire action
is parameter translation; in the unchanged simple-pole frame the factor
e^(-ap) remains. The exponentials and their polynomial extension K_a are
both displayed, including the case when p is not real.

## 6. Small-loop periods, the actual unit gauge and dual maps

For a positively oriented small circle gamma_p enclosing only p, the exact
additional period is

    integral_{gamma_p} wF ds = 2 pi i (Res_w F)_p.              (AP19)

Thus the extra periods are concrete loops, with their orientation and 2 pi i
factor retained. Every original polynomial image has zero such loop period.
For any original rapid-decay contour avoiding P_nu, the incoming polynomial
period is still its old integral, with its original ray orientation and phase.

Choose the finite parts of the original d rapid-decay contours to avoid every
point of P_nu, including zero when zero belongs to that set. Such detours leave
their polynomial integrals unchanged, since those integrands are entire.
Different detours for a rational integrand can add the small loops AP19; those
are retained rows, not discarded contour ambiguities. At infinity w has the
same decay on the specified rays as in the original polynomial period proof,
and the simple-pole functions are O(1/s), so all new integrals converge. On
compact parameter subsets in an admitted u-sector and bounded t, the negative
leading exponential dominates the lower terms and justifies differentiation.

In the unchanged AP6 frame these d contours followed by the r small loops give
the full period matrix

    Pi_ext = [ Pi_pol V_pole ; 0 (2 pi i) W ],
    det Pi_ext = det Pi_pol (2 pi i)^r product_p w(p).            (AP19a)

Pi_pol is the original full polynomial period matrix, whose nonzero determinant
was proved by the monomial ray matrix and coefficient-connection transport.
Hence AP19a is invertible: it realizes all d+r analytic classes and all their
loop periods. Integrals of D-exact forms vanish at the decaying endpoints or on
closed loops. Differentiating with t therefore gives

    dPi_ext/dt = -Pi_ext A_ext(t)/u,
    C_ext,a = Pi_ext(u,t)^-1 Pi_ext(u,t+ua).                     (AP19b)

The second identity follows from the same ODE and initial value as AP16, for
fixed nonzero u in the admitted sector. No period matrix is evaluated at u=0.

On the same localized complex define the actual gauge differential

    D^nu=nu D nu^-1=u d/ds+h-t-u nu'/nu.                       (AP20)

The cochain map is multiplication by nu in both degrees. Its inverse is
multiplication by nu^-1 in B_loc. The target weight is w/nu, and the identities

    (w/nu)D^nu F = u ((w/nu)F)',
    (w/nu)(nu F)=wF                                           (AP21)

show exact equality of every small-loop and every old rapid-decay period
under this map. The target extra class nu/(s-p) need not have a pole as a
rational function; its weighted form (w/nu)nu/(s-p)=w/(s-p) retains the pole.
The original image is nu times H_pol, not the unmodified polynomial frame.

The ordinary algebraic dual of AP5 is the exact sequence

    0 --> (C^{P_nu})* --Res_w^T--> H_loc* --i^T--> H_pol* --> 0. (AP22)

In AP6 the injected column for alpha is (0,W^T alpha). The dual connection
is d/dt+A_ext(t)^T/u. Its action on that column is (0,W^T alpha'):
the derivative -P W/u cancels P W/u, and the upper block is zero.
Thus the loop-functional injection is explicitly horizontal for the trivial
weighted-residue dual. Under the gauge the dual is the inverse transpose of
multiplication by nu. This statement concerns the ordinary linear dual; the
previous tau-base dagger and moment-line dual retain their separate, already
calculated conjugation and weight-line maps. No positive pairing is inferred
from AP22, and no original inverse Taylor unit is replaced by nu on a dual.

## 7. Exact relation to the formal contraction, including the endpoint

UG uses C[s][[u,t]] and C[s,nu^-1][[u,t]], with coefficientwise completion.
On the added pole module h is invertible because gcd(h,nu)=1. Writing H
for this inverse and E=u d/ds-t, its exact formal inverse is the ordered
sum sum_{n>=0}(-HE)^n H. That is the contraction proved in UG. AP3 instead
fixes u!=0 first and calculates a cokernel of dimension r, nonzero when r>0.
For constant nu, r=0 and the additional pole complex and its residue map are
zero; localization adds no analytic or formal classes in that case.

The two operations are related by the original rational complexes and the
localization arrow, but the formal completion has no evaluation homomorphism
at an arbitrary nonzero complex u. A formal coefficient sequence may diverge
there. Thus the previously displayed formal contraction is not evaluated to
claim that AP3's residue classes vanish. AP3 gives exactly the missing cokernel.

There is a concrete endpoint calculation. For p in P_nu, gcd(h,nu)=1 gives
h(p)!=0. At u=t=0 the class of 1/(s-p) modulo h is the original polynomial
class

    [1/(s-p)] = -[(h(s)-h(p))/((s-p)h(p))] in C[s]/(h).         (AP23)

Indeed multiplying the displayed polynomial by s-p gives 1-h(s)/h(p).
This is the literal inverse of s-p in the original algebra, with every jet
of h retained. For formal u,t before the endpoint, D(1/(s-p)) gives

    (h(p)-t)[1/(s-p)] =
        u[1/(s-p)^2] - [(h(s)-h(p))/(s-p)].                    (AP24)

The successive higher-pole relations AP4 and ordered formal inverse supply
the remaining u,t coefficients. AP23 is not a rank-(d+r) basis at u=0.
It explicitly describes how these rational lifts are represented in the
original rank-d formal fibre.

The weighted residue factors also retain their parameter behavior:
w(p)=exp((Phi(p)-tp)/u). At fixed t with Phi(p)-tp!=0 this has an essential
singularity at u=0. If that numerator vanishes, that particular value is one;
its exact derivative is always u d_t w(p)=-p w(p). For p=0, w(0) is independent
of t: it is identically one when Phi(0)=0, and is exp(Phi(0)/u) otherwise.
Thus no universal singularity or t-dependence is asserted for every residue
coordinate. Even when w(p)=1, AP4 on higher pole orders uses w^{(n)}(p), whose
highest inverse-u term is w(p)(h(p)-t)^n/u^n. Because h(p)!=0, these contain
unbounded inverse-u powers as the pole order increases near t=0. Consequently
when r>0, AP2 does not define a coefficientwise continuous residue map on UG's
completed pole module. For r=0 its zero map is of course continuous. The
obstruction to evaluating the nonzero-pole formal contraction is not
replaced by a false assertion that every individual loop factor is singular.

There is also an exact map for the entire displayed endpoint matrix. Let Q_0
have p-th column the polynomial in AP23, expressed in the original degree-d
frame, and put J_0=[I_d Q_0]. Direct multiplication of AP23 gives

    A Q_0 = B_0+Q_0 P,
    J_0 A_ext(0) = A J_0,
    ker J_0 = {(-Q_0 c,c):c in C^r}.                           (AP25)

The map c -> (-Q_0 c,c) carries P to A_ext(0), by the first identity. Thus the
endpoint has an explicit invariant r-dimensional kernel and the original
arithmetic quotient, rather than an unexplained rank comparison. Entire matrix
exponentiation yields

    J_0 C_ext,a(0,0) = exp(-aA) J_0.                           (AP26)

Here C_ext,a(0,0)=exp(-a A_ext(0)) is the matrix specialization of AP16; J_0
then maps it to actual formal-fibre cohomology. Multiplication by the full unit
upsilon_h after J_0 gives the gauge endpoint. It commutes with A since that
unit is an element of the original algebra, so the same action diagram holds.
The endpoint comparison therefore retains the full unit as well as all jets.

Completed scope: the original arithmetic polynomial cohomology injects into
the analytic localization; all additional pole periods, their connection,
finite scaling, unit-gauge image and linear dual are calculated. The formal
and analytic constructions retain their exact common maps and different
coefficient operations. This does not supply a uniform theta-norm bound or
an arithmetic Frobenius comparison not constructed in these equations.

## Provenance and verification scope

Input proof: ACTUAL_TAYLOR_UNIT_FORMAL_GAUGE.md, SHA256
9ded2486160b76bf65f92d44b73cdd0c59a3ca7e5334f88682e10592d5a45b2f.
Original scaling proof after the accepted integer-power-map clarification:
../f1_scaling_frobenius/ACTUAL_TAU_SCALING_AND_EXPONENTIAL_FLOW.md, SHA256
4e4cb66e3cbbff6379ae389ddaaad65045ac0ed380f17a87ac7c4241c45e6c08.
The cumulative-reader owner supplied AP3's local-primitive construction and
AP8--AP13's exact connection in coordinated messages. Root supplied this full
written continuation, AP15--AP18's entire extension transport, AP22's explicit
dual and AP23--AP24's endpoint comparison. The independent reviewer supplied
the determinant extension AP19a and the endpoint intertwiner AP25--AP26;
root incorporated their full proofs and fixed the review's p=0 residue-factor
exception explicitly. No remote publication of this new
note, new Lean execution, or certified arithmetic-zero computation is claimed.
