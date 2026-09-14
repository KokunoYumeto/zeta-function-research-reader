# Independent check of the incoming PR29 metric continuation

Date: 2026-09-13. Scope: all of the user's supplied continuation, the complete SP1–13 source, and the existing exact SP/AW correspondence receipt. No Lean process was started. The supplied Lean text remains an uncompiled draft; none of the checks below changes that status.

The input is local:user-profile/.codex/attachments/0d84cbd9-4bea-48b2-8d49-3443a3ef7514/pasted-text.txt. The complete original file is retained by the parent intake. This bounded review does not identify a generic polynomial fixture with a zeta-zero packet.

## 1. Source sandwich, signs, and literal primitive

Let H=P_(2q) in its original monomial coordinates. For N in {q−1,q,2q−1,2q}, let I_N:P_N→H be coefficient inclusion, B_N:P_(N−q)→H multiplication by the original monic chi followed by inclusion, and C:E→H the fixed degree-less-than-q monomial lift. Put H_a=B_N* M_a B_N and K_a=H_a^(-1)B_N* M_a C when N≥q. At N=q−1, use the unique map K_a:E→{0}; no inverse is introduced. Then rho_a=C−B_N K_a and G_a=rho_a* M_a rho_a.

Multiplication by monic chi is injective, so H_a is positive definite on its admitted relation space. The identity B_N* M_a rho_a=0 proves the canonical orthogonality. The difference is the actual relation

    delta = rho_1−rho_0 = B_N(K_0−K_1).

Thus rho_1=rho_0+delta, and orthogonality in M_0 yields rho_1* M_0 rho_1=G_0+delta* M_0 delta. Likewise rho_0=rho_1−delta and orthogonality in M_1 yields rho_0* M_1 rho_0=G_1+delta* M_1 delta. Substitution gives exactly

    G_1−aG_0 = rho_1*(M_1−aM_0)rho_1 + a delta* M_0 delta,
    bG_0−G_1 = rho_0*(bM_0−M_1)rho_0 + delta* M_1 delta.

Both retained boundary-Gram signs are positive. The identities require only a real scalar for their algebra; their positivity consequence uses a≥0 and the stated positive source comparisons. At N=q−1, B has zero columns and delta=0, and both identities remain exact.

For aM_0≤M_1≤bM_0 with 0<a≤b, congruence of the source inequalities and positivity of the boundary terms give aG_0≤G_1≤bG_0. All q eigenvalues of G_0^(-1)G_1 therefore lie in [a,b], so q log a≤log(det G_1/det G_0)≤q log b. The two positive and two negative endpoint signs give the supplied 2q log(b/a) bound. The bound is valid. The already proved SP13/AW14 control supplies the stronger coefficient 2q−1 for the same source enclosure: the relative source eigenvalue ratio is at most b/a, and SP13 yields (2q−1)log(b/a). Both statements must be attributed correctly, and the older stronger control must not be dropped in propagation.

A common source scalar c>0 changes each G_N to cG_N because K_a is unchanged. Each determinant acquires c^q, whose two positive and two negative powers cancel in the original endpoint observation. This is a proved effect of the literal scaling map M→cM; no source matrix is replaced by a normalized representative.

The relation primitive above is an element of the actual polynomial relation domain. It is not, by itself, a proof that an arbitrary proper-W supported class vanishes. The supplied formal supported-sandwich draft explicitly requires its hB inclusion of relation columns in the specified original relation fibre. That hypothesis is essential to the supported conclusion; the finite Gram identities require no claim that every finite-observation kernel is an original boundary.

## 2. Canonical quotient projector equals source projector minus relation projector

Use Pi_N for the incoming text's projector P_N, reserving P_N and Q_N for the established SP source and relation projectors:

    P_N = I_N (I_N* M I_N)^(-1) I_N* M,
    Q_N = B_N (B_N* M B_N)^(-1) B_N* M,
    Pi_N = rho_N G_N^(-1) rho_N* M.

At the first degree Q_(q−1)=0. Every v in I_N(P_N) has a unique polynomial decomposition v=C e+B_N w by Euclidean division by the same monic chi. Replacing C by rho_N=C−B_NK_N gives v=rho_N e+B_N(w+K_N e). Orthogonality gives the direct M-orthogonal sum

    I_N(P_N) = image(rho_N) orthogonal-direct-sum image(B_N).

