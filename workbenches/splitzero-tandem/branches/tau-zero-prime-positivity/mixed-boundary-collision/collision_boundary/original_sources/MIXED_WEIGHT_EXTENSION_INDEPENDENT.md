# Independent derivation of the mixed boundary collision comparison

Date: 2026-09-23.

This note independently derives the algebra in BCE5–27 of
MIXED_BOUNDARY_COLLISION_EXTENSION.tex from its coefficient definitions.
It also checks the coefficient base changes of BCE1–4 and the formal
support operations of BCE28. It does not independently reprove the
adelic boundary injection GSB1–22a or the finite-spectrum theorem FL1–15.
Those geometric assertions remain identified inputs.

The complete current BCE source and the complete
COLLISION_FROBENIUS_FILTRATION_AND_SUPPORT.tex were read. This derivation
does not use the previous agent's reported conclusions as evidence.
No source-reading claim beyond these two files is made here.

## 1. Original algebra and differential extension

Let \(O=\mathbb Z_3\), \(K=\mathbb Q_3\), \(c\in O\), and retain
\[
C=O[\epsilon,T]/(\epsilon^2,T^2-6\epsilon),\qquad z=\epsilon T.
\]
Successive division by the two monic polynomials gives the \(O\)-basis
\(1,\epsilon,T,z\). Its multiplication identities are
\[
\epsilon^2=0,\quad T^2=6\epsilon,\quad \epsilon T=z,\quad
\epsilon z=Tz=z^2=0.
\]
Thus \(M=O\epsilon\oplus OT\oplus Oz\) satisfies
\(M^2=6O\epsilon\oplus Oz\), \(M^3=6Oz\), \(M^4=0\).
Since \(C/M=O\) is reduced, \(M\) is exactly the nilradical.

Define \(F|_O=1\), \(F(\epsilon)=0\), \(F(T)=9cz\).
The relations map to zero, so this defines an algebra map, with
\[
F_M(T)=9cz,\qquad F_M(\epsilon)=F_M(z)=0,\qquad F_M^2=0.
\]

The equations \(\epsilon^2,T^2-6\epsilon\) form a regular sequence:
the first is a nonzero divisor in the polynomial ring, and the second
is monic in \(T\) after quotienting by the first. The cotangent complex
therefore has the two-term presentation
\[
C^2\xrightarrow{A}C\,d\epsilon\oplus C\,dT,\qquad
A=\begin{pmatrix}2\epsilon&-6\\0&2T\end{pmatrix}.
\]
Put \(u=d\epsilon\), \(v=dT\), \(q=\epsilon v\).
Because 2 is a unit, the first column and its multiples impose
\(\epsilon u=zu=0\). The second column gives \(Tv=3u\);
its \(\epsilon\)-multiple gives \(zv=0\); its \(T\)-multiple gives
\(3(Tu-2\epsilon v)=0\). All other multiples follow: multiplying this
last relation by \(T\) or \(\epsilon\) vanishes using the preceding ones.
Set \(w=Tu-2q\). Elimination of \(\epsilon u,zu,Tv,zv\), followed by
\(Tu=w+2q\), proves the exact presentation
\[
\Omega=\Omega_{C/O}=Ou\oplus Ov\oplus Oq\oplus(O/3)w.
\]
Thus \(w\) has exact order 3 and \(u,v,q\) are independent free coordinates.

The universal differential restricted to \(M\) is \(O\)-linear:
\[
d_M(\epsilon)=u,\quad d_M(T)=v,\quad d_M(z)=w+3q.
\]
The image of \(a\epsilon+bT+hz\) has free coordinates \(a,b,3h\);
these vanish only if \(a=b=h=0\). Hence \(d_M\) is injective.
Its cokernel has \(u=v=0\), \(w=-3q\), \(3w=0\), and is exactly
\(Q=O/9\), with
\[
\rho(u)=\rho(v)=0,\quad\rho(q)=1,\quad\rho(w)=-3.
\]
We have proved
\[
0\longrightarrow M\xrightarrow{d_M}\Omega
\xrightarrow{\rho}Q\longrightarrow0. \tag{I1}
\]
The lift \(q\) of \(1\) satisfies \(9q=3d_M(z)\).
Using \(O\xrightarrow9O\) as the resolution of \(Q\), its extension
class is \([3z]\in M/9M\), of exact order 3. Changing \(q\) by
\(d_M(y)\) changes the representative by \(9y\). Since \(3z\notin9M\),
(I1) is not split.

The induced Frobenius is
\[
F_\Omega(u)=F_\Omega(q)=F_\Omega(w)=0,\qquad
F_\Omega(v)=d(9cz)=9c(w+3q)=27cq.
\]
The term \(9cw\) vanishes because \(3w=0\); the coefficient \(27c\)
is retained. On the quotient \(F_Q=0\). Direct evaluation on the
basis of \(M\) proves \(F_\Omega d_M=d_MF_M\), and
\(\rho F_\Omega=0=F_Q\rho\). Thus (I1) is exact in \(O\)-modules
with an endomorphism. It is not being declared a sequence of
\(C\)-module maps: \(d_M\) obeys Leibniz.

