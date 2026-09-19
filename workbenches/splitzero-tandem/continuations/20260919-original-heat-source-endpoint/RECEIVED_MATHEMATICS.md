# GitHub integration and further calculations

I read the new repository work at commit **`607728ee3c35be98720d548794727670b1946c91`**, including the full-window source-product results, the original observation-response equations, and the heat, Beurling, and source-inversion constructions. That commit remained the repository head when I checked again. 

The combination yields four further results:

$$
\boxed{\log c_N=o_h(N)}
$$

for the previously unevaluated heat-comparison constant;

$$
\boxed{
\frac{J_{\mathrm{guard}}(k)}q
\longrightarrow
\frac{2\log(4/\pi)}{\log2}
}
$$

for the repository’s simultaneous original-response certification guard on the simple-quartet window;

$$
\boxed{
b^*\mathsf G_Z^{-1}b
=
1-\prod_{\rho\in Z_+}
\left|\frac{1-\rho}{\rho}\right|^{2m_\rho}
}
$$

for its new finite Beurling quotient; and an explicit asymptotic for the **original reconstructed-source cutoff metric**, including its determinant, nilpotent scaling, and arithmetic weight defect.

The heat calculation also gives a denominator-free evaluation of the three original projected currents. At a specified linear-in-$q$ heat depth, its **summed full-window error is exponentially small**. This controls the approximation error; it does not assign a sign to an unevaluated current.

There is one correction to propagate first.

## 1. The repository corrects the scope of the earlier coefficient-image calculation

The repository distinguishes the consecutive minor $I_0$ from the originally retained minor $I$. Its exact change of coefficient section is

$$
\boxed{
L_I=F_C D_{0I}+L_0M_{0I},
}
\tag{1}
$$

with $M_{0I}$ invertible. The native metric satisfies

$$
D_I=M_{0I}^*D_0M_{0I},
$$

because the conductor contribution is removed by the native lower-evaluation minimum. The arithmetic pullback is instead

$$
\begin{aligned}
L_I^*GL_I
={}&M_{0I}^*G_{00}M_{0I}
+D_{0I}^*G_{CC}D_{0I}\\
&+M_{0I}^*G_{0C}D_{0I}
+D_{0I}^*G_{C0}M_{0I}.
\end{aligned}
\tag{2}
$$

These are the actual four terms. The consecutive-chart result

$$
\operatorname{im}L_0=\mathcal P_{m-1}
$$

does not establish that equality for $L_I$ while $F_CD_{0I}$ remains. The repository explicitly identifies this issue. 

Accordingly, my earlier low-degree localization and compression results retain their **consecutive-chart qualification**. I do not use them below as statements about an arbitrary retained minor. The observation-kernel calculations use $K=\ker\Lambda$ itself, and the new heat comparisons act on the full original Gram before any coefficient section is pulled back.

---

# 2. The heat-comparison constant has subexponential growth

The new GitHub construction retains the fixed one-factor divisor $h$, its full jet space, and the original physical norm $L^2(\mathbb R_{>0},dx)$. Its full finite Gram is

$$
\mathbb G_N=
\begin{pmatrix}
A_0&C_N\\
C_N^*&S_N
\end{pmatrix},
\qquad
A_0=R_h^*R_h,
$$

and its attained one-factor quotient is

$$
H_N^{(1)}=A_0-C_NS_N^{-1}C_N^*.
$$

The repository proves the exact identity

$$
\boxed{
c_N^2
=
\lambda_{\max}\!\left(
(H_N^{(1)})^{-1/2}A_0(H_N^{(1)})^{-1/2}
\right)
}
\tag{3}
$$

and $c_N\to\infty$, but leaves its growth rate unassigned. Its heat error is

$$
2^{-(J+1)/2}c_N.
$$

All these matrices use the full original section, arithmetic unit, and relation block.  

The following calculation resolves the exponential growth scale:

$$
\boxed{
c_N\longrightarrow\infty,
\qquad
\lim_{N\to\infty}\frac{\log c_N}{N}=0.
}
\tag{4}
$$

The divergence in (4) is the repository’s result. The subexponential upper estimate is the new deduction.

## 2.1 First obtain a completely finite bound

Put

$$
F_h(z)=\frac{g}{h}\!\left(\frac12+iz\right),
\qquad
w_h(y)=\frac{|F_h(y)|^2}{2\pi},
\qquad g=2\xi,
$$

and let $d_h=\deg h$.

On the stipulated quartet domain, $F_h(0)\ne0$. This does not require a zero-free-region assumption: the paired alternating series for $\eta(1/2)$ is strictly positive, while

$$
\zeta(1/2)=\frac{\eta(1/2)}{1-\sqrt2}\ne0,
$$

and $h(1/2)\ne0$.

Define

$$
f_0=|F_h(0)|,\qquad
M_0=\max_{|z|=1}|F_h(z)|,
\qquad
b_0=\min\left\{\frac12,\frac{f_0}{4M_0}\right\}.
$$

Cauchy’s coefficient formula gives

$$
|F_h(y)-F_h(0)|
\le \frac{M_0b_0}{1-b_0}\le\frac{f_0}{2}
\qquad(|y|\le b_0),
$$

so

$$
\boxed{
w_h(y)\ge w_*:=\frac{f_0^2}{8\pi}
\qquad(|y|\le b_0).
}
\tag{5}
$$

Let

$$
R_h=\max_{\rho\mid h}\left|\frac{\rho-\frac12}{i}\right|,
\qquad
B_h=1+\frac{2(R_h+1)}{b_0}.
$$

For the Legendre polynomials,

$$
|P_n(z)|\le(1+2R)^n\qquad(|z|\le R).
$$

This follows directly by induction from

$$
(n+1)P_{n+1}(z)=(2n+1)zP_n(z)-nP_{n-1}(z);
$$

