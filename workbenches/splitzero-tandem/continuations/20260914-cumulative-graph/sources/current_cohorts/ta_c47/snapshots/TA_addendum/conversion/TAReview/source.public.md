# Independent calculation and review of theta-admitted pole complexes

Date: 2026-09-13. This records the independent calculation supplied while
the root proof `THETA_ADMITTED_POLE_COMPLEX.md` was being written. A final
review seal, if appended below, identifies the complete root version read
and accepted. No source-owner or publication file is edited here. There
is no numerical, arithmetic-zero, Lean, or quotient-positivity certificate.

## 1. Exact admission for the stipulated critical-line norm

Keep the original entire function `v_h=g/h`, with h containing the full
selected zero orders. Its norm on a rational coefficient F is exactly

`integral_R |v_h(1/2+i y) F(1/2+i y)|^2 dy/(2 pi)`.

The parameter y on this line is distinct from the deformation parameter t
in `D=u partial_s+h-t`. Throughout the pole-complex calculation u is fixed
and nonzero. No phase, cancellation, or mass in this integral is replaced
by a discrete or diagonal surrogate.

Let P be the distinct roots of the actual Hermite polynomial nu, and let
O and C be its off-line and critical-line subsets. At p in C put
`m_p=ord_p(v_h)`. If F has an actual pole of order n at p, the weighted
integrand is a nonzero smooth factor times `|y-y_p|^{2(m_p-n)}` locally.
Its integrability is equivalent to `2(m_p-n)>-1`, hence exactly to
`n<=m_p`, since both orders are integers. Apparent terms whose leading
coefficients cancel must first be combined into F's actual Laurent order.

There is no obstruction at infinity for a rational F. This can be checked
from the original source without a new zeta estimate: A1--A3 give
`g=Mellin(Theta phi_*)` with `Theta phi_*` in the strong-Schwartz space.
Its Mellin restriction to any fixed vertical line is a Schwartz Fourier
transform after x=exp(r). Division by h preserves this rapid decay at
infinity, and the selected finite singularities are removable. Rational
functions and their derivatives grow at most polynomially away from
their finite poles. Off-line poles therefore impose no further condition
for this line norm. Indeed every admitted weighted restriction v_h F is
Schwartz on the line, not merely square-integrable.

This statement proves exactly line-norm admission. It does not turn a
meromorphic off-line Mellin multiplier into an entire Mellin transform.

## 2. The maximal two-term norm-admitted complex

Write `PP_p` for finite principal parts at p, and `PP_p^{<=j}=0` for
j<=0. The degree-one admitted rational space and its degree-zero graph
domain are

`A^1=C[s] + direct_sum_{p in O} PP_p`
`              + direct_sum_{p in C} PP_p^{<=m_p}`,

`A^0=C[s] + direct_sum_{p in O} PP_p`
`              + direct_sum_{p in C} PP_p^{<=max(m_p-1,0)}`.

All sums here are direct as polynomial-plus-principal-part vector spaces.
The complex is `[A^0 --D--> A^1 ds]`. It is the maximal such subcomplex
of the analytic localization with the stipulated degree-one admission:

`A^0=D^{-1}(A^1)` inside `C[s,nu^{-1}]`.

Indeed, at a pole of order n>=1 in Q, the highest pole of DQ has order
n+1 and coefficient `-u n` times the leading coefficient of Q. The
multiplier h-t cannot cancel it. Consequently DQ is admitted at a critical
point exactly when Q has no pole or has order at most m_p-1. Such a Q
is automatically in A^1 as well. This proves the asserted maximal graph
domain rather than assuming D preserves the original degree-one space.

Let `S=O union {p in C:m_p>=1}` and `Z={p in C:m_p=0}`. The weighted
analytic residue of AP, with `w=exp((Phi-ts)/u)`, has exactly the image
`C^S` on the admitted complex. Its coordinates on Z vanish identically.
For every p in S, the admitted lift `1/(w(p)(s-p))` gives the p-th
coordinate vector, with its actual weight retained.

