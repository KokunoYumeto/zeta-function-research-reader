# The exact covering algebra, its original q-descent, and the finite-boundary section

Independent derivation OQ0–OQ10, 24 September 2026.

The finite-boundary restriction of the explicit rational-frequency algebra on the adelic covering space, with the original \(W_{\mathrm{alg}}\) and locally constant finite coefficients, has an equivariant global section. Its algebraic group-cochain connecting maps vanish. The original source \(q^r\) on the classical quotient is a frame-dependent invariant family of these covering functions, not one fixed-frequency function on the full covering space. OQ10 proves that exact descent map and its domain. The vanishing calculation is not asserted for all geometric sheaf cohomology or silently transferred to a boundary extension of that invariant family.

## OQ0. Original source, current definitions, and coordinates

Human source: Alain Connes and Caterina Consani, [*The Riemann–Roch strategy: Complex lift of the Scaling Site*, arXiv:1805.10501v1](https://arxiv.org/abs/1805.10501v1), original author thecurve_K.tex, §7.1, equations holom, holombis, holom1, holom2, Propositions frobarith and functionq, and Remark perfectoid. These passages were read directly. The source uses the algebraic first approximation
\[
W_{\mathrm{alg}}=\mathbb C[\mathbb R_{>0}^{\times}],
\quad [x][y]=[xy],\quad
\theta_\mu([x])=[x^\mu],\quad
\chi_\lambda([x])=x^\lambda
\quad(\mu,\lambda>0).
\tag{OQ0.1}
\]
Elements of \(W_{\mathrm{alg}}\) are finite complex linear combinations of the displayed formal basis elements. The source's Teichmüller notation \(\tau(x)\) is not the user's primitive \(Z_1/\tau\). We use only \([x]\) here.

The original moving function is
\[
q(X+iY)=[e^{-2\pi Y}]e^{2\pi iX},
\tag{OQ0.2}
\]
on the original classical orbit, with its rational powers and coefficient-character holomorphy. The source proposes the ring \(W[q^r]\), \(r\in\mathbb Q\), in Remark perfectoid; it does not identify that algebraic ring with every completion or all sheaf cohomology.

The current corpus and operation rules (private construction record; not included) and B1–B5 of [the source-operation proofs](../foundations/user_definitions_20260924/SOURCE_OPERATIONS_AND_PROOFS.md) were read for this derivation. The complete user passages USR-9ad1c0a2d09dba92, USR-f55d16feb948d8c2, and USR-6152e3bc6302258c were read in the preceding finite-boundary derivation and remain controlling. All arithmetic operations below belong to the already reconstructed arithmetic and original complex receiving algebra. No addition, parity, numerical metric, or coordinate is assigned to primitive \(\tau\).

Write \(F=\mathbb A_f\), \(E=F_X\times F_Y\), \(Z=F_X\times\{0\}\), and \(\Omega^+=\mathbb R_{X_\infty}\times\mathbb R_{>0,Y_\infty}\). The algebra will first be realized on \(E\times\Omega^+\). To give the action of all \(P(\mathbb Q)\), including \(a<0\), we then extend its same formulas to
\[
\Omega^\times=\mathbb R_{X_\infty}\times\mathbb R^\times_{Y_\infty}.
\tag{OQ0.3}
\]
Negative rational \(a\) exchanges the two halves; it is not claimed to preserve \(\Omega^+\). Positive rational \(a\) preserves each half. Both the two-sided extension and this restriction are retained.

## OQ1. The global additive character and the actual rational powers

Use the additive character
\[
\psi(X_f,X_\infty)=\psi_f(X_f)e^{2\pi iX_\infty}
\quad\text{on }\mathbb A_{\mathbb Q}/\mathbb Q.
\tag{OQ1.1}
\]
One explicit convention is
\[
\psi_f(X_f)=
\exp\!\left(-2\pi i\sum_p\{X_p\}_p\right),
\tag{OQ1.2}
\]
where \(\{X_p\}_p\) is the finite negative-power part of the \(p\)-adic expansion, chosen in \(\mathbb Z[1/p]\cap[0,1)\). All but finitely many terms vanish. The identity
\(\{x+y\}_p-\{x\}_p-\{y\}_p\in\mathbb Z\) proves the character law. Each local factor is trivial on \(\mathbb Z_p\); the restricted product makes \(\psi_f\) continuous and locally constant.

For \(b\in\mathbb Q\), the rational number
\[
b-\sum_p\{b\}_p
\]
is integral at every finite prime: at a fixed \(p\), its first subtraction leaves a \(p\)-adic integer and all other summands have denominator prime to \(p\). A rational integral at every prime is an integer. Therefore
\[
\psi_f(b)e^{2\pi ib}=1.
\tag{OQ1.3}
\]
This fixes the sign convention and proves triviality on diagonal rational translations. The same formula applies to \(rb\) for every rational \(r\).

For each \(r\in\mathbb Q\), define the actual \(W_{\mathrm{alg}}\)-valued function
\[
\boxed{
q_r(X_f,Y_f,X_\infty,Y_\infty)
=\psi_f(rX_f)e^{2\pi irX_\infty}
[\,e^{-2\pi rY_\infty}\,].}
\tag{OQ1.4}
\]
The finite coordinate \(Y_f\) remains present in the domain; this particular function is independent of it. Formula (OQ1.4) agrees with original \(q^r\) on the finite-unit frame \(Y_f\in\widehat{\mathbb Z}^{\,*}\), \(Y_\infty>0\). On the complete classical preimage the original pullback is instead \(q_{r/c}\), with the exact frame \(c\) proved in OQ10. There is no choice of an \(r\)-th root or logarithm of a complex phase: the global character defines the covering rational power directly. Multiplication gives
\[
q_rq_s=q_{r+s},\quad q_0=[1],\quad q_r^{-1}=q_{-r}.
\tag{OQ1.5}
\]
These use the original factors in (OQ1.4), not a completed or rescaled zeta function.

## OQ2. The exact algebra presentation and its injective realization

Let \(L_E=\operatorname{LC}(E,\mathbb C)\), with unrestricted global locally constant functions and pointwise multiplication. This is a unital function algebra; no compact-support condition is imposed. Let \(\mathbb C[\mathbb Q]\) have basis \(U_r\), \(r\in\mathbb Q\), with \(U_rU_s=U_{r+s}\). Define the algebraic tensor product
\[
A_E=L_E\otimes_{\mathbb C}W_{\mathrm{alg}}
\otimes_{\mathbb C}\mathbb C[\mathbb Q].
\tag{OQ2.1}
\]
Its elements have finite sums of the unique form
\[
F=\sum_{r\in S}\sum_{x\in S_r}f_{x,r}[x]U_r,
\tag{OQ2.2}
\]
where the finite sets \(S\subset\mathbb Q\) and \(S_r\subset\mathbb R_{>0}\) contain distinct indices, and \(f_{x,r}\in L_E\). The formal tensor presentation has the realized map
\[
\operatorname{ev}\bigl(f[x]U_r\bigr)
=f(X_f,Y_f)\psi_f(rX_f)e^{2\pi irX_\infty}
[\,x e^{-2\pi rY_\infty}\,].
\tag{OQ2.3}
\]
Its multiplicativity follows from the character law and (OQ1.5).

This map is injective. Suppose the image of (OQ2.2) vanishes. Apply every \(\chi_\lambda\), \(\lambda>0\), and fix a finite point \((X_f,Y_f)\) and \(Y_\infty>0\). The resulting identity for all \(X_\infty\in\mathbb R\) is
\[
\sum_{r\in S}
e^{2\pi irX_\infty}\psi_f(rX_f)e^{-2\pi r\lambda Y_\infty}
\left(\sum_{x\in S_r}f_{x,r}(X_f,Y_f)x^\lambda\right)=0.
\tag{OQ2.4}
\]
Distinct \(r\) give linearly independent exponential functions. For a direct proof, differentiate at any \(X_\infty\) in orders \(0,\ldots,|S|-1\); the matrix with entries \((2\pi ir)^j\) is a Vandermonde matrix with nonzero determinant. Hence every parenthesized sum vanishes for every \(\lambda>0\). For a fixed \(r\), evaluate at \(\lambda=1,\ldots,d\), where \(d=|S_r|\). The matrix \((x^\lambda)\) has determinant
\[
\left(\prod_{x\in S_r}x\right)
\prod_{x<x'\ \mathrm{in\ a\ fixed\ ordering}}(x'-x)\ne0.
\tag{OQ2.5}
\]
Thus every coefficient \(f_{x,r}(X_f,Y_f)\) is zero. The finite point was arbitrary, so all coefficients vanish. This also proves that the complete character family faithfully observes this exact moving-function algebra.

No dependence of \(f_{x,r}\) on \(X_\infty,Y_\infty\) was allowed in (OQ2.1); introducing such coefficients would change the presentation and require another independence argument. No completion or infinite Fourier sum is asserted here.

## OQ3. Original coefficient-character holomorphy

The scalar character realization is
\[
\chi_\lambda\operatorname{ev}(f[x]U_r)
=f(X_f,Y_f)\psi_f(rX_f)x^\lambda
e^{2\pi irX_\infty}e^{-2\pi r\lambda Y_\infty}.
\tag{OQ3.1}
\]
The original operator is
\[
L_\lambda
=Y_\infty(\lambda\partial_{X_\infty}+i\partial_{Y_\infty}).
\tag{OQ3.2}
\]
Its two terms on (OQ3.1) have coefficients \(2\pi ir\lambda Y_\infty\) and \(-2\pi ir\lambda Y_\infty\), so they cancel exactly:
\[
L_\lambda\chi_\lambda\operatorname{ev}(F)=0
\quad(F\in A_E,\ \lambda>0).
\tag{OQ3.3}
\]
This proves the extension is holomorphic in the exact source sense on every archimedean leaf. Locally constant finite coefficients introduce no archimedean derivatives. The same calculation holds on \(Y_\infty<0\); no growth or boundedness assertion on that half is required.

This proves inclusion in the corresponding algebraic holomorphic family. It does not assert that every holomorphic function in every proposed completed structure sheaf is a finite element of \(A_E\).

## OQ4. All rational affine pullbacks with the translation factors retained

Let \(g=(a,b)\in P(\mathbb Q)=\mathbb Q^\times\ltimes\mathbb Q\). Its source multiplication is
\[
(a,b)(a',b')=(aa',ab'+b).
\]
The action on both finite and infinite coordinates is
\[
\ell_g(X_f,Y_f,X_\infty,Y_\infty)
=(aX_f+b,aY_f,aX_\infty+b,aY_\infty).
\tag{OQ4.1}
\]
For all \(a\ne0\) this is an automorphism of \(E\times\Omega^\times\). Direct substitution gives
\[
q_r\circ\ell_g
=\psi_f(rb)e^{2\pi irb}\,q_{ar}
=q_{ar},
\tag{OQ4.2}
\]
where the first equality retains both rational-translation factors and the second uses (OQ1.3). The induced exact algebra automorphism is
\[
\boxed{\sigma_g(f[x]U_r)
=(f\circ L_f(a,b))[x]U_{ar},}
\qquad
L_f(a,b)(X_f,Y_f)=(aX_f+b,aY_f).
\tag{OQ4.3}
\]
Its realization is pullback by the original source action; no coordinate change or scalar factor is inserted.

Pullback is contravariant:
\[
\sigma_g\sigma_h=\sigma_{hg}.
\tag{OQ4.4}
\]
Indeed \(f\circ L_h\circ L_g=f\circ L_{hg}\), and the rational frequency becomes \(a_ha_gr\). Therefore these formulas give a right \(P(\mathbb Q)\)-action, or a left action \(g\cdot F=\sigma_{g^{-1}}F\). Both conventions are explicit. On the original upper half only the positive subgroup preserves the domain.

Holomorphy remains compatible: \(\partial_X+i\lambda^{-1}\partial_Y\) is rescaled by \(a\), while \(Y\) contributes \(a^{-1}\) when comparing pullbacks. In the full form the exact identity is
\[
L_\lambda P_\infty(a,b)=P_\infty(a,b)L_\lambda.
\tag{OQ4.5}
\]
This follows by substituting \(Y'=aY\) into the displayed operator, and holds for both signs of \(a\) on \(\Omega^\times\).

## OQ5. Right arithmetic Frobenius and its complete character action

Use the original
\[
\mathfrak F_\mu=\theta_\mu R(\mu^{-1}),\qquad\mu>0,
\]
where the geometric right action is \(Y_\infty\mapsto Y_\infty/\mu\), with \(X_\infty\) and finite coordinates fixed. Its exact effect is
\[
\mathfrak F_\mu q_r
=\psi_f(rX_f)e^{2\pi irX_\infty}
\theta_\mu([e^{-2\pi rY_\infty/\mu}])
=q_r.
\tag{OQ5.1}
\]
For constant coefficients, \(\theta_\mu[x]=[x^\mu]\). Thus
\[
\boxed{\mathfrak F_\mu(f[x]U_r)=f[x^\mu]U_r.}
\tag{OQ5.2}
\]
These are algebra automorphisms, with \(\mathfrak F_\mu\mathfrak F_\nu=\mathfrak F_{\mu\nu}\). They commute with all rational affine pullbacks: one changes \(x\) by the coefficient power, the other changes \(r\) and finite arguments, and the displayed operations commute.

At every character, the original formula remains
\[
\chi_\lambda\operatorname{ev}(\mathfrak F_\mu F)
=S_{\mu^{-1}}\chi_{\lambda\mu}\operatorname{ev}(F),
\quad
S_{\mu^{-1}}h(X_\infty,Y_\infty)
=h(X_\infty,Y_\infty/\mu).
\tag{OQ5.3}
\]
For a generator, the right side has coefficient \(x^{\lambda\mu}\) and exponential \(e^{-2\pi r\lambda\mu(Y_\infty/\mu)}\), proving equality with every factor retained. This is the exact source coefficient-character Frobenius, not an independently chosen action on a spectral quotient.

## OQ6. Boundary restriction and its global equivariant algebra section

Define the boundary algebra
\[
A_Z=\operatorname{LC}(F_X,\mathbb C)\otimes W_{\mathrm{alg}}
\otimes\mathbb C[\mathbb Q],
\tag{OQ6.1}
\]
with the same moving-\(q_r\) realization restricted to \(Y_f=0\). The proof in OQ2 applies verbatim with one finite coordinate, so this realization is injective.

Coefficient restriction and extension are
\[
R:A_E\longrightarrow A_Z,\qquad
R(f[x]U_r)=f(X_f,0)[x]U_r,
\]
\[
\boxed{S:A_Z\longrightarrow A_E,\qquad
S(k[x]U_r)=k(X_f)[x]U_r.}
\tag{OQ6.2}
\]
They are algebra homomorphisms and \(RS=I\). The extension uses no choice of a cutoff, Haar average or transverse measure. It is independent of \(Y_f\), exactly as specified.

Both maps commute with every \(\sigma_g\) in OQ4:
\[
R\sigma_g=\sigma_g^Z R,\qquad
\sigma_gS=S\sigma_g^Z,
\tag{OQ6.3}
\]
because \((aY_f)|_{Y_f=0}=0\), while \(k(aX_f+b)\) is still independent of \(Y_f\). Both commute with every arithmetic Frobenius in OQ5 because neither changes the coefficient parameter \(x\) or frequency \(r\).

Let \(I_Z^E=\{f\in L_E:f|_Z=0\}\). Injectivity of the algebra presentations gives
\[
\ker R=I_Z^E\otimes W_{\mathrm{alg}}\otimes\mathbb C[\mathbb Q].
\tag{OQ6.4}
\]
There is an exact, equivariantly split sequence of global algebras and their underlying complex vector spaces:
\[
0\longrightarrow\ker R
\longrightarrow A_E
\xrightarrow{R}A_Z
\longrightarrow0.
\tag{OQ6.5}
\]
Its additive decomposition is
\[
F=(F-SRF)+SRF,\qquad
A_E=\ker R\oplus S(A_Z).
\tag{OQ6.6}
\]
The projection \(SR\) is an equivariant idempotent. This is not an assertion that \(A_E\) is a direct product of rings: mixed products between the kernel ideal and section subalgebra need not vanish.

The unrestricted global locally constant coefficient domain matters. If one separately imposes compact support in \(Y_f\), the displayed \(S(k)\) is not compactly supported unless zero. The current unital algebra contains the original constant coefficient \(1\), so compact support was not its definition. No claim about a different Schwartz completion is inferred.

## OQ7. The global section is not a local splitting

Sheafify the same finite-sum presentations on open finite-transversal sets and archimedean open sets, retaining the \(W_{\mathrm{alg}}\) and \(q_r\) generators. Independence is still valid on an archimedean interval: differentiating the exponential identity at a point gives the same Vandermonde argument. Boundary restriction is consequently locally exact, and on the finite coefficient sheaf it is exactly
\[
0\longrightarrow j_!\mathscr L_U
\longrightarrow\mathscr L_E
\longrightarrow i_*\mathscr L_Z\longrightarrow0
\tag{OQ7.1}
\]
as proved in FB2, tensored with the displayed finite algebra generators.

There is no nonzero locally constant-coefficient section supported entirely on \(Z\). A nonzero coefficient persists on a finite open neighborhood, and the injective moving-\(q\) presentation prevents cancellation from hiding it off \(Z\). Therefore this sheaf restriction has no sheaf section, by the support argument of FB2.

The explicit global \(S\) in OQ6 does not contradict this. For example \(S(1)=1\). On an open finite-transversal set disjoint from \(Z\), the boundary sheaf restricts \(1\) to zero, while the restriction of \(S(1)\) is the nonzero constant function. Thus \(S\) fails the restriction-commutation requirement for a sheaf morphism. Its exact domain is the global module, and it is an equivariant global algebra map there.

This gives a proved map relating the local nonsplitting and global splitting. Neither is presented as a statement about the other category without its map.

## OQ8. The group-cochain connecting map is identically zero

Let \(G=P(\mathbb Q)\), considered as a discrete group, act from the left by \(g\cdot F=\sigma_{g^{-1}}F\). Alternatively use its positive subgroup on the upper half. The maps \(R,S\) are \(G\)-linear. All statements below also hold for the discrete direct product with the commuting arithmetic-Frobenius group \(\mathbb R_{>0}^{\times}\), using (OQ5.2). No topology on group cochains is silently added.

For a \(G\)-module \(M\), take inhomogeneous cochains
\[
C^n(G,M)=\{c:G^n\to M\},
\]
with differential
\[
(dc)(g_1,\ldots,g_{n+1})
=g_1c(g_2,\ldots,g_{n+1})
+\sum_{j=1}^{n}(-1)^j
c(g_1,\ldots,g_jg_{j+1},\ldots,g_{n+1})
+(-1)^{n+1}c(g_1,\ldots,g_n).
\tag{OQ8.1}
\]
For degree zero this means \(dm(g)=gm-m\). Define \(S_n\) by applying \(S\) to every value of a cochain. Since \(S\) commutes with the action and is linear, each term in (OQ8.1) gives
\[
dS_n=S_{n+1}d,\qquad R_nS_n=I.
\tag{OQ8.2}
\]
Hence (OQ6.5) gives a split short exact sequence of these entire cochain complexes.

For any boundary cocycle \(c\), its explicitly chosen lift is \(S_nc\). Its coboundary is
\[
d(S_nc)=S_{n+1}(dc)=0.
\]
The definition of the connecting map therefore gives
\[
\boxed{
\delta_G^n:H^n(G,A_Z)\longrightarrow H^{n+1}(G,\ker R),
\qquad \delta_G^n=0
\quad\text{for every }n\ge0.}
\tag{OQ8.3}
\]
This is an unconditional vanishing calculation for the exact covering algebra (OQ2.1), not a proposed vanishing premise. The decomposition of cochain complexes also gives
\[
H^n(G,A_E)
\cong H^n(G,\ker R)\oplus H^n(G,A_Z).
\tag{OQ8.4}
\]
The cohomology groups on the right are not claimed to vanish.

The map (OQ8.3) is not the distribution-complex connecting map \(\Delta_\lambda\) of FB6A.5. The latter uses a normal derivative between two supported-current complexes and has value \(\lambda h\) on constants. Here the exact sequence is the covering function-algebra boundary restriction with section (OQ6.2); its group connecting map is zero. The sequences, modules and comparison maps have all been displayed.

## OQ9. Entry into the finite-boundary distribution map and exact limits

The covering-algebra function restriction is linked directly to FB by finite-boundary insertion. At each coefficient character \(\lambda\), define
\[
\mathcal T_\lambda(F)
=\sum_{r,x}
f_{x,r}(X_f,0)\psi_f(rX_f)x^\lambda
e^{2\pi irX_\infty}e^{-2\pi r\lambda Y_\infty}
\,dX_f\otimes\delta_0(Y_f).
\tag{OQ9.1}
\]
This is a smooth archimedean family of finite-adele distributions: compactly supported finite tests make every Haar integral finite, and the sum over \(x,r\) is finite. It is defined character by character; no integral of arbitrary moving basis elements in the uncompleted group algebra is asserted.

It is precisely restriction \(R\), followed by the injective boundary-density insertion of FB1. Injectivity on boundary data follows from finite test-function separation and the Fourier–Vandermonde proof of OQ2. Thus its joint kernel for all \(\lambda>0\) is exactly \(\ker R\). The original global section provides the exact return
\[
R\,S=I
\]
before insertion into distributions. This links the actual covering function algebra to the preceding distribution enlargement, with every coefficient and character retained. Its source-classical-orbit comparison is OQ10.

For positive rational affine pullback the finite insertion acquires the full factor \(a=|a|_f^{-1}\) from FB4. The moving-\(q\) factors transform as proved in OQ4, so that factor is not cancelled by an omitted phase. For negative \(a\), the finite factor is \(|a|_\infty\); combining it with an archimedean derivative factor \(a^{-1}\) would leave \(\operatorname{sgn}(a)\). FB's compensated chain-map assertion was on the positive branch and is not extended across this sign without an explicit orientation coefficient.

The construction proves a boundary-lift vanishing on the exact algebraic group-cochain sequence (OQ6.5). It does not identify that sequence with Deligne's specialization sequence, nor identify its group cohomology with all geometric sheaf cohomology of the adelic quotient. The source \(q\)-descent comparison is proved next and retained rather than replaced by the covering algebra. Primitive \(Z_1/\tau\), all supported labels \(z_\lambda\), the original arithmetic and original zeta function remain unchanged.

## OQ10. Exact comparison with the original classical quotient

Source §5.4 identifies
\[
\Gamma_{\mathbb Q,\mathrm{cl}}
\cong G\times\mathbb R_{>0},\qquad
G=\mathbb A_{\mathbb Q}/\mathbb Q.
\tag{OQ10.1}
\]
Its selected representatives have \(Y_f\in\widehat{\mathbb Z}^{\,*}\) and positive real \(Y_\infty\). On the full preimage of this orbit, \(Y_f\) is a finite idele and \(Y_\infty\ne0\). There is a unique
\[
c=\operatorname{sgn}(Y_\infty)
\prod_p p^{v_p(Y_f)}\in\mathbb Q^\times,\qquad
u=Y_f/c\in\widehat{\mathbb Z}^{\,*},
\tag{OQ10.2}
\]
with \(y=Y_\infty/c>0\). The product is finite by the finite-idele condition. Existence is the displayed formula; uniqueness follows because a positive rational unit at every prime is one, with sign fixed by \(Y_\infty/c>0\).

The exact quotient-coordinate map is
\[
\kappa(X_f,Y_f,X_\infty,Y_\infty)
=\left(g=[(X_f,X_\infty)/c]\in G,\
y=Y_\infty/c\right).
\tag{OQ10.3}
\]
Right multiplication of \(Y_f\) by \(\widehat{\mathbb Z}^{\,*}\) changes \(u\), not \(c,g,y\). Under left \((a,b)\in P(\mathbb Q)\), the new frame is \(c'=ac\). The new \(y\) equals \(y\), and the new \(g\) is
\[
[(aX+b)/(ac)]=[X/c+b/(ac)]=[X/c],
\tag{OQ10.4}
\]
because \(b/(ac)\) is diagonal rational. Thus \(\kappa\) is invariant under the actual quotient actions. Every orbit has a unit-frame representative obtained by \(a=1/c\), followed by the finite unit action. Two such representatives have the same \(G\)-class exactly when their \(X\)'s differ by a rational translation. This proves the set-level quotient comparison and its fibres.

The original source function is
\[
q^r_{\mathrm{source}}(g,y)=\psi(rg)[e^{-2\pi ry}].
\]
Its exact pullback is
\[
\boxed{\kappa^*q^r_{\mathrm{source}}
=q_{r/c}(X_f,Y_f,X_\infty,Y_\infty).}
\tag{OQ10.5}
\]
Its invariance follows directly from the covering calculation:
\[
q_{r/(ac)}\circ\ell(a,b)=q_{r/c}.
\tag{OQ10.6}
\]
Thus fixedness under the actual left gauge action and the covering frequency change \(r\mapsto ar\) describe two explicitly related maps. No single action has been assigned contradictory rules.

The original finite \(q\)-algebra has a complete algebraic descent description. Put \(B=W_{\mathrm{alg}}\otimes\mathbb C[\mathbb Q]\), and take
\[
\mathfrak A_{\mathrm{frame}}=\prod_{c\in\mathbb Q^\times}B.
\tag{OQ10.7}
\]
Each component is a finite polynomial; there is no imposed common finite frequency set over all frames. Define \(\sigma_a^{\mathrm{freq}}([x]U_r)=[x]U_{ar}\), and
\[
(\sigma^{\mathrm{frame}}_{a,b}b)_c
=\sigma_a^{\mathrm{freq}}(b_{ac}).
\tag{OQ10.8}
\]
The translation phase is one by OQ1.3. The exact mutually inverse algebra maps are
\[
B\longrightarrow\mathfrak A_{\mathrm{frame}}^{P(\mathbb Q)},
\quad F\longmapsto
\bigl(\sigma_{1/c}^{\mathrm{freq}}F\bigr)_c,
\]
\[
\mathfrak A_{\mathrm{frame}}^{P(\mathbb Q)}
\longrightarrow B,\quad (b_c)_c\longmapsto b_1.
\tag{OQ10.9}
\]
Substitution into OQ10.8 proves the first family invariant. Conversely invariance with \(a=c\), evaluated at frame one, gives \(b_1=\sigma_c^{\mathrm{freq}}b_c\), hence \(b_c=\sigma_{1/c}^{\mathrm{freq}}b_1\). Both maps commute with arithmetic Frobenius on \(W_{\mathrm{alg}}\). This is the exact all-frame source descent.

For \(r\ne0\), the pulled-back invariant family OQ10.5 is not a single element of the globally finite-frequency algebra \(A_E\). Any element of \(A_E\) has one finite set \(S\) of archimedean frequencies. Equality with OQ10.5 on frame \(c\) requires \(r/c\in S\), by the exponential independence in OQ2. The frequencies \(r/c\) for \(c\in\mathbb Q^\times\) form an infinite set. The same argument applies to a nonconstant finite polynomial in source \(q\): one nonzero frequency has an infinite frame orbit, and distinct frequencies at a fixed frame cannot cancel. Constant \(W_{\mathrm{alg}}\) coefficients do lie in \(A_E\).

This is a specific domain statement with the exact extension OQ10.7–OQ10.9. It is not an obstruction to a full source sheaf or a larger completed algebra. In particular OQ8's connecting-map vanishing must not be transferred by identifying its \(A_E\) with the invariant frame-family algebra.

Topology must also be retained. The map \(Y_f\mapsto c\) is locally constant for the finite-idele topology, with sign fixed on each archimedean half. It is not locally constant in the subspace topology inherited from all \(\mathbb A_f\). For example \(c_n=1+n!\) tends to \(1\) in \(\mathbb A_f\): all terms are integral at every prime, and \(n!\) tends to zero at each fixed finite set of primes. Each \(c_n\) is a finite idele. With \(X=0,Y_\infty=1\), OQ10.3 gives \(y_n=1/(1+n!)\), which does not tend to the value \(y=1\) at \(Y_f=1\). Thus \(\kappa\), with target \(G\times\mathbb R_{>0}\), is not continuous for that ambient subspace topology. No ambient continuous extension across \(Y_f=0\) follows from the set-level quotient formula.

The source-compatible outcome consists of two linked exact constructions. The original invariant \(W[q^r]\) algebra has the all-frame realization OQ10.9. The separate fixed-frequency covering algebra has the global equivariant boundary section OQ6.2. Their common unit-frame restriction is explicit. The section of the second is not an asserted boundary extension of the first.

The positive-branch comparison was independently derived in [MOVING_Q_ZETA_COMPARISON.md, MQ8.5–MQ8.8](MOVING_Q_ZETA_COMPARISON.md). That complete MQ8 passage was read and compared with OQ10; the additional full-sign frame, invariant product-algebra presentation, and finite-frequency exclusion are proved here. The topology counterexample was supplied by the coordinating calculation and its convergence and coordinate values are verified above.

## Source-reading and provenance

The original author thecurve_K.tex has SHA256 da52001209424c19fb223905804a9eed1147c72331cf881aa0352bc759976061. Read directly for this calculation: §7.1 from its heading through Remark perfectoid; and §5.4 completely, including Jdefn1, classorb1, proetcov and Remark additivestruct. The original affine action and global character convention were read in the preceding FB derivation at §5.1–5.2, especially Lemma adelicomp and equation actionpq, and were recalculated in OQ1 and OQ4. This is bounded source coverage, not a whole-paper claim.

The current operation rules and B1–B5 were reread before constructing (OQ2.1). The user-originating programme seeks full global reconstruction and vanishing of the appropriate lifting map; OQ6 and OQ8 provide the displayed exact global section and its actual vanishing result. Connes and Consani retain credit for \(W\), the coefficient characters, moving \(q^r\), and arithmetic Frobenius. The finite-transversal extension, injectivity, exact global section, and cochain calculation are derived in this note. No historical novelty is asserted for a split-module connecting map being zero.
