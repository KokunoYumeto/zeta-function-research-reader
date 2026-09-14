# Circle and critical observations of the original arithmetic source

Read Circle_Critical_Observation_Diamond.pdf. The complete new proof DC1–DC30 follows the unchanged exponential determinant XD1–26, constituent curvature SC1–37, and period/critical-kernel bridge PC1–41.

The joint observation is exactly the fibre product of the two actual images over the quotient by gcd(chi_crit,k,p_L), and is realized by the quotient by their lcm. The source retains chi_h,k, all tuple collisions, all higher jets, the full tensor arithmetic unit, the critical derivative phases, and the original circle Fourier amplitudes and weights. The proof calculates the actual factorization maps in both directions, the entire extra circle summand, an explicit polynomial source lift, and every transported action and differential defect.

For k=1 the full local unit proves that every sampled selected h-root has positive weight, even if other circle atoms have zero weight. This gives the precise factorization through the critical observation. At every tensor degree the min/max local exponents retain the complete relationship.

## Editable source and rebuild

The master is main.tex and every included mathematical body is in proofs/. From this folder, run twice:

    pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build main.tex

The resulting build/main.pdf is copied to Circle_Critical_Observation_Diamond.pdf. The dependency files are retained as complete texts beside this PDF:

- dependencies/PERIODIZED_SOURCE_CONTROL_NOTE.tex: the entire delivered P1–P64 proof, including source coordinates, Fourier factors, weighted circle completion, all kernel proofs, and the source metric estimates.
- dependencies/HOCHSCHILD_COMPARISON.md: the entire accepted PR27 H1–H42 proof, retained as an adjacent analytic dependency.
- dependencies/arithmetic_input.tex, coherent_tensor_integration.tex, and toda_cv_exact_bridge.tex: the complete original theta source, local arithmetic units, Gram minimization, and cyclic tensor source proofs.
- dependencies/SGA_TRACE_PERIOD_CONTROL_NOTE.tex: the complete delivered period-control note used by the constituent continuation.
- proofs/exponential_period_determinant.tex, sga_constituent_curvature.tex, and period_critical_kernel_bridge.tex: complete unchanged XD, SC, and PC proof bodies, included in the PDF.
- proofs/circle_critical_observation_diamond.tex: the complete new DC1–DC30 calculation, included in the PDF.

Paths within the proof bodies identify their original source locations; the corresponding complete files are supplied here under the explicit mapping above. No attached source is reduced to a theorem list. No new arithmetic upper estimate is claimed.

SOURCE_FILES.json pins every copied source. The review folder retains full mathematical readings, source provenance, the prior page verification and the final visual receipt. Build logs record the actual typesetting commands. The earlier 18 rendered pages are reused only after exact byte and pixel comparison; the appended proof pages are individually inspected. No Lean or numerical test execution is claimed by the PDF build.
