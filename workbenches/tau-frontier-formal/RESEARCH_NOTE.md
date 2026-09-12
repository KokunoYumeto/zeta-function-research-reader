# Finite frontier estimates and the actual projected cohomology

Owner-directed continuation of the SplitZero/theta programme. This work is on an
additive branch of the verified boundary library, not on another session's branch.
The source for the new targets is the supplied Symmetric Frontier Control note
(12 September 2026), together with the preceding Kernel Layer Integration note.
The source's arithmetic construction remains attributed to the owner and that
research continuation. General Reynolds projection, matrix algebra, and
Cauchy--Schwarz are reused mathematics, not novelty claims.

## Status and unchanged objects

The Lean files are subject to the dedicated exact-head workflow. A pending or
failed run is not a certificate. The PR validation record identifies any completed
successful run. This note describes the intended statements and their proofs;
read the final run status before calling them kernel-checked.

The base remains the marked tau object with the square G(Z) -> G(C) over Z -> C.
The original scalar G(R), supported zero e, external absence tau, test-function
spaces V and B, theta map, arithmetic quotient q:B->B/Theta V, D=-x partial_x,
and normalization g=2 xi are not changed. Neither the source's full spectral jets
nor its arithmetic unit j_h(g/h) are replaced by reduced evaluations.

The local execution service failed before the new ZIP could be inspected. The
complete supplied markdown and available pinned repository sources were read.
No verification of that archive's manifest or rerun of its 22 regression methods
is claimed. The mathematical text is available independently of the archive.

## 1. Deriving the finite incidence estimate

This section gives the local algebraic calculation behind the source's Gamma.
Let i range through k coordinates. On degree M let R_i raise coordinate i with
coefficient sqrt(a_(alpha_i+1)), and let L_i lower it with coefficient
sqrt(a_(alpha_i)), with a_0=0. They land in different spaces: degree M+1 and
M-1 respectively. These spaces are not identified.

For distinct i,j the coefficient shift operators give

    Re <R_i x,R_j x> = Re <L_i x,L_j x>.

One way to verify the equation is to commute the two different-coordinate
operations, using R_i^*=L_i, then use conjugate symmetry. Thus, on the underlying
real Hilbert spaces,

    ||sum_i R_i x||^2 - ||sum_i L_i x||^2
      = sum_i (||R_i x||^2 - ||L_i x||^2).             (1)

Proof: expand the two squared sums as double sums. All off-diagonal differences
vanish. The remaining diagonal entries are precisely the right side.

Cauchy--Schwarz on the k lowering vectors gives

    ||sum_i L_i x||^2 <= k sum_i ||L_i x||^2.

Substitution in (1), with c_alpha=|x_alpha|^2, gives

    ||sum_i R_i x||^2
      <= sum_alpha [sum_i a_(alpha_i+1)
                     +(k-1)sum_i a_(alpha_i)] c_alpha
      <= Gamma_(k,M) sum_alpha c_alpha.              (2)

Here Gamma_(k,M) is exactly the maximum printed in the source, not k times an
independently selected one-factor estimate. No monotonicity of a_n is used.
The source coefficient and all normalizing norm ratios remain explicit.

`SplitZeroIncidenceEstimate.lean` proves (1), the finite vector Cauchy--Schwarz
step, the k-1 estimate, and the final diagonal maximum bound. Its hypotheses are
the local off-diagonal identities and the exact diagonal sums. It does not
postulate (2) as a field of an input structure. The construction of all-degree
polynomial operators and their analytic norm sequence remains an instantiation
of these finite lemmas; it is not included by asserting that the variables have
arithmetic names.

## 2. The cross bound and its precise arithmetic substitution

Let H be any complex inner-product space. For q,gamma,lambda >= 0 and x,y in H,
suppose

    ||x||^2 <= lambda q,       ||y||^2 <= gamma q.

Then

    |Re(<x,y>+<y,x>)| <= 2 sqrt(gamma lambda) q.       (3)

