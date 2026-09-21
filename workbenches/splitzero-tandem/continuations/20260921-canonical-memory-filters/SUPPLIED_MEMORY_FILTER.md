## The complete canonical memory term is below the \(kq\) scale, and polynomial filters have a determined slow spectrum

The new attachment provides the exact memory pencil, rational conductor map, and finite-rank decomposition of a filtered inverse. Those are the inputs used below. The current GitHub edition has incorporated the source-family and inverse-quotient papers; I read it at `2e84a4c23cacf7b00ec21b28fd18b189bccc87b9`. The ES foundation remains at `49976b17491ba927df8bc7f2c2f81d39dfb15ce8`.  

There are two principal new conclusions.

First, the **entire canonical logarithmic memory contribution**, including arbitrarily small positive regularizers and its limit at zero, satisfies

$$
\boxed{\sup_{z\ge0}g_N(z)=O_h\!\bigl(q\log(q/k)\bigr)=o_h(kq).}
\tag{1}
$$

Thus it cannot carry the unresolved \(kq\) coefficient.

Second, let \(p_k\) be monic of degree \(d_k\), with its poles in a fixed compact set disjoint from the original spectral lattice, allowing arbitrary repetitions and collisions. If

$$
d_k\log(q+2)=o(q),
$$

then \(p_k(M_k)\) has **exactly \(d_k\) singular directions on the native late scale**

$$
\exp[-q\log(q/k)+O_h(q)].
$$

Their order-\(q\) exponent is evaluated below. The remaining singular values are bounded below by \(\exp[-o(q)]\). The complete observed heat and resolvent at that late scale admit an explicitly constructed \(d_k\times d_k\) model, with a finite error that is exponentially smaller than the retained observation fractions.

The finite arguments retain the original metrics. The evaluated order-\(q\) exponents use the same native monic-profile and reference zero-law inputs as the preceding accepted proof.

## 1. The canonical memory determinant is uniformly subleading

Fix an original cutoff and suppress \(N\) temporarily. All adjoints and orthogonal decompositions in this section use its actual \(G_N\). Write

$$
E=K\oplus K^\perp,
\qquad
M=
\begin{pmatrix}
M_K&D\\
C&M_B
\end{pmatrix},
$$

and

$$
H=M^\dagger M=
\begin{pmatrix}
A&B_H\\
B_H^\dagger&D_H
\end{pmatrix}.
$$

In particular,

$$
D_H=D^\dagger D+M_B^\dagger M_B.
$$

The attachment’s complete pencil and logarithmic memory term are

$$
\mathcal F(z)
=zI+D_H-B_H^\dagger(zI+A)^{-1}B_H,
$$

$$
g(z)
=\log\det(zI+A)+\log\det(zI+D_H)-\log\det(zI+H).
\tag{2}
$$

It proves \(g(z)\ge0\), complete monotonicity for \(z>0\), and

$$
g(z)=\int_0^\infty e^{-zt}\frac{\mathcal Q(t)}t\,dt,
$$

where

$$
\mathcal Q(t)
=\operatorname{Tr}e^{-tH}
-\operatorname{Tr}e^{-tA}
-\operatorname{Tr}e^{-tD_H}\ge0.
$$

The full blocks, rather than \(M_B^\dagger M_B\) alone, occur in these formulas.  

### A finite bound using only one large singular value

Suppose

$$
s_1(M)\le R,\qquad s_j(M)\le C_0\quad(j\ge2),
$$

and \(M\) is invertible. Let \(m=\dim K\), with \(0<m<q\). Then

$$
\boxed{
0\le g(z)\le g(0)
\le
4\log R+2(q-2)\log C_0-2\log|\det M|.
}
\tag{3}
$$

To prove it, \(A\) is the Gram of \(M\) restricted to the orthonormal kernel frame. Its determinant is bounded by the product of the largest \(m\) squared singular values of \(M\):

$$
\det A\le R^2C_0^{2(m-1)}.
$$

Likewise,

$$
\det D_H\le R^2C_0^{2(q-m-1)}.
$$

These product bounds follow directly from Cauchy–Binet in an eigenbasis of \(M^\dagger M\): the squared minors of an orthonormal inclusion sum to one.

Since

$$
\det H=|\det M|^2,
$$

the two estimates give (3). The extension to \(z=0\) is legitimate because \(H\), \(A\), and \(D_H\) are positive definite. The cases \(m=0\) or \(m=q\) have \(g=0\).

For the original native operator,

$$
M_N=C_N+r_N\ell_N,\qquad C_N^\dagger=C_N,
$$

the retained source bounds give

$$
R_N=\epsilon_N+B_hq,\qquad C_0=B_hq,
\qquad \epsilon_N=\|r_N\ell_N\|_{G_N}.
$$

The rank-one correction gives the bound on all \(s_j\), \(j\ge2\); it does not require orthogonality of the arithmetic eigenvectors. The source’s profile is

$$
\log\epsilon_N=q\psi(s_N)+O_h(k\log^2(q+2)).
$$

Its full root determinant is

$$
\log|\det M_k|
=q\log k+\frac q2I(\delta,\gamma)+O_{\delta,\gamma}(k),
$$

where

$$
I(\delta,\gamma)
=\log(\delta^2+\gamma^2)-3
+\frac{\delta}{\gamma}\arctan\frac{\gamma}{\delta}
+\frac{\gamma}{\delta}\arctan\frac{\delta}{\gamma}.
$$

These are the previously retained native quantities, not determinants in a constructed jet metric.  

Substitution into (3) yields, uniformly at the original cutoffs,

