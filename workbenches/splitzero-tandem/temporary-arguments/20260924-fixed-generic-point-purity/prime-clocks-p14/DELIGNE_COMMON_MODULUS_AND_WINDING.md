# Deligne's exact common modulus and the retained winding characters

24 September 2026. Private continuation. Proof labels D1–D5. This note answers the user's request to retrieve Deligne from GitHub and make the proposed common-distance comparison exact. It retains all original powers of the residue cardinality. It introduces no distance or addition on the user's parityless \(\tau\langle Z_1;\text{no }Z_2\rangle\).

## D1. The retrieved source and the meaning of same

The GitHub file D032_FULL_EN.tex was retrieved at commit 492a44c2938cc6f5e3c41105567492a8fa528c8c of KokunoYumeto/zeta-function-research-reader. Its SHA-256 is 316cbc52349cd6bc2dedbd0a493a530696d367ca0e292fc64ee3c3973327567e. It is a historical English transcription, not Deligne's original author TeX. The current French S20 transcription was read beside it. No original author TeX is available in this indexed edition; the distinction is preserved rather than describing a transcription as an author file. The published article is Pierre Deligne, La conjecture de Weil. II, IHES 52 (1980), 137–252.

Definition 1.2.1 says that an algebraic number \(\alpha\) is pure of weight \(w\), relative to a prime power \(q\), when every complex embedding has
\[
|\iota(\alpha)|=q^{w/2}.
\]
For a sheaf, Definition 1.2.2 applies this statement to Frobenius eigenvalues at every closed point \(x\), with \(q\) replaced by its residue-field size \(N(x)\). Thus the original pointwise formula is
\[
|\iota(\alpha_x)|=N(x)^{w/2}.
\]
A common weight is the same exponent \(w\) throughout this statement. It does not make different residue cardinalities equal. For instance the weight-one radii at residue cardinalities two and three are \(2^{1/2}\) and \(3^{1/2}\). At a fixed finite field and fixed pure weight all the relevant eigenvalues and all their complex conjugates do have one common numerical radius. The radius is a complex absolute value of an eigenvalue; it is not a subtraction of the geometric base point from that eigenvalue.

Keep the symbols separate: \(m\) in the winding source \(T^m\) counts signed turns; \(w\) denotes Deligne's weight; \(i\) below is cohomological degree. None is identified with another merely because all are integer-valued in the relevant instances.

## D2. How the exact circle is obtained, retaining the Tate factor

Here are Deligne's hypotheses and the actual last step of the proof. Let \(X_0\) be smooth of finite type over \(\mathbb F_q\), pure of dimension \(d\). Let \(\ell\) differ from the field characteristic and let \(\mathcal F_0\) be a lisse pure \(\overline{\mathbb Q}_\ell\)-sheaf of weight \(n\). Put \(X=X_0\times_{\mathbb F_q}\overline{\mathbb F}_q\) and let \(\mathcal F\) be its pullback. These are the hypotheses of the cited theorem, not hypotheses asserted for the user's construction.

Deligne 3.3.4 gives weights at most \(n+i\) on
\[
V_c=H_c^i(X,\mathcal F).
\]
The dual sheaf has weight \(-n\). Applying 3.3.4 to it gives weights at most
\[
-n+(2d-i)
\]
on \(W=H_c^{2d-i}(X,\mathcal F^\vee)\). In the geometric Frobenius convention a Tate twist \((d)\) multiplies its eigenvalues by \(q^{-d}\). Poincare duality is the exact Frobenius-equivariant identification
\[
H^i(X,\mathcal F)\cong\bigl(H_c^{2d-i}(X,\mathcal F^\vee)(d)\bigr)^\vee.
\]
Therefore an eigenvalue \(\beta\) on \(W\) produces the eigenvalue
\[
\lambda=(q^{-d}\beta)^{-1}=q^d/\beta
\]
on the dual space. For every complex embedding, the cited upper estimate gives
\[
|\iota(\beta)|\le q^{(-n+2d-i)/2}.
\]
Retaining the whole Tate factor yields
\[
|\iota(\lambda)|
=\frac{q^d}{|\iota(\beta)|}
\ge \frac{q^d}{q^{(-n+2d-i)/2}}
=q^{(n+i)/2}.
\]
This proves the lower weight assertion 3.3.5 from the upper assertion and the stated duality theorem.

Now take the actual Frobenius-equivariant comparison map
\[
u:H_c^i(X,\mathcal F)\longrightarrow H^i(X,\mathcal F)
\]
and its image \(I\). This image is simultaneously a quotient of \(V_c\) and a subspace of \(H^i\). For an invariant subspace, a basis beginning with a basis of the subspace makes the matrix of Frobenius block triangular; hence its characteristic polynomial is the product of those on the subspace and quotient. It follows that eigenvalues of \(I\), with their algebraic conjugates, satisfy both the cited upper estimate and the derived lower estimate. Thus each satisfies
\[
q^{(n+i)/2}\le |\iota(\alpha)|\le q^{(n+i)/2},
\qquad
\boxed{|\iota(\alpha)|=q^{(n+i)/2}.}
\]
This is Corollary 3.3.6. If \(X_0\) is proper, compactly supported and ordinary cohomology coincide, so the image is the whole cohomology. For constant coefficients of weight zero and degree one, the radius is exactly \(q^{1/2}\). No division by \(q^{1/2}\) has replaced that eigenvalue.

