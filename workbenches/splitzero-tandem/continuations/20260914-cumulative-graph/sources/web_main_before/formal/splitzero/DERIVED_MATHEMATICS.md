# SplitZero: reconstruction, internal homology, and balanced finite jets

Owner-directed formalization continuation, 12 September 2026.

## Scope and provenance

This contribution extends `formal/splitzero` on the owner's Zeta workbench. Its base is the synchronization PR #5, commit `236f0a8370477991e2d0cf334ad1ebfe4f3f8b17`, itself based on the structural PR #4. The original scalar core and all five preceding extension sources remain unchanged. There is no Sneed-side submission or integration in this continuation.

The mathematical source is the owner's SplitZero programme, including the supplied continuation's internal homology and balanced-Mellin sections. The implementation below distinguishes source-derived structure, ordinary reusable algebra, and the new explicit comparison example. It makes no global priority claim and does not treat the number of Lean declarations as a number of mathematical discoveries. No private conversation or source-literature corpus is republished.

The exact build certificate for a revision is the completed `SplitZero derived constructions` workflow on that commit, including direct source checks and its generated `AuditDerived.lean`. The PR records the accepted execution revision and run. A failed earlier development run is not a certificate for later source.

## 1. Reverse reconstruction, with actual scalar action

Let R be a commutative ring, L a join-semilattice with bottom, and let D consist of R-modules V_i with linear transition maps

    rho_ij : V_i -> V_j  (i <= j),
    rho_ii = id,  rho_jk rho_ij = rho_ik.

No finiteness, field, injectivity, or nontriviality assumption is imposed. Construct

    Total(D) = disjoint union of V_i over i in L.

The global zero is (bottom,0), and

    (i,x) + (j,y) = (i join j, rho_i,i-join-j(x) + rho_j,i-join-j(y)).
    tau . (i,x) = (bottom,0).
    ofR(r) . (i,x) = (i,r x).

`LinearDiagram.totalAddCommMonoid` and `LinearDiagram.totalModule` construct the actual instances and prove every law. For associativity, transport both sides to i join j join k. Linearity and transition composition reduce both to the same three-term sum. The scalar laws follow in the supported case from the R-module laws and in the absent cases from the chosen global zero. The supported-zero scalar sends (i,x) to (i,0).

The bottom fibre is allowed to be nonzero. Specializing it to the zero module recovers the source's carrier consisting of one absent point and the non-bottom fibres. This is an explicit generalization, not an assumption that the bottom fibre in every later dual diagram vanishes. Opposite-index duality itself is not constructed here.

Fixed-index natural families of linear maps produce actual `G(R)`-linear maps between reconstructed totals. Identity and composition are proved. More substantially, `Recovery.recoverEquiv` reconstructs the intrinsic support fibres of **any** existing `G(R)`-semimodule M and gives a full `G(R)`-linear equivalence back to M:

    (l,x) |-> x,        m |-> (e m,m).

Its addition proof uses the original absorption identity m + e m = m. It is not merely a bijection of carriers. A bundled equivalence of the two full categories, including arbitrary changes of support index and both natural inverse comparisons, is a separate library interface not claimed by this implementation.

## 2. The internal quotient is characterized by a universal property

Let B_i be transition-stable submodules of V_i. The quotient diagram has fibres V_i/B_i and the genuinely induced quotient transition maps. The projection

    q : Total(D) -> Total(D/B),  q(i,x) = (i,[x])

is a surjective `G(R)`-linear map. The code proves the exact equality criterion

    q(i,x)=q(i,y)  iff  x-y is in B_i.

Different labels cannot become equal under q. In particular a relation maps to its own fibre zero.

The main point is stronger than that observation. Let N be **any** `G(R)`-semimodule, not assumed additively cancellative, and let f:Total(D)->N be split-linear. If

    f(i,b)=f(i,0)  for every b in B_i,

then there exists a unique split-linear g:Total(D/B)->N with g q=f. The proof does not subtract elements in N. If x-y is in B_i, use the identity y+(x-y)=x inside V_i and then apply additivity of f. This proves constancy on q-fibres. Surjectivity constructs the descended function; linearity and uniqueness follow by lifting representatives.

`Relations.coequalizer_universal` states this against the actual inclusion of the relation diagram and its supported-zero companion. Thus the universal property is proved against arbitrary semimodule targets, not only against a selected class of fixed-support maps. The implementation gives the complete unbundled universal property; it does not merely define the desired quotient and label it a coequalizer.

## 3. Actual homology and the exact transported-class kernel

At a degree i of a cochain complex, use the window

    C^(i-1) --dPrev--> C^i --dNext--> C^(i+1),  dNext dPrev=0.

`Window.boundaryToCycles` constructs the incoming map into ker(dNext). Boundaries are its actual linear range, and H is the module quotient of cycles by that range. `Window.ofCochain` imports these data at every integer degree of a Mathlib `CochainComplex`; `ChainMap.ofCochain` imports an actual cochain map without replacing its differentials.

