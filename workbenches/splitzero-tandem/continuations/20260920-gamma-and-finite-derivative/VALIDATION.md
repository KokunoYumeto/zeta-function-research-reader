# Validation of the complete source edition

Root read the complete gamma proof, finite derivative repair, independent proof note and executable checkers. The independent derivative check found no mathematical error in the submitted parent proof and added the explicit rational evaluation constant K_m, whose full argument is retained in both proof bodies. The original author source is unchanged.

Fresh normal and optimized runs passed 3,271 exact finite checks for result056 and 2,692 for result058 in each mode. Three deliberately incorrect gamma variants and five incorrect derivative variants each exited with an explicit failure in both modes. [The complete replay receipt](checks/ROOT_REPLAY.json) records every run and control.

The original gamma checker contains Python assertions. Its [strict runner](checks/gamma/strict_verification.py) verifies the unchanged original checker's SHA256 and replaces every assertion with an explicit exception-raising predicate before execution. None of its checks disappears under `-O`. Run `python checks/gamma/strict_verification.py` and `python checks/repair/verification.py`; optimized runs add `-O` before the script name. Negative controls are named in the receipt and accepted by `--negative-control`.

These are integer/rational certificates and finite synthetic branch tests, not sampled proofs of analytic statements or numerical values for the source's actual derivatives. The gamma asymptotic, all-degree kernel positivity, exact Taylor remainder, branch termination and polynomial evaluation bound are proved in full in the accompanying LaTeX.

The scientific diagram was generated from its retained source and visually inspected. It contains no sampled derivative curves. Draft-only TeX validation checks the complete new source and its references without producing or reading a PDF; the exact receipt is included after that check succeeds. The three large cumulative insertions are verified reversible to their byte-pinned predecessors. No fresh compilation or layout inspection of those cumulative manuscripts is claimed.
