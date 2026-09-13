# Final mathematical integration review of R33–R37

This review reads the complete appended conclusion against the complete TVB.1–TVB.44 proof, TI.1–TI.32 proof, TC1–TC13 calibration and the original supplied parent join. Its object is the actual source-to-conclusion integration: hypotheses, domains, maps, measures, signs, constants, endpoints, numerical scope and the four retained losses. Every equation group in those proof sources was read in order. The source appendices and the independent computational receipts were inspected at the scopes stated below. No Lean process, new numerical replay, PDF edit, source-chapter edit, stage edit or frozen-release edit was performed by this reviewer.

The reviewed conclusion is `output/split_zero_rh_tandem_2026-09-12/tex/research_conclusion.tex`, SHA256 **`b0aaab31ed11d56650919d9abfc12a6e74c431263912a9e713d845c93f8808c2`**. Its appended section begins with “The original Toda volumes and the complete four-term loss” and includes R33–R37 and all intervening and following prose. The full amended section was read after the corrections recorded in section 9.

## 1. Source identities and exact scope

The full source pins used for the mathematical comparison are:

| Source | SHA256 | Complete reading |
| --- | --- | --- |
| `work/toda_cv_exact_bridge_20260912.tex` | `9d38489ac9e7e2f529266403ace0f69641e4da6ef7a8cf46f64179ab572c1c71` | Complete source, definitions and proofs TVB.1–44, including TVB.38a–c and crosswalk |
| `work/toda_theta_input_tail_20260912.tex` | `e50a11c51293017b1a433f3ed9b499947a953e6b2955f59f3c46f14ed26a409d` | Complete source and proofs TI.1–32, certificate statement and scope |
| `work/toda_exterior_equality_calibration_20260913.tex` | `772e2cd7efef88cd9591d1918b6a1fbcacbede51cbef50d109b33b246a79238f` | Complete source and calculations TC1–13 |
| `output/split_zero_rh_tandem_2026-09-12/sources/web_toda_parent_join/PARENT_EXACT_JOIN.md` | `71e275a8543448e57bcfafc5ead8cf3c7f98d594ae994582d1180999d98c6370` | Complete original supplied join, including evidence and endpoint qualifications |

The final bridge pin is **97652a43445708c0e6d2a959f45aed8a4f2a7f73f9cd4b6cd57e67b8fedb408e**. Its two final domain additions were read and checked; exact reversal of those additions reconstructs the fully read earlier pin in the table. The delta proof and acceptance are recorded in section 10.

R33–R34 now explicitly use an integer tensor degree $k\ge1$, a nonempty actual dagger-stable packet with its complete selected zero orders, the original annihilator degree $q\ge1$, real $|\theta|<\pi/2$, and $N\ge q$, except for the separately written first degree $N=q-1$. R35 explicitly specializes to the original observation $\theta=0$, $N\ge q$, and positive full spectral excess $L>0$. R36 explicitly restricts its absolute-square integral to real $|\theta|<\pi/2$. Its analytic strip continuation is proved through the holomorphic Laplace integral and, for the seed, the holomorphic two-factor integral; the absolute-square notation is not used as a holomorphic function of complex $\theta$. R37 retains the declared Gaussian fixture $\mu>0,\sigma>0,k=1,c=1/2$ from TC1.

## 2. Original objects, quotient and actual metric

The arithmetic source is

\[
g(s)=s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)=2\xi(s),\qquad
v_h=g/h,\qquad w_h(t)=\frac{|v_h(1/2+it)|^2}{2\pi}.
\]

Division by the complete order at each selected zero makes $v_h$ entire and its local constant coefficient nonzero. The exact jet map sends an entire function to its Taylor polynomial in each factor $\mathbb C[t]/(t^{m_\rho})$, then uses the inverse Chinese remainder map. The element $\upsilon_h=[v_h]_h$ is a unit: if its local coefficients are $a_j$, its inverse coefficients obey $b_0=a_0^{-1}$ and $b_n=-a_0^{-1}\sum_{j=1}^n a_jb_{n-j}$. Multiplication verifies the inverse with every retained jet coefficient.

Set $I=(h(s_1),\ldots,h(s_k))$, $S=\sum_i s_i$, and let $\chi$ generate the exact contraction $I\cap\mathbb C[S]$. Monic division by its least-degree monic element proves that it generates that whole ideal. Thus

\[
C=\mathbb C[S]/(\chi),\quad A=M_S:C\to C,
\quad \eta[P]=\upsilon_h^{\otimes k}[P(S)]_I
\]

is the same injective map into $(E_h^{\otimes k})^{\mathfrak S_k}$ as the cyclic construction: its kernel is zero because the unit is invertible and the other factor has exactly the stated contraction kernel. This retains the arithmetic class used by every subsequent quotient metric.

For the original $D=-x\partial_x$, the polynomial source map is

\[
\mathcal VP=P(D_1+\cdots+D_k)F_h^{\otimes k},\qquad
\|\mathcal VP\|^2=\int_{\mathbb R}|P(c+iu)|^2m_k(u)\,du,
\quad m_k=w_h^{*k},\quad \int m_k=\mu_h^k.
\]

Here $c=k/2$ and $\mu_h=M_h(0)$. The sum map is the actual change $(y_1,\ldots,y_{k-1},u)\mapsto(y_1,\ldots,y_{k-1},u-\sum_i y_i)$, with determinant $1$ in that order and $(-1)^{k-1}$ if $u$ is put first. Integrating the full product density in $y$ gives $m_k$, without dividing by its mass.

For real $|\theta|<\pi/2$, the actual tilted pairing is

