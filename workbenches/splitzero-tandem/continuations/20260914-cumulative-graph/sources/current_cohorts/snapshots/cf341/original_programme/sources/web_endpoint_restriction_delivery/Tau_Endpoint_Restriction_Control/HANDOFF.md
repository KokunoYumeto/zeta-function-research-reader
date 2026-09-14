# Handoff: canonical endpoint restriction and logarithmic control

## Scope and source state

Main was read at `7ea0a49945390eae14d3160a5730858899768b5f`. The actual current
`workbenches/tau-toda-volume-formal/ENDPOINT_CRITERION.md` was fetched (blob
`09d658b1c50245b9e340722817bc9487f1ce409a`). Retain its corrected top-exterior
case and its second-exterior multiplicity cost. No new Lean execution or remote
change was performed here.

The inherited `Tau_Arithmetic_Endpoint_Bounds` source supplies the written
analytic estimate `(omega_(2n)/omega_n)^(1/(2n)) <= C_h n`, for n>=k>=3 with
fixed actual packet h. It is not formalized by the finite results below.
The new construction reads its remaining four-volume term at the types of the
original source and quotient.

## 1. Bounded matrix/reconstruction target

Retain monic polynomial columns b_a, actual norms omega_a, and

    B_N=[b_0,...,b_N],  O_N=diag(omega_0,...,omega_N),
    K_N=B_N O_N^(-1) B_N*,  G_N=K_N^(-1),
    R_N=O_N^(-1) B_N* G_N.

B_N is the original remainder map; its kernel is multiplication by chi on the
specified lower-degree polynomials. Every new displayed inverse is a finite
positive Gram inverse, not a claim of uniform conditioning.

For i<=j let L pad source coefficients and P keep the first i+1 coefficients.
The actual quotient transport I_(i,j) is identity on E with metrics G_i,G_j.
Construct its adjoint

    T_(i,j)=K_i G_j : (E,G_j)->(E,G_i).

Prove directly:

    G_i T_(i,j)=G_j,
    L R_i T_(i,j)=P R_j,
    T_(i,j) T_(j,l)=T_(i,l),
    det T_(i,j)=V_j/V_i.

This is the quantitative return map, not a unital algebra morphism. The forward
identity transports commute with A. The return's action defect is explicitly

    [A,T_(i,j)] = H_i T_(i,j)-T_(i,j) H_j
                = Vcontrol_i G_j-K_i W_j,
    H_n=K_n W_n, W_n=A*G_n+G_n A-kG_n,
    Vcontrol_n=A K_n+K_n A*-kK_n.

Use the existing support reconstruction on each active fibre. A reverse natural
transformation of the entire original forward-index diagram is NOT claimed.
The actual reverse-composition law above is provided.

## 2. Same original boundary

Put H=1-T. Then

    d_(i,j)=L R_i-R_j=L R_i H-(1-P)R_j,
    B_j d_(i,j)=0,
    d_(i,j)* O_j d_(i,j)=G_i-G_j.

The two terms on the middle right have the same original arithmetic remainder H.
Their difference is a specified original chi relation. Its actual theta
primitive is the existing division/Koszul primitive. Under the original split
quotient it maps to the receiving supported zero e at that label; tau stays tau.

The maps T have eigenvalues g_a in (0,1]. Their adjoint interpretation gives
actual source singular values sqrt(g_a), with the source norm and target norm
both supplied. No change to the arithmetic metric is made.

## 3. Exterior full-jet determinant weights

For a q-element degree set D inside 0,...,j, retain

    a_D=|det B_D|^2 / product_(d in D) omega_d.

Cauchy--Binet proves

    det K_j=sum_D a_D,
    Z_(i,j)(z)=det(K_i+z(K_j-K_i))
              =sum_D a_D z^(#(D intersect {i+1,...,j})),
    Z_(i,j)(z)/det K_j=det(T+zH).

These are finite scalar observations of retained totals. No arithmetic mass is
assigned the value one. An admitted dependent basis has weight e=0^bullet;
an index set outside the admitted degree collection is structurally absent.
Full raw-jet row changes use the confluent Vandermonde with all factorials and
the actual unit multiplication matrix. For a square image-coordinate map, all weights acquire its common squared
determinant; the displayed endpoint ratios then cancel that same factor. The actual ambient
eta can be rectangular: retain wedge^q(eta B_D)=det(B_D) wedge^q(eta)(e_top),
rather than taking a determinant of eta.

## 4. Logarithmic enclosure target

Let s_m=tr(H^m). A verified matrix inequality K_i>=g0 K_j, 0<g0<=1, supplies
r=1-g0 as an upper bound on H's spectrum. For p>=1 and r>0:

    L=log(V_i/V_j)=sum_(m>=1) s_m/m,
    lower_p=sum_(m=1..p) s_m/m,
    c_p(r)=(-log(1-r)-sum_(m=1..p)r^m/m)/r^(p+1),
    lower_p <= L <= lower_p+c_p(r) s_(p+1).

The proof is the coefficientwise bound on the positive logarithm tail and then
the finite spectral theorem. r=0 has H=0 and L=0; do not divide by r there.
Finite matrix algebra, scalar power sums, and the exact rational atanh-log
bounds are bounded formalization targets. The full convergence/functional
calculus statement has a written proof and is not represented as compiled Lean.

Apply this to (q-1,2q-1) and (q,2q). Their upper certificates U0+U1 compose with
the inherited arithmetic norm theorem to give

    min_(q<=N<2q) epsilon_N <= C_h q sinh((U0+U1)/(2q)).

A uniform bound on those gaps and moments is still required. Finite existence
of g0>0 is not a uniform bound, nor an RH proof.

## 5. Explicit off-line consequence

For the exact hypothetical quartet, inherited B>=2q asinh(delta k/(2C_h)) and
B=-sum(log g_a) over the two q-dimensional returns imply that some

    g_a <= exp(-asinh(delta k/(2C_h))).

For its actual eigenvector v:

    ||P R_j v||^2 / ||R_j v||^2 = g_a,
    ||(1-P) R_j v||^2 / ||R_j v||^2 = 1-g_a.

The old portion has arithmetic coordinate g_a v. To recover v use the actual
invertible return map, not a declaration of absence. The exact information
still lies in the original relation correction in target degree j.
This implication has no converse; the supplied nilpotent on-line calibration
also has nontrivial restriction losses.

## Evidence

Nineteen exact rational/complex-rational test methods include original-Gram
adjoints, cochain relation corrections, action defect, return composition,
full-jet minors, the generating polynomial, raw confluent factorials, arithmetic
unit changes, literal mass, and exact log enclosures. They use declared Gaussian
polynomial fixtures, not actual zeta zeros. See CHECKS.md for executions.
