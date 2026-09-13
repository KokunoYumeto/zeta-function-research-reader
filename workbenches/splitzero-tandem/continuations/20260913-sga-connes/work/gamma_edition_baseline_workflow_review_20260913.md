# Gamma edition workflow: independent frozen-H baseline review

Read-only review dated 2026-09-13. Sources read: the complete `work/toda_edition_workflow_20260913.py`, the complete JSON specification `work/toda_edition_spec_20260913.json`, the path and source-package contract `work/cyclic_publication_contract_20260912.py`, the called metadata-alias function and import guard in `work/publish_split_zero_continuation_20260912.py`, the frozen H manifest/build inventory, and the H release handoff. I also inspected the actual Gamma checker entry points and their companion-file requirements. No collection, staging, build, replay, publication, freezing, or Lean command was executed by this review.

The new Gamma workflow and specification were not yet present when this baseline review was written. Their separate independent review follows after their concrete files are supplied. This document describes the exact inherited contract and the specific adaptations supported by the inspected files; it does not approve an unseen implementation or an unbuilt final PDF.

## 1. The exact H baseline

The independent script `work/gamma_edition_baseline_readonly_audit_20260913.py` read every file under `release_20260913h`. All 943 ordinary manifest rows match their recorded bytes and SHA-256 values. Together with the three special files, the directory has exactly 946 members. Its complete path set matches the manifest, with no duplicate/case-colliding names, symlinks, or junctions. Every one of its 39 TeX input hashes and 18 original source-witness hashes also matches the build receipt.

The baseline's own published commit is `16fc4dbb817b82023c6126e636f1c6df28d4cecd`. The `base_commit` inside H's current manifest is `161089942cce70a09fbe441d08ba4d36c1fd810c`, its G ancestor. The Gamma specification must name H's own commit as its immediate baseline; copying the ancestor field would misstate provenance.

| Frozen H special file | SHA-256 |
|:--|:--|
| `PUBLIC_SOURCE_MANIFEST.json` | `affffb542a9e6ab11c7b665e38da2220802300b45599ce7e5464e3da82ae13f6` |
| `README.md` | `260e24b160a3e8d49e6bc2df5ac4885904c0706c78d918837ed8902adbd448ff` |
| `scripts/build_reader.py` | `1715e0fb749291d5453c580820cf1f41e4ee85f09615d0ccfa444c850c216904` |

H has 38 full proof chapters, 18 full source appendices, and a 424-page PDF with SHA-256 `f70b1c4e34cd2339080b8b9071ff3dd9d5b8dda80433b6eb191b84c9a9085cf4`. The read-only audit is recorded in `work/gamma_edition_baseline_readonly_audit_20260913.json`, including the complete original TeX and source-witness inventories.

The five-proof cut is explicit in `work/record_gamma_five_proof_cut_20260913.py`: the exact coefficient join, seed moments, seed source costs, finite metric transfer, and phase/fibre transport. Over H this is exactly 43 proof chapters and 44 TeX inputs including `tex/main.tex`; one added whole Gamma source appendix gives 19 appendices. The arithmetic cut must be derived from those exact path sets, with these counts as consequences. The coexisting `gamma_endpoint_window_bridge*` files belong to the explicitly separate next mathematical lane; a broad `gamma*` directory glob would accidentally mix that evolving lane into this cut.

## 2. What the inherited functions enforce

In the Toda workflow, `snapshot` at line 73 validates a whole tree, rejects links/junctions and case collisions, and records both size and hash. `baseline` at line 88 verifies the three independently pinned special files and every manifest row, and requires equality of the actual and expected file sets. These checks are materially stronger than checking the PDF or manifest hash alone and should be preserved against frozen H.

`edition` at line 103 requires a specification under the local work directory, canonical direct-child baseline/stage/frozen directory names, unique valid proof basenames, and an exact inherited-TeX update scope containing only `tex/main.tex` and `tex/research_conclusion.tex`. The Gamma names must replace the Toda names in its declarations and messages. No prior proof chapter can be silently replaced by reusing its basename.

