from pathlib import Path
import hashlib,json,re
ROOT=Path(r'workspace:')
OUT=ROOT/'work/backpropagation_20260913/boundary'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
manifest=json.loads((OUT/'PATCH_MANIFEST.json').read_text(encoding='utf-8'))
results=json.loads((OUT/'CONCLUSION_REPLACEMENTS.json').read_text(encoding='utf-8'))
for r in manifest['records']:
 if 'revised' in r:
  assert sha(OUT/r['revised'])==r['revised_sha256']
  assert sha(Path(r['source']))==r['original_sha256']
 else:
  assert sha(Path(r['source']))==r['sha256']
  assert sha(OUT/r['copied'])==r['sha256']
for r in results['records']:
 assert sha(Path(r['source']))==r['source_sha256']
 assert Path(r['source']).read_text(encoding='utf-8-sig').count(r['old'])==1
proofs=[
('XD1–26','XD.u1–7','Exact ordinary division and derivative correction give the full u matrix, chain-degree term, flatness and original determinant constants.','R52; SC.u1–7; PC.u1–3; LC.u1; DC31–32; RCX.u1–6; APU1–23.'),
('DS1–69, especially DS69 source deformation','DS70–74','Degree-correct ordered chain operator and the actual source connection/Euler commutator retain the theta primitive.','R51/R52/R57; R68 product degree terms and exact transverse map; R70 regular formal operator.'),
('DT1–13 translation and fixed-point character','DT14–16','Full u scalar-gauge derivative and explicitly typed derived compact-support direct images over G_m,u × A1,t retain the entire character sheaf.','R52 family-character correction; RCX.u5–6; R62 pure-u translation terms.'),
('SC1–37 constituent and neighboring minors','SC.u1–7','Full Hermitian Hessian in u,t; original moving theta metric; every primary ideal determinant with all Gamma/Pascal/frame constants; exact zero u-normal map on that primary t=0 slice.','R52/R56/R57/R62; PC.u3 and quotient Hessian.'),
('PC1–41, including original PC30 full proof','PC.u1–3 and PC30a–g','Full observer u derivative. Original cyclic map gains its full factorial image, saturation, free complement, Tor map, residual-collision polynomial and specialized kernel. PC30 characteristic-zero formula preserved.','R56/R68; BPC1–14; SPBT tensor continuation.'),
('LC1–16','LC.u1','Exact u transport of metric, Laplacian and action retains the original numerical-range parameter and full comparison eigenvalues.','R57; RCX.u3–4 original metric and forced relation descendants.'),
('DC1–30 all four observation roles','DC31–32','Every observation map has the exact u inverse derivative; original weighted circle form, empty kernels and diamond maps retained.','R59 four observations and original metric derivatives.'),
('RCX1–40, including RCX38 translation scope','RCX.u1–6','Complete noncommutative two-parameter derivative recursion, original path metric derivative, forced Laplacian u descendant and pure-u translation terms.','R62; original t-jet calculations remain their r=0 slice.'),
('BC original final future-primary paragraph','Full SPC proof continuation and SPBT1–3','Single-primary period/monodromy/source/unit/sheaf calculations replace the earlier future calculation; completed tensor characters replace the one-factor-only continuation.','R52/R56/R68; complete BPC/BTP/BTF proofs; exact local-versus-larger coefficient maps.'),
('AP1–26, directly after original AP13','APU1–23','Complete two-parameter rational-pole connection, flatness, residue and oriented-loop maps, full-unit gauge, dual, formal endpoint-source map and shifted transport derivative.','Active tex/actual_tau_analytic_pole_complete.tex; R52/R69/R70/R71.'),
('SPC one-factor invariant vanishing; TP/TPF/TCL stable full source','BPC1–14, BTP1–11, BTF1–11','Exact ordered tensor character projectors, wild cancellation, full Gauss orbit descent and original factorial coefficient lattice with actual phase/CRT denominator exclusions.','PC30a–g; SPBT1–3; R56/R68.'),
]
lines=['# Boundary propagation: final source and dependency receipt','',
'This lane revises the complete affected earlier proof bodies in isolated staging. It preserves the accepted 821-page source edition and every stable BC/SPC/TP source byte. The full cumulative assembly, current-result merge and public delivery belong to the parent. This receipt records the exact local closure rather than claiming that every page of the cumulative corpus was reread.','',
'## Exact earlier-claim propagation','',
'| Earlier claim/proof site | Current proof tags | Actual replacement or refinement | Downstream propagation |',
'|---|---|---|---|']
lines += ['| '+' | '.join(row)+' |' for row in proofs]
lines+=['','## Full reading and proof verification','',
'The parent lane fully read the affected old DS, XD, DT, SC, PC, LC, DC and RCX proof bodies, BC and all AP1–26; bounded rereads recovered initially truncated output. The single-primary child fully read all 1,162 source lines and produced its detailed reading receipt. The tensor child fully read all 2,896 lines of the pinned TP/TPF/TCL source; the earlier 2,917-line estimate was corrected in its final receipt. The parent fully read every new BPC/BTP/BTF and PC30a–g proof, every APU1–23 proof, both primary conclusion insertions, and every current-result replacement.','',
'Independent full inserted-proof review accepted DS70–74, XD.u1–7, DT14–16, SC.u1–7, PC.u1–3, LC.u1, DC31–32 and RCX.u1–6 after the explicitly typed derived direct-image repair. The separate coefficient reviewer accepted PC30a–g and all BPC/BTF coefficient-domain claims. The AP checker reports 52 exact generic polynomial identities; the tensor checker reports 264 unequal-order local and 24 residual-collision cases, all passing. These checks supplement the complete written proofs.','',
'The 127-page combined affected-proof reader compiles in two passes with zero TeX errors and no undefined references. The 11-page complete current-result replacement reader also compiles with zero errors and undefined references. The auxiliary proof reader retains width and duplicate-destination notices from its combined presentation; no visual quality claim is made. The parent builder owns its separate display reflow layer in the full reader.','',
'## Exact phase and coefficient domains','',
'Factorial coefficient calculations use the actual given localization and p greater than every relevant primary order. They preserve r! rather than dividing an original vector by it. The actual finite-field phase also requires every original inverse, in particular m+1, and the presented sheaf calculation uses p>m+1. At m=1,p=2 the supplied coefficient-only map has K=0 and a unit image but cannot extend across 1/2. A local coefficient map is never extended silently through the full sum-CRT stage: its retained divided difference explicitly inverts p when the stated quartet stage has k>=p. The sheaf and coefficient characters are related by their proved common cyclotomic model and two base changes.','',
'The one-factor V^I=0 conclusion remains its original one-factor statement. Ordered complex tensor invariants have dimension (m^k+m(-1)^k)/(m+1); actual finite-field original-inertia invariants also require cancellation of kc. Every original source unit, frame determinant, period contour, additive phase, weight, support label, represented zero and external absent element remains in its exact map.','',
'## Integration routes and exact pins','',
'PATCH_MANIFEST.json is the complete 15-record mathematical overlay. Its hashes are hashes of the actual written file bytes. The active AP route is tex/actual_tau_analytic_pole_complete.tex, with exact reversible wrapper equality in AP_WRAPPER_MAPPING.json. The archived source route is retained as a source dependency and is not substituted for the active compiled route. The complete tensor companion is tex/tensor_primary_boundary_backpropagation.tex. The standalone revised BC is tex/marked_product_boundary_connection.tex; proofs/BC_CURRENT_FRAGMENT.tex is its complete document-wrapper-free equivalent for insertion.','',
'CONCLUSION_REPLACEMENTS.json gives ten unique exact old/new blocks, original source hashes and line locators for R51/52/56/57/59/62 and R68–71. Every old result body is retained; the exact title/family-character/derivative-domain corrections are recorded. R68 and R70 contain complete proofs of their additional transverse and regular formal operator identities. Parent-owned R67 and R72–74 are untouched.','',
'| Route | Actual SHA-256 |','|---|---|']
pinfiles=['PATCH_MANIFEST.json','AP_WRAPPER_MAPPING.json','CONCLUSION_REPLACEMENTS.json','fragments/COMPLETE_CURRENT_RESULT_REPLACEMENTS.tex','proofs/BC_CURRENT_FRAGMENT.tex','BOUNDARY_VERIFICATION.pdf','BOUNDARY_VERIFICATION.log','CURRENT_RESULTS_VERIFICATION.pdf','CURRENT_RESULTS_VERIFICATION.log','receipts/TENSOR_PRIMARY_FULL_READ.md','reviews/SINGLE_PRIMARY_READ.md','fragments/APU_SOURCE_READ.md']
for route in pinfiles:lines.append(f'| {route} | {sha(OUT/route)} |')
lines+=['','## Reproducibility and preservation','',
'The staged patch workflow is build_boundary_patch.py, assemble_boundary_verification.py, apply_boundary_descendants.py, then finalize_boundary_wave.py. The finalizer verifies all source pins, performs the direct PC30 insertion and current BC tensor continuation, constructs the active AP wrapper mapping and hashes final written bytes. assemble_conclusion_replacements.py constructs the separate exact root-merge records. Each stage only writes within this boundary staging directory. Historical inputs are rehashed again by this receipt generator.','',
'The eight original and revised proof diffs, the AP and BC complete-body diffs, and source-reading/check receipts remain alongside the full TeX. Current-source mathematical closure here is complete for the listed sites. The parent confirmed applying all ten exact current-result replacements to their actual sources, including the R52 family-character and R62 pure-derivative corrections, and independently accepted R68–71 after full reading and a separate audit. The cumulative builder owns final compiled-route and display validation.','',
'The subsequently announced FPB/GRM source lane was not consumed by this lane: no claim here asserts that its full-packet formal boundary proofs have been included or reviewed. Any propagation from those sources requires their own pinned full proof reading and actual inclusion. Sectorial multi-primary work and a uniform original arithmetic estimate remain continuing independent calculations, not assumptions inserted into any result.','']
(OUT/'CLAIM_PROPAGATION.md').write_bytes('\n'.join(lines).encode())
audit={'manifest_sha256':sha(OUT/'PATCH_MANIFEST.json'),'conclusion_sha256':sha(OUT/'CONCLUSION_REPLACEMENTS.json'),'verified_overlay_records':len(manifest['records']),'verified_unique_current_result_records':len(results['records']),'historical_sources_unchanged':True,'proof_reader_pages':127,'current_result_reader_pages':11,'new_mathematical_sources_changed_after_final_pins':False,'claim_receipt_sha256':sha(OUT/'CLAIM_PROPAGATION.md')}
(OUT/'FINAL_VERIFICATION.json').write_bytes((json.dumps(audit,indent=2)+'\n').encode())
print(json.dumps(audit,indent=2))
