# Strong source exhaustion, filtered tensor cohomology, and arithmetic degree flux

Owner-directed continuation of Zeta PR #14, 12 September 2026. New written proofs for review. The finite regression checks below are not Lean certificates or arithmetic quadrature certificates.

## 0. Scope, source, and what changes

The input is PR #14 at `3bff1b2bd87dfa2592f65c5ccc231f6ee9541dfc`, together with its supplied `NOTE.tex`. The earlier formalization supplies the original internal quotient and the algebraic/topological consequences of a specified retraction; the analytic theta maps retain their written-proof status. Neither another session's branch nor an existing definition is modified.

Three additions are proved here. First, the particular source ladder $V_n=\operatorname{span}\{D^j\phi_*:0\le j\le n\}$ exhausts the actual source in its **Schwartz topology**, with explicit finite-rank projections and seminorm error bounds. Second, all the tensor relations, relations between relations, and their signs fit into an explicit filtered cochain contraction. Third, the exact tensor control matrix can be tested on the dual interpolation space without either large matrix inversion: its whole defect is a last-degree-shell expression obtained from a one-variable recurrence. Packet enlargement has a cochain map and a calculated Gram correction; tensor minimum representatives are not presumed to be exactly natural under a change of packet.

The final uniform arithmetic upper estimate remains unproved. No statement below imports finite-field purity into the tau base, assumes that the spectrum is simple, or deletes an off-line packet. The aim is to calculate the control object and its source maps more effectively, not to rename the desired estimate.

## 1. Fixed arithmetic object and the original two zeros

Retain

$$G(R)=\{\tau\}\sqcup\{r^\bullet:r\in R\},\qquad e_R=0_R^\bullet,$$

$$\boxed{\begin{array}{ccc}
G(\mathbb Z)&\xrightarrow{G(j)}&G(\mathbb C)\\
p_{\mathbb Z}\downarrow&&\downarrow p_{\mathbb C}\\
\mathbb Z&\xrightarrow{j}&\mathbb C.
\end{array}}\tag{1.1}$$

The infinite target of $p_{\mathbb Z}$ remains attached to the marked base $\mathfrak b_\tau$. Supported zero and external absence have different lifts before this observation. An equation in an active coefficient fibre uses that fibre's additive identity. In the reconstructed carrier its value is $(\lambda,0)$, while multiplication by the original scalar $\tau$ gives the global absent point.

The spaces and operators are unchanged:

$$V=\{\phi\in\mathcal S(\mathbb R):\phi(-x)=\phi(x),\ \phi(0)=0,\ \int_{\mathbb R}\phi=0\},$$

$$\mathscr B=\{F\in C^\infty(\mathbb R_{>0}):\sup_{x>0}x^b|D^jF(x)|<\infty\text{ for every }b\in\mathbb Z,j\ge0\},\quad D=-x\partial_x,$$

$$\Theta\phi(x)=\sum_{m\ne0}\phi(mx),\qquad C_+=[V\xrightarrow{\Theta}\mathscr B],\qquad Q=\mathscr B/\Theta V.\tag{1.2}$$

The complex is in degrees $0,1$. The polynomial variable $t$ acts as this $D$. Write $q:\mathscr B\to Q$.

$$\phi_*(x)=(4\pi^2x^4-6\pi x^2)e^{-\pi x^2},\quad f_0=\Theta\phi_*,\quad g(s)=2\xi(s)=s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),$$

$$\mathcal MF(s)=\int_0^\infty F(x)x^s\frac{dx}{x},\qquad \mathcal Mf_0=g.\tag{1.3}$$

The earlier global map $\Lambda:\mathscr B\to V$ and section $s:Q\to\mathscr B$ satisfy $\Lambda\Theta=1$, $qs=1$, and $sq=1-\Theta\Lambda$. In particular $\Theta V$ is closed in the stated topology. This note uses that actual analytic construction and does not add it as a formal axiom.

## 2. The derivative ladder is strongly exhaustive, with a rate

Put $\gamma_0=e^{-\pi x^2}$ and $\gamma_2=2\pi x^2e^{-\pi x^2}$. Retain the already specified moment projection

$$P_Vf=f-f(0)\gamma_0-\left(\int f-f(0)\right)\gamma_2.\tag{2.1}$$

Use the physicists' Hermite polynomial $\mathrm H_m(y)=(-1)^me^{y^2}(d/dy)^me^{-y^2}$ and define

