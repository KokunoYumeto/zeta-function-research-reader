# The original cutoff profile: exact coordinate, convergent endpoint correction, and certified half-volume position

This calculation receives the cutoff function in CP3–CP8 of the supplied continuation. It preserves its original cutoff variable \(t=j/q\), the physical coordinate, every original coefficient metric and every invariant row. The new variable below is a coordinate for the scalar elliptic equation only. No source metric is changed.

## EP1. The original scalar and its exact coordinate map

For a modulus \(0le a<1\), use the complete integrals

\[
 K(a)=\int_0^{\pi/2}(1-a^2\sin^2\theta)^{-1/2}d\theta,
 \qquad E(a)=\int_0^{\pi/2}(1-a^2\sin^2\theta)^{1/2}d\theta.
 \tag{EP1}
\]

The original profile has \(r=r_t\in(0,1)\), \(\kappa=\sqrt{1-r^2}\), and

\[
 1+t=\frac{E(\kappa)}{rK(\kappa)},\qquad
 J(t)=t\log\frac{1+r}{1-r}+2\log\frac{(1+r)K(\kappa)}\pi.
 \tag{EP2}
\]

Its alternative expression in CP3 follows by substituting its first equation; thus no independent constant is being fixed. Set

\[
 w=\frac{1-r}{1+r},\quad \mu=w^2,\quad
 r=\frac{1-\sqrt\mu}{1+\sqrt\mu},\quad
 \kappa=\frac{2\sqrt w}{1+w},\quad
 k(\mu)=\frac{2K(\sqrt\mu)}\pi,
 \quad e(\mu)=\frac{2E(\sqrt\mu)}\pi.
 \tag{EP3}
\]

These formulas give mutually inverse maps between \(0<r<1\) and \(0<\mu<1\), preserving the positive square-root branch. The descending Landen formulas are

\[
 K(\kappa)=(1+w)K(w),\qquad
 E(\kappa)=\frac{2E(w)-(1-w^2)K(w)}{1+w}.
 \tag{EP4}
\]

