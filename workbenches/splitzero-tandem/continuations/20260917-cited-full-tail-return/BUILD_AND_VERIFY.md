# Build and verification

From the extracted package root, run:

```text
python verify_package.py
```

This requires Python 3 and no third-party modules. It verifies all listed payload hashes, the four controlling source pins, the exact accepted PDF pins and the three index source snapshots. The manifest intentionally excludes its own bytes to avoid a circular hash. The publication inventory outside the source folder pins the manifest.

The four controlling `.tex` files are complete standalone documents with in-file bibliographies. Optional compilation requires XeLaTeX with Latin Modern Roman, fontspec, fontenc, amsmath, amssymb, amsthm, mathtools, mathrsfs, geometry, longtable, booktabs, url, hyperref, etoolbox and amscd. Use an up-to-date TeX distribution with these packages available. No literature PDFs or private source directories are required.

Create a new output directory named `derived_build`, then run from the package root:

```text
xelatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=derived_build -jobname=FULL_RECEIVER_CUMULATIVE_PROOFS 14_CURRENT_KERNEL_AND_MULTIPLICITY_PROOFS.tex
xelatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=derived_build -jobname=FULL_RECEIVER_PROOF_SUPPLEMENT FULL_RECEIVER_PROOF_SUPPLEMENT.tex
```

Repeat each command until `.aux`, `.toc` and `.out` stop changing (the accepted build used a maximum of four passes). The other two controlling texts can be compiled by substituting their filenames and distinct job names. A rebuilt PDF is a derived artifact, not the supplied accepted byte sequence: metadata, engine and package versions can change output bytes. Do not overwrite the accepted PDFs when testing.

Packaging did not run these compilation commands. The accepted compilation, reference-destination and scoped visual evidence is supplied in `evidence/build/`. Historical warning classes and review-scope limits remain recorded there. The programme index explicitly distinguishes o(aq) estimates from the finer q log a comparison still required by the final exterior benchmark.
