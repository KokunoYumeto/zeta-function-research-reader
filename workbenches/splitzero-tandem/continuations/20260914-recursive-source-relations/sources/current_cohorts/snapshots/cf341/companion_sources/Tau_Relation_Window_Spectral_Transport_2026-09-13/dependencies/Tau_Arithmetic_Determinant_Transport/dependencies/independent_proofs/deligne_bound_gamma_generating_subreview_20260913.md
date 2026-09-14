# Independent Gamma generating-function calculation

Date: 2026-09-13. Scope: the Gamma source, its exact mass and convolution, and the polynomial generating function and recurrence in equations (28), (29), (31), and (35) of the delivered `Tau_Deligne_Bound_Audit/NOTE.tex`. The source SHA-256 is `bfe63094ec360b6059f2936e5e456c6c0fd08db144bbabc29621a527b89c13c6`. The source remains unchanged. The quotient, trace, and determinant estimates are reviewed separately.

**Finding.** The printed generating function has linear coefficient \(+x\), and its exponential generating coefficients are literally monic polynomials in \(x\). The printed substitution produces literally monic polynomials in \(S\), and produces the negative last term of recurrence (35). The constants and convolution mass in (28)–(29) are also correct. No sign or mass correction is required for these formulas.

The proof below retains the original density, coordinate \(S=k/2+ix\), positive integer \(k\), and all factors of \(2\), \(i\), and \(\pi\). Euler's Beta integral is recorded in [DLMF 5.12.1](https://dlmf.nist.gov/5.12.E1) and [DLMF 5.12.3](https://dlmf.nist.gov/5.12.E3). The Fourier, convolution, and polynomial calculations here are derived explicitly from that integral.

## 1. Fourier transform of the unchanged Gamma density

Let \(a>0\), and define

\[
r_a(x)=\frac{|\Gamma(a+ix/2)|^2}{2\pi},\qquad
c_a=2^{1-2a}\Gamma(2a),\qquad x\in\mathbb R.
\tag{G1}
\]

We use the convention

\[
\mathcal F_+ f(t)=\int_{\mathbb R} f(x)e^{itx}\,dx.
\tag{G2}
\]

The Beta identity with arguments \(a+iu,a-iu\), followed by \(v=e^y\), gives

\[
\begin{aligned}
\frac{\Gamma(a+iu)\Gamma(a-iu)}{\Gamma(2a)}
&=\int_0^\infty\frac{v^{a+iu-1}}{(1+v)^{2a}}\,dv\\
&=\int_{\mathbb R}\frac{e^{ay}}{(1+e^y)^{2a}}e^{iuy}\,dy\\
&=\int_{\mathbb R} f_a(y)e^{iuy}\,dy,
\qquad f_a(y)=(2\cosh(y/2))^{-2a}.
\end{aligned}
\tag{G3}
\]

The function \(f_a\) and all its derivatives decay exponentially as \(y\to\pm\infty\). In particular, \(f_a,f_a''\in L^1(\mathbb R)\); integration by parts twice shows that its Fourier transform is \(O((1+|u|)^{-2})\). Fourier inversion therefore applies as an absolutely convergent integral. Write the left side of (G3) as \(F_a(u)\). Then

\[
f_a(y)=\frac1{2\pi}\int_{\mathbb R}F_a(u)e^{-iuy}\,du.
\tag{G4}
\]

Since \(r_a(x)=\Gamma(2a)F_a(x/2)/(2\pi)\), the change of variables \(x=2u\) in the original density gives

\[
\begin{aligned}
\mathcal F_+r_a(t)
&=\frac{\Gamma(2a)}{\pi}\int_{\mathbb R}F_a(u)e^{2itu}\,du\\
&=2\Gamma(2a)f_a(-2t)\\
&=2\Gamma(2a)(2\cosh t)^{-2a}
=c_a(\cosh t)^{-2a}.
\end{aligned}
\tag{G5}
\]

