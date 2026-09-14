# Actual boundary tilts and uniform convolution tails

This calculation retains the original arithmetic density and the complete hypothetical actual quartet. It does not replace that density with a reference measure. The estimates do not assume RH or a pointwise lower bound for zeta.


## 1. Objects and the exact retained expression

Fix \(0<\delta<1/2\), \(\gamma>0\), and an integer \(m\ge1\), and suppose the selected full-order quartet is a quartet of zeros of the original \(g=2\xi\). Its monic polynomial is
\[
h(s)=\prod_{\epsilon,\eta\in\{-1,1\}}
 (s-\tfrac12-\epsilon\delta-i\eta\gamma)^m,
\qquad \deg h=4m.
\tag{BT1}
\]
The entire function \(g/h\), its original Taylor unit, source maps, and measure remain unchanged:
\[
w_h(t)=\frac{|(g/h)(1/2+it)|^2}{2\pi},\qquad
\alpha=\frac\pi2,\qquad R_0=\sqrt{\delta^2+\gamma^2}.
\tag{BT2}
\]
The original completion formula gives, exactly,
\[
\begin{split}
w_h(t)
&=\frac{(t^2+1/4)^2}{\sqrt\pi}\,
 \frac{|\zeta(1/2+it)|^2}{|h(1/2+it)|^2}\,\sigma(t),\\
\sigma(t)
&=\frac{|\Gamma(1/4+it/2)|^2}{2\pi},\\
|h(1/2+it)|^2
&=\bigl[((t-\gamma)^2+\delta^2)
              ((t+\gamma)^2+\delta^2)\bigr]^{2m}.
\end{split}
\tag{BT3}
\]
The two factors with each fixed imaginary sign contribute a minus sign before multiplication, so their product is the positive expression in the last line. Every denominator in (BT3) is positive. Conjugation of the original \(g\) and the real coefficients of \(h\) give \(w_h(-t)=w_h(t)\).

## 2. A centered partial-sum bound from the original floor formula

For every integer \(N\ge1\), initially for \(\Re s>1\),
\[
\zeta(s)=\sum_{n=1}^{N}n^{-s}
 +\frac{N^{1-s}}{s-1}
 -s\int_N^\infty \{x\}x^{-s-1}\,dx.
\tag{BT4}
\]
To verify (BT4), integrate the constant value \(\lfloor x\rfloor\) on each interval \([n,n+1)\), or telescope integration by parts of the absolutely convergent tail. The last integral is absolutely and locally uniformly convergent for \(\Re s>0\), so the identity continues to that half-plane with \(s\ne1\).

Let \(B_1(x)=\{x\}-1/2\), so \(|B_1(x)|\le1/2\). The identity \(\int_N^\infty x^{-s-1}dx=N^{-s}/s\) gives exactly
\[
\zeta(s)=\sum_{n=1}^{N-1}n^{-s}+\frac12N^{-s}
 +\frac{N^{1-s}}{s-1}
 -s\int_N^\infty B_1(x)x^{-s-1}\,dx.
\tag{BT5}
\]
No asymptotic remainder is substituted here.

On \(s=1/2+it\), put \(\varrho=\sqrt{t^2+1/4}\), which is both \(|s|\) and \(|s-1|\). For \(N\ge2\),
\[
\sum_{n=1}^{N-1}n^{-1/2}+\tfrac12N^{-1/2}
\le 2\sqrt{N-1}-1+\tfrac1{2\sqrt N}
\le 2\sqrt N-1.
\]
The first inequality follows from the integral bound for the decreasing function \(x^{-1/2}\). For the second, \(2(\sqrt N-\sqrt{N-1})=2/(\sqrt N+\sqrt{N-1})\ge1/\sqrt N\). At \(N=1\), the same asserted inequality holds directly, with left side \(1/2\). The absolute integral in (BT5), before its multiplier \(s\), is at most \(\tfrac12\int_N^\infty x^{-3/2}dx=N^{-1/2}\). Therefore
\[
|\zeta(1/2+it)|
\le 2\sqrt N-1+\frac{\sqrt N}{\varrho}
                       +\frac{\varrho}{\sqrt N}
\quad(t\in\mathbb R,\ N\ge1).
\tag{BT6}
\]
The infimum over these explicitly specified integer choices is also a bound.

