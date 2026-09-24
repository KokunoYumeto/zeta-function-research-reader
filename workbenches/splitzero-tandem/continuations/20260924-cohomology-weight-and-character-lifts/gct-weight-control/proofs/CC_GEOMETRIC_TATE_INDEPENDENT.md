# The CC chart realization, its Tate class, and its ramified specialization

Independent derivation, 24 September 2026. Proof locators CGT0–CGT12.

## CGT0. Objects, prerequisites, and source coverage

The supporting datum remains the user's \(\tau\langle Z_1;\text{no }Z_2\rangle\). No addition on \(\tau\) is used. The ring \(\mathbf Z\) in this calculation is the already recovered arithmetic coefficient ring. It is not defined by selecting the primes \(2,3\), or by a finite part of the timing history. Every ring operation, scheme, cohomology group, and quotient below is downstream of that reconstruction.

The specific object evaluated here is Connes–Consani's supplied chart construction. The Gaussian coefficient ring appearing in its evaluation is a receiver for those charts. It is not an alternative prime spectrum offered as a counterexample to the user's global reconstruction. In particular, this calculation makes no identification of \(\tau\) with a Gaussian integer, a zero, a unit, or a cohomology class.

The instruction CORPUS_AND_OPERATION_RULE.md (private construction record; not included) was read before the calculation. The root task additionally supplied the relevant correction: the user has already rejected replacing the reconstruction by a Gaussian-integer counterexample. That rejected use is not made here.

