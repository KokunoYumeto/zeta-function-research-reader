# Exact check of the length-two filtered extension

This review checks the stated formulas independently, retaining the ordered original basis (1,u) of V=C[u]/(u²). The full parent TeX had not yet appeared at the initial calculation; any later source-specific verdict is recorded separately.

Fix q>1 and a>0, with q^ρ=exp(ρ log q) and a^ρ=exp(ρ log a), using real logarithms. Let N be multiplication by u, K=Cu, Q=V/K, i:K→V the inclusion, and p:V→Q the quotient. In the ordered basis (1,u),

\[
 N=\begin{pmatrix}0&0\\1&0\end{pmatrix},\quad
 F_2=\begin{pmatrix}q^{\rho+1/2}&0\\0&q^{\rho-1/2}\end{pmatrix},\quad
 A_a=a^\rho\begin{pmatrix}1&0\\\log a&1\end{pmatrix}.
\]

These formulas include every term, since N²=0. The original arithmetic action is unchanged.

## The strict sequence with induced filtrations

The centered nilpotent filtration on V is

\[
 M_jV=\begin{cases}
 0&j<-1,\\ K&-1\leq j<1,\\ V&j\geq1.
 \end{cases}
\]

The induced filtrations are M_jK=0 for j<−1 and K for j≥−1, and M_jQ=0 for j<1 and Q for j≥1. Thus K has its specified degree −1 and Q its specified degree +1. Direct inspection of the three ranges above gives

\[
 i(M_jK)=i(K)\cap M_jV,\qquad p(M_jV)=M_jQ
\]

for every integer j. Therefore 0→K→V→Q→0 is a strict exact sequence of filtered vector spaces. The induced endomorphisms N_K,N_Q are zero. The actions induced by F_2 are exactly

\[
 F_K=q^{\rho-1/2},\qquad F_Q=q^{\rho+1/2},
\]

and those induced by A_a are A_{a,K}=A_{a,Q}=a^ρ. Both i and p intertwine N, F and every original A_a. Each action preserves the indicated filtrations.

## The exact twisted nilpotent map

Let T_q=Ct be a one-dimensional space with filtration degree −2, added action F_T(t)=q^−1t, and original arithmetic action A_{a,T}(t)=t. Define

\[
 \overline N:Q\otimes T_q\longrightarrow K,\qquad
 \overline N(p(v)\otimes t)=Nv.
\]

If v is replaced by v+cu, its image under N is unchanged because N(u)=0. Hence this is well-defined. It sends [1]⊗t to u and is a linear isomorphism. The domain has filtration degree 1−2=−1, equal to that of K, so it is a strict filtered isomorphism. Moreover

\[
 \overline N((F_Q\otimes F_T)([1]\otimes t))
 =q^{\rho+1/2}q^{-1}u
 =F_K(\overline N([1]\otimes t)),
\]

and

\[
 \overline N((A_{a,Q}\otimes A_{a,T})([1]\otimes t))
 =a^\rho u
 =A_{a,K}(\overline N([1]\otimes t)).
\]

This proves the specified types, degree and both equivariances exactly. On V itself,

\[
 F_2NF_2^{-1}=q^{-1}N,
\]

with the same sign and exponent as the twisted map.

## Relative filtration for W=M

Set W=M on the same original V. Then N preserves W because it lowers its index by two. The only nonzero W-graded spaces are gr^W_{−1}V=K and gr^W_1V=Q. On each, the endomorphism induced by N is zero: N(K)=0 and N(V)⊂K.

The filtration induced by M on gr^W_wV is concentrated in degree w. Explicitly its j-th step is zero for j<w and the whole space for j≥w, because W=M and the induced filtration is

\[
 ((M_jV\cap W_wV)+W_{w-1}V)/W_{w-1}V.
\]

Consequently, for every r≥0,

\[
 N^r:\operatorname{gr}^{M}_{w+r}\operatorname{gr}^{W}_w V
       \longrightarrow
       \operatorname{gr}^{M}_{w-r}\operatorname{gr}^{W}_w V
\]

