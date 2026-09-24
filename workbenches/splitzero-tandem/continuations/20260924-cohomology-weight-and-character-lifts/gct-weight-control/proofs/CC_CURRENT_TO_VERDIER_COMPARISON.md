# From literal continuous currents to the ordinary Verdier cone

Complete independent derivation and operator audit, 24 September 2026. Locators CV0–CV9.

## CV0. Exact inputs and scope

The supporting datum remains \(\tau\langle Z_1;\mathrm{no}\ Z_2\rangle\). This calculation acts on the already reconstructed coefficient spaces and the sphere receiver; it puts no coordinate, metric, addition or scalar operation on \(\tau\). The source stage, full-history requirement, retracted addition and correction precedence remain those recalled in CSD0. Neither the source \(J\) nor its quotient \(Q\) is replaced.

The accepted CC_CONTINUOUS_SUPPORT_DUAL_SHEAF.md, CSD0–CSD12, is retained unchanged at SHA256 361a5798405cc6688f8ea249f2bdfb05c1eb9b67499b52cfc27f6a2bade5579c. For this continuation the complete VSD1–VSD8 and VSD13 were read, together with their coefficient definitions in VSD0, in CC_VERDIER_SUPPORT_INDEPENDENT.md, SHA256 a49fccbe2773e6d6378aceb394273e734f2ca206f4d6d787500927a1f6280d2b. The source identity and original-author reading coverage remain CSD0 and VSD0; this is a new local construction, not a new reading of the complete human papers.

Write \(E'\) for continuous complex-linear functionals, \(E^*=\operatorname{Hom}_{\mathbb C}(E,\mathbb C)\) for all algebraic functionals, and \(E^\dagger=E^*/E'\) as a vector space. No topology is imposed on a discontinuous functional or on this quotient. The objective is a literal morphism of sheaf complexes, and then a verification of VSD13's rational-operator comparison.

## CV1. The original sheaf and its compact tests

Retain \(Y=\mathbb P^1(\mathbb C)\), \(P=\{0,\infty\}\), \(i:P\hookrightarrow Y\), and
\[
S=\{f\in\mathcal S(\mathbb R;\mathbb C):f(-v)=f(v),\
f(0)=0,\ \int_{\mathbb R}f=0\},\qquad
V_\pm=S\oplus E_\pm,\quad E_\pm=\mathbb C^2,
\]
\[
A=\{a\in C^\infty(\mathbb R_{>0}):
\sup_{u>0}(u^N+u^{-N})|(u\partial_u)^ja(u)|<\infty
\text{ for all }N,j\ge0\},
\]
\[
\Sigma f(u)=2\sum_{k\ge1}f(ku),\quad
Ra(u)=u^{-1}a(u^{-1}),\quad
r_+(f,e)=\Sigma f,\quad r_-(h,e)=R\Sigma h=\Sigma\widehat h,
\tag{CV1.1}
\]
where \(\widehat h(t)=\int_{\mathbb R}h(v)e^{-2\pi ivt}\,dv\).
The source theorem proves \(J=\Sigma S\) closed, \(\Sigma:S\to J\) a topological isomorphism, and \(Q=A/J\) Fréchet. Both endpoint coordinates in each \(E_\pm\) are retained. With \(V=V_+\oplus V_-\),
\[
\mathscr F=\underline A_Y\times_{i_*A^2}i_*V,\qquad
0\to\mathscr F\to\underline A_Y\oplus i_*V
\xrightarrow{\mathrm{ev}-r}i_*A^2\to0.
\tag{CV1.2}
\]

Let \(\mathcal E_c^q(U;A)\) be compactly supported smooth \(A\)-valued \(q\)-forms, with the compact-support inductive-limit topology and the original coefficient seminorms. The single primal resolution is
\[
\mathscr K^0=\mathscr E_A^0\oplus i_*V,\quad
\mathscr K^1=\mathscr E_A^1\oplus i_*A^2,\quad
\mathscr K^2=\mathscr E_A^2,
\]
\[
d^0(f,v)=(df,\mathrm{ev}(f)-rv),\qquad d^1(\omega,a)=d\omega.
\tag{CV1.3}
\]
CSD1 constructs this resolution and its compact-support acyclicity. The continuous-current complex in that proof is
\[
\mathscr T_c^n(U)=\bigl(\mathcal E_c^{-n}(U;A)\bigr)',\qquad
dT=(-1)^{n+1}T\,d,\quad -2\le n\le0.
\tag{CV1.4}
\]