If an admitted degree-one F has zero weighted residues, the AP local
primitive construction gives a rational Q with DQ-F polynomial. At a
critical point, Q has pole order at most one less than F, so Q belongs
to A^0; at every off-line point no additional restriction is imposed.
Thus the same proof gives the exact sequence

`0 -> H_pol -> H^1(A) -> C^S -> 0`.

A basis is `1,s,...,s^{d-1}` followed by `1/(s-p)` for p in S.
In particular `dim H^1(A)=d+|S|` and `H^0(A)=0`. Full multiplicities
m_p remain in the cochain spaces and their differentials; the single
residue coordinate per admitted point is a proved cohomological quotient.

## 3. Exact map to AP and absence of an additional kernel

If an admitted F is DQ in the full analytic localization, the graph-domain
identity forces Q into A^0. Therefore the induced cohomology map is
injective: restricting degree zero in this maximal way creates no extra
kernel. Its image is exactly the classes whose weighted residues on Z
vanish. In full, the actual map fits into

`0 -> H^1(A) -> H_loc -> C^Z -> 0`,

where the last map is the corresponding coordinate restriction of AP's
weighted-residue map. This also accounts for all cokernel coordinates.

There is a direct quotient-complex check. At critical p with m_p>=1,
the quotient complex is

`PP_p/PP_p^{<=m_p-1} --D--> PP_p/PP_p^{<=m_p}`.

Its differential is bijective: remove the highest target pole with the
unique predecessor having one lower order, and continue downward; all
remaining target orders at most m_p are zero in this quotient. Injectivity
is the same leading-pole argument. At m_p=0 the quotient is the full AP
principal-part complex with its one-dimensional residue cokernel. At
off-line points the quotient is zero. Hence this computation gives exactly
the preceding short exact sequence and no hidden additional classes.

The operator `L=u partial_t-s` preserves both A^0 and A^1 and commutes
with D. Multiplication by s does not raise any finite pole order, and
t differentiation does not alter these fixed pole bounds. The admitted
connection, weighted-residue transition, and scaling matrix are therefore
AP's matrices with precisely the pole rows and columns in S retained:
`[[A(t),B_S],[0,P_S]]`, `W_S`, and their displayed off-diagonal integral.
This is an invariant subfamily, not a chosen replacement operator.

## 4. Entire-Mellin admission and the actual strong-Schwartz source

For this stronger admission put `m_p=ord_p(v_h)` at every p in P, not
just on the critical line. Since gcd(h,nu)=1, h does not vanish at these
points and this equals `ord_p(g)`. Let

`k=product_{m_p>0}(s-p)^{m_p}`,
`k_0=product_{m_p>0}(s-p)^{m_p-1}`,
`b=k/k_0=product_{m_p>0}(s-p)`.

The empty products are one. The rational coefficients F for which v_h F
is entire are exactly `k^{-1} C[s]`. Their graph domain under D for
u nonzero is `k_0^{-1} C[s]`, by the same leading-pole argument.
The inclusion into the line-norm admitted complex is literal. Its image
on cohomology retains just the residues at points with m_p>0, and it is
injective by the same maximal-domain argument. Thus the difference from
the line-norm domain consists exactly of off-line points where m_p=0.

This stronger space has an exact realization in the original source,
not only a formal entire-function criterion. Set `H=h k`. Every root
of H is an actual g-zero with its full order, and its two factors have
disjoint root sets. The original repeated-root division construction
gives `F_H=S_H Theta phi_*` in the strong-Schwartz space, with Mellin
transform g/H. Consequently

`V(P/k)=P(D_x)F_H`, where `D_x=-x partial_x`,

