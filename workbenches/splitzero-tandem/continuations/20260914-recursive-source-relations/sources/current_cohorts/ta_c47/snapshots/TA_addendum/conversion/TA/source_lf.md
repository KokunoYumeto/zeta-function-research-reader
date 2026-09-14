# Which analytic pole classes belong to the original theta source?

13 September 2026. This is the next calculation after AP1--26. It keeps the
original one-factor arithmetic source, its Mellin measure and mass, and computes
both its Hilbert admission and its strong-Schwartz admission. The resulting
complexes, their residue images, their exact source maps and their theta-boundary
defects are displayed. No freely chosen metric or hypothetical zero replaces
the arithmetic input.

## 1. Original source, fixed parameters, and the exact norm

Retain the full actual packet h of degree d>0, g=2 xi, the entire function
v_h=g/h, and the original F_h in the strong Schwartz source B with Mellin
transform v_h. Retain the complete Taylor-unit polynomial nu representing
upsilon_h=j_h(g/h); gcd(h,nu)=1. Let P_nu be its distinct roots. At every
p in P_nu put m_p=ord_p v_h, a finite nonnegative integer. Since h(p)!=0,
this is exactly ord_p g, not a multiplicity of nu or a presumed simple zero.

Use s for the Mellin coordinate and y for its critical-line imaginary part.
The independent geometric parameters are u in C* and t in C. Distinguish

    D_x=-x d/dx,    D_exp=u d/ds+h(s)-t,    L=u d/dt-s.          (TA1)

On rational coefficients R in C[s,nu^-1], the stipulated original Hilbert norm is

    ||V_h,rat R||^2
       = (1/(2 pi)) integral_R |v_h(1/2+iy) R(1/2+iy)|^2 dy.    (TA2)

When finite, inverse Mellin on this line defines V_h,rat R in L^2(R_+,dx).
Indeed logarithmic coordinates x=e^z turn F(x) into e^(z/2)F(e^z), whose
Fourier Plancherel identity is precisely TA2. No total mass is divided out.
For polynomial R this is exactly R(D_x)F_h, the original source map.

## 2. Complete Hilbert admission, including zeros on the observation line

Partition P_nu into O={p:Re p!=1/2} and C={p:Re p=1/2}. Let PP_p^{<=n}
be the span of (s-p)^(-1),...,(s-p)^(-n), and PP_p the union over n.
The zero bound n=0 means the zero space, not a discarded supported point.

The rational coefficients of finite TA2 norm are exactly

    A^1 = C[s] + direct_sum_{p in O} PP_p
                 + direct_sum_{p in C} PP_p^{<=m_p}.           (TA3)

To prove necessity at p=1/2+iy_p, write v_h(s)=(s-p)^m_p a(s),
where a(p)!=0, and R(s)=(s-p)^(-n)c(s), where c(p)!=0. Along the line,
the squared modulus is bounded above and below by positive constants times
|y-y_p|^(2(m_p-n)) near p. Its integral is finite exactly when
2(m_p-n)>-1, or, because the orders are integers, n<=m_p. The leading
coefficient cannot be cancelled by principal parts at another point.

There are no local line singularities from O. Outside a fixed compact interval,
any rational R has at most polynomial growth. The actual Mellin transform v_h
is rapidly decreasing on every vertical strip, as follows from F_h in B;
equivalently its gamma decay gives more than the required line decay.
Thus every coefficient described in TA3 has finite norm, proving sufficiency.

The exact domain making D_exp an admitted differential is

    A^0 = D_exp^-1(A^1)
        = C[s] + direct_sum_{p in O} PP_p
          + direct_sum_{p in C} PP_p^{<=max(m_p-1,0)}.           (TA4)

For a pole of order n>=1, D_exp R has the uncancellable leading pole
-u n c(p)(s-p)^(-n-1). Hence at a line point its image is admitted exactly
when n+1<=m_p. A polynomial has polynomial image and is always admitted.
This proves TA4 and also A^0 subset A^1 without any extra domain assumption.

