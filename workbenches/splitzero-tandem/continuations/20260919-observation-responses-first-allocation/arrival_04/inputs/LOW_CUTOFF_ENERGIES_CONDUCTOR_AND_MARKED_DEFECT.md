**The new GitHub edition makes a more direct continuation possible: two of the actual source energies in its response calculation can now be evaluated at the original low cutoffs.** They behave very differently:

$$
\boxed{
\begin{aligned}
p_{1,N}
&=\exp\!\left[-2q\log(4/\pi)+O_h(k+\log q)\right],
&&N=q-1,q,\\
p_{2,q-1}
&=\frac{\pi^2(\delta^2+\gamma^2)}{16}\frac{k^2}{q^2}
\bigl(1+o_h(1)\bigr),\\
p_{2,q}&=1-o_h(1).
\end{aligned}}
\tag{1}
$$

These are the \(p_1,p_2\) of **JRE20**, not native flag eigenvalues, rank fractions, or the observation-kernel energy \(\theta\). The calculation uses the full retained eigenclass and the original arithmetic minimum metrics.

I used the repository’s new commit **`0562d35abb20ec87be85aba00a6206fcd843cd58`**, published while this run was in progress. Its continuation explicitly identifies \(p_1,p_2,\theta\) as the three scalar inputs to the joint response ellipse. It also contains the preceding \(q/\log q\) arithmetic refinement.

The implications below go further than inserting these values into an unrestricted ellipse. The **actual observation kernel** supplies an additional bound that removes the ellipse’s possible \(e^{cq}\)-scale amplification of \(U\). The concurrent absolute-baseline result also combines with the slow-tail calculation to give the **complete simple-packet canonical action through \(q/\log q\)**.

## 1. Evaluate the two original low-cutoff response energies

Retain

$$
e=1+k(m_0-1),\qquad q=e(k+1)^2,\qquad k\equiv1\pmod4,
$$

$$
c=k/2,\qquad
\lambda=k\rho=c+d+it,\qquad d=k\delta,\quad t=k\gamma,
$$

and

$$
z=\frac{\lambda-c}{i}=t-id,\qquad
R=|z|=k\sqrt{\delta^2+\gamma^2}.
$$

The complete polynomial and terminal class remain

$$
Q(y)=i^{-q}\chi_k(c+iy),\qquad
v_\lambda=
\left[
b_\lambda\frac{\chi_k(S)}{S-\lambda}
\right],
\qquad
b_\lambda=\chi_{k,\lambda}(\lambda)^{-1}.
$$

Thus repeated primaries retain their terminal power and their nonzero complete-primary denominator.

At cutoff \(N\), let

$$
W_N=[b_N,b_{N+1},v_\lambda],\qquad
F_N=W_N^*G_NW_N,\qquad E_N=(F_N)_{33}.
$$

The quantities calculated here are exactly

$$
p_{1,N}=\frac{|(F_N)_{13}|^2}{E_N(F_N)_{11}},
\qquad
p_{2,N}=\frac{|(F_N)_{23}|^2}{E_N(F_N)_{22}}.
\tag{2}
$$

Their definitions and the full three-column Gram are retained in the current JRE calculation.

### Exact identities before taking a limit

Set

$$
\nu_0=\int_{\mathbb R}Q(y)^2m_k(y)\,dy,
\qquad
\nu_1=\int_{\mathbb R}y^2Q(y)^2m_k(y)\,dy.
$$

For calculations involving ratios, introduce the auxiliary probability

$$
d\mu_Q(y)=\nu_0^{-1}Q(y)^2m_k(y)\,dy,
$$

and retain the three actual scalar integrals

$$
a_z=\int\frac{d\mu_Q(y)}{y-z},
\qquad
m_z=\int\frac{d\mu_Q(y)}{|y-z|^2},
\qquad
s_2=\int y^2\,d\mu_Q(y)=\frac{\nu_1}{\nu_0}.
\tag{3}
$$

The source mass has not been changed: \(\nu_0\) remains in every norm below.

Write

$$
d_0=\frac{\omega_q}{\nu_0},
\qquad
d_1=\frac{\omega_{q+1}}{\nu_1},
\tag{4}
$$

where \(\omega_n\) is the squared norm of the original arithmetic monic polynomial.

