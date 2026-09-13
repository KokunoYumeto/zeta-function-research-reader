# Sum-generated arithmetic cohomology, scalar control, and exact conormal depth

Owner-directed continuation of the split-zero programme — 12 September 2026.

**Status.** Written deductions for mathematical review. This note uses the original theta source and its stated finite-packet realization from the preceding work. It does not claim a new Lean certificate, a global comparison-kernel theorem, or a uniform arithmetic purity estimate. The new constructions are (i) an explicitly injected sum-generated arithmetic submodule containing every amplified spectral value, (ii) its scalar convolution norm and rank-two control formula, (iii) raw-moment formulas for the complete differentiated polynomial image, and (iv) the exact contraction of every original conormal thickening to that sum coordinate. The full relative quotient, its action, and its trace are retained.

## 1. Source intake and fixed objects

The two new transcript files were searched for changes to the arithmetic/control and formalization interfaces. They preserve the earlier full-jet kernel/layer calculations and the formalized internal quotient; they do not supply a later analytic proof of the remaining estimate. The previous `Tau_Sum_Connection_Control` archive was opened directly, its LaTeX and mathematical note were read, and all 48 entries of its supplied manifest verified. Its scalar contraction and matrix connection are inputs [S1], not attributed to the present continuation. The previous transcript's checked algebraic interfaces remain within their reported scope [S2–S4].

The original base is still $\mathfrak b_\tau$. Retain

$$G(R)=\{\tau\}\sqcup\{r^\bullet:r\in R\},\qquad e_R=0_R^\bullet,$$
$$\begin{array}{ccc}
G(\mathbb Z)&\xrightarrow{G(j)}&G(\mathbb C)\\
p_{\mathbb Z}\downarrow&&\downarrow p_{\mathbb C}\\
\mathbb Z&\xrightarrow{j}&\mathbb C .
\end{array}\tag{1.1}$$

The target of $p_{\mathbb Z}$ is infinite. A ring homomorphism is lifted through $G$. A complex-linear map $T:V\to W$ has instead the explicitly defined $G(\mathbb C)$-linear lift $T^\tau(v^\bullet)=(Tv)^\bullet$, $T^\tau(\tau)=\tau$. In a support diagram the formula is $(\lambda,v)\mapsto(\varphi(\lambda),T_\lambda v)$, with its stated support map $\varphi$. These formulas commute with the respective amplitude observations.

Use exactly

$$V=\{\phi\in\mathcal S(\mathbb R):\phi\text{ even},\ \phi(0)=0,\ \int_{\mathbb R}\phi=0\},$$
$$\mathscr B=\{F\in C^\infty(\mathbb R_{>0}):\sup_{x>0}x^b|D^jF(x)|<\infty\ (b\in\mathbb Z,j\ge0)\},\quad D=-x\partial_x,$$
$$C_+=[V\xrightarrow{\Theta}\mathscr B],\quad Q=\mathscr B/\Theta V,\quad
\Theta\phi(x)=\sum_{n\ne0}\phi(nx),$$
$$\phi_*=(4\pi^2x^4-6\pi x^2)e^{-\pi x^2},\quad
 g(s)=2\xi(s),\quad \mathcal M\Theta\phi=gH_\phi,\quad H_{\phi_*}=1.\tag{1.2}$$

Let $h(s)=\prod_{\rho\in Z}(s-\rho)^{m_\rho}$ be a **nonempty** finite packet of actual zeros of $g$, with their full orders. Assume it is stable under $\rho\mapsto1-\bar\rho$. Put

$$d=\deg h,\qquad v_h=g/h,\qquad E_h=\mathbb C[s]/(h),\qquad
\upsilon_h=j_h(v_h)\in E_h^\times.\tag{1.3}$$

The preceding source provides the actual test function $F_h$ and map

$$\mathcal MF_h=v_h,\quad h(D)F_h=\Theta\phi_*,\qquad
\mathcal T_h(P)=P(D)F_h,$$
$$\mathcal T_h(hP)=\Theta(P(D)\phi_*),\qquad
J_h\mathcal T_h(P)=\upsilon_h[P]_h,\qquad
q\mathcal T_h(P)=\sigma_h(\upsilon_h[P]_h).\tag{1.4}$$

For $k\ge2$, define

$$\mathcal P_k=\mathbb C[s_1,\ldots,s_k],\quad I_k=(h(s_1),\ldots,h(s_k)),\quad
B_k=\mathcal P_k/I_k=E_h^{\otimes k},$$
$$S=s_1+\cdots+s_k,\qquad A_k=M_S,\qquad U_k=\upsilon_h^{\otimes k}\in B_k^\times.\tag{1.5}$$

The ordinary invariant submodule is $B_k^{\mathrm{sym}}=B_k^{S_k}$. Its cochain realization is the existing signed chain projector $\frac1{k!}\sum_\pi\operatorname{sgn}(\pi)T_\pi$: in top degree the Koszul sign in $T_\pi$ cancels the displayed sign. The complementary cochain summand and both traces remain in the programme. No change to that projector is made here.

## 2. The sum-generated submodule and its exact spectrum

Index the distinct roots by $\rho_1,\ldots,\rho_a$, with orders $m_1,\ldots,m_a$. For an occupation vector $\mathbf n=(n_1,\ldots,n_a)$ with $\sum n_i=k$, set

$$\lambda_{\mathbf n}=\sum_i n_i\rho_i,\qquad
L_{\mathbf n}=1+\sum_i n_i(m_i-1).\tag{2.1}$$

Let $\Lambda_k$ be the set of distinct values of $\lambda_{\mathbf n}$, and put

$$\ell_\lambda=\max_{\mathbf n:\lambda_{\mathbf n}=\lambda}L_{\mathbf n},\qquad
\boxed{\chi_{h,k}(S)=\prod_{\lambda\in\Lambda_k}(S-\lambda)^{\ell_\lambda}.}\tag{2.2}$$