For \(x=|t|\ge1\), choose \(N=\lfloor x\rfloor\). Then
\[
x/2\le N\le x,\qquad
\varrho\le\frac{\sqrt5}{2}x,\qquad
\frac{\sqrt N}{\varrho}\le x^{-1/2}.
\]
Since \(-1+x^{-1/2}\le0\), (BT6) yields
\[
\boxed{|\zeta(1/2+it)|\le Z_*\sqrt{|t|}\quad(|t|\ge1),
\qquad Z_*=2+\sqrt{5/2}.}
\tag{BT7}
\]
This improves the polynomial exponent in the uncentered estimate used in TG.15. It is not a claim that (BT7) is the strongest known zeta bound. On the whole real line the original \(N=1\) uncentered formula gives independently
\[
|\zeta(1/2+it)|\le 1+2\sqrt{t^2+1/4}.
\tag{BT8}
\]

## 3. Explicit two-sided Gamma bounds

The complete Binet calculation included below proves
\[
\boxed{
c_\Gamma e^{-\alpha|t|}(1+|t|)^{-1/2}
\le \sigma(t)\le
C_\Gamma e^{-\alpha|t|}(1+|t|)^{-1/2}
\quad(t\in\mathbb R),}
\tag{BT9}
\]
where
\[
c_\Gamma=\sqrt2\,e^{-7/6},\qquad
C_\Gamma=\sqrt{2\sqrt5}\,e^{2/3}.
\tag{BT10}
\]
For completeness, its exact starting identity for \(\Re z>0\) is
\[
\log\Gamma z=(z-\tfrac12)\log z-z+\tfrac12\log(2\pi)+R(z),
\quad
R(z)=\int_0^\infty e^{-zu}
 \left(\frac1{e^u-1}-\frac1u+\frac12\right)\frac{du}{u}.
\]
The logarithmic branch is the one real on the positive real axis. The kernel is
\((\coth x-1/x)/(4x)\), with \(x=u/2>0\). Define
\[
F(x)=x\cosh x-\sinh x,\qquad
G(x)=(x^2+3)\sinh x-3x\cosh x.
\]
Both vanish at zero, and \(F'(x)=x\sinh x\ge0\), \(G'(x)=xF(x)\ge0\). Dividing their nonnegative values by the appropriate positive factors gives \(0\le\coth x-1/x\le x/3\). Thus the kernel lies between zero and \(1/12\). At \(z=1/4+it/2\), integration of \(e^{-u/4}/12\) proves \(|R(z)|\le1/3\).

Twice the real part of Binet's identity, with \(x=|t|\), gives exactly
\[
\sigma(t)=|z|^{-1/2}
 \exp[-x\arctan(2x)-1/2+2\Re R(z)].
\]
For \(x>0\),
\[
-x\arctan(2x)-\tfrac12
=-\alpha x+x\arctan(1/(2x))-\tfrac12
\le-\alpha x,
\]
because \(\arctan v\le v\) for \(v\ge0\). At \(x=0\), the same inequality is \(-1/2\le0\). The lower bound uses \(\arctan(2x)\le\pi/2\). Hence the full exponent is between \(-\alpha x-7/6\) and \(-\alpha x+2/3\), including zero.

Finally \(|z|^2=1/16+x^2/4\), and the exact squared differences
\[
\frac{(1+x)^2}{4}-|z|^2=\frac{3+8x}{16},\qquad
|z|^2-\frac{(1+x)^2}{20}=\frac{(4x-1)^2}{80}
\]
give
\[
\sqrt2(1+x)^{-1/2}\le |z|^{-1/2}
\le\sqrt{2\sqrt5}(1+x)^{-1/2}.
\]
These prove (BT9)–(BT10) with no unproved Stirling remainder and no unquantified compact Gamma minimum.

## 4. A global explicit actual boundary-tilt bound

