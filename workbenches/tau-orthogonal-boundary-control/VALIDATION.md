# Validation and provenance

Base read: PR #11 at `d37eade4f9e6a82c1a88aeff710a3b851a34eb49`. The supplied other-session homotopy proof and its then-uncompiled Lean draft were read in full. Its coefficient theorem is correct by the written two-equation proof. The continuous and twisted-action integrations were already in PR #11 and are used, not claimed again.

## Updated formalization status

The attached draft's execution status has been superseded by the other session's successful PR #12 at `5d2772ea0a16d177ac3e01ff70394b90ba95a232`. The complete `SplitZeroTauHomotopy.lean`, all-success job steps and full job log `103535438942` were read. The log checks out the exact source revision, installs Lean 4.31.0, verifies the existing Mathlib pin and original core, checks all seven tau sources separately with `--trust=0 -DwarningAsError=true`, and accepts the declared axiom reports. The actual `cochainHomotopyEquiv`, both inverse laws and both cochain equations are present. See `COORDINATION_UPDATE.md`.

This is a remote certificate produced by the other session, not a local Lean execution. It covers its explicitly stated algebraic/topological interfaces. It does not certify the actual analytic theta construction, the full support-changing homotopies, or the new Gram/control arguments here.

## New finite checks

The new checker ran under Python 3.13.5 and SymPy 1.14.0. Thirteen named finite test methods passed normally and under `python -O`; successful JSON records matched byte-for-byte. The intentionally failing extra test failed in both modes with exit status 1.

The public checker was fetched after publication. Its Git blob `4049113a3256e8b8786530cf4e32da2487753f7c` matches the locally tested bytes. Its SHA-256 is `ce4bc51e8bb6f5338bf4ba17da45216fe9c9d7cfb596fe7531c54a062531dcb6`.

The checker tests finite algebraic identities and declared calibration models. It does not verify actual zeta zeros, the prior analytic range theorem, the new infinite-dimensional density argument, or any Lean declaration. No `lean` or `lake` executable is installed in this runtime; no new formal certificate for this contribution is claimed.

Reproduce:

```sh
python check_boundary_control.py --json result.json
python -O check_boundary_control.py --json result-O.json
cmp result.json result-O.json
python check_boundary_control.py --deliberate-failure # expected exit 1
python -O check_boundary_control.py --deliberate-failure # expected exit 1
```

The conversation package also contains an exploratory 80-digit evaluation of the first four actual theta moment rows using five Gaussian terms on each exterior. The Gaussian-tail expression is proved analytically; the decimal incomplete-gamma evaluation is not an interval certificate, and no uncomputed arithmetic cross-Gram matrix is certified.

Source reading: the attached other-session note; live PR #11 mathematical sections 1-7; the supplied global-retraction and Deligne-control authored notes; retained Weil II TeX excerpts around 3.3.1-3.3.6 and derived purity in 6.2.4-6.2.7; the successful PR #12 source and job above. These are selected readings, not a new full audit of Deligne's proof. NIST DLMF 18.2 was consulted for standard polynomial context; the needed density result for the actual weight has its proof in the new note. No OCR was used.

The scalar definition, arithmetic quotient, extension class, residues, finite traces, source labels and original formal modules remain unchanged. This contribution adds only authored research exposition, test code and validation. No private transcript, source-literature corpus, credentials or font files are published.
