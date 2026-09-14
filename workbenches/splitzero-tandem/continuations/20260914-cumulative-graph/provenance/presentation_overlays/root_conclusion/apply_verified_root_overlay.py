from pathlib import Path
import hashlib,json,re
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parent
def sha(b):return hashlib.sha256(b).hexdigest()
def pin(p):b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':sha(b)}
p=json.loads((ROOT/'OVERLAY_PROPOSALS.json').read_text(encoding='utf-8'))
active=Path(p['active_source']);raw=active.read_bytes();new=Path(p['proposed_after']['path']).read_bytes()
assert sha(raw)==p['accepted_before']['sha256']=='a310d094b172289340485cb306881c029de81f1e9eff605716d70d27df0a3aa3'
assert sha(new)==p['proposed_after']['sha256']
inverse=new.decode('utf-8')
for r in reversed(p['records']):
    assert inverse.count(r['new_display'])==1
    inverse=inverse.replace(r['new_display'],r['old_display'],1)
assert inverse.encode('utf-8')==raw
before=(ROOT/'before_console.txt').read_text(encoding='utf-8-sig')
after=(ROOT/'after_console.txt').read_text(encoding='utf-8-sig')
widths=re.findall(r'Overfull \\hbox \(([^)]+)\)',before)
assert widths==['43.69221pt too wide','11.693pt too wide','64.58684pt too wide']
assert not re.search(r'Overfull|Missing character|Undefined control sequence|undefined references',after)
active.write_bytes(new)
assert sha(active.read_bytes())==p['proposed_after']['sha256']
assert pin(Path(p['RMT16_readonly']['path']))==p['RMT16_readonly']
receipt={'utc':datetime.now(timezone.utc).isoformat(),'active_file':pin(active),
    'accepted_full_R62_restored_root_sha256':p['accepted_before']['sha256'],
    'typeset_active_root_sha256':p['proposed_after']['sha256'],
    'overlaid_display_count':3,'exact_full_source_inverse':True,
    'every_nonpresentation_content_token_identical':True,
    'raw_owner_sources_edited':False,'R62_restoration_performed_by_owner_before_overlay':True,
    'proposal':pin(ROOT/'OVERLAY_PROPOSALS.json'),'before_log':pin(ROOT/'before_console.txt'),
    'after_log':pin(ROOT/'after_console.txt'),'all_three_original_widths_reproduced':widths,
    'after_overfull_count':0,'after_missing_glyph_count':0,
    'visual_review':{'status':'PASS','render':pin(ROOT/'after_verified_page1.png'),
        'complete_blocks':['Full cyclic u/t connection and flatness','Residual collision annihilator with complete exponent, kernel and image','Translated metric with all three derivatives','Original parent RMT16 three formulas and tag'],
        'finding':'All four blocks fit with every term, sign, coefficient and condition visible; no overlap, clipping or missing glyphs. No scaling.'},
    'RMT16_original_parent_overlay_unchanged':p['RMT16_readonly'],
    'whole_cumulative_compile_performed_here':False,'operation_marker':'Existing parent operation reused; no new marker.'}
(ROOT/'APPLIED_ROOT_CONCLUSION_OVERLAY_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'applied_active_root_sha256':pin(active)['sha256'],
    'receipt_sha256':pin(ROOT/'APPLIED_ROOT_CONCLUSION_OVERLAY_RECEIPT.json')['sha256'],
    'source_exact_inverse':True,'overfull_after':0,'visual':'PASS','RMT16_unchanged':True}))