On these two subspaces and their common ambient orthogonal complement, the two sides of Pi_N=P_N−Q_N have the same actions, respectively identity, zero, and zero. This proves their exact equality as endomorphisms of the unchanged H. It also proves Pi_N^2=Pi_N, Pi_N* M=M Pi_N, and Tr Pi_N=q.

The incoming signed projector is

    A = Pi_(q−1)+Pi_q−Pi_(2q−1)−Pi_(2q).

Substituting Pi_N=P_N−Q_N and Q_(q−1)=0 gives

    A = (Q_(2q−1)+Q_(2q)−Q_q)
        − ((P_(2q−1)−P_(q−1))+(P_(2q)−P_q)).

Consequently A is exactly SP's mathcal R−mathcal P and AW's U−W. The incoming X=M^(-1)dot M is exactly SP's T and AW's C. The new interpolation variable s equals their x or t by the identity parameter map, and all original source coordinates and masses remain unchanged. The orientation agrees; there is no sign reversal.

Differentiating pi_chi rho_N=I gives pi_chi rho_N'=0 in the original polynomial quotient, so rho_N' lies in the admitted polynomial relation subspace. Canonical orthogonality removes both derivative cross terms in G_N'=rho_N'*M rho_N+rho_N*dot M rho_N+rho_N*M rho_N'. Hence G_N'=rho_N*dot M rho_N. Jacobi's formula and cyclicity give (log det G_N)'=Tr(X Pi_N). The four original signs prove B'=Tr(XA), and Tr A=0 proves Tr(XA)=Tr((X−cI)A) for every real c. This signed pairing is the same previously proved AW/SP first variation in canonical-section coordinates.

## 3. Exact cross-Gram and restriction-loss identities

For i≤j, write B_i=B_j J_(i,j), with J the literal zero-padding of relation coefficients. Then

    rho_i−rho_j = B_j(K_j−J_(i,j)K_i).

The right side is a degree-at-most-j original polynomial relation. Orthogonality of rho_j to image(B_j) gives rho_j* M rho_i=G_j. Taking adjoints gives rho_i* M rho_j=G_j because G_j is Hermitian. Thus

    Tr(Pi_i Pi_j)
      = Tr(G_i^(-1) (rho_i* M rho_j) G_j^(-1) (rho_j* M rho_i))
      = Tr(G_i^(-1) G_j).

Since rho_i=rho_j+(rho_i−rho_j), the same orthogonality gives

    G_i−G_j = (rho_i−rho_j)* M (rho_i−rho_j) ≥ 0.

Therefore T_(i,j)=G_i^(-1)G_j is positive and self-adjoint in G_i, with spectrum in (0,1]. Its loss Tr(I−T_(i,j)) is nonnegative. Idempotence and trace q of both projectors imply

    Tr((Pi_i−Pi_j)^2) = 2q−2Tr(Pi_i Pi_j)
                         = 2Tr(I−T_(i,j)).

Let A_0=Pi_(q−1)−Pi_(2q−1), A_1=Pi_q−Pi_(2q), so A=A_0+A_1. Expanding the square and using trace cyclicity gives the retained cross term

    Tr(A^2)=2 loss_0+2 loss_1+2Tr(A_0 A_1).

No sign is assigned to Tr(A_0 A_1). After simultaneous conjugation Z→M^(1/2) Z M^(−1/2), all these M-self-adjoint operators become Hermitian, their products have unchanged traces, and ||A_0+A_1||_HS^2≤2||A_0||_HS^2+2||A_1||_HS^2 gives Tr(A^2)≤4(loss_0+loss_1). This conjugation is a typed isometry from the original metric space to Euclidean coordinates, used to prove the inequality; the original Gram and source observation remain the ones defined above.

## 4. Centered and signed residual bounds

The relation M X=dot M=dot M* implies X is M-self-adjoint, its eigenvalues and trace are real, and the centered operator X_c=X−Tr(X)I/n has squared Hilbert–Schmidt norm

    Sigma=Tr(X_c^2)=Tr(X^2)−Tr(X)^2/n≥0, n=2q+1.

