# Original zeta: heat, signed divisor, contact, and retained arithmetic factors

This calculation starts with the original meromorphic zeta function. It reconstructs the heat and contact receivers formerly presented through AG, GC, CH, and RT. Every completion factor and fixed divisor entry remains explicit. An auxiliary entire product is used for growth estimates with its return map proved; it does not replace the original zeta function. No Euler product at nonzero heat time and no positivity theorem are asserted.

## 1. Original meromorphic family and differential equation

Keep the source's exact time and spatial coordinates:
\[
\begin{aligned}
\zeta_t(s)&=\frac{8}{C(s)}
\int_0^\infty e^{tu^2}\Phi(u)\cosh((2s-1)u)\,du,\quad \zeta_0=\zeta,\\
C(s)&=\frac{s(s-1)}2\pi^{-s/2}\Gamma(s/2),\\
\Phi(u)&=\sum_{n\ge1}
(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})e^{-\pi n^2e^{4u}},\\
q(s)&=\frac{C'(s)}{C(s)}
=\frac1s+\frac1{s-1}-\frac{\log\pi}2+\frac12\psi(s/2).
\end{aligned}\tag{OZH1}
\]
The time-zero equality is Rodgers–Tao's equations hoz, sas, phidef, and htdef, with their factor \(1/8\) retained. This is a meromorphic quotient; \(C\) is not a holomorphic unit everywhere. Write \(E_t=C\zeta_t\) only for the auxiliary entire numerator product.

