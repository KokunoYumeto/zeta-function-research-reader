# The continuous support-dual sheaf on the actual sphere

Complete independent derivation, 24 September 2026. Proof locators CSD0–CSD12.

## CSD0. Input stage and the category being constructed

The supporting datum remains \(\tau\langle Z_1;\mathrm{no}\ Z_2\rangle\). All coefficient vector spaces and all complex coordinates below belong to the receiving geometry after complete arithmetic reconstruction. No addition, numerical coordinate, midpoint or distance is assigned to \(\tau\).

For this continuation the current READ_FIRST_USER_CONSTRUCTION.md, the connected USER_ARGUMENT_RECONSTRUCTION.md and correction table, PC01–PC05 including its latest continuation, and verbatim WU050–WU055 and WU061–WU063 were recalled. The no-addition, no-metric, full-history and separate-branch corrections govern the same receiver as in CSP and CDW. The actual source maps are retained; the kernel \(J\) is not replaced by its quotient \(Q\).

The original-source use is that recorded in CSP0 and CDW0: Alain Connes and Caterina Consani, *Schemes over \(\mathbb F_1\) and zeta functions*, [arXiv:0903.2024v3](https://arxiv.org/abs/0903.2024v3), §5, and the field-valued charts and real structure of [arXiv:2609.00299v1](https://arxiv.org/abs/2609.00299v1). Those source readings and the local reconstructions are different provenance claims; this continuation does not claim a fresh complete reading of either paper.

The complete current proof CC_CONTINUOUS_DUAL_INDEPENDENT.md, CDI0–CDI12, supplies the continuous duals of the already constructed global and support coefficient complexes. Its full maps are the comparison target here. CSP0–CSP13 and CDW0–CDW10 supply the sphere sheaf and one compatible fine resolution. SSI1–SSI7 and ESI give the closed image and continuous inverse of the full original summation source.

Before the final topology and transfer comparisons below, the complete accepted CC_STRONG_DUAL_TOPOLOGY_AND_JETS.md, SDT0–SDT9, and CC_RAMIFIED_TRACE_AND_RESIDUE_ACTION.md, GTR0–GTR9, were read. Their bounded-lift theorem and separate weighted geometric trace are imported with their exact scope; neither is attributed to the preceding current construction.

An actual complex of sheaves with continuous maps is constructed below from continuous functionals on compactly supported tests. It is not defined by an unrestricted algebraic internal Hom. In particular \(A'\) always means the continuous complex-linear dual of the stated locally convex \(A\), never its algebraic dual. No equivalence for arbitrary topological sheaves is assumed.

## CSD1. Full primal source and single resolution

Let \(Y=\mathbb P^1(\mathbb C)\), \(P=\{0,\infty\}\), and \(i:P\hookrightarrow Y\). Retain
\[
S=\{f\in\mathcal S(\mathbb R;\mathbb C):f(-v)=f(v),\
f(0)=0,\ \int_{\mathbb R}f(v)\,dv=0\},\quad
V_\pm=S\oplus E_\pm,\quad E_\pm=\mathbb C^2,
\]
\[
A=\left\{a\in C^\infty(\mathbb R_{>0}):
\sup_{u>0}(u^N+u^{-N})|(u\partial_u)^ja(u)|<\infty\
\text{for all }N,j\ge0\right\},
\]
\[
\begin{gathered}
\Sigma f(u)=2\sum_{k\ge1}f(ku),\quad
Ra(u)=u^{-1}a(u^{-1}),\quad
\widehat f(t)=\int_{\mathbb R}f(v)e^{-2\pi ivt}\,dv,\\
\quad r_+(f,e)=\Sigma f,\quad r_-(h,e)=R\Sigma h=\Sigma\widehat h.
\end{gathered}
\tag{CSD1.1}
\]
The last equality uses the full Poisson formula with terms \(u^{-1}h(0)-\int h\), which vanish on this stated \(S\). Both coordinates of each \(E_\pm\), labelled value at zero and real integral, remain distinct.

The actual source image \(J=\Sigma S\) is closed, \(\Sigma:S\to J\) is a topological isomorphism, and \(Q=A/J\) has its Fréchet quotient topology. The proved inverse-image sheaf is
\[
\mathscr F=\pi^{-1}\Omega
=\underline A_Y\times_{i_*(A\oplus A)}i_*(V_+\oplus V_-).
\tag{CSD1.2}
\]
Here \(\pi(0)=x_+\), \(\pi(\infty)=x_-\), and \(\pi(\mathbb C^\times)=\eta\). Its generic inverse image is the entire punctured plane, not a numerical coordinate assigned to \(\tau\).

Put \(V=V_+\oplus V_-\). The difference map is onto on stalks through its evaluation component and gives
\[
0\to\mathscr F\to\underline A_Y\oplus i_*V
\xrightarrow{\mathrm{ev}-r}i_*A^2\to0.
\tag{CSD1.3}
\]
For smooth \(A\)-valued differential forms \(\mathscr E_A^q\), the single resolution from CDW2 is
\[
\mathscr K^0=\mathscr E_A^0\oplus i_*V,\quad
\mathscr K^1=\mathscr E_A^1\oplus i_*A^2,\quad
\mathscr K^2=\mathscr E_A^2,
\]
\[
d^0(f,v)=(df,\mathrm{ev}(f)-rv),\qquad d^1(\omega,a)=d\omega.
\tag{CSD1.4}
\]
Its degree-zero kernel is (CSD1.2). At a pole, a closed pair \((\omega,a)\) has primitive \(f=g+a-g(p)\), \(v=0\), where \(dg=\omega\). Away from the poles the coefficient-valued Poincaré lemma applies. This proves exactness in positive degrees with continuous local primitives. Forms and finite skyscrapers are fine.

This resolution also computes compactly supported cohomology. A section defined near a compact set extends after multiplication by a smooth cutoff equal to one on a smaller neighborhood of that set. The partition-of-unity contraction of the augmented Čech complex therefore works with compact supports: only finitely many members of a locally finite partition meet an input compact support, and all multiplications and sums are continuous. This proves the needed compact-support acyclicity for these form and skyscraper terms. It does not imply acyclicity for sections supported at a single point.

## CSD2. Continuous compact-support contraction

Set \(\mathcal E_c^q(U;A)=\Gamma_c(U,\mathscr E_A^q)\). Its topology is the locally convex inductive limit over compact supports, each given all smooth-derivative seminorms from \(A\). Finite pole sums have their product topologies. Extension by zero of compactly supported forms is continuous.

An explicit compact-support Poincaré calculation is useful. In an oriented plane chart choose \(\rho_x,\rho_y\in C_c^\infty(\mathbb R)\) with integrals one. Define
\[
I_x f(y)=\int_{\mathbb R}f(x,y)\,dx,\qquad
H_x f(x,y)=\int_{-\infty}^x f(t,y)\,dt
-\left(\int_{-\infty}^x\rho_x(t)\,dt\right)I_x f(y),
\tag{CSD2.1}
\]
and define \(H_y\) similarly. Completeness of \(A\) supplies the integrals. For every continuous seminorm,
\[
p\!\left(\int f\right)\le\int p(f),
\tag{CSD2.2}
\]
which also proves continuity after any fixed number of derivatives.

For compactly supported forms put
\[
K(P\,dx+Q\,dy)=H_xP,
\]
\[
K(G\,dx\wedge dy)=H_xG\,dy-\rho_x(x)H_y(I_xG)(y)\,dx,
\qquad K|_{\mathcal E_c^0}=0.
\tag{CSD2.3}
\]
Each output is supported in a fixed rectangle determined by the input support and the two fixed bumps. Thus these are continuous operators on the stated inductive limits. Direct differentiation gives
\[
Kd f=f,\qquad dK\omega+Kd\omega=\omega\quad(\deg\omega=1),
\]
\[
dK\omega=\omega-\rho_x\rho_y\,dx\wedge dy
\int_{\mathbb R^2}\omega\quad(\deg\omega=2).
\tag{CSD2.4}
\]
Indeed \(\partial_xH_xf=f-\rho_xI_xf\) and \(H_y\partial_yg=g\) for compactly supported \(g\) give every term in these identities. The bump two-form has positive integral one and is annihilated by \(K\). This is a continuous contraction onto \(A\) in degree two. An orientation-preserving disk-to-plane diffeomorphism transfers it to every disk below.

On the cylinder \(t=\log|z|\), \(\theta=\arg z\), combine the one-dimensional compact contraction in \(t\) with the following circle homotopy: subtract the angular mean, integrate that mean-zero coefficient from zero to \(\theta\), then subtract the mean of the primitive. Its derivative is the original coefficient minus its mean and it is periodic. The surviving circle classes are constants and \(d\theta/(2\pi)\). The compact cylinder classes are consequently
\[
\rho(t)\,dt\quad(\deg1),\qquad
\rho(t)\,dt\wedge\frac{d\theta}{2\pi}\quad(\deg2),\qquad \int\rho=1.
\tag{CSD2.5}
\]
All homotopies are continuous and use actual test forms, not an unproved homotopy-invariance assertion for topological coefficients.

## CSD3. The continuous-current sheaf

For \(-2\le n\le0\), define
\[
\mathscr T_A^n(U)=\bigl(\mathcal E_c^{-n}(U;A)\bigr)',
\qquad (dT)(\phi)=(-1)^{n+1}T(d\phi).
\tag{CSD3.1}
\]
Other degrees vanish. Each dual may carry the weak topology of pointwise evaluation or the strong topology of uniform convergence on bounded test sets. Both use exactly the same continuous functionals.

Restriction is transpose to extension by zero. To prove the sheaf axiom, decompose a compactly supported test form by a locally finite subordinate partition of unity and evaluate compatible local functionals on its pieces. Only finitely many terms meet the compact support. Compatibility proves independence of the partition and uniqueness; continuity on every fixed-support space proves continuity on the specified inductive limit. Restriction and scalar multiplication of currents are continuous for both dual topologies: they transpose continuous operations on tests which take bounded sets to bounded sets.

The differential is the continuous Hom differential, so \(d^2=0\). Smooth functions multiply currents on their test argument, making every term a fine sheaf. This gives ordinary-section acyclicity on all opens used below.

The positive complex orientation defines
\[
\underline{A'}_Y[2]\longrightarrow\mathscr T_A^\bullet,\qquad
c_\lambda(\phi)=\int_U\lambda(\phi)
\quad(\phi\text{ a compactly supported two-form}).
\tag{CSD3.2}
\]
It is continuous and closed by Stokes. Transpose the explicit contraction (CSD2.4): this proves that (CSD3.2) is a local quasi-isomorphism with continuous inverse on cohomology. In particular its coefficient is the entire continuous \(A'\). The weak-topology comparison is a homeomorphism. For this local coefficient the strong-topology comparison also follows from the two explicit bounded-set preserving test maps.

No tensor-product identification between scalar distributions and \(A'\) is used. Currents mean exactly (CSD3.1). At a pole define the positive Dirac current
\[
\delta_p\lambda(f)=\lambda(f(p)),\qquad i_*A'\longrightarrow\mathscr T_A^0.
\tag{CSD3.3}
\]
This is the actual local Gysin chain map, with its orientation fixed below.

## CSD4. The actual support-dual complex

Using the ordinary cone differential \(d(b,a)=(d_Bb+ga,-d_Aa)\), put
\[
\boxed{\mathscr D_c\mathscr F
=\operatorname{Cone}\!\left(i_*A'^2
\xrightarrow{(\delta,-r')}
\mathscr T_A^\bullet\oplus i_*V'\right).}
\tag{CSD4.1}
\]
The domain is in degree zero. Its complete terms and maps are
\[
(\mathscr D_c\mathscr F)^{-2}=\mathscr T_A^{-2},\qquad
(\mathscr D_c\mathscr F)^{-1}=\mathscr T_A^{-1}\oplus i_*A'^2,\qquad
(\mathscr D_c\mathscr F)^0=\mathscr T_A^0\oplus i_*V',
\]
\[
d^{-2}T=(dT,0),\qquad
d^{-1}(T,\lambda_+,\lambda_-)
=\left(dT+\delta_0\lambda_++\delta_\infty\lambda_-,
-r_+'\lambda_+,-r_-'\lambda_-\right).
\tag{CSD4.2}
\]
Every map is continuous for both dual topologies.

The cone is the literal continuous transpose of the compact-support resolution: for every open \(U\),
\[
\boxed{\Gamma(U,\mathscr D_c\mathscr F)
=\bigl(\Gamma_c(U,\mathscr K^\bullet)\bigr)^\vee,\qquad
(C^\vee)^n=(C^{-n})',\quad
d^\vee_n=(-1)^{n+1}(d_C^{-n-1})'.}
\tag{CSD4.3}
\]
For degree \(-1\), transposing \(d^0(f,v)\) gives
\(T(df)+\sum_p\lambda_p(f(p)-r_pv_p)\), exactly (CSD4.2). Degree \(-2\) has the minus sign in (CSD3.1). Restriction in (CSD4.3) is adjoint to extension by zero.

Evaluation is a cochain pairing: its two differential contributions are
\((-1)^{n+1}\lambda(dc)\) and \((-1)^n\lambda(dc)\), whose sum is zero. Formula (CSD4.3), together with the proved compact-support resolution, is the precise continuous support-duality meaning used here. It is an actual sheaf complex, not a declaration that general continuous dualization is exact.

Using (CSD3.2), it represents the candidate
\[
\operatorname{Cone}\bigl(i_*A'^2
\xrightarrow{(\mathrm{Gys},-r')}
\underline{A'}_Y[2]\oplus i_*V'\bigr),
\tag{CSD4.4}
\]
whose derived Gysin arrow is represented exactly by (CSD3.3).

## CSD5. Pole stalk and original compact-support pairing

Use the positive local coordinate \(z_p=z\) at zero and \(z_p=1/z\) at infinity. The form
\[
\vartheta_p=\frac{d\arg z_p}{2\pi}
\tag{CSD5.1}
\]
is locally integrable. Its degree-minus-one current is
\(h_p\lambda(\phi)=\int\vartheta_p\wedge\lambda(\phi)\).
The local \(1/r\) coefficient is integrable against the area factor \(r\,dr\,d\theta\). Stokes on a punctured disk with compact test \(f\) gives
\[
d(h_p\lambda)(f)=h_p\lambda(df)=\lambda(f(p)),
\qquad dh_p\lambda=\delta_p\lambda.
\tag{CSD5.2}
\]
The positive small-circle limiting integral fixes the sign.

The primal pole costalk is
\(L_p=[V_p\xrightarrow{r_p}A\xrightarrow0 A]\) in degrees \(0,1,2\).
Its dual differential is \(r_p'\) in degrees \(-1,0\). The actual stalk comparison is
\[
\begin{array}{c|c}
\text{degree}&L_p^\vee\longrightarrow(\mathscr D_c\mathscr F)_p\\ \hline
-2&\lambda\mapsto c_\lambda\\
-1&\mu\mapsto(h_p\mu,-\mu)\\
0&\nu\mapsto(0,\nu).
\end{array}
\tag{CSD5.3}
\]
Indeed \(d(h_p\mu,-\mu)=(0,r_p'\mu)\). The local current contraction leaves only \(A'\) in degree \(-2\); the Dirac arrow is locally null-homotopic through \(h_p\), leaving exactly \(r_p'\). This proves the quasi-isomorphism with continuous maps. The same construction on shrinking disks gives the actual stalk.

For a direct pairing check choose \(\chi\in C_c^\infty\) equal to one near \(p\), and a compact positive two-form \(\omega_c\) of integral one. The primal compact-source chain map is
\[
L_p\longrightarrow\Gamma_c(U,\mathscr K),\quad
v\mapsto(\chi r_pv,v),\quad
a\text{ in degree1}\mapsto(d\chi\,a,0),\quad
a\text{ in degree2}\mapsto\omega_c a.
\tag{CSD5.4}
\]
Its differential is \(r_p\). The compact contraction (CSD2.4) followed by elimination of the evaluation coordinate proves it is a quasi-isomorphism. Pairing it with (CSD5.3) gives
\[
\lambda(a),\qquad
\int\vartheta_p\wedge d\chi\,\mu(a)=\mu(a),\qquad
\nu(v).
\tag{CSD5.5}
\]
The middle identity is (CSD5.2) on test \(\chi\). This is precisely CDI's positive-orientation costalk pairing.

For clarity about the cohomology topology, on each fixed disk \(U\), transposing the compact-test map (CSD5.4) gives a continuous reverse chain map from sections of the current complex on that disk. It is not an evaluation of an arbitrary current germ on a fixed test support. In degrees \(-2,-1,0\) it is
\[
T\mapsto\bigl(a\mapsto T(\omega_c a)\bigr),\qquad
(T,\lambda)\mapsto\bigl(a\mapsto T(d\chi\,a)\bigr),
\]
\[
(T,\nu)\mapsto\nu+r_p'\bigl(a\mapsto T(\chi a)\bigr).
\tag{CSD5.7}
\]
It composes with the disk version of (CSD5.3) to the identity. Because that map is already a quasi-isomorphism, the induced cohomology maps are inverse continuous maps. Their cohomology identifications agree under shrinking disks: degree-minus-two cocycles are constant currents; for a degree-minus-one cocycle \((T,\lambda)\), the equation \(dT+\delta_p\lambda=0\) gives \(T(d\chi\,a)=-\lambda(a)\), independent of the cutoff; and degree-zero cutoff changes lie in \(\operatorname{im}r_p'\). The underlying sheaf stalk therefore has these groups. Its cohomology topology in this proof means the stable small-disk cohomology topology, identified by these identity transition maps. It is not a claim that arbitrary locally convex inductive limits of germs commute with forming cohomology topologies. This gives the precise topological comparison for both stated dual topologies before identifying the quotient coefficient through SDT below.

Consequently
\[
H^{-2}(i_p^*\mathscr D_c\mathscr F)=A',\quad
H^{-1}(i_p^*\mathscr D_c\mathscr F)=Q',\quad
H^0(i_p^*\mathscr D_c\mathscr F)=E_p'.
\tag{CSD5.6}
\]
The middle identification is \(\ker r_p'=J^\perp=q'Q'\). The last uses the actual splitting \(V_p=E_p\oplus J\) from \(\Sigma^{-1}\), and Hahn–Banach extends every continuous functional on closed \(J\) to \(A\). Thus these are the entire continuous duals.

## CSD6. Derived point support, computed separately

Fineness does not make a current sheaf automatically acyclic for support at a point. A current on a punctured disk need not extend across its missing point. Compute support by the actual restriction fibre cone
\[
R\Gamma_{\{p\}}(U,\mathscr D_c\mathscr F)
=\operatorname{Cone}\bigl(
\Gamma(U,\mathscr D_c\mathscr F)\to
\Gamma(U\setminus\{p\},\mathscr D_c\mathscr F)\bigr)[-1].
\tag{CSD6.1}
\]
The ordinary sections here compute hypercohomology because the displayed terms are fine. They are not replaced by termwise point-supported currents.

On a disk the current complex has \(A'\) in degree \(-2\). On its puncture it has \(A'\) in degrees \(-2,-1\), represented by \(c_\lambda,h_p\lambda\), by the cylinder contraction (CSD2.5). In particular \(h_p\lambda\) pairs as \(-\lambda(a)\) with \(\rho(t)dt\,a\), since \(d\theta\wedge dt=-dt\wedge d\theta\). This radial sign is retained.

Restriction on (CSD5.3) is identity in degrees \(-2,-1\) and zero in degree zero. In the fibre-cone convention \(d(x,y)=(dx,\mathrm{res}(x)-dy)\), cancel its contractible degree-minus-two pair. The remaining complex is
\[
A'\longrightarrow V_p'\oplus A',\qquad
\mu\longmapsto(r_p'\mu,\mu).
\tag{CSD6.2}
\]
The last coordinate records the punctured angular current. The positive supported coordinate is its negative: in the same cone,
\(d(h_p\lambda,0)=(\delta_p\lambda,h_p\lambda)\),
so \((\delta_p\lambda,0)\) is cohomologous to \((0,-h_p\lambda)\).
Changing to that positive supported coordinate and negating the source rewrites (CSD6.2) as
\[
A'\xrightarrow{\lambda\mapsto(\lambda,-r_p'\lambda)}
A'\oplus V_p'\quad\text{in degrees }-1,0.
\tag{CSD6.3}
\]
The first target is now measured by the positive Dirac orientation.

The continuous deformation retraction onto \(V_p'[0]\) is
\[
P(a,\nu)=\nu+r_p'a,\qquad S(\nu)=(0,\nu),\qquad h(a,\nu)=a.
\tag{CSD6.4}
\]
One has \(PS=1\), \(hd=1\) on degree \(-1\), and
\(dh(a,\nu)=(a,-r_p'a)=(a,\nu)-SP(a,\nu)\). Therefore
\[
\boxed{i_p^!\mathscr D_c\mathscr F\simeq V_p'[0]
=(i_p^*\mathscr F)^\vee.}
\tag{CSD6.5}
\]
Costalk-to-stalk is \(\nu\mapsto(0,\nu)\) in (CSD5.3); on degree-zero cohomology it is restriction \(V_p'\to E_p'\). Together with CSD5 this proves both support/stalk comparisons from actual local complexes.

## CSD7. Global angular current and the CDI chain comparison

The angular form \(\vartheta=d\arg z/(2\pi)\) is locally integrable on the sphere. At infinity it is \(-\vartheta_-\); hence
\[
d(\vartheta\lambda)=\delta_0\lambda-\delta_\infty\lambda.
\tag{CSD7.1}
\]
The original global complex and its continuous dual are
\[
D=[V_+\oplus V_-\xrightarrow{r_+-r_-}A\xrightarrow0 A],
\]
\[
D^\vee=[A'\xrightarrow0 A'
\xrightarrow{\mu\mapsto(r_+'\mu,-r_-'\mu)}
V_+'\oplus V_-']
\tag{CSD7.2}
\]
in degrees \(0,1,2\) and \(-2,-1,0\), respectively. There is an actual continuous chain map
\[
\Psi:D^\vee\longrightarrow\Gamma(Y,\mathscr D_c\mathscr F),
\]
\[
\lambda\mapsto c_\lambda\quad(\deg-2),\qquad
\mu\mapsto(\vartheta\mu;-\mu,+\mu)\quad(\deg-1),\qquad
(\nu_+,\nu_-)\mapsto(0;\nu_+,\nu_-)\quad(\deg0).
\tag{CSD7.3}
\]
The middle differential's current terms cancel by (CSD7.1), leaving precisely \((r_+'\mu,-r_-'\mu)\).

To prove this is a quasi-isomorphism, compute the global current complex using the local and cylinder contractions (CSD2.4)–(CSD2.5) and two-chart Mayer–Vietoris. Its cohomology is \(A'\) in degrees \(-2,0\) and zero in degree \(-1\). The first class is \(c_\lambda\); the last is evaluated on constant test functions. Both positive Dirac currents have that last value \(\lambda\). All comparisons are finite sums, the written integral operators and partition-of-unity maps, so they are continuous. This computes the current cohomology without assuming arbitrary exactness of continuous dualization.

The cone then has the finite model
\[
P^{-2}=A',\quad P^{-1}=A'^2,\quad
P^0=A'\oplus V_+'\oplus V_-',
\]
\[
d^{-1}(\lambda_+,\lambda_-)
=(\lambda_++\lambda_-,-r_+'\lambda_+,-r_-'\lambda_-).
\tag{CSD7.4}
\]
Its explicit deformation retraction is
\[
\begin{array}{c|c|c}
\text{degree}&P\to D^\vee&D^\vee\to P\\ \hline
-2&1&1\\
-1&(\lambda_+,\lambda_-)\mapsto-\lambda_+&
\mu\mapsto(-\mu,\mu)\\
0&(a,\nu_+,\nu_-)\mapsto(\nu_+,\nu_-+r_-'a)&
(\nu_+,\nu_-)\mapsto(0,\nu_+,\nu_-).
\end{array}
\tag{CSD7.5}
\]
The homotopy \(h^0(a,\nu_+,\nu_-)=(0,a)\) satisfies \(dh+hd=1-SP\); substitute into (CSD7.4) to check both degrees. The current map (CSD7.3) induces the section in (CSD7.5), proving its quasi-isomorphism.

There is also a direct pairing check. Set
\[
\omega_Y=\frac1\pi\frac{dx\wedge dy}{(1+|z|^2)^2},\qquad \int_Y\omega_Y=1.
\]
The primal finite complex maps into global sections of \(\mathscr K\) by
\[
(v_+,v_-)\mapsto
(\operatorname{constant}(r_-v_-),v_+,v_-),\quad
b\text{ in degree1}\mapsto(0;-b,0),\quad
a\text{ in degree2}\mapsto\omega_Ya.
\tag{CSD7.6}
\]
Its differential is \(r_+-r_-\), including the displayed degree-one minus. Pairing (CSD7.3) and (CSD7.6) gives the original evaluation in every degree. Thus this realizes CDI's pairings and signs, not only its cohomology groups.

The continuous transpose of (CSD7.6) is an explicit cohomological inverse to (CSD7.3). Put \(\ell_T(a)=T(\operatorname{constant}(a))\) for a degree-zero current. In degrees \(-2,-1,0\), this reverse chain map is
\[
T\mapsto\bigl(a\mapsto T(\omega_Ya)\bigr),\qquad
(T,\lambda_+,\lambda_-)\mapsto-\lambda_+,
\]
\[
(T,\nu_+,\nu_-)\mapsto(\nu_+,\nu_-+r_-'\ell_T).
\tag{CSD7.8}
\]
For degree \(-1\), its chain identity is
\((-r_+'\lambda_+,r_-'\lambda_+)=d_{D^\vee}(-\lambda_+)\).
It composes with \(\Psi\) to the identity in every degree. All test embeddings in this formula are continuous and take bounded sets to bounded sets. Therefore the induced inverse cohomology maps are continuous for both weak and strong dual topologies. No theorem that continuous dualization preserves arbitrary quasi-isomorphisms is used to prove this assertion.

In particular
\[
H^{-2}(Y,\mathscr D_c\mathscr F)=A',\qquad
H^{-1}(Y,\mathscr D_c\mathscr F)=Q',\qquad
H^0(Y,\mathscr D_c\mathscr F)=Z',
\]
\[
Z=\{(v_+,v_-):r_+v_+=r_-v_-\}\simeq J\oplus E_+\oplus E_-.
\tag{CSD7.7}
\]
The last comparison uses the original Fourier-source inverse and retains all four endpoint lines.

## CSD8. Restriction realizes the transposed support map

Restriction of the global angular current is \(h_+\) at zero and \(-h_-\) at infinity. Thus (CSD7.3) and (CSD5.3) give exactly
\[
D^\vee\to L_+^\vee:
\quad(\deg0,\deg-1,\deg-2)=(\operatorname{pr}_{V_+'},+1,+1),
\]
\[
D^\vee\to L_-^\vee:
\quad(\deg0,\deg-1,\deg-2)=(\operatorname{pr}_{V_-'},-1,+1).
\tag{CSD8.1}
\]
These are the transposes of the original support-to-global map
\[
L_+\oplus L_-\to D,\quad
k^0=1,\quad k^1(b_+,b_-)=b_+-b_-,\quad k^2(c_+,c_-)=c_++c_-.
\tag{CSD8.2}
\]
Consequently degree-minus-one is anti-diagonal and degree-minus-two diagonal:
\[
Q'\to Q'^2:\mu\mapsto(\mu,-\mu),\qquad
A'\to A'^2:\lambda\mapsto(\lambda,\lambda).
\tag{CSD8.3}
\]
Degree zero is endpoint restriction \(Z'\to E_+'\oplus E_-'\).

The complete cone comparison is
\[
\operatorname{Cone}(k)^\vee
\longrightarrow\operatorname{Cone}(k^\vee)[-1],\qquad
(\phi,\psi)\mapsto((-1)^{n+1}\psi,\phi)\text{ in degree }n.
\tag{CSD8.4}
\]
Substitution into the Hom and shifted-cone differentials proves it is a chain isomorphism. The dual long row is therefore the full CDI5 row
\[
0\to A'\xrightarrow{\Delta}A'^2
\xrightarrow{-\lambda_++\lambda_-}A'
\xrightarrow0Q'\xrightarrow{(\mu,-\mu)}Q'^2
\xrightarrow{q'(\mu_++\mu_-)}A'
\xrightarrow{r'}Z'\to E_+'\oplus E_-'\to0.
\tag{CSD8.5}
\]
Here \(r:Z\to A\) is common restriction and \(r'\lambda=(\lambda|_J,0,0)\) in (CSD7.7). Diagonal/difference identities and Hahn–Banach on \(J\subset A\) prove exactness. Thus the earlier continuous coefficient duality has an actual sheaf support construction realizing its maps.

The ordinary annular dual in (CSD8.4) has degrees \(-1,0\). It is not confused with \(R\Gamma(\mathbb C^\times,\mathscr T_A)\), whose degrees are \(-2,-1\) because it is dual to compactly supported annular cohomology. Formula (CSD4.3) specifies the support convention.

## CSD9. Proper geometric transposes and both mirrors

A continuous coefficient-diagram map acts on compact tests and, contravariantly, on this current complex. All evaluation comparisons are natural for these actual transposes.

For a recovered positive integer \(n\), \(b_n(z)=z^n\) is proper. Hence test pullback preserves compact supports and its transpose defines
\[
(b_{n*}T)(\phi)=T(b_n^*\phi).
\tag{CSD9.1}
\]
After including the transposed coefficient action, this is the proper current pushforward \(b_{n*}\mathscr D_c\mathscr F\to\mathscr D_c\mathscr F\), adjoint to primal pullback. It is not pullback on the dual object and is not an inverse root map.

The primal coefficient action is
\[
T_ab(u)=b(u/a),\quad
\rho_+(a)(f,c_0,c_1)=(f(\cdot/a),c_0,ac_1),\quad
\rho_-(a)(h,d_0,d_1)=(ah(a\,\cdot),ad_0,d_1).
\tag{CSD9.2}
\]
The current transpose uses \(T_n'\) and \(\rho_\pm(n)'\). Under (CSD7.3) its complete finite-model action is
\[
(nT_n',\,T_n',\,\rho_+(n)'\oplus\rho_-(n)')
\quad\text{in degrees }-2,-1,0.
\tag{CSD9.3}
\]
For a direct check, \(b_{n*}c_\lambda=nc_\lambda\), \(b_{n*}\vartheta=\vartheta\), and \(b_{n*}\delta_p=\delta_p\). On the punctured receiver the \(n\) inverse branches each contribute \(1/n\) of the angular form to its trace. The locally integrable current equality extends across the poles. These calculations verify the precise current/global comparison. The broader geometric trace with other coefficient conventions is a separate receiver map, not identified with this one by terminology.

The specified mirrors and their sphere orientation degrees are
\[
w(z)=-1/z,\quad\varepsilon_w=+1;\qquad
\alpha(z)=-1/\overline z,\quad\varepsilon_\alpha=-1.
\tag{CSD9.4}
\]
Both transpose the pole swap and use \(R'\). For a current represented by a form, proper pushforward acts as \(\varepsilon_g(g^{-1})^*\) because the integration orientation is fixed. Thus
\[
g_*c_\lambda=\varepsilon_gc_\lambda,\qquad
g_*\vartheta=-\vartheta\quad(g=w,\alpha),
\tag{CSD9.5}
\]
using \(w^*\vartheta=-\vartheta\), \(\alpha^*\vartheta=+\vartheta\).
The global dual actions are exactly
\[
(\varepsilon_gR',-R',\text{dual pole swap})
\quad\text{in degrees }-2,-1,0.
\tag{CSD9.6}
\]
At pole stalks each angular current uses its own positive coordinate. Degree minus one is \(+R'\) with pole swap, while degree minus two is \(\varepsilon_gR'\) with swap. Hence (CSD8.1) intertwines the mirrors with all CDI7 signs.

The coefficient contragredient giving an invariant pairing is different. On the already constructed cohomological representation extended to \(a>0\), it is
\[
(a^{-1}(T_{a^{-1}})',\ (T_{a^{-1}})',\
\rho_+(a^{-1})'\oplus\rho_-(a^{-1})').
\tag{CSD9.7}
\]
It satisfies \(\langle B_a^\vee\lambda,B_ax\rangle=\langle\lambda,x\rangle\).
This is CDI6's inverse-parameter coefficient operation. It is not asserted to arise from a holomorphic \(z^{1/a}\) and is not substituted for (CSD9.1).

There is now also a separately constructed weighted trace on the primal sheaf. GTR2 uses the sum over all \(n\) interior sheets and \(n\) times the identity on each ramified pole space, including both endpoint coordinates. It proves \(\operatorname{Tr}_n b_n^*=n\,1\) on that sheaf. GTR3–GTR4 prove its global degree factors \((n,n,1)\), and, after composing with the inverse coefficient action, the representative
\[
\mathsf U_n=(n\rho(n^{-1}),\,nT_{n^{-1}},\,T_{n^{-1}}),
\qquad
\mathsf U_n\mathsf B_n=\mathsf B_n\mathsf U_n=n\,1
\tag{CSD9.8}
\]
in primal degrees \(0,1,2\), where \(\rho=\rho_+\oplus\rho_-\).
Its transpose on the full coefficient dual consequently is
\[
\mathsf U_n'
=(T_{n^{-1}}',\,nT_{n^{-1}}',\,n\rho(n^{-1})')
=n(\mathsf B_n^{-1})'
\tag{CSD9.9}
\]
in degrees \(-2,-1,0\). These are the induced maps and the explicitly constructed coefficient representative from GTR, not a claim that a chain lift to currents is uniquely determined by its cohomology. In particular the middle operator \(nT_{n^{-1}}'\) in (CSD9.9) is different from \(T_n'\) in the current pushforward (CSD9.3). GTR5 proves that the original reflected residue map intertwines the former operator. The current support-duality comparison keeps these maps distinct and retains the ramification factor.

## CSD10. Topologies and the proved extent of duality

Every current and functional is continuous for the actual Fréchet and compact-test topologies. The comparisons use explicit integrations, cutoffs and continuous finite operations. Exactness of continuous dualization for arbitrary locally convex complexes has not been assumed.

The weak-dual cohomology topologies are precisely CDI3's. The annihilator \(J^\perp\subset A'\) has the weak topology of \(Q'\): evaluation at \(a\) is evaluation at \(q(a)\), and every quotient vector has a representative. The actual continuous decompositions \(V_p=E_p\oplus J\) and \(V_+\oplus V_-=Z\oplus J\) transpose to finite decompositions, identifying the degree-zero quotient topologies. The current homotopies and comparison maps preserve those identifications. All these pairings are separated and involve the entire continuous dual.

For strong duals every displayed map remains continuous. The induced topology on \(Q'\subset A'_\beta\) initially has the seminorm family
\[
\mu\longmapsto\sup_{a\in B}|\mu(q(a))|,
\qquad B\subset A\text{ bounded}.
\tag{CSD10.1}
\]
The accepted SDT2–SDT5 proof now identifies this family with the full strong topology of \(Q'\). It proves compact closure of every bounded subset of \(Q\) using the original two-sided weighted derivative bounds, then constructs a compact lift through \(q\) as a uniformly convergent series of finite choices. Intersecting that compact lift with the inverse image of a bounded subset \(B\subset Q\) gives a bounded set \(\widetilde B\subset A\) with \(q(\widetilde B)=B\). Hence
\[
\sup_{y\in B}|\mu(y)|=\sup_{a\in\widetilde B}|q'\mu(a)|,
\qquad
Q'_\beta\xrightarrow[\ q'\ ]{\ \sim\ }J^\perp\subset A'_\beta.
\tag{CSD10.2}
\]
Conversely, continuous \(q\) takes bounded subsets of \(A\) to bounded subsets of \(Q\), giving the other topology inclusion.

The finite source splittings used above give the strong topology on the degree-zero groups, and the fixed-test maps (CSD5.7) and (CSD7.8) identify the current cohomology topologies with those of the finite coefficient complexes. Thus the global identifications are strong topological isomorphisms with \(A'_\beta,Q'_\beta,Z'_\beta\). The pole stalk groups, equipped with the stable small-disk cohomology topology specified in CSD5, are strongly topologically isomorphic to \(A'_\beta,Q'_\beta,E_p'{}_\beta\). The supported comparison (CSD6.4) uses continuous finite operations on the local restriction cone and gives \(V_p'{}_\beta\) with the analogous stable local topology. This imports exactly SDT's proved bounded-lift result; it does not assume or assert strong openness of the separate restriction \(A'_\beta\to J'_\beta\).

Ordinary algebraic sheaf Hom is not invoked to turn these continuous duals into algebraic duals. The exact support-dual object established here is (CSD4.1), with test-functional characterization (CSD4.3) and its proved local/global comparisons.

## CSD11. Original zeta and every coefficient contribution

Neither \(A\) nor its original source \(J\) has changed. Retain
\[
\Theta a(s)=\frac12\int_0^\infty a(u)u^s\,\frac{du}{u},\qquad
\mathcal M_0\Sigma f(s)=2\zeta(s)\int_0^\infty f(v)v^s\,\frac{dv}{v}
\quad(\Re s>1).
\tag{CSD11.1}
\]
For \(f_0(v)=\frac\pi2v^2(2\pi v^2-3)e^{-\pi v^2}\),
\[
\Theta\Sigma f_0(s)=F_0(s)
=\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2)\zeta(s).
\tag{CSD11.2}
\]
The endpoint values \(F_0(0)=F_0(1)=1/8\) and all trivial-zero comparisons remain
\[
F_0(-2r)=\frac{r(2r+1)(-1)^r\pi^r}{2\,r!}\zeta'(-2r)
=\frac{(1+2r)(2r)}8\pi^{-(1+2r)/2}
\Gamma((1+2r)/2)\zeta(1+2r),\quad r\ge1.
\tag{CSD11.3}
\]
The complete inverse and these contributions are proved in SSI/ESI and retained in CSP11/CDW10.

For \(\mathcal B\), the entire functions rapidly decreasing on every bounded real strip, let
\[
\mathcal I=\{F\in\mathcal B:F^{(j)}(\rho)=0
\text{ for every actual nontrivial zero }\rho,\ 0\le j<m_\rho\}.
\]
The proved map is the topological isomorphism
\(\kappa:Q\to\mathcal Q=\mathcal B/\mathcal I\),
\(\kappa([a])=[\Theta a]\), with \(\Theta J=\mathcal I\). Its actual continuous transpose is
\[
\kappa':\mathcal Q'\to Q',\qquad
(\kappa'\lambda)([a])=\lambda([\Theta a]).
\tag{CSD11.4}
\]
Thus the factor \(1/2\) has not disappeared in duality. Every jet
\(\delta_{\rho,j}([a])=(\Theta a)^{(j)}(\rho)\)
is a continuous element of the \(Q'\) in CSD5 and CSD7. Its entire transpose matrix is
\[
T_a'\delta_{\rho,j}
=a^\rho\sum_{\ell=0}^j\binom j\ell
(\log a)^{j-\ell}\delta_{\rho,\ell}.
\tag{CSD11.5}
\]
For the normal contragredient the scalar is \(a^{-\rho-1}\) and each logarithm is \(-\log a\), as in CDI6.8. Every multiplicity is retained without presuming a location inside the known open critical strip.

The notation in (CSD11.5) uses raw derivatives. GTR and RD also use Taylor-coefficient functionals. Their exact comparison is
\[
\delta_{\rho,j}^{\mathrm{raw}}
=j!\,\delta_{\rho,j}^{\mathrm{Taylor}},
\qquad
\delta_{\rho,j}^{\mathrm{Taylor}}([a])
=\frac{(\Theta a)^{(j)}(\rho)}{j!}.
\tag{CSD11.6}
\]
In that latter basis the actual transfer transpose from (CSD9.9) is
\[
\mathsf U_n'\delta_{\rho,j}^{\mathrm{Taylor}}
=n^{1-\rho}\sum_{h=0}^j
\frac{(-\log n)^{j-h}}{(j-h)!}
\delta_{\rho,h}^{\mathrm{Taylor}}.
\tag{CSD11.7}
\]
Multiplying by \(j!\) gives the raw-derivative formula with \(\binom jh\). Thus the factorials, inverse parameter and ramification factor are all explicit in the comparison to GTR.

This construction does not promote the finite-residue identification to a topological self-duality of all \(Q\), replace \(J\) by \(Q\), or infer positivity of a Hermitian form from separated evaluation.

## CSD12. Constructed support-duality result

The actual sheaf complex (CSD4.1) is the continuous current dual of the compact-support resolution. Its Gysin and endpoint arrow is \((\delta,-r')\). The local angular current and restriction fibre cone prove
\[
i_p^*\mathscr D_c\mathscr F\simeq(i_p^!\mathscr F)^\vee,\qquad
i_p^!\mathscr D_c\mathscr F\simeq(i_p^*\mathscr F)^\vee.
\]
The global chain map (CSD7.3) realizes CDI's entire continuous dual of the original sphere complex. Its restrictions give the full diagonal and anti-diagonal support maps. Proper cover transposes and both actual mirrors retain their degree and orientation factors.

This proves continuous support duality for the specified receiver. It assigns no operation to \(\tau\), introduces no finite-dimensional coefficient replacement, and asserts no RH or Deligne-purity conclusion.
