# Independent review of the growing-degree Gamma return bounds

Verdict: **PASS. No mathematical repair required for RWB1–27.**

Reviewed in full: `recurrence_bounds.tex`, SHA256 `580f282cb2be5225383da4913dec33810d5482a5d02097ed594173f0bc70b87f`. The source was not edited. This review checks the written mathematical proof, including its analytic justifications, original polynomial spaces, all endpoint multiplicities and its uniform numerical constants. It asserts no PDF build, visual review, Lean execution or publication.

The exact HCT/PHT/LET sources already read for `REVIEW_PRODUCT.md` supply the original measure, norm identities, orthogonal polynomial recurrence and receiving signs. Their pinned hashes remain in that review. In particular HCT1, HCT5–6, HCT9–13, HCT33–37, PHT20–23 and LET19–21 give the same definitions used in this source.

## RWB1–4: original Gamma density and its logarithmic derivative

The source keeps the original measure `|Gamma(1/4+iy/2)|^2 dy/(2 pi)` and its full mass in the norms. Its square pushforward has density `t^-1/2 sigma(sqrt(t))`; hence `nu_a` has density `t^(a-1/2) sigma(sqrt(t))`. The quotient `h_j^(a+1)/h_j^(a)` is exactly the existing Christoffel coefficient, with the same monic polynomial definitions.

For every positive integer `N`, beta integration gives

\[
\int_0^1 x^{z-1}(1-x)^N\,dx=\frac{N!}{z(z+1)\cdots(z+N)}.
\]

The substitution `u=Nx` proves RWB3 with its exact power `N^z` and exponent `N`. Extend the integral to the positive half line with its indicator. On a compact subset of `Re z>0`, the stated small- and large-`u` bounds, multiplied by `e^-u`, dominate uniformly. The same bounds with `|log u|` dominate the complex derivative. The dominated convergence argument therefore gives both the locally uniform Gamma limit and the derivative limit used subsequently.

At `z=alpha+iv`, taking the modulus of the exact finite expression relative to its value at `alpha>0` cancels `N! N^alpha` and gives the displayed product. Since the logarithms of its positive factors have a convergent sum and `Gamma(alpha)>0` by its Euler integral, its limit is strictly positive. This proves the required nonvanishing before any division by Gamma. Logarithmic differentiation of the finite expression is `log N-sum_r 1/(z+r)`. Its imaginary part is the convergent positive series displayed in RWB4 for `v>0`; the signs are correct.

For `z=1/4+iy/2`, differentiating the logarithm of the absolute square gives `sigma'/sigma=-Im(Gamma'/Gamma)`. Thus the identity for `L` in RWB4 has the required positive sign and no missing factor of two.

The decreasing function `F_v(x)=v^2/(x^2+v^2)` satisfies

\[
\int_{1/4}^{\infty}F_v\le\sum_{r\ge0}F_v(r+1/4)
\le F_v(1/4)+\int_{1/4}^{\infty}F_v.
\]

Subtracting its full integral `pi v/2` gives lower error at least `-1/4`. For the upper error, `integral_0^(1/4) F_v >= F_v(1/4)/4`, so the error is at most `3F_v(1/4)/4 <=3/4`. Since `yL(y)=2 sum F_v` at `y=2v>0`, doubling gives exactly `[-1/2,3/2]` in RWB2. Evenness and continuity give the remaining points. The derivative bound at infinity and its continuity near zero, together with the previous exponential Gamma bound, justify the polynomial integration by parts used below.

## RWB5–6: inverse moment on the specified shifted polynomial

The polynomial is precisely `Q=P_j^(a+1)`, while the probability ratio in RWB6 uses its norm in `nu_(a+1)`. Differentiation of the exact density gives

\[
\frac{d}{dt}\log\big(t^{a+1/2}\sigma(\sqrt t)\big)
=\frac{a+1/2}{t}-\frac{L(\sqrt t)}{2\sqrt t}.
\]

The boundary value of `Q^2 t^(a+1/2) sigma(sqrt(t))` vanishes at both endpoints for `a>=1`, and its derivative is integrable there. Orthogonality removes `integral QQ' dnu_(a+1)` because `deg Q'<j`. The remaining equation is exactly RWB6.

The numerator defining `J` is finite and strictly positive. RWB2 gives `L(sqrt(t))/sqrt(t) <= pi/(2sqrt(t))+3/(2t)`, and Cauchy–Schwarz in the same positive measure gives `E(t^-1/2)<=sqrt(E(t^-1))=sqrt(J)`. Therefore

\[
(a-1/4)J\le(\pi/4)\sqrt J,
\]