The two-term complex [A^0 --D_exp--> A^1 ds] is consequently the original
norm-admitted subcomplex of AP's analytic localization at fixed u!=0.
This is a graph-domain calculation, not an assertion that all finite-norm
coefficients form a differential-invariant space in both degrees.

## 3. Its entire cohomology and exact inclusion into the analytic family

Put S=O union {p in C:m_p>=1} and Z={p in C:m_p=0}.
Use the actual weight w=exp((Phi(s)-ts)/u), with Phi'=h and its original
constant. AP's exact residue map restricts to give

    0 --> H_pol --> H^1(A) --Res_w--> C^S --> 0,                (TA5)
    0 --> H^1(A) --> H_loc --Res_w|_Z--> C^Z --> 0.             (TA6)

Here H^0(A)=0, and a basis of H^1(A) is the original polynomial basis
1,s,...,s^(d-1), followed by 1/(s-p) for p in S.

For full proof, the highest-pole argument makes D_exp injective on rational
functions, followed by its leading-degree argument on polynomials. If an
admitted F equals D_exp Q in the larger localized complex, TA4 forces Q to
belong to A^0. Thus the induced map on H^1 has no kernel. Subtract from an
admitted F its weighted residues using (Res_w F)_p/(w(p)(s-p)) for p in S.
At a point with bound m_p, AP's log-free local primitive then has pole order
at most m_p-1. Its sum of principal parts belongs to A^0. Subtracting its
D_exp image leaves a polynomial and proves the kernel assertion in TA5.
Those simple-pole lifts prove surjectivity. Independence follows by residues
and then polynomial cohomology. Finally AP's full residue decomposition shows
that precisely the classes with zero Z-residues have such representatives,
proving TA6.

All original m_p occur in the two chain spaces and in their local primitive
maps. One coordinate per admitted point is the computed cohomology, not a
replacement of the original zero orders by one.

Because L does not increase finite pole order and commutes with D_exp, it
preserves A^0 and A^1. Its connection on TA5 is exactly the submatrix of AP:

    L = u d/dt - [ A(t) B_S ; 0 diag(p)_{p in S} ],             (TA7)

where each column of B_S is the original constant-polynomial column. Its
weighted-residue factors w(p), its entire upper-right scaling integral and
its oriented 2 pi i loop periods are the corresponding AP formulas restricted
to S. No new connection or residue scaling is chosen.

## 4. Strong-Schwartz admission is an actual full-zero packet construction

The original source is

    B={F smooth on R_+: sup_{x>0} x^b |D_x^j F(x)|<infinity
                             for every integer b and j>=0}.   (TA8)

Its Mellin transforms are entire: for s in a compact set the bounds at zero
and infinity dominate the integral and all its logarithmic derivatives.
Therefore V_h,rat R can belong to B only when every finite pole of v_h R
is removable, at all p in P_nu, not just on the observation line. Agreement
of its entire Mellin transform with v_h R on a nonsingular segment of the
critical line extends to the connected punctured plane by the identity theorem,
which proves the necessity of the removable-pole assertion.

Define the actual polynomials

    S_B={p in P_nu:m_p>0},
    kappa(s)=product_{p in S_B}(s-p)^m_p,
    kappa_0(s)=product_{p in S_B}(s-p)^(m_p-1),
    b(s)=kappa/kappa_0=product_{p in S_B}(s-p),
    c(s)=sum_{p in S_B}(m_p-1)b(s)/(s-p),
    H(s)=h(s)kappa(s).                                         (TA9)

Empty products equal one and the empty sum is zero. These are products of
the specified monic factors, not renormalizations of an arbitrary leading
coefficient. Since gcd(h,nu)=1, the roots of h and kappa are disjoint.
H therefore selects only actual zeros of g, retaining their complete orders.

