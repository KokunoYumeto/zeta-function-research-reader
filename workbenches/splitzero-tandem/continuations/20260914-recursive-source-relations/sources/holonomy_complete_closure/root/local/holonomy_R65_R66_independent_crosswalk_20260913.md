# Independent formula crosswalk for R65–R66

The assigned scope is R65 and R66 only. This report compares their formulas and scope with the actual complete HG1–25 and HD1–10 proof bodies, the complete coordinating CR1–14 body including CR12a–c, and the complete independent continuous-completion proof. The comparison is a written calculation. No mathematical suite or Lean run was made, and no source was edited by this reviewer.

The initially supplied current-results source has 9,642 bytes and SHA-256 73c3aeae19c3ac94563bcbb5f91fc75527f02cef7ea9bd8a50c42b2c1b5027a1. The final disposition and current reviewed source pin are recorded in the companion JSON. R63–64 belong to the parent's disjoint review.

The full proof sources actually read are:

- HG: holonomy_generator_control_bridge_20260913.tex, 22,469 bytes, SHA-256 39c67cb2953de52c109831893c347a6ff97639a151f24445d98b357edd7d3282.
- HD: holonomy_degree_cost_20260913.tex, 8,947 bytes, SHA-256 9a1ba6cd7e8bee67c6d7868c74f2cf4f9d8c11fa255d9d278c7a2420cf0daca6.
- CR: period_laplacian/CONTINUOUS_RELATION_COMPLETION.md, 13,776 bytes, SHA-256 37e187b0ae6a258f3123cef8ec09328a1658eb0ffe6727f232bf669730f01467.
- Additional continuous-completion proof: continuous_completion_review/INDEPENDENT_CONTINUOUS_COMPLETION_REVIEW.md, 16,619 bytes, SHA-256 f0a3eb09df7e9daccaac91d69a273eb97fe4be3433b6f6872bd07903d6e8a018.

The holonomy v2 reader-input manifest, SHA-256 b0915e0ebbc920edff73bf853e9be1fee100fd29d28ad05d04084ed0d320a923, explicitly sends HCD/HG/HD/CR external companions to their authors/companion builder; it does not itself seal those parallel sources. Following that route, HCD_CR_READER_DERIVATION.json, SHA-256 9664124916184d9ddc15556e844feee2ff979525220efc449e3c1b541815e9cf, identifies the actual CR Markdown above. CURRENT_REVIEW_PROVENANCE.json identifies the independent completion proof. Their full contents, including the finite singular quotient and projection calculation, were read rather than inferred from a claim receipt. The JSON records the exact absolute source paths.

## R65: exact generator transfer

Keep \(h,k,\chi=\chi_{h,k}\), \(q=\deg\chi\), \(N\ge q-1\), the original quotient frame, \(A=M_S\), \(e_0=[1]\), \(\ell[P]=[S^{q-1}]\operatorname{rem}_\chi P\), \(R=e_0\ell\), and the complex parameter \(t\). R65's generator is exactly
\[
T_t=A+tR-kI/2.
\]
In the admitted HG source domain, \(a>0\) has the actual finite weighted source Grams, \(L\) gives \(\delta=\kappa/(e^{aL}-1)<1\), and HG3 proves
\[
(1-\delta)M\preceq M_\theta\preceq(1+\delta)M.
\]
The original relation columns give \(C-C_\theta=B_{\rm rel}X_\theta\). Their orthogonality supplies the actual relation Gram
\[
\mathscr D=\int(C-C_\theta)^*M_\theta(C-C_\theta)\,d\mu,
\qquad G=\overline G+\mathscr D.
\]
The inverse chord in HG6 followed by the positive \(2\)-by-\(2\) block Schur complement gives \(0\preceq\mathscr D\preceq\delta^2G\). Therefore \(\mathsf D=G^{-1}\mathscr D\) is self-adjoint for \(\langle v,w\rangle_G=v^*Gw\), with spectrum in \([0,\delta^2]\).