Original-author source actually read: Alain Connes and Caterina Consani, [The Absolute Twistor Line and the Geometry of the compactified Spec Z](https://arxiv.org/html/2609.00299v1), supplied author file CC.tex, especially lines 430–460, 526–542, 576–602, 617–758 and 765–851. These are the signed base, chart and overlap presentations, field-valued point comparison, and involution. SHA-256 of that file is 57a10dcef5cd758e6b2f1c54b1c0a11b0fb093638f74fb1be515ec3bc7080ba4.

The Stacks Project original TeX was read locally at commit d3e53496bbd24b82a1d87ce513c913923ebbebb2:

- etale-cohomology.tex, lines 11071–11244: Kummer calculation and the pullback degree formula, [03RQ](https://stacks.math.columbia.edu/tag/03RQ), [0AMB](https://stacks.math.columbia.edu/tag/0AMB).
- The same file, lines 6547–6570: invariance under a nilpotent closed immersion, [03SI](https://stacks.math.columbia.edu/tag/03SI).
- The same file, lines 18610–18704: proper base change and its proof, [095T](https://stacks.math.columbia.edu/tag/095T).
- The same file, lines 19523–19585: proper specialization and the smooth specialization consequence, [0GKD](https://stacks.math.columbia.edu/tag/0GKD).
- trace.tex, lines 196–354: arithmetic/geometric Frobenius convention and the degree computation on the projective line.
- more-etale.tex, lines 4278–4362: the smooth proper curve consequence and its references.

This is reading coverage of the stated passages, not a claim to have reread the entire Stacks Project or CC paper. The two source hashes are etale-cohomology.tex: 015f27b1d332cc096b1f323daeeb855b299bb5a08f43c05131f196d4c183e7bf; trace.tex: 642cb0f2314fc73bef27542c79f55af87dcc0b0bf87d7cecf29b9b61860e4bfc.

## CGT1. The ring realization and its exact twisted overlap

For a commutative coefficient ring \(R\), define
\[
A_R=R[J]/(J^2+1),\quad
A_+=R[J_+]/(J_+^2+1)[T],\quad
A_-=R[J_-]/(J_-^2+1)[U],
\]
\[
A_\circ=R[J]/(J^2+1)[T,T^{-1}].
\tag{CGT1.1}
\]
The overlap homomorphisms, with all signs retained, are
\[
\rho_+(J_+)=J,\quad \rho_+(T)=T,\qquad
\rho_-(J_-)=-J,\quad \rho_-(U)=T^{-1}.
\tag{CGT1.2}
\]
These are precisely the ring presentations representing the signed chart evaluations: for every commutative \(R\)-algebra \(D\), a homomorphism \(A_+\to D\) is uniquely a pair \((t,j_+)\) with \(j_+^2=-1\); the other chart and overlap have the same universal property, with \(t\) invertible on the overlap. The signed source element \(\epsilon\) is sent to \(-1_D\). Thus this realization is specified by a universal mapping property, not merely by agreement of geometric points over fields.

Let \(X_R\) be the scheme obtained by gluing these affine spectra along their displayed localizations. Define the global coefficient \(J\) to be \(J_+\) on the plus chart and \(-J_-\) on the minus chart. The two definitions have the same restriction, because \(\rho_-(-J_-)=J\).

The standard two charts of \(\mathbf P^1_{A_R}\), with \(T=X/Y\) and \(U=Y/X\), now give isomorphisms to the two charts of \(X_R\): their coefficient maps are respectively \(J\mapsto J_+\) and \(J\mapsto-J_-\), and their coordinate maps are \(T\mapsto T\), \(U\mapsto U\). On the overlap both become the same homomorphism \(A_R[T,T^{-1}]\to A_\circ\). The inverse homomorphisms send \(J_+\mapsto J\), \(J_-\mapsto-J\). Both composites fix every generator. The gluing universal property therefore proves
\[
\boxed{X_R\simeq\mathbf P^1_{A_R}}
\tag{CGT1.3}
\]
with the original twisted chart identifications explicitly retained. This does not replace \(J_-\) by \(J_+\): it records their comparison \(J_-=-J\) in the global coefficient chart.

For \(R=\mathbf Z\), write \(A=\mathbf Z[J]/(J^2+1)\). The evaluation \(J\mapsto i\) is a ring isomorphism \(A\to\mathbf Z[i]\), with inverse \(a+bi\mapsto a+bJ\). Uniqueness follows from the monic quadratic relation, which gives the free \(\mathbf Z\)-basis \(1,J\).

## CGT2. The involution on the entire scheme

Let \(c:A_R\to A_R\) be \(c(J)=-J\), \(c(r)=r\) for \(r\in R\). Under CGT1 the supplied CC involution is
\[
\alpha([X:Y],J)=([-Y:X],-J),
\qquad
\alpha^*(T)=-T^{-1},\quad \alpha^*(J)=-J.
\tag{CGT2.1}
\]
This notation describes the semilinear scheme morphism over \(R\); it does not assert that \(\alpha\) is over \(A_R\).

Its plus-to-minus chart map is
\[
A_-\longrightarrow A_+,\qquad U\longmapsto-T,\quad J_-\longmapsto J_+,
\tag{CGT2.2}
\]
and its minus-to-plus map is
\[
A_+\longrightarrow A_-,\qquad T\longmapsto-U,\quad J_+\longmapsto J_-.
\tag{CGT2.3}
\]
For example, restricting (CGT2.2) sends \(J_-\) to \(J\), while applying the generic formula to \(\rho_-(J_-)=-J\) also gives \(J\). The coordinate comparison sends \(U\) to \(-T\) on both routes. The other comparison is identical on its stated generators. Thus these are morphisms of the glued scheme.

Applying (CGT2.1) twice gives \([-X:-Y]=[X:Y]\) and \(J\mapsto J\). Hence \(\alpha^2=1\). The projective transformation has degree \(1\), although its affine formula contains a minus sign and inversion. This degree will determine its action on \(H^2\).

## CGT3. All finite-field coefficient fibres, including the nonreduced fibre

Let \(q=p^f\), \(k=\mathbf F_q\), and \(\bar k\) an algebraic closure.

For \(p\ne2\), choose once a root \(j\in\bar k\) of \(J^2+1\). The Chinese remainder map is
\[
A_{\bar k}\longrightarrow\bar k\oplus\bar k,\qquad
F(J)\longmapsto(F(j),F(-j)).
\tag{CGT3.1}
\]
It is an isomorphism because \(2j\ne0\). Its inverse on a pair \((a,b)\) is
\[
\frac{a+b}{2}+\frac{a-b}{2j}J.
\tag{CGT3.2}
\]
Both branches remain labeled by their actual coefficient values \(j,-j\). Consequently
\[
X_{\bar k}=\mathbf P^1_{\bar k,+}\sqcup\mathbf P^1_{\bar k,-}.
\tag{CGT3.3}
\]
The involution interchanges these components and applies \([X:Y]\mapsto[-Y:X]\) on their coordinates.

For \(p=2\), set \(\nu=J-1\). Then
\[
A_{\bar k}=\bar k[\nu]/(\nu^2),\qquad
X_{\bar k}=\mathbf P^1_{\bar k[\nu]/(\nu^2)}.
\tag{CGT3.4}
\]
This is a nonreduced scheme. Its closed immersion
\[
\iota:\mathbf P^1_{\bar k}\hookrightarrow X_{\bar k}
\tag{CGT3.5}
\]
is defined by the nonzero square-zero ideal \((\nu)\). The scheme and its reduction are not identified in this calculation. Instead, topological invariance gives the actual equivalence of étale topoi \(\iota^{-1}\), and hence the cohomology isomorphisms \(\iota^*\). The nilpotent coefficient \(\nu\) is retained in (CGT3.4), even though the constant étale-cohomology receiver does not distinguish it.

Here \(\alpha^*(J)=-J=J\), so \(\alpha^*(\nu)=\nu\). The coordinate formula becomes \(T\mapsto T^{-1}\); it is still the reduction of the full formula \(-T^{-1}\).

## CGT4. Cohomology and the geometric origin of the Tate factor

Fix a coefficient prime \(\ell\ne p\), put \(E=\mathbf Q_\ell\), and first work with coefficients \(\mathbf Z/\ell^r\mathbf Z\). On \(\mathbf P^1_{\bar k}\), the Kummer sequence gives
\[
H^1(\mathbf P^1_{\bar k},\mu_{\ell^r})
=\operatorname{Pic}(\mathbf P^1_{\bar k})[\ell^r]=0,
\]
\[
H^2(\mathbf P^1_{\bar k},\mu_{\ell^r})
=\operatorname{Pic}(\mathbf P^1_{\bar k})/
\ell^r\operatorname{Pic}(\mathbf P^1_{\bar k})
=\mathbf Z/\ell^r\mathbf Z.
\tag{CGT4.1}
\]
Here \(\operatorname{Pic}(\mathbf P^1_{\bar k})=\mathbf Z[\mathcal O(1)]\). The other possible terms vanish because \(\bar k^\times\) is \(\ell^r\)-divisible and the higher \(\mathbf G_m\)-cohomology of this smooth curve vanishes, as in the cited proof of 03RQ. The same source gives vanishing in degrees above \(2\). Passing through the compatible surjective coefficient transition maps, then tensoring with \(E\), yields
\[
H^0=E,\qquad H^1=0,\qquad H^2=E(-1).
\tag{CGT4.2}
\]
The isomorphism \(E\to H^2(\mathbf P^1_{\bar k},E(1))\) sends \(1\) to \(c_1(\mathcal O(1))\), not to an arbitrarily chosen eigenvector.

Here is the actual geometric multiplication factor. For every integer \(n\ge1\), the morphism
\[
b_n:\mathbf P^1_{\bar k}\to\mathbf P^1_{\bar k},
\qquad [X:Y]\longmapsto[X^n:Y^n]
\tag{CGT4.3}
\]
has
\[
b_n^*\mathcal O(1)=\mathcal O(n),\quad
b_n^*c_1(\mathcal O(1))=n\,c_1(\mathcal O(1)).
\tag{CGT4.4}
\]
The first equality follows by pulling back the homogeneous transition function \(X/Y\), which becomes \((X/Y)^n\); the second follows from the tensor-product additivity and functoriality of the Kummer boundary. Thus the factor \(n\) comes from a morphism and its divisor pullback.

For \(n=q\) the coordinate morphism is the relative \(q\)-power Frobenius of the projective line. With geometric Frobenius defined as inverse arithmetic Galois Frobenius, its action on untwisted \(H^2\) is multiplication by \(q\). Equivalently, arithmetic Frobenius acts by \(q\) on \(\mathbf Z_\ell(1)\), geometric Frobenius by \(q^{-1}\), and the class \(c_1(\mathcal O(1))\) is Galois-fixed in \(H^2(E(1))\). Untwisting therefore gives \(q\), with no rescaling.

Applying \(\alpha\)'s coordinate morphism to the same transition function gives degree \(1\), so its pullback on \(H^2\) is \(+1\). The minus sign in \(-T^{-1}\) is not a negative cohomological degree.

## CGT5. Full Frobenius matrices and all repetition traces

For odd \(p\), in the ordered component basis \((+, -)\), let
\[
P_q=\begin{cases}
\begin{pmatrix}1&0\\0&1\end{pmatrix},&q\equiv1\pmod4,\\[2mm]
\begin{pmatrix}0&1\\1&0\end{pmatrix},&q\equiv3\pmod4.
\end{cases}
\tag{CGT5.1}
\]
Indeed arithmetic Frobenius sends \(j\) to \(j^q\); since \(j^2=-1\), this is \(j\) or \(-j\) according to \(q\bmod4\). The inverse permutation for geometric Frobenius is the same, because the permutation has order at most two. Combining this permutation with CGT4 gives
\[
H^0(X_{\bar k},E)=E^2,\quad F_q=P_q;\qquad
H^1=0;\qquad
H^2=E(-1)^2,\quad F_q=qP_q.
\tag{CGT5.2}
\]
Thus the eigenvalues are \(1,1\) and \(q,q\) when \(q\equiv1\pmod4\), and \(1,-1\) and \(q,-q\) when \(q\equiv3\pmod4\).

The matrix description is valid already at integral coefficient level. The decomposition into plus and minus eigenlines uses \(1/2\), so it is asserted here over \(E\), including \(E=\mathbf Q_2\), not indiscriminately over \(\mathbf Z_2\).

For \(p=2\), the pullback along (CGT3.5) and CGT4 give
\[
H^0(X_{\bar k},E)=E,\quad F_q=1;\qquad
H^1=0;\qquad
H^2(X_{\bar k},E)=E(-1),\quad F_q=q.
\tag{CGT5.3}
\]
The \(q\)-power map sends \(\nu\) to \(0\), whereas \(\alpha\) fixes \(\nu\). They are different scheme maps. They nevertheless give the stated cohomology actions through the explicitly proved reduction map.

For every repetition number \(m\ge1\), the full alternating Frobenius trace is
\[
\operatorname{Tr}(F_q^m\mid H^\bullet)
=\begin{cases}
(1+q^m)\operatorname{Tr}(P_q^m),&p\ne2,\\
1+q^m,&p=2.
\end{cases}
\tag{CGT5.4}
\]
In the nonsplit odd case this is zero for odd \(m\) and \(2(1+q^m)\) for even \(m\). In the split odd case it is \(2(1+q^m)\) for every \(m\). These agree directly with the number of \(\mathbf F_{q^m}\)-points: the projective coordinate gives \(q^m+1\) for each available root of \(J^2+1\). No repetition or coefficient branch is dropped.

The cohomological weights here are \(0\) in degree \(0\) and \(2\) in degree \(2\), since the complex absolute values of the eigenvalues are \(1=q^{0/2}\) and \(q=q^{2/2}\). There is no degree-one cohomology in this particular scheme.

## CGT6. The signed absolute powers and the prime \(2\)

The supplied signed absolute power map has \(T\mapsto T^n\), \(J\mapsto J^n\), and must preserve \(\epsilon=-1\). It extends over the ring realization for odd \(n\), because
\[
(J^n)^2=(-1)^n=-1.
\tag{CGT6.1}
\]
The minus-chart compatibility is
\[
(-J)^n=-J^n.
\tag{CGT6.2}
\]
Its coordinate degree is \(n\), and its coefficient action is identity for \(n\equiv1\pmod4\) and conjugation for \(n\equiv3\pmod4\). Hence its action on the two geometric component cohomologies is \(P_n\) in degree \(0\) and \(nP_n\) in degree \(2\). It commutes with \(\alpha\): on \(T\), both pullback composites give \(-T^{-n}\); on \(J\), both give \(-J^n\).

For even \(n\), \(J\mapsto J^n\) is not a homomorphism of this global signed presentation over \(\mathbf Z\), since its squared image is \(1\), not \(-1\). The morphism \(b_n\) from CGT4 does exist with the coefficient \(J\) fixed, but it is not that signed source power map. In characteristic \(2\), the Frobenius of the fibre also exists, including its action \(\nu\mapsto0\). These maps have different stated domains and coefficient actions. The cohomology at \(2\) in CGT5 is obtained from the fibre Frobenius, not by inventing an even signed source endomorphism.

## CGT7. The actual wild specialization at \(2\)

Let
\[
S=\operatorname{Spec}\mathbf Z_2,\quad
S'=\operatorname{Spec}\mathbf Z_2[i],\quad
Y=\mathbf P^1_{S'},\quad g:Y\to S.
\tag{CGT7.1}
\]
The polynomial of \(\pi=1-i\) is
\[
\pi^2-2\pi+2=0.
\tag{CGT7.2}
\]
It is Eisenstein at \(2\), so \(\mathbf Q_2(i)/\mathbf Q_2\) is a totally ramified quadratic extension, with uniformizer \(\pi\), residue field \(\mathbf F_2\), and
\[
2=i\pi^2,\qquad c(\pi)=1+i=i\pi.
\tag{CGT7.3}
\]
It is wild because its ramification degree is the residue characteristic. The quotient of inertia acting on its two embeddings is the order-two group generated by \(i\mapsto-i\). This action is retained.

Let \(\ell\ne2\). Over a geometric generic point, \(Y_{\bar\eta}\) is the disjoint union of two projective lines, indexed by the embeddings \(i\mapsto i\) and \(i\mapsto-i\). Over a geometric special point its coefficient ring is \(\overline{\mathbf F}_2[\nu]/(\nu^2)\). Hence
\[
H^0(Y_{\bar s},E)=E,\quad H^2(Y_{\bar s},E)=E(-1),
\]
\[
H^0(Y_{\bar\eta},E)=E^2,\quad
H^2(Y_{\bar\eta},E)=E(-1)^2.
\tag{CGT7.4}
\]
All degree-one groups vanish.

The actual specialization maps are
\[
\operatorname{sp}_0:a\longmapsto(a,a),\qquad
\operatorname{sp}_2:a\,h_s\longmapsto(a\,h_+,a\,h_-),
\tag{CGT7.5}
\]
where the notation \(h=c_1(\mathcal O(1))\) is interpreted in the twisted group \(H^2(E(1))\) before untwisting. To prove these formulas, use the global unit section for degree zero and the global line bundle \(\mathcal O_Y(1)\) for degree two. Their restrictions to each geometric generic component are respectively the unit and the degree-one hyperplane class. These generate all groups by CGT4. Proper base change defines the special-fibre stalk, and smooth proper specialization for \(Y\to S'\) proves that the restriction of each generator to each generic branch is an isomorphism. This proves (CGT7.5), including its coefficient \(1\) on each branch.

For \(\ell\ne2\), inertia acts trivially on \(\mathbf Q_\ell(1)\): every \(\ell^r\)-th root of unity belongs to an unramified extension of \(\mathbf Q_2\), by lifting the simple roots in the algebraic closure of the residue field. It therefore acts on (CGT7.4) solely by the wild branch swap
\[
P=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\tag{CGT7.6}
\]
The invariant subspaces are exactly the diagonals. Consequently the actual maps
\[
\boxed{\operatorname{sp}_j:
H^j(Y_{\bar s},E)\ \xrightarrow{\ \sim\ }\
H^j(Y_{\bar\eta},E)^I,\qquad j=0,1,2}
\tag{CGT7.7}
\]
are isomorphisms. In degree \(1\) both sides are zero. Their cokernels, the obstruction spaces for this specified specialization problem, are zero.

The anti-diagonal generic class \((a,-a)\) is not discarded. It is the sign representation of the wild inertia quotient and is not invariant unless \(a=0\). Over \(E\) it is the kernel of the sum map, complementary to the image in (CGT7.5). The factor \(2\) in the sum of a diagonal vector, \((a,a)\mapsto2a\), is retained. Thus the disappearance of a second geometric special component is represented by the nonreduced coefficient fibre and this explicit ramified representation, not by silently merging two generic basis vectors.

Residual geometric Frobenius acts on the invariant degree-zero line by \(1\) and on the invariant degree-two line by \(2\). Any two lifts of residual Frobenius differ by inertia, so these values are independent of the chosen lift. On the full generic two-component space the branch permutation of a lift may differ; we make no choice-independent assertion about that extra permutation.

This is a calculation in a mixed-characteristic model smooth over \(S'\), not an assertion that \(g:Y\to S\) is smooth. Indeed the nonreduced special fibre shows that \(g\) is not smooth. The equal-characteristic hypotheses of Deligne's §3.6 are not silently substituted for the actual hypotheses here.

## CGT8. The full proper pushforward before taking invariants

Fix \(\ell\) and put
\[
B=\operatorname{Spec}\mathbf Z[1/\ell],\quad
C=\operatorname{Spec}\bigl(\mathbf Z[1/\ell,J]/(J^2+1)\bigr),
\quad f:C\to B,\quad p:X=\mathbf P^1_C\to C,\quad g=f\circ p.
\tag{CGT8.1}
\]
The unit and hyperplane class define a map in the étale derived category
\[
\mathbf Q_{\ell,C}\oplus
\mathbf Q_{\ell,C}(-1)[-2]\longrightarrow Rp_*\mathbf Q_{\ell,X}.
\tag{CGT8.2}
\]
The first summand is the adjunction unit. The second is the morphism represented by \(c_1(\mathcal O_X(1))\in H^2(X,\mathbf Q_\ell(1))\), with the twist and cohomological shift explicitly displayed.

At every geometric point of \(C\), proper base change identifies (CGT8.2) with the unit and hyperplane maps of CGT4. They are isomorphisms in degrees \(0\) and \(2\), and both sides have no other cohomology. A map of complexes inducing an isomorphism on all cohomology stalks is a quasi-isomorphism. Therefore (CGT8.2) is an isomorphism. One may first carry out the same construction with \(\mathbf Z/\ell^r\) coefficients; the computed groups have surjective transitions, so passage to \(\mathbf Z_\ell\) and then \(\mathbf Q_\ell\) preserves these computations.

The finite morphism \(f\) has no higher direct images on these coefficients. Proper base change computes a stalk as cohomology of a finite geometric fibre; each such fibre is a disjoint union of spectra of Artinian local algebras over an algebraically closed field. Reduction and étale topological invariance identify its cohomology with that of a finite discrete set, which has no positive cohomology. This proves the vanishing by stalks, including the ramified fibre.

Applying \(Rf_*=f_*\) to (CGT8.2) yields the full comparison
\[
\boxed{Rg_*\mathbf Q_\ell
\simeq f_*\mathbf Q_\ell\ \oplus\
f_*\mathbf Q_\ell(-1)[-2].}
\tag{CGT8.3}
\]
No branch has been removed in (CGT8.3). The sheaf \(f_*\mathbf Q_\ell\) has geometric stalk dimension \(2\) away from \(2\), and dimension \(1\) at \(2\) when \(2\in B\); its specialization is the diagonal map just calculated.

The involution acts by coefficient conjugation on the first summand. It has the same coefficient action on the second, because the projective part pulls back \(\mathcal O(1)\) to \(\mathcal O(1)\). Thus the decomposition is \(\alpha\)-equivariant.

## CGT9. The invariant sheaf, with the ramified stalk retained

Define the unit map
\[
d:\mathbf Q_{\ell,B}\longrightarrow f_*\mathbf Q_{\ell,C}.
\tag{CGT9.1}
\]
At an odd geometric residue characteristic its stalk is \(a\mapsto(a,a)\). Conjugation interchanges the two entries, so its image is exactly the invariant subspace. At residue characteristic \(2\), its stalk is \(a\mapsto a\) on the single-point étale receiver of the nonreduced ring. Conjugation acts trivially there. The same two-entry calculation applies at a geometric characteristic-zero point.

It follows on every geometric stalk that
\[
\boxed{\mathbf Q_{\ell,B}\xrightarrow{\sim}
(f_*\mathbf Q_{\ell,C})^\alpha.}
\tag{CGT9.2}
\]
This is a sheaf isomorphism, not solely a fibrewise dimension comparison, because it is induced by the single map (CGT9.1).

Since \(2\) is invertible in \(\mathbf Q_\ell\), the projector
\[
e_+=(1+\alpha)/2
\tag{CGT9.3}
\]
is defined on rational \(\ell\)-adic sheaves and makes taking invariants exact. This includes \(\ell=2\) with rational coefficients; it is not a statement about exact invariants of integral \(2\)-adic modules. Apply the projector to the equivariant decomposition (CGT8.3). The result is the proved derived comparison
\[
\boxed{(Rg_*\mathbf Q_\ell)^\alpha
\simeq\mathbf Q_{\ell,B}\oplus
\mathbf Q_{\ell,B}(-1)[-2].}
\tag{CGT9.4}
\]
The complementary sheaf \((f_*\mathbf Q_\ell)^-\) is retained as the kernel of \(1+\alpha\). Its geometric stalk is the anti-diagonal at odd primes and at the generic point, and zero at \(2\). Thus (CGT9.4) records a projection with an explicitly described complementary receiver. It does not identify the original scheme or the full pushforward with the invariant part.

## CGT10. The resulting full Euler products in their convergence domain

For every prime \(p\ne\ell\) and every \(m\ge1\), (CGT9.4) gives the invariant alternating trace
\[
1+p^m.
\tag{CGT10.1}
\]
With a formal variable \(u\), its local factor is
\[
\exp\left(\sum_{m\ge1}\frac{1+p^m}{m}u^m\right)
=\frac1{(1-u)(1-pu)}.
\tag{CGT10.2}
\]
This retains both cohomological degrees and every repetition. The equality follows from the convergent power series for \(-\log(1-z)\) near zero, or as a formal power-series identity with constant term \(1\).

To include \(p=\ell\), compute that fibre with a different coefficient prime \(\ell'\ne p\). CGT4–CGT5 give the same integer traces \(1+p^m\); hence the local polynomial is independent of this choice. This procedure retains the entire prime spectrum and does not place a missing-prime factor into an unspecified unit.

On the explicit domain \(\Re(s)>2\), all prime-repetition series are absolutely convergent, and \(u=p^{-s}\) gives
\[
\begin{aligned}
\prod_p\frac1{(1-p^{-s})(1-p^{\,1-s})}
&=\exp\left(\sum_p\sum_{m\ge1}
\frac{p^{-ms}+p^{m(1-s)}}m\right)\\
&=\left(\sum_{a\ge1}a^{-s}\right)
\left(\sum_{b\ge1}b^{\,1-s}\right)\\
&=\boxed{\zeta(s)\zeta(s-1)}.
\end{aligned}
\tag{CGT10.3}
\]
The second equality is the Euler product using the already recovered arithmetic and unique factorization; it is not a construction of arithmetic from a finite prime selection. The unit terms \(a=b=1\) and the factor at \(2\) are explicit. These are the original zeta functions; no completion, Gamma multiplier, heat rescaling, or endpoint cancellation has been introduced.

For comparison, the full unprojected object of CGT8 has local factors
\[
\begin{cases}
\bigl((1-p^{-s})^2(1-p^{1-s})^2\bigr)^{-1},&p\equiv1\pmod4,\\
\bigl((1-p^{-2s})(1-p^{2(1-s)})\bigr)^{-1},&p\equiv3\pmod4,\\
\bigl((1-2^{-s})(1-2^{1-s})\bigr)^{-1},&p=2.
\end{cases}
\tag{CGT10.4}
\]
These follow directly by taking determinants of the matrices in CGT5. They are recorded alongside the invariant factors so that projection has a visible effect on the Euler product.

## CGT11. The exact lifting result and the boundary of this calculation

The specialization problem solved here is (CGT7.7): lift every inertia-invariant geometric generic class of the realized CC projective line from its geometric special fibre at \(2\). The maps are written in (CGT7.5), their images are computed in (CGT7.6), and their cokernels are zero. This proof retains the wild branch permutation and the nilpotent coefficient fibre.

The Tate factor in CGT4–CGT10 is obtained from the actual class \(c_1(\mathcal O(1))\), its Kummer boundary, and pullback of the degree-\(q\) morphism. No character is assigned to an arbitrary analytic vector or to \(\tau\).

There is no proved identification here of the original-zeta zero-jet sheaf, the full timing reconstruction, or the user's desired lifting map with this \(Rg_*\mathbf Q_\ell\). In particular, the weight-\(0\) and weight-\(2\) summands and the vanishing \(H^1\) of this concrete projective line are exactly what the calculation gives. Calling that a weight-\(1\) zero space or a proof of RH would add a conclusion not established by any map in this file.

The comparison is nevertheless explicit: it evaluates the supplied signed CC charts, retains their involution, derives a geometric Tate factor, proves the ramified specialization lift, and recovers the full original product \(\zeta(s)\zeta(s-1)\) after the specified invariant projection. The factors and the complementary branch sheaf remain available for any further comparison.

## CGT12. Diagram of the actual maps

The following diagram records the maps of CGT7. The left column is the geometric special fibre's cohomology; the middle column is the full geometric generic cohomology; the right column records its actual inertia invariants. In degree \(2\), the displayed \(E(-1)\) is produced by CGT4.

\[
\begin{array}{c|ccc}
\text{degree}&H^j(Y_{\bar s},E)&H^j(Y_{\bar\eta},E)&
H^j(Y_{\bar\eta},E)^I\\ \hline
0&E\xrightarrow{\ a\mapsto(a,a)\ }&
E^2&\{(a,a):a\in E\}\\[1mm]
2&E(-1)\xrightarrow{\ a\mapsto(a,a)\ }&
E(-1)^2&\{(a,a):a\in E(-1)\}.
\end{array}
\tag{CGT12.1}
\]
The unit and hyperplane comparisons have the respective derived types \(E\to R\Gamma(\mathbf P^1,E)\) and \(E(-1)[-2]\to R\Gamma(\mathbf P^1,E)\), as in (CGT8.2). There is no asserted unshifted equivariant map \(E\to E(-1)\). The horizontal arrows in (CGT12.1) are the specialization morphisms; their images are exactly the invariant subspaces in the right column.