Proof: the left side is |2 Re<x,y>|, at most 2||x||||y||. Multiplying the two
squared inequalities and taking nonnegative square roots proves (3). This proof
also handles q=0 or either cost equal to zero, without division by those values.

`SplitZeroFrontierEstimate.lean` proves (3), both order inequalities, the
actual-linear-map version, a variant retaining separate rational norm budgets,
and an instantiation for the previous library's actual negative boundary form.

For the supplied source choose

    x = Omega^(-1/2) F* v,
    y = Omega^(-1/2) E_+* v,
    q = v* C_M v,       C_M = G_M^(-1).

The definition of lambda_(k,M) supplies the first squared inequality; (2),
through the supplied jet map, supplies the second. The actual source identity
Z_M=F Omega^(-1) E_+*+E_+ Omega^(-1) F* then yields the stated finite bound.
This is the written source-to-code substitution. Constructing the analytic
moment matrix and proving its source incidence hypotheses remains separate.

No decay of Gamma lambda with k is inferred. In particular a finite upper bound
alone is not the sublinear arithmetic bound needed for amplification.

## 3. The signed projection is a cochain map before homology

Let rho be a representation of a finite group Gamma on a complex module. The
literal Reynolds operator is

    P_rho = (1/|Gamma|) sum_g rho(g).

Its image consists of invariant vectors, and it fixes those vectors. These are
Mathlib's `averageMap_invariant` and `averageMap_id`, reused on the unchanged pin.
An actual intertwiner f satisfies f P_rho = P_sigma f, by interchanging f with
the finite sum. Hence an action on each term of a cochain window, commuting with
the original differentials, gives a cochain idempotent.

For a character chi:Gamma->C with chi(g)^2=1, twist a supplied representation by
chi(g). The library constructs this representation and proves the literal signed
average formula. If the top-degree action is T_g=chi(g)rho(g), the second sign
cancels the first, so the signed top projector is P_rho. A rho-invariant vector
is fixed, not lost by a sign convention.

For Gamma=S_k in the source, chi is the sign character and the given Koszul
formula is T_pi=sgn(pi)P_pi on degree k. Therefore the signed projector keeps
v^(tensor k), whenever that vector is supplied. This file proves the both-sign
cancellation for arbitrary supplied character/actions; it does not claim to
construct every permutation of completed topological tensor products in Lean.
The original analytic completed tensor construction must supply that action.

`SplitZeroSignedProjector.lean` constructs the average cochain map on the existing
`SplitZero.Homology.Window`, proves its induced homology operator idempotent,
proves preservation of invariant cycle classes, and keeps the complementary
operator 1-P_H with its own idempotence and sum-to-identity formula.

## 4. Homology of the projected subcomplex, not a post-hoc definition

Let C be any cochain complex over a commutative ring and p:C->C a cochain
idempotent. At each degree construct the actual fixed submodule

    C_p^i = {x in C^i : p^i x=x}.

The differential restricts since dp=pd. There are cochain maps

    i:C_p->C,       r:C->C_p,       r(x)=p(x),

with r i=1 and i r=p. Passing through the original cycles-and-boundaries quotient
therefore gives r_H i_H=1 and i_H r_H=p_H. In particular

    H^i(C_p) ~= {u in H^i(C) : p_H u=u}.              (4)

The maps in (4) are i_H forward and r_H backward. The two identities prove both
inverse laws. Fixed vectors of an idempotent are also its image: fixed u has
preimage u, while p(pv)=pv. Thus (4) is the claimed selected cohomology summand,
with the original quotient and original cycle representatives retained.

`SplitZeroProjectedHomology.lean` constructs the restricted window, inclusion,
projection, their homology maps, and this linear equivalence. It then builds
all idempotence inputs from the actual finite-group average of the preceding
file. It reuses, rather than replaces, the previous homology implementation.
The earlier adapters from Mathlib integer-degree cochain complexes remain valid.

This is the bounded algebraic theorem needed for the source's signed symmetric
summand. Its completed topological Kunneth identification is still provided by
the source's separate analytic contraction; it is not a new axiom here.

## 5. Preserve the orbit factors in the metric

