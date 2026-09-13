"""Read-only final visual evidence/spec audit; writes only its named evidence JSON."""
from pathlib import Path
import ast
import hashlib
import json
import re
from PIL import Image
from pypdf import PdfReader

W = Path(__file__).resolve().parents[1]
R = W / 'output/split_zero_rh_tandem_2026-09-12'
work = W / 'work'
H = work / 'history/gamma_edition_pre_visual_20260913'
WORKFLOW = 'd881c7ebdbfee984b8eead90cb78a1f4e90693c8748f4210d3dc4be55e8978f9'
PDF_SHA = '9e79bd6cb4f95d845af0f637a1cb4fdcb56ddf32015f89430fa12c530b8b1680'
VISUAL_SHA = '57929b33bc93d9f6b7767840133a9062b0014f28bc071a3b77a0f06cb6c719d4'

def read(p):
    return json.loads(p.read_text(encoding='utf-8-sig'))

def pin(p):
    data = p.read_bytes()
    return {'sha256': hashlib.sha256(data).hexdigest(), 'bytes': len(data)}

def need(ok, msg):
    if not ok:
        raise RuntimeError(msg)

def relative(locator):
    value = locator.replace('\\', '/')
    prefix = R.as_posix() + '/'
    if value.casefold().startswith(prefix.casefold()):
        value = value[len(prefix):]
    if value.startswith('package:'):
        value = value[len('package:'):].lstrip('/')
    need(not value.startswith('/') and ':' not in value and all(s not in ('', '.', '..') for s in value.split('/')), 'Noncanonical locator')
    p = R / value
    need(p.resolve().is_relative_to(R.resolve()), 'Locator escapes R')
    return value

def check_image(rel, sha):
    p = R / relative(rel)
    need(pin(p)['sha256'] == sha, 'Image hash: ' + relative(rel))
    with Image.open(p) as image:
        dimensions = list(image.size)
        format_name = image.format
        image.verify()
    return {'path': relative(rel), **pin(p), 'dimensions': dimensions, 'format': format_name}

need(pin(work / 'gamma_edition_workflow_20260913.py')['sha256'] == WORKFLOW, 'Workflow changed')
spec = read(work / 'gamma_edition_spec_20260913.json')
previous = read(H / 'gamma_edition_spec_20260913.json')
extras = read(work / 'gamma_visual_public_files_fragment_20260913.json')
need(len(extras) == 54 and len({x['path'].casefold() for x in extras}) == 54, '54 unique extras required')
need(spec['preceding_review_history'] == 'work/history/gamma_edition_pre_visual_20260913/HISTORY.json', 'Exact preceding-history locator')
need({k: v for k, v in spec.items() if k not in ('public_files', 'work_files', 'preceding_review_history')} ==
     {k: v for k, v in previous.items() if k not in ('public_files', 'work_files')}, 'Out-of-scope spec change')
need(spec['public_files'] == previous['public_files'] + extras, 'Exact ordered public append')
need(not ({x['path'] for x in extras} & {x['path'] for x in previous['public_files']}), 'Existing public path duplicated')
history = read(H / 'HISTORY.json')
historical = []
for row in history['files']:
    p = work / row['historical_work_path']
    need(pin(p) == {k: row[k] for k in ('sha256', 'bytes')}, 'Historical evidence changed')
    historical.append({'path': 'work/' + row['historical_work_path'], **pin(p)})
need(pin(H / 'gamma_edition_spec_20260913.json')['sha256'] == '5780e4f4306365ef1a4e8775ae15522e78263b1d387808218caf2a3da0547081', 'Old spec pin')
need(pin(H / 'gamma_edition_independent_workflow_review_receipt_20260913.json')['sha256'] == '00f524b5e37d2dfdba82ca49fc010707ba8af64fd702c3c2d2e250d4c7b12ff8', 'Old seal pin')
expected_work = {x['historical_work_path'] for x in history['files']} | {
    'history/gamma_edition_pre_visual_20260913/HISTORY.json',
    'gamma_visual_public_files_fragment_20260913.json',
    'gamma_edition_final_visual_allowlist_review_20260913.md',
    'gamma_edition_final_visual_allowlist_audit_20260913.py',
    'gamma_edition_final_visual_allowlist_evidence_20260913.json',
    'gamma_edition_final_visual_allowlist_review_seal_20260913.json'}