All entire-admitted rational coefficients are exactly kappa^-1 C[s].
This follows either from partial fractions with the full order bounds, or
by multiplying by kappa: the resulting rational function has no finite poles
and is polynomial. Conversely P/kappa has at most the prescribed orders.

Sufficiency for the original B follows through its existing Euler inverses,
without a new space-identification assumption. Apply the original S_rho
inverses successively to Theta phi_* through every full factor of H. At each
step the remaining Mellin zero supplies the required kernel condition. Their
already proved source map gives F_H in B with Mellin transform g/H. Therefore

    V_h,rat(P/kappa)=P(D_x)F_H,
    M(P(D_x)F_H)=gP/H=v_h P/kappa.                             (TA10)

Every term on the right is an original strong-Schwartz theta-source vector.
This proves the converse and the exact source realization, not merely finite
norm. The differential graph domain of this strong-source degree-one space is
kappa_0^-1 C[s], by the same highest-pole calculation as TA4 at every p.

Thus the strong-source complex is the explicit subcomplex

    [ kappa_0^-1 C[s] --D_exp--> kappa^-1 C[s] ds ].             (TA11)

It injects into the Hilbert-admitted and full analytic cohomologies with no
extra kernel, by the same D_exp-preimage proof. Its residue image is exactly
C^{S_B}. In particular a nu-root off the critical line with m_p=0 is admitted
by the Hilbert norm but not by B; its exact omitted coordinate is its AP residue.

## 5. Polynomial coordinates, source maps and every retained boundary defect

Use the literal maps Q -> Q/kappa_0 in degree zero and P -> P/kappa in
degree one. They carry TA11 to a polynomial complex with differential

    E(Q)=kappa D_exp(Q/kappa_0)
        =u b Q' + [b(h-t)-u c]Q.                              (TA12)

The quotient kappa_0'/kappa_0=sum_p(m_p-1)/(s-p) proves this identity with
all orders and the negative derivative term retained. Since b and h are the
specified monic polynomials, the leading term of E(Q) has degree
deg Q+d+|S_B| and unchanged leading coefficient. Every other term has lower
degree. Thus E is injective and its cokernel has the unique polynomial basis
of degrees less than d+|S_B|, by terminating leading-term reduction.

The original polynomial exponential complex maps into it by the exact square

    C[s] --------D_exp-------> C[s]
      | multiplication kappa_0   | multiplication kappa
      v                           v
    C[s] ----------E----------> C[s],

    E(kappa_0 Q)=kappa D_exp Q.                                (TA13)

Leibniz differentiation proves this directly, or use the denominator maps.
The original arithmetic source is carried identically, since
V_h,rat((kappa P)/kappa)=P(D_x)F_h. No map here sends supported zero to tau
or changes the base point; lift each displayed linear map on its original mask.

There is also an exact arithmetic-quotient map, with its boundary value fully
retained. Write E_H=C[s]/(H), upsilon_H=j_H(g/H), and use the existing full
packet section sigma_H:E_H -> Q=B/Theta V. For the original full jet J_H,

    J_H V_h,rat(P/kappa)=upsilon_H [P]_H,
    q V_h,rat(P/kappa)=sigma_H(upsilon_H [P]_H).                (TA14)

To justify the second equation, H(D_x)P(D_x)F_H=Theta(P(D_x)phi_*)
by Mellin identity and injectivity, so its Q-class lies in Q[H(D_x)]. On that
actual submodule the original full-jet map and sigma_H are inverse. Thus the
displayed equation follows from the first one, which is the literal product
of Taylor series. Restriction to the original h-block gives

    j_h(kappa upsilon_H P)=upsilon_h [P]_h.                    (TA15)

At each added kappa-block, kappa P vanishes through its full order. The old
source inclusion therefore retains its actual full-unit h-component and has
zero added components, not a hidden mixture of old and new source classes.

For a geometric degree-zero numerator Q the observed boundary is exactly

    q V_h,rat(E(Q)/kappa)=sigma_H(upsilon_H [E(Q)]_H).           (TA16)