At \(N=q-1\), there is no relation in the minimum fibre. Consequently,

$$
P_{q-1,\lambda}(c+iy)
=b_\lambda i^{q-1}\frac{Q(y)}{y-z},
\qquad
E_{q-1}=|b_\lambda|^2\nu_0m_z.
$$

Orthogonality to all lower-degree polynomials gives

$$
(F_{q-1})_{11}=\omega_{q-1},
\qquad
|(F_{q-1})_{13}|=|b_\lambda|\omega_{q-1}.
$$

Also, the representative of \(b_q\) is \(p_q-\chi_k\), so

$$
(F_{q-1})_{22}=\nu_0-\omega_q,
\qquad
|(F_{q-1})_{23}|=|b_\lambda|\nu_0|a_z|.
$$

Therefore

$$
\boxed{
p_{1,q-1}=\frac{\omega_{q-1}}{\nu_0m_z},
\qquad
p_{2,q-1}=\frac{|a_z|^2}{(1-d_0)m_z}.
}
\tag{5}
$$

At \(N=q\), the complete relation space is the one-dimensional space spanned by \(\chi_k\). Subtracting its **actual orthogonal projection** gives

$$
P_{q,\lambda}(c+iy)
=b_\lambda i^{q-1}Q(y)
\left(\frac1{y-z}-a_z\right),
$$

and

$$
E_q=|b_\lambda|^2\nu_0(m_z-|a_z|^2).
\tag{6}
$$

The next attained monic relation is \(\chi_k(S)(S-c)\). Its preceding constant-relation projection vanishes exactly by evenness. Thus \(\nu_1\), rather than a trial norm with an omitted projection, is its attained norm.

Using

$$
\int\frac{y}{y-z}\,d\mu_Q(y)=1+za_z
$$

now gives

$$
\boxed{
\begin{aligned}
p_{1,q}
&=
\frac{d_0|a_z|^2}
{(1-d_0)(m_z-|a_z|^2)},\\
p_{2,q}
&=
\frac{|1+za_z|^2}
{s_2(1-d_1)(m_z-|a_z|^2)}.
\end{aligned}}
\tag{7}
$$

Equations (5)–(7) retain the exact first and second source minima. The coefficient \(b_\lambda\) cancels only between the matching numerator and denominator of each response energy.

### A finite enclosure for the exponentially small energy

Use the original whole-polynomial comparison

$$
\ell_k\|P\|_\sigma^2
\le \|P\|_{m_k}^2
\le u_k\|P\|_\sigma^2,
\qquad
\log(u_k/\ell_k)=O_h(k+\log q),
\tag{8}
$$

through degree \(2q\). This is a comparison before minimization, not a pointwise lower bound for the arithmetic density. 

Let \(c_G,C_G>0\) be the retained Gamma-density constants:

$$
c_G\frac{e^{-\alpha|y|}}{\sqrt{1+|y|}}
\le \sigma(y)
\le C_G\frac{e^{-\alpha|y|}}{\sqrt{1+|y|}},
\qquad \alpha=\pi/2.
$$

For a monic polynomial of degree \(n\) whose roots have modulus at most \(R\), define

$$
\mathscr L_n(R)=
\frac{2c_Ge^{-\alpha R}}{\sqrt{R+2}}\,
\alpha^{-2n-1/2}\Gamma(2n+\tfrac12,\alpha),
$$

$$
\mathscr U_n(R)=
2C_Ge^{\alpha R}\,
\alpha^{-2n-1}\Gamma(2n+1).
$$

Then

$$
\mathscr L_n(R)\le \|P\|_\sigma^2\le \mathscr U_n(R).
\tag{9}
$$

For the upper bound, use \(|P(y)|\le(|y|+R)^n\), substitute \(s=|y|+R\), and retain the complete Gamma tail. For the lower bound, integrate over \(|y|\ge R+1\), use \(|P(y)|\ge(|y|-R)^n\), and

$$
1+R+s\le(R+2)s\qquad(s\ge1).
$$

These steps prove (9) directly.

The exact Gamma monic norm is

$$
\gamma_n=\sqrt{2\pi}\,\frac{\Gamma(2n+1)}{4^n}.
$$

Applying (8)–(9) to the monic polynomial \(Q/(y-z)\), of degree \(n=q-1\), gives the finite interval