need(spec['work_files'][:len(previous['work_files'])] == previous['work_files'], 'Previous work order changed')
need(set(spec['work_files'][len(previous['work_files']):]) == expected_work and len(spec['work_files']) == len(set(spec['work_files'])), 'Unexpected work additions')

pdf = R / 'Split_Zero_Cohomology_and_Arithmetic_Weight_Control.pdf'
need(pin(pdf)['sha256'] == PDF_SHA and len(PdfReader(pdf).pages) == 478, 'Actual PDF identity/count')
visual_path = R / 'build/qa/visual_review.json'
need(pin(visual_path)['sha256'] == VISUAL_SHA, 'Aggregate visual pin')
visual = read(visual_path)
need(read(R / 'logbook/GAMMA_VISUAL_REVIEW_20260913.json') == visual, 'Aggregate logbook/build correspondence')
need(visual['pdf_sha256'] == PDF_SHA and visual['pages'] == 478 and visual['approved'] is True and visual['reviewed_all_pages'] is True, 'Aggregate PDF/scope')
need(visual['coverage'] == list(range(1, 479)), 'Aggregate complete exact coverage')
qa_path = R / visual['render_receipt']['path']
need(pin(qa_path)['sha256'] == visual['render_receipt']['sha256'], 'Render receipt pin')
qa = read(qa_path)
need(qa['pdf_sha256'] == PDF_SHA and qa['pages'] == qa['rendered_pages'] == 478 and qa['dpi'] == 95, 'Render PDF/count/DPI')
need(qa['out_of_page_words'] == qa['body_margin_crossings'] == [], 'Renderer layout flags')
build = read(R / 'build/build_receipt.json')
need(build['status'] == 'compiled' and build['pdf_sha256'] == PDF_SHA and build['pages'] == 478 and len(build['tex_inputs']) == 44 and len(build['source_notes']) == 19, 'Reader proof/source cut')
for rel, sha in build['tex_inputs'].items():
    need(pin(R / rel)['sha256'] == sha, 'Current reader input: ' + rel)
for row in build['source_notes']:
    need(pin(R / row['source'])['sha256'] == row['sha256'], 'Current appendix source')

source_audit = read(R / spec['source_audit'])
need(source_audit['pdf_sha256'] == PDF_SHA and source_audit['proof_fragments'] == 43 and source_audit['complete_source_appendices'] == 19, 'Final source audit identity')
for row in source_audit['checks']:
    need(row['matches'] is True and pin(R / row['path'])['sha256'] == row['sha256'], 'Final proof audit pin')
for row in source_audit['sources']:
    need(row['original_preserved'] is True and pin(R / row['path'])['sha256'] == row['sha256'] and
         pin(R / row['converted'])['sha256'] == row['converted_sha256'], 'Final appendix audit pin')

