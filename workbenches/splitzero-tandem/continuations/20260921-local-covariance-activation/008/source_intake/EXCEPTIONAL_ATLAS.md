# Exceptional-map atlas: the finite signed-root completion

**Date:** 20 September 2026.  
**Basis:** `KokunoYumeto/zeta-function-research-reader`, commit
`405dd5b5d3ab99c5622e1aedb5a16404f6bf94eb`,
`workbenches/splitzero-tandem/continuations/20260920-fable-signed-states/FABLE_TO_ORIGINAL_CONDUCTOR.tex`,
Git blob `50b39a82568bbe5104aeed3de5ad9441cb6a5602`.

The source already supplies the four-coordinate polynomial, its complete ordinary fibres, image complement, nonproper-value locus, and signed monodromy. This note retains those formulas. Its additional work is the global finite degree-eight completion, its complete nonreduced fibres, the ramification and omitted-chart divisors, the finite-root escape and singular-value laws in a fixed original metric, the paired critical degeneration, and the completion's exact finite-field point counts.

The symbolic verifications accompanying this note check identities in the displayed algebra. The singular-value examples are explicitly artificial parameter diagnostics, not evaluations of a hypothetical zeta packet or the original period. No RH counterexample or new independent discovery of the Jacobian counterexample is asserted.

## 1. Original polynomial and factor map

In the original coordinates \(q=(a,y,z,w)\), put
\[
\begin{aligned}
b&=i+ay, &c&=-i+2ay+a^2z,\\
d&=-iy-a(iz+2y^2)-a^2yz,
&e&=2z-7iy^2+aw,\\
f&=iw+3iy^3-4yz+a(6iy^2z+wy+4y^4)+2a^2y^3z.
\end{aligned}
\tag{EA1}
\]
The target map is precisely
\[
P(q)=(ac,ae+bd,af+be,bf)=(A,B,C,D).
\tag{EA2}
\]
The original incidence and resultant are polynomial identities
\[
ad+bc=1,\qquad a^3f-a^2be+ab^2d-b^3c=1.
\tag{EA3}
\]
Thus, with \(L=aU+bV\) and \(K=cU^3+dU^2V+eUV^2+fV^3\),
\[
LK=H_u(U,V)=AU^4+U^3V+BU^2V^2+CUV^3+DV^4.
\tag{EA4}
\]
The cubic coefficient is one throughout. These are source FC31 and GF1–4 in factor form; expanding EA2 gives the exact four original component polynomials.

