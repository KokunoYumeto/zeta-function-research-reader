"""Read-only package validation; writes only its own work-directory receipt.

This does not collect, stage, replay, freeze, publish, run mathematics, or alter R.
"""
from pathlib import Path
import hashlib
import importlib.util
import json
import re
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
SOURCE = HERE / 'gamma_edition_workflow_20260913.py'
SPEC = HERE / 'gamma_edition_spec_20260913.json'
checks = []


def check(name, condition):
    checks.append({'name': name, 'passed': bool(condition)})
    if not condition:
        raise RuntimeError('Static workflow check failed: ' + name)


compile(SOURCE.read_text(encoding='utf-8'), str(SOURCE), 'exec')
module_spec = importlib.util.spec_from_file_location('gamma_workflow_static_target', SOURCE)
workflow = importlib.util.module_from_spec(module_spec)
module_spec.loader.exec_module(workflow)
spec = workflow.edition(SPEC)
base, manifest, build, files = workflow.baseline(spec)
check('all exact H members', len(files) == 946)
check('H proof sections and inputs', len(build['tex_inputs']) == 39)
check('H complete sources', len(build['source_notes']) == 18)
check('H actual own commit', spec['base_commit'] == '16fc4dbb817b82023c6126e636f1c6df28d4cecd')
check('new complete proof count', len(spec['new_proofs']) == 5 and len(set(build['tex_inputs']) | {'tex/'+n+'.tex' for n in spec['new_proofs']}) == 44)
members = workflow.paths.package_members(spec)
check('exact original archive plus provenance', len(members) == 40)
support = workflow.read(HERE / spec['support_inventory'])
for row in support['files']:
    source = HERE / row['path']
    check('support bytes ' + row['path'], source.stat().st_size == row['bytes'] and workflow.paths.sha(source) == row['sha256'])
for row in support['proofs_handled_by_PROOFS']:
    check('original proof bytes ' + row['path'], workflow.paths.sha(HERE / row['path']) == row['sha256'])
jobs = workflow.read(HERE / spec['portable_jobs_file'])
check('full declared replay membership', len(jobs['jobs']) == jobs['job_count'] == spec['expected_portable_jobs'] == 65)
check('primary and independent counts', jobs['primary_jobs'] == 60 and jobs['independent_jobs'] == 5)
check('comparison pair count', len(jobs['normal_optimized_pairs']) == 29)
index = {job['label']: job for job in jobs['jobs']}
workflow.unique(list(index), 'job labels')
check('unique labels', len(index) == 65)
allowed_outputs = {'json-option', 'absent', 'stdout-json', 'fixed-sibling-json', 'stdout-text'}
allowed_profiles = {'sympy-1.14.0', 'sympy-1.13.1', 'python-flint-0.9.0', 'python-stdlib'}
known = set(files) | {r['archive_path'] for r in support['files']} | {r['path'] for r in spec['public_files']}
known |= {'work/' + name for name in spec['work_files']} | {m['path'] for m in members}
for job in jobs['jobs']:
    label = job['label']
    check('known script ' + label, job['script'] in known)
    if job['script'].startswith(spec['support_directory'] + '/'):
        source = HERE / job['script'].removeprefix(spec['support_directory'] + '/')
    else:
        source = workflow.paths.contained(workflow.R, job['script'])
    check('checker pin ' + label, source.is_file() and (not job.get('script_sha256') or workflow.paths.sha(source) == job['script_sha256']))
    check('output/runtime contract ' + label, job['output_kind'] in allowed_outputs and job['runtime_profile'] in allowed_profiles)
    check('companions retained ' + label, all(name in known for name in job['companion_files']))
    expanded = [arg.replace('{support}', 'support').replace('{delivery}', 'delivery').replace('{output}', 'result.json') for arg in job['args']]
    check('relative arguments ' + label, all(not re.search(r'[A-Za-z]:[\\/]|^[/\\]', arg) for arg in expanded))
    check('assertion optimization scope ' + label, not (job.get('optimized_execution_forbidden') and job['optimized']))
    if job['output_kind'] == 'absent':
        check('exact guard rejection ' + label, job['expected_exit_code'] == 1 and bool(job['stderr_contains']))
for pair in jobs['normal_optimized_pairs']:
    left, right = index[pair['left']], index[pair['right']]
    check('pair same calculation ' + pair['left'], left['script'] == right['script'] and left['args'] == right['args'] and not left['optimized'] and right['optimized'])
    check('pair ignore only observed mode ' + pair['left'], set(pair['ignore_fields']).issubset({'optimization_flag', 'python_optimized', 'optimized_python'}))
check('new helper dependency explicitly packaged', 'cyclic_publication_contract_20260912.py' in spec['work_files'])
check('public exact checker sources omit native account locators', all(Path.home().name.casefold() not in (HERE / row['path']).read_text(encoding='utf-8-sig').casefold() for row in support['files'] if row['path'].endswith('.py') and not row.get('contains_native_execution_locator')))
for rel in spec['aliased_native_helpers']:
    original = (HERE / rel.removeprefix(spec['support_directory'] + '/')).read_text(encoding='utf-8-sig')
    changed = workflow.metadata_aliases(original)
    check('native helper aliases ' + rel, changed != original and Path.home().name.casefold() not in changed.casefold())
check('unchanged exact H snapshot after read-only check', workflow.snapshot(base) == files)
receipt = {'schema': 'gamma-edition-readonly-static-checks-v1', 'status': 'passed',
           'source_sha256': workflow.paths.sha(SOURCE), 'spec_sha256': workflow.paths.sha(SPEC),
           'jobs_sha256': workflow.paths.sha(HERE / spec['portable_jobs_file']),
           'support_inventory_sha256': workflow.paths.sha(HERE / spec['support_inventory']),
           'checks': checks, 'check_count': len(checks), 'H_files_verified': 946,
           'collect_executed': False, 'stage_executed': False, 'replay_executed': False,
           'freeze_executed': False, 'publication_executed': False,
           'scope': 'Syntax, exact H/archive/support source membership, concrete replay contracts and path aliases only. No new mathematical execution or publication.'}
target = HERE / 'gamma_edition_workflow_static_checks_20260913.json'
target.write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'status': 'passed', 'checks': len(checks), 'receipt': target.name}))
