# The absolute Gamma baseline and complete canonical action through order q

19 September 2026. New value calculation on the original fixed-packet domain, with complete multiplicity. This section evaluates the order-q term that was still left inside the absolute Gamma baseline even after the preceding arithmetic–Gamma correction had been evaluated. It does not evaluate the restriction to the observation kernel or the independent proper-source metric.

## 1. Definitions and result

Retain k=4l+1, e=1+k(m0-1), q=e(k+1)^2, c=k/2, the complete polynomial chi, and the exact density sigma(y)=|Gamma(1/4+iy/2)|^2/(2pi). Put Q(y)=i^(-q)chi(c+iy). Its roots, including repetitions, are

    omega_(a,b)=(2b-k)gamma-i(2a-k)delta.

Use the original EIQ probability density rho=rho_(2,pi), on [u^2,v^2], where uK(kappa)=2, vE(kappa)=4. Define

    F=F(2,pi), L=integral log(x)rho(x)dx,
    M_(-1)=integral rho(x)/x dx,
    C_B=9-8log2+F,
    C_sigma=F+6-(3/2)L-6log2+2log pi,
    eta_h=(gamma^2-delta^2)/3.

The new expansion is

    B_k[sigma]
      =C_B q^2+C_sigma q-2 eta_h M_(-1) k(k+2)+o_h(q).       (B1)

On the simple stratum the remainder in this statement is O_h(log q). At fixed higher multiplicity the displayed remainder is only claimed o(q); the explicitly retained k(k+2) term is not a claim that all other sub-q terms have been evaluated.

Combining (B1) with the preceding arithmetic–Gamma value gives

    B_k[m_k]
      =C_B q^2+[C_sigma-(4m0-2)C_Gamma]q
       +(log2/pi) I_h k^2-2 eta_h M_(-1) k(k+2)+o_h(q).      (B2)

The original CAI window and penalty calculation then yields

    J_k^action
      =C_B q^2+4q log q
       +[C_sigma+8log2-4-(4m0-2)C_Gamma]q
       +(log2/pi) I_h k^2-2 eta_h M_(-1) k(k+2)+o_h(q).      (B3)

The identities C_B=9-8log2+F and C_Gamma=2L-8log2+4 also give, by direct substitution,

    C_sigma=C_B-(3/4)C_Gamma+2log(pi/4),
    C_sigma+8log2-4-(4m0-2)C_Gamma
      =C_B-(4m0-5/4)C_Gamma+2log(4pi)-4.                 (B3a)

This is a stated algebraic identity between the constants in the displayed formulas, not a change of their source definitions.

The constants C_Gamma and I_h retain their preceding original-source definitions. The new result (B1) does not use the preceding arithmetic-tail theorem; (B2)–(B3) use that theorem at its stated written-proof status.

## 2. Exact source/relation bookkeeping

Let R_n(Q)=det[integral y^(i+j)|Q(y)|^2 sigma(y)dy]_(0<=i,j<n), with R_0=1. The original Schur identity gives exactly

    B_k[sigma]
      =log R_q(Q)+log R_(q+1)(Q)-log R_1(Q)
       -sum_(n=q)^(2q) c_(n-q) log gamma_n,
    c_0=c_q=1, c_r=2 otherwise,
    gamma_n=sqrt(2pi) Gamma(2n+1)/4^n.                    (B4)

This is the complete relation determinant, not the product of unminimized relation norms. Evenness makes its two parity blocks exact. The real-coordinate map P(S) -> P(c+iy), followed by its monic phase, has determinant of modulus one and carries chi P to i^q Q P. No coordinate mass is omitted.

## 3. A full-form localization for the positive-halfline ensembles

Set x=(y/q)^2. Fix a compact interval of potential parameters containing (2,pi), with alpha bounded below by a positive number. For each relevant parity block the polynomial degree is at most q/2+1, while the factor from Q has degree q in x.

