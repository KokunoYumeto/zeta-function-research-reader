# The original observation and its mixed factors

Open `Original_Observation_Addendum.tex` for the complete editable entry. It contains the accepted OPG1–26 calculation, its exact OPR receiver interface, and the complete required proof spans for the source norms, mixed rows and original period isomorphism.

- `sources/OPG.tex`: full new original observation calculation.
- `sources/OPR.tex`: exact map into the original MRI kernel and boundary factors.
- `sources/OGN.tex`: full norms of the two existing Gamma sources.
- `sources/PGCC.tex`: complete Gamma grid-product proof for the original period determinant constant.
- `proofs/`: exact required spans copied from the original complete providers.
- `originals/`: complete unchanged BRU, PDE, IPM, IGO and GMB editions.
- `review/`: independent proof reviews and source locators.
- `SOURCE_DEPENDENCIES.json`: full source hashes, exact copied byte ranges, equation ranges and mathematical dependency routes.
- `NEXT_RECEIVING_INTERFACE.md`: precise next MRI/BRI integration against the preserved frozen receiver bodies.

The entry uses XeLaTeX and ordinary AMS packages. All of its input paths are relative to this folder. Two source-only XeLaTeX runs passed; see `BUILD_CHECK.md` for the exact scope and the two inherited layout warnings. To typeset a PDF, run `xelatex -interaction=nonstopmode -halt-on-error Original_Observation_Addendum.tex` twice from this folder and inspect its rendered pages. The main Cut 22 PDF remains unchanged. This package delivers editable source; a rendered addendum PDF and its visual layout check are not claimed here. Run `python verify_sources.py` to check the included byte-preservation and relative-input records.

All original unit derivatives, nilpotents, source masses, centres, contour orientations and cyclic-average terms remain in the proofs. The source orders are the already existing 1 and k. OPG and OPR retain the actual observation kernel and its action defect.
