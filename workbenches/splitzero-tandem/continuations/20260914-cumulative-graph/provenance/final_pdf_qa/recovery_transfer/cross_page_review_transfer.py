"""Transfer a pinned visual review by exact page/body pixels across repagination.

No PDF or mathematical source is modified. No body character, equation number,
sign, or other mathematical content is removed or normalized. A numeric footer
substitution is the sole permitted pixel difference in an inherited page: every
other pixel must agree, and the replacement footer must itself equal the rendered
footer of an already reviewed baseline page with that exact printed number.
All other differences remain in an exhaustive queue for actual visual review.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys
import time

import fitz
import numpy as np

HERE = Path(__file__).resolve().parent
QA = HERE.parent
BASELINE = QA / 'pre_visual_correction' / 'candidate_a8264bef.pdf'
BASELINE_SHA = 'a8264bef3b1256087f99708c2d06e4bf6c45aa41669fd10679c8f352b0153252'
MATCHER = QA / 'match_cumulative_pages.py'
BODY_TOP = 55.0
BOTTOM_MARGIN = 56.89
DPI = 144
PAGE_FIELDS = ('visually_reviewed_pages', 'reviewed_actual_pages',
               'visually_inspected_actual_one_based_pages', 'reviewed_pages',
               'reviewed_actual_one_based_pages', 'inspected_pages_1based')


def sha(data):
    return hashlib.sha256(data).hexdigest()


def pin(path):
    path = Path(path).resolve()
    h = hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda: f.read(1024 * 1024), b''):
            h.update(block)
    return {'path': str(path), 'bytes': path.stat().st_size, 'sha256': h.hexdigest()}


def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def load_matcher():
    spec = importlib.util.spec_from_file_location('pinned_cumulative_matcher', MATCHER)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def geometry_args():
    return argparse.Namespace(body_top=BODY_TOP, body_bottom_margin=BOTTOM_MARGIN,
                              body_side_margin=24 * 72 / 25.4, margin_tolerance=3,
                              expected_width=595.276, expected_height=841.89)


def review_coverage(count):
    paths = sorted(QA.glob('review_*/REVIEW_RECEIPT.json'))
    paths.append(QA.parent / 'root' / 'visual_review_final_tail' / 'REVIEW_RECEIPT.json')
    coverage, bad, receipts = {}, {}, []
    for path in paths:
        value = json.loads(path.read_text(encoding='utf-8'))
        if value.get('pdf_sha256') != BASELINE_SHA:
            raise ValueError(f'Review receipt has another PDF pin: {path}')
        fields = [key for key in PAGE_FIELDS if key in value]
        if len(fields) != 1:
            raise ValueError(f'Unrecognized or ambiguous reviewed-page list: {path}')
        pages = value[fields[0]]
        if not pages or any(not isinstance(n, int) or not 1 <= n <= count for n in pages):
            raise ValueError(f'Invalid reviewed-page coverage: {path}')
        for n in pages:
            coverage.setdefault(n, []).append(str(path))
        unresolved = []
        for finding in value.get('findings', []):
            # Positive observations are explicitly marked PASS. All other
            # findings are retained unless their exact record says resolved.
            if finding.get('status') == 'PASS' or finding.get('resolved') is True:
                continue
            numbers = finding.get('pages', [])
            if not isinstance(numbers, list):
                numbers = []
            for key in ('actual_page', 'pdf_page', 'page'):
                if isinstance(finding.get(key), int):
                    numbers = numbers + [finding[key]]
            if not numbers:
                numbers = pages  # Fail closed if a defect has no page locator.
            for n in numbers:
                bad.setdefault(n, []).append({'receipt': str(path), 'finding': finding})
            unresolved.extend(numbers)
        if not str(value.get('status', '')).startswith('PASS') and not unresolved:
            for n in pages:
                bad.setdefault(n, []).append({'receipt': str(path),
                                              'reason': 'Non-PASS receipt without localized findings.'})
        receipts.append({**pin(path), 'reviewed_pages': pages,
                         'receipt_status': value.get('status'),
                         'unresolved_finding_pages': sorted(set(unresolved))})
    missing = sorted(set(range(1, count + 1)) - coverage.keys())
    if missing:
        raise ValueError(f'Baseline pages without actual review receipts: {missing}')
    return coverage, bad, receipts


def furniture_record(page):
    top, bottom = BODY_TOP, page.rect.height - BOTTOM_MARGIN
    header, footer = [], []
    flags = fitz.TEXT_PRESERVE_LIGATURES | fitz.TEXT_PRESERVE_WHITESPACE | fitz.TEXT_USE_CID_FOR_UNKNOWN_UNICODE
    for block in page.get_text('rawdict', flags=flags)['blocks']:
        for line in block.get('lines', []):
            for span in line['spans']:
                for char in span['chars']:
                    box = list(char['bbox'])
                    centre = (box[1] + box[3]) / 2
                    if top <= centre <= bottom:
                        continue
                    record = {'c': char['c'], 'font': span['font'], 'size': span['size'],
                              'color': span.get('color'), 'alpha': span.get('alpha'),
                              'bbox': box, 'origin': list(char['origin'])}
                    (header if centre < top else footer).append(record)
    return {'header_glyphs': header, 'footer_glyphs': footer,
            'header_literal_text': ''.join(g['c'] for g in header),
            'footer_literal_text': ''.join(g['c'] for g in footer)}


def expected_number(physical_page):
    return '' if physical_page == 1 else '2' if physical_page == 2 else str(physical_page - 2)


def render(page):
    pix = page.get_pixmap(matrix=fitz.Matrix(2, 2), colorspace=fitz.csRGB,
                          alpha=False, annots=True)
    array = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width, 3)
    # Integer raster partition contains every page pixel exactly once. The
    # central band includes both rounded geometric boundaries, never less.
    y0 = math.floor(BODY_TOP * 2) - pix.y
    y1 = math.ceil((page.rect.height - BOTTOM_MARGIN) * 2) - pix.y
    signature = {'width': pix.width, 'height': pix.height, 'channels': pix.n,
                 'pixmap_origin': [pix.x, pix.y], 'rgb_sha256': sha(pix.samples),
                 'body_rows_half_open': [y0, y1],
                 'body_rgb_sha256': sha(array[y0:y1].tobytes()),
                 'header_rgb_sha256': sha(array[:y0].tobytes()),
                 'footer_rgb_sha256': sha(array[y1:].tobytes())}
    return array, signature


def page_record(page, matcher, args):
    record = matcher.page_record(page, args)
    furniture = furniture_record(page)
    record['furniture'] = furniture
    literal = furniture['footer_literal_text']
    if literal != expected_number(page.number + 1):
        record['anomalies'].append({'kind': 'literal_footer_number_mismatch',
                                    'expected': expected_number(page.number + 1), 'actual': literal})
    return record


def full_geometry_equal(a, b):
    return all(a[k] == b[k] for k in ('rotation', 'page_rect', 'media_box', 'crop_box', 'body_crop'))


def numeric_box(record, shape):
    glyphs = record['furniture']['footer_glyphs']
    if not glyphs or any(g['c'] not in '0123456789' for g in glyphs):
        return None
    bounds = [min(g['bbox'][0] for g in glyphs), min(g['bbox'][1] for g in glyphs),
              max(g['bbox'][2] for g in glyphs), max(g['bbox'][3] for g in glyphs)]
    # One device-pixel padding covers antialiased edges, with a strict check
    # that the complete mask stays inside the footer and page rectangle.
    box = [math.floor(bounds[0] * 2) - 1, math.floor(bounds[1] * 2) - 1,
           math.ceil(bounds[2] * 2) + 1, math.ceil(bounds[3] * 2) + 1]
    if box[1] < math.ceil(record['body_crop'][3] * 2) or box[0] < 0 or box[2] > shape[1] or box[3] > shape[0]:
        return None
    return box


def crop(array, box):
    x0, y0, x1, y1 = box
    return array[y0:y1, x0:x1]


def outside_mask_signature(array, box):
    x0, y0, x1, y1 = box
    # Hash the four disjoint rectangles covering precisely the complement;
    # their shapes and ordering are fixed, so no byte ambiguity is possible.
    regions = [array[:y0], array[y0:y1, :x0], array[y0:y1, x1:], array[y1:]]
    return [{'shape': list(a.shape), 'rgb_sha256': sha(a.tobytes())} for a in regions]


def footer_substitution(before, after, before_record, after_record, reference_doc,
                        reference_records, output, final_page):
    left, right = before_record['furniture'], after_record['furniture']
    result = {'accepted': False, 'before': left, 'after': right}
    if left['header_glyphs'] != right['header_glyphs']:
        result['reason'] = 'Header glyph content or geometry changed.'
        return result
    old_number, new_number = left['footer_literal_text'], right['footer_literal_text']
    if old_number == new_number or new_number != expected_number(final_page):
        result['reason'] = 'Difference is not the exact expected numeric footer substitution.'
        return result
    b0, b1 = numeric_box(before_record, before.shape), numeric_box(after_record, after.shape)
    if b0 is None or b1 is None or before.shape != after.shape:
        result['reason'] = 'Numeric glyph boxes do not meet the strict footer mask geometry.'
        return result
    union = [min(b0[0], b1[0]), min(b0[1], b1[1]), max(b0[2], b1[2]), max(b0[3], b1[3])]
    exterior0, exterior1 = outside_mask_signature(before, union), outside_mask_signature(after, union)
    result.update({'before_number': old_number, 'after_number': new_number,
                   'number_delta': int(new_number) - int(old_number),
                   'before_numeric_box_pixels': b0, 'after_numeric_box_pixels': b1,
                   'union_mask_pixels': union, 'before_outside_mask': exterior0,
                   'after_outside_mask': exterior1, 'outside_mask_exactly_equal': exterior0 == exterior1})
    if exterior0 != exterior1:
        result['reason'] = 'Pixels outside the numeric glyph mask changed.'
        return result
    # The baseline page at this physical index has the exact replacement
    # number. No re-typesetting or synthetic approximation is used as oracle.
    ref = reference_records[final_page - 1]
    result['reviewed_number_reference_page'] = final_page
    if ref['furniture']['footer_glyphs'] != right['footer_glyphs']:
        result['reason'] = 'Replacement footer glyphs differ from the reviewed exact-number reference.'
        return result
    ref_array, _ = render(reference_doc[final_page - 1])
    exact_number = np.array_equal(crop(after, union), crop(ref_array, union))
    result['replacement_number_pixels_equal_reviewed_reference'] = bool(exact_number)
    if not exact_number:
        result['reason'] = 'Replacement footer pixels differ from the reviewed exact-number reference.'
        return result
    number_dir = output / 'numeric_substitutions'
    number_dir.mkdir(exist_ok=True)
    from PIL import Image
    images = {}
    for name, array in [('before', before), ('after', after), ('reviewed_reference', ref_array)]:
        path = number_dir / f'page_{final_page:04d}_{name}.png'
        Image.fromarray(crop(array, union)).save(path)
        images[name] = pin(path)
    result.update({'accepted': True, 'reason': 'Exact replacement glyphs and pixels; all other page pixels identical.',
                   'numeric_glyph_images': images})
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--new', type=Path, required=True)
    parser.add_argument('--new-sha256', required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--render-review-dpi', type=int, default=180)
    args = parser.parse_args()
    old_pin, new_pin, matcher_pin = pin(BASELINE), pin(args.new), pin(MATCHER)
    if old_pin['sha256'] != BASELINE_SHA or new_pin['sha256'] != args.new_sha256:
        parser.error('An exact PDF pin differs; no comparison performed.')
    if args.output.exists():
        parser.error('Choose a fresh output directory; previous evidence is preserved.')
    if not args.output.resolve().is_relative_to(QA):
        parser.error('Output must be under the dedicated page_qa directory.')
    if args.render_review_dpi < 144:
        parser.error('Queued full-page renders require at least 144 DPI.')
    before_doc, after_doc = fitz.open(BASELINE), fitz.open(args.new)
    coverage, defects, receipts = review_coverage(len(before_doc))
    args.output.mkdir(parents=True)
    matcher, geo_args = load_matcher(), geometry_args()
    started = time.time()
    old_records, by_body, by_full = [], {}, {}
    for i, page in enumerate(before_doc):
        record = page_record(page, matcher, geo_args)
        _, signature = render(page)
        record['pixels'] = signature
        old_records.append(matcher.compact_record(record))
        by_body.setdefault(record['literal_body_text_sha256'], []).append(i)
        by_full.setdefault(signature['rgb_sha256'], []).append(i)
        if (i + 1) % 100 == 0:
            print(f'Indexed reviewed baseline: {i + 1}/{len(before_doc)}.', flush=True)
    rows, queue, transferred = [], [], []
    for i, page in enumerate(after_doc):
        current = page_record(page, matcher, geo_args)
        after, pixels = render(page)
        current['pixels'] = pixels
        candidates = list(dict.fromkeys(by_full.get(pixels['rgb_sha256'], []) +
                                       by_body.get(current['literal_body_text_sha256'], [])))
        candidates.sort(key=lambda n: (n != i, abs(n - i)))
        attempts, match = [], None
        for n in candidates:
            old = old_records[n]
            attempt = {'baseline_page': n + 1, 'baseline_review_receipts': coverage[n + 1],
                       'baseline_unresolved_findings': defects.get(n + 1, [])}
            attempts.append(attempt)
            if defects.get(n + 1):
                attempt['result'] = 'Baseline page has an unresolved defect; cannot transfer acceptance.'
                continue
            if not full_geometry_equal(old, current):
                attempt['result'] = 'Page or fixed crop geometry changed.'
                continue
            if old['pixels']['rgb_sha256'] == pixels['rgb_sha256']:
                attempt['result'] = 'exact_full_page_pixels'
                match = attempt
                break
            if old['literal_body_text_sha256'] != current['literal_body_text_sha256']:
                attempt['result'] = 'Literal body glyph sequence changed.'
                continue
            old_complete = page_record(before_doc[n], matcher, geo_args)
            geometry, delta = matcher.geometry_match(old_complete, current, 0.01)
            attempt['body_glyph_geometry_equal'] = geometry
            attempt['maximum_body_geometry_delta_points'] = delta
            if not geometry or old['pixels']['body_rgb_sha256'] != pixels['body_rgb_sha256']:
                attempt['result'] = 'Body geometry or exact body pixels changed.'
                continue
            attempt['exact_body_pixels'] = True
            prior, _ = render(before_doc[n])
            substitution = footer_substitution(prior, after, old, current, before_doc,
                                               old_records, args.output, i + 1)
            attempt['footer_substitution'] = substitution
            if substitution['accepted']:
                attempt['result'] = 'exact_body_and_furniture_with_proved_numeric_footer_substitution'
                match = attempt
                break
            attempt['result'] = 'Body matches; changed page furniture requires actual visual review.'
        auto = match is not None and not current['anomalies']
        if auto:
            transferred.append(i + 1)
        else:
            queue.append(i + 1)
            render_dir = args.output / 'changed_pages'
            render_dir.mkdir(exist_ok=True)
            page.get_pixmap(matrix=fitz.Matrix(args.render_review_dpi / 72, args.render_review_dpi / 72),
                            colorspace=fitz.csRGB, alpha=False, annots=True).save(render_dir / f'page_{i + 1:04d}.png')
        rows.append({**matcher.compact_record(current), 'candidate_checks': attempts,
                     'matched_baseline_page': match['baseline_page'] if match else None,
                     'transfer_kind': match['result'] if match else None,
                     'inherited_visual_acceptance': auto, 'actual_visual_review_required': not auto})
        if (i + 1) % 50 == 0:
            write_json(args.output / 'IN_PROGRESS_QUEUE.json',
                       {'final_pdf': new_pin, 'final_pages_accounted_so_far': i + 1,
                        'total_final_pages': len(after_doc), 'incomplete': True,
                        'changed_pages_requiring_actual_visual_review': queue,
                        'render_directory': str(args.output / 'changed_pages')})
            print(f'Final pages accounted: {i + 1}/{len(after_doc)}; new visual queue: {len(queue)}.', flush=True)
    assert set(queue).isdisjoint(transferred)
    assert set(queue) | set(transferred) == set(range(1, len(after_doc) + 1))
    assert pin(BASELINE) == old_pin and pin(args.new) == new_pin and pin(MATCHER) == matcher_pin
    assert all(pin(r['path'])['sha256'] == r['sha256'] for r in receipts)
    report = {'schema': 'cross-page-exact-render-review-transfer-v1',
              'status': 'exhaustive transfer complete; changed-page visual review remains pending',
              'script': pin(__file__), 'geometry_matcher': matcher_pin,
              'baseline_pdf': old_pin, 'final_pdf': new_pin,
              'baseline_page_count': len(before_doc), 'final_page_count': len(after_doc),
              'baseline_review_receipts': receipts, 'baseline_unresolved_defects': defects,
              'renderer': {'pymupdf': fitz.VersionBind, 'python': sys.version, 'dpi': DPI,
                           'colorspace': 'RGB', 'alpha': False, 'annotations': True},
              'comparison': {'body_top_points': BODY_TOP, 'body_bottom_margin_points': BOTTOM_MARGIN,
                             'body_text_normalized': False, 'body_pixel_equality': 'Exact RGB byte hashes.',
                             'body_geometry_tolerance_points': 0.01,
                             'numeric_substitution': 'Only exact printed-number replacement; reviewed reference glyph pixels; exact complement-of-mask page pixels.',
                             'source_or_pdf_mutations': False},
              'all_final_pages_accounted': True, 'inherited_visual_pages': transferred,
              'changed_pages_requiring_actual_visual_review': queue,
              'page_records': rows, 'baseline_page_records': old_records,
              'elapsed_seconds': round(time.time() - started, 3),
              'whole_document_visual_acceptance': False}
    write_json(args.output / 'CROSS_PAGE_RENDER_TRANSFER.json', report)
    write_json(args.output / 'CHANGED_PAGE_VISUAL_QUEUE.json',
               {'final_pdf': new_pin, 'all_final_pages_accounted': True, 'pages': queue,
                'batches': [{'batch': k // 12 + 1, 'pages': queue[k:k + 12]} for k in range(0, len(queue), 12)],
                'render_dpi': args.render_review_dpi, 'directory': str(args.output / 'changed_pages')})
    write_json(args.output / 'OUTPUT_MANIFEST.json',
               {'final_pdf': new_pin, 'files': [pin(p) for p in sorted(args.output.rglob('*')) if p.is_file()]})
    print(json.dumps({'final_pages': len(after_doc), 'transferred': len(transferred),
                      'review_queue': queue, 'output': str(args.output)}, indent=2), flush=True)


if __name__ == '__main__':
    main()