\[
\langle P,Q\rangle_\theta
=\int\overline{P(c+iu)}Q(c+iu)e^{\theta u}m_k(u)\,du.
\]

TVB.5 and TI.14 prove locally uniform convergence of all polynomially weighted derivatives on compact substrips. The multiplication map $f(u)\mapsto e^{\theta u/2}f(u)$ is the exact isometry from this weighted ambient space to the untilted one; it changes the polynomial image. The $R_N,G_N,I_N,O_N$ used below belong to the actual current tilted pairing and fixed polynomial coordinates, not to an unchanged polynomial image under that multiplication.

Let $\mathcal P_N=\mathbb C[S]_{\le N}$. For $m=N-q+1\ge0$, monic division proves the exact sequence

\[
0\longrightarrow\mathcal P_{m-1}
\xrightarrow{\;Q\mapsto\chi Q\;}\mathcal P_N
\xrightarrow{\;T_N:P\mapsto[P]_\chi\;}C\longrightarrow0,
\]

with $\mathcal P_{-1}=0$. Its kernel is $\mathcal D_N=\chi\mathcal P_{m-1}$. The least-norm section $R_N:C\to\mathcal P_N$ is uniquely characterized by $T_NR_N=I_C$ and $\operatorname{im}R_N=\mathcal D_N^\perp\cap\mathcal P_N$. In original source monomial coordinates, if $M_N$ is the source Gram and $J_N$ is the quotient matrix, then

\[
K_N=J_NM_N^{-1}J_N^*,\quad G_N=K_N^{-1},\quad
R_N=M_N^{-1}J_N^*G_N.
\]

Multiplication verifies the quotient identity, orthogonality to the kernel and $R_N^*M_NR_N=G_N$. Pythagoras proves the minimum property. The source density is positive almost everywhere, so a nonzero polynomial has strictly positive norm and all admitted source and quotient Grams are positive definite.

## 3. R33: original determinants, retained phase and positive minors

With $Z=M_h^k$, differentiating under the proved integral gives

\[
\mathscr L(SP)=(c+i\partial_\theta)\mathscr L(P),\qquad
Z_\chi=\overline\chi(c-i\partial_\theta)\chi(c+i\partial_\theta)Z
=\int|\chi(c+iu)|^2e^{\theta u}m_k(u)\,du.
\]

The minus sign is the conjugate factor in the original sesquilinear pairing; both polynomial factors remain. The real-coordinate source and relation Hankel matrices therefore are exactly $Z^{(a+b)}$ and $Z_\chi^{(a+b)}$. Their determinants are $\mathfrak D_n$ and $\mathfrak B_m$, with dimension-zero value one. The coordinate map from powers of $u$ to powers of $S$ retains

\[
S^j=\sum_{r=0}^j\binom jr c^{j-r}i^ru^r,
\quad \det C_n=i^{n(n-1)/2},\quad |\det C_n|^2=1.
\]

Thus the Hankel determinants equal the original monomial Gram determinants. This is an exact congruence with its phase, rather than a replacement measure or a rescaled polynomial.

Choose the least-norm lifts of $1,S,\ldots,S^{q-1}$, followed by the monic relation basis $\chi,\chi S,\ldots,\chi S^{m-1}$. Their coefficient change from the original monomial basis has determinant one: each quotient lift differs from its polynomial representative by a relation, and the monic ordered relation block is triangular with diagonal one. The two blocks are orthogonal. Taking the determinant of their full Gram proves

\[
V_N=\det G_N=\mathfrak D_{N+1}/\mathfrak B_m.
\]

Putting the kernel block first changes the determinant-line map by the original sign $(-1)^{qm}$. The source alternation map has squared norm factor $n!$ on an $n$-fold wedge, and the original tensor cochain degree is retained in TVB.15 and TVB.31; no invisible division by these factors enters R33.

Let $p_j$ be the source monic orthogonal polynomials, $\omega_j=\|p_j\|_\theta^2$, $b_j=[p_j]_\chi$, and $r_j$ the relation monic orthogonal polynomials with $\nu_j=\|\chi r_j\|_\theta^2$. Orthogonal source coordinates give

\[
K_N=\sum_{j=0}^N\frac{b_jb_j^*}{\omega_j}.
\]

For $N\ge q$, both $K_{N-1}$ and $K_N$ are positive definite. The rank-one determinant identity and inverse update, applied to the displayed original $b_N/\sqrt{\omega_N}$, give

\[
\delta_N=\frac{V_N}{V_{N-1}}=\frac{\omega_N}{\nu_{m-1}},\quad
\frac{b_N^*G_Nb_N}{\omega_N}=1-\delta_N,\quad
b_{N+1}^*G_Nb_{N+1}=\nu_m-\omega_{N+1}
=\omega_{N+1}(\delta_{N+1}^{-1}-1).
\]

In particular $0<\delta_N\le1$. The last identity follows directly from the orthogonal decomposition $\chi r_m=p_{N+1}-R_Nb_{N+1}$, so it retains the full next relation norm.

In the real variable $X=(S-c)/i$, dagger stability makes $\operatorname{Tr}X=(\operatorname{Tr}A-cq)/i$ real. The trace of the compression of multiplication by $X$ to the least-norm image is $\partial_\theta\log V_N$. The exact next-boundary trace calculation TVB.25–26, including the coordinate change $S=c+iu$, yields

\[
z_N:=b_N^*G_Nb_{N+1}=i\omega_N\psi_N,\qquad
\psi_N=\frac{\operatorname{Tr}A-cq}{i}-\partial_\theta\log V_N\in\mathbb R.
\]

