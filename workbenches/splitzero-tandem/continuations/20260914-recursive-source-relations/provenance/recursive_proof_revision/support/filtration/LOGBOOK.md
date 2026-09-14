# Filtration propagation logbook — 2026-09-13

## Delegated instruction (verbatim)

Bounded actual TeX propagation under parent support lane. User requests preserve old editions, update older proofs with new precise results, propagate downstream. Own MW/MRE only. Read full workspace:/work/tau_mixed_support_monodromy_filtration_20260913.tex and tau_mixed_relative_extension_control_20260913.tex and full work/tau_f1_transcript_audit_20260913/continuation_intake/FILTRATIONS_READ.md. Stage preserved originals + revised complete MW/MRE in work/backpropagation_20260913/support/filtration (do not edit live sources). Explicitly type T_(a,q)=A_a Psi_q before MW10 and propagate exact combined vs individual operators through downstream tensor formulas; inspect whether additional clarification/proof needed for length-two quotient of actual m>=2 packet, using induced filtration (do NOT silently recenter actual quotient). Write complete exact proof comparing actual m-block length2 quotient to MRE with degree translation or show exact filtered shifted coordinates; retain all arithmetic coefficients and added F/Gamma factors; MRE at arbitrary rho must not assert actual repeated zeta zero. Existing MRE exact strict K/Q extension stays. Return full proof edits with actual old->new->downstream locators and hashes in PROPAGATION.md. Can prove new quotient shift: quotient V_m/(u²) has induced degrees m-1,m-3 vs MRE degrees1,-1, shift m-2, F induced q^(rho+(m-1)/2),q^(rho+(m-3)/2) vs MRE q^(rho+1/2),q^(rho-1/2); scalar q^((m-2)/2) bridges. Exact proof and maps required. Parent independently handles MCF source-support propagation.

## Coverage and preservation

- Read all 321 lines of MW, all 447 lines of MRE, and the complete intake FILTRATIONS_READ.md.
- Copied original bytes to originals/MW.tex and originals/MRE.tex; complete revised files live only under revised/.
- MW original SHA256: 1834376A6EB1B338090CFFA04D77361B25D4E63A5A909DF6B24C5C9551688598.
- MRE original SHA256: 35C080171F5BBC895D3E7F7F89776EABC7D71C5376DBC6BE1A1BB0102C30FD73.
- Parent owns the full session user-transcript provenance and cumulative global publication artifacts; this bounded worker records its received instruction verbatim above.

## Decisions and work remaining

- Name and type the combined operator on the full linear coefficient space, where signed-permutation eigenspaces exist. A moving individual mask is not itself claimed to be an invariant eigenspace.
- Propagate all three separate operators through tensor products, added diagonal reconstruction, and contragredient duality.
- Prove the actual packet quotient with its induced filtration, retaining its shift b=m-2. Use a specified degree-b line with added scalar q^(b/2) and arithmetic scalar 1 for the exact comparison.
- Retain existing MRE1–MRE33 and append the actual shifted K/Q comparison, Tate map, relative filtration, and full extension discrepancies.
- Independent read-only checker: quotient_proof_check, assigned exact quotient and shift verification while staged edits proceed.
- Finish with full-source preservation verification, equation-tag/TeX compilation checks when available, and exact locator/hash report in PROPAGATION.md.

## Completed work and verification

- Completed full revised MW1–MW27 plus all lettered formulas and MRE1–MRE42. All MRE original lines remain in order; its original 33 equation bodies are unchanged. Only original MW10's tagged equation body changes, retaining the original combined value and adding explicit individual operator values.
- Independent quotient checker confirmed the degree-b actual quotient, degree-minus-two kernel, added factors, strict maps, and auxiliary H/E issue. Parent independently read the complete revised bodies and checked their proofs.
- Applied parent precision correction: MRE40 explicitly names the filtration on the original coefficient packet. Parent owns the separate source-complex comparison in MCF.
- Full 15-page TeX compilation passes without errors, warnings, overfull boxes, or underfull boxes after displayed-formula line wrapping. The compile harness is not presented as the cumulative publication PDF.
- verify_stage.py verifies byte-preserved originals and unchanged live sources, original equation bodies, complete MRE line preservation, unique tags, and clean compile log. Initial ancestor-path mistake was repaired; final validation passes.
- Final MW SHA256: fa8b2882d20340573c74044758edec727aeded02efd34b89338bf18b291b5b79; 27427 bytes, 644 lines.
- Final MRE SHA256: c453731650ffb204391491115d6693481c08a6e6214e2a826097875716848c0f; 33672 bytes, 790 lines.
- PROPAGATION.md contains old-to-new-to-downstream proof locators and integration scope. INVENTORY.json contains all source pins and equation-tag locators.