which proves the finite bound `J <= (pi/(4a-1))^2`. Its denominator is positive throughout the asserted domain. No estimate is applied to a different polynomial or a different shift.

## RWB7–10: odd polynomial identity and lower Christoffel bound

In `dw_a=y^(2a) d sigma`, the two original polynomials `R=P_j^(a)(y^2)` and `O=yP_j^(a+1)(y^2)` are monic of degrees `2j` and `2j+1`, with squared norms `h_j^(a)` and `h_j^(a+1)`. Orthogonality to all lower degrees follows by the exact parity decomposition and the square pushforward; both sectors occur.

The three identities in RWB9 hold as follows:

- `O'-(2j+1)R` has degree at most `2j-1` and is perpendicular to `R`.
- `R'` has degree at most `2j-1` and is perpendicular to `O`.
- `O/y-R` has degree at most `2j-2` and is perpendicular to `R`; `O/y` is a polynomial including at zero.

Integrating the derivative of `OR y^(2a) sigma` consequently gives

\[
(2a+2j+1)h_j^{(a)}=\int ORL\,dw_a.
\]

There is no surviving interior boundary at zero and the terms at infinity vanish. This checks RWB10 including the positive `2a` contribution.

With `L=(pi/2)sgn+rho`, Cauchy–Schwarz bounds the first term divided by `h_j^(a)` by `(pi/2)sqrt(c_j^(a))`. The bound `|y rho|<=3/2` makes the second at most

\[
\frac32\sqrt{c_j^{(a)}J_{a,j}}
\le\frac{3\pi}{2(4a-1)}\sqrt{c_j^{(a)}}.
\]

Combining these estimates and dividing by their positive coefficient proves both identical presentations of RWB7. The degree `j`, shift `a`, parameter `1/4` and factor `pi` all remain exact.

## RWB11–12: low coefficient and its necessary upper sign

For `I_p=integral_0^infinity y^p sigma(y)dy`, the integrated derivative of `y^(p+1)sigma` gives

\[
(p+1)I_p=\frac\pi2 I_{p+1}
 +\int_0^\infty y^p\big(yL(y)-\pi y/2\big)\sigma(y)\,dy.
\]

The error interval `[-I_p/2,3I_p/2]` gives exactly the lower `(2p-1)/pi` and upper `(2p+3)/pi` bounds for `I_(p+1)/I_p`. Boundary and integrability assertions hold for the whole stated domain `p>=0`.

Both applications used for the upper bound on `c_0^(a)=I_(2a+2)/I_(2a)` are positive upper bounds. They yield `(4a+3)(4a+5)/pi^2` as in RWB12. This is indeed the side needed for subtracting the low logarithm in the eventual lower return bound.

## RWB13–20: all original endpoints and the explicit lower return

RWB14 reproduces PHT23 exactly: the two `a=q+s` factors supply `2` copies at each `j<n` and `1` at `j=n`; the odd block supplies `2` copies at `a=q+s+1,j<n`; the low coefficient supplies the negative `a=q+s,j=0` copy. Thus each shift has `2q+1` positive copies and `1` negative copy. The original product `G` has both inclusive ranges `q,...,2q-1` and `q+1,...,2q`, with `4lq` linear factors. The logarithmic scale cancellation in RWB15 is exact.

The ratio `(4a-1)/(4a+2)` is increasing, so RWB7 at every positive occurrence implies RWB16 with `a>=q`. The replacement `a+j+1/2 >= q+j` is in the correct direction. The low coefficient bound in RWB17 uses the largest actual value `a=q+l-1`; its factors are consequently `4q+4l-1` and `4q+4l+1`, exactly as written.

The left/right sum inequality in RWB18 has endpoint difference `log(3/2)`. There are eight total copies of its degree sum after substituting RWB16 into the two doubled coefficient blocks; the additional `j=n` term contributes `2 log(3/2)`. The net endpoint correction is therefore `-6 log(3/2)`, as in RWB19. The constant `2q+1` coefficient count gives `(4q+2)` copies of each of `log(4/pi)` and `log r_q`, also as written.

For the original products, `log(1+x)<=x` gives the correction `(b+1/2)/q`. Summing over `2q` original `u` entries and `2l` original `b` entries gives exactly `4l^2`. The combined two unshifted endpoint sums equal twice the composite trapezoidal sum; concavity puts that sum below the exact integral. With the original negative sign this provides the lower product contribution stated before RWB20.

The leading logarithms combine to

\[
4lq\big[\log(4/\pi)+3\log(3/2)-2\log2\big]
=4lq\log(27/(8\pi)).
\]

