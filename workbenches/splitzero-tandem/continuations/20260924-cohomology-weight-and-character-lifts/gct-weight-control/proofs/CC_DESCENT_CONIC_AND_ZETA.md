# The descended CC conic, its integral fibre, and its full zeta function

Independent mathematical derivation, 24 September 2026. Proof locators CD0–CD12.

The concrete results are an explicit descent isomorphism over \(\mathbf Z[1/2,i]\), an integral conic retaining its nonreduced fibre at \(2\), and the complete arithmetic Euler product
\[
Z(\mathcal C,s)=\zeta(s)\zeta(s-1),\qquad \Re s>2.
\tag{CD0.1}
\]
The two functions on the right are the original Riemann zeta function at the displayed arguments. The translated factor has a geometric origin in the degree-two cohomology of the descended conic. The integral model at \(2\) is examined separately from finite étale descent.

## CD0. Input stage, source use, and operation check

The support remains the user's \(\tau\langle Z_1;\text{no }Z_2\rangle\). The coefficient ring \(\mathbf Z\), all its primes and its original zeta function are used only after the complete arithmetic reconstruction. None of the projective coordinates below is a coordinate on that supporting datum. No addition, norm, metric or vector is assigned to \(\tau\). The coefficient extension adjoining \(i\) evaluates the supplied signed CC charts; it is not an alternative arithmetic offered as an RH counterexample. Separate branch return measures are not pooled.

The current READ_FIRST_USER_CONSTRUCTION.md and USER_ARGUMENT_RECONSTRUCTION.md, including the correction-precedence table, were read before the construction, together with PC01–PC03 of PREREQUISITE_AND_OBSTRUCTION_CHECKS.md. The operations checked here are the explicit CC chart evaluation, finite étale descent of its projective action, an integral model, its finite-field point counts, and its coefficient cohomology. Their prerequisites are proved below or cited at their exact previously proved source locations. None requires an exact eigenfunction lift in the analytic source.

The existing source-use coverage in [CC_GEOMETRIC_TATE_INDEPENDENT.md](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/gct-weight-control/proofs/CC_GEOMETRIC_TATE_INDEPENDENT.md), CGT0–CGT12, was read. That witness's hash at reading was 9C296F9F590D842B1C593F530C12CBCC6E6FE302F354C6170CF18CB050FFC960. The original author source read for the present comparison was Alain Connes and Caterina Consani, [The Absolute Twistor Line and the Geometry of the compactified Spec Z](https://arxiv.org/html/2609.00299v1), CC.tex, lines 484–604 and 773–848, containing the three-point support, ordered charts, signed Bombelli overlap, and full involution. The source hash is 57A10DCEF5CD758E6B2F1C54B1C0A11B0FB093638F74FB1BE515EC3BC7080BA4.

The exact starting ring realization from CGT1–CGT2 is
\[
X_R=\mathbf P^1_{R[i]},\quad i^2=-1,\qquad
\alpha([X:Y],i)=([-Y:X],-i).
\tag{CD0.2}
\]
This is the explicit evaluation of the original restrictions \(J_+\mapsto J\), \(J_-\mapsto-J\), with global coefficient \(J=i\); it does not erase either chart. On the overlap, \(\alpha^*T=-T^{-1}\), \(\alpha^*i=-i\). The statement is semilinear over \(R[i]\) and linear over \(R\).

