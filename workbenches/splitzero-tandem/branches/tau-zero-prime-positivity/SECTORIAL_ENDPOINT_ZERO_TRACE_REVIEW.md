# Independent review of the original-zeta endpoint-sector return

Review date: 2026-09-23.

The complete proof SER1–27 in SECTORIAL_ENDPOINT_ZERO_TRACE_RETURN.md was read and independently checked.

Reviewed source SHA256:
ef1b929539d4838feabd4cbe7b386241a0a083968ee5ba452ddceaf6efad27d0.

The controlling companion ESH1–18 was read in full separately, at SHA256 dd15be7c5b3d755a98f5f75a2d026c1ffe9e0f6f801c0e2f91bd060c377f198a. The independent receiving derivation is SECTORIAL_FILTER_TRACE_DERIVATION.md, SFT1–47. This review does not replace the proof source or assert a new RH conclusion.

## SERA1. Original factors, Gaussian legs and their signs

The coordinate \(Z=-2i(s-1/2)\) gives \(1+iZ=2s\), \(1-iZ=2(1-s)\), and \(-\partial_Z^2=\partial_s^2/4\). Thus both the original time and the factor \(1/4\) in SER11 are correct.

With \(K_t=\sqrt{\pi/t}\), the upper \(q\)-lateral square root \(+i\sqrt t\) gives
\[
 F_+(t,a)=-i\int_0^\infty e^{-tv^2+iav}\,dv.
\]
The lower value has the opposite prefactor and exponent sign. Their difference is the full Gaussian Fourier integral, giving \(-iK_t e^{-a^2/(4t)}\). Replacing \(a\) by \(-a\) in the upper leg gives the same sum identity. Substitution of \(a=2(s-1)\) therefore gives
\[
 I_+=J+2iK_t e^{-(s-1)^2/t},\qquad
 I_-=J-2iK_t e^{-s^2/t}.
\]
This verifies SER3–8 and the factor \(A^{-1}\) in the original \(f_+-f_-\). The inverse triangular map SER9 is exact when its two endpoint coordinates remain in the domain. It is not a bijection after those coordinates are forgotten.

## SERA2. The initial value and all one-sided derivatives

For \(\Im s\ge\delta>0\), every fixed-order derivative of each endpoint integral is dominated by \(C v^m e^{-2\delta v}\), independently of \(t\ge0\). Consequently all right derivatives at zero exist locally uniformly, and spatial derivatives can be interchanged with those right derivatives.

At \(t=0\),
\(\int_0^\infty e^{2isv}dv=-1/(2is)\), so the two terms \(2i\int(e^{2isv}-e^{2i(s-1)v})dv\) give exactly \(-1/s+1/(s-1)\). The identity theorem extends the original-strip Mellin equality to the upper half-plane, where \(A\zeta\) is holomorphic. This verifies SER10 without assigning pole-neighborhood convergence.

For every \(k\ge0\),
\[
 \int_0^\infty v^{2k}e^{2isv}\,dv
       =\frac{(2k)!}{(-2is)^{2k+1}},
\]
and multiplication by \(2i(-1)^k\) gives
\[
 \partial_t^kJ|_{0+}
 =\partial_t^k\mathcal L|_0+
    \frac{(2k)!}{4^k}
       [(s-1)^{-2k-1}-s^{-2k-1}].
\]
Every factorial and sign in SER12 is correct.

## SERA3. Zero Taylor radius and the actual remainder

If \(|s|\ne|s-1|\), the smaller denominator gives geometric domination in the endpoint difference. The coefficient, after division by \(k!\), contains \((2k)!/(4^k k!)\); its \(k\)-th root diverges. Multiplication by the fixed geometric denominator cannot prevent that divergence.

If the distances are equal in the upper half-plane, then \(\Re s=1/2\), \(s=Re^{i\theta}\) for \(0<\theta<\pi/2\), and \(s-1=Re^{i(\pi-\theta)}\). For the odd exponent \(2k+1\) this gives the exact difference
\[
 -2R^{-2k-1}\cos((2k+1)\theta).
\]
The identity
\(\sin(2\theta)=\cos x\sin(x+2\theta)-\sin x\cos(x+2\theta)\)
implies
\(|\sin(2\theta)|\le|\cos x|+|\cos(x+2\theta)|\).
Hence at least one of each consecutive pair of relevant cosine factors has magnitude at least \(\sin(2\theta)/2>0\). This proves the required divergent subsequence of coefficient roots even at equal distances.

The Taylor coefficients of the entire-in-time \(\mathcal L_t(s)\) have root limsup zero and cannot cancel that subsequence. Since \(A(s)\) is a finite nonzero constant for fixed \(s\) in the upper half-plane, the same conclusion holds for \(u_t=J_t/A\). This establishes the zero Taylor radius claimed in SER12–13; it does not contradict the locally uniform one-sided \(C^\infty\) statement.

For \(x\ge0\), Taylor's integral remainder gives
\[
 \left|e^{-x}-\sum_{k=0}^{N-1}\frac{(-x)^k}{k!}\right|
          \le\frac{x^N}{N!}.
\]
In SER7 each exponential leg has modulus at most \(e^{-2\delta v}\), the outside coefficient has modulus two, and there are two legs. Thus the remainder bound is
\[
 \frac{4t^N}{N!}\int_0^\infty v^{2N}e^{-2\delta v}dv
       =\frac{4t^N(2N)!}{N!(2\delta)^{2N+1}},
\]
exactly SER14. Its statement retains the independent entire \(\mathcal L\) remainder and does not claim convergence of the full Taylor series.

