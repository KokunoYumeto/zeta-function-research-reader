# The finite boundary trace, its sheaf exact sequence, and the original Dolbeault connecting map

Independent receiving calculation FB0–FB9, 24 September 2026. The complete coefficient-character family is retained in FB6A–FB6B, with its exact arithmetic Frobenius, rather than being replaced by the \(\lambda=1\) specialization.

The finite boundary supplies an actual local trace map. Its rational scaling character compensates one archimedean normal derivative. The map is constructed on the complete finite-adele transversal, with every original Jacobian, before taking an adelic quotient. It is not a projection onto a selected two-dimensional space.

## FB0. Source, user definitions, and scope

Human source: Alain Connes and Caterina Consani, *The Riemann–Roch strategy: Complex lift of the Scaling Site*, arXiv:1805.10501v1, original author file thecurve_K.tex. The source passages actually read are §5.2, equation actionpq, Lemma adelicomp1, Definition adelicomp2, and the subsequent description of the open set \(V\); and §6.6 through Proposition comparescalcs. The beginning of §6.8, including degenerate triangular structures, was also read. Their original data are
\[
\ell(a,b)(X,Y)=(aX+b,aY),\qquad
\mathcal C_{\mathbb Q}=P(\mathbb Q)\backslash\mathbb A_{\mathbb Q}^{\,2},
\]
\[
D=\partial_{X_\infty}+i\partial_{Y_\infty},\qquad
D_Y=Y_\infty D.
\tag{FB0.1}
\]
The positive upper-half-plane branch uses \(a\in\mathbb Q_{>0}\), \(b\in\mathbb Q\), and \(Y_\infty>0\). Source §5.2 retains the finite boundary \(Y_f=0\) in the full adelic space. Its stated open set on which the right real action is free excludes this boundary.

The operation rules in CORPUS_AND_OPERATION_RULES.md were read before this calculation. The exact user passages USR-9ad1c0a2d09dba92, USR-f55d16feb948d8c2, and USR-6152e3bc6302258c were read from the complete preserved user corpus. They require the full arithmetic reconstruction, globally compatible comparisons, and a proved Deligne comparison. The original arithmetic has already been reconstructed in the receiving programme; no conclusion below treats that arithmetic as absent. U01–U18 were consulted for source notation and corrections.

Thus \(Z_0,Z_1,Z_2,\tau\) retain their source meanings. The coordinate equation \(Y_f=0\) below belongs to Connes–Consani's specified adelic affine space. It does not assign a coordinate or parity to \(\tau\). No addition on source \(\tau\) is used. Existing supported coefficients \(z_\lambda\) retain their labels.

The locally constant coefficient sheaf below is the specified finite-transversal receiving sheaf. The cited passages provide the adelic space, affine action and archimedean operators; they do not themselves assert that the distribution enlargement constructed below is identical to all cohomology of the adelic quotient.

The original coefficient-character operator from §7.1 is also retained:
\[
L_\lambda=Y_\infty(\lambda\partial_{X_\infty}+i\partial_{Y_\infty}),
\qquad \lambda>0.
\tag{FB0.2}
\]
It arises from \((\lambda X+iY)\chi_\lambda(f)\) in source equation holom. The coordinate \(Y_\infty\) is distinct from the source's vector field denoted \(Y=Y_\infty\partial_{Y_\infty}\). FB6A–FB6B retain the character change \(\lambda\mapsto\lambda\mu\).

## FB1. The finite trace is a local sheaf map

Put
\[
F=\mathbb A_f,\quad E=F_X\times F_Y,\quad
Z=F_X\times\{0\},\quad U=E\setminus Z.
\]
Write \(i:Z\hookrightarrow E\), \(j:U\hookrightarrow E\). Let \(\mathscr L_E\) and \(\mathscr L_Z\) be the sheaves of complex-valued locally constant functions. Choose additive Haar measures \(dX_f,dY_f\) with the original arithmetic convention
\[
\operatorname{vol}(\widehat{\mathbb Z})=1.
\tag{FB1.1}
\]
This convention fixes the scalar coefficient of every density in the following formulas; it is not removed by a rescaling.

