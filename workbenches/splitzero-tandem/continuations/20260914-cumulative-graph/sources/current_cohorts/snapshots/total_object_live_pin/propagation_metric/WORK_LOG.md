# Metric propagation log

Task: preserve the sealed cumulative edition and produce complete derived copies
with every proved arithmetic spectral/overlap refinement at its affected earlier
theorem, proof and downstream use. Live output and other lanes are not edited.

Initial source intake: complete AT/AW/SP/ACM, CA, affected AAM/QT/HC/TW/PAM
sections, reconstruction and combined restriction; all source paths and hashes
are captured by build_propagation.py and its manifest. Original source bytes
are retained in originals/. The independent scope audit runs in the child
metric_scope_audit. Source support and marked-product boundary updates belong
to their designated lanes.

Mathematical decisions:

- AT becomes the self-contained finite-dimensional proof source, avoiding a
  cycle when AW and its downstream uses are strengthened.
- Preserve the exact trace-norm bound already proved in SP13. Its pointwise
  minimum with AW's full spectrum is at least as sharp as ACM's requested
  spectral/overlap minimum. Display both and their exact order.
- The sigma reference in CA/AAM is not the tensor Gamma reference. Re-run the
  same coefficient construction on its actual sigma interpolation and label
  its control separately; keep both masses and the original theta observation.
- Preserve all original angle estimates, signs, relation energies, nilpotent
  multiplicities, source kernels and asymptotic domains. A fixed finite bound
  does not imply a shrinking tensor error.
- HC11 remains a fact about the coarse width, not about the newly intersected
  interval. HC14's phase allowance is unchanged; the upper value it transports
  is replaced by the sharper original-source bound.

Status: deriving complete revised sources and proof locators; independent
review follows source generation. No RH endpoint established.
