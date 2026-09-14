from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

wave = Path(__file__).resolve().parents[1]
qa = wave / 'page_qa'
def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def pin(p):
    p = Path(p)
    return {'path': str(p), 'bytes': p.stat().st_size, 'sha256': sha(p)}
def check(test, message):
    if not test:
        raise RuntimeError(message)
def read(p):
    return json.loads(Path(p).read_text(encoding='utf-8-sig'))
pdf = wave.parents[1] / 'output/Split_Zero_Recursive_Integration_2026-09-13/repository/Split_Zero_Cohomology_and_Arithmetic_Weight_Control.pdf'
expected = '8bbd9da0d566fc5c5364a50da9b0976f9fcc21834de47822374966707b17c273'
check(sha(pdf) == expected, 'Final PDF differs from actually reviewed edition')
root_pages = [811,1137,1138,1185,1187,1189,1190,1192,1193,1194,1195,1207,1220,1224,1251,1353]
reviewdir = qa / 'final_changed_review_root_remaining'
reviewdir.mkdir(exist_ok=True)
receipt = {'status': 'PASS', 'reviewer': '/root', 'utc': datetime.now(timezone.utc).isoformat(), 'pdf_sha256': expected, 'physical_pages': root_pages, 'scope': 'Each listed entire final PNG was opened through view_image at original detail. All formulas, signs, restored superscripts, headers and footers are visible; no collision or clipping found. Historical literal plain-text formula passages remain as supplied.', 'pages': []}
for n in root_pages:
    p = qa / 'final_corrected_8bbd9da0/changed_pages' / f'page_{n:04}.png'
    receipt['pages'].append({'physical_page': n, 'image': str(p), 'sha256': sha(p), 'actually_viewed_full_page': True})
remaining = reviewdir / 'REVIEW_RECEIPT.json'
check(not remaining.exists(), 'Preserve earlier root receipt')
remaining.write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8')
handoff_path = qa / 'recovery_transfer/COMPLETED_TRANSFER_HANDOFF.json'
handoff = read(handoff_path)
check(handoff['final_pdf'] == pin(pdf), 'Transfer PDF pin differs')
for row in handoff['evidence']:
    check(pin(row['path']) == row, 'Transfer evidence changed: ' + row['path'])
transfer = read(qa / 'final_corrected_8bbd9da0/CROSS_PAGE_RENDER_TRANSFER.json')
check([r['page'] for r in transfer['page_records']] == list(range(1,1625)), 'Page membership differs')
inherited = set(transfer['inherited_visual_pages'])
changed = set(transfer['changed_pages_requiring_actual_visual_review'])
check(len(inherited) == 1590 and len(changed) == 34 and inherited.isdisjoint(changed) and inherited | changed == set(range(1,1625)), 'Full coverage fails')
check(not any(r['anomalies'] for r in transfer['page_records']), 'Unresolved render anomaly')
reviews = [qa / 'final_changed_review_root_contents/REVIEW_RECEIPT.json', qa / 'final_changed_review_ledger_1134_1151/REVIEW_RECEIPT.json', remaining]
covered = set()
for p in reviews:
    r = read(p)
    check(r['status'] == 'PASS' and r['pdf_sha256'] == expected, 'Unaccepted changed page review')
    for item in r['pages']:
        image = item.get('image', item.get('png_path'))
        digest = item.get('sha256', item.get('png_sha256'))
        check(sha(image) == digest, 'Reviewed image changed')
        covered.add(item['physical_page'])
check(covered == changed, 'Fresh review does not cover exact changed queue')
result = {'status': 'PASS', 'utc': datetime.now(timezone.utc).isoformat(), 'pdf': str(pdf), 'pdf_sha256': expected, 'final_pages': 1624, 'inherited_visual_pages': 1590, 'exact_full_page_matches': 1124, 'exact_body_and_numeric_footer_transfers': 466, 'freshly_inspected_pages': sorted(covered), 'freshly_inspected_page_count': len(covered), 'all_pages_covered': True, 'transfer_receipt': pin(handoff_path), 'actual_changed_page_reviews': [pin(p) for p in reviews], 'scope': 'Complete final rendered-page layout and visible formula inspection. Inherited pages have exact full pixels or exact body/header pixels and separately proved numeric-footer substitution from previously actually inspected pages. Mathematical proof and source-conversion acceptance remain separate.'}
target = qa / 'FINAL_PDF_VISUAL_ACCEPTANCE.json'
check(not target.exists(), 'Preserve earlier final QA receipt')
target.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print(json.dumps(pin(target)))
