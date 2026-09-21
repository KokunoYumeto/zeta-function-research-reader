# Uniform control of the original source families

The continuation now gives **uniform control of the complete finite metric family**, not just its determinant. It covers all fixed restrictions and attained quotients, all mixed derivatives in the source weights, the full observed heat operator with its memory term, and rational conductor observations with repeated or colliding poles.

One consequence directly concerns the original simple-quartet observation. Retain its original kernel \(K_k=\ker\Lambda_k\), original metric \(G_N\), original minimum section \(L_N\), and

$$
M=\frac{M_S-kI/2}{i},
\qquad
M_{B,N}=\Lambda_kML_N.
$$

Then, at every original cutoff and every heat time,

$$
\boxed{
\sup_{\tau\ge0}
\left|
\operatorname{Tr}\!\left(\Lambda_k e^{-\tau M^{\dagger_{G_N}}M}L_N\right)
-\operatorname{Tr}e^{-\tau M_{B,N}^{\dagger_{Q_N}}M_{B,N}}
\right|
\le 8k-16.
}
\tag{1}
$$

Consequently,

$$
\boxed{
\sup_{\tau\ge0}
\frac1{(k+1)^2}
\left|
\operatorname{Tr}\!\left(\Lambda_k e^{-\tau M^{\dagger_{G_N}}M}L_N\right)
-\operatorname{Tr}e^{-\tau M_{B,N}^{\dagger_{Q_N}}M_{B,N}}
\right|
\longrightarrow0.
}
\tag{2}
$$

The complete memory and leakage terms are retained in the proof. No lower bound for a spectral gap, no estimate for the largest native singular value, and no assumption that \(K_k\) is invariant under \(M\) enters (1).