is the identity when r=0 and an isomorphism between zero spaces when r>0. Also NM_jV⊂M_{j-2}V was computed directly above. These are precisely the relative nilpotent filtration requirements, and establish M as a relative filtration for this specified W. This calculation does not remove the nonzero cross-constituent map: it is retained exactly by the isomorphism Nbar above.

If K and Q are instead each given their separate centered nilpotent filtration for N=0, their unique nonzero graded degree becomes 0. Retaining V with its original M, i and p remain filtration preserving, but neither is strict: at j=−1,

\[
 i(M_{-1}^{\mathrm{centered}}K)=0
 \ne i(K)\cap M_{-1}V=K,
\]

and at j=0,

\[
 p(M_0V)=0\ne M_0^{\mathrm{centered}}Q=Q.
\]

Thus this exact repair uses the induced constituent degrees −1 and +1; it must not relabel those degrees as separate centered degree 0.

## Exact splitting calculation and category

Every linear section of p has the form

\[
 s_c([1])=1+cu,\qquad c\in\mathbb C.
\]

It satisfies

\[
 (Ns_c-s_cN_Q)([1])=u\ne0.
\]

Hence the extension has no N-equivariant splitting, and no splitting in a category requiring N together with the displayed actions. For any fixed a≠1,

\[
 (A_as_c-s_cA_{a,Q})([1])=a^\rho(\log a)u\ne0,
\]

so there is also no splitting respecting that original arithmetic action, or respecting the full family of actions A_a.

The category must be specified: every s_c is a filtered vector-space section for the induced filtrations, and s_0 is F_2-equivariant. Indeed

\[
 (F_2s_c-s_cF_Q)([1])
 =c\bigl(q^{\rho-1/2}-q^{\rho+1/2}\bigr)u,
\]

which vanishes exactly when c=0. Thus the sequence splits for the added F action alone. This fact and the N-nonsplitting are related by the exact defect Ns_0−s_0N_Q=u, rather than by an unsupported comparison of categories.

Finally the added F and the original arithmetic action generally do not commute:

\[
 F_2A_aF_2^{-1}
 =a^\rho\exp\bigl(q^{-1}(\log a)N\bigr).
\]

This follows by applying F_2 to the full finite exponential. A statement treating both as commuting actions would be false for a≠1; the displayed conjugation is their exact relation.

All checks above are exact, with no numerical test or arithmetic purity assumption.

## Final acceptance of the complete actual TeX, MRE1–MRE33

I subsequently read the COMPLETE actual source `workspace:\work\tau_mixed_relative_extension_control_20260913.tex`, including the added final conjugation calculation MRE33. The accepted source SHA256 is:

`35c080171f5bbc895d3e7f7f89776eabc7d71c5376dbc6be1a1bb0102c30fd73`.

**Verdict: all mathematical claims in this complete version pass this independent review; no algebraic correction is required.** The source explicitly states the category of nonsplitting, proves the separate added-F splitting, fixes the chosen W, and records the full noncommutation identity. The initial caveats in this review are therefore addressed by the actual text.

### General uniqueness proof MRE1–MRE4

The proof is valid for every integer d≥0 satisfying N^(d+1)=0, including a nonminimal nilpotence bound. Here is an independent account of each reduction.

For k>d, the induced N^k is zero, so its asserted isomorphism forces both gr_k and gr_−k to vanish. Finiteness then forces M_d=V and M_−d−1=0. At k=d, N^d consequently induces an isomorphism V/M_d−1→M_−d. Its kernel and image show exactly M_d−1=ker N^d and M_−d=im N^d. When d=0, the filtration is already concentrated in degree zero, so the proof terminates.

For d≥1, 2d≥d+1 proves im N^d⊂ker N^d. Both subspaces are invariant under N, so K_d=ker N^d/im N^d carries the quotient endomorphism. Its d-th power is zero. The induced filtration has zero graded pieces at indices at most −d or at least d, and has exactly the original graded pieces at −d<j<d: for those indices the common quotient im N^d⊂M_j does not change the successive quotients. Therefore all centered isomorphisms for 0≤k<d are inherited, while for k≥d they are between zero spaces. Induction with bound d−1 proves uniqueness of the quotient filtration.