No ordinary-conjugation symmetry or zero phase is imposed here. The full trace of the square of the relative rank-two operator before that identity is $(2a d_++2\operatorname{Re}(z_N^2))/\omega_N^2$, where $a=b_N^*G_Nb_N$ and $d_+=b_{N+1}^*G_Nb_{N+1}$. As $z_N$ is purely imaginary, $2\operatorname{Re}(z_N^2)=-2|z_N|^2$, and the trace-zero rank-two radius is $\epsilon_N^2=\operatorname{Tr}(H_N^2)/2=(a d_+-|z_N|^2)/\omega_N^2$. Substituting the three displayed scalar identities gives the first radius formula in R33, with the subtraction $-\psi_N^2$.

TVB.27–31 perform the corresponding determinant lemma and exterior expansion on the same $b_j$ matrix. The positive minor sum $\Delta_N$ is the squared original wedge-source norm: its source vector uses the conjugates of the actual minors and the product of original $\omega_j^{-1}$, so the wedge orthogonality gives exactly that sum. The signed determinant decomposition retains the omitted direction with its exact phase contribution $\psi_N^2/\alpha_{N+1}$. Consequently

\[
\epsilon_N^2=\alpha_{N+1}\frac{\Delta_N}{\det K_N},
\quad \alpha_{N+1}=\omega_{N+1}/\omega_N,
\]

at precisely the same $N,\theta,h,k$. This proves the second equality in R33 without using a different quotient, selected minor or metric.

## 4. First degree, q=1 and the empty packet

At $N=q-1$, $T_{q-1}$ is an isomorphism, so no $G_{q-2}^{-1}$ is required. Write the complete monic expansion

\[
\chi=p_q+\sum_{j<q}\gamma_jp_j.
\]

It gives $b_q=-\sum_{j<q}\gamma_jb_j$, $\nu_0=\omega_q+\sum_{j<q}|\gamma_j|^2\omega_j$, and $\gamma_{q-1}=-i\psi_{q-1}$. Substitution into the rank-two formula proves

\[
\epsilon_{q-1}^2
=\frac{\nu_0-\omega_q}{\omega_{q-1}}-\psi_{q-1}^2
=\frac{\sum_{j<q-1}|\gamma_j|^2\omega_j}{\omega_{q-1}}.
\]

This also corrects the delivered note's earlier vector/scalar notation slip: the scalar $\nu_0-\omega_q$ is $b_q^*G_{q-1}b_q$, whereas $b_q$ itself is a quotient vector. The final conclusion uses the correct scalar.

For $q\ge2$, put $D=\det K_{q-1}=\prod_{j<q}\omega_j^{-1}$, $I_j=\{0,\ldots,q-2\}\setminus\{j\}$, and

\[
e_j=\left(\bigwedge_{i\in I_j}p_i\right)\wedge p_{q-1}\wedge p_q.
\]

The exact endpoint correspondence is

\[
\mathcal H:\mathcal P_{q-2}\to\mathcal E_{q-1},\qquad
\sum_{j<q-1}a_jp_j\longmapsto
\sum_{j<q-1}(-1)^{q-j}\overline{a_j}\frac{\omega_jD}{\omega_q}e_j.
\]

The sign follows by putting the final $b_j$ into position $j$ in its minor, including the minus sign in $b_q=-\sum\gamma_jb_j$. The inverse sends $\sum t_je_j$ to $\sum(-1)^{q-j}\omega_q\overline{t_j}p_j/(\omega_jD)$. Each $e_j$ has squared norm $\omega_q/(D\omega_j)$, and the source and target basis vectors are pairwise orthogonal. Therefore

\[
\|\mathcal HP\|^2=\frac D{\omega_q}\|P\|^2,\quad
\zeta_{q-1}=\mathcal H(\mathsf P_{q-2}\chi),\quad
\Delta_{q-1}=\frac D{\omega_q}\|\mathsf P_{q-2}\chi\|^2.
\]

Thus the factor written after R33 is the **squared-norm factor**. The ordinary norm factor is its positive square root. The corrected conclusion states the former exactly. The alternating tensor image has squared norm $q!D\|\mathsf P_{q-2}\chi\|^2/\omega_q$, and the omitted top coefficient remains $D|\gamma_{q-1}|^2\omega_{q-1}/\omega_q$.

For $q=1$, the endpoint correspondence is the unique map between the two zero spaces. Multiplication on the one-dimensional quotient is a scalar fixed by the dagger involution, hence its real part is $c$ and $A^\sharp+A-2cI=0$ in every admitted positive metric. Thus $\epsilon_N=0$ for every $N\ge0$. For $N\ge1$, consecutive monic orthogonal polynomials cannot share a root: their three-term recurrence has nonzero positive coefficient, so such a root would propagate to $p_0=1$. Hence $b_N,b_{N+1}$ cannot both vanish. The two-step kernel update is nonzero positive semidefinite, giving $V_{N-1}/V_{N+1}>1$. Its Toda upper expression is strictly positive, exactly as the added q=1 sentence states.

For $h=1$, $\chi=1,q=0,C=0$. The source sequence is multiplication by one on $\mathcal P_N$, followed by the zero quotient. Thus $Z_\chi=Z$, $\mathfrak B_{N+1}=\mathfrak D_{N+1}$, $V_N=1$ for $N\ge0$, and the minimum lift and curvature maps are the unique zero maps. Source norms and the positive seed mass still exist. This proves the exact source-to-zero-quotient map supporting the q=0 statement; it does not identify the positive seed norm with a quotient norm.

