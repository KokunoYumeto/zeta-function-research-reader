# A global retraction of the original theta complex over the tau base

Owner-directed continuation of Zeta PR #9, 12 September 2026. New derivations are submitted as research proofs for review, not as Lean-certified analytic theorems.

## 0. Fixed source, result, and provenance

The base is PR #9 at `8f99b94d306c3b1aaa817d52c57fa6fd298d511c`; its chain-descent note has Git blob `86db838e79d10a8fe7d4376303706c4ea64570a1`. Its source and the owner's derived SplitZero attachment remain the inputs. This continuation constructs an inverse on the entire original theta image, not only on a chosen finite spectral packet.

Retain

$$G(R)=\{\tau\}\sqcup\{r^\bullet:r\in R\},\qquad e_R=0_R^\bullet,$$

$$\mathfrak b_\tau=\operatorname{Spec}\mathbf F_{1,\tau},\qquad
\begin{array}{ccc}G(\mathbb Z)&\xrightarrow{G(j)}&G(\mathbb C)\\
p_{\mathbb Z}\downarrow&&\downarrow p_{\mathbb C}\\
\mathbb Z&\xrightarrow{j}&\mathbb C.\end{array}\tag{1}$$

The first vertical target is still infinite. The geometric base, the original additive laws, and the arithmetic quotient are unchanged. The auxiliary cutoffs below are parameters of an explicit continuous representative map; they do not change an Euler factor, the theta relation space, or the completed zeta function.

**Result.** For every pair of the cutoffs specified in section 3 there is an explicitly constructed continuous complex-linear map

$$\Lambda_{\alpha,\beta}:\mathscr B\longrightarrow V,\qquad
\boxed{\Lambda_{\alpha,\beta}\Theta=\operatorname{id}_V.}\tag{2}$$

Consequently the actual image $\Theta V$ is closed and complemented in the stated strong-Schwartz topology. The original quotient $Q=\mathscr B/\Theta V$ is Hausdorff. The note constructs its global section, the full supported cochain homotopy, the exact change of the finite sections in #9, its continuous dual sequence, and the completed tensor powers. The proof does not assume RH, simplicity of any zero, or vanishing of the separate balanced-Mellin kernel.

Spectral realizations on nuclear Frechet spaces are prior work, notably R. Meyer, arXiv:math/0412277. That paper's abstract was consulted for scope, but no theorem from an unread body of that paper is imported. The proof below is given for the workbench's precise spaces. No global novelty claim is made.

## 1. Spaces and all transforms

Let

$$V=\{\phi\in\mathcal S(\mathbb R):\phi(-x)=\phi(x),\ \phi(0)=0,\ \int_{\mathbb R}\phi(x)\,dx=0\},$$

$$\mathscr B=\{F\in C^\infty(\mathbb R_{>0}):
p_{b,k}(F):=\sup_{x>0}x^b|D^kF(x)|<\infty
\text{ for every }b\in\mathbb Z,\ k\ge0\},\qquad D=-x\partial_x.\tag{3}$$

These seminorms give $\mathscr B$ its Frechet topology; under $x=e^y$ they are the weighted uniform derivative seminorms on smooth functions of $y$. Completeness follows by uniform convergence on compact sets of every derivative, followed by the weighted bounds. $V$ has its closed-subspace Schwartz topology.

The original maps are

$$\Theta\phi(x)=\sum_{n\in\mathbb Z\setminus\{0\}}\phi(nx)
=2\sum_{n\ge1}\phi(nx),$$

$$\mathcal F\phi(\xi)=\int_{\mathbb R}\phi(x)e^{-2\pi i x\xi}\,dx,\qquad
\mathcal F^{-1}u(x)=\int_{\mathbb R}u(\xi)e^{2\pi i x\xi}\,d\xi,$$

$$JF(x)=x^{-1}F(1/x),\qquad
\mathcal MF(s)=\int_0^\infty F(x)x^s\,\frac{dx}{x}.\tag{4}$$