Equal sums are grouped by their exact equality; no assumption of linear independence or of absent collisions is used. The distinct occupation idempotents stay in $B_k^{\mathrm{sym}}$ even when their sums agree.

**Theorem 2.1.** The polynomial (2.2) is the minimal polynomial of $A_k$ both on $B_k$ and on $B_k^{\mathrm{sym}}$. There are an injective unital algebra map and a separate injective module map

$$\alpha_{h,k}:C_{h,k}:=\mathbb C[S]/(\chi_{h,k})\hookrightarrow B_k^{\mathrm{sym}},\quad [P]\mapsto P(A_k)1,$$
$$\boxed{\eta_{h,k}=M_{U_k}\alpha_{h,k}:C_{h,k}\hookrightarrow B_k^{\mathrm{sym}},\quad
[P]\mapsto U_kP(A_k)1.}\tag{2.3}$$

The map $M_{U_k}$ is an invertible $B_k^{\mathrm{sym}}$-module map on its carrier. It is not asserted to be a unital algebra homomorphism; its inverse is $M_{U_k^{-1}}$. The full jet unit is retained by this pair of maps rather than assigned the value one.

**Proof.** At an ordered root tuple the local factor is

$$L_{\boldsymbol\rho}=\mathbb C[z_1,\ldots,z_k]/(z_1^{m_{i_1}},\ldots,z_k^{m_{i_k}}),\qquad
A_k=\lambda I+N,\quad N=M_{z_1+\cdots+z_k}.$$

Every monomial of degree greater than $\sum_j(m_{i_j}-1)$ vanishes. In precisely that degree, $N^D1$ contains the nonzero monomial $\prod z_j^{m_{i_j}-1}$ with coefficient $D!/\prod(m_{i_j}-1)!$. Thus its nilpotence index is $D+1$. The minimal polynomial on the product takes the maximum index over factors at the same eigenvalue, which is (2.2). For the invariant algebra, the vector $1$ is invariant and its annihilator under $\mathbb C[S]$ is already the same polynomial; indeed $P(A_k)1=0$ is equivalent to the algebra element $P(S)$ being zero. Thus restriction to invariants does not reduce this minimal polynomial. Multiplication by the actual unit $U_k$ has zero kernel and commutes with $A_k$. This proves all assertions.

In particular, for every $\rho\in Z$, the value $k\rho$ occurs in $\Lambda_k$. The cyclic module has a nonzero eigenvector at every $\lambda\in\Lambda_k$: take the local class $(S-\lambda)^{\ell_\lambda-1}$ in its Chinese-remainder factor, and zero in its other factors. Its image under $\eta_{h,k}$ is still nonzero and has eigenvalue $\lambda$.

This retains every exponent required for tensor amplification. It does not claim that a chosen repeated pure tensor is literally the same vector as this cyclic eigenvector when different occupations have the same sum. The original repeated-local-factor projection is the explicit map

$$C_{h,k}\xrightarrow{\eta_{h,k}}B_k^{\mathrm{sym}}
\longrightarrow L_{(\rho,\ldots,\rho)};\tag{2.4}$$

its complete nilpotent image is generated by the local unit times $1,N,\ldots,N^{k(m_\rho-1)}$. A cyclic eigenvector supported at a collided sum can have zero projection to a shorter local block. The spectral value is nevertheless present by the proved injection (2.3).

### The remainder of the arithmetic module remains as a quotient

Let

$$T_{h,k}=B_k^{\mathrm{sym}}/\eta_{h,k}C_{h,k}.$$

Then

$$\boxed{0\to C_{h,k}\xrightarrow{\eta_{h,k}}B_k^{\mathrm{sym}}\to T_{h,k}\to0}\tag{2.5}$$

is an exact sequence of $\mathbb C[S]$-modules. This is a module quotient, not a new algebra quotient of $B_k$. Its split lift is the original $G(\mathbb C)$-linear internal quotient. An element of the retained submodule maps to the supported zero; $\tau$ remains $\tau$.

The sequence also has a constructed $\mathbb C[S]$-linear retraction. On the generalized $\lambda$-part let $N_\lambda=A_k-\lambda I$, $w_\lambda=e_\lambda(A_k)U_k1$, and $\ell=\ell_\lambda$. Choose the fixed-order root tuple attaining $\ell$ and let $\vartheta_\lambda$ extract one of the top monomial coefficients of $N_\lambda^{\ell-1}w_\lambda$ there. That coefficient is its nonzero local arithmetic unit times the corresponding multinomial coefficient. In particular

$$\vartheta_\lambda(N_\lambda^{\ell-1}w_\lambda)\ne0.$$

Define

$$\pi^0_\lambda(v)=\sum_{j=0}^{\ell-1}
\vartheta_\lambda(N_\lambda^{\ell-1-j}v)X^j\pmod{X^\ell},\qquad
p_\lambda(X)=\pi^0_\lambda(w_\lambda).$$

Its constant term is nonzero, so $p_\lambda$ has a unique multiplicative inverse modulo $X^\ell$. The actual retraction is

$$\boxed{\pi_\lambda(v)=p_\lambda(X)^{-1}\pi^0_\lambda(v).}\tag{2.5a}$$

Indeed $\pi^0_\lambda(N_\lambda v)=X\pi^0_\lambda(v)$, and $\pi_\lambda(w_\lambda)=1$. Combining these maps with the CRT idempotents gives $\pi:B_k^{\mathrm{sym}}\to C_{h,k}$ with $\pi\eta_{h,k}=1$. Thus the inverse pair is

$$C_{h,k}\oplus\ker\pi\longrightarrow B_k^{\mathrm{sym}},\quad(c,t)\mapsto\eta_{h,k}c+t,$$
$$v\longmapsto(\pi v,v-\eta_{h,k}\pi v).\tag{2.5b}$$

