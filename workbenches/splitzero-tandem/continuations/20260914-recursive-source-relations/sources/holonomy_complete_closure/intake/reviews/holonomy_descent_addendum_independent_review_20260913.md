# Independent full proof review of HDI1–HDI24

Review date: 2026-09-13. This report audits the complete file
workspace:/work/holonomy_descent_typed_addendum_20260913.tex,
lines 1–410, at final SHA256
9ef47bf6aa55cb2ef79d687190ada3b051c968c106ce43ad4ecfbe960fb578ce.
Every numbered equation HDI1–HDI24 was read. The original H packet, source maps, coordinates, measures, and constants remain those pinned in the accompanying full review:
workspace:/work/holonomy_descent_independent_proof_review_20260913.md.
That review's corrected sealed SHA256 is
695fe1351e9d4712971a4151bfea705c216788828c89a087bfd0af7e18beb9ad.

The selected source dependency was also read through PSD22, including the pointwise PSD16 proof, in
workspace:/work/periodized_source_density_review_20260913.tex,
SHA256 51102189bcc7a45610464143a5c0bee21c08059c317024e6e856bc7de993fe74.
The remaining density and completion steps are proved independently below. This is a finite proof review, not a new survey of the primary corpus.

All formulas and their mathematical claims in HDI1–HDI24 are accepted at the final pin above. The complete first version was read at SHA256 e4dfa835d3cb48d9f8e9e6a1ee6ed142edf9a684ba446139964daec2a66fae8d. The author then applied the review's sole required wording correction at source lines 21–24; that corrected block was read again and the final hash checked. When the relation dimension is zero, an expression factoring through the zero relation space is zero on its stated domain and codomain; those outer spaces need not themselves be zero-dimensional. For example, the Schur correction is the zero map \(E\to E\). The final source now states:

> For \(r=0\), the relation metric and its inverse are the unique automorphism of \(\{0\}\); every correction factoring through \(B\) is the zero map on its stated domain and codomain. For \(r>0\), \(M_B\succ0\).

No raw source or current addendum was edited in this review.

Two harmless notational readings are made explicit in the proof below. In HDI19, the symbol used for the source isometry denotes a map from the positive-support sequence space, while HDI11 uses the same glyph for its index set; the Fourier sequence is extended by zero outside that set. The relative eigenvalues \(1\pm\eta\) after HDI23 are those of \(M^{-1}M_\theta\); the off-diagonal perturbation itself has eigenvalues \(\pm\eta\). Neither reading changes a map, constant, or numbered formula.

## 1. Exact metric compressions and the selected inverse strip

Let the original finite polynomial space be \(\mathcal P_N\), with positive Gram \(M=\Psi^*\Psi\), quotient \(J:\mathcal P_N\twoheadrightarrow E\), and literal relation inclusion \(B:\mathbb C^r\hookrightarrow\mathcal P_N\) onto \(\ker J\). Put
\[
G=(JM^{-1}J^*)^{-1},\qquad C=M^{-1}J^*G,\qquad M_B=B^*MB.
\]
The matrix \(JM^{-1}J^*\) is positive because \(J^*\) is injective. Thus \(G\) exists and is positive. Direct multiplication gives \(JC=I\), \(C^*MC=G\), and \(B^*MC=B^*J^*G=0\).
The dimensions of \(\operatorname{im}C\) and \(\operatorname{im}B\) sum to \(\dim\mathcal P_N\). These maps therefore give the exact orthogonal decomposition with its original metrics
\[
U:(E,G)\oplus(\mathbb C^r,M_B)\longrightarrow(\mathcal P_N,M),
\qquad U(x,y)=Cx+By.
\]
Its inverse is \(p\mapsto(Jp,M_B^{-1}B^*Mp)\). In particular,
\[
C^\dagger=G^{-1}C^*M=J,\qquad
B^\dagger=M_B^{-1}B^*M
\]
are the actual metric adjoints. This proves HDI1 and HDI5, including the domains of each compression.

