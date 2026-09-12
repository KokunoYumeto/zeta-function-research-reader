# Parallel formalization handoff: arithmetic frontier and symmetric tensors

Input: PR #14, exact head `3bff1b2bd87dfa2592f65c5ccc231f6ee9541dfc`.
This is an additive mathematical continuation. No original scalar, internal quotient,
retraction, homotopy, topology, or prior proof file has been modified.

## Existing verified interfaces to reuse

The supplied PR #12 receipt reports the actual quotient section and all its changes,
the operator defect, the complete two-leg homotopy family, fixed-index `Hom.total`
reconstruction, and the declared finite-chart dual maps. Its analytic hypotheses
remain hypotheses. Do not assert that this note's analysis acquired a Lean certificate.

## New bounded algebraic targets

1. **Highest-degree relation graph.** Let a finite polynomial-type space be an
orthogonal sum `H_low + H_top`, let `J` be a surjection to `E`, and let `R:E->H_low`
be the unique right inverse orthogonal to the old kernel. For the actual highest
column map `T` and `F=J T`, set `b=T-R F`. Prove that `b` maps isomorphically to
the new relation layer, with inverse highest-component extraction. Prove
`b* b=Omega+F*G F`, `b*R=-F*G`, `Jb=0`. This is an actual kernel computation.

2. **Original supported transport.** Apply the already proved internal quotient to
`B_old <= B_new`. `b(u)` is nonzero in `B_new/B_old` for `u != 0` and becomes
its next label's represented zero. Keep the support transition and the compatible
operator restriction as in the existing `homologyKernelEquiv` interface.

3. **Update and flux maps.** From the first target prove the precise formulas for
`Y=-b H^-1 F*G`, `Crel=b Omega^-1 Eplus*G`, and
`W=G(F Omega^-1 Eplus* + Eplus Omega^-1 F*)G`.
All source/target matrices are specified in NOTE sections 3--4.

4. **Polynomial border cancellation.** Given the displayed unscaled recurrence
`t p_n=p_(n+1)+b_n p_n-a_n p_(n-1)`, with `a_n=omega_n/omega_(n-1)` and
`b_n+conj b_n=1`, prove the total-degree finite-sum displacement (4.2).
The imaginary part of `b_n` is not assumed zero. The packet unit is included in
`z_alpha`; no root-simplicity or diagonalizability is assumed.

5. **Relative certificate.** Prove congruence (4.5), the AB/BA nonzero-spectrum
comparison (4.6), and the row-sum bound in (4.8). The latter is a finite matrix
bound with explicit `Gamma` and `lambda`; no asymptotic smallness is supplied.

6. **Odd-degree symmetric summand.** The chain permutation uses Koszul signs.
The projector is `sum(sign(pi)*T_pi)/k!`; top degree therefore has the ORDINARY
symmetric permutation projector. Show idempotence and commutation with the
cochain differential. Keep the complement. The unsigned chain average has a
different top-degree image; do not substitute it.

7. **Orbit-coordinate comparisons.** Use unscaled orbit sums. Their squared
coordinate norms are `k!/prod(n_i!)`. The full-to-symmetric extraction is
`L=(I*I)^-1 I*`; both equations (6.4) contain the necessary factors.

8. **Trace decomposition.** For the finite packet prove (6.6), its degree-`k`
supertrace sign `(-1)^k`, and the retained complement (6.7). Full Jordan action
stays in the object even though ordinary trace reads diagonal entries.

## Analytic hypotheses that this contribution uses

The original theta range construction, the entire quotient `g/h`, the precise
Mellin/Plancherel map, full finite jet surjectivity, and existence of the preceding
least-norm representative are taken from the pinned written source. Arithmetic
moment quadrature and any uniform estimate remain outside the finite checker.

## Fresh finite evidence

`check_frontier_control.py` has 22 named tests. They use declared Gaussian moment
models (including nonzero mean and nonconstant quotient units), exact polynomial
and rational/complex matrix algebra, repeated-root jets, cochain signs, and split
support transitions. They are not zeta packets and do not test RH. Normal and
optimized runs agree; intentional negative controls fail in both modes.

During development two display-fixture comparisons exposed the difference between
the bases `(1,s)` and `(1,s-1/2)`. They were repaired by the explicitly retained
matrix `B=[[1,-1/2],[0,1]]`, not by changing the mathematical equations.

## Actual next analytic target

Estimate the largest generalized eigenvalue of the symmetric highest-degree
pencil (4.5), with the full arithmetic recurrence and jet unit. The finite bound
(4.8) gives one sufficient quantitative estimate; the signed formula (4.6) retains
cross-term cancellation when that bound is too coarse. No sublinear-in-tensor-
degree bound has been proved here.
