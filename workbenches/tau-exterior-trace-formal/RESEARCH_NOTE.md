# Exterior determinant control and retained filtrations

## Scope and source map

This continuation formalizes the finite determinant-line estimate in the supplied `Tau_Exterior_Trace_Amplification` note. It does not replace the original theta complex, arithmetic inclusion, quotient, unit, support reconstruction, or canonical metric. The parallel contribution's full exterior representative, factorial, Koszul signs and theta primitive remain source statements with their own proof scope.

The implementation is stacked on PR #21 at `2abc351424ba87aeda948a5cfb846e15ed9373d1`, including main `4c5ce7a8575fa8b95df272116eb5783b2309cdb7`. The nonempty-packet qualification and completed 68-target Codex audit are retained. Strict CI, not this prose or a filename, determines the Lean verification status; the PR records the exact completed run when available.

The newly supplied six-part Deligne archive could not be opened in this turn: both local execution services timed out before reading its bytes. No reassembly or manifest check is claimed. Independently, the original author's IAS-hosted scan of *La conjecture de Weil. II* was consulted at printed pages 165, 203 and 206, including sections 1.5.3/1.6.1, 3.2.13, and 3.3.4--3.3.6. This selected reading is not an audit of all 116 pages or of the uploaded transcription. No external source corpus or private transcript is committed here.

The finite-dimensional constructions below are our explicit specialization. Deligne's purity theorem is not invoked for a space that has not been shown to satisfy its hypotheses.

## 1. Original metric and finite theorem

Let C be the original finite cyclic packet, A its multiplication-by-S operator, w=k its retained weight, R its specified representative and G=R*R its positive definite Gram. Write

    W=A*G+GA-wG,    H=G^(-1)W.

Use the actual two-coordinate factorization H=UV from the source boundary rows. It satisfies

    tr(VU)=0,    det(VU)=-epsilon^2,    epsilon>=0.

The theorem proved by the finite interface is this: for every A-invariant subspace with explicit inclusion B and coefficient extraction L, satisfying LB=1 and with BL the G-orthogonal projection,

    |2 Re tr(A_restricted)-w dim(E)| <= epsilon.

A need not be normal or semisimple. In particular, E may be the full sum of generalized eigenspaces whose real parts exceed w/2. Its trace counts every generalized-eigenspace dimension. No invariant orthogonal complement is assumed.

### Constructing the control projections

For a two by two matrix C0, direct Cayley--Hamilton gives

    C0^2-tr(C0) C0+det(C0) I=0.

Thus C0=VU has C0^2=epsilon^2 I, and the literal rectangular maps U,V give

    H^3=epsilon^2 H,
    tr H=0,
    tr H^2=2epsilon^2.

When epsilon>0 put

    F_+=(H^2+epsilon H)/(2epsilon^2),
    F_-=(H^2-epsilon H)/(2epsilon^2).

The cubic identity proves F_+^2=F_+, F_-^2=F_- and epsilon(F_+-F_-)=H. Self-adjointness of H in G proves self-adjointness of these projections. The two trace identities give tr F_+=tr F_-=1. These are control projections, not spectral projections of A.

At epsilon=0, self-adjointness and tr H^2=0 force H=0. It is important to keep this case separate from the formulas that divide by epsilon. A non-self-adjoint nilpotent matrix would not satisfy that implication.

### Projection trace proof

For orthogonal projections P,F in Euclidean coordinates,

    Re tr(PF)=||FP||_HS^2 >=0.

If tr F=1, applying the same equality to 1-P shows Re tr(PF)<=1. Consequently

    tr(PH)=epsilon(tr(PF_+)-tr(PF_-))

has absolute value at most epsilon. The exact slack is

    tr(PH)=epsilon(1-||F_+(1-P)||_HS^2-||F_-P||_HS^2).

For the invariant subspace E, P=BL. Cyclicity of trace and AB=B a give tr(PA)=tr a. Self-adjointness of P gives tr(P A*)=conj(tr(PA)). Thus

    tr(PH)=2 Re tr a-w dim E.

Only AP=PAP is needed. PA=AP is not inferred.

### Explicit isometry, not another metric

The Gram module retains inverse coordinate matrices T,U0 with

    U0 T=T U0=1,    T* T=G.

Transport all maps together:

    A'=T A U0,  H'=T H U0,  B'=T B,  L'=L U0.