## 2. Comparison complex and Ext sign

Let \(m\ge0\), \(a=3^m\), and let \(F_E\) be an \(O\)-linear
endomorphism of an \(O\)-module \(E\). Define
\[
\mathcal K_m(E)=[E\xrightarrow{a-F_E}E]
\]
in cohomological degrees 0 and 1.
Put \(R=O[t]\), \(O_a=(O,t=a)\), and \(E_F=(E,t=F_E)\).
There is an exact augmented free resolution
\[
0\longrightarrow R\xrightarrow{a-t}R
\longrightarrow O_a\longrightarrow0. \tag{I2}
\]
Evaluation at \(a\) gives its quotient. Division by \(t-a\) gives
the kernel; the highest polynomial coefficient proves injectivity.

Use the chain-resolution convention whose Hom differential is
precomposition with \(a-t\). This gives exactly \(a-F_E\).
If instead one uses the signed cochain Hom convention, the
corresponding degree-one sign isomorphism gives the same displayed
complex. Thus
\[
H^0\mathcal K_m(E)=\operatorname{Hom}_R(O_a,E_F),\qquad
H^1\mathcal K_m(E)=\operatorname{Ext}^1_R(O_a,E_F),
\]
and all higher Ext groups vanish.

An explicit extension fixes the sign: the class of \(x\in E\) is
represented by \(E\oplus O\widetilde1\) with
\[
t|_E=F_E,\qquad t\widetilde1=a\widetilde1-x. \tag{I3}
\]
Indeed \((a-t)\widetilde1=x\).
Every extension has this form because its underlying \(O\)-module
sequence splits. Replacing the lift by \(\widetilde1+y\) replaces
\(x\) by \(x+(a-F_E)y\). Conversely this change gives an
isomorphism fixing the ends. This proves the Ext classification,
splitting criterion, and sign in BCE9.

## 3. Every tensor order and its invariant factors

Let \(k\ge1\), \(M_k=M^{\otimes_O k}\), \(n=3^k\), \(b=(9c)^k\).
Keep the word basis in \(\epsilon,T,z\), and denote
\(e_T=T^{\otimes k}\), \(e_z=z^{\otimes k}\).
Then \(F_k=F_M^{\otimes k}\) sends \(e_T\) to \(be_z\) and
kills each other word. Hence \(F_k^2=0\).
For \(L=aI-F_k\),
\[
L^{-1}=a^{-1}I+a^{-2}F_k\quad\text{over }K, \tag{I4}
\]
because multiplication in either order gives \(I-a^{-2}F_k^2=I\).
The original free module embeds into its scalar extension to \(K\),
so \(\ker L=0\) over \(O\).
In the order \(e_z,e_T\), the original exceptional block is
\[
B=\begin{pmatrix}a&-b\\0&a\end{pmatrix}; \tag{I5}
\]
all other coordinates are multiplication by \(a\).

Set \(v_3(0)=+\infty\) and \(\nu=\min(m,2k+kv_3(c))\).
If \(a\mid b\), add \(b/a\) times the first column to the second:
the block becomes \(aI_2\), giving \(\nu=m\), including \(b=0\).
If \(b=3^\nu u\), \(u\in O^\times\), \(\nu<m\), put
\(h=3^{m-\nu}\). The block is
\(3^\nu\left(\begin{smallmatrix}h&-u\\0&h\end{smallmatrix}\right)\).
Use these invertible operations over \(O\):

1. Exchange the two columns.
2. Multiply the first row by \(-u^{-1}\).
3. Subtract \(h\) times the first row from the second.
4. Add \(h/u\) times the first column to the second.
5. Multiply the second row by \(u\).

The diagonal entries become \(3^\nu\) and
\(3^\nu h^2=3^{2m-\nu}\).
These operations prove invariant factors and do not substitute
new coordinates for the connecting or pairing formulas.
For every \(c\in O\), \(m\ge0\), \(k\ge1\),
\[
H^0\mathcal K_m(M_k)=0,\qquad
H^1\mathcal K_m(M_k)\cong
(O/3^m)^{3^k-2}\oplus O/3^\nu\oplus O/3^{2m-\nu}. \tag{I6}
\]
Here \(O/3^0=0\). Its finite order is \(3^{m3^k}\),
matching \(\det L=a^{3^k}\).
Equation (I4) gives a contraction of the rationalized two-term
complex; it does not delete its integral cokernel.

## 4. Transpose torsion pairing and detector

Using the original coordinate dual, define
\[
\operatorname{coker}L\times\operatorname{coker}L^t\to K/O,\qquad
([x],[y])\longmapsto y^tL^{-1}x\bmod O. \tag{I7}
\]
Replacing \(x\) by \(x+Lu\) adds \(y^tu\in O\);
replacing \(y\) by \(y+L^tv\) adds \(v^tx\in O\).
Thus it is well-defined. If all pairings against integral \(y\)
vanish, all coordinates of \(L^{-1}x\) lie in \(O\), so \(x\in LM_k\).
The transpose argument gives \(y\in L^tM_k\) for the other radical.
Both radicals are zero.

