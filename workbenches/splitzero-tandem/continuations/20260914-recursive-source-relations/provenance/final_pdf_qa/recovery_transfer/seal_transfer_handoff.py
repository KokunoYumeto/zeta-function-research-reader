"""Check the completed comparison inventory and emit a compact handoff."""
from collections import Counter
from pathlib import Path
import json
import cross_page_review_transfer as transfer

root = Path(__file__).resolve().parent
result = root.parent / 'final_corrected_8bbd9da0'
report_path = result / 'CROSS_PAGE_RENDER_TRANSFER.json'
report = json.loads(report_path.read_text(encoding='utf-8'))
manifest_path = result / 'OUTPUT_MANIFEST.json'
manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
for record in manifest['files']:
    assert transfer.pin(record['path']) == record, record['path']
assert transfer.pin(report['final_pdf']['path']) == report['final_pdf']
assert transfer.pin(report['baseline_pdf']['path']) == report['baseline_pdf']
rows = report['page_records']
assert [row['page'] for row in rows] == list(range(1, 1625))
accepted = [row['page'] for row in rows if row['inherited_visual_acceptance']]
queued = [row['page'] for row in rows if row['actual_visual_review_required']]
assert accepted == report['inherited_visual_pages']
assert queued == report['changed_pages_requiring_actual_visual_review']
assert set(accepted).isdisjoint(queued)
assert set(accepted) | set(queued) == set(range(1, 1625))
assert not any(row['anomalies'] for row in rows)
assert len(accepted) == 1590 and len(queued) == 34
for row in rows:
    if not row['inherited_visual_acceptance']:
        continue
    assert row['matched_baseline_page'] not in [811, 1137]
    if row['transfer_kind'] == 'exact_body_and_furniture_with_proved_numeric_footer_substitution':
        success = [c for c in row['candidate_checks'] if c.get('footer_substitution', {}).get('accepted')]
        assert len(success) == 1
        proof = success[0]['footer_substitution']
        assert proof['outside_mask_exactly_equal'] and proof['replacement_number_pixels_equal_reviewed_reference']
        assert proof['after_number'] == transfer.expected_number(row['page'])
        assert proof['reviewed_number_reference_page'] == row['page']
paths = [report_path, result / 'CHANGED_PAGE_VISUAL_QUEUE.json', manifest_path,
         root / 'cross_page_review_transfer.py', root / 'primitive_checks' / 'PRIMITIVE_CHECKS.json',
         root / 'code_review' / 'EXACT_SCRIPT_AND_RECEIPT_REVIEW.json']
handoff = {'status': 'PASS for complete exact transfer and inventory; fresh review of all 34 queued pages required',
           'final_pdf': report['final_pdf'], 'baseline_pdf': report['baseline_pdf'],
           'final_pages': 1624, 'exact_full_page_matches': 1124,
           'exact_body_and_numeric_footer_transfers': 466, 'inherited_visual_pages': 1590,
           'queue': queued, 'current_geometry_or_glyph_anomalies': [],
           'inventory_files_checked': len(manifest['files']),
           'output_inventory_all_hashes_match': True, 'all_final_pages_accounted_exactly_once': True,
           'evidence': [transfer.pin(path) for path in paths],
           'whole_document_visual_acceptance': False,
           'next_action': 'Combine every queued final page with its actual fresh visual-inspection receipt. Parent has already reviewed final pages 811, 1136, 1137, 1138; this script does not assert or synthesize that visual acceptance.'}
output = root / 'COMPLETED_TRANSFER_HANDOFF.json'
assert not output.exists()
transfer.write_json(output, handoff)
print(json.dumps({'handoff': transfer.pin(output), 'inventory_files_checked': len(manifest['files']),
                  'final_pages': 1624, 'inherited': 1590, 'queued': 34}, indent=2))
