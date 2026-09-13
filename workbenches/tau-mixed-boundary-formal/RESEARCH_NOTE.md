# Mixed-boundary recovery on the original SplitZero quotient

14 September 2026. This continuation preserves main `8e28e155bcffe605af8fa6cce313e05cd692341a` and recovers the entire unfinished mixed-support contribution at `fb60c6694093ee41648cf31d4be75bb69c145770`, with its ancestry. The actual observed Lean checkpoint is recorded separately in STATUS.md; a proof written here is not thereby a kernel certificate.

## 1. Sources and scope

The new source is the delivered Mixed Boundary Continuation, its accompanying 767-line markdown, and the Marked Product Four Endpoint package. The current main includes the accepted MCF, SP, BC and other mixed-control source modules. The local delivery copies of MCF.tex, SP.tex and BC.tex have exactly Git blobs `a8b1300ea8b842ab1340d67e44cd6da2f71e8e62`, `f249baf3a8eb6691aad153076a34ed5ec7c20631` and `19dc709bd219ebe5f267a386561a5e6b5f581c15`, respectively. Selected MCF34--MCF41 outer/inner-face comparisons and the complete SP1--SP13 were read, in addition to the actual recovered Lean sources. This is not a claim to have independently audited every analytic source in the cumulative reader.

The two archives were safely extracted and all manifest entries verified. Nevertheless NEW_BODY.tex and CONTINUATION.tex jump from MB19 to MB45 and omit the intervening proof text. COMPLETE_CONTINUATION.tex includes NEW_BODY.tex and therefore does not independently restore it. FAILURE_REVIEW.md and INTAKE.json preserve this distinction. The following lattice proof is an independent reconstruction from the explicit delivered formulas, not a claim to reproduce missing prose verbatim. The sealed attachments are unchanged.

The original scalar stays G(R)={tau} disjoint-union R^bullet, with e=0^bullet. The base is the original pointed tau-base with the arithmetic maps p_R attached. Coefficient specialization v->0 sends a supported v to e, not tau. No Boolean localization replaces the full arithmetic source, and the original theta boundary family is not equated with a finite observation kernel.

## 2. One exact kernel theorem supplies the boundary comparison

Let R be a commutative ring, M an R-module, v in R, and f:M->M an injective R-linear map. Assume multiplication by v is injective on M. Set

    T = M / v f(M),       S = M / vM.

There is a canonical linear isomorphism

    c_f : S -> ker(v:T->T),       [x] -> [f(x)].              (BR1)

This is a v-annihilator, called the v-socle here. It is not implicitly the socle for every maximal ideal of a parameter ring.

Proof. If x changes by vy, f(x) changes by vf(y), so the class is well-defined. Multiplication by v sends [f(x)] to zero in T. If [f(x)]=[f(y)], then f(x-y)=vf(z)=f(vz) for some z. Injectivity of f gives x-y=vz, proving injectivity. Conversely, if v[z]=0, then vz=vf(x) for some x. Cancellation of v on the prequotient M gives z=f(x), proving surjectivity. All inverse laws are thereby established. No cancellation is asserted on T itself, which is precisely where the torsion is retained.

Lean constructs BR1 using the actual Submodule quotients, with `comparison`, `comparison_injective`, `toSocle_surjective` and `socleEquiv`. It also constructs the diagonal instance `diagonalSocleEquiv`: over a domain with v nonzero, f(x)_i=v^(n_i)x_i for arbitrary n_i>=0. The target is therefore the actual quotient by the positive-exponent diagonal v^(n_i+1), not an independently supplied copy of its kernel.

For linear A,B with Bf=fA, A preserves vM and B preserves vf(M). The implementation constructs both quotient actions and proves

    B_bar c_f = c_f A_bar.                                  (BR2)

If the supplied lattice equation is B(vf)=(vf)A, cancellation by v proves the needed Bf=fA first. This is `divide_intertwiner`, followed by `action_square`.

There is also a fully typed homological interpretation. When M is free, [M --vf--> M] is a free resolution of T in degrees -1,0. After tensoring with R/(v), its differential is zero. The connecting map from its degree -1 cohomology to ker(v:T->T) is exactly [x]->[f(x)]. This follows by lifting x, writing vf(x)=v f(x), and taking [f(x)] in T. Thus BR1 identifies the actual Tor1 term. The code proves this explicit kernel model and its maps; it does not bundle a general derived-category Tor functor in this contribution.

## 3. Apply it to the retained ramified primary lattice