Choose fixed 0<epsilon<1<2<M so small and so large, respectively, that the EIQ support lies strictly inside [epsilon,M]. All the following comparisons are performed before minimizing any polynomial norm.

On [0,epsilon], the shifted-Legendre expansion on [1,2] gives

    |P(x)|^2 <= poly(q) C^q integral_1^2 |P(t)|^2dt.

For the power weight, its integral there is bounded by a fixed polynomial in q times epsilon^(q-O(1)). For the original root weight, pair opposite roots and use |omega|<=k sqrt(delta^2+gamma^2). Since k/q -> 0, its normalized multiplier is bounded by (2epsilon)^q on that interval, eventually. The exact Gamma upper bound contributes only a polynomial in q and an integrable x^(-1/2) factor. On [1,2], the full weight is bounded below by exp(-C_h q) times a polynomial in q. Thus epsilon can be fixed so that the lower-tail quadratic form is at most exp(-c q) times the complete norm.

On [M,infinity), the same Legendre expansion gives

    |P(x)|^2 <= poly(q)[C(1+x)]^(q+2) integral_1^2 |P(t)|^2dt.

The full density has exponential factor exp[-(pi q/2)sqrt(x)]. Its remaining power is at most x^(2q+O(1)) times a fixed polynomial in q. Choose M large enough that 3log(1+x)-(pi/2)sqrt(x) is below a negative fixed multiple of sqrt(x) for x>=M. Direct integration of the resulting tail bounds its quadratic form by exp(-c q) times the [1,2] norm. Root factors are bounded above by (x+(R/q)^2)^q and below on [1,2] by the paired-root lower product; these add only the already retained constants.

Consequently the full and restricted Gram forms differ by a relative exp(-c q) bound, uniformly on all the polynomial spaces used in the two high relation determinants. Their logarithmic determinants differ by O(q exp(-c q)). Both tails, all roots and the complete minima have been retained in this comparison.

On [epsilon,M], the exact Gamma factor has the uniform expansion

    sigma(q sqrt(x))
       =sqrt(2) q^(-1/2) x^(-1/4)
         exp[-(pi q/2)sqrt(x)] [1+O(q^(-2))].             (B5)

The O(q^(-2)) bound follows by taking real parts of Stirling's expansion at 1/4+iq sqrt(x)/2. The first possible inverse-y term cancels in the modulus. A weaker O(q^(-1)) estimate would also suffice for (B1). The factor in (B5), including sqrt(2), is therefore returned through the complete forms with logarithmic determinant error O(q^(-1)).

## 4. The external one-cut theorem is applied on its actual domain

The primary analytic input is Borot–Guionnet, Asymptotic expansion of beta matrix models in the one-cut regime, arXiv:1107.1167v3, Proposition 1.2, equations (1-3)–(1-6), and Sections 4–5. Its integration interval may be a finite interval whose endpoints are strictly outside the equilibrium support. On [epsilon,M] the potentials V_(alpha,beta)(x)=beta sqrt(x)-alpha log x are holomorphic on a common complex neighborhood, confining on the compact interval, and have the EIQ single positive square-root density. EIQ proves the strict exterior inequality and positive endpoint coefficients. The displaced parameters below differ from (2,pi) by O(q^(-1)) and have full inverse-degree expansions. Thus the hypotheses are verified on the exact truncated interval; no analyticity through x=0 is asserted.

At beta-ensemble index 2, the coefficient of order n in the potential-dependent free energy is zero for a fixed potential. Dividing the paper's Gaussian partition function by the original n! gives

    log det Gram_(P_(n-1))[exp(-nV) dx]
       =n^2 F(V)+n log(2pi)+O(log n).                    (B6)

The leading coefficient agrees with the original negative EIQ minimum energy by the exact Vandermonde integral. For a fixed analytic factor exp(W), the one-point expansion and its contour integral give

    log det Gram[exp(-nV+W) dx]
       =n^2 F(V)+n log(2pi)+n integral W rho_V+O(log n).  (B7)

