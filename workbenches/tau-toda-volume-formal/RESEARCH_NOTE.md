# Canonical quotient volumes, trace control and an endpoint-budget criterion

## Scope, provenance and coordination

This is an add-only formalization/collaboration continuation of the supplied *Tau Toda Volume Control* and *Tau Exterior Trace Amplification* notes. Their theta source, convolution measure, cyclic inclusion, full Taylor unit, supported quotient and canonical least-norm metric remain the inputs. The analytic constructions are not added as Lean axioms.

The branch is based on inspected PR #22 head `811210d24b80813a08972ca23f919db015383137`, itself including main `fa4be32f87a9a90f3c02a07f7790dea95a1e7b0f`. PR #21 is already included on that main. No competing scalar or quotient implementation is introduced, and no other-session branch is rewritten. Actual verification is determined by the completed strict Actions run, whose exact revision and logs are recorded in this PR; this note does not itself certify execution.

Both local execution services timed out before opening the uploaded ZIPs. The full pasted Toda and exterior notes were read. This is not an independent manifest audit or rerun of the uploaded 24/22-method suites. The six-part Deligne archive was not reassembled. The original author-hosted scan of Weil II was independently opened; printed pages 156,158,203 were visually inspected, including the context for section 1.3, Definition 1.3.5, and section 3.2.13. Some other requested page screenshots failed and are not counted as read. No historical transcription is silently promoted to a checked source.

## 1. The source and relation volumes are connected by actual maps

In fixed finite source coordinates let C be the column map of the original quotient representatives and B the column map of the original admitted relations. Put H=(B*B)^(-1). Define

    R=C-B H B*C.

Then B*R=0, and direct expansion proves

    R*R=C*C-C*B H B*C.

The actual source Gram in the ordered columns [C,B] is

    [[C*C,C*B],[B*C,B*B]].

The Schur determinant identity therefore proves

    det(sourceGram)=det(B*B) det(R*R).

This is implemented by `residual`, `residual_orthogonal`, `residual_gram`, `determinant_factor` and `determinant_ratio`. The last formula explicitly requires the nonzero denominator. It invokes the existing Mathlib Schur-complement theorem with the constructed residual Gram; it is not a novelty claim about determinants.

For every specified observation J with JB=0, the implementation proves JR=JC. Thus the canonical correction preserves the original finite arithmetic jets and quotient whenever their original relation-killing equations are supplied.

In the source's polynomial presentation the exact sequence is

    0 -> P_(N-q) --times chi--> P_N -> C[S]/chi -> 0.

The ordered basis 1,S,...,S^(q-1),chi,chi*S,... has change-of-basis determinant one because chi is monic. Hence this matrix theorem gives exactly

    V_N(theta)=D_(N+1)(theta)/B_(N-q+1)(theta).

The D determinant is that of the source measure; the B determinant is that of its Gram multiplier |chi|^2. The latter is not an identification of the contracted ideal at depth two with (chi^2). Higher relation depth still uses the pullback of I^r. At h=1 the quotient is zero-dimensional and its determinant is one, while the nonzero analytic mass is retained.

The polynomial basis construction and analytic moments remain source proofs. The formal theorem covers the finite matrix calculation once those column maps and inverse are supplied.

## 2. Both losses have a division-free numerator formula

Use the source volumes at three consecutive degrees:

    P=V_(N-1)>0, M=V_N, Q=V_(N+1)>0,
    a=omega_(N+1)/omega_N >=0,
    z=sigma-partial_theta log V_N.

The supplied exact radius formula is

    epsilon^2=a(1-M/P)(M/Q-1)-z^2.

Without changing any of these quantities, scalar algebra gives

    epsilon^2
      = a(P-Q)^2/(4PQ)
        -a(2M-P-Q)^2/(4PQ)-z^2.

Indeed 4(P-M)(M-Q)=(P-Q)^2-(2M-P-Q)^2. This rational form is preferable for an exact finite certificate: it does not introduce logarithms or hyperbolic functions just to verify the subtraction of the two squares.

For a>=0 and P,Q>0 it implies

    epsilon^2 <= a(P-Q)^2/(4PQ).

For epsilon>=0 and P>=Q, it also implies

    epsilon <= sqrt(a)(P-Q)/(2sqrt(PQ)).

When a>0, equality in the squared upper bound holds exactly when

    2M=P+Q  and  z=0.

Thus maximality requires the arithmetic midpoint of the original volumes, not their geometric midpoint, as well as zero phase. This is the exact equality case of the source bound; it is not an assumption that either condition holds for the arithmetic family.

The formal module proves these identities, the first-admissible-degree upper bound from its separate endpoint identity, an exact finite logarithmic telescope, and the cancellation under a common explicitly specified volume scaling. No probability normalization of the source mass is used.

## 3. Compose with the original-Gram spectral certificate

The integrated exterior module constructs rank-one control projections from the literal two-coordinate factorization. Its theorem `TraceCertificate.original_gram_bound` applies to an A-invariant subspace with explicit inclusion B, extraction L, and G-orthogonal projector BL. It proves

    |2 Re tr(A_sub)-w dim(E)| <= epsilon

without assuming A is normal or its orthogonal complement is invariant. The exact Gram-coordinate isometry is part of its input data, not a replacement favorable metric.

`TodaTrace.original_gram_volume` invokes that theorem and proves

    4 P Q (2 Re tr(A_sub)-w dim(E))^2 <= a(P-Q)^2.

This is a composition of actual finite certificates. The source's analytic identification of epsilon^2 with the radius energy remains a stated premise, not an undocumented postulate.

