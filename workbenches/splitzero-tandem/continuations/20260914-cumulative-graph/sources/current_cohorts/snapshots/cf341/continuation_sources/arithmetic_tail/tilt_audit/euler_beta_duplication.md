# Euler's Gamma limit, its reciprocal product, and duplication

## Task, domain, and conventions

This file completes the foundations requested by the parent `balanced_audit`
lane for its independent Binet derivation. It proves the Euler limit with
uniformly convergent first and second derivatives, constructs the logarithm
without assuming Gamma has no zeros, and proves the beta and duplication
identities with their original constants.

The common Gamma domain is

\[
\mathcal H=\{z\in\mathbb C:\Re z>0\}.
\tag{E1}
\]

For every positive real base \(v\), the convention is
\(v^z=\exp(z\log v)\), with the real logarithm of \(v\). The symbol
\(\operatorname{Log}\) denotes the principal holomorphic logarithm when
its complex argument lies in the right half-plane. Integer indices retain
their stated ranges. No analytic continuation outside \(\mathcal H\) is
needed.

The duplication substitutions and Gaussian calculation were independently
checked by the bounded `duplication_check` subagent, which made no file edits.
All derivations needed for the conclusions are included here. This lane has
written only this new report and its previously assigned Gamma-bound report.

## The defining integral and its derivatives

For \(z\in\mathcal H\), define

\[
\Gamma(z)=\int_0^\infty v^{z-1}e^{-v}\,dv.
\tag{E2}
\]

Let \(K\) be any nonempty compact subset of \(\mathcal H\), and set

\[
a=\min_{z\in K}\Re z>0,
\qquad b=\max_{z\in K}\Re z.
\]

For each \(m\in\{0,1,2\}\), an integrable dominating function is

\[
D_{K,m}(v)=e^{-v}|\log v|^m
\begin{cases}
v^{a-1},&0<v\le1,\\
v^{b-1},&v>1.
\end{cases}
\tag{E3}
\]

For \(m=0\), the logarithmic factor means \(1\). Near zero its integrability
follows from

\[
\int_0^1 v^{a-1}|\log v|^m\,dv
=\int_0^\infty e^{-ay}y^m\,dy
=\frac{m!}{a^{m+1}},
\tag{E4}
\]

where \(y=-\log v\) and the last equality follows by \(m\) integrations
by parts, beginning with \(\int_0^\infty e^{-ay}dy=1/a\). At infinity,
\(\log v\le v\) for \(v\ge1\); every function \(v^p e^{-v/2}\) with
fixed \(p\ge0\) is bounded there, as its derivative has the sign of
\(p-v/2\). Thus the tail of (E3) is bounded by a constant times
\(e^{-v/2}\).

The same construction on compact neighborhoods of points of \(\mathcal H\)
justifies holomorphic differentiation under the integral, and proves

\[
\Gamma^{(m)}(z)=\int_0^\infty
v^{z-1}(\log v)^m e^{-v}\,dv,
\qquad m=0,1,2.
\tag{E5}
\]

Integration by parts in the defining integral is legitimate because
\(v^z e^{-v}\to0\) at both endpoints for \(\Re z>0\). It gives

\[
\Gamma(z+1)=z\Gamma(z),\qquad \Gamma(1)=1.
\tag{E6}
\]

For every positive real \(x\), the integrand in (E2) is positive, hence
\(\Gamma(x)>0\). No claim of nonvanishing at complex arguments has yet
been used.

## The beta integral and the finite product

For \(z,w\in\mathcal H\), define

\[
B(z,w)=\int_0^1 u^{z-1}(1-u)^{w-1}\,du.
\tag{E7}
\]

It is absolutely convergent: the endpoint powers have exponents
\(\Re z-1>-1\) and \(\Re w-1>-1\). For an integer \(N\ge1\), integration
by parts using the primitive \(u^z/z\) gives

