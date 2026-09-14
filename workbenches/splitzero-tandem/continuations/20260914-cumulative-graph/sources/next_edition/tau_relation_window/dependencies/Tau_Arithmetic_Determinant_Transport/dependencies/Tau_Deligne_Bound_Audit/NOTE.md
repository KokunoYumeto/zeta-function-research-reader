---
title: "The Deligne-to-RH estimate: a failure-of-implication certificate"
subtitle: "The original split base, a pure exponential counterexample, and the Gamma reference obstruction"
date: "13 September 2026"
---

# Result and scope

The requested alternative is to prove the remaining arithmetic estimate or demonstrate why the current Deligne analogue does not imply it. This note establishes the second alternative. It does **not** prove that the desired estimate for the original function $g=2\xi$ is false, and it does not refute the split-zero construction.

Two concrete conclusions are proved.

**Operator counterexample.** The polynomial-exponential construction used in the programme has pure weight-one finite-field cohomology for an explicit polynomial whose recovered complex multiplication operator has eigenvalue $3/4$. A reflection-stable rational quartet gives the same counterexample without breaking the fixed reflection. Thus purity of this auxiliary exponential cohomology cannot be transferred to the arithmetic multiplication operator by the existing coefficient and period maps alone.

**Quantitative reference counterexample.** On the exact Gamma reference already used in the programme, with canonical polynomial representatives and their literal masses, an explicit reflection-stable quartet has

$$
\liminf_{k\to\infty}
\frac{\mathcal B_k^\Gamma}{q_k\log k}\ge4.
\tag{1}
$$

Its auxiliary exponential cohomology nevertheless satisfies the same Deligne purity theorem. Hence a sub-threshold upper estimate cannot be deduced from that auxiliary purity, canonical positivity, source convolution, split support, and the displayed generic quotient identities. The full arithmetic multiplier must supply an additional estimate; its precise signed place in the volume formula is given in Section 6.

These are counterexamples to particular **inferences**. The example polynomials are not asserted to divide $2\xi$. All assertions about the original arithmetic source retain its original $g,h,\Theta$ and full Taylor unit.

# 1. The actual target and original source

Retain the original semiring

$$
G(R)=\{\tau\}\sqcup R^\bullet,\qquad e_R=0_R^\bullet,
\qquad p_R(\tau)=0,\quad p_R(r^\bullet)=r.
\tag{2}
$$

The Boolean support observation is $b_R(\tau)=0$, $b_R(r^\bullet)=1$. The map $(p_R,b_R)$ is injective. The original structural diagram remains

$$
\begin{array}{ccc}
G(\mathbb Z)&\xrightarrow{G(\jmath)}&G(\mathbb C)\\
p_{\mathbb Z}\downarrow&&\downarrow p_{\mathbb C}\\
\mathbb Z&\xrightarrow{\jmath}&\mathbb C.
\end{array}
\tag{3}
$$

In particular its arithmetic target is infinite. No localization imposing $e=1$ is used. The higher relation modules all remain over this one scalar construction.

The original function spaces and maps, in `arithmetic_input.tex` (A1)--(A3), are

$$
\begin{aligned}
V&=\{\phi\in\mathcal S(\mathbb R)_{\mathrm{ev}}:\phi(0)=0,\ \int\phi=0\},\\
\mathscr B&=\{F:\sup_{x>0}x^b|D^jF(x)|<\infty\text{ for all }b\in\mathbb Z,j\ge0\},\\
D&=-x\partial_x,\quad
\Theta\phi(x)=2\sum_{n\ge1}\phi(nx),\quad
\mathcal MF(s)=\int_0^\infty F(x)x^{s-1}\,dx,\\
Q&=\mathscr B/\Theta V,\qquad
\mathcal M\Theta\phi=gH_\phi,\qquad g=2\xi.
\end{aligned}
\tag{4}
$$

For an actual finite packet $h$ of full zero orders, $F_h$ is the specified inverse with $\mathcal MF_h=g/h$. At tensor degree $k$, retain

$$
\mathcal V_{h,k}P=P(D_1+\cdots+D_k)F_h^{\otimes k},\quad
E_{h,k}=\mathbb C[S]/\chi_{h,k},\quad A_k=M_S.
\tag{5}
$$

Here $S=s_1+\cdots+s_k$, not the average. Its full arithmetic inclusion is

$$
\eta_{h,k}[P]=\upsilon_h^{\otimes k}P(A_h^{(k)})1,
\quad \upsilon_h=j_h(g/h),\qquad
J^{(k)}\mathcal V_{h,k}=\eta_{h,k}\pi_\chi.
\tag{6}
$$

No Taylor unit is assigned the value one. The coefficient quotient is the original remainder map, and $\eta_{h,k}$ is its specified injective observation into the larger arithmetic module.

For $N\ge q_k-1$, let $M_{k,N}$ be the Gram of the actual polynomial source and $J_N$ its remainder map. The canonical quotient metric is

