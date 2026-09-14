---
title: "A complete retraction proof on the original theta source"
date: "2026-09-13"
---

# 1. Original spaces and the fixed auxiliary functions

Work over \(\mathbb C\), with Fourier convention
\[
\widehat\phi(\xi)=\int_{\mathbb R}\phi(x)e^{-2\pi ix\xi}\,dx.
\]
Retain the original spaces, with their indicated seminorm topologies:
\[
V=\{\phi\in\mathcal S(\mathbb R):\phi(-x)=\phi(x),\
\phi(0)=0,\ \widehat\phi(0)=0\},
\]
\[
\mathscr B=\{F\in C^\infty(\mathbb R_{>0}):
p_{b,k}(F)=\sup_{x>0}x^b|D^kF(x)|<\infty
\quad(b\in\mathbb Z,\ k\ge0)\},\qquad D=-x\partial_x.
\]
Use Schwartz seminorms
\(\sigma_{m,j}(u)=\sup_{x\in\mathbb R}(1+|x|)^m|u^{(j)}(x)|\).
The Fourier transform preserves the even Schwartz space and satisfies
\(\mathcal F^2\phi(x)=\phi(-x)\). Consequently it preserves \(V\), since
\(\widehat\phi(0)=\int\phi\) and
\(\int\widehat\phi=\phi(0)\).

Fix the following explicit smooth functions for the entire construction:
\[
h(t)=
\begin{cases}
e^{-1/t},&t>0,\\
0,&t\le0,
\end{cases}
\qquad
\chi(x)=
\frac{h(1/16-x^2)}
{h(1/16-x^2)+h(x^2-1/64)},\qquad \alpha=\beta=\chi.
\]
All derivatives of \(h\) at zero vanish: each derivative for \(t>0\)
is a polynomial in \(1/t\) times \(e^{-1/t}\), which tends to zero.
The denominator defining \(\chi\) never vanishes, since its two
arguments cannot both be nonpositive. Thus \(\chi\) is real, even,
smooth, lies in \([0,1]\), equals one for \(|x|\le1/8\), and vanishes
for \(|x|\ge1/4\). In particular
\[
\|\chi\|_2^2\le\frac12.
\]
These are choices of reconstruction data on the original coordinates.
The spaces, Fourier convention and arithmetic theta map remain exactly
those displayed here.

# 2. Theta continuity and recovery on both exterior regions

The original maps are
\[
\Theta\phi(x)=\sum_{n\ne0}\phi(nx)=2\sum_{n\ge1}\phi(nx),
\qquad JF(x)=x^{-1}F(1/x).
\]
Poisson summation gives \(\Theta\mathcal F=J\Theta\) on \(V\).
For this identity, periodize the Schwartz function
\(t\mapsto\phi(xt)\); its Fourier coefficients are
\(x^{-1}\widehat\phi(n/x)\), obtained by integrating over all translated
unit intervals. Both the periodization and its Fourier series converge
absolutely with derivatives. Evaluation at zero gives
\(\sum_n\phi(nx)=x^{-1}\sum_n\widehat\phi(n/x)\).
The two zero-index terms vanish by the original moments.

The theta map is continuous into \(\mathscr B\). Indeed, for \(x\ge1\),
an integer \(N>1\), and
\(s_{N,k}(\phi)=\sup_{t>0}t^N|D^k\phi(t)|\),
\[
|D^k\Theta\phi(x)|
\le2\zeta(N)s_{N,k}(\phi)x^{-N}.
\]
Each \(s_{N,k}\) is bounded by finitely many Schwartz seminorms.
Choosing \(N\ge b\) bounds the part of \(p_{b,k}\) on \(x\ge1\).
The identities
\[
D^kJ=J(1-D)^k,\qquad
p_{b,k}(JF)\le\sum_{j=0}^k\binom{k}{j}p_{1-b,j}(F)
\]
follow by differentiating \(x^{-1}F(1/x)\).
For \(x\le1\), apply the preceding theta estimate to
\(\widehat\phi\) at \(1/x\); choosing also \(N\ge1-b\) bounds this
part by
\(2\zeta(N)\sum_{j=0}^k\binom{k}{j}s_{N,j}(\widehat\phi)\).
This proves every required bound and also continuity of \(J\).