Set
\[
p=8m-\frac92,\qquad \beta=p-\frac12=8m-5,\qquad
T_h=\max(1,2R_0).
\tag{BT11}
\]
Then \(p\ge7/2>1\) and \(\beta>0\). Define
\[
\begin{split}
C_{\mathrm{comp}}
={}&\frac{C_\Gamma}{\sqrt\pi}
 (T_h^2+1/4)^2
 [1+2\sqrt{T_h^2+1/4}]^2
 \delta^{-8m}(1+T_h)^\beta,\\
C_{\mathrm{tail}}
={}&\frac{25C_\Gamma Z_*^2}{16\sqrt\pi}
 \left(\frac43\right)^{4m}
 \left(1+\frac1{T_h}\right)^\beta,\\
C_h^{\mathrm{tilt}}
={}&\max(C_{\mathrm{comp}},C_{\mathrm{tail}}).
\end{split}
\tag{BT12}
\]
These constants are explicit in the fixed quartet and elementary constants. None is an unevaluated zeta supremum, and none changes the source mass.

For \(|t|\le T_h\), (BT3) has \(|h(1/2+it)|^2\ge\delta^{8m}\). Apply (BT8) and the upper inequality of (BT9). Multiplying by \(e^{\alpha|t|}(1+|t|)^p\) leaves the factor \((1+|t|)^\beta\); bounding \(|t|\) by \(T_h\) proves the constant \(C_{\mathrm{comp}}\).

For \(x=|t|\ge T_h\), retain the exact identity
\[
((t-\gamma)^2+\delta^2)((t+\gamma)^2+\delta^2)
=(t^2-R_0^2)^2+4\delta^2t^2
\ge\frac9{16}t^4.
\tag{BT13}
\]
The last inequality uses \(t^2\ge4R_0^2\). Thus
\[
|h(1/2+it)|^2\ge(3/4)^{4m}x^{8m},
\qquad
(t^2+1/4)^2\le(25/16)x^4.
\]
Applying (BT7) and (BT9) to (BT3) gives
\[
e^{\alpha x}w_h(t)
\le\frac{25C_\Gamma Z_*^2}{16\sqrt\pi}
\left(\frac43\right)^{4m}
x^{5-8m}(1+x)^{-1/2}.
\]
Multiplication by \((1+x)^p\) leaves
\(((1+x)/x)^\beta\le(1+1/T_h)^\beta\). This proves the global bound
\[
\boxed{
0\le e^{\alpha|t|}w_h(t)
\le C_h^{\mathrm{tilt}}(1+|t|)^{-p}
\quad(t\in\mathbb R).}
\tag{BT14}
\]
The exact expression (BT3), including its actual zeta numerator and complete quartet denominator, is the object bounded throughout.

## 5. Boundary moments and finite derivative orders

Define the original two boundary tilts and their actual masses:
\[
f_\pm(t)=e^{\pm\alpha t}w_h(t),\qquad
M_\pm=\int_{\mathbb R}f_\pm(t)\,dt.
\tag{BT15}
\]
The nonzero entire function \(g/h\) has only isolated zeros on the integration line, so both masses are positive. Evenness gives \(M_+=M_-=:M_\alpha\). Integration of (BT14) proves
\[
\boxed{
0<M_\alpha=M_h(\alpha)=M_h(-\alpha)
\le\frac{2C_h^{\mathrm{tilt}}}{p-1}<\infty.}
\tag{BT16}
\]
For every real \(j\ge0\) with \(j<p-1\), the inequality
\(|t|^j\le(1+|t|)^j\) gives
\[
\int_{\mathbb R}|t|^j e^{\pm\alpha t}w_h(t)\,dt
\le\frac{2C_h^{\mathrm{tilt}}}{p-j-1}.
\tag{BT17}
\]
More precisely, for \(R\ge0\), the part \(|t|\ge R\) is at most
\[
\frac{2C_h^{\mathrm{tilt}}}{p-j-1}
(1+R)^{j-p+1}.
\tag{BT18}
\]
Thus every integer order \(0\le j\le8m-6\) is absolutely integrable at both boundary tilts. For a simple quartet, this includes orders zero, one and two.

For the actual Laplace function \(M_h(z)=\int e^{zt}w_h(t)\,dt\), differentiation in \(|\Re z|<\alpha\) gives \(\int t^j e^{zt}w_h(t)\,dt\). For each stated order, (BT14) dominates the absolute integrand uniformly on \(|\Re z|\le\alpha\) by the integrable function \(C_h^{\mathrm{tilt}}|t|^j(1+|t|)^{-p}\). Dominated convergence therefore extends those derivatives continuously to the closed strip with exactly the boundary moments above. This does not assert holomorphic continuation through the boundary or finiteness of every endpoint derivative.

