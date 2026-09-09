# Riemann Zeta Function: Research Reader

[What we tried and why](ATTEMPTS.md) · [Structured attempt records](ATTEMPTS.json)

## Six-reader collection

Start with the [complete six-reader edition](zenodo_collection_20260909_main411/). It includes separate PDFs and a [complete source ZIP](zenodo_collection_20260909_main411/07-complete-mathematical-sources.zip) of their paired source trees.

This GitHub repository is the living research repository. The frozen 2026-09-09 six-reader edition is archived on [Zenodo](https://zenodo.org/records/22678086), with DOI [10.5281/zenodo.22678086](https://doi.org/10.5281/zenodo.22678086) assigned by Zenodo.

[Archived main PDF](https://zenodo.org/records/22678086/files/01-main-reader.pdf?download=1) · [Download archived source ZIP](https://zenodo.org/records/22678086/files/07-complete-mathematical-sources.zip?download=1).

| Subject | Reader | Pages |
|---|---|---:|
| Zeta and exact correspondences | [Main PDF](zenodo_collection_20260909_main411/01-main-reader.pdf) | 411 |
| Fluid equations | [Fluid PDF](zenodo_collection_20260909_main411/02-fluid-reader.pdf) | 208 |
| Heat transport | [Heat PDF](zenodo_collection_20260909_main411/03-heat-reader.pdf) | 120 |
| Arithmetic trace quotients | [Connes PDF](zenodo_collection_20260909_main411/04-connes-reader.pdf) | 82 |
| Geometric complexity | [GCT PDF](zenodo_collection_20260909_main411/05-gct-reader.pdf) | 174 |
| Vacuum and gravity | [Vacuum PDF](zenodo_collection_20260909_main411/06-vacuum-reader.pdf) | 37 |

The six-reader collection is a frozen, paired edition, not a claim that every working file below is at the same revision. The older root-level mirror is retained below. The separate [corrected Navier–Stokes edition](https://doi.org/10.5281/zenodo.22678406) and its [reading guide](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/tree/main/navier-stokes) are related work, not the DOI for this collection. The [earlier Navier–Stokes edition](https://doi.org/10.5281/zenodo.22667379) remains available; neither replaces the frozen fluid PDF above. No Millennium-problem resolution is claimed.

<!-- END COLLECTION -->


A living literature-based research reader, with full TeX proofs, bibliographies,
authored calculations and permitted proof certificates. Incoming work retains
its own statements, hypotheses, qualifications and proof/sketch status.
Mirroring is not a mathematical audit or an endorsement of an endpoint claim.

| Reader | PDF | Pages in this snapshot |
|---|---|---:|
| main | [Read PDF](reader.pdf) | 377 |
| fluid | [Read PDF](sidebar/fluid/reader.pdf) | 208 |
| heat | [Read PDF](sidebar/heat/reader.pdf) | 120 |
| connes | [Read PDF](sidebar/connes/reader.pdf) | 82 |
| gct | [Read PDF](sidebar/gct/reader.pdf) | 149 |

The main TeX entrypoint is [main.tex](main.tex). The complete incoming texts
are indexed in [SIDEBAR_WORK.md](SIDEBAR_WORK.md), with their own source trees
under `sidebar/fluid`, `sidebar/heat`, `sidebar/connes` and `sidebar/gct`.
The [sidebar compendium](sidebar-work.tex) includes the four complete PDFs.

## Relationship to Overleaf

[Canonical Overleaf project](https://www.overleaf.com/project/6a8c9ff10c2a1270c918f8b7). This repository
publishes the current authorized **local** snapshot. The last independently
confirmed Overleaf main build had 272 pages; current
Overleaf synchronization must not be inferred from this GitHub commit.
See [MIRROR_STATUS.json](MIRROR_STATUS.json) for exact snapshot status.

The recurring Overleaf mirror timer was removed on 9 September 2026 at the owner’s request. Updates are manual for now. The latest manual connection attempt could not access an authenticated browser, so no newer Overleaf synchronization is claimed.

## References and provenance

Human-source attribution and citations are retained in the mathematical texts,
including the [main bibliography](satellites/90_references.tex), and the
[GCT cumulative bibliography](sidebar/gct/complete_bibliography.bib).
The contributing-model disclosure remains in the main reader. It is not a
substitute for human-source citations or authorship responsibility.

## Checking and building

The TeX, bibliographies, authored code and permitted certificates are included.
Build the main reader from repository root with `pdflatex main.tex` twice;
follow each sidebar's README for its own entrypoint and mathematical checks.
Some administrative seal scripts refer to private continuity/provenance files
that are deliberately not included and are not required to read the proofs.
No proof checks were rerun as part of this mirror publication.

## Rights and privacy

See [RIGHTS.md](RIGHTS.md) and the exact per-file [manifest](PUBLIC_FILE_MANIFEST.json).
Protected literature shelves, source books/PDFs, raw transcripts, credentials,
and private continuity logs are excluded. Publication copies mechanically mask
identifying paths; private JSON metadata may be omitted. Mathematical TeX is
not abridged or rewritten. Metadata-derived certificates are identified as
publication copies, not falsely described as byte-identical private originals.
