# Spectral-sum descent with the relative arithmetic fibre retained

Owner-directed continuation of the split-zero programme. 12 September 2026.

**Status.** Written deductions for review. These results use the actual theta range and representative constructions stated in the preceding packages. Their analytic inputs are not newly Lean-certified. The finite polynomial, quotient, and matrix statements below have independent proofs and executable finite tests. No RH, GRH, or sublinear arithmetic weight bound is asserted.

## 1. Integration and purpose

The new Kernel–Layer Integration supplement and the preceding Symmetric Frontier note overlap in their explicit relation basis and inverse-metric control. We retain the dictionary

$$K_N=\mathcal C_M,\quad U_N=F,\quad D_N=\Omega,\quad
\mathscr E_N=b_M,\quad F_N=\Omega^{-1}E_+^*,\quad V_N=\mathcal Z_M,\qquad N=M.\tag{1.1}$$

The supplement's sharper rank bound follows by grouping the summed derivative at degree $M$ rather than counting all degree-$M+1$ coordinates. Its identities are not counted again as new work. In particular its one-variable map

$$e_{n+d+1}=u_{n+1},\qquad
\mathfrak h_{n+1}=\kappa_{n+d+1}^{(h)}+a_{n+d+1}^*G_{h,n}a_{n+d+1}\tag{1.2}$$

is retained: it identifies the packet-dependent interpolation layer with the original packet-independent theta relation by an actual polynomial-divisibility map.

The new step is to push the arithmetic tensor system along its **sum coordinate**, retaining the relative coordinates in a matrix-valued arithmetic measure. We calculate the entire symmetric-square relation algebra, its original theta primitives, the exact norm under the pushforward, and the full nilpotent fibres of the sum action. This is a product-to-one-parameter construction on the existing characteristic-zero object over the tau base. It is not a use of finite-field purity with relabelled coefficients.

## 2. Unchanged source, split quotient, and tensor cohomology

Keep

$$G(R)=\{\tau\}\sqcup\{r^\bullet:r\in R\},\quad e_R=0_R^\bullet,\qquad
\begin{array}{ccc}G(\mathbb Z)&\xrightarrow{G(j)}&G(\mathbb C)\\
p_{\mathbb Z}\downarrow&&\downarrow p_{\mathbb C}\\
\mathbb Z&\xrightarrow{j}&\mathbb C.\end{array}\tag{2.1}$$

The first quotient remains infinite. All spaces and morphisms are marked over the existing absolute pointed base $\mathfrak b_\tau$. At an active coefficient label $\lambda$, the lift of a linear map $T$ is $(\lambda,x)\mapsto(\lambda,Tx)$; it fixes external absence. Its amplitude-zero value is $(\lambda,0)$, the image of the original supported-zero action, not $\tau$.

Use precisely

$$V=\{\phi\in\mathcal S(\mathbb R):\phi\text{ even},\ \phi(0)=0,\ \int_{\mathbb R}\phi=0\},\qquad
\mathscr B=\{F:\sup_{x>0}x^b|D^jF(x)|<\infty\ (b\in\mathbb Z,j\ge0)\},\quad D=-x\partial_x,$$

$$C_+=[V\xrightarrow\Theta\mathscr B],\qquad
\Theta\phi(x)=\sum_{n\ne0}\phi(nx),\qquad Q=\mathscr B/\Theta V,$$

$$\phi_*=(4\pi^2x^4-6\pi x^2)e^{-\pi x^2},\qquad
\mathcal M\Theta\phi_*=g,\qquad g(s)=2\xi(s).\tag{2.2}$$

For a finite nonempty packet of actual zeros with their full orders, put

$$h(s)=\prod_{\rho\in Z}(s-\rho)^{m_\rho},\quad d=\deg h,\quad
E_h=\mathbb C[s]/(h),\quad v_h=g/h,\quad \upsilon_h=j_hv_h\in E_h^\times.$$

The prior analytic construction supplies $F_h\in\mathscr B$ with $\mathcal MF_h=v_h$ and $h(D)F_h=\Theta\phi_*$. Retain its maps

$$\mathcal T_h(P)=P(D)F_h,\quad
\mathcal T_h(hP)=\Theta(P(D)\phi_*),\quad J_h\mathcal T_h(P)=\upsilon_h[P]_h.\tag{2.3}$$

For tensor degree $k$, use $\mathcal P_M=\mathbb C[s_1,\ldots,s_k]_{\deg\le M}$ and

$$E_k=E_h^{\otimes k},\quad A_k=M_{s_1+\cdots+s_k},\quad
\mathcal T_k(P)=P(D_1,\ldots,D_k)F_h^{\otimes k},$$

$$I_{k,M}=\mathcal P_M\cap(h(s_1),\ldots,h(s_k)),\qquad B_{k,M}=\mathcal T_k I_{k,M}.\tag{2.4}$$