It need not be zero. TA16 is the calculated defect preventing an unproved
descent from geometric de Rham cohomology to the original theta quotient.
The cochain source map, its full-unit jet value and its entire residual
boundary have all been supplied; no false cohomology intertwiner replaces them.

At the fixed-domain specialization u=t=0, E=b h. The quotient of the original
arithmetic E_H by its ideal (b h)/(H), transported by the unit upsilon_H,
is exactly the geometric polynomial quotient C[s]/(b h). At an added root p
this ideal is (s-p)/(s-p)^m_p; at an original h-root its component is zero.
This computes the complete endpoint kernel, including every removed higher
jet, instead of identifying the two quotients outright. For m_p=1 that
component is zero. Its rank count is d+|S_B|, with no deletion from the
larger original E_H before the specified quotient map.

The fixed pair TA11 was derived for u!=0. At u=0, recomputing the maximal
graph domain allows all coefficients in kappa^-1 C[s], since h-t has no pole;
that is a different degree-zero domain. At u=t=0 its localized cohomology
has rank d. The fixed-domain specialization just calculated has rank d+|S_B|.
Both domains and the exact endpoint quotient are explicit; no flatness of
the recomputed graph domain is asserted.

## 6. The actual theta Gram and finite source cost

For the literal denominator frame TA10, TA2 becomes the exact identity

    ||V_h,rat(P/kappa)||^2 = integral_R |P(1/2+iy)|^2 w_H(y) dy,
    w_H(y)=|(g/H)(1/2+iy)|^2/(2 pi),    integral w_H=mu_H.       (TA17)

All removable values on the line are filled by the original entire g/H.
This is the already specified arithmetic convolution seed for the actual
extended packet H, with its own full mass mu_H, not a unit-mass replacement.
For any finite numerator degree N, the exact Gram is

    (M_H,N)_{ij}=integral_R conjugate((1/2+iy)^i)
                     (1/2+iy)^j w_H(y) dy,   0<=i,j<=N.       (TA18)

It is positive definite: a nonzero polynomial is nonzero outside a finite set,
and the nonzero entire g/H is nonzero almost everywhere on the line.
All moments converge by the original rapid vertical decay. In an arbitrary
specified finite rational basis R_j, the unchanged norm instead has matrix
integral conjugate(R_i)R_j w_h; TA17--18 are its exact denominator-coordinate
pullback, not a change of norm.

Let E_N be the coefficient matrix of TA12 from degrees <=N to degrees
<=N+d+|S_B|. The full source cost of the actual geometric boundary is

    ||V_h,rat(E(Q)/kappa)||^2
       = Q^* E_N^* M_H,N+d+|S_B| E_N Q.                       (TA19)

This includes u, t, every m_p through c, and all cross terms. Its arithmetic
class is TA16. If G_H is an existing canonical quotient Gram at an admitted
cutoff and T_N is the literal matrix Q -> upsilon_H [E(Q)]_H, the quotient
cost is exactly Q^* T_N^* G_H T_N Q. No new quotient metric is selected.
No uniform bound on these actual matrices is inferred from their positivity.

Completed result: all analytic pole classes have their exact original-Hilbert
admission test; those with genuine strong-Schwartz source representatives are
realized by an actual enlarged full-zero packet. Their complex, residues,
source Gram and arithmetic boundary defect are explicitly calculated.

## 7. The connection in the same arithmetic numerator frame

Write r=|S_B| and q=d+r. In the degree-one numerator frame
f_j=s^j/kappa, 0<=j<q, the actual connection is

    L = u d/dt - A_adm(u,t),
    A_adm = Companion(chi_adm),
    chi_adm(u,t;s)=b(s)(h(s)-t)-u c(s).                       (TA20)