## CV2. Algebraic test currents really form a sheaf

Define on the same test spaces
\[
\mathscr T_a^n(U)=
\operatorname{Hom}_{\mathbb C}(\mathcal E_c^{-n}(U;A),\mathbb C),
\qquad dT=(-1)^{n+1}T\,d.
\tag{CV2.1}
\]
No continuity restriction is imposed. Restrictions transpose extension by zero, and \(d^2=0\).

For a cover of \(U\), choose a locally finite subordinate smooth partition \((\rho_i)\). Compatible local functionals act on a test form \(\phi\) by summing their values on \(\rho_i\phi\). Only finitely many terms meet the compact support of \(\phi\). For two partitions, refine by their products; compatibility equates the resulting finite sums. This proves existence, independence and uniqueness of gluing. No infinite summation is passed through an algebraic functional. Thus (CV2.1) is a sheaf.

It is fine: multiplication by a smooth scalar function acts on tests, and the associated locally finite partition endomorphisms add to the identity on every compact test by a finite sum. It is also flabby in the algebraic sheaf category. Indeed extension by zero embeds the test space of a smaller open as a vector subspace of that of a larger open; every linear functional on the subspace extends by a basis extension. This flabbiness is not asserted for the continuous-current sheaf.

The inclusion of continuous functionals gives a literal injective morphism of complexes
\[
\jmath:\mathscr T_c^\bullet\hookrightarrow\mathscr T_a^\bullet.
\tag{CV2.2}
\]
All statements about the target here are statements about vector-space sheaves, not continuity of discontinuous functionals.

## CV3. Integrate in the coefficient space before applying a functional

For \(\lambda\in A^*\), define the constant algebraic current by
\[
c_\lambda(\phi)=\lambda\!\left(\int_U\phi\right),
\qquad \phi\in\mathcal E_c^2(U;A).
\tag{CV3.1}
\]
The integral is first taken in the complete Fréchet space \(A\). The expression \(\int\lambda(\phi)\) is not used for discontinuous \(\lambda\).

Here is the local contraction underlying the assertion about its cohomology. In an oriented plane chart choose compact scalar bumps \(\rho_x,\rho_y\) of integral one, and define
\[
I_xf(y)=\int_{\mathbb R}f(x,y)\,dx,\qquad
H_xf(x,y)=\int_{-\infty}^xf(t,y)\,dt
-\left(\int_{-\infty}^x\rho_x(t)\,dt\right)I_xf(y).
\]
For compact forms put
\[
K(P\,dx+Q\,dy)=H_xP,\qquad
K(G\,dx\wedge dy)=H_xG\,dy-\rho_xH_y(I_xG)\,dx.
\tag{CV3.2}
\]
These are the continuous operators proved in CSD2. Their identities are identities in \(A\):
\[
Kd f=f,\quad dK+Kd=1\text{ in degree }1,\quad
dK\omega=\omega-\rho_x\rho_y\,dx\wedge dy\int\omega
\text{ in degree }2.
\tag{CV3.3}
\]
They follow directly from \(\partial_xH_xf=f-\rho_xI_xf\) and \(H_y\partial_yg=g\) for compact \(g\). All output supports stay in a fixed enlarged rectangle. Algebraic transposition preserves these identities because they are already identities of linear maps. Hence
\[
\underline{A^*}_Y[2]\xrightarrow[\lambda\mapsto c_\lambda]{\simeq}
\mathscr T_a^\bullet.
\tag{CV3.4}
\]
For continuous \(\lambda\), (CV3.1) equals CSD's continuous current. Thus the square with \(\underline{A'}[2]\to\mathscr T_c\) and (CV2.2) commutes literally.