The quotient $T_{h,k}$ is linked to $\ker\pi$ by $[v]\mapsto v-\eta\pi v$, with inverse given by inclusion followed by the quotient. This retains every remaining nilpotent block; at each sum precisely one maximal-length block is assigned to the cyclic summand. The choice of top coefficient is recorded. This splitting is not asserted orthogonal: an arithmetic Gram $H$ pulls back to the full block matrix containing $\eta^*H\eta$, $\eta^*H|_{\ker\pi}$, and its adjoint cross term, not just their diagonal blocks.

On a fixed sum $\lambda$, the dimension of the symmetric generalized eigenspace is

$$a_\lambda=\sum_{\mathbf n:\lambda_{\mathbf n}=\lambda}
\prod_i\binom{n_i+m_i-1}{m_i-1}.\tag{2.6}$$

Thus $T_{h,k}$ has dimension $a_\lambda-\ell_\lambda$ there. For every entire $f$, trace additivity in (2.5) proves

$$\operatorname{Tr}(f(A_k)|B_k^{\mathrm{sym}})=
\sum_\lambda \ell_\lambda f(\lambda)
+\sum_\lambda(a_\lambda-\ell_\lambda)f(\lambda).\tag{2.7}$$

The first term is the cyclic trace; the second is the retained quotient trace. All terms get the same cohomological factor $(-1)^k$ in top-degree supertrace. This calculation is valid with nilpotents; it does not replace their modules by their residue values.

For example, the algebraic fixture with simple roots $1/4,1/2,3/4$ and $k=2$ has a six-dimensional symmetric module but a five-dimensional cyclic module. The two occupations with sum $1$ give a one-dimensional quotient at that sum. The fixture with one root of order three and $k=2$ has symmetric dimension six, cyclic length five, and quotient length one at $2\rho$. These are fixtures of the formulas, not assertions of zeta zeros at those locations or multiplicities.

## 3. An original source realization whose norm is the scalar sum density

Define the linear map

$$\boxed{\mathcal V_{h,k}:\mathbb C[S]\to\mathscr B^{\otimes k},\qquad
P\mapsto P(D_1+\cdots+D_k)(F_h^{\otimes k}).}\tag{3.1}$$

Its Mellin transform is

$$\mathcal M^{(k)}\mathcal V_{h,k}(P)
=\left(\prod_i v_h(s_i)\right)P(s_1+\cdots+s_k).$$

It is injective: if this analytic function vanishes, it vanishes on an open set where all $v_h$ are nonzero, forcing the polynomial $P$ to vanish identically. Its actual arithmetic map is

$$\boxed{J^{(k)}\mathcal V_{h,k}=\eta_{h,k}\pi_\chi,\qquad
q^{(k)}\mathcal V_{h,k}=\sigma_h^{\otimes k}\eta_{h,k}\pi_\chi,}\tag{3.2}$$

where $\pi_\chi(P)=[P]_\chi$. Thus its arithmetic kernel is exactly $(\chi)$ and not a selected subset of the original relations.

Let $q_k=\deg\chi_{h,k}$ and $N\ge q_k-1$. At finite source degree,

$$\boxed{0\to\mathbb C[S]_{\le N-q_k}\xrightarrow{\times\chi}
\mathbb C[S]_{\le N}\xrightarrow{\pi_\chi}C_{h,k}\to0.}\tag{3.3}$$

A negative bound means the zero space. Define the actual boundary space

$$\mathcal D_{h,k,N}=\mathcal V_{h,k}(\chi\,\mathbb C[S]_{\le N-q_k}).$$

Because $\chi(s_1+\cdots+s_k)\in I_k$, fixed-order monic division gives

$$\chi(S)Q(S)=\sum_i h(s_i)Q_i(\mathbf s).\tag{3.4}$$

Each term is an original top cochain boundary: replace $F_h$ in factor $i$ by $\phi_*$, apply the polynomial $Q_i(D_1,\ldots,D_k)$, and give the primitive $(-1)^{i-1}$. The tensor differential gives the second $(-1)^{i-1}$. Their product is $+1$. This supplies the original primitive rather than defining a new vanishing relation by fiat.

The split quotient of (3.3) has equality criterion $P\sim P'$ precisely when $P-P'\in\chi\mathbb C[S]_{\le N-q_k}$. A relation maps to the supported zero at label $\lambda_N$. Degree transport retains the preceding label and its killed-representative kernel.

### The exact norm

Retain from [S1]

$$a_h(t)=\frac{v_h(1/2+it)}{\sqrt{2\pi}},\quad
w_h(t)=|a_h(t)|^2,\quad \mu_h=\int w_h,\quad m_{h,k}=w_h^{*k}.$$

In centered sum coordinates $u=\sum t_i$, $y_i=t_i-u/k$, the amplitude is $\Psi_{h,k}(u,\mathbf y)=\prod_i a_h(u/k+y_i)$. Its relative integral is $m_{h,k}(u)$. Therefore

$$\boxed{\|\mathcal V_{h,k}P\|_{L^2(d^kx)}^2
=\int_{\mathbb R}|P(k/2+iu)|^2m_{h,k}(u)\,du.}\tag{3.5}$$

This is the restriction of the preceding full matrix-weight realization to the **specific source family** $P(S)$, through (3.1) and (3.2). It does not identify every relative coefficient with the constant relative coefficient.

The full relative module remains in (2.5). For comparison with the previous least-norm representative, at the same ambient degree $N$ the maps obey

$$\mathcal V_{h,k}(\mathbb C[S]_{\le N})\hookrightarrow
\mathcal T_h^{(k)}(\mathcal P_{k,N}),\qquad
\mathcal D_{h,k,N}\hookrightarrow\mathcal B_{k,N}.$$