For −d≤j≤d−1, M_j lies in ker N^d and contains im N^d. It is consequently the inverse image of its quotient step under ker N^d→K_d. The two endpoints are already fixed, and the remaining outside steps are 0 or V. This completes uniqueness on V. If N^d=0 already, then K_d=V and the same reduction merely lowers the bound d; it remains a valid induction. Existence and the coefficient-one graded isomorphisms on the original jet blocks are exactly the displayed basis calculation MRE4, and direct sums preserve the calculation.

### Specified-degree translation MRE5–MRE6

The only nonzero W^[b]-graded constituent is at index b. On it, replacing M_j by M_j−b identifies the two relative graded indices b±k with centered indices ±k, giving precisely MRE1. All other W-graded constituents vanish. The lowering inclusion is unchanged after translation. Every integer b is included, and no added arithmetic weight assumption occurs.

### Exact sequence and shifted actions MRE7–MRE22

These agree with the full independent computation above. The shifts M_j^K=C_j+1 K and M_j^Q=C_j−1 Q retain degrees −1 and +1 respectively. At each of the three exhaustive integer ranges, MRE16 is exact. MRE19 has the correct F and Gamma factors; MRE20 correctly writes the defects against the separately centered scalar operators as q^−1/2 on the inclusion and q^+1/2 on the quotient. In MRE21 the order F Gamma^−1 (I+(log q)N) gives exactly q^ρ times the full finite exponential. The logarithmic moduli in MRE22 are therefore 2 Re ρ−1 and 2 Re ρ+1 as stated.

### Twisted strict map MRE23–MRE27

In addition to the previously checked F and arithmetic actions, the Gamma intertwining is exact: Gamma_Q Gamma_T=q^1/2 q^−1=q^−1/2=Gamma_K. For the map N:V_2⊗T_q→V_2, the domain's j-th step is M_j+2 V_2⊗T_q. If j<−1, M_j+2 V_2 is contained in K and N kills it; simultaneously im N∩M_j V_2=0. If j≥−1, the domain step contains all of V_2 and both images equal K. This proves strictness for every integer. The relation FN=q^−1 NF gives exactly equivariance from F⊗q^−1 on the domain to F on the codomain; Gamma has the same relation, and A_a commutes with N as the full polynomial in N displayed in MRE10.

### Relative existence and uniqueness MRE28–MRE29

The source explicitly chooses W=M with constituent degrees −1,+1. The existence verification is the exact calculation already given above. Its additional uniqueness argument is also complete. For any other relative filtration R′, each W-graded piece has zero induced N; the relative isomorphisms force its R′-graded degrees other than its specified W-degree to vanish. Consequently R′ induces degree −1 on K and degree +1 on Q. For j<−1, its intersection with K and its image in Q are zero, forcing R′_j=0. For −1≤j<1, it contains K but has zero image in Q, forcing R′_j=K. For j≥1, it contains K and surjects to Q, forcing R′_j=V_2. These are all its steps, so R′=M. This establishes uniqueness for the specified W; the source does not claim that an independently supplied arbitrary W has been constructed or controlled.

### Original extension and action relation MRE30–MRE33

The section calculations agree with the independent computation above, including the coefficient-one defect Ns−sN_Q=u and the arithmetic defect a^ρ(log a)u. The separate filtered F-equivariant splitting s_0 is explicitly proved and correctly distinguished by its exact defects. The final added MRE33 has the correct complete conjugation and difference:

\[
 F_{q,2}A_{a,2}F_{q,2}^{-1}-A_{a,2}
 =a^\rho(q^{-1}-1)(\log a)N.
\]

Since q>1, a>0, a≠1, a^ρ≠0 and N≠0 on the specified V_2, this difference is nonzero. Thus the claimed noncommutation is proved under precisely the stated domain conditions.

### Integration scope retained

The source defines and proves its result for the explicit length-two algebra V_2=C[u]/(u²), at any fixed ρ∈C. This proof does not establish that the original function g has a zero of multiplicity at least two. Any later identification with an actual zero packet must retain that packet's multiplicity. For a block C[u]/(u^m) with m≥2, the quotient map to V_2 is explicit and intertwines N and the full arithmetic action; the present text does not need that extra identification for its displayed finite-dimensional claims. No nonexistent double zero is inferred by this acceptance.