In a positive local coordinate \(z_p\), define
\[
h_p\lambda(\phi)=
\lambda\!\left(\int\frac{d\arg z_p}{2\pi}\wedge\phi\right),
\qquad
\delta_p\lambda(f)=\lambda(f(p)).
\tag{CV3.5}
\]
The angular integral is an actual \(A\)-valued integral. Its coefficient \(1/r\) is locally integrable against area, and every coefficient seminorm is bounded on the compact test support. Truncated integrals converge in each seminorm, hence in \(A\). The \(A\)-valued Stokes identity is
\[
\int\frac{d\arg z_p}{2\pi}\wedge df=f(p).
\]
It is proved by the positive small-circle boundary limit in \(A\), before \(\lambda\) is applied. Therefore
\[
dh_p\lambda=\delta_p\lambda.
\tag{CV3.6}
\]
The positive compact form \(-d\chi\wedge d\arg z_p/(2\pi)\) has integral one when \(\chi=1\) near \(p\). As in CSD6, the restriction fibre cone identifies the class of \(\delta_p\lambda\) with the positive local fundamental class. Hence the chain map
\[
i_*A^*\xrightarrow{\delta_p}\mathscr T_a^\bullet
\tag{CV3.7}
\]
is exactly VSD2's positive Gysin map \(g_{p,A^*}\), not only an unspecified nonzero multiple of it.

## CV4. Literal comparison of the two complete cone complexes

Form the algebraic current cone
\[
\mathscr D_a\mathscr F=
\operatorname{Cone}\!\left(
i_*(A^*)^2\xrightarrow{(\delta,-r^*)}
\mathscr T_a^\bullet\oplus i_*V^*\right).
\tag{CV4.1}
\]
Its terms in degrees \(-2,-1,0\) are \(\mathscr T_a^{-2}\),
\(\mathscr T_a^{-1}\oplus i_*(A^*)^2\), and
\(\mathscr T_a^0\oplus i_*V^*\), with
\[
d^{-1}(T,\lambda_+,\lambda_-)
=\left(dT+\delta_0\lambda_++\delta_\infty\lambda_-,
-r_+^*\lambda_+,-r_-^*\lambda_-\right).
\tag{CV4.2}
\]
Its differential is exactly the algebraic Hom differential of \(\Gamma_c(U,\mathscr K)\) on each open. Every endpoint is still present.

To identify the target, VSD1's ordinary vector-sheaf calculation gives
\[
R\mathcal Hom(\underline E,\underline{\mathbb C}[2])
=\underline{E^*}[2],\qquad
R\mathcal Hom(i_*E,\underline{\mathbb C}[2])=i_*E^*.
\]
The first uses disk adjunction
\(\operatorname{Hom}(\underline E,K)=\operatorname{Hom}_{\mathbb C}(E,\Gamma K)\),
exactness of vector-space Hom, and vanishing of higher disk cohomology of the constant target. The second uses positive local support cohomology of that target and exact vector-space Hom at a point. Thus neither requires finite rank. Dualizing (CV1.2) gives the cone of the Gysin map and \(-r^*\). Equations (CV3.4)–(CV3.7) identify precisely those maps. Consequently
\[
\boxed{\mathscr D_a\mathscr F\simeq
R\mathcal Hom_Y(\mathscr F,\underline{\mathbb C}_Y[2])
=\mathbb D_Y\mathscr F.}
\tag{CV4.3}
\]

The inclusions of functionals now give an actual termwise injective chain map
\[
\boxed{c_{\mathrm{cur}}:\mathscr D_c\mathscr F
\hookrightarrow\mathscr D_a\mathscr F,}
\tag{CV4.4}
\]
using (CV2.2) on currents and \(A'\hookrightarrow A^*\), \(V'\hookrightarrow V^*\) at the poles. Its chain compatibility follows immediately from (CV4.2), including both minus signs. The constant-current comparison commutes with the coefficient inclusion, and the Dirac comparisons commute with the same inclusion. Under (CV4.3) this is the morphism \(c\) of VSD7. It is an actual map out of the fixed CSD complex.

## CV5. The literal quotient current sheaf and comparison defect

Let \(\mathscr T_\dagger^n=\mathscr T_a^n/\mathscr T_c^n\) as an ordinary quotient sheaf. For each open \(U\),
\[
\Gamma(U,\mathscr T_\dagger^n)
=
\operatorname{Hom}_{\mathbb C}(\mathcal E_c^{-n}(U;A),\mathbb C)
\big/\bigl(\mathcal E_c^{-n}(U;A)\bigr)'.
\tag{CV5.1}
\]
Indeed \(\mathscr T_c^n\) is fine on these paracompact opens, so its first cohomology vanishes. The sheaf exact sequence therefore gives exactness on sections at the quotient term. This also provides a direct gluing proof for (CV5.1), without declaring arbitrary presheaf quotients to be sheaves.

