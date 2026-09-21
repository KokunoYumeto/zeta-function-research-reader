# Complete received mathematical continuations



## Received contribution 1

## A quantitative calculation of the original invariant determinant

The remaining quantity is still

$$
\mathcal K_k
=
\mathcal R\log\det(I_K^*G_NI_K),
\qquad
\mathcal R f_N=f_{q-1}+f_q-f_{2q-1}-f_{2q}.
$$

The new KG, MF, and PC results do not assign its \(kq\) coefficient. Your attachment explicitly identifies the full projected invariant covariance—not another heat or inverse estimate—as the next calculation. 

The result obtained here is a **finite-\(k\) formula for this original determinant with an explicit \(O_{h,A}(q\log q)\) remainder**. It retains every invariant row and every lower-root projection. Its scalar reference factor is a specified positive rational number; its remaining matrix can be calculated on one fixed zero-free circle, without deleting conductor-pole rows.

In particular, the normalized remainder is

$$
O_{h,A}\!\left(\frac{\log q}{k}\right).
$$

This is a quantitative remainder for the actual kernel allocation. **I have not obtained a numerical value for its limiting coefficient:** the period-dependent projected covariance in the formula below has not been numerically evaluated in this turn.

I used the mathematical edition at `cb9705da84d6f8689611914ed9659298e620ba0a` and its checked successor `bee43be41d2f6f872869d5e258fa5f752335a5ad`. The latter’s recorded change is the publication-link update, not a new kernel-coefficient theorem.

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

Let \(Z\) be the complete original invariant-row matrix from CG29–30, after the specified low-degree constraint elimination. Its rank is

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

where \(E_N\) evaluates at **all** original lower roots. This is the matrix specified in your attachment, now in the fixed \(R_Z\)-orthonormal row frame.

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
2mL_k^{\mathrm{form}}
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
\|\widehat P_N-P_N\|\le3\epsilon_E/s_E,
}
\tag{21}
$$

where \(\widehat P_N\) is formed using every row of \(\widehat E_N\). One proves (21) by bounding the two cross-projections between the nullspaces: their norms are at most \(\epsilon_E/s_E\) and \(\epsilon_E/(s_E-\epsilon_E)\).

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
ZU_{\mathcal D}L_{\mathcal D},
\qquad
Z_{\mathcal D}=Z-B_{\mathcal D}C_A.
\tag{31}
$$

Then

$$
Z_{\mathcal D}U_{\mathcal D}=0,
$$

