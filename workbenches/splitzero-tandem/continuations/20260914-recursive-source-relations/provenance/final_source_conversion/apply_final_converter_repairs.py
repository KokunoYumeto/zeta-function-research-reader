"""Apply the complete independently replayed original-source corrections."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil

W=Path(__file__).resolve().parent
Q=W/'cohort_staging/ledger_exponent_correction/independent_scan'
OUT=W/'cohort_staging/ledger_exponent_correction/final_application'
BASES={'stage':W/'cumulative_source_v1', 'delivery':W.parents[1]/'output/Split_Zero_Recursive_Integration_2026-09-13/repository'}
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
receipt=json.loads((Q/'PROPOSAL_REPLAY_RECEIPT.json').read_text(encoding='utf-8'))
assert receipt['edit_count']==19 and receipt['file_count']==3
assert not OUT.exists(), 'Preserve prior application evidence.'
work=[]
for role,base in BASES.items():
    for row in receipt['files']:
        current=base/row['path']; replacement=Q/'proposed_scratch_outputs'/row['path']
        assert sha(current)==row['reviewed_input_sha256'],str(current)
        assert sha(replacement)==row['scratch_output_sha256'],str(replacement)
        before=current.read_bytes().decode('utf-8'); after=replacement.read_bytes().decode('utf-8')
        restored=after
        for edit in reversed(row['edits']):
            assert restored[edit['new_start']:edit['new_end']]==edit['new']
            restored=restored[:edit['new_start']]+edit['old']+restored[edit['new_end']:]
        assert restored.encode('utf-8')==current.read_bytes()
        work.append((role,base,row,current,replacement))
OUT.mkdir(parents=True)
records=[]
for role,base,row,current,replacement in work:
    backup=OUT/'before'/role/row['path']; backup.parent.mkdir(parents=True,exist_ok=True)
    shutil.copy2(current,backup); shutil.copy2(replacement,current)
    assert sha(current)==row['scratch_output_sha256']
    records.append({'location':role,'path':row['path'],'before_sha256':sha(backup),'after_sha256':sha(current),
                    'edit_count':row['edit_count'],'all_untouched_spans_preserved':True,'inverse_byte_exact':True})
result={'created_utc':datetime.now(timezone.utc).isoformat(),'status':'applied original-source corrections',
        'reviewed_proposal_receipt':{'path':str(Q/'PROPOSAL_REPLAY_RECEIPT.json'),'sha256':sha(Q/'PROPOSAL_REPLAY_RECEIPT.json')},
        'per_repository_edits':19,'repositories':2,'records':records,'historical_sources_modified':False}
(OUT/'APPLIED_FINAL_CONVERTER_CORRECTIONS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
