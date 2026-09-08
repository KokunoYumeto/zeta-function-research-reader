"""Build the full inclusion body and bounded provenance/claim records."""
from pathlib import Path
import json,hashlib,re,datetime,sys
ROOT=Path(__file__).resolve().parents[1]
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def read(relative): return (ROOT/relative).read_text(encoding='utf-8-sig')
def expand(relative, stack=()):
    if relative in stack: raise ValueError("cyclic input")
    text=read(relative)
    return re.sub(r'\\input\{([^}]+)\}',lambda m: expand(m[1],stack+(relative,)),text)
body=expand('tex/proofs.tex')
header=("% Complete inclusion-ready proof body; no omitted inputs.\n"
        "% Requires amsmath, amssymb, amsthm, booktabs, hyperref, mathrsfs and proposition/theorem/lemma/corollary/definition/remark environments.\n"
        "% Bibliography keys are in complete_bibliography.bib.\n"
        "% Our prose and proofs only; external primary-source TeX is not embedded.\n"
        "\\providecommand{\\GL}{\\operatorname{GL}}\n"
        "\\providecommand{\\End}{\\operatorname{End}}\n")
(ROOT/'complete_proof_fragment.tex').write_text(header+body,encoding='utf-8')
(ROOT/'complete_bibliography.bib').write_text(read('build/combined.bib'),encoding='utf-8')
root_claims=[
 ('ROOT-01','conductor specialization and exact Tor sign','tex/specialization_spectral.tex','prop:spec-defect'),
 ('ROOT-02','finite sign-group graded characters and conductor layer','tex/specialization_spectral.tex','eq:specialization-matrix'),
 ('ROOT-03','finite-field point-count zeta factors with chart exclusion','tex/specialization_spectral.tex','eq:node-zeta'),
 ('ROOT-04','characteristic-coefficient invariant ring pullback and kernel','tex/specialization_spectral.tex','prop:matrix-invariants'),
 ('ROOT-05','GCT coefficient conic is exactly original-cover base change','tex/conic_arithmetic_bridge.tex','prop:conic-base-change'),
 ('ROOT-06','coefficient polynomial in unchanged a and s coordinates','tex/conic_arithmetic_bridge.tex','eq:C-a'),
 ('ROOT-07','rank-four Laurent extension and inverse block operator','tex/conic_arithmetic_bridge.tex','eq:quartic-operator'),
 ('ROOT-08','original arithmetic spectral coordinate preserved','tex/conic_arithmetic_bridge.tex','eq:quartic-q'),
 ('ROOT-09','source coefficient transported to polynomial in S','tex/conic_arithmetic_bridge.tex','eq:coefficient-operator'),
 ('ROOT-10','coefficient heat derivation and both ramification loci','tex/conic_arithmetic_bridge.tex','The original coefficient heat flow'),
 ('ROOT-11','two involutions and exact negative circle evaluation','tex/conic_arithmetic_bridge.tex','The exact positivity test'),
 ('ROOT-12','Boolean formula counting and uniform bit interface','tex/boolean_reduction.tex','prop:counting'),
 ('ROOT-13','one-index VNP verifier family with exact witness padding','tex/boolean_reduction.tex','t=(n+m-2)'),
 ('ROOT-14','full material drift, scalar pullback and unique localized cubic lift','tex/material_generator_interface.tex','eq:gct-full-material-drift'),
 ('ROOT-15','original two-coefficient Euclidean diffusion with exact common-fibre values','tex/material_generator_interface.tex','eq:gct-Euclidean-coefficients'),
 ('ROOT-16','arbitrary-b quartic conic maps, original inverse coordinates and both branch loci','tex/material_extension.tex','eq:rb-quartic'),
 ('ROOT-17','arbitrary-b rank-four multiplication and original spectral-coordinate recovery','tex/material_extension.tex','eq:rb-original-S'),
 ('ROOT-18','full localized rank-four connection and every zeroth-order square term','tex/material_extension.tex','eq:rb-full-square')]
claims=[{'id':i,'statement':s,'proof_file':f,'locator':loc,
         'status':'proved_here','proof_sha256':sha(ROOT/f),
         'checker':('agents/material_extension/check_material_extension.py' if f=='tex/material_extension.tex' else 'scripts/check_bridges.py'),
         'check_scope':'symbolic identities and bounded finite checks; general proofs are in TeX'}
        for i,s,f,loc in root_claims]
for path in ['agents/fibre_complexity/claims.json','agents/invariant_transport/claims.json',
             'agents/material_extension/claims.json',
             'agents/gct_obstruction_literature/source_route_and_claims.json']:
    data=json.loads(read(path))
    claims.append({'id':'IMPORTED-PROOF-INVENTORY-'+path.split('/')[1],
                  'status':'individual_claim_status_retained','inventory':path,'data':data})
continuation_claims=ROOT/'logbook/continuation_claims.json'
if continuation_claims.exists():
    for claim in json.loads(continuation_claims.read_text(encoding='utf-8-sig')):
        claim['proof_sha256']=sha(ROOT/claim['proof_file'])
        claims.append(claim)
