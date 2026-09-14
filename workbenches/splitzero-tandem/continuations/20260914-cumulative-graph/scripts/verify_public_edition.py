"""Read-only verification of the exact built edition, not a new proof review."""
from pathlib import Path
import gzip, hashlib, json

ROOT = Path(__file__).resolve().parents[1]

def need(ok, message):
    if not ok:
        raise RuntimeError(message)

def pin(path):
    h = hashlib.sha256(); size = 0
    with path.open('rb') as f:
        for b in iter(lambda: f.read(1048576), b''):
            h.update(b); size += len(b)
    return {'bytes': size, 'sha256': h.hexdigest()}

def read(name):
    return json.loads((ROOT / name).read_bytes())

def pointer(obj, route):
    need(route.startswith('/'), 'Invalid review JSON pointer')
    for key in route.split('/')[1:]:
        key = key.replace('~1', '/').replace('~0', '~')
        obj = obj[int(key)] if isinstance(obj, list) else obj[key]
    return obj

def main():
    manifest = read('CURRENT_SOURCE_MANIFEST.json')
    need(manifest['schema'] == 'public-source-built-files-v1', 'Not a built-edition manifest')
    actual = {p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*') if p.is_file()}
    need(actual == set(manifest['files']) | {'CURRENT_SOURCE_MANIFEST.json'}, 'File membership differs')
    for name, row in manifest['files'].items():
        need(pin(ROOT / name) == row, 'Changed public file: ' + name)
    current = read('provenance/CURRENT_COMPILED_SOURCE_PINS.json')['files']
    expected = read('provenance/ASSEMBLED_SOURCE_EXPECTATIONS.json')['files']
    build = read('build/CURRENT_BUILD_RECEIPT.json')
    acceptance = read('validation/PUBLIC_SOURCE_ACCEPTANCE.json')
    visual = read('validation/PUBLIC_PDF_VISUAL_ACCEPTANCE.json')
    derivation = read('PUBLIC_DERIVATION.json')
    need(len(current) == 279 and current == expected == build['compiled_sources'], 'Compiler closure differs')
    need(all(manifest['files'][n] == r for n, r in current.items()), 'Compiler inputs not bound')
    need(build['status'] == 'compiled-current-revised-source' and not build['source_preparation_replayed'], 'Wrong build route')
    need(not any(build['warnings'].values()), 'Unexpected build warnings')
    need(acceptance['status'] == 'PASS_LOCAL_BUILT_SOURCE_AND_VISUAL_BINDING', 'Source acceptance status')
    need(visual['status'] == 'ROOT_VISUAL_ACCEPTANCE_BOUND', 'Visual acceptance status')
    pdf = acceptance['pdf']
    need(pin(ROOT / pdf['path']) == {k: pdf[k] for k in ('bytes', 'sha256')}, 'PDF identity differs')
    need((build['pdf_sha256'], build['pdf_bytes'], build['pages']) == (pdf['sha256'], pdf['bytes'], pdf['pages']), 'Build/PDF binding differs')
    need(visual['pdf'] == pdf and acceptance['compiled_inputs'] == 279, 'Visual/PDF or source count mismatch')
    for row in visual['evidence']:
        need(pin(ROOT / row['public_path']) == row['public'], 'Visual evidence changed')
    reviewed = read(visual['evidence'][0]['public_path'])
    need(pointer(reviewed, visual['root_status_pointer']) == visual['root_accepted_status'], 'Root acceptance status differs')
    need(pointer(reviewed, visual['root_pdf_sha256_pointer']) == pdf['sha256'], 'Root reviewed another PDF')
    need(reviewed['all_pages_covered'] and reviewed['pages'] == pdf['pages'], 'Review coverage differs')
    need(reviewed['successful_current_build_receipt_sha256'] == acceptance['build']['original']['sha256'], 'Root/build original receipt mismatch')
    history = {r['previous_path']: r for r in derivation['preserved_predecessor_paths']}
    for row in read(derivation['baseline']['inventory']):
        target = history[row['path']]['preserved_path'] if row['path'] in history else row['path']
        need(pin(ROOT / target) == {k: row[k] for k in ('bytes', 'sha256')}, 'Accepted baseline not retained: ' + row['path'])
    for row in derivation['selected_source_dispositions']:
        if row['public_path'] is not None:
            need(pin(ROOT / row['public_path']) == row['public'], 'Selected dependency changed')
    for name, row in derivation['compiler']['default_builders'].items():
        need(pin(ROOT / name) == row, 'Fixed builder changed')
    for row in read('PUBLIC_REPRESENTATIONS.json')['representations']:
        stored = ROOT / row['stored_public_path']
        need(pin(stored) == row['compressed'], 'Historical representation changed')
        h = hashlib.sha256(); size = 0
        with gzip.open(stored, 'rb') as f:
            for b in iter(lambda: f.read(1048576), b''):
                h.update(b); size += len(b)
        need({'bytes': size, 'sha256': h.hexdigest()} == row['decompressed'], 'Historical decompression differs')
    print(json.dumps({'status': 'PASS_LOCAL_BUILT_PUBLIC_EDITION', 'files': len(actual), 'compiled_inputs': 279,
                      'pdf': pdf, 'new_mathematical_or_Lean_verification': False, 'remote_publication': False}))

if __name__ == '__main__':
    main()
