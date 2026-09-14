# Independent full-proof review of all-holonomy descent

Date: 2026-09-13. The complete 760-line NOTE.md and complete SOURCE_REVIEW.md were read. The note has 73 labelled displays: H1–H66 together with H49a–H49g. This review checks the new identities and inequalities, retains the exact inherited arithmetic maps, and supplies complete proofs of the quantitative and completion statements needed for their use. It does not replay the packet's tests, alter its raw files, or claim a new audit of the entire inherited analytic corpus.

## 1. Source pin and disposition

The reviewed packet is

    source-workspace/output/split_zero_rh_tandem_2026-09-12/sources/web_holonomy_descent_delivery/Tau_Holonomy_Descent_Control

Its source pins are:

- NOTE.md, 35088 bytes, SHA-256 900e7c16369a58093b16a03dbc449d41a100ee45dbe8515e30bc026e660ba393.
- NOTE.tex, 38667 bytes, SHA-256 444f82a8fa420e6f471ef448442085f3a93acb137069e1505d155faab051b881.

SOURCE_REVIEW.md, INTAKE.json and COORDINATION.md were also read. Their prior-source reading and execution claims remain historical receipts; they are not relabelled as fresh scans or test executions.

The new central mathematics is correct: the common-versus-phase minimum discrepancy is the exact norm of an original relation; its averaged loss is at most \(\eta^2G\); the complex extension and Fourier quadrature preserve the reference metrics; the finite cover maps have the stated signs and factors; and the later completed quotient has zero direct integral almost everywhere.

Two phrases need precise interpretation in any integrated reader:

1. A fixed-phase transform is defined on the admitted rapidly decaying sources, and for almost every phase for a general Hilbert source. It is the joint direct-integral transform that extends to all of \(L^2(\mathbb R;\mathcal K)\). Point evaluation at an arbitrarily prescribed phase is not a bounded map on that whole Hilbert space.
2. The inverse in H49c is guaranteed on the selected strip \(|\operatorname{Im}z|\le s\) with \(d_s<1\). The larger strip \(|\operatorname{Im}z|<aL\) is the domain of the correlation series, and does not by itself guarantee inverse existence.

For H64 the proof must first retain the positive-weight support of its measure. The marked \(k=1\) source has nonzero weight at every sampled root of \(\chi\), because its selected zero orders are complete; for \(k\ge2\) all sample weights are positive. Thus the printed H64 target is valid for the marked source, rather than requiring deletion of one of its represented root fibres.

## 2. The original arithmetic reference map is retained

Keep the original
\[
g=2\xi,\quad D=-x\partial_x,\quad
\Theta\phi(x)=2\sum_{n\ge1}\phi(nx),
\]
the admitted \(V,\mathscr B\), the full-order packet \(h\), and the seed
\[
\mathcal MF_h=g/h,\qquad h(D)F_h=\Theta\phi_*,
\]
\[
\phi_*=(4\pi^2x^4-6\pi x^2)e^{-\pi x^2}.
\]
The finite source map, arithmetic quotient, and inclusion remain
\[
\mathcal VP=P(D_1+\cdots+D_k)F_h^{\otimes k},\qquad
E=\mathbb C[S]/(\chi_{h,k}),\quad S=s_1+\cdots+s_k,\quad A=M_S,
\]
\[
J^{(k)}\mathcal V=\eta\pi_\chi,\qquad
q^{(k)}\mathcal V=\sigma_h^{\otimes k}\eta\pi_\chi,\qquad
\eta[P]=\upsilon_h^{\otimes k}P(A_k)1.
\tag{R1}
\]
Here \(\upsilon_h=j_h(g/h)\) is the original unit on the complete selected jets. The same symbol \(\eta\) is used in the note both for this inclusion and for a scalar error parameter later; they are different typed objects. In this review \(\eta\) in a scalar interval or \(\eta^2\) means only the scalar error parameter. Equation (R1) always denotes the retained arithmetic inclusion.

The quotient map at degree \(N\ge q-1\), with \(q=\deg\chi>0\), is the literal
\[
J_N=\pi_\chi|_{P_N},\qquad
P_N=\mathbb C[S]_{\le N},\qquad
\ker J_N=\chi P_{N-q}.
\tag{R2}
\]
The complete-jet construction makes the inclusion in (R1) injective: \(\upsilon_h^{\otimes k}\) is a unit, while \(\chi\) is precisely the annihilator polynomial of the cyclic vector for the tensor-sum action. Consequently (R2) is the same polynomial relation space seen in the full arithmetic image. No rectangular determinant of the inclusion is introduced, and no inverse is declared on a larger target than its image.

The predecessor locator for the retained norm and relation maps is

    source-workspace/output/split_zero_rh_tandem_2026-09-12/sources/web_periodized_source_delivery/Tau_Periodized_Source_Control/RESEARCH_NOTE.md

at SHA-256 f903ae8473efdfcde0f45a83878837289d2b0604c1a34903276d7c840fe972b9. Selected lines 77–158 and the relation-primitive passage 408–416 were read directly for this review. They retain the full \(g/h\), the unit, the derivative coordinates, and the explicit primitive below.

If \(Q\) is any polynomial coefficient map and \(\chi(S)Q(S)\) is an original relation, fixed-order division in the multivariate polynomial ring gives
\[
\chi(s_1+\cdots+s_k)Q(s_1+\cdots+s_k)
=\sum_{i=1}^k h(s_i)Q_i(s_1,\ldots,s_k).
\tag{R3}
\]
The remainder is zero because \(\chi(S)\) annihilates the cyclic class in
\(\mathbb C[s_1,\ldots,s_k]/(h(s_1),\ldots,h(s_k))\).
Division by the retained \(h(s_i)\), using its actual nonzero leading coefficient, constructs the \(Q_i\); it does not replace the ideal by a power of \(\chi\) or change the seed \(g/h\).

The actual tensor primitive of (R3) has its \(i\)-th summand obtained by replacing \(F_h\) in slot \(i\) by \(\phi_*\), applying \(Q_i(D_1,\ldots,D_k)\), and multiplying that summand by \((-1)^{i-1}\). The tensor differential contributes its own \((-1)^{i-1}\), so each resulting relation has the positive sign in (R3). This proves the primitive map for every coefficient discrepancy used below, including its tensor signs.

The lift to a retained support label is \((\ell,v)\mapsto(\ell,fv)\), with \(\tau\mapsto\tau\). For a quotient by a relation module, equality is exactly equality modulo that module. Therefore a zero coefficient output is the receiving represented zero. The pair of observations \((p_R,b_R)\) distinguishes it from \(\tau\): both have arithmetic value zero, but their support observations differ. H2–H4 and the arithmetic square H3 follow directly from these definitions and are preserved by every coefficient-linear map in this review.

## 3. All-holonomy isometry with every measure and Fourier factor

The original logarithmic coordinate map is
\[
x_i=e^{r+z_i}\ (i<k),\qquad x_k=e^r,\qquad
(\mathcal U_kF)(r,z)
=e^{(kr+\sum_{i<k}z_i)/2}F(x_1,\ldots,x_k).
\]
The linear map \((r,z)\mapsto(\log x_1,\ldots,\log x_k)\) has determinant of absolute value one, while
\[
d^kx=e^{kr+\sum z_i}\,dr\,dz.
\]
Thus the displayed half-density gives the exact original \(L^2(d^kx)\)-norm, and differentiation gives
\[
\mathcal U_kD^{(k)}
=(-\partial_r+k/2)\mathcal U_k.
\tag{R4}
\]
No \(z_i\) is averaged or integrated away before forming the \(\mathcal K\)-valued source, where \(\mathcal K=L^2(\mathbb R^{k-1},dz)\), with \(\mathcal K=\mathbb C\) for \(k=1\).

Fix \(L>0\). Decompose a real coordinate uniquely as \(r+aL\), with \(0\le r<L\), \(a\in\mathbb Z\), modulo the measure-zero cell boundaries. The map
\[
\psi\longmapsto\bigl(\psi(r+aL)\bigr)_{a\in\mathbb Z}
\]
is an isometry
\[
L^2(\mathbb R;\mathcal K)
\longrightarrow L^2([0,L];\ell^2(\mathbb Z;\mathcal K)).
\]
It is onto by the inverse cell assembly. Fourier series of this actual sequence then give
\[
(\mathcal Z_{L,\theta}\psi)(r)
=\sum_{a\in\mathbb Z}e^{ia\theta}\psi(r+aL)
\]
and the unitary joint transform
\[
\mathcal Z_L:
L^2(\mathbb R;\mathcal K)
\xrightarrow{\sim}
\int_{[0,2\pi)}^\oplus L^2([0,L];\mathcal K)\,\frac{d\theta}{2\pi}.
\tag{R5}
\]
Its inverse coefficient formula is exactly
\[
\psi(r+aL)
=\frac1{2\pi}\int_0^{2\pi}
e^{-ia\theta}(\mathcal Z_L\psi)(r,\theta)\,d\theta.
\tag{R6}
\]
For general Hilbert data these are Fourier-series identities in \(L^2\), with the inverse understood as a Bochner Fourier coefficient for almost every \(r\). For the admitted rapidly decaying source columns, the series and differentiated series converge on compact sets, so the pointwise formulas and every fixed phase are available.

