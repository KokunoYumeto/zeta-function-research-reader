# Independent review of analytic pole-residue transport

Date: 2026-09-13. This reviewer read the complete
`ANALYTIC_POLE_RESIDUE_TRANSPORT.md`, originally AP1--24, its unnumbered
assertions, and its provenance and scope paragraphs. The revised AP19a--b,
AP25--26, and their complete surrounding proofs were then read as well.
The formal-unit gauge and the
original scaling proof were independently reviewed or derived in the
adjoining work. This review changes neither the source proof nor its sources,
and does not certify an arithmetic-zero computation, a metric estimate,
an analytic evaluation of the formal inverse, or a Lean result.

## Disposition and the one local edge case

Accept AP1--26, including AP19a--b, and their proofs. The weighted-residue
exact sequence, the coupling into polynomial cohomology, the off-diagonal
transport integral, the actual unit gauge, and the ordinary dual have the
correct domains, signs, and matrix order. Neither repeated roots of \(h\) nor
the multiplicities of \(\nu\) need to be removed.

One unnumbered sentence in Section 7 was reported for correction before
sealing this review. The claim that the full residue exponential and its
\(t\)-derivative still contain \(t/u\) when its exponent vanishes requires an
exception for a pole point \(p=0\). The exact derivative is
\(u\partial_t w(p)=-p w(p)\). If \(p=0\) and \(\Phi(0)=0\), then
\(w(0;u,t)=1\) identically and its \(t\)-derivative is zero. If \(p=0\) and
\(\Phi(0)\) is nonzero, it is independent of \(t\) and has an essential singularity
only in \(u\). For \(p\) nonzero, the displayed two-parameter exponential retains
its \(t/u\) dependence. This comment concerns only that local prose assertion;
AP11, AP18, and all the numbered formulas already have the correct factors.

## Pole quotient: all maps and exactness

For fixed \(u\) nonzero, the quotient
\(M=\mathbb C[s,\nu^{-1}]/\mathbb C[s]\) is the vector space of finite principal parts at
the distinct roots of \(\nu\). Although \(\nu\) can have repeated roots, localization
allows every finite pole order at each such point. Polynomial differences
are killed only in this quotient. Multiplication by the entire nonvanishing
weight \(w\) does not define a rational multiplier, and the proof does not use
it as one: its uses are local meromorphic products and contour integrands.