For a chain map f:C->D, the code constructs

    f_Z : Z(C) -> Z(D),
    H(f) : Z(C)/B(C) -> Z(D)/B(D).

It proves identity, composition, and

    H(f)([z])=0  iff  there exists y with dPrev_D(y)=f_i(z).

Define the module of killed representatives and its original relation submodule:

    Krep = {z in Z(C) : f_Z(z) is in B(D)},
    Bold = B(C), viewed as a submodule of Krep.

There is a constructed linear equivalence

    Krep/Bold  ~=  ker H(f).

Forward map: the class of z goes to the kernel element [z]. It is well-defined because Bold consists exactly of original source boundaries. It is injective because equality of source classes is exactly a difference in Bold. It is surjective because every kernel class has a cycle representative whose image is a boundary. This is `ChainMap.homologyKernelEquiv`, obtained from a general quotient-kernel equivalence proved in the same file.

The calculation retains actions as well. Given chain endomorphisms a of C and b of D satisfying f a=b f, `homology_intertwines` proves H(f) H(a)=H(b) H(f). `kernelAction` constructs the restriction of H(a) to ker H(f). Thus passing to the comparison kernel does not discard a compatible operator or require asserting that the kernel is zero.

## 4. Internal homology on the complete support diagram

For coherent support-indexed chain windows, the code constructs the diagrams of preceding terms, middle terms, following terms, cycles, boundaries, and homology. Let R_L denote the reverse reconstruction.

The differential identity is typed as

    R_L(dNext) R_L(dPrev) = z_L : R_L(C^(i-1)) -> R_L(C^(i+1)),
    z_L(l,x)=(l,0).

The source and target degrees are explicit. A theorem shows that z_L differs from the constant global-zero map whenever L has a non-bottom element. Cycles satisfy the actual equalizer equation d(x)=e.d(x).

The internal homology projection

    q : R_L(Z(C)) -> R_L(H(C))

is the coequalizer of the **original incoming differential into cycles** and its supported-zero companion. `homology_coequalizes` and `homology_coequalizer` establish both parts of that universal property against every split-linear target. This is not an assumed homology compatibility of reconstruction.

For every transition i<=j,

    rho^H_ij([z])=0  iff  rho_ij(z) is a boundary at j.

If z is not a boundary at i, its retained class (i,[z]) is not (i,0), regardless of whether that transition kills it. The quotient-kernel equivalence of section 3 computes all such classes as a module, not just a yes/no predicate.

## 5. A concrete comparison that detects more than the support labels

Fix any nontrivial commutative ring k. In the displayed degree let

    C: k --0--> k --0--> k,
    D: k --a |-> (a,0)--> k^2 --0--> k.

Use zero maps in the outside degrees. The two middle chain maps are

    f(a)=(a,0),            g(a)=(0,a).

The code proves that the source class [1] is nonzero. Its f-image is the **nonzero vector** (1,0), but that vector is a boundary in D, so H(f)([1])=0. In fact H(f)=0 on every source class. The g-image (0,1) cannot be a boundary, because every boundary has second coordinate zero. Hence H(g)([1]) is nonzero and H(f) is not H(g).

The ordinary calculation gives H(C)=k and H(D)=k (the latter through second-coordinate projection). These identifications explain the example; the Lean acceptance tests directly prove the nonzero source class, the nonzero chain image, the zero induced map, the surviving class, and the distinction of induced maps rather than relying on a dimension computation.

Consequently the source and target complexes, individual fibre homology, and terminal homology can be identical while the transition kernel differs. This example is parametric over all nontrivial commutative rings, not a finite numerical experiment. Together with the general assembly theorem it supplies an explicit test of the information retained by support-indexed homology. It is an algebraic test case, not a claimed model of the global theta comparison.

## 6. Balanced finite jets, including the original split quotient square

Let k and B be commutative rings and fix a k[t]-algebra structure on B. Let u:k[t]->B denote that map and

    I_(rho,m)=((t-rho)^m),    m>=0.

There is an explicit B-algebra equivalence

    B tensor_(k[t]) (k[t]/I_(rho,m)) ~= B/((u(t)-u(rho))^m).

It maps b tensor [p] to [u(p)b], with inverse [b] to b tensor 1. No flatness assumption is used for this quotient base-change theorem. This is a specialization of the existing Mathlib theorem `Algebra.TensorProduct.quotIdealMapEquivTensorQuot`, not a claim to have independently developed general tensor-product quotient theory.

`splitBaseChange` lifts this equivalence to the original G-construction on both sides and proves the commutative square with reflect. It preserves tau and e separately and is a genuine semiring equivalence, not just an amplitude comparison. Thus every element of the finite-jet quotient has an inverse image before forgetting split support.

For any k[t]-module V and v in V, the exact balancing calculation is

    (1-u(t)) tensor (t.v) - u(t) tensor (v-t.v) = 0.

Expanding gives 1 tensor (t.v)-u(t) tensor v, which vanishes by the tensor balancing relation. This is the algebraic equation of the source's Mellin repair. The choice u(t)=s and t.v=Dv is an application once those analytic module structures and intertwining maps have been constructed. It does not assert that the entire global balanced kernel vanishes, or that analytic scalar extension is flat without proof.

