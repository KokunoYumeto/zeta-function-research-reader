# Tau-base recovery, complete homotopy classification, and global retractions

Owner-directed continuation, 12 September 2026. This note distinguishes recovered formal sources, new formalization of source-derived consequences, and analytic inputs still requiring their own formal implementation. The successful workflow on an exact commit is the build record; until that run completes this note makes no certificate claim.

**Build status added on 12 September 2026.** The preceding sentence records the pre-run state. The later [successful run 34686934725, job 103535438942](https://github.com/KokunoYumeto/zeta-function-research-reader/actions/runs/34686934725/job/103535438942) used exact source head `5d2772ea0a16d177ac3e01ff70394b90ba95a232`. Its seven module hashes and 87 selected axiom reports were independently checked during integration. This is the certificate for those declarations, not for the separate analytic theta construction or an arithmetic weight estimate. The mathematical sources below are unchanged.

## 1. Provenance and unchanged data

The base is the accepted SplitZero package on `main` at `14c69d604044b848d64318751a7bee19edfd9aba`. The original scalar core, earlier theorem modules, dependency pin and old workflows are unchanged. Four tau sources are recovered from the interrupted branch at `621eb8863d6e0421b1ce3a604e5712c14d7b5cc2`, with proof-script repairs where fresh Lean runs exposed incomplete elaboration. Those repairs do not change the mathematical statements.

The new homotopy result develops the two-leg comparison of chain-descent PR #9 (`8f99b94d306c3b1aaa817d52c57fa6fd298d511c`, `workbenches/tau-chain-descent/RESEARCH_NOTE.md`). The retraction and topology files formalize consequences of the specified maps in global-retraction PR #10 (`d26c283c2a58da57bb5a5a4d4bc8669019f6ebb7`). They do not count those written analytic arguments as already checked Lean proofs. The source programme and its construction remain attributed to the owner; ordinary quotient algebra and Mathlib reuse are not new discoveries.

The retained scalar is G(R) with structural zero tau, supported zero e, and the original amplitude map to R. The base F1_tau is the pointed multiplicative monoid {tau,1}, not the Boolean semiring. Its structural maps, unique multiplicative prime, finite-word relations, and commuting arithmetic map are implemented in `SplitZeroTauBase.lean`. This is a specified minimal pointed/preaddition interface, not a completed general blueprint-scheme library.

## 2. The recovered finite chart and dual maps

The chart is the four-point ordered topological space + < eta < sigma and - < eta < sigma. A diagram F retains all four modules and its three generating restriction maps. Its displayed differential is

    d_F(x,y)=r_+(x)-r_-(y).

The code proves that compatible sections are exactly its kernel, and that their eta/sigma values extend uniquely. The two degree windows and the induced chain map are constructed from those actual restrictions.

Opposite-index dual transport is precomposition. The bottom fibre of the opposite diagram is not assumed zero. The code constructs quotient-dual/annihilator equivalences, evaluation and its naturality, the double-dual comparison, and the twisted operator action a times precomposition by U inverse. Evaluation obeys the full twist.

For coefficient W, the two cofree chart terms have exact linear Hom equivalences

    Hom(F,I_eta W) ~= Hom(F_eta,W),
    Hom(F,I_+ W + I_- W) ~= Hom(F_+,W) x Hom(F_-,W).

Their differential corresponds to ell |-> (ell r_+, -ell r_-). The signs are proved in both Hom-comparison squares. Over a field these cofree terms have the proved lifting property across pointwise injective maps. In particular the dual of the actual degree-one quotient is identified with the kernel of this signed dual differential.

The implementation establishes these objects, equations and lifting properties. It does not bundle the entire derived-category adjunction, the projective resolution of the constant sheaf, or a Verdier six-functor formalism.

## 3. Every homotopy of the two-leg comparison

Let R be any commutative ring, Theta:V->B an injective R-linear map, and F:V~=V an R-linear automorphism. In degrees 0,1 put

    C=[V x V --d--> B],   d(v,w)=Theta(v-Fw),   Q=B/Theta(V).

Let kappa:B->V be linear and kappa Theta=0. The prescribed cochain difference is Delta=(0,Theta kappa). A homotopy is exactly a linear H:B->V x V satisfying BOTH

    d H=Theta kappa,     H d=0.

There is an explicit equivalence

    Hom_R(Q,V) ~= {such homotopies},
    alpha |-> H_alpha(b)=(kappa(b)+alpha(qb), F^(-1) alpha(qb)).

Proof: substitution gives d H_alpha=Theta kappa. Both kappa and alpha q vanish on Theta(V), so H_alpha d=0. Conversely write H=(u,v). Injectivity of Theta gives u-Fv=kappa. Since im d=im Theta, the second equation gives H Theta=0; therefore Fv descends uniquely through q to alpha. This gives the stated inverse. The Lean definition `cochainHomotopyEquiv` proves both inverse laws.

The solution set is affine, with difference module Hom_R(Q,V). It is not a linear space with zero as its natural origin when Delta is nonzero. Requiring only the first equation would instead yield parameters Hom_R(B,V); the second equation is essential.

The two source-note choices correspond to alpha=0 and alpha=-kappa_bar. Their difference is (kappa(b),F^(-1)kappa(b)), a cycle. It is nonzero whenever kappa(b) is nonzero. Since there is no degree -1 incoming differential, these cycles represent degree-zero cohomology. The ordinary kernel is canonically V through v |-> (v,F^(-1)v); the Lean acceptance tests prove the explicit nonzero cycle and classify all homotopies directly. The chart adapter identifies the differential with the existing four-point chart, rather than introducing an unrelated complex.

## 4. Construct the global quotient section, not merely a proposed map

Suppose Theta:V->B and Lambda:B->V are linear with Lambda Theta=id. Define

    K=id_B-Theta Lambda,    Q=B/range(Theta),    q:B->Q.

The code proves

    K^2=K, ker K=range Theta, range K=ker Lambda.

Indeed K Theta=0, Lambda K=0, and b=Theta Lambda b+Kb. These identities prove both image/kernel assertions and idempotence without finite-dimensional assumptions.

Since K kills the original range, the quotient universal property constructs

    s:Q->B, s(qb)=Kb.

Then qs=id, Lambda s=0 and the maps

    V x Q -> B, (v,u) |-> Theta v+s u,
    B -> V x Q, b |-> (Lambda b,qb)

are inverse R-linear maps. This is the actual `splitEquiv`. The quotient is the range quotient already used in the homology package, not a quotient postulated to be isomorphic to a selected finite model.

The `fromReconstruction` constructor retains the source's intermediate maps: i:V->W, P:W->V, T,N:W->W, Y:B->W, with P i=id, N(w-Tw)=w, and Y Theta=i-Ti. It constructs Lambda=P N Y and proves Lambda Theta=id. The analytic cutoff, Neumann inverse and moment calculations must supply those input identities at their analytic types. They are not silently provided as axioms.

## 5. Exact operator defect and changes of representatives

Let A_B and A_V intertwine Theta. The code constructs the actual induced operator A_Q on Q and

    k_A=Lambda A_B s : Q->V.

Decompose A_B s(u) through the preceding inverse maps to obtain

    A_B s=Theta k_A+s A_Q.

For composable endomorphisms A,C of the same data, substitution yields

    k_(AC)=A_V k_C+k_A C_Q.

Indeed expand C_B s, apply A_B, use its intertwining with Theta, and apply Lambda. This is a general composition theorem; for a group action it gives the displayed dilation cocycle without assuming its vanishing.

Every other linear section has a unique form s_b=s+Theta b with b:Q->V. The proof applies the decomposition to s'(u); the parameter is Lambda s'. Applying Lambda proves uniqueness. Its defect is exactly

    k_A^b=k_A+A_V b-b A_Q.

The code proves the changed block equation and

    A_B s_b=s_b A_Q  iff  k_A^b=0.

Thus equivariance is an equation to solve for an actual source-valued map. It is not obtained merely by choosing representatives. In particular a continuous splitting is not being relabelled an equivariant splitting.

For ANY finite representative map f:E->B, the identity

    s q f=f-Theta Lambda f

is proved at its actual map type. Applying it to the source's finite section explains the representative correction; proving the analytic Ext/residue interpretation remains separate.

## 6. Keep the actual quotient topology

Give V and B their specified topologies. If B is a Hausdorff topological additive group and Theta,Lambda are continuous, K is continuous. Since range Theta=K^(-1)({0}), the range is closed.

The quotient topology on Q makes q a quotient map. The equality s q=K therefore proves continuity of s. Both maps of the preceding linear equivalence are continuous, yielding the actual `splitHomeomorph`. The quotient is Hausdorff, and the induced A_Q and defect k_A are continuous whenever A_B is continuous.

This argument does not require a Banach norm. In a future analytic instantiation it can use the source's strong-Schwartz topology. It must not be read as a claim that the theta range is closed in an unrelated L2 completion. Nor does a closed range prove injectivity of a different spectral-observation map.

## 7. Carry the retraction through the existing supported objects

Let D,E be the original linear join diagrams and theta:D->E, lambda:E->D actual natural transformations satisfying lambda_i theta_i=id. Define residual_i=id-theta_i lambda_i. Naturality is proved using the original transport equations, so these are actual G(R)-linear maps on reconstructed total semimodules.

The checked identities are

    lambda_total theta_total=id,
    residual_total^2=residual_total,
    residual_total(theta_total x)=e . theta_total x.

The final right side is the supported zero in the SAME fibre. It is not global absence. The theorem is stated against the existing `Hom.total` and original scalar e, not against a newly invented scalar implementation. No injectivity of arbitrary support transports is assumed.

These are fixed-index natural maps. The complete support-changing synchronization homotopy, the general category equivalence with changing index, and the geometric sheaf realization are not claimed by these three identities.

## 8. Exact formal/analytic boundary

The formal package contains seven sources: four recovered tau modules and three additions for homotopies, retractions and topology. Their target manifest enumerates the principal constructions and proof terms for transitive axiom checking. Declaration counts include definitions and infrastructure and are not discovery counts.

Analytic obligations not formalized here include: Mobius/Fourier exterior reconstruction on the original test spaces; compactness and the strict cutoff-operator norm inequality; the actual Neumann inverse in the stated Frechet/Schwartz construction; its analytic seminorm bounds; global spectral synthesis and the other observation kernels; the arithmetic residue/Ext identification; and the common-scale weight estimate. The new Deligne-control archive was not readable through the available file reader, and the local execution sandbox did not open it. No claim to have audited that archive is made.

The source's global-retraction note was read through the supplied rendered text and its published PR record. It supplies the motivation and specified analytic input, not an additional trusted theorem of Lean. The precise output of this continuation is the conditional algebraic/topological theorem package and the recovered finite-chart maps. No positivity, purity, RH or GRH conclusion is assumed in a formal definition.

## 9. Reproduction

In `formal/splitzero` with the existing pinned Lean 4.31.0 environment:

```sh
python3 prepare.py
python3 check_tau_recovery.py --prepare
python3 -m unittest -v test_tau_recovery.py test_derived_checker.py
python3 -O -m unittest -v test_tau_recovery.py test_derived_checker.py
lake update
test "$(git -C .lake/packages/mathlib rev-parse HEAD)" = fabf563a7c95a166b8d7b6efca11c8b4dc9d911f
lake exe cache get
lake -KmaxJobs=2 build
while IFS= read -r name; do
  lake env lean --trust=0 -DwarningAsError=true -o ".lake/build/lib/lean/$name.olean" "$name.lean" || exit 1
done < TAU_RECOVERY_MODULES.txt
lake env lean --trust=0 -DwarningAsError=true AuditTauRecovery.lean >AuditTauRecovery.log
python3 check_tau_recovery.py AuditTauRecovery.log
```

The workflow also reruns the older 73-target derived and 28-target structural audits. Shared parser tests exercise missing, duplicate, unexpected and forbidden axiom reports; new tests cover source/module agreement and proof-escape rejection. Tests are not proof certificates; Lean execution is the mathematical validation. The source manifest prints SHA-256 hashes so the accepted source can be identified exactly. Development failures remain in branch history.

## References and reuse

Owner-directed SplitZero programme. (2026). *Chain-level arithmetic descent over the tau base* (Zeta PR #9, exact revision above).

Owner-directed SplitZero programme. (2026). *Global theta retraction* (Zeta PR #10, exact revision above).

Mathlib contributors. (2026). *Mathlib4* (revision `fabf563a7c95a166b8d7b6efca11c8b4dc9d911f`). Quotient linear maps, product linear equivalences, topological quotient modules, and ordinary Lean tactics are reused under the existing dependency license.
