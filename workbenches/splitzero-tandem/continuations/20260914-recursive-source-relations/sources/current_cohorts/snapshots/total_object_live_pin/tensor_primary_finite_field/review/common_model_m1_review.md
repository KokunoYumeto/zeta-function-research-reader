# Review of the shared integral model and the rank-one exception

Parent task (verbatim):

> Final new proof TPF.36–50 now written in main tensor_primary_finite_field.tex: exact terminal dictionary, scalar in charp coefficient module, stage-domain restriction, and shared B=Z[ζ_N,1/N] model with M_B=B[y]dy/y^mB[y]dy, projectors, two basechanges and canonical isotypic reconstruction of actual Ql Gauss lines. Please review this bounded addition; note M_B is NOT Kahler differentials of truncated algebra. Root also requests m1 exception, I am appending: N2,Q=Q0, gamma=−chi(2)G, gamma²=chi(−1)Q; c!=0,k=2pr invariant eigen=(chi(−1)Q)^(pr), original K0 scalarunit survives actual specialization. Complex rank1 line S=kρ, a>0 actiona^(kρ); anynonzeroT from complex Gauss model toactual arithmeticline obeys A_a T=(a^(kρ)/gamma^k) T Fr. No canonicalcomparison claimed. Can independentlycheck new common-model maps and exactm1formulas beforefinalseal.

Read in full: the updated TPF.36–50 source, including the added domain restriction before TPF.41. The preceding terminal review covers the exact signs and scalar. The present review checks the common integral representation and the rank-one exception.

## 1. Projectors and their exact integral module

Put
\[
B=\mathbf Z[\zeta_N,1/N],\qquad
C_N=\langle\gamma:\gamma^N=1\rangle,\qquad
e_j=\frac1N\sum_{a=0}^{N-1}\zeta_N^{-ja}\gamma^a.
\]
The finite geometric sum gives
\(e_i e_j=\delta_{ij}e_j\), \(\sum_j e_j=1\), and
\(\gamma e_j=\zeta_N^j e_j\).
In particular \(Be_j\) is free of rank one over \(B\): its generator \(e_j\) is nonzero, and multiplication \(a\mapsto ae_j\) is injective because the coefficient of \(\gamma^0\) is \(a/N\).

The marked ambient-form quotient
\[
M_B=B[y]\,dy/y^mB[y]\,dy
\]
has the free basis \(y^{j-1}dy\), \(1\le j\le N-1\).
Its action is \(\gamma(y^{j-1}dy)=\zeta_N^j y^{j-1}dy\).
Therefore the map
\[
\bigoplus_{j=1}^{N-1}Be_j\longrightarrow M_B,\qquad
\sum_j a_j e_j\longmapsto\sum_j a_j y^{j-1}dy
\]
is a \(B[C_N]\)-isomorphism. Its explicit inverse extracts the coefficients in this displayed basis and sends \(y^{j-1}dy\) to \(e_j\).
No relation obtained by differentiating \(y^m=0\) is imposed: this is not \(\Omega^1_{(B[y]/y^m)/B}\).

For the ordered tensor, the tensor product of the specified maps has inverse the tensor product of these coefficient-extraction inverses. The simultaneous \(e_0\) acts on a tuple by the scalar
\[
\frac1N\sum_{a=0}^{N-1}\zeta_N^{a(j_1+\cdots+j_k)},
\]
which equals one if the displayed sum is divisible by \(N\), and zero otherwise. Thus the claimed terminal character and all tuple projector multiplicities remain exact in this common module.

## 2. Both ring maps are well defined

Let \(\zeta_L\) and \(\zeta_\ell\) be the specified primitive \(N\)th roots.
The map \(B\to\overline{\mathbf Q}_\ell\), \(\zeta_N\mapsto\zeta_\ell\), is the cyclotomic evaluation in characteristic zero, with \(N\) invertible.

For \(B\to L\), the identity
\(X^N-1=\prod_{r\mid N}\Phi_r(X)\) remains valid after reduction. A root of \(\Phi_r\) is a root of \(X^r-1\). Hence a primitive \(N\)th root in \(L\) cannot be a root of \(\Phi_r\) for \(r<N\). The product identity therefore forces \(\Phi_N(\zeta_L)=0\). Since \(p\nmid N\), the required inverse of \(N\) exists. This proves the stated finite-field ring map without a map from \(L\) to the characteristic-zero coefficient field.

