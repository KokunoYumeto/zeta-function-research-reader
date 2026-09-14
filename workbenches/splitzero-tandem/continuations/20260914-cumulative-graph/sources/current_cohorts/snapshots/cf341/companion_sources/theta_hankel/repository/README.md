# Original theta moments and Hankel certification

The complete readable paper is **Tau_Theta_Hankel_Complete_Proofs.pdf**.
Its first five pages give the original theta-tail estimates, exact moment
and logarithmic-coefficient maps, finite rational witnesses, and the
certified calculation. The following 42 pages contain nine complete proof
bodies: the original counterfactual workbench, its independent packet proof,
the numerical method and analytic reviews, the full genus-zero product
proof, and the final independent proof with explicit theta-growth constants.

For the unchanged function F(z²)=2 xi(1/2+iz), both original matrices
H15=(b[i+j]) and H15^(1)=(b[i+j+1]), 0<=i,j<=15, are positive definite.
The 33 original moments M0,M2,...,M64 are obtained from the original theta
integral, retaining its original mass, all negative summands and both
factors of two. The omitted n and y regions have proved positive upper
bounds. All 32 original pivots and 32 leading determinants have strictly
positive lower endpoints. This statement concerns these finite matrices.

TC21–26 also gives an explicit separator degree and rational coefficient
accuracy for every off-real reciprocal zero. WBR retains the complete
original packet, reflected primary blocks, nilpotent inverse, half-trace,
theta boundary and critical-observation defect. GF and GFR provide the full
product and growth arguments used by that scalar trace map. Every proof is
included; the analytic endpoint of the broader research programme is not
asserted here.

## Editable sources

`Tau_Theta_Hankel_Certification.tex` includes the full TC proof in
`proofs/TC.tex`. `support_reader/main.tex` includes every complete converted
proof in `support_reader/typed/`. Their exact originals, original preambles,
parsed Markdown trees and reversible layout records are retained alongside
them. The source-pin table and CLI option typography have recorded layout
adaptations; mathematical payloads and original files are retained.

The archived Workbench note and its exploratory numerical runs are retained
under `dependencies/RH_Counterfactual_Workbench/`. Its nu_N/u_N typo is
repaired by the explicit identity nu_N:=u_N in the later proofs. The early
workbench and review correctly describe their own unvalidated numerical
stage; the later TC/CH certificate supplies the finite analytic enclosures.
The earlier root acceptance predates the final independent GFR review.
Two preserved reviews use the same TR equation prefix; cite their chapter
title together with the equation number.

## Reproduce the exact integer verification

Use Python 3.11 or later, without optimization. This command uses only the
Python standard library and reconstructs the coefficients and both LDL
recursions from the exported finite-integral pieces and tail upper bounds:

```sh
python verify_exact_rational.py
```

It checks 1,400 exact endpoint pairs and writes
`exact_rational_reproduction.json`. The original and fresh integration
records agree in every numerical field; elapsed times and platform labels
are not mathematical inputs. The recurrence verifier uses integer
intervals on the grid with denominator 2^4096. The proved finite-piece
integration enclosures remain its explicitly identified analytic inputs.

## Recompute the original theta integrals

Install `requirements-calculation.txt`, then run:

```sh
python calculation/certify_theta_hankel.py --dimension 16 --precision 1024 --target-bits 850 --first-omitted-n 20 --length 4 --output fresh_theta_certificate.json
```

This uses python-flint 0.9.0 validated complex-ball integration. The retained
finite interval is split into eight exact half-unit pieces. The source and
API contract, explicit tail proofs, exact dyadic exporter, all saved
intervals and independent integer arithmetic are included. The original
decimal-only replay and its stricter input-contract verifier are retained
separately with their exact finite scope.

## Rebuild the PDFs

Install `requirements-pdf.txt` and provide pdflatex and lualatex with the
packages listed in the two preambles, then run:

```sh
python rebuild_pdfs.py
```

The typed proof bodies are already supplied, so Pandoc is not required to
rebuild the PDFs. All 47 pages of the distributed combined PDF were checked
to render identically to their reviewed component pages. PDF byte hashes
can change on recompilation because the TeX engines record build metadata.

`MANIFEST.json` pins every distributed file except itself. The package
retains complete mathematical sources and calculations. A separate metadata
map records the replacement of three local machine paths in a review
receipt; its mathematical findings and source hashes remain unchanged.
