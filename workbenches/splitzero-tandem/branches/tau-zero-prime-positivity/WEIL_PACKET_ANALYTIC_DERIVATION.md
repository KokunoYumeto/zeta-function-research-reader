# The explicit formula on the original entire-function packet

This note proves the analytic identity needed to connect the [finite packet](WEIL_PACKET_DERIVATION.md) to the arithmetic side of Weil's explicit formula. It uses the programme's actual multiplier, retains both polynomial coordinates, and proves convergence of every term. The result is an identity, not a proof of positivity or of the Riemann hypothesis.

The classical source for the formula and the Fourier/Mellin conventions is Alain Connes and Caterina Consani, [*Weil positivity and Trace formula, the archimedean place*, arXiv:2006.13771v1](https://arxiv.org/abs/2006.13771v1), original author source `weil-compo.tex`, Appendix A, “Fourier versus Mellin transforms” (`appenmellinapp`), and Appendix B, “Explicit formula” (`appendix2`), source lines 2011–2070. In particular `bombieriexplicit`, `bombieriexplicit1`, and `burnolexplicit1` fix the pole terms, prime terms, and archimedean sign. That source states its formula for compactly supported functions. The proof below establishes the required extension directly for the present functions; it does not infer admissibility from a numerical residual.

## WA1. Objects, involutions, and the exact integrand

Let
\[
g(s)=2\xi(s)=s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s).
\tag{WA1}
\]
Use the entire continuation of this classical function, with
\(g(1-s)=g(s)\), \(\overline{g(\bar s)}=g(s)\), and \(g(0)=g(1)=1\).
Retain the programme's counterfactual quartet
\[
\rho=\tfrac12+\delta+i\gamma,\quad
0<\delta<\tfrac12,\quad \gamma>2,\qquad
\mathcal R=(\rho,1-\bar\rho,\bar\rho,1-\rho).
\]
Each of these four distinct points is a zero of exact order \(m\ge1\) of \(g\). This is the original counterfactual input, not an assertion that such a zero has been found. Put
\[
h(s)=\prod_{\alpha\in\mathcal R}(s-\alpha)^m,
\quad v(s)=g(s)/h(s),\quad
\theta(s)=(s-\tfrac12)/i,\quad \iota(z)=\tfrac12+iz.
\tag{WA2}
\]
All apparent singularities of \(v\) are removable. At each packet point,
\[
v(\alpha)=\frac{g^{(m)}(\alpha)}{m!\prod_{\eta\in\mathcal R\setminus\{\alpha\}}(\alpha-\eta)^m}\ne0.
\]
For polynomials \(P,Q\in\mathbb C[z]\), define
\[
q_P=P\circ\theta,\quad q_Q=Q\circ\theta,\qquad
F_P(z)=P(z)v(\iota(z)),\quad F_Q(z)=Q(z)v(\iota(z)).
\]
For an entire function \(a\) in the \(s\)-coordinate, write
\(a^\#(s)=\overline{a(1-\bar s)}\). Conjugation followed by coefficient conjugation makes this entire, and the operation respects products. Reflection and conjugation permute the four factors of \(h\); the reflection contributes the sign \((-1)^{4m}=1\). Thus \(h^\#=h\) and \(v^\#=v\). The exact pairing integrand is
\[
A(s)=q_P^\#(s)q_Q(s)v(s)^2.
\tag{WA3}
\]
It is entire. On the critical line,
\[
K(t):=A(\tfrac12+it)=\overline{F_P(t)}F_Q(t),\qquad t\in\mathbb R.
\tag{WA4}
\]
At a packet point it is
\[
A(\alpha)=\overline{q_P(1-\bar\alpha)v(1-\bar\alpha)}\,q_Q(\alpha)v(\alpha).
\tag{WA5}
\]
These identities follow by substitution in the displayed involution. They do not replace \(q_P\) by \(P\).

## WA2. Uniform decay in every fixed vertical strip

Here is a decay proof that needs no zero-free horizontal line or estimate of \(\zeta'/\zeta\) inside the critical strip.

For \(\Re s>1\), integration of the absolutely convergent series for \(\zeta\) gives
\[
\zeta(s)=s\int_1^\infty\lfloor x\rfloor x^{-s-1}\,dx
=\frac{s}{s-1}-s\int_1^\infty\{x\}x^{-s-1}\,dx.
\tag{WA6}
\]
For the first equality, write \(\lfloor x\rfloor=\sum_{n\ge1}1_{[n,\infty)}(x)\), exchange the absolutely convergent sum and integral, and integrate each term. The last integral is holomorphic for \(\Re s>0\), by uniform domination on compact subsets there. It therefore gives the meromorphic continuation to this half-plane and the bound
\[
|\zeta(s)|\le |s/(s-1)|+|s|/(\Re s).
\tag{WA7}
\]
In particular it is bounded by a constant times \(1+|\Im s|\) when the real part ranges in a fixed compact interval contained in \((0,\infty)\) and \(|\Im s|\ge2\).

For \(z=\sigma+it\), \(\sigma>0\), rotate the Euler integral for \(\Gamma(z)\) through the angle \(\vartheta\operatorname{sgn}(t)\), where \(0<\vartheta<\pi/2\). The integral on the small circular arc tends to zero because \(\sigma>0\); the large arc tends to zero because the real part of its ray is positive. Cauchy's theorem gives
\[
\Gamma(z)=e^{i\vartheta\operatorname{sgn}(t)z}
\int_0^\infty e^{-r e^{i\vartheta\operatorname{sgn}(t)}}r^{z-1}\,dr,
\qquad
|\Gamma(\sigma+it)|\le e^{-\vartheta|t|}
\frac{\Gamma(\sigma)}{(\cos\vartheta)^\sigma}.
\tag{WA8}
\]
The bound is uniform for \(\sigma\) in any positive compact interval. Apply it with \(\vartheta=\pi/3\) to \(\Gamma(s/2)\). Equations WA1 and WA7 show, uniformly in every fixed interval \(1/2\le\Re s\le B\),
\[
|g(s)|\le C_B(1+|\Im s|)^3 e^{-\pi|\Im s|/6}
\quad(|\Im s|\ge2).
\tag{WA9}
\]
Reflection \(g(s)=g(1-s)\) gives the same type of estimate on every fixed vertical strip, including negative real parts. The constant may depend on that strip. Applying Cauchy's derivative formula on circles of radius \(1/4\), inside a slightly larger strip, gives the same estimate with an adjusted constant for every fixed derivative of \(g\). The exponential changes on such a circle by at most a constant factor.

For \(|\Im s|\) larger than twice the largest modulus of a packet point plus the strip width, every factor of \(h\) has modulus bounded below by a fixed positive multiple of \(1+|\Im s|\). Division by this polynomial and multiplication by the finite polynomials \(q_P^\#,q_Q\) therefore give
\[
|A^{(j)}(s)|\le C_{B,P,Q,j}(1+|\Im s|)^{D_j}e^{-\pi|\Im s|/3}
\tag{WA10}
\]
on each fixed vertical strip, for each fixed derivative order \(j\). On its bounded remaining part, entireness supplies a finite maximum. The same argument gives exponential strip decay of \(F_P,F_Q\) and every fixed derivative, with exponent \(\pi/6\). These are estimates on the actual functions, not assertions of uniform constants as the packet or the polynomials vary.

## WA3. The inverse transform, convolution, and prime-tail convergence

Define
\[
f_P(u)=\frac1{2\pi}\int_{\mathbb R}F_P(t)e^{itu}\,dt,
\quad f_Q(u)=\frac1{2\pi}\int_{\mathbb R}F_Q(t)e^{itu}\,dt,
\quad k(u)=\frac1{2\pi}\int_{\mathbb R}K(t)e^{itu}\,dt.
\tag{WA11}
\]
Exponential decay and its derivative estimates show that these inverse transforms are Schwartz functions. More explicitly, differentiate under the integral for derivatives in \(u\), and integrate by parts any number of times for powers of \(u\). All boundary terms vanish by WA10, and all resulting integrals converge absolutely. Fourier inversion on Schwartz functions gives \(\widehat f_P=F_P\), \(\widehat f_Q=F_Q\) with the convention \(\widehat f(t)=\int f(u)e^{-iut}du\).

For any real \(R>0\), shift the \(t\)-contour in the last integral of WA11 to \(\Im t=R\) for \(u\ge0\), and to \(\Im t=-R\) for \(u<0\). The vertical connecting pieces tend to zero by WA10; multiplication by \(e^{itu}\) is bounded on each connecting segment for fixed \(u\). Thus
\[
|k(u)|\le C_R e^{-R|u|},\qquad
C_R=\frac1{2\pi}\max_{\epsilon=\pm1}
\int_{\mathbb R}|A(\tfrac12-\epsilon R+it)|\,dt<\infty.
\tag{WA12}
\]
The same proof applies to \(f_P,f_Q\), and to their derivatives after inserting powers of the integration variable. Fubini's theorem on Schwartz functions gives the exact convolution
\[
k=\widetilde f_P*f_Q,\qquad \widetilde f_P(u)=\overline{f_P(-u)}.
\tag{WA13}
\]
Its Fourier transform is \(\overline{F_P(t)}F_Q(t)=K(t)\), which proves the equality by Fourier inversion.

Let \(\Lambda_{\rm ar}(n)=\log \ell\) when \(n=\ell^r\) for a prime \(\ell\) and \(r\ge1\), and zero otherwise. This is the arithmetic von Mangoldt function, not the observation map. Since \(0\le\Lambda_{\rm ar}(n)\le\log n\), taking any \(R>1/2\) in WA12 proves absolute convergence of
\[
\sum_{n\ge2}\frac{\Lambda_{\rm ar}(n)}{\sqrt n}
\bigl(k(\log n)+k(-\log n)\bigr).
\tag{WA14}
\]
There is also the explicit bound for every integer \(N\ge2\):
\[
\sum_{n>N}\frac{\Lambda_{\rm ar}(n)}{\sqrt n}
\bigl(|k(\log n)|+|k(-\log n)|\bigr)
\le 2C_R\sum_{n>N}\frac{\log n}{n^{R+1/2}}.
\tag{WA15}
\]
For example, with \(R=2\), the right side is at most
\[
2C_2N^{-3/2}\left(\frac23\log N+\frac49\right).
\tag{WA16}
\]
Indeed \((\log x)x^{-5/2}\) is decreasing for \(x\ge2\), so its sum beyond \(N\) is bounded by its integral from \(N\) to infinity; integration by parts gives the displayed expression. A numerical error certificate would additionally require a certified numerical bound for \(C_2\); the existence proof alone is not such a certificate.

## WA4. Cancellation of every unwanted zero

Set
\[
L(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s)=\frac{g(s)}{s(s-1)},
\qquad \ell(s)=L'(s)/L(s).
\tag{WA17}
\]
This meromorphic completed function has simple poles at \(0,1\), is invariant under \(s\mapsto1-s\), and otherwise has exactly the nontrivial zeta zeros with their multiplicities. These assertions also follow from WA1 and the stated entire continuation of \(g\). As a meromorphic identity,
\[
\ell(s)A(s)=q_P^\#(s)q_Q(s)\frac{g'(s)g(s)}{h(s)^2}
-\frac{A(s)}s-\frac{A(s)}{s-1}.
\tag{WA18}
\]
Away from the roots of \(g\), this is the logarithmic derivative identity and cancellation of one factor of \(g\). Both sides then have the same meromorphic continuation.

At a zero outside \(\mathcal R\), the first term in WA18 is holomorphic: its denominator does not vanish there. At \(\alpha\in\mathcal R\), the logarithmic derivative of \(g\) has residue \(m\); multiplication by the entire function \(A\) gives residue \(mA(\alpha)\), also when that residue is zero. At \(0,1\), the residues are respectively \(-A(0),-A(1)\). These are the only possible poles. This proves exact cancellation at every other zero, regardless of its location or multiplicity.

Choose a rectangle with vertical sides \(\Re s=3/2\) and \(\Re s=-1/2\), and horizontal sides \(\Im s=\pm T\), for \(T>\gamma+1\). There are no poles on its boundary after the removable singularities in WA18 have been filled. Equations WA9–WA10 bound its horizontal integrals by a polynomial in \(T\) times \(e^{-\pi T/3}\). They therefore tend to zero for all sufficiently large \(T\), without selecting a sequence avoiding other zeta zeros. The residue theorem and \(\ell(1-s)=-\ell(s)\) give
\[
m\sum_{\alpha\in\mathcal R}A(\alpha)-A(0)-A(1)
=\frac1{2\pi i}\int_{\Re s=3/2}
\ell(s)\bigl(A(s)+A(1-s)\bigr)\,ds.
\tag{WA19}
\]
The integral is oriented upwards. To verify the sign, the positively oriented left edge is downward. Writing it as minus an upward integral and substituting \(w=1-s\) changes \(\ell(1-w)\) to \(-\ell(w)\); its total contribution is therefore the plus \(A(1-s)\) term in WA19.

## WA5. The arithmetic integral and its exact signs

On \(\Re s=3/2\), the absolutely convergent Euler product gives
\[
\ell(s)=-\tfrac12\log\pi+\tfrac12\psi(s/2)
-\sum_{n\ge2}\Lambda_{\rm ar}(n)n^{-s},
\qquad \psi=\Gamma'/\Gamma.
\tag{WA20}
\]
For completeness, absolute convergence follows from \(\sum_{n\ge2}(\log n)n^{-3/2}<\infty\). Expanding each Euler factor as a geometric series gives \(\zeta\); expanding its logarithm and differentiating on any strictly smaller closed half-plane gives the last series with the displayed coefficients. Uniform convergence justifies that differentiation and shows the product is nonzero there.

The gamma factor in WA20 is holomorphic between real parts \(1/2\) and \(3/2\). Its growth is at most polynomial, which is sufficient here. One direct bound uses
\[
\psi(z)=-\gamma_E+\sum_{j=0}^\infty
\left(\frac1{j+1}-\frac1{j+z}\right),\qquad \Re z>0.
\tag{WA21}
\]
This expansion follows by logarithmic differentiation of Euler's gamma product, uniformly on compact subsets of this half-plane. For \(\Re z\ge a>0\), its summand has modulus at most
\(|z-1|/((j+1)(j+a))\), so the series gives \(|\psi(z)|\le C_a(1+|z|)\). Gamma conjugation gives \(\psi(\bar z)=\overline{\psi(z)}\). Shift the gamma integral in WA19 to \(\Re s=1/2\); the horizontal pieces vanish by this bound and WA10. Then substitute \(s=1/2+it\), and in the term with \(A(1-s)\) replace \(t\) by \(-t\). The result is
\[
\frac1{2\pi}\int_{\mathbb R}K(t)
\left(\Re\psi(\tfrac14+\tfrac{it}2)-\log\pi\right)dt.
\tag{WA22}
\]
All these integrals are absolutely convergent.

For the Dirichlet series part, WA10 and its absolute convergence on \(\Re s=3/2\) permit termwise integration by absolute domination. For each fixed \(n\), shift the entire integrand \(n^{-s}(A(s)+A(1-s))\) to the critical line. WA11 then gives
\[
\frac1{2\pi i}\int_{\Re s=3/2}n^{-s}
\bigl(A(s)+A(1-s)\bigr)ds
=\frac{k(-\log n)+k(\log n)}{\sqrt n}.
\tag{WA23}
\]
The first sign comes from \(n^{-it}=e^{-it\log n}\); reflection changes it for the second term. Thus the prime contribution is exactly minus WA14. Its convergence can be justified either before the shift by the absolutely convergent Dirichlet series or afterwards by WA12–WA15.

Combining WA19, WA22 and WA23 proves the complete identity
\[
\boxed{\begin{aligned}
m\sum_{\alpha\in\mathcal R}
\overline{q_P(1-\bar\alpha)v(1-\bar\alpha)}\,q_Q(\alpha)v(\alpha)
={}&A(0)+A(1)\\
&+\frac1{2\pi}\int_{\mathbb R}\overline{F_P(t)}F_Q(t)
\left(\Re\psi(\tfrac14+\tfrac{it}2)-\log\pi\right)dt\\
&-\sum_{n\ge2}\frac{\Lambda_{\rm ar}(n)}{\sqrt n}
\bigl(k(\log n)+k(-\log n)\bigr).
\end{aligned}}
\tag{WA24}
\]
It holds for every pair of polynomials and every packet satisfying the retained original hypotheses. No assumption of Weil positivity enters its proof.

## WA6. Exact comparison with the published multiplicative convention

Define a function on \(\mathbb R_{>0}\) by
\[
b_A(x)=x^{-1/2}k(-\log x).
\tag{WA25}
\]
It has decay sufficient for all the following integrals by WA12. Substituting \(x=e^u\) in its Mellin transform gives
\[
\int_0^\infty b_A(x)x^{s-1}dx
=\int_{\mathbb R}k(-u)e^{(s-1/2)u}du=A(s).
\tag{WA26}
\]
On the critical line this is Fourier inversion, and on the whole plane it follows by the same absolutely convergent transform and analytic continuation. Its involution satisfies
\[
b_A^\sharp(x)=x^{-1}b_A(x^{-1})=x^{-1/2}k(\log x).
\tag{WA27}
\]
Consequently the two pole integrals in `bombieriexplicit` are precisely \(A(1),A(0)\); for the second integral use the substitution \(y=x^{-1}\). At a prime power \(x=\ell^r\), its two finite-place terms are exactly \(\ell^{-r/2}(k(-r\log\ell)+k(r\log\ell))\). The opposite of the archimedean distribution in `burnolexplicit1` is the integral in WA24. Equations WA25–WA27 prove the complete change of conventions, including its inverse \(k(u)=e^{-u/2}b_A(e^{-u})\). The function is not asserted compactly supported; WA19–WA24 provide the required analytic extension.

## WA7. Consequence for the programme's finite form, with the radical retained

Let \(E_h=\mathbb C[s]/(h)\), let \(U=M_{j_h(v)}\) be the literal finite Taylor-remainder multiplier, and let \(e:E_h\to\mathbb C^{\mathcal R}\) evaluate the zeroth jets. The finite proofs WP13–WP25 give its complete jet formula and establish
\[
a_h=eU,\qquad a_h([q])=(q(\alpha)v(\alpha))_\alpha,\qquad
\ker a_h=(d)/(d^m),\quad d=\prod_{\alpha\in\mathcal R}(s-\alpha).
\tag{WA28}
\]
The elementary proof of the kernel is that all \(v(\alpha)\) are nonzero and a polynomial vanishes at the four distinct points exactly when divisible by \(d\). Surjectivity follows from interpolation at those points. The actual multiplier retains the higher jets, as specified in WP21; WA28 takes their stated quotient.

In the displayed order of \(\mathcal R\), the left side of WA24 is the pullback under \(a_h\) of
\[
b(c,d)=m(\bar c_2d_1+\bar c_1d_2+\bar c_4d_3+\bar c_3d_4).
\tag{WA29}
\]
Each pair has matrix \(m\begin{pmatrix}0&1\\1&0\end{pmatrix}\), with eigenvectors \((1,1)\), \((1,-1)\) and eigenvalues \(m,-m\). Hence this form has inertia \((2,2)\), and its pullback has inertia \((2,2,4m-4)\) and radical exactly WA28. The degree-three polynomial
\[
q_-(s)=\frac{\prod_{\eta\ne\alpha_1}(s-\eta)}
{v(\alpha_1)\prod_{\eta\ne\alpha_1}(\alpha_1-\eta)}
-\frac{\prod_{\eta\ne\alpha_2}(s-\eta)}
{v(\alpha_2)\prod_{\eta\ne\alpha_2}(\alpha_2-\eta)}
\tag{WA30}
\]
has amplitude values \((1,-1,0,0)\). Taking \(P_-=q_-\circ\iota\), and \(P=Q=P_-\) in WA24, proves that its full arithmetic right side is exactly \(-2m\). This is the arithmetic identity associated with the assumed off-line packet. It is not a constructed off-line zero and does not establish that the arithmetic right side is nonnegative for zeta.

The analytic identity closes the admissibility question for these noncompact test functions. The remaining RH question is an actual sign statement for the right side of WA24 on this programme family. Neither positive source norms nor the nonzero divided-power classes alone prove that sign. Their comparison must supply a proved map and an inequality before any RH conclusion can be drawn.
