# Formalization handoff: residue-driven constituent curvature

The mathematical input is the unchanged finite cyclic coefficient module and its original source metric. No new scalar or support construction is introduced. Use the existing SplitZero lift on each retained fibre.

## Exact algebraic targets

1. With `A=M_S`, `ell` the top remainder coefficient, and `R=one tensor ell`, prove that the matrices `A^i R A^j`, for `0 <= i,j < q`, form a basis of the coefficient endomorphisms. The proof uses the explicit determinant of the residue Gram and cyclicity of `one`, not an irreducibility axiom.
2. Given the actual inclusion `I:F -> E` and quotient `pi:E -> E/F`, with `F` nonzero, proper and `A`-invariant, prove `pi R I=(pi one) tensor (ell I)` has rank exactly one, kernel `ker(ell I)`, and image the line spanned by `pi one`. Keep both nonvanishing witnesses.
3. Given invertible `Pi`, define `P=Pi I`, `H=P*P`, the orthogonal projector `p=P H^-1 P*`, and the local derivative `P1=-Pi(A+tR)I/u`. Prove `(1-p)P1=-(t/u)(1-p)Pi R I`. The finite matrix trace of its squared norm factors exactly as RC25. Holomorphy and differential interpretation remain separate analytic inputs.
4. For original positive `Gi >= Gj`, construct the quotient norm of `one mod F` and dual norm of `ell|F`. Prove the two order bounds RC35 and the determinant bound RC36, retaining all inverse-domain hypotheses. The written logarithm step and finite matrix order proof have distinct interfaces.
5. Prove the second-derivative jet identity `u^2 Pi2+k u Pi1+u Pi R=Pi(A_t^2-k A_t)` from `Pi1=-Pi A_t/u` and `Pi2=Pi A_t^2/u^2-Pi R/u`. Compose with the original source observation; do not use an uncorrected second derivative as the arithmetic Laplacian.
6. Under the actual Pascal translation, carry the inclusion, unit, residue functional and positive metric together. Prove exact curvature invariance and the constituent trace shift `2 dim(F) Re(a)`. A translated auxiliary polynomial is not an asserted arithmetic packet.

## Analytic interfaces

The supplied XD proof gives the entire fixed-u period matrix and its nonvanishing. The new written calculation differentiates `log det(P*P)` using Wirtinger derivatives. The first nonzero mixed jet is of order `(2,2)`; its coefficient is one quarter of the mixed derivative, not the real-axis fourth derivative. No part of this package asserts a new Lean build.

The period target metric `I_q` and the exact transport `Pi^{-*} G_N Pi^{-1}` have different roles. Their comparison uses the condition number of `G_N^-1 Pi*Pi` in RC33. Determinant nonvanishing does not replace that condition number.

## Scope of executions

The new twelve-method finite suite has actual normal/optimized records and three deliberately false formula controls per mode. It samples exact polynomial and rational complex matrix fixtures, including repeated roots. No predecessor suite, source quadrature, or actual zeta-zero packet is claimed as a new test.