(ROOT/'claims.json').write_text(json.dumps({'schema_version':1,'claims':claims,
 'source_theorem_status':'External GCT/Connes theorems are attributed source results, not asserted independently certified; conjectured arrows remain conjectured.',
 'nonclaims':['No RH counterexample','No P=NP or P!=NP proof','No general nonstandard quantum-group positivity theorem',
              'No permanent/determinant obstruction inferred from the fixed binary cubic or independent-block family']},indent=2),encoding='utf-8')
edges=[
 ('retained_F','projective_simple_root_cubic','proved coordinate isomorphism; x=0 sheet retained','tex/retained_fibres.tex'),
 ('retained_cubics_n','selector_determinant_4n_plus_1','proved coefficient-recoverable determinant projection','tex/retained_fibres.tex'),
 ('selector_determinant_4n_plus_1','determinant_orbit_boundary','proved explicit endomorphism degeneration and strict nonorbit inclusion','tex/gct_obstruction_interface.tex'),
 ('determinant_orbit_boundary','graded_coordinate_quotient','proved exact kernel and degreewise multiplicity inequality','tex/gct_obstruction_interface.tex'),
 ('retained_cover','node_conductor','proved completed self-fibre product; physical exclusion separate','tex/invariant_transport.tex'),
 ('node_conductor','GL2_induced_defect_modules','proved exact induction; explicit adjoint and determinant-inverse submodules','tex/invariant_transport.tex'),
 ('node_conductor','finite_field_zeta','proved point counts and conductor factors','tex/specialization_spectral.tex'),
 ('GCT_IV_coefficient','retained_conic_base_change','proved Laurent coordinate ring isomorphisms','tex/conic_arithmetic_bridge.tex'),
 ('retained_conic_base_change','arithmetic_rank4_module','proved finite free tensor extension, companion operator and spectral-coordinate preservation','tex/conic_arithmetic_bridge.tex'),
 ('coefficient_heat','conic_derivation','proved localized derivation with full exceptional loci','tex/conic_arithmetic_bridge.tex'),
 ('full_material_drift','localized_cubic_derivation','proved unique lift retaining the transverse 6c derivative','tex/material_generator_interface.tex'),
 ('original_Euclidean_diffusion','two_source_dependent_coefficients','proved exact A and B expression and common-fibre nonconstancy','tex/material_generator_interface.tex'),
 ('retained_quadratic_arbitrary_b','Laurent_rank4_arbitrary_b','proved quartic, original-coordinate recovery, full connection and square','tex/material_extension.tex'),
 ('Boolean_formula','VNP_counting_family','proved exact arithmetization and encoding','tex/boolean_reduction.tex'),
 ('nonstandard_RH_programme','nonstandard_positivity','source-proposed extension; no full Frobenius hypothesis specified','tex/nonstandard_rh_bridge.tex'),
 ('nonstandard_positivity','effective_multiplicity_formulas','source requires additional labels/cells/reciprocity/effectivity','tex/nonstandard_rh_bridge.tex'),
 ('effective_multiplicity_formulas','complexity_obstruction','source additionally requires obstruction existence and class-variety transport','tex/nonstandard_rh_bridge.tex')]
edge_records=[{'from':a,'to':b,'status_and_map':s,'proof_or_source_record':p} for a,b,s,p in edges]
continuation_edges=ROOT/'logbook/continuation_dependencies.json'
if continuation_edges.exists():
    edge_records.extend(json.loads(continuation_edges.read_text(encoding='utf-8-sig')))
(ROOT/'dependencies.json').write_text(json.dumps({'schema_version':1,'edges':edge_records},indent=2),encoding='utf-8')
routes=[]
for p in ['agents/nonstandard_rh/source_route.json','agents/invariant_transport/source_routes.json',
          'agents/material_extension/provenance.json',
          'logbook/quantum_tensor_source_route.json',
          'agents/ym_composition_review/source_provenance.json',
          'agents/ns_scaling_bridge/source_audit/source_audit.json',
          'agents/gct_obstruction_literature/source_route_and_claims.json']:
    if (ROOT/p).exists(): routes.append({'path':p,'sha256':sha(ROOT/p),'data':json.loads(read(p))})
for folder in ['gct_generator_block','coefficient_geometry','shared_verifier',
               'full_source_generators','source_character_decomposition',
               'frobenius_generator_bridge','compressed_permanent_trace']:
    for filename in ['source_receipt.json','source_receipts.json','provenance.json','source_audit.json']:
        p=f'agents/{folder}/{filename}'
        if (ROOT/p).exists():
            routes.append({'path':p,'sha256':sha(ROOT/p),'data':json.loads(read(p))})