Then G becomes the coordinate identity because U0* G U0=1, while B'L'=T(BL)U0 and the control becomes A'*+A'-wI. The original representative is still R U0 in these coordinates, and it has the transported jets, not jets silently reset to the identity. Returning through T recovers the original metric and all original maps. The Lean coordinate object records this isometry as explicit data; its existence for a positive definite finite Gram is the usual Gram-factorization theorem and is not claimed as a new declaration here.

### Oblique spectral projection

Let Q be the CRT idempotent of the same spectral subspace. Then QP=P and PQ=Q, so (P-Q)^2=0. If AQ=QA, trace cyclicity proves tr(PA)=tr(QA). The complement remains: tr f(A)=tr(Q f(A))+tr((1-Q)f(A)). No inverse-compression lemma for an arbitrary oblique projector is used.

## 2. Further deduction: one budget for an entire invariant filtration

This is a complete written deduction, not silently another bundled Lean filtration theorem.

Let 0=E_0 subset E_1 subset ... subset E_s=C be any A-invariant filtration. Let P_i be the orthogonal projections in the same G, and Q_i=P_i-P_(i-1). Nestedness gives P_i P_j=P_min(i,j), hence the Q_i are mutually orthogonal projections summing to 1.

Let a_i be the actual induced action on E_i/E_(i-1). Trace additivity, with the quotient metric supplied by orthogonal projection, gives

    D_i:=2 Re tr a_i-w dim(E_i/E_(i-1))=tr(Q_i H).

Define t_i^+=tr(Q_i F_+), t_i^-=tr(Q_i F_-). Projection positivity proves t_i^+,t_i^->=0, and their respective sums are one. Therefore

    D_i=epsilon(t_i^+-t_i^-),
    sum_i |D_i| <= 2epsilon,
    |sum_{i in J}D_i| <= epsilon

for every subset J of the disjoint graded pieces. The number of layers does not multiply the allowance. This is a finite filtration-control consequence of the same rank-two operator, rather than a fresh estimate assumed on each graded piece.

In an adapted basis G need not be block diagonal. For one step write

    G=[[G11,G12],[G21,G22]],
    Gquot=G22-G21 G11^(-1) G12.

The actual orthogonal lift of quotient coordinates is y -> (-G11^(-1)G12 y,y). It has Gram Gquot, and det G=det G11 det Gquot. Iterating produces exact quotient metrics and determinant norms for the whole filtration. Cross terms have been used in the formula, not discarded by declaration. The induced quotient operator is not the restriction to an arbitrarily selected complement.

For a spectral ordering this gives a capped polygon of cumulative real trace defects. In particular, the total positive defect is at most epsilon and the sum of absolute real defects, counted with algebraic multiplicity, is at most 2epsilon. The underlying matrix principle is classical; the contribution is its explicit map into this source's invariant quotients and metric.

## 3. Deligne machinery that can be applied without changing the arithmetic action

Deligne's section 1.5.3 uses exterior powers and determinant weights to turn aggregate information into individual weight conclusions. Section 1.6.1 constructs the unique monodromy filtration of a nilpotent endomorphism. Section 3.2.13 then requires a geometric estimate after tensoring; the tensor map alone is not that estimate. These are distinct tools, and their hypotheses must remain distinct.

There is an explicit application of the nilpotent-filtration construction to every original cyclic primary packet, independent of a purity claim. On

    C_lambda=C[z]/(z^ell),  A=lambda+N,  N=M_z,

retain the original basis 1,z,...,z^(ell-1). For j in Z define

    M_j=span{z^a : ell-1-2a <= j}.

This is increasing, exhaustive and finite. Multiplication by z lowers the displayed index by two, so NM_j subset M_(j-2). For j>=0 the map

    N^j:Gr_j^M C_lambda -> Gr_(-j)^M C_lambda

is either the zero-space isomorphism on both sides, or takes the one basis class z^((ell-1-j)/2) to z^((ell-1+j)/2) with coefficient exactly one. Thus it is an isomorphism in every case. This verifies the two defining conditions of Deligne's monodromy filtration for this actual Jordan module. No multiple jet is dropped.

The coefficient pairing beta(f,g)=[z^(ell-1)]fg is perfect, and

    (M_j)^perp_beta=M_(-j-1).