For \(B=G^{-1}(H-G)\), \(I+B\succeq_G\alpha I>0\), the original-metric positive square root \(\mathsf S=(I+B)^{1/2}\) satisfies \(\mathsf S^*G\mathsf S=H\). Thus it is the exact map \((E,H)\to(E,G)\). Write
\[
Z=[\mathsf S,T_t]\mathsf S^{-1}.
\]
Direct expansion gives
\[
\mathsf S(T_t^{\dagger_H}+T_t)\mathsf S^{-1}
 -(T_t^{\dagger_G}+T_t)=Z+Z^{\dagger_G}.
\]
The Sylvester equation \(\mathsf S Y+Y\mathsf S=[B,T_t]\) has the unique solution
\[
Y=[\mathsf S,T_t]
 =\int_0^\infty e^{-r\mathsf S}[B,T_t]e^{-r\mathsf S}\,dr.
\]
Indeed differentiation of the integrand yields its endpoint \([B,T_t]\), and all spectral block sums of \(\mathsf S\) are positive, so the homogeneous equation has only zero solution. The actual estimates are
\[
\|Y\|_G\le\frac{\|[B,T_t]\|_G}{2\sqrt\alpha},
\qquad
\|Z+Z^{\dagger_G}\|_G\le\frac{\|[B,T_t]\|_G}{\alpha}.
\]
Set \(H=\overline G\), \(B=-\mathsf D\), and \(\alpha=1-\delta^2\). The overall negative sign disappears under the norm, while the internal cancellation remains. This gives the first inequality in R65 exactly:
\[
|\epsilon_{\overline G}(t)-\epsilon_G(t)|
\le\frac{\|[\mathsf D,A]+t[\mathsf D,R]\|_G}{1-\delta^2}.
\]

HG11a retains the spectral projections of every self-adjoint \(B\). For distinct eigenvalues \(b_1<\cdots<b_r\), let \(P_j=\mathbf1_{(b_j,\infty)}(B)\). Then
\[
B=b_1I+\sum_{j=1}^{r-1}(b_{j+1}-b_j)P_j.
\]
In the original orthogonal image/kernel decomposition, \([P_j,T]\) has blocks \(0,T_{12};-T_{21},0\), so its norm is \(\max(\|T_{12}\|,\|T_{21}\|)\le\|T\|_G\). Summing the positive differences gives
\[
\|[B,T]\|_G\le(b_r-b_1)\|T\|_G.
\]
The scalar case has an empty sum and zero commutator. Apply this with the actual \(\mathsf D\) spectrum to obtain R65's second bound \(\delta^2\|T_t\|_G/(1-\delta^2)\). It is the accepted spectral-diameter factor, with no extraneous factor two.

## R65: residue norm, including every singular case

The vectors are exactly \(x=e_0\), \(y=G^{-1}\ell^*\). Hence \(R(v)=x\langle y,v\rangle_G\). For any actual self-adjoint discrepancy \(B\), the maps
\[
U=[Bx,x],\qquad V=[y,-By]
\]
satisfy \([B,R]=UV^{\dagger_G}\), including the negative second column. Self-adjointness makes \(p_0=\langle x,Bx\rangle_G\) and \(r_0=\langle y,By\rangle_G\) real. Their full Grams are
\[
P=U^{\dagger_G}U=
\begin{pmatrix}a_0&p_0\\p_0&c_0\end{pmatrix},
\qquad
Q=V^{\dagger_G}V=
\begin{pmatrix}d_0&-r_0\\-r_0&f_0\end{pmatrix}.
\]
Thus
\[
\operatorname{tr}(PQ)=a_0d_0+c_0f_0-2p_0r_0=T_{\rm res},
\qquad
\det(PQ)=(a_0c_0-p_0^2)(d_0f_0-r_0^2)=\Delta_{\rm res}.
\]
The rectangular determinant identity \(\det(I+zA_0B_0)=\det(I+zB_0A_0)\), proved by the two block eliminations in HG13, identifies the nonzero eigenvalues of \(VPV^{\dagger_G}\) with those of \(PQ\). A second application identifies the characteristic polynomial of \(PQ\) with that of \(P^{1/2}QP^{1/2}\succeq0\), even for singular \(P\). The squared singular values of the commutator are therefore the roots of \(\lambda^2-T_{\rm res}\lambda+\Delta_{\rm res}\). Its largest root is exactly the R65 formula
\[
\|[B,R]\|_G^2
=\frac{T_{\rm res}+\sqrt{T_{\rm res}^2-4\Delta_{\rm res}}}{2}.
\]
No inverse of a mass or determinant has been introduced. \(T_{\rm res}=0\) gives the zero operator; \(\Delta_{\rm res}=0<T_{\rm res}\) gives rank one and norm squared \(T_{\rm res}\); \(\Delta_{\rm res}>0\) gives rank two, including equal singular values when the discriminant is zero. For \(q=1\), \(B=bI\) gives \(a_0=b^2c_0,p_0=bc_0,f_0=b^2d_0,r_0=bd_0\), so both displayed invariants vanish. These cover exactly R65's listed degeneracies and retain all original primary factors of \(\chi\).