Reindexing \(a\) gives the boundary multiplier
\[
\mathcal Z_{L,\theta}\psi(r+L)
=e^{-i\theta}\mathcal Z_{L,\theta}\psi(r).
\]
With the original Fourier convention
\[
\widehat\psi(u)=\int_\mathbb R\psi(r)e^{iur}\,dr,
\]
the coefficient against the normalized basis
\[
L^{-1/2}e^{-i(2\pi n+\theta)r/L}
\]
is \(L^{-1/2}\widehat\psi((2\pi n+\theta)/L)\). Indeed, on substituting \(y=r+aL\), the factor is
\[
e^{ia\theta}e^{-ia(2\pi n+\theta)}=1.
\]
This proves H11–H14 including their signs and all \(L,2\pi\) factors.

A bounded map on the joint direct integral cannot in general be evaluated at a prescribed phase. Already on the scalar sequence space, the functional \((c_a)\mapsto\sum_a e^{ia\theta_0}c_a\) is unbounded on \(\ell^2(\mathbb Z)\): take \(c_a=m^{-1/2}e^{-ia\theta_0}\) on \(m\) consecutive indices. Its sequence norm is one and its phase value is \(\sqrt m\). This proves the domain qualification stated in Section 1, without restricting the admitted finite sources.

For \(\Psi_N=\mathcal U_k\mathcal V|_{P_N}\), apply (R5) to each pair of columns and polarize. It gives
\[
M_N=\Psi_N^*\Psi_N
=\int_0^{2\pi}
(\mathcal Z_{L,\theta}\Psi_N)^*(\mathcal Z_{L,\theta}\Psi_N)
\,\frac{d\theta}{2\pi}
=\int_0^{2\pi}M_N(\theta)\,\frac{d\theta}{2\pi}.
\tag{R7}
\]
The factor \(d\theta/(2\pi)\) is Fourier inversion measure. It does not change any column norm or original arithmetic mass.

The spectral norm retained from the source is
\[
\int_\mathbb R |P(k/2+iu)|^2m_{h,k}(u)\,du,\qquad
m_{h,k}=w_h^{*k},\qquad
w_h(u)=\frac{|(g/h)(1/2+iu)|^2}{2\pi}.
\]
Partial Plancherel therefore identifies the \(\mathcal K\)-inner product of the Fourier columns with \(2\pi m_{h,k}(u)\) times their polynomial factors. The coefficient computation above proves exactly
\[
M_N(\theta)_{ab}
=\frac{2\pi}{L}\sum_{n\in\mathbb Z}
m_{h,k}\!\left(\frac{2\pi n+\theta}{L}\right)
\overline{P_a\!\left(k/2+i\frac{2\pi n+\theta}{L}\right)}
P_b\!\left(k/2+i\frac{2\pi n+\theta}{L}\right).
\tag{R8}
\]
In particular the \(\theta=0,n=0\) term is retained. Since \(w_h\) is nonnegative and positive almost everywhere, its convolution with itself is strictly positive at every real point; induction gives the same assertion for \(k\ge2\). Infinitely many distinct sample points then make (R8) positive definite on a finite polynomial source. At any other admitted source where a relative bound with error less than one is supplied, that bound independently guarantees positivity.

## 4. Exact sections, discrepancy, and original relation primitive

Fix a finite source and retain the surjection \(J:P_N\to E\), the injective relation column matrix \(B:\mathbb C^r\to P_N\) with image \(\ker J\), and the exact phase mean \(M=\int M_\theta\,d\theta/(2\pi)\). All metrics in this section are positive definite.

Put
\[
G=(JM^{-1}J^*)^{-1},\qquad C=M^{-1}J^*G,
\]
\[
G_\theta=(JM_\theta^{-1}J^*)^{-1},\qquad
C_\theta=M_\theta^{-1}J^*G_\theta.
\tag{R9}
\]
Surjectivity of \(J\) makes \(JM^{-1}J^*\) positive definite: for \(x\ne0\), \(J^*x\ne0\), so \(x^*JM^{-1}J^*x>0\). Thus every inverse is well typed on \(E\).

Direct multiplication proves
\[
JC=JC_\theta=\mathbf1_E,\quad
B^*MC=B^*J^*G=0,\quad
B^*M_\theta C_\theta=0,
\]
\[
C^*MC=G,\qquad C_\theta^*M_\theta C_\theta=G_\theta.
\tag{R10}
\]
For an arbitrary representative \(v=Cx+By\) of \(x\in E\),
\[
v^*Mv=x^*Gx+y^*(B^*MB)y.
\]
Hence \(Cx\) is the unique minimum-norm representative. The same proof applies at each phase, without changing the quotient map.

Since \(J(C-C_\theta)=0\), there is a unique coefficient map \(X_\theta:E\to\mathbb C^r\) with
\[
C-C_\theta=BX_\theta.
\]
Applying \(B^*M_\theta\) proves its actual coefficient formula
\[
X_\theta=(B^*M_\theta B)^{-1}B^*M_\theta C.
\tag{R11}
\]
Here \(B\) is multiplication by the literal polynomial \(\chi\), in the specified relation basis. Applying the fixed division and tensor primitive (R3) to each column of \(BX_\theta\) gives its original theta primitive with all signs and coefficients retained.

Expanding \(C=C_\theta+BX_\theta\) in \(C^*M_\theta C\), both cross terms vanish by (R10), so
\[
C^*M_\theta C
=G_\theta+X_\theta^*B^*M_\theta BX_\theta.
\]
Integrating and using the actual mean \(M\) gives
\[
\boxed{
G=\overline G+\mathscr D,\qquad
\overline G=\int G_\theta\frac{d\theta}{2\pi},\quad
\mathscr D=\int X_\theta^*B^*M_\theta BX_\theta\frac{d\theta}{2\pi}.
}
\tag{R12}
\]
Equivalently \(\mathscr D=\int(C-C_\theta)^*M_\theta(C-C_\theta)\,d\theta/(2\pi)\).
Every integrand is positive semidefinite. This proves H24–H28, including the same original quotient and reference section. At \(N=q-1\), \(r=0\); the relation term is the zero map, the \(0\times0\) inverse is the inverse of the unique automorphism of the zero space, and the formulas reduce to equality \(G=\overline G\).

## 5. Complete proof of the sharp \(\eta^2\) enclosure

Assume the actual source bound
\[
(1-\eta)M\preceq M_\theta\preceq(1+\eta)M,\qquad 0\le\eta<1.
\tag{R13}
\]
The upper inequality \(\overline G\preceq G\) is already (R12).

For \(x\in[1-\eta,1+\eta]\), direct subtraction gives
\[
\frac{2-x}{1-\eta^2}-\frac1x
=\frac{\eta^2-(x-1)^2}{x(1-\eta^2)}\ge0.
\tag{R14}
\]
The auxiliary congruence
\[
T_\theta=M^{-1/2}M_\theta M^{-1/2}
\]
is Hermitian positive definite, with precisely that spectral interval. Diagonalizing this auxiliary operator and applying (R14) to its eigenvalues gives
\[
T_\theta^{-1}\preceq
\frac{2\mathbf1-T_\theta}{1-\eta^2}.
\]
Congruence back by \(M^{-1/2}\), retaining the original dual-coordinate map, proves
\[
M_\theta^{-1}\preceq
\frac{2M^{-1}-M^{-1}M_\theta M^{-1}}{1-\eta^2}.
\tag{R15}
\]
This is the same map as the note's functional calculus for the \(M\)-self-adjoint operator \(M^{-1}M_\theta\), followed by \(M^{-1}\); it does not replace \(M\) by a new arithmetic form.