$$
\boxed{
\frac{\ell_k}{u_k}\frac{\gamma_n}{\mathscr U_n(R)}
\le p_{1,q-1}\le
\frac{u_k}{\ell_k}\frac{\gamma_n}{\mathscr L_n(R)}.
}
\tag{10}
$$

Stirling’s formula and the Gamma-ratio expansion yield

$$
\log p_{1,q-1}
=-2(q-1)\log(4/\pi)+O_h(k+\log q).
\tag{11}
$$

Here \(R=O_h(k)\), and every Gamma-ratio error is logarithmic. The classical expansions used in this step are those of NIST’s *Digital Library of Mathematical Functions*, §§5.11(i), 5.11(iii). ([DLMF][1])

The same bounds applied to \(Q\) and \(yQ\) prove

$$
\log d_0=-2q\log(4/\pi)+O_h(k+\log q),
$$

$$
\log d_1=-2(q+1)\log(4/\pi)+O_h(k+\log q).
\tag{12}
$$

In particular, both \(d_0,d_1\) tend to zero exponentially.

### Evaluate the three remaining integrals

Put

$$
Y_q=\frac{4q}{\pi}.
$$

The original opposite-root estimate, now applied to \(Q\) itself, is

$$
(y^2-R^2)^q\le Q(y)^2\le(y^2+R^2)^q\qquad(y>R),
$$

with the upper bound valid on the whole real line.

After \(y=Y_qx\), the exponential part of the upper integral is

$$
\exp\left\{q\left[\log\left(x^2+\frac{R^2}{Y_q^2}\right)-2x\right]\right\}.
$$

Its limiting exponent \(2\log x-2x\) has its unique maximum at \(x=1\). The full source-comparison width is \(o(q)\), while \(R/Y_q\to0\). This proves concentration of \(|y|/Y_q\) at one in \(d\mu_Q\), including the required second-moment control.

For completeness, the finite outside-mass bound is obtained from

$$
D_*=
\frac{2\ell_kc_G(Y_q^2-R^2)^q
e^{-\alpha(Y_q+1)}}{\sqrt{Y_q+2}}
\le\nu_0
$$

and, for \(0<b<1\),

$$
\begin{aligned}
U_j(b)={}&
2u_kC_G
\sum_{r=0}^{q}\binom qr R^{2(q-r)}
\alpha^{-(2r+j+1/2)}\\
&\times\left[
\gamma(2r+j+\tfrac12,\alpha(1-b)Y_q)
+\Gamma(2r+j+\tfrac12,\alpha(1+b)Y_q)
\right],
\end{aligned}
\tag{13}
$$

for \(j=0,2\). Thus the outside probability is at most \(U_0(b)/D_*\), and its normalized second moment is at most \(U_2(b)/(Y_q^2D_*)\). For each fixed \(b>0\), both tend to zero exponentially after the stated source factors are included. This is the same complete-integral method used in the preceding reflected-class calculation, applied to the different polynomial required here. 

Evenness gives

$$
a_z=z\int\frac{d\mu_Q(y)}{y^2-z^2}.
$$

The denominators obey

$$
|y-z|\ge d,\qquad |y^2-z^2|\ge2td.
$$

The exponentially small central mass therefore remains negligible even after these inverse denominators are included. On the concentrating annulus, both denominators have their explicit \(Y_q\)-scale limits. Consequently,

$$
\boxed{
Y_q^2m_z\longrightarrow1,\qquad
\frac{Y_q^2a_z}{z}\longrightarrow1,\qquad
\frac{s_2}{Y_q^2}\longrightarrow1.
}
\tag{14}
$$

For example, if \(\eta_b=\min(1,U_0(b)/D_*)\), then

$$
\frac{1-\eta_b}{((1+b)Y_q+R)^2}
\le m_z
\le
\frac1{((1-b)Y_q-R)^2}+\frac{\eta_b}{d^2},
$$

whenever \((1-b)Y_q>R\). Also,

$$
\left|\frac{Y_q^2a_z}{z}-1\right|
\le
\frac{2b+b^2+R^2/Y_q^2}
{(1-b)^2-R^2/Y_q^2}
+\eta_b\left(1+\frac{Y_q^2}{2td}\right).
\tag{15}
$$

