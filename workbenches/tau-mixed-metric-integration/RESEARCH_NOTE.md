# Canonical source bounds with mixed support retained

13 September 2026. This continuation combines the recovered source-resolvent work with the actual current main and the original SplitZero reconstruction. The newly published marked-product note was read through its full source, including the external weight-k family, cyclic family defect, mixed theta-source pairing, and signed four-endpoint formula. The published R62 reader and all prior sources remain unchanged. Verification status is recorded only after observing a completed run.

## 1. What mixed support means here

The scalar remains G(R)={tau} disjoint-union R^bullet, with e=0^bullet. We use the existing LinearDiagram and its Total, not a new scalar or a product of independently forgotten fibres. In Total,

    (i,x)+(j,y)=(i join j, D(i<=i join j)x+D(j<=i join j)y).

No injectivity of transports is assumed. The bottom fibre is as in the original general interface; claims excluding global absence state a nonbottom receiving label explicitly. The original Relations quotient retains labels and imposes only the supplied original relation submodules.

For a finite family x_a=(i_a,v_a), its support is join_a i_a. If v_a is an original boundary in its own fibre, linearity of the EXISTING quotient and stability of the original relations prove that its sum maps to (join_a i_a,0). A nonbottom join is not global absence even when the amplitudes cancel completely. The empty family has bottom support, as it must.

For canonical representative changes at different supports, the recovered resolvent supplies the explicit boundary primitive in each input fibre. The new `mixed_canonical_classes` theorem adds their images using the actual G(R)-linear total quotient map and proves equality of the resulting original classes. It does not infer boundary membership from equality of finite observations.

At a specified common receiving support J, every source column is first transported by D(i_a<=J). Only then is its specified coordinate equivalence applied for the metric observation. For those transported matrices F_a,

    Gram_M(sum_a F_a) = sum_a sum_b F_a^* M F_b.

This is `gathered_gram`, with its actual column transports constructed. The corresponding columns' original boundary membership and quotient image are checked separately by `gathered_column_boundary`. Koszul or other original signs are part of the columns before the double sum. There is no rule making a!=b terms vanish merely because the initial labels differ. For the marked-product note's (46), these are the separate Zi terms and every conjugate Zi*Zj pairing.

This is the finite mixed-sum and metric interface, not a claim that a complete new tensor/sheaf/six-functor formalism has been implemented. It imports and is checked together with the original synchronization and joint homotopy. Future changes to mixed-support tensor machinery must be reviewed through these explicit maps, not silently replaced by a constant active support.

## 2. Source enclosures descend with both boundary Grams

Keep the actual relation columns B and fixed quotient lifts C. For the inherited Metric M_a, its canonical representative and Gram are

    R_a=C-B(B^* M_a B)^(-1) B^* M_a C,    G_a=R_a^* M_a R_a.

Write Delta=R_1-R_0. The original primitive is B(Z_0-Z_1), and the recovered resolvent computes it from the actual perturbation. The proved Pythagoras identities give

    G_1-a G_0 = R_1^*(M_1-a M_0)R_1 + a Delta^* M_0 Delta,
    b G_0-G_1 = R_0^*(b M_0-M_1)R_0 + Delta^* M_1 Delta.

Expansion proves both identities; positivity of each displayed summand yields the quotient sandwich whenever a>=0 and the source hypotheses hold. No new chosen metric or relation space enters. `supported_sandwich` accompanies these inequalities with equality in the original Relations.quotientDiagram after the specified source-coordinate equivalence. The first admissible degree has a zero-dimensional relation space; no earlier inverse is introduced.

The following determinant consequence has a complete written proof but is not a new Lean log-monotonicity theorem in this contribution. If 0<a<=b and a M0<=M1<=b M0 on the common degree-2q source, each of the four restricted q-dimensional quotient Grams satisfies the same sandwich. Its generalized eigenvalues belong to [a,b], hence

    q log a <= log(V_N^1/V_N^0) <= q log b.

Combining two added and two subtracted endpoints gives

    |B(M1)-B(M0)| <= 2 q log(b/a).

A relative source enclosure (1-epsilon) Mhat<=M<=(1+epsilon) Mhat, epsilon<1, thus gives error at most 2q log((1+epsilon)/(1-epsilon)) for the entire four-endpoint expression. A common source mass multiplier cancels only after the original q-dimensional determinant factors are retained.