For cohomology only, CGT4, CGT8 and CGT9 supply the previously read Kummer, nilpotent-invariance and proper-base-change calculations. Their underlying primary-source locators are the Stacks Project [03RQ](https://stacks.math.columbia.edu/tag/03RQ), [03SI](https://stacks.math.columbia.edu/tag/03SI), and [095T](https://stacks.math.columbia.edu/tag/095T), at the author-source commit recorded in CGT0. Those Stacks files were not newly reread for this note; the exact receiver calculations from CGT are the input. The descent and point counts in CD1–CD9 are derived here.

## CD1. The actual finite étale cover and its cocycle

Put
\[
R=\mathbf Z[1/2],\quad A=R[i]=R[t]/(t^2+1),\quad
c(i)=-i,\quad c|_R=1.
\tag{CD1.1}
\]
As an \(R\)-module, \(A\) is free on \(1,i\). Since \(2i\) is a unit, the derivative of its defining polynomial is a unit. Equivalently, the finite free presentation has
\(\Omega_{A/R}=A\,di/(2i\,di)=0\); the elementary monogenic étale criterion proves that \(A/R\) is finite étale. It is faithfully flat because its free rank is two.

The complete split overlap is
\[
A\otimes_R A\longrightarrow A\times A,\qquad
a\otimes b\longmapsto(ab,a\,c(b)).
\tag{CD1.2}
\]
It is an isomorphism: as a polynomial algebra over the left copy of \(A\), its two factors are \(t-i\) and \(t+i\), whose difference \(2i\) is a unit. Explicit idempotents are
\[
e_1=\frac{1-i\otimes i}{2},\qquad
e_2=\frac{1+i\otimes i}{2},
\tag{CD1.3}
\]
with images \((1,0)\) and \((0,1)\). This proves directly that the semilinear involution supplies the two required components of the descent datum over the actual fibre product.

The projective transformation is represented by
\[
M=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
M\,c(M)=M^2=-I.
\tag{CD1.4}
\]
Thus its square is the identity on projective space. The matrix square is retained: it is \(-I\) on the rank-two vector presentation, not \(I\). The projective cocycle condition is exactly the one required for (CD0.2).

## CD2. The explicit descended conic and its inverse charts

Define the smooth projective \(R\)-scheme
\[
\mathcal C_R=\operatorname{Proj}R[x,y,z]/(x^2+y^2+z^2).
\tag{CD2.1}
\]
Smoothness follows from the Jacobian criterion: on a geometric fibre, simultaneous vanishing of \(2x,2y,2z\) would force all projective coordinates to be zero, because \(2\) is invertible.

Over \(A\), define
\[
\phi:\mathbf P^1_A\longrightarrow(\mathcal C_R)_A,\qquad
[X:Y]\longmapsto
[X^2-Y^2:\ i(X^2+Y^2):\ 2XY].
\tag{CD2.2}
\]
Its coordinates satisfy the full identity
\[
(X^2-Y^2)^2+\bigl(i(X^2+Y^2)\bigr)^2+(2XY)^2=0.
\tag{CD2.3}
\]
There are no basepoints: on \(D(X)\), the combination \(x-iy\) pulls back to \(2X^2\), a generator of the corresponding line-bundle fibre; on \(D(Y)\), the combination \(-x-iy\) pulls back to \(2Y^2\). These two opens cover \(\mathbf P^1_A\).

On the conic set
\[
a=x-iy,\qquad b=z,\qquad d=-x-iy.
\]
The defining equation gives
\[
ad=b^2.
\tag{CD2.4}
\]
The opens \(D(a)\) and \(D(d)\) cover the conic. Indeed a prime containing both contains \(x,y\), since \(2i\) is a unit; the equation then forces it to contain \(z\), which is not a projective point. Define inverse maps on those opens by
\[
\psi|_{D(a)}=[a:b]=[x-iy:z],\qquad
\psi|_{D(d)}=[b:d]=[z:-x-iy].
\tag{CD2.5}
\]
On their intersection (CD2.4) makes the two projective pairs equal. The displayed nonvanishing first or second coordinate makes each map well-defined.

Their composites with \(\phi\) equal \([X:Y]\): the two pairs become
\([2X^2:2XY]\) on \(D(X)\) and \([2XY:2Y^2]\) on \(D(Y)\). For the other composite on \(D(a)\), the three coordinate identities are
\[
a^2-b^2=2ax,\quad
i(a^2+b^2)=2ay,\quad
2ab=2az.
\tag{CD2.6}
\]
The common factor \(2a\) is invertible in the local trivialization on that open. On \(D(d)\), substitution using \(b^2=ad\) gives
\(b^2-d^2=d(a-d)=2dx\),
\(i(b^2+d^2)=id(a+d)=2dy\), and \(2bd=2dz\).
Thus the common factor on this second chart is \(+2d\), and the full formulas are
\[
b^2-d^2=2dx,\quad i(b^2+d^2)=2dy,\quad2bd=2dz.
\tag{CD2.7}
\]
They prove the other composite as well. Consequently \(\phi\) is an isomorphism, with the complete inverse (CD2.5).

## CD3. Verification of descent, including the homogeneous sign

Apply the full semilinear action to the three quadratic sections in (CD2.2). Since it sends \(X\mapsto-Y\), \(Y\mapsto X\), \(i\mapsto-i\), one obtains
\[
\alpha^*(X^2-Y^2)=-(X^2-Y^2),
\]
\[
\alpha^*\bigl(i(X^2+Y^2)\bigr)=-i(X^2+Y^2),\qquad
\alpha^*(2XY)=-2XY.
\tag{CD3.1}
\]
The same sign occurs in all three coordinates. It acts trivially on their projective class. Accordingly \(\phi\) intertwines \(\alpha\) with coefficient conjugation on \((\mathcal C_R)_A\).

There is also an explicit graded-ring descent. The second Veronese ring of \(A[X,Y]\) is
\[
A[a,b,d]/(ad-b^2),\qquad a=X^2,\ b=XY,\ d=Y^2,
\]
where each of \(a,b,d\) has Veronese degree one. The invertible linear change
\[
x=a-d,\quad y=i(a+d),\quad z=2b
\tag{CD3.2}
\]
has inverse \(a=(x-iy)/2\), \(d=(-x-iy)/2\), \(b=z/2\), and sends
\[
x^2+y^2+z^2=-4(ad-b^2).
\tag{CD3.3}
\]
On Veronese degree \(n\), replace the linearized action by
\(\beta=(-1)^n\alpha^*\). This is a graded-ring automorphism, because degrees add, and its square is one. Equation (CD3.1) says that \(\beta\) fixes \(x,y,z\) and conjugates only their \(A\)-coefficients. Every element of the resulting ring has a unique expression \(f+i g\) with \(f,g\) in \(R[x,y,z]/(x^2+y^2+z^2)\). It is fixed exactly when \(2ig=0\), hence exactly when \(g=0\). Thus its invariant graded ring is precisely the ring in (CD2.1).

The factor \((-1)^n\) does not change the induced projective action. This calculation proves effective descent by the written rings and inverse charts; it does not merely identify point sets over a field. It also records why a sign in the vector presentation is consistent with an involution on the projective object.

After base change to \(\mathbf Q\), the descended conic has no rational point: a rational solution of \(x^2+y^2+z^2=0\), viewed in \(\mathbf R\), has \(x=y=z=0\). Hence it is not \(\mathbf P^1_{\mathbf Q}\), which has rational points. Nevertheless its base change to \(\mathbf Q(i)\) is exactly (CD2.2). This is the nontrivial form dictated by the supplied semilinear action, with no new arithmetic base substituted for the recovered \(\mathbf Z\).

The same sign has a vector-level explanation. Multiplying \(M\) in (CD1.4) by \(b\in\mathbf Q(i)^\times\) changes its cocycle square to \(-b\,c(b)I\). It could be \(I\) only if \(b\,c(b)=-1\). Writing \(b=u+iv\) with rational \(u,v\) gives \(b\,c(b)=u^2+v^2>0\), so this is impossible. This concerns the specified rank-two lift of this projective cocycle; projective descent itself has already been constructed.

## CD4. The integral model and its retained fibre at \(2\)

Take the explicit integral model
\[
\mathcal C=\operatorname{Proj}\mathbf Z[x,y,z]/(x^2+y^2+z^2),
\qquad f:\mathcal C\to\operatorname{Spec}\mathbf Z.
\tag{CD4.1}
\]
It restricts to the descended conic over \(R\). It is projective. Its homogeneous coordinate ring is free over \(\mathbf Z\), with basis
\[
x^a y^b z^c,\qquad a,b\ge0,\ c\in\{0,1\},
\tag{CD4.2}
\]
because division by the monic polynomial \(z^2+x^2+y^2\) leaves a unique remainder of degree less than two in \(z\). Localization preserves \(\mathbf Z\)-torsion-freeness, as does taking the degree-zero submodule of each Proj chart. A torsion-free module over the principal ideal domain \(\mathbf Z\) is flat: every finitely generated submodule is free, and the module is their filtered union; tensor product commutes with that union and filtered unions preserve exactness. Thus every affine chart is flat, proving that \(f\) is flat.

Over \(\mathbf F_2\), the defining polynomial is
\[
x^2+y^2+z^2=(x+y+z)^2.
\tag{CD4.3}
\]
Let \(l=x+y+z\). Then the actual fibre and its reduction are
\[
\mathcal C_{\mathbf F_2}=V(l^2),\qquad
L=V(l)\simeq\mathbf P^1_{\mathbf F_2}.
\tag{CD4.4}
\]
An explicit isomorphism from \(\mathbf P^1\) onto \(L\) is
\([a:b]\mapsto[a:b:a+b]\), with inverse \([x:y:z]\mapsto[x:y]\).
The nilpotent ideal is \((l)/(l^2)\), is square-zero, and is not zero. Globally it is \(\mathcal O_L(-1)\); multiplication by the degree-one equation \(l\) identifies it with the restriction of that twist. Therefore the full sheaf sequence is
\[
0\longrightarrow\mathcal O_L(-1)
\longrightarrow\mathcal O_{\mathcal C_{\mathbf F_2}}
\longrightarrow\mathcal O_L\longrightarrow0.
\tag{CD4.5}
\]
This retains the nonreduced structure, rather than replacing the fibre by its reduction. The morphism is smooth away from \(2\), by CD2, and is not smooth at \(2\), since that fibre is not geometrically reduced.

## CD5. Why the ramified integral quotient is a separate problem

Write \(A_{\mathbf Z}=\mathbf Z[i]\). The ring map
\[
A_{\mathbf Z}\otimes_{\mathbf Z}A_{\mathbf Z}
\longrightarrow A_{\mathbf Z}\times A_{\mathbf Z},
\quad a\otimes b\longmapsto(ab,a\,c(b))
\tag{CD5.1}
\]
has matrix \(\begin{pmatrix}1&i\\1&-i\end{pmatrix}\) over the left coefficient ring, of determinant \(-2i\). It is injective, but its image consists exactly of pairs \((u,v)\) with \(u-v\in2A_{\mathbf Z}\). Indeed the preimage coefficients must be \(b=(u-v)/(2i)\), \(a=u-ib\); the displayed condition is sufficient and necessary. Its cokernel is \(A_{\mathbf Z}/2A_{\mathbf Z}\), via the difference of the two entries. Thus it is not an isomorphism at \(2\).

The finite flat cover at \(2\) is therefore not the \(C_2\)-torsor used in CD1. A pair consisting of the identity and a semilinear involution does not by itself specify an isomorphism over this whole ramified fibre product. Finite étale descent cannot be applied there by using the two graphs as though they were a disjoint covering.

The actual quadratic formula (CD2.2) also fails to extend to a morphism \(\mathbf P^1_{\mathbf Z[i]}\to\mathcal C_{\mathbf Z[i]}\). At the prime \(\pi=1+i\), it reduces to
\[
[(X+Y)^2:(X+Y)^2:0],
\tag{CD5.2}
\]
which has the basepoint \([1:1]\). This failure is not removable by another presentation of the same generic map. Over the discrete valuation ring \(D=\mathbf Z[i]_{(1+i)}\), the two sections
\[
P=[1:1],\qquad Q=[1:i]
\]
have the same closed specialization. Their generic images under (CD2.2), retaining the original factors before choosing integral representatives, are
\[
\phi(P)=[0:2i:2]=[0:i:1],\qquad
\phi(Q)=[2:0:2i]=[1:0:i].
\tag{CD5.3}
\]
The last triples are valid \(D\)-points of the conic. They specialize to the distinct points \([0:1:1]\) and \([1:0:1]\). If a morphism extending \(\phi\) existed, its compositions with \(P,Q\) would agree with these generic images, and separatedness of the projective target would force these displayed integral extensions. Their values at the common source specialization would have to agree, a contradiction.

There is an additional direct model distinction: base changing (CD4.1) to \(D\) gives a doubled-line closed fibre, while \(\mathbf P^1_D\) has a reduced closed fibre. Consequently this integral \(\mathcal C\) is not a descent of the full scheme \(\mathbf P^1_{\mathbf Z[i]}\) through an isomorphism extending CD2. It is the specified integral model of its already constructed generic descent.

These are precise facts about these integral maps. They neither discard the CC signed charts nor identify \(\mathcal C\) with their ramified coarse quotient. Constructing that coarse quotient or a resolving modification is a different operation. The model (CD4.1), its nilpotents and its zeta factors are all retained below.

## CD6. All finite-field points, without assuming an initial point

Let \(q=p^r\) be any finite prime power. First suppose \(p\ne2\), and let \(\chi:\mathbf F_q\to\{0,\pm1\}\) be its quadratic character, with \(\chi(0)=0\). The equation
\[
v^2=y^2+1
\]
is equivalent to \((v-y)(v+y)=1\). Its solutions correspond bijectively to \(u\in\mathbf F_q^\times\), through
\[
v-y=u,\qquad v+y=u^{-1}.
\tag{CD6.1}
\]
Division by two gives the inverse pair \(v=(u+u^{-1})/2\), \(y=(u^{-1}-u)/2\). Counting the same solutions by \(y\) gives
\[
q+\sum_{y\in\mathbf F_q}\chi(y^2+1)=q-1,
\qquad \sum_y\chi(y^2+1)=-1.
\tag{CD6.2}
\]

In the affine chart \(z=1\) of the conic, the equation is \(x^2+y^2=-1\). Its number of points is exactly
\[
\sum_y\left(1+\chi(-1-y^2)\right)=q-\chi(-1).
\tag{CD6.3}
\]
At infinity, \(z=0\) forces \(y\ne0\), and \((x/y)^2=-1\) has \(1+\chi(-1)\) solutions. Thus
\[
\#\mathcal C(\mathbf F_q)
=\bigl(q-\chi(-1)\bigr)+\bigl(1+\chi(-1)\bigr)=q+1.
\tag{CD6.4}
\]
Both chart contributions have been calculated. No rational point or splitting of the conic was assumed to obtain them.

For \(p=2\), a map to a field annihilates every nilpotent. Conversely every field point of \(L\) is a point of \(V(l^2)\). These mutually inverse operations identify the point sets while preserving the different schemes from CD4. Hence
\[
\#\mathcal C(\mathbf F_{2^r})
=\#L(\mathbf F_{2^r})=2^r+1.
\tag{CD6.5}
\]
We have proved, for every prime and every positive repetition,
\[
\boxed{\#\mathcal C(\mathbf F_{p^r})=1+p^r.}
\tag{CD6.6}
\]
The coefficient two defining the doubled fibre has not been used as a second copy of each point. A nilpotent thickening does not create extra field-valued points.

## CD7. The geometric Tate line, retaining the degree-two comparison

Fix \(p\), a coefficient prime \(\ell\ne p\), and \(E=\mathbf Q_\ell\). At an odd characteristic, CD2 after geometric base change identifies \(\mathcal C_{\overline{\mathbf F}_p}\) with \(\mathbf P^1\). At characteristic two, the closed immersion \(L_{\overline{\mathbf F}_2}\hookrightarrow\mathcal C_{\overline{\mathbf F}_2}\) induces the étale-topos equivalence of CGT3–CGT4. These are the specified maps used to obtain
\[
H^0(\mathcal C_{\bar k},E)=E,\quad H^1=0,\quad
H^2(\mathcal C_{\bar k},E)=E(-1),\quad H^j=0\ (j>2).
\tag{CD7.1}
\]

There is a factor in this comparison that must be kept. The conic hyperplane line bundle satisfies
\[
\phi^*\mathcal O_{\mathcal C_R}(1)=\mathcal O_{\mathbf P^1_A}(2).
\tag{CD7.2}
\]
The reason is the homogeneous degree two of the basepoint-free sections in (CD2.2): on each trivialization their ratios are exactly the transition maps for the pullback of \(\mathcal O(1)\). Thus the Kummer first Chern class, in the twisted cohomology group, obeys
\[
\phi^*c_1(\mathcal O_{\mathcal C_R}(1))
=2c_1(\mathcal O_{\mathbf P^1_A}(1)).
\tag{CD7.3}
\]
On the reduced special line at \(2\), by contrast,
\[
\mathcal O_{\mathcal C_{\mathbf F_2}}(1)|_L=\mathcal O_L(1).
\tag{CD7.4}
\]
The class at that fibre is the single line hyperplane class. Both maps are retained.

The global hyperplane class is Galois-fixed in \(H^2(E(1))\), and is nonzero: its geometric comparison coefficient is two at odd and characteristic-zero fibres, and one at the fibre at \(2\). These are nonzero invertible scalars in \(E\). Hence geometric Frobenius has eigenvalue \(p\) on untwisted \(H^2\), because it has eigenvalue \(p^{-1}\) on \(E(1)\). It has eigenvalue one on \(H^0\). Its full repetition trace is consequently
\[
\operatorname{Tr}(F_p^r\mid H^0)
-\operatorname{Tr}(F_p^r\mid H^1)
+\operatorname{Tr}(F_p^r\mid H^2)=1+p^r.
\tag{CD7.5}
\]
This agrees with the independent point count CD6.

One may retain the whole proper pushforward. On \(S_\ell=\operatorname{Spec}\mathbf Z[1/\ell]\), the unit and actual hyperplane class define
\[
E_{S_\ell}\oplus E_{S_\ell}(-1)[-2]
\longrightarrow Rf_*E_{\mathcal C_{S_\ell}}.
\tag{CD7.6}
\]
Proper base change identifies its stalks with the maps just calculated. They are isomorphisms in degrees zero and two, and all other stalk cohomology vanishes. Therefore (CD7.6) is a quasi-isomorphism. This is an actual geometric source of the twist and shift; it is not a chosen weight assigned to an analytic eigenvector.

For completeness, specialize this model over \(\mathbf Z_2\), with \(\ell\ne2\). Write \(h_s=c_1(\mathcal O_L(1))\) on the reduced geometric special line and \(h_\eta=c_1(\mathcal O_{\mathbf P^1}(1))\) after the geometric generic parametrization. The global line bundle and proper specialization give
\[
\operatorname{sp}_0(1)=1,\qquad
\operatorname{sp}_2(h_s)=2h_\eta
\quad\text{in the twisted degree-two groups}.
\tag{CD7.7}
\]
The scalar two follows from (CD7.3)–(CD7.4), not from a choice to renormalize the trace. The generic rational groups are \(E\) and \(E(-1)\), with inertia trivial: their nonzero global hyperplane class fixes the twisted line, and prime-to-two roots of unity are unramified. Thus (CD7.7) is an isomorphism onto inertia invariants with rational coefficients. This model's factor two differs from CGT7's two-entry diagonal map, because those are different integral models with different displayed maps. Their generic descent relation does not equate those special-fibre formulas.

## CD8. Every local factor, including the prime \(2\)

Define the local scheme zeta function by its complete point-count series:
\[
Z(\mathcal C_{\mathbf F_p},T)
=\exp\left(\sum_{r\ge1}\frac{\#\mathcal C(\mathbf F_{p^r})}{r}T^r\right).
\tag{CD8.1}
\]
Using every repetition in (CD6.6),
\[
\begin{aligned}
Z(\mathcal C_{\mathbf F_p},T)
&=\exp\left(\sum_{r\ge1}\frac{T^r}{r}
                 +\sum_{r\ge1}\frac{p^rT^r}{r}\right)\\
&=\frac1{(1-T)(1-pT)}.
\end{aligned}
\tag{CD8.2}
\]
This is a formal power-series identity with constant term one; analytically it follows from the two logarithm series for \(|T|<p^{-1}\). Its cohomological determinant form retains both groups:
\[
Z(\mathcal C_{\mathbf F_p},T)
=\frac{\det(1-TF_p\mid H^1)}
{\det(1-TF_p\mid H^0)\det(1-TF_p\mid H^2)}
=\frac1{(1-T)(1-pT)}.
\tag{CD8.3}
\]

In particular the full local factor at the nonreduced fibre is
\[
Z(\mathcal C_{\mathbf F_2},2^{-s})
=\frac1{(1-2^{-s})(1-2^{1-s})}.
\tag{CD8.4}
\]
This equality is not an assertion that the fibre is reduced; its square-zero sheaf (CD4.5) remains present, and both point counts and the constant étale receiver pass through the specified reduction map.

## CD9. The arithmetic Euler product and its exact comparison to the original zeta

The scheme zeta function of this specified finite-type \(\mathbf Z\)-scheme is the product over its finite-field fibres. For \(\sigma=\Re s>2\),
\[
\sum_p\sum_{r\ge1}
\frac{|p^{-rs}|+|p^{r(1-s)}|}{r}<\infty.
\tag{CD9.1}
\]
Indeed each repetition sum is bounded by a constant, depending on \(\sigma\), times \(p^{-\sigma}+p^{1-\sigma}\), and their sums over primes are bounded by the corresponding convergent sums over all positive integers greater than one. Therefore all rearrangements below are justified by absolute convergence:
\[
\begin{aligned}
Z(\mathcal C,s)
&=\prod_p\frac1{(1-p^{-s})(1-p^{1-s})}\\
&=\exp\left(\sum_p\sum_{r\ge1}
             \frac{p^{-rs}+p^{r(1-s)}}r\right)\\
&=\left(\sum_{a\ge1}a^{-s}\right)
  \left(\sum_{b\ge1}b^{1-s}\right)
=\zeta(s)\zeta(s-1).
\end{aligned}
\tag{CD9.2}
\]
The two unit terms are retained. The products use every prime in the already recovered integer ring. They count two cohomological degrees of one conic; they are not the sum or pooling of two branch return measures.

The open-base descent model alone has
\[
Z(\mathcal C_R,s)
=(1-2^{-s})(1-2^{1-s})\,\zeta(s)\zeta(s-1).
\tag{CD9.3}
\]
Multiplying by the explicitly computed factor (CD8.4) gives exactly (CD9.2). Thus no prime at which descent was not étale has been hidden in an unspecified correction factor.

Equation (CD9.2) supplies its meromorphic continuation as this original product. Its pole residues at \(s=1\) and \(s=2\) are respectively \(\zeta(0)=-1/2\) and \(\zeta(2)\). At the original trivial zeros \(s=-2r\), the other factor is the nonzero \(\zeta(-2r-1)\); at the translated trivial zeros \(s=1-2r\), the other factor is the nonzero \(\zeta(1-2r)\), for every \(r\ge1\). Thus none of those trivial-zero factors has been cancelled by a completion in this Euler product. Its value at zero is \(\zeta(0)\zeta(-1)=1/24\). These evaluations describe the original meromorphic functions, not a completed substitute.

## CD10. The exact connection with the constructed translated analytic divisor

GSL6.5–GSL6.11 construct the actual analytic quotient on the union of the original nontrivial divisor \(\mathscr Z\) and its translate \(\mathscr Z+1\). The high-weight source multiplier there is exactly
\[
\begin{aligned}
G_{\rm high}(s)
&=F_0(s)F_0(s-1)\\
&=\left[\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2)\right]
  \left[\frac{(s-1)(s-2)}8\pi^{-(s-1)/2}
                         \Gamma((s-1)/2)\right]
  Z(\mathcal C,s).
\end{aligned}
\tag{CD10.1}
\]
All endpoint factors, both powers of \(\pi\), both Gamma factors and the full denominator \(64\) remain in this identity. The product has its entire continuation given by the two source elements \(F_0\), rather than by declaring any exceptional value a unit and discarding it.

At an original nontrivial zero \(\rho\), the shifted factor \(\zeta(\rho-1)\) is nonzero: its point is in \(-1<\Re s<0\), where the full functional equation transfers to \(\Re(1-s)>1\) with nonzero Euler product and unit factors. At a shifted nontrivial zero \(\rho+1\), the original \(\zeta(\rho+1)\) is nonzero by its absolutely convergent Euler product. Hence the local multiplicities of the two nontrivial divisors in \(Z(\mathcal C,s)\) are exactly \(m_\rho\), without cancellation. The entire source multiplier (CD10.1) has exactly their union, as already checked in GSL, and retains its endpoint and trivial-zero values through its two explicit \(F_0\) factors.

This gives a precise geometric provenance for the translated factor already used in that analytic extension: \(H^2=E(-1)\), with Frobenius \(p\), produces \(1-p^{1-s}\) in each local denominator, while \(H^0=E\) produces \(1-p^{-s}\). It does not identify the analytic zero-jet quotient with \(H^1\) of this conic. That group is zero in every geometric fibre by (CD7.1). The zeros of the global arithmetic product and the finite-dimensional cohomology of an individual fibre have the explicit determinant/Euler maps (CD8.3)–(CD10.1); no additional cohomological identification is asserted.

The construction also distinguishes this descent from the original unprojected evaluated scheme \(\mathbf P^1_{\mathbf Z[i]}\). CGT10.4 retains its two-component split and nonsplit local factors. The descended conic has the single factors calculated in CD8. They coincide with the rational invariant-cohomology factors of CGT9–CGT10 through the explicit generic descent, with the independently verified fibre at \(2\). Equality of those factors is not substituted for an isomorphism of the ramified integral schemes.

## CD11. Diagram and exact scope of the lift

The proved finite étale geometric diagram is
\[
\begin{array}{ccc}
\mathbf P^1_{\mathbf Z[1/2,i]}
 &\xrightarrow{\ \phi\ }&
\mathcal C_{\mathbf Z[1/2,i]}\\
\alpha\downarrow&&\downarrow c\\
\mathbf P^1_{\mathbf Z[1/2,i]}
 &\xrightarrow{\ \phi\ }&
\mathcal C_{\mathbf Z[1/2,i]}.
\end{array}
\tag{CD11.1}
\]
The right-hand object is the base change of the written conic over \(\mathbf Z[1/2]\). The two arithmetic-model maps at \(2\) are deliberately recorded with their actual domains: this \(\mathcal C_{\mathbf Z_2}\) has doubled-line special fibre and specialization \(h_s\mapsto2h_\eta\), while the CGT model \(\mathbf P^1_{\mathbf Z_2[i]}\) has the coefficient thickening and its two-branch diagonal specialization. Their generic relation has been proved and its failure to extend through \(\phi\) has been proved.

The resulting geometric lift (CD7.7) and proper pushforward (CD7.6) supply an actual Tate line with its coefficient two, and the complete original product (CD9.2). No map in this calculation identifies this specialization problem with the user's entire required weight-separation lifting problem. The calculation constructs concrete geometry receiving the CC action and the translated analytic divisor; it supplies no RH verdict and no new assumed purity for the original zero space.

## CD12. Independent derivation and retained work record

An independent mathematical derivation checked the odd-field character sum without an assumed point, every repetition at \(2\), flatness, the doubled-line fibre, the complete Euler product, and the nonremovable basepoint using the two sections in (CD5.3). The complete written derivation is supplied to the parent for reading and to the independent checker for verification of the descent, full maps and cohomological comparison.

This is the sole new file for this task. Source identities, reading coverage, exact receiver stage, and the correction audit are recorded in CD0. No peer source was edited, no remote publication occurred, and no arithmetic was assigned to the parityless supporting datum.