## 7. Where Deligne enters the intended RH route

None of sections 1-6 imports a Deligne purity theorem. They provide the algebraic maps with which a proposed realization can now be specified and its kernel retained.

For this programme, the subsequent dependency diagram should distinguish the following mathematical obligations:

1. Construct the actual operator-balanced theta complex at the relevant support labels, and its action-compatible analytic comparison beta to the spectral sheaf O/(2 xi). Identify its kernel or cone using the same maps; a finite-jet isomorphism is not a global injectivity argument.
2. Construct the geometric compact-support and ordinary complexes, their actual comparison c, their correspondence action, and a compatible realization identifying the required spectral sheaf with the image of H^1(c). Any additional kernel/cone contributions to the trace must be kept or proved to vanish.
3. Establish two-sided weight control on that **same image**. In Deligne's geometric setting the compact-support upper estimate and the duality-derived ordinary-cohomology lower estimate meet on the image. The dualizing operation, degree and Tate twists, tensor-power maps, and hypotheses of the estimates are part of this step, not consequences stipulated in the definition of support.
4. Transport the spectral normalization without changing the arithmetic function. For a dilation parameter a>1, an eigenvalue a^rho has modulus a^(Re rho). A proved weight-one modulus a^(1/2), for the representation identified with every relevant spectral zero, then forces Re rho=1/2. This last calculation does not supply the missing weight estimate; it states the precise final implication of this route.

These are dependencies of the specified route, not a claim that every possible proof of RH must follow it. The newly implemented kernel action is useful in steps 1-2 precisely because it keeps the part killed by a comparison available to the operator and trace calculation.

The supplied Connes-Consani article has an actual quotient-sheaf realization with a specified closure and scaling action. Its Theorem 1.2 realizes **critical zeros**. That theorem alone cannot be substituted for an identification representing all nontrivial zeros in the desired purity argument. This is a concrete source/target distinction for a future comparison map, not a dismissal of the construction.

## 8. Reading record and references

The six supplied S20 chunks were checked against their individual declared hashes and concatenated in order. The resulting archive has 216,580,466 bytes, 312 members, and SHA-256

    e2005bf31e1fcf362765f73c315c855e0f504f24f34d3a0ab188049da522b7c8.

The current top-level `readers/english_standalone.html` and `readers/source_language.html` were used for the selected readings, not the nested zero-accepted salvage corpus. The inspected windows include the tensor-square improvement in 3.2.13, the upper-bound statement in 3.3.1, and the duality/image argument in 3.3.4-3.3.6. This is not an independent audit of every page or of the entire historical proof. The Connes-Consani introduction and Theorem 1.2 were read in the supplied volume, printed pages 83-85 (physical PDF pages 94-96). No copyrighted source corpus is included in this contribution.

Deligne, P. (1980). La conjecture de Weil. II. *Publications Mathematiques de l'IHES, 52*, 137-252. https://doi.org/10.1007/BF02684780

Connes, A., & Consani, C. (2023). Hochschild homology, trace map and zeta-cycles. In A. Connes, C. Consani, B. I. Dundas, M. Khalkhali, & H. Moscovici (Eds.), *Cyclic cohomology at 40: Achievements and future prospects* (Proceedings of Symposia in Pure Mathematics, Vol. 105, pp. 83-102). American Mathematical Society.

Mathlib contributors. (2026). *Mathlib4*, revision `fabf563a7c95a166b8d7b6efca11c8b4dc9d911f`. In particular, `LinearAlgebra/Quotient/{Defs,Basic}.lean`, `RingTheory/TensorProduct/Quotient.lean`, `Algebra/Homology/HomologicalComplex.lean`, and `Algebra/Category/ModuleCat/Basic.lean`.

## 9. Reproduction

From `formal/splitzero` on this branch, with elan and Python installed:

```sh
python3 prepare.py
python3 check_derived.py --prepare
python3 -m unittest -v test_derived_checker.py
lake update
# Verify the resolved Mathlib revision before fetching its cache.
test "$(git -C .lake/packages/mathlib rev-parse HEAD)" = fabf563a7c95a166b8d7b6efca11c8b4dc9d911f
lake exe cache get
lake -KmaxJobs=1 build
for name in SplitZeroReconstruction SplitZeroRecovery SplitZeroHomology SplitZeroInternalQuotient SplitZeroComplex SplitZeroHomologyExample SplitZeroFiniteJets; do
  lake env lean --trust=0 -DwarningAsError=true "$name.lean"
done
lake env lean --trust=0 -DwarningAsError=true AuditDerived.lean > AuditDerived.log
python3 check_derived.py AuditDerived.log
```

The manifest enumerates the selected declarations, including the principal structures, universal properties, equivalences, and example proofs. Missing, duplicate, unexpected, or nonstandard axiom reports fail. Source checks reject unfinished proofs and native-reduction escapes. The Python tests validate this checking machinery; the mathematical certificate is the successful Lean execution. Build-job totals include dependencies and are not theorem counts.
