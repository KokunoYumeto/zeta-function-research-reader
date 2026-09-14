"""Apply proposals only to owned scratch copies and prove their exact inverse."""
from pathlib import Path
from collections import defaultdict
from datetime import datetime,timezone
import json,hashlib,re

OUT=Path(__file__).resolve().parent
BASE=Path('workspace:')
def readj(p): return json.loads(p.read_text(encoding='utf-8'))
def sha(raw): return hashlib.sha256(raw).hexdigest()

ledger=readj(OUT/'originals/CLASSIFICATION_AND_PROPOSALS.json')
local=readj(OUT/'LINK_AND_LOCAL_PROPOSALS.json')
proposals=[]
for p in ledger['superscript_proposals']:
    proposals.append({'id':p['id'],'path':p['active_path'],'old':p['standalone_old_tex_phrase'],
                      'new':p['proposed_inline_math'],'source_path':p['packaged_path'],
                      'source_line':p['source_line'],'source_phrase':p['exact_original_phrase'],
                      'source_sha256':p['source_sha256']})
for p in ledger.get('formula_link_proposals',[]):
    proposals.append({'id':p['id'],'path':p['active_path'],'old':p['standalone_old_tex_phrase'],
                      'new':p['proposed_inline_math'],'source_path':p['packaged_path'],
                      'source_line':p['source_line'],'source_phrase':p['exact_original_phrase'],
                      'source_sha256':p['source_sha256']})
for p in local['confirmed_conversion_proposals']:
    proposals.append({'id':p['id'],'path':p['active_relative_path'],'old':p['old_tex'],
                      'new':p['proposed_tex'],'source_path':p['source']['path'],
                      'source_line':p['source_line'],'source_phrase':p['source_exact_phrase'],
                      'source_sha256':p['source']['sha256']})
if len(proposals)!=19: raise ValueError(('Expected nineteen companion proposals',len(proposals),list(ledger)))

groups=defaultdict(list)
for p in proposals:
    source_path=Path(p['source_path'])
    if not source_path.is_absolute():source_path=BASE/source_path
    raw=source_path.read_bytes()
    if sha(raw)!=p['source_sha256']: raise ValueError(('Source hash changed',p['id']))
    source_line=raw.decode('utf-8-sig').splitlines()[p['source_line']-1]
    if p['source_phrase'] not in source_line:raise ValueError(('Exact source phrase missing',p['id']))
    groups[p['path']].append(p)

records=[]
for path,grouped in groups.items():
    source=OUT/'reviewed_active_inputs'/path
    raw=source.read_bytes()
    before=raw.decode('utf-8')
    unique={}
    for p in grouped:
        key=(p['old'],p['new'])
        if key not in unique:unique[key]=[]
        unique[key].append(p['id'])
    edits=[]
    for (old,new),ids in unique.items():
        matches=list(re.finditer(re.escape(old),before))
        if len(matches)!=len(ids):raise ValueError(('Occurrence mismatch',ids,len(matches)))
        for i,m in enumerate(matches):
            edits.append({'id':ids[i],'old_start':m.start(),'old_end':m.end(),'old':old,'new':new})
    edits.sort(key=lambda p:p['old_start'])
    for a,b in zip(edits,edits[1:]):
        if a['old_end']>b['old_start']:raise ValueError(('Overlapping replacements',a['id'],b['id']))
    pieces=[]
    old_cursor=0
    new_cursor=0
    for edit in edits:
        prefix=before[old_cursor:edit['old_start']]
        pieces.extend((prefix,edit['new']))
        edit['new_start']=new_cursor+len(prefix)
        edit['new_end']=edit['new_start']+len(edit['new'])
        new_cursor=edit['new_end']
        old_cursor=edit['old_end']
    pieces.append(before[old_cursor:])
    after=''.join(pieces)
    restored=after
    for edit in reversed(edits):
        if restored[edit['new_start']:edit['new_end']]!=edit['new']:raise ValueError('Inverse span mismatch')
        restored=restored[:edit['new_start']]+edit['old']+restored[edit['new_end']:]
    assert restored.encode('utf-8')==raw
    assert '\\textsuperscript' not in after
    assert '\\footnote' not in after
    assert not re.search(r'\\href\{(?:x|k\+1)\}',after)
    candidate=OUT/'proposed_scratch_outputs'/path
    candidate.parent.mkdir(parents=True,exist_ok=True)
    candidate.write_bytes(after.encode('utf-8'))
    records.append({'path':path,'reviewed_input_sha256':sha(raw),'scratch_output_sha256':sha(after.encode('utf-8')),
                    'original_bytes':len(raw),'scratch_bytes':len(after.encode('utf-8')),'edit_count':len(edits),
                    'all_untouched_spans_preserved':True,'exact_inverse_bytes':True,
                    'raw_caret_bracket_count_before':before.count('^['),'raw_caret_bracket_count_after':after.count('^['),
                    'textsuperscript_after':after.count('\\textsuperscript'),'footnote_after':after.count('\\footnote'),
                    'formula_hyperlinks_after':len(re.findall(r'\\href\{(?:x|k\+1)\}',after)),
                    'edits':edits})

result={'created_utc':datetime.now(timezone.utc).isoformat(),'scope':'Scratch-only exact source-mapped replay of all nineteen remaining companion corrections. The two BF12 footnotes had already been corrected by the parent before these reviewed inputs were captured.',
        'original_source_hashes_and_exact_phrases_verified':True,'proposal_count':len(proposals),
        'edit_count':sum(r['edit_count'] for r in records),'file_count':len(records),'files':records,
        'active_source_edits_performed':False,'pdf_built':False,'original_source_modified':False}
(OUT/'PROPOSAL_REPLAY_RECEIPT.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:result[k] for k in ['proposal_count','edit_count','file_count','original_source_hashes_and_exact_phrases_verified']},indent=2))
print('receipt_sha256',sha((OUT/'PROPOSAL_REPLAY_RECEIPT.json').read_bytes()))