Let $R^{\mathrm{full}}_{k,N}$ be the old joint minimum, and $\mathcal R_N$ the cyclic minimum constructed next. Their exact relationship is

$$\Delta_N=\mathcal R_N-R^{\mathrm{full}}_{k,N}\eta_{h,k}\in
\operatorname{Hom}(C_{h,k},\mathcal B_{k,N}),$$
$$\boxed{\mathcal G_N=\eta_{h,k}^*G^{\mathrm{full}}_{k,N}\eta_{h,k}+\Delta_N^*\Delta_N.}\tag{3.6}$$

Both maps represent the same full jets; their difference is in the original relation ideal, and the full minimum is orthogonal to it. This proves (3.6). The corresponding control difference is

$$\mathcal W_N-\eta_{h,k}^*W^{\mathrm{full}}_{k,N}\eta_{h,k}
=A_\chi^*\Delta_N^*\Delta_N+\Delta_N^*\Delta_NA_\chi-k\Delta_N^*\Delta_N.\tag{3.7}$$

This explicitly retains why the Gram inequality does not itself order the control forms.

The scalar source must reach degree $q_k-1$ to realize all cyclic jets. This can exceed $k(d-1)$. The reduction in relative rank has a degree cost which remains in every estimate.

## 4. Canonical scalar representatives and rank-two arithmetic control

Apply Gram–Schmidt by subtracting lower-degree projections from $1,S,S^2,\ldots$ for the exact measure in (3.5). Let $p_j^{[h,k]}$ be the resulting polynomial with leading coefficient one, and retain

$$\omega_j^{[h,k]}=\int |p_j^{[h,k]}(k/2+iu)|^2m_{h,k}(u)\,du>0.\tag{4.1}$$

No polynomial is divided by its norm. In particular $\omega_0^{[h,k]}=\mu_h^k$. For this section suppress the indices $h,k$ and write

$$b_j=[p_j]_\chi\in C_{h,k},\qquad
\mathcal K_N=\sum_{j=0}^N\frac{b_jb_j^*}{\omega_j},\qquad
\mathcal G_N=\mathcal K_N^{-1}.\tag{4.2}$$

The coordinates on $C_{h,k}$ are the fixed remainder basis $1,S,\ldots,S^{q_k-1}$. Its inclusion into the original full jets is $\eta_{h,k}$, carrying $U_k$; $b_j$ is not an assertion that $U_k=1$.

The unique least-norm representative modulo the specified $\mathcal D_{h,k,N}$ is

$$\boxed{\mathcal R_Nu=\mathcal V_{h,k}\left(
\sum_{j=0}^Np_j\frac{b_j^*\mathcal G_Nu}{\omega_j}\right).}\tag{4.3}$$

Its identities are

$$J^{(k)}\mathcal R_N=\eta_{h,k},\quad
q^{(k)}\mathcal R_N=\sigma_h^{\otimes k}\eta_{h,k},\quad
\mathcal R_N^*\mathcal R_N=\mathcal G_N.\tag{4.4}$$

**Proof.** The coefficient map in (4.3) is the weighted adjoint of the full remainder map followed by $(JJ^*)^{-1}$ in the displayed orthogonal coordinates. Multiplication verifies its right-inverse identity. If $Z$ is another polynomial with the same remainder, their difference lies in the exact kernel (3.3); the cross term with (4.3) is zero by the adjoint formula. The norm is therefore the displayed minimum plus the squared norm of that difference. This proves uniqueness and all equations, before any completion of the arithmetic quotient.

Let $A_\chi=M_S$ on $C_{h,k}$. Multiplication by $S$ has adjoint multiplication by $k-S$ on the integration line. Orthogonality and leading coefficients give

$$Sp_j=p_{j+1}+\beta_jp_j-\frac{\omega_j}{\omega_{j-1}}p_{j-1},\qquad
\Re\beta_j=k/2,\tag{4.5}$$

with the last term absent at $j=0$. This is the ordinary orthogonal-polynomial recurrence in the retained complex coordinate; its general framework is recorded in DLMF §18.2 [E1].

**Theorem 4.1 (two-row control on a spectrum-complete submodule).**

$$\boxed{\mathcal Z_N:=A_\chi\mathcal K_N+\mathcal K_NA_\chi^*-k\mathcal K_N
=\frac{b_{N+1}b_N^*+b_Nb_{N+1}^*}{\omega_N}.}\tag{4.6}$$

Consequently

$$\boxed{\mathcal W_N:=A_\chi^*\mathcal G_N+\mathcal G_NA_\chi-k\mathcal G_N
=\mathcal G_N\mathcal Z_N\mathcal G_N,\qquad \operatorname{rank}\mathcal W_N\le2.}\tag{4.7}$$

**Proof.** Substitute (4.5) into the finite sum (4.2). Each adjacent pair internal to $0,\ldots,N$ cancels because the negative lower coefficient is exactly $-\omega_j/\omega_{j-1}$. Each diagonal pair is $k b_jb_j^*/\omega_j$. The only remaining adjacent pair is the one in (4.6). Congruence gives (4.7). This is a Christoffel–Darboux cancellation on the actual cyclic source, not a statement that the full relative module's control has rank two.

### The original next relation is retained

Define

$$\mathfrak b_N=\mathcal V_{h,k}(p_{N+1})-\mathcal R_Nb_{N+1}.$$

Its full jets vanish and its polynomial degree is $N+1$. It gives the explicit isomorphism

$$\boxed{\mathbb C\xrightarrow{c\mapsto c\mathfrak b_N}
\mathcal D_{h,k,N+1}\cap\mathcal D_{h,k,N}^{\perp}
\xrightarrow{z\mapsto[z]}
\mathcal D_{h,k,N+1}/\mathcal D_{h,k,N}.}\tag{4.8}$$

The leading term proves injectivity; the one-dimensional degree increment proves surjectivity. Its norm and pairing are