so \(Z_{\mathcal D}\) factors through the actual \(\pi_{\mathcal D}\). The coefficient left inverse in (31) is used only to specify the map; it is not declared an isometry of a native metric.

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
\ell_z[\chi']=G_z''(0)-G_z'(0)=\frac{17i}{24}.
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

The actual numerical sequence \(\mathcal R\log\det C_N/(kq)\), or an analytic asymptotic for those same invariant rows, remains to be evaluated. No complex-current phase is assigned by these positive Gram calculations. The runtime remained unavailable, so no fresh executed covariance values, checker receipt, or repository modification is claimed.

### References

Koornwinder, T. H., Wong, R., Koekoek, R., Swarttouw, R. F., & Reinhardt, W. P. (n.d.). Orthogonal polynomials. In *NIST Digital Library of Mathematical Functions* (Chapter 18). Equations 18.22.8 and 18.23.7 supply the recurrence and generating-function conventions used above. ([DLMF][2])

*Continue the original kernel allocation after the complete late-memory calculation*. (2026, September 21). [User-supplied research instructions and source specification]. The canonical determinant target and required full projected covariance are retained here. 

Split-Zero research programme. (2026a, September 21). *ACTUAL_KERNEL_FILTRATION_AND_GRAPH.tex* [Proof source, KF37–55]. *Zeta-function research reader*, commit `bee43be41d2f6f872869d5e258fa5f752335a5ad`. The complete finite source comparison, relation graph, and fixed-frame determinant transport are the inherited inputs to (7) and (30).

Split-Zero research programme. (2026b, September 21). *COMPLETE_CONDUCTOR_GRAPH_METRIC.tex* and *INVARIANT_STRIP_ANGLE_REDUCTION.tex* [Proof sources, CG18–32 and CGS1–20]. Same repository and commit. The full-form errors and the post-projection lower bound are retained with their original finite domains.

[1]: https://dlmf.nist.gov/18.23.E7 "https://dlmf.nist.gov/18.23.E7"
[2]: https://dlmf.nist.gov/18 "https://dlmf.nist.gov/18"


## Received contribution 2

The moving-denominator construction can be taken to an **explicit collision involving \(q'=(k-7)^2\) original arithmetic roots**, far beyond the previously controlled regime \(d\log q=o(q)\). At this collision, the resulting polynomial word is singular on the full arithmetic quotient but remains injective on the **entire original observation kernel**.

This gives an evaluated long-word image of that kernel:

$$
\boxed{
\mathcal R\log\det
\left[
(D_k(M)I_K)^*G_ND_k(M)I_K
\right]
=
(8k-16)\,C_\partial q+o_{h,\varpi}(kq).
}
\tag{1}
$$

Here \(D_k\) is an explicit factor of the original \(Q_k\), defined below. It has degree \(q'\), and the source cutoff on the left remains exactly \(N\).

There is a second, distinct calculation. The collision quotient carries the original kernel isomorphically to a space whose **entire \(kq\)-coefficient is zero**:

$$
\boxed{
0\le
\mathcal R\log\det \widehat H^{\,\partial}_{K,N}(\alpha)
\le
O_{h,\varpi}\!\left(k^2\log^2(q+2)\right)
=o(kq),
\qquad 0\le\alpha\le1.
}
\tag{2}
$$

This does not set the original kernel coefficient to zero. The exact difference is a positive graph determinant, displayed in equation (23). Its metric contribution remains in the calculation.

Finally, the original projected invariant covariance can be approximated **with all original rows retained**, on one fixed zero-free Cauchy circle. The determinant error can be made arbitrarily small using

$$
\boxed{
T=O_{h,\varpi}\!\left(q\log(q+2)+\log(r/\epsilon)\right)
}
\tag{3}
$$

sampling points. This removes the preceding need to discard a growing conductor-pole subspace and then charge its complementary Schur determinant.

The collision quotient, its kernel, the metric bounds, and the full-row approximation are finite deductions below. Equation (1) additionally uses the existing **all-direction near-root estimate** from DCR, rather than only its full-volume conclusion.

## 1. An actual factor of the original arithmetic relation

Retain the simple-quartet domain

$$
k\equiv1\pmod4,\qquad k\ge9,\qquad
q=(k+1)^2,
$$

$$
0<\delta<\frac12,\qquad \gamma>2,
\qquad
\omega_{ab}=(2b-k)\gamma-i(2a-k)\delta,
$$

and

$$
Q_k(y)=\prod_{a,b=0}^{k}(y-\omega_{ab}),
\qquad
E_k=\mathbb C[y]/(Q_k),
\qquad
M[p]=[yp].
$$

The physical coordinate remains

$$
S=k/2+iy.
$$

Use the **original conductor biform**

$$
A=\sum_{r,s=0}^{8}a_{rs}e^{(8)}_{rs}.
$$

Let \((r_*,s_*)\) be its prescribed largest nonzero pivot and write

$$
a_*=a_{r_*s_*}\ne0.
$$

Define the actual pivot-interior box

$$
\mathcal I_k
=
\{(r_*+a,s_*+b):0\le a,b\le k-8\},
$$

and its complement

$$
\partial_k=\{0,\ldots,k\}^2\setminus\mathcal I_k.
$$

Their dimensions are

$$
q'=(k-7)^2,\qquad
\Delta=q-q'=16k-48.
$$

Now take the literal factors

$$
\boxed{
D_k(y)=\prod_{(a,b)\in\mathcal I_k}(y-\omega_{ab}),
\qquad
O_k(y)=\prod_{(a,b)\in\partial_k}(y-\omega_{ab}),
\qquad Q_k=D_kO_k.
}
\tag{4}
$$

No conductor zero has been substituted for an arithmetic root.

The corresponding monic polynomial in the original physical coordinate is

$$
D_k^S(S)=i^{q'}D_k((S-k/2)/i),
$$

so

$$
D_k(M)=i^{-q'}D_k^S(A).
$$

The displayed phase is retained.

### The conductor proves injectivity on the original kernel

In original root-value coordinates, order the interior coordinates first and the boundary coordinates second. The conductor has the block form

$$
C_A=[T_k\ \ U_k].
$$

The pivot-interior block is triangular, with every diagonal entry equal to \(a_*\). Therefore

$$
\boxed{\det T_k=a_*^{\,q'}\ne0.}
\tag{5}
$$

This is the original OCF triangular elimination. Its path bound also gives

$$
\log^+\|T_k^{-1}U_k\|=O_\varpi(k),
$$

with the actual coefficients and pivot retained.

Put

$$
F_k=-T_k^{-1}U_k.
$$

Then the complete conductor kernel in root-value coordinates is

$$
\ker C_A
=
\left\{
\binom{F_kb}{b}:b\in\mathbb C^\Delta
\right\}.
\tag{6}
$$

The actual observation kernel satisfies \(K\subset\ker C_A\). If \(\mathsf V\) is the original value isomorphism, define

$$
J_{\partial,k}
=
\operatorname{pr}_{\partial_k}\mathsf V I_K.
$$

Equation (6) gives the exact original-frame identity

$$
\boxed{
\mathsf V I_K
=
\binom{F_k}{I_\Delta}J_{\partial,k}.
}
\tag{7}
$$

In particular \(J_{\partial,k}\) has the same column rank

$$
m=\dim K=8k-16.
$$

The polynomial word \(D_k(M)\) vanishes precisely on the interior primary coordinates:

$$
V_{D_k}:=\ker D_k(M)
=
O_k\mathcal P_{<q'}.
$$

If \(x\in K\cap V_{D_k}\), its boundary coordinates vanish. Equation (6) then forces its interior coordinates to vanish as well. Thus

$$
\boxed{
K\cap\ker D_k(M)=0.
}
\tag{8}
$$

This is an injectivity statement for the **actual original kernel**, not for a generic \(m\)-plane.

## 2. The collision is covered by the polynomial continuation, not by rational inversion

At this divisor,

$$
\gcd(Q_k,D_k)=D_k.
$$

The rational map \(p/D_k\) is therefore unavailable in the original quotient. The polynomial continuation remains exact.

Indeed,

$$
\operatorname{rem}_{Q_k}(D_kp)
=
D_k\,\operatorname{rem}_{O_k}p.
$$

Consequently the continued quotient map is

$$
\boxed{
\pi_{D_k}
=
\operatorname{quo}_{D_k}\operatorname{rem}_{Q_k}(D_k\,\cdot)
=
\operatorname{rem}_{O_k}.
}
\tag{9}
$$

Its kernel is \(O_k\mathcal P_{<q'}\), of dimension \(q'\), and its target has dimension \(\Delta\).

The polynomial frame from PC specializes to

$$
y^{\Delta+j}-\operatorname{rem}_{O_k}(y^{\Delta+j}),
\qquad 0\le j<q'.
$$

These are a unit-triangular change from the frame

$$
O_k,\ yO_k,\ldots,y^{q'-1}O_k.
$$

Thus every colliding direction remains present. The determinant of the rational coordinate change vanishes here; the rank-\(q'\) polynomial subspace does not disappear.

### Exact observation complex

Write the remaining original invariant columns in the strip frame as \(Z_k\). In suitable **fixed algebraic output coordinates**, the unchanged observation is

$$
\widetilde\Lambda
\binom{x_{\mathcal I}}{x_\partial}
=
\binom{T_kx_{\mathcal I}+U_kx_\partial}
{Z_k^{\mathsf T}x_\partial}.
$$

Its kernel is the original \(K\), and

$$
\operatorname{rank}Z_k=8k-32.
$$

The transpose is complex-linear. This is the complete invariant image, including the nonconductor columns.

The quotient observation is therefore exactly

$$
\boxed{
\bar\Lambda_\partial:
\mathbb C^\Delta\longrightarrow\mathbb C^{8k-32},
\qquad
b\longmapsto Z_k^{\mathsf T}b,
}
\tag{10}
$$

and

$$
\ker\bar\Lambda_\partial=\operatorname{im}J_{\partial,k}.
$$

The contractible subcomplex being removed is

$$
V_{D_k}\xrightarrow{\ \Lambda\ }\Lambda V_{D_k}.
$$

Its differential is an isomorphism by (8).

All maps can be written explicitly. In the displayed coordinates, let

$$
j_Eb=\binom{F_kb}{b},\qquad
j_B\eta=\binom0\eta,
$$

$$
q_E\binom{x_{\mathcal I}}{x_\partial}=x_\partial,
\qquad
q_B\binom c\eta=\eta,
$$

and

$$
h\binom c\eta=\binom{T_k^{-1}c}{0}.
$$

Direct multiplication gives

$$
I_E-j_Eq_E=h\widetilde\Lambda,
\qquad
I_B-j_Bq_B=\widetilde\Lambda h.
\tag{11}
$$

These are exact algebraic homotopy identities. They do not declare \(j_E\) to be a minimum section or an isometry.

The arithmetic operator descends because \(V_{D_k}\) is invariant:

$$
q_EM=M_\partial q_E,
\qquad
M_\partial=\operatorname{diag}(\omega_{ab})_{(a,b)\in\partial_k}.
$$

The section defect is retained:

$$
\boxed{
Mj_E-j_EM_\partial
=
\binom{
\operatorname{diag}(\omega_{\mathcal I})F_k
-F_k\operatorname{diag}(\omega_\partial)
}{0}.
}
\tag{12}
$$

It lies in the removed interior subspace. The reduced kernel need not be invariant under \(M_\partial\).

## 3. The reduced kernel’s whole \(kq\)-coefficient is zero

Give the boundary quotient its **attained original metric**

$$
G^\partial_N(\alpha)
=
\left(
\pi_\partial G_N(\alpha)^{-1}\pi_\partial^*
\right)^{-1},
$$

where

$$
\pi_\partial=\operatorname{pr}_{\partial_k}\mathsf V.
$$

Define

$$
\widehat H^\partial_{K,N}(\alpha)
=
J_{\partial,k}^*G^\partial_N(\alpha)J_{\partial,k}.
\tag{13}
$$

This quotient has a direct scalar-source interpretation: it prescribes only the values at the \(\Delta\) original boundary roots, while still minimizing over the entire original degree-\(N\) source.

Let

$$
R_k=k\sqrt{\delta^2+\gamma^2},
\qquad M_\sigma=\sqrt{2\pi}.
$$

The exact Gamma generating function bounds the complete boundary evaluation covariance by

$$
A^\partial_N I_\Delta,
$$

where

$$
A^\partial_N
=
\frac{\Delta e^2}{M_\sigma}
(N+1)^{3/2}(2N+1)^{R_k+1}.
$$

Conversely, interpolate the boundary data by its full degree-\((\Delta-1)\) Lagrange polynomial. Every boundary-root separation is at least \(2\delta\). Repeated Gamma multiplication gives

$$
B^\partial_k
=
\Delta M_\sigma
\left(\frac{2\Delta+R_k}{2\delta}\right)^{2(\Delta-1)}
$$

as a squared interpolation-norm bound. Hence

$$
(A^\partial_{2q})^{-1}I
\preceq G_N^{\partial,\sigma}
\preceq B^\partial_kI.
\tag{14}
$$

The important point is the dimension in this estimate:

$$
\log A^\partial_{2q}
+\log B^\partial_k
=O_h(k\log(q+2)),
$$

rather than \(O(q\log q)\).

Retain the original full polynomial comparison

$$
\ell_k\|P\|_\sigma^2
\le\|P\|_{\mu_k}^2
\le u_k\|P\|_\sigma^2,
$$

and the joint-source enclosure

$$
\mathbf L_k^{-1}T_k\preceq G_N^J\preceq\mathbf B_kT_k.
$$

In root values \(T_k\) has the original positive tuple weights \(W_\omega\), with

$$
a_{\min}^k\le W_\omega\le A_w^k.
$$

Set

$$
\underline b_k
=
\min\left\{
\frac{\ell_k}{A^\partial_{2q}},
\frac{a_{\min}^k}{\mathbf L_k}
\right\},
\qquad
\overline b_k
=
\max\left\{
u_kB^\partial_k,\,
\mathbf B_kA_w^k
\right\}.
$$

The exact covariance blend preserves these common bounds:

$$
\boxed{
\underline b_k I
\preceq G^\partial_N(\alpha)
\preceq\overline b_k I,
\qquad
0\le\alpha\le1,\quad q-1\le N\le2q.
}
\tag{15}
$$

Write

$$
\kappa_{\partial,k}=\overline b_k/\underline b_k.
$$

The retained source constants give

$$
\log\kappa_{\partial,k}
=O_{h,\varpi}(k\log^2(q+2)).
$$

For a fixed activation, the source spaces increase with \(N\), so the attained metrics decrease. Restricting (15) to the same frame \(J_{\partial,k}\) therefore proves

$$
\boxed{
0\le
\mathcal R\log\det\widehat H^\partial_{K,N}(\alpha)
\le
2m\log\kappa_{\partial,k}
=
O_{h,\varpi}(k^2\log^2(q+2)).
}
\tag{16}
$$

The frame \(J_{\partial,k}\) need not be well-conditioned. Its fixed Euclidean determinant factor cancels between the four cutoffs. No generic lower bound for one of its minors is assumed.

The same conclusion holds for every fixed arithmetic polynomial word on the boundary quotient that is injective on the relevant frame. Indeed, for \(P_k(M_\partial)J_{\partial,k}\), apply (15) to that entire fixed frame. Its Euclidean volume cancels under \(\mathcal R\). Thus its action-volume four-return is \(o(kq)\), without a word-length restriction arising from repeated norm multiplication.

This is a result in the collision quotient. The metric cost of returning to the original kernel is still present.

## 4. The long word’s image in the original metric is an ordinary outer quotient

The word \(D_k(M)\) has an additional advantage: its image of \(K\) can be evaluated in the **unmodified canonical metric**.

Let \(\mathsf V_{O_k}\) be evaluation at the boundary roots for polynomials of degree below \(\Delta\), and put

$$
P_K=\mathsf V_{O_k}^{-1}J_{\partial,k}.
$$

Then the original word image has the degree-below-\(q\) representative

$$
\boxed{
D_k(M)I_K=[D_kP_K].
}
\tag{17}
$$

Both sides vanish at every interior root and have the same value \(D_k(\omega)J_{\partial,k}\) at every boundary root.

Every scalar representative of this class at cutoff \(N\) vanishes at all roots of \(D_k\). It must therefore be divisible by \(D_k\). Consequently its canonical minimum is exactly the quotient metric

$$
\mathfrak G_N^{D,O}([p])
=
\min_{\deg(p+O_kh)\le N-q'}
\int_{\mathbb R}
|D_k(y)|^2|p(y)+O_k(y)h(y)|^2\,d\mu_k(y)
$$

on \(\mathbb C[y]/(O_k)\). Thus

$$
(D_k(M)I_K)^*G_ND_k(M)I_K
=
P_K^*\mathfrak G_N^{D,O}P_K.
$$

The source degrees are literally

$$
N-q'=\Delta-1,\ \Delta,\ q+\Delta-1,\ q+\Delta,
$$

and the relation degrees are still

$$
-1,\ 0,\ q-1,\ q.
$$

No product of a minimum source representative has been allowed a larger cutoff.

The inner polynomial is a fixed translate of the original lower grid:

$$
D_k(y)=Q_{k-8}(y-z_*),
\qquad
z_*=(2s_*-8)\gamma-i(2r_*-8)\delta.
$$

All roots of the outer polynomial \(O_k\) have modulus \(O_h(k)=o(q)\). It has degree \(O(k)\), and there are no exceptional \(q\)-scale outer roots.

These are precisely the small-root hypotheses needed for the all-direction part of the existing DCR outer-quotient estimate. The fixed translation is returned through the original Gamma translation inequality; the arithmetic comparison is applied before the same minima. The comparison is a form comparison, so it applies to the actual frame \(P_K\), irrespective of its orientation. It is not inferred from equality of two full determinants.

It follows that

$$
\boxed{
\mathcal R\log\det
\left[
(D_k(M)I_K)^*G_ND_k(M)I_K
\right]
=
mC_\partial q+o_{h,\varpi}(kq),
\qquad m=8k-16.
}
\tag{18}
$$

In particular,

$$
\lim_{k\to\infty}
\frac1{kq}
\mathcal R\log\det
\left[
(D_k(M)I_K)^*G_ND_k(M)I_K
\right]
=8C_\partial.
$$

This is an actual long polynomial word on the original kernel. Its degree is \(q'\), so it is outside the short-word regime whose distortion had previously been bounded by \(o(kq)\).

The statement is canonical. For weak critical activations where AK13–16 preserve the entire metric exponentially accurately, it remains valid with \(G_N(\alpha)\). A general activated tensor minimum is not identified with a scalar divisibility ideal.

## 5. The exact term separating the word calculation from the canonical kernel

Write the original metric in root coordinates as

$$
\mathsf G_N=
\begin{pmatrix}
G_{\mathcal I\mathcal I}&G_{\mathcal I\partial}\\
G_{\partial\mathcal I}&G_{\partial\partial}
\end{pmatrix}.
$$

Its boundary quotient is

$$
G^\partial_N
=
G_{\partial\partial}
-G_{\partial\mathcal I}
G_{\mathcal I\mathcal I}^{-1}
G_{\mathcal I\partial}.
$$

The original conductor-zero section and the actual minimum boundary section differ by

$$
X_N=
\left(
F_k+G_{\mathcal I\mathcal I}^{-1}
G_{\mathcal I\partial}
\right)J_{\partial,k}.
$$

Completing the full quadratic square gives

$$
\boxed{
H_{K,N}
=
\widehat H^\partial_{K,N}
+X_N^*G_{\mathcal I\mathcal I}X_N.
}
\tag{19}
$$

This includes every interior correction.

Define

$$
\Xi_N
=
G_{\mathcal I\mathcal I}^{1/2}
X_N
(\widehat H^\partial_{K,N})^{-1/2}.
$$

Then

$$
\boxed{
\delta^\partial_{K,N}
:=
\log\det H_{K,N}
-\log\det\widehat H^\partial_{K,N}
=
\log\det(I_m+\Xi_N^*\Xi_N)\ge0.
}
\tag{20}
$$

All \(m\) eigenvalues are retained, including any zero eigenvalues of \(\Xi_N^*\Xi_N\).

Equations (16) and (20) give the finite original-kernel receiver

$$
\boxed{
0\le
\mathcal R\log\det H_{K,N}
-\mathcal R\log\det(I+\Xi_N^*\Xi_N)
\le2m\log\kappa_{\partial,k}.
}
\tag{21}
$$

There is also a full-window variation bound. Let

$$
b_N=
\log\det\widehat H^\partial_{K,q-1}
-\log\det\widehat H^\partial_{K,N}.
$$

Then \(b_N\) is increasing, \(0\le b_N\le m\log\kappa_{\partial,k}\), and

$$
\delta^\partial_{K,N}-b_N
=
\log\det H_{K,N}
-\log\det\widehat H^\partial_{K,q-1}
$$

is decreasing. Hence

$$
\boxed{
\sum_{N=q-1}^{2q-1}
\left(
\delta^\partial_{K,N+1}
-\delta^\partial_{K,N}
\right)_+
\le m\log\kappa_{\partial,k}=o(kq).
}
\tag{22}
$$

Thus the remaining positive graph determinant is decreasing at the \(kq\) scale, up to a completely bounded cumulative correction. This is a whole-window statement, not \(q\) separate \(O(q)\) bounds.

Combining the evaluated word image with (21) yields

$$
\boxed{
\begin{aligned}
\mathcal R\log
\frac{
\det[(D_k(M)I_K)^*G_ND_k(M)I_K]
}{
\det(I_K^*G_NI_K)
}
={}&mC_\partial q\\
&-\mathcal R\log\det(I+\Xi_N^*\Xi_N)
+o(kq).
\end{aligned}}
\tag{23}
$$

The word reaches a calculable ordinary outer quotient, but its distortion is exactly where the still-uncomputed canonical coefficient remains. Equation (23) prevents that distortion from being dropped.

## 6. The collision loses an evaluated amount of inverse-power metric

The metric failure of the algebraic retraction can be quantified on the original inverse-power family.

For \(1\le r\le\Delta\), the boundary evaluations of

$$
U_rd=\sum_{j=1}^{r}d_j[y^{-j}]
$$

form the matrix

$$
V_{\partial,r}=(\omega^{-j})_{\omega\in\partial_k,\ 1\le j\le r}.
$$

It has full column rank. This proves

$$
V_r\cap V_{D_k}=0
$$

without a coprimality assertion about \(D_k\) and \(Q_k\).

Let

$$
\varrho_k=\min_{\omega\in\partial_k}|\omega|.
$$

Then

$$
\varrho_k\ge\sqrt{\delta^2+\gamma^2}>2,
$$

and, once \(k>14\),

$$
\varrho_k\ge\delta(k-14).
$$

Indeed every boundary index has at least one coordinate within seven positions of an outer edge.

For any \(r\) selected boundary roots,

$$
\left|\frac1{\omega_i}-\frac1{\omega_j}\right|
\ge\frac{2\delta}{R_k^2}.
$$

The full inverse-Vandermonde estimate therefore gives

$$
\boxed{
\frac1{rR_k^2T_k^{2(r-1)}}I_r
\preceq
V_{\partial,r}^*V_{\partial,r}
\preceq
\frac{\Delta}{\varrho_k^2-1}I_r,
}
\tag{24}
$$

where

$$
T_k=
\max\left\{
1,\frac{R_k^2(1+\varrho_k^{-1})}{2\delta}
\right\}.
$$

The proof is the coefficient bound for each complete Lagrange polynomial on the reciprocal nodes, followed by the diagonal factor \(1/\omega_i\). No pole sign or root is removed.

Equations (15) and (24) show that the boundary quotient metric of these \(r\) inverse powers has logarithmic width

$$
O_{h,\varpi}\bigl(k\log^2(q+2)+r\log(q+2)\bigr).
$$

The full original source metric, by the supplied harmonic theorem, is

$$
H^E_{r,N}(\alpha)
=
h_N(\alpha)\,e^{\pm E_{r,N}}
$$

as a two-sided form comparison.

Thus the exact angle loss to this large collision quotient is

$$
\boxed{
\begin{aligned}
\delta_{V_r,V_{D_k},N}
&=
\log\det H^E_{r,N}(\alpha)
-\log\det\!\left[
V_{\partial,r}^*G^\partial_N(\alpha)V_{\partial,r}
\right]\\
&=
r\log h_N(\alpha)
+O_{h,\varpi}\!\left(
r k\log^2(q+2)+r^2\log(q+2)
\right).
\end{aligned}}
\tag{25}
$$

For \(r=O(k)\), the error is \(o(rq)\).

At the original critical activation,

$$
\alpha_k(\zeta)=e^{-2q\log(q/k)-\zeta q},
$$

this gives

$$
\boxed{
\mathcal R\delta_{V_r,V_{D_k},N}
=
rq\,C_{\rm inv}(\zeta)+o(rq),
}
\tag{26}
$$

with the unchanged clipped coefficient

$$
C_{\rm inv}(\zeta)
=
2[\min(\beta_{\mathrm L},\zeta)
-\min(\beta_{\mathrm H},\zeta)].
$$

Therefore the algebraic collision quotient is not a low-cost extension of the separated-pole theorem merely because the kernel map remains injective. Its loss on a rank-\(k\) original inverse-power sector is already of order \(kq\), and has the evaluated value (26).

The reduced arithmetic operator also has no late soft mode:

$$
\frac{\varrho_k^2}{\kappa_{\partial,k}}I
\preceq
M_\partial^{\dagger}M_\partial
\preceq
R_k^2\kappa_{\partial,k}I.
\tag{27}
$$

At the original late times \(e^{2q\log(q/k)+bq}\), its complete heat trace tends to zero. The ultrasmall mode of the original quotient is not preserved by this nonisometric retraction; its loss is recorded in (25).

## 7. The remaining projected covariance can be evaluated without discarding conductor-pole rows

The attachment identifies the still-required original covariance as

$$
C^U_N=W_NP_NW_N^*,
\qquad
P_N=I-E_D^*(E_DE_D^*)^{-1}E_D,
\qquad D=N-v.
$$

The original row functions are

$$
F_z(w)=\sum_\alpha z_\alpha e^{\beta_\alpha w},
$$

$$
H_z(t)
=
(1+t^2)^{-1/4}
e^{-c'w(t)}
\frac{F_z(w(t))}{E_A(w(t))},
\qquad
w(t)=-i\arctan t.
$$

Those are the rows specified for the unresolved calculation in the supplied file.

The preceding large-circle construction cancelled conductor poles by restricting the row space. A fixed small circle avoids that operation entirely.

### A zero-free circle determined by the actual first moment

Set

$$
A_1=\sum_j|a_j|,
\qquad
B_A=\max(1,\max_j|b_j|),
\qquad
c_v=\frac{A_1B_A^v}{|\mu_v|}.
$$

Define

$$
R_A=
B_A^{-1}
\min\left\{1,\frac{v+1}{4e\,c_v}\right\}.
$$

The exact Taylor series gives

$$
\left|
\frac{v!E_A(w)}{\mu_vw^v}-1
\right|
\le
\frac{c_vB_A|w|e^{B_A|w|}}{v+1}
\le\frac14
\quad(|w|\le R_A).
\tag{28}
$$

Take

$$
s=\min\{1/4,\tanh(R_A/2)\},
\qquad r=s/2.
$$

Then \(|w(t)|\le R_A/2\) on \(|t|\le s\). The only zero of \(E_A(w(t))\) in this disk is its retained zero of order \(v\) at the origin.

Every actual row under consideration annihilates degrees below \(v\). Its numerator has the matching zero. Thus **every original row \(H_z\) is holomorphic on this same disk**; no row-space codimension is imposed.

Put

$$
B_k=\max(1,\max_\alpha|\beta_\alpha|).
$$

Taylor’s remainder gives

$$
\left|\frac{F_z(w)}{w^v}\right|
\le
\frac{\sqrt q\,B_k^v}{v!}
e^{B_k|w|}\|z\|_2.
$$

Consequently,

$$
\boxed{
\sup_{|t|\le s}|H_z(t)|
\le
M_k\|z\|_2,
}
$$

where

$$
M_k=
\frac{4\sqrt q\,B_k^v}{3|\mu_v|}
(1-s^2)^{-1/4}
e^{(B_k+|c'|)\operatorname{arctanh}s}.
\tag{29}
$$

For the fixed original period,

$$
\log M_k=O_{h,\varpi}(k+\log q).
$$

### Full-row Fourier reconstruction with an explicit relative error

Let \(Z\) be the actual full row matrix, of rank \(r_Z\), and use

$$
\widehat Z=(ZZ^*)^{-1/2}Z
$$

only for the numerical error norm. This is a fixed row congruence; its determinant cancels between the projected and unprojected row Grams.

Write

$$
H_z(t)=\sum_{n\ge0}a_{z,n}t^n,
\qquad
W_{z,n}=\frac{\rho_n}{\sqrt{M_\sigma}}a_{z,n},
\qquad
\rho_n^2=\frac{n!}{(1/2)_n}.
$$

Define

$$
B_D=
\frac{M_k}{\sqrt{M_\sigma}}
\left(\sum_{n=0}^{D}\rho_n^2s^{-2n}\right)^{1/2}.
$$

Then

$$
\|W_N\|\le B_D,
\qquad
\log B_D=O_{h,\varpi}(q).
$$

For \(T>D\), sample the original functions at

$$
t_j=r e^{2\pi ij/T}.
$$

Set

$$
\widehat a_{z,n}
=
\frac1{Tr^n}\sum_{j=0}^{T-1}
H_z(t_j)e^{-2\pi ijn/T}.
$$

The aliasing identity is exact:

$$
\widehat a_{z,n}-a_{z,n}
=
\sum_{\ell\ge1}a_{z,n+\ell T}r^{\ell T}.
$$

Therefore

$$
\boxed{
\|\widehat W_N-W_N\|
\le
B_D\frac{2^{-T}}{1-2^{-T}}.
}
\tag{30}
$$

The actual projected row map has a finite lower bound

$$
C^U_N\succeq\lambda_NI,
$$

where one may use

$$
\boxed{
\lambda_N=
\left[
M_D^2\,B_k^{\rm val}\,
q\left(\frac{A_1}{|a_*|}\right)^{20k}
\right]^{-1}.
}
\tag{31}
$$

Here \(M_D\) is the complete Gamma forward norm bound for the original conductor, and

$$
B_k^{\rm val}
=
qM_\sigma
\left(\frac{2q+R_k}{2\delta}\right)^{2(q-1)}.
$$

For clarity, the lower-bound argument retains the actual lower-root projection. For any row correction \(bE_D\), multiplication by the conductor source matrix gives the original upper evaluation row of

$$
z-M_Ab.
$$

The strip elimination satisfies \(N_kM_A=0\) and returns \(z\) unchanged in its strip coordinates. Its norm is at most

$$
\sqrt q(A_1/|a_*|)^{10k}.
$$

The complete upper-root interpolation bound is \(B_k^{\rm val}\), and the conductor forward norm is \(M_D\). Taking the minimum over **all** \(b\) gives (31).

In particular,

$$
-\log\lambda_N=O_{h,\varpi}(q\log(q+2)).
$$

Let

$$
\widehat C^U_N=\widehat W_NP_N\widehat W_N^*,
\qquad
\widehat C^0_N=\widehat W_N\widehat W_N^*.
$$

For \(0<\eta<1/2\), it suffices to choose

$$
\boxed{
T\ge
\max\left\{
2q-v+1,\,
\left\lceil
\log_2\frac{24B_*^2}{\eta\lambda_*}
\right\rceil
\right\},
}
\tag{32}
$$

where \(B_*=\max_NB_D\) and \(\lambda_*=\min_N\lambda_N\). Equations (30)–(31) then imply

$$
\boxed{
(1-\eta)C_N^X
\preceq\widehat C_N^X
\preceq(1+\eta)C_N^X,
\qquad X=U,0.
}
\tag{33}
$$

All four cutoffs use prefixes of the **same reconstructed coefficient matrix**. Thus their source ordering is retained instead of making four unrelated approximations.

Let

$$
\ell_N=\log\det C_N^U-\log\det C_N^0,
\qquad
\widehat\ell_N=
\log\det\widehat C_N^U-\log\det\widehat C_N^0.
$$

Then

$$
\boxed{
|\mathcal R(\widehat\ell_N-\ell_N)|
\le8r_Z[-\log(1-\eta)].
}
\tag{34}
$$

Choosing

$$
\eta=1-e^{-\epsilon/(8r_Z)}
$$

gives any requested determinant tolerance \(\epsilon\), and (32) has the growth stated in (3).

The projector need not be evaluated by subtracting two nearly equal determinants. The exact identity

$$
\det C_N^U
=
\frac{
\det\!\left(
\begin{bmatrix}E_D\\W_N\end{bmatrix}
\begin{bmatrix}E_D\\W_N\end{bmatrix}^{\!*}
\right)
}{
\det(E_DE_D^*)
}
\tag{35}
$$

retains the same complete projection and permits a positive block-Gram evaluation.

No conductor-pole rootfinding, pole-cancellation subspace, or complementary omitted-row determinant occurs in (28)–(35).

The original kernel relation from ACC can consequently be certified by

$$
\widehat{\mathcal B}_{K,k}
=
gqC_\partial
+2(\widehat\ell_{q-1}-\widehat\ell_{2q-1}),
\qquad g=16k-48-v,
$$

with

$$
\boxed{
\left|
\mathcal R\log\det(I_K^*G_NI_K)
-\widehat{\mathcal B}_{K,k}
\right|
\le E_{{\rm reference},k}+\epsilon.
}
\tag{36}
$$

Here \(E_{{\rm reference},k}=o(kq)\) is the previously proved source, outer-divisor, and adjacent-cutoff error. The new discretization contributes the explicit \(\epsilon\), not another uncontrolled \(kq\)-scale term.

## What has been determined

The collision \(D_k\mid Q_k\) is now treated inside the actual original packet. Its degree is \(q'\), its full \(q'\)-dimensional kernel is retained, and the original observation kernel intersects it trivially by the actual conductor pivot matrix.

The resulting quotient kernel has zero leading \(kq\) metric return, while the **same original kernel after the long arithmetic word \(D_k(M)\)** has the evaluated return

$$
(8k-16)C_\partial q+o(kq).
$$

The distinction is accounted for by the complete positive graph determinant (20), not by an assumed isometry of a cohomological quotient. The inverse-power loss at this collision is independently evaluated by (25)–(26).

The canonical \(kq\)-coefficient itself remains the return of that actual graph determinant, equivalently the original projected invariant covariance in (36). The new full-row construction provides an arbitrary-accuracy evaluation of that covariance without sacrificing a growing pole subspace. No numerical value of the period-dependent determinant in (36), and no sign of the separate native complex-current coefficient, is asserted here.