`inspect` at line 118 builds an explicit allowlist from work files, exact archive/Git members, whole source witnesses, declared public files, and check receipts. Source packages are checked against the original archive or commit provenance; ZIP member reads check the actual member bytes and CRCs, and every member is required by the archive inventory. The archive's instructions remain source material. They do not become workflow actions merely because they are inside the package.

The TeX checks retain every inherited input except the two declared cumulative-edit files. The current main must include each inherited and newly declared chapter exactly once; its source-appendix assembly must also occur exactly once. Every inherited source-witness/hash/converted-path triple must survive, and every inherited converted appendix must remain byte-identical. The new appendix set must be exactly the inherited set plus the explicit new whole source witnesses. The Gamma cut therefore retains all 18 H original/converted pairs and adds the entire delivered Gamma NOTE as the nineteenth witness.

The production checks tie the current PDF hash to the build receipt, exact TeX input hashes, complete source receipt, rendered-page count, geometry checks, all-page visual approval, and all component review hashes. The source audit must cover every proof input and every original/converted source pair at the final PDF hash. The workflow can remain pending while the root task supplies these final artifacts; it must not fabricate final hash, page count, approval, or source-audit fields to satisfy the expected schema.

The workflow permits editing the entire cumulative conclusion file as a path-level operation. The separate source/integration audit must additionally establish preservation of the complete earlier conclusion and propagation of affected mathematics. A path allowlist alone does not prove that an old conclusion body was retained. Likewise, transitive TeX inputs or Python companion files must be included by their explicit dependency closure; checking only main's top-level `input` list is not a substitute for that closure.

## 3. Source closure and metadata history

The Gamma allowlist should come from the five final proof-component manifests plus their explicitly named supporting files, reviewed images, source-transformation records, root integration/audit files, and the complete source archive. A manifest's recorded dependencies are to be resolved relative to that manifest's declared location, not relative to an arbitrary current working directory. All listed SHA-256/size pairs must resolve to the actual collected bytes or to an explicitly documented original/public metadata pair.

Specific current dependencies include the finite-error review manifest and its ten members, the pinned inherited TI normal JSON consumed by the seed coefficient transfer, the Gamma seed normal JSON consumed by source-cost calculations, proof `.tex` companions consumed by checkers, and the actual QA PNG/contact images referenced by component receipts. Including only QA JSON receipts while omitting the images they attest to would leave that support package incomplete. Original full mathematical `.tex`, `.py`, raw ZIP members, binary figures, and the source ZIP retain their exact bytes; the scope of any machine-path transformation is explicitly recorded metadata.

The inherited `stage` function starts with a full copy of the verified baseline and requires a fresh sibling destination. It does not delete or reuse a previous stage. Before replacing current metadata, it preserves historical bytes and the three special files under a dated history prefix, with a locator receipt tying them to the old edition. For Gamma that prefix must be `history/20260913-toda/`, leaving the earlier nested history untouched. The historical receipt's internal paths and validation scopes refer to historical H; they are not rewritten to pretend that its old checks validated Gamma.

The original workflow chooses historical metadata copies by comparing incoming original hashes against old public hashes. If an unchanged public metadata file had already received aliases, this can create an extra exact historical copy even when the eventual new public bytes match the old public bytes. That is safe but affects file counts. Final member counts must therefore be derived after staging and sealing, not guessed from the number of new files.

The old `publication_note` copied into H's manifest still describes an earlier F baseline and a prior witness. Gamma should give its current manifest a public-facing description of the actual H-to-Gamma collection while retaining old metadata under history. This is an accuracy correction to the current description, not a change to historical mathematics.

After staging, the saved integration inventory must still equal a fresh inspection of the declared final local inputs. Every input size/hash is rechecked during copy. The new public manifest must cover exactly the resulting ordinary members; the three special files receive their separate sealing pins. The old H directory is snapshotted again and must remain byte-identical. Those checks should also run after the fresh-copy replay. No Gamma workflow path may point its stage or future frozen directory at H itself.

## 4. Exact aliasing boundary

