# All arithmetic coefficient-image flags: a uniform exponential return estimate

19 September 2026. The coefficient image and its actual arithmetic pullback metric are those proved in Note 1. This calculation is not an identification with the native DNE/Gamma coefficient metric. It measures that distinction on every original fixed flag at once.

## 1. Full source constants and the exact common spaces

Retain the simple quartet, degree a=k+4, q=(a+1)^2, m=16a-48-v, and the original density mu=w_h^{*a}. The RTM/GTM source bounds, without changing its mass, have the form

    b_a (1+y^2)^(-25) sigma(y) <= mu(y) <= B_a sigma(y),
    log(B_a/b_a)=O_h(a+log a).

Here one literal choice, from the original GRA3 constants, is

    b_a=c_h vartheta_h^(a-3) exp[-(pi/2)(a-3)]
          /[C_Gamma 2^25 (a-2)^50],
    B_a=(C_h^tilt/c_Gamma) a^(9/2) M_(pi/2)^(a-1),
    vartheta_h=integral_(-1)^1 w_h,
    c_Gamma=sqrt(2)exp(-7/6),
    C_Gamma=sqrt(2sqrt(5))exp(2/3).

The positive c_h and C_h^tilt are the original TW7/BT12 lower-convolution and tilted-envelope constants. Their original defining estimates remain the inputs, with the full arithmetic amplitude and mass.

For a polynomial of degree at most D, the original Gamma multiplication estimate and Jensen give

    b_a[1+4(D+1)^2]^(-25)||P||_sigma^2
      <=||P||_mu^2<=B_a||P||_sigma^2.

Write K_(a,D)=(B_a/b_a)[1+4(D+1)^2]^25. Its logarithm is O_h(a+log(D+2)). These are the complete source constants already used in the preceding comparison; they are not assigned pointwise lower bounds for the zeta factor.

Set R=a sqrt(delta^2+gamma^2), Y=2^(-16)q, and d=floor(Y/16). Use the explicit eventual guards

    R<=Y/4, m+1<=Y/16, d>=1.

The original coefficient image is P_(m-1), and its multiplication-output image has degree at most m. The full relation space through the last endpoint is chi P_q.

## 2. Both complementary concentrations are exponentially bounded before minimization

For every F in chi P_q, the exact paired-root and shifted-Legendre estimate gives

    integral_(|y|<=Y) |F(c+iy)|^2 dmu
      <= eta_a ||F||_mu^2,

where

    eta_a=K_(a,2q) [sqrt(2pi)/c_Gamma]
      [(q+1)^2 sqrt(1+2q)/q] exp(pi q)100^q
      [(Y+R)/(q-R)]^(2q).                              (A1)

For the numerator use |chi(c+iy)|<=(Y+R)^q on the inner interval. The Legendre expansion bounds a degree-q polynomial there by (q+1)^2 100^q/q times its squared norm on [q,2q]. On that interval |chi|>=(q-R)^q and the full Gamma density is at least c_Gamma exp(-pi q)/sqrt(1+2q). The complete Gamma mass bounds the inner integral. Applying the two original source comparisons proves (A1). In particular

    eta_a <= exp[-(30log2-pi-log100)q+O_h(a+log q)].

For every P of degree at most m, apply Gamma multiplication d times. All intermediate degrees are at most m+d, and the stated guard gives 2(m+d+1)/Y<=1/3 eventually (enlarge only the finite guard, not the spaces). Consequently

    integral_(|y|>Y) |P(c+iy)|^2 dmu
      <= zeta_a ||P||_mu^2,
    zeta_a=K_(a,m) 3^(-2d).                             (A2)

The affine coordinate c is handled by replacing P(c+iy) with its actual y-polynomial; multiplication in (A2) is by y, so no factor c is inserted in its Gamma recurrence. Indeed the Gamma tail is bounded by Y^(-2d)||y^d P||_sigma^2 and the product of the recurrence bounds is at most [2(m+d+1)]^(2d). Returning its norm by the lower source inequality proves (A2).