HG15 uses the triangle inequality only as an optional bound. R65 correctly retains \(\|[B,A]+t[B,R]\|_G\) as the primary combined quantity, so no cancellation has been discarded in the claimed equality.

## R65: finite constants, strip, boundary and final comparisons

The original \(\kappa_\pm\) and derivative Gram give \(b_a=\sqrt{\kappa_+\kappa_-}\) and \(h_p\), with
\[
d_s=\frac{2b_a}{e^{aL-s}-1},\qquad
\varepsilon=\frac{2}{(1-d_s)(e^{sm}-1)},\qquad
\epsilon_J=\frac{h_p}{2p-1}
\left(\frac{L}{2\pi(J-1)}\right)^{2p-1},
\qquad \xi_J=\frac{\epsilon_J}{1-\delta}.
\]
In HG17 the stars act on fixed maps, not the complex strip variable. In the original relation and quotient metrics the diagonal, cross and inverse bounds give
\[
1+d_s+\frac{d_s^2}{1-d_s}=\frac1{1-d_s}.
\]
Contour shift by \(-s\operatorname{sign}n\) bounds the \(n\)-th coefficient by \((1-d_s)^{-1}e^{-s|n|}\); averaging \(m\) phases retains the multiples of \(m\), giving the displayed two-tail \(\varepsilon\). The finite-frequency estimate retains both tails, its \(2\pi\), \(J-1\), and the full zero-frequency coefficient.

The exact choices in HG20 are
\[
\begin{gathered}
L=a^{-1}\log(1+\kappa/\delta_0+4b_a),\qquad
s=aL-\log(1+4b_a),\\
m=\max\{1,\lceil s^{-1}\log(1+4/\varepsilon_0)\rceil\},\\
J=2+\left\lceil\frac{L}{2\pi}
\left(\frac{h_p}{(2p-1)\xi_0(1-\delta)}\right)^{1/(2p-1)}
\right\rceil,
\end{gathered}
\]
where \(0<\delta_0<1\), \(0<\varepsilon_0<1-\delta_0^2\), \(0<\xi_0<1\). Since \(b_a>0\), substitution proves \(0<s<aL\), \(d_s=1/2\), \(\delta<\delta_0\), \(\varepsilon\le\varepsilon_0\), and \(\xi_J\le\xi_0\). If \(h_p=0\), the formula gives \(J=2\) and the tail is zero. For the neighborhood mentioned in R65, the explicit larger strip
\[
s'=aL-\log(1+3b_a)>s,\qquad d_{s'}=2/3<1
\]
certifies the same Schur inverse on a neighborhood of the closed \(s\)-strip.