These classical formulas are cited to B. C. Carlson, [DLMF19.8.12a–b](https://dlmf.nist.gov/19.8.E12). The original equation TeX was obtained and read in full for this calculation. We also give a proof so that the exact parameter and branch in use can be checked.

Expanding the integrand in EP1 on compact subdisks and integrating powers of sine gives

\[
 k(\mu)=\sum_{n\ge0}c_n\mu^n,\qquad
 e(\mu)=1-\sum_{n\ge1}\frac{c_n\mu^n}{2n-1},\qquad
 c_n=\frac{\binom{2n}{n}^2}{16^n}.
 \tag{EP5}
\]

The integral of \(\sin^{2n}\theta\) equals \(\pi\binom{2n}{n}/2^{2n+1}\), by integration by parts starting at \(n=0\). The binomial coefficients therefore give exactly EP5, with radius of convergence one. The second binomial series gives its stated factor \(1/(2n-1)\). These are also [Carlson's DLMF19.5.1–2](https://dlmf.nist.gov/19.5), whose original equation TeX is retained.

Their coefficient recurrence, or differentiation of EP1 followed by integration by parts, gives

\[
 \frac{d}{dz}K(\sqrt z)=\frac{E(\sqrt z)/(1-z)-K(\sqrt z)}{2z},\quad
 \frac{d}{dz}E(\sqrt z)=\frac{E(\sqrt z)-K(\sqrt z)}{2z}.
 \tag{EP6}
\]

Let \(z=4w/(1+w)^2\) and \(F(w)=K(\sqrt z)/(1+w)\). Applying EP6 twice yields

\[
 w(1-w^2)F''+(1-3w^2)F'-wF=0.
 \tag{EP7}
\]

This identity follows by the quotient and chain rules; `check_profile_scalar.py` independently verifies both rational coefficients multiplying \(K(\sqrt z)\) and \(E(\sqrt z)\) vanish. For an analytic series \(F=\sum a_nw^n\), EP7 gives \(a_1=0\) and \(n^2a_n=(n-1)^2a_{n-2}\) for \(n\ge2\). Since \(F(0)=\pi/2\), its unique analytic solution is \(K(w)\), by EP5. This proves the first EP4 near zero and then on the whole real interval by uniqueness for the ordinary differential equation away from zero. The identity \(E(w)=(1-w^2)[wK'(w)+K(w)]\), from EP6, proves the second EP4 after substituting the first. Every branch is the real positive one fixed in EP1.

Substitution into EP2 proves the exact original-profile representation

\[
 \boxed{t=T(\mu)=2\left[\frac{e(\mu)}{(1-\mu)k(\mu)}-1\right]
       =4\mu\frac{k'(\mu)}{k(\mu)},\qquad
 J(t)=-\frac t2\log\mu+2\log k(\mu).}
 \tag{EP8}
\]

The second equality for \(T\) is EP6 with its factors of two retained. In particular \(t\) is still the original cutoff fraction, not a rescaled fraction. Returning through EP3 reproduces EP2 exactly.

## EP2. Unique inverse, derivatives and the positive series distribution

For each \(0<\mu<1\), define a probability on the nonnegative integers by

\[
 p_n(\mu)=\frac{c_n\mu^n}{k(\mu)}.
 \tag{EP9}
\]

Every mass is positive, their sum is one, and their moments of every order converge on compact subintervals of \(0<\mu<1\). Termwise differentiation is justified there by absolute convergence. It gives

\[
 T(\mu)=4\mathbb E_\mu n,\qquad
 \mu T'(\mu)=4\operatorname{Var}_\mu(n)>0.
 \tag{EP10}
\]

The variance is strictly positive since both masses at zero and one are positive. This proves strict increase without subtracting nearby elliptic quantities. At zero, EP5 gives \(T(\mu)=\mu+O(\mu^2)\). At one, the defining integral makes \(k(\mu)\to\infty\): monotone convergence gives the divergent integral of \(1/\cos\theta\). For any fixed integer \(L\), \(\sum_{n<L}p_n\to0\), because its numerator stays bounded while \(k\to\infty\). Therefore \(\liminf\mathbb E n\ge L\), and \(L\) is arbitrary. Thus \(T\to\infty\). EP8 has a unique inverse \(\mu(t)\in(0,1)\) for every \(t>0\), and this is the same \(r_t\) as EP2.

Differentiating EP8 while keeping \(t=T(\mu)\), the two terms \(-t/(2\mu)\) and \(2k'/k\) cancel exactly. It follows that

\[
 \boxed{f(t):=J'(t)=-\tfrac12\log\mu(t)
 =\log\frac{1+r_t}{1-r_t}>0,\qquad
 J''(t)=-\frac1{2\mu T'(\mu)}
       =-\frac1{8\operatorname{Var}_\mu(n)}<0.}
 \tag{EP11}
\]

The integer distribution is an auxiliary exact representation of the elliptic derivatives, with its connecting map EP8–EP10 proved above. It does not replace the arithmetic spectral measure. In particular \(J\) is increasing and strictly concave. EP8 at \(\mu\downarrow0\) gives \(J(0)=0\). For \(0\le x\le y\\), the decreasing derivative implies

\[
 0\le J(y)-J(x)\le J(y-x).
 \tag{EP12}
\]

The endpoint derivative is integrable by the expansion proved next. EP12 supplies the actual modulus of continuity used in PP35–PP37, including intervals meeting the first cutoff.

## EP3. A convergent correction after the logarithmic term

EP5 gives the convergent series

\[
 T(\mu)=\mu+\frac78\mu^2+\frac{13}{16}\mu^3
 +\frac{791}{1024}\mu^4+\frac{1523}{2048}\mu^5+O(\mu^6).
 \tag{EP13}
\]

The function is holomorphic in a neighborhood of zero and \(T'(0)=1\). The analytic inverse theorem therefore gives a convergent power series there, not only a formal asymptotic. Coefficient substitution into EP13 gives

\[
 \mu(t)=t-\frac78t^2+\frac{23}{32}t^3
 -\frac{581}{1024}t^4+\frac{1783}{4096}t^5+O(t^6).
 \tag{EP14}
\]

For completeness, local invertibility here can also be obtained by writing \(T(\mu)=\mu+\mu^2g(\mu)\): on sufficiently small disks the equation \(\mu=t-\mu^2g(\mu)\) is a uniform contraction, whose analytic iterates converge to the inverse. Thus \(\mu(t)/t\) is analytic and equals one at zero. Its logarithm with value zero at zero is analytic on a smaller disk. Substituting EP14 into the convergent logarithm series proves

\[
 f(t)=-\frac12\log t+\frac7{16}t-\frac{43}{256}t^2
 +\frac{497}{6144}t^3-\frac{1381}{32768}t^4+O(t^5).
 \tag{EP15}
\]

All coefficients are rational. The companion checker obtains them from finite rational polynomial operations, and checks the inverse relation through degree five. Taylor's theorem for the analytic correction gives the displayed remainder. Integrating from zero, using \(J(0)=0\), gives

\[
 \boxed{J(t)=\frac t2(1-\log t)+\frac7{32}t^2-\frac{43}{768}t^3
 +\frac{497}{24576}t^4-\frac{1381}{163840}t^5+O(t^6).}
 \tag{EP16}
\]

The difference \(J(t)-t(1-\log t)/2\) is a convergent analytic series at zero. This strengthens the first supplied response's remainder \(O(t^{5/2})\) and preserves its coefficient \(7/32\). It also proves \(J(h)=O(h\log(C/h))\) used to quantify the complete-jet cutoff error. No microscopic finite-\(k\) determinant coefficient is obtained by differentiating an \(o(kq)\) error.

## EP4. Independent outward intervals and the half-volume cutoff

The independent checker uses intervals with integer endpoints divided by \(10^{90}\). Each addition, subtraction, multiplication and division rounds outward with integer floor and ceiling; its square root uses integer square roots. For EP5 truncated after degree \(N\), the positive \(k\) tail is bounded by the next term divided by \(1-\mu\), since \(c_{n+1}/c_n=((2n+1)/(2n+2))^2<1\). The magnitude of the \(e\) tail is bounded by this same bound divided by \(2N+1\). All bisection points lie between \(1/20\) and \(13/20\); \(N=512\) suffices for the reported intervals. Monotonicity EP10 makes the certified signs decisive.

For \(x\ge1\), use \(z=(x-1)/(x+1)\) and

\[
 \log x=2\sum_{j=0}^{L-1}\frac{z^{2j+1}}{2j+1}+R_L,
 \qquad 0\le R_L\le\frac{2z^{2L+1}}{(2L+1)(1-z^2)}.
 \tag{EP17}
\]

Integrating the geometric series proves this exact remainder. The code uses \(L=1024\) for \(x=1/\mu\) and \(x=k(\mu)\), and then EP8 and EP11; no numerical value of \(\pi\) is needed. At \(t=1/4,1/2,3/4,1\) it independently encloses \(r,J,8J,f\) strictly inside all sixteen supplied intervals. Those intervals and the narrower computed endpoints are retained in `profile_intervals_verified.json`.

There is a unique \(t_{1/2}\in(0,1)\) with \(J(t_{1/2})=J(1)/2\), by EP11. The computation first encloses the root \(T(\mu)=1\) more tightly than \(10^{-55}\), then bisects \(J(T(\mu))-J(1)/2\) using its outward interval, and returns through \(T\). It certifies

\[
 \boxed{0.28581630680480845015<t_{1/2}<0.28581630680480845016.}
 \tag{EP18}
\]

This certifies the decimal supplied in the first response, which was not included in its interval JSON. On the original kernel, PP45 gives uniformly

\[
 \log\frac{\det H_{K,q-1}}{\det H_{K,q-1+\lfloor tq\rfloor}}
 =mqJ(t)+o(kq),\quad m=8k-16.
 \tag{EP19}
\]

Consequently EP18 locates half of the limiting volume loss over the full original cutoff window. It is an asymptotic statement in the original fixed-period family; it is not an exact finite-\(k\) cutoff or a numerical evaluation of an assumed off-line zero. The four prescribed cutoffs still give two copies of \(J(1)=C_\partial/2\), hence \(mC_\partial q+o(kq)\), as in the published [CK14](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/1447462732b40b1474bd9a819cf79257f5326ada/workbenches/splitzero-tandem/continuations/20260922-kernel-frequency/COMBINED_KERNEL_AND_RECEIVERS.md#L148). That earlier coefficient is preserved.

## Proof provenance and receiving scope

Original incoming CP profile: `inputs/02_COMPLETE_PROOFS.md`, CP3–CP8 and CP19–CP23; both full responses are retained separately in the intake. The first response supplies its heat extension and sharper stated endpoint expansion, the second its full subquotient formulas. The analytic profile itself is verified by the independent PP proof and EP8. EP9–EP16 supplies the exact derivative representation and convergent higher correction; EP18 is a new independent certificate for the stated half-volume position.

Human reference: B. C. Carlson, *Elliptic Integrals*, DLMF Chapter19, original equation TeX19.8.12a,19.8.12b,19.5.1,19.5.2. These four formula sources were read, downloaded intact and hashed. No whole-book reading is claimed. The full elementary derivations used here are EP1–EP17. The original arithmetic and Gamma objects are connected by the retained024 CK/PJ/EL proofs and the new PP proof, all included in the cumulative source bank at publication.
