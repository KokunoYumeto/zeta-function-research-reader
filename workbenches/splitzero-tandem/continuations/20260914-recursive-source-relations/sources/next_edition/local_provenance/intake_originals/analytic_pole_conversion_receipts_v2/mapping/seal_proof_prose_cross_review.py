"""Seal the contextual cross-review of the two disjoint AP prose maps."""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent
FIRST = ROOT / 'proof_prose_sections_1_4.json'
SECOND = ROOT / 'proof_prose_sections_5_7.json'
EXPECTED_FIRST = 'b4f13a89f9a069cafd773b58116cfb4d317bf1e86bfb37dfb1b61b967eb2b899'
EXPECTED_SECOND = '42fdefdfa8bf3130657db7364abe3bc2f06ec7f79828682d9c76d83c00b63d45'


def pin(path):
    b = path.read_bytes()
    return {'path': path.as_posix(), 'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest()}


first_pin, second_pin = pin(FIRST), pin(SECOND)
assert first_pin['sha256'] == EXPECTED_FIRST
assert second_pin['sha256'] == EXPECTED_SECOND
first = json.loads(FIRST.read_text(encoding='utf-8'))
second = json.loads(SECOND.read_text(encoding='utf-8'))
source_path = Path(second['source']['path'])
raw = source_path.read_bytes()
assert hashlib.sha256(raw).hexdigest() == '357923aead35c77f2fa98598fbc4ed8bc1f7cd6ebc04760da504a0ded765a652'
assert len(raw) == 18433
cutoff = raw.index(b'## 5.')
assert len(first['prose_math_mappings']) == 112
assert len(second['prose_math_mappings']) == 116

# Validate exact spans, disjointness, protected headings/code and literal
# inversion independently of the map authors' generation code.
rows = sorted(first['prose_math_mappings'] + second['prose_math_mappings'],
              key=lambda row: row['source_byte_start'])
out = bytearray()
cursor = 0
inverse = []
for row in rows:
    a, z = row['source_byte_start'], row['source_byte_end']
    assert cursor <= a < z
    assert raw[a:z] == row['original'].encode('utf-8')
    line_start = raw.rfind(b'\n', 0, a) + 1
    assert not raw[line_start:].startswith((b'    ', b'#'))
    out.extend(raw[cursor:a])
    replacement = ('\\(' + row['tex'] + '\\)').encode('utf-8')
    left = len(out)
    out.extend(replacement)
    inverse.append((left, len(out), raw[a:z]))
    cursor = z
out.extend(raw[cursor:])
restored = bytes(out)
for a, z, b in reversed(inverse):
    restored = restored[:a] + b + restored[z:]
assert restored == raw
assert all(r['source_byte_end'] <= cutoff for r in first['prose_math_mappings'])
assert all(r['source_byte_start'] >= cutoff for r in second['prose_math_mappings'])

false_spans = {(8963,8964),(13990,13991),(14123,14124),(15740,15741),
               (17878,17879),(17923,17924),(18024,18025),(18059,18060),
               (18090,18091),(18277,18278)}
second_by_span = {(r['source_byte_start'],r['source_byte_end']):r for r in second['prose_math_mappings']}
assert false_spans.isdisjoint(second_by_span)
assert second_by_span[15229,15247]['tex'] == 'u d_t w(p)=-p w(p)'
assert second_by_span[16847,16848]['tex'] == 'A'
assert any(r['original'] == 'alpha' and r['tex'] == r'\alpha' for r in second['prose_math_mappings'])
assert any(r['original'] == 'tau' and r['tex'] == r'\tau' for r in second['prose_math_mappings'])
assert any(r['original'] == 'theta' and r['tex'] == r'\theta' for r in second['prose_math_mappings'])

receipt = {
    'schema': 'ap-plain-prose-math-typing-cross-review-v1',
    'status': 'accepted',
    'source': pin(source_path),
    'independently_reviewed_by_this_lane': {
        'reviewer': '/root/cumulative_reader_update/unit_gauge_source_conversion/ap_prose_first_half',
        'map': second_pin,
        'scope': 'All ordinary prose from Section 5 through Section 7 and provenance; all 116 final mappings read in source context.',
        'mapping_count': 116,
        'semantic_review': 'Every mapped mathematical expression retains its original named objects, ordered products, signs, parameters, coefficients, derivative symbol and complete expression content. Every untyped prose line was also read for omitted mathematical variables and expressions.',
        'initial_findings': 'Nine possessive-s false matches and English article A were removed; alpha, tau and theta occurrences were added; d_t was preserved exactly.',
        'final_findings': [],
        'headings_codeblocks_source_locators_hashes_untouched': True,
        'proof_reaudit_or_pdf_acceptance_claimed': False,
    },
    'independent_acceptance_received_for_this_lanes_authored_map': {
        'reviewer': '/root/cumulative_reader_update/unit_gauge_source_conversion',
        'map': first_pin,
        'scope': 'Introductory prose and Sections 1–4, 112 mappings.',
        'acceptance_source': 'Direct collaboration message received in this task.',
        'verbatim_acceptance': 'I read all112 first-half mappings against full source and accept their typings, including original complex/rational coefficient rings, entire weight, primitive, all maps/inverse-unit and fullcohomology/connection expressions.',
        'attribution_note': 'The first-half author does not claim an independent review of their own typings; the quoted acceptance is the other map author’s review.',
    },
    'joint_mechanical_checks': {
        'mapping_count': 228,
        'byte_spans_match_original_utf8': True,
        'maps_disjoint_and_in_declared_sections': True,
        'original_heading_and_indented_codeblock_spans_untouched': True,
        'literal_full_source_inverse_verified': True,
        'author_source_unchanged': source_path.read_bytes() == raw,
    },
    'review_findings_document': pin(ROOT / 'proof_prose_sections_5_7_first_half_lane_review.md'),
}
path = ROOT / 'proof_prose_cross_review.json'
path.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')
print(json.dumps(pin(path)))
