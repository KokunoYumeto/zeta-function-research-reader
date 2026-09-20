# The one-step proper-source kernel vanishes off a fixed finite period set

19 September 2026. This calculation concerns the original invariant source, four x_i^4 multipliers, and final invariant quotients. It is not an identification of the native source and target metrics. The original simple quartet, full unit, period and branch are retained. The independent sixteen-observation theorem applies also on the exceptional set left by this proof.

## 1. A precise finite-fibre criterion

Use the original notation of note 02: R=S/(Q), B=im(S^G -> R), A=product of the other four orbit quadrics, and conductor(B subset R)=A R. Let

    T=B+x1^4 B+x2^4 B+x3^4 B+x4^4 B subset R.                 (K1)

An invariant lift f of an element in the original one-step proper-source kernel satisfies f T subset B. This follows from the actual target equalities modulo B/A R; since A R subset B they are literal memberships in B.

On a nonzero coordinate chart the ambient cyclic quotient is etale: xi has primitive character and satisfies T^5-xi^5 over the invariant ring, with invertible derivative. A geometric fibre of R over B is therefore a reduced subset of the five orbit points. Let r be its size and let l be the number of active coordinates of its representative. The evaluations of 1 and the active xi^4 are nonzero column scalings of the Fourier-5 matrix, on those r rows and the l+1 distinct characters 0,4i.

Every square minor of Fourier-5 is nonzero. For sizes one and two this is respectively a root of unity and a nonzero multiple of 1-zeta^a, a nonzero modulo five. The inverse matrix is one fifth the conjugate Fourier matrix. The complementary-minor identity therefore proves the assertion for sizes three and four, and the full Vandermonde determinant proves size five. This is a complete proof in this fixed size, not an appeal to generic minors.

Consequently T generates R at a fibre with r<=l+1. To justify the passage from fibre to local module, the finite cokernel has zero reduction modulo the local maximal ideal. Choose a finite generating vector and write it as M times itself with entries in that maximal ideal. The determinant of I-M is a unit; its adjugate annihilates the vector. The cokernel is zero.

## 2. All possible divisorial failures

Only the following coordinate curves can support a divisorial failure of the criterion in Section 1:

(a) a coordinate projective line contained in Q;
(b) a coordinate-plane conic on which the restriction of Q has a single cyclic character.

Indeed l=4 gives r<=5=l+1. At l=3 failure requires all five orbit points to lie in Q. The six quadratic monomials on that coordinate plane have five characters, with exactly one character repeated. Fourier inversion then makes every singleton-character monomial vanish. At points with all three indicated coordinates active, each singleton coefficient must be zero. Thus the restriction is exactly the two-term semi-invariant conic (or a further degeneration).

At l=2, failure requires r>=4. The three binary quadratic monomials have three distinct characters; their evaluations on any three of these rows are independent. Since both coordinates are active, every binary quadratic coefficient must vanish. The coordinate line is contained in Q. At l=1 the projective set is zero-dimensional, not a divisor of the smooth projective quadric.

When neither (a) nor (b) occurs, T=R at the generic point of every projective divisor. For an f in the original proper-source kernel, fT subset B then makes f a conductor element at every such generic point. Hence f is divisible there by A, including every multiplicity of its restricted factors. Under the original Segre biform map, unique factorization gives global divisibility by that full product. Its degree-k class in R/A R is zero. We have proved

    E_k^prop=0 on the locus excluding (a),(b), for every original k. (K2)

No coprimality of the restricted orbit factors was used.

## 3. Evaluate this locus in the actual PCL family

Retain

    H(u)=exp(a_*/u) G_u R(1/u) V^(-1) U,
    U=diag(a,conj(a),conj(a),a), a!=0.

Put z=1/u and use the explicit invertible diagonal coordinate map X=G_u^(-1)x. Multiplication of the equation by the nonzero scalar exp(2a_*/u) gives the same original quadric in these coordinates as

    Qtilde_z(X)=Q0(U^(-1)V R(z)^(-1) X).                       (K3)

This diagonal change commutes with the original fifth-root action and preserves coordinate lines and planes. It changes the cofactor xi^4 only by its actual nonzero fourth-power factor, so it preserves the kernels being tested. No metric invariance is inferred from it.

The matrix R(z) and its inverse are the retained entire PCL coefficient matrices. Let r=delta+i gamma, R0=r^2, T0=conj(r)^2, and set

    beta=-(R0+T0)=2(gamma^2-delta^2)>0,
    eta=R0 T0=(delta^2+gamma^2)^2>0,
    p=a^(-2), b=conj(a)^(-2),
    u0=(2R0-T0)/3, v0=(2T0-R0)/3.

The original constant matrix is J=I-(beta/3)E13-(2beta/3)E24. Direct substitution gives

    Qtilde_0=p(X1+u0 X3)^2-b(X1+v0 X3)^2
             -p R0(X2-v0 X4)^2+b T0(X2-u0 X4)^2.              (K4)

Its even block on (X1,X3) and odd block on (X2,X4) have entries

    e0=p-b, e1=p u0-b v0, e2=p u0^2-b v0^2,
    o0=-p R0+b T0, o1=p R0 v0-b T0 u0,
    o2=-p R0 v0^2+b T0 u0^2.

Their determinants are

    e0 e2-e1^2=-p b(R0-T0)^2 !=0,
    o0 o2-o1^2=-p b R0 T0(R0-T0)^2 !=0.                      (K5)

### Coordinate-plane gates

On the plane omitting X1, the repeated character has monomials X3^2,X2X4. Its semi-invariant failure requires o0=o2=0, which implies u0^2=v0^2. This is impossible since (u0-v0)(u0+v0)=(R0-T0)(R0+T0)/3 is nonzero. On the plane omitting X4 the analogous failure requires e0=e2=0 and gives the same contradiction.