Every integral used in (G5) is absolutely convergent. In particular, its value at \(t=0\) proves the original mass

\[
\int_{\mathbb R}r_a(x)\,dx=c_a.
\tag{G6}
\]

For later coefficient extraction we also prove the exponential moments, rather than assuming them. The expression \(f_a(z)=(2\cosh(z/2))^{-2a}\) has the analytic branch positive on the real axis throughout \(|\operatorname{Im}z|<\pi\). For \(|\sigma|<\pi\),

\[
|\cosh((y+i\sigma)/2)|^2
=\sinh^2(y/2)+\cos^2(\sigma/2)
\ge\cos^2(\sigma/2)\cosh^2(y/2).
\tag{G7}
\]

Consequently \(f_a(y+i\sigma)\) is integrable in \(y\), uniformly when \(\sigma\) ranges in a closed smaller strip. The vertical sides of the contour rectangle in (G3) tend to zero because \(f_a\) decays exponentially in the real direction. Shifting the contour upward for \(u\ge0\) and downward for \(u<0\) therefore proves, for each \(0<\sigma<\pi\),

\[
|F_a(u)|\le
e^{-\sigma|u|}\int_{\mathbb R}|f_a(y+i\sigma)|\,dy.
\tag{G8}
\]

For \(u<0\) the integral along \(-i\sigma\) has the same bound by conjugation. Inserting \(u=x/2\) proves that \(r_a(x)\) is bounded by a constant times \(e^{-\sigma|x|/2}\). Thus every exponential moment of order strictly less than \(\pi/2\) is finite. Both sides of (G5) extend holomorphically to \(|\operatorname{Im}t|<\pi/2\); the right side uses the branch equal to the positive real value on the real axis. Equality on the real axis and the identity theorem imply

\[
\int_{\mathbb R}e^{vx}r_a(x)\,dx
=c_a(\cos v)^{-2a},\qquad v\in\mathbb R,\quad |v|<\pi/2.
\tag{G9}
\]

This is the exact moment generating function of the density with mass \(c_a\); no mass has been divided out.

## 2. The \(k\)-fold convolution and its mass

Fix the original value \(a=1/4\). Since \(\Gamma(1/2)=\sqrt\pi\), (G1) gives

\[
c_{1/4}=2^{1/2}\Gamma(1/2)=\sqrt{2\pi}.
\tag{G10}
\]

For every positive integer \(k\), the convolution theorem for the integrable functions in (G1) and formula (G5) give

\[
\begin{aligned}
\mathcal F_+(r_{1/4}^{*k})(t)
&=c_{1/4}^{k}(\cosh t)^{-k/2}\\
&=\mathcal F_+\left(\frac{c_{1/4}^{k}}{c_{k/4}}r_{k/4}\right)(t).
\end{aligned}
\tag{G11}
\]

Fourier uniqueness proves equality almost everywhere. The densities here are continuous: each \(r_a\) is continuous, bounded, and integrable, and convolution of an integrable function with a bounded uniformly continuous function is continuous. The required uniform continuity of \(r_a\) follows either from (G4) and the exponential estimate (G8), or directly by dominated differentiation there. Hence the equality holds at every real \(x\):

\[
r_{1/4,k}(x)=r_{1/4}^{*k}(x)
=\frac{c_{1/4}^{k}}{c_{k/4}}
\frac{|\Gamma(k/4+ix/2)|^2}{2\pi}.
\tag{G12}
\]

At \(t=0\), or by Tonelli's theorem in the original \(k\) variables,

\[
\int_{\mathbb R}r_{1/4,k}(x)\,dx
=c_{1/4}^{k}=(2\pi)^{k/2}.
\tag{G13}
\]

These are exactly equations (28)–(29) of the delivered note, including the coefficient \(c_{1/4}^{\,k}/c_{k/4}\).