Keep the delivered primary polynomial h_rho(s)=(s-rho)^m, m>=1, and the original additive constant kappa=-(-rho)^(m+1)/(m+1). On the specified chart

    u=v^(m+1),  t=a v^m,  s=rho+vx,

its phase is literally

    kappa/v^(m+1) - rho a/v + x^(m+1)/(m+1) - ax.

The Jacobian ds=v dx is present. It gives the lattice diagonal

    D_v=diag(v,v^2,...,v^m),       f=D_v/v=diag(1,v,...,v^(m-1)).

Let A0=C[a] and O=A0[[v]]. The exact sequence is

    0 -> O^m --D_v--> O^m -> T_rho -> 0,
    T_rho = direct_sum_(0<=b<m) O/(v^(b+1)) epsilon_b.        (BR3)

BR1 gives the precise coefficient family

    A0 tensor_C E_rho -> ker(v:T_rho->T_rho),
    z^b -> v^b epsilon_b,   E_rho=C[z]/(z^m).                (BR4)

A necessary typing qualification: with a still variable, the right-hand side has rank m over C[a], not dimension m over C. Specializing a=a0 gives the displayed m-dimensional complex arithmetic block. The same qualification applies to lengths: the sum m(m+1)/2 is the A0-rank of this finite A0-module, equivalently its v-adic graded length over A0. It is not finite composition length over all of O with an unspecialized affine parameter.

Let N z^b=z^(b+1), with N z^(m-1)=0, and R z^(m-1)=1, with R z^b=0 for b<m-1. The source action and receiving action are

    A(v)=rho I+N+a v^m R,
    L(v)=rho I+v(N+aR).

Direct evaluation on every basis vector gives L D_v=D_v A(v). The same equation divided by v gives L f=f A(v). Therefore BR2 proves that the action on BR4 is rho I+N, including every nonzero arrow. On the ordinary quotient T_rho/vT_rho, the receiving action is rho I. These are two different cohomology groups of the same specialized resolution, with different induced operators. No arithmetic Jordan block is discarded to make them agree.

For example, at m=2 the target module is O/(v) epsilon_0 plus O/(v^2) epsilon_1. Its v-kernel basis is epsilon_0, v epsilon_1. L sends epsilon_0 to rho epsilon_0+v epsilon_1 and v epsilon_1 to rho v epsilon_1. Its ordinary quotient has basis [epsilon_0],[epsilon_1], and L acts by rho on both. The derived-kernel arrow, not the ordinary quotient alone, retains the Jordan step.

The scalar exponential line kappa/v^(m+1)-rho a/v and the regular factor in a remain distinct from this arithmetic action. In particular the formal spectral nilpotent N has not been relabelled the logarithm of geometric inertia. Character-twisted horizontality in the supplied note retains its own target line, and finite-field wild/tame invariants require the supplied separate calculation.

## 4. All ordered tensor directions, with their actual exponents

For k>=1 equal-primary factors the single tensor lattice map has diagonal

    D_(k,b)=v^(k+|b|),    b=(b1,...,bk), 0<=bi<m.

Its cokernel is

    T_(rho,k)=direct_sum_b O/(v^(k+|b|)) epsilon_b.

Apply BR1 with n_b=k+|b|-1, which is nonnegative. The resulting isomorphism is

    A0 tensor_C E_rho^(tensor k) -> ker(v:T_(rho,k)->T_(rho,k)),
    z^b -> v^(k+|b|-1) epsilon_b.                            (BR5)

The rank is m^k over A0. The action is k rho I+sum_i N_i: the same diagonal calculation conjugates the sum action before specialization, and BR2 specializes the full source operator. For b_i<m-1 its image exponent increases by one in the receiving component. A wrapped term carries the exact v^m coefficient and vanishes in that receiving quotient, not by an external absence convention.

Summing the exponents gives the complete finite A0-rank of T_(rho,k):

    sum_b(k+|b|)=k(m+1)m^k/2.

At m=2,k=2 the socle has four coordinates, whereas the sum-generated cyclic subspace has dimension three: 1, z1+z2, 2z1z2. The additional vector z1-z2 remains in the full tensor block. The coefficient two and the extra vector are retained in the independent regressions. No sum-coordinate compression is declared an equivalence with the full ordered tensor space.

For unequal multiplicities one may use a common ramification r divisible by every mi+1. The positive exponent is sum_i r(bi+1)/(mi+1); BR1 applies to those exact integer exponents as well. The corresponding action and source map still require their supplied lattice intertwining, not just agreement of dimensions.

