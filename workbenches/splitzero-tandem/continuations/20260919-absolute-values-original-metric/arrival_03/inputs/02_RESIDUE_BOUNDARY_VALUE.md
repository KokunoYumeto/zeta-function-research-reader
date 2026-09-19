# A negative reflected-trace class in the original coefficient image

19 September 2026. This calculation uses the actual COB residue injection determined in 01_ORIGINAL_COEFFICIENT_IMAGE.md. It compares its reflected arithmetic trace to both original positive boundary forms. It does not substitute a finite packet trace for the full infinite Weil distribution.

## 1. An explicit admitted class

Retain a=4l+1, q=(a+1)^2, m=16a-48-v, c=a/2, with 0<delta<1/2, gamma>2 and v<=80. The root grid is

    lambda_(u,b)=c+(2u-a)delta+i(2b-a)gamma.

Set

    t0=pi/(2gamma), r0=t0 delta, c0=8 log 4-10>0,
    P_a(S)=sum_(j=0)^(4a) t0^(2j)(S-c)^(2j)/(2j)! .    (R1)

Its degree is 8a. For a>=17, 8a<=m-1, even at v=80. Hence P_a belongs to the exact image of the original L_a. Its actual coefficient preimage z_a is given by the Laurent-coefficient inverse in (F1)–(F2), not by a changed injection. In four copies use (z_a,0,0,0).

Write the original reflected trace on E as

    W(f,g)=sum_lambda conjugate(f(a-conjugate(lambda))) g(lambda).

Since P_a has real even coefficients in S-c, P_a^sharp=P_a. Therefore W(P_a,P_a)=sum_lambda P_a(lambda)^2; the full grid is conjugation-stable, so this sum is real.

## 2. Evaluate the sign and its exact leading value

For every grid point z=lambda-c,

    cosh(t0 z)=i sin(pi(2b-a)/2) sinh(r0(2u-a)).

The sine is +1 or -1 because a is odd. Thus the full function is purely imaginary at every grid point, and none of these values is zero.

Moreover t0|z|<2a. The Taylor tail satisfies

    |P_a(c+z)-cosh(t0 z)|
       <= exp(2a)(2a)^(8a+1)/(8a+1)!
       <= exp(-c0 a) =: epsilon_a.                      (R2)

For the last inequality use n!>=(n/e)^n and n=8a+1. The bound t0 sqrt(delta^2+gamma^2)<2 follows from delta/gamma<1/4 and pi<22/7.

On the explicit eventual guard epsilon_a<=r0/4, this is at most one quarter of every |sinh(r0(2u-a))|. If F=i s with real s and |P-F|<=|s|/4, direct expansion gives Re(P^2)<=-7s^2/16. Summing proves

    W(P_a,P_a)
     <= -(7/32)(a+1) [sinh(2r0(a+1))/sinh(2r0)-(a+1)]
     <0.                                                (R3)

The bracket is positive since it equals 2 sum_(u=0)^a sinh^2(r0(2u-a)). No uncomputed sign remains.

In fact the exact comparison function has trace

    sum_lambda cosh(t0(lambda-c))^2
     = -(a+1)/2 [sinh(2r0(a+1))/sinh(2r0)-(a+1)].        (R4)

The finite geometric sum proves (R4). The difference of (R4) and the polynomial trace is bounded by

    2 epsilon_a (a+1) sum_(u=0)^a |sinh(r0(2u-a))|
       +q epsilon_a^2.

This is relatively O_(delta,gamma)(a exp(-(c0+r0)a)). Consequently

    W(P_a,P_a)
      = -(a+1) exp(2r0(a+1))/(4 sinh(2r0)) [1+o(1)].    (R5)

This is a new explicit class in the existing coefficient image. It is not the terminal eigenvector: (F3) proves that the terminal eigenvector does not belong to that image. The distinction is made by the actual polynomial and its inverse coefficient map.

## 3. Keep the original arithmetic source mass

Let dmu_a=w_h^{*a}(y)dy and M_h(theta)=integral exp(theta y)w_h(y)dy. The measure is even and has its original full mass M_h(0)^a. On the original integration line,

    |P_a(c+iy)| <= cosh(t0 |y|) <= exp(t0 |y|).

Since 2t0=pi/gamma<pi/2=alpha,

    ||P_a||_(mu_a)^2 <= 2 M_h(2t0)^a.                  (R6)

Set theta1=(alpha-2t0)/2>0 and theta2=2t0+theta1<alpha. For every Y>0 the complete tail satisfies

    integral_(|y|>Y) |P_a(c+iy)|^2 dmu_a
       <= 2 exp(-theta1 Y) M_h(theta2)^a.              (R7)

Both follow from the exact convolution transform M_(mu_a)(theta)=M_h(theta)^a. There is no probability renormalization of the source.

## 4. The two actual boundary energies are exponentially small