$$\|\mathfrak b_N\|^2=\omega_{N+1}+b_{N+1}^*\mathcal G_Nb_{N+1},\qquad
\mathfrak b_N^*\mathcal R_N=-b_{N+1}^*\mathcal G_N.\tag{4.9}$$

The class is nonzero at degree $N$ and becomes the receiving supported zero at degree $N+1$. Its theta primitive is obtained from the original division (3.4). The scalar support itself is not adjoined again.

The exact update is

$$\mathcal K_{N+1}=\mathcal K_N+b_{N+1}b_{N+1}^*/\omega_{N+1},$$
$$\mathcal G_{N+1}=\mathcal G_N-
\frac{\mathcal G_Nb_{N+1}b_{N+1}^*\mathcal G_N}
{\omega_{N+1}+b_{N+1}^*\mathcal G_Nb_{N+1}}.\tag{4.10}$$

### Same-metric reflection and exact excess

Let $P^{\dagger_k}(S)=\overline{P(k-\bar S)}$. The polynomial $\chi$ obeys $\chi^{\dagger_k}=(-1)^{q_k}\chi$. The induced antilinear involution on the **weighted** cyclic module is

$$j_C[P]=(-1)^{kd}[P^{\dagger_k}].\tag{4.11}$$

This sign is forced by $U_k^\dagger=(-1)^{kd}U_k$ in the original embedding. It intertwines with the actual function reflection and preserves the source degree and norm. Hence the unique minimum obeys reflection on the same $\mathcal G_N$.

Uniqueness of the monic orthogonal polynomial gives $p_j^{\dagger_k}=(-1)^jp_j$. In particular

$$c_N=b_N^*\mathcal G_Nb_{N+1}\quad\text{satisfies}\quad \bar c_N=-c_N.$$

Write $a_N=b_N^*\mathcal G_Nb_N$ and $d_N=b_{N+1}^*\mathcal G_Nb_{N+1}$. The nonzero generalized control eigenvalues are the eigenvalues of

$$\frac1{\omega_N}\begin{pmatrix}\bar c_N&d_N\\a_N&c_N\end{pmatrix}.$$

Therefore the exact least two-sided excess is

$$\boxed{\epsilon_{h,k,N}^{\mathrm{cyc}}=
\frac{\sqrt{a_Nd_N-|c_N|^2}}{\omega_N}.}\tag{4.12}$$

The determinant is nonnegative by the Gram inequality. Zero and rank-one degeneracies are covered by the same formula; in the reflection-stable case a nonzero rank-one signed defect cannot occur. No phase is dropped.

For the actual eigenvector at $k\rho$ constructed in Section 2,

$$\boxed{k|2\Re\rho-1|\le\epsilon_{h,k,N}^{\mathrm{cyc}}.}\tag{4.13}$$

This is a proved diagnostic of this explicit family. A sublinear bound on the calculated right side as $k$ grows is still to be established from the arithmetic input. The rank-two identity is not such a bound by itself.

## 5. Keep packet changes through their actual source seeds

Let $h\mid H$ include complete multiplicities, and let $m=H/h$. Then

$$F_h=m(D)F_H,\qquad
\mathcal V_{h,k}P=\mathcal T_H^{(k)}\left(\prod_i m(s_i)\,P(S)\right).\tag{5.1}$$

The full CRT inclusion on jets is the $\mathbb C[S]$-linear map which inserts zero jets at the added centres. Its old unit maps to the associated idempotent, so it is not described as a unital algebra inclusion into the entire larger packet.

The right side of (5.1) has the fixed seed $a_{hH}(\mathbf s)=\prod_i m(s_i)$. Its source norm is exactly the old norm, since $(g/H)m=g/h$ in every factor. It therefore defines an isometric map of the marked polynomial sources and their internal quotients, with the old cyclic annihilator $\chi_{h,k}$.

This is the correct packet-coherence comparison. The new seed is generally not a polynomial in $S$ alone. For example, if $m(s)=s-1/2$ and $k=2$, then

$$m(s_1)m(s_2)=\frac{(S-1)^2-(s_1-s_2)^2}{4}.\tag{5.2}$$

The relative square and its coefficient are retained. The explicit source-seed map (5.1), followed by the larger packet's full relative source inclusion, replaces any unjustified identification with that larger packet's unmarked constant-seed cyclic submodule. No original packet, supported relation, or canonical scalar norm is changed by this marked comparison.

## 6. The scalar Fisher estimate now acts on this source, and all polynomial derivative moments are calculable

From [S1],

$$\mathcal I_{h,k}+4\int\|n_{h,k}(u)\|^2du
=\frac{\mu_h^{k-1}}k\mathcal I_h,
\qquad \mathcal I_h=4\int|a_h'(t)|^2dt.\tag{6.1}$$

The cyclic source (3.5) uses **that very density** $m_{h,k}$, not another scalar replacement for the full matrix norm. The full derivative still has the specified two components:

$$\boxed{\partial_u\bigl(\Psi_{h,k}P(k/2+iu)\bigr)
=\Psi_{h,k}\left(iP'(k/2+iu)+\frac{m_{h,k}'}{2m_{h,k}}P(k/2+iu)\right)
+n_{h,k}P(k/2+iu).}\tag{6.2}$$

They are pointwise orthogonal. The second component is retained even though the original coefficient polynomial depends only on the sum. Its arithmetic interpretation is the graph map and logarithmic observable from [S1]. The generator remains $A_k$; the derivative corresponds to $i\mathscr L_k$, with $[D^{(k)},\mathscr L_k]=-1$.

### Raw moments give the complete differentiated finite source without multidimensional quadrature

Define the finite moments

$$\mu_j=\int t^j|a_h(t)|^2dt,\qquad
\nu_j=\int t^j|a_h'(t)|^2dt,\qquad
\theta_j=\int t^j\overline{a_h(t)}a_h'(t)dt.$$