Poisson summation, with both source moments zero, gives

$$\Theta\mathcal F=J\Theta,\qquad J^2=1,\qquad D J=J(1-D).\tag{5}$$

The theta sum and each derivative converge absolutely on closed subsets of $x>0$. At infinity, Schwartz estimates give all $p_{b,k}$ bounds. At zero use (5) and the same estimates on $\widehat\phi$. This proves continuity $\Theta:V\to\mathscr B$. Also $J$ is continuous on $\mathscr B$: $p_{b,k}(JF)$ is bounded by the binomial sum of $p_{1-b,j}(F)$, $0\le j\le k$.

The original complex is $C_+=[V\xrightarrow\Theta\mathscr B]$ in degrees $0,1$, over $A=\mathbb C[t]$ with $t$ acting as $D$. The two-leg tau chart retains $C_{+-}=[V^2\to\mathscr B]$ with differential $\Theta(\phi-\widehat\psi)$ and source action $(D,1-D)$.

## 2. Arithmetic inversion on the two exterior regions

Let $\mu$ be the ordinary Mobius function, characterized by

$$\sum_{d\mid n}\mu(d)=\begin{cases}1,&n=1,\\0,&n>1.\end{cases}$$

For $F\in\mathscr B$ define, for $x\ne0$,

$$\boxed{\mathcal U F(x)=\frac12\sum_{n\ge1}\mu(n)F(n|x|).}\tag{6}$$

The factor $1/2$ is the inverse of the full nonzero-integer theta sum in (4). The map is complex-linear into smooth even functions on $\mathbb R\setminus\{0\}$. It is not asserted to be smooth at zero for arbitrary $F$.

Here are the required estimates. For $j\ge0$, let $P_j(T)=(-1)^jT(T+1)\cdots(T+j-1)$, with $P_0=1$. Then $x^j\partial_x^j=P_j(D)$. If $C_{N,j}(F)$ is the sum of the $p_{N,k}(F)$ weighted by the absolute coefficients of $P_j$, then, for $x>0$ and integer $N>1$,

$$|\partial_x^j\mathcal U F(x)|
\le\frac12\zeta(N)C_{N,j}(F)x^{-N-j}.\tag{7}$$

Indeed each summand is bounded by $C_{N,j}(F)n^{-N}x^{-N-j}/2$. This proves convergence of every derivative uniformly for $|x|\ge\delta>0$, and gives rapid decay there. It also proves continuity of the cut-off exterior maps used below.

For every $\phi\in V$,

$$\boxed{\mathcal U\Theta\phi(x)=\phi(x),\qquad
\mathcal U J\Theta\phi(x)=\widehat\phi(x)\quad(x\ne0).}\tag{8}$$

For the first equality the double series is absolutely convergent for each $x>0$: its absolute value is bounded by $\sum_{k\ge1}d(k)|\phi(kx)|$, which is finite by Schwartz decay. Rearrange by $k=mn$ and use the displayed divisor identity. Evenness handles negative $x$. The second equality follows from (5) and the first equality applied to $\widehat\phi\in V$.

In the split lift, every $\mu(n)$ is the supported integer $\mu(n)^\bullet$, including $\mu(n)=0$. A convergent sum within a specified active fibre begins at that fibre's zero and is taken in that fibre's vector-space topology. Formula (8) thus lifts to a support-preserving equality. A computed cancellation is not external absence.

## 3. The reconstruction operator, with the strict contraction proved

Choose and retain real, even $\alpha,\beta\in C_c^\infty(\mathbb R)$ satisfying $0\le\alpha,\beta\le1$ and equal to $1$ on neighborhoods of zero. Their supports and all values are part of the auxiliary data. Work on $\mathcal H=L^2(\mathbb R,dx)$ with the Fourier convention in (4).

Define bounded operators