Equivalently, absorb -W/n into the permitted potential expansion. The n term is the variational derivative of the leading energy, with its sign fixed by the positive integral. The errors are uniform for the finitely many parameter sequences used here; EIQ endpoint smoothness, the fixed interval and the strict positive gap keep every contour and offcriticality bound uniform. The original unrestricted ensembles are restored by the full-form comparison in Section 3.

No arbitrary one-cut ansatz or generic period matrix is used. Charlier's independent Theorem 1.1 (arXiv:1706.03579) corroborates the coefficient n log(2pi)+n integral W rho for its stated real-line analytic domain; it is not applied in place of the finite-interval theorem above.

## 5. The complete root perturbation has an evaluated first moment

By the actual rectangular root sum,

    sum omega_(a,b)^2
       = q k(k+2)(gamma^2-delta^2)/3.                    (B8)

Opposite roots cancel every odd power. Uniformly on a complex neighborhood of [epsilon,M],

    log(|Q(q sqrt(x))|^2/[q^(2q) x^q])
       =-tau_k/x+O_h(k^4/q^3),
    tau_k=eta_h k(k+2)/q.                               (B9)

The notation on the left means its real-positive value on the interval, with the analytic logarithm continued from that value. This is well defined because every scaled root tends to zero outside the fixed neighborhood.

For simple multiplicity, k(k+2)=q-1, so tau_k=eta_h(1-1/q) and the error in (B9) is O_h(1/q). Replacing it by the fixed factor exp(-eta_h/x) costs O_h(1) in the high determinants. At fixed higher multiplicity tau_k ->0, and its whole logarithmic determinant contribution is O_h(k^2)=o(q). A uniform compact-factor application of (B7), or its exact first-variation integral with the one-point expansion, retains its displayed value -n tau_k M_(-1) up to o(q).

The fixed inverse moment is entirely determined by the original EIQ measure. With A=u^2, B=v^2, its one-dimensional endpoint integral is

    M_(-1)=(A+B)/(2AB)
       -(uv/4) integral_0^infinity
          (A+B+2s)/[sqrt(s)((A+s)(B+s))^(3/2)] ds.         (B10)

To obtain (B10), expand the EIQ Cauchy transform G(z)=integral rho(x)/(z-x)dx at z=0. In its Stieltjes representation, subtract 1/(uv) from 1/sqrt((A+s)(B+s)) before taking the limit. The remaining integral is absolutely convergent. One integration by parts gives the displayed expression. Since G(0)=-integral rho(x)/x dx, its sign is fixed, and M_(-1)>0 follows directly from the positive measure. This is not a new normalization of L or F.

The integral in (B10) also has a closed endpoint value. Indeed

    integral_0^infinity ds/[sqrt(s)sqrt((A+s)(B+s))]
       =2K(kappa)/v.

Apply -2(partial_A+partial_B) to this identity. The left side is the positive integral in (B10); differentiation of the defining elliptic integrals gives its value 2E(kappa)/(u^2 v). Since vE(kappa)=4 at the retained parameters,

    M_(-1)=(u^2+v^2-4uv)/(2u^2v^2).                     (B10a)

Every constant in (B1) is consequently given by the two original elliptic endpoints and elementary functions. Positivity of (B10a) is also certified by its original positive integral, not inferred from a numerical endpoint fit.

## 6. Expand both high determinants and every endpoint shift

Write q=2N. For a parity block of size n=N+s and starting exponent q+epsilon, where (s,epsilon) is one of (0,0),(1,0),(0,1), the exact coordinate powers from x=(y/q)^2 give

    log H_n^(q+epsilon)
      =[2(q+epsilon)n+2n^2-(3/2)n]log q +(n/2)log2
       +n^2 F((q+epsilon)/n,pi q/(2n))
       +n log(2pi)-(3/4)n L((q+epsilon)/n,pi q/(2n))
       -n tau_k M_(-1)((q+epsilon)/n,pi q/(2n))+o(q).       (B11)