Minimization on the original remainder fibres gives
\[
\alpha G\preceq H_{m,J}\preceq\beta G,\qquad
\alpha=(1-\xi_J)(1-\delta^2-\varepsilon)>0,\quad
\beta=1+\varepsilon.
\]
The actual discrepancy is \(B_{m,J}=-\mathsf D+\mathsf E_{m,J}\). From the upper bound \(H_{m,J}\preceq\overline G+\varepsilon G\) and lower bound \(H_{m,J}\succeq(1-\xi_J)(\overline G-\varepsilon G)\), together with \(\overline G\preceq G\), one gets
\[
-\rho I\preceq_G\mathsf E_{m,J}\preceq_G\varepsilon I,\qquad
\rho=\xi_J+(1-\xi_J)\varepsilon.
\]
HG11a therefore gives \(\|[\mathsf E_{m,J},T_t]\|_G\le(\rho+\varepsilon)\|T_t\|_G\), while the entire \(B_{m,J}\) spectrum gives \((\beta-\alpha)\|T_t\|_G/\alpha\) as a second control allowance. The first allowance still contains the complete signed commutator
\[
\alpha^{-1}\|-[\mathsf D,A]-t[\mathsf D,R]
 +[\mathsf E_{m,J},A]+t[\mathsf E_{m,J},R]\|_G.
\]
These are the final accepted HG22 bounds cited by R65.

HG23 starts with the literal degree-\(N+1\) identity \(SC_{\theta,J}-C_{\theta,J}A=\chi Q_{\theta,J}\). The original source, half-density map, periodization and spectral projection commute with \(D_{L,\theta}=-\partial_r+k/2\). The common boundary multiplier \(e^{-i\theta}\) has modulus one, so integration by parts gives \(D^*+D=k\). Substitution into \(D\mathscr R_j-\mathscr R_jA=\mathscr B_j\) gives
\[
A^*H_{m,J}+H_{m,J}A-kH_{m,J}
=-\frac1m\sum_j
(\mathscr R_j^*\mathscr B_j+\mathscr B_j^*\mathscr R_j).
\]
The sign and both ordered boundary terms in R65's cited formula are correct. Complex \(t\) adds exactly \(\overline tR^*H_{m,J}+tH_{m,J}R\).

For the HG24 coefficient, minimum comparison gives a factor in \([\alpha,\beta]\) and the restricted inverse Gram gives a factor in \([\beta^{-1},\alpha^{-1}]\). Their product proves the unchanged \([\alpha/\beta,\beta/\alpha]\) comparison on every nonzero proper invariant \(F\). Positivity of the first factor follows from cyclicity of \(e_0\); positivity of the second follows from the perfect residue pairing and invariance, as proved in the accepted full finite-bound review.

Finally HG25 sets \(e=\epsilon_H(t)+\|Z+Z^{\dagger_G}\|_G\ge\epsilon_G(t)\), with the same Laplacian \(\mathcal L_t=T_t^2-k^2I/4\). For the original nonzero vector \(v\), its definitions give
\[
\operatorname{Re}z=a_1-r^2-k^2/4,\qquad
\operatorname{Im}z=b_1,\qquad a_1^2+b_1^2\le e^2r^2.
\]
Hence
\[
e^2\left(\frac{e^2-k^2}{4}-\operatorname{Re}z\right)-b_1^2
=(a_1-e^2/2)^2+e^2r^2-a_1^2-b_1^2\ge0.
\]
Also \(a_1-r^2\le er-r^2\le e^2/4\). This verifies the exact numerical-range parabola referenced by R65, including \(e=0\), with no inference that the finite metric presentation alone bounds \(\epsilon_H\).

## R66: fixed-source degree cost

The source retained throughout is
\[
w_h(u)=|(g/h)(1/2+iu)|^2/(2\pi),\qquad
m=w_h^{*k},\quad d\nu=m\,du,\quad S(u)=k/2+iu.
\]
The packet \(h\), tensor degree \(k\), \(L>0\), and chosen real sample \(u_0\) are fixed; only the polynomial degree \(N\) grows. For the unchanged frame \(1,S,\ldots,S^N\), HD2–3 give
\[
\Lambda_N=a_NM_N^{-1}a_N^*,\qquad
c_N=M_N^{-1}a_N^*/\Lambda_N,\qquad
a_Nc_N=1,\qquad c_N^*M_Nc_N=\Lambda_N^{-1}.
\]
The last equality follows by direct substitution, using that \(\Lambda_N>0\) is real. The original half-density map is an isometry, so this is both the original \(\mathcal V P_N\) squared norm in R66 and the transformed source squared norm in HD5.