Here Companion means the column-convention matrix taking e_j to e_(j+1)
for j<q-1 and taking e_(q-1) to minus the coefficient column of the
lower-degree part of the displayed monic polynomial. This specifies every
matrix entry without a basis convention left implicit.

Indeed [L,E]=0 on parameter-dependent polynomial numerators: the term
[u d/dt,E]=-u b cancels [-s,u b d/ds]=u b, and all remaining commutators
vanish. Thus L descends through the parameter-dependent cokernel. Its value
on f_j is -s^(j+1)/kappa. Only the last basis vector requires reduction,
and the exact reduction relation is E(1)=chi_adm. This proves TA20.
It does not assert that multiplication by s alone descends on the fixed
quotient by the image of the differential operator E. Nor is chi_adm being
declared an annihilator made of new actual zeros of g. It is the calculated
connection matrix in the already admitted arithmetic frame.

Here is its exact relation to AP's polynomial-plus-simple-pole frame.
Use that frame restricted to S_B, and denote its connection matrix by
T_B=[A(t) B_(S_B);0 diag(p)]. Let G(u,t) be the matrix whose jth column
is the AP coordinates of [s^j/kappa]. Its residue-block entries are

    G_(p,j) = Res_p(w(s)s^j/kappa(s) ds)/w(p)
       = (d/ds)^(m_p-1)[w(s)s^j/kappa_p(s)]_(s=p)
                      / ((m_p-1)! w(p)),
    kappa_p(s)=kappa(s)/(s-p)^m_p.                            (TA21)

All m_p derivatives, the original exponential weight, and its value w(p)
are retained. To compute the polynomial-block entries, subtract the simple
poles with these coefficients from f_j. The result has zero weighted
residue at every admitted point. Take AP's log-free local primitives,
keep their finite principal parts, and subtract their D_exp images. This
leaves a polynomial. Reduce it to degree less than d with the original
leading-term reduction for D_exp. These coefficients are exactly the
remaining entries of G. This is a finite formula for each column, not a
choice of an unspecified comparison map.

Both sets are proved bases of the same admitted cohomology, so G is
invertible. The primitive calculations only divide by nonzero u, w(p),
nonzero leading coefficients, and fixed nonzero differences of distinct
points. Their finite coefficients are therefore holomorphic for u!=0 and
all t. Applying L to each column, with its parameter dependence included,
gives the exact identity and finite scaling transport

    u G_t = T_B G - G A_adm,
    A_adm = G^-1 T_B G - u G^-1 G_t,
    C_adm(a;t)=G(t)^-1 C_B(a;t) G(t+u a).                     (TA22)

The fixed u is suppressed only in the last line's arguments. For proof of
that line, differentiate its right side with respect to a, use
C_B'(a;t)=-C_B(a;t) T_B(t+u a), and then the first identity of TA22.
The derivative is -C_adm(a;t) A_adm(t+u a) and the value at a=0 is I.
The uniqueness of this finite linear differential equation proves the
transport formula. Both endpoint frames and the derivative gauge term
are present; a pointwise similarity would omit an actual term.

These same numerator vectors are the actual source vectors D_x^j F_H
by TA10, so their original norm is the explicitly calculated M_H,q-1.
The cohomological frame change G, however, also used D_exp primitives.
Those primitive differences have exactly the source cost TA19 and the
full arithmetic image TA16. A norm isometry between arbitrary reduced
representatives is not silently inferred from a cohomology change of basis.
Thus TA20--22 supply the concrete arithmetic-frame connection, its exact
comparison with AP, and the already computed source-level discrepancy.

## 8. Exact recovery of the old canonical quotient metric

The comparison reaches the original quotient metric as well as individual
source vectors. Put K=deg kappa and D=deg H=d+K. Use the literal injection

    i_kappa:C[s]/h -> C[s]/H,   [P]_h -> [kappa P]_H.