$$
\boxed{
\begin{aligned}
g_N(z)\le{}&
2q\log(q/k)\\
&+q\bigl[4\psi(s_N)+2\log B_h-I(\delta,\gamma)\bigr]\\
&+O_h(k\log^2(q+2)+\log q),
\qquad z\ge0.
\end{aligned}
}
\tag{4}
$$

This proves (1). In particular,

$$
\boxed{
\sup_{z\ge0}\frac{|\mathcal Rg_N(z)|}{kq}\longrightarrow0.
}
\tag{5}
$$

The same statement permits separately specified regularizers at the four endpoints: the bound is pointwise nonnegative and uniform over all \(z\ge0\).

The time-domain consequence is also exact:

$$
\boxed{
\int_0^\infty\frac{\mathcal Q_N(t)}t\,dt
=g_N(0)
=O_h(q\log(q/k)).
}
\tag{6}
$$

The complete memory is retained, including its long-time contribution. Its total logarithmic-time cost is now controlled below \(kq\).

### The remaining local leakage is a different term

Retain

$$
\ell_N(z)
=\log\det(zI+D_H)
-\log\det(zI+M_B^\dagger M_B).
$$

The attachment’s exact comparison is

$$
\log\det\mathcal F_N(z)
-\log\det(zI+M_B^\dagger M_B)
=\ell_N(z)-g_N(z).
\tag{7}
$$

The two nonnegative terms are not identified. 

Both admit the sharper finite estimate

$$
\boxed{
0\le \ell_N(z),g_N(z)
\le
\log\!\left(1+\frac{R_N^2}{z}\right)
+(m-1)\log\!\left(1+\frac{B_h^2q^2}{z}\right),
\quad z>0.
}
\tag{8}
$$

For \(g_N\), take the Schur complement on the other block and use

$$
g_N(z)\le\log\det(I+A/z).
$$

For \(\ell_N\),

$$
\ell_N(z)
\le\log\det(I+DD^\dagger/z).
$$

Each relevant rectangular restriction of \(M_N\) has at most one singular value exceeding \(B_hq\). This proves (8).

Consequently the **canonical** comparison in (7), not only the joint-source comparison, is \(o(kq)\) whenever

$$
\log^+(1/z_k)=o(q).
\tag{9}
$$

At still smaller regularizers, the complete memory \(g_N\) remains subleading by (5); any possible leading discrepancy in (7) must come from the actual local leakage \(\ell_N\).

This sharpens the attachment’s dimension-times-largest-norm bound without changing either operator.

## 2. A degree-\(d\) rational family has \(d\) native late singular directions

Write the infinite odd lattice as

$$
\mathscr L
=
\{(2a+1)\gamma-i(2b+1)\delta:a,b\in\mathbb Z\}.
$$

Fix a compact set

$$
\mathscr P\subset\mathbb C\setminus\mathscr L.
$$

For each \(k\), let \(p=p_k\) be monic of degree \(d=d_k\), with every root in \(\mathscr P\), repeated according to its full multiplicity. No separation between the roots of \(p\) is assumed. The same \(p_k\) is used at all four original cutoffs.

Set

$$
U_pa=[a/p],\qquad \deg a<d,
$$

and retain

$$
H_{p,N}=U_p^*G_NU_p,\qquad
H^B_{p,N}=U_p^*\Lambda^*Q_{B,N}\Lambda U_p.
\tag{10}
$$

