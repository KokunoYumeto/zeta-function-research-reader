# The continuing prime-two channel in the actual heat derivative

<!-- original-zeta-reconstruction-start -->
**Original-zeta receiving calculation.** The working meromorphic function is the original Riemann zeta, with its full Gamma/endpoints multiplier and its full trivial-zero and pole divisor retained. [TF1–42](FAITHFUL_THETA_COMPLETION_RETURN.md) proves the original labelled theta inverse and the actual heat-image defect. [UZ1–53](FAITHFUL_UNCOMPLETED_ZETA_HEAT.md) proves every exceptional-point fibre, jet, original-zeta heat term and reflection orientation. [OZC1–48](ORIGINAL_ZETA_COMPACT_WEIL_RECONSTRUCTION.md) rederives the compact contour and interval operator directly from zeta, including the left-cutoff Gamma boundary, and specifies exactly which compensated pairing the bounds concern. [OZH1–49](ORIGINAL_ZETA_HEAT_CONTACT_RECONSTRUCTION.md) rederives the actual meromorphic heat, rational signed trace, compact-test domain, contact drift and full causal arithmetic variation. The raw full divisor and the compensated Weil receiver are linked by their displayed correction, not identified. In particular the fixed-test trivial-zero sum converges exactly at translations at least 1/32 and equals the earlier R term; at zero translation it requires the proved cutoff compensation. [OZK1–38](ORIGINAL_ZETA_CAUCHY_RECONSTRUCTION.md) reconstructs the original signed Cauchy trace, its full Gamma correction, resonant finite parts, every finite matrix and its index, and the complete local heat jets. Its invertible map retains the raw trace and correction separately. These complete receiving proofs govern the interpretation of the retained auxiliary calculations below.
<!-- original-zeta-reconstruction-end -->


This calculation keeps the original fixed test and heat time. Immediately after the prime-two window in the zero-time Weil pairing has ended, its mixed endpoint/Gamma–prime heat channel is still strictly negative. The complete archimedean heat term is evaluated by an exact convergent series and bounded independently. Together these calculations prove that the actual full right heat derivative of this fixed correlation is strictly negative throughout the stated closed interval. This sign concerns the original whole-zero-set correlation, not positivity of every Weil test.

## 1. Fixed objects, interval and the actual derivative

Use the probability density and convolution of PW3–5, with their original radius:
\[
r=\frac1{64},\quad
b=\mathop{*}_{j\ge1}\frac{\mathbf1_{[-r2^{-j},r2^{-j}]}}{2r2^{-j}},
\quad k=b^\#*b=b*b,\quad T=D^2-\tfrac14,
\quad f=Tb,\quad h=f^\#*f=T^2k.
\tag{PT1}
\]
Thus \(b\) and \(k\) are real, even, nonnegative smooth probability densities, with supports contained in \([-r,r]\) and \([-2r,2r]\). The compact functions \(h\) and \(k\), with all their derivatives, vanish at and outside the endpoints \(\pm2r\). The proof uses containment of the supports, not equality with the entire containing intervals. Let
\[
L=\log2,\qquad \beta=\frac{L}{\sqrt2},\qquad
A_* =\frac{19}{25}-2r,
\qquad I=[L+2r,A_*],\qquad
A_a(s)=M_{h(\cdot+a)}(s).
\tag{PT2}
\]
The scalar \(L\) in this note is distinct from the programme's support lattice.

The interval is nonempty. The exact expansion
\[
\log2=2\sum_{j\ge0}\frac{1}{(2j+1)3^{2j+1}}
\tag{PT3}
\]
follows by integrating the uniformly convergent geometric series for \((1-u^2)^{-1}\) from 0 to \(1/3\). Its first term gives \(L>2/3\). Bounding \(2j+1\ge3\) for \(j\ge1\) gives \(L<2/3+1/36=25/36<279/400=19/25-4r\). This proves nonemptiness with the fixed constants retained. Set
\[
d=\frac{19}{25}-L.
\quad\text{Then}\quad 0<d<\frac7{75}<\frac1{10}.
\tag{PT4}
\]

