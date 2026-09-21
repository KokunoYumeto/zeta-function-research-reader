## The inverse-power theorem gives a quantitative reduction of the original observation complex

The main propagated identity is

$$
\boxed{
\mathcal R\log\det(I_K^*G_NI_K)
=
\mathcal R\log\det\!\left[
(\pi_rI_K)^*
(\pi_rG_N^{-1}\pi_r^*)^{-1}
(\pi_rI_K)
\right]
+o_{h,A}(kq).
}
\tag{1}
$$

Here \(\pi_r\) is an explicit quotient by the first \(r\) inverse powers, defined below. The right side retains the original kernel, period, source measure, and full polynomial relation. It removes the large inverse-power directions without changing the kernel’s \(kq\) coefficient.

At the same time, the removed observed sector carries the evaluated contribution

$$
\boxed{
\mathcal R\log\det H^B_{r,N}
=
\mathfrak C\,rq+o_{h,A}(rq),
\qquad
1.353893<\mathfrak C<1.354751.
}
\tag{2}
$$

That contribution is transferred between specified determinant factors; it is not added to the original total while its compensating factor is held fixed.

The reduction also turns inverse multiplication into **ordinary Taylor division between successive quotient spaces**, with explicit subexponential norm bounds. This supplies a controlled arithmetic action after the reduction, rather than an unsupported assertion that multiplication descends to a fixed quotient.

### Retained hypotheses and notation

Keep

$$
q=(k+1)^2,\qquad m=\dim K=8k-16,
$$

on the original simple-quartet and proved observation domain. Write

$$
E=\mathbb C[y]/(Q_k),\qquad M[p]=[yp],
$$

$$
\Lambda:E\longrightarrow B,\qquad K=\ker\Lambda,
$$

and retain the fixed original kernel frame \(I_K\). At cutoff \(N\),

$$
Q_{B,N}=(\Lambda G_N^{-1}\Lambda^*)^{-1},
\qquad
L_{B,N}=G_N^{-1}\Lambda^*Q_{B,N},
\qquad
P_{B,N}=L_{B,N}\Lambda.
$$

All coordinates use the original substitution \(S=k/2+iy\). A stored \(S\)-coefficient frame is carried to these coordinates by

$$
(T_c)_{ab}=\binom ba c^{\,b-a}i^a,\qquad c=k/2,
$$

with

$$
I_K^y=T_cI_K^S,\qquad G_N^S=T_c^*G_N^yT_c.
$$

Thus the phases are part of the coordinate map, not omitted from it.

Set

$$
U_rd=\sum_{j=1}^r d_j[y^{-j}],\qquad
V_r=\operatorname{im}U_r,\qquad
\Phi_r=\Lambda U_r,
$$

$$
H^E_{r,N}=U_r^*G_NU_r,\qquad
H^B_{r,N}=\Phi_r^*Q_{B,N}\Phi_r.
$$

I use the preceding theorem in the following form:

$$
\boxed{
a_{r,N}H^E_{r,N}\preceq H^B_{r,N}\preceq H^E_{r,N},
\qquad
a_{r,N}\ge e^{-\varepsilon_{k,r}},
}
\tag{IP}
$$

where

$$
\varepsilon_{k,r}
=
C_{h,A}(k+Jr)\log(q+Jr+2)=o(q)
$$

when

$$
r\log(q+2)=o(q).
$$

Its explicit finite lower factor can be used instead of the asymptotic expression. \(J\) remains the number of nonzero original conductor coefficients.

The algebraic conductor and its full-kernel inclusion are the original IK1–IK8 identities; the source was read at the pinned repository version `fe22dc1dd51c633e82f93b731cbb6ec96b11ed64`.  The coefficient limits continue to consume the stated monic-profile input, rather than an independently re-proved EIQ asymptotic. 

The finite arguments below apply more generally to any positive finite source and onto observation satisfying (IP).

---

## 1. The original kernel loses only a controlled angle determinant

Fix one cutoff temporarily and suppress \(N\). Put

$$
H_K=I_K^*GI_K,\qquad
\Gamma=I_K^*GU_r.
$$

Since \(I-P_B\) is the original orthogonal kernel projection,

$$
\boxed{
H^B_r=H^E_r-\Gamma^*H_K^{-1}\Gamma.
}
\tag{3}
$$

Now quotient the source by \(V_r\). The image of \(K\) remains injective because \(K\cap V_r=0\), as proved by the conductor theorem. Its attained metric is

$$
\boxed{
\widehat H_{K,r}
=
H_K-\Gamma(H^E_r)^{-1}\Gamma^*.
}
\tag{4}
$$

These two Schur complements have exactly the same nontrivial relative eigenvalues. Indeed, define

$$
T=H_K^{-1/2}\Gamma(H^E_r)^{-1/2}.
$$

Then

$$
H^B_r=(H^E_r)^{1/2}(I-T^*T)(H^E_r)^{1/2},
$$

$$
\widehat H_{K,r}=H_K^{1/2}(I-TT^*)H_K^{1/2}.
$$

Equation (IP) implies

$$
T^*T\preceq(1-a_{r,N})I.
$$

Therefore

