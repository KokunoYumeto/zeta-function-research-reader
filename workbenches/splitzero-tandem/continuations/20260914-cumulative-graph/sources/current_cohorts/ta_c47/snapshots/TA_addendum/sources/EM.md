# The added arithmetic directions: exact mixed metric and volume

13 September 2026. This continues TA1--24 on the original theta source.
TA23 recovers the old packet's canonical metric inside an extended actual
packet. Here the other directions, their mixed terms and their quotient
volume are calculated. The quotient behind the Schur complement is
identified by its original source map; no new metric is selected.

## 1. Actual packets, original sources, and fixed coordinate conventions

Use TA's coprime monic actual full-zero packets h and kappa, H=h kappa,
with d=deg h>0, K=deg kappa, and D=d+K. The multiplicities are their
full orders as zeros of g=2 xi. This does not assert a new zero exists.
K=0 is allowed and treated at the end. Initially take K>0.

For f=h,kappa,H, retain the original Euler-inverse source F_f with
Mellin transform g/f, original generator D_x=-x partial_x, and density

    w_f(y)=|(g/f)(1/2+i y)|^2/(2 pi).

The original strong-Schwartz source gives all finite moments and positive
finite polynomial Grams. None of the masses integral w_f is divided out.
Write P_n=C[s]_{<=n}, E_f=C[s]/f, in increasing-power remainder bases.
For N>=D-1, all quotient observations below are onto. Let R_f,n^coef
and G_f,n^coef denote the original unique least-source-norm representative
and its Gram for E_f from P_n with weight w_f. Abbreviate

    A=G_h,N-K^coef, B=G_kappa,N-d^coef, G=G_H,N^coef.

The superscript coef refers to coefficient remainders, not physical jets.
Physical jets retain the full unit U_f=M_upsilon_f, upsilon_f=j_f(g/f),
and G_f,n^coef=U_f^* G_f,n^jet U_f.

## 2. Full block matrix and the exact mixed term

Define the literal polynomial map

    T:E_h direct_sum E_kappa -> E_H,
    T(P,Q)=kappa P+h Q.                                      (EM1)

It is well-defined. Reduction modulo h and modulo kappa proves it is
bijective, since kappa mod h and h mod kappa are units. Every original
jet order is retained by these reductions. TA23 applied to both factors
gives the exact representatives and block Gram

    R_H,N^coef T(P,Q)
       =kappa R_h,N-K^coef P+h R_kappa,N-d^coef Q,
    T^* G T = [ A C ; C^* B ].                               (EM2)

For completeness, each summand on the right is the canonical lift of
its own class by TA23. Their sum is still orthogonal to the full relation
space H P_{N-D}. It is therefore the unique canonical lift of the sum.
This proves the first identity, including its representative, not only
its quotient value. Taking all pairwise original source inner products
proves the second. Specifically, in the indicated bases,

    C_ij=integral overline(kappa(s)(R_h,N-K^coef e_i)(s))
                       h(s)(R_kappa,N-d^coef e_j)(s) w_H(y) dy,
    s=1/2+i y.                                              (EM3)

Equivalently C_ij is the original source inner product between
(R_h,N-K^coef e_i)(D_x)F_h and
(R_kappa,N-d^coef e_j)(D_x)F_kappa. This follows from the exact identities
kappa(D_x)F_H=F_h and h(D_x)F_H=F_kappa. Every phase and mixed term in
EM3 is retained. No orthogonality of distinct zero blocks is assumed.

## 3. The original source quotient behind the Schur complement

Let U=M_{h mod kappa} on E_kappa. Define the canonical Gram Gamma_N
directly from the following observation of the same source P_N,w_H:

    0 -> P_{N-K} --multiplication kappa--> P_N
                         --pi_kappa--> E_kappa -> 0.          (EM4)