For \(x\ne0\), define the actual arithmetic inverse series
\[
\mathcal UF(x)=\frac12\sum_{n\ge1}\mu(n)F(n|x|).
\]
Here \(\mu\) is the ordinary Möbius function; the factor \(1/2\)
inverts the sum over both nonzero integer signs. Put
\[
P_j(T)=(-1)^jT(T+1)\cdots(T+j-1),\quad P_0=1,\qquad
C_{N,j}(F)=\sum_{k=0}^j|[T^k]P_j(T)|p_{N,k}(F).
\]
The identity \(x^j\partial_x^j=P_j(D)\) follows by induction.
Therefore, for \(x>0\) and integer \(N>1\),
\[
|\partial_x^j\mathcal UF(x)|
\le\frac{\zeta(N)}2C_{N,j}(F)x^{-N-j}.                 \tag{1}
\]
The same absolute bound holds for negative \(x\). It proves locally
uniform convergence of every differentiated series away from zero.

For \(\phi\in V\), the divisor rearrangement is legitimate: for fixed
\(x>0\),
\(\sum_{m,n\ge1}|\phi(mnx)|\) is finite, by a Schwartz bound of
degree \(N>1\) and \(\sum_{m,n}(mn)^{-N}=\zeta(N)^2\).
Thus
\[
\mathcal U\Theta\phi(x)
=\sum_{k\ge1}\left(\sum_{d\mid k}\mu(d)\right)\phi(kx)
=\phi(x).
\]
The divisor sum is one for \(k=1\) and zero otherwise: prime
factorization gives the product \(\prod_{p\mid k}(1-1)\) when \(k>1\).
Evenness gives recovery on negative \(x\), and Poisson summation gives
the second exterior recovery:
\[
\boxed{\mathcal U\Theta\phi=\phi,\qquad
\mathcal UJ\Theta\phi=\widehat\phi\quad(x\ne0).}         \tag{2}
\]
In particular \(\Theta\) is injective, including at zero by continuity.
No information about zeros of zeta in a critical strip enters this proof.

# 3. Fixed contraction and full Schwartz estimates

On \(L^2(\mathbb R,dx)\), set
\[
A=M_\chi,\qquad B=\mathcal F^{-1}M_\chi\mathcal F,\qquad T=AB.
\]
Its integral kernel is \(\chi(x)\check\chi(x-y)\).
Plancherel and the change of variable \(z=x-y\) give
\[
\|T\|^2\le\|T\|_{\rm HS}^2
=\|\chi\|_2^2\|\check\chi\|_2^2
=\|\chi\|_2^4\le\frac14.
\]
Consequently the operator-norm convergent series supplies the actual inverse:
\[
\boxed{(1-T)^{-1}=\sum_{n=0}^{\infty}T^n,\qquad
\|(1-T)^{-1}\|\le2.}                                 \tag{3}
\]
Multiplying its partial sums by \(1-T\) leaves \(1-T^{n+1}\),
which tends to the identity, proving both inverse identities.

Define exterior functions, extended by zero near the origin, by
\[
a_F=(1-\chi)\mathcal UF,\qquad
b_F=(1-\chi)\mathcal UJF,\qquad
YF=a_F+\chi\mathcal F^{-1}b_F.
\]
Here are explicit bounds verifying all their Schwartz seminorms.
Write \(c_0=1\) and \(c_r=\|\chi^{(r)}\|_\infty\) for \(r\ge1\).
Leibniz's rule and (1), with \(N=m+2\), give
\[
\sigma_{m,j}(a_F)
\le\frac{\zeta(m+2)}2\,9^m
\sum_{r=0}^j\binom jr c_r\,8^{2+j-r}C_{m+2,j-r}(F).  \tag{4}
\]
Indeed every nonzero differentiated term occurs at \(|x|\ge1/8\),
where \(1+|x|\le9|x|\) and
\(|x|^{-2-j+r}\le8^{2+j-r}\).
The same bound holds for \(b_F\) with \(JF\) in place of \(F\);
the displayed bounds for \(J\) express it in finitely many original
\(p_{b,k}(F)\). Smoothness across the plateau endpoints follows from
smoothness of the cutoffs and their identically zero interior factors.

Fourier inversion is continuous on these Schwartz seminorms. Explicitly,
integration by parts gives
\[
\sigma_{m,j}(\mathcal F^{-1}u)
\le\sum_{r=0}^m\binom mr(2\pi)^{j-r}
\bigl\|\partial_\xi^r(\xi^ju)\bigr\|_1.
\]
Each integral on the right is bounded by a finite sum of Schwartz
seminorms, using Leibniz's rule and
\(\int_{\mathbb R}(1+|\xi|)^{-2}d\xi=2\).
Together with (4), this proves that \(Y:\mathscr B\to\mathcal S^{\rm even}\)
is continuous.

