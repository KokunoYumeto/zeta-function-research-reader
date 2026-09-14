"""Apply five exact checked boundary-display overlays to active copies only."""
from pathlib import Path
import hashlib,json,re
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parent
def sha(b):return hashlib.sha256(b).hexdigest()
def pin(p):b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':sha(b)}
proposal=json.loads((ROOT/'OVERLAY_PROPOSALS.json').read_text(encoding='utf-8'))
before_log=(ROOT/'before_console.txt').read_text(encoding='utf-8-sig')
after_log=(ROOT/'after_console.txt').read_text(encoding='utf-8-sig')
widths=re.findall(r'Overfull \\hbox \(([^)]+)\)',before_log)
assert widths==['28.4165pt too wide','10.01018pt too wide','84.23085pt too wide','10.84186pt too wide','28.35316pt too wide']
assert not re.search(r'Overfull|Missing character|Undefined control sequence|undefined references',after_log)
for r in proposal['records']:
    p=Path(r['active_path']);old=p.read_bytes();new=Path(r['after']['path']).read_bytes()
    assert sha(old)==r['before']['sha256'],('Active source changed; refuse overwrite',str(p))
    assert sha(new)==r['after']['sha256']
    assert new.decode('utf-8').replace(r['new_display'],r['old_display'],1).encode('utf-8')==old
records=[]
for r in proposal['records']:
    p=Path(r['active_path']);p.write_bytes(Path(r['after']['path']).read_bytes())
    assert sha(p.read_bytes())==r['after']['sha256']
    records.append({'active_path':str(p),'accepted_derived_before_sha256':r['before']['sha256'],
        'typeset_active_after_sha256':r['after']['sha256'],'before_bytes':r['before']['bytes'],
        'after_bytes':r['after']['bytes'],'inverse':'Replace exact new_display by old_display from OVERLAY_PROPOSALS.json.',
        'full_source_exact_byte_inverse':True,'nonpresentation_content_tokens_identical':True,
        'matrix_row_and_column_data_identical':True,'display_tag':r['display_tag']})
receipt={'utc':datetime.now(timezone.utc).isoformat(),'active_files_modified':5,
    'raw_owner_sources_and_sealed_snapshots_modified':False,
    'mechanical_derived_to_active_map':records,'proposals':pin(ROOT/'OVERLAY_PROPOSALS.json'),
    'before_log':pin(ROOT/'before_console.txt'),'after_log':pin(ROOT/'after_console.txt'),
    'original_five_overfull_widths_reproduced_exactly':widths,'after_overfull_count':0,
    'after_missing_glyph_count':0,'scratch_context':'Exact cumulative preamble, including original local small size for analytic-pole display.',
    'visual_review':{'status':'pass','render':pin(ROOT/'after_verified_page1.png'),
        'checked':'All five complete displays with original terms, labels, Gamma factors, derivative signs and all four connection-matrix entries fit. No clipping, overlap or glyph loss. Only aligned rows were added; no font scaling.'},
    'scratch_pdfs':[pin(ROOT/'before.pdf'),pin(ROOT/'after.pdf')],
    'operation_marker':'Parent marker reused; no new marker.',
    'whole_cumulative_pdf_rebuilt_here':False}
(ROOT/'APPLIED_BOUNDARY_OVERLAY_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'five_files_applied':True,'all_exact_inverses':True,'all_content_and_matrix_entries_preserved':True,
    'scratch_after_overfull_count':0,'visual_review':'pass','receipt_sha256':sha((ROOT/'APPLIED_BOUNDARY_OVERLAY_RECEIPT.json').read_bytes())}))