The finite estimate on `(4q+2)log r_q` is `-3-9/(4q-1)`. The upper bound on `log U` cancels the remaining `2log(4/pi)` and contributes at worst `2(l+1/4)/q`. These calculations reproduce every sign and term in RWB20.

## RWB21–23: positive finite constant and original coupled limit

The displayed positive integral for `22/7-pi` is correct. It yields `27/(8pi)>189/176`. The derivative of `log(1+x)-2x/(2+x)` is `x^2/((1+x)(2+x)^2)>=0`, so `4log(27/(8pi))>104/365`. The integrated cubic majorant of the reciprocal gives `log(3/2)<=5/12`.

The packet identity gives `q>0` even and `q>=(4l+2)^2>=36l`. Upon dividing RWB20 by `lq`, the four finite subtractions are respectively at most

\[
\frac19,\quad\frac{11}{72},\quad\frac1{572},\quad\frac5{2592}.
\]

For the last one, use `l+1/4<=(5/4)l` and `q^2>=1296l^2`; for the third, use `q>=36` and monotonicity of `q(4q-1)`.

Exact integer fraction arithmetic was executed independently and confirms

\[
\frac{104}{365}-\frac19-\frac{11}{72}-\frac1{572}-\frac5{2592}
=\frac{2349349}{135289440}
=\frac1{64}+\frac{470903}{270578880}.
\]

Thus RWB21 is proved uniformly for every original integer `l>=1,m>=1`, including the smallest packet. Along any integer choices `m=m(l)>=1`, `q>=(4l+2)^2` implies that all four explicit errors divided by `lq` tend to zero. This proves the liminf bound RWB23 with its stated uniformity. No equality or missing determinant asymptotic has been inserted.

## RWB24–27: original polynomial map and the upper return

The monic minimum-norm property used in RWB24 follows directly from orthogonality. Applying it in `nu_(a+1)` to the trial polynomial `P_j^(a)` gives `h_j^(a+1)<=integral t(P_j^(a))^2 dnu_a`. With `F(y)=y^a P_j^(a)(y^2)`, the numerator is exactly `||yF||_sigma^2`, and the denominator is `||F||_sigma^2=h_j^(a)`. This retains the original polynomial of degree `D=a+2j` and the map into degree `D+1`.

The normalized HCT5 basis gives raising coefficients `sqrt((d+1)(d+1/2))` and lowering coefficients `sqrt(d(d-1/2))`, with the lowering value zero at `d=0`. Each part has mutually orthogonal images of the basis vectors, so its norm on the polynomial subspace of degree at most `D` is bounded by its respective largest coefficient. The triangle inequality gives the first RWB24 bound. For `D>=1`, arithmetic–geometric means bound these two coefficients by `D+3/4` and `D-1/4`. Thus the final square is exactly `(2a+4j+1/2)^2`.

For RWB25, the two lower moment-ratio bounds have positive factors throughout `a>=1`, so multiplication preserves their direction and gives `(4a-1)(4a+1)/pi^2`. At the original low indices it is strictly larger than `q^2` by `q>=36` and `pi<22/7`. Hence the low logarithm contributes negatively to `W` and may be discarded when producing an upper bound. The logarithms of the original linear factors divided by `q` are also strictly positive and occur negatively.

Every remaining positive coefficient has `a<=q+l,j<=q/2`, so its logarithm is at most `2log(4+(2l+1/2)/q)`. Their exact count is `l(2q+1)`, producing RWB26's factor `l(4q+2)`. The bound `q>=36l` gives the argument at most `293/72`.

Independent exact integer fraction arithmetic confirms the exponential partial sum `sum_(r=0)^4 (10/7)^r/r! = 29593/7203`. Cross multiplication against `293/72` gives positive numerator difference `20217`. Therefore the logarithm is less than `10/7`; `(4q+2)10/7<=6q` holds for every `q>=10`. This proves the uniform upper bound `6lq` on the actual packet and completes RWB27.

## Receiving meaning and limits of this review

The proof establishes substantive growth bounds on the original universal Gamma centre:

\[
\frac{lq}{64}\le W_k\le6lq,
\qquad
\liminf\frac{W_{4l+1}}{lq}\ge4\log\frac{27}{8\pi}>0,
\]

with the sharper signed finite lower remainder RWB20. In LET20 this enters with coefficient `+1`; in LET21 the arithmetic contribution of this same quantity carries coefficient `-1`. The remaining original arithmetic quantities must continue to use their actual definitions and proved bounds. This review supports precisely the RWB claims and their stated interfaces; it makes no claim about an additional arithmetic or RH conclusion.