The inherited `metadata_aliases` at line 262 calls the existing corpus/runtime alias function, adds the OS corpus alias, and removes user-profile roots in ordinary, forward-slash, JSON-escaped, and repeated-separator spellings. Its legacy module has an `if __name__ == '__main__'` guard, so importing its helper does not execute a publisher. A standalone replacement can preserve those mappings explicitly without making the collection workflow depend on publication code.

The `put` operation aliases only designated non-exact `.json`, `.md`, `.txt`, or `.log` files. It records both the original `source_sha256` and public `sha256`, plus whether the bytes changed. Mathematical source designated exact is never rewritten. A remaining private-account string in a public text member causes staging to stop; the correct response is to repair the metadata source/mapping within scope, not erase mathematical content or relax the check.

The public alias glossary should include every alias actually used, including `local:user-profile`, which the current helper can emit but H's inherited glossary does not list. The package, workspace, corpus, and runtime alias meanings remain explicit. A hash inside an aliased historical receipt can legitimately refer to its original metadata bytes; current-public verification must use its own manifest row, keeping the original/public distinction explicit.

The replay currently requires the staged specification's parsed JSON to equal the live specification. Therefore the new spec itself should contain canonical package/work-relative paths and public-facing scope text, so metadata aliasing does not change its semantics. Absolute source-workspace paths should not be placed in executable spec arguments merely to make a local replay pass.

## 5. Replay contracts that differ between Gamma checkers

The baseline's `replay` at line 364 copies the entire verified stage into a fresh temporary package and builds there. It compares every page's extracted text and the exact page count with the contributed PDF, checks the TeX log for missing characters, overfull boxes, undefined references/control sequences, and fatal errors, and verifies that the stage and frozen baseline are unchanged. A rebuilt PDF may have a different byte hash because of metadata, but its final contributed PDF hash and the replayed PDF hash are separately recorded. This is a text/build replay; the root's all-page visual receipt remains independently required for the contributed PDF.

Each checker then runs in its own new directory with the declared script and companion inputs copied from the verified package. This avoids accidental success through undeclared work-directory imports. All support-file basenames, script basenames, and chosen output names must be checked for exact and case-folded collisions; the Toda loop checks only a support filename against the script, and could otherwise overwrite one companion with another having the same basename. No companion should be overwritten by the output path. The copied script and input hashes can be checked before and after execution to retain their exact roles.

The actual inspected entry points have these differing semantics:

| Checker | Positive output/input contract | Negative semantics |
|:--|:--|:--|
| Archived `check_gamma_descent.py` | `--json result.json`; 17 unittest methods | `--fail-control` raises `deliberately false exact equality` before any suite or JSON write; expect exit one, absent output, and that stderr text. |
| `gamma_exact_coefficient_join_check_20260913.py` | required `--json`; recorded exact rows, with no optimization field | Six `--mutant` choices write failure JSON and exit one; verify the exact failed identity list, not a generic exception. |
| `gamma_seed_intervals_20260913_check.py` | required `--output`; recorded `optimization_flag`; fresh Arb values and proved tails | Four declared fault choices write failure JSON and exit one; preserve each precise failure and numeric scope. |
| `gamma_seed_intervals_20260913_source_costs_check.py` | required `--output`; `--input` defaults to the companion `gamma_seed_intervals_20260913_normal.json`, whose SHA is checked | Three declared faults write failure JSON and exit one; this is exact transport of pinned seed intervals, not a fresh quadrature. |
| `gamma_finite_metric_transfer_check_20260913.py` | `--output`; 121 exact checks; `python_optimized` | Five faults write JSON with exactly one named failure and exit one. |
| `gamma_phase_fibre_transport_check_20260913.py` | required `--output`; sibling `gamma_phase_fibre_transport_20260913.tex` is read; `optimized_python` | Three faults write failure JSON and exit one; preserve its source hash and failed-entry list. |
| `gamma_seed_coefficient_certificate_20260913.py` | required `--input` and `--output`; input is the exact inherited TI normal JSON; `optimization_flag` | `--negative-control` rejects the false `Q0<1` bound before writing output; require exit one, absent output, and its exact rejection text. |
| `gamma_finite_metric_transfer_independent_check_20260913.py` | no argument parser; writes `gamma_finite_metric_transfer_independent_check_result_20260913.json` beside its own file | No supplied negative mode. Its 37-check result is a positive independent algebraic regression, not a newly invented mutant suite. |

