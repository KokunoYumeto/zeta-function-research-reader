from pathlib import Path
import hashlib
import json
import re
import subprocess
import sys

sys.stdout.reconfigure(encoding='utf-8')
ROOT=Path('workspace:')
OUT=Path(__file__).resolve().parent
LEDGER=ROOT/'work/backpropagation_20260913/cohort_staging/snapshots/transcript/ledger_publication'
manifest=json.loads((LEDGER/'sources_manifest.json').read_text(encoding='utf-8-sig'))

def flat(x):
    if isinstance(x,list):return ''.join(map(flat,x))
    if not isinstance(x,dict):return ''
    if x.get('t')=='Str':return x['c']
    if x.get('t') in ('Space','SoftBreak','LineBreak'):return ' '
    if x.get('t') in ('Code','Math'):return x['c'][-1]
    return flat(x.get('c',[]))

def nodes(x):
    if isinstance(x,list):
        for item in x:yield from nodes(item)
    elif isinstance(x,dict):
        if x.get('t') in ('Note','Superscript','Link'):yield x
        yield from nodes(x.get('c',[]))

records=[]
for m in manifest:
    path=LEDGER/m['packaged_path']
    source=path.read_text(encoding='utf-8-sig')
    cmd=['pandoc',str(path),'--from=markdown+tex_math_single_backslash','--to=json']
    run=subprocess.run(cmd,capture_output=True,check=True)
    ast=json.loads(run.stdout)
    selected=[]
    used={}
    for n in nodes(ast['blocks']):
        if n['t']=='Link' and n['c'][2][0]!='k+1':continue
        value=flat(n['c'][1]) if n['t']=='Link' else flat(n)
        token=('['+value+']('+n['c'][2][0]+')') if n['t']=='Link' else ('^['+value+']' if n['t']=='Note' else '^'+value+'^')
        matches=[]
        for i,line in enumerate(source.splitlines(),1):
            start=0
            while (at:=line.find(token,start))>=0:
                matches.append({'line':i,'column':at+1,'exact_raw_token':token,'exact_raw_line':line})
                start=at+1
        key=(n['t'],value)
        ordinal=used.get(key,0)
        used[key]=ordinal+1
        assert ordinal<len(matches),(m['slug'],n['t'],value,ordinal)
        selected.append({'node_type':n['t'],'contents':value,'raw_matches':[matches[ordinal]],'ast':n})
    rec={'slug':m['slug'],'packaged_path':path.relative_to(ROOT).as_posix(),'original_path':m['original_relative_path'],'source_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'command':cmd,'note_count':sum(x['node_type']=='Note' for x in selected),'superscript_count':sum(x['node_type']=='Superscript' for x in selected),'formula_link_count':sum(x['node_type']=='Link' for x in selected),'selected_nodes':selected}
    records.append(rec)
    if selected:
        print(m['slug'],rec['note_count'],rec['superscript_count'])
        for x in selected:
            print(x['node_type'],repr(x['contents']))
            for loc in x['raw_matches']:print(loc['line'],loc['column'],loc['exact_raw_line'])

version=subprocess.run(['pandoc','--version'],capture_output=True,check=True).stdout.decode('utf-8')
extensions=subprocess.run(['pandoc','--list-extensions=markdown'],capture_output=True,check=True).stdout.decode('utf-8')
receipt={'pandoc_version':version.splitlines()[0],'relevant_enabled_extensions':[s for s in extensions.splitlines() if any(t in s for t in ['footnote','superscript','tex_math_single'])],'records':records,'summary':{'source_files':len(records),'notes':sum(r['note_count'] for r in records),'superscripts':sum(r['superscript_count'] for r in records),'formula_links_with_target_k_plus_one':sum(r['formula_link_count'] for r in records)}}
(OUT/'PARSER_PROBE.json').write_text(json.dumps(receipt,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps(receipt['summary']))