The operator \(T\) also maps \(L^2\) continuously to Schwartz space.
Put
\[
b_j=\|(2\pi\xi)^j\chi(\xi)\|_2
\le\frac{(\pi/2)^j}{\sqrt2},\qquad
A_{m,j}=(5/4)^m
\sum_{r=0}^j\binom jr\|\chi^{(r)}\|_\infty b_{j-r}.
\]
Cauchy–Schwarz in the Fourier integral bounds
\(\|\partial^jBf\|_\infty\) by \(b_j\|f\|_2\).
Leibniz's rule and the support of \(\chi\) therefore give
\[
\sigma_{m,j}(Tf)\le A_{m,j}\|f\|_2.
\]
Set \(\Phi F=(1-T)^{-1}YF\), initially in \(L^2\).
The equation \(\Phi F=YF+T\Phi F\) proves that it is Schwartz, and
supplies the explicit continuity estimate
\[
\sigma_{m,j}(\Phi F)
\le\sigma_{m,j}(YF)+2A_{m,j}\|YF\|_2.                 \tag{5}
\]
The final \(L^2\) norm is bounded by
\(\sqrt2\,\sigma_{1,0}(YF)\).
Every operator preserves parity; hence \(\Phi F\) is even.
Equations (2) give
\[
Y\Theta\phi=(1-A)\phi+A(1-B)\phi=(1-T)\phi,
\qquad \Phi\Theta\phi=\phi.                          \tag{6}
\]

# 4. The original moment correction and exact splitting

Retain
\[
\gamma_0(x)=e^{-\pi x^2},\qquad
\gamma_2(x)=2\pi x^2e^{-\pi x^2}.
\]
Their moment columns \((\phi(0),\int_{\mathbb R}\phi)\) are
\((1,1)\) and \((0,1)\).
For the integral constants, the square of the Gaussian integral is
the planar polar integral \(2\pi\int_0^\infty re^{-\pi r^2}dr=1\).
Integrating \(\partial_x(xe^{-\pi x^2})\) then gives
\(2\pi\int x^2e^{-\pi x^2}dx=1\).
Thus the continuous projection
\[
P_Vu=u-u(0)\gamma_0-
\left(\int_{\mathbb R}u-u(0)\right)\gamma_2
\]
has both original moments zero and is identity on \(V\).
Continuity follows from
\(|u(0)|\le\sigma_{0,0}(u)\) and
\(|\int u|\le2\sigma_{2,0}(u)\).
The required map is therefore
\[
\boxed{\Lambda=P_V(1-T)^{-1}Y:\mathscr B\longrightarrow V,
\qquad \Lambda\Theta=1_V.}                           \tag{7}
\]
All constants and seminorm dependence have been supplied in (1)–(5).
For the original quotient \(q:\mathscr B\to Q=\mathscr B/\Theta V\),
put \(K=1-\Theta\Lambda\).
Equation (7) gives \(K^2=K\), \(\ker K=\Theta V\), and
\(\operatorname{im}K=\ker\Lambda\).
The image \(\Theta V\) is closed because it is the kernel of continuous
\(K\). The continuous map \(K\) descends by the quotient topology to
\[
s:Q\to\mathscr B,\qquad s[F]=KF,\qquad
qs=1,\quad\Lambda s=0,\quad\Theta\Lambda+sq=1.
\]
These equations prove the continuous inverse pair
\[
V\oplus Q\longrightarrow\mathscr B,\quad
(\phi,u)\longmapsto\Theta\phi+su,\qquad
F\longmapsto(\Lambda F,qF).
\]

Finally, retain \(U_aF(x)=F(x/a)\).
It is continuous because \(p_{b,k}(U_aF)=a^bp_{b,k}(F)\);
its source action preserves \(V\) and obeys
\(U_a\Theta=\Theta U_a\).
It therefore induces \(\overline U_a\) on \(Q\).
Put \(k_a=\Lambda U_as\).
The decomposition of \(U_as\) gives
\[
U_as=\Theta k_a+s\overline U_a,\qquad
k_{ab}=U_ak_b+k_a\overline U_b,\qquad k_1=0.
\]
For the middle identity, substitute the first identity with parameter
\(b\) into \(\Lambda U_aU_bs\), and use
\(\Lambda U_a\Theta=U_a\) and \(\Lambda U_as=k_a\).
Writing \(F=\Theta\Lambda F+s qF\) also proves
\[
U_a\Lambda-\Lambda U_a=-k_aq.
\]
Consequently the reversed-support dual roof's action defect is exactly
\[
\boxed{d_a(c)=-a^wc\mathcal F^{-1}k_{1/a}.}
\]
This connects the completed retraction to the original action on
the full \(Q\), retaining its Fourier inverse, weight factor, reciprocal
parameter and sign. The calculation does not set this cocycle to zero.
