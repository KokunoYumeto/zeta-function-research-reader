# Orthogonal theta boundaries and rank-two arithmetic control

Owner-directed SplitZero continuation, 12 September 2026. Base: PR #11, d37eade4f9e6a82c1a88aeff710a3b851a34eb49. This is an additive research contribution with written proofs for review, not a new Lean certificate. The conversation delivery contains a longer numbered LaTeX/HTML version, the full reading record, and exploratory arithmetic moments.

## 1. Reviewed input and exact types

The supplied other-session theorem is correct: for injective Theta:V->B, an R-linear automorphism F, Q=B/Theta V, and kappa:B->V with kappa Theta=0, all homotopies satisfying BOTH dH=Theta kappa and Hd=0, for d(v,w)=Theta(v-Fw), are

    H_alpha(b)=(kappa b+alpha qb, F^-1 alpha qb),   alpha:Q->R V.

Writing H=(u,v) gives u-Fv=kappa. Since d(x,0)=Theta x, Hd=0 gives H Theta=0; hence Fv descends uniquely to alpha. Substitution proves the converse. The difference is gamma(alpha-beta)q with gamma(v)=(v,F^-1v). The solution set is affine relative to H_0, not generally a vector space with the zero homotopy as origin.

Its Lean draft remains uncompiled. Neither lean nor lake is installed in this runtime. The proposed zero-composition repair has the right mathematical type, but no kernel certificate is inferred from that observation. PR #11 already supplies the continuous specialization, the Fourier twist over C[t], support-changing lifts, coherent dilations and representative-change formulas. Those are retained inputs, not new results here.

Keep the original tau base and the square G(Z)->G(C) over Z->C, with p:G(Z)->Z still infinite, e=ofR(0), and tau the external scalar zero. No Boolean localization replaces the base quotient. All quotient relations below use the original internal coequalizer and preserve the support label.

Retain V, B and the actual operators of PRs #8-#11:

    V={even Schwartz phi on R: phi(0)=0 and integral(phi)=0};
    B={smooth F on R_+: sup x^b |D^k F(x)|<infinity for all integer b and k>=0};
    D=-x d/dx; Theta phi(x)=2 sum_(n>=1) phi(nx);
    M F(s)=integral_0^infinity F(x)x^s dx/x;
    phi_*=(4 pi^2 x^4-6 pi x^2)exp(-pi x^2);
    phi_j=D^j phi_*; f_j=Theta phi_j=D^j f_0;
    M f_j(s)=s^j g(s), g=2 xi.

The Hilbert observation is H=L2(R_+,dx), conjugate-linear in the first argument. Polynomial packet coordinates are retained, not changed to orthonormal coordinates.

For an actual finite packet with all multiplicities, let E=C[t]/h_Z, A=M_t. The previous analytic constructions supply

    R_0:E->B, J_Z:B->E, qR_0=sigma_Z, J_ZR_0=1, J_ZTheta=0,
    DR_0-R_0 A=f_0 ell_Z.

