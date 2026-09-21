# Complete finite invariant determinant calculation

The complete received argument is retained below, with the sharper same-source width in equation (12), the constant-one projection estimate in equation (21), and the weighted-functional correction in the auxiliary example. The following FI sections give the additional proofs and full source identifications.

## A quantitative calculation of the original invariant determinant

The remaining quantity is still

$$
\mathcal K_k
=
\mathcal R\log\det(I_K^*G_NI_K),
\qquad
\mathcal R f_N=f_{q-1}+f_q-f_{2q-1}-f_{2q}.
$$

The new KG, MF, and PC results do not assign its \(kq\) coefficient. The received invariant-determinant argument identifies the full projected invariant covariance as the remaining calculation. 

The result obtained here is a **finite-\(k\) formula for this original determinant with an explicit \(O_{h,A}(q\log q)\) remainder**. It retains every invariant row and every lower-root projection. Its scalar reference factor is a specified positive rational number; its remaining matrix can be calculated on one fixed zero-free circle, without deleting conductor-pole rows.

In particular, the normalized remainder is

$$
O_{h,A}\!\left(\frac{\log q}{k}\right).
$$

This is a quantitative remainder for the actual kernel allocation. **The limiting coefficient remains unevaluated:** the period-dependent projected covariance in the formula below has not been numerically evaluated in this finite derivation.

The received argument used the mathematical edition at `cb9705da84d6f8689611914ed9659298e620ba0a` and its checked successor `bee43be41d2f6f872869d5e258fa5f752335a5ad`. The latter’s recorded change is the publication-link update, not a new kernel-coefficient theorem.

---

## 1. The finite-\(k\) theorem

Retain

$$
q=(k+1)^2,\qquad q'=(k-7)^2,\qquad
c=k/2,\qquad c'=c-4,
$$

the original conductor order \(v\), and

$$
g=q-q'-v.
$$

At each original cutoff put

$$
L=N-q,\qquad D_N=N-v,\qquad M_N=L+g.
$$

Thus the four values of \(L\) are exactly

$$
-1,\quad0,\quad q-1,\quad q.
$$

Let \(Z\) be a complete independent row basis in the original strip coordinates, after the CG29–30 low-degree constraint elimination. Its weighted functionals have initial coefficient matrix \(A_R\); its full upper-root row embedding is \(\widetilde Z=ZS_k^{\mathsf T}\), as proved in FI2 below. Its rank is

$$
r=g-(m-s_k)=8k-32-v+s_k,
\qquad s_k=\dim(K\cap\mathcal P_{<v}).
$$

Write

$$
R_Z=ZZ^*>0,\qquad Z^\circ=R_Z^{-1/2}Z.
$$

This is an explicit, cutoff-independent change of row coordinates. Its determinant cancels under the four prescribed signs; it does not change the physical source metric.

For a row \(z\) of \(Z^\circ\), keep

$$
F_z(w)=\sum_\alpha z_\alpha e^{\beta_\alpha w},
\qquad
G_z(w)=\frac{F_z(w)}{E_A(w)},
$$