## 6. A uniform convolution envelope with the literal tilted mass

If a nonnegative integrable function \(f\) has actual mass \(M>0\) and
\(f(x)\le C(1+|x|)^{-p}\), then for every integer \(k\ge1\),
\[
\boxed{
f^{*k}(u)\le kCM^{k-1}(1+|u|/k)^{-p}.}
\tag{BT19}
\]
For \(k=1\) this is the hypothesis. In the convolution integral with
\(x_1+\cdots+x_k=u\), at least one index has \(|x_i|\ge|u|/k\). Bound its integrand by the sum of the \(k\) restrictions to these events. On the event for index \(i\), the factor \(f(x_i)\) is at most \(C(1+|u|/k)^{-p}\). Parametrize the convolution hyperplane by the other \(k-1\) coordinates; the change from any such convolution parametrization to another has absolute determinant one. Dropping the event now leaves the full product integral \(M^{k-1}\). Summing proves (BT19), without a probability normalization.

Multiplication inside the original convolution gives exactly
\[
f_\pm^{*k}(u)=e^{\pm\alpha u}m_{h,k}(u),
\qquad m_{h,k}=w_h^{*k}.
\tag{BT20}
\]
Use the plus tilt for \(u\ge0\), the minus tilt for \(u<0\), and their same actual mass \(M_\alpha\). The result is
\[
\boxed{
m_{h,k}(u)\le
kC_h^{\mathrm{tilt}}M_\alpha^{k-1}
e^{-\alpha|u|}(1+|u|/k)^{-p}}
\quad(k\ge1,\ u\in\mathbb R).
\tag{BT21}
\]
All dependence on \(k\) is displayed. The constants \(C_h^{\mathrm{tilt}},p,M_\alpha\) belong to fixed \(h\).

For every integer \(n\ge0\) with \(2n>p-1\), use
\((1+u/k)^{-p}\le k^pu^{-p}\) for \(u>0\). The Gamma integral gives
\[
\boxed{
\int_{\mathbb R}u^{2n}m_{h,k}(u)\,du
\le 2C_h^{\mathrm{tilt}}k^{p+1}M_\alpha^{k-1}
\frac{\Gamma(2n-p+1)}{\alpha^{\,2n-p+1}}.}
\tag{BT22}
\]
The condition \(2n>p-1\) is precisely what makes this comparison integrable at zero. The actual raw moments exist also when the condition fails, but (BT22) is not used there.

For the retained source comparison, one direct corollary is
\[
m_{h,k}(u)\le b_k\sigma(u),\qquad
b_k=\frac{C_h^{\mathrm{tilt}}}{c_\Gamma}
k^{p+1}M_\alpha^{k-1}>0.
\tag{BT23}
\]
Indeed \(1+|u|/k\ge(1+|u|)/k\); (BT21) and the lower Gamma bound leave
the additional factor \((1+|u|)^{-p+1/2}\le1\). This is a proved identity-map norm comparison; it does not assert equality of the measures.

# Internal derivation of the exact Binet identity

This note proves the exact identity used in the actual boundary-tilt calculation from the defining Gamma integral, elementary integration, locally uniform products, and the Beta substitution. No Stirling formula, Gamma asymptotic, or cited Binet identity is assumed.

All complex powers of positive real integration variables use their real logarithms. The notation \(\operatorname{Log}z\) on \(\Re z>0\) denotes the principal holomorphic logarithm. The holomorphic logarithm of Gamma will be constructed below and will be real on the positive real axis.

## 1. Defining integrals and the finite Euler formula

For \(\Re z>0\), define
\[
\Gamma(z)=\int_0^\infty x^{z-1}e^{-x}\,dx.
\tag{BI1}
\]
This is absolutely convergent. On a compact set with \(0<a\le\Re z\le b\), its integrand and each of its first finitely many derivatives in \(z\) are bounded in absolute value by
\[
(x^{a-1}+x^{b-1})(1+|\log x|^j)e^{-x},
\]
with the appropriate fixed integer \(j\). This function is integrable at zero and infinity. Differentiation under the integral is therefore valid, and \(\Gamma\) is holomorphic on the right half-plane. Integration by parts gives
\[
\Gamma(z+1)=z\Gamma(z),
\qquad \Gamma(1)=1,
\tag{BI2}
\]
because \(x^ze^{-x}\) tends to zero at both endpoints for \(\Re z>0\).

