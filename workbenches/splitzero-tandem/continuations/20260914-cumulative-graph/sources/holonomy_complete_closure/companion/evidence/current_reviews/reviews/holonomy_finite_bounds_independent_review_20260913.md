# Independent calculation of HG16–HG24

Status: accepted. The assigned bounds, finite choices and ordered action identities are valid in the original source metrics. No mathematical correction is required by this review.

The initial assigned file had 20,028 bytes and SHA-256 0a636275807067e19c03b0e55a4a1c10359c7ad20bd912227f7d9f30e5e2b74a. During this review the owner appended HG25 outside this lane and strengthened the spectral-diameter allowance by HG11a. The final source pin is recorded in the companion receipt. This review covers HG16–HG24, the HG11a estimate needed by their final allowance, and their adjoining deductions; HG25 remains with its separate reviewer.

The original supplied Tau_Holonomy_Descent_Control/NOTE.md has 35,088 bytes and SHA-256 900e7c16369a58093b16a03dbc449d41a100ee45dbbe8515e30bc026e660ba393. Its H49a–H55 were read at lines 496–618. In particular line 566 fixes \(0\le\theta<2\pi\), the representative interval used in the frequency estimate. The original admitted source columns have the weighted regularity and finite derivative Grams stated in that source. Their integrals remain actual source integrals; no numerical interval enclosure is claimed here.

No source file was edited, no Lean or mathematical test was run, and no publication was performed. The calculations below retain every source metric, quotient, coefficient, Fourier factor and boundary term.

## Original objects used in the calculation

Keep the original \(k\ge1\), monic \(\chi=\chi_{h,k}\) of degree \(q\ge1\), and
\[
E=\mathbb C[S]/(\chi),\quad A=M_S,\quad e_0=[1],\quad
\ell[P]=[S^{q-1}]\operatorname{rem}_{\chi}P,\quad R=e_0\ell.
\]
All primary multiplicities remain. The fixed source is
\[
\Psi_N:\mathcal P_N\longrightarrow
L^2(\mathbb R,dr;\mathcal K),\qquad
\mathcal K=L^2(\mathbb R^{k-1},dz),\qquad M=\Psi_N^*\Psi_N\succ0,
\]
with \(N\ge q-1\). Keep its original remainder map, canonical section \(C:E\to\mathcal P_N\), original relation embedding \(B_{\rm rel}\), and quotient metric \(G\). Their exact identities from HG4–HG5 are
\[
C^*MC=G,\qquad B_{\rm rel}^*MC=0,\qquad JC=I_E,
\qquad\operatorname{im}B_{\rm rel}=\ker J.
\]
Here \(J:\mathcal P_N\twoheadrightarrow E\) is the remainder map. The separate occurrence \(J\in\mathbb Z_{\ge2}\) in HG18–HG23 is the frequency cutoff. Every minimization below is on the same original remainder fibre, and every frequency sum uses the integer cutoff.

The preceding proved identities HG3–HG7 are
\[
(1-\delta)M\preceq M_\theta\preceq(1+\delta)M,\quad
G=\overline G+\mathscr D,\quad 0\preceq\mathscr D\preceq\delta^2G,
\quad\mathsf D=G^{-1}\mathscr D.
\]
Consequently
\[
(1-\delta^2)G\preceq\overline G\preceq G.
\]
These are explicit preceding constructions in the reviewed source, not new assumptions substituting for missing work. All norms below retain their original Gram, for example \(\|v\|_M^2=v^*Mv\). No vector mass is reset or source metric replaced.

## HG16: correlation and the exact strip bound