Let Y=2^(-16)q, R=a sqrt(delta^2+gamma^2), and retain the original eventual root guard R<=Y/4. Let L_a^-,L_a^+ be the original full-polynomial comparisons with sigma through degree 2q:

    ||F||_(mu_a)^2 >= L_a^- ||F||_sigma^2,
    dmu_a <= L_a^+ dsigma,
    log(L_a^+/L_a^-)=O_h(a+log q).

The complete shifted-Legendre estimate on [q,2q], including its original Gamma mass, gives for every Q=chi P with deg P<=q

    integral_(|y|<=Y) |Q(c+iy)|^2 dmu_a
       <= eta_a ||Q||_(mu_a)^2,                        (R8)

where a valid explicit bound is

    eta_a = (L_a^+/L_a^-)(sqrt(2pi)/c_Gamma)
       ((q+1)^2 sqrt(1+2q)/q)
       exp(pi q) 100^q [(Y+R)/(q-R)]^(2q).

One may replace eta_a by min(1,eta_a). It includes all original root factors and the full source mass. Under the guard, the last ratio is at most 2^(-15), so

    log eta_a <= -c1 q+O_h(a+log q),
    c1=30 log 2-pi-log 100>0.                           (R9)

The source itself supplies the same style of uniform estimate before minimization; the displayed proof uses the actual degree q relation space, not its diagonal trial norms.

For any unit vector f in either complete boundary relation band, splitting its pairing with P_a at Y gives

    |<f,P_a>| <= sqrt(eta_a)||P_a|| + ||1_(|y|>Y)P_a||.

The exact COB orthogonal projection formulas are

    Delta_0 P_a = -Proj_span(e_0,...,e_(q-1)) P_a,
    Delta_1 P_a = -Proj_span(e_1,...,e_q) P_a.

They retain both original windows. Taking the supremum over unit vectors in those bands, then using (R6)–(R7), proves, for i=0,1,

    0< z_a* Gamma_i z_a
       <= 4 eta_a M_h(2t0)^a
          +4 exp(-theta1 2^(-16)q) M_h(theta2)^a.       (R10)

No factor equal to the number of rows is charged: the estimate applies to every unit vector of the whole band. Strict positivity follows from the original injectivity of Delta_i L_a.

## 5. The residue-versus-boundary discrepancy has an evaluated value

On the same coefficient input define exactly

    D_i = Gamma_i - L_a* W L_a

in one copy, or its four-copy version. Combining (R5) and (R10) gives

    z_a* D_i z_a
       = (a+1) exp(2r0(a+1))/(4 sinh(2r0)) [1+o_h(1)],

and therefore

    lim_(a->infinity) z_a*D_i z_a / [a exp(pi delta a/gamma)]
      = exp(pi delta/gamma)/(4 sinh(pi delta/gamma)),   (R11)

for both original windows, along the admitted odd subsequence and original guards.

The fixed arithmetic unit is retained through the original theta injection and its source density; the finite trace is the original reflected trace in those packet coordinates. The full tensor-residue factorization remains W(f,g)=B(f,a_tr g)+W_Z(f,g). Formula (R3) concerns their sum and does not remove W_Z or assign its value separately.

Thus the positive boundary metric is not the reflected trace on this actual coefficient image, with a discrepancy evaluated on an explicit input. This is a calculation about those two specified forms and their specified map. It is not a claim excluding other arithmetic realizations or a proof of positivity/nonpositivity of the full infinite Weil form.

## 6. Relative spectrum in the actual boundary metric

Keep the exact finite lower bound N_a for -W(P_a,P_a) from (R3), and write the two-term right side of the boundary-energy estimate (R10) as B_a. Both are positive on the displayed guards. On the original coefficient domain put

    T_i=Gamma_i^(-1/2) L_a* W L_a Gamma_i^(-1/2).

For four copies use the corresponding one-copy vector and blocks. This is a Hermitian matrix because the original reflected trace is Hermitian. The Rayleigh quotient of the actual coefficient vector z_a gives

    lambda_min(T_i) <= -N_a/B_a <0,
    ||I-T_i|| >= 1+N_a/B_a,   i=0,1.                    (R12)

Thus the relative operator, not only an unweighted trace, has an explicitly negative eigenvalue. The norm bound is measured in the original Gamma_i boundary metric.

Let epsilon_*=2^(-16) and

    c_*=min(30 log 2-pi-log 100, theta_1 epsilon_*)>0,
    theta_1=(pi/2-pi/gamma)/2.

The earlier full-source constants give

    log B_a <= -c_* q+O_h(a+log q),
    log N_a=2r_0 a+log a+O_h(1).

Consequently

    liminf_(a->infinity) q^(-1) log(-lambda_min(T_i)) >= c_*>0.       (R13)

The negative eigenvalue in this statement is ensured by (R12). No sign is assigned to an unrelated native metric. This completes an actual relative-metric consequence of the residue/trace factorization on an explicit vector in the original COB coefficient image. It shows quantitatively why positivity of the boundary norm cannot be transported to that trace form by an omitted small correction.