The cone of the single tensor lattice map is not automatically the tensor product of the individual two-term cokernel resolutions. They have different complexes and generally different homology. BR5 concerns the former, exactly as its diagonal is specified. A complete cubical derived comparison requires its additional face maps and signs; those are not silently certified by the generic diagonal theorem.

## 5. The new maps are inside the original mixed-support reconstruction

Let D be the original LinearDiagram over the support semilattice L and let f be a natural endomorphism. Define original relation diagrams fibrewise by

    B_source(i)=v D_i,       B_target(i)=v f_i(D_i).

Their stability follows from linearity of the existing transports and f's actual naturality equation. `comparisonHom` descends f through these two existing `Relations.quotientDiagram`s. Its square is an equality of the original G(R)-linear total maps:

    comparisonHom.total o q_source = q_target o f.total.     (BR6)

If each f_i is injective, the total map is injective. No injectivity of the coefficient transport D(i<=j) is imposed. Its exact total image is

    { y : v^bullet * y = e * y }.                           (BR7)

The right side compares v-action with the zero OF THE SAME SUPPORT FIBRE. It does not compare v*y with global tau. This is proved by quotient induction and the constructed surjection in BR1, not by calling an amplitude kernel a support kernel.

The MCF source has independent outer source/leg data and inner coefficient faces. The new `present_empty_face` theorem records a corresponding necessary distinction: in any original diagram indexed by L times Finset J, ((i,empty),0) is not global absence when i is nonbottom. A coefficient face can have zero vector space while its outer source/leg label remains present. This does not contradict `sum_support` for an actually empty finite sum, which has the true global bottom label. The two operations must not be conflated.

The recovered `SplitZeroMixedSupportMetric` is complementary. A finite sum has support the JOIN of all its original input supports, including supported coefficients that happen to be zero. The original quotient sends a family of original relations to the zero of that join. `gathered_zero_iff` tests membership of the transported SUM in the receiving relation submodule; membership of each summand separately is sufficient but not necessary. Thus cancellation between transported terms is permitted without erasing their source labels.

For columns F_a transported into a stated common fibre and its original form M, the recovered theorem proves

    gram_M(sum_a F_a)=sum_a sum_b F_a^* M F_b.                (BR8)

Every off-diagonal mixed term is present. Different support labels do not prove orthogonality after the receiving transports. Canonical section changes have their actual original-boundary witnesses, so their mixed total quotient maps agree, while their prequotient pairings remain available.

## 6. Metric work recovered rather than restarted

Seven recovered modules retain their ancestry: MetricResolvent, MetricResolventSupport, CertifiedTraceBounds, MetricSandwich, SourceProjectorContrast, MixedSupportMetric and CanonicalSourceContrast. The recovery repairs proof elaboration; it does not replace their mathematical targets.

MetricSandwich proves the scaled canonical secants with the actual old-boundary difference Delta=R1-R0:

    G1-aG0=R1^*(M1-aM0)R1+a Delta^*M0 Delta,
    bG0-G1=R0^*(bM0-M1)R0+Delta^*M1 Delta.

It composes the PSD comparison with equality in the original supported quotient. SourceProjectorContrast and CanonicalSourceContrast prove the four-endpoint trace cancellation and pairing on the actual canonical residuals, not arbitrary independently chosen matrices. The mixed-square formula retains its cross term. Source-path differentiation and the final Hilbert--Schmidt estimates remain written analytic consequences unless separately checked by their actual declarations.

The accepted SP module supplies the stronger integrated condition-number estimate (2q-1) log(rmax/rmin) for its specific common polynomial source/relation geometry; the earlier general four-endpoint sandwich only gives 2q log(rmax/rmin). The former uses the overlap of two rank-(q+1) spaces inside dimension 2q+1. This current source refinement is preserved and attributed. It is not contradicted by the more general finite source-sandwich lemma and is not claimed as newly Lean-proved here.

## 7. What the result does and does not settle

This completes a concrete kernel-and-action mechanism for retaining the arithmetic nilpotent at the mixed boundary, together with the support diagram in which it lives. It also recovers the failed finite metric source work and all its mixed source pairings. The three recorded historical jobs reached Lean after successful syncing; their failures do not constitute counterexamples to the mathematics.

The exact boundary coefficient maps, their equivalence, their induced action squares and natural total maps are the new formal targets. The full irregular/finite-field comparison, analytic period asymptotics, Stokes data and a uniform arithmetic endpoint upper estimate are not inferred from those targets. Nothing here is an RH proof or an impossibility theorem. The continuing quantitative argument must use the original theta source, its complete marked packet and its actual prequotient norms.
