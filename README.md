# Riemann Zeta Function: Research Reader

## Current calculations: theta norms, kernel layers and symmetric control

**Published:** [Zenodo DOI 10.5281/zenodo.22728704](https://doi.org/10.5281/zenodo.22728704) · [separate PDFs and matching source packages](calculation_edition_20260912b/). That frozen edition includes PRs #14–17 and #19, including repaired #16. PR #18 and the exterior-packet continuation are newer current-repository work.

Start with the [current research guide](CURRENT_RESEARCH.md), which explains the objects, the motivation for each attempt and what it produced. Read the [complete 216-page continuation](workbenches/splitzero-tandem/continuations/20260912-frontier/Split_Zero_Cohomology_and_Arithmetic_Weight_Control.pdf) with its [proofs and checks](workbenches/splitzero-tandem/continuations/20260912-frontier/), or the [433-page main research reader](reader.pdf). Earlier frozen editions below are preserved.

The current reader now includes [alternating/exterior packet-cost calculations](workbenches/exterior-packet-cost/) in Section 38, pages 397–404, with full proof source and exact checkers. This continuing-reader update leaves the frozen DOI edition unchanged.

[What we tried and why](ATTEMPTS.md) · [Structured attempt records](ATTEMPTS.json)

## Earlier calculation edition: SplitZero, theta cohomology and weight control

**Earlier frozen calculation edition:** [separate PDFs and source packages](calculation_edition_20260912/) · [Zenodo DOI](https://zenodo.org/records/22727889). The earlier edition below is preserved.

The September 12 calculations develop support-preserving arithmetic coefficients, the quotient of rapidly decreasing functions by theta-function relations, and finite spectral data attached to zeta's zeros. They calculate explicit comparison maps, homotopies and rank-two matrices in an attempt to obtain the kind of weight control that makes Deligne's Weil II machinery effective. They do not yet establish the needed uniform estimate.

Start with [the research-programme guide](RESEARCH_PROGRAMMES.md): it defines the objects and explains what each attempt was for, what worked and what remains unfinished. Then follow the full proofs and executable checks in each linked workbench. [Machine-readable routes and versions](WORKBENCHES.json) · [September 12 checking and source report](INTEGRATION_REVIEW_20260912.md).

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

The six-reader collection is a frozen, paired edition, not a claim that every working file below is at the same revision. The current root-level main reader is listed below; the frozen collection remains unchanged. The separate [corrected Navier–Stokes edition](https://doi.org/10.5281/zenodo.22678406) and its [reading guide](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/tree/main/navier-stokes) are related work, not the DOI for this collection. The [earlier Navier–Stokes edition](https://doi.org/10.5281/zenodo.22667379) remains available; neither replaces the frozen fluid PDF above. No Millennium-problem resolution is claimed.

<!-- END COLLECTION -->


A living literature-based research reader, with full TeX proofs, bibliographies,
authored calculations and permitted proof certificates. Incoming work retains
its own statements, hypotheses, qualifications and proof/sketch status.
Mirroring is not a mathematical audit or an endorsement of an endpoint claim.

| Reader | PDF | Pages in this snapshot |
|---|---|---:|
| main | [Read PDF](reader.pdf) | 433 |
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

The recurring Overleaf mirror timer was removed on 9 September 2026 at the owner’s request. Updates are manual for now. The latest manual attempt returned an unavailable browser connection; no visible window opened and no newer Overleaf synchronization is claimed.

## References and provenance

Human-source attribution and citations are retained in the mathematical texts,
including the [main bibliography](satellites/90_references.tex), and the
[GCT cumulative bibliography](sidebar/gct/complete_bibliography.bib).
The contributing-model disclosure remains in the main reader. It is not a
substitute for human-source citations or authorship responsibility.

## Checking and building

The TeX, bibliographies, authored code and permitted certificates are included.
Build the main reader from repository root with `pdflatex main.tex` until cross-references and contents page numbers stabilize (normally three passes from clean auxiliary files);
follow each sidebar's README for its own entrypoint and mathematical checks.
Some administrative seal scripts refer to private continuity/provenance files
that are deliberately not included and are not required to read the proofs.
That statement of the original mirror's scope remains historical. The September 12 workbench integration separately replayed its finite tests and checked the exact successful Lean source run; see [the checking report](INTEGRATION_REVIEW_20260912.md). These checks do not retroactively certify all frozen readers.

## Rights and privacy

See [RIGHTS.md](RIGHTS.md) and the exact per-file [manifest](PUBLIC_FILE_MANIFEST.json).
Protected literature shelves, source books/PDFs, raw transcripts, credentials,
and private continuity logs are excluded. Publication copies mechanically mask
identifying paths; private JSON metadata may be omitted. Mathematical TeX is
not abridged or rewritten. Metadata-derived certificates are identified as
publication copies, not falsely described as byte-identical private originals.