For \(\Re z,\Re w>0\), let
\[
B(z,w)=\int_0^1 t^{z-1}(1-t)^{w-1}\,dt.
\tag{BI3}
\]
For an integer \(N\ge1\), integration by parts gives
\[
B(z,N+1)=\frac{N}{z}B(z+1,N).
\]
Iterating, and using \(B(z+N,1)=1/(z+N)\), proves the exact finite formula
\[
B(z,N+1)=\frac{N!}{z(z+1)\cdots(z+N)}.
\tag{BI4}
\]
In particular none of these denominators vanishes in the right half-plane.

Set
\[
E_N(z)=N^zB(z,N+1)
=\frac{N^zN!}{z(z+1)\cdots(z+N)},\qquad N\ge1.
\tag{BI5}
\]
The substitution \(t=x/N\) gives
\[
E_N(z)=\int_0^N x^{z-1}(1-x/N)^N\,dx.
\tag{BI6}
\]
For \(0\le x<N\), \(\log(1-x/N)\le-x/N\), so
\[
0\le(1-x/N)^N\le e^{-x}.
\]
For each fixed \(x>0\), the expression on the left tends to \(e^{-x}\), with the indicator of \(x<N\) understood.

On a compact set as above, therefore
\[
\begin{split}
\sup_z|E_N(z)-\Gamma(z)|
\le\int_0^\infty &(x^{a-1}+x^{b-1})\\
&\cdot\left|(1-x/N)^N\mathbf1_{\{x<N\}}-e^{-x}\right|dx
\longrightarrow0
\end{split}
\]
by dominated convergence. The same argument with an additional factor \(|\log x|^j\), for \(j=1,2\), proves locally uniform convergence of those two derivatives as well. Thus the Euler limit and the derivative limits are established directly from their integrals.

## 2. Nonvanishing and the holomorphic Gamma logarithm

Write \(H_N=\sum_{j=1}^N1/j\). The real numbers
\[
\gamma_N=H_N-\log N
\]
decrease and are bounded below by zero. Indeed
\[
\gamma_{N+1}-\gamma_N
=\frac1{N+1}-\log(1+1/N)<0
\]
by integrating \(1/x>1/(N+1)\) on \([N,N+1)\), while
\(H_N\ge\int_1^{N+1}dx/x=\log(N+1)\). Let
\(\gamma_{\mathrm E}=\lim_N\gamma_N\).

For \(\Re z>0\), every \(1+z/j\) has positive real part. Its principal logarithm is holomorphic. Define
\[
Q_N(z)=\operatorname{Log}z+z(H_N-\log N)
 +\sum_{j=1}^N\left(\operatorname{Log}(1+z/j)-z/j\right).
\tag{BI7}
\]
Exponentiating this literal sum and using (BI5) gives exactly
\[
e^{Q_N(z)}
=zN^{-z}\prod_{j=1}^N(1+z/j)=\frac1{E_N(z)}.
\tag{BI8}
\]

The logarithmic series in (BI7) converges locally uniformly. To prove this explicitly, for \(|w|\le1/2\),
\[
\operatorname{Log}(1+w)-w
=-\int_0^1\frac{t w^2}{1+tw}\,dt,
\]
whence \(|\operatorname{Log}(1+w)-w|\le|w|^2\). On a compact set with \(|z|\le R\), this bounds the \(j\)-th summand by \(R^2/j^2\) whenever \(j\ge2R\). The finite initial part is holomorphic and the summable bound proves uniform convergence of the tail. Hence
\[
Q(z)=\operatorname{Log}z+\gamma_{\mathrm E}z
 +\sum_{j=1}^\infty
       \left(\operatorname{Log}(1+z/j)-z/j\right)
\tag{BI9}
\]
is holomorphic and \(Q_N\to Q\) locally uniformly.

Taking limits in \(E_N e^{Q_N}=1\), using Section 1, proves
\[
\Gamma(z)e^{Q(z)}=1.
\tag{BI10}
\]
This proves that Gamma is nowhere zero on the entire right half-plane. It also constructs the required holomorphic logarithm:
\[
\mathcal G(z):=-Q(z),\qquad e^{\mathcal G(z)}=\Gamma(z).
\tag{BI11}
\]
For \(x>0\), every term in \(Q(x)\) is real and the defining Gamma integral is positive. Thus \(\mathcal G(x)\) is precisely the real logarithm of \(\Gamma(x)\); there is no unspecified additive \(2\pi i\) constant.