Fixed arithmetic phase and integration by parts give

$$\theta_0=0,\qquad \theta_j=-\frac j2\mu_{j-1}\quad(j\ge1).\tag{6.3}$$

Use the **formal** exponential generating series

$$\mathcal M(z)=\sum_{j\ge0}\mu_jz^j/j!,\qquad
\mathcal N(z)=\sum_{j\ge0}\nu_jz^j/j!.$$

No convergence of these series is needed for the finite coefficient identities. Their constant terms remain the actual mass and derivative energy.

Let

$$M_{j,k}=\int u^jm_{h,k}(u)du,\qquad
B_{j,k}=\int u^j\|\partial_u\Psi_{h,k}(u,\cdot)\|^2du.$$

**Theorem 6.1 (all polynomial derivative moments).**

$$\boxed{M_{j,k}=j![z^j]\mathcal M(z)^k,}\tag{6.4}$$
$$\boxed{B_{j,k}=j![z^j]\left[
\frac1k\mathcal N(z)\mathcal M(z)^{k-1}
+\frac{k-1}{4k}z^2\mathcal M(z)^k\right].}\tag{6.5}$$

**Proof.** Expand $u^j=(t_1+\cdots+t_k)^j$ and use Fubini; all integrals are absolutely finite. For (6.5), the diagonal terms of $|k^{-1}\sum_i a_i'\prod_{r\ne i}a_r|^2$ give $k^{-1}\mathcal N\mathcal M^{k-1}$. The distinct-index terms give $(k-1)\Theta(z)^2\mathcal M^{k-2}/k$, where $\Theta(z)=\sum\theta_jz^j/j!=-z\mathcal M(z)/2$ by (6.3). Substitution gives the displayed expression. The second term is not discarded: the cross terms vanish only for the unweighted zeroth moment, not for arbitrary polynomial moments.

In particular,

$$M_{0,k}=\mu_0^k,\quad M_{1,k}=k\mu_1\mu_0^{k-1},$$
$$M_{2,k}=k\mu_2\mu_0^{k-1}+k(k-1)\mu_1^2\mu_0^{k-2},$$
$$B_{0,k}=\frac1k\nu_0\mu_0^{k-1}=\frac{\mu_h^{k-1}}{4k}\mathcal I_h.\tag{6.6}$$

The first orthogonal norm and diagonal coefficient on the sum line are accordingly

$$\omega_0=\mu_0^k,\quad
\beta_0=\frac k2+i\frac{k\mu_1}{\mu_0},\quad
\omega_1=k\mu_0^{k-2}(\mu_0\mu_2-\mu_1^2).\tag{6.7}$$

No symmetry assumption setting $\mu_1=0$ is made.

For any two polynomials $P,Q$, let $c_P(u)=P(k/2+iu)$ and $c_Q(u)=Q(k/2+iu)$. Their complete graph-energy form is

$$\begin{aligned}
\mathfrak D_k(P,Q)={}&\int\overline{c_P}c_Q\,\|\Psi_k'\|^2du
+\int\overline{c_P'}c_Q'\,m_kdu\\
&+\frac12\int\left(\overline{c_P}c_Q'+\overline{c_P'}c_Q\right)m_k'du.
\end{aligned}\tag{6.8}$$

All four terms remain. Equations (6.4)–(6.5) and $\frac12\int u^jm_k'=-jM_{j-1,k}/2$ evaluate every matrix entry on a fixed polynomial degree using only $\mu_j,\nu_j$. This is the complete derivative graph norm from the existing sum-fibre construction, not merely the scalar score norm. It is positive definite on every nonzero polynomial source: a zero derivative would make $\Psi_kP$ constant in $u$ for almost every relative coordinate, while its decay forces that constant and then $P$ to be zero.

For a finite canonical representative, its graph-energy matrix is obtained by applying its actual coefficient matrix from (4.3) on both sides of (6.8). Thus there are now explicit moment matrices for both the original metric and the differentiated representative. No continuous jet functional on arbitrary $L^2$ classes is assumed.

## 7. Exact sum-coordinate conormal depth at every original thickening

The derivative graph still needs the class **before** an original relation is sent to $e$. The required domains can now be computed exactly on the sum line.

For $r\ge1$, retain the original thickened ring

$$B_{k,r}=\mathcal P_k/I_k^r.$$

Define, for an ordered root tuple $\boldsymbol\rho=(\rho_{i_1},\ldots,\rho_{i_k})$,

$$L_{\boldsymbol\rho,r}=1+\sum_{j=1}^k(m_{i_j}-1)+(r-1)\max_jm_{i_j},$$
$$\ell_{\lambda,r}=\max_{\boldsymbol\rho:\sum\rho_{i_j}=\lambda}L_{\boldsymbol\rho,r},\qquad
\boxed{\chi_{h,k,r}(S)=\prod_{\lambda\in\Lambda_k}(S-\lambda)^{\ell_{\lambda,r}}.}\tag{7.1}$$

**Theorem 7.1.** The exact contracted ideal is

$$\boxed{I_k^r\cap\mathbb C[S]=(\chi_{h,k,r}).}\tag{7.2}$$

Consequently there is an injective unital algebra map

$$\boxed{\alpha_r:C_{h,k,r}:=\mathbb C[S]/(\chi_{h,k,r})\hookrightarrow B_{k,r}^{S_k},\quad[P]\mapsto[P(S)].}\tag{7.3}$$

**Proof.** At a root tuple, the units in $h(\rho_i+z_i)=u_i(z_i)z_i^{m_i}$ make the original local ideal equal to $(z_1^{m_1},\ldots,z_k^{m_k})$, with its $r$th power retained. A monomial $z^\alpha$ survives precisely when

$$\sum_i\left\lfloor\frac{\alpha_i}{m_i}\right\rfloor\le r-1.\tag{7.4}$$