$$A_\alpha=M_\alpha,\qquad
B_\beta=\mathcal F^{-1}M_\beta\mathcal F,\qquad
T_{\alpha,\beta}=A_\alpha B_\beta.\tag{9}$$

**Lemma.** $T_{\alpha,\beta}$ is compact and $c_{\alpha,\beta}:=\|T_{\alpha,\beta}\|<1$.

**Proof.** Its kernel is $\alpha(x)\check\beta(x-y)$, whose squared integral is $\|\alpha\|_2^2\|\beta\|_2^2$. Hence it is Hilbert-Schmidt. Both factors are contractions. If the norm were $1$, compactness would supply a unit vector $f$ attaining it. Equality in

$$\|A_\alpha B_\beta f\|\le\|B_\beta f\|\le\|f\|$$

forces $\widehat f$ to be supported where $\beta=1$; there $B_\beta f=f$. The first equality forces $f$ to be supported where $\alpha=1$. Both supports are compact. The inverse Fourier transform of compactly supported $\widehat f\in L^2$ is entire, by differentiation under its finite-interval integral. Its continuous restriction agrees with the compactly supported $f$, so it vanishes on an open real interval and hence identically. This contradicts $\|f\|=1$. Thus $c_{\alpha,\beta}<1$.

Consequently the exact Neumann inverse exists:

$$\boxed{(1-T_{\alpha,\beta})^{-1}=\sum_{k\ge0}T_{\alpha,\beta}^k,
\qquad\|(1-T_{\alpha,\beta})^{-1}\|\le\frac1{1-c_{\alpha,\beta}}.}\tag{10}$$

No uniform bound as the cutoffs vary is claimed. In particular the gap $1-c_{\alpha,\beta}$ is retained, not replaced by a positive universal constant.

The operator $T_{\alpha,\beta}$ maps $L^2$ continuously to the Schwartz space. For each derivative, compact Fourier support and Cauchy-Schwarz bound $\partial^j B_\beta f$ uniformly by a constant times $\|f\|_2$; multiplication by the smooth compactly supported $\alpha$ gives every Schwartz seminorm.

Define the two exterior data and their combination:

$$a_F=(1-\alpha)\mathcal U F,\qquad
b_F=(1-\beta)\mathcal U JF,$$

$$Y_{\alpha,\beta}F=a_F+\alpha\mathcal F^{-1}b_F.\tag{11}$$

The exterior terms are extended by zero near the origin, where their cutoff is identically zero. Estimates (7) prove that both are even Schwartz functions and depend continuously on $F$. Therefore $Y:\mathscr B\to\mathcal S(\mathbb R)^{\mathrm{even}}$ is continuous.

Put

$$\Phi_{\alpha,\beta}F=(1-T_{\alpha,\beta})^{-1}Y_{\alpha,\beta}F.\tag{12}$$

This initially defines an $L^2$ vector, but the identity $\Phi F=YF+T\Phi F$ proves it is Schwartz. If $q$ is any Schwartz seminorm and $q(Tu)\le C_q\|u\|_2$, then

$$q(\Phi F)\le q(YF)+\frac{C_q}{1-c_{\alpha,\beta}}\|YF\|_2.\tag{13}$$

This is an explicit continuity estimate. Both sides are even because the cutoff operators preserve parity.

For $F=\Theta\phi$, equations (8) give

$$Y\Theta\phi=(1-A_\alpha)\phi+A_\alpha(1-B_\beta)\phi
=(1-T_{\alpha,\beta})\phi,$$

hence

$$\boxed{\Phi_{\alpha,\beta}\Theta\phi=\phi.}\tag{14}$$

## 4. Keep both original moment conditions

For arbitrary $F$, (12) need not satisfy the two source moments. The correction is the following specified projection, not an alteration of $V$.

Retain

$$\gamma_0(x)=e^{-\pi x^2},\qquad
\gamma_2(x)=2\pi x^2e^{-\pi x^2}.$$

Their moment columns $(\phi(0),\int\phi)$ are $(1,1)$ and $(0,1)$. Define