## 3. The printed generating function has \(+x\), not \(-x\)

The printed function is, for \(z\) near zero,

\[
F_a(z,x)=(1-iz)^{-a+ix/2}(1+iz)^{-a-ix/2}
=\sum_{n=0}^{\infty}b_n^{(a)}(x)\frac{z^n}{n!}.
\tag{G14}
\]

Use the logarithms vanishing at \(z=0\). Their exact derivatives give

\[
\begin{aligned}
\partial_z\log F_a(z,x)
&=\frac{(-a+ix/2)(-i)}{1-iz}
+\frac{(-a-ix/2)i}{1+iz}\\
&=\frac{x-2az}{1+z^2}.
\end{aligned}
\tag{G15}
\]

In particular \(F_a(0,x)=1\) and \(\partial_zF_a(0,x)=x\). For real \(z\) near zero the same branches give the exact expression

\[
F_a(z,x)=(1+z^2)^{-a}\exp(x\arctan z).
\tag{G16}
\]

The sign in the exponential is positive because

\[
\log(1-iz)-\log(1+iz)=-2i\arctan z,
\quad
\frac{ix}{2}(-2i\arctan z)=x\arctan z.
\tag{G17}
\]

Multiply the differential equation (G15) by \(F_a\) and compare the coefficient of \(z^n/n!\). For \(n\ge1\), the coefficient contributed by \(z^2\partial_zF_a\) is \(n(n-1)b_{n-1}^{(a)}\), and that contributed by \(2azF_a\) is \(2an b_{n-1}^{(a)}\). Therefore

\[
b_0^{(a)}=1,\quad b_1^{(a)}=x,\quad
b_{n+1}^{(a)}(x)=x b_n^{(a)}(x)-n(n+2a-1)b_{n-1}^{(a)}(x).
\tag{G18}
\]

For \(n=0\), the same equation reads \(b_1^{(a)}=x b_0^{(a)}\), with the last term omitted. Induction in (G18) proves that \(b_n^{(a)}\in\mathbb R[x]\) has degree \(n\) and leading coefficient exactly \(1\). For example, the first values are

\[
\begin{aligned}
b_0^{(a)}&=1,& b_1^{(a)}&=x,\\
b_2^{(a)}&=x^2-2a,&
b_3^{(a)}&=x^3-(6a+2)x.
\end{aligned}
\tag{G19}
\]

Thus no replacement of \(z\), \(x\), or either exponent is needed to obtain monicity.

## 4. Exact orthogonality and norms

Take real \(z,w\) in a neighborhood of zero sufficiently small that \(|\arctan z+\arctan w|<\pi/2\). Equations (G9) and (G16) give

\[
\begin{aligned}
\int_{\mathbb R}F_a(z,x)F_a(w,x)r_a(x)\,dx
&=c_a(1+z^2)^{-a}(1+w^2)^{-a}
\bigl(\cos(\arctan z+\arctan w)\bigr)^{-2a}\\
&=c_a(1-zw)^{-2a}.
\end{aligned}
\tag{G20}
\]

The last equality uses the exact identity

\[
\cos(\arctan z+\arctan w)
=\frac{1-zw}{\sqrt{1+z^2}\sqrt{1+w^2}}.
\tag{G21}
\]

On a sufficiently small closed complex bidisc around \(z=w=0\), the absolute value of the integrand in (G20) is bounded by a constant times \(r_a(x)e^{v_0|x|}\) for some \(v_0<\pi/2\). This follows directly from the analytic logarithms in (G14). That dominating function is integrable by (G8). Consequently the integral is holomorphic on the open bidisc. The real identity (G20) extends there by applying the one-variable identity theorem first in \(z\), then in \(w\). Differentiation under the integral at zero is justified by Cauchy's formula and the same domination.

The coefficient of \(z^n w^m\) on the left side of (G20) is