Write
\[
M_{a,\pm}=(e^{\pm ar}\Psi_N)^*(e^{\pm ar}\Psi_N)
\preceq\kappa_\pm M,\qquad b_a=\sqrt{\kappa_+\kappa_-}.
\]
For the original vectors \(v,w\) and a translation \(u\ge0\),
\[
\begin{aligned}
|v^*\mathcal C(u)w|
&=e^{-au}\left|\int
\langle e^{-ar}\Psi_Nv(r),
e^{a(r+u)}\Psi_Nw(r+u)\rangle_{\mathcal K}\,dr\right|\\
&\le e^{-au}(v^*M_{a,-}v)^{1/2}
                  (w^*M_{a,+}w)^{1/2}\\
&\le b_a e^{-au}\|v\|_M\|w\|_M.
\end{aligned}
\]
The substitution \(r'=r+u\) gives the exact second weighted Gram. The identity \(\mathcal C(-u)=\mathcal C(u)^*\) reverses the two weighted factors for negative translation, with the same \(b_a\). Taking the defining supremum over both original nonzero vectors proves
\[
\|M^{-1}\mathcal C(nL)\|_M\le b_a e^{-a|n|L}.
\]
For
\[
\widetilde M(z)=M+\sum_{n\ne0}e^{inz}\mathcal C(nL),
\]
every fixed derivative series converges uniformly on a compact substrip \(|\operatorname{Im}z|\le s<aL\): its terms are bounded by a constant times \(|n|^j e^{-(aL-s)|n|}\). Thus the matrix is holomorphic on the open strip \(|\operatorname{Im}z|<aL\). Its full relative norm bound on the chosen closed substrip is
\[
\begin{aligned}
\|M^{-1}(\widetilde M(z)-M)\|_M
&\le b_a\sum_{n\ne0}e^{-(aL-s)|n|}\\
&=\frac{2b_a}{e^{aL-s}-1}=d_s.
\end{aligned}
\]
Both signs of the correlation index are included. For complex \(z\) this is an operator-norm bound, not a Hermitian-order assertion.

## HG17: the literal Schur complement and its inverse domain

Let \(K=B_{\rm rel}^*MB_{\rm rel}\). On a nonzero relation space it is positive because \(M\succ0\) and \(B_{\rm rel}\) is injective. With the original relation metric \(K\), both \(C\) and \(B_{\rm rel}\) are isometries into the \(M\)-metric source. Their adjoints are
\[
C^\dagger=G^{-1}C^*M,\qquad
B_{\rm rel}^\dagger=K^{-1}B_{\rm rel}^*M,\qquad
C^\dagger B_{\rm rel}=0.
\]
Put \(E_z=M^{-1}(\widetilde M(z)-M)\). The exact HG17 expression becomes
\[
\begin{aligned}
G^{-1}\widetilde G(z)
={}&I+C^\dagger E_zC\\
&-C^\dagger E_zB_{\rm rel}
(I+B_{\rm rel}^\dagger E_zB_{\rm rel})^{-1}
B_{\rm rel}^\dagger E_zC.
\end{aligned}
\]
Indeed,
\[
B_{\rm rel}^*\widetilde M(z)B_{\rm rel}
=K(I+B_{\rm rel}^\dagger E_zB_{\rm rel}),
\]
whose inverse is \((I+B_{\rm rel}^\dagger E_zB_{\rm rel})^{-1}K^{-1}\). Since \(\|E_z\|_M\le d_s<1\), its relative inverse is the convergent Neumann series with norm at most \((1-d_s)^{-1}\). The two cross maps have norm at most \(d_s\), while the first line has norm at most \(1+d_s\). Therefore
\[
\|G^{-1}\widetilde G(z)\|_G
\le1+d_s+\frac{d_s^2}{1-d_s}
=\frac1{1-d_s}.
\]
On the real axis, minimizing
\((Cv+B_{\rm rel}x)^*M_\theta(Cv+B_{\rm rel}x)\)
over the original relation coefficient \(x\) gives exactly HG17, so \(\widetilde G(\theta)=G_\theta\). If the relation space is zero, the second line is the zero map; there is no nonzero-dimensional relation inverse to perform, and the bound \(1+d_s\) already suffices.

The inverse is proved on the smaller strip with \(d_s<1\), whereas the correlation matrix itself is holomorphic on \(|\operatorname{Im}z|<aL\). There is no contour-domain gap: continuity of \(d_s\) gives a slightly larger closed substrip still satisfying \(d_s<1\), so the contour at height \(s\) lies inside an open inverse domain. For the explicit HG20 choice one may take \(s'=aL-\log(1+3b_a)>s\), where \(d_{s'}=2/3<1\). Every star in HG17 acts on a fixed coefficient map and does not conjugate \(z\).

