# Recursive mathematical propagation audit

This audit belongs to the user's instruction to retain earlier editions for provenance, replace affected current calculations by their more precise versions, and carry those refinements through later uses. It reviews a bounded dependency closure; it does not claim a fresh line-by-line reading of every proof in the 821-page edition.

## Historical source and executable inclusion

The authoritative historical source is the complete current_source_20260913_periodized_residue directory. All **4,923 existing files** were pinned independently in HISTORICAL_821_BASELINE_PINS.json. The initial preservation check found no changed or missing file. The actual baseline main recursively includes 129 TeX files through 128 input edges, with no unresolved input. The v19 staging main initially had that same 129-file graph: placing later source files beside it had not itself made those files part of the compiled mathematical argument.

The final assembly must preserve the historical source and bind each accepted replacement to the path actually read from its main file. In particular, v20's draft master names tex/AT_complete.tex and tex/AW_complete.tex, while the metric lane's supplied source paths contain an additional next_edition directory. The cumulative builder was informed of this mismatch and confirmed explicit route mapping. The builder was also warned that the existing preparer maps earlier chapters to inherited prepared bodies; applying a patch before that preparation could silently overwrite the revised proof. Preparation is therefore performed first, followed by recorded regeneration overlays.

The executable audit_inclusion.py verifies both exact revised bytes and recursive inclusion. A correct archived source whose active chapter is stale does not pass this check. collect_patch_expectations.py gathers the owners' current source pins, checking each pin against actual bytes before constructing EXPECTED_ACTIVE_PATCHES.json.

## Actual proof contexts read here

- Original support_diagrams D1–D8, original TC29 and its preceding arithmetic bound, and TB.24–26 plus TB.35–36 and their complete relevant proofs.
- Complete new D9–D14, TC29a–d, TB.37–39, MCF42–46 source compatibility, and MCF47–51 filtered source quotient. Later notation changes and the explicit D−rho source codomain were reported by the owner and retain those proofs.
- Original research conclusion opening through R6, complete R47, and all R50–R62. Original circle diamond DC27–30 and the full weighted extra-circle decomposition/proof were read.
- Complete revised SP1–SP13, the entire revised AT18–22 proof, and the entire FV.M1–FV.M12 insertion with its source primitive. The broad line-ending-heavy diff output was truncated; this receipt relies on the separately read actual source blocks, not that diff output.
- Existing AP analytic pole source AP1–AP13 and AP19–AP26 were read in their original proof context. The exact new u-connection on the pole extension was then calculated and sent to the boundary owner for its full source insertion.
- A separate independent child reads the complete newly inserted boundary proof blocks in their actual revised source. Its source-hashed receipt is BOUNDARY_NEW_PROOFS_REVIEW.md.

## Concrete closure findings and repairs dispatched

1. **Four circle observations were an omitted descendant of the new u connection.** Existing DC30 retained only the t equation. For Omega=-C/u^2+B/u and Pi_u=Pi Omega, the exact derivative is d_u(T_s Pi^-1)=-T_s Omega Pi^-1 for each of s=a,b,d,l. The fixed comparison maps carry these derivatives to the common quotient, and the original circle weights stay unchanged. The boundary owner accepted this finding and produced DC31–32.

2. **The existing analytic Taylor-unit pole extension also needs the new u connection.** For f=Phi-ts and the original pole vector r_p=(s-p)^-1, divide q_p=(f-f(p))/(s-p) by h-t. Its ordinary quotient is the constant 1/(d+1), whose derivative is zero. Thus Q_p=rem_(h-t)q_p is the exact twisted remainder and nabla_u r_p=-Q_p/u^2-f(p)r_p/u^2. The full matrix has polynomial block Omega, pole-coupling block -Q/u^2, and pole diagonal -diag(f(p))/u^2. This preserves the original weighted-residue map [0,W], since W_u=-diag(f(p))W/u^2, as well as its distinct small-loop map 2 pi i [0,W]. It does not evaluate the formal contraction at nonzero u. This calculation was sent to the boundary owner and assigned a full current-source proof.