$$
\boxed{
a_{r,N}H_K\preceq\widehat H_{K,r}\preceq H_K.
}
\tag{5}
$$

More importantly, the complete logarithmic loss is

$$
\boxed{
\begin{aligned}
\delta_{r,N}
&:=\log\det H^E_{r,N}-\log\det H^B_{r,N}\\
&=\log\det H_{K,N}-\log\det\widehat H_{K,r,N}\\
&=-\log\det(I-T^*T).
\end{aligned}
}
\tag{6}
$$

If \(\nu_{r,N}=\operatorname{rank}\Gamma\), only \(\nu_{r,N}\) eigenvalues contribute:

$$
\boxed{
0\le\delta_{r,N}
\le \nu_{r,N}\varepsilon_{k,r}
\le\min(m,r)\varepsilon_{k,r}.
}
\tag{7}
$$

The factor \(\min(m,r)\), rather than \(r\), matters when many inverse powers are retained. Because \(m=O(k)\),

$$
\boxed{
\delta_{r,N}=o_{h,A}(kq)
}
\tag{8}
$$

throughout the entire allowed regime \(r\log q=o(q)\), uniformly over the original cutoffs.

For the four signs,

$$
\boxed{
\left|
\mathcal R\log\det\widehat H_{K,r,N}
-\mathcal R\log\det H_{K,N}
\right|
\le2\min(m,r)\varepsilon_{k,r}.
}
\tag{9}
$$

Each endpoint loss belongs to the same interval
\([0,\min(m,r)\varepsilon_{k,r}]\); two occur with each sign. The factor two therefore retains the correlation of the four errors.

The estimate is sharp given only (IP). In an orthonormal space, take \(\nu\) unit vectors of \(V_r\) of the form

$$
\sqrt{1-a}\,e_j+\sqrt a\,f_j,
$$

where \(e_j\in K\) and \(f_j\perp K\), and put the remaining vectors perpendicular to \(K\). Then exactly \(\nu\) relative eigenvalues equal \(a\), and

$$
\delta=\nu\log(1/a).
$$

### Explicit quotient coordinates

No numerical nullspace choice is needed for \(E/V_r\). Define

$$
\boxed{
\pi_r[p]
=
\mathscr D^r\!\left(\operatorname{rem}_{Q_k}(y^rp)\right),
\qquad
\mathscr D^rf=
\frac{f-\operatorname{Tay}_{<r}f}{y^r}.
}
\tag{10}
$$

Its target is the coefficient space \(\mathcal P_{<q-r}\).

Multiplication by \(y\) is invertible modulo \(Q_k\), and

$$
M^rV_r=\mathcal P_{<r}.
$$

Consequently

$$
\ker\pi_r=V_r.
$$

The ordinary low-degree inclusion

$$
\iota_r:\mathcal P_{<q-r}\hookrightarrow E
$$

satisfies

$$
\pi_r\iota_r=I.
$$

The actual quotient metric is

$$
\boxed{
\overline G_{r,N}
=
(\pi_rG_N^{-1}\pi_r^*)^{-1}.
}
\tag{11}
$$

This is not the raw polynomial Gram on \(\mathcal P_{<q-r}\). It is the minimum over all original representatives after quotienting by the specified inverse-power space.

The image of the original kernel has frame

$$
\overline I_{K,r}=\pi_rI_K,
$$

and

$$
\overline I_{K,r}^*\overline G_{r,N}\overline I_{K,r}
=
\widehat H_{K,r,N}.
$$

Equations (8)–(11) prove the opening identity (1).

For example, one may take

$$
r_k=\left\lfloor\frac{q}{\log^2(q+2)}\right\rfloor.
$$

Then \(r_k\) is much larger than \(m\), but

$$
\delta_{r_k,N}
=
O_{h,A}\!\left(\frac{kq}{\log q}\right)
=o(kq).
$$

Thus considerably more than \(O(k)\) inverse directions can be removed while preserving the original kernel coefficient.

---

## 2. This is a chain-homotopy reduction, not merely a determinant comparison

Let

$$
W_r=\Lambda V_r\subset B.
$$

Choose a fixed algebraic quotient map

$$
\rho_r:B\longrightarrow B/W_r.
$$

It can be constructed from an actual nonzero \(r\times r\) minor of \(\Phi_r\): retain those pivot rows and subtract their exact interpolation from the remaining rows. The matrix is fixed as \(N\) varies.

There is an induced onto map

$$
\overline\Lambda_r:E/V_r\longrightarrow B/W_r,
\qquad
\overline\Lambda_r\pi_r=\rho_r\Lambda.
\tag{12}
$$

Its kernel is exactly \(\pi_rK\). The diagram

$$
\begin{array}{ccccccccc}
0&\to&V_r&\to&E&\xrightarrow{\pi_r}&E/V_r&\to&0\\
&&\downarrow{\Lambda|_{V_r}}&&\downarrow\Lambda&&
\downarrow\overline\Lambda_r\\
0&\to&W_r&\to&B&\xrightarrow{\rho_r}&B/W_r&\to&0
\end{array}
\tag{13}
$$

has exact rows and an isomorphism on the left.

The attained target metric is

$$
\overline Q_{r,N}
=
(\rho_rQ_{B,N}^{-1}\rho_r^*)^{-1}.
$$