A character \(O/3^h\to K/O\) is specified by an element of
\(3^{-h}O/O\), a group of order \(3^h\). The finite invariant
factors in (I6) show that both sides and their character modules
have the same order. The injective character maps are therefore
isomorphisms, proving perfection.
The transpose receiver is necessary: this is not an assertion of
a symmetric, Hermitian, or ordered form on one module.

For \(k=1\), selecting the \(z\)-coordinate row of (I4) gives
\[
\lambda_m([x_\epsilon\epsilon+x_TT+x_zz])
=\frac{x_z}{3^m}+\frac{9c\,x_T}{3^{2m}}\pmod O. \tag{I8}
\]
The coordinates of \(Ly\) are
\(a y_\epsilon,a y_T,a y_z-9cy_T\); substitution gives exactly
\(\lambda_m(Ly)=y_z\bmod O=0\).
This directly verifies the sign and coefficient \(9c\).

## 5. The connecting map for every \(m\)

Applying \(\mathcal K_m\) to (I1) gives a short exact sequence of
complexes. For \(m\ge1\), \(H^0\mathcal K_m(M)=0\).
On the independent coordinates of \(\Omega\), the differential sends
\[
xu+yv+hq+tw\longmapsto
axu+ayv+(ah-27cy)q+atw.
\]
Its free coordinates vanish only when \(x=y=h=0\);
\(atw=0\) because \(m\ge1\) and \(3w=0\). Thus, with
\(s=\max(0,2-m)\),
\[
H^0\mathcal K_m(\Omega)=(O/3)w,\qquad
H^0\mathcal K_m(Q)=Q[3^m]=3^sO/9. \tag{I9}
\]
The preceding kernel map sends \(w\) to \(-3\).
For \(m=0\), all three operators \(1-F\) are invertible
with inverse \(1+F\), since \(F^2=0\); every cohomology group is zero.

Lift \(3^s\in Q[3^m]\) to \(3^sq\). Its differential is
\[
(3^m-F_\Omega)(3^sq)=3^{m+s}q
=3^{m+s-1}d_M(z).
\]
Since \(m+s\ge2\), the \(w\)-term in the right hand side is
annihilated exactly. The connecting map, with the fixed sign, is
\[
\delta_m(3^s)=[3^{m+s-1}z]\in M/(3^m-F_M)M. \tag{I10}
\]

The order of \([z]\) is exactly \(3^m\). If
\(hz=(3^m-F_M)(x\epsilon+yT+tz)\), comparison of the free
\(\epsilon,T\) coordinates forces \(x=y=0\), and then \(h=3^mt\).
The converse follows from \(Lz=3^mz\).
Consequently
\[
\delta_1(3)=[3z]=0;
\]
\[
\delta_m(1)=[3^{m-1}z]\ne0,\qquad
3\delta_m(1)=0,\qquad
\ker\delta_m=3O/9\quad(m\ge2). \tag{I11}
\]
This is independent of \(c\).
For \(m=1\), the map \(w\mapsto-3\) is onto \(Q[3]\);
for \(m\ge2\), its image is \(3O/9\), agreeing with (I11).
No order-nine term has been omitted.

When \(m=1\), the free image on \(\Omega\) is
\(3Ou+3Ov+3Oq\), with no \(w\)-component. Hence
\[
\begin{aligned}
&H^1\mathcal K_1(M)=(O/3)\{\epsilon,T,z\},\\
&H^1\mathcal K_1(\Omega)=(O/3)\{u,v,q,w\},\\
&H^1\mathcal K_1(Q)=O/3,\\
&d_{M,*}(\epsilon)=u,\quad d_{M,*}(T)=v,\quad d_{M,*}(z)=w,\\
&\rho_*q=1,\quad\rho_*u=\rho_*v=\rho_*w=0.
\end{aligned} \tag{I12}
\]
For arbitrary \(m\ge1\), the original \(q,v\) block is
\(\left(\begin{smallmatrix}3^m&-27c\\0&3^m\end{smallmatrix}\right)\).
The row and column proof of section 3 applies; the \(u\) coordinate
contributes \(O/3^m\), and the \(w\) coordinate contributes \(O/3\).
Writing \(\mu=\min(m,3+v_3(c))\), we get
\[
H^1\mathcal K_m(\Omega)\cong
O/3^m\oplus O/3^\mu\oplus O/3^{2m-\mu}\oplus O/3,\qquad
H^1\mathcal K_m(Q)=O/3^{\min(m,2)}. \tag{I13}
\]
The original maps remain \(d_{M,*}(z)=w+3q\),
\(\rho_*(q)=1,\rho_*(w)=-3\); the invariant factor presentation
does not replace them by unspecified maps.

Finally, (I8) and (I11) give the exact nonzero value
\[
\lambda_m\delta_m(1)=1/3\bmod O\ne0\quad(m\ge2). \tag{I14}
\]
It detects the entire order-three image. Every additive map from
this image to a characteristic-zero vector space vanishes, since
such a target has no nonzero element killed by 3. This concerns
those specified additive maps, not every possible arithmetic use
of the original extension.

## 6. Cotangent cycles and the fixed-degree-zero chain lift