The variational formula for evaluation implies monotonicity of \(\Lambda_N\). If it had a finite bound, its represented Hilbert functional would produce \(\sigma=\overline f\nu-\delta_{u_0}\) with all polynomial moments zero. The actual exponential moment and Cauchy–Schwarz give exponentially weighted finite variation, so its Fourier transform is holomorphic on a strip, with every derivative zero at the origin. The identity theorem makes it zero on that strip. Its Gaussian convolution vanishes by Fubini with the displayed signs and \(1/(2\pi)\); uniform Gaussian approximation on compactly supported continuous functions makes the measure zero. This contradicts the atom of mass one, since \(\overline f\nu\) is atomless. These are the full HD4–5 calculations; no new moment-determinacy hypothesis enters R66.

At \(u_0=(2\pi n_0+\theta)/L\) with \(m(u_0)>0\), the exact sampled mass is \(\omega_0=(2\pi/L)m(u_0)\). Its single Gram summand yields
\[
M_{N,\theta}\succeq\omega_0a_N^*a_N,\qquad
\frac{c_N^*M_{N,\theta}c_N}{c_N^*M_Nc_N}
\ge\omega_0\Lambda_N.
\]
Combine this with the full correlation comparison
\[
M_{N,\theta}\preceq
\left(1+\frac{\kappa_{a,N}}{e^{aL}-1}\right)M_N
\]
to obtain exactly
\[
\kappa_{a,N}\ge(e^{aL}-1)(\omega_0\Lambda_N-1)\longrightarrow\infty.
\]
The exponent \(a\) is an actual admissible weighted-source exponent from HG3/HD8. The correlation upper bound used here does not require its error to be below one. No rate in \(N\), or assertion about variation in the distinct tensor degree \(k\), follows.

The all-phase isometry gives
\[
\int\|\mathcal Z_{L,\vartheta}\mathcal U_k\mathcal VP_N\|^2
\frac{d\vartheta}{2\pi}=\Lambda_N^{-1}\to0,\qquad
\|\mathcal Z_{L,\theta}\mathcal U_k\mathcal VP_N\|^2\ge\omega_0.
\]
This exposes the one wording issue in the initial R66: its phrase “selected phase norm remains at least \(\omega_0\)” must say “selected phase squared norm remains at least \(\omega_0\)”. The ordinary norm bound is \(\sqrt{\omega_0}\). No normalization imposes \(\omega_0\le1\). The first phrase is correspondingly precise as “full holonomy mean squared norm tending to zero”. The source owner was notified; the companion receipt records the disposition of this correction.

The quotient criterion is exact: evaluation annihilates \((\chi)\) if and only if \(\chi(S_0)=0\). When it does, its kernel in the unchanged \(E\) is the image of \((S-S_0)\). If \(\chi=(S-S_0)^rq_0\), the local factor \(\mathbb C[x]/(x^r)\) maps by its constant coefficient and retains \((x)/(x^r)\) in its kernel; all other primary blocks map to zero. This is precisely the HD primary kernel cited by R66.

## R66: continuous completion and canonical metric limit

The CR source fixes the same \(h,k,\chi\), including all coefficients and multiplicities. Put
\[
H=L^2(m\,du),\qquad
H_\chi=L^2(|\chi(S(u))|^2m(u)\,du).
\]
The weighted exponential moment is finite after reducing its exponent to absorb the fixed polynomial \(|\chi|^2\). For either measure, an orthogonal vector gives an exponentially weighted finite measure \(\overline f\,d\eta\) with all polynomial moments zero, using the exact inverse \(u=(S-k/2)/i\). The holomorphic Fourier and Gaussian argument just checked proves \(f=0\). Thus the polynomials are dense in both of these particular Hilbert spaces.

The multiplier
\[
U_\chi:H_\chi\to H,\qquad f\mapsto\chi(S)f
\]
has the stated domain, and its inverse is division by \(\chi(S)\) away from its finitely many real-line zeros. Those points have zero measure. The two identities
\[
\|\chi f\|_H^2=\|f\|_{H_\chi}^2,\qquad
\|v/\chi\|_{H_\chi}^2=\|v\|_H^2
\]
prove both onto isometry and inverse without claiming bounded multiplication on the unweighted space \(H\). Transporting polynomial density through \(U_\chi\) proves \(\overline{\chi\mathbb C[S]}^H=H\). R66 states exactly this weighted multiplier and inherited continuous relation closure.