Direct substitution proves

$$
\boxed{
\overline Q_{r,N}
=
\left(
\overline\Lambda_r\overline G_{r,N}^{-1}
\overline\Lambda_r^*
\right)^{-1}.
}
\tag{14}
$$

Thus either order of the two complete quotient minima gives the same metric.

### An explicit contracting homotopy

Define

$$
\boxed{
h_{r,N}
=
U_r(H^B_{r,N})^{-1}\Phi_r^*Q_{B,N}:B\to E.
}
\tag{15}
$$

Then

$$
\Lambda h_{r,N}
=
\Phi_r(H^B_{r,N})^{-1}\Phi_r^*Q_{B,N}
$$

is the \(Q_{B,N}\)-orthogonal projection onto \(W_r\), whereas \(h_{r,N}\Lambda\) is the projection onto \(V_r\) along

$$
\Lambda^{-1}(W_r^{\perp_{Q_{B,N}}}).
$$

The latter is generally oblique, not orthogonal.

Equation (IP) gives

$$
\boxed{
\|h_{r,N}\|_{Q_{B,N}\to G_N}\le a_{r,N}^{-1/2}
\le e^{\varepsilon_{k,r}/2}.
}
\tag{16}
$$

For the finite cochain complex

$$
\mathcal C_N^\bullet=[E\xrightarrow{\Lambda}B],
$$

the two projections

$$
I-h_{r,N}\Lambda,\qquad I-\Lambda h_{r,N}
$$

give its complementary subcomplex, and

$$
I-jp=dh+hd.
\tag{17}
$$

Here \(p=(\pi_r,\rho_r)\); an explicit chain section \(j\) is obtained by composing the minimum section of \(\pi_r\) with \(I-h\Lambda\), and the minimum section of \(\rho_r\) in degree one.

This proves a chain-homotopy equivalence

$$
\boxed{
[E\to B]\simeq[E/V_r\to B/W_r].
}
\tag{18}
$$

Its degree-zero cohomology remains the original observation kernel \(K\). This is a statement about this finite observation complex, not an unconstructed identification with the entire infinite theta complex. The standard meanings of “acyclic” and “quasi-isomorphism” are as in the Stacks Project; the homotopy itself is explicitly given in (15)–(17). ([The Stacks Project][1])

### The full polynomial-source relations survive

Let

$$
J_N:\mathcal P_N\to E,\qquad L_N:E\to\mathcal P_N
$$

be the actual remainder map and its original minimum section. The physical polynomial lift of the contracting homotopy is

$$
\widetilde h_{r,N}=L_Nh_{r,N}.
$$

Its range is the actual source subspace \(L_NV_r\), and

$$
\|\widetilde h_{r,N}\|=\|h_{r,N}\|.
$$

The complete relation space

$$
Q_k\mathcal P_{N-q}
$$

is untouched: \(J_N\) kills it, so the contraction vanishes on it. It is also orthogonal to \(L_NV_r\). Hence the same reduction lifts to

$$
[\mathcal P_N\xrightarrow{\Lambda J_N}B]
$$

without deleting any original polynomial relation.

---

## 3. The determinant contribution moves with a known coefficient

There are two different operations.

If only the target is quotiented by \(W_r\), the new kernel is

$$
K_r=K+V_r.
$$

In the fixed frame \([I_K,U_r]\),

$$
\boxed{
\det\bigl([I_K,U_r]^*G_N[I_K,U_r]\bigr)
=
\det H_{K,N}\det H^B_{r,N}.
}
\tag{19}
$$

This is the Schur complement (3).

If both source and target are quotiented, as in (13), the kernel remains isomorphic to \(K\), with the controlled metric change (6).

For the target-only quotient, choose one fixed complement to \(W_r\) in \(B\). Its coefficient-frame determinant is independent of \(N\), so

$$
\boxed{
\mathcal R\log\det\overline Q_{r,N}
=
\mathcal R\log\det Q_{B,N}
-
\mathcal R\log\det H^B_{r,N}.
}
\tag{20}
$$

Suppose \(r/k\to\lambda\). The preceding theorem therefore gives the exact leading redistribution

$$
\boxed{
\begin{aligned}
\frac{\mathcal R\log\det G_{K_r,N}
-\mathcal R\log\det G_{K,N}}{kq}
&\longrightarrow\lambda\mathfrak C,\\
\frac{\mathcal R\log\det\overline Q_{r,N}
-\mathcal R\log\det Q_{B,N}}{kq}
&\longrightarrow-\lambda\mathfrak C.
\end{aligned}
}
\tag{21}
$$

The two contributions cancel in the total determinant identity. For \(r=k\), the transferred coefficient is precisely \(\mathfrak C\).

Meanwhile the relative squared-volume cost of the contractible block

$$
V_r\xrightarrow{\Lambda}W_r
$$

is

$$
\log\det H^E_{r,N}-\log\det H^B_{r,N}
=\delta_{r,N}=o(kq).
$$

Thus the large, evaluated \(+\mathfrak C rq\) term occurs in both its source and observed volumes; their relative distortion is subleading.

---

## 4. The arithmetic inverse becomes bounded Taylor division on the reduced spaces

