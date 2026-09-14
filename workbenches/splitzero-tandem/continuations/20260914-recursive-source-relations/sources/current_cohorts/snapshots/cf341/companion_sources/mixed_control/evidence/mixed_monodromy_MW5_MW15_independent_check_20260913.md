# Independent exact check of MW5 and MW11–MW15

Source reviewed in full: `tau_mixed_support_monodromy_filtration_20260913.tex`, with this review confined to its intrinsic filtration formula and tensor chain proof. No source file was edited.

## Verdict

The displayed intrinsic formula MW5 is correct. Its following sentence gives an incorrect unsaturated minimum for sufficiently negative integers j. The corrected minimum is

\[
 t(m,j)=\max\!\left(0,-j,\left\lceil\frac{m-1-j}{2}\right\rceil\right).
\]

This changes no filtration subspace: in the range in which the omitted term matters, the terminal spans in question are both zero. MW11–MW15 have a complete valid tensor-chain argument. A short coordinate explanation of MW15 and an optional direct identification using MW5 are supplied below.

## MW5: all integers, including j below minus m

Keep the original block basis v_0,...,v_{m-1}, with Nv_r=v_{r+1} and Nv_{m-1}=0. For every integer t≥0, write

\[
 S_t=\operatorname{span}\{v_r:t\leq r<m\},
\]

where S_t=0 for t≥m. For i≥0,

\[
 \ker N^{i+1}=S_{\max(0,m-1-i)},\qquad
 \operatorname{im}N^{\max(0,i-j)}=S_{\max(0,i-j)}.
\]

Thus their intersection is S_{f(i)}, where

\[
 f(i)=\max(0,m-1-i,i-j).
\]

For every integer i≥0, f(i)≥0 and f(i)≥−j. Also the sum of the last two affine expressions is m−1−j; since f(i) is an integer at least their maximum, f(i)≥ceil((m−1−j)/2). Consequently f(i)≥t(m,j).

Conversely, set t=t(m,j) and choose the original integer index

\[
 i_*=\max(0,m-1-t).
\]

The inequalities t≥−j and 2t≥m−1−j imply both 0≤t+j and m−1−t≤t+j. Hence i_*≤t+j, while its definition gives m−1−i_*≤t. All three expressions defining f(i_*) are therefore at most t. The lower bound already proved gives f(i_*)=t. This proves the asserted exact minimum, including every negative j.

The terminal spans are nested, so their sum is S_t. To compare it with MW3 without discarding the low-index case, consider the two exhaustive ranges.

* If j≥−(m−1), then m−1+j≥0, so (m−1−j)/2≥−j. Its ceiling therefore dominates −j. Thus t=max(0,ceil((m−1−j)/2)), precisely the least allowable exponent in MW3.
* If j<−(m−1), integrality gives j≤−m. Then t≥−j≥m. Also ceil((m−1−j)/2)≥ceil((2m−1)/2)=m. Both formulas specify the zero terminal span, exactly as MW3 does because its least basis weight is −(m−1).

For an explicit counterexample to the source's literal unsaturated-minimum sentence, m=3 and j=−6 give min f(i)=6, whereas max(0,ceil((m−1−j)/2))=4. Both S_6 and S_4 are zero, explaining why the displayed MW5 identity remains valid.