has Mellin transform `gP/H=v_h P/k`. This proves sufficiency by the
original source construction. Necessity follows because the Mellin
transform of a strong-Schwartz source is entire: every pole of v_h F
must cancel. The coefficient derivative partial_s in D is not D_x;
the latter corresponds to multiplication by s under Mellin transform.

The full source jet map is

`J_H V(P/k)=upsilon_H [P]_H`,

with the actual complete unit `upsilon_H=j_H(g/H)`. On the old polynomial
inclusion the target numerator is kP; restricting to the original h packet
gives `j_h(k upsilon_H P)=upsilon_h[P]`. At newly added roots kP vanishes
to the full corresponding orders. These identities retain all original
jets and the full Taylor units; they do not replace them by leading values.

## 5. Polynomial coordinates for the stronger complex

Under the degree-zero and degree-one denominator identifications, put

`c=b k_0'/k_0=sum_{m_p>0}(m_p-1)b/(s-p)`.

This is a polynomial, including when some or all m_p equal one. The
exact polynomial differential is

`E=u b partial_s+b(h-t)-u c`,

because `k D(P/k_0)=E(P)`. The old polynomial complex embeds by
multiplication by k_0 in degree zero and k in degree one:

`E(k_0 P)=k D(P)`.

If `q=d+deg b`, the leading term of E(P) for nonzero polynomial P
has degree `deg P+q` and unchanged leading coefficient. The derivative
and c terms have strictly smaller degree. Hence E is injective, its
cohomology is free on the degree-below-q remainder basis at fixed
parameters, and its dimension q agrees with the exact residue sequence.

The commuting connection in this numerator basis is also explicit.
`[u partial_t-s,E]=0`, and the last basis column is reduced using
`E(1)=b(h-t)-u c`. Thus its matrix is

`u partial_t-Companion(b(h-t)-u c)`.

It need not be pointwise similar to AP's polynomial-plus-simple-poles
block: their parameter-dependent frame transition is a connection gauge,
whose derivative term must be included. In particular c records the full
multiplicities without changing the original arithmetic packet H.

These coefficient/source maps are degreewise. An exponential boundary
E(P) need not be an arithmetic theta boundary; its exact arithmetic
jet observation is `upsilon_H [E(P)]_H`. No descent through the arithmetic
quotient is asserted by merely writing a strong-Schwartz representative.
Likewise the fixed pair with denominators k_0,k is the maximal graph
domain only when u is nonzero. Setting u=0 in its matrix is not the same
as recomputing the maximal graph domain, which then admits the full
orders m_p in degree zero as well.

## Source and verification scope

The original source identities A1--A3 were reread in
`arithmetic_input.tex`.
Its previously recorded SHA-256 is
`a50b0fb587b644c4ea94dba45b2b423d038f2bfbe7fef188543939ba850e58d2`.
The repeated-root primitive, full-unit section, and exact original source
were read completely in the prior independent scaling work. The accepted
AP proof supplies the already independently checked local weighted-residue
primitive and entire transport, with no change of arithmetic input.

All cohomology assertions above are algebraic. Finite norm of the displayed
representatives does not by itself prove closedness of the boundary range
or a nondegenerate induced quotient norm. This review neither chooses a
new metric nor asserts such a conclusion.

## Full read of the root TA1--19 proof

The complete root TA1--19 note was read after it became available,
including its source, endpoint, and cost paragraphs. No mathematical
correction was required in that version. In addition to the independent
calculations above, the following root extensions were checked directly.

First, the original source identification descends exactly to its stated
arithmetic-quotient value. Multiplying `P(D_x)F_H` by H(D_x) gives
`Theta(P(D_x)phi_*)`, so its Q-class belongs to the actual H-torsion
submodule. The original packet section is inverse to the full jet map
there. This proves the root's
`q V(P/kappa)=sigma_H(upsilon_H[P]_H)` with the complete unit. Applying
the same identity to E(Q) proves the exact nonzero boundary observation;
no assertion of geometric-boundary descent is needed or made.