parent=Path('[local]/Documents/Papors/Chatnotes/Zeta-Function-Foundation')
localsources=[
 (parent/'ACTIVE_RESEARCH_DIRECTION.md','Read entire current source direction; no RH counterexample recorded'),
 (parent/'tex/satellites/23_source_mechanism_transfer.tex','Read complete mechanism; used original fibre/node/arithmetic formulas'),
 (parent/'logbook/rh_counterexample_20260908/mechanism_actions.json','Read source and claim routing receipt'),
 (parent/'config/literature_index_entrypoint.json','Read query/path contract; no index modified'),
 (parent/'tex/satellites/27_material_arithmetic_generator.tex','Read entire new parent chapter; independently proved all material/root/Euclidean identities used, retained full arbitrary-b connection'),
 (Path('[local]/Documents/math/output/navier_stokes_research_2026-09-08/tex/inverse_fibre_heat.tex'),
  'Read full fibre/heat extension; used identities independently rederived'),
 (Path('[local]/Documents/Papors/used often/NCG/Zeta-zeros-and-prolateproofs-final-2024.pdf'),
  'Primary PDF pages 1 and 17-19, section 3.6, Proposition 3.6 and preceding definitions')]
prior_sources=json.loads(read('sources.json')) if (ROOT/'sources.json').exists() else {}
source_observations=prior_sources.get('local_sources',[])
if '--observe-parent' in sys.argv:
    source_observations=[{'path':str(p),'observed_sha256_at_seal':sha(p),
      'bytes':p.stat().st_size,'read_scope':s,
      'hash_scope':'Explicit current source observation; exact initial source hashes remain in subordinate records'}
      for p,s in localsources]
(ROOT/'sources.json').write_text(json.dumps({'schema_version':1,'private_provenance':True,
 'routes':routes,'local_sources':source_observations,
 'parent_observation_mode':'explicit_refresh' if '--observe-parent' in sys.argv else 'preserved_prior_read_receipts_no_external_files_opened',
 'online_source_shelves':'Bounded source archives and exact hashes under agent source routes; local only',
 'no_source_library_mutation':True},indent=2),encoding='utf-8')
chronology=[
 'Read exact parent sources and current directives; bounded session input intake saved.',
 'User correction prioritizes nonstandard RH finite-field GCT programme; exact original TeX located.',
 'Independent fibre/complexity, invariant-theory and nonstandard-source work completed in separate folders.',
 'Original source identified with complete simple-root locus of projective cubic; selector determinant 4n+1 proved.',
 'Source GCT IV coefficient conic identified with base change of retained a=-rÃƒâ€šÃ‚Â²; rank-four s extension constructed.',
 'Exact Tor/character/finite-field zeta and characteristic-invariant maps proved.',
 'Independent review repaired one-index VNP convention and original-vs-extended operator typing; full bit encoding clarified.',
 'Coefficient heat derivation and two real-structure evaluation tests added; original 297 root checks pass.',
 'Latest parent source chapter read in full; complete material drift and two-coefficient Euclidean diffusion rederived, bringing root checks to 308; arbitrary-b rank-four connection integrated.',
 'Core PDF compiled clean; whole-page render inspection performed; final source-bound orbit interface integrated.',
 'Completed artifacts, source/claim/dependency records and reproduction receipt sealed; unresolved endpoint statements remain explicit.']
continuation_events=ROOT/'logbook/continuation_events.json'
if continuation_events.exists():
    chronology.extend(json.loads(continuation_events.read_text(encoding='utf-8-sig')))
(ROOT/'logbook/chronology.json').write_text(json.dumps({'schema_version':1,
 'date':'2026-09-08','events':[{'order':i+1,'event':e} for i,e in enumerate(chronology)],
 'prior_goal_turn_classification':'progress: source files, complete proof fragments, exact checks and rendered reader changed authoritative state'},indent=2),encoding='utf-8')
manifestfiles=[]
for name in ['reader.pdf','complete_proof_fragment.tex','complete_bibliography.bib','bibliography.bib','.gitignore','README.md','requirements.txt',
 'claims.json','dependencies.json','sources.json','checks/reproduction.json','checks/pdf_qa.json']:
    p=ROOT/name
    if p.exists(): manifestfiles.append(p)
for folder in ['tex','scripts','checks','logbook']:
    manifestfiles.extend(p for p in (ROOT/folder).glob('*') if p.is_file() and p.suffix in ['.tex','.py','.json','.md'])
for p in (ROOT/'agents').rglob('*'):
    if not p.is_file() or p.suffix not in ['.tex','.bib','.py','.json','.md']:
        continue
    if any(part in ['shelf','sources','source','build','qa','checkout','checkout_material','__pycache__'] for part in p.relative_to(ROOT).parts):
        continue
    manifestfiles.append(p)
seen=set(); entries=[]
for p in manifestfiles:
    rel=p.relative_to(ROOT).as_posix()
    if rel not in seen:
        seen.add(rel); entries.append({'path':rel,'bytes':p.stat().st_size,'sha256':sha(p)})
(ROOT/'manifest.json').write_text(json.dumps({'schema_version':1,
 'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'hash_algorithm':'SHA-256','self_hash_excluded':True,'files':entries},indent=2),encoding='utf-8')
print(json.dumps({'complete_fragment_bytes':(ROOT/'complete_proof_fragment.tex').stat().st_size,
                  'root_claims':len(root_claims),'manifest_files':len(entries)}))