\[
B(z,N+1)=\frac{N}{z}B(z+1,N).
\tag{E8}
\]

The boundary term \(u^z(1-u)^N/z\) vanishes at both endpoints. Also
\(B(z,1)=1/z\). Applying (E8) exactly \(N\) times therefore proves

\[
B(z,N+1)=\frac{N!}{z(z+1)\cdots(z+N)},
\qquad N\ge0,\quad z\in\mathcal H.
\tag{E9}
\]

Every denominator in this formula is nonzero because its real part is
positive. This finite identity has not divided by a Gamma value.

## The Euler limit, including two derivatives

For every integer \(N\ge1\), define

\[
F_N(z)=N^zB(z,N+1)
=\frac{N^zN!}{z(z+1)\cdots(z+N)}.
\tag{E10}
\]

In the beta integral use the substitution \(v=Nu\), retaining
\(du=dv/N\). Since the bases are positive, the three powers of \(N\)
cancel as \(N^zN^{1-z}N^{-1}=1\). Hence

\[
F_N(z)=\int_0^N v^{z-1}\left(1-\frac vN\right)^N\,dv
=\int_0^\infty v^{z-1}k_N(v)\,dv,
\tag{E11}
\]

where

\[
k_N(v)=
\begin{cases}
(1-v/N)^N,&0<v<N,\\
0,&v\ge N.
\end{cases}
\tag{E12}
\]

For \(0\le s<1\), the integral identity
\(-\log(1-s)=\int_0^s(1-y)^{-1}dy\) gives

\[
-\frac{s}{1-s}\le\log(1-s)\le-s.
\tag{E13}
\]

It follows that \(0\le k_N(v)\le e^{-v}\) for all \(v>0\). For fixed
\(v>0\) and \(N>v\), (E13) also gives

\[
-\frac{v}{1-v/N}
\le N\log(1-v/N)\le-v.
\]

Both endpoints tend to \(-v\), so \(k_N(v)\to e^{-v}\).

For each \(m\in\{0,1,2\}\), differentiating (E11) under its integral is
justified by (E3), because \(k_N\le e^{-v}\). Thus

\[
F_N^{(m)}(z)=\int_0^\infty
v^{z-1}(\log v)^m k_N(v)\,dv.
\tag{E14}
\]

For the compact \(K\) and numbers \(a,b\) above, the supremum of the
derivative error satisfies the concrete bound

\[
\begin{aligned}
\sup_{z\in K}|F_N^{(m)}(z)-\Gamma^{(m)}(z)|
&\le\int_0^\infty |\log v|^m
\begin{cases}
v^{a-1},&0<v\le1,\\
v^{b-1},&v>1
\end{cases}
\bigl(e^{-v}-k_N(v)\bigr)\,dv.
\end{aligned}
\tag{E15}
\]

The integrand is nonnegative, tends pointwise to zero, and is at most the
integrable function (E3). Dominated convergence therefore shows that the
right side of (E15) tends to zero. This proves simultaneously

\[
\boxed{
F_N^{(m)}\longrightarrow\Gamma^{(m)}
\text{ locally uniformly on }\mathcal H,
\qquad m=0,1,2.
}
\tag{E16}
\]

In particular, the Euler limit has exactly the requested indexing:

\[
\boxed{
\Gamma(z)=\lim_{N\to\infty}
\frac{N^zN!}{z(z+1)\cdots(z+N)},
\qquad\Re z>0.
}
\tag{E17}
\]

## The reciprocal limit proves nonvanishing

Write \(H_N=\sum_{j=1}^N1/j\). The real sequence
\(H_N-\log N\) is positive: integrating \(1/u\) on the intervals
\([j,j+1]\) gives
\(H_N\ge\log(N+1)>\log N\). It is decreasing because

\[
\begin{aligned}
(H_{N+1}-\log(N+1))-(H_N-\log N)
&=\frac1{N+1}-\log(1+1/N)<0,
\end{aligned}
\]