The residue functional descends to \(M\) because \(w\) times a polynomial is
holomorphic at all the designated points. The identity
\(w DQ=u(wQ)'\) proves that its composite with \(D\) is zero, retaining \(u\).
If a principal part of \(Q\) at \(p\) starts with \(c(s-p)^{-n}\), its derivative
contributes the uncancellable highest pole
\(-u n c(s-p)^{-n-1}\). Thus \(D\) is injective on \(M\).

For a zero-residue \(F\), each Laurent series \(wF\) has a meromorphic primitive
\(H_p\) without a logarithm. The function \(H_p/(u w)\) is meromorphic locally
and satisfies \(DQ_p=F\). Taking its finite principal part, and summing over
the finitely many points, gives a rational \(Q\) with only allowed poles.
The difference \(DQ-F\) is rational and holomorphic at every finite point,
hence polynomial. No global analytic primitive or rationality of \(w\) is
assumed. A change of integration constant contributes a holomorphic germ
because \(w\) never vanishes, so the principal part does not change.

The explicit lift \(1/(w(p)(s-p))\) has weighted-residue vector exactly the
\(p\)-th coordinate vector, including its nonzero phase and mass. This proves
surjectivity. These arguments establish all of AP3. AP4 is the literal
Taylor expansion of \(h\) and the Laurent-residue formula for \(w\), so its
factorials, derivative order, \(t\) term, and leading sign are correct.

## Polynomial injection and the displayed basis

For nonzero polynomial \(Q\) of degree \(n\), \(DQ\) has degree \(n+d\), since \(h\) is
monic and \(d>0\). Therefore \(D\) is injective on polynomials, and recursive
leading-term subtraction gives a unique remainder of degree below \(d\).
For a rational \(Q\) with polynomial \(DQ\), the preceding highest-pole argument
first forces \(Q\) to be polynomial. Thus localization kills no original
polynomial cohomology class.

AP3 now gives AP5 with the indicated kernel and surjection. Subtracting
\(\sum_p(\operatorname{Res}_w F)_p/(w(p)(s-p))\) removes all weighted residues; reduction
then leaves exactly a degree-below-\(d\) polynomial. Conversely, applying
the residues to a linear relation among AP6's vectors kills every pole
coefficient, and polynomial injectivity kills the rest. The dimension
is therefore \(d+r\) for \(u\) nonzero, with the original rank-\(d\) object explicitly
injected. These statements include \(\nu\) constant, when \(r=0\) and the additional
maps and blocks have zero size. No squarefreeness of \(h\) is used.

## Connection, frames, and entire transport

AP7's two nonzero commutators are \(-u\) and \(+u\), so \(L\) commutes with \(D\).
Its action on the last polynomial basis vector uses only \(D(1)=h-t\);
it is the companion block \(A(t)\). On a simple pole,
\(-s/(s-p)=-1-p/(s-p)\). Consequently the upper-right block of
\(A_{\mathrm{ext}}\) is the constant column \(e_0\) repeated once per pole, with the
positive sign in \(A_{\mathrm{ext}}\) and the negative sign in \(L\). All of AP8--10 follows
without asserting that multiplication by \(s\) alone descends on the quotient.

The residue row is \([0,W]\), and \(u W_t=-P W\). Thus
\(\operatorname{Res}_w L=u\partial_t\operatorname{Res}_w\), both by direct differentiation and by
multiplying the block matrices. The normalized vector \(r_p/w(p)\) has
\(L(r_p/w(p))=-1/w(p)\): the two terms with \(p\) cancel exactly.
AP13's diagonal frame change is therefore correct, without replacing
the original \(W\) by identity.

For the source-to-target flow from the fibre at \(t+ua\) to the fibre at \(t\),
the ODE must be \(C_{\mathrm{ext},a}'=-C_{\mathrm{ext},a}A_{\mathrm{ext}}(t+ua)\). Its upper-right block
therefore obeys \(K_a'=-C_a B_0-K_a P\), with zero initial value.
The integral in AP15 solves exactly this equation; in particular its
\(C_b\) is on the left of \(B_0\) and its final exponential is on the right.
The integrand is entire in the integration variable and the finite
matrix ODE gives the asserted entire continuation. The inverse block,
shifted groupoid law AP17, and weighted-residue identity AP18 follow
with the stated order and signs. Since \(W\) never vanishes for \(u\) nonzero,
none of these operations silently discards a residue coordinate.

The formal flow on rational representatives is only coefficientwise in \(a\).
The note correctly obtains nonzero-\(a\) transport from finite matrices rather
than treating \(\exp(-as)\) as a rational cochain multiplier. The ODE matrix
can extend to \(u=0\) without its \(d+r\) representatives becoming a cohomology
basis at that endpoint.

## Contours, actual gauge, and ordinary dual

Counterclockwise small loops give exactly \(2\pi i\operatorname{Res}_w\), not the
normalized residue alone. The original rapid-decay contours have their
finite portions routed away from the designated poles, including zero
if necessary. Polynomial periods are unchanged because their integrands
are entire; different rational routings can change periods by precisely
the retained small-loop periods. The infinite rays are unchanged, so
their original rapid decay dominates the rational factors. Local uniform
domination on the admitted \(u\)-sector and bounded parameter sets justifies
the asserted differentiation in \(t\).

In these actual contours the extended period matrix has the block form
of AP19a. Its determinant is \(\det(\Pi_{\mathrm{pol}})(2\pi i)^r\prod_p w(p)\),
with no missing factor or sign for the stated counterclockwise loops.
The original nonzero polynomial determinant and nonvanishing of each
\(w(p)\) prove invertibility. Boundaries integrate to zero along these
contours, so the connection calculation gives
\(\partial_t\Pi_{\mathrm{ext}}=-\Pi_{\mathrm{ext}}A_{\mathrm{ext}}/u\). Consequently
\(\Pi_{\mathrm{ext}}(u,t)^{-1}\Pi_{\mathrm{ext}}(u,t+ua)\) solves AP16 with the correct initial
value. This proves AP19b for fixed nonzero \(u\) and does not evaluate any
period matrix at \(u=0\).

Leibniz differentiation verifies
\(D^\nu=u\partial_s+h-t-u\nu'/\nu\). Multiplication by \(\nu\) in both
degrees is an isomorphism on the explicitly localized complexes. The
equalities in AP21 prove exact equality of weighted periods, including
all multiplicities in \(\nu\) and the original constant in \(\Phi\). It is correct
that the target representative \(\nu/(s-p)\) can be polynomial: its weighted
form still has the relevant simple pole. The image of the old polynomial
subspace is represented by \(\nu\) times that frame, not by a silently
unchanged polynomial frame in the new differential.

Dualizing the finite-dimensional exact sequence gives AP22 with reversed
arrows. The injected dual column is \((0,W^T\alpha)\). Acting by
\(\partial_t+A_{\mathrm{ext}}^T/u\) gives \((0,W^T\alpha')\), since
\(W_t^T=-W^T P/u\) cancels the lower diagonal block, and the upper component
remains zero. The inverse transpose is the correct forward transport of
functionals under the gauge. This is an ordinary linear-dual statement;
it neither supplies a Hermitian positivity assertion nor replaces the
original \(\tau\)-base conjugation or moment-line twist.

## Formal endpoint and limits of the result

The coefficientwise formal inverse of the earlier note is not evaluated
at a nonzero \(u\) here. The distinction is essential: AP3 directly computes
its nonzero-\(u\) residue cokernel, whereas the formal pole complex is
contractible because \(h\) is invertible on \(M\) and the perturbation raises
parameter order. These are different coefficient operations on the same
original rational complex, not contradictory dimension assertions.

For \(p\) a root of \(\nu\), \(h(p)\) is nonzero. Multiplying AP23's displayed
polynomial by \(s-p\) gives \(1-h(s)/h(p)\), proving its exact inverse identity
in the full quotient, including repeated roots. Directly setting the
cohomology class of \(D(1/(s-p))\) to zero gives AP24 with its positive
\(u\) term and negative divided-polynomial term.

In particular, if \(Q_0\) has these AP23 polynomials as columns, then
\(A Q_0=B_0+Q_0 P\). The specialization map from the \(d+r\) displayed lifts
to the actual rank-\(d\) endpoint is \([I,Q_0]\), and it intertwines \(A_{\mathrm{ext}}(0)\)
with \(A\). This confirms the note's endpoint distinction without assigning
\(d+r\) independent classes to the formal special fibre.

The affirmative result is the fully computed analytic extension, its
weighted residues, connection transport, actual-unit gauge, and linear
dual, together with their precise original polynomial subobject. No
uniform metric bound or unconstructed Frobenius identification follows
from this review.

## Revised endpoint and empty-pole clarification

The revised AP25--26 include the preceding explicit endpoint check.
The kernel of \([I,Q_0]\) is precisely \(\{(-Q_0 c,c)\}\), and
\(A_{\mathrm{ext}}(0)(-Q_0 c,c)=(-Q_0 Pc,Pc)\). Its dimension is \(r\), including
the zero-dimensional case, and the induced quotient action is the
original \(A\). At \(u=t=0\) the matrix ODE has constant coefficient \(A_{\mathrm{ext}}(0)\),
so exponentiating the intertwiner proves AP26. The original full unit
multiplier commutes with \(A\) on the full algebra, which also verifies the
stated gauge endpoint without dropping any Taylor coefficient.

The corrected \(p=0\) discussion separates all exceptional cases accurately.
For each existing pole \(p\), the highest inverse-\(u\) term in
\(w^{(n)}(p)/w(p)\) is \((h(p)-t)^n/u^n\); its coefficient is nonzero
at \(t=0\) because \(h(p)\) is nonzero. In the usual \(u\)-adic scalar topology,
one can see the noncontinuity explicitly even after dividing out \(w(p)\):
the source sequence \(u^n/(s-p)^{2n+1}\) tends to zero, whereas its
normalized residue at \(t=0\) has \(u\)-valuation \(-n\), with nonzero leading
coefficient \(h(p)^{2n}/(2n)!\). Thus the weighted-residue operation is
not a coefficientwise continuous extension to the earlier formal pole
module. No claim that \(w(p)\) itself is always singular is required.

The last argument presupposes at least one pole. A final local wording
comment therefore asked that Section 7's "nonzero cokernel" and
noncontinuous-residue assertions be explicitly qualified by \(r>0\).
For \(\nu\) constant, the pole module, residue cokernel, and residue map
are all zero; the zero map is continuous. This is the complete
degenerate case, not an exception to AP3 or any matrix formula.

## Final acceptance seal

On 2026-09-13 I reread the revised pole-factor discussion and both explicit
\(r=0\) qualifications. The \(p=0\) and empty-pole comments above are preserved
as the historical review record; neither remains an outstanding correction.

The exact accepted proof is `ANALYTIC_POLE_RESIDUE_TRANSPORT.md`, SHA-256:

`357923aead35c77f2fa98598fbc4ed8bc1f7cd6ebc04760da504a0ded765a652`.

Final disposition: accept AP1--26, including AP19a--b and all accompanying
scope statements, with no outstanding mathematical correction. This is a
complete independent written-proof review of the residue exact sequence,
full connection and period transport, actual-unit gauge, ordinary dual,
and original formal endpoint. No numerical fixture, arithmetic-zero
certificate, Lean replay, positive metric estimate, or additional
Frobenius comparison is certified by this seal.