Cauchy–Schwarz after the same metric isometry gives |Tr(XA)|^2≤Sigma Tr(A^2), and therefore the two bounds in the incoming (13). For any specified M-self-adjoint Y, let E=X_c−Y. Then Tr(XA)=Tr(YA)+Tr(EA), all terms are real, and |Tr(EA)|≤sqrt(Tr(E^2)Tr(A^2)). This proves both signed inequalities in (14). The formula retains the signed central correlation and an actual residual; assigning Y alone gives no sign conclusion.

## 5. Finite polynomial signed certificate and uniform remainder

Let D=M_0^(-1)M_1, with its actual positive eigenvalues d_1,...,d_n in the M_0 metric. Write alpha=min d_j and beta=max d_j. For x in [0,1], set

    B_x=I+x(D−I), a_x=(2+x(alpha+beta−2))/2,
    H_x=I−B_x/a_x, C_x=B_x^(-1)(D−I).

The factorization M_x=M_0 B_x is literal, so C_x is the same relative source derivative X. All these endomorphisms are real rational functions of D with no poles on its positive spectrum. They commute and are self-adjoint in M_0. Since M_x=M_0 B_x and B_x commutes with them, they are also self-adjoint in the actual M_x metric.

For L≥0 define

    C_(L,x)=a_x^(-1) (sum_(r=0)^L H_x^r)(D−I).

Multiplying the finite geometric identity (I−H)sum_(r=0)^L H^r=I−H^(L+1) by C_x and using I−H_x=B_x/a_x proves exactly

    C_x−C_(L,x)=H_x^(L+1) C_x.

In a single M_0-orthonormal eigenbasis of D, the eigenvalues of C_x and H_x are

    c_j(x)=(d_j−1)/(1+x(d_j−1)),
    h_j(x)=1−(1+x(d_j−1))/a_x.

The same eigenvectors are orthogonal in M_x, with literal squared weights 1+x(d_j−1); their normalization only effects the metric isometry used in the proof. The residual eigenvalues are delta_j(x)=h_j(x)^(L+1)c_j(x). Centering C_(L,x) as Y_(L,x)=C_(L,x)−Tr(C_(L,x))I/n and centering its residual as E_(L,x) gives X_c=Y_(L,x)+E_(L,x) and exactly

    Tr(E_(L,x)^2)=sum_j delta_j(x)^2−(sum_j delta_j(x))^2/n.

The midpoint choice yields max_j |h_j(x)|≤theta_x=x(beta−alpha)/(2+x(alpha+beta−2)). Its derivative is 2(beta−alpha)/(2+x(alpha+beta−2))^2≥0, so theta_x≤theta=(beta−alpha)/(beta+alpha)<1. Further |c_j(x)|≤|d_j−1|/min(1,d_j), hence with the finite exact constant

    K=sum_j (|d_j−1|/min(1,d_j))^2

one has Tr(E_(L,x)^2)≤theta^(2(L+1))K. Existing SP8 and the actual range-overlap inequality Tr(UW)≥1 give Tr(A_x^2)=8q−4−2Tr(UW)≤8q−6. Applying the signed residual bound and integrating over an interval of length one proves

    | C_(h,k) − integral_0^1 Tr(Y_(L,x) A_x) dx |
      ≤ theta^(L+1) sqrt(K(8q−6)).

The exact pointwise radius from the residual variance and actual Tr(A_x^2) is retained and may be smaller. The finite approximant and its signed integral use the original source projector; the displayed geometric tail gives convergence for each specified positive source pair. It does not assert a uniform growing-family arithmetic estimate for K, theta, or the signed central term. At alpha=beta, H=0, the approximation is exact from L=0; scalar cancellation also makes the endpoint contrast zero.

For rational input validation one may use certified source spectral enclosures alpha_0≤d_j≤beta_0 in the same midpoint formula. The identical proof then gives theta≤(beta_0−alpha_0)/(beta_0+alpha_0); this is a bound on the original matrices, not a replacement of their eigenvalues. Our exact fixtures use [1,100] and retain their actual matrices throughout.

## 6. Executable verification

