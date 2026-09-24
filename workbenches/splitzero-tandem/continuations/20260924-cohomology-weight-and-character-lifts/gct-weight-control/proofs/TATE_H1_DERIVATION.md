# Full-period Tate cohomology and the degree mechanism

**Date:** 2026-09-24. **Status:** complete local derivation from the supplied Tate-curve model. All coordinates in this document belong to the displayed Tate curves or their product. No coordinate, differential, metric, complex structure, or cohomology theory is assigned here to the base tau.

**Human source.** Alain Connes and Caterina Consani, *On the Absolute Geometry of Spec Z and the Fargues–Fontaine curve*, original-author `FF.tex`, source directory `01_CC_Absolute_Geometry_SpecZ`, SHA-256 `14C17A95040BE7BFC57BB5F87E58907A05CACD0BCB1B6967B2892CF3D9BC1229`. The source portions actually read are lines 1–100 and 1390–1640. The receiving definitions are Proposition `prop:archimedean_points_C` at line 1465, the Tate quotient discussion at lines 1548–1579, the real structure at lines 1581–1593, and the rectangular decomposition at lines 1595–1638. The occurrence of `thm:tate_decomposition` used here is at line 1624; that label also occurs earlier in the source. The cohomology and isogeny calculations below are derivations from that model, not assertions that the source states them.

## T1. The original periods and complex structure

Fix the source prime $p$, and retain

\[
A=\log p>0,\qquad B=2\pi>0,\qquad
\Lambda_p=A\mathbb Z+iB\mathbb Z.
\tag{T1.1}
\]

Write $z\in\mathbb C^\times$ for the source's nonzero **morphism parameter**. The exponential map in the new logarithm variable $w=x+i\theta$ gives

\[
z=e^w=e^xe^{i\theta},\qquad
e^{w+A}=pe^w,\qquad e^{w+iB}=e^w.
\tag{T1.2}
\]

Consequently the exact identification is

\[
E_p=\mathbb C^\times/p^{\mathbb Z}
\cong\mathbb C/\Lambda_p
\cong (\mathbb R/A\mathbb Z)\times(\mathbb R/B\mathbb Z).
\tag{T1.3}
\]

