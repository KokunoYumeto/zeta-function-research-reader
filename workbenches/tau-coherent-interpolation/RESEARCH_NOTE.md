# Coherent arithmetic interpolation and joint tensor boundary control

Owner-directed continuation, 12 September 2026. Written mathematical arguments for review; the new analytic and matrix results in this note have not been Lean-checked.

## 0. Accepted inputs and the change in the continuation

The new formalization receipt reports—and the repository metadata and workflow step summaries confirm—a successful check at `5d2772ea0a16d177ac3e01ff70394b90ba95a232` in PR #12. That certificate covers the specified retraction's algebraic/topological consequences, the complete coefficient homotopy family, and the stated finite-chart dual maps. It does not certify the analytic construction of the theta retraction, support-changing synchronization homotopies, or the matrix estimates developed here. Its branch is left untouched.

The second attachment proves, for an unrestricted finite correction matrix $B$, the exact formula

$$G_B=G_{\perp,m}+(B+H_m^{-1}C_m)^*H_m(B+H_m^{-1}C_m).\tag{0.1}$$

Once $m+1\ge\dim E_Z$, every positive metric ray is realized by an actual theta-boundary correction, with the arithmetic jets unchanged. Its further conclusion

$$\inf_B\epsilon_A(G_B)=\max_{\rho\in Z}|2\Re\rho-1|\tag{0.2}$$

therefore has to be retained. This note does not count unrestricted metric optimization as a new arithmetic estimate. It instead uses the unique least-norm representative for a fixed, increasing space of the original arithmetic boundaries. It proves compatibility of these representatives for all finite packets, an exact full-jet moment-matrix formula, and a joint total-degree tensor construction.

All conclusions are derived on the existing characteristic-zero theta complex over the marked tau-base. None is asserted to be an application of finite-field purity to a space merely renamed tau.

## 1. Fixed scalar, cochain, and arithmetic maps

Retain the original scalar construction

$$G(R)=\{\tau\}\sqcup\{r^\bullet:r\in R\},\qquad e_R=0_R^\bullet,$$

and the entire square

$$\boxed{\begin{array}{ccc}
G(\mathbb Z)&\xrightarrow{G(j)}&G(\mathbb C)\\
p_{\mathbb Z}\downarrow&&\downarrow p_{\mathbb C}\\
\mathbb Z&\xrightarrow{j}&\mathbb C.
\end{array}}\tag{1.1}$$

The target of $p_{\mathbb Z}$ is infinite. This quotient remains part of the marked geometry over $\mathfrak b_\tau$. Coefficient maps below fix external absence and carry a represented scalar zero to the represented scalar zero of the target.

Use the unchanged spaces

$$V=\{\phi\in\mathcal S(\mathbb R):\phi\text{ even},\ \phi(0)=0,\ \int_{\mathbb R}\phi=0\},$$

$$\mathscr B=\{F\in C^\infty(\mathbb R_{>0}):\sup_{x>0}x^b|D^kF(x)|<\infty\ \forall b\in\mathbb Z,k\ge0\},\qquad D=-x\partial_x,$$

$$\Theta\phi(x)=\sum_{m\ne0}\phi(mx),\quad C_+=[V\xrightarrow{\Theta}\mathscr B],\quad Q=\mathscr B/\Theta V.$$

The complex is in degrees $0,1$. Write $q:\mathscr B\to Q$. Its action is by the original $D$, not a shifted operator. Let

$$\mathcal MF(s)=\int_0^\infty F(x)x^s\frac{dx}{x},\quad
\phi_*(x)=(4\pi^2x^4-6\pi x^2)e^{-\pi x^2},\quad f_0=\Theta\phi_*,$$

$$g(s)=2\xi(s)=s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),\qquad\mathcal Mf_0=g.\tag{1.2}$$

The established range identities are used with these exact constants. They give $\mathcal M\Theta\phi=gH_\phi$, with $H_\phi$ entire. In particular every finite jet map used below annihilates $\Theta V$.

For $n\ge0$, retain

$$V_n=\operatorname{span}\{\phi_*,D\phi_*,\ldots,D^n\phi_*\},\qquad L_n=\Theta V_n,$$

$$Q_n=\mathscr B/L_n\longrightarrow Q_{n+1},\qquad\ker= L_{n+1}/L_n.\tag{1.3}$$

