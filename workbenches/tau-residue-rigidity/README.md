# Residue rigidity on the original SplitZero arithmetic packet

Base inspected: `867454a00c64291c4498a36769ccd36508c63458` (merged PR28). The original scalar, full infinite quotient, actual packet section, support labels and source metric remain inputs. This contribution completes previously written algebraic results rather than treating an auxiliary-purity counterexample as a global verdict.

## Mathematical target

For a monic polynomial h of positive degree over a field, E=K[S]/(h) is the literal `AdjoinRoot h`. The residue is the coefficient of S^(deg h-1) in its unique monic remainder. A nonzero representative p of degree d is detected by S^(deg h-1-d): no reduction affects the top coefficient, which is the nonzero leading coefficient of p. This proves perfectness without assuming squarefreeness or inverting the discriminant.

The actual linear duality map x -> (y -> residue(y*x)) is constructed and proved invertible. For an S-stable submodule F with 0<F<E, cyclicity gives 1 not in F, while perfectness gives residue|F nonzero. Consequently pi_F R inc_F, with R(v)=residue(v)*1, has exactly the image K*pi_F(1), rank one, and the full codimension-one kernel ker(residue|F). It is not declared injective when dim F>1.

The source module reuses the original `Relations.quotientDiagram` and the original integrated `residueInsertion`. If J r=1 and J kills the original relations B, the packet section injects into D/B. For every nonzero packet vector x, a power n<deg h gives a nonzero residue response that remains nonzero in that original supported quotient. Nonbottom support is stated wherever global absence is excluded. A further constituent observation is a separate quotient.

## Connection to the existing period calculation

The written source proves Pi'=-Pi(A+tR)/u and period invertibility for u nonzero. The now-targeted rank-one theorem supplies the nonvanishing used in the normal derivative

  (1-P_F) (Pi inc_F)' = -(t/u)(1-P_F)Pi(1) residue|F.

It does not identify the arithmetic operator with Frobenius or establish a uniform arithmetic endpoint bound. The previously written curvature and period-integral proofs keep their existing status.

## Integration and verification

The initial commit contains complete proof scripts awaiting a run; no success is claimed here in advance. The dedicated workflow uses the unchanged toolchain and Mathlib pin, reuses the inherited fail-closed audit parser, and strictly recompiles the actual local dependency closure. All new theorem targets are enumerated in `TARGETS.json`. `STATUS.md`, when added after an observed run, records the exact verified source commit.

The valid counterexamples in the user's transfer audit remain tests of a generic transfer theorem. They do not justify erasing the original arithmetic hypotheses or announcing failure of every construction over the tau base. No inherited file or another session's branch is changed.
