# Independent proof review of the periodized-curvature control bridge

Date: 2026-09-13. The complete original FC1–FC23 source, complete LC1–LC16 source including LC12a, and the periodized-source note P19–P64 including P26a–P26b were read and checked. No source was edited; no numerical test, Lean run, or remote action was performed.

The complete detailed LC proof is retained verbatim as the companion work/periodized_curvature_control_lc_peer_20260913.md, SHA-256 7cf70ef4bfe2a4aae0bcfca10fd07a80068c9e89e617c656d3d1c1049d6592f1. It was read in full in this review. This file supplies the full P/FC derivations and their exact connection to LC. The JSON companion records all source hashes and read scopes.

No mathematical defect was found in the assigned FC or LC formulas. The original P note uses inherited symbols \(v_h,w_h\) without first giving standalone definitions. The intake companion PSA1 already supplies the necessary exact definitions
\[
g(s)=2\xi(s),\qquad v_h(s)=g(s)/h(s),\qquad
w_h(t)=\frac{|v_h(1/2+it)|^2}{2\pi},\qquad m_{h,k}=w_h^{*k}.
\]
Here \(g/h\) is its entire canceled extension at every selected zero, retaining all orders. This known presentation correction does not change the P formulas. The complete density companion work/periodized_source_density_review_20260913.md was read; its PSD1–PSD40 supplies the detailed tail, exact Hilbert map, and completion proofs.

The original FC source has SHA-256 9837c2970dcef4ff89449c2d4535ecd0648ff4d1b53ba2ed48db3900e7c77694 and is preserved as work/periodized_curvature_control_before_endpoint_strengthening_20260913.tex. LC has SHA-256 84d884eeceae8ab339b78c29404d86798fcd04b6d40dde1abcff1cc7ed631231. During review the author explicitly added FC3a, sharpened FC13, and supplied FC24–FC29. The entire exact source diff was read, including the integer tensor-degree typing. All additions are proved below. The final reviewed FC source is SHA-256 4b831330fad05c6092d3887f877fadcd84eebe94d83e8b000324ec031f1e3779, with complete FC1–FC29 and FC3a.

## 1. Original coordinates, source regularity, and Fourier constants

Retain \(E=\mathbb C[S]/(\chi)\), with the original monic \(\chi\) of degree \(q\ge1\), the increasing-power remainder frame, \(A=M_S\), \(e_0=[1]\), and \(\ell[P]=[S^{q-1}]\operatorname{rem}_{\chi}P\). At degree \(N\ge q-1\), the original remainder map \(J_N:\mathcal P_N\to E\) is surjective because the first \(q\) powers give the remainder basis. Its original Gram \(M_N\) is positive: the squared norm of a nonzero source polynomial integrates \(|P(k/2+iu)|^2m_{h,k}(u)\); the density is positive almost everywhere and a nonzero polynomial has only finitely many roots.

For \(k=1\), \(\mathcal K=\mathbb C\); otherwise \(\mathcal K=L^2(\mathbb R^{k-1},d\mathbf z)\). In the ordered coordinates \((r,z_1,\ldots,z_{k-1})\), put \(y_i=r+z_i\) for \(i<k\), \(y_k=r\), and \(x_i=e^{y_i}\). The determinant to the ordered \(y\) coordinates is \((-1)^{k-1}\); its absolute value is one. Consequently
\[
d^kx=e^{kr+\sum_{i<k}z_i}\,dr\,d\mathbf z.
\]
Multiplication by the exact square-root density gives FC2/P12. The inverse substitutes \(r=\log x_k\), \(z_i=\log x_i-\log x_k\), and multiplies by \((x_1\cdots x_k)^{-1/2}\). Direct substitution proves both composites are the identity and proves equality of squared norms. Simultaneous translation of all \(y_i\) changes \(r\) with all \(z_i\) fixed, so
\[
\mathcal U_kD^{(k)}=(-\partial_r+k/2)\mathcal U_k,\qquad
\partial_r^p\mathcal U_k=(-1)^p\mathcal U_k(D^{(k)}-k/2)^p.
\]
The original tensor-sum coordinate \(S\), the variable \(r\), and the factor \(k/2\) are unchanged.