## 5. R34: each curvature map and each positive cost

Every derivative here is taken in fixed polynomial coordinates while differentiating the actual weight $e^{\theta u}$. Differentiating $T_NR_N=I$ gives $R_N'x\in\mathcal D_N$. Differentiating orthogonality of $R_Nx$ against every fixed boundary polynomial gives

\[
R_N'=-I_N,\quad I_N=P_{\mathcal D_N}XR_N:C\to\mathcal D_N,
\quad O_N=(1-P_N)XR_N:C\to\mathcal P_{N+1}\cap\mathcal P_N^\perp,
\]

where $P_N$ is the actual tilted source projection onto $\mathcal P_N$. It is distinct in type and formula from the quotient spectral projection $\mathsf P:C\to C$ in R35.

Differentiating $G_N=R_N^*R_N$ with the weight derivative gives

\[
G_N'=R_N^*XR_N,\qquad
G_N''=R_N^*X^2R_N-2I_N^*I_N.
\]

The three components of $XR_N$, in $\mathcal D_N$, $\operatorname{im}R_N$, and $\mathcal P_N^\perp$, are orthogonal. The middle projection is $R_NG_N^{-1}R_N^*$. Subtracting its squared contribution $G_N'G_N^{-1}G_N'$ therefore leaves exactly $O_N^*O_N-I_N^*I_N$. These are maps $C\to C^{\mathrm{anti}*}$: for example $O_N^*O_Nx$ sends $y$ to $\langle O_Ny,O_Nx\rangle_\theta$. Fixed Euclidean coefficient coordinates identify that antidual with the displayed matrix. The traces in R34 compose these forms with the actual inverse metric $G_N^{-1}$.

The source leading coefficient of $X=(S-c)/i$ is $-i$. The exact rank-one formulas TVB.20 give

\[
O_Nx=-i p_{N+1}\frac{b_N^*G_Nx}{\omega_N},\qquad
I_Nx=-i\chi r_{m-1}\frac{b_{N+1}^*G_Nx}{\nu_{m-1}}\quad(m\ge1).
\]

The second minus sign includes conjugating the coefficient when moving the self-adjoint $X$ across the pairing, followed by $\langle\chi r_m,R_Nx\rangle=-b_{N+1}^*G_Nx$. The original norms of $p_{N+1}$ and $\chi r_{m-1}$ then give

\[
\operatorname{Tr}(G_N^{-1}O_N^*O_N)
=\frac{\omega_{N+1}}{\omega_N^2}b_N^*G_Nb_N
=\alpha_{N+1}(1-\delta_N),
\]

\[
\operatorname{Tr}(G_N^{-1}I_N^*I_N)
=\frac{b_{N+1}^*G_Nb_{N+1}}{\nu_{m-1}}
=\frac{\nu_m-\omega_{N+1}}{\nu_{m-1}}
=\beta_m-\alpha_{N+1}\delta_N.
\]

Both costs retain their shared subtracted quantity $\alpha_{N+1}\delta_N$. Their difference is $\alpha_{N+1}-\beta_m$, matching the difference of the two scalar Toda curvatures. At $m=0,N=q-1$, the boundary space is zero, so $I_N=0$; the source coefficient $b_N^*G_Nb_N=\omega_N$ gives the other cost $\alpha_q$. No $\nu_{-1}$ is defined or required.

The derivative boundary is also an actual differential in the original tensor complex. Ordered monic division gives polynomials $Q_i$ with $\chi(S)=\sum_i h(s_i)Q_i(s_1,\ldots,s_k)$. For any polynomial $P$, the precise primitive is

\[
\sum_{i=1}^k(-1)^{i-1}Q_i(D_1,\ldots,D_k)P(D_1+\cdots+D_k)
\bigl(F_h^{\otimes(i-1)}\otimes\phi_0\otimes F_h^{\otimes(k-i)}\bigr),
\]

where $\phi_0=(4\pi^2x^4-6\pi x^2)e^{-\pi x^2}\in V$, $h(D)F_h=\Theta\phi_0$, and the complex is $(V\xrightarrow{\Theta}\mathscr B)^{\otimes k}$. Its first $i-1$ factors have cochain degree one, so the differential contributes the second $(-1)^{i-1}$. Their product is $1$, yielding the complete relation $\mathcal V(\chi P)$. Euler differentiation preserves the original spaces and commutes with $\Theta$. This supplies the literal map claimed by the sentence after R34.

## 6. R35: all four losses in one original metric

At $\theta=0,N\ge q$, retain $A^\sharp=G_N^{-1}A^*G_N$ and $\mathcal H_N=A^\sharp+A-kI$. Let $C_+$ be the full generalized spectral subspace of $A$ with $\operatorname{Re}\lambda>c$, let $C_-=C_+^{\perp_{G_N}}$, and let $\mathsf P$ be the orthogonal projection onto $C_+$. Every generalized multiplicity is retained in

\[
L=\sum_{\operatorname{Re}\lambda>c}\ell_\lambda(2\operatorname{Re}\lambda-k).
\]

For $L>0$, the proved trace bound gives $\epsilon_N>0$. The $G_N$-unit eigenvectors $u_+,u_-$ at $\pm\epsilon_N$ are orthogonal. Define $E:\mathbb C^2\to C$ by $E(z_+,z_-)=z_+u_++z_-u_-$ and $M=E^\sharp\mathsf PE$. The standard metric on this two-dimensional coefficient domain is transported isometrically to the two actual eigenlines, since $E^\sharp E=I_2$. It does not replace $G_N$ on $C$. Direct quadratic forms give $0\le M\le I_2$.