The second derivatives of the series in (BI9) converge locally uniformly, since \(\sum_j|z+j|^{-2}\) does. Termwise differentiation gives
\[
\boxed{
\mathcal G''(z)=\sum_{j=0}^{\infty}\frac1{(z+j)^2}
\qquad(\Re z>0).}
\tag{BI12}
\]
For justification without assuming a derivative-series theorem, on any slightly larger compact subset of the same half-plane the series converges uniformly; Cauchy's integral formula on small circles then gives uniform convergence of its derivatives. Direct estimates of the derivatives of its summands give the same conclusion.

## 3. Beta product, duplication, and the factor \(\sqrt\pi\)

The absolutely convergent product of the two defining Gamma integrals admits the change of variables
\[
x=rt,\qquad y=r(1-t),\qquad r>0,\quad0<t<1.
\]
Its Jacobian matrix has determinant \(-r\), so the positive integration Jacobian is \(r\). Consequently
\[
\Gamma(z)\Gamma(w)=\Gamma(z+w)B(z,w)
\qquad(\Re z,\Re w>0).
\tag{BI13}
\]
All powers here are powers of positive real bases. Fubini and the change of variables are justified by the same integrals with real parts of the exponents.

In \(B(z,z)\), first substitute \(t=(1+u)/2\), and then use symmetry and \(v=u^2\). Every factor is retained:
\[
\begin{split}
B(z,z)
&=2^{1-2z}\int_{-1}^1(1-u^2)^{z-1}\,du\\
&=2^{2-2z}\int_0^1(1-u^2)^{z-1}\,du\\
&=2^{1-2z}B(1/2,z).
\end{split}
\tag{BI14}
\]

Finally \(x=t^2\) in (BI1) gives
\(\Gamma(1/2)=2\int_0^\infty e^{-t^2}dt\).
The latter is the positive integral over the whole real line. Its square is
\(\int_{\mathbb R^2}e^{-(x^2+y^2)}dx\,dy\). Polar coordinates, whose positive Jacobian is \(r\), evaluate this square as
\[
2\pi\int_0^\infty re^{-r^2}\,dr=\pi.
\]
Thus \(\Gamma(1/2)=\sqrt\pi\). Inserting (BI13) into (BI14), and using the nonvanishing established in (BI10), proves
\[
\boxed{
\Gamma(z)\Gamma(z+1/2)
=2^{1-2z}\sqrt\pi\,\Gamma(2z)
\qquad(\Re z>0).}
\tag{BI15}
\]
On the positive real axis all these factors are positive, so their real logarithms obey the corresponding additive identity without any branch ambiguity.

## 4. The bounded integral remainder