contact_rows, native_rows, components, coverage = [], [], [], []
extra_render_hashes = []
raw_index = {x['path']: x['sha256'] for x in visual['original_component_receipts']}
for index, (first, last) in enumerate(((1, 120), (121, 240), (241, 360), (361, 478))):
    wrapper_pin = visual['component_receipts'][index]
    wrapper_path = R / wrapper_pin['path']
    need(pin(wrapper_path)['sha256'] == wrapper_pin['sha256'], 'Wrapper hash')
    wrapper = read(wrapper_path)
    raw_path = R / wrapper['original_receipt']['path']
    need(pin(raw_path)['sha256'] == wrapper['original_receipt']['sha256'] == raw_index[wrapper['original_receipt']['path']], 'Original review hash')
    raw = read(raw_path)
    need(wrapper['original_review'] == raw, 'Wrapper full original object differs')
    need(wrapper['pdf_sha256'] == PDF_SHA and wrapper['pages'] == 478 and wrapper['approved'] is True and
         wrapper['first_pdf_page'] == first and wrapper['last_pdf_page'] == last, 'Wrapper PDF/range')
    raw_pdf = raw.get('pdf_sha256', raw.get('pdf_sha256_independently_measured'))
    need(raw_pdf == PDF_SHA, 'Raw review PDF')
    contacts = raw.get('viewed_contact_sheets', raw.get('viewed_contacts', raw.get('contacts_actually_viewed')))
    need(len(contacts) == 20, 'Raw contacts count')
    projected_contacts = [{'path': relative(row['path']), 'sha256': row['sha256'],
                           'pages': row.get('physical_pages', row.get('pages', row.get('physical_pdf_pages')))} for row in contacts]
    need(projected_contacts == wrapper['reviewed_contacts'], 'Exact raw/contact projection')
    pages = [n for row in projected_contacts for n in row['pages']]
    need(pages == list(range(first, last + 1)), 'Exact component contact coverage')
    coverage.extend(pages)
    for row in projected_contacts:
        contact_rows.append({**check_image(row['path'], row['sha256']), 'pages': row['pages']})
    natives = raw.get('viewed_native_page_pngs', raw.get('viewed_native_pages', raw.get('native_pages_actually_viewed')))
    if natives is None:
        natives = [r for r in raw['covered_page_images'] if r['additionally_viewed_native']]
    projected_natives = [{'path': relative(row['path']), 'sha256': row['sha256']} for row in natives]
    need(len({row['path'] for row in projected_natives}) == len(projected_natives), 'Repeated native path')
    ordered_natives = sorted(projected_natives, key=lambda row: row['path'])
    need(ordered_natives == wrapper['individually_viewed_page_images'], 'Exact path-ordered raw/native projection')
    for row in ordered_natives:
        native_rows.append(check_image(row['path'], row['sha256']))
    for row in raw.get('covered_page_images', []) + raw.get('page_coverage_and_render_hashes', []):
        rel = relative(row.get('path', row.get('rendered_page_path')))
        sha = row.get('sha256', row.get('rendered_page_sha256'))
        need(pin(R / rel)['sha256'] == sha, 'Additional raw render-page pin')
        extra_render_hashes.append({'path': rel, **pin(R / rel)})
    components.append({'path': wrapper_pin['path'], **pin(wrapper_path), 'raw_path': wrapper['original_receipt']['path'],
                       'raw_sha256': pin(raw_path)['sha256'], 'first': first, 'last': last,
                       'contact_count': len(contacts), 'native_count': len(natives),
                       'native_projection_raw_indices': [projected_natives.index(row) for row in ordered_natives]})

need(coverage == visual['coverage'] and len(contact_rows) == 80 and len(native_rows) == 44, 'Aggregate component coverage/counts')
need([r['path'] for r in contact_rows] == [relative(x) for x in qa['contact_sheets']], 'Renderer contact order/closure')
native_page_numbers = sorted(int(Path(x['path']).stem.split('-')[1]) for x in native_rows)
need(native_page_numbers == visual['individually_viewed_pages'], 'Aggregate native page set')
need({row['path'] for row in extras if row['exact']} == {row['path'] for row in native_rows}, 'Exact44 native extras')
need(sum(row['exact'] for row in extras) == 44 and all(Path(row['path']).suffix == ('.png' if row['exact'] else Path(row['path']).suffix) for row in extras), 'Image exactness declaration')
needed_text = {x['path'] for x in visual['original_component_receipts']} | {x['path'].removesuffix('.json') + '.md' for x in visual['original_component_receipts']} | {'logbook/GAMMA_VISUAL_REVIEW_20260913.json', 'logbook/GAMMA_VISUAL_REVIEW_20260913.md'}
need({row['path'] for row in extras if not row['exact']} == needed_text, 'Exact10 text extras')