This is an explicit additional observation of the already fixed source,
not a replacement of its norm by w_kappa. Its unique least-norm section
will be denoted R_free. Then the exact Schur complement and minimizer are

    S_N=B-C^* A^-1 C = U^* Gamma_N U,
    P_min=-A^-1 C Q,
    kappa R_h,N-K^coef P_min+h R_kappa,N-d^coef Q
                                         =R_free(UQ).        (EM5)

Here is a proof through the complete original affine spaces. First,
pi_kappa T(P,Q)=h Q=UQ. For fixed Q, varying P in E_h ranges through
every class of E_H with this prescribed kappa remainder: the kernel
of E_H -> E_kappa is precisely the ideal (kappa)/(H), the image of
the first summand of T. Each of these classes in turn has all its
P_N representatives obtained by adding H P_{N-D}. Their union is
exactly every polynomial in P_N with kappa remainder UQ. Thus minimizing
first within each H-class and then over P is exactly the minimization
specified by EM4, with no omitted relation directions.

In EM2 the squared norm at fixed Q is

    (P+A^-1 C Q)^* A (P+A^-1 C Q)
                               +Q^*(B-C^* A^-1 C)Q.

Since A is positive definite, the minimum has the stated unique P_min.
This proves the form identity and, by uniqueness, the source identity in
EM5. Gamma_N and S_N are positive definite; the larger relation space in
EM4 has not been replaced by the smaller H-relation space.

In the original arithmetic cohomology Q_theta=B_source/Theta V, the
full packet has its original section sigma_H and full-jet observation.
Projection onto the kappa-primary arithmetic submodule is the actual map

    Q_theta[H(D_x)] -> Q_theta[kappa(D_x)],
    z -> sigma_kappa pr_kappa J_H z,
    P(D_x)F_H -> sigma_kappa (upsilon_H|kappa [P]_kappa).       (EM6)

The last expression means the quotient class of that source vector.
The previous equality follows from the full-jet inverse on the actual
H-torsion submodule. Its kernel is the original h-primary submodule.
Consequently EM4--5 calculate the finite source cost of the same
arithmetic projection, expressed in its stated coordinates. These are
the arithmetic submodules of the original tau-base pushforward; no
different cohomology group or source sheaf is substituted.

## 4. Resultant, determinant line, and the full-unit conversion

In the increasing-power bases, T's columns are

    kappa, kappa s,...,kappa s^(d-1), h,h s,...,h s^(K-1).

Its determinant is exactly Res(h,kappa), including sign in this convention.
Indeed the basis [1,s,...,s^(d-1),h,h s,...,h s^(K-1)] has triangular
change-of-basis determinant one. In that basis T has diagonal blocks
M_{kappa mod h} and I_K. The determinant of the former is
product_{h(rho)=0} kappa(rho)^(ord_rho h)=Res(h,kappa), with complete
multiplicities. It is nonzero by coprimality. Hence EM2 gives

    det G = det A det S_N / |Res(h,kappa)|^2.                 (EM7)

This is the determinant-line factor for the displayed ordered map, not
an arbitrary volume convention. Also det U=Res(kappa,h), and
Res(kappa,h)=(-1)^(dK) Res(h,kappa). Substituting the full U term of
EM5 therefore yields the further exact identity

    det G_H,N^coef = det G_h,N-K^coef det Gamma_N.             (EM8)

Both resultant factors were retained and cancel algebraically in EM8.
Neither is individually set to one.

For the physical full-jet formulation, put a=upsilon_H|kappa and

    J=U_H T diag(U_h^-1,U_kappa^-1),
    Gamma_N^phys=M_a^{-*} Gamma_N M_a^-1.                     (EM9)

The columns of J are exactly the two extension-by-zero inclusions of
the full physical h and kappa jets, by upsilon_h=kappa upsilon_H|h
and upsilon_kappa=h upsilon_H|kappa. They are not asserted orthogonal.
The physical Schur complement is Gamma_N^phys, since
U_kappa=M_a U and the multipliers commute. The absolute determinant
of J is 1/|Res(h,kappa)|: the determinant of U_H is the product of its
two restriction determinants, whereas det U_h times det U_kappa has the
two additional resultant factors. Thus the physical formula is

    det G_H,N^jet = |Res(h,kappa)|^2
                       det G_h,N-K^jet det Gamma_N^phys.     (EM10)