On the plane omitting X2 the repeated-character monomials are X1^2,X3X4. At least one of the off-character coefficients e1,e2 is nonzero by (K5). On the plane omitting X3 the repeated-character monomials are X1X2,X4^2; at least one of o0,o1 is nonzero. Thus all four plane gates have a specified nonzero coefficient at z=0.

### Coordinate-line gates

The lines (1,3) and (2,4) are excluded by (K5). The line (1,2) would require e0=o0=0 and hence R0=T0. The two lines (1,4) and (2,3) are excluded by

    T0 u0^2-R0 v0^2
      =-(R0-T0)(R0^2-7R0 T0+T0^2)/9 !=0.                    (K6)

Here (R0^2+T0^2)/(R0T0) lies in [-2,2], so the second factor divided by R0T0 is at most -5.

Only the line (3,4) can occur at z=0. It requires e2=o2=0. On that precise stratum e1,o1 are nonzero and

    (o1/e1)^2=eta.                                         (K7)

We next compute its actual first variation, rather than assume that the limiting line is absent.

## 4. The only possible limiting coordinate line does not persist

The original PCL coefficient formula gives the following exact first derivatives, in ordinary matrix indices:

    R'21=eta-beta^2/9,
    R'23=7beta^3/81-2beta eta/3,
    R'12=beta^3/27-beta eta/3,
    R'14=-11beta^4/324+beta^2 eta/3-eta^2/2.

For example these follow by summing the finitely many p,h with 2p+4h=5+r+1-a in PCL2 at series degree one. All rising factorials and signs are retained.

Put K=R'(0)J^(-1). Then

    K23=beta(4beta^2-27eta)/81 <0,
    K14=-(beta^4-12beta^2 eta+54eta^2)/108 <0.                (K8)

Writing Qtilde_z=Qtilde_0(J R(z)^(-1)X), its matrix derivative is -K^T Qtilde_0-Qtilde_0 K. On e2=o2=0 its (3,4) entry is

    Qtilde'34(0)=-e1[K14+(o1/e1)K23].                       (K9)

The exceptional algebra gives T0 u0^4=R0 v0^4. Set b0=beta/sqrt(eta), which lies in (0,2). Dividing the equation by powers of T0 and using R0!=T0 gives

    b0^4-27b0^2+81=0,
    b0=3(sqrt(5)-1)/2,
    b0^2+3b0-9=0.                                        (K10)

For o1/e1=+sqrt(eta) the bracket in (K9) is strictly negative by (K8). For o1/e1=-sqrt(eta), direct reduction using (K10) gives

    K14-sqrt(eta)K23=eta^2(108-45b0)/324 >0.                (K11)

Thus Qtilde'34(0) is nonzero on the entire possible exceptional limiting stratum. No original unit phase was assigned: p and b remain their actual reciprocal squares throughout this calculation.

## 5. Fixed finite period tests and uniformity in degree

For each of the six coordinate lines choose one nonzero coefficient gate, and for each of the four planes choose one singleton-character coefficient gate. Sections 3-4 specify such ten entire functions g_nu(z). Their leading order r_nu is zero, except possibly the (3,4) gate, for which it is one and its leading coefficient is (K9).

Write g_nu(z)=c_nu z^(r_nu)+higher terms, c_nu!=0, and set

    C_nu=1+sum_{n>r_nu}|[z^n]g_nu|,
    epsilon_nu=min(1,|c_nu|/(2 C_nu)),
    R_prop=max(R_*,(min_nu epsilon_nu)^(-1)).                (K12)

The sums converge because the functions are entire. For 0<|z|<=epsilon_nu, the full tail is at most C_nu |z|^(r_nu+1), so |g_nu(z)| >= |c_nu||z|^(r_nu)/2. Therefore every fixed original |u|>=R_prop, on every original branch, satisfies

    E_k^prop=0 for every original rank-valid k>=9.          (K13)

More generally define the explicit exceptional superset

    X_prop={u:|u|>=R_*, product_nu g_nu(1/u)=0}.

It is finite, independently of k. Indeed, divide the product by its specified zero order at z=0; the resulting entire function is nonzero at zero and has only finitely many zeros on the closed disk |z|<=R_*^(-1). At a selected-gate zero an actual failure has not been asserted; the coefficient test can be refined there. The sixteen-observation theorem in note 02 holds even at these exceptions.

A finite zero-count allowance is also explicit. For h(z)=z^(-sum r_nu) product g_nu(z), put R=R_*^(-1) and M_{2R}=sum_n|h_n|(2R)^n. Jensen's circle identity gives

    #zeros in |z|<=R <= log(M_{2R}/|h(0)|)/log 2,

with multiplicity. No numerical value for this count or for the actual period gates is claimed.

## 6. Exact propagation to the independent proper-source metric

The source value rank is now r_I=j_{0,k}=8k-32-v+t0(k,u) off X_prop. On the two-active-point stratum from the preserved fixed-jet proof, its eventual value is 8k-32-v. These are the original low-jet and invariant dimensions, not ambient ranks.

The source E-minimum disappears because E=0; the original target J-minimum does not. In its retained Z_R frame,

    Q_N=Z_R^* J0^* D_{k,N-v}^{s0} J0 Z_R,
    H_N=F_R^* D_target F_R
       -F_R^* D_target J_*(J_*^*D_target J_*)^(-1)
                                   J_*^*D_target F_R.      (K14)

The original source-E determinant correction is exactly one. The complete scalar R log det(Q_N^(-1/2)H_N Q_N^(-1/2)) is still not evaluated by (K13). Equation (K14) records the exact remaining metric problem after this algebraic kernel has been removed on the stated original-period locus.
