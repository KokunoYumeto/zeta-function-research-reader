# Exact finite normal-image reconstruction: integration ledger

Date: 2026-09-12. Root requested the complete source-to-jet reconstruction after the actual strict-normal theorem. The new subsection FC.28–FC.36, including FC.29a, was appended to `tex/sum_connection_stieltjes.tex`. No further mathematical extension is included in this lane.

## Exact source and preservation

- Original complete FC.1–FC.27 SHA-256: `639fc202b30a5504a6b280f0b8dd155daaa48d12f3e9da80fe9ac30c524c744a`.
- Complete TeX SHA-256 at reconstruction handoff: `ff30e49f3d33df24fbacbd4504ede5e82bff251d248cccb4d594905e26a97b45`.
- TeX size at that handoff: 36,805 bytes.
- A byte-prefix verification at the new subsection marker returns exactly the original SHA-256 above. Thus the earlier FC.1–FC.27 bytes, including their final newline, are preserved.
- First reconstruction draft SHA-256: `b86b987de6099f510e58e21a192c21b6e60e1cb6c46ea3af3ac743f052998911`. Review corrections are recorded below rather than being hidden by a hash replacement.

## The complete mathematical additions

FC.28 retains the literal source basis `P_(alpha,n)=theta_alpha(z) S^n` with `0≤n≤M−ell_alpha`. Its matrix `C_M(u)` has columns `delta_(alpha,beta)(k/2+iu)^n`, and its derivative retains the factor `i n`. A negative degree bound contributes no source column. The empty source has its unique maps between zero spaces.

FC.29 defines the actual normal map `N_M p=N_u C_M(u)p` and tangential map `T_M p=j_u(C_M'+Gamma C_M)p` into the original Hilbert space `L²(du dy)`. Projection contraction and the actual differentiated Schwartz bounds make all columns square-integrable. FC.26 proves the computed normal Gram

\[
H_M^N=N_M^*N_M=\int C_M^*\mathcal N C_M\,du
\]

strictly positive for every nonzero source vector, including a nonzero relation polynomial whose arithmetic class is supported zero.

FC.29a also retains the original amplitude Gram

\[
H_M^0=\int C_M^*W C_M\,du>0,
\quad K_M^{N:0}=(H_M^0)^{-1}H_M^N,
\quad (K_M^{N:0})^*H_M^0=H_M^0K_M^{N:0}=H_M^N.
\]

Thus the normal metric is a computed pullback, with its exact positive self-adjoint operator relative to the original amplitude metric. The original and normal norms are never identified without this operator.

FC.30 proves the integral adjoint and inverse

\[
L_M^N=(H_M^N)^{-1}N_M^*,\qquad
N_M^*r=\int C_M^*N_u^*r(u)\,du.
\]

Every scalar integral is absolutely convergent by Cauchy–Schwarz. The identity `L_M^N N_M=I` gives the source inverse on the actual normal image, while `N_M L_M^N` is the orthogonal projection onto that finite closed image.

FC.31–FC.32 recover both graph components by `r↦(T_M L_M^N r,r)`. The inverse takes the second component. The graph metric is explicitly `H_M^partial=T_M*T_M+H_M^N`; reconstruction has squared norm `||r||²+||T_M L_M^N r||²`. No isometry from the normal norm to the larger graph norm is asserted.

FC.33–FC.34 retain the full product quotient `E=C[s_1,...,s_k]/(h(s_1),...,h(s_k))`, the full entire multiplier `U=product v_h(s_i)`, and its unit jet. The derivative column for the literal source basis is

\[
J_M^{\log}e_{\alpha,n}
=j_I(\partial_S^{\rm rel}(U\theta_\alpha S^n))
=n\upsilon^{(k)}[\theta_\alpha S^{n-1}]_I
+\beta_h\upsilon^{(k)}[\theta_\alpha S^n]_I.
\]

Here `partial_S^rel=(1/k)sum partial_(s_i)`, `beta_h=(upsilon^(k))^(-1)j_I(partial_S^rel U)`, and the first term is zero when n=0. Every local order and unit coefficient remains; inverses of v_h are only used on its actual finite unit neighbourhoods. For h=1 the arithmetic target and observations are zero, while the analytic reconstruction remains valid.

FC.35 defines the arithmetic derivative observation on the actual finite normal image by `Obs_M^log=J_M^log L_M^N`. Reconstructing both graph components, adding them, applying `−i U_k^(-1)` and then the original full jet gives exactly that observation. The factor −i is the inverse of the original Mellin identity `partial_u U_k=i U_k L_k`. Every penultimate function is an actual logarithmic multiple of a finite tensor source function. The formula does not assign an independent arithmetic meaning to an arbitrary unrelated measurable section.

FC.36 proves exact gauge invariance: the transformed coefficient matrix is `C_M^C=C^(-1)C_M`; the `C^(-1)C'` connection term cancels the derivative of C inverse. Both amplitude maps N_M and T_M, their normal Gram, the image inverse and the reconstructed arithmetic observation are the same maps after that declared coefficient transport.

## Corrections made during independent review

1. Root and the independent reviewer found three literal missing backslashes in `quad`/`qquad`. All were repaired, and a PCRE2 text check finds no remaining standalone unescaped instance.
2. The independent reviewer noted that calling H_M^N “the actual source metric” could suggest it was the original amplitude Gram. FC.29a now proves the exact relation between both retained metrics as written above. This is a mathematical precision correction with its complete typed operator, not a relabeling.
3. FC.35's long source path was split into two matching displayed rows for layout. Its intermediate amplitude is repeated exactly, so the composed source-to-jet map is unchanged.

The full initial reconstruction and the complete corrected FC.28–FC.36 subsection were independently read. The reviewer reports that all definitions, domains, three retained forms, inverse and projection, both graph components, full arithmetic columns, gauge transport and zero-space scopes pass, with no further mathematical correction. Its full proof review is `work/sum_connection_normal_reconstruction_independent_review_20260912.md`.

Root subsequently moved an earlier FC.4 derivative expression into a display and clarified that each diagonal term is computed before the common `k^(−2)` factor. The exact receipt in `logbook/stieltjes_typesetting_repairs.json` records whole-file SHA-256 `ff30e49f3d33df24fbacbd4504ede5e82bff251d248cccb4d594905e26a97b45` to `fb453c93e3a08e3ed2aca04691e9401b13779be137eb07b2de55571df6b888cc`. Reversing only that recorded earlier window in memory recovers a byte-exact historical snapshot at ff30e49. The current and historical complete FC.28–FC.36 excerpts are byte-identical, with SHA-256 `03b2f13329d4a18e75d2f7328b072f9faf2f4d698aa991ec3896c6a56e0fceeb`. The independent reviewer retains that snapshot and preservation receipt in its final manifest. No reconstruction theorem changed during this layout pass.

Root maintains compilation and publication. The prior source analytic audit and the independently reviewed FC.21–FC.27 strictness results retain their original scoped hashes. This lane is complete and makes no further speculative extension before the build.