On the full positive-defect generalized spectral subspace it gives the source's L_(h,k), with every cyclic length retained. Combining a finite spectral lower allowance with the scalar bound never discards an off-line block or a nilpotent jet.

## 4. Further deduction: endpoint volume budgets select an admitted degree

This section is a new handoff deduction from the supplied finite estimate, not an arithmetic asymptotic claim.

Fix k,h and a nonempty window of r disjoint two-degree steps

    N_j=N_0+2j,  0<=j<r,  N_0>=q.

Suppose the actual recurrence coefficients satisfy sqrt(a_(N_j+1))<=A on that window. Put

    B=log(V_(N_0-1)/V_(N_0+2r-1)) >=0.

By exact telescoping,

    sum_j log(V_(N_j-1)/V_(N_j+1))=B.

At least one j has its logarithmic contraction <=B/r. Since the local finite estimate is epsilon_(N_j)<=A*sinh(log ratio/2), monotonicity of sinh gives

    exists j<r: epsilon_(N_j) <= A*sinh(B/(2r)).

This selects one of the existing canonical representatives. No metric is selected independently, and the source/jet equations remain those at the selected index. The new module formalizes finite selection, the actual volume telescope, and transport through a supplied proved monotone local control function. Instantiation by sinh and the arithmetic recurrence assumptions is the written step above.

For the supplied quartet, let q_k=[1+k(m-1)](k+1)^2. The exact exterior formula gives

    L_(h,k)>=delta*k*q_k/2.

Consequently any proof of

    A_(h,k)*sinh(B_(h,k)/(2r_k))=o(k*q_k)

on an admitted sequence of windows would suffice for that contradiction route. Constants may depend on the fixed packet. In particular, if r_k is bounded below by a positive constant times q_k, A_(h,k)=O(q_k), and B_(h,k)=o(q_k log k), then the displayed target follows: B/(2r)=o(log k), so exp(B/(2r))=k^(o(1)), and the quotient by k*q_k tends to zero. None of these three arithmetic estimates is proved here.

This replaces the need to guess a good degree or uniformly bound every local inverse by a possible endpoint-volume budget. It is still an estimate on the original arithmetic determinants, including their conditioning; it is not a consequence merely of their positivity or Toda identities.

## 5. Toda curvature audit and determinant connections

The source's matrix curvature formula has the correct sign and coefficient. To see this directly, fix the tilted inner product and set Y=XR. The canonical representative obeys R'=-I, where I is the projection of Y into the old relation space. Orthogonality gives

    G'=R*XR,
    G''=Y*Y-2I*I.

The orthogonal decomposition of Y into its representative component, old relation component I, and outgoing component O gives

    Y*Y=G' G^(-1)G'+I*I+O*O.

Subtracting proves G''-G'G^(-1)G'=O*O-I*I. Positivity of either Gram does not give a sign for this difference. The analytic differentiability and the original projection maps remain part of this written argument; this identity is not included in the present Lean target list.

At determinant level, the exact sequence identifies det(source) with det(relations) tensor det(quotient). Thus the quotient logarithmic connection is the difference of the two source connections, and its curvature is the difference of their Toda curvatures. The source's spectral trace sigma and the auxiliary tilt derivative ell_N' are distinct; their difference is the measured cross-term phase. The theta tilt is not a Frobenius or a new weight action.

## 6. What the selected Deligne reading does and does not supply

On printed p.158, Definition 1.3.5 defines determinantal weights using top exterior powers of constituents divided by their ranks. This is the relevant determinant/average-slope operation, not the claim that every positive metric makes an arithmetic object pure. The current finite analogy is the literal normalized trace (2 Re tr a-w dim E)/dim E, with the full determinant line retained by the exterior construction.

On printed p.203, Lemmas 3.2.10--3.2.12 control actual spectral-sequence terms before 3.2.13 uses the tensor-square inclusion and improves the bound. In particular, the geometric estimate is not produced by the tensor-square map itself. In this programme the endpoint-volume/recurrence estimate is a candidate remaining analytic comparison of that role. The exact quotient maps, determinant norms, and exterior trace certificate have been constructed, but these facts do not identify the theta complex with a lisse sheaf satisfying Deligne's finite-field hypotheses.

This reading is deliberately distinct from the uploaded S20 archive, which was inaccessible locally. It adds a source-checked determinant-weight and post-tensor-estimate comparison, not a claim to have audited all Weil II or derived the missing arithmetic bound from it.

## Verification scope

The four new modules' selected targets are listed in TODA_VOLUME_TARGETS.json. The strict workflow uses the unchanged Lean/Mathlib pins and the inherited transitive report parser. Exact finite tests include original relation corrections, nonnormal control, source/relation determinant factors, both losses, quartet multiplicities, mass, and small Hankel-Toda identities. They are declared rational finite calibrations, not actual arithmetic packets. The uploaded numerical theta evaluations and archive tests are not relabelled as fresh executions.

## References

Deligne, P. (1980). La conjecture de Weil. II. Publications mathematiques de l'IHES, 52, 137--252. doi:10.1007/BF02684780. Original scan consulted: https://publications.ias.edu/sites/default/files/Number40.pdf . This turn visually checked printed pp.156,158,203 only; the S20 upload was not reassembled.

National Institute of Standards and Technology. (n.d.). General orthogonal polynomials (Section 18.2). Digital Library of Mathematical Functions. https://dlmf.nist.gov/18.2 . General moment/orthogonal-polynomial background, not a certificate for the particular arithmetic upper estimate.

Supplied research notes (2026-09-12): Tau Toda Volume Control; Tau Exterior Trace Amplification. The source-specific identities and original source/quotient constructions remain attributed to those notes.