The quotient in (18) is not automatically stable under multiplication by \(M\). The following gives the exact replacement.

Let

$$
\mathscr D^sp=
\frac{p-\operatorname{Tay}_{<s}p}{y^s}.
$$

For \(x\in E\), write the actual minimum representative as

$$
L_Nx
=
\sum_{j=0}^{s-1}c_j(x)y^j+y^s\mathscr D^sL_Nx.
$$

Then

$$
\boxed{
M^{-s}
=
J_N\mathscr D^sL_N+U_sF_{s,N},
\qquad
(F_{s,N}x)_n=c_{s-n}(x).
}
\tag{22}
$$

These \(c_j\) are divided Taylor coefficients of \(L_Nx\), not evaluation functionals asserted to descend directly to \(E\).

Retain

$$
a_N^\Gamma=
\sqrt{n_N(n_N+1)}(1+\sqrt{N+1}),
\qquad
n_N=\left\lceil\frac{N+2}{2}\right\rceil.
$$

The supplied Gamma division estimate and native comparison give

$$
\boxed{
\|J_N\mathscr D^sL_N\|
\le
\mathfrak B_{s,N}
:=
\sqrt{\frac{u_k}{\ell_{k,N}}}\,(a_N^\Gamma)^s.
}
\tag{23}
$$

Only one native/Gamma comparison is used; it is not multiplied \(s\) times. In particular,

$$
\log^+\mathfrak B_{s,N}
=
O_h(k+s\log(q+2))
$$

on the relevant degree range. The retained division estimate and its mass convention are S11–S16 of the supplied proof. 

### Exact degree-changing inverse maps

For \(r+s\le q\), multiplication by \(M^{-s}\) induces

$$
\mathcal I_{r,s}:E/V_r\longrightarrow E/V_{r+s},
\qquad
[x]\longmapsto[M^{-s}x].
$$

It is well-defined because \(M^{-s}V_r\subset V_{r+s}\).

In the canonical polynomial coordinates (10),

$$
\boxed{
\mathcal I_{r,s}p=\mathscr D^sp.
}
\tag{24}
$$

Indeed, for \(\deg p<q-r\), the polynomial \(y^rp\) already has degree below \(q\). Applying (10) to \(M^{-s}p\) therefore drops exactly the first \(s\) coefficients of \(p\).

The whole sequence is

$$
\boxed{
0\longrightarrow\mathcal P_{<s}
\longrightarrow E/V_r
\xrightarrow{\mathcal I_{r,s}}E/V_{r+s}
\longrightarrow0.
}
\tag{25}
$$

To check the kernel, multiply by \(M^s\):

$$
M^sV_{r+s}=V_r+\mathcal P_{<s}.
$$

The sum is direct because multiplication by \(M^r\) sends its two parts to disjoint monomial ranges of degree below \(q\).

Equation (22) gives the original-metric bound

$$
\boxed{
\|\mathcal I_{r,s}\|_{\overline G_{r,N}\to\overline G_{r+s,N}}
\le\mathfrak B_{s,N}.
}
\tag{26}
$$

The large rank-\(s\) term in (22) lands in \(V_s\subset V_{r+s}\) and vanishes in this specified quotient.

These maps compose exactly:

$$
\mathcal I_{r+s,t}\mathcal I_{r,s}
=
\mathcal I_{r,s+t}.
\tag{27}
$$

### The observation retains a complete memory term

Let \(\overline L_{r,N}\) be the minimum section of \(\overline\Lambda_r\). Define the observed inverse-step map

$$
\mathcal B_{r,s,N}
=
\overline\Lambda_{r+s}
\mathcal I_{r,s}\overline L_{r,N}.
$$

Then

$$
\boxed{\|\mathcal B_{r,s,N}\|\le\mathfrak B_{s,N}.}
\tag{28}
$$

It is not asserted to be the inverse of an independently compressed observed multiplication operator.

Let \(\overline P^K_{r,N}\) be the projection onto \(\ker\overline\Lambda_r\). The full action identity is

$$
\boxed{
\overline\Lambda_{r+s}\mathcal I_{r,s}
=
\mathcal B_{r,s,N}\overline\Lambda_r
+
\overline\Lambda_{r+s}\mathcal I_{r,s}\overline P^K_{r,N}.
}
\tag{29}
$$

The second term is the retained kernel leakage, with norm at most \(\mathfrak B_{s,N}\).

Likewise,

$$
\boxed{
\begin{aligned}
\mathcal B_{r,s+t,N}
-\mathcal B_{r+s,t,N}\mathcal B_{r,s,N}
={}&
\overline\Lambda_{r+s+t}\mathcal I_{r+s,t}
\overline P^K_{r+s,N}
\mathcal I_{r,s}\overline L_{r,N}.
\end{aligned}
}
\tag{30}
$$

Its rank is at most \(m\), and its norm is at most

$$
\mathfrak B_{t,N}\mathfrak B_{s,N}.
$$

Thus the observation’s failure to compose is not discarded; it is a specified, bounded kernel-feedback map.

For the original kernel itself, (22) gives the particularly direct identity