Thus (14) has finite, original-source enclosures; it is not a new uncomputed Gram limit.

Substitution into (5) and (7) proves (1). More precisely,

$$
p_{1,q}
=
d_0\,\frac{\pi^2(\delta^2+\gamma^2)k^2}{16q^2}
\bigl(1+o_h(1)\bigr),
\tag{16}
$$

which, together with (12), gives its stated exponential rate.

There is an accompanying same-class norm calculation:

$$
\boxed{
\frac{E_q}{E_{q-1}}
=
1-\frac{\pi^2(\delta^2+\gamma^2)}{16}
\frac{k^2}{q^2}\bigl(1+o_h(1)\bigr).
}
\tag{17}
$$

The complete quotient determinant contracts exponentially in this first update, while this particular class norm changes by only \(O_h(k^2/q^2)\). Those are different calculated quantities.

## 2. Propagate the values into the actual response calculation

### The first-cutoff response ellipse is exponentially anisotropic

JRE19 gives the exact response matrix

$$
ET=
\begin{pmatrix}
p_1^{-1}-1&-1\\
-1&p_2^{-1}-1
\end{pmatrix}.
\tag{18}
$$

The factor \(E\) is explicit: the eigenvalues of \(T\) are the following eigenvalues divided by the original \(E\). No source metric is replaced.

At \(N=q-1\),

$$
\boxed{
\begin{aligned}
\lambda_{\max}(ET)
&=\exp\!\left[2q\log(4/\pi)+O_h(k+\log q)\right],\\
\lambda_{\min}(ET)
&=\frac{16}{\pi^2(\delta^2+\gamma^2)}
\frac{q^2}{k^2}\bigl(1+o_h(1)\bigr).
\end{aligned}}
\tag{19}
$$

Indeed, the exact two eigenvalues are

$$
\frac12\left[
p_1^{-1}+p_2^{-1}-2
\pm\sqrt{(p_1^{-1}-p_2^{-1})^2+4}
\right],
$$

and \(p_1/p_2\to0\) exponentially.

In particular,

$$
\boxed{
\lim\frac1q\log\operatorname{cond}(ET)
=2\log(4/\pi).
}
\tag{20}
$$

This evaluates a directional spectrum in the **same-class response receiver**. It is not the spectrum of a native four-dimensional flag compression.

At \(N=q\), the result \(p_2\to1\) has a different consequence. Let

$$
\theta_N=\frac{K_{33}}{E_N}
=\frac{\|P_Kv_\lambda\|_{G_N}^2}{E_N}.
$$

The exact JRE ellipse gives

$$
\boxed{
|V_q-\theta_q|
\le
\sqrt{\theta_q(1-\theta_q)
\left(\frac1{p_{2,q}}-1\right)}
=o_h(1).
}
\tag{21}
$$

The convergence is uniform over the allowed orthogonal projections because \(\theta(1-\theta)\le1/4\).

Thus the second response at the second original cutoff is asymptotically real and equals the actual kernel energy, up to the displayed error. That does **not** permit replacing

$$
\bar U_qV_q
$$

by \(\theta_q\bar U_q\) without multiplying the error in (21) by the actual \(|U_q|\).

### The original kernel gives a stronger bound than the unrestricted ellipse

The archive supplies more than the rank of \(K\). On the original simple-quartet conductor domain,

$$
K=\ker\Lambda_k\subset V_A=\ker C,
$$

and

$$
V_A=
\left\{
P\in\mathcal P_{q-1}:
\chi_{k-8}\mid\mathcal T_AP
\right\}.
\tag{22}
$$

These are the actual conductor and observation maps.  

This subsection therefore uses \(m_0=1\), \(q=(k+1)^2\), and

$$
q'=(k-7)^2,\qquad
r_N=N-v-q',\qquad N=q-1,q.
$$

Let

$$
\pi_{1,K,N}
=
\frac{\|P_Kb_N\|_{G_N}^2}{(F_N)_{11}}.
$$

Use the original normalized conductor

$$
\mathcal C_A=(v!/\mu_v)\mathcal T_A.
$$

Its leading coefficient on a degree-\(N\) polynomial is \((N)_v\) times the original leading coefficient, and its retained Gamma norm bound is