The jet map $\mathcal J_kP=\upsilon_h^{\otimes k}[P]$ has this exact kernel and is onto when $M\ge k(d-1)$. This map is linear, with an invertible unit multiplication after the algebra quotient; it is not called a unital algebra homomorphism. The source representative $R_{k,M}$ is its unique least-norm lift with the specified theta relations allowed. Thus

$$J^{(k)}R_{k,M}=1,\quad q^{(k)}R_{k,M}=\sigma_h^{\otimes k},\quad
G_{k,M}=R_{k,M}^*R_{k,M},\quad
W_{k,M}=A_k^*G_{k,M}+G_{k,M}A_k-kG_{k,M}.\tag{2.5}$$

The tensor differential retains $(-1)^{j-1}$ when it applies the differential in the $j$th factor to a degree-$(k-1)$ primitive with all other factors of degree one. A primitive for the positive relation $h(s_j)P_j$ has the matching sign $(-1)^{j-1}$.

In top degree the signed chain projector

$$\mathsf S_k=\frac1{k!}\sum_{\pi\in S_k}\operatorname{sgn}(\pi)T_\pi\tag{2.6}$$

selects ordinary symmetric tensors: the Koszul sign in $T_\pi$ supplies the second permutation sign. The factor $1/k!$ is retained. We work on this image while retaining the complementary chain projector $1-\mathsf S_k$ and its trace. A source mask is transported to the union of its permutation orbit before averaging; its cancelled coordinates remain supported at that joined label.

## 3. The spectral-sum direct image is an exact functor with its action fixed

Define the actual ring map

$$\iota_k:\mathbb C[S]\longrightarrow E_k,\qquad S\longmapsto[s_1+\cdots+s_k].\tag{3.1}$$

For an $E_k$-module $M$, let $\pi_{k*}M$ be that same module with the $\mathbb C[S]$ action restricted through $\iota_k$. The functor is exact because its maps, kernels, and underlying abelian groups are unchanged. It has the explicit adjunction

$$\operatorname{Hom}_{E_k}(E_k\otimes_{\mathbb C[S]}L,M)
\cong\operatorname{Hom}_{\mathbb C[S]}(L,\pi_{k*}M),\tag{3.2}$$

with forward map $f\mapsto(l\mapsto f(1\otimes l))$ and inverse $a\otimes l\mapsto a f(l)$. On quasi-coherent sheaves this is pushforward along the finite morphism $\operatorname{Spec}E_k\to\operatorname{Spec}\mathbb C[S]$. The affine pushforward statement concerns quasi-coherent complexes, not all sheaves of modules (Stacks, Tag 0AVV).

The split map is $G(\iota_k)$, with

$$p_{E_k}G(\iota_k)=\iota_kp_{\mathbb C[S]},\quad
G(\iota_k)(e_{\mathbb C[S]})=e_{E_k},\quad G(\iota_k)(\tau)=\tau.\tag{3.3}$$

Consequently the geometric arrow is over the same $\mathfrak b_\tau$. It does not replace that base by a finite field. The additional line $\operatorname{Spec}\mathbb C[S]$ is the recipient of a specified arithmetic correspondence.

At the original cochain level, $S$ acts by $D_1+\cdots+D_k$. Its finite representative equation remains

$$D^{(k)}R_{k,M}-R_{k,M}A_k=dK_{k,M}\in B_{k,M+1}.\tag{3.4}$$

The jet and cohomology maps intertwine that action exactly. Restriction of scalars preserves their kernels and this boundary equation. It does not declare the chosen representative $R_{k,M}$ equivariant.

On the symmetric summand the ring is $B_k=(E_k)^{S_k}$, its inclusion is the original invariant inclusion, and $S$ acts by the same sum. Exactness of taking invariants here follows from the specified Reynolds projector $k!^{-1}\sum P_\pi$ over $\mathbb C$.

### 3.1 The pushforward has a computed free resolution and dualizing comparison

Let $E$ denote the actual finite ordered or symmetric image, with its exact sum operator $A$. Put $R=\mathbb C[S]$ and $n=\dim_\mathbb C E$. There is the actual free resolution

$$\boxed{0\longrightarrow R\otimes_\mathbb C E
\xrightarrow{\ S I-A\ }R\otimes_\mathbb C E
\xrightarrow{\mathrm{ev}_A}\pi_*E\longrightarrow0,\qquad
\mathrm{ev}_A(P\otimes v)=P(A)v.}\tag{3.5}$$

Injectivity of $SI-A$ follows either from its monic nonzero determinant or by inspecting the highest coefficient of a polynomial vector. To identify the kernel of $\mathrm{ev}_A$, use

$$S^jv-A^jv=(SI-A)\sum_{i=0}^{j-1}S^{j-1-i}A^iv.$$