$$
\boxed{
\rho_{r+s}\Lambda M^{-s}I_K
=
\rho_{r+s}\Lambda J_N\mathscr D^sL_NI_K,
}
\tag{31}
$$

whose norm, from \(H_{K,N}\) to the attained target metric, is at most \(\mathfrak B_{s,N}\).

The full inverse has norm of order

$$
\exp[q\log(q/k)+O_h(q)].
$$

After the specified quotient, the actual kernel-to-observation inverse map has norm \(\exp(o(q))\) whenever \(s\log q=o(q)\).

### A full shift-and-minimize realization of the original kernel

There is a useful version involving only original polynomial source Grams.

Let \(r\log q=o(q)\). In \(\mathcal P_{N+r}\), form the complete relation matrix whose columns are

$$
1,y,\ldots,y^{r-1},
\qquad
Q_k,yQ_k,\ldots,y^{N+r-q}Q_k.
$$

Call it \(R_{r,N}\). Let \(E_{r,N}\) contain the coefficient columns of \(y^rI_K\), using the original degree-below-\(q\) representatives.

With the full source Gram \(H_{N+r}^{\mathrm{src}}\), define

$$
\boxed{
\begin{aligned}
\mathcal H^{\mathrm{shift}}_{r,N}
={}&E_{r,N}^*H_{N+r}^{\mathrm{src}}E_{r,N}\\
&-E_{r,N}^*H_{N+r}^{\mathrm{src}}R_{r,N}
(R_{r,N}^*H_{N+r}^{\mathrm{src}}R_{r,N})^{-1}
R_{r,N}^*H_{N+r}^{\mathrm{src}}E_{r,N}.
\end{aligned}
}
\tag{32}
$$

Every inverse is of a complete positive Gram. Both the low-polynomial directions and all shifted \(Q_k\)-relations remain.

Multiplication by \(y^r\) gives the exact isomorphism

$$
E/V_r\longrightarrow E/\mathcal P_{<r}.
$$

The source cutoff is \(N\); the target cutoff is \(N+r\).

A forward norm bound is

$$
\mathfrak A_{r,N}
=
\prod_{j=0}^{r-1}
C_{\mathrm{mult}}(h)
\left[2(N+j)+\lfloor k/3\rfloor\right].
$$

The inverse bound is \(\mathfrak B_{r,N+r}\). Indeed, multiply a minimum source representative by \(y^r\) for the forward estimate; for the inverse, apply \(\mathscr D^r\) to a complete target representative. Its discarded Taylor polynomial is precisely an allowed target relation.

Consequently,

$$
\boxed{
\mathfrak B_{r,N+r}^{-2}\widehat H_{K,r,N}
\preceq
\mathcal H^{\mathrm{shift}}_{r,N}
\preceq
\mathfrak A_{r,N}^{2}\widehat H_{K,r,N}.
}
\tag{33}
$$

Since

$$
\log^+\mathfrak A_{r,N}
+\log^+\mathfrak B_{r,N+r}
=
O_h(k+r\log q),
$$

equations (7) and (33) prove

$$
\boxed{
\mathcal R\log\det(I_K^*G_NI_K)
=
\mathcal R\log\det\mathcal H^{\mathrm{shift}}_{r,N}
+o_{h,A}(kq).
}
\tag{34}
$$

Equation (34) is a new explicit polynomial-source target for the remaining kernel coefficient. Its four target cutoffs are \(N+r\); they have not been relabelled as the old cutoffs.

---

## 5. The late heat is localized in the removed observed sector

The source identifies

$$
u=-Q_k(0)[y^{-1}]
$$

as the surviving late-heat line and proves, on its finite guard,

$$
\|P_{\min,N}-P_{u,N}\|\le\eta_N,
\qquad
\eta_N=\frac{D_N}{E_N-D_N}.
$$

The remaining singular values are at least \(D_N^{-1}\). These are the original LS1–LS5 statements, with the original metric.

Let

$$
W^E_{r,N}=P_{B,N}V_r,
$$

and let \(P_{W,r,N}\) be its original-metric orthogonal projection:

$$
P_{W,r,N}
=
P_{B,N}U_r(H^B_{r,N})^{-1}U_r^*G_NP_{B,N}.
$$

Then

$$
P^{\mathrm{rem}}_{r,N}
=
P_{B,N}-P_{W,r,N}
$$

is the projection onto \((K+V_r)^{\perp_{G_N}}\).

Since \(u\in V_1\subset V_r\),

$$
P^{\mathrm{rem}}_{r,N}u=0.
$$

If \(a_N\) is the unit smallest right singular vector,

$$
\|P^{\mathrm{rem}}_{r,N}a_N\|^2\le\eta_N^2.
$$

Therefore

$$
\boxed{
0\le
\operatorname{Tr}\!\left(
P^{\mathrm{rem}}_{r,N}e^{-\tau M^\dagger M}
\right)
\le
\eta_N^2e^{-\tau s_{\min,N}^2}
+(q-1)e^{-\tau/D_N^2}.
}
\tag{35}
$$

The error is quadratic in the line-angle bound here because the residual projection kills the reference line exactly.

The preceding inverse-power theorem gives

$$
\theta_N=
\frac{\|P_{B,N}u\|^2}{\|u\|^2}
\ge e^{-O_{h,A}(k\log q)}.
$$

