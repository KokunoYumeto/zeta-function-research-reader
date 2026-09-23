# Complete independent mathematical review of the endpoint-resonant zero detector

Review date: 2026-09-23.

**Accepted proof:** ENDPOINT_RESONANT_ZERO_DETECTION.md, the complete ERD1–50.

**Accepted source SHA256:**
ab38da7a21bcd40f125a10879968bccc75a48f2bcbc01ddcfd22c802f2e87c15.

The accepted file has 614 lines. Its complete ERD1–39 argument and complete ERD40–50 append were independently read and checked. The append's single domain correction, specifying a **nonempty** open set before ERD49, is present in the accepted source. There are no remaining mathematical corrections from this review.

The incoming source used by the proof was also read in full: ENDPOINT_RESONANCE_AND_PRIME_CLASS.tex, ER1–40a, including ER26a–f, SHA256 8e068f06bc98749a7e5747b17a798d3221dc4984dec316026bcd213a874bf667. Its role here is the actual ER31–34 cosine source and its original-zeta transform. No scalar arithmetic pairing is evaluated by this review.

The original heat source cited by the proof is Brad Rodgers and Terence Tao, [The de Bruijn–Newman constant is non-negative, arXiv:1801.05914v5](https://arxiv.org/abs/1801.05914v5), author-source labels phidef, htdef, hoz and sas. This review does not represent its bounded reading of the incoming programme source as a fresh full reading of that human paper.

## ERR1. Exact source, original variables and Gaussian constants — ERD1–5

The proof uses the original time \(t\), \(w=s-1/2\), and the full product
\[
 \mathcal Q(a)=a(a-1)\pi^{-a/2}\Gamma(a/2)\zeta(a)
           =16H_0(-2i(a-1/2)).
\]
The multiplier here has no factor \(1/2\). All subsequent constants are consistent with that convention.

For the actual source
\[
 h_t(Z)=e^{-Z^2/(4t)}H_t(Z)\cos(Z/(2t)),
\]
the Gaussian integration identity was independently checked:
\[
 \int_{\mathbb R}e^{-Z^2/(4t)-bZ}\cos(uZ)\,dZ
       =2\sqrt{\pi t}\,e^{tb^2-tu^2}\cos(2tbu).
\]
Its two exponential terms have the same sign in \(tb^2\) and the negative sign in \(tu^2\). Multiplication by the original density's factor \(e^{tu^2}\) removes only that exact factor; the other factors remain in the stated receiving formula. The Gaussian and density bounds in the proof justify the exchange of integrals for every fixed complex \(b\).

Splitting the source cosine therefore gives exactly
\[
 M_t(s)=\sqrt{\pi t}\left[
 e^{t(w-i/(2t))^2}H_0(2tw-i)
 +e^{t(w+i/(2t))^2}H_0(2tw+i)\right].
\]
For \(z=itw\), the two original arguments are \(1+z\) and \(z\). In particular \(iw=z/t\), so the two external phases become \(e^{-z/t}\) and \(e^{z/t}\), respectively. ERD5 retains the common factor
\(\sqrt{\pi t}\,e^{tw^2-1/(4t)}/16\), together with each argument's endpoint polynomial, Gamma factor, power of pi and original zeta function. These signs and the factor sixteen are correct.

## ERR2. Original endpoint and trivial-zero germs — ERD6–14

Multiplication of the original theta formula by \(a(a-1)\) gives
\[
 a(a-1)\left[-\frac1a+\frac1{a-1}\right]=1.
\]
Thus \(\mathcal Q=1+a(a-1)\mathcal J\), with
\(\mathcal J(1-a)=\mathcal J(a)\). The endpoint values and derivatives follow without suppressing either original rational term:
\[
 \mathcal Q(0)=\mathcal Q(1)=1,\qquad
 \mathcal Q'(1)=\mathcal J(1)=\delta>0,\qquad
 \mathcal Q'(0)=-\delta.
\]
At zero, \(A(h)=h^{-1}a_0(h)\), \(a_0(0)=2\), so the full multiplier \(a(a-1)A(a)\) has value \(-2\), which multiplies \(\zeta(0)=-1/2\). At one, its simple zero multiplies the original simple zeta pole of residue one. These are the correctly retained two exceptional germs.

At \(a=-2m+h\), the Gamma residue is
\[
 A(-2m+h)=h^{-1}a_m(h),\qquad
 a_m(0)=\frac{2(-1)^m\pi^m}{m!}.
\]
The local formula
\[
 \zeta(-2m+h)
  =h\,\frac{\mathcal Q(-2m+h)}
           {(-2m+h)(-2m-1+h)a_m(h)}
\]
is therefore exact. Reflection gives
\(\mathcal Q(-2m)=\mathcal Q(1+2m)>0\), proving the asserted simple original trivial zero with its full unit coefficient. No cancelled factor is used as a reason to erase that germ.

## ERR3. The elementary low-height exclusion — ERD10–13

For \(0\le\Re a\le1\), both powers in the theta-tail integrand have absolute value at most \(x^{-1/2}\le1\). Hence
\[
 |\mathcal J(a)|
 \le 2\sum_{n\ge1}\frac{e^{-\pi n^2}}{\pi n^2}
 \le\frac2{\pi(e^\pi-1)}
 <\frac2{21}.
\]
The geometric-series step uses \(n^2\ge n\) and \(1/n^2\le1\); \(\pi>3\) and \(e^3>8\) prove the last strict bound. This is uniform in imaginary part and yields \(0<\delta<2/21\).

If also \(|\Im a|\le1\), then \(|a(a-1)|\le2\). Consequently
\(|\mathcal Q(a)-1|<4/21<1\), which excludes a zero there.

The absolutely convergent Euler product excludes zeros of the full product for \(\Re a>1\); the reflected full product excludes them for \(\Re a<0\). The resulting enclosure is the closed vertical strip:
\[
 \rho=\beta+i\gamma,\qquad 0\le\beta\le1,\quad|\gamma|>1.
\]
The proof correctly does not assume a separate zero-free theorem on the boundary lines. At every enclosed zero the original multiplier is a holomorphic unit, so its multiplicity is the original-zeta multiplicity.

## ERR4. The complete genus-one factorization — ERD15–17

The theta-tail estimate gives
\(\log^+|\mathcal Q(a)|=O((1+|a|)\log(2+|a|))\). The proof retains its polynomial endpoint factor when deriving this bound.

The self-contained product argument was checked in full. Jensen's identity gives \(n(R)=O(R^{1+\varepsilon})\), with \(\varepsilon=1/4\); dyadic summation then gives \(\sum|\rho|^{-2}<\infty\). The genus-one product converges locally normally with the exact zero divisor.

For the quotient's entire logarithm, excluding intervals of radius \(R^{-3}\) about zero moduli up to \(4R\) removes total length \(O(R^{-2+\varepsilon})\), leaving a radius in \([R,2R]\). On its circle the small-zero product has lower logarithmic bound
\(-O(R^{1+\varepsilon}\log R)\); the tail has bound
\(-O(R^{1+\varepsilon})\). The Fourier-coefficient bound for the quotient logarithm then forces every coefficient of degree at least two to vanish. Its value at zero is zero, and its derivative is \(-\delta\). Therefore the exact product is
\[
 \mathcal Q(a)=e^{-\delta a}
        \prod_\rho(1-a/\rho)e^{a/\rho}.
\]
The linear exponential is not set to zero.

Logarithmic differentiation gives
\[
 \mathcal L(a)=-\delta+\sum_\rho
          \left[\frac1{a-\rho}+\frac1\rho\right],\qquad
 \mathcal L'(a)=-\sum_\rho\frac1{(a-\rho)^2}.
\]
The full original expression
\[
 \mathcal L(a)=\frac{\zeta'}{\zeta}(a)
 +\frac1a+\frac1{a-1}
 -\frac12\log\pi+\frac12\psi_\Gamma(a/2)
\]
is retained beside the product expression. The normally convergent derivative series and all signs are correct.

## ERR5. The uniform curvature bound — ERD18–21

The exact endpoint difference is
\[
 \sum_\rho\frac1{\rho(1-\rho)}
     =\mathcal L(1)-\mathcal L(0)=2\delta.
\]
The sum is absolutely convergent, including multiplicities.

For \(x=\gamma^2>1\) and \(b=\beta(1-\beta)\in[0,1/4]\), the real-part calculation is
\[
 \Re\frac1{\rho(1-\rho)}
 =\frac{x+b}{(x+b)^2+x(1-4b)}
 \ge\frac1{x+1}>\frac1{2x}.
\]
The first cross-multiplied difference is precisely
\(b(3x+1-b)\ge0\). Hence
\[
 \sum_\rho\gamma^{-2}\le4\delta<8/21.
\]
For \(|\Im a|=|v|<1\),
\(|a-\rho|\ge(1-|v|)|\gamma|\). The complete curvature bound is therefore
\[
 |\mathcal L'(u+iv)|
 \le\frac{4\delta}{(1-|v|)^2}
 <\frac8{21(1-|v|)^2},
\]
uniformly in \(u\). No high-zero ordinate or RH assertion enters this estimate.

## ERR6. Relative phase and the closed-strip theorem — ERD22–28

The full product is nonzero on \(|\Im a|<1\) and positive on the real axis. Its holomorphic logarithm can therefore be chosen real there. For
\[
 b(z)=\log\mathcal Q(z+1)-\log\mathcal Q(z)
\]
one has
\[
 b'(z)=\int_0^1\mathcal L'(z+x)\,dx.
\]
Integrating vertically gives the factor
\[
 \int_0^{|v|}\frac{dy}{(1-y)^2}
       =\frac{|v|}{1-|v|},
\]
rather than a constant-height bound. The resulting phase estimate
\[
 |\Im b(u+iv)|
 \le4\delta\,\frac{|v|}{1-|v|}
 <\frac8{21}\frac{|v|}{1-|v|}
\]
is correct.

For \(z=it(s-1/2)\), the closed critical strip gives \(|v|\le t/2\). The exact bracket factors as
\[
 e^{-z/t}\mathcal Q(z)\,[e^{b(z)}+e^{2z/t}].
\]
A zero of the last factor requires its relative phase to be an odd multiple of \(\pi\). Instead,
\[
 \left|\Im b(z)-\frac{2v}{t}\right|
 <1+\frac8{21}\frac{t}{2-t}\le\pi
\]
when
\[
 0<t\le T_*=\frac{2(\pi-1)}{\pi-1+8/21}.
\]
The first inequality remains strict at \(t=T_*\). Thus the theorem includes this upper time endpoint and both edges of the critical strip. When \(v=0\), the two terms are positive real, separately excluding cancellation.

At the requested \(t=1/32\), the exact bound is
\[
 1+\frac8{21\cdot63}=\frac{1331}{1323}<\pi.
\]
The prefactor \(\sqrt{\pi t}e^{tw^2-1/(4t)}/16\), the exponential \(e^{-z/t}\), and \(\mathcal Q(z)\) are nonzero on the stated domain. Thus the relative-phase calculation proves nonvanishing of the actual \(M_t\), not merely of an incompletely compared auxiliary expression. The bound is uniform at all heights.

## ERR7. The central line and global common-zero assertion — ERD29–33

At \(s=1/2+iy\), \(z=-ty\) is real. Both full products in ERD29 are positive, giving
\[
 M_t(\tfrac12+iy)
 =\frac{\sqrt{\pi t}}{16}e^{-ty^2-1/(4t)}
       [e^y\mathcal Q(1-ty)+e^{-y}\mathcal Q(-ty)]>0
\]
for every \(t>0\). This is correctly stated for the central line without extending the proved full-strip time range.

For the entire-in-time coefficient,
\[
 B(0,w)=\frac{\cos w}{8},\qquad
 \partial_tB(0,w)=\frac{\delta w\sin w}{8}.
\]
The derivative's sign and factor were checked directly using
\(\mathcal Q'(1)=\delta\), \(\mathcal Q'(0)=-\delta\). At every zero \(w=\pi/2+k\pi\) of the first coefficient, the second is nonzero. Therefore \(B(\cdot,w)\) is never identically zero. Its zeros at positive real time are discrete, and it is nonzero for all sufficiently small positive times at every fixed \(w\), including those where its constant term vanishes.

The original prefactor is nonzero at positive time, so the \(M_t\) family has no common zero anywhere in \(\mathbb C\). Multiplication by \(s(s-1)\) gives exactly the common zeros \(0,1\) for the \(F_t\) family. They have common multiplicity exactly one because \(M_t\) is nonzero at both endpoints for every time in the proved interval.

## ERR8. Source inverse, original zero multiplicities and jets — ERD34–38

Gaussian decay justifies both integrations by parts:
\[
 \mathcal M[(\partial_Z^2-\tfrac14)h_t]
       =[(s-\tfrac12)^2-\tfrac14]M_t=s(s-1)M_t.
\]
The derivative jump of \(e^{-|Z|/2}\) is \(-1\), so the correct Green distribution is
\(G=-e^{-|Z|/2}\), with
\((\partial_Z^2-\tfrac14)G=\delta_0\).
Its convolution preserves Schwartz space by the displayed weighted integral estimates. The homogeneous exponential solutions have no nonzero Schwartz member. The inverse ERD35 is therefore two-sided on that exact source.

At \(t=1/32\), \(F_t\) is a holomorphic unit on the open critical strip \(U\). Multiplication and division by \(F_t\) are mutually inverse \(\mathcal O(U)\)-module maps. They are not described as unital ring homomorphisms.

For an original zero \(\zeta(\rho+h)=h^m u(h)\), the product is
\[
 F_t(\rho+h)\zeta(\rho+h)
       =h^m F_t(\rho+h)u(h),
\]
with a nonzero unit coefficient. The multiplicity is exactly \(m\), including for \(F_t^2\zeta\). The inverse coefficients
\[
 b_0=a_0^{-1},\qquad
 b_n=-a_0^{-1}\sum_{k=1}^{n}a_kb_{n-k}
\]
are the correct recursion for \(1/F_t\), proving all finite jet inverses. The proof correctly restricts this module inverse to \(U\); it does not claim that division by \(F_t\) preserves the global Mellin–Schwartz test class.

## ERR9. The fixed support carrier — ERD39

The specified carrier has nonzero amplitudes only at top support and retains every lower-support zero point. A complex-linear map sends a top amplitude to its image with the same top label. A zero image is \(e=(0,1_L)\), not \(\tau=(0,0_L)\). Lower-support points remain fixed.

Consequently the proved function and jet inverses lift to inverse maps on the stated carriers. The scalar coefficient-base map is separately its identity, giving identity pullback on its prime spectrum. The proof does not infer a spectral map from multiplication by a function merely because that map is complex-linear.

## ERR10. The full scalar derivative recurrence — ERD40–42

The flat-time append retains
\[
 g_t=\sqrt{\pi t}e^{-1/(4t)},\qquad
 D(t,s)=e^{t(s-1/2)^2}B(t,s-1/2),\qquad
 M_t=g_tD,\quad F_t=s(s-1)g_tD.
\]
The function \(D\) is jointly entire. The scalar is specified on positive real time with its positive square root.

Direct differentiation verifies
\[
 g_t^{(n)}
 =\sqrt\pi e^{-1/(4t)}t^{1/2-2n}P_n(t),\qquad
 P_{n+1}=t^2P_n'
       +[(\tfrac12-2n)t+\tfrac14]P_n.
\]
The three terms arise, respectively, from differentiating the polynomial, power and exponential. In particular
\[
 P_1=\frac t2+\frac14,\qquad
 P_2=-\frac{t^2}{4}-\frac t4+\frac1{16};
\]
induction gives \(\deg P_n\le n\), \(P_n(0)=4^{-n}\).

In the \(n\)-th time derivative of \(gD\), the term with \(g^{(j)}\) has the additional factor \(t^{2(n-j)}\) relative to
\(t^{1/2-2n}e^{-1/(4t)}\). It is at most one for \(0<t\le1\). Joint entirety bounds every remaining mixed derivative of \(D\) on compact sets, giving exactly ERD42 for \(M_t\) and \(F_t\). The polynomial factor of \(F_t\) introduces only finitely many bounded spatial factors.

## ERR11. Smooth flatness and its correct analytic exceptions — ERD43–44

Every bound in ERD42 tends to zero faster than any power of \(t\). Dividing the corresponding bound by one further power proves inductively that the actual right derivatives at zero exist and vanish. Their continuity is given by the same estimates. This proves the \(C^\infty\) right extension with all mixed time and spatial derivatives zero, locally uniformly in the whole \(s\)-plane.

The proof does not identify this boundary value with the positive-time function: nonvanishing on the proved strip and time interval remains ERD44. For each fixed \(s\), the global small-time coefficient argument shows that \(M_t(s)\) is nonzero arbitrarily close to \(t=0+\). Its vanishing Taylor series therefore proves that it is not real analytic at that boundary. The same argument applies to \(F_t(s)\) for \(s\notin\{0,1\}\); at those two endpoints it is identically zero and is analytic. These are the correct exceptions.

## ERR12. Exact augmented inverse and coefficients — ERD45–48

For \(t>0\), \(g_t\ne0\), and
\[
 B(t,w)=e^{-tw^2}\frac{M_t(1/2+w)}{g_t}
\]
is the exact inverse formula when \(g_t\) remains a retained coordinate. At \(t=0\) this formula is undefined; the proof correctly keeps the augmented triple \((g_t,M_t,B)\). Positive-time data recover the analytic \(B\) and its limit, while the Taylor jets of the first two coordinates alone do not support the displayed division.

The coefficients in the two analytic coordinates are
\[
 B_t(0,w)=\frac{\delta w\sin w}{8},\qquad
 D_t(0,1/2+w)=\frac{w^2\cos w+\delta w\sin w}{8}.
\]
The \(w^2\cos w\) term is the required derivative of \(e^{tw^2}\). The compact-uniform analytic remainders follow from joint entire dependence. Multiplication by the unchanged full \(g_t\) and by \(w^2-1/4\) gives ERD47 without discarding either factor.

At the center the exact constants are
\[
 M_t(1/2)=\frac{\sqrt{\pi t}}8e^{-1/(4t)},\qquad
 F_t(1/2)=-\frac{\sqrt{\pi t}}{32}e^{-1/(4t)}.
\]
The sign and factor four in the second value are correct.

## ERR13. Flat ideal, dual-number map and corrected domain — ERD49–50

For a nonempty open \(U\), the smooth right-time holomorphic germs form the stated algebra \(\mathscr H(U)\). Leibniz's rule proves that
\[
 J_N(a)=\sum_{n=0}^N
       \frac{\partial_t^na(0,s)}{n!}\varepsilon^n
       \quad\bmod\varepsilon^{N+1}
\]
is a unital algebra homomorphism. Its coefficient convolution is exactly the factorial form of the binomial derivative formula. The intersection of its kernels over all \(N\) is the displayed flat ideal.

The evaluated maps are correct:
\[
 J_N(g)=J_N(M)=J_N(F)=0,\qquad
 J_1(B)=\frac{\cos(s-1/2)}8+
       \frac{\delta(s-1/2)\sin(s-1/2)}8\,\varepsilon,
 \quad\varepsilon^2=0.
\]
Thus the finite first-order map is explicitly related to the original detector, and no nonzero value of \(g\) is falsely identified with the dual-number element \(\varepsilon\).

For every finite \(k\ge1\), \(g_t^k>0\) at positive time. On a nonempty \(U\), its time germ is consequently nonzero. Hence \(g\) is nonzero and nonnilpotent although every finite time jet kills it.

The earlier append stated this paragraph for an arbitrary open \(U\); on the empty open set its nonzero assertion would have no content in the zero function algebra. The accepted source now explicitly says **nonempty open set**. This is the only correction found in the full append. All subsequent label lifts send its vanished top amplitude to \(e\), retain every lower support, and keep \(\tau\) distinct.

## ERR14. Scope of acceptance and limits actually used

The proof establishes a single-time zero detector on the entire closed critical strip, a precise nonoptimal positive-time interval, the global absence of common zeros for the full cosine family, full original-factor and finite-jet comparisons, and the exact flat-time/finite-jet relation.

It does not infer the sign of an individual off-line test term, the sign of a general Weil form, an RH conclusion, or preservation of an unstated global test-function class by the strip-wise inverse. The scalar arithmetic pairing belongs to a separate calculation. These boundaries are mathematical domain statements and are already present in the accepted proof.

The complete proof ERD1–50 is accepted at SHA256
ab38da7a21bcd40f125a10879968bccc75a48f2bcbc01ddcfd22c802f2e87c15,
with no remaining mathematical correction from this review.
