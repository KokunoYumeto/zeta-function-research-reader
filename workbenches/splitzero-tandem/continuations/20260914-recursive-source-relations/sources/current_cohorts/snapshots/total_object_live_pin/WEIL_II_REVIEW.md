# Independent review of the Weil II boundary amplification

Date: 2026-09-13. Read all 40 lines of `WEIL_II_AMPLIFICATION.md`, then reread the complete corrected source including the additions at lines 5 and 26. Final reviewed source SHA-256: `E20D120920B3A9FA6D7AB831FD6E4834D51874DBED4E64D17B3573E92FEBBC93`. The reviewer did not edit that source; the root agent added the definitions recorded below. The reviewed primary-source transcriptions are `output/Deligne_Weil_II_S20_LaTeX/typed_latex/S20_EN_article_text.txt` and `S20_FR_article_text.txt`: Lemma 1.8.1 and its complete proof at lines 1073–1095, and Corollary 1.4.3 at line 676. The adjoining inputs 1.3.5, 1.4.1–1.4.2, 1.4.6–1.4.7 were checked where needed to verify applicability. No étale foundations were reproved.

## Verdict

The pole argument, its upper-only conclusion, the invariant-tensor injection, and the finite integer choice are correct and agree with both current transcriptions. The denominator is correctly \(H_c^2\). Both initially missing definitions are now present and verified: the \(\ell\)-adic coefficient convention with \(\ell\ne\operatorname{char}\mathbb F_q\) and the fixed \(\iota\), and the local generic fibre \(W\) with inertia \(I_x\) and its boundary-stalk identification. No corrections or outstanding definitions remain in this bounded review. The source-to-Corollary 1.4.3 bridge is recorded below in full finite-curve form.

## Hypotheses and the cohomological pole exclusion

The source assumes the conventions of 0.7 (English lines 186–190): \(q\) is a power of a prime distinct from \(\ell\); the coefficient objects are the \(\overline{\mathbb Q}_\ell\) sheaves of the article; the chosen \(\iota:\overline{\mathbb Q}_\ell\to\mathbb C\) is fixed. The curve is smooth and geometrically irreducible, the complement is finite, and \(\mathcal F_0\) is lisse on the nonempty open curve and pointwise \(\iota\)-pure of weight \(\beta\). Lemma 1.8.1 does not require \(\beta\) to be an integer, tame local monodromy, semisimplicity, or equality of the boundary weights. The argument concerns this fixed \(\iota\), not an unassumed purity condition for every embedding.

To make the curve affine, remove a closed point of \(U_0\) from both \(X_0\) and \(U_0\), leaving the original boundary points and their local stalks unchanged. This is the reduction in the source at line 1079. On the resulting affine curve, a compactly supported section of \(j_*\mathcal F\) has finite support. Its restriction to \(U\) is a compactly supported section of a lisse sheaf on an affine connected curve, hence is zero by 1.4.1(a). A section of \(j_*\mathcal F\) is determined by this restriction, so the original section is zero. Thus \(H_c^0(X,j_*\mathcal F)=0\), justifying the missing degree-zero denominator in DII1 even though \(j_*\mathcal F\) need not itself be lisse on \(X\).

Corollary 1.4.3 is stated for a lisse sheaf. Its application here is through
\[
H_c^2(X,j_*\mathcal F)\simeq H_c^2(U,\mathcal F).
\]
This is exactly 1.4.1(b), English lines 659–663, specialized to the finite boundary. Equivalently, in the exact sequence \(0\to j_!\mathcal F\to j_*\mathcal F\to\mathcal Q\to0\), the sheaf \(\mathcal Q\) has finite support. Its positive-degree geometric compactly supported cohomology vanishes, so the long exact sequence gives the displayed Frobenius-equivariant isomorphism.

Pointwise purity forces every determinantal weight of \(\mathcal F_0\) to be \(\beta\), as stated immediately after Definition 1.3.5, English lines 544–546. Explicitly, an invariant filtration of a local Frobenius matrix makes its characteristic polynomial the product of the characteristic polynomials on the subquotients. Each constituent's local eigenvalues therefore has modulus \(N(x)^{\beta/2}\). The determinant of a rank-\(r\) constituent has modulus \(N(x)^{r\beta/2}\), and dividing its weight by \(r\) gives \(\beta\). Corollary 1.4.3 now says that every eigenvalue on the above \(H_c^2\) has weight \(\beta+2\). Every denominator root is consequently on the circle
\[
|t|=q^{-(\beta+2)/2},
\]
so the right side of DII1 has no pole in the open disc. No boundary-purity assertion was assumed to establish this exclusion.

