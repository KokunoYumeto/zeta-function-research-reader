# Boundary-layer integration over the original tau base

## Source, scope, and placement

This is an additive formalization of the owner’s SplitZero programme. It builds on the verified tau library at `5d2772ea0a16d177ac3e01ff70394b90ba95a232` (PR #12). The companion written research source is PR #13 at `e7ba4c29d4503bf20d06cb70c93c3347f199f1b4`, together with the supplied “Pasted markdown(20260912-154311).md” (SHA-256 `96b9d523ed336f96b2822e1636fe8e9b9ed104e3743b1b8b56729b2e8439f818`). Neither companion branch is modified.

The scalar core, marked arithmetic quotient, four-point tau chart, and original reconstruction are imported rather than redefined. The new code concerns support-changing morphisms, the complete joint-support homotopy, actual relation quotients, orthogonal representatives, the one-layer boundary pairing, and the finite rank-two calculation.

Statements here are separated into encoded Lean conclusions and the analytic inputs required to instantiate them. The exact successful commit/run and source hashes belong to the verification receipt and PR record. A source file or a regression test alone is not a kernel certificate.

### Coexistence with the established boundary library

PR #15 at `21970bbf4760d0bbca512a4a7996a2e38f968947` is retained intact, including its original support/relation files, all five modules, and 38-target audit. This integration's support and relation additions live in `SplitZeroSupportChangeIntegration.lean` and `SplitZeroRelationLayerIntegration.lean`, importing those originals. Their namespaces coexist: `SupportMap/HomOver` and `ReindexedHom` retain their respective presentations; the original bundled `RelationLayer.Data` and the unbundled quotient maps retain their original domains.

For every original `S : RelationLayer.Data R B`, `transport S.lower S.upper S.inclusion = S.transition`. For the same derivative `D` and preservation proof, the two derivative maps are also equal. Both are definitional equalities proved in Lean, with the same ambient representatives and no changed quotient. The 66 prior integration targets and these two compatibility equalities have their own 68-target manifest; neither manifest replaces the other.

The active-support nonabsence proof uses the actual extensive support map: if `syncIndex A = empty`, then `A <= syncIndex A = empty`, whence `A = empty`, contradicting the original nonempty-support hypothesis. This changes only the proof script, not the theorem or its hypotheses.

## 1. The support-changing map is part of the morphism

For existing linear join diagrams D over L and E over K, a `ReindexedHom D E` consists of a join-and-bottom-preserving map f:L->K and linear maps D_i->E_(f i), with the naturality squares for the given transports. The implementation constructs its actual G(R)-linear total map

    (i,x) |-> (f(i),u_i(x)).

Join preservation proves additivity of the reconstructed sum; bottom preservation handles the external scalar zero. The supported scalar action is inherited from the original `LinearDiagram.totalModule`. An existing fixed-index `Hom` embeds with exactly its existing total map.

If u_i(x)=0, the image is (f(i),0). If f(i) is not bottom, this is proved different from the global zero. No injectivity of an arbitrary support transport is assumed.

Declarations: `ReindexedHom.total`, `killed_fibre`, `killed_not_absent`, `supported_zero`, and `Hom.reindexed_total`.

### The actual four support masks

`SplitZeroJointHomotopy` uses L=P({false,true}). Degree zero has the submodule of V×V in which absent coordinates must be zero. Thus singleton masks have one actual coefficient leg, the joint mask has two, and the empty mask has only the zero pair. Degree one has a copy of B on each active mask and a zero bottom fibre. The inclusions and differentials are constructed.

Synchronization has index empty->empty and active->joint and includes each coefficient into that joint fibre. The differential is the imported

    d(v,w)=Theta(v-Fw),

with the same Theta and F as `TauHomotopy`. Every linear H:B->V×V has a constructed support-changing lift to the joint face.

For every member H of the existing complete homotopy classification, the code proves the two typed equations

    d_total H_total = sync_B (Theta kappa)_total,
    H_total d_total = sync_V (zero-fibre-map)_total.

The second equation is a joint fibre zero on active input, not an externally zero map. The first equation uses the very differential from the preceding chart. `classifiedLift` applies this construction to every parameter in `cochainHomotopyEquiv`.

This does not add a new analytic Fourier theorem or claim polynomial-linearity of an arbitrary complex-linear homotopy.

## 2. The admitted relation layer is an actual kernel

For submodules U<=W of the same R-module B, `transport U W` is the quotient map

    B/U -> B/W, [x]_U |-> [x]_W.

Its vanishing criterion is exactly x in W. Its kernel equivalence reuses the earlier `Homology.quotientKernelEquiv`; it does not replace that earlier construction by a dimension count.

Over a field, if W=U+ku with u not in U, `oneNewRelationEquiv` constructs

    k ~= ker(B/U -> B/W), a |-> [a u]_U.

Injectivity follows because a[u]=0 and [u] !=0 force a=0. For surjectivity, a kernel representative y belongs to W, so y=l+a u with l in U. The source quotient then gives [y]=[a u]. Both inverse laws are packaged by `LinearEquiv.ofBijective`.

For D with D(U)<=W, the induced derivative is explicitly B/U->B/W. It is not falsely typed as an endomorphism of B/U. If a defect is old-a u with old in U, its source class is -a[u]; its image at the next level vanishes. When u is not in U, the class is nonzero exactly when a is nonzero.

The integration module also constructs `quotientTransportLift` on the original four-mask reconstruction. It uses this very quotient transport as its coefficient map and synchronization as its support map. `quotientTransport_fibre_zero` and `quotientTransport_not_absent` prove the specified higher-label zero result on those total objects.

### Orthogonal realization of the same layer

Let H be an arbitrary complex inner-product space, U<=W submodules, and suppose U has an orthogonal projection P_U. The implementation constructs

    W/(U as a submodule of W) ~= W intersect U^perp,
    [z] |-> z-P_U z.

No finite-dimensional hypothesis on H is imposed. Finite-dimensional U, as in the source, supplies the projection instance.

The map is well-defined since it kills U. Its value lies in W because P_U z lies in U<=W, and in U^perp by the projection property. If two residuals agree, the difference of their representatives lies in U, which proves injectivity. For w in W intersect U^perp, P_U w=0, so [w] supplies a preimage. `orthogonalLayerEquiv` packages the full linear equivalence and `orthogonalLayerEquiv_apply` gives its actual formula.

The source specialization is U=L_n=Theta V_n and W=L_(n+1), with u=u_(n+1). These are algebraic relation quotients. Neither quotient is replaced by the closure of the full theta image in L2.

## 3. The selected representative is still the orthogonal residual

The new note chooses R_n=(1-P_n)s_Z for the admitted finite relation space L_n. It is a specific sequence, not an unconstrained choice of a positive metric.

For vectors R_i and corrections C_i in U, the code proves the exact matrix identity

    Gram(R+C)=Gram((1-P_U)R)+Gram(P_U R+C).

It follows by expanding the pairings and using orthogonality for both cross terms. The second Gram is proved positive semidefinite, so the residual Gram is the minimum in the admitted family in the Loewner sense. Adding an already admitted relation before projection does not change the residual.

This is an operator-projection formulation of the same Schur-complement calculation. The code does not claim a minimum of the normalized weight defect.

Positive definiteness uses the original test space B. Given an injective observation B->H and a jet map B->C^I taking the representative columns to the standard coordinate basis, the observed Gram is proved positive definite. Jets are not assumed to extend continuously, or even to be supplied, on all of H. Applying the jets to a vanishing source linear combination proves independence, then Mathlib's Gram theorem gives positive definiteness.

Declarations: `gram_minimum_decomposition`, `gram_minimum_posSemidef`, `residual_relation_invariant`, and `gram_posDef_of_source_jets`.

## 4. The one new relation gives the actual rank-two pairing

Let R_i be the retained representative columns and write the full derivative boundary as

    B_i=old_i-r_i u,

where <R_i,old_j>=0 for all i,j. Retain the unscaled vector u and real h, with

    <u,R_i>=h s_i.

Then the actual boundary contraction is

    -(R*B+B*R)=h(s* r+r* s).

Proof, entry by entry:

    -(<R_i,B_j>+<B_i,R_j>)
      = <R_i,u> r_j + conjugate(r_i)<u,R_j>
      = h(conjugate(s_i)r_j+conjugate(r_i)s_j).

This is `one_new_relation_control`. The old boundary vectors remain in the input; only their pairings vanish.

The matrix is factored through two coordinates by

    x |-> (r x,s x),
    (a,b) |-> h(s* a+r* b).

`rank_le_two` proves its rank bound in arbitrary finite packet dimension; `hermitian` proves its adjoint symmetry.

### Link to the derivative operator

The code takes the source Green identity on the actual vectors:

    <sum_k A_ki R_k+B_i,R_j> +
    <R_i,sum_k A_kj R_k+B_j> = <R_i,R_j>.

It proves

    A*G+GA-G=-(R*B+B*R), G=Gram(R).

Combining this with the one-layer boundary gives the single declaration `weight_defect_one_layer`:

    A*G+GA-G=h(s* r+r* s).

The analytic task supplying this Green identity for D=-x d/dx is not hidden. The theorem is not obtained by assuming the desired matrix identity.

For the new attachment, use u=u_(n+1), h=mathfrak h_(n+1), r=r_n and s=r_(n+1). The source's extraction of the boundary as an old relation minus u r is the remaining Krylov/orthogonalization interface to instantiate.

## 5. The Gram update retains its norm and its relation

Assume additionally <u,u>=h. Define R'_i=R_i-s_i u. Expansion gives

    Gram(R)-Gram(R')=h s* s.

The code also proves <u,R'_i>=0 and that the Gram difference has rank at most one. There is no normalization u/||u|| and no omitted factor h. This is the supplied update from n to n+1.

Together with Section 2, this records both aspects of the step: the exact source relation killed by the quotient transport and its former contribution to the Hilbert Gram matrix.

## 6. The compressed scalar calculation

For any supplied matrix Ginv, the normalized control factors as

    Ginv W = (Ginv [h s*,h r*]) [r;s].

The code proves both directions of transfer of nonzero eigenvectors between the two compositions of arbitrary linear maps. It does not discard zero eigenvalues by asserting an invertible change of coordinates between spaces of different dimensions.

For the explicit two-by-two matrix

    K=[[c,a],[b,conjugate(c)]], a,b real,

the code proves

    det(K-tI)=0 <-> (t-Re c)^2=a b-(Im c)^2

for real t. Under |c|^2<=a b it proves the real-root formula and the exact maximal absolute root value

    max |h(Re c+sqrt(a b-(Im c)^2))|,
        |h(Re c-sqrt(a b-(Im c)^2))|
      =h(|Re c|+sqrt(a b-(Im c)^2)), h>=0.

The zero-real-part simplification is also proved.

Precise boundary: the implementation establishes the factorization, nonzero-eigenvector transfer, scalar characteristic equation, and maximum-of-roots identity. It does not yet package the whole generalized self-adjoint spectral theorem as a single Lean equivalence with the optimal Loewner allowance for the actual G, r and s. Positivity of G, the Cauchy inequality for the actual contractions, and the entry identification of the compressed composition must be connected in that final spectral wrapper. The written two-by-two argument in the source remains intact; its complete bundling is not being counted as done here.

## 7. The old homotopy theorem is applied to the actual packet projector

Given the original maps rep:E->B, jet:B->E, Theta:V->B, K:E->V and operators D,A with

    D rep=rep A+Theta K, jet D=A jet, jet Theta=0,

the new module constructs the projector rep jet and proves

    D(rep jet)-(rep jet)D=Theta(K jet),
    (K jet)Theta=0.

If jet rep=id, the projector is idempotent. `allPacketHomotopies` then uses the existing full equivalence with kappa=K jet. The support-changing construction from Section 1 applies to every resulting homotopy. Changing representatives by Theta b preserves the original jets.

This ties the classification to the supplied arithmetic commutator. It neither reruns the classification as a new discovery nor confuses Lambda Theta=id with the separate annihilation requirement kappa Theta=0.

## 8. Source qualifications retained

The full three-term recurrence's diagonal coefficient 1/2 uses the reality of the actual theta seed and its real Gram-Schmidt coefficients in addition to integration by parts. For a general complex seed, the latter fixes only the real part of that diagonal coefficient. The supplied real theta sequence has the extra property; this integration does not silently generalize it away.

The theta-series construction, Poisson/Mellin identities, all-degree three-term recurrence, density in L2, strong-Schwartz retraction, numerical moment values and truncation bounds remain analytic research inputs rather than new Lean certificates. In particular an integer-tail allowance is not a floating-point enclosure and does not certify Gram inversion.

No conclusion about RH, global purity, absence of nilpotent jets or vanishing of the global spectral-observation kernel is inferred from these modules. The conditional algebraic and inner-product conclusions remain useful without those additional results.

## 9. Reproduction

From `formal/splitzero` on this contribution's branch, use Lean 4.31.0 and the unchanged Mathlib revision `fabf563a7c95a166b8d7b6efca11c8b4dc9d911f`.

    python3 prepare.py
    lake update
    lake exe cache get
    lake -KmaxJobs=2 build
    python3 check_tau_recovery.py --prepare
    python3 check_boundary.py
    python3 check_boundary_integration.py --prepare

Then compile the tau modules listed in `TAU_RECOVERY_MODULES.txt`, the preserved five modules in `BOUNDARY_MODULES.txt`, and the six additions in `BOUNDARY_INTEGRATION_MODULES.txt`, in that order, with:

    lake env lean --trust=0 -DwarningAsError=true \
      -o .lake/build/lib/lean/NAME.olean NAME.lean

Finally:

    lake env lean --trust=0 -DwarningAsError=true AuditBoundaryIntegration.lean \
      > AuditBoundaryIntegration.log
    python3 check_boundary_integration.py AuditBoundaryIntegration.log
    lake env lean --trust=0 -DwarningAsError=true AuditBoundary.lean > AuditBoundary.log
    python3 check_boundary.py AuditBoundary.log

The dedicated workflow checks all 68 integration targets and all 38 preserved boundary targets, and reruns the 87-target tau, 73-target derived, and 28-target structural audits and the checking-harness tests normally and with Python optimization. The seven integration Python methods combine exact finite regression models and negative audit controls, including independence from the preserved manifest. They are not arithmetic quadrature tests and do not replace Lean.

No pre-existing scalar source, formal module, dependency pin, old workflow, reader corpus or another session's branch is changed.