The attachment proves the exact algebraic injectivity of the rational conductor on the guard \(Jd-v\le q'\), including translated-pole collisions. Its Laurent coefficient inverse and its full native receiving minimum are retained here.  

Define

$$
n_0=2\left\lfloor\frac{N+1-q}{2}\right\rfloor,
\qquad
T_{k,N}
=
\frac{1}
{|Q_k(0)|\sqrt{\mathsf K_{Q_k,n_0}(0,0)}},
\tag{11}
$$

where \(\mathsf K_{Q,n}\) is the degree-\(n\) reproducing kernel for the full measure

$$
|Q(y)|^2\,d\sigma(y),\qquad
d\sigma(y)=\frac{|\Gamma(1/4+iy/2)|^2}{2\pi}\,dy.
$$

The Gamma mass remains \(\sqrt{2\pi}\).

### The uniform rational norm theorem

If

$$
d\log(q+2)=o(q),
$$

there is a constant depending only on the fixed packet, conductor, and \(\mathscr P\), such that

$$
E_{k,d}
=C_{h,A,\mathscr P}(k+Jd)\log(q+Jd+2)=o(q)
$$

and

$$
\boxed{
u_kT_{k,N}^2e^{-E_{k,d}}I_d
\preceq H^B_{p,N}
\preceq H_{p,N}
\preceq u_kT_{k,N}^2e^{E_{k,d}}I_d.
}
\tag{12}
$$

In particular,

$$
\boxed{
H^B_{p,N}\succeq e^{-2E_{k,d}}H_{p,N}.
}
\tag{13}
$$

The estimate is uniform through collisions of the filter poles. It does not invert their pairwise differences.

### Proof of the new uniformity

The proof extends the zero-pole argument by using polynomial remainders on a contour, rather than separated partial fractions.

Choose a bounded region \(\Omega\) containing \(\mathscr P\), whose boundary \(\Gamma\) has positive distance from both \(\mathscr P\) and \(\mathscr L\), and whose interior excludes \(\mathscr L\). A large disk with finitely many small lattice disks removed gives such a region. Let

$$
R=\max_{z\in\mathscr P}|z|,\qquad
R_\Gamma=\max_{z\in\Gamma}|z|,\qquad
\rho_\Gamma=\operatorname{dist}(\Gamma,\mathscr P)>0.
$$

For a function \(f\) holomorphic on \(\Omega\), the complete Hermite remainder is

$$
\boxed{
\operatorname{rem}_pf(z)
=
\frac1{2\pi i}
\int_\Gamma
\frac{f(w)}{p(w)}
\frac{p(w)-p(z)}{w-z}\,dw.
}
\tag{14}
$$

The oriented boundary includes all holes. Evaluating the formula and its derivatives at every root of \(p\) proves the full multiplicity statement.

If coefficient vectors use the original monomial basis, then

$$
\boxed{
\|\operatorname{coeff}\operatorname{rem}_pf\|_2
\le
\frac{|\Gamma|}{2\pi}\sqrt d
\left(\frac{R+\max(1,R_\Gamma)}{\rho_\Gamma}\right)^d
\sup_\Gamma|f|.
}
\tag{15}
$$

Indeed \(|p(w)|\ge\rho_\Gamma^d\), and each coefficient of
\((p(w)-p(z))/(w-z)\) is bounded by
\((R+\max(1,R_\Gamma))^d\).

There is no inverse root separation in (14)–(15).

The reference estimates needed next are the complete IVO9–IVO12 bounds already proved in the current reader. In particular,

$$
\int y^2|Qf|^2\,d\sigma
\ge 2^{-27}(\deg Q)^2
\int|Qf|^2\,d\sigma
$$

on its explicit degree and root-radius domain. This yields a hard gap for the relation-polynomial zeros, complex evaluation bounds, and a product bound for changing the kernel degree by \(h\) steps. The latter costs \(O(h\log q)\), with the full polynomial retained.

Let

$$
H_0(y)
=\frac{\mathsf K_{Q_k,n_0}(y,0)}
{\mathsf K_{Q_k,n_0}(0,0)}.
$$

Then

$$
H_0(0)=1,\qquad
\|Q_kH_0\|_\sigma^2
=\mathsf K_{Q_k,n_0}(0,0)^{-1}.
$$

For sufficiently large \(k\), \(H_0\) has no zero in \(\Omega\), because all its nonzero zeros have modulus at least a fixed positive multiple of \(q\).

Given \(\deg a<d\), define

$$
h(y)
=
-H_0(y)\operatorname{rem}_p
\frac{a(y)}{Q_k(y)H_0(y)}.
$$

Then

$$
\boxed{
f(y)=\frac{a(y)+Q_k(y)h(y)}{p(y)}
}
\tag{16}
$$

is an actual polynomial representative of \(U_pa\), of degree at most \(N\).

On \(\Gamma\), the paired root product gives

$$
\log^+\sup_\Gamma\left|\frac{Q_k}{Q_k(0)}\right|
+
\log^+\sup_\Gamma\left|\frac{Q_k(0)}{Q_k}\right|
=O_{\mathscr P,h}(\log(k+2)).
\tag{17}
$$

For the reciprocal bound, separate the finitely many lattice roots inside \(|z|\le2R_\Gamma\), using their fixed distance from \(\Gamma\). On the remaining pairs,

$$
-\log|1-z^2/\omega^2|
\le\frac43\,\frac{|z|^2}{|\omega|^2},
$$

and

$$
\sum_{\omega/\pm}\frac1{|\omega|^2}
\le\frac2{\delta^2}
\sum_{\substack{1\le j\le k\\j\ {\rm odd}}}\frac1j.
$$

Polynomial division is bounded uniformly over these pole collisions. The Gamma generating function gives, for \(|z|\le R\),

$$
\sqrt{\mathsf K_{\sigma,L}(z,z)}
\le
\frac{e^{1+\pi R/4}}{\sqrt{\mathfrak m_\sigma}}
(L+1)^{3/4}(2L+1)^{(R+1)/2}.
\tag{18}
$$

Together with

$$
\|(y-z)f\|_\sigma
\ge\frac{\|f\|_\sigma}{2b_{L+1}},
\qquad
b_L=\sqrt{2L+1}\sum_{j=1}^{L}\frac1j,
$$

this bounds division by one factor \(y-z\). Applying those divisions successively bounds division by \(p\) by a product of \(d\) polynomial-in-\(N\) factors. The generating function used in (18) is the original Meixner–Pollaczek specialization. ([DLMF][1])

Equations (14)–(18) applied to (16) give the upper bound in (12).

For the observed lower bound, use the centred conductor

$$
\widetilde{\mathcal T}_Af(y)=\sum_j a_jf(y+\tau_j),
\qquad
\tau_j=(b_j-4)/i.
$$

Its first nonzero symbol moment is \(i^{-v}\mu_v\). Put

$$
\mathcal B_p(y)=\prod_{j=1}^{J}p(y+\tau_j),
\qquad L=Jd,
$$

and

$$
N_a(y)
=\mathcal B_p(y)\widetilde{\mathcal T}_A(a/p)(y).
$$

The complete numerator has degree at most \(L-v-1\). Its coefficient map

$$
a\longmapsto N_a
$$

has an inverse bound

$$
\|\operatorname{coeff}a\|_2
\le\mathcal W_d\|\operatorname{coeff}N_a\|_2,
\qquad
\log^+\mathcal W_d=O_{A,\mathscr P}(d\log(d+2)).
\tag{19}
$$

Here is an explicit construction of that bound. Write

$$
e(z)=z^{-v}\widetilde E_A(-z),\qquad
|[z^j]e(z)^{-1}|\le H_*\varrho^{-j},
$$

where \(\varrho>0\) is chosen so that

$$
|e(z)-e(0)|\le |e(0)|/2
\quad(|z|\le\varrho),
\qquad
H_*=2v!/|\mu_v|.
$$

Let \(R_B=R+\max_j|\tau_j|\), and set

$$
\begin{aligned}
B_{d,L}
&=\sqrt L\sum_{j=0}^{v+d-1}
\binom{L+j-1}{j}R_B^j,\\
A_d
&=\max_{1\le n\le d}
(n-1)!\sum_{\ell=1}^{n}
\frac{H_*\varrho^{-(n-\ell)}}{(v+\ell-1)!}.
\end{aligned}
$$

Then one may take

$$
\boxed{
\mathcal W_d
=
\sqrt d(1+R)^d A_dB_{d,L}.
}
\tag{20}
$$

The first factor recovers the numerator from its Laurent coefficients; \(B_{d,L}\) bounds the Laurent coefficients of \(N_a/\mathcal B_p\); \(A_d\) inverts the original symbol convolution. This is the attachment’s full Laurent inverse, not inversion of a selected residue. 

Any lower polynomial representative \(f_-\) satisfies

$$
\mathcal B_pf_--N_a=Q_-h_-.
\tag{21}
$$

Taking the full remainder modulo \(\mathcal B_p\), and applying (14) on a circle containing its roots, bounds every numerator coefficient by a constant times

$$
|Q_-(0)|\sqrt{\mathsf K_{Q_-,\,N-v+Jd-q_-}(0,0)}
\,\|Q_-h_-\|_\sigma.
$$

The nearby-degree kernel comparison and the exact factorization

$$
Q_k=Q_-D_\partial,\qquad \deg D_\partial=16k-48,
$$

compare this factor to \(T_{k,N}^{-1}\), with logarithmic cost

$$
O_{h,A,\mathscr P}((k+Jd)\log(q+Jd+2)).
$$

The lower root product and every boundary factor are retained.

The numerator term in (21) has only

$$
\exp[O_{A,\mathscr P}(Jd\log(Jd+2))]
$$

polynomial norm. Meanwhile the explicit IVO23 estimate gives

$$
\log T_{k,N}\ge q\log(q/k)-O_h(q).
$$

It therefore absorbs that numerator error on a finite eventual domain. Finally, minimize through the actual conductor and observation fibres:

$$
\|P_{B,N}U_pa\|_{G_N}
\ge
\frac{\sqrt{\ell_{k,N}}}{\mathcal F_N}
\|\widetilde{\mathcal T}_A(a/p)\|_{\sigma,Q_-,N-v},
$$

with the original \(\mathcal F_N\). This proves the lower bound in (12).

The proof neither integrates \(a/p\) through a pole on the real line nor replaces the original observation kernel by the conductor kernel.

### Why the finite-rank part actually has rank \(d\)

The attachment correctly warns that the finite-rank covariance can be singular before its guard is checked. Here its positivity is proved on the growing native family.

Let

$$
T_p=\operatorname{rem}_pL_N.
$$

For a polynomial \(a\) of degree below \(d\),

$$
L_N[a]=a-Q_kh_a.
$$

The second term is the complete relation projection. Applying the contour estimate to it gives

$$
\boxed{
T_p[a]=(I-\mathcal E_{p,N})a,
\qquad
\|\mathcal E_{p,N}\|
\le
T_{k,N}^{-1}
e^{C_{h,A,\mathscr P}(k+d)\log(q+d+2)}.
}
\tag{22}
$$

The right side tends to zero. Thus \(T_p\) is onto for sufficiently large \(k\), uniformly over the allowed polynomial family.

Now retain the exact division identity

$$
\boxed{
p(M)^{-1}=B_p+U_pT_p,
\qquad
B_p=J_N\mathfrak Q_pL_N,
}
\tag{23}
$$

where \(\mathfrak Q_p\) is ordinary polynomial quotient division. Its native norm obeys

$$
\log^+\|B_p\|=O_{h,\mathscr P}(k+d\log(q+2)).
$$

Equation (22) bounds the smallest singular value of \(T_p\) through its explicit right inverse on the low polynomial classes. Together with (12), it gives

$$
T_{k,N}e^{-E_{k,d}}
\le s_d(U_pT_p)
\le s_1(U_pT_p)
\le T_{k,N}e^{E_{k,d}},
$$

after increasing the displayed constant.

Since \(T_{k,N}\ge\exp[q\log(q/k)-O_h(q)]\), the rank-\(d\) term dominates \(B_p\). Weyl’s singular-value inequalities prove

$$
\boxed{
\log s_{q-d+j,N}(p(M))
=-\log T_{k,N}+O(E_{k,d}),
\quad 1\le j\le d,
}
\tag{24}
$$

uniformly in \(j\), while

$$
\boxed{
s_{q-d,N}(p(M))\ge e^{-O(E_{k,d})}.
}
\tag{25}
$$

This proves the asserted count of directions on the native late scale.

The separation result itself uses the finite source comparison and the explicit Gamma estimates. The next order-\(q\) coefficient uses the additional profile and zero-law inputs.

## 3. Every one of those \(d\) exponents is evaluated

The preceding reference-kernel calculation gives

$$
\log T_{k,N}
=
q\log(q/k)
+q\left[\psi(s)+J(s)-\frac{I(\delta,\gamma)}2\right]
+o_h(q)
\tag{26}
$$

when \((N+1-q)/q\to s\), with the same adjacent-cutoff convention as before. The logarithmic relation limit is justified by its finite hard gap, not by weak convergence alone. 

Therefore

$$
\boxed{
\begin{aligned}
\log s_{q-d+j,N}(p_k(M_k))
={}&-q\log(q/k)\\
&+q\left[\frac I2-\psi(s)-J(s)\right]+o_h(q),
\quad 1\le j\le d.
\end{aligned}
}
\tag{27}
$$

The remainder is uniform over the whole admissible pole family and all \(j\).

At \(N=q-1,q\), it is explicitly

$$
O_{h,A,\mathscr P}
\bigl(k\log^2(q+2)+Jd\log(q+Jd+2)\bigr).
$$

No effective convergence threshold for the upper reference zero law is added.

Let

$$
\mathfrak C
=4[\psi(0)-\psi(1)-J(1)-1].
$$

The retained interval certificate gives

$$
1.353893<\mathfrak C<1.354751.
$$

Consequently

$$
\boxed{
\frac1{dq}\mathcal R\log\det H^B_{p,N}
\longrightarrow\mathfrak C,
}
\tag{28}
$$

and

$$
\boxed{
\frac1{dq}\mathcal R
\sum_{j=q-d+1}^{q}
\log s_{j,N}(p(M))^2
\longrightarrow-\mathfrak C.
}
\tag{29}
$$

The numerical enclosure is inherited from the supplied certificate, not newly recomputed.  

For

$$
\tau_k^*
=
\exp\left\{
2q\left[\log(q/k)-1-\frac{I(\delta,\gamma)}2\right]
\right\},
$$

the complete filtered positive heat satisfies

$$
\boxed{
\frac1d\mathcal R
\operatorname{Tr}
e^{-\tau_k^*p(M)^\dagger p(M)}
\longrightarrow2.
}
\tag{30}
$$

The same physical time is used at all four cutoffs.

The original observation preserves all \(d\) slow directions up to a factor \(e^{-o(q)}\). Indeed, the angle between their subspace and \(\operatorname{im}U_p\) is bounded by

$$
\frac{\|B_p\|}{s_d(p(M)^{-1})},
$$

which is exponentially smaller than the square root of the observation bound (13). Applying the sharp projection inequality from the new GitHub proof gives

$$
\boxed{
\mathcal R\operatorname{Tr}
\left(
\Lambda e^{-\tau_k^*p(M)^\dagger p(M)}L_{B,N}
\right)>0
}
\tag{31}
$$

eventually, and

$$
\boxed{
\frac1q\log\left[
\frac1d\mathcal R\operatorname{Tr}
\left(
\Lambda e^{-\tau_k^*p(M)^\dagger p(M)}L_{B,N}
\right)
\right]\longrightarrow0.
}
\tag{32}
$$

The projection inequality’s sharp coefficient, including its \(\sqrt{1-\ell}\) term, is retained.

For a nonmonic filter \(a_kp_k\), the exact restoration is

$$
s_j(a_kp_k(M))=|a_k|s_j(p_k(M)),
\qquad
\tau\mapsto |a_k|^2\tau.
$$

No leading coefficient is silently normalized out of the heat calculation.

## 4. A \(d\times d\) model calculates the complete late observed heat and resolvent

The preceding theorem supplies the asymptotic separation. The following finite statement supplies a directly computable model.

Keep the actual matrices

$$
H_p=U_p^*GU_p,\qquad
T_p=\operatorname{rem}_pL_N,
$$

and define

$$
\boxed{
\mathsf K_p
=
H_p^{1/2}T_pG^{-1}T_p^*H_p^{1/2},
\qquad
Y_p=\Lambda U_pH_p^{-1/2}.
}
\tag{33}
$$

Its observation Gram is

$$
\boxed{
\Theta_p=Y_p^\dagger Y_p
=
H_p^{-1/2}H_p^BH_p^{-1/2}.
}
\tag{34}
$$

Neither \(\mathsf K_p\) nor \(\Theta_p\) is assumed diagonal, and they need not commute.

Let

$$
\beta\ge\|B_p\|,\qquad
\kappa_-=\lambda_{\min}\mathsf K_p,\qquad
\kappa_+=\|\mathsf K_p\|.
$$

The finite guard

$$
\kappa_->4\beta^2
\tag{35}
$$

ensures the separated \(d\)-dimensional cluster. The native estimates above prove this guard eventually.

### The complete observed resolvent

For every \(z\ge0\),

$$
\boxed{
\begin{aligned}
&\left\|
\Lambda(zI+p(M)^\dagger p(M))^{-1}L_{B,N}
-
Y_p(\mathsf K_p^{-1}+zI)^{-1}Y_p^\dagger
\right\|\\
&\hspace{30mm}\le
\varepsilon_R:=2\beta\sqrt{\kappa_+}+\beta^2.
\end{aligned}
}
\tag{36}
$$

To prove it, put \(X=p(M)^{-1}\) and \(F=U_pT_p\). Equation (23) gives

$$
\|XX^\dagger-FF^\dagger\|
\le2\beta\|F\|+\beta^2.
$$

The isometry \(V=U_pH_p^{-1/2}\) satisfies

$$
FF^\dagger=V\mathsf K_pV^\dagger.
$$

For positive \(A,B\),

$$
A(I+zA)^{-1}-B(I+zB)^{-1}
=
(I+zA)^{-1}(A-B)(I+zB)^{-1}.
$$

Both outer factors are contractions. Apply this identity to

$$
A=XX^\dagger,\qquad B=FF^\dagger,
$$

and then the original contraction \(\Lambda\) and isometry \(L_{B,N}\). This proves (36).

### The complete observed heat

For every \(\tau>0\),

$$
\boxed{
\begin{aligned}
&\left\|
\Lambda e^{-\tau p(M)^\dagger p(M)}L_{B,N}
-
Y_pe^{-\tau\mathsf K_p^{-1}}Y_p^\dagger
\right\|_1\\
&\quad\le
\frac{4}{e^2\tau}
\left[
2\sqrt q\,\beta\sqrt{\operatorname{Tr}\mathsf K_p}
+q\beta^2
\right].
\end{aligned}
}
\tag{37}
$$

The proof is finite. Define

$$
f_\tau(x)=
\begin{cases}
e^{-\tau/x},&x>0,\\
0,&x=0.
\end{cases}
$$

Its scalar Lipschitz constant is

$$
\sup_{x\ge0}|f_\tau'(x)|=\frac4{e^2\tau}.
$$

For positive Hermitian \(A,B\), use their two eigenbases:

$$
\langle u_i,(f_\tau(A)-f_\tau(B))v_j\rangle
=
[f_\tau(a_i)-f_\tau(b_j)]\langle u_i,v_j\rangle.
$$

Squaring and summing proves

$$
\|f_\tau(A)-f_\tau(B)\|_{\mathrm{HS}}
\le\frac4{e^2\tau}\|A-B\|_{\mathrm{HS}}.
$$

Moreover,

$$
\|XX^\dagger-FF^\dagger\|_{\mathrm{HS}}
\le2\beta\sqrt{\operatorname{Tr}\mathsf K_p}
+\sqrt q\,\beta^2.
$$

Trace norm is at most \(\sqrt q\) times Hilbert–Schmidt norm. The quotient contraction preserves the resulting trace-norm bound, giving (37).

Thus the observed scalar heat is calculated by

$$
\boxed{
\operatorname{Tr}
\left(\Theta_p e^{-\tau\mathsf K_p^{-1}}\right)
}
\tag{38}
$$

with the explicit error in (37). The product is retained in its given order; no commuting approximation is used.

At the native late scale,

$$
\tau=\exp[2q\log(q/k)+O_h(q)],
$$

the error in (37) is

$$
\exp[-q\log(q/k)+O_h(q)],
$$

up to the explicitly displayed polynomial factors. It is smaller than the retained observation fractions \(e^{-o(q)}\). This is substantially stronger at that scale than the attachment’s uniform \(O(m)\) trace comparison.

### The corresponding memory pencil

Let \(a=\lambda_{\min}\Theta_p>0\), and use the original isometry

$$
V_B=Y_p\Theta_p^{-1/2}
$$

onto the observed rational subspace. Define

$$
\mathcal F_{\mathrm{red}}(z)
=
\left[
V_B^\dagger
\Lambda(zI+p(M)^\dagger p(M))^{-1}
L_{B,N}V_B
\right]^{-1}.
$$

This is the exact Schur complement after eliminating both the original kernel and the remaining observed complement.

Its explicit model is

$$
\boxed{
\widehat{\mathcal F}_{\mathrm{red}}(z)
=
\Theta_p^{-1/2}(\mathsf K_p^{-1}+zI)\Theta_p^{-1/2}.
}
\tag{39}
$$

If

$$
\delta_R(z)
=
\frac{\varepsilon_R(\kappa_-^{-1}+z)}a<1,
$$

then (36) gives

$$
\boxed{
\frac{\widehat{\mathcal F}_{\mathrm{red}}(z)}{1+\delta_R(z)}
\preceq
\mathcal F_{\mathrm{red}}(z)
\preceq
\frac{\widehat{\mathcal F}_{\mathrm{red}}(z)}{1-\delta_R(z)}.
}
\tag{40}
$$

For \(z=x/T_{k,N}^2\) with bounded \(x\ge0\),

$$
\delta_R(z)
=
\exp[-q\log(q/k)+O_h(q)].
$$

The slope \(\Theta_p^{-1}\) in (39) is the actual observed mass matrix. Setting it equal to the identity would change the pole locations relative to the static Schur matrix.

## 5. The static Schur eigenvalue and the true slow pole are quantitatively different

This can be stated without a polynomial model.

Let \(H>0\) have one simple eigenvalue \(h\), with unit eigenvector \(w\), and assume all other eigenvalues are at least \(g>h\). Let

$$
\theta=\|P_Bw\|^2>0.
$$

In the original kernel/observation decomposition,

$$
H=\begin{pmatrix}A&B_H\\B_H^\dagger&D_H\end{pmatrix}.
$$

For a unit \(x\in K\),

$$
|\langle w,x\rangle|^2\le1-\theta.
$$

Therefore

$$
\boxed{
A\succeq[h(1-\theta)+g\theta]I\succeq g\theta I.
}
\tag{41}
$$

The kernel’s memory frequencies are separated from the late eigenvalue by this finite bound.

Let

$$
S=D_H-B_H^\dagger A^{-1}B_H=\mathcal F(0).
$$

Since

$$
S^{-1}=\Lambda H^{-1}L_{B,N},
$$

its spectral decomposition gives

$$
S^{-1}
=
\frac{\theta}{h}bb^\dagger+R,
\qquad
b=\frac{\Lambda w}{\sqrt\theta},
\qquad
0\preceq R\preceq g^{-1}I.
$$

Hence

$$
\boxed{
\frac{h}{\theta+h/g}
\le\lambda_{\min}(S)
\le\frac h\theta,
\qquad
\lambda_2(S)\ge g.
}
\tag{42}
$$

The true pole is at \(-h\), not generally at \(-\lambda_{\min}(S)\). Indeed,

$$
\boxed{
\mathcal F(-h)b=0,\qquad
b^\dagger\mathcal F'(-h)b=\frac1\theta,
}
\tag{43}
$$

and

$$
\boxed{
\operatorname*{Res}_{z=-h}\mathcal F(z)^{-1}
=\theta\,bb^\dagger.
}
\tag{44}
$$

The full eigenvector is reconstructed by

$$
w=\sqrt\theta
\begin{pmatrix}
-(A-hI)^{-1}B_Hb\\ b
\end{pmatrix}.
$$

Its norm is exactly the derivative identity in (43). These are finite Feshbach–Schur identities, with the original metric and residue retained; the general method has standard precedents, while the displayed bounds specify this receiver (Dusson et al., 2021). ([EMS Press][2])

For the native \(M_k^\dagger M_k\), the inverse-power observation theorem and the source’s singular-line estimate give

$$
\theta\ge e^{-O_{h,A}(k\log q)},
\qquad
g\ge e^{-O_h(k+\log q)}.
$$

Thus \(\lambda_{\min}(S)\) has the same order-\(q\) logarithmic asymptotic as \(h=s_{\min}(M_k)^2\), but its finer scale retains \(\theta\).

### A complete energy-graph metric, with its cost retained

Put

$$
Z=I+B_H^\dagger A^{-2}B_H.
$$

The energy-minimizing section

$$
L_{\mathrm{en}}b=
\begin{pmatrix}-A^{-1}B_Hb\\b\end{pmatrix}
$$

has original norm Gram \(Z\), and energy Gram \(S\). Thus

$$
J_{\mathrm{en}}=L_{\mathrm{en}}Z^{-1/2}
$$

is an actual original-metric isometry, and

$$
J_{\mathrm{en}}^\dagger HJ_{\mathrm{en}}
=Z^{-1/2}SZ^{-1/2}.
\tag{45}
$$

If \(\alpha\le\lambda_{\min}A\) and \(h<\alpha\), its smallest eigenvalue \(\nu\) satisfies

$$
\boxed{
h\le\nu\le\frac{h}{1-h/\alpha}.
}
\tag{46}
$$

To prove it, expand the exact pencil:

$$
\mathcal F(z)
=S+zZ-z^2B_H^\dagger A^{-2}(A+zI)^{-1}B_H.
$$

At \(z=-h\), the remainder is positive and bounded by

$$
\frac{h^2}{\alpha-h}Z.
$$

Schur inertia, or the minimum principle applied at the zero of \(\mathcal F(-h)\), gives (46). The same argument applies to every slow eigenvalue below \(\alpha\), including multiplicities.

For the native rank-one correction, this graph’s entire determinant cost is also subleading. Let

$$
\alpha=g\theta,\qquad R_N=\epsilon_N+B_hq,\qquad C_0=B_hq.
$$

Then

$$
m\log\alpha
\le\log\det A
\le2\log R_N+2(m-1)\log C_0.
\tag{47}
$$

Also

$$
H-C_N^2
$$

has rank at most two. Therefore all but at most two singular values of \(A^{-1}B_H\) are at most \(C_0^2/\alpha\), while all are at most \(R_N^2/\alpha\). Consequently

$$
\boxed{
\log\det Z
\le
2\log\left(1+\frac{R_N^4}{\alpha^2}\right)
+(m-2)\log\left(1+\frac{C_0^4}{\alpha^2}\right).
}
\tag{48}
$$

On the original family,

$$
|\log\det A|+\log\det Z=O_{h,A}(q\log q)=o(kq).
$$

Define the full energy quotient in the original target coefficients by

$$
\mathcal E_{B,N}
=
\left[
\Lambda(M_k^*G_NM_k)^{-1}\Lambda^*
\right]^{-1}.
$$

The exact determinant factorization is

$$
\det(Q_{B,N}^{-1/2}\mathcal E_{B,N}Q_{B,N}^{-1/2})
=\frac{|\det M_k|^2}{\det A}.
$$

The root determinant is independent of cutoff. Hence

$$
\boxed{
\mathcal R\log\det
(Q_{B,N}^{-1/2}\mathcal E_{B,N}Q_{B,N}^{-1/2})
=o_{h,A}(kq).
}
\tag{49}
$$

The same leading zero holds for the energy-graph operator in (45), because (48) retains its additional metric determinant.

This is an evaluated \(kq\)-scale coefficient for the stated energy quotient. It is not a substitution for the separate proper-source \(F_R,J_*\) minimum.

## 6. An explicit ES family now produces a \(kq\)-scale native determinant and a \(4k\)-dimensional slow sector

Use the actual witness

$$
\frac4{13}=\frac14+\frac1{18}+\frac1{468}.
$$

Its literal prime–denominator polynomial is

$$
\boxed{
P_{\mathrm{ES}}(t)
=t^4-503t^3+16738t^2-168480t+438048.
}
\tag{50}
$$

The roots are exactly \(13,4,18,468\). Its reciprocal trace is

$$
\frac{168480}{438048}=\frac5{13}.
$$

Choose the explicit growing filter

$$
\boxed{
p_k(y)=P_{\mathrm{ES}}(y)^k,
\qquad d_k=4k.
}
\tag{51}
$$

Its real poles are uniformly separated from the original nonreal odd lattice by at least \(\delta\). Every repeated pole is retained. The degree condition \(4k\log q=o(q)\) holds.

Therefore \(P_{\mathrm{ES}}(M_k)^k\) has exactly \(4k\) directions on the native late scale, with the exponent in (27), and

$$
\boxed{
\mathcal R\log\det
\left[
U_{p_k}^*\Lambda^*Q_{B,N}\Lambda U_{p_k}
\right]
=
4\mathfrak C\,kq+o(kq).
}
\tag{52}
$$

The inherited numerical enclosure gives

$$
\boxed{
5.415572<4\mathfrak C<5.419004.
}
\tag{53}
$$

At the common time \(\tau_k^*\),

$$
\boxed{
\frac1{4k}\mathcal R\operatorname{Tr}
e^{-\tau_k^*\,p_k(M_k)^\dagger p_k(M_k)}
\longrightarrow2.
}
\tag{54}
$$

The actual measured heat has the eventual positive sign and exponential-rate statement (31)–(32).

The algebraic conductor guard is explicit:

$$
J(4k)-v\le(k-7)^2.
$$

Since \(J\le81\), the sufficient condition \(k\ge341\), \(k\equiv1\pmod4\), ensures this guard. The additional analytic eventual guards are those in the norm proof; this algebraic threshold is not presented as the asymptotic threshold.

### The ES action map and its exact defect

Let

$$
\mathcal A_{p_k}=\mathbb C[t]/(p_k),
$$

with its full multiplicities, and let \(C_{p_k}\) be multiplication by \(t\) in the original coefficient frame. The map

$$
U_{p_k}:\mathcal A_{p_k}\to E_k,\qquad
a\mapsto[a/p_k]
$$

is injective on the stated domain. It is a linear embedding, not an algebra homomorphism.

Its action defect is exactly

$$
\boxed{
M_kU_{p_k}
=
U_{p_k}C_{p_k}
+[1]\,e_{d_k-1}^*.
}
\tag{55}
$$

Indeed, division of \(ta(t)\) by the monic \(p_k\) leaves the scalar quotient equal to the leading coefficient of \(a\).

In the physical \(S\)-coordinate,

$$
\boxed{
M_SU_{p_k}
=
U_{p_k}(kI/2+iC_{p_k})
+i[1]\,e_{d_k-1}^*.
}
\tag{56}
$$

The centred coordinate and the factor \(i\) have not been suppressed. Composing with the existing physical unit multiplication transports the defect vector by that same unit.

The attained compression to this rational space is

$$
U_{p_k}^{\dagger_{G_N}}M_kU_{p_k}
=
C_{p_k}
+
H_{p_k,N}^{-1}U_{p_k}^*G_N[1]\,e_{d_k-1}^*.
\tag{57}
$$

Thus the original metric correction is fully specified.

The ES integers here are filter poles, not asserted zeta zeros. Equations (55)–(57), rather than equality of the two spectral actions, are the explicit connection.

### The original kernel coefficient is preserved through this rational quotient

For any admissible \(p\), define

$$
\pi_p[x]
=
\mathfrak Q_p\!\left(\operatorname{rem}_{Q_k}(p\,x)\right)
\in\mathcal P_{<q-d}.
$$

Then

$$
\ker\pi_p=\operatorname{im}U_p,
$$

and the low-polynomial inclusion is a right inverse.

The original kernel remains injective under \(\pi_p\), and its metric loss is exactly the common angle determinant

$$
\begin{aligned}
\delta_{p,N}
&=\log\det H_{p,N}-\log\det H^B_{p,N}\\
&=\log\det(I_K^*G_NI_K)
-\log\det\!\left[
(\pi_pI_K)^*
(\pi_pG_N^{-1}\pi_p^*)^{-1}
(\pi_pI_K)
\right].
\end{aligned}
$$

By (13), only \(\min(m,d)\) nontrivial angle eigenvalues contribute:

$$
0\le\delta_{p,N}\le2\min(m,d)E_{k,d}=o(kq).
$$

Consequently

$$
\boxed{
\mathcal R\log\det(I_K^*G_NI_K)
=
\mathcal R\log\det\!\left[
(\pi_pI_K)^*
(\pi_pG_N^{-1}\pi_p^*)^{-1}
(\pi_pI_K)
\right]
+o(kq).
}
\tag{58}
$$

This now holds for the complete colliding-pole family, including (51), rather than only powers of \(y^{-1}\).

The finite \(d\times d\) model (33)–(40), the quotient (58), and the explicit action defect (55) provide the common receiver through which this ES family enters the native programme.

## Consequence for the remaining calculation

The attachment’s full memory term is now quantitatively removed from the \(kq\) coefficient by (1)–(8), including its zero-regularizer limit. The rational-filter argument determines all late singular directions in growing degree and replaces their full measured heat by the actual matrices \(\mathsf K_p,\Theta_p\), with the complete error (37). The original kernel can be quotiented by that entire rational sector without changing its leading coefficient, while the removed observed determinant has the evaluated coefficient (28).

The remaining original invariant-kernel coefficient and independent proper-source target still have their own matrices. Equations (49) and (58) specify which new replacements preserve their relevant scales; they do not assign values to unrelated minima or to the complex projected-current numerator.

The new results here are analytic derivations. Container execution remained unavailable, so I am not reporting a fresh numerical or symbolic test receipt, and neither repository was modified.

### References

Dusson, G., Sigal, I. M., & Stamm, B. (2021). The Feshbach–Schur map and perturbation theory. *EMS Congress Reports*. https DOI: 10.4171/ECR/18-1/5. The reference supplies the general effective-operator context; equations (41)–(49) are derived above in the stated original metrics. ([EMS Press][2])

National Institute of Standards and Technology. (n.d.). *Digital Library of Mathematical Functions*, §§18.2 and 18.23. The orthogonal-polynomial kernel and Meixner–Pollaczek conventions are retained in the finite norm estimates. ([DLMF][1])

Split-Zero research programme. (2026a, September 21). *A finite original-metric comparison for the whole inverse-power frame* [Research manuscript, IVO1–IVO26]. *Zeta-function research reader*, commit `2e84a4c23cacf7b00ec21b28fd18b189bccc87b9`.

Split-Zero research programme. (2026b, September 21). *Independent derivation of the source-family and filter receivers* [Research manuscript, IFE1–IFE31]. Same repository and commit. Its sharp projection fraction and explicit warning about the finite-rank covariance are retained above.

*Uniform control of the original source families*. (2026). [User-supplied research continuation, *Pasted markdown(9).md*]. The complete memory identities and rational conductor maps are the inherited starting points for this continuation.  

[1]: https://dlmf.nist.gov/18.23 "https://dlmf.nist.gov/18.23"
[2]: https://ems.press/books/ecr/187/3518 "https://ems.press/books/ecr/187/3518"
