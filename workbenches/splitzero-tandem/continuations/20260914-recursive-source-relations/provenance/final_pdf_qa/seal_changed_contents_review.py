from pathlib import Path
import hashlib, json
from datetime import datetime, timezone

wave = Path(r'workspace:\work\backpropagation_20260913')
pdf = Path(r'repository:\Split_Zero_Cohomology_and_Arithmetic_Weight_Control.pdf')
expected = '8bbd9da0d566fc5c5364a50da9b0976f9fcc21834de47822374966707b17c273'
def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()
if digest(pdf) != expected:
    raise RuntimeError('The PDF differs from the actually reviewed edition')
pages = []
for n in range(24, 33):
    p = wave / 'page_qa/final_corrected_8bbd9da0/changed_pages' / f'page_{n:04}.png'
    pages.append({'physical_page': n, 'image': str(p), 'sha256': digest(p), 'review': 'Full image opened and visually inspected by root; text and page numbers are readable, all lines remain inside margins, and no overlap or clipping observed.'})
out = wave / 'page_qa/final_changed_review_root_contents'
out.mkdir(parents=True, exist_ok=True)
receipt = {'status': 'PASS', 'utc': datetime.now(timezone.utc).isoformat(), 'pdf': str(pdf), 'pdf_sha256': expected, 'physical_pages': list(range(24, 33)), 'reviewer': '/root', 'method': 'Each of the nine full-page rendered images was opened with view_image. Pages 25 through 32 used original detail.', 'pages': pages, 'scope': 'Only these nine changed contents pages; no mathematical proof acceptance or whole-reader release acceptance is implied.'}
p = out / 'REVIEW_RECEIPT.json'
p.write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'path': str(p), 'sha256': digest(p)}))