This follows because the dual of z^a is z^(ell-1-a), whose index is the negative of the first. Inserting an arithmetic unit gives the corresponding pairing by the explicit invertible multiplication map; it is not set to one.

All these subspaces are invariant under the actual A=lambda+N. Its induced action on each nonzero graded piece is still lambda. In particular the determinant trace is ell*lambda, not a trace on a reduced one-dimensional packet. The filtration can therefore be placed directly into the control calculation of section 2 with its actual quotient metrics.

The auxiliary monodromy indices are not yet Frobenius weights. The actual A commutes with N. A Deligne-type Tate-covariant action would require an additional specific relation with N; it is not manufactured by relabelling the index j. The useful next operation is to formalize this exact filtered module, its quotient duality and the control budget, and then carry a stated analytic comparison through them.

## 4. Concrete analytic target passed back to the other session

For the source's quartet with displacement delta>0, height gamma>0 and common multiplicity m,

    ell_k=1+k(m-1),
    d_k=ell_k(k+1)^2,
    L_(h,k)=2delta ell_k(k+1) floor((k+1)^2/4).

The exact ratio is

    L_(h,k)/d_k = 2delta floor((k+1)^2/4)/(k+1) >= delta*k/2.

Thus any proof epsilon_(h,k,N(k))=o(k*d_k), with N(k)>=d_k-1 and fixed h, suffices for this contradiction argument. For m=1 this is subcubic; for m>1 the corresponding scale is quartic. A uniform bound C_h*d_k would be more than sufficient. None is asserted here.

The prior kernel-update deduction remains attached to the actual convolution measure:

    K_N=sum_(j<=N) b_j b_j*/omega_j,   G_N=K_N^(-1),
    theta_N=(b_N*G_Nb_N)/omega_N in [0,1],
    Lambda_N=(b_(N+1)*G_Nb_(N+1))/omega_(N+1),
    alpha_(N+1)=omega_(N+1)/omega_N.

The determinant lemma gives 1+Lambda_N=det K_(N+1)/det K_N, and

    epsilon_N^2
      =alpha_(N+1)(theta_N Lambda_N
           -|b_N*G_Nb_(N+1)|^2/(omega_N omega_(N+1)))
      <=alpha_(N+1) Lambda_N.

The source's mass omega_0=mu_h^k and all cross terms are retained. The estimate still requires arithmetic control of the recurrence and relative interpolation cost. This document does not infer it from scalar Fisher contraction, absolute Gram decay, a small rank, or a change of homotopy witness.

## 5. Formalization boundary and reproduction

The selected finite trace declarations are specified in `EXTERIOR_TRACE_TARGETS.json`. The construction of the actual exterior algebra object, its additive generator, full spectral-subspace existence, the p! source norm, Koszul boundary primitive and topological completed tensor maps are not all included merely because their determinant-line consequence is proved. The canonical analytic moment construction is also an input rather than a new Lean axiom.

From `formal/splitzero`, the dedicated workflow checks the original environment, each new file using `--trust=0 -DwarningAsError=true`, the combined import, and every existing selected audit. `check_exterior_trace.py` rejects proof escapes and uses the inherited strict report parser. The exact rational checker runs normally and under `python -O` with deliberate-failure controls. Its Gaussian-free rational examples are not actual zeta packets. The uploaded exterior ZIP's reported 22-method suite and the new six-part Deligne archive have not been independently rerun or verified in this environment.

## References

Deligne, P. (1980). La conjecture de Weil. II. *Publications mathematiques de l'IHES, 52*, 137--252. doi:10.1007/BF02684780. Original author-hosted scan: https://publications.ias.edu/sites/default/files/Number40.pdf . Printed pages 165, 203, 206 were visually inspected. The volume number is taken from the journal bibliographic record, not a discrepant label on a host landing page.

Overton, M. L., & Womersley, R. S. (1992). On the sum of the largest eigenvalues of a symmetric matrix. *SIAM Journal on Matrix Analysis and Applications, 13*(1), 41--45. doi:10.1137/0613006. Background for the extremal-trace principle, not the source of the arithmetic representative construction.

Supplied research note: *Tau exterior trace amplification* (2026-09-12), original canonical cyclic control, exterior representatives, multiplicities and typed support maps. This implementation retains its attribution and does not claim the exterior amplification as an independently discovered result.
