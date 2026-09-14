# Exact primary cyclic lattice: durable record

This bounded subtask belongs to `/root/purity_program/tensor_cyclic_lattice`.
The parent owns the active goal, cumulative manuscript and user provenance.
No main source outside this directory is edited by this subtask.

## Parent assignment (verbatim)

> New bounded exact p-local cyclic lattice proof from parent root, disjoint from main complex and finite-field sheaf. Work actual ordered k tensor primary algebra E_R=R[y1..yk]/(yi^m), K=k(m−1), p>m, R actual retained coefficient ring localized at denominators prime to p / p-local suitable flat domain char0, includes full unit and inverse. J=sum yi. Original cyclic map R[T]/T^(K+1)→E_R sends T^r→J^r, full multiplier U retained (commutesJ, invertible). Construct V_r=Σ_{sum b=r,0<=b<m}1/prod b_i! y^b (denominators units p>m), J^r=r! V_r, JV_r=(r+1)V_(r+1). Primitive direct summand spanV_r (one unit coordinate each distinct degree) and originalimage diagonal(r!) into it; original multiplier transportswholelattice (do notreplaceoriginalmap). Cokernel ⊕R/(r!), p-depth v_p(r!) exactfloor sum; derive basechange reducedmapkernel spanT^p..T^K ifK>=p, nilpotency min(p,K+1), Tor1 lostdirections. Tie exact ideal chains/sum/intersection/product to original support type G_Cn via explicit maps if original definition source accessible; do not invent comparison. Main finitefield child owns sheaf Kummer/Gauss/inertia and will distinguish charp coefficient reduction from Ql scalar. Your module own total_object/tensor_primary_cyclic_lattice/tensor_primary_cyclic_lattice.tex tags TCL, no main edits. Prove all definitions/maps and corrected ring assumptions (avoid claiming general coefficient R is DVR). Parent requests actual map of retained coefficient specialization, no hypothetical missing assumptions. Can use universal Z_(p)[rho,a0^±,ai,...] base-change to given retained ring if needed but don't replaceactualring. Need review by independent child ifslot. Send progress.

## Parent precision (verbatim)

> Root precision: use retained coefficient ring localized at an ACTUAL prime ideal over p (p>m). Do not assert α exists if original full-quartet cyclic CRT stage already inverts p via differences of amplified grid centres. State local single-primary map directly, no quartet idempotent required. S=R_m subsetC domain, pnonunit nonzerodivisor, all other integersunits. V_r hasunitcoordinate extendsS-basis. FullU multiplication invertible transportscokernel. If alloriginalMAIstagecoeffspecialize then terminalscalarformulaapplies; otherwise nonexistentα not vanishedvector. Please inspect originalfullquartetCRT denominators enough to show specific p≤k obstruction if useful; source mixed_amplification_identity.tex/PAM.1–5. Own exactlatticemap enough, root handlesgenealogy.

## Source reads and pins

- `../full_mixed_carrier_attachment.tex`: MFC.29–44 and MFC.48 read in full. SHA256 `5E960B547592A83952E88FF65EC22577F182C652A7BE48C1DA1DCBDB91DF7ABF`.
- `../tensor_primary_boundary_control.tex`: TP.1–9, TP.23–25, TP.32–35 read. Snapshot SHA256 `913DFD191FF7EB1A826EECAF0F3C668B8C8A7FA7B0527B72CCD8585F873F00B9`; parent may continue editing it.
- `../single_primary_finite_field/single_primary_finite_field.tex`: SPF.1 coefficient datum and specialization read. SHA256 `538B2DA5ADF307B54396E46F0848A49C63F0D81072844D191768016255C4FD53`.
- `../tensor_primary_finite_field/tensor_primary_finite_field.tex`: TPF.1–6 read; this is the sibling's live file.

## Decisions

Use precisely the single-primary coefficient specialization already fixed in SPF, with localization at its actual kernel. Do not construct or presume any extension to a larger ring containing quartet CRT denominators. Preserve the given tensor unit and inverse. Distinguish the abstract reduced cyclic source (nilpotency K+1) from its ambient image (nilpotency min(p,K+1)). Prove the relation by its exact matrix and Tor sequence. The support comparison uses the actual MFC chain carrier and coefficient extension of Z/p^D into S/p^D. Only the principal p-power subchain of the latter is identified, never all its ideals.

Independent child cyclic_lattice_review reviewed algebra, base change, the support bridge and every formula TCL.1–37. The parent also read the entire main module. Both accepted all mathematics.

## Completed work

Additional source pin: purity_amplification_match.tex, PAM.1–5 read in full, SHA256 E8250C3F4F55517A2987A2D3C932CA83ABA035A3D8232B29B18E865CF32092C9.

The complete includable main proof is tensor_primary_cyclic_lattice.tex, TCL.1–37. It retains the original weighted map and both monomial translations; constructs a primitive containing lattice, its explicit projection, full-unit transport and saturation; computes the factorial inclusion, full quotient and exact Tor sequence; distinguishes the three reduced actions and all divided-power chains; proves the literal original chain-support and coefficient-ideal diagrams; computes the simultaneous character and p-depth labels; and proves the actual CRT-idempotent obstruction and the rational subring in the complete directed split-stage coefficient ring. It includes the surviving reduced character-zero direction and its precise nonzero characteristic-zero precursor.

The source-specific CRT proof was added only after reading PAM.1–5, including the actual quartet, grid, full coefficient injection and terminal idempotent. The complete original coordinate bounds 0<delta<1/2 and gamma>0 are retained. The directed coefficient union starts at tensor order 2, matching the actual displayed source range.

The independent five-page proof is review/cyclic_lattice_independent_review.tex, PCLR.1–29, with SHA256 80F48C8DD0897BF945189BE4BA2B8D60C3E27B1F1D899846AD9221BD540EDC90. Its full main-read receipt is review/MAIN_REVIEW.md. I read the complete independent proof and accepted it.

## Final validation

- Main SHA256: 7371F26AA05099D14D72D55999C9AF8605125A20DA017876B3E129775E2EFAAE.
- Complete main draft compilation: 10 pages, no overfull or underfull boxes, no LaTeX warning. Command: pdflatex -draftmode -interaction=nonstopmode -halt-on-error compile.tex. Draft mode intentionally produces no PDF; the parent owns the combined PDF and its visual review.
- check_cyclic_lattice.py passed 25 ordered packet cases and 164 prime-packet cases, using exact rational and finite-field arithmetic. It checks full-unit inversion, iterative powers against divided powers, unit-transported action, original source sum-coordinate columns, selected original-coordinate expansions, reduced map ranks and zero columns, exact integer factorial depths, ambient nilpotency and independent symbolic divided-difference identities of degrees 1–9.
- EXACT_CHECKS.json records all finite test cases and pins the exact final main hash. The finite checks supplement the general mathematical proofs; they are not presented as a proof by sampling.
- All 37 TCL equation tags are unique and sequential.
- No Lean, publication, global source edits, goal mutation or RH verdict occurred in this subtask.

No mathematical work remains within this bounded module. The parent may now embed the stable main proof and keep the independent review and exact-check receipts alongside the cumulative source.