The accompanying check_incoming_metric.py constructs all source and quotient matrices from the original polynomial coordinate S=1/2+i y and the literal Gaussian moments of mass seven and variance one. The second density multiplies this measure by 2+2y+y^2=1+(y+1)^2 and has literal mass twenty-one. The three polynomial fixtures are S−1/2, (S−1/2)^2, and 1+(S−1/2)^2; they include q=1, a repeated primary q=2, and a distinct-root q=2. The endpoint matrices are certified positive and noncommuting. Every relation matrix is actual polynomial multiplication by chi.

The checks cover every admitted endpoint, the zero-dimensional first relation, the literal relation primitive, both signed scaled identities and inequalities, the failure of the opposite boundary signs when the boundary is nonzero, common mass scaling, all ordered cross-Grams and restriction-loss pairs, canonical/source/relation projector equality, the exact AW/SP orientation, retained cross term, centered and signed residual inequalities, and L=0,1,2 polynomial certificates at x=0,1/3,1/2,1. A separate symbolic differentiation of the full determinant ratio is compared with the signed projector trace. Results and pins are in exact_check_results.json and MANIFEST.json after the completed run.

The completed run passed all 1,841 exact checks in 367.022 seconds. All three complete symbolic determinant derivatives matched the original-source signed pairing. The script SHA256 is a98b2e9d7c8cdc20de977ee193c22ab31e680a166c55c1d6cc051074922e1991. The exact input SHA256 is caab15a2eee196cb1b8d38060726c77db518a06c34eaaaa8789160fe80c182f7. The calculation uses no floating-point tolerance or numerical eigenvalue approximation.

## 7. Complete ISM source acceptance

I read the complete actual parent source incoming_source_metric_control.tex, ISM1–43, then reread both revised regions after the two precision repairs. The accepted source has 692 lines and SHA256 3028a11f991b872751209cfca83c05657875ed8d70da3adff5d1cb4b9f0ed79e. The full End(H) algebra is now explicitly the domain of the conjugation isomorphism, with the self-adjoint subset mapped to Hermitian endomorphisms. The supported comparison now uses the fixed finite coefficient carrier (T tensor-power k) direct-summed over I, with literal A→I zero insertion, preserving every outer support label.

The added full two-leg comparison is exact. For T=[V direct-sum F(V)→B], d(phi,hatpsi)=Theta(phi−F^(-1)hatpsi), both j_+(v)=(v,0) and j_−(v)=(0,−Fv) are cochain maps from the one-leg complex with degree-one identity. The map p(phi,hatpsi)=phi−F^(-1)hatpsi satisfies p j_+=p j_−=identity; their difference j_+−j_− is the full diagonal (v,Fv), in the degree-zero kernel. Tensoring these maps preserves the differential signs in ISM40 and hence the proved primitive identity ISM41. Applying the construction componentwise to the full carrier retains the diagonal and coefficient faces.

For ISM38–39, the cyclic annihilation chi(A_h^(k))1=0 makes the multivariate polynomial f_v zero in the tensor quotient. Successive monic division preserves every earlier variable's degree bound and yields a final multivariate remainder with every degree below deg h. The tensor monomial basis makes this remainder zero, proving the literal telescoping decomposition. The primitive ISM40 has exactly i−1 preceding degree-one factors; its inserted sign cancels the differential sign and gives the stated positive sum. This proves ISM41 in the original source, retaining the full unit through ISM1.

ISM42 is the exact kernel quotient of supported top cohomology mapping to the full top quotient. Its class is zero precisely when the displayed full-source boundary is also a boundary from the declared supported subcomplex. The chosen primitive's membership is a sufficient witness, and is never inferred for arbitrary proper W. In the one-coefficient, one-factor specialization of ISM43, W is the admitted source image under p and the boundary range is Theta W; injectivity of Theta identifies its kernel with V/W exactly. The final componentwise statement applies this same map to the other coefficient positions.

No mathematical defect remains in this bounded written-source audit. Acceptance covers the complete written ISM1–43 source at the stated pin and the exact finite checks. It does not certify the supplied Lean draft, a growing-family arithmetic asymptotic, or any unpublished ZIP contents.