The exact ell_Z comes from epsilon_Z=j_h(h/(2 xi)); at a simple zero its value on 1 is 1/(2 xi'(rho)). These analytic constructions remain the cited research-proof dependencies, not theorems certified by the finite tests here.

## 2. An actual minimum over the admitted theta relations

For m>=0 define

    W_m=span(phi_0,...,phi_m);
    Phi_m:C^(m+1)->V, c |-> sum c_j phi_j;
    F_m=Theta Phi_m:C^(m+1)->H;
    H_m=F_m* F_m; C_m=F_m* R_0; G_0=R_0*R_0.

The f_j are independent: Mellin sends a relation to g(s)P(s)=0. Thus H_m is positive definite. Here C_m is a cross-Gram matrix E->C^(m+1), not the complex of that name in the endpoint workbench.

Set

    B_m=-H_m^-1 C_m;
    Pi_m=F_m H_m^-1 F_m*;
    R_m=R_0+Theta Phi_m B_m=(1-Pi_m)R_0.

The correction is a finite original theta boundary, so R_m lands in B, qR_m=sigma_Z, and J_ZR_m=1 at every m. Direct multiplication proves

    F_m*R_m=0;
    G_m=R_m*R_m=G_0-C_m*H_m^-1 C_m >0.

Positive definiteness follows from J_ZR_m=1. For any B:E->C^(m+1),

    (R_0+F_m B)*(R_0+F_m B)
      =G_m+(B-B_m)*H_m(B-B_m).

This is the minimum of the Hilbert Gram within the stated source family, not yet a minimum of its relative weight error. Also (1-Pi_m)(R_0+F_m B')=R_m: changing the initial representative by a relation already in W_m leaves the result unchanged.

## 3. The complete control form has rank at most two

Let I_m,S_m:C^(m+1)->C^(m+2) be I_m e_j=e_j and S_m e_j=e_(j+1). Define

    K_m=e_0 ell_Z+S_m B_m-I_m B_m A.

Then

    DR_m-R_m A=F_(m+1)K_m=Theta(Phi_(m+1)K_m).

No boundary component is discarded in this identity. Put b_m=e_m*B_m:E->C, and z_m=R_m*f_(m+1):C->E. Integration by parts on the stated source functions gives

    <DF,H>+<F,DH>=<F,H>,

with vanishing boundary term [x conjugate(F)H]_0^infinity. Hence

    W_m=A*G_m+G_m A-G_m
       =-(R_m*F_(m+1)K_m+K_m*F_(m+1)*R_m)
       =-z_m b_m-b_m*z_m*.

The last equality uses F_m*R_m=0 and the exact last row of K_m, which is b_m. Thus rank(W_m)<=2 for every packet dimension and every finite m. The pairings with the first m+1 theta directions vanish; those supported vectors themselves are retained.

Define the actual scalar quantities

    u_m=z_m*G_m^-1 z_m >=0;
    v_m=b_m G_m^-1 b_m* >=0;
    c_m=b_m G_m^-1 z_m.

The nonzero spectrum of G_m^-1 W_m is the nonzero spectrum of

    -[[c_m,v_m],[u_m,conjugate(c_m)]].

This follows by factoring through the two-column map [z_m,b_m*] and using the equality of nonzero spectra of the two compositions. Its trace is -2 Re(c_m), determinant |c_m|^2-u_m v_m. Therefore the least symmetric control allowance is

    epsilon_m=|Re(c_m)|+sqrt(u_m v_m-(Im(c_m))^2),
    -epsilon_m G_m <= W_m <= epsilon_m G_m.

Cauchy-Schwarz makes the radicand nonnegative. The formula also covers rank one. A reflection-stable full packet has

    trace(G_m^-1 W_m)=2 Re(trace A)-dim E=0,

so Re(c_m)=0. This is an exact trace identity, not a choice of coordinates. For every eigenvector Av=rho v,

    (v*W_m v)/(v*G_m v)=2 Re(rho)-1.

Thus the relative control still detects precisely the original spectral weight.

## 4. The next relation is a rank-one update with its own retained coordinate

Set

    a_(m+1)=(1-Pi_m)f_(m+1)=Theta psi_(m+1),
    psi_(m+1)=phi_(m+1)-Phi_m H_m^-1 F_m*f_(m+1),
    eta_(m+1)=||a_(m+1)||^2 >0.

Then R_m*a_(m+1)=z_m, and orthogonal decomposition gives

    Pi_(m+1)=Pi_m+a_(m+1) eta_(m+1)^-1 a_(m+1)*;
    R_(m+1)=R_m-a_(m+1) eta_(m+1)^-1 z_m*;
    G_(m+1)=G_m-eta_(m+1)^-1 z_m z_m*.

The control update is obtained by applying the same real-linear operator X |-> A*X+XA-X to the last identity.

The original quotient transport is

    Q_Wm=B/Theta W_m -> Q_W(m+1)=B/Theta W_(m+1),
    kernel=Theta W_(m+1)/Theta W_m ~= W_(m+1)/W_m.

That kernel is one-dimensional. The square E->Q_Wm by R_m and E->Q_W(m+1) by R_(m+1) commutes. The new relation becomes the supported zero only through the actual next-level quotient; it is not another scalar adjunction at the bottom.

There is a form on the entire quotient:

    Hcal_m([F],[G])=<(1-Pi_m)F,(1-Pi_m)G>.

It is positive definite since the kernel of 1-Pi_m in B is exactly Theta W_m. Let lambda_(m+1)[F]=<a_(m+1),F>. This is well defined on Q_Wm and

    Hcal_m(x,y)=Hcal_(m+1)(qx,qy)
                +eta_(m+1)^-1 conjugate(lambda(x))lambda(y).

The map (q,lambda):Q_Wm -> Q_W(m+1) plus C is a linear isomorphism. Its inverse is

    ([F],c) |-> [F-a eta^-1<a,F>+a eta^-1 c]_Wm.

Changing F by a relation at level m+1 changes this expression only by a relation at level m. This supplies the exact metric comparison between levels instead of treating the quotient transports as isometries.

Every displayed linear map has its original fixed-support lift. On the full source chain, reconstructed addition uses the join max(m,n) and the above transports. The scalar e sends (m,[F]) to (m,[0]); tau sends it to external absence. The two-leg primitives are (k_m u,0) and (0,-Fourier^-1 k_m u), where k_m=Phi_(m+1)K_m. Synchronization by the original E_sync=(1,e) supplies their common joint support. Their difference remains the H0 cycle (k_m u,Fourier^-1 k_m u). The other session's Hom(Q,H0) freedom leaves their differential and hence W_m unchanged.

## 5. Actual arithmetic moments and their truncation allowance

The matrices H_m come from the original arithmetic functions. Since JF(x)=x^-1 F(1/x) is unitary on L2(dx), Jf_0=f_0 and JD=(1-D)J,

    H_ij=integral_1^infinity [conjugate(f_i)f_j
                 +conjugate(f_i^ref)f_j^ref] dx,
    f_j^ref=(1-D)^j f_0.

This retains both multiplicative ends and permits absolutely convergent Gaussian sums on x>=1. Write

    phi_j(x)=P_j(x)exp(-pi x^2),
    P_0=4 pi^2 x^4-6 pi x^2,
    P_(j+1)=2 pi x^2 P_j-x P_j',
    P_j=sum_r c_(j,r)x^(2r),
    c_(j+1,r)=2 pi c_(j,r-1)-2r c_(j,r).

For f_j^[N](x)=2 sum_(n=1)^N P_j(nx)exp(-pi n^2x^2), put

    C_j=sum_r |c_(j,r)|sqrt(Gamma(2r+1/2)/(2 pi^(2r+1/2))).

Then

    ||f_j-f_j^[N]||_L2([1,infinity))
      <= 2 C_j (N+1)^(-1/2) exp(-pi(N+1)^2/2)
         /[1-exp(-pi(2N+3)/2)].

Proof: on x>=1, 2 pi n^2x^2 >= pi n^2+pi n^2x^2. Integrating each monomial's squared bound gives n^-1/2 exp(-pi n^2/2) times the displayed gamma constant. Minkowski and a geometric bound on consecutive n terms give the formula. The reflected derivative retains the absolute binomial sum of these allowances.

The finite integral entries use exactly

    integral_1^infinity x^(2k)exp(-c x^2) dx
      =Gamma(k+1/2,c)/(2 c^(k+1/2)), c=pi(n^2+n'^2).

For truncation tail norms delta_i,delta_j, each inner-product error is bounded by delta_i||f_j^[N]||+||f_i^[N]||delta_j+delta_i delta_j, plus its reflected contribution. Numerical evaluation errors for the finite expression still require their own enclosure. The optional conversation computation is explicitly exploratory, not interval-certified.

The exact consistency check is H_(i+1,j)+H_(i,j+1)=H_ij. Cross-Gram columns F_m*R_0 remain their actual source integrals and are not replaced by arbitrary matrices.

## 6. The same source proves a strong topology comparison

For this actual f_0,

    closure span{D^j f_0:j>=0} in L2(R_+,dx) = H.

Proof. The explicit unitary Mellin-line map sends F to M F(1/2+it) in L2(R,dt/(2 pi)). It sends D to 1/2+it and f_j to (1/2+it)^j g(1/2+it). The log-space function h(z)=exp(z/2) f_0(exp z) is holomorphic in |Im z|<pi/4 by its Gaussian series. For |Im z|<=a<pi/4 it decays superexponentially as Re z tends to positive infinity. Poisson gives h(z)=h(-z), so the same holds at the other end. Fourier contour displacement therefore gives |g(1/2+it)|<=C_a exp(-a|t|).

The measure dmu=|g(1/2+it)|^2dt/(2 pi) has a positive exponential moment. If an L2(mu) function is orthogonal to all polynomials, multiplying mu by its conjugate gives a finite complex measure with a smaller positive exponential moment. Its Fourier transform is analytic in a strip and all derivatives at zero vanish. Analyticity and uniqueness of the Fourier transform imply that measure is zero. Thus polynomials are dense in L2(mu). Multiplication by g is unitary from this weighted space onto L2(dt/(2 pi)), because the nonzero analytic function g on the line is nonzero almost everywhere. This proves the assertion without RH.

As a result, for a fixed finite packet,

    R_m -> 0 in Hom(E,H), G_m -> 0 and W_m -> 0,
    while qR_m=sigma_Z and J_ZR_m=1 for every m.

This specifies why unscaled smallness of W_m cannot be used alone as weight control: its denominator G_m is also shrinking. The exact relative formula in section 3 must be retained.

The corrective map is the Hilbert/jet graph:

    closure{(F,J_ZF):F in B} = H plus E;
    closure{(Theta phi,0):phi in V} = H plus 0.

Indeed finite theta polynomials give every (h,0) in the closure, and the sequence (R_m u,u) gives (0,u). For a specified positive metric on E, completion in ||F||_2^2+||J_ZF||_E^2 is this graph closure, and the quotient by the boundary closure is E by [(h,u)]|->u. The added metric is retained supplied data, not an implied positivity theorem for the Weil pairing.

Its split observation is

    ((R_m u)^bullet,u^bullet) -> (e_H,u^bullet)

in the product of the stated support-fibre topologies. The arithmetic component survives above a supported Hilbert zero. External absence is (tau,tau).

## 7. Duality, trace and scope

The original residue map has matrix S with S*=-S and A*S+SA=S. Its pullback of the dual metric is

    G_m^D=S*G_m^-1 S,
    W_m^D=-S*G_m^-1 W_m G_m^-1 S.

Thus the upper-to-lower comparison is retained on the same arithmetic packet. The Weil pairing stays S J_g, with explicit metric comparison G_m^-1 S J_g. Its positivity is not imposed by choosing a positive Gram matrix.

All representative changes above are original theta boundaries. Their extension class j_h(h/(2 xi)) is unchanged; the induced finite cochain projectors differ by the homotopy (bJ_Z,0). The trace difference is zero because J_ZTheta=0. Degree-one and tensor Koszul signs remain those of the source complex. On a raw tensor metric, the inserted W_m terms give the copied allowance n epsilon_m; tensoring alone does not improve it.

The new results are the actual orthogonal source choice, rank-two boundary formula, exact relative certificate, rank-one source-kernel recurrence, arithmetic moment tail bound, and the full Hilbert/jet topology comparison. No uniform arithmetic purity estimate, global spectral-kernel vanishing, RH or GRH is asserted.

The thirteen finite exact tests check the encoded algebra and declared calibration models, not infinite analytic arguments or actual zeta zeros. The complete cochain-homotopy theorem remains the other session's result. Existing Lean modules and earlier validation receipts are untouched.

References: live PR #11 at the pinned head; the supplied Tau_Deligne_Control and Tau_Global_Comparison source notes; the supplied other-session homotopy proof and uncompiled draft; the previously retained Weil II 3.3.4-3.3.6 and 6.2 duality excerpts. Standard orthogonal-polynomial context is NIST DLMF 18.2; the density argument needed here is proved above for the actual arithmetic measure.