Second, at the fixed-pair endpoint u=t=0 the geometric polynomial
differential is multiplication by b h. Since b h divides H, the map
`C[s]/H -> C[s]/(b h)` is onto with kernel `(b h)/(H)`.
At an old h-root its kernel is zero, and at an added p it is exactly
`(s-p)/(s-p)^{m_p}`. The kernel dimension is
`sum_{p in S_B}(m_p-1)`, and the quotient dimension is d+|S_B|.
Multiplication by the actual unit preserves this ideal and gives the
stated transported comparison. Recomputing the graph domain at u=t=0
instead uses kappa in both degrees and produces the rank-d quotient.
This verifies both endpoint statements with their distinct domains.

Third, TA17--19 are exact pullbacks of the retained source norm.
For numerator P the weight is `|g/H|^2/(2 pi)`, with the original
unrenormalized mass. Its Gram is positive on every finite polynomial
coefficient space because g/H is a nonzero entire function and a
nonzero polynomial has only finitely many zeros. All moments converge
by the original source's rapid vertical decay. For a fixed matrix E_N,
expanding the original quadratic form gives precisely
`Q^* E_N^* M_H E_N Q`, including every cross term. Composing instead
with the existing arithmetic quotient map and its specified G_H gives
`Q^* T_N^* G_H T_N Q`. These equalities are changes of coordinates in
given forms; they do not define a new quotient norm or infer a uniform
estimate from positive definiteness.

## Complete review of TA20--22 and the frame transport

The full new Section 7 was read, including the explicitly stated column
companion convention, the finite primitive construction of G, its
holomorphic parameter domain, and the source-discrepancy paragraph.
Its formulas agree exactly with the independent connection calculation.

For each numerator vector `s^j/kappa`, the simple-pole AP coefficient at
p is its weighted residue divided by w(p). Expanding kappa at its full
order m_p gives exactly TA21's derivative of order m_p-1 and factorial
`(m_p-1)!`. The complementary factor kappa_p is nonzero at p. After
subtracting those simple poles, AP's primitive reduces the remaining
zero-residue rational coefficient within the admitted degree-zero bound.
Polynomial leading-term reduction then supplies its unique old-polynomial
coordinates. This proves that the displayed finite algorithm computes G
with every required unit, derivative, and residue value retained.

The two bases have already been proved independent and spanning, hence
G is invertible without a separate determinant assumption. The finite
algorithm has only the stated nonzero denominators on u nonzero and
all t; a value h(p)-t=0 does not introduce an unlisted division. Thus
the asserted holomorphic parameter domain is correct, including the
empty-pole case in which G is the identity.

The frame orientation is AP coordinates = G times numerator coordinates.
Applying L gives `u G_t-T_B G=-G A_adm`, which is TA22 with exactly
the negative derivative term in `G^{-1}T_B G-u G^{-1}G_t`.
Differentiating
`G(t)^{-1} C_B(a;t) G(t+ua)` therefore yields
`-C_adm(a;t) A_adm(u,t+ua)`, with initial value identity. This checks
the matrix order, signs, source and target parameter fibres, and both
endpoint frame factors. No pointwise similarity is substituted for the
connection gauge.

The representative differences used to construct this cohomological
frame change are actual D_exp primitives in the strong-source graph
domain. Their source images consequently have precisely the already
computed TA19 cost and TA16 arithmetic boundary value. Keeping this
discrepancy prevents an unjustified source-norm isometry or arithmetic
cohomology descent from being inferred from G.

## Final independent acceptance

The complete root proof TA1--22, including all unnumbered scope statements
and the final source paragraph, has now been read and checked. The exact
accepted artifact is `THETA_ADMITTED_POLE_COMPLEX.md`, SHA-256:

`3f9a79e61de1f38bc0944be4e43b1ef20f02f99b55637f3afa8b773fb38cf8ec`.