3. **The new metric proof initially killed a relation at every arbitrary proper source W.** FV.M12 correctly constructed its full tensor primitive, then stated that its class vanished at every outer label (W,S). The support refinement shows the precise correction: at one source leg its class is eta_W of the primitive's class in V/W. At tensor degree k the typed residual lies in d(C_full^(k−1))/d(C_lambda^(k−1)), mapped into the degree-k declared-source quotient. That entire tensor module must not be silently identified with V/W. The metric owner received this exact correction; global-source vanishing remains true and the original polynomial remainder remains zero. This is a real compatibility issue across lanes, not a missing citation.

4. **A literal Gamma exponent typo was found during full source reading.** FV.M1 had c_(1/4)^{,k}; the owner was asked to correct it to c_(1/4)^k in both current TeX and paired Markdown and refresh pins. Compilation alone would not have found this mathematical transcription error.

5. **The actual quotient of a length-m packet carries its induced shift.** MCF47–51 retains the quotient degrees m−1 and m−3, with shift m−2 relative to the earlier centered length-two presentation. Its q-preimage source complexes retain the common low-step complex [V→Theta V]. For proper W, the low-step H1 is V/W and the joint H0 is W. These exact maps were checked and accepted; no recentering or erasure of the residual is permitted in later uses.

6. **Current result paragraphs must change at their old sites.** R1 receives the precise source-level quotient map. R44/R45/R47 receive signed metric budgets. R52/R56/R57/R59/R62 receive the singular connection and its actual descendants. R58 receives the strengthened sampled/original bound. The root owns the single merged conclusion to avoid conflicting edits. R51's title must describe the compact-support comparison actually built, rather than imply that the entire Deligne programme was completed.

7. **Existing estimates keep their exact operator domains.** R50's positive cost Z=(K_j−K_i)G_i acts on E and has its original Hermite two-trace majorant. The signed source difference U−W acts on P_(2q), has trace zero, and is paired with M_x^−1 dot M. The original minimum section, its range projection, and determinant derivative give the exact bridge; the signed operator cannot be substituted into a positive-cost theorem. Likewise the finite-circle metric remains the actual sampled form, not the Gamma form. AW7/AW14 remain credited as the earlier spectral and condition-number calculations, while SP supplies the actual overlap refinement.

The machine-readable DEPENDENCY_CHANGE_USE_LEDGER.json records exact source pins and line locators for these changes and uses. LEXICAL_CHANGE_USE_CANDIDATES.json is explicitly a discovery index, not a mathematical acceptance record. Final active inclusion and historical preservation are recorded separately after assembly.

## Resolved repairs and the final current-source closure

The FV source issue above was repaired in the actual earlier proof. The exact top-degree kernel is

\[
\bigl(d\mathsf C_{\rm full}^{k-1}\cap\mathsf C_\lambda^k\bigr)
/d\mathsf C_\lambda^{k-1}.
\]

The earlier shorthand without the intersection is superseded by this displayed domain: the represented full boundary must also belong to the declared degree-k source. FV.M13 gives the primitive preimage and its kernel, and FV.M14 gives the exact one-factor map. Both complete repairs were reread and accepted. The Gamma exponent typo was also repaired in both TeX and the paired Markdown source.

The final root R67/R72–74 source was independently read with the complete ISM and RMT continuation. Three scope issues were found and repaired at the actual result sites: the proper-support tensor residual now specifies the admitted top representatives and the differential of its displayed primitive; the acyclic low tail is explicitly full-source, while proper-source V/W and the two-leg diagonal remain; the reverse-restriction cross trace explicitly requires i≤j. The corrected root source was accepted at SHA256 `13288392b5cc9a19b7099e347a6d55b5b4790da58476e1b0385ea41bb648c921`. ROOT_AND_SIGNED_PROOF_REVIEW.json records the exact source pins and checks, including the finite signed residual, original weighted self-adjoint operators, nonlinear derivative/inverse, and full endpoint intersection.