The local long exact sequence and (CV3.4) give
\[
\mathcal H^{-2}(\mathscr T_\dagger)=\underline{A^\dagger},
\qquad \mathcal H^{n\ne-2}(\mathscr T_\dagger)=0.
\]
There is a specified local quasi-isomorphism
\[
\underline{A^\dagger}[2]\longrightarrow\mathscr T_\dagger,
\qquad [\lambda]\longmapsto[c_\lambda].
\tag{CV5.2}
\]
It is well defined because a continuous coefficient yields a continuous current. The same observation defines \([\delta_p\lambda]\) and \([h_p\lambda]\). No integration in an unspecified topology on \(A^\dagger\) is required: choose a representative in \(A^*\), integrate in \(A\), apply it, and pass to the current quotient.

The quotient of (CV4.4) is consequently the actual complex
\[
\mathscr D_\dagger=
\operatorname{Cone}\!\left(
i_*(A^\dagger)^2\xrightarrow{(\delta^\dagger,-r^\dagger)}
\mathscr T_\dagger\oplus i_*V^\dagger\right).
\tag{CV5.3}
\]
The map \(\operatorname{Cone}(c_{\mathrm{cur}})\to\mathscr D_\dagger\) sends \((b,a)\) to the quotient class of \(b\). Its kernel is the cone of the identity of \(\mathscr D_c\), which contracts by \((b,a)\mapsto(0,b)\). Therefore it is a quasi-isomorphism. With (CV5.2), this proves
\[
\boxed{\operatorname{Cone}(c_{\mathrm{cur}})
\simeq\operatorname{Cone}\!\left(
i_*(A^\dagger)^2\xrightarrow{(g_{A^\dagger},-r^\dagger)}
\underline{A^\dagger}[2]\oplus i_*V^\dagger\right).}
\tag{CV5.4}
\]
This is exactly VSD8's comparison object, now obtained as a quotient of the literal current complexes. The quotient has no imposed topology.

## CV6. Exact support and global maps of the comparison

The CSD chain maps work algebraically with the integral-before-functional convention. At a pole the finite model is
\[
[A^*\xrightarrow0 A^*\xrightarrow{r_p^*}V_p^*]
\quad\text{in degrees }-2,-1,0,
\]
mapped into currents by
\[
\lambda\mapsto c_\lambda,\qquad
\mu\mapsto(h_p\mu,-\mu),\qquad
\nu\mapsto(0,\nu).
\tag{CV6.1}
\]
Its costalk is the positive Gysin cone
\[
A^*\xrightarrow{\lambda\mapsto(\lambda,-r_p^*\lambda)}
A^*\oplus V_p^*,
\]
contracting to \(V_p^*\) by \((a,\nu)\mapsto\nu+r_p^*a\). Restricting (CV6.1) to continuous functionals gives exactly CSD5–CSD6. Quotienting gives the dagger versions, with the same signs.

Globally the \(A\)-valued angular identity is
\[
d\vartheta=\delta_0-\delta_\infty,\qquad
\vartheta=\frac{d\arg z}{2\pi}.
\]
Thus
\[
[A^*\xrightarrow0 A^*\xrightarrow{(r_+^*,-r_-^*)}V^*]
\longrightarrow\Gamma(Y,\mathscr D_a\mathscr F)
\]
has the chain map
\[
\lambda\mapsto c_\lambda,\qquad
\mu\mapsto(\vartheta\mu;-\mu,+\mu),\qquad
(\nu_+,\nu_-)\mapsto(0;\nu_+,\nu_-).
\tag{CV6.2}
\]
The compact-test homotopies and the finite contraction in VSD5 prove this is a quasi-isomorphism, exactly as in CSD7. All integrals in (CV6.2) are taken before applying an algebraic coefficient functional.

Restriction from (CV6.2) to the poles is identity at degree \(-2\), has signs \(+,-\) at degree \(-1\), and is coordinate projection at degree zero. This proves the VSD6 diagram, with continuous inclusions and dagger quotients commuting throughout. The full nonzero dual localization row is
\[
0\to A^*\xrightarrow{\Delta}(A^*)^2
\xrightarrow{-\lambda_++\lambda_-}A^*
\xrightarrow{0}Q^*\xrightarrow{(\mu,-\mu)}(Q^*)^2
\xrightarrow{q^*(\mu_++\mu_-)}A^*
\xrightarrow{r^*}Z^*\to E_+^*\oplus E_-^*\to0,
\tag{CV6.3}
\]
where \(Z=\ker(r_+-r_-)\) and \(r:Z\to A\) is common restriction. The same row holds for continuous duals and dagger quotients, with finite endpoint dagger coefficients zero.