Subtracting these displayed relations leaves precisely the constant vector $\mathrm{ev}_A(f)$. This proves exactness with both original arrows retained.

Let $E^\vee=\operatorname{Hom}_\mathbb C(E,\mathbb C)$ and $A^\vee\lambda=\lambda\circ A$. This is the algebraic dual; its matrix is a transpose. The coefficient conjugation $\overline{E^\vee}\to E^\#$, $\overline\lambda\mapsto(v\mapsto\overline{\lambda(v)})$, connects it explicitly to the antidual used in the control matrices.

Applying $\operatorname{Hom}_R(-,R\,dS)$ to (3.5) gives

$$R\operatorname{Hom}_R(\pi_*E,R\,dS)
\simeq [R\otimes E^\vee\,dS\xrightarrow{\ S I-A^\vee\ }R\otimes E^\vee\,dS],\tag{3.6}$$

in degrees $0,1$. Its degree-zero group is zero, and

$$\boxed{\operatorname{Ext}^1_R(\pi_*E,R\,dS)\cong E^\vee,\qquad
[P(S)dS]\mapsto P(A^\vee).}\tag{3.7}$$

Here $P(A^\vee)$ means $\sum_j(A^\vee)^j\lambda_j$ for a polynomial dual vector $P(S)=\sum_jS^j\lambda_j$. The inverse is the constant class $\lambda\mapsto[\lambda dS]$.

For the explicit cohomological shift, $C[b]^i=C^{i+b}$. Thus

$$R\operatorname{Hom}_R(\pi_*E[-k],R\,dS[1])\simeq E^\vee[k].\tag{3.8}$$

The degree-$k$ arithmetic image becomes degree $-k$ under the stated dualizing object of the sum line. These shifts are obtained from (3.6), not inferred by calling the finite packet a curve.

The adjoint behind this calculation is the actual module-category map

$$\operatorname{Hom}_R(\pi_*M,L)\cong
\operatorname{Hom}_{B_k}(M,\operatorname{Hom}_R(B_k,L)),\qquad
f\mapsto(m\mapsto(b\mapsto f(bm))).\tag{3.9}$$

The inverse evaluates the inner map at $1$. Passing to derived Hom gives the corresponding derived right adjoint. This concerns the exact restriction functor on module categories; no exactness of pushforward on all sheaves is asserted (Stacks, Tag 0AWZ).

### 3.2 Resolve the finite arithmetic trace through that same duality

The pairing in (3.7) is equivalently the concrete resolvent-residue pairing

$$\boxed{\langle v,[P(S)dS]\rangle
=\sum_{\lambda\in\operatorname{Spec}A}
\operatorname{Res}_{S=\lambda}
P(S)\bigl((SI-A)^{-1}v\bigr)dS.}\tag{3.10}$$

Relations from $SI-A^\vee$ produce polynomial expressions with no finite residue. Expanding the resolvent at infinity proves that the sum is $P(A^\vee)(v)$: the coefficient of $S^{-1}$ is $\sum_j\lambda_j(A^jv)$. This proves perfectness without deleting nilpotents.

On a block $A=\lambda I+N$ the retained resolvent is

$$(SI-A)^{-1}=\sum_{j=0}^{\ell-1}\frac{N^j}{(S-\lambda)^{j+1}},\qquad N^\ell=0.\tag{3.11}$$

The trace observation of that resolvent is a further specified map. For a function $\psi$ holomorphic at the finite spectrum,