For \(v>0\), the original correlation pairing has the exact weighted factorization
\[
\int_{\mathbb R}
\langle\Psi(r)x,\Psi(r+v)y\rangle_{\mathcal K}\,dr
=e^{-av}\int_{\mathbb R}
\langle e^{-ar}\Psi(r)x,e^{a(r+v)}\Psi(r+v)y\rangle_{\mathcal K}\,dr.
\]
Translation in the second squared integral gives the unchanged forms \(M_{a,-}\) and \(M_{a,+}\). Cauchy–Schwarz therefore bounds the absolute value by
\[
e^{-av}\sqrt{x^*M_{a,-}x}\sqrt{y^*M_{a,+}y}
\le K_a e^{-av}\|x\|_M\|y\|_M.
\]
For \(v<0\), use the opposite signs; the same product \(K_a=\sqrt{\kappa_+\kappa_-}\) results. Taking the dual norm in the same metric \(M\) proves HDI3. The factors \(e^{\pm2ar}\) are \(x_k^{\pm2a}\) in the unchanged original coordinates.

Since \(\mathcal C(0)=M\), for \(|\operatorname{Im}z|\le s<aL\) the nonzero terms in the correlation series have total norm at most
\[
K_a\sum_{n\ne0}e^{-(aL-s)|n|}
=\frac{2K_a}{e^{aL-s}-1}=d_s.
\]
Multiplication by any fixed power of \(|n|\) preserves convergence on smaller closed strips. The series and derivative series thus converge normally on \(|\operatorname{Im}z|<aL\), proving the holomorphic periodic extension and HDI4.

Choose the stated \(0<s<aL\) with \(d_s<1\), and put \(T=M^{-1}(\widetilde M-M)\). Since \(B,C\) and their metric adjoints have norm one on their nonzero spaces, the four blocks
\[
T_{11}=C^\dagger TC,\quad T_{12}=C^\dagger TB,\quad
T_{21}=B^\dagger TC,\quad T_{22}=B^\dagger TB
\]
have norms at most \(d_s\) in their stated metrics. The exact relation block is
\[
B^*\widetilde MB=M_B(I+T_{22}).
\]
The Neumann series for \(I+T_{22}\) converges in operator norm and its inverse norm is at most \((1-d_s)^{-1}\). The strict inequality persists at some \(s'>s\) with \(s'<aL\); hence the inverse is holomorphic in a neighborhood of the closed contour strip. This proves the precise HDI6 domain, rather than asserting inverse existence everywhere on the larger correlation strip.

The Schur complement is
\[
\widetilde G=C^*\widetilde MC
-C^*\widetilde MB(B^*\widetilde MB)^{-1}B^*\widetilde MC.
\]
In the retained \(G\)-metric its exact expression is
\[
G^{-1}\widetilde G
=I+T_{11}-T_{12}(I+T_{22})^{-1}T_{21}.
\]
Thus its norm is at most
\[
1+d_s+\frac{d_s^2}{1-d_s}=\frac1{1-d_s},
\]
which is HDI7. On the real axis, \(M_\theta\) is positive, since the bound on the relative perturbation is below one. The section
\[
C_\theta=C-B(B^*M_\theta B)^{-1}B^*M_\theta C
\]
satisfies \(JC_\theta=I\) and \(B^*M_\theta C_\theta=0\). Every other section representative of \(x\in E\) is \(C_\theta x+By\), whose squared norm is
\[
x^*C_\theta^*M_\theta C_\theta x+y^*B^*M_\theta By.
\]
The unique minimum occurs at \(y=0\), and its Gram is the same Schur complement. This also proves the real quotient interpretation without changing \(J\) or the source section.

The displayed complex extension is holomorphic and involves no conjugation of \(z\). Its section difference from \(C\) still factors through the original \(B\). Consequently applying the inherited source comparison to that section still gives the same arithmetic map \(\eta:E\to H^1(\mathcal C_h)^{\otimes k}\), with every original relation primitive retained.

## 2. Fourier tails and the finite budget