$$\mathsf m(\phi)=\bigl(\phi(0),\int_{\mathbb R}\phi\bigr),\qquad
j_0(a,b)=a\gamma_0+(b-a)\gamma_2,$$

$$P_V\phi=\phi-j_0\mathsf m(\phi)
=\phi-\phi(0)\gamma_0-\left(\int\phi-\phi(0)\right)\gamma_2.\tag{15}$$

Then $\mathsf m j_0=1$, $P_V^2=P_V$, $\operatorname{im}P_V=V$, and $P_V|_V=1$. All maps are continuous.

The promised map is

$$\boxed{\Lambda_{\alpha,\beta}=P_V(1-T_{\alpha,\beta})^{-1}Y_{\alpha,\beta}:\mathscr B\to V.}\tag{16}$$

Equation (14) and $P_V|_V=1$ prove (2). The discarded moment vector has the recorded map $\mathsf m\Phi:\mathscr B\to\mathbb C^2$ and the explicit correction $j_0\mathsf m\Phi$. It vanishes on the actual theta image. No endpoint constant was absorbed into the zeta function.

## 5. The full quotient is closed and has a continuous section

Write $\Lambda=\Lambda_{\alpha,\beta}$, and define

$$P_\Theta=\Theta\Lambda,\qquad K=1_{\mathscr B}-\Theta\Lambda.\tag{17}$$

Direct substitution gives

$$P_\Theta^2=P_\Theta,\quad K^2=K,\quad
\ker K=\Theta V,\quad\operatorname{im}K=\ker\Lambda.\tag{18}$$

Since $K$ is continuous, its kernel is closed. Thus $Q=\mathscr B/\Theta V$ with its actual quotient topology is Frechet and Hausdorff. If $q:\mathscr B\to Q$ is the original quotient map, the continuous section is

$$\boxed{s:Q\to\mathscr B,\qquad s[F]=KF,\quad qs=1,\quad\Lambda s=0.}\tag{19}$$

The explicit topological direct-sum isomorphism is

$$\boxed{V\oplus Q\xrightarrow{\sim}\mathscr B,
\quad(\phi,u)\mapsto\Theta\phi+su,
\quad F\mapsto(\Lambda F,qF).}\tag{20}$$

For a convergent sequence $\Theta\phi_n\to F$ in $\mathscr B$, one can check the closedness without any abstract theorem: $\phi_n=\Lambda\Theta\phi_n\to\Lambda F$ in $V$, so $F=\Theta\Lambda F$ by continuity of theta.

This computes the earlier Hausdorff arrow:

$$Q^{\mathrm{alg}}=\mathscr B/\Theta V\longrightarrow
Q^{\mathrm H}=\mathscr B/\overline{\Theta V},\qquad[F]\mapsto[F],\tag{21}$$

as an isomorphism with zero amplitude kernel. It does not say the map from $Q$ into its product of spectral jets is injective. The latter map and the balanced analytic map still have their own named kernels:

$$Q\to\prod_\rho\mathcal O_\rho/(g),\qquad
\mathcal O\otimes_{\mathbb C[t]}Q\xrightarrow{\beta}\mathcal O/(g).$$

No claim that $\mathcal R_\infty$ or $\ker\beta$ vanishes is inferred from (21).

### Smaller admitted relations

For any specified subspace $W\subset V$, retain

$$Q_W=\mathscr B/\Theta W\longrightarrow Q,\qquad
\ker=\Theta V/\Theta W\cong V/W.\tag{22}$$

The isomorphism sends $[\phi]\mapsto[\Theta\phi]$. It is algebraic for arbitrary $W$; when $W$ is closed, (20) makes it a topological isomorphism onto the kernel. The pullback of the global section has the representative relation kernel in (22); the full-source result is not silently asserted with $W$ in place of $V$.

## 6. Perform the original internal quotient and synchronization

