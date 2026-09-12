# Validation and provenance

## Exact base read

- Base PR #9 was read through the connected GitHub actions. Its current head was `8f99b94d306c3b1aaa817d52c57fa6fd298d511c`.
- The locally opened chain-descent note matches remote blob `86db838e79d10a8fe7d4376303706c4ea64570a1`.
- The original derived-mathematics attachment and the selected supplied Weil II TeX excerpt were read for their actual interfaces. No new Lean execution or full Deligne audit is claimed.

## New local checks

- Python 3.13.5; SymPy 1.14.0.
- Twelve unittest methods, containing finite parameter families, passed in normal and optimized execution.
- Both successful JSON records were byte-identical.
- The intentional extra failure test failed in both modes, exit status 1.
- The previous chain-descent checker was rerun normally and passed its twelve tests. It was not rebuilt or rerun in Lean.
- The finite checks exercise the encoded algebra. The general range, continuity, compactness, and density statements have written proofs in the note; they are not inferred from these tests.

## Authored source identities

| File | Git blob | SHA-256 |
|---|---|---|
| `RESEARCH_NOTE.md` | `e2d06b7bfee8caacea35a2a7e5fc70754d96d840` | `496f3ec752e3e67ddafaae7423feb300b1faa789ca6907872f8d539bdf6e1859` |
| `check_global_retraction.py` | `a65478ffff51f866ddacfcf0494e2650b10ab4ec` | `ed99482e6a7d8681ff4ec0a9edfa6d25f819b04db4c299677f9178923f702362` |

## Scope retained

The result identifies the algebraic-to-Hausdorff quotient map for the original strong-Schwartz topology. It does not prove that all finite spectral observations separate the entire quotient, remove the balanced meromorphic summand, establish an infinite trace-class formula, or prove the geometric weight estimates.

The auxiliary cutoffs and the reconstruction constant remain explicit. The new section changes each prior finite representative by a calculated theta boundary, not by rescaling the arithmetic function. The original quotient `G(Z) -> Z`, supported zero e, structural zero tau, local residue units and degree signs remain in the maps.

Only authored text, test code and this validation record are proposed for public addition. No source-literature corpus, private transcript, credentials or font files are included.