For \(\mathcal B_N=\chi\mathcal P_{N-q}\), the source orthogonal projection \(\Pi_N\) and the fixed remainder section \(s:E\to\mathcal P_{q-1}\) give
\[
R_N=(I-\Pi_N)s,\qquad J_NR_N=I_E,\qquad G_N=R_N^*R_N.
\]
Indeed \(s(x)+\mathcal B_N\) is the full fibre of \(J_N\), and its orthogonal component is the unique least-norm element. This proves the equality with the original coefficient formulas \(G_N=(J_NM_N^{-1}J_N^*)^{-1}\), \(R_N=M_N^{-1}J_N^*G_N\). At \(N=q-1\), the relation subspace is zero and the same formulas apply.

The increasing \(\mathcal B_N\) have dense union. For any \(v\in H\), approximate it by one \(b\in\mathcal B_n\); for \(N\ge n\), \(\|(I-\Pi_N)v\|\le\|v-b\|\). Hence \(\Pi_N\to I\) strongly. Apply this to the finitely many unchanged columns of \(s\): \(R_N\to0\), and \(|(G_N)_{ij}|\le\|R_Ne_i\|\|R_Ne_j\|\to0\). Enlarging the relation subspace decreases each minimum, proving the Loewner statement \(G_N\downarrow0\), with every finite \(G_N>0\).

For any \((v,y)\in H\times E\), choose polynomial \(p_j\to v\). For the particular vector \(x_j=y-Jp_j\), choose \(N_j\) so that \(\|R_{N_j}x_j\|<1/j\). Then \(p_j+R_{N_j}x_j\to v\) and its exact \(J\)-value is \(y\). Thus \(\overline{\operatorname{graph}J}=H\times E\) as R66 states. This does not make the original finite class map zero. The graph and norm limits use a fixed finite coefficient frame and require no bound uniform in the varying \(x_j\).

## R66: singular phase quotient, exact gap and finite average positivity

For each original phase retain \(u_n(\theta)=(2\pi n+\theta)/L\), \(\nu_{n,\theta}=(2\pi/L)m(u_n(\theta))\), its positive-mass index set \(I_\theta\), and \(H_\theta=\ell^2(I_\theta,\nu_\theta)\). The map \(T_\theta P=(P(S(u_n(\theta))))_{n\in I_\theta}\) takes every finite polynomial into this original sampled Hilbert space by the accepted exponential lattice bounds. Null-weight coordinates are never inverted.

Both \(T_\theta(\mathcal P_N)\) and \(T_\theta(\mathcal B_N)\) are finite-dimensional closed subspaces. Thus
\[
Q_{N,\theta}
=T_\theta(\mathcal P_N)/T_\theta(\mathcal B_N),
\qquad
\rho_{N,\theta}[P]=[T_\theta P]
\]
is the correct receiving normed quotient even when the phase Gram is singular. It is well defined because differences of lifts lie in \(\mathcal B_N\). If \(T_\theta P=T_\theta b\), \(b\in\mathcal B_N\), then \(P-b\in\ker T_\theta\) and \(J_N(P-b)=J_NP\); the converse is immediate by selecting such a null representative. Consequently
\[
\ker\rho_{N,\theta}
=J_N(\ker(T_\theta|_{\mathcal P_N})).
\]
This restriction is implicit in R66's finite-domain \(T_\theta\) notation; the type is the image of a coefficient kernel in \(E\), not a substituted quotient by all of \(\ker T_\theta\).

