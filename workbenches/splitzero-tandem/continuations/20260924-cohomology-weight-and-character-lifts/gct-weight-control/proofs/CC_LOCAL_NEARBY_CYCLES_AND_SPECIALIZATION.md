# Nearby cycles, the local specialization quotient, and the actual global lift

This proof uses the existing sphere sheaf. Stable locators are **LNC0–LNC11**. It derives its nearby-cycle and invariant-cycle maps and compares them with FOD7's actual lift. It retains the original Schwartz source, the complete original-zeta ideal, both endpoint coordinates at each pole, and all orientation signs.


Historical attribution: these nearby/vanishing-cycle constructions go back to Deligne’s SGA7, ExposésXIII–XIV, and Beilinson’s *How to glue perverse sheaves*. The inspected explanatory author source is Ryan Reich, [Notes on Beilinson’s “How to glue perverse sheaves”, arXiv:1002.1686v4](https://arxiv.org/abs/1002.1686v4), definitions and gluing maps at the source ranges recorded above. Credit to those originals is retained through Reich; this edition does not claim a fresh reading of the original SGA or Beilinson chapters.

Human-source attribution: the extension of continuous linear functionals is the Hahn–Banach theorem, not a programme result. See Terence Tao, [245B, Notes6: Duality and the Hahn–Banach theorem](https://terrytao.wordpress.com/2009/01/26/245b-notes-6-duality-and-the-hahn-banach-theorem/), Theorem1 and its complex proof (26 January2009). For the locally convex use here, continuity bounds a functional by a continuous seminorm; quotienting its kernel reduces this application to that normed-space theorem. No continuous splitting of the original quotient is thereby asserted.

## LNC0. Prerequisites and category

The governing construction and correction chain are READ_FIRST_USER_CONSTRUCTION.md, USER_ARGUMENT_RECONSTRUCTION.md, USER_ARGUMENT_CONNECTIONS.md, and USER_CONSTRUCTION_FULL_LOGBOOK.md. The supporting datum remains
\[
\tau\langle Z_1;\ \mathrm{no}\ Z_2\rangle .
\tag{LNC0.1}
\]
Arithmetic below is after the complete-history arithmetic reconstruction. No coordinate, distance, subtraction, or retracted addition is assigned to \(\tau\). Coordinates belong to the existing receiver \(Y=\mathbb P^1(\mathbb C)\). The specialization \(\pi:Y\to X=\{x_+,\eta,x_-\}\) sends \(0,\infty,\mathbb C^\times\) to \(x_+,x_-,\eta\). A coordinate on this receiver is not a coordinate on \(\eta\).

The proved inputs are CSP2–CSP8 (the sheaf, continuous local resolutions, costalks, orientation, and support maps); CDW2–CDW9 (the coefficient-natural direct-image splitting and angular-to-integration sign); CW10 (the existing ordinary disk/localization rows); CSD2–CSD9 (the literal continuous-current support dual); SSI/ESI (closed \(J\) and its continuous Schwartz inverse); SDT as incorporated in CSD (the strong \(Q'\) topology); DC3–DC9 (Deligne's exact cross and boundary quotient); and GMS9–GMS10/FOD7 (the actual global coefficient triangle and derived source lift). The file identities and reading coverage are recorded in LNC11.

The sheaf computations use complexes of sheaves of complex vector spaces. Every displayed map between coefficient models is continuous for the stated Fréchet topologies. Dual maps are continuous for the weak topology and the strong topology of uniform convergence on bounded sets, with the precise cohomology topology proved in CSD/SDT. We do not infer a general exact category of topological sheaves from these concrete models. The later derived \(M\)-module statements are algebraic derived statements on the actual modules, not assertions about every continuous representation of a generator.

The convention is
\[
R\phi_f\mathscr H=\operatorname{Cone}(i^*\mathscr H\longrightarrow R\psi_f\mathscr H).
\tag{LNC0.2}
\]
This fixes all degrees; no perverse shift is suppressed. Reich's original author source, arXiv:1002.1686v4, lines 261–303 and 356–375, was read for the universal-cover definition and monodromy triangle. Its finite-constructibility theorems are not applied to these infinite coefficients. The required contractions are calculated below.

## LNC1. The full existing coefficient system

Put
\[
S=\{f\in\mathcal S(\mathbb R;\mathbb C):
 f(-v)=f(v),\ f(0)=0,\ \int_{\mathbb R}f(v)\,dv=0\},
\quad E_+=E_-=\mathbb C^2,\quad V_p=S\oplus E_p,
\]
\[
A=\left\{a\in C^\infty(\mathbb R_{>0}):
\sup_{u>0}(u^N+u^{-N})|(u\partial_u)^ja(u)|<\infty
\text{ for every }N,j\right\}.
\tag{LNC1.1}
\]
The endpoint coordinates retain the value-at-zero and integral channels. The source maps are
\[
\Sigma f(u)=2\sum_{n\geq1}f(nu),\quad Ra(u)=u^{-1}a(u^{-1}),
\quad\widehat f(v)=\int_{\mathbb R}f(x)e^{-2\pi ixv}\,dx,
\]
\[
r_+(f,c_0,c_1)=\Sigma f,\qquad
r_-(g,d_0,d_1)=R\Sigma g=\Sigma\widehat g.
\tag{LNC1.2}
\]
The last identity retains the complete Poisson comparison
\[
\Sigma\widehat g(u)
=u^{-1}\Sigma g(u^{-1})+u^{-1}g(0)-\int_{\mathbb R}g(x)\,dx.
\tag{LNC1.3}
\]
Its last two terms vanish on \(S\); the separate endpoint coordinates have not been removed.

Define \(J=\Sigma S\), \(Q=A/J\), and \(q:A\to Q\). The cited SSI/ESI proofs give closed \(J\), a continuous inverse \(H=\Sigma^{-1}:J\to S\), and
\[
s_+(b)=(Hb,0,0),\quad
s_-(b)=(\widehat{Hb},0,0),\quad
r_ps_p=1_J,\quad
V_p=E_p\oplus s_pJ.
\tag{LNC1.4}
\]
Thus \(\ker r_p=E_p\), \(\operatorname{im}r_p=J\), and all these maps are actual continuous maps.

For \(D=\{0,\infty\}\), \(i:D\hookrightarrow Y\), \(j:\mathbb C^\times\hookrightarrow Y\), \(W=V_+\oplus V_-\), the sheaf is
\[
\mathscr F=\underline A_Y\times_{i_*A^2}i_*W,\qquad
0\to\mathscr F\to\underline A_Y\oplus i_*W
\xrightarrow{\mathrm{ev}-r}i_*A^2\to0.
\tag{LNC1.5}
\]
Its interior is constant \(A\), pole stalks are \(V_p\), and generizations are \(r_p\).

The original arithmetic is carried by
\[
\Theta a(s)=\frac12\int_0^\infty a(u)u^s\frac{du}{u},\qquad
\Theta^{-1}F(u)=\frac{u^{-1/2}}{\pi}
\int_{\mathbb R}F(1/2+it)u^{-it}\,dt.
\tag{LNC1.6}
\]
This identifies \(A\) with the entire strip-Schwartz space \(\mathcal B\), \(J\) with the full ideal
\[
\mathcal I=\{F\in\mathcal B:F^{(j)}(\rho)=0
\text{ for every original nontrivial zero }\rho,\ 0\leq j<m_\rho\},
\quad Q\simeq\mathcal Q=\mathcal B/\mathcal I.
\tag{LNC1.7}
\]
The original source and divisor are
\[
f_0(v)=\frac{\pi}{2}v^2(2\pi v^2-3)e^{-\pi v^2},\qquad
F_0(s)=\Theta\Sigma f_0(s)
=\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2)\zeta(s).
\tag{LNC1.8}
\]
This is the retained source map, not a replacement for the original zeta function. The complete endpoint and trivial-zero cancellations are
\[
F_0(0)=F_0(1)=\frac18,\quad F_0(-1)=F_0(2)=\frac{\pi}{24},
\]
\[
F_0(-2r)=
\frac{r(2r+1)(-1)^r\pi^r}{2\,r!}\zeta'(-2r)
=\frac{(1+2r)(2r)}8
\pi^{-(1+2r)/2}\Gamma((1+2r)/2)\zeta(1+2r)\ne0
\quad(r\geq1).
\tag{LNC1.9}
\]
These full original-source comparisons, including all nontrivial-zero jets, are proved in the receiving source files. The present calculation does not alter their ideal. In particular \(Q\ne0\): at an actual nontrivial zero \(\rho\), \(F_0(s)/(s-\rho)\in\mathcal B\) has order \(m_\rho-1\) at \(\rho\), so defines a nonzero quotient class.

## LNC2. The actual universal-cover nearby object

At \(p=0\) use \(z_p=z\), and at \(p=\infty\) use \(z_p=1/z\). Let \(D_p=\{|z_p|<\epsilon\}\) and \(D_p^*=D_p\setminus\{p\}\). The local function in this section is explicitly
\[
f_p(z_p)=z_p.
\tag{LNC2.1}
\]
The universal cover is
\[
\widetilde D_p^*=\{t\in\mathbb C:\operatorname{Re}t<\log\epsilon\},
\quad v_p(t)=e^t,\quad \gamma(t)=t+2\pi i.
\tag{LNC2.2}
\]
The pullback of \(\mathscr F|_{D_p^*}\) is constant \(A\). Resolve it by smooth \(A\)-valued forms. The straight-line contraction on this convex half-plane is, in positive degree \(k\),
\[
(\mathsf H\omega)_x
=\int_0^1t^{k-1}\iota_{x-t_0}\omega_{t_0+t(x-t_0)}\,dt,
\qquad d\mathsf H+\mathsf Hd=1-\mathrm{ev}_{t_0}.
\tag{LNC2.3}
\]
The integral exists in the complete Fréchet space \(A\). Each seminorm of the integral is bounded by the integral of that seminorm. On compact sets the intervening segments form a compact set, so this also proves continuity for every smooth compact seminorm. Differentiation under the integral proves the displayed homotopy identity in \(A\). Partitions of unity make the form resolution fine. On all these half-planes, compatibly as \(\epsilon\) decreases, constants therefore give
\[
R\psi_{f_p}\mathscr F
=i_p^*R(j_pv_p)_*v_p^*(\mathscr F|_{D_p^*})
\simeq A[0].
\tag{LNC2.4}
\]
Deck translation fixes these constant representatives. The actual monodromy is thus
\[
\mathcal T_p=1_A.
\tag{LNC2.5}
\]
This is computed from the existing sheaf; no inertia action has been independently assigned.

A pole germ \(v\in V_p\) restricts to the constant punctured section \(r_pv\). Consequently the universal-cover adjunction gives exactly
\[
\operatorname{sp}_p:V_p[0]\longrightarrow A[0],\qquad
v\longmapsto r_pv.
\tag{LNC2.6}
\]
Its kernel, image, and cokernel are \(E_p,J,Q\). In convention (LNC0.2), the actual vanishing complex is
\[
R\phi_{f_p}\mathscr F=
[V_p\text{ in }-1\xrightarrow{r_p}A\text{ in }0],
\quad H^{-1}=E_p,\quad H^0=Q.
\tag{LNC2.7}
\]
The point-supported endpoints survive even though they have no generic nearby component.

## LNC3. Angular cohomology and the invariant/coinvariant row

The deck group is the discrete group \(\mathbb Z\). Its group algebra has the free resolution
\[
0\to\mathbb C[\gamma,\gamma^{-1}]
\xrightarrow{\gamma-1}\mathbb C[\gamma,\gamma^{-1}]
\xrightarrow{\gamma\mapsto1}\mathbb C\to0.
\tag{LNC3.1}
\]
Injectivity follows from the extreme exponents of a nonzero Laurent polynomial. Finite division by \(\gamma-1\) gives the augmentation kernel. Applying Hom to this resolution yields
\[
[A\xrightarrow{\mathcal T_p-1}A]=[A\xrightarrow0A]
\quad\text{in degrees }0,1.
\tag{LNC3.2}
\]
Its actual comparison with punctured cohomology uses constants and
\[
\vartheta_p=\frac{d\arg z_p}{2\pi}.
\tag{LNC3.3}
\]
Write a closed form on the cylinder \(t=\log|z_p|\), \(\theta=\arg z_p\) as
\(\omega=P(t,\theta)dt+Q_1(t,\theta)d\theta\).
The period \(b=\int_0^{2\pi}Q_1(t_0,\theta)d\theta\) is independent of \(t_0\), by closedness. Subtracting \(b\vartheta_p\), a periodic primitive is
\[
g(t,\theta)=\int_{t_0}^tP(x,0)\,dx+
\int_0^\theta\left(Q_1(t,\varphi)-\frac b{2\pi}\right)d\varphi.
\tag{LNC3.4}
\]
Differentiation proves \(dg=\omega-b\vartheta_p\), using
\(\partial_tQ_1=\partial_\theta P\). Compact seminorm bounds for these finite integrals prove continuity. Radial contraction and the circle calculation give no further cohomology. Hence
\[
B_p^\bullet:=R\Gamma(D_p^*,\mathscr F)
\simeq A[0]\oplus A[\vartheta_p][-1],\qquad
R\Gamma(D_p,\mathscr F)\simeq V_p[0],
\tag{LNC3.5}
\]
with restriction \((r_p,0)\).

Set \(V_i=H^i(R\psi_{f_p}\mathscr F)\),
\(C_i=V_i^{\mathcal T_p}\), and
\(K_i=V_{i-1,\mathcal T_p}[\vartheta_p]\).
Then the actual exact row is
\[
0\longrightarrow K_i\xrightarrow{j_i}B_i
\xrightarrow{\pi_i}C_i\longrightarrow0,\quad
B_i=H^i(B_p^\bullet).
\tag{LNC3.6}
\]
For \(i=0\), this is \(0\to0\to A\xrightarrow1A\to0\); for \(i=1\), it is
\(0\to A[\vartheta_p]\xrightarrow1A[\vartheta_p]\to0\to0\).
The label \([\vartheta_p]\) retains the angular generator and its cover factor, proved in LNC5. The corresponding étale term in DC is \((-1)\); no identification of this topological deck group with \(\ell\)-adic inertia is asserted.

## LNC4. The exact cross and the computed obstruction quotient

Use the fibre-cone convention
\[
\operatorname{Fib}(f)^n=C^n\oplus D^{n-1},\qquad
d(x,y)=(d_Cx,fx-d_Dy).
\tag{LNC4.1}
\]
Taking the restriction fibre gives the CSP costalk, with degree two measured by positive complex-oriented integration:
\[
L_p=Ri_p^!\mathscr F=
[V_p^0\xrightarrow{r_p}A^1\xrightarrow0A^2].
\tag{LNC4.2}
\]
The angular boundary is \(-1\) in these coordinates. Indeed choose \(\chi=1\) near \(p\), zero near the outer circle. Then \(\beta=(1-\chi)\vartheta_p\) extends smoothly over \(p\), and
\[
d\beta=-d\chi\wedge\vartheta_p,\qquad \int_{D_p}d\beta=1.
\tag{LNC4.3}
\]
The fibre-cone differential makes the boundary of \(\vartheta_p\) cohomologous to \(-d\beta\). Thus
\[
H^0_p=E_p,\quad H^1_p=Q,\quad H^2_p=A,\qquad
\partial_0=q,\quad\partial_1=-1_A,
\tag{LNC4.4}
\]
and the complete nonzero localization row is
\[
0\to E_p\to V_p\xrightarrow{r_p}A\xrightarrow qQ\to0
\to A[\vartheta_p]\xrightarrow{-1}A\to0.
\tag{LNC4.5}
\]
These previously established ordinary local maps now have the actual nearby-cycle interpretation from LNC2–LNC3.

With \(A_i^{\rm sp}=H^i(D_p,\mathscr F)\) and \(O_i=H^{i+1}_p(\mathscr F)\), the exact cross has:

| \(i\) | \(A_i^{\rm sp}\) | \(K_i\) | \(B_i\) | \(C_i\) | \(O_i\) | \(\partial_i\) |
|---|---|---|---|---|---|---|
| \(-1\) | \(0\) | \(0\) | \(0\) | \(0\) | \(E_p\) | \(0\) |
| \(0\) | \(V_p\) | \(0\) | \(A\) | \(A\) | \(Q\) | \(q\) |
| \(1\) | \(0\) | \(A[\vartheta_p]\) | \(A[\vartheta_p]\) | \(0\) | \(A\) | \(-1\) |

Here \(\operatorname{sp}_i=\pi_i\alpha_i\). The quotient formula requires no assumed weight: lift \(c\in C_i\) to \(b\in B_i\) and send it to \([\partial_i b]\) in \(O_i/\partial_i j_iK_i\). Two lifts differ by \(j_iK_i\), so this is well defined. If its value is zero, \(\partial_i(b-j_ik)=0\) for some \(k\); localization exactness gives \(b-j_ik=\alpha_i a\), hence \(c=\operatorname{sp}_i a\). This proves the kernel and image, and therefore
\[
\boxed{\operatorname{coker}\operatorname{sp}_0
=\frac{\operatorname{im}\partial_0}{\partial_0j_0K_0}=Q,\qquad
\operatorname{coker}\operatorname{sp}_1
=\frac{\operatorname{im}\partial_1}{\partial_1j_1K_1}=0.}
\tag{LNC4.6}
\]
All other obstruction quotients vanish; in particular the preceding receiver \(O_{-1}=E_p\) has zero boundary image and is retained in the table and in (LNC4.5). In degree zero the actual boundary is the nonzero quotient \(q:A\to Q\). The existing separator acts as identity on \(Q\), so this is not a boundary it annihilates. Its relation to the genuine normal lift is calculated in LNC8–LNC9.

## LNC5. Actual covers, mirrors, and changing the local function

For a recovered integer \(n\geq1\), the holomorphic covering \(b_n(z)=z^n\) is \(z_p\mapsto z_p^n\) in both positive pole coordinates. Its lift of universal covers is \(t\mapsto nt\), intertwining the source deck generator with the \(n\)-th power of the target generator. A pulled-back degree-one group cocycle has value
\[
b+\mathcal T_pb+\cdots+\mathcal T_p^{n-1}b=nb,
\qquad b_n^*\vartheta_p=n\vartheta_p.
\tag{LNC5.1}
\]
The retained coefficient actions are
\[
T_ab(u)=b(u/a),\quad
\rho_+(a)(f,c_0,c_1)=(f(\cdot/a),c_0,ac_1),
\]
\[
\rho_-(a)(g,d_0,d_1)=(ag(a\,\cdot),ad_0,d_1).
\tag{LNC5.2}
\]
The source formulas give \(r_p\rho_p(a)=T_ar_p\). Including both geometry and coefficients gives:

| Receiver | Actual \(b_n\) pullback with coefficients |
|---|---|
| pole \(V_p\) | \(\rho_p(n)\) |
| nearby \(A\), \(B_0\), \(C_0\) | \(T_n\) |
| \(B_1=K_1=A[\vartheta_p]\) | \(nT_n\) |
| support \(H^0_p=E_p\) | \(\rho_p(n)|_{E_p}\) |
| support \(H^1_p=Q\) | \(\overline T_n\) |
| support \(H^2_p=A\) | \(nT_n\) |
| vanishing \(H^{-1}=E_p,\ H^0=Q\) | \(\rho_p(n)|_{E_p},\ \overline T_n\) |

All cross maps commute, by \(r_p\rho_p(n)=T_nr_p\), \(qT_n=\overline T_nq\), and the same factor \(n\) on both sides of \(\partial_1=-1\). The notation \(A(-1)\) below records this proved \(nT_n\) action. For real \(a>0\) the coefficient action exists separately; there is no asserted holomorphic map \(z\mapsto z^a\) for a noninteger \(a\).

The two actual mirrors are
\[
w(z)=-1/z,\qquad \alpha(z)=-1/\overline z.
\tag{LNC5.3}
\]
They exchange poles. Using target coordinate \(w'=1/z'\) at infinity, their local forms from zero are \(w'=-z\) and \(w'=-\bar z\). Thus the positive local angular and support-orientation signs are \(+1\) for \(w\), \(-1\) for \(\alpha\). Both use coefficient \(R\), swap pole spaces, and act by \(\overline R\) on local \(Q\). Nearby coefficients transform by \(R\); local angular and degree-two support coefficients transform by \(+R,-R\), respectively.

For the global annular coordinate \(\vartheta=d\arg z/(2\pi)\), however,
\[
w^*\vartheta=-\vartheta,\qquad
\alpha^*\vartheta=+\vartheta,\qquad
\vartheta_\infty=-\vartheta_0.
\tag{LNC5.4}
\]
This accounts for the global loop boundary \((-a,a)\). The local and global angular signs are not interchangeable.

Now keep the sheaf fixed but change the function itself to \(f_{p,n}(z_p)=z_p^n\) over a fixed target disk. This is a different nearby-cycle construction. The pullback of the target universal cover has \(n\) components, each a contractible half-plane. A target deck generator cyclically permutes them:
\[
R\psi_{f_{p,n}}\mathscr F=A^n[0],\qquad
\mathcal T(a_0,\ldots,a_{n-1})=(a_{n-1},a_0,\ldots,a_{n-2}).
\tag{LNC5.5}
\]
Its invariant space is diagonal \(A\), and its coinvariant identification is
\[
(A^n)_{\mathcal T}\xrightarrow{\sim}A,\qquad
[(a_0,\ldots,a_{n-1})]\longmapsto\sum_j a_j.
\tag{LNC5.6}
\]
The kernel of this sum is the image of \(\mathcal T-1\), as solving by successive partial sums verifies; that solution is a finite-coordinate continuous map. Specialization is \(\operatorname{diag}(r_p)\), so its cokernel in the invariant space is still \(Q\). The diagonal map induces multiplication by \(n\) on coinvariants. This also follows by restricting a target cocycle to its \(n\)-fold domain loop and summing its translates.

No other part of this nearby object is dropped. In the full vanishing cone,
\[
H^{-1}(R\phi_{f_{p,n}}\mathscr F)=E_p,\qquad
H^0(R\phi_{f_{p,n}}\mathscr F)=A^n/\operatorname{diag}J.
\tag{LNC5.7}
\]
The explicit isomorphism of the last group is
\[
[a_0,\ldots,a_{n-1}]
\longmapsto
\left(q\bar a,\ (a_0-\bar a,\ldots,a_{n-1}-\bar a)\right)
\in Q\oplus\ker(\textstyle\sum),\quad
\bar a=\frac1n\sum_j a_j.
\tag{LNC5.8}
\]
Its inverse sends \((q b,v)\) to \([\operatorname{diag}b+v]\), independent of the lift of \(qb\). Continuity follows from the finite-coordinate maps and the quotient topology. The second summand retains every nontrivial cyclic-monodromy component. Formula (LNC5.5) is not substituted for the identity-function nearby object \(A\) in LNC2.

## LNC6. The actual continuous dual specialization

Use the literal current complex from CSD4:
\[
\mathscr D_c\mathscr F
=\operatorname{Cone}\left(i_*A'^2
\xrightarrow{(\delta,-r')}\mathscr T_A^\bullet\oplus i_*W'\right).
\tag{LNC6.1}
\]
Here \(\mathscr T_A^k(U)=\Gamma_c(U,\mathcal E_A^{-k})'\), with Hom differential, and restriction is transpose to extension by zero of compact tests. Its terms in degrees \(-2,-1,0\) are \(\mathscr T_A^{-2}\), \(\mathscr T_A^{-1}\oplus i_*A'^2\), and \(\mathscr T_A^0\oplus i_*W'\), and
\[
d^{-2}T=(dT,0),\qquad
d^{-1}(T,\lambda)=(dT+\delta\lambda,-r'\lambda).
\tag{LNC6.2}
\]
This is continuous duality, not unrestricted algebraic duality.

For \(\lambda\in A'\), define the constant current \(c_\lambda(\omega)=\lambda(\int\omega)\) and
\[
h_p\lambda(\phi)=\lambda\left(\int\vartheta_p\wedge\phi\right).
\tag{LNC6.3}
\]
The angular current is locally integrable at the pole. Stokes on a positive small circle gives \(dh_p\lambda=\delta_p\lambda\). Thus CSD's exact pole-stalk comparison is
\[
P_p=[A'\text{ in }-2\xrightarrow0A'\text{ in }-1
\xrightarrow{r_p'}V_p'\text{ in }0]
\longrightarrow i_p^*\mathscr D_c\mathscr F,
\]
\[
\lambda\mapsto c_\lambda,\qquad
\mu\mapsto(h_p\mu,-\mu),\qquad
\nu\mapsto(0,\nu).
\tag{LNC6.4}
\]
Indeed \(d(h_p\mu,-\mu)=(0,r_p'\mu)\). The compact-test contraction of CSD proves this a quasi-isomorphism by continuous comparison maps on each small disk. The integral in (LNC6.3) is formed in \(A\) first and then evaluated by the continuous functional.

On the puncture the representatives are \(c_\lambda,h_p\mu\) in degrees \(-2,-1\). Restriction is therefore the exact chain map
\[
P_p\longrightarrow A'[2]\oplus A'[1],\qquad
(\deg-2,\deg-1,\deg0)=(1,1,0).
\tag{LNC6.5}
\]
On the universal cover the angular current has the primitive \(\arg z_p/(2\pi)\). The same current contraction, obtained by transposing the compact-test contraction, leaves only constant currents. Consequently
\[
R\psi_{f_p}(\mathscr D_c\mathscr F)=A'[2],\qquad
\mathcal T=1,\qquad
\operatorname{sp}^{\vee}_p:P_p\to A'[2]
=(1\text{ in }-2,\ 0\text{ otherwise}).
\tag{LNC6.6}
\]
This is the map induced by current restriction and universal-cover adjunction.

The complete pole-stalk cohomology is
\[
H^{-2}(P_p)=A',\quad
H^{-1}(P_p)=\ker r_p'=q'Q',\quad
H^0(P_p)=V_p'/\operatorname{im}r_p'=E_p'.
\tag{LNC6.7}
\]
The middle comparison carries the strong \(Q'\) topology by SDT. For the last, \(V_p=E_p\oplus s_pJ\), and Hahn–Banach extends every continuous functional on the closed \(J\subset A\). Hence the image is the full \(J'\) summand of \(V_p'\), and the quotient is the endpoint dual. No strong openness of \(A'\to J'\) is assumed.

The fibre of (LNC6.5) cancels its identity pair in degree \(-2\). The remaining complex is
\[
A'\longrightarrow V_p'\oplus A',\qquad
\mu\longmapsto(r_p'\mu,\mu)
\quad\text{in degrees }-1,0.
\tag{LNC6.8}
\]
The quotient coordinate \((\nu,b)\mapsto\nu-r_p'b\) gives its continuous deformation retraction to \(V_p'[0]\). Therefore
\[
Ri_p^!\mathscr D_c\mathscr F\simeq V_p'[0],\qquad
\partial^\vee_{-1}=-r_p':A'\longrightarrow V_p'.
\tag{LNC6.9}
\]
The nontrivial localization part is
\[
0\to Q'\xrightarrow{q'}A'\xrightarrow{-r_p'}V_p'\to E_p'\to0,
\tag{LNC6.10}
\]
alongside identity \(A'\to A'\) in degree \(-2\).
For this dual nearby object, \(V^\vee_{-2}=A'\) is its only nearby cohomology. The invariant row in degree \(-2\) has \(B_{-2}=C_{-2}=A'\), \(K_{-2}=0\), with specialization identity. In degree \(-1\), \(B_{-1}=K_{-1}=A'\), \(C_{-1}=0\), and boundary \(-r_p'\). Thus its boundary quotients \(\operatorname{im}\partial^\vee/\partial^\vee jK\) are zero. The kernel \(Q'\) remains in (LNC6.10).

It remains visible also in vanishing cycles. The cone of (LNC6.6) contains a contractible identity pair in degrees \(-3,-2\); eliminating it gives
\[
R\phi_{f_p}(\mathscr D_c\mathscr F)
\simeq[A'\text{ in }-2\xrightarrow{-r_p'}V_p'\text{ in }-1],
\qquad H^{-2}=Q',\quad H^{-1}=E_p'.
\tag{LNC6.11}
\]
The pointwise Hom differential of the continuous dual of
\([V_p^{-1}\xrightarrow{r_p}A^0]\) is \(-r_p'\).
Thus, on these actual complexes,
\[
R\phi_{f_p}(\mathscr D_c\mathscr F)
\simeq (R\phi_{f_p}\mathscr F)^\vee[2].
\tag{LNC6.12}
\]
Dual specialization is onto its nearby cohomology, but the primal quotient becomes the displayed dual stalk/vanishing term; it is not removed.

For a power cover, the actual map on this dual is proper-current pushforward, transpose to primal pullback. Its factors on (LNC6.4) are
\[
(\deg-2,\deg-1,\deg0)
=(nT_n',\,T_n',\,\rho_p(n)').
\tag{LNC6.13}
\]
For constant currents, pulling back a compact two-form multiplies its integral by \(n\). For the angular current, the \(n\) inverse sheets each contribute \(1/n\) to its trace, giving factor one. A point Dirac current pushes forward with factor one. These are also the direct transposes of the compact pole-costalk maps.

The nearby functor types of this pushforward must be retained. For the fixed target function \(f_p=z_p\), its literal source and map are
\[
R\psi_{f_p}(b_{n*}\mathscr D_c\mathscr F)
\simeq R\psi_{f_p\circ b_n}(\mathscr D_c\mathscr F)
=A'^n[2]
\xrightarrow{(\lambda_j)\mapsto\sum_jT_n'\lambda_j}
A'[2]=R\psi_{f_p}(\mathscr D_c\mathscr F).
\tag{LNC6.14}
\]
To prove this comparison directly, pull back the target universal cover: its inverse image under \(b_n\) has \(n\) components, as in (LNC5.5). Each component carries a constant current, and away from the pole its branch map is an orientation-preserving local isomorphism. Its pushforward therefore contributes \(T_n'\lambda_j\), without an additional degree factor on a single branch. Adding the branches proves (LNC6.14). The source monodromy is cyclic permutation; the sum intertwines it with identity. At the pole a finite proper map has direct-image stalk equal to the sum of its finitely many inverse-image stalks: disjoint neighborhoods of the inverse images and properness provide a cofinal such neighborhood system. Here there is just one inverse image at the pole, so this comparison also has the correct pole source \(P_p\).

Specialization to the source nearby invariants is diagonal on its degree-\(-2\) \(A'\). Restricting (LNC6.14) to that diagonal yields \(nT_n'\). On coinvariants, identified by the sum as in (LNC5.6), the induced map is \(T_n'\). Thus the invariant/coinvariant factors are exactly the degree-\(-2\)/degree-\(-1\) factors in (LNC6.13), and the dual point-costalk factor is \(\rho_p(n)'\). The full \(A'^n\) is retained; it is not replaced by its invariant diagonal when stating the nearby functor itself.

This is not a holomorphic inverse root map. The separately defined coefficient contragredient for the original pairing has factors
\(a^{-1}(T_{a^{-1}})'\), \((T_{a^{-1}})'\), and \(\rho_p(a^{-1})'\).
Under either mirror, the local degree \(-1\) current action is \(+R'\), and the degree \(-2\) action is \(\varepsilon_gR'\), where \(\varepsilon_w=1,\varepsilon_\alpha=-1\); endpoints swap dually. A current represented by a form pushes forward as \(\varepsilon_g(g^{-1})^*\), so the local angular sign cancels the orientation sign in degree \(-1\). These maps are the transposes of the primal local maps and commute with all displayed dual arrows.

## LNC7. The existing coefficient triangle on nearby and vanishing cycles

Define \(\mathscr F_J=\underline J_Y\times_{i_*J^2}i_*W\) and
\(\mathscr G=j_!\underline Q\). The actual row is
\[
0\longrightarrow\mathscr F_J\longrightarrow\mathscr F
\longrightarrow\mathscr G\longrightarrow0.
\tag{LNC7.1}
\]
At a pole it is \(0\to V_p\xrightarrow1V_p\to0\to0\); on the puncture it is \(0\to J\to A\xrightarrow qQ\to0\). The coefficientwise universal-cover contraction gives
\[
\begin{array}{ccc}
V_p&\xrightarrow{r_p:J}&J\\
\Vert&&\downarrow\\
V_p&\xrightarrow{r_p:A}&A\\
\downarrow&&\downarrow q\\
0&\longrightarrow&Q .
\end{array}
\tag{LNC7.2}
\]
The right column is the actual nearby extension. Taking its indicated cones gives
\[
[V_p^{-1}\to J^0]\longrightarrow[V_p^{-1}\to A^0]
\longrightarrow[0\to Q^0].
\tag{LNC7.3}
\]
Since \(r_p:V_p\to J\) has section \(s_p\), their cohomology groups are, respectively, \(E_p\) in degree \(-1\); \(E_p,Q\) in degrees \(-1,0\); and \(Q\) in degree zero. The map on the degree-zero defect is exactly
\[
Q\xrightarrow{1_Q}Q.
\tag{LNC7.4}
\]
Thus this quotient sheaf preserves and displays the local vanishing-cycle quotient.

The actual current-dual comparison has coefficient maps
\[
Q'\xrightarrow{q'}A'\xrightarrow{\mathrm{restriction}}J'.
\tag{LNC7.5}
\]
Hahn–Banach gives exactness of this underlying continuous-functional sequence. Applying the literal CSD cone maps, or the finite local complexes (LNC6.4) and (LNC6.11), makes (LNC7.4) the identity on \(Q'\) in vanishing degree \(-2\). This is a concrete transpose on the actual sheaf models; no general exactness of arbitrary topological dualization is needed.

## LNC8. The local coefficient boundary and its exact global image

The continuous section \(s_p\) gives the projection
\(\operatorname{pr}_{E_p}(v)=v-s_pr_pv\).
The pole costalks of (LNC7.1) form the exact row of complexes
\[
L_{J,p}=(V_p\xrightarrow{r_p}J\xrightarrow0J(-1)),\quad
L_{F,p}=(V_p\xrightarrow{r_p}A\xrightarrow0A(-1)),\quad
L_{G,p}=(0\longrightarrow Q\xrightarrow0Q(-1))
\tag{LNC8.1}
\]
in degrees \(0,1,2\). The normal label retains the proved cover factor \(n\). The continuous chain maps
\[
L_{J,p}\longrightarrow E_p[0]\oplus J(-1)[-2],
\quad(v,b,c)\longmapsto(\operatorname{pr}_{E_p}v,0,c),
\]
\[
L_{F,p}\longrightarrow E_p[0]\oplus Q[-1]\oplus A(-1)[-2],
\quad(v,b,c)\longmapsto(\operatorname{pr}_{E_p}v,qb,c)
\tag{LNC8.2}
\]
are quasi-isomorphisms: their kernels in degrees \(0,1\) are
\(s_pJ\xrightarrow{r_p}J\), contracted by \(s_p\). The formulas commute with the row inclusions and quotient. They leave the identity row on \(E_p\) in degree zero, the identity \(Q\to Q\) in degree one, and the full normal short exact row in degree two. No section of \(A\to Q\) is introduced.

Let
\[
e_0=[\,0\to J\to A\xrightarrow qQ\to0\,].
\tag{LNC8.3}
\]
The actual local coefficient connecting morphism
\(\delta_p:L_{G,p}\to L_{J,p}[1]\) is therefore zero on \(Q[-1]\) and equals
\[
e_0(-1)[-2]:Q(-1)[-2]\longrightarrow J(-1)[-1]
\tag{LNC8.4}
\]
on the normal component. This follows from the simultaneous chain maps, so it fixes the extension, degree, and sign rather than merely matching its cohomology.

The already constructed support-to-global map is
\[
k_p:L_p\longrightarrow
D_F=(W\xrightarrow{r_+-r_-}A\xrightarrow0A(-1)),
\]
\[
\begin{array}{c|ccc}
 &k_p^0&k_p^1&k_p^2\\ \hline
p=0&v\mapsto(v,0)&+1&+1\\
p=\infty&v\mapsto(0,v)&-1&+1 .
\end{array}
\tag{LNC8.5}
\]
The differential equality at infinity is
\((r_+-r_-)(0,v)=-r_-v=k_p^1r_-v\); at zero it is \(r_+v=k_p^1r_+v\). Positive complex integration gives \(+1\) in degree two at both poles. The same formulas with coefficients \(J,Q\) commute with (LNC8.1). Hence the actual coefficient triangles have the naturality square
\[
\begin{array}{ccc}
L_{G,p}&\xrightarrow{\delta_p}&L_{J,p}[1]\\
\downarrow k_{G,p}&&\downarrow k_{J,p}[1]\\
D_G&\xrightarrow{\delta}&D_J[1].
\end{array}
\tag{LNC8.6}
\]
Both normal vertical maps are \(+1\). Thus (LNC8.4) is the actual global normal extension class, with the same sign.

On the low quotient the support map is instead
\[
H^1_p(\mathscr F)=Q\longrightarrow H^1(Y,\mathscr F)=Q,
\qquad +1\text{ at }0,\quad-1\text{ at }\infty.
\tag{LNC8.7}
\]
Thus the local failure to extend a punctured constant section becomes an actual global cohomology class with its stated sign. The two-pole map is the difference \(Q^2\to Q\). Its dual is the actual anti-diagonal \(Q'\to Q'^2\); the degree-two support sum dualizes to the diagonal \(A'\to A'^2\), as CSD8 proves by restriction of currents.

The compatible angular description is also explicit. CDW gives the coefficient-natural map
\[
R\pi_*\mathscr F\simeq
\Omega\oplus j_{X!}A[\vartheta][-1]
\tag{LNC8.8}
\]
simultaneously for \(\mathscr F_J,\mathscr F,\mathscr G\). Its angular coefficient row is
\(j_{X!}J[\vartheta]\to j_{X!}A[\vartheta]\to j_{X!}Q[\vartheta]\).
Taking its single nonzero Čech degree gives the normal degree-two row. The comparison with positive sphere integration is minus the identity on each of \(J,A,Q\). Indeed use the chart forms
\[
\beta_+=\frac{r^2}{1+r^2}\vartheta,\quad
\beta_-=-\frac1{1+r^2}\vartheta,\quad
\beta_+-\beta_-=\vartheta,\quad
d\beta_+=d\beta_-=\omega_Y,\quad\int_Y\omega_Y=1.
\tag{LNC8.9}
\]
The Čech-total differential identifies the class of \(a\vartheta\) with \(-a\omega_Y\). Applying this same comparison to both ends and the middle of the short exact row preserves its extension class. This proves the angular-to-normal agreement in (LNC8.6) while retaining the degree-two minus sign.

## LNC9. Full arithmetic transport and the FOD7 lifting equation

Let \(M\) be the ring of entire functions polynomially bounded on each closed vertical strip. Its action on \(\mathcal B,\mathcal I,\mathcal Q\) is multiplication. In original Mellin variable \(s\), the normal action is \(h(s+1)\), and the actual power-cover dilation is \(n^{s+1}\), with its factor \(n\). The coordinate transport
\[
(\mathcal VF)(\lambda)=F(\lambda-1)
\tag{LNC9.1}
\]
sends the full normal row to
\[
0\to\mathcal I_+\to\mathcal B\to\mathcal Q_+\to0,\qquad
\mathcal I_+=\{F:F^{(j)}(\rho+1)=0,\ 0\leq j<m_\rho\}.
\tag{LNC9.2}
\]
Its full source divisor is
\[
F_+(\lambda)=F_0(\lambda-1)
=\frac{(\lambda-1)(\lambda-2)}8
\pi^{-(\lambda-1)/2}\Gamma((\lambda-1)/2)\zeta(\lambda-1).
\tag{LNC9.3}
\]
The values \(1/8\) occur at \(\lambda=1,2\); the values \(\pi/24\) at \(\lambda=0,3\); the values at \(\lambda=1-2r\) are exactly (LNC1.9). At \(\lambda=\rho+1\) every original product derivative and multiplicity \(m_\rho\) is transported. The normal class in (LNC8.6) becomes \(e_+[-2]\), where \(e_+\) is the extension (LNC9.2).

The existing \(M\)-action on \(V_p=E_p\oplus s_pJ\) is transported through \(s_p\) on the \(J\) summand; the four endpoint characters of \(W\) remain
\[
(h(0),h(1),h(1),h(0)).
\tag{LNC9.4}
\]
Thus \(r_p,s_p\), the costalk row, and its support-to-global square are \(M\)-linear. The normal action is shifted, rather than replaced by \(h(s)\). Mirrors intertwine the low variable by \(s\mapsto1-s\), and the normal variable by \(\lambda\mapsto3-\lambda\); they are not \(M\)-linear for an unchanged parameter.

With \(Z=\ker(r_+-r_-)\), the simultaneous quasi-isomorphisms proved in GMS9 are
\[
D_J\simeq Z[0]\oplus\mathcal I_+[-2],\quad
D_F\simeq Z[0]\oplus\mathcal Q[-1]\oplus\mathcal B[-2],\quad
D_G=\mathcal Q[-1]\oplus\mathcal Q_+[-2],
\]
\[
\delta:D_G\to D_J[1],\qquad
\delta=(0,e_+[-2]).
\tag{LNC9.5}
\]
Their kernels are the explicit contractible source complexes, not sections of \(\mathcal B\to\mathcal Q\).

The actual whole-history separator \(c=E_+\in M\), constructed in GSL/GMS, has the full-jet actions
\[
c_{\mathcal Q}=1,\qquad c_{\mathcal Q_+}=0,\qquad ce_+=0.
\tag{LNC9.6}
\]
It is not an idempotent on all of \(\mathcal B,\mathcal I_+,D_F,D_J\). For every derived \(M\)-morphism \(f:\mathcal Q[k]\to D_G\), the actual lifting equation is
\[
\delta f=\delta f c_{\mathcal Q[k]}
=\delta c_{D_G}f=c_{D_J[1]}\delta f=0.
\tag{LNC9.7}
\]
The last equality follows from the actual component \(e_+\) and (LNC9.6). GMS's complete bar contraction equivalently gives
\(\operatorname{RHom}_M(\mathcal Q,\mathcal Q_+)=0\). Thus in (LNC9.5) the normal component of \(f\) is zero in the derived category, and its low component can be retained in \(D_F\). This constructs its derived lift as in FOD7. The map from local costalks to this equation is the proved square (LNC8.6).

This leaves the calculated local invariant-cycle cross unchanged. Its degree-zero boundary is \(q:A\to Q\), and, transporting \(c\) back by \(\Theta\),
\[
q\,c_A=c_Qq=q.
\tag{LNC9.8}
\]
It is preserved, whereas the normal global extension class is killed. The exact morphisms between these receivers are the coefficient row, angularization, and support-to-global maps of LNC7–LNC8. Those maps relate the two boundaries; they do not identify the operators \(q\) and \(e_+\).

The full source representative of normal multiplication is still
\[
a\longmapsto
\Theta^{-1}[(1-E(s))\Theta a(s)](u)
=\frac{u^{-1/2}}{\pi}\int_{\mathbb R}
(1-E(1/2+it))\Theta a(1/2+it)u^{-it}\,dt\in J,
\tag{LNC9.9}
\]
followed by \(H=\Sigma^{-1}\) for a Schwartz representative. Here
\(E_+(s+1)=1-E(s)\). This retains the actual full ideal and original source; no smaller kernel is substituted.

## LNC10. The resulting diagram and its continuous dual

The complete path of constructed maps is:

    pole V_p --r_p--> nearby A, with monodromy identity
                          |
                     boundary q
                          v
                Q = local vanishing quotient
                          |
             support-to-global: +1 at 0, −1 at infinity
                          v
                      H^1(Y,F)=Q

    nearby coefficient row:     0 → J → A → Q → 0
    angular row:                 0 → J[angle] → A[angle] → Q[angle] → 0
    positive normal row:         0 → J(−1) → A(−1) → Q(−1) → 0
    full shifted Mellin row:     0 → I_plus → B → Q_plus → 0
                                             class e_plus
                                             c e_plus = 0

Every arrow has been constructed above, including the common minus sign from angular Čech cohomology to positive integration. The local invariant-cycle receiver is \(Q\). Its normal twist is the quotient in the actual normal extension, whose class is \(e_+\). The cyclic class module \(M e_+\) is a module of central multiples of that extension class; it is not identified with \(Q\).

Continuous support duality retains the additional exact comparison
\[
Q=H^0(R\phi\mathscr F)\quad\longmapsto\quad
Q'=H^{-2}(R\phi\mathscr D_c\mathscr F)
=\ker(A'\xrightarrow{r_p'}V_p').
\tag{LNC10.1}
\]
The complete original-zeta jet functionals, including multiplicities, are in this actual continuous quotient dual. Dual specialization is identity on its separate nearby \(A'\) in degree \(-2\); \(Q'\) remains in stalk degree \(-1\) and vanishing degree \(-2\).

Taking the transpose of (LNC9.8) gives
\[
c_A'q'=q',\qquad (c_Q)'=1_{Q'}.
\tag{LNC10.2}
\]
This is the transpose of the specified coefficient action, not an inserted Hermitian identification or inverse-parameter contragredient. Thus the dual local quotient also survives the separator. Its pairings remain the actual \(Q'\times Q\to\mathbb C\), induced from \(A'\times A\), and the compact-test integration maps of LNC6.

This specifies the comparison with DC. There the support group receiving \(\partial_i\), after dividing by the coinvariant boundary, has a weight range separated from the classes in \(C_i\); that proves its boundary zero. Here the actual cross has been calculated: at \(i=0\) its receiver is \(Q\) and its map is \(q\); at \(i=1\) the coinvariant term accounts for the entire boundary. Under full continuous duality the first quotient becomes the explicit \(Q'\) kernel and vanishing term, with all endpoint degrees retained.

FOD7 supplies a genuine global derived lift in this same sheaf's coefficient triangle, related through (LNC8.6). It does not make \(r_p:V_p\to A\) onto. These conclusions compute the available lift and the residual local receiver on the original source and its actual dual. They do not assign an unconstructed finite-field weight filtration to the infinite coefficient spaces or assert a new RH conclusion.

## LNC11. Source-reading and use record

For this derivation, CSP2–CSP8, CDW2–CDW6 and CDW8–CDW9, CSD4–CSD9, DC3–DC9, and FOD6–FOD7 were read as proof sources. Their full local filenames are:

* CC_SPHERE_PULLBACK_AND_NORMAL_DIRECTION.md;
* CC_DERIVED_DIRECT_IMAGE_AND_WINDING.md;
* CC_CONTINUOUS_SUPPORT_DUAL_SHEAF.md;
* DELIGNE_INVARIANT_CYCLE_QUOTIENT.md;
* CC_FULL_SOURCE_OBSTRUCTION_DECOMPOSITION.md.

The complete accepted GMS proof in CC_GLOBAL_MULTIPLIER_SEPARATION.md was previously authored and independently reviewed in this task. Its actual modules and category are retained in LNC9. The ordinary localization calculation is also recorded in CW10 of CC_ACTUAL_WEIGHT_LIFT_COMPARISON.md; it is used as an established calculation, not claimed as newly discovered here.

The original author TeX source sources/Reich_1002_1686_v4/author_source/beilinson_nearby-cycles.tex, lines 251–382, was read for the nearby-cycle definition and monodromy convention. Its public source identity is [Ryan Reich, Notes on Beilinson's “How to glue perverse sheaves”, arXiv:1002.1686v4](https://arxiv.org/abs/1002.1686v4). No finite-dimensional decomposition or constructibility theorem in that source is asserted for \(A\).

The newly proved comparisons are: the actual universal-cover nearby object and monodromy (LNC2); its invariant/coinvariant cross and exact quotient (LNC3–LNC4); the distinction between a power cover and a power local function, retaining both entire nearby objects (LNC5); continuous-current specialization and the shifted dual defect (LNC6–LNC7); and the natural morphism from this cross through the full coefficient row to FOD7's global lift (LNC8–LNC10). The earlier ordinary localization maps are retained with their original signs to prove those comparisons.
