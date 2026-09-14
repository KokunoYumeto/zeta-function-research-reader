# Exact finite operator quotients of the tau-base theta cohomology

Owner-directed continuation, 12 September 2026. Mathematical derivation and research draft; no new analytic theorem below is claimed to have been checked by Lean.

## 0. Inputs, provenance, and the new result

This note continues `TAU_BASE_MODEL.md`, rather than moving the programme back to a finite-field variety. Its arithmetic coefficient object is the original split semiring

$$G(R)=\{\tau\}\sqcup\{r^\bullet:r\in R\},\qquad e=0_R^\bullet.$$

The geometric base remains the one-point absolute pointed base described there. The quotient

$$p_{\mathbb Z}:G(\mathbb Z)\longrightarrow\mathbb Z$$

and its square with $G(\mathbb C)\to\mathbb C$ remain part of the marked object. No ideal norm, Euler factor, scaling parameter, Gaussian, or completion factor is changed here.

The supplied derived formalization (PR #6, `5f6ee6575550d8a20c6fc3990359cb4f67855f80`) provides the actual reconstruction, internal quotient, homology-kernel equivalence, and compatible kernel actions. Its finite-jet module supplies the balanced tensor-quotient comparison with the split-reflection square. Those results are reused; this note does not duplicate their Lean implementation.

The new analytic step computes the previously only surjective finite Mellin-jet observation as an exact operator quotient. For every polynomial $h$ whose roots lie in the open critical strip, it constructs

$$Q/h(D)Q\ \xrightarrow{\sim}\ E_h/g_hE_h,\qquad
Q[h(D)]\ \xrightarrow{\sim}\ \ker(g_h:E_h\to E_h),$$

with $E_h=\mathbb C[t]/(h)$ and $g=2\xi$. It then constructs finite spectral projectors on the original $Q$, not only quotients of $Q$, and identifies the torsion subsheaf of the balanced analytic realization with $\mathcal O/(2\xi)$. Their kernels, original supported zeros, nilpotent actions, and trace-producing residue pairing are all retained.

The general existence of spectral realizations of zeta zeros is prior literature (not a novelty claim here): see R. Meyer, *A spectral interpretation for the zeros of the Riemann zeta function*, arXiv:math/0412277. The contribution of this note is the explicit comparison in the specified workbench, together with its original SplitZero quotients and its complete finite kernel calculation.

## 1. The exact arithmetic complex and its operator

Retain

$$V=\{\phi\in\mathcal S(\mathbb R):\phi(-x)=\phi(x),\ \phi(0)=0,\ \int_{\mathbb R}\phi(x)\,dx=0\},$$

$$\mathscr B=\{F\in C^\infty(\mathbb R_{>0}):
\sup_{x>0}x^b|(-x\partial_x)^kF(x)|<\infty\ \text{for all }b\in\mathbb Z,\ k\ge0\}.$$

The source maps, with their original factors, are

$$D=-x\partial_x,\quad
\Theta\phi(x)=\sum_{n\in\mathbb Z\setminus\{0\}}\phi(nx),\quad
\mathcal MF(s)=\int_0^\infty F(x)x^s\frac{dx}{x}.$$

The Fourier transform is $\widehat\phi(\xi)=\int_{\mathbb R}\phi(x)e^{-2\pi i x\xi}\,dx$. Poisson and the two moment conditions put $\Theta V$ in $\mathscr B$. Also $D\Theta=\Theta D$, and $D$ preserves $V$.

Set

$$A=\mathbb C[t],\qquad t\cdot F=DF,\qquad t\cdot\phi=D\phi,$$

$$C_+=[V\xrightarrow{\Theta}\mathscr B]\quad\text{in degrees }0,1,
\qquad Q=\mathscr B/\Theta V.$$

The existing injectivity proof of $\Theta$ gives $H^0(C_+)=0$ and $H^1(C_+)=Q$.

This is the one-leg subcomplex of the actual tau-base chart complex

$$C_{+-}=[V\oplus V\xrightarrow{\Theta\phi-\Theta\widehat\psi}\mathscr B].$$

Its inclusion is $\phi\mapsto(\phi,0)$ in degree zero and the identity in degree one. The quotient complex is the second copy of $V$ in degree zero. The explicit section is $\psi\mapsto(\widehat\psi,\psi)$. The operator on that second copy is $1-D$, because $D\widehat\psi=\widehat{(1-D)\psi}$. Thus the additional joint-support degree-zero cohomology is retained in this split exact sequence; it is not included in $Q$ and then silently discarded.

The actual source multiplier is

$$g(s)=2\xi(s)=s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),$$

