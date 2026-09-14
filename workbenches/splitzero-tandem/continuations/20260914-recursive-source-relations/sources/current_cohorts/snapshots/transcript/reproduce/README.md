# Reproduction from this standalone repository

The portable transcript and audit checks need Python 3; both verifiers use its standard library. Run from any directory by supplying the path to these scripts:

    python verify_transcript.py
    python -X utf8 verify_audit.py

The original scripts and their historical receipts remain in the source/validation records. The portable copies only change path discovery; the separate portable-run receipt verifies the delivered audit files themselves.

To compile the proof volume, change to publication and run LuaLaTeX on actual-cohomology-proofs.tex twice. The root TeX uses only its bundled fragments and standard TeX packages, with Latin Modern text and math fonts. To rebuild the ledger, follow ledger_publication/README.md and its bundled build script or compile the supplied complete ledger.tex using the engine recorded there. The optional Markdown regeneration uses Pandoc.

After both PDFs have been rebuilt, run assemble_reading_edition.py with PyMuPDF installed. It combines their pages without scaling and checks identical page text, geometry and rendered pixels against both input volumes. This creates the final reading PDF and a separate combination-QA receipt.

The extraction script uses BeautifulSoup and decodes the saved public page's JSON reference table without executing its JavaScript. The delivered complete source and individual turn files can be checked without refetching the network. The published share's explicit redactions remain redactions in every reproduced edition.

MANIFEST.json at the repository root lists the retained file hashes and exact sizes. ZIP_RECEIPT.json beside the distributed archive records the full archive hash and the successful full-byte/CRC check of every member. Those records certify the bytes of this edition, not a rerun of every inherited source calculation.