Let \(g_t(s)=16H_t(-2i(s-1/2))\) be the original heat family, and define the complete actual zero trace
\[
K_t(a)=Z_t(A_a)=\sum_{g_t(\rho)=0}m_{\rho,t}A_a(\rho),\qquad t\ge0.
\tag{PT5}
\]
RT12–16 proves that this is smooth in nonnegative real time and that the derivative at zero from the right is the CH receiver. In particular, with the exact causal \(\alpha\) of CH4, \(\pi=\sum_{n\ge2}\Lambda(n)n^{-1/2}\delta_{\log n}\), and \(\ell=\alpha-\pi\),
\[
4\dot K_{0+}(a)
=\left\langle v^2\ell-v(\ell*\ell),
h(v+a)+h(a-v)\right\rangle.
\tag{PT6}
\]
This note uses that accepted real-time theorem, not an unproved derivative of an unrestricted moving-zero sum.

## 2. Complete specialization on the first gap

For \(a\in I\), the first test in (PT6) vanishes on the causal half-line because \(a>2r\). The second has support in \([a-2r,a+2r]\subset[L,19/25]\). The bound \(\log3\ge1>19/25\) follows from \(\log x\ge2(x-1)/(x+1)\) for \(x\ge1\); differentiating the difference gives \((x-1)^2/[x(x+1)^2]\ge0\). Therefore only the prime-power index 2 can occur in the pure-prime or mixed-prime sums of CH24. The smallest ordered product of two indices with nonzero von Mangoldt coefficient is 4, and \(\log4=2L>4/3>19/25\), so the prime-product term has no nonzero-amplitude contribution. Consequently the complete specialization is
\[
\begin{aligned}
4\dot K_{0+}(a)={}&
\left\langle v^2\alpha-v(\alpha*\alpha),h(a-v)\right\rangle
-\beta L^2h(a-L)\\
&+2\beta\left\langle\alpha,(v+L)h(a-L-v)\right\rangle,
\qquad a\in I.
\end{aligned}
\tag{PT7}
\]
Every endpoint/Gamma contribution remains in \(\alpha\). Since \(a-L\ge2r\), including its left endpoint where the compact test is flat, \(h(a-L)=0\). Thus, writing
\[
\mathcal A(a)=\frac14\left\langle v^2\alpha-v(\alpha*\alpha),h(a-v)\right\rangle,
\qquad
\mathcal C_2(a)=\frac\beta2\left\langle\alpha,(v+L)h(a-L-v)\right\rangle,
\tag{PT8}
\]
one has the exact equality
\[
\boxed{\dot K_{0+}(a)=\mathcal A(a)+\mathcal C_2(a),\qquad a\in I.}
\tag{PT9}
\]
At time zero the original PW13 prime term likewise vanishes, giving \(K_0(a)=-R_r(a)\) on this interval. The operator \(\mathcal C_2\) in (PT8) is a different, surviving term of its heat derivative.

## 3. An ordinary integral for the mixed channel, including the left endpoint

Away from zero, the full causal distribution has its original density
\[
\alpha_0(v)=e^{-v/2}+e^{v/2}-w(v),\qquad
w(v)=\frac{e^{-v/2}}{1-e^{-2v}}=\frac{e^{v/2}}{2\sinh v},\qquad v>0.
\tag{PT10}
\]
Let \(c=a-L\). The mixed test has support in \([c-2r,c+2r]\subset[0,d]\). When \(c>2r\), it vanishes near zero, so the subtraction and delta term in CH4 do not contribute and its action is integration against (PT10). When \(c=2r\), the same assertion follows from flatness: \((v+L)h(2r-v)\) and every derivative are \(O(v^N)\) for every fixed \(N\) as \(v\downarrow0\). In particular its value at zero is zero, and the remaining \(O(v^{-1})\) density is integrable against it. Thus both endpoint cases give exactly
\[
\mathcal C_2(a)=\frac\beta2\int_{c-2r}^{c+2r}
(v+L)\alpha_0(v)T_v^2k(c-v)\,dv.
\tag{PT11}
\]
At the left endpoint the integral is interpreted by its convergent limit from \(v>0\); it has no unspecified finite part.

