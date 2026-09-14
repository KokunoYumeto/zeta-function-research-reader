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

## Provenance and independence

The Gamma subreviewer independently checked the Euler-limit, reciprocal-product nonvanishing, Beta Jacobians, duplication coefficients, and \(\Gamma(1/2)\) calculation; its separate record is euler_beta_duplication.md. The balanced-audit lane supplies the consolidated proof above, including the two affine constants. This note removes Binet's formula as an external proof dependency of the adjacent density bounds. Its identity agrees with DLMF 5.9.10_2, but the citation is a comparison, not an assumed step in this proof. No arithmetic density, quotient, source mass, existing edition, remote artifact, or Lean process was changed.
