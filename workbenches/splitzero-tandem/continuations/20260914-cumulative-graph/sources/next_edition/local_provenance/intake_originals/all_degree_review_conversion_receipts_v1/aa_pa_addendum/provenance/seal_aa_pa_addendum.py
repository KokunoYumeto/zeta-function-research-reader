"""Seal three whole accepted AGT support proofs as an additive source version."""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parent
DEST=ROOT/'aa_pa_addendum'
def pin(path):
    path=Path(path);b=path.read_bytes()
    return {'path':str(path),'relative_path':path.relative_to(ROOT).as_posix(),
            'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def write(path,b):
    path.parent.mkdir(parents=True,exist_ok=True)
    if path.exists() and path.read_bytes()!=b:raise RuntimeError('Refusing sealed source mutation')
    path.write_bytes(b)

selection=ROOT.parent/'tau_all_degree_angle_public_reader_inputs_20260913.json'
assert hashlib.sha256(selection.read_bytes()).hexdigest()=='778d7a7d2fe5b6425f1ec37ebc33c5929b7b298543023cf101af072da965dc00'
selection_copy=DEST/'provenance/AGT_PUBLIC_READER_INPUTS.json';write(selection_copy,selection.read_bytes())
public=set();local={selection_copy};proofs=[]
for key,n,prefix,digest in [
 ('all_degree_angle_review',44,'AA','b0634428d69f80dedd4f68766ef9e6468c390eaac86dfe58b08c21c8fb896e03'),
 ('principal_angle_volume_review',29,'PA','5f6a75afdbdfd4dcd81781a336702ea6d6545fd8fd0a9b2e014a605e414b3198'),
 ('angle_primitive_acceptance',0,'','8def95f8c69d3df47a82948882d161ba134b1b37d3abfb482595891eb93a2f56')]:
    receipt=ROOT/'receipts'/f'{key}.json';r=json.loads(receipt.read_text(encoding='utf-8'))
    c=json.loads((ROOT/r['adapter_row']['conversion_receipt']).read_text(encoding='utf-8'))
    assert r['original_source']['sha256']==digest
    if key!='angle_primitive_acceptance':assert r['public_source']['sha256']==digest
    assert r['source_equation_tags']==[prefix+str(i) for i in range(1,n+1)]
    assert all((r['exact_byte_inverse_restores_entire_original_source'],
                r['complete_expected_original_to_public_literal_sequence_equal'],
                c['prepared_edit_inverse_restores_complete_original_ast'],
                c['writer_edit_inverse_restores_complete_prepared_ast'],
                c['all_complete_literal_payload_byte_spans_equal_original']))
    source=Path(r['public_source']['path']);wrapper=Path(r['wrapper']['path'])
    public.update((source,wrapper));public.update(ROOT/v for v in c['artifacts'].values())
    local.update((receipt,Path(r['raw_snapshot']['path']),Path(r['raw_original_ast']['path'])))
    proofs.append({'key':key,'title':r['adapter_spec']['title'],
        'public_source':pin(source),'wrapper':pin(wrapper),'original_source_sha256':digest,
        'original_source_bytes':r['original_source']['bytes'],
        'complete_source_equation_tags':r['source_equation_tags'],'math_node_counts':r['math_node_counts'],
        'typed_code_count':r['typed_code_count'],
        'typed_plain_or_malformed_math_count':r.get('typed_plain_or_malformed_math_count',0),
        'retained_code_count':r['retained_code_count'],'adapter_spec':r['adapter_spec'],
        'adapter_row':r['adapter_row'],'local_exact_source_inverse':pin(receipt),
        'proof_status':'complete-supporting-proof-selected-from-parent-accepted-AGT-companion',
        'source_conversion_status':'complete-raw-public-AST-prose-literal-inverses-and-clean-compiler-check',
        'source_reading':'Entire original source read in this conversion lane; no new mathematical re-audit is claimed.'})
public.add(DEST/'public_provenance/PRIMITIVE_NOTATION_AND_AST_INVERSE.json')
public.add(DEST/'SOURCE_PLAN.md')
public.add(ROOT/'pipeline/endpoint_source_appendix_adapter.py')
independent_review=DEST/'independent_review/PRIMITIVE_FINAL_READINESS_REVIEW.json'
assert pin(independent_review)['sha256']=='50150f8a2057d600defb78361eaa9b666bde5666a6d9b164458fe3172b3707f4'
for path in sorted((DEST/'independent_review').rglob('*')):
    if path.is_file():local.add(path)
for name in ('prepare_conversions.py','prepare_angle_primitive.py','syntax_check.py','seal_aa_pa_addendum.py','check_staged_aa_pa_syntax.py'):
    frozen=DEST/'provenance'/name;write(frozen,(ROOT/name).read_bytes());local.add(frozen)
stage_script=ROOT.parent/'stage_all_degree_review_conversions_20260913_v19.py'
stage_frozen=DEST/'provenance'/stage_script.name;write(stage_frozen,stage_script.read_bytes());local.add(stage_frozen)
syntax_source=ROOT/'syntax_aa_pa_primitive/SYNTAX_RECEIPT.json'
syntax_target=DEST/'provenance/SYNTAX_RECEIPT.json';write(syntax_target,syntax_source.read_bytes());local.add(syntax_target)
syntax=json.loads(syntax_target.read_text(encoding='utf-8'))
assert not any((syntax['exit_code'],syntax['overfull_boxes'],syntax['missing_glyphs'],syntax['undefined_controls'],syntax['latex_errors']))
assert syntax['keys']==[p['key'] for p in proofs]
for p in sorted(public):
    assert b'Users' not in p.read_bytes(),str(p)
earlier={
 'READY_FIVE_INPUTS.json':'0d78f48c47c44df7f0ec5bedfd597931ad9420466bd33f10ef6699690fb91b95',
 'SCALING_WINDOW_ADDENDUM_INPUTS.json':'db429fcb46c06b2e6510b8943c82577813bbccf36a68b7b5343d62876d237a10',
 'VARIATION_ADDENDUM_INPUTS.json':'94aa2f4a078a4ff88513c12f2e94a5fc8e0284da3146d4bd7e27a74fd88615d0',
 'fs_sr_addendum/READY_INPUTS.json':'0a0a70b64771809ccd896fade135ea0f85adbb2f66ab1f7edc6e6ec3c1bf0339',
 'layout_ready_five/TYPOGRAPHY_ACCEPTANCE.json':'47db50054bc8c78a96b6f2d4deb14b101c6e538d7e03d588ef96049b7ef235cd'}
for name,digest in earlier.items():assert pin(ROOT/name)['sha256']==digest
result={'schema':'actual-tau-AA-PA-primitive-complete-source-readiness-v1',
 'status':'three-complete-accepted-supporting-proof-conversions-sealed',
 'parent_accepted_companion_selection':pin(selection_copy),
 'existing_source_and_typography_seals_unchanged':[pin(ROOT/name) for name in earlier],
 'additional_complete_source_count':3,'preceding_complete_source_conversion_count':10,
 'combined_complete_source_conversion_count':13,'additional_complete_math_nodes':440,
 'combined_complete_math_nodes_in_this_lane':3064,
 'proofs':proofs,'public_support':[pin(p) for p in sorted(public)],
 'local_provenance_only':[pin(p) for p in sorted(local)],
 'primitive_transcription':{
   'original_byte_count':5785,'original_sha256':'8def95f8c69d3df47a82948882d161ba134b1b37d3abfb482595891eb93a2f56',
   'typed_byte_count':5828,'typed_sha256':'a78384fe3a1cff8398713f89181c38c62351315d6f32aca314d357e457938de4',
   'explicit_delimiter_repairs':26,'plain_parenthesized_count':17,'malformed_delimiter_count':9,
   'existing_math_payloads_unchanged':7,'source_and_hash_Code_payloads_unchanged':6,
   'full_original_byte_inverse':True,'full_raw_to_typed_AST_inverse':True,
   'public_complete_inverse':pin(DEST/'public_provenance/PRIMITIVE_NOTATION_AND_AST_INVERSE.json')},
 'syntax_check':syntax,'visual_acceptance':False,
 'independent_complete_primitive_notation_and_inverse_acceptance':pin(independent_review),
 'scope':'Every complete AA1–AA44 and PA1–PA29 proof and all six primitive-acceptance proof paragraphs are retained. Original mathematical payloads, all tensor differential signs, full deterministic division, original norm domains, all proof prose and equation tags remain. This seals source readiness and exact byte/AST/literal inverses, without claiming a new mathematical audit or final cumulative PDF visual acceptance.'}
target=DEST/'READY_INPUTS.json';write(target,(json.dumps(result,ensure_ascii=False,indent=2)+'\n').encode())
print(json.dumps({'manifest':pin(target),'public_support_count':len(public),'local_provenance_count':len(local),'whole_proofs':3,'math_nodes':440}))