This preserves the exact coordinate change from the coefficient formula.
Physical jets in monomial remainder coordinates are not assigned a
product determinant frame without this J factor.

## 5. The relation-volume is the original theta seed

Define, for f=h,H,1, the actual moment Gram determinants

    Delta_f,n=det[integral overline(s^i)s^j w_f(y) dy]_(i,j=0)^(n-1),
    Delta_f,0=1, w_1=|g|^2/(2 pi), s=1/2+i y.

The original relation source for E_f at cutoff n-1 consists of f times
polynomials. Its weight is exactly |f|^2 w_f=w_1. In particular the
relation weight does not depend on which actual full-zero packet was
divided out. Using the monic ordered basis of quotient powers followed
by f times relation powers, whose determinant is one, the ordinary Gram
Schur complement proves, for n>=deg f,

    det G_f,n-1^coef = Delta_f,n/Delta_1,n-deg f.

Apply this at the actual paired cutoffs in TA23. The two relation
dimensions are both N-D+1, so their full denominators agree, giving

    det G_H,N^coef / det G_h,N-K^coef
                =Delta_H,N+1/Delta_h,N-K+1=det Gamma_N.       (EM11)

The last equality also follows directly from EM4: its relation Gram
has weight |kappa|^2 w_H=w_h and dimension N-K+1. Thus EM11 is verified
by the two exact sequences independently. At N=D-1 the common original
H/h relation dimension is zero and its determinant is one; no negative
index is introduced. All numerator and denominator masses remain those
of the displayed arithmetic weights.

This identifies the added quotient volume by two explicitly specified
arithmetic moment determinants. It is not left as the determinant of
an unnamed complement.

## 6. Exact mixed-volume cost

One can also retain the entire loss relative to keeping the added
coordinates fixed with the old coordinates zero:

    det S_N/det B = det(I_K-B^-1 C^* A^-1 C),
    Q^*(B-S_N)Q = (A^-1 C Q)^* A (A^-1 C Q).                 (EM12)

The endomorphism B^-1 C^* A^-1 C is self-adjoint and nonnegative in
the existing B form; its eigenvalues belong to [0,1), because EM5 is
positive definite. These assertions follow respectively by taking its
B inner product and by writing Q^*S_N Q>0. The right-hand side of
the second identity is the exact original source cost of the optimizing
old component. No change to a unit-mass measure or a different metric
has been made. The determinant loss is the product of the retained
1-minus-eigenvalue factors, not a presumed zero mixed term.

These identities compute the finite extension volume and all mixed
contributions. They do not prove a uniform bound as packet size and
cutoff vary. The original full arithmetic-boundary discrepancy TA16,
its source cost TA19 and the geometric connection TA20--22 remain in
place; projecting physical arithmetic classes in EM6 is not an assertion
that every geometric exponential boundary has become a theta boundary.

For K=0, E_kappa is zero, all its determinants are one, the second
block and its maps are empty, Res(h,1)=1, and H=h. EM1--12 reduce to
the identity comparison with no added classes. No nonempty extension
is inferred from the formulas.

## Sources and verification scope

The actual-source input is the accepted TA1--24 proof, SHA256
830e9a254465434fd61cb16212544f004ddf54a5adc72554bccabe217b045e5a.
Root reread its final metric section and the original arithmetic-input
Euler inverse, full jets and packet section A5--A10. Root also reread
AT1--AT7: the original tau pushforward, retained source map and canonical
Gram construction. These are applied here to the specified one-factor
arithmetic packets. No tensor-sum convolution identity is inferred by
replacing its separate cyclic relation with H. This note contains written
proofs and no new Lean execution, interval computation, or zero-location
certificate. An independent collaborator derives and checks the block
and quotient maps separately; its final review pins the accepted text.
