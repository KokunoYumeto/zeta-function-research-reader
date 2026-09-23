# The zero-prime endpoint form through a nilpotent collision

23 September 2026. This note starts with the specified endpoint contribution \(W_0(a,b)=2\operatorname{Re}(a\overline b)\). It constructs the exact double-root family carrying that form, computes its sign on every real fibre, proves what a nilpotent thickening can retain, and constructs the positive correction by reflection. The calculation concerns this endpoint contribution. It does not identify the reflected endpoint contribution with the full corrected Weil distribution.

The original observed-family coordinates used in Section 8 are those of [the complete escaping-to-observed comparison, EFI51–EFI63](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/173dbc6ed5a03235dbe7654f928f3692107db39b/workbenches/splitzero-tandem/branches/tau-zero-prime-positivity/ESCAPING_FIBRE_INFINITESIMAL_DERIVATION.md). Their operator/metric distinctions are proved in [the original metric comparison, ISP45–ISP53](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/173dbc6ed5a03235dbe7654f928f3692107db39b/workbenches/splitzero-tandem/branches/tau-zero-prime-positivity/INFINITESIMAL_SUPPORT_POSITIVITY_DERIVATION.md), which was read for this calculation. Every finite algebra and form used below is defined and calculated here.

## 1. The endpoint form and its negative direction