$$
H_z(t)
=(1+t^2)^{-1/4}e^{-c'w(t)}G_z(w(t)),
\qquad w(t)=-i\arctan t.
$$

The source proves that these are the actual invariant functionals, and that their covariance is

$$
C_N
=
W_NP_NW_N^*,
\qquad
P_N=I-E_N^*(E_NE_N^*)^{-1}E_N,
\tag{1}
$$

where \(E_N\) evaluates at **all** original lower roots. This is the matrix specified in the received argument, now in the fixed \(R_Z\)-orthonormal row frame.

Define the rational moments

$$
\nu_{2j}=(2j)![t^{2j}](\cos t)^{-1/2},
\qquad \nu_{2j+1}=0,
$$

and the positive rational determinants

$$
\Delta_n(a)=
\det[\nu_{2a+i+j}]_{i,j=0}^{n},
\qquad
\Delta_{-1}(a)=1.
$$

Set

$$
\boxed{
\mathcal A_{k,v}
=
\frac{
\Delta_{g-1}(q')\Delta_g(q')
\Delta_{q-1}(q-v)\Delta_q(q-v)
}{
\Delta_{q+g-1}(q')\Delta_{q+g}(q')
\Delta_0(q-v)
}.
}
\tag{2}
$$

Every factor is positive. Only moments through order \(4q-2v\) occur.

**Theorem.** On the original finite KF/CG guard domain, there is the explicitly specified error \(\mathcal E_k\) in equation (13) below such that

$$
\boxed{
\left|
\mathcal K_k
-\log\mathcal A_{k,v}
-\mathcal R\log\det C_N
\right|
\le \mathcal E_k,
\qquad
\mathcal E_k=O_{h,A}(q\log(q+2)).
}
\tag{3}
$$

Furthermore, all four \(C_N\) can be approximated using every original row, with no pole-filtration deletion, by positive matrices \(\widehat C_N\) satisfying

$$
\boxed{
\left|
\mathcal K_k
-\log\mathcal A_{k,v}
-\mathcal R\log\det\widehat C_N
\right|
\le
\mathcal E_k+\frac{4r}{4q-1}.
}
\tag{4}
$$

The required number of circle samples at each cutoff is

$$
O_{h,A}(q\log(q+2)),
$$

with an explicit sufficient count in equation (22). The absolute tolerances on the assembled original function samples and lower-root matrix require \(O_{h,A}(q\log q)\) digits in the logarithmic sense made precise below.

Equation (3) does **not** use the high-endpoint monic-profile or zero-law asymptotic. Its inputs are the finite original-source comparison, the complete conductor graph estimate, and full-polynomial Gamma inequalities. The previously obtained \(gqC_\partial\) is replaced here by the exact finite rational expression \(\log\mathcal A_{k,v}\), not by a newly asserted rate of convergence to that constant.

## 2. Derivation of the scalar factor and its remainder

Let

$$
d_A=\mathcal U_A1,\qquad
a_A=\mu_v\binom qv,
$$

so \(d_A\) is the full original outer polynomial of degree \(g\), with its actual leading coefficient \(a_A\).

For a polynomial \(F\), define the physical Gamma Gram

$$
\mathsf H_n[F]_{ij}
=
\int_{\mathbb R}
\overline{(c'+iy)^i}(c'+iy)^j
|F(c'+iy)|^2\,d\sigma(y),
\quad 0\le i,j\le n,
\tag{5}
$$

where

$$
d\sigma(y)=
\frac{|\Gamma(1/4+iy/2)|^2}{2\pi}\,dy,
\qquad
\mathfrak m_\sigma=\sqrt{2\pi}.
$$

An empty Gram has determinant one.

### The exact outer quotient determinant

The coefficient basis

$$
1,S',\ldots,S'^{g-1},
d_A,S'd_A,\ldots,S'^Ld_A
$$

has determinant \(a_A^{L+1}\). Taking its full Gram determinant and Schur-complementing the **entire** \(d_A\mathcal P_L\) relation space gives

$$
\boxed{
\det Q_N^d
=
|a_A|^{2(L+1)}
\frac{\det\mathsf H_{M_N}[\chi']}
{\det\mathsf H_L[\chi'd_A]}.
}
\tag{6}
$$

For \(L=-1\), the exponent is zero and the denominator is the empty determinant.

The source’s exact complementary identity is

$$
\det H_{\overline K,Y_N}
=
|\det T_{\mathrm{frame}}|^2
\det Q_N^U\,\det C_N^U.
$$

The same fixed frame is used at every cutoff. The finite native-to-graph comparison is KF49, and the full-volume graph comparison is CG24. Consequently

$$
\boxed{
\left|
\mathcal K_k-
\mathcal R\bigl(\log\det Q_N^d+\log\det C_N\bigr)
\right|
\le
B_{\mathrm{KF49}}+\sum_NE_N^{\mathrm{vol}}.
}
\tag{7}
$$

There is no replacement of the restriction to \(\overline K\) by a full-volume estimate in this step: the actual invariant covariance \(C_N\) remains in the determinant identity.

### Replace the scalar reference integrals, with their full error

Use the original finite form bounds CG18 and CG20:

$$
e^{-E_{\chi'}}
\|y^{q'}p(c'+iy)\|_\sigma^2
\le
\|\chi'p\|_{\sigma,c'}^2
\le
e^{E_{\chi'}}
\|y^{q'}p(c'+iy)\|_\sigma^2,
$$

$$
e^{-E_{d,N}}|a_A|^2
\|y^{q-v}h(c'+iy)\|_\sigma^2
\le
\|\chi'd_Ah\|_{\sigma,c'}^2
\le
e^{E_{d,N}}|a_A|^2
\|y^{q-v}h(c'+iy)\|_\sigma^2.
\tag{8}
$$

Here \(p\) ranges through the complete degree-\(M_N\) space, and \(h\) through degree \(L\). The published finite bounds satisfy

$$
E_{\chi'}=O_A(1),
\qquad E_{d,N}=O_A(\log(q+2)).
$$

Their proof retains both integration regions and all exceptional outer roots; those factors are consumed through their displayed errors, not removed.

Define

$$
\mathsf J_n^{(a)}
=
\left[\int y^{2a+i+j}\,d\sigma(y)\right]_{i,j=0}^n.
$$

The transformation from \(S'^j=(c'+iy)^j\) to \(y^j\) is triangular with diagonal \(i^j\). Its determinant has modulus one. Thus (8), followed by determinants in the same coefficient frames, gives

$$
\boxed{
\left|
\log\det Q_N^d
-
\left[
\log\det\mathsf J_{M_N}^{(q')}
-\log\det\mathsf J_L^{(q-v)}
\right]
\right|
\le
(M_N+1)E_{\chi'}+(L+1)E_{d,N}.
}
\tag{9}
$$

The factor \(|a_A|^{2(L+1)}\) in (6) cancels the identical factor in the full relation Gram. This is the exact location of that cancellation.

The Gamma generating function, in the retained monic convention, is

$$
\sum_{n\ge0}\frac{p_n(y)}{n!}t^n
=
(1+t^2)^{-1/4}e^{y\arctan t}.
$$

Integrating its formal coefficients and then putting \(t=\tan u\) gives

$$
\boxed{
\sum_{j\ge0}\frac{u^j}{j!}
\int y^j\,d\sigma(y)
=
\mathfrak m_\sigma(\cos u)^{-1/2}.
}
\tag{10}
$$

This follows from the Meixner–Pollaczek generating function in the original variable and normalization; no probability normalization has been imposed. ([DLMF][1])

Hence

$$
\det\mathsf J_n^{(a)}
=
\mathfrak m_\sigma^{\,n+1}\Delta_n(a).
$$

At each cutoff, the difference in dimensions in (9) is \(g\). Its mass term is therefore \(g\log\mathfrak m_\sigma\), whose four-cutoff return is exactly zero. Substituting the four values of \(L\) yields precisely

$$
\boxed{
\mathcal R
\left[
\log\det\mathsf J_{M_N}^{(q')}
-\log\det\mathsf J_L^{(q-v)}
\right]
=\log\mathcal A_{k,v}.
}
\tag{11}
$$

For reference, the first normalized moments are

$$
1,\quad \frac12,\quad \frac74,\quad
\frac{139}{8},\quad \frac{5473}{16}
$$

in even orders \(0,2,4,6,8\). Odd orders vanish. All later moments in (2) are obtained by the same exact power series.

### The complete finite remainder

The retained source bound is

$$
B_{\mathrm{KF49}}
=
2m\Lambda_k
+2s_k\log\kappa_k^*
+2B_k^{\mathrm{ang}}
+2\sum_NE_N^*,
$$

where

$$
B_k^{\mathrm{ang}}
=
v\log\kappa_k^*
+2v\log(1/\varepsilon_k),
$$

$$
E_N^*=(N+1)\log M_{N-v}+J_{N-v},
\qquad
J_D=(D+1)\log^+(1/|(-i)^v\mu_v/v!|).
\tag{12}
$$

These are the original finite interpolation, low-angle, and exterior constants in KF37–49. The graph error \(E_N^{\mathrm{vol}}\) is zero at both low cutoffs and is the full CG24 bound at the high cutoffs.

Thus the error in (3) is explicitly

$$
\boxed{
\mathcal E_k
=
B_{\mathrm{KF49}}
+\sum_N
\left[
E_N^{\mathrm{vol}}
+(M_N+1)E_{\chi'}
+(L+1)E_{d,N}
\right].
}
\tag{13}
$$

Every term is a previously specified finite source quantity. Since

$$
M_N=O(q),\quad L+1\le q+1,\quad m=O(k),
$$

their proved orders give

$$
\mathcal E_k=O_{h,A}(q\log(q+2)).
$$

This is a bound around a finite determinant formula. It is not a claim that the unresolved invariant covariance already has a limiting coefficient.

## 3. Every original invariant row can be calculated on one fixed circle

The existing CGP sampling construction works near the unit circle after imposing conductor-pole cancellation conditions on a smaller row space. The following construction keeps **all** rows. Its circle is chosen inside a certified zero-free neighborhood of the original symbol.

Write

$$
E_A(w)=\sum_{j=1}^{J}a_je^{b_jw},
\qquad
v=\operatorname{ord}_0E_A,
\qquad
\mu_v=E_A^{(v)}(0)\ne0.
$$

Set

$$
A_1=\sum_j|a_j|,
\qquad B_A=\max(1,\max_j|b_j|),
\qquad
C_v=\frac{A_1B_A^v}{|\mu_v|}.
$$

Define

$$
R_A=
B_A^{-1}
\min\left(1,\frac{v+1}{2eC_v}\right),
\qquad
s=R_A/2,\qquad a=s/2.
\tag{14}
$$

These depend on the fixed actual conductor, not on \(k\).

Taylor’s formula gives, for \(|w|\le R_A\),

$$
\left|
\frac{v!E_A(w)}{\mu_vw^v}-1
\right|
\le
C_v\frac{B_A|w|e^{B_A|w|}}{v+1}
\le\frac12.
$$

Therefore

$$
\boxed{
|E_A(w)/w^v|\ge\frac{|\mu_v|}{2v!}.
}
\tag{15}
$$

At \(w=0\), the quotient denotes its removable value.

Let

$$
R_k=k\sqrt{\delta^2+\gamma^2},
\qquad B_k=4+R_k,
\qquad n_E=16k-48.
$$

For every coefficient-unit row in the original invariant row space,

$$
e^{-c'w}F_z(w)
=\sum_\alpha z_\alpha e^{(\beta_\alpha-c')w}
$$

vanishes through order \(v-1\), has at most \(n_E\) nonzero terms, and

$$
|\beta_\alpha-c'|\le B_k.
$$

Hence

$$
\left|
w^{-v}e^{-c'w}F_z(w)
\right|
\le
\frac{\sqrt{n_E}B_k^v}{v!}e^{B_k|w|}.
$$

For \(|t|\le s\le1/2\),

$$
|w(t)|\le\operatorname{arctanh}s<R_A.
$$

Combining this with (15),

$$
\boxed{
|H_z(t)|\le A_k\|z\|_2,
\qquad
A_k=
\frac{2\sqrt{n_E}B_k^v}{|\mu_v|}
(1-s^2)^{-1/4}
e^{B_k\operatorname{arctanh}s}.
}
\tag{16}
$$

Thus \(H_z\) is holomorphic on the entire disk \(|t|\le s\), for every original row, and

$$
\log A_k=O_{h,A}(k+\log(k+2)).
$$

No zero of \(E_A\) outside this disk is omitted from the function: it remains encoded in its Taylor coefficients.

### Exact aliasing formula

Put

$$
\rho_n=\sqrt{\frac{n!}{(1/2)_n}},
\qquad
(W_N)_{z,n}
=
\frac{\rho_n}{\sqrt{\mathfrak m_\sigma}}[t^n]H_z(t),
\quad 0\le n\le D_N.
$$

Define

$$
B_N=
\max\left\{
1,\,
\frac{A_k}{\sqrt{\mathfrak m_\sigma}}
\left(\sum_{n=0}^{D_N}\rho_n^2s^{-2n}\right)^{1/2}
\right\}.
\tag{17}
$$

Then \(\|W_N\|\le B_N\).

For \(T>D_N\), let \(\omega_T=e^{2\pi i/T}\), and calculate

$$
[t^n]^{[T]}H_z
=
\frac{a^{-n}}T
\sum_{\ell=0}^{T-1}
H_z(a\omega_T^\ell)\omega_T^{-n\ell}.
$$

Writing \(H_z(t)=\sum c_jt^j\), the exact discrete Fourier identity is

$$
[t^n]^{[T]}H_z-c_n
=
\sum_{j\ge1}c_{n+jT}a^{jT}.
$$

Since \(a/s=1/2\), Cauchy’s coefficient estimate yields the full matrix bound

$$
\boxed{
\|W_N^{[T]}-W_N\|
\le
B_N\frac{2^{-T}}{1-2^{-T}}.
}
\tag{18}
$$

The bound holds simultaneously on every linear combination of the original rows.

## 4. The lower-root projection has an explicit precision budget

Let \(a_*\) be the actual leading biform conductor coefficient from OCF5, and put

$$
\kappa_A=A_1/|a_*|.
$$

The full original strip reduction has path length at most \(10k\). The source consequently proves

$$
C_N\succeq\lambda_N I_r,
$$

where a valid finite choice is

$$
\boxed{
\lambda_N
=
\min\left\{
1,\,
\left[
M_{D_N}^2 B_{\mathrm{val}}q\kappa_A^{20k}
\right]^{-1}
\right\},
}
\tag{19}
$$

$$
B_{\mathrm{val}}
=
q\mathfrak m_\sigma
\left(\frac{2q+R_k}{2\delta}\right)^{2(q-1)}.
$$

Here \(M_{D_N}\ge1\) is the unchanged full-conductor forward bound. In particular,

$$
\log(1/\lambda_N)=O_{h,A}(q\log(q+2)).
$$

This is the lower bound **after** the full lower-root projection, not the easier unprojected strip bound.

For the lower-root matrix itself, the complete lower Lagrange polynomials give

$$
\sigma_{\min}(E_N)\ge s_E,
$$

with

$$
\boxed{
s_E=
\left[
q'\mathfrak m_\sigma
\left(\frac{2q'+R_-}{2\delta}\right)^{2(q'-1)}
\right]^{-1/2},
\qquad
R_-=(k-8)\sqrt{\delta^2+\gamma^2}.
}
\tag{20}
$$

Indeed the coefficient columns of those interpolation polynomials form a right inverse of \(E_N\); the sum of their squared Gamma norms bounds its squared operator norm.

If

$$
\|\widehat E_N-E_N\|\le\epsilon_E\le s_E/2,
$$

the full row rank persists, and

$$
\boxed{
\|\widehat P_N-P_N\|\le\epsilon_E/s_E,
}
\tag{21}
$$

where \(\widehat P_N\) is formed using every row of \(\widehat E_N\). The equal-rank principal-angle proof in FI5 establishes the constant-one estimate (21).

Choose \(0<\theta\le1/2\), and set

$$
\boxed{
T_N=
\max\left\{
D_N+1,\,
\left\lceil
\log_2\frac{32B_N^2}{\theta\lambda_N}
\right\rceil
\right\}.
}
\tag{22}
$$

Require the additional row-evaluation error to satisfy

$$
\|\widehat W_N-W_N^{[T_N]}\|
\le\frac{\theta\lambda_N}{16B_N},
$$

and require

$$
\boxed{
\|\widehat E_N-E_N\|
\le
\frac{\theta\lambda_Ns_E}{32B_N^2}.
}
\tag{23}
$$

Equation (18) gives

$$
e_N:=\|\widehat W_N-W_N\|
\le\frac{\theta\lambda_N}{8B_N}.
$$

Therefore

$$
\begin{aligned}
\|\widehat W_N\widehat P_N\widehat W_N^*
-W_NP_NW_N^*\|
&\le (2B_N+e_N)e_N\\
&\quad +(B_N+e_N)^2\|\widehat P_N-P_N\|\\
&<\theta\lambda_N.
\end{aligned}
$$

Thus

$$
\boxed{
(1-\theta)C_N
\preceq\widehat C_N
\preceq(1+\theta)C_N.
}
\tag{24}
$$

The final products and inverses can be performed exactly on Gaussian-rational centers, or their additional arithmetic error must be included in the displayed margin. A floating-point midpoint is not by itself a certificate.

For \(\theta=1/(4q)\), the four correlated determinant errors satisfy

$$
\boxed{
|\mathcal R\log\det\widehat C_N
-\mathcal R\log\det C_N|
\le
2r\log\frac{4q+1}{4q-1}
\le\frac{4r}{4q-1}.
}
\tag{25}
$$

Equations (3) and (25) prove (4).

Because \(s,a\) are fixed by the actual conductor,

$$
\log B_N=O_{h,A}(q),
\qquad
\log(1/s_E)=O_h(q\log q).
$$

It follows directly from (22)–(23) that the sample count and logarithmic absolute tolerances have the claimed \(O_{h,A}(q\log q)\) sizes.

These are tolerances on the **assembled original row functions and lower-root evaluations**. Additional uncertainty in a period, physical unit, or selected invariant frame must be propagated into them; the theorem does not invent such input enclosures.

### Evaluating the removable quotient without cancellation

The samples need not be calculated by dividing two tiny raw values. Write

$$
w^{-v}e^{-c'w}F_z(w)=\sum_{\ell\ge0}f_{z,\ell}w^\ell,
\qquad
w^{-v}E_A(w)=\sum_{\ell\ge0}g_\ell w^\ell.
$$

Their exact coefficients are

$$
f_{z,\ell}
=
\frac{\sum_\alpha z_\alpha(\beta_\alpha-c')^{v+\ell}}
{(v+\ell)!},
\qquad
g_\ell=\frac{\mu_{v+\ell}}{(v+\ell)!}.
$$

The quotient coefficients satisfy

$$
\boxed{
u_{z,0}=f_{z,0}/g_0,\qquad
u_{z,n}
=
g_0^{-1}
\left(
f_{z,n}-\sum_{j=1}^ng_ju_{z,n-j}
\right).
}
\tag{26}
$$

All zero coefficients below order \(v\) are enforced by the original algebraic constraints.

For example, truncation after \(\ell=L-1\) has the explicit numerator tail

$$
\left|
\sum_{\ell\ge L}f_{z,\ell}w^\ell
\right|
\le
\sqrt{n_E}\|z\|_2 B_k^v
\frac{(B_k|w|)^Le^{B_k|w|}}{(v+L)!},
\tag{27}
$$

and the analogous denominator tail replaces \(\sqrt{n_E}B_k^v\) by \(A_1B_A^v\). The denominator floor is already (15).

Thus the new precision statement includes a convergent, guarded calculation of the actual samples; it does not assume that a black-box evaluation of \(F_z/E_A\) is stable.

## 5. An algebraic route uses the actual invariant rows as initial data

There is also a finite coefficient calculation of the same projected covariance, with no Cauchy sampling.

Let

$$
\ell_z[\eta]
=
[\eta(\partial_w)\chi'(\partial_w)G_z(w)]_{w=0},
$$

and write

$$
u_n(S')
=
\mathcal U_A(S^n)(S')
=
\sum_j a_jd_j(S')(S'+b_j)^n.
$$

The source’s full relation identity proves

$$
\ell_z[u_n]=0.
$$

Moreover,

$$
\deg u_n=n+g,
\qquad
[S'^{n+g}]u_n
=
\mu_v\binom{q+n}{v}\ne0.
$$

Hence the actual moments

$$
b_{z,j}=\ell_z[S'^j]
$$

satisfy the exact triangular recurrence

$$
\boxed{
b_{z,n+g}
=
-\frac{
\sum_{j=0}^{n+g-1}[S'^j]u_n\,b_{z,j}
}{
\mu_v\binom{q+n}{v}
}.
}
\tag{28}
$$

The first \(g\) columns are precisely the original \(A_R\), with its low-constraint elimination. No free initial row is inserted.

Let \(\mathsf B_N=[b_{z,j}]_{j=0}^{M_N}\). Multiplication by the full \(\chi'\) has a coefficient matrix \(J_{\chi',N}\) into the lower Gamma-orthonormal frame, satisfying

$$
J_{\chi',N}^*J_{\chi',N}
=\mathsf H_{M_N}[\chi'],
$$

$$
P_N
=
J_{\chi',N}
\mathsf H_{M_N}[\chi']^{-1}
J_{\chi',N}^*,
\qquad
\mathsf B_N=W_NJ_{\chi',N}.
$$

Therefore

$$
\boxed{
C_N
=
\mathsf B_N\mathsf H_{M_N}[\chi']^{-1}\mathsf B_N^*.
}
\tag{29}
$$

This is a factorization of the **full lower-root projection**, not its replacement by the identity.

It gives a useful complete bordered determinant. Set

$$
\mathbb H_N=
\begin{pmatrix}
\mathsf H_{M_N}[\chi']&\mathsf B_N^*\\
\mathsf B_N&0
\end{pmatrix},
$$

$$
\mathsf R_N
=
\mathsf U_N^*
\mathsf H_{M_N}[\chi']
\mathsf U_N,
$$

where \(\mathsf U_N\) contains all relation columns

$$
u_0,u_1,\ldots,u_L,
$$

and

$$
\tau_N=\prod_{n=0}^{L}\mu_v\binom{q+n}{v}.
$$

Empty products and empty relation determinants equal one.

The complete graph basis has determinant \(\tau_N\). Block elimination gives

$$
(-1)^r\det\mathbb H_N
=
\det\mathsf H_{M_N}[\chi']\det C_N>0.
$$

Consequently

$$
\boxed{
\left|
\mathcal K_k
-
\mathcal R\log
\left[
\frac{
|\tau_N|^2(-1)^r\det\mathbb H_N
}{
\det\mathsf R_N
}
\right]
\right|
\le B_{\mathrm{KF49}}.
}
\tag{30}
$$

Equation (30) retains the **original nonideal relation operator \(\mathcal U_A\)**. It requires no passage from its graph to the outer ideal. In particular, the large source determinant cancels exactly inside the bordered formula; the complete relation Gram in the denominator remains.

Equations (28)–(30) and the all-row Cauchy construction are two independent ways to calculate the same actual invariant covariance. Their equality supplies an exact cross-check for an implementation.

## 6. What the rational quotient does to these actual rows

The allowed quotient must be carried through the lower-root projection before any minimization. That transport can be written explicitly.

Let \(\mathcal D\) be an admitted rational denominator, and let \(U_{\mathcal D}\) be its original root-value numerator map. Put

$$
R_{\mathcal D}=C_AU_{\mathcal D}.
$$

On the MF degree guard, this has full column rank. Choose the exact coefficient left inverse

$$
L_{\mathcal D}
=
(R_{\mathcal D}^*R_{\mathcal D})^{-1}R_{\mathcal D}^*,
$$

and define

$$
B_{\mathcal D}
=
\widetilde ZU_{\mathcal D}L_{\mathcal D},
\qquad
Z_{\mathcal D}=\widetilde Z-B_{\mathcal D}C_A.
\tag{31}
$$

Then

$$
Z_{\mathcal D}U_{\mathcal D}=0,
$$

so \(Z_{\mathcal D}\) factors through the actual \(\pi_{\mathcal D}\). Here \(\widetilde Z=ZS_k^{\mathsf T}\) is the full upper-root row matrix. The coefficient left inverse in (31) is used only to specify the map; it is not declared an isometry of a native metric.

Each row of \(C_A\), at a lower root \(\eta\), has exponential numerator

$$
E_A(w)e^{\eta w}.
$$

Therefore

$$
G_{z_{\mathcal D}}(w)
=
G_z(w)-\sum_\eta(B_{\mathcal D})_{z\eta}e^{\eta w},
$$

and its Gamma row is exactly

$$
\boxed{
W_{N,\mathcal D}=W_N-B_{\mathcal D}E_N.
}
\tag{32}
$$

Since \(E_NP_N=0\),

$$
\boxed{
W_{N,\mathcal D}P_NW_{N,\mathcal D}^*
=
W_NP_NW_N^*.
}
\tag{33}
$$

This is the explicit original-row consequence of the quotient. It preserves every lower-root constraint. It also shows why choosing another admitted pole family does not by itself assign a new value to the remaining projected covariance: its projected Gram is exactly the same.

The unprojected Gram does change:

$$
W_{N,\mathcal D}W_{N,\mathcal D}^*
\ne W_NW_N^*
$$

in general. Therefore one cannot replace the strip-angle denominator by the new unprojected Gram without carrying that change separately.

At a resultant zero or observation-rank drop, (31) is not used. The PC7 and PC27 exact kernel sequences, and PC32’s positive-rank determinant identity, are the applicable maps. The new off-boundary sampling estimate is not asserted through a vanishing observed fraction.

## 7. An exact example retaining an interior conductor pole and the full projection

The following is a finite complex-conductor illustration of the new mechanism, **not** a native xi packet.

Take

$$
\mathcal T_Af(S')=f(S'+4i)-f(S'),
$$

$$
\chi'(S')=S'(S'-1),
$$

$$
\chi(S)=S(S-1)(S-4i)(S-1-4i).
$$

Choose the upper row

$$
F_z(w)=e^w-1.
$$

Then

$$
E_A(w)=e^{4iw}-1,\qquad
G_z(w)=\frac{e^w-1}{e^{4iw}-1}.
$$

Its first coefficients are

$$
G_z(w)
=
-\frac i4
+\left(-\frac12-\frac i8\right)w
+\left(-\frac14+\frac{7i}{24}\right)w^2+\cdots.
$$

At \(N=3\), the lower Gamma degree is \(2\). In the original Gamma-orthonormal frame,

$$
W=
\frac1{\sqrt{\mathfrak m_\sigma}}
\left(
-\frac i4,\,
\sqrt2\left(-\frac18+\frac i2\right),\,
\sqrt{\frac23}\left(\frac12-\frac{11i}{24}\right)
\right),
$$

and the two original lower-root evaluation rows are

$$
E=
\frac1{\sqrt{\mathfrak m_\sigma}}
\begin{pmatrix}
1&0&-1/\sqrt6\\
1&-i\sqrt2&-\sqrt{3/2}
\end{pmatrix}.
$$

Directly,

$$
WW^*=\frac{389}{432\mathfrak m_\sigma}.
$$

The lower-root ideal is spanned by

$$
\chi'(iy)=-y^2-iy,
$$

whose squared norm is

$$
\|\chi'\|_\sigma^2=\frac94\mathfrak m_\sigma.
$$

The actual functional value is

$$
L_z[\chi']=\ell_z[1]=G_z''(0)-G_z'(0)=\frac{17i}{24}.
$$

Thus

$$
\boxed{
WP_IW^*
=
\frac{289}{1296\mathfrak m_\sigma},
\qquad
\frac{WP_IW^*}{WW^*}
=
\frac{289}{1167}.
}
\tag{34}
$$

The generating function has an actual interior pole at

$$
t=i\tanh(\pi/2),
$$

because \(w(t)=\pi/2\), the denominator vanishes there, and the numerator does not. The fixed circle in (14) lies inside that pole and computes this full row without deleting it.

Equation (34) independently agrees with the algebraic formula (29), where the weighted source Gram has the single entry \(9\mathfrak m_\sigma/4\). Omitting the lower-root projection would replace \(289/1296\) by \(389/432\), a different covariance.

## 8. Consequences for the outstanding coefficient

The complete finite approximation is now

$$
\boxed{
\frac{\mathcal K_k}{kq}
=
\frac{
\log\mathcal A_{k,v}
+\mathcal R\log\det\widehat C_N
}{kq}
+
O_{h,A}\!\left(\frac{\log(q+2)}k\right),
}
\tag{35}
$$

with the finite error given by (13), (22)–(25), rather than an unspecified asymptotic remainder.

The full invariant covariance is increasing with the allowed source degree. Thus

$$
\mathcal R\log\det C_N\le0.
$$

The original kernel metric decreases with the source degree, so

$$
\mathcal K_k\ge0.
$$

Equations (3) and (11) therefore also give the finite upper bound

$$
\boxed{
0\le\mathcal K_k
\le\log\mathcal A_{k,v}+\mathcal E_k.
}
\tag{36}
$$

Using the separately established outer-volume limit would yield

$$
\limsup\frac{\mathcal K_k}{kq}\le16C_\partial.
$$

That is only an upper bound; it is not the missing coefficient.

The useful advance is more specific than that coarse bound. **The canonical kernel allocation now has an all-row, full-projection finite calculation with an \(O(q\log q)\) physical comparison error and an independently adjustable numerical determinant error.** There is no complementary pole-row determinant left to estimate. The exact quotient transport is (31)–(33), and the original nonideal relation calculation is (28)–(30).

The actual numerical sequence \(\mathcal R\log\det C_N/(kq)\), or an analytic asymptotic for those same invariant rows, remains to be evaluated. No complex-current phase is assigned by these positive Gram calculations. The exact auxiliary checks accompanying this proof verify the finite algebra. They do not evaluate the original native period-dependent covariance sequence.

### References

Koornwinder, T. H., Wong, R., Koekoek, R., Swarttouw, R. F., & Reinhardt, W. P. (n.d.). Orthogonal polynomials. In *NIST Digital Library of Mathematical Functions* (Chapter 18). Equations 18.22.8 and 18.23.7 supply the recurrence and generating-function conventions used above. ([DLMF][2])

Split-Zero research programme. (2026a, September 21). [*ACTUAL_KERNEL_FILTRATION_AND_GRAPH.tex*, KF37–55](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/0fd693c844aad9117e30ec447c59864a28af10f3/workbenches/splitzero-tandem/continuations/20260921-native-spectral-real-pair/003/ACTUAL_KERNEL_FILTRATION_AND_GRAPH.tex#L270). *Zeta-function research reader*, pinned original proof edition. The complete finite source comparison, relation graph, and fixed-frame determinant transport are the inherited inputs to (7) and (30).

Split-Zero research programme. (2026b, September 21). [*COMPLETE_CONDUCTOR_GRAPH_METRIC.tex*, CG18–32](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/0fd693c844aad9117e30ec447c59864a28af10f3/workbenches/splitzero-tandem/continuations/20260921-native-spectral-real-pair/003/COMPLETE_CONDUCTOR_GRAPH_METRIC.tex#L113). Same pinned original proof edition. The full-form errors and the post-projection lower bound are retained with their original finite domains.

[1]: https://dlmf.nist.gov/18.23.E7 "https://dlmf.nist.gov/18.23.E7"
[2]: https://dlmf.nist.gov/18 "https://dlmf.nist.gov/18"


# Additional finite proofs and exact source identifications

## FI1. The sharper comparison on the identical source

The original simple-quartet domain has multiplicity parameter $m_0=1$, $k\equiv1\pmod4$, $q=(k+1)^2$, $c=k/2$, the unchanged divisor $h$, and arithmetic measure $d\mu_k=w_h^{*k}(y)\,dy$, $w_h(y)=|(2\xi/h)(1/2+iy)|^2/(2\pi)$. This is precisely NG1 with $m_0=1$, not a comparison with a different arithmetic model. In [NG1–3, lines 27–72](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/5992ad50c0f2a06921f1fcaded7b4e38097c0739/workbenches/splitzero-tandem/continuations/20260920-original-kernel-mixed-determinants/providers/NATIVE_GAUSSIAN_TRANSFER.tex#L27), put $M=21+4m_0=25$ and use its original positive full-mass constants $a_k,A_k$ from CAI16. Then, simultaneously for every original polynomial degree $N\le2q$,
\[
 \ell_{k,2q}\|p\|_\sigma^2\le\|p\|_{\mu_k}^2\le u_k\|p\|_\sigma^2,
 \quad \ell_{k,2q}=\frac{a_k}{[1+4(2q+25)^2]^{25}},\quad u_k=A_k,
 \quad \Lambda_k=\log\frac{u_k}{\ell_{k,2q}}=O_h(k+\log(q+2)).
 \tag{FI1}
\]
The polynomial is the full original polynomial evaluated at $c+iy$. Its roots and its coefficient frame are unaltered. The different lower physical center $c'=c-4$ enters only in the subsequent KF conductor transport, whose existing bounds remain.

Here is the exact passage from FI1 to an arbitrary fixed target subspace. Let $T_N:\mathcal P_N\to V$ be the original onto coefficient map; write $G_N^{\mu}$ and $G_N^\sigma$ for its attained metrics. The minimum of a positive definite finite-dimensional quadratic form over the closed affine fibre $T_Np=x$ exists: decompose the source into $\ker T_N$ and its orthogonal complement, on which $T_N$ is an isomorphism onto $V$. Applying FI1 to every element of that same fibre and then taking infima gives
\[
 \ell_{k,2q}G_N^\sigma\preceq G_N^\mu\preceq u_kG_N^\sigma.
 \tag{FI2}
\]
For every fixed injective rank-$t$ frame $J:\mathbb C^t\to V$, congruence by $J$ preserves these inequalities. Congruence again by $(J^*G_N^\sigma J)^{-1/2}$ puts every eigenvalue in $[\ell_{k,2q},u_k]$. Multiplying the eigenvalues proves
\[
 t\log\ell_{k,2q}\le d_N:=\log\frac{\det(J^*G_N^\mu J)}{\det(J^*G_N^\sigma J)}\le t\log u_k.
\]
There are exactly two positive and two negative signs in $\mathcal R$. Thus the largest possible value of $\mathcal R d_N$ is $2t\log u_k-2t\log\ell_{k,2q}$ and the smallest is its negative. Consequently
\[
 |\mathcal R d_N|\le2t\Lambda_k.\tag{FI3}
\]
Use the original frame $J=I_K$, with $t=m=8k-16$. This proves the sharper MR21/JM25 receiver directly from the same source. It changes only the width term in [KF49, lines 354–363](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/0fd693c844aad9117e30ec447c59864a28af10f3/workbenches/splitzero-tandem/continuations/20260921-native-spectral-real-pair/003/ACTUAL_KERNEL_FILTRATION_AND_GRAPH.tex#L354):
\[
 B_{\rm KF49}^{\rm sharp}=2m\Lambda_k+2s_k\log\kappa_k^*+2B_k^{\rm ang}+2\sum_NE_N^*.
 \tag{FI4}
\]
Every original low intersection, angle, exterior bound, physical mass and finite guard stays in FI4. In particular $E_N^*=(N+1)\log M_{N-v}+(N-v+1)\log^+(1/|(-i)^v\mu_v/v!|)$ is unchanged. Adding the [CG24 full-volume error, lines 158–192](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/0fd693c844aad9117e30ec447c59864a28af10f3/workbenches/splitzero-tandem/continuations/20260921-native-spectral-real-pair/003/COMPLETE_CONDUCTOR_GRAPH_METRIC.tex#L158) and the [CG18–20 scalar errors, lines 113–136](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/0fd693c844aad9117e30ec447c59864a28af10f3/workbenches/splitzero-tandem/continuations/20260921-native-spectral-real-pair/003/COMPLETE_CONDUCTOR_GRAPH_METRIC.tex#L113) gives exactly equation (13), with equation (12) read as FI4. Its order is $O_{h,A}(q\log(q+2))$: the new first term is $O_h(k^2+k\log(q+2))=O_h(q)$ and all retained terms have the stated $O(q\log(q+2))$ bound. The former width of order $k\log^2q$ would not prove this sharper remainder.

## FI2. Original strip rows, full upper-root rows and weighted functionals

Let $S_k:\mathbb C^{n_E}\to\mathbb C^q$ insert zeros in the original conductor pivot positions, in the lexicographic coefficient order of [OCF2–8, lines 34–163](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/5992ad50c0f2a06921f1fcaded7b4e38097c0739/workbenches/splitzero-tandem/continuations/20260920-original-kernel-mixed-determinants/providers/ORIGINAL_CONDUCTOR_STRIP_FRAME.tex#L34). Thus $S_k^*S_k=I$, $n_E=16k-48$, and a strip row $z$ means the full upper-root row $\widetilde z=zS_k^{\mathsf T}$. Transposition here specifies the complex-linear evaluation row; $S_k$ is a real zero-insertion matrix, so its transpose also equals its adjoint. In particular $\|\widetilde z\|_2=\|z\|_2$. The symbol in every equation (1)–(34) is
\[
 F_z(w)=\sum_{\alpha=1}^q\widetilde z_\alpha e^{\beta_\alpha w}.
 \tag{FI5}
\]
The row basis is obtained by the exact CG29–30 low-degree elimination. That elimination says $\sum_\alpha\widetilde z_\alpha\beta_\alpha^j=0$ for $0\le j<v$. It therefore makes $F_z/E_A$ holomorphic at zero. It does not replace the physical norm by the Euclidean row norm. Applying $(ZZ^*)^{-1/2}$ to all rows is the same fixed invertible row map at all cutoffs, and its determinant contribution $-\log\det(ZZ^*)$ cancels because $1+1-1-1=0$.

Define two distinct complex-linear functionals:
\[
 L_z(f)=[f(\partial_w)G_z(w)]_{w=0},\qquad
 \ell_z(\eta)=L_z(\chi'\eta),\qquad G_z=F_z/E_A.
 \tag{FI6}
\]
The first has domain the unweighted lower polynomial space; the second has domain the weighted coefficient polynomial space. The Taylor identity $E_AG_z=F_z$ implies, first on a monomial and then by linearity,
\[
 L_z(\mathcal T_Ap)=\sum_\alpha\widetilde z_\alpha p(\beta_\alpha).
 \tag{FI7}
\]
To verify it explicitly, $\mathcal T_A=e^{b_1\partial}a_1+\cdots+e^{b_J\partial}a_J$. Thus $(\mathcal T_Ap)(\partial_w)G_z|_0=p(\partial_w)(E_AG_z)|_0=p(\partial_w)F_z|_0$. Only finitely many derivatives occur for each polynomial.

Let $D=N-v$ and $M=N-v-q'=L+g$. In the lower source use the exact orthonormal polynomials
\[
 \psi_n(S')=\frac{p_n(-i(S'-c'))}{\sqrt{\mathfrak m_\sigma n!(1/2)_n}},\quad0\le n\le D.
\]
Their squared norm on $S'=c'+iy$ is one. Substituting the complete generating function gives $L_z(\psi_n)=\rho_n[t^n]H_z/\sqrt{\mathfrak m_\sigma}$, exactly the row $W_N$ in the retained text. Let $E_N$ evaluate these polynomials at every lower root. The roots are distinct on the original simple-quartet domain, and $D\ge q'-1$, so interpolation proves $\operatorname{rank}E_N=q'$. Its kernel is exactly $\chi'\mathcal P_M$: a degree-at-most-$D$ polynomial vanishes at all $q'$ distinct roots if and only if it is divisible by their full monic product. The coefficient map $J=J_{\chi',N}$ of $\eta\mapsto\chi'\eta$ has this range, is injective, and satisfies $J^*J=\mathsf H_M[\chi']$. Consequently
\[
 P_N=J(J^*J)^{-1}J^*,\quad W_NJ=\mathsf B_N,
 \quad C_N=\mathsf B_N\mathsf H_M[\chi']^{-1}\mathsf B_N^*.
 \tag{FI8}
\]
Indeed $J(J^*J)^{-1}J^*$ is self-adjoint, fixes the range of $J$, and annihilates its orthogonal complement. This proves equality to the full root-kernel projection, including every original lower root.

The identity $\mathcal T_A(\chi S^n)=\chi'u_n$ and FI7 give $\ell_z(u_n)=0$, because $\chi(\beta_\alpha)=0$ at every upper root. Since $u_n$ has exact degree $g+n$ and leading coefficient $a_n=\mu_v\binom{q+n}{v}\ne0$, coefficient comparison gives equation (28). Inductively it determines every $b_{z,j}$ for $j\ge g$ from the actual first $g$ values, one new coefficient at a time. Conversely, a functional defined by those initial values and that recurrence annihilates every $u_n$. The $u_0,\ldots,u_L$ are linearly independent by their distinct leading degrees, and division by their successive leading terms expresses every degree-at-most-$M$ polynomial uniquely as a degree-below-$g$ remainder plus their complete span. Thus the recurrence gives exactly the original quotient functional, not merely necessary constraints. All relation coefficients, including its nonideal lower terms, are retained.

The degree-triangular full basis $[1,S',\ldots,S'^{g-1},u_0,\ldots,u_L]$ has determinant $\tau_N=\prod_{n=0}^La_n$. Its Gram determinant is $|\tau_N|^2\det\mathsf H_M[\chi']$. Taking the Schur complement of the full relation Gram $\mathsf R_N$ proves $\det Q_N^U=|\tau_N|^2\det\mathsf H_M[\chi']/\det\mathsf R_N$. Taking the Schur complement of the upper-left block in $\mathbb H_N$ proves $(-1)^r\det\mathbb H_N=\det\mathsf H_M[\chi']\det C_N$. Combining the two identities with CG31 and FI4 proves equation (30), including $L=-1$ under the empty determinant convention.

In the auxiliary example the value is $L_z(\chi')=\ell_z(1)=17i/24$. The expression $\ell_z(\chi')$ would instead insert the lower root polynomial twice. The covariance and the displayed value in equation (34) use $L_z(\chi')=\ell_z(1)$.


# Full-row finite certificate and typed quotient

## FI3. Positivity and exact scalar cancellation

In the retained physical convention, the monic recurrence and norms are $p_{n+1}=yp_n-n(n-1/2)p_{n-1}$ and $\|p_n\|_\sigma^2=\mathfrak m_\sigma n!(1/2)_n$, with $\mathfrak m_\sigma=\sqrt{2\pi}$. These follow from the original Meixner–Pollaczek equations [DLMF18.22.8](https://dlmf.nist.gov/18.22.E8) and [18.23.7](https://dlmf.nist.gov/18.23.E7), by T. H. Koornwinder, R. Wong, R. Koekoek, R. F. Swarttouw and W. P. Reinhardt; the author TeX equations have been read. Orthogonality gives $\int p_n\,d\sigma=0$ for $n>0$. Integrating the generating function coefficient by coefficient therefore gives
\[
 (1+t^2)^{-1/4}\sum_{j\ge0}\frac{(\arctan t)^j}{j!}\int y^j\,d\sigma=\mathfrak m_\sigma.
\]
This is a formal power series identity: at each degree it uses only finitely many moments. Substitute $t=\tan u$ formally; $(1+\tan^2u)^{1/4}=(\cos u)^{-1/2}$, proving equation (10). The constant term is the full physical mass. Each normalized coefficient $\nu_j$ is rational because $\cos u$ has rational coefficients and the unique power series with constant term one satisfying $F^2\cos u=1$ is obtained by rational recursion. For every $a,n\ge0$ and nonzero vector $x$,
\[
 \sum_{i,j=0}^n\overline{x_i}\nu_{2a+i+j}x_j
 =\mathfrak m_\sigma^{-1}\int y^{2a}\left|\sum_{j=0}^nx_jy^j\right|^2d\sigma>0.
 \tag{FI9}
\]
The integrand is positive outside the finite zero set of a nonzero polynomial and the Gamma density is positive everywhere. Thus every $\Delta_n(a)$ in equation (2) is a positive rational number.

For clarity, put $J(L)=\det\mathsf J_{L+g}^{(q')}/\det\mathsf J_L^{(q-v)}$. The mass exponent is $(L+g+1)-(L+1)=g$, also at $L=-1$ with the empty convention. The exact product $J(-1)J(0)/(J(q-1)J(q))$ therefore has mass exponent zero and is
\[
 \frac{\Delta_{g-1}(q')\Delta_g(q')\Delta_{q-1}(q-v)\Delta_q(q-v)}{\Delta_{q+g-1}(q')\Delta_{q+g}(q')\Delta_0(q-v)}.
 \tag{FI10}
\]
The largest moment index is $2q'+2(q+g)=4q-2v$; the second family also reaches $2(q-v)+2q=4q-2v$. The unit-modulus triangular basis change in equation (9) retains the exact complex phase $i^j$ at every degree. The factor $|a_A|^{2(L+1)}$ cancels the full relation Gram's factor, rather than a monic replacement of $d_A$.

The finite error statement uses the actual simple-quartet five-orbit domain of KF, and the CG6 guards $k\ge29$, $q\ge2v$, $k\ge2v-1$, $4+R_k\le2^{-64}q/8$, $q\ge8\cdot2^{64}$, and $8/(2^{-64}q)+(16+R_k^2)/(2^{-64}q)^2<1/2$. The KF low-angle quantities retain their actual finite nonzero values. The exact determinant identities and the following finite-dimensional certificates hold wherever their displayed degree and rank conditions hold; no small auxiliary fixture is asserted to satisfy these eventual physical comparison guards.

## FI4. A post-projection lower bound with every original root

Let $N_k$ and $M_A$ be the actual OCF reduction and conductor multiplication maps. Write $C_A=M_A^{\mathsf T}:\mathbb C^q\to\mathbb C^{q'}$. Then $N_kM_A=0$ and $N_kS_k=I$. Set $\kappa_A=A_1/|a_*|\ge1$. In every recursive OCF elimination step, a nonleading shift $(r-r_*,s-s_*)$ strictly decreases the integer potential $9i+j$: if $r<r_*$ its change is at most $-9+8=-1$, and if $r=r_*$ its change is negative because $s<s_*$. The potential on the $k$ square ranges from zero to $10k$. Hence every branch has length at most $10k$. At each node the sum of absolute child coefficients is $(A_1-|a_*|)/|a_*|\le\kappa_A$. Induction on the remaining depth bounds the final column sum by $\kappa_A^{10k}$, including terminal strip nodes. Therefore
\[
 \|N_k\|_2\le\|N_k\|_F\le\sqrt q\,\kappa_A^{10k}.
 \tag{FI11}
\]

Let $V_N$ evaluate the original upper Gamma polynomial source at all $q$ upper roots, and let $\mathcal T_N$ be the full conductor matrix from that source to the lower Gamma degree-$D$ source. Every upper Lagrange polynomial has the product of $q-1$ original linear factors divided by products of root gaps. All gaps have modulus at least $2\delta$. Multiplication by each factor on the required Gamma degrees has norm at most $2q+R_k$, because $\|yp\|_\sigma\le2(d+1)\|p\|_\sigma$ and all centered roots have modulus at most $R_k$. Starting from $\|1\|_\sigma=\sqrt{\mathfrak m_\sigma}$, the sum of squared norms of these $q$ polynomials is at most $B_{\rm val}$ in equation (19). Their coefficient columns give a right inverse $J_+$ of $V_N$, of norm at most $\sqrt{B_{\rm val}}$. Thus for every full upper row $a$,
\[
 \|aV_N\|_2\ge\|a\|_2/\sqrt{B_{\rm val}}.
 \tag{FI12}
\]
For a row combination $x$ in the fixed orthonormal invariant frame put $z=xZ^\circ$ in strip coordinates, so $\|z\|=\|x\|$. For any row $b\in\mathbb C^{1\times q'}$, FI7 and root addition give
\[
 (W_z-bE_N)\mathcal T_N=(zS_k^{\mathsf T}-bC_A)V_N.
\]
Applying $N_k$ to the transpose of the row on the right before $V_N$ gives $z^{\mathsf T}$ exactly. Hence FI11–12 and the unchanged full conductor bound $\|\mathcal T_N\|\le M_D$ imply
\[
 \|W_z-bE_N\|\ge\frac{\|x\|}{M_D\sqrt{B_{\rm val}}\sqrt q\,\kappa_A^{10k}}.
\]
The minimum over every $b$ equals $\|W_zP_N\|$: it is the distance from $W_z$ to the full row space of $E_N$. Squaring proves equation (19) with its stated minimum with one. This proof controls the covariance after projection.

The same Lagrange proof for the $q'$ lower roots uses their actual centered radius $R_-=(k-8)\sqrt{\delta^2+\gamma^2}$ and gives a right inverse $J_-$ with squared norm at most $q'\mathfrak m_\sigma((2q'+R_-)/(2\delta))^{2(q'-1)}$. From $E_NJ_-=I$ it follows that $\|E_N^*a\|\ge\|a\|/\|J_-\|$, proving exactly the $s_E$ in equation (20).

## FI5. Equal-rank projection perturbation and certified arithmetic

Suppose $\|\widehat E-E\|\le\epsilon_E<s_E$. For every row-space vector $a$, $\|\widehat E^*a\|\ge(s_E-\epsilon_E)\|a\|$, so the row ranks, and thus the kernel dimensions, agree. If $x\in\ker\widehat E$, then $Ex=(E-\widehat E)x$. Since the inverse of $E$ from its row space to its target has norm at most $1/s_E$, the distance of $x$ to $\ker E$ is at most $\epsilon_E\|x\|/s_E$. Thus $\|(I-P)\widehat P\|\le\epsilon_E/s_E$.

Here is the equal-rank step explicitly. For orthonormal frames $U,V$ of the two kernels, take a singular-value decomposition of $U^*V$, and change both frame bases by its unitary factors. The new vectors satisfy $\langle u_i,v_j\rangle=c_i\delta_{ij}$, $0\le c_i\le1$. For $c_i<1$, put $r_i=(v_i-c_i u_i)/\sqrt{1-c_i^2}$. These vectors are orthonormal, perpendicular to all $u_j$, and each pair of projections acts in $\operatorname{span}(u_i,r_i)$ by the matrices
\[
 \begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad
 \begin{pmatrix}c_i^2&c_i\sqrt{1-c_i^2}\\c_i\sqrt{1-c_i^2}&1-c_i^2\end{pmatrix}.
\]
Their difference has eigenvalues $\pm\sqrt{1-c_i^2}$. Terms with $c_i=1$ are common fixed directions, and the complement of both frames contributes zero. Hence the projection difference and either directed cross-projection have the same norm, $\max_i\sqrt{1-c_i^2}$. Consequently
\[
 \|\widehat P-P\|\le\epsilon_E/s_E.\tag{FI13}
\]
This proves the repaired equation (21); no factor three is required.

For $B=B_N\ge1$, $\lambda=\lambda_N\le1$, $0<\theta\le1/2$, the count (22) gives $x=2^{-T}\le\theta\lambda/(32B^2)\le1/64$. Therefore the aliasing error is at most $Bx/(1-x)\le\theta\lambda/(16B)$. Adding the row assembly budget gives $e=\|\widehat W-W\|\le\theta\lambda/(8B)$. The root budget (23) and FI13 give $\|\widehat P-P\|\le\theta\lambda/(32B^2)$. Expansion of the two products yields
\[
 \|\widehat W\widehat P\widehat W^*-WPW^*\|
 \le(2B+e)e+(B+e)^2\frac{\theta\lambda}{32B^2}
 \le\theta\lambda\left(\frac14+\frac1{128}+\frac{289}{8192}\right)
 =\frac{2401}{8192}\theta\lambda<\theta\lambda.
 \tag{FI14}
\]
Here $e/B\le1/16$ was used. This explicit slack can cover additional arithmetic error if enclosed; otherwise perform the finite products and inverses exactly on Gaussian-rational centers. A matrix error at most $\theta\lambda$ is at most $\theta C$ in form order because $C\succeq\lambda I$, proving (24). Each log determinant error is in $[r\log(1-\theta),r\log(1+\theta)]$. The same two-positive/two-negative argument as FI3 gives $2r\log((1+\theta)/(1-\theta))$. For $\theta=1/(4q)$, use $\log(1+x)\le x$ with $x=2/(4q-1)$ to obtain (25).

To state an explicit sample input budget, let the Euclidean norm of the vector error across all $r$ assembled row values at each circle sample be at most $\epsilon_s$. The discrete sum gives a coefficient-vector error at most $a^{-n}\epsilon_s$. Thus its full matrix Frobenius norm is at most
\[
 \frac{\epsilon_s}{\sqrt{\mathfrak m_\sigma}}
 \left(\sum_{n=0}^{D_N}\rho_n^2a^{-2n}\right)^{1/2}.
 \tag{FI15}
\]
Making this at most $\theta\lambda_N/(16B_N)$ proves the row assembly requirement. For entrywise root evaluation enclosures of radius $\epsilon_{\rm entry}$, the sufficient operator error is $\sqrt{q'(D_N+1)}\epsilon_{\rm entry}$, by the Frobenius bound. These statements concern the original values, so errors in the conductor and invariant coefficients must be included in them.

## FI6. The fixed zero-free circle retains all rows

For $x=B_A|w|$, the Taylor terms after the first nonzero conductor coefficient obey
\[
 \left|\frac{v!E_A(w)}{\mu_vw^v}-1\right|
 \le C_v\sum_{j\ge1}\frac{v!x^j}{(v+j)!}
 \le \frac{C_vxe^x}{v+1}.
\]
The last inequality follows term by term from $(v+j)!/v!\ge(v+1)(j-1)!$ for $j\ge1$. Radius (14) makes this at most $1/2$, proving the denominator floor. The numerator after multiplication by $e^{-c'w}$ still vanishes to order $v$, because multiplication by an analytic nonvanishing exponential preserves that order. Its remaining coefficients are bounded by the exact finite exponential sum and $\sum|z_\alpha|\le\sqrt{n_E}\|z\|$. This proves the numerator bound and equation (16). Since $B_A\ge1$, $R_A\le1$ and $s=R_A/2\le1/2$. The power series for $\arctan$ gives $|w(t)|\le\operatorname{arctanh}|t|$, and $\operatorname{arctanh}(R_A/2)<R_A$ for $0<R_A\le1$ (its derivative comparison, or integrating $(1-x^2)^{-1}\le4/3$ on $[0,1/2]$, gives the stronger bound $2R_A/3$). The analytic factor $(1+t^2)^{-1/4}$ uses its branch with value one at zero. It has modulus at most $(1-s^2)^{-1/4}$. Thus every actual row is holomorphic in a neighborhood of the closed circle used for Cauchy bounds.

Expanding its absolutely convergent Taylor series at the sample points and summing roots of unity gives equation (18) term by term. For a unit row combination $x$, Cauchy's estimate bounds each coefficient by $A_ks^{-n}$; the tail sum is exactly bounded by $A_ks^{-n}2^{-T}/(1-2^{-T})$. After multiplying by the original $\rho_n/\sqrt{\mathfrak m_\sigma}$ and summing squares, (18) follows in operator norm, with no extra factor depending on the number of rows.

The recurrence (26) follows by multiplying two convergent series whose denominator constant is $g_0=\mu_v/v!\ne0$, and comparing each coefficient. For the numerator tail use $(v+L+j)!\ge(v+L)!j!$ term by term; summing gives precisely (27). The denominator has the same bound with $A_1,B_A$. If a truncated denominator has error $\delta_g<|\mu_v|/(4v!)$, its modulus is at least $|\mu_v|/(4v!)$. For true values $f,g$ and approximants $\widehat f,\widehat g$,
\[
 \left|\frac{\widehat f}{\widehat g}-\frac f g\right|
 \le\frac{|\widehat f-f|}{|\widehat g|}
 +\frac{|f|\,|\widehat g-g|}{|g|\,|\widehat g|}.
 \tag{FI16}
\]
This and the numerator bound produce the assembled sample enclosures in FI15. Factorial tails tend to zero, so any positive target enclosure is reached after finitely many terms for specified original input enclosures.

Because $s,a$ are fixed by the actual conductor, $\rho_n^2\le2n+1$, $D_N=O(q)$ and $\log A_k=O(k+\log(k+2))$ imply $\log B_N=O(q)$. FI11–12, the stated polynomial conductor norm and the lower-root bound give $\log(1/\lambda_N),\log(1/s_E)=O(q\log(q+2))$. Therefore (22), (23), FI15 and the entrywise enclosure have logarithmic precision requirements $O(q\log(q+2))$. This is a bound on sample count and absolute tolerances, not a claim of that arithmetic operation count for computing a large determinant.

## FI7. Fully typed quotient invariance

All spaces here are complex coefficient spaces in their original frames. Let $X=\mathbb C^q$ be full upper-root values, $Y=\mathbb C^{q'}$ lower-root values, $U_{\mathcal D}:\mathbb C^d\hookrightarrow X$ the admitted rational numerator map, and $C_A:X\to Y$ the complete conductor observation. On the MF degree and denominator guard the map $R_{\mathcal D}=C_AU_{\mathcal D}:\mathbb C^d\to Y$ is injective. Use its displayed exact left inverse $L_{\mathcal D}:Y\to\mathbb C^d$. In equation (31), $Z$ must mean its full-root embedding $\widetilde Z=ZS_k^{\mathsf T}:X\to\mathbb C^r$. Then
\[
 B_{\mathcal D}=\widetilde ZU_{\mathcal D}L_{\mathcal D}:Y\to\mathbb C^r,
 \quad Z_{\mathcal D}=\widetilde Z-B_{\mathcal D}C_A:X\to\mathbb C^r.
 \tag{FI17}
\]
Direct multiplication gives $Z_{\mathcal D}U_{\mathcal D}=0$. Hence $\overline Z_{\mathcal D}([x])=Z_{\mathcal D}x$ is a well-defined map $X/\operatorname{im}U_{\mathcal D}\to\mathbb C^r$, the exact meaning of factoring through the actual quotient. For each lower root $\eta$, root addition gives the row symbol $E_A(w)e^{\eta w}$ for that row of $C_A$. It follows that $G_{z_{\mathcal D}}=G_z-\sum_\eta B_{z\eta}e^{\eta w}$ and hence $W_{N,\mathcal D}=W_N-B_{\mathcal D}E_N$. Since $E_NP_N=0$ and $P_NE_N^*=0$, multiplication proves equation (33) exactly. No change of an adjoint or source metric enters this identity. Another left inverse gives another correction of the form $BE_N$ and the same projected covariance. The unprojected Gram has the full extra cross terms $-BE_NW_N^*-W_NE_N^*B^*+BE_NE_N^*B^*$, which need not vanish.

If $R_{\mathcal D}$ loses rank, its displayed inverse is undefined and FI17 is not used. The exact defect is $\ker(C_AU_{\mathcal D})$, whose image under the injective $U_{\mathcal D}$ is exactly $\operatorname{im}U_{\mathcal D}\cap\ker C_A$; both inclusions follow directly by applying $C_A$. Thus the rank guard is the injectivity of this concrete observation, not a presumed metric property. The original collision proof supplies its applicable rank-stratified quotient calculations. No limiting native determinant coefficient follows from the finite certificates above.