Meanwhile

$$
\eta_N=\exp[-q\log(q/k)+O_h(q)].
$$

It follows that, at the same common late time

$$
\tau_k^*
=
\exp\left\{
2q\left[\log(q/k)-1-\frac{I(\delta,\gamma)}2\right]
\right\},
$$

the original measured heat is asymptotically entirely carried by \(W^E_{r,N}\):

$$
\boxed{
\frac{
\operatorname{Tr}(P_{W,r,N}e^{-\tau_k^*M^\dagger M})
}{
\operatorname{Tr}(P_{B,N}e^{-\tau_k^*M^\dagger M})
}
\longrightarrow1.
}
\tag{36}
$$

For the four-cutoff return, the residual contribution obeys

$$
\boxed{
\limsup_{k\to\infty}
\frac{
\log\left|
\mathcal R\operatorname{Tr}
(P^{\mathrm{rem}}_{r,N}e^{-\tau_k^*M^\dagger M})
\right|
}{
q\log(q/k)
}
\le-2,
}
\tag{37}
$$

with \(\log0=-\infty\).

Thus the positive late-heat event from the preceding theorem is located in a specific contractible observed sector. Its determinant contribution is already accounted for by (19)–(21).

### The remaining positive square has a finite gap

Let \(S_{r,N}:E/V_r\to E\) be the original minimum section of \(\pi_r\), with image \(V_r^\perp\). For \(x\perp V_r\),

$$
x=(I-P_{V_r})M^{-1}Mx
=(I-P_{V_r})J_N\mathscr DL_NMx.
$$

Hence

$$
\|Mx\|\ge D_N^{-1}\|x\|.
$$

The full-output positive operator therefore satisfies

$$
\boxed{
S_{r,N}^\dagger M^\dagger MS_{r,N}
\succeq D_N^{-2}I.
}
\tag{38}
$$

This is the positive square of the rectangular map \(MS_{r,N}\). It is not identified with either the square of a compressed endomorphism or the compression of its exponential.

### Applying the original arithmetic action preserves the kernel coefficient

Put

$$
Z_{r,N}=(I-P_{V_r,N})I_K,
\qquad
\mathcal E^{(s)}_{K,r,N}
=
(M^sZ_{r,N})^*G_N(M^sZ_{r,N}),
$$

where \(1\le s\le r\).

Equation (22) gives

$$
\|M^sx\|\ge\mathfrak B_{s,N}^{-1}\|x\|,
\qquad x\perp V_r.
$$

For the upper determinant bound, the rank-one relation \(M=C_N+R_N\) implies

$$
\sigma_j(M)\le B_hq\quad(j\ge2),\qquad
\sigma_1(M)\le\epsilon_N+B_hq.
$$

Exterior submultiplicativity therefore gives

$$
\boxed{
\begin{aligned}
-2m\log\mathfrak B_{s,N}
\le{}&
\log\frac{\det\mathcal E^{(s)}_{K,r,N}}
{\det\widehat H_{K,r,N}}\\
\le{}&
2s\log(\epsilon_N+B_hq)
+2s(m-1)\log(B_hq).
\end{aligned}
}
\tag{39}
$$

Only one large singular value of \(M\) enters the exterior bound; it is not charged independently in all \(m\) directions.

Using the retained \(\log\epsilon_N=O_h(q)\), for \(s=o(k)\),

$$
\boxed{
\mathcal R\log\det\mathcal E^{(s)}_{K,r,N}
=
\mathcal R\log\det(I_K^*G_NI_K)+o_{h,A}(kq).
}
\tag{40}
$$

The kernel coefficient is therefore preserved both by the quantified inverse-sector quotient and by applying these powers of the original arithmetic action to its minimum representatives.

---

## 6. Two existing programme terms can now be sharpened

### The eigenclass angle term in NP19 is \(o(q)\)

For a conductor-detected original eigenclass \(v_\lambda\), the preceding theorem gives

$$
\beta_N(\lambda)
=
\frac{\|\Lambda v_\lambda\|_{Q_{B,N}}^2}
{\|v_\lambda\|_{G_N}^2}
\ge e^{-C_{h,A}k\log(q+2)}.
$$

Therefore

$$
\boxed{
|\mathcal R\log\beta_N(\lambda)|
\le2C_{h,A}k\log(q+2)=o(q).
}
\tag{41}
$$

This closes the leading-order uncertainty in NP19’s displayed canonical observation-angle correction on the conductor-detected eigenline domain. The source’s complete output-stack identity is NP18; it retains that angle rather than removing it by observability alone.

In fact, for any depth \(d=d(k)\) used identically at all four cutoffs,

$$
\|\mathcal O_dv_\lambda\|^2
=
\left(\sum_{j=0}^{d}|\lambda|^{2j}\right)
\|\Lambda v_\lambda\|^2.
$$

The entire geometric factor cancels under \(\mathcal R\), even when \(d\) grows. Thus

$$
\boxed{
\mathcal R\log\|\mathcal O_dv_\lambda\|^2
=
\mathcal R\log\|v_\lambda\|_{G_N}^2
+O_{h,A}(k\log q).
}
\tag{42}
$$

