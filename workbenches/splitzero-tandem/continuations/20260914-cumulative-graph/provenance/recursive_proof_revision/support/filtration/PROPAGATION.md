# MW/MRE complete staged propagation — 2026-09-13

This directory contains byte-preserved original MW/MRE sources and complete revised TeX sources. The full proofs are in revised/MW.tex and revised/MRE.tex; this file is the provenance and integration receipt. No live source, sealed edition, or public object was modified by this worker.

## Source preservation and final pins

| Object | Bytes | Lines | SHA256 |
|---|---:|---:|---|
| originals/MW.tex | 13088 | 321 | 1834376a6eb1b338090cffa04d77361b25d4e63a5a909df6b24c5c9551688598 |
| revised/MW.tex | 27427 | 644 | fa8b2882d20340573c74044758edec727aeded02efd34b89338bf18b291b5b79 |
| originals/MRE.tex | 17424 | 447 | 35c080171f5bbc895d3e7f7f89776eabc7d71c5376dbc6be1a1bb0102c30fd73 |
| revised/MRE.tex | 33672 | 790 | c453731650ffb204391491115d6693481c08a6e6214e2a826097875716848c0f |

The originals remain byte-identical to the live sources work/tau_mixed_support_monodromy_filtration_20260913.tex and work/tau_mixed_relative_extension_control_20260913.tex. Their hashes also match the sealed-source pins recorded in the fully read work/tau_f1_transcript_audit_20260913/continuation_intake/FILTRATIONS_READ.md. The full MW and MRE bodies, including all original proofs, were read before editing. All revised differences were subsequently read; the parent independently read the revised bodies and checked the mathematics.

## Exact old → revised → downstream locators

Line numbers are the literal one-based lines of the named staged source. A tagged-equation line identifies the equation and surrounding complete proof. INVENTORY.json records every original and revised tag locator.

| Original dependency / ambiguity | Exact revised proof | Propagated downstream proof |
|---|---|---|
| Original MW.tex:132–146, MW9–MW10: unnamed combined action | Revised MW.tex:137–187, MW9a at 150 and MW10 at 172: T_(a,q)=A_a Psi_q with domain and codomain B_n, full basis formula, finite signed-permutation order, eigenspace projection, and separate graded eigenvalues | MW16a at 300 and MW16b at 312 retain tensor signs, factorials, nilpotent powers, and all three eigenvalues; MW21a at 395 reconstructs the combined tensor operator with both added factors; MW22a at 427 retains inverse coefficient eigenvalue in the dual; MRE42 at 751 transports it through the actual quotient |
| Original MW.tex:224, MW16: arithmetic tensor operator only | Revised MW16 at 264 remains verbatim; MW16a–MW16b at 300–312 give the separately typed arithmetic, coefficient, and combined tensor operators | MW27 at 613 and MRE42 at 751 prove the actual quotient tensor map, summed degree shift, multiplied added factors, and unchanged original eigenvalues |
| Original MW3 at 38, MW8 at 118, MW18 at 251; original MRE7 at 108 specifies length two for arbitrary parameter | MW23 at 453 defines the actual quotient C_rho=E_rho/(u_rho²) and inverse basis isomorphism; MW24 at 479 proves the full induced filtration and strict quotient sequence | MRE34 at 464 constructs actual K_rho/C_rho/Q_rho maps; MRE35 at 495 proves strict exactness at each step and both constituent shifts |
| Original centered length-two filtration MRE13–MRE16 at 161–186 | MW24–MW26 at 479–544 prove phi(Mbar_j)=M_(j−b)V2, with b=m−2, and the strict comparison with V2 tensor D_b | MRE35 at 495 and MRE37 at 576: full strict isomorphism of exact sequences, all inverse maps, and non-strictness of the unshifted comparison for m>2 |
| Original MW18–MW19 at 251–259; original MRE17–MRE22 at 211–265 | MW25 at 518 and MW26 at 544 retain induced exponents (m−1)/2−r, the coefficient a^rho log(a), both q^(b/2) factors, and ordered reconstruction | MRE36 at 537 proves induced/restricted/quotient eigenvalues and moduli; MRE37 at 576 gives exact intertwiners; MRE41 at 715 retains complete arithmetic and diagonal extension discrepancies |
| Original full-block MW3 and MW11; actual quotient kernel had no explicit shifted comparison | MW26a at 578 proves the kernel map u^r to v_(rho,r+2), kernel degree shift −2, both diagonal factors q^−1, and unchanged arithmetic action; preceding proof retains descended H2+bI and proves the original E does not descend by its actual coefficient 2(m−2) | MW27 at 613 proves the tensor quotient kernel and strictness directly on every original tensor basis vector |
| Original coefficient-one link MRE23–MRE27 at 280–328 | Existing MRE23–MRE27 retained verbatim at revised 286–334 | MRE38 at 609 proves actual-quotient factorization, strict Tate-typed isomorphism and inverse, every operator, and comparison with MRE26; MRE39 at 638 proves strictness of the entire quotient nilpotent map and commutation with the original packet quotient |
| Original relative extension filtration MRE28–MRE29 at 346–365 | Original proof retained verbatim at revised 352–386 | MRE40 at 668 translates both W and R, proves all relative graded maps and uniqueness, and explicitly identifies W^full_j E_rho=M_jE_rho as the specified filtration on the original coefficient packet |
| Original extension class MRE30–MRE33 at 391–430 | Every original formula body and prose retained | MRE41 at 715 calculates actual quotient section defects and full conjugation difference with every scalar and coefficient intact |

