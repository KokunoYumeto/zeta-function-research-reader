from pathlib import Path
import hashlib
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

ROOT = Path('workspace:')
OUT = Path(__file__).resolve().parent
LEDGER = ROOT / 'work/backpropagation_20260913/cohort_staging/snapshots/transcript/ledger_publication'
manifest_path = LEDGER / 'sources_manifest.json'
manifest = json.loads(manifest_path.read_text(encoding='utf-8-sig'))
sha = lambda b: hashlib.sha256(b).hexdigest()
patterns = {
    'inline_note_or_exponent_candidate': r'\^\[',
    'labelled_markdown_note_marker': r'\[\^',
    'tex_note_command': r'\\footnote(?:mark|text)?\b',
    'html_note_semantics': r'(?:role\s*=\s*[\"\']doc-(?:noteref|footnote)|class\s*=\s*[\"\'][^\"\']*footnote)',
}
files = []
for m in manifest:
    for role, path in [('packaged', LEDGER / m['packaged_path']), ('original', ROOT / m['original_relative_path'])]:
        rec = {'slug': m['slug'], 'role': role, 'path': path.relative_to(ROOT).as_posix(), 'expected_manifest_sha256': m['sha256'], 'expected_manifest_bytes': m['bytes'], 'exists': path.is_file()}
        if path.is_file():
            data = path.read_bytes()
            text = data.decode('utf-8-sig')
            rec.update(bytes=len(data), sha256=sha(data), matches_manifest_sha256=sha(data)==m['sha256'], matches_manifest_bytes=len(data)==m['bytes'])
            occurrences = []
            for kind, pattern in patterns.items():
                for match in re.finditer(pattern, text, flags=re.IGNORECASE):
                    pos = match.start()
                    start = text.rfind('\n', 0, pos) + 1
                    end = text.find('\n', pos)
                    if end < 0:
                        end = len(text)
                    occurrences.append({'kind': kind, 'line': text.count('\n', 0, pos)+1, 'column': pos-start+1, 'character_offset': pos, 'marker': match.group(), 'line_text': text[start:end], 'context_before': text[max(0, pos-200):pos], 'context_after': text[pos:min(len(text), pos+300)]})
            rec['occurrences'] = sorted(occurrences, key=lambda x:x['character_offset'])
            rec['marker_counts'] = {kind:sum(o['kind']==kind for o in occurrences) for kind in patterns}
        files.append(rec)
extra=[]
for name in ['build_ledger.py', 'layout.lua', 'ledger.md', 'ledger.tex']:
    path=LEDGER/name
    data=path.read_bytes()
    extra.append({'path':path.relative_to(ROOT).as_posix(), 'bytes':len(data), 'sha256':sha(data)})
receipt={'scope':'12 manifest entries, each packaged Markdown source and workspace-original source; frozen converter and combined ledger inspected separately.', 'manifest_path':manifest_path.relative_to(ROOT).as_posix(), 'manifest_sha256':sha(manifest_path.read_bytes()), 'entry_count':len(manifest), 'source_file_count':len(files), 'files':files, 'additional_inputs':extra, 'missing_files':[x['path'] for x in files if not x['exists']], 'mismatched_source_hashes':[x['path'] for x in files if x['exists'] and not x['matches_manifest_sha256']]}
(OUT/'SOURCE_SCAN.json').write_text(json.dumps(receipt,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps({'entry_count':len(manifest), 'source_file_count':len(files), 'missing_files':receipt['missing_files'], 'mismatched_source_hashes':receipt['mismatched_source_hashes'], 'manifest_sha256':receipt['manifest_sha256']},indent=2))
for f in files:
    if f['role']=='packaged':
        print(f"{f['slug']}: {f['marker_counts']}")
        for o in f['occurrences']:
            print(f"  {o['line']}:{o['column']} {o['kind']}: {o['line_text']}")