the recurrence is the standard Legendre one. ([DLMF](https://dlmf.nist.gov/18.9))

Expansion in the orthonormal Legendre basis on $[-b_0,b_0]$, followed by (5), therefore gives

$$
\sup_{|z|\le R_h+1}
\left|P\!\left(\frac12+iz\right)\right|
\le
\frac{(N+1)B_h^N}{\sqrt{2b_0w_*}}\,
\|P\|_{w_h},
\qquad \deg P\le N.
\tag{6}
$$

Cauchy’s formula on the unit circles about the original jet points bounds every divided derivative by the same right-hand side.

Let $\mathsf T_h$ be multiplication by the complete unit $j_h(g/h)$ in the original divided-jet coordinates. Then the original quotient value is

$$
u=\mathsf T_hj_hP,
$$

and (6) proves

$$
\boxed{
H_N^{(1)}
\succeq
\frac{2b_0w_*}
{d_h\|\mathsf T_h\|^2(N+1)^2B_h^{2N}}\,I.
}
\tag{7}
$$

Combining (3) and (7),

$$
\boxed{
c_N\le C_h(N+1)B_h^N,
\qquad
C_h=
\sqrt{
\frac{d_h\|\mathsf T_h\|^2\|A_0\|}
{2b_0w_*}
}.
}
\tag{8}
$$

Every quantity in $C_h$ is fixed one-factor data. There is no growing Gram inverse inside it.

## 2.2 Remove the positive exponential rate

The preceding bound uses a small interval only to obtain a positive lower density. The zeros of the original density can instead be retained by an explicit polynomial factor.

Fix a large $R>0$, with neither endpoint a zero of $F_h$. Let

$$
p_R(y)=
\prod_{\substack{t\in[-R,R]\\F_h(t)=0}}
(y-t)^{n_t},
\qquad d_R=\deg p_R,
$$

where $n_t$ is the full analytic multiplicity.

The quotient $F_h/p_R$ has no zero on $[-R,R]$. Consequently,

$$
\omega_R=
\min_{|y|\le R}\frac{|F_h(y)/p_R(y)|^2}{2\pi}>0,
$$

and

$$
\|p_RP\|_{L^2[-R,R]}
\le\omega_R^{-1/2}\|P\|_{w_h}.
\tag{9}
$$

This retains the density’s real zeros rather than asserting a positive lower bound across them.

At every original root of $h$, the cofactor $g/h$ is nonzero. Choose fixed small Cauchy circles around those roots on which $F_h$ has no zero. Every $p_R$ is nonzero on these circles. Put

$$
m_R=\min_{\text{those circles}}|p_R|>0.
$$

Apply the Legendre estimate to the polynomial $p_RP$, of degree at most $N+d_R$, and then divide by $p_R$ on those circles. There is a fixed $R_0$, independent of $R,N$, such that

$$
\boxed{
c_N
\le
C_{h,R}(N+d_R+1)
\left(1+\frac{2R_0}{R}\right)^{N+d_R}.
}
\tag{10}
$$

The constant $C_{h,R}$ consists of $m_R,\omega_R$, the fixed Cauchy radii, and the same full jet and reference-section matrices. It is finite for each fixed $R$.

For each such $R$,

$$
\limsup_{N\to\infty}\frac{\log c_N}{N}
\le
\log\left(1+\frac{2R_0}{R}\right).
$$

Now let $R\to\infty$. Since $c_N\ge1$ once the relation block is present, this proves (4).

**No polynomial rate for $c_N$ has been asserted.** What is now settled is its exact exponential scale: zero.

---

# 3. The original projected currents admit a denominator-free computation

The repository’s new response proof retains

$$
Q_N=(\Lambda G_N^{-1}\Lambda^*)^{-1},
$$

$$
\Omega_N=\Lambda^*Q_N\Lambda,\qquad
L_N=G_N-\Omega_N=G_NP_{K,N}.
$$

Here $K=\ker\Lambda$, and $P_{K,N}$ is its projection in the actual arithmetic metric. The vectors remain

$$
a_1=b_N,\qquad a_2=b_{N+1},\qquad v=v_\lambda.
$$

Define

$$
F_i=a_i^*G_Nv,\qquad
K_i=a_i^*L_Nv,\qquad
B_i=a_i^*\Omega_Nv=F_i-K_i,
$$

$$
E_N=v^*G_Nv,\qquad
d_i=a_i^*G_Na_i,\qquad
\kappa_N=\frac{\sqrt{d_1d_2}}{\omega_N}.
$$

The original source identity is

$$
\mathfrak c_N
=\frac{\overline{F_1}F_2}{\omega_NE_N},
$$

and its three products are $\overline UV$, $(1-\overline U)(1-V)$, and their complementary cross term.  

Substituting those definitions gives

$$
\boxed{
\begin{aligned}
\Phi_{K,N}
&=\frac2{\omega_N}\Re(\overline{K_1}K_2),\\
\Phi_{B,N}
&=\frac2{\omega_N}\Re(\overline{B_1}B_2),\\
\Phi_{\times,N}
&=\frac2{\omega_N}
\Re(\overline{K_1}B_2+\overline{B_1}K_2).
\end{aligned}
}
\tag{11}
$$

The divisions by $F_1,F_2$ cancel **algebraically**, before approximation. These formulas retain both cross products.

## 3.1 Full perturbation bound in the original metric

Let $G_N'$ be the heat approximation constructed in HM. Keep the original vectors $a_1,a_2,v$ and the original $\omega_N$; do not recompute them from a different monic system.

Suppose the proved comparison gives

$$
(1-\eta)G_N\preceq G_N'\preceq(1+\eta)G_N,
\qquad 0<\eta\le\frac14.
$$

The repository’s HR calculation supplies

$$
|K_i'-K_i|\le2\eta\sqrt{d_iE_N},
\qquad
|B_i'-B_i|\le\eta\sqrt{d_iE_N}.
\tag{12}
$$

Its proof uses the full quotient minimum for $\Omega_N$, not a fixed Euclidean projection. 

Define $\widetilde\Phi_{X,N}$ by the three polynomial products in (11), using $K_i',B_i'$. Expanding every product gives

$$
\boxed{
\begin{aligned}
|\widetilde\Phi_{K,N}-\Phi_{K,N}|
&\le2\kappa_NE_N(4\eta+4\eta^2),\\
|\widetilde\Phi_{B,N}-\Phi_{B,N}|
&\le2\kappa_NE_N(2\eta+\eta^2),\\
|\widetilde\Phi_{\times,N}-\Phi_{\times,N}|
&\le2\kappa_NE_N(6\eta+4\eta^2).
\end{aligned}}
\tag{13}
$$

For example, the first bound is the sum of the two linear corrections and the actual quadratic correction:

$$
\overline{K_1'}K_2'-\overline{K_1}K_2
=
\overline{(K_1'-K_1)}K_2
+\overline{K_1}(K_2'-K_2)
+\overline{(K_1'-K_1)}(K_2'-K_2).
$$

With $E_N'=v^*G_N'v$, (13) yields the common normalized bound

$$
\boxed{
\left|
\frac{\widetilde\Phi_{X,N}}{2E_N'}
-\frac{\Phi_{X,N}}{2E_N}
\right|
\le12\kappa_N\eta,
\qquad X=K,B,\times.
}
\tag{14}
$$

This calculation remains defined even when an approximate $F_i'$ vanishes.

It is related explicitly to HR’s ratio-based approximation. On the common nonzero-denominator domain, put

$$
\mathfrak c_N'
=\frac{\overline{F_1'}F_2'}{\omega_NE_N'}.
$$

Then

$$
\widetilde\Phi_{X,N}
-\Phi_{X,N}^{\mathrm{HR}}
=
2E_N'\Re\!\left[
(\mathfrak c_N'-\mathfrak c_N)P_{X,N}'
\right].
\tag{15}
$$

Thus (11)-(14) are not obtained by silently identifying two different approximate currents.

## 3.2 A finite upper bound for the amplification

This can be bounded without an unknown observation Gram.

Retain the original full-source constants

$$
\underline a_k(1+y^2)^{-M_h}\sigma(y)
\le m_k(y)\le\overline a_k\sigma(y),
\qquad M_h=21+4m_0,
$$

and their polynomial comparison factor

$$
D_n=[1+4(n+M_h)^2]^{M_h}.
$$

The exact $\underline a_k,\overline a_k$, including the original masses and convolution constants, are those already supplied in EC14/GRA3. `Untitled 1775.md`

Let

$$
n_*=2q+2,\qquad
R_k=k\sqrt{\delta_\rho^2+\gamma^2},\qquad
\tau=\pi/4,
$$

and define

$$
\boxed{
\underline\Delta_k
=
\min\left\{
\frac12,\,
\frac{\underline a_k\sqrt{2\pi}}
{2D_{n_*}e^{\tau R_k}M_h(\tau)^k}
\left(\frac{\tau^2}{4}\right)^{n_*}
\right\}.
}
\tag{16}
$$

For the original rank-$r$ monic relation minimum $\nu_r$, the actual trial $y^rQ(y)$ gives, with $n=q+r$,

$$
\nu_r
\le
2e^{\tau R_k}M_h(\tau)^k(2n)!\tau^{-2n}.
$$

The source minimum satisfies

$$
\omega_n
\ge
\frac{\underline a_k}{D_{n_*}}\,
\sqrt{2\pi}\frac{(2n)!}{4^n}.
$$

Consequently the original ratio obeys

$$
\Delta_r=\frac{\omega_{q+r}}{\nu_r}\ge\underline\Delta_k
$$

through the required window.

Set

$$
\overline b_k
=
\max\left\{
1,\,
\frac{\overline a_kD_{n_*}}{\underline a_k}(n_*+1)^2
\right\}.
$$

The full source comparison gives $\omega_{n+1}/\omega_n\le\overline b_k$. The original rank-two boundary formula therefore proves

$$
\boxed{
\kappa_N\le
\overline\kappa_k:=
\sqrt{\overline b_k/\underline\Delta_k},
\qquad
\log\overline\kappa_k=O_h(q).
}
\tag{17}
$$

There is also a finite common lower bound for both source denominators. The exact identities

$$
|\mathfrak c_N|^2=\kappa_N^2p_{1,N}p_{2,N},
\qquad
\Re\mathfrak c_N=k\delta_\rho
$$

give

$$
\boxed{
p_{i,N}\ge
p_*:=
\min\left\{
\frac12,\,
\frac{k^2\delta_\rho^2}{\overline\kappa_k^2}
\right\},
\qquad i=1,2.
}
\tag{18}
$$

All full primary multiplicities remain in $q,\chi$, the source minima, and the terminal class.

---

# 4. The whole-window heat depth now has an evaluated leading coefficient

The repository proves

$$
(1-t_J)^{2k}G_N
\preceq G_N^{[J]}
\preceq(1+t_J)^{2k}G_N,
\qquad
t_J=2^{-(J+1)/2}c_*,
\tag{19}
$$

where $c_*$ is the maximum of the original one-factor constants over the finite cutoff family. The multinomial tensor map and the identical full $\chi$-fibres are part of that proof. 

By (4), throughout the growing original window,

$$
\boxed{\log c_*=o_h(q).}
\tag{20}
$$

## 4.1 Finite depth attaining stated error tolerances

A completely finite upper value for $c_*$ is supplied by (8):

$$
\overline c_k=C_h(n_*+1)B_h^{n_*}.
$$

For a chosen $\eta_*\le1/4$, define

$$
d_*=(1+\eta_*)^{1/(2k)}-1,
$$

$$
\boxed{
J=
\max\left\{
0,\,
\left\lceil2\log_2(\overline c_k/d_*)\right\rceil-1
\right\}.
}
\tag{21}
$$

Then the symmetric relative error in (12) is at most $\eta_*$.

For the original weights $w_N=1,2,\ldots,2,1$, whose sum is $2q$, equation (14) gives

$$
\boxed{
\sum_{N=q-1}^{2q-1}w_N
\left|
\frac{\widetilde\Phi_{X,N}}{2E_N'}
-\frac{\Phi_{X,N}}{2E_N}
\right|
\le24q\,\overline\kappa_k\eta_*.
}
\tag{22}
$$

Thus $\eta_*\le\varepsilon/(32q\overline\kappa_k)$ attains error at most $\varepsilon$ for each of the three complete weighted current sums.

For the original complex responses, HR gives

$$
|U_N'-U_N|,\ |V_N'-V_N|
\le6\eta_*/p_*
$$

under $\eta_*\le\sqrt{p_*}/2$. These guards can be included in the same minimum defining $\eta_*$.

For a specified determinant return with total absolute weighted rank $B_{\det}$, the same comparison gives

$$
|\mathcal L'-\mathcal L|
\le B_{\det}[-\log(1-\eta_*)].
\tag{23}
$$

The finite choices (16)-(23) give

$$
J=O_h\!\left(q+\log^+(1/\varepsilon)\right)
$$

for all these original receivers. This is a bound on dyadic heat depth, not a claim about the computational cost of evaluating all heat integrals.

## 4.2 The sharp exponential-scale depth on the simple stratum

The new full-window proof supplies

$$
-\log p_{1,q-1+r}
=
2q\psi(r/q)+O_h(k+\log q),
$$

uniformly in the window, while $|\log p_{2,N}|=O_h(\log q)$. It also supplies

$$
|U_N|\le
\exp[O_{h,u}(k\log q)],
\qquad
|V_N|\le O_h(q/k),
$$

with the stronger parity-dependent bound retained in FW50. 

Here $\psi$ decreases on the window and

$$
\psi(0)=a_0=\log(4/\pi)>0.
$$

Therefore

$$
\boxed{
-\log\min_{N,\ i=1,2}p_{i,N}
=
2a_0q+O_h(k+\log q),
}
\tag{24}
$$

and the exact source product identity gives

$$
\boxed{
\log\max_N\kappa_N
=
a_0q+O_h(k+\log q).
}
\tag{25}
$$

Let $J_{\mathrm{guard}}$ denote the least **common** heat depth satisfying HR’s original denominator guard

$$
(1+2^{-(J+1)/2}c_*)^{2k}-1
<
\min_{N,i}\sqrt{p_{i,N}}.
$$

Solving this scalar inequality, keeping its original $c_*$, gives

$$
J_{\mathrm{guard}}+1
=
2\log_2c_*+2\log_2(2k)
-\log_2\min_{N,i}p_{i,N}+O(1).
$$

Combining (20) and (24),

$$
\boxed{
\lim_{k\to\infty}
\frac{J_{\mathrm{guard}}(k)}q
=
\frac{2\log(4/\pi)}{\log2}.
}
\tag{26}
$$

This is the threshold of the **specified HR certification guard**, not a universal lower bound on every possible numerical method.

More importantly, the same coefficient gives an explicit successful full-window prescription. For any fixed $\varepsilon_0>0$, set

$$
\boxed{
J_k=
\left\lceil
\left[
\frac{2\log(4/\pi)}{\log2}+\varepsilon_0
\right]q
\right\rceil.
}
\tag{27}
$$

Then the actual relative metric error is

$$
\eta_{J_k}
=
\exp\left[
-a_0q-\frac{\varepsilon_0\log2}{2}q+o_h(q)
\right].
$$

Equations (22), (25), and the original FW response bounds yield

$$
\boxed{
\begin{aligned}
&\max_N\bigl(|U_N^{[J_k]}-U_N|+|V_N^{[J_k]}-V_N|\bigr)\\
&\quad+
\sum_Nw_N
\left|
\frac{\widetilde\Phi_{X,N}^{[J_k]}}{2E_N^{[J_k]}}
-\frac{\Phi_{X,N}}{2E_N}
\right|\\
&\qquad\le
\exp\left[
-\frac{\varepsilon_0\log2}{2}q+o_{h,u}(q)
\right],
\qquad X=K,B,\times.
\end{aligned}}
\tag{28}
$$

**The approximation error is now below the arithmetic scale across the entire original window, including the small-denominator rows.**

For comparison, a prescribed determinant accuracy in the original $G_N$, its fixed restrictions, and its attained quotients needs only

$$
J=2\log_2c_*+O(\log q+\log^+(1/\varepsilon))=o_h(q)
$$

at fixed tolerance. The additional linear depth in (26) is the quantitatively identified response amplification.

## 4.3 Carry the heat replacement through the actual arithmetic action

The action comparison also has an explicit source-valued remainder.

For a one-factor polynomial $P$, let

$$
r=\operatorname{rem}_hP,
\qquad
\ell_h(P)=[w^{d_h-1}]r.
$$

The original and heat-modified source maps are

$$
\mathcal A_NP=P(D)a_h,
$$

$$
\mathcal A_N^{[J]}P
=(I-T_s)P(D)a_h+T_s r(D)a_h,
\qquad s=2^{J+1}.
$$

Since $D$ commutes with $T_s$ and $h(D)a_h=f_0=\Theta\phi_*$,

$$
\boxed{
D\mathcal A_N^{[J]}P
-\mathcal A_{N+1}^{[J]}(wP)
=
T_sf_0\,\ell_h(P).
}
\tag{29}
$$

This term lies in the original theta source:

$$
T_sf_0=\Theta(T_s\phi_*),\qquad T_s\phi_*\in V.
$$

The same fixed-jet proof as in §2 gives

$$
\log^+\|\ell_h\|_{\mathcal H_N^*}=o_h(N).
$$

After the literal multinomial tensor substitution, the defect is the sum of the $k$ tensor terms containing $T_sf_0\ell_h$ in one factor. Its norm, measured from the original polynomial convolution form, is bounded by

$$
\boxed{
k\,s^{-1/2}\|f_0\|
\|\ell_h\|_{\mathcal H_N^*}
(1+t_J)^{k-1}.
}
\tag{30}
$$

At $J=\lceil\varepsilon_0q\rceil$, this is

$$
\exp[-(\varepsilon_0\log2/2)q+o_h(q)].
$$

The original minimum-section boundary has not disappeared. If $T_N$ is the original attained section and $A=M_S$, its receiving equation is

$$
\boxed{
\begin{aligned}
D_{\mathrm{tot}}\mathcal A_{k,N}^{[J]}T_N
-\mathcal A_{k,N+1}^{[J]}T_{N+1}A
={}&\mathfrak D_{k,N}^{[J]}T_N\\
&+\mathcal A_{k,N+1}^{[J]}
(M_ST_N-T_{N+1}A).
\end{aligned}}
\tag{31}
$$

The second term contains the original relation-valued map

$$
M_ST_N-T_{N+1}A.
$$

Equation (30) controls the **new heat defect** in the first term. It does not delete the programme’s existing canonical boundary term in the second.

---

# 5. The new Beurling quotient is evaluated completely

The GitHub construction introduces

$$
\mathscr H_B=L^2((1,\infty),y^{-2}dy)
$$

and, for the actual finite right-primary set $Z_+$,

$$
(J_+f)_{\rho,j}
=
\frac1{j!}\int_1^\infty
f(y)(-\log y)^j y^{-\rho-1}\,dy,
\qquad 0\le j<m_\rho.
$$

Its representers are

$$
k_{\rho,j}(y)
=
\frac{(-\log y)^j}{j!}y^{1-\overline\rho},
$$

with full confluent Gram

$$
\boxed{
(\mathsf G_Z)_{(\rho,j),(\sigma,l)}
=
\frac{(-1)^{j+l}\binom{j+l}{j}}
{(\rho+\overline\sigma-1)^{j+l+1}}.
}
\tag{32}
$$

The target vector for the function $1$ is

$$
b_{\rho,j}=\frac{(-1)^j}{\rho^{j+1}}.
$$

The repository gives the lower bound $b^*\mathsf G_Z^{-1}b$ and the original theta receiver $R_{Z_+}J_+$, but leaves this scalar in inverse-Gram form. 

## 5.1 Evaluate the inverse-Gram scalar

Define

$$
B_Z(s)=
\prod_{\rho\in Z_+}
\left(\frac{s-\rho}{s+\overline\rho-1}\right)^{m_\rho},
\qquad
c_Z=\overline{B_Z(1)}.
$$

Then

$$
c_ZB_Z(0)=1,\qquad
|B_Z(1/2+it)|=1.
$$

Set

$$
R_Z(s)=\frac{c_ZB_Z(s)}s,\qquad
S_Z(s)=\frac{1-c_ZB_Z(s)}s.
\tag{33}
$$

The pole at zero in $S_Z$ cancels. Its remaining poles are exactly at $1-\overline\rho$, with the retained multiplicities. Therefore $S_Z$ is the Mellin transform of a vector in the span of the $k_{\rho,j}$.

The function $R_Z$ vanishes to the full prescribed orders at every $\rho$. Its inverse transform is orthogonal to that span. Thus

$$
1=s_Z+r_Z
$$

is the exact orthogonal decomposition associated with $J_+$.

Under $y=e^t$, the map

$$
f(y)\longmapsto e^{-t/2}f(e^t)
$$

is an isometry onto $L^2(0,\infty;dt)$, and the transform is the corresponding Laplace transform. Parseval, with the retained $1/(2\pi)$, gives

$$
\|r_Z\|^2
=
\frac{|c_Z|^2}{2\pi}
\int_{\mathbb R}\frac{dt}{1/4+t^2}
=|c_Z|^2.
$$

This is the same Mellin-Fourier normalization used in the original physical-space calculation. ([DLMF](https://dlmf.nist.gov/1.14))

Since $\|1\|_{\mathscr H_B}^2=1$,

$$
\boxed{
b^*\mathsf G_Z^{-1}b
=
\|s_Z\|^2
=
1-\prod_{\rho\in Z_+}
\left|\frac{1-\rho}{\rho}\right|^{2m_\rho}.
}
\tag{34}
$$

For the original right half of the quartet,

$$
\rho=\frac12+\delta_\rho+i\gamma,\qquad \overline\rho,
$$

each of multiplicity $m_0$, this becomes

$$
\boxed{
1-
\left[
\frac{(1/2-\delta_\rho)^2+\gamma^2}
{(1/2+\delta_\rho)^2+\gamma^2}
\right]^{2m_0}.
}
\tag{35}
$$

This is strictly positive on the stipulated domain.

It is the evaluated finite-primary lower term, not an asserted value of the complete finite Beurling approximation error. Indeed, for the original Beurling source span $\mathscr V_Q$,

$$
\boxed{
\operatorname{dist}(1,\mathscr V_Q)^2
=
\|s_Z\|^2+\operatorname{dist}(r_Z,\mathscr V_Q)^2.
}
\tag{36}
$$

The remaining distance is retained in the orthogonal complement.

Finite-zero Gram projections in the Nyman-Beurling problem have classical antecedents; Burnol’s analysis uses such finite-primary projection methods. The calculation here evaluates the particular matrix and theta receiver supplied in the new repository. ([arXiv](https://arxiv.org/html/math/0103058))

## 5.2 Recover every coefficient without a growing inverse

The coefficient vector $a=\mathsf G_Z^{-1}b$ follows directly from the partial fractions of (33):

$$
\boxed{
a_{\rho,j}
=
\frac{(-1)^j}{(m_\rho-j-1)!}
\left[
\frac{d^{m_\rho-j-1}}{ds^{m_\rho-j-1}}
\left((s+\overline\rho-1)^{m_\rho}S_Z(s)\right)
\right]_{s=1-\overline\rho}.
}
\tag{37}
$$

There is also an explicit inverse for arbitrary original jet data $u$.

Put

$$
H(s)=\prod_\rho(s-\rho)^{m_\rho},
\qquad
D(s)=\prod_\rho(s+\overline\rho-1)^{m_\rho},
\qquad
H_\rho=H/(s-\rho)^{m_\rho},
$$

and

$$
U_\rho(s)=\sum_{j<m_\rho}u_{\rho,j}(s-\rho)^j.
$$

The polynomial

$$
\boxed{
P_u(s)
=
\sum_\rho H_\rho(s)\,
\operatorname{rem}_{(s-\rho)^{m_\rho}}
\left(\frac{D(s)U_\rho(s)}{H_\rho(s)}\right)
}
\tag{38}
$$

has degree below $\deg H$, and $P_u/D$ has precisely the prescribed jets. Its partial fractions, by the rule in (37), give $\mathsf G_Z^{-1}u$.

Every derivative slot and every factorial is present.

## 5.3 Determinant and arithmetic action defect

The confluent Cauchy determinant is

$$
\boxed{
\det\mathsf G_Z
=
\frac{
\displaystyle\prod_{\rho<\sigma}
|\rho-\sigma|^{2m_\rho m_\sigma}
}{
\displaystyle
\prod_\rho(2\Re\rho-1)^{m_\rho^2}
\prod_{\rho<\sigma}
|\rho+\overline\sigma-1|^{2m_\rho m_\sigma}
}.
}
\tag{39}
$$

This follows by applying the ordinary Cauchy determinant to separated nearby points, dividing by the within-cluster Vandermondes, and taking the divided-derivative limits. No extra factorial is introduced. The underlying Cauchy determinant identity is DLMF 1.3.14. ([DLMF](https://dlmf.nist.gov/1.3))

Let $A_Z$ be multiplication by $s$ on the original divided jets, and let $e$ have entry one in every zeroth-jet position and zero elsewhere. Entrywise substitution into (32), using Pascal’s identity, proves

$$
\boxed{
A_Z\mathsf G_Z+\mathsf G_ZA_Z^*-\mathsf G_Z=ee^*.
}
\tag{40}
$$

Thus the attained metric $\mathsf H_Z=\mathsf G_Z^{-1}$ satisfies

$$
\boxed{
A_Z^*\mathsf H_Z+\mathsf H_ZA_Z-\mathsf H_Z
=
\mathsf H_Zee^*\mathsf H_Z.
}
\tag{41}
$$

Its relative weight defect has rank one, with its single nonzero eigenvalue evaluated as

$$
\boxed{
e^*\mathsf G_Z^{-1}e
=
\sum_{\rho\in Z_+}m_\rho(2\Re\rho-1).
}
\tag{42}
$$

To obtain (42), multiply (40) by $\mathsf G_Z^{-1}$ and take the trace.

The positive metric therefore comes with its explicit nonzero arithmetic weight defect. It is not a zero-defect polarization of the off-critical packet.

---

# 6. The same Cauchy Gram evaluates the reconstructed source at its singular endpoint

The new source-inversion theorem gives

$$
\psi_u=\mathcal I_\mu R_Zu,
\qquad
\mathcal I_\mu F(x)=\frac12\sum_{n\ge1}\mu(n)F(nx),
$$

with

$$
\Theta\psi_u=R_Zu,
\qquad
\mathcal M\psi_u(s)=\frac{\mathcal M R_Zu(s)}{2\zeta(s)}.
$$

It computes the full primary singularity at zero and proves that the remaining term is $O(x^2)$, with all derivatives. It does not evaluate the cutoff Gram. 

That metric can now be calculated.

## 6.1 The exact original jet-to-principal-part map

Restrict first to the original right-primary divisor $Z_+$. Write

$$
\zeta(\rho+z)=z^{m_\rho}\zeta_\rho(z),
\qquad \zeta_\rho(0)\ne0.
$$

In the original divided-jet coordinates, define

$$
\boxed{
a_{\rho,j}
=
[z^{m_\rho-j-1}]
\frac{\sum_{l<m_\rho}u_{\rho,l}z^l}
{2\zeta_\rho(z)},
\qquad 0\le j<m_\rho.
}
\tag{43}
$$

Call this blockwise invertible map $a=\mathsf U_Zu$. It is the complete principal-part map of $\mathcal M\psi_u$, including the original $1/2$ and every derivative of the local zeta unit.

Its determinant is

$$
\boxed{
|\det\mathsf U_Z|
=
\prod_\rho
\left(
2\left|\frac{\zeta^{(m_\rho)}(\rho)}{m_\rho!}\right|
\right)^{-m_\rho}.
}
\tag{44}
$$

The source has the exact form

$$
\psi_u(x)
=
\sum_{\rho,j}
a_{\rho,j}\,x^{-\rho}
\frac{(-\log x)^j}{j!}
+r_u(x),
\qquad r_u(x)=O(x^2)
$$

near zero. For the full physical norm, subtract this singular part only on $0<x<1$. The resulting remainder is a fixed bounded map into $L^2(dx)$.

Define the actual cutoff Gram

$$
\boxed{
u^*\Gamma_Z(T)u
=
\int_{e^{-T}}^\infty|\psi_u(x)|^2\,dx.
}
\tag{45}
$$

This uses the original physical coordinate and original reconstructed functions.

## 6.2 Keep the complete nilpotent translation

Set $t=-\log x$. The singular part in the $L^2(dt)$ coordinate is

$$
e^{-t/2}\psi_u(e^{-t})
=
\sum_{\rho,j}
a_{\rho,j}e^{(\rho-1/2)t}\frac{t^j}{j!}.
$$

Reverse the finite interval by $\tau=T-t$. Define

$$
\boxed{
\mathsf E_T
=
\bigoplus_\rho
e^{(\rho-1/2)T}
\exp(TJ_{m_\rho}^{\uparrow}),
}
\tag{46}
$$

where $J_m^\uparrow$ has ones on the first superdiagonal. Explicitly,

$$
(\mathsf E_Ta)_{\rho,l}
=
e^{(\rho-1/2)T}
\sum_{j=l}^{m_\rho-1}
a_{\rho,j}\frac{T^{j-l}}{(j-l)!}.
$$

The reversed singular function is then

$$
\sum_{\rho,l}
(\mathsf E_Ta)_{\rho,l}
e^{-(\rho-1/2)\tau}
\frac{(-\tau)^l}{l!}.
\tag{47}
$$

The infinite-$\tau$ Gram of these functions is exactly

$$
\widehat{\mathsf G}_Z
=
\overline{\mathsf G_Z}.
$$

On a conjugation-stable set, this is also $C^*\mathsf G_ZC$, where $C$ is the explicit permutation $(\rho,j)\mapsto(\overline\rho,j)$.

Consequently,

$$
\boxed{
\mathsf E_T^{-*}\mathsf U_Z^{-*}
\Gamma_Z(T)
\mathsf U_Z^{-1}\mathsf E_T^{-1}
\longrightarrow
\widehat{\mathsf G}_Z.
}
\tag{48}
$$

This is the precise matrix comparison between the original inverse-source endpoint and the new Beurling Gram.

## 6.3 A finite error bound

Put

$$
d_*=\min_{\rho\in Z_+}(\Re\rho-\tfrac12)>0,
\qquad
m_*=\max_\rho m_\rho,
$$

$$
P_*(T)=\sum_{j=0}^{m_*-1}\frac{T^j}{j!}.
$$

Let $R_0$ bound the fixed regular remainder map in the principal-part coordinates $a$. Then

$$
\|\mathsf E_T^{-1}\|
\le e^{-d_*T}P_*(T).
$$

The discarded tail of (47) has operator norm at most its trace,

$$
\boxed{
\begin{aligned}
\mathcal T_Z(T)
={}&
\sum_{\rho}\sum_{j=0}^{m_\rho-1}
\frac{(2j)!e^{-2d_\rho T}}
{(j!)^2(2d_\rho)^{2j+1}}
\sum_{l=0}^{2j}\frac{(2d_\rho T)^l}{l!},\\
&d_\rho=\Re\rho-\tfrac12.
\end{aligned}}
\tag{49}
$$

Thus the norm of the difference in (48) is at most

$$
\boxed{
\begin{aligned}
\mathcal E_Z(T)
={}&\mathcal T_Z(T)
+2\sqrt{\|\mathsf G_Z\|}\,
R_0e^{-d_*T}P_*(T)\\
&+R_0^2e^{-2d_*T}P_*(T)^2.
\end{aligned}}
\tag{50}
$$

The constant $R_0$ does not conceal a growing source inverse. It can be bounded from the explicit MI6 integrals. For

$$
\phi_*(x)=(4\pi^2x^4-6\pi x^2)e^{-\pi x^2},
\qquad C_\phi=4\pi^2+6\pi,
$$

the regular part of $S_\rho^\ell\phi_*$ has squared norm at most

$$
\frac{C_\phi^2}{5(\Re\rho+2)^{2\ell}}
+\frac12
\left[
\frac{C_\phi}{2(\ell-1)!}
\left(\frac\pi2\right)^{-(\Re\rho+\ell+3)/2}
\Gamma\!\left(\frac{\Re\rho+\ell+3}{2}\right)
\right]^2.
\tag{51}
$$

The finite triangular map from $a$ to the MI6 coefficients is obtained by multiplying the principal parts by the Taylor series of $1/\mathcal M\phi_*(\rho+z)$. Applying its norm to the finite sum of (51) gives $R_0$.

Moreover,

$$
g_*=
\frac{\det\mathsf G_Z}
{(\operatorname{Tr}\mathsf G_Z)^{d_Z-1}}>0,
\qquad d_Z=\sum_\rho m_\rho,
$$

is an explicit lower bound for $\lambda_{\min}(\mathsf G_Z)$. Therefore (50), divided by $g_*$, is a relative metric error bound.

## 6.4 The determinant, including its constant term

The nilpotent exponential in (46) has determinant one. Hence

$$
|\det\mathsf E_T|^2
=
\exp\left[
2T\sum_\rho m_\rho(\Re\rho-\tfrac12)
\right].
$$

Equations (39), (44), and (48) give

$$
\boxed{
\begin{aligned}
\log\det\Gamma_Z(T)
={}&
2T\sum_\rho m_\rho(\Re\rho-\tfrac12)\\
&-2\sum_\rho m_\rho
\log\left(
2\left|\frac{\zeta^{(m_\rho)}(\rho)}{m_\rho!}\right|
\right)
+\log\det\mathsf G_Z\\
&+O_Z\!\left(T^{m_*-1}e^{-d_*T}\right).
\end{aligned}}
\tag{52}
$$

**There is no $\log T$ term for a complete right-primary block.** Individual jet directions have polynomial factors, but the full nilpotent translation has determinant one.

For the original right conjugate pair of common multiplicity $m_0$,

$$
\boxed{
\begin{aligned}
\log\det\Gamma_+(T)
={}&4m_0\delta_\rho T
-4m_0\log\left(
2\left|\frac{\zeta^{(m_0)}(\rho)}{m_0!}\right|
\right)\\
&+2m_0^2
\log\frac{\gamma}
{2\delta_\rho\sqrt{\delta_\rho^2+\gamma^2}}
+o(1).
\end{aligned}}
\tag{53}
$$

The full quartet can also be retained before minimization. Split its reconstructed-source Gram into right and left primary blocks. The left block converges to its positive $L^2(dx)$ Gram. After the right transformation in (48), the cross block tends to zero: split the logarithmic interval at $T/2$, using right-end exponential localization on one half and left-source decay on the other.

Thus the attained right-value quotient

$$
\Gamma_{++}
-\Gamma_{+-}\Gamma_{--}^{-1}\Gamma_{-+}
$$

has the same limit (48) and determinant expansion (53). The complete left minimum and its cross terms are present in this statement.

This quotient is explicitly $E_h/E_-$, with value map $[u_++u_-]\mapsto u_+$. It has not been substituted for PRD’s different $Z_R$ quotient.

---

# 7. The endpoint calculation also evaluates the nilpotent metric spectrum and action defect

## 7.1 Every singular scale of one right-primary block

For a single original primary of multiplicity $m$, put

$$
b_\rho=2\Re\rho-1>0.
$$

In principal-part coordinates, the eigenvalues of the cutoff metric, ordered decreasingly, are

$$
\boxed{
\lambda_r(T)
=
e^{b_\rho T}
\left(\frac{(r-1)!}{(m-r)!}\right)^2
b_\rho^{-(2r-1)}
T^{2(m+1-2r)}
\left[1+O_{\rho,m}(T^{-1})\right],
\quad1\le r\le m.
}
\tag{54}
$$

Equivalently, these are the generalized eigenvalues of the original $\Gamma_\rho(T)$ relative to the explicit reference $\mathsf U_\rho^*\mathsf U_\rho$. The map $u\mapsto\mathsf U_\rho u$ proves that equivalence.

To derive (54), the largest degree of a minor of order $r$ in $e^{TJ_m^\uparrow}$ is $r(m-r)$. Its unique extreme minor has coefficient

$$
c_{m,r}
=
\prod_{j=0}^{r-1}\frac{j!}{(m-r+j)!}.
$$

The coefficient follows by factoring each column and taking the Vandermonde of its falling factorials. All other minors have smaller degree.

The leading principal Cauchy Gram determinant of order $r$ is $b_\rho^{-r^2}$. Therefore the product of the largest $r$ metric eigenvalues has leading value

$$
e^{rb_\rho T}
c_{m,r}^2b_\rho^{-r^2}T^{2r(m-r)}.
$$

Taking consecutive ratios proves (54).

The powers

$$
m-1,\ m-3,\ldots,1-m
$$

are therefore present in the actual source metric. They have not been removed by retaining only the terminal eigenvector.

## 7.2 The critical primary has a different, explicitly computed finite limit

For an original critical primary $\Re\rho=1/2$, define

$$
D_T=\operatorname{diag}(T^{j+1/2})_{j=0}^{m-1}.
$$

The same finite integral, now evaluated at zero real displacement, gives

$$
\boxed{
D_T^{-1}\mathsf U_\rho^{-*}\Gamma_\rho(T)
\mathsf U_\rho^{-1}D_T^{-1}
\longrightarrow
\mathsf H_m,
\qquad
(\mathsf H_m)_{ij}
=\frac1{i!j!(i+j+1)}.
}
\tag{55}
$$

Indeed, its singular contribution is exactly

$$
\int_0^T\frac{t^{i+j}}{i!j!}\,dt
=
\frac{T^{i+j+1}}{i!j!(i+j+1)}.
$$

The regular remainder has normalized norm $O(T^{-1/2})$. Consequently,

$$
\boxed{
\log\det\Gamma_\rho(T)
=
m^2\log T
-2m\log\left(
2\left|\frac{\zeta^{(m)}(\rho)}{m!}\right|
\right)
+\log\prod_{j=0}^{m-1}\frac{j!}{(m+j)!}
+O_\rho(T^{-1/2}).
}
\tag{56}
$$

The coefficient is $m^2$, with the complete multiplicity.

## 7.3 The original relative arithmetic weight is evaluated as well

The principal-part map intertwines the original arithmetic action with

$$
A_{\mathrm{pp}}
=
\bigoplus_\rho(\rho I+J_{m_\rho}^{\uparrow}),
\qquad
\mathsf U_ZA_Z=A_{\mathrm{pp}}\mathsf U_Z.
\tag{57}
$$

This follows by multiplying each principal part by $s$: the new coefficient is $\rho a_j+a_{j+1}$.

The endpoint transformation $\mathsf E_T$ commutes with $A_{\mathrm{pp}}$. Equation (48) therefore evaluates the generalized eigenvalues of

$$
A_Z^*\Gamma_Z(T)+\Gamma_Z(T)A_Z-\Gamma_Z(T).
$$

On the right-primary divisor,

$$
\boxed{
\operatorname{spec}\!\left[
\Gamma_Z(T)^{-1/2}
(A_Z^*\Gamma_Z(T)+\Gamma_Z(T)A_Z-\Gamma_Z(T))
\Gamma_Z(T)^{-1/2}
\right]
\longrightarrow
\left\{
\sum_\rho m_\rho(2\Re\rho-1),\,
0,\ldots,0
\right\}.
}
\tag{58}
$$

For a single critical primary, its two possible nonzero leading eigenvalues are

$$
\boxed{
\pm\frac{m\sqrt{m^2-1}}{T}
+O_\rho(T^{-3/2}),
}
\tag{59}
$$

and the remaining eigenvalues are $O_\rho(T^{-3/2})$. For $m=1$, the defect is exactly zero.

Here is the finite matrix calculation behind (59). With $N=J_m^\uparrow$,

$$
N^*\mathsf H_m+\mathsf H_mN
=bb^*-e_0e_0^*,
\qquad b_j=1/j!.
$$

The shifted Legendre kernel on $[0,1]$ gives

$$
b^*\mathsf H_m^{-1}b
=e_0^*\mathsf H_m^{-1}e_0=m^2,
$$

$$
e_0^*\mathsf H_m^{-1}b=(-1)^{m-1}m.
$$

Thus the relative rank-two matrix has eigenvalues
$\pm m\sqrt{m^2-1}$. Under $D_T$, the nilpotent becomes $N/T$, proving (59).

These are values of the relative defect in the specified reconstructed-source cutoff metric-not conclusions drawn merely from its shrinking or growing absolute norm.

## 7.4 The comparison back to the Beurling metric retains the boundary map

For a conjugation-stable right divisor, define

$$
\boxed{
M_T=\mathsf G_Z\,C\,\mathsf E_T\,\mathsf U_Z.
}
\tag{60}
$$

It is invertible, with its explicit factorwise inverse. Since $\mathsf H_Z=\mathsf G_Z^{-1}$,

$$
M_T^*\mathsf H_ZM_T
=
\mathsf U_Z^*\mathsf E_T^*
\widehat{\mathsf G}_Z
\mathsf E_T\mathsf U_Z.
$$

This is the reference metric in (48), on the **same original $u$-coordinates**.

Its action equation is

$$
\boxed{
M_TA_Z=(I-A_Z)M_T+e\,\ell_T,
\qquad
\ell_T=e^*C\mathsf E_T\mathsf U_Z.
}
\tag{61}
$$

Equation (61) follows by substituting (40). The row $\ell_T$ is the normalized singular-source value at the retained endpoint $x=e^{-T}$. It is nonzero.

The actual cutoff metric also has an exact integration-by-parts identity. Let

$$
D\psi_u=\psi_{A_Zu}+\phi_*\,\ell_{\mathrm{ref}}(u),
$$

where $\ell_{\mathrm{ref}}$ is the original highest-coefficient functional of the canonical section. Then

$$
\boxed{
\begin{aligned}
A_Z^*\Gamma_Z(T)+\Gamma_Z(T)A_Z-\Gamma_Z(T)
={}&e^{-T}\Psi(e^{-T})^*\Psi(e^{-T})\\
&-\ell_{\mathrm{ref}}^*
\langle\phi_*,\Psi\rangle_{[e^{-T},\infty)}\\
&-\langle\Psi,\phi_*\rangle_{[e^{-T},\infty)}
\ell_{\mathrm{ref}}.
\end{aligned}}
\tag{62}
$$

Both source cross terms remain. Equations (58)-(61) describe their controlled endpoint limit; they do not erase them from the finite arithmetic comparison.

---

# 8. Propagation to the original observation and the remaining programme values

The latest local observability proof applies to $K_k=\ker\Lambda_k$ itself and proves

$$
K_\infty=0
$$

on its explicit full-support period locus, including every fixed $|u|\ge R_{\mathrm{det}}$ for the stated eventual degrees. It gives the actual full-packet inverse, not merely a rank count. `04_FULL_ORIGINAL_OBSERVABILITY.md` `04_FULL_ORIGINAL_OBSERVABILITY.md`

On that locus, every terminal column is detected, so

$$
(\Lambda v)^*Q_N(\Lambda v)>0,\qquad \theta_N<1
$$

at every original cutoff. The new full-window class-energy formula can therefore be used in its logarithmic form without leaving a zero-observation alternative:

$$
\boxed{
\begin{aligned}
&\log
\frac{
(\Lambda v)^*Q_{q-1}(\Lambda v)\,
(\Lambda v)^*Q_q(\Lambda v)
}{
(\Lambda v)^*Q_{2q-1}(\Lambda v)\,
(\Lambda v)^*Q_{2q}(\Lambda v)
}\\
&\quad=
C_\partial q
+\log\frac{
(1-\theta_{q-1})(1-\theta_q)
}{
(1-\theta_{2q-1})(1-\theta_{2q})
}
+O_{h,u}(k+\log q).
\end{aligned}}
\tag{63}
$$

The first term is the repository’s evaluated full terminal-class loss. The second is the actual observation-angle correction.  

That remaining scalar has a particularly clean heat error. HR4 gives

$$
\frac{\alpha}{\beta}(1-\theta_N)
\le1-\theta_N^{[J]}
\le\frac{\beta}{\alpha}(1-\theta_N),
$$

so the four-endpoint angle return has error at most

$$
\boxed{
8k\log\frac{1+t_J}{1-t_J}.
}
\tag{64}
$$

There is no denominator $1-\theta_N$ in this error bound. The small observed energy is controlled multiplicatively through its actual quotient metric.

The work completed in this pass is therefore:

| Object | New calculation |
|---|---|
| Original heat constant $c_N$ | Finite exponential bound and the stronger $\log c_N=o(N)$. |
| Original $U,V$ and three projected currents | Explicit full-window heat depth, evaluated leading guard coefficient, and exponentially small propagated error. |
| Heat arithmetic action | Exact source-valued defect (29), tensor bound (30), and unchanged minimum-section boundary (31). |
| New Beurling finite quotient | Scalar value, inverse coefficients, determinant, and rank-one weight defect, all with full multiplicity. |
| Original inverse-source endpoint metric | Complete determinant asymptotic, nilpotent metric scales, critical multiplicity coefficient, and relative action spectrum. |
| Observation/class-energy receiver | The detected-class branch is activated on the established original period locus, with angle-error bound (64). |

The outstanding values remain

$$
\mathcal R\log\det(I_K^*G_NI_K),
$$

$$
\mathcal M^p
=
\mathcal R\log\det\!\left[
(Q_N^p)^{-1/2}H_N^p(Q_N^p)^{-1/2}
\right],
$$

and the actual signed evaluations of the projected-current numerators in (11). The proper-source annihilator from the preceding local work still retains the target’s full $J$-minimum; none of the new Beurling or endpoint metrics has been inserted in its place. `03_PROPER_SOURCE_ANNIHILATOR.md`

The new results remove an unquantified growth constant and the uncontrolled approximation amplification from the original arithmetic current calculation. They also evaluate the new finite-primary Hilbert receiver and its exact source-endpoint/action comparison. **They do not yet evaluate the remaining native orientations or produce the required same-class Frobenius comparison.**

The execution runtime failed repeatedly during this turn. These are written derivations from the cited repository inputs and the proofs above; I am not claiming an executed numerical test suite, a new downloadable bundle, or a GitHub commit.

---

**Sources:**

- [https://dlmf.nist.gov/18.9](https://dlmf.nist.gov/18.9)
- [https://arxiv.org/html/math/0103058](https://arxiv.org/html/math/0103058)



---
Powered by [ChatGPT Exporter](https://www.chatgptexporter.com)