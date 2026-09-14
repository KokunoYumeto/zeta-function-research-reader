"""Bounded positive and negative tests of the exact rendered-footer bridge.

Only in-memory pixel arrays are altered; no PDF or source is edited.
"""
import copy
import json
from pathlib import Path
import fitz
import numpy as np
import cross_page_review_transfer as transfer


def main():
    output = Path(__file__).resolve().parent / 'primitive_checks'
    if output.exists():
        raise RuntimeError('Preserve previous checks; this fixed run already exists.')
    output.mkdir()
    baseline_pin = transfer.pin(transfer.BASELINE)
    assert baseline_pin['sha256'] == transfer.BASELINE_SHA
    doc = fitz.open(transfer.BASELINE)
    matcher, args = transfer.load_matcher(), transfer.geometry_args()
    # Actual reviewed footer 98 at physical page 100 is changed to the actual
    # reviewed footer 99 from physical page 101. The source body stays exact.
    old_record = transfer.page_record(doc[99], matcher, args)
    reference_record = transfer.page_record(doc[100], matcher, args)
    final_record = copy.deepcopy(old_record)
    final_record['furniture'] = copy.deepcopy(reference_record['furniture'])
    old, old_signature = transfer.render(doc[99])
    reference, _ = transfer.render(doc[100])
    b0 = transfer.numeric_box(old_record, old.shape)
    b1 = transfer.numeric_box(final_record, old.shape)
    union = [min(b0[0], b1[0]), min(b0[1], b1[1]), max(b0[2], b1[2]), max(b0[3], b1[3])]
    x0, y0, x1, y1 = union
    final = old.copy()
    final[y0:y1, x0:x1] = reference[y0:y1, x0:x1]
    reference_records = [None] * len(doc)
    reference_records[100] = reference_record
    checks = []

    def run(name, array, record, expected):
        result = transfer.footer_substitution(old, array, old_record, record, doc,
                                               reference_records, output, 101)
        assert result['accepted'] == expected, (name, result)
        checks.append({'name': name, 'expected_acceptance': expected,
                       'actual_acceptance': result['accepted'], 'reason': result['reason']})

    run('Exact numeric substitution, complete body and remaining furniture unchanged', final, final_record, True)
    changed_body = final.copy()
    changed_body[300, 300] ^= 1
    run('One altered body pixel is rejected', changed_body, final_record, False)
    changed_header = final.copy()
    changed_header[20, 300] ^= 1
    run('One altered header pixel is rejected', changed_header, final_record, False)
    changed_footer = final.copy()
    changed_footer[y0 + 1, x0 + 1] ^= 1
    run('One unexpected pixel inside numeric mask is rejected', changed_footer, final_record, False)
    wrong_glyph = copy.deepcopy(final_record)
    wrong_glyph['furniture']['footer_glyphs'][0]['c'] = '0'
    run('Wrong replacement glyph identity is rejected', final, wrong_glyph, False)
    wrong_number = copy.deepcopy(final_record)
    wrong_number['furniture']['footer_literal_text'] = '97'
    run('Incorrect expected printed number is rejected', final, wrong_number, False)
    changed_header_geometry = copy.deepcopy(final_record)
    changed_header_geometry['furniture']['header_glyphs'][0]['bbox'][0] += 1
    run('Changed header glyph geometry is rejected', final, changed_header_geometry, False)
    coverage, bad, receipts = transfer.review_coverage(len(doc))
    assert set(coverage) == set(range(1, 1626)) and set(bad) == {811, 1137}
    checks.append({'name': 'All 1625 baseline pages have actual review receipts; exactly known unresolved pages excluded', 'pass': True})
    assert transfer.pin(transfer.BASELINE) == baseline_pin
    report = {'status': 'PASS', 'script': transfer.pin(transfer.__file__),
              'checker': transfer.pin(__file__), 'baseline_pdf': baseline_pin,
              'checks': checks, 'pdf_or_source_modified': False,
              'scope': 'Bounded primitive correctness checks. The exhaustive final-PDF transfer is separately recorded.'}
    transfer.write_json(output / 'PRIMITIVE_CHECKS.json', report)
    print(json.dumps({'status': 'PASS', 'checks': len(checks), 'receipt': str(output / 'PRIMITIVE_CHECKS.json')}))


if __name__ == '__main__':
    main()