## Pole noncancellation and the one-sided bound

By 1.4.6 on the one-dimensional open curve, pointwise weight \(\beta\) makes its Euler product holomorphic and nowhere zero on \(|t|<q^{-(\beta+2)/2}\). The remaining finite product is exactly \(1/P(t)\), where
\[
P(t)=\prod_{x\in|S_0|}\det(1-\iota F_x\,t^{\deg x},(j_*\mathcal F_0)_{\bar x}).
\]
It has constant term one. Every root of \(P\) gives a genuine pole of \(1/P\), with its full multiplicity; the numerator cannot cancel it. DII1 and division by the holomorphic nowhere-zero open factor therefore prohibit every such root in the open disc. Cancellation between the numerator and denominator of the cohomological expression is irrelevant to this conclusion: its quotient is already holomorphic in the disc, and the finite boundary product has no numerator zero.

Frobenius acts invertibly, so a boundary eigenvalue \(\alpha\ne0\) yields roots of \(1-\iota\alpha\,t^d\), with \(d=\deg x\ge1\), all of modulus \(|\iota\alpha|^{-1/d}\). Absence of a root in the open disc gives
\[
|\iota\alpha|^{-1/d}\ge q^{-(\beta+2)/2}
\iff |\iota\alpha|\le q^{d(\beta+2)/2}
=N(x)^{(\beta+2)/2}.
\]
With the source's factor-two weight convention, this is exactly DII2, \(w_{N(x)}(\alpha)\le\beta+2\). Roots on the bounding circle are allowed. There is no lower bound in this pole-exclusion step.

## Tensor map, purity, and finite contradiction

For a boundary geometric point \(\bar x\), let \(\bar\eta\) be a geometric generic point of its strict henselian local trait, let \(W=\mathcal F_{\bar\eta}\), and let \(I_x\) be the local inertia group. Then \((j_*\mathcal F)_{\bar x}=W^{I_x}\). The natural map in DII3 is the tensor of the vector-space inclusions \(W^{I_x}\hookrightarrow W\), followed by its factorization through the invariant subspace. Basis extension proves injectivity. Every inertia element fixes every factor in its image. A Frobenius lift normalizes \(I_x\), hence preserves its invariants, and the tensor inclusion commutes with that lift. The induced action on invariants is independent of the chosen lift, since two lifts differ by inertia.

If \(v\in W^{I_x}\) is a nonzero eigenvector of eigenvalue \(\alpha\), choose a linear functional with value one on \(v\). Its \(k\)-fold tensor evaluates to one on \(v^{\otimes k}\), proving that this tensor and its DII3 image are nonzero. Frobenius acts on it by \(\alpha^k\). No semisimplicity or equality \((W^{I_x})^{\otimes k}=(W^{\otimes k})^{I_x}\) is required.

Triangularize each finite Frobenius matrix over the coefficient algebraic closure. The tensor matrix is triangular in the corresponding tensor basis, with diagonal entries the products of the original diagonal entries. Thus all local eigenvalues of \(\mathcal F_0^{\otimes k}\) have modulus \(N(x)^{k\beta/2}\). It is lisse and pointwise pure of weight \(k\beta\), so the already proved DII2 applies to this new sheaf and to the retained eigenvalue \(\alpha^k\). This proves
\[
k\,w_{N(x)}(\alpha)=w_{N(x)}(\alpha^k)\le k\beta+2.
\]
For \(w_{N(x)}(\alpha)=\beta+\varepsilon\), \(\varepsilon>0\), the integer \(k=\lfloor2/\varepsilon\rfloor+1\) is positive and satisfies \(k>2/\varepsilon\), including when \(2/\varepsilon\) is an integer. Hence \(k\varepsilon>2\), contradicting the displayed inequality. This proves exactly the upper boundary bound \(w_{N(x)}(\alpha)\le\beta\). No positive even-exponent restriction is needed here.

## Definition additions verified and closed

Source line 5 now specifies \(\ell\ne\operatorname{char}\mathbb F_q\) and \(\iota:\overline{\mathbb Q}_\ell\to\mathbb C\) in Deligne's convention. Source line 26 now defines \(W=\mathcal F_{\bar\eta}\), its local inertia \(I_x\), and \((j_*\mathcal F)_{\bar x}=W^{I_x}\). Both additions were reread in the final source at the hash above and are correct. They do not alter the proved amplification or require further source edits.