$$\psi_r(x)=\mathrm H_{2r}(\sqrt{2\pi}\,x)e^{-\pi x^2},\quad
\delta_r=\|\psi_r\|_{L^2(\mathbb R,dx)}^2=\frac{2^{2r}(2r)!}{\sqrt2}.\tag{2.2}$$

No $\psi_r$ is divided by its norm. The actual oscillator and its eigenvalues are

$$\mathcal H_0=-\partial_x^2+4\pi^2x^2,\quad L=1+\mathcal H_0,\quad
L\psi_r=\mu_r\psi_r,\quad \mu_r=1+2\pi(4r+1).\tag{2.3}$$

The coordinate $x$, Fourier convention $e^{-2\pi ix\xi}$, and all factors in these formulas remain fixed. Rodrigues' formula, integration by parts, and the Gaussian integral prove (2.2)--(2.3). Completeness follows as well: orthogonality to all polynomial multiples of $\gamma_0$ makes every derivative at zero of the Fourier transform of the finite measure $f\gamma_0\,dx$ vanish. Cauchy--Schwarz with Gaussian decay makes this transform entire. Analytic and Fourier uniqueness give $f=0$. Restricting to even functions gives the basis used here.

Let

$$\Pi_Nf=\sum_{r=0}^N\psi_r\frac{\langle\psi_r,f\rangle}{\delta_r},\qquad
S_n=P_V\Pi_{n+2}|_V.\tag{2.4}$$

**Strong source-exhaustion theorem.** The maps $S_n:V\to V_n$ are continuous projections onto the original

$$V_n=\operatorname{span}_{\mathbb C}\{\phi_*,D\phi_*,\ldots,D^n\phi_*\}.$$

They satisfy

$$\boxed{S_nS_m=S_{\min(n,m)},\qquad S_n\phi\longrightarrow\phi\text{ in }\mathcal S(\mathbb R).}\tag{2.5}$$

**Identification of the range.** Even Gaussian polynomials of degree at most $2n+4$ have dimension $n+3$. The value and integral conditions are independent because the moment columns of $\gamma_0,\gamma_2$ are $(1,1),(0,1)$. Their joint kernel has dimension $n+1$. Every $D^j\phi_*$ belongs to it, and its leading coefficient relative to $\psi_{j+2}$ is exactly

$$D^j\phi_*=2^{-2j-4}\psi_{j+2}+\operatorname{span}(\psi_0,\ldots,\psi_{j+1}).\tag{2.6}$$

The nonzero triangular coefficients prove that this kernel is $V_n$. Since $P_V$ fixes it, $S_n$ is the stated projection. For nesting, the correction map in (2.1) has image in $\operatorname{span}(\psi_0,\psi_1)$; both relevant $\Pi$'s fix this image and $P_V$ annihilates it. Expanding $P_V\Pi_{n+2}P_V\Pi_{m+2}$ proves (2.5).

**Quantitative estimate.** For integers $r\ge1$ and $a\ge0$,

$$\boxed{\|L^r(\phi-S_n\phi)\|_2
\le C_r\mu_{n+3}^{-a}\|L^{r+a}\phi\|_2,}\tag{2.7}$$

where the fully retained constant is

$$C_r=1+\frac{\|L^r\gamma_0\|_2+2\|L^r\gamma_2\|_2}{\sqrt2},$$

$$\|L^r\gamma_0\|_2^2=\delta_0\mu_0^{2r},\qquad
\|L^r\gamma_2\|_2^2=\frac{\delta_1\mu_1^{2r}}{16}+\frac{\delta_0\mu_0^{2r}}4.\tag{2.8}$$

For the proof, the retained Fourier convention and Cauchy--Schwarz give