For a vector \((a_0,b_0)\) in the kernel of \(A\), the lower equation
is \(Tb_0=0\); basis comparison forces \(b_0=t z\), \(t\in O\).
The upper equation is \(\epsilon a_0=3tz\). It forces the scalar
coefficient of \(a_0\) to vanish and its \(T\)-coefficient to be
\(3t\); the \(\epsilon,z\) coefficients are free. Therefore
\[
H=H^{-1}(L_{C/O})=Ov_1\oplus Ov_2\oplus Ov_3,\quad
v_1=(\epsilon,0),\ v_2=(z,0),\ v_3=(3T,z). \tag{I15}
\]

Lift \(F\) to the polynomial ring by
\(\epsilon\mapsto0,\ T\mapsto9c\epsilon T\).
The relation generators map to \(0,81c^2T^2\epsilon^2\).
The induced degree-minus-one semilinear matrix over \(C\) is
\[
\begin{pmatrix}0&486c^2\epsilon\\0&0\end{pmatrix}.
\]
It is applied to the \(F\)-images of coefficient vectors.
The second coordinates of \(v_1,v_2,v_3\) are \(0,0,z\), whose
\(F\)-images vanish; thus \(F_H=0\).

Retain the injection
\[
\kappa(\epsilon)=3v_1,\quad
\kappa(T)=v_3-2v_2,\quad\kappa(z)=3v_2. \tag{I16}
\]
Its free coordinates prove injectivity. The identities
\[
\epsilon v_1=\epsilon v_2=0,\quad\epsilon v_3=3v_2,\quad
Tv_1=v_2,\quad Tv_2=0,\quad Tv_3=18v_1
\]
prove its \(C\)-linearity by checking \(\epsilon,T\).
Its original Frobenius defect is
\[
\Delta=\kappa F_M-F_H\kappa,\qquad
\Delta(T)=27cv_2,\quad\Delta(\epsilon)=\Delta(z)=0. \tag{I17}
\]
For \(c\ne0\), it remains nonzero over \(K\).

Fix the degree-zero component of a chain map
\(\mathcal K_m(M)\to\mathcal K_m(H)\) to equal \(\kappa\).
Its degree-one component \(g\) must satisfy
\[
g(3^m-F_M)=3^m\kappa. \tag{I18}
\]
After extension to \(K\), (I4) forces uniquely
\[
g=\kappa+3^{-m}\kappa F_M. \tag{I19}
\]
In the original coordinates,
\[
g(\epsilon)=3v_1,\quad g(z)=3v_2,\quad
g(T)=v_3-2v_2+3^{3-m}cv_2.
\]
This is integral exactly when \(27c\in3^mO\).
Uniqueness over \(K\), and injectivity of the scalar extension of
the free source and target, prove integral uniqueness as well.
Conversely,
\[
(\kappa+3^{-m}\kappa F_M)(3^m-F_M)
=3^m\kappa-\kappa F_M+\kappa F_M-3^{-m}\kappa F_M^2
=3^m\kappa,
\]
proving the chain equation and its positive correction.
For \(c\ne0\), existence is \(m\le3+v_3(c)\); for \(c=0\),
it holds for every \(m\ge0\).

In these particular modules the correction is also \(C\)-linear:
\(\kappa F_M\) kills \(M^2=6O\epsilon+Oz\), and its image lies
in \(Ov_2\), annihilated by \(\epsilon,T\). Thus the integral
map \(g\) is \(C\)-linear, although only \(O\)-linearity is
needed for this comparison.

The exact obstruction to the fixed-degree-zero problem is
\[
\operatorname{ob}_m(\kappa):M\to H/3^mH,\quad
T\mapsto27cv_2,\quad\epsilon,z\mapsto0. \tag{I20}
\]
It vanishes exactly under the displayed divisibility condition.
For \(c\ne0\) and \(m>3+v_3(c)\), its image has exact order
\(3^{m-3-v_3(c)}\), by the coefficient in the free \(v_2\) direction.
Where \(g\) exists and \(m\ge2\),
\[
g_*\delta_m(1)=[3^{m-1}g(z)]=[3^mv_2]=0
\quad\text{in }H/3^mH. \tag{I21}
\]
This zero image and (I14)'s nonzero detector are different,
explicitly evaluated receivers of the same class.

The chain lift does not repair Frobenius equivariance of the
coefficient injection. The defect (I17) persists; moreover
\(gF_M(T)=27cv_2\). The result is a chain map with different
degree-zero and degree-one components. For \(c\ne0\) it is not
an \(O[t]\)-linear coefficient map \(M_F\to H_0\) inducing both
components. BCE22–25 formulate the two-term problem correctly.

## 7. Boundary lattice and all-prime Hom family