On the single-leg map, or a fixed-index diagram of that same map, the split lifts are

$$\widetilde\Theta(\lambda,\phi)=(\lambda,\Theta\phi),\quad
\widetilde\Lambda(\lambda,F)=(\lambda,\Lambda F),\quad
\widetilde K(\lambda,F)=(\lambda,KF).\tag{23}$$

They preserve external bottom and commute with scalar reflection. In particular

$$\widetilde K\widetilde\Theta(\lambda,\phi)=(\lambda,0_{\mathscr B})=z_{V,\mathscr B}(\lambda,\phi).$$

Here $z_{V,\mathscr B}$ is the label-preserving zero map from the source fibre to the target fibre. The mixed chart, whose minus restriction is $-\Theta\mathcal F$, is treated separately by the explicit maps (25)-(28), without changing that restriction. The actual chart has zero bottom fibre; a general nonzero bottom fibre is acted on by its stated linear map, rather than identified with the single global zero.

The supported image projection is idempotent, and the quotient map is exactly the coequalizer of the theta relation inclusion and its supported-zero companion. The implementation's universal property applies against all split-linear targets. A theta boundary is sent to $e_\lambda=(\lambda,0)$; it is not sent to external absence.

For the single-leg complex there is an actual continuous contraction

$$C_+\ \xrightleftharpoons[s]{q}\ Q[-1],\qquad H^1=\Lambda,$$

$$\boxed{q s=1,\qquad 1_{C_+}-s q=dH+Hd.}\tag{24}$$

In degree zero this is $\Lambda\Theta=1_V$; in degree one it is $\Theta\Lambda=1-K$. In split notation the subtraction means addition of the supported scalar $(-1)^\bullet$ times the second map. It yields the correct labelled zero wherever the amplitude vanishes.

For the two-leg chart set $H_0=V[0]\oplus Q[-1]$ with zero differential, and define

$$p_L^0(\phi,\psi)=\psi,\quad p_L^1=q,\qquad
i^0(\psi)=(\widehat\psi,\psi),\quad i^1=s,$$

$$H_L^1(F)=(\Lambda F,0).\tag{25}$$

Then $p_L i=1$, and $1-i p_L=dH_L+H_Ld$. The degree-zero identity is $(\phi,\psi)-(\widehat\psi,\psi)=(\phi-\widehat\psi,0)$.

The other leg gives

$$p_R^0(\phi,\psi)=\widehat\phi,\quad p_R^1=q,\qquad
H_R^1(F)=(0,-\widehat{\Lambda F}).\tag{26}$$

It obeys $1-i p_R=dH_R+H_Rd$. Their homotopies differ by

$$\boxed{H_L^1F-H_R^1F=(\Lambda F,\widehat{\Lambda F}),}\tag{27}$$

the actual joint degree-zero cycle, which is retained.

On the complete original support diagram, use literal multiplication by $E_{\mathrm{sync}}=(1,e)$ in degree zero and the source's active-label-to-joint map in degree one:

$$\mathfrak r^0(a,b)=(a+eb,b+ea),\qquad
\mathfrak r^1(\lambda,F)=(\{+,-\},F)\quad(\lambda\ne\bot).$$

The absent input remains absent. The original differential obeys $d\mathfrak r=\mathfrak r d$ and $\mathfrak r^2=\mathfrak r$. Consequently (25) lifts to the fully typed equation

$$\boxed{\mathfrak r-\widetilde i\widetilde p_L\mathfrak r
=\widetilde d\,\widetilde H_L+\widetilde H_L\widetilde d,}\tag{28}$$

where $\widetilde H_L(\lambda,F)=(\{+,-\},(\Lambda F,0))$ for each active label. The right-leg equation is analogous with (26). The original mask is recorded with the injection $x\mapsto(\operatorname{supp}x,\mathfrak r x)$ already proved for this chart. Neither synchronization nor the contraction identifies the three supported origins with $\tau$.