$$
G_{k,N}=(J_NM_{k,N}^{-1}J_N^*)^{-1},\quad
V_{k,N}=\det G_{k,N},\quad
W_{k,N}=A_k^*G_{k,N}+G_{k,N}A_k-kG_{k,N}.
\tag{7}
$$

The actual arithmetic measure is

$$
w_h(t)=\frac{|(g/h)(1/2+it)|^2}{2\pi},\quad
m_{h,k}=w_h^{*k},\quad
\|\mathcal V_{h,k}P\|^2=\int|P(k/2+it)|^2m_{h,k}(t)\,dt.
\tag{8}
$$

The endpoint quantity is

$$
\mathcal B_{h,k}=
\log\frac{V_{k,q_k-1}V_{k,q_k}}
{V_{k,2q_k-1}V_{k,2q_k}}.
\tag{9}
$$

For the hypothetical actual quartet $1/2\pm\delta\pm i\gamma$ of full common multiplicity $m$, the supplied exterior and consecutive-window results give

$$
\begin{aligned}
q_k&=[1+k(m-1)](k+1)^2,\\
L_{h,k}&=2\delta[1+k(m-1)](k+1)
\left\lfloor\frac{(k+1)^2}{4}\right\rfloor,\\
\mathcal B_{h,k}&\ge4q_k\log(D_hk).
\end{aligned}
\tag{10}
$$

Those are inherited statements, with their written analytic and finite formalization scopes retained. A sufficient upper estimate would give a limiting upper ratio in (9), divided by $q_k\log k$, strictly below four. The present note does not claim that estimate for (8).

# 2. What Deligne controls, and the exact map that has not transported it

The supplied primary-source correction identifies *Weil II* 1.8.12 as a theorem about a lisse $\iota$-mixed sheaf on a connected finite-type scheme over a finite field, pure at one point. Constant rank is not the mixedness hypothesis. The same correction retains the strict inequality in 3.2.10, the square of the same eigenvalue in 3.2.13, and the reference to Roman **I.8.11**, namely *Weil I*. This note reads that correction as the supplied primary-review record; it does not claim a new full scan audit.

For the polynomial construction at issue, take

$$
\chi(S)=S^q+\sum_{a<q}c_aS^a,\quad
\Phi_t(S)=\frac{S^{q+1}}{q+1}
+\sum_{a<q}\frac{c_aS^{a+1}}{a+1}-tS.
\tag{11}
$$

The coefficient complex is