It is well-defined because H=h kappa and injective because the polynomial
ring has no zero divisors. Its image is the ideal (kappa)/(H). At the
old h-block it multiplies by the actual nonzero Taylor unit j_h(kappa);
at every new block it is zero through that block's full order. Composing
with upsilon_H yields precisely the original arithmetic unit upsilon_h
by TA15, not a newly chosen identification of the h-component.

Let R_H,N^coef be the existing unique least-source-norm representative for
coefficient classes in C[s]/H among polynomials of degree at most N;
let G_H,N^coef be its Gram. Define R_h,N-K^coef and G_h,N-K^coef in precisely the
same way using the original weight w_h. Take N>=D-1 so both quotient
maps are onto and both metrics are defined. Then, as maps and forms,

    R_H,N^coef i_kappa = M_kappa R_h,N-K^coef,
    i_kappa^* G_H,N^coef i_kappa = G_h,N-K^coef.               (TA23)

where M_kappa is literal polynomial multiplication. These are the
original least-norm constructions, not newly selected quotient metrics.

For proof, a degree-at-most-N representative Q of i_kappa[P]_h has
Q-kappa P=H T for some polynomial T. Thus Q=kappa R with [R]_h=[P]_h
and deg R<=N-K. Conversely every such R gives an allowed Q. This is a
bijection between the two complete affine spaces of representatives,
including all their relation directions. Their norms agree exactly:

    integral |kappa(s)R(s)|^2 w_H(y) dy
          = integral |R(s)|^2 w_h(y) dy,   s=1/2+iy,
    w_h(y)=|kappa(1/2+iy)|^2 w_H(y).                          (TA24)

The last identity is g/h=kappa g/H, with the removable line values
filled by those entire functions. It retains both unnormalized masses;
neither mass is asserted equal to the other. Finite-dimensional positive
definiteness gives a unique minimizer in each affine space. The norm
bijection therefore proves the first identity of TA23, and polarization
proves its full Hermitian Gram identity, including cross terms.

Under the actual source maps the two minimizing polynomials give the
identical strong-Schwartz function:

    (R_H,N^coef i_kappa[P])(D_x) F_H
                         = (R_h,N-K^coef[P])(D_x) F_h,

because kappa(D_x)F_H=F_h follows from the original Mellin transforms.
Thus TA23 is a calculated isometric inclusion of the original arithmetic
quotient observation into the extended-packet observation with the exact
degree shift K. It is stronger than a bound inferred from positivity.
For precision about full-unit coordinates, write G_H,N^jet for the
same canonical observation expressed in physical jet coordinates
J_H=upsilon_H pi_H. Then

    G_H,N^coef=M_upsilon_H^* G_H,N^jet M_upsilon_H,
    j=M_upsilon_H i_kappa M_upsilon_h^-1,
    j^* G_H,N^jet j=G_h,N-K^jet.

Here M_upsilon denotes multiplication by the indicated complete Taylor
unit, not its leading coefficient. TA15 proves that j is exactly the
identity on the original h-block and zero on each added full kappa-block.
These equations specify the equivalent metric statement in the physical
jet convention used for the arithmetic cost in TA19. No unit-coordinate
change is left implicit or omitted from a Gram pullback.

TA23 does not identify the extra quotient directions or their mixed Gram
entries with old directions. Those remain in the actual extended metric; the
geometric-boundary image TA16 and its source cost TA19 remain unchanged.

## Sources and verification scope

Root reread A1--A5 of the current `tex/arithmetic_input.tex`, including the
definition of B, g=2 xi, Theta phi_*, and the original Euler inverse. The full
A1--A19 source and its full-order section were read previously. AP1--26 is the
accepted analytic input, SHA256
357923aead35c77f2fa98598fbc4ed8bc1f7cd6ebc04760da504a0ded765a652.
The independent collaborator derived and checked TA3--TA7, the global graph
domain and TA12--TA16 while root wrote their complete proofs and source-cost
formulas here. This note claims written mathematics, not new Lean execution,
numerical zero certification, a uniform estimate, or remote publication.