Set
\[
K_\theta=JM_\theta^{-1}J^*=G_\theta^{-1},\quad
K=JM^{-1}J^*=G^{-1},\quad
\overline K=\int K_\theta\,\frac{d\theta}{2\pi}.
\]
Congruence by \(J\) and the exact mean in (R15) prove
\[
\overline K\preceq(1-\eta^2)^{-1}K.
\tag{R16}
\]
For \(x,y\in E\),
\[
\begin{pmatrix}x\\y\end{pmatrix}^*
\begin{pmatrix}K_\theta&\mathbf1\\\mathbf1&G_\theta\end{pmatrix}
\begin{pmatrix}x\\y\end{pmatrix}
=(x+G_\theta y)^*K_\theta(x+G_\theta y)\ge0.
\]
Averaging and then substituting \(x=-\overline K^{-1}y\) give
\[
y^*(\overline G-\overline K^{-1})y\ge0.
\]
Thus \(\overline G\succeq\overline K^{-1}\).
Order reverses under inversion on positive definite matrices: to see this, conjugate \(A\preceq B\) by \(A^{-1/2}\), invert its eigenvalues, and conjugate back. Applying this to (R16) proves
\[
\boxed{
(1-\eta^2)G\preceq\overline G\preceq G,\qquad
0\preceq\mathscr D\preceq\eta^2G.
}
\tag{R17}
\]
This verifies H1 and H32–H37 completely. The exact mean condition is essential in passing from (R15) to (R16).

For \(aM\preceq M_\theta\preceq bM\), with \(0<a\le1\le b\), the identity
\[
\frac{a+b-x}{ab}-\frac1x
=\frac{(x-a)(b-x)}{abx}\ge0
\]
on \([a,b]\) replaces (R14). The same argument gives
\[
\overline G\succeq\frac{ab}{a+b-1}G,\qquad
\mathscr D\preceq
\frac{(1-a)(b-1)}{a+b-1}G.
\tag{R18}
\]
Here \(a+b-1>0\), and subtracting \(ab/(a+b-1)\) from one gives exactly the stated defect coefficient. This verifies H38.

### Exact sharpness on a smooth full phase circle

H65–H66 are correct: the two forms
\[
M_\pm=7\begin{pmatrix}1&\pm\eta\\\pm\eta&1\end{pmatrix},
\quad M=7\mathbf1,\quad J=(1\ \ 0),\quad B=\binom01
\]
have \(G=7\), \(C=(1,0)^T\), \(C_\pm=(1,\mp\eta)^T\), and
\[
G_\pm=7(1-\eta^2),\qquad \mathscr D=7\eta^2.
\]
The two stated point masses on \(-1,1\) give exactly their entries \(1,S,S^2\), including the mass \(7\).

The same loss is attained by a smooth analytic phase family, so there is no need to rely on a discontinuous embedding of a two-point example into the circle:
\[
M_\theta=7
\begin{pmatrix}
1&\eta e^{i\theta}\\
\eta e^{-i\theta}&1
\end{pmatrix}.
\tag{R19}
\]
Its eigenvalues are \(7(1-\eta),7(1+\eta)\), its exact mean is \(7\mathbf1\), and its canonical section and quotient are
\[
C_\theta=\binom{1}{-\eta e^{-i\theta}},\qquad
G_\theta=7(1-\eta^2).
\]
Thus (R17) is saturated at every phase after averaging, with \(\mathscr D=7\eta^2\).

This family is also the all-holonomy Gram of explicit smooth finite source columns. Choose orthonormal \(f,g\in C_c^\infty(0,L)\), extend them by zero, and put
\[
\psi_1(r)=\sqrt7 f(r),\qquad
\psi_2(r)=\sqrt7\bigl(\eta f(r-L)+\sqrt{1-\eta^2}\,g(r)\bigr).
\]
Then
\[
\mathcal Z_{L,\theta}\psi_1=\sqrt7 f,\qquad
\mathcal Z_{L,\theta}\psi_2
=\sqrt7\bigl(\eta e^{i\theta}f+\sqrt{1-\eta^2}\,g\bigr),
\]
whose Gram is exactly (R19), with original source Gram \(7\mathbf1\).
This proves sharpness even in a smooth all-holonomy finite-source setting. It is a positive-source calibration, not a claim that these chosen columns form a particular zeta packet.

## 6. Weighted source bounds and every finite endpoint factor

Retain
\[
M_{a,\pm}=\int_\mathbb R e^{\pm2ar}\Psi_N(r)^*\Psi_N(r)\,dr,\qquad
\kappa_{a,N}=\sup_{v\ne0}
\frac{v^*(M_{a,+}+M_{a,-})v}{v^*Mv}.
\]
The coordinate factors are precisely \(x_k^{\pm2a}\), since \(r=\log x_k\).
For
\[
\mathcal C(t)=\int_\mathbb R\Psi_N(r)^*\Psi_N(r+t)\,dr
\]
and \(t>0\), the exact weighted identity is
\[
v^*\mathcal C(t)w
=e^{-at}\int
\langle e^{-ar}\Psi_N(r)v,\ e^{a(r+t)}\Psi_N(r+t)w\rangle_{\mathcal K}\,dr.
\tag{R20}
\]
Cauchy–Schwarz gives its bound by
\[
e^{-at}\sqrt{(v^*M_{a,-}v)(w^*M_{a,+}w)}.
\]
For \(t<0\) the signs interchange. Reindexing and unfolding the double periodization sum prove
\[
M_\theta=\sum_{b\in\mathbb Z}e^{ib\theta}\mathcal C(bL),\qquad
\mathcal C(0)=M,\quad\mathcal C(-t)=\mathcal C(t)^*.
\tag{R21}
\]
For a single vector \(v\), summing the two nonzero tails in (R20) and using \(2\sqrt{xy}\le x+y\) prove
\[
|v^*(M_\theta-M)v|
\le\frac{v^*(M_{a,+}+M_{a,-})v}{e^{aL}-1}
\le\delta_L\,v^*Mv,
\]
\[
\delta_L=\frac{\kappa_{a,N}}{e^{aL}-1}.
\tag{R22}
\]
Thus H39–H41 are correct, with the actual source mass and both weighted Grams retained. When \(\delta_L<1\), it is an evaluated source-relative error parameter for (R13), and (R17) gives loss at most \(\delta_L^2G\). No assertion that \(\kappa_{a,N}\) is uniformly bounded in the arithmetic packet is introduced.

For positive definite \(M_1\preceq M_2\), minimizing over the same affine representatives \(Jv=x\) proves
\[
\mathcal Q_J(M_1)\preceq\mathcal Q_J(M_2),\qquad
\mathcal Q_J(M)=(JM^{-1}J^*)^{-1}.
\tag{R23}
\]
Its exact scalar law is \(\mathcal Q_J(cM)=c\mathcal Q_J(M)\), for \(c>0\).
These two facts justify every source-to-quotient order transport below without changing \(J\).

If \(a_0G_N\preceq H_N\preceq b_0G_N\) for each of the four endpoint quotient metrics, with \(0<a_0\le b_0\), then their \(q\) positive generalized eigenvalues give
\[
q\log a_0
\le\log\det H_N-\log\det G_N
\le q\log b_0.
\tag{R24}
\]
A sum of two such errors minus two others lies in
\[
\left[-2q\log(b_0/a_0),\ 2q\log(b_0/a_0)\right].
\tag{R25}
\]
For \(a_0=1-\eta^2,b_0=1\), these are H42–H43. From the exact equation \(G_N=\overline G_N+\mathscr D_N\), determinant multiplicativity also proves
\[
V_N=\overline V_N
\det(\mathbf1+\overline G_N^{-1}\mathscr D_N),
\]
which is H44. The endomorphism \(\overline G_N^{-1}\mathscr D_N\) is self-adjoint and nonnegative in the \(\overline G_N\)-metric, by direct adjoint computation.

For \(m\) equally spaced phases, the finite character calculation in Section 8 gives the literal source mean
\[
M^{(m)}=\frac1m\sum_{j=0}^{m-1}M(L,2\pi j/m)=M(mL,0).
\tag{R26}
\]
Applying (R22) with the period \(mL\) yields
\[
(1-\delta_m)M\preceq M^{(m)}\preceq(1+\delta_m)M,\qquad
\delta_m=\frac{\kappa_{a,N}}{e^{amL}-1}.
\]
Subtracting the source mean from a sampled source gives
\[
-(\delta_L+\delta_m)M
\preceq M(L,\theta_j)-M^{(m)}
\preceq(\delta_L+\delta_m)M.
\]
Since \(M\preceq(1-\delta_m)^{-1}M^{(m)}\), this proves H46–H47 with
\[
\nu_m=\frac{\delta_L+\delta_m}{1-\delta_m}.
\]
The finite weighted average has the same proof (R9)–(R17), with its actual mean and canonical section. Combining it with (R23), when the displayed errors are less than one, gives exactly
\[
(1-\nu_m^2)(1-\delta_m)G
\preceq\overline G^{(m)}
\preceq(1+\delta_m)G.
\tag{R27}
\]
Inserting these two positive factors into (R25) proves H49:
\[
2q\log\frac{1+\delta_m}
{(1-\delta_m)(1-\nu_m^2)}.
\]
This checks H45–H49. The error tends to the quadratic mean/minimum loss as \(m\to\infty\) at fixed \(L\), rather than claiming that mean and minimum eventually commute.

