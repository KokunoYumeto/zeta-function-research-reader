# Orthogonal relation layers and arithmetic boundary control

Owner-workbench continuation of the checked tau library, based on PR #12 at
`5d2772ea0a16d177ac3e01ff70394b90ba95a232`.

## Scope and provenance

The new source is the owner's supplied 501-line note, “The other session's
homotopy classification is correct ... rank-at-most-two presentation”, dated
12 September 2026. Its Sections 4–7 contain the nested theta relations,
orthogonal residual representatives, rank-two control and numerical norm
sequence. Earlier inputs are the source/extension construction in PR #9 and
the global retraction in PR #10. The original scalar G(R), tau base, arithmetic
quotient, derivative D=-x partial_x, theta normalization g=2 xi, and full packet
multiplicities are unchanged.

This document separates three kinds of result: the added Lean statements,
written analytic consequences proved here, and numerical evaluations. The PR
validation record supplies the exact successfully checked commit when available;
a pending run is not a certificate. No full private transcript is republished.

## 1. What is being formalized

`SplitZeroSupportChange.lean` constructs support-changing morphisms using the
existing `LinearDiagram.Total`, not a second scalar or carrier. The index map
preserves bottom and binary joins. The coefficient maps satisfy naturality.
The total map is bundled as a G(R)-linear map, with its support, fibre-zero,
composition and actual transport formulas proved. No coefficient transport is
assumed injective.

`SplitZeroRelationLayer.lean` constructs, for L <= M and a retraction P onto L,

    M/L ~= M intersect ker(P),      [z] |-> z-Pz.

Its inverse includes the vector and takes its old quotient class. The file also
constructs B/L -> B/M and, when D(L) <= M, the distinct map B/L -> B/M induced by D.
It proves the criterion for a class to vanish after transition and the old
quotient's boundary-class identity. `orthogonalData` instantiates P with the
actual Mathlib starProjection onto L. In that instance ker(P)=L-perp, giving
precisely the orthogonal relation layer used in the source.

`SplitZeroBoundaryControl.lean` defines the residual representative R=(1-P)s,
the boundary B=DR-RA, and the control form from A and R. It proves the Green
identity calculation, the rank-two expression, the Gram downdate, and the
boundary's class in the old quotient. The rank-two expression is a conclusion,
not an input. The ambient inner-product space is not required complete: D may
therefore act on the original test-function space with its L2 inner product,
without asserting an everywhere-defined derivative on the L2 completion.

`SplitZeroKrylovStep.lean` goes a step further. From a finite raw-column expansion
of P s, D f_j=f_(j+1), and independence of the next column, it proves the one-layer
escape equation and constructs the entire local BoundaryControl.Data. It defines
the next vector as (1-P)f_(n+1), its unscaled norm square, and the next row by the
actual inner product divided by that norm. Thus the escape equation need not be
postulated when applying the boundary theorem.

`SplitZeroControlCompression.lean` factors the derived control matrix through
Fin 2 and proves rank <= 2. It proves nonzero eigenvalue transfer through a pair
of linear maps, the 2-by-2 determinant, its real roots, and their exact symmetric
radius. It does not claim that the entire generalized-eigenvalue/Loewner-norm
identification is bundled into a single formal theorem. The written proof below
makes that remaining connection explicit.

The analytic theta-map identities, integration by parts on the actual test
spaces, their finite Gram expansions and independence must instantiate these
interfaces. This contribution does not insert them as axioms or certify the
entire analytic programme by a finite-dimensional test. The full all-n monic
three-term recurrence and a bundled support-changing homotopy of the specific
theta chart remain distinct formalization targets.

## 2. Audit of the source recurrence

Use the original real-valued functions f_j=D^j f_0, f_0=Theta(phi_*), with
M f_0(s)=g(s)=2 xi(s). Let L_n=span_C{f_0,...,f_n}, P_n its orthogonal projection
and u_n=(1-P_(n-1))f_n (u_0=f_0). The vectors are monic in f_n and are not
renormalized. Write h_n=||u_n||^2>0.

The source's recurrence is

    D u_0 = u_1 + (1/2)u_0,
    D u_n = u_(n+1) + (1/2)u_n - (h_n/h_(n-1))u_(n-1), n>=1.