tree = ast.parse((work / 'gamma_edition_workflow_20260913.py').read_text(encoding='utf-8'))
alias_def = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'metadata_aliases')
ns = {'Path': Path, 'W': W, 'R': R, 're': re}
exec(compile(ast.fix_missing_locations(ast.Module(body=[alias_def], type_ignores=[])), '<pure-alias-review>', 'exec'), ns)
for component in components:
    wrapper_public = json.loads(ns['metadata_aliases']((R / component['path']).read_text(encoding='utf-8-sig')))
    raw_public = json.loads(ns['metadata_aliases']((R / component['raw_path']).read_text(encoding='utf-8-sig')))
    need(wrapper_public['original_review'] == raw_public, 'Public alias/raw embedding does not commute')
for rel in ('gamma_edition_spec_20260913.json', 'gamma_edition_independent_workflow_review_receipt_20260913.json'):
    original = (H / rel).read_bytes()
    need(ns['metadata_aliases'](original.decode('utf-8-sig')).encode('utf-8') == original, 'Public alias changes preserved critical spec/seal')
extras_pins = []
for row in extras:
    p = R / relative(row['path'])
    b = p.read_bytes()
    public = b if row['exact'] else ns['metadata_aliases'](b.decode('utf-8-sig')).encode('utf-8')
    if p.suffix == '.json':
        json.loads(public)
    extras_pins.append({**row, **pin(p), 'public_sha256': hashlib.sha256(public).hexdigest(), 'public_bytes': len(public), 'machine_metadata_aliased': b != public})

record = {'schema': 'gamma-final-visual-allowlist-readonly-evidence-v1', 'status': 'passed',
          'workflow': {'path': 'work/gamma_edition_workflow_20260913.py', **pin(work / 'gamma_edition_workflow_20260913.py')},
          'specification': {'path': 'work/gamma_edition_spec_20260913.json', **pin(work / 'gamma_edition_spec_20260913.json')},
          'original_specification': {'path': 'work/history/gamma_edition_pre_visual_20260913/gamma_edition_spec_20260913.json', **pin(H / 'gamma_edition_spec_20260913.json')},
          'preserved_history': historical,
          'allowlist_fragment': {'path': 'work/gamma_visual_public_files_fragment_20260913.json', **pin(work / 'gamma_visual_public_files_fragment_20260913.json')},
          'public_extras': extras_pins, 'components': components, 'contacts': contact_rows, 'native_pages': native_rows,
          'additional_raw_render_hashes_verified': extra_render_hashes,
          'proof_input_hashes_verified': len(build['tex_inputs']), 'whole_source_hashes_verified': len(build['source_notes']),
          'current_pdf': {'path': pdf.name, **pin(pdf), 'pages': 478},
          'aggregate_visual': {'path': 'build/qa/visual_review.json', **pin(visual_path)},
          'render_receipt': {'path': 'build/qa/qa_receipt.json', **pin(qa_path)},
          'final_source_audit': {'path': spec['source_audit'], **pin(R / spec['source_audit'])},
          'final_integration_review': {'path': spec['final_review'], **pin(R / spec['final_review'])},
          'coverage': coverage, 'individual_page_numbers': native_page_numbers,
          'public_alias_preserves_raw_embedding': True, 'preceding_spec_and_seal_unchanged_by_public_alias': True,
          'layout_observation_preserved': visual['recorded_nonblocking_layout_observation'],
          'new_images_visually_viewed_by_this_audit': 0, 'workflow_actions_executed': [], 'mathematical_checkers_executed': [],
          'scope': 'Read-only provenance/hash/image-file integrity/PDF-count audit of existing complete visual reviews; does not impersonate their recorded viewing actions.'}
out = work / 'gamma_edition_final_visual_allowlist_evidence_20260913.json'
out.write_text(json.dumps(record, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'status': record['status'], 'extras': len(extras), 'native_pages': len(native_rows), 'contacts': len(contact_rows),
                  'pdf_pages': 478, 'additional_raw_render_hashes': len(extra_render_hashes), 'evidence': out.name, **pin(out)}, indent=2))
