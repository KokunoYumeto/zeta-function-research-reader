# Every original projection-angle direction

Independent derivation, 21 September 2026. The supplied arrival is checked below with its actual coefficient rows, source measures, physical coordinates and full lower-root projection. The arithmetic endpoint statistic at order kq is not assigned a value. The statements do not close the Riemann hypothesis.

## AS1. Original objects and finite domain

Fix the original simple quartet, conductor and period. Let
\[
k\equiv1\pmod4,\quad k\ge17,\quad q=(k+1)^2,\quad
k'=k-8,\quad q'=(k-7)^2,\quad 0<\delta<1/2,\quad\gamma>2,
\quad R_h=\sqrt{\delta^2+\gamma^2}.
\]
The estimates using the interval [q,2q] require the explicit guard
\(q\ge2kR_h\). Everything holds eventually for fixed original data.
The original exponents and centers are
\[
c=k/2,\quad c'=k/2-4,\quad
\beta_{ab}=c+(2a-k)\delta+i(2b-k)\gamma,
\quad\omega_{ab}=(\beta_{ab}-c)/i,
\]
\[
\beta'_{ab}=c'+(2a-k')\delta+i(2b-k')\gamma,
\quad\omega'_{ab}=(\beta'_{ab}-c')/i.
\]
Thus \(\omega_{ab}=(2b-k)\gamma-i(2a-k)\delta\), and the same formula with k' gives every lower root. Put
\[
E_A(w)=\sum_{r,s=0}^8a_{rs}e^{b_{rs}w},\quad
b_{rs}=4+(2r-8)\delta+i(2s-8)\gamma,
\quad A_1=\sum|a_{rs}|,
\]
\[
v=\operatorname{ord}_0E_A\le80,\quad
\mu_v=E_A^{(v)}(0)\ne0,\quad d_A=|\mu_v|/v!,\quad
B_A=\max_{a_{rs}\ne0}|b_{rs}|.
\]
The bound v≤80 follows because the at most 81 distinct exponents have invertible Vandermonde moment matrix: 81 vanishing initial moments force all coefficients to be zero. The actual conductor is nonzero.