## HG16: phase quadrature with its exact constant

Set \(F(z)=G^{-1}\widetilde G(z)\) and
\[
F_n=\frac1{2\pi}\int_0^{2\pi}F(x)e^{-inx}\,dx.
\]
For \(n>0\), the contour \(z=x-is\) gives
\(e^{-in(x-is)}=e^{-inx}e^{-ns}\).
For \(n<0\), \(z=x+is\) gives \(e^{-s|n|}\). The vertical sides cancel by periodicity. Thus
\[
\|F_n\|_G\le(1-d_s)^{-1}e^{-s|n|}.
\]
These coefficients are absolutely summable and their Fourier series equals \(F\). One can verify the equality without an extra regularity assertion using the Fejér kernels
\[
K_Q(x)=\frac1{Q+1}\left|\sum_{r=0}^{Q}e^{irx}\right|^2.
\]
They are nonnegative, have integral one for \(dx/(2\pi)\), and have mass outside each neighborhood of zero tending to zero, since there they are bounded by a constant divided by \(Q+1\). Their convolution tends uniformly to the continuous \(F\). Convolution of the absolutely convergent coefficient series has the same coefficients and tends to that series, proving equality entry by entry.

The exact finite character sum is
\[
\frac1m\sum_{j=0}^{m-1}e^{2\pi i n j/m}
=\begin{cases}1,&m\mid n,\\0,&m\nmid n.\end{cases}
\]
It is valid also for \(m=1\). Hence
\[
\begin{aligned}
G^{-1}(H_m-\overline G)&=\sum_{\ell\ne0}F_{\ell m},\\
\|G^{-1}(H_m-\overline G)\|_G
&\le\frac2{1-d_s}\sum_{\ell=1}^{\infty}e^{-s\ell m}\\
&=\frac2{(1-d_s)(e^{sm}-1)}=\varepsilon.
\end{aligned}
\]
The difference of the two real-phase means is Hermitian, so the corresponding endomorphism is \(G\)-self-adjoint. It follows that
\[
-\varepsilon G\preceq H_m-\overline G\preceq\varepsilon G,
\quad
(1-\delta^2-\varepsilon)G\preceq H_m\preceq(1+\varepsilon)G.
\]

## HG18: Fourier convention and both omitted tails

For the original representative phase \(0\le\theta<2\pi\), retain
\[
e_{n,\theta}(r)=L^{-1/2}e^{-i(2\pi n+\theta)r/L},
\qquad \omega_{n,\theta}=(2\pi n+\theta)/L.
\]
This basis has boundary multiplier \(e^{-i\theta}\). Its coefficient in the original twisted periodization is
\[
\begin{aligned}
&\int_0^L e_{n,\theta}(r)^*
\sum_{a\in\mathbb Z}e^{ia\theta}\psi(r+aL)\,dr\\
&\quad=L^{-1/2}\sum_a\int_{aL}^{(a+1)L}
e^{ia\theta}e^{i\omega_{n,\theta}(u-aL)}\psi(u)\,du\\
&\quad=L^{-1/2}\widehat\psi(\omega_{n,\theta}),
\end{aligned}
\]
because \(e^{ia\theta}e^{-ia(2\pi n+\theta)}=1\), with
\(\widehat\psi(u)=\int\psi(r)e^{iur}dr\).
No phase, Fourier sign, \(L\), or \(2\pi\) factor is omitted.

For \(p\ge1\), write \(f=\Psi_Nv\). The admitted weighted derivative regularity gives vanishing integration-by-parts boundary terms and
\[
\widehat{f^{(p)}}(u)=(-iu)^p\widehat f(u).
\]
For \(u\ne0\), Hilbert-valued weighted Cauchy–Schwarz gives
\[
\begin{aligned}
\|\widehat f(u)\|_{\mathcal K}^2
&\le |u|^{-2p}
\left(\int_{\mathbb R}\frac{dr}{1+r^2}\right)
\left(\int_{\mathbb R}(1+r^2)\|f^{(p)}(r)\|_{\mathcal K}^2dr\right)\\
&=\pi|u|^{-2p}v^*H_{p,N}v.
\end{aligned}
\]
Only omitted nonzero frequencies require this estimate. The original \(n=0,\theta=0\) coefficient stays inside the retained set.