The equality has therefore been derived on a specified image of a specified cohomological map. The construction of that map and the two controls are the mechanisms, rather than an assumption that every noncentral datum has a common distance.

## D3. The product mechanism behind the upper control

The preceding use of 3.3.4 is a use of Deligne's theorem, not a claim to have reproduced its entire proof here. The relevant part of his curve argument was also read directly in the current French text, 3.2.4–3.2.15. Here is its exact numerical mechanism and the source geometry it uses.

For a smooth curve and a lisse sheaf of pointwise weight zero, 3.2.4 proves, for every integer \(k\ge0\),
\[
w_q(\alpha)\le1+2^{-k},
\qquad
w_q(\alpha)=\frac{2\log|\iota(\alpha)|}{\log q}.
\]
He forms \(S_0=X_0\times X_0\), \(V_0=U_0\times U_0\), and the external tensor product \(\mathcal G_0=\mathcal F_0\boxtimes\mathcal F_0\). A Lefschetz pencil, its vanishing cycles, and the local monodromy filtration control the Leray terms. At the decisive induction step he has Frobenius-equivariant inclusions
\[
H_c^1(U,\mathcal F)\otimes H_c^1(U,\mathcal F)
\hookrightarrow H_c^2(V,\mathcal G)
\hookrightarrow H_c^2(\widetilde V,\pi^*\mathcal G).
\]
The target weight bound is \(2+2^{-k}\). If \(\alpha\) is a source eigenvalue, a nonzero eigenvector tensored with itself gives eigenvalue \(\alpha^2\) in the tensor square. Over a field its pure tensor is nonzero: choose a linear functional nonzero on the eigenvector and apply its tensor square. The injections preserve that eigenvalue. Therefore
\[
2w_q(\alpha)=w_q(\alpha^2)\le2+2^{-k},
\qquad
w_q(\alpha)\le1+2^{-(k+1)}.
\]
Holding for every \(k\), these inequalities imply \(w_q(\alpha)\le1\): any larger value differs from one by a positive amount, and some \(2^{-k}\) is smaller than that amount. For pointwise weight \(\beta\), the original bound is \(\beta+1\). Deligne applies it to \(\mathcal F_0^\vee(1)\), whose weight is \(-\beta-2\); the duality pairing then gives
\[
w_q(\alpha^{-1})\le(-\beta-2)+1,
\qquad w_q(\alpha)\ge\beta+1.
\]
Together the two results give weight exactly \(\beta+1\).

This is weight control driven by product geometry and duality. It is not a finite numerical scan. This note uses the source's geometric lemmas, rather than claiming to have reconstructed its monodromy and vanishing-cycle proofs in full.

## D4. The precise same-modulus receiver for the retained winding

Use the full signed generic group and action proved in W1–W2 of WINDING_PARITY_AND_INTEGER_SPECTRUM.md. Its actual signed complex-character space is
\[
\mathcal C=\{\chi_{z,j}:z\in\mathbb C^\times,\ j\in\{i,-i\}\},
\qquad
\chi_{z,j}(T^mJ^k)=z^m j^k.
\]
Here \(k\pmod4\) retains both the imaginary branch and the sign. Define the space of bounded-winding evaluations inside this actual character space by
\[
\mathcal U=\left\{\chi\in\mathcal C:\sup_{m\in\mathbb Z}|\chi(T^m)|<\infty\right\}.
\]
This is a space of evaluation maps, not a boundedness axiom placed on \(\tau\). Its definition is independent of changing the source lift from \(T\) to \(TJ^c\) or to its inverse, because \(|j^c|=1\) and both signs of \(m\) occur.

Write \(r=|z|>0\). Then \(|\chi(T^m)|=r^m\). If \(r>1\), positive powers are unbounded; if \(r<1\), negative powers are unbounded; if \(r=1\), every power has modulus one. This proves the exact classification
\[
\boxed{\mathcal U=\{\chi_{z,j}:|z|=1,\ j=\pm i\}.}
\]
For every \(g=\epsilon^aT^mJ^b\in G\) and every \(\chi\in\mathcal U\),
\[
|\chi(g)|=|(-1)^a z^m j^b|=1.
\]
The full pointed monoid has a faithful receiver in functions on \(\mathcal U\):
\[
E:G\sqcup\{0\}\longrightarrow\operatorname{Map}(\mathcal U,\mathbb C),
\qquad E(g)(\chi)=\chi(g),\quad E(0)=0.
\]
It preserves multiplication and the absorbing element by the character law. To prove injectivity, suppose \(E(T^mJ^k)=E(T^{m'}J^{k'})\). Evaluate first at \((z,j)=(1,i)\); this gives \(k=k'\pmod4\). Thus \(z^{m-m'}=1\) for every \(|z|=1\). If \(a=m-m'\ne0\), choose \(z=\exp(i\pi/a)\); then \(z^a=-1\), a contradiction. Hence \(m=m'\). Finally the zero function differs from each nonabsorbing image because those images have modulus one at every character. All integer winding data and all four branch/sign states therefore survive in this receiver despite its common modulus.