Four integrations by parts move \(T_v^2\) onto \((v+L)\alpha_0(v)\). The upper support boundary contributes zero because \(k\) is flat. At \(v=0\), when present, each derivative of order at most three of the kernel is \(O(v^{-4})\), while every derivative of the compact factor is \(O(v^N)\) for every \(N\). Hence all those boundary terms also tend to zero. For \(\lambda=\pm1/2\),
\(T((v+L)e^{\lambda v})=2\lambda e^{\lambda v}\) and \(Te^{\lambda v}=0\); therefore their second application vanishes exactly. Define
\[
W(v)=T_v^2w(v),\qquad B(v)=T_v^2(vw(v)),\qquad
H_L(v)=LW(v)+B(v).
\tag{PT12}
\]
The complete mixed integral is then
\[
\boxed{\mathcal C_2(a)=-\frac\beta2\int_{c-2r}^{c+2r}
H_L(v)k(c-v)\,dv.}
\tag{PT13}
\]
This is an exact calculation of the continuing channel, not a deletion of the endpoint densities: their stated differential image has been proved zero.

## 4. Reproducing the complex-circle estimate and the strict sign

The bounded analytic remainder used in the incoming N52 is exactly
\[
r_0(z)=w(z)-\frac1{2z},\qquad b_0(z)=zw(z)=\frac12+zr_0(z).
\tag{PT14}
\]
Both singularities at zero are removable, by the Taylor series of \(e^{z/2}\) and \(\sinh z\). They are holomorphic in a neighborhood of \(|z|\le2\). Indeed the only zeros of \(\sinh(x+iy)\) have \(x=0\), \(\sin y=0\); for \(0<|y|\le2\), the Taylor lower bound \(\sin|y|\ge |y|-|y|^3/6>0\) excludes such a zero.

Here is the circle bound with its full proof. On \(|z|=2\), write \(z=x+iy\). The identity
\( |\sinh z|^2=\sinh^2x+\sin^2y\)
and \(|\sinh x|\ge|x|\) give
\[
|\sinh z|^2\ge x^2+\left(\frac{\sin2}{2}\right)^2y^2
\ge\left(\frac{\sin2}{2}\right)^2(x^2+y^2)=\sin^22.
\tag{PT15}
\]
The first inequality uses that \(\sin y/y\) decreases on \([0,2]\): the derivative numerator \(y\cos y-\sin y\) has derivative \(-y\sin y\le0\) and starts at zero. Alternating Taylor terms give
\(\sin2>2-2^3/3!+2^5/5!-2^7/7!=286/315>9/10\).
Also \(e<65/24+1/100=1631/600<11/4\): sum its first five Taylor terms and bound the tail from \(1/5!\) by the geometric ratio \(1/6\). Therefore, on the circle,
\[
|r_0(z)|\le\frac{e}{2\sin2}+\frac14
<\frac{55}{36}+\frac14=\frac{16}{9}<2,
\quad |b_0(z)|<\frac92.
\tag{PT16}
\]
The maximum principle gives the same latter bound throughout the closed disc. This reproduces the actual incoming circle estimate without relying on numerical sampling of the kernel.

For \(0\le v\le d<1/10\), use the Cauchy derivative circle of radius \(2-v\ge19/10\) centered at \(v\). Since \(B=T^2b_0=b_0^{(4)}-b_0''/2+b_0/16\),
\[
\begin{aligned}
|B(v)|
&<\frac{108}{(19/10)^4}+\frac{9/2}{(19/10)^2}+\frac9{32}<10,\\
10-\left\{\frac{108}{(19/10)^4}+\frac{9/2}{(19/10)^2}+\frac9{32}\right\}
&=\frac{771431}{4170272}>0.
\end{aligned}
\tag{PT17}
\]
Every constant follows from \(4!(9/2)=108\), \((1/2)2!(9/2)=9/2\), and the retained coefficient \(1/16\).

PW16 independently proves, with \(\lambda_j=2j+1/2\),
\[
W(v)=\sum_{j\ge1}4j^2(2j+1)^2e^{-\lambda_jv}
=\frac{4e^{-5v/2}(9+55e^{-2v}+31e^{-4v}+e^{-6v})}{(1-e^{-2v})^5}.
\tag{PT18}
\]
For \(0<v\le d<1/10\), its first term gives
\(W(v)\ge36e^{-5v/2}>27\), using \(e^{-x}>1-x\) for \(x>0\). Together with \(L>2/3\) and (PT17), this proves
\[
H_L(v)>18-10=8\qquad(0<v\le d).
\tag{PT19}
\]
The weight \(k(c-v)dv\) in (PT13) is nonnegative and has total mass one: its whole support lies in the displayed interval since \(c\ge2r\). Its possible endpoint at zero has no atom. It follows that
\[
\boxed{\mathcal C_2(a)<-4\beta=-\frac{4\log2}{\sqrt2}<0,
\qquad L+2r\le a\le\frac{19}{25}-2r.}
\tag{PT20}
\]
At the boundary \(v=0\), the integrable product with the flat density was proved in Section 3, so no divergent lower-end term has been assigned a sign.