For completeness, the dual sheaf's own support-to-global map has a different direction. Its two costalks \(V_+^*\oplus V_-^*\) enter degree zero of (CV6.2). On cohomology their map to \(Z^*\) is
\[
(\nu_+,\nu_-)\longmapsto
(s_+^*\nu_++s_-^*\nu_-,\nu_+|_{E_+},\nu_-|_{E_-}),
\tag{CV6.4}
\]
where \(s_p:J\to V_p\) are the actual continuous sections of \(r_p\).
Its kernel is \(\{(r_+^*\lambda,-r_-^*\lambda):\lambda\in A^*\}\): a functional killing \(Z\) factors through \(V/Z=J\), then extends algebraically to \(A\). Its surjectivity follows from \(V\simeq Z\oplus J\). The same proof for continuous functionals uses Hahn–Banach and the continuous splitting. Thus (CV4.4) also realizes VSD6.4, not only its restriction maps.

The exact quotient row
\[
0\to Q^\dagger\to A^\dagger\to J^\dagger\to0
\tag{CV6.5}
\]
follows from the continuous and algebraic restriction rows. At its middle kernel, subtract a continuous Hahn–Banach extension of the restriction to \(J\); the remainder factors algebraically through \(Q\). Surjectivity at the right uses algebraic extension from \(J\). Since \(E_\pm\) are finite dimensional,
\[
V_p^\dagger\simeq J^\dagger,\quad Z^\dagger\simeq J^\dagger,\quad E_p^\dagger=0.
\]
Hence the literal comparison defect has exactly
\[
\mathcal H^{-2}=\underline{A^\dagger},\quad
\mathcal H^{-1}=i_*(Q^\dagger\oplus Q^\dagger),\quad
\mathcal H^0=0,\quad i_p^!\mathscr D_\dagger=J^\dagger[0],
\]
\[
H^{-2}(Y,\mathscr D_\dagger)=A^\dagger,\quad
H^{-1}(Y,\mathscr D_\dagger)=Q^\dagger,\quad
H^0(Y,\mathscr D_\dagger)=J^\dagger.
\tag{CV6.6}
\]
These groups retain the Gysin extension; a zero degree-zero cohomology sheaf has not been mistaken for zero global degree-zero cohomology.

Every actual continuous coefficient map and every proper test pullback preserves continuous functionals under transposition. Thus the inclusion, quotient and all maps above commute with the CSD cover-current pushforwards and both mirrors. Their signs are inherited from identities in the \(A\)-valued tests before any functional is applied. This makes no topology claim about the algebraic target.

## CV7. Audit of the exact rational operator and original factors

Use the original Mellin comparison
\[
\Theta a(s)=\frac12\int_0^\infty a(u)u^s\frac{du}{u},\qquad
\Theta:A\xrightarrow{\sim}\mathcal B,\quad \Theta J=\mathcal I,\quad
\mathcal Q=\mathcal B/\mathcal I,
\]
where \(\mathcal B\) is the entire strip-Schwartz space and \(\mathcal I\) the full original nontrivial-zero jet ideal. Let \(L F=sF\). The exact source identity remains
\[
\mathcal M_0\Sigma f(s)=2\zeta(s)\int_0^\infty f(v)v^s\frac{dv}{v}
\quad(\Re s>1),\qquad \mathcal M_0=2\Theta.
\tag{CV7.1}
\]

For any \(\mu\in\mathbb C\), \(M_\mu=L-\mu\) on \(\mathcal B\) is injective and has image exactly \(\{F:F(\mu)=0\}\). Evaluation is continuous and onto, for \(e^{(s-\mu)^2}\) lies in \(\mathcal B\) and equals one at \(\mu\). Division by \(s-\mu\) is continuous on this image: outside \(|s-\mu|<1\) the quotient has the original strip bound; inside, the maximum principle on the circle of radius two bounds the holomorphic quotient by a larger-strip seminorm. The imaginary polynomial weight is bounded on this fixed disk. Thus the image is closed of codimension one and the inverse on it is continuous.

