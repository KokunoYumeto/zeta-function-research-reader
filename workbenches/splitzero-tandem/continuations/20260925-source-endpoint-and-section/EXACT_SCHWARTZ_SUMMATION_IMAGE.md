# Exact Schwartz summation image and the original-zeta cohomology

24 September 2026. Complete global calculation SSI0–SSI10. This strengthens the closure result S5 in `GLOBAL_MELLIN_SYNTHESIS.md` to an equality with the actual image. It uses the original zeta function throughout. All zero multiplicities, trivial-zero residues, endpoint conditions, the two signs in rational summation, and the two chart orientations are retained.

## SSI0. Prerequisites and the precise operation

The governing user arguments and corrections are in `argument_reconstruction/CORPUS_AND_OPERATION_RULE.md`, `LATEST_DIRECT_ARGUMENTS.md`, `CORRECTION_CHAINS.md`, and the complete verbatim corpus. They require global reconstruction before arithmetic operations. The integers, their unit, primes, prime powers, complex coefficient field, Schwartz spaces and Mellin maps in the present calculation are the already reconstructed receivers in `CANONICAL_GENERIC_RECONSTRUCTION.md`, CG0–CG4, and `GLOBAL_MELLIN_SYNTHESIS.md`, S1–S6. No operation here constructs them by selecting a few primes. In particular, the Möbius inverse in SSI7 uses the entire reconstructed arithmetic.

The support notation remains \(Z_0,Z_1,Z_2,\ldots,\tau\). No addition at \(\tau\), numerical value of \(\tau\), distance to \(\tau\), or purity assumption is introduced. The theorem concerns an actual linear map on the coefficient spaces carried at the support. Its receiving cohomology maps are given in SSI8; no arithmetic weight separation is inferred from closedness.