The source involution preserves \(\mathcal U\) by
\[
\alpha_{\mathcal C}(z,j)=(-z^{-1},-j).
\]
The receiver is exactly equivariant:
\[
E(A(g))(\chi)=\chi(A(g))=E(g)(\chi\circ A).
\]
Every sign-preserving commuting lift \(f_{n,c,b}\) from W5 also preserves \(\mathcal U\), because its character action is
\[
(z,j)\longmapsto(z^n j^c,j^b),
\]
whose spatial coordinate has modulus \(|z|^n=1\), while odd \(b\) retains \(j^b\in\{i,-i\}\). On the source's quotient sphere the odd Frobenius branches remain \(z^n\) and \(-1/z^n\), both preserving this circle. The full character space \(\mathcal C\), its inclusion \(\mathcal U\hookrightarrow\mathcal C\), and its unrestricted radii are retained; no rescaling turns an arbitrary source character into a unit character.

This proves a substantive part of the user's geometric picture: all full winding integers can be retained faithfully while their evaluated values have the same modulus. The property is realized by the precisely identified bounded-winding character space. The absence of a parity label at the fixed base point did not, by itself, establish that every arithmetic spectral receiver is this space.

## D5. Exact comparison with purity and limits of the result

The statement in D4 concerns values of all group elements under a family of multiplicative characters. Deligne's statement concerns eigenvalues of a particular Frobenius action on one cohomological degree, including every algebraic conjugate and the full residue-cardinality factor. The following exact formula connects repetition with his modulus law without discarding that factor. For an eigenvalue \(\alpha\) of pure weight \(w\) relative to \(q\), iteration \(r\) gives
\[
|\iota(\alpha^r)|=q^{rw/2}=(q^r)^{w/2}.
\]
Thus the weight remains \(w\) when the base finite field is extended to cardinality \(q^r\), while the original numerical radius changes. By comparison, winding evaluation has \(|\chi(T^m)|=|z|^m\). Both preserve the full exponent; a constant numerical radius for all windings corresponds to the special unit-character sector, not to dropping \(q^{w/2}\) from Deligne's formula.

The arithmetic reconstruction W1–W6 and the faithful common-modulus receiver D4 are now proved. No cohomological realization identifying this receiver with the eigenvalues detecting zeros of the original Riemann zeta function has been derived here. Consequently no RH conclusion is claimed. Neither the integer spectrum nor the common-modulus construction is discarded because this last identification is absent.

## Source comparison corrections retained in the reading record

The fetched GitHub historical English witness compresses several proof passages. In its lines 2064–2066 it writes the polynomial \(\det(1-Ft)\) and then assigns its roots the eigenvalue radius \(q^{i/2}\). The current French 3.3.9 instead uses \(\det(t\,1-F^*)\), whose roots are the eigenvalues and correctly have that radius. These two polynomials have reciprocal roots: \(\det(1-tF)=\prod_j(1-t\alpha_j)\), so its roots are \(\alpha_j^{-1}\), of modulus \(q^{-i/2}\). This follows directly by factoring the characteristic polynomial over an algebraic closure and preserves all multiplicities. The source file has not been silently rewritten; the corrected receiving formulas here use the current French statement.

The historical English 3.2.4 prints strict inequalities where the current French 3.2.4, 3.2.11–13 use non-strict inequalities. D3 retains the current French inequalities. The English compressed 3.2.7 calls the external tensor product itself real; the French proof first adjoins its dual by the direct sum \(\mathcal G_0\oplus\mathcal G_0^\vee\). D3 does not replace that source construction with the compressed assertion. The current French, not the historical English shortening, governs these comparisons.

Reading coverage: GitHub English lines 116–145, 572–622 and 1939–2110; current French S20 lines 477–541, 2088–2227 and 2221–2308. D2's Tate-factor calculation and D4's faithful character receiver were independently derived by a mathematical agent. This is a reading of the named passages, not a claim of rereading all Weil II.

Public original identity: https://www.numdam.org/item/PMIHES_1980__52__137_0/

Pinned GitHub transcription: https://github.com/KokunoYumeto/zeta-function-research-reader/blob/492a44c2938cc6f5e3c41105567492a8fa528c8c/workbenches/splitzero-tandem/continuations/20260919-observation-responses-first-allocation/prior_intakes/supporting_sources/D032_FULL_EN.tex