The pullback form is the exact minimum
\[
x^*G_{N,\theta}x
=\min_{b\in\mathcal B_N}\|T_\theta(sx+b)\|^2.
\]
The observed minimum exists uniquely in the orthogonal complement of the relation image, although its coefficient lift can be nonunique. Taking the infimum over rational complex relation coefficients proves measurability. Testing \(R_Nx\), and unfolding the exact phase measure, gives
\[
0\le\int x^*G_{N,\theta}x\,\frac{d\theta}{2\pi}
\le\int\|T_\theta R_Nx\|^2\,\frac{d\theta}{2\pi}
=\|R_Nx\|_H^2.
\]
The mass factor is exact: \((2\pi/L)d\theta/(2\pi)=du\) on each lattice interval. Polarization and the positive-form Cauchy–Schwarz inequality make every matrix entry integrable. This proves R66's \(0\preceq\overline G_N\preceq G_N\) without a singular matrix inverse.

Let \(\Pi_{N,\theta}\) now mean the orthogonal projection in \(H_\theta\) onto \(T_\theta(\mathcal B_N)\). Since \(T_\theta R_Nx-T_\theta sx\) is a relation, the minimizing observed lift is \((I-\Pi_{N,\theta})T_\theta R_Nx\). Pythagoras and the all-phase identity yield the full independent gap formula cited in R66:
\[
x^*(G_N-\overline G_N)x
=\int\|\Pi_{N,\theta}T_\theta R_Nx\|^2
\frac{d\theta}{2\pi}.
\]
The independent proof also constructs this projection as \(T_\theta B F_\theta^+d_\theta x\), where \(F_\theta=B^*M_{N,\theta}B\), \(d_\theta=B^*M_{N,\theta}R_N\). Any vector in \(\ker F_\theta\) is an observed zero relation, so it pairs to zero with \(T_\theta R_Nx\); this proves \(d_\theta x\in\operatorname{ran}F_\theta\). The Borel limit \((F_\theta^2+\epsilon I)^{-1}F_\theta\to F_\theta^+\) proves measurability, while the observed projection norm is bounded by the trial norm. At the empty relation space the projection and gap are zero.

For \(k=1\), the nonzero entire \(g/h\) has countably many real-line zeros. Their phase residues modulo \(2\pi\) form a countable set. Outside it, every lattice weight is positive. A nonzero polynomial cannot vanish at all infinitely many distinct sample points, so \(M_{N,\theta}>0\) there, for every finite \(N\). For \(k\ge2\), positivity of the original convolution gives the same property at every phase. Therefore, for each fixed nonzero \(x\in E\), its finite quotient minimum is strictly positive almost everywhere, and its integral is strictly positive. This proves every finite \(\overline G_N>0\) stated in R66.

Phasewise enlargement of relations gives \(\overline G_N\downarrow0\) using its upper bound by \(G_N\). Also \(0\preceq\mathscr D_N\preceq G_N\) gives the absolute gap limit zero. Neither argument asserts monotonicity of \(\mathscr D_N\), a zero limit of \(G_N^{-1}\mathscr D_N\), a uniform positive lower bound over phases, or a rate in tensor degree \(k\).

Finally, at an actual positive-mass sampled root \(S_{n,\theta}\) of the unchanged \(\chi\), a class \(x\) evaluating to one there has
\[
x^*G_{N,\theta}x\ge\nu_{n,\theta}>0,\qquad
\frac{x^*G_{N,\theta}x}{x^*G_Nx}
\ge\frac{\nu_{n,\theta}}{x^*G_Nx}\longrightarrow\infty.
\]
The numerator bound survives the relation quotient because every literal \(\chi\)-multiple vanishes at that root. This verifies CR14's exact ratio cited in R66. When no positive-mass root is sampled, the displayed lower bound is not claimed. Full primary multiplicities stay in \(E\); the completed sampled quotient receives only the constant coefficient at sampled roots and has the full nilpotent and unsampled-block kernel. The absolute source limit does not determine its relative gap.

## Continuity and disposition record

R65's formulas and scope pass the full proof-body crosswalk. R66's formulas, fixed-\(h,k\) limits and singular quotient types pass; the initial ordinary-norm wording issue is identified above and was sent promptly to the source owner. The companion JSON records the final source hash and whether that exact wording correction has been incorporated.

Root owns the full session and user-input provenance. This report records the assigned mathematical comparisons and the source correction history. No earlier accepted source, proof review or visual receipt was altered.