For \(u>0\), define
\[
K(u)=\left(\frac1{e^u-1}-\frac1u+\frac12\right)\frac1u.
\tag{BI16}
\]
We prove its exact bounds rather than assuming a Bernoulli expansion. With \(x=u/2>0\),
\[
K(u)=\frac{\coth x-1/x}{4x}.
\]
The two functions
\[
F_0(x)=x\cosh x-\sinh x,\qquad
F_1(x)=(x^2+3)\sinh x-3x\cosh x
\]
vanish at zero and satisfy \(F_0'(x)=x\sinh x\ge0\) and
\(F_1'(x)=xF_0(x)\ge0\). Dividing their nonnegative values by positive factors gives
\[
0\le\coth x-\frac1x\le\frac{x}{3}.
\]
Therefore
\[
\boxed{0\le K(u)\le\frac1{12}\quad(u>0).}
\tag{BI17}
\]

Define the actual remainder candidate
\[
R(z)=\int_0^\infty e^{-zu}K(u)\,du,\qquad \Re z>0.
\tag{BI18}
\]
It is absolutely convergent and holomorphic. Differentiating \(j\) times is justified on every compact set with \(\Re z\ge a>0\) by \(u^je^{-au}/12\). In particular
\[
|R(z)|\le\frac1{12\Re z},
\qquad 0\le R(x)\le\frac1{12x}\quad(x>0).
\tag{BI19}
\]

## 5. Equality of second derivatives

Put \(c=\tfrac12\log(2\pi)\), and define
\[
\mathcal F(z)=(z-\tfrac12)\operatorname{Log}z-z+c+R(z).
\tag{BI20}
\]
Differentiation and the exact algebraic identity
\[
u^2K(u)=\frac{u}{e^u-1}-1+\frac u2
\]
give
\[
\begin{split}
\mathcal F''(z)
&=\frac1z+\frac1{2z^2}
 +\int_0^\infty e^{-zu}
       \left(\frac{u}{e^u-1}-1+\frac u2\right)du\\
&=\frac1{z^2}
 +\int_0^\infty\frac{u e^{-zu}}{e^u-1}\,du.
\end{split}
\tag{BI21}
\]
Here \(\int_0^\infty e^{-zu}du=1/z\) and
\(\int_0^\infty ue^{-zu}du=1/z^2\) follow by elementary integration on \(\Re z>0\); all cancellation factors are displayed.

The geometric series \(1/(e^u-1)=\sum_{j=1}^\infty e^{-ju}\) is valid for \(u>0\). Its absolute integral after multiplication by \(ue^{-zu}\) is bounded by the same expression with \(\Re z\), which is integrable at zero and infinity. Hence termwise integration is valid, and
\[
\mathcal F''(z)
=\frac1{z^2}+\sum_{j=1}^\infty
 \int_0^\infty ue^{-(z+j)u}du
=\sum_{j=0}^\infty\frac1{(z+j)^2}
=\mathcal G''(z).
\tag{BI22}
\]
The right half-plane is connected, so the holomorphic function
\(\mathcal F-\mathcal G\) has zero second derivative and consequently equals \(az+b\) there, for constants \(a,b\in\mathbb C\).

## 6. The recurrence fixes the linear constant

For positive real \(x\), (BI2) and the real-axis branch in (BI11) give
\[
\mathcal G(x+1)-\mathcal G(x)=\log x.
\]
The corresponding exact difference of the explicit function (BI20) is
\[
\mathcal F(x+1)-\mathcal F(x)-\log x
=(x+\tfrac12)\log(1+1/x)-1+R(x+1)-R(x).
\tag{BI23}
\]
The left side equals \(a\). The elementary integral bounds
\[
\frac{y}{1+y}\le\log(1+y)\le y\qquad(y>0)
\]
show that \(x\log(1+1/x)\to1\) and
\(\tfrac12\log(1+1/x)\to0\). The remainder bound (BI19) makes the remaining difference tend to zero. Thus \(a=0\), and
\(\mathcal F-\mathcal G=b\) throughout the right half-plane.

## 7. Duplication fixes the additive constant

For \(x>0\), the positive-real logarithm of (BI15) is
\[
\mathcal G(x)+\mathcal G(x+1/2)-\mathcal G(2x)
=(1-2x)\log2+\tfrac12\log\pi.
\tag{BI24}
\]
Since \(\mathcal F=\mathcal G+b\), the difference between the same expression using \(\mathcal F\) and the right side of (BI24) equals exactly \(b+b-b=b\).

Insert (BI20) without dropping any constant. The terms containing \(\log x\) cancel, and the resulting difference is
\[
\begin{split}
b={}&x\log(1+1/(2x))-\tfrac12\\
&+\left(c-\tfrac12\log(2\pi)\right)
 +R(x)+R(x+1/2)-R(2x).
\end{split}
\tag{BI25}
\]
Our displayed \(c=\tfrac12\log(2\pi)\) cancels exactly. The same elementary logarithm bounds show
\(x\log(1+1/(2x))\to1/2\), and each remainder tends to zero by (BI19). Thus \(b=0\).

Combining Sections 5–7 proves the complete exact identity
\[
\boxed{
\log\Gamma(z)
=(z-\tfrac12)\operatorname{Log}z-z+\tfrac12\log(2\pi)
+\int_0^\infty e^{-zu}
\left(\frac1{e^u-1}-\frac1u+\frac12\right)\frac{du}{u},
\quad\Re z>0.}
\tag{BI26}
\]
The logarithm on the left is the uniquely specified holomorphic branch from (BI11). The integral is absolutely convergent, and its bound and all differentiations have been justified. This is the identity used by the actual boundary-tilt proof.