The connection to the actual coefficient domain is the exact map
\[
R\otimes_{\mathbf Z}B\longrightarrow L,\qquad
r\otimes b\longmapsto\alpha(r)\iota_p(b).
\]
It is balanced over \(\mathbf Z\), additive, and multiplicative on elementary tensors, so the universal property gives the ring map. It introduces no inverses beyond the given domains.

If a larger stage inverts \(p\), it has no extension of this coefficient map: evaluating \(p\cdot p^{-1}=1\) would give \(0=1\). The updated TPF wording correctly treats this as absence of a map, not as an image of a coefficient equal to zero.

## 3. Canonical reconstruction of the actual Gauss lines

Let \(W_\ell\) be the stated actual fibre at \(u=1\), with the original additive factor explicitly tensored by its dual, and let its cyclic action be the ordinary source pullback \(\gamma=D_{\zeta_L}^{-1}\).
Then the image of the integral projector is
\[
\frac1N\sum_{a=0}^{N-1}\zeta_\ell^{-ja}D_{\zeta_L}^{-a}
=\frac1N\sum_{a=0}^{N-1}\zeta_\ell^{ja}D_{\zeta_L}^{a}
=e_{\chi_*^j}^{\rm SPF}.
\]
The middle equality reindexes the finite sum by \(a\mapsto-a\), and the last equality is the original SPF definition.
Thus its image is exactly the actual Gauss line
\(H_j=e_{\chi_*^j}^{\rm SPF}W_\ell\), with its full scalar
\(-\chi_*^j(N)G_L(\chi_*^j,\psi)\).

Write \(E=\overline{\mathbf Q}_\ell\). With identity Frobenius on the first character factor, the isotypic reconstruction is
\[
\Theta:\bigoplus_j (Be_j\otimes_B E)\otimes_E H_j^{\rm triv}
\longrightarrow W_\ell,\qquad
(ae_j)\otimes h\longmapsto ah.
\]
An explicit inverse is
\[
\Theta^{-1}(w)=\sum_{j=1}^{N-1}
e_j\otimes e_{\chi_*^j}^{\rm SPF}w.
\]
Indeed \(\Theta\Theta^{-1}(w)=w\) by completeness of the SPF projectors. On a pure tensor \((ae_j)\otimes h\), orthogonality shows that the reverse composition is exactly \((ae_j)\otimes h\). This proves an actual inverse without choosing a numerical basis of \(H_j\).

The map is equivariant for the deck action because that action on both corresponding summands is multiplication by \(\zeta_\ell^j\). It is equivariant for \(\operatorname{Fr}_Q\) because this Frobenius commutes with the projectors over the splitting field, is assigned the identity on \(Be_j\otimes_B E\), and retains its actual action on \(H_j^{\rm triv}\). The word “triv” removes only the cyclic group action, not Frobenius. These are exactly the actions required in TPF.50.

This map reconstructs \(W_\ell\) from the common character modules tensored with their actual one-dimensional multiplicity spaces. It does not choose an isomorphism from an unweighted character module to a Gauss line. Thus it supplies the asserted canonical correspondence without assuming the comparison that the source has expressly declined to assert.

## 4. Exact rank-one Gauss calculation

Let \(m=1\), \(N=2\), \(p>2\), and \(Q=Q_0\).
There is one nontrivial character, the quadratic character \(\chi\).
Put
\[
G=\sum_{x\in\mathbf F_Q^\times}\chi(x)\psi(x),\qquad
\gamma=-\chi(2)G.
\]
The substitution \(y=tx\) in the product of the two sums gives
\[
\begin{aligned}
G^2
&=\sum_{t\ne0}\chi(t)\sum_{x\ne0}\psi((1+t)x)\\
&=\chi(-1)(Q-1)-\sum_{\substack{t\ne0\\t\ne-1}}\chi(t)\\
&=\chi(-1)(Q-1)+\chi(-1)
=\chi(-1)Q.
\end{aligned}
\]
The first line uses \(\chi(x)^2=1\). The inner sum is \(Q-1\) at \(t=-1\), and \(-1\) otherwise; the last line uses \(\sum_{t\ne0}\chi(t)=0\).
As \(\chi(2)^2=1\), this proves the exact identity
\[
\boxed{\gamma^2=\chi(-1)Q.}
\tag{CM.1}
\]
No root choice or normalization of a Gauss sum has occurred.

For \(c\ne0\), the invariant criterion is \(2p\mid k\).
Writing \(k=2pr\), \(r\ge1\), the one-dimensional invariant space has exactly
\[
\boxed{\operatorname{Fr}_Q=\gamma^k
=(\chi(-1)Q)^{pr}.}
\tag{CM.2}
\]
The sign \(\chi(-1)^{pr}\) is retained. The characteristic-zero eigenvalue is nonzero.

