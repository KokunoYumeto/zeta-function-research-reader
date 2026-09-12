# Convergent generating operators for the actual highest radial diagonals

## Source status and exact scope

This note proves a convergent reconstruction of the highest profile-order diagonal in the source radial jets. It does not replace the full source by that diagonal. The exact source is the OpenAI 166-page *Finite Time Blowup for Navier--Stokes*, SHA-256 `0e779481c4da40bd28d1e642e1d8ca57447d129610df28dfa5a11e9af8ae228f`. Pages 24--27, 35--36, 45--49, 57, 60--61 were read in the preceding full recurrence review; complete pages 144--147 were additionally read for this note. The current parent `29p_ns_finite_radial_recursion.tex` has SHA-256 `e2ac77ee6dd576a7b2849a5513f946bc2a120738d421332075359cb746f058a9`; its full proof was independently reviewed, with its sole final layout change verified by exact reconstruction of the previously reviewed hash. The source's full existence result remains imported.

The scalar kernel already occurs in the primary source: Appendix B, p.146, equation (B.11), defines

    f0(s) = sum_(j>=0) (-s/2)^j/[j!(j+1)!].

The Bessel notation and classical integral provenance are F. W. J. Olver and L. C. Maximon, *NIST Digital Library of Mathematical Functions*, Chapter 10, equations [10.2.2](https://dlmf.nist.gov/10.2#E2) and [10.9.1, 10.9.4](https://dlmf.nist.gov/10.9#E4), read on 2026-09-09. The latter section traces the real-line integral formulas to G. N. Watson, *A Treatise on the Theory of Bessel Functions*, 2nd edition, 1944, pp.19--21, 47--48, 68--71, 169--170, 175--180; those book pages were not read in this note, so this is an explicit secondary provenance pointer, not a claim of direct book verification. The integral and coefficient identities used below are also proved directly.

No source field, original viscosity, coordinate, cutoff or parameter is normalized away. No public record is changed.

## 1. Original physical axis data have a proved positive holomorphic radius

Retain the fixed source choices

    A=1/2+h, D=1/2-h, k=1+h, c=-A, lambda_n=2nh,
    0<h<1/100, nu>0,
    C>1, 0<j0<=1/20, sigma_*>0, Lambda>=1,
    tau=1-t, sigma=r^2/2, y=z/sqrt(nu),
    tau=q(1-eta^2), y=q^D eta, X=sigma/(nu q).

These constants have the original source dependencies. Put d=1-eta^2, L=1-2h eta^2,

    U(eta)=4eta+j0,
    H_*(eta)=D eta+d U(eta),
    zeta_*(eta)= -L H_* /(H_*^2+sigma_*^2),
    phi(eta)=exp(Lambda integral_0^eta zeta_*(v)dv).

The source selects the last function on a simply connected complex neighborhood, (B.1)--(B.3), pp.144--145. In particular its real values and holomorphic germ are fixed, not new choices. The exact physical axis data are

    w0(z,t)=sqrt(nu) q^(-A) U(eta),
    b1(z,t)=2 q^(-k) phi(eta)/C.                                  (1)

Here b1=partial_sigma <r u_theta>|axis. The viscosity factor cancels in b1 but not in w0. These are the source axis-data functions for q>0. Their identification with the complete localized field is made on the central preterminal slab where the final spatial and temporal cutoffs are identically one and the annular corrections vanish near the axis, exactly as in parent29p. No equality with the full field outside that slab is being asserted.

For completeness a local inverse and a positive radius can be constructed explicitly. Fix a real preterminal axis point (z0,t0), let tau0=1-t0>0, and denote its real parameter by eta0 in (-1,1). Define

    F(eta)=eta(1-eta^2)^(-D),
    z=sqrt(nu) tau^D F(eta), q=tau/(1-eta^2).                     (2)

All powers initially take their positive values on the real interval. Let S be the finite set consisting of +1, -1, the roots of L, and the roots of H_*^2+sigma_*^2. None is eta0. Choose

    delta0 = (1/4) min_(a in S) |eta0-a| >0.

On the eta disk of radius delta0, d has a holomorphic logarithm agreeing with its positive value at eta0, and the rational zeta_* has no pole. The source germ phi continues there by

    phi(eta0) exp(Lambda integral_(eta0)^eta zeta_*(v)dv).

This continuation agrees with the source germ by equality on their common neighborhood. It involves no change of the source real integral or amplitude.

Set a=F'(eta0)=L(eta0)d(eta0)^(-D-1)>0. The derivative is obtained by differentiating (2), not by treating q and eta as independent. One may use the explicit finite bound

    E=|eta0|+delta0,
    dmin=(1-eta0-delta0)(1+eta0-delta0)>0,
    M2=2E dmin^(-D-2)[(D+1)(1+2hE^2)+2h(1+E^2)],

because

    F''(eta)=2eta d^(-D-2)[(D+1)L-2h d]

and each factor has the indicated bound on that disk. Choose

    delta=min(delta0/2, a/[4(M2+1)]),
    R=sqrt(nu) tau0^D a delta/4.                                (3)

For |eta-eta0|<=delta, integration of F'' along the straight segment gives |F'(eta)/a-1|<=1/4. If |Y-F(eta0)|<a delta/4, the map

    T_Y(eta)=eta+(Y-F(eta))/a

has Lipschitz constant at most 1/4 and maps the closed delta disk into its interior: its displacement from eta0 is bounded by delta/4+delta/4. Iteration from eta0 converges uniformly at a geometric rate to its unique fixed point. The iterates are holomorphic in Y and their uniform limit is holomorphic. This proves the inverse eta(Y) with a positive explicit disk, without merely asserting an inverse map exists. Taking Y=z/(sqrt(nu)tau0^D) proves analyticity of q(z,t0), eta(z,t0), w0(z,t0), and b1(z,t0) on |z-z0|<R.

The same inverse eta(Y) also proves joint local analyticity in (z,t), since tau^D is holomorphic on a small complex neighborhood of tau0>0, and Y=z/(sqrt(nu)tau^D) remains in the same inverse disk on a smaller product neighborhood. Every real preterminal point of these axis-data functions therefore admits such a joint neighborhood. Uniform statements use a compact subdomain of these neighborhoods, not a radius asserted uniform up to t=1. The displayed physical radius retains sqrt(nu) tau0^D.

At the physical origin there is a simpler quantitative bound. Write x=z/(sqrt(nu)tau^D). For |x|<=1/8, the fixed-point map eta->x(1-eta^2)^D takes the closed disk |eta|<=1/4 into itself: its absolute value is at most sqrt(17)/32<1/4, and its derivative is at most (1/8)(1)(1/4)(16/15)=1/30. Uniform iteration from zero gives a holomorphic inverse for |x|<1/8. Consequently w0 is holomorphic for |z|<sqrt(nu)tau^D/8. For b1 choose epsilon=min(1/4,(1/4)min_(s in S)|s|). With |x|<=epsilon/2 the same map takes |eta|<=epsilon into itself and has derivative at most 8epsilon^2/15<=1/30; the pole-free source continuation for phi on this disk gives the explicit radius sqrt(nu)tau^D epsilon/2 for b1. All these bounds concern the actual fixed source parameters.

## 2. The generating kernels and their convergence proof

For a function f holomorphic in |z-z0|<R, define, when |z-z0|+|r|<R,

    H0[f](r,z)=(1/(2pi)) integral_0^(2pi) f(z+i r cos(theta))dtheta,
    H1[f](r,z)=(1/pi) integral_0^(2pi)
                          sin(theta)^2 f(z+i r cos(theta))dtheta. (4)

The second coefficient is 1/pi for integration from 0 to 2pi; the equivalent 0-to-pi formula has coefficient 2/pi. Both operators take the value f at r=0. They are holomorphic in (r,z), even in r, and thus holomorphic in sigma=r^2/2 near zero. For real z,r and a source germ real on the real interval, the values are real: pairing theta with pi-theta pairs conjugate arguments and equal real weights.

Here is the complete coefficient calculation. Let I_j=(2pi)^(-1) integral_0^(2pi)cos(theta)^(2j)dtheta. Integrating the derivative of sin(theta)cos(theta)^(2j-1) gives 2j I_j=(2j-1)I_(j-1), and I_0=1. Hence

    I_j=(2j)!/[4^j(j!)^2].

The weighted moment is

    (1/pi) integral sin(theta)^2 cos(theta)^(2j)dtheta
       =2(I_j-I_(j+1))=I_j/(j+1)
       =(2j)!/[4^j j!(j+1)!].

Every odd moment is zero by theta->theta+pi. Taylor expansion of f inside (4), followed by these finite moments, gives

    H0[f] = sum_(j>=0) alpha_j[f] sigma^j,
       alpha_j[f]=(-1)^j f^(2j)/(2^j(j!)^2),

    H1[f] = sum_(j>=0) beta_j[f] sigma^j,
       beta_j[f]=(-1)^j f^(2j)/(2^j j!(j+1)!).                   (5)

This is a convergent expansion. Indeed, choose |r|<a<R-|z-z0| and let M bound f on |Z-z|=a. Cauchy's formula gives |f^(2j)(z)|<=(2j)!M/a^(2j). Since binomial(2j,j)<=4^j, each term of H0 is bounded by M(|r|/a)^(2j), and each H1 term by M(|r|/a)^(2j)/(j+1). Thus both series converge absolutely and uniformly on smaller compact domains, with derivatives obtained using a slightly larger compact domain and Cauchy's formula. Taylor insertion into (4), every radial or axial differentiation below, and every physical time derivative of the actual jointly analytic inputs are justified this way.

In conventional Bessel notation, the proved operators are

    H0=J0(r partial_z),
    H1=2J1(r partial_z)/(r partial_z)=f0(sigma partial_z^2).      (6)

Equation (6) is defined by (4) or the convergent series (5). The apparent quotient in the middle is its removable entire power series; no inverse of partial_z is used. The last identity identifies exactly the scalar f0 in primary (B.11), including its argument and all constants. This is not an asserted bounded functional calculus on arbitrary smooth functions or a radius-semigroup assertion.

## 3. Exact PDEs, inverse maps and differential relations

Define the operators in the unchanged physical radial variable

    L0=2sigma partial_sigma^2+2partial_sigma+partial_z^2,
    L1=2sigma partial_sigma^2+4partial_sigma+partial_z^2,
    LB=2sigma partial_sigma^2+partial_z^2.

They are respectively partial_r^2+r^(-1)partial_r+partial_z^2, partial_r^2+3r^(-1)partial_r+partial_z^2, and partial_r^2-r^(-1)partial_r+partial_z^2 on r>0, with their regular sigma formulations at the axis. The factorial recurrences in (5) give, coefficient by coefficient,

    L0 H0[f]=0, L1 H1[f]=0, LB(sigma H1[f])=0.                  (7)

For example 2(j+1)^2 alpha_(j+1)[f]=-partial_z^2 alpha_j[f]; for H1 the factor is 2(j+1)(j+2). These equalities plus the established convergence prove (7) analytically, not just formally.

The exact dimension-raising and differential identities are

    partial_sigma(sigma H1[f])=H0[f],
    partial_sigma H0[f]=-(1/2)H1[f_zz],
    partial_r H0[f]=-(r/2)H1[f_zz].                             (8)

They follow immediately from alpha_j=(j+1)beta_j and the adjacent coefficient relation. Axial and physical temporal differentiation commute with each H operator on the common local analytic domain.

The maps H0 and H1 are linear bijections from holomorphic axis germs f to, respectively, solution germs holomorphic in (sigma,z) of L0 W=0 and L1 G=0: restriction to sigma=0 is the inverse. They are even in r, not necessarily even in sigma. Surjectivity and uniqueness follow because those PDEs determine the next sigma coefficient from the previous one by the same nonzero factorial divisors. The map f->sigma H1[f] is a linear bijection to holomorphic germs B with B(0,z)=0 and LB B=0, with inverse partial_sigma B(0,z). Their kernels are zero. No assertion about the whole smooth germ from an arbitrary Taylor sequence is used; these are explicitly holomorphic-germ maps.

These maps do not preserve ordinary pointwise multiplication. The exact discrepancy is already visible at f(z)=z: H0[z]=z but H0[z^2]=z^2-sigma. More generally the Laplacian of the product of two harmonic representatives is twice the scalar product of their gradients. If an algebra structure is desired on this range, its transported product is W[f] star W[g]=W[fg], with the just-proved axis inverse; it is not the ordinary product. This states the map and the lost ordinary multiplicative relation explicitly.

## 4. Selected source diagonals and their vector reconstruction

The all-order source result in parent29p gives

    z_beta=(d partial_eta+2beta eta)/L,
    partial_z(q^beta f(eta))=nu^(-1/2)q^(beta-D)z_beta f,

    u[j,j]=(-1)^j/(2^j(j!)^2)
                z_(c-(2j-1)D)...z_c U,
    phi[j,j]=(-1)^j/(2^j j!(j+1)!)
                z_(-k-(2j-1)D)...z_(-k) phi.

Combining the physical chain rules there with (1) and (5) proves the exact uncut generating expressions

    w_diag=H0[w0],
    g_diag=H1[b1],
    B_diag=sigma g_diag.                                        (9)

At each radial degree j, w_diag takes only profile order n=j from the two-index axial jet array. At radial degree j+1, B_diag takes only n=j from the angular array. This is the coefficient selection relation, not equality with the full actual velocity. Every lower profile-order contribution remains outside this selected diagonal, and the source's original cutoffs will be restored in Section 5.

The associated radial component is determined without another choice by incompressibility and regularity:

    R_diag=r u_r,diag=-integral_0^sigma partial_z w_diag(s,z)ds
                     =-sigma H1[w0_z],
    u_r,diag=-(r/2)H1[w0_z],
    u_theta,diag=(r/2)H1[b1], u_z,diag=H0[w0].                  (10)

The selected radial coefficient is exactly the highest n contribution of the original incompressibility formula: [sigma^(j+1)]R_diag=-(j+1)^(-1) partial_z alpha_j[w0]. This agrees with parent29p, including nu, because c-D=-1. In Cartesian coordinates x1=r cos(theta), x2=r sin(theta), the complete selected field is

    u_diag=(-x1 H1[w0_z]/2-x2 H1[b1]/2,
            -x2 H1[w0_z]/2+x1 H1[b1]/2,
             H0[w0]).                                          (11)

It is smooth across the physical axis and divergence-free. Every Cartesian component is harmonic: for any scalar G(sigma,z),

    Delta_(x1,x2,z)(x_i G)=x_i L1 G  (i=1,2),
    Delta_(x1,x2,z)W=L0 W.

These identities follow by two Cartesian derivatives and sigma=(x1^2+x2^2)/2. With (7) they prove Delta u_diag=0. The physical viscous term is consequently nu Delta u_diag=0 for this selected field. The dependence on nu has not disappeared from its values, from (1), or from its positive physical radius (3).

More explicitly define

    P[f]=(-x1 H1[f_z]/2,-x2 H1[f_z]/2,H0[f]),
    S[g]=(-x2 H1[g]/2,x1 H1[g]/2,0).

Then u_diag=P[w0]+S[b1], and direct differentiation using (8) gives

    div P[f]=div S[g]=0,
    curl P[f]=0,
    curl S[g]=P[g],
    curl u_diag=P[b1].                                         (12)

The map (f,g)->P[f]+S[g] is a linear bijection onto the axisymmetric, axis-regular, divergence-free, componentwise harmonic analytic vector-field germs. Its inverse is f=u_z|axis and g=(curl u)_z|axis=2lim_(r->0)u_theta/r. Indeed the axial and swirl harmonic equations force exactly the recurrences (5), and divergence together with axis regularity forces the radial integral (10); these prove both surjectivity and uniqueness. Thus the kernel is zero in this germ category and the complete differential map is explicit. This does not identify the source's full velocity with an irrotational or harmonic field.

## 5. Restore every original cutoff and calculate its defects

Let rho_0=1 and rho_j(z,t)=chi(c_j q(z,t)) for j>=1, exactly as in the original source. Define the **selected cutoff diagonals**

    W_rho[f]=sum_(j>=0)rho_j alpha_j[f]sigma^j,
    G_rho[f]=sum_(j>=0)rho_j beta_j[f]sigma^j,
    B_rho=sigma G_rho[b1].                                      (13)

For every preterminal point q>0 this sum is locally finite, since c_j increases geometrically and chi vanishes for arguments >=1. Thus it is a polynomial in sigma locally, with smooth physical parameter coefficients. No holomorphic continuation of the smooth chi in the complex-shift integrals is attempted. In general (13), not (4) with an invented complex cutoff, is the correct cutoff operator.

The actual highest-source summands are precisely (13); their inverse axis restrictions still recover f. The radial component must retain the original potential commutator:

    R_rho[f]=-integral_0^sigma partial_z W_rho[f](s,z)ds
       =-sum_(j>=0)partial_z(rho_j alpha_j[f])sigma^(j+1)/(j+1).

In the source variables the derivative of rho_j contributes exactly the following term to [sigma^(j+1)]R_rho:

    -nu^(-j)q^(lambda_j-j-1) (2eta/L) q rho_j'(q)u[j,j]/(j+1),

matching the negative term in (5.45) and parent29p. Axial differentiation is at fixed physical t; rho_j'(q) denotes its ordinary q derivative. No axial derivative is taken at fixed eta. The companion selected cutoff field, obtained from R_rho[w0], B_rho and W_rho[w0], is therefore still divergence-free.

All differential defects have finite explicit formulas. For a=0,1 put d_(0,j)=alpha_j and d_(1,j)=beta_j, and H_(0,rho)=W_rho, H_(1,rho)=G_rho. Then

    E_(a,rho)[f] := L_a H_(a,rho)[f]
      =sum_(j>=0) sigma^j [
          (rho_j-rho_(j+1)) partial_z^2 d_(a,j)[f]
          +2(partial_z rho_j) partial_z d_(a,j)[f]
          +(partial_z^2 rho_j)d_(a,j)[f] ].                     (14)

To prove (14), the radial operator sends the (j+1)-st term to -rho_(j+1)partial_z^2 d_(a,j)[f]sigma^j by the exact factorial recurrence; the axial operator differentiates rho_j d_(a,j)[f] twice, giving the remaining terms. Adjacent cutoff indices and their physical derivatives are both essential.

For physical time,

    partial_t H_(a,rho)[f]-H_(a,rho)[partial_t f]
      =sum_(j>=0)(partial_t rho_j)d_(a,j)[f]sigma^j,              (15)

and the analogous first axial commutator replaces t by z. Formulas (14)--(15) retain the entire local differential action; they are not estimates.

The identity partial_sigma(sigma G_rho[f])=W_rho[f] survives because rho_j is independent of sigma. Consequently the selected cutoff poloidal and swirl maps satisfy curl S_rho[g]=P_rho[g] when P_rho is constructed using R_rho, not by dropping derivatives of rho. Their further curl is

    curl P_rho[f]=-(1/r) integral_0^sigma E_(0,rho)[f](s,z)ds e_theta,

with its smooth axis extension. The vector Laplacian of S_rho[g] is (r/2)E_(1,rho)[g]e_theta, the axial Laplacian of P_rho[f] is E_(0,rho)[f], and its radial component is

    -(1/r) integral_0^sigma partial_z E_(0,rho)[f](s,z)ds.

These follow either by direct cylindrical differentiation or by differentiating the defining integral for R_rho. They specify exactly what the cutoffs change.

For each fixed J, q<(2c_J)^(-1) makes rho_0,...,rho_J equal one on an open neighborhood. Therefore the first J+1 selected coefficients in (13) agree with their convergent uncut counterparts, while the corresponding residual coefficients in (14) vanish for j<J. No positive neighborhood uniform in J is claimed.

There is also a quantitative local comparison. If |r|<R_C, f is bounded by M on the Cauchy circle of radius R_C, and M_rho=max(1,sup|chi|), then on a point where rho_0,...,rho_J=1,

    |H_(a,rho)[f]-H_a[f]|
       <=(1+M_rho) M (|r|/R_C)^(2J+2)/(1-(|r|/R_C)^2).         (16)

Here the subscript a on H is either 0 or 1. Formula (16) is the geometric tail estimate from (5), since only j>J contributes. It concerns the selected diagonal, not the missing lower profile-order array of the actual field.

## 6. Exact first comparison with the full source and its nonlinear equation

Let H(eta), R(eta) be the fully specified functions in parent29o. The actual second coefficient and its selected cutoff diagonal obey

    b2_actual=[q^(-2-h)H-rho_1 q^(-2+h)R]/(2nu C),
    b2_diag,rho=-rho_1 q^(-2+h)R/(2nu C),
    b2_actual-b2_diag,rho=q^(-2-h)H/(2nu C)<0.                   (17)

The strict sign is the previously proved exact expression

    H=phi[(h-3-j0 eta)/L-Lambda H_*^2/(H_*^2+sigma_*^2)].

Thus the first missing off-diagonal contribution is explicitly nonzero. The relation between selected and actual fields is not merely described verbally: their equal axis values, selected coefficients, and first coefficient difference are given by (1), (9), (13), (17).

The selected uncut field also has an exact full angular momentum residual. For f=w0 and g=b1, set W=H0[f], B=sigma H1[g], Rrad=-sigma H1[f_z]. Its full fluxes are P=Rrad B and Q=W B. Since partial_sigma Rrad+partial_z W=0 and LB B=0, the full angular residual is

    F_diag=partial_t B+partial_sigma P+partial_z Q-nu LB B
      =sigma[H1[g_t]-H1[f_z]H0[g]+H0[f]H1[g_z]].                (18)

No nonlinear flux was removed to obtain (18). At the axis its ordinary sigma coefficient is

    g_t-f_z g+f g_z=2q^(-2-h)H/C.                              (19)

The original source angular-force coefficient is exactly zero in its sufficiently late constant-cutoff region, whereas (19) is nonzero. The omitted term in (17) supplies the corresponding radial diffusion contribution in the full source. This is exact accounting for why convergence and harmonicity of the selected diagonal do not imply convergence, harmonicity or a new unforced equation for the complete source.

## 7. Nonclaims and next use

Independent helper `diagonal_kernel_check/DIAGONAL_KERNEL_CHECK.md`, SHA-256 `4aa934f3c84af5ffc2e261ab9736a69dbf678157d4d46b4e27ce6c1a9aae1d9f`, was read completely. Its independently derived integral constants, scalar PDEs, vector germ bijection, physical derivative factors and cutoff commutators agree with this proof; its 71 exact regressions are supplementary checks, not the all-order proof. That helper did not reread the original primary PDF; the complete primary reading cited above was performed by this note's author.

The selected diagonal is now a genuine locally convergent analytic function with explicit kernels, exact PDEs, inverse axis maps, original cutoff filters, commutators and full-source coefficient comparison. The construction gives no universal analytic radius at terminal time, no convergence of the uncut source correction series, no equality between a smooth field and its Taylor sequence, no harmonicity assertion for the full actual field, and no RH counterexample. Its relevance to the ongoing source-first calculation is that the all-order highest source coefficients are now represented by a proved analytic operator rather than only a sequence of formal expressions.
