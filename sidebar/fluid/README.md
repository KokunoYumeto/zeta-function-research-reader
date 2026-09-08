# Exact fluid constructions and the Navier–Stokes question

This active research notebook reconstructs exact fluid layers, their viscosity terms, predecessor scale estimates, and concrete maps from the earlier polynomial, S6 and arithmetic work. The current cumulative reader does not establish a classical Navier–Stokes counterexample. A 165-page classical manuscript has now been released and obtained; its complete independent reconstruction is the current priority. The original discovery transcript has not been obtained.

The new primary sources are [Finite time blowup for Navier–Stokes](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf) and its [formalization repository](https://github.com/openai/NavierStokesAndEuler). The manuscript SHA-256 is 8c8a94ad9ac824c8b605b9827cadf7beaca48bd10b380de3cfc872a2c37afa81. Its release supersedes earlier availability statements in the existing reader. Acquisition and partial review do not yet amount to independent validation of all its arguments.

Read `tex/main.pdf`, or build it from `tex/main.tex`. The mathematical sections retain original coordinates, signs, constants, domains, data and forces. The source estimates used from external blowup papers are explicitly identified; this repository does not certify those complete external proofs. The newly proved finite constructions and identities have written analytical proofs and supplementary exact symbolic checks.

`reconstruction.json` contains the complete notebook source and replay code, source receipts, and check results. It is a newly produced reconstruction record, not an original external discovery transcript. Its embedded files have SHA-256 hashes. To recover them into a new directory, run:

```text
python scripts/extract_reconstruction.py reconstruction.json extracted-notebook
```

Install the dependency from `requirements.txt`, then replay the exact checks:

```text
python -m pip install -r requirements.txt
python scripts/verify_all.py
```

The replay requires no network access, sibling project, or Lean installation once SymPy is installed. Written analytical arguments supply the claims beyond symbolic identities. To build the reader, install a LaTeX distribution with the packages named in `tex/main.tex`, make `pdflatex` available, and run:

```text
python scripts/build_pdf.py
```

The source trail begins with the four-page Buckmaster statement, the released Alpöge–Buckmaster fluid papers, and the Córdoba–Martínez-Zoroa–Zheng dissipative predecessor. Full citations and attribution appear in the reader. No prize claim is made by this notebook. Public posting has not been performed as part of this reconstruction.

The released classical proof now has a dedicated reader: build it with `python scripts/build_released_ns_reader.py` and read [`tex/released_ns_reader.pdf`](tex/released_ns_reader.pdf). The accompanying [`released_ns_primary.json`](released_ns_primary.json) records the exact source URL, 165-page source hash, pinned formal repository, component proof files, and scope-limited validation receipts. It distinguishes the source manuscript's theorem statement from the independent checks; complete validation remains active after reconstruction and correction of the Section9 stage assembly and its imported interfaces.
The current primary reader has76 pages and six complete component bodies. Its43-file standalone bundle is [`released-ns-reader-2026-09-08.zip`](released-ns-reader-2026-09-08.zip), SHA-256 `678e9a14e64641c8427b42aa57bbbdae5ab5f5f0a6590f0be7811e2c3f9e8bd1`. The JSON embeds41 text/code files. All five included replay programs pass after fresh extraction; all76 pages have rendered-layout review. These checks do not certify the full theorem. The pinned Lean source closure is actively compiling under the coordinated single-worker policy.

The cumulative reader also includes the complete audited additions from the supplied web-research report, the coupled growth/steering/holding calculation with physical diffusion, and the axis-crossing three-dimensional/five-dimensional transfer. The incoming report is source material; its assertions are not automatically certified by inclusion in the research archive. Integration records preserve the exact source hashes, executable checks, and the scope of cited external theorems.

The completed arithmetic additions retain the original inverse cover, the actual Newman heat function and its analytic factors, the full Euclidean observable, and both successive diffusion calculations. The Gaussian family calculation includes its complete pressure and force, all derivative bounds, and every amplitude and exponent case. Each conclusion applies to the explicitly defined objects in its proof.

The fourth-order lattice spectral calculation is included with its entire source proof, the derivative distribution and both spin channels, the physical parameter path, its exact heat transport, and the inverse Fourier multiplier on the stated function space. The moving-center calculation proves the full velocity, pressure and force maps and their inverses. For the specified Gaussian family, a paired-point calculation retains every center derivative and proves the force-derivative bound for every smooth center curve and every real exponent.

The [Overleaf working mirror](https://www.overleaf.com/project/6aa00ea8d33adcc58f39d8df) was last verified at 78 pages. A later cumulative update is prepared, but authenticated browser access became unavailable before upload. The local reader and reconstruction record contain the subsequent completed mathematics. Only explicitly selected mathematical files and provenance are included, without private conversation logs.
