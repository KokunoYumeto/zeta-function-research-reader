"""Compare cumulative pages to a pinned historical PDF without changing either PDF.

Literal body-character text selects candidates; actual character geometry and
rendered body pixels must then match. Every other page remains for visual review.
The fixed geometric crop excludes header/footer/page-number regions only. It does
not remove section numbers, equation numbers, signs, constants or mathematical
characters inside the body. The tool never declares a complete visual audit.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
import sys
import time

import fitz

HISTORICAL_SHA = 'fa24ff486c02da2c4e3a66389a148faff7c0024bbca319e8f3e4625f647bd855'
DEFAULT_HISTORICAL = Path(r'workspace:\output\split_zero_rh_tandem_2026-09-12\current_source_20260913_periodized_residue\Split_Zero_Cohomology_and_Arithmetic_Weight_Control.pdf')


def digest(data):
    return hashlib.sha256(data).hexdigest()


def file_pin(path):
    path = Path(path).resolve()
    hasher = hashlib.sha256()
    size = 0
    with path.open('rb') as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b''):
            hasher.update(block)
            size += len(block)
    return {'path': str(path), 'bytes': size, 'sha256': hasher.hexdigest()}


def save_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def finite_box(box):
    return len(box) == 4 and all(math.isfinite(x) for x in box) and box[2] >= box[0] and box[3] >= box[1]


def crop_for(page, args):
    return fitz.Rect(0, args.body_top, page.rect.width, page.rect.height - args.body_bottom_margin)


def body_character(char, crop):
    # Whole mathematical glyphs at a crop boundary are flagged separately.
    bbox = char['bbox']
    centre_y = (bbox[1] + bbox[3]) / 2
    return crop.y0 <= centre_y <= crop.y1


def page_record(page, args):
    crop = crop_for(page, args)
    # Preserve the PDF's CID fallback for valid legacy CMEX10 symbols whose
    # ToUnicode mapping is incomplete. No Unicode normalization is performed.
    extraction_flags = fitz.TEXT_PRESERVE_LIGATURES | fitz.TEXT_PRESERVE_WHITESPACE | fitz.TEXT_USE_CID_FOR_UNKNOWN_UNICODE
    raw = page.get_text('rawdict', flags=extraction_flags)
    glyphs = []
    anomalies = []
    boundary_glyphs = []
    outside_page = []
    suspected_glyphs = []
    for block in raw['blocks']:
        for line in block.get('lines', []):
            for span in line['spans']:
                for char in span['chars']:
                    box = char['bbox']
                    literal_space = char['c'] in {' ', '\u00a0'} and not span['font'].upper().startswith(('CM', 'LM', 'MSAM', 'MSBM'))
                    if not finite_box(box):
                        anomalies.append({'kind': 'invalid_character_box', 'character': char['c'], 'bbox': box})
                        continue
                    if not literal_space and (box[0] < -0.5 or box[1] < -0.5 or box[2] > page.rect.width + 0.5 or box[3] > page.rect.height + 0.5):
                        outside_page.append({'character': char['c'], 'bbox': list(box)})
                    # Check crossings before selecting centres: content whose
                    # centre is outside the crop must not disappear silently.
                    if not literal_space and (box[1] < crop.y0 < box[3] or box[1] < crop.y1 < box[3]):
                        boundary_glyphs.append({'character': char['c'], 'bbox': list(box)})
                    if not body_character(char, crop):
                        continue
                    glyphs.append({'c': char['c'], 'font': span['font'], 'size': span['size'],
                                   'literal_space': literal_space, 'bbox': list(box), 'origin': list(char['origin'])})
                    # NUL/control/PUA values can be valid CMEX10 ToUnicode
                    # encodings in the historical PDF; preserve them literally.
                    if char['c'] == '\ufffd':
                        suspected_glyphs.append({'kind': 'rawdict_replacement_character', 'character': repr(char['c']), 'bbox': list(box)})
    if outside_page:
        anomalies.append({'kind': 'characters_outside_page', 'characters': outside_page})
    if boundary_glyphs:
        anomalies.append({'kind': 'body_glyph_crosses_header_footer_crop', 'characters': boundary_glyphs})
    # Glyph id zero is a suspicion requiring visual inspection, not a mathematical
    # conclusion: some PDF fonts intentionally use unusual encodings.
    for trace in page.get_texttrace():
        for unicode_value, glyph_id, origin, bbox in trace['chars']:
            literal_space = unicode_value in {32, 160} and not trace['font'].upper().startswith(('CM', 'LM', 'MSAM', 'MSBM'))
            if glyph_id == 0 and not literal_space and crop.y0 <= origin[1] <= crop.y1:
                suspected_glyphs.append({'kind': 'zero_glyph_id', 'unicode': unicode_value,
                                        'origin': list(origin), 'bbox': list(bbox), 'font': trace['font']})
    if suspected_glyphs:
        anomalies.append({'kind': 'suspected_missing_glyphs', 'items': suspected_glyphs})
    text = ''.join(glyph['c'] for glyph in glyphs)
    if not text.strip():
        anomalies.append({'kind': 'empty_body_text'})
    visible = [g for g in glyphs if not g['literal_space']]
    if visible:
        limits = [min(g['bbox'][0] for g in visible), min(g['bbox'][1] for g in visible),
                  max(g['bbox'][2] for g in visible), max(g['bbox'][3] for g in visible)]
        margin = args.body_side_margin
        if limits[0] < margin - args.margin_tolerance or limits[2] > page.rect.width - margin + args.margin_tolerance:
            anomalies.append({'kind': 'body_side_margin_overflow', 'body_bbox': limits,
                              'expected_left': margin, 'expected_right': page.rect.width - margin,
                              'tolerance_points': args.margin_tolerance})
    else:
        limits = None
    if page.rotation != 0:
        anomalies.append({'kind': 'rotated_page', 'rotation': page.rotation})
    for kind, boxes in [('vector', [d['rect'] for d in page.get_drawings()]),
                        ('image', [d['bbox'] for d in page.get_image_info()])]:
        crossings = [list(box) for box in boxes if box[1] < crop.y0 < box[3] or box[1] < crop.y1 < box[3]]
        if crossings:
            anomalies.append({'kind': kind + '_crosses_header_footer_crop', 'boxes': crossings})
    if abs(page.rect.width - args.expected_width) > 0.2 or abs(page.rect.height - args.expected_height) > 0.2:
        anomalies.append({'kind': 'unexpected_page_size', 'actual': list(page.rect),
                          'expected': [args.expected_width, args.expected_height]})
    return {'page': page.number + 1, 'body_crop': list(crop), 'page_rect': list(page.rect),
            'media_box': list(page.mediabox), 'crop_box': list(page.cropbox),
            'rotation': page.rotation, 'body_bbox': limits,
            'literal_body_text_sha256': digest(text.encode('utf-8')),
            'font_typed_body_text_sha256': digest(json.dumps([(g['font'], g['c']) for g in glyphs], ensure_ascii=False).encode('utf-8')),
            'body_character_count': len(glyphs), 'glyphs': glyphs,
            'anomalies': anomalies}


def geometry_match(left, right, tolerance):
    if left['rotation'] != right['rotation'] or len(left['glyphs']) != len(right['glyphs']):
        return False, None
    maximum = 0.0
    for key in ['page_rect', 'media_box', 'crop_box', 'body_crop']:
        maximum = max(maximum, *(abs(x - y) for x, y in zip(left[key], right[key])))
    for lchar, rchar in zip(left['glyphs'], right['glyphs']):
        if lchar['c'] != rchar['c'] or lchar['font'] != rchar['font']:
            return False, None
        maximum = max(maximum, abs(lchar['size'] - rchar['size']))
        for key in ['bbox', 'origin']:
            maximum = max(maximum, *(abs(x - y) for x, y in zip(lchar[key], rchar[key])))
        if maximum > tolerance:
            return False, maximum
    return maximum <= tolerance, maximum


def pixel_signature(page, crop, dpi):
    pix = page.get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72), clip=fitz.Rect(crop),
                          colorspace=fitz.csRGB, alpha=False, annots=True)
    return {'width': pix.width, 'height': pix.height, 'channels': pix.n,
            'rgb_sha256': digest(pix.samples)}


def compact_record(record):
    return {key: value for key, value in record.items() if key != 'glyphs'}


def render_review(doc, pages, output, args):
    if not (args.contact_sheets or args.render_review_pages):
        return []
    from PIL import Image, ImageDraw
    sheets = []
    columns, rows, width, label = 3, 4, 420, 30
    height = int(width * args.expected_height / args.expected_width)
    sheet = None
    draw = None
    batch = []
    for position, number in enumerate(pages):
        if position % (columns * rows) == 0:
            sheet = Image.new('RGB', (columns * width, rows * (height + label)), 'white')
            draw = ImageDraw.Draw(sheet)
            batch = []
        pix = doc[number - 1].get_pixmap(matrix=fitz.Matrix(args.review_dpi / 72, args.review_dpi / 72),
                                       colorspace=fitz.csRGB, alpha=False)
        if args.render_review_pages:
            page_dir = output / 'review_pages'
            page_dir.mkdir(exist_ok=True)
            pix.save(page_dir / f'page_{number:04d}.png')
        if args.contact_sheets:
            image = Image.frombytes('RGB', [pix.width, pix.height], pix.samples)
            image.thumbnail((width - 12, height - 8), Image.Resampling.LANCZOS)
            local = position % (columns * rows)
            x, y = (local % columns) * width, (local // columns) * (height + label)
            draw.text((x + 10, y + 7), f'PDF page {number}', fill='black')
            sheet.paste(image, (x + (width - image.width) // 2, y + label))
            batch.append(number)
            if local == columns * rows - 1 or position == len(pages) - 1:
                name = f'review_sheet_{len(sheets) + 1:03d}.png'
                sheet.save(output / name)
                sheets.append({'file': name, 'pages': batch.copy()})
    return sheets


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--current', type=Path, required=True)
    parser.add_argument('--historical', type=Path, default=DEFAULT_HISTORICAL)
    parser.add_argument('--mode', choices=['prototype', 'final'], default='prototype')
    parser.add_argument('--expected-current-sha256')
    parser.add_argument('--expected-historical-sha256', default=HISTORICAL_SHA)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--body-top', type=float, default=55)
    parser.add_argument('--body-bottom-margin', type=float, default=56.89)
    parser.add_argument('--body-side-margin', type=float, default=24 * 72 / 25.4)
    parser.add_argument('--margin-tolerance', type=float, default=3)
    parser.add_argument('--geometry-tolerance', type=float, default=0.01)
    parser.add_argument('--expected-width', type=float, default=595.276)
    parser.add_argument('--expected-height', type=float, default=841.89)
    parser.add_argument('--pixel-dpi', type=int, default=144)
    parser.add_argument('--review-dpi', type=int, default=110)
    parser.add_argument('--contact-sheets', action='store_true')
    parser.add_argument('--render-review-pages', action='store_true')
    parser.add_argument('--limit-current-pages', type=int, help='Prototype only; never truncates a final audit.')
    args = parser.parse_args()
    if args.mode == 'final' and (not args.expected_current_sha256 or args.limit_current_pages is not None):
        parser.error('Final mode requires the exact current SHA256 and forbids a page limit.')
    current_pin, historical_pin = file_pin(args.current), file_pin(args.historical)
    if historical_pin['sha256'] != args.expected_historical_sha256:
        parser.error('Historical PDF pin differs.')
    if args.expected_current_sha256 and current_pin['sha256'] != args.expected_current_sha256:
        parser.error('Current PDF pin differs.')
    if args.output.exists():
        parser.error('Choose a fresh output directory; prior QA results are preserved.')
    if args.output.resolve().is_relative_to(args.historical.resolve().parent):
        parser.error('QA output must be outside the sealed historical package.')
    if args.limit_current_pages is not None and args.limit_current_pages <= 0:
        parser.error('A prototype page limit must be positive.')
    args.output.mkdir(parents=True)
    historical = fitz.open(args.historical)
    current = fitz.open(args.current)
    started = time.time()
    old_records = []
    by_text = {}
    print(f'Checking historical page text and geometry: {len(historical)} pages.', flush=True)
    for page in historical:
        record = page_record(page, args)
        # Retain only small historical index records. Re-extract coordinates
        # for actual candidates rather than retaining millions of glyph dicts.
        old_records.append(compact_record(record))
        by_text.setdefault(record['literal_body_text_sha256'], []).append(page.number)
    records = []
    review_pages = []
    used_historical = set()
    old_pixels = {}
    limit = min(len(current), args.limit_current_pages or len(current))
    for number in range(limit):
        page = current[number]
        record = page_record(page, args)
        candidates = by_text.get(record['literal_body_text_sha256'], [])
        status = 'unmatched_body_text'
        geometry_candidates = []
        matched = None
        current_pixels = None
        checks = []
        for candidate in candidates:
            old = page_record(historical[candidate], args)
            equal_geometry, delta = geometry_match(old, record, args.geometry_tolerance)
            check = {'historical_page': candidate + 1, 'geometry_equal': equal_geometry,
                     'maximum_geometry_delta_points': delta}
            if not equal_geometry:
                checks.append(check)
                continue
            geometry_candidates.append(candidate + 1)
            if current_pixels is None:
                current_pixels = pixel_signature(page, record['body_crop'], args.pixel_dpi)
            if candidate not in old_pixels:
                old_pixels[candidate] = pixel_signature(historical[candidate], old['body_crop'], args.pixel_dpi)
            check['historical_pixels'] = old_pixels[candidate]
            check['current_pixels'] = current_pixels
            check['pixels_equal'] = old_pixels[candidate] == current_pixels
            checks.append(check)
            if check['pixels_equal']:
                matched = candidate + 1
                used_historical.add(matched)
                break
        if candidates:
            status = 'literal_text_matches_geometry_changed'
        if geometry_candidates:
            status = 'literal_text_and_geometry_match_pixels_changed'
        if matched is not None:
            status = 'exact_inherited_body_pixel_match'
        auto_pass = matched is not None and not record['anomalies']
        if not auto_pass:
            review_pages.append(number + 1)
        records.append({**compact_record(record), 'status': status, 'matched_historical_page': matched,
                        'candidate_historical_pages': [i + 1 for i in candidates],
                        'candidate_checks': checks, 'automatic_body_acceptance': auto_pass,
                        'visual_review_required': not auto_pass})
        if (number + 1) % 50 == 0:
            print(f'Current pages checked: {number + 1}/{limit}; visual review required: {len(review_pages)}.', flush=True)
    assert len(records) == limit
    assert set(review_pages) | {r['page'] for r in records if r['automatic_body_acceptance']} == set(range(1, limit + 1))
    assert not set(review_pages) & {r['page'] for r in records if r['automatic_body_acceptance']}
    sheets = render_review(current, review_pages, args.output, args)
    assert file_pin(args.current) == current_pin and file_pin(args.historical) == historical_pin, 'An input PDF changed during QA.'
    report = {
        'schema': 'cumulative-historical-page-matcher-v1',
        'mode': args.mode,
        'status': 'prototype_only' if args.mode == 'prototype' else 'awaiting_exhaustive_visual_review',
        'script': file_pin(Path(__file__)), 'historical_pdf': historical_pin, 'current_pdf': current_pin,
        'tool_version': {'pymupdf': fitz.VersionBind, 'python': sys.version},
        'comparison': {'literal_body_text': True, 'mathematical_text_normalized': False,
                       'rawdict_extraction_flags': 131,
                       'legacy_glyphs': 'Literal CID/control/PUA values retained with font identity; no semantic Unicode substitution.',
                       'header_footer_exclusion': 'Fixed geometric crop only; all body section/equation numbers retained.',
                       'body_top_points': args.body_top, 'body_bottom_margin_points': args.body_bottom_margin,
                       'geometry_tolerance_points': args.geometry_tolerance, 'pixel_dpi': args.pixel_dpi,
                       'pixels': 'Exact RGB sample hash, common body crop, same renderer/options.',
                       'automatic_acceptance_requires_no_anomalies': True},
        'historical_page_count': len(historical), 'current_page_count': len(current),
        'current_pages_examined': limit, 'all_current_pages_examined': limit == len(current),
        'automatic_inherited_body_matches': sum(r['automatic_body_acceptance'] for r in records),
        'visual_review_pages': review_pages,
        'visual_review_batches': [{'batch': i // 12 + 1, 'pages': review_pages[i:i + 12]}
                                  for i in range(0, len(review_pages), 12)],
        'anomaly_pages': [r['page'] for r in records if r['anomalies']],
        'unmapped_historical_pages': sorted(set(range(1, len(historical) + 1)) - used_historical),
        'unmapped_historical_meaning': 'No exact current page-body match; this may reflect revision or repagination and is not a claim that historical mathematics is missing.',
        'header_footer_review_required': 'The final complete edition still requires global header/footer/page-number checks; body matching intentionally excludes those regions.',
        'page_records': records, 'historical_page_records': [compact_record(r) for r in old_records],
        'contact_sheets': sheets, 'elapsed_seconds': round(time.time() - started, 3),
        'source_or_pdf_mutations': False, 'visual_audit_complete': False,
    }
    save_json(args.output / 'PAGE_MATCH_REPORT.json', report)
    save_json(args.output / 'VISUAL_REVIEW_QUEUE.json', {'schema': 'exhaustive-current-page-review-queue-v1',
              'mode': args.mode, 'pdf': current_pin, 'pages': review_pages,
              'batches': report['visual_review_batches'], 'all_current_pages_examined': limit == len(current)})
    (args.output / 'REVIEW_PAGE_NUMBERS.txt').write_text(', '.join(map(str, review_pages)) + '\n', encoding='utf-8')
    md = ['# Cumulative PDF page comparison', '',
          '**Mode: ' + args.mode + '.** ' + report['status'] + '.', '',
          f'Examined {limit} of {len(current)} current pages against all {len(historical)} historical pages.', '',
          f'Exact inherited body matches with no flagged anomaly: {report["automatic_inherited_body_matches"]}.', '',
          f'Pages requiring visual review: {len(review_pages)}. The complete list and batches are in VISUAL_REVIEW_QUEUE.json.', '',
          'Every automatically mapped page passed literal body text, character geometry and exact body-pixel comparison. The fixed crop excludes only header/footer regions; mathematical text is not normalized.', '',
          'All-page geometry and suspected missing glyph checks are recorded per page. An anomaly is a review signal, not a proof of defective mathematics or a missing glyph.', '',
          'Contact sheets provide navigation. Inspect full pages whenever a contact-sheet cell is insufficient to verify labels, displays or clipping. Marked historical page matches do not replace global header/footer/page-number review.', '',
          'No final visual acceptance is asserted by this script.', '']
    (args.output / 'README.md').write_text('\n'.join(md), encoding='utf-8')
    products = [file_pin(p) for p in sorted(args.output.rglob('*')) if p.is_file()]
    save_json(args.output / 'QA_OUTPUT_MANIFEST.json', {'schema': 'page-qa-output-manifest-v1',
              'mode': args.mode, 'current_pdf': current_pin, 'historical_pdf': historical_pin, 'files': products})
    print(json.dumps({'status': report['status'], 'output': str(args.output),
                      'automatic_body_matches': report['automatic_inherited_body_matches'],
                      'review_pages': len(review_pages), 'anomaly_pages': len(report['anomaly_pages'])}, indent=2))


if __name__ == '__main__':
    main()
