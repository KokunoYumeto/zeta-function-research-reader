# Consecutive-window verification record

Integrated main: 952ef9fee1e1419b6858d920354de8fa99430b7d. Draft PR25 is add-only against that snapshot and does not change main or another session's branch.

At implementation commit a02db96da0faff1aae32409c2719aab395a4aae9, run 34728139612 / job 103645875951 PASSED all four new source checks and the inherited TodaVolume dependency. All nine selected new transitive reports used only propext, Classical.choice, Quot.sound. Seven exact regression methods passed normally and under python -O; both negative controls failed. The full log was read back.

The successor adds canonical_norm_volume, which composes the original radius sequence with the derived window propagation and supplied norm bound, rather than assuming the propagated endpoint inequality. The new run also replays the byte-pinned 18-method arithmetic source checker and its balanced-window checker in a separate pinned Sympy environment. Consult PR25 for completion status of this successor run; the successful predecessor does not certify a later edit by itself.

The analytic proof of the actual zeta/convolution norm estimate, the comparable-window extension, the limiting four-volume threshold and the block generalized-eigenvalue interpretation have written proofs. They are not additional Lean declarations or interval certificates. No source mass, arithmetic unit, quotient or original support operation is changed.