where
\(\log(1+1/N)=\int_N^{N+1}u^{-1}du>1/(N+1)\).
Thus the finite real limit

\[
\gamma=\lim_{N\to\infty}(H_N-\log N)
\tag{E18}
\]

exists. This equation defines the constant used below.

For \(z\in\mathcal H\), both \(z\) and every \(1+z/j\) lie in the right
half-plane. Define the holomorphic finite sums

\[
q_N(z)=\operatorname{Log}z
+z(H_N-\log N)
+\sum_{j=1}^N
\left(\operatorname{Log}(1+z/j)-\frac zj\right).
\tag{E19}
\]

Exponentiating this finite expression, with all factors retained, gives

\[
\begin{aligned}
e^{q_N(z)}
&=z\,e^{z(H_N-\log N)}
 \prod_{j=1}^N\left[(1+z/j)e^{-z/j}\right]\\
&=zN^{-z}\prod_{j=1}^N(1+z/j)
=\frac{z(z+1)\cdots(z+N)}{N^zN!}
=\frac1{F_N(z)}.
\end{aligned}
\tag{E20}
\]

To establish convergence of (E19), let \(K\Subset\mathcal H\) and choose
\(M>0\) with \(|z|\le M\) on \(K\). For a complex number \(w\) with
\(|w|\le1/2\), the straight-segment integral gives

\[
\operatorname{Log}(1+w)-w
=-w^2\int_0^1\frac{s}{1+sw}\,ds.
\tag{E21}
\]

The segment remains within \(\Re(1+sw)>0\). Therefore

\[
|\operatorname{Log}(1+w)-w|
\le\frac{|w|^2}{2(1-|w|)}\le|w|^2.
\tag{E22}
\]

For every integer \(j\ge2M\), this bounds the absolute value of the
\(j\)-th summand of (E19) by \(M^2/j^2\), uniformly on \(K\).
The convergence of \(\sum_{j\ge1}j^{-2}\) follows, for example, from
\(\sum_{j>J}j^{-2}\le\int_J^\infty u^{-2}du=1/J\).
The finitely many remaining summands are holomorphic. Consequently

\[
q(z)=\operatorname{Log}z+\gamma z
+\sum_{j=1}^\infty
\left(\operatorname{Log}(1+z/j)-\frac zj\right)
\tag{E23}
\]

is holomorphic on \(\mathcal H\), and \(q_N\to q\) locally uniformly.
The exponentials converge locally uniformly as well. Combining this with
(E16) and the exact finite identity (E20) yields

\[
\Gamma(z)e^{q(z)}
=\lim_{N\to\infty}F_N(z)e^{q_N(z)}=1.
\tag{E24}
\]

It follows, without assuming nonvanishing in advance, that

\[
\boxed{\Gamma(z)=e^{-q(z)}\ne0\qquad(z\in\mathcal H).}
\tag{E25}
\]

Equivalently, the convergent reciprocal product is

\[
\boxed{
\frac1{\Gamma(z)}
=z e^{\gamma z}
\prod_{j=1}^\infty (1+z/j)e^{-z/j}.
}
\tag{E26}
\]

The product in (E26) means the limit of the displayed finite products;
(E21)--(E24) prove its locally uniform convergence and its nonzero value.

## The holomorphic logarithm and its second derivative

Define

\[
\ell(z)=-q(z),\qquad z\in\mathcal H.
\tag{E27}
\]

Then \(e^{\ell(z)}=\Gamma(z)\). When \(z=x>0\), every logarithm in
(E23) is real, so \(\ell(x)\) is the real logarithm of the positive number
\(\Gamma(x)\). In particular, \(\ell(1)=0\) by (E6). Thus (E27)
constructs the precise branch denoted by \(\log\Gamma\), rather than
assuming a branch or taking the pointwise principal logarithm of possibly
nonreal Gamma values.

