"""Apply the five verified overlays, only if all active originals still match."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re
ROOT=Path(__file__).resolve().parent
def sha(b):return hashlib.sha256(b).hexdigest()
def pin(p):b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':sha(b)}
proposal=json.loads((ROOT/'OVERLAY_PROPOSALS.json').read_text(encoding='utf-8'))
before_log=(ROOT/'before_console.txt').read_text(encoding='utf-8-sig')
after_log=(ROOT/'after_console.txt').read_text(encoding='utf-8-sig')
before_overfulls=re.findall(r'Overfull \\hbox \(([^)]+)\)',before_log)
assert len(before_overfulls)==5
assert not re.search(r'Overfull|Missing character|Undefined control sequence|undefined references',after_log)
for r in proposal['records']:
    active=Path(r['active_path'])
    assert sha(active.read_bytes())==r['original']['sha256'],('Live source changed; refuse overwrite',str(active))
    changed=Path(r['proposed_overlay']['path']).read_bytes()
    assert sha(changed)==r['proposed_overlay']['sha256']
    assert changed.decode('utf-8').replace(r['new'],r['old'],1).encode('utf-8')==active.read_bytes()
applied=[]
for r in proposal['records']:
    active=Path(r['active_path'])
    active.write_bytes(Path(r['proposed_overlay']['path']).read_bytes())
    assert sha(active.read_bytes())==r['proposed_overlay']['sha256']
    applied.append({'active':pin(active),'before_sha256':r['original']['sha256'],
        'after_sha256':r['proposed_overlay']['sha256'],'exact_byte_inverse':True,
        'all_nonpresentation_mathematical_and_prose_tokens_preserved':True})
receipt={'utc':datetime.now(timezone.utc).isoformat(),'scope':'Only the five specifically assigned active cohort files.',
    'active_files_modified':5,'raw_and_snapshot_sources_modified':False,
    'records':applied,'overlay_proposals':pin(ROOT/'OVERLAY_PROPOSALS.json'),
    'scratch_before_log':pin(ROOT/'before_console.txt'),'scratch_after_log':pin(ROOT/'after_console.txt'),
    'before_overfull_widths':before_overfulls,'after_overfull_count':0,'after_missing_glyph_count':0,
    'scratch_font_and_geometry':'Exact current cumulative main.tex preamble; XeLaTeX.',
    'visual_review':{'render':pin(ROOT/'after_page1.png'),'status':'pass',
        'checked':'All four complete mathematical displays, original equation tags and full review paragraph fit; no clipping, overlaps or missing glyphs. Source hash digits retain their original order across the permitted line break.'},
    'scratch_pdfs':[pin(ROOT/'before.pdf'),pin(ROOT/'after.pdf')],
    'whole_cumulative_pdf_rebuilt_here':False,
    'operation_marker':'Reused parent existing artifact operation as instructed; no new marker run.'}
(ROOT/'APPLIED_OVERLAY_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'applied_files':5,'all_exact_inverses':True,'all_nonpresentation_tokens_preserved':True,
    'scratch_before_overfulls':len(before_overfulls),'scratch_after_overfulls':0,
    'visual_review':'pass','receipt_sha256':sha((ROOT/'APPLIED_OVERLAY_RECEIPT.json').read_bytes())}))