In the original orthogonal decomposition $C=C_+\oplus C_-$, invariance of $C_+$ gives

\[
A=\begin{pmatrix}B&\mathsf C\\0&D^{\rm op}\end{pmatrix},\qquad
\mathsf C=\mathsf PA|_{C_-}:C_-\to C_+,
\quad \mathsf P\mathcal H_N|_{C_-}=\mathsf C.
\]

Put $a_\pm=\|\mathsf Pu_\pm\|_{G_N}^2$ and $z=\langle\mathsf Pu_+,\mathsf Pu_-\rangle_{G_N}$. Expanding the rank-two spectral decomposition gives

\[
L=\epsilon_N(a_+-a_-),\quad
\|\mathsf C\|_{\mathrm{HS},G_N}^2
=\epsilon_N^2(a_++a_--a_+^2-a_-^2+2|z|^2).
\]

The determinants of $M$ and $I_2-M$ are $a_+a_--|z|^2$ and $1-a_+-a_-+a_+a_--|z|^2$. Adding them to the preceding squared norm and to $L^2$ cancels all $a_\pm,z$ terms except $1$. Thus

\[
\epsilon_N^2-L^2=\|\mathsf C\|_{\mathrm{HS},G_N}^2
+\epsilon_N^2\{\det M+\det(I_2-M)\}.
\]

This proves the exterior part of the parent join with its full original metric. Each determinant is nonnegative because the corresponding matrix is positive semidefinite.

Set $v_N=-\log\delta_N\ge0$, $s_N=(v_N+v_{N+1})/2$, $t_N=(v_{N+1}-v_N)/2$. In the exact R33 expression,

\[
(1-e^{-v_N})(e^{v_{N+1}}-1)
=2e^{t_N}\cosh s_N-1-e^{2t_N}
=\sinh^2s_N-(e^{t_N}-\cosh s_N)^2.
\]

Retaining the $-\psi_N^2$ gives the exact Toda loss

\[
\alpha_{N+1}\sinh^2s_N-\epsilon_N^2
=\alpha_{N+1}(e^{t_N}-\cosh s_N)^2+\psi_N^2.
\]

Literal addition of these two equalities proves R35. Its four nonnegative terms are the actual volume imbalance square, the actual phase square, the original spectral coupling norm, and the two-dimensional compression determinant term. No term changes metric and no sign cancellation hides one of these quantities. Dropping only the first and fourth terms gives

\[
\log\frac{V_{N-1}}{V_{N+1}}
\ge2\operatorname{arsinh}\left(
\frac{\sqrt{L^2+\psi_N^2+\|\mathsf C\|_{\mathrm{HS},G_N}^2}}
{\sqrt{\alpha_{N+1}}}\right),
\]

because the left logarithm is $2s_N\ge0$. This is exactly the strengthened lower bound described after R35 and in the original parent join.

The spectral projector $Q$ is constructed from the full minimal polynomial factors $m_+,m_-$: if $a m_++b m_-=1$, then $Q=b(A)m_-(A)$. It has blocks $\left(\begin{smallmatrix}I&Y\\0&0\end{smallmatrix}\right)$, with $Y:C_-\to C_+$. The commuting relation $AQ=QA$ is exactly $BY-YD^{\rm op}=\mathsf C$, while $Q-\mathsf P$ has only the block $Y$. The map

\[
\mathscr S:\operatorname{Hom}(C_-,C_+)\to\operatorname{Hom}(C_-,C_+),\quad
Y\mapsto BY-YD^{\rm op}
\]

has inverse

\[
\mathscr S^{-1}(Z)=\int_0^\infty e^{-tB}Ze^{tD^{\rm op}}\,dt.
\]

On a selected full generalized block the first exponential is $e^{-t\lambda}\sum_{j<\ell_\lambda}(-t)^j(B-\lambda I)^j/j!$, with its spectral projector; the remaining exponential has its corresponding full positive-$t$ nilpotent polynomial. All selected real parts exceed $c$, and all remaining real parts are at most $c$, so every product is a polynomial times a strictly decaying exponential. The integral converges in the original operator norm. Differentiating the integrand gives $-B e^{-tB}Ze^{tD^{\rm op}}+e^{-tB}Ze^{tD^{\rm op}}D^{\rm op}$; the endpoint values are $Z$ and zero, proving the inverse identity with the stated sign. The same differentiation proves injectivity. The actual smallest singular value in the original Hilbert–Schmidt pairing therefore gives $\|\mathsf C\|\ge s_{B,D}\|Q-\mathsf P\|$, without a uniform lower bound being inserted. For the dagger-stable nonempty positive spectral selection, its reflected eigenvalues also show that the remaining space is nonzero.

For $L=0$, the proof uses the Toda identity directly; it does not assert positive eigenlines when $\epsilon_N=0$. The first degree $N=q-1$ uses the separate endpoint expression instead of a preceding-volume ratio. These restrictions in the original parent join are retained in the final conclusion and its full bridge.

## 7. R36: exact analytic maps, masses and certified interval scope

TI constructs the original theta series in the sector $|\arg z|<\pi/4$, with its principal logarithm, and retains

\[
\vartheta(z)=\sum_{n\in\mathbb Z}e^{-\pi n^2z^2},\quad
f_0(z)=D(D-1)\vartheta(z)
=2\sum_{n\ge1}(4\pi^2n^4z^4-6\pi n^2z^2)e^{-\pi n^2z^2}.
\]