The original invariant rows after the entire low-polynomial constraint form a fixed space \(V_k\), with full row frame Z and coefficient form
\[
R_Z=ZZ^*>0,\quad r=r_k=8k-32-v+s_k,\quad
s_k=\dim(K_k\cap\mathcal P_{<v}),\quad0\le s_k\le v.
\]
They are supported on the actual conductor strip, whose cardinality is
\(n_E=q-q'=16k-48\). At k≥17 one has r≥24, while r≤8k−32. The particular row frame is never replaced by arbitrary exponential rows. Coordinate comparison with \(R_Z\) is a congruence on that same space. The measure is unchanged.

For each original row z put
\[
F_z(w)=\sum_\alpha z_\alpha e^{\beta_\alpha w},\quad
G_z(w)=F_z(w)/E_A(w),\quad A_z(w)=e^{-c'w}G_z(w).
\tag{AS1}
\]
All derivatives of \(F_z\) of orders below v vanish at zero, so both quotients are holomorphic there. The exact physical functional is
\[
\ell_z[f]=[f(-i\partial_w)A_z(w)]_{w=0}
=[f((\partial_w-c')/i)G_z(w)]_{w=0}.
\tag{AS2}
\]
Indeed \(\partial_w^n(e^{-c'w}G)=e^{-c'w}(\partial_w-c')^nG\), by induction, and \(e^{-c'w}=1\) at zero. Both c' and −i remain.

For every integer q−1≤N≤2q put D=N−v and M=D−q'. The full lower ideal in physical coordinates is
\[
Q_-(y)=i^{-q'}\chi'(c'+iy)=\prod_{a,b=0}^{k'}(y-\omega'_{ab}),
\qquad I_N=Q_-\mathbb C[y]_{\le M}\subset\mathbb C[y]_{\le D}.
\tag{AS3}
\]
Multiplication by \(i^{q'}\) is of modulus one; no norm factor is suppressed. Retain
\[
d\sigma(y)=\frac{|\Gamma(1/4+iy/2)|^2}{2\pi}\,dy,
\quad M_\sigma=\sqrt{2\pi},
\quad p_{n+1}=yp_n-n(n-1/2)p_{n-1},
\quad\gamma_n=M_\sigma n!(1/2)_n.
\]
The frame \(p_n/\sqrt{\gamma_n}\) is the original orthonormal frame. With
\((E_D)_{\alpha n}=p_n(\omega'_\alpha)/\sqrt{\gamma_n}\), full-root Lagrange interpolation gives \(\operatorname{rank}E_D=q'\), since D≥q'−1. A polynomial vanishes at all lower roots precisely when it is divisible by Q_-. Hence
\[
P_N=I-E_D^*(E_DE_D^*)^{-1}E_D
\tag{AS4}
\]
is the orthogonal projection onto the complete \(I_N\). This follows also by multiplying the matrix: it is self-adjoint, idempotent, kills \(\operatorname{im}E_D^*\), and is identity on \(\ker E_D\).

Let \(W_N\) be the matrix of all these functionals on the orthonormal frame. Define
\[
C_N=W_NP_NW_N^*,\quad B_N=W_NW_N^*,\quad
S_N=B_N^{-1/2}C_NB_N^{-1/2},\quad
C_N^\circ=R_Z^{-1/2}C_NR_Z^{-1/2},\quad
B_N^\circ=R_Z^{-1/2}B_NR_Z^{-1/2}.
\tag{AS5}
\]
The original map is \(\mathcal P_N=P_NT_N\), where
\(T_N=W_N^*B_N^{-1/2}:\mathbb C^r\to\mathcal P'_D\).
Then \(T_N^*T_N=I\) and \(\mathcal P_N^*\mathcal P_N=S_N\). Its injectivity will follow quantitatively from AS10 below; in particular \(0<S_N\le I\).

## AS2. All upper roots improve the projected lower bound

For fixed upper lattice point α, set
\(r_{\alpha\beta}=\max(|a_\alpha-a_\beta|,|b_\alpha-b_\beta|)\).
The exact rectangular coordinates give
\[
|\omega_\alpha-\omega_\beta|^2
=4\gamma^2(b_\alpha-b_\beta)^2+4\delta^2(a_\alpha-a_\beta)^2
\ge4\delta^2r_{\alpha\beta}^2.
\]
The shell r=j contains at most 8j lattice points; truncating it at the box boundary can only decrease this count. Because log t≤t−1 for t>0,
\[
\sum_{\beta\ne\alpha}\log(k/r_{\alpha\beta})
\le\sum_{j=1}^k8j\log(k/j)
\le8\sum_{j=1}^k(k-j)=4k(k-1)\le4q.
\]
Exponentiating proves, without dropping any root,
\[
\prod_{\beta\ne\alpha}|\omega_\alpha-\omega_\beta|
\ge(2\delta k)^{q-1}e^{-4q}.
\tag{AS6}
\]

In the orthonormal Gamma recurrence, multiplication by y has upper and lower shift weights √((n+1)(n+1/2)) and √(n(n−1/2)). Each is at most D+1 on degree≤D. The triangle inequality gives
\[
\|(y-z)p\|_\sigma\le[2(D+1)+|z|]\|p\|_\sigma.
\tag{AS7}
\]
Apply this successively to all q−1 factors of the Lagrange numerator. Every root has modulus≤\(kR_h\). The squared operator norm of the full interpolation map from root values to polynomials is at most the sum of its q squared column norms, thus at most
\[
B_{\mathrm{val},k}=qM_\sigma e^{8q}
\left(\frac{2q+kR_h}{2\delta k}\right)^{2(q-1)}.
\tag{AS8}
\]
Consequently every full upper-root row h has Gamma functional norm at least \(B_{\mathrm{val},k}^{-1/2}\|h\|_2\): compose its evaluation row with this exact interpolation right inverse.

We also require a forward bound for the original conductor matrix \(A_{D,1}\). Let
\[
\mathfrak M_k=\max\{1,e^{1+2\pi\gamma}A_1
(8q+1)^{1/4}(2q+1)(4q+1)^{4\delta}\}.
\tag{AS9}
\]
Here is a direct verification including v. Put \(w(t)=-i\arctan t\) and
\(g(t)=t^{-v}e^{-4w(t)}E_A(w(t))\). For m=j+v≥1 choose radius m/(m+1). The right-half-plane logarithm of (1−it)/(1+it) gives
\(|e^{(b_{rs}-4)w(t)}|\le e^{2\pi\gamma}(2m+1)^{4\delta}\).
Cauchy's coefficient estimate applied to \(t^vg(t)\) gives
\(|g_j|\le e^{1+2\pi\gamma}A_1[2(j+v)+1]^{4\delta}\).
For m=0, \(g_0=E_A(0)\), and the same inequality holds directly.
The exact WCF matrix is \((A_{D,1})_{ij}=g_{j-i}\rho_{j+v}/\rho_i\) for i≤j, with \(\rho_n^2=n!/(1/2)_n\). All \(\rho_i\ge1\). Induction proves \(\rho_n^4\le4n+1\): the needed one-step difference is
\((4n+5)(n+1/2)^2-(4n+1)(n+1)^2=1/4\).
Thus every nonzero entry is bounded by the product in AS9 without the factor 2q+1. There are at most D+1≤2q+1 entries in each row and column. The inequality \(\|A\|_2^2\le\|A\|_1\|A\|_\infty\), obtained by weighted Cauchy–Schwarz, proves \(\|A_{D,1}\|\le\mathfrak M_k\).

Let \(a_*\) be the actual nonzero lexicographic conductor pivot and \(C_{\mathrm{path}}=A_1/|a_*|\ge1\). Original elimination replaces the pivot \((r_0+i,s_0+j)\) by all other terms \(-a_{rs}/a_*\) at (r+i,s+j). Height 9a+b strictly decreases: when \(r<r_0\) the decrease is at least 9−8=1, and when \(r=r_0\) it is \(s_0-s\ge1\). Heights range from 0 to 10k. A substitution path therefore has length≤10k. The sum of absolute outgoing edge weights is \(C_{\mathrm{path}}-1\), so the sum of terminal-path weights is at most
\(\sum_{j=0}^{10k}(C_{\rm path}-1)^j\le C_{\rm path}^{10k}\).
Consequently the exact strip map has
\(\|N_k\|_2\le\sqrt qC_{\rm path}^{10k}\), \(N_kz=z\) on the strip and \(N_kM_A=0\) on the full conductor image. It follows that
\(\operatorname{dist}(z,\operatorname{im}M_A)\ge\|z\|/(\sqrt qC_{\rm path}^{10k})\).

To transfer this distance through the actual projection, for any lower evaluation row \(bE_D\) use the exact duality \(F_z=E_AG_z\). Multiplication by the original \(A_{D,1}\) sends \(W_z-bE_D\) to the full upper Gamma functional row of \(z-M_Ab\), with its first v identically zero entries removed. The equality of exponent coordinates is
\(\beta'_{ij}+b_{rs}=\beta_{i+r,j+s}\), so this is the entire original conductor image. The zero entries do not change the norm. AS8, AS9 and the strip-distance estimate give
\[
\inf_b\|W_z-bE_D\|^2
\ge c_k\|z\|^2,\qquad
c_k=[\mathfrak M_k^2B_{\mathrm{val},k}qC_{\rm path}^{20k}]^{-1}.
\tag{AS10}
\]
The infimum is exactly \(\|W_zP_N\|^2\), by AS4. Hence \(C_N^\circ\succeq c_kI\). This proves injectivity with the full projection retained.

The exact useful logarithmic expansion is
\[
\log(1/c_k)=2(q-1)\log(q/k)+8q
+2(q-1)\log\frac{2+kR_h/q}{2\delta}
+2\log\mathfrak M_k+\log(q^2M_\sigma)+20k\log C_{\rm path}.
\tag{AS11}
\]
All terms after the first are O(q) for fixed original data. In particular no q log k loss has been inserted in the remainder.

## AS3. Cancellation of the actual conductor zeros

To avoid a collision between two meanings of \(b_A\), write
\(b(w)=E_A(w)/w^v\), \(a_0=\log^+(A_1/d_A)/\log2\),
\(b_0=4B_A/\log2\). The function b is entire and \(|b(0)|=d_A\).
For R≥1, Jensen's formula at radius 4R gives
\[
n_A(2R)\le a_0+b_0R,
\tag{AS12}
\]
where \(n_A\) counts zeros of b in the open disk |w|<2R with multiplicity. To see this without a boundary assumption, factor the finitely many interior zeros of b and apply the mean-value identity to the logarithm of the zero-free quotient on radii approaching 4R. Each zero of modulus<2R contributes more than log2. On |w|=4R,
\(|b(w)|\le A_1(4R)^{-v}e^{4B_AR}\le A_1e^{4B_AR}\).
The resulting bound is \((\log(A_1/d_A)+4B_AR)/\log2\); replacing the first logarithm by its positive part proves AS12. Zeros exactly on either count boundary cause no failure of the bound.

Define the actual row subspace
\[
\mathcal Z_R=\{z\in V_k:F_z^{(j)}(\zeta)=0
\text{ for every }b(\zeta)=0,\ |\zeta|<2R,\ 0\le j<\operatorname{ord}_\zeta b\}.
\tag{AS13}
\]
These are linear value-and-jet equations on the same rows Z. Their rank is their true codimension, which is at most \(n_A\)(2R); independence is unnecessary.

Take the finite radius-2R Blaschke product
\(\mathcal B_R(w)=\prod_\zeta [2R(w-\zeta)/((2R)^2-\bar\zeta w)]^{m_\zeta}\).
There is no zero at zero because b(0)≠0. Both \(b/\mathcal B_R\) and
\(e^{-c'w}F_z(w)/(w^v\mathcal B_R(w))\) extend holomorphically across the canceled zeros; the first has no zero in the open disk. All factor poles lie strictly outside the closed disk, and \(|\mathcal B_R|=1\) on its boundary. Put
\(M_R^b=\max(A_1,d_A)e^{2B_AR}\).
The maximum principle gives \(|b/\mathcal B_R|\le M_R^b\), and
\(|(b/\mathcal B_R)(0)|\ge d_A\). The nonnegative harmonic function
\(u=\log(M_R^b/|b/\mathcal B_R|)\) satisfies
\(u(w)\le3u(0)\) for |w|≤R. This follows from the Poisson kernel on any intermediate circle, whose maximum is (s+|w|)/(s−|w|), followed by s↑2R. Thus boundary zeros of b do not require cancellation. Rearranging gives
\(|b/\mathcal B_R|\ge d_A^3/(M_R^b)^2\).

On |w|=2R, each centered exponent \(\beta_\alpha-c'\) has modulus≤4+\(kR_h\). Since \((2R)^{-v}\le1\) and z is supported on \(n_E\) positions,
\[
|e^{-c'w}F_z(w)/w^v|
\le\sqrt{n_E}e^{2(4+kR_h)R}\|z\|.
\]
The maximum principle for the numerator divided by \(\mathcal B_R\) and the last denominator bound prove
\[
\max_{|w|\le R}|A_z(w)|
\le C_A\sqrt{n_E}e^{(2kR_h+8+4B_A)R}\|z\|,
\quad C_A=\max(A_1,d_A)^2/d_A^3,
\quad z\in\mathcal Z_R.
\tag{AS14}
\]

For uncanceled rows use \(\bar B_A=\max(1,B_A)\) and
\[
\rho_A=\min\left\{1,
\frac{(v+1)!d_A}{2A_1\bar B_A^{v+1}e^{\bar B_A}}\right\}.
\tag{AS15}
\]
For |w|≤1 the exponential series bounds
\[
|b(w)-b(0)|\le
\frac{A_1\bar B_A^{v+1}}{(v+1)!}|w|e^{\bar B_A|w|}.
\]
Indeed \((v+1+j)!\ge(v+1)!j!\); sum the remainder series after dividing by \(w^v\). Therefore \(|b|\ge d_A/2\) on this disk. Bound the centered numerator on its boundary and use its removable value at zero. The maximum principle proves
\[
\max_{|w|\le\rho_A}|A_z(w)|\le M_{0,k}\|z\|,
\quad M_{0,k}=2\sqrt{n_E}\rho_A^{-v}d_A^{-1}
e^{(4+kR_h)\rho_A}.
\tag{AS16}
\]
No first symbol coefficient has been set equal to one.

## AS4. The full Gamma ideal norm controls every derivative

The original Gamma product at a=1/4 and t=y/2 yields
\[
\frac{|\Gamma(a+it)|^2}{\Gamma(a)^2}
=\prod_{n\ge0}(1+t^2/(n+a)^2)^{-1}.
\]
For the decreasing nonnegative function f(x)=log(1+t²/x²),
\(\sum_{n\ge1}f(n+a)\le\int_a^\infty f(x)dx\le\int_0^\infty f(x)dx=\pi|t|\).
The integral follows by differentiating in |t|>0, obtaining π, and taking its zero limit; equivalently integrate by parts after x=|t|u. Keeping the n=0 factor proves
\[
\sigma(y)\ge c_\sigma e^{-\pi|y|/2}/(1+4y^2),
\qquad c_\sigma=\Gamma(1/4)^2/(2\pi).
\tag{AS17}
\]
Every lower root has modulus≤\(kR_h\)≤q/2. Thus on q≤y≤2q,
\(|Q_-(y)|\ge(q/2)^{q'}\), and the full-line norm has the lower bound
\[
\|Q_-p\|_\sigma^2\ge
\frac{c_\sigma q e^{-\pi q}}{1+16q^2}(q/2)^{2q'}
\|p(q\,\cdot)\|_{L^2[1,2]}^2.
\tag{AS18}
\]
The interval gives an inequality for the original full measure; it does not define a replacement measure.

Here are details of the coefficient estimate. Rodrigues' formula gives the orthonormal polynomials \(\sqrt{2n+1}P_n(2x-3)\) on [1,2]. Orthogonality implies all their n roots lie in (1,2): otherwise the product of factors at sign-changing roots there, of degree<n, has product with the polynomial of one nonzero sign, contrary to orthogonality. The leading coefficient is positive, so the coefficients alternate and their absolute sum is
\(\sqrt{2n+1}P_n(5)\). The integral
\(P_n(x)=\pi^{-1}\int_0^\pi(x+\sqrt{x^2-1}\cos\theta)^n d\theta\) for x≥1 follows by summing the geometric series inside the integral and obtaining \((1-2xt+t^2)^{-1/2}\), the read original Legendre generating function. Hence \(P_n(5)\le(5+\sqrt{24})^n\le10^n\). If \(p(qx)=\sum d_n\sqrt{2n+1}P_n(2x-3)\), the triangle inequality and Cauchy–Schwarz give
\[
\|\operatorname{coef}p(q\,\cdot)\|_1
\le\Big(\sum_{n=0}^M(2n+1)100^n\Big)^{1/2}\|p(q\,\cdot)\|_2
\le(M+1)10^M\|p(q\,\cdot)\|_2.
\]
Writing \(M_{\max}=2q-v-q'\), define
\[
\mathfrak A_k=(M_{\max}+1)10^{M_{\max}}2^{q'}e^{\pi q/2}
\sqrt{(1+16q^2)/(c_\sigma q)}.
\tag{AS19}
\]
Combining with AS18 proves
\[
\|\operatorname{coef}p(q\,\cdot)\|_1
\le\mathfrak A_kq^{-q'}\|Q_-p\|_\sigma.
\tag{AS20}
\]

Suppose \(\max_{|w|\le R}|A_z(w)|\le H_R\|z\|\). Cauchy's estimate applied to AS2 gives
\(|\ell_z[y^n]|\le H_R\|z\|n!R^{-n}\le H_R\|z\|(D/R)^n\) for n≤D. Put t=D/R. The full coefficient sum of Q_- is at most \((kR_h+t)^{q'}\). For \(p(y)=\sum p_jy^j\),
\(\sum|p_j|t^j\le\max(1,t/q)^M\sum|p_j|q^j\).
Multiply the two sums and use AS20 to obtain the exact functional norm bound
\[
\|\ell_z|_{I_N}\|\le\mathfrak A_kH_R
\left(kR_h/q+D/(qR)\right)^{q'}
\max(1,D/(qR))^M\|z\|.
\tag{AS21}
\]
For 2≤R≤k, the last maximum is one since D≤2q. Also \(kR_hR\le k^2R_h\le qR_h\), so the other parenthesis is at most (\(R_h\)+2)/R. AS14 therefore proves
\[
\|\ell_z|_{I_N}\|\le\mathfrak F_kR^{-q'}\|z\|,
\quad\mathfrak F_k=\mathfrak A_kC_A\sqrt{n_E}
e^{2R_hq+(8+4B_A)k}(R_h+2)^{q'},\quad z\in\mathcal Z_R.
\tag{AS22}
\]
For all rows, AS16 and AS21 instead give
\[
\|\ell_z|_{I_N}\|\le\mathfrak F_{0,k}\|z\|,
\quad\mathfrak F_{0,k}=\mathfrak A_kM_{0,k}
(kR_h/q+2/\rho_A)^{q'}(2/\rho_A)^{M_{\max}}.
\tag{AS23}
\]
Here \(\log\mathfrak A_k\), \(\log\mathfrak F_k\) and \(\log\mathfrak F_{0,k}\) are O(q): \(M_{\max}\le2q\), q'≤q and all conductor/quartet factors except k are fixed. All derivatives through D were included.

## AS5. Every eigenvalue and the actual squared angles

Order the eigenvalues of \(C_N^\circ\) as \(\lambda_{1,N}\ge\cdots\ge\lambda_{r,N}\). Put
\[
L_A=b_0+9,\quad
j_A=\left\lceil\max\{2(a_0+1),a_0+1+4L_A\}\right\rceil,
\quad R_j=(j-1-a_0)/(2L_A).
\tag{AS24}
\]
For \(j_A\le j\le r\), first \(j-1-a_0\ge4L_A\), so \(R_j\ge2\). Second \(j\ge2(a_0+1)\) gives \(R_j\ge j/(4L_A)\). Third
\(R_j<r/(2L_A)\le(8k-32)/18<k\).
Finally
\[
a_0+b_0R_j
\le a_0+(j-1-a_0)/2=(j-1+a_0)/2<j.
\]
Thus the actual cancellation space has codimension at most j−1. In the coefficient-orthonormal row frame, AS22 bounds its covariance quadratic form by \(\mathfrak F_k^2R_j^{-2q'}\). Diagonalizing \(C_N^\circ\) proves the min–max step directly: if \(\lambda _j\) exceeded that number, the span of its first j eigenvectors would intersect this codimension<j space nontrivially and violate the quadratic-form bound. Therefore
\(\lambda_{j,N}\le\mathfrak F_k^2(4L_A/j)^{2q'}\).
For j<\(j_A\), AS23 suffices. Define
\[
\mathfrak U_k=\max\{\mathfrak F_k^2(4L_A)^{2q'},
\mathfrak F_{0,k}^2j_A^{2q'}\}.
\]
AS10 gives the full enclosure
\[
c_k\le\lambda_{j,N}\le\mathfrak U_kj^{-2q'},
\quad1\le j\le r,\quad\log\mathfrak U_k=O(q).
\tag{AS25}
\]
If \(j_A\)>r, the second term still proves every finite upper bound. No rank or cancellation independence assumption is needed.

The strip interpolation bound, using AS7 on exactly its \(n_E\) nodes with separation≥2δ, is
\[
B_E=n_EM_\sigma\left(\frac{2n_E+kR_h}{2\delta}\right)^{2(n_E-1)}.
\]
The actual upper functional row is \(W_zA_{D,1}\) and has its first v entries zero. Strip interpolation therefore gives
\(\|W_z\|\ge\|z\|/(\mathfrak M_k\sqrt{B_E})\). Thus
\[
B_N^\circ\succeq b_k^-I,
\quad b_k^-=(\mathfrak M_k^2B_E)^{-1}.
\tag{AS26}
\]
For an upper bound take \(t_A=\tanh(\rho_A/2)\), so
\(|\arctan t|\le\sum_{j\ge0}|t|^{2j+1}/(2j+1)
=\operatorname{arctanh}|t|\le\rho_A/2\).
The original generating function is
\[
H_z(t)=(1+t^2)^{-1/4}A_z(-i\arctan t)=\sum a_{z,n}t^n,
\quad W_{z,n}=\rho_na_{z,n}/\sqrt{M_\sigma}.
\tag{AS27}
\]
It follows by applying AS2 to the exact Gamma generating function
\(\sum p_n(y)t^n/n!=(1+t^2)^{-1/4}e^{y\arctan t}\).
AS16 and Cauchy's coefficient bound give
\(|a_{z,n}|\le M_{0,k}(1-t_A^2)^{-1/4}t_A^{-n}\|z\|\).
Since \(\rho_n^2\le2n+1\) and \(\sum_{n=0}^D(2n+1)=(D+1)^2\),
\[
B_N^\circ\preceq b_k^+I,\qquad
b_k^+=\max\left\{1,
\frac{M_{0,k}^2(1-t_A^2)^{-1/2}}{M_\sigma}
(2q+1)^2t_A^{-4q}\right\}.
\tag{AS28}
\]
The bounds are for all row combinations, hence contain no extra factor r.

The explicit unitary
\(U_N=B_N^{1/2}R_Z^{-1/2}(B_N^\circ)^{-1/2}\)
satisfies \(U_N^*U_N=I\) and
\(U_N^*S_NU_N=(B_N^\circ)^{-1/2}C_N^\circ(B_N^\circ)^{-1/2}\).
Generalized min–max applied to the Rayleigh quotient \(u^*C_N^\circ u/(u^*B_N^\circ u)\), using AS25–28, proves the actual squared-angle enclosure
\[
\frac{c_k}{b_k^+}\le s_{j,N}\le
\min\left\{1,\frac{\mathfrak U_k}{b_k^-}j^{-2q'}\right\},
\qquad s_{1,N}\ge\cdots\ge s_{r,N}>0.
\tag{AS29}
\]
Every original lower-root constraint remains in \(C_N\).

## AS6. A bounded centered spectrum, volume and all inverse exterior ranks

Set \(\ell_k=\log(q/k)\), \(x_{j,N}=q^{-1}\log s_{j,N}+2\ell_k\) and
\[
C_k^{\mathrm{ang}}=\max\left\{0,
-q^{-1}\log(c_k/b_k^+)-2\ell_k,
q^{-1}\log(\mathfrak U_k/b_k^-)+2\ell_k
-(2q'/q)\log r\right\}.
\tag{AS30}
\]
This is a finite explicit number and is O(1). Here are all contributions to that claim. AS11 yields \(q^{-1}\log(1/c_k)-2\ell_k=O(1)\); the difference between q−1 and q contributes exactly \(-2\ell_k/q\). AS28 gives \(q^{-1}\log b_k^+=O(1)\), because \(\rho _A\),\(t_A\) are fixed positive numbers and \(\log M_{0,k}=O(k+\log k)\). Also \(\log(1/b_k^-)=O(k\log(k+2))\), and AS25 gives \(\log\mathfrak U_k=O(q)\). Finally
\[
2\ell_k-(2q'/q)\log r
=2\log\frac{q}{kr}+2(1-q'/q)\log r=O(1),
\]
since r=8k+O(1), q/k²→1 and 1−q'/q=(16k−48)/q. Thus the centered constant is bounded for fixed original data; this proof never asserts uniformity when \(d_A\) or |\(a_*\)| tends to zero.

AS29 and q'≤q give
\[
-C_k^{\mathrm{ang}}\le x_{j,N}
\le C_k^{\mathrm{ang}}+(2q'/q)\log(r/j)
\le C_k^{\mathrm{ang}}+2\log(r/j).
\tag{AS31}
\]
The elementary integral estimate
\(\sum_{j=1}^r\log(r/j)\le r\)
follows from \(\log(r!)\ge\int_1^r\log t\,dt=r\log r-r+1\). Summation proves the finite determinant enclosure
\[
-2rq\ell_k-C_k^{\mathrm{ang}}rq
\le\log\det S_N
\le-2rq\ell_k+(C_k^{\mathrm{ang}}+2)rq.
\tag{AS32}
\]
Therefore uniformly on the entire integer cutoff window,
\[
\log\det S_N=-2r_kq\log(q/k)+O(kq),\qquad
\frac{\log\det S_N}{kq\log(q/k)}\longrightarrow-16.
\tag{AS33}
\]
AS31 also gives \(|x_{j,N}|\le C_k^{\mathrm{ang}}+2\log(r/j)\), and hence the full empirical estimate
\[
\frac1r\sum_{j=1}^r
\left|\frac{-\log s_{j,N}}{2q\ell_k}-1\right|
\le\frac{C_k^{\mathrm{ang}}+2}{2\ell_k}.
\tag{AS34}
\]

The inverse of the exact map \(\mathcal P_N=P_NT_N\) is taken only on its image, with the inherited lower Gamma norm. Its singular values are \(s_{r,N}^{-1/2},\ldots,s_{1,N}^{-1/2}\). Thus
\[
\log\|\wedge^p\mathcal P_N^{-1}\|
=pq\ell_k-\frac q2\sum_{j=r-p+1}^r x_{j,N}.
\]
The average of the last p values of the decreasing sequence log(r/j) is no larger than its full average≤1. AS31 proves simultaneously for every 1≤p≤r that
\[
pq\left(\ell_k-\frac{C_k^{\mathrm{ang}}+2}{2}\right)
\le\log\|\wedge^p\mathcal P_N^{-1}\|
\le pq\left(\ell_k+\frac{C_k^{\mathrm{ang}}}{2}\right).
\tag{AS35}
\]
Division by pq\(\ell\)_k gives a uniform limit of one over N and p.

For any actual p-dimensional subspace X of the original row space, restrict both covariances before forming \(S_{X,N}\). AS10 and AS28 give every restricted squared angle≥\(c_k\)/\(b_k\)^+. Restriction of generalized min–max gives its jth squared angle≤the full \(s_{j,N}\). Multiplication of AS29 for j≤p proves
\[
p\log(c_k/b_k^+)\le\log\det S_{X,N}
\le\min\{0,p\log(\mathfrak U_k/b_k^-)-2q'\log(p!)\}.
\tag{AS36}
\]
No identification of \(S_{X,N}\) with a principal submatrix of \(S_N\) is used.

## AS7. Exponential tails and full cutoff variation

Write \(C=C_k^{\mathrm{ang}}\). For u≥C, AS31 implies
\(x_{j,N}>u\Rightarrow j<r e^{-(u-C)/2}\), and consequently
\(\#\{j:x_{j,N}>u\}\le r e^{-(u-C)/2}\).
Integrate this count from T to infinity to obtain, for T≥C,
\[
\frac1r\sum_j(x_{j,N}-T)_+
\le2e^{-(T-C)/2}.
\tag{AS37}
\]
There is no lower tail below −C. For 0≤θ<1/2, monotonicity of \(t^{-2\theta}\) gives
\(\sum_{j=1}^r j^{-2\theta}\le\int_0^r t^{-2\theta}dt
=r^{1-2\theta}/(1-2\theta)\).
Therefore
\[
\frac1r\sum_j e^{\theta x_{j,N}}
\le e^{\theta C}/(1-2\theta).
\tag{AS38}
\]
These bounds, with C=O(1), prove uniform integrability of the centered logarithms at the kq determinant scale.

The same row functionals act on nested spaces \(I_N\subset I_{N+1}\) and \(\mathcal P'_D\subset\mathcal P'_{D+1}\). Each inclusion adds exactly one unit orthogonal polynomial direction. Parseval therefore gives the exact fixed-row updates
\[
C_{N+1}=C_N+a_Na_N^*,\qquad B_{N+1}=B_N+b_Nb_N^*.
\tag{AS39}
\]
These are ACC17's full ideal and Gamma columns. Let \(\tau _j\) be the ordered generalized eigenvalues of \((C_{N+1},B_N)\). Min–max gives \(\tau_j\ge s_{j,N}\) and \(\tau_j\ge s_{j,N+1}\). Hence
\[
\sum_j|\log s_{j,N+1}-\log s_{j,N}|
\le\sum_j(\log\tau_j-\log s_{j,N})
+\sum_j(\log\tau_j-\log s_{j,N+1})
=\log\frac{\det C_{N+1}}{\det C_N}
+\log\frac{\det B_{N+1}}{\det B_N}.
\tag{AS40}
\]
This proves the sorted-spectrum variation bound even when individual squared angles change direction or collide.

For completeness the finite unprojected determinant allowance can be specified from already proved original forward and determinant estimates. Use
\[
V_N=\frac{qe^2}{M_\sigma}(N+1)^{3/2}(2N+1)^{kR_h+1},
\quad J_D=(D+1)\log^+(1/d_A),
\]
\[
K_N=\max\{r\log^+(\mathfrak M_k^2B_E),
r\log^+V_N+2(D+1)\log\mathfrak M_k+2J_D\}.
\tag{AS41}
\]
The root-evaluation bound \(V_N\) follows directly from the generating function before division by \(E_A\). At radius \(r_N=N/(N+1)\), one has \(r_N^{-n}\le e\) for n≤N, \(|\arctan t|\le\tfrac12\log(2N+1)\), and \(|1+t^2|^{-1/2}\le(N+1)/\sqrt{2N+1}\). Squaring Cauchy's coefficient bound and multiplying by \(\rho_n^2/M_\sigma\) gives
\[
|\phi_n(\omega_\alpha)|^2\le\frac{e^2}{M_\sigma}
\frac{\sqrt{4N+1}(N+1)}{\sqrt{2N+1}}(2N+1)^{kR_h}.
\]
The prefactor without \(e^2/M_\sigma\) is at most \((N+1)^{1/2}(2N+1)\), since \((4N+1)(N+1)\le(2N+1)^3\); their difference is \(8N^3+8N^2+N\ge0\). Sum over N+1 degrees and q original roots to obtain the stated \(V_N\). This is the CGR10/KF33 constant. The triangular matrix has
\(|\det A_{D,1}|=d_A^{D+1}\prod_{i=0}^D\rho_{i+v}/\rho_i\ge d_A^{D+1}\).
The singular-value complement identity gives
\(\|\wedge^j A_{D,1}^{-1}\|\le\mathfrak M_k^{D+1-j}e^{J_D}\).
Apply this to \(W_N=B_FA^{-1}\) and \(B_FB_F^*\preceq V_NR_Z\); together with AS26 it proves
\[
|\log(\det B_N/\det R_Z)|\le K_N=O(q\log(q+2)).
\tag{AS42}
\]
The slightly larger common \(\mathfrak M_k\) leaves CGS17's order unchanged and makes every constant here explicit.

Let \(\mu_{k,N}=r^{-1}\sum_j\delta_{x_{j,N}}\). For ordered empirical measures on the real line the optimal \(W_1\) matching is the ordered one: any crossed pairing a≤b,c≤d satisfies |a−c|+|b−d|≤|a−d|+|b−c|, and successively removing crossings proves the claim. Thus \(W_1\) is \(r^{-1}\) times the sum of ordered absolute differences. Sum AS40 over N=q−1,…,2q−1 and telescope both determinants. Since det C=det S det B, AS32 gives
\[
\sum_{N=q-1}^{2q-1}W_1(\mu_{k,N+1},\mu_{k,N})
\le2C_k^{\mathrm{ang}}+2+
\frac{2(K_{q-1}+K_{2q})}{rq}.
\tag{AS43}
\]
The last term tends to zero. This is a bound on the complete path, not a deduction from endpoint weak convergence.

## AS8. Both original Gamma source orders

Write \(k=4\ell+1\). The original order-s source is
\[
dm_s(y)=\frac{(2\pi)^{s/2}2^{s/2}}{4\pi\Gamma(s/2)}
|\Gamma(s/4+iy/2)|^2dy,\qquad s\in\{1,k\}.
\]
For s=1 this equals dσ. Applying Γ(z+1)=zΓ(z) exactly \(\ell\) times, without rescaling the source mass, gives
\[
dm_k(y)=\beta_k\prod_{j=0}^{\ell-1}[y^2+(2j+1/2)^2]d\sigma(y),
\qquad\beta_k=(2\pi)^{k/2}/(\sqrt2\Gamma(k/2)).
\tag{AS44}
\]
For any P of degree≤D, each positive factor is at least (2j+1/2)², proving the lower comparison. For the upper comparison, write the product as the squared modulus of \(\prod_j(y+i(2j+1/2))\), and apply AS7 successively. Before the jth multiplication the degree is at most D+j. Hence
\[
a_{k,D}\|P\|_\sigma^2\le\|P\|_{m_k}^2\le b_{k,D}\|P\|_\sigma^2,
\]
\[
a_{k,D}=\beta_k\prod_{j<\ell}(2j+1/2)^2,
\quad b_{k,D}=\beta_k\prod_{j<\ell}[2(D+j+1)+2j+1/2]^2.
\tag{AS45}
\]
This full-line comparison is valid on the entire source and on \(I_N\), with unchanged lower roots and center. For the norm of a fixed functional, taking the supremum \(|\ell(P)|^2/\|P\|^2\) reverses these inequalities. Thus both restricted and unrestricted covariances have comparisons \(b^{-1}C^{(1)}\preceq C^{(k)}\preceq a^{-1}C^{(1)}\), and likewise for B. Their generalized Rayleigh quotients are within factors a/b and b/a. Generalized min–max proves, for every j,
\[
|\log s_{j,N}^{(k)}-\log s_{j,N}^{(1)}|
\le L_{k,D}:=\log(b_{k,D}/a_{k,D})
=2\sum_{j<\ell}\log\frac{2(D+j+1)+2j+1/2}{2j+1/2}.
\tag{AS46}
\]
This sum is O(k log(q+2)), uniformly D≤2q. A finite common bound is
\(L_k^{\max}=2\ell\log(8q+8\ell+5)\), since the denominator≥1/2. The source mass \(\beta _k\) cancels only in the displayed angle ratio, after both physical metrics have been retained.

For the original four signs \(\mathcal Rf=f_{q-1}+f_q-f_{2q-1}-f_{2q}\), summing gives the finite receiver
\[
|\mathcal R\log\det S_N^{(k)}-
\mathcal R\log\det S_N^{(1)}|
\le r\sum_{N\in\{q-1,q,2q-1,2q\}}L_{k,N-v}
\le4rL_k^{\max}=O(k^2\log(q+2))=o(kq).
\tag{AS47}
\]
Likewise \(W_1(\mu^{(k)}_{k,N},\mu^{(1)}_{k,N})\le L_{k,D}/q=o(1)\). Replacing \(C_k^{\mathrm{ang}}\) by \(C_k^{\mathrm{ang}}+L_k^{\max}/q\) transfers AS31, AS34 and AS37 to the second source order, including the full spectrum and its tails. No interchange of an unrelated quotient with the lower-root projection is needed.

## AS9. The original arithmetic receiver and its remaining endpoint statistic

This section retains the finite domain and proved source inputs of DCR1–27, OOQ1–40 and ACC17–22. Its outer scalar \(C_\partial\) is precisely their monic-profile coefficient, with its recorded mathematical status; no new scalar equilibrium claim is inserted here. In particular DCR9 retains the OSP, OR12 and CG6 guards, k≥257, a≥1, n≥2g+1, n≥2/\(b_*\), \(r_b\)≤ρ/2, ρ≤min(1/2,√(\(a_eq\)/2)), and each of its explicitly listed parameter pairs in [3/2,5/2]×[π/4,π]. The finite angle estimates AS1–47 require only their own weaker guards. The larger original domain is needed solely for the inherited arithmetic outer receiver.

The complete conductor divisor and its physical transport are
\[
d_{\mathrm{cond}}(S')=\mathcal T_A\chi(S')/\chi'(S'),\quad
a_A=[S'^g]d_{\mathrm{cond}}=\mu_v\binom qv,\quad g=q-q'-v,
\quad p_A(y)=d_{\mathrm{cond}}(c'+iy)/(a_Ai^g).
\]
The notation \(d_{\mathrm{cond}}\) denotes the original conductor polynomial; the scalar \(d_A=|\mu_v|/v!\) remains unchanged. Every original factor of χ' remains in the measure |χ'(c'+iy)|²dσ. The coefficient transport is
\((T_{c',i})_{aj}=\binom ja(c')^{j-a}i^a\), with inverse \(y^j\mapsto i^{-j}(S'-c')^j\). Thus the actual observation becomes \(A_R^y=A_RT_{c',i}^{-1}\); its Gram is transported, not identified with a different coefficient metric.

Here is the exact inherited error used in the endpoint reduction:
\[
E_{\mathrm{DCR},k}=B_{\mathrm{KF49}}+\widehat E_0+\widehat E_1
+\sum_{N\in\{q-1,q,2q-1,2q\}}(E_N^{\mathrm{vol}}+K_N),
\tag{AS48}
\]
where the sharpened original comparison is
\(B_{\rm KF49}^{\rm sharp}=2m\Lambda_k+2s_k\log\kappa_k^*
+2B_k^{\rm ang}+2\sum_NE_N^*\), and this sharper value is used for \(B_{\mathrm{KF49}}\) in AS48. Here
\(\Lambda_k=\log(u_k/\ell_{k,2q})=O_h(k+\log(q+2))\),
\(\ell_{k,2q}=a_k/[1+4(2q+M_h)^2]^{M_h}\),
\(u_k=A_k\), and \(M_h=21+4m_0=25\) on the present simple-quartet packet. These are NG2's original positive full-mass constants \(a_k\),\(A_k\) from CAI16, with their original h and arithmetic source.

The improvement uses the same source, not a second norm comparison: NG2 bounds the full original polynomial forms by these two scalars simultaneously for N≤2q. Taking the infimum over each complete original affine quotient fibre preserves the two constants. Restriction to the actual rank-m kernel frame then puts each determinant log difference in \([m\log\ell,m\log u]\). The four signs contain two positive and two negative terms, hence their combined absolute difference is at most \(2m(\log u-\log\ell)=2m\Lambda_k\). This proves the replacement of only the term \(2mL^{\mathrm{form}}\) in KF49. The low-intersection, low-angle and exterior terms keep every original constant and guard. This is the same exact repair FR1 in the 018 finite determinant continuation. Here \(E_N^*=(N+1)\log M_D+J_D\), and \(E_N^{\mathrm{vol}}=0\) at the low cutoffs while at N=q+L, L=q−1,q,
\(E_N^{\rm vol}=2v(L+1)\log[(q+L)/(q-v+1)]+B_N^{\rm graph}\), exactly CG24's full graph allowance. The \(K_N\) in AS41 may replace the smaller original CGS constants because it was independently proved.

To specify the distant-component cost, DCR factors the entire monic \(p_A=p_bp_f\) at \(|\zeta|=q^{7/8}/8\), assigning boundary roots to \(p_f\) and retaining full multiplicities. Let b=deg \(p_f\) and a=g−b. The full source remainder covariance has finite bounds
\(\widehat lI_g\preceq(Q_N^d)^{-1}\preceq\widehat u_NI_g\), with
\(\widehat l=(h_+^0)^{-1}\),
\(\widehat u_N=B_{\rm rem}(M)^2/h_-(M)\),
\[
B_{\rm rem}(M)=g2^g(1+R_d)^g\sqrt{M+1}(2R_d)^M,
\quad R_d=\max(1,|c'|+q/r_*),
\]
\[
h_-(M)=\frac{C_Le^{-\pi(q+1)}(q^2-k^2R_h^2)^{q'}}
{(M+1)^2(2M+1)64^M(1+|c'|+q)^{2M}},
\quad h_+^0=gM_\sigma(4q+2+kR_h+|c'|)^{2q}.
\]
These are CGR16's original finite bounds, including \(r_*\) and \(C_L\). DCR16 gives the full scalar allowance \(\varepsilon_k^b\) in terms of its explicit high/low errors and the original OSP full-source comparison. Writing \(\Delta c=qC_\partial/2\) and \(u_i=2q-1+i\), its exact Schur error is
\[
\widehat E_i=2(g-b)\varepsilon_k^b+
b\{\log^+(\widehat u_{u_i}/\widehat l)+|\Delta c|\}.
\tag{AS49}
\]
Every distant primary component is therefore paid for at its complete metric cost; its small dimension is used only after these bounds.

The two original integration regions are also retained. In DCR's full exponential comparison, with n=q/2, Q=q' and \(f(nz)=f_e(z^2)+zf_o(z^2)\), the original real-line norm is exactly
\[
n^{2Q+1}\left[
\int_0^\infty|f_e(x)|^2x^{Q-1/2}e^{-n\beta\sqrt x}dx
+\int_0^\infty|f_o(x)|^2x^{Q+1/2}e^{-n\beta\sqrt x}dx\right].
\tag{AS50}
\]
Indeed the contributions of y=+n√x and y=−n√x cancel the cross term and their Jacobians sum to exactly the displayed powers. The exact lift \(r_n(z^2)a_t(z)\) is bounded on both branches by
\(|a_t(\pm\sqrt x)|\le\|a_t\|_1(1+\sqrt x)^{a-1}\).
Thus the monic-profile upper and lower comparisons entering \(\varepsilon_k^b\) use the whole source. The original OOQ30–31 comparison then returns to |χ'|²dσ without deleting either region.

The exact frame identity underlying the receiver is
\[
\det(J_K^*Q_N^UJ_K)=|\det[J_K,J_R]|^2
\det Q_N^U\,\det C_N,
\tag{AS51}
\]
where \(J_R\) is a fixed right inverse of the actual onto observation \(A_R\), and \(\ker A_R=\operatorname{im}J_K\). To prove it, perform block elimination of the positive Gram in frame [\(J_K\),\(J_R\)]; its complementary Schur metric is \((A_R(Q_N^U)^{-1}A_R^*)^{-1}\), as follows by minimizing over the first block on every fibre. Taking determinants proves AS51. The fixed frame determinant cancels with the four signs. Transfer the complete arithmetic kernel through KF49, use CG24 for det Q^U versus det Q^d, use the full DCR24 metric return with errors AS49, and then use AS42. The triangle inequality yields
\[
|\mathcal R\log\det H_{K,N}^{\rm ar}-gqC_\partial-
\mathcal R\log\det S_N^{(1)}|\le E_{\rm DCR,k}=o(kq).
\tag{AS52}
\]
Thus the coefficient is the exact g, not the row dimension r.

The adjacent error can now be specified using this proof's sharper constants. Define
\(u_k=\max(1,\mathfrak U_k,b_k^+)\),
\(A_k^{adj}=\log^+(u_k/c_k)\),
\(B_k^{adj}=\log^+(u_k/b_k^-)\), and
\(E_{adj,k}=2\max(A_k^{adj},B_k^{adj})\).
In AS39 the determinant lemma gives each increasing covariance log ratio as \(\log(1+a^*C^{-1}a)\). The relative rank-one matrix has just one nonunit eigenvalue, and AS10/25/26/28 bound it by \(u_k\)/\(c_k\) or \(u_k/b_k^-\). Therefore each adjacent angle log increment lies in \([-B_k^{\mathrm{adj}},A_k^{\mathrm{adj}}]\), and
\[
\left|\mathcal R\log\det S_N^{(1)}
-2\log\frac{\det S_{q-1}^{(1)}}{\det S_{2q-1}^{(1)}}\right|
\le E_{adj,k}=O(q\log(q+2))=o(kq).
\tag{AS53}
\]
This follows exactly by writing the four-return as twice the endpoint ratio plus \(\delta_{q-1}-\delta_{2q-1}\); no extra rank factor is paid.

Put \(E_{\mathrm{rec},k}=E_{\mathrm{DCR},k}+E_{\mathrm{adj},k}\). From AS52–53 and the definition of x,
\[
\left|\mathcal R\log\det H_{K,N}^{\rm ar}-gqC_\partial
-2q\left(\sum_jx_{j,q-1}-\sum_jx_{j,2q-1}\right)\right|
\le E_{rec,k}=o(kq).
\tag{AS54}
\]
The common leading angular term cancels exactly. Its residual endpoint statistic remains present and unevaluated. AS47 gives the corresponding four-angle receiver for the other original source order with the additional finite error \(r\sum_N L_{k,N-v}\). For the twice-endpoint form AS54, the additional error is
\(2r(L_{k,q-1-v}+L_{k,2q-1-v})\). Both are o(kq).

## AS10. A bounded-logarithm realization of the residual statistic

For T≥\(C_k^{\mathrm{ang}}\), define using the complete covariances
\[
\mathcal L_{N,T}=-rT+q^{-1}\log
\frac{\det(B_N+e^{q(2\ell_k+T)}C_N)}
{\det(B_N+e^{q(2\ell_k-T)}C_N)}.
\tag{AS55}
\]
Diagonalizing \(B_N^{-1/2}C_NB_N^{-1/2}\) expresses this as \(\sum f_{q,T}(x_{j,N})\), where
\(f_{q,T}(x)=-T+q^{-1}\log(1+e^{q(x+T)})-q^{-1}\log(1+e^{q(x-T)})\).
For any t, \(\log(1+e^{qt})/q=t_++d_q(t)\), where
\(0\le d_q(t)=q^{-1}\log(1+e^{-q|t|})\le\log2/q\).
Subtracting the two d terms, whose difference has modulus≤log2/q, proves
\(|f_{q,T}(x)-\max(-T,\min(x,T))|\le\log2/q\).
AS31 has no lower tail below −T. Apply AS37 to its upper tail to obtain
\[
\left|\sum_jx_{j,N}-\mathcal L_{N,T}\right|
\le2r e^{-(T-C_k^{ang})/2}+r\log2/q.
\tag{AS56}
\]
Combining the two endpoints with AS54 proves the finite original receiver
\[
\left|\mathcal R\log\det H_{K,N}^{\rm ar}-gqC_\partial
-2q(\mathcal L_{q-1,T}-\mathcal L_{2q-1,T})\right|
\le E_{rec,k}+8rq e^{-(T-C_k^{ang})/2}+4r\log2.
\tag{AS57}
\]
The choice \(T=C_k^{\mathrm{ang}}+2\log\log(q+e)\) makes the new error o(kq). Each \(C_N\) in AS55 is still the exact Schur expression \(W_NW_N^*-W_NE_D^*(E_DE_D^*)^{-1}E_DW_N^*\), with every original lower root. The expression is a regularization of its logarithms; it does not define a new arithmetic heat operator.

One directed restriction follows from complete positivity. Since both covariances increase, \(\det C_{2q-1}\ge\det C_{q-1}\). AS42 yields
\(\log(\det S_{2q-1}/\det S_{q-1})\ge-K_{q-1}-K_{2q-1}\).
The original kernel quotient metric decreases with source enlargement, so its four-return is nonnegative. AS54 then gives
\[
-\frac{K_{q-1}+K_{2q-1}}{rq}
\le\bar x_{2q-1}-\bar x_{q-1}
\le\frac{gC_\partial}{2r}+\frac{E_{rec,k}}{2rq},
\qquad\bar x_N=r^{-1}\sum_jx_{j,N}.
\tag{AS58}
\]
Because g/(2r)→1, the limiting permitted interval is [0,C_∂]. This proves a restriction; it does not choose a point in that interval.

## AS11. Exact Cauchy sampling on every actual row

Take the fixed zero-free t disk from AS27 and sample \(H_z\) at radius \(t_A\)/2. For an integer T>D define
\[
a_{z,n}^{[T]}=\frac{(t_A/2)^{-n}}T\sum_{j=0}^{T-1}
H_z((t_A/2)e^{2\pi ij/T})e^{-2\pi ijn/T},\quad0\le n\le D.
\tag{AS59}
\]
The finite geometric sum projects exactly onto indices congruent to n mod T. Since n<T, there are no negative aliases, and absolute convergence gives
\[
a_{z,n}^{[T]}-a_{z,n}=\sum_{l\ge1}a_{z,n+lT}(t_A/2)^{lT}.
\]
Use the full-row Cauchy estimate in AS28 on each combination of coefficient-orthonormal original rows. Summing the exact Gamma weights proves
\[
\|W_N^{[T]}-W_N^\circ\|
\le\sqrt{b_k^+}\frac{2^{-T}}{1-2^{-T}},
\qquad W_N^\circ=R_Z^{-1/2}W_N.
\tag{AS60}
\]
Choose
\[
T_k=\max\left\{2q+1,
\left\lceil\log_2(32b_k^+/c_k)\right\rceil\right\}.
\tag{AS61}
\]
AS10 and AS28 on the nonzero row space imply \(c_k\le b_k^+\), so \(2^{-T_k}\le c_k/(32b_k^+)\le1/32\) and the error e is at most \(c_k/(31\sqrt{b_k^+})\). Since \(\|W_N^\circ\|\le\sqrt{b_k^+}\), the error in either sampled covariance, using exactly \(P_N\) or I, is at most
\(2\sqrt{b_k^+}e+e^2\le c_k(2/31+1/31^2)<c_k/4\).
Both true covariances are≥\(c_kI\). Therefore
\[
\tfrac34C_N^\circ\preceq C_N^{[T]}\preceq\tfrac54C_N^\circ,
\qquad\tfrac34B_N^\circ\preceq B_N^{[T]}\preceq\tfrac54B_N^\circ.
\tag{AS62}
\]
Taking determinants gives each ratio in \([(3/4)^r,(5/4)^r]\). Their quotient is in \([(3/5)^r,(5/3)^r]\), hence
\[
\left|\log\det S_N-
\log\frac{\det C_N^{[T]}}{\det B_N^{[T]}}\right|
\le r\log(5/3).
\tag{AS63}
\]
AS11 and \(\log b_k^+=O(q)\) show
\[
T_k=\frac2{\log2}q\log(q/k)+O(q).
\tag{AS64}
\]
Eventually this term exceeds 2q+1. This is a sufficient exact sample count, not a complexity lower bound. Evaluating these functions numerically and inverting the full lower-root Gram require their own certified error bounds. AS63 does not certify arbitrary floating-point samples.

## AS12. Sources, inheritance and scope

The calculation AS1–47 and AS55–64 is proved directly above from the original finite objects and the read classical formulas. AS48–54 states precisely how it enters the already established DCR/ACC arithmetic receiver, keeping that receiver's original monic-profile input and finite guards. It neither upgrades the status of an inherited source nor replaces the original arithmetic weight by Gamma.

- [Original conductor frame OCF4–8](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/5992ad50c0f2a06921f1fcaded7b4e38097c0739/workbenches/splitzero-tandem/continuations/20260920-original-kernel-mixed-determinants/providers/ORIGINAL_CONDUCTOR_STRIP_FRAME.tex#L27) supplies the actual strip, pivot and exact elimination.
- [Weighted conductor WCF4–13, WCF19a–f, WCF20–22](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/5992ad50c0f2a06921f1fcaded7b4e38097c0739/workbenches/splitzero-tandem/continuations/20260920-original-kernel-mixed-determinants/providers/WEIGHTED_CONDUCTOR_FORWARD.tex#L28) specifies the unaltered matrix, both centers and source orders.
- [The original full-source comparison NG2](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/5992ad50c0f2a06921f1fcaded7b4e38097c0739/workbenches/splitzero-tandem/continuations/20260920-original-kernel-mixed-determinants/providers/NATIVE_GAUSSIAN_TRANSFER.tex#L51) supplies the sharper same-source width used in AS48. Its quotient, restriction and four-sign proof is included above; the 018 FR1 repair records the identical map.
- [CGR1–29](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/7230c00b9f07dd222b2aea95427d67918f3a8cac/workbenches/splitzero-tandem/continuations/20260921-local-covariance-activation/009/INVARIANT_COVARIANCE_POLE_FILTRATION.tex) and [CGS1–22](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/7230c00b9f07dd222b2aea95427d67918f3a8cac/workbenches/splitzero-tandem/continuations/20260921-local-covariance-activation/009/INVARIANT_STRIP_ANGLE_REDUCTION.tex) specify and prove the actual row covariance and projection-angle map.
- [CGP1–28](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/7230c00b9f07dd222b2aea95427d67918f3a8cac/workbenches/splitzero-tandem/continuations/20260921-local-covariance-activation/010/ORIGINAL_PROJECTION_CAUCHY_ACTION.tex), especially CGP2–11, specifies every lower root, the original generating function and zero-kernel proof. AS59–64 extends the finite sampling estimate to every row.
- [DCR1–27](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/7230c00b9f07dd222b2aea95427d67918f3a8cac/workbenches/splitzero-tandem/continuations/20260921-local-covariance-activation/009/CONDUCTOR_DIVISOR_COVARIANCE_RETURN.tex#L139) and [ACC17–23](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/7230c00b9f07dd222b2aea95427d67918f3a8cac/workbenches/splitzero-tandem/continuations/20260921-local-covariance-activation/010/ORIGINAL_ADJACENT_CUTOFF_CURRENT.tex) are the full arithmetic receiver. [OOQ1–40](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/5992ad50c0f2a06921f1fcaded7b4e38097c0739/workbenches/splitzero-tandem/continuations/20260920-original-kernel-mixed-determinants/providers/09_INPUT_CUMULATIVE_PROOFS.tex#L23179) is the exact original outer-profile source; this note makes no new claim of reading the whole cumulative corpus.
- R. A. Askey and R. Roy document the [Gamma product, DLMF 5.8.3](https://dlmf.nist.gov/5.8.E3). T. H. Koornwinder, R. Wong, R. Koekoek, R. F. Swarttouw and W. P. Reinhardt document the [Legendre generating function, 18.12.11](https://dlmf.nist.gov/18.12.E11), [Meixner–Pollaczek recurrence, 18.22.8](https://dlmf.nist.gov/18.22.E8), and [generating function, 18.23.7](https://dlmf.nist.gov/18.23.E7). The retained original formula TeX files were read, not PDFs.
- J. L. W. V. Jensen, *Sur un nouvel et important théorème de la théorie des fonctions*, Acta Mathematica 22 (1899), 359–364, [DOI](https://doi.org/10.1007/BF02417878), is the human source of the zero-count formula. Its finite use and the required disk harmonic argument are proved in AS3; no unread result is imported as a missing estimate.

The independent exact checker has auxiliary finite Gamma and lattice fixtures. These verify the recorded algebraic identities and failure controls; they do not evaluate the period-dependent original rows or the residual kq coefficient.


The preceding complete proofs are published at a fixed edition: [FI1–17; FR1–4](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/75256b0237884bdef0074c2ac6310de1ea32ec26/workbenches/splitzero-tandem/continuations/20260921-invariant-collision/FINITE_INVARIANT_PROOFS.md), [CI1–26; CL1–18](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/75256b0237884bdef0074c2ac6310de1ea32ec26/workbenches/splitzero-tandem/continuations/20260921-invariant-collision/CUTOFF_INNOVATION_PROOFS.md), [IC1–42](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/75256b0237884bdef0074c2ac6310de1ea32ec26/workbenches/splitzero-tandem/continuations/20260921-invariant-collision/COLLISION_PROOFS.md). All original source versions and human citations are retained in the accompanying source bank.
