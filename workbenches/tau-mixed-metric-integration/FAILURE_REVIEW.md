# Failed execution review and recovery

13 September 2026. This record separates observed Lean failures from local transport failures. It does not infer a mathematical contradiction from a tool timeout.

## The two failed resolvent workflows actually retrieved

1. Run 34775074985, job 103771596758, source 12a830194a4bc164e13f80a5222f686b2f667447. Checkout/synchronization, scalar recovery, toolchain, cache, inherited 35-file strict closure and 60-target audit all succeeded. The new MetricResolvent file failed at three primary proof-script sites: deprecated `Matrix.mul_eq_one_comm`; a secant equation supplied without moving its G0 term to the other side; and a rewrite with an unspecified base metric. The last produced cascading unused-simp warnings. The branch subsequently corrected these with `mul_eq_one_comm`, an explicit additive calc, and `section_update M0 M1 C`. The theorem statements were retained.

2. Run 34775645022, job 103773145903, source bfe017b6e48cd0c9e8828f3ed9e5e5244016a172. The preceding repairs worked: MetricResolvent and CertifiedTraceBounds strictly compiled. MetricResolventSupport stopped on an unused automatically included `[Fintype n]` in `primitive_cocycle`. This recovery adds `omit [Fintype n] in` to that theorem. The finite column sum is not used by the primitive identity; no mathematical assumption, strict flag or warning category is weakened or suppressed. Later tests were skipped by those failed runs and are not counted as executed there.

The full decoded logs of both jobs were read. The owner mentioned three failed syncing traces, but these two retrieved workflow runs cannot be asserted to be those exact three UI traces without identifiers. The first run contains three primary proof/API errors; that is not three separate sync failures. The older PR28 status separately records its own historical failures.

## Operational failures reproduced in this session

A simple container command and a Python archive-path probe each returned TransportTimeoutError before yielding source or mathematical output. These are failures of the local execution transport, not evidence against the formula. The hosting transport is not repaired by editing a theorem. Verification is instead executed using the repository's working GitHub Actions path.

## Reconciliation and remaining scope

The entire eight-file resolvent contribution is retained from bfe017b6e48cd0c9e8828f3ed9e5e5244016a172 with its ancestry. Its previous note remains an immutable account of the earlier intake; the current marked-product NOTE was subsequently read from main at bcf60f578e45620d36d680cbaf5a3d65cb746361. That closes the mathematical reading gap for the published note, not a byte-level verification of the uploaded ZIP. The marked-product source's full mixed pairings (46), common source (49)-(53), signed contrast (54)-(61), and finite error formula (67) are retained.

Initial new source state is a candidate, not a successful certificate. New development failures and observed final verification, if obtained, are recorded separately in STATUS.md. Current main and the parallel branch refs are not rewritten.