On \(\mathcal I\), retain the full original-source function
\[
F_0(s)=\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2)\zeta(s).
\tag{CV7.2}
\]
Its zero divisor is exactly the nontrivial-zero divisor with full multiplicities. The quotient \(F/F_0\) is entire for \(F\in\mathcal I\), although it need not belong to \(\mathcal B\). Its value at \(\mu\) is the continuous functional
\[
\ell_\mu(F)=
\begin{cases}
F(\mu)/F_0(\mu),&F_0(\mu)\ne0,\\
F^{(m)}(\mu)/F_0^{(m)}(\mu),&\operatorname{ord}_\mu F_0=m.
\end{cases}
\tag{CV7.3}
\]
There is no missing factorial: both order-\(m\) Taylor coefficients have the same \(m!\), which cancels in their ratio. Cauchy estimates prove continuity, and \(\ell_\mu(F_0)=1\). Multiplication by \(s-\mu\) on \(\mathcal I\) has image \(\ker\ell_\mu\): division there leaves all required orders intact, including the full multiplicity at \(\mu\). Its inverse is the preceding continuous division restricted to the closed ideal.

This includes the endpoints and cancelled trivial-zero locations. No zero value of \(F_0\) is assumed there:
\[
F_0(0)=F_0(1)=\frac18,\qquad
F_0(-2r)=\frac{r(2r+1)(-1)^r\pi^r}{2\,r!}\zeta'(-2r)
\]
\[
=\frac{(1+2r)(2r)}8\pi^{-(1+2r)/2}
\Gamma((1+2r)/2)\zeta(1+2r)\ne0\quad(r\ge1).
\tag{CV7.4}
\]
These points use the first branch of (CV7.3). The original pole at one, Gamma poles and all trivial-zero derivatives remain in the comparison.

