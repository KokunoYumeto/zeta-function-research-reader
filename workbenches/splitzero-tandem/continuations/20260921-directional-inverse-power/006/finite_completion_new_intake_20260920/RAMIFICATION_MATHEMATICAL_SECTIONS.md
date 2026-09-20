# Received ramification calculation: mathematical sections 1–5

Mathematical extract of the supplied AI-generated calculation of 20 September 2026. No human author name was supplied. The original received SHA-256 is `259b9f7bcf84b6885f3e88a2ba045825d02d0e9e11e7df66c84ffe3750e2eae3`. Only the conversational opening and publication-status paragraph are omitted. The extract has its own manifest hash; it is not the original byte sequence. The independent accepted proof and corrections are GB1–22 in the cumulative article.

## 1. The missing boundary is now an explicit finite cover

Retain the original output coordinates \(Y=(A,B,C,D)\) and the unchanged coefficient convention

$$
F_Y(r)=Ar^4+r^3+Br^2+Cr+D.
$$

For a finite selected root, the normalized factor equation is

$$
a^2F_Y'(r)=1.
$$

Introduce the reciprocal factor coordinate

$$
\sigma=\frac1a.
$$

Instead of removing the points where \(F_Y'(r)=0\), retain the equations

$$
F_Y(r)=0,\qquad \sigma^2=F_Y'(r).
$$

They solve polynomially for the last two target coefficients:

$$
\boxed{
\begin{aligned}
C&=\sigma^2-4Ar^3-3r^2-2Br,\\
D&=3Ar^4+2r^3+Br^2-r\sigma^2.
\end{aligned}}
\tag{1}
$$

Thus the finite-root chart of the completion is affine four-space with coordinates \((A,B,r,\sigma)\). Its coefficient map \(\widehat\pi\) has the exact Jacobian

$$
\boxed{\det D\widehat\pi=2\sigma^3.}
\tag{2}
$$

The return to the original FC44 source coordinates is explicit on \(\sigma\ne0\):

$$
\boxed{
\begin{aligned}
a&=\sigma^{-1},\\
y&=-r-i\sigma,\\
z&=A\sigma^3+3i\sigma^2+2r\sigma,\\
w&=7ir^2\sigma+(B-17r+Ar^2)\sigma^2
      -13i\sigma^3-2A\sigma^4.
\end{aligned}}
\tag{3}
$$

Writing this map as \(X\), the identities are

$$
P_i\circ X=\widehat\pi,\qquad
\det DX=-\sigma^3,\qquad
\det DP_i=-2.
\tag{4}
$$

Consequently, equation (2) does identify a critical locus, but its points occur where the original coordinate \(a\) escapes to infinity. Equations (3)–(4) specify the change of domain and its exact Jacobian.

The root at infinity requires a second chart:

$$
G_Y(\tau)=A+\tau+B\tau^2+C\tau^3+D\tau^4,
\qquad
G_Y(\tau)=0,\qquad
\theta^2=-G_Y'(\tau).
$$

The full transition is

$$
\tau=r^{-1},\qquad \theta=\sigma/r.
$$

At \(\tau=0\), the equations give

$$
A=0,\qquad \theta=\pm i.
$$

Both factor signs are therefore present. The original factor is recovered by

$$
a=\frac{\tau}{\theta},\qquad b=-\frac1\theta,
$$

so the previously omitted \(b=-i\) state is precisely \(\theta=-i\).

Let \(Z\) denote the space obtained by gluing these charts. The resulting theorem is

$$
\boxed{\pi:Z\longrightarrow\mathbb A^4_Y
\text{ is smooth-source, finite, flat, and of degree }8.}
\tag{5}
$$

Finiteness follows through the proper projective root incidence with finite fibres; the explicit free algebra below proves flatness over the entire coefficient space. This is the standard finite-morphism criterion applied to the displayed incidence, not an assumption that a constant affine Jacobian implies properness (The Stacks Project Authors, 2026, Tag 02OG).

There are two separate, disjoint boundary divisors:

$$
R=\{\sigma=0\}\simeq\mathbb A^3_{A,B,r},
\qquad
E_-=\{\tau=0,\theta=-i\}\simeq\mathbb A^3_{B,C,D}.
$$

The exact open complements are

$$
\boxed{
\mathfrak X=Z\setminus R,\qquad
\mathbb A^4_{\text{original source}}=Z\setminus(R\cup E_-).
}
\tag{6}
$$

Here \(E_-\) maps isomorphically and unramifiedly onto \(A=0\). In contrast, the ramification divisor is exactly \(3R\), and its image is the quartic discriminant hypersurface

$$
\Delta(Y)=0.
$$

Moreover, \(R\to\{\Delta=0\}\) is its normalization. Restoring the missing infinity sign and restoring a repeated selected root are therefore different geometric operations, with different local derivatives.

The completion also records the difference topologically:

$$
H_2(Z;\mathbb Z)\cong\mathbb Z^2,\qquad
H_j(Z;\mathbb Z)=0\quad(j>0,\ j\ne2),
$$

and

$$
\operatorname{Pic}(Z)
=\operatorname{Cl}(Z)
=\mathbb Z[R]\oplus\mathbb Z[E_-].
$$

These follow from the open complement \(\mathbb C^4\) and the two disjoint closed copies of \(\mathbb C^3\); they concern this finite-dimensional variety, not the programme’s theta-source topology.

## 2. All eight dimensions survive in an explicit algebra

The finite cover has a global free rank-eight algebra over \(\mathbb C[A,B,C,D]\). A basis that remains valid at both \(A=0\) and \(\Delta=0\) is

$$
\begin{aligned}
(e_0,e_1,e_2,e_3)
&=(1,\ Ar,\ Ar^2+r,\ Ar^3+r^2+Br),\\
(o_0,o_1,o_2,o_3)
&=\sigma\bigl(A,\ Ar+1,\ Ar^2+r+B,\
                    Ar^3+r^2+Br+C\bigr).
\end{aligned}
\tag{7}
$$

The apparent use of the finite coordinate \(r\) does not exclude infinity. In its chart,

$$
\begin{aligned}
e_1&=-1-B\tau-C\tau^2-D\tau^3,\\
e_2&=-B-C\tau-D\tau^2,\\
e_3&=-C-D\tau,
\end{aligned}
\qquad
(o_0,o_1,o_2,o_3)=(e_1,e_2,e_3,-D)\theta.
$$

The proof establishes freeness globally through the exact projective transition classes. The package supplies all eight multiplication matrices, including every coefficient at the discriminant.

For the multiplication-trace pairing

$$
T(f,g)=\operatorname{Tr}(m_{fg}),
$$

the even and odd blocks satisfy

$$
\boxed{
T_{eo}=0,\qquad
\det T_{ee}=16\Delta,\qquad
\det T_{oo}=16\Delta^2,\qquad
\det T=256\Delta^3.
}
\tag{8}
$$

This is the discriminant of the finite locally free algebra in the multiplication-trace convention. It is distinct from the original Hermitian Gamma Gram (The Stacks Project Authors, 2026, Tag 0BVH).

The degeneration can now be resolved into its complete local algebra. Suppose \(r_0\) has multiplicity \(m\in\{2,3,4\}\), and write

$$
F_0(r_0+x)=x^m h(x),\qquad h(0)\ne0.
$$

Its signed local fibre is

$$
\boxed{
\mathscr E_{r_0}
=
\mathbb C[x,\sigma]\Big/
\left(x^m,\ \sigma^2-x^{m-1}u(x)\right),
\qquad u(0)=mh(0).
}
\tag{9}
$$

It has the explicit basis

$$
1,x,\ldots,x^{m-1},
\quad
\sigma,x\sigma,\ldots,x^{m-1}\sigma,
$$

and hence length \(2m\). In particular,

$$
\boxed{m=2\quad\Longrightarrow\quad
\mathscr E_{r_0}\cong\mathbb C[\sigma]/(\sigma^4).}
\tag{10}
$$

Thus two colliding root labels, each carrying two signs, produce a length-four nonreduced block. They do not leave an unexplained deficit of four states.

For every \(m\ge2\),

$$
\sigma^4=0,\qquad \sigma^3\ne0.
$$

The multiplication-trace pairing has rank one on this local block. Nevertheless, the coefficient functional of \(x^{m-1}\sigma\) supplies a nondegenerate socle pairing:

$$
(f,g)\longmapsto
[x^{m-1}\sigma](fg).
$$

Its matrix is

$$
\begin{pmatrix}0&J_m\\J_m&0\end{pmatrix},
$$

where \(J_m\) reverses the basis order, and its determinant is \((-1)^m\).

This gives an explicit replacement for the degenerate trace pairing while retaining the nilpotent directions. It does not assign that socle pairing the role of the original positive metric.

## 3. The connection is fully evaluated, including the extension at collisions

On the unramified locus, differentiation along a coefficient \(\alpha\in\{A,B,C,D\}\) is determined by the two incidence equations. With \(V_\alpha=\partial_\alpha F\),

$$
\boxed{
\nabla_\alpha r=-\frac{V_\alpha}{F'},
\qquad
\nabla_\alpha\sigma
=
\sigma\frac{V_\alpha'F'-F''V_\alpha}{2(F')^2}.
}
\tag{11}
$$

In the global basis (7), all four connection matrices have been evaluated:

$$
\Gamma_\alpha=\frac{Q_\alpha}{\Delta},
\qquad
Q_\alpha\in
\operatorname{Mat}_8\bigl(\mathbb Q[A,B,C,D]\bigr).
\tag{12}
$$

The complete \(Q_A,Q_B,Q_C,Q_D\) are included in `CONNECTION.json`. After returning to this global frame, there is **no denominator \(A\)**. The excluded-sign hyperplane therefore produces no connection pole away from the discriminant.

The exact identities are

$$
\boxed{\operatorname{tr}\Gamma=\frac32\,d\log\Delta,}
\tag{13}
$$

$$
\partial_\alpha T
=
\Gamma_\alpha^{\mathsf T}T+T\Gamma_\alpha,
$$

and

$$
\boxed{
\partial_\alpha\Gamma_\beta-\partial_\beta\Gamma_\alpha
+[\Gamma_\alpha,\Gamma_\beta]=0.
}
\tag{14}
$$

All polynomial numerators in these identities were checked exactly.

The extension at higher collisions is also determined. Along the transverse family \(F_t=F_0-t\), retain the reversible analytic changes

$$
q=xh(x)^{1/m},
\qquad
\widetilde\sigma
=
\frac{\sigma}{
\sqrt{F_0'(r_0+x(q))/q^{m-1}}
}.
$$

The equations become

$$
q^m=t,\qquad \widetilde\sigma^2=q^{m-1},
$$

with both selected unit roots and their inverses retained.

In the corresponding rank-\(2m\) extension, the residue spectrum is exactly

$$
\boxed{
\left\{\frac jm:0\le j<m\right\}
\cup
\left\{\frac jm+\frac{m-1}{2m}:0\le j<m\right\}.
}
\tag{15}
$$

For a double root this gives

$$
0,\quad\frac14,\quad\frac12,\quad\frac34.
$$

For a triple root the spectrum includes \(1\); for a quadruple root it includes \(9/8\). Those integer parts belong to the retained extension. Replacing them by \(0\) and \(1/8\) would change the extension lattice, even though the corresponding monodromy eigenvalues would be unchanged.

The local monodromy has one \(2m\)-cycle when \(m\) is even and two \(m\)-cycles when \(m\) is odd. The old factor coordinate has the exact growth order

$$
|a|\asymp |t|^{-(m-1)/(2m)}.
\tag{16}
$$

This supplies the collision algebra, its continuation, its residue spectrum, and its escaping original coordinate in one calculation.

## 4. The complete-action question now has an exact answer

The original nonzero Jacobian gives every constant target matrix \(M\) a unique polynomial lift:

$$
X_M(x)
=
-\frac12\operatorname{adj}(DP_i(x))\,MP_i(x),
\qquad
DP_i\,X_M=MP_i.
\tag{17}
$$

The preceding calculation established that formula. The new result classifies its completeness, without assuming that the source field is linear:

$$
\boxed{
X_M\text{ is complete for all complex times and initial points}
\iff
M=\lambda\operatorname{diag}(1,-1,-2,-3).
}
\tag{18}
$$

The necessity follows from the original nonproper locus. A complete flow \(\varphi_t\) is a holomorphic automorphism and satisfies

$$
P_i\varphi_t=e^{tM}P_i.
$$

It must therefore preserve the nonproper-value set. In particular, the linear target action preserves the irreducible discriminant hypersurface, forcing

$$
(MY)\cdot\nabla\Delta=\kappa\Delta.
\tag{19}
$$

The full sixteen-variable stabilizer calculation has only one parameter. Its derivation already follows from the lowest homogeneous pieces:

$$
\begin{aligned}
\Delta_2&=-27D^2,\\
\Delta_3&=18BCD-4C^3,\\
\Delta_4&=144ABD^2-6AC^2D-4B^3D+B^2C^2.
\end{aligned}
$$

Coefficient comparison first forces

$$
\dot D=\frac\kappa2D,\qquad
\dot B=\frac\kappa6B,\qquad
\dot C=\frac\kappa3C,
$$

with every off-diagonal term removed. The remaining degree-four equation is

$$
(144BD^2-6C^2D)
\left(\dot A+\frac\kappa6A\right)=0,
$$

and hence \(M=-(\kappa/6)\operatorname{diag}(1,-1,-2,-3)\).

Conversely, this matrix has the explicit complete source flow

$$
(a,y,z,w)\longmapsto
(e^{\lambda t}a,e^{-\lambda t}y,
 e^{-2\lambda t}z,e^{-3\lambda t}w).
$$

### A bounded construction of an escaping orbit

The obstruction is constructive for every other \(M\). Define

$$
\begin{aligned}
Y_{A,B,r}
&=(A,B,-4Ar^3-3r^2-2Br,\,
             3Ar^4+2r^3+Br^2),\\
V_M(A,B,r)
&=(MY_{A,B,r})\cdot(r^4,r^2,r,1),\\
H(A,B,r)
&=(B+3r+6Ar^2)
  (1-4Ar-8A^2r^2-4AB).
\end{aligned}
$$

The condition \(AHV_M\ne0\) gives a quartic with exactly one double selected root and a linear orbit transverse to the discriminant.

For every \(M\) outside (18), one of the following **312 candidates** passes:

$$
A\in\{1,\ldots,6\},\qquad
B\in\{0,\ldots,3\},\qquad
r\in\{0,\ldots,12\}.
\tag{20}
$$

The proof uses the separate degree bounds \(5,3,12\) of the nonzero polynomial \(AHV_M\). It is a finite interpolation argument, not a heuristic search.

Starting shortly before that target on its linear orbit gives four original-source lifts with

$$
\|x(t)\|\asymp(T-t)^{-1/4}
\quad\text{as }t\uparrow T,
$$

while the target remains finite. This statement uses positive real time on the complex coefficient space.

### Application to the actual original translation operator

On the original conductor target \(\mathcal P_3\), differentiation has matrix

$$
N=
\begin{pmatrix}
0&1&0&0\\
0&0&2&0\\
0&0&0&3\\
0&0&0&0
\end{pmatrix}.
$$

Retain the published receiving map

$$
\Psi=Y_{\mathrm{mat}}K^{-1}.
$$

The actual target translation generator in the polynomial coordinates is

$$
M_{\mathrm{tr}}=\Psi^{-1}N\Psi.
\tag{21}
$$

Here \(Y_{\mathrm{mat}}\) retains the original moments:

$$
(Y_{\mathrm{mat}})_{k\alpha}
=
\sum_{j=k}^3
\lambda_{j\alpha}
\binom{v+j}{k}\mu_{v+j-k}.
$$

These are the FC35 receiving coordinates, not a fitted replacement.

Since \(M_{\mathrm{tr}}\) is nonzero nilpotent, it cannot belong to (18). Therefore:

$$
\boxed{
\text{The original translation action has no complete lift through }
P_{\mathcal W}=\Psi P_i\Psi^{-1}.
}
\tag{22}
$$

The original **linear** conductor still commutes with translations exactly. What fails is global completeness of the introduced nonlinear lift. The finite-cover connection and its retained collision algebras describe the boundary where that lift fails, rather than transferring the failure to the conductor.

## 5. The literal quartet and its formal collision are evaluated

For the original marking

$$
\rho_{\mathrm M,\mathrm N,\mathrm T,\mathrm E}
=
\frac12+\delta+i\gamma,\ 
\frac12+\delta-i\gamma,\ 
\frac12-\delta+i\gamma,\ 
\frac12-\delta-i\gamma,
$$

put

$$
F_\rho(u)=-\frac12\prod_\alpha(u-\rho_\alpha).
$$

Its \(u^3\) coefficient is exactly one, so it lies in the retained slice. The evaluated discriminants are

$$
\boxed{
\Delta(F_\rho)
=
64\delta^4\gamma^4(\delta^2+\gamma^2)^2,
}
\tag{23}
$$

and

$$
\boxed{
\det T_\rho
=
2^{26}\delta^{12}\gamma^{12}
(\delta^2+\gamma^2)^6.
}
\tag{24}
$$

They are nonzero on the original stipulated domain \(0<\delta<1/2,\ \gamma>2\).

The separate formal coefficient specialization \(\delta=0\) gives

$$
F_0(u)
=
-\frac12\left((u-\tfrac12)^2+\gamma^2\right)^2.
$$

Its full signed fibre is

$$
\boxed{
\mathscr E_0
\cong
\mathbb C[\sigma_+]/(\sigma_+^4)
\oplus
\mathbb C[\sigma_-]/(\sigma_-^4).
}
\tag{25}
$$

The upper block retains the nearby M,T branches and their signs; the lower block retains N,E and their signs.

There is an important operator distinction inside each block. With

$$
r_\pm=\frac12\pm i\gamma,\qquad x=u-r_\pm,
$$

the exact local relation is

$$
\sigma_\pm^2=4\gamma^2x.
$$

Consequently,

$$
\boxed{
m_u
=
r_\pm I+\frac1{4\gamma^2}N_{\sigma_\pm}^{\,2}.
}
\tag{26}
$$

Multiplication by \(\sigma_\pm\) has one size-four nilpotent Jordan block. Multiplication by \(u-r_\pm\) has two size-two blocks. These are different operators linked by (26), not interchangeable descriptions of the same action.

The trace form has rank two and a six-dimensional radical at this specialization, but the fibre still has length eight.

Finally, the retained local basis has an explicit return to any fixed admitted original conductor. For a block of length \(n\), map its specified basis elements \(b_j\) to

$$
J_n(b_j)=[S^{v+j}],\qquad 0\le j<n.
$$

Then

$$
T_{\mathcal A}J_n(b_j)
=
\sum_{k=0}^j
\binom{v+j}{k}\mu_{v+j-k}S'^k.
\tag{27}
$$

The inverse on the image is triangular back substitution, because every diagonal entry is

$$
\binom{v+j}{v}\mu_v\ne0.
$$

With the original Gamma polynomial norms

$$
h_{j,s}=(2\pi)^{s/2}j!(s/2)_j,
$$

the complete source and target Gram determinants are

$$
\det G_+=\prod_{j=0}^{n-1}h_{v+j,s},
$$

$$
\det G_-
=
|\mu_v|^{2n}
\left(\prod_{j=0}^{n-1}\binom{v+j}{v}\right)^2
\prod_{j=0}^{n-1}h_{j,s},
$$

and hence

$$
\boxed{
\frac{\det G_-}{\det G_+}
=
\left|\frac{\mu_v}{v!}\right|^{2n}
\prod_{j=0}^{n-1}
\frac{(\rho_{v+j}^{(s)})^2}{(\rho_j^{(s)})^2}
=
|\det A_{n-1,s}|^2>0.
}
\tag{28}
$$

This retains the original quotient metric, Gamma mass, centres, and moment convention of FC20–30. For the two length-four blocks in (25), the same construction uses two copies of the existing four-dimensional conductor.

Thus the trace degeneracy, the nilpotent root action, and the original positive Gamma metric now have separately specified maps and evaluated determinants. The formal coefficient specialization does not assume that actual zeta zeros or their period units move to that boundary.