For the unchanged cardinal eigenclass of the preceding calculation, the \(q\)-coefficient is therefore \(\mathfrak C\).

The physical class must remain fixed as \(N\) varies; separate unit normalization at each cutoff would change this statement. Equations (41)–(42) concern squared norms, not the sign of the different complex product \(\Re(\overline zw)\).

### The full inverse-power current has an \(O(k)\)-dimensional receiver

The orthogonal decomposition

$$
E=K\oplus W^E_{r,N}\oplus(K+V_r)^\perp
$$

has the exact block-diagonal metric

$$
H_{K,N}\oplus H^B_{r,N}\oplus\overline Q_{r,N}
$$

in the corresponding minimum-section frame.

For \(x=U_rd\), its last component is zero, and its first two coordinates are

$$
\kappa=H_K^{-1}\Gamma d,\qquad d.
$$

Let \(A\) be the original arithmetic action, and retain its actual blocks in this frame. Then the original pair is exactly

$$
\boxed{
z=\kappa^*H_KA_{K,W}d,
\qquad
w=d^*H^B_rA_{W,K}\kappa.
}
\tag{43}
$$

Thus the current on the entire inverse-power sector is computed in dimension \(m+r\), with both cross blocks and their phases retained. For \(r=k\), this is \(9k-16\), rather than \(q=(k+1)^2\).

Higher powers require the full return through the third block. For example,

$$
P_{K+V_r}A^2P_{K+V_r}
=
(P_{K+V_r}AP_{K+V_r})^2
+
P_{K+V_r}AP_{\mathrm{rem}}AP_{K+V_r}.
\tag{44}
$$

The last term is not discarded. This is the same distinction enforced by the full moving-section action formula M16 in the supplied manuscript. 

---

## 7. The reduction commutes with the complete mixed-source covariance

The general-family source supplies the actual normal Gram and value map

$$
H_Z,\qquad F_Z,\qquad
\ker H_Z\subseteq\ker F_Z,
$$

and

$$
\Omega_N=F_ZH_Z^+F_Z^*.
$$

Its source-activation metric is

$$
G_N(t)=(G_N^{-1}+t\Omega_N)^{-1}.
$$

These maps contain the full cross Gram between the scalar source and the added tensor section. 

Quotienting by the fixed \(V_r\) gives, exactly,

$$
\boxed{
\overline G_{r,N}(t)
=
\left[
\overline G_{r,N}(0)^{-1}
+t\,\pi_r\Omega_N\pi_r^*
\right]^{-1}.
}
\tag{45}
$$

The new normal value map is simply \(\pi_rF_Z\), with the same full \(H_Z^+\). The compatibility of its kernel follows from the original one.

Let

$$
\mathcal C_N=G_N^{1/2}\Omega_NG_N^{1/2}.
$$

The covariance on \(E/V_r\), in its initial metric, is a compression

$$
\overline{\mathcal C}_{r,N}=S_r\mathcal C_NS_r^*,
\qquad S_rS_r^*=I_{q-r}.
$$

Interlacing gives

$$
\boxed{
0\le
\operatorname{Tr}\frac{t\mathcal C_N}{I+t\mathcal C_N}
-
\operatorname{Tr}\frac{t\overline{\mathcal C}_{r,N}}
{I+t\overline{\mathcal C}_{r,N}}
\le r,
}
\tag{46}
$$

and

$$
\boxed{
0\le
\log\det(I+t\mathcal C_N)
-\log\det(I+t\overline{\mathcal C}_{r,N})
\le r\log(1+t\|\mathcal C_N\|).
}
\tag{47}
$$

Consequently the supplied effective-dimension law

$$
q^{-1}\operatorname{Tr}
\frac{t_k(b)\mathcal C_N}{I+t_k(b)\mathcal C_N}
\longrightarrow(1-b)_+,
\qquad
t_k(b)=e^{-2bq\log(q/k)},
$$

survives this quotient, with an additional finite error at most \(r/q\). The original law and its precise normalization are C6–C10. 

Likewise, the source’s bound

$$
\log(1+\|\mathcal C_N\|)
=
O_h(q\log(q/k))
$$

and \(r\log q=o(q)\) show that the quotient changes its full metric cost by \(o(q^2)\). Thus the known weak-activation return remains

$$
\boxed{
\mathcal R\log\det
(I+e^{-2\theta q}\overline{\mathcal C}_{r,N})
=
C_Bq^2+o_h(q^2).
}
\tag{48}
$$

The same conclusion holds after the additional original observation quotient, whose codimension contributes another \(m=o(q/\log q)\). This uses the supplied H18–H23 domain, not a new evaluation of its original profile. 

At the finer kernel scale, there remains an exact angle correction. Define \(\delta_{r,N}(t)\) by (6), now using \(G_N(t)\). If

$$
F_K(t)=\log\det H_K(0)-\log\det H_K(t),
$$

and \(\overline F_K\) is the corresponding deflated quantity, then

$$
\boxed{
\overline F_K(t)
=
F_K(t)+\delta_{r,N}(t)-\delta_{r,N}(0).
}
\tag{49}
$$

The canonical bound controls \(\delta_{r,N}(0)\). It does not assign \(\delta_{r,N}(t)\) after a large source change.