$$H_\phi(s)=c(s)M_+\phi(s),\quad
c(s)=\frac{2\pi^{s/2}}{s(s-1)\Gamma(s/2)},\quad
M_+\phi(s)=\int_0^\infty\phi(x)x^s\frac{dx}{x}.$$

On the open strip $\mathscr S=\{0<\Re s<1\}$, $c(s)$ is holomorphic and nowhere zero. The source identity is

$$\mathcal M\Theta\phi=gH_\phi.$$

The specific function

$$\phi_*(x)=(4\pi^2x^4-6\pi x^2)e^{-\pi x^2}$$

has $H_{\phi_*}=1$. Consequently

$$H_{P(D)\phi_*}(s)=P(s),\qquad
\mathcal M\Theta(P(D)\phi_*)=g(s)P(s).$$

These are identities with the stated Gaussian and $g=2\xi$; no rescaling is performed.

## 2. A continuous inverse to the actual Euler differential

For any $\rho\in\mathbb C$, define on the subspace $\{H\in\mathscr B:\mathcal MH(\rho)=0\}$

$$\boxed{S_\rho H(x)=x^{-\rho}\int_x^\infty H(t)t^{\rho-1}\,dt.}$$

All powers use the real logarithm on $x,t>0$. Direct differentiation gives

$$(D-\rho)S_\rho H=H.$$

**Endpoint control.** Write $x=e^y$, $h(y)=H(e^y)$, and $\sigma=\Re\rho$. At $y\ge0$, the displayed tail and a bound $|h(t)|\le C_Ne^{-Nt}$ give

$$|S_\rho H(e^y)|\le\frac{C_N}{N-\sigma}e^{-Ny}\quad(N>\sigma).$$

At $y\le0$, the zero moment changes the same expression into the negative lower tail. A bound $|h(t)|\le C_N'e^{Nt}$ gives