For the integer \(J\ge2\) and \(|n|>J\),
\[
|n+\theta/(2\pi)|\ge|n|-1>0.
\]
Parseval gives, with both tails explicit,
\[
\begin{aligned}
v^*(M_\theta-M_{\theta,J})v
&=\frac1L\sum_{|n|>J}
\|\widehat{\Psi_Nv}(\omega_{n,\theta})\|_{\mathcal K}^2\\
&\le\frac\pi L\left(\frac L{2\pi}\right)^{2p}
\sum_{|n|>J}(|n|-1)^{-2p}\ v^*H_{p,N}v\\
&=\frac{2\pi}L\left(\frac L{2\pi}\right)^{2p}
\sum_{r=J}^{\infty}r^{-2p}\ v^*H_{p,N}v\\
&\le\left(\frac L{2\pi}\right)^{2p-1}
\left(\int_{J-1}^{\infty}x^{-2p}dx\right)v^*H_{p,N}v\\
&=\frac1{2p-1}\left(\frac L{2\pi(J-1)}\right)^{2p-1}
v^*H_{p,N}v.
\end{aligned}
\]
For each integer \(r\ge J\), the decreasing function \(x^{-2p}\) has integral on \([r-1,r]\) at least \(r^{-2p}\), proving the sum-integral comparison. The two tails multiply \(\pi/L\) by exactly two; their combination is the power \(2p-1\) displayed in HG18.

Applying \(H_{p,N}\preceq h_pM\) proves
\[
0\preceq M_\theta-M_{\theta,J}\preceq\epsilon_JM,\qquad
\epsilon_J=\frac{h_p}{2p-1}
\left(\frac L{2\pi(J-1)}\right)^{2p-1}.
\]
The original \(M_\theta\succeq(1-\delta)M\) implies
\[
M_{\theta,J}\succeq
M_\theta-\frac{\epsilon_J}{1-\delta}M_\theta
=(1-\xi_J)M_\theta,\qquad
\xi_J=\epsilon_J/(1-\delta).
\]
If \(\xi_J<1\), this proves positivity directly, without requiring each sampled weight to be positive. Minimize on the identical original remainder fibre. For every representative \(P\) of \(v\),
\(P^*M_{\theta,J}P\ge(1-\xi_J)P^*M_\theta P\);
minimizing gives the lower bound. Evaluating \(M_{\theta,J}\preceq M_\theta\) at the \(M_\theta\)-minimizer gives the upper bound. Thus
\[
(1-\xi_J)G_\theta\preceq G_{\theta,J}\preceq G_\theta.
\]
All domains, representatives and the quotient map are retained.

## HG19–HG20: explicit positive finite constants

Averaging the preceding bounds on the specified phases yields
\[
(1-\xi_J)H_m\preceq H_{m,J}\preceq H_m.
\]
Therefore
\[
\alpha G\preceq H_{m,J}\preceq\beta G,\quad
\alpha=(1-\xi_J)(1-\delta^2-\varepsilon),\quad
\beta=1+\varepsilon.
\]
Keep the chosen budgets
\[
0<\delta_0<1,\qquad
0<\varepsilon_0<1-\delta_0^2,\qquad
0<\xi_0<1.
\]
Both weighted Grams are positive, so \(b_a>0\), and the original \(\kappa>0\). The stated choices
\[
L=a^{-1}\log(1+\kappa/\delta_0+4b_a),\qquad
s=aL-\log(1+4b_a)
\]
give
\[
s=\log\frac{1+\kappa/\delta_0+4b_a}{1+4b_a}>0,\quad
aL-s=\log(1+4b_a)>0,
\]
and
\[
\delta=\frac{\kappa}{\kappa/\delta_0+4b_a}<\delta_0,\qquad
d_s=\frac{2b_a}{(1+4b_a)-1}=\frac12.
\]
The integer
\[
m=\max\left\{1,\left\lceil s^{-1}\log(1+4/\varepsilon_0)\right\rceil\right\}
\]
satisfies \(e^{sm}-1\ge4/\varepsilon_0\), hence
\[
\varepsilon=\frac4{e^{sm}-1}\le\varepsilon_0<1.
\]
To check exactly the given cutoff, name its actual real expression
\[
X=\frac L{2\pi}
\left(\frac{h_p}{(2p-1)\xi_0(1-\delta)}\right)^{1/(2p-1)},
\qquad J=2+\lceil X\rceil.
\]
This names an expression and does not change a source coordinate or object. Then \(J\ge2\) and \(J-1=1+\lceil X\rceil\ge X\). For \(h_p>0\), substitution into the proved tail yields
\[
\epsilon_J\le\frac{h_p}{2p-1}
\left(\frac L{2\pi X}\right)^{2p-1}
=\xi_0(1-\delta),\qquad \xi_J\le\xi_0.
\]
The displayed cutoff also handles \(h_p=0\) directly: \(X=0,J=2,\epsilon_J=\xi_J=0\), without division by \(X\). Finally
\[
\alpha>(1-\xi_0)(1-\delta_0^2-\varepsilon_0)>0.
\]
The strict inequality follows from \(\delta<\delta_0\), together with \(\varepsilon\le\varepsilon_0\) and \(\xi_J\le\xi_0\). These are explicit values from the actual weighted source integrals and budgets; no claim of executed interval arithmetic is used.