Proof. D u_n-u_(n+1) belongs to L_n. For j<=n-2, Green's identity gives
< u_j,D u_n>=<u_j,u_n>-<D u_j,u_n>=0 since D u_j belongs to L_(j+1).
The coefficient of u_(n-1) is -h_n/h_(n-1), since D u_(n-1) has leading u_n.
Finally 2 Re<u_n,D u_n>=h_n. Here the functions and the monic orthogonalization
have real coefficients, so that inner product is real and its coefficient is
exactly 1/2. Green's identity alone for an arbitrary complex seed would only
fix the real part; the source's reality condition is essential to this last step.

For s=s_Z and Ds-sA=f_0 ell_Z, put r_n=h_n^(-1)u_n^*s. Pairing this equation
with u_n gives

    (h_(n+1)/h_n)r_(n+1)
      = r_n((1/2)I-A)+r_(n-1)-1_(n=0) ell_Z,    r_(-1)=0.

Thus the arithmetic extension functional is retained, including at the first
stage. No spectral model is substituted for the actual packet operator A.

## 3. Derive the boundary and the two rows from the finite source

Put R_n=(1-P_n)s. The correction P_n s belongs to L_n=Theta V_n, so qR_n=qs
and J_Z R_n=1. These equalities imply injectivity of R_n. The Gram matrix
G_n=R_n^*R_n is positive definite; when interpreting equality in L2, first use
that a smooth function vanishing almost everywhere vanishes everywhere, then
apply the jet map on the test-function space.

Write P_n s=sum_(j=0)^n u_j r_j. The finite degree relations imply

    (1-P_n) D P_n s = u_(n+1) r_n.

The formal constructor proves this directly from an expansion in f_j: every
j<n term has derivative in L_n, and the remaining leading coefficient is r_n
because both raw and orthogonal bases are monic.

Let B_n=DR_n-R_n A. Direct expansion gives

    B_n=f_0 ell_Z-DP_n s+P_n s A.

The first and third terms are in L_n and are orthogonal to R_n. Green's identity
on R_n x,R_n y gives

    W_n=A^*G_n+G_n A-G_n=-(R_n^* B_n+B_n^* R_n).

Consequently

    W_n=R_n^*DP_n s+(DP_n s)^*R_n
       =h_(n+1)(r_(n+1)^*r_n+r_n^*r_(n+1)).

Both rows are induced by the same actual source and the same projection. The
first is the leading old projection coefficient; the next is the component of
the retained representative in the newly admitted relation. Similarly,

    R_(n+1)=R_n-u_(n+1)r_(n+1),
    G_n-G_(n+1)=h_(n+1)r_(n+1)^*r_(n+1).

In the old quotient,

    [B_n x]_(B/L_n)=-[u_(n+1)] r_n(x).

The quotient transition B/L_n -> B/L_(n+1) kills this class. Since
u_(n+1) is nonzero and orthogonal to L_n, its old class is nonzero. At the
reconstructed support level the zero is the receiving fibre's zero, not external
tau. The generic HomOver map supplies that precise scalar-linear transition;
this statement does not silently assert that every specific chart map has already
been bundled into a cochain homotopy in Lean.

## 4. The exact 2-by-2 calculation and a reflection simplification

Abbreviate h=h_(n+1), r=r_n, t=r_(n+1), G=G_n. Define

    a=rG^(-1)r*,  b=tG^(-1)t*,  c=rG^(-1)t*.

The nonzero eigenvalues of G^(-1)W equal those of

    h [[c,a],[b,conj(c)]].

Indeed G^(-1)W is the composite of the row map x |-> (r x,t x) and the
outgoing map (z,w) |-> h(G^(-1)t* z+G^(-1)r* w). Reversing the composites
preserves nonzero eigenvalues. The determinant without the h factor is

    (lambda-Re c)^2 + (Im c)^2 - a b.

Cauchy-Schwarz gives a b>=|c|^2, so its two roots are real. Since G^(-1)W is
similar to the Hermitian matrix G^(-1/2)W G^(-1/2), the least two-sided control
constant is exactly

    epsilon=h (|Re c|+sqrt(a b-(Im c)^2)).

