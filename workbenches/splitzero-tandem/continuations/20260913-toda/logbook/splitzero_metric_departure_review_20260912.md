# Independent metric-departure review — 12 September 2026

Read the complete `output/split_zero_rh_tandem_2026-09-12/tex/metric_departure.tex` and the revised TB32–TB33 paragraph in `tau_boundary.tex`. Independently re-derived MD1–MD9, including the arbitrary-packet rank-two formula, Gram pullback, nilpotent traces, and every exponent. A second reviewer independently checked MD6–MD9. No mathematical correction is required in the reviewed text. No root TeX was edited and no Lean process was run.

Reviewed SHA256:

- `metric_departure.tex`: `5208810509526560B31F0E8EA84D6A08D70F131E745FAC54E99CF0EF6B6A7924`.
- `tau_boundary.tex`: `312EDBD818647B27F0ACC7C79DC6CAFF07B5CBF5EF6F13C0A851C73700518E69`.

## MD1–MD5: departure and arbitrary-packet rank-two control

Set C=G^(1/2)AG^(−1/2), through the displayed isometry from the retained metric space (E,G) to Euclidean coordinates. Cyclicity gives

Tr(C*C)=Tr(G⁻¹A*GA),

and S_G=C+C*−I. The constructive unitary triangularization in the proof is valid: after choosing an eigenvector as the first orthonormal basis vector the lower-left block vanishes, and induction triangularizes the remaining compression. Its diagonal contains all algebraic multiplicities. Consequently the stated departure is exactly the sum of squared moduli of the strict upper-triangular entries. It is nonnegative and vanishes exactly for a normal C. Conjugating the normality equation by the original positive square-root isometry yields precisely AA^sharp=A^sharp A with A^sharp=G⁻¹A*G, as written.

The trace expansion has the correct signs:

Tr(S_G²)=2Tr(C*C)+2Re Tr(C²)−4Re Tr C+d.

Triangularization gives Tr C=Σρ_j and Tr C²=Σρ_j² even for defective eigenvalues. On each diagonal entry the scalar contribution is

2|ρ|²+2Re(ρ²)−4Re ρ+1=4(Re ρ−1/2)².

This proves both MD2 identities without dropping nilpotent directions.

For the original rank-at-most-two forms, write their two potentially nonzero real eigenvalues as a,b, padding by zero when needed, including dimension one. If S=Σδ_j and Q=Σδ_j², then

a+b=2S,

a²+b²=4Q+2d_G(A),

(a−b)²/4=2Q+d_G(A)−S².

The identity max(|a|,|b|)=|(a+b)/2|+|a−b|/2 proves MD3 exactly. No reflection assumption or opposite-sign assumption is needed for MD3. Reflection stability then gives S=0 and proves MD4 with its factor 2 and every multiplicity retained.

## MD6: original local-unit Gram pullback

From G_m=U* K_N⁻¹U and AU=UA, both U and U* are invertible and A*U*=U*A*. Direct substitution yields

G_m⁻¹A*G_m A=U⁻¹(K_N A* K_N⁻¹A)U.

Thus the trace in MD6 is exact. The local unit is preserved in the actual representative and Gram map; only its commuting similarity disappears inside this specific scalar trace invariant.

## MD7–MD9: full local jet and condition-number bounds

The Chinese-remainder inclusion I_ρ is injective and intertwines A with ρI+N_ρ. Therefore G_ρ=I_ρ*GI_ρ is positive definite, and the exact pulled-back form is

I_ρ*W_G I_ρ=2δG_ρ+N_ρ*G_ρ+G_ρN_ρ.

Pullback preserves the global two-sided form bound. Under the explicit local square-root isometry this becomes T=2δI+L+L*, with L=G_ρ^(1/2)N_ρG_ρ^(−1/2), and ||T||≤ε_G.

Nilpotence gives Tr L=Tr L²=0. Expanding the square gives

Tr T²=4rδ²+2||L||_F².

Since T is Hermitian and every one of its r real eigenvalues has modulus at most ε_G,

||L||_F²≤(r/2)(ε_G²−4δ²).

This is MD9, with the correct subtraction and factor r/2. The independent eigenvector estimate gives ε_G≥2|δ|. For r≥2 the nilpotent is nonzero, so ||L||_F²>0 and the bracket is strictly positive.

The squared metric norms satisfy

||N_ρ^ell z^k||²_(G_ρ)≤||L||^(2ell)||z^k||²_(G_ρ)≤[(r/2)(ε_G²−4δ²)]^ell ||z^k||²_(G_ρ).

The exact power N_ρ^ell z^k=z^(k+ell) gives MD7 with exponent ell, without changing any Taylor basis factors. Finally λ_max(G_ρ)/λ_min(G_ρ)≥(G_ρ)_(0,0)/(G_ρ)_(r−1,r−1). Combining this with k=0 and ell=r−1 gives precisely MD8's exponent −(r−1). The assertion remains true when its lower bound is below one; no extra smallness assumption is required. At a critical repeated root, ε_G→0 therefore forces the stated diverging condition number in the retained Taylor coordinates.

## TB32–TB33: narrowly scoped reflection-stable comparison

The revised paragraph expressly imposes Z=Z† with full multiplicities only for the same-packet residue/dual-metric formulas TB32–TB33. It expressly retains arbitrary packets for the preceding kernel and source-boundary results and supplies the general conjugate-linear map E_Z→E_(Z†). This is the required scope.

For the stable packet the residue matrix obeys A*S+SA=S, as follows directly from (sf)†=(1−s)f† in the pairing. Reflection and the functional equation give S*=−S. The dual weight identity follows algebraically from the intertwining relation:

A*(S*G⁻¹S)+(S*G⁻¹S)A−S*G⁻¹S

=S*[G⁻¹−AG⁻¹−G⁻¹A*]S

=−S*G⁻¹(A*G+GA−G)G⁻¹S.

This checks the minus sign in TB32. The residue pairing is nondegenerate on the retained full local algebras: in each primary algebra its matrix has nonzero anti-diagonal coefficient coming from the unit g/(s−ρ)^r, and reflection permutes those primary blocks. Thus S is invertible and the stated dual Gram is a positive metric. TB33 is the exact identity u*SJ_gv=u*G_m(G_m⁻¹SJ_g)v, with no missing adjoint or scalar factor.

All requested checks passed. No remaining defect was found within this review's scope.