Their split reconstructions have labels $V_n$. The transport of a class in $L_{n+1}/L_n$ is the supported zero at $V_{n+1}$; it is not external absence. The derivative has type $Q_n\to Q_{n+1}$ because $DL_n\subseteq L_{n+1}$.

## 2. A polynomial presentation of the actual finite representatives

Take a nonempty finite set $Z$ of actual zeros of $g$, with their complete orders $m_\rho$, and put

$$h(t)=\prod_{\rho\in Z}(t-\rho)^{m_\rho},\quad d=\deg h,\quad E_h=\mathbb C[t]/(h),\quad v_h(s)=g(s)/h(s).\tag{2.1}$$

The polynomial variable $t$ acts on the source by $D$ and is evaluated at $s$ by Mellin transformation. Full orders make $v_h$ nonzero at all selected centres. Let $j_h$ be the complete Hermite-jet/Chinese-remainder map into $E_h$ and retain

$$\upsilon_h=j_hv_h\in E_h^\times,\qquad\varepsilon_h=\upsilon_h^{-1}.\tag{2.2}$$

The unit $\varepsilon_h$ is not the scalar $e$. Its split scalar is $\varepsilon_h^\bullet$.

There is an actual $F_h\in\mathscr B$ with $h(D)F_h=f_0$ and $\mathcal MF_h=v_h$. It can be obtained successively from

$$S_\rho F(x)=x^{-\rho}\int_x^\infty F(y)y^{\rho-1}\,dy,\qquad(D-\rho)S_\rho F=F,\tag{2.3}$$

whenever the required Mellin value vanishes. At zero, replace the integral by its negative from $0$ to $x$, using that vanishing; at infinity use the displayed integral. The defining estimates of $\mathscr B$ prove rapid decay of every scaling derivative at both ends. Repeated zero jets permit iteration. Uniqueness follows from injectivity of Mellin and $h\mathcal MF=0\Rightarrow F=0$.

Define the linear map

$$\boxed{\mathcal T_h:\mathbb C[t]\longrightarrow\mathscr B,\qquad P\longmapsto P(D)F_h.}\tag{2.4}$$

It is injective and satisfies

$$\mathcal M\mathcal T_h(P)=\frac gh P,\quad
\mathcal T_h(hP)=\Theta(P(D)\phi_*),\quad
J_h\mathcal T_h(P)=\upsilon_h[P]_h.\tag{2.5}$$

Here $J_hF=j_h\mathcal MF$. The first equation retains the whole completed function, not its values only on the critical line.

For $N=n+d$, let $\mathcal P_N=\mathbb C[t]_{\le N}$, and define

$$\mathcal J_{h,N}:\mathcal P_N\twoheadrightarrow E_h,\qquad P\longmapsto\upsilon_h[P]_h.$$

Its exact sequence is

$$\boxed{0\longrightarrow\mathcal P_n\xrightarrow{\times h}\mathcal P_{n+d}
\xrightarrow{\mathcal J_{h,n+d}}E_h\longrightarrow0.}\tag{2.6}$$

Applying $\mathcal T_h$ sends the left map to the original theta relations $L_n$. Thus its split internal quotient has exactly the relation $P-P'\in h\mathcal P_n$, with the support label retained.

The original source section is

$$s_h(u)=\mathcal T_h(\operatorname{rem}_h(\varepsilon_hu)),\quad J_hs_h=1,\quad qs_h=\sigma_h.\tag{2.7}$$

No arbitrary metric or section has entered (2.6).

## 3. Exact arithmetic moment matrices and the full-jet interpolation formula

The Hilbert observation is $\mathcal H=L^2((0,\infty),dx)$. The precise transform map is

$$\mathcal H\xrightarrow{\mathcal L}L^2(\mathbb R,dy)
\xrightarrow{\mathcal F_+}L^2(\mathbb R,dt/(2\pi)),$$

$$\mathcal LF(y)=e^{y/2}F(e^y),\quad
\mathcal F_+\psi(t)=\int_{\mathbb R}\psi(y)e^{ity}dy,\quad
(\mathcal F_+\mathcal LF)(t)=\mathcal MF(\tfrac12+it).\tag{3.1}$$

Both arrows are unitary with these measures. The inverse Fourier factor is $1/(2\pi)$; no mass of a measure below is set equal to one. The same map carries $D$ to multiplication by $s_t=1/2+it$.

Define the finite positive measure

$$\boxed{d\nu_h(t)=\left|\frac{g(\tfrac12+it)}{h(\tfrac12+it)}\right|^2\frac{dt}{2\pi}.}\tag{3.2}$$