## 3. All four projectors occupy the same source

Let rho_N:E->P_(2q) be the padded original canonical representative and G_N=rho_N^* M rho_N. Set

    P_N=rho_N G_N^(-1) rho_N^* M.

The projector, its weighted adjoint equation P_N^* M=M P_N, and trace q are derived from the actual inverse-Gram equation. No Euclidean self-adjointness is assumed.

For X=M^(-1) E_M, the finite identity

    tr(G_N^(-1) rho_N^* E_M rho_N)=tr(X P_N)

is proved by cyclicity with the original inverse M. On the affine source path M_s=M_Gamma+s(M_ar-M_Gamma), the inherited written derivative G_N'=rho_N^* E_M rho_N therefore gives

    d/ds B(M_s)=tr(X_s Q_s),
    Q_s=P_(q-1)+P_q-P_(2q-1)-P_(2q).

The finite trace identity is checked; the path derivative and its integral remain the source's written analytic result. Since tr(Q_s)=0, every common scalar c cancels exactly:

    tr((X_s-c I)Q_s)=tr(X_s Q_s).

This does not set a source mass to one. It removes a scalar direction only from the signed observation. The equal-rank cancellation is about the traces of these q-rank projectors; the positive shell operators in the marked-product source have trace 2q but rank q+1, not rank 2q.

For nested endpoints i<=j, the original cross-Gram relation rho_j^* M rho_i=G_j and its conjugate prove

    tr(P_i P_j)=tr(G_i^(-1)G_j),
    tr((P_i-P_j)^2)=2 tr(I-G_i^(-1)G_j).

Thus, with Q0=P_(q-1)-P_(2q-1) and Q1=P_q-P_(2q),

    tr(Q_s^2)=tr(Q0^2)+tr(Q1^2)+2 tr(Q0 Q1).

The last cross term is retained in the new finite formalization. It is not assigned a favorable sign.

The subsequent estimate is a written proof: simultaneously conjugate X_s and Q_s by M_s^(1/2) to Hermitian matrices, subtract c=tr(X_s)/(2q+1), and apply Hilbert-Schmidt Cauchy-Schwarz. This gives

    |B'(M_s)|^2 <= [tr(X_s^2)-(tr X_s)^2/(2q+1)] tr(Q_s^2),
    tr(Q_s^2) <= 4 [tr(I-T_0)+tr(I-T_1)].

A specified weighted-self-adjoint approximation Y_s to X_s-cI gives a signed interval centered at tr(Y_s Q_s), with error sqrt(tr((X_s-cI-Y_s)^2) tr(Q_s^2)). Integrating is an actual arithmetic-correlation target, not a proof of its sign. Certified trace errors can use the recovered finite log-input module without subtracting independently upper-bounded prefixes.

## 4. Recovery and verification boundary

The recovered eight-file resolvent branch is retained with ancestry and attribution. Its proved finite content includes the exact cross-block primitive, nonlinear canonical quotient secant, and signed logarithm enclosure for bounded input data. The latest old failure was an unused section instance, corrected by narrowing its binder rather than disabling strict warnings. FAILURE_REVIEW.md records the full observed failures and distinguishes them from local transport timeouts.

The new runner executes the recovered runner, then strictly compiles every additional member of the used dependency closure, including the original synchronization module. It reuses the original fail-closed axiom parser, prints all selected transitive axioms in a combined environment, and records hashes. The independent finite job runs even if a Lean proof fails, so a skipped test is never called a passing test. False-formula controls include omission of the mixed Gram, collapse of nonbottom join to absence, and omission of the old-boundary secant loss.

The finite fixtures retain Gaussian mass seven, the original-style coordinate S=1/2+i*x, positive asymmetric density changes, repeated-root quotients, complex noncommuting matrices, and the first degree with no relation columns. They are not asserted arithmetic zero packets. The actual arithmetic input remains g=2xi, full h multiplicities and Taylor units, its infinite theta quotient, and the explicit theta primitives in the marked-product note.

No uniform arithmetic endpoint bound, no finite-field-to-arithmetic purity transfer, and no impossibility theorem for the programme is claimed. The new three-module scope is source sandwiches, actual mixed joins/cross pairings, and common-source projector algebra; the surrounding derivative and norm comparisons have the stated written proofs.
