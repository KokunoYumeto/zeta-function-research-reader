# Chain-level arithmetic descent over the tau base

Owner-directed research continuation, 12 September 2026. Draft proofs for review; no new Lean certification or RH claim.

## 0. Fixed inputs and publication scope

This is an additive continuation of Zeta PR #8 at `25689c5376166df37801229bc275ff5a896007d9`, particularly `workbenches/tau-base-cohomology/FINITE_OPERATOR_COMPARISON.md` (Git blob `68f59d098d60708f8e899bb960abbd1135ebb3b4`). Its sections 1–5 supply the stated analytic range theorem and the finite packet maps. The new result here is their chain-level descent, its actual extension class, and the connection of that class to residue duality and the arithmetic trace.

The source programme retains

$$G(R)=\{\tau\}\sqcup\{r^\bullet:r\in R\},\quad e_R=0_R^\bullet,$$

$$p_R(\tau)=0_R,\qquad p_R(r^\bullet)=r.$$

The absolute pointed base and the coefficient square remain

$$\mathfrak b_\tau=\operatorname{Spec}\mathbf F_{1,\tau},\qquad
\begin{array}{ccc}G(\mathbb Z)&\xrightarrow{G(j)}&G(\mathbb C)\\
p_{\mathbb Z}\downarrow&&\downarrow p_{\mathbb C}\\
\mathbb Z&\xrightarrow{j}&\mathbb C.\end{array}$$

The target of the first vertical map remains the infinite ring of integers. Every new arrow below is a coefficient or cochain construction over this marked base. No base field, ideal norm, Euler factor, or completion constant is changed.

The supplied derived note and PR #6 provide `Recovery.recoverEquiv`, `Relations.coequalizer_universal`, the internal-homology coequalizer, `ChainMap.homologyKernelEquiv`, and `homology_intertwines`. Their algebraic conclusions are used at their stated types. No existing formal module is modified. Analytic inputs from PR #8 remain written research arguments; they are not promoted to Lean theorems.

## 1. The actual arithmetic source and packet

Let

$$V=\{\phi\in\mathcal S(\mathbb R):\phi(-x)=\phi(x),\ \phi(0)=0,\ \int_{\mathbb R}\phi(x)\,dx=0\},$$

$$\mathscr B=\{F\in C^\infty(\mathbb R_{>0}):
\sup_{x>0}x^b|(-x\partial_x)^kF(x)|<\infty\text{ for every }b\in\mathbb Z,k\ge0\}.$$

Retain

$$D=-x\partial_x,\quad \Theta\phi(x)=\sum_{n\in\mathbb Z\setminus\{0\}}\phi(nx),\quad
\mathcal MF(s)=\int_0^\infty F(x)x^s\frac{dx}{x},$$

$$\widehat\phi(\xi)=\int_{\mathbb R}\phi(x)e^{-2\pi i x\xi}\,dx,\qquad
A=\mathbb C[t],\quad t\cdot F=DF.$$

The one-leg tau-chart complex is

$$C_+=[V\xrightarrow{\Theta}\mathscr B],\quad |V|=0,\quad |\mathscr B|=1,\qquad Q=H^1(C_+).$$

The injectivity of theta gives $H^0(C_+)=0$. The two-leg complex is

$$C_{+-}=[V\oplus V\longrightarrow\mathscr B],\qquad
(\phi,\psi)\longmapsto\Theta\phi-\Theta\widehat\psi.$$

Its source operator is $(D,1-D)$; the inclusion $C_+\to C_{+-}$ is $\phi\mapsto(\phi,0)$ and the identity in degree one. It leaves the extra degree-zero copy of $V$ in $C_{+-}$ present.

Use the unchanged arithmetic multiplier

$$g(s)=2\xi(s)=s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s).$$

The input function is

$$\phi_*(x)=(4\pi^2x^4-6\pi x^2)e^{-\pi x^2},$$

and the established identities are

$$\mathcal M\Theta\phi=gH_\phi,\qquad H_{\phi_*}=1,\qquad
H_{P(D)\phi_*}(s)=P(s).$$

Fix a nonempty finite packet $Z$ of actual nontrivial zeros, with full orders $m_\rho$. Set

