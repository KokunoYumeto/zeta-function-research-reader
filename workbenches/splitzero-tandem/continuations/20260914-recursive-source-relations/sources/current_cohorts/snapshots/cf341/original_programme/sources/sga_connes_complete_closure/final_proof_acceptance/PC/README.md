# Period curvature of the critical-comparison kernel

This source companion contains the complete exponential period determinant (XD1–26), constituent curvature and collision calculation (SC1–37), and the new critical-kernel bridge (PC1–41). The PDF retains the previously verified XD/SC pages and appends the new proof. Its principal result identifies the period curvature with the curvature of the exact critical-comparison kernel, including the arithmetic unit and every surviving or killed jet.

For one packet, the original polynomial is exactly chi_(h,1)=h. The theta section is sigma_h eta_h, where eta_h multiplies by the full jet unit j_h((2 xi)/h). The exact finite kernel is the full off-critical primary summand. At tensor degree k, the factorwise critical comparison has kernel (chi_(crit,k))/(chi_(h,k)); this also retains excess nilpotent jets when distinct tuples have the same sum. The finite image remains injective in the completed projective target because the explicitly weighted critical-jet evaluations give a continuous tensor retraction.

## Read and rebuild

Read `Period_Critical_Kernel_Bridge.pdf`. The new bridge begins at Section 3. The complete editable master is `main.tex`, which inputs the three unchanged proof-body files in `proofs/`. Run the following twice from this folder with a standard TeX installation:

    pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build main.tex

The resulting `build/main.pdf` is copied to the readable PDF filename. No mathematical checker or Lean execution is part of this PDF build.

## Complete local mathematical inputs

- `proofs/exponential_period_determinant.tex`: the entire fixed-ray analytic determinant proof, including repeated-root parameters, constants, and phases.
- `proofs/sga_constituent_curvature.tex`: the entire rank-one normal derivative, curvature, metric transport, collision Tor calculation, and neighboring-minor identity.
- `proofs/period_critical_kernel_bridge.tex`: the entire new source-to-critical-kernel derivation and its completed tensor generalization.
- `dependencies/HOCHSCHILD_COMPARISON.md`: the full accepted public PR27 note H1–42, including the continuous critical quotient, all generalized blocks, the phase i^(-j)/j!, and the source/closure qualifications. This proof dependency is retained beside the PDF rather than duplicated inside it.
- `dependencies/arithmetic_input.tex`: the complete original theta complex, Euler inverses, finite packet section, exact sequence, and original representative extension.
- `dependencies/coherent_tensor_integration.tex`: the complete full-unit coordinate comparison and canonical positive-Gram minimization proof.
- `dependencies/toda_cv_exact_bridge.tex`: the complete original arithmetic unit/source construction, tensor-sum annihilator, original density and mass, and exact source-volume comparisons.
- `dependencies/SGA_TRACE_PERIOD_CONTROL_NOTE.tex`: the complete delivered SGA trace/period note used by the constituent continuation, retaining its attribution and stated source conventions.

Classical published results retain their source references inside these complete proof texts. The new bridge uses the actual inherited analytic maps and their proved identities; it introduces no unproved arithmetic estimate. The fixed period-coordinate metric and the moving original-theta metric are both kept, with the exact derivative terms connecting them.

`SOURCE_FILES.json` records byte-for-byte provenance of every copied proof. `review/` retains the full mathematical readings and the exact scope of prior visual verification. `build/` contains actual TeX logs. The final visual receipt records which pages were newly inspected and which were verified identical to previously inspected pages.