$$
\|\mathcal C_AP\|_{\sigma,c-4}
\le M_N\|P\|_{\sigma,c},
$$

where

$$
M_N=
\max\left\{
1,\frac{v!}{|\mu_v|}
\sum_{r,s}|a_{rs}|
e^{|\beta_{8,r,s}-4|(\mathsf H_N+2)}
\right\},
\qquad
\mathsf H_N=\sum_{j=1}^N\frac1j.
\tag{23}
$$

Every coefficient and the original centre displacement remain. This is the FEX bound, not a new inverse-conductor assumption. 

Let \(\nu^-_{r_N,1}\) be the complete lower-root monic minimum. A minimum representative of an element of \(K\) still satisfies the divisibility in (22), since adding an original relation preserves it. Therefore, for its leading coefficient \(a_N(P)\),

$$
\|P\|_{m_k}^2
\ge
\ell_kM_N^{-2}(N)_v^2
\nu^-_{r_N,1}|a_N(P)|^2.
\tag{24}
$$

On the other hand,

$$
\langle b_N,[P]\rangle_{G_N}
=\omega_Na_N(P).
$$

Taking the supremum over the **whole actual kernel**, rather than a chosen kernel basis, proves

$$
\boxed{
\pi_{1,K,N}
\le
\min\left\{
1,\,
\frac{u_k}{\ell_k}
\frac{M_N^2\gamma_N}
{\eta_N(N)_v^2\nu^-_{r_N,1}}
\right\},
}
\tag{25}
$$

where

$$
\eta_{q-1}=1,\qquad \eta_q=1-d_0.
$$

This retains every kernel direction and requires no nonzero projection assumption.

The original LRC monic estimate evaluates its exponential size. With \(a_0=\log(4/\pi)\),

$$
\log\nu^-_{r,1}
=
\log\gamma_{q'+r}
+2q'\psi(r/q')+O_h(\log q).
$$

The existing relation

