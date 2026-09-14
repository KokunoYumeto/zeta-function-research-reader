# Balanced arithmetic norm windows and the strengthened endpoint threshold

This is a written analytic extension of the supplied arithmetic endpoint note, not a Lean certificate or a numerical enclosure. The fixed packet, original source, Taylor unit, measure and total mass are unchanged. It is intended for the next integration cut, not the already frozen E publication.

## Original measure and constants

Fix a monic finite divisor h of g=2xi, removing its selected zeros with their full orders, and put d=deg h. On the original line S=k/2+iu, use

    w_h(t)=|(g/h)(1/2+it)|^2/(2pi), m_(h,k)=w_h^{*k},
    omega_(h,k,j)=inf_(P monic, degree j) integral |P(k/2+iu)|^2 m_(h,k)(u) du.

The mass is mu_h^k, not one. The original note proves, for a=pi/2 and B=42+2d,

    m_(h,k)(u) >= c_h vartheta_h^(k-3)
       exp[-a(|u|+k-3)] (1+|u|+k-3)^(-B),  k>=3,

where c_h=b_h c_h^(1)>0, b_h=min_(|v|<=1)(w_h*w_h)(v)>0, and vartheta_h=integral_[-1,1] w_h>0. Fix 0<b<a and retain both actual finite exponential moments M_+=integral exp(bt)w_h(t)dt and M_-=integral exp(-bt)w_h(t)dt. Define X=max(1,M_+,M_-) and K=max(1,vartheta_h^(-1)). None of these definitions normalizes the source.

## Exact preceding estimate

The monic Lebesgue minimum, allowing any leading coefficient of modulus one, is

    ell_n(L) = [2 L^(2n+1)/(2n+1)] [2^n (n!)^2/(2n)!]^2.

This includes the original leading phase i^n under S=k/2+iu. For integers n>=0, r>=1, k>=3 and any L>0, the trial-monomial exponential upper bound and interval Legendre lower bound give

    A_(h,k,n,r) := (omega_(h,k,n+r)/omega_(h,k,n))^(1/(2r))
      <= [(2(n+r))! b^(-2(n+r)) (M_+^k+M_-^k)
           exp[a(L+k-3)] (1+L+k-3)^B
           / (c_h vartheta_h^(k-3) ell_n(L))]^(1/(2r)).       (BW1)

For the balanced-window theorem take integers n>=k>=3 and n/2<=r<=n, and set L=n. Then

    A_(h,k,n,r) <= Cbal_h n,                              (BW2)
    Cbal_h = 256 exp(pi) max(1,3/c_h) X K
                max(1,b^(-3)) 6^(B/3).                  (BW3)

### Proof of the uniform constant

The central-binomial bound gives ell_n(n)>=2 n^(2n+1)/[(2n+1)4^n]. Also (2(n+r))!<=(4n)^(2(n+r)) and M_+^k+M_-^k<=2X^k. Combining these before taking roots cancels the factor two. The factorial, Legendre and c_h factors after the 2r-th root are at most

    n * 4 * 8^(n/r) * [(2n+1)/(c_h n)]^(1/(2r))
      <= 256 n max(1,3/c_h).

Here n/r<=2, (2n+1)/n<=3, and 0<1/(2r)<=1. The remaining factors obey

    X^(k/(2r)) <= X,
    vartheta_h^(-(k-3)/(2r)) <= K,
    b^(-(n+r)/r) <= max(1,b^(-3)),
    exp[a(n+k-3)/(2r)] <= exp(2a)=exp(pi).

Finally 1+n+k-3<=2n and 2r>=n. The function log(2x)/x decreases for x>=3, since its derivative is [1-log(2x)]/x^2<0. Hence

    (1+n+k-3)^(B/(2r)) <= (2n)^(B/n) <= 6^(B/3).

Multiplication proves BW2-BW3. This proof works for the original arithmetic density without an evenness hypothesis. The constants depend on fixed h and b only, never n,k,r.

## Composition with the exact consecutive-window product

This paragraph assumes the separately reviewed exact-window theorem for the original canonical quotient family, including its nonnegative contractions and zero-contraction cases. Write V_N=det G_N>0 and Lambda_N=omega_N/V_N. Its simple product corollary is

    min_(n<=N<n+r) epsilon_N
       <= (Lambda_(n+r)/Lambda_n)^(1/(2r))
       = A_(h,k,n,r) (V_n/V_(n+r))^(1/(2r)).              (BW4)

Do not infer BW4 from BW1 alone. It uses the original rank-two Toda identities and the retained source/quotient maps. If every allowance on the window has the exterior lower bound L_(h,k), BW2-BW4 imply

    log(V_n/V_(n+r)) >= 2r log[L_(h,k)/(Cbal_h n)].        (BW5)

This holds even if the right side is negative; canonical volume monotonicity independently gives a nonnegative left side.

For the packet consisting exactly of the hypothetical off-line quartet 1/2 +/- delta +/- i gamma, with fixed delta,gamma>0 and common multiplicity m>=1, retain

    q=q_k=[1+k(m-1)](k+1)^2,
    L_(h,k)=2delta[1+k(m-1)](k+1)floor((k+1)^2/4),
    q>=k>=3, L_(h,k)/q>=delta k/2.

Take n=q and r=q-1. Since q>=3, q/2<=q-1<=q; the degrees q,...,2q-2 are admitted and the norm endpoint is 2q-1, not 2q. Define the central two-volume cost

    C_k=log(V_q/V_(2q-1)).

Then

    C_k >= 2(q-1) log[delta k/(2 Cbal_h)].                 (BW6)

Canonical monotonicity gives V_(q-1)>=V_q and V_(2q-1)>=V_(2q). Consequently each outer cost dominates this same central cost:

    log(V_(q-1)/V_(2q-1)) >= C_k,
    log(V_q/V_(2q)) >= C_k.

For the original four-volume budget B_k=log[V_(q-1)V_q/(V_(2q-1)V_(2q))],

    B_k >= 2 C_k >= 4(q-1) log[delta k/(2 Cbal_h)],
    liminf_(k->infinity) B_k/(q_k log k) >= 4.            (BW7)

Indeed q_k>= (k+1)^2 tends to infinity, so (q_k-1)/q_k tends to one; fixed positive delta/(2Cbal_h) contributes only O_h(q_k). The diagonal choice r=q also yields log(V_q/V_(2q))>=2q log[delta k/(2Cbal_h)], but the overlapping shorter window proves the stronger four-volume threshold.

The supplied note's older threshold 2 remains correct under its weaker sinh endpoint estimate. BW7 is a strengthened synthesis using BW4, not a correction to that valid implication. No upper estimate on B_k or C_k follows. A separately proved limsup B_k/(q_k log k)<4 would contradict this quartet; no such upper estimate and no RH proof is asserted here.

## Reference and evidence boundary

The analytic ingredients are the zeta reflection formula ([DLMF 25.4.2](https://dlmf.nist.gov/25.4.E2)), the gamma vertical-strip estimate, uniform for bounded real part ([DLMF 5.11.9](https://dlmf.nist.gov/5.11.E9)), and the Legendre orthogonality/leading coefficient ([DLMF 18.3](https://dlmf.nist.gov/18.3)). The annulus propagation, convolution restriction, BW1-BW3 and BW5-BW7 are written derivations. Finite regression checks support algebraic fixtures only, not the analytic quantifiers or arithmetic zero hypotheses.