## HG21–HG22: discrepancy and the complete generator allowance

The original identity \(G=\overline G+\mathscr D\) gives exactly
\[
B_{m,J}=G^{-1}(H_{m,J}-G)
=-\mathsf D+\mathsf E_{m,J},\qquad
\mathsf E_{m,J}=G^{-1}(H_{m,J}-\overline G).
\]
Each endomorphism is \(G\)-self-adjoint because its product on the left by \(G\) is the displayed Hermitian form. The upper estimate is
\(H_{m,J}-\overline G\preceq\varepsilon G\).
The full lower estimate is
\[
\begin{aligned}
H_{m,J}-\overline G
&\succeq(1-\xi_J)(\overline G-\varepsilon G)-\overline G\\
&=-\xi_J\overline G-(1-\xi_J)\varepsilon G\\
&\succeq-[\xi_J+(1-\xi_J)\varepsilon]G,
\end{aligned}
\]
where the last sign uses \(\overline G\preceq G\). Thus
\[
\rho=\xi_J+(1-\xi_J)\varepsilon,\qquad
\rho-\varepsilon=\xi_J(1-\varepsilon)\ge0,\qquad
\|\mathsf E_{m,J}\|_G\le\rho.
\]
Also \(1-\rho=(1-\xi_J)(1-\varepsilon)>0\). Both the relation-cost and finite-tail signs remain as written.

