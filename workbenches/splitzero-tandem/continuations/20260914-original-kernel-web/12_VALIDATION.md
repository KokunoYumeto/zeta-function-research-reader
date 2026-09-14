# Validation of the flat continuation folder
This folder contains one current continuation prompt, one previously inspected PDF, and the complete editable TeX proof files. No subfolders or ZIP archives are required.
The 75-page PDF is an exact copy of the accepted reader. All 75 actual pages were visually inspected for its frozen edition. The newer TeX files are source editions: their source-only builds do not claim a new visual PDF review.
| TeX file | Source check | XDV pages | External TeX files |
|---|---|---:|---:|
| 02_FULL_GAMMA_PROOFS.tex | 3 successful XeLaTeX `-no-pdf` passes | 243 | 0 |
| 03_FULL_OBSERVATION_PROOFS.tex | 3 successful XeLaTeX `-no-pdf` passes | 22 | 0 |
| 04_CYCLIC_SECTORS.tex | 3 successful XeLaTeX `-no-pdf` passes | 8 | 0 |
| 05_ORBIT_CONDUCTOR.tex | 3 successful XeLaTeX `-no-pdf` passes | 6 | 0 |
| 06_ACTUAL_PERIOD_QUADRIC.tex | 3 successful XeLaTeX `-no-pdf` passes | 10 | 0 |
| 07_ORIGINAL_KERNEL_VOLUME_BOUND.tex | 3 successful XeLaTeX `-no-pdf` passes | 6 | 0 |
| 08_ORIGINAL_MIXED_CONTROL.tex | 3 successful XeLaTeX `-no-pdf` passes | 3 | 0 |
| 09_UPDATED_JOINT_NOTE.tex | 3 successful XeLaTeX `-no-pdf` passes | 110 | 0 |
| 10_UPDATED_SIGNED_RETURN.tex | 3 successful XeLaTeX `-no-pdf` passes | 104 | 0 |
| 13_ARITHMETIC_MIXED_TRANSFER.tex | 3 successful XeLaTeX `-no-pdf` passes | 10 | 0 |

Every literal source input was expanded. Actual compiler input records confirmed that each TeX file builds without another TeX source file. Standard TeX packages and fonts are the only build dependencies; the source wrappers use standard TeX-distribution fonts.

Every declared original source and selected proof-span hash was checked. Full mathematical proof content is retained across the numbered TeX files. Historical path references are provenance locators; the exact paths, hashes, spans, inline expansions and reversible display-wrapper edits are recorded in `11_SOURCE_MAP.json`.

A separate source-preservation review of files 02-10 reversed the recorded document edits and recovered every complete original provider and all27 selected proof spans exactly. It found no proof truncation or external TeX input. Its pinned receipt is embedded in the source map.

File13 separately passed an exact full-source check: the complete accepted AMT1-49 original bytes occur once, unchanged, inside the standalone wrapper. Its source and output hashes are recorded in the map.

The full incoming historical proofs occupy 23 provider families and 27 selected complete proof spans. Foundational Fourier, complex-analysis and special-function inputs remain explicitly cited in those sources and in the source map. The source check verifies portability and TeX syntax; it does not claim a new independent mathematical audit.

No original research source or sealed cut22 file was modified. Historical proof displays retain some overfull/underfull warnings in source-only builds; no additional PDF was created from these source editions.