\[
\frac1{n!m!}\int_{\mathbb R}b_n^{(a)}(x)b_m^{(a)}(x)r_a(x)\,dx.
\]

The binomial series on the right side is \(c_a\sum_{j\ge0}(2a)_j(zw)^j/j!\). Comparing coefficients yields

\[
\int_{\mathbb R}b_n^{(a)}(x)b_m^{(a)}(x)r_a(x)\,dx
=\mathbf1_{n=m}\,c_a n!(2a)_n.
\tag{G22}
\]

The polynomials have real coefficients, so (G22) is also their Hermitian orthogonality relation. In particular it is the norm of the original monic polynomial, with mass \(c_a\) retained.

## 5. Exact transport to \(S=k/2+ix\)

Set \(a=k/4\) and \(c=k/2\). Define the polynomial in the original complex variable \(S\) by

\[
p_n(S)=i^n b_n^{(k/4)}((S-c)/i).
\tag{G23}
\]

The coefficient of \(S^n\) is \(i^n i^{-n}=1\); hence this is literally monic in \(S\). The lower coefficients are obtained by the displayed affine substitution, with no change to the source norm or its mass. On the source line, \(S=c+ix\), equation (G23) gives \(p_n(c+ix)=i^n b_n^{(k/4)}(x)\). Therefore (G12) and (G22) imply

\[
\begin{aligned}
\int_{\mathbb R}\overline{p_n(c+ix)}p_m(c+ix)r_{1/4,k}(x)\,dx
&=\frac{c_{1/4}^{k}}{c_{k/4}}(-i)^n i^m
\int_{\mathbb R}b_n^{(k/4)}(x)b_m^{(k/4)}(x)r_{k/4}(x)\,dx\\
&=\mathbf1_{n=m}\,(2\pi)^{k/2}n!(k/2)_n.
\end{aligned}
\tag{G24}
\]

In the surviving term \(m=n\), the phase is \((-i)^n i^n=1\). This proves the exact norm \(\omega_{k,n}^{\Gamma}\) printed in (35).

To transport the recurrence, multiply (G18), in its form \(x b_n=b_{n+1}+n(n+2a-1)b_{n-1}\), by \(i^{n+1}\). Since \(S-c=ix\), the result is

\[
\begin{aligned}
(S-c)p_n(S)
&=p_{n+1}(S)
+n(n+k/2-1)i^{n+1}b_{n-1}^{(k/4)}((S-c)/i)\\
&=p_{n+1}(S)-n(n+k/2-1)p_{n-1}(S).
\end{aligned}
\tag{G25}
\]

The minus sign is exactly \(i^{n+1}/i^{n-1}=i^2=-1\). Restoring \(c=k/2\) proves

\[
Sp_n=p_{n+1}+\frac{k}{2}p_n-n(n+k/2-1)p_{n-1},
\qquad
\omega_{k,n}^{\Gamma}=(2\pi)^{k/2}n!(k/2)_n.
\tag{G26}
\]

The last term is omitted at \(n=0\). The first polynomials in the original coordinate are

\[
p_0=1,\qquad
p_1=S-k/2,\qquad
p_2=(S-k/2)^2+k/2,\qquad
p_3=(S-k/2)^3+(3k/2+2)(S-k/2).
\tag{G27}
\]

Finally, consecutive norm ratios retain the same constants before their displayed cancellation:

\[
\frac{\omega_{k,n}^{\Gamma}}{\omega_{k,n-1}^{\Gamma}}
=\frac{(2\pi)^{k/2}n!(k/2)_n}
{(2\pi)^{k/2}(n-1)!(k/2)_{n-1}}
=n(n+k/2-1),\qquad n\ge1.
\tag{G28}
\]

This supplies precisely the coefficient needed for the interior cancellation following equation (36). The derivation establishes the Gamma formulas and their original polynomial coordinates; it does not by itself assert the later determinant bound or a comparison with the arithmetic theta source.