The factor two is the sum of the positive and negative theta indices. Gaussian Fourier transformation and periodization prove $\vartheta(z)=z^{-1}\vartheta(1/z)$; applying $D(D-1)$, with $DR=R(1-D)$, gives the rapid endpoint bounds for $f_0$ and its Euler derivatives. Termwise Mellin integration initially for $\operatorname{Re}s>1$ gives $\mathcal Mf_0=g=2\xi$, with the substitution factor $1/2$ and both coefficients $4,-6$. The rapid endpoint integral proves entire continuation and both functional symmetries.

For the packet, entire Mellin division $g/h$ and inverse Mellin integration construct the same rapid sector function $F_h$, proving $h(D)F_h=f_0$. The exact Hilbert-space change is

\[
U:L^2(\mathbb R_{>0},dx)\to L^2(\mathbb R,dy),\quad
UF(y)=e^{y/2}F(e^y),\quad
U^{-1}u(x)=x^{-1/2}u(\log x).
\]

For real $|\theta|<\pi/2$, analytic translation on the constructed rapid sector functions is

\[
E_\theta F(y)=e^{(y+i\theta/2)/2}F(e^{y+i\theta/2}),\qquad
\mathcal F_+(E_\theta F_h)(t)=e^{\theta t/2}v_h(1/2+it).
\]

The source retains its phase $e^{i\theta/4}$. The Fourier kernel is $e^{ity}$, and Plancherel retains the $1/(2\pi)$ density. Therefore $M_h(\theta)$ is exactly the full positive-axis norm of $F_h(e^{i\theta/2}x)$.

Dagger stability yields

\[
F_h(e^{i\theta/2}/x)=(-1)^d e^{-i\theta/2}x\overline{F_h(e^{i\theta/2}x)}.
\]

Taking its squared modulus retains the $x^2$, which cancels the Jacobian of $x\mapsto1/x$. Thus the integral over $(0,1)$ equals the integral over $(1,\infty)$, proving the factor two in R36. Additional ordinary-conjugation stability, when present, proves evenness; dagger stability alone is not used to impose zero phase or evenness.

The source arrow $F_h\xmapsto{h(D)}f_0$ commutes with the Mellin/Fourier arrow $v_h(1/2+it)\xmapsto{h(1/2+it)}g(1/2+it)$. Squaring the original amplitudes gives $w_1=|h(1/2+it)|^2w_h$. At selected line zeros it holds by continuity of the globally divided entire function; no pointwise $0/0$ definition is required. This is the exact packet passage claimed by R36.

For the seed, TI.19 supplies the complete double sum with $c_1=-6,c_2=4$, $C_{mn}=\pi(m^2e^{i\theta}+n^2e^{-i\theta})$, the coefficient $4c_rc_s(\pi m^2)^r(\pi n^2)^s e^{i\theta(r-s)}$, and the term $\Gamma(r+s+1/2,C_{mn})/C_{mn}^{r+s+1/2}$. On each compact rectangle $|\operatorname{Re}\theta|\le\theta_0<\pi/2,|\operatorname{Im}\theta|\le B$, the real part of $C_{mn}$ is positive. The right-half-plane power and incomplete-gamma branch are proved from the integral $I_p(C)=\Gamma((p+1)/2,C)/(2C^{(p+1)/2})$.

The omitted square $m>J$ or $n>J$ is bounded by the explicit TI.23 quantity $16A_1A_{J+1}I_8(d_0(1+(J+1)^2))$, where $d_0=\pi e^{-B}\cos\theta_0>0$. The positive finite $A_a$ is built from the exact geometric/Stirling sums bounding each original polynomial coefficient. The bound follows by the complete product difference $(f^+-f_J^+)f^-+f_J^+(f^--f_J^-)$, including the outer factor two and both errors. It decreases to zero locally uniformly. The derivative tail is controlled by the written Cauchy estimate, and TI.25–30 separately compute the exact derivative polynomial $16y^3-60y^2+30y$, its $RH=-H$ sign, and its explicit tail $4B_1B_{J+1}I_{12}(\pi(1+(J+1)^2))$.

For $h=1$, the original even density has zero first moment. Its $k$-fold convolution has mass $\mu_1^k$ and second moment $k\mu_1^{k-1}M_1''(0)$. Therefore the first source monic squared-norm ratio is exactly $a_1^{(k)}=kM_1''(0)/M_1(0)$. No probability rescaling occurs: both original source norms are exhibited before taking their ratio.

The certificate inspected in this audit uses python-flint 0.9.0, Arb/Acb at 256 bits, one thread, and $J=8$. The complete source proof was read; the saved replay receipt and both mode-record identities were inspected. The replay receipt records exit zero for the ordinary and optimized normal runs, exit one for the two deliberate false-inequality controls, and identical mathematical records in the two successful modes. This reviewer did not rerun that certificate or claim a new numerical enclosure independent of it.

The saved successful record gives exactly these rational decimal intervals:

| Quantity | Lower endpoint | Upper endpoint |
| --- | --- | --- |
| $M_1(0)$ | 1.2790072478464851404795335922671932744916 | 1.2790072478464851404795335922671932744919 |
| $M_1(1/10)$ | 1.3459071784582497969682205923576298051604 | 1.3459071784582497969682205923576298051607 |
| $M_1''(0)$ | 13.0555493025705584353926846581231936824343 | 13.0555493025705584353926846581231936824346 |
| $a_1^{(k)}/k$ | 10.2075647534857216888657612522375551749964 | 10.2075647534857216888657612522375551749967 |

