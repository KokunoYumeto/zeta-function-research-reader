# Exact mapping-torus convention check after the companion seal

This is a new mathematical source check for a later additive update. It does not modify the sealed 36-page companion or the accepted 726-page mathematics. It proves the even-to-odd boundary for explicitly fixed maps. The accompanying ODD_BOUNDARY.md and DOWNSTREAM_USE_RECONCILIATION.md complete the odd boundary and the identified direct uses.

## Authenticated source

Bruce Blackadar, *K-Theory for Operator Algebras*, author-hosted corrected second edition: <https://www.bruceblackadar.com/Mathematics/book6.pdf>. The author's publication page <https://bruceblackadar.com/mathpubs.html> identifies the edition. Acquired 17 September 2026, 1,562,151 bytes, SHA256 `a20e676e9d400ebcd0cd07c13fbdbe1fac759a30c739fab23d6161ecfb1a23fb`.

Visually read printed pp.64,68,74,76 (PDF pp.78,82,88,90): Definition 9.1.1 fixes the positive-circle Bott representative;9.3.2 gives the positive exponential boundary; Definition 10.3.1 gives the forward endpoint relation. Proposition 10.4.1 prints the opposite-sign expression and reversed affine path. Exact ideal inclusion and orientation must be specified before using its sign. This report derives the result directly for the maps below.

## Objects and maps, with no implicit orientation change

Let A be a C*-algebra and alpha an automorphism. Extend alpha to the unitization by fixing scalars and entrywise to matrices. Set

    SA = C_0((0,1), A),
    M_alpha = {f in C([0,1],A): f(1)=alpha(f(0))}.

The ideal injection j:SA -> M_alpha is extension by zero at both endpoints, with the same increasing coordinate t. The quotient is pi(f)=f(0). Its kernel is exactly j(SA): pi(f)=0 implies f(1)=alpha(0)=0, and the reverse implication is immediate. It is onto, since a has the continuous lift h_a(t)=(1-t)a+t alpha(a). Thus

    0 -> SA --j--> M_alpha --pi--> A -> 0

is the specified exact sequence. Use the exponential boundary delta([p]-[e])=[exp(2 pi i h_p)] from 9.3.2 and the positive Bott map

    beta_A([p]-[e]) = [t |-> exp(2 pi i t p) exp(-2 pi i t e)],

where p is a projection in M_n(A^+) and e is its scalar image (after the usual scalar basis choice, a diagonal projection). The formula is precisely 9.1.1 with z=exp(2 pi i t). The loop is scalar1 and has endpoint1. No replacement of t by1-t is made.

## Exact even-to-odd boundary calculation

Put q=alpha(p). Then q and p have the same scalar image e. The self-adjoint lift is

    h_p(t)=(1-t)p+t q.

It has the required endpoints p,q, scalar image e, and pi(h_p)=p. Its exponential u(t)=exp(2 pi i h_p(t)) therefore belongs to the unitization of M_n(SA), is scalar1 and equals1 at both endpoints.

For s,t in[0,1], define the explicit homotopy

    H(s,t)=exp(2 pi i ((1-s)(1-t)p+t q)) exp(2 pi i s(1-t)p).

Every factor is unitary because its exponent before multiplication by i is self-adjoint. Norm continuity follows from the norm-convergent exponential power series on the bounded parameter square. At t=0 both factors are functions of p, so H(s,0)=exp(2 pi i p)=1. At t=1, H(s,1)=exp(2 pi i q)=1. Its scalar image is

    exp(2 pi i ((1-s)(1-t)+t)e) exp(2 pi i s(1-t)e)
      = exp(2 pi i e)=1.

Consequently H is a homotopy of loops in the unitization of M_n(SA). Its ends are

    H(0,t)=u(t),
    H(1,t)=exp(2 pi i t q) exp(-2 pi i t p),

using exp(2 pi i(1-t)p)=exp(-2 pi i t p), since p is a projection. The last loop factors exactly, without commuting p and q, as

    (exp(2 pi i t q) exp(-2 pi i t e))
    (exp(2 pi i t e) exp(-2 pi i t p)).

The second factor is the inverse of the Bott loop for p. Multiplication of loops represents addition in K1. It follows that

    delta([p]-[e])
      = beta_A([q]-[e])-beta_A([p]-[e])
      = beta_A((alpha_*-id)([p]-[e])).

Projection differences generate K0(A), so this proves the exact homomorphism identity

    beta_A^{-1} o delta = alpha_*-id

for the fixed forward injection, evaluation at0, positive exponential and positive-circle Bott map. No commutativity of p and alpha(p) is required.

## Exact relationship to the opposite convention

Let M_rev={g:g(0)=alpha(g(1))}, with quotient pi_rev(g)=g(1) and the forward-coordinate zero-endpoint inclusion. Time reversal rho(f)(t)=f(1-t) is a *-isomorphism M_alpha -> M_rev: the endpoint equation follows by substitution; pointwise multiplication and adjoints are preserved; rho composed with itself is the identity. Also pi_rev o rho=pi. On the ideal it induces r(a)(t)=a(1-t).

For the positive Bott loop v_p(t)=exp(2 pi i t p)exp(-2 pi i t e), time reversal gives

    v_p(1-t)=exp(-2 pi i t p)exp(2 pi i t e).

Its K1 class is the negative of [v_p], since it is the product of the inverse p-loop and the positive e-loop in the ambient loop group; equivalently these two factors represent the reversed based loop. More directly, a based loop and its reversed traversal concatenate to a null-homotopic loop by contracting the outgoing and returning path lengths together. Thus r_* beta_A=-beta_A. Naturality of the exponential boundary under rho can also be checked directly by composing h_p with1-t. Hence

    beta_A^{-1} o delta_rev = id-alpha_*.

This supplies the exact map relating the two sign presentations. Reversing the chosen suspension identification has the same sign effect. The abstract occurrence of id-alpha_* alone is therefore not a defect; its compatibility with the displayed maps is the issue.

## Concrete check and retained limitation

For A=C^3, let p=e1 and alpha(e1)=e2 in a three-cycle. The valid lift is((1-t),t,0), so its exponential has component winding numbers(-1,+1,0), exactly alpha_*[p]-[p]. The reversed affine path(t,1-t,0) violates the forward endpoint equation: its initial value is e2 and its final value e1, whereas alpha(e2)=e3.

The source's printed affine-path expression matches the reversed convention. The companion files now pin the historical suspension identification, prove the odd-to-even map, and reconcile the named downstream uses. Preserve its historical record and attach explicit convention data before propagating a corrected sign. Do not treat a catalogue mismatch as a failure of Pimsner–Voiculescu exactness or as an obstruction to the accepted zeta continuation.
