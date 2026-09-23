# Explicit tails for the original test at time 1/32

Date: 2026-09-23. This is an independent derivation for the original source and filter in ER2, ER27, ER34, and ER39–40 of `../endpoint_resonance_20260923/ENDPOINT_RESONANCE_AND_PRIME_CLASS.tex`.

## Source and reading record

The source file was read in full. The calculations below use its exact theta density (ER2), actual test (ER27), differential filter and convolution (ER34), and complete arithmetic and Gamma pairing (ER39–40). The human source identified there is Brad Rodgers and Terence Tao, *The de Bruijn–Newman constant is non-negative*, [arXiv:1801.05914v5](https://arxiv.org/abs/1801.05914v5), original-source equation identifiers `phidef` and `htdef`. This independent derivation read the programme file containing those formulas; it does not claim a new reading of the original author source archive. The explicit-formula convention is the one already proved in ER39–40, with Alain Connes's [original paper](https://arxiv.org/abs/math/9811068v1), Appendix II, cited there.

No hypothesis on the positions of zeta zeros, no numerical zero list, and no completed-function substitution enters any bound below. The displayed inequalities majorize the original functions for error control. They do not change the functions used in the pairing.

## 1. Original definitions and uniform derivative moments

Throughout this note the heat time is exactly

\[
t=\frac1{32},\qquad \frac1{4t}=8,\qquad \frac1{2t}=16.
\]

Retain the entire original density

\[
\Phi(u)=\sum_{n=1}^{\infty}
\bigl(2\pi^2n^4e^{9u}-3\pi n^2e^{5u}\bigr)
e^{-\pi n^2e^{4u}},\qquad u\ge0,
\]

and define

\[
H(x)=\int_0^\infty e^{u^2/32}\Phi(u)\cos(xu)\,du,
\qquad
M_j=\int_0^\infty u^j e^{u^2/32}\Phi(u)\,du
\quad(j\ge0).
\tag{TB1}
\]

Each original summand is strictly positive because
\(2\pi n^2e^{4u}>3\). In an upper bound it is therefore legitimate to use

\[
0<\Phi(u)\le2\pi^2\sum_{n\ge1}n^4e^{9u}e^{-\pi n^2e^{4u}}.
\tag{TB2}
\]

This inequality retains the negative summand in the definition TB1; it records its sign explicitly when estimating the full sum. For every \(u\ge0\), the exponential series gives

\[
e^{4u}\ge1+4u+8u^2.
\]

Since \(\pi>3\), \(\pi^2<10\), and \(8\pi n^2-1/32>0\),

\[
\begin{aligned}
\frac{u^2}{32}+9u-\pi n^2e^{4u}
&\le-\pi n^2-(4\pi n^2-9)u-(8\pi n^2-1/32)u^2\\
&\le-3n^2-(12n^2-9)u.
\end{aligned}
\]

Tonelli's theorem applies to the nonnegative majorant, and hence

\[
\begin{aligned}
M_j
&\le20j!\sum_{n\ge1}\frac{n^4e^{-3n^2}}{(12n^2-9)^{j+1}}\\
&\le\frac{20j!}{3^{j+1}}\sum_{n\ge1}n^{2-2j}e^{-3n^2}
\le\frac{20j!}{3^{j+1}}\sum_{n\ge1}n^2e^{-3n^2}.
\end{aligned}
\tag{TB3}
\]

Here \(12n^2-9\ge3n^2\). The elementary estimate

\[
\sum_{n\ge1}n^2e^{-3n^2}<\frac1{20}
\tag{TB4}
\]

can be checked entirely with rational arithmetic. Indeed,

\[
e^3>\sum_{j=0}^{10}\frac{3^j}{j!}
=\frac{899569}{44800}>\frac{2007}{100}>20.
\]

For \(n\ge2\), \(n^2\ge1+3(n-1)\). Put \(q=1/8000\). Then

\[
\begin{aligned}
\sum_{n\ge1}n^2e^{-3n^2}
&<\frac{100}{2007}+\frac1{20}\sum_{n\ge2}n^2q^{n-1}\\
&=\frac{100}{2007}+\frac1{20}
\left(\frac{1+q}{(1-q)^3}-1\right)\\
&=\frac{1024129791832007}{20543974083319860}<\frac1{20}.
\end{aligned}
\]

The rational generating-function identity follows by differentiating \(\sum_{n\ge0}q^n=(1-q)^{-1}\) twice within \(|q|<1\). Consequently

\[
\boxed{M_j\le\frac{j!}{3^{j+1}},\qquad
|H^{(j)}(x)|\le M_j\quad(x\in\mathbb R, j\ge0).}
\tag{TB5}
\]

The same integrable bounds justify differentiating TB1 under the integral sign. In particular, \(H\) is real and even, \(M_0=H(0)>0\), and \(H''(0)=-M_2<0\).

## 2. The actual filtered function and its derivatives

Retain the functions

\[
h(x)=e^{-8x^2}H(x)\cos(16x),\qquad
f(x)=h''(x)-\frac14h(x),\qquad
k(x)=\int_{\mathbb R}f(y)f(x-y)\,dy.
\tag{TB6}
\]

Direct differentiation, with the \(-h/4\) term included, gives the exact formula

\[
\begin{aligned}
f(x)=e^{-8x^2}\bigl\{&
[(256x^2-1089/4)H(x)-32xH'(x)+H''(x)]\cos(16x)\\
&+[512xH(x)-32H'(x)]\sin(16x)\bigr\}.
\end{aligned}
\tag{TB7}
\]

Thus, with \(r=|x|\), TB5 implies

\[
\begin{aligned}
|f(x)|
&\le e^{-8x^2}
\left[(256r^2+512r+1089/4)M_0+(32r+32)M_1+M_2\right]\\
&\le e^{-8x^2}\left(\frac{10193}{108}+\frac{1568}{9}r+\frac{256}{3}r^2\right)\\
&\le(95+175r+86r^2)e^{-8x^2}
\le(183+174x^2)e^{-8x^2}.
\end{aligned}
\tag{TB8}
\]

The last inequality uses \(175r\le(175/2)(1+r^2)\). Also,
\(re^{-4r^2}\le1/4\) and \(r^2e^{-4r^2}\le1/10\), because \(e>5/2\). Therefore

\[
\boxed{|f(x)|\le148e^{-4x^2}.}
\tag{TB9}
\]

Here is a finite formula giving all required derivative bounds without omitting any derivative of \(H\). Define positive polynomials

\[
T_m(r)=\sum_{a=0}^{\lfloor m/2\rfloor}
\frac{m!\,8^a\,16^{m-2a}}{a!(m-2a)!}(1+r)^{m-2a},
\]

\[
S_m(r)=\sum_{\ell=0}^{m}\binom m\ell
\frac{\ell!}{3^{\ell+1}}T_{m-\ell}(r),\qquad
B_j(r)=S_{j+2}(r)+\frac14S_j(r).
\tag{TB10}
\]

To prove their bounds, let \(a(x)=e^{-8x^2+16ix}\). Its exact derivative polynomial is

\[
a^{(m)}(x)=a(x)
\sum_{b=0}^{\lfloor m/2\rfloor}
\frac{m!(-8)^b}{b!(m-2b)!}(-16x+16i)^{m-2b}.
\tag{TB11}
\]

This follows by taking the coefficient of \(z^m\) in
\(a(x+z)=a(x)\exp[(-16x+16i)z-8z^2]\).
Since \(|-16x+16i|\le16(1+r)\), TB11 gives
\(|a^{(m)}(x)|\le e^{-8x^2}T_m(r)\).
Leibniz's rule, TB5, and \(h=\Re(aH)\) prove

\[
|h^{(m)}(x)|\le e^{-8x^2}S_m(r),\qquad
\boxed{|f^{(j)}(x)|\le e^{-8x^2}B_j(r).}
\tag{TB12}
\]

For convenient integer ceilings,

\[
\boxed{|f^{(j)}(x)|\le C_j e^{-4x^2}\quad(0\le j\le4),}
\tag{TB13}
\]

with the following constants:

| \(j\) | \(C_j\) |
|---:|---:|
| 0 | 148 |
| 1 | 3,350 |
| 2 | 81,000 |
| 3 | 2,050,000 |
| 4 | 54,500,000 |

For a reproducible rational verification, if \(B_j(r)=\sum_pb_{jp}r^p\), use

\[
(d_0,d_1,d_2,d_3,d_4,d_5,d_6)
=\left(1,\frac14,\frac1{10},\frac3{50},\frac1{25},\frac1{32},\frac{27}{1000}\right).
\]

For \(0\le p\le6\), \(r^pe^{-4r^2}\le d_p\): the maximum for \(p>0\) is
\((p/(8e))^{p/2}\), and the displayed rational ceilings follow from \(e>5/2\), including \(\sqrt{3/20}<2/5\) for \(p=3\). Substituting TB10 gives the exact upper sums

\[
\left(\sum_pb_{jp}d_p\right)_{j=0}^4
=\left(
\frac{79093}{540},
\frac{9042119}{2700},
\frac{327148231}{4050},
\frac{24888564437}{12150},
\frac{1653729054454}{30375}
\right).
\]

Each is less than its corresponding \(C_j\), proving the table.

## 3. Convolution bounds with the original Gaussian exponent retained

The identity

\[
y^2+(x-y)^2=\frac{x^2}{2}+2(y-x/2)^2
\tag{TB14}
\]

and TB9 first give

\[
|k(x)|\le148^2\sqrt{\frac\pi8}\,e^{-2x^2}
<14000e^{-2x^2}.
\tag{TB15}
\]

A stronger tail bound follows by convolving the final polynomial in TB8. Put \(a=183\), \(b=174\), and \(z=y-x/2\). Integrating all terms, including the negative quadratic contribution of \(y^2(x-y)^2\), gives

\[
\begin{aligned}
|k(x)|
&\le\frac{\sqrt\pi}{4}e^{-4x^2}
\left[a^2+ab\left(\frac{x^2}{2}+\frac1{16}\right)
+b^2\left(\frac{x^4}{16}-\frac{x^2}{64}+\frac3{1024}\right)\right]\\
&=\frac{\sqrt\pi}{4}e^{-4x^2}
\left(\frac{9105363}{256}+\frac{247167}{16}x^2+\frac{7569}{4}x^4\right)\\
&\le Q(x)e^{-4x^2},\qquad
\boxed{Q(x)=16000+6900x^2+850x^4.}
\end{aligned}
\tag{TB16}
\]

Indeed, for the Gaussian \(e^{-16z^2}\), its total mass is \(\sqrt\pi/4\), its second moment divided by that mass is \(1/32\), and its fourth moment divided by that mass is \(3/1024\). This proves the first line. The classical elementary bound \(\pi<22/7<256/81\) implies \(\sqrt\pi/4<4/9\). Multiplying the three coefficients by \(4/9\) gives respectively \(15807.921875\), \(6865.75\), and \(841\), each below the corresponding integer in \(Q\). The terminating decimals here are exact rational values.

Differentiation under the convolution integral is justified by TB13. One may put any selected derivatives on either factor. In particular,

\[
k'=f'*f,\quad k''=f'*f',\quad
k'''=f''*f',\quad k^{(4)}=f''*f''.
\]

Using \(\sqrt{\pi/8}<63/100\) and TB13 gives

\[
|k^{(j)}(x)|\le D_j e^{-2x^2},\quad 0\le j\le4,
\tag{TB17}
\]

where

\[
(D_0,D_1,D_2,D_3,D_4)
=(14000,313000,7100000,171000000,4140000000).
\]

For example the pre-ceiling constants are
\((63/100)148^2\), \((63/100)148\cdot3350\),
\((63/100)3350^2\), \((63/100)81000\cdot3350\), and
\((63/100)81000^2\), respectively.

Both \(f\) and \(k\) are real and even. The original value satisfies

\[
k(0)=\int_{\mathbb R}f(y)^2\,dy>0,
\]

because TB7 gives \(f(0)=-M_2-(1089/4)M_0<0\). Also,

\[
k(0)-k(x)=\frac12\int_{\mathbb R}[f(y)-f(y-x)]^2\,dy\ge0.
\tag{TB18}
\]

Expanding the square proves the identity, since translation preserves the two square integrals and evenness converts the cross integral to \(k(x)\). By the fundamental theorem of calculus, Cauchy–Schwarz, and Tonelli,

\[
0\le k(0)-k(x)\le\frac{x^2}{2}\int_{\mathbb R}|f'(y)|^2\,dy
\le\frac{D_2x^2}{2}.
\tag{TB19}
\]

The final inequality follows either directly from TB13 or from the constants used in TB17.

## 4. Prime tail, including every prime power

For an integer \(N\ge3\), define the actual omitted arithmetic term

\[
P_{>N}=2\sum_{n>N}\frac{\Lambda(n)}{\sqrt n}k(\log n),
\quad \Lambda(p^a)=\log p\ (a\ge1),
\quad \Lambda(n)=0\text{ otherwise}.
\tag{TB20}
\]

The elementary inequality \(0\le\Lambda(n)\le\log n\) holds at every integer, including all prime powers. Put

\[
L=\log N,\quad c=8L-\frac12,
\quad
\mathcal T_p(L,c)=\sum_{j=0}^{p}\binom pj
\frac{L^{p-j}j!}{c^{j+1}}.
\tag{TB21}
\]

Then

\[
\boxed{
|P_{>N}|\le
2e^{-4L^2+L/2}
\left[16000\mathcal T_1(L,c)
+6900\mathcal T_3(L,c)
+850\mathcal T_5(L,c)\right].}
\tag{TB22}
\]

Here is the complete sum-to-integral justification. For \(u\ge1\), the logarithmic derivative of
\(uQ(u)e^{-4u^2-u/2}\) is

\[
\frac1u+\frac{Q'(u)}{Q(u)}-8u-\frac12
\le\frac5u-8u-\frac12<0.
\]

The inequality \(uQ'(u)\le4Q(u)\) follows directly from the three positive terms in TB16. Since \(N\ge3>e\), the nonnegative function
\((\log x)x^{-1/2}Q(\log x)e^{-4(\log x)^2}\)
decreases for \(x\ge N\). Consequently TB16 and the integral comparison for a decreasing function yield

\[
|P_{>N}|
\le2\int_N^\infty(\log x)x^{-1/2}Q(\log x)e^{-4(\log x)^2}\,dx
=2\int_L^\infty uQ(u)e^{-4u^2+u/2}\,du.
\]

For \(u=L+v\), the exponent is exactly

\[
-4u^2+u/2=-4L^2+L/2-cv-4v^2.
\]

Bounding \(e^{-4v^2}\le1\), expanding each of \((L+v)^1,(L+v)^3,(L+v)^5\), and using
\(\int_0^\infty v^je^{-cv}\,dv=j!/c^{j+1}\) proves TB22. It also proves absolute convergence independently of any information about zeros or prime density.

A useful completely rational cutoff consequence is

\[
\boxed{|P_{>64}|<10^{-21}.}
\tag{TB23}
\]

To verify it, \(e<11/4\) implies \(e^4<(11/4)^4<64\), hence \(\log64>4\). One elementary proof of the bound on \(e\) is

\[
e=\sum_{j=0}^3\frac1{j!}+\sum_{j\ge4}\frac1{j!}
\le\frac83+\frac1{24}\sum_{j\ge0}5^{-j}
=\frac{87}{32}<\frac{11}{4}.
\]

Increase the integral majorant's domain from \([\log64,\infty)\) to \([4,\infty)\). Applying TB22's polynomial integration with \(L=4\), \(c=63/2\), its coefficient in front of \(e^{-62}\) is exactly

\[
2[16000\mathcal T_1(4,63/2)+6900\mathcal T_3(4,63/2)+850\mathcal T_5(4,63/2)]
=\frac{1882788609056000}{20841167403}<100000.
\]

Finally \(e^{62}>e^{60}>20^{20}>10^{26}\), proving TB23. Every original arithmetic term with \(n\le64\), including powers of primes, remains in the finite calculation.

## 5. Gamma integral: the combined numerator, endpoint, and tail

For the original even convolution, ER40's Gamma integral is

\[
\int_0^\infty
\frac{e^{-x}k(0)-e^{-x/4}k(x/2)}{1-e^{-x}}\,dx.
\tag{TB24}
\]

The prefactor in the full archimedean term remains
\(-(\gamma_{\rm E}+\log\pi)k(0)\), exactly as in ER40.
The combined numerator can be written exactly as

\[
(e^{-x}-e^{-x/4})k(0)+e^{-x/4}[k(0)-k(x/2)].
\tag{TB25}
\]

By TB19 the second bracket is between zero and \(D_2x^2/8\). Since
\((e^{-x}-e^{-x/4})/x\to-3/4\) and \((1-e^{-x})/x\to1\), the integrand has the definite endpoint value

\[
\boxed{\lim_{x\downarrow0}
\frac{e^{-x}k(0)-e^{-x/4}k(x/2)}{1-e^{-x}}
=-\frac34k(0).}
\tag{TB26}
\]

In particular no individual divergent integral has been used at zero. More explicitly, for \(0<x\le1\),
\(|e^{-x}-e^{-x/4}|\le3x/4\) and \(1-e^{-x}\ge x/2\), so the absolute value of the original integrand is at most
\(3k(0)/2+D_2x/4\). This proves its local integrability with a stated majorant.

For any \(T>0\), the actual tail admits the exact decomposition

\[
\begin{aligned}
G_{>T}
&=\int_T^\infty
\frac{e^{-x}k(0)-e^{-x/4}k(x/2)}{1-e^{-x}}\,dx\\
&=-k(0)\log(1-e^{-T})-\mathcal R_T,\\
\mathcal R_T
&=\int_T^\infty\frac{e^{-x/4}k(x/2)}{1-e^{-x}}\,dx.
\end{aligned}
\tag{TB27}
\]

The first term follows by the substitution \(v=e^{-x}\). It can be retained exactly in a finite-interval evaluation. Neither the sign of \(k(x/2)\) nor that of \(\mathcal R_T\) is assumed.

Using TB16, put \(d=2T+1/4\) and use \(\mathcal T_p\) from TB21. Then

\[
\boxed{
|\mathcal R_T|\le
\frac{e^{-T^2-T/4}}{1-e^{-T}}
\left[16000\mathcal T_0(T,d)
+1725\mathcal T_2(T,d)
+\frac{425}{8}\mathcal T_4(T,d)\right].}
\tag{TB28}
\]

Indeed,

\[
|k(x/2)|\le
\left(16000+1725x^2+\frac{425}{8}x^4\right)e^{-x^2},
\]

and \((1-e^{-x})^{-1}\le(1-e^{-T})^{-1}\) for \(x\ge T\). Under \(x=T+v\), the complete exponent is
\(-T^2-T/4-dv-v^2\). Bounding its last factor by one and integrating the expanded polynomial gives TB28.

In particular,

\[
\boxed{G_{>8}=-k(0)\log(1-e^{-8})-\mathcal R_8,
\qquad |\mathcal R_8|<10^{-23}.}
\tag{TB29}
\]

For the rational check, \(d=65/4\), and the bracket in TB28 is

\[
16000\mathcal T_0(8,65/4)+1725\mathcal T_2(8,65/4)
+\frac{425}{8}\mathcal T_4(8,65/4)
=\frac{1006957513344}{46411625}.
\]

Its double is less than \(100000\); also \((1-e^{-8})^{-1}<2\). Since \(e^{66}>20^{22}>10^{28}\), TB28 is less than \(100000/10^{28}=10^{-23}\). Thus the finite Gamma integral over \([0,8]\), its endpoint value TB26, the exact term \(-k(0)\log(1-e^{-8})\), and the bound on \(\mathcal R_8\) keep all original archimedean contributions.

For a shorter but weaker bound, TB15 gives

\[
|\mathcal R_T|\le
\frac{14000e^{-T^2/2-T/4}}{(1-e^{-T})(T+1/4)}.
\tag{TB30}
\]

This follows from
\(x^2/2+x/4\ge T^2/2+T/4+(T+1/4)(x-T)\).
If the exact first term in TB27 is not evaluated, add
\(k(0)[-\log(1-e^{-T})]\) to either TB28 or TB30 to bound \(|G_{>T}|\).

## 6. Exact constant-plus-remainder comparison requested by the receiving calculation

This section verifies the root calculation's comparison with its full residual. Put

\[
C=H(0)=M_0,\qquad R(x)=H(x)-C,
\]

\[
f_0(x)=Ce^{-8x^2}
[(256x^2-1089/4)\cos(16x)+512x\sin(16x)],
\qquad e_f(x)=f(x)-f_0(x).
\tag{TB31}
\]

The identity \(H'(0)=0\), Taylor's integral formula, and TB1 give

\[
|R(x)|\le\frac{M_2x^2}{2},\quad
|R'(x)|\le M_2|x|,\quad
|R''(x)|\le M_2,\quad
|R'''(x)|\le M_3.
\tag{TB32}
\]

Substitution into the exact formula TB7 gives

\[
\begin{aligned}
e_f(x)=e^{-8x^2}\bigl\{&
[(256x^2-1089/4)R-32xR'+R'']\cos(16x)\\
&+[512xR-32R']\sin(16x)\bigr\},
\end{aligned}
\tag{TB33}
\]

and therefore

\[
\boxed{|e_f(x)|\le M_2e^{-8x^2}E(|x|),\quad
E(r)=1+32r+\frac{1345}{8}r^2+256r^3+128r^4.}
\tag{TB34}
\]

For example the quadratic coefficient is exactly
\(1089/8+32=1345/8\), retaining both the original \(-1089/4\) filter coefficient and the derivative term \(-32xR'\).

Differentiating TB33 gives the exact coefficients

\[
\begin{aligned}
e_f'(x)=e^{-8x^2}\bigl\{&
[(13060x-4096x^3)R+(768x^2-3265/4)R'
-48xR''+R''']\cos(16x)\\
&+[(4868-12288x^2)R+1536xR'-48R'']\sin(16x)\bigr\}.
\end{aligned}
\tag{TB35}
\]

Using all four TB32 bounds yields

\[
\boxed{|e_f'(x)|\le e^{-8x^2}[M_2E_1(|x|)+M_3],}
\tag{TB36}
\]

\[
E_1(r)=48+\frac{3457}{4}r+3970r^2+7298r^3+6144r^4+2048r^5.
\]

Alternatively \(H'''(0)=0\) and \(|H^{(4)}|\le M_4\) give
\(|R'''(x)|\le M_4|x|\); the final \(M_3\) in TB36 may then be replaced by \(M_4|x|\) when that yields a smaller integrated bound.

Let \(k_0=f_0*f_0\) denote the comparison convolution only in this section, and let \(\Delta=k-k_0\). Since
\(\Delta=f_0*e_f+e_f*f_0+e_f*e_f\), Cauchy–Schwarz gives the global bounds

\[
\begin{aligned}
|\Delta(x)|&\le2\|f_0\|_2\|e_f\|_2+\|e_f\|_2^2=:\delta_0,\\
|\Delta''(x)|&\le2\|f_0'\|_2\|e_f'\|_2+\|e_f'\|_2^2=:\delta_2.
\end{aligned}
\tag{TB37}
\]

All functions are real and even except their odd derivatives, so \(\Delta'(0)=0\). Consequently

\[
|\Delta(x)-\Delta(0)|\le\frac{\delta_2x^2}{2},
\qquad
|\Delta(x)-\Delta(0)|\le2\delta_0.
\tag{TB38}
\]

These bounds are statements about the exact residual; the original \(H\), \(f\), and \(k\) remain those of TB1 and TB6. Every norm bound supplied by TB34 or TB36 is a finite sum of exact Gaussian moments. Specifically, for integers \(m\ge0\),

\[
\int_{\mathbb R}|x|^m e^{-16x^2}\,dx
=16^{-(m+1)/2}\Gamma\left(\frac{m+1}{2}\right).
\tag{TB39}
\]

This follows from \(v=16x^2\) on each half-line; the Gamma factor and the full power of 16 have both been retained. Squaring the polynomials in TB34 and TB36 and applying TB39 yields computable certified bounds for \(\|e_f\|_2\) and \(\|e_f'\|_2\). No sign for the full pairing is claimed by these estimates.

## 7. Certified tails for direct evaluation of the original moments

For each \(j\in\{0,2,3,4\}\), retain the exact finite integral

\[
M_j^{[16,3]}=\int_0^3u^je^{u^2/32}
\sum_{n=1}^{16}(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})
e^{-\pi n^2e^{4u}}\,du.
\tag{TB40}
\]

We prove, with ample margin,

\[
\boxed{0<M_j-M_j^{[16,3]}<10^{-300}.}
\tag{TB41}
\]

All original summands are positive, so the left inequality holds. The omitted domain is contained in the union of all indices with \(u\ge2\) and the indices \(n\ge17\) with all \(u\ge0\). Bounding those two sets separately is sufficient even though their intersection is counted twice.

First let \(u=2+v\), \(v\ge0\). Since \(e^3>20\),
\(e^8>e^6>400\), and hence

\[
e^{4u}=e^8e^{4v}>400(1+4v+8v^2).
\]

Keeping every term in the original exponent before estimating it, we obtain

\[
\begin{aligned}
\frac{u^2}{32}+9u-\pi n^2e^{4u}
&\le\frac{145}{8}-1200n^2
-\left(4800n^2-\frac{73}{8}\right)v
-\left(9600n^2-\frac1{32}\right)v^2\\
&\le-1180n^2-v.
\end{aligned}
\tag{TB42}
\]

The last line uses \(145/8\le20n^2\),
\(4800n^2-73/8\ge1\), and positivity of the final quadratic coefficient. For \(j\le4\), \((2+v)^j\le(2+v)^4\), and

\[
\int_0^\infty(2+v)^4e^{-v}\,dv
=16+32+48+48+24=168.
\]

The same majorant TB2 therefore yields

\[
\int_2^\infty u^je^{u^2/32}\Phi(u)\,du
\le3360\sum_{n\ge1}n^4e^{-1180n^2}.
\]

Since \(n^2\ge1+3(n-1)\), put \(q=e^{-3540}<1/2\). Differentiating the geometric series gives

\[
\sum_{n\ge1}n^4q^{n-1}
=\frac{1+11q+11q^2+q^3}{(1-q)^5}<300.
\]

It follows that

\[
\int_2^\infty u^je^{u^2/32}\Phi(u)\,du
<1008000e^{-1180}<10^{-383}.
\tag{TB43}
\]

For the last numerical inequality, \(e^{1180}>e^{1170}>(20)^{390}>10^{390}\) and \(1008000<10^7\). This also bounds the smaller integral from \(u=3\).

For the index tail, the first two lines of TB3 applied only to \(n\ge17\) give

\[
\begin{aligned}
&\int_0^\infty u^je^{u^2/32}
\sum_{n\ge17}(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})
e^{-\pi n^2e^{4u}}\,du\\
&\hspace{2em}\le\frac{20j!}{3^{j+1}}\sum_{n\ge17}n^2e^{-3n^2}.
\end{aligned}
\tag{TB44}
\]

Write \(n=17+a\), \(a\ge0\) an integer. Then
\(n^2=289+34a+a^2\ge289+35a\). With \(q=e^{-105}<1/2\),

\[
\begin{aligned}
\sum_{n\ge17}n^2e^{-3n^2}
&\le e^{-867}\sum_{a\ge0}(17+a)^2q^a\\
&=e^{-867}\left[\frac{289}{1-q}
+\frac{34q}{(1-q)^2}+\frac{q(1+q)}{(1-q)^3}\right]\\
&<652e^{-867}.
\end{aligned}
\]

For each requested \(j\), \(20j!/3^{j+1}\le20/3\), so TB44 is less than \(10000e^{-867}<10^{-369}\). Indeed,

\[
e^{867}>20^{289}=2^{289}10^{289}
>2^{280}10^{289}>10^{84}10^{289}=10^{373},
\]

using \(2^{10}>10^3\). Together TB43 and TB44 prove
\(M_j-M_j^{[16,3]}<10^{-383}+10^{-369}<10^{-300}\), which is TB41. Thus adding a symmetric ball of radius \(10^{-300}\) to a rigorous enclosure of TB40 encloses the exact original moment. No estimate of the finite integral itself is substituted for its certified integration.

## 8. Independent derivation of the comparison convolution and certificate checks

Retain the comparison source from TB31,
\(h_0(x)=Ce^{-8x^2}\cos(16x)\), so
\(f_0=(D^2-1/4)h_0\). The cosine product identity and TB14 give

\[
\begin{aligned}
(h_0*h_0)(x)
&=\frac{C^2}{2}e^{-4x^2}
\int_{\mathbb R}e^{-16z^2}[\cos(32z)+\cos(16x)]\,dz\\
&=\frac{C^2\sqrt\pi}{8}e^{-4x^2}
[e^{-16}+\cos(16x)].
\end{aligned}
\tag{TB45}
\]

The Gaussian Fourier integral here is
\(\int e^{-16z^2}\cos(32z)\,dz=(\sqrt\pi/4)e^{-16}\), with its full exponential factor retained. Since all sources and their derivatives have Gaussian decay, differentiating under convolution and integrating by parts give

\[
k_0=f_0*f_0=(D^2-1/4)^2(h_0*h_0).
\]

For an algebraic verification, put \(q=-8x+16i\). For \(a(x)=e^{-4x^2+16ix}\),

\[
D^2a=(q^2-8)a,\qquad
D^4a=(q^4-48q^2+192)a,
\]

and hence

\[
(D^2-1/4)^2a
=\left(q^4-\frac{97}{2}q^2+\frac{3137}{16}\right)a.
\]

The same identity with \(q=-8x\) applies to \(e^{-4x^2}\). Expanding the real and imaginary parts proves exactly

\[
\boxed{\begin{aligned}
k_0(x)=\frac{C^2\sqrt\pi}{128}e^{-4x^2}\bigl[&
(65536x^4-1622528x^2+1250369)\cos(16x)\\
&+2048x(256x^2-1121)\sin(16x)\\
&+e^{-16}(65536x^4-49664x^2+3137)\bigr].
\end{aligned}}
\tag{TB46}
\]

This is the exact expression used in `certify_pairing.py`; `K0_EXACT.txt` contains the same expression with its common factor \(C^2\) handled by the script.

The polynomial envelopes for the comparison function and derivative are

\[
\begin{aligned}
|f_0(x)|&\le Ce^{-8x^2}A(|x|),
&A(r)&=\frac{1089}{4}+512r+256r^2,\\
|f_0'(x)|&\le Ce^{-8x^2}B(|x|),
&B(r)&=4868+13060r+12288r^2+4096r^3.
\end{aligned}
\tag{TB47}
\]

TB31 proves the first bound; TB35 with \(R=C\) constant proves the second derivative formula, or it follows by direct differentiation of TB31. TB39 computes the squared envelope norms exactly. Since \(C=M_0\le1/3\), the envelope for \(f_0\) is bounded by the envelope TB8 used for \(f\). Therefore the universal convolution and Gamma-tail bounds TB16 and TB29 apply to \(k_0\) as well.

For clarity, the script's additional error expressions have the following rigorous justifications.

For \(0<\varepsilon\le1\), the omitted origin interval of the Gamma integral of \(k_0\) has absolute value at most

\[
\frac32k_0(0)\varepsilon
+\frac{\|f_0'\|_2^2\varepsilon^2}{8}.
\tag{TB48}
\]

This is the integration of the TB25 majorant using
\(0\le k_0(0)-k_0(x/2)\le\|f_0'\|_2^2x^2/8\)
and \(1-e^{-x}\ge x/2\). Any upper bound for \(\|f_0'\|_2\), such as TB47, is valid in TB48.

Let \(\Delta=k-k_0\), with the exact residual bounds \(\delta_0,\delta_2\) from TB37. For \(0<h\le1\), the complete Gamma functional difference satisfies

\[
\begin{aligned}
|A_\infty(k)-A_\infty(k_0)|
\le{}&\left[\gamma_{\rm E}+\log\pi+\frac32
+4\log\frac1h
+\frac{e^{-1}+4e^{-1/4}}{1-e^{-1}}\right]\delta_0
+\frac{\delta_2h^2}{8}.
\end{aligned}
\tag{TB49}
\]

To verify every interval in this bound, on \((0,1]\) write the Gamma numerator difference exactly as

\[
(e^{-x}-e^{-x/4})\Delta(0)
+e^{-x/4}[\Delta(0)-\Delta(x/2)].
\]

The first part integrates to at most \(3\delta_0/2\), by
\(|e^{-x}-e^{-x/4}|\le3x/4\) and \(1-e^{-x}\ge x/2\). For the second part use
\(|\Delta(0)-\Delta(x/2)|\le\delta_2x^2/8\) on \((0,h]\), yielding \(\delta_2h^2/8\), and use \(2\delta_0\) on \([h,1]\), yielding \(4\delta_0\log(1/h)\). On \([1,\infty)\) use the original numerator directly to get
\(\delta_0\int_1^\infty(e^{-x}+e^{-x/4})/(1-e^{-1})\,dx\).
Its value is the last coefficient in TB49. The retained prefactor contributes \((\gamma_{\rm E}+\log\pi)\delta_0\). This proves the script's full Gamma error at \(h=1/16\).

Finally, for \(x\ge0\), define the exact envelope integral

\[
\mathcal C_{P,Q}(x)=\int_{\mathbb R}e^{-16z^2}
P(|z|+x/2)Q(|z|+x/2)\,dz,
\]

where \(P,Q\) have nonnegative coefficients. Under \(y=x/2+z\), both \(|y|\) and \(|x-y|\) are at most \(|z|+x/2\). Therefore TB34 and TB47 give

\[
|\Delta(x)|\le e^{-4x^2}
[2CM_2\mathcal C_{A,E}(x)+M_2^2\mathcal C_{E,E}(x)].
\tag{TB50}
\]

The script expands these positive polynomials and integrates every power with TB39. Multiplying TB50 at \(x=\log n\) by \(2\Lambda(n)/\sqrt n\) and summing over all prime powers \(2\le n\le64\) gives the stated finite prime error. The remaining original prime tail is bounded by TB23.

Thus the exact-convolution formula, original-source moment tails, derivative residuals, finite prime error, origin error, and Gamma error used by the certificate all have independent proofs here. This audit inspected the mathematics and script expressions; it did not rerun the numerical Weil-pairing calculation or independently assert its final numerical enclosure.

## Derivation log

1. Read the programme source file, with particular attention to the exact variables, heat time, filter, convolution, prime factor two, and Gamma numerator.
2. Derived the all-orders moment bound TB5 from the complete original density by positive majorants; kept the source's negative summand explicit in TB1–2.
3. Expanded the actual differential filter and derived the polynomial and Gaussian bounds TB7–17.
4. Proved the arithmetic sum-to-integral comparison, retaining all prime powers, and the rational cutoff TB23.
5. Split the Gamma tail only for a strictly positive lower endpoint, evaluated its \(k(0)\) contribution exactly, and proved TB26–30.
6. Independently verified the receiving calculation's residual polynomial and supplied the derivative residual, TB31–39.
7. Evaluated the displayed rational coefficient identities with Python's exact `fractions.Fraction`; the proofs also specify the finite formulas from which each coefficient can be reproduced.
8. Proved TB40–44 for the requested original moment truncation, with tails strictly smaller than the script's radius \(10^{-300}\).
9. Read `certify_pairing.py`, `K0_EXACT.txt`, and the current `CERTIFICATE.json`; independently derived TB45–50 and checked each mathematical error expression used by the script. No numerical pairing was rerun.

No publication, remote mutation, rendering, source indexing, numerical Weil-pairing evaluation, or assertion of its sign was performed by this derivation.