## SERA4. Reflections and differential return

Conjugation after \(s\mapsto1-\overline s\) interchanges the two endpoint exponential legs and conjugates \(2i\) to \(-2i\); their two sign changes cancel. Thus \(J^\#=J\). The original evenness of \(I_+\) gives the oriented defect
\[
 J(1-s)-J(s)=2iK_t(E_1-E_0).
\]
Also \(E_1^\#=E_0\), so \(I_+^\#=I_-\). This independently verifies all signs and orientations in SER15.

The original functions obey \(A^\#u^\#=Au\) and \(A^\#f_+^\#=Af_-\); these are the required twisted maps, rather than a factor-free assertion.

The twice integrated density gives the retained boundary \(-\rho'(0)\). The Poisson derivative identity gives \(\rho'(0)=0\), and separate endpoint/theta parts yield the two constants \(-1/64\) and \(-1/16\) exactly as in ESH. In the original variable, multiplication by sixteen gives
\[
 B_t=P+\frac t2+t(s-\tfrac12)\partial_s+\frac{t^2}{4}\partial_s^2.
\]
Both \(E_0\) and \(E_1\) lie in its kernel by direct differentiation. Therefore \(z_t=P_tu_t=P_tf_\pm\), with the full \(PA\) denominator, as claimed in SER16–18.

## SERA5. Actual zero comparison in the upper wedge

On a compact subset of the strict wedge, both exponents have real parts at least \(\eta/t>0\). Each raw branch contains one such term with coefficient \(2iK_t\); the common part is uniformly bounded at small nonnegative time. The reverse triangle inequality therefore gives exactly SER20. The Gamma factor is a unit in that wedge.

For a disk around an isolated original zero, both \(u_t\) and \(z_t\) converge uniformly to \(\zeta\), with nonzero boundary. Rouché's theorem preserves the total zero multiplicity inside. This argument includes multiple zeros and does not identify a uniformly valid threshold for an unbounded zero set. The contrast with the raw lateral functions is an actual local divisor calculation.

## SERA6. First variation and finite contour trace

For \(\beta=P'/P\), one has \(\beta'+\beta^2=P''/P=2/P\). Expanding the two covariant squares gives
\[
 \frac14(D_A+\beta)^2-\frac14D_A^2
      =\frac{\beta}{2}D_A+\frac1{2P},
\]
including the zero-order term. At a simple original zero, implicit differentiation and the nonzero spatial derivative give the two velocities of SER22. Their difference is \(-\beta(\rho)/2\), and is not a velocity of either raw lateral family.

Writing \(r=x+iy\), the difference is \(-r/(r^2-1/4)\). Multiplication by the conjugate denominator gives
\[
 \Re(v_C-v_A)=
   -\frac{x(x^2+y^2-1/4)}{|\rho(\rho-1)|^2},
\]
so SER23 has the correct sign and numerator. The reflection of the actual functions through their Gamma units preserves zeros. A simple zero fixed by that reflection therefore stays on the critical line while it is the unique local zero, which is precisely the local scope stated in the source.

For any multiplicity, logarithmic differentiation gives
\[
 \partial_t(\ell_z-\ell_u)|_{0+}
   =\partial_s\left[
       \frac{\beta}{2}\left(\frac{\zeta'}{\zeta}+\kappa\right)
        +\frac1{2P}\right].
\]
Near an upper-half-plane original zero \(\rho\) of multiplicity \(m\), the bracket has principal part \(m\beta(\rho)/(2(s-\rho))\). Differentiation gives exactly the double pole
\(-m\beta(\rho)/(2(s-\rho)^2)\), with no simple pole.

For the bounded domain and holomorphic test \(a\) specified in SER25, uniform boundary control permits differentiating the finite argument-principle integral. Multiplying the double pole by \(a(s)\) gives residue
\(-m\beta(\rho)a'(\rho)/2\). Summing proves SER25 for arbitrary multiplicities. No differentiation of individual multiple roots and no exchange with an infinite trace is required.

## SERA7. Growth and the support map

Completing the real quadratic in SER26 bounds each half-line integral by the full Gaussian integral, giving exactly \(\sqrt{\pi/t}\exp(|\Im s|^2/t)\). The double-exponential theta estimate gives order at most one for \(\mathcal L\), and the reciprocal-Gamma product preserves an order-at-most-two upper bound for the original raw functions. The source correctly avoids inferring an actual quadratic zero density or divergence of a quadratic-decay trace. The separate independent SFT39–47 supplies a cubic-decay rational domain with the linear genus-two polynomial retained.

The carrier in SER27 permits nonzero amplitudes only at top support. Its linear extension maps a vanishing top amplitude to \((0,\top)=e\) and fixes every lower-support zero point. This is a well-defined map on that exact carrier. The separately stated identity of the scalar coefficient semiring gives the identity pullback on its prime spectrum; the proof does not infer this prime map from the linear function-space operator. Endpoint coordinate retention and lower-support label retention are stated as different coordinates and are not conflated.

## Acceptance

No mathematical correction is required in the reviewed SER1–27 source at the hash above. The one-sided time domain, zero-radius series, finite-contour restriction, full Gamma twists and support morphism are all explicit and correctly used.