Set \(\ell_N=-q_N\). Differentiating the finite expression (E19) gives

\[
\ell_N'(z)=\log N-\sum_{j=0}^N\frac1{z+j},
\qquad
\ell_N''(z)=\sum_{j=0}^N\frac1{(z+j)^2}.
\tag{E28}
\]

The derivative convergence in (E16) also justifies this twice-differentiated
limit directly through the original Euler formula. On each compact
\(K\Subset\mathcal H\), continuity and (E25) give
\(m_K=\min_{z\in K}|\Gamma(z)|>0\). For all sufficiently large \(N\),
the uniform convergence of \(F_N\) gives \(|F_N(z)|\ge m_K/2\) on \(K\).
Therefore (E16), applied to the two ratios below, proves

\[
\begin{aligned}
\ell_N''(z)
&=\frac{F_N''(z)}{F_N(z)}
-\left(\frac{F_N'(z)}{F_N(z)}\right)^2\\
&\longrightarrow
\frac{\Gamma''(z)}{\Gamma(z)}
-\left(\frac{\Gamma'(z)}{\Gamma(z)}\right)^2
=\ell''(z)
\end{aligned}
\tag{E29}
\]

locally uniformly. For \(j\ge1\) and \(z\in\mathcal H\),
\(|z+j|\ge\Re(z+j)>j\), so
\(|(z+j)^{-2}|\le j^{-2}\). Thus the sums on the right in (E28) converge
locally uniformly to their infinite series, including the separate
\(j=0\) term. Passing to the limit in (E28)--(E29) proves

\[
\boxed{
(\log\Gamma)''(z)
=\frac1{z^2}+\sum_{j=1}^\infty\frac1{(z+j)^2}
=\sum_{j=0}^\infty\frac1{(z+j)^2},
\qquad\Re z>0.
}
\tag{E30}
\]

For completeness, the first derivative is also explicit:

\[
(\log\Gamma)'(z)
=-\gamma-\frac1z
+\sum_{j=1}^\infty\left(\frac1j-\frac1{j+z}\right).
\tag{E31}
\]

Its series converges locally uniformly since, on \(|z|\le M\) in
\(\mathcal H\),
\(|1/j-1/(j+z)|=|z|/(j|j+z|)\le M/j^2\).
Thus both the product differentiation and the differentiated-integral
argument retain the same logarithmic branch.

## The product form of the beta identity

For \(z,w\in\mathcal H\), the product of the two integrals (E2) is
absolutely convergent on \((0,\infty)^2\): its absolute integrand integrates
to \(\Gamma(\Re z)\Gamma(\Re w)<\infty\). Make the bijective substitution

\[
s=x+y,\qquad u=\frac{x}{x+y},\qquad
x=su,\quad y=s(1-u),
\]

from \(x,y>0\) to \(s>0\), \(0<u<1\). Its signed Jacobian is

\[
\det\frac{\partial(x,y)}{\partial(s,u)}
=\det\begin{pmatrix}u&s\\1-u&-s\end{pmatrix}=-s,
\]

and the absolute Jacobian for integration is \(s\). Since every base is
positive real, addition of real logarithms gives exactly

\[
(su)^{z-1}(s(1-u))^{w-1}s
=s^{z+w-1}u^{z-1}(1-u)^{w-1}.
\]

Fubini's theorem and this substitution therefore prove the product identity

\[
\boxed{\Gamma(z)\Gamma(w)=\Gamma(z+w)B(z,w),
\qquad \Re z,\Re w>0.}
\tag{E32}
\]

This derivation itself does not divide by a Gamma value. By (E25), division
by \(\Gamma(z+w)\) is now justified if the quotient form is desired.

## The Gaussian value

Let

\[
I=\int_{-\infty}^\infty e^{-u^2}\,du.
\]

This integral is finite because \(e^{-u^2}\le e^{-|u|}\) for \(|u|\ge1\),
and it is positive. Tonelli's theorem and polar coordinates give

\[
\begin{aligned}
I^2
&=\int_{\mathbb R^2}e^{-(x^2+y^2)}\,dx\,dy\\
&=\int_0^{2\pi}\int_0^\infty e^{-r^2}r\,dr\,d\theta\\
&=2\pi\left[-\frac12e^{-r^2}\right]_{r=0}^{r=\infty}
=\pi.
\end{aligned}
\tag{E33}
\]

The polar absolute Jacobian is \(r\); one may apply the substitution first
on disks of finite radius and then use monotone convergence. The origin and
the boundary ray of the polar coordinate chart have area zero. Since
\(I>0\), (E33) gives \(I=\sqrt\pi\), the positive square root. Finally,
in (E2) for \(z=1/2\), the substitution \(v=u^2\), \(dv=2u\,du\), gives

\[
\boxed{
\Gamma(1/2)
=\int_0^\infty v^{-1/2}e^{-v}\,dv
=2\int_0^\infty e^{-u^2}\,du
=\sqrt\pi.
}
\tag{E34}
\]

## Duplication with all substitution factors retained

Take \(z\in\mathcal H\). In (E7) for \(B(z,z)\), use
\(u=(1+y)/2\), so \(du=dy/2\) and
\(u(1-u)=(1-y^2)/4\). All complex powers use positive real bases in the
interiors of their intervals. The successive substitutions and evenness give

\[
\begin{aligned}
B(z,z)
&=\int_0^1[u(1-u)]^{z-1}\,du\\
&=\frac{4^{1-z}}2\int_{-1}^1(1-y^2)^{z-1}\,dy\\
&=2^{1-2z}\int_{-1}^1(1-y^2)^{z-1}\,dy\\
&=2^{2-2z}\int_0^1(1-y^2)^{z-1}\,dy\\
&=2^{2-2z}\frac12\int_0^1
v^{-1/2}(1-v)^{z-1}\,dv\\
&=2^{1-2z}B(1/2,z).
\end{aligned}
\tag{E35}
\]

In the penultimate line the substitution is \(v=y^2\), with
\(dy=dv/(2\sqrt v)\). Absolute convergence follows from \(\Re z>0\),
and is preserved at each step.

Use (E32) and then (E35), retaining their product form:

\[
\begin{aligned}
\Gamma(z)^2\Gamma(z+1/2)
&=\Gamma(2z)B(z,z)\Gamma(z+1/2)\\
&=2^{1-2z}\Gamma(2z)B(1/2,z)\Gamma(z+1/2)\\
&=2^{1-2z}\Gamma(2z)\Gamma(1/2)\Gamma(z).
\end{aligned}
\tag{E36}
\]

The value \(\Gamma(z)\) is nonzero by the independently established
reciprocal limit (E24)--(E25), so cancellation of this factor is justified.
Substitution of (E34) proves the exact duplication formula

\[
\boxed{
\Gamma(z)\Gamma(z+1/2)
=2^{1-2z}\sqrt\pi\,\Gamma(2z),
\qquad \Re z>0,
}
\tag{E37}
\]

where \(2^{1-2z}=\exp((1-2z)\log2)\). The beta and Gaussian derivations
introduce no Gamma normalization other than the defining integral (E2).

## Completion and dependency record

The derivations above prove (E17), local uniform convergence through the
second derivative, nonvanishing on the whole stated domain, the real-axis
branch of \(\log\Gamma\), the exact series (E30), and duplication (E37).
They use the displayed defining integrals and elementary integration,
dominated convergence, holomorphic differentiation under an integrable
dominator, and locally uniform convergence of holomorphic series. No
unproved Gamma identity, asymptotic Stirling formula, RH assumption, or
numerical Gamma evaluation was used. No Lean, Lake, or Elan process was run.