For every fixed \(a>0,j\ge0\), strong-Schwartz estimates on the finite tensor source give
\[
I_{a,j}:=\int e^{2a|r|}\|\partial_r^j\psi(r)\|_{\mathcal K}^2dr<\infty.
\]
After the exact coordinate substitution this is bounded by the sum of the original integrals with weights \(x_k^{2a},x_k^{-2a}\), applied to the indicated finite derivative tensor combination. Each integral factors into finite strong-Schwartz integrals. For a Hilbert-valued \(H^1\) function on \([r,r+1]\), choose a point with squared norm at most its average, integrate the derivative, and apply Cauchy–Schwarz; this proves
\[
\|f(r)\|^2\le2\int_r^{r+1}(\|f(t)\|^2+\|f'(t)\|^2)dt.
\]
Thus
\[
\|\partial_r^j\psi(r)\|^2
\le2e^{2a}e^{-2a|r|}(I_{a,j}+I_{a,j+1}).
\]
This proves uniform convergence of every periodized derivative on one period and absolute convergence of the unfolded products below, on the stated finite source.

The plus Fourier transform is \(\widehat\psi(u)=\int\psi(r)e^{iur}dr\). Integration by parts sends \(-\partial_r+k/2\) to \(k/2+iu\). The orthonormal circle basis is \(L^{-1/2}e^{-2\pi inr/L}\); unfolding its coefficient gives \(L^{-1/2}\widehat\psi(2\pi n/L)\). Hence Parseval gives the exact \(L^{-1}\) in P26 and FC4. At zero, the Fourier coefficient \(L^{-1/2}\widehat\psi(0)\) and the constant function's value \(L^{-1}\widehat\psi(0)\) are different specified quantities. The P17 component with metric \(L^{-1}\langle\, ,\,\rangle_{\mathcal K}\) reconstructs precisely the full zero coefficient.

For the tensor seed, in simultaneous Fourier variables set \(t_k=u-\sum_{i<k}t_i\). The amplitude is
\[
\prod_{i<k}v_h(1/2+it_i)\,v_h(1/2+it_k).
\]
Partial Plancherel in the \(k-1\) relative variables contributes \((2\pi)^{-(k-1)}\), whereas the actual convolution already contains \((2\pi)^{-k}\). Therefore, pointwise in \(u\),
\[
\|\widehat{\mathcal U_kF_h^{\otimes k}}(u)\|_{\mathcal K}^2
=2\pi m_{h,k}(u).
\]
Absolute convergence and continuity determine this pointwise representative, so the formula can be evaluated at the lattice nodes. Applying the original polynomials \(P_a(k/2+iu)\) proves P26a–P26b with every factor \(2\pi/L\). For \(k\ge2\), \(w_h*w_h(u)>0\) everywhere: the two discrete zero sets leave a point where its continuous integrand is positive on an interval. Further convolutions preserve strict positivity. Thus the full periodic Gram is positive at every finite source degree for \(k\ge2\). No all-integer positivity assertion is extended to \(k=1\).

## 2. P19–P32: full period recovery and exact all-period identity

For the original coefficient vectors define
\[
c^*\mathcal C(s)d=\int\langle\Psi c(r),\Psi d(r+s)\rangle_{\mathcal K}dr.
\]
Expanding the two periodized series, grouping by their index difference, and unfolding one period gives \(M(L)=\sum_{m\in\mathbb Z}\mathcal C(mL)\), \(\mathcal C(0)=M\). The full sum is Hermitian even though a single correlation need not be.

For \(s>0\), insert \(e^{-ar}\) in the first factor and \(e^{a(r+s)}\) in the second. Their product is \(e^{as}\) times the original integrand. Cauchy–Schwarz yields
\[
|c^*\mathcal C(s)c|
\le e^{-as}\sqrt{(c^*M_{a,-}c)(c^*M_{a,+}c)}.
\]
For \(s<0\), interchange the weights. Summing both nonzero lattice directions and then using the elementary product inequality gives
\[
|c^*(M(L)-M)c|
\le\frac{2\sqrt{(c^*M_{a,-}c)(c^*M_{a,+}c)}}{e^{aL}-1}
\le\frac{c^*(M_{a,-}+M_{a,+})c}{e^{aL}-1}.
\]
This holds for every unchanged coefficient vector, proving the full Loewner inequalities, including all cross entries. The weighted forms are exactly the original integrals with \(x_k^{\pm2a}\). Subtracting the zero Fourier summand gives P27 with its literal \(L^{-1}Z_0^*Z_0\).

For the positive exponent \(\delta\) in P28–P32, evaluate the proposed identity on a coefficient \(c\) and apply Tonelli to the nonnegative Fourier sum. At \(n>0\), the substitution \(u=2\pi n/L\), with reversed integration endpoints, gives
\[
\int_0^\infty L^{-2-\delta}\|\widehat{\Psi c}(2\pi n/L)\|^2dL
=(2\pi n)^{-1-\delta}\int_0^\infty u^\delta\|\widehat{\Psi c}(u)\|^2du.
\]
The negative indices yield the negative half-line with \(|u|^\delta\). Summing the positive integers gives exactly \(\zeta(1+\delta)\). Multiplication by \((2\pi)^\delta/\zeta(1+\delta)\) leaves the original continuous factor \(1/(2\pi)\), proving P29. Polarization recovers every matrix entry. This identity integrates source Grams before taking any nonlinear quotient minimum.

For \(0<\delta\le\delta_0\), the mean-value formula in the exponent gives
\[
\big||u|^\delta-1\big|
\le\delta|\log|u||\,(1+|u|^{\delta_0})\qquad(u\ne0).
\]
The logarithm is integrable at zero and the remaining tails are Schwartz. Integrating each quadratic form proves P31–P32 and \(M_\delta\to M\). On any vector with \(Z_0c\ne0\), inserting the raw zero summand into the all-period integral produces the divergent factor \(\int_0^1L^{-2-\delta}dL\). The separate reconstruction is therefore exact.

## 3. P33–P42, P59–P64, FC1–FC7: finite source and quotient errors

For positive \(M\) and surjective \(J\), retain
\[
G=(JM^{-1}J^*)^{-1},\qquad C=M^{-1}J^*G.
\]
\(JM^{-1}J^*>0\) because \(J^*\) is injective. Multiplication gives \(JC=I\), \(C^*MC=G\). Every representative of \(v\) is \(Cv+z\), \(z\in\ker J\), and \(z^*MCv=z^*J^*Gv=0\). Consequently
\[
(Cv+z)^*M(Cv+z)=v^*Gv+z^*Mz.
\]
This proves the exact unique minimum and its coefficient lift, including FC1, FC6, and P36.

The finite Rayleigh maxima \(\kappa_{a,D},\lambda_{p,D}\) exist because \(M_D>0\). Every smaller-degree form is the restriction under its actual polynomial inclusion, so those maxima bound all smaller-degree quotients. Section 2 gives the period error \(-\eta_PM_N\preceq M_N(L)-M_N\preceq\eta_PM_N\) with the exact \(\eta_P=\kappa_{a,D}/(e^{aL}-1)\).

Integration by parts \(p\) times gives \(\widehat{\partial_r^p\psi}(u)=(-iu)^p\widehat\psi(u)\). Weighted Cauchy–Schwarz therefore gives
\[
\|\widehat{\Psi_Nc}(u)\|^2
\le |u|^{-2p}\left(\int(1+r^2)^{-1}dr\right)
\int(1+r^2)\|\partial_r^p\Psi_Nc(r)\|^2dr
=\pi|u|^{-2p}c^*H_{p,N}c.
\]
The omitted Fourier Gram is positive. Its two tails have coefficient
\[
\frac{2\pi}{L}\left(\frac L{2\pi}\right)^{2p}
\sum_{n>J}n^{-2p}
\le\frac1{2p-1}\left(\frac L{2\pi J}\right)^{2p-1}.
\]
The last step integrates the decreasing function \(x^{-2p}\) from \(J\) to infinity; it holds for the stated integers \(p,J\ge1\). Since \(H_{p,N}\preceq\lambda_{p,D}M_N\), this proves the exact FC3/P61 tail factor.

Put \(\eta_T=\lambda_{p,D}(L/(2\pi J))^{2p-1}/(2p-1)\), \(\alpha=1-\eta_P-\eta_T\), and \(\beta=1+\eta_P\). Subtracting the positive tail from the period comparison proves
\[
\alpha M_N\preceq M_N(L,J)\preceq\beta M_N.
\]
This is the sharper asymmetric FC5, and its symmetric weakening is P63. For positive budgets \(\varepsilon_P+\varepsilon_T<1\), FC3a/P64 choose
\[
L\ge a^{-1}\log(1+\kappa_{a,D}/\varepsilon_P),\qquad
J\ge\max\left\{1,D,\frac L{2\pi}
\left(\frac{\lambda_{p,D}}{(2p-1)\varepsilon_T}\right)^{1/(2p-1)}\right\},
\quad J\in\mathbb Z.
\]
Direct substitution gives \(\eta_P\le\varepsilon_P\), \(\eta_T\le\varepsilon_T\), including \(\lambda_{p,D}=0\). An integer ceiling preserves the inequality. Hence \(\alpha>0\) is proved before every sampled inverse is taken.

Apply the source form bounds to each representative of the same \(v\), then take the exact minima proved above. This gives \(\alpha G\preceq H\preceq\beta G\). With FC's \(\delta=\eta_P+\eta_T\), it also gives \((1-\delta)G\preceq H\preceq(1+\delta)G\). The eigenvalues of the \(G\)-self-adjoint \(G^{-1}H\) lie in \([\alpha,\beta]\); their product is \(\det H/\det G\). Thus each endpoint log-determinant error lies in \([q\log\alpha,q\log\beta]\). Two numerator and two denominator errors give exactly \(2q\log(\beta/\alpha)\). The symmetric special case proves P39–P41. At fixed symmetric error budget, division by the unchanged \(q_k\log k\) bounds the P42 difference by a fixed constant divided by \(\log k\), which tends to zero.

The two minimizers differ by \(\ker J_N=\chi\mathcal P_{N-q}\), with zero relation space at \(N=q-1\). Monic division gives their exact quotient polynomial. The original annihilator relation gives \(\chi(S)Q(S)=\sum_i h(s_i)Q_i(\mathbf s)\), by fixed ordered monic division. In the tensor complex with \(V\) in degree zero and \(\mathscr B\) in degree one, the primitive with \(V\) in slot \(i\) has differential sign \((-1)^{i-1}\). Giving that primitive the same coefficient makes its boundary the positive \(i\)-th summand. Replacing \(F_h\) by \(\phi_*\) in that slot and applying \(Q_i(D_1,\ldots,D_k)\) proves the asserted original primitive, retaining each polynomial, sign, and support.

## 4. P43–P58: periodic operator, exact image quotient, and completion

On the original circle basis, \(D_L=-\partial_r+k/2\) has diagonal \(k/2+2\pi in/L\). Its quadratic expression is \(\partial_r^2-k^2/4\), with real diagonal \(-(2\pi n/L)^2-k^2/4\). On the domain where the squared diagonal is summable it is self-adjoint: coordinatewise computation of the adjoint gives exactly the same real diagonal and domain. This proves P43–P44 and retains the zero mode at \(-k^2/4\).

Intertwining gives \(D_LR_{N,L}-R_{N,L}A=B_{N,L}\), \(R_{N,L}^*R_{N,L}=G_N(L)\). Since \(D_L^*+D_L=k\) on the smooth columns,
\[
R^*B+B^*R
=R^*(D_L+D_L^*)R-G_N(L)A-A^*G_N(L)
=-W_{G_N(L)}(0).
\]
Applying \(D_L\) again gives \(D_L^2R=RA^2+BA+D_LB\); subtracting \(kD_LR=kRA+kB\) proves P48 with both \((D_L-k)B\) and \(BA\). On \(Av=\rho v\), this boundary equals \((\mathscr L_{L,k}-\rho(\rho-k))Rv\). Expansion in the real diagonal proves that its squared norm is at least \(|\operatorname{Im}(\rho(\rho-k))|^2\|Rv\|^2\), establishing P49 in its actual lower-bound direction.

Positivity of the finite source Gram makes \(\Phi_{N,L}\) injective. Its inverse onto its image defines \(J_N\Phi_{N,L}^{-1}\), whose kernel is exactly \(\Phi_{N,L}(\ker J_N)\). Thus P52 identifies that image quotient with the full \(E\). P50 is explicitly the named inherited critical Schwartz comparison theorem, not a new assertion proved by periodization. Given its stated kernel \(E_{Z,\mathrm{off}}\), P51 is the exact sequence of that map onto its actual image. The two-term complex in degrees \(-1,0\) has its kernel as degree-\(-1\) cohomology and zero degree-zero cohomology. This verifies the precise use of that inherited input without erasing its kernel.

For \(k\ge2\), set \(u_n=2\pi n/L\), \(S_n=k/2+iu_n\), \(b_n=\widehat{\mathcal U_kF_h^{\otimes k}}(u_n)\), and \(\nu_n=\|b_n\|^2/L=(2\pi/L)m_{h,k}(u_n)>0\). The isometry from \(\ell^2(\mathbb Z,\nu)\) into the original circle space has \(n\)-th Fourier coefficient \(L^{-1/2}a_nb_n\). Its squared norm is \(\sum_n\nu_n|a_n|^2\); on polynomials \(a_n=P(S_n)\) it equals the actual periodized source. Its inverse on its range is
\[
a_n=\sqrt L\,
\frac{\langle b_n,\widehat f(n)\rangle_{\mathcal K}}{\|b_n\|^2}.
\]
All denominators are positive. Thus the sequence description has a proved exact map to the unchanged Hilbert-valued source.

The density companion's original-source tail can be checked directly. Rotation of the gamma-integral ray by \(\operatorname{sign}(y)\theta\) gives
\[
|\Gamma(a+iy)|\le\Gamma(a)(\cos\theta)^{-a}e^{-\theta|y|},
\quad a>0,\quad0<\theta<\pi/2.
\]
The small arc is \(O(\varepsilon^a)\); the large arc is a power times \(e^{-R\cos\theta}\). Both vanish, and the rotated ray has exactly the factor \(e^{-\theta|y|}\). For \(\operatorname{Re}s>0\), partial summation gives \(\eta(s)=s\int_1^\infty A(x)x^{-s-1}dx\), \(A(x)\in\{0,1\}\). On \(s=1/2+it\), this gives \(|\eta(s)|\le2|s|\), and \(|1-2^{1-s}|\ge\sqrt2-1\), so \(|\zeta(s)|\le2|s|/(\sqrt2-1)\). The identity between \(\eta\) and \(\zeta\) first holds by absolutely convergent rearrangement and then by analytic continuation.

Using the original \(g(s)=s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)\), the square modulus and the literal \(1/(2\pi)\) give
\[
w_h(t)\le
\frac{2\Gamma(1/4)^2}{\pi^{3/2}(\sqrt2-1)^2\sqrt{\cos\theta}}
\frac{(t^2+1/4)^3}{|h(1/2+it)|^2}e^{-\theta|t|}.
\]
For the monic \(h\), if \(|t|\ge R=\max(1,2\max_\rho|\rho-1/2|)\), its original product gives \(|h(1/2+it)|\ge(|t|/2)^{\deg h}\). The compact remainder uses the entire canceled quotient, which is bounded there. Taking \(b<\theta<\pi/2\) therefore proves \(e^{b|t|}w_h\in L^1\cap L^\infty\), with the full denominator and constants retained. If a selected root has order \(m\), its canceled value is \(g^{(m)}(\rho)/h^{(m)}(\rho)\ne0\), by factoring both original functions; it is not an uncanceled \(0/0\).