## 7. Holomorphic quotient, certified inverse domain, and quadrature

Put
\[
\kappa_\pm=\sup_{v\ne0}\frac{v^*M_{a,\pm}v}{v^*Mv},
\qquad K_a=\sqrt{\kappa_+\kappa_-}.
\]
Using two independent vectors in (R20), then taking the supremum over their \(M\)-unit spheres, proves
\[
\|M^{-1}\mathcal C(nL)\|_M
\le K_a e^{-a|n|L}.
\tag{R28}
\]
This is an operator-norm proof of H49a, not an inference from a quadratic-form bound on a non-Hermitian correlation.

The correlation series
\[
\widetilde M(z)=M+\sum_{n\ne0}e^{inz}\mathcal C(nL)
\]
and each differentiated series converge uniformly on compact subsets of \(|\operatorname{Im}z|<aL\), since the additional factors \(|n|^j\) are dominated by geometric decay. Thus it is holomorphic and \(2\pi\)-periodic there. For \(0<s<aL\),
\[
\sup_{|\operatorname{Im}z|\le s}
\|M^{-1}(\widetilde M(z)-M)\|_M
\le\frac{2K_a}{e^{aL-s}-1}=d_s.
\tag{R29}
\]
The two separate tail denominators are \(e^{aL+\operatorname{Im}z}-1\) and \(e^{aL-\operatorname{Im}z}-1\); replacing both by \(e^{aL-s}-1\) gives the stated enclosure. This proves H49b without claiming optimality.

Choose the specified \(s\) with \(d_s<1\). Put \(H_B=B^*MB\). The unchanged maps
\[
C:(E,G)\to(P_N,M),\qquad
B:(\mathbb C^r,H_B)\to(P_N,M)
\]
are isometries onto orthogonal complementary subspaces. Their actual direct-sum map and inverse are
\[
T(x,y)=Cx+By,\qquad
T^{-1}p=(Jp,H_B^{-1}B^*Mp).
\tag{R30}
\]
The inverse follows by writing \(p-CJp\in\ker J=\operatorname{im}B\) and applying \(B^*M\).