$$\boxed{\operatorname{Tr}(\psi(A))=
\sum_\lambda\operatorname{Res}_{S=\lambda}
\psi(S)\operatorname{Tr}((SI-A)^{-1})dS
=\sum_\lambda\operatorname{Res}_{S=\lambda}\psi(S)\frac{\chi_A'(S)}{\chi_A(S)}dS,}\tag{3.12}$$

where $\chi_A(S)=\det(SI-A)$ is the exact finite characteristic polynomial. It is not substituted for the original $g=2\xi$. With $\psi(S)=a^S$, (3.12) is the finite Lefschetz contribution of the same diagonal scaling correspondence. The cochain image is in degree $k$, so its supertrace includes $(-1)^k$.

The constant-class maps in (3.5)–(3.7), and the linear functional in (3.10), lift fibrewise to the original split objects. Every zero functional or zero residue remains supported. At fixed label the equations forming the resolution have composite the supported zero map. The residue pairing is an ordinary bilinear pairing in that coefficient fibre, with its split lift separately additive, not a linear map on its Cartesian product.

## 4. The symmetric tensor-square has an explicit two-generator relation algebra

Use three distinguished polynomials

$$S=s_1+s_2,\qquad r=s_1-s_2,\qquad \Delta=r^2.\tag{4.1}$$

The inverse map before taking invariants is

$$s_1=(S+r)/2,\qquad s_2=(S-r)/2.$$

Swap fixes $S$ and sends $r$ to $-r$. Therefore the algebra map

$$\Phi:\mathbb C[S,\Delta]\xrightarrow{\sim}\mathbb C[s_1,s_2]^{S_2},\qquad
S\mapsto s_1+s_2,\quad\Delta\mapsto(s_1-s_2)^2\tag{4.2}$$

is an isomorphism. Its proof is even/odd expansion in $r$, using the displayed inverse with both factors $1/2$. Give $S$ degree one and $\Delta$ degree two; then $\Phi$ preserves the entire original total-degree filtration.

Define actual polynomials $H_0,H_1$ by

$$h((S+r)/2)=H_0(S,r^2)+rH_1(S,r^2),$$

$$h((S-r)/2)=H_0(S,r^2)-rH_1(S,r^2).\tag{4.3}$$

In particular $H_0$ is the half-sum and $H_1$ is the difference divided by $2r$. That difference is an odd polynomial, so this is polynomial division, not localization away from $r=0$.

**Theorem (complete symmetric relation ideal).**

$$\boxed{B_2=(E_h\otimes E_h)^{S_2}
\cong\mathbb C[S,\Delta]/(H_0,\Delta H_1).}\tag{4.4}$$

**Proof.** In $\mathbb C[S,r]$, the original ideal $(h(s_1),h(s_2))$ is $(H_0,rH_1)$. Its even part is exactly $(H_0,r^2H_1)$: average an expression $H_0a+rH_1b$ under $r\mapsto-r$. Writing $a=a_0+r a_1$, $b=b_0+r b_1$ gives the even expression $H_0a_0+\Delta H_1b_1$. Conversely both generators are in the original ideal. Invariants of the quotient equal the quotient of invariants because Reynolds averaging is an exact projector. This proves (4.4), including coincident roots and all nilpotents.

The quotient has dimension $d(d+1)/2$. Indeed the unscaled orbit sums of the basis $s_1^is_2^j$, $0\le i,j<d$, give that many independent invariant vectors. The associated graded Hilbert series is

$$\sum_{0\le i\le j<d}z^{i+j}
=\frac{(1-z^d)(1-z^{d+1})}{(1-z)(1-z^2)}.\tag{4.5}$$

Here associated graded refers to the original degree filtration; (4.5) is not a claim that a nonhomogeneous $h$ defines a graded algebra. Polynomial remainder lowers degree, and Reynolds averaging respects the filtration, proving the formula for every monic $h$ of degree $d$.

### 4.1 All original primitives and their degrees survive

Let a symmetric relation of degree at most $M$ have, after original ordered division, the expression $h(s_1)Q_1+h(s_2)Q_2$ with $\deg Q_i\le M-d$. Averaging yields paired coefficients

$$C_1=(Q_1+Q_2\circ\mathrm{swap})/2,\qquad C_2=C_1\circ\mathrm{swap}.$$

Put $A_0=C_1+C_2$ and $A_1=(C_1-C_2)/r$. Then $A_0,A_1$ are polynomials in $S,\Delta$ and

$$H_0A_0+\Delta H_1A_1=h(s_1)\frac{A_0+rA_1}{2}
+h(s_2)\frac{A_0-rA_1}{2}.\tag{4.6}$$

Their weighted degree bounds are $\deg A_0\le M-d$ and $\deg A_1\le M-d-1$. The two source primitives are respectively

$$\frac{A_0+rA_1}{2}(D_1,D_2)(\phi_*\otimes F_h),\qquad
-\frac{A_0-rA_1}{2}(D_1,D_2)(F_h\otimes\phi_*).\tag{4.7}$$

The negative sign in the second primitive meets the negative cochain sign of the second differential. Applying $d$ gives exactly (4.6) through $\mathcal T_2$.

The unit $\upsilon_h\otimes\upsilon_h$ is symmetric. Under (4.4) denote its full class by $\upsilon_{2,h}$. The jet map in these coordinates is exactly

$$\mathcal J'_{2,M}:\mathbb C[S,\Delta]_{\deg S+2\deg\Delta\le M}
\longrightarrow B_2,\qquad P\longmapsto\upsilon_{2,h}[P].\tag{4.8}$$

Its kernel is the full weighted-degree part of $(H_0,\Delta H_1)$. It is onto for $M\ge2(d-1)$. This is the original full-jet map conjugated by $\Phi$, not a scalar evaluation at the sum coordinate.

On the split totals, $\widetilde\Phi(\lambda_M,P)=(\lambda_M,\Phi P)$ and $\widetilde\Phi(\tau)=\tau$. The induced isomorphism of relation quotients commutes with every $M\to M+1$. A nonzero new relation therefore becomes $(\lambda_{M+1},0)$ under exactly the same degree transition as before.

## 5. The arithmetic norm becomes a one-variable matrix weight

Let

$$w_h(t)=\left|\frac{g(1/2+it)}{h(1/2+it)}\right|^2\frac1{2\pi},\qquad d\nu_h(t)=w_h(t)dt.\tag{5.1}$$

No mass is assigned the value one. The source norm of a two-variable polynomial is

$$\|\mathcal T_2P\|^2=\int_{\mathbb R^2}|P(1/2+it_1,1/2+it_2)|^2w_h(t_1)w_h(t_2)dt_1dt_2.$$

Make the exact real coordinate change

$$u=t_1+t_2,\quad v=t_1-t_2,\qquad
(t_1,t_2)=((u+v)/2,(u-v)/2),\qquad dt_1dt_2=\tfrac12du\,dv.\tag{5.2}$$

Then $S=1+iu$, $r=iv$, and $\Delta=-v^2$. If

$$P(S,\Delta)=\sum_{a=0}^{b}\Delta^a f_a(S),\qquad b=\lfloor M/2\rfloor,\quad\deg f_a\le M-2a,$$

define the full matrix

$$\boxed{\mathsf W_{h,b}(u)_{ac}
=\frac{(-1)^{a+c}}2\int_{\mathbb R}v^{2(a+c)}
w_h((u+v)/2)w_h((u-v)/2)\,dv.}\tag{5.3}$$

**Theorem (isometric spectral-sum realization).**

$$\boxed{\|\mathcal T_2\Phi P\|^2
=\int_{\mathbb R}f(1+iu)^*\mathsf W_{h,b}(u)f(1+iu)\,du.}\tag{5.4}$$

This follows by (5.2), finite polynomial expansion, and Fubini. All integrals converge by the source's exponential moments. For every real $u$, the matrix $\mathsf W_{h,b}(u)$ is positive definite: its quadratic form is the integral of the squared modulus of a nonzero polynomial in $-v^2$ against a density positive almost everywhere. Zeros of the nonzero entire $g/h$ are discrete and cannot remove a positive-measure set of the $v$-line. The exponential bounds prove convergence also for each fixed $u$.

For $b=0$ the scalar coefficient is the convolution

$$\mathsf W_{h,0}(u)=(w_h*w_h)(u).\tag{5.5}$$

For $b>0$, its additional rows are the actual relative-coordinate moments. They have not been replaced by (5.5).

The map in (5.4) sends a polynomial to its vector of coefficient functions; its inverse is $f\mapsto\sum\Delta^af_a(S)$ on the specified filtered image. Multiplication by $s_1+s_2$ is exactly multiplication by $S$ on every component. Hence its generator is still $A_2$, its degree increase is still one, and its boundary is still (3.4).

### 5.1 General tensor degree

For any $k$, set $S=\sum s_i$, retain $x_i=s_i$ for $i<k$, and put $s_k=S-\sum_{i<k}x_i$. This is a polynomial algebra isomorphism with determinant one on the real variables $(t_1,\ldots,t_k)\leftrightarrow(t_1,\ldots,t_{k-1},u=\sum t_i)$.

Write $P=\sum_\alpha x^\alpha f_\alpha(S)$, with $\deg f_\alpha\le M-|\alpha|$. Its matrix weight is

$$\mathsf W_{k,M}(u)_{\alpha\beta}
=\int_{\mathbb R^{k-1}}\overline{\prod_{i<k}(1/2+it_i)^{\alpha_i}}
\prod_{i<k}(1/2+it_i)^{\beta_i}
\prod_{i<k}w_h(t_i)\,w_h(u-\sum_{i<k}t_i)\,d^{k-1}t.\tag{5.6}$$

The outer coordinate is $S=k/2+iu$. The same proof gives an isometry on the actual degree-$M$ source, with every original relation substituted through this algebra isomorphism. Its entries have exponential moments in $u$ for every exponent below the source threshold $\pi/2$: use $|\sum t_i|\le\sum|t_i|$, the polynomial factors, and the one-variable exponential moment. Constants depend on the retained packet, $k$, and degrees; no uniform-in-$k$ estimate is inferred.

## 6. The canonical representative, kernel control and relation layers commute with the descent

Let $C_M$ be the explicit coefficient matrix of $\Phi$ from $S^a\Delta^b$ to the original symmetric polynomial basis. It is invertible between those two filtered spaces. Let $U$ be the exact coordinate map of (4.4) to the original unscaled invariant quotient basis. Retain its orbit coefficients.

For the source moment and full-jet matrices,

$$M'_M=C_M^*M_M C_M,\qquad J'_M=U^{-1}J_MC_M.\tag{6.1}$$

The matrix in (5.3) gives exactly $M'_M$ by one-dimensional integration of its entries against the retained powers of $S$.

The inverse interpolation kernel and its metric satisfy

$$K'_M=J'_M(M'_M)^{-1}(J'_M)^*=U^{-1}K_M(U^{-1})^*,\qquad
G'_M=U^*G_MU.\tag{6.2}$$

These identities follow by multiplying the stated inverses, not by selecting a new metric. The least-norm representatives obey $R'_M=R_MU$ after their polynomial-source identification. Their action and control are

$$A'_2=U^{-1}A_2U,\quad W'_M=U^*W_MU,\quad
\mathcal Z'_M=U^{-1}\mathcal Z_M(U^{-1})^*.\tag{6.3}$$

Thus every control inequality is exactly transported. The same isometry sends the actual next boundary layer, its Gram matrix, and its two maps $Y_M,C_M^{\mathrm{rel}}$ to their images in (5.4). It preserves the finer rank bound supplied by the new attachment.

The arithmetic representative defect remains a relation with an explicit primitive (4.7). Its cross-pairing is evaluated by (5.3); it is not erased when the relation becomes a supported zero in the next internal quotient.

### 6.1 Retain the base and relative parts of the norm separately through a triangular map

Write the finite matrix weight as

$$\mathsf W(u)=\begin{pmatrix}m_0(u)&b(u)\\b(u)^*&C(u)\end{pmatrix},\qquad m_0(u)>0.$$

There is the exact isometric map into the stated direct-sum weighted space

$$\mathcal A:f\longmapsto\bigl(f_0+m_0^{-1}b f_{\mathrm{rel}},\ f_{\mathrm{rel}}\bigr),\tag{6.4}$$

with inverse $(a,z)\mapsto(a-m_0^{-1}bz,z)$ and weights

$$m_0(u),\qquad C(u)-b(u)^*m_0(u)^{-1}b(u).\tag{6.5}$$

Completing the square proves the isometry and positivity of the second weight. No measure is renormalized: $m_0$ and its reciprocal are both in the formulas. The image $\mathcal A(\mathcal P_M^{\mathrm{sym}})$ is retained, not enlarged to arbitrary functions in the target. The ratio $m_0^{-1}b$ need not be polynomial. Multiplication by $S=1+iu$ commutes with this pointwise map, so the derivative action is still specified without a new connection term.

This supplies two concrete analytic quantities for the next estimates: the convolution mass and the full relative covariance matrix. Neither positivity of this representative norm nor the scalar mass alone is being substituted for the arithmetic Weil pairing.

## 7. Calculate every nilpotent fibre of the sum map

The pushforward must not replace a multiple jet by its residue. We now give its complete Jordan lengths.

For an ordered root tuple $(\rho_1,\ldots,\rho_k)$ with retained orders $m_i$, its local algebra is

$$L_{\boldsymbol\rho}=\mathbb C[z_1,\ldots,z_k]/(z_1^{m_1},\ldots,z_k^{m_k}),\quad
A_k=\rho_\Sigma I+N,\quad \rho_\Sigma=\sum\rho_i,\quad N=M_{\sum z_i}.\tag{7.1}$$

Let $D_0=\sum(m_i-1)$ and $c_r=[t^r]\prod_i(1+t+\cdots+t^{m_i-1})$, with $c_{-1}=0$.

**Theorem (full ordered sum-fibre decomposition).** As a $\mathbb C[S]$-module,

$$\boxed{\pi_{k*}L_{\boldsymbol\rho}\cong
\bigoplus_{r=0}^{\lfloor D_0/2\rfloor}
\left(\mathbb C[S]/(S-\rho_\Sigma)^{D_0-2r+1}\right)^{\oplus(c_r-c_{r-1})}.}\tag{7.2}$$

Here the isomorphism is constructed by primitive vectors, as follows. On $z_i^j$ set

$$F_i z_i^j=j(m_i-j)z_i^{j-1},\quad H_i z_i^j=(2j-(m_i-1))z_i^j.$$

For $F=\sum F_i$ and $H=\sum H_i$, direct substitution gives

$$[N,F]=H,\qquad[H,N]=2N,\qquad[H,F]=-2F.\tag{7.3}$$

An auxiliary positive inner product making $F=N^*$ is explicitly diagonal:

$$\langle z^\alpha,z^\beta\rangle_0=
\delta_{\alpha\beta}\prod_i\frac{\alpha_i!(m_i-1)!}{(m_i-1-\alpha_i)!}.\tag{7.4}$$

These are specified positive numbers. For the actual arithmetic Gram $G_{k,M}$ and the displayed diagonal Gram $G_0$, their exact comparison is the invertible operator $C_0=G_{k,M}^{-1}G_0$, with inverse $G_0^{-1}G_{k,M}$:

$$\langle v,w\rangle_0=\langle v,C_0w\rangle_{G_{k,M}}.\tag{7.4a}$$

Equation (7.4) is used only to prove the algebraic decomposition. All arithmetic control remains with $G_{k,M}$. In the primitive-ladder basis its entries are $(N^ip)^*G_{k,M}(N^jq)$, including all cross-ladder terms. They are not discarded because the auxiliary Gram admits orthogonal ladders.

A primitive vector $p$ has degree $r$ and satisfies $Fp=0$. Put $w=D_0-2r$. The commutators prove

$$FN^jp=j(w-j+1)N^{j-1}p,\quad
\|N^jp\|_0^2=\frac{j!w!}{(w-j)!}\|p\|_0^2\quad(0\le j\le w).\tag{7.5}$$

Thus its ladder has length $w+1$ and $N^{w+1}p=0$. Conversely a nonzero lowest vector has $r\le D_0/2$, since $\|Np\|_0^2=(D_0-2r)\|p\|_0^2$. Orthogonal complements of the constructed ladders are invariant under $N,F,H$, so induction decomposes the full finite space. Counting degree-$r$ vectors before the middle gives $c_r-c_{r-1}$ new primitive ladders. The isomorphism in (7.2) maps $[q(S)]$ in a chosen primitive copy to $q(\rho_\Sigma+N)p$.

### 7.1 All symmetric packets, including collisions of sums

For an occupation list $\mathbf n=(n_\rho)_\rho$, $\sum n_\rho=k$, the corresponding invariant local component is

$$B_{\mathbf n}=\bigotimes_\rho
\left(\mathbb C[z_1,\ldots,z_{n_\rho}]/(z_j^{m_\rho})\right)^{S_{n_\rho}}.$$

It retains its own canonical central idempotent even when two different occupation lists have the same sum $\sum n_\rho\rho$. Its graded dimensions $c_r$ are counted by unscaled orbit monomials; equivalently their generating polynomial is

$$\prod_\rho\prod_{j=1}^{n_\rho}
\frac{1-t^{m_\rho+j-1}}{1-t^j}.\tag{7.6}$$

For $n_\rho=0$ the factor is one. This is a polynomial identity for the orbit counts; no division at a root of unity is needed. The same operators preserve invariants and the same primitive proof gives (7.2) with

$$D_0=\sum n_\rho(m_\rho-1),\qquad \rho_\Sigma=\sum n_\rho\rho$$

and these invariant $c_r$. It includes all $k$ and all finite multiplicities.

For one order-three zero taken twice, write $z_i=s_i-\rho$, $X=z_1+z_2$. The symmetric component has the exact ladders

$$1,\ X,\ X^2,\ X^3,\ X^4,\qquad
p=z_1^2-z_1z_2+z_2^2,\quad Xp=0,\tag{7.7}$$

with $X^3=3(z_1^2z_2+z_1z_2^2)$ and $X^4=6z_1^2z_2^2$. Its pushforward is

$$\mathbb C[S]/(S-2\rho)^5\ \oplus\ \mathbb C[S]/(S-2\rho).\tag{7.8}$$

The actual total dimension is six. Merely retaining one evaluation at $2\rho$ would lose five dimensions; the displayed injective primitive maps and direct sum retain all six.

The original $\upsilon_h^{\otimes k}$ acts by an invertible multiplication map on every component and commutes with $A_k$. It carries these coordinates to the original full-jet coordinates. Its coefficients are not assigned one.

## 8. Pairings, traces, and the support-layer meaning of the ladders

The algebraic direct image in (3.1) keeps the full underlying vector space. Therefore its trace of $a^{A_k}$ is unchanged. On the occupation component,

$$\operatorname{Tr}(a^{A_k}\mid B_{\mathbf n})
=\left[\prod_\rho\binom{n_\rho+m_\rho-1}{n_\rho}\right]
 a^{\sum n_\rho\rho}.\tag{8.1}$$

This is valid with all nonzero nilpotents, since their exponential is triangular with diagonal one. The cochain summand has degree $k$, so its supertrace is $(-1)^k$ times (8.1). The complementary symmetry summands retain their previously calculated traces. No packet is deleted by pushing to the sum line.

Each ladder map in (7.2) has a split lift fixing $\tau$. In the module $\mathbb C[S]/(S-\rho_\Sigma)^\ell$, the transition to the quotient of length $\ell-1$ takes the nonzero top jet to the supported zero. On its original side the quotient map is the corresponding quotient by $\mathbb C N^{\ell-1}p$; it is a $\mathbb C[S]$-module quotient, not a declaration that this line is an algebra ideal. The full direct-image theorem retains the line before that optional observation.

The residue pairing and arithmetic Jacobian trace form are transported by the same full coordinate matrices. For an invertible coordinate map $U$, retain

$$S'=U^*S U,\qquad J'_g=U^{-1}J_gU,\qquad G'=U^*G U,\qquad
S'J'_g=U^*S J_gU.\tag{8.2}$$

On product cohomology one additionally retains the original tensor-duality signs. No auxiliary inner product from (7.4) is substituted in (8.2). A supported zero of the trace and a full vanishing jet are connected only through the stated Jacobian/trace map.

## 9. A complete unscaled arithmetic-moment calibration

For a declared Gaussian calibration, not an asserted zeta packet, take the one-variable measure $e^{-t^2/2}dt$. The change (5.2) gives

$$\mathsf W_2(u)=\sqrt\pi e^{-u^2/4}
\begin{pmatrix}
1&-2&12\\-2&12&-120\\12&-120&1680
\end{pmatrix}\tag{9.1}$$

on coefficient functions of $1,\Delta,\Delta^2$. This uses

$$\frac12\int v^{2j}e^{-v^2/4}dv=2^j(2j-1)!!\sqrt\pi,$$

with $(-1)!!=1$. The actual triangular coordinate matrix with columns $1,\Delta+2,\Delta^2+12\Delta+12$ is

$$T=\begin{pmatrix}1&2&12\\0&1&12\\0&0&1\end{pmatrix},\qquad
T^*\mathsf W_2(u)T=\sqrt\pi e^{-u^2/4}\operatorname{diag}(1,8,384).\tag{9.2}$$

All three fibre directions and their norms survive. For the first two directions, the exact base/relative decomposition is

$$\|f_0+\Delta f_1\|^2
=\sqrt\pi\int e^{-u^2/4}\left(|f_0-2f_1|^2+8|f_1|^2\right)du.\tag{9.3}$$

The source metric has total two-variable mass $2\pi$, retained by these formulas. Exact symbolic tests compare the moments of $S^a\Delta^b$ computed directly in $(t_1,t_2)$ and through (9.1), and compare the resulting constrained representatives, jet maps, Grams and controls.

For the actual arithmetic measure, (5.3) supplies the corresponding nonconstant matrix. Its relative covariance need not have the constant Gaussian form. Neither the calibration's triangular coefficients nor its control are imported into the arithmetic case.

## 10. Position in the Deligne-style programme

The source's tensor-square step is followed by geometric pushforward and control on that pushforward, not by tensoring alone. The construction here now supplies a **specified sum-coordinate pushforward** of the actual finite arithmetic image and its original filtered representatives. Its metric realization is the exact one-dimensional matrix weight (5.3) or (5.6), with the relative directions retained. The symmetric relation presentation (4.4) and original primitives (4.7) say exactly which zero-amplitude relations are present in that fibre.

The result does not identify this finite spectral scheme or matrix-weight model with a lisse sheaf on a Lefschetz pencil. The map actually constructed is the quasi-coherent finite pushforward (3.1), connected to the original analytic representatives by (2.3), (4.8), and (5.4). Deligne's geometric hypotheses and estimates have not thereby been imported.

The immediate control task now has an explicit base/relative split: estimate the actual convolution mass, the full relative covariance, and the full-jet interpolation on the **image** of the filtered polynomial family in (6.4). These determine the same $K_M,\mathcal Z_M$ as the preceding work. The sum map retains $A_k$ and every repeated eigenline, so a bound sublinear in $k$ would still have the intended force. No such bound is proved in this note.

The concrete advances are the exact filtered symmetric relation algebra, an all-$k$ spectral-sum norm realization, and a full nilpotent direct-image decomposition that retains multiplicities and colliding occupations. They are new applications to this specified programme; the reusable algebra and integration tools are standard and are not asserted to be globally novel.

## References and reading scope

1. Supplied **Tau Kernel Layer Integration**, RESEARCH_NOTE.md and NOTE.tex; read in full in this continuation. Its finite-layer identifications and sharper rank are retained as source results.
2. Supplied **Tau Symmetric Frontier Control**, RESEARCH_NOTE.md; read in full. Its signed projector, orbit factors, next-layer map, and finite bound are retained.
3. Supplied **Tau Coherent Interpolation Control**, especially polynomial/jet definitions and joint total-degree sections; used as stated analytic input.
4. The Stacks Project, Tag **0AVV**, affine pushforward of quasi-coherent complexes; Tag **0AWZ**, the precise categories for the finite-pushforward adjoint. https://stacks.math.columbia.edu/tag/0AVV and https://stacks.math.columbia.edu/tag/0AWZ .
5. NIST DLMF, §18.2, polynomial moment and kernel background. https://dlmf.nist.gov/18.2 .
6. Deligne, *La conjecture de Weil II*, IHES 52 (1980), 137–252. The retained French TeX window around §§3.2.11–3.2.15 was reread. Its line 872 contains an inconsistent numerical implication in the historical transcription; that literal line is not used as a proof step here. The source-based tensor/pushforward architecture is used, not a certification of the entire 116-page proof. Original bibliographic record: https://archive.numdam.org/articles/10.1007/BF02684780/ .