## 5. The exact mixed tail outside the original window

The definition of \(\mathcal C_2(a)\) in (PT8) makes sense for every real \(a\) and is smooth in \(a\). On each compact interval of \(a\), its translated test and all parameter derivatives have a common compact support and converge in the smooth test topology; continuity of the distribution \(\alpha\) proves the assertion. Causality makes it vanish for \(a<L-2r\). Its ordinary-integral formula (PT13) is valid for every \(a\ge L+2r\), even when other channels enter the whole heat derivative.

For a further explicit expression, put \(c_j=\lambda_j^2-1/4=2j(2j+1)\). Differentiation of \(v e^{-\lambda_jv}\) gives
\[
H_L(v)=\sum_{j\ge1}\{c_j^2(v+L)-4\lambda_jc_j\}e^{-\lambda_jv}.
\tag{PT21}
\]
Let \(G(z)=M_b(1/2-z)=\int b(u)e^{zu}du\), the same original even product \(G_r\) as in PW3, and set \(S(z)=G(z)^2=\int k(u)e^{zu}du\). Then
\[
\boxed{\mathcal C_2(a)=-\frac\beta2
\sum_{j\ge1}e^{-\lambda_j(a-L)}
\left[\{c_j^2a-4\lambda_jc_j\}S(\lambda_j)-c_j^2S'(\lambda_j)\right],
\quad a\ge L+2r.}
\tag{PT22}
\]
To prove it substitute \(u=a-L-v\) in (PT13) and integrate each term in (PT21). For the boundary value \(a=L+2r\), absolute interchange remains valid: smooth compact support and integration by parts give \(|S(\lambda)|+|S'(\lambda)|\le C_Ne^{2r\lambda}(1+\lambda)^{-N}\) for every \(N\) on positive real \(\lambda\). The powers of \(j\) in (PT22) are therefore summable. Alternatively the absolute exponential series in (PT21), multiplied by the flat \(k(2r-v)\), is integrable near zero. The same estimates prove local uniform convergence of (PT22) and all its \(a\) derivatives on this closed half-line. This records the exact continuing tail with its original test, rather than extending a finite prime atom by assertion.

## 6. Closed expression for the full remaining archimedean term

The term \(\mathcal A(a)\) in (PT8) is still part of the complete derivative. It has an exact convergent formula on the required interval. Retain
\[
c_0=\frac{\gamma+\log\pi}{2},\quad E(v)=e^{v/2}\mathbf1_{v>0},\quad
g(v)=-\tfrac12e^{-v/2}\log(1-e^{-2v})\mathbf1_{v>0}.
\tag{PT23}
\]
CH7–9 proves the full distribution identity
\(\alpha=E+(D+1/2)g-c_0\delta_0\), with \(g\) a locally integrable density. In the following convolution calculations, these causal functions denote their density measures and differentiation is distributional. For \(v>0\), write
\[
\lambda_n=2n+\tfrac12,\qquad
g(v)=\frac12\sum_{n\ge1}\frac{e^{-\lambda_nv}}n,\qquad
C(v)=(g*g)(v).
\tag{PT24}
\]
The original convolution definition, or Tonelli applied to its positive series, gives
\[
\boxed{C(v)=\frac14\sum_{n\ge1}\frac{e^{-\lambda_nv}}{n^2}
\left(v+\frac1n-H_{n-1}\right),\qquad H_0=0,
\quad H_j=\sum_{m=1}^j\frac1m.}
\tag{PT25}
\]
Here is the full grouping verification. The diagonal product terms give \(v e^{-\lambda_nv}/(4n^2)\). A product with distinct indices \(m,n\) has convolution \((e^{-\lambda_nv}-e^{-\lambda_mv})/[2(m-n)]\). After accounting for both orders, its total coefficient at \(e^{-\lambda_nv}\) is
\[
\frac1{4n}\sum_{m\ne n}\frac1{m(m-n)}
=\frac1{4n^2}\left(\frac1n-H_{n-1}\right).
\tag{PT26}
\]
The last equality follows from \(1/[m(m-n)]=(1/n)\{1/(m-n)-1/m\}\) and a finite partial sum, followed by its limit. The regrouping is absolutely justified: writing \(m=n+k\) bounds its total by a constant times
\(\sum_{k\ge1}H_k/k^2<\infty\), since \(H_k\le1+\log k\). On each \(v\ge\varepsilon>0\), every differentiated series is likewise uniformly absolutely convergent, by its exponential factor. Therefore all derivatives used below are ordinary derivatives of the original convolution density there.

The endpoint density gives \(E*E=ve^{v/2}\) and
\[
(D+\tfrac12)(E*g)=g+E*g,\qquad
2(E*g)(v)=e^{v/2}\sum_{n\ge1}\frac{1-e^{-(2n+1)v}}{n(2n+1)}.
\tag{PT27}
\]
The first identity follows by differentiating \(\int_0^v e^{(v-u)/2}g(u)du\). The second follows by integrating the positive series (PT24). The sum of its constant coefficients is
\[
\sum_{n\ge1}\frac1{n(2n+1)}=2-2\log2.
\tag{PT28}
\]
For proof use \(1/[n(2n+1)]=1/n-2/(2n+1)\); finite partial sums equal \(2H_N-2H_{2N+1}+2\), which tend to \(2-2\log2\). The difference \(H_{2N+1}-H_N\to\log2\) follows by upper and lower integral bounds for \(1/x\) on \([N,2N+1]\).

Applying \((D+1/2)^2\) to (PT25) gives
\[
(D+\tfrac12)^2C(v)=\sum_{n\ge1}(v-H_{n-1})e^{-\lambda_nv},\qquad v>0.
\tag{PT29}
\]
Indeed the shifted differential operator acts on a summand \(e^{-\lambda_nv}(v+1/n-H_{n-1})\) as
\(e^{-\lambda_nv}\{4n^2(v+1/n-H_{n-1})-4n\}\), cancelling its \(1/n\) after division by \(4n^2\).

Now expand the complete square of the distribution in (PT23). For \(v>0\), the \(c_0^2\delta_0\) term has no density there, while every other term remains:
\[
\begin{aligned}
q(v):=(\alpha*\alpha)(v)
={}&ve^{v/2}+2g(v)+2(E*g)(v)
+(D+\tfrac12)^2C(v)-2c_0\alpha_0(v)\\
={}&(v+2-2L-2c_0)e^{v/2}\\
&+\sum_{n\ge1}
\left(v-H_{n-1}+\frac{2}{2n+1}+2c_0\right)e^{-\lambda_nv}.
\end{aligned}
\tag{PT30}
\]
The first line is obtained by expanding \([E+(D+1/2)g-c_0\delta_0]^2\); the second uses (PT24) and (PT27)–(PT29), together with
\(\alpha_0(v)=e^{v/2}-\sum_{n\ge1}e^{-\lambda_nv}\).
No endpoint coefficient or subtraction constant is absent in (PT30).

Put
\[
d_n=H_{n-1}-\frac2{2n+1}-2c_0,\qquad c_n=\lambda_n^2-\tfrac14=2n(2n+1).
\tag{PT31}
\]
The exact density of \(v^2\alpha-v(\alpha*\alpha)\), away from zero, is
\[
S_\alpha(v)=2(L+c_0-1)v e^{v/2}
+\sum_{n\ge1}(-2v^2+d_nv)e^{-\lambda_nv}.
\tag{PT32}
\]
The compact test in \(\mathcal A(a)\) has support in \([a-2r,a+2r]\subset[L,19/25]\), strictly separated from zero. Therefore it receives this density exactly; no origin distribution has been discarded on its support. Four integrations by parts give
\[
\boxed{\mathcal A(a)=\frac14\int_{a-2r}^{a+2r}\mathcal W_\alpha(v)k(a-v)\,dv,}
\tag{PT33}
\]
where its full normally convergent kernel is
\[
\begin{aligned}
\mathcal W_\alpha(v)=T_v^2S_\alpha(v)
=\sum_{n\ge1}e^{-\lambda_nv}\Big[
-2c_n^2v^2+(c_n^2d_n+16\lambda_nc_n)v
-4\lambda_nc_nd_n-16\lambda_n^2-8c_n\Big],\quad v>0.
\end{aligned}
\tag{PT34}
\]
To verify the polynomial, conjugate \(T\) by \(e^{-\lambda_nv}\): it becomes \(D^2-2\lambda_nD+c_n\). Its square acting on \(P(v)=-2v^2+d_nv\) is
\(c_n^2P-4\lambda_nc_nP'+(4\lambda_n^2+2c_n)P''\), which is the displayed expression. The separate \(v e^{v/2}\) term in (PT32) is annihilated by \(T^2\), as proved in Section 3. Every differentiated series converges uniformly on the present compact interval, because its coefficients have only polynomial and harmonic-number growth and \(v\ge L>0\).

Equations (PT9), (PT13), and (PT33)–(PT34) are the complete original first heat derivative on the specified interval. The following bounds compare both terms; no term of this equality is replaced by a sign assumption.

## 7. A rational bound for the complete actual derivative

First strengthen the mixed bound without changing its kernel. By the positive rational expression in (PT18), \(1-e^{-2v}\le2v\), and \(0<v\le d<1/10\),
\[
W(v)\ge\frac{36e^{-5v/2}}{(2v)^5}
=\frac{9e^{-5v/2}}{8v^5}>84375.
\quad\text{Hence}\quad
H_L(v)>56250-10=56240,
\quad\boxed{\mathcal C_2(a)<-28120\beta.}
\tag{PT35}
\]
The strict numerical bound uses \(e^{-5v/2}>3/4\) and \(v^{-5}>100000\). The factor \(L>2/3\), the derivative bound (PT17), and the probability mass one then give the last two assertions. It remains to bound the *complete* archimedean term, not a selected part of it.

For \(v\in[a-2r,a+2r]\subset[L,19/25]\), the exact summands in (PT34) satisfy
\[
\begin{gathered}
0<v<1,\quad c_n=2n(2n+1)\le6n^2,\quad
\lambda_n=2n+\tfrac12\le\tfrac52n,\quad
e^{-\lambda_nv}\le2^{-\lambda_n}<4^{-n},\quad |d_n|<n+3,\\
\left|-2c_n^2v^2+(c_n^2d_n+16\lambda_nc_n)v
-4\lambda_nc_nd_n-16\lambda_n^2-8c_n\right|
\le36n^5+240n^4+420n^3+148n^2.
\end{gathered}
\tag{PT36}
\]
To check the constant in \(d_n\), harmonic integral bounds give \(0\le\gamma\le1\), and the area bound \(1<\pi<4\) together with (PT3) gives \(0<\log\pi<\log4<3/2\). Thus \(0<2c_0<5/2\). Also \(H_{n-1}\le n-1\) and \(2/(2n+1)\le2/3\), so
\(|d_n|\le H_{n-1}+2/(2n+1)+2c_0<n+13/6<n+3\).
For the last line of (PT36), the six terms are bounded respectively by
\(72n^4\), \(36n^4(n+3)\), \(240n^3\), \(60n^3(n+3)\), \(100n^2\), and \(48n^2\). Adding these gives exactly its polynomial. Thus this estimate includes every sign and constant of the full archimedean series.

Applying \(q\partial_q\) repeatedly to \((1-q)^{-1}\) and setting \(q=1/4\) gives
\[
\sum_{n\ge1}\frac{n^2}{4^n}=\frac{20}{27},\quad
\sum_{n\ge1}\frac{n^3}{4^n}=\frac{44}{27},\quad
\sum_{n\ge1}\frac{n^4}{4^n}=\frac{380}{81},\quad
\sum_{n\ge1}\frac{n^5}{4^n}=\frac{4108}{243}.
\]
These are differentiations of an absolutely convergent geometric series at an interior point, so their use involves no summation prescription. Inserting them in (PT36) yields
\[
\sup_{L\le v\le19/25}|\mathcal W_\alpha(v)|
<\frac{68272}{27},\qquad
\boxed{|\mathcal A(a)|<\frac{17068}{27},\qquad a\in I.}
\tag{PT37}
\]
The second inequality uses the original factor \(1/4\) in (PT33) and the original probability mass \(\int k=1\), without rescaling the test.

Finally \(\sqrt2<5/3\) by squaring, and \(L>2/3\), so
\[
\beta=\frac{L}{\sqrt2}>\frac25,\qquad
\frac{17068}{27}-28120\frac25=-\frac{286628}{27}.
\tag{PT38}
\]
Combining the exact identity (PT9) with the two proved bounds (PT35) and (PT37) therefore proves
\[
\boxed{
\left.\frac{d}{dt}\right|_{0+}K_t(a)
<-\frac{286628}{27}<0,
\qquad
\log2+\frac1{32}\le a\le\frac{583}{800}.}
\tag{PT39}
\]
The upper endpoint is exactly \(19/25-1/32\). RT16 proves that the left side is the actual right derivative of the original complete zero trace. The result is not merely a sign of a channel or of a finite set of zeros. It is a statement about this fixed translated correlation on this interval; it does not assert a sign for all tests, all translation parameters or finite nonzero heat times.

## 8. Full support and source use

Let \(L_{\rm sup}\) denote the original finite bounded distributive support lattice. The full endpoint coefficients of \(h(\cdot+a)\) vanish by PW5, and the fixed endpoint representations have zero time derivative. Thus CH27 and RT16 give
\[
\dot{\boldsymbol B}_{L_{\rm sup}}=0,\qquad
\dot{\boldsymbol Z}_{L_{\rm sup}}
=(\mathcal A(a)+\mathcal C_2(a))\mathbf e_{1_{L_{\rm sup}}},\qquad
\dot{\boldsymbol D}_{L_{\rm sup}}
=-(\mathcal A(a)+\mathcal C_2(a))\mathbf e_{1_{L_{\rm sup}}}.
\tag{PT40}
\]
The pure prime-two term in (PT7) has zero amplitude but retains its selected top support; it is \(e\), not \(\tau\), under the lifted test map of CH29–30. The numerical ordered-prime-product sum has no nonzero-amplitude contribution on this interval. Its sparse lift has no ordered selected indices there, while the raw lift still records the zero-amplitude pairs \((1,2)\) and \((2,1)\) at index 2, because the raw index-one value is \(e\). Their amplitudes are zero and their retained labels are top. The scalar trace does not identify these two support presentations. The surviving mixed coefficient and the actual negative total derivative are nonzero and top-labelled. All original coordinate spaces, their full coefficient injections, and their label retractions remain those of CH27–30; the evaluation of an endpoint amplitude as zero is not a new quotient of those objects.

Actual reading for this derivation:

- `CAUSAL_HEAT_ARITHMETIC_DISTRIBUTION.md`, CH1–30, written and checked in this independent task. CH4, CH7–14, CH22–25, and CH27–30 are the exact distribution and support dependencies.
- `REAL_TIME_HEAT_TRACE_DERIVATION.md`, RT1–18 read with their proofs; source SHA256 `aa783421f559bba4ba123bbffba18e2c0336bcbcccd2aec865892df6f50983ae`. RT16 supplies the actual right derivative. Its de Bruijn strip input and the cited original Rodgers–Tao and Dobner author TeX remain the human-source dependencies of that proof; this bounded task does not claim a fresh reading of those author archives.
- `PRIMITIVE_PRIME_WINDOW_DERIVATION.md`, PW1–22 was independently reviewed in full; source SHA256 `e8da53af85b0e68deca03115796fccaa1a94871e3e62970fa7e1ff2fd3fe837b`. PW16 supplies \(W\), with its independent coefficient check retained in `PRIME_WINDOW_REVIEW.md`.
- Incoming manuscript *Direct RH continuation: the optimal packet cost in the full Weil form*, SHA256 `d3b1ac08c71f6104cfe011ba5e5b86f6fbe182916c0b0270511671b1f7165d5b`: read the original definitions N1–7, the N10–11 remainder statement, and the N50–52 argument with adjacent text. The circle estimate preceding N52 is the method used and fully reproved in PT14–17. Its symbol \(r\) is this note's \(r_0\), not the fixed radius \(1/64\). No claim of a complete reading of that incoming work is made.

This source is a new derivation kept separate from the sealed publication target. Its complete dependencies should accompany publication with their actual verified proof links. PT39 proves the actual total-derivative sign only in the stated domain; it gives no RH conclusion by itself.


## Exact objects and proved bounds

![The original prime atom ends at log 2 plus 1/32, but its mixed heat channel remains. The enlarged interval retains the same original translation coordinates. The two displayed integral bounds include the complete archimedean convolution and the entire mixed prime-2 term; their sum proves the actual negative right derivative. The figure records rigorous inequalities, not sampled zero motion. Proofs PT7–40; actual heat differentiability RT12–16, with the original Rodgers–Tao and de Bruijn–Dobner inputs cited there.](prime_two_heat_tail.png)