The triangle inequality inside convolution proves pointwise
\[
e^{b|u|}m_{h,k}(u)
\le(e^{b|\cdot|}w_h)^{*k}(u)
\le\|e^{b|\cdot|}w_h\|_\infty
\|e^{b|\cdot|}w_h\|_1^{k-1}.
\]
This is P54. It gives finite exponential moments for the lattice measure and each polynomially weighted version.

Here is the needed full polynomial-density proof. Suppose \(\mu_n>0\) on a subset \(I\) of this lattice and \(\sum_Ie^{c|u_n|}\mu_n<\infty\). If \(f\in\ell^2(I,\mu)\) is orthogonal to all polynomials, then Cauchy–Schwarz gives \(\sum_I|f_n|\mu_ne^{a|u_n|}<\infty\) for \(0<a<c/2\). Consequently
\[
F(z)=\sum_{n\in I}\overline{f_n}\mu_ne^{izu_n}
\]
is holomorphic on \(|\operatorname{Im}z|<c/2\). On any smaller closed strip, an extra exponential margin absorbs every fixed power of \(|u_n|\), proving normal convergence of all derivative series. The original polynomial \(((S-k/2)/i)^j\) evaluates to \(u_n^j\); orthogonality therefore makes every derivative of \(F\) at zero vanish. The identity theorem gives \(F=0\). Absolute summability permits termwise integration of \(F(x)e^{-2\pi imx/L}\) over \([0,L]\); division by \(L\) recovers exactly \(\overline{f_m}\mu_m\). Thus \(f=0\), proving density. The half-width \(c/2\) is the justified one.

Let \(\mathcal Z_L=\{n:\chi(S_n)=0\}\) and \(p_L(S)=\prod_{n\in\mathcal Z_L}(S-S_n)\), with empty product one. Coordinate evaluation has norm \(\nu_n^{-1/2}\). Hence the closure of \(\chi\mathbb C[S]\) vanishes on \(\mathcal Z_L\). Conversely, if \(f\) vanishes there, the sequence \(f_n/\chi(S_n)\) on the complement has squared norm \(\sum_{n\notin\mathcal Z_L}|f_n|^2\nu_n\) for the measure \(|\chi(S_n)|^2\nu_n\). The proved density for this measure and multiplication by \(\chi\) approximate \(f\) in its original norm. This identifies the closed relation space exactly. Its quotient is the values on \(\mathcal Z_L\), with metric \(\sum_{n\in\mathcal Z_L}\nu_n|v_n|^2\), proving P56.

The evaluation map from \(E\) is onto by the original Lagrange polynomials \(\prod_{m\ne n}(S-S_m)/(S_n-S_m)\). A polynomial vanishes at these distinct nodes exactly when divisible by \(p_L\); since \(p_L\mid\chi\), its kernel is \((p_L)/(\chi)\), proving P57. The exact injective map onto that kernel is \([Q]_{\chi/p_L}\mapsto[p_LQ]_\chi\): cancellation proves injectivity without coprimality. In each full primary algebra \(\mathbb C[\varepsilon]/(\varepsilon^m)\), a sampled root maps to its constant term and leaves \(\varepsilon\mathbb C[\varepsilon]/(\varepsilon^m)\) in the kernel; an unsampled primary block remains entirely in the kernel. Multiplication by the original \(S\) intertwines and induces \(S_n\) on surviving coordinates. Its quadratic expression induces \(-k^2/4-u_n^2\).

For a fixed remainder \(v\), its degree-\(N\) representatives are \(R_v+\chi\mathcal P_{N-q}\). Their increasing relation spaces have union \(\chi\mathbb C[S]\). The finite-degree minima decrease to the distance to its computed closure, namely \(\sum_{n\in\mathcal Z_L}\nu_n|R_v(S_n)|^2\). Polarization determines each entry and finite dimension gives P58 as a matrix limit. Its radical is precisely the kernel \((p_L)/(\chi)\). Thus all completed-away directions are related to the original packet through explicit maps and an exact limit. The all-integer positivity and finite-degree inverse statements here retain the specified \(k\ge2\) domain.

## 5. FC8–FC13: residue coefficient and exact endpoint factors

Let \(I:F\hookrightarrow E\), \(AI=IA_F\), \(0<\dim F<q\). Invariance under \(A\) implies invariance under every polynomial in \(A\), so \(I(F)\) is an ideal of the original algebra. Its polynomial preimage is \((g)\), where \(\chi=gh\) with monic \(g,h\). The map \([a]_h\mapsto[ga]_\chi\) is onto that ideal and injective by cancellation. Hence \(\deg h=p_F=\dim F\), and its full basis is \([g],\ldots,[S^{p_F-1}g]\). The last member is monic of degree \(q-1\), proving \(L_F=\ell I\ne0\). A proper ideal cannot contain \(e_0=[1]\). This proves strict positivity below with every repeated factor retained, and shows \(q>1\) in this subsection.

For positive \(T\), the displayed \(P_{T,F}=I(I^*TI)^{-1}I^*T\) satisfies \(P^2=P\), \(P^*T=TP\), and has image \(I(F)\). Completion of the square gives
\[
a_F(T)=\min_x(e_0-Ix)^*T(e_0-Ix)
=\|(1-P_{T,F})e_0\|_T^2>0.
\]
Also \(b_F(T)=L_F(I^*TI)^{-1}L_F^*>0\). For every positive \(T\) and column \(w\), exact square completion gives
\[
2\operatorname{Re}(w^*x)-x^*Tx
=w^*T^{-1}w-(x-T^{-1}w)^*T(x-T^{-1}w).
\]
Its maximum is \(w^*T^{-1}w\), proving inverse order without a commutation assumption.

Apply \(\alpha G\preceq H\preceq\beta G\) to every \(e_0-Ix\), then take minima. This gives \(\alpha a_F(G)\le a_F(H)\le\beta a_F(G)\). Compress the same forms by \(I\), use inverse order, and evaluate on \(L_F^*\). It gives \(\beta^{-1}b_F(G)\le b_F(H)\le\alpha^{-1}b_F(G)\). Multiplying the positive factors proves exactly
\[
\frac\alpha\beta\le
\frac{\mathfrak c_F(H)}{\mathfrak c_F(G)}
\le\frac\beta\alpha,\qquad
\left|\log\frac{\mathfrak c_F(H)}{\mathfrak c_F(G)}\right|
\le\log\frac\beta\alpha.
\]
The same direct and inverse evaluations on \(e_0\) and \(\ell^*\) prove FC10. No determinant or dimension factor enters either coefficient estimate.

For \(T_{\rm per}=\Pi^*\Pi>0\), the operator \(H^{-1}T_{\rm per}\) is \(H\)-self-adjoint and positive because \(H(H^{-1}T_{\rm per})=T_{\rm per}\). Its exact extreme eigenvalues \(m_H,M_H\) imply \(m_HH\preceq T_{\rm per}\preceq M_HH\). The just-proved minimum/inverse argument gives FC11 with the literal factors \(m_H/M_H,M_H/m_H\).

For the original nested endpoint forms \(G_i\succeq G_j>0\), let \(\theta,\zeta_+\) be the least and greatest eigenvalues of \(G_i^{-1}G_j\), preserving the final FC notation. Then \(0<\theta\le\zeta_+\le1\) and \(\theta G_i\preceq G_j\preceq\zeta_+G_i\). Applying the same argument gives the strengthened FC13:
\[
\left|\log\frac{\mathfrak c_F(G_j)}{\mathfrak c_F(G_i)}\right|
\le\log(\zeta_+/\theta)\le-\log\theta
\le\log\frac{\det G_i}{\det G_j}.
\]
For the last inequality, the product of the \(q\) eigenvalues in \((0,1]\) is at most their least member \(\theta\). Taking negative logarithms gives exactly the displayed direction. This also proves the original weaker FC13 and shows the new greatest-eigenvalue factor is a valid strengthening.

The RCX18–RCX21 path derivation was read as a crosscheck. Its symbol \(\eta\) denotes exactly the greatest eigenvalue called \(\zeta_+\) in FC13. With \(T=G_i^{-1}G_j\), \(M(s)=G_i(I+s(T-I))\), direct multiplication gives \(M(s)^{-1}\dot M(s)=(I+s(T-I))^{-1}(T-I)\). Its eigenvalue at \(\lambda\) is \((\lambda-1)/(1+s(\lambda-1))\); the derivative with respect to \(\lambda\) is \(1/(1+s(\lambda-1))^2>0\). Integrating the spread of its extreme values gives \(\log\eta-\log\theta=\log\zeta_+-\log\theta\). All denominators stay positive for \(0\le s\le1\), since every original \(\lambda>0\). This agrees with the direct minimum/inverse proof above and requires no rescaling of an arithmetic source.