The author source is Alain Connes and Caterina Consani, *Schemes over F1 and zeta functions*, [arXiv:0903.2024v3](https://arxiv.org/abs/0903.2024v3), original `announc3.tex`, §5, lines1376–1667, read in full. Source SHA256: `8254a72d27b082e0a3550e6be9398bae1c7e267303dc2b86a904703f58569fd4`. The retained archive has SHA256 `f09e4f8a917de991a84b508023598259e9d79694425ce5bd1ddd33d7c729e53f`. This note proves a real even-Schwartz summation theorem and applies it to the explicitly defined coefficient sheaf CSL1. Its further identification with a particular convention for adelic coinvariants is a separate comparison; no missing coinvariant proof is supplied by a name.

The full dependency for the growth estimate is S2–S3 and its independent proof audit R1–R3 in `GLOBAL_MELLIN_SYNTHESIS_REVIEW.md`. The proof below uses the subquadratic division bound proved there, rather than a conjectural lower bound on zeta in the critical strip. Poisson summation and ordinary Fourier inversion use the same convention as that source. The standard Gamma recurrence and reflection identities are used with their factors displayed.

## SSI1. Spaces, maps and the claimed equality

Let
\[
S=\{f\in\mathcal S(\mathbb R;\mathbb C):
 f(-v)=f(v),\quad f(0)=0,\quad\int_{\mathbb R}f(v)\,dv=0\}.
\tag{SSI1.1}
\]
It is a closed subspace of Schwartz space. Its seminorms may be taken to be
\[
q_{r,j}(f)=\sup_{v\in\mathbb R}(1+|v|)^r|f^{(j)}(v)|,
\qquad r,j\ge0.
\tag{SSI1.2}
\]
Let
\[
A=\{b\in C^\infty(\mathbb R_{>0}):
 p_{N,j}(b)=\sup_{u>0}(u^N+u^{-N})|(u\partial_u)^jb(u)|<\infty
 \text{ for all }N,j\ge0\},
\tag{SSI1.3}
\]
and let \(\mathcal B\) consist of entire functions with seminorms
\[
b_{A_0,M}(F)=\sup_{|\sigma|\le A_0,\ t\in\mathbb R}
 (1+|t|)^M|F(\sigma+it)|<\infty
\quad(A_0,M\ge0).
\tag{SSI1.4}
\]
Integer indices suffice in these seminorms. The raw Mellin map and its inverse are
\[
\mathcal M_0b(s)=\int_0^\infty b(u)u^s\frac{du}{u},\qquad
b(e^x)=\frac{e^{-cx}}{2\pi}\int_{\mathbb R}
 (\mathcal M_0b)(c+it)e^{-itx}\,dt .
\tag{SSI1.5}
\]
They are mutually inverse continuous maps \(A\leftrightarrow\mathcal B\), for any real \(c\). This is S1 with its exact change of exponent. Specifically, for its centered map \(\mathcal M\) and \(\mathcal T k(u)=2u^{-1/2}k(u)\), one has \(\mathcal M_0\mathcal T=2\mathcal M\). Multiplication by these displayed powers preserves all the spaces with continuous inverse.

For every actual nontrivial zero \(\rho\) of the original \(\zeta\), let \(m_\rho\) be its original multiplicity. Define the closed subspace
\[
I=\{F\in\mathcal B:F^{(j)}(\rho)=0
 \text{ for every }\rho\text{ and }0\le j<m_\rho\}.
\tag{SSI1.6}
\]
Jet evaluation is continuous by Cauchy's integral formula on a fixed small circle, so this intersection is closed. Define
\[
\Sigma:S\longrightarrow A,\qquad
\Sigma f(u)=2\sum_{n\ge1}f(nu),\qquad J=\Sigma S.
\tag{SSI1.7}
\]
The factor2 is the contribution of both signs in the even sector. The theorem proved below is the topological isomorphism
\[
\boxed{\mathcal M_0\Sigma:S\xrightarrow{\ \sim\ }I.}
\qquad
\boxed{J=\mathcal M_0^{-1}I=\overline J^{\,A}.}
\tag{SSI1.8}
\]
The inverse is actual Schwartz inversion, with no limiting class substituted for a source function.

## SSI2. Continuity, inclusion, injectivity and full meromorphic division

On \(u\ge1\), every logarithmic derivative of the series in (SSI1.7) is bounded by a finite sum of Schwartz seminorms times \(u^{-L}\sum n^{-L}\), for any sufficiently large integer \(L>1\). For \(0<u\le1\), the Fourier convention
\[
\widehat f(t)=\int_{\mathbb R}f(v)e^{-2\pi ivt}\,dv
\tag{SSI2.1}
\]
and Poisson summation give the full identity
\[
\Sigma\widehat f(u)=u^{-1}\Sigma f(u^{-1})
 +u^{-1}f(0)-\int_{\mathbb R}f(v)\,dv.
\tag{SSI2.2}
\]
For \(f\in S\), the last two terms vanish by the two stated moment conditions; \(\widehat f\in S\). This proves the required estimates at zero and the continuity \(\Sigma:S\to A\).

For \(\Re s>1\), absolute integration and summation give
\[
\mathcal M_0\Sigma f(s)=2\zeta(s)\int_0^\infty f(v)v^s\frac{dv}{v}.
\tag{SSI2.3}
\]
The positive-axis Mellin integral is holomorphic on \(\Re s>-2\), since evenness and \(f(0)=0\) give \(f(v)=O(v^2)\). It vanishes at \(s=1\), because \(\int_{\mathbb R}f=0\). Thus (SSI2.3) continues through the zeta pole at1 and proves full-order vanishing at every nontrivial zero. This proves \(\mathcal M_0\Sigma S\subset I\).

If \(\Sigma f=0\), the nonvanishing Euler product for \(\zeta\) on \(\Re s>1\) implies that the positive-axis Mellin transform is zero on that half-plane. Fourier uniqueness on a vertical line gives \(f=0\) on \(\mathbb R_{>0}\), and evenness and continuity give \(f=0\) on all of \(\mathbb R\). Hence \(\Sigma\) is injective.

Conversely, let \(F\in I\) and put
\[
H(s)=\frac{F(s)}{2\zeta(s)}.
\tag{SSI2.4}
\]
At a nontrivial zero \(\rho\), write \(\zeta(s)=(s-\rho)^{m_\rho}u(s)\), with \(u(\rho)\ne0\), and \(F(s)=(s-\rho)^{m_\rho}v(s)\). Then \(H=v/(2u)\) extends holomorphically there. No simplicity or separation of these zeros is assumed. The only possible poles of \(H\) are the simple trivial-zero poles
\[
\operatorname{Res}_{s=-2r}H(s)=c_r(F):=
 \frac{F(-2r)}{2\zeta'(-2r)},\qquad r\ge1.
\tag{SSI2.5}
\]
The original functional equation proves that these zeros are simple: its sine factor has a simple zero at \(-2r\), whereas its Gamma factor and \(\zeta(1+2r)\) are finite and nonzero. At zero and one the exact values are
\[
H(0)=-F(0),\qquad H(1)=0,\qquad H'(1)=\frac{F(1)}2.
\tag{SSI2.6}
\]
Here \(\zeta(0)=-1/2\) and the residue of \(\zeta\) at1 is1. The endpoint pole and each trivial zero have been used, not discarded.

## SSI3. Growth and exact estimates on the two vertical edges

Keep the auxiliary source transform of S2 with all factors:
\[
F_*(s)=\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2)\zeta(s).
\tag{SSI3.1}
\]
It is the function denoted \(F_0\) in S2. Its zeros are exactly the nontrivial zeros with their multiplicities, and \(F_*(0)=F_*(1)=1/8\). It is used only for the proved division estimate. S3 gives
\[
\sup_{|\sigma|\le A_0}|F/F_*(\sigma+it)|
\le C_{A_0,F}\exp\{C_{A_0}(|t|+2)^{3/2}\log(|t|+2)\}.
\tag{SSI3.2}
\]
Retaining the comparison rather than replacing \(\zeta\), one has
\[
H(s)=\frac{s(s-1)}{16}\pi^{-s/2}\Gamma(s/2)
 \frac{F(s)}{F_*(s)}.
\tag{SSI3.3}
\]
On every bounded real strip and \(|t|\ge1\), the Gamma factor has an upper bound by a polynomial in \(1+|t|\). Indeed choose an integer \(L\) for which \(\sigma/2+L\ge1\) throughout the strip. The recurrence and Euler integral give
\[
|\Gamma(s/2)|=
\frac{|\Gamma(s/2+L)|}{\prod_{j=0}^{L-1}|s/2+j|}
\le\frac{\Gamma(\sigma/2+L)}{(|t|/2)^L}.
\tag{SSI3.4}
\]
The numerator is bounded on the compact interval of its real arguments. Equations (SSI3.2)–(SSI3.4) therefore give subquadratic growth for \(H\), away from its finitely many poles in each strip. This is sufficient for the maximum-principle argument; no conjectural reciprocal-zeta estimate is used.

Choose an integer \(N\ge0\), let \(a=-2N-1\), and choose a real \(b\ge2\). On the right edge, the absolutely convergent reciprocal Euler series yields
\[
|\zeta(b+it)^{-1}|\le\sum_{n\ge1}|\mu(n)|n^{-b}\le\zeta(b).
\tag{SSI3.5}
\]
Here \(\mu\) is the Möbius function of the complete reconstructed integers; its use does not select a finite set of primes.

On the left edge retain the functional equation in its full multiplier form
\[
\zeta(s)=\chi(s)\zeta(1-s),\qquad
\chi(s)=\pi^{s-1/2}\frac{\Gamma((1-s)/2)}{\Gamma(s/2)}
=2^s\pi^{s-1}\sin(\pi s/2)\Gamma(1-s).
\tag{SSI3.6}
\]
Writing \(y=t/2\), Gamma recurrence and reflection give the exact identity
\[
|\chi(-2N-1+it)|^2=
\pi^{-4N-3}\,y\coth(\pi y)
 \prod_{k=1}^{N}(k^2+y^2)
 \prod_{j=0}^{N}\big((j+\tfrac12)^2+y^2\big).
\tag{SSI3.7}
\]
The empty product is1 and \(y\coth(\pi y)\) has the value \(1/\pi\) at zero. To verify (SSI3.7), apply the recurrence to \(\Gamma(N+1-iy)\), and to \(\Gamma(-N-1/2+iy)\) up to \(\Gamma(1/2+iy)\). The remaining exact quotient of squared moduli is
\[
\frac{|\Gamma(1-iy)|^2}{|\Gamma(1/2+iy)|^2}
=\frac{\pi y/\sinh(\pi y)}{\pi/\cosh(\pi y)}
=y\coth(\pi y).
\tag{SSI3.8}
\]
These two modulus identities follow from \(\Gamma(z)\Gamma(1-z)=\pi/\sin(\pi z)\) and \(\Gamma(1+z)=z\Gamma(z)\); their values at zero are their continuous limits. All factors on the right of (SSI3.7) are positive for real \(y\), and their growth at infinity gives constants \(c_N,C_N>0\) with
\[
c_N(1+|t|)^{4N+3}\le |\chi(a+it)|^2
 \le C_N(1+|t|)^{4N+3}.
\tag{SSI3.9}
\]
For completeness, this follows on \(|t|\ge1\) by bounding each quadratic between positive multiples of \(1+t^2\), and bounding \(y\coth(\pi y)\) between positive multiples of \(1+|y|\). On \(|t|\le1\), positivity and continuity give the same inequalities after changing the constants. Since \(\Re(1-a-it)=2N+2>1\), (SSI3.5) applies to \(\zeta(1-a-it)\). Thus \(1/\zeta\) is polynomially bounded on the left edge too, with no zero on either edge.

It follows that \(H\) decreases faster than every inverse power on each edge. Every such bound is bounded by a fixed constant times a finite seminorm of \(F\) in \(\mathcal B\). The constants can depend on \(N,b\) and the requested power, but not on \(F\).

## SSI4. The maximum principle removes the Gaussian approximation

Define
\[
P_N(s)=\prod_{r=1}^N(s+2r),\qquad P_0=1,\qquad V_N=P_NH.
\tag{SSI4.1}
\]
This product cancels exactly the possible poles inside the strip \(a\le\Re s\le b\). Hence \(V_N\) is holomorphic on a neighborhood of that closed strip. For an integer \(M\ge0\) set \(\kappa=2N+2\) and
\[
W(s)=(s+\kappa)^M V_N(s).
\tag{SSI4.2}
\]
The estimates in SSI3 give, on the two vertical edges,
\[
|W(s)|\le C_{N,b,M}\, b_{A_0,M+N}(F),
\quad A_0\ge\max(2N+1,b).
\tag{SSI4.3}
\]
Indeed the polynomial factors have total degree \(M+N\), and the reciprocal-zeta bounds on each edge are bounded, in addition to having the more precise polynomial behavior already computed.

For \(\varepsilon>0\), apply the maximum-modulus principle to
\(e^{\varepsilon s^2}W(s)\) on the rectangle with vertical edges \(a,b\) and horizontal edges \(\Im s=\pm T\). On the horizontal edges, (SSI3.2)–(SSI3.4) give a bound of the form
\[
C_{F,N,b,M,\varepsilon}(1+T)^L
\exp\{-\varepsilon T^2+C_{N,b}(T+2)^{3/2}\log(T+2)\},
\tag{SSI4.4}
\]
which tends to zero as \(T\to\infty\), uniformly in the real coordinate. On the vertical edges, (SSI4.3) gives
\[
|e^{\varepsilon s^2}W(s)|\le
e^{\varepsilon\max(a^2,b^2)}C_{N,b,M}b_{A_0,M+N}(F).
\tag{SSI4.5}
\]
Fix any interior \(s\), let \(T\to\infty\), and then let \(\varepsilon\downarrow0\). The resulting estimate is
\[
|W(s)|\le C_{N,b,M}b_{A_0,M+N}(F).
\tag{SSI4.6}
\]
This also holds on the edges by continuity. Since \(\Re(s+\kappa)\ge1\) throughout the strip,
\[
\boxed{\sup_{a\le\sigma\le b,\ t\in\mathbb R}
(1+|t|)^M|P_N(\sigma+it)H(\sigma+it)|
\le C'_{N,b,M}b_{A_0,M+N}(F).}
\tag{SSI4.7}
\]
The growth constant depending on \(F\) in (SSI4.4) is used only to remove the horizontal edges for a fixed \(F\). It does not enter the final bound (SSI4.7). Thus (SSI4.7) proves continuous seminorm control as well as existence of rapid decrease. There is no limit of source classes left in the assertion.

On a vertical line avoiding the finitely many trivial poles, division by \(P_N\) gives corresponding rapid bounds for \(H\). On horizontal lines with \(|t|\ge1\), each \(|s+2r|\ge|t|\), so the same bounds justify all contour shifts below. Cauchy's integral formula on small disks away from the poles also gives rapid bounds for every holomorphic derivative of \(H\).

## SSI5. Actual inverse Mellin and all even Taylor coefficients

Define for \(x>0\)
\[
f_F(x)=\frac1{2\pi}\int_{\mathbb R}H(2+it)x^{-2-it}\,dt.
\tag{SSI5.1}
\]
This integral is absolutely convergent and can be differentiated any finite number of times. On every compact interval of \(x>0\), the integrable majorant follows from (SSI4.7). The exact derivative factor is
\[
\frac{d^j}{dx^j}x^{-s}=(-1)^j(s)_j x^{-s-j},
\qquad (s)_j=s(s+1)\cdots(s+j-1),\quad(s)_0=1.
\tag{SSI5.2}
\]
Contour shifting to any \(c\ge2\) crosses no pole and gives
\[
f_F^{(j)}(x)=\frac{(-1)^j}{2\pi}
\int_{\mathbb R}(c+it)_jH(c+it)x^{-c-it-j}\,dt.
\tag{SSI5.3}
\]
The horizontal contributions tend to zero by SSI4. Taking \(c\) arbitrarily large proves faster-than-any-power decay of every derivative at infinity.

Shifting the contour to \(a=-2N-1\) crosses precisely the poles in (SSI2.5) for \(1\le r\le N\), with their positive residue sign. Thus
\[
f_F(x)=\sum_{r=1}^N c_r(F)x^{2r}
 +\frac1{2\pi}\int_{\mathbb R}H(a+it)x^{-a-it}\,dt.
\tag{SSI5.4}
\]
For every integer \(j\ge0\), the remainder after differentiating this equality \(j\) times is bounded, on \(0<x\le1\), by
\[
\frac{x^{2N+1-j}}{2\pi}
\int_{\mathbb R}|(a+it)_jH(a+it)|\,dt.
\tag{SSI5.5}
\]
This integral is finite and bounded by a finite seminorm of \(F\). For any prescribed derivative order choose \(N\) large enough that \(2N+1-j>0\). Each derivative then has a finite limit as \(x\downarrow0\), equal to the derivative at zero of the even polynomial in (SSI5.4). These limits consistently extend \(f_F\) to a smooth function on the half-line: the fundamental theorem of calculus applied to successive derivatives, followed by their continuous limits, proves that the extended derivative is indeed the derivative of the extended preceding function. Extending by \(f_F(-x)=f_F(x)\) is smooth because every odd one-sided derivative is zero. In particular,
\[
f_F(0)=0,\qquad f_F^{(2r-1)}(0)=0,\qquad
\boxed{\frac{f_F^{(2r)}(0)}{(2r)!}=
 \frac{F(-2r)}{2\zeta'(-2r)}}\quad(r\ge1).
\tag{SSI5.6}
\]
Equations (SSI5.3) and (SSI5.4) prove \(f_F\in\mathcal S(\mathbb R)\), not merely a function on the punctured positive axis.

On the line \(\Re s=2\), \(t\mapsto H(2+it)\) is Schwartz by SSI4 and Cauchy's formula. Ordinary Fourier inversion applied to \(x=e^y\) in (SSI5.1) therefore gives
\[
\int_0^\infty f_F(x)x^s\frac{dx}{x}=H(s)
\quad(\Re s=2).
\tag{SSI5.7}
\]
Both sides are holomorphic on \(\Re s>-2\), since \(f_F(x)=O(x^2)\) at zero, and have no poles there. The identity theorem extends (SSI5.7) throughout that half-plane. At \(s=1\), (SSI2.6) gives
\[
\int_{\mathbb R}f_F(x)\,dx=2H(1)=0.
\tag{SSI5.8}
\]
Thus \(f_F\in S\). By (SSI2.3), \(\mathcal M_0\Sigma f_F=2\zeta H=F\) on \(\Re s>1\); both sides are entire, so equality holds on the whole plane. This proves the surjectivity in (SSI1.8).

## SSI6. Continuity of the inverse and endpoint information

For any Schwartz seminorm \(q_{r,j}\), split its domain into \(|x|\ge1\) and \(|x|\le1\). On the first part use (SSI5.3) with \(c\ge\max(2,r+2)\), and a rapid bound for \(H(c+it)\) of order greater than \(j+1\). It yields a constant times one finite seminorm of \(F\). On the second part choose \(N\ge j+1\) in (SSI5.4). The finitely many polynomial coefficients satisfy
\[
|c_k(F)|\le\frac{b_{A_0,0}(F)}{2|\zeta'(-2k)|}
\quad(A_0\ge2N),
\tag{SSI6.1}
\]
and the remainder is bounded by (SSI5.5) and (SSI4.7). Consequently, for suitable finite indices \(A_0,M\) depending on \(r,j\),
\[
q_{r,j}(f_F)\le C_{r,j} b_{A_0,M}(F).
\tag{SSI6.2}
\]
This proves continuity of the inverse. Together with SSI2 and SSI5 it proves the topological isomorphism (SSI1.8). Because \(I\) is closed, the image \(J\) is closed in \(A\).

The endpoint information is more than the two vanishing conditions. Differentiating (SSI5.7), with dominated convergence, and using (SSI2.6) gives
\[
\int_0^\infty f_F(x)\frac{dx}{x}=-F(0),\qquad
\int_0^\infty f_F(x)\log x\,dx=\frac{F(1)}2.
\tag{SSI6.3}
\]
All Taylor coefficients at the original trivial zeros are retained in (SSI5.6). Higher coefficients at these points are obtained by Laurent division of the full original \(F/(2\zeta)\); no substitution by the completed function is required. In particular, the Gamma cancellation in (SSI3.1) did not erase the information that reconstructs the source jet.

In the centered convention of S1–S6, \(\mathcal E f(u)=u^{1/2}\sum_{n\ge1}f(nu)\). Hence \(\Sigma=\mathcal T\mathcal E\), and the strengthened centered statement is
\[
\mathcal M\mathcal E:S\xrightarrow{\sim}I,\qquad
\int_0^\infty f_F^{\rm centered}(x)x^s\frac{dx}{x}
=\frac{F(s)}{\zeta(s)},\qquad
f_F^{\rm centered}=2f_F.
\tag{SSI6.4}
\]
The original Gaussian approximants in S4–S5 therefore converge in Schwartz space to this actual source function: their transforms converge in \(I\), and the continuous inverse just proved carries that convergence to every Schwartz seminorm. This strengthens the older closure statement without invalidating its proof.

## SSI7. An inverse on the counting side and the full Fourier map

For \(b\in J\), the exact inverse can also be written directly in the original counting variable:
\[
\boxed{\Sigma^{-1}b(x)=\frac12\sum_{n\ge1}\mu(n)b(nx)}
\quad(x>0).
\tag{SSI7.1}
\]
For fixed \(x>0\), the sum and all its derivatives converge absolutely and locally uniformly, using the arbitrary decay of \(b\) at infinity. To prove the identity, write \(b=\Sigma f\) by SSI5. Then, for any \(L>1\),
\[
\sum_{n,m\ge1}|f(mnx)|
\le C_{x,L}\sum_{n,m\ge1}(mn)^{-L}<\infty.
\tag{SSI7.2}
\]
The same bound with a sufficiently higher decay order applies to derivatives. Thus sums can be rearranged, and
\[
\frac12\sum_n\mu(n)b(nx)
=\sum_{k\ge1}f(kx)\sum_{n\mid k}\mu(n)=f(x).
\tag{SSI7.3}
\]
The last finite divisor sum is1 at \(k=1\) and0 otherwise, as follows by expanding \(\prod_{p\mid k}(1-1)\). All prime divisors are those already present in the complete arithmetic. This calculation does not posit independent meanings for a few labels before that reconstruction. Formula (SSI7.1) is not asserted to be termwise differentiable at \(x=0\); its smooth extension and its complete jet there are supplied by (SSI5.4)–(SSI5.6).

Let \(Rb(u)=u^{-1}b(u^{-1})\) and \(\jmath F(s)=F(1-s)\). The functional equation, with its nonzero multiplier on the critical strip, pairs all actual nontrivial-zero jets, so \(\jmath I=I\). The exact inverse intertwines the full reflection with Fourier transform:
\[
\Sigma^{-1}Rb=\widehat{\Sigma^{-1}b},\qquad
f_{\jmath F}=\widehat{f_F}.
\tag{SSI7.4}
\]
Proof: (SSI2.2) gives \(R\Sigma f=\Sigma\widehat f\) on \(S\); injectivity proves the first equality. Raw Mellin gives \(\mathcal M_0Rb(s)=\mathcal M_0b(1-s)\), proving the second. Equivalently their positive-axis Mellin transforms satisfy
\[
\int_0^\infty\widehat{f_F}(x)x^s\frac{dx}{x}
=\frac{F(1-s)}{2\zeta(s)}
=\frac{\zeta(1-s)}{\zeta(s)}H(1-s),
\tag{SSI7.5}
\]
as meromorphic identities. The complete functional multiplier is retained in the last quotient and in (SSI3.6); it has not been set equal to1.

For \(a>0\), let \(T_ab(u)=b(u/a)\) and \(D_af(x)=f(x/a)\). Direct summation gives \(\Sigma D_a=T_a\Sigma\), and direct Mellin transformation gives multiplication by \(a^s\). Therefore the inverse is continuously equivariant for every positive dilation. Its derivative \(-x\partial_x\) on \(S\) corresponds to multiplication by \(s\) on \(I\); this follows by differentiating in \(\log a\), or by integration by parts with the endpoint decay already proved. Every multiplicity and nilpotent zero-jet action in the quotient consequently remains unchanged.

## SSI8. Actual cohomology, strict support maps and the vanishing closure quotient

Apply the theorem to the sheaf explicitly constructed in `CC_SUPPORTED_LOCALIZATION_AND_WEIGHT_MAPS.md`, CSL1–CSL9. Its underlying space has opens \(\varnothing,U,U_+,U_-,X\), with \(U=\{\eta\}\), \(U_\pm=\{x_\pm,\eta\}\); its chart spaces are \(V_\pm=S\oplus\mathbb C^2\), overlap \(A\), and restrictions
\[
r_+(f,c_0,c_1)=\Sigma f,\qquad
r_-(h,d_0,d_1)=R\Sigma h.
\tag{SSI8.1}
\]
Each map is a continuous map onto \(J\), with continuous right inverse into its Schwartz summand, and kernel exactly its two endpoint lines. Equation (SSI7.4) proves that the two images are the same closed subspace, with their Fourier comparison retained.

The ordinary Cech complex is
\[
V_+\oplus V_-\xrightarrow{r_+-r_-}A.
\tag{SSI8.2}
\]
Its differential has closed image \(J\); the inverse of \(\Sigma\) gives a continuous right inverse from that image to the first chart summand. Thus this differential is strict onto its image. Ordinary sheaf cohomology, with its quotient topology, is already Hausdorff, and the exact isomorphism is
\[
\boxed{H^1(X,\Omega)=A/J\xrightarrow{\sim}\mathcal B/I,
\quad[b]\longmapsto[\mathcal M_0b].}
\tag{SSI8.3}
\]
In the notation \(C=\overline J\), \(Q_{\rm alg}=A/J\), \(Q_H=A/C\), \(N=C/J\), the previously retained comparison kernel is now calculated:
\[
\boxed{C=J,\qquad N=0,\qquad Q_{\rm alg}\xrightarrow{\sim}Q_H.}
\tag{SSI8.4}
\]
This is an unconditional vanishing of this particular closure quotient. It is not identified with Deligne's lifting-obstruction group.

All supported rows in CSL therefore act on the actual ordinary cohomology, with no additional Hausdorffization step. For one closed point, \(H^1_{\{x_+\}}(X,\Omega)\to H^1(X,\Omega)\) is the identity on \(A/J\); the other chart has the retained orientation minus sign. For both closed points the exact row is
\[
0\longrightarrow Q\xrightarrow{q\mapsto(q,q)}Q\oplus Q
\xrightarrow{(q_+,q_-)\mapsto q_+-q_-}Q\longrightarrow0,
\qquad Q=\mathcal B/I.
\tag{SSI8.5}
\]
The quotient of the generic restriction by its kernel \(J\) is the first \(Q\). The section \(q\mapsto\tfrac12(q,-q)\) is continuous and dilation-equivariant. It is also mirror-equivariant with \(\jmath\) on the first \(Q\), \((q_+,q_-)\mapsto(\jmath q_-,\jmath q_+)\) in the middle, and \(-\jmath\) on the last \(Q\). Substituting into the difference verifies both the section identity and the orientation sign. The scalar \(1/2\) belongs to the already reconstructed coefficient field; it is not an operation on \(\tau\).

The full zeroth cohomology remains the Fourier graph
\[
\{((\widehat h,c_0,c_1),(h,d_0,d_1)):
h\in S,\ c_0,c_1,d_0,d_1\in\mathbb C\}.
\tag{SSI8.6}
\]
Its four endpoint lines retain the unshifted dilation characters \(1,a,a,1\). None is removed by the closed-image theorem. The proof affects the topological comparison kernel in (SSI8.4), not the original nontrivial-zero jets of \(Q\).

## SSI9. Exact scope of the new vanishing result

Every \(F\in I\) now has a unique actual source function, given by (SSI5.1), with its complete expansion (SSI5.4), continuity (SSI6.2), counting inverse (SSI7.1), and Fourier comparison (SSI7.4). This resolves the old image-versus-closure question globally, for every zero and every multiplicity at once. It strengthens S5 and allows the algebraic cohomology and supported maps of CSL to receive the exact quotient \(\mathcal B/I\) directly.

The target requested from Deligne's theorem remains the weight-separated vanishing for the actual \(\tau\)-supported geometric lifting map. In Deligne §3.6, the obstruction receiver is \(H^{2N-i-1}(X_s,E)^\vee(-N)\), and the inertia term is \(H^{i-1}(X_{\bar\eta},E)_I(-1)\). Equations (SSI8.3)–(SSI8.5) construct the analytic receiver and its support maps; they do not insert an identification with those two geometric terms. The present proof does not move any original zero or show \(\Re\rho=1/2\). Its proved new vanishing is precisely \(\overline{\Sigma S}/\Sigma S=0\), with the displayed inverse and preserved endpoint data.

## SSI10. The adelic sector and the alternative source's retained prime directions

The linked source comparison `CC_SHEAF_ORIGINAL_ZETA_COHOMOLOGY.md`, CS0–CS10 including CS2A, has now been read in full. It proves the adelic comparison that SSI0 kept separate. Here are its receiving maps and the additional Fourier and dilation calculation, retaining the source-domain distinction.

The full companion `CC_ENDPOINT_DEFECT_ACTIONS.md`, CSB0–CSB10, has also been read. Its CSB1–CSB9 independently proves these endpoint actions and supplies an exactly Fourier-equivariant Schwartz representative. CSB10 proves the coordinate comparison to the prior FR15–FR25 calculation, whose earlier public source is [Prime boundary classes in the actual adelic theta receiver, PM4–PM15](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/44d03e48849934edf59f645cb5021b639ab31ac4/workbenches/splitzero-tandem/continuations/20260923-original-zeta-return/sources/21_prime_memory_and_actual_theta_receiver.tex). That public source identity was verified; a new complete reading of its earlier base conventions is not claimed. The prime-boundary component is retained programme mathematics. SSI10 receives and checks its maps without claiming discovery of that component.

Put \(K=\widehat{\mathbb Z}^{\times}\). On the moment-null adelic Schwartz space let \(D\) be the Hausdorff quotient by rational differences generated by arbitrary adelic Schwartz functions, and let \(D_{\rm null}\) instead restrict the generators themselves to moment-null functions. Both kinds of difference are moment-null because the adelic modulus of a rational number is1. CS2 proves the continuous inverse maps
\[
j:S\longrightarrow D^K,\quad f\longmapsto[f\otimes1_{\widehat{\mathbb Z}}],
\qquad
\bar B\left[\sum_d f_d\otimes1_{d\widehat{\mathbb Z}}\right](v)
=\sum_d f_d^{\rm ev}(dv).
\tag{SSI10.1}
\]
The radial-ball expansion is finite after \(K\)-averaging. Its uniqueness and the preservation of both endpoint functionals are proved in CS2. Rational scaling takes the ball \(d\widehat{\mathbb Z}\) to \((d/|q|)\widehat{\mathbb Z}\), while scaling the real function by \(|q|\); the two changes cancel in \(B\). This proves that the formula descends to the quotient. The difference between a ball tensor and its displayed real representative is a sum of two full rational differences, as proved in CS2.7a. Thus \(\bar Bj=1\) and \(j\bar B=P_K\), with both inverses continuous.

On the overlap, summation of \(jf\) over \(\mathbb Q^\times\) is exactly \(\Sigma f\): a rational number in \(\widehat{\mathbb Z}\) is an integer, and both signs contribute. Therefore the actual full-difference CC source sector has the continuous isomorphism
\[
D^K\xrightarrow{\ \bar B\ }S
\xrightarrow{\ \Sigma\ }J
\xrightarrow{\ \mathcal M_0\ }I.
\tag{SSI10.2}
\]
The middle isomorphism is SSI1–SSI6; thus this statement now concerns the proved adelic source sector as well as its explicit real presentation.

For the second source convention CS2A constructs
\[
V=\bigoplus_{p\ \mathrm{prime}}\mathbb C^2,
\qquad D_{\rm null}\xrightarrow{\sim}D\oplus V,
\quad[F]_{\rm null}\longmapsto([F],\mathscr LF),
\tag{SSI10.3}
\]
with its continuous inverse and locally convex direct-sum topology. On a ball tensor the components are
\[
\ell_p(f\otimes1_{d\widehat{\mathbb Z}})
=v_p(d)\left(f(0),\ d^{-1}\int_{\mathbb R}f(v)\,dv\right),
\qquad \mathscr L=(\ell_p)_p.
\tag{SSI10.4}
\]
For nonradial inputs average over \(K\) first. All operations in (SSI10.3)–(SSI10.4) concern the complete reconstructed prime system. Each test function has a finite radial-ball expansion, so its image has finite prime support; this property of individual sections is not a truncation of the prime system. CS2A proves that the extra \(V\) is precisely the kernel of the source comparison, not an unspecified possible defect.

Let \(C(a,b)=(b,a)\) on each \(\mathbb C^2\). Under the self-dual adelic Fourier convention, the finite Fourier transform satisfies
\[
\widehat{1_{d\widehat{\mathbb Z}}}
=d^{-1}1_{d^{-1}\widehat{\mathbb Z}}.
\tag{SSI10.5}
\]
Indeed the annihilator of the ball is the displayed reciprocal ball, and its Haar volume is \(d^{-1}\). For a real Schwartz factor the two Fourier endpoint identities are \(\widehat f(0)=\int f\) and \(\int\widehat f=f(0)\). Substitute all these values into (SSI10.4). Since \(v_p(d^{-1})=-v_p(d)\), one obtains
\[
\ell_p(\widehat F)=-C\ell_p(F),\qquad
\boxed{\mathscr L\widehat F=-C\mathscr LF.}
\tag{SSI10.6}
\]
The same identity holds before averaging: Fourier conjugates the action of a finite unit to its inverse, and Haar averaging is unchanged by inversion. Linearity and continuity then extend the calculation from ball tensors to the stated source. Thus (SSI10.3) intertwines Fourier transform with \((\widehat{\phantom F}_D,-C)\). The minus sign records the inverted finite valuation; it cannot be suppressed by only retaining the two unordered endpoint coordinates.

For positive real dilation, define
\[
\rho_+(a)F(v,x_f)=F(v/a,x_f),\qquad
\rho_-(a)F(v,x_f)=aF(av,x_f).
\tag{SSI10.7}
\]
Evaluation at zero and change of variables in the real integral give
\[
\mathscr L\rho_+(a)=
\begin{pmatrix}1&0\\0&a\end{pmatrix}\mathscr L,
\qquad
\mathscr L\rho_-(a)=
\begin{pmatrix}a&0\\0&1\end{pmatrix}\mathscr L.
\tag{SSI10.8}
\]
These formulas hold in every prime summand of \(V\). Consequently the exact splitting (SSI10.3) is equivariant for these displayed actions, without requiring its chosen endpoint section to be equivariant. This also verifies Fourier interchange of the two actions, with the retained \(-C\).

For the sheaves in this note, take the \(K\)-fixed sector explicitly. The group \(K\) acts trivially on \(V\), and (SSI10.3) is \(K\)-equivariant, so it restricts to the topological isomorphism \(D_{\rm null}^K\cong D^K\oplus V\). Define \(\Omega_{\rm null}\) with chart source \(D_{\rm null}^K\), its two endpoint lines on each chart, and the same \(K\)-fixed overlap \(A\) as \(\Omega\). This is not the sheaf containing every nontrivial finite-unit character. Each extra \(V\) class has the representative \(\mathscr T(v)\) constructed in CS2A.7, a finite sum of full rational differences. Its sum vanishes by reindexing. The relation closure also sums to zero by continuity, so the whole \(V\) summand restricts to zero on the overlap. Let \(i_\pm:\{x_\pm\}\hookrightarrow X\). The source comparison therefore gives the actual sheaf decomposition
\[
\Omega_{\rm null}\cong\Omega\oplus(i_+)_*V\oplus(i_-)_*V.
\tag{SSI10.9}
\]
This is verified on both charts, the overlap and their restrictions; hence it is an isomorphism of sheaves. In the two-term Cech complex it adds \(V\oplus V\) in degree0 with zero differential, and adds nothing in degree1. It follows directly that
\[
H^0(X,\Omega_{\rm null})\cong H^0(X,\Omega)\oplus V\oplus V,
\qquad
\boxed{H^1(X,\Omega_{\rm null})\cong H^1(X,\Omega)
\cong\mathcal B/I.}
\tag{SSI10.10}
\]
The same calculation retains one additional \(V\) at the corresponding single closed support. The chart-exchanging sheaf mirror swaps the two \(V\) copies; this is a different typed map from the adelic Fourier map \(-C\) within a source copy in (SSI10.6). Formula (SSI10.8) gives their separate endpoint characters. Thus the extra prime directions are preserved, while the degree-one original-zeta quotient remains exactly the same. This identifies the consequence of the source-domain choice without confusing it with the vanished closure quotient or the still-unproved geometric weight separation.
