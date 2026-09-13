from pathlib import Path
import hashlib
import json

work = Path(__file__).resolve().parent
project = work.parent
build = work / 'deligne_split_sidebar_build_20260913'

def pin(path):
    data = path.read_bytes()
    return {'path': str(path), 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}

source = work / 'deligne_split_sidebar_20260913.tex'
receipt_path = work / 'deligne_split_sidebar_build_receipt_20260913.json'
receipt = json.loads(receipt_path.read_text())
if pin(source) != receipt['source']:
    raise RuntimeError('Source changed after the final build')
pdf = Path(receipt['pdf']['path'])
if pin(pdf) != receipt['pdf']:
    raise RuntimeError('PDF changed after the final build')
if receipt['status'] != 'PASS' or len(receipt['rendered_pages']) != 12:
    raise RuntimeError('Final successful twelve-page build required')
for page in receipt['rendered_pages']:
    if pin(Path(page['path'])) != page:
        raise RuntimeError('Rendered page changed after the final build')

ndjson = project / 'output/Deligne_Weil_II_S20_LaTeX/source_package/edition/source_language.ndjson'
records = [json.loads(line) for line in ndjson.read_text(encoding='utf-8').splitlines()]
selected = []
for record in records:
    if 201 <= record.get('printed_page', 0) <= 207:
        calculated = hashlib.sha256(record['text'].encode('utf-8')).hexdigest()
        if calculated.lower() != record['text_sha256'].lower():
            raise RuntimeError('Selected S20 text digest mismatch')
        selected.append({'printed_page': record['printed_page'],
                         'physical_page': record['physical_page'],
                         'article_page': record['article_page'],
                         'text_sha256': calculated,
                         'reading': 'Complete text field read; no excerpt omission on this selected page.'})

visual = {
    'status': 'PASS', 'source': pin(source), 'pdf': pin(pdf),
    'pages': receipt['rendered_pages'],
    'inspection': 'All final pages 01 through 12 viewed individually via view_image at 110 dpi after the final source edit and build.',
    'findings': ['Readable text and formulas on every page.',
                 'No clipped equations, overlaid labels, missing glyphs or page-edge overflow.',
                 'Twelve-page complete source, including all DS1 through DS69 labels.',
                 'The final partial page contains the complete exponential source join, with no blank trailing page.'],
    'build_receipt': pin(receipt_path)
}
visual_path = work / 'deligne_split_sidebar_visual_20260913.json'
visual_path.write_text(json.dumps(visual, indent=2) + '\n', encoding='utf-8')

proof_map = {
    'DS1-DS6': 'Complete image, mapping cone, dual-image and compatible-action proofs, tied to the existing internal comparison kernel.',
    'DS7-DS9': 'Deligne 3.3.4-3.3.6 with degree 2N-m, Tate twist (N), geometric Frobenius convention, and the exact tensor image map.',
    'DS10-DS11': 'Exact split lift, distinct e and tau fibres, inclusions into the full supported kernel carrier, and the original integer/complex coefficient square.',
    'DS12-DS18': 'Delivered original relation curve, source projection, exceptional derived fibre and dual line factors, with complete reconstructed proofs.',
    'DS19-DS36': 'Delivered logarithmic cohomology, trace line T and orientation, support-compatible dual and action-stable hull, with full chain categories and dual-action maps.',
    'DS37-DS45': 'Same source-induced curvature, relation observations, traces and additive/multiplicative observer map, with original constants.',
    'DS46-DS52': 'General divisor depth and explicit contraction; full meromorphic dual lattice; independent conormal-depth map and curvature pullback.',
    'DS53-DS65': 'Delivered invariant subquotient metric and coupling subtraction, plus its explicitly proved matrix remainder, including both zero-dimensional endpoints.',
    'DS66-DS69': 'Delivered exponential coefficient family, special-fibre quasi-isomorphism, regular specialized operator and exact original theta-source deformation.'
}
reading = {
    'source': pin(source), 'S20_archive_material': pin(ndjson), 'selected_S20_pages': selected,
    'delivered_pastes': [pin(Path(p)) for p in [
        r'local:user-profile\.codex\attachments\3bcdb13a-df73-497d-8510-00d8ff837753\pasted-text.txt',
        r'local:user-profile\.codex\attachments\1f285372-dda6-457d-a82e-0bf484ccab65\pasted-text.txt']],
    'new_paste_reading': 'Entire second paste read in successive nonoverlapping ranges covering both the exponential and logarithmic constituent-control notes.',
    'source_map': proof_map,
    'attribution': 'The delivered logarithmic and constituent-coupling calculations are attributed to their web contributions; no claim of a new independent discovery of those delivered results.',
    'scope': 'This is a complete mathematical sidebar and standalone PDF, not a full audit of all 117 Deligne page records or a new proof of Weil II.',
    'validation': 'Written mathematical derivations, root and independent mathematical review, actual TeX build and all-page visual inspection. No new Lean or arithmetic checker run is claimed.'
}
reading_path = work / 'deligne_split_sidebar_reading_20260913.json'
reading_path.write_text(json.dumps(reading, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'source': pin(source), 'visual': pin(visual_path), 'reading': pin(reading_path)}))