$$|S_\rho H(e^y)|\le\frac{C_N'}{N+\sigma}e^{Ny}\quad(N+\sigma>0).$$

Differentiating uses $(S_\rho H)'_y=-\rho S_\rho H-H(e^y)$, so every derivative has the same family of estimates. This proves membership in $\mathscr B$ and continuity in its stated seminorms. The homogeneous solution $x^{-\rho}$ fails the required rapid decrease unless its coefficient is zero. Thus $D-\rho$ is injective, and

$$\boxed{(D-\rho)\mathscr B=\ker(F\mapsto\mathcal MF(\rho)).}$$

Mellin intertwining gives

$$\mathcal M(S_\rho H)(s)=\frac{\mathcal MH(s)}{s-\rho},$$

with the removable value filled at $s=\rho$.

There is also a source inverse. For $\rho\in\mathscr S$ and $\phi\in V$ with $H_\phi(\rho)=0$, use the same tail for $x>0$ and extend evenly. The nonvanishing of $c(\rho)$ gives $M_+\phi(\rho)=0$. Near zero the formula is

$$S_\rho\phi(x)=-\int_0^1u^{\rho-1}\phi(xu)\,du.$$

Differentiation under this integral proves smoothness at zero in every order. The function is even and its value at zero is zero. The upper-tail formula proves Schwartz decay at infinity. Finally

$$(1-\rho)\int_{\mathbb R}S_\rho\phi(x)\,dx=\int_{\mathbb R}\phi(x)\,dx=0,$$

so the second moment condition is preserved. This proves the source range identity

$$\boxed{(D-\rho)V=\ker(\phi\mapsto H_\phi(\rho))\quad(\rho\in\mathscr S).}$$

At the level of Taylor coefficients $\phi(x)=\sum_{j\ge1}a_{2j}x^{2j}$, the local expression is $-\sum_{j\ge1}a_{2j}x^{2j}/(\rho+2j)$, interpreted to each finite Taylor order with its smooth remainder. All denominators and the minus sign are retained. Endpoints $0,1$ are not included in this source range theorem.

## 3. Every finite operator test, without choosing zeros first

Choose any finite set of distinct centres $\rho_1,\ldots,\rho_r\in\mathscr S$ and positive integers $m_i$. Define the particular polynomial

$$h(t)=\prod_{i=1}^r(t-\rho_i)^{m_i},\quad d=\deg h,\quad E_h=A/(h).$$

This defines the test; it does not presume that any centre is a zeta zero. The Chinese-remainder map is

$$\theta_h:E_h\xrightarrow{\sim}\prod_i\mathbb C[z_i]/(z_i^{m_i}),\qquad
[P(t)]\mapsto[P(\rho_i+z_i)].$$

For a holomorphic germ family $f$ at the centres, $j_hf$ denotes its Taylor jets transported back by $\theta_h^{-1}$. In particular $g_h=j_hg$ retains the original local units of $g$.

Iterate Section 2 through the factors of $h$. Uniqueness makes the inverse independent of their chosen order. This gives the continuous inverse

$$S_h:\ker(j_h\mathcal M)\longrightarrow\mathscr B,
\qquad h(D)S_h=\mathrm{id}.$$

The exact range identities are

$$h(D)\mathscr B=\ker(j_h\mathcal M),\qquad
h(D)V=\ker(j_hH).$$

Surjectivity on the source follows from $H_{P(D)\phi_*}=P$. Surjectivity of the target jet map follows directly from finite Mellin interpolation: on an interval in $y=\log x$, the functions $e^{\rho_i y}y^j/j!$ are linearly independent. For a nonnegative smooth bump $\eta$ positive on a subinterval, the Gram matrix

$$G_{(i,j),(k,l)}=\int\eta(y)e^{(\rho_i+\bar\rho_k)y}\frac{y^{j+l}}{j!l!}\,dy$$

is positive definite. Multiplying its inverse into the prescribed jet vector produces a compactly supported smooth preimage. This is only an interpolation device; it does not define or alter the arithmetic Weil pairing.

Consequently the vertical arrows in

$$\boxed{\begin{array}{ccc}
V/h(D)V&\xrightarrow{\overline\Theta}&\mathscr B/h(D)\mathscr B\\
\alpha_h\downarrow\wr&&\wr\downarrow\beta_h\\
E_h&\xrightarrow{\times g_h}&E_h
\end{array}}$$

are actual $A$-module isomorphisms:

$$\alpha_h[\phi]=j_hH_\phi,\qquad \beta_h[F]=j_h\mathcal MF.$$

An inverse to $\alpha_h$ sends the unique polynomial representative $P$ of degree less than $d$ to $[P(D)\phi_*]$. An inverse to $\beta_h$ is any of the above explicit interpolation lifts, taken modulo $h(D)\mathscr B$; the class is independent of that choice by the range theorem.

## 4. The kernel and quotient of the global arithmetic operator

Both $V$ and $\mathscr B$ are torsion-free $A$-modules: every factor $D-\rho$ is injective, since its homogeneous solution cannot be Schwartz at infinity. Over the PID $A$, they are flat. The bounded complex $C_+$ is therefore a valid flat model for derived tensoring. The displayed isomorphism computes

$$\boxed{C_+\otimes_A^{\mathbf L}E_h\ \simeq\ [E_h\xrightarrow{\times g_h}E_h]}$$

in degrees zero and one. It is the base-change of the actual theta complex, not a newly declared spectral complex with an assigned differential.

The original exact sequence $0\to V\xrightarrow\Theta\mathscr B\to Q\to0$ also gives

$$\boxed{0\to Q[h(D)]\xrightarrow{\kappa_h}E_h
\xrightarrow{\times g_h}E_h\longrightarrow Q/h(D)Q\to0.}$$

Here $Q[h(D)]=\ker(h(D):Q\to Q)$. The maps are explicit:

* Given $[F]\in Q[h(D)]$, uniquely write $h(D)F=\Theta\phi$. Then $\kappa_h[F]=j_hH_\phi$.
* The quotient observation sends $[F]$ to $j_h\mathcal MF$ modulo $g_hE_h$.
* For $P\in\ker(g_h:E_h\to E_h)$, choose its polynomial representative of degree less than $d$ and set

$$\boxed{\partial_h(P)=[S_h\Theta(P(D)\phi_*)]\in Q[h(D)].}$$

The last expression is defined because its theta input has zero jets modulo $h$. Replacing $P$ by $P+hR$ changes the result by $\Theta(R(D)\phi_*)$. Thus it is independent of representatives and is the inverse of $\kappa_h$ onto its kernel. The two injectivity and surjectivity assertions also follow directly by lifting representatives in the preceding exact sequence; no dimension-only argument is needed.

All maps commute with $D$, with $U_aF(x)=F(x/a)$, and with compactly supported multiplicative convolution. On $E_h$, the scaling action is multiplication by $j_h(a^s)$, including its entire finite nilpotent Taylor polynomial.

At one centre, retain $g(\rho+z)=u(z)z^r$, where $u(0)\ne0$ (and $r=0$ is allowed). For test order $m$, the two cohomology modules have dimension $\min(m,r)$. When $r=0$, multiplication by $g_h$ is invertible. The derived amplitude complex is then acyclic, while its reconstructed supported homology still has each labelled internal zero.

The degree-zero term is $Q[h(D)]$; the degree-one term is $Q/h(D)Q$. Their finite alternating traces cancel. The arithmetic packet trace below is the degree-one action, or equivalently its explicitly constructed direct summand in the original $Q$. The canonical truncation triangle retains the degree-zero term rather than relabelling it as zero.

## 5. Exact finite spectral projectors on the original cohomology

Now let $Z$ be any finite set of actual nontrivial zeros and retain their full multiplicities $r_\rho$. Put

$$h_Z(t)=\prod_{\rho\in Z}(t-\rho)^{r_\rho},\quad E_Z=A/(h_Z),\quad
v_Z(s)=g(s)/h_Z(s).$$

The quotient $v_Z$ is entire and its germs are nonzero at every point of $Z$. Hence $v_{Z,h}=j_{h_Z}v_Z$ is an invertible element of $E_Z$. This inverse retains the actual Taylor coefficients of $g/h_Z$; it is not set to one.

Here $g_{h_Z}=0$, and the exact sequence becomes

$$Q[h_Z(D)]\xrightarrow[\kappa_Z]{\sim}E_Z,
\qquad Q/h_Z(D)Q\xrightarrow[\beta_Z]{\sim}E_Z.$$

There is a further map that must be calculated, not assumed: the inclusion of the kernel into $Q$, followed by the quotient. For $P\in E_Z$,

$$\mathcal M\bigl(S_{h_Z}\Theta(P(D)\phi_*)\bigr)
=\frac{gP}{h_Z}=v_ZP.$$

Therefore this kernel-to-quotient comparison is precisely

$$\boxed{\beta_Z\,q_Z\,\partial_Z=M_{v_{Z,h}}:E_Z\xrightarrow{\sim}E_Z.}$$

Define

$$\sigma_Z=\partial_Z\circ M_{v_{Z,h}^{-1}}:E_Z\longrightarrow Q,$$

$$\boxed{\Pi_Z=\sigma_ZJ_Z:Q\longrightarrow Q,\qquad J_Z[F]=j_{h_Z}\mathcal MF.}$$

Then

$$\boxed{J_Z\sigma_Z=\mathrm{id},\quad \Pi_Z^2=\Pi_Z,\quad
\operatorname{im}\Pi_Z=Q[h_Z(D)],\quad \ker\Pi_Z=h_Z(D)Q.}$$

This gives the actual equivariant direct sum

$$\boxed{Q=Q[h_Z(D)]\oplus h_Z(D)Q.}$$

A representative formula is completely determined. For $F\in\mathscr B$, let $P_{Z,F}$ be the unique polynomial of degree less than $\deg h_Z$ representing $v_{Z,h}^{-1}j_{h_Z}\mathcal MF$. Then

$$\boxed{\Pi_Z[F]=[S_{h_Z}\Theta(P_{Z,F}(D)\phi_*)].}$$

For a simple actual zero $\rho$, this specializes to

$$\Pi_{\{\rho\}}[F]=\frac{\mathcal MF(\rho)}{g'(\rho)}
\left[x^{-\rho}\int_x^\infty\Theta\phi_*(t)t^{\rho-1}\,dt\right].$$

The displayed denominator is the actual $g'(\rho)=2\xi'(\rho)$; it is not omitted. The bracketed class is an actual nonzero eigenclass in $Q$, proved by the exact sequence, even though its representative is only an eigenvector modulo the theta relation.

For finite packets the projectors satisfy

$$\Pi_Z\Pi_W=\Pi_{Z\cap W},\qquad
\Pi_{Z\cup W}=\Pi_Z+\Pi_W\quad(Z\cap W=\varnothing).$$

These follow from the direct sums, coprimality of disjoint packet polynomials, and commutation with $D$. Inclusions of finite packets therefore give compatible invariant subspaces and quotient observations. No convergence of an infinite sum of projectors is asserted.

## 6. Carry every projector through the original split quotient

For any vector space $M$ the single-active-fibre lift is $M^\tau=\{\tau\}\sqcup\{m^\bullet:m\in M\}$. For a submodule $N$ use exactly

$$q_N^{\mathrm{sp}}:M^\tau\to(M/N)^\tau,\quad
m^\bullet\mapsto[m]^\bullet,\quad\tau\mapsto\tau.$$

This is the original coequalizer of the relation inclusion and its internal-zero companion. Its universal property is the one implemented in PR #6, including arbitrary noncancellative target semimodules.

Consequently the finite observation has the split-linear equivalence

$$\boxed{(Q/h(D)Q)^\tau\xrightarrow{\sim}G(E_h/g_hE_h),\qquad
[F]^\bullet\mapsto(j_h\mathcal MF\bmod g_hE_h)^\bullet.}$$

The domain is being used as a split semimodule, not as an unconstructed ring. A class in $h(D)Q$ maps to the supported zero, and external absence alone maps to external absence.

Lift the projector as

$$\widetilde\Pi_Z(\lambda,[F])=(\lambda,\Pi_Z[F]).$$

This formula applies to the actual nonempty support faces of the tau-base theta model; their degree-one transports are the stated identities of $Q$. At bottom it is the original zero map of the bottom module. The full reconstruction interface permits a nonzero bottom fibre when a subsequent diagram requires one; it is not silently specialized away on an opposite-index dual diagram.

For disjoint packets,

$$\boxed{\widetilde\Pi_Z\widetilde\Pi_W=\varepsilon,
\qquad\varepsilon(\lambda,x)=(\lambda,0).}$$

This is the supported lift of the zero linear operator, not the constant external-zero map. More uniformly, take $\Pi_\varnothing=0_Q$ and lift it to $\varepsilon$. The scalar representation

$$G(\operatorname{End}_{\mathbb C}Q)\longrightarrow
\operatorname{End}_{G(\mathbb C)}(Q^\tau)$$

sends $f^\bullet$ to its split lift and sends $\tau$ to the constant-\(\tau\) map. It is a unital semiring morphism and sends the supported scalar zero to $\varepsilon$.

### Retain smaller admitted source labels

For a subspace $W\subset V$, first use its specified enlargement $W_D=\mathbb C[D]W$ and keep the map

$$\mathscr B/\Theta W\longrightarrow Q_{W_D}:=\mathscr B/\Theta W_D,
\qquad\ker=\Theta W_D/\Theta W.$$

For a $D$-stable $W$, define the ideal

$$J_{W,h}=\{j_hH_\phi:\phi\in W\}\subseteq E_h.$$

It is an ideal because $H_{P(D)\phi}=P H_\phi$ and every element of $E_h$ has a polynomial representative. The same target range calculation gives

$$\boxed{Q_W/h(D)Q_W\cong E_h/(g_hJ_{W,h}).}$$

Enlarging to $W+\mathbb C[D]\phi_*$ makes $J_{W,h}=E_h$. The exact finite comparison kernel is

$$\boxed{g_hE_h/(g_hJ_{W,h}).}$$

Thus the finite equality for the full arithmetic relation space has a precise smaller-label comparison. It is not asserted for every original $W$ without this kernel.

## 7. The Hausdorff observation and the remaining global kernel

The projectors just constructed have continuous finite-rank representatives on $\mathscr B$: $J_Z$ is continuous, $E_Z$ is finite dimensional, and $S_{h_Z}$ is continuous on its zero-jet domain. They annihilate $\Theta V$, hence also its closure. They therefore descend to

$$Q^{\mathrm H}=\mathscr B/\overline{\Theta V}.$$

The finite observation still has kernel exactly $h_Z(D)Q^{\mathrm H}$. Indeed

$$\ker J_Z=h_Z(D)\mathscr B+\Theta V,$$

and continuity gives $\overline{\Theta V}\subset\ker J_Z$. Hence adding the closure to the right side leaves it unchanged. The same finite section yields a continuous direct sum

$$Q^{\mathrm H}=\sigma_Z(E_Z)\oplus h_Z(D)Q^{\mathrm H}.$$

The algebraic packet $Q[h_Z(D)]$ injects into this Hausdorff quotient: its composite with $J_Z$ is already an isomorphism onto $E_Z$. No conclusion about vanishing of the entire algebraic-to-Hausdorff kernel follows from this finite statement.

Let

$$\mathcal R_\infty=\bigcap_{Z\text{ finite}}\ker\Pi_Z
=\bigcap_{Z\text{ finite}}h_Z(D)Q.$$

The map $Q\to\prod_\rho\mathcal O_\rho/(g)$ has exactly this kernel. Every nonzero polynomial whose roots are in $\mathscr S$ acts bijectively on $\mathcal R_\infty$. To verify this, its kernel on $Q$ lies in the finite packet at its zero centres; its cokernel is supported there as calculated in Section 4. On the complementary summand it is bijective, and its inverse preserves all other commuting finite projectors. This proves injectivity and surjectivity on the intersection.

The continuation retains $\mathcal R_\infty$ and its scaling action. Finite packets do not prove it zero. A topological spectral-synthesis theorem or a global cohomological trace argument must address that specific invariant module rather than infer its disappearance from finite-jet isomorphisms.

### 7.1 The global balanced kernel has a computed local-cohomology complement

Work now on the analytic strip $\mathscr S$, with its sheaf $\mathcal O$ and sheaf $\mathcal K$ of meromorphic functions. Form the sheafified balanced realization

$$\mathcal M_Q=\mathcal O\otimes_AQ,\qquad
\beta:\mathcal M_Q\longrightarrow\mathcal O/(g),\quad
b\otimes[F]\longmapsto[b\,\mathcal MF].$$

Let $\operatorname{tors}_{\mathcal O}(\mathcal M_Q)$ denote its torsion subsheaf: a germ is in it when some nonzero holomorphic germ annihilates it. This is torsion over the specified analytic coefficient ring; its connection to the original split support is the reconstruction of the inclusion and quotient maps below.

**Theorem.** The actual Mellin map restricts to an isomorphism

$$\boxed{\beta|_{\operatorname{tors}}:
\operatorname{tors}_{\mathcal O}(\mathcal M_Q)
\xrightarrow{\sim}\mathcal O/(g).}$$

Moreover, $\mathcal N=\ker\beta$ has a canonical $\mathcal K$-module structure, and the displayed map canonically splits the sequence:

$$\boxed{\mathcal M_Q\cong\mathcal O/(g)\oplus\mathcal N,
\qquad\mathcal K\otimes_{\mathcal O}\mathcal N\cong\mathcal N.}$$

**Proof at every stalk.** Fix $\rho\in\mathscr S$ and set $x=s-\rho$. If $g(\rho)\ne0$, Section 4 with $h=t-\rho$ proves that $D-\rho$ is bijective on $Q$. Consequently $x$ is invertible on $\mathcal M_{Q,\rho}$, and this module is a module over the meromorphic field $\mathcal O_\rho[1/x]$. Its torsion is zero, as is $\mathcal O_\rho/(g)$.

If $r=\operatorname{ord}_\rho g>0$, the finite projector for this one full packet gives

$$Q=Q[(D-\rho)^r]\oplus (D-\rho)^rQ.$$

On the second summand, $(D-\rho)^r$ is bijective: it is injective by the direct-sum intersection, and

$$(D-\rho)^rQ=(D-\rho)^{2r}Q$$

follows by applying $(D-\rho)^r$ to the direct sum. Hence $D-\rho$ itself is bijective there. Tensoring the direct sum with $\mathcal O_\rho$ gives a first summand $\mathcal O_\rho/(x^r)$, on which $\beta$ is the isomorphism calculated in Section 5, and a second summand on which $x$ is invertible. The map $\beta$ kills the second summand because it is in $x^r\mathcal M_{Q,\rho}$, while $x^r$ annihilates its target. Every nonzero germ of $\mathcal O_\rho$ is a unit times a power of $x$, so that second summand is a module over $\mathcal K_\rho$ and is torsion-free.

This proves the stated torsion isomorphism at every stalk. It glues without choosing neighbourhood projectors: both the torsion subsheaf and the restricted map $\beta$ are intrinsic. The inverse of that isomorphism, followed by the torsion inclusion, is the global section of $\beta$. Local inverses to nonzero holomorphic scalars on $\mathcal N$ are unique, so they glue to its $\mathcal K$-module structure. This proves the theorem.

### 7.2 The extraction is an actual local-cohomology map

At the same stalk the principal-ideal local-cohomology complex is the explicit localization complex

$$R\Gamma_{(x)}(\mathcal M_{Q,\rho})
=[\mathcal M_{Q,\rho}\longrightarrow\mathcal M_{Q,\rho}[1/x]],
\quad\text{degrees }0,1.$$

The decomposition just proved computes it:

$$\boxed{R\Gamma_{(x)}(\mathcal M_{Q,\rho})
\xrightarrow{\sim}(\mathcal O_\rho/(g))[0].}$$

The finite torsion summand maps to zero upon localization; the meromorphic summand maps isomorphically to itself. The map to the displayed target is $\beta$ in degree zero and zero in degree one. Thus the supported arithmetic divisor is the actual cohomological image of the localization kernel, not a prescribed deletion of a list of spectral points.

Before analytic extension there is the corresponding operator-localization map

$$Q\longrightarrow A[h_Z^{-1}]\otimes_AQ,$$

with kernel $Q[h_Z(D)]$ and cokernel zero, because $h_Z(D)$ is invertible on its complementary summand. Its supported lift sends that kernel to the internal supported zero, not to external absence.

At every original label $\lambda$, reconstruct the localization complex using

$$d(\lambda,m)=(\lambda,m/1),\qquad
\varepsilon(\lambda,m)=(\lambda,0).$$

Its internal degree-zero cycles are exactly the reconstructed torsion module. Its internal first cohomology is the support skeleton, since the ordinary first cohomology vanishes. The map $p_{\mathbb Z}$ remains in the structural coefficient square throughout; $x$ is the analytic image of the operator $t-\rho$, not a replacement for the scalar $e$ or $\tau$.

The theorem does not assert $\mathcal N=0$. It computes what local cohomology does to it: localization is an isomorphism on that module, so it contributes no cohomology to the stated local-support complex. Its possible contribution to a different global trace functor has not been declared absent.

## 8. The residue duality is now inside an actual derived finite comparison

Assume the centres and their orders in $h$ are stable under $\iota(s)=1-\bar s$. For germs define

$$f^\dagger(s)=\overline{f(1-\bar s)}.$$

The chosen monic polynomial satisfies $h^\dagger=(-1)^d h$. Retain that factor. Define the perfect finite algebra pairing

$$R_h(f,u)=\sum_i\operatorname{Res}_{s=\rho_i}
\frac{f^\dagger(s)u(s)}{h(s)}\,ds.$$

It satisfies $\overline{R_h(u,f)}=(-1)^{d+1}R_h(f,u)$. No phase is inserted to change this sign. Since $g^\dagger=g$, multiplication by $g_h$ is self-adjoint for this pairing. Therefore it induces a perfect pairing

$$\boxed{\overline{\operatorname{coker}g_h}\ \otimes\ \ker g_h
\longrightarrow\mathbb C.}$$

Well-definedness is the identity $R_h(ga,u)=R_h(a,gu)$; nondegeneracy follows by taking the annihilator of the image in the finite perfect algebra pairing. Through Section 4 this pairs the two actual cohomology groups of $C_+\otimes_A^{\mathbf L}E_h$.

For an exact packet $h_Z$, set $v_{Z,h}=j_h(g/h_Z)$ as above and

$$\jmath_Z:A_Z\to\ker g_h=E_Z,\qquad
[f]\mapsto[j_h(h_Z/g)f].$$

Here $A_Z=\prod_{\rho\in Z}\mathcal O_\rho/(g)\cong E_Z$ by the specified local quotient maps; $h_Z/g$ is holomorphic at every centre. The local units are not replaced by one. The exact contraction is

$$\boxed{R_h(f,\jmath_Zk)=
\sum_{\rho\in Z}\operatorname{Res}_{\rho}\frac{f^\dagger k}{g}\,ds=:R_Z(f,k).}$$

Thus the previously constructed arithmetic residue form is the duality pairing of the actual finite operator comparison after the displayed unit morphism.

The Jacobian map is still $J_g[k]=[g'k]$. Its contraction is

$$\boxed{R_h(f,\jmath_ZJ_gk)=R_Z(f,J_gk)
=\sum_{\rho\in Z}r_\rho\overline{f(1-\bar\rho)}k(\rho)
=\operatorname{Tr}(M_{f^\dagger k}|A_Z).}$$

In particular the factor $2$ in $g=2\xi$ is retained in both the denominator and the Jacobian. The trace contraction is invariant under their combined explicitly specified transformation, not by deleting that factor in only one place.

Every map lifts to the original support fibres. Dual support arrows are precomposition maps on the opposite index category. A vanishing pairing value is the supported scalar $e_{\mathbb C}$; an absent argument gives $\tau$.

## 9. Cohomological placement and arithmetic traces

On the tau-base chart use the one-leg sheaf $\mathcal T_+$ and its $A$-action. The bounded projective resolution from `TAU_BASE_MODEL.md` gives the canonical map

$$\mathsf A_\tau(\mathcal T_+\otimes_A^{\mathbf L}E_h)
\xrightarrow{\sim}
\mathsf A_\tau(\mathcal T_+)\otimes_A^{\mathbf L}E_h
\xrightarrow{\sim}[E_h\xrightarrow{g_h}E_h].$$

These isomorphisms use finite evaluation sums and the displayed free/flat resolutions. They are not compact-support base-change assertions for a different arithmetic scheme.

The packet projector is now an actual finite-rank endomorphism of the original $H^1_\tau=Q$ (and of each of its retained support fibres). For an admissible smooth compactly supported multiplicative test $k$,

$$H_kF(x)=\int_0^\infty k(a)F(x/a)\,\frac{da}{a}$$

commutes with the projector. Its ordinary finite-rank trace is

$$\boxed{\operatorname{Tr}(H_k\Pi_Z|Q)
=\sum_{\rho\in Z}r_\rho\mathcal Mk(\rho).}$$

This is a finite-rank trace on the original cohomology, using its explicit finite invariant image. It is stronger than declaring that a surjective finite observation has a trace. Infinite trace summation still requires the specified topology and admissible test class.

On $r$-fold products over the tau-point, the already calculated external tensor map gives $H^r=Q^{\otimes r}$. The operator $\Pi_Z^{\otimes r}$ is a finite projector onto $Q[h_Z]^{\otimes r}$. The full nilpotent scaling action there is

$$a^{\rho_1+\cdots+\rho_r}
\exp\left((\log a)\sum_{j=1}^rN_{\rho_j,j}\right).$$

For a repeated exponent the exact modulus comparison remains

$$\log\frac{|a^{r\rho}|^2}{a^r}=r(2\Re\rho-1)\log a.$$

This supplies actual finite invariant objects on which a Deligne-style tensor estimate would have to act. It does not prove that estimate. The source's opposite weight bounds, its global dualizing theory, and the admissibility of its geometric hypotheses have not been inferred from these finite isomorphisms.

## 10. Status and publication boundary

**Established in this note, with written proofs:** the differential range identities on the stated spaces; the exact finite operator quotient and torsion kernel; the derived finite comparison; the analytic torsion-subsheaf and local-cohomology identification with $\mathcal O/(2\xi)$; finite spectral direct summands with explicit projectors; the original split lifts and smaller-label kernels; the residue/Jacobian contraction on that comparison; and compatible finite-rank arithmetic traces and tensor actions.

**Not claimed:** a global injectivity theorem for the full balanced analytic realization; vanishing of $\mathcal R_\infty$; identification of the entire four-point chart category with an arithmetic curve; a full compact-support/ordinary-cohomology realization satisfying the hypotheses of Weil II; positivity of the unshifted Weil form; RH or GRH. The finite tests are not a Lean or analytic proof certificate.

The prior base note and this continuation are published as additive research material beside PR #6. The original scalar core, formal modules, frozen reader and all existing branches remain unchanged. New derivations are AI-assisted work under the owner's programme; the structural source and its Lean implementation retain their own attribution. No copyrighted source corpus or private conversation is included.

### References and source interfaces

- Owner's SplitZero programme: the original scalar, support fibre and quotient constructions; PR #6 at `5f6ee6575550d8a20c6fc3990359cb4f67855f80`, especially `SplitZeroHomology.lean`, `SplitZeroComplex.lean`, `SplitZeroInternalQuotient.lean`, and `SplitZeroFiniteJets.lean`.
- `TAU_BASE_MODEL.md`: the actual characteristic-zero chart, cohomology, right-adjoint and tensor constructions used here. It remains an authored research model, not an accepted geometric RH realization.
- Deligne, P., *La conjecture de Weil. II* (1980), sections 3.3.4-3.3.6 and 6.2.1-6.2.7. Selected supplied TeX passages were reread for the intended comparison/duality architecture; no source proof is republished or claimed fully audited.
- Meyer, R., *A spectral interpretation for the zeros of the Riemann zeta function*, arXiv:math/0412277. Prior spectral-realization context; no theorem from it is silently used to identify the test spaces here.
- The Stacks Project, Derived tensor product, Tag 06XY. The general bounded-flat-complex construction used in Section 4.