$$
\mathcal C_{u,t}=
[\mathbb C[u,t,S]\xrightarrow{\mathcal D_{u,t}}\mathbb C[u,t,S]dS],
\quad \mathcal D_{u,t}P=(uP'+(\chi-t)P)dS.
\tag{12}
$$

Leading-degree division gives free rank-$q$ degree-one cohomology $\mathcal H$. Its special fibre and parameter connection are

$$
\mathcal H/(u,t)\mathcal H\simeq E,\qquad
\nabla_t=\partial_t-A(t)/u,\quad A(t)=A+t\mathcal R,\qquad
(-u\nabla_t)\bmod(u,t)=A.
\tag{13}
$$

Here $\mathcal R=1_E\otimes\ell$ and $\ell$ is the original last-remainder-coefficient functional. The specialization of a free module is a valid map. The connection used on $u\ne0$ has the displayed pole at $u=0$; its recovered operator is the regular first-order operator $-u\nabla_t$ on that specialization.

For a specified coefficient reduction $R_0\to\mathbb F_Q$ of characteristic $p>q+1$ and $u\ne0$, Deligne's exponential theorem gives weight-one compact degree-one cohomology for

$$
Y^p-Y=\Phi_t(S)/u.
\tag{14}
$$

Its degree is $q+1$, its leading coefficient is $1/((q+1)u)$, and the top homogeneous projective zero set in $\mathbb P^0$ is empty. The corresponding leading form is smooth in precisely the sense used by the theorem. The finite-field comparison and the complex coefficient complex are related by the source span

$$
(R_0,\Phi,u,t)\longrightarrow
\begin{cases}
(\mathbb C,\mathcal H,\nabla_t,\Pi),\\
(\mathbb F_Q,H_c^1,\operatorname{Frob}_Q).
\end{cases}
\tag{15}
$$

The right branch controls eigenvalues of its Frobenius. The left branch recovers $A$ through (13). Their common coefficients do not add an operator intertwiner to (15).

To specify the relevant proposed intertwiner, choose the complex coefficient realization of the finite-field eigenvalues used in the definition of weight. For weight $k$, an arrow that would transfer the modulus to the arithmetic object would have the type

$$
T:(E_{h,k},Q^{A_k})\longrightarrow
(V_\iota,F_\iota),\qquad
TQ^{A_k}=F_\iota T,
\quad Q^{A_k}=e^{(\log Q)A_k}.
\tag{16}
$$

The direct application in (14) has weight one; for a tensor comparison, the target and its tensor degree would have to be supplied explicitly. Formula (16) is not one of the period or coefficient maps in the sources.

There is a useful exact fact about any arrow (16). On a generalized block $E_\lambda$ of length $r$,

$$
Q^{A_k}|_{E_\lambda}=Q^\lambda
\sum_{j=0}^{r-1}\frac{(\log Q)^j}{j!}N_\lambda^j.
\tag{17}
$$

If the target is pure of weight $k$ and $\Re\lambda\ne k/2$, then $F_\iota-Q^\lambda$ is invertible, since all its eigenvalues have modulus $Q^{k/2}$ while $|Q^\lambda|=Q^{\Re\lambda}$. Intertwining sends the nilpotent source equation to

$$
(F_\iota-Q^\lambda)^r T(E_\lambda)=0,
\tag{18}
$$

and invertibility proves $T(E_\lambda)=0$. This is a theorem about the exact kernel of a possible comparison on such blocks, not an assertion that a faithful comparison has been constructed.

# 3. An explicit counterexample to purity-by-specialization

Take the coefficient ring $R_0=\mathbb Z[1/2]$ and

$$
\chi_\lambda(S)=S-\lambda,\qquad \lambda=3/4,
\qquad \Phi_t(S)=S^2/2-(\lambda+t)S.
\tag{19}
$$

The special fibre is one-dimensional with multiplication operator $A=3/4$. For $u>0$, the upward-oriented contour $i\mathbb R$ gives

$$
\Pi_{\mathrm{up}}(u,t)=i\sqrt{2\pi u}\,
\exp\!\left(-\frac{(\lambda+t)^2}{2u}\right),
\qquad -u\,\frac{\partial_t\Pi_{\mathrm{up}}}{\Pi_{\mathrm{up}}}=\lambda+t.
\tag{20}
$$

In the period-ray ordering in the supplied note, $q=1$ has $\Gamma_1$ oriented downward. The exact orientation map is $\Gamma_{\mathrm{up}}=-\Gamma_1$, hence $\Pi_{\mathrm{up}}=-\Pi_1$. Both give the same displayed logarithmic derivative, and the unsquared sign is retained.

Formula (20) follows by $S=ix$ and the Fourier transform of $e^{-x^2/(2u)}$. Its norm is

$$
|\Pi_{\mathrm{up}}|^2=2\pi u\,e^{-(\lambda+t)^2/u}
\quad (\lambda,t\in\mathbb R).
\tag{21}
$$

Now reduce the same coefficients into any finite field of odd characteristic and take a nontrivial additive character $\psi$. With $b=\bar\lambda+t$ and $u\ne0$,

$$
\sum_{x\in\mathbb F_Q}\psi\!\left(\frac{x^2/2-bx}{u}\right)
=\psi\!\left(-\frac{b^2}{2u}\right)
\sum_{x\in\mathbb F_Q}\psi\!\left(\frac{x^2}{2u}\right).
\tag{22}
$$

The first factor has modulus one. If the second sum is $G_Q(u)$, then

$$
\begin{aligned}
|G_Q(u)|^2
&=\sum_{x,y}\psi((x^2-y^2)/(2u))\\
&=\sum_{r,s}\psi(rs/(2u))=Q.
\end{aligned}
\tag{23}
$$

The coordinate map is $r=x-y,s=x+y$, with inverse $x=(s+r)/2,y=(s-r)/2$. For $r=0$ the inner sum is $Q$; for $r\ne0$ it is zero by additive-character orthogonality. No asymptotic or unproved estimate appears here.

The degree-one cohomological trace is the **negative** of (22), because only $H_c^1$ contributes. Its Frobenius eigenvalue therefore has modulus $\sqrt Q$. This is the rank-one instance of the auxiliary purity theorem, directly checked.

Nevertheless, for every positive scalar metric $G$ on the complex special fibre,

$$
\frac{A^*G+GA-G}{G}=2(3/4)-1=1/2.
\tag{24}
$$

Thus pure auxiliary Frobenius and the exact coefficient/period specialization coexist with a complex operator off the weight-one line. The claim that (14) and (13) alone force (24) to vanish is false.

The split lift is present on the same coefficient model:

$$
G(R_0)\longrightarrow G(\mathbb C),\qquad
G(R_0)\longrightarrow G(\mathbb F_Q),
\tag{25}
$$

and all represented kernel values specialize to $e$, while $\tau$ maps to $\tau$. This preserves, rather than repairs, the counterexample to the operator inference.

The supplied translation theorem makes this phenomenon uniform: $T_aP(X)=P(X+a)$ is an explicit chain isomorphism, and

$$
T_aA_aT_a^{-1}=A+aI,\qquad
\Pi_a=f_a\Pi C_a,\qquad
f_a=\exp((-\Phi(-a)-ta)/u).
\tag{26}
$$

The factor $f_a$ is retained. Curvature of the corresponding determinant line is unchanged by its nonvanishing holomorphic scalar, whereas the additive trace defect changes by $2\dim(F)\Re a$. Thus curvature alone does not recover that scalar trace. The original arithmetic construction stays at the marked value $a=0$.

## A reflection-preserving version

To avoid relying on a translation that changes the reflection centre, take the explicit rational polynomial

$$
\begin{aligned}
h_*(S)&=\prod_{\varepsilon,\eta\in\{\pm1\}}
(S-1/2-\varepsilon/4-i\eta)\\
&=(S-1/2)^4+\frac{15}{8}(S-1/2)^2+\frac{289}{256}.
\end{aligned}
\tag{27}
$$

It is real, monic, and satisfies $h_*(1-S)=h_*(S)$. Its roots have real parts $1/4$ and $3/4$. The degree-five potential with derivative $h_*$ satisfies the same Deligne theorem at every specified good reduction of characteristic greater than five. All coefficients belong to a finite localization of $\mathbb Z$, the leading coefficient stays nonzero, and the infinity calculation remains valid.

Thus the auxiliary-purity implication still fails with the exact quartet symmetry retained. Neither (19) nor (27) is asserted to be an actual zero polynomial of $2\xi$.

# 4. A quantitative counterexample on the programme's own Gamma reference

The previous Gamma comparison fixes

$$
r_{1/4}(x)=\frac{|\Gamma(1/4+ix/2)|^2}{2\pi},
\qquad c_{1/4}=\sqrt{2\pi}.
\tag{28}
$$

Its $k$-fold convolution is

$$
r_{1/4,k}(x)=\frac{c_{1/4}^k}{c_{k/4}}\,
\frac{|\Gamma(k/4+ix/2)|^2}{2\pi},
\qquad c_a=2^{1-2a}\Gamma(2a),
\tag{29}
$$

and its mass is $(2\pi)^{k/2}$. These are exactly the existing reference, not a reference newly chosen for the counterexample.

Fix a positive integer $m$ and use $h_*^m$. Its cyclic $k$-fold sum polynomial is

$$
\begin{aligned}
\lambda_{a,b}&=k/2+(2a-k)/4+i(2b-k),\quad 0\le a,b\le k,\\
\ell_k&=1+k(m-1),\qquad q_k=\ell_k(k+1)^2,\\
\chi_k(S)&=\prod_{a,b=0}^k(S-\lambda_{a,b})^{\ell_k}.
\end{aligned}
\tag{30}
$$

For any pair of margins $a,b$, choose $t=\max(0,a+b-k)$. The occupation tuple $(t,a-t,b-t,k-a-b+t)$ is nonnegative and realizes that sum. Distinct margins have distinct real/imaginary coordinates. The nilpotency length at an occupation is $1+k(m-1)$, because the top multinomial in the sum of local nilpotents has a nonzero coefficient in characteristic zero. Thus all powers in (30) are retained, including for $m>1$.

Set $E_k=\mathbb C[S]/(\chi_k)$ and define the **canonical** metrics using the source norm

$$
\|P\|_{k,\Gamma}^2=
\int_{\mathbb R}|P(k/2+ix)|^2r_{1/4,k}(x)\,dx,
\tag{31}
$$

and the exact relation sequence

$$
0\to\mathcal P_{N-q_k}
\xrightarrow{\times\chi_k}\mathcal P_N
\xrightarrow{\pi_{\chi_k}}E_k\to0,
\qquad N\ge q_k-1.
\tag{32}
$$

An arbitrary fixed invertible full-observation multiplier can be retained: compose $\pi_{\chi_k}$ with the cyclic inclusion and multiplication by that unit. Injectivity of the latter means the same feasible set defines the canonical coefficient metric. This is not a redefinition of the original $\upsilon_h$, which remains attached whenever this reference is compared with an actual arithmetic packet.

The split lift of (32) sends $(\ell,\chi_kP)$ to $(\ell,0)$, preserves its relation source, and sends $\tau$ to $\tau$. The polynomial coefficient of the relation and every higher power of the original relation ideal remain available. The proof below does not identify higher depth with repeated adjunction of a scalar zero.

## Theorem: the reference already reaches the obstructing scale

Write $G_{k,N}^\Gamma$ for this canonical quotient Gram, $V_{k,N}^\Gamma=\det G_{k,N}^\Gamma$, and

$$
\mathcal B_k^\Gamma=
\log\frac{V_{k,q_k-1}^\Gamma V_{k,q_k}^\Gamma}
{V_{k,2q_k-1}^\Gamma V_{k,2q_k}^\Gamma}.
\tag{33}
$$

Then, for every positive integer $k$,

$$
\boxed{\mathcal B_k^\Gamma\ge
4q_k\log\left(\frac{k}{8\sqrt5}\right).}
\tag{34}
$$

In particular (1) holds. For small $k$ the right side may be negative; the inequality is still valid. Its limiting statement concerns $k\to\infty$.

### Proof, with the original finite quantities

Let $p_n$ be the monic Gamma polynomials evaluated on $S=k/2+ix$. Their exact norms and recurrence are

$$
\begin{aligned}
\omega_{k,n}^\Gamma&=(2\pi)^{k/2}n!(k/2)_n,\\
Sp_n&=p_{n+1}+\frac{k}{2}p_n-n(n+k/2-1)p_{n-1}.
\end{aligned}
\tag{35}
$$

The final term is omitted at $n=0$. One derivation uses

$$
(1-iz)^{-a+ix/2}(1+iz)^{-a-ix/2}
=\sum_{n\ge0}b_n^{(a)}(x)\frac{z^n}{n!}.
$$

Against $r_a(x)dx$, the product of two such generating functions integrates to $c_a(1-zw)^{-2a}$. Extracting coefficients gives the exact norms $c_a n!(2a)_n$. Differentiating the generating function gives the real-variable monic recurrence. Substituting $p_n(S)=i^n b_n^{(k/4)}((S-k/2)/i)$ gives (35), and (29) supplies the remaining mass factor.

In the fixed remainder basis set $b_n=[p_n]_{\chi_k}$ and

$$
K_N=\sum_{n=0}^N\frac{b_nb_n^*}{\omega_{k,n}^\Gamma},
\quad G_N=K_N^{-1},\quad
W_N=A_k^*G_N+G_NA_k-kG_N.
\tag{36}
$$

Surjectivity of the remainder map gives positive definiteness for $N\ge q_k-1$. Orthogonality proves that these are exactly the least-norm quotient metrics from (31)--(32).

Insert (35) into $A_kK_N+K_NA_k^*-kK_N$. Every interior pair cancels using the exact ratio of consecutive norms. The result is

$$
W_N=G_N\frac{b_{N+1}b_N^*+b_Nb_{N+1}^*}
{\omega_{k,N}^\Gamma}G_N.
\tag{37}
$$

Thus $\mathsf H_N=G_N^{-1}W_N$ is $G_N$-self-adjoint of rank at most two. Since the roots in (30) occur in reflected pairs,

$$
\operatorname{Tr}\mathsf H_N
=2\Re\operatorname{Tr}A_k-kq_k=0.
$$

Its possible nonzero eigenvalues are $+\epsilon_N,-\epsilon_N$.

Let $P_>$ be the $G_N$-orthogonal projection onto the sum of the full generalized eigenspaces with $\Re\lambda>k/2$. Invariance under $A_k$ makes its block matrix upper triangular, even when the orthogonal complement is not invariant. Hence

$$
\begin{aligned}
\operatorname{Tr}(P_>\mathsf H_N)
&=2\Re\operatorname{Tr}(A_k|E_>)-k\dim E_>\\
&=L_k=\frac12\ell_k(k+1)
\left\lfloor\frac{(k+1)^2}{4}\right\rfloor
\le\epsilon_N.
\end{aligned}
\tag{38}
$$

The last inequality uses the single positive control eigenline: its contribution is at most $\epsilon_N$, and the negative eigenline contributes a nonpositive quantity. The exact count yields $L_k\ge kq_k/8$.

It remains to propagate this lower allowance through the canonical degrees. Put

$$
\Lambda_N=\omega_{k,N}^\Gamma/V_{k,N}^\Gamma.
$$

For $N\ge q_k$, the rank-one kernel update gives

$$
\begin{aligned}
\delta_N&=V_N/V_{N-1},\\
b_N^*G_Nb_N&=\omega_{k,N}^\Gamma(1-\delta_N),\\
b_{N+1}^*G_Nb_{N+1}
&=\omega_{k,N+1}^\Gamma(\delta_{N+1}^{-1}-1).
\end{aligned}
\tag{39}
$$

The two-column factorization in (37) retains its complex cross term $z_N=b_N^*G_Nb_{N+1}$ and gives

$$
\epsilon_N^2=
\frac{\omega_{k,N+1}^\Gamma}{\omega_{k,N}^\Gamma}
(1-\delta_N)(\delta_{N+1}^{-1}-1)
-\frac{|z_N|^2}{(\omega_{k,N}^\Gamma)^2}
\le\frac{\Lambda_{N+1}}{\Lambda_N}.
\tag{40}
$$

Here $\Re z_N=0$ follows from the computed zero trace. Both lost factors in the final inequality are nonnegative with their specified sizes; no phase is assumed zero.

At $N=q_k-1$, use the separate original endpoint. If $\nu_0=\|\chi_k\|^2$, orthogonal expansion of the monic $\chi_k$ gives

$$
b_{q_k}^*G_{q_k-1}b_{q_k}=\nu_0-\omega_{k,q_k}^\Gamma,
\quad
V_{q_k}/V_{q_k-1}=\omega_{k,q_k}^\Gamma/\nu_0.
$$

The rank-two expression implies

$$
\epsilon_{q_k-1}^2\le
\frac{\nu_0}{\omega_{k,q_k-1}^\Gamma}
=\frac{\Lambda_{q_k}}{\Lambda_{q_k-1}}.
\tag{41}
$$

No rank-deficient preceding Gram is inverted.

Multiply (40)--(41) over either of the length-$q_k$ windows $i=q_k-1$ or $i=q_k$, and use (38). With $j=i+q_k$,

$$
L_k^{2q_k}\le\frac{\omega_{k,j}^\Gamma}{\omega_{k,i}^\Gamma}
\frac{V_{k,i}^\Gamma}{V_{k,j}^\Gamma}.
\tag{42}
$$

For the norms, every recurrence index in either window is at most $2q_k$. Since $k\le q_k$,

$$
\frac{\omega_{k,j}^\Gamma}{\omega_{k,i}^\Gamma}
=\prod_{n=i+1}^{j}n(n+k/2-1)
\le(5q_k^2)^{q_k}.
\tag{43}
$$

Combining (42), (43), and $L_k\ge kq_k/8$ gives, for each window,

$$
\log(V_{k,i}^\Gamma/V_{k,j}^\Gamma)
\ge2q_k\log(k/(8\sqrt5)).
$$

Adding the two inequalities proves (34). The common Gamma mass has cancelled only in the displayed norm and volume ratios; it remains in (35)--(36). The proof applies to all $m\ge1$ and retains the generalized blocks in (30).

## Why this is an actual counterexample to the proposed inference

For every $k$, the polynomial $\chi_k$ also defines the degree-$(q_k+1)$ exponential family in Section 2. At any specified good finite-field reduction with characteristic greater than $q_k+1$, its degree-one compact cohomology is pure of weight one by the same Deligne theorem. Its free complex coefficient fibre, residue pairing, contour periods, and split lifts remain available.

Yet its canonical Gamma-source volumes satisfy (34), the opposite of a sub-threshold upper bound. Therefore those auxiliary-purity and reference-source facts cannot imply such an upper bound. This statement concerns the reference subtree of the programme; it does not replace the actual arithmetic measure (8).

For comparison, the same construction on the explicit Gaussian convolution measure of mass $7^k$ and variance $k$ has $\omega_{k,n}=7^k k^n n!$. The identical proof gives each window at least $3q_k\log k+O(q_k)$ and therefore a combined limiting lower coefficient at least six, since $q_k=(k+1)^2$ for $m=1$. This optional comparison is not used in the Gamma theorem or any assertion about $2\xi$.

# 5. The current period and holonomy maps cannot erase this cost

The supplied SGA-period note calculates the complete period determinant, but its transport of the original metric is

$$
\widetilde G_N=\Pi^{-*}G_N\Pi^{-1},\qquad
\frac{\det\widetilde G_i}{\det\widetilde G_j}
=\frac{V_i}{V_j}.
\tag{44}
$$

Thus the evaluated common period determinant cancels from the **same** endpoint ratio. In fact, with $\widetilde W_N=\Pi^{-*}W_N\Pi^{-1}$,

$$
\widetilde G_N^{-1}\widetilde W_N
=\Pi(G_N^{-1}W_N)\Pi^{-1}.
\tag{45}
$$

This preserves every generalized control eigenvalue. In the exact period-coordinate Gram $I$, the source has changed its metric; the precise comparison operator is $G_N^{-1}\Pi^*\Pi$, whose condition number is not fixed by its determinant. Formula (45) is the map connecting these facts, not an assertion that the periods have no relation to the original source.

The original theta extension supplies an additional source-level test. Write the actual finite-domain boundary map as $B_N^{\mathrm{src}}=D^{(k)}r_N-r_NA_k=dK_N$. Integration by parts in the retained source measure gives

$$
W_N=-(r_N^*B_N^{\mathrm{src}}+(B_N^{\mathrm{src}})^*r_N).
\tag{45a}
$$

For every nonzero eigenvector $A_kv=\lambda v$, injectivity of the full-jet section gives $r_Nv\ne0$. Therefore

$$
2\Re\lambda-k=
-\frac{2\Re\langle r_Nv,B_N^{\mathrm{src}}v\rangle}{\|r_Nv\|^2},
\qquad
\frac{\|B_N^{\mathrm{src}}v\|}{\|r_Nv\|}
\ge |\Re\lambda-k/2|.
\tag{45b}
$$

The inequality is Cauchy--Schwarz applied to the displayed equality. The image of $B_N^{\mathrm{src}}v$ in the original quotient is the supported zero; the source vector and its cross-pairing remain. Declaring that pairing zero merely because the quotient kills its input would contradict (45b) on every off-weight eigenline. This is the source term requiring an estimate, not a scalar convention.

The holonomy construction similarly proves an exact source recovery and the quotient identity

$$
G_N=\overline G_N+\mathscr D_N,\qquad
\mathscr D_N=\int X_\theta^*(B^*M_\theta B)X_\theta\,\frac{d\theta}{2\pi}\succeq0.
\tag{46}
$$

With the stated relative source control it gives

$$
(1-\eta^2)G_N\preceq\overline G_N\preceq G_N.
\tag{47}
$$

The generator is still $A_k$. For any of its eigenvectors, in **each** positive phasewise metric,

$$
\frac{v^*(A_k^*G_{N,\theta}+G_{N,\theta}A_k-kG_{N,\theta})v}
{v^*G_{N,\theta}v}
=2\Re\lambda-k.
\tag{48}
$$

A close or even exact metric comparison therefore does not make that defect zero. The completed circle quotients have critical spectrum because their explicit comparison has a kernel. Completing first is not the same as the finite-source recovery: the supplied holonomy note computes kernel $(p_{L,\theta})/(\chi)$, and for a fixed finite $\chi$ its completed targets vanish for almost every phase. That cannot be substituted for a faithful full-jet image.

The same point appears in the original Connes comparison. Its actual map is

$$
\Gamma\sigma_Z:E_Z\longrightarrow
\mathcal S(\mathbb R)/\overline{\zeta(1/2+it)\mathcal S(\mathbb R)},
\quad
\ker(\Gamma\sigma_Z)=E_{Z,\mathrm{off}}.
\tag{49}
$$

An off-critical block is killed because the target multiplier $(1/2+it-\rho)^{-1}$ is a continuous Schwartz multiplier; a critical block has its explicit derivative-jet recovery. This is the supplied proof, including higher jets. After the split lift,

$$
(\ell,\sigma_Zv)\longmapsto(\ell,0),\qquad
v\in E_{Z,\mathrm{off}},
\tag{50}
$$

while $\tau\mapsto\tau$. The support records the retained kernel; it does not turn (49) into an injection. Across all actual finite packets, injectivity of this particular comparison is equivalent to absence of off-critical nontrivial zeros, by its already calculated kernel and critical retractions.

# 6. The exact arithmetic term that must supply a different estimate

The actual Gamma comparison uses

$$
m_{h,k}(x)=r_{1/4,k}(x)B_{h;k}(x).
\tag{51}
$$

The coefficient identity between the two polynomial sources is the actual linear map

$$
I_N:(\mathcal P_N,M_N^\Gamma)\longrightarrow(\mathcal P_N,M_N^{\mathrm{ar}}),
\qquad P\longmapsto P.
\tag{52}
$$

It preserves the remainder map and multiplication by $\chi$. Its induced map on the common quotient is the identity from $(E,G_N^\Gamma)$ to $(E,G_N^{\mathrm{ar}})$, with the two displayed metrics. If $R_N^\Gamma$ and $R_N^{\mathrm{ar}}$ are their canonical polynomial sections and $B$ the actual coefficient map $Q\mapsto\chi Q$, then

$$
R_N^{\mathrm{ar}}
=R_N^\Gamma-
B(B^*M_N^{\mathrm{ar}}B)^{-1}B^*M_N^{\mathrm{ar}}R_N^\Gamma.
\tag{53}
$$

Every added term is an original source relation, and its full arithmetic observation still contains (6). In the true arithmetic source, applying $\mathcal V_{h,k}$ supplies the original theta primitive. None of the reference calculations declares these norms identical.

Define the exact positive quotient-volume correction

$$
T_{k,N}=\frac{V_{k,N}^{\mathrm{ar}}}{V_{k,N}^\Gamma}.
$$

Then

$$
\boxed{\mathcal B_{h,k}^{\mathrm{ar}}
=\mathcal B_{h,k}^{\Gamma}
+\log\frac{T_{k,q_k-1}T_{k,q_k}}
{T_{k,2q_k-1}T_{k,2q_k}}.}
\tag{54}
$$

For a fixed off-line quartet displacement $\delta$, the proof of (34) with $1/4$ replaced by $\delta$ gives

$$
\mathcal B_{h,k}^{\Gamma}\ge
4q_k\log\left(\frac{\delta k}{2\sqrt5}\right).
\tag{55}
$$

Consequently a putative arithmetic upper bound $(4-\varepsilon)q_k\log k$ would require the actual signed correction in (54) to be at most

$$
-\varepsilon q_k\log k+O_h(q_k).
\tag{56}
$$

This identifies a specific negative correction, of a specific scale, in the already existing framework. It is not supplied by an upper bound on each $T_{k,N}$ separately, by positivity of a Gram, by a finite quadrature error, or by the Deligne weight of (14). The extreme bounded multiplier $B_{h;k}=1$ on the reference subtree has $T_{k,N}=1$ and correction zero, and (34) still holds. That is the exact reason a theorem using only boundedness of the multiplier could not give (56).

The special identity that distinguishes the actual arithmetic source from the reference examples is already explicit in the new upload. For an arbitrary monic test polynomial $h_0$ in the critical strip, the original theta complex supplies

$$
0\longrightarrow Q[h_0(D)]\longrightarrow E_{h_0}
\xrightarrow{\times j_{h_0}g}E_{h_0}
\longrightarrow Q/h_0(D)Q\longrightarrow0.
\tag{57}
$$

Only for a packet of actual zeros is $j_{h_0}g=0$ with the exact required orders and $g/h_0$ entire. Formula (57) is the typed comparison locating the arithmetic input omitted by an arbitrary polynomial calibration. This note does not assume that the explicit $h_*$ in (27) makes that multiplication map zero.

The remaining mathematically valid routes are therefore source-specific: bound the signed determinant correction in (54), or construct an action-compatible comparison whose kernel has been controlled without presupposing (49) is injective. Neither is furnished by declaring the existing auxiliary exponential family pure. These are statements about the already specified maps, not a prohibition on further research or a claim that the broader split-base programme cannot be developed.

# 7. Verification, attribution, and reading scope

The owner supplies the split-base construction, original theta complex, canonical arithmetic representatives, and the source notes. The Gamma identities, Christoffel--Darboux calculation, Gauss-sum orthogonality, and finite-field purity are established mathematical mechanisms. The contribution of this note is their explicit use as a failure-of-implication test for the proposed weight transfer and for the Gamma-reference upper-estimate strategy.

The attached `verify.py` runs finite exact rational/symbolic regressions. It checks the explicit quartet, finite sum-grid counts, literal Gamma norm ratios, canonical quotient maps, rank-two boundary identity, endpoint step, volume telescopes, rank-one period derivative, finite-field character orthogonality counts, supported kernel values, and metric congruence. It does not prove the all-$k$ theorem by finitely many samples; the written proof above does that. It does not certify the original arithmetic moments or provide a Lean execution.

An initial check compared two identical exponentials in different unreduced symbolic forms and failed structural expression equality. That comparison was repaired by testing their exact symbolic difference. Both initial logs and final runs are retained. No mathematical hypothesis was weakened.

The selected direct reads include the complete `arithmetic_input.tex`; the source/multiplicity and final tensor-control sections of `coherent_tensor_integration.tex`; the scalar and spectral joins in `toda_cv_exact_bridge.tex`; Sections 6--12 of `SGA_TRACE_PERIOD_CONTROL_NOTE.tex`; the complete dated primary-source correction; the specified translation maps; and the quotient/control and completion sections of the holonomy note. File hashes and exact reading ranges are in `SOURCES.json`. The GitHub main revision inspected is recorded there. No remote revision is presented as a fresh formal certificate.

# References

1. User-supplied `arithmetic_input.tex`, especially (A1)--(A13), (A17)--(A19). This supplies the actual theta map, its finite-packet exact sequence, and the canonical representative defect.
2. User-supplied `coherent_tensor_integration.tex`, especially (CT.1)--(CT.7), (CT.20)--(CT.26). It retains the Taylor-unit congruence, packet comparisons, and relative costs.
3. User-supplied `toda_cv_exact_bridge.tex`, especially (TVB.32)--(TVB.44), including the separate first-admissible-degree calculation.
4. User-supplied `SGA_TRACE_PERIOD_CONTROL_NOTE.tex`, Sections 6--12. It supplies the coefficient/period maps and explicitly records which operator and metric comparisons are, and are not, established.
5. User-supplied `Deligne_Primary_Source_Correction(2).tex` and `Exponential_Translation_Comparison(2).tex`. The correction's claimed scan-reading scope remains its own review record.
6. User-supplied `HOCHSCHILD_COMPARISON.md`, (H19)--(H25); `Tau_Holonomy_Descent_Control/NOTE.tex`, (H24)--(H44), (H64).
7. P. Deligne, *La conjecture de Weil. II*, Publications Mathématiques de l'IHÉS 52 (1980), 137--252. DOI 10.1007/BF02684780. Relevant source application: 1.8.12, 3.3.6, 3.7.2--3.7.4, with the supplied primary correction.
8. S. Bloch and H. Esnault, *Gauß--Manin determinant connections and periods for irregular connections*, arXiv:math/9912095. Cited for the classical polynomial-exponential setting, not as a source for an arithmetic RH estimate.
9. A. Connes and C. Consani, *Hochschild homology, trace map and zeta-cycles*, arXiv:2207.10419; final publication in *Cyclic Cohomology at 40*, Proceedings of Symposia in Pure Mathematics 105 (2023). The source distinguishes its all-zero Laplacian and critical-only realizations.
10. NIST Digital Library of Mathematical Functions, Sections 18.2 and 18.23, for the classical orthogonal-polynomial recurrence and generating-function setting. The literal Gamma scaling used in Section 4 is derived there from its displayed generating function and retained Fourier identity.