$$h(t)=\prod_{\rho\in Z}(t-\rho)^{m_\rho},\quad d=\deg h,\quad E=A/(h),\quad v(s)=g(s)/h(s).$$

The specific monic polynomial defines this finite test; it does not rescale $g$. Write $j_h$ for the complete Taylor-jet/Chinese-remainder map at these centres, and retain the invertible element

$$v_h=j_hv\in E^\times,\qquad \varepsilon_Z=v_h^{-1}.$$

For $u\in E$, let $R_Z(u)\in\mathbb C[t]_{<d}$ be the unique polynomial representing $\varepsilon_Zu$.

The input range theorem supplies the inverse $S_h^{\mathscr B}$ of $h(D)$ on the zero-jet range, and the analogous source inverse $S_h^V$. For one factor,

$$S_\rho F(x)=x^{-\rho}\int_x^\infty F(y)y^{\rho-1}\,dy.$$

The stated source inverse uses $0<\Re\rho<1$ and the zero moment. Iteration supplies $S_h$. Define the actual maps

$$J:\mathscr B\to E,\quad JF=j_h\mathcal MF,$$

$$s:E\to\mathscr B,\quad s(u)=S_h^{\mathscr B}\Theta(R_Z(u)(D)\phi_*).$$

The inverse is defined because $gR_Z(u)$ has all required zero jets. Directly,

$$\mathcal Ms(u)=vR_Z(u),\quad Js=1_E,\quad J\Theta=0,\quad
h(D)s(u)=\Theta(R_Z(u)(D)\phi_*).\tag{1}$$

These equations fix the representative map, including all derivatives of $g/h$. On $Q$, the existing projector is $\Pi_Z=\bar s\bar J$, with image $Q[h(D)]$ and kernel $h(D)Q$.

## 2. The exact equivariant extension and its class

Define an actual subspace of the original test-function space:

$$\mathscr B_Z=\{F\in\mathscr B:[F]\in Q[h(D)]\}.$$

Then

$$\mathscr B_Z=\Theta V\oplus s(E)\quad\text{as complex vector spaces},$$

with maps

$$(\phi,u)\longmapsto\Theta\phi+s(u),\qquad
F\longmapsto\bigl(\Theta^{-1}(F-sJF),JF\bigr).\tag{2}$$

For the inverse, $F-sJF$ has zero class in $Q$ by the packet projector theorem; injectivity of theta makes its source unique. The intersection is zero by $Js=1$ and $J\Theta=0$.

The original operator $D$ preserves $\mathscr B_Z$, and there is a short exact sequence of $A$-modules

$$\boxed{0\longrightarrow V\xrightarrow{\Theta}\mathscr B_Z\xrightarrow{J}E\longrightarrow0.}\tag{3}$$

The arrows in (3), not just the three modules, specify its extension class. Compute it using the resolution

$$0\longrightarrow A\xrightarrow{\times h}A\longrightarrow E\longrightarrow0.$$

The resulting isomorphism $\operatorname{Ext}^1_A(E,V)\cong V/h(D)V$ sends an extension to $h(D)b$ in the source, where $b$ is any lift of $1\in E$. Fixing this explicit rule fixes its sign. Under the existing map $[\phi]\mapsto j_hH_\phi$, the class of (3) is

$$\boxed{[\mathscr B_Z]=\varepsilon_Z=j_h(h/g)\in E^\times.}\tag{4}$$

Proof: use the lift $s(1)$ and (1). Its source boundary is $R_Z(1)(D)\phi_*$, whose $H$-jet is $\varepsilon_Z$.

In particular, (3) has no $A$-linear section. This also follows immediately from the injectivity of $h(D)$ on $\mathscr B$: an $A$-linear map $E\to\mathscr B$ has image killed by $h(D)$ and is therefore zero. The map $s$ in (2) is the explicit complex-linear section, and the next section computes exactly how it fails to intertwine the arithmetic action. This non-splitting occurs for every nonempty packet, including critical-line packets; it is not an RH-failure criterion.

The general use of extension classes is standard homological algebra (Stacks, Tags 010I and 06XP). Formula (4) calculates the specific extension arising from this theta complex.

## 3. The scaling defect is an original theta boundary

