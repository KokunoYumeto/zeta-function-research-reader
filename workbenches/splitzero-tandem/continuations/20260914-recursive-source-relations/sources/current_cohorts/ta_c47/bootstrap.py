from pathlib import Path
import json, hashlib

ROOT=Path(__file__).resolve().parent
WORK=ROOT.parents[2]
SESSION=Path('local:user-profile/.codex/sessions/2026/09/13/rollout-2026-09-13T21-37-09-01a09c46-04d9-7a03-9a9a-c4b985513cab.jsonl')
turns=[]
for line in SESSION.read_text(encoding='utf-8').splitlines():
    j=json.loads(line)
    if j.get('type')=='response_item' and j.get('payload',{}).get('role')=='user':
        p=j['payload']; t='\n'.join(c.get('text','') for c in p.get('content',[]) if c.get('type') in ('input_text','text'))
        turns.append((j.get('timestamp',''),t))
(ROOT/'USER_INPUTS_VERBATIM.md').write_text('# User inputs retained from session JSONL\n\n'+''.join('## '+ts+'\n\n'+t+'\n\n' for ts,t in turns),encoding='utf-8')
(ROOT/'LOGBOOK.md').write_text('# TA and C47 full-body staging\n\nAssignment: own only this directory; snapshot original TA1–24 plus full review and certified47 repository; prepare complete namespaced bodies with reversible transformations; do not build PDFs or modify originals.\n\nRead the session JSONL once to retain all available user inputs verbatim. New precise results must propagate backwards and forwards, with all provenance retained. This staging establishes full source inputs; it does not claim every historical mathematical body was revised.\n\nLocated C47 exact repository at output/Tau_Theta_Hankel_Certification_2026-09-13/repository. Its README identifies five main plus42 support pages and all ten complete proof bodies. Located theta_admitted_cumulative_conversion_20260913 and v22 addendum inventory for TA.\n',encoding='utf-8')
inv=WORK/'cumulative_actual_tau_extended_inventory_20260913_v22_addendum.json'
j=json.loads(inv.read_text(encoding='utf-8'))
def scan(o,path='root'):
    if isinstance(o,dict):
        s=json.dumps(o,ensure_ascii=False)
        if len(s)<25000 and any(x in s for x in ['theta_admitted','TA1','TA24']):
            print(path,s[:15000])
            return
        for k,v in o.items(): scan(v,path+'.'+k)
    elif isinstance(o,list):
        for i,v in enumerate(o):scan(v,path+f'[{i}]')
scan(j)
