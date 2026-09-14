# Arithmetic norm review and comparable-degree windows

The owner supplied the 2026-09-13 arithmetic endpoint note. Its principal input is the actual density w_h=|2xi/h|^2/(2pi), its k-fold convolution, and the unscaled monic squared norms omega_(h,k,j). This is a review and extension of that written proof, not a Lean certificate for zeta estimates or arithmetic integrals. The locally linked delivery archive was not accessible in this runtime; its reported test and manifest results are not counted as fresh executions.

## 1. Audit of the analytic steps

The Joukowski ellipse with |w|=8 has semiaxes 65/16 and 63/16. For f_T(z)=zeta(1/2+iT+iz), |T|>=10 keeps the pole outside its closure. Its image lies in the fixed real strip [-55/16,71/16], with imaginary magnitude between |T|-65/16 and |T|+65/16. Split that strip at Re(s)=1/4. Above this value, the fractional-part integral gives polynomial growth O((1+|T|)); below it the functional equation and vertical-strip gamma estimate give O((1+|T|)^(1/2-Re(s)+1)). The largest exponent is 79/16<6. Thus the claimed envelope M_T=C_0(1+|T|)^6 is sufficient, uniformly on the ellipse. Increase C_0 so M_T>=1.

The point z=-3i/2 corresponds to |w|=(3+sqrt(13))/2<4 and hence to zeta(2+iT). The reciprocal Dirichlet series gives modulus at least zeta(2)^(-1). The annular maximum principle gives m_T>=zeta(2)^(-3) M_T^(-2). Every closed unit disk centred on [-1,1] lies strictly within the ellipse: its surrounding rectangle [-2,2]x[-1,1] already satisfies the ellipse inequality. The maximum principle and Cauchy estimate therefore give sup|f_T'|<=M_T. At a maximizer use the longer one-sided interval in [-1,1], of length at least one; m_T/(2M_T)<=1/2. Integration gives m_T^3/(8M_T) and the stated exponent 42. The compact remaining T-range is handled by continuity and analytic nonvanishing on an interval. No nonvanishing on the critical line is assumed.

For the passage to |g/h|, use g=h(g/h) before taking absolute values. The polynomial upper bound on |h| avoids division at a selected zero. Gamma asymptotics yield the claimed interval-mass bound. One regularity detail should be explicit: w_h is bounded as well as integrable, by its continuous entire quotient on compact sets and exponential tail. Thus w_h*w_h is continuous, using L1 translation continuity against the bounded factor. Its integrand is positive almost everywhere, so the convolution is strictly positive everywhere. This justifies its positive minimum on [-1,1]. Restricting the remaining factors to that interval proves the note's lower envelope with the original factor vartheta_h^(k-3).

The monic Legendre norm on [-L,L] is exactly

    l_n(L)=2 L^(2n+1)/(2n+1) [2^n(n!)^2/(2n)!]^2.

The trial upper bound at degree j is (2j)! b^(-2j)(M_h(b)^k+M_h(-b)^k), for fixed 0<b<pi/2. Both are used on the original shifted line S=k/2+iu; multiplication by i^j has modulus one and does not change the leading coefficient norm. These arguments validate the supplied O_h(n) doubling-window result as a written theorem, not as a floating-point or Lean assertion.

## 2. Stronger, two-sided envelope

Write a=pi/2 and retain the lower-envelope constants c>0, vartheta>0, B=42+2 deg(h). Put

    t=min(1,vartheta), c0=min(1,2c/3),
    ell=(1/2) exp(-a) sqrt(c0 t) 2^(-B/2),
    M=max(1,M_h(b),M_h(-b)), U=4 sqrt(M)/b.

Then, for every n>=k>=3,

    (ell n)^(2n) <= omega_(h,k,n) <= (U n)^(2n).       (A)

Proof of the lower bound: l_n(n)>=(2/3)n^(2n)4^(-n); vartheta^(k-3)>=t^n; exp(-a(n+k-3))>=exp(-2an); (1+n+k-3)^(-B)>=(2n)^(-B)>=2^(-nB), since 2n<=2^n for integer n>=1; finally 2c/3>=c0^n. Multiply. For the upper bound use (2n)!<=(2n)^(2n), k<=n and M_h(b)^k+M_h(-b)^k<=2M^n, then 2<=4^n. This proves (A), retaining all masses in constants rather than resetting them.

For n>=k>=3 and n/2<=r<=2n, let m=n+r. From (A),

    (omega_m/omega_n)^(1/(2r))
       <= n U^(1+n/r) ell^(-n/r)(1+r/n)^(1+n/r)
       <= C_h n,
    C_h=27 max(1,U)^3 max(1,ell^(-1))^2.              (B)

This extends the doubling-window estimate to the overlapping windows needed by the volume theorem. Constants depend only on the fixed h and chosen b, not k,n,r. No monotonicity of the monic norms is assumed. The inequality is valid at r=n and at r=n+1 when n>=1.

References: NIST DLMF 25.4 (functional equation), 5.11.9 (uniform bounded-real-part gamma asymptotic), 18.3 (Legendre normalization). The general arguments above are written proofs; the present Lean contribution formalizes their finite norm-to-volume consequences, not their analytic hypotheses.
