"""Seal the fully typed accepted AP proof and review with exact current routes."""
from pathlib import Path
import hashlib,json
R=Path(__file__).resolve().parent
def pin(p):
    p=Path(p);b=p.read_bytes();return {'path':str(p),'relative_path':p.relative_to(R).as_posix(),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def dump(x):return (json.dumps(x,ensure_ascii=False,indent=2)+'\n').encode()
def fresh(p,b):
    p.parent.mkdir(parents=True,exist_ok=True)
    if p.exists() and p.read_bytes()!=b:raise RuntimeError('Refusing sealed file mutation '+str(p))
    p.write_bytes(b)
def verify_pin(row):
    p=Path(row['path']);b=p.read_bytes()
    if len(b)!=row['bytes'] or hashlib.sha256(b).hexdigest()!=row['sha256']:raise RuntimeError('Pinned input changed '+str(p))
keys=['analytic_pole','analytic_pole_review'];public=set();local=set();proofs=[]
for key in keys:
    receipt=R/'receipts'/f'{key}.json';r=json.loads(receipt.read_text(encoding='utf-8'))
    conversion=R/r['adapter_row']['conversion_receipt'];c=json.loads(conversion.read_text(encoding='utf-8'))
    verify_pin(r['original_source'])
    if not all((r['exact_byte_inverse_restores_entire_original_source'],r['complete_expected_original_to_public_literal_sequence_equal'],c['prepared_edit_inverse_restores_complete_original_ast'],c['writer_edit_inverse_restores_complete_prepared_ast'],c['all_complete_literal_payload_byte_spans_equal_original'])):
        raise RuntimeError('A full source inverse is unverified')
    original_wrapper=Path(r['wrapper']['path']);source=Path(r['public_source']['path'])
    current_wrapper=R/'tex/analytic_pole_reader.tex' if key=='analytic_pole' else original_wrapper
    current_body=R/'layout/analytic_pole_source.tex' if key=='analytic_pole' else R/r['adapter_row']['converted']
    public.update((source,original_wrapper,current_wrapper,current_body,conversion))
    for name in c['artifacts'].values():public.add(R/name)
    mp=R/'mapping'/f'{key}_full_math_mapping.json';m=json.loads(mp.read_text(encoding='utf-8'))
    portable={'schema':'portable-whole-body-explicit-math-transcription-v2','key':key,
      'source':{'filename':Path(m['source']['path']).name,'bytes':m['source']['bytes'],'sha256':m['source']['sha256']},
      'whole_body_scope':m['whole_body_scope']}
    for field in ('math_code_mappings','retained_code','display_codeblock_mappings','prose_math_mappings','notation_dictionary'):
        if field in m:portable[field]=m[field]
    portable_path=R/'public_mapping'/f'{key}_full_math_mapping.json';fresh(portable_path,dump(portable));public.add(portable_path)
    local.update((receipt,Path(r['raw_snapshot']['path']),Path(r['raw_original_ast']['path']),Path(r['public_original_ast']['path'])))
    proofs.append({'key':key,'title':r['adapter_spec']['title'],'public_source':pin(source),
      'wrapper':pin(current_wrapper),'reader_body':pin(current_body),'adapter_wrapper':pin(original_wrapper),
      'original_source_sha256':r['original_source']['sha256'],'original_source_bytes':r['original_source']['bytes'],
      'complete_source_equation_tags':r['source_equation_tags'],'math_node_counts':r['math_node_counts'],
      'typed_code_count':r['typed_code_count'],'typed_codeblock_count':r['typed_codeblock_count'],
      'typed_prose_math_count':r['typed_prose_math_count'],'retained_code_count':r['retained_code_count'],
      'adapter_spec':r['adapter_spec'],'adapter_row':r['adapter_row'],'local_exact_publication_inverse':pin(receipt),
      'portable_complete_math_mapping':pin(portable_path),
      'current_reader_route':'Use wrapper and reader_body, which include the separately documented provenance wrapping; adapter_wrapper and adapter_row retain the untouched literal-adapter baseline.',
      'source_and_proof_scope':'Complete accepted source, all paragraphs and equations, including every ordinary-prose mathematical expression, with explicit per-span typing and full inverse.'})
public.update((R/'pipeline/endpoint_source_appendix_adapter.py',R/'layout/PROVENANCE_WRAP.json'))
wrap=json.loads((R/'layout/PROVENANCE_WRAP.json').read_text(encoding='utf-8'))
if not wrap['exact_inverse_restores_every_original_TeX_byte'] or not wrap['all_256_math_payloads_preserved_exactly']:raise RuntimeError('Current reader wrapping lacks complete inverse')
for p in (R/'mapping').rglob('*'):
    if p.is_file():local.add(p)
for p in (R/'review').rglob('*'):
    if p.is_file():local.add(p)
acceptance=R/'review/REVIEW.json';review=json.loads(acceptance.read_text(encoding='utf-8'))
if review.get('status')!='accepted':raise RuntimeError('Current full independent typing review is not accepted')
def check_declared_pins(x):
    if isinstance(x,dict):
        if all(k in x for k in ('path','bytes','sha256')):
            p=Path(x['path'])
            if p.is_absolute():verify_pin(x)
        for v in x.values():check_declared_pins(v)
    elif isinstance(x,list):
        for v in x:check_declared_pins(v)
check_declared_pins(review)
for name in ('ROOT_SOURCE_ACCEPTANCE.md','PREVIOUS_PREPARED_VERSION_PINS.json'):
    local.add(R/name)
prior=json.loads((R/'PREVIOUS_PREPARED_VERSION_PINS.json').read_text(encoding='utf-8'))
for row in prior['files']:verify_pin(row)
for name in ('prepare_conversions.py','parent_pipeline_reference.py','assemble_full_mappings.py','make_later_prose_mapping.py','prepare_provenance_wrap.py','syntax_check.py','seal_analytic_pole_inputs.py'):
    p=R/name;q=R/'provenance/sealed'/name;fresh(q,p.read_bytes());local.add(q)
syntax=R/'syntax_check/SYNTAX_RECEIPT.json';syn=json.loads(syntax.read_text(encoding='utf-8'))
if syn['exit_code'] or syn['overfull_boxes'] or syn['missing_glyphs'] or syn['undefined_controls'] or syn['latex_errors']:raise RuntimeError('Current complete reader syntax check is not clean')
q=R/'provenance/sealed/SYNTAX_RECEIPT.json';fresh(q,syntax.read_bytes());local.add(q)
for p in public:
    b=p.read_bytes()
    for forbidden in (b'C:/Users/',b'C:\\Users\\',b'F:/user/',b'F:\\user\\'):
        if forbidden in b:raise RuntimeError('Private absolute path in public support '+str(p))
result={'schema':'analytic-pole-ready-complete-whole-body-typing-inputs-v2','status':'two-complete-accepted-source-conversions-sealed',
 'completed_source_count':2,'typed_prose_math_count':345,'typed_inline_code_count':46,'typed_codeblock_count':28,
 'total_converted_math_count':419,'retained_code_count':3,'proofs':proofs,
 'public_support':[pin(p) for p in sorted(public)],'local_provenance_only':[pin(p) for p in sorted(local)],
 'root_source_acceptance':pin(R/'ROOT_SOURCE_ACCEPTANCE.md'),'independent_typing_acceptance':pin(acceptance),
 'provenance_wrap':pin(R/'layout/PROVENANCE_WRAP.json'),'syntax_check':syn,
 'layout_state':'Both complete current reader routes compile under the inherited cumulative preamble with zero overfull boxes, missing glyphs, undefined controls or LaTeX errors. No final PDF visual acceptance is claimed.',
 'roundtrip_disposition':'The 28 display Math payloads retain their full boundary LF bytes in emitted TeX. The exact parser-only round-trip difference and full literal/prose inverses are bound in the independent review; the original comparison flags are not rewritten.',
 'publication_boundary':'Only public_support is selected for publication. Exact original bytes, full public-wording inverses, internal locators, coordination source acceptance, mappings with original local paths and workflow receipts remain local_provenance_only.',
 'prior_version_preserved':pin(R/'PREVIOUS_PREPARED_VERSION_PINS.json'),
 'scope':'Complete accepted mathematical source typing and exact byte/AST/literal transport. No source proof was summarized, no fixture or Lean run was replayed, no remote publication or current cumulative-master edit occurred.'}
p=R/'READY_ANALYTIC_POLE_INPUTS.json';fresh(p,dump(result))
print(json.dumps({'manifest':pin(p),'public_files':len(public),'local_files':len(local),'math_nodes':419}))
