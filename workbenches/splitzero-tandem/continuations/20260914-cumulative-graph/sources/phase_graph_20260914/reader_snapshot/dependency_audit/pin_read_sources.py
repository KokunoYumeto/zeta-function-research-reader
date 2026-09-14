from pathlib import Path
import hashlib
import json
import re

math = Path(r'workspace:')
wave = math / 'work/backpropagation_20260913'
intake = wave / 'next_phase_graph_intake'
out = intake / 'reader/dependency_audit'
dep = json.loads((intake / 'source_snapshot/SOURCE_DEPENDENCIES.json').read_text(encoding='utf-8'))
entries = []
for item in dep['files']:
    p = Path(item['path'])
    data = p.read_bytes()
    actual = hashlib.sha256(data).hexdigest()
    entries.append({**item, 'current_bytes': len(data), 'current_sha256': actual,
                    'matches_declared': len(data) == item['bytes'] and actual == item['sha256'],
                    'reading': 'complete proof body read'})

extra = [
 ('PGS', intake / 'source_snapshot/phase_graph_schur.tex'),
 ('PGD', intake / 'source_snapshot/density_bounds.tex'),
 ('PGM sealed v2', intake / 'source_snapshot/strict_mixed_residual_v2.tex'),
 ('PGB', intake / 'phase_graph_averaged_bridge.tex'),
 ('PGMB', intake / 'mixed_residual_completion_addendum.tex'),
 ('accepted HCD raw', wave / 'cumulative_source_v1/sources/holonomy_complete_closure/companion/originals/HCD.tex'),
 ('original full holonomy NOTE', wave / 'cumulative_source_v1/sources/holonomy_complete_closure/companion/originals/H_NOTE.tex'),
 ('PSD', wave / 'cumulative_source_v1/sources/holonomy_complete_closure/companion/dependencies/finite_circle/proofs/PSD.tex'),
 ('original arithmetic input', wave / 'cumulative_source_v1/sources/holonomy_complete_closure/companion/dependencies/finite_circle/inherited/arithmetic_input.tex'),
 ('HCA', math / 'work/rh_counterfactual_20260913/total_object/certified_hankel_attachment.tex'),
 ('LHT', math / 'work/rh_counterfactual_20260913/total_object/quartet_critical_values/low_height_theta.tex'),
]
for role, p in extra:
    data = p.read_bytes()
    entries.append({'role': role, 'path': str(p), 'current_bytes': len(data),
                    'current_sha256': hashlib.sha256(data).hexdigest(),
                    'reading': 'complete proof body read'})

labels = {}
refs = []
for item in entries:
    text = Path(item['path']).read_text(encoding='utf-8-sig')
    for line, content in enumerate(text.splitlines(), 1):
        for label in re.findall(r'\\label\{([^}]+)\}', content):
            labels.setdefault(label, []).append({'path': item['path'], 'line': line})
        for label in re.findall(r'\\(?:eqref|ref|pageref)\{([^}]+)\}', content):
            refs.append({'label': label, 'path': item['path'], 'line': line})

report = {
 'scope': 'Bounded source dependency and full-reading record. Not a proof acceptance of every historical appendix assertion.',
 'date': '2026-09-14',
 'full_read_count': len(entries),
 'declared_ten_match': all(x['matches_declared'] for x in entries if 'matches_declared' in x),
 'sources': entries,
 'duplicate_literal_labels': {k:v for k,v in labels.items() if len(v)>1},
 'unresolved_literal_tex_references': [r for r in refs if r['label'] not in labels],
 'reference_scan_limit': 'Names cited as prose such as HCA.5 and AT22 are not captured by this regex. Consult DEPENDENCY_FINDINGS.md.',
 'findings_sha256': hashlib.sha256((out / 'DEPENDENCY_FINDINGS.md').read_bytes()).hexdigest(),
}
(out / 'READING_AND_PIN_RECEIPT.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'full_read_count': len(entries), 'declared_ten_match': report['declared_ten_match'],
                  'duplicate_labels': len(report['duplicate_literal_labels']),
                  'unresolved_literal_tex_references': len(report['unresolved_literal_tex_references']),
                  'findings_sha256': report['findings_sha256']}, indent=2))