## 6. FC14–FC18: complete control transfer and the original-metric parabola

Retain \(A_t=A+tR\), \(R=e_0\ell\), \(T_t=A_t-kI/2\), with real \(k\). Then \(W_G=T_t^*G+GT_t\), \(W_H=T_t^*H+HT_t\). For \(B=G^{-1}(H-G)\), the exact identity \(GB=H-G\) shows \(B^{\dagger_G}=B\). The form bounds give \(-\delta G\preceq GB\preceq\delta G\), hence \(\|B\|_G\le\delta\). Also \(H=G(I+B)\) in the original coordinates.

Since \(I+B=G^{-1}H\), multiplying \(X_H=H^{-1}W_H\) gives
\[
(I+B)X_H=G^{-1}W_H
=X_G+T_t^{\dagger_G}B+BT_t.
\]
This proves FC15 with both noncommuting products retained. On each original vector,
\[
v^*(W_H-W_G)v
=\langle T_tv,Bv\rangle_G+\langle Bv,T_tv\rangle_G.
\]
Cauchy–Schwarz bounds its modulus by \(2\delta\tau_G(t)v^*Gv\), \(\tau_G=\|T_t\|_G\), proving FC16.

Both \(X_G\) and \(X_H\) are self-adjoint in their respective metrics, so their norms are the suprema of their absolute quadratic-form quotients. Dividing the numerator estimate by \(v^*Hv\ge\alpha v^*Gv\) gives
\[
\epsilon_H\le\frac{\epsilon_G+2\delta\tau_G}{\alpha}.
\]
Reversing the numerator comparison, using \(v^*Hv\le\beta v^*Gv\), and taking the \(G\)-form supremum gives
\[
\epsilon_G\le\beta\epsilon_H+2\delta\tau_G.
\]
Thus FC17 retains the actual generator size. It makes no inference that a small relative metric error alone controls an arbitrarily large generator.

Set \(e=\beta\epsilon_H+2\delta\tau_G\ge\epsilon_G\). Expanding the unchanged operators gives
\[
G(A_t^2-kA_t)=W_GT_t-T_t^*GT_t-k^2G/4.
\]
For nonzero original \(v\), let \(z,r,a,b\) have exactly the FC18 definitions. Cauchy–Schwarz gives \(a^2+b^2\le e^2r^2\), while the displayed expansion gives
\[
\operatorname{Re}z=a-r^2-k^2/4,\qquad\operatorname{Im}z=b.
\]
Since \(a\le er\), completing the scalar square gives
\[
\operatorname{Re}z\le(e^2-k^2)/4-(r-e/2)^2\le(e^2-k^2)/4.
\]
Direct expansion gives the second inequality through the exact identity
\[
e^2\left((e^2-k^2)/4-\operatorname{Re}z\right)-b^2
=(a-e^2/2)^2+(e^2r^2-a^2-b^2)\ge0.
\]
If \(e=0\), then \(a=b=0\) and \(\operatorname{Re}z=-r^2-k^2/4\le-k^2/4\). No division by \(e\), change of metric, or replacement of the original vector occurs.

The LC additional radius used here is exact. For \(q>1\), \(R^2=0\), and the original columns \(e_0,f=G^{-1}\ell^*\) have Gram \(\operatorname{diag}(a_0,b_0)\), where \(a_0=e_0^*Ge_0\), \(b_0=\ell G^{-1}\ell^*\). They are orthogonal because \(\ell e_0=0\). On these unscaled columns the self-adjoint perturbation \(tR+\bar tR^{\dagger_G}\) has matrix
\[
\begin{pmatrix}0&tb_0\\\bar t a_0&0\end{pmatrix}.
\]
Both terms vanish on their \(G\)-orthogonal complement. Its eigenvalues are \(\pm|t|\sqrt{a_0b_0}\), giving the exact extra radius \(|t|\sigma(G)\). For \(q=1\), \(R=I_E\), and the exact extra radius is \(2|\operatorname{Re}t|\), not \(2|t|\). FC10 controls the same \(\sigma^2\); the full LC proof and all boundary cases are included in the appendix below.

## 7. FC19–FC20: the actual finite Fourier boundary

\(Q_J\) is the orthogonal projection onto the modes \(|n|\le J\) with the entire original \(\mathcal K\) fibre at each mode. It commutes with \(D_L\), since both are diagonal in the same Fourier decomposition. Finite mode count does not replace the retained \(\mathcal K\)-valued target by an unrelated scalar space.

For \(C=C_N(L,J)\), the exact minimum identities give \(J_NC=I_E\), \(C^*M_N(L,J)C=H\). Hence
\[
\mathscr R=Q_J\mathcal P_L\mathcal U_k\mathcal V_{h,k}C
\quad\hbox{satisfies}\quad\mathscr R^*\mathscr R=H.
\]
Intertwining, followed by the commuting \(Q_J\), gives \(D_L\mathscr R-\mathscr RA=\mathscr B\). The coefficient polynomial of the original relation is \(SC-CA\); its remainder is zero, since multiplication by \(S\) descends to \(A\). Ordered monic division therefore gives the same explicit tensor primitive proved in Section 3, now in the source degree raised by one when necessary. This exact identity does not assert that the finite source image is an invariant circle eigenspace.

Substitution into \(\mathscr R^*(D_L+D_L^*)\mathscr R=kH\) gives
\[
W_H(0)=-(\mathscr R^*\mathscr B+\mathscr B^*\mathscr R).
\]
Applying \(D_L\) once more and subtracting \(kD_L\mathscr R\) gives
\[
(D_L^2-kD_L)\mathscr R-\mathscr R(A^2-kA)
=(D_L-k)\mathscr B+\mathscr BA.
\]
Every term is defined on these smooth finite-mode columns. Thus FC20 supplies the actual boundary form transported by FC17, including its negative sign and both quadratic boundary terms. It supplies no uncomputed interval enclosure for the arithmetic entries.

## 8. FC12 and FC21–FC23: exact constituent and quotient compensation