The generic replay must therefore support a declared output filename instead of requiring every unchanged checker to produce `result.json`. It must preserve the fixed basename for companion-based checkers. For the seed coefficient transfer, copying the TI JSON into the isolated directory and passing its local basename with `--input` satisfies the required contract without accessing the parent workspace. The source-cost checker has a different input receipt and must receive that exact Gamma seed companion. Its hardcoded input hash is not interchangeable with the FE/TI input hash.

The archived Gamma negative control differs from the Toda archived suite, whose deliberate control ran an extra unittest method and wrote a failed JSON record. Reusing Toda's negative JSON expectations would reject the intended Gamma behavior or mistake an early exception for a suite result. The new spec must encode each actual control's semantics rather than apply one blanket negative-case schema.

Normal and optimized modes should be separately executed with the actual commands and compared after removing only each checker's declared mode field. Relevant field names differ: `python_optimized`, `optimized_python`, and integer `optimization_flag`. Scripts without a recorded mode field should have their identical output compared directly; the receipt should record the executed `-O` argument without inventing a process-reported field. Fault result lists and mathematical output values are never omitted from this comparison.

## 6. Execution provenance and package immutability

The original Toda `run` helper records only label, exit code, and stdout/stderr hashes; its per-job update adds script hash, receipt hash, a requested PYTHONPATH flag, and parsed record. It does not record the complete argv, actual working directory, copied support hashes, or an actual mode field as separate execution provenance. The later H seal had to distinguish details reconstructed from the executed script from details actually observed in its result.

Gamma should record argv, cwd, the actual interpreter, requested optimization mode, selected environment override, copied input hashes, result filename, actual exit code, stdout/stderr hashes, and any checker's own observed mode field directly during each execution. An unavailable mode field should remain unavailable. Record whether a declared pinned Python path was actually set; the old `pinned_pythonpath_used` default is a requested flag and can misdescribe an environment when no such spec path exists. Remove ambient PYTHONPATH for jobs declaring that they use the ordinary installed runtime, and apply the pinned path only to jobs that actually require that declared dependency.

The reader command's execution record should also be retained, rather than discarded after its return code check. The complete logs belong to the replay result inventory. No later metadata repair should relabel inferred command details as independent observations. A verifier can confirm an existing receipt without repeating the expensive mathematics; its own receipt must explicitly state that it only verified those existing records.

Replay outputs are exclusive: the declared final portable receipt must not already exist. A failed previous replay or stage is preserved under its own path; a new authorized attempt gets a fresh declared destination. The copied package may change its generated PDF and build artifacts during compilation, while all copied proof/source inputs and the original stage/baseline remain fixed. Standalone checker outputs belong outside the package under their isolated run directories. These are workflow repairs within the existing task, not new permission requests.

The collector/stager/replayer has no publication or freezing command. Its imports must not execute such actions. Publication and freeze still require their own later exact-byte verification and the coordinated owner's established integration lane. This review performs none of them.

## 7. Concrete acceptance state for the forthcoming Gamma implementation

The inherited baseline has been fully verified. The new workflow review should now check its actual H pins and commit; the five named new proof inputs and one whole source witness; complete component-manifest and companion closure; preservation of all H proof/source/converted bytes; current production/QA/source-audit binding; dated H metadata history; exact/public metadata hashes and complete alias glossary; fresh destination and replay isolation; actual checker-specific positive/negative contracts; direct execution provenance; and unchanged H/stage snapshots.

The final PDF, page count, all-page QA, source audit, and global mathematical review remain supplied by the root's final build. Their absence before that build is a pending production input, not a mathematical failure and not authorization to infer success. The independently reviewed Gamma implementation and its final concrete specification will be recorded separately once available.