The integral and all its derivatives converge locally uniformly in complex \(t,s\). Indeed \(|\Phi(u)|\le K e^{9u-ce^{4u}}\): split \(\pi n^2e^{4u}\) into equal parts, bound one below by \((\pi/2)e^{4u}\), and sum the other against \(n^4\). The factors \(e^{Tu^2+K_1u}\) contributed by compact time and spatial sets, and all polynomial factors from differentiation, are dominated by the retained superexponential decay. Twice differentiating in \(s\) multiplies the integrand by \(4u^2\). Expanding the product derivative therefore proves the meromorphic identity
\[
\boxed{4\partial_t\zeta_t
=\zeta_t''+2q\zeta_t'+(q'+q^2)\zeta_t.}
\tag{OZH2}
\]
For \(l_t=\zeta_t'/\zeta_t\), continued meromorphically,
\[
\boxed{4\partial_t l_t
=l_t''+2l_tl_t'+2q l_t'+2q'l_t+q''+2qq'.}
\tag{OZH3}
\]
On a simply connected zero-free neighborhood first divide (OZH2) by \(\zeta_t\), obtaining
\(4\partial_t\log\zeta_t=l_t'+l_t^2+2ql_t+q'+q^2\);
then differentiate in \(s\). Meromorphic continuation proves the result without a global logarithm. Although \(q\) is time independent, its terms in (OZH3) do not vanish.

Repeated differentiation of the original integral and the Leibniz rule give
\[
\partial_t^n\zeta_t(s)=
\frac1{4^n}\sum_{j=0}^{2n}\binom{2n}{j}
\frac{C^{(j)}(s)}{C(s)}\zeta_t^{(2n-j)}(s).
\tag{OZH4}
\]
This is \(4^{-n}C^{-1}\partial_s^{2n}(C\zeta_t)\) expanded with every factor retained. It is an equality of meromorphic functions at exceptional points as well.

## 2. Fixed zeros, pole, and local units

The complete multiplier divisor and its local constants are
\[
\begin{aligned}
\operatorname{div}C&=[1]-\sum_{m\ge1}[-2m],\\
C(-2m+h)&=h^{-1}b_m(h),&
b_m(0)&=\frac{(-1)^m2m(2m+1)\pi^m}{m!},\\
C(1+h)&=h\,c(h),&c(0)&=\frac12,\qquad C(0)=-1 .
\end{aligned}\tag{OZH5}
\]
Gamma has residue \((-1)^m/m!\) at \(-m\); the argument \(s/2=-m+h/2\) supplies the factor 2. Multiplying all the other factors in (OZH1) gives the stated residue. The pole at zero cancels the explicit factor \(s\), giving \(-1\). Gamma has no zeros, so these are all divisor points.

For real \(t,s\), \(E_t(s)>0\). Every summand of \(\Phi(u)\) is positive for \(u\ge0\), since \(2\pi n^2e^{4u}-3>0\), and the cosine-hyperbolic factor is positive. Consequently
\[
\begin{aligned}
\zeta_t(-2m+h)&=h\,v_{m,t}(h),&
v_{m,t}(h)&=E_t(-2m+h)/b_m(h),\\
\zeta_t(1+h)&=h^{-1}v_{1,t}(h),&
v_{1,t}(h)&=E_t(1+h)/c(h),\\
\zeta_t(0)&=-E_t(0)\ne0 .
\end{aligned}\tag{OZH6}
\]
The displayed units are nonzero at zero at every real time. Thus all negative even zeros and the pole at 1 are simple and stationary. The scalar meromorphic function has no zero or pole at the origin. The supported prime \(e\) remains in the programme's support carrier; this scalar statement does not remove it.

The complete jet maps are explicit. If \(E_t(s_0+h)=\sum e_j(t)h^j\) and \(b(h)^{-1}=\sum d_jh^j\), then
\[
[h^n]v_t(h)=\sum_{j=0}^n d_j e_{n-j}(t).
\tag{OZH7}
\]
Multiplication by the nonvanishing unit \(b\) is the inverse; at the pole use \(c\). The original embedded fibers are \(h\mathcal O/h^2\mathcal O\) at a negative even zero and \(h^{-1}\mathcal O/\mathcal O\) at the pole, not their images in the ordinary fiber of \(\mathcal O\).

At a fixed divisor point set \(k=1\) for a zero and \(k=-1\) for the pole. With the appropriate multiplier unit \(b\),
\[
l_t=k/h+v_t'/v_t,\qquad
q=-k/h+b'/b,\qquad
l_t+q=v_t'/v_t+b'/b.
\tag{OZH8}
\]
The last expression is holomorphic. The right side of (OZH3) is therefore holomorphic there, being the spatial derivative of
\(\{(l_t+q)'+(l_t+q)^2\}\).
Equivalently \(\partial_t l_t=\partial_s(\partial_t v_t/v_t)\).
This proves that every fixed divisor residue has derivative zero, while retaining its unit and all unit derivatives. It proves the cancellations of the apparent singularities rather than discarding the individual singular terms.

## 3. Complete signed-divisor traces for rational tests

Let \(A\) be rational and \(A(s)=O(s^{-2})\) at infinity. Its poles must avoid the divisor of \(C\), and the zeros and poles of \(\zeta_{t_*}\), at a fixed real time \(t_*\). Let \(\mathcal Z_t\) be the zeros of \(\zeta_t\) away from the fixed negative even zeros, with multiplicities \(m_{\rho,t}\). For real time these are exactly the zeros of \(E_t=C\zeta_t\). The full signed trace is
\[
\mathcal T_t^\zeta(A)=
\sum_{\rho\in\mathcal Z_t}m_{\rho,t}A(\rho)
+\sum_{m\ge1}A(-2m)-A(1).
\tag{OZH9}
\]
Both sums converge absolutely. Substitution \(x=e^{4u}\) in the estimate of section 1 gives
\(\log\max_{|s|\le R}|E_t(s)|=O_T((R+1)\log(R+2))\).
Since \(E_{t_*}(0)>0\), its value remains bounded away from zero on a small complex time disc. Jensen's formula gives
\(N_t(R)=O(R\log(R+2))\) uniformly there, and dyadic summation gives
\(\sum_{|\rho|>R}m_{\rho,t}/|\rho|^2=O(\log(R+2)/R)\).
The fixed sum is dominated by \(\sum m^{-2}\).

The digamma series, with its zero pole explicitly cancelled against the \(1/s\) already present in (OZH1), gives
\[
q(s)=\frac1{s-1}-\frac{\gamma+\log\pi}{2}
+\sum_{m\ge1}\left(\frac1{2m}-\frac1{s+2m}\right).
\tag{OZH10}
\]
This equality does not replace the original factor formula (OZH1). Its paired summand is \(s/(2m(s+2m))\), proving normal convergence off the poles. Hadamard factorization applied to the auxiliary product, with the growth just verified, gives the original-zeta identity
\[
l_t(s)=\beta_t+
\sum_{\rho\in\mathcal Z_t}m_{\rho,t}
\left(\frac1{s-\rho}+\frac1\rho\right)-q(s),\quad
\beta_t=l_t(0)+q(0),\quad
q(0)=-1-\frac{\gamma+\log\pi}{2}.
\tag{OZH11}
\]
The two series explicitly retain the trivial zeros and pole. Their normal convergence follows from the square-denominator bounds.

For the finite test-pole set \(\mathcal P(A)\),
\[
\boxed{\mathcal T_t^\zeta(A)=
-\sum_{p\in\mathcal P(A)}\operatorname{Res}_{s=p}(A(s)l_t(s)).}
\tag{OZH12}
\]
Indeed a constant times \(A\) has total finite residue zero, since \(A=O(s^{-2})\). Each moving-zero paired term in (OZH11) contributes \(A(\rho)\), by the residue theorem for \(A(s)/(s-\rho)\). Each negative even term in \(-q\) contributes \(A(-2m)\), and its pole term contributes \(-A(1)\). Normal convergence on circles around the finite test poles permits termwise residues. All correction constants remain until their residue is proved zero.

The finite residue expression is holomorphic on a small complex time disc avoiding zeros at the test poles and gives the analytic continuation of the real-time full trace. At any complex-time collision with a fixed divisor point the signed orders add; the meromorphic identity still gives their sum. Differentiating the finite expression proves
\[
\boxed{
\partial_t\mathcal T_t^\zeta(A)=
-\frac14\sum_{p\in\mathcal P(A)}\operatorname{Res}_{p}
A\{l_t''+2l_tl_t'+2q l_t'+2q'l_t+q''+2qq'\}.}
\tag{OZH13}
\]
The complete fixed sum and pole entry in (OZH9) are independent of time, so their derivative is zero. No interchange with an unrestricted differentiated moving-zero sum is used.

For \(A_{z,w}(s)=-[(s-(1-\bar z))(s-w)]^{-1}\), whose distinct poles satisfy the exclusions, direct residue evaluation gives
\[
\mathcal T_t^\zeta(A_{z,w})=
\frac{l_t(w)-l_t(1-\bar z)}{w+\bar z-1}.
\tag{OZH14}
\]
Its difference from the moving-zero receiver is exactly
\(\sum_m A_{z,w}(-2m)-A_{z,w}(1)\). The actual reflection is
\[
l_t(1-s)=-l_t(s)-q(s)-q(1-s),\qquad
\partial_t l_t(1-s)=-\partial_t l_t(s).
\tag{OZH15}
\]
Differentiate \(C(1-s)\zeta_t(1-s)=C(s)\zeta_t(s)\), which follows from the integral's reflection. Thus the original reflected rational kernel retains both multiplier terms.

## 4. Compact tests and an exact trivial-zero convergence boundary

Use the original transform
\[
A(s)=M_h(s)=\int_{\mathbb R}h(v)e^{-(s-1/2)v}\,dv,
\qquad h\in C_c^\infty(\mathbb R).
\tag{OZH16}
\]
Integration by parts gives rapid vertical decay on every fixed closed strip. It does not give decay on the negative real axis: a nonzero nonnegative \(h\) supported in \([d,2d]\), \(d>0\), has
\(A(-2m)\ge e^{(2m+1/2)d}\int h\). Its trivial-zero sum diverges. Thus (OZH9) is not a scalar functional on all compact Mellin tests.

The complete object on that larger domain is the indexed divisor record
\[
\mathcal D_t(A)=
\left((m_{\rho,t}A(\rho))_{\rho\in\mathcal Z_t},
(A(-2m))_{m\ge1},-A(1)\right).
\tag{OZH17}
\]
For \(t\ge0\) its first component is absolutely summable. The de Bruijn strip theorem in RT2, with its exact original time, applies to the real even kernel with the superexponential bound already proved. The known time-zero strip, under the source coordinate \(Z=-2i(s-1/2)\), gives
\(|\Re\rho_t-\frac12|\le\frac12\sqrt{\max(1-2t,0)}\le\frac12\).
The zero count and the compact-test strip decay prove absolute summability, uniformly on compact positive-time intervals. No common strip is asserted for negative or complex time.

Each finite fixed-divisor cutoff is an actual receiving map:
\[
\begin{aligned}
\mathcal T_{t,N}^\zeta(A)&=
\sum_{\rho\in\mathcal Z_t}m_{\rho,t}A(\rho)
+\sum_{m=1}^N A(-2m)-A(1),\\
\mathcal T_{t,N}^\zeta(A)-\sum_{m=1}^N A(-2m)+A(1)
&=\sum_{\rho\in\mathcal Z_t}m_{\rho,t}A(\rho).
\end{aligned}\tag{OZH18}
\]
The right side is independent of \(N\). This proves the relative-trace map from the complete record, with its full compensation exhibited. It does not assert convergence of the uncompensated first line.

For the fixed primitive test retain exactly
\[
\begin{aligned}
r&=1/64,\quad b_r=*_{j\ge1}
\frac{\mathbf1_{[-r2^{-j},r2^{-j}]}}{2r2^{-j}},\quad
G_r(z)=\int b_r(v)e^{-zv}\,dv,\\
F(s)&=s(s-1)G_r(s-1/2),\quad H(s)=F(s)^2,\quad
A_a(s)=e^{a(s-1/2)}H(s).
\end{aligned}\tag{OZH19}
\]
UP1–UP10 proves \(b_r\ge0\), smoothness, evenness, mass 1, and support in \([-r,r]\). Its dyadic construction also proves positive mass in \([r',r]\) for every \(r'<r\). To see this, the uniformly convergent sum of independent uniform variables with these radii exists because their absolute radii sum to \(r\). Its characteristic function is the defining Fourier product, so its law is \(b_r(v)\,dv\). Choose finitely many summands so the remaining tail radius is less than \((r-r')/4\), and restrict each chosen summand to a sufficiently short interval next to its upper endpoint. This event has positive product probability, and every permitted tail gives a sum greater than \(r'\). This proves the endpoint mass assertion for the exact density.

There is an exact convergence boundary:
\[
\boxed{\sum_{m\ge1}A_a(-2m)<\infty
\quad\Longleftrightarrow\quad a\ge2r=\frac1{32}
\qquad(a\in\mathbb R).}
\tag{OZH20}
\]
All these summands are positive. Put \(R=2m+\frac12\). Flatness at the endpoints permits repeated integration by parts:
\[
|G_r(R)|\le\|b_r^{(N)}\|_{L^1}R^{-N}e^{rR}.
\tag{OZH21}
\]
Since \(G_r\) is even,
\(A_a(-2m)=(2m)^2(2m+1)^2e^{-aR}G_r(R)^2\).
For \(a\ge2r\) the bound is a constant times \(m^{4-2N}\), summable for \(N\ge3\). This includes equality. For \(a<2r\), choose \(r'<r\) with \(2r'>a\). Evenness and positive endpoint mass give \(G_r(R)\ge c_{r'}e^{r'R}\). The summands then grow at least as a positive polynomial times \(e^{(2r'-a)R}\), so do not tend to zero. This proves both directions.

Thus at \(a=0\) the earlier \(K_t(a)\) is the relative trace in (OZH18), not an absolutely convergent complete-divisor scalar trace. For \(t\ge0\) and \(a\ge1/32\) its exact relation is
\[
\mathcal T_t^\zeta(A_a)=K_t(a)+U(a),\qquad
U(a)=\sum_{m\ge1}(2m)^2(2m+1)^2
e^{-a(2m+1/2)}G_r(2m+1/2)^2>0.
\tag{OZH22}
\]
The pole entry is the evaluated zero \(-A_a(1)=0\), because of the retained test factor \(s(s-1)\). Every \(a\) derivative of \(U\) converges at and beyond the boundary by (OZH21), after increasing \(N\). This is an exact comparison function, not a transfer of a positivity theorem.

## 5. Actual compact-test variation in original coordinates

Choose \(1<\sigma<3\), so \(1-\sigma\) lies left of the moving strip and right of the first trivial zero. The original logarithmic derivative yields
\[
\begin{aligned}
Z_t(A)-A(1)=\frac1{2\pi i}\int_{\Re s=\sigma}
\bigl[&
\{A(s)+A(1-s)\}l_t(s)\\
&+A(1-s)\{q(s)+q(1-s)\}\bigr]\,ds,\quad t\ge0 .
\end{aligned}\tag{OZH23}
\]
Here \(Z_t\) denotes only the first-component sum in (OZH18). A rectangle between the two lines contains the pole at 1, of residue \(-A(1)\), and no trivial zeros. On the left edge the downward orientation and \(s\mapsto1-s\) give \(-A(1-s)l_t(1-s)\); (OZH15) gives precisely the displayed integrand.

The convergence and exhaustion can be checked directly with (OZH10)–(OZH11). On the two lines split their zero sums at \(|\rho|=2(|s|+1)\). The near part has multiplicity \(O(R\log R)\) and fixed horizontal distance from the line; the tail retains \(s/[\rho(s-\rho)]\). Their spatial derivatives have similar bounds. This gives \(O((1+|\Im s|)^2)\) for each fixed derivative of \(l_t+q\), uniformly on compact positive-time intervals. The paired series (OZH10) gives a polynomial bound for each derivative of \(q\) on both lines, avoiding its poles. Each separate term is therefore integrable against the arbitrarily rapid strip decay of \(A\).

At height \(j\), choose \(Y_j\in[j,j+1]\) at distance at least \(j^{-3}\) from adjacent absolute zero ordinates. The excluded length is \(O(j^{-2}\log j)<1\). The near sums on the horizontal edges then have polynomial growth, and the paired tails have the previous bounds. The rapid decay of \(A\) forces the horizontal integrals to zero. This proves (OZH23) from the residue theorem, with the pole contribution retained.

Equation (OZH3) and induction give polynomial bounds for every fixed time derivative on the lines. Dominated integration and the fundamental theorem of calculus in real time prove that every finite cutoff trace is \(C^\infty\) for \(t\ge0\), with right derivatives at zero. In particular
\[
\boxed{
\left.\partial_t\mathcal T_{t,N}^\zeta(A)\right|_{0+}
=\frac1{2\pi i}\int_{\Re s=\sigma}
\{A(s)+A(1-s)\}
\frac{l_0''+2l_0l_0'+2q l_0'+2q'l_0+q''+2qq'}4\,ds.}
\tag{OZH24}
\]
The finite fixed-divisor entries have zero derivative, so this value is independent of \(N\). If the full fixed sum converges, its derivative is the same because its full added value is time independent.

All higher recurrences can likewise retain the two separate types of jets. In a polynomial algebra use formal \(l_j,q_j\), let \(Dl_j=l_{j+1}\), \(Dq_j=q_{j+1}\), and set
\[
\mathcal B=\tfrac14(l_2+2l_0l_1+2q_0l_1+2q_1l_0+q_2+2q_0q_1),
\qquad Vl_j=D^j\mathcal B,\quad Vq_j=0.
\tag{OZH25}
\]
The chain rule proves \(\partial_t^k l_t=V^k l_0\) after evaluating the spatial jets. For \(k\ge1\) this replaces the quotient in (OZH24). For \(k=0\), the additional multiplier-reflection and pole terms remain exactly as in (OZH23). No zeroth-order boundary term is inherited as zero.

## 6. Contact in original-zeta units

At a moving zero \(\rho\) of multiplicity \(m\), write
\[
\zeta(s)=(s-\rho)^m v_\rho(s),\qquad
d_\rho=v_\rho'(\rho)/v_\rho(\rho),\qquad
q_\rho=\frac1\rho+\frac1{\rho-1}-\frac{\log\pi}2+
\frac12\psi(\rho/2).
\tag{OZH26}
\]
Both \(C\) and \(v_\rho\) are holomorphic nonzero units near \(\rho\). Expanding every term of (OZH2) divided by \(\zeta\) gives the principal part
\[
\operatorname{PP}_\rho
\left(\frac{\zeta''}{\zeta}+2q\frac{\zeta'}{\zeta}+q'+q^2\right)
=\frac{m(m-1)}{(s-\rho)^2}
+\frac{2m(d_\rho+q_\rho)}{s-\rho}.
\tag{OZH27}
\]
The term \(2q\zeta'/\zeta\) supplies \(2mq_\rho/(s-\rho)\); \(q'+q^2\) is holomorphic here, not discarded elsewhere.

For \(A\) holomorphic in an isolating disc,
\[
\boxed{
\left.\partial_t\right|_0\frac1{2\pi i}
\int_{\partial D_\rho}A(s)l_t(s)\,ds
=-\frac{m(m-1)}4A''(\rho)
-\frac m2(d_\rho+q_\rho)A'(\rho).}
\tag{OZH28}
\]
Compact nonvanishing on the contour permits time differentiation. Differentiate (OZH27) in \(s\), multiply by the Taylor expansion of \(A\), and take the residue. This proves the cluster formula without choosing differentiable labels for splitting multiple roots. At a simple zero it yields
\[
\rho'(0)=-\frac{\zeta''(\rho)}{4\zeta'(\rho)}-\frac{q_\rho}{2}
=-\frac{d_\rho+q_\rho}{2}.
\tag{OZH29}
\]
Thus the Gamma and endpoint contribution is part of the actual velocity.

For the fixed primitive tests, the contact sum is
\[
\mathcal C(a)=\frac14\sum_\rho m_\rho(m_\rho-1)A_a''(\rho).
\tag{OZH30}
\]
It converges absolutely with all real \(a\) derivatives, locally uniformly in \(a\). The squared multiplicity in a radius-\(R\) annulus is \(O(R^2\log^2R)\), bounded by the square of its total multiplicity. Each test derivative decreases faster than any power on the zero strip; \(a\) derivatives introduce only powers of \(s-\frac12\). These estimates prove the assertions by dyadic summation. The fixed simple trivial zeros and pole have zero variation by (OZH8), not a fictitious moving contact term.

The exact globally grouped expression, for compact Mellin tests, retains the unit interactions. Put
\[
\beta=l_0(0)-1-\frac{\gamma+\log\pi}{2},\qquad
T_A(\rho,\eta)=
\frac{A'(\rho)-A'(\eta)}{\rho-\eta}
+\frac{A'(\rho)}{\eta}+\frac{A'(\eta)}{\rho}.
\tag{OZH31}
\]
For the actual right derivative \(\mathcal V(A)\) in (OZH24),
\[
\begin{aligned}
\mathcal V(A)+\frac14\sum_\rho m_\rho(m_\rho-1)A''(\rho)
=-\frac12\bigg[&
\beta\sum_\rho m_\rho A'(\rho)
+\sum_\rho\frac{m_\rho^2A'(\rho)}{\rho}\\
&+\sum_{\{\rho,\eta\}}m_\rho m_\eta T_A(\rho,\eta)\bigg].
\end{aligned}\tag{OZH32}
\]
The last sum is over unordered distinct moving supports. Taking the regular part of (OZH11), with \(q\) retained, proves
\[
d_\rho+q_\rho=\beta+\frac{m_\rho}{\rho}
+\sum_{\eta\ne\rho}m_\eta
\left(\frac1{\rho-\eta}+\frac1\eta\right).
\tag{OZH33}
\]
Its tail is \(O_\rho(m_\eta/|\eta|^2)\). Insert this in (OZH28), summed over a finite separated contour. The pairs inside combine into (OZH31).

For completeness all limits here are controlled. For comparable large moduli, use \(A''\) integrated along the joining segment when the two supports are close, and rapid endpoint estimates when far. The resulting divided differences have arbitrarily rapid decay; the pair multiplicity weight is \(O(R^2\log^2R)\). For \(|\eta|\ge2|\rho|\), the exact rearrangement
\[
T_A(\rho,\eta)=
\frac{\rho A'(\rho)}{\eta(\rho-\eta)}
+\frac{\eta A'(\eta)}{\rho(\eta-\rho)}
\tag{OZH34}
\]
is bounded by \(2|\rho||A'(\rho)|/|\eta|^2+
2|A'(\eta)|/|\rho|\). The zero count gives the square tail
\(O(\log R/R)\) and \(\sum_{|\rho|\le R}m_\rho/|\rho|=O(\log^2(R+2))\),
proving absolute convergence. Across the separated contour at height \(T\), the bounded-height cross terms are \(O(\log T/T)\); those of moduli comparable to \(T\) are \(O_N(T^{5-N}\log^2T)\), using the distance \(T^{-3}\); the further tail is \(O_N(T^{1-N}\log^2T)\). These tend to zero. This proves (OZH32) with its grouped sums and the derivative already proved in (OZH24). It does not assume convergence of the ungrouped velocity series. Rational tests instead have their full derivative defined and proved by (OZH13), without needing this compact-test exhaustion.

Let \(c_\rho=\rho-\frac12\). For the fixed \(H=F^2\), the Laplace transform in \(a\), first for \(\Re w>\frac12\), has the exact residual principal part
\[
\boxed{
\operatorname{PP}_{w=c_\rho}\widehat{\mathcal V+\mathcal C}(w)
=-\frac{m_\rho}{2}
\left(d_\rho+\frac1\rho+\frac1{\rho-1}
-\frac{\log\pi}{2}+\frac12\psi(\rho/2)\right)
\left(\frac{F(\rho)^2}{(w-c_\rho)^2}
+\frac{2F(\rho)F'(\rho)}{w-c_\rho}\right).}
\tag{OZH35}
\]
To prove it, the Laplace transform of \(A_a(s)\) is
\(H(s)/(w-(s-\frac12))\) on the zero strip. The preceding estimates have integrable majorant \((1+a^2)e^{-(\Re w-1/2)a}\), so transformation through every grouped sum is justified. Their tails converge normally on compact \(w\)-sets avoiding the discrete \(c_\rho\), by the same divided-difference bounds and high-height denominator bounds. Isolating the pairs containing \(\rho\) and using (OZH33) gives (OZH35). The contact contribution removed has principal part
\[
\frac{m_\rho(m_\rho-1)}4
\left(\frac{2H(\rho)}{(w-c_\rho)^3}
+\frac{2H'(\rho)}{(w-c_\rho)^2}
+\frac{H''(\rho)}{w-c_\rho}\right).
\tag{OZH35a}
\]
This computes all of it, not only its triple pole.

The higher-order original-zeta formula is also exact. At a simple zero define
\[
n_\rho=\min\left\{n\ge1:
\sum_{j=0}^{2n}\binom{2n}{j}
C^{(j)}(\rho)\zeta^{(2n-j)}(\rho)\ne0\right\}.
\tag{OZH36}
\]
This minimum is finite: substitution \(x=\sqrt T\,u\) in the original integral proves
\(\sqrt T\,\zeta_{-T}(\rho)\to4\sqrt\pi\,\Phi(0)/C(\rho)\ne0\)
by dominated convergence, with bound a constant times
\(e^{-x^2+|2\rho-1|x}\). Thus its time-entire value is not identically zero. Formula (OZH4) identifies its Taylor coefficients. Analytic division at the simple zero then gives
\[
\rho(t)=\rho-
\frac{\sum_{j=0}^{2n_\rho}\binom{2n_\rho}{j}
C^{(j)}(\rho)\zeta^{(2n_\rho-j)}(\rho)}
{4^{n_\rho}n_\rho!\,C(\rho)\zeta'(\rho)}
t^{n_\rho}+O(t^{n_\rho+1}).
\tag{OZH37}
\]
The local resolvent's first nonzero time derivative has the same coefficient without \(n_\rho!\), multiplying
\(\{F(\rho)^2/(w-c_\rho)^2+2F(\rho)F'(\rho)/(w-c_\rho)\}\).
All multiplier derivatives remain in that numerator.

## 7. Original Euler derivative and full causal arithmetic

At time zero on \(\Re s>1\), the original Euler product gives
\[
l_0(s)=-P(s),\qquad P(s)=\sum_{n\ge2}\Lambda(n)n^{-s}.
\tag{OZH38}
\]
Local uniform convergence and differentiation follow from comparison with
\(\sum(\log n)n^{-\sigma}\), retaining a smaller positive convergence margin for derivatives. Equation (OZH3) becomes
\[
4\partial_t l_t|_0=-P''+2PP'-2qP'-2q'P+q''+2qq'.
\tag{OZH39}
\]
Every term is calculated from the original \(\zeta'/\zeta\), including both cross terms and both pure multiplier terms.

For compact smooth \(\varphi\) define
\[
\begin{aligned}
\pi_{\rm ar}&=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\delta_{\log n},\\
\langle\alpha,\varphi\rangle
&=\int_0^\infty(e^{-v/2}+e^{v/2})\varphi(v)\,dv
-\frac{\gamma+\log\pi}{2}\varphi(0)\\
&\quad+\int_0^\infty
\frac{e^{-2v}\varphi(0)-e^{-v/2}\varphi(v)}
{1-e^{-2v}}\,dv .
\end{aligned}\tag{OZH40}
\]
The last numerator near zero is
\(v(-3\varphi(0)/2-\varphi'(0))+O(v^2)\), so the quotient is bounded. Beyond the compact support the remaining term is integrable. This is a causal distribution of order at most one. On \(\Re s>1\), substitution of the exponential test and \(x=2v\) in the last integral gives
\[
M_{\pi_{\rm ar}}=P,\qquad
M_\alpha=\frac1s+\frac1{s-1}-\frac{\log\pi}{2}
+\frac12\psi(s/2)=q.
\tag{OZH41}
\]
Here the convergent digamma integral is
\(\int_0^\infty(e^{-x}-e^{-zx})/(1-e^{-x})\,dx=\psi(z)+\gamma\).
It proves all endpoint, Gamma, and constant contributions separately.

To define singular convolutions, retain the measures
\[
G=-\tfrac12e^{-v/2}\log(1-e^{-2v})\mathbf1_{v>0}\,dv,\qquad
m=e^{v/2}\mathbf1_{v>0}\,dv+\tfrac12G
-\tfrac{\gamma+\log\pi}{2}\delta_0 .
\tag{OZH42}
\]
Then \(\alpha=DG+m\) as distributions on the whole real line. Write \(g\) for the density of \(G\); for \(v>0\),
\(g'+g/2=-e^{-5v/2}/(1-e^{-2v})\), and
\(\int_\varepsilon^\infty e^{-2v}/(1-e^{-2v})\,dv
=e^{\varepsilon/2}g(\varepsilon)\).
After integration by parts the difference of the two cutoff boundary expressions is
\(g(\varepsilon)(e^{\varepsilon/2}\varphi(0)-\varphi(\varepsilon))
=O(\varepsilon|\log\varepsilon|)\to0\). This proves the distribution equality without a hidden boundary atom.

For every \(c>1/2\), \(G,m,\pi_{\rm ar}\) have finite exponentially weighted total variation and every polynomial moment with that weight. Near zero \(g=O(1+|\log v|)\); at infinity \(g=O(e^{-5v/2})\); the prime contribution is bounded by
\(\sum(\log n)n^{-c-1/2}\). Polynomial moments follow by retaining a smaller positive exponential margin. Causal convolution of these measures is locally finite because addition is proper on the causal quadrant over compact sets; its weighted norm is at most the product of the norms. Define distribution convolutions by derivatives of these measure convolutions, for instance
\(\alpha*\alpha=D^2(G*G)+2D(G*m)+m*m\).
Weighted Fubini proves transform multiplication, and multiplication by \(v\) transforms to \(-\partial_s\).

It follows that the full causal receiver of (OZH39) is
\[
\boxed{
4\mathfrak J_\zeta=
-v^2\pi_{\rm ar}-v(\pi_{\rm ar}*\pi_{\rm ar})
+2v(\alpha*\pi_{\rm ar})
+v^2\alpha-v(\alpha*\alpha).}
\tag{OZH43}
\]
This proves its definition and every coefficient. The fixed multiplier contributes both its pure terms and its interaction with the prime measure.

Fourier inversion in the original convention gives
\[
\left.\partial_t\mathcal T_{t,N}^\zeta(M_h)\right|_{0+}
=\langle\mathfrak J_\zeta,h(v)+h(-v)\rangle .
\tag{OZH44}
\]
For verification, first let the causal distribution be a measure with finite exponential weight \(e^{-(\sigma-\frac12)v}\). Fourier inversion and weighted Fubini pair its transform with \(M_h(s)\) to yield \(h(-v)\), and with \(M_h(1-s)\) to yield \(h(v)\); the exponential weights cancel in each case. For a derivative of a measure use the differentiated compact test and its rapid Fourier decay. Every term of (OZH43) has this derivative-of-measures form by (OZH42), including the polynomial weights. Equation (OZH24) now proves the result for the actual right derivative.

Writing \(F_h(v)=h(v)+h(-v)\), with support in \([-R,R]\), the complete expression is
\[
\begin{aligned}
4\langle\mathfrak J_\zeta,F_h\rangle={}&
\langle v^2\alpha-v(\alpha*\alpha),F_h\rangle\\
&-\sum_{2\le n\le e^R}\frac{\Lambda(n)}{\sqrt n}
(\log n)^2F_h(\log n)\\
&+2\sum_{2\le n\le e^R}\frac{\Lambda(n)}{\sqrt n}
\langle\alpha,(v+\log n)F_h(v+\log n)\rangle\\
&-\sum_{2\le k\le e^R}\frac{(\Lambda*\Lambda)(k)}{\sqrt k}
(\log k)F_h(\log k).
\end{aligned}\tag{OZH45}
\]
The coefficient \((\Lambda*\Lambda)(k)=\sum_{mn=k}\Lambda(m)\Lambda(n)\) retains every ordered factorization. Causality proves the finite cutoffs. This reconstructs the arithmetic variation from the original Euler derivative rather than replacing that derivative by a completed one.

## 8. Full lattice labels and receiving maps

Let \(L\) be the original finite bounded distributive lattice. Its carrier is exactly \(G_L(V)=\{(v,1_L):v\in V\}\cup\{z_\lambda=(0,\lambda):\lambda\ne1_L\}\), on each stated scalar or linear receiving space. Nonzero amplitudes occur only at top support. Keep each divisor entry in (OZH17) with its original index and top support; the lower zero labels remain separate. A zero amplitude at a present top-supported entry is \((0,1_L)=e\); absence is \(\tau=z_{0_L}\). A specified linear residue, contour, differentiation, or finite-cutoff receiver lifts by
\[
(U,1_L)\longmapsto(\mathcal F(U),1_L),\qquad
z_\lambda\longmapsto z_\lambda\quad(\lambda\ne1_L).
\tag{OZH46}
\]
Linearity of the amplitude map and retention of the join label prove additivity; the original scalar action retains its meet rule. The independent complex coefficients \(c_\lambda\) are values of functions on lower carrier points; they belong to the attached function space and are retained by the identity there. They are not nonzero amplitudes in the lower carrier strata. An arbitrary test pairing is not asserted multiplicative. Causal convolution uses meet labels and the original ordered indices, before labels over the same product index are joined. In particular the raw index \(n=1\) retains \(e\), while the sparse index retains \(\tau\). Their amplitude-zero images are different labelled objects.

Retain the original supported identity, on its proved test domain,
\[
\begin{aligned}
\boldsymbol B_L&=(A(0)+A(1))\mathbf e_{1_L}
+A(0)\sum_{\lambda\ne1_L}\mathbf e_\lambda,\\
\boldsymbol Z_L&=Z_0(A)\mathbf e_{1_L},\\
\boldsymbol D_L&=(P_{\rm fin}-A_\infty)\mathbf e_{1_L}
+A(0)\sum_{\lambda\ne1_L}\mathbf e_\lambda,\qquad
\boldsymbol B_L-\boldsymbol Z_L=\boldsymbol D_L.
\end{aligned}\tag{OZH47}
\]
The finite-prime and archimedean functionals have exactly the original SZW definitions. Their separate original-zeta reconstruction is the companion OZC calculation; the map here does not suppress them. Define
\[
\begin{aligned}
U_N(A)&=\sum_{m=1}^N A(-2m),\\
\boldsymbol B_{L,N}^\zeta&=\boldsymbol B_L+
\{U_N(A)-A(1)\}\mathbf e_{1_L},\\
\boldsymbol Z_{L,N}^\zeta&=\mathcal T_{0,N}^\zeta(A)\mathbf e_{1_L},\qquad
\boldsymbol B_{L,N}^\zeta-\boldsymbol Z_{L,N}^\zeta
=\boldsymbol D_L.
\end{aligned}\tag{OZH48}
\]
Substitution of (OZH18) proves the equality. Store the full indexed fixed sequence as well as these finite receiving maps. When it converges, absolute convergence gives the corresponding full-sum map. The \(A(0)\) coordinate and every lower lattice coordinate remain; this states precisely how the supported-zero prime is retained when the scalar zeta divisor has no point at zero.

For fixed tests, in the induced time-dependent identity,
\[
\dot{\boldsymbol B}_{L,N}^\zeta=0,\qquad
\dot{\boldsymbol Z}_{L,N}^\zeta=\mathcal V(A)\mathbf e_{1_L},\qquad
\dot{\boldsymbol D}_{L,N}^\zeta=-\mathcal V(A)\mathbf e_{1_L}.
\tag{OZH49}
\]
All fixed divisor, endpoint, and lower support coordinates have their calculated zero derivative with labels retained. Adding contact changes the last two entries by \(+\mathcal C\,\mathbf e_{1_L}\) and \(-\mathcal C\,\mathbf e_{1_L}\). The original heat equation remains (OZH2); the trace correction does not construct a different persistent-contact heat family.

These calculations retain the previously obtained first-variation numbers on their proved domains, reconstruct their local drift with all original-zeta and multiplier terms, and restore the full fixed divisor record. The additional boundary (OZH20) proves that the old zero-strip correlation at the origin is a relative trace and cannot be called an absolutely convergent complete-divisor sum.

## Sources and actual reading

The original author source is Brad Rodgers and Terence Tao, *The de Bruijn–Newman constant is non-negative*, [arXiv:1801.05914v5 author TeX](https://arxiv.org/src/1801.05914v5). Its file fmp-template.tex, lines 64–153, was read for this calculation, including hoz, sas, phidef, htdef and the heat equation. This is bounded reading, not a claim to have reread the entire paper.

The complete programme proofs read are AG1–AG24, GC1–GC31a, CH1–CH30, and RT1–RT30. Their SHA256 values, in that order, are:

- `00b2bc42ab649558e7af9c8c781bdb4d3b08f43bcfd496fe6f9e6e0fa453a4b0`
- `589c5b42c3bf2ad63c5370f89eb36e7272b28c0408d460f041ccd12060b4e27b`
- `6fed48dd0eb9e4ce335d3b84532d2117bc2349370630912358439003aae35de1`
- `aa783421f559bba4ba123bbffba18e2c0336bcbcccd2aec865892df6f50983ae`

UP0–UP18 was reread for the density and product. The classical bump attribution remains Juan Arias de Reyna, *An infinitely differentiable function with compact support: Definition and properties*, arXiv:1702.05442v1, Theorem 1; its dyadic constants are unchanged. The de Bruijn theorem is used exactly as quoted in RT2: Alexander Dobner, arXiv:2005.05142v2, author file paper.tex, theorem debruijnthm, citing N. G. de Bruijn (1950), Theorem 13. This derivation has not independently reread those latter author sources; section 4 verifies the same hypotheses for the exact kernel.

OZH1–OZH15 reconstruct AG's full rational receiver; OZH16–OZH25 reconstruct RT's compact-test domain and prove the new trivial-zero boundary; OZH26–OZH37 reconstruct GC's contact and local higher-motion receiver; OZH38–OZH45 reconstruct CH from the original Euler derivative; OZH46–OZH49 prove the labelled receiving maps. The companion UZ source supplies the compatible embedded line-module and all-jet multiplier description. These results do not supply the unresolved uniform positivity bound for RH.




## Original-zeta Gaussian and affine receiving maps

The complete extension OZG1–55 proves that Gaussian convolution of the test at every positive time makes the original trivial-zero scalar sum diverge for every real translation. Its admissible replacement retains each cutoff trace and the Gamma boundary with the identical finite sum U_N; OZG20–27 gives both maps and the inverse. The full coefficient tower, its raw non-Hermitian correction and exact compensated negative index are OZG28–39. No compact-support prime window is assumed after smoothing; all prime powers and Gamma terms, with explicit error bounds, are OZG40–52. This extension acts on the tests while fixing the original zeta zeros.

The different affine change of the actual original heat family is OZR1–36. Its multiplier is exp(chi) C(phi)/C, with the full inverse, exceptional units and local jets. The original generator contains every q derivative term. The signed divisor comparison is OZR19–24; its Cauchy logarithmic kernel has an additional growth contribution 2a. OZR33 proves the exact full negative index after that contribution is retained. The full support carrier and every lower coordinate are OZG53–55 and OZR34–36. These are the receiving maps for these specified extensions; the original preceding test, time and domains remain those stated in its proof.