The convention is
\[
\widehat G_n=\frac1{2\pi}\int_0^{2\pi}
e^{-in\theta}\widetilde G(\theta)\,d\theta.
\]
For \(n>0\), move the contour to imaginary part \(-s\), where the modulus of the exponential is \(e^{-ns}\). For \(n<0\), move it to imaginary part \(+s\), where its modulus is \(e^{-s|n|}\). Periodicity cancels both vertical sides, and the already proved neighborhood of holomorphy permits the contour. HDI7 gives
\[
\|G^{-1}\widehat G_n\|_G
\le (1-d_s)^{-1}e^{-s|n|}.
\]
The geometric bound proves absolute uniform convergence of the Fourier series on the real axis. Averaging at \(2\pi j/m\) keeps exactly the indices divisible by \(m\). Subtracting the continuous mean removes the zero coefficient, so the error is at most
\[
\frac1{1-d_s}\sum_{\ell\ne0}e^{-sm|\ell|}
=\frac{2}{(1-d_s)(e^{sm}-1)}.
\]
Both Fourier directions and both nonzero tails are present. This proves HDI8.

For the actual choices in HDI9,
\[
aL\ge s_0+\log(1+2K_a/d_0),\qquad
aL\ge\log(1+\kappa/\eta_0).
\]
The weighted source forms are positive, so \(K_a>0\) and \(aL>s_0\). Rearranging these two inequalities gives \(d_{s_0}\le d_0<1\) and \(\delta_L\le\eta_0<1\), respectively. The chosen positive integer \(m\) satisfies
\[
e^{s_0m}-1\ge\frac{2}{(1-d_0)\varepsilon_0}.
\]
Hence the quadrature error is at most \(\varepsilon_0\) in the \(G\)-relative norm. Because the error matrix is Hermitian, this is equivalent to a two-sided error bounded by \(\varepsilon_0G\). The already proved full-mean theorem gives
\[
(1-\eta_0^2)G\preceq\overline G\preceq G.
\]
Adding and subtracting the quadrature error gives exactly HDI10,
\[
(1-\eta_0^2-\varepsilon_0)G
\preceq\frac1m\sum_{j=0}^{m-1}G_{2\pi j/m}
\preceq(1+\varepsilon_0)G.
\]
Its lower factor is strictly positive by the specified \(\varepsilon_0<1-\eta_0^2\). No growth estimate for the arithmetic weighted forms is implied by these finite formulas.

## 3. Positive masses and density with the full shifted coordinate

Keep
\[
u_n=(2\pi n+\theta)/L,\qquad
S_n=k/2+iu_n,\qquad
\nu_n=(2\pi/L)m_{h,k}(u_n).
\]
The pointwise PSD14 estimate, with the actual \(w_h=(2\pi)^{-1}|g/h|^2\), proves
\[
m_{h,k}(u)\le A_b B_b^{k-1}e^{-b|u|}
\qquad(0<b<\pi/2).
\]
The source density \(w_h\) is continuous and positive off a discrete set, since \(g/h\) is a nonzero entire function. For any \(u\), the union of its zero set and the reflected zero set has a complement. A point in that complement has a neighborhood on which \(w_h(t)w_h(u-t)>0\). Its integral is positive. Convolving an everywhere positive continuous function with \(w_h\), which is positive on an interval, proves positivity for every \(k\ge2\).

For \(k=1\), retain \(I_\theta=\{n:\nu_n>0\}\). At a selected root \(\rho\) of full order \(d_\rho\) in both \(g\) and \(h\), the literal Taylor factors give
\[
(g/h)(\rho)=
\frac{g^{(d_\rho)}(\rho)}{h^{(d_\rho)}(\rho)}\ne0.
\]
If \(h=a_h\prod_\sigma(S-\sigma)^{d_\sigma}\), then
\[
h^{(d_\rho)}(\rho)
=a_h d_\rho!\prod_{\sigma\ne\rho}(\rho-\sigma)^{d_\sigma}.
\]
This retains the leading coefficient. The cyclic minimal polynomial generates the ideal \((h)\); it equals \(h\) in the original monic convention. Thus every sampled root of \(\chi_{h,1}\) has precisely the positive mass
\[
\nu_n=\frac1L
\left|\frac{g^{(d_\rho)}(\rho)}{h^{(d_\rho)}(\rho)}\right|^2>0,
\]
including the original \(g=2\xi\). This proves HDI11–HDI14.

