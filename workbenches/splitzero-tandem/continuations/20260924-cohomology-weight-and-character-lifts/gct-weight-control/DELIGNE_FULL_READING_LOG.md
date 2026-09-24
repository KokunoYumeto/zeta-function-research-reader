# Deligne weight-control reading and reconstruction

The current request is WU055: read and reconstruct the full weight-control mechanism, then calculate its relation to the user's construction. This is a reading log, not a claim that a transferred RH proof exists.

## Source edition

Pierre Deligne, *La conjecture de Weil. II*, IHES 52 (1980), 137–252. Canonical routing IDs PUBUNIT-3D90B487DBD1CC3A259C6455 and PUBUNIT-574B0214207BBB2BDABCFFF9. The workspace's RESEARCH_SOURCE_INDEX.md supplies the more recent editable witness absent from those index routes: output/Deligne_Weil_II_S20_LaTeX/typed_latex/S20_FR_record_export.tex, SHA256 d6836ae15d98f2b27eb98c9bd039a7d921679becd9fa47ff4717410289dbd351. This is a complete French transcription export, not Deligne-authored TeX. Its export verification proves page-record preservation, not correctness of every formula. Historical English math-mode text is a secondary reading witness only. Original scans and the intact source archive remain unchanged and have not been read in this continuation. The earlier PDF-format question is superseded by the available current TeX route; no PDF exception has been assumed.

The display script read_deligne_source.py reads the unchanged French TeX, reports printed-page and TeX-line locators, and reverses display escapes. It does not correct the source.

## Root's actual reading coverage

- Printed page137 contents; pp138–145 introduction and conventions, complete.
- pp146–156: complete §§1.1–1.2, beginning1.3.1.
- pp157–165: complete §§1.3–1.5; beginning1.6.
- pp166–175: complete §§1.6–1.7 and1.8.1–1.8.4 statement.
- pp176–186: rest1.8, complete1.9–1.11.
- pp187–196: complete §§2.1–2.2.
- pp197–206: §§3.1–3.2 and beginning3.3; printed p203 was separately refetched in full after output truncation.
- pp207–216: remainder3.3 and complete3.4–3.7.
- pp217–228: §§4.1–4.3 and beginning4.4.
- pp229–242: remainder4.4–4.5 and all5.1–5.3.
- pp243–252: all6.1–6.2, notes and bibliography.

This completes root reading of the entire 116-page article in the current French transcription. It does not upgrade that transcription to original author TeX, and does not claim that every cited upstream SGA proof or Weil I has been independently read and reconstructed. Root's reading remains transcription-based; the separately attributed peer original reading is recorded below.

Reading is distinct from independently reconstructing each cited upstream theorem. The reconstruction names external SGA, class-field, and representation-theoretic inputs where Deligne invokes them. Independent agents reconstruct1.6–1.9 and3.1–3.3; root reconstructs determinant weights, real-sheaf purity, the boundary nonvanishing mechanism, and the exact receiving maps. Agent reading does not replace root coverage.

## Mathematical dependencies already located

1. The base is Spec(F_q), and a geometric point is a map Spec(kbar) to the scheme. Neither is an arithmetical zero. The zero sheaf in1.2.2 has empty weight set. The parameter t=0 in a generating function has another role. These roles must receive individually typed comparisons with tau〈Z1; no Z2〉.
2. A local geometric Frobenius F_x has degree [k(x):F_q]. The fibre representation, its determinant, and its trace are separate data. A fixed support does not remove its fibre action:1.1.7,1.1.10–14.
3. The geometric rank-one monodromy is finite (1.3.1–4); the remaining character is c^degree. This gives determinant weights, not yet pointwise eigenvalue purity.
4. The trace identity retains H_c^0, H_c^1, H_c^2. Even tensor powers give nonnegative local power-series coefficients; determinant weights control possible poles; exterior powers and determinant sums force equality for individual eigenvalue weights (1.5.1–3).
5. The nilpotent logarithm is a map V(1)→V. Its monodromy filtration and Tate twists must be retained; tensor powers and the dual give exact primitive weights (1.6–1.8).
6. The strict starting inequality for H_c^1 uses2.1–2.2: positive logarithmic-derivative measures, compact-group representations, a boundary-zero classification, and an actual double cover to exclude the exceptional quadratic character. The existence of a double cover alone does not supply those analytic and cohomological identities.

## Witness discrepancies and displayed-formula checks

These were initially checks of the available local witnesses; root has not independently compared the original scans. A later peer original-scan comparison is recorded immediately below. Keep displayed source formulas and separately derived corrections distinct.

Update, 24 September 2026, receipt10:26UTC: task01a0baa4 completed original published-page reading137–252, using direct PDF extraction and separately listed visual formula checks. Root read its READING_LEDGER.json and complete-reading notes in work/quantum_tau_programme_bridge_20260924/argument_reconstruction/original_deligne_reading/. This is peer reading, not root scan coverage or certification of external references. The original PDF SHA256 is b06eea61bf9cb2b596c162f5befc85d1be69828910a6107c8aa3a99c4afcc71.