The final ISM43 was reread in full after its carrier repair. It first defines the singleton coefficient carrier and proves inverse projection/insertion maps, then proves the componentwise `(V/W)^A` kernel on the full fixed carrier, with both inverse composites, zero insertion, signed permutations, and empty-mask outer label. This prevents a one-factor vector space from being silently used for an arbitrary direct-sum coefficient carrier.

Further actual downstream sites were found in the current CF cohort: ACM11/ACM13 still used a two-control minimum, and HC14 still used the earlier `2q` phasewise source error. The metric owner accepted their propagation. The neighboring averaged quotient form remains separately typed: averaging already minimized quotient Grams has not been identified with the minimum quotient of one averaged source Gram. The existing averaged-quotient bound therefore keeps its own proved scope.

Active source transfer is now checked independently of source-copy presence. The entire revised AP body occurs exactly once in its active compiled wrapper after the two inherited presentation transformations; its raw source and wrapper both retain exact pins. The complete BC abstract and mathematical body occur unchanged exactly once in its extracted active fragment; the standalone document is separately preserved as a source asset. The first active boundary check found one correctly copied but unincluded tensor companion and dispatched that omission to the builder, which added its full input route. These checks preserve all 4,923 pinned historical files.

The five current cohort typography edits and the HCD inherited layout edits were independently replayed and inverted on complete bytes. TYPOGRAPHY_INDEPENDENT_CHECK.json records every old/new edit, both source hashes, and exact forward/inverse equality. They do not alter mathematical source identities or conclusions. Later active typography overlays require the same explicit mapping before final validation.

## Final accepted closure

The first frozen whole conclusion passed source-hash checks but failed the independent complete-block check: its old-ending truncation discarded the entire new R62 Hessian and derivative continuation. The rejected source `4e4eb1bd...` and exact diff are retained here. The assembler was repaired to remove only the literal six-line historical closing paragraph. All new R62 proof paragraphs now survive. The corrected whole conclusion `a310d094...`, followed by its explicitly inverted three-display typesetting transform to active `dc9852c...`, passes all **22 complete-block checks**.

The final ACM and HC revised proof bodies were independently read and accepted, including the finite signed construction, original Gamma-to-arithmetic dictionary, exact phase-source restriction, and subsequent derivative-source energy budget. Their earlier affected formulas are replaced at ACM11/13 and HC9/10/13/14. The averaged-quotient estimate retains the exact positive relation correction and its separate proved scope.

Final active verification passes **41 explicit source/asset paths**, with **14 complete-file reversible presentation maps**. Those maps include the root and boundary display changes; LF-to-CRLF transport is explicitly recorded where the builder changed file encoding. No mathematical term, matrix entry, coordinate, source mass, or proof paragraph is removed by these maps. The actual main recursively includes **239 TeX files through 238 edges**, with zero missing inputs. Every one of those 239 files is present with the same byte hash in the compiler recorder. Its one additional input is the verbatim displayed `at_hash_clarification_v1/verify_reconstruction.py` source, giving 240 recorder-bound source files in total. All **4,923 historical baseline files** remain unchanged. The compiler receipt reports a 1,625-page PDF with zero undefined controls, missing characters, LaTeX warnings, font warnings, or overfull boxes. PDF layout review and portable rebuilding remain the builder's separately recorded work.

FINAL_AUDIT_RECEIPT.json binds this source/dependency acceptance to the actual compiler source manifest and PDF hash. It records no unresolved finding within this audit's stated bounded scope. The mathematical programme continues beyond these finite calculations; this receipt accepts the completed recursive update and proof transfer rather than declaring that programme closed.
