"""Seal the two complete UG sources for cumulative-reader integration."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parent
def pin(p):
    p=Path(p);b=p.read_bytes()
    return {'path':str(p),'relative_path':p.relative_to(ROOT).as_posix(),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def write(p,b):
    p.parent.mkdir(parents=True,exist_ok=True)
    if p.exists() and p.read_bytes()!=b:raise RuntimeError('Refusing sealed conversion mutation: '+str(p))
    p.write_bytes(b)
def data(x):return (json.dumps(x,ensure_ascii=False,indent=2)+'\n').encode('utf-8')
keys=['f1_unit_gauge','f1_unit_gauge_review'];proofs=[];public=set();local=set()
for key in keys:
    receipt=ROOT/'receipts'/f'{key}.json';r=json.loads(receipt.read_text(encoding='utf-8'))
    cpath=ROOT/r['adapter_row']['conversion_receipt'];c=json.loads(cpath.read_text(encoding='utf-8'))
    for name,value in {
      'publication_inverse':r['exact_byte_inverse_restores_entire_original_source'],
      'literal_sequence':r['complete_expected_original_to_public_literal_sequence_equal'],
      'prepared_ast_inverse':c['prepared_edit_inverse_restores_complete_original_ast'],
      'writer_ast_inverse':c['writer_edit_inverse_restores_complete_prepared_ast'],
      'emitted_literal_payloads':c['all_complete_literal_payload_byte_spans_equal_original'],
      'original_source_unchanged':r['source_unchanged_after_conversion']}.items():
        if not value:raise RuntimeError('Unproved source invariant: '+name)
    original=Path(r['original_source']['path']).read_bytes()
    if len(original)!=r['original_source']['bytes'] or hashlib.sha256(original).hexdigest()!=r['original_source']['sha256']:
        raise RuntimeError('Accepted original changed after conversion')
    source=Path(r['public_source']['path']);wrapper=Path(r['wrapper']['path'])
    public.update((source,wrapper,cpath))
    for artifact in c['artifacts'].values():public.add(ROOT/artifact)
    mapping=ROOT/(key+'_math_mapping.json');m=json.loads(mapping.read_text(encoding='utf-8'))
    portable=json.loads(json.dumps(m));portable['source'].pop('path')
    portable['source']['filename']=Path(m['source']['path']).name
    portable['publication_note']='Original source SHA-256 identifies the accepted full source. This portable dictionary contains every original Code payload and its complete Math replacement; the complete original bytes and public-wording inverse are retained in local provenance.'
    target=ROOT/'public_mapping'/(key+'_math_mapping.json');write(target,data(portable));public.add(target)
    local.update((receipt,mapping,Path(r['raw_snapshot']['path']),Path(r['raw_original_ast']['path']),Path(r['public_original_ast']['path'])))
    proofs.append({'key':key,'title':r['adapter_spec']['title'],'public_source':pin(source),'wrapper':pin(wrapper),
      'original_source_sha256':r['original_source']['sha256'],'original_source_bytes':r['original_source']['bytes'],
      'complete_source_equation_tags':r['source_equation_tags'],'math_node_counts':r['math_node_counts'],
      'typed_code_count':r['typed_code_count'],'retained_code_count':r['retained_code_count'],
      'adapter_spec':r['adapter_spec'],'adapter_row':r['adapter_row'],
      'portable_complete_math_mapping':pin(target),'local_exact_publication_inverse':pin(receipt),
      'source_and_proof_scope':'Entire accepted source body, all proof paragraphs and original formula blocks. No source selection or mathematical summary.'})
public.add(ROOT/'pipeline/endpoint_source_appendix_adapter.py')
for name in ('prepare_conversions.py','parent_pipeline_reference.py','make_unit_gauge_mappings.py','syntax_check.py','seal_unit_gauge_inputs.py'):
    original=ROOT/name;frozen=ROOT/'provenance/sealed'/name;write(frozen,original.read_bytes());local.add(frozen)
acceptance=ROOT/'review/INDEPENDENT_TYPING_ACCEPTANCE.json'
review=json.loads(acceptance.read_text(encoding='utf-8'))
if review['status']!='accepted' or {x['key'] for x in review['sources']}!=set(keys):
    raise RuntimeError('Independent typing acceptance does not cover both full sources')
for row in review['sources']:
    if row['status']!='accepted':raise RuntimeError('Source not accepted by independent typing review')
    for field in ('original_source','mapping','public_source','converted_tex','wrapper','conversion_receipt','source_typing_receipt'):
        expected=row[field];b=Path(expected['path']).read_bytes()
        if len(b)!=expected['bytes'] or hashlib.sha256(b).hexdigest()!=expected['sha256']:
            raise RuntimeError('Independent typing review pin changed: '+field)
local.add(acceptance)
for p in (ROOT/'review').rglob('*'):
    if p.is_file():local.add(p)
root_acceptance=Path(json.loads((ROOT/'receipts/f1_unit_gauge.json').read_text(encoding='utf-8'))['original_source']['path']).parent/'ROOT_ACCEPTANCE.md'
snapshot=ROOT/'raw/ROOT_ACCEPTANCE.md';write(snapshot,root_acceptance.read_bytes());local.add(snapshot)
syntax=ROOT/'syntax_check/SYNTAX_RECEIPT.json';syn=json.loads(syntax.read_text(encoding='utf-8'))
if syn['exit_code'] or syn['overfull_boxes'] or syn['missing_glyphs'] or syn['undefined_controls'] or syn['latex_errors']:
    raise RuntimeError('Full fragment syntax check is not clean')
frozen=ROOT/'provenance/sealed/SYNTAX_RECEIPT.json';write(frozen,syntax.read_bytes());local.add(frozen)
result={'schema':'unit-gauge-ready-complete-source-conversion-inputs-v1',
 'status':'two-complete-source-conversions-sealed','completed_source_count':2,
 'original_inline_code_count':121,'typed_mathematical_code_count':115,'retained_code_count':6,
 'unchanged_original_display_math_count':27,'total_converted_math_count':142,
 'original_gauge_equation_tags':['UG'+str(i) for i in range(1,20)],
 'proofs':proofs,'public_support':[pin(p) for p in sorted(public)],
 'local_provenance_only':[pin(p) for p in sorted(local)],
 'independent_typing_acceptance':pin(acceptance),'syntax_check':syn,
 'layout_state':'Both complete fragments compile under the inherited cumulative reader preamble with zero overfull boxes, missing glyphs, undefined controls or LaTeX errors. This is syntax readiness; no final PDF or visual acceptance is claimed.',
 'publication_boundary':'Only public_support is selected for public inclusion. local_provenance_only retains the unchanged original source bytes, absolute local locators, exact public-wording inverse, independent audit and workflow scripts. Portable mathematical mapping files retain every original formula Code payload without private absolute paths.',
 'scope':'Complete mathematical source transcription and exact byte/AST/literal preservation. The original mathematics was already accepted. No new mathematical fixture replay, Lean execution, remote publication or cumulative-master edit occurred.'}
for p in public:
    raw=p.read_bytes()
    for forbidden in (b'C:/Users/',b'C:\\Users\\',b'F:/user/',b'F:\\user\\'):
        if forbidden in raw:raise RuntimeError('Absolute local path in selected public support: '+str(p))
target=ROOT/'READY_UNIT_GAUGE_INPUTS.json';write(target,data(result))
print(json.dumps({'inventory':pin(target),'public_support_count':len(public),'local_provenance_count':len(local),'source_count':2}))