The factor \(\alpha^{-1}\) in the generator estimate follows directly in the retained metrics. Put
\[
T_t=A+tR-kI/2,\quad H=H_{m,J}=G(I+B_{m,J}),\quad
\mathsf S=(I+B_{m,J})^{1/2},
\]
where the square root is positive in the original \(G\) metric. Its spectrum is at least \(\sqrt\alpha\), and \(\mathsf S^*G\mathsf S=H\), so it is an exact isometry from \((E,H)\) to \((E,G)\). For \(X_H=T_t^{\dagger_H}+T_t\),
\[
\mathsf S X_H\mathsf S^{-1}-X_G
=Z+Z^{\dagger_G},\qquad Z=[\mathsf S,T_t]\mathsf S^{-1}.
\]
This follows by expanding the first term as
\(\mathsf S^{-1}T_t^{\dagger_G}\mathsf S+\mathsf ST_t\mathsf S^{-1}\),
retaining both orders. The exact commutator solves
\[
\mathsf S[\mathsf S,T_t]+[\mathsf S,T_t]\mathsf S
=[\mathsf S^2,T_t]=[B_{m,J},T_t].
\]
Its solution is
\[
[\mathsf S,T_t]=\int_0^\infty
e^{-r\mathsf S}[B_{m,J},T_t]e^{-r\mathsf S}\,dr.
\]
Differentiation of the integrand proves the equation, with the original commutator at zero and zero limit at infinity. Uniqueness holds on each pair of eigenspaces since the sum of the two positive eigenvalues is nonzero. Consequently
\[
\|[\mathsf S,T_t]\|_G\le
\frac{\|[B_{m,J},T_t]\|_G}{2\sqrt\alpha},
\qquad\|\mathsf S^{-1}\|_G\le\alpha^{-1/2}.
\]
Use the isometry, reverse triangle inequality, and
\(\|Z+Z^{\dagger_G}\|_G\le2\|Z\|_G\).
They prove
\[
|\epsilon_H(t)-\epsilon_G(t)|
\le\alpha^{-1}\|[B_{m,J},T_t]\|_G.
\]
The full commutator is
\[
\begin{aligned}
[B_{m,J},T_t]
={}&-[\mathsf D,A]-t[\mathsf D,R]
+[\mathsf E_{m,J},A]+t[\mathsf E_{m,J},R]\\
={}&-[\mathsf D,T_t]+[\mathsf E_{m,J},T_t].
\end{aligned}
\]
The original complex \(t\) and all cancellation are retained; \(kI/2\) commutes and therefore contributes zero. Submultiplicativity gives the further allowance
\[
\|[B_{m,J},T_t]\|_G
\le\|[\mathsf D,T_t]\|_G+2\rho\|T_t\|_G.
\]
The independent spectral interval allowance is also correct. HG19 places the spectrum of \(B_{m,J}\) in \([\alpha-1,\varepsilon]\), and
\[
1-\alpha-\varepsilon
=\xi_J(1-\varepsilon)+(1-\xi_J)\delta^2\ge0.
\]
Hence
\[
\|B_{m,J}\|_G\le1-\alpha,\qquad
|\epsilon_H(t)-\epsilon_G(t)|
\le\frac{2(1-\alpha)}{\alpha}\|T_t\|_G.
\]
The source's strengthened allowance follows from the following complete spectral-projection argument, preserving the original operator and its spectral spaces. Let a \(G\)-self-adjoint endomorphism \(B\) have distinct eigenvalues \(b_1<\cdots<b_r\). For \(1\le j<r\), let \(P_j\) be its original \(G\)-orthogonal spectral projection onto the sum of eigenspaces whose eigenvalue is greater than \(b_j\). On the \(b_\ell\)-eigenspace,
\[
b_1I+\sum_{j=1}^{r-1}(b_{j+1}-b_j)P_j
=b_1+\sum_{j<\ell}(b_{j+1}-b_j)=b_\ell.
\]
Thus this expression is exactly \(B\), including every repeated-eigenvalue subspace. Relative to the \(G\)-orthogonal image and kernel of \(P_j\),
\[
[P_j,T]=
\begin{pmatrix}0&T_{12}\\-T_{21}&0\end{pmatrix}.
\]
For the original components \(u,v\), its squared output norm is
\(\|T_{12}v\|_G^2+\|T_{21}u\|_G^2\).
This proves that its operator norm is at most
\(\max(\|T_{12}\|,\|T_{21}\|)\); vectors supported in either component give the reverse inequality. Each block is an orthogonal compression of \(T\), so this maximum is at most \(\|T\|_G\). The complete decomposition therefore gives
\[
\|[B,T]\|_G
\le\sum_{j=1}^{r-1}(b_{j+1}-b_j)\|[P_j,T]\|_G
\le(b_r-b_1)\|T\|_G.
\]
When \(r=1\), \(B=b_1I\) and the commutator is zero. This proves HG11a without changing or centering \(B\).

For \(\mathsf D\), its original spectrum is contained in \([0,\delta^2]\); hence
\[
\|[\mathsf D,T_t]\|_G\le\delta^2\|T_t\|_G.
\]
For the finite actual \(B_{m,J}\), the interval \([\alpha-1,\beta-1]\) gives the stronger final allowance
\[
|\epsilon_{H_{m,J}}(t)-\epsilon_G(t)|
\le\frac{\beta-\alpha}{\alpha}\|T_t\|_G.
\]
It improves the valid preceding \(2(1-\alpha)/\alpha\) bound because
\(\beta-\alpha=(1-\alpha)+\varepsilon\le2(1-\alpha)\).

