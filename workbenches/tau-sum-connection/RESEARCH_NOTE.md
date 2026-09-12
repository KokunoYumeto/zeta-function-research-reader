# Sum-fibre differential control and the conormal trace

Additive continuation of `tau-spectral-sum` at PR #17, commit `33b29f706008124886614ba4bd55bffc489df9e2`. This is a written research contribution for review, not a new Lean certificate or a proof of RH. Existing scalar definitions, original quotient relations and formalization sources are unchanged.

## 1. Fixed source and arithmetic mass

Keep the original marked tau base and the square

$$\begin{array}{ccc}G(\mathbb Z)&\longrightarrow&G(\mathbb C)\\p_{\mathbb Z}\downarrow&&\downarrow p_{\mathbb C}\\\mathbb Z&\longrightarrow&\mathbb C.\end{array}$$

The arithmetic quotient has infinite target. A complex-linear map lifts by $(\lambda,v)\mapsto(\lambda,Tv)$ and fixes external tau; a relation goes to its receiving supported zero, not tau.

The analytic inputs remain those of the preceding notes: $D=-x\partial_x$, $C_+=[V\xrightarrow\Theta\mathscr B]$, $Q=\mathscr B/\Theta V$, $g=2\xi$, and

$$\mathcal M\Theta\phi=gH_\phi,\qquad H_{\phi_*}=1.$$

For a finite reflection-stable packet of actual zeros with full multiplicities, retain $h=\prod(s-\rho)^{m_\rho}$, $d=\deg h$, $v_h=g/h$, and the actual $F_h\in\mathscr B$ satisfying $\mathcal MF_h=v_h$. The full jet map includes the unit $\upsilon_h=j_hv_h$.

Set

$$a_h(t)=\frac{v_h(1/2+it)}{\sqrt{2\pi}},\quad w_h=|a_h|^2,\quad \mu_h=\int w_h=\|F_h\|_{L^2(dx)}^2.$$

No mass is assigned one. Reflection gives $v_h^\dagger=(-1)^dv_h$, so $\overline{a_h(t)}=(-1)^da_h(t)$. Hence