For a continuous injective \(M:E\to E\) onto a closed finite-codimensional subspace with continuous inverse on its image, both transposes are onto. Algebraic surjectivity extends a functional on \(M(E)\) by a basis; continuous surjectivity extends the continuous functional \(Mx\mapsto\lambda(x)\) by Hahn–Banach. Both kernels are the full dual of the finite-dimensional Hausdorff quotient \(E/M(E)\); hence
\[
\ker M^*=\ker M'\subset E',\qquad
M^\dagger:E^\dagger\xrightarrow{\sim}E^\dagger.
\tag{CV7.5}
\]
For injectivity of the last map, if \(M^*\lambda\) is continuous, choose continuous \(\nu\) with \(M'\nu=M^*\lambda\). Then \(\lambda-\nu\) is in the continuous kernel, so \(\lambda\) is continuous.

Apply (CV7.5) to \(M_\mu\) on \(\mathcal B\) and \(\mathcal I\). Their dagger operators are bijective for every \(\mu\). The exact row
\(0\to\mathcal Q^\dagger\to\mathcal B^\dagger\to\mathcal I^\dagger\to0\)
commutes with them. To solve an equation in \(\mathcal Q^\dagger\), solve it in \(\mathcal B^\dagger\); the image of that solution in \(\mathcal I^\dagger\) is killed by its bijective operator, so is zero. Injectivity follows from that on \(\mathcal B^\dagger\). Thus
\[
L^\dagger-\mu:\mathcal Q^\dagger\xrightarrow{\sim}\mathcal Q^\dagger
\quad(\mu\in\mathbb C).
\tag{CV7.6}
\]
Factoring any nonzero polynomial into linear factors proves that every \(P(L^\dagger)\) is bijective. The commuting inverses define the exact rational action
\[
\frac{P(t)}{Q(t)}x=P(L^\dagger)Q(L^\dagger)^{-1}x.
\tag{CV7.7}
\]
Cross multiplication proves independence of presentation. This verifies VSD13's rational-operator argument on the complete actual coefficients.

## CV8. Transported source operators and polynomial comparison

For clarity about every operator in that comparison, put \(D_u=u\partial_u\), \(D_v=v\partial_v\). Integration by parts in the rapidly decreasing source gives \(\Theta(-D_u a)=s\Theta a\). The compatible actual source operators are
\[
L_A=-D_u,\qquad
G_+(f,c_0,c_1)=(-D_vf,0,c_1),
\]
\[
G_-(h,d_0,d_1)=(h+D_vh,d_0,0).
\tag{CV8.1}
\]
They preserve the stated source conditions: \(D_v\) preserves evenness, vanishing at zero, and the zero-integral condition by integration by parts. Their endpoint generators are respectively \(\operatorname{diag}(0,1)\) and \(\operatorname{diag}(1,0)\), exactly those of the original dilation action.

Termwise differentiation of the convergent summation gives
\(D_u\Sigma=\Sigma D_v\), while \(D_uR=-R-RD_u\). Hence
\[
L_A r_+=r_+G_+,\qquad L_A r_-=r_-G_-.
\tag{CV8.2}
\]
Under \(V_p\simeq J\oplus E_p\), these are \(L_J\) plus the stated finite endpoint blocks. On \(Z\simeq J\oplus E_+\oplus E_-\), the endpoint block is \(\operatorname{diag}(0,1,1,0)\). Thus dagger transport to \(V_p^\dagger,Z^\dagger\) retains all original finite blocks in the continuous sector; it does not erase their polynomial kernels or cokernels. Restrictions and Gysin are \(\mathbb C(t)\)-linear for these coefficient operators.

For \(E=A,J,Q\), and also \(V_p,Z\) with these operators, inclusion \(E'\hookrightarrow E^*\) gives exactly
\[
\boxed{\ker P(L')\xrightarrow{\sim}\ker P(L^*),\qquad
\operatorname{coker}P(L')\xrightarrow{\sim}\operatorname{coker}P(L^*)}
\quad(P\ne0).
\tag{CV8.3}
\]
For the kernel, a killed algebraic functional has dagger class killed by the bijection \(P(L^\dagger)\), so is continuous. For cokernel surjectivity, solve
\(P(L^\dagger)\bar\mu=\bar\lambda\) and lift \(\bar\mu\) algebraically; then
\(\lambda-P(L^*)\mu\) is continuous. For injectivity, if continuous \(\eta=P(L^*)\lambda\), injectivity on the dagger quotient forces \(\lambda\) continuous. These are algebraic kernel/cokernel identities, not assertions that a quotient topology is Hausdorff.

A finite-dimensional \(L^*\)-invariant subspace is killed by the characteristic polynomial of its restricted operator, by the adjugate identity. Equation (CV8.3) therefore places the entire subspace in \(E'\). The equality of kernels also applies to \((L^*-\mu)^m\) without a finite-dimension assumption on that kernel. Replacing \(L\) by a stated \(L+k\) changes the polynomial to \(P(t+k)\), still nonzero, so the same conclusion includes the specified normal-degree shifts on those coefficient groups.

Mirrors must not be included in an assertion that all maps commute with \(L\). The actual reflection satisfies
\[
L_AR=R(1-L_A),\qquad
R^\dagger f(L^\dagger)=f(1-L^\dagger)R^\dagger
\quad(f\in\mathbb C(t)).
\tag{CV8.4}
\]
The first equality follows from the displayed \(D_uR\) formula; transposition, \(R^2=1\), and the uniqueness of polynomial inverses give the second. For \(L+k\) the reflection of the rational variable is \(t\mapsto1+2k-t\). The same source identity holds on \(V\) with chart swap by (CV8.1), including endpoints. Orientation signs multiply these operators by \(\pm1\) and do not alter that semilinearity.

Finally \(L^\dagger\) is the induced transpose of a specified continuous operator on the primal coefficient. This proof never differentiates the action on a discontinuous functional or moves one through a limiting difference quotient. The rational structure and polynomial comparison do not classify arbitrary algebraic dilation characters.

## CV9. What the constructed map proves

There is now a literal map from the fixed continuous-current sheaf complex to a current resolution of ordinary algebraic Verdier duality, equation (CV4.4). Its quotient is the computed current/Gysin cone (CV5.3), and its derived comparison defect is exactly VSD8. Every local, global, costalk and support map is realized by the explicit current representatives in CV6, with the original endpoint and orientation signs.

The independent VSD13 audit verifies its rational-operator and full polynomial kernel/cokernel assertions for the actual coefficients, including multiple zeros, endpoint blocks and normal scalar shifts. Mirrors are explicitly semilinear rather than falsely asserted to commute with the rational variable. No topology on discontinuous functionals, finite-dimensional replacement of the original source, or RH conclusion is used.

