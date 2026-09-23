# All-prime tensor boundary weights and the original support receiver

The [eight-page paper](ROOT_BOUNDARY_WEIGHT_HOMOLOGY.pdf) computes all tensor powers of the arithmetic boundary obtained by evaluation at supported zero and integration at every place. It keeps the original rational and idele actions, all Haar factors, both sign projectors, and the entire coefficient support lattice. [Complete LaTeX](ROOT_BOUNDARY_WEIGHT_HOMOLOGY.tex) and [clickable proof/result index](RESULT_INDEX.json) accompany the paper.

The main result identifies every rational tensor coinvariant and all group-homology degrees. It calculates the actual idele weight on each component. A specific mixed tensor class survives this calculation but vanishes in the tensor of the two-endpoint quotient. The exact connecting map goes back into the original Schwartz-kernel homology. This supplies a boundary term needed by the programme's weight construction; it does not prove interior purity or decide RH.

The complete independent tensor derivation is [TB1–29](INDEPENDENT_BOUNDARY_TENSOR_WEIGHTS.tex). The [bounded homology review](INDEPENDENT_BOUNDARY_HOMOLOGY_AUDIT.md) identified the sign-projector correction now present in BW20–22; [the final correction receipt](LITERATURE_BOUNDARY_RECEIVER_REVIEW.md) states the publisher's reading scope. The original 187 exact finite checks are preserved; the packaged checker was rerun independently with only its dependency path changed. The original predecessor components and complete public 031 proof source are included in sources/.

Human attribution and exact reading coverage are in [SOURCE_READING.json](SOURCE_READING.json) and the paper's point-of-use citations to Pierre Deligne and Alain Connes. The new balanced-space, homology and support-map calculations are programme derivations, not claims attributed to those authors. Primary human works are linked at their original hosts, not redistributed here.

## Reproduce

Compile ROOT_BOUNDARY_WEIGHT_HOMOLOGY.tex with pdflatex twice in this directory; the included PNG supplies the figure. The complete figure source and SVG are retained. Run check_boundary_tensor_weights.py with Python and SymPy to reproduce the exact finite checks. They supplement rather than replace the full proofs. The PDF was rendered and every page inspected; the full formula BW15 was wrapped without changing its terms. No former sealed edition was modified.