$$\mathcal I_h:=\int\frac{w_h'^2}{w_h}=4\int|a_h'|^2=4\int_0^\infty(\log x)^2|F_h(x)|^2dx<\infty,\qquad\int\overline{a_h}a_h'=0.$$

The formula is proved away from the discrete zero set by $w_h'=2\overline{a_h}a_h'$, and extends as an integral over the whole line. Mellin Plancherel supplies the second equality. Thus no bounded logarithmic score or log-concavity is assumed.

## 2. Quantitative sum contraction with its complete relative term

For $k\ge2$, use $u=\sum t_i$, $y_i=t_i-u/k$ for $i<k$, and $y_k=-\sum_{i<k}y_i$. The inverse is $t_i=u/k+y_i$; the real Jacobian has absolute value one. For two factors the previous coordinate is $v=2y_1$, retaining its Jacobian $1/2$.

Put

$$\Psi_k(u,\mathbf y)=\prod_i a_h(u/k+y_i),\qquad m_k(u)=\int|\Psi_k|^2d\mathbf y=w_h^{*k}(u),\qquad\int m_k=\mu_h^k.$$

The fibre is $\mathscr H_u=L^2(d\mathbf y)$. Its actual line projection is

$$\Pi_{0,u}Z=\Psi_k\frac{\langle\Psi_k,Z\rangle}{m_k},\qquad n_k=(1-\Pi_{0,u})\partial_u\Psi_k=\partial_u\Psi_k-\frac{m_k'}{2m_k}\Psi_k.$$

Every $m_k(u)>0$ because $w_h$ is positive almost everywhere. All entries are smooth and integrable by the source's Schwartz estimates.

**Theorem.** With $\mathcal I_{h,k}=\int m_k'^2/m_k$,

$$\boxed{\mathcal I_{h,k}+4\int\|n_k(u)\|^2du=\frac{\mu_h^{k-1}}{k}\mathcal I_h.}$$

**Proof.** Differentiation at fixed relative coordinates gives

$$\partial_u\Psi_k=\frac1k\sum_i a_h'(t_i)\prod_{j\ne i}a_h(t_j).$$

Its integrated squared norm has $k$ diagonal terms $\mu_h^{k-1}\|a_h'\|^2$ and $k(k-1)$ cross terms $\mu_h^{k-2}|\int\overline{a_h}a_h'|^2=0$, all divided by $k^2$. Therefore it is $\mu_h^{k-1}\mathcal I_h/(4k)$. Fixed phase gives $\langle\Psi_k,\partial_u\Psi_k\rangle=m_k'/2$. Orthogonal decomposition into that line and $n_k$ proves the formula. This is the standard Fisher-information projection mechanism applied with the actual arithmetic amplitude, mass and relative residual retained.

The map $(\Pi_{0,u}\partial_u\Psi_k,n_k)\mapsto\partial_u\Psi_k$ is addition of orthogonal components. Neither component is removed when it has supported zero amplitude.

## 3. The full matrix connection

Use independent relative polynomials $\theta_\alpha(\mathbf z)$, $z_i=s_i-S/k$, independent of $S=\sum s_i$. The original filtered numerator is exactly $P=\sum\theta_\alpha f_\alpha(S)$, with $\deg f_\alpha\le M-\deg\theta_\alpha$.

Define

$$j_uc=\Psi_k\sum_\alpha\theta_\alpha(i\mathbf y)c_\alpha,\quad W=j^*j,\quad B=j^*j',\quad T=(j')^*j'.$$

These are the full matrix-weight integrals, not just their constant entry. Positivity of $W$ follows from independence of the polynomials and the almost-everywhere nonzero amplitude. Fixed phase gives $B=W'/2$. Put

$$\Pi=jW^{-1}j^*,\qquad\Gamma=W^{-1}B,\qquad N=(1-\Pi)j'.$$

Direct multiplication proves

$$\boxed{\partial_u(jc)=j(c'+\Gamma c)+Nc,\quad j^*N=0,\quad \Gamma^*W+W\Gamma=W',}$$

$$\boxed{N^*N=T-B^*W^{-1}B\succeq0,\quad
\|\partial_u(jc)\|^2=(c'+\Gamma c)^*W(c'+\Gamma c)+c^*N^*Nc.}$$

For an invertible varying frame $C(u)$, the exact maps are

$$W^C=C^*WC,\qquad\Gamma^C=C^{-1}\Gamma C+C^{-1}C',\qquad N^C=NC.$$

In particular the derivative term is retained when using the preceding pointwise triangular square-completion map. The exact transformed polynomial image is retained; it is not enlarged to all measurable sections.

The Mellin-coordinate unitary $\mathscr U_k$ connects these derivatives to the original arithmetic operators:

$$\mathscr U_kD^{(k)}=(k/2+iu)\mathscr U_k,\qquad
\partial_u\mathscr U_k=i\mathscr U_k\mathscr L_k,\quad
\mathscr L_k=\frac1k\sum_i\log x_i,\quad[D^{(k)},\mathscr L_k]=-1.$$

For actual filtered coefficients $c_P$, retain the graph of $(j\nabla c_P,Nc_P)$. Adding its two entries recovers $\partial_u\mathscr U_k\mathcal T_kP$. On this exact graph, applying $-i\mathscr U_k^{-1}$ and then the original full-jet map is defined. No arithmetic-jet map on a freely chosen measurable normal component is asserted.

## 4. The derivative of an original supported relation is its Jacobian

One variable already supplies the exact source equation

$$\boxed{J_h(\log x\,\Theta\phi)=j_h(g')j_h(H_\phi).}$$

Proof: differentiate $\mathcal M\Theta\phi=gH_\phi$ before reducing modulo $h$. The term $gH_\phi'$ then maps to zero; $g'H_\phi$ remains. For $\phi=P(D)\phi_*$, every polynomial remainder $[P]_h$ is obtained.

The correct domain retaining this derivative is constructed as follows. Put $\mathcal P=\mathbb C[s_1,\ldots,s_k]$, $I=(h(s_i))$, $E=\mathcal P/I$, $E^{[2]}=\mathcal P/I^2$. Then

$$0\to I/I^2\to E^{[2]}\xrightarrow{\pi}E\to0,\qquad
E^k\xrightarrow{\sim}I/I^2,\quad(a_i)\mapsto[\sum_i h(s_i)\widetilde a_i].$$

For a nonempty packet, so $d\ge1$, monic division proves the isomorphism: $\mathcal P$ is free over $\mathbb C[h(s_1),\ldots,h(s_k)]$ with basis $s^\alpha$, $0\le\alpha_i<d$; only degrees zero and one in the latter variables survive modulo $I^2$.

For the empty packet $h=1$, with the same $k\ge2$, every generator $h(s_i)$ is $1$. Thus $I=\mathcal P$ and $I^r=\mathcal P$ for every $r\ge1$: $E$, $E^{[2]}$, $I/I^2$, all higher quotient spaces, and all associated-graded pieces are zero. Their quotient and derivative maps are the unique zero maps on these underlying modules; in particular $\delta_S(S)=1_E$ reads $0=0$ in the zero ring. Their split lifts still retain supported zero separately from external $\tau$. The analytic amplitude $v_1=g$, its actual mass $\mu_1$, and the analytic definitions and estimates above remain unchanged.

The derivative at fixed relative coordinates descends as the complex-linear map

$$\boxed{\delta_S:E^{[2]}\to E,\quad[P]\mapsto\left[\frac1k\sum_i\partial_{s_i}P\right],\qquad
\delta_S(a_i)=\frac1k\sum_i h'(s_i)a_i\text{ on }I/I^2.}$$

The first assertion uses $\partial_S(I^2)\subset I$. Its relative Leibniz rule is $\delta_S(ab)=\pi(a)\delta_S(b)+\pi(b)\delta_S(a)$, with $\delta_S(S)=1$. The full conormal differential is the diagonal map $(a_i)\mapsto\sum h'(s_i)a_i\,ds_i$; contraction by $\partial_S$ gives the displayed row.

Its original split maps have explicit types: $G(\pi)$ is a semiring homomorphism; $\delta_S^\tau$ is a $G(\mathbb C)$-linear map of coefficient semimodules. A nonzero conormal class maps to supported zero under $G(\pi)$, while its derivative can be the nonzero supported value in the row above. Both maps retain external absence. No extra scalar zero is adjoined.

Retain the analytic unit $U=\prod_i(g/h)(s_i)$ and its actual Taylor class $\widehat U$ modulo $I^2$. Define $\widehat{\mathcal J}P=\widehat U[P]_{I^2}$ and $\beta=U^{-1}\delta_S\widehat U$. Product differentiation gives

$$\boxed{J^{(k)}\mathscr L_k\mathcal T_kP
=\delta_S\widehat{\mathcal J}P
=\mathcal J(\partial_SP)+\beta\mathcal JP.}$$

For the original relation $P=\sum_i h(s_i)P_i$ this is

$$\boxed{J^{(k)}\mathscr L_k\mathcal T_kP=\frac1kU\sum_i h'(s_i)[P_i]_I.}$$

Modulo $I$, the corresponding factor $v_h(s_i)h'(s_i)$ is exactly $g'(s_i)$, with all remaining $v_h$ factors retained. The local multiplicity factors and nonconstant units have not been discarded.

Pairing the one-variable formula with the existing residue duality yields

$$\boxed{\mathscr R_Z(f,J_h(\log x\,\Theta(P(D)\phi_*)))
=\sum_{\rho\in Z}m_\rho\overline{f(1-\bar\rho)}P(\rho).}$$

This is the original arithmetic multiplication trace, from the residues of $g'/g$, obtained by differentiating an actual theta relation before its supported quotient.

## 5. Higher layers, actual signs, and scope

For every $r\ge1$, the same derivation gives $\mathcal P/I^{r+1}\to\mathcal P/I^r$. Under

$$\operatorname{gr}_I\mathcal P\cong E[\eta_1,\ldots,\eta_k],\qquad\eta_i\leftrightarrow[h(s_i)],$$

its degree-minus-one part is

$$\frac1k\sum_i h'(s_i)\partial_{\eta_i}.$$

Every multiplicity $\alpha_i$ in differentiating $\eta^\alpha$ remains. These graded pieces are higher relation fibres, not repeated scalar adjunctions.

The full mixed derivative retains the product Jacobian:

$$\left[\partial_{s_1}\cdots\partial_{s_k}(UP\prod_i h(s_i))\right]_I
=\left[UP\prod_i h'(s_i)\right]_I
=\left[P\prod_i g'(s_i)\right]_I.$$

The original primitive for $h(s_i)P_i$ keeps its $(-1)^{i-1}$ coefficient and the matching cochain differential sign. The ordered residue form and tensor-duality signs are not replaced by an unsigned supertrace.

The old control remains $W_M=A_k^*G_M+G_MA_k-kG_M$, with the full-jet inverse comparison from Kernel Layer Integration. The new estimate concerns the sum density's differentiated amplitude, connected to that operator by the explicit logarithmic commutator and the conormal map. It is not yet a uniform sublinear bound for that whole finite-packet control. The full matrix terms and the exact filtered graph above specify the additional quantities needed; the scalar contraction alone is not used to certify them.

## Evidence and references

The expanded conversation package contains the complete proof, twenty-method exact checker, source-manifest receipts, a bounded formalization handoff, and the HTML/LaTeX reader. Both normal and optimized runs of that checker passed; deliberate-failure controls failed. The attachment's eighteen-method suite also passed independent reruns. These are finite regression tests, not new Lean certificates. Actual theta-seed quadrature at two precisions is explicitly numerical rather than interval-certified.

Standard ingredients: Johnson and Barron, *Fisher Information inequalities and the Central Limit Theorem*, arXiv:math/0111020; Stacks Project, Tags 00S0 and 08SH, conormal and complete-intersection cotangent complexes. The source's Deligne tensor/pushforward/dual-control architecture motivates estimating this actual pushforward; no finite-field purity theorem is applied merely by renaming the base.