For \(a\ne0\), the marked root and scale are
\[
r=-b/a=-y-i/a,\qquad a^2h_u'(r)=1,
\quad h_u(s)=As^4+s^3+Bs^2+Cs+D.
\tag{EA5}
\]
Both square roots of \(1/h_u'(r)\) are retained. The original inverse is
\[
\begin{aligned}
a&=a,\qquad y=-r-i/a,\\
z&=A/a^3+2r/a+3i/a^2,\\
w&=7ir^2/a+(B-17r+Ar^2)/a^2-13i/a^3-2A/a^4.
\end{aligned}
\tag{EA6}
\]
These follow by successive coefficient comparison in EA4 and the two equations EA3. No local Jacobian assertion is needed to count these roots.

At \(a=0\), the original source contains exactly the state
\[
q_\infty(u)=\left(0,B,\frac{i(7B^2-C)}2,11B^3-2BC-D\right)
\tag{EA7}
\]
for every target with \(A=0\). Its factor has \(b=i\). The resultant-one factor with \(b=-i\) is absent from the original affine chart.

The source claims \(\det DP=-2\). Direct exact expansion in SymPy and an independent Wolfram evaluation give the same result. Section 2 also gives a short derivation that locates the cancelled boundary factor.

## 2. A finite-root chart that includes the escaping states

Use the **reciprocal** factor scale
\[
t=1/a.
\]
It is not a change that is invertible on the boundary. Its domain and added points are explicitly retained:
\[
\overline X_{\mathrm{fin}}
=\{(u,r,t):h_u(r)=0,\ t^2=h_u'(r)\}.
\tag{EA8}
\]
The two equations solve linearly for \(C,D\):
\[
\boxed{
\begin{aligned}
C&=t^2-4Ar^3-3r^2-2Br,\\
D&=3Ar^4+2r^3+Br^2-rt^2.
\end{aligned}}
\tag{EA9}
\]
Therefore this entire chart, including \(A=0\) and \(t=0\), is affine four-space in \((t,r,A,B)\).

Its projection to the unchanged target is
\[
\pi(t,r,A,B)=(A,B,t^2-4Ar^3-3r^2-2Br,
3Ar^4+2r^3+Br^2-rt^2).
\tag{EA10}
\]
On \(t\ne0\) its map to the original source is
\[
\boxed{
\begin{aligned}
q(t,r,A,B)=\bigl(&t^{-1},-r-it,At^3+2rt+3it^2,\\
&7ir^2t+(B-17r+Ar^2)t^2-13it^3-2At^4\bigr).
\end{aligned}}
\tag{EA11}
\]
Substitution gives the exact commuting equation
\[
P\circ q=\pi.
\tag{EA12}
\]
In the column order \((t,r,A,B)\),
\[
\boxed{\det D\pi=-2t^3,\qquad \det Dq=t^3.}
\tag{EA13}
\]
The ratio is the original \(-2\) for \(t\ne0\). Both sides of \(\det DP=-2\) are polynomials in the original coordinates, so the identity extends to the original \(a=0\) chart. EA13 exposes the ramification factor in the completed map and the identical factor in the meromorphic coordinate transformation; it does not replace the original polynomial map by a singular differential.

## 3. Infinity chart, transition, and finite flatness

Put
\[
v=V/U,\qquad k_u(v)=A+v+Bv^2+Cv^3+Dv^4.
\]
The second chart is
\[
\overline X_\infty=\{(u,v,\theta):k_u(v)=0,
\ \theta^2=-k_u'(v)\}.
\tag{EA14}
\]
On the intersection,
\[
\boxed{v=1/r,\qquad \theta=-t/r.}
\tag{EA15}
\]
Indeed \(k(v)=v^4h(1/v)\), and at a root
\(k'(v)=-v^2h'(r)\). The inverse is \(r=1/v,t=-\theta/v\).
Thus EA15 preserves both equations, including the sign.

At infinity \(v=0\),
\[
A=0,\qquad \theta^2=-1.
\tag{EA16}
\]
There are two disjoint infinity divisors, each parametrized by \((B,C,D)\). The factor coefficients on \(\theta\ne0\) are
\[
\boxed{
\begin{aligned}
a&=-v/\theta,& b&=1/\theta,\\
c&=\theta(1+Bv+Cv^2+Dv^3),&d&=\theta(B+Cv+Dv^2),\\
e&=\theta(C+Dv),&f&=\theta D.
\end{aligned}}
\tag{EA17}
\]
These formulas are obtained from EA4, and give EA3 by \(\theta^2=-k'(v)\).
The original included infinity sheet is \(\theta=-i\), or \(b=i\); the absent sheet is \(\theta=i\), or \(b=-i\).

### 3.1 An explicit regular inverse on the included sheet

The inverse EA6 has denominators \(a\), so it is not used without correction at \(a=0\). In the factor coordinates of EA3, on \(b(b+i)\ne0\), set
\[
Y=\frac{a^2f-abe+2b^2d}{b+i}.
\]
Then the complete regular inverse is
\[
\boxed{
\begin{aligned}
y&=Y,\\
z&=\frac{af-be+7Y^2-10iaY^3-4a^2Y^4}{2b^3},\\
w&=\frac{a^2eY^3+7ia^2Y^5+3iaeY^2-17aY^4-2eY-f-11iY^3}{b^3}.
\end{aligned}}
\tag{EA18}
\]
For the first identity, EA3 gives
\(b^2+1=a(a^2f-abe+2b^2d)\), hence \(b-i=aY\).
Substitute that identity into the incidence and resultant equations and divide only by the displayed units to obtain the other two expressions. The attached symbolic test verifies all three compositions with EA1 exactly. This chart contains the entire included infinity divisor. Together with \(a\ne0\), it proves the claimed open immersion of the original source.

### 3.2 The completion is finite locally free of degree eight

For \(A\ne0\), EA8 has the free algebra
\[
\mathcal O[r,t]/(h(r),t^2-h'(r))
\tag{EA19}
\]
with basis \(1,r,r^2,r^3,t,tr,tr^2,tr^3\). The nonzero leading coefficient is retained by using the monic equation \(A^{-1}h\).

There is a five-chart proof covering the entire characteristic-zero target. The exact coefficient identity is
\[
1=\tfrac12h(0)-\tfrac12h(1)-\tfrac16h(-1)+\tfrac16h(2)-2A.
\tag{EA20}
\]
On the open set where \(H(p,1)\ne0\), take the fixed determinant-one change
\[
(U,V)=(pU'-V',U').
\]
The new polynomial is \(h_p(z)=H(pz-1,z)\), with invertible leading coefficient \(H(p,1)\). The root and sign coordinates on the overlap are
\[
r_p=1/(p-r),\qquad t_p=t/(p-r).
\tag{EA21}
\]
At a root \(h_p'(r_p)=h'(r)/(p-r)^2\), so the same two monic relations give a free rank-eight algebra. Use \(p=0,1,-1,2\) and the original infinity chart \(A\ne0\); EA20 says these opens cover the base.

Thus the glued map
\[
\boxed{\pi:\overline X\longrightarrow\mathbb A^4_u}
\tag{EA22}
\]
is finite flat of degree eight. It is a finite completion over the coefficient base, not a claim that the total space is compact over a point.

The finite-root chart is smooth affine four-space. At infinity, the defining equations reduce to
\[
A=-v-Bv^2-Cv^3-Dv^4,\qquad
1+\theta^2+2Bv+3Cv^2+4Dv^3=0.
\]
At \(v=0\), the derivative with respect to \(\theta\) is \(2\theta\ne0\), so the completion is smooth there as well. The finite-root chart is dense and irreducible. Hence the completion is normal and is the finite normalization of the coefficient base in the degree-eight function-field extension of the original map.

### 3.3 Exactly which divisors the original source removes

The ramification divisor is
\[
R_0=\{t=0\}\cong\mathbb A^3_{A,B,r}.
\]
It has no point at infinity because EA16 has \(\theta\ne0\). The original omitted infinity divisor is
\[
D_-=\{A=0,v=0,\theta=i\}\cong\mathbb A^3_{B,C,D}.
\]
They are disjoint. EA11 and EA18 prove
\[
\boxed{\mathbb A^4_q\simeq\overline X\setminus(R_0\cup D_-).}
\tag{EA23}
\]
The two maps and their domains have been given explicitly. The constant Jacobian of the original affine map is compatible with ramification of its finite completion precisely because the original source removes \(R_0\).

## 4. All completed fibres, including their nilpotents

Let \(r_0\) be a finite root of exact multiplicity \(m\), and put \(\epsilon=r-r_0\). Write \(h=\epsilon^m g(\epsilon)\), \(g(0)\ne0\). In the fibre algebra,
\[
\epsilon^m=0,\qquad t^2=mg(0)\epsilon^{m-1}.
\tag{EA24}
\]
Terms of higher degree in the derivative are multiples of \(\epsilon^m\). A constant square-root scaling of \(t\) gives the following exact local types; its inverse is the reciprocal scaling.

| Original root multiplicity | Completed algebra at that root | Length | Original finite source states |
|---|---|---:|---:|
| 1 | two copies of \(\mathbb C\) | 2 | 2 |
| 2 | \(\mathbb C[t]/(t^4)\) | 4 | 0 |
| 3 | \(\mathbb C[\epsilon,s]/(\epsilon^3,s^2-\epsilon^2)\) | 6 | 0 |
| 4 | \(\mathbb C[\epsilon,s]/(\epsilon^4,s^2-\epsilon^3)\) | 8 | 0 |

For multiplicity two, \(\epsilon=t^2/(2g(0))\) supplies the stated isomorphism. The other two rows retain their two-generator relations. A basis in each case is \(1,\epsilon,\ldots,\epsilon^{m-1},t,t\epsilon,\ldots,t\epsilon^{m-1}\), proving length \(2m\).

At \(A=0\), infinity is always simple, because the \(U^3V\) coefficient is one. It contributes two reduced completed points, of which exactly the \(b=i\) point is in the original source.

Consequently the original counts \(8,4,2,0\) over quartics, and \(7,3,1\) over cubics, are obtained by deleting the indicated points from fibres of constant **scheme length eight**. In particular:

* a \(2+2\) target has two length-four completed points;
* a quadruple target has one length-eight completed point;
* a \(3+1\) target has one length-six point and two reduced points;
* a cubic triple target has a length-six finite point and two reduced infinity points.

No disappearing labelled states are identified with a zero-dimensional fibre of the completion.

### 4.1 Exact omitted surface and its quadruple curve

The original image complement is the smooth surface
\[
4AB-1-8A^2C=0,\qquad D-AC^2=0.
\tag{EA25}
\]
The maps
\[
(A,C)\mapsto(A,(4A)^{-1}+2AC,C,AC^2),\qquad
(A,B,C,D)\mapsto(A,C)
\]
are inverse, with domain \(A\ne0\). Thus this surface is explicitly \(\mathbb C^*\times\mathbb C\). On it
\[
h=A(s^2+s/(2A)+C)^2.
\]
The quadruple-root curve is
\[
\boxed{B=3/(8A),\quad C=1/(16A^2),\quad D=1/(256A^3),\quad A\ne0.}
\tag{EA26}
\]
Its root is \(-1/(4A)\). Away from this curve, EA25 has the \(2+2\) completed fibre.

### 4.2 Discriminant and full trace discriminant

Let \(\mathfrak D=\operatorname{Disc}(H_u)\), in the source's exact binary-quartic convention. On \(A\ne0\), \(\mathfrak D=A^6\Delta^2\), where \(\Delta=\prod_{i<j}(r_j-r_i)\).

In the basis EA19, the bilinear trace Gram is block diagonal:
\[
\operatorname{Tr}_{\overline X/u}(fg)
=\begin{pmatrix}2T&0\\0&2T_{h'}\end{pmatrix},
\quad T_{ij}=\sum r_l^{i+j},\quad
(T_{h'})_{ij}=\sum h'(r_l)r_l^{i+j}.
\]
Indeed the sign involution fixes the even part and negates the odd part. Vandermonde multiplication gives
\(\det T=\Delta^2\) and
\(\prod h'(r_l)=A^4\Delta^2\). Therefore
\[
\boxed{\det\operatorname{Tr}_{\overline X/u}(fg)
=256\,\frac{\mathfrak D^3}{A^{14}}.}
\tag{EA27}
\]
The factor \(A^{-14}\) belongs to this particular basis on \(A\ne0\). It is not an extra ramification component at \(A=0\).

The ramification divisor in the finite-root coordinates has multiplicity three by EA13. Its restriction to \(t=0\) is the repeated-root parametrization EA9. Its derivative has rank three exactly when
\[
\kappa=h''(r)=12Ar^2+6r+2B\ne0;
\]
the third column is \((0,0,-\kappa,r\kappa)^T\). Thus double-root points and the triple-root rank drop are located without a schematic discriminant label replacing the equations.

The original nonproper-value locus is exactly
\[
\boxed{\{A=0\}\cup\{\mathfrak D=0\}.}
\tag{EA28}
\]
These are the images of the two removed divisors in EA23. Over the complement, the finite completion is a disjoint local eight-sheet inverse. A convergent target family there has bounded roots and bounded nonzero derivatives, so EA6 bounds every source coordinate. On \(A=0\), the original factor-sign involution produces the escaping absent sheet; at a repeated root, the perturbation in section 5 supplies escaping states. This proves both inclusions.

## 5. Escape orders, local monodromy, and exact differential

### 5.1 Specified constant-term unfoldings

Take any actual quartic coefficient point with finite root \(r_0\) of multiplicity \(m=2,3,4\), and form the explicit family
\[
h_\varepsilon(s)=h_0(s)-\varepsilon.
\tag{EA29}
\]
This preserves the original cubic coefficient. Write
\(h_0(s)=c_m(s-r_0)^m+O((s-r_0)^{m+1})\), \(c_m\ne0\).
All roots in this cluster are obtained by inversion of
\(z=(s-r_0)[h_0(s)/(c_m(s-r_0)^m)]^{1/m}\), whose derivative at zero is one. This gives convergent Puiseux expansions, with the \(m\) choices and both factor signs retained:
\[
r-r_0=\zeta_m^j(\varepsilon/c_m)^{1/m}(1+O(\varepsilon^{1/m})),
\quad t^2=h_\varepsilon'(r).
\]
Their original states satisfy
\[
\boxed{
|\varepsilon|^{(m-1)/(2m)}\|\Psi q\|_\Gamma
\longrightarrow
\frac{\|\Psi e_a\|_\Gamma}{\sqrt m\,|c_m|^{1/(2m)}}.
}
\tag{EA30}
\]
Here \(\Psi\) and its original positive Gamma norm are held fixed. Equation EA11 proves the limit because \(a=1/t\) is the only divergent original coordinate and the remaining three tend to \((-r_0,0,0)\).

The target difference is exactly \(-\varepsilon e_D\). In the transported target it has norm \(|\varepsilon|\|\Psi e_D\|_\Gamma\). This restores the complete constant when measuring escape against target distance.

On a loop of \(\varepsilon\), the \(m\) roots cycle; after \(m\) loops the sign scale has changed by \((-1)^{m-1}\). Thus the cluster cycle types are:

| multiplicity | escape exponent in \(|\varepsilon|\) | cycle type on its signed states |
|---|---:|---|
| 2 | \(1/4\) | one four-cycle |
| 3 | \(1/3\) | two three-cycles |
| 4 | \(3/8\) | one eight-cycle |

The exponents belong to EA29, not all possible target paths. For example,
\(h_\varepsilon=h_0+\varepsilon(s-r_0)\) retains the root exactly and gives
\(t^2=\varepsilon\); its escape exponent is \(1/2\) for every original multiplicity. More generally the exact equation \(a^2h'(r)=1\) gives half the order of derivative vanishing along any chosen root arc.

### 5.2 The missing infinity sheet has a different exact pole

For a transverse target arc with \(A\to0\) and \((B,C,D)\) convergent, the included original branch tends to EA7. Its first coordinate is \(a=iA+O(A^2)\). Apply the original factor-sign involution
\[
\Sigma(a,y,z,w)=(-a,y+2i/a,6i/a^2-z,
 w-14iy^2/a+28y/a^2+40i/a^3).
\tag{EA31}
\]
The omitted branch has
\[
a=-iA+O(A^2),\quad y=2/A+O(1),\quad
z=-6i/A^2+O(A^{-1}),\quad w=-40/A^3+O(A^{-2}).
\]
Therefore
\[
\boxed{|A|^3\|\Psi q_{\mathrm{miss}}\|_\Gamma
\longrightarrow40\|\Psi e_w\|_\Gamma.}
\tag{EA32}
\]
In the completed infinity chart both sign states are finite. The obstruction is precisely the removed \(\theta=i\) sheet.

### 5.3 The full inverse differential, with every coefficient direction

For an infinitesimal target variation \(du=(dA,dB,dC,dD)\), put
\[
\ell_r=(r^4,r^2,r,1),\qquad
\ell'_r=(4r^3,2r,1,0),\qquad \kappa=h''(r).
\]
The exact root/sign differential is
\[
\boxed{dr=-\ell_rdu/t^2,\qquad
 dt=\ell'_rdu/(2t)-\kappa\ell_rdu/(2t^3).}
\tag{EA33}
\]
The original source differential is
\[
\begin{aligned}
da&=-dt/t^2,\\
dy&=-dr-i\,dt,\\
dz&=t^3dA+2t\,dr+(3At^2+2r+6it)dt,\\
dw&=(r^2t^2-2t^4)dA+t^2dB
+[14irt+(-17+2Ar)t^2]dr\\
&\qquad+[7ir^2+2(B-17r+Ar^2)t-39it^2-8At^3]dt.
\end{aligned}
\tag{EA34}
\]
Substitution of EA33 into EA34 is the whole matrix \(DP(q)^{-1}\), not a leading term. Multiplication in both orders with the original Jacobian gives the identity symbolically.

### 5.4 Every singular value along EA29, in a fixed original metric

Put \(G=\Psi^*\mathcal H_\Gamma\Psi\), where \(\mathcal H_\Gamma\) is the original cubic target Gram, not a Euclidean replacement. In the source and target coordinates \((a,y,z,w)\) and \((A,B,C,D)\), it is the same fixed form because the receiving map is the conjugacy \(P_W=\Psi P\Psi^{-1}\).

At the limiting root \(r_0\), define
\[
v=(1,-r_0^2,-2r_0^3,2r_0^4)^T,
\quad w=(0,1,-2r_0,r_0^2)^T,
\quad\ell=(r_0^4,r_0^2,r_0,1).
\]
Let
\[
\begin{aligned}
C_1&=\sqrt{v^*Gv}\sqrt{(G^{-1})_{zz}},\\
C_2&=\sqrt{\det([v\ w]^*G[v\ w])}
\sqrt{\det(G^{-1})_{\{z,w\},\{z,w\}}},\\
C_3&=\sqrt{G_{aa}}\sqrt{\ell G^{-1}\ell^*}.
\end{aligned}
\tag{EA35}
\]
They are strictly positive; the two vectors in the middle formula are independent.

For the four decreasing singular values of the original-metric derivative along EA29,
\[
\boxed{
\begin{aligned}
\sigma_1&\sim C_1|t|^{-3},\\
\sigma_2&\sim(C_2/C_1)|t|^{-2},\\
\sigma_3&\sim(C_3/C_2)|h_\varepsilon''(r)|,\\
\sigma_4&\sim2|t|^5/(C_3|h_\varepsilon''(r)|).
\end{aligned}}
\tag{EA36}
\]
The proof uses the exact compound-matrix leading terms:
\[
t^3DP\to v e_z^*,\qquad
 t^5\wedge^2DP\to(v\wedge w)(e_z\wedge e_w)^*,
\]
and EA33–34 gives
\[
DP^{-1}\sim \frac{h''(r)}{2t^5}e_a\ell
\]
along EA29. Here \(h''(r)/t^2\) grows like \((m-1)/(r-r_0)\), so the \(t^{-3}\ell'\) term is strictly lower order. The other three rows in EA34 are also lower order. The third exterior norm follows from the exact complementary exterior identity with \(|\det DP|=2\); consecutive exterior-norm ratios give EA36.

The exponents in \(|\varepsilon|\) are therefore

| \(m\) | \(\sigma_1\) | \(\sigma_2\) | \(\sigma_3\) | \(\sigma_4\) |
|---|---:|---:|---:|---:|
| 2 | \(-3/4\) | \(-1/2\) | \(0\) | \(5/4\) |
| 3 | \(-1\) | \(-2/3\) | \(1/3\) | \(4/3\) |
| 4 | \(-9/8\) | \(-3/4\) | \(1/2\) | \(11/8\) |

Their sum is zero, as the determinant demands. These are the particular completed-fibre approaches EA29. The exact differential EA33–34, rather than the table alone, applies to other approaches.

## 6. The original quartet collision as a finite rank-eight family

Take the original formal quartet roots
\(1/2\pm\delta\pm i\gamma\), retaining \(\gamma>2\), and put
\[
w=\delta^2,\qquad
h_w(s)=-\tfrac12\left(((s-\tfrac12-i\gamma)^2-w)
((s-\tfrac12+i\gamma)^2-w)\right).
\tag{EA37}
\]
The factor \(-1/2\) fixes the original cubic coefficient. For a height sign \(\eta=\pm1\), set
\(r_\eta=1/2+i\eta\gamma\) and \(\epsilon=r-r_\eta\). The corresponding root algebra has \(\epsilon^2=w\), and direct differentiation gives
\[
t^2=4\gamma^2\epsilon-4i\eta\gamma w.
\]
Consequently the complete four-state cluster is
\[
\boxed{
\mathcal A_\eta=
\mathbb C[[w]][t]/
\left(t^4+8i\eta\gamma w t^2
-16\gamma^2w(\gamma^2+w)\right),
\quad
r=r_\eta+\frac{t^2+4i\eta\gamma w}{4\gamma^2}.
}
\tag{EA38}
\]
The original paired root factors are coprime over \(\mathbb C[[w]]\); their retained resultant gives the two-cluster Chinese-remainder decomposition. At \(w=0\),
\[
\boxed{\mathcal A_+\oplus\mathcal A_-
\simeq\mathbb C[t]/t^4\oplus\mathbb C[t]/t^4.}
\tag{EA39}
\]
The root algebra \(\mathbb C[\epsilon]/\epsilon^2\) is embedded by
\(\epsilon\mapsto t^2/(4\gamma^2)\). Its nilpotent has not been removed.

The local base function is explicitly
\[
\boxed{
 w(t)=\tfrac12\left[-\gamma^2+\frac{i\eta t^2}{2\gamma}
+\gamma^2\sqrt{1-i\eta t^2/\gamma^3}\right]
=\frac{t^4}{16\gamma^4}+
\frac{i\eta t^6}{32\gamma^7}+O(t^8),
}
\tag{EA40}
\]
where the square-root branch takes value one at zero. Thus each cluster has ramification index four, and a loop about \(w=0\) gives the two disjoint four-cycles of the paired collision.

## 7. Arithmetic eligibility on the completed algebra

No equation \(h(r)=0\) is declared to be \(\xi(r)=0\). The actual scalar on the finite-root chart is
\[
\mathscr Z(u,r,t)=\xi(r),\qquad
\operatorname*{Res}_{s=r}\frac{\xi(s)}{h_u(s)}
=\frac{\xi(r)}{t^2}
\quad(t\ne0).
\tag{EA41}
\]
The sign involution fixes this scalar. It is holomorphic through every finite-root ramification point. At infinity it becomes \(\xi(1/v)\), which has an essential singularity: an entire function meromorphic at infinity is a polynomial, whereas the original Gamma completion of \(\xi\) grows faster than every polynomial on the positive real axis. The Gamma factor and \(\zeta(x)\to1\) give that growth directly.

For any finite fibre algebra and any holomorphic \(f\), multiplication by \(f(r)\) acts by the same matrix on its even and odd root-module summands. Hence
\[
\boxed{
\operatorname{Tr}M_{f(r)}=2\sum_jm_j f(r_j),\qquad
\det M_{f(r)}=\left(\prod_jf(r_j)^{m_j}\right)^2.
}
\tag{EA42}
\]
The class itself retains all Hermite jets; its zero determinant alone does not say it is zero. At a root of multiplicity \(m\), with \(\nu=\operatorname{ord}_{r_j}f\), the exact rank is
\[
\boxed{\operatorname{rank}M_f=2\max(m-\nu,0).}
\tag{EA43}
\]
This follows in the basis of EA24 by multiplying \(\epsilon^\nu\) and a unit on each of the two root-module summands.

For the paired critical limit, write
\(X(\gamma)=\xi(1/2+i\gamma)\in\mathbb R\). Conjugation and the original functional equation give
\(\xi'(r_\eta)=-i\eta X'(\gamma)\). Equation EA38 therefore gives the exact special-fibre class
\[
\boxed{
\xi(r)=X(\gamma)-\frac{i\eta X'(\gamma)}{4\gamma^2}t^2
\pmod{t^4}.
}
\tag{EA44}
\]
On a simple critical-zero stratum, this is nonzero with rank two on each length-four cluster. The original affine fibre is empty at that square target, but the completion retains the derivative as a nonzero nilpotent direction.

Along EA40, at such a simple critical zero,
\[
\boxed{\frac{\xi(r(t))}{t^2}
\longrightarrow -\frac{i\eta X'(\gamma)}{4\gamma^2}\ne0.}
\tag{EA45}
\]
At a nonzero critical value the same residue has a \(t^{-2}\) pole. At a critical zero of order at least two it tends to zero, and the higher jets determine the next term. These are distinct strata of the explicitly defined readout, not assumptions about the location of zeta zeros.

A candidate divisor of \(\xi\) requires its full Hermite remainder to vanish. For four distinct formal quartet roots, this is equivalently the four equalities \(\xi(r_j)=0\). None is supplied by the resultant-one construction.

## 8. Sign cover and monodromy: what is retained and what is added

The source calculates the monodromy group
\[
G=\{(\sigma,\pi)\in\{\pm1\}^4\rtimes S_4:
\prod_j\sigma_j=\operatorname{sgn}\pi\},\qquad |G|=192.
\tag{EA46}
\]
Its adjacent-root exchanges are four-cycles on the corresponding signed states. Their squares generate every even sign pattern. Their product is an eight-cycle. This is the source's signed permutation group, not an unproved identification with another group of order 192.

The new completion extends the deck involution **regularly**:
\[
\boxed{(r,t)\mapsto(r,-t),\qquad
(v,\theta)\mapsto(v,-\theta).}
\tag{EA47}
\]
Its fixed locus is the finite-root ramification divisor. It exchanges the two infinity divisors. Therefore it does not preserve the open source EA23: it takes the included infinity sheet to the removed one. On the original source its rational expression is precisely EA31, with the pole \(2i/a\). This identifies the complete boundary reason it has no global polynomial deck extension there.

The quotient by EA47 is the original universal projective root scheme. On EA19 its invariant part is \(\mathcal O[r]/h\), embedded as the even part. The odd part is \(t\mathcal O[r]/h\); it is a module, and its products return to the even part by \(t^2=h'(r)\). These formulas continue to hold in the nonreduced fibres EA24 and EA39.

## 9. Exact finite-field counts of this specific completion

The equations EA8, EA14, and transition EA15 contain no \(i\). Thus the completion descends to every field of odd characteristic. Its finite-root chart is exactly \(\mathbb A^4\) by EA9. The complement is
\[
\mathbb A^3_{B,C,D}\times\operatorname{Spec}K[\theta]/(\theta^2+1).
\tag{EA48}
\]
For an odd prime power \(\mathfrak q\), let \(\chi_{\mathfrak q}(-1)\in\{1,-1\}\) be its quadratic character. Directly counting the two strata gives
\[
\boxed{
\#\overline X(\mathbb F_{\mathfrak q^n})
=\mathfrak q^{4n}+
[1+\chi_{\mathfrak q}(-1)^n]\mathfrak q^{3n}.
}
\tag{EA49}
\]
Its exact finite-field zeta function, by its defining exponential series, is
\[
\boxed{
Z(\overline X/\mathbb F_{\mathfrak q},u)
=\frac1{(1-\mathfrak q^4u)(1-\mathfrak q^3u)
(1-\chi_{\mathfrak q}(-1)\mathfrak q^3u)}.
}
\tag{EA50}
\]
Over fields containing \(i\), the original polynomial open chart is defined, and EA23 gives the same count as \(\mathbb A^4\) plus its two explicit removed \(\mathbb A^3\) divisors. Over fields not containing \(i\), the two infinity components are conjugate; the completed model is still defined over the base field, but the original chosen \(i\)-chart is not silently declared to descend.

Exact finite-field enumeration verifies EA49 at sizes 3, 5, 7, and 11. At size 5, where \(i=2\), all 625 target fibres of the original polynomial were also checked against the original simple-root/infinity rule. These computations check the geometric model, not a specialization of an unspecified complex arithmetic zero.

For the finite root-coordinate action, Frobenius obeys the exact equation
\[
\operatorname{Fr}_{\mathfrak q}M_r=M_{r^{\mathfrak q}}\operatorname{Fr}_{\mathfrak q}.
\]
EA50 is the point-counting zeta function of the displayed finite completion. No equality with the Riemann zeta function, or with the program's missing same-class Frobenius realization, is inserted.

## 10. Return through the original weighted conductor

Retain the original finite-shift conductor
\[
\mathcal T_AP(S')=\sum_{u,w}a_{uw}P(S'+\beta_{8,u,w}),
\quad v=\operatorname{ord}_0E_A,\quad\mu_v\ne0.
\]
For \(\mathcal U=\mathcal P_{v+3}/\mathcal P_{v-1}\) and \(\mathcal W=\mathcal P_3\), the source fixes
\[
x_j=[S^v\ell_j(S)],\quad y_j=\mathcal T_Ax_j,
\quad X e_j=x_j,\quad Y e_j=y_j.
\]
With the source's original collision matrix \(K\),
\[
\Phi_{\mathrm{FC}}=XK^{-1},\qquad\Psi=YK^{-1},\qquad
\mathcal T_A\Phi_{\mathrm{FC}}=\Psi.
\tag{EA51}
\]
Every entry is fixed by the original moments:
\[
[\Psi]=B_v(V_\rho^T)^{-1}K^{-1},\qquad
(B_v)_{kr}=\binom{v+r}{k}\mu_{v+r-k}\ (k\le r),
\]
with zeros for \(k>r\). The inverse is the explicit product of the three inverses. Its determinant is nonzero by \(\mu_v\ne0\), the original Vandermonde, and \(\det K=77\sqrt2 i/2\).

The nonlinear receiving map is \(P_W=\Psi P\Psi^{-1}\). The finite completion in its target is the same \(\overline X\), now with base projection \(\Psi\pi\), and open source immersion \(p\mapsto\iota(\Psi^{-1}p)\). This gives all completed fibres and boundary maps without varying the original period or metric along the target deformation.

The original target norm is
\[
\|p\|_\Gamma^2=
\int_{\mathbb R}|p(c+iy)|^2
\frac{(2\pi)^{s/2}2^{s/2}}{4\pi\Gamma(s/2)}
|\Gamma(s/4+iy/2)|^2dy.
\]
Thus \(G=\Psi^*\mathcal H_\Gamma\Psi\) in EA35 retains every mass and cross term. In its monomial frame,
\[
(\mathcal H_\Gamma)_{jk}
=\sum_{p=0}^j\sum_{q=0}^k
\binom jp\binom kq c^{j+k-p-q}(-i)^pi^q m_{p+q},
\]
where, for \(b=s/2\), \(M_s=(2\pi)^{s/2}\),
\[
m_0=M_s,\quad m_2=M_sb,\quad m_4=M_s(3b^2+2b),
\quad m_6=M_s(15b^3+30b^2+16b),
\]
and all odd moments vanish. This makes every metric constant in EA30, EA32, and EA35–36 finite and explicit in the original input data.

None of the added nonlinear degenerations changes the original conductor determinant
\[
\det A_{D,s}=
\left[(-i)^v\mu_v/v!\right]^{D+1}
\prod_{j=0}^D\rho_{j+v}/\rho_j.
\]
The source already gives its exact fixed-old-quotient order-jump correction. That correction remains separate from the ramification of the introduced nonlinear completion, through EA51 rather than by an assertion of unrelatedness.

## Verification and source status

* The source's original determinant and collision were checked directly in SymPy. Wolfram independently returned the determinant \(-2\), the full composition EA12, and both Jacobians in EA13.
* Exact symbolic checks cover the source factorization, all inverse-chart identities, both differential inverse compositions, exterior leading matrices, paired critical algebra, omitted surface, and the five-open cover.
* The finite-field counts and all original \(\mathbb F_5\) fibres are exact finite arithmetic.
* The singular-value diagnostics use nine artificial quartics/approach points and a fixed artificial positive matrix with nonzero cross terms. They are non-interval high-precision checks, not substitutes for the proofs of EA36.
* No native program action, arithmetic zero, or full Weil sign is inferred from those finite geometric tests.

The source-derived fibre classification and signed monodromy remain credited to the repository. The new completion, its displayed arithmetic-jet and finite-field calculations, and the finite-collision singular-value formulas are the continuation proved here. Their scope is this explicit map and its explicitly transported conductor realization.