For a varying period, rather than a fixed-packet source activation, the quotient map itself moves. Its complete covariance derivative is

$$
\boxed{
\begin{aligned}
\partial(\pi_rG^{-1}\pi_r^*)
={}&
(\partial\pi_r)G^{-1}\pi_r^*
+\pi_rG^{-1}(\partial\pi_r)^*\\
&-\pi_rG^{-1}(\partial G)G^{-1}\pi_r^*.
\end{aligned}
}
\tag{50}
$$

Thus period derivatives do not lose the two quotient-frame terms.

---

## 8. The proper-source comparison retains its entire target minimum

The independent proper-source matrix remains

$$
H_e^p
=
F_{R,e}^*\mathcal D_e^pF_{R,e}
-
F_{R,e}^*\mathcal D_e^pJ_*
(J_*^*\mathcal D_e^pJ_*)^{-1}
J_*^*\mathcal D_e^pF_{R,e}.
\tag{51}
$$

Here \(e\) indexes its four original endpoints. The full \(J_*\), the independent source metric \(Q_e^p\), and the original degree shifts remain. These are precisely the NP30–NP31 objects.

Let their common input dimension be \(r_p=O(k)\). Use the ordered inverse-power frame of length \(r_p\) only as an explicit comparison space, at

$$
\widehat N_e=q-1,\ q,\ 2q-1,\ 2q
$$

respectively. This does not identify \(\widehat N_e\) with the proper-source degrees.

There are exact maps

$$
U_{r_p}d\longmapsto d
$$

into the original proper-source coordinate frame, and

$$
\Phi_{r_p}d\longmapsto[F_{R,e}d]\pmod{\operatorname{im}J_*}
$$

into the full target quotient. The second is well-defined because \(\Phi_{r_p}\) is injective. It makes the corresponding source–observation square commute.

Taking determinants in that common coefficient frame gives

$$
\boxed{
\begin{aligned}
\mathcal M^p
={}&
\mathcal R_e
\left[
\log\frac{\det H_e^p}{\det H^B_{r_p,\widehat N_e}}
-
\log\frac{\det Q_e^p}{\det H^E_{r_p,\widehat N_e}}
\right]\\
&-\mathcal R\delta_{r_p,N}.
\end{aligned}
}
\tag{52}
$$

Since \(\mathcal R\delta_{r_p,N}=o(kq)\),

$$
\boxed{
\mathcal M^p
=
\mathcal R_e
\left[
\log\frac{\det H_e^p}{\det H^B_{r_p,\widehat N_e}}
-
\log\frac{\det Q_e^p}{\det H^E_{r_p,\widehat N_e}}
\right]
+o(kq).
}
\tag{53}
$$

This is the exact propagation into the proper-source branch. The common evaluated inverse-power coefficient cancels between its source and target reference volumes. The remaining two comparison determinants contain the actual proper-source geometry and its full target Schur term; they have not been assigned values by the cancellation.

---

## What has changed in the programme

The inverse-power result now supplies more than another nonvanishing theorem.

The original observation kernel has a **cohomology-preserving, quantitatively equivalent quotient realization** at the \(kq\) scale, equations (1), (18), and (34). The known inverse-sector coefficient is allocated exactly between kernel augmentation and residual observation, equation (21). The previously unresolved canonical eigenclass angle is now \(o(q)\) on the conductor-detected domain, equation (41).

The arithmetic inverse on the reduced spaces is the explicit Taylor-division sequence (24)–(27), with the complete observed feedback term (30). The late-heat event is isolated in the removed observed sector with the stronger residual bound (35). The large mixed-source covariance law survives, while its finer kernel correction is identified explicitly by (49).

The remaining fixed-kernel coefficient may therefore be calculated from the full shifted-source matrix (32), with a proved \(o(kq)\) error. The independent proper-source coefficient is the exact comparison in (53). Neither step requires replacing the original kernel by a generically oriented subspace or deleting a target-invariant direction.

No executable verification completed in this turn: the runtime calls timed out. The added statements above are written proofs from the preceding theorem and the cited source identities; no repository files were changed.

### References

National Institute of Standards and Technology. (n.d.). *Digital Library of Mathematical Functions*, §18.23, Meixner–Pollaczek generating functions. ([DLMF][2])

*Original-metric heat transitions and complete mixed-family control*. (2026, September 20). [User-supplied research manuscript]. The imported profile, complete mixed minimum, and covariance-response domains are retained above. 

Split-Zero research programme. (2026, September 21). *The original conductor detects a full inverse-power space* [Research manuscript, IK1–IK12]. *Zeta-function research reader*, inspected at commit `fe22dc1dd51c633e82f93b731cbb6ec96b11ed64`.

The Stacks Project Authors. (n.d.). *Definition 12.13.10: Acyclic complexes and quasi-isomorphisms* (Tag 0115). The finite contraction used here is given explicitly in equations (15)–(17). ([The Stacks Project][1])

[1]: https://stacks.math.columbia.edu/tag/0115 "https://stacks.math.columbia.edu/tag/0115"
[2]: https://dlmf.nist.gov/18.23 "https://dlmf.nist.gov/18.23"
