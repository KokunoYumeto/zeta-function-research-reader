# Complete proof modules for parent integration

Use these three final, standalone includable proof modules, in this order or separately:

1. multiplicity_boundary_floor.tex — complete actual-source construction, invariant trace, rank-two compression, full multiplicity floor, arbitrary/reflected packet qualification, quartet and tensor consequences. Tags BF.01–BF.41.
2. symmetric_frontier_determinant.tex — complete arithmetic minimum, relation/frontier map, recurrence and exact Gamma proof, signed symmetric projector, original orbit factors, aggregate Schur/composition calculation, coordinate invariance, determinant product and signed witness. Forty-four FD-prefixed tags.
3. conormal_jacobian_symmetric_trace.tex — complete original-source pin and arithmetic injection, CRT construction, conormal domain, all C1–C25 proofs including C17a/b, ordered residue and nondegeneracy, intrinsic symmetric trace comparison, exact source representatives, complete inertia, and individual exact sum-fibre restrictions.

Each begins with \section, contains no preamble or custom theorem environments, and defines its introduced notation. Required math packages for the three together are amsmath, amssymb, mathrsfs. BF and FD individually use only amsmath, amssymb. Do not input the helper conormal_source_header.tex separately: it is already embedded verbatim into the complete C module.

The tex_module_inventory.json file contains final content hashes, sizes, all equation tags and labels. The check_tex_module_inventory.py script verifies the no-preamble contract and confirms 112 unique equation tags, 99 unique labels, and preservation of C1–C25 plus C17a/b.

The final complete modules were compiled together using all_proof_modules_compile_check.tex in pdflatex -draftmode, with A4, 23mm margins and 11pt article. The final pass is clean: no LaTeX warnings, undefined references, overfull or underfull boxes, or errors. It paginates to 26 pages in that wrapper. No PDF was authored in this combined check; the parent remains responsible for visual verification of the assembled readable artifact.

The mathematical source reports and independent reviews remain in this directory. The BF and FD proof authors independently reviewed their complete TeX modules and incorporated endpoint/domain/notation corrections. The C module preserves every mathematical conclusion of its reviewed Markdown proof and adds explicit source-domain, CRT, residue, and cohomology-injection proofs needed to make all its symbols and maps reviewable in the included module.

No global TeX, publication, or external application was edited in this subtask.