The original marked scalar has \(K=k(m-1)=0\), hence
\(C_{h_0,k}=u_0^k\).
When \(u_0\) and its inverse are in the actual coefficient domain, their product specializes to one, so
\(\alpha(u_0)^k\ne0\). Thus the factorial obstruction present for \(m\ge2\) does not occur here. This proves survival of this exact scalar; it asserts nothing about an additional, unspecified scalar or about a stage outside the domain of \(\alpha\).

## 5. All actions in the rank-one comparison identity

Choose a complex embedding of the number field generated by the finite character values and the Gauss sum, and write
\(\lambda=\iota(\gamma^k)\).
Let \(G_k^{\mathbf C}\) be the resulting one-dimensional complex Gauss model with \(\operatorname{Fr}=\lambda I\).

On the original complex arithmetic coefficient line, multiplication by \(s\) in \(\mathbf C[s]/(s-\rho)\) is multiplication by \(\rho\). The ordered sum on the \(k\)-fold tensor is therefore
\[
S=k\rho\,I,\qquad
A_a=\exp((\log a)S)=\exp(k\rho\log a)\,I,\qquad a>0.
\]
Here \(\log a\) is the real logarithm. No logarithmic branch is implicit.
For every chosen nonzero complex-linear map \(T:G_k^{\mathbf C}\to L_{\rm ar}\), one has
\[
\boxed{
A_aT=\frac{\exp(k\rho\log a)}{\lambda}\,T\operatorname{Fr}.
}
\tag{CM.3}
\]
Both sides act on each vector by the same scalar times its image under \(T\); this proves the identity and all its domains. The scalar \(\lambda\) is nonzero by (CM.1).
Such a map is an isomorphism of one-dimensional complex vector spaces, but no particular map is made canonical or assumed to intertwine the two operators.

For \(a=Q\), the exact discrepancy is
\[
A_QT-T\operatorname{Fr}=(Q^{k\rho}-\lambda)T,\qquad
\left|\frac{Q^{k\rho}}{\lambda}\right|
=Q^{k(\operatorname{Re}\rho-\frac12)}.
\tag{CM.4}
\]
For the invariant case \(k=2pr\), exact intertwining holds precisely when
\[
\operatorname{Re}\rho=\frac12,\qquad
\exp\!\bigl(i k\,\operatorname{Im}\rho\,\log Q\bigr)
=\chi(-1)^{pr}.
\tag{CM.5}
\]
Necessity follows by comparing absolute values and then phases. Conversely these two equalities give \(Q^{k\rho}=\lambda\), so (CM.4) vanishes.
Thus purity of the finite eigenvalue alone does not give an intertwiner; the actual discrepancy and both equations have been computed.

Finally, \(p\mid k\) makes the image of \(k\rho\) vanish in the characteristic-\(p\) coefficient field. It does not make the original complex number \(k\rho\) zero. The integer \(k=2pr\) remains in every tensor count, Gauss exponent, and complex exponential.

The second independent reviewer confirmed (CM.1)–(CM.5), including their signs and coefficient-field qualification. No mathematical error was found in the reviewed shared-model formulas.

## Final source receipt

The final main manuscript has tags TPF.1–55 and SHA256
5c2fa0e144f74aea4f21604e986a36fd8b5f37ee4e8235a36a605b49eba32b95.
I read its final multiplicity-one subsection TPF.51–55 in full and verified the explicit identity Frobenius added before TPF.50.

The manuscript's conjugate-Gauss proof of TPF.52 is correct: quadratic character values are real, conjugating the additive character replaces its argument by its negative, and substitution gives
\(\overline G=\chi(-1)G\). Together with \(G\overline G=Q\), this gives the same exact square identity as (CM.1). The original minus sign and \(\chi(2)\) both square to one, with neither omitted from the underlying definition.

TPF.53 keeps the \(c\ne0\) degree \(k=2pr\), the nonzero retained unit scalar, the \(c=0\) even-degree case, and the sign of the Gauss eigenvalue correctly. TPF.54–55 specify the complex source and target lines, the embedding of the cyclotomic number field, the positive real dilation parameter and its logarithm, and the exact ratio. Every displayed formula agrees with (CM.2)–(CM.4).

Final review outcome: no mathematical error found; the previously requested explicit Frobenius action has been supplied. No additional manuscript expansion is requested.
