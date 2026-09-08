# Riemann Zeta Function: Research Reader

A living literature-based research reader, with full TeX proofs, bibliographies,
authored calculations and permitted proof certificates. Incoming work retains
its own statements, hypotheses, qualifications and proof/sketch status.
Mirroring is not a mathematical audit or an endorsement of an endpoint claim.

| Reader | PDF | Pages in this snapshot |
|---|---|---:|
| main | [Read PDF](reader.pdf) | 338 |
| fluid | [Read PDF](sidebar/fluid/reader.pdf) | 208 |
| heat | [Read PDF](sidebar/heat/reader.pdf) | 96 |
| connes | [Read PDF](sidebar/connes/reader.pdf) | 62 |
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