Every upper endpoint exceeds the corresponding lower endpoint by exactly $3\cdot10^{-40}$. The records also save exact dyadic endpoints and the positive omitted-tail bounds, below $7\cdot10^{-107}$, $3\cdot10^{-106}$, and $4\cdot10^{-103}$, respectively. The finite Arb/Acb computation is enlarged by the proved infinite tail before outward decimal enclosure and positive interval division. Thus the conclusion's enclosure language is supported by the analytic tail proof and outward ball arithmetic, rather than by agreement of precisions or cutoffs.

The complete `toda_theta_tail_rational_receipt_review_20260913.json` was read. It checks both saved records with exact rational arithmetic: all eight decimal enclosures and widths, positive mass, dyadic denominators, ratio interval containment of endpoint interval division, and mode-pair identity. Its own stated scope is saved-endpoint arithmetic. It is not promoted here to an independent Arb evaluation or a separate proof of the analytic tail. The full theta independent proof review has accepted the source at its pinned hash; that independent proof and the author's execution evidence remain separately attributable.

The certificate script SHA256 is `db01839848cb6b67d24f5702789f6b9eb27d523a80c40cc58b25b9634ce101c5`; the normal and optimized result pins are `2d5ebb1a40f1f33cff8d227ae57d68fb3ae0a18d084b74973d08fcf2c1cc32cc` and `3d5f835f6f4f39f130ade91077e9ec9c1f8a808782faed5d8491598c41961bb7`; the replay receipt pin is `1c74d398871ff0bde77002f15890e3d03da3dc1099db3dd7238cc06fe61ad1cb`. The 21-file component manifest pins the proof, certificate, records and visual receipt. The four seed intervals certify these three analytic values and one ratio; neither their statements nor R36 infer a finite-packet determinant bound or growth estimate from them.

## 8. R37: exact calculated comparison of the two gaps

TC1 fixes

\[
d\nu(u)=\frac{\mu}{\sqrt{2\pi}\sigma}e^{-u^2/(2\sigma^2)}du,
\quad \mu,\sigma>0,\quad c=1/2,\quad x=S-c,\quad\chi=x^2-\sigma^2.
\]

The coefficients of this fixture are declared; no arithmetic zero identity is inferred from them. In quotient coordinates $(1,x)$ and the original coordinates $(1,S)$, the exact coefficient map is

\[
L_{\rm coord}=\begin{pmatrix}1&-c\\0&1\end{pmatrix},\quad
A_x=\begin{pmatrix}c&\sigma^2\\1&c\end{pmatrix},\quad
A_SL_{\rm coord}=L_{\rm coord}A_x.
\]

Here $A_x$ represents multiplication by $S$; multiplication by $x$ is $A_x-cI$. The determinant-one coordinate map gives $G_{N,x}=L_{\rm coord}^*G_{N,S}L_{\rm coord}$, so it preserves the exact determinant while retaining the full matrices and pairing.

Gaussian integration by parts gives the original moments $m_{2j}=\mu(2j-1)!!\sigma^{2j}$ and odd moments zero. The first four source polynomials and squared norms are

\[
(p_0,p_1,p_2,p_3)=(1,x,x^2+\sigma^2,x^3+3\sigma^2x),
\quad(\omega_0,\omega_1,\omega_2,\omega_3)
=(\mu,\mu\sigma^2,2\mu\sigma^4,6\mu\sigma^6).
\]

Their evaluations retain $p_1(c+iu)=iu$, $p_2(c+iu)=-(u^2-\sigma^2)$, $p_3(c+iu)=-i(u^3-3\sigma^2u)$. Reduction by $x^2=\sigma^2$ gives $b_0=(1,0)^{\mathsf T}$, $b_1=(0,1)^{\mathsf T}$, $b_2=(2\sigma^2,0)^{\mathsf T}$, $b_3=(0,4\sigma^2)^{\mathsf T}$. The exact kernel sum and inversion then give

\[
G_{1,x}=\operatorname{diag}(\mu,\mu\sigma^2),\quad
G_{2,x}=\operatorname{diag}(\mu/3,\mu\sigma^2),\quad
G_{3,x}=\operatorname{diag}(\mu/3,3\mu\sigma^2/11).
\]

Their determinants prove the first R37 vector with its full mass $\mu^2$. The relation on the actual vertical line is $-u^2-\sigma^2$, and the original relation norms are $\nu_0=6\mu\sigma^4$, $\nu_1=22\mu\sigma^6$. Dividing the source determinants $\prod_{j<N+1}\omega_j$ by $1,\nu_0,\nu_0\nu_1$ reproduces the same three volumes, including the literal first-degree empty relation determinant.

The weighted adjoint calculation gives

\[
\mathcal H_1=\begin{pmatrix}0&2\sigma^2\\2&0\end{pmatrix},\quad
\mathcal H_2=\begin{pmatrix}0&4\sigma^2\\4/3&0\end{pmatrix},\quad
\epsilon_1^2=4\sigma^2,\quad \epsilon_2^2=16\sigma^2/3.
\]

The eigenvalues of $A_x$ are $c+\sigma,c-\sigma$, so $L_{\rm spec}=2\sigma$. Reflection $u\mapsto-u$ supplies an exact diagonal congruence between the original source and relation moment Grams at $\theta$ and $-\theta$; the original $S=c+iu$ coordinate map has determinant of modulus one. Thus both determinant sequences are even, $\partial_\theta\log V_N|_0=0$, and $\operatorname{Tr}((A_x-cI)/i)=0$, proving the phase is zero at zero tilt.

The actual volume ratios are $\delta_2=1/3$, $\delta_3=3/11$, $\mathcal R_2=V_1/V_3=11$, and $\alpha_3=3\sigma^2$. Consequently