The peer directly confirms the source itself prints the §3.5.6 density and elliptic trace display on212, the finite-subgroup wording in1.3.10(iv) on160, the terminal Jordan-chain index in1.6.7 on166, and the intermediary inequality in1.6.13 on169. Its visual checks also place the1.6.14.3 twist sign and1.7.5 filtration/conjugation displays on original170–171. These must not be attributed solely to transcription. Its original158 check confirms the full multiplied degree factor in1.3.6. The ledger retains unresolved original-formula checks at2.1.1,2.2.8,3.2.7.1 and6.2.11; do not declare those individually certified. Original217 and221 explicitly suppress Tate twists after a chosen coefficient isomorphism over an algebraically closed base; the arithmetic comparisons here retain the equivariant twists. Source displays and independently derived corrections remain separate.

-1.8.1 denominator: current French H_c^2, historical English H^0. Use H_c^2 from the full trace identity.
-1.3.10(iv): current French says image is a finite subgroup of Z, but the proof constructs a central element of nonzero degree and1.3.11 states finite cokernel. The mathematical condition is finite index.
-1.3.6: a twist defined over F_p acts at a closed point by b^{[k(x):F_p]}=b^{[F_q:F_p] deg(x)}. Any division by [F_q:F_p] in that exponent conflicts with1.2.7; retain and derive the full factor.
-1.6.7: the displayed Jordan-chain exception must be i≠−d, with Ne_{−d}=0.
-1.6.13: the needed inequality is k−2i−2≥2j−k for k>i and j≤0; the printed intermediary k−2i−2≥k cannot hold.
-1.6.14.3: from N^r:Gr_i(V)(r)→P_{−j}, r=(i+j)/2, the inverse description is P_{−j}(−r). The available witness misses that minus; the other Tate tensor/dual formulas and the claimed isobarity confirm it.
-1.7.5: weight filtration M_i is the sum of generalized eigenspaces of weights ≤i. A product over j<i would give the wrong graded index. Geometric Frobenius gives FNF^{-1}=q^{-1}N, hence the conjugation coefficient for F^n is 1−q^{-n}; all factors are rederived.
-2.1.1: omega_s=q^{−s degree} has period 2pi i/log(q), not 2pi i log(q).
-2.2.8(i): omega_s has weight −2 Re(s). Under2.1.1's definition of Re(tau), the pointwise weight is −2 Re(tau), not the opposite sign in the witness.

Every independent correction will be proved in the reconstruction; source files remain unchanged.

Further issues found in full reading and independent reconstructions:

-2.1.7: the lower bound for a character integral includes a possibly negative contribution outside the concentration neighbourhood. The exact factor is (1−e1)(1−e2)−e2, not simply 1−e1−e2. Taking e1=e2=e/4 proves the required result with that term retained.
-3.2.1: the Poincaré-dual coefficient sheaf is F∨(1); a displayed F∨(−1) gives the opposite Tate factor.
-3.2.7.1: the Rf! fibre is compactly supported Hc1. The real companion used in applying1.5 cannot be omitted when the original tensor-product sheaf is not itself real.
-3.2.12: a surviving β in the transcription's weight-zero specialization is tracked by deriving the entire proof at original weight β.
-Historical English3.2 changes several non-strict inequalities into strict ones and drops a term from the five-term sequence. Historical3.3.9 also changes det(tI−F) to det(I−Ft), reversing the moduli of its roots. The current French and the exact derivations govern.
-3.5.6 in the current French displays (1/(2π))sin²θ dθ on [0,π], whose total mass is1/4; the probability density is (2/π)sin²θ dθ. With eigenvalues q^(n/2)e^(±iθ), the trace formula gives 1−2cosθ q^(n/2)+q^n. These application-level discrepancies are retained separately from the purity proof.

DP0–DP9 now supplies the full determinant/tensor/exterior-power proof, including the rank-one argument, the degree factor [Fq:Fp], the complete trace denominator, and the coefficient-domination argument. DLM, DW and DB supply the other reconstruction sections; their independent checks and root reading are recorded separately as they occur.

## Final invariant-cycle reconstruction and exact scope

Root reread the complete source §3.6, printed pp212–215, and read the full independent derivation DC0–DC12 in DELIGNE_INVARIANT_CYCLE_QUOTIENT.md. Independent mathematical review checked the inertia Frobenius sign, support-duality shift, both exact sequences, the complete specialization kernel, and the actual recovered-base maps. The degree-zero sentence was corrected: only negative cohomological degrees automatically vanish.

DC proves the rational ℓ-adic local invariant-cycle theorem in the source's henselian curve setting. After its stated arithmetic reduction, K=H^(i−1)(X_bar_eta)_I(−1) and the support term O have weights at least i+1, while C=H^i(X_bar_eta)^I has weights at most i. Hence W_iB maps isomorphically to C. The obstruction image im(∂)/∂K vanishes, while the whole quotient O/∂K can remain and equals the next specialization kernel. The unique Frobenius-equivariant lift is into B, not a unique representative in special-fibre cohomology. This splitting is asserted for the fixed arithmetic model. The complex analytic mixed-Hodge analogue in §3.6.4 was read as a cited remark, not independently reconstructed.
