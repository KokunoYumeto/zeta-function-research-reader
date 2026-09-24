# Polynomial spectral lifting through the actual current-dual comparison

Complete independent derivation, 24 September 2026. Proof locators CP0–CP11.

## CP0. Source stage and the actual comparison

The support remains \(\tau\langle Z_1;\mathrm{no}\ Z_2\rangle\). The operations in this note act on the already reconstructed arithmetic coefficients and the actual sphere sheaf. They assign no addition, coordinate, metric, numerical origin, or parity to \(\tau\). The complete-history-before-arithmetic order and the separate branch counters are retained.

READ_FIRST_USER_CONSTRUCTION.md, the full connected USER_ARGUMENT_RECONSTRUCTION.md with its correction table, and PC07 in PREREQUISITE_AND_OBSTRUCTION_CHECKS.md were recalled before the operations below. The governing verbatim WU050–WU055 and WU061–WU063 passages were read in the preceding connected derivation. The new lifting problem is the one defined by the actual continuous-current inclusion; it is not an independently chosen extension.

The following complete local proofs were read:

- CC_VERDIER_SUPPORT_INDEPENDENT.md, VSD0–VSD14, in the adjacent quantum_tau_programme_bridge_20260924 directory; SHA256 \(\texttt{A49FCCBE2773E6D6378ACEB394273E734F2CA206F4D6D787500927A1F6280D2B}\).
- CC_CONTINUOUS_SUPPORT_DUAL_SHEAF.md, CSD0–CSD12; SHA256 \(\texttt{361A5798405CC6688F8EA249F2BDFB05C1EB9B67499B52CFC27F6A2BADE5579C}\).
- CC_CURRENT_TO_VERDIER_COMPARISON.md, CV0–CV9, including its final operator audit; SHA256 \(\texttt{F4825A0CED9ACE0D3610A064A6DC8B21311E86822B10937DB2AF5002728BF286}\).