Let I:C^d->C^n be the inclusion of unscaled orbit sums, L:C^n->C^d their
coefficient extraction, and P=I L. Suppose

    L I=1,      P*=P,      P K=K P,      G K=1.

Then

    (I* G I)(L K L*)=1.                              (5)

Proof: the product is I* G P K L*=I* G K P L*=I* P L*=I*L*=1.
For I*P=I*, transpose PI=I and use P*=P. Every multiplication is typed; I and L
are rectangular, not inverses between equal-dimensional spaces.

For the actual orbit basis, D=I*I is the diagonal of orbit cardinalities and
L=D^(-1)I*. The metric commutes with P because the canonical representative
intertwines variable permutations and the ambient measure is permutation
invariant. Thus (5) gives

    G_sym=I*GI,       C_sym=L C L*,

with exactly the source's orbit multiplicities. Without the commutation
hypothesis, arbitrary inverse compression is false; the hypothesis is retained
in the formal statement.

For AI=I A_sym, the same file proves

    I*(A*G+GA-wG)I = A_sym*G_sym+G_sym A_sym-wG_sym.

It also proves, for K=G^(-1), the full-jet kernel congruence

    K(A*G+GA-wG)K = AK+KA*-wK,                        (6)

and the inverse witnesses under a square coordinate change. These identities
retain the original real weight w; w=k on the product construction. Formula (6)
is a change along an explicit invertible map, not an independently chosen
metric on a different arithmetic packet.

The complementary trace remains

    Tr(PA)+Tr((1-P)A)=Tr(A).

Multiplication by the source's cohomological sign (-1)^k gives the corresponding
supertrace identity. The full cycle-index trace formula and the all-k partition
counts are not part of this finite matrix certificate.

## 6. What the support and arithmetic interfaces still require

All new algebraic constructions are over the previous original modules and
homology quotients. At a fixed invariant support label they pass through the
existing Hom.total, which sends a zero amplitude to that fibre's zero. For a
non-invariant support, the source's signed average first transports to the
orbit join of labels. The prior HomOver infrastructure has the correct type for
that map. This new contribution does not falsely claim to have instantiated
the entire orbit-join action or completed analytic tensor homotopy.

The finite projector does not turn a nonzero source into external absence. Its
complement is explicitly retained. In particular selecting the symmetric
summand does not assert that all other mixed-support data vanish.

The next instantiations are the exact weighted degree-shift operators on every
multi-index, their source theta primitive maps, the full-jet minimum as an actual
Lean linear equivalence, and orbit-indexed maps for the completed tensor
complex. No arithmetic kernel vanishing, purity, RH, or GRH is claimed by the
finite identities alone.

## Coordination and references

At the inspected revisions, Codex #16 (40346cbda35df1bc0242b8fdd449670d4af19a80)
contains another four-mask homotopy integration. Its latest inspected workflow
was not successful; a code file existing in the repository is not a certificate.
It was left untouched. The #17 handoff (33b29f706008124886614ba4bd55bffc489df9e2)
adds spectral-sum, transverse-coordinate and nilpotent-ladder targets. This
contribution does not duplicate their modules or edit their branches.

The owner-provided Symmetric Frontier Control markdown, Sections 4--6, is the
source for Gamma, the signed symmetric projection and orbit-coordinate targets.
The Kernel Layer Integration supplement is the source for the primal/kernel
interface. Both precede this formalization; neither is presented as newly
discovered here.

The mathlib Community. (2026). RepresentationTheory/Invariants and Data/Matrix/Mul
[Lean source files, revision fabf563a7c95a166b8d7b6efca11c8b4dc9d911f].
https://github.com/leanprover-community/mathlib4/tree/fabf563a7c95a166b8d7b6efca11c8b4dc9d911f

The Stacks Project Authors. (n.d.). Tensor products of complexes (Tag 0GWN).
https://stacks.math.columbia.edu/tag/0GWN
The source uses its Koszul convention; our current algebraic file takes the
specified group action and proves the consequent both-sign cancellation.
