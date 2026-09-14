# Primary-source verification for SPF

The proof module uses explicit source maps and a direct local calculation. The external foundations imported are compact-support base change and projection formula, étale cohomology of a smooth curve, its duality and Euler characteristic formula, and the trace formula. Its Gauss decomposition is proved by the actual power-map projectors and the parameter isomorphism w=az, not inferred just from trace functions.

## Verified primary sources

1. Nicholas M. Katz, *Gauss Sums, Kloosterman Sums, and Monodromy Groups*, Annals of Mathematics Studies 116, Princeton University Press. [Author-hosted full text](https://web.math.princeton.edu/~nmk/Katz-GKM.pdf).
   - Section 2.0.5–2.0.6, printed pp. 26–27: compact-support degree-zero vanishing on an open curve; degree-two cohomology is the Tate-twisted geometric coinvariant representation.
   - Section 2.2: compact-support functor and coefficient compatibility.
   - Section 2.3.1–2.3.3, printed pp. 32–33: Euler–Poincaré and Lefschetz formulas; Frobenius is explicitly the inverse of x↦x^q; degree-one trace occurs with a minus sign.
   - Section 4.0, printed pp. 46–47: the unscaled Gauss sum is sum over nonzero elements of psi(a)chi(a), and its nontrivial-character absolute value is sqrt(q). SPF.28 also proves the absolute-value identity directly.
   - Section 4.3, printed pp. 59–60: additive and multiplicative character sheaves from Lang torsors, their multiplicative tensor law, additive Swan conductor one, and tame Kummer inertia.
   - Section 8.2.3–8.2.4, printed pp. 132–133: the naive Fourier transform is R^1(pr_2)! of the additive-kernel tensor product. SPF uses the parameter source isomorphism directly, without applying an unproved Fourier identification.
2. The Stacks Project, [Section 59.63, tag 0A3J](https://stacks.math.columbia.edu/tag/0A3J): the Artin–Schreier exact sequence with x↦x^p−x. Read via web tool.
3. The Stacks Project, [Section 59.28, tag 03PK](https://stacks.math.columbia.edu/tag/03PK), especially Lemma 59.28.1: the Kummer exact sequence, and the finite étale torsor T^n=f when n and f are invertible. Read via web tool.

## Acquisition and convention audit

The author-hosted Katz PDF was found through web search. The web PDF viewer timed out; the same primary-source URL was then fetched directly with Invoke-WebRequest and read through its local text extraction. It is retained in sources/Katz_GKM.pdf with sources/Katz_GKM.txt. No third-party mathematical source is relied on. Numdam's Laumon article was inspected as a bibliographic lead, but is not used for a mathematical premise here.

The sign convention is fixed independently at four places:

- The χ power-map projector has image λχ inverse and geometric Frobenius trace χ(x).
- H_c^1 has geometric Frobenius eigenvalue −G.
- At a=1/(nu), the Kummer factor is χ inverse in a, hence χ(n)χ(u) in u.
- Over F_(Q^r), −G_r=(−G)^r; the geometric constant factor is not −G^r.

The retained AS factor has numerator bc with ψ=ϑ∘Tr(b·). For c nonzero it is wild, has Swan conductor one on each summand, and is nontrivial by the pole-order argument. For c=0, all n−1 tame character summands are still nontrivial on inertia. The finite cover kills the AS factor by its own torsor, not by omitting it.

## Scope

The specified coefficient map R→F_Q evaluates every coefficient of the full Taylor class upsilon_h=j_h(g/h) and its inverse in the retained m-dimensional remainder basis, along with rho and every other original coefficient. This refers to the finite retained Taylor class, not to adjoining every coefficient of an infinite analytic function. The displayed sheaf uses the given primitive of h. This module never divides the phase by its unit, changes its base value, or constructs a complex zeta zero.