$$
2\{\psi(t)-(1+t)\psi'(t)\}=f(t),
\qquad
f(t)=-\tfrac12\log t+O(\sqrt t)
$$

gives, by integration,

$$
\psi(t)=
a_0+\frac t4\log t+(a_0-\tfrac14)t+O(t^{3/2}).
$$

Here \(r_N=16k+O(1)\), while \(q'\asymp k^2\). Hence (25) yields

$$
\boxed{
\pi_{1,K,N}
\le
\exp\!\left[
-2q\log(4/\pi)+8k\log k+O_{h,\varpi}(k)
\right],
\quad N=q-1,q.
}
\tag{26}
$$

The period \(\varpi\) remains fixed, and the LRC finite guards are retained. The small-\(t\) profile and original monic normalization used here are those of the supplied CRV/LRC calculation.  

Now Cauchy–Schwarz in the actual kernel gives

$$
|U_N|
\le\sqrt{\frac{\theta_N\pi_{1,K,N}}{p_{1,N}}},
\qquad
|V_N|\le\sqrt{\frac{\theta_N}{p_{2,N}}}.
$$

Combining this with (1) proves

$$
\boxed{
|U_N|
\le
\sqrt{\theta_N}\,
\exp\!\left[4k\log k+O_{h,\varpi}(k)\right],
\quad N=q-1,q,
}
\tag{27}
$$

and

$$
\boxed{
\begin{aligned}
|V_{q-1}|
&\le
\frac{4q}{\pi k\sqrt{\delta^2+\gamma^2}}
\sqrt{\theta_{q-1}}\bigl(1+o_h(1)\bigr),\\
|V_q|&\le\sqrt{\theta_q}\bigl(1+o_h(1)\bigr).
\end{aligned}}
\tag{28}
$$

The unrestricted ellipse permits \(e^{q\log(4/\pi)}\)-scale response amplification. The **original kernel constraint** removes that leading \(q\)-exponent from \(U\). This conclusion uses the actual conductor, not a generic projection inequality.

The propagated phase-error bounds remain correlated. Put

$$
A_N=\sqrt{\frac{\theta_N\pi_{1,K,N}}{p_{1,N}}},
\qquad
B_N=\sqrt{\frac{\theta_N}{p_{2,N}}}.
$$

Then

$$
\begin{aligned}
|\Im P_K|&\le A_NB_N,\\
|\Im P_B|&\le A_N+B_N+A_NB_N,\\
|\Im P_\times|&\le A_N+B_N+2A_NB_N.
\end{aligned}
\tag{29}
$$

These can be intersected with JRE15. Their phase-error contributions are still

$$
2E_N(-1)^{N+1-q}\varepsilon_{N,\lambda}\Im P_X,
$$

and their signed sum is exactly zero.

The bounds in (27)–(29) are not yet small enough to replace the phase error at the \(k\delta E_N\) benchmark. They improve the **actual response bounds**, but do not assign \(\theta_N\), the phase of \(U_N\), or an individual projected sign.

## 3. The absolute baseline and slow-tail result now combine through \(q/\log q\)

For this finer absolute statement, use the **simple-packet** \(O_h(\log q)\) remainder stated in your concurrent report. Define

$$
r_h=\frac23(\gamma^2-\delta^2)M_{-1},
$$

$$
\mathfrak b_h=
C_\sigma-2C_\Gamma+\frac{\log2}{\pi}I_h-r_h,
$$

$$
\mathfrak a_h=
C_B-\frac{11}{4}C_\Gamma
+2\log(4\pi)-4
+\frac{\log2}{\pi}I_h-r_h.
\tag{30}
$$

Your new absolute-Gamma calculation gives

$$
\mathcal B_k[\sigma]
=C_Bq^2+C_\sigma q-r_hk(k+2)+O_h(\log q).
$$

The current SR28–30 result gives the arithmetic difference through

$$
\frac{C_\Gamma q}{2(\log q+c_\zeta)}
$$

with an \(o_h(q/\log q)\) error.

Since

$$
q=(k+1)^2,\qquad
k(k+2)=q-1,\qquad
k^2=q-2k-1,
$$

the combination is

$$
\boxed{
\mathcal B_k[m_k]
=
C_Bq^2+\mathfrak b_hq
+\frac{C_\Gamma q}{2(\log q+c_\zeta)}
+o_h(q/\log q).
}
\tag{31}
$$

For the complete action, the original source comparison bounds the arithmetic monic window against its Gamma window by \(O_h(k+\log q)\). Stirling’s formula gives

$$
\mathcal W_k^\sigma
=
4q\log q+(8\log2-4)q+O(\log q).
$$

The original penalty bound is \(O_h(1)\) on the simple lane. All are \(o_h(q/\log q)\). The exact CAI action identity therefore gives

$$
\boxed{
J_k^{\mathrm{action}}
=
C_Bq^2+4q\log q+\mathfrak a_hq
+\frac{C_\Gamma q}{2(\log q+c_\zeta)}
+o_h(q/\log q).
}
\tag{32}
$$

The monic window, penalties, and determinant are combined only through their original identity. 

A finite combined error is the SR30 error plus \(O_h(k+\log q)\):

$$
C_hq\left[
\frac{(1+\log\log q)^2}{(\log q)^2}
+q^{-1/200}(\log q)^2
\right]
+O_h(k+\log q).
\tag{33}
$$

Consequently, the complete benchmark difference now reads

$$
\boxed{
\begin{aligned}
J_k^{\mathrm{action}}-4q\log L_{h,k}
={}&C_Bq^2-2q\log q\\
&+\left[\mathfrak a_h-4\log(\delta/2)\right]q\\
&+\frac{C_\Gamma q}{2(\log q+c_\zeta)}
+o_h(q/\log q).
\end{aligned}}
\tag{34}
$$

Here \(L_{h,k}=\delta q(k+1)/2\). The positive \(C_Bq^2\) term remains.

This \(q/\log q\)-precision is asserted for the simple lane. The concurrent report’s higher-multiplicity absolute remainder is only \(o(q)\), so I have not promoted it to the finer scale by adding a more accurate arithmetic difference.

There is also a useful backward correction from the new repository: TS4–5 now proves \(d_0(h)>1\) on the stipulated actual simple-packet source. Thus the formal zero-threshold case discussed in my previous slow-tail response is **not an available actual simple-packet stratum**. Its algebraic threshold calculation remains correct, but the new source inequality excludes it.

## 4. The optimal positive-trace metrics have an exponential cost in the original canonical metric

The concurrent minimization theorem determines

$$
\min_{G\succ0}\operatorname{Tr}(H_G)_+
=L_{h,k}.
$$

The new response-energy calculation quantifies a cost not supplied by that minimum: how far an attaining metric must be from the original canonical one.

At \(N=q-1\), use the exact source-space action

$$
B_0=A-cI=i\mathsf J+\epsilon_0fe^*,
\qquad
e^*f=0,\quad \|e\|=\|f\|=1.
\tag{35}
$$

This is the original rank-one nonnormal term, not a replacement of \(A\) by its Hermitian compression. 

From the exact first-cutoff Gram,

$$
\epsilon_0^2=\frac{\nu_0-\omega_q}{\omega_{q-1}}
=\frac{1-d_0}{m_zp_{1,q-1}}.
$$

Hence

$$
\boxed{
\epsilon_0=
\frac{4q}{\pi\sqrt{p_{1,q-1}}}\bigl(1+o_h(1)\bigr).
}
\tag{36}
$$

Let \(\widehat G\) be any positive metric on the same complete packet and put

$$
\kappa=
\operatorname{cond}\left(
G_{q-1}^{-1/2}\widehat G\,G_{q-1}^{-1/2}
\right),
\qquad
\mathcal P(\widehat G)=\operatorname{Tr}(H_{\widehat G})_+.
$$

Let

$$
J_*=
C_{\mathrm{mult}}(h)
\left(2q-2+\lfloor k/3\rfloor\right)
$$

be the original multiplication bound for \(\|\mathsf J\|\).

Then every such metric satisfies

$$
\boxed{
\epsilon_0
\le
\mathcal P(\widehat G)\sqrt\kappa+2J_*\kappa.
}
\tag{37}
$$

To prove this, write \(S\) for the positive square root of the relative metric. In its orthonormal coordinates, the rank-one term becomes

$$
\epsilon_0(Sf)(S^{-*}e)^*.
$$

Its two vectors remain orthogonal because

$$
(S^{-*}e)^*(Sf)=e^*f=0.
$$

The norm of its Hermitian part is at least \(\epsilon_0/\sqrt\kappa\). The Hermitian part of \(iS\mathsf JS^{-1}\) has norm at most \(2J_*\sqrt\kappa\).

The full centred Hermitian weight has trace zero. Its operator norm is therefore at most its positive trace. The reverse triangle inequality proves (37).

For every minimizing metric,

$$
\boxed{
\kappa\ge
\left[
\frac{2\epsilon_0}
{L_{h,k}+\sqrt{L_{h,k}^2+8J_*\epsilon_0}}
\right]^2.
}
\tag{38}
$$

Since \(\epsilon_0\) is exponential while \(L_{h,k}\) and \(J_*\) are polynomial,

$$
\kappa
\ge
\frac{1-o_h(1)}
{\pi C_{\mathrm{mult}}(h)\sqrt{p_{1,q-1}}}.
$$

Consequently,

$$
\boxed{
\liminf_{k\to\infty}\frac1q\log\kappa
\ge\log(4/\pi)>0.
}
\tag{39}
$$

This applies to **every** minimizing metric, including the explicit full-CRT metric in your paste, and retains all nilpotents. It also applies to any metric family whose positive trace is only polynomial in \(q\).

Thus the positive-trace optimization is valid, but passing from the original canonical metric to an attaining metric necessarily has an exponential relative condition-number cost. This is a calculation in the original source metric, not a generic warning about changing metrics.

## 5. The coefficient-image result improves the observed marked-defect calculation

The same original conductor gives a sharper observation statement than the degree-dependent bound in my preceding marked continuation.

For a nonzero polynomial \(P\) of degree \(D\ge v\),

$$
\deg(\mathcal T_AP)=D-v,
$$

with leading coefficient

$$
\mu_v\binom Dv\,\operatorname{lc}(P).
$$

If \(D<q'+v\), this degree is below \(\deg\chi_{k-8}=q'\). Therefore the divisibility condition in (22) forces

$$
\boxed{
K\cap\mathcal P_D=K\cap\mathcal P_{v-1},
\qquad v-1\le D<q'+v.
}
\tag{40}
$$

In particular,

$$
\mathcal T_A(S^v)=\mu_v\ne0,
\qquad
\boxed{\Lambda_kS^v\ne0.}
\tag{41}
$$

Thus

$$
j_*:=\min\{j\ge0:\Lambda_kS^j\ne0\}
\le v\le80.
\tag{42}
$$

This replaces the earlier bound \(j_*\le8k-16\).

To propagate this into the marked family, retain

$$
A(t)=A+t\,e_0e_{q-1}^{\mathsf T},
\qquad
U'(t)=A(t)U(t)/u,\quad U(0)=I,
$$

and the specified analytic continuation

$$
\Lambda_h(t)=\Lambda_kU(t)^{-1}.
$$

Let

$$
Y(t)=e^{\lambda t/u}\Lambda_h(t)v_\lambda-\Lambda_kv_\lambda.
$$

The original marked identity gives

$$
Y'(t)
=-\frac{b_\lambda}{u}\,t\,
e^{\lambda t/u}\Lambda_h(t)\mathbf1.
$$

The first nonzero derivative is therefore

$$
\boxed{
Y^{(j_*+2)}(0)
=
b_\lambda(j_*+1)(-u)^{-(j_*+1)}
\Lambda_kS^{j_*}\ne0.
}
\tag{43}
$$

Its order is at most

$$
\boxed{v+2\le82,}
\tag{44}
$$

independently of tensor degree. The marked recurrence used here is the full differential-quotient recurrence, not arithmetic powers of the eigenline. 

There is an even more explicit receiver. Since \(\ker\Lambda_k\subset\ker C\), the original conductor factors uniquely as

$$
C=\overline C\,\Lambda_k.
$$

For \(r<v\),

$$
\overline C\,Y^{(r+2)}(0)=0,
$$

whereas

$$
\boxed{
\overline C\,Y^{(v+2)}(0)
=
b_\lambda(v+1)(-u)^{-(v+1)}
\mu_v\,\mathbf1_{q'}\ne0.
}
\tag{45}
$$

This coefficient contains only the original terminal coefficient, conductor moment, and marked parameter. It does not leave a period-matrix vector unnamed.

On the \(v=0\) locus, this proves \(\Lambda_k\mathbf1\ne0\) at **every admitted degree**, strengthening the earlier sufficient cofinal sequence \(k=20n+5\).

Finally, combine (40) with the concurrent result

$$
\operatorname{im}L_a=\mathcal P_{m_a-1}.
$$

For \(a\ge29\),

$$
\boxed{
K_a\cap\operatorname{im}L_a
=
K_a\cap\mathcal P_{v-1},
\qquad
\operatorname{rank}(\Lambda_aL_a)=m_a-t_{0,a}.
}
\tag{46}
$$

Thus the original coefficient image loses at most the explicitly retained low-jet intersection under observation.

The concurrent negative-trace polynomial \(P_a\), of degree \(8a\), satisfies

$$
v\le8a<q'_a+v
$$

on this domain. Equation (40) therefore proves

$$
\boxed{\Lambda_aP_a\ne0.}
\tag{47}
$$

Its leading conductor coefficient is explicitly

$$
\mu_v\binom{8a}{v}\frac{t_0^{8a}}{(8a)!}\ne0.
$$

So that negative reflected-trace class survives the **actual finite observation**. This does not identify its reflected trace with a projected arithmetic weight form or with a class in Deligne’s pure middle image.

## Resulting continuation state

The current response calculation now has evaluated source energies at **both original low cutoffs**, including an exponential rate for \(p_1\), an explicit coefficient for \(p_{2,q-1}\), and the limit \(p_{2,q}\to1\). The actual conductor further bounds \(U\) by \(e^{4k\log k+O(k)}\), rather than the \(e^{cq}\) amplification permitted by the unrestricted ellipse.

The simple-packet canonical scalar now combines through \(q/\log q\), using the absolute-Gamma remainder stated in your paste. The all-positive-metric optimization has a quantified exponential cost relative to the original canonical metric. The marked observation defect is detected by order at most \(82\), with the explicit conductor-visible coefficient (45).

The remaining projected-sign calculation still needs the actual period-dependent \(\theta_N\) and response position, including the products of \(U\) with the error in (21). The two high cutoffs and the independent proper-source return have not been assigned values by these low-cutoff results. No new computational verification or repository write is claimed in this turn.

[1]: https://dlmf.nist.gov/5.11 "https://dlmf.nist.gov/5.11"