The largest surviving total degree is $\sum_i(m_i-1)+(r-1)\max_i m_i$. It is attained by assigning all $r-1$ full blocks to an index of maximal $m_i$, and taking remainders $m_i-1$ in every index. The corresponding term of $(\sum z_i)^D$ has coefficient $D!/\prod\alpha_i!\ne0$. All terms of degree $D+1$ vanish. Thus the exact nilpotence index is (7.1). Take the maximum over collided sums and then the product over different sums. This gives precisely the annihilator of the algebra element $S$, proving (7.2). The same cyclic image is in the invariants because $S$ and $1$ are invariant. No local unit has been discarded: it enters the specified invertible change of generators of the ideal, not an alteration of the physical coordinate $S$.

### Quotient and derivative maps on the same tower

There are commuting quotient squares

$$\begin{array}{ccc}
C_{h,k,r+1}&\xrightarrow{\alpha_{r+1}}&B_{k,r+1}\\
\downarrow&&\downarrow\\
C_{h,k,r}&\xrightarrow{\alpha_r}&B_{k,r}.
\end{array}\tag{7.5}$$

Each quotient is a ring map, hence has the original split lift. Its kernel is retained. On the sum side,

$$0\to \mathbb C[S]/(\chi_{r+1}/\chi_r)
\xrightarrow{\times\chi_r}C_{r+1}\to C_r\to0.\tag{7.6}$$

The first arrow is explicitly a module map. Under $\alpha_{r+1}$ its image lies in $I_k^r/I_k^{r+1}$; this is the actual relation fibre sent to the supported zero by the right vertical quotient.

The exact exponent satisfies $\ell_{\lambda,r+1}\ge\ell_{\lambda,r}+1$. Hence $\chi_r$ divides $\chi_{r+1}'$, and the linear derivative map is well-defined:

$$\boxed{\partial_r:C_{r+1}\to C_r,\quad[P]\mapsto[P'].}\tag{7.7}$$

It commutes with the original relative-sum derivative

$$\delta_r:B_{k,r+1}\to B_{k,r},\quad
[P]\mapsto\left[\frac1k\sum_i\partial_{s_i}P\right],$$
$$\boxed{\delta_r\alpha_{r+1}=\alpha_r\partial_r.}\tag{7.8}$$

The derivatives are coefficient-linear maps and are lifted as such, not called ring homomorphisms. For example,

$$h(s)=(s-\rho)^2,\quad k=2,\quad X=S-2\rho
\quad\Longrightarrow\quad\chi_r=X^{2r+1}.\tag{7.9}$$

The class $X^3$ is nonzero modulo $X^5$, maps to the supported zero modulo $X^3$, and its derivative maps to $3X^2$, which is nonzero there.

This also calculates the relationship to a naive scalar power thickening:

$$\mathbb C[S]/(\chi_1^r)\twoheadrightarrow C_r\hookrightarrow B_{k,r}.\tag{7.10}$$

For the fixture in (7.9) at $r=2$, the first map is $\mathbb C[X]/(X^6)\twoheadrightarrow\mathbb C[X]/(X^5)$, with kernel the retained class of $X^5$. The original joint thickening therefore carries a different sum-coordinate depth, and the precise quotient above gives their relationship. This is a calculation about powers of the original relation ideal; it is not iteration of the scalar zero adjunction.

### The arithmetic Taylor unit remains through differentiation

Let $U_{k,r}$ be the full Taylor class of $\prod v_h(s_i)$ in $B_{k,r}$. It is invertible and compatible under the quotient tower. Define the coefficient-linear inclusion

$$\eta_r=M_{U_{k,r}}\alpha_r.$$

The full equation is

$$\boxed{\delta_r\eta_{r+1}(P)
=U_{k,r}\alpha_r(P')+(\delta_rU_{k,r+1})\alpha_r(P).}\tag{7.11}$$

The second term remains in the relative ring $B_{k,r}$. It is not presumed to be in the cyclic image. Its exact map is $M_{\delta_rU_{k,r+1}}\alpha_r$, and the complementary quotient $B_{k,r}/\eta_rC_r$ records its noncyclic part. This is the algebraic counterpart of the retained normal derivative in (6.2).

At $r=1$, the quotient and derivative thus give two actual maps out of the same lifted thickening. A conormal relation can map to $e$ under the quotient and to a nonzero supported value under the derivative. Differentiating the original theta relation, not the scalar $e$ itself, is what produces that value.

## 8. The conormal derivative reaches both cyclic and full arithmetic traces, with their difference retained

Choose an original division

$$\chi_1(S)=\sum_i h(s_i)B_i(\mathbf s).$$

Applying the actual derivative and then the original quotient yields

$$\boxed{\alpha_1(\chi_1')
=\frac1k\sum_i h'(s_i)[B_i]_{I_k}.}\tag{8.1}$$

The right side is the source's conormal row. For the weighted relation $U\chi_1P$, the term containing $\delta U$ has an undifferentiated $\chi_1$ and vanishes in $B_k$. Therefore

$$\boxed{\delta_1[U\chi_1P]_{I_k^2}
=U_k\alpha_1(\chi_1'P).}\tag{8.2}$$

It has the actual analytic representative

$$J^{(k)}\mathscr L_k\mathcal V_{h,k}(\chi_1P)
=U_k\alpha_1(\chi_1'P),\qquad
\mathscr L_k=\frac1k\sum_i\log x_i.\tag{8.3}$$

Here the left source is an original theta boundary, supplied by (3.4). Its first differentiated arithmetic value is read before it is collapsed to its supported zero.

For $C_1=\mathbb C[S]/(\chi_1)$, the explicitly chosen finite residue pairing is

$$R_\chi(f,P)=\sum_\lambda\operatorname{Res}_{S=\lambda}
\frac{f^{\dagger_k}(S)P(S)}{\chi_1(S)}\,dS.$$

Its Jacobian contraction is

$$\boxed{R_\chi(f,\chi_1'P)
=\sum_\lambda \ell_\lambda\,\overline{f(k-\bar\lambda)}P(\lambda)
=\operatorname{Tr}(M_{f^{\dagger_k}P}|C_1).}\tag{8.4}$$

This is the cyclic trace. The original full symmetric trace has $a_\lambda$ instead of $\ell_\lambda$ and is their sum with the quotient trace (2.7). Equivalently, let $\chi_{\mathrm{full}}(S)=\prod_\lambda(S-\lambda)^{a_\lambda}$. Its difference is the explicit residue functional

$$\boxed{\operatorname{Tr}(f(A_k)|T_{h,k})
=\sum_\lambda\operatorname{Res}_{S=\lambda}f(S)
\left(\frac{\chi_{\mathrm{full}}'}{\chi_{\mathrm{full}}}-
\frac{\chi_1'}{\chi_1}\right)dS.}\tag{8.5}$$

There is a further explicit comparison for the original arithmetic vector pairing. Its pullback through the **weighted** inclusion is

$$\operatorname{Tr}_{B_k^{\mathrm{sym}}}M_{(\eta f)^\dagger\eta P}
=\operatorname{Tr}_{B_k^{\mathrm{sym}}}M_{U_k^\dagger U_k\,\alpha_1(f^{\dagger_k}P)}.\tag{8.6}$$

The factor $U_k^\dagger U_k$ remains. It need not lie in the sum-generated subalgebra. The trace decomposition (2.7) applies to the invariant operator $f(A_k)$; it is not an assertion that this weighted vector pairing is automatically the cyclic residue form (8.4).

Neither polynomial is substituted for the original $g=2\xi$. Their finite trace comparison is (8.5), while $U_{k,r}$ and the map (8.3) retain their arithmetic source. The original product residue/Jacobian trace can still be evaluated on the full module and its retained quotient. No trace contribution is declared absent.

## 9. Checks, counterfactual tests, and the next estimate

The exact checker implements finite polynomial, matrix, and Gaussian-amplitude fixtures. Its tests cover exact thickening dimensions and nilpotence; collision grouping; cyclic injections and trace complements; the non-naive thickening map; the derivative square; supported-zero versus absence; the original conormal row; full unit differentiation; scalar minimum and updates; rank-two control; reflection with a nonzero imaginary cross term; amplified off-line test exponents; raw convolution and complete polynomial derivative moments; and the marked source-seed transition. These are regression checks, not tests asserting that a fixture's roots are zeta zeros.

In particular an off-line reflected polynomial fixture remains off-line under the new construction: its exact eigenline identity is still $2\Re\lambda-k$. The scalar Fisher contraction does not annul this value. This guards against an inference from convolution smoothing alone to purity. The constructive object supplied instead is (4.12): two explicitly computed full-jet rows relative to the exact cyclic interpolation metric, with every scalar moment obtainable from the original one-factor moments by (6.4).

The degree cost $N\ge\deg\chi_{h,k}-1$ and the reciprocal metric in (4.12) are retained as $k$ grows. The derivative matrix (6.8) likewise keeps the polynomially weighted normal contribution. Controlling those quantities on the actual arithmetic inputs, rather than just the constant polynomial, is the remaining quantitative step of this branch.

The connection to the Deligne amplification programme is now a smaller, exactly included cohomological image with every amplified exponent represented; its source norm is the scalar sum-density norm for which (6.1) was proved. The original multi-direction module, its complementary trace, and all powers of its conormal ideal remain as explicit surrounding objects. This is not a transfer of finite-field purity by notation.

No remote repository is modified in this delivery. The user has assigned GitHub integration and Lean work to the parallel session. The authored note, checker, and a bounded handoff are ready for that session without changes to its existing files.

## Source record and references

- **[S1]** Owner programme, `Tau_Sum_Connection_Control/NOTE.tex` and `RESEARCH_NOTE.md`, archive `Tau_Sum_Connection_Control_2026-09-12.zip`. Selected analytic source, scalar information identity, full matrix connection, original first and higher conormal derivative. Exact hashes and source-manifest verification are in `checks/source_manifest.json` and `SOURCE_READING.json`.
- **[S2]** User upload `Untitled 1765(1).md`: retained progression from globalization to coherent interpolation, highest relation layer and spectral-sum descent. Read as a research transcript, not as an independent certificate for every embedded claim.
- **[S3]** User upload `Untitled 1766(1).md`: formalization progression, retained bounded scopes, and the kernel-layer integration. No new Lean run is claimed in this note.
- **[S4]** `SplitZero_Derived_Mathematics_2026-09-12(1).md` and retained source-derived interfaces: internal quotient, transported-class kernel and tensor base-change. Used within their stated hypotheses.
- **[E1]** NIST, *Digital Library of Mathematical Functions*, §18.2, particularly recurrence, Christoffel–Darboux, and moments. https://dlmf.nist.gov/18.2 . General framework only; the arithmetic source maps and cyclic calculation are proved here.
- **[E2]** The Stacks Project, Tag 00S0, *The naive cotangent complex*. https://stacks.math.columbia.edu/tag/00S0 . Background for the conormal map; (7.1)–(7.11) compute the exact present ideals and coordinate derivative.
- **[E3]** O. Johnson and A. Barron, *Fisher Information inequalities and the Central Limit Theorem*, arXiv:math/0111020. https://arxiv.org/abs/math/0111020 . General convolution-projection mechanism; the mass-retaining arithmetic identity is the earlier source [S1].
- **[D]** P. Deligne, *La conjecture de Weil. II*, supplied TeX/source excerpts in the programme, especially §3.2.13 and §3.3.4–3.3.6. This turn uses the previously read amplification target; it does not claim to have reread or independently verified the whole paper.
