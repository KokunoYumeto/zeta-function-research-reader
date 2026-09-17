"""Read-only portable verification of the bounded public source package."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def checked(path, row):
    target = (ROOT/path).resolve()
    assert target.is_relative_to(ROOT), 'Unsafe path'
    raw = target.read_bytes()
    assert len(raw) == row['bytes'], path
    assert hashlib.sha256(raw).hexdigest() == row['sha256'], path
    return raw

def main():
    manifest = json.loads((ROOT/'FILE_MANIFEST.json').read_text(encoding='utf-8'))
    for row in manifest:
        checked(row['path'],row)
    derivation = json.loads((ROOT/'SOURCE_PINS_AND_PUBLIC_DERIVATION.json').read_text(encoding='utf-8'))
    exact = 0
    for row in derivation['files']:
        checked(row['public_path'],row['public'])
        if row['role'].startswith('accepted_exact_PDF') or row['role']=='complete_controlling_TeX':
            checked(row['public_path'],row['original'])
            exact += 1
    assert exact == 6
    index = json.loads((ROOT/'research_index/PROGRAM_INDEX.json').read_text(encoding='utf-8'))
    for row in index['sources'].values():
        checked(row['path'],row)
    print(json.dumps({'status':'passed','payload_files_verified':len(manifest),'exact_controlling_sources_and_PDFs':exact,'index_sources_verified':len(index['sources'])},indent=2))

if __name__ == '__main__':
    main()