Fix \(r\ge2\), \(1\le m<r\), \(j\ge1\). Let
\[
\mathcal A=\{A\subset\{1,\ldots,r\}:|A|=m\},\quad
X=\mathcal A^{\{\infty\}\sqcup\mathcal P},\quad
E=\{(A,A,\ldots):A\in\mathcal A\}.
\]
For a coefficient ring \(S\), let \(I(S)\) be the locally constant
functions on \(X\) vanishing on \(E\), and put
\[
B(S)=I(S)\otimes_S
\Lambda^j\left(\bigoplus_{p\in\mathcal P}S\vartheta_p\right).
\]
Order the primes and always retain the infinity coordinate.
A finite-stage basis of \(I(S)\) consists exactly of the indicators
of nonconstant patterns. On refinement each old indicator becomes
the sum of its disjoint child indicators. Choose one child per
old pattern. In that block, the child sum and all unchosen child
indicators form a basis, since the chosen child is their difference.
Nonconstant children of old constant patterns are additional
independent vectors. This supplies a free complement to every
stage inclusion over every \(S\). Hence \(I(\mathbb Z_{(3)})\)
is free and
\[
I(\mathbb Z_{(3)})\otimes_{\mathbb Z_{(3)}}S=I(S).
\]
Increasing distinct prime wedges give a free basis of the exterior
factor, proving the analogous assertion for \(B\). The maps from
\(B(\mathbb Z_{(3)})\) to \(B(\mathbb C)\) and to \(B(O)\) are
injective. They are two specializations, not a map
\(\mathbb C\to K\).

Taking GSB's boundary theorem as an identified input, the idele
\(\alpha=(3,(1)_p)\) has character value \(3^m\) on the count-\(m\)
module. The diagonal rational 3 instead has modulus
\(3\cdot3^{-1}=1\). The integral lattice is stable under
nonnegative powers of \(\alpha\). Multiplication by \(3^m\)
is not invertible on a nonzero \(O\)-free lattice, so this does
not give an integral representation of the entire idele group.

Put \(B=B(O)\), \(t=a=3^m\). Since \(B\) is free, it has
the exact projective resolution
\[
0\to R\otimes_OB\xrightarrow{a-t}R\otimes_OB\to B\to0.
\]
The proof is the polynomial division and leading-coefficient
argument of (I2), componentwise. Applying Hom gives
\[
\operatorname{RHom}_R(B,E_F)
=[\operatorname{Hom}_O(B,E)\xrightarrow{a-F_E}
  \operatorname{Hom}_O(B,E)].
\]
Projectivity of \(B\) makes \(\operatorname{Hom}_O(B,-)\) exact;
therefore
\[
\operatorname{Hom}_R(B,M_k)=0,\qquad
\operatorname{Ext}^1_R(B,M_k)
=\operatorname{Hom}_O(B,\operatorname{coker}L_{m,k}). \tag{I22}
\]
For infinite basis this is a product, not a tensor direct sum.
No interchange of arbitrary Hom and scalar extension is asserted.

Exact Hom carries the connecting map to its pointwise formula.
For \(j=1\), choose \(A\ne D\) in \(\mathcal A\), a prime \(p\),
and the point \(x_\infty=A,x_p=D,x_q=A\) for \(q\ne p\).
Let \(\ell:B(O)\to O\) extract the \(\vartheta_p\)-coefficient
and evaluate at this point. The cylinder
\(f=\mathbf1_{\{x_\infty=A,x_p=D\}}\) vanishes at every endpoint,
and \(\ell(f\otimes\vartheta_p)=1\).
For \(m\ge2\), the class \(\ell\bmod9\) is in the degree-zero
kernel with \(Q\) coefficients because \(3^mQ=0\). Its image is
\[
b\longmapsto[3^{m-1}z\,\ell(b)],\qquad
\lambda_m\delta_m(\ell)(f\otimes\vartheta_p)=1/3\bmod O. \tag{I23}
\]
For \(m=1\), every connecting class vanishes; the domain is
\(\operatorname{Hom}_O(B,3O/9)\), not all of
\(\operatorname{Hom}_O(B,Q)\).
The first count permitting nonzero image is \(m=2\), first present
at \(r=3\), with \(A=\{1,2\}\), \(D=\{1,3\}\). Each prime gives
a witness.

This proves a coefficient extension on a specified boundary-character
lattice. It does not construct Frobenius on the Schwartz source,
integral Schwartz exactness, a full-idele equivariant collision
receiver, or Weil positivity.

## 8. Formal support operations and stated inputs

The earlier FL/CFF geometric input is
\[
R\Gamma(Y,\mathcal U(E))=E[0],\qquad
R\Gamma_X(Y,\mathcal U(E))=P_S\otimes_OE.
\]
Here \(P_S^0=O\), \(P_S^i=C^{i-1}(S,O)\) for \(i\ge1\);
its terms are finite free and its differentials are
\(-\Delta,-d\). These geometric quasi-isomorphisms are not
independently reproved by this note.
Finite freeness makes tensoring (I1)'s comparison complexes
termwise exact. The total differential on bidegree \((i,j)\) is
\[
d_P\otimes1+(-1)^i1\otimes d_{\mathcal K};
\]
the mixed terms in its square cancel.

For the two-element lattice,
\(P_S=[O\xrightarrow{-1}O]\) has contraction \(-1\) from
degree 1 to degree 0. On the total tensor complex, \(h\otimes1\)
contracts it: the cross terms involving \(d_{\mathcal K}\)
have opposite signs because \(h\) lowers the first degree.
Thus the relative complex is contractible while (I1) remains
on every stalk and in the ordinary coefficient receiver.
No relative nonvanishing is inferred solely from (I23).