For a finite direct sum of blocks, kernels and images decompose by blocks. Intersection is coordinatewise, and the sum of the resulting subspaces is coordinatewise. MW5 therefore holds on the original finite packet E_Z. If fN=N'f, then f(ker N^{i+1})⊆ker(N')^{i+1} and f(im N^r)⊆im(N')^r for each r≥0. Applying f to the sum of intersections proves the stated functoriality.

Suggested replacement for the erroneous source prose:

> The exact minimum is max(0,−j,ceil((m−1−j)/2)). If j≥−(m−1), its −j term is redundant. If j≤−m, both this minimum and max(0,ceil((m−1−j)/2)) are at least m and specify the zero span. In both cases the resulting subspace agrees with MW3.

## MW11–MW15: exact tensor-chain verification

The source's endpoint conventions v_{−1}=v_m=0 give, on every original basis vector,

\[
 [H,L]v_r=-2Lv_r,\quad [H,E]v_r=2Ev_r,
\]

and

\[
 [E,L]v_r=((r+1)(m-r-1)-r(m-r))v_r
           =(m-1-2r)v_r=Hv_r.
\]

These formulas remain valid at r=0 and r=m−1 because the omitted endpoint vector is zero. For 0≤r<m−1, the displayed positive coefficients satisfy

\[
 c_{r+1}=(r+1)(m-r-1)c_r.
\]

With the basis orthogonal of squared lengths c_r, this proves L*=E; the diagonal real H is self-adjoint. The same adjoint relations hold for the factorwise sums on a finite tensor product equipped with the specified product form. All operators from different factors commute. The total lowering operator is nilpotent: every term in a multinomial expansion of total degree greater than Σν(mν−1) contains some factor Nν^{mν}=0.

Choose a nonzero eigenvector v for the largest eigenvalue d of H_tot. This eigenvalue exists and is an integer because H_tot is diagonal in the original tensor basis, with integer entries. The relation [H_tot,E_tot]=2E_tot makes E_tot v an eigenvector of eigenvalue d+2 if nonzero; maximality therefore gives E_tot v=0.

The exact induction for the source's MW14 is as follows. Its r=1 case is E_tot L_tot v=dv. If it holds at r≥1, then [E_tot,L_tot]=H_tot and H_tot L_tot^r v=(d−2r)L_tot^r v give

\[
\begin{aligned}
 E_{\rm tot}L_{\rm tot}^{r+1}v
 &=L_{\rm tot}E_{\rm tot}L_{\rm tot}^{r}v
   +H_{\rm tot}L_{\rm tot}^{r}v\\
 &=(r(d-r+1)+d-2r)L_{\rm tot}^{r}v\\
 &=(r+1)(d-r)L_{\rm tot}^{r}v.
\end{aligned}
\]

Nilpotence supplies a largest ℓ with L_tot^ℓv≠0. At r=ℓ+1, MW14 has zero left side and right side (ℓ+1)(d−ℓ)L_tot^ℓv. It follows exactly that d=ℓ, with no positivity estimate or arithmetic purity assumption. For 0≤r≤d the vectors L_tot^rv are nonzero, have pairwise distinct weights d−2r, and are linearly independent. Their span is invariant under H_tot,L_tot,E_tot by the formulas already proved.

For w orthogonal to this span and u in it, the adjoint identities give ⟨L_tot w,u⟩=⟨w,E_tot u⟩=0 and ⟨E_tot w,u⟩=⟨w,L_tot u⟩=0; self-adjointness treats H_tot. Therefore the orthogonal complement is invariant under all three operators. It still has a diagonalizable self-adjoint H_tot, integer spectrum contained in the original one, and nilpotent L_tot. Induction on its dimension decomposes the entire tensor space into the displayed chains.

On a chain of highest weight d and basis w_r=L_tot^rv, L_tot w_r=w_{r+1}. Its weights are d−2r and its length is d+1. The proof of MW5, now applied with m=d+1, identifies its intrinsic nilpotent filtration with the span of weights at most j. Taking the direct sum over the invariant chains identifies the full intrinsic filtration with the H_tot filtration. This provides a direct verification independent of an appeal to uniqueness in Deligne's proposition.

Finally, a vector in the original tensor basis v_{ρ1,r1}⊗⋯⊗v_{ρk,rk} has weight Σν(mρν−1−2rν). Every basis tensor in a summand of the right side of MW15 has factor weights at most jν and therefore total weight at most Σνjν≤j. Conversely, for every original basis tensor of total weight at most j, choose jν=mρν−1−2rν. It then belongs to that exact summand. This proves both inclusions in MW15 with the original tensor coordinates retained.

For each k≥0, the chain has weight k precisely when d−k is even and 0≤k≤d. Then its weight-k basis vector is w_{(d−k)/2}, and L_tot^k sends it to w_{(d+k)/2}, with coefficient exactly one. When weight k is absent, weight −k is absent as well. This proves all required graded isomorphisms and completes the tensor proof.

No numerical computation is used in this verdict. No arithmetic purity estimate is asserted by this review.
