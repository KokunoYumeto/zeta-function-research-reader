"""Bind the repaired portable build to the historical accepted source audit.

This is additive. Earlier receipts continue to describe their original bytes.
PDF visual acceptance is explicitly outside this program's source audit.
"""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import hashlib, json, re, importlib.util

HERE=Path(__file__).resolve().parent; WAVE=HERE.parent; BASE=WAVE.parents[1]
STAGE=WAVE/'cumulative_source_v1'
DELIVERY=BASE/'output/Split_Zero_Recursive_Integration_2026-09-13/repository'
HISTORY=HERE/'history/pre_conversion_fidelity_20260913'
PREBUILD=WAVE/'page_qa/pre_final_converter_build'
def readj(p): return json.loads(p.read_text(encoding='utf-8'))
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def pin(p): return {'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size}
spec=importlib.util.spec_from_file_location('audit_inclusion',HERE/'audit_inclusion.py')
graph_module=importlib.util.module_from_spec(spec); spec.loader.exec_module(graph_module)

previous=readj(HISTORY/'FINAL_AUDIT_RECEIPT.json')
oldgraph=readj(HISTORY/'FINAL_ASSEMBLY_INCLUSION_GRAPH.json')
oldpins=readj(PREBUILD/'delivery/provenance/CURRENT_COMPILED_SOURCE_PINS.json')['files']
assert len(oldpins)==240
assert set(oldpins)==set(oldgraph['files'])|set(previous['compiler_only_inputs'])
for rel,v in oldgraph['files'].items(): assert oldpins[rel]['sha256']==v['sha256'],rel
oldbuild=readj(PREBUILD/'delivery/build/CURRENT_BUILD_RECEIPT.json')
previous_delivery=readj(HISTORY/'DELIVERED_SOURCE_AND_PDF_CHECK.json')
assert oldbuild['compiled_sources']==oldpins
assert oldbuild['pdf_sha256']==previous_delivery['pdf']['sha256']
assert sha(PREBUILD/'delivery'/oldbuild['pdf'])==previous_delivery['pdf']['sha256']
assert previous_delivery['stage_audit_receipt']['sha256']==sha(HISTORY/'FINAL_AUDIT_RECEIPT.json')

replay=readj(HERE/'CONVERSION_NINETEEN_INDEPENDENT_CHECK.json')
assert replay['all_active_stage_and_delivery_bytes_match']
correction_outputs={r['path']:r['after']['sha256'] for r in replay['file_checks']}
tcl=readj(WAVE/'page_qa/tcl2_display_repair/TCL2_REVERSIBLE_DISPLAY_MAP.json')
correction_outputs['tex/cohorts/cf/49_TP.tex']=tcl['after_sha256']
assert len(correction_outputs)==4

current_graph=graph_module.graph(STAGE)
delivered_graph=graph_module.graph(DELIVERY)
assert not current_graph['missing'] and not delivered_graph['missing']
assert set(current_graph['files'])==set(oldgraph['files'])==set(delivered_graph['files'])
assert [(r['from'],r['to']) for r in current_graph['edges']]==[(r['from'],r['to']) for r in oldgraph['edges']]
assert current_graph['files']==delivered_graph['files']
current_pins=readj(STAGE/'provenance/CURRENT_COMPILED_SOURCE_PINS.json')['files']
assert set(current_pins)==set(oldpins)
assert current_pins==readj(DELIVERY/'provenance/CURRENT_COMPILED_SOURCE_PINS.json')['files']
changed=[]
for rel,v in current_pins.items():
    assert sha(STAGE/rel)==sha(DELIVERY/rel)==v['sha256'],rel
    if v['sha256']!=oldpins[rel]['sha256']:
        assert correction_outputs.get(rel)==v['sha256'],rel
        changed.append({'path':rel,'before_sha256':oldpins[rel]['sha256'],'after_sha256':v['sha256']})
assert {r['path'] for r in changed}==set(correction_outputs)

builds=[]
for root in (STAGE,DELIVERY):
    p=root/'build/CURRENT_BUILD_RECEIPT.json'; build=readj(p)
    assert build['compiled_sources']==current_pins
    assert all(not v for v in build['warnings'].values())
    assert sha(root/build['pdf'])==build['pdf_sha256']
    if root==DELIVERY: assert not build['source_preparation_replayed']
    builds.append({'root':str(root),'build_receipt':pin(p),'pdf':pin(root/build['pdf']),
                   'pages_from_build_receipt':build['pages'],
                   'warning_counts':{k:len(v) for k,v in build['warnings'].items()},
                   'all_compiled_sources_match':True})

expected=readj(HISTORY/'EXPECTED_FINAL_ACTIVE_PATCHES.json')['patches']
patchchecks=[]
for r in expected:
    rel=r['reader_path']; actual=sha(STAGE/rel)
    expected_hash=correction_outputs.get(rel,r['sha256'])
    assert actual==expected_hash,rel
    required=r.get('include_required',True)
    assert not required or rel in current_graph['files'],rel
    patchchecks.append({'path':rel,'sha256':actual,'included':rel in current_graph['files'],
                       'source_scope_unchanged':rel not in correction_outputs,'pass':True})
assert len(patchchecks)==41

# Parse every active href with balanced braces; compare with the earlier exact
# inventory after removing exactly the three proven parser-created links.
def group(text,start):
    assert text[start]=='{'
    level=1; i=start+1
    while i<len(text):
        if text[i]=='\\': i+=2; continue
        if text[i]=='{': level+=1
        elif text[i]=='}':
            level-=1
            if level==0: return text[start+1:i],i+1
        i+=1
    raise AssertionError('Unbalanced TeX group')

links=[]; footnotes=[]; superscripts=[]
for rel in current_graph['files']:
    text=(STAGE/rel).read_text(encoding='utf-8-sig')
    for m in re.finditer(r'\\href\s*\{',text):
        target,end=group(text,text.find('{',m.start()))
        while text[end].isspace(): end+=1
        display,end=group(text,end)
        links.append((rel,target,display))
    if re.search(r'\\footnote\b',text): footnotes.append(rel)
    if re.search(r'\\textsuperscript\b',text): superscripts.append(rel)
inventory=readj(WAVE/'cohort_staging/ledger_exponent_correction/independent_scan/LINK_AND_LOCAL_PROPOSALS.json')
original_links=[(r['path'],r['target'],r['display']) for r in inventory['links'] if r['classification']!='confirmed_mathematical_link_parser_corruption']
assert Counter(links)==Counter(original_links)
assert len(links)==82 and not footnotes and not superscripts

baseline=readj(HERE/'HISTORICAL_821_BASELINE_PINS.json')
for rel,v in baseline['files'].items(): assert sha(Path(baseline['root'])/rel)==v['sha256'],rel
assert len(baseline['files'])==4923

result={
 'status':'PASS: final converted sources and portable PDF independently bound to prior mathematical source audit',
 'utc':datetime.now(timezone.utc).isoformat(),
 'scope':'Four changed compiler inputs are precisely the accepted conversion/layout repairs. All other236 compiled inputs retain the previously accepted bytes; all239 TeX routes and238 input edges remain. This is source/conversion/build acceptance; rendered-page acceptance remains separately required.',
 'prior_audit':pin(HISTORY/'FINAL_AUDIT_RECEIPT.json'),
 'prior_pdf_bound_to_preserved_build':True,'compiler_sources_checked':240,
 'unchanged_compiler_sources':236,'exact_changed_sources':changed,
 'recursive_tex_files':len(current_graph['files']),'recursive_input_edges':len(current_graph['edges']),
 'accepted_paths_checked':patchchecks,'complete_conclusion_blocks_previously_checked':22,
 'historical_source_files_checked_unchanged':4923,
 'remaining_href_commands':82,'remaining_href_commands_exactly_preserved':True,
 'remaining_footnotes':footnotes,'remaining_textsuperscripts':superscripts,
 'builds':builds,
 'evidence':[pin(HERE/'CONVERSION_NINETEEN_INDEPENDENT_CHECK.json'),
             pin(WAVE/'page_qa/tcl2_display_repair/TCL2_REVERSIBLE_DISPLAY_MAP.json'),
             pin(HISTORY/'CONCLUSION_COMPLETE_BLOCK_TRANSFER_CHECK.json'),
             pin(HERE/'READABLE_LEDGER_CHECK.json')],
 'visual_acceptance':'separately required; no rendered-page claim in this receipt'
}
(HERE/'FINAL_CONVERTED_SOURCE_AND_PDF_BINDING.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':result['status'],'changed_inputs':len(changed),'unchanged_inputs':236,'pages':[b['pages_from_build_receipt'] for b in builds],'sha256':sha(HERE/'FINAL_CONVERTED_SOURCE_AND_PDF_BINDING.json')},indent=2))