The same exact argument also gives the following refinement of the separate-tail estimate: the already proved spectrum of \(\mathsf E_{m,J}\) lies in \([-\rho,\varepsilon]\), so
\[
\|[\mathsf E_{m,J},T_t]\|_G
\le(\rho+\varepsilon)\|T_t\|_G
\le2\rho\|T_t\|_G.
\]
Thus the complete preserved commutator has the allowance
\[
\|-[\mathsf D,T_t]+[\mathsf E_{m,J},T_t]\|_G
\le\|[\mathsf D,T_t]\|_G+(\rho+\varepsilon)\|T_t\|_G.
\]
This sharper consequence was sent to the owner for propagation. All these bounds concern the same original control radius, so the lesser of their independently proved right-hand sides is valid. The actual \(B_{m,J}\) satisfies the \(G\)-self-adjointness required in HG14; its entire finite tail is therefore included when that exact rank-at-most-two residue formula is applied.

## HG23: original action, domain and boundary

For each retained phase \(\theta_j=2\pi j/m\), take the canonical section
\(C_{\theta_j,J}:E\to\mathcal P_N\) for \(M_{\theta_j,J}\succ0\).
The map
\[
SC_{\theta_j,J}-C_{\theta_j,J}A:E\longrightarrow\mathcal P_{N+1}
\]
has zero remainder modulo the original \(\chi\), since multiplication by \(S\) induces exactly \(A\). Monic division produces the unique map \(Q_{\theta_j,J}\) with
\[
SC_{\theta_j,J}-C_{\theta_j,J}A=\chi Q_{\theta_j,J}.
\]
The quotient has degree at most \(N+1-q\). This uses neither simple roots nor a discriminant inverse.

Let \(\mathcal O_{\theta_j,J}\) be the exact composite of the original source map, half-density isometry, twisted periodization and projection to \(|n|\le J\), with its degree-\(N+1\) domain used on that identity. Its degree-\(N\) restriction has Gram \(M_{\theta_j,J}\). Define
\[
\mathscr R_j=\mathcal O_{\theta_j,J}C_{\theta_j,J},\qquad
\mathscr B_j=\mathcal O_{\theta_j,J}(\chi Q_{\theta_j,J}).
\]
The source action carries multiplication by \(S\) to \(D^{(k)}\); the half-density map carries this to \(-\partial_r+k/2\); and periodization intertwines the same operators. On the original retained basis,
\[
D_{L,\theta_j}e_{n,\theta_j}
=\left(k/2+i(2\pi n+\theta_j)/L\right)e_{n,\theta_j}.
\]
Thus projection to the retained frequencies commutes exactly with \(D_{L,\theta_j}\). Every projected column is a finite \(\mathcal K\)-valued trigonometric sum in the quasi-periodic derivative domain. Therefore
\[
D_{L,\theta_j}\mathscr R_j-\mathscr R_jA=\mathscr B_j,\qquad
\mathscr R_j^*\mathscr R_j
=C_{\theta_j,J}^*M_{\theta_j,J}C_{\theta_j,J}
=G_{\theta_j,J}.
\]
The transverse space remains \(\mathcal K=L^2(\mathbb R^{k-1})\); finite phase and frequency indices do not replace that original target by a scalar space.

For two columns \(f,g\) with boundary multiplier \(e^{-i\theta_j}\),
\[
\langle f(L),g(L)\rangle_{\mathcal K}
=\langle e^{-i\theta_j}f(0),e^{-i\theta_j}g(0)\rangle_{\mathcal K}
=\langle f(0),g(0)\rangle_{\mathcal K}.
\]
Integration by parts therefore gives \(D^*+D=kI\) on these columns. Expand the two ordered terms:
\[
\begin{aligned}
\mathscr R_j^*\mathscr B_j+\mathscr B_j^*\mathscr R_j
&=\mathscr R_j^*D\mathscr R_j-G_{\theta_j,J}A
+\mathscr R_j^*D^*\mathscr R_j-A^*G_{\theta_j,J}\\
&=kG_{\theta_j,J}-G_{\theta_j,J}A-A^*G_{\theta_j,J}.
\end{aligned}
\]
Rearrangement and averaging give exactly
\[
A^*H_{m,J}+H_{m,J}A-kH_{m,J}
=-\frac1m\sum_j
(\mathscr R_j^*\mathscr B_j+\mathscr B_j^*\mathscr R_j).
\]
For the original complex \(t\), expansion of \(A+tR\) adds exactly
\[
\overline t R^*H_{m,J}+tH_{m,J}R.
\]
Multiplication of the complete form by \(H_{m,J}^{-1}\) gives
\(T_t^{\dagger_{H_{m,J}}}+T_t\), whose norm is the same control radius used in HG22. The relation boundary has not been asserted orthogonal to the representative. Even at \(N=q-1\), where the degree-\(N\) relation space is zero, multiplication by \(S\) reaches degree \(q\), so the degree-\(N+1\) action boundary remains present.