Indeed, $e^{w'}/e^w\in p^{\mathbb Z}$ holds exactly when $w'-w\in A\mathbb Z+iB\mathbb Z$. This proves both injectivity and surjectivity of the middle identification. The last identification records both original periods and is a real product decomposition, not a replacement of the complex structure.

The invariant forms and the orientation are

\[
dx=\frac{d|z|}{|z|},\qquad d\theta,\qquad
\omega_p=\frac{dz}{z}=dx+i\,d\theta,\qquad
dx\wedge d\theta>0.
\tag{T1.4}
\]

The forms $dx,d\theta$ descend despite the multivalued functions $x,\theta$. Their periods on the positive radial and angular loops

\[
r_p(t)=[e^{At}],\qquad a_p(t)=[e^{iBt}],\qquad 0\le t\le1,
\tag{T1.5}
\]

are respectively

\[
\left(\int_{r_p}dx,\int_{a_p}dx\right)=(A,0),\qquad
\left(\int_{r_p}d\theta,\int_{a_p}d\theta\right)=(0,B).
\tag{T1.6}
\]

In particular, neither winding direction nor either period is discarded. The source's modular parameter $iA/B$ is recovered by the comparison $u=w/(iB)$: the positive angular generator goes to $1$, and the positive radial generator goes to $-iA/B$. Reversing the latter generator gives the source's lattice basis $1,iA/B$. Thus the apparent sign change is an explicit choice of lattice generator, not a changed real structure or period. The variable $w$ and full lattice (T1.1) remain the working objects.

The complex structure $J_p$ satisfies

\[
J_p\partial_x=\partial_\theta,\qquad
J_p\partial_\theta=-\partial_x,
\qquad J_p^*dx=-d\theta,\quad J_p^*d\theta=dx.
\tag{T1.7}
\]

The source supplies the form $dz/z$. Its real quadratic form is

\[
g_p=dx\otimes dx+d\theta\otimes d\theta,
\qquad \operatorname{Area}(E_p,g_p)=AB=2\pi\log p.
\tag{T1.8}
\]

It is well defined because both deck transformations in (T1.2) preserve $dw$. Multiplying the parameter $z$ by any fixed nonzero complex number also preserves $dz/z$, so this construction is independent of a translated choice of origin. We do not introduce a freely chosen positive inner product later.

## T2. All cohomology groups, the cup product, and the Hodge form

With complex coefficients, the de Rham cohomology is

\[
H^0(E_p,\mathbb C)=\mathbb C\cdot1,
\quad H^1(E_p,\mathbb C)=\mathbb C[dx]\oplus\mathbb C[d\theta],
\quad H^2(E_p,\mathbb C)=\mathbb C[dx\wedge d\theta].
\tag{T2.1}
\]

Here and below the same symbols denote invariant representatives when this creates no ambiguity. For completeness, use the Fourier modes

\[
e^{i(k_xx+k_\theta\theta)},\qquad
k_x=\frac{2\pi m}{A},\quad k_\theta=\frac{2\pi l}{B},
\quad (m,l)\in\mathbb Z^2.
\tag{T2.2}
\]

For a closed one-form, each nonzero Fourier coefficient pair $(f,g)$ satisfies $k_xg-k_\theta f=0$. The scalar coefficient

\[
h=\frac{k_xf+k_\theta g}{i(k_x^2+k_\theta^2)}
\tag{T2.3}
\]

has differential coefficients $f,g$. Thus all nonconstant modes of a closed one-form are exact. Division by a nonzero quadratic frequency preserves smooth Fourier convergence. The constant modes are not exact because their periods on (T1.5) are $Af$ and $Bg$. A two-form with nonzero Fourier coefficient $c$ is the differential of the one-form with coefficients

\[
-\frac{k_\theta c}{i(k_x^2+k_\theta^2)}\,dx
+\frac{k_xc}{i(k_x^2+k_\theta^2)}\,d\theta.
\tag{T2.4}
\]

Its constant mode is not exact because

\[
\int_{E_p}dx\wedge d\theta=AB.
\tag{T2.5}
\]

Finally a function with zero differential is constant on the connected torus. This proves (T2.1), including its representatives and periods.

The integral cohomology is specified inside these unchanged real de Rham groups by the period conditions

\[
H^1(E_p,\mathbb Z)
=\left\{a\,dx+b\,d\theta:\ Aa\in\mathbb Z,\ Bb\in\mathbb Z\right\},
\quad
H^2(E_p,\mathbb Z)=\frac{1}{AB}\mathbb Z[dx\wedge d\theta].
\tag{T2.6}
\]

These are exact comparison maps with singular integral cohomology: the torus has the two cycles (T1.5), their oriented product is the fundamental two-cycle, and no torsion occurs. Writing the reciprocal periods in (T2.6) does not replace the full-period forms (T1.4).

For

\[
\alpha=a\,dx+b\,d\theta,\qquad
\beta=c\,dx+d\,d\theta,
\]

the cup pairing, including its full volume factor, is

\[
Q_p(\alpha,\beta)=\int_{E_p}\alpha\wedge\beta
=AB(ad-bc).
\tag{T2.7}
\]

The Hodge star from (T1.8) and the displayed orientation is

\[
*_p dx=d\theta,\qquad *_p d\theta=-dx,
\qquad *_p\omega_p=-i\omega_p,
\quad *_p\overline\omega_p=i\overline\omega_p.
\tag{T2.8}
\]

It equals $-J_p^*$ on real one-forms. Its positive Hermitian pairing is therefore

\[
h_p(\alpha,\beta)
=\int_{E_p}\alpha\wedge *_p\overline\beta
=AB(a\overline c+b\overline d).
\tag{T2.9}
\]

In particular $h_p(\alpha,\alpha)>0$ for every nonzero class. Positivity follows from $A,B>0$ and the displayed sum of absolute squares; it is not an imposed spectral assumption.

Every holomorphic one-form on $E_p$ is a multiple of $\omega_p$. To prove this, lift the form to $f(w)\,dw$ on $\mathbb C$. The function $f$ is entire and lattice periodic, hence bounded on the plane by its bound on a compact fundamental rectangle; Liouville's theorem makes $f$ constant. Complex conjugation gives the antiholomorphic forms. Thus

\[
H^{1,0}(E_p)=\mathbb C\omega_p,\qquad
H^{0,1}(E_p)=\mathbb C\overline\omega_p,
\quad H^1(E_p,\mathbb C)=H^{1,0}\oplus H^{0,1}.
\tag{T2.10}
\]

The direct sum is exact because

\[
dx=\frac{\omega_p+\overline\omega_p}{2},\qquad
d\theta=\frac{\omega_p-\overline\omega_p}{2i}.
\tag{T2.11}
\]

Every factor in the positivity calculation is visible:

\[
\omega_p\wedge\overline\omega_p=-2i\,dx\wedge d\theta,
\qquad
i\int_{E_p}\omega_p\wedge\overline\omega_p
=2AB=4\pi\log p.
\tag{T2.12}
\]

Also $-i\int\overline\omega_p\wedge\omega_p=2AB$. The Hodge types of $H^0,H^1,H^2$ are respectively $(0,0)$, $(1,0)\oplus(0,1)$, and $(1,1)$. This establishes their Hodge weights $0,1,2$. It does not by itself specify an arithmetic Frobenius operator.

## T3. The actual source actions and the distinct parameter power maps

### T3.1 Parameter scaling and source Frobenius

The source identifies a morphism with

\[
\rho_z(t)=e^{zt},\qquad z\in\mathbb C,
\tag{T3.1}
\]

and then removes $z=0$. Its Weil/stalk scaling action is $z\mapsto cz$, for fixed $c\in\mathbb C^\times$. On the displayed quotient $E_p$ this becomes a translation

\[
T_c:[z]\longmapsto[cz].
\tag{T3.2}
\]

Choose any logarithm $d$ of $c$. In the full-period logarithm coordinates, $T_c$ lifts to $w\mapsto w+d$. Different logarithms differ by $iB\mathbb Z$, so they define the same map. The derivative fixes $dx,d\theta$, and the cohomology calculation (T2.1) proves

\[
T_c^*|_{H^0}=1,\qquad T_c^*|_{H^1}=I_2,
\qquad T_c^*|_{H^2}=1.
\tag{T3.3}
\]

For $c=p$, the lift translates by $A\in\Lambda_p$, so the quotient map itself is the identity:

\[
F_{\mathrm{source}}([z])=[pz]=[z].
\tag{T3.4}
\]

This is a degree-one map on $E_p$. Its $H^1$ eigenvalues are $1,1$.

There is an additional exact distinction at the level of morphisms. For a positive integer $n$, valuewise exponentiation gives

\[
(\rho_z(t))^n=e^{nzt}=\rho_{nz}(t).
\tag{T3.5}
\]

Thus **powering the values of the source morphism gives parameter scaling $z\mapsto nz$**. It does not give the parameter map $z\mapsto z^n$. Equation (T3.5) is the required comparison between the two constructions. On $E_p$, its induced map is $T_n$, which has the cohomological action (T3.3).

### T3.2 The parameter power map

For a nonzero integer $n$, define the different map

\[
P_n:E_p\longrightarrow E_p,\qquad [z]\longmapsto[z^n].
\tag{T3.6}
\]

It is well defined because $(p^kz)^n=p^{kn}z^n$. Its lift is $w\mapsto nw$, so

\[
P_n^*dx=n\,dx,\qquad P_n^*d\theta=n\,d\theta,
\quad P_n^*\omega_p=n\omega_p.
\tag{T3.7}
\]

The lattice subgroup $n\Lambda_p\subset\Lambda_p$ has index $n^2$; equivalently the kernel has the $n^2$ classes represented, with $q=|n|$, by

\[
p^{j/q}e^{iBk/q},\qquad 0\le j,k<q.
\tag{T3.8}
\]

Therefore

\[
\deg P_n=n^2,\qquad
P_n^*|_{H^0}=1,\quad
P_n^*|_{H^1}=nI_2,\quad
P_n^*|_{H^2}=n^2.
\tag{T3.9}
\]

Both radial and angular loops acquire winding $n$, including its sign. Equations (T2.7) and (T2.9) give

\[
Q_p(P_n^*\alpha,P_n^*\beta)=n^2Q_p(\alpha,\beta),\qquad
h_p(P_n^*\alpha,P_n^*\beta)=n^2h_p(\alpha,\beta).
\tag{T3.10}
\]

In particular $P_p$ has degree $p^2$ and $H^1$ eigenvalues $p,p$. Its square-root-of-degree law is $|p|=\sqrt{p^2}$, not a claim that this map has degree $p$. The map $P_0$, if included, is constant; it fixes $H^0$ and kills $H^1,H^2$.

### T3.3 Real involution and the half-turn

The source real structure is

\[
\sigma([z])=[\overline z],\qquad
(x,\theta)\longmapsto(x,-\theta).
\tag{T3.11}
\]

It preserves the lattice, so it is well defined. Its cohomology actions and form actions are

\[
\sigma^*|_{H^0}=1,\qquad
\sigma^*dx=dx,\quad\sigma^*d\theta=-d\theta,
\qquad \sigma^*|_{H^2}=-1,\quad
\sigma^*\omega_p=\overline\omega_p.
\tag{T3.12}
\]

It preserves $h_p$ and negates $Q_p$, as follows directly from (T2.7)–(T2.9). The fixed points satisfy $2\theta\in B\mathbb Z$, and therefore form the two radial circles $\theta=0,B/2\pmod B$. Equivalently $\overline z=p^kz$ forces $p^k=1$ by absolute values, then $k=0$ and $z\in\mathbb R^\times$. This reproduces the source's two real components with radial period $A$.

The parameter scaling $T_{-1}:[z]\mapsto[-z]$ is instead the translation $\theta\mapsto\theta+B/2$. Its action on all cohomology is the identity. It must not be identified with the antiholomorphic involution $\sigma$, or with the inversion $P_{-1}:[z]\mapsto[z^{-1}]$, whose $H^1$ action is $-I_2$.

## T4. Every genuine holomorphic self-isogeny has the exact degree norm

Let $f:E_p\to E_p$ be a nonconstant holomorphic map. Lift it through the universal cover to an entire function $\widetilde f:\mathbb C\to\mathbb C$. For each $\lambda\in\Lambda_p$, the difference $\widetilde f(w+\lambda)-\widetilde f(w)$ takes values in the discrete lattice and is continuous, hence is constant. It follows that $\widetilde f'$ is lattice periodic, bounded on a fundamental rectangle, and then bounded on the plane. Liouville's theorem gives

\[
\widetilde f(w)=c\,w+d,\qquad c\ne0,
\qquad c\Lambda_p\subseteq\Lambda_p.
\tag{T4.1}
\]

Conversely (T4.1) defines a holomorphic map. The translation $d$ does not affect its cohomology. For $c=a+ib$, the exact actions are

\[
f^*dx=a\,dx-b\,d\theta,\qquad
f^*d\theta=b\,dx+a\,d\theta,
\qquad f^*\omega_p=c\omega_p,
\quad f^*\overline\omega_p=\overline c\,\overline\omega_p.
\tag{T4.2}
\]

To make the descent condition explicit in the original periods, write

\[
cA=mA+r\,iB,\qquad c\,iB=sA+t\,iB,
\qquad m,r,s,t\in\mathbb Z.
\tag{T4.3}
\]

Comparison of real and imaginary parts gives exactly

\[
a=m=t,\qquad b=r\frac BA,\qquad
sA^2+rB^2=0.
\tag{T4.4}
\]

Conversely these equations imply (T4.3). In the ordered lattice basis $A,iB$, multiplication by $c$ has matrix

\[
M_c=\begin{pmatrix}m&s\\r&m\end{pmatrix}.
\tag{T4.5}
\]

The map is a covering because $c\ne0$. Its kernel is $c^{-1}\Lambda_p/\Lambda_p$, which maps bijectively onto $\Lambda_p/c\Lambda_p$ by multiplication by $c$. Thus its degree is the lattice index, and

\[
N=\deg f=\det M_c
=m^2-rs=m^2+r^2\frac{B^2}{A^2}=a^2+b^2=|c|^2.
\tag{T4.6}
\]

Positivity of this determinant also follows from the preserved complex orientation. In particular $N$ is a positive integer.

Using (T4.2) in the already derived pairing (T2.9) proves

\[
h_p(f^*\alpha,f^*\beta)=N\,h_p(\alpha,\beta),
\qquad Q_p(f^*\alpha,f^*\beta)=N\,Q_p(\alpha,\beta),
\qquad (f^*)^\dagger f^*=N I_2.
\tag{T4.7}
\]

For example, the coefficient matrix on $H^1$ is
\[
\begin{pmatrix}a&b\\-b&a\end{pmatrix}
\]
its conjugate transpose times itself is $(a^2+b^2)I_2$, and the full factor $AB$ remains in both sides of the inner-product identity. The Hodge lines in (T2.10) are eigenlines with eigenvalues $c,\overline c$. Hence

\[
|\lambda|=\sqrt N\quad\text{for every eigenvalue on }H^1,
\qquad f^*|_{H^0}=1,\quad f^*|_{H^2}=N.
\tag{T4.8}
\]

This proves the degree mechanism from the source differential: holomorphicity preserves the Hodge star, the cup integral multiplies by degree, their combination is positive, and the positive norm identity forces the square-root magnitude. No arbitrary metric or unknown endomorphism has been assumed.

There is also an exact arithmetic statement for this genuine isogeny. Its two eigenvalues solve

\[
T^2-2mT+N=0\quad\text{in }\mathbb Z[T].
\tag{T4.9}
\]

If $b\ne0$, they are the two conjugate roots and both have modulus $\sqrt N$; if $b=0$, then $c=m\in\mathbb Z$ and $N=m^2$. Thus every algebraic conjugate of an $H^1$ eigenvalue has that same modulus. This is an actual Weil-number-type conclusion for the specified isogeny. It does not identify the source deck transformation with a finite-field Frobenius.

## T5. The two degree-n maps retain opposite winding directions

Fix a positive integer $n$. In this section $p^n$ is an extended real scale, not a new prime. Define explicitly

\[
E_{p^n}=\mathbb C^\times/(p^n)^{\mathbb Z}
\cong\mathbb C/\Lambda_{p^n},\qquad
\Lambda_{p^n}=nA\mathbb Z+iB\mathbb Z.
\tag{T5.1}
\]

Use $x_n,\theta_n$ for its logarithm coordinates and retain

\[
\omega_{p^n}=dx_n+i\,d\theta_n,\qquad
\int_{E_{p^n}}dx_n\wedge d\theta_n=nAB.
\tag{T5.2}
\]

The exact maps are

\[
U_n:E_{p^n}\longrightarrow E_p,\qquad [z]_{p^n}\longmapsto[z]_p,
\tag{T5.3}
\]

\[
V_n:E_p\longrightarrow E_{p^n},\qquad [z]_p\longmapsto[z^n]_{p^n}.
\tag{T5.4}
\]

For $U_n$, descent follows from $\Lambda_{p^n}\subset\Lambda_p$, and its lift is $w\mapsto w$. For $V_n$, descent follows from $n\Lambda_p\subset\Lambda_{p^n}$, and its lift is $w\mapsto nw$. The two lattice indices are

\[
[\Lambda_p:\Lambda_{p^n}]=n,\qquad
[\Lambda_{p^n}:n\Lambda_p]=n.
\tag{T5.5}
\]

Thus both maps have degree $n$. Their kernels, including the distinct directions, are

\[
\ker U_n=\{[p^j]_{p^n}:0\le j<n\},\qquad
\ker V_n=\{[e^{iBk/n}]_p:0\le k<n\}.
\tag{T5.6}
\]

For the second formula, $z^n=p^{nj}$ gives $z=p^je^{iBk/n}$, and the factor $p^j$ disappears exactly in the domain quotient. Both compositions are the parameter power map on the appropriate curve:

\[
U_n\circ V_n=P_n\text{ on }E_p,
\qquad V_n\circ U_n=P_n\text{ on }E_{p^n}.
\tag{T5.7}
\]

On the original forms the pullbacks are

\[
U_n^*dx=dx_n,\quad U_n^*d\theta=d\theta_n,
\quad V_n^*dx_n=n\,dx,\quad V_n^*d\theta_n=n\,d\theta.
\tag{T5.8}
\]

On the positive radial and angular cycles they have the distinct winding matrices

\[
(U_n)_*:r_{p^n}\mapsto n r_p,\ a_{p^n}\mapsto a_p,
\qquad
(V_n)_*:r_p\mapsto r_{p^n},\ a_p\mapsto n a_{p^n}.
\tag{T5.9}
\]

For example, $V_n(e^{At})=e^{nAt}$ traverses the target radial period once, whereas $V_n(e^{iBt})=e^{inBt}$ traverses its unchanged angular period $n$ times. The matrices are therefore diagonal $\operatorname{diag}(n,1)$ and $\operatorname{diag}(1,n)$ on homology in the displayed source/target cycle bases. The pullback matrices on the corresponding integral dual bases are the same diagonal matrices; this is compatible with (T5.8) because the radial periods are $A$ and $nA$, not equal.

On $H^0$, both pullbacks fix $1$. On the full area forms,

\[
U_n^*(dx\wedge d\theta)=dx_n\wedge d\theta_n,
\qquad
V_n^*(dx_n\wedge d\theta_n)=n^2dx\wedge d\theta.
\tag{T5.10}
\]

There is no contradiction with their degree $n$: the exact integral fundamental classes are represented by $dx\wedge d\theta/(AB)$ and $dx_n\wedge d\theta_n/(nAB)$, so both pullbacks multiply the target fundamental class by $n$. All area factors are retained in this comparison.

## T6. The adjoint identity, with both volumes retained

Write $H_p=H^1(E_p,\mathbb C)$ and $H_{p^n}=H^1(E_{p^n},\mathbb C)$. Their positive forms are

\[
h_p(a\,dx+b\,d\theta,c\,dx+d\,d\theta)
=AB(a\overline c+b\overline d),
\tag{T6.1}
\]

\[
h_{p^n}(a\,dx_n+b\,d\theta_n,c\,dx_n+d\,d\theta_n)
=nAB(a\overline c+b\overline d).
\tag{T6.2}
\]

For $\alpha=a\,dx+b\,d\theta$ and $\beta=c\,dx_n+d\,d\theta_n$, equations (T5.8) give

\[
h_{p^n}(U_n^*\alpha,\beta)
=nAB(a\overline c+b\overline d)
=h_p(\alpha,V_n^*\beta).
\tag{T6.3}
\]

Therefore, with adjoints taken between the indicated spaces,

\[
(U_n^*)^\dagger=V_n^*,\qquad
(V_n^*)^\dagger=U_n^*,
\tag{T6.4}
\]

\[
(U_n^*)^\dagger U_n^*=nI_{H_p},\qquad
(V_n^*)^\dagger V_n^*=nI_{H_{p^n}}.
\tag{T6.5}
\]

This also follows by pullback from the two compositions (T5.7), whose $H^1$ action is $nI$, but equation (T6.3) proves that the compositional partners really are adjoints for the source-defined positive forms. Consequently all singular values of either pullback are $\sqrt n$. These are maps between two different cohomology spaces, so it would be incorrect to call these singular values eigenvalues of an endomorphism of $H_p$.

The corresponding cup identities are

\[
Q_{p^n}(U_n^*\alpha,U_n^*\alpha')=nQ_p(\alpha,\alpha'),
\qquad Q_p(V_n^*\beta,V_n^*\beta')=nQ_{p^n}(\beta,\beta').
\tag{T6.6}
\]

They follow either from (T2.7) and the full areas, or from the proven degree and change of variables. The complex structures commute with both pullbacks by (T5.8).

## T7. An actual polarized product receiver and its full weight spectrum

The inter-curve correspondence has an exact receiver as a holomorphic self-isogeny. Use the displayed origins $[1]$ and form the product of the two source-model elliptic curves

\[
\mathcal A_{p,n}=E_p\times E_{p^n},\qquad
\Phi_{p,n}(u,v)=(U_n(v),V_n(u)).
\tag{T7.1}
\]

It is a complex torus of complex dimension two. The product of the source elliptic algebraic structures also makes it an abelian surface. In logarithm coordinates its lift is exactly

\[
(w_1,w_2)\longmapsto(w_2,nw_1),
\quad
(w_1,w_2)\in\mathbb C^2/
(\Lambda_p\oplus\Lambda_{p^n}).
\tag{T7.2}
\]

The two descent inclusions have already been proved in T5. Its kernel is $\ker V_n\times\ker U_n$, so

\[
\deg\Phi_{p,n}=n^2,
\qquad \Phi_{p,n}^2=[n]_{\mathcal A_{p,n}}.
\tag{T7.3}
\]

This degree $n^2$ is appropriate to complex dimension two and is not replaced by $n$.

The positive integral alternating forms on the two original lattices are

\[
\mathscr E_p((x,\theta),(x',\theta'))
=\frac{x\theta'-\theta x'}{AB},
\tag{T7.4}
\]

\[
\mathscr E_{p^n}((x_n,\theta_n),(x_n',\theta_n'))
=\frac{x_n\theta_n'-\theta_nx_n'}{nAB}.
\tag{T7.5}
\]

In their respective original lattice bases $A,iB$ and $nA,iB$, both have integer matrix $\begin{pmatrix}0&1\\-1&0\end{pmatrix}$, of determinant one. Moreover $\mathscr E(v,Jv)>0$ for nonzero real $v$, since its numerator is $x^2+\theta^2$ (respectively $x_n^2+\theta_n^2$). They therefore give the principal polarizations with all original period factors shown. Their associated two-forms are

\[
\Omega_{p,n}
=\frac{dx\wedge d\theta}{AB}
+\frac{dx_n\wedge d\theta_n}{nAB}.
\tag{T7.6}
\]

This is the product principal polarization. Direct substitution of (T7.2) gives the exact multiplier identity

\[
\Phi_{p,n}^*\Omega_{p,n}=n\Omega_{p,n}.
\tag{T7.7}
\]

The factors are essential: the first summand pulls back to $dx_n\wedge d\theta_n/(AB)$, while the second pulls back to $n^2dx\wedge d\theta/(nAB)$.

The duality of $U_n,V_n$ can also be checked before taking cohomology. For $v\in\mathbb C$ in the $E_{p^n}$ tangent space and $w\in\mathbb C$ in the $E_p$ tangent space,

\[
\mathscr E_p(U_n v,w)=\mathscr E_{p^n}(v,V_n w).
\tag{T7.8}
\]

Both sides are $(x_v\theta_w-\theta_vx_w)/(AB)$. Together with the integral lattice maps, this proves that $V_n$ is the polarized dual of $U_n$. For the product alternating form, (T7.8) proves

\[
\mathscr E_{\mathrm{prod}}(\Phi_{p,n}v,w)
=\mathscr E_{\mathrm{prod}}(v,\Phi_{p,n}w).
\tag{T7.9}
\]

Thus the Rosati adjoint of this actual product isogeny equals itself. Equations (T7.3) and (T7.9) give

\[
\Phi_{p,n}^{\dagger}\Phi_{p,n}=[n].
\tag{T7.10}
\]

On $H^1(\mathcal A_{p,n},\mathbb C)=H_p\oplus H_{p^n}$, the pullback is the explicit exchange operator

\[
F_1(\alpha,\beta)=(V_n^*\beta,U_n^*\alpha).
\tag{T7.11}
\]

Its positive Hermitian form is exactly $h_p\oplus h_{p^n}$, with factors $AB,nAB$. This form is the one obtained from the product polarization: the alternating form on $H^1$ is $\int_{\mathcal A}\alpha\wedge\beta\wedge\Omega_{p,n}$. For classes both from the first factor, the second summand of $\Omega$ integrates to one, leaving $Q_p$; for classes both from the second factor, the first summand integrates to one, leaving $Q_{p^n}$; mixed terms vanish by degree on each two-dimensional real factor. Combining this with $-J^*$ gives exactly the displayed direct sum of (T6.1) and (T6.2).

Consequently T6 proves, without a new choice of inner product,

\[
F_1^\dagger=F_1,\qquad
F_1^2=nI_4,\qquad
h_{\mathrm{prod}}(F_1a,F_1b)=n\,h_{\mathrm{prod}}(a,b).
\tag{T7.12}
\]

Since $n>0$, the polynomial $T^2-n$ has two distinct roots. The invariant real-form pairs $(dx,dx_n)$ and $(d\theta,d\theta_n)$ each have coefficient matrix

\[
\begin{pmatrix}0&n\\1&0\end{pmatrix}.
\tag{T7.13}
\]

Hence

\[
\det(TI_4-F_1)=(T^2-n)^2,
\quad \operatorname{Spec}(F_1)=
\{\sqrt n,\sqrt n,-\sqrt n,-\sqrt n\}.
\tag{T7.14}
\]

For $\lambda=\pm\sqrt n$, explicit eigenforms are

\[
\lambda\,dx+dx_n,\qquad
\lambda\,d\theta+d\theta_n,
\qquad
\lambda\,\omega_p+\omega_{p^n}\in H^{1,0}.
\tag{T7.15}
\]

All original period data remains attached to the four forms. Their eigenvalues have modulus $\sqrt n$; if $n$ is nonsquare, its two algebraic conjugates are the two displayed signs and have the same modulus. If $n$ is square, they are integers with the stated modulus.

For completeness the entire cohomology ring of this real four-torus is the exterior algebra on the four invariant one-forms. This follows by the same Fourier argument as T2 in four variables: on a nonzero frequency vector $k$, exterior multiplication by $ik$ is the de Rham differential, and contraction by $k/(i|k|^2)$ satisfies the identity $d\iota+\iota d=1$. Thus every nonzero Fourier mode is contractible, whereas invariant forms survive by their periods on products of lattice loops. This proves the ring statement, rather than merely applying a dimension count. Since pullback commutes with wedge product,

\[
\Phi_{p,n}^*|_{H^k}=\bigwedge^k F_1,
\quad \dim H^k=\binom4k.
\tag{T7.16}
\]

Every eigenvalue is therefore a product of $k$ eigenvalues in (T7.14), and every one has modulus

\[
|\lambda_k|=n^{k/2},\qquad 0\le k\le4.
\tag{T7.17}
\]

The complete spectra, including signs and multiplicities, are

| Degree | Eigenvalues of the actual product-isogeny pullback |
|---|---|
| $0$ | $1$, multiplicity $1$ |
| $1$ | $+\sqrt n$, multiplicity $2$; $-\sqrt n$, multiplicity $2$ |
| $2$ | $+n$, multiplicity $2$; $-n$, multiplicity $4$ |
| $3$ | $+n^{3/2}$, multiplicity $2$; $-n^{3/2}$, multiplicity $2$ |
| $4$ | $n^2$, multiplicity $1$ |

For degree two, the two positive products come from choosing both positive eigenlines or both negative eigenlines; the four mixed choices have negative sign. For degree three, the two choices with two negative eigenlines have positive sign, and the two with one negative eigenline have negative sign. The top product is $n^2$, agreeing with the degree (T7.3).

The full determinant factors, useful without any loss of signs or multiplicities, are

\[
\begin{aligned}
\det(I-T\Phi^*|H^0)&=1-T,\\
\det(I-T\Phi^*|H^1)&=(1-nT^2)^2,\\
\det(I-T\Phi^*|H^2)&=(1-nT)^2(1+nT)^4,\\
\det(I-T\Phi^*|H^3)&=(1-n^3T^2)^2,\\
\det(I-T\Phi^*|H^4)&=1-n^2T.
\end{aligned}
\tag{T7.18}
\]

In particular choosing $n=p$ gives an actual degree-$p^2$ polarized self-isogeny of $E_p\times E_{p^p}$, with multiplier $p$, whose cohomological eigenvalues satisfy the exact powers $p^{k/2}$. The second factor has radial period $p\log p$, angular period $2\pi$, and scale $p^p$. This construction does not assert that $p^p$ is a prime, that the second curve was already a separate prime stalk, or that $\Phi$ is the source's parameter Frobenius.

## T8. Torsor origins, real compatibility, and the exact limitation

The source's intrinsic description is a torsor. The group formulas $P_n,V_n,[n]$ above use the displayed model $\mathbb C^\times/p^{\mathbb Z}$ with origin $[1]$, and the analogous origin on $E_{p^n}$. A different identification $z'=cz$ changes the parameter power operation, expressed back in the previous coordinate, to

\[
z\longmapsto c^{n-1}z^n.
\tag{T8.1}
\]

This differs from $P_n$ or $V_n$ by a translation in its target. If independent origins are chosen for the two factors, each component changes by a target translation for the same reason. Such translations act trivially on cohomology by T3.1 and preserve the invariant differential and polarization forms. Therefore all cohomological maps, adjoint relations, eigenvalues, degrees, and winding maps proved above are independent of these translated choices. The group equality $\Phi^2=[n]$ is asserted for the displayed origins; without those origins its affine version can contain an additional translation. No origin-independent identity of torsor points is being silently assumed.

The real structures commute with $U_n$ and $V_n$ because complex conjugation commutes with both $z\mapsto z$ and $z\mapsto z^n$. Hence the product real involution commutes with $\Phi$ and with $F_1$, and it exchanges the holomorphic and antiholomorphic eigenforms of the same real eigenvalue in (T7.15). In the four real one-form directions it has signs $+,-,+,-$, each with its original radial or angular label.

A proposed degree-$n$ self-map of the single real torus that stretches only one winding direction must be tested against the source complex structure. For example

\[
R_n:(x,\theta)\longmapsto(nx,\theta)
\tag{T8.2}
\]

is well defined and has topological degree $n$. For $n>1$, however,

\[
dR_n(J\partial_x)=\partial_\theta,
\qquad J(dR_n\partial_x)=n\partial_\theta,
\tag{T8.3}
\]

so it is not holomorphic. Its $H^1$ eigenvalues are $n,1$, and

\[
h_p(R_n^*\alpha,R_n^*\alpha)
=AB(n^2|a|^2+|b|^2)
\ne nAB(|a|^2+|b|^2)
\tag{T8.4}
\]

for general $\alpha=a\,dx+b\,d\theta$. Nor can any other positive inner product make this particular operator satisfy a common factor $n$: applying that proposed identity to its nonzero eigenvector with eigenvalue $n$ would force $n^2h(v,v)=nh(v,v)$, impossible when $n>1$. The failure identifies a precise complex-structure defect. T5–T7 repair that defect by retaining the changed radial period in a second curve and constructing an exact holomorphic correspondence and product isogeny. They do not declare the original objects unrelated.

Thus the degree/positivity mechanism is fully realized here on specified complex curves and on a specified product, while the original source Frobenius remains exactly the identity on the single quotient $E_p$. An additional map from any tau-support object into these source receivers is a separate construction and is neither presumed nor assigned coordinates in this derivation.

## Appendix T9. Optional self-endomorphism classification for algebraic p

**Source-use status.** This appendix invokes the classical Gelfond–Schneider theorem as an external theorem. No original-source proof of that theorem has been acquired or read in this subtask. Its precise statement and full application are given to keep this dependence visible. None of T1–T8, including the product receiver and its weight spectrum, requires this appendix.

The theorem states: if $a\in\overline{\mathbb Q}\setminus\{0,1\}$ and $b\in\overline{\mathbb Q}\setminus\mathbb Q$, then every value $\exp(bL)$, where $e^L=a$, is transcendental.

Suppose that the positive real number $A/B=\log p/(2\pi)$ were algebraic. Then

\[
b=-2i\frac AB
\tag{T9.1}
\]

would be algebraic and nonreal, hence irrational. Set $a=-1$ and use its logarithm $L=iB/2=i\pi$. The full power calculation is

\[
\exp(bL)
=\exp\!\left(\left(-2i\frac AB\right)\left(\frac{iB}{2}\right)\right)
=e^A=p.
\tag{T9.2}
\]

This contradicts Gelfond–Schneider because the source prime $p$ is algebraic. Therefore $A/B$ is transcendental. The argument works for every algebraic real $p>1$.

If the coefficient $r$ in (T4.4) were nonzero, then $s\ne0$ and

\[
\left(\frac AB\right)^2=-\frac rs\in\mathbb Q,
\tag{T9.3}
\]

which would make $A/B$ algebraic, a contradiction. Hence $r=s=0$, $c=m\in\mathbb Z$, and the exact endomorphism ring is

\[
\operatorname{End}_{\mathrm{hol}}(E_p)=\mathbb Z.
\tag{T9.4}
\]

Using the affine classification (T4.1), every holomorphic self-map in the displayed multiplicative model has form $[z]\mapsto[c_0z^m]$ for some $c_0\in\mathbb C^\times$ and $m\in\mathbb Z$. It is constant for $m=0$, and otherwise its degree is $m^2$. For prime $p$, the integer equation $m^2=p$ has no solution. Thus $E_p$ has no holomorphic self-map of degree $p$. For an arbitrary integer $p>1$, a degree-$p$ self-isogeny exists precisely when $p$ is a perfect square. The actual degree-$p$ maps $U_p,V_p$ of T5 run between $E_p$ and $E_{p^p}$, and the product construction of T7 gives an actual self-isogeny without contradicting this single-curve classification.