## Scope and integration facts

- Actual packet quotient constructions are indexed by the explicitly defined subset Z_(>=2)={rho in Z : m_rho>=2}. No claim is made that this subset is nonempty. The addition after MRE7 expressly retains its arbitrary-parameter scope.
- The actual quotient is not recentered. Its surviving powers retain degrees m−1 and m−3. The comparison is the proved isomorphism to a specified degree-shifted model, with both added operator factors.
- D_b is a fully specified complex filtered line. No odd shift is silently identified with an integer Tate twist, and no geometric realization is asserted.
- MRE40 names the coefficient packet filtration exactly. The parent separately owns the comparison from the original source complex to this coefficient quotient in MCF. This worker does not assert W^full is that source filtration.
- No original arithmetic scalar, logarithmic coefficient, coefficient-permutation sign, nilpotent coordinate, or active-mask zero was replaced.
- The integration unit is each complete revised file. Older editions remain preserved. The parent can include the full revised bodies in the next cumulative TeX and propagate its independent MCF source bridge.

## Validation completed

1. verify_stage.py verified both original SHA256 pins and byte equality between each preserved original and the unchanged live source.
2. Every original MRE line remains in original order in the complete revision. All 33 original MRE tagged equation bodies are exactly unchanged.
3. All original MW tagged equation bodies except explicitly clarified MW10 are exactly unchanged. Its original eigenvalue omega a^rho remains, now with the combined operator named and both individual values displayed.
4. All 75 revised tagged equations are unique: 33 MW and 42 MRE. INVENTORY.json records full locators and preservation lists.
5. The command pdflatex -interaction=nonstopmode -halt-on-error -file-line-error VERIFY.tex compiled the complete revised bodies together to a 15-page verification PDF. The final log has no LaTeX warnings, overfull boxes, underfull boxes, or errors. VERIFY.tex is a compile harness; the cumulative publication PDF belongs to parent integration.
6. The independent quotient checker verified quotient and kernel shifts, exact arithmetic and diagonal intertwiners, strict K/Q and Tate maps, relative transport, and the auxiliary H/E issue. The parent separately read all revised MW/MRE bodies and confirmed these calculations.

A transient ancestor-path error in the validation script was repaired. No mathematical source was affected; the subsequent full validation passed.