Zero rows and linearly dependent rows are included: extra zero eigenvalues do
not change this radius.

New deduction for a reflection-stable packet, with multiplicities retained:
2 Re Tr(A)=dim E_Z. Cyclicity of trace therefore gives

    Tr(G^(-1)W)=2 Re Tr(A)-dim E_Z=0=2h Re c.

Thus Re c=0. The only possible nonzero eigenvalues are opposite, and

    epsilon^2=h^2(a b-|c|^2).

The normalized control is either zero or has one positive and one negative
eigenvalue. This is not a smallness estimate merely from low rank.

There is a scalar relative-conditioning certificate. Put

    delta_n=det(G_(n+1))/det(G_n).

The matrix determinant lemma and positive definiteness give

    delta_n=1-h_(n+1)b_n,     0<delta_n<=1.

For n>=1, apply the inverse rank-one update to G_(n-1)=G_n+h_n r_n* r_n:

    h_n a_n=delta_(n-1)^(-1)-1.

Hence

    epsilon_n^2 <= (h_(n+1)/h_n)
                    (delta_(n-1)^(-1)-1)(1-delta_n).

The exact formula also subtracts h_(n+1)^2 |c_n|^2. This identifies a concrete
quantity to bound and keeps the inverse Gram conditioning in the estimate.
These reflection/determinant consequences are written proofs here, not part of
the current Lean target list unless a later certificate explicitly includes them.

## 5. The full Gram tail: a further analytic consequence

This section is a new deduction from the source functions, not a claim of an
already kernel-checked analytic theorem.

The actual Krylov span is dense in H=L2((0,infinity),dx). To prove it, use the
unitary logarithmic change f(x) |-> e^(y/2)f(e^y), followed by Fourier transform
with kernel exp(i t y), normalized so that the target measure is dt/(2 pi).
The result is M f(1/2+i t). The images of f_j are therefore

    (1/2+i t)^j g(1/2+i t).

Let dmu(t)=|g(1/2+i t)|^2 dt/(2 pi). The function g is entire and not identically
zero, so it is nonzero almost everywhere on this line. Moreover mu has exponential
moments for every exponent a<pi/2. One elementary bound sufficient for this is

    |g(1/2+i t)| <= C (1+|t|)^(11/4) exp(-pi|t|/4).

Here g(s)=s(s-1)pi^(-s/2)Gamma(s/2)zeta(s). The Gamma bound is the standard
vertical-strip estimate (NIST DLMF 5.11.9); a crude bound zeta(1/2+i t)=O(1+|t|)
follows from

    zeta(s)=s/(s-1)-s integral_1^infinity {x} x^(-s-1) dx, Re(s)>0,

first obtained in Re(s)>1 from floor(x), then continued by the convergent
integral. This gives the stated polynomial exponent and exponential decay.

Polynomials are dense in L2(mu). Indeed, if psi is orthogonal to them, the finite
complex measure conj(psi) mu has an exponential moment by Cauchy-Schwarz. Its
Fourier-Laplace transform is analytic on a nonempty strip. Every derivative at
zero vanishes by the polynomial orthogonality, so the identity theorem makes
that transform identically zero. Uniqueness of the Fourier transform of a finite
measure then gives psi=0 mu-almost everywhere. Multiplication by g identifies
L2(mu) isometrically and surjectively with L2(dt/(2 pi)), using g!=0 a.e. This
proves density of the original Krylov span, without a claim about where all the
zeros of g lie.

It follows that P_n -> I strongly in L2 and, for every fixed finite packet,
R_n -> 0 in L2 operator norm and G_n -> 0. Parseval now upgrades the finite
Gram downdate to the actual positive tail formula

    G_n=sum_(j>n) h_j r_j* r_j,

convergent in finite-packet operator norm. Positivity holds at every finite
stage even though the limit is zero.

This does not kill the arithmetic quotient: qR_n=sigma_Z and J_ZR_n=1 still
hold in the original test space at each stage. Rather, these observations are
not continuous for the weaker L2 topology. A nonzero L2-continuous functional
annihilating the dense theta-Krylov span would be impossible. Strong-Schwartz
closedness of the full theta image, if supplied by the separate retraction
construction, is compatible with this weaker-topology density. No new quotient
by the L2 closure is substituted into the programme.

