# Complete covariance sampling with a finite input-error certificate

22 September 2026. This derivation proves the complete-row sampling calculation in the original coefficient, Gamma and root coordinates. It also gives an arbitrary-accuracy sample count and an explicit perturbation bound for the full lower-root multiplication map. The native period-dependent covariance is not numerically evaluated here.

## CS1. Original spaces and the exact functional

Retain the original simple-quartet five-orbit domain, $k\equiv1\pmod4$, $k\ge17$, $q=(k+1)^2$, $q'=(k-7)^2$, $0<\delta<1/2$, $\gamma>2$, $R_h=\sqrt{\delta^2+\gamma^2}$, and the finite guard $q\ge2kR_h$. The fixed conductor is
\[
 E_A(w)=\sum_{a,b=0}^8a_{ab}e^{b_{ab}w},\quad
 b_{ab}=4+(2a-8)\delta+i(2b-8)\gamma,
 \quad v=\operatorname{ord}_0E_A,\quad\mu_v=E_A^{(v)}(0)\ne0.
 \tag{CS1}
\]
Set $c'=k/2-4$, $g=q-q'-v$, $r=8k-32-v+s_k$, $s_k=\dim(K\cap\mathcal P_{<v})$, and $n_E=16k-48$. The original complete invariant row space after low-degree elimination is $V_k\subset\mathbb C^{n_E}$, with its actual strip embedding $S_k:\mathbb C^{n_E}\hookrightarrow\mathbb C^q$ given by zero insertion. A row $z$ means the full-root row $zS_k^{\mathsf T}$ in an exponential sum. For its original upper roots $\beta_\alpha$, put
\[
 F_z(w)=\sum_{\alpha=1}^q(zS_k^{\mathsf T})_\alpha e^{\beta_\alpha w},
 \quad A_z(w)=e^{-c'w}F_z(w)/E_A(w),
 \quad\ell_z(y^n)=(-i)^nn![w^n]A_z(w).
 \tag{CS2}
\]
The complete low-degree constraint implies $F_z^{(j)}(0)=0$ for $j<v$; the quotient is removable at zero. The phase and center in CS2 follow from
$\partial_w^n(e^{-c'w}G)=e^{-c'w}(\partial_w-c')^nG$ and $y=(S'-c')/i$. This is the unweighted functional in the physical $y$ coordinate. On a weighted coefficient polynomial $p$, its ideal restriction is $\ell_z(Q_-p)$, with the full factor $Q_-$ inserted once.

For $q-1\le N\le2q$ put $D=N-v$, $M=D-q'$ and
\[
 Q_-(y)=i^{-q'}\chi'(c'+iy)=\prod_{a,b=0}^{k-8}(y-\omega'_{ab}),
 \quad \omega'_{ab}=(2b-k+8)\gamma-i(2a-k+8)\delta,
 \quad I_N=Q_-\mathcal P_M\subset\mathcal P_D.
 \tag{CS3}
\]
Every lower root occurs, with its exact coordinate. The source measure is $d\sigma(y)=|\Gamma(1/4+iy/2)|^2dy/(2\pi)$ and has mass $M_\sigma=\sqrt{2\pi}$. Its monic polynomials satisfy
\[
 p_{n+1}=yp_n-n(n-1/2)p_{n-1},\qquad
 \gamma_n=\|p_n\|_\sigma^2=M_\sigma n!(1/2)_n,
 \qquad\sum_{n\ge0}\frac{p_n(y)}{n!}t^n=(1+t^2)^{-1/4}e^{y\arctan t}.
 \tag{CS4}
\]
The original NIST author TeX for [DLMF18.22.8](https://dlmf.nist.gov/18.22.E8) and [18.23.7](https://dlmf.nist.gov/18.23.E7) was read. The authors are T. H. Koornwinder, R. Wong, R. Koekoek, R. F. Swarttouw and W. P. Reinhardt. CS4 is their Meixner–Pollaczek specialization with the displayed full mass.

For the original row matrix $Z$, the fixed row change $R_Z^{-1/2}$, $R_Z=ZZ^*$, gives a coefficient-orthonormal frame of $V_k$. This is a congruence on row Grams; it changes neither the source norm nor the ideal. In that frame let $W_N$ evaluate every $\ell_z$ on $p_n/\sqrt{\gamma_n}$. Let $E_D$ evaluate those polynomials at every lower root. Interpolation at the $q'$ distinct roots proves $\ker E_D=I_N$ and $\operatorname{rank}E_D=q'$. Thus
\[
 P_N=I-E_D^*(E_DE_D^*)^{-1}E_D,
 \quad C_N=W_NP_NW_N^*,\qquad B_N=W_NW_N^*.
 \tag{CS5}
\]
These denote the row-congruent original matrices throughout. The inverse congruence restores the physical row frame after calculation. If $r=0$, all row determinants are one and the sample count is zero; below $r>0$.

## CS2. Analytic inputs with their exact source status

The complete independent original-angle source, [AS6–26 of the complete original-angle proof](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/9b7b0bad40b33dc88bba7d8cb1548da1fadbb585/workbenches/splitzero-tandem/continuations/20260921-original-angle-word/ANGLE_PROOFS.md), supplies the following finite estimates; its mathematical argument was read directly. These are proved analytic inputs, not consequences of its auxiliary checker. Write $A_1=\sum|a_{ab}|$, $d_A=|\mu_v|/v!$, $B_A=\max_{a_{ab}\ne0}|b_{ab}|$, $C_{\rm path}=A_1/|a_*|$, where $a_*$ is the actual nonzero lexicographic pivot. Define
\[
 \mathfrak M_k=\max\{1,e^{1+2\pi\gamma}A_1(8q+1)^{1/4}(2q+1)(4q+1)^{4\delta}\},
\]
\[
 B_{{\rm val},k}=qM_\sigma e^{8q}\left(\frac{2q+kR_h}{2\delta k}\right)^{2(q-1)},
 \quad B_E=n_EM_\sigma\left(\frac{2n_E+kR_h}{2\delta}\right)^{2(n_E-1)},
\]
\[
 c_k=(\mathfrak M_k^2B_{{\rm val},k}qC_{\rm path}^{20k})^{-1},\quad
 b_k^-=(\mathfrak M_k^2B_E)^{-1},
 \qquad C_N\succeq c_kI,\quad B_N\succeq b_k^-I.
 \tag{CS6}
\]
AS6 retains every upper-root gap: shells of radius $j$ have at most $8j$ nodes, giving $\prod_{\beta\ne\alpha}|\omega_\alpha-\omega_\beta|\ge(2\delta k)^{q-1}e^{-4q}$. Full Lagrange interpolation gives $B_{{\rm val},k}$. The exact conductor matrix has norm at most $\mathfrak M_k$; the full strip reduction has norm at most $\sqrt qC_{\rm path}^{10k}$. Applying these maps to $W_z-bE_D$ and minimizing over every lower row $b$ proves the first bound of CS6 after projection. Strip interpolation gives the second. In particular
\[
 \log(1/c_k)=2(q-1)\log(q/k)+O_{h,A}(q),\qquad
 \log(1/b_k^-)=O_{h,A}(k\log(q+2)).
 \tag{CS7}
\]
The exact first remainder is $8q+2(q-1)\log((2+kR_h/q)/(2\delta))+2\log\mathfrak M_k+\log(q^2M_\sigma)+20k\log C_{\rm path}$, so CS7 introduces no hidden $q\log k$ term.

For $R\ge1$, let $\mathcal Z_R\subset V_k$ impose all numerator value-and-jet cancellations, through the full multiplicity of each zero of $E_A(w)/w^v$ in $|w|<2R$. Set
\[
 a_0=\log^+(A_1/d_A)/\log2,\quad b_0=4B_A/\log2,\quad
 C_A=\max(A_1,d_A)^2/d_A^3.
\]
AS12–16 proves
\[
 \operatorname{codim}\mathcal Z_R\le a_0+b_0R,\quad
 \max_{|w|\le R}|A_z(w)|\le M_k(R)\|z\|,
 \quad M_k(R)=C_A\sqrt{n_E}e^{(2kR_h+8+4B_A)R},\quad z\in\mathcal Z_R.
 \tag{CS8}
\]
The count uses the full entire function $E_A/w^v$. The quotient estimate divides numerator and denominator by the same radius-$2R$ finite Blaschke product, then applies the maximum principle and the Harnack factor three on $|w|\le R$. Thus it bounds the removable values as well as values away from zeros. No independence of cancellation equations enters. For arbitrary rows, with $\bar B_A=\max(1,B_A)$, the original fixed disk is
\[
 \rho_A=\min\{1,(v+1)!d_A/(2A_1\bar B_A^{v+1}e^{\bar B_A})\},\quad
 M_{0,k}=2\sqrt{n_E}\rho_A^{-v}d_A^{-1}e^{(4+kR_h)\rho_A},
 \quad\max_{|w|\le\rho_A}|A_z(w)|\le M_{0,k}\|z\|.
 \tag{CS9}
\]
The analytic estimates CS6–9 are finite and do not use the monic-profile limit, the DCR asymptotic, or an assigned native determinant coefficient. Their complete proof source accompanies this derivation in the retained programme collection. The later asymptotic ACC/DCR receiver has its separate source status and is unnecessary for the finite rational receiver in CS24 below.

## CS3. Full-source and complete-ideal envelope estimates

Let a finite functional $e$ on $\mathcal P_D$ satisfy $|e(y^n)|\le Hn!R^{-n}$ for $0\le n\le D$. This includes a moment error; it need not itself come from an exponential quotient. Extend its moment sequence by zero above $D$. For $t_R=\min(1/2,R/4)$, the power series gives $|\arctan t|\le\operatorname{arctanh}t_R\le R/2$ on $|t|=t_R$. Therefore
\[
 \left|(1+t^2)^{-1/4}\sum_{n=0}^D\frac{e(y^n)}{n!}(\arctan t)^n\right|
 \le2H(1-t_R^2)^{-1/4}.
\]
Its coefficient through degree $D$ is $e(p_n)/n!$, by CS4. Cauchy's estimate and $\rho_n^2=n!/(1/2)_n\le2n+1$ show
\[
 \|e\|_{\mathcal P_D^*}^2=\sum_{n=0}^D\frac{|e(p_n)|^2}{\gamma_n}
 \le\frac{4H^2}{M_\sigma\sqrt{1-t_R^2}}\sum_{n=0}^D(2n+1)t_R^{-2n}
 \le H^2P_D(R)^2,
\]
\[
 P_D(R)=\frac{2(D+1)t_R^{-D}}{\sqrt{M_\sigma}(1-t_R^2)^{1/4}}.
 \tag{CS10}
\]
The last step uses $t_R\le1$ and $\sum_{n=0}^D(2n+1)=(D+1)^2$. The bound on $\rho_n$ follows inductively since $\rho_{n+1}^2/\rho_n^2=(n+1)/(n+1/2)$ and $(2n+1)(n+1)/(n+1/2)=2n+2\le2n+3$.

Here is the complete ideal estimate, including the original physical norm. The [original Gamma-product TeX, DLMF5.8.3](https://dlmf.nist.gov/5.8.E3), by R. A. Askey and R. Roy, gives
\[
 \sigma(y)\ge\frac{c_\sigma e^{-\pi|y|/2}}{1+4y^2},\qquad c_\sigma=\Gamma(1/4)^2/(2\pi).
\]
Indeed isolate the $n=0$ product factor and bound the remaining logarithmic sum by $\int_0^\infty\log(1+t^2/x^2)dx=\pi|t|$, with $t=y/2$. Differentiating that integral in $|t|>0$ gives $\pi$ and its limit at zero is zero. On $q\le y\le2q$, every lower-root factor has modulus at least $q/2$, by the finite guard. Hence
\[
 \|Q_-p\|_\sigma^2\ge\frac{c_\sigma q e^{-\pi q}}{1+16q^2}(q/2)^{2q'}\|p(q\,\cdot)\|_{L^2[1,2]}^2.
\]
Expanding $p(qx)$ in the orthonormal Legendre polynomials $\sqrt{2n+1}P_n(2x-3)$ gives
$\|\operatorname{coef}p(q\,\cdot)\|_1\le(M+1)10^M\|p(q\,\cdot)\|_2$.
To verify the coefficient bound, the $n$ roots of $P_n(2x-3)$ lie in $(1,2)$ by its orthogonality and the sign-change argument: multiplying its interior sign-change factors would otherwise be a lower-degree polynomial with nonzero integral against it. Its coefficients therefore alternate, so their absolute sum is $P_n(5)$. The integral representation obtained by summing the [original Legendre generating function, DLMF18.12.11](https://dlmf.nist.gov/18.12.E11) gives $P_n(5)\le(5+\sqrt{24})^n\le10^n$. Cauchy–Schwarz and $\sum_{n\le M}(2n+1)=(M+1)^2$ give the stated coefficient bound.

Put $M_{\max}=2q-v-q'$ and
\[
 \mathfrak A_k=(M_{\max}+1)10^{M_{\max}}2^{q'}e^{\pi q/2}
 \sqrt{(1+16q^2)/(c_\sigma q)}.
\]
Then $\sum_j|p_j|q^j\le\mathfrak A_kq^{-q'}\|Q_-p\|_\sigma$. As $n!\le D^n$ for $n\le D$, put $t=D/R$. The weighted absolute coefficient sum of the full root polynomial is at most $(kR_h+t)^{q'}$, and
$\sum|p_j|t^j\le\max(1,t/q)^M\sum|p_j|q^j$. Consequently
\[
 \boxed{\|e|_{I_N}\|\le H\mathfrak A_k
 (kR_h/q+D/(qR))^{q'}\max(1,D/(qR))^{D-q'}.}
 \tag{CS11}
\]
All coefficients of $Q_-$ were included before taking absolute values. This proof applies identically to the original functional and to any finite error sequence with the envelope in CS10.

For $2\le R\le k$, CS8 and CS11 give $\|\ell_z|_{I_N}\|\le\mathfrak F_kR^{-q'}\|z\|$, where
\[
 \mathfrak F_k=\mathfrak A_kC_A\sqrt{n_E}
 e^{2R_hq+(8+4B_A)k}(R_h+2)^{q'}.
\]
For all rows CS9 gives $\|\ell_z|_{I_N}\|\le\mathfrak F_{0,k}\|z\|$, with
\[
 \mathfrak F_{0,k}=\mathfrak A_kM_{0,k}
 (kR_h/q+2/\rho_A)^{q'}(2/\rho_A)^{M_{\max}}.
 \tag{CS12}
\]
Their logarithms are $O_{h,A}(q)$, since the original conductor is fixed, $M_{\max}\le2q$, $q'\le q$, and $k^2\le q$.

## CS4. One complete basis uses the nested cancellation spaces

Set $L_A=b_0+9$, $j_A=\lceil\max\{2(a_0+1),a_0+1+4L_A\}\rceil$, and $R_j=(j-1-a_0)/(2L_A)$ for $j\ge j_A$. Then $R_j\ge2$, $R_j\ge j/(4L_A)$ and $R_j<r/(2L_A)\le(8k-32)/18<k$. Moreover
$\operatorname{codim}\mathcal Z_{R_j}\le a_0+b_0R_j\le(j-1+a_0)/2<j$.
Choose $z_r,z_{r-1},\ldots,z_{j_A}$ successively. At stage $j$, all previously chosen vectors belong to $\mathcal Z_{R_j}$, since its radius is smaller, and their span has dimension $r-j$. The space $\mathcal Z_{R_j}$ has dimension at least $r-j+1$, so its intersection with the orthogonal complement of that span has positive dimension. Select a unit vector there. Complete the early part by any orthonormal basis of the remaining orthogonal complement. If $j_A>r$, simply choose a complete orthonormal basis. This constructs a fixed unitary row map $U$ and retains exactly $r$ rows at every cutoff.

Define $\mathcal R_j=\rho_A$, $\mathcal M_j=M_{0,k}$ for early rows, and $\mathcal R_j=R_j$, $\mathcal M_j=M_k(R_j)$ for late rows. Put
\[
 \mathfrak U_k=\max\{\mathfrak F_k^2(4L_A)^{2q'},\mathfrak F_{0,k}^2j_A^{2q'}\},
 \quad B_j=\sqrt{\mathfrak U_k}\,j^{-q'},\quad F_j=\mathcal M_jP_{2q}(\mathcal R_j).
 \tag{CS13}
\]
CS10–12 prove $\|\ell_{z_j}|_{I_N}\|\le B_j$ and $\|\ell_{z_j}\|_{\mathcal P_D^*}\le F_j$. They also prove the same bounds multiplied by $\varepsilon$ for every error sequence whose Taylor coefficients obey $|e_n|\le\varepsilon\mathcal M_j\mathcal R_j^{-n}$. This last assertion uses the finite envelope proof, not an assumption that an aliased sequence has the same pole cancellations. Uniformly in $j$, $\log^+F_j=O(q)$: late radii satisfy $kR_j\le k^2$, and early radii are fixed positive numbers. Since $C_N\succeq c_kI$, each unit row has ideal norm at least $\sqrt{c_k}$, so $B_j/\sqrt{c_k}\ge1$; similarly $F_j/\sqrt{b_k^-}\ge1$.

## CS5. Exact aliasing and an arbitrary-accuracy sample count

Fix $0<\eta\le1/8$ and set $a_j=\mathcal R_j/2$. For $T_j>2q$ sample the exact removable function $A_{z_j}$ at $a_j\exp(2\pi i\ell/T_j)$, $0\le\ell<T_j$. The Fourier coefficient estimate through degree $2q$ is
\[
 a^{[T]}_{j,n}=\frac{a_j^{-n}}{T_j}\sum_{\ell=0}^{T_j-1}A_{z_j}(a_je^{2\pi i\ell/T_j})e^{-2\pi in\ell/T_j}.
\]
The Taylor series converges absolutely at these points, since it is holomorphic on a neighborhood of the closed radius-$\mathcal R_j$ disk. Interchanging its sum with the finite Fourier sum gives, for $0\le n<T_j$,
\[
 a^{[T]}_{j,n}-[w^n]A_{z_j}
 =\sum_{h\ge1}[w^{n+hT_j}]A_{z_j}\,a_j^{hT_j},
 \quad |a^{[T]}_{j,n}-[w^n]A_{z_j}|
 \le\frac{\mathcal M_j\mathcal R_j^{-n}}{2^{T_j}-1}.
 \tag{CS14}
\]
The physical moments are $(-i)^nn!a^{[T]}_{j,n}$. Applying the finite-envelope bounds CS10–13 gives ideal row error $B_j/(2^{T_j}-1)$ and full-source row error $F_j/(2^{T_j}-1)$ before any Gram is formed.

Choose
\[
 \boxed{T_j(\eta)=\max\left\{2q+1,\left\lceil\log_2\left[\frac{4\sqrt r}{\eta}\max\left(\frac{B_j}{\sqrt{c_k}},\frac{F_j}{\sqrt{b_k^-}}\right)\right]\right\rceil\right\}.}
 \tag{CS15}
\]
Let $A_j$ denote the maximum in this formula; $A_j\ge1$. Then
\[
 \frac{B_j}{2^{T_j}-1}\le\frac{\eta\sqrt{c_k}}{(4-\eta)\sqrt r},\qquad
 \frac{F_j}{2^{T_j}-1}\le\frac{\eta\sqrt{b_k^-}}{(4-\eta)\sqrt r}.
\]
Permit an additional numerical row error at most $\eta\sqrt{c_k}/(2\sqrt r)$ on the ideal and $\eta\sqrt{b_k^-}/(2\sqrt r)$ on the full source. The Frobenius bound, namely the square root of the sum of squared row norms, bounds each operator error. Since $1/(4-\eta)+1/2<1$ on the stated range, the resulting map errors are strictly less than $\eta\sqrt{c_k}$ and $\eta\sqrt{b_k^-}$ respectively, simultaneously for all $N$.

Scalar sample errors can meet both budgets. A value error of modulus at most $\epsilon_j$ at every sample gives coefficient error at most $\epsilon_ja_j^{-n}$ by the finite Fourier sum. Define
\[
 D_j^I=\mathfrak A_k(kR_h/q+2/a_j)^{q'}\max(1,2/a_j)^{M_{\max}}.
\]
Then the sufficient input enclosure is
\[
 \boxed{\epsilon_j\le\frac{\eta}{2\sqrt r}
 \min\left\{\frac{\sqrt{c_k}}{D_j^I},\frac{\sqrt{b_k^-}}{P_{2q}(a_j)}\right\}.}
 \tag{CS16}
\]
The bounds include all Taylor coefficients, the factorials and the derivative phases. Errors in the actual row coefficients, physical period and removable quotient must be included in these enclosures. At a true canceled zero a raw rounded quotient is not the target value: one evaluates the holomorphic quotient using its exact cancellation identity and enclosed derivatives. An approximate cancellation equation alone is not a proof that a larger circle is admissible. Construction and certification of the actual cancellation flag are the stated input model of the sample-count theorem.

Put
\[
 H_k(\eta)=\max\left\{0,\log\frac{4\sqrt{r\mathfrak U_k}}{\eta r^{q'}\sqrt{c_k}},
 \max_j\log\frac{4\sqrt rF_j}{\eta\sqrt{b_k^-}}\right\}.
\]
Then $\log(4\sqrt rA_j/\eta)\le H_k(\eta)+q'\log(r/j)$, so
\[
 \boxed{\sum_{j=1}^rT_j(\eta)
 \le r(2q+2)+\frac{rH_k(\eta)+q'[r\log r-\log(r!)]}{\log2}
 \le r\left(2q+2+\frac{H_k(\eta)+q'}{\log2}\right).}
 \tag{CS17}
\]
The first inequality uses $\max(a,b)\le a+b$ for nonnegative $a,b$ and the ceiling bound. For the second, $\log(r!)=\sum_{j=1}^r\log j\ge\int_1^r\log x\,dx=r\log r-r+1$.

Here is the exact cancellation needed to estimate $H_k$, rather than an extra logarithm charged to every row. The terms $\tfrac12\log\mathfrak U_k$ and all full-source terms are $O(q)$. By CS7 the remaining term is
\[
 (q-1)\log(q/k)-q'\log r
 =(q-1-q')\log k+(q-1)\log(q/k^2)-q'\log(r/k).
\]
The first is $O(k\log k)$ because $q-1-q'=16k-49$; the second is $O(k)$ because $q/k^2=(1+1/k)^2$; and the last is $O(q)$ because $r/k$ is bounded above and below by positive constants for the stated fixed-conductor domain. Consequently
\[
 H_k(\eta)=O_{h,A}(q)+\log(1/\eta),\qquad
 \boxed{\sum_jT_j(\eta)=O_{h,A}(kq+k\log(1/\eta)).}
 \tag{CS18}
\]
For fixed accuracy this is the asserted $O(kq)$ total scalar count. Individual early rows may require $O(q\log q)$ samples. The same coefficients through degree $2q$ supply all four original cutoffs, and in fact the whole intervening window. CS18 is a count of scalar row-function evaluations, not of zero isolation, exact rank decisions, bit operations, or matrix inversion.

## CS6. Errors before Grams, with the exact complete ideal

Let $H_D$ be the original Gamma Gram on $1,y,\ldots,y^D$, and let $L_N$ be the moment row matrix, with entries $(-i)^nn![w^n]A_{z_j}$. Let $J_N:\mathbb C^{M+1}\hookrightarrow\mathbb C^{D+1}$ contain every coefficient column of multiplication by the complete monic $Q_-$. Then
\[
 B_N=L_NH_D^{-1}L_N^*,\qquad
 C_N=(L_NJ_N)(J_N^*H_DJ_N)^{-1}(L_NJ_N)^*.
 \tag{CS19}
\]
To verify equality with CS5, put $T=H_D^{1/2}J_N(J_N^*H_DJ_N)^{-1/2}$. Its columns are orthonormal and span the full ideal in source orthonormal coordinates; hence $TT^*$ is precisely $P_N$ in those coordinates. The map $L_NH_D^{-1/2}$ is the full original functional matrix. Substitution proves CS19. The physical $S'$ frame includes the factor $i^{q'}$ in $J_N$ and its corresponding coefficient transform; both numerator and denominator of CS19 carry that same factor, so it cancels there exactly. No lower-root row has been removed.

For either full or ideal map write its original covariance as $X=KK^*\succeq xI$. If $\|\widehat K-K\|\le\eta\sqrt x$, then for every row-space vector $u$,
$\|\widehat K^*u-K^*u\|\le\eta\|K^*u\|$. Both triangle inequalities, followed by squaring, give
$(1-\eta)^2X\preceq\widehat K\widehat K^*\preceq(1+\eta)^2X$.
This compares the maps before forming Grams and therefore does not multiply the error by the largest singular value of $K$.

If $(1-\tau)H_D\preceq\widehat H_D\preceq(1+\tau)H_D$, $0\le\tau<1$, the same inequalities hold after congruence by the complete $J_N$, and inverse order gives
\[
 \boxed{\alpha X_N\preceq\widehat X_N\preceq\beta X_N\quad(X=C,B),\qquad
 \alpha=\frac{(1-\eta)^2}{1+\tau},\quad\beta=\frac{(1+\eta)^2}{1-\tau}.}
 \tag{CS20}
\]
For the received choices $\eta=1/32$, $\tau=1/16$, the stronger exact interval is
$\alpha=961/1088$, $\beta=1089/960$, inside $[3/4,5/4]$. This gives the same received conclusion with a smaller finite determinant error. The original Gamma moment matrix can be represented as $H_D=M_\sigma[\nu_{i+j}]$, where $\nu_j=j![t^j](\cos t)^{-1/2}\in\mathbb Q$. Thus exact rational moment arithmetic and a scalar enclosure of the physical mass alone provide the source-form enclosure; entrywise rounding of an ill-conditioned moment matrix is unnecessary. This representation retains $M_\sigma$ explicitly.
To prove the moment formula, integrate CS4 coefficient by coefficient: orthogonality makes the integral of $p_n$ zero for $n>0$. Substitute $t=\tan u$ into that formal identity to obtain $\sum_{n\ge0}u^n\int y^n\,d\sigma/n!=M_\sigma(\cos u)^{-1/2}$. Each coefficient uses finitely many moments, so this argument requires no interchange of an infinite integral and an analytic series.

## CS7. A certificate when every lower-root coefficient is enclosed

The preceding received formula uses the exact matrix $J_N$. Here is an explicit extension for an approximated full multiplication matrix $\widehat J_N$, with no omitted root. Write $G=J_N^*H_DJ_N>0$, $\Delta J=\widehat J_N-J_N$, and
\[
 \delta_N=\|H_D^{1/2}\Delta JG^{-1/2}\|<1,\qquad
 F_*=\left(\sum_{j=1}^rF_j^2\right)^{1/2},\qquad
 d_N=\frac{(F_*+\eta\sqrt{b_k^-})\delta_N}{\sqrt{c_k}}.
\]
The moment matrix $\widehat L_N$ has the sampled map-error bounds proved above. Set
$T=H_D^{1/2}J_NG^{-1/2}$, $\widehat T=H_D^{1/2}\widehat J_NG^{-1/2}$, so $T^*T=I$ and $\|\widehat T-T\|=\delta_N$. Both triangle inequalities give
$(1-\delta_N)^2I\preceq\widehat T^*\widehat T\preceq(1+\delta_N)^2I$.
Also
\[
 \|\widehat L_N\widehat J_NG^{-1/2}-L_NJ_NG^{-1/2}\|
 \le\eta\sqrt{c_k}+(F_*+\eta\sqrt{b_k^-})\delta_N
 =(\eta+d_N)\sqrt{c_k}.
\]
The first term is the error on the exact ideal. The second uses the entire full-source map bound $\|\widehat L_NH_D^{-1/2}\|\le F_*+\eta\sqrt{b_k^-}$. Thus no unprojected norm is incorrectly substituted for the small ideal lower bound. Combining these two comparisons with the source error $\tau$ proves
\[
 \boxed{\frac{(1-\eta-d_N)^2}{(1+\tau)(1+\delta_N)^2}C_N
 \preceq
 (\widehat L_N\widehat J_N)(\widehat J_N^*\widehat H_D\widehat J_N)^{-1}(\widehat L_N\widehat J_N)^*
 \preceq\frac{(1+\eta+d_N)^2}{(1-\tau)(1-\delta_N)^2}C_N,}
 \tag{CS21}
\]
where $\eta+d_N<1$. In detail, express both the numerator and denominator in the fixed coefficient frame $G^{-1/2}$, apply CS20's vector comparison to the numerator, and inverse order to the denominator. There is no comparison of independently chosen square-root gauges. The middle matrix uses the complete polynomial with enclosed coefficients and approximates the exact original ideal by this displayed estimate; it is not asserted to equal that ideal's projection before the error is paid.

Every quantity in this condition has a finite coefficient enclosure. For example, choose certified $h_+\ge\lambda_{\max}(H_D)$ and $g_-\le\lambda_{\min}(G)$, both positive. Then
\[
 \delta_N\le\sqrt{h_+/g_-}\,\|\Delta J\|_F
 \le\sqrt{h_+/g_-}\sqrt{M+1}\,\|\operatorname{coef}(\widehat Q_--Q_-)\|_2.
 \tag{CS22}
\]
The second inequality follows because every column of $\Delta J$ is a shift of the full coefficient error vector. Bounds $h_+=\operatorname{tr}H_D$ and $g_-=\det G/(\operatorname{tr}G)^M$ are valid: the product of the other $M$ positive eigenvalues is at most $(\operatorname{tr}G)^M$. Certified bounds on the positive trace and determinant give numerical versions, or interval elimination gives sharper ones. Positivity is proved independently from the injectivity of multiplication by the monic $Q_-$, so sufficient refinement of enclosures yields a positive margin.

If each of the $q'$ original roots is enclosed to error at most $\epsilon_\omega$, and all exact roots have modulus at most $R_-= (k-8)R_h$, telescoping the two full products gives
\[
 \|\operatorname{coef}(\widehat Q_--Q_-)\|_1
 \le q'\epsilon_\omega(1+R_-+\epsilon_\omega)^{q'-1}.
\]
Indeed replace the factors one at a time; the changed factor is a constant of modulus at most $\epsilon_\omega$, and coefficient $\ell^1$ norms are submultiplicative. This estimate preserves the degree, original number of factors and monic leading coefficient. It requires neither root deletion nor a favorable rank decision.

A concrete common budget is
\[
 \eta=1/64,\quad\tau\le1/16,\quad
 \delta_N\le\min\left\{\frac1{64},\frac{\sqrt{c_k}}{64(F_*+\sqrt{b_k^-}/64)}\right\}
 \quad\hbox{for every cutoff}.
 \tag{CS23}
\]
Then $d_N\le1/64$. Formula CS21 gives the explicit common interval
$\alpha_J=(31/32)^2/[(17/16)(65/64)^2]$,
$\beta_J=(33/32)^2/[(15/16)(63/64)^2]$.
Direct rational comparison shows $\alpha_J>3/4+1/32$ and $\beta_J<5/4-1/32$. Consequently one may additionally allow final absolute arithmetic error at most $c_k/32$ in the computed ideal covariance and still retain $3C_N/4\preceq\widehat C_N\preceq5C_N/4$. The full covariance has the stronger CS20 interval with $\eta=1/64$, and similarly permits output error $b_k^-/32$. Alternatively compute the finite products and inverses exactly on Gaussian-rational centers. The extra input coefficient precision in CS22 is displayed explicitly; CS18 does not claim to bound its bit cost.

## CS8. Original determinant consequence and source transport

Suppose $\alpha C_N\preceq\widehat C_N\preceq\beta C_N$ at all four cutoffs, with fixed $0<\alpha\le\beta$. Every log determinant error lies in $[r\log\alpha,r\log\beta]$. Two signs are positive and two negative, so
\[
 |\mathcal R\log\det\widehat C_N-\mathcal R\log\det C_N|
 \le2r\log(\beta/\alpha).
\]
Write $\mathcal Rf_N=f_{q-1}+f_q-f_{2q-1}-f_{2q}$. The [complete finite invariant-determinant proof, equations (2), (3), (12), (13) and FI1–4 of edition018](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/75256b0237884bdef0074c2ac6310de1ea32ec26/workbenches/splitzero-tandem/continuations/20260921-invariant-collision/FINITE_INVARIANT_PROOFS.md), therefore gives
\[
 \boxed{\left|\mathcal K_k-\log\mathcal A_{k,v}-\mathcal R\log\det\widehat C_N\right|
 \le\mathcal E_k+2r\log(\beta/\alpha).}
 \tag{CS24}
\]
Here $\mathcal K_k=\mathcal R\log\det(I_K^*G_NI_K)$ is the original arithmetic kernel, $\mathcal A_{k,v}$ is the exact positive rational Hankel-determinant factor, and $\mathcal E_k$ is the complete physical comparison error with the same-source NG2 width and all original low, angle and exterior terms. All its finite guards remain. This receiver uses neither a monic-profile asymptotic nor the ACC/DCR replacement by $gqC_\partial$. In particular $[3/4,5/4]$ gives only $2r\log(5/3)$ additional error in CS24; the sharper intervals of CS20–21 give their smaller corresponding constants. Fixed row congruences cancel in this four-sign expression because the same frame is used throughout.

If instead one uses the already proved ACC/DCR two-endpoint angle receiver, both $C$ and $B$ satisfy the same interval and the additional error in $2\log(\det C_L\det B_H/(\det C_H\det B_L))$ is at most $4r\log(\beta/\alpha)$. Its analytic-profile status remains exactly that of the inherited receiver. This sampling argument does not establish that asymptotic or assign its unknown native coefficient.

For completeness, an actual proved full-source comparison $aH^\sigma\preceq H^\mu\preceq bH^\sigma$ on the same polynomial space transports every complete restriction and inverse by order. Thus the sampling constants become $c^\mu=c^\sigma/b$, $(b_- )^\mu=(b_- )^\sigma/b$, $B_j^\mu=B_j^\sigma/\sqrt a$, $F_j^\mu=F_j^\sigma/\sqrt a$. Their row thresholds increase by $\log(b/a)/(2\log2)$ before integer ceilings. This is a direct statement about the same maps and full forms; it supplies no comparison for an unrelated source. The stronger original NG2 same-source width, where applicable, is $O_h(k+\log(q+2))$. All individual physical masses stay in the constants.

The strengthened results are therefore the complete original-row certificate CS15–20 with arbitrary prescribed accuracy, the explicit full-root coefficient perturbation bounds CS21–23, and the finite original-kernel receiver CS24. Their exact checks concern finite declared auxiliary data. The native original period-dependent determinant sequence remains unevaluated.
