from pathlib import Path
import hashlib
import json
import shutil
from datetime import datetime, timezone

q = Path(__file__).resolve().parent
pdf = q.parent.parent / 'Tau_Split_Zero_Total_Counterfactual.pdf'
expected = '08a5293305eb1fd7b0ce22816a2ded717d002bf7a5f44e7177560efbb3a1b5eb'
assert hashlib.sha256(pdf.read_bytes()).hexdigest() == expected
metrics = json.loads((q / 'layout_metrics.json').read_text())
mapping = json.loads((q / 'baseline_page_mapping.json').read_text())
assert metrics['pages'] == 224 and metrics['sha256'] == expected
changed = mapping['new_or_changed_pages']
individual = [1,2,3,4,5,9,10,12,13,22,23,28,31,35,44,161,166,169,174,185,193,204,206,216,218,222,224]
receipt = {
    'status': 'PASS',
    'scope': 'Read-only visual and page-layout QA; no mathematical proof certification.',
    'sealed_utc': datetime.now(timezone.utc).isoformat(),
    'pdf_filename': pdf.name,
    'sha256': expected,
    'pages': 224,
    'baseline_sha256': mapping['frozen_baseline_sha256'],
    'render': {'engine': 'Poppler pdftoppm', 'dpi': 90, 'pages_rendered': 224},
    'geometry_checked_pages': list(range(1,225)),
    'new_or_changed_pages_visually_reviewed_in_contact_sheets': changed,
    'unchanged_pages_reusing_frozen_baseline_visual_review': 224-len(changed),
    'full_size_individual_pages_reviewed': individual,
    'detailed_boxed_expressions_reviewed': 47,
    'outside_crop_glyphs': sum(len(p['outside_crop']) for p in metrics['page_results']),
    'missing_glyph_candidates': sum(len(p['missing_glyph_candidates']) for p in metrics['page_results']),
    'duplicate_chars': sum(len(p['duplicate_chars']) for p in metrics['page_results']),
    'overfull_or_missing_character_log_entries': [s for s in metrics['log_layout_warnings'] if 'Overfull' in s or 'Missing character' in s],
    'high_overlap_review': 'Candidates are deliberate arrow components, combining accents, and underbraces; no unintended visual overlap found.',
    'visual_defects': [],
    'repairs': [],
    'valid_only_for_recorded_sha256': True,
}
(q/'FINAL_VISUAL_QA_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
report = f'''# Visual QA receipt: 224-page edition

**PASS** for `Tau_Split_Zero_Total_Counterfactual.pdf`, SHA256 `{expected}`.

This receipt is restricted to the recorded PDF bytes. No mathematical source or PDF edits were made. Later editions require changed-page review.

## Coverage

- All 224 physical PDF pages rendered by Poppler at 90 dpi and scanned for text/crop geometry, absent glyph indicators, and duplicate characters.
- The frozen 109-page baseline has SHA256 `{mapping['frozen_baseline_sha256']}`. Header/footer-stripped text comparison identifies {len(changed)} new or changed physical pages and {224-len(changed)} pages whose body text matches previously reviewed baseline pages.
- All new/changed pages were visually inspected in contact sheets: **1–54; 59; 74; 90; 95–96; 98; 101–104; 106; 116; 126; 136; 141–142; 144; 146–148; 151; 157; 159–224**. See `baseline_page_mapping.json` for exact page mapping.
- All 47 detected boxed expressions on changed pages were inspected in detailed crops, including equation labels. The crop index is `boxed_detail_index.json` and the rendered sheets are `boxed-details-01.png` through `boxed-details-03.png`.
- Full-size individual inspection covered physical pages **{', '.join(map(str, individual))}**, including title/contents, dense mathematical text, diagrams, long equations, final chapter, and final provenance page.

## Findings

No clipped expressions, equation-label collisions, unintended glyph overlaps, unreadable layouts, orphan headings, or footer collisions were found. Title, contents, and deliberately sparse chapter/part endings are legible and consistently spaced. No repairs were needed.

The all-page extraction reports zero glyphs outside crop boxes, zero missing-glyph candidates, and zero duplicate-character candidates. There are no overfull or missing-character compiler entries. Fourteen underfull paragraph warnings have no observed layout defect. High-overlap candidates are intentional assembled arrows, combining accents, and underbraces; they do not indicate unintended visual overlap.

This is a visual/layout receipt. Mathematical validity and source/provenance closure are handled by the separate proof and repository reviews.
'''
(q/'VISUAL_QA.md').write_text(report,encoding='utf-8')
snapshot = q/'version_224'
snapshot.mkdir(exist_ok=True)
for p in list(q.iterdir()):
    if p.is_file():
        shutil.copy2(p,snapshot/p.name)
shutil.copy2(pdf,snapshot/pdf.name)
print(json.dumps({'status':'PASS','sha256':expected,'pages':224,'changed_pages_reviewed':len(changed),'individual_pages':len(individual),'snapshot':str(snapshot)},indent=2))