## 6. Independent arithmetic input evaluation and explicit tail bound

The accompanying Wolfram Language script computes the first four unscaled
norm squares from the actual theta polynomials, not a finite matrix model.
At 65-digit working precision and integer cutoff 8 it returned

    1.279007247846485140479533592267...
    13.055549302570558435392684658123...
    250.008976819049914517451258753644...
    6694.666685525627506773475623955402...

These reproduce the displayed source values. They are evaluations, not
validated-rounding certificates. The file records the executable calculation.

Here is an independent bound for the omitted integer terms of the exact 4-by-4
raw Gram matrix. It does not claim to reproduce the source's unavailable tail
checker. Write p_0=4z^2-6z, p_(j+1)=2z(p_j-p_j'), j<=2, and
q_j=sum_(k=0)^j (-1)^k binomial(j,k)p_k. All p_j,q_j for j<=3 have degree<=5
and sum of absolute coefficients <=2898< C=3000. Thus on z>=1 their absolute
values are bounded by C z^5.

The inversion Jf(x)=x^(-1)f(1/x) is unitary on L2(dx); Jf_0=f_0 and
J D^j f_0=(1-D)^j f_0. Splitting at x=1 gives two absolutely convergent integrals
on [1,infinity), whose integer expansions use p_j and q_j. For c>10,

    integral_1^infinity x^20 exp(-c x^2) dx <= exp(-c)/(2c-20),

because log x<=x-1 and x^2>=1+2(x-1). The omitted terms where either integer
exceeds N therefore have entrywise absolute bound

    16 C^2 pi^10 / (2pi((N+1)^2+1)-20)
    * (N+1)^10 exp(-pi(N+1)^2)
        / (1-((N+2)/(N+1))^10 exp(-pi(2N+3)))
    * exp(-pi)/(1-2^10 exp(-3pi)).

For N=8, the expression evaluates to approximately 1.368e-92. A conservative
rigorous consequence is <1e-80 without treating that decimal as an interval
certificate: use 3<pi<4, e^3>20 (its first nine Taylor terms suffice), both
successive-term ratios <1/2, 9^10<10^10 and 20^81>10^105. The two series are
then bounded by 1 and 2e-95 respectively, and the prefactor by 2e14, giving
4e-81<1e-80. This bound is on omitted integer terms, not numerical rounding,
Schur-complement sensitivity or inverse-Gram errors.

## 7. Reproduction and the next bounded step

From formal/splitzero, use the unchanged Lean 4.31.0 and Mathlib commit
fabf563a7c95a166b8d7b6efca11c8b4dc9d911f. The added workflow rebuilds the prior
library and tau sources, checks every new file with --trust=0 and
-DwarningAsError=true, and checks the exact target manifest through #print axioms.
It reruns the old 87, 73 and 28 target audits as well. Only propext,
Classical.choice and Quot.sound are allowed. Python tests validate the audit
harness, not the mathematical theorems.

The next analytic estimate can now be stated on the actual relative tail
quantities in Section 4. A bound epsilon_n -> 0 for every fixed arithmetic packet
would force its exponents to have real part 1/2, by evaluating
v*W_n v / v*G_n v = 2 Re(rho)-1 on an eigenvector. No such uniform smallness
is inferred from h_n growing, G_n decreasing, or rank(W_n)<=2.

## References

National Institute of Standards and Technology. (n.d.). Digital Library of
Mathematical Functions, Equations 5.11.9 and 25.4.4.
https://dlmf.nist.gov/5.11.E9 and https://dlmf.nist.gov/25.4.E4.
These supply standard Gamma asymptotics and the xi normalization, not the
source-specific boundary theorem.

The Lean code reuses the pinned Mathlib orthogonal-projection and quotient
implementations, and the owner's previously checked SplitZero reconstruction.
The source programme and its theta/split constructions remain attributed to
the owner. No claim of global mathematical priority is made for the general
linear-algebra identities or the new formalization.