The guard m+1<=Y/16 yields 2(m+d+1)/Y<=1/4, so the larger 1/3 used in (A2) is valid without a limiting approximation. Thus

    zeta_a=exp[-2d log3+O_h(a+log q)]
           <=exp[-(2^(-19)log3)q+O_h(a+log q)].

Split the original scalar product of P and a unit F in chi P_q at |y|=Y. Cauchy–Schwarz on the two regions gives

    |<F,P>_mu| <= (sqrt(eta_a)+sqrt(zeta_a)) ||P||_mu.

Taking the supremum over every unit F in the complete relation space proves

    ||Proj_(chi P_q) P||_mu^2 <= beta_a ||P||_mu^2,
    beta_a=(sqrt(eta_a)+sqrt(zeta_a))^2,
    beta_a=exp[-c_h q+O_h(a+log q)]                      (A3)

with any fixed 0<c_h<min(30log2-pi-log100,2^(-19)log3). There is no rowwise factor q and no omitted relation cross term in this projection estimate.

## 3. Every original arithmetic minimum on the image is stable

At N=q-1 the representative of a class P in P_m is exactly P. For q-1<=N<=2q its entire affine fibre is P+chi P_(N-q); the attained representative is P minus its orthogonal projection onto that full relation space. Equation (A3) therefore proves

    (1-beta_a)G_(q-1)|P_m <= G_N|P_m <=G_(q-1)|P_m.     (A4)

No comparison is made after dropping the source relations. For sufficiently large a, beta_a<1, so this is a relative bound on every direction, not merely an absolute norm estimate.

The same bound holds on the four-copy coefficient pullback

    G_(H,N)=M*diag(G_N,4)M

and on every fixed restriction and every attained quotient in the actual original B,S,W,J,I,K_c,K_i,T,W_i flags, when their metric is G_(H,N). Restriction substitutes the original columns in (A4). A quotient takes the two inequalities on every representative in its unchanged affine fibre and then minimizes. All fixed coordinate-frame factors cancel only in their own endpoint ratios.

For any such value form of dimension r, its actual four-endpoint return obeys

    0 <= logdet G_(X,q-1)+logdet G_(X,q)
          -logdet G_(X,2q-1)-logdet G_(X,2q)
       <= -2r log(1-beta_a).                            (A5)

To prove the sign, set l_N=logdet G_(X,N)-logdet G_(X,q-1). Monotonicity gives 0>=l_q>=l_(2q-1)>=l_(2q). The return is l_q-l_(2q-1)-l_(2q)>=0. Each high term is at least r log(1-beta_a), while l_q<=0, proving the upper bound.

Thus all these arithmetic coefficient-image returns are O_h(a exp[-c_h q+O_h(a+log q)]), since r<=4m=O(a). In particular every polynomial scale coefficient of these arithmetic returns is zero.

## 4. Both COB boundary metrics remain small relative to this original arithmetic metric

COB's exact identities are

    Gamma_0=M*diag(G_(q-1)-G_(2q-1),4)M,
    Gamma_1=M*diag(G_q-G_(2q),4)M.

Their positivity and injective proper-source interpretation remain the original COB results. Equation (A4) gives the new full-space inequalities

    0<Gamma_i<=beta_a G_(H,q-1), i=0,1.                 (A6)

The inverse comparisons consequently have eigenvalues at least beta_a^(-1). This does not estimate Gamma_0 relative to Gamma_1, and does not claim that an error small in G_(H,q-1) is small in the much smaller boundary metric. Note 2 gives the concrete negative relative trace eigenvalue that survives precisely this distinction.

For clarity, the native forms D_(j,N-v) and their four-copy restrictions are not G_(H,N). Their total native return has order a q, while (A5) is exponentially small. An identification of these two sequences would therefore contradict their displayed original returns. Their actual maps remain available for a metric comparison, but none is declared isometric here. In particular (A5) does not set the native absolute common kernel, proper-source scalar, or the seven native allocation terms to zero.