Let \(D(z)=M^{-1}(\widetilde M(z)-M)\), and retain its four blocks
\[
D_{11}=G^{-1}C^*MDC,\quad D_{12}=G^{-1}C^*MDB,
\]
\[
D_{21}=H_B^{-1}B^*MDC,\quad
D_{22}=H_B^{-1}B^*MDB.
\]
Every block has norm at most \(d_s\) in its actual source and target metrics, because the inclusions in (R30) are isometries and their metric adjoints have norm one. Therefore
\[
B^*\widetilde M(z)B=H_B(\mathbf1+D_{22}),
\qquad
(B^*\widetilde M(z)B)^{-1}
=(\mathbf1+D_{22})^{-1}H_B^{-1},
\]
\[
\|(\mathbf1+D_{22})^{-1}\|_{H_B}
\le\sum_{j\ge0}d_s^j=\frac1{1-d_s}.
\tag{R31}
\]
This proves inverse existence on the selected closed strip \(|\operatorname{Im}z|\le s\). Since \(d_s<1\) strictly and its displayed expression is continuous in \(s\), the same proof works at some \(s'>s\); hence the inverse is holomorphic on an open neighborhood of the closed contour strip.

The exact holomorphic quotient of H49c is
\[
\widetilde G
=C^*\widetilde MC
-C^*\widetilde MB(B^*\widetilde MB)^{-1}B^*\widetilde MC.
\]
Its block expression is
\[
G^{-1}\widetilde G
=\mathbf1+D_{11}
-D_{12}(\mathbf1+D_{22})^{-1}D_{21}.
\]
Thus
\[
\|G^{-1}\widetilde G(z)\|_G
\le1+d_s+\frac{d_s^2}{1-d_s}
=\frac1{1-d_s}.
\tag{R32}
\]
All source, relation, and quotient metrics are present in this bound. At real \(z=\theta\), this Schur complement equals the original \(G_\theta\) by uniqueness of the orthogonal minimum in (R10).

The actual reference section remains available even off the real axis:
\[
\widetilde C(z)
=C-B(B^*\widetilde M(z)B)^{-1}B^*\widetilde M(z)C.
\tag{R33}
\]
It satisfies
\[
J\widetilde C=\mathbf1_E,\qquad
B^*\widetilde M\widetilde C=0,\qquad
C-\widetilde C=B(\mathbf1+D_{22})^{-1}D_{21}.
\]
Consequently
\[
J^{(k)}\mathcal V\widetilde C=\eta,\qquad
q^{(k)}\mathcal V\widetilde C=\sigma_h^{\otimes k}\eta.
\tag{R34}
\]
This is the retained arithmetic inclusion, including its unit and full jets. The relation correction has its exact primitive (R3). The off-axis holomorphic quotient must not be replaced by \(\widetilde C(z)^*\widetilde M(z)\widetilde C(z)\), which would introduce conjugation of the complex parameter.

Also \(\widetilde M=M(\mathbf1+D)\) is invertible on this certified strip. Block inversion through (R30) then shows
\[
\widetilde G=(J\widetilde M^{-1}J^*)^{-1}.
\]
This follows because the upper-left block of \((T^*\widetilde MT)^{-1}\) is both the inverse Schur complement and \(J\widetilde M^{-1}J^*\). It gives the strongest exact quotient identification on the proved domain.

For the Fourier coefficient
\[
\widehat G_n=\frac1{2\pi}\int_0^{2\pi}G_\theta e^{-in\theta}\,d\theta,
\]
shift to \(z=x-is\) when \(n>0\), and to \(z=x+is\) when \(n<0\). The vertical sides cancel by periodicity. The exponential factor has modulus \(e^{-s|n|}\), so
\[
\|G^{-1}\widehat G_n\|_G
\le\frac{e^{-s|n|}}{1-d_s}.
\tag{R35}
\]
The Fourier series is uniformly absolutely convergent on the real axis. Averaging at \(\theta_j=2\pi j/m\) retains exactly multiples of \(m\); the zero coefficient is the exact phase mean. Thus
\[
\overline G^{(m)}-\overline G
=\sum_{\ell\ne0}\widehat G_{\ell m},
\]
\[
\left\|G^{-1}(\overline G^{(m)}-\overline G)\right\|_G
\le\frac2{1-d_s}\sum_{\ell\ge1}e^{-sm\ell}
=\frac2{(1-d_s)(e^{sm}-1)}
=\varepsilon_{m,s}.
\tag{R36}
\]
The two real means are Hermitian, so (R36) is equivalent to a two-sided Loewner error \(\pm\varepsilon_{m,s}G\). Adding it to (R17) proves H49f; inserting \(a_0=1-\eta^2-\varepsilon_{m,s}>0\) and \(b_0=1+\varepsilon_{m,s}\) into (R25) proves H49g. This checks H49a–H49g with every inverse, reference map, \(2\pi\), and both Fourier tails.

The selected-strip qualification is substantive as a domain statement. For example
\[
M_\theta=\operatorname{diag}(1,1+\tfrac12\cos\theta),
\quad J=(1\ \ 0),\quad B=\binom01
\]
is positive definite for every real \(\theta\) and extends to an entire matrix function. But its relation block vanishes at
\[
z=\pi\pm i\operatorname{arcosh}2,
\]
since \(\cos(\pi+iy)=-\cosh y\). Therefore correlation holomorphy on a larger strip cannot replace (R31)'s certified inverse domain. This does not refute the source's displayed bounds on its selected strip.

### The finite frequency tail

For \(p\ge1\), integration by parts and Bochner Cauchy–Schwarz give
\[
\|\widehat{\Psi_Nv}(u)\|_{\mathcal K}^2
\le |u|^{-2p}
\left(\int_\mathbb R\frac{dr}{1+r^2}\right)
\int_\mathbb R(1+r^2)\|\partial_r^p\Psi_N(r)v\|_{\mathcal K}^2\,dr
=\pi|u|^{-2p}v^*H_{p,N}v.
\]
For \(J\ge2\), \(\phi=\theta/(2\pi)\in[0,1)\), and omitted \(|n|>J\),
\[
|n+\phi|\ge|n|-1,\qquad
\sum_{|n|>J}(|n|-1)^{-2p}
=2\sum_{j=J}^\infty j^{-2p}
\le\frac{2(J-1)^{1-2p}}{2p-1}.
\]
The actual discrete Gram coefficient is \(1/L\). Multiplying it by \(\pi(L/(2\pi))^{2p}\) and the last two-tail bound yields exactly
\[
0\preceq M(L,\theta)-M(L,\theta;J)
\preceq
\frac1{2p-1}\left(\frac{L}{2\pi(J-1)}\right)^{2p-1}H_{p,N}.
\tag{R37}
\]
This is H50–H51. If its specified source-relative coefficient is \(\epsilon_J\), (R22) gives an omitted error at most
\[
\xi_JM(L,\theta),\qquad
\xi_J=\frac{\epsilon_J}{1-\delta_L}.
\]
For \(\xi_J<1\), minimization over the same \(J\)-representatives in (R23) proves H52. The finite averaged lower factor is multiplied by \(1-\xi_J\), the upper factor stays unchanged, and (R25) adds exactly \(2q\log(1/(1-\xi_J))\). No omitted near-zero frequency was divided by zero, since the entire set \(|n|\le J\) is retained.

## 8. Finite covers, coefficient descent, and the exact comparison complex

On the circle of length \(mL\), let \(Tf(r)=f(r+L)\), so \(T^m=\mathbf1\), and put \(\theta_j=2\pi j/m\). The actual projectors are
\[
Q_j=\frac1m\sum_{a=0}^{m-1}e^{ia\theta_j}T^a.
\]
The finite geometric sum is \(m\) when its integer frequency is divisible by \(m\), and zero otherwise. Multiplying the two sums proves
\[
Q_jQ_\ell=\delta_{j\ell}Q_j,\qquad
\sum_jQ_j=\mathbf1.
\]
Replacing \(a\) by \(-a\) modulo \(m\) gives \(Q_j^*=Q_j\), and reindexing gives \(TQ_j=e^{-i\theta_j}Q_j\).

At \(r\in[0,L)\), the vector \((f(r+aL))_{0\le a<m}\) is transformed by the literal unitary Fourier matrix
\[
g_j(r)=\frac1{\sqrt m}\sum_{a=0}^{m-1}e^{ia\theta_j}f(r+aL)
=\sqrt m\,Q_jf(r).
\]
Its inverse is
\[
f(r+aL)=\frac1{\sqrt m}\sum_{j=0}^{m-1}e^{-ia\theta_j}g_j(r).
\]
Integrating the finite Parseval identity over \(r\) proves H18–H19 as unitary maps with the displayed interval measures and direct-sum norm.

For the original source, write every integer \(c=a+mb\), \(0\le a<m\). Then
\[
Q_j\mathcal Z_{mL,0}\psi(r)
=\frac1m\sum_{a,b}e^{ia\theta_j}\psi(r+(a+mb)L)
=\frac1m\mathcal Z_{L,\theta_j}\psi(r).
\]
The unitary target therefore has components \(m^{-1/2}\mathcal Z_{L,\theta_j}\psi\). Squared norms and polarization prove H20, including its exact \(1/m\) Gram average.

For a general phase \(\theta\), put \(\delta=L/n\), \(\varphi_a=(\theta+2\pi a)/n\), and let \(T_\delta\) translate on the length-\(L\) quasi-periodic space. Then
\[
T_\delta^n=e^{-i\theta}\mathbf1,\qquad
Q_a^{(n,\theta)}=\frac1n\sum_{b=0}^{n-1}e^{ib\varphi_a}T_\delta^b.
\]
The same Fourier calculation gives a unitary decomposition by
\[
f\mapsto\bigl(\sqrt n\,Q_a^{(n,\theta)}f|_{[0,L/n)}\bigr)_a,
\]
and
\[
Q_a^{(n,\theta)}\mathcal Z_{L,\theta}\psi
=\frac1n\mathcal Z_{L/n,\varphi_a}\psi.
\]
Thus H21 follows. Equivalently its samples are
\[
\frac{2\pi j+\varphi_a}{L/n}
=\frac{2\pi(nj+a)+\theta}{L},
\]
and \((1/n)(2\pi/(L/n))=2\pi/L\). A second refinement by \(p\) has phase \((\theta+2\pi(a+nb))/(np)\); the index \(a+nb\) runs through the classes modulo \(np\), proving the claimed composition law with factor \(1/(np)\).

For the algebraic cover, retain
\[
A_{\rm cov}=\mathbb C[z,z^{-1}],\quad
B_{\rm cov}=\mathbb C[w,w^{-1}],\quad z\mapsto w^m,\quad
\zeta=e^{2\pi i/m}.
\]
The unique division \(d=mq+j\), \(0\le j<m\), of an arbitrary integer exponent gives
\[
w^d=z^qw^j,\qquad
B_{\rm cov}=\bigoplus_{j=0}^{m-1}A_{\rm cov}w^j.
\tag{R38}
\]
Uniqueness of Laurent coefficients proves freeness, rather than just generation. The algebra is also \(A_{\rm cov}[w]/(w^m-z)\), since \(w^{-1}=z^{-1}w^{m-1}\). Its derivative \(mw^{m-1}\) is invertible. Across a square-zero extension, a provisional lift \(v\) of \(w\) is uniquely corrected by
\[
-\frac{v^m-z}{mv^{m-1}},
\]
because all terms of degree two in the correction vanish. This proves the unique infinitesimal lifting property; together with finite presentation and (R38), it proves that this exact cover is finite étale.

The deck map \(\gamma_a(w)=\zeta^{-a}w\) fixes \(z\). The character sum gives
\[
\frac1m\sum_{a=0}^{m-1}\zeta^{ja}\gamma_a
\quad\hbox{with image }A_{\rm cov}w^j.
\]
Multiplication of two basis summands retains its carry:
\[
(f(z)w^j)(g(z)w^\ell)
=f(z)g(z)\,
z^{\lfloor(j+\ell)/m\rfloor}
w^{j+\ell-m\lfloor(j+\ell)/m\rfloor}.
\tag{R39}
\]
For any unital \(A_{\rm cov}\)-algebra \(A'\), the image \(z'\) of \(z\) is a unit. Tensoring the displayed presentation gives exactly H23. Its inverse sends \(a'\) to \(1\otimes a'\), \(w\) to \(w\otimes1\), and \(w^{-1}\) to \(w^{-1}\otimes1\); both composites fix every generator. The basis remains \(1,w,\ldots,w^{m-1}\).

The full gluing map can be made explicit as an additional exact descent statement:
\[
\Phi:B_{\rm cov}\otimes_{A_{\rm cov}}B_{\rm cov}
\longrightarrow\prod_{a=0}^{m-1}B_{\rm cov},\qquad
\Phi_a(f\otimes g)=f\,\gamma_a(g).
\tag{R40}
\]
Let \(t=(1\otimes w)/(w\otimes1)\), so \(t^m=1\) and \(\Phi_b(t)=\zeta^{-b}\). Define
\[
e_a=\frac1m\sum_{j=0}^{m-1}\zeta^{aj}t^j.
\]
The same geometric sums give \(\Phi_b(e_a)=\delta_{ab}\), orthogonal idempotents summing to one, and the inverse
\[
(b_a)_a\longmapsto\sum_a(b_a\otimes1)e_a.
\]
Every element is a \(B_{\rm cov}\)-linear combination of \(1,t,\ldots,t^{m-1}\), so these formulas prove both composites are identities. Under (R40), the two maps \(b\mapsto b\otimes1\) and \(b\mapsto1\otimes b\) become \((b)_a\) and \((\gamma_a(b))_a\). Their equalizer is exactly the invariant ring \(A_{\rm cov}\), by (R38). This supplies the explicit coefficient descent map without invoking an unidentified arithmetic Frobenius.

Under \(w(r)=e^{-2\pi ir/(mL)}\), one has \(w(r+aL)=\zeta^{-a}w(r)\) and \(z(r)=e^{-2\pi ir/L}\). Therefore the deck action and projectors are precisely the analytic translations and H18 projectors. Applying the stated split lift preserves \(\tau\) and the represented coefficient zero. The linear character projectors are not asserted to be ring homomorphisms or the scalar supported-zero element.

For H29–H31, let \(\Delta_m\) repeat coefficients and \(\operatorname{av}_m\) be their actual arithmetic mean. Both commute with the inclusion differential and \(\operatorname{av}_m\Delta_m=\mathbf1\). If \((P_j)\) has common jet \(x\), then \(J\operatorname{av}_m(P_j)=x\). Hence
\[
P_j-\operatorname{av}_m(P_j)\in\ker J=B_N.
\]
The two mutually inverse coefficient maps are
\[
(P_j)\mapsto
\left(\operatorname{av}_m(P_j),
(P_j-\operatorname{av}_m(P_j))_j\right),
\]
\[
(P,(b_j))\mapsto(P+b_j)_j,\qquad \sum_jb_j=0.
\]
They identify the common-jet complex with the original complex plus
\[
[\mathcal B_{N,m}^0\xrightarrow{\mathbf1}\mathcal B_{N,m}^0].
\]
The explicit degree-minus-one homotopy is
\[
h(P_j)=(P_j-\operatorname{av}_m(P_j))_j
\]
in degree one, with \(h=0\) in degree zero. Direct substitution gives
\[
dh+hd=\mathbf1-\Delta_m\operatorname{av}_m.
\tag{R41}
\]
Their degree-one common-jet map is the same \(E\) with inclusion \(\eta\); degree-zero cohomology is zero. Repetition, mean, and this homotopy preserve the stated degree filtration, and commute with multiplication by \(S\) as a map from cutoff \(N\) to cutoff \(N+1\). They do not turn it into an endomorphism at a fixed cutoff.

The contraction (R41) is a coefficient contraction, not an isometry claim. For example the metric adjoint of a diagonal inclusion into the continuous phase source is
\[
P(\theta)\longmapsto
M^{-1}\int M_\theta P(\theta)\,\frac{d\theta}{2\pi},
\]
whereas its arithmetic coefficient retraction is the unweighted mean. The exact relation norm in (R12) is therefore still needed. On each preserved complement a chain endomorphism has identical degree-zero and degree-one blocks, so its two cohomological traces cancel; the norm of that complement need not vanish.

## 9. Complete polynomial-density and completed-phase quotient proof

Retain
\[
u_{n,\theta}=\frac{2\pi n+\theta}{L},\quad
S_{n,\theta}=k/2+iu_{n,\theta},\quad
\nu_{n,\theta}=\frac{2\pi}{L}m_{h,k}(u_{n,\theta}),
\]
\[
I_\theta=\{n:\nu_{n,\theta}>0\},\qquad
\mathcal H_\theta=\ell^2(I_\theta,\nu_\theta).
\tag{R42}
\]
Zero-mass coordinates are quotiented out of the Hilbert seminorm; they are not evaluation functionals on \(\mathcal H_\theta\).

The predecessor's retained exponential-tail estimate is
\[
f_b(u)=e^{b|u|}w_h(u)\in L^1\cap L^\infty
\qquad(0<b<\pi/2).
\]
This is the actual \(g/h\) density, not a substituted weight. Its convolution consequence follows directly from \(|u_1+\cdots+u_k|\le\sum|u_i|\):
\[
e^{b|u|}m_{h,k}(u)
\le f_b^{*k}(u)
\le C_{b,h,k}:=\|f_b\|_\infty\|f_b\|_1^{k-1}.
\tag{R43}
\]
For \(0\le a<b\), summing the positive and negative lattice tails separately gives the literal finite bound
\[
\begin{aligned}
\sum_{n\in I_\theta}\nu_{n,\theta}e^{a|u_{n,\theta}|}
&\le\frac{2\pi C_{b,h,k}}L
\sum_{n\in\mathbb Z}e^{-(b-a)|2\pi n+\theta|/L}\\
&=\frac{2\pi C_{b,h,k}}L
\frac{e^{-(b-a)\theta/L}
+e^{-(b-a)(2\pi-\theta)/L}}
{1-e^{-2\pi(b-a)/L}}.
\end{aligned}
\tag{R44}
\]
At \(\theta=0\) this retains the zeroth term. Since \(\chi(k/2+iu)\) is the original polynomial of degree \(q\), its square modulus is bounded by a constant times \((1+|u|)^{2q}\), with that constant the sum of the actual coefficient bounds. Choosing two distinct exponents \(0<a_1<a_2<b\) and using the finite maximum of \((1+t)^{2q}e^{-(a_2-a_1)t}\) proves a positive exponential moment also for \(|\chi|^2\nu_\theta\).

Here is a full density proof for either of those two measures. Let positive weights \(\mu_n\) on a subset of the shifted lattice satisfy
\[
\sum_n\mu_ne^{a|u_{n,\theta}|}<\infty
\]
for some \(a>0\). Suppose \(f\in\ell^2(\mu)\) is orthogonal to all polynomial evaluation vectors. Since \(u=(S-k/2)/i\), the polynomial evaluation spans in \(u\) and \(S\) agree. Conjugating the orthogonality equations when required gives
\[
\sum_n f_n\mu_nu_{n,\theta}^j=0\quad(j\ge0).
\]
For \(|\operatorname{Re}z|<a/2\), define
\[
F(z)=\sum_n f_n\mu_ne^{zu_{n,\theta}}.
\]
Cauchy–Schwarz gives local absolute convergence:
\[
\sum_n|f_n|\mu_ne^{t|u_{n,\theta}|}
\le\|f\|_{\ell^2(\mu)}
\left(\sum_n\mu_ne^{2t|u_{n,\theta}|}\right)^{1/2}<\infty
\quad(0\le t<a/2).
\]
On a smaller closed strip, every differentiated series converges uniformly by using a slightly larger \(t<a/2\) and the finite bound on \(x^je^{-\epsilon x}\). Hence \(F\) is holomorphic, and all its derivatives vanish at zero. Its Taylor series and holomorphic uniqueness show \(F=0\) on that connected strip.

Fourier uniqueness on the exact shifted lattice is now elementary, with no omitted phase factor. For every index \(m\), absolute convergence permits
\[
0=\frac1L\int_0^L F(it)e^{-itu_{m,\theta}}\,dt
=\sum_n f_n\mu_n\frac1L
\int_0^L e^{2\pi i(n-m)t/L}\,dt
=f_m\mu_m.
\tag{R45}
\]
Thus \(f=0\), proving density. Equation (R44) and its polynomially weighted version apply this proof to \(\nu_\theta\) and \(|\chi|^2\nu_\theta\).

Set
\[
Z_\theta=\{n\in I_\theta:\chi(S_{n,\theta})=0\},\qquad
p_\theta(S)=\prod_{n\in Z_\theta}(S-S_{n,\theta}),
\]
with empty product one. The sample points are distinct; therefore \(p_\theta\) is a squarefree divisor of \(\chi\), and \(|Z_\theta|\le q\).
Every \(\chi P\) vanishes on \(Z_\theta\), and those coordinates are continuous because
\[
|f_n|\le\nu_{n,\theta}^{-1/2}\|f\|_{\mathcal H_\theta}.
\]
Hence its closure is contained in the subspace vanishing there. Conversely, for \(f\) vanishing on \(Z_\theta\), define
\[
g_n=f_n/\chi(S_{n,\theta})\quad(n\in I_\theta\setminus Z_\theta).
\]
It lies in \(\ell^2(|\chi|^2\nu_\theta)\) with squared norm exactly \(\|f\|_{\mathcal H_\theta}^2\). Polynomial density there gives \(P_j\to g\); multiplication by the original \(\chi\) gives \(\chi P_j\to f\) in \(\mathcal H_\theta\). Therefore
\[
\overline{\chi\mathbb C[S]}
=\{f\in\mathcal H_\theta:f_n=0\ (n\in Z_\theta)\}.
\tag{R46}
\]
Orthogonal coordinate restriction gives the isometric quotient
\[
\mathcal H_\theta/\overline{\chi\mathbb C[S]}
\simeq
\left(\mathbb C^{Z_\theta},
\ \|(v_n)\|^2=\sum_{n\in Z_\theta}\nu_{n,\theta}|v_n|^2\right).
\tag{R47}
\]
The original coefficient comparison is exactly
\[
E\longrightarrow\mathbb C^{Z_\theta},\qquad
[P]\longmapsto(P(S_{n,\theta}))_{n\in Z_\theta}.
\tag{R48}
\]
Lagrange interpolation at the distinct \(S_{n,\theta}\) proves surjectivity: the coordinate polynomial is the product of
\((S-S_{m,\theta})/(S_{n,\theta}-S_{m,\theta})\) over \(m\ne n\).
Vanishing at all these points is equivalent to divisibility by \(p_\theta\). Thus its exact kernel is \((p_\theta)/(\chi)\), preserving the original higher multiplicities in \(\chi\). At a sampled root of multiplicity \(m\), only its scalar value survives; its maximal ideal of dimension \(m-1\) remains in this kernel.

### The exact selected-root mass, including the leading coefficient

For \(k\ge2\), (R8)'s positivity proves \(I_\theta=\mathbb Z\).
For \(k=1\), the original cyclic algebra is \(\mathbb C[S]/(h)\). A polynomial annihilates multiplication by \(S\) exactly when it lies in \((h)\), as is seen by applying it to the unit. Hence
\[
(\chi_{h,1})=(h).
\]
Equality of the literal generators is used only when their original convention already makes both the same monic polynomial; it is not needed here.

Write the unchanged packet with its actual leading coefficient:
\[
h(S)=a_h\prod_{\rho\in Z_h}(S-\rho)^{m_\rho},\qquad
a_h\ne0,\qquad m_\rho=\operatorname{ord}_\rho g.
\]
Full-order cancellation gives
\[
\left(\frac gh\right)(\rho)
=\frac{g^{(m_\rho)}(\rho)}{h^{(m_\rho)}(\rho)}
=\frac{g^{(m_\rho)}(\rho)}
{a_h\,m_\rho!\prod_{\sigma\ne\rho}(\rho-\sigma)^{m_\sigma}}
\ne0.
\tag{R49}
\]
For a sampled root \(\rho=1/2+iu_{n,\theta}\), its actual mass is therefore
\[
\boxed{
\nu_{n,\theta}
=\frac1L
\left|\frac{g^{(m_\rho)}(\rho)}{h^{(m_\rho)}(\rho)}\right|^2
=
\frac{|g^{(m_\rho)}(\rho)|^2}
{L|a_h|^2(m_\rho!)^2
\prod_{\sigma\ne\rho}|\rho-\sigma|^{2m_\sigma}}
>0.
}
\tag{R50}
\]
This retains \(g=2\xi\), every derivative order, the leading coefficient, and \(1/L\). Consequently no sampled root in the printed H64 is removed by a zero weight in the marked \(k=1\) source. Equations (R47)–(R50) prove H64 at every admitted \(k\ge1\), with its full weighted metric. For an unrelated nonnegative sampled density the positive-support restriction would remain essential.

### Explicit measurable field and the almost-everywhere zero map

For each phase use the isometric embedding
\[
(v_n)_{n\in Z_\theta}
\longmapsto
(\mathbf1_{n\in Z_\theta}\sqrt{\nu_{n,\theta}}\,v_n)_{n\in\mathbb Z}
\quad\hbox{into }\ell^2(\mathbb Z).
\tag{R51}
\]
Its image is the range of the diagonal orthogonal projection with entries
\[
\mathbf1_{\nu_{n,\theta}>0}\,
\mathbf1_{\chi(k/2+i(2\pi n+\theta)/L)=0}.
\]
Each entry is measurable, so this is an explicit measurable Hilbert field.
A nonzero fibre requires a root \(\rho\) of \(\chi\) with
\[
\operatorname{Re}\rho=k/2,\qquad
\theta\equiv L\operatorname{Im}\rho\pmod{2\pi}.
\]
Each root determines at most one phase in \([0,2\pi)\), and then one integer \(n\). There are therefore at most \(q\) exceptional phases. Every section of this field vanishes outside a finite set, and its squared norm
\[
\int_0^{2\pi}\sum_{n\in Z_\theta}
\nu_{n,\theta}|v_n(\theta)|^2\,\frac{d\theta}{2\pi}
\]
is zero. The direct integral is the zero Hilbert space, and the map from \(E\) induced by (R48) has kernel all of \(E\).

Each individual exceptional evaluation map (R48) still exists and has the positive masses (R50). The a.e. quotient does not identify those pointwise maps with source absence. Its split lift maps \((\ell,v)\) to \((\ell,0)\), while \(\tau\) remains \(\tau\). This proves the completion claim with its actual maps and kernels, without exchanging it with the source unitary (R5) or the finite quotient (R9).

## 10. Action, residue coefficient, and the unchanged period reference

### The action and its actual boundary map

Regard \(C_{N,\theta}:E\to P_N\) also as a map to \(P_{N+1}\) through the literal polynomial inclusion. Since \(J_{N+1}(SP)=A J_NP\), its two sections obey
\[
J_{N+1}(SC_{N,\theta}-C_{N,\theta}A)=A-A=0.
\]
The kernel of \(J_{N+1}\) is \(\chi P_{N+1-q}\). Multiplication by the fixed monic \(\chi\) is injective, so there is one and only one polynomial map
\[
Q_{N,\theta}:E\longrightarrow P_{N+1-q},\qquad
SC_{N,\theta}-C_{N,\theta}A=\chi Q_{N,\theta}.
\tag{R52}
\]
At \(N=q-1\), this conclusion still uses \(P_0\), rather than discarding the new action relation at the raised cutoff.

Write the actual half-density source at degree \(N\) as \(\Psi_N=U_k V_h^{(k)}|_{P_N}\), and define the representative map and its relation image by
\[
R_{N,\theta}=\mathcal Z_{L,\theta}\Psi_N C_{N,\theta},
\qquad
\mathscr B_{N,\theta}
=\mathcal Z_{L,\theta}\Psi_{N+1}(\chi Q_{N,\theta}).
\tag{R53}
\]
The original tensor primitive in Section 2 maps to the second expression. The differential identity \(U_kD^{(k)}=(-\partial_r+k/2)U_k\), and differentiation of the convergent regular-source periodization, prove H54 with this precise map:
\[
D_{L,\theta}R_{N,\theta}
=R_{N,\theta}A+\mathscr B_{N,\theta}.
\]
These operations are on the admitted regular sources. A bounded differentiation map on all of the \(L^2\) completion is not asserted.

On the twisted \(H^1\) domain
\[
\{f\in H^1([0,L];\mathcal K):
f(L)=e^{-i\theta}f(0)\},
\]
the two endpoint inner products are equal, since both factors acquire the same unit-modulus multiplier. Thus integration by parts gives
\[
\langle D_{L,\theta}f,g\rangle+
\langle f,D_{L,\theta}g\rangle=k\langle f,g\rangle.
\]
Inserting (R53), and retaining \(R_{N,\theta}^*R_{N,\theta}=G_{N,\theta}\), yields exactly
\[
A^*G_{N,\theta}+G_{N,\theta}A-kG_{N,\theta}
=-(R_{N,\theta}^*\mathscr B_{N,\theta}
+ \mathscr B_{N,\theta}^*R_{N,\theta}).
\tag{R54}
\]
The phase unitary, finite character maps, and explicit primitive maps of Sections 2, 3, and 8 carry this equality. No vanishing of either cross term follows from it alone.

For the inherited holomorphic period matrix, put \(B(t)=A+t\mathcal R\), with \(u\ne0\) fixed. Differentiating \(\Pi'=-\Pi B/u\) with respect to the original \(t\) gives
\[
\Pi''=\frac{\Pi B^2}{u^2}-\frac{\Pi\mathcal R}{u}.
\]
Consequently
\[
u^2\Pi''+ku\Pi'+u\Pi\mathcal R
=\Pi(B^2-kB),
\tag{R55}
\]
which verifies all terms and signs in H56.

### Perfect residue form and rank one on every proper invariant constituent

In the ordered basis \(e_i=[S^i]\), \(0\le i<q\), define
\[
\ell([P])=[S^{q-1}]\operatorname{rem}_\chi P,\qquad
\beta(x,y)=\ell(xy).
\]
For \(i+j<q-1\), \(\beta(e_i,e_j)=0\); for \(i+j=q-1\), it equals \(1\). Reverse the columns of this Gram matrix. The result is triangular with diagonal \(1\), so
\[
\det\beta=(-1)^{q(q-1)/2}.
\tag{R56}
\]
In particular, the rows \(\ell A^j\), \(0\le j<q\), form a basis of \(E^*\). Since the columns \(A^i1_E=e_i\) form a basis of \(E\), the \(q^2\) operators
\[
A^i\mathcal R A^j=e_i\otimes(\ell A^j)
\]
form a basis of \(\operatorname{End}_{\mathbb C}(E)\), not merely a spanning collection. This argument uses the actual quotient algebra and allows every repeated-root multiplicity in \(\chi\).

Let \(\iota:F\hookrightarrow E\) be nonzero, proper, and \(A\)-invariant, and let \(\pi:E\to E/F\) be the quotient map. If \(1_E\) belonged to \(\iota F\), invariance and cyclicity would force all \(e_i\) into \(\iota F\), contrary to properness. Thus \(\pi1_E\ne0\). If \(\ell_F=\ell\iota\) vanished, then \(\ell A^j\iota=\ell\iota A_F^j=0\) for every \(j\). The basis of \(E^*\) above would imply \(\iota F=0\), contrary to nonzeroness. Hence
\[
\pi\mathcal R\iota=(\pi1_E)\otimes\ell_F
\tag{R57}
\]
has rank exactly one. This proves H57–H58 with both nonzero factors.

For a positive metric \(M\), let
\[
P_F^M=\iota(\iota^*M\iota)^{-1}\iota^*M,\qquad
r_M=(1-P_F^M)1_E.
\]
Orthogonality proves
\[
\min_{f\in F}\|1_E-\iota f\|_M^2=r_M^*Mr_M>0.
\]
The squared dual norm of \(\ell_F\) is
\(\ell_F(\iota^*M\iota)^{-1}\ell_F^*>0\).
Their product is precisely H59. If \(aG\preceq M\preceq bG\), with \(a,b>0\), minimizing the first inequalities gives factors \(a,b\), while restriction and inversion give factors \(1/b,1/a\) for the second. Therefore
\[
\frac ab\,\mathfrak c_F(G)
\le\mathfrak c_F(M)\le
\frac ba\,\mathfrak c_F(G).
\tag{R58}
\]
Taking \(M=\overline G_N\), \(G=G_N\), \(a=1-\eta^2\), \(b=1\) proves H60. This is a comparison of the coefficient at the two stated metrics. It is not an interchange of this nonlinear coefficient with phase averaging.

### Curvature and the exact reference determinant

On the locus of the inherited period construction where \(\Pi(t)\) is holomorphic and invertible, put
\[
H(t)=\Pi(t)^*\Pi(t),\quad
X(t)=\Pi(t)\iota,\quad
H_F(t)=X(t)^*X(t),\quad
P_X=XH_F^{-1}X^*.
\]
Here the derivative and complex conjugate derivative treat \(t,\bar t\) independently. The usual product rule can be written without omitting a term:
\[
\partial_t\log\det H_F
=\operatorname{Tr}(H_F^{-1}X^*X'),
\]
\[
\partial_{\bar t}\partial_t\log\det H_F
=\operatorname{Tr}
\!\left(H_F^{-1}X'^*(1-P_X)X'\right).
\tag{R59}
\]
Indeed, \(\partial_{\bar t}H_F=X'^*X\), so differentiating the inverse in the first formula gives the subtractive term
\(-\operatorname{Tr}(H_F^{-1}X'^*XH_F^{-1}X^*X')\), and differentiating \(X^*\) gives the positive term
\(\operatorname{Tr}(H_F^{-1}X'^*X')\). Their difference is (R59).

The invariant inclusion satisfies \(A\iota=\iota A_F\). The differential equation therefore gives
\[
X'=-\frac1u XA_F-\frac tu\,\Pi1_E\,\ell_F,\qquad
(1-P_X)X'=-\frac tu(1-P_X)\Pi1_E\,\ell_F.
\]
The squared norm of the latter normal vector is the quotient norm of \(1_E\) for \(H\):
\[
\|(1-P_X)\Pi1_E\|^2
=\min_{f\in F}\|\Pi(1_E-\iota f)\|^2.
\]
Taking the trace in (R59) now proves exactly H61:
\[
\partial_{\bar t}\partial_t\log\det(\iota^*H(t)\iota)
=\frac{|t|^2}{|u|^2}\mathfrak c_F(H(t)).
\tag{R60}
\]

Along the original real \(t\) axis, with the original real \(u>0\), the equation at \(t=0\) is \(X'=-XA_F/u\). Hence
\[
\left.\frac d{dt}\log\det H_F(t)\right|_{t=0}
=-\frac{2}{u}\operatorname{Re}\operatorname{Tr}A_F.
\]
The reference determinant \(\det(\iota^*G_N\iota)\) in H62 is positive and independent of \(t\). It remains inside the ratio and has derivative zero. Thus
\[
-u\left.\frac d{dt}\log
\frac{\det(\iota^*H(t)\iota)}
{\det(\iota^*G_N\iota)}\right|_{t=0}-k\dim F
=2\operatorname{Re}\operatorname{Tr}A_F-k\dim F.
\tag{R61}
\]
The proof does not replace \(G_N\) by an identity metric or by a phase metric.

Finally, for H63 retain the original potential constant and translation maps:
\[
\Pi_a=f_a\Pi C_a,\qquad
f_a=\exp\!\left(\frac{-\Phi(-a)-ta}{u}\right),\qquad
C_aA_aC_a^{-1}=A+aI.
\]
Take the transported inclusion \(\iota_a=C_a^{-1}\iota\), so that
\(\Pi_a\iota_a=f_a\Pi\iota\). If \(p=\dim F\), the determinant of its Gram matrix is \(|f_a|^{2p}\det H_F\). A different fixed frame on the transported \(F\) contributes only its constant absolute determinant squared. Since \(f_a\) is nonzero and holomorphic, \(\partial_{\bar t}\partial_t\log|f_a|^{2p}=0\), which proves the asserted curvature invariance with an explicit constituent map. For real \(u>0\),
\[
\frac d{dt}\log|f_a|^{2p}
=-\frac{2p}{u}\operatorname{Re}a.
\]
Multiplication by \(-u\) in the trace observable therefore adds \(2p\operatorname{Re}a\), exactly as H63 states. The marked fibre used in this packet is \(a=0\); this calculation does not alter it.

## 11. Equation coverage and final disposition

The source contains 73 labelled displays: H1–H66 together with H49a–H49g. The following table accounts for every label. Line numbers refer to the byte-pinned NOTE.md in Section 1.

| Source labels | Source lines | Proof in this review | Disposition |
| --- | ---: | --- | --- |
| H1 | 18 | Section 5 | Correct; constant is sharp even for an analytic full-circle family. |
| H2–H8 | 33–87 | Section 2 | Original quotient, support, reference, and tensor primitive maps retained; source analytic existence remains the explicitly identified inherited construction. |
| H9–H17 | 102–174 | Section 3 | Correct; fixed-phase evaluation is on regular sources, and the full \(L^2\) unitary is a direct-integral statement. |
| H18–H23 | 187–236 | Section 8 | Correct with exact \(1/\sqrt m\), \(1/m\), deck signs, Laurent inverse, and descent inverse. |
| H24–H28 | 252–286 | Section 4 | Correct with the complete minimization defect and original section maps. |
| H29–H31 | 300–318 | Section 8 | Correct as coefficient cochain maps; their metric adjoint is the separately displayed weighted map. |
| H32–H38 | 334–387 | Section 5 | Correct; the inverse chord and averaged block proof give the stated \(\eta^2\) bound. |
| H39–H41 | 402–419 | Section 6 | Correct with both exponential weights and \(e^{aL}-1\). |
| H42–H49 | 433–491 | Section 6 | Correct including \(q\), every determinant factor, and the finite-mean centering. |
| H49a–H49g | 505–559 | Section 7 | Correct on the selected closed strip satisfying \(d_s<1\); Fourier and two-sided alias tails retain the stated budget. |
| H50–H52 | 570–587 | Section 7 | Correct with the exact \(2\pi/L\), \(J-1\), \(2p-1\), and lower-metric transport. |
| H53–H56 | 598–625 | Section 10 | Correct with the degree-raising relation primitive, twisted boundary domain, and \(u\Pi\mathcal R\) term. |
| H57–H63 | 637–696 | Section 10 | Correct including repeated roots, the unchanged \(G_N\) reference, and the exact translation factor. |
| H64 | 710 | Section 9 | Correct for the marked source; positive selected-root mass and a measurable direct-integral model are now explicit. |
| H65–H66 | 727–736 | Section 5 | Correct with the literal mass \(7\); Section 5 also supplies a smooth analytic full-circle calibration. |

Two domain clarifications should be made whenever these statements are propagated. First, pointwise phase summation is a map on the regular source domain; it does not extend boundedly to a single chosen phase on the entire real-line \(L^2\) space. Second, the complex inverse assertion at source line 527 is valid throughout each selected closed strip \(|\operatorname{Im}z|\le s\) with \(d_s<1\), and a neighborhood of that strip. It should not be read as an inverse assertion on the entire, possibly larger, correlation-convergence strip \(|\operatorname{Im}z|<aL\).

No numerical reruns, checker executions, Lean runs, broad source scans, raw-packet edits, or new primary-source claims were used in this review. The finite algebra, minimization, analytic extension, Fourier estimates, descent maps, and completion argument above are proofs. They do not purport to certify an uncomputed arithmetic matrix or supply a numerical enclosure for an unevaluated sample.