For simple multiplicity the error here is O_h(log q). The high relation sum is exactly

    log R_q+log R_(q+1)
      =log H_N^q+log H_(N+1)^q+2log H_N^(q+1).            (B12)

The energy derivatives are the original F_alpha=L and F_beta=-6/pi at (2,pi). Hence

    n^2 F((q+epsilon)/n,pi q/(2n))
      =(q^2/4)F
       +q[s(F-L+3)+(epsilon/2)L]+O(1).                   (B13)

Across (B12), the sum of s is one and the weighted sum of epsilon is two. Thus the L terms in (B13) cancel, leaving q(F+3). The exact sum of the coordinate exponents in (B11) is 6q^2+3q+1/2. We obtain

    log R_q+log R_(q+1)
      =(6q^2+3q+1/2)log q+F q^2
       +q[F+3-(3/2)L+3log2+2log pi]
       -2 eta_h M_(-1) k(k+2)+o(q).                      (B14)

This keeps the q+1 relation rank, the parity increment q+1, the Gamma mass and the two endpoint weights separately until their sum is taken.

## 7. The low relation and the exact source product

The low relation determinant is a scalar. The same full root/Gamma comparison and Laplace/Stirling estimate give

    log R_1(Q)
      =2q log q+[4log2-2log pi-2]q+O_h(log q).             (B15)

For example its power comparison is exactly

    2sqrt(2) Gamma(2q+1/2)/(pi/2)^(2q+1/2).

The root multiplier at its y=O(q) saddle has bounded logarithm, and its complementary regions have the full exponential estimates already established. The empty relation determinant is still one.

For the source, the exact formula for gamma_n gives

    log gamma_n
      =2n log n-2n+(1/2)log n+(3/2)log2+log pi+O(1/n).

The original weights are the trapezoidal weights multiplied by two, so Euler summation, with its derivative remainder, gives

    sum_(n=q)^(2q) c_(n-q)log gamma_n
      =6q^2 log q+(8log2-9)q^2
       +q log q+[5log2+2log pi-1]q+O(log q).              (B16)

Substitution of (B14)–(B16) into (B4) cancels the q log q coefficient 3-2-1 exactly. The q coefficient is

    F+3-(3/2)L+3log2+2log pi
      -(4log2-2log pi-2)-(5log2+2log pi-1)
    =F+6-(3/2)L-6log2+2log pi.

This proves (B1).

## 8. Coefficients and the unchanged benchmark

ECL gives explicit endpoint expressions, with w=(u+v)/2, z=uv and cap=(v^2-u^2)/4:

    L=6log w-2log z-2,
    lambda=8-4log w-2log cap,
    F=-lambda/2-3+L.

Non-interval quadrature gives, as diagnostics only,

    C_B = 0.46008785145276085575482286909319848...,
    C_sigma = -0.51361602020653955823830889419104066...,
    M_(-1) = 0.50320199067867672571265901986969507....

On the simple stratum the full arithmetic order-q coefficient is

    C_sigma-2C_Gamma
      -(2/3)(gamma^2-delta^2)M_(-1)+(log2/pi)I_h.

At each fixed m0>=2 it is C_sigma-(4m0-2)C_Gamma. These are coefficients of the actual full baseline, not only its difference from a Gamma reference.

For the original benchmark L_(h,k)=delta q(k+1)/2, subtraction from (B3) gives

    J_k^action-4qlog L_(h,k)
      =C_Bq^2-4qlog(k+1)
       +[C_sigma+8log2-4-(4m0-2)C_Gamma-4log(delta/2)]q
       +(log2/pi)I_h k^2-2eta_hM_(-1)k(k+2)+o_h(q).        (B17)

The positive C_Bq^2 term is retained. The result therefore sharpens, rather than reverses, the computed obstruction in the canonical window. It does not evaluate the native observation-kernel restriction or the independent PRD relative return.
