"""Read source trees; write this audit directory only. No PDF build or math replay."""
from pathlib import Path
from collections import Counter, defaultdict
import hashlib
import json
import re

ROOT = Path('workspace:/output/Tau_Theta_Hankel_Certification_2026-09-13/repository')
BASELINE = Path('workspace:/output/split_zero_rh_tandem_2026-09-12/current_source_20260913_periodized_residue')
OUT = Path(__file__).resolve().parent
ORDER = ['TC', 'WB', 'WBR', 'CH', 'TR', 'TT', 'GF', 'TCReview', 'RootAcceptance', 'GFR']


def content(path):
    return path.read_text(encoding='utf-8-sig')


def pin(path):
    data = path.read_bytes()
    return {'path': path.relative_to(ROOT).as_posix(), 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}


labels, tags = defaultdict(list), defaultdict(list)
bodies = []
bibkeys = set()
for key in ORDER:
    path = ROOT / ('proofs/TC.tex' if key == 'TC' else f'support_reader/typed/{key}.tex')
    text = content(path)
    row = pin(path)
    row.update(key=key, lines=len(text.splitlines()), environments=dict(Counter(re.findall(r'\\begin\{([^}]+)\}', text))))
    row['nested_inputs'] = re.findall(r'\\(?:input|include)\{([^}]+)\}', text)
    row['references'] = re.findall(r'\\(?:ref|eqref|pageref|autoref|cref|Cref)\*?\{([^}]+)\}', text)
    row['tags'] = re.findall(r'\\tag\*?\{([^}]+)\}', text)
    row['labels'] = re.findall(r'\\label\{([^}]+)\}', text)
    row['control_words'] = sorted(set(re.findall(r'\\([A-Za-z]+)', text)))
    row['non_ascii_characters'] = sorted(set(c for c in text if ord(c) > 127))
    row['definitions'] = [line for line in text.splitlines() if re.search(r'\\(?:newcommand|renewcommand|providecommand|newtheorem|DeclareMathOperator|def)\b', line)]
    row['bibliography_keys'] = re.findall(r'\\bibitem(?:\[[^]]*\])?\{([^}]+)\}', text)
    bibkeys.update(row['bibliography_keys'])
    bodies.append(row)
    for kind, destination in [('label', labels), ('tag', tags)]:
        for match in re.finditer(r'\\' + kind + r'\*?\{([^}]+)\}', text):
            destination[match.group(1)].append({'file': row['path'], 'line': text[:match.start()].count('\n') + 1})

baseline_label_collisions = []
baseline_bib_collisions = []
baseline_file_count = 0
for path in BASELINE.rglob('*.tex'):
    baseline_file_count += 1
    text = content(path)
    for match in re.finditer(r'\\label\{([^}]+)\}', text):
        if match.group(1) in labels:
            baseline_label_collisions.append({'label': match.group(1), 'file': path.relative_to(BASELINE).as_posix(), 'line': text[:match.start()].count('\n') + 1})
    for match in re.finditer(r'\\bibitem(?:\[[^]]*\])?\{([^}]+)\}', text):
        if match.group(1) in bibkeys:
            baseline_bib_collisions.append({'key': match.group(1), 'file': path.relative_to(BASELINE).as_posix(), 'line': text[:match.start()].count('\n') + 1})

manifest = json.loads(content(ROOT / 'MANIFEST.json'))
manifest_failures = []
for expected in manifest['files']:
    path = ROOT / expected['path']
    if not path.is_file():
        manifest_failures.append({'path': expected['path'], 'reason': 'missing'})
    elif pin(path) != expected:
        manifest_failures.append({'expected': expected, 'actual': pin(path)})

preservation = json.loads(content(ROOT / 'support_reader/conversion/SOURCE_PRESERVATION.json'))
source_preservation_failures = []
for source in preservation['sources']:
    for kind in ('original', 'typed'):
        expected = source[kind]
        path = ROOT / 'support_reader' / expected['path']
        actual = pin(path)
        if actual['bytes'] != expected['bytes'] or actual['sha256'] != expected['sha256']:
            source_preservation_failures.append({'key': source['key'], 'kind': kind, 'expected': expected, 'actual': actual})

report = {
    'schema': 'c47-read-only-inclusion-audit-v1',
    'root': ROOT.as_posix(),
    'baseline': BASELINE.as_posix(),
    'scope': 'Source inclusion and TeX compatibility audit only. No source edits, PDF build, integral replay, or new mathematical acceptance.',
    'body_count': len(bodies),
    'bodies_in_combined_reader_order': bodies,
    'tex_labels': dict(labels),
    'duplicate_labels': {k: v for k, v in labels.items() if len(v) > 1},
    'duplicate_displayed_tags': {k: v for k, v in tags.items() if len(v) > 1},
    'baseline_tex_files_scanned': baseline_file_count,
    'baseline_tree_label_collisions': baseline_label_collisions,
    'baseline_tree_bibliography_key_collisions': baseline_bib_collisions,
    'manifest_checked_files': len(manifest['files']),
    'manifest_failures': manifest_failures,
    'source_preservation_failures': source_preservation_failures,
    'dependency_source_pins': [pin(ROOT / f'dependencies/dependencies/{name}') for name in ['arithmetic_input.tex', 'HOCHSCHILD_COMPARISON.md', 'MATHEMATICAL_NOTE.md', 'DERIVED_MATHEMATICS.md']],
    'compatibility_additions_relative_to_821_preamble': ['listings package with breaklines and keepspaces', r'\R = \mathbb R', r'\C = \mathbb C', r'\Q = \mathbb Q'],
    'provenance_records': [pin(ROOT / rel) for rel in ['MANIFEST.json', 'evidence/TC_EXTRACTION.json', 'support_reader/conversion/SOURCE_PRESERVATION.json', 'support_reader/conversion/BUILD_RECEIPT.json', 'dependencies/TC_SOURCE_STAGING.json']],
}
(OUT / 'C47_INCLUSION_AUDIT.json').write_text(json.dumps(report, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
print(json.dumps({key: report[key] for key in ['body_count', 'baseline_tex_files_scanned', 'baseline_tree_label_collisions', 'baseline_tree_bibliography_key_collisions', 'manifest_checked_files', 'manifest_failures', 'source_preservation_failures']}))
