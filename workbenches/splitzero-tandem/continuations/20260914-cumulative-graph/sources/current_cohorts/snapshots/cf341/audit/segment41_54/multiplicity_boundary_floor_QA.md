# Multiplicity boundary-floor TeX conversion record

The parent requested conversion of the complete new invariant-trace, invariant-subspace projection, multiplicity boundary-floor, and counterfactual proof into a standalone includable TeX module, with no preamble and no edits to the global document.

Delivered module: multiplicity_boundary_floor.tex.

- Begins with a section; uses no theorem environment or custom macro.
- Requires only standard LaTeX plus amsmath and amssymb.
- All 47 labels use the BF: prefix; the 41 explicit equation tags run from BF.01 through BF.41.
- Source definitions and authoritative A1644/A1771 message and line pins are included.
- Full original constants, polynomial coordinates, extension unit and row, norm squares, local jet lengths, and the half-line measure dx are retained.
- General nonstable-packet one-sided estimates precede the reflection-stable packet combination. No residue self-duality is asserted for a nonstable packet.
- Empty packets, zero invariant subspaces, missing signed eigenvalues and their projections, and tensor powers k >= 1 are explicit.
- The indefinite rank-two conclusion expressly requires a reflection-stable actual packet containing an off-line root.

An independent agent read the complete module and checked the mathematical proof, constants, signs, equation references, and edge cases. Its two notation recommendations were incorporated: the restricted Gram formulas are invoked only on nonzero invariant subspaces, and the Fourier convention and homotopy-map domains are fully defined.

A temporary test wrapper in _bf_tex_check/bf_compile_check.tex loads only amsmath and amssymb, uses article at 11pt with text width 460pt, and inputs the module. After syntax/layout repair and the reference-resolving run, pdflatex returned exit code 0 and produced an 11-page PDF. The final log has no Warning, Overfull, Underfull, or error entries. This compile verifies TeX integration in that wrapper; the parent remains responsible for the final combined document layout.

Final module SHA256: CFC188BB8E0A6081BE52C144AFF9FB325CA563DBA7A44C411C8F9CBF3118BD17.
