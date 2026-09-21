# Four labelled roots, eight oriented factor states, and the original conductor

## Source boundary and coordinates

The incoming transcript reports four labelled Time components, a seven-point affine fibre, an eighth factor-sign state excluded by the chart `b=i+ay`, and an escaping branch whose image tends to `2i` times a target basis vector. The transcript does not supply the coefficient list of the unpublished `FABLE_TO_ORIGINAL_CONDUCTOR.tex`. The following polynomial is an **explicitly reconstructed linear–cubic factor realization**, with its coefficient map, inverse, and verification supplied here. No byte-for-byte or coordinate-name identity with that unpublished file is asserted. The four names M,N,T,E are retained as abstract labels; their assignment to displayed projective roots is not guessed. In particular A from an earlier informal label list is not silently identified with N.

All results below are proved for the displayed map and for its explicitly defined conjugation into the original conductor. They do not identify that nonlinear map with the original linear conductor, the native observation, or its proper-source target minimum.

## 1. Complete factor chart

Let x=(a,y,z,t) in C^4. Set

\[
\begin{aligned}
b&=i+ay,&c&=-i+2ay+a^2z,\\
d&=-iy-2ay^2-iaz-a^2yz,&e&=-7iy^2+2z+at,\\
f&=2a^2y^3z+aty+4ay^4+6iay^2z+it+3iy^3-4yz.
\end{aligned}
\]

Put L=aU+bV and Q=cU^3+dU^2V+eUV^2+fV^3. Direct multiplication proves

\[
ad+bc=1,\qquad \operatorname{Res}(L,Q)=-cb^3+dab^2-ea^2b+fa^3=1.
\]

Define

\[
P_i(a,y,z,t)=(ac,\ ae+bd,\ af+be,\ bf)=(A,B,C,D).
\]

Thus

\[
LQ=AU^4+U^3V+BU^2V^2+CUV^3+DV^4.
\]

On a nonzero, the inverse factor coordinates are

\[
y=(b-i)/a,\qquad z=(c+i-2ay)/a^2,\qquad
 t=(e+7iy^2-2z)/a.
\]

On a=0 the factor constraints give b=+i or -i. The displayed chart contains precisely b=i, c=-i, with free d,e,f, and its inverse there is

\[
y=id,\quad z=(e+7iy^2)/2,\quad t=(f-3iy^3+4yz)/i.
\]

The other sign is retained in the second chart P_{-i}, obtained by replacing every i by -i. This is the same factor space, not removal of the eighth state. The two-chart transition on a nonzero is

\[
C_{-+}(a,Y,Z,T)=
\left(a,Y-2i/a,Z+6i/a^2,T+14iY^2/a+28Y/a^2-40i/a^3\right),
\]

and

\[
P_i\circ C_{-+}=P_{-i},\qquad \det DC_{-+}=1.
\]

### Constant Jacobian

On a nonzero use intermediate coordinates (a,b,c,e). Their Jacobian from (a,y,z,t) is a^4. Elimination gives

\[
\begin{aligned}
A&=ac,\\
B&=ae+b/a-b^2c/a,\\
C&=(1-b^2+2cb^3)/a^2+2be,\\
D&=b(1-b^2+2cb^3)/a^3+b^2e/a.
\end{aligned}
\]

The Jacobian of these four functions with respect to (a,b,c,e) is -2/a^4. The chain rule therefore gives

\[
\boxed{\det DP_i=-2.}
\]

Both sides are polynomials, so the equality extends to a=0. There is no finite critical point.

## 2. All fibres, the exact image, and the nonproper set

Write

\[
F_Y(u)=Au^4+u^3+Bu^2+Cu+D.
\]

For every finite simple root r of F_Y, the full oriented factor states are

\[
a^2F_Y'(r)=1,\quad b=-ar,\quad
L=a(U-rV),\quad Q=F_Y(U,V)/L.
\]

There are exactly two signs of a, and the chart inverse above recovers exactly two source points. A repeated selected root is impossible because its resultant would be zero. For A=0, infinity is a simple projective root since the coefficient of U^3V remains 1. Its two normalized factors have b=+i and b=-i, and exactly the first lies in the displayed chart.

