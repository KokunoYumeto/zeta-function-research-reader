"""Seal the actually validated mixed-face edition; retain historical seals."""
from pathlib import Path
import datetime
import hashlib
import json
import shutil

WORK = Path(__file__).resolve().parents[1]
REPO = WORK.parents[1] / 'output/tau_split_zero_counterfactual_continuation_20260913'

def main():
    validation = json.loads((REPO/'build/REPOSITORY_VALIDATION.json').read_text())
    qa = json.loads((REPO/'build/visual_qa/FINAL_VISUAL_QA_RECEIPT.json').read_text())
    inputs = json.loads((REPO/'provenance/CONTINUATION_INPUT_MANIFEST.json').read_text())
    pdf = REPO/'Tau_Split_Zero_Total_Counterfactual.pdf'
    digest = hashlib.sha256(pdf.read_bytes()).hexdigest()
    assert validation['passed'] and validation['pdf_sha256'] == digest
    assert qa['status'] == 'PASS' and qa['sha256'] == digest
    required = {'TO', 'CAU', 'CFA', 'MFC', 'MCF', 'MW', 'MRE', 'MAI', 'WDB', 'SPC', 'ACM', 'BC', 'SP', 'EPE'}
    actual = {row['code'] for row in inputs['entries']}
    assert required <= actual, sorted(required-actual)
    timestamp = datetime.datetime.now().astimezone().isoformat()
    count = len(validation['proof_integrity'])
    pages = validation['pdf_pages']
    record = {
        'recorded_at': timestamp, 'pdf_sha256': digest, 'pages': pages,
        'validation': 'PASS', 'visual_qa': 'PASS', 'proof_modules': count,
        'mixed_coefficient_generators_explicit': True,
        'original_leg_and_coefficient_masks_independent': True,
        'rh_endpoint_established': False,
        'goal_status_observed': 'active when restored on 2026-09-13; this seal does not change the goal',
        'publication': 'none',
        'preceding_248_page_edition': 'preserved separately as intermediate',
    }
    (REPO/'provenance/TOTAL_OBJECT_EDITION.json').write_text(
        json.dumps(record, indent=2), encoding='utf8')
    readme = (WORK/'total_object/README_MIXED_EDITION.md').read_text(encoding='utf8')
    for key, value in {
        '@PAGES@': pages, '@MODULES@': count,
        '@LABELS@': validation['label_count'],
        '@REFS@': validation['reference_count'], '@PDF_SHA@': digest,
    }.items():
        readme = readme.replace(key, str(value))
    (REPO/'README.md').write_text(readme, encoding='utf8')
    notes = (WORK/'total_object/MIXED_EDITION_CALCULATION.md').read_text(encoding='utf8')
    addition = (f'\n## {timestamp} — Mixed-face cumulative edition\n\n'
                f'Validated PDF: {pages} pages, {count} proof modules, SHA256 {digest}. '
                'Visual QA and source/reference validation match this exact hash.\n\n'
                + notes + '\n')
    for name in ['CURRENT_CALCULATION.md', 'WORK_LOG.md']:
        path = WORK/name
        if digest not in path.read_text(encoding='utf8'):
            with path.open('a', encoding='utf8') as stream:
                stream.write(addition)
    for name in ['CURRENT_CALCULATION.md', 'WORK_LOG.md',
                 'USER_INPUTS_VERBATIM.md', 'CORRECTED_ACTIVE_GOAL.md']:
        shutil.copy2(WORK/name, REPO/'provenance'/name)
    shutil.copy2(WORK/'shared_thread_audit/THIS_SESSION_USER_INPUTS_VERBATIM.md',
                 REPO/'provenance/THIS_SESSION_USER_INPUTS_VERBATIM.md')
    print(json.dumps(record, indent=2))

if __name__ == '__main__':
    main()