## 7. Global scaling defects, and their agreement with the finite extensions

Let $U_aF(x)=F(x/a)$, $a>0$, and denote its induced continuous action on $Q$ by $\overline U_a$. The section (19) gives a global continuous boundary map

$$\boxed{k_a=\Lambda U_a s:Q\to V,\qquad
U_a s-s\overline U_a=\Theta k_a.}\tag{29}$$

The proof applies $K+\Theta\Lambda=1$ to $U_as$, then uses $qU_as=\overline U_a$. Therefore

$$k_{ab}=U_a k_b+k_a\overline U_b,\qquad k_1=0.\tag{30}$$

The same calculation works for $D$ and compactly supported multiplicative convolution, with $k_D=\Lambda D s$. In the explicit coordinates (20),

$$\boxed{U_a|_{\mathscr B}=\begin{pmatrix}U_a|_V&k_a\\0&\overline U_a\end{pmatrix},
\qquad D|_{\mathscr B}=\begin{pmatrix}D|_V&k_D\\0&D_Q\end{pmatrix}.}\tag{31}$$

Thus the topological splitting is not substituted for an equivariant splitting. Equation (29) is the precise comparison between them.

For two cutoff choices, let $s_0,s_1$ be their sections and set $b_{10}=\Lambda_0s_1:Q\to V$. Then

$$s_1-s_0=\Theta b_{10},\qquad
k_a^{(1)}=k_a^{(0)}+U_ab_{10}-b_{10}\overline U_a.\tag{32}$$

All dependence on the chosen representative map is carried by this displayed coboundary. No canonical cutoff or average over choices is declared.

### Restrict back to PR #9 without changing its extension class

Use its existing maps $s_Z:E_Z\to\mathscr B$, $\sigma_Z=q s_Z:E_Z\to Q$, and $J_Z:\mathscr B\to E_Z$. Put $b_Z=\Lambda s_Z$. The new continuous representative of the same finite arithmetic class is

$$s_Z^{\mathrm{new}}=s\sigma_Z=K s_Z=s_Z-\Theta b_Z.\tag{33}$$

If $P(D)s_Z-s_ZM_P=\Theta k_{P,Z}$, direct substitution gives

$$k_{P,Z}^{\mathrm{new}}=k_{P,Z}-P(D)b_Z+b_ZM_P.\tag{34}$$

For $P=h_Z$, this changes the source boundary by $-h_Z(D)b_Z$. It is zero in $V/h_Z(D)V$, so the extension class remains exactly

$$\varepsilon_Z=j_{h_Z}(h_Z/g),\qquad g=2\xi.\tag{35}$$