Let \(V=\mathbb C^2\), with coordinates \(x=(a,b)\), coordinatewise multiplication, and unit \((1,1)\). Define the antilinear algebra involution and linear trace
\[
x^\#=(\overline b,\overline a),\qquad
\operatorname{tr}(a,b)=a+b.
\tag{PZS1}
\]
Applying the involution twice fixes each coordinate; it preserves products because multiplication is coordinatewise. Its trace-Hermitian form is
\[
W_0(x,y)=\operatorname{tr}(x^\#y)
=\overline b\,a'+\overline a\,b',
\qquad y=(a',b').
\tag{PZS2}
\]
It is conjugate-linear in its first entry, linear in its second, and Hermitian by direct conjugation and reordering of the two summands. Its matrix in the coordinate basis is
\[
J=\begin{pmatrix}0&1\\1&0\end{pmatrix},
\qquad W_0(x,y)=x^*Jy.
\tag{PZS3}
\]
In particular
\[
W_0(x,x)=2\operatorname{Re}(a\overline b)
=\frac12\bigl(|a+b|^2-|a-b|^2\bigr).
\tag{PZS4}
\]
Expansion of the absolute squares proves the last identity. The vectors \((1,1)/\sqrt2\) and \((1,-1)/\sqrt2\) are orthonormal eigenvectors of \(J\) with eigenvalues \(+1,-1\); hence the form has inertia \((1,1,0)\), in the order positive, negative, radical dimensions. This keeps the whole negative direction, rather than only its numerical value.

## 2. A flat algebra family with the required involution

For each real number \(u\), define
\[
A_u=\mathbb C[w]/(w^2-u),\qquad
(c+dw)^\#=\overline c-\overline d\,w.
\tag{PZS5}
\]
The involution is well-defined because \((w^2-u)^\#=w^2-u\) for real \(u\). It is multiplicative, antilinear, and has square the identity. The complete family is
\[
\mathcal A=\mathbb C[u,w]/(w^2-u),\qquad
\mathbb C[u]\longrightarrow\mathcal A,
\quad u\longmapsto w^2.
\tag{PZS6}
\]
Monic division gives the free \(\mathbb C[u]\)-basis \(1,w\); therefore the family is flat of rank two, including at \(u=0\). Its fibre is the stated quotient \(A_u\). The family has the coefficient-conjugating involution fixing \(u\) and sending \(w\) to \(-w\); its real fibres inherit PZS5.

In basis \(1,w\), multiplication by \(c+dw\) has matrix
\[
M_{c+dw}=\begin{pmatrix}c&ud\\d&c\end{pmatrix}.
\tag{PZS7}
\]
Its regular trace is \(2c\). Thus for \(p=c+dw\), \(q=c'+d'w\),
\[
\begin{aligned}
q_u(p,q)&:=\operatorname{Tr}_{A_u/\mathbb C}(M_{p^\#q})\\
&=2\overline c\,c'-2u\overline d\,d',
\end{aligned}
\qquad
[q_u]_{(1,w)}=\begin{pmatrix}2&0\\0&-2u\end{pmatrix}.
\tag{PZS8}
\]
To verify this, expand \((\overline c-\overline d w)(c'+d'w)\), whose constant coefficient is \(\overline c c'-u\overline d d'\), and apply PZS7. The displayed matrix also proves Hermitian symmetry.

## 3. The original endpoints occur at the exact fibre \(u=1/4\)

Evaluation at the two roots gives an algebra map
\[
E:A_{1/4}\longrightarrow V,\qquad
p\longmapsto\bigl(p(-1/2),p(1/2)\bigr).
\tag{PZS9}
\]
Its explicit inverse is
\[
E^{-1}(a,b)=\frac{a+b}{2}+(b-a)w.
\tag{PZS10}
\]
Substitution verifies both endpoint values. Conversely, for \(p=c+dw\), these values are \((c-d/2,c+d/2)\), and PZS10 recovers \(c,d\). This proves the algebra isomorphism, since evaluation is multiplicative.

One has the commuting identities
\[
E(p^\#)=E(p)^\#,
\quad \operatorname{Tr}_{A_{1/4}}(M_p)=\operatorname{tr}(E(p)),
\quad q_{1/4}(p,q)=W_0(E(p),E(q)).
\tag{PZS11}
\]
The first follows because negating the real roots interchanges them; the second follows by summing \(c-d/2\) and \(c+d/2\); the third follows from the first two and multiplicativity. It also follows directly by substituting PZS10 into PZS8:
\[
q_{1/4}(E^{-1}x,E^{-1}x)
=\frac12|a+b|^2-\frac12|b-a|^2=W_0(x,x).
\tag{PZS12}
\]
Thus the constant, variable, involution, and endpoint ordering are all fixed by exact maps.

## 4. The sign changes through the actual collision

The matrix PZS8 gives the full list
\[
\operatorname{inertia}(q_u)=
\begin{cases}
(1,1,0),&u>0,\\
(1,0,1),&u=0,\\
(2,0,0),&u<0.
\end{cases}
\tag{PZS13}
\]
For \(u\ne0\), the two complex roots of \(w^2-u\) are distinct, each with multiplicity one. For \(u=0\), the fibre is
\[
A_0=\mathbb C[w]/w^2,
\qquad w\ne0,\qquad \operatorname{rad}q_0=\mathbb Cw.
\tag{PZS14}
\]
Here \(w\ne0\) follows from the free basis, and the radical follows from the diagonal matrix. The collision has length two; no multiplicity is removed when its two points merge.

For \(u>0\), put \(r=\sqrt u>0\). Evaluation at \(-r,r\) identifies \(A_u\) with two coordinate factors, and the involution interchanges their conjugates. Its trace form is therefore the same hyperbolic endpoint form as PZS2. For \(u<0\), put \(r=\sqrt{-u}>0\). Evaluation at \(-ir,ir\) instead has
\[
(p^\#)(\pm ir)=\overline{p(\pm ir)},
\quad
q_u(p,p)=|p(-ir)|^2+|p(ir)|^2.
\tag{PZS15}
\]
Indeed \((p^\#)(z)=\overline{p(-\overline z)}\), and each imaginary root satisfies \(-\overline z=z\). The sum of the values still equals the regular trace. Evaluation is invertible because the roots are distinct. This proves directly why the involution and sign change together while the total length remains two.

There is an explicit continuing negative vector: the polynomial \(p=-2w\) corresponds at \(u=1/4\) to \((a,b)=(1,-1)\), and
\[
q_u(-2w,-2w)=-8u.
\tag{PZS16}
\]
It is negative for \(u>0\), zero for \(u=0\), and positive for \(u<0\). The fixed free module \(\mathbb C[u]\oplus\mathbb C[u]w\) supplies this precise continuation through the collision. A sign change is therefore possible in the real family. The nilpotent fibre itself makes this direction radical; positivity of that direction occurs after continuing to the other side.

The two signs are not connected by an involution-preserving isomorphism of the endpoint algebras. For \(u>0\), the two nontrivial primitive idempotents \((1\pm w/\sqrt u)/2\) are exchanged by \(\#\). For \(u<0\), the two primitive idempotents associated with the imaginary roots are each fixed by \(\#\), because evaluation has componentwise conjugation by PZS15. An algebra isomorphism permutes the two primitive idempotents, so cannot change an exchanged pair into a fixed pair while preserving the involution. There are nevertheless explicit algebra isomorphisms: for \(u>0,v<0\),
\[
A_u\longrightarrow A_v,\qquad
w\longmapsto i\sqrt{u/(-v)}\,w',
\tag{PZS17}
\]
with inverse multiplication by the reciprocal coefficient. Its square is \(u\) because \((w')^2=v\). Its precise involution defect on \(w\) is
\[
\phi(w^\#)-\phi(w)^\#=-2i\sqrt{u/(-v)}\,w'\ne0.
\tag{PZS18}
\]
This proves both the relationship and the information not preserved by that isomorphism.

## 5. A nilpotent thickening of the original endpoints keeps their negative residue

Let \(R\) be a commutative real algebra with a nilpotent ideal \(I\) and a fixed isomorphism \(R/I\cong\mathbb R\). Extend conjugation to \(R_{\mathbb C}=R\otimes_{\mathbb R}\mathbb C\) by fixing \(R\). Let \(\widetilde V=R_{\mathbb C}^2\) and let \(\widetilde G\) be any Hermitian matrix whose reduction modulo \(I\) is \(J\) of PZS3. This includes every matrix deformation of the original endpoint pairing over this nilpotent base.

For every lift \(\widetilde x\) of \((1,-1)\), reduction gives
\[
\widetilde x^*\widetilde G\widetilde x\pmod I=-2.
\tag{PZS19}
\]
This follows by applying the quotient homomorphism to the entire matrix product. On the other hand every element of the Hermitian-square cone
\[
\Sigma_R=\left\{\sum_{j=1}^n z_j^*z_j:
n\ge0,\ z_j\in R_{\mathbb C}\right\}\subset R
\tag{PZS20}
\]
has nonnegative residue, because its residue is \(\sum_j|\pi(z_j)|^2\), where \(\pi:R_{\mathbb C}\to\mathbb C\) is the quotient homomorphism. Therefore the value PZS19 is outside \(\Sigma_R\), for every possible nilpotent correction. No deformation of the pairing reducing to the original endpoint form can make all its values Hermitian-square-positive.

This result also has a scalar receiver: compose the deformed pairing with \(R\to\mathbb R\). The resulting scalar form is exactly \(W_0\) and retains value \(-2\) on every such lift. Thus the negative direction cannot be removed by adding terms that vanish under this residue map. Crossing the family from \(u=1/4\) to \(u<0\) in Section 4 changes the residue parameter; it is not a nilpotent thickening with residue \(u=1/4\).

## 6. Positive functionals at the collision and their exact radical

On the involutive algebra \(A_0\), call a complex-linear functional \(\ell\) positive when \(\ell(p^\#p)\) is a nonnegative real number for every \(p\). Then all such functionals are exactly
\[
\ell(c+dw)=t c,\qquad t\in\mathbb R_{\ge0}.
\tag{PZS21}
\]
Here is a direct proof. Positivity at \(p=1\) gives \(t=\ell(1)\ge0\). For \(p=1+dw\), the product is \(p^\#p=1+(d-\overline d)w\). With \(d=i y\), \(y\in\mathbb R\), positivity requires \(t+2iy\ell(w)\) to be real and nonnegative for every real \(y\). Its slope must be real because the whole expression is real, and must be zero because otherwise it takes negative values for one sign of sufficiently large \(y\). Hence \(\ell(w)=0\). Linearity proves the asserted form. Conversely \(\ell(p^\#p)=t|c|^2\ge0\), proving sufficiency.

For \(t>0\), the induced form \(\ell(p^\#q)\) has radical exactly \(\mathbb Cw\); for \(t=0\), its radical is all of \(A_0\). Thus every positive functional kills the nonzero infinitesimal direction, with the explicit augmentation map
\[
\epsilon:A_0\to\mathbb C,\quad c+dw\mapsto c,
\quad\ker\epsilon=\mathbb Cw,
\quad\ell=t\epsilon.
\tag{PZS22}
\]
The scalar section \(c\mapsto c\) splits this map and leaves its square-zero kernel specified.

More generally, let \(B\) be a positive semidefinite Hermitian form on the regular vector space of \(A_0\), compatible with the specified multiplication adjoints:
\[
B(M_a x,y)=B(x,M_{a^\#}y).
\tag{PZS23}
\]
Then \(B(w,w)=B(1,-w^2)=0\). A zero-norm vector of a positive semidefinite form lies in its radical: expanding \(B(x+tz,x+tz)\ge0\) with \(B(z,z)=0\) and varying complex \(t\) forces \(B(x,z)=0\). Apply this to \(z=w\). Thus compatible positivity cannot give a positive norm to the nilpotent regular generator. A positive norm on that generator requires a changed adjoint relation, whose concrete original-observation example is ISP51–ISP52.

## 7. An explicit positive correction on the fixed endpoint space

The linear involution \(J(a,b)=(b,a)\) is also an algebra automorphism of the endpoint algebra. Define
\[
W_+(x,y)=W_0(x,Jy).
\tag{PZS24}
\]
Using \(J^2=I\) in PZS3 gives
\[
W_+(x,y)=x^*y,
\qquad W_+(x,x)=|a|^2+|b|^2.
\tag{PZS25}
\]
Thus it is positive definite. Its exact difference from the original form is the positive rank-one form
\[
W_+(x,y)-W_0(x,y)
=\overline{(a-b)}(a'-b'),
\quad W_+(x,x)-W_0(x,x)=|a-b|^2.
\tag{PZS26}
\]
Expansion proves these formulas. The correction has kernel \(\{(a,a):a\in\mathbb C\}\) and takes value \(4\) on \((1,-1)\), changing the old value \(-2\) to \(+2\). This is an explicit way to flip the negative direction while retaining its removed contribution as a known form.

The same change can be expressed as a changed algebra involution. Put
\[
x^\star=J(x^\#)=(\overline a,\overline b).
\tag{PZS27}
\]
Then \(\operatorname{tr}(x^\star y)=W_+(x,y)\). The original involution \(\#\) and the new \(\star\) are related by the exact automorphism \(J\), but are not equal. On \(A_{1/4}\), the automorphism is the sheet map \(w\mapsto-w\). Under PZS27 the generator satisfies \(w^\star=w\); under the original involution it satisfies \(w^\#=-w\). This records the data altered by the correction.

The endpoint multiplication operator corresponding to the coordinate \(s\) is
\[
S=\begin{pmatrix}0&0\\0&1\end{pmatrix}.
\tag{PZS28}
\]
Its adjoint for \(W_0\) is
\[
S^{\dagger_0}=J S^*J=I-S,
\qquad W_0(Sx,y)=W_0(x,(I-S)y),
\tag{PZS29}
\]
whereas its adjoint for \(W_+\) is \(S^{\dagger_+}=S\). These follow by the displayed matrix products. Also \(JSJ=I-S\), proving the exact operator intertwining with the sheet switch.

Consequently the centered Fourier coordinate \(Y=(S-I/2)/i\) is self-adjoint for \(W_0\), but skew-adjoint for \(W_+\):
\[
Y^{\dagger_0}=Y,\qquad Y^{\dagger_+}=-Y.
\tag{PZS30}
\]
The sign in the first assertion follows because adjoints conjugate \(1/i\) and replace \(S-I/2\) by its negative. The second uses the ordinary adjoint of the real diagonal matrix \(S-I/2\). Thus positivity of the corrected form does not retain the old adjoint identity for this operator.

Let \(\mathcal P=\mathbb C[s]\), let \(\operatorname{ev}_{0,1}(f)=(f(0),f(1))\), and define the reflection automorphism \((Tf)(s)=f(1-s)\). Then
\[
\operatorname{ev}_{0,1}\,T=J\operatorname{ev}_{0,1},
\quad T^2=I,\quad T M_s=(I-M_s)T.
\tag{PZS31}
\]
Each identity follows by evaluation or direct substitution. Therefore
\[
W_0\bigl(\operatorname{ev}_{0,1}f,
\operatorname{ev}_{0,1}(Tg)\bigr)
=\overline{f(0)}g(0)+\overline{f(1)}g(1).
\tag{PZS32}
\]
This proves the positive correction as an exact reflected-test map for the endpoint contribution alone. Applying \(T\) to a test in a full analytic explicit formula also changes its other terms; PZS32 does not assert their invariance or positivity.

## 8. The observed quadratic pullback selects a side and an involution

Retain the observed family
\[
B_\lambda=\mathbb C[z]/(z^2-\lambda z),
\qquad \lambda=a_{\rm obs}(s-s_*),\quad a_{\rm obs}>0.
\tag{PZS33}
\]
For a real displacement \(s-s_*\), \(\lambda\in\mathbb R\). The exact coordinate map is
\[
w=z-\lambda/2,\qquad u=\lambda^2/4,
\quad w^2-u=z^2-\lambda z.
\tag{PZS34}
\]
It identifies \(B_\lambda\) with \(A_{\lambda^2/4}\). The inverse is \(z=w+\lambda/2\). Under the endpoint involution \(w^\#=-w\), one has
\[
z^\#=\lambda-z,
\quad [q^-_\lambda]_{(1,w)}=
\begin{pmatrix}2&0\\0&-\lambda^2/2\end{pmatrix},
\quad [q^-_\lambda]_{(1,z)}=
\begin{pmatrix}2&\lambda\\\lambda&0\end{pmatrix}.
\tag{PZS35}
\]
For the second matrix, trace of \(z\) is \(\lambda\) and \(z^\#z=(\lambda-z)z=0\). Its determinant is \(-\lambda^2\). Thus along this original real observed path, the endpoint form is indefinite for every \(\lambda\ne0\), and becomes radical at \(\lambda=0\). The base map \(u=\lambda^2/4\) stays on \(u\ge0\) and cannot reach the positive side \(u<0\) in PZS13.

The positive escaping trace previously calculated in EFI61–EFI62 and ISP45 instead uses the coefficient-conjugating involution \(w^\star=w\), equivalently \(z^\star=z\). With that involution its matrices are
\[
[q^+_\lambda]_{(1,w)}=
\begin{pmatrix}2&0\\0&\lambda^2/2\end{pmatrix},
\quad [q^+_\lambda]_{(1,z)}=
\begin{pmatrix}2&\lambda\\\lambda&\lambda^2\end{pmatrix}.
\tag{PZS36}
\]
This is the same algebra and the same regular trace, with the different stated involution. Their connecting automorphism is
\[
\sigma(w)=-w,\quad\sigma(z)=\lambda-z,
\quad \star=\sigma\circ\#,
\quad q^+_\lambda(p,q)=q^-_\lambda(p,\sigma q).
\tag{PZS37}
\]
To prove the form identity, regular trace is invariant under \(\sigma\): conjugation by an algebra automorphism sends a multiplication matrix to a similar matrix. Hence
\(\operatorname{Tr}(p^\#\sigma q)=\operatorname{Tr}(\sigma(p^\#)q)=\operatorname{Tr}(p^\star q)\). One can also verify it using
\[
[\sigma]_{(1,z)}=\begin{pmatrix}1&\lambda\\0&-1\end{pmatrix},
\quad
[q^+_\lambda]-[q^-_\lambda]
=\begin{pmatrix}0&0\\0&\lambda^2\end{pmatrix}.
\tag{PZS38}
\]
Thus the positive escaping trace has an exact relationship to the original negative endpoint form: it performs the fundamental-symmetry correction on the same fibres. This is not evidence that the original endpoint involution already had the positive trace.

At \(\lambda=0\), both trace forms have matrix \(\operatorname{diag}(2,0)\), although their involutions still differ on the nonzero nilpotent generator. For \(\lambda\ne0\), their signs differ exactly as PZS35–PZS36 calculate. This specifies the coincidence at the collision and the data that remain distinct there.

There is also a real obstruction to reaching the positive side through this fixed observed base map, valid over any real nilpotent parameter algebra with residue field \(\mathbb R\): the residue of \(\lambda^2/4\) is nonnegative. To access \(u<0\), one must change the real base path, or change the involution as in PZS37. Both constructions are explicitly available above, and neither is identified with a nilpotent correction leaving the original endpoint form unchanged.

## 9. What the calculation establishes for the proposed sign flip

The free family PZS6 and its original involution provide an actual passage from a negative direction, through a nonzero trace-null dual-number direction, to a positive direction, as PZS13–PZS16 prove. The original observed quadratic base map restricts this family to its nonnegative-\(u\) side. Its previously positive trace uses the alternative involution, connected by PZS37. On the fixed endpoint space, PZS24–PZS32 construct the positive correction and identify exactly its rank-one contribution and altered multiplication adjoint. A nilpotent thickening that reduces to the original endpoint pairing retains its negative residue by PZS19; at the collision, every positive functional has the explicit radical and augmentation in PZS21–PZS23.

These are complete calculations of the proposed endpoint mechanism. They retain the nilpotent, the full multiplicity, the sign-changing continuation, and the correction maps. The analytic effect of applying the same reflection or continuation to every other term of the corrected Weil formula is a separate calculation on those actual terms; no endpoint-only identity above asserts that effect.

## 10. Exact verification

The reproducible script `check_prime_zero_sign_deformation.py` passed 16 exact checks, recorded in `PRIME_ZERO_SIGN_DEFORMATION_CHECKS.json`. They verify the endpoint interpolation and its inverse, the involution and trace isometries, the continuing negative vector, the rank-one fundamental-symmetry correction, both endpoint multiplication adjoints, the two observed-coordinate trace forms and their sheet-switch relation, and preservation of a negative residue under a specified matrix deformation with nilpotent parameters. These checks use symbolic arithmetic. They support the calculations but do not replace the proofs for arbitrary parameters and nilpotent bases, and do not assert positivity of the full Weil formula.