For an open set \(O\subset E\), let \(\mathscr D'_E(O)\) be the continuous dual of the compactly supported locally constant test functions on \(O\), with their usual inductive-limit topology. There are injective maps
\[
\iota_E(f)(\varphi)=
\int_O f(X_f,Y_f)\varphi(X_f,Y_f)\,dX_f\,dY_f,
\]
\[
\iota_Z(k)(\varphi)=
\int_{O\cap Z}k(X_f)\varphi(X_f,0)\,dX_f.
\tag{FB1.2}
\]
The second map has domain \(i_*\mathscr L_Z(O)\). Both are well defined because a locally constant function has finitely many values on any compact set. To prove injectivity, a nonzero value is constant on a compact open neighborhood of positive Haar measure; the indicator of a smaller such neighborhood detects it.

Restriction and boundary insertion give
\[
r:\mathscr L_E\longrightarrow i_*\mathscr L_Z,\qquad
r(f)(X_f)=f(X_f,0),
\]
\[
\boxed{T=\iota_Zr,\qquad
T(f)=f(X_f,0)\,dX_f\otimes\delta_0(Y_f).}
\tag{FB1.3}
\]
All three maps commute with restriction to open subsets. In particular \(T\) is a sheaf map, and
\[
\operatorname{supp}T(f)
=i\bigl(\operatorname{supp}(f|_Z)\bigr)
\subset\operatorname{supp}f\cap Z.
\tag{FB1.4}
\]
The equality follows because each nonzero locally constant value on \(Z\) is detected by a compact open test there.

The map is \(\mathscr L_E\)-linear:
\[
T(gf)=g\,T(f),
\tag{FB1.5}
\]
where multiplication on the right restricts \(g\) to the boundary. This locality and module law distinguish it from an arbitrary projection onto a finite-dimensional distribution space.

## FB2. Exact sequence, image, and absence of a sheaf splitting into functions

Restriction gives the exact sheaf sequence
\[
0\longrightarrow j_!\mathscr L_U
\longrightarrow\mathscr L_E
\xrightarrow{\,r\,}i_*\mathscr L_Z
\longrightarrow0.
\tag{FB2.1}
\]
Exactness can be checked at every stalk. At a point off \(Z\), the right stalk is zero and the first map is the identity. At a point of \(Z\), restriction of a locally constant germ is its constant value and is onto; a germ restricting to zero is identically zero on a neighborhood. Thus its kernel stalk and the stalk of \(j_!\mathscr L_U\) both vanish. This also proves
\[
\ker T=j_!\mathscr L_U,\qquad
\operatorname{im}T=\mathscr B:=\iota_Z(i_*\mathscr L_Z).
\tag{FB2.2}
\]
There is no nonzero locally constant function on \(E\) supported in \(Z\). The set \(Z\) has empty interior: every neighborhood of \(0\in F_Y\) contains nonzero elements. A nonzero locally constant function is nonzero on an open neighborhood, so cannot have that support.

Consequently (FB2.1) has no sheaf-linear section. The image of a section \(i_*\mathscr L_Z\to\mathscr L_E\) would restrict to zero on \(U\), hence consist of functions supported on \(Z\), and therefore be zero. It could not split the nonzero boundary restriction.

This does not obstruct global restriction or extension of individual functions. Globally \(k(X_f)\) extends as \(k(X_f)\) independent of \(Y_f\). For compactly supported \(k\), choose a compact open neighborhood \(K\) of zero in \(F_Y\); then \(k(X_f)1_K(Y_f)\) is a compactly supported locally constant extension. These extensions are not sheaf sections of (FB2.1): values away from \(Z\) depend on boundary data outside the local open set. The distribution insertion \(\iota_Z\), in contrast, is local and has the specified boundary support.

## FB3. Exact distribution enlargement and its cokernel

Let \(\mathscr D'_{E,Z}\) be distributions on \(E\) supported in \(Z\). There is a canonical isomorphism
\[
i_*\mathscr D'_Z\xrightarrow{\ \simeq\ }\mathscr D'_{E,Z},
\qquad
v\longmapsto[\varphi\mapsto v(\varphi|_Z)].
\tag{FB3.1}
\]
Here \(\mathscr D'_Z\) means all finite-transversal distributions on \(F_X\), not only densities.

For surjectivity, take a distribution \(u\) supported in \(Z\). If a compactly supported locally constant test \(\varphi\) vanishes on \(Z\), local constancy and compactness imply that its compact support is disjoint from \(Z\): at any point of its support, a nonzero local constant value persists. Thus \(u(\varphi)=0\). Restriction of compact tests to \(Z\) is onto, by the extension construction in FB2. On an arbitrary open \(O\), cover the compact boundary support by finitely many compact-open rectangles contained in \(O\), partition its \(X_f\) support into finitely many disjoint compact-open pieces subordinate to these rectangles, and use their respective \(Y_f\) indicators. This supplies the required compact extension inside \(O\). Therefore \(u\) factors uniquely through restriction. Its induced functional is continuous: on each finite-dimensional test stage it is continuous, and the locally constant test topology is the inductive limit of these stages. This proves (FB3.1).

In particular there are no additional normal derivatives at the finite boundary in this test category. Every distribution supported there is exactly a distribution in \(X_f\) multiplied by \(\delta_0(Y_f)\). This fact concerns the specified totally disconnected tests; it does not remove any archimedean normal derivative.

The exact quotient of distributions by the image of \(T\) has the filtration
\[
0\longrightarrow
i_*(\mathscr D'_Z/\iota_Z^{\,\mathrm{int}}\mathscr L_Z)
\longrightarrow\mathscr D'_E/\mathscr B
\longrightarrow\mathscr D'_E/\mathscr D'_{E,Z}
\longrightarrow0,
\tag{FB3.2}
\]
where \(\iota_Z^{\,\mathrm{int}}k=k\,dX_f\) is the internal density map on \(Z\). The injection and quotient are those of nested subspaces
\(\mathscr B\subset\mathscr D'_{E,Z}\subset\mathscr D'_E\); their exactness follows by taking the displayed quotients. For example \(\delta_0(X_f)\delta_0(Y_f)\) lies in \(\mathscr D'_{E,Z}\) but not in \(\mathscr B\), because no locally constant Haar density in \(X_f\) is supported on its singleton. Thus the first cokernel piece need not vanish.

Moreover
\[
\iota_E(\mathscr L_E)\cap\mathscr D'_{E,Z}=0.
\tag{FB3.3}
\]
A nonzero locally constant density has a nonzero value on a compact open set meeting \(U\), and a test there detects it; it therefore cannot be supported in \(Z\).

The minimal coefficient sheaf containing the regular functions as densities and the boundary trace image is consequently the internal direct sum
\[
\boxed{\mathscr M
=\iota_E(\mathscr L_E)\oplus\mathscr B
\subset\mathscr D'_E.}
\tag{FB3.4}
\]
It has the exact sequence
\[
0\longrightarrow\iota_E(\mathscr L_E)
\longrightarrow\mathscr M
\longrightarrow\mathscr B\longrightarrow0
\tag{FB3.5}
\]
split by the actual boundary inclusion. This split sequence is different from the nonsplit function-restriction sequence (FB2.1).

The span of the two global distributions
\[
h_0=dX_f\,dY_f,\qquad h_1=dX_f\,\delta_0(Y_f)
\tag{FB3.6}
\]
is not a coefficient subsheaf or \(\mathscr L_E\)-submodule: multiplication by a nonconstant compact-open indicator produces distributions outside that two-dimensional span. Its full sheaf-generated enlargement is (FB3.4). No projection onto only the two global vectors is used.

## FB4. Full affine covariance and the finite product formula

For \(a\in\mathbb Q_{>0}\), \(b\in\mathbb Q\), put
\[
L_f(a,b)(X_f,Y_f)=(aX_f+b,aY_f),\qquad q=|a|_f.
\]
Scalar-distribution pullback is
\[
\langle P_f(a,b)u,\varphi\rangle
=q^{-2}\left\langle u,
\varphi\!\left(\frac{X_f-b}{a},\frac{Y_f}{a}\right)
\right\rangle.
\tag{FB4.1}
\]
Both finite Jacobian factors remain. On regular distributions it agrees with function pullback:
\[
P_f\iota_E(f)=\iota_E(f\circ L_f).
\tag{FB4.2}
\]
On boundary densities, changing \(X_f=az+b\), with \(dX_f=q\,dz\), gives
\[
P_f\iota_Z(k)
=q^{-1}\iota_Z(k(aX_f+b)).
\tag{FB4.3}
\]
Hence
\[
\boxed{P_fT=q^{-1}T P_f^{\mathrm{fun}}.}
\tag{FB4.4}
\]
The arithmetic product formula is exact here:
\[
a=\prod_p p^{v_p(a)},\quad
q=\prod_p p^{-v_p(a)}=a^{-1},\quad q^{-1}=a.
\tag{FB4.5}
\]
All but finitely many factors equal one. Thus \(h_0\) is fixed and \(h_1\) transforms by \(a\), with no arbitrary character supplied:
\[
P_fh_0=h_0,\qquad P_fh_1=a h_1.
\tag{FB4.6}
\]
The same finite trace commutes with multiplication of \(Y_f\) by an element of \(\widehat{\mathbb Z}^{\,*}\), because this fixes \(Y_f=0\) and has modulus one.

Extend the trace to the minimal sheaf by
\[
N_f(\iota_E(f)+\iota_Z(k))=\iota_Z(f|_Z).
\tag{FB4.7}
\]
Its unique decomposition in (FB3.4) proves that this is well defined and local. Its full algebra is
\[
N_f^2=0,\quad
\ker N_f=\iota_E(j_!\mathscr L_U)\oplus\mathscr B,\quad
\operatorname{im}N_f=\mathscr B,\quad
\operatorname{coker}N_f\cong\iota_E(\mathscr L_E),
\]
\[
P_fN_f=aN_fP_f.
\tag{FB4.8}
\]
The covariance follows on both summands from (FB4.2)–(FB4.4). This is an actual coefficient operator on a stated enlargement, not an operator already acting inside the original function summand.

## FB5. The compensated normal derivative is an equivariant chain map

Write \(\Omega_\infty=\mathbb R_X\times(0,\infty)_Y\). Retain the DR supported space on every rational branch:
\[
\mathcal J_{\mathbb Q}
=\bigoplus_{c\in\mathbb Q}\bigoplus_{j\ge0}
\delta_c^{(j)}(X_\infty)\otimes\mathcal D'((0,\infty)).
\tag{FB5.1}
\]
Every vector has finite branch and normal-order support. All statements also hold locally as sheaf statements. Scalar pullback at infinity has the original factor \(a^{-2}\), and DR2 gives
\[
P_\infty(a,b)(\delta_c^{(j)}\otimes g)
=a^{-j-1}\delta_{(c-b)/a}^{(j)}\otimes Q_ag,\qquad
Q_ag(Y)=g(aY).
\tag{FB5.2}
\]
Therefore
\[
P_\infty\partial_{X_\infty}
=a^{-1}\partial_{X_\infty}P_\infty.
\tag{FB5.3}
\]
Use the original diagonal rational action \(P_\infty\otimes P_f\), not separate unrelated choices of \(a\). The coefficient trace and normal derivative combine as
\[
\boxed{\mathcal B=\partial_{X_\infty}\otimes T:
\mathcal J_{\mathbb Q}\otimes\mathscr L_E
\longrightarrow\mathcal J_{\mathbb Q}\otimes\mathscr B.}
\tag{FB5.4}
\]
Equations (FB4.4) and (FB5.3) give
\[
(P_\infty\otimes P_f)\mathcal B
=(a^{-1}a)\mathcal B(P_\infty\otimes P_f^{\mathrm{fun}})
=\mathcal B(P_\infty\otimes P_f^{\mathrm{fun}}).
\tag{FB5.5}
\]
The compensation is the full product formula. It occurs for every positive rational simultaneously.

Both original operators commute with \(\partial_{X_\infty}\):
\[
[D,\partial_{X_\infty}]=0,\qquad
[D_Y,\partial_{X_\infty}]=0,
\tag{FB5.6}
\]
because \(Y_\infty\) is independent of \(X_\infty\). Thus \(\mathcal B\) is a chain map for both two-term complexes. For \(D\), its degree-zero action is \(P_\infty\otimes P_f\) and its degree-one action is \(aP_\infty\otimes P_f\); this factor is retained. For \(D_Y\), both degrees have the raw action.

On the minimal enlargement there is the square-zero endomorphism
\[
\widetilde{\mathcal B}
=\partial_{X_\infty}\otimes N_f,\qquad
\widetilde{\mathcal B}^{\,2}=0.
\tag{FB5.7}
\]
It is equivariant and commutes with both differentials by the same calculations. Its archimedean derivative is nonzero, but its square vanishes because the actual finite coefficient operator has square zero.

As a map of coefficient vector spaces, (FB5.4) has
\[
\ker\mathcal B
=\mathcal J_{\mathbb Q}\otimes j_!\mathscr L_U,
\quad
\operatorname{im}\mathcal B
=\mathcal J_{\mathbb Q,\ge1}\otimes\mathscr B,
\]
\[
\operatorname{coker}\mathcal B
\cong\left(\bigoplus_{c\in\mathbb Q}\mathcal D'((0,\infty))\right)
\otimes\mathscr B.
\tag{FB5.8}
\]
Here \(\mathcal J_{\mathbb Q,\ge1}\) consists of positive normal orders and the last quotient is the coefficient of \(\delta_c\). The kernel follows from injectivity of \(\partial_X\) on finite normal jets and the exact kernel in FB2. The image and cokernel follow by the same basis expansion. These statements concern algebraic tensor products of the displayed coefficient spaces, or their sheafification; no completed tensor product is silently substituted.

## FB6. The induced cohomology map and the nonzero connecting map

Retain the complete original residues from DR3:
\[
R(u)_c=\sum_j(-i)^j\partial_Y^jg_{c,j},
\quad
R_Y(u)_c=\sum_j(-i)^j\partial_Y^j(Y^{-1}g_{c,j})
\tag{FB6.1}
\]
for \(u=\sum_{c,j}\delta_c^{(j)}\otimes g_{c,j}\). DR3 proves
\[
H^0(\mathcal J_{\mathbb Q}\xrightarrow D\mathcal J_{\mathbb Q})=0,\quad
H^1\xrightarrow{\ R\ }\bigoplus_c\mathcal D'((0,\infty)),
\]
and the corresponding assertions for \(D_Y,R_Y\), with section
\(E_Yh=\sum_c\delta_c\otimes Yh_c\). Every \(Y^{-1}\) and \(Y\) stays in these comparisons.

Direct substitution gives
\[
R\partial_X=-i\partial_YR,\qquad
R_Y\partial_X=-i\partial_YR_Y.
\tag{FB6.2}
\]
Consequently the exact cohomological map induced by (FB5.4), for either original complex in its stated residue coordinates, is
\[
\boxed{-i\partial_Y\otimes T.}
\tag{FB6.3}
\]
It is not zero. For instance \(h(Y)=Y\), any nonzero compactly supported locally constant boundary coefficient \(k\), and any one rational branch give output \(-i\otimes\iota_Z(k)\). The input boundary coefficient is reached from an actual locally constant extension as in FB2.

There is a stronger exact connecting sequence. Identify the coefficient quotient \(\mathscr L_E/j_!\mathscr L_U\) with \(i_*\mathscr L_Z\), retaining its ordinary function action. In each cochain degree, the derivative gives
\[
0\longrightarrow
\mathcal J_{\mathbb Q}\otimes i_*\mathscr L_Z
\xrightarrow{\ \partial_X\otimes\iota_Z\ }
\mathcal J_{\mathbb Q}\otimes\mathscr B
\longrightarrow
\left(\bigoplus_c\mathcal D'((0,\infty))\right)\otimes\mathscr B
\longrightarrow0.
\tag{FB6.4}
\]
It is equivariant by the compensated covariance, and is a short exact sequence of the two-term \(D\) complexes. On its last complex the differential is \(i\partial_Y\), since the \(\partial_X\) term has positive normal order and vanishes in the quotient. For \(D_Y\) the last differential is \(iY\partial_Y\).

On the connected interval \((0,\infty)\), distributional differentiation is onto and its kernel is the constant densities. An explicit proof of onto-ness is as follows. Choose \(\chi\in C_c^\infty((0,\infty))\) with integral one, and define
\[
\mathcal P\psi(y)=\int_0^y
\left(\psi(t)-\chi(t)\int_0^\infty\psi(s)\,ds\right)dt.
\]
This is compactly supported. For a distribution \(v\), set \(w(\psi)=-v(\mathcal P\psi)\); then
\[
w'(\psi)=-w(\psi')=v(\mathcal P\psi')=v(\psi).
\]
Continuity follows from the usual compact-test seminorms, with support in a fixed compact set containing the supports of \(\psi,\chi\). If \(v'=0\), every test of integral zero is a compactly supported derivative, so \(v\) vanishes on it and equals a constant times the integral. Multiplication by \(Y\) is invertible on this open interval, so \(iY\partial_Y\) is also onto with the same kernel.

The long exact cohomology sequence of (FB6.4) is therefore the explicit sequence
\[
0\longrightarrow
\left(\bigoplus_c\mathbb C\right)\otimes i_*\mathscr L_Z
\xrightarrow{\ \Delta\ }
\left(\bigoplus_c\mathcal D'((0,\infty))\right)\otimes i_*\mathscr L_Z
\xrightarrow{\ -i\partial_Y\otimes\iota_Z\ }
\left(\bigoplus_c\mathcal D'((0,\infty))\right)\otimes\mathscr B
\longrightarrow0.
\tag{FB6.5}
\]
The connecting map \(\Delta\) is the inclusion of constant densities, with no missing sign. For \(D\), lift the constant quotient cocycle as \(\delta_c\otimes1\otimes\iota_Z(k)\). Its differential is \(\delta_c'\otimes1\otimes\iota_Z(k)\). The preimage under the first arrow of (FB6.4) is \(\delta_c\otimes1\otimes k\), whose residue is \(1\otimes k\). For \(D_Y\), the differential of that same lifted cocycle is \(\delta_c'\otimes Y\otimes\iota_Z(k)\); its preimage has residue \(R_Y(\delta_c\otimes Y)=1\). Both give the displayed map.

Thus this receiver has a nonzero canonical boundary connecting map and a completely calculated surjective derivative map after it. Their existence does not by itself calculate all cohomology of the adelic quotient.

## FB6A. The complete coefficient-character family and its residue

For every \(\lambda>0\), put
\[
D_\lambda=\lambda\partial_X+i\partial_Y,\qquad
L_\lambda=YD_\lambda,\qquad
c_\lambda=-\frac{i}{\lambda}.
\]
These expressions contain no rescaling of the source operator. Define the full residues on all rational branches by
\[
R_\lambda(u)_c=\sum_jc_\lambda^j\partial_Y^jg_{c,j},
\qquad
R_{\lambda,Y}(u)_c
=\sum_jc_\lambda^j\partial_Y^j(Y^{-1}g_{c,j}).
\tag{FB6A.1}
\]
The source relation is \(R_\lambda D_\lambda=0\), since the two consecutive coefficients satisfy \(\lambda c_\lambda+i=0\).

There is an explicit full homotopy:
\[
T_\lambda u
=\lambda^{-1}\sum_c\sum_{j\ge1}\sum_{r=0}^{j-1}
c_\lambda^r\delta_c^{(j-1-r)}\otimes\partial_Y^rg_{c,j}.
\tag{FB6A.2}
\]
Applying \(D_\lambda\) makes consecutive terms cancel and leaves
\[
D_\lambda T_\lambda=I-ER_\lambda,\quad
T_\lambda D_\lambda=I,\quad R_\lambda E=I,
\]
where \(Eh=\sum_c\delta_c\otimes h_c\). The second identity follows from the first applied to \(D_\lambda u\), because the highest normal order proves \(D_\lambda\) injective. For \(L_\lambda\), use \(T_{\lambda,Y}=T_\lambda M_{Y^{-1}}\), \(E_Y=M_YE\), and \(R_{\lambda,Y}=R_\lambda M_{Y^{-1}}\); their identities follow by multiplication in this order. Thus all exact cohomology comparisons used in FB6 hold for the full family.

The normal derivative commutes with \(D_\lambda,L_\lambda\), and
\[
R_\lambda\partial_X
=-\frac{i}{\lambda}\partial_YR_\lambda,\qquad
R_{\lambda,Y}\partial_X
=-\frac{i}{\lambda}\partial_YR_{\lambda,Y}.
\tag{FB6A.3}
\]
Consequently the full family of induced boundary maps is
\[
\boxed{K_\lambda=-\frac{i}{\lambda}\partial_Y\otimes T.}
\tag{FB6A.4}
\]
Equations (FB6.2)–(FB6.3) are exactly its \(\lambda=1\) specialization for the two explicitly named original operators, not a replacement for (FB6A.4).

The cokernel complex in FB6.4 still has differential \(i\partial_Y\) for \(D_\lambda\), or \(iY\partial_Y\) for \(L_\lambda\), because the normal derivative term vanishes in the quotient. The connecting map now retains the full coefficient
\[
\boxed{\Delta_\lambda(h\otimes k)=\lambda h\otimes k
\quad\text{for constant densities }h.}
\tag{FB6A.5}
\]
Indeed \(D_\lambda(\delta_c\otimes h)=\lambda\delta_c'\otimes h\), whose preimage under \(\partial_X\) has residue \(\lambda h\). For \(L_\lambda\), its preimage is \(\lambda\delta_c\otimes Yh\); \(R_{\lambda,Y}\) again gives \(\lambda h\). The image is exactly the kernel of \(K_\lambda\).

## FB6B. Arithmetic Frobenius including the residue Jacobian

Source equations holombis and holom1 and Proposition frobarith give
\[
\mathfrak F_\mu=\theta_\mu R(\mu^{-1}),\qquad
\chi_\lambda\mathfrak F_\mu f
=S_{\mu^{-1}}\chi_{\lambda\mu}f,\qquad \mu>0,
\]
where \(S_cu(X,Y)=u(X,cY)\) for functions. Its scalar-distribution definition is
\[
\langle S_cu,\varphi\rangle
=c^{-1}\langle u,\varphi(X,Y/c)\rangle.
\tag{FB6B.1}
\]
On \(\delta_c^{(j)}\otimes g\), it is the identity on the normal derivative and \(Q_c\) on \(g\). The original family intertwining is
\[
L_\lambda S_{\mu^{-1}}
=S_{\mu^{-1}}L_{\lambda\mu}.
\tag{FB6B.2}
\]
Direct differentiation proves this: both sides on functions are
\(Y\lambda Q_{\mu^{-1}}\partial_X+
iY\mu^{-1}Q_{\mu^{-1}}\partial_Y\). The distribution identity follows by transposition.

On the \(L_\lambda\) residue family the exact Frobenius is
\[
R_{\lambda,Y}S_{\mu^{-1}}u_{\lambda\mu}
=\mu^{-1}Q_{\mu^{-1}}R_{\lambda\mu,Y}u_{\lambda\mu}.
\tag{FB6B.3}
\]
To prove it retain both identities
\[
Y^{-1}Q_{\mu^{-1}}=\mu^{-1}Q_{\mu^{-1}}Y^{-1},
\qquad
\partial_Y^jQ_{\mu^{-1}}
=\mu^{-j}Q_{\mu^{-1}}\partial_Y^j.
\]
Substitution in (FB6A.1) gives (FB6B.3) term by term. The factor \(\mu^{-1}\) is part of the original residue comparison. The raw \(D_\lambda\) residue identity is \(R_\lambda S_{\mu^{-1}}=Q_{\mu^{-1}}R_{\lambda\mu}\). For the two-term \(D_\lambda\) complex, however, the cochain map has degree-zero component \(S_{\mu^{-1}}\) and degree-one component \(\mu^{-1}S_{\mu^{-1}}\), because
\[
D_\lambda S_{\mu^{-1}}
=\mu^{-1}S_{\mu^{-1}}D_{\lambda\mu}.
\]
Consequently its induced degree-one cohomology action is also \(\mu^{-1}Q_{\mu^{-1}}\). The raw identity is not substituted for this cochain action.

The coefficient trace is independent of \(\lambda\) and commutes with the coefficient automorphism \(\theta_\mu\). This right archimedean action fixes the finite-adele factor. Hence the boundary map (FB6A.4) commutes with arithmetic Frobenius. On \(L_\lambda\) residue families its two composites are
\[
K_\lambda\bigl(\mu^{-1}Q_{\mu^{-1}}h_{\lambda\mu}\bigr)
=-\frac{i}{\lambda\mu^2}
Q_{\mu^{-1}}h'_{\lambda\mu},
\]
\[
\mu^{-1}Q_{\mu^{-1}}\bigl(K_{\lambda\mu}h_{\lambda\mu}\bigr)
=-\frac{i}{\lambda\mu^2}
Q_{\mu^{-1}}h'_{\lambda\mu}.
\tag{FB6B.4}
\]
The factors \(1/\lambda\), character change, derivative scaling and residue Jacobian all remain. On cochains the same result follows because \(\partial_X\) commutes with \(S_{\mu^{-1}}\) and \(N_f\) is independent of the coefficient character.

## FB7. Compatibility with the existing finite primary realization

DR defines
\[
B_{\rho,m}=\mathbb C[x,y]/(x,y)^m,\quad
\alpha=\rho+1,\quad
\Phi_c(x^uy^j)
=\delta_c^{(j)}\otimes
Y^\alpha\frac{(\log Y)^{m-j-1-u}}{(m-j-1-u)!}.
\tag{FB7.1}
\]
The source of \(x,y\) here is that explicit complex receiver; neither is primitive \(\tau\). On its image,
\[
\mathscr J=Y\partial_Y-\alpha,\quad
\mathscr N=\partial_X\mathscr J,\qquad
\mathscr N\Phi_c=\Phi_c M_y.
\tag{FB7.2}
\]
Because \(\mathscr J\) commutes with the rational affine pullback,
\[
P_\infty\mathscr N=a^{-1}\mathscr NP_\infty.
\]
Therefore
\[
\mathscr N\otimes N_f
\tag{FB7.3}
\]
is an affine-equivariant operator on the fixed DR finite image with the minimal finite coefficient enlargement. It realizes \(M_y\otimes N_f\), preserves the fixed value of \(m\), and has square zero because \(N_f^2=0\). For \(m\ge2\) it is nonzero. This proves that finite-boundary coefficients can compensate the existing normal-order weight shift inside that finite object. It precludes transporting an argument that assumed all finite coefficients were fixed under dilation to this enlarged coefficient sheaf.

The different map \(\partial_X\) from FB5 is a chain map but does not preserve every fixed finite DR image. Precisely,
\[
\partial_X\Phi_{c,m}(x^uy^j)
=\Phi_{c,m+1}(x^uy^{j+1}),
\tag{FB7.4}
\]
with \(\rho,\alpha\) unchanged. This relation increases the auxiliary truncation parameter; it does not increase an actual zeta zero's multiplicity by assertion.

The full residue of that tower entry is explicit. Put \(r=m-j-1-u\), retain
\[
P_j(z)=\prod_{v=0}^{j-1}(z-v),\quad P_0(z)=1,\qquad
P_j(\rho+z)=\sum_{h=0}^j C_{j,h}(\rho)z^h,
\]
\[
C_{j,h}(\rho)=
\sum_{\substack{S\subset\{0,\ldots,j-1\}\\|S|=h}}
\prod_{v\notin S}(\rho-v).
\tag{FB7.4a}
\]
The empty product is one. Applying \(j\) derivatives to
\(Y^\rho f(\log Y)\) gives
\(Y^{\rho-j}P_j(\rho+\partial_{\log Y})f(\log Y)\), by induction with every factor \(\rho-v\) retained. Therefore
\[
R_{\lambda,Y}\Phi_{c,m}(x^uy^j)
=\left(-\frac{i}{\lambda}\right)^j
Y^{\rho-j}
\sum_{h=0}^{\min(j,r)}
C_{j,h}(\rho)\frac{(\log Y)^{r-h}}{(r-h)!},
\]
\[
\boxed{
R_{\lambda,Y}\partial_X\Phi_{c,m}(x^uy^j)
=\left(-\frac{i}{\lambda}\right)^{j+1}
Y^{\rho-j-1}
\sum_{h=0}^{\min(j+1,r)}
C_{j+1,h}(\rho)\frac{(\log Y)^{r-h}}{(r-h)!}.}
\tag{FB7.4b}
\]
In the full boundary map this expression is tensored with
\(T(f)=f(X_f,0)dX_f\delta_0(Y_f)\). Every branch \(c\), original \(u,j,m\), nilpotent coefficient and coefficient-character parameter is retained.

For example, on the \(j=0,u=0\) source generator and \(m\ge2\), the image residue is
\[
-\frac{i}{\lambda}Y^{\rho-1}
\left(\rho\frac{(\log Y)^{m-1}}{(m-1)!}
+\frac{(\log Y)^{m-2}}{(m-2)!}\right)\otimes T(f).
\tag{FB7.4c}
\]
For \(m=1\), only the first term \(-i\lambda^{-1}\rho Y^{\rho-1}\otimes T(f)\) occurs. The second term in (FB7.4c) is the retained nontrivial spectral nilpotent contribution, not an error term.

At an actual nontrivial zero \(0<\Re\rho<1\), all factors \(\rho-v\) are nonzero. For fixed \(j\), the full logarithmic-polynomial operator in (FB7.4b) has nonzero diagonal \((-i/\lambda)^{j+1}P_{j+1}(\rho)\), after retaining its displayed factor \(Y^{\rho-j-1}\). The incremental derivative from the preceding residue has polynomial factor \((\rho-j)+\partial_{\log Y}\), whose diagonal is \(\rho-j\ne0\); its additional residue coefficient remains \(-i/\lambda\). Both descriptions prove injectivity on the stated finite spans. The logarithmic degree and its original multiplicity length are retained. The larger symbol \(B_{\rho,m+1}\) in the tower is an ambient normal-jet realization containing the image; it is not a statement that the original zeta has order \(m+1\).

Its full rational affine weight is also retained. The source branch has factor \(a^{\rho-j}\) with the complete logarithmic mixing of DR2.5. The target archimedean branch has \(a^{\rho-j-1}\), while its finite boundary density has \(a\). Their product is precisely \(a^{\rho-j}\), including all original logarithmic mixing. This is the concrete compensation without changing the reconstructed arithmetic or the zeta multiplicity.

Conversely the fixed-image operator \(\mathscr N\) need not be a chain map on the whole Dolbeault distribution complex. Its exact commutators are
\[
[D,\mathscr N]=i\partial_X\partial_Y,\qquad
[D_Y,\mathscr N]=-Y\partial_X^2.
\tag{FB7.5}
\]
Indeed \([D,\mathscr J]=i\partial_Y\), \([D_Y,\mathscr J]=-Y\partial_X\), and both differentials commute with \(\partial_X\). These formulas prove (FB7.5) and prevent substituting (FB7.3) for the cohomology map (FB6.3). On the finite cohomology image already proved injective in DR4, one can transport \(M_y\) by the explicitly invertible image comparison; that is a named finite-image operation, not a newly asserted cochain map on all distributions.

## FB8. Support filtration, quotient descent, and retained labels

On archimedean normal order, FB5 gives
\[
\mathcal B(\mathcal J_{\le n}\otimes\mathscr L_E)
\subset\mathcal J_{\le n+1}\otimes\mathscr B.
\tag{FB8.1}
\]
On actual supports it gives
\[
\{X_\infty=c\}\times\operatorname{supp}f
\longmapsto
\{X_\infty=c\}\times
\bigl(\operatorname{supp}f\cap\{Y_f=0\}\bigr).
\tag{FB8.2}
\]
The finite support becomes smaller, and archimedean normal order increases by one. It is therefore compatible with retaining boundary supports and with the displayed degree-shifted normal-order filtration. It is not a degree-zero endomorphism of the original function-only coefficient filtration: (FB3.3) proves that its nonzero boundary output is outside that function summand. The exact enlargement (FB3.4) is the map resolving that issue.

On the source open set \(V\) with \(Y_f\ne0\), the trace restricts to zero. On the full adelic space it is present. Rational affine maps preserve \(Y_f=0\), and the compensated map is equivariant under their full action. Thus it defines a morphism of equivariant sheaves, or of sheaves on the corresponding action groupoid. Taking global invariants or coinvariants need not preserve every short exact sequence; no such preservation is inferred merely from equivariance.

Every additional specified split-support label is retained by tensoring these maps with its identity, or by applying them separately on each labeled summand. Algebraic tensors are finite sums in independent coefficient coordinates, so the kernel after identity extension is the original kernel tensored with the label space. No \(z_\lambda\) is identified with \(\tau\), and amplitude vanishing does not delete a retained label.

## FB9. Mathematical outcome and proof-use limits

The finite boundary contribution is connected to the original locally constant coefficients by the actual sheaf-local map \(T\), its exact restriction sequence, and its boundary-density insertion. The nonzero finite factor \(a=|a|_f^{-1}\) is forced by the original Haar Jacobians and rational product formula. It compensates an archimedean normal derivative with factor \(a^{-1}\). This yields the explicit equivariant chain map \(\partial_X\otimes T\), its square-zero extension, and the nonzero connecting map (FB6.5).

These results supply an actual geometric coupling where a calculation using only fixed finite coefficients would have missed it. They do not identify the enlarged local coefficient complex with the full primitive-\(\tau\) cohomology, do not turn an auxiliary truncation into an actual zero multiplicity, and do not prove or disprove the programme's complete lifting theorem or RH. Every limitation here is attached to a specified map together with its proved extension, rather than claimed as an obstruction to the full user-defined global system.

For the complete coefficient-character family the same commutator calculation in (FB7.5) is
\[
[D_\lambda,\mathscr N]=i\partial_X\partial_Y,\qquad
[L_\lambda,\mathscr N]=-\lambda Y\partial_X^2.
\tag{FB9.1}
\]
Thus retaining \(\lambda\) also retains the exact failure of the fixed-block operator to be a global chain map; the compensated chain map is the independently proved \(\partial_X\otimes T\).

## Source-reading record

Primary public source: Alain Connes and Caterina Consani, [*The Riemann–Roch strategy: Complex lift of the Scaling Site*, arXiv:1805.10501v1](https://arxiv.org/abs/1805.10501v1). The retained author TeX has SHA256 \nolinkurl{da52001209424c19fb223905804a9eed1147c72331cf881aa0352bc759976061}. The exact source labels used are actionpq, adelicomp1, adelicomp2, comparescalcs, holom, holombis, holom1 and frobarith.

Read for this calculation:

- CORPUS_AND_OPERATION_RULES.md completely.
- Exact user corpus records USR-9ad1c0a2d09dba92; USR-f55d16feb948d8c2; and USR-6152e3bc6302258c completely. U01–U18 supply definition routing and current corrections.
- Original author thecurve_K.tex, §5.2 through the stated open-set condition; §6.6 through Proposition comparescalcs; §6.8 beginning through Proposition degeneratetr1; §7 opening and §7.1 through Proposition functionq and the following remark perfectoid. These are the specified passages, not a whole-paper reading claim.
- DISTRIBUTION_REALIZATION_OF_B_INDEPENDENT.md, DR0–DR3 completely, and DR4 through the displayed exact residue formulas; the finite definitions and operator comparisons used here are proved there and recalculated where needed above.
- CC_SUPPORTED_DOLBEAULT_BOUNDARY.tex, its original-source statement, SDB3–SDB6 definitions, and SDB8–SDB16 exact complex and homotopy portion. DR3 restates the complete branchwise proof used for FB6.

Human authorship of the adelic complex lift and its operators belongs to Alain Connes and Caterina Consani. The finite trace, exact coefficient enlargement, compensated chain map and connecting-map calculations FB1–FB8 are receiving derivations supplied here. No historical novelty is asserted for restriction of locally constant functions or insertion of a boundary distribution.


## FB10. Exact comparison with the added classical-orbit boundary

The factors \(M_{Y^{-1}}\) used in FB6A act on the stated open archimedean domain \(Y>0\). They do not extend as invertible smooth multipliers over \(Y=0\). The later complete calculation CB4–CB6A in CLASSICAL_BOUNDARY_LIFTING.md retains Connes–Consani's extension \((G\times\mathbb R)/\{\pm1\}\), their actual moving functions \(q^r(g,y)=e_r(g)[e^{-2\pi r y}]\), and the entire original operator \(L_\lambda=y(\lambda\partial_g+i\partial_y)\). On the defined smooth-radial finite-frequency algebra it proves the exact chain sequence
\[
0\longrightarrow(\mathcal C\xrightarrow{i\partial_y}\mathcal C)
\xrightarrow{(\mathrm{id},M_y)}
(\mathcal C\xrightarrow{iy\partial_y}\mathcal C)
\longrightarrow\mathcal B[-1]\longrightarrow0.
\]
Here \(\mathcal B=W_{\mathrm{alg}}\otimes\mathbb C[\mathbb Q]\), with its full character realization, is the exact cokernel in degree one. The raw and original degree-one Frobenius factors differ by \(\mu^{-1}\); their intertwining is proved in CB6A. No boundary term may be removed by extending the open-domain inversion across zero. This comparison retains the validity of FB6A on its domain and supplies the additional archimedean boundary contribution. CB1–CB3 separately construct the finite-valuation factor and graph correspondence relating a finite collapsed point to the entire \(G\) fibre; a finite-adele zero locus is not identified with this added archimedean boundary by notation alone.