For $P\in A$ and $u\in E$, define

$$q_P(u)=\frac{P(t)R_Z(u)-R_Z(Pu)}{h(t)}\in A,\qquad
k_P(u)=q_P(u)(D)\phi_*\in V.\tag{5}$$

The numerator is divisible by $h$, since both of its residues are $P\varepsilon_Zu$. Using (1) and the injectivity of $h(D)$ on $\mathscr B$ gives

$$\boxed{P(D)s-sM_P=\Theta k_P.}\tag{6}$$

No quotient has yet been applied in (6). The right side is an actual theta function. The composition law is

$$\boxed{k_{PQ}=P(D)k_Q+k_PM_Q.}\tag{7}$$

It follows either by expanding the numerator of (5), or by expanding the commutator in (6) and using injectivity of theta.

For $P=t$, the numerator of (5) has degree at most $d$. Hence

$$\ell_Z(u)=[t^{d-1}]R_Z(u),\quad q_t(u)=\ell_Z(u),\quad
\boxed{Ds(u)-s(tu)=\ell_Z(u)\Theta\phi_*.}\tag{8}$$

Thus, in the exact coordinates (2), the original operator is

$$\boxed{D_{\mathscr B_Z}=
\begin{pmatrix}D_V&\phi_*\ell_Z\\0&M_t\end{pmatrix}.}\tag{9}$$

Its off-diagonal map is rank one and its coefficient is determined by the retained local arithmetic unit. It is not chosen to improve a spectral estimate.

For one simple zero,

$$h=t-\rho,\quad \varepsilon_Z=1/g'(\rho),$$

