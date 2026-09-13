"""Read-only closure and in-memory alias audit; never imports or runs workflow actions."""
from pathlib import Path
import ast
import collections
import hashlib
import json
import re
import zipfile

W = Path(__file__).resolve().parents[1]
R = W / 'output/split_zero_rh_tandem_2026-09-12'
work = W / 'work'

def read(p):
    return json.loads(p.read_text(encoding='utf-8-sig'))

def pin(p):
    b = p.read_bytes()
    return {'sha256': hashlib.sha256(b).hexdigest(), 'bytes': len(b)}

def require(ok, message):
    if not ok:
        raise RuntimeError(message)

workflow = work / 'gamma_edition_workflow_20260913.py'
source = workflow.read_text(encoding='utf-8')
tree = ast.parse(source)
alias_def = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'metadata_aliases')
alias_ns = {'Path': Path, 'W': W, 'R': R, 're': re}
exec(compile(ast.fix_missing_locations(ast.Module(body=[alias_def], type_ignores=[])),
             '<reviewed-pure-metadata-function>', 'exec'), alias_ns)
alias = alias_ns['metadata_aliases']
spec = read(work / 'gamma_edition_spec_20260913.json')
inventory = read(work / spec['support_inventory'])
job_document = read(work / spec['portable_jobs_file'])
jobs = job_document['jobs']
base = R / spec['base_directory']
manifest = read(base / 'PUBLIC_SOURCE_MANIFEST.json')
base_names = {row['path'] for row in manifest['files']} | set(spec['base_pins'])
actual_names = set()
for p in base.rglob('*'):
    require(not p.is_symlink() and not p.is_junction(), 'Linked baseline entry')
    if p.is_file():
        actual_names.add(p.relative_to(base).as_posix())
require(actual_names == base_names and len(actual_names) == 946, 'Baseline membership')
for row in manifest['files']:
    require(pin(base / row['path']) == {k: row[k] for k in ('sha256', 'bytes')}, 'Baseline bytes: ' + row['path'])
for rel, sha in spec['base_pins'].items():
    require(pin(base / rel)['sha256'] == sha, 'Baseline special: ' + rel)
authority = read(R / spec['base_verification'])
require(authority['commit'] == spec['base_commit'], 'H actual own commit')
require(authority['public_manifest_sha256'] == spec['base_pins']['PUBLIC_SOURCE_MANIFEST.json'], 'H authority manifest')
require(set(authority['verified_files']) == actual_names, 'H authority full membership')
for rel, row in authority['verified_files'].items():
    require(pin(base / rel) == {k: row[k] for k in ('sha256', 'bytes')}, 'H authority member: ' + rel)

rows = inventory['files']
names = [row['archive_path'] for row in rows]
require(len(rows) == inventory['support_count'] == 249, 'Support count')
require(len(set(x.casefold() for x in names)) == len(names), 'Support collision')
support_reports = []
changed = set()
for row in rows:
    rel = row['archive_path']
    p = R / rel
    require(pin(p) == {k: row[k] for k in ('sha256', 'bytes')}, 'Support pin: ' + rel)
    require(not p.is_symlink() and not p.is_junction(), 'Linked support')
    data = p.read_bytes()
    exact = p.suffix in ('.tex', '.py', '.png', '.pdf') and not row.get('contains_native_execution_locator', False)
    public = data
    if not exact and (p.suffix in ('.json', '.md', '.txt', '.log') or rel in spec['aliased_native_helpers']):
        public = alias(data.decode('utf-8-sig')).encode('utf-8')
    if public != data:
        changed.add(rel)
    if p.suffix == '.json':
        json.loads(public)
    if p.suffix not in ('.zip', '.pdf', '.png', '.jpg'):
        require(W.parts[2].casefold() not in public.decode('utf-8', errors='replace').casefold(), 'Unaliased account text: ' + rel)
    support_reports.append({'path': rel, **pin(p), 'exact_staging': exact,
                            'aliased_sha256': hashlib.sha256(public).hexdigest(), 'bytes_changed': public != data})

closure = set(names) | {x['path'] for x in spec['public_files']}
job_inputs = set()
for job in jobs:
    rel = job['script']
    job_inputs.add(rel)
    if job.get('script_sha256'):
        require(pin(R / rel)['sha256'] == job['script_sha256'], 'Script pin: ' + job['label'])
    for rel in job.get('companion_files', []):
        if isinstance(rel, dict):
            rel = rel['path']
        job_inputs.add(rel)
        require((R / rel).is_file(), 'Missing companion: ' + rel)
    for rel in job.get('hash_fields', {}).values():
        rel = rel.replace('{support}', spec['support_directory']).replace('{delivery}', spec['delivery_directory'])
        job_inputs.add(rel)
        require((R / rel).is_file(), 'Missing hash input: ' + rel)
require(not (changed & job_inputs), 'Aliasing changes an actual checker/companion input')
for package in spec['source_packages']:
    p = R / package['stage'] / package['archive']
    require(pin(p)['sha256'] == package['sha256'], 'Original archive pin')
    require(pin(p)['bytes'] == package['bytes'], 'Original archive size')
    with zipfile.ZipFile(p) as archive:
        members = [i for i in archive.infolist() if not i.is_dir()]
        require(len(members) == package['members'], 'Original archive member count')
        for item in members:
            destination = p.parent / item.filename
            require(destination.read_bytes() == archive.read(item), 'Original delivery member: ' + item.filename)

proof_pins = []
for rel, sha in spec['pinned_files'].items():
    p = W / rel if rel.startswith('work/') else R / rel
    require(pin(p)['sha256'] == sha, 'Declared source/dependency pin: ' + rel)
    proof_pins.append({'path': rel, **pin(p)})
files = ['gamma_edition_workflow_20260913.py', 'gamma_edition_spec_20260913.json',
         'GAMMA_EDITION_WORKFLOW_20260913.md', spec['support_inventory'], spec['portable_jobs_file'],
         'gamma_edition_workflow_static_checks_20260913.json', 'cyclic_publication_contract_20260912.py']
report = {'schema': 'gamma-edition-independent-readonly-audit-v1', 'status': 'passed',
          'reviewed_files': [{'path': 'work/' + f, **pin(work / f)} for f in files],
          'baseline_files_verified': len(actual_names), 'support_files_verified': len(rows),
          'original_archive_members_verified': len(members), 'jobs_declared': len(jobs),
          'normal_optimized_pairs': len(job_document['normal_optimized_pairs']),
          'actual_checker_or_companion_paths': sorted(job_inputs),
          'actual_checker_or_companion_aliased': [],
          'public_metadata_changes': sorted(changed), 'support': support_reports,
          'pinned_dependencies': proof_pins,
          'runtime_profiles': dict(collections.Counter(j['runtime_profile'] for j in jobs)),
          'output_contracts': dict(collections.Counter(j['output_kind'] for j in jobs)),
          'workflow_actions_executed': [], 'mathematical_checkers_executed': [],
          'scope': 'Read-only complete H/support/archive hash audit and in-memory public alias transformation; source review separately states the execution limits.'}
out = work / 'gamma_edition_independent_readonly_audit_20260913.json'
out.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
print(json.dumps({k: v for k, v in report.items() if k not in ('support', 'actual_checker_or_companion_paths', 'pinned_dependencies', 'reviewed_files')}, indent=2))
