"""Apply the reviewed tocdepth state restoration and preserve build outputs."""
from pathlib import Path
import json, shutil
from prepare_successor import STAGE,SUPPORT,BASE,sha,row,save,preserve

revision=STAGE/'history/source_assembly_revisions/tocdepth_restore'
relative='tex/current_phase_graph_successor.tex'
wrapper=STAGE/relative
old=wrapper.read_text(encoding='utf-8')
before='\\begingroup\n\\input{'
after='\\begingroup\n\\edef\\GraphVTwoSavedTocDepth{\\number\\value{tocdepth}}\n\\input{'
close_before='}\n\\endgroup\n'
close_after='}\n\\setcounter{tocdepth}{\\GraphVTwoSavedTocDepth}\n\\endgroup\n'
if old.count(before)!=38 or old.count(close_before)!=38:
    raise RuntimeError('Expected exactly38 unmodified full-body groups.')
new=old.replace(before,after).replace(close_before,close_after)
if new.replace(after,before).replace(close_after,close_before)!=old:
    raise RuntimeError('Tocdepth state-wrapper transport is not reversible.')
for name in [relative,'provenance/ASSEMBLED_SOURCE_EXPECTATIONS.json','provenance/SOURCE_BUILD_READINESS.json','CURRENT_SOURCE_MANIFEST.json']:
    target=revision/name; target.parent.mkdir(parents=True,exist_ok=True)
    shutil.copy2(STAGE/name,target)
wrapper.write_text(new,encoding='utf-8',newline='\n')
expected_path=STAGE/'provenance/ASSEMBLED_SOURCE_EXPECTATIONS.json'
expected=json.loads(expected_path.read_text(encoding='utf-8'))
expected['files'][relative]=row(wrapper)
save(expected_path,expected)
save(STAGE/'provenance/TOCDEPTH_STATE_TRANSPORT.json',{
    'status':'exact_reversible_wrapper_state_restore',
    'source_contract':'source_assembly_tools/contract_review/article_transport_contract.json',
    'target':relative,'before':row(revision/relative),'after':row(wrapper),
    'operations':[{'old':before,'new':after,'count':38},{'old':close_before,'new':close_after,'count':38}],
    'full_inverse_replay':True,'body_edits':0,
    'reason':'The original dep08 setcounter(tocdepth,3) has global state; restore the entry value after each grouped body.'})
for source in (SUPPORT/'contract_review').rglob('*'):
    if source.is_file() and source.suffix.lower() in ['.json','.md','.py']:
        target=STAGE/'provenance/source_assembly_tools/contract_review'/source.relative_to(SUPPORT/'contract_review')
        target.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(source,target)
generated=[]
for source in (BASE/'build').glob('*'):
    if source.is_file() and (source.name.startswith('reader.') or source.name.startswith('current-xelatex-') or source.name=='CURRENT_BUILD_RECEIPT.json'):
        relative=source.relative_to(BASE).as_posix(); preserve(relative); generated.append(relative)
save(STAGE/'provenance/PRE_BUILD_GENERATED_HISTORY.json',{'preserved':generated,'count':len(generated),'baseline_mutations':0})
current_path=STAGE/'CURRENT_SOURCE_MANIFEST.json'
current=json.loads(current_path.read_text(encoding='utf-8'))
current['source_expectations']={'path':'provenance/ASSEMBLED_SOURCE_EXPECTATIONS.json',**row(expected_path)}
save(current_path,current)
ready_path=STAGE/'provenance/SOURCE_BUILD_READINESS.json'
ready=json.loads(ready_path.read_text(encoding='utf-8'))
ready['expected_source_manifest_sha256']=sha(expected_path)
ready['current_source_manifest_sha256']=sha(current_path)
ready['tocdepth_state_transport_sha256']=sha(STAGE/'provenance/TOCDEPTH_STATE_TRANSPORT.json')
save(ready_path,ready)
print(json.dumps({'status':'ready_for_guarded_build','expected_source_manifest_sha256':sha(expected_path),'preserved_build_outputs':len(generated)}))