Final disposition: accept TA1--22 with no outstanding mathematical
correction. This is a written-proof review of the norm and strong-source
admission, both maximal graph complexes, exact residue images and
injections, full-packet source realization, retained arithmetic boundary
defect, endpoint quotient, actual Gram/cost pullbacks, and connection
frame transport. No numerical fixture, arithmetic-zero evaluation,
Lean replay, uniform metric bound, or new Frobenius identification is
certified by this acceptance.

## Additive review of the exact canonical-metric recovery, TA23--24

The complete Section 8 was subsequently read, including its explicit
coefficient-versus-physical-jet conventions. The preceding TA1--22 seal
and its hash remain a historical acceptance of that earlier version.
The following checks concern the additive TA23--24 continuation.

Set K=deg kappa, so K includes every full added zero order, not merely
the number of distinct added points. With D=deg H=d+K, the stated
cutoff N>=D-1 gives N-K>=d-1. Both coefficient quotient observations
are therefore onto, including the endpoint cutoffs and the empty-added-
packet case K=0. Multiplication by kappa is injective from C[s]/h to
C[s]/H because H=h kappa in the polynomial integral domain.

Fix a coefficient class [P]_h. A representative Q of its image satisfies
`Q-kappa P=H T` if and only if `Q=kappa R` with `[R]_h=[P]_h`.
Because multiplication by the nonzero degree-K polynomial kappa shifts
the degree of every nonzero R by exactly K, the restriction deg Q<=N
is exactly deg R<=N-K. Zero is included separately with no difficulty.
This proves a bijection of the whole affine representative spaces, not
only an injection of selected representatives or a comparison inequality.

The pointwise identity `v_H kappa=v_h` gives equality of the original
norms for each pair of corresponding representatives, with their
original measure and neither source mass renormalized. Positive
definiteness of the finite coefficient Grams gives unique minimizers;
the bijection therefore proves the representative identity in TA23.
Polarization proves its full Hermitian-form identity, retaining all
mixed terms among old quotient directions. The actual source vectors
coincide because `kappa(D_x)F_H=F_h` by Mellin injectivity. Thus there
is no unrecorded source representative or cutoff defect.

The addendum correctly distinguishes G^coef from the physical-jet G^jet
used in TA19. For U_H=M_upsilon_H and U_h=M_upsilon_h, the identities

`G_H^coef=U_H^* G_H^jet U_H`,
`j=U_H i_kappa U_h^{-1}`

give `j^*G_H^jet j=G_h^jet` at the stated respective cutoffs.
On the original h-block, `upsilon_H kappa=upsilon_h` proves that j
is identity. On every added block it is zero through the full order
because kappa vanishes to that order and both units are genuine full
Taylor units. This is precisely the original packet's extension by
zero in physical jets, not the bare coefficient multiplication map
silently reused in a different coordinate convention.

No orthogonality to the added directions follows or is claimed. Their
mutual and mixed Gram entries remain in the extended metric. TA16's
arithmetic boundary value and TA19's full cost are unchanged. Therefore
the addendum establishes an exact restriction of the existing canonical
metrics, without selecting a new metric or deriving a uniform estimate.

## Final acceptance of TA1--24

The complete added Section 8 and its final unit-coordinate clarification
have been read and checked. The exact accepted proof is
`THETA_ADMITTED_POLE_COMPLEX.md`, SHA-256:

`830e9a254465434fd61cb16212544f004ddf54a5adc72554bccabe217b045e5a`.

Final disposition: accept TA1--24 and their stated scope, with no
outstanding mathematical correction. This supersedes only the version
pin of the earlier TA1--22 acceptance, which remains recorded above.
The present addition is a written-proof review of exact cutoff,
minimizer, source-map, and full-unit Gram identities; it includes no
numerical replay, Lean execution, arithmetic-zero evaluation, or
uniform metric-bound claim.