If n_s(Y) is the number of finite simple roots, this proves

\[
\boxed{\#P_i^{-1}(Y)=2n_s(Y)+\mathbf1_{A=0}.}
\]

The exact possibilities are 8,4,2,0 for quartics of root patterns 1111,211,31,22 or 4, respectively; they are 7,3,1 for cubics of root patterns 111,21,3. Every finite preimage is reduced, since the Jacobian is invertible there.

A quartic with no simple root is a scalar times a squared quadratic. In the literal coefficient slice it has

\[
F_Y(u)=A\left(u^2+\frac{u}{2A}+C\right)^2.
\]

Consequently the full image is

\[
\boxed{
P_i(\mathbb C^4)=\mathbb C^4\setminus
\{4AB-8A^2C=1,\quad D=AC^2\}.
}
\]

The equation 4AB-8A^2C=1 itself ensures A nonzero. This omitted codimension-two set includes both double-double and quadruple-root polynomials. No cubic target is omitted.

Let Delta(Y) be the binary quartic discriminant, with its polynomial continuation to A=0 (where it equals the cubic discriminant). Then the exact nonproper-value set is

\[
\boxed{S_{P_i}=\{A=0\}\cup\{\Delta(Y)=0\}.}
\]

Proof of inclusion for A=0: every such target has a finite lift in the negative chart at a=0,b=-i. In negative-chart coordinates one can take

\[
Y_0=B,\quad Z_0=\frac i2(C-7B^2),\quad
T_0=-D-3B^3+4iBZ_0.
\]

Let a tend to zero with these three coordinates fixed and use C_{-+}. Its y coordinate diverges as -2i/a, whereas its image converges to the given target. For a finite multiple root r of F_0, put F_epsilon=F_0+epsilon^2(u-r). The marked root remains r, its derivative is epsilon^2, and the normalized factor coefficient a=1/epsilon diverges. This constructs an escaping lift to every discriminant target. Conversely, on any compact set avoiding A=0 and Delta=0, all four roots are uniformly bounded and separated, and their derivatives are bounded above and away from zero. The formulas for a,b,c,d,e,f and for the source coordinates then bound every preimage. This proves the reverse inclusion.

### The seven-point collision

For Y_*=(0,0,-1,0), the product is UV(U-V)(U+V). It has the four distinct projective roots infinity,0,1,-1. There are eight oriented normalized factor states, and precisely seven points in the positive chart. They are listed exactly in checks.json. The positive infinity state is (0,0,i/2,0). The two zero-root states are (-i,1,-3i,-13) and (i,-1,-3i,13). The remaining four follow the same derivative formula with a=+/-1/sqrt(2). Their root labels are kept separate from the signs.

### Completing the missing sign separates two different boundary mechanisms

The two charts cover the smooth affine fourfold

\[
\mathfrak X=\{(a,b,c,d,e,f):ad+bc=1,\ -cb^3+dab^2-ea^2b+fa^3=1\}.
\]

Their intersection is precisely a nonzero and is isomorphic to C^* times C^3. Smoothness follows directly: scale L and Q separately. The derivatives of the two defining functions on these two tangent directions form the matrix [[1,1],[3,1]], with determinant -2. For the factor multiplication map pi:X->C^4, a tangent vector in its kernel satisfies delta L Q+L delta Q=0. Coprimality forces delta L=lambda L and delta Q=-lambda Q. Differentiating the resultant gives 2lambda=0. Thus pi is locally invertible at every point of X, including both a=0 sign components.

For completeness, the chart inverse is regular at the relevant zero component, not only set-theoretic. Work near b=i, so b+i and b are units. The two defining relations imply successively b-i is divisible by a, c+i-2ay is divisible by a^2, and e+7iy^2-2z is divisible by a. They give the displayed regular y,z,t. One may see these divisibilities by substitution into the two relations and cancellation of a on their dense a-nonzero open subset; smoothness and the reduced a=0 component extend the resulting identities. The negative chart is identical with i replaced by -i. Thus the two displayed copies of C^4 are actual open charts of X.

Restoring the other chart removes the entire spurious nonproper hyperplane A=0 away from the discriminant:

\[
\boxed{S_\pi=\{\Delta=0\},\qquad
\#\pi^{-1}(Y)=2\,\#\{\hbox{simple projective roots of }F_Y\}.}
\]

To prove properness over the squarefree locus, use disjoint compact local disks about all four projective roots, choosing either U/V or V/U at each root. In each disk the nonzero derivative and the normalized resultant give exactly two bounded factor scales. Their finite union bounds every lift of a compact sufficiently small target neighborhood. Conversely the multiple-root deformation used above has an unbounded factor coefficient, so adding the other a=0 chart cannot cure that escape. The full eight-state fibre at Y_* is restored, but a repeated selected root still cannot satisfy resultant one.

The completion has a genuine topology difference from affine four-space. The two contractible charts have intersection C^* times C^3, so the Mayer--Vietoris sequence gives

\[
\boxed{H_2(\mathfrak X;\mathbb Z)\simeq\mathbb Z,
\quad H_j(\mathfrak X;\mathbb Z)=0\ (j>0,\ j\ne2).}
\]

This explicitly prevents identifying the completed factor space with C^4. This is ordinary singular homology of this finite-dimensional factor variety, not a replacement of any original source topology or tau-seminorm.

## 3. Monodromy retains the signs

On the target open set A Delta nonzero, P_i is an eight-sheet covering. Let r_1,...,r_4 be temporarily ordered roots and choose a_j^2=1/F_Y'(r_j). Put V(r)=product_{j<l}(r_j-r_l). Then

\[
\prod_j F_Y'(r_j)=A^4V(r)^2,
\qquad A^2V(r)\prod_j a_j\in\{+1,-1\}.
\]

The last value is constant under analytic continuation on an ordered lift. A monodromy permutation pi with sheet signs epsilon_j therefore obeys

\[
\prod_j\epsilon_j=\operatorname{sgn}(\pi).
\]

A small half-twist around a simple discriminant point exchanges two roots. Its lift is an order-four permutation of their four oriented states: in suitable sign conventions,

\[
(\alpha,+)\mapsto(\beta,+)\mapsto(\alpha,-)
\mapsto(\beta,-)\mapsto(\alpha,+).
\]

After squaring, it flips exactly the two signs. Such pair flips generate the eight-element even sign subgroup. The root permutations generate S_4; they may be realized with a fixed nonzero sum of roots, hence a fixed A=-1/sum r_j, so the coefficient slice imposes no missing generator. The full monodromy is therefore the 192-element group

\[
\boxed{\{(\epsilon,\pi)\in\{\pm1\}^4\rtimes S_4:
\prod\epsilon_j=\operatorname{sgn}\pi\}.}
\]

The Time labels M,N,T,E can be attached to the four roots at a basepoint without identifying any of them. Their four-label permutation action is the quotient by the even sign subgroup. Keeping only four root labels loses the order-four lifted monodromy.

The product-preserving global sign on the normalized factor space is (L,Q)->(-L,-Q). In the positive chart it is the rational involution

\[
\left(-a,y+2i/a,-z+6i/a^2,
 t-14iy^2/a+28y/a^2+40i/a^3\right).
\]

It has poles at a=0; it is not an everywhere-defined polynomial symmetry of this one chart. Its apparent absence there is exactly the lost negative infinity state.

## 4. Quantitative degeneration at the escaped sign

Take epsilon positive and

\[
x_\epsilon=
\left(\epsilon,-2i/\epsilon,6i/\epsilon^2,-2i-40i/\epsilon^3\right).
\]

The image is exactly

\[
\boxed{P_i(x_\epsilon)=(i\epsilon,-2i\epsilon^2,-4\epsilon,2i).}
\]

Thus the image tends to 2i e_4, while x_epsilon has a cubic pole. In any fixed positive metric H on these retained four coordinates,

\[
\|x_\epsilon\|_H\sim40\sqrt{H_{44}}\epsilon^{-3}.
\]

At (epsilon,0,0,-2i) the two-chart derivative is

\[
DC_{-+}=
\begin{pmatrix}
1&0&0&0\\
2i\epsilon^{-2}&1&0&0\\
-12i\epsilon^{-3}&0&1&0\\
120i\epsilon^{-4}&28\epsilon^{-2}&0&1
\end{pmatrix}.
\]

The maximal exterior pole orders at ranks 1,2,3,4 are exactly 4,5,4,0; the unique leading minors have coefficients 120i,-336i,64i,1. Consequently its singular exponents are -4,-1,1,4. Since

\[
DP_i(x_\epsilon)=DP_{-i}(\epsilon,0,0,-2i)(DC_{-+})^{-1}
\]

and DP_{-i}(0,0,0,-2i) is invertible, the four singular scales in ANY fixed positive source and target metrics are

\[
\boxed{\epsilon^{-4},\quad\epsilon^{-1},\quad\epsilon,\quad\epsilon^4.}
\]

Here a scale means two-sided comparability with strictly positive constants fixed with those metrics. The squared relative metric scales are epsilon^{-8},epsilon^{-2},epsilon^2,epsilon^8; the condition number is comparable to epsilon^{-8}. Nonetheless det DP_i=-2 exactly. In the same constant metric on both sides the squared volume Jacobian is exactly 4. This is a quantified anisotropic degeneration at infinity, not a finite determinant zero.

### A different metric degeneration at a genuine repeated-root boundary

The restored chart does not repair all nonproperness. For epsilon positive set

\[
z_\epsilon=(\epsilon^{-1},-i\epsilon,3i\epsilon^2,
\epsilon^2-13i\epsilon^3).
\]

Exact substitution gives

\[
\boxed{P_i(z_\epsilon)=(0,1,\epsilon^2,0),\qquad
F_\epsilon(u)=u^3+u^2+\epsilon^2u.}
\]

The selected root is zero and its derivative is epsilon^2. The normalized factor therefore has a=epsilon^{-1}; this divergence occurs in the full factor space X, not just in its plus chart. The discriminant is epsilon^4(1-4epsilon^2). The differential is exactly

\[
DP_i(z_\epsilon)=
\begin{pmatrix}
4i&2\epsilon^{-2}&\epsilon^{-3}&0\\
2\epsilon-14i\epsilon^2&-13&2\epsilon^{-1}&\epsilon^{-2}\\
-2\epsilon^3-2i\epsilon^2&2&0&0\\
-i\epsilon^4&\epsilon^2&0&0
\end{pmatrix}.
\]

Its maximal exterior pole orders are 3,5,5,0, with leading coefficients 1,1,2,-2. Thus in every fixed positive source and target metric its singular scales are

\[
\boxed{\epsilon^{-3},\quad\epsilon^{-2},\quad1,\quad\epsilon^5.}
\]

The relative pullback-metric scales are epsilon^{-6},epsilon^{-4},1,epsilon^{10}. This separates a genuine selected-root collision from the lost-sign chart boundary, whose four scales were different. Both retain constant nonzero Jacobian; neither supplies a finite rank-zero point of the conductor.

## 5. Exact embedding through the original conductor

Retain the original conductor order v, moment mu_v nonzero, complete source orders s and degree D, and its actual square matrix

\[
A_{D,s}=\operatorname{diag}(\rho_j)^{-1}T_D(g)
\operatorname{diag}(\rho_{j+v}),\qquad
\rho_n^2=n!/(s/2)_n,
\]

\[
g(t)=t^{-v}e^{-4w(t)}E_A(w(t)),\quad w(t)=-i\arctan t,
\quad g(0)=(-i)^v\mu_v/v!.
\]

Thus

\[
\det A_{D,s}=g(0)^{D+1}\prod_{j=0}^D\rho_{j+v}/\rho_j\ne0.
\]

This is the existing original conductor from WCF/LRC, not the nonlinear polynomial P_i. At fixed original data it has no input-dependent singular point.

Here is one explicit four-channel injection into the unchanged target space. For the original simple lower grid of degree k-8, let lambda_alpha^- be its four distinct corners in the retained order and put

\[
j_\alpha(S')=\frac{\chi_{k-8}(S')}
{(S'-\lambda_\alpha^-)\chi_{k-8}'(\lambda_\alpha^-)},\qquad
Jz=\sum_{\alpha=1}^4 z_\alpha j_\alpha.
\]

The source cutoffs under discussion satisfy D at least (k-7)^2-1, so these are elements of the literal target polynomial space. The inverse on this four-dimensional image is evaluation at the four labelled corners. Any already prescribed arithmetic Taylor units are retained when this polynomial injection is composed with the original arithmetic inclusion. For a different retained label ordering, insert its permutation matrix on the right of J and its inverse in the evaluation map; no assignment of the unseen Time labels to these four corners is inferred. Set L=A_{D,s}^{-1}J. Then A_{D,s}L=J, with inverse on each of these four-dimensional images specified by the corresponding coordinate map. Define

\[
\mathcal F_-=JP_iJ^{-1},\qquad \mathcal F_+=LP_iL^{-1}.
\]

They obey the exact typed equation

\[
A_{D,s}\mathcal F_+=\mathcal F_-A_{D,s}.
\]

The inverses J^{-1},L^{-1} here are only on their displayed images. All seven finite collision points, the eighth oriented factor state in the other chart, the full nonproper divisor, and the monodromy are carried by these maps. The transported missing-value set is J applied to the codimension-two set in Section 2. The nonproper set is J applied to {A Delta=0}. Every finite differential determinant in these common transported frames is still -2. There is no implication that the original A_{D,s} has become singular.

For the original positive Gram G_N or a retained attained quotient Gram, the actual four-channel pullback is J^*G_NJ. If the same four-channel map remains injective after the specified quotient, this is positive, and the metric rates in Section 4 apply to it without changing any affine minimizing fibre. If that quotient kills a direction, its kernel is retained and the four-dimensional positive-metric assertion is applied only on the actual image; rank is not restored by fiat.

The original multiplication action has a separate explicit translation residual. Before passing to its own quotient it satisfies

\[
\mathcal T_A(SP)=S'\mathcal T_AP+\mathcal T_{A'}P,\qquad
\mathcal T_{A'}P=\sum_{u,w}a_{uw}\beta_{8,u,w}P(S'+\beta_{8,u,w}).
\]

For centers c and c'=c-4, the centered residual replaces beta by beta-4. Thus conjugating the new nonlinear map through A_{D,s} does not silently make A_{D,s} an intertwiner for the original multiplication actions.

If the conductor parameters themselves vary and its order changes from v to v+r, the old fixed-quotient matrix has rank max(D+1-r,0). Its kernel has dimension min(r,D+1), consisting precisely of the extra low polynomial degrees. Rebuilding the quotient at the new order restores the correctly typed square map. The Fable source coordinates do not by themselves vary the original moment mu_v.

## 6. Which arithmetic action survives, and the explicit replacement

For a constant complex 4x4 matrix B, consider infinitesimal equivariance

\[
DP_i(x)Bx=BP_i(x).
\]

The full solution space is

\[
\boxed{B=\tau\operatorname{diag}(1,-1,-2,-3),\quad\tau\in\mathbb C.}
\]

Proof: DP_i(0)=diag(-i,1,2i,-1) has four distinct eigenvalues. The linear terms force B to commute with this diagonal matrix, so B is diagonal. The monomials a^2y and a^3z in the first coordinate and a^2t in the second force respectively lambda_y=-lambda_a, lambda_z=-2lambda_a, lambda_t=-3lambda_a. Every remaining monomial has the required weight, proving sufficiency. The executable checker independently solves the full sixteen-unknown linear system.

The original arithmetic quartet eigenvalues c+/-d+/-ig with d,g>0 are not proportional to (1,-1,-2,-3), in any ordering. Their trace fixes the putative scalar as real, whereas their eigenvalues are nonreal; for the centered quartet the trace instead forces that scalar to zero. Thus no constant coordinate conjugation makes this nonlinear map commute with the original linear quartet action.

There is an exact constructive action lift rather than an absent comparison:

\[
\boxed{X_B(x)=-\tfrac12\operatorname{adj}(DP_i(x))\,BP_i(x).}
\]

It is a polynomial vector field, because det DP_i=-2, and satisfies DP_i X_B=BP_i. It is the unique such vector field. Its correction to the original linear field is

\[
X_B-Bx=-\tfrac12\operatorname{adj}(DP_i)\,[BP_i-DP_iBx].
\]

This is a nonlinear field, not a linear endomorphism of the original cohomology.

### Its incompleteness is explicit for the original quartet

Let B=diag(lambda_1,lambda_2,lambda_3,lambda_4) be the retained quartet action in the corresponding labelled target coordinates. All lambda_j=c+/-d+/-ig. Put omega=3lambda_3-2lambda_4, which is nonzero since its imaginary coefficient is +/-g or +/-5g. The target orbit starting at (0,0,-3,1) is

\[
Y(t)=(0,0,-3e^{\lambda_3t},e^{\lambda_4t}).
\]

The cubic factor polynomial has discriminant

\[
27e^{2\lambda_4t}(4e^{\omega t}-1).
\]

At t_*=-log(4)/omega this vanishes simply, with a double root and a different simple root. The two colliding root sheets have

\[
F_{Y(t)}'(r(t))\asymp(t-t_*)^{1/2},\quad
 a(t)\asymp(t-t_*)^{-1/4}.
\]

The other source coordinates remain bounded or tend to zero by the explicit inverse; the retained source norm diverges at the same quarter-power rate. These are actual local solution branches of X_B whose target linear orbit remains finite. Thus the polynomial action lift is incomplete in finite complex time. Neither a source coordinate nor the conductor parameter is silently deleted at that endpoint.

### Metric action identity

For a fixed positive target H define G(x)=DP_i(x)^*HDP_i(x). Along real time for the underlying real vector field of X_B,

\[
\mathcal L_{X_B}G=DP_i^*(B^*H+HB)DP_i.
\]

The derivative of the metric and both DX_B terms are included by this Lie derivative. Subtracting 2cG yields the pullback of the original centered arithmetic defect B^*H+HB-2cH. Hence its generalized spectrum relative to G is exactly the target defect spectrum relative to H at every finite point. The nonlinear conditioning collapse does not produce a zero-defect polarization of the offcritical quartet.

## 7. Status and original receivers

The new calculations evaluate the full image and nonproper set, all root-multiplicity fibre counts, the two-chart completion and its homology, the signed monodromy group, the explicit two-chart inverse and both distinct metric-degeneration spectra, the entire linear infinitesimal symmetry space, and a polynomial lift of the original action together with an explicit finite-complex-time blowup. The original conductor still has its stated inverse. The original kernel determinant, proper-source target Schur minimum, and projected-current phases are not assigned values from these different nonlinear quantities. No RH conclusion is claimed.

The checker performs exact polynomial, rational, radical and exterior-minor identities. It does not evaluate actual zeta zeros or periods, and it is not a substitute for the analytic arguments about properness or continuation.

## Source record

- Incoming user-supplied Codex transcript: four Time labels; seven/eight factor-sign distinction; missing b=-i chart; escaping branch; source/version names.
- Original conductor WCF/LRC, retained in the supplied `Pasted text(20260917-221721).txt` and `Pasted markdown (2).md`: exact A_{D,s}, g, rho, moment and ordinary-transpose conventions.
- Terence Tao (2026, July 21), *A digestion of the Jacobian conjecture counterexample*, equations (2),(5)-(10): the linear-times-quadratic/resultant framework and its Fable attribution. The linear-times-cubic construction and all formulas here are derived explicitly; they are not quoted as Tao's formulas.
- GitHub repositories actually consulted: KokunoYumeto/erdos-straus-foundation and KokunoYumeto/zeta-function-research-reader. The root ES README identifies the 488-page reader but its zipped source was not successfully downloaded here. The latest zeta branch read in this turn is commit 2412f4aaa07c3fb19052cc0e537e93c2db9b0b1d; its README records the observed-class continuation, not the unpublished Fable coefficient list. No exhaustive reader audit or inspection of the unpublished Fable-conductor manuscript is claimed.

- Allen Hatcher (2002), *Algebraic Topology*, section 2.2: Mayer--Vietoris, used only in the explicitly stated two-chart homology calculation.