\[
\alpha_3(1-\delta_2)(\delta_3^{-1}-1)=16\sigma^2/3,
\quad \alpha_3(\mathcal R_2-1)^2/(4\mathcal R_2)=75\sigma^2/11.
\]

For $s=\log(11)/2$ and $t=(\log(11/3)-\log3)/2$, $e^t=\sqrt{11}/3$ and $\cosh s=6/\sqrt{11}$. Therefore the exact imbalance square is

\[
3\sigma^2(\sqrt{11}/3-6/\sqrt{11})^2
=49\sigma^2/33
=75\sigma^2/11-16\sigma^2/3.
\]

This proves the first gap in R37 with its exact source map.

For $v_+=(\sigma,1)^{\mathsf T}$, $v_-=(-\sigma,1)^{\mathsf T}$, retain $G=G_{2,x}$. The exact orthogonal and spectral projectors are

\[
P=\begin{pmatrix}1/4&3\sigma/4\\1/(4\sigma)&3/4\end{pmatrix},\quad
Q=\begin{pmatrix}1/2&\sigma/2\\1/(2\sigma)&1/2\end{pmatrix}.
\]

They have common image $\mathbb Cv_+$, with kernels $\mathbb C(-3\sigma,1)^{\mathsf T}$ and $\mathbb Cv_-$, respectively. The first is the exact $G$-orthogonal complement; direct products prove both projection identities. For $X=Q-P$, direct multiplication using the full $G$-adjoint gives

\[
X^\sharp X=\frac13(I-P),\qquad XX^\sharp=\frac13P,
\quad\operatorname{Tr}(X^\sharp X)=1/3.
\]

Transporting all three matrices by $L_{\rm coord}$ and $G$ by its inverse congruence preserves that trace, as adjacent inverse matrices cancel. Therefore

\[
\epsilon_2^2-L_{\rm spec}^2
=16\sigma^2/3-4\sigma^2
=4\sigma^2/3
=L_{\rm spec}^2\|Q-P\|_{\mathrm{HS},G_2}^2.
\]

This proves the second gap in R37. It retains the exact projector map in addition to the first gap's exact volume-imbalance map. The independent calibration review was read in full as supplementary evidence; it records its own 161 exact comparisons in two modes and three deliberate single-fault controls. This integration audit relies on the complete written calculations above and does not reattribute those executions to itself.

## 9. Corrections requested and verified in the final conclusion

The first complete read used conclusion SHA256 `483317a2ea6eb9b3b4436e5146303cd99b149f381207fcf940b1beb5a1b76f9a`. It exposed one exact terminology error and several places where locally explicit domains would make the appended section self-contained. The root installed the following corrections, and the entire amended section was then read at SHA256 `b0aaab31ed11d56650919d9abfc12a6e74c431263912a9e713d845c93f8808c2`:

1. “Full norm factor” after R33 became “full squared-norm factor,” matching the proved endpoint map $\|\mathcal HP\|^2=(\det K_{q-1}/\omega_q)\|P\|^2$.
2. The R33–R34 preamble now states the actual packet, full orders, $k,q,N$ and real-tilt domains, with the first degree explicitly separate.
3. The projection $P_N$ in R34 is explicitly the tilted source projection onto $\mathcal P_N$, so its type is clear before the different quotient spectral projection in R35.
4. The absolute-square integral in R36 is explicitly a real-tilt identity, with the holomorphic strip continuation referred to its complete proof.
5. The q=0 zero quotient and empty determinant, and q=1 zero radius with strictly positive later Toda upper expression, are explicitly stated with their proved endpoint meanings.

No sign, measure mass, determinant coefficient, interval endpoint, radius value, projector norm, or four-loss formula required alteration. The corrected conclusion adds no premise replacing unproved arithmetic and makes no RH claim or growing-degree estimate beyond its cited full proofs.

## 10. Final source delta and seal

The final bridge SHA256 is **97652a43445708c0e6d2a959f45aed8a4f2a7f73f9cd4b6cd57e67b8fedb408e**. The final conclusion remains **b0aaab31ed11d56650919d9abfc12a6e74c431263912a9e713d845c93f8808c2**. Both final domain passages in the bridge were read:

- The Mellin integral of the individual seed $\phi_0$ initially has domain $\operatorname{Re}s>-2$, since $\phi_0(x)=-6\pi x^2+O(x^4)$ near zero and has Gaussian decay at infinity. Its displayed gamma expression follows by substitution on that domain; the theta-sum termwise integration remains on $\operatorname{Re}s>1$.
- In the join, $C_-\ne0$: otherwise $C_+=C$ and the trace-zero relative operator would give $L=\operatorname{Tr}\mathcal H_N=0$, contrary to the explicit $L>0$. Together with $C_+\ne0$, the original Hom space has a nonempty unit sphere, validating the stated smallest singular value argument.

A byte-preserving reversal of exactly those two inserted passages, with the existing LF newlines retained, has SHA256 9d38489ac9e7e2f529266403ace0f69641e4da6ef7a8cf46f64179ab572c1c71. This independently proves the final source differs from the previously fully read source by precisely the two reviewed domain changes.

**Approved: true** for R33–R37 and their full surrounding appended prose at the stated conclusion pin, against the final TVB pin, the unchanged TI and TC pins, and the original parent join pin. Every integration correction identified by this audit is installed and verified. The report itself retains the full deriving evidence, exact source identities, numerical evidence scopes and endpoint cases. This acceptance is mathematical source integration only; the final cumulative PDF receives a separate visual review after its appendix conversion repair.