$$s(1)=\frac1{g'(\rho)}x^{-\rho}\int_x^\infty\Theta\phi_*(y)y^{\rho-1}\,dy,$$

$$\boxed{(D-\rho)s(1)=\frac1{g'(\rho)}\Theta\phi_*.}\tag{10}$$

The coefficient is $1/(2\xi'(\rho))$, with the original factor two retained.

### The full dilation group

For $a>0$, retain $U_aF(x)=F(x/a)$ and $A_a=M_{j_h(a^s)}$ on $E$. Define

$$k_a(u)=S_h^V\bigl(U_a(R_Z(u)(D)\phi_*)-R_Z(A_au)(D)\phi_*\bigr).\tag{11}$$

The source of $S_h^V$ has zero $H$-jets because $a^s\varepsilon_Zu$ and $\varepsilon_ZA_au$ have equal jets. All powers use the real logarithm of $a$. The exact identities are

$$U_as-sA_a=\Theta k_a,\qquad
k_{ab}=U_ak_b+k_aA_b,\qquad k_1=0.\tag{12}$$

The same construction applies to a smooth compactly supported multiplicative test $f$: replace $U_a$ by $H_f=\int f(a)U_a\,da/a$ and $A_a$ by $M_{j_h\mathcal Mf}$. The source integral belongs to $V$; its $H$-jets give the same cancellation. These are actual linear maps, not a choice of a formal matrix on $E$ alone.

## 4. A derived equivariant inclusion with its full homotopy

Put $P_Z=sJ:\mathscr B\to\mathscr B$. It is a finite-rank idempotent, and $P_Z\Theta=0$. Consequently

$$\mathsf p_Z=(0,P_Z):C_+\to C_+\tag{13}$$

is a cochain idempotent. Its image is the two-term complex $[0\to s(E)]$, complex-linearly isomorphic to $E[-1]$.

For the operator $P(D)$ on $C_+$, define a degree-minus-one map with sole component

$$\mathsf H_P^1=k_PJ:\mathscr B\to V.$$

Equation (6) gives

$$\boxed{P(D)\mathsf p_Z-\mathsf p_ZP(D)
=d\mathsf H_P+\mathsf H_Pd.}\tag{14}$$

In degree one this is $\Theta k_PJ$; in degree zero it is zero because $J\Theta=0$. For dilation use $\mathsf H_a^1=k_aJ$. Equation (12) is the coherence law of those homotopies.

There is also a strictly $A$-linear derived presentation. Set

$$C_Z=[V\xrightarrow{\Theta}\mathscr B_Z].$$

In the coordinates (2) its differential is $\phi\mapsto(\phi,0)$ and its action is (9). The maps

$$\iota:C_Z\hookrightarrow C_+,\qquad
\pi:C_Z\to E[-1],\quad\pi^0=0,\ \pi^1=J\tag{15}$$

are strictly $A$-linear cochain maps, and $\pi$ is a quasi-isomorphism. Thus the actual equivariant inclusion is the roof

$$\boxed{E[-1]\xleftarrow[\simeq]{\pi}C_Z\xrightarrow{\iota}C_+.}\tag{16}$$

The complex-linear deformation retraction also has an exact contracting homotopy: on $\mathscr B_Z$, send $\Theta\phi+s(u)$ to $\phi\in V$. Its equation is $1-s\pi=dH+Hd$ (with $s$ interpreted as the degree-one cochain section). This homotopy is not claimed $A$-linear; the $A$-linear replacement is the roof (16).

The strictly $A$-linear map $j:C_+\to E[-1]$ is $J$ in degree one and zero in degree zero. It satisfies $j\iota=\pi$. This gives a split retract in $D(A)$ without falsely asserting an $A$-linear section into $\mathscr B$.

On the two-leg complex use $\mathsf p_Z^0=0$ on $V\oplus V$, $\mathsf p_Z^1=P_Z$, and $\mathsf H_a^1(F)=(k_aJF,0)$. The source dilation is $(U_a,aU_{1/a})$, so (14) holds with its original two-leg differential. The inclusion $C_+\to C_{+-}$ commutes with these cochain projectors. The extra degree-zero cohomology of $C_{+-}$ is killed by this projector; it remains in the complementary complex.

## 5. The mixed-support homotopies require the actual synchronization map

Let $L=\mathcal P(\{+,-\})$ be the original chart-support lattice. Its three active complexes are

$$C_+=[V\xrightarrow{\Theta}\mathscr B],\quad
C_-=[V\xrightarrow{-\Theta\mathcal F}\mathscr B],\quad
C_{+-}=[V\oplus V\xrightarrow{\Theta(\phi-\widehat\psi)}\mathscr B].$$

Here $\mathcal F$ is the specified Fourier transform, with $\mathcal F^2=1$ on even functions. The source inclusions into the joint fibre are $v\mapsto(v,0)$ and $v\mapsto(0,v)$; degree-one transports are identities. The bottom complex is zero in this particular model. The new formalization allows a nonzero bottom fibre in the general reconstruction; no assertion about all diagrams is obtained by specializing this model.

The reconstructed operations are

$$(\lambda,x)+(\mu,y)=
(\lambda\vee\mu,\rho_{\lambda,\lambda\vee\mu}x+\rho_{\mu,\lambda\vee\mu}y),$$

$$e(\lambda,x)=(\lambda,0),\qquad
\tau(\lambda,x)=(\bot,0).\tag{17}$$

The cochain projector $\widetilde{\mathsf p}_Z$ is zero-in-its-fibre in degree zero and $P_Z$ in degree one. It commutes with the support transports. So does the actual action: $U_a$ on the plus source, $aU_{1/a}$ on the minus source, their direct sum on the joint source, and $U_a$ at every active overlap.

The objectwise homotopies are, however, different maps. With $b=k_aJF$, they are

$$\mathsf H_{a,+}^1(F)=b,\qquad
\mathsf H_{a,-}^1(F)=-\widehat b.$$

Their images in the joint source are $(b,0)$ and $(0,-\widehat b)$. The difference is the explicit cycle

$$\boxed{(b,\widehat b)\in\ker d_{+-}=H^0(C_{+-}).}\tag{18}$$

For nonzero $k_a$, there is no label-preserving family of homotopies compatible with both source inclusions: the joint component would have to equal both $(b,0)$ and $(0,-\widehat b)$. This says exactly which naturality square fails. It does not discard the cohomology or the arithmetic action.

The replacement is the programme's actual synchronization. Define the support map

$$r_L(\bot)=\bot,\qquad r_L(\lambda)=\{+,-\}\quad(\lambda\ne\bot).$$

In degree zero use literal multiplication by $E=(1,e)$ on the original two-coordinate support module:

$$\mathfrak r^0(a,b)=(a+eb,b+ea).$$

In degree one define $\mathfrak r^1(\lambda,F)=(r_L\lambda,F)$ for active labels and preserve global zero. An absent source coordinate becomes its supported vector zero, so the source differential has unchanged amplitude. Hence

$$\boxed{d\mathfrak r^0=\mathfrak r^1d,\qquad
\mathfrak r^2=\mathfrak r.}\tag{19}$$

This uses the operation verified in the synchronization attachment, now on the actual complex. The fixed active fibre is exactly $C_{+-}$. On degree-one homology, the map is

$$(\lambda,[F])\longmapsto(\{+,-\},[F]).$$

It has no nonzero amplitude kernel, because all degree-one transports are the identity of $Q$. The original mask is retained through

$$x\longmapsto(\operatorname{supp}(x),\mathfrak r x).$$

This map is injective in each degree of this chart complex: in degree zero the coordinate inclusions are injective, and in degree one the transport is the identity. This injectivity is a proved property of these maps, not an assumption for general diagrams with noninjective transports.

There are now two actual split-linear homotopies with the same support map $r_L$. Define

$$\widetilde{\mathsf H}^{\mathrm{left},1}_a(\lambda,F)
=(\{+,-\},(k_aJF,0)),$$

$$\widetilde{\mathsf H}^{\mathrm{right},1}_a(\lambda,F)
=(\{+,-\},(0,-\mathcal F k_aJF)),$$

and send global zero to global zero. Both satisfy

$$\boxed{\mathfrak r\bigl(\widetilde U_a\widetilde{\mathsf p}_Z
+(-1)^\bullet\widetilde{\mathsf p}_Z\widetilde U_a\bigr)
=\widetilde d\widetilde{\mathsf H}_a+
\widetilde{\mathsf H}_a\widetilde d.}\tag{20}$$

In degree one this is (6); in degree zero it follows from $Jd=0$. The two choices differ by the retained cycle (18). No averaging or removal of that cycle is performed. This is the precise role of synchronization here: it permits a common supported comparison fibre for the homotopy, while the original mask and the difference of homotopies remain recorded.

In the simple-zero case (10), the defect in any source support is the nonzero chain amplitude $\Theta(\phi_*/g'(\rho))$. Its internal homology class is the zero of that support, not external absence.

For every chain comparison $f:C\to C'$, the supplied formalized kernel equivalence remains

$$\{z\in Z(C):f(z)\in B(C')\}/B(C)\xrightarrow{\sim}\ker H(f).$$

Applied to $\pi$ in (15), it computes the zero kernel in degree one from its actual exact sequence. Applied to support synchronization, it yields the degree-one assertion just proved and the separately retained degree-zero data. It is not applied to a different global comparison without carrying that comparison's maps.

For any smaller $D$-stable admitted source $W\subset V$, the map $Q_W\to Q$ has kernel $\Theta V/\Theta W$. A homotopy value may not already lie in $W$. The explicit replacement is enlargement by the actual source values, with this quotient map and its kernel retained. The present chart uses full $V$, where every displayed homotopy is defined.

## 6. The same extension class produces the arithmetic duality factor

Assume $Z$ is stable under $\rho\mapsto1-\bar\rho$. Then

$$f^\dagger(s)=\overline{f(1-\bar s)},\qquad h^\dagger=(-1)^d h.$$

The perfect finite pairing is

$$R_h(f,u)=\sum_{\rho\in Z}\operatorname{Res}_{s=\rho}
\frac{f^\dagger(s)u(s)}{h(s)}\,ds,$$

with exact symmetry $\overline{R_h(u,f)}=(-1)^{d+1}R_h(f,u)$.

Identify $E$ with the actual divisor algebra $A_Z=\prod_{\rho\in Z}\mathcal O_\rho/(g)$ by polynomial evaluation and the complete Chinese-remainder jets. The nonzero local units in $g/h$ make this an isomorphism. The operator represented by the extension class is

$$M_{\varepsilon_Z}:E\to E.$$

Substituting (4) into the residue formula gives

$$\boxed{R_h(f,M_{\varepsilon_Z}u)
=\sum_{\rho\in Z}\operatorname{Res}_{\rho}
\frac{f^\dagger u}{g}\,ds=R_Z(f,u).}\tag{21}$$

This is independent of representatives: changing $\varepsilon_Z$ by $h$ times a germ adds a holomorphic differential. Thus the actual extension class is precisely the unit morphism converting the polynomial-resolution residue form into the arithmetic residue form.

Let $J_g=M_{j_hg'}$. Then

$$\boxed{R_h(f,M_{\varepsilon_Z}J_gu)
=\sum_{\rho\in Z}m_\rho\overline{f(1-\bar\rho)}u(\rho)
=\operatorname{Tr}(M_{f^\dagger u}\mid E).}\tag{22}$$

Locally $g=z^m w(z)$ gives $g'/g=m/z+w'/w$. This proves the formula and retains every multiplicity. The product $\varepsilon_ZJ_g$ carries both factors associated to $g=2\xi$.

The pairing-valued support map sends a zero value to $e_{\mathbb C}$ and an absent argument to $\tau$. Its original input support and relation fibre remain available upstream. Formula (22) is a calculated trace, not a positivity assertion.

### Reflection is strict for this specified section

Define conjugate-linear involutions

$$\mathfrak j_BF(x)=x^{-1}\overline{F(1/x)},\quad
\mathfrak j_V\phi=\overline{\widehat\phi},\quad j_Eu=u^\dagger.$$

They satisfy $\Theta\mathfrak j_V=\mathfrak j_B\Theta$ and $J\mathfrak j_B=j_EJ$. The actual source function is Fourier-fixed: writing $\phi_*=D(D-1)e^{-\pi x^2}$, Fourier sends the two factors to $(1-D)(-D)=D(D-1)$ and fixes the Gaussian. It is real, so $\mathfrak j_V\phi_*=\phi_*$.

Since $\varepsilon_Z^\dagger=(-1)^d\varepsilon_Z$ and reflection preserves polynomial degree,

$$R_Z(j_Eu)=(-1)^d(R_Z(u))^\dagger.$$

Uniqueness of the inverse of $h(D)$ on its range gives

$$\mathfrak j_B S_h^{\mathscr B}=(-1)^d S_h^{\mathscr B}\mathfrak j_B.$$

Both factors $(-1)^d$ are retained in the substitution, and their product is one. Therefore

$$\boxed{\mathfrak j_Bs=sj_E,\qquad
\mathfrak j_BP_Z=P_Z\mathfrak j_B.}\tag{23}$$

This is an actual equality for this section; it would not follow for an arbitrary choice of representatives. Its compatibility with the nonzero dilation homotopy is

$$\boxed{\mathfrak j_V k_a=a k_{1/a}j_E.}\tag{24}$$

Indeed, apply $\mathfrak j_B$ to (12), use $\mathfrak j_BU_a=aU_{1/a}\mathfrak j_B$ and (23), then use injectivity of theta. The split lift is semilinear through $r^\bullet\mapsto\bar r^\bullet$, which fixes both $e$ and $\tau$.

## 7. A finite-rank Lefschetz trace on the actual chain complex

For $f\in C_c^\infty(\mathbb R_{>0})$, let $\mathsf U_f$ be its convolution action on $C_+$. The cochain endomorphism

$$\mathsf p_Z\mathsf U_f=(0,sJH_f)$$

has finite-rank components. Its cochain supertrace is therefore defined without an infinite-dimensional regularization:

$$\boxed{\operatorname{Str}(\mathsf p_Z\mathsf U_f\mid C_+)
=-\operatorname{Tr}(sJH_f\mid\mathscr B)
=-\sum_{\rho\in Z}m_\rho\mathcal Mf(\rho).}\tag{25}$$

The finite-rank identity $\operatorname{Tr}(AB)=\operatorname{Tr}(BA)$ reduces the middle expression to $\operatorname{Tr}(JH_fs\mid E)$; this is multiplication by $j_h\mathcal Mf$. Equation (25) equals the supertrace of the induced operator on homology. On $C_{+-}$ its degree-zero contribution is still zero, since the same cochain projector has zero degree-zero component.

The boundary representatives in (6), (14), and (20) are retained even though their contribution to homology is zero. The finite-rank trace does not delete their complex or assign its zero to external absence.

For the $n$-fold tensor complex over the tau-base product, use the original coefficient tensor over $\mathbb C$ and its differential

$$d(x_1\otimes\cdots\otimes x_n)=
\sum_j(-1)^{\sum_{i<j}|x_i|}
 x_1\otimes\cdots\otimes dx_j\otimes\cdots\otimes x_n.$$

The projector $\mathsf p_Z^{\otimes n}$ has image $E^{\otimes n}[-n]$. For independently specified tests $f_1,\ldots,f_n$,

$$\operatorname{Str}\left(\bigotimes_j(\mathsf p_Z\mathsf U_{f_j})\right)
=(-1)^n\prod_j\sum_{\rho\in Z}m_\rho\mathcal Mf_j(\rho).\tag{26}$$

Let $A=U_a\mathsf p_Z$ and $B=\mathsf p_ZU_a$ as cochain maps. A homotopy for $A^{\otimes n}-B^{\otimes n}$ is

$$\sum_{j=1}^nB^{\otimes(j-1)}\otimes\mathsf H_a\otimes A^{\otimes(n-j)},$$

with the displayed Koszul sign on homogeneous inputs when the degree-minus-one map crosses the preceding factors. The telescoping identity and (14) prove it. The full support mask maps to the product of its input masks; vanishing products of represented amplitudes stay supported.

## 8. What now enters the Weil II programme

The structural base, the infinite quotient, and the actual theta complex are unchanged. The new objects are the extension (3), its unit class (4), its synchronized homotopy (20), its strict equivariant derived roof (16), and the chain trace (25). The arithmetic residue unit in (21) is now supplied by that very extension rather than appended without its source.

Deligne's inspected comparison-image argument (Weil II 3.3.4–3.3.6) requires two weight bounds on the same cohomological image. The inspected derived formulation (6.2.1–6.2.7) retains the dualizing operation, its degree and Tate shifts, and its exchange of direct-image functors. This continuation supplies coherent arithmetic maps and finite trace operations for the tau model; it does not transfer the finite-field hypotheses or assert those two bounds.

The retained error is explicit: it is the original boundary $\Theta k_a$ on representatives, with the nonzero Ext class (4). It is removed at homology by the original supported quotient, not by making its input absent. A geometric comparison can now be tested for compatibility with this class and the residue map (21). A complex-linear section that ignores (6) fails that test.

No infinite sum of packet projectors is asserted to converge. The existing meromorphic/kernel summand from PR #8 remains in its own exact sequence, and a different global trace functor must retain or analyze its contribution. The source's finite-jet isomorphisms and the new finite-rank chain trace do not by themselves set that summand to zero.

## 9. Verification and references

The new finite checker tests polynomial remainder identities, the extension class, rank-one scaling defects, cochain homotopies, dilation cocycles, residue contraction, tensor signs, trace identities, and original support operations. These finite algebraic models are not numerical tests of zeta zeros and not certificates for the analytic range theorem. No Lean execution is claimed for this continuation.

Read source interfaces:

- PR #8 at the pinned revision above, `FINITE_OPERATOR_COMPARISON.md`, sections 1–10; `TAU_BASE_MODEL.md` is its already-published model.
- Owner's `SplitZero_Derived_Mathematics_2026-09-12(1).md`, sections 1–7. In particular its allowance of a nonzero bottom fibre and the exact homology-kernel/action theorems are retained.
- `formal/splitzero/SplitZeroHomology.lean`, lines 175–end, read at the same revision; blob `7b9e5c49a494dd0c751133e0234b3e01048f7b67`.
- Supplied Deligne TeX excerpts: French segment 2, original lines 882–950; segment 3, original lines 675–756. The used equations are the image bounds and duality operations, not every assertion in the historical transcription. No source corpus is republished with this contribution.
- The Stacks Project, Tags 010I and 06XP, for extension classes and their projective-resolution interpretation.
- R. Meyer, *A spectral interpretation for the zeros of the Riemann zeta function*, arXiv:math/0412277, for prior spectral-realization context. No global priority claim is made here.

New calculations are AI-assisted work under the owner's programme. Existing mathematical files, formalizations, licensing, and source attribution remain untouched.
