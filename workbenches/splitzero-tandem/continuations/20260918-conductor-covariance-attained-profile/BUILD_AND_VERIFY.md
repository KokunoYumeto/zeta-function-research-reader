# Source package and verification

Read `PROGRAMME_GUIDE.md` for the purpose and precise scope of this continuation. `DUAL_WEB_PROOF_SUPPLEMENT.pdf` is the new 68-page reading copy. The `cumulative/` directory contains three complete editable successors; the earlier deposited 837-page reader and 263-page companion are retained at their existing edition.

The standalone `DUAL_WEB_PROOF_SUPPLEMENT.tex` contains its full body and bibliography. With XeLaTeX, Latin Modern and the declared standard packages installed, run `xelatex -interaction=nonstopmode -halt-on-error DUAL_WEB_PROOF_SUPPLEMENT.tex` twice from this directory. It has no external TeX source inputs. This package does not claim that its three cumulative sources were recompiled: their exact predecessor recovery and shared-body preservation were checked instead.

Run `python -B verify_package.py` from this directory to check the allowlisted source hashes, sixteen portable source anchors, 3,908 formula locators, three exact cumulative recoveries, and the citation-only conductor derivative recovery. This verifies packaging integrity, not a new independent mathematical proof audit.

`SOURCE_PINS_AND_PUBLIC_DERIVATION.json` records original local artifact hashes and outgoing derivative hashes. Paths beginning `PROJECT_ROOT`, `PRIVATE_INPUT_ROOT`, `LOCAL_ACCOUNT_ROOT` or `LOCAL_CACHE_ROOT` are logical provenance aliases, not missing downloadable files. Original pin hashes in historical receipts continue to identify their original artifact bytes; the derivative inventory identifies the downloadable metadata versions.

Files under `evidence/assembly/` ending `.py` are provenance copies of the local build scripts. Their recorded machine locators are translated to logical aliases, and they are not advertised as portable build tools. The self-contained TeX compile command above is the public rebuild route. Private messages, protected human literature and local credentials are not included.

The package's programme index preserves the existing DOI state. The GitHub publisher supplies a separate additive-publication receipt; this package itself claims no remote write or DOI assignment.