The polynomial residue form still becomes the arithmetic one by $M_{\varepsilon_Z}$; its Jacobian contraction remains $M_{\varepsilon_Z}M_{j_h g'}$. No unit, derivative, sign, or factor of $2$ is changed.

The two finite cochain projectors differ by the explicit homotopy $-b_ZJ_Z$ in degree minus one. Their finite-rank trace difference is zero because $J_Z\Theta=0$. Hence their cochain Lefschetz trace is the unchanged

$$-\sum_{\rho\in Z}m_\rho\mathcal Mf(\rho).\tag{36}$$

## 8. Continuous duality and completed tensor powers of the full object

Use continuous duals, denoted $E'_b$ with the strong topology. Transpose the actual topological splitting (20). It gives

$$\boxed{0\to Q'_b\xrightarrow{q'}\mathscr B'_b
\xrightarrow{\Theta'}V'_b\to0,\qquad \Theta'\Lambda'=1.}\tag{37}$$

The continuous cochain-dual complex is $[\mathscr B'_b\xrightarrow{\Theta'}V'_b]$ in degrees $-1,0$. Its cohomology is $Q'_b$ in degree $-1$ and zero in degree $0$. The transpose contraction proves this directly; no general exactness theorem for arbitrary locally convex quotients is assumed.

The actual finite residue map into that continuous dual is

$$\overline{E_Z}\longrightarrow Q'_b,\qquad
\bar f\longmapsto\bigl(u\mapsto R_Z(f,j_Zu)\bigr),\tag{38}$$

where $j_Zq=J_Z$. Continuity follows from the finite Mellin jets and finite dimensionality of $E_Z$. It is injective by their surjectivity and perfect residue duality. Multiplication by $g'$ then gives the arithmetic finite trace pairing, with its previously calculated radical retained.

Let $\widehat\otimes_\pi$ denote completed projective tensor product. The comparison from the previous algebraic tensor is its canonical completion map. All chain operators in (24) are continuous. Thus their finite tensor products and homotopies extend to the completed products. With $P=sq$ on $C_+$, the homotopy

$$H_n=\sum_{j=1}^n P^{\widehat\otimes(j-1)}\widehat\otimes H
\widehat\otimes1^{\widehat\otimes(n-j)}\tag{39}$$

includes $(-1)^{\sum_{i<j}|x_i|}$ on homogeneous inputs. It satisfies

$$dH_n+H_nd=1-P^{\widehat\otimes n}.$$

Consequently, for the completed external coefficient complex on the same tau-base chart product,

$$\boxed{H^k(C_+^{\widehat\otimes n})=
\begin{cases}Q^{\widehat\otimes n},&k=n,\\0,&k\ne n.\end{cases}}\tag{40}$$

This follows from a split continuous contraction, not from a blanket claim that completed tensor product preserves every exact sequence.

For the joint chart use (25). Its full cohomology in degree $k$ is the direct sum, indexed by subsets $J\subseteq\{1,\ldots,n\}$ with $|J|=k$, of the ordered completed tensors having $Q$ in the slots of $J$ and $V$ in the other slots. In those $V$ slots the scaling action is $aU_{1/a}$, exactly as in the original minus-coordinate representative. The degree-zero contribution is not discarded. Split reconstruction retains each product mask and each internal zero.

## 9. The pairing calculation is now a specified global boundary problem

The section $s:Q\to\mathscr B\subset L^2(dx)$ supplies a positive definite auxiliary form

$$\mathcal H_s(u,v)=\langle su,sv\rangle_{L^2(dx)}.$$

This is not assigned to the arithmetic Weil form. The explicit weight-covariance defect is calculated using (29) and $\langle U_af,U_ag\rangle=a\langle f,g\rangle$:

$$\boxed{\begin{aligned}
\mathcal H_s(\overline U_au,\overline U_av)-a\mathcal H_s(u,v)
={}&-\langle U_asu,\Theta k_av\rangle
-\langle\Theta k_au,U_asv\rangle\\
&+\langle\Theta k_au,\Theta k_av\rangle.
\end{aligned}}\tag{41}$$

The original source boundary and both of its cross-pairings remain. Being a boundary in $Q$ does not assert these pairings are zero in the representative Hilbert space. In a split lift each computed zero is its supported value $e$.

For a reduced eigenline of the actual dilation representation with exponent $\rho$, the left side at $u=v$ is $(a^{2\Re\rho}-a)\mathcal H_s(u,u)$. Formula (41) locates that defect in the full global boundary cocycle, with the original operator retained.

### A concrete comparison explaining which topology must be kept

In fact $\Theta V$ is dense in $L^2(\mathbb R_{>0},dx)$, although it is closed in $\mathscr B$. Here is a proof retaining the map between them. Set $b_*=\Theta\phi_*$ and

$$W:L^2(dx)\xrightarrow{\sim}L^2(dy),\qquad WF(y)=e^{y/2}F(e^y).$$

The Fourier transform in $y$, with kernel $e^{-2\pi i\nu y}$, gives

$$\mathcal F_yWb_*(\nu)=g(1/2-2\pi i\nu).$$

This is nonzero almost everywhere, because $g$ is a nonzero entire function. The span of all translates of $Wb_*$ is dense in $L^2(dy):$ a vector orthogonal to all translates has Fourier transform whose product with $\overline{\mathcal F_yWb_*}$ is an $L^1$ function with zero Fourier transform, hence vanishes almost everywhere. The nonvanishing just stated then makes that vector zero. Since $WU_ab_*=a^{1/2}(Wb_*)(y-\log a)$ and $U_ab_*\in\Theta V$, density follows.

The exact quotient comparison is therefore

$$\boxed{Q=\mathscr B/\Theta V\longrightarrow
L^2(dx)/\overline{\Theta V}^{L^2}=0.}\tag{42}$$

Its kernel is all of $Q$. Its split lift sends every supported input to the supported zero in $G(0)=\mathbb B$, while keeping external absence separate. The constructive replacement is the Frechet quotient and the explicit global section (19), not a claim that the ordinary Hilbert quotient secretly retains those classes.

## 10. Scope of the progress toward the Deligne comparison

The selected supplied Weil II passages 3.3.4-3.3.6 put two bounds on the same compact-to-ordinary image; 6.2 retains the dualizing operation and its shifts. This continuation does not apply those bounds over a new base without their geometric proof. It makes the existing characteristic-zero arithmetic complex globally split in its precise topological category, gives its continuous dual and completed products, and computes the operator defects on those same objects.

The formerly unresolved algebraic-to-Hausdorff kernel is now zero by (16)-(21). The finite extension class and its residue/Jacobian trace are carried by (33)-(36). The full scaling boundary is (29), its dependence on the auxiliary cutoffs is (32), and its metric defect is (41). These are concrete maps available for a global comparison.

Still retained: the common kernel of all finite spectral observations, the meromorphic summand of the balanced analytic realization, and the requirement to identify the correct arithmetic polarization/weight control on the global geometric image. The density map (42) explains why discarding the stronger topology would remove the entire arithmetic cohomology, not why the supported programme should be abandoned.

The reconstruction estimate contains $1-c_{\alpha,\beta}$; no asymptotic uniform estimate for it is proved. No global positivity, RH, GRH, or infinite trace-class theorem is claimed. No theorem from the earlier finite-range work is upgraded to a Lean certificate. The new global retraction proof itself uses only the original theta/Poisson identities, absolute Mobius inversion, the displayed Fourier compactness argument, and the two retained moment maps.

## 11. Verification and references

The written analytic proofs are the evidence for the new analytic statements. The accompanying unittest script tests exact finite identities: divisor cancellation with supported zeros, cutoff-resolvent identities in a finite unitary model, moment corrections, contractions, synchronization masks, operator cocycles, changes of sections, preservation of extension classes, finite trace changes, and completed-tensor algebra before completion. It does not numerically certify a Fourier operator norm, an analytic convergence statement, or a Riemann zero.

Source interfaces read:

- Owner's `SplitZero_Derived_Mathematics_2026-09-12(1).md`, sections 1-7; the source permits nonzero bottom fibres in its general interface.
- PR #9, `workbenches/tau-chain-descent/RESEARCH_NOTE.md`, at the commit above; local bytes match its Git blob.
- PR #8's finite comparison as retained and invoked in #9; the sections using $s_Z$ and $J_Z$ are explicitly dependencies of (33)-(38), not inputs to the proof of (2).
- Supplied Weil II TeX: the actual 3.3.1-3.3.6 excerpt, including its finite-type base and duality assumptions. It was read as TeX, not obtained by OCR. No full source-proof audit is claimed.
- Ralf Meyer, *A spectral interpretation for the zeros of the Riemann zeta function*, arXiv:math/0412277: prior-context abstract only in this continuation. A source-archive retrieval failed; no unread detailed theorem is cited as a premise.

The contribution is AI-assisted under the owner's mathematical direction. Original mathematical files, formal sources, attribution and licenses are unchanged. Only authored exposition, test code and validation records are proposed for public addition; no private transcript or source-literature corpus is published.