Any apparent singularity at a selected critical-line zero is removed by the entire function $v_h$. All moments are finite. In the fixed basis $1,t,\ldots,t^N$ of $\mathcal P_N$, put

$$(M_{h,N})_{ij}=\int_{\mathbb R}\overline{s_t^i}s_t^j\,d\nu_h(t),\qquad 0\le i,j\le N.\tag{3.3}$$

In the integrand $t$ is the real integration variable; the polynomial basis is evaluated at $s_t$. This prevents the polynomial variable from being confused with the spectral-height coordinate.

The matrix $M_{h,N}$ is positive definite. A polynomial with zero norm vanishes almost everywhere on a line on which $v_h$ is nonzero almost everywhere, hence is zero. Write $J_{h,N}$ for the matrix of $\mathcal J_{h,N}$ in the fixed quotient basis $1,t,\ldots,t^{d-1}$. It includes multiplication by the actual unit $\upsilon_h$.

Set

$$\boxed{\mathcal C_{h,N}=J_{h,N}M_{h,N}^{-1}J_{h,N}^*,\qquad
C_{h,N}=M_{h,N}^{-1}J_{h,N}^*\mathcal C_{h,N}^{-1}.}\tag{3.4}$$

These are finite matrices on declared coordinate spaces. $J_{h,N}C_{h,N}=1$. The actual test-function map is

$$R_{h,n}=\mathcal T_h C_{h,n+d}:E_h\longrightarrow\mathscr B.\tag{3.5}$$

**Theorem.** This is precisely the preceding orthogonal representative $(1-P_n)s_h$, where $P_n$ is the $L^2(dx)$ orthogonal projection onto $L_n$. In particular,

$$\boxed{qR_{h,n}=\sigma_h,\quad J_hR_{h,n}=1,\quad
G_{h,n}:=R_{h,n}^*R_{h,n}=\mathcal C_{h,n+d}^{-1}.}\tag{3.6}$$

**Proof.** Every polynomial with jet $u$ is $C_{h,N}u+z$ with $J_{h,N}z=0$. The cross term vanishes because

$$z^*M_{h,N}C_{h,N}u=z^*J_{h,N}^*\mathcal C_{h,N}^{-1}u=0.$$

Its norm is therefore $u^*\mathcal C_{h,N}^{-1}u+z^*M_{h,N}z$. This proves the unique minimizer. By (2.6), its difference from the degree-below-$d$ lift (2.7) is exactly a member of $L_n$. It must be $(1-P_n)s_h$. This also proves (3.6).

Thus the subtraction-of-nearby-Grams formula of the previous note has the exact alternative (3.6): invert the full-jet interpolation matrix. This is a matrix-valued Christoffel construction with the arithmetic local unit retained. The finite least-norm identity itself is standard linear algebra; its application here identifies the actual original representative, source relation, and completed multiplier.

For one simple zero $\rho$, the same formula is

