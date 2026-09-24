> Original-source reading update: every printed page137–252 of Deligne's published article has now been read. The reading ledger (private construction record; not included) distinguishes this from individual formula checks and unread external references. The current corpus and operation instruction (private construction record; not included) governs all receiving calculations. The actual tau-supported lifting target remains active.

# Deligne's weight control and the complete return measure

24 September 2026. Proof reconstruction and programme comparison. Locators DWR0–DWR14.

![The top diagram shows the complete global weight-tightening mechanism, including the integral congruence class, strict bound, product map, and duality. The bottom diagram shows the proved invertible map between the complete counting measure and Deligne's original-zeta return measure. Proofs: DWR7–DWR12. The figure contains no finite numerical verification or claim of an established cohomology equivalence.](deligne_weight_return_comparison.png)

## DWR0. Sources, scope, and the user's proposed comparison

Pierre Deligne, *La conjecture de Weil. II*, Publications mathématiques de l'IHÉS 52 (1980), 137–252, [published source identity](https://numdam.org/item/PMIHES_1980__52__137_0/). The initial reconstruction used the complete [French S20 LaTeX transcription](https://www.numdam.org/item/PMIHES_1980__52__137_0/), with selected comparisons to the historical English math-mode transcription. The entire French text has been read, including chapters IV–VI. This is not a claim to have verified every transcription against the original scan, or to have independently reconstructed every cited SGA theorem. The exact coverage and discrepancies are retained in the private reading ledger (private construction record; not included). Neither transcription is the author's original TeX. The subsequent reading covered the entire original published article, printed137–252, using its original PDF and direct visual checks. The ledger records the exact original source hash, coverage and independently justified corrections. That original reading supersedes the earlier transcription-only coverage.

This note reconstructs the proof of the fundamental weight bound, its local-monodromy input, and the passage to purity. It identifies the foundational theorems being used instead of disguising them as new proofs. Applications to root systems and rational homotopy were read but are not new theorems claimed here.

The receiving datum is the user's parityless \(Z_1/\tau\) support with the complete arithmetic history retained in its receiver. No addition at \(\tau\) is defined here. No count of copies of \(\tau\) is taken. Integer labels below refer to the already reconstructed arithmetic receiver; these calculations do not replace the requested preceding construction of that receiver from the complete history.

The proposed replacement of a source zero by \(Z_1/\tau\) is investigated through the actual maps. It is not installed as an axiom. In particular, weight zero in Deligne means a modulus condition on nonzero Frobenius eigenvalues, not an unsupported arithmetic element.

## DWR1. The exact weight and operator conventions

Let \(X_0\) be of finite type over \(\mathbf F_q\), let \(X=X_0\otimes_{\mathbf F_q}\overline{\mathbf F}_q\), and let \(F\) be geometric Frobenius. A closed point \(x\) has degree \(d_x=[k(x):\mathbf F_q]\) and norm \(N(x)=q^{d_x}\). For a fixed coefficient embedding \(\iota:\overline{\mathbf Q}_\ell\to\mathbf C\), define

\[
w_Q(\alpha)=\frac{2\log|\iota\alpha|}{\log Q},\qquad Q>1,\quad\alpha\ne0.
\tag{DWR1.1}
\]

A lisse sheaf is pointwise \(\iota\)-pure of weight \(\beta\) when each eigenvalue at each closed point satisfies \(|\iota\alpha|=N(x)^{\beta/2}\). Mixed means a finite filtration with pure successive quotients. Without \(\iota\), purity requires algebraicity and this modulus for every complex embedding, with integer weight. Source: §§1.2.1–1.2.6.

Tensor products multiply eigenvalues and add weights; the dual replaces \(\alpha\) by \(\alpha^{-1}\). The Tate object \(\mathbf Q_\ell(1)\) has geometric Frobenius \(Q^{-1}\), hence weight \(-2\). Thus a twist by \((a)\) multiplies eigenvalues by \(Q^{-a}\), retaining the shift \(-2a\).

For a rank-one Weil sheaf on \(\operatorname{Spec}\mathbf F_p\) with Frobenius \(b\), its pullback at \(x\) multiplies an eigenvalue by
\[
b^{[k(x):\mathbf F_p]}=b^{[\mathbf F_q:\mathbf F_p]d_x}.
\tag{DWR1.2}
\]
The inverse tensor functor uses \(b^{-1}\), and evaluation gives the natural isomorphism between their composite and the original sheaf. No factor in (DWR1.2) is discarded. A numerical shift of weight is therefore a specified change of coefficient object and Frobenius, not a relocation of the supporting point. The reconstruction below keeps arbitrary \(\beta\) in its formulas.

## DWR2. Why determinant weights are controlled

Sources: §§1.3.1–1.3.15 and 1.11.4. For a normal geometrically connected \(X_0\), the Weil group fits into
\[
1\longrightarrow\pi_1(X,\bar x)\longrightarrow W(X_0,\bar x)
\xrightarrow{\deg}\mathbf Z\longrightarrow0.
\tag{DWR2.1}
\]
In the abelianization of the Weil group, the geometric image is the product of a finite group of order prime to \(p\) and a pro-\(p\) group. Here is the source's reduction: for a curve, class field theory describes it through degree-zero divisor class groups with moduli at the removed points. The ordinary degree-zero class group is finite because it is the rational-point group of the finite-type Picard variety over a finite field. The additional local units are finite groups times pro-\(p\) groups. For general normal \(X_0\), pass to a dense quasi-projective open and a sufficiently general curve section. Bertini surjectivity on fundamental groups and specialization of the prime-to-\(p\) abelian quotient reduce the assertion to the curve. These are the precise class-field, Picard, Bertini and specialization inputs of §1.3.1, completed in §1.11.4.

For a rank-one \(\ell\)-adic character \(\chi\), the geometric image also lies in a compact subgroup of \(E^*\) for a finite extension \(E/\mathbf Q_\ell\). Such a compact subgroup is finite times pro-\(\ell\). Because \(p\ne\ell\), the geometric image is finite. A power of \(\chi\) is therefore trivial geometrically and has the form \(b^{\deg}\). Taking a root of \(b\) proves
\[
\chi(w)=c^{\deg(w)}\epsilon(w),\qquad\epsilon\text{ of finite order}.
\tag{DWR2.2}
\]
Roots of unity have complex modulus one, so the rank-one weight is the constant \(w_q(c)\).

For an irreducible constituent \(V\) of rank \(r\), its determinant is rank one. Its determinantal weight is \(w(\det V)/r\). To control tensor and exterior powers, Deligne forms \(G^0\), the Zariski closure of geometric monodromy, and its Weil extension \(G\). A degree-one Weil element acts on \(G^0\) by conjugation, giving the exact semidirect-product construction of §1.3.7.

For a semisimple sheaf the connected geometric group is semisimple. To see the source's argument, a central torus has finitely many weights in a faithful representation. After a finite cover and a finite extension of constants the Weil action fixes those weights, acts on the connected reductive group by inner automorphisms, and the extension splits as a product with \(\mathbf Z\). Any remaining torus quotient would then supply a rank-one character with Zariski-dense geometric image. Equation (DWR2.2) makes that image finite, forcing the torus quotient to be trivial. For a nonsemisimple sheaf, passage to its Jordan–Hölder graded object has unipotent kernel. This proves the unipotent-radical assertion used in the source.

For the following central-element calculation use the semisimplified fibre: its constituent determinant weights are unchanged, while extensions in the original sheaf remain part of the later cohomology calculation. Write \(G^{00}\) for the identity component of \(G^0\), and \(w\) for the degree-one lift. A positive power \(w^a\) acts by an inner automorphism on \(G^{00}\), and trivially on the finite group \(G^0/G^{00}\). Choose \(h_0\in G^{00}\) so that \(y=h_0w^a\) centralizes \(G^{00}\). For each representative \(h\) of \(G^0/G^{00}\), the commutator \([y,h]\) lies in \(G^{00}\) and centralizes it; it is therefore in the finite centre \(Z(G^{00})\). The same is true of \([y,w]\): membership in \(G^{00}\) follows from the expression for \(y\), and centralization follows because both \(y\) and \(wyw^{-1}\) centralize \(G^{00}\). Since \(y\) centralizes this finite centre, a common positive power kills all these commutators. It centralizes the identity component, all component representatives, and the degree generator. Thus it gives \(g\in Z(G)\) of degree \(m>0\). The centre's degree kernel is finite and its image has finite index in \(\mathbf Z\).

On an irreducible representation \(V\), \(g\) is scalar. The rank-one determinant identity extends from the Weil group to \(G\): a power of the determinant character is trivial on geometric monodromy, hence on its Zariski closure \(G^0\). It therefore factors through degree. Taking the corresponding scalar root expresses the determinant as \(c^{\deg}\epsilon\) with \(\epsilon\) of finite order on \(G\) itself. Evaluation at \(g\) is legitimate even when \(g\) is not in the Weil-group image. If \(V\) has rank \(r\) and central scalar \(\alpha\), then \(\alpha^r=c^m\epsilon(g)\), whence \(|\iota\alpha|^r=|\iota c|^m\). Consequently
\[
V\text{ has determinantal weight }\beta
\quad\Longleftrightarrow\quad
|\iota\alpha|=q^{m\beta/2}\text{ for every eigenvalue of }g\text{ on }V.
\tag{DWR2.3}
\]
Multiplication of these central eigenvalues proves addition of determinantal weights under tensor product. If \(n(\beta)\) is the total rank of constituents of weight \(\beta\), the weights in \(\bigwedge^a V\) are exactly
\[
\sum_\beta a(\beta)\beta,\qquad
\sum_\beta a(\beta)=a,\quad 0\le a(\beta)\le n(\beta).
\tag{DWR2.4}
\]
The coefficients in (DWR2.4) are integers; this is exterior algebra on the complete representation, not a finite numerical test of primes.

## DWR3. Trace identity and all even tensor powers

Sources: §§1.4–1.5. Grothendieck's trace identity is
\[
\prod_{x\in|X_0|}\det(1-F_xt^{d_x},\mathcal F_{\bar x})^{-1}
=\prod_i\det(1-Ft,H_c^i(X,\mathcal F))^{(-1)^{i+1}}.
\tag{DWR3.1}
\]
It first holds as a formal power series. If the local weights are at most \(\beta\), and \(\dim X_0=d\), the bound on the number of closed points of degree \(n\) by \(Cq^{dn}\) gives absolute convergence for \(|t|<q^{-\beta/2-d}\). This also proves the product has no zero there: the sum of the absolutely convergent logarithmic series defines its logarithm.

For a smooth connected curve, \(H^0\) consists of geometric invariants and \(H_c^2\) consists of geometric coinvariants twisted by \((-1)\). Their weights are respectively determinantal weights \(\gamma\) and \(\gamma+2\). The full curve formula is
\[
L(\mathcal F,t)=
\frac{\det(1-Ft,H_c^1)}{\det(1-Ft,H_c^0)\det(1-Ft,H_c^2)}.
\tag{DWR3.2}
\]
On an affine curve with lisse coefficients, \(H_c^0=0\); its determinant is exactly one. Its removal from the displayed quotient is justified by that vanishing, not an arbitrary cancellation.

Suppose now that the local characteristic polynomials of \(\mathcal F\), after applying \(\iota\), have real coefficients. Write \(r\) for its largest determinantal weight. For every positive integer \(k\), every local factor for \(\mathcal F^{\otimes2k}\) has nonnegative real coefficients. Indeed,
\[
\det(1-At^{d_x})^{-1}
=\exp\left(\sum_{m\ge1}\frac{\operatorname{Tr}(A^m)}m t^{md_x}\right),
\quad
\operatorname{Tr}((F_x^{\otimes2k})^m)=\operatorname{Tr}(F_x^m)^{2k}\ge0.
\tag{DWR3.3}
\]
The trace is real because the characteristic polynomial is real; Newton identities or conjugate eigenvalue multisets prove this for every power. Exponentiating a series of nonnegative coefficients preserves nonnegativity. Each local factor has constant coefficient one. Thus each local series is coefficientwise bounded by the complete product series.

The denominator of the cohomological product has no zero in
\[
|t|<q^{-(2kr+2)/2},
\tag{DWR3.4}
\]
by (DWR2.4) and the \(H_c^2\) calculation. Hence the product is analytic there. Coefficientwise domination makes every local series converge in that disk too. If \(\alpha\) is a local eigenvalue, \(\alpha^{2k}\) is a tensor-power eigenvalue, and its local reciprocal determinant has a pole at every solution of \(t^{d_x}=\alpha^{-2k}\). There is no numerator in this local factor to cancel the pole. Comparing its modulus with (DWR3.4) yields
\[
|\iota\alpha|^{2k/d_x}\le q^{(2kr+2)/2},
\qquad w_{N(x)}(\alpha)\le r+\frac1k.
\tag{DWR3.5}
\]
This holds for every \(k\), so \(w_{N(x)}(\alpha)\le r\).

For each determinant-weight class \(\beta\), write its local eigenvalues as \(\alpha_i^\beta\). The determinant gives the exact equality
\[
\sum_i w_{N(x)}(\alpha_i^\beta)=n(\beta)\beta.
\tag{DWR3.6}
\]
Let \(a=1+\sum_{\gamma>\beta}n(\gamma)\). The largest determinant weight of \(\bigwedge^a\mathcal F\) is \(\beta+\sum_{\gamma>\beta}n(\gamma)\gamma\), by (DWR2.4). This exterior power is also real: its eigenvalue multiset is made of products of distinct indices from a conjugation-stable multiset. Apply (DWR3.5), for all \(k\), to the eigenvalue
\(\alpha_i^\beta\prod_{\gamma>\beta}\prod_j\alpha_j^\gamma\).
Subtract (DWR3.6) for every \(\gamma>\beta\). The result is \(w(\alpha_i^\beta)\le\beta\). Summing those inequalities gives equality (DWR3.6), so every inequality is equality. This proves §1.5.1: every constituent of a real lisse sheaf on the curve is pure.

## DWR4. Boundary weights with every boundary factor retained

Source: §1.8.1. Let \(j:U_0\hookrightarrow X_0\) be the complement of a finite set \(S_0\) in a smooth curve, and let \(\mathcal F_0\) be lisse pure of weight \(\beta\) on \(U_0\). Remove a point of \(U_0\), if necessary, to make the ambient curve affine without removing the boundary point under consideration. Then
\[
\prod_{x\in|U_0|}\det(1-F_xt^{d_x},\mathcal F)^{-1}
\prod_{x\in|S_0|}\det(1-F_xt^{d_x},j_*\mathcal F)^{-1}
=\frac{\det(1-Ft,H_c^1(X,j_*\mathcal F))}
{\det(1-Ft,H_c^2(X,j_*\mathcal F))}.
\tag{DWR4.1}
\]
The interior product is nonzero and holomorphic in \(|t|<q^{-(\beta+2)/2}\). The right denominator has no zero in that disk. Therefore the boundary product has no pole there. Its reciprocal-polynomial factors cannot cancel each other's poles. This proves each boundary eigenvalue has weight at most \(\beta+2\).

At a boundary stalk, the inclusion
\[
(V^I)^{\otimes k}\hookrightarrow(V^{\otimes k})^I
\tag{DWR4.2}
\]
is the literal inclusion of tensors of inertia-invariant vectors into invariant tensors. Applying the preceding bound to \(\mathcal F^{\otimes k}\) gives
\[
kw_{N(x)}(\alpha)\le k\beta+2,
\quad w_{N(x)}(\alpha)\le\beta+2/k.
\tag{DWR4.3}
\]
All positive integers \(k\) give the sharp boundary bound \(w\le\beta\). The zero-free comparison of the same complete identity bounds \(H_c^1\) by \(\beta+2\). Extension to general open immersions is by sheaf extensions, support reduction, finite normalization, and restriction to generic points of boundary divisors, as in §1.8.9; transverse curves supply the boundary calculation. The dual gives the opposite bound wherever a lisse sheaf extends across the boundary.

## DWR5. The local nilpotent operator and its exact purity calculation

Sources: §§1.6–1.8. For a nilpotent endomorphism \(N\), its monodromy filtration \(M\) is characterized by
\[
NM_i\subset M_{i-2},\qquad
N^j:\operatorname{Gr}_j^M V\xrightarrow{\sim}\operatorname{Gr}_{-j}^M V.
\tag{DWR5.1}
\]
For a Jordan chain of length \(d+1\), place its vectors in degrees \(d,d-2,\ldots,-d\); \(N\) lowers degree by two. Their sums construct \(M\). Intrinsically, if \(N^{d+1}=0\), take \(M_d=V\), \(M_{d-1}=\ker N^d\), \(M_{-d}=\operatorname{im}N^d\), \(M_{-d-1}=0\), and recurse on \(\ker N^d/\operatorname{im}N^d\). The same forced extreme terms and induction prove uniqueness. For a relative filtration, §1.6.13 uses induction on the pre-existing filtration; no existence is asserted solely from uniqueness.

In the geometric application the operator is typed as
\[
N:V(1)\longrightarrow V,
\qquad \rho(\sigma)=\exp(Nt_\ell(\sigma))
\tag{DWR5.2}
\]
on a finite-index inertia subgroup. After a finite cover, this subgroup is all inertia. The cover changes neither the weights nor the monodromy filtration: it raises Frobenius powers and multiplies the chosen logarithm by a nonzero scalar. Thus \(V^I=\ker N\) is the boundary stalk.

Put \(P_{-j}=\ker(N:\operatorname{Gr}_{-j}^M V\to\operatorname{Gr}_{-j-2}^M V(-1))\). Keeping the one-dimensional space of logarithms gives
\[
\operatorname{Gr}_i^M V\cong
\bigoplus_{j\ge|i|,\ j\equiv i\ (2)}P_{-j}\bigl(-(i+j)/2\bigr).
\tag{DWR5.3}
\]
The sign is forced: \(N^{(i+j)/2}\) maps the corresponding summand of \(\operatorname{Gr}_i^M V((i+j)/2)\) to \(P_{-j}\). Solving for the untwisted source gives (DWR5.3). The local transcription's positive sign in §1.6.14.3 fails this test and its own weight check; the original file is preserved and the correction is recorded separately.

The \(\mathfrak{sl}_2\) decomposition of Jordan chains gives the primitive tensor and dual maps
\[
P_{-j'}(V)\otimes P_{-j''}(W)
\bigl((j-j'-j'')/2\bigr)\longrightarrow P_{-j}(V\otimes W)
\tag{DWR5.4}
\]
as direct summands for \(|j'-j''|\le j\le j'+j''\) with the matching parity, and
\[
P_{-j}(V^\vee)\cong P_{-j}(V)^\vee(j).
\tag{DWR5.5}
\]
For specificity, the tensor decomposition is \(S_{j'}\otimes S_{j''}=\bigoplus_{j=|j'-j''|,\;\mathrm{step}\;2}^{j'+j''}S_j\), where \(S_j=\operatorname{Sym}^j\) of the two-dimensional representation. Comparing the weights \(j,j-2,\ldots,-j\) proves its character identity; complete reducibility in characteristic zero gives the decomposition. Choosing lowest-weight vectors determines the maps, and tracking their rescaling by the choice of \(N\) gives exactly the twist in (DWR5.4). Applying the dual to a chain gives (DWR5.5).

Now retain arbitrary input weight \(\beta\), and write \(Q=N(s)\) at the boundary point. A primitive eigenvalue \(\alpha\) in \(P_{-j}(V)\) gives an eigenvalue \(\alpha^2Q^j\) in the summand \(P_{-j}(V)^{\otimes2}(-j)\subset P_0(V^{\otimes2})\). By DWR4 applied to the sheaf of weight \(2\beta\),
\[
|\iota\alpha|^2Q^j\le Q^{\beta}.
\tag{DWR5.6}
\]
Apply this same result to the dual sheaf, of weight \(-\beta\). Equation (DWR5.5) supplies its primitive eigenvalue \(\alpha^{-1}Q^{-j}\), hence
\[
|\iota\alpha|^{-2}Q^{-2j}Q^j\le Q^{-\beta}.
\tag{DWR5.7}
\]
Equations (DWR5.6)–(DWR5.7) force
\[
|\iota\alpha|=Q^{(\beta-j)/2}.
\tag{DWR5.8}
\]
Finally (DWR5.3) multiplies it by \(Q^{(i+j)/2}\), so every eigenvalue on \(\operatorname{Gr}_i^M V\) has modulus \(Q^{(\beta+i)/2}\). This is the full local-monodromy purity theorem §1.8.4, with its original weight and every Tate factor retained. Boundary invariants occupy only indices \(i\le0\).

## DWR6. Why the preliminary cohomological bound is strict

Sources: chapter II, especially §§2.1.4–2.1.9 and 2.2.10. Let a group \(G\) be an extension of \(\mathbf Z\) or \(\mathbf R\) by a compact group; let \(x_v\) be conjugacy classes with \(Nv>1\). Suppose the Euler products converge for \(\Re s>1\). For a unitary representation \(\rho\),
\[
-\frac{L'}{L}(\rho,s)
=\sum_{v,m\ge1}(\log Nv)(Nv)^{-ms}\operatorname{Tr}\rho(x_v^m).
\tag{DWR6.1}
\]
For real \(\sigma>1\), the weights on the right define a finite positive measure. Since \(\operatorname{Tr}(\rho\otimes\bar\rho)(g)=|\operatorname{Tr}\rho(g)|^2\), its transform is nonnegative on every such tensor square, including virtual representations.

Assume now the source's specified meromorphic continuation with only the trivial-character simple pole on the boundary \(\Re s\ge1\). Multiplying the preceding inequality by \(\sigma-1>0\) and taking \(\sigma\downarrow1\) gives
\[
\nu(\rho\otimes\bar\rho)\ge0,
\tag{DWR6.2}
\]
where \(\nu\) is pole order minus zero order at the boundary. Thus \(\nu(1)=1\), \(\nu(\chi)=\nu(\bar\chi)\), and \(\nu(\chi)\le0\) for nontrivial irreducibles.

Here is the global character argument that uses all representations. First take the closure \(K\) of the image of \(G\) in the product of the unitary groups of all its finite-dimensional unitary representations. This is compact. Each such representation extends by its coordinate projection; density preserves irreducibility, intertwiners, tensor products and multiplicities because each intertwining equation is a closed condition. Conversely every continuous representation of \(K\) restricts to one of \(G\). The character calculation can therefore be made on \(K\), with Haar measure of total mass one.

Fix a finite set of irreducibles and \(0<\epsilon<1\). Put \(e_1=e_2=\epsilon/4\), and choose a central inversion-invariant neighbourhood \(U\) of the identity on which \(|\chi(g)-\dim\chi|<e_1\dim\chi\) for every chosen character. A continuous central inversion-invariant function supported in \(U\) is obtained by averaging a bump function over conjugation and inversion. Add a sufficiently small positive constant and approximate uniformly by a finite character combination using the central Peter–Weyl density theorem. Taking its real part and inversion average gives a real inversion-invariant combination. Its character coefficients are real: substitution \(g\mapsto g^{-1}\) in their Haar integrals identifies each coefficient with its complex conjugate. Approximate these coefficients by rationals, preserving conjugate pairs, and multiply by a common positive denominator. The resulting integral virtual character \(f\) can still be chosen with \(M=\int_K|f|^2>0\) and \(\int_{K\setminus U}|f|^2\le e_2M\), since both strict concentration and positivity persist under sufficiently small uniform perturbations.

Write \(f=\rho^+-\rho^-\) with disjoint irreducible supports and put \(\rho=\rho^++\rho^-\). The exact difference
\[
\rho\otimes\bar\rho-f\otimes\bar f
=2\bigl(\rho^+\otimes\overline{\rho^-}+\rho^-\otimes\overline{\rho^+}\bigr)
\tag{DWR6.2a}
\]
has nonnegative multiplicities and trivial multiplicity zero. The exterior part of the Haar integral cannot be dropped: \(\operatorname{Re}\overline{\chi(g)}\ge-\dim\chi\) everywhere, so
\[
\begin{aligned}
[f\otimes\bar f:\chi]
&=\operatorname{Re}\int_K|f|^2\bar\chi\,dg\\
&\ge(\dim\chi)\bigl[(1-e_1)(1-e_2)-e_2\bigr]M\\
&=(\dim\chi)(1-3\epsilon/4+\epsilon^2/16)M
\ge(1-\epsilon)(\dim\chi)M.
\end{aligned}
\tag{DWR6.2b}
\]
Since \([\rho\otimes\bar\rho:1]=M\), this proves
\[
[\rho\otimes\bar\rho:\chi]\ge(1-\epsilon)\dim\chi\,[\rho\otimes\bar\rho:1].
\tag{DWR6.3}
\]
Use (DWR6.3) in (DWR6.2), let \(\epsilon\downarrow0\), and enlarge the finite set. Because all nontrivial contributions are nonpositive integers,
\[
1+\sum_{\chi\ne1}\dim\chi\,\nu(\chi)\ge0.
\tag{DWR6.4}
\]
At most one nontrivial irreducible can have negative order; it must have dimension one, order \(-1\), and be self-conjugate. It is a character of order two. This is Deligne's precise exceptional possibility, not an unmentioned deletion.

For the curve's monodromy representation, DWR2 supplies a semisimple geometric group. Its complexification has a compact form after retaining the degree direction. Twisting each pure constituent by its inverse central scalar makes its geometric semisimple Frobenius powers relatively compact; conjugacy of maximal compact subgroups places those classes in the compact form. The tensor functor and all inverse twists remain those of (DWR1.2). The trace formula supplies the meromorphic continuation required above. A nontrivial irreducible on the geometric subgroup has neither invariant nor coinvariant and hence no denominator in (DWR3.2). The geometrically trivial one supplies the curve's zeta pole. The possible quadratic exception is removed by the exact double-cover identity
\[
\zeta_{X'_0}(s)=\zeta_{X_0}(s)L(\epsilon,s):
\tag{DWR6.5}
\]
both curve zeta functions have a simple pole at \(s=1\), so the second factor cannot vanish there. These statements concern the actual connected cover; extensions of the constant field retain a simple pole at this real point as well.

Consequently the cohomological numerator has no zero on its outer weight boundary. Together with DWR4 this proves
\[
\alpha\in\operatorname{Spec}(F|H_c^1(U,\mathcal F))
\quad\Longrightarrow\quad w_q(\alpha)<\beta+2.
\tag{DWR6.6}
\]
At a trivial-character pole there is also no hidden numerator cancellation: the actual pole is simple and the denominator has exactly that simple zero. Arbitrary \(\beta\) follows with the explicit eigenvalue multiplier and inverse from (DWR1.2).

## DWR7. Vanishing cycles retain the orientation data

Source: §3.1. Embed a smooth projective surface \(S\), with normal-crossings boundary \(D\), in projective space and choose a Lefschetz pencil transverse to its strata. Blow up its axis: \(\pi:\widetilde S\to S\), and write \(f:\widetilde S\to\mathbf P^1\). The three exceptional fibres have an ordinary node, a tangency to one boundary branch, or a crossing of two boundary branches. Assume unipotent local monodromy of the coefficient sheaf, obtained later by a finite cover.

For a two-element set \(B\), the orientation object is
\[
\epsilon(B)=\mathbf Z^B/\mathbf Z(1,1).
\tag{DWR7.1}
\]
Exchanging the two labels acts by minus one. This actual source orientation is retained; no identification with a user's information layer is assumed. The only nonzero vanishing-cycle degree is one. At a node,
\[
\Phi_x^1=\mathcal G_x(-1)\otimes\epsilon(B).
\tag{DWR7.2}
\]
At a boundary tangency or crossing, a local filtration \(A\) with constant quotients gives
\[
\operatorname{Gr}_A^i\Phi_x^1
=\operatorname{Gr}_A^i(\mathcal G)_x\otimes\epsilon(B).
\tag{DWR7.3}
\]
At a node \(uv=t\), Picard–Lefschetz retains the two Kummer branch classes \([u],[v]\). Over the geometric generic fibre \([u]+[v]=[t]=0\), and exchanging branches sends \([u]\) to \(-[u]\). Thus the quotient of the two labelled generators by their sum gives exactly the orientation object in (DWR7.1); the Kummer coefficient twist supplies \((-1)\). The class \([u/v]=[u]-[v]=2[u]\) must not replace the labelled branch generator in integral or mod-two coefficients. For tangency, apply vanishing cycles to \(0\to j_!\mathbf Q_\ell\to\mathbf Q_\ell\to\mathbf Q_{\ell,D}\to0\); the ambient smooth contribution vanishes and the boundary's degree-zero difference moves into degree one. For a crossing use the two-branch normalization sequence \(0\to j_!\mathbf Q_\ell\to\mathbf Q_\ell\to i_*\mathbf Q_\ell\to\mathbf Q_{\ell,x}\otimes\epsilon(B)\to0\). Its last term has vanishing cycles in degree \(-1\), so the two shifts again place the answer in degree one. Applying the local filtration proves (DWR7.3) for the original sheaf.

The axis correction and the receiving spectral sequence are
\[
H_c^*(\widetilde V,\pi^*\mathcal G)
\cong H_c^*(V,\mathcal G)\oplus
H^0(V\cap A,\mathcal G)(-1)[-2],
\tag{DWR7.4}
\]
\[
E_2^{ab}=H^a(\mathbf P^1,R^bf_!\pi^*\mathcal G)
\Longrightarrow H_c^{a+b}(\widetilde V,\pi^*\mathcal G).
\tag{DWR7.5}
\]
The extra summand in (DWR7.4) is in cohomological degree two. The pullback injection of the original cohomology has a retraction by proper pushforward/Poincaré duality; no exceptional divisor contribution is discarded.

## DWR8. The global product argument, with the original input weight

Source: §§3.2.1–3.2.14. We prove, for every integer \(k\ge0\), every smooth curve \(U_0\), and every lisse pure coefficient sheaf of weight \(\beta\),
\[
w_q(\alpha)\le\beta+1+2^{-k}
\quad(\alpha\text{ on }H_c^1(U,\mathcal F)).
\tag{DWR8.1}
\]
The case \(k=0\) is DWR4. A sheaf on a curve that is lisse pure on a dense open has its \(H_c^1\) as a quotient of that open's \(H_c^1\): the complementary finite support has no \(H_c^1\). Thus (DWR8.1) applies to such intermediate extensions too.

Assume (DWR8.1) for a fixed \(k\). Let \(X_0\) compactify \(U_0\), put \(V_0=U_0\times U_0\), and retain the actual coefficient
\[
\mathcal G_0=\mathcal F_0\boxtimes\mathcal F_0,
\qquad w(\mathcal G_0)=2\beta.
\tag{DWR8.2}
\]
Choose the pencil of DWR7 on \(X_0\times X_0\). For arbitrary real \(\beta\), take a rank-one Weil object \(L\) whose eigenvalue at a point of norm \(Q\), after \(\iota\), is \(Q^{2\beta}\). Such an object is obtained on \(\mathbf F_p\) by \(\iota(b)=p^{2\beta}\), as in (DWR1.2). Then
\[
\mathcal G_0\oplus(\mathcal G_0^\vee\otimes L)
\tag{DWR8.3}
\]
is pure of weight \(2\beta\) and real: if \(|\lambda|=Q^\beta\), its paired eigenvalue is \(Q^{2\beta}/\lambda=\bar\lambda\). This keeps the companion and its factor explicitly, without replacing \(\mathcal G_0\).

The fibre trace formula and strict bound DWR6 separate the \(H_c^2\) poles from \(H_c^1\) zeros; their conjugate multisets are therefore separately invariant. Duality handles \(H_c^0\) for a proper fibre. Thus the \(H_c^1\) characteristic polynomial of a real pure coefficient sheaf is real (§3.2.1). Applied fibrewise to (DWR8.3), this makes \(R^1f_!\pi^*\mathcal G_0\) on the smooth pencil locus a direct summand of a real sheaf. DWR3 proves that all its constituents are pure.

The vanishing-cycle exact sequence is
\[
0\to(R^1f_!\pi^*\mathcal G)_{\bar t}
\to(R^1f_!\pi^*\mathcal G)_{\bar\eta}
\to\Phi_x^1
\to(R^2f_!\pi^*\mathcal G)_{\bar t}
\to(R^2f_!\pi^*\mathcal G)_{\bar\eta}\to0.
\tag{DWR8.4}
\]
There are no punctual sections in \(R^1\). Extend a constituent filtration by intersection in the direct image from the smooth locus. The defect of a constituent's specialization is a subquotient of \(\Phi_x^1\).

DWR5 at the boundary of \(U_0\) gives weights in \(\beta+\mathbf Z\); tensoring the two factors gives \(2\beta+\mathbf Z\). Equations (DWR7.2)–(DWR7.3), including the twist \((-1)\) and the finite orientation character, keep vanishing-cycle weights in \(2\beta+\mathbf Z\). A constituent with nonzero specialization defect therefore has weight in this same class modulo \(\mathbf Z\). If it has no defect anywhere, it is lisse on all of \(\mathbf P^1\), hence geometrically constant, and its \(H^1\) is zero. DWR6 applied to every smooth fibre gives weight strictly below \(2\beta+2\). Every contributing constituent thus has
\[
w\in2\beta+\mathbf Z,\qquad w<2\beta+2,
\qquad\text{hence }w\le2\beta+1.
\tag{DWR8.5}
\]
This is the exact place where strictness and integrality work together.

Apply the induction bound to these constituents on the pencil. It gives weight at most \(2\beta+2+2^{-k}\) on \(E_2^{11}\). The invariant/coinvariant computations of DWR3 give at most \(2\beta+2\) on \(E_2^{02}\) and \(E_2^{20}\). The spectral sequence (DWR7.5), whose later terms are subquotients, therefore bounds the whole \(H_c^2(\widetilde V,\pi^*\mathcal G)\) by \(2\beta+2+2^{-k}\).

Künneth and the actual pullback give the Frobenius-equivariant injections
\[
H_c^1(U,\mathcal F)\otimes H_c^1(U,\mathcal F)
\hookrightarrow H_c^2(V,\mathcal G)
\hookrightarrow H_c^2(\widetilde V,\pi^*\mathcal G).
\tag{DWR8.6}
\]
An eigenvalue \(\alpha\) therefore supplies \(\alpha^2\) in that bounded group. Consequently
\[
2w_q(\alpha)\le2\beta+2+2^{-k},
\qquad w_q(\alpha)\le\beta+1+2^{-(k+1)}.
\tag{DWR8.7}
\]
To remove the auxiliary pencil and ramification assumptions, a finite cover makes boundary monodromy unipotent, and a finite extension of the field defines a sufficiently general pencil and its exceptional points. Pullback on cohomology is injective because trace divided by the nonzero covering degree is a retraction in \(\mathbf Q_\ell\). Extension \(\mathbf F_q\subset\mathbf F_{q^d}\) replaces \(F\) by \(F^d\), and \(w_{q^d}(\alpha^d)=w_q(\alpha)\); the bound descends. This completes induction for every \(k\). Taking all \(k\) proves \(w_q(\alpha)\le\beta+1\), globally.

## DWR9. The reverse inequality and purity

Source: §3.2.15. For \(j:U\hookrightarrow X\) with \(X\) a smooth proper curve, \(H^1(X,j_*\mathcal F)\) is the image of \(H_c^1(U,\mathcal F)\to H^1(U,\mathcal F)\). Its upper bound is DWR8. Poincaré duality supplies the perfect pairing with \(H^1(X,j_*\mathcal F^\vee(1))\). The latter sheaf has input weight \(-\beta-2\), so its eigenvalue paired with \(\alpha\) is \(\alpha^{-1}\), and DWR8 gives
\[
w_q(\alpha^{-1})\le(-\beta-2)+1=-\beta-1.
\tag{DWR9.1}
\]
Thus \(w_q(\alpha)\ge\beta+1\). Combining the two proved bounds gives equality. Degrees zero and two are the invariant and twisted-coinvariant calculations. This proves
\[
w_q(\alpha)=\beta+i
\quad\text{on }H^i(X,j_*\mathcal F).
\tag{DWR9.2}
\]
The source's arithmetic zeros in kernels and exact sequences remain zero vectors throughout. Neither inequality is supplied by relabelling them.

## DWR10. General direct images and every boundary term

Source: §3.3. For \(f:X\to Y\) of finite type and mixed \(\mathcal F\) of weights at most \(n\), the conclusion is that \(R^if_!\mathcal F\) has weights at most \(n+i\). The source reductions are: sheaf extensions by long exact sequences; open/closed decompositions in \(X\) and \(Y\); composition by the Leray spectral sequence; invariance under universal homeomorphisms; and relative dimension zero, where only \(f_!\) remains and preserves weight. An affine-coordinate factorization followed by these reductions reduces relative dimension to one. Dense-open reduction and a finite cover then give a smooth proper curve family \(\bar f:\bar X\to Y\), a finite étale boundary \(i:D\hookrightarrow\bar X\), and \(j:X\hookrightarrow\bar X\), with tame lisse pure coefficients of weight \(n\).

Retain the exact sequence
\[
0\to j_!\mathcal F\to j_*\mathcal F\to i_*i^*j_*\mathcal F\to0.
\tag{DWR10.1}
\]
DWR9 on each fibre makes \(R^i\bar f_*j_*\mathcal F\) pure of weight \(n+i\). DWR5 filters the boundary term into weights \(n+a\), \(a\le0\). Since \(\bar f i\) is finite, its higher direct images vanish and its degree-zero direct image preserves those weights. The long exact sequence of (DWR10.1) proves the claimed bound for \(R^if_!\mathcal F\), including the boundary injection into degree one. This is the final calculation behind the general theorem, rather than an assumption of purity for the boundary.

For \(X\) smooth of pure dimension \(d\) and \(\mathcal F\) lisse of weights at least \(n\), apply the upper bound to \(\mathcal F^\vee\). The group
\[
H_c^{2d-i}(X,\mathcal F^\vee)(d)
\tag{DWR10.2}
\]
has weights at most \(-n+(2d-i)-2d=-n-i\). Its dual is \(H^i(X,\mathcal F)\), giving the lower bound \(n+i\). Hence the image of \(H_c^i\to H^i\), for pure coefficients, is pure of weight \(n+i\). Properness makes that map an isomorphism.

## DWR11. What the later mixed-sheaf formalism adds

Sources: §§3.4, 3.6 and 6.1–6.2. Initially let \(\mathcal F_0,\mathcal G_0\) be lisse pure of weights \(\beta,\gamma\) on a smooth finite-type \(X_0/\mathbf F_q\). The extension exact sequence
\[
0\to H^0(X,\mathcal Hom(\mathcal F,\mathcal G))_F
\to\operatorname{Ext}^1(\mathcal F_0,\mathcal G_0)
\to H^1(X,\mathcal Hom(\mathcal F,\mathcal G))^F
\tag{DWR11.1}
\]
comes from comparing a geometric splitting with its Frobenius translate: its difference is a homomorphism, changed by \((F-1)h\) when the splitting changes. A geometric extension needs eigenvalue one in the final group. DWR10 bounds that group's weights below by \(\gamma-\beta+1\), in the congruence class \(\gamma-\beta+\mathbf Z\). Thus a geometrically nontrivial extension of weights \(\beta,\gamma\) requires \(\beta>\gamma\) and equal classes modulo \(\mathbf Z\). This proves geometric semisimplicity for pure sheaves, and permits induction constructing the unique weight filtration and decomposition modulo \(\mathbf Z\). The stalks are sums of the corresponding generalized Frobenius eigenspaces; this gives uniqueness and strict compatibility of maps.

For a bounded constructible complex \(K\), the dual is
\[
D_XK=R\mathcal Hom(K,K_X),\qquad K_X=Ra^!\mathbf Q_\ell.
\tag{DWR11.2}
\]
For smooth \(d\)-dimensional \(X\), \(K_X=\mathbf Q_\ell(d)[2d]\). Weight at most \(n\) means \(\mathcal H^iK\) has weight at most \(n+i\). The spectral sequence with terms \(R^pf_!\mathcal H^qK\) then proves preservation of the complex bound by \(Rf_!\). Purity requires the upper bound for \(K\) and the opposite upper bound for \(D_XK\). Proper duality \(D_YRf_*K\cong Rf_*D_XK\) proves proper pushforward preserves this purity. The operator, shift, and Tate factor all belong to that argument.

For the local invariant-cycle calculation of §3.6, take a proper morphism \(f:X\to S\), with \(S\) a henselian trait with algebraically closed residue field \(k\), \(X\) essentially smooth over \(k\), and \(X_{\bar\eta}\) smooth over its geometric generic point. All cohomology in the conclusion has \(\mathbf Q_\ell\) coefficients, with \(\ell\) invertible on \(S\). Spreading out and specialization reduce to \(S\) the henselization at a point of a smooth curve, and \(X\) the corresponding localization of a smooth variety \(X'\). Descent to a finite field supplies the arithmetic Frobenius. Work on a connected component of \(X'\), and retain \(N=\dim X'\), the total dimension, not the dimension of the special fibre.

Write \(I=\operatorname{Gal}(\bar\eta/\eta)\). Its prime-to-\(\ell\) part has no higher \(\ell\)-primary cohomology; the remaining procyclic quotient \(\mathbf Z_\ell(1)\) has cohomology only in degrees zero and one, namely invariants and coinvariants with twist \((-1)\). The Hochschild–Serre sequence therefore gives the complete exact row
\[
0\longrightarrow H^{i-1}(X_{\bar\eta})_I(-1)
\longrightarrow H^i(X_\eta)
\longrightarrow H^i(X_{\bar\eta})^I
\longrightarrow0.
\tag{DWR11.3}
\]
Proper base change identifies \(H^i(X)\) with \(H^i(X_s)\). Localization and the duality for the smooth total space give the exact portion
\[
H^i(X_s)\longrightarrow H^i(X_\eta)
\xrightarrow{\partial}H^{i+1}_{X_s}(X)
\cong H^{2N-i-1}(X_s)^\vee(-N).
\tag{DWR11.4}
\]
The duality assertion here is made after passage to \(\mathbf Q_\ell\); integral torsion has not been asserted absent. The specialization map is the composite of the first arrow of (DWR11.4) and the surjection in (DWR11.3).

The generic \(H^i\) arises from the pure weight-\(i\) sheaf of the smooth proper family away from the special point. DWR5 bounds its inertia invariants above by \(i\). The proper special fibre has \(H^{2N-i-1}\) of weights at most \(2N-i-1\), by DWR10. Taking its dual and the displayed twist gives the opposite bound
\[
w\!\left(H^i(X_{\bar\eta})^I\right)\le i,\qquad
w\!\left(H^{2N-i-1}(X_s)^\vee(-N)\right)
\ge -(2N-i-1)+2N=i+1.
\tag{DWR11.5}
\]
Let \(W_i\) select all generalized Frobenius eigenspaces of weight at most \(i\). This is an exact functor on the finite-dimensional mixed Frobenius modules: an equivariant map respects the generalized-eigenvalue decomposition, and taking any chosen set of those summands is exact. Equation (DWR11.3) thus makes \(W_iH^i(X_\eta)\) surject onto the whole invariant target. Equation (DWR11.5) makes \(\partial\) vanish on \(W_iH^i(X_\eta)\), since its target has no such weights. Exactness of (DWR11.4) lifts each of those classes to \(H^i(X_s)\). Consequently
\[
\operatorname{sp}^*:H^i(X_s)\twoheadrightarrow H^i(X_{\bar\eta})^I
\tag{DWR11.6}
\]
is surjective. This is the source's actual quotient-and-lift calculation: the obstruction map vanishes on the required weight part, while the entire obstruction group, the coinvariant term, and both Tate twists remain in the diagram.

## DWR12. Exact map from complete returns to Deligne's measure

Receiving source: [RETURN_MEASURE_RIGIDITY.md, RMR0–RMR5](RETURN_MEASURE_RIGIDITY.md), read for this comparison, and [GLOBAL_HISTORY_WEIL_ENERGY.md, GHE1–GHE9](GLOBAL_HISTORY_WEIL_ENERGY.md). The preceding complete-history construction is required before attaching the conventional integer labels. In its arithmetic receiver retain
\[
\mathcal D=\delta_0+\sum_{n\ge2}\delta_{\log n},\quad
\mathcal R=\sum_p\sum_{m\ge1}\frac1m\delta_{m\log p},\quad
\mathcal W=t\mathcal R=\sum_p\sum_{m\ge1}\frac{m\log p}{m}\delta_{m\log p}.
\tag{DWR12.1}
\]
Each measure is locally finite. To specify the domains, let \(\mathfrak I\) be the additive group of locally finite complex measures of locally finite total variation on \([0,\infty)\), each supported in \([a,\infty)\) for some \(a>0\). The value of \(a\) may depend on the measure. Convolution is defined by addition of times. It is locally finite because the inverse image of \([0,T]\) is contained in \([0,T]^2\), where both total variations are finite. The convolution of \(r\) copies of a measure supported in \([a,\infty)\) is supported in \([ra,\infty)\). Accordingly \(\delta_0+\mathfrak I\) is a group under convolution, with inverse \(\sum_{r\ge0}(-h)^{*r}\) for \(\delta_0+h\); only finitely many terms contribute on each \([0,T]\).

In this same group define
\[
\log_*(\delta_0+h)=\sum_{r\ge1}\frac{(-1)^{r+1}}r h^{*r},
\qquad
\exp_*h=\delta_0+\sum_{r\ge1}\frac{h^{*r}}{r!}.
\tag{DWR12.1a}
\]
The formal power-series identities for exponential and logarithm become finite identities after restriction to any \([0,T]\). Therefore they are inverse group isomorphisms between \((\delta_0+\mathfrak I,*)\) and \((\mathfrak I,+)\). This proves the identities for the complete measures, not just a finite set of return times. The exact arithmetic convolution maps are
\[
\mathcal R=\log_*\mathcal D,\qquad
\mathcal D=\exp_*\mathcal R
=\delta_0+\sum_{r\ge1}\frac{\mathcal R^{*r}}{r!}.
\tag{DWR12.2}
\]
Here convolution adds real times in the receiver. No operation on \(\tau\) is implied. On every compact time interval, the positive-time part is nilpotent under truncated convolution since its support starts at \(\log2>0\). Exponential and logarithm are therefore finite polynomial identities on that interval. For each primitive period, \(\exp_*(\sum_{m\ge1}\delta_{m\log p}/m)=\sum_{a\ge0}\delta_{a\log p}\). Multiplying these factors gives exactly \(\mathcal D\) by unique factorization. This proves (DWR12.2) globally by equality on every compact interval, with its unit atom intact.

For real \(\sigma>1\), set
\[
\mu_\sigma=e^{-\sigma t}\mathcal W
=\sum_p\sum_{m\ge1}(\log p)p^{-m\sigma}\delta_{m\log p}.
\tag{DWR12.3}
\]
This is **exactly** the measure in Deligne §2.1.9, not merely an analogous shape. The morphism on the original complete measures and its inverse are
\[
\mathcal D\longmapsto e^{-\sigma t}\,t\log_*\mathcal D=\mu_\sigma,
\qquad
\mu_\sigma\longmapsto
\exp_*\left(\frac{e^{\sigma t}}t\mu_\sigma\right)=\mathcal D.
\tag{DWR12.4}
\]
More generally \(\Phi_\sigma:\delta_0+\mathfrak I\to\mathfrak I\), given by the first formula in (DWR12.4), is a group isomorphism from convolution to addition. Indeed \(\log_*(D_1*D_2)=\log_*D_1+\log_*D_2\), and multiplication of a measure by \(e^{-\sigma t}t\) is a linear automorphism of \(\mathfrak I\), with inverse multiplication by \(e^{\sigma t}/t\). Both multipliers and their inverses are bounded on every compact subset of the positive support. This proves both the operation law and the displayed inverse. For the arithmetic \(\mathcal D\), its image is also a finite positive measure when \(\sigma>1\); general elements of \(\mathfrak I\) need not be positive or have finite total mass.

The inverse multiplier is only applied on \(t>0\), where the return measure is supported; it has no division at a zero atom. The unit \(\delta_0\) returns as the constant term of \(\exp_*\). Thus all prime-power repetitions and the unit are recovered. The absence of an atom in \(\mathcal R\) at time zero is distinct from the parityless supporting datum. The marked comparison \((\tau,D)\mapsto(\tau,\Phi_\sigma(D))\) fixes that supporting datum in both directions and adds no operation on it.

For \(\Re s>1\), absolute convergence follows from comparison with \(\sum_{n\ge2}(\log n)n^{-1-\delta}\) on every \(\Re s\ge1+\delta\). Consequently
\[
\zeta(s)=\int e^{-st}\,d\mathcal D(t)
=\exp\left(\int_{t>0}\frac{e^{-(s-\sigma)t}}t\,d\mu_\sigma(t)\right),
\quad
-\frac{\zeta'}{\zeta}(\sigma+iu)=\int e^{-iut}\,d\mu_\sigma(t).
\tag{DWR12.5}
\]
The original \(\zeta\), with constant term one, is used throughout. There is no Gamma multiplier or completed replacement in (DWR12.5).

Positive definiteness is now a calculation for every finite family of real \(u_j\) and complex \(c_j\):
\[
\sum_{j,k}\bar c_jc_k\left[-\frac{\zeta'}\zeta(\sigma+i(u_k-u_j))\right]
=\int\left|\sum_k c_ke^{-iu_kt}\right|^2d\mu_\sigma(t)\ge0.
\tag{DWR12.6}
\]
This is the positivity that enters chapter II. Its stated domain is \(\sigma>1\). Analytic continuation of the scalar transform does not continue a finite positive measure by itself; the source's boundary argument explicitly supplies the additional meromorphic and pole information before taking its residue limit.

## DWR13. The base-point map and the weight datum in its stalk

The following comparison uses the already constructed pointed receiver; it does not define \(\tau\) by a complex coordinate. On a singleton supporting space named \(\tau\), a sheaf of coefficient vector spaces is specified by its stalk \(V\), with its operator \(F\), filtration and any pairing. The unique map from a singleton named \(b\) to this singleton induces mutually inverse sheaf functors: keep the same stalk and each of its maps. Explicitly,
\[
(\{b\},V,F,M,\langle\ ,\ \rangle)
\longmapsto(\{\tau\},V,F,M,\langle\ ,\ \rangle),
\tag{DWR13.1}
\]
with inverse changing only the support name back. Compositions fix every stalk element and every operator. This proves the exact base-renaming isomorphism. It assigns no parity or arithmetic value to \(\tau\). It also leaves every eigenvalue unchanged, because \(\det(TI-F)\) is literally the same polynomial before and after the functor.

An actual Frobenius-equivariant stalk isomorphism \(f:V\to W\) likewise has \(F_W=fF_Vf^{-1}\), so
\[
\det(TI-F_W)=\det(f(TI-F_V)f^{-1})=\det(TI-F_V).
\tag{DWR13.2}
\]
These are useful faithful maps, but neither creates the weight estimates DWR5–DWR10. The parityless supporting point can carry the coefficient calculation while remaining distinct from all its arithmetic elements. The role of the coefficient zero is different: any additive coefficient isomorphism sends zero vector to zero vector, since \(f(0)+f(v)=f(v)\). This uses addition in the coefficient stalk and makes no statement about addition on the supporting \(\tau\).

For a Frobenius-equivariant quotient \(V\twoheadrightarrow Q\) with kernel \(K\), choose a basis adapted to \(K\). The matrix is block triangular, proving
\[
\det(1-tF_V)=\det(1-tF_K)\det(1-tF_Q),
\qquad\operatorname{Tr}(F_V^m)=\operatorname{Tr}(F_K^m)+\operatorname{Tr}(F_Q^m).
\tag{DWR13.3}
\]
Thus the user's global quotient proposal has an exact trace receiver: its kernel contributes a specified factor, which has to be retained in the complete return comparison. Deligne's local invariant-cycle argument DWR11 controls a quotient by proving that its obstruction lies in disjoint weights. That is a closer mathematical target than identifying a support point with a numerical zero.

## DWR14. What has actually transferred

The complete-return measure has now been identified with the measure used in Deligne's own original-zeta example, with the inverse (DWR12.4) restoring the unit and every repetition. This identifies the scalar analytic input to his chapter-II method exactly. It does not assert that his finite-field coefficient sheaves and the programme's entire cohomology are already isomorphic.

The global weight-control proof itself has been reconstructed through explicit maps: tensor and exterior powers, inertia invariants, nilpotent primitive pieces and their duals, vanishing cycles, blowup pullback and trace, Künneth, Leray, and the dual cohomology pairing. Its removal of all excess weight is (DWR8.5)–(DWR8.7), followed by (DWR9.1). Neither a selected pair of primes nor a bounded calculation is used to infer the result.

For the programme, the remaining unconstructed comparison is the coefficient object and its geometric operations realizing those particular maps for the original zeta spectrum. This note has not proved their existence, assumed them as purity axioms, or declared the RH problem solved. It has proved the return-measure map, reconstructed the source proof that the proposed transfer must carry, and identified the quotient-kernel determinant and duality data that must be computed on the existing programme objects next.