A second consequence is an exact complexity restriction on the original observation kernel. Let the actual conductor have \(J\) labelled shifts, lower-packet degree \(q'\), and first nonzero symbol moment \(\mu_v\). For every nonzero \(x\in K_k\), define its proper rational complexity by

$$
d_{\mathrm{rat}}(x)
=
\min\left\{
\deg D:
D\text{ monic},\ (D,\chi_k)=1,\ 
x=[p/D],\ \deg p<\deg D
\right\}.
$$

Then

$$
\boxed{
d_{\mathrm{rat}}(x)
\ge
\left\lfloor\frac{q'+v}{J}\right\rfloor+1.
}
\tag{3}
$$

This holds for arbitrary poles and all their multiplicities—not only the inverse powers at zero considered in the preceding calculation.

The repository inputs used here are the complete inverse-power conductor and observed-heat/memory proofs already retrieved at **`fe22dc1dd51c633e82f93b731cbb6ec96b11ed64`**. I have not verified a later revision in this continuation. The new work below extends those fixed sources; it does not claim that subsequent GitHub changes have been incorporated.

---

## 1. A common complex neighbourhood for every fixed subquotient

Start with the original finite arithmetic value space \(E\), a positive metric \(G_\circ\), and the actual positive covariance contributions of complete normal-source groups:

$$
\Omega_1,\ldots,\Omega_p\succeq0.
$$

Their construction retains the original cross Gram and positive-range inverse. In particular, the original single addition remains

$$
\Omega=F_ZH_Z^+F_Z^*,
$$

with

$$
H_Z=\Gamma-C_X^*H_X^{-1}C_X,
\qquad
F_Z=I-J_NH_X^{-1}C_X.
$$

The supplied direction-preserving inequality

$$
F_Z^*G_{k,1}F_Z\preceq \Lambda_{h,n}^{\,k}H_Z
$$

is retained; it is not replaced by unrelated bounds on \(F_Z\) and \(H_Z^+\). 

Use logarithmic source weights:

$$
\boxed{
C(\mathbf x)=G_\circ^{-1}+\sum_{i=1}^p e^{x_i}\Omega_i,
\qquad
G(\mathbf x)=C(\mathbf x)^{-1},
\qquad
\mathbf x\in\mathbb R^p.
}
\tag{4}
$$

The weights describe the stated source penalties. The original physical joint source is the prescribed point of this family, not every point with a newly declared unchanged norm.

Fix any original flag

$$
E_0\subset E_1\subset E.
$$

Let \(Q_F(\mathbf x)\) be the full minimum metric on the specified coefficient space for \(E_1/E_0\), and let

$$
r=\dim(E_1/E_0).
$$

Put

$$
R_0=\log(5/4),\qquad L_0=\log(3/2).
$$

For every real base point \(\mathbf x_*\), the exact rational formula for \(Q_F\) has a holomorphic continuation to

$$
|z_i|\le R_0
$$

around \(\mathbf x_*\), and

$$
\boxed{
\left\|
Q_F(\mathbf x_*)^{-1/2}
Q_F(\mathbf x_*+\mathbf z)
Q_F(\mathbf x_*)^{-1/2}
-I
\right\|
\le\frac12.
}
\tag{5}
$$

Its inverse satisfies

$$
\boxed{
\left\|
Q_F(\mathbf x_*)^{1/2}
Q_F(\mathbf x_*+\mathbf z)^{-1}
Q_F(\mathbf x_*)^{1/2}
-I
\right\|
\le\frac13.
}
\tag{6}
$$

At complex parameters these are bounds for the holomorphic continuation of the complete matrix formula. A complex parameter is not assigned a positive physical minimum.

### 1.1 Proof with the exact quotient order

Choose a fixed \(G(\mathbf x_*)\)-orthonormal frame respecting

$$
E_0\oplus L\oplus O,
\qquad
L=E_1\cap E_0^{\perp_{G(\mathbf x_*)}},
\qquad
O=E_1^{\perp_{G(\mathbf x_*)}}.
$$

Call its inclusion matrix \(F\). Then

$$
F^*G(\mathbf x_*)F=I,
\qquad
F^{-1}=F^*G(\mathbf x_*).
$$

In this frame,

$$
D(\mathbf z)
=
F^{-1}C(\mathbf x_*+\mathbf z)F^{-*}
=
K_0+\sum_i e^{z_i}K_i,
$$

where

$$
K_i\succeq0,\qquad \sum_{i=0}^pK_i=I.
$$

The map

$$
v\longmapsto(K_0^{1/2}v,\ldots,K_p^{1/2}v)
$$

is an isometry. Therefore

$$
\left\|D(\mathbf z)-I\right\|
\le
\max_i|e^{z_i}-1|
\le e^{R_0}-1=\frac14.
\tag{7}
$$

Write \(D=I+\Delta\). The full source metric is \(D^{-1}\). Restrict it to \(E_1\), then minimize over \(E_0\). Block inversion gives the **inverse** of that attained quotient as

$$
\boxed{
E_F(\mathbf z)
=
D_{LL}
-D_{LO}D_{OO}^{-1}D_{OL}.
}
\tag{8}
$$

This follows by first inverting the restriction of \(D^{-1}\) to \(E_1\), and then taking its \(LL\)-block. Thus (8) is not obtained by replacing the inverse of a full matrix with an inverse of a restriction.

Equation (7) gives

$$
\|E_F-I\|
\le
\frac14+\frac{(1/4)^2}{1-1/4}
=\frac13.
$$

Hence

$$
\|E_F^{-1}-I\|\le\frac{1/3}{1-1/3}=\frac12.
$$

Undoing the fixed quotient-frame congruence proves (5)–(6).

The constants are independent of the spectrum of every \(\Omega_i\), of their ranks, and of whether they commute.

### 1.2 All mixed derivatives have an explicit bound

Use the logarithm determined by the convergent series for \(E_F-I\). Then

$$
\left|\log\det E_F\right|
\le r\log(3/2).
$$

For every nonzero multi-index \(\alpha\), multivariable Cauchy estimates prove

$$
\boxed{
\left|
\partial_{\mathbf x}^{\alpha}
\log\det Q_F(\mathbf x)
\right|
\le
r\,\alpha!\,L_0R_0^{-|\alpha|}.
}
\tag{9}
$$

Likewise,

$$
\boxed{
\left\|
Q_F(\mathbf x)^{-1/2}
(\partial^\alpha Q_F)(\mathbf x)
Q_F(\mathbf x)^{-1/2}
\right\|
\le
\frac{\alpha!}{2R_0^{|\alpha|}}.
}
\tag{10}
$$

The first derivatives also have the sharper directed identity

$$
\boxed{
-\partial_iQ_F\succeq0,
\qquad
\sum_i
Q_F^{-1/2}(-\partial_iQ_F)Q_F^{-1/2}
\preceq I.
}
\tag{11}
$$

To verify it, differentiate the complete minimum representative. Its derivative lies in the original relation space and is orthogonal to that representative, so only the metric derivative contributes. The normalized covariance derivatives are positive matrices whose sum is at most the identity.

Thus

$$
0\le-\sum_i\partial_i\log\det Q_F\le r.
$$

These statements include every fixed original flag quotient. They do not require a new rank theorem for a conjecturally identified subspace.

### 1.3 Finite changes have a global bound

For two real parameter values put

$$
a=\min(0,y_1-x_1,\ldots,y_p-x_p),
$$

$$
b=\max(0,y_1-x_1,\ldots,y_p-x_p).
$$

The source covariance satisfies

$$
e^aC(\mathbf x)\preceq C(\mathbf y)\preceq e^bC(\mathbf x).
$$

Taking the same full inverse, restriction and minimum proves

$$
\boxed{
e^{-b}Q_F(\mathbf x)
\preceq Q_F(\mathbf y)
\preceq e^{-a}Q_F(\mathbf x).
}
\tag{12}
$$

The baseline covariance is the term of logarithmic weight zero; that is why zero appears in the definitions of \(a,b\).

---

## 2. The complete projected complex current is controlled on the same domain

Retain the original observation \(\Lambda\), its kernel projection \(P(\mathbf x)\), the original action \(A\), and the same marked vector \(v\).

At a real reference point, use its exact orthonormal kernel/observation frame. The covariance has blocks \(D_{KK},D_{KB},D_{BB}\), and

$$
X(\mathbf z)=D_{KB}D_{BB}^{-1}.
$$

Equation (7) gives

$$
\|X\|\le\frac13.
$$

The complete kernel projection is

$$
P(\mathbf z)=
\begin{pmatrix}I&-X\\0&0\end{pmatrix},
$$

so

$$
\|P\|,\ \|I-P\|\le\frac{\sqrt{10}}3,
\qquad
\|G(\mathbf z)\|\le\frac43.
\tag{13}
$$

The physical pairings are

$$
z(\mathbf x)
=
\langle Pv,A(I-P)v\rangle_{G(\mathbf x)},
$$

$$
w(\mathbf x)
=
\langle(I-P)v,APv\rangle_{G(\mathbf x)}.
$$

Their holomorphic continuations are the exact formulas

$$
z(\mathbf z)=v^*G(\mathbf z)P(\mathbf z)A(I-P(\mathbf z))v,
$$

$$
w(\mathbf z)=v^*G(\mathbf z)(I-P(\mathbf z))AP(\mathbf z)v.
\tag{14}
$$

For real parameters, \(P^*G=GP\), so these are the original pairings.

A scalar multiple of the identity can be subtracted from \(A\), because \(P(I-P)=0\). Put

$$
\mathfrak a=
\|A-cI\|_{G(\mathbf x_*)}\,\|v\|_{G(\mathbf x_*)}^2
$$

for the retained arithmetic centre \(c\). Equations (13)–(14) give

$$
|z(\mathbf z)|,\ |w(\mathbf z)|
\le\frac{40}{27}\mathfrak a.
$$

Define \(f^\sharp(\mathbf z)=\overline{f(\bar{\mathbf z})}\). The actual real phase has the holomorphic continuation

$$
\mathcal P(\mathbf z)
=
\frac12\bigl(z^\sharp(\mathbf z)w(\mathbf z)
+w^\sharp(\mathbf z)z(\mathbf z)\bigr).
$$

Therefore

$$
\boxed{
\left|
\partial^\alpha
\Re(\overline z\,w)(\mathbf x_*)
\right|
\le
\left(\frac{40}{27}\right)^2
\mathfrak a^2\,\alpha!R_0^{-|\alpha|}.
}
\tag{15}
$$

Both moving projections and both complex products remain. Equation (15) bounds their variation; it does not assign their sign.

It also yields a finite Taylor certificate. On

$$
\|\mathbf z\|_1\le\theta R_0,\qquad 0<\theta<1,
$$

the total-degree-\(N\) Taylor remainder is at most

$$
\boxed{
\left(\frac{40}{27}\right)^2
\mathfrak a^2\frac{\theta^{N+1}}{1-\theta}.
}
\tag{16}
$$

The same argument gives \(rL_0\theta^{N+1}/(1-\theta)\) for the logarithmic determinant.

All derivatives are calculable through finite matrix recurrences. For example, differentiating \(C\,G=I\) gives

$$
\boxed{
G_\alpha
=
-G_0
\sum_{0<\beta\le\alpha}
\binom{\alpha}{\beta}
C_\beta G_{\alpha-\beta}.
}
\tag{17}
$$

The order of the factors is part of the formula. No commutation of the source additions is used.

---

## 3. Heat control is uniform in the heat time

The preceding derivative bounds concern matrices and phases. The full positive heat operator admits an additional control independent of the largest native action norm.

Let \(M\) be the fixed original centred arithmetic action. Put

$$
H(\mathbf x)=M^{\dagger_{G(\mathbf x)}}M.
$$

For two positive metrics in (12), singular-value comparison through the coefficient identity gives

$$
e^{-(b-a)/2}s_j(M;G(\mathbf x))
\le
s_j(M;G(\mathbf y))
\le
e^{(b-a)/2}s_j(M;G(\mathbf x)).
$$

Since

$$
\sup_{u\ge0}ue^{-u}=1/e,
$$

we obtain

$$
\boxed{
\sup_{\tau\ge0}
\left|
\operatorname{Tr}e^{-\tau H(\mathbf y)}
-\operatorname{Tr}e^{-\tau H(\mathbf x)}
\right|
\le
\frac{\operatorname{rank}M}{e}(b-a).
}
\tag{18}
$$

Likewise, for every \(a_*>0\),

$$
\boxed{
\left|
\log\det(a_*I+H(\mathbf y))
-\log\det(a_*I+H(\mathbf x))
\right|
\le
\operatorname{rank}M\,(b-a).
}
\tag{19}
$$

Zero singular directions contribute the same constant at both endpoints.

### 3.1 The actual projected full heat has a derivative bound too

Consider a straight logarithmic path

$$
\mathbf x(s)=\mathbf x_0+s\mathbf v,
$$

and put

$$
\Delta_{\mathbf v}
=
\max(0,v_1,\ldots,v_p)-\min(0,v_1,\ldots,v_p).
$$

Use the explicitly metric-compatible moving frame

$$
F'(s)=-\frac12G^{-1}G'F.
$$

In that frame,

$$
F^*GF=I,\qquad
B=F^*G'F=B^*,
$$

and the original fixed arithmetic action satisfies

$$
\dot M=\frac12[B,M].
$$

The spectrum of \(B\) has width at most \(\Delta_{\mathbf v}\). Its scalar midpoint can be subtracted from the commutator.

For \(H=M^*M\),

$$
\dot H=M^*BM-\frac12(BH+HB).
$$

Writing \(M=UH^{1/2}\), with the actual polar factor, and applying the divided-difference formula for \(e^{-\tau H}\), gives

$$
\boxed{
\|\nabla_s e^{-\tau H}\|_{\mathrm{HS}}
\le
\left(\frac1e+\frac12\right)
\frac{\sqrt q}{2}\Delta_{\mathbf v},
\qquad \tau\ge0.
}
\tag{20}
$$

The two scalar estimates behind this are

$$
\sqrt{xy}\left|
\frac{e^{-\tau x}-e^{-\tau y}}{x-y}
\right|\le\frac1e,
$$

$$
\frac{x+y}{2}\left|
\frac{e^{-\tau x}-e^{-\tau y}}{x-y}
\right|\le\frac12.
\tag{21}
$$

The first follows by differentiating in \(\log x\) and using that the logarithmic mean is at least the geometric mean. For the second, write \(\tau x=b+d,\tau y=b\). The quantity before division by two is

$$
e^{-b}\left(1+\frac{2b}{d}\right)(1-e^{-d}).
$$

Its maximum over \(b\ge0\) is at \(b=0\) for \(d\ge2\), and at \(b=1-d/2\) for \(d<2\); both maxima are below one. Repeated and zero eigenvalues are covered by the continuous limits.

For the original fixed kernel, the projection derivative in this frame is

$$
\nabla_sP_K
=
\frac12\bigl[(I-P_K)BP_K+P_KB(I-P_K)\bigr].
\tag{22}
$$

If \(P\) is this projection or its complement, of rank \(\ell\), its positive derivative trace is at most

$$
\frac14\min(\ell,q-\ell)\Delta_{\mathbf v}.
$$

Combining (20)–(22),

$$
\boxed{
\begin{aligned}
\left|
\frac d{ds}\operatorname{Tr}
\left(P(s)e^{-\tau H(s)}\right)
\right|
\le
\Delta_{\mathbf v}\left[
\frac{\min(\ell,q-\ell)}4
+\frac{\frac12+\frac1e}{2}\sqrt{\ell q}
\right].
\end{aligned}
}
\tag{23}
$$

For the original observation,

$$
\operatorname{Tr}_B\!\left(\Lambda e^{-\tau H}L\right)
=
\operatorname{Tr}_E\!\left((I-P_K)e^{-\tau H}\right).
$$

Thus (23) is a bound for the actual observed full heat, not a trace in a different observation space.

A varying period can also move \(\Lambda\). Its additional frame derivative must then be retained. No dimension-only bound can control an arbitrarily fast reparameterization of that extra motion.

---

## 4. Every multiscale covariance family has an explicit metric normal form

The bounds above hold at all positive source weights. The following calculation determines the complete boundary scales.

After the fixed initial isometry, consider

$$
C(T)=I+\sum_{j=1}^sT^{a_j}K_j,
\qquad
a_1>\cdots>a_s>0,
\qquad K_j\succeq0.
\tag{24}
$$

Equal weights have already been combined by addition of their actual covariance matrices.

Set

$$
V_j=\sum_{i\le j}\operatorname{ran}K_i,
\qquad
E_j=V_j\cap V_{j-1}^{\perp},
$$

and let \(P_j\) project onto \(E_j\). Let \(P_0\) project onto \(V_s^\perp\).

Define

$$
D_T=P_0+\sum_jT^{a_j/2}P_j,
$$

$$
H_j=P_jK_jP_j|_{E_j},
\qquad
H_\infty=P_0+\sum_jP_jK_jP_j.
\tag{25}
$$

Every nonempty \(H_j\) is positive definite. Indeed, a vector in \(E_j\) annihilated by \(K_j\) is orthogonal both to \(V_{j-1}\) and to \(\operatorname{ran}K_j\), hence to \(V_j\), and is zero.

The exact limit is

$$
\boxed{
D_T^{-1}C(T)D_T^{-1}\longrightarrow H_\infty.
}
\tag{26}
$$

### 4.1 A finite error, not merely a limit

For \(j>1\), set

$$
\delta_j(T)=T^{-(a_{j-1}-a_j)/2}.
$$

Then

$$
\boxed{
\left\|D_T^{-1}C(T)D_T^{-1}-H_\infty\right\|
\le
T^{-a_s}
+\sum_{j=2}^s
(2\delta_j+\delta_j^2)\|K_j\|.
}
\tag{27}
$$

To prove it, the \(j\)-th normalized summand is

$$
(P_j+R_j(T))K_j(P_j+R_j(T)),
$$

where \(R_j(T)\) acts only on \(V_{j-1}\) and has norm at most \(\delta_j(T)\). The identity contribution supplies \(T^{-a_s}\).

There is also an all-\(T\ge1\) comparison with no division by the exponent gaps.

Put

$$
W_j=K_jP_jH_j^{-1},
\qquad
L=\sum_j\|W_j-P_j\|,
\qquad
\gamma=\min\bigl(1,\min_j\lambda_{\min}H_j\bigr).
$$

The exact factor

$$
K_j\succeq W_jH_jW_j^*
$$

follows by inserting the orthogonal projection onto
\(\operatorname{ran}(K_j^{1/2}P_j)\).

The matrix

$$
U=P_0+\sum_jW_jP_j
$$

is block upper triangular with identity diagonal. After conjugation by \(D_T\), its strictly upper part has norm at most \(L\), and its inverse is the finite nilpotent series. Therefore

$$
\boxed{
\frac{\gamma}{(1+L+\cdots+L^s)^2}\,I
\preceq
D_T^{-1}C(T)D_T^{-1}
\preceq
\left(1+\sum_j\|K_j\|\right)I.
}
\tag{28}
$$

This remains valid when several source ranges coincide or some layer is empty. For arbitrary positive weights, sort them together with the baseline weight one. The same construction applies on each of the finitely many ordering charts; subunit weights enter the upper bound, while the baseline controls their remaining directions.

### 4.2 All singular and exterior scales of the arithmetic action

The exact model metric is

$$
G_{\mathrm{mod}}(T)=D_T^{-1}H_\infty^{-1}D_T^{-1}.
$$

Its isometry to Euclidean coordinates is

$$
S_T=H_\infty^{-1/2}D_T^{-1}.
$$

Choose orthonormal bases inside the layers. Let their weights be \(w_1,\ldots,w_q\), including zero on \(V_s^\perp\), and put

$$
\widehat A=H_\infty^{-1/2}AH_\infty^{1/2}.
$$

Then

$$
(S_TAS_T^{-1})_{ij}
=
T^{(w_j-w_i)/2}\widehat A_{ij}.
$$

For every exterior rank \(r\le\operatorname{rank}A\), define

$$
\boxed{
\beta_r=
\max_{\det\widehat A_{I,J}\ne0}
\frac{\sum_{j\in J}w_j-\sum_{i\in I}w_i}{2}.
}
\tag{29}
$$

Let \(\mathcal A_r\) be the full exterior matrix retaining precisely the minors attaining that exponent. It is nonzero. Then

$$
\boxed{
T^{-\beta_r}
\|\wedge^rA\|_{G(T)}
\longrightarrow\|\mathcal A_r\|.
}
\tag{30}
$$

The finite relative comparison in (27) bounds the error before taking a limit. In particular, it supplies an actual guard when the coefficient data themselves vary with \(k\); a fixed-data \(o(1)\) has not been declared uniform in \(k\).

For operator norm,

$$
\beta_1=
\max_{P_iAP_j\ne0}\frac{a_j-a_i}{2},
$$

with the complementary weight zero included. Thus

$$
\boxed{
\|A\|_{G(T)}\text{ stays bounded}
\quad\Longleftrightarrow\quad
A V_j\subset V_j\ \text{for every }j.
}
\tag{31}
$$

The equivalence follows directly from the displayed action blocks. It does not assume an arithmetic invariant filtration.

For an invertible \(A\), the full exterior exponent is zero:

$$
\det(S_TAS_T^{-1})=\det A.
$$

Growing and shrinking singular directions therefore compensate exactly.

### 4.3 Complete fixed subquotients

For a fixed inclusion \(B:\mathbb C^m\to E\), set

$$
C_B=H_\infty^{-1/2}B.
$$

The \(r\)-th exterior norm of \(D_T^{-1}C_B\) is governed by the least sum of row weights among its nonzero \(r\times r\) minors. Denote that sum by \(w_r\), with \(w_0=0\), and the norm of the full leading exterior matrix by \(c_r>0\).

Then the eigenvalues of the actual restricted metric satisfy

$$
\boxed{
\lambda_r(B^*G(T)B)
\sim
\left(\frac{c_r}{c_{r-1}}\right)^2
T^{-(w_r-w_{r-1})}.
}
\tag{32}
$$

The matrix of all leading minors is retained, not a single favoured minor.

For a quotient \(E/E_0\), its exact covariance is

$$
\Lambda_0C(T)\Lambda_0^*.
$$

For \(E_1/E_0\), restrict that attained quotient to its actual image of \(E_1\). Every representative of that value lies in \(E_1\), because its difference from a chosen lift lies in \(E_0\). Thus this order of quotient and restriction is exactly the original full minimum.

Applying (24)–(32) to the projected source matrices therefore calculates every fixed flag’s metric and exterior scales.

### 4.4 A noncommuting check in closed form

Take

$$
b_1=(1,1,0)^T,\quad
b_2=(1,i,1)^T,\quad
b_3=(1,0,0)^T,
$$

and

$$
C(T)=I+T^3b_1b_1^*+Tb_2b_2^*+T^2b_3b_3^*.
$$

The three layers are

$$
\frac{(1,1,0)}{\sqrt2},\qquad
\frac{(1,-1,0)}{\sqrt2},\qquad
(0,0,1),
$$

with weights \(3,2,1\), and

$$
H_\infty=\operatorname{diag}(2,1/2,1).
$$

Hence the covariance eigenvalues are asymptotic to

$$
2T^3,\quad \frac12T^2,\quad T.
$$

For the original-coordinate subspace \(\mathbb Ce_1\),

$$
e_1^*C(T)^{-1}e_1\sim T^{-2}.
$$

For \(A=e_3e_1^*\),

$$
\|A\|_{C(T)^{-1}}\sim T.
$$

This agrees with the exact layer calculation (29). No commuting approximation was used.

---

## 5. The full observed memory has a gap-free positive representation

Return to the original metric and its orthogonal decomposition

$$
E=K\oplus L B.
$$

Write the original arithmetic operator as

$$
M=
\begin{pmatrix}
M_K&D\\
C&M_B
\end{pmatrix}.
$$

Then

$$
H=M^\dagger M
=
\begin{pmatrix}
A&B_H\\
B_H^\dagger&D_H
\end{pmatrix},
$$

where

$$
A=M_K^\dagger M_K+C^\dagger C,
$$

$$
B_H=M_K^\dagger D+C^\dagger M_B,
$$

$$
D_H=D^\dagger D+M_B^\dagger M_B.
\tag{33}
$$

These are the complete original blocks in the repository’s observed-heat equation. In particular, \(D_H\) is not replaced by \(M_B^\dagger M_B\).

Positivity proves

$$
\ker A\subset\ker B_H^\dagger,
\qquad
S=D_H-B_H^\dagger A^+B_H\succeq0.
$$

Let \(P_\lambda\) be the spectral projections of \(A\) for \(\lambda>0\), and define

$$
C_\lambda=\lambda^{-1}B_H^\dagger P_\lambda B_H\succeq0.
$$

Then

$$
\sum_{\lambda>0}C_\lambda
=B_H^\dagger A^+B_H
=:T\preceq D_H.
\tag{34}
$$

The memory kernel and its Laplace-domain pencil are exactly

$$
\boxed{
\mathcal M(\tau)
=
B_H^\dagger e^{-\tau A}B_H
=
\sum_{\lambda>0}\lambda e^{-\lambda\tau}C_\lambda,
}
\tag{35}
$$

$$
\boxed{
\mathcal F(z)
=
zI+D_H-B_H^\dagger(zI+A)^{-1}B_H
=
zI+S+\sum_{\lambda>0}\frac{z}{z+\lambda}C_\lambda.
}
\tag{36}
$$

The compressed resolvent is

$$
\boxed{
\Lambda(zI+H)^{-1}L=\mathcal F(z)^{-1}.
}
\tag{37}
$$

Every \(C_\lambda\) is a full positive matrix; they need not commute.

### 5.1 All memory derivatives have a common integral bound

For every integer \(n\ge0\),

$$
(-1)^n\mathcal M^{(n)}(\tau)\succeq0,
$$

and

$$
\boxed{
\int_0^\infty
\tau^n(-1)^n\mathcal M^{(n)}(\tau)\,d\tau
=n!T\preceq n!D_H.
}
\tag{38}
$$

Pointwise,

$$
\boxed{
\tau^{n+1}(-1)^n\mathcal M^{(n)}(\tau)
\preceq
\left(\frac{n+1}{e}\right)^{n+1}T.
}
\tag{39}
$$

These follow by integrating or maximizing the actual scalar factors
\(\lambda^{n+1}\tau^ne^{-\lambda\tau}\).

There is no lower bound on the positive \(\lambda\) in (38)–(39). Long memory at small \(\lambda\) remains present with its exact weight.

For \(z>0\),

$$
\mathcal F'(z)
=I+\sum_\lambda\frac{\lambda}{(z+\lambda)^2}C_\lambda.
$$

For all \(n\ge1\), subtracting \(I\) at \(n=1\),

$$
\boxed{
0\preceq
z^n(-1)^{n-1}
\bigl(\mathcal F^{(n)}(z)-\mathbf1_{n=1}I\bigr)
\preceq
n!\frac{n^n}{(n+1)^{n+1}}T.
}
\tag{40}
$$

For \(\Im z>0\),

$$
\Im\mathcal F(z)
=
(\Im z)\left[
I+\sum_\lambda
\frac{\lambda}{|z+\lambda|^2}C_\lambda
\right]\succ0.
\tag{41}
$$

Thus the analytic pencil is controlled on the full upper half-plane, not only at positive real regularizers.

### 5.2 The exact smallest memory realization

Let

$$
r_{\mathrm{mem}}=\sum_{\lambda>0}\operatorname{rank}C_\lambda.
$$

The coupled kernel space is

$$
K_{\mathrm{coupled}}
=
\bigoplus_{\lambda>0}\operatorname{ran}(P_\lambda B_H).
$$

Its orthogonal complement is invariant under \(A\) and annihilated by \(B_H^\dagger\).

On

$$
\bigoplus_{\lambda>0}\operatorname{ran}C_\lambda,
$$

define

$$
A_{\min}=\bigoplus_\lambda\lambda I,
\qquad
B_{\min}=
\operatorname{stack}_\lambda\sqrt\lambda\,C_\lambda^{1/2}.
$$

The explicit isometry to the original coupled kernel is

$$
\boxed{
J_\lambda=
\lambda^{-1/2}P_\lambda B_HC_\lambda^{+1/2}.
}
\tag{42}
$$

It intertwines both \(A_{\min}\) and \(B_{\min}\) with the original blocks.

The reduced positive matrix

$$
\begin{pmatrix}
A_{\min}&B_{\min}\\
B_{\min}^\dagger&D_H
\end{pmatrix}
$$

has the exact same observed resolvent and heat as (33). The discarded original kernel summand remains as a separate decoupled block in the full trace.

This realization is minimal among positive selfadjoint finite realizations of the same memory: the residue at each distinct pole \(-\lambda\) has rank \(\operatorname{rank}C_\lambda\), requiring at least that many states at that eigenvalue.

---

## 6. Complete heat and determinant mixing are bounded by the coupling rank

Put

$$
H_0=\operatorname{diag}(A,D_H),
\qquad
r_c=\operatorname{rank}B_H.
$$

Define the complete heat-mixing quantity

$$
\mathcal Q(\tau)
=
\operatorname{Tr}e^{-\tau H}
-\operatorname{Tr}e^{-\tau A}
-\operatorname{Tr}e^{-\tau D_H}.
$$

Then

$$
\boxed{
0\le\mathcal Q(\tau)
\le
\min\{r_c,\ \tau^2\|B_H\|_{\mathrm{HS}}^2\}.
}
\tag{43}
$$

### 6.1 Positivity retains the complete operator

Choose eigenbases of \(A\) and \(D_H\). For each corresponding unit vector \(v\), the spectral measure of the full \(H\) and scalar convexity give

$$
\langle v,e^{-\tau H}v\rangle
\ge e^{-\tau\langle v,Hv\rangle}.
$$

Sum over the two bases. This proves \(\mathcal Q(\tau)\ge0\).

This is a trace inequality. It does not assert the generally unjustified operator inequality

$$
P_Be^{-\tau H}P_B\succeq e^{-\tau D_H}.
$$

### 6.2 The rank bound

The off-diagonal perturbation

$$
O=\begin{pmatrix}0&B_H\\B_H^\dagger&0\end{pmatrix}
$$

has positive and negative parts of rank \(r_c\). First add \(O_+\) to \(H_0\), then subtract \(O_-\).

Min–max shows that adding \(O_+\) cannot increase the trace of the decreasing scalar function \(e^{-\tau x}\). Subtracting a rank-\(r_c\) positive matrix can increase that trace by at most \(r_c\), because the scalar function lies between zero and one. This proves the first upper bound.

### 6.3 The quadratic bound

The path

$$
H_s=H_0+sO,\qquad 0\le s\le1,
$$

is positive. For

$$
\phi(s)=\operatorname{Tr}e^{-\tau H_s},
$$

one has \(\phi'(0)=0\), and

$$
\phi''(s)
=
\tau^2\int_0^1
\operatorname{Tr}
\left(
Oe^{-(1-u)\tau H_s}Oe^{-u\tau H_s}
\right)du.
$$

In the actual eigenbasis of \(H_s\), this is a sum of

$$
|O_{ij}|^2e^{-\tau[(1-u)\lambda_i+u\lambda_j]}.
$$

It is nonnegative and at most \(\tau^2\|O\|_{\mathrm{HS}}^2\). Since

$$
\|O\|_{\mathrm{HS}}^2=2\|B_H\|_{\mathrm{HS}}^2,
$$

integration against \(1-s\) proves the second upper bound in (43).

### 6.4 Return to the original observed compression

The same scalar Jensen calculation on the observed block gives

$$
0\le
\operatorname{Tr}\!\left(\Lambda e^{-\tau H}L\right)
-\operatorname{Tr}e^{-\tau D_H}
\le\mathcal Q(\tau).
\tag{44}
$$

Since

$$
D_H=M_B^\dagger M_B+D^\dagger D,
$$

min–max and a positive interpolation give

$$
0\le
\operatorname{Tr}e^{-\tau M_B^\dagger M_B}
-\operatorname{Tr}e^{-\tau D_H}
\le
\min\{\operatorname{rank}D,\ \tau\|D\|_{\mathrm{HS}}^2\}.
$$

Combining,

$$
\boxed{
\begin{aligned}
-\min\{\operatorname{rank}D,\tau\|D\|_{\mathrm{HS}}^2\}
\le{}&
\operatorname{Tr}\!\left(\Lambda e^{-\tau H}L\right)
-\operatorname{Tr}e^{-\tau M_B^\dagger M_B}\\
\le{}&
\min\{\operatorname{rank}B_H,\tau^2\|B_H\|_{\mathrm{HS}}^2\}.
\end{aligned}}
\tag{45}
$$

Both ranks are at most \(\dim K\). This proves (1)–(2).

The error can be order \(k\) on the original simple family, so it is not automatically negligible at the arithmetic \(k\)-scale. It is uniformly negligible after normalization by \(q=(k+1)^2\).

### 6.5 The complete logarithmic mixing is also explicit

Define

$$
g(z)
=
\log\det(zI+A)+\log\det(zI+D_H)
-\log\det(zI+H).
$$

The full determinant identity and (43) give

$$
\boxed{
g(z)
=
\log\det(zI+D_H)-\log\det\mathcal F(z)
=
\int_0^\infty e^{-z\tau}\frac{\mathcal Q(\tau)}{\tau}\,d\tau.
}
\tag{46}
$$

Thus \(g\) is completely monotone on \(z>0\), and

$$
\boxed{
0\le g(z)\le\frac{\|B_H\|_{\mathrm{HS}}^2}{z^2},
}
$$

$$
\boxed{
0\le(-1)^ng^{(n)}(z)
\le
\min\left\{
\frac{r_c(n-1)!}{z^n},
\frac{\|B_H\|_{\mathrm{HS}}^2(n+1)!}{z^{n+2}}
\right\},
\quad n\ge1.
}
\tag{47}
$$

A useful rank form is

$$
\boxed{
g(z)\le
r_c\log\left(
1+\frac{\min(\|A\|,\|D_H\|)}z
\right).
}
\tag{48}
$$

It follows by applying the same Schur determinant on either block and using \(\mathcal F(z)\succeq zI\).

The local leakage correction is

$$
\ell(z)
=
\log\det(zI+D_H)
-\log\det(zI+M_B^\dagger M_B)\ge0.
$$

The actual observed pencil therefore satisfies

$$
\boxed{
\log\det\mathcal F(z)
-\log\det(zI+M_B^\dagger M_B)
=
\ell(z)-g(z).
}
\tag{49}
$$

Both nonnegative terms remain; their difference is not assigned a sign.

At every original cutoff,

$$
\boxed{
|\ell(z)-g(z)|
\le
m\log\left(1+\frac{\|M\|_G^2}{z}\right).
}
\tag{50}
$$

For the supplied joint-source metric,

$$
\log^+\|M\|_{G_N^J}
=O_h(k\log^2(q+2)).
$$

Hence at fixed \(z>0\), the right side of (50) is

$$
O_h(k^2\log^2(q+2))=o_h(kq).
\tag{51}
$$

This completes the joint-source observed positive spectral comparison at that scale. The corresponding canonical bound can still be of order \(kq\), and has not been assigned the joint value. The original source explicitly distinguishes those metrics and their leakage term. 

---

## 7. The conductor detects every sufficiently low-degree proper rational family

This extends the repository’s original inverse-power calculation to arbitrary poles, their full multiplicities, and collisions among translated poles.

Retain the original finite translation operator

$$
\mathcal T_Af(S)=\sum_{j=1}^{J}a_jf(S+b_j),
$$

with nonzero symbol

$$
E_A(z)=\sum_ja_je^{b_jz},
\qquad
v=\operatorname{ord}_0E_A,
\qquad
\mu_v\ne0.
$$

Coincident shifts can be combined by their exact coefficient sum. The labelled product below may still retain all of them.

Let \(\chi\) be the original upper relation and \(\widehat\chi\) the lower one. The induced full-jet map is justified by the exact divisibilities

$$
\widehat\chi(S)\mid\chi(S+b_j).
\tag{52}
$$

The original map \(C_A:E\to E_-\) therefore satisfies

$$
C_A[P]=[\mathcal T_AP],
\qquad K\subset\ker C_A.
$$

Choose any monic polynomial

$$
D(S)=\prod_\alpha(S-z_\alpha)^{m_\alpha},
\qquad d=\deg D,
\qquad (D,\chi)=1.
$$

Define the original arithmetic subspace

$$
\boxed{
U_Dp=[p/D],
\qquad \deg p<d.
}
\tag{53}
$$

The physical value remains \(\eta U_Dp\), with the original full unit in \(\eta\).

### 7.1 A nonzero translation operator has no proper-rational kernel

For a nonzero proper rational \(f\), write its actual expansion at infinity

$$
f(S)=cS^{-n_0}+O(S^{-n_0-1}),
\qquad n_0\ge1,\quad c\ne0.
$$

The first nonzero term of its translated sum is

$$
\boxed{
\mathcal T_Af(S)
=
(-1)^v
\binom{n_0+v-1}{v}\mu_vc\,
S^{-n_0-v}
+O(S^{-n_0-v-1}).
}
\tag{54}
$$

All contributions from higher Laurent coefficients have a symbol moment of order below \(v\) at this leading power and vanish. The displayed coefficient is nonzero.

Thus

$$
\boxed{\mathcal T_Af=0\quad\Longrightarrow\quad f=0}
\tag{55}
$$

on the complete space of proper rational functions.

This includes translated-pole collisions. It is not a simple-pole argument.

### 7.2 The exact finite observation guard

Use the fixed-degree common denominator

$$
\mathcal B(S)=\prod_{j=1}^{J}D(S+b_j),
\qquad L=Jd.
$$

For \(f=p/D\),

$$
N_p(S)=\mathcal B(S)\mathcal T_A(p/D)(S)
$$

is a polynomial. Equation (54) gives

$$
\deg N_p\le L-v-1.
$$

The denominator is coprime to \(\widehat\chi\), by (52) and \((D,\chi)=1\). Therefore vanishing of all original lower jets makes \(\widehat\chi\) divide \(N_p\).

On the explicit degree domain

$$
\boxed{Jd-v\le q':=\deg\widehat\chi,}
\tag{56}
$$

this forces \(N_p=0\), then \(p=0\) by (55). Hence

$$
\boxed{\ker C_A\cap U_D\mathcal P_{d-1}=0.}
\tag{57}
$$

The same proof uses the smaller degree of the actual least common denominator when some translated poles coincide. For a family crossing such collisions, the fixed product \(\mathcal B\) gives one constant-degree formula.

Equation (57), together with \(K\subset\ker C_A\), proves (3). The complexity is always finite: \(D=\chi+1\) and the original remainder polynomial give a proper rational representative of degree at most \(q\).

### 7.3 A global coefficient inverse survives changes of the symbol order

Define the polynomial columns

$$
F_l(S)
=
\mathcal B(S)
\sum_{j=1}^{J}
a_j\frac{(S+b_j)^l}{D(S+b_j)},
\qquad 0\le l<d.
$$

Let \(\mathscr T_D\) be their coefficient matrix through degree \(L-1\).

It has rank \(d\) whenever the original symbol is nonzero, by (55). Its entries are polynomial expressions in the coefficients of \(D\), the shifts, and the conductor coefficients. No difference between pole centres is inverted.

On the uniform family domain \(L\le q'\), take the actual lower quotient value \(y=C_AU_Dp\). Then

$$
N_p=\operatorname{rem}_{\widehat\chi}(\mathcal B y)
$$

as an actual polynomial of degree below \(L\). Thus

$$
\boxed{
W_D
=
(\mathscr T_D^*\mathscr T_D)^{-1}\mathscr T_D^*
\,\operatorname{coeff}_{<L}
\,M_{\mathcal B}^{(-)}
}
\tag{58}
$$

satisfies

$$
\boxed{W_DC_AU_D=I_d.}
\tag{59}
$$

Here \(M_{\mathcal B}^{(-)}\) is multiplication by \(\mathcal B\) in the original lower quotient. All complete lower jets are converted by their actual Hermite map.

This inverse is real analytic across a zero of \(\mu_0\), or any other change in the first nonzero symbol moment, as long as the full operator remains nonzero. Its finite norm has the bound

$$
\boxed{
\|W_D\|
\le
\left[
\frac{
\operatorname{Tr}(\mathscr T_D^*\mathscr T_D)^{d-1}
}{
\det(\mathscr T_D^*\mathscr T_D)
}
\right]^{1/2}
\left\|\operatorname{coeff}_{<L}M_{\mathcal B}^{(-)}\right\|.
}
\tag{60}
$$

The Gram in this expression is a specified finite polynomial coefficient Gram, not an unevaluated native observation kernel.

For example,

$$
\mathcal T_\epsilon f(S)
=(1+\epsilon)f(S+1)-f(S),
\qquad D(S)=S,
$$

has

$$
\mathcal B(S)\mathcal T_\epsilon(1/S)=\epsilon S-1.
$$

Its coefficient column is \((-1,\epsilon)^T\), and its inverse uses

$$
\frac{(-1,\bar\epsilon)}{1+|\epsilon|^2}.
$$

It remains bounded at \(\epsilon=0\), where the symbol order changes from zero to one. Dividing only by \(\mu_0=\epsilon\) would have introduced an artificial singularity.

### 7.4 The original symbol also gives a triangular inverse

Write

$$
f(S)=\sum_{n\ge1}c_nS^{-n},
\qquad
\mathcal T_Af(S)=\sum_{m\ge1}b_mS^{-m},
$$

and

$$
e(z)=z^{-v}E_A(-z),\qquad
h_j=[z^j]e(z)^{-1}.
$$

Then

$$
\boxed{
c_n
=
(n-1)!
\sum_{l=1}^{n}
h_{n-l}\frac{b_{v+l}}{(v+l-1)!},
\qquad1\le n\le d.
}
\tag{61}
$$

Finally,

$$
\boxed{
p(S)=
\operatorname{pol}_{S=\infty}
\left[D(S)\sum_{n=1}^{d}c_nS^{-n}\right].
}
\tag{62}
$$

To verify (61), the coefficient of \(S^{-m}\) is

$$
b_m
=
\sum_{n=1}^{m}
(-1)^{m-n}
\binom{m-1}{m-n}\mu_{m-n}c_n.
$$

Division by \((m-1)!\), at \(m=v+l\), turns this into ordinary finite convolution by \(e(z)\). Equations (61)–(62) invert that convolution.

The two inverse constructions agree on the actual conductor image because both recover \(p\). They need not agree on unrelated output vectors.

### 7.5 Pole collisions retain the full arithmetic metric

In separated partial-fraction coordinates, the numerator columns are

$$
D(S)/(S-z_\alpha)^j.
$$

Their coefficient matrix \(\mathcal P_D\), ordered by root and increasing pole order, has

$$
\boxed{
\det\mathcal P_D
=
(-1)^{d(d-1)/2}
\prod_{\alpha<\beta}
(z_\beta-z_\alpha)^{m_\alpha m_\beta}.
}
\tag{63}
$$

This follows from the full Hermite evaluation map and the local triangular division by \(D/(S-z_\alpha)^{m_\alpha}\).

The numerator coordinate \(p\) remains a fixed \(d\)-dimensional frame through collisions. For any original positive arithmetic metric,

$$
\boxed{
G_{\mathrm{partial}}
=
\mathcal P_D^*(U_D^*GU_D)\mathcal P_D.
}
\tag{64}
$$

The observed Gram has exactly the same congruence. Thus the determinant vanishing of the separated-pole frame is retained, while the full confluent numerator frame remains nondegenerate.

For instance,

$$
\frac1\epsilon
\left(\frac1{S-\epsilon}-\frac1S\right)
\longrightarrow\frac1{S^2}.
$$

The numerator of the left side in the common denominator \(S(S-\epsilon)\) is exactly one. This is the explicit recovery of the additional confluent pole, not deletion of the diverging separated coefficients.

### 7.6 Return through the actual native observation norm

The original map has

$$
C_A=R_A\Lambda,
\qquad
R_A=C_AL_N.
$$

For

$$
Q_N=(\Lambda G_N^{-1}\Lambda^*)^{-1},
\qquad
\Gamma_A=C_AG_N^{-1}C_A^*,
$$

one has

$$
R_AQ_N^{-1}R_A^*=\Gamma_A.
$$

The complete lower minimum therefore gives

$$
\boxed{
U_D^*\Lambda^*Q_N\Lambda U_D
\succeq
(C_AU_D)^*\Gamma_A^{-1}(C_AU_D).
}
\tag{65}
$$

With \(H_D=U_D^*G_NU_D\), equations (59) and (65) give

$$
\boxed{
U_D^*\Lambda^*Q_N\Lambda U_D
\succeq
\ell_D H_D,
\qquad
\ell_D=
\frac1{
\lambda_{\max}\Gamma_A\,
\|W_D\|^2\,
\lambda_{\max}H_D
}>0.
}
\tag{66}
$$

Every quantity is in the original metrics. In particular, the full arithmetic unit remains in \(\Lambda\) and \(G_N\).

---

## 8. Multipole detection controls the full slow singular subspace of an arithmetic filter

Let \(p(y)\) be monic of degree \(d\), coprime to the original relation. Retain the original full minimum polynomial section

$$
\widehat R_N:E\to\mathcal P_N.
$$

Divide its actual polynomial representative:

$$
\widehat R_Nx
=
p\,\mathfrak Q_p\widehat R_Nx
+\mathfrak R_p\widehat R_Nx.
$$

Then

$$
\boxed{
p(M)^{-1}
=
B_p+U_pT_p,
}
\tag{67}
$$

where

$$
B_p=J_N\mathfrak Q_p\widehat R_N,
\qquad
T_p=\mathfrak R_p\widehat R_N,
\qquad
U_pr=[r/p].
$$

The first term has the finite original bound

$$
\|B_p\|
\le
D_p:=
\|\mathfrak Q_p\|_{H_N\to H_{N-d}}.
\tag{68}
$$

Its coefficient matrix is the actual long-division map, and its norm uses the full native moment matrices.

Put \(X=p(M)^{-1}\), and order its singular values decreasingly:

$$
\sigma_1(X)\ge\cdots\ge\sigma_q(X)>0.
$$

Let \(V_d\) be its top \(d\) left singular subspace. Since the second term of (67) has range in \(\operatorname{im}U_p\) and rank at most \(d\),

$$
\sigma_{d+1}(X)\le D_p,
$$

and

$$
\boxed{
\|(I-P_{U_p})P_{V_d}\|
\le
\varepsilon_p:=
\min\left\{1,\frac{D_p}{\sigma_d(X)}\right\}.
}
\tag{69}
$$

Apply the native rational observation bound \(\ell_p\) from (66). Every unit vector in \(V_d\) then has observed fraction at least

$$
\boxed{
\ell_{\mathrm{slow}}
=
\left(
\sqrt{\ell_p}\sqrt{1-\varepsilon_p^2}
-\varepsilon_p
\right)_+^2.
}
\tag{70}
$$

The left singular vectors of \(p(M)^{-1}\) are the right singular vectors of \(p(M)\). Therefore the full filtered heat satisfies

$$
\boxed{
\operatorname{Tr}\!\left(
P_Be^{-\tau p(M)^\dagger p(M)}
\right)
\ge
\ell_{\mathrm{slow}}
\sum_{j=1}^{d}e^{-\tau/\sigma_j(X)^2}.
}
\tag{71}
$$

Its kernel counterpart has the complete upper bound

$$
\boxed{
\begin{aligned}
\operatorname{Tr}\!\left(
P_Ke^{-\tau p(M)^\dagger p(M)}
\right)
\le{}&
(1-\ell_{\mathrm{slow}})
\sum_{j=1}^{d}e^{-\tau/\sigma_j(X)^2}\\
&+(q-d)e^{-\tau/D_p^2}.
\end{aligned}}
\tag{72}
$$

The last term is absent at \(d=q\).

This generalizes the source’s one inverse-power late-heat comparison to the entire proper rational family. The small matrix

$$
H_p^{1/2}T_pG_N^{-1}T_p^*H_p^{1/2}
$$

contains the nonzero singular values of the finite-rank part \(U_pT_p\), so the finite guard in (69) can also be evaluated using that matrix and \(D_p\).

The right side of (70) may be zero when the available approximation is not sufficiently accurate. It is not replaced by a positive constant without checking the stated finite quantities.

---

## 9. Rank-changing parameter families have an explicit boundary correction

Uniform logarithmic source-weight control does not justify continuity of a literal source image when that image loses rank. The complete extension can nevertheless be constructed.

Let \(B(p)\) be a holomorphic finite source coefficient matrix in a fixed ambient source with positive metric \(H(p)\). Include the original scalar source \(X\) among its columns, with the original value map \(J|_X\) onto \(E\).

On the maximal-rank locus, consider

$$
p\longmapsto\operatorname{im}B(p)
$$

in the Grassmannian. Take the closure of its graph. Every limiting plane \(Y\) contains both the literal image at that point and the original \(X\).

On a Grassmann chart,

$$
Y=\operatorname{im}\binom I Z.
$$

Its full source Gram and value map are

$$
H_Y=\binom I Z^*H\binom I Z,
\qquad
J_Y=J\binom I Z,
$$

with the obvious parenthesized interpretation
\(H_Y=[I;Z]^*H[I;Z]\).
The attained quotient is

$$
\boxed{
Q_Y=(J_YH_Y^{-1}J_Y^*)^{-1}.
}
\tag{73}
$$

It stays positive because \(Y\) contains \(X\), and

$$
\boxed{
Q_{\mathrm{ambient}}\preceq Q_Y\preceq Q_X.
}
\tag{74}
$$

At a rank-drop point, orthogonalize the extra columns of \(Y\) against the **whole literal source**. If their actual normal Gram and value map are \(H_{\mathrm{miss}},F_{\mathrm{miss}}\), then

$$
\boxed{
Q_Y
=
\left[
Q_{\mathrm{literal}}^{-1}
+
F_{\mathrm{miss}}H_{\mathrm{miss}}^+
F_{\mathrm{miss}}^*
\right]^{-1}.
}
\tag{75}
$$

This is the boundary correction, with its complete minimum.

### 9.1 A two-parameter example displays the exceptional fibre

In \(\mathbb C^3\), with its Euclidean metric and

$$
J(x_1,x_2,x_3)=x_1+x_2+x_3,
$$

retain \(X=\mathbb Ce_1\) and

$$
R_{z_1,z_2}
=
(1-z_1-z_2)e_1+z_1e_2+z_2e_3.
$$

It has \(JR=1\). The full normal data are

$$
H_Z=|z_1|^2+|z_2|^2,\qquad F_Z=z_1+z_2,
$$

so

$$
|F_Z|^2\le2H_Z
$$

everywhere.

Along the direction \([a:b]\), the limiting joint metric is

$$
\boxed{
\frac{|a|^2+|b|^2}
{|a|^2+|b|^2+|a+b|^2}.
}
\tag{76}
$$

It equals \(1/3\), \(1/2\), or \(1\) on the directions \([1:1]\), \([1:0]\), and \([1:-1]\). The literal metric at the origin is one.

The graph extension retains the projective direction \([a:b]\). It does not select one of these different limits and call the original metric continuous.

### 9.2 Observation-rank loss has a separate factor

For a holomorphic observation of generic rank \(r\), use a row-Grassmann chart

$$
\Lambda_{\mathrm{sat}}=[I,Z].
$$

The actual observation factors there as

$$
\boxed{
\Lambda=A\,\Lambda_{\mathrm{sat}},
}
\tag{77}
$$

where \(A\) is the original selected \(r\times r\) column block.

On the full-rank locus,

$$
\boxed{
Q_\Lambda=A^{-*}Q_{\mathrm{sat}}A^{-1},
\qquad
L_\Lambda=L_{\mathrm{sat}}A^{-1}.
}
\tag{78}
$$

Therefore its observed arithmetic action satisfies

$$
\boxed{
A_{B,\Lambda}
=
A\,A_{B,\mathrm{sat}}A^{-1}.
}
\tag{79}
$$

The metric and action transform together. A coefficient pole of \(A^{-1}\) is not by itself a blow-up of the action norm in its own quotient metric.

At a rank-drop point the literal target is \(\operatorname{im}A\). If \(L_A\) is the full minimum section of \(A\) in \(Q_{\mathrm{sat}}\), the literal observed action is

$$
A_{B,\mathrm{literal}}
=
A\,A_{B,\mathrm{sat}}L_A,
$$

and the exact descent defect is

$$
\boxed{
A\,A_{B,\mathrm{sat}}
-A_{B,\mathrm{literal}}A
=
A\,A_{B,\mathrm{sat}}P_{\ker A}.
}
\tag{80}
$$

Thus the new kernel is retained in the arithmetic action.

### 9.3 An explicit finite pivot construction controls every parameter branch

The singular factor \(A\) can itself be analysed without assuming a one-parameter path.

Blow up the projective direction of its list of entries. On a chart with selected entry \(a_1\), every entry is \(a_1\) times its retained ratio. The selected ratio is one. Fixed permutations and elementary row and column operations reduce that ratio matrix to

$$
\operatorname{diag}(1,B_1).
$$

Repeat on the entries of \(B_1\). After at most \(r\) pivots, each resulting chart has

$$
\boxed{
A=P\,\operatorname{diag}(d_1,\ldots,d_r)\,Q,
\qquad
d_i=a_1a_2\cdots a_i,
}
\tag{81}
$$

with \(P,Q\) holomorphic and invertible.

Each step is the closure of the explicitly displayed projective graph of the residual entries. Its charts cover every approaching parameter branch. This construction does not assert that the divisor of every \(a_i\) is already normal crossing.

All metric factors are retained:

$$
\boxed{
P^*Q_\Lambda P
=
D^{-*}H_{\mathrm{reg}}D^{-1},
\qquad
D=\operatorname{diag}(d_i),
\qquad
H_{\mathrm{reg}}=Q^{-*}Q_{\mathrm{sat}}Q^{-1}.
}
\tag{82}
$$

In particular,

$$
\boxed{
\begin{aligned}
\log\det Q_\Lambda
={}&
\log\det Q_{\mathrm{sat}}
-2\log|\det P\det Q|\\
&-2\sum_{j=1}^r(r-j+1)\log|a_j|.
\end{aligned}}
\tag{83}
$$

The actual module discrepancy is

$$
\boxed{
\operatorname{coker}A
\simeq\bigoplus_{i=1}^r\mathcal O/(d_i).
}
\tag{84}
$$

Along an analytic curve, \(d_i=z^{\nu_i}\) times a unit, and every inverse-exterior exponent is the sum of the corresponding largest \(\nu_i\). The missing derivative orders remain in (84).

### 9.4 The boundary connection and all its mixing terms

In the holomorphic frame of (82), the Chern connection is

$$
\boxed{
\Gamma
=
D H_{\mathrm{reg}}^{-1}\partial H_{\mathrm{reg}}D^{-1}
-D'D^{-1}.
}
\tag{85}
$$

The second term is the explicit logarithmic factor

$$
-\sum_j\operatorname{diag}(0,\ldots,0,1,\ldots,1)
\,\frac{\partial a_j}{a_j}.
$$

The first term retains every off-diagonal mixing entry, multiplied by its actual ratio \(d_i/d_j\).

On the complement of the divisor,

$$
\boxed{
\mathcal F_\Gamma
=
D\,\mathcal F_{H_{\mathrm{reg}}}\,D^{-1}.
}
\tag{86}
$$

The map \(D^{-1}\) is the exact isometry in (82), so the curvature norm in that metric is the norm of the regular curvature. It is bounded on compact regular-metric charts.

This Chern connection is not silently the real metric connection used for the heat derivative. In a given frame their difference is exactly

$$
\boxed{
\nabla^{\mathrm{Ch}}
-\left(d+\frac12G^{-1}dG\right)
=
\frac12G^{-1}(\partial G-\bar\partial G).
}
\tag{87}
$$

Equations (81)–(87) provide a finite parameter model with explicit weight factors, complete extension data, and a controlled regular remainder. They do not construct a Hodge filtration or a Frobenius action that is absent from the arithmetic comparison.

---

## 10. What this gives the original programme

The new control is uniform in the aspects that can be made uniform from the actual finite positive-source data:

* Every fixed original subquotient has the same complex logarithmic neighbourhood (5) and all-order mixed derivative bounds (9)–(10).
* All covariance scales and noncommuting source ranges have the exact filtration model (24)–(32), including every metric and action exterior exponent.
* The complete observed heat has the no-gap memory representation (35)–(42), and its comparison with the actual observed squared action is bounded by the original kernel rank in (45).
* Every proper rational testing family below the exact conductor degree bound is faithfully observed, with the original metric return (65)–(66), including repeated and colliding poles.
* Source-rank and observation-rank degenerations retain their full missing-value modules and additional minima in (75), (80), and (84).

For the original simple family, the bulk observed positive-heat comparison is now completed by (1)–(2). The joint-source positive spectral comparison is below the \(kq\) scale by (50)–(51). The kernel’s low proper-rational complexity is excluded by (3), uniformly over pole choices in its stated arithmetic domain.

The remaining scalar values are still

$$
\mathcal R\log\det(I_K^*G_NI_K),
$$

at its unresolved finer coefficient,

$$
\mathcal M^p
=
\mathcal R\log\det\!\left[
(Q_N^p)^{-1/2}H_N^p(Q_N^p)^{-1/2}
\right],
$$

and the actual native projected-current sign. Their complete maps are retained here; they are not replaced by the new saturated or weighted metrics.

I am not claiming a fresh executed numerical checker receipt or an arithmetic zero computation for these new proofs. The exact finite examples above are included to make the identities and limiting scales directly checkable.

**The finite-family result is now considerably closer to the kind of control you asked for: a common analytic domain, all mixed derivatives, explicit boundary weights, complete source and observation extensions, and uniform heat-memory bounds. The uncontrolled native quantity is no longer hidden inside an unspecified change of metric or disappearing source direction; it remains as the explicit original determinant or phase evaluated through those maps.**