For completeness the exponential lattice moment follows with all constants retained. Put \(C_b=A_bB_b^{k-1}\). For \(0<c<b\), since \(0\le\theta<2\pi\),
\[
\sum_{n\in\mathbb Z}e^{c|u_n|}\nu_n
\le\frac{2\pi C_b}{L}
\frac{e^{-(b-c)\theta/L}
+e^{-(b-c)(2\pi-\theta)/L}}
{1-e^{-2\pi(b-c)/L}}<\infty.
\]
This is the sum of the \(n\ge0\) and \(n\le-1\) geometric tails. A fixed factor \(|\chi(S_n)|^2\) is absorbed by using two exponents \(c<b'<b\), since
\(\sup_u|\chi(k/2+iu)|^2e^{-(b'-c)|u|}<\infty\).

For an arbitrary positive submeasure \(\mu_n\) with such an exponential moment, take \(v\in\ell^2(I,\mu)\) orthogonal to every polynomial sequence. If \(0<d<c/2\), then
\[
\sum_I|v_n|\mu_ne^{d|u_n|}
\le\|v\|_\mu
\left(\sum_I\mu_ne^{2d|u_n|}\right)^{1/2}<\infty.
\]
Thus \(F(z)=\sum_I\overline v_n\mu_ne^{izu_n}\) is holomorphic for \(|\operatorname{Im}z|<c/2\), with normal convergence of each derivative series on smaller strips. Orthogonality to the original-coordinate polynomial \(((S-k/2)/i)^j\) makes every derivative at zero vanish. Holomorphic uniqueness gives \(F=0\).

The full phase is retained in the extraction:
\[
\frac1L\int_0^L F(x)e^{-iu_mx}\,dx
=\sum_I\overline v_n\mu_n
\frac1L\int_0^L e^{2\pi i(n-m)x/L}\,dx
=\mathbf1_{m\in I}\overline v_m\mu_m.
\]
Absolute summability permits termwise integration. The common \(\theta/L\) cancels in the difference of the two frequencies, without changing either frequency separately. Every coefficient is zero, so \(v=0\). This proves HDI15–HDI16 and polynomial density both for \(\nu\) on its positive support and for \(|\chi(S_n)|^2\nu_n\) on the complement of the sampled roots.

## 4. Exact completion, source amplitudes, and the almost-everywhere map

Set \(Z_\theta=\{n\in I_\theta:\chi(S_n)=0\}\). Each coordinate functional on \(\mathcal H_\theta=\ell^2(I_\theta,\nu)\) has norm \(\nu_n^{-1/2}\). Therefore the closure of \(\chi\mathbb C[S]\) vanishes on \(Z_\theta\). Conversely, if \(f\) vanishes there, set \(a_n=f_n/\chi(S_n)\) on its complement. Then
\[
\sum_{n\notin Z_\theta}|a_n|^2|\chi(S_n)|^2\nu_n
=\sum_{n\notin Z_\theta}|f_n|^2\nu_n.
\]
Polynomial density in this weighted space supplies \(P_j\to a\); multiplication by \(\chi\) is an isometry to the vanishing-coordinate subspace and gives \(\chi P_j\to f\). The two closed subspaces are therefore equal. Orthogonal restriction to \(Z_\theta\) identifies their quotient with
\[
\mathcal T_\theta=
\left(\mathbb C^{Z_\theta},\sum_{n\in Z_\theta}\nu_n|a_n|^2\right).
\]

The map \(e_\theta:E\to\mathcal T_\theta\), \([P]\mapsto(P(S_n))\), is well-defined. The nodes are distinct, so their Lagrange polynomials prove surjectivity. Vanishing at all of them is equivalent to divisibility by the squarefree polynomial \(p_\theta=\prod_{n\in Z_\theta}(S-S_n)\). Hence its kernel is \((p_\theta)/(\chi)\). Since \(p_\theta\) divides \(\chi\), multiplication by \(p_\theta\) gives the exact map
\[
\mathbb C[S]/(\chi/p_\theta)\longrightarrow E,\qquad
[Q]\longmapsto[p_\theta Q].
\]
If its value is zero, \(\chi\mid p_\theta Q\), and polynomial cancellation implies \(\chi/p_\theta\mid Q\). The map is injective, and its image is exactly the kernel above. This proves HDI17–HDI18, also for an empty sampled-root set and without coprimality. In a repeated-root block \(\mathbb C[\epsilon]/(\epsilon^{d_\rho})\), sampled evaluation retains the constant coefficient; the nilpotent ideal is its kernel. At an unsampled root the full primary block is killed.

For the exact comparison with the original source, define
\[
b_n(\theta)=\widehat{\mathcal U_k F_h^{\otimes k}}(u_n)\in\mathcal K.
\]
The pointwise partial Plancherel identity PSD16 is
\[
\|b_n(\theta)\|_{\mathcal K}^2
=(2\pi)^{-(k-1)}
\int_{\mathbb R^{k-1}}\prod_{j<k}|v_h(1/2+it_j)|^2
\left|v_h\!\left(1/2+i\left(u_n-\sum_{j<k}t_j\right)\right)\right|^2d\mathbf t
=2\pi m_{h,k}(u_n).
\]
The identity is pointwise: the admitted transformed source is regular, both sides have continuous representatives, and the absolutely convergent displayed integral determines the partial transform norm at each \(u_n\).

Use the orthonormal twisted basis \(L^{-1/2}e^{-i(2\pi n+\theta)r/L}\). The map \(I_\theta\) from the positive weighted sequence space is specified by the Fourier coefficients
\[
\widehat{I_\theta a}(n)=L^{-1/2}a_nb_n(\theta).
\]
Parseval gives
\[
\|I_\theta a\|^2
=\sum_{n\in I_\theta}L^{-1}|a_n|^2\|b_n(\theta)\|_{\mathcal K}^2
=\sum_{n\in I_\theta}\nu_n|a_n|^2.
\]
It has a closed range. On that range, taking the inner product with \(b_n(\theta)\), conjugate-linear in the first variable, gives the exact inverse
\[
a_n=\sqrt L\,
\frac{\langle b_n(\theta),\widehat f(n)\rangle_{\mathcal K}}
{\|b_n(\theta)\|_{\mathcal K}^2}.
\]
Every denominator is positive on \(I_\theta\). Unfolding the holonomy sum with its factor \(e^{ia\theta}\) gives the Fourier coefficient \(L^{-1/2}\widehat\Psi(u_n)\): the extra cell factor is \(e^{-i(2\pi n+\theta)a}\), which cancels \(e^{ia\theta}\). For the polynomial source, the plus-sign transform of \(-\partial_r+k/2\) is multiplication by \(S_n\). Thus
\[
I_\theta(P(S_n))
=\mathcal Z_{L,\theta}\mathcal U_k\mathcal V P.
\]
The just-proved polynomial density makes its closed range exactly the closed polynomial source. This proves every factor and both maps in HDI19.

Embed \(\mathcal T_\theta\) into the fixed \(\ell^2(\mathbb Z)\) by multiplying each sampled coordinate by \(\sqrt{\nu_n(\theta)}\) and setting other coordinates to zero. Its range is the diagonal projection \(Q_\theta\) in HDI20. Each diagonal entry is Borel, because its defining \(\nu_n(\theta)\) and \(\chi(S_n(\theta))\) are continuous. Finite-coordinate approximations show strong measurability on every vector, and \(Q_\theta e_n\) give a countable family spanning each range.

A nonzero entry requires a root \(\rho\) of \(\chi\) with
\[
\operatorname{Re}\rho=k/2,\qquad
\theta\equiv L\operatorname{Im}\rho\pmod{2\pi}.
\]
Each root gives at most one phase in the chosen half-open interval. Hence \(Q_\theta=0\) outside a finite set. Its decomposable action on the fixed direct integral is zero because the norm squared is the integral of a function supported on that finite set. The induced section from \([P]\in E\) has the explicit Borel coordinates
\[
\mathbf1_{n\in Z_\theta}\sqrt{\nu_n(\theta)}P(S_n(\theta)).
\]
It has zero norm, proving HDI21 and kernel \(E\). The positive weighted pointwise evaluation maps survive as HDI17–HDI18; taking their almost-everywhere class is the exact additional zero map.

For every original support label, the coefficient maps lift as \((\ell,v)\mapsto(\ell,fv)\), and fix \(\tau\). In particular, the final kernel produces represented zero at the receiving support, not external absence. No reference or support map is discarded.

## 5. The literal mass \(7\) and the exact phase sign in the sharp realization

Choose the displayed nonzero smooth functions with disjoint compact supports in \((0,L)\), and retain
\(\alpha=\int|f_0|^2>0\), \(\beta=\int|g_0|^2>0\).
The explicit coordinate maps \(f=f_0/\sqrt\alpha\), \(g_1=g_0/\sqrt\beta\) give orthonormal functions. The shifted \(f(\cdot-L)\) is supported in \((L,2L)\), so it is orthogonal to both unshifted functions. Consequently
\[
\psi_0=\sqrt7 f,\qquad
\psi_1=\sqrt7(\eta f(\cdot-L)+\sqrt{1-\eta^2}g_1)
\]
have squared norms \(7\) and inner product zero: the real-line Gram is exactly \(7I_2\). Smooth compact support gives all finite exponential weighted norms and derivative moments.

For \(0\le r<L\), unshifted \(f,g_1\) contribute only at cell \(a=0\); the shifted function contributes only at \(a=1\). Therefore the original holonomy transform gives
\[
\mathcal Z_{L,\theta}\psi_0=\sqrt7 f,\qquad
\mathcal Z_{L,\theta}\psi_1
=\sqrt7(\eta e^{i\theta}f+\sqrt{1-\eta^2}g_1).
\]
Using the inner product conjugate-linear in its first variable, the Gram entry \(01\) is \(7\eta e^{i\theta}\) and entry \(10\) is \(7\eta e^{-i\theta}\). Thus HDI23 has precisely the correct signs:
\[
M_\theta=7
\begin{pmatrix}1&\eta e^{i\theta}\\
\eta e^{-i\theta}&1\end{pmatrix}.
\]
The mean is \(7I_2\). The off-diagonal relative perturbation squares to \(\eta^2I_2\), so the relative eigenvalues are \(1-\eta\) and \(1+\eta\), positive for \(0\le\eta<1\).

For \(J=(1\ 0)\) and \(B=(0\ 1)^T\), the unique section of \(J\) orthogonal to \(B\) is
\[
C_\theta=\binom{1}{-\eta e^{-i\theta}},
\qquad
C=\binom10,\qquad C-C_\theta=BX_\theta,\quad
X_\theta=\eta e^{-i\theta}.
\]
Multiplying by the actual \(M_\theta\) gives
\[
M_\theta C_\theta=7\binom{1-\eta^2}{0},\qquad
G_\theta=7(1-\eta^2),\qquad G=7.
\]
The relation metric is \(B^*M_\theta B=7\), so
\[
X_\theta^*B^*M_\theta BX_\theta=7\eta^2,\qquad
\mathscr D=7\eta^2.
\]
This proves HDI22–HDI24 and equality in the full-circle quadratic-loss bound, including the endpoint \(\eta=0\). The functions and the map \(\Psi:\mathbb C^2\to L^2(\mathbb R)\), together with \(J\), completely specify the calibration. No identification with a particular arithmetic packet is asserted or needed for this sharpness statement.

## 6. Coverage and review limits

| Labels | Source range | Disposition |
| --- | --- | --- |
| HDI1–HDI7 | lines 12–105 | Correct metrics, adjoints, inverse domain, and Schur maps; zero-dimensional wording corrected in the final pin. |
| HDI8–HDI10 | lines 106–147 | Correct Fourier contours, both tails, finite choices, and positive lower factor. |
| HDI11–HDI16 | lines 149–234 | Correct full-order root mass and shifted-lattice density with all \(2\pi,L,k,\theta\) factors. |
| HDI17–HDI18 | lines 236–282 | Exact weighted quotient, surjection, kernel, and primary-block maps. |
| HDI19 | lines 284–304 | Exact source isometry and inverse, checked against the pointwise PSD16 identity. |
| HDI20–HDI21 | lines 306–346 | Explicit measurable field, zero direct integral, and preserved pointwise/support maps. |
| HDI22–HDI24 | lines 348–410 | Exact compact-support realization, phase signs, literal mass \(7\), and equality case. |

Independent delegated reviews separately checked the strip/realization block and the source/completion block. No numerical tests, formal checker runs, broad scans, new primary-source searches, or source edits were performed by this reviewer. The sole required correction was applied by the author and verified at the final source pin. No numbered formula requires alteration.