$$G_{\rho,n}=\frac{1}{|g'(\rho)|^2\,\mathcal K_{\nu_\rho,n+1}(\rho,\rho)},\quad
\mathcal K_{\nu,N}(z,w)=(1,z,\ldots,z^N)M_N^{-1}(1,w,\ldots,w^N)^*.\tag{3.7}$$

The complex conjugate in the second evaluation is part of the displayed kernel. Higher orders use (3.4), not just point evaluations. The factor $g'=2\xi'$ is retained.

## 4. All finite packets fit the same source filtration

Let $h\mid H$ be polynomials for nested packets with full orders and set $m=H/h$. Since the newly added centres are disjoint, $h$ and $m$ are coprime. There is a $\mathbb C[t]$-linear CRT injection

$$\iota_{hH}:E_h\hookrightarrow E_H,$$

which inserts zero jets at the new centres. It is multiplication by the appropriate CRT idempotent after lifting a residue; it sends the unit of $E_h$ to that idempotent, so it is not being asserted to be a unital ring map.

The polynomial map $P\mapsto mP$ has the exact properties

$$\mathcal T_H(mP)=\mathcal T_h(P),\qquad
J_H\mathcal T_h(P)=\iota_{hH}\mathcal J_h(P),\tag{4.1}$$

and is isometric from $\nu_h$ to $\nu_H$ because $|v_HmP|=|v_hP|$. The CRT equations and degree bounds prove

$$s_H\iota_{hH}=s_h.$$

The original $L_n$ is independent of the packet, so

$$\boxed{R_{H,n}\iota_{hH}=R_{h,n},\quad
\iota_{hH}^*G_{H,n}\iota_{hH}=G_{h,n},\quad
\iota_{hH}^*W_{H,n}\iota_{hH}=W_{h,n}.}\tag{4.2}$$

The action also intertwines: $A_H\iota_{hH}=\iota_{hH}A_h$, where $A_h=M_t$. Thus a certificate on the larger packet restricts by this actual congruence to the smaller packet. The inverse interpolation matrices satisfy the corresponding inverse-compression formula; inverse and compression are not commuted.

The finite sections consequently glue on the algebraic direct limit of the actual packet injections. This statement does not assert convergence of an infinite sum of packet projectors or identify the whole $Q$ with that direct limit.

At every support label, lift these maps as $(\lambda,u)\mapsto(\lambda,\iota_{hH}u)$ and $(\lambda,u)\mapsto(\lambda,R_{h,n}u)$. Added zero jets remain represented zeros. The label map in (1.3) is still the map that admits one more source relation.

## 5. A global density result, with its precise cohomological consequence

The single derivative family $\{D^nf_0:n\ge0\}$ is already dense in $\mathcal H$.

**Proof.** Put $d\nu(t)=|g(1/2+it)|^2dt/(2\pi)$. It has an exponential moment of every order $c<\pi/2$. To verify this, the alternating-series formula and partial summation give

$$|\zeta(\tfrac12+it)|\le\frac{2|\tfrac12+it|}{\sqrt2-1}.$$

The gamma vertical-line asymptotic gives, for sufficiently large $|t|$,

$$|g(\tfrac12+it)|^2\le C(1+|t|)^{11/2}e^{-\pi|t|/2}.$$

The constant $C$ is a fixed bound, not a numerical enclosure claimed here. The gamma fact used is NIST DLMF 5.11.9. The same exponential-moment property holds for $\nu_h$, since $v_h$ is entire at the finitely many possible denominator zeros and has polynomially modified tails.

If $f\in L^2(\nu)$ is orthogonal to every polynomial, the finite measure $\overline f\,d\nu$ has a holomorphic Fourier transform in a nonempty horizontal strip, by Cauchy–Schwarz and the exponential moment. All derivatives at the origin vanish. Analytic uniqueness makes its transform zero; Fourier uniqueness for finite measures makes the measure zero. Thus polynomials are dense in $L^2(\nu)$.

Multiplication by the actual function $g(1/2+it)$ is a unitary map $L^2(\nu)\to L^2(dt/(2\pi))$: its inverse divides by $g$ away from its measure-zero set of real-line zeros. The inverse is a map of weighted $L^2$ spaces, not holomorphic division through an arithmetic zero. Combining it with (3.1) sends polynomials to $P(D)f_0$. This proves the assertion.

It follows for each fixed packet that

$$\boxed{G_{h,n}\longrightarrow0\quad\text{in every matrix entry and in operator norm}.}\tag{5.1}$$

Indeed $P_n\to1$ strongly on $\mathcal H$, and the finite number of columns of $s_h$ is fixed. Since each $G_{h,n}$ is positive definite, the least eigenvalue of its inverse tends to infinity. Every nonzero arithmetic row functional $\ell:E_h\to\mathbb C$ therefore has

$$\boxed{\|\ell\|_{G_{h,n}^{\vee}}^2=
\ell\mathcal C_{h,n+d}\ell^*\longrightarrow\infty.}\tag{5.2}$$

These facts do not kill a cohomology class. The actual maps are

$$\mathscr B/L_n\longrightarrow\mathcal H/L_n,\qquad
Q=\mathscr B/\Theta V\longrightarrow\mathcal H/\overline{\Theta V}^{\mathcal H}=0.\tag{5.3}$$

The first map is injective because $L_n$ is finite-dimensional and consists of the same smooth functions in both spaces. The second map forgets the stronger topology and has the whole $Q$ as kernel. Its split lift lands at the represented zero in $G(0)$, not at $\tau$. $G(0)$ retains both elements. An active class may therefore tend to zero under the $L^2$ observation while remaining fixed by $qR_{h,n}=\sigma_h$ and $J_hR_{h,n}=1$.

The constructive consequence is to estimate relative boundary flux against the complete interpolation cost (3.4), not to use the absolute smallness of $G_{h,n}$ as a weight bound.

## 6. Tail representation and same-metric reflection control

Retain the unscaled orthogonal vectors from the previous calculation:

$$u_0=f_0,\quad u_n=(1-P_{n-1})D^nf_0,\quad\mathfrak h_n=\|u_n\|^2,$$

$$Du_n=u_{n+1}+\tfrac12u_n-\frac{\mathfrak h_n}{\mathfrak h_{n-1}}u_{n-1}\quad(n\ge1).\tag{6.1}$$

The identity $D^*=1-D$ fixes the real part of the diagonal to $1/2$ and gives the negative last coefficient. Here the actual seed $f_0=\Theta\phi_*$ is real, $D$ preserves real functions, and the Gram--Schmidt projections of this real Krylov family preserve reality. Thus the diagonal coefficient is real and is exactly $1/2$. Equivalently, the actual spectral weight $|g(1/2+it)|^2$ is even and the centered orthogonal polynomials have the corresponding parity. Neither the $u_n$ nor their norms are rescaled. Define $r_n=\mathfrak h_n^{-1}u_n^*s_h$. The new density result makes the entire tail formula exact:

$$\boxed{G_{h,n}=\sum_{j>n}\mathfrak h_j r_j^*r_j.}\tag{6.2}$$

This series converges in finite matrix norm. Its source map is $u\mapsto(r_j u)_{j>n}$ into the weighted sequence space with norm $\sum_{j>n}\mathfrak h_j|c_j|^2$. The map retains every coefficient; it is an isometry for $G_{h,n}$.

The previous boundary calculation, or telescoping (6.1), gives

$$\boxed{W_{h,n}=A_h^*G_{h,n}+G_{h,n}A_h-G_{h,n}
=\mathfrak h_{n+1}(r_{n+1}^*r_n+r_n^*r_{n+1}).}\tag{6.3}$$

It pairs two explicit maps into $L_{n+1}/L_n$. At the original support $V_n$ the derivative defect is $-[u_{n+1}]r_n$; at $V_{n+1}$ it becomes the supported zero. This is also the input to the now-checked coefficient homotopy family, with $\kappa_n=K_nJ_h$ and $\kappa_n\Theta=0$.

For a reflection-stable packet define the actual antilinear involution

$$j_hu(s)=\overline{u(1-\bar s)}\pmod h.$$

On functions use $j_BF(x)=x^{-1}\overline{F(1/x)}$. It is antiunitary on $\mathcal H$ and satisfies $Dj_B=j_B(1-D)$. The specific section (2.7) satisfies $j_Bs_h=s_hj_h$: since $h^\dagger=(-1)^dh$, both the unit and the numerator have the corresponding $(-1)^d$ factor. Also $j_BL_n=L_n$, so uniqueness of orthogonal projection gives $j_BR_{h,n}=R_{h,n}j_h$.

Write $j_hu=C_h\bar u$ in the retained coordinates. Then

$$\boxed{C_h^*G_{h,n}C_h=\overline{G_{h,n}},\quad
A_hC_h=C_h(I-\overline{A_h}),\quad
C_h^*W_{h,n}C_h=-\overline{W_{h,n}}.}\tag{6.4}$$

Consequently the generalized spectrum of $(W_{h,n},G_{h,n})$ is symmetric under $\lambda\mapsto-\lambda$ **for this same canonical metric**, with full multiplicities retained. An upper inequality $W_{h,n}\preceq\epsilon G_{h,n}$ therefore implies the lower inequality $W_{h,n}\succeq-\epsilon G_{h,n}$ by applying $j_h$ to the input vector.

The residue duality is still the separate explicit morphism with matrix $S_h$, and its pulled-back metric is $S_h^*G_{h,n}^{-1}S_h$. The relation to the current metric is the linear map $G_{h,n}^{-1}S_h$ into its antilinear dual coordinates. The arithmetic Weil form remains $S_hJ_g$; no positivity is supplied merely by (6.4).

For completeness, retain the full rank-two formula

$$a_n=r_nG_{h,n}^{-1}r_n^*,\quad b_n=r_{n+1}G_{h,n}^{-1}r_{n+1}^*,\quad c_n=r_nG_{h,n}^{-1}r_{n+1}^*.$$

The least control excess is

$$\epsilon_{h,n}=\mathfrak h_{n+1}\left(|\Re c_n|+\sqrt{a_nb_n-(\Im c_n)^2}\right).\tag{6.5}$$

For reflection-stable $Z$, the additional proved identity is $\Re c_n=0$: take the trace of $G_{h,n}^{-1}W_{h,n}$, which is $2\Re\operatorname{Tr}A_h-d=0$. Thus (6.5) also equals $\mathfrak h_{n+1}\sqrt{a_nb_n-(\Im c_n)^2}$. Both equations are retained. Equation (3.6) supplies every occurrence of $G_{h,n}^{-1}$ without a difference of nearly equal Gram matrices.

## 7. Joint total-degree control on the actual product complex

The tensor degree will be denoted $k$, independently of the relation degree $n$ and the packet multiplicities. Put

$$E_h^{(k)}=E_h^{\otimes k},\quad
A_h^{(k)}=\sum_{j=1}^k I^{\otimes(j-1)}\otimes A_h\otimes I^{\otimes(k-j)}.$$

The existing product complex over $\mathfrak b_\tau$ has differential

$$d(x_1\otimes\cdots\otimes x_k)=\sum_j(-1)^{\sum_{i<j}|x_i|}x_1\otimes\cdots\otimes dx_j\otimes\cdots\otimes x_k.$$

Define $\mathcal P_M^{(k)}=\mathbb C[t_1,\ldots,t_k]_{\text{total degree}\le M}$ for $M\ge k(d-1)$ and

$$\mathcal T_h^{(k)}P=P(D_1,\ldots,D_k)(F_h^{\otimes k}).\tag{7.1}$$

Its Mellin transform is $P(s_1,\ldots,s_k)\prod_j g(s_j)/h(s_j)$. Its full jet map $J_{k,M}$ is reduction modulo each $h(t_j)$ followed by multiplication by $\upsilon_h^{\otimes k}$. The target is $E_h^{(k)}$ and this map is surjective. The tensor remainder basis has total degree at most $k(d-1)$.

The exact relation space is

$$\mathcal I_{k,M}=\mathcal P_M^{(k)}\cap(h(t_1),\ldots,h(t_k)).\tag{7.2}$$

Polynomial division in the fixed order $t_1,\ldots,t_k$ represents each member as $\sum_j h(t_j)P_j$, with $\deg P_j\le M-d$. It terminates because every $h$ is monic and replacing a leading power lowers total degree. Under (7.1), each term is an actual top cochain boundary: in the $j$-th source factor use $\phi_*$ in place of $F_h$ and give its primitive the factor $(-1)^{j-1}$. The differential contributes the second $(-1)^{j-1}$. The resulting boundary is $+h(t_j)P_j$ with no removed sign.

Thus these joint corrections are maps in the original product complex, not freely chosen positive tensor metrics. Set $\mathcal B_{k,M}=\mathcal T_h^{(k)}\mathcal I_{k,M}$.

The moment matrix on the monomials of total degree at most $M$ is

$$\boxed{(M_{k,M})_{\alpha\beta}=\prod_{j=1}^k\int\overline{s_t^{\alpha_j}}s_t^{\beta_j}\,d\nu_h(t).}\tag{7.3}$$

Its positive definiteness follows because a polynomial cannot vanish almost everywhere on the full real product unless it is zero. It is a principal submatrix of the stated product moment matrix, not a declaration that the total-degree space is a tensor product of smaller univariate spaces.

The actual joint least-norm representative and its metric are

$$\boxed{R_{k,M}=\mathcal T_h^{(k)}M_{k,M}^{-1}J_{k,M}^*
(J_{k,M}M_{k,M}^{-1}J_{k,M}^*)^{-1},}$$

$$\boxed{G_{k,M}=(J_{k,M}M_{k,M}^{-1}J_{k,M}^*)^{-1}.}\tag{7.4}$$

The proof is the same explicit constrained-minimum calculation as (3.6), now with the relation ideal (7.2). In particular its arithmetic class is exactly $\sigma_h^{\otimes k}$ and every jet is fixed.

For a rectangular degree budget $N$ one has the actual inclusion

$$\mathcal P_N^{\otimes k}\hookrightarrow\mathcal P_{kN}^{(k)}.$$

It carries the old product representative into the feasible set of the new problem. Therefore

$$G_{k,kN}\preceq G_{h,N-d}^{\otimes k}\qquad(N\ge d).\tag{7.5}$$

This is an inequality from an inclusion of admissible original boundaries. It is not asserted to imply the same ordering of control forms, whose dependence on $A$ is retained separately.

## 8. The product error is one new total-degree layer

Let $\mathcal H_k=L^2(\mathbb R_{>0}^k,d^kx)$, and let $P_{\mathcal B_{k,M}}$ be its orthogonal projection onto the finite-dimensional actual boundary space. With the fixed low-degree section $s_h^{\otimes k}$,

$$R_{k,M}=(1-P_{\mathcal B_{k,M}})s_h^{\otimes k}.$$

Put

$$\mathcal E_{k,M}=(1-P_{\mathcal B_{k,M}})\mathcal B_{k,M+1}.$$

Because the jet map is already onto at both degrees,

$$\boxed{\dim\mathcal E_{k,M}=\binom{M+k}{k-1}.}\tag{8.1}$$

This is $\dim\mathcal P_{M+1}^{(k)}-\dim\mathcal P_M^{(k)}$; the $d^k$ jet constraints cancel from the dimension difference.

Let $D^{(k)}=\sum_jD_j$. Its induced action on jets is $A_h^{(k)}$. The actual derivative defect lies in $\mathcal B_{k,M+1}$:

$$B_{k,M}=D^{(k)}R_{k,M}-R_{k,M}A_h^{(k)}.$$

Define the two explicitly typed maps into the same new relation layer

$$Y_{k,M}=P_{\mathcal E_{k,M}}R_{k,M}:E_h^{(k)}\to\mathcal E_{k,M},$$

$$C_{k,M}=(1-P_{\mathcal B_{k,M}})B_{k,M}:E_h^{(k)}\to\mathcal E_{k,M}.$$

Integration by parts gives $(D^{(k)})^*+D^{(k)}=kI$ on these functions. Orthogonality then proves

$$\boxed{W_{k,M}:=(A_h^{(k)})^*G_{k,M}+G_{k,M}A_h^{(k)}-kG_{k,M}
=-(Y_{k,M}^*C_{k,M}+C_{k,M}^*Y_{k,M}),}\tag{8.2}$$

$$\boxed{G_{k,M}-G_{k,M+1}=Y_{k,M}^*Y_{k,M},\qquad
\operatorname{rank}W_{k,M}\le2\binom{M+k}{k-1}.}\tag{8.3}$$

For (8.3), use the orthogonal decomposition $\mathcal B_{k,M+1}=\mathcal B_{k,M}\oplus\mathcal E_{k,M}$. Its projection sends $R_{k,M}$ to $Y_{k,M}$ and the new representative is $R_{k,M}-Y_{k,M}$.

The source quotient map is the same degree transport as before:

$$\mathcal B_{k,M+1}/\mathcal B_{k,M}\xrightarrow{\sim}\mathcal E_{k,M},\quad[z]\mapsto(1-P_{\mathcal B_{k,M}})z.$$

A derivative class in this kernel becomes the supported zero only at the next total-degree label. The primitive retains which tensor factor supplied the theta boundary and its cochain sign. Synchronization by $(1,e)$ in each required two-leg factor supplies the common joint support, while the original mask remains recorded.

Thus the product estimate need not simply copy $k$ identical one-factor errors: (8.2) gives a new jointly optimized boundary-layer expression with completely specified moment data and maps. Its rank bound alone does not bound its generalized eigenvalues.

## 9. Same-metric reflection and residue duality on the product

For a reflection-stable packet, $j_h^{\otimes k}$ is the antilinear involution on $E_h^{(k)}$, defined on pure tensors by applying $j_h$ to every factor. The corresponding function reflection is $F(x_1,\ldots,x_k)\mapsto\prod_jx_j^{-1}\overline{F(x_1^{-1},\ldots,x_k^{-1})}$.

It preserves both the total-degree numerator space and its relation ideal. Since $(g/h)^\dagger=(-1)^d(g/h)$, its action on a numerator is $(-1)^{kd}P^\dagger$; this factor is retained. Uniqueness of the minimum in (7.4) proves reflection compatibility of $R_{k,M}$. Therefore the analogue of (6.4) gives symmetry of the generalized spectrum of $(W_{k,M},G_{k,M})$ on the same metric.

Residue duality remains the explicitly specified map with matrix $S_h^{\otimes k}$ and target line $\mathcal L_k$, on which dilation acts by $a^k$. It satisfies

$$(A_h^{(k)})^*S_h^{\otimes k}+S_h^{\otimes k}A_h^{(k)}=kS_h^{\otimes k}.$$

Any fixed degree-orientation scalar in the cochain evaluation is retained separately; the ordered product of the scalar residue pairings here has matrix exactly $S_h^{\otimes k}$.

Its dual metric and control are

$$G_{k,M}^{\mathrm D}=(S_h^{\otimes k})^*G_{k,M}^{-1}S_h^{\otimes k},$$

$$W_{k,M}^{\mathrm D}=-(S_h^{\otimes k})^*G_{k,M}^{-1}W_{k,M}G_{k,M}^{-1}S_h^{\otimes k}.\tag{9.1}$$

The Jacobian contraction is still the original multiplication trace, with every multiplicity, and is unchanged by the source boundaries used to construct (7.4). Neither (9.1) nor reflection alone establishes an arithmetic upper bound.

## 10. Quantitative certificate and the Deligne comparison

For one or several variables write $M$ for the positive moment matrix, $J$ for its fixed full-jet map, and $\mathcal C=JM^{-1}J^*$. These actual matrices now replace an unrestricted metric search.

A useful deterministic enclosure is as follows. Suppose a Hermitian approximation $\widehat M$ has a verified bound $\|M-\widehat M\|\le\eta$ and $\widehat M\succeq\mu I$ for a retained $\mu>\eta$. Then

$$\|M^{-1}-\widehat M^{-1}\|\le\frac{\eta}{\mu(\mu-\eta)},\quad
\|\mathcal C-J\widehat M^{-1}J^*\|\le\|J\|^2\frac{\eta}{\mu(\mu-\eta)}.\tag{10.1}$$

This is the resolvent identity for inverses. The positive lower bound on $\mathcal C$ must also be retained before a second inversion. With $\widehat G$ and $\widehat W$ and verified errors $\eta_G,\eta_W$, the sufficient matrix certificate is

$$\widehat G-\eta_GI\succ0,\qquad
\epsilon\widehat G\pm\widehat W-(\epsilon\eta_G+\eta_W)I\succeq0.\tag{10.2}$$

No numerical interval enclosure for the actual infinite arithmetic moments is claimed merely from a floating-point calculation. The previous exterior-theta sums give another exact representation of their one-variable inputs; all tails and roundoff must be supplied to (10.1).

Deligne's retained Corollaries 3.3.4–3.3.6 place upper and dual lower bounds on the same compact-to-ordinary image; the tensor step in 3.2.13 improves an estimate only after additional geometric control. This note supplies a canonical coherent family, its exact source relation ideal on products, and the same-metric reflection/dual operations with which such an upper estimate can now be tested. It does not import finite-field hypotheses into the tau chart.

For an actual eigenvector $A_hv=\rho v$, every constructed tensor metric still has the exact diagnostic

$$\frac{(v^{\otimes k})^*W_{k,M}v^{\otimes k}}
{(v^{\otimes k})^*G_{k,M}v^{\otimes k}}
=k(2\Re\rho-1).\tag{10.3}$$

The quantity to bound is therefore the generalized boundary form (8.2) relative to (7.4). A dimension/rank estimate, a decrease of a Gram matrix, or unrestricted metric realizability is not substituted for that relative estimate. The new constructive route is the exact finite full-jet moment problem together with its next-layer flux, not another homotopy choice.

## 11. Reading, provenance, and validation

Newly read: both supplied formalization/control notes in full; the preceding local `Tau_Homotopy_Boundary_Control/NOTE.tex`, especially sections 4–10; the retained Deligne English TeX excerpt 3.3.4–3.3.6 and French 6.2.4–6.2.7. This is not a new audit of every page of Weil II. No OCR or PDF extraction was used. Source hashes are in the package reading record.

External context checked: NIST DLMF 5.11.9 for the gamma bound; Connes–Consani–Moscovici, arXiv:2403.01247, abstract, for prior moment/Jacobi constructions from squared absolute local factors; Romik, arXiv:1902.06330, abstract, for prior orthogonal-polynomial expansions of Xi; Lasserre–Pauwels, arXiv:1606.03858, abstract, for inverse-moment/Christoffel context. Only the gamma asymptotic is used as an external estimate; the other papers are priority/context references, not sources of an unread theorem. The arguments above prove the specific maps used here.

The accompanying exact checker uses declared finite discrete calibration measures and rational complex polynomial data. It checks the general finite matrix identities, joint relation ranks, signs, full repeated-root reductions, reflection, naturality, and comparison metrics. Its model polynomial is never labelled an arithmetic zeta counterexample. Analytic density, asymptotic gamma bounds, and the original theta range identities are written arguments, not certified by those finite tests. No new Lean execution is claimed. No RH or GRH conclusion is claimed.