At fixed original \(u\ne0\), the retained period matrix is holomorphic in \(t\), invertible at every \(t\), and obeys \(\Pi'=-\Pi(A+tR)/u\). For \(Y=\Pi I\), \(H_F=Y^*Y\), \(P=YH_F^{-1}Y^*\), invariance \(AI=IA_F\) gives
\[
Y'=-YA_F/u-t\Pi e_0L_F/u,\qquad
(1-P)Y'=-t(1-P)\Pi e_0L_F/u.
\]
The residual norm is exactly \(a_F(T_{\rm per})\) by its original coefficient minimum, and \(L_FH_F^{-1}L_F^*=b_F(T_{\rm per})\).

With the original Wirtinger derivatives,
\[
\partial_tH_F=Y^*Y',\quad
\partial_{\bar t}H_F=Y'^*Y,\quad
\partial_{\bar t}H_F^{-1}=-H_F^{-1}Y'^*YH_F^{-1}.
\]
Differentiating the determinant and using cyclic trace gives
\[
\partial_{\bar t}\partial_t\log\det H_F
=\operatorname{Tr}(H_F^{-1}Y'^*(1-P)Y')
=\frac{|t|^2}{|u|^2}a_F(T_{\rm per})b_F(T_{\rm per}).
\]
This proves FC12 with the exact sign and \(|u|^{-2}\), without an additional real-Laplacian factor of four.

Choose the constant lift \(J_F\) of the fixed original quotient basis, and retain \(C=[I,J_F]\). The lift columns together with \(I(F)\) form a basis, so \(C\) is invertible. Completing the square in \(\|\Pi(J_Fv+Ix)\|^2\) gives the unique minimizing \(x=-H_F^{-1}I^*T_{\rm per}J_Fv\). Thus its lift is exactly
\[
Q(t)=J_F-IH_F^{-1}I^*T_{\rm per}J_F,
\]
and its Gram is the FC21 Schur complement \(K(t)\). Direct substitution proves \(\pi Q=\pi J_F\), \(I^*T_{\rm per}Q=0\). A nonzero quotient vector cannot have zero minimum, since its lift does not belong to \(I(F)\) and \(T_{\rm per}>0\); hence \(K(t)>0\).

Changing \(J_F\) to \(J_F+IB_0\) adds \(IB_0\) both to the first term and to the subtracted term of \(Q\); therefore \(Q,K\) remain unchanged. Changing to \(J_FD_0\) gives \(Q\mapsto QD_0\), \(K\mapsto D_0^*KD_0\). Block elimination of \(C^*T_{\rm per}C\), with determinant-one triangular elimination matrices, has diagonal blocks \(H_F,K\). Therefore
\[
\det H_F\,\det K=\det(C^*T_{\rm per}C)
=|\det C|^2|\det\Pi|^2.
\]
This proves FC22 and agrees exactly with the complete parent compensation proof read for this audit.

The original ray frame gives
\[
\det\Pi(t)=\det\Pi_{\rm mon}(u)
\exp\!\left(\operatorname{Tr}\Phi_t(A+tR)/u\right),
\qquad |\det\Pi_{\rm mon}(u)|^2=(2\pi|u|)^q.
\]
SC6a–SC6b retains every factor in the evaluated constant. With \(d=q+1\), the original root-of-unity matrix contributes \(d^{q+1}\), the squared radial column factors contribute \((d|u|)^q/d^{2q}\), and the stated gamma multiplication identity gives \((\prod_{l=1}^{d-1}\Gamma(l/d))^2=(2\pi)^q/d\). The full exponent of \(d\) is \((q+1)+q-2q-1=0\). The original complex phase remains in \(\det\Pi_{\rm mon}\). Its squared modulus here is precisely the determinant of the pulled-back positive period Gram.

The logarithm of \(|\det\Pi(t)|^2\) is its retained real constant plus twice the real part of a holomorphic polynomial expression in \(t\); its mixed derivative is zero. Since \(C\) is constant, differentiating the exact product relation proves
\[
\partial_{\bar t}\partial_t\log\det K(t)
=-\frac{|t|^2}{|u|^2}\mathfrak c_F(T_{\rm per}(t)).
\]
Thus FC23 has exactly the opposite sign to the constituent curvature. The coefficient is strictly positive, including at zero, by Section 5. Both actual curvatures vanish at \(t=0\) through the retained \(|t|^2\).

Entries of \(\Pi\) have convergent power series; the positive determinant makes the inverse Gram entries and \(\mathfrak c_F(T_{\rm per})\) real analytic. Applying \(\partial_t\partial_{\bar t}\) at zero to \(t\bar t\,\mathfrak c_F(T_{\rm per}(t))/|u|^2\) gives \(\mathfrak c_F(T_{\rm per}(0))/|u|^2\). Hence the fourth mixed derivatives have the stated opposite values, and their \(t^2\bar t^2\) Taylor coefficients are divided by \(2!2!=4\).

Applying the same quotient minimum to \(\alpha G\preceq H\preceq\beta G\) proves \(\alpha K_G\preceq K_H\preceq\beta K_G\). The literal endomorphism \(K_G^{-1}K(t)\) satisfies \(K_G(K_G^{-1}K(t))=K(t)>0\), so it is \(K_G\)-self-adjoint and positive. Its determinant is \(\det K(t)/\det K_G\), with \(K_G\) independent of \(t\); its log-determinant curvature is consequently FC23. This proves the actual original-quotient morphism together with its finite sampling estimate.

## 9. FC24–FC29: exact commutator allowance and original-space covariance

This later appendix was read in its entirety in the final source diff and independently checked. Retain \(\mathcal C=G^{-1}H=I+B\), a positive \(G\)-self-adjoint operator with spectrum in \([\alpha,\beta]\). The constant quotient frame \(C=[I,J_F]\) is a different, unchanged object. Since \(X_G=T_t^{\dagger_G}+T_t\), subtracting \(\mathcal CX_G\) from FC15 gives
\[
\mathcal C(X_H-X_G)
=T_t^{\dagger_G}B+BT_t-B(T_t^{\dagger_G}+T_t)
=[T_t^{\dagger_G},B].
\]
The inverse of \(\mathcal C\) exists because \(\alpha>0\); this proves FC24 with its ordered commutator.

The positive \(G\)-self-adjoint square root \(\mathcal S=\mathcal C^{1/2}\) is constructed from the actual spectral projections of \(\mathcal C\) and their positive eigenvalue square roots. For uniqueness, any positive square root commutes with its square, hence preserves each eigenspace of \(\mathcal C\). On an eigenspace with eigenvalue \(\lambda>0\), its positive eigenvalues must all equal \(\sqrt\lambda\); self-adjointness then makes its restriction \(\sqrt\lambda I\). Thus the root is unique. It satisfies
\[
\mathcal S^*G\mathcal S=G\mathcal S^2=G\mathcal C=H.
\]
Consequently \(\mathcal S:(E,H)\to(E,G)\) is the exact onto isometry, with inverse \(\mathcal S^{-1}\). This supplies the complete map between the two original metrics.

Multiplying the exact expression
\[
X_H=\mathcal C^{-1}T_t^{\dagger_G}\mathcal C+T_t
\]
on the two sides by \(\mathcal S,\mathcal S^{-1}\) gives
\[
Y_H=\mathcal S X_H\mathcal S^{-1}
=\mathcal S^{-1}T_t^{\dagger_G}\mathcal S
+\mathcal S T_t\mathcal S^{-1}.
\]
For \(Z=[\mathcal S,T_t]\mathcal S^{-1}\), taking the \(G\)-adjoint gives \(Z^{\dagger_G}=\mathcal S^{-1}[T_t^{\dagger_G},\mathcal S]\). Expanding both ordered terms proves \(Y_H-X_G=Z+Z^{\dagger_G}\), FC25. The proved isometry implies \(\|Y_H\|_G=\epsilon_H\). The reverse triangle inequality and invariance of the induced norm under adjoint prove
\[
|\epsilon_H-\epsilon_G|
\le\|Z+Z^{\dagger_G}\|_G
\le2\|[\mathcal S,T_t]\mathcal S^{-1}\|_G.
\]
This is FC26.

The actual commutator \(Y=[\mathcal S,T_t]\) obeys
\[
\mathcal SY+Y\mathcal S
=[\mathcal S^2,T_t]=[\mathcal C,T_t]=[B,T_t].
\]
Its claimed integral is absolutely convergent in the original \(G\)-operator norm, because \(\|\exp(-r\mathcal S)\|_G\le e^{-r\sqrt\alpha}\). Let \(V(r)=e^{-r\mathcal S}[B,T_t]e^{-r\mathcal S}\). Then \(V'(r)=-\mathcal SV(r)-V(r)\mathcal S\), and \(V(0)=[B,T_t]\), \(V(r)\to0\). Integration therefore proves that \(\int_0^\infty V(r)dr\) solves this exact Sylvester equation. For uniqueness, multiply a homogeneous solution on the left and right by any two spectral projections of \(\mathcal S\). The resulting block is multiplied by the positive sum of the corresponding eigenvalues; it must vanish. Thus the integral is the original commutator, establishing FC27, not merely a separately chosen solution.

The same convergent integral gives
\[
\|[\mathcal S,T_t]\|_G
\le\frac{\|[B,T_t]\|_G}{2\sqrt\alpha},\qquad
\|\mathcal S^{-1}\|_G\le\alpha^{-1/2}.
\]
The factor \(2\) in FC26 cancels the factor \(2\) in this denominator, proving
\[
|\epsilon_H-\epsilon_G|
\le\|Z+Z^{\dagger_G}\|_G
\le\alpha^{-1}\|[B,T_t]\|_G.
\]
The scalar \(k/2\) commutes with every operator, so
\[
[B,T_t]=[B,A]+t[B,R],\qquad
[B,R]v=(Be_0)\ell(v)-e_0\ell(Bv).
\]
These prove FC28 with both original residue terms and its exact \(\alpha^{-1}\). Since \(\epsilon_G\le\epsilon_H+\|Z+Z^{\dagger_G}\|_G\), the actual \(e_{\rm comm}\) of FC29 is another valid radius in FC18. The minimum of this radius and the earlier proved radius still bounds \(\epsilon_G\), because each separately does.

If \([B,T_t]=0\), taking its \(G\)-adjoint gives \([T_t^{\dagger_G},B]=0\); FC24 gives \(X_H=X_G\). Sylvester uniqueness gives \([\mathcal S,T_t]=0\), whence \(Z=0\), \(Y_H=X_G\), and \(\epsilon_H=\epsilon_G\). These are exact equalities, not an error estimate with a discarded term.

Finally let \(U:E'\to E\) be any invertible coordinate map, with \(G'=U^*GU\), \(H'=U^*HU\), \(T_t'=U^{-1}T_tU\), and \(B'=U^{-1}BU\). The map \(U\) is an exact isometry between the corresponding coordinate presentations. The operator \(U^{-1}\mathcal SU\) is positive and self-adjoint for \(G'\), and its square is \(G'^{-1}H'\), so uniqueness gives \(\mathcal S'=U^{-1}\mathcal SU\). Every commutator and every exponential-integral factor then transforms by the same similarity. The induced norms are preserved by the displayed isometry. This proves the final covariance claim with the full metrics retained. The source realization uses its fixed integer \(k\ge1\); the purely finite matrix calculations remain valid for real scalar \(k\).

## 10. Review closure and retained LC proof

The finite-sampling, residue-coefficient, endpoint, generator-dependent control, original-metric parabola, finite boundary, quotient-compensation, and exact commutator formulas are accepted in their stated domains. All FC1–FC29, FC3a, and the sharpened FC13 are explicitly included in this acceptance. All LC1–LC16 formulas and LC12a are accepted by the complete independent algebraic proof below, including \(q=1\), \(N=q-1\), \(t=0\), and zero-radius cases at their stated uses. The actual LC source hash was rechecked after that peer review.

This is written proof review. It does not certify an interval evaluation of the arithmetic Fourier samples, a Lean theorem, an estimate uniform in packet or tensor degree, or a new endpoint asymptotic. The original P note's inherited \(v_h,w_h\) symbols require the already-supplied explicit intake definitions; no incorrect identity in P19–P64 is identified by this audit.

The following appendix is the complete independently authored LC proof, retained verbatim rather than reduced to an acceptance assertion.


<!-- BEGIN VERBATIM LC PEER PROOF -->

# Independent proof review of LC1–16, including LC12a

Review date: 13 September 2026.

Disposition: **accepted within the stated original reflection-stable source and period construction; no mathematical defect found in LC1–16 or LC12a.** This is a bounded proof review of the complete assigned TeX file. It is not an execution of numerical tests, Lean, a source edit, a PDF inspection, or a remote publication.

## Exact object, scope, and provenance

The complete file read is `work/period_laplacian_control_bridge_20260913.tex`.

Its SHA-256 is `84d884eeceae8ab339b78c29404d86798fcd04b6d40dde1abcff1cc7ed631231`.

Local dependency passages inspected:

1. `work/toda_cv_exact_bridge_20260912.tex`, through TVB.31, in particular the original pairing and reflection hypotheses, tensor primitive TVB.9, original Gram TVB.14, recurrence and rank-two calculation TVB.22–27, and determinant/minor identities TVB.28–30. SHA-256: `97652a43445708c0e6d2a959f45aed8a4f2a7f73f9cd4b6cd57e67b8fedb408e`.
2. `work/sga_constituent_period_curvature_20260913.tex`, with particular attention to SC1–25: the original period equation, invertible period construction, actual source lift, invariant ideal, normal derivative, and curvature convention. SHA-256: `f7cbbb2da3a97722c9f9128602b4de64ad1ab9cfccdbb03e8ee9363321f7de63`.
3. `work/sga_trace_period_NOTE_corrected_20260913.tex`, original arithmetic construction and interfaces (5)–(11), to verify that the source jet map is on the stated test-function domain. SHA-256: `5c0e890a9370f4aeab646aa7c375f5924aec05b60e060f7ede914638d203b2bf`.

An independently delegated bounded algebraic crosscheck of LC13–16 returned acceptance of the projection types, repeated-factor ideal proof, both comparison inequalities, complex derivative signs, retained factor `|t|²`, and exact two-term loss. The calculations below also record those claims directly.

The original reflection-stable source matters for LC3. That identity is not being asserted for an arbitrary unrelated positive Gram or polynomial lacking the retained reflection construction. LC4 onward uses the explicitly fixed positive metric and finite-dimensional operators; the hypotheses inherited at each use remain the ones in the source.

## LC1–3: original control, spectrum, and every determinant boundary

Work in the original increasing-power coordinates on

\[
E=\mathbb C[S]/(\chi),\quad q=\deg\chi\ge1,\quad
A=M_S,\quad G=G_N>0,\quad N\ge q-1,\quad k\in\mathbb R.
\]

The inner product is conjugate-linear in its first argument:
\(\langle v,w\rangle_G=v^*Gw\). The coefficient functional is the literal row \(\ell[P]=[S^{q-1}]\operatorname{rem}_\chi P\); in particular it is nonzero because \(\ell[S^{q-1}]=1\). The column \(e_0=[1]\) is nonzero because a polynomial of degree zero is not in the ideal of a monic polynomial of positive degree.

For \(A_t=A+t e_0\ell\), the matrix
\(W_t=A_t^*G+GA_t-kG\) is Hermitian. Its relative endomorphism \(X_t=G^{-1}W_t\) has the exact property

\[
X_t^*G=W_tG^{-1}G=W_t=GX_t.
\]

Thus it is self-adjoint in this original metric. Its eigenvalues are real, its operator norm is the largest absolute eigenvalue, and the Rayleigh quotient therefore proves
\(-\|X_t\|_GG\preceq W_t\preceq\|X_t\|_GG\). No identification of a form with an endomorphism has omitted a factor of \(G^{-1}\).

Let \(u=b_N\), \(v=b_{N+1}\), \(w=\omega_N\), and \(w_+=\omega_{N+1}\). These symbols in this paragraph are only names for the original columns and positive norms, not replacements of their lengths or coordinates. The source recurrence used in TVB is

\[
S p_j=p_{j+1}+(k/2+i b_j^{\rm rec})p_j-\alpha_jp_{j-1},
\qquad \alpha_j=\omega_j/\omega_{j-1}.
\]

Applying its reduction to \(AK_N+K_NA^*-kK_N\), every adjacent interior pair has coefficient \(1/\omega_j-\alpha_{j+1}/\omega_{j+1}=0\), the real diagonal contribution is \(k-k=0\), and the remaining last pair gives

\[
AK_N+K_NA^*-kK_N=(vu^*+uv^*)/w.
\]

Because \(G=K_N^{-1}\), multiplication by \(G\) on both sides gives precisely

\[
W_0=G(vu^*+uv^*)G/w,\qquad
X_0=(vu^*+uv^*)G/w.
\]

Write \(a=u^*Gu\), \(d_+=v^*Gv\), and \(z_N=u^*Gv\). The original reflection proof TVB.25–26 retains the phase
\(z_N=i\omega_N\psi_N\), with \(\psi_N\in\mathbb R\). One can see that phase without changing any of these original scalar observations: the explicitly transported real-coordinate source columns satisfy \(Eb_j=i^jd_j\); the transformed Gram and \(d_j\) are real, so their original scalar product acquires the factor \(\overline{i^N}i^{N+1}=i\). Therefore

\[
\operatorname{Tr}X_0=(z_N+\overline{z_N})/w=0,
\]

and expansion of the original rank-one products gives

\[
\operatorname{Tr}(X_0^2)
=\frac{z_N^2+\overline{z_N}^{\,2}+2ad_+}{w^2}
=\frac{2(ad_+-|z_N|^2)}{w^2}.
\]

The range lies in \(\operatorname{span}\{u,v\}\), hence the rank is at most two. A self-adjoint rank-at-most-two endomorphism of trace zero either vanishes or has precisely two nonzero eigenvalues of opposite sign. In the latter case writing them \(\lambda,-\lambda\) in the squared-trace equation gives

\[
\|X_0\|_G^2=\lambda^2=(ad_+-|z_N|^2)/w^2.
\]

In the zero case the same equality follows from the same squared trace. This verifies the first equality of LC3, including possible column dependence and zero radius. For \(q=1\) the endomorphism is scalar and trace zero, hence \(X_0=0\); also \(ad_+=|z_N|^2\) identically for two columns in a one-dimensional space.

For the determinant equality, retain \(D_j=\det K_j\), with \(K_{-1}=0\) as a \(q\)-by-\(q\) matrix, and \(D_N>0\). Only \(K_N\) is inverted. The one-column and two-column determinant formulas yield

\[
\begin{aligned}
\frac{D_{N-1}}{D_N}&=1-\frac a w,\\
\frac{D_{N+1}}{D_N}&=1+\frac{d_+}{w_+},\\
\frac{\widetilde D_N}{D_N}
&=\left(1-\frac a w\right)\left(1+\frac{d_+}{w_+}\right)
+\frac{|z_N|^2}{ww_+}.
\end{aligned}
\]

The last plus sign is forced by the mixed negative and positive rank-one updates: their off-diagonal product has a negative sign, and the determinant subtracts that product. Subtracting these exact expressions in the original definition
\(\Delta_N=D_{N+1}+D_{N-1}-D_N-\widetilde D_N\) gives

\[
\frac{\Delta_N}{D_N}=\frac{ad_+-|z_N|^2}{ww_+}.
\]

Multiplication by the actual \(\alpha_{N+1}=w_+/w\) gives the second equality of LC3.

At \(N=q-1\), the columns \(b_0,\ldots,b_{q-2}\) are monic of distinct degrees \(0,\ldots,q-2\), hence independent. Thus \(K_{q-2}\) has rank \(q-1\) and determinant zero. The formulas just proved still invert only \(K_{q-1}\), which is positive because the first \(q\) monic columns form a triangular basis. In particular they entail \(a/\omega_{q-1}=1\) at this boundary without defining an inverse for \(K_{q-2}\). For \(q=1,N=0\), \(K_{-1}\) is the one-by-one zero matrix and its determinant is zero, not an empty determinant of value one.

The positive-minor proof is valid at the same boundary: determinant multilinearity of \(\sum_j b_jb_j^*/\omega_j\) gives the sum over increasing sets of \(q\) distinct column indices, with summand \(|\det[b_j]|^2/\prod_j\omega_j\). In the four determinants defining \(\Delta_N\), terms containing neither of \(N,N+1\) have coefficient \(1+1-1-1=0\), those containing exactly one have coefficient zero, and those containing both have coefficient one. Therefore for \(q\ge2\)

\[
\Delta_N=
\sum_{\substack{J\subseteq\{0,\ldots,N-1\}\\|J|=q-2}}
\frac{|\det[b_j]_{j\in J\cup\{N,N+1\}\text{ increasing}}|^2}
{\omega_N\omega_{N+1}\prod_{j\in J}\omega_j}\ge0.
\]

For \(q=2\), \(J\) can be the empty set and its denominator factor is the empty product one. For \(q=1\), no one-element column set contains both last indices, so \(\Delta_N=0\). All endpoint and repeated-factor cases remain covered.

## LC4–8: the exact companion radius and quadratic deformation

For \(R=e_0\ell\), the adjoint is
\(R^{\dagger_G}=G^{-1}R^*G=G^{-1}\ell^*e_0^*G\). The literal expansion gives

\[
X_t-X_0=tR+\bar t R^{\dagger_G}.
\]

If \(q>1\), \(\ell e_0=0\), so \(R^2=e_0(\ell e_0)\ell=0\). Define the original column and scalar observations

\[
f=G^{-1}\ell^*,\quad a_0=e_0^*Ge_0>0,\quad
b_0=\ell G^{-1}\ell^*>0.
\]

Here \(f^*Gf=b_0\) and \(e_0^*Gf=\overline{\ell e_0}=0\). The positive lengths and orthogonality prove independence. Direct application gives

\[
Re_0=0,\quad Rf=b_0e_0,\quad
R^{\dagger_G}e_0=a_0f,\quad R^{\dagger_G}f=0.
\]

Thus the matrix on the unchanged ordered columns \((e_0,f)\) is exactly

\[
\begin{pmatrix}0&t b_0\\\bar t a_0&0\end{pmatrix},
\]

with Gram \(\operatorname{diag}(a_0,b_0)\). On its \(G\)-orthogonal complement both functionals \(e_0^*G\) and \(f^*G=\ell\) vanish, so both rank-one terms vanish. The two-dimensional characteristic polynomial is \(x^2-|t|^2a_0b_0\), yielding the full eigenvalue list \(\pm|t|\sqrt{a_0b_0}\) and remaining zeros. For \(t=0\) the entire operator is zero. Self-adjointness in the unchanged metric proves

\[
\|X_t-X_0\|_G=|t|\sigma_N,\qquad \sigma_N=\sqrt{a_0b_0}.
\]

If \(q=1\), \(\ell e_0=1\) and \(R=I_E\), so
\(X_t-X_0=(t+\bar t)I_E\). Its exact norm is \(2|\operatorname{Re}t|\), including purely imaginary nonzero \(t\). This proves the separate scalar case in LC7.

The triangle inequality for the same operator norm gives exactly LC7, followed by the self-adjoint Rayleigh-quotient form inequalities proved above. It supplies an upper bound for \(\|X_t\|_G\); it makes no unsupported equality claim for the sum of the two norms.

Multiplication of the original noncommuting sum gives

\[
(A+tR)^2-k(A+tR)-(A^2-kA)
=t(AR+RA-kR)+t^2R^2.
\]

This proves LC8 with both cross terms, its original minus sign, and the scalar \(t^2I_E\) when \(q=1\).

## LC9–11: exact Laplacian identities and the whole numerical range

Write \(B_t=A_t-kI/2\). Since \(k\) is real, \(W_t=B_t^*G+GB_t\) and \(L_t=B_t^2-k^2I/4\). For the first LC9 identity, expansion gives

\[
\begin{aligned}
A_t^*W_t-W_tA_t
&=(A_t^*)^2G+A_t^*GA_t-kA_t^*G\\
&\quad-A_t^*GA_t-GA_t^2+kGA_t\\
&=L_t^*G-GL_t.
\end{aligned}
\]

For the second,

\[
W_tB_t-B_t^*GB_t-k^2G/4
=GB_t^2-k^2G/4=GL_t.
\]

Neither calculation assumes \(G\), \(A_t\), \(W_t\), or their adjoints commute.

For each original \(v\ne0\), let \(z,r,a,b\) have precisely the definitions LC10 and let \(e=E_N(t)\ge0\). Cauchy–Schwarz and the definition of operator norm give

\[
|a+ib|=
\frac{|\langle v,X_tB_tv\rangle_G|}{\|v\|_G^2}
\le\frac{\|X_t\|_G\|B_tv\|_G}{\|v\|_G}
\le er.
\]

The second LC9 identity evaluated on \(v\) gives
\(\operatorname{Re}z=a-r^2-k^2/4\) and \(\operatorname{Im}z=b\). Therefore

\[
\operatorname{Re}z\le er-r^2-k^2/4
=\frac{e^2-k^2}{4}-(r-e/2)^2
\le\frac{e^2-k^2}{4}.
\]

For the second inequality, direct expansion on the original scalars gives

\[
\begin{aligned}
e^2\left(\frac{e^2-k^2}{4}-\operatorname{Re}z\right)
-(\operatorname{Im}z)^2
&=e^4/4-e^2a+e^2r^2-b^2\\
&=(a-e^2/2)^2+(e^2r^2-a^2-b^2)\ge0.
\end{aligned}
\]

The second term is nonnegative by the previous norm inequality. This proves both assertions LC11. In the special case \(e=0\), it yields \(a=b=0\), \(\operatorname{Im}z=0\), and \(\operatorname{Re}z=-r^2-k^2/4\le-k^2/4\); the separate real-part inequality correctly retains this ray. There was no division by \(e\).

If \(L_tv=\lambda v\) for an eigenvector \(v\ne0\), the displayed quotient equals \(\lambda\), proving spectral inclusion. The proof uses no diagonalizability assertion and retains the larger set of quotients for all nonzero original vectors.

## LC12: period congruence and its exact form-to-operator map

The retained period construction gives invertible \(\Pi(u,t)\) for fixed \(u\ne0\). With the exact definitions LC12, direct multiplication proves

\[
\widetilde A_t^*\widetilde G+\widetilde G\widetilde A_t-k\widetilde G
=\Pi^{-*}(A_t^*G+GA_t-kG)\Pi^{-1}=\widetilde W_t,
\]

and \(\widetilde A_t^2-k\widetilde A_t=\Pi L_t\Pi^{-1}=\widetilde L_t\). The relative control transports by similarity:

\[
\widetilde X_t:=\widetilde G^{-1}\widetilde W_t
=\Pi X_t\Pi^{-1},\qquad
\widetilde B_t=\Pi B_t\Pi^{-1}.
\]

For the literal corresponding vector \(x=\Pi v\),

\[
\begin{aligned}
x^*\widetilde Gx&=v^*Gv,\\
x^*\widetilde G\widetilde L_tx&=v^*GL_tv,\\
x^*\widetilde W_tx&=v^*W_tv,\\
\|\widetilde B_tx\|_{\widetilde G}&=\|B_tv\|_G,\\
\langle x,\widetilde X_t\widetilde B_tx\rangle_{\widetilde G}
&=\langle v,X_tB_tv\rangle_G.
\end{aligned}
\]

Surjectivity of \(\Pi\) makes these equalities identities of the complete quotient sets and operator norms, not merely inclusions. Furthermore

\[
\widetilde L_t^*\widetilde G-\widetilde G\widetilde L_t
=\Pi^{-*}(L_t^*G-GL_t)\Pi^{-1}
=\widetilde A_t^*\widetilde W_t-\widetilde W_t\widetilde A_t.
\]

The fixed action and companion term remain
\(\Pi A_t\Pi^{-1}=\Pi A\Pi^{-1}+t\Pi R\Pi^{-1}\). These statements concern the transported metric \(\widetilde G\); the later constituent section explicitly uses the different specified period-coordinate metric \(I_q\) and supplies the comparison between them.

## LC12a: source-domain types, differential sign, and complete primitive

The original tensor complex has factors \(V\xrightarrow{\Theta}\mathscr B\), with \(V\) in degree zero and \(\mathscr B\) in degree one. Its primitive term \(\mathcal C_{\rm prim}\) is the degree \(k-1\) term, and its top term is the degree \(k\) tensor source. The Euler operator is degree zero: its restriction \(D_0\) to \(\mathcal C_{\rm prim}\) and its top restriction \(D^{(k)}\) preserve these respective domains. TVB.9 gives the actual primitive with the sign \((-1)^{i-1}\) at its sole degree-zero factor. Its differential carries the same sign from the preceding \(i-1\) degree-one factors, so the product of these signs is positive and gives the original relation \(\chi(S)=\sum_i h(s_i)Q_i\).

Euler differentiation preserves the original test-function conditions and commutes with \(\Theta\). On a homogeneous simple tensor, the differential at factor \(i\) is multiplied by \((-1)^{\sum_{j<i}\deg x_j}\); the Euler operator changes none of those degrees. The same-factor commutator vanishes by \(D\Theta=\Theta D\), and different-factor operations commute. Thus every term agrees with its counterpart with the same sign, proving the actual typed identity

\[
D^{(k)}d=dD_0:
\mathcal C_{\rm prim}\longrightarrow\mathcal C^k.
\]

The jet observation annihilates the original boundaries, \(j_Ed=0\), and its stated source domain includes the original Euler-stable test-function domain; it is not restricted to the finite-dimensional image of one lift \(r_N\). Consequently applying the degree-zero source action a second time is defined on the actual images appearing here. The finite-rank term takes its values in that same domain via \(r_N:E\to\mathcal C^k\).

Let \(K=K_N^{\rm prim}:E\to\mathcal C_{\rm prim}\). The original relations are

\[
j_Er_N=I_E,\quad
j_ED^{(k)}=Aj_E,\quad
D^{(k)}r_N-r_NA=dK.
\]

For \(D_t^{(k)}=D^{(k)}+t r_NRj_E\), insertion of \(j_Er_N=I_E\) proves

\[
D_t^{(k)}r_N=r_N(A+tR)+dK=r_NA_t+dK.
\]

Also, insertion of \(j_Ed=0\) gives
\(D_t^{(k)}d=D^{(k)}d+t r_NRj_Ed=dD_0\).
Now both compositions in the square are fully typed, and direct expansion gives

\[
\begin{aligned}
(D_t^{(k)})^2r_N
&=D_t^{(k)}(r_NA_t)+D_t^{(k)}dK\\
&=(r_NA_t+dK)A_t+dD_0K\\
&=r_NA_t^2+d(KA_t+D_0K).
\end{aligned}
\]

Subtracting exactly \(kD_t^{(k)}r_N=kr_NA_t+kdK\) gives

\[
\bigl((D_t^{(k)})^2-kD_t^{(k)}\bigr)r_N-r_NL_t
=d(D_0K+KA_t-kK).
\]

This is LC12a. Each of \(D_0K\), \(KA_t\), and \(kK\) maps \(E\) into \(\mathcal C_{\rm prim}\). The expansion of \(KA_t\) includes \(tKR\), so no deformation contribution has been dropped. The primitive is the original \(K\), with its original differential and source action; the calculation requires neither a new primitive choice nor a change of coordinates. At \(q=1\), the quadratic companion term in \(L_t\) remains present inside \(A_t^2\); the proof did not use \(R^2=0\).

## LC13: projection types and strict positivity for every proper constituent

Let \(I:F\hookrightarrow E\) have matrix size \(q\times p\), with \(0<p<q\) and \(AI=IA_F\). Set \(G_F=I^*GI\), \(P_F=IG_F^{-1}I^*G\), and \(L=\ell I\). Injectivity gives \(G_F>0\). Direct multiplication gives

\[
P_F^2=P_F,\quad P_FI=I,\quad P_F^*G=GP_F.
\]

Since its image is contained in \(I(F)\) and it fixes \(I(F)\), this is exactly the original \(G\)-orthogonal projection. Orthogonality therefore gives

\[
\begin{aligned}
a_\perp&=e_0^*G(1-P_F)e_0=\|(1-P_F)e_0\|_G^2,\\
\|P_Ff\|_G^2
&=f^*GP_Ff
=\ell IG_F^{-1}I^*\ell^*=b_F.
\end{aligned}
\]

The image \(I(F)\) is invariant under every polynomial in \(A\), hence under multiplication by every element of \(E\). Thus it is an ideal. Its inverse image in \(\mathbb C[S]\) is an ideal containing \((\chi)\), so it is generated by a unique monic divisor \(g\) of \(\chi\). Write \(\chi=gh\). The map

\[
\mathbb C[S]/(h)\longrightarrow I(F),\qquad[a]_h\longmapsto[ga]_\chi
\]

is well-defined because \(g(ha)=\chi a\), onto by the ideal description, and injective because \(gh\mid ga\) implies \(h\mid a\) in the polynomial domain. Its dimensions give \(\deg h=p\), and its increasing-power basis gives the original image basis \([g],[Sg],\ldots,[S^{p-1}g]\). Since \(g\) is monic of degree \(q-p\), the last column is monic of degree \(q-1\) and is unchanged by remainder reduction. Applying \(\ell\) gives one, so \(L\ne0\) and \(b_F>0\) by positivity of \(G_F^{-1}\).

If \(e_0\) belonged to the ideal \(I(F)\), multiplication by every element would put all of \(E\) in it, contradicting \(p<q\). Therefore \((1-P_F)e_0\ne0\), proving \(a_\perp>0\). No step removes or weakens any repeated factor of \(g\), \(h\), or \(\chi\).

## LC14: the original metric compared with the coordinate period metric

Put \(Q(t)=\Pi(t)^*\Pi(t)>0\). The comparison endomorphism \(B(t)=G^{-1}Q(t)\) satisfies

\[
B(t)^*G=Q(t)=GB(t),\qquad
\langle v,B(t)v\rangle_G=\|\Pi(t)v\|_{I_q}^2>0\quad(v\ne0).
\]

The finite spectral theorem for this same \(G\)-inner product gives positive finite extremal eigenvalues \(m(t),M(t)\). Expansion in a \(G\)-orthogonal eigenbasis, retaining all original eigenvalues, proves
\(m(t)G\preceq Q(t)\preceq M(t)G\). No replacement of either metric is used to define the observations below.

For \(Y=\Pi I\), \(H_F=Y^*Y>0\), and \(P^{\rm per}=YH_F^{-1}Y^*\), the same multiplication as above, now in \(I_q\), makes \(P^{\rm per}\) the orthogonal projection onto \(Y(F)\). Consequently its residual \(z=(1-P^{\rm per})\Pi e_0\) satisfies

\[
\|z\|_{I_q}^2=\min_{x\in F}\|\Pi(e_0-Ix)\|_{I_q}^2.
\]

The original-metric squared norm has the explicit completion

\[
\|e_0-Ix\|_G^2
=a_\perp+(x-x_0)^*G_F(x-x_0),\qquad
x_0=G_F^{-1}I^*Ge_0.
\]

For every \(x\) the lower comparison bound is at least \(m(t)a_\perp\); taking its minimum gives the first lower bound. Evaluating the upper comparison at \(x_0\) gives the first upper bound. Hence

\[
m(t)a_\perp\le\|z\|_{I_q}^2\le M(t)a_\perp.
\]

Compression by \(I\) gives
\(m(t)G_F\preceq H_F\preceq M(t)G_F\). To verify inverse order with all scalar factors, for positive \(T\) and arbitrary column \(w\), the exact square completion is

\[
2\operatorname{Re}(w^*x)-x^*Tx
=w^*T^{-1}w-(x-T^{-1}w)^*T(x-T^{-1}w).
\]

Thus its maximum over \(x\) is \(w^*T^{-1}w\), and a larger positive \(T\) gives a smaller maximum. Applied to the three displayed forms this proves

\[
M(t)^{-1}G_F^{-1}\preceq H_F^{-1}\preceq m(t)^{-1}G_F^{-1}.
\]

Evaluating on the unchanged column \(w=L^*\) proves
\(b_F/M(t)\le LH_F^{-1}L^*\le b_F/m(t)\). This proves both LC14 pairs without a commutation hypothesis.

## LC15: holomorphic derivative, retained sign, and exact curvature

The original SC4 period equation is \(\Pi'=-\Pi(A+tR)/u\). Its sign is consistent with differentiating the exponential \(e^{\Phi_t/u}\), because \(\partial_t\Phi_t=-S\). For the last column, integration by parts gives the reduction \(S^q\equiv-\sum_{a<q}c_aS^a+t\), so its companion entry is \(+tR\); the two signs are both retained. Hence \(AI=IA_F\) and \(RI=e_0L\) give

\[
Y'=-YA_F/u-t\Pi e_0L/u,\qquad
(1-P^{\rm per})Y'=-tzL/u.
\]

With \(H=H_F=Y^*Y\), holomorphy gives

\[
\partial_tH=Y^*Y',\quad
\partial_{\bar t}H=Y'^*Y,\quad
\partial_{\bar t}\partial_tH=Y'^*Y',\quad
\partial_{\bar t}H^{-1}=-H^{-1}Y'^*YH^{-1}.
\]

The positive determinant uses the real logarithm. Differentiating its determinant derivative and retaining product order proves

\[
\begin{aligned}
\partial_{\bar t}\partial_t\log\det H
&=\operatorname{Tr}\bigl(H^{-1}Y'^*Y'
-H^{-1}Y'^*YH^{-1}Y^*Y'\bigr)\\
&=\operatorname{Tr}\bigl(H^{-1}Y'^*(1-P^{\rm per})Y'\bigr).
\end{aligned}
\]

Because \(1-P^{\rm per}\) is self-adjoint and idempotent, substitution of the exact normal derivative gives

\[
Y'^*(1-P^{\rm per})Y'
=\frac{|t|^2\|z\|_{I_q}^2}{|u|^2}L^*L.
\]

Taking the trace yields

\[
\partial_{\bar t}\partial_t\log\det H_F
=|t|^2c_F(t),\qquad
c_F(t)=\frac{\|z\|_{I_q}^2}{|u|^2}LH_F^{-1}L^*.
\]

The negative sign in each normal factor multiplies its conjugate, producing the displayed positive expression. The nonzero denominator is the original \(|u|^2\), and the derivative convention is the original Wirtinger one; there is no additional real-Laplacian factor of four in this displayed mixed derivative.

Both factors in LC14 are strictly positive. Multiplying their two lower bounds, and separately their two upper bounds, gives exactly

\[
\frac{m(t)}{M(t)}\frac{a_\perp b_F}{|u|^2}
\le c_F(t)\le
\frac{M(t)}{m(t)}\frac{a_\perp b_F}{|u|^2}.
\]

At \(t=0\), \(c_F(0)>0\), while the actual curvature is zero because its expression retains the factor \(|t|^2\). Thus the proof does not confuse a positive coefficient with a nonzero curvature at the stationary parameter.

## LC16: exact loss and final radius comparison

The original projection gives two orthogonal decompositions, with no terms omitted:

\[
a_0=\|P_Fe_0\|_G^2+a_\perp,\qquad
b_0=b_F+\|(1-P_F)f\|_G^2.
\]

Multiplying the first equality by the whole original \(b_0\) and subtracting \(a_\perp b_F\) gives

\[
\begin{aligned}
\sigma_N^2-a_\perp b_F
&=\|P_Fe_0\|_G^2b_0+a_\perp(b_0-b_F)\\
&=\|P_Fe_0\|_G^2b_0
+a_\perp\|(1-P_F)G^{-1}\ell^*\|_G^2\ge0.
\end{aligned}
\]

This verifies the stated exact two-term loss; the first term retains the full \(b_0\), including its complement contribution. Combining it with LC15 gives

\[
c_F(t)\le\frac{M(t)}{m(t)}\frac{\sigma_N^2}{|u|^2}.
\]

Since a proper nonzero constituent has \(q>1\), the applicable exact companion norm is precisely
\(\|X_t-X_0\|_G^2=|t|^2\sigma_N^2\). Multiplication by the retained \(|t|^2\) proves the final assertion

\[
\partial_{\bar t}\partial_t\log\det H_F(t)
\le\frac{M(t)}{m(t)}\frac{\|X_t-X_0\|_G^2}{|u|^2}.
\]

Both sides vanish at \(t=0\). The cases \(q=1\), \(F=0\), and \(F=E\) are not improperly included in the strictly positive proper-constituent statement: LC13 explicitly assumes \(0<p<q\), and the earlier scalar companion calculation handles \(q=1\).

## Review closure

All original metric factors, conjugations, source types, polynomial cross terms, reflection phase, determinant signs, and stationary-parameter factors needed for LC1–16 and LC12a have been checked in the calculations above. No claim of a uniform bound on \(\epsilon_N\), \(\sigma_N\), or \(M(t)/m(t)\) has been added. No concrete defect was found. The assigned mathematical source was not edited, and no numerical, Lean, or remote action was performed.

<!-- END VERBATIM LC PEER PROOF -->