These are local derivations, not new original-author sources. Their source uses remain Connes and Consani, [*Schemes over \(\mathbb F_1\) and zeta functions*, §5](https://arxiv.org/abs/0903.2024v3), and the later signed charts in [arXiv:2609.00299v1](https://arxiv.org/abs/2609.00299v1). The original author TeX and reading coverage are those recorded in CSD0, CV0, and the preceding CSL review. The comparison to Deligne uses the complete DC5–DC7 reconstruction of [*La conjecture de Weil. II*, §3.6](https://www.numdam.org/item/PMIHES_1980__52__137_0/), with its stated French-transcription witness.

Put \(R=\mathbb C[t]\). Every derived Hom below is over this ring with a specified operator \(t\), not a formal list of eigenvalue labels. We prove that the actual comparison becomes an isomorphism on all derived polynomial spectral sectors. We also give the correction of a representative, the exact uniqueness statement, and the complete original-zero multiplicity case.

## CP1. Original coefficients, their operators, and retained endpoints

Let
\[
S=\{f\in\mathcal S(\mathbb R;\mathbb C):f(-v)=f(v),\
f(0)=0,\ \int_{\mathbb R}f=0\},\quad
V_\pm=S\oplus E_\pm,\quad E_\pm=\mathbb C^2,
\]
\[
A=\{a\in C^\infty(\mathbb R_{>0}):
\sup_{u>0}(u^N+u^{-N})|(u\partial_u)^ja(u)|<\infty
\text{ for every }N,j\ge0\}.
\tag{CP1.1}
\]
The actual source maps are
\[
\Sigma f(u)=2\sum_{n\ge1}f(nu),\quad
Ra(u)=u^{-1}a(u^{-1}),\quad
r_+(f,e)=\Sigma f,\quad
r_-(h,e)=R\Sigma h=\Sigma\widehat h.
\tag{CP1.2}
\]
Here \(\widehat h(x)=\int_{\mathbb R}h(v)e^{-2\pi ivx}\,dv\). The full Poisson formula before the two source conditions is
\[
\Sigma\widehat h(u)
=u^{-1}\Sigma h(u^{-1})+u^{-1}h(0)-\int_{\mathbb R}h.
\tag{CP1.3}
\]
The exact source theorem gives \(J=\Sigma S\) closed in \(A\), a continuous inverse \(\Sigma^{-1}:J\to S\), and the Fréchet quotient \(Q=A/J\). Both endpoint coordinates on each chart are retained.

Write \(D_u=u\partial_u\), \(D_v=v\partial_v\). The actual coefficient operators of CV8 are
\[
L_A=-D_u,\qquad
G_+(f,c_0,c_1)=(-D_vf,0,c_1),\qquad
G_-(h,d_0,d_1)=(h+D_vh,d_0,0).
\tag{CP1.4}
\]
They are continuous and preserve all stated source conditions. Integration by parts proves the integral condition; differentiation preserves evenness and the value condition. From \(D_u\Sigma=\Sigma D_v\) and \(D_uR=-R-RD_u\),
\[
L_A r_+=r_+G_+,\qquad L_A r_-=r_-G_-.
\tag{CP1.5}
\]
Thus these are compatible operators on the actual coefficient diagram. Under the proved splittings
\[
V_p\simeq J\oplus E_p,\qquad
Z:=\ker(r_+-r_-)\simeq J\oplus E_+\oplus E_-,
\tag{CP1.6}
\]
the endpoint operators are \(\operatorname{diag}(0,1)\) at \(+\),
\(\operatorname{diag}(1,0)\) at \(-\), and
\(\operatorname{diag}(0,1,1,0)\) on \(Z\).
These splittings intertwine the operators: the source section on \(J\) is \(\Sigma^{-1}\), or its Fourier transform on the other chart, and (CP1.5) proves the intertwining.

For a coefficient \(E\), write
\[
E'=\operatorname{Hom}_{\mathrm{cont},\mathbb C}(E,\mathbb C),\quad
E^*=\operatorname{Hom}_{\mathbb C}(E,\mathbb C),\quad
E^\dagger=E^*/E'.
\tag{CP1.7}
\]
On these spaces \(t\) is the ordinary transpose of the specified primal operator, or its induced quotient operator. In particular it is \(L'\), \(L^*\), or \(L^\dagger\) on \(A,J,Q\). On \(V_p,Z\) it is the transpose of the full operator in (CP1.4)–(CP1.6). No derivative of a discontinuous functional's dilation orbit is being taken.

The original Mellin comparison is
\[
\Theta a(s)=\frac12\int_0^\infty a(u)u^s\,\frac{du}{u},
\qquad \Theta L_A=s\Theta,\qquad
\Theta:A\xrightarrow{\sim}\mathcal B,\quad \Theta J=\mathcal I,
\tag{CP1.8}
\]
where \(\mathcal B\) is the entire strip-Schwartz space and \(\mathcal I\) is the ideal of all full original nontrivial-zero jets. In particular the factor \(1/2\) in \(\Theta\) and the factor \(2\) in \(\Sigma\) remain present. Section CP9 records the complete original-zeta factors used below.

## CP2. The literal current comparison and its exact defect

Let \(Y=\mathbb P^1(\mathbb C)\), with positive complex orientation, and pole inclusion \(i:\{0,\infty\}\hookrightarrow Y\). The primal sheaf is
\[
\mathscr F=\underline A_Y\times_{i_*A^2}i_*(V_+\oplus V_-).
\]
CSD constructs continuous currents from the compactly supported \(A\)-valued tests; CV constructs algebraic currents on the same tests. With \(V=V_+\oplus V_-\), their actual complexes are
\[
\mathscr C_c=
\operatorname{Cone}\bigl(i_*A'^2
\xrightarrow{(\delta,-r')}\mathscr T_c^\bullet\oplus i_*V'\bigr),
\]
\[
\mathscr C_a=
\operatorname{Cone}\bigl(i_*(A^*)^2
\xrightarrow{(\delta,-r^*)}\mathscr T_a^\bullet\oplus i_*V^*\bigr).
\tag{CP2.1}
\]
The current differential in degree \(n\) is \(T\mapsto(-1)^{n+1}T\,d\).
The positive Dirac current at either pole is \(\delta_p\lambda(f)=\lambda(f(p))\). The degree-minus-one differential retains both signs:
\[
(T,\lambda_+,\lambda_-)\longmapsto
(dT+\delta_0\lambda_++\delta_\infty\lambda_-,
-r_+^*\lambda_+,-r_-^*\lambda_-),
\tag{CP2.2}
\]
and likewise for continuous coefficients.

CV4 proves the literal termwise injection
\[
c:\mathscr C_c\hookrightarrow\mathscr C_a,\qquad
\mathscr C_a\simeq\mathbb D_Y\mathscr F.
\tag{CP2.3}
\]
It is \(R\)-linear. The primal coefficient operators commute with the test differential, evaluation and integration; their transposes therefore commute with every arrow in (CP2.1). For algebraic functionals integration is performed in the complete coefficient space before applying the functional, as in CV3.

Let \(\mathscr D=\mathscr C_a/\mathscr C_c\). This is CV5.3's literal quotient-current complex, and
\[
\operatorname{Cone}(c)\xrightarrow{\simeq}\mathscr D,\qquad
(b,a)\mapsto[b].
\tag{CP2.4}
\]
Its kernel is \(\operatorname{Cone}(1_{\mathscr C_c})\), contracted by
\((b,a)\mapsto(0,b)\). It has the coefficient/Gysin description
\[
\mathscr D\simeq
\operatorname{Cone}\bigl(
i_*(A^\dagger)^2\xrightarrow{(g,-r^\dagger)}
\underline{A^\dagger}_Y[2]\oplus i_*V^\dagger\bigr).
\tag{CP2.5}
\]
The positive Gysin maps are coefficient-natural. Formula (CP2.5) does not delete their extension class.

The exact dagger row and endpoint facts are
\[
0\to Q^\dagger\to A^\dagger\to J^\dagger\to0,\qquad
V_p^\dagger\simeq J^\dagger,\quad
Z^\dagger\simeq J^\dagger,\quad E_p^\dagger=0.
\tag{CP2.6}
\]
Its proof subtracts a continuous Hahn–Banach extension at the middle kernel and uses algebraic extension for surjectivity. Endpoint dagger spaces vanish because every functional on a finite-dimensional endpoint space is continuous, not because those endpoints were removed.

For reference, the complete actual defect groups are
\[
\mathcal H^{-2}(\mathscr D)=\underline{A^\dagger}_Y,\quad
\mathcal H^{-1}(\mathscr D)=i_*(Q^\dagger\oplus Q^\dagger),\quad
\mathcal H^0(\mathscr D)=0,
\]
\[
H^{-2}(Y,\mathscr D)=A^\dagger,\quad
H^{-1}(Y,\mathscr D)=Q^\dagger,\quad
H^0(Y,\mathscr D)=J^\dagger,\qquad
i_p^!\mathscr D\simeq J^\dagger[0].
\tag{CP2.7}
\]
The local pole stalk has \(A^\dagger,Q^\dagger,0\) in degrees \(-2,-1,0\). The open-stratum restriction is \(\underline{A^\dagger}[2]\). These are the actual CSD/CV/VSD comparisons and maps; no new dual cone is being chosen.

## CP3. Why every nonzero polynomial is invertible on the defect

We recall the exact algebra needed from VSD13 and CV7. On \(\mathcal B\), multiplication by \(s-\lambda\) is injective, with closed codimension-one image \(\{F:F(\lambda)=0\}\). Division on that image is continuous, by the fixed-disk Cauchy estimate and division outside the disk.

On \(\mathcal I\), its image is the kernel of the continuous functional
\[
\ell_\lambda(F)=\left(\frac F{F_0}\right)(\lambda),\qquad
F_0(s)=\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2)\zeta(s).
\tag{CP3.1}
\]
At a zero of \(F_0\) of order \(m\), this is
\(F^{(m)}(\lambda)/F_0^{(m)}(\lambda)\); otherwise it is \(F(\lambda)/F_0(\lambda)\).
It is onto because \(\ell_\lambda(F_0)=1\). The same division estimate applies, and division retains all required zero orders.

If a continuous injective \(M:E\to E\) has closed finite-codimensional image and continuous inverse on that image, both transposes \(M'\) and \(M^*\) are onto. Extend a functional from the image algebraically, or continuously by Hahn–Banach. Their kernels coincide, because all functionals on the finite-dimensional Hausdorff quotient \(E/M(E)\) are continuous. Consequently \(M^\dagger\) is bijective: if \(M^*\lambda\) is continuous, subtract a continuous preimage and then use the common continuous kernel.

Apply this to \(L-\lambda\) on \(\mathcal B,\mathcal I\). The exact row (CP2.6) then proves bijectivity on \(Q^\dagger\) as well: solve in \(A^\dagger\); the image of the solution in \(J^\dagger\) is killed by its invertible operator and is therefore zero. Thus
\[
t-\lambda:E^\dagger\xrightarrow{\sim}E^\dagger
\quad(E=A,J,Q,V_p,Z;\ \lambda\in\mathbb C).
\tag{CP3.2}
\]
The finite endpoint dagger coefficients are zero. Factoring a nonzero polynomial into linear factors gives
\[
\boxed{P(t):E^\dagger\xrightarrow{\sim}E^\dagger
\quad(P\in R\setminus\{0\}).}
\tag{CP3.3}
\]
Every coefficient-diagram map commutes with these inverses. Hence the coefficient model (CP2.5) can be formed over \(\mathbb C(t)\).

In particular \(P\) acts bijectively on every cohomology sheaf, global group, local group and costalk in (CP2.7). This does not assert that \(P\) is invertible on each *raw quotient-current term*. The latter assertion is unnecessary and is not used.

## CP4. The exact derived polynomial spectral complex

For any cohomological \(R\)-complex \(C\), and nonzero \(P\in R\), use the free resolution
\[
0\to R\xrightarrow{P}R\to R/(P)\to0
\tag{CP4.1}
\]
with its free terms in degrees \(-1,0\). It is exact because \(R\) is an integral domain. These two free modules are projective, so their Hom complex computes derived Hom on any \(C\), with no injectivity assumption on its coefficients.

Use the following completely specified model:
\[
K_P(C)^n=C^n\oplus C^{n-1},\qquad
\delta(x,y)=(dx,Px-dy).
\tag{CP4.2}
\]
Indeed ordinary Hom has differential \(d_Cf-(-1)^nf\,d_R\). If its components are \((x,b)\), the coordinate \(y=(-1)^nb\) gives (CP4.2). Therefore
\[
\boxed{K_P(C)\simeq\operatorname{RHom}_R(R/(P),C).}
\tag{CP4.3}
\]
The formula also defines the internal derived Hom of sheaves of \(R\)-modules: internal Hom from the constant rank-one free module is the identity, so the same two-term free resolution computes it stalkwise.

The maps on cohomology are exactly
\[
0\to
\frac{H^{n-1}(C)}{P H^{n-1}(C)}
\xrightarrow{[y]\mapsto[(0,y)]}
H^nK_P(C)
\xrightarrow{[(x,y)]\mapsto[x]}
\ker(P:H^n(C)\to H^n(C))
\to0.
\tag{CP4.4}
\]
To prove this, a cycle has \(dx=0\) and \(Px=dy\), so its first coordinate lies in the displayed kernel. Every class in that kernel admits such a \(y\). If \(x=da\), subtracting \(\delta(a,0)\) leaves \((0,y-Pa)\), with second coordinate closed. Changing \(a\) by a closed element changes its class by \(P H^{n-1}(C)\); changing the second coordinate by a differential changes it by a spectral boundary. Conversely those two changes are spectral boundaries. This proves every term and map, without choosing a splitting.

For a map \(c:C_c\to C_a\), the actual spectral comparison is the componentwise map
\[
K_P(c)(x,y)=(c x,c y).
\tag{CP4.5}
\]
There is a literal cone identity
\[
K_P(\operatorname{Cone}(c))
\xrightarrow{\sim}\operatorname{Cone}(K_P(c)),
\quad
((b,a),(v,u))\longmapsto((b,v),(a,-u)).
\tag{CP4.6}
\]
Substituting the cone differential \((db+c a,-da)\) and (CP4.2) verifies both components and the minus sign on \(u\).

## CP5. Acyclicity of the actual spectral obstruction

Apply (CP4.4) to the actual defect. Bijectivity in CP3 makes both its displayed kernel and cokernel zero, so
\[
\boxed{
\operatorname{RHom}_R(R/(P),\operatorname{Cone}(c))
\simeq\operatorname{RHom}_R(R/(P),\mathscr D)
\simeq0.}
\tag{CP5.1}
\]
For sheaves this means the corresponding internal derived Hom object is zero. Derived global sections, derived point support, and restriction to either stalk preserve that zero object. Finite cones and finite direct sums commute with these derived functors, so the same assertion computes the polynomial spectral complexes of the actual global, stalk and costalk models.

On a dagger coefficient model, where \(P\) is termwise invertible, the vanishing has an explicit contraction:
\[
h^n(x,y)=(P^{-1}y,0),\qquad
\delta h+h\delta=1,\qquad h^2=0.
\tag{CP5.2}
\]
The inverse commutes with the differential, since \(P\) does. Direct substitution gives
\[
\delta h(x,y)=(P^{-1}dy,y),\qquad
h\delta(x,y)=(x-P^{-1}dy,0).
\]
This contraction applies to the coefficient/Gysin model and its finite global and local complexes. For raw quotient currents, (CP5.1) follows from the cohomology calculation, and the representative correction in CP6 uses only that justified version.

By (CP4.6), the cone of the actual comparison (CP4.5) is acyclic. Consequently the canonical map
\[
\boxed{
\operatorname{RHom}_R(R/(P),\mathscr C_c)
\xrightarrow{\sim}
\operatorname{RHom}_R(R/(P),\mathscr C_a)}
\tag{CP5.3}
\]
is a quasi-isomorphism for every nonzero \(P\). This is an isomorphism in the derived category, with a unique inverse there. It is not a claimed projection from algebraic currents to continuous currents, and it does not choose chain representatives.

The defect itself need not be zero. VSD9 proves \(A^\dagger\ne0\) and \(J^\dagger\ne0\) for these actual infinite-dimensional Fréchet coefficients. Equation (CP5.1) instead proves that this precisely defined defect has no derived sector tested by \(R/(P)\), including its degree-one Ext contribution. This is stronger than only saying that it has no eigenvectors.

## CP6. Exact correction of an algebraic spectral lift

Take one of the actual complexes of sections, stable local models, or finite coefficient models for which CV gives the degreewise exact sequence
\[
0\to C_c\to C_a\xrightarrow q D\to0.
\tag{CP6.1}
\]
For literal currents on the opens in use, exactness of sections at the quotient follows from CV5.1 and fineness of the continuous-current terms; pole coefficient quotients are exact. The current global and local contractions identify their defect cohomology with CP2.7.

Let \((x,y)\in K_P(C_a)^n\) be a cycle:
\[
dx=0,\qquad Px=dy.
\tag{CP6.2}
\]
Its actual obstruction to a continuous spectral lift is
\[
\operatorname{obs}_n[(x,y)]=[(\bar x,\bar y)]
\in H^nK_P(D),\qquad \bar x=q(x),\ \bar y=q(y).
\tag{CP6.3}
\]
This is the map induced by the actual quotient complex, so boundaries change it by boundaries. Its kernel is exactly the image of \(H^nK_P(C_c)\): one implication is immediate; for the converse, subtract a lift of a quotient primitive. Equation (CP5.1) makes its target zero.

Here is the full correction for raw quotient currents, without a termwise \(P^{-1}\) on those currents. Since \(d\bar x=0\) and \(P\bar x=d\bar y\), injectivity of \(P\) on \(H^n(D)\) gives
\[
\bar x=du\quad\text{for some }u\in D^{n-1}.
\]
Put \(w=\bar y-Pu\); then \(dw=0\). Surjectivity of \(P\) on \(H^{n-1}(D)\) gives a closed \(v\in D^{n-1}\) representing the unique class \(P^{-1}[w]\). Choose \(z\in D^{n-2}\) with
\[
dz=w-Pv.
\tag{CP6.4}
\]
These choices satisfy the exact signed identity
\[
\delta(u+v,-z)=(\bar x,\bar y).
\tag{CP6.5}
\]
Choose any cochains \(U\in C_a^{n-1}\), \(V\in C_a^{n-2}\) lifting \(u+v,-z\), respectively. Then
\[
\boxed{(x_c,y_c)=(x-dU,\ y-PU+dV)}
\tag{CP6.6}
\]
lies in \(C_c^n\oplus C_c^{n-1}\), is a cycle, and represents the same algebraic spectral class. Both assertions follow by applying \(q\), (CP6.5), and \(\delta^2=0\). This is an explicit correction by the spectral boundary \(\delta(U,V)\).

For a finite coefficient model the shorter correction follows directly from (CP5.2). Choose \(U\) lifting \(P^{-1}\bar y\) and set \(V=0\). Then
\[
(x_c,y_c)=(x-dU,\ y-PU).
\tag{CP6.7}
\]
The two formulae have distinct stated domains; the latter is not imposed on raw currents.

Uniqueness is exactly uniqueness modulo *continuous spectral boundaries*. Suppose a cycle in \(K_P(C_c)^n\) is \(\delta b\) in the algebraic complex. Then \(\bar b\) is a cycle of \(K_P(D)^{n-1}\). Its cohomology vanishes, so write \(\bar b=\delta\bar a\), lift \(\bar a\), and put \(b_c=b-\delta a\). This belongs to the continuous complex and has \(\delta b_c=\delta b\). Thus a continuous spectral class which becomes zero is already zero. Together with (CP6.6),
\[
H^nK_P(C_c)\xrightarrow{\sim}H^nK_P(C_a)
\tag{CP6.8}
\]
for every \(n\).

Changing any primitive, lift, or algebraic representative in the correction therefore changes the resulting continuous representative by a continuous spectral boundary. The cohomology lift is canonical and linear because it is the inverse of the specified linear isomorphism (CP6.8). The chosen cochains, primitive representatives, and correction operators are not asserted to be canonical or continuous in their choices.

## CP7. All degrees, including endpoints and the nonzero cokernel terms

For a module \(M\), write
\[
M[P]=\ker(P:M\to M),\qquad M/PM=\operatorname{coker}(P:M\to M).
\]
On a module in degree zero, \(K_P(M)=[M\xrightarrow P M]\) in degrees \(0,1\). Thus (CP5.3) includes exactly both the kernel and cokernel comparisons of VSD13; there is no omitted Ext degree.

The actual global continuous model is
\[
C_c^{-2}=A',\quad C_c^{-1}=A',\quad
C_c^0=V_+'\oplus V_-',\qquad
d^{-2}=0,\quad d^{-1}\lambda=(r_+'\lambda,-r_-'\lambda).
\tag{CP7.1}
\]
Its cohomology is \(A',Q',Z'\) in degrees \(-2,-1,0\). The algebraic version uses stars and the identical maps. Formula (CP4.2) specifies the spectral complex in degrees \(-2,-1,0,1\):
\[
A',\quad A'\oplus A',\quad
(V_+'\oplus V_-')\oplus A',\quad V_+'\oplus V_-'.
\tag{CP7.2}
\]
The differentials are, writing \(d'\lambda=(r_+'\lambda,-r_-'\lambda)\),
\[
x\mapsto(0,Px),\qquad
(x,y)\mapsto(d'x,Px),\qquad
(\nu,x)\mapsto P\nu-d'x.
\tag{CP7.3}
\]
All occurrences of \(P\) use the specified coefficient operator on their own term.

Every nonzero \(P\) is onto on \(A'\) and \(J'\): each factor \(L'-\lambda\) is onto by the transpose argument of CP3, and their composition remains onto. The full spectral global groups are therefore
\[
H^{-2}K_P(C_c)=A'[P],\qquad
H^{-1}K_P(C_c)=Q'[P],
\]
\[
0\to Q'/PQ'\to H^0K_P(C_c)\to Z'[P]\to0,\qquad
H^1K_P(C_c)=Z'/PZ',
\tag{CP7.4}
\]
and all other degrees vanish. These are the canonical maps of (CP4.4), rather than a silently chosen splitting of its middle extension. The algebraic-current groups are canonically identified with them by inclusion.

At a pole the continuous stalk complex is
\([A'\to^0A'\to^{r_p'}V_p']\). Its cohomology is \(A',Q',E_p'\), so
\[
H^{-2}K_P(i_p^*\mathscr C_c)=A'[P],\quad
H^{-1}K_P(i_p^*\mathscr C_c)=Q'[P],
\]
\[
0\to Q'/PQ'\to H^0K_P(i_p^*\mathscr C_c)\to E_p'[P]\to0,\quad
H^1K_P(i_p^*\mathscr C_c)=E_p'/PE_p'.
\tag{CP7.5}
\]
At a pole costalk the actual contraction gives \(V_p'[0]\), hence
\[
H^0K_P(i_p^!\mathscr C_c)=V_p'[P],\qquad
H^1K_P(i_p^!\mathscr C_c)=V_p'/PV_p'.
\tag{CP7.6}
\]
For the interior stalk, \(A'[2]\) gives only \(A'[P]\) in degree \(-2\), since \(A'/PA'=0\). For the interior costalk, \(A'[0]\) gives only \(A'[P]\) in degree zero. All these statements also hold for the actual algebraic comparison through (CP5.3).

The endpoint terms can be specified completely. Let
\[
E_{p,P}=\bigoplus_{\substack{e\text{ an endpoint eigenline at }p\\
P(\gamma_e)=0}}e',\qquad
\gamma_e\in\{0,1\}
\tag{CP7.7}
\]
using \((0,1)\) at \(+\) and \((1,0)\) at \(-\). Then
\[
E_p'[P]=E_p'/PE_p'=E_{p,P}.
\tag{CP7.8}
\]
Each selected endpoint contributes one dimension even if the root of \(P\) is repeated, because that endpoint operator is already scalar. Since \(J'/PJ'=0\),
\[
Z'/PZ'=E_{+,P}\oplus E_{-,P},\qquad
V_p'/PV_p'=E_{p,P},
\]
\[
Z'[P]=J'[P]\oplus E_{+,P}\oplus E_{-,P},\qquad
V_p'[P]=J'[P]\oplus E_{p,P}.
\tag{CP7.9}
\]
In particular \(Q'/PQ'\) is not discarded in degree zero of (CP7.4) or (CP7.5). CP8 computes it explicitly for the original-zero polynomial.

Restriction to the two pole stalks remains diagonal on degree-minus-two coefficients and anti-diagonal on degree-minus-one coefficients:
\[
\lambda\mapsto(\lambda,\lambda),\qquad
\mu\mapsto(\mu,-\mu).
\tag{CP7.10}
\]
Apply these maps to both components of \(K_P\); the exact source support signs are unchanged. The dual's costalk-to-global map is the original positive sum on its \(J'\) coordinates with both endpoint restrictions retained. All these \(R\)-linear maps commute with the canonical spectral comparison and its cohomological inverse.

## CP8. Each actual original-zero jet, with its complete multiplicity

Fix an actual nontrivial zero \(\rho\) of the original \(\zeta\), of multiplicity \(m=m_\rho\), and now take
\[
P_\rho(t)=(t-\rho)^m.
\tag{CP8.1}
\]
No zero is invented and no critical-line position is assumed. Since \(0<\Re\rho<1\), \(P_\rho(0)\) and \(P_\rho(1)\) are nonzero, so every endpoint term in (CP7.7) is zero for this polynomial.

The polynomial jet module is
\[
R/(P_\rho)\simeq\mathbb C[z]/(z^m),\qquad
t\text{ acts by }\rho+z.
\tag{CP8.2}
\]
Evaluation of full Taylor jets gives a surjection
\[
\mathcal Q\to\mathbb C[z]/(z^m),\qquad
[F]\mapsto\sum_{j=0}^{m-1}\frac{F^{(j)}(\rho)}{j!}z^j,
\]
whose kernel is \(P_\rho(L)\mathcal Q\). Indeed a representative with these jets zero is divisible in \(\mathcal B\) by \((s-\rho)^m\); continuous division follows by repeated fixed-disk estimates. Conversely multiplication by that polynomial kills these jets. Surjectivity uses an entire Gaussian times a polynomial with the prescribed finite Taylor coefficients.

Thus
\[
Q'[P_\rho]=(Q/P_\rho Q)^*
=\operatorname{span}\{\delta_{\rho,0},\ldots,\delta_{\rho,m-1}\},
\quad
\delta_{\rho,j}([a])=\frac{(\Theta a)^{(j)}(\rho)}{j!}.
\tag{CP8.3}
\]
All these functionals are continuous. Their algebraic and continuous polynomial kernels coincide *as these very functionals* under inclusion. In particular the canonical degree-minus-one lift in (CP7.4) and (CP7.5) identifies every actual algebraic original-zero jet with its unique continuous functional, with its full multiplicity \(m\).

We also compute the cokernel term, using a single actual finite projector rather than a formal infinite decomposition. Put
\[
B_\rho(s)=\frac{F_0(s)}{(s-\rho)^m},
\qquad
\Pi_\rho F(s)=B_\rho(s)
\sum_{j=0}^{m-1}\frac1{j!}
\left(\frac F{B_\rho}\right)^{(j)}(\rho)(s-\rho)^j.
\tag{CP8.4}
\]
The quotient \(F/B_\rho\) is used only in a neighborhood of \(\rho\), where its denominator is nonzero. \(B_\rho\in\mathcal B\) by division estimates. This finite operator is continuous, has the same full jet as \(F\) at \(\rho\), and vanishes at every other actual zero to its full order. It therefore induces a continuous projection \(\overline\Pi_\rho\) on \(\mathcal Q\), commuting with \(L\).

Its image \(K_\rho\) is precisely \(\ker P_\rho(L)\), has dimension \(m\), and maps isomorphically to the displayed jet module. To verify the equality, \(P_\rho\Pi_\rho F=F_0\) times a polynomial lies in \(\mathcal I\). Conversely, a class killed by \(P_\rho\) has zero jets at every other original zero and is determined by its jet at \(\rho\), hence equals its projection.

Let \(Q_0=\ker\overline\Pi_\rho\). On this actual closed complement, \(P_\rho(L)\) is a continuous automorphism. Its inverse is
\[
q=[F]\in Q_0\longmapsto
(1-\overline\Pi_\rho)\left[\frac{F(s)}{(s-\rho)^m}\right].
\tag{CP8.5}
\]
Every representative of \(q\) has zero full jet at \(\rho\), so the quotient in brackets is entire and belongs to \(\mathcal B\). Changing \(F\) by \(\mathcal I\) changes that quotient by a class supported only at \(\rho\), removed by \(1-\overline\Pi_\rho\). Multiplication in both orders gives the identity because \(P_\rho\overline\Pi_\rho=0\) and the projection commutes with \(L\).
Continuity follows by division on the closed finite-jet kernel in \(\mathcal B\) and the quotient topology; that kernel modulo \(\mathcal I\) has exactly the subspace topology of \(Q_0\), as is seen from the continuous finite Taylor interpolation projection.

Dualizing the actual decomposition \(Q=K_\rho\oplus Q_0\), the operator \(P_\rho\) is zero on \(K_\rho^*\) and invertible on \(Q_0'\). Hence
\[
Q'/P_\rho Q'\xrightarrow{\sim}K_\rho^*,\qquad
[\lambda]\mapsto\lambda|_{K_\rho},
\quad \dim(Q'/P_\rho Q')=m.
\tag{CP8.6}
\]
This proves that the cokernel term retained in CP7 is nonzero. It is not eliminated by the comparison's acyclic defect.

The same fixed finite-jet division on \(\mathcal B\) and \(\mathcal I\), using the jets of \(F\) and \(F/F_0\), shows
\[
\dim A'[P_\rho]=m,\qquad \dim J'[P_\rho]=m,
\quad A'/P_\rho A'=J'/P_\rho J'=0.
\tag{CP8.7}
\]
For the dimension statement on \(\mathcal I\), the kernel of the map taking the first \(m\) Taylor coefficients of \(F/F_0\) at \(\rho\) is \((s-\rho)^m\mathcal I\). All \(m\) values are realized by \(F_0\) times a polynomial times an entire Gaussian; this preserves membership in \(\mathcal I\) and realizes any finite jet. Its dual is the displayed polynomial kernel. This is a fixed actual-zero calculation, not an assumed analytic family of arbitrary spectra.

Consequently the global spectral cohomology for (CP8.1) is
\[
\begin{array}{c|cccc}
\text{degree}&-2&-1&0&1\\ \hline
\dim H^nK_{P_\rho}(R\Gamma\mathscr C_c)&m&m&2m&0 ,
\end{array}
\tag{CP8.8}
\]
where degree zero retains the canonical exact sequence
\[
0\to K_\rho^*\to H^0K_{P_\rho}(R\Gamma\mathscr C_c)
\to J'[P_\rho]\to0.
\tag{CP8.9}
\]
The same dimensions and canonical comparison hold for \(\mathscr C_a\).
At a pole stalk the corresponding dimensions are \(m,m,m,0\) in degrees \(-2,-1,0,1\); its degree-zero group is canonically \(K_\rho^*\).
At a pole costalk the only nonzero group has degree zero and dimension \(m\), namely \(J'[P_\rho]\).
The interior stalk has dimension \(m\) only in degree \(-2\); the interior costalk has dimension \(m\) only in degree zero.
Thus every degree and every original multiplicity is retained.

## CP9. Full original-zeta and dilation comparison

The source relations used above are the original ones:
\[
\mathcal M_0\Sigma f(s)=
2\zeta(s)\int_0^\infty f(v)v^s\,\frac{dv}{v},
\qquad \Theta=\tfrac12\mathcal M_0,
\quad \Re s>1,
\]
\[
\zeta(s)=1+\sum_{n\ge2}n^{-s}
=\prod_p(1-p^{-s})^{-1},\qquad
-\frac{\zeta'}{\zeta}(s)=\sum_p\sum_{k\ge1}(\log p)p^{-ks}.
\tag{CP9.1}
\]
The unit summand and every prime-power repetition remain present. The actual source
\[
f_0(v)=\frac\pi2v^2(2\pi v^2-3)e^{-\pi v^2}
\]
has transform
\[
F_0(s)=\Theta\Sigma f_0(s)
=C_0(s)\zeta(s),\qquad
C_0(s)=\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2).
\tag{CP9.2}
\]
The factor \(1/8\) is not changed. The apparent endpoint and trivial-zero singularities have the retained values
\[
F_0(0)=F_0(1)=\tfrac18,\qquad
F_0(-2r)=\frac{r(2r+1)(-1)^r\pi^r}{2\,r!}\zeta'(-2r)
\]
\[
=\frac{(1+2r)(2r)}8\pi^{-(1+2r)/2}
\Gamma((1+2r)/2)\zeta(1+2r)\ne0\quad(r\ge1).
\tag{CP9.3}
\]
Therefore at these locations the nonvanishing branch of (CP3.1) is used. The original pole of \(\zeta\), its trivial zeros, the Gamma poles, and their derivative cancellations have not become extra zeros of the receiver.

Near the actual \(\rho\), write \(z=s-\rho\) and
\[
\zeta(s)=z^m u_\rho(s),\qquad
F_0(s)=z^m b_\rho(s),\qquad
b_\rho(s)=C_0(s)u_\rho(s).
\tag{CP9.4}
\]
All three local factors on the right are holomorphic and \(u_\rho(\rho),b_\rho(\rho),C_0(\rho)\ne0\). The exact local comparison
\(\mathcal O_\rho/(\zeta)\simeq\mathcal O_\rho/(F_0)
\simeq\mathbb C[z]/(z^m)\)
is induced by the identity on germs, since the two ideals differ by the explicit local unit \(C_0\). That unit is retained in every derivative and residue comparison.

For example the original reflected residue is
\[
\operatorname{Res}_{s=\rho}
\frac{F(s)G(1-s)}{\zeta(s)}\,ds
=\operatorname{Res}_{s=\rho}
\frac{C_0(s)F(s)G(1-s)}{F_0(s)}\,ds.
\tag{CP9.5}
\]
If \(F(\rho+z)=\sum f_jz^j\),
\(G(1-\rho+z)=\sum g_jz^j\), and
\(1/u_\rho(\rho+z)=\sum v_jz^j\), its full value is
\[
\sum_{j+k+\ell=m-1}f_j(-1)^kg_kv_\ell.
\tag{CP9.6}
\]
Here
\[
v_\ell=\sum_{a+b=\ell}
\frac{C_0^{(a)}(\rho)}{a!}
\frac{(1/b_\rho)^{(b)}(\rho)}{b!},
\tag{CP9.7}
\]
so no derivative of the original multiplier has been suppressed.

In the Taylor-functional basis of (CP8.3),
\[
L'\delta_{\rho,j}=\rho\,\delta_{\rho,j}+\delta_{\rho,j-1},
\qquad \delta_{\rho,-1}=0.
\tag{CP9.8}
\]
The full existing dilation transpose on this finite sector is
\[
T_a'\delta_{\rho,j}
=a^\rho\sum_{h=0}^{j}
\frac{(\log a)^{j-h}}{(j-h)!}\delta_{\rho,h}.
\tag{CP9.9}
\]
This follows by the complete product derivative of \(a^sF(s)\) at \(\rho\).
Raw derivative functionals are \(j!\delta_{\rho,j}\); their matrix has
\(\binom jh(\log a)^{j-h}\), retaining precisely that factorial conversion.

The comparison (CP5.3) preserves these actual finite-sector matrices, because it is literal inclusion of the functionals and commutes with the specified coefficient action. No classification of arbitrary discontinuous dilation characters is needed.
For the normal ordinary transpose \(aT_a'\), the scalar in (CP9.9) is \(a^{\rho+1}\).
For the degree-minus-one inverse-coefficient transfer transpose \(aT_{a^{-1}}'\), it is \(a^{1-\rho}\) and every logarithm is \(-\log a\).
For the normal contragredient \(a^{-1}T_{a^{-1}}'\), it is \(a^{-\rho-1}\), again with \(-\log a\).
For integer \(a=n\ge1\), these are the specified geometric-cover, transfer and contragredient maps on the coefficient model. For arbitrary \(a>0\), they are the coefficient-complex extensions proved in CP10 below. They are different maps, not replacements for one another; no nonintegral sphere covering is asserted.

For \(a>1\), their modulus weights are respectively
\(2\Re\rho\), \(2\Re\rho+2\), \(2-2\Re\rho\), and \(-2-2\Re\rho\), using \(2\log|\lambda|/\log a\). The spectral lift preserves the full matrices for the actual \(\rho\); it does not force \(2\Re\rho=1\).

## CP10. Mirrors, shifts, and naturality of the canonical spectral lift

Let \(M\) denote one of the actual complex-linear mirrors, with its degreewise orientation and pole-swap signs. On coefficient operators,
\[
Mt=(1-t)M,\qquad MP(t)=P(1-t)M.
\tag{CP10.1}
\]
This is semilinearity for the ring involution \(\iota(t)=1-t\), fixing \(\mathbb C\). It is not \(R\)-linearity with the same variable on both sides.
Define \(P^\iota(t)=P(1-t)\). Then the exact spectral transport is
\[
K_P(C)\longrightarrow K_{P^\iota}(C),\qquad
(x,y)\longmapsto(M_nx,M_{n-1}y).
\tag{CP10.2}
\]
Indeed \(M\) commutes with the cochain differential and
\(P^\iota M=MP\), so substitution in (CP4.2) proves the chain identity. There is no further totalization sign.

For \(P=(t-\rho)^m\),
\[
P^\iota(t)=(-1)^m(t-(1-\rho))^m.
\tag{CP10.3}
\]
If the target polynomial is written as the monic factor
\((t-(1-\rho))^m\), the precise chain map is
\[
(x,y)\longmapsto(M_nx,\,(-1)^mM_{n-1}y).
\tag{CP10.4}
\]
The second-coordinate factor follows because changing the polynomial from \(Q\) to \(cQ\) changes that coordinate by \(c\). At the level of Taylor functionals, \(R'\delta_{\rho,j}=(-1)^j\delta_{1-\rho,j}\); the actual global degree-minus-one mirror has the additional CSD sign \(-R'\). These signs are compatible with (CP10.4) and retain all multiplicities. A separately chosen conjugate-linear coefficient mirror would also conjugate the polynomial coefficients; that is not substituted for the complex-linear mirrors here.

If the stated operator is \(t=L+k\), then \(P(t)\) means \(P(L+k)\), a nonzero polynomial in \(L\), so the same proof applies. Its mirror variable is
\[
t\longmapsto1+2k-t.
\tag{CP10.5}
\]
An actual zero block is then at \(t=\rho+k\), sent to \(1-\rho+k\). Scalar shifts do not change its length.

For the actual sphere cover \(z\mapsto z^n\), with integer \(n\ge1\), the ordinary transposed action on the global coefficient complex is, in degrees \(-2,-1,0\),
\[
(nT_n',\,T_n',\,\rho_+(n)'\oplus\rho_-(n)').
\tag{CP10.6}
\]
The positive-real extension in this paragraph is an action on that finite coefficient complex, whose coefficient spaces remain the full infinite-dimensional spaces. For \(a>0\), define the primal coefficient maps by
\[
T_a b(u)=b(u/a),\qquad
\rho_+(a)(f,c_0,c_1)=(f(v/a),c_0,ac_1),
\]
\[
\rho_-(a)(h,d_0,d_1)=(a h(av),ad_0,d_1).
\tag{CP10.7}
\]
They preserve all conditions in (CP1.1). Substitution gives
\(T_aT_b=T_{ab}\) and \(\rho_p(a)\rho_p(b)=\rho_p(ab)\), with identity at one and inverses at \(a^{-1}\). The summation formula gives \(r_+\rho_+(a)=T_ar_+\). On the other chart the full Fourier formula
\(\widehat{a h(a\,\cdot)}(v)=\widehat h(v/a)\) gives \(r_-\rho_-(a)=T_ar_-\), with no discarded factor. Transposing these identities proves that
\[
U_a=(aT_a',\,T_a',\,\rho_+(a)'\oplus\rho_-(a)')
\tag{CP10.8}
\]
commutes with the coefficient-complex differential. Indeed the degree-minus-two differential is zero, and the only other differential is \(d'\lambda=(r_+'\lambda,-r_-'\lambda)\), for which \(\rho(a)'d'=d'T_a'\). The primal maps commute, so their transposes satisfy \(U_aU_b=U_{ab}\). These proofs also give algebraic-transpose actions and the action on their quotient by continuous functionals. They do not construct sphere covers of noninteger degree.

Smoothness here is asserted on the continuous dual coefficient complex, equipped with its strong dual topology. Write \(a=e^h\). For any primal continuous seminorm \(p\), direct differentiation of (CP10.7) gives a continuous seminorm \(q\) and, on a compact \(h\)-interval, a constant \(C\) such that
\[
p\bigl(V_hx-x-hGx\bigr)\le C h^2q(x),
\qquad V_h=T_{e^h}\ \text{or}\ \rho_p(e^h),
\tag{CP10.9}
\]
with the corresponding \(G=L\) or \(G_p\). On \(A\), this follows from the weights \(u^N+u^{-N}\) under \(u\mapsto e^{-h}u\), bounded by \(e^{N|h|}\), and two additional logarithmic derivatives. On the Schwartz summands it follows from the same change of variable in the defining polynomial-weighted derivative seminorms; the extra factor \(e^h\) on the minus chart is retained. On the endpoint summands it is the scalar exponential Taylor estimate. Integral Taylor remainder proves the displayed bound; applying the same argument after any number of derivatives proves its higher-order versions. For a continuous functional \(\lambda\), choose \(p\) bounding \(|\lambda|\). For every bounded primal set \(B\), \(\sup_{x\in B}q(x)<\infty\), so (CP10.9), divided by \(|h|\) and transposed, tends to zero uniformly on \(B\). Thus the dual orbit is differentiable in the strong dual topology, and the higher-order estimates prove smoothness. Its infinitesimal operators are precisely
\((L'+1,L',G')\), including the derivative of the retained factor \(e^h\) in degree minus two. On the algebraic dual, the corresponding specified operators are the primal transposes \((L^*+1,L^*,G^*)\); no derivative of an arbitrary discontinuous-functional orbit is used or asserted.

The normal shift \(k=1\) occurs only in the degree-minus-two summand, whose differential to the next term is zero; the other linked terms use \(k=0\). Apply (CP10.5) to that normal summand, giving \(3-t\), and \(1-t\) on the unshifted summands. This is not a claim of one common affine reflection for two different generator conventions.
On the same coefficient complex the inverse-coefficient transfer transpose is
\((T_{a^{-1}}',aT_{a^{-1}}',a\rho(a^{-1})')\), and the contragredient is
\((a^{-1}T_{a^{-1}}',T_{a^{-1}}',\rho(a^{-1})')\).
Their group laws and chain identities follow from the same calculation, since the linked degrees carry the same additional scalar. For integer \(a=n\ge1\) they are the specified cover-associated maps. On the continuous dual their generators are respectively
\((-L',1-L',1-G')\) and \((-L'-1,-L',-G')\), by the proved smoothness; on the algebraic dual these expressions again mean induced primal transposes only. Their endpoint blocks follow from the explicitly retained eigenvalues \(0,1,1,0\).
Polynomial comparison remains valid for each of these specified nonconstant affine polynomials in \(L\).

All actual \(R\)-linear restriction, support and coefficient maps induce maps on \(K_P\) by applying the map to both coordinates. The comparison squares commute literally. Their cohomological inverse squares therefore commute by uniqueness of the inverse in (CP6.8). The mirror squares commute with the changed polynomial as in (CP10.2). Thus the canonical lifted classes preserve the actual support maps, endpoint summands, cover matrices and mirror signs even though their chain representatives are not canonically chosen.

## CP11. The exact lifting mechanism and its relation to Deligne

The actual obstruction in degree \(n\) is (CP6.3), lying in
\[
H^n\operatorname{RHom}_R(R/(P),\operatorname{Cone}(c)).
\tag{CP11.1}
\]
The exact triangle of the actual comparison, followed by the two-term free resolution, makes its kernel the image of the continuous spectral cohomology. CP3–CP5 prove that this receiver is zero in every degree. CP6 constructs the correction explicitly and proves both existence and uniqueness of the continuous *cohomology class*.

The algebraic separation is exact: \(P\) annihilates the test module \(R/(P)\), whereas \(P\) is invertible on every cohomology group of the actual comparison defect. The two-term resolution proves vanishing of both possible derived contributions,
\[
\ker(P:H^nD\to H^nD)=0,\qquad
\operatorname{coker}(P:H^{n-1}D\to H^{n-1}D)=0.
\tag{CP11.2}
\]
This is the precise linear mechanism resolving this actual lifting obstruction. It tests Ext as well as Hom and therefore does not stop at an eigenvector statement.

For comparison, DC5 describes Deligne's obstruction by
\[
c_i\longmapsto[\partial_i b_i]\in
O_i/\partial_i j_i(K_i),\qquad \pi_i(b_i)=c_i,
\]
\[
\operatorname{coker}\operatorname{sp}_i
\simeq\operatorname{im}\partial_i/\partial_i j_i(K_i).
\tag{CP11.3}
\]
DC6–DC7 prove low weights on the classes and high weights on the geometric obstruction receiver; the exact weight cutoff then kills the obstruction and supplies a lift. Here the actual quotient current map supplies (CP6.3), and polynomial-torsion versus polynomial-invertible coefficients supply the vanishing in (CP11.2). Both arguments use a proved separation to kill a specified equivariant obstruction, with their own exact sequences and maps.

The present construction does not identify the current-dual cone with Deligne's inertia/duality cross
\[
K_i=H^{i-1}(X_{\bar\eta},E)_I(-1),\qquad
O_i=H^{2N-i-1}(X_s,E)^\vee(-N).
\tag{CP11.4}
\]
No map identifying those geometric groups has been assumed. Instead the connecting morphism, target, and correction for the actual current comparison are (CP6.3)–(CP6.6), and their complete local and global degrees are CP7–CP8.

The resulting canonical comparison on each actual original-zero jet retains the whole factor \(F_0=C_0\zeta\), all derivative and residue terms, every endpoint block, all multiplicities and the actual dilation matrices. It removes no original zero and provides no bound stronger than the already known open strip for its real part. The defect can remain nonzero outside all these polynomial spectral tests. These limits are part of the exact result, rather than a substituted purity premise or an RH conclusion.
