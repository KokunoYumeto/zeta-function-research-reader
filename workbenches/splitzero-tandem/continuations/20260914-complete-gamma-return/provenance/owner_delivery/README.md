# Complete original Gamma return

Read `Complete_Gamma_Return.pdf` (15 pages), then `00_CONTINUE_THE_PROGRAMME.md`.
The PDF prints the entire LET1–21, PHT1–23 including PHT17a, and HCT1–39
proof bodies. All 84 original equation tags are retained. The continuation
prompt is the exact current mathematical owner's text; the accompanying
`CURRENT_RESEARCH_WORKFLOW_4000_CHARS.md` contains exactly 4,000 characters.

The full editable entrypoint is `Complete_Gamma_Return.tex`. `originals/`
holds all three author documents byte-for-byte. `sources/` holds the full
compiled bodies. `SOURCE_TRANSPORTS.json` records the reversible wrapper,
input-path, line-width, bookmark and single-display pagination changes.
Reversing them reproduces each entire original source. `BUILD_VISUAL_RECEIPT.json`
binds the actual compiled source closure, accepted PDF and all-page review.

The full current receiving successors are in `dependencies/complete_gamma_receiving/`,
including the complete NOTE and JSR texts and their WRC receiving proof.
Their final copy receipt is `provenance/COMPLETE_GAMMA_RECEIVING_COPY_RECEIPT.json`.
The preceding full receivers are retained in `dependencies/current_receiving/`;
`dependencies/bulk_sources/` contains the complete BRD, FTC, CTR and IBC providers;
`dependencies/joint_schur_previous/` retains all preceding textual proof and
provenance dependencies. Its 50 duplicate PDF/ZIP/PNG files are individually
inventoried as omitted in `provenance/DEPENDENCY_COPY_RECEIPT.json`; every textual
proof remains present. Final root and independent proof acceptances are copied
verbatim under `provenance/proof_acceptance/`.

The earlier 2,343-page cumulative volume and the separate 27-, 46- and 33-page
readers retain their historical source cuts. This supplement supplies the full
later proofs and current receiving sources. It does not replace their sealed
PDF bytes. `history/` here preserves the two earlier presentation builds,
including the actual review that found the HCT39 page break; the final PDF has
that display together and no pending visual defects.

For a portable rebuild, use XeLaTeX with the Cambria, Calibri and Consolas fonts
and the packages declared in the main TeX. Run `xelatex -interaction=nonstopmode
-halt-on-error -file-line-error -recorder Complete_Gamma_Return.tex` three times
from an extracted copy. Alternatively, `python prepare_and_build.py build` uses
XeLaTeX on PATH or `XELATEX_BIN` and requires PyMuPDF for the build receipt.
The `prepare`, presentation-repair and sealing commands document one-time
construction steps; existing final source snapshots must be preserved.
Rebuilding can change PDF metadata, so the supplied receipt pins the delivered
PDF rather than promising a binary-identical rebuild.

`Complete_Gamma_Return_Source.zip` contains this complete source/dependency,
PDF, provenance, history and visual-review tree. `ARCHIVE_MANIFEST.json` lists
every archive member; `DELIVERY_RECEIPT.json` records byte-for-byte extraction,
CRC and stable-tree checks. Those two post-archive seals and the ZIP itself are
outside the archive to avoid self-reference. No files outside this folder are
modified by its packaging script.