$$|f(0)|\le\frac1{\sqrt2}(\|f\|_2^2+\|f'\|_2^2)^{1/2}
\le\frac1{\sqrt2}\|L^{1/2}f\|_2.$$

The same estimate applies to $\int f=\widehat f(0)$ because Fourier conjugates $L$ to itself. For $r\ge1$, (2.1) is consequently bounded by $C_r$ in the $L^r$ graph norm. Parseval applied to the tail $r'>n+2$ gives (2.7). These graph seminorms generate the Schwartz topology: the identities for $\partial_x\pm2\pi x$ bound every $x^a\partial_x^bf$ in $L^2$ by a finite oscillator graph norm, and the one-dimensional Sobolev estimate bounds the corresponding uniform seminorms. The reverse continuity is immediate from the differential expression for $L^r$.

This proves

$$\boxed{\overline{\bigcup_n V_n}^{\mathcal S}=V,\qquad
\overline{\bigcup_n\Theta V_n}^{\mathscr B}=\Theta V.}\tag{2.9}$$

The second equality uses continuity of $\Theta$ and its already-proved closed image. Algebraic union and closure remain connected by the actual quotient

$$\mathscr B/\bigcup_n\Theta V_n\twoheadrightarrow Q,\qquad
\ker=\Theta V/\bigcup_n\Theta V_n.\tag{2.10}$$

No equality of these algebraic spaces is asserted.

### Propagate this through the original quotient tower

Define

$$K_n^{\mathrm{str}}=1-\Theta S_n\Lambda:\mathscr B\to\mathscr B.\tag{2.11}$$

Then

$$\boxed{(K_n^{\mathrm{str}})^2=K_n^{\mathrm{str}},\quad
\ker K_n^{\mathrm{str}}=\Theta V_n,\quad
K_n^{\mathrm{str}}K_m^{\mathrm{str}}=K_{\max(n,m)}^{\mathrm{str}},\quad
K_n^{\mathrm{str}}F\to sqF\text{ in }\mathscr B.}\tag{2.12}$$

The kernel proof applies $q$ to $F=\Theta S_n\Lambda F$, then uses injectivity of $\Theta$. Every other equality follows from (2.5) and $\Lambda\Theta=1$. At label $n$ the original quotient therefore has the section

$$s_n^{\mathrm{str}}:\mathscr B/\Theta V_n\to\mathscr B,
\qquad [F]\mapsto K_n^{\mathrm{str}}F.\tag{2.13}$$

The support lift sends $(n,F)$ to $(n,K_n^{\mathrm{str}}F)$, and a boundary to $(n,0)$; $\tau$ stays $\tau$. The transition $n\to m$ for $m\ge n$ is represented by $K_m^{\mathrm{str}}s_n^{\mathrm{str}}$. Thus this is a coherent strong-topology tower, not a replacement by the zero Hilbert quotient.

For the previous least-$L^2$ representatives $R_{h,n}=s_h-\Theta b_{h,n}$ the exact comparison is

$$R_{h,n}-K_n^{\mathrm{str}}s_h
=\Theta(S_n\Lambda s_h-b_{h,n}).\tag{2.14}$$

Its first term can tend to zero in $L^2$ while the strong representative tends to $s\sigma_h$. The displayed original boundary records the difference.

## 3. The full finite-degree tensor complex, including all syzygies

Take an actual finite packet with complete multiplicities, and keep

$$h(t)=\prod_{\rho\in Z}(t-\rho)^{m_\rho},\quad d=\deg h,\quad
E_h=\mathbb C[t]/(h),\quad v_h=g/h,\quad
\upsilon_h=j_hv_h\in E_h^\times.\tag{3.1}$$

The established input $F_h\in\mathscr B$ satisfies $h(D)F_h=f_0$ and $\mathcal MF_h=v_h$. The coefficient unit $\upsilon_h$ is carried by $\upsilon_h\mapsto\upsilon_h^\bullet\in G(E_h)$; it is not renamed $e$.

Let $k$ be tensor degree, let $M$ be total polynomial degree, and put $\mathcal P_r^{(k)}=0$ for $r<0$. Define a genuine cochain complex by

$$\boxed{\mathcal K_{h,k,M}^{p}=
\bigoplus_{\substack{I\subseteq\{1,\ldots,k\}\\|I|=p}}
\mathcal P_{M-(k-p)d}^{(k)}.}\tag{3.2}$$

An index in $I$ is a degree-one target factor; an index outside $I$ is a degree-zero source factor. For $j\notin I$ the component of the differential is

$$d_{I\cup\{j\},I}(P)
=(-1)^{\#\{i\in I:i<j\}}h(t_j)P.\tag{3.3}$$

Every pair of orders for introducing two indices has opposite signs, so $d^2=0$. Polynomial degree grows by exactly the allowed $d$.

There is an explicit map of this complex into the original $C_+^{\otimes k}$. On the $I$-component it is

$$b_j^I=\begin{cases}\phi_*,&j\notin I,\\F_h,&j\in I,\end{cases}\qquad
\mathscr T_I(P)=P(D_1,\ldots,D_k)\left(\bigotimes_{j=1}^k b_j^I\right).\tag{3.4}$$

The factors in (3.4) remain in their original order. Applying the $j$th theta differential replaces $\phi_*$ with $f_0=h(D_j)F_h$, with precisely the sign in (3.3). This proves the cochain square. In top degree its quotient map is

$$\pi_{h,k,M}(P)=\upsilon_h^{\otimes k}[P]_{(h(t_1),\ldots,h(t_k))}.\tag{3.5}$$

### Construct a filtration-preserving homotopy

In one variable write Euclidean division in the exact form

$$P=h\,\operatorname{quo}_hP+\operatorname{rem}_hP,\qquad
\deg\operatorname{rem}_hP<d.$$

On $[\mathbb C[t]\xrightarrow{h}\mathbb C[t]]$, take $H^1=\operatorname{quo}_h$ and let $P^{\mathrm{red}}$ be zero in degree zero and remainder in degree one. Direct substitution gives

$$dH+Hd=1-P^{\mathrm{red}}.\tag{3.6}$$

On $k$ ordered factors use

$$\boxed{H_k=\sum_{j=1}^k(P^{\mathrm{red}})^{\otimes(j-1)}\otimes H\otimes1^{\otimes(k-j)},}\tag{3.7}$$

with the ordinary cochain tensor rule: the degree-$-1$ map $H$ acquires $(-1)^{|x_1|+\cdots+|x_{j-1}|}$. The terms telescope to

$$dH_k+H_kd=1-(P^{\mathrm{red}})^{\otimes k}.\tag{3.8}$$

Division lowers the degree in the divided variable by $d$, and every remainder lowers or preserves total degree. Consequently (3.7) restricts to the finite spaces (3.2). For $M\ge k(d-1)$, the inverse of (3.5) on the contracted complex is the reduced polynomial representing $\upsilon_h^{-\otimes k}u$. It fits the declared degree bound. We obtain

$$\boxed{\mathcal K_{h,k,M}^{\bullet}\simeq E_h^{\otimes k}[-k],\quad
H^p=0\ (p<k),\quad H^k=E_h^{\otimes k}.}\tag{3.9}$$

This is a computed filtered contraction. It tracks the lower-degree primitives and their syzygies, rather than counting only top-degree relations. It also gives the exact identity

$$\sum_{j=0}^k(-1)^j\binom{k}{j}\binom{M-jd+k}{k}=d^k,
\quad M\ge k(d-1),\tag{3.10}$$

with a binomial interpreted as zero when $M-jd<0$. At smaller $M$ the top dimension is the number of reduced monomials $t^\alpha$ with $0\le\alpha_j<d$ and $|\alpha|\le M$.

The usual Koszul exactness for regular sequences is background (Stacks, Tag 062F). Equations (3.2)--(3.8) supply the particular finite-degree maps and proof needed here; they do not assume a filtered exactness result without checking the filtration.

### Original split support and the operator

Reconstruct the degree-budget diagram, with joins given by maximum budget and an external bottom, together with the original chart masks. Every linear map above lifts as $(\lambda,x)\mapsto(\lambda,fx)$, with the declared budget change when one is present. Thus $\widetilde d^2(\lambda,x)=(\lambda,0)$ and the homotopy equation uses the label-preserving zero, not the constant absent map. Its top quotient is the original internal coequalizer. This is exactly the certified quotient interface; no group inverse on the whole split carrier is introduced.

Multiplication by $t_1+\cdots+t_k$ has type

$$\mathcal K_{h,k,M}^\bullet\longrightarrow\mathcal K_{h,k,M+1}^\bullet,\tag{3.11}$$

and commutes with (3.3). Its top action is $A_k=\sum_j A_j$, $A=M_t$ on $E_h$. Under (3.4) it is the unchanged $D^{(k)}=\sum_jD_j$. The nilpotent blocks of $A$ stay present.

## 4. Compute the tensor interpolation matrix without a tensor moment inverse

Retain the actual measure

$$d\nu_h(u)=\left|\frac{g(\tfrac12+iu)}{h(\tfrac12+iu)}\right|^2\frac{du}{2\pi}.\tag{4.1}$$

It has finite moments of every order by the previous analytic estimate. The integration variable is $u$; the polynomial coordinate remains $t$. The inner product is

$$\langle P,Q\rangle_h=\int\overline{P(\tfrac12+iu)}Q(\tfrac12+iu)\,d\nu_h(u).$$

Construct by subtraction from the actual monomials

$$p_0=1,\quad
p_n=t^n-\sum_{j<n}p_j\frac{\langle p_j,t^n\rangle_h}{\eta_j},\quad
\eta_j=\langle p_j,p_j\rangle_h>0.\tag{4.2}$$

These are monic polynomials; each leading coefficient remains one because the construction subtracts lower degrees. No norm is assigned value one. In particular $\eta_0$ is the actual mass of (4.1).

The change from monomials to the $p_j$ is the specified unit upper-triangular coefficient matrix $B_N$, satisfying

$$B_N^*M_{h,N}B_N=\operatorname{diag}(\eta_0,\ldots,\eta_N).\tag{4.3}$$

This is the explicit comparison between bases, not a change to $g$, $h$, the metric, or the original scalar support.

Since $\bar t=1-t$ on the integration line,

$$\boxed{tp_n=p_{n+1}+a_np_n-b_np_{n-1},\quad
 a_n=\frac{\langle p_n,tp_n\rangle_h}{\eta_n},\quad
 a_n+\bar a_n=1,\quad b_n=\frac{\eta_n}{\eta_{n-1}}>0.}\tag{4.4}$$

The last term is absent for $n=0$. Its negative sign follows from the adjoint identity for multiplication by $t$. Orthogonality kills all lower terms below $p_{n-1}$; moving multiplication to the first argument gives coefficient $-\eta_n/\eta_{n-1}$. The diagonal is allowed its full imaginary part. No extra symmetry of $\nu_h$ is imposed.

Set

$$v_n=\upsilon_h[p_n]_h\in E_h,\qquad
v_\alpha=v_{\alpha_1}\otimes\cdots\otimes v_{\alpha_k},\qquad
\eta_\alpha=\prod_j\eta_{\alpha_j}.\tag{4.5}$$

The actual finite jet map therefore carries the entire recurrence, including the local unit and nilpotents:

$$Av_n=v_{n+1}+a_nv_n-b_nv_{n-1}.\tag{4.6}$$

The products $p_\alpha$ with $|\alpha|\le M$ are an orthogonal basis of the **same total-degree numerator space** as in (3.2). Orthogonality follows from the product measure; the basis change is triangular in total degree. Therefore the input interpolation matrix is exactly

$$\boxed{\mathcal C_{k,M}=\sum_{|\alpha|\le M}\frac{v_\alpha v_\alpha^*}{\eta_\alpha}
=J_{k,M}M_{k,M}^{-1}J_{k,M}^*.}\tag{4.7}$$

For $M\ge k(d-1)$ the full jet map is onto, so $\mathcal C_{k,M}$ is positive definite. The original least-norm representative has

$$G_{k,M}=\mathcal C_{k,M}^{-1}.\tag{4.8}$$

The new formula evaluates the *dual* matrix directly by positive rank-one additions; it does not replace the original representative by a new metric. The map linking the coefficient dual to the representative is

$$z\longmapsto
\mathcal T_h^{(k)}\left(\sum_{|\alpha|\le M}p_\alpha
\frac{v_\alpha^*z}{\eta_\alpha}\right),\tag{4.9}$$

whose jet is $\mathcal C_{k,M}z$. Composing (4.9) with $z=G_{k,M}u$ recovers $R_{k,M}u$.

The customary Christoffel--Darboux mechanism is background (DLMF 18.2(iv)--(v)); (4.4)--(4.9) are proved with the actual complex-line coordinate, full arithmetic jets, and unscaled norm factors.

## 5. Exact cancellation of every interior degree: the control is one shell

Define the Hermitian matrix on the dual interpolation coordinates

$$\mathcal F_{k,M}=A_k\mathcal C_{k,M}+\mathcal C_{k,M}A_k^*-k\mathcal C_{k,M}.\tag{5.1}$$

For $|\alpha|=M$, put

$$w_\alpha=\sum_{j=1}^k v_{\alpha+e_j}.\tag{5.2}$$

**Degree-flux theorem.**

$$\boxed{\mathcal F_{k,M}=
\sum_{|\alpha|=M}\frac{w_\alpha v_\alpha^*+v_\alpha w_\alpha^*}{\eta_\alpha}.}\tag{5.3}$$

**Proof.** Apply (4.6) to every tensor factor in (4.7). Its diagonal contributions are $\sum_j(a_{\alpha_j}+\bar a_{\alpha_j})=k$, exactly canceled by the last term of (5.1). Pair the raising term at $\alpha$ with the lowering term at $\alpha+e_j$. Their coefficients are respectively $1/\eta_\alpha$ and $-b_{\alpha_j+1}/\eta_{\alpha+e_j}$; these sum to zero by (4.4). This cancels every adjacent pair contained inside $|\alpha|\le M$. Only the raising edges leaving $|\alpha|=M$ remain, giving (5.3). There is no term below index zero.

This identity keeps every imaginary diagonal, every positive norm, the minus sign in the recurrence, and the actual weight $k$ until the displayed cancellation.

The relation to the original control is the explicit congruence

$$\boxed{W_{k,M}=G_{k,M}\mathcal F_{k,M}G_{k,M},\qquad
\mathcal F_{k,M}=\mathcal C_{k,M}W_{k,M}\mathcal C_{k,M}.}\tag{5.4}$$

In particular,

$$\boxed{W_{k,M}\preceq\epsilon G_{k,M}
\quad\Longleftrightarrow\quad
\mathcal F_{k,M}\preceq\epsilon\mathcal C_{k,M}.}\tag{5.5}$$

The same holds for the lower inequality. Formula (5.5) allows the exact control test to be performed without either large matrix inversion. It changes the coordinates used to test the form through a specified invertible map; it does not change the form or suppress small eigenvalues of $G$.

To see the precise types, equip the coefficient space of degree-$M$ multi-indices with the diagonal inner product having matrix $\operatorname{diag}(\eta_\alpha)$. The two linear maps sending its basis to $v_\alpha,w_\alpha$ have adjoints carrying the reciprocal factors $1/\eta_\alpha$. Their symmetrized product is (5.3). Thus

$$\operatorname{rank}\mathcal F_{k,M}\le2\binom{M+k-1}{k-1}.\tag{5.6}$$

This is a boundary-shell rank estimate, not a bound on its generalized eigenvalues.

### Connection with the original supported next relation layer

The previous maps $Y,C:E_h^{\otimes k}\to\mathcal E_{k,M}$ satisfy

$$W_{k,M}=-(Y^*C+C^*Y),\quad
\mathcal E_{k,M}\cong\mathcal B_{k,M+1}/\mathcal B_{k,M}.$$

Combining with (5.4) gives the exact comparison

$$\mathcal F_{k,M}
=-\mathcal C_{k,M}(Y^*C+C^*Y)\mathcal C_{k,M}.\tag{5.7}$$

The top derivative of $R_{k,M}$ is a boundary in $\mathcal B_{k,M+1}$, with a primitive provided by (3.7). At degree $M$ it can be a nonzero class in the displayed relation layer; the original transport to $M+1$ sends it to that label's supported zero. The maps (3.4), (3.7), and (5.4) carry that same fact into (5.3). Taking the amplitude matrix does not retrospectively identify it with $\tau$.

## 6. Positive shell comparisons and an executable estimate interface

Set

$$\mathcal L_{k,M}=\sum_{|\alpha|=M}\frac{v_\alpha v_\alpha^*}{\eta_\alpha},\qquad
\mathcal U_{k,M}=\sum_{|\alpha|=M}\frac{w_\alpha w_\alpha^*}{\eta_\alpha}.\tag{6.1}$$

The first is the exact information increment:

$$\mathcal C_{k,M}-\mathcal C_{k,M-1}=\mathcal L_{k,M}.\tag{6.2}$$

For every real $a>0$,

$$\boxed{-(a\mathcal L_{k,M}+a^{-1}\mathcal U_{k,M})
\preceq\mathcal F_{k,M}\preceq
 a\mathcal L_{k,M}+a^{-1}\mathcal U_{k,M}.}\tag{6.3}$$

Subtracting either side yields the sum of matrices
$(\sqrt a\,v_\alpha\mp a^{-1/2}w_\alpha)
(\sqrt a\,v_\alpha\mp a^{-1/2}w_\alpha)^*/\eta_\alpha$.
This is an explicit positive decomposition, not a norm inequality with omitted cross terms.

In particular, verified comparisons $\mathcal L\preceq\ell\mathcal C$ and $\mathcal U\preceq u\mathcal C$ give $\epsilon=2\sqrt{\ell u}$ when $\ell,u>0$. These are sufficient certificates; the sharp test remains (5.5).

There is an additional entirely explicit bound from the one-variable recurrence:

$$\boxed{\mathcal U_{k,M}\preceq
k\sum_{|\beta|=M+1}\left(\sum_{j:\beta_j>0}b_{\beta_j}\right)
\frac{v_\beta v_\beta^*}{\eta_\beta}.}\tag{6.4}$$

For each $\alpha$, use $(\sum_j x_j)(\sum_jx_j)^*\preceq k\sum_jx_jx_j^*$ with $x_j=v_{\alpha+e_j}$, and retain
$1/\eta_\alpha=b_{\alpha_j+1}/\eta_{\alpha+e_j}$. This proves (6.4) by collecting the stated indices. No upper growth bound for the actual $b_j$ is assumed here.

All degrees can also be assembled by a formal power series, with no analytic convergence claim:

$$\mathsf V_h(z)=\sum_{r\ge0}\frac{v_rv_r^*}{\eta_r}z^r,\qquad
\boxed{\mathcal C_{k,M}=[z^M]\frac{\mathsf V_h(z)^{\otimes k}}{1-z}.}\tag{6.5}$$

The coefficient extraction is finite. Thus total-degree data in $k$ variables are generated from one-variable matrix coefficients by a specified convolution, rather than by separately inverting every multivariate moment matrix.

### Certified finite enclosures

For $\epsilon\ge0$, if Hermitian approximations obey $\|\mathcal C-\widehat{\mathcal C}\|\le\eta_C$ and $\|\mathcal F-\widehat{\mathcal F}\|\le\eta_F$, sufficient tests are

$$\widehat{\mathcal C}-\eta_CI\succ0,\qquad
\epsilon\widehat{\mathcal C}\pm\widehat{\mathcal F}
-(\epsilon\eta_C+\eta_F)I\succeq0.\tag{6.6}$$

These now require no inverse-enclosure step. Coefficient and moment errors have not disappeared: they enter $v_j,\eta_j$ and consequently $\eta_C,\eta_F$. For example

$$\|vv^*-\widehat v\widehat v^*\|\le2\|\widehat v\|\,\delta_v+\delta_v^2$$

when $\|v-\widehat v\|\le\delta_v$, and a positive lower bound for $\eta_j$ must be retained before using its reciprocal. The checker tests exact rational calibrations; it supplies no unevaluated arithmetic integral enclosure.

## 7. Packet enlargement on products: the exact cochain map and its metric correction

Let $H=mh$ with $h,m$ coprime, and write $\ell=\deg m$. The CRT injection $i:E_h\hookrightarrow E_H$ inserts zero jets at the new centres; it is $\mathbb C[t]$-linear and sends the unit to its CRT idempotent.

There is a cochain map on every finite-degree complex:

$$\boxed{\Phi^p_{hH}:\mathcal K_{h,k,M}^{p}
\longrightarrow\mathcal K_{H,k,M+k\ell}^{p},\qquad
(P_I)_I\longmapsto\left(P_I\prod_{j\in I}m(t_j)\right)_I.}\tag{7.1}$$

The source degree bound increases by $p\ell$, precisely the degree of the displayed multiplier. For a differential introducing $j$, the equality is

$$h(t_j)\prod_{i\in I\cup\{j\}}m(t_i)
=H(t_j)\prod_{i\in I}m(t_i),$$

with the same cochain sign on both sides. Under the actual theta maps (3.4), the functions agree because $m(D)F_H=F_h$. The top jet map is $i^{\otimes k}$.

For $k=1$, the previous common-$L_n$ argument still gives equality of canonical representatives at the matching relation budget. For $k>1$, the constructed map is (7.1); the enlarged total-degree problem may admit extra relations outside its image. The complete comparison is

$$\Delta_{hH}=R_{h,k,M}-R_{H,k,M+k\ell}i^{\otimes k}
\in\operatorname{Hom}(E_h^{\otimes k},\mathcal B_{H,k,M+k\ell}).\tag{7.2}$$

Both sides here are actual functions after (3.4). The original jets and global cohomology annihilate $\Delta_{hH}$. Orthogonality of the larger minimum to its boundary space proves

$$\boxed{G_{h,k,M}=(i^{\otimes k})^*G_{H,k,M+k\ell}i^{\otimes k}
+\Delta_{hH}^*\Delta_{hH}.}\tag{7.3}$$

Thus there is an exact Gram gap, not an assumed equality or an inverse-compression interchange. The top polynomial difference is in the enlarged relation ideal, and (3.7) gives a primitive. Its split lift becomes the supported zero under precisely that enlarged quotient. This is a cohomological comparison, not deletion of the original packet.

The corresponding control gap is

$$W_h=(i^{\otimes k})^*W_Hi^{\otimes k}
+A_{h,k}^*(\Delta^*\Delta)+(\Delta^*\Delta)A_{h,k}-k\Delta^*\Delta.\tag{7.4}$$

The full last term is retained; a positive Gram gap does not imply a positive control gap. This supplies the exact correction needed when transporting an upper estimate between differently sized product packets.

## 8. Reflection, residue trace, and the intended Deligne estimate

For a reflection-stable packet the existing involution $j_hu(s)=\overline{u(1-\bar s)}$ and its product preserve the canonical minimum. Let $C_h$ be its one-factor matrix, and set $C_{h,k}=C_h^{\otimes k}$ on $E_h^{\otimes k}$. With $G=G_{k,M}$ the identities are

$$C_{h,k}\overline{C_{h,k}}=1,\quad C_{h,k}^*G C_{h,k}=\bar G,\quad
A_kC_{h,k}=C_{h,k}(kI-\bar A_k).\tag{8.1}$$

These are the same-metric input identities proved in PR #14. In the dual information coordinates put $B_h=(C_h^{-1})^*$. Inverting only the formal identity (8.1), not performing a numerical inverse, gives

$$\boxed{(B_h^{\otimes k})^*\mathcal C(B_h^{\otimes k})=\bar{\mathcal C},\qquad
(B_h^{\otimes k})^*\mathcal F(B_h^{\otimes k})=-\bar{\mathcal F}.}\tag{8.2}$$

Thus an upper certificate in (5.5) has the opposite lower certificate for the same arithmetic family. All Jordan blocks remain.

Residue duality is retained by its original matrix $S_h^{\otimes k}$ and the action line $\mathcal L_k$. On one factor its exact contraction is

$$R_h(f,J_gu)=\operatorname{Tr}(M_{f^\dagger u}\mid E_h),\qquad
J_g=M_{j_hg'},\quad g=2\xi.\tag{8.3}$$

The representative changes (2.14) and (7.2) are original theta boundaries; they change neither this finite arithmetic trace nor the completed arithmetic function. Perfect residue duality, the positive Hilbert observation, and the Hermitian Weil form remain related by $J_g$ and the existing metric-to-dual map; none is substituted for another.

The current Deligne-like step is therefore an estimate on the explicit family (5.3) relative to (4.7). For actual $Av=\rho v$, the exact identity remains

$$\frac{(v^{\otimes k})^*W_{k,M}v^{\otimes k}}
{(v^{\otimes k})^*G_{k,M}v^{\otimes k}}
=k(2\Re\rho-1).\tag{8.4}$$

No estimate sublinear in $k$ has been established in this contribution. What has changed is that its left-hand form is now produced by a one-variable recurrence and a finite shell sum, while its entire source relation complex and approximation maps are explicit. The source-exhaustion constants (2.7)--(2.8) concern their stated graph norms; they are not assumed uniform in tensor degree or equal to the desired relative moment bound.

The supplied Deligne TeX, §§3.2.11--3.2.15 and §§3.3.4--3.3.6, was reread for the tensor-improvement and dual-image roles. The retained French witness at §3.2.13 has a missing square in one printed transcription line; this note uses only the explicitly described tensor eigenvalue map $\alpha\mapsto\alpha^2$ and does not import that corrupted line as an inequality. The derived-sign window §6.2.4--§6.2.7 was also checked. This is a bounded reading, not a fresh audit of the whole article.

## 9. Reproducibility and source boundaries

The input `NOTE.tex` was read in full. The new strong-exhaustion, filtered-contraction, and degree-flux arguments above are deductions made here. Their general analytic claims are written proofs, not statements covered by another session's Lean run.

The regression script uses exact Gaussian and finite-discrete calibration measures, rational complex polynomials, repeated roots, nonconstant coefficient units, and original supported-zero examples. It compares the shell formula with the full moment inverse, verifies all finite cochain/homotopy signs, and tests the nonzero packet-enlargement Gram gap. The calibration polynomials are not asserted to divide the Riemann function. Normal and optimized runs and intentionally failing controls are retained.

External references used for context and the standard ingredients:

- The Stacks Project, Tag 062F, regular sequences and Koszul exactness. The finite-degree contraction in (3.7) is supplied explicitly here.
- NIST DLMF, §18.2(iv)--(v), orthogonal-polynomial recurrences and the Christoffel--Darboux identity. The complex-line recurrence and full-jet tensor identity are derived in (4.4)--(5.3).
- NIST DLMF, §18.3 and §18.9, Hermite orthogonality and identities. The norm factors, oscillator, moments, and topological estimate used here are displayed in §2.
- Deligne, *La conjecture de Weil II* (1980), supplied TeX windows listed in §8. No outside finite-field weight theorem is applied to the tau chart.

Only authored exposition, test code, and provenance records are intended for public integration. The user's original definitions and all other workbenches remain unchanged.