## HG24: positivity and the full original-metric ratio

For a nonzero proper \(A\)-invariant inclusion \(I:F\hookrightarrow E\) and positive \(T\), retain the two scalar factors
\[
d_T=\min_{x\in F}\|e_0-Ix\|_T^2,\qquad
u_T=\ell I(I^*TI)^{-1}I^*\ell^*,\qquad
\mathfrak c_F(T)=d_Tu_T.
\]
The first minimum exists since the finite-dimensional subspace \(I(F)\) is closed. If it were zero, positive definiteness would put \(e_0\) in \(I(F)\). Invariance and the complete cyclic list \(e_0,Ae_0,\ldots,A^{q-1}e_0\) would then give \(I(F)=E\), contradicting properness. Therefore \(d_T>0\).

The residue pairing is perfect for every monic \(\chi\). Indeed, for any nonzero degree-\(<q\) representative \(P\) of degree \(d\) and leading coefficient \(a_d\ne0\), choose \(Q=S^{q-1-d}\). The product has degree exactly \(q-1\), so
\[
\ell([P][Q])=a_d\ne0.
\]
If \(\ell I=0\), invariance forces \(\ell A^jI=0\) for every \(j\ge0\). For each \(f\in F\), its residue pairing with every monomial, and therefore every quotient element, is zero. Perfection forces \(If=0\) for every \(f\), contradicting nonzero \(F\). Thus \(\ell I\ne0\), and positivity of \((I^*TI)^{-1}\) proves \(u_T>0\). No vector mass or repeated-root data has been divided away.

For the actual comparison \(\alpha G\preceq T\preceq\beta G\), \(\alpha>0\), every original \(x\in F\) satisfies
\[
\alpha\|e_0-Ix\|_G^2
\le\|e_0-Ix\|_T^2
\le\beta\|e_0-Ix\|_G^2.
\]
Taking minima on the same affine family proves
\(\alpha d_G\le d_T\le\beta d_G\).
On the same \(F\),
\[
\alpha I^*GI\preceq I^*TI\preceq\beta I^*GI,
\]
so inverse order gives
\[
\beta^{-1}(I^*GI)^{-1}
\preceq(I^*TI)^{-1}
\preceq\alpha^{-1}(I^*GI)^{-1}.
\]
Apply the unchanged covector \(\ell I\) to obtain
\(\beta^{-1}u_G\le u_T\le\alpha^{-1}u_G\).
Multiplying these positive scalar comparisons proves the complete formula
\[
\frac\alpha\beta\mathfrak c_F(G)
\le\mathfrak c_F(T)
\le\frac\beta\alpha\mathfrak c_F(G).
\]
For \(T=\overline G\), take \(\alpha=1-\delta^2,\beta=1\); for \(T=H_{m,J}\), take the explicit positive constants of HG19–HG20. The original period metric \(\Pi(t)^*\Pi(t)\), its original \(u,t\), unit and residue functional retain their separately proved comparison and curvature expression. No phase character is substituted for the arithmetic action or the period parameter.

## Acceptance and continuity

All assigned estimates and ordered identities HG16–HG24 are accepted with the derivations above. The phase error \(\varepsilon\), source-tail error \(\epsilon_J\), phase-relative tail \(\xi_J\), and generator radius \(\epsilon_H(t)\) retain their distinct meanings.

The owner reviews HG25 and carries out global propagation. Root maintains the complete session and user-input provenance. This delegated review and its companion JSON record the present task and pins; all earlier v11/v15 source and visual acceptance files remain unchanged.