For
\[
G_L(E)=\{(v,1_L):v\in E\}\cup\{(0,\lambda):\lambda\in L\},
\]
addition is \((v,\lambda)+(w,\mu)=(v+w,\lambda\vee\mu)\).
Every additive \(f:E\to E'\) defines
\(G_L(f)(v,\lambda)=(f(v),\lambda)\).
Substitution proves well-definedness, addition preservation,
and composition. All zero labels are fixed. If \(f(v)=0\),
the image of \((v,1_L)\) is \(e=(0,1_L)\), not
\(\tau=(0,0_L)\). This does not create an ordering on the
torsion-valued detector.

## 9. Verification outcome

The independent derivation confirms all-\(m\), all-\(k\)
invariant factors (I6), Ext sign (I2–3), connecting map (I10–11),
perfect transpose linking pairing (I7), detector (I8, I14),
unique chain lift (I18–19), exact obstruction (I20), zero
cotangent image (I21), and the all-prime Hom family (I22–23).
No algebraic error was found in BCE5–27.

BCE1–4's coefficient construction is verified here; BCE2's adelic
injection and FL's geometric receiver remain named external inputs.
This note is not a second proof of those geometric theorems.

Two interpretation boundaries must remain explicit: the chain
lift does not restore coefficient Frobenius equivariance, and the
integral lattice stable under nonnegative powers of one idele is
not the full invertible idele representation. BCE currently
formulates both distinctions correctly. No positivity statement
for the original zeta pairing follows from these calculations.

## 10. Further derivation: completion and transported local filtration

This section independently checks the new receiving calculation from
BCE29–41, using the same original \(C,\phi,d=3+\epsilon\).
It addresses every \(m\ge1\) and \(c\in O\). The assertions here
concern the displayed local filtration on this one prism; they
do not identify it with derived global absolute prismatic cohomology.

Write
\[
R=\ker\phi,\qquad
\eta_m=\begin{cases}1,&3\nmid m,\\0,&3\mid m,\end{cases}
\]
and, when \(c\ne0\), put \(s_c=2+v_3(c)\),
\(h_m=\max(0,m-s_c)\). When \(c=0\), set \(h_m=0\).

Since \(d(3-\epsilon)=9\) and \(C\) is \(O\)-free, multiplication
by \(d\) is injective. Its exact \(m\)-th power is
\[
d^m=3^m+m3^{m-1}\epsilon.
\]
For \(x=x_0+x_\epsilon\epsilon+x_TT+x_zz\), retain
\[
\phi(x)=x_0+9cx_Tz,\qquad
d^{-m}\phi(x)=
3^{-m}x_0-m3^{-m-1}x_0\epsilon+3^{2-m}cx_Tz. \tag{I24}
\]
This equality is in \(C[1/3]\); it can be verified by multiplying
by \(d^m\). Its integrality conditions are
\(x_0\in3^mO\), \(mx_0\in3^{m+1}O\), and
\(9cx_T\in3^mO\). Therefore
\[
N_mC=\phi^{-1}(d^mC)
=3^{m+\eta_m}O1\oplus O\epsilon
 \oplus3^{h_m}OT\oplus Oz. \tag{I25}
\]
In particular \(R\subset N_mC\) for every \(m\).
Every \(N_mC\) is an ideal, being the preimage of the ideal
\(d^mC\) under the ring homomorphism \(\phi\).
The ideals are decreasing, and
\(N_iC\,N_jC\subset N_{i+j}C\).
These are ideal and multiplication claims for the original ring,
not merely statements about its coordinate modules.

The displayed formula for \(\phi(x)\), and torsionfreeness of \(O\),
give
\[
R=
\begin{cases}
O\epsilon\oplus Oz,&c\ne0,\\
M,&c=0.
\end{cases} \tag{I26}
\]
They are ideals. For \(c\ne0\), the products with \(\epsilon,T\)
are \(\epsilon\epsilon=0,\ T\epsilon=z,\ \epsilon z=Tz=0\);
for \(c=0\), \(R=M\) was already an ideal.
The quotient map \(\pi:C\to\bar C=C/R\) is consequently a ring map,
with
\[
\bar C=
\begin{cases}
O[\bar T]/(\bar T^2),&c\ne0,\\
O,&c=0.
\end{cases} \tag{I27}
\]
The relation \(\bar T^2=0\) is the actual image of
\(T^2=6\epsilon\), since \(\epsilon\in R\).
No coefficient from the original relation was suppressed.

Because \(R\subset N_mC\), the quotient \(C/N_mC\) is canonically
\(\bar C/\bar N_m\), where the transported domain is
\[
\bar N_m=\pi(N_mC)=
\begin{cases}
3^{m+\eta_m}O1\oplus3^{h_m}O\bar T,&c\ne0,\\
3^{m+\eta_m}O,&c=0.
\end{cases} \tag{I28}
\]
These are ideals of \(\bar C\), since they are images of the ideals
\(N_mC\). Explicitly, multiplication by \(\bar T\) takes the constant
summand into the \(T\) summand because \(h_m\le m+\eta_m\);
\(\bar T^2=0\).

For \(c\ne0\), \(h_m\le m+\eta_m\) and \(h_m\to\infty\).
Thus
\[
3^{m+\eta_m}\bar C\subset\bar N_m\subset3^{h_m}\bar C.
\]
For any prescribed \(n\), choosing \(m\ge n+s_c\) gives
\(\bar N_m\subset3^n\bar C\). Conversely, for every \(m\),
\(3^{m+\eta_m}\bar C\subset\bar N_m\). These prove cofinality
of the two ideal filtrations. For \(c=0\), it follows directly
from \(\bar N_m=3^{m+\eta_m}O\) and \(m+\eta_m\to\infty\).
The \(O\)-module \(\bar C\) is finite free and complete, so
\[
\varprojlim_m C/N_mC
=\varprojlim_m\bar C/\bar N_m
\cong\bar C. \tag{I29}
\]
The isomorphism is the canonical one: its constant and, when
present, \(T\)-coordinates are the unique compatible 3-adic
limits of the residue coordinates. It preserves multiplication
because every finite-stage map does. The kernel of the natural
map \(C\to\varprojlim C/N_mC\) is exactly \(R\).
This is the separated completion for this local filtration.

## 11. Descent of Frobenius, multiplication, and divided maps

Since \(\phi(R)=0\), the ring endomorphism descends to
\(\bar\phi:\bar C\to\bar C\), with
\[
\bar\phi|_O=1,\qquad \bar\phi(\bar T)=0
\quad(c\ne0),\qquad \bar d=\pi(d)=3.
\]
In either case \(\bar C\) is 3-torsionfree, so division by
\(3^m\), when defined, is unique.

For \(x\in N_mC\), let \(\phi_m(x)\) denote the unique
\(y\in C\) with \(d^m y=\phi(x)\).
If \(r\in R\), \(\phi_m(r)=0\). The divided map therefore
descends to \(\bar N_m=N_mC/R\).
Applying \(\pi\) to \(d^m\phi_m(x)=\phi(x)\) proves
\[
\pi\phi_m(x)=\bar\phi(\pi x)/3^m. \tag{I30}
\]
This also proves that the expression on the right is integral
on the transported domain, with no choice of lift.

The family of divided maps respects multiplication in its
correct degrees:
\[
\phi_{i+j}(xy)=\phi_i(x)\phi_j(y),
\quad x\in N_iC,\ y\in N_jC. \tag{I31}
\]
Indeed multiplying the right side by \(d^{i+j}\) gives
\(\phi(x)\phi(y)=\phi(xy)\); injectivity of \(d^{i+j}\)
proves the identity. The same proof after applying \(\pi\)
gives the corresponding formula on \(\bar N_\bullet\).
For a fixed \(m\), \(\phi_m(ax)=\phi(a)\phi_m(x)\).
These are semilinear identities; the fixed-point
differential \(\phi_m-\iota\) is an \(O\)-linear map and
need not be \(C\)-linear or \(\bar C\)-linear.

Define
\[
J_m(C)=[N_mC\xrightarrow{\phi_m-\iota}C],\qquad
\bar J_m=[\bar N_m\xrightarrow{\bar\phi/3^m-\iota}\bar C].
\]
Equation (I30) gives a surjective chain map \(J_m(C)\to\bar J_m\).
Its kernel in both degrees is \(R\); on \(R\) its differential
is \(-I\), because \(\phi_m(R)=0\). Therefore
\[
0\to[R\xrightarrow{-I}R]\to J_m(C)\to\bar J_m\to0 \tag{I32}
\]
is a short exact sequence of \(O\)-module complexes.
The kernel is contractible, with homotopy \(-I\).
It follows that the quotient map is a quasi-isomorphism.

There is also an explicit chain-homotopy equivalence.
For \(c\ne0\), choose the degree-one section \(s^1:\bar C\to C\)
which lifts \(1,\bar T\) to \(1,T\). For
\(\bar x=3^{m+\eta_m}a+3^{h_m}t\bar T\), define
\[
s^0(\bar x)=3^{m+\eta_m}a+3^{h_m}tT
-m3^{\eta_m-1}a\epsilon
+3^{2+h_m-m}ctz. \tag{I33}
\]
Both extra coefficients are integral: when \(\eta_m=0\),
\(3\mid m\); and the definition of \(h_m\) gives
\(2+h_m-m+v_3(c)\ge0\).
Their summands lie in \(R\subset N_mC\).

The original differential on the first two terms of (I33) has
the extra \(R\)-part
\(-m3^{\eta_m-1}a\epsilon+3^{2+h_m-m}ctz\).
Adding that part to the domain cancels it under the differential
\(-I\) on \(R\). Hence
\[
d_Js^0=s^1d_{\bar J},\qquad \pi s=I.
\]
For \(c=0\), omit the \(T\) terms in \(\bar C,s^1,s^0\);
the same formula with its \(\epsilon\)-correction works.

Let \(P_R(y)=y-s^1\pi(y)\). This is a projection \(C\to R\).
The degree-minus-one map
\(H=-P_R:C\to R\subset N_mC\) satisfies
\[
d_JH+Hd_J=I-s\pi.
\]
In degree one this is \(d_J(-P_R)=P_R=I-s^1\pi\).
In degree zero, writing \(x=s^0_{\rm initial}\pi(x)+r_0\)
shows that the \(R\)-part of \(d_Jx\) is
\(r(\pi x)-r_0\), where \(r\) is the correction in (I33);
its negative is exactly \(x-s^0\pi x\). This proves the
second identity. Thus completion with the transported domain
preserves the local complex up to explicit chain homotopy.

## 12. Reconstructing the domain on the completed quotient

Now form the intrinsic preimage filtration on the quotient ring:
\[
\widetilde N_m=\{x\in\bar C:
\bar\phi(x)\in3^m\bar C\}.
\]
Because \(\bar\phi\) keeps only the constant coefficient,
\[
\widetilde N_m=
\begin{cases}
3^mO1\oplus O\bar T,&c\ne0,\\
3^mO,&c=0.
\end{cases} \tag{I34}
\]
Thus \(\bar N_m\subset\widetilde N_m\).
The inclusion is **not always strict**. Its quotient is
\[
Q_m=\widetilde N_m/\bar N_m=
\begin{cases}
(O/3^{\eta_m})[3^m]\oplus(O/3^{h_m})[\bar T],&c\ne0,\\
(O/3^{\eta_m})[3^m],&c=0.
\end{cases} \tag{I35}
\]
For \(c\ne0\), equality of the domains occurs exactly when
\(3\mid m\) and \(m\le2+v_3(c)\).
For instance \(m=3,c=3\) gives equality.
For \(c=0\), equality occurs exactly when \(3\mid m\).
In every other case the inclusion is strict.

The intrinsic fixed-point complex is
\[
\widetilde J_m=
[\widetilde N_m\xrightarrow{\bar\phi/3^m-\iota}\bar C].
\]
On \(3^ma+t\bar T\), its differential is
\[
(1-3^m)a-t\bar T. \tag{I36}
\]
For \(m\ge1\), \(1-3^m\) is an \(O\)-unit, so this is an
\(O\)-linear isomorphism. Its inverse is
\[
y_0+y_T\bar T\longmapsto
3^m(1-3^m)^{-1}y_0-y_T\bar T;
\]
omit \(T\) if \(c=0\). Hence \(\widetilde J_m\) is contractible.
The restriction \(m\ge1\) is essential: at \(m=0\) the
constant differential vanishes.

The transported differential is still
\[
3^{m+\eta_m}a+3^{h_m}t\bar T
\longmapsto3^{\eta_m}(1-3^m)a-3^{h_m}t\bar T. \tag{I37}
\]
It is injective, and its cokernel is
\((O/3^{\eta_m})[1]\oplus(O/3^{h_m})[\bar T]\), with the
\(T\) factor omitted for \(c=0\).
This agrees with the cohomology of the original \(J_m(C)\)
through the concrete equivalence (I32–33).

There is a short exact sequence
\[
0\to\bar J_m\to\widetilde J_m
\to[Q_m\to0]\to0. \tag{I38}
\]
The degree-one quotient is zero because both complexes have
the same degree-one module \(\bar C\); their differentials
agree on \(\bar N_m\). Since both degree-zero kernels vanish
and \(\widetilde J_m\) is acyclic, its connecting map is an
isomorphism
\[
Q_m\xrightarrow{\sim}H^1(\bar J_m).
\]
Lifting the two displayed generators in (I35) to
\(\widetilde N_m\) and using (I36) fixes its signs:
\[
[3^m]\longmapsto[1-3^m],\qquad
[\bar T]\longmapsto[-\bar T]. \tag{I39}
\]
The first is a unit multiple of the constant generator; the
second has sign minus one. These formulas include the
cases in which either or both groups are zero.

## 13. Necessary category and interpretation restrictions

All complexes in (I32–39) are complexes of \(O\)-modules.
The underlying quotient \(C\to\bar C\) is a ring map, the
filtration terms are ideals, and their divided maps have
the graded multiplicative property (I31). It does not follow
that the fixed-point differential is \(\bar C\)-linear.

For a concrete check, take \(c\) a unit and \(m=3\). Then
\(\eta_m=0,h_m=1\), and (I37) has image
\[
O1\oplus3O\bar T\subset\bar C.
\]
It contains 1 but not \(\bar T\), so is not a \(\bar C\)-ideal.
Therefore its cokernel has no quotient \(\bar C\)-module
structure through that image. Neither the quasi-isomorphism
nor the connecting isomorphism above is being asserted in
that nonexistent module category.

The exact conclusion is that the local filtered completion
retains the original local fixed-point complex when the
filtration is transported. Rebuilding the intrinsic preimage
filtration on the quotient changes its domain by the precisely
computed object \(Q_m\), and yields an acyclic complex for
\(m\ge1\). The connecting isomorphism (I39) measures everything
lost by that particular change. When \(Q_m=0\), nothing is
lost and both complexes were already acyclic.

This is not a statement about a global absolute Nygaard
completion, derived prismatic descent, a new Weil form, or
the sign of the original zeta pairing. It is the complete
local comparison on the original coefficients with every
nonzero and zero image specified.


