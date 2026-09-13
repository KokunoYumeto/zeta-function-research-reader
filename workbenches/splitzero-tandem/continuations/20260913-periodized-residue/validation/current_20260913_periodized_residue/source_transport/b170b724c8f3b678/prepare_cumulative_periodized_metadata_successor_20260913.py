"""Create a new WORK-only metadata successor of an already compiled reader.

Only the public source-selection JSON may differ in the copied workspace.
The existing source planner emits the successor PLAN; no compile, render,
mathematical checker, promotion command, or remote operation is available.
Importing this module performs no work.
"""
from __future__ import annotations
import argparse
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import shutil

WORK = Path(__file__).resolve().parent
SELECTOR = 'sources/periodized_residue_complete_closure/integration/PUBLIC_SOURCE_SELECTION.json'
INVENTORY_SHA = '032f63ec9650ca4ebe2c0e18e3785a6359e730abd965ba23b593ac106f12010d'
OLD_SELECTOR_SHA = '0b70df8b0710b073c9c389191ecf0dcb0c341331372827b3184dd227aaf9bd14'
PDF_NAME = 'Split_Zero_Cohomology_and_Arithmetic_Weight_Control.pdf'
PDF_SHA = 'fa24ff486c02da2c4e3a66389a148faff7c0024bbca319e8f3e4625f647bd855'

def need(condition, message):
    if not condition:
        raise RuntimeError(message)

def byte_pin(data):
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}

def pin(path):
    h = hashlib.sha256()
    size = 0
    with Path(path).open('rb') as f:
        for b in iter(lambda: f.read(1024 * 1024), b''):
            h.update(b)
            size += len(b)
    return {'bytes': size, 'sha256': h.hexdigest()}

def full_pin(path):
    return {'path': str(Path(path).resolve()), **pin(path)}

def identity(row):
    return {k: row[k] for k in ('bytes', 'sha256')}

def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))

def encoded(value):
    return (json.dumps(value, indent=2, ensure_ascii=False) + '\n').encode('utf-8')

def write_new(path, data):
    path = Path(path)
    need(not path.exists(), 'Existing output must remain untouched: ' + str(path))
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('xb') as f:
        f.write(data)

def snapshot(root):
    root = Path(root).resolve()
    rows = {}
    for p in root.rglob('*'):
        if p.is_file():
            need(p.resolve().is_relative_to(root), 'Source tree contains an escaping path')
            rows[p.relative_to(root).as_posix()] = pin(p)
    return dict(sorted(rows.items()))

def load_module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def prepare(source_iteration, iteration, visual_receipt):
    need(source_iteration == 17 and iteration > source_iteration,
         'This correction requires the complete v17 predecessor and a fresh later WORK iteration.')
    old_source = WORK / f'cumulative_deligne_build_20260913_v{source_iteration}'
    old_inputs = WORK / f'cumulative_deligne_inputs_20260913_v{source_iteration}'
    old_plan_dir = WORK / f'cumulative_deligne_plan_20260913_v{source_iteration}'
    source = WORK / f'cumulative_deligne_build_20260913_v{iteration}'
    inputs = WORK / f'cumulative_deligne_inputs_20260913_v{iteration}'
    plan_dir = WORK / f'cumulative_deligne_plan_20260913_v{iteration}'
    for p in (source, inputs, plan_dir):
        need(p.resolve().parent == WORK.resolve() and not p.exists(), 'A fresh direct WORK destination is required: ' + str(p))
    inventory_path = WORK / 'cumulative_periodized_residue_source_input_20260913.json'
    need(pin(inventory_path)['sha256'] == INVENTORY_SHA, 'Final source inventory changed')
    inventory = read(inventory_path)
    old_plan_path = old_plan_dir / 'PLAN.json'
    old_plan = read(old_plan_path)
    old_verification_path = old_plan_dir / 'BUILD_VERIFICATION.json'
    old_verification = read(old_verification_path)
    need(old_verification['status'] == 'complete-endpoint-source-and-build-verified' and
         old_verification['plan_pin'] == pin(old_plan_path), 'Predecessor build verification mismatch')
    need(old_verification['pages'] == 821 and old_verification['pdf_pin']['sha256'] == PDF_SHA and
         old_verification['full_proof_bodies'] == 25 and
         old_verification['inherited_source_witnesses'] + old_verification['new_source_witnesses'] == 47,
         'Predecessor edition extent or PDF identity changed')
    need(pin(old_source / SELECTOR)['sha256'] == OLD_SELECTOR_SHA, 'Historical selector differs from the reviewed finding')
    visual_path = Path(visual_receipt).resolve()
    visual = read(visual_path)
    need(visual['status'] == 'all-pages-visually-accepted' and not visual.get('findings', []) and
         identity(visual['pdf']) == identity(old_verification['pdf_pin']) and
         visual.get('physical_pages', visual.get('pages')) == 821,
         'The exact complete visual acceptance is required for identity transport')
    preparer_path = WORK / 'prepare_cumulative_periodized_residue_reader_20260913.py'
    preparer = load_module(preparer_path, 'metadata_only_public_selector_preparer')
    public_record = preparer.public_source_selection(inventory)
    corrected_bytes = encoded(public_record)
    need(public_record['public_source_count'] == len(public_record['files']) == 351 and
         public_record['local_provenance_file_count_excluded'] == 57,
         'Public whitelist extent mismatch')
    forbidden_locator = str(Path.home().name).casefold()
    need(forbidden_locator not in corrected_bytes.decode('utf-8').casefold(),
         'A local user locator escaped the public metadata projection')
    for row in inventory['public_support_files'] + inventory['local_provenance_support_files']:
        need(pin(old_source / row['archive_path']) == identity(row), 'Predecessor archive row changed: ' + row['archive_path'])
    public_paths = {r['archive_path'] for r in public_record['files']}
    local_paths = {r['archive_path'] for r in inventory['local_provenance_support_files']}
    need(not public_paths.intersection(local_paths), 'Public selector contains local provenance')
    fourth = [r for r in public_record['public_selection_mappings']
              if r['selected_destination'].endswith('/fourth_jet_paper_audit.md')]
    need(len(fourth) == 1 and fourth[0]['bytes'] == 12559 and
         fourth[0]['sha256'] == '5050f2deee2dbb44e992b671d3551125b481b48e478cdbd26e595595a12f0bba',
         'Public fourth-jet mapping must identify the selected derivative')

    old_source_files = snapshot(old_source)
    old_input_files = snapshot(old_inputs)
    old_plan_files = snapshot(old_plan_dir)
    engine_path = WORK / 'endpoint_reader_integration_20260913.py'
    need(pin(engine_path) == old_plan['script_pin'], 'Accepted integration planner changed')
    engine = load_module(engine_path, 'metadata_only_existing_source_planner')
    engine.DEST = source
    old_config = read(old_inputs / 'INPUTS.json')
    need(engine.integration_configuration(old_config) == engine.integration_configuration(old_plan['configuration']),
         'Predecessor integration configuration changed')
    config = copy.deepcopy(old_config)
    rows = [r for r in config['additional_support_files'] if r['archive_path'] == SELECTOR]
    need(len(rows) == 1 and identity(rows[0]) == old_source_files[SELECTOR], 'Selector must have one exact input binding')
    original_binding = copy.deepcopy(rows[0])
    new_input_selector = inputs / 'source_snapshot' / SELECTOR
    rows[0].update({'path': str(new_input_selector), **byte_pin(corrected_bytes)})
    restored = copy.deepcopy(config)
    target = next(r for r in restored['additional_support_files'] if r['archive_path'] == SELECTOR)
    target.clear()
    target.update(original_binding)
    need(restored == old_config, 'Configuration changed beyond the one selector binding')

    # The first writes create only fresh WORK metadata inputs.
    write_new(new_input_selector, corrected_bytes)
    write_new(inputs / 'INPUTS.json', encoded(config))
    engine.plan(inputs / 'INPUTS.json', plan_dir)
    plan_path = plan_dir / 'PLAN.json'
    plan = read(plan_path)
    need(Path(plan['destination']).resolve() == source.resolve(), 'Successor PLAN destination mismatch')
    old_changes = {r['path']: r for r in old_plan['changes']}
    new_changes = {r['path']: r for r in plan['changes']}
    need(new_changes.keys() == old_changes.keys(), 'Metadata successor altered planned member membership')
    changed_planned = []
    for name, row in new_changes.items():
        proposed = pin(plan_dir / 'files' / name)
        need(proposed == row['after'], 'New PLAN does not describe its proposed bytes')
        if proposed != old_source_files[name]:
            changed_planned.append(name)
        if name != SELECTOR:
            need(row == old_changes[name] and proposed == old_source_files[name],
                 'A non-selector planned source would change: ' + name)
    need(changed_planned == [SELECTOR], 'The selector must be the sole changed planned payload')
    need(new_changes[SELECTOR]['before'] == old_changes[SELECTOR]['before'],
         'The immutable Gamma-I baseline before pin must remain unchanged')
    write_new(inputs / 'INSPECTION.json', encoded(plan['inspection']))

    # Copy the completed workspace, preserving all original compiler/QA artifacts.
    shutil.copytree(old_source, source)
    need(snapshot(source) == old_source_files, 'Completed workspace copy is not exact')
    with (source / SELECTOR).open('wb') as f:
        f.write(corrected_bytes)
    new_source_files = snapshot(source)
    expected_source_files = {**old_source_files, SELECTOR: byte_pin(corrected_bytes)}
    need(new_source_files == expected_source_files, 'Successor source delta exceeds the selector metadata')
    build = read(source / 'build/build_receipt.json')
    need(build['status'] == 'compiled' and build['pages'] == 821 and build['pdf_sha256'] == PDF_SHA,
         'Historical compiler receipt changed')
    compiled = {}
    for name, sha in build['tex_inputs'].items():
        need(name != SELECTOR and pin(source / name)['sha256'] == sha, 'Compiled input changed: ' + name)
        compiled[name] = pin(source / name)
    need(len(compiled) == 151 and len(build['source_notes']) == 47 and
         len({r['source'] for r in build['source_notes']}) == 47, 'Compiled input/witness extent changed')
    witnesses = []
    for row in build['source_notes']:
        need(pin(source / row['source'])['sha256'] == row['sha256'], 'Original witness changed')
        witnesses.append({'source': row['source'], **pin(source / row['source'])})
    for name in (PDF_NAME, 'build/reader.pdf'):
        need(pin(source / name) == identity(old_verification['pdf_pin']), 'PDF changed in metadata successor')
    need(snapshot(old_source) == old_source_files and snapshot(old_inputs) == old_input_files and
         snapshot(old_plan_dir) == old_plan_files, 'The original v17 source/input/plan tree changed')

    transport_path = plan_dir / 'METADATA_SUCCESSOR_TRANSPORT.json'
    transport = {'schema': 'exact-reader-metadata-successor-transport-v1',
        'status': 'metadata-only-successor-byte-identity-verified',
        'predecessor': {'workspace': str(old_source), 'plan': full_pin(old_plan_path),
                        'inputs': full_pin(old_inputs / 'INPUTS.json'),
                        'build_verification': full_pin(old_verification_path),
                        'applied': full_pin(old_plan_dir / 'APPLIED.json')},
        'successor': {'workspace': str(source), 'plan': full_pin(plan_path), 'inputs': full_pin(inputs / 'INPUTS.json')},
        'public_selection_correction': {'path': SELECTOR, 'before': old_source_files[SELECTOR],
            'after': byte_pin(corrected_bytes), 'public_files': 351, 'local_files_excluded': 57,
            'public_selected_mappings': 93, 'local_selected_mappings_excluded': 34,
            'fourth_jet_selected_public_pin': identity(fourth[0])},
        'configuration_delta': {'only_changed_archive_binding': SELECTOR, 'original_binding': original_binding,
                                'successor_binding': rows[0]},
        'source_file_count': len(new_source_files), 'source_delta_paths': [SELECTOR],
        'source_before': old_source_files, 'source_after': new_source_files,
        'predecessor_source_input_plan_trees_unchanged': True,
        'historical_compiler_receipt': full_pin(source / 'build/build_receipt.json'),
        'historical_source_receipt': full_pin(source / 'build/source_receipt.json'),
        'historical_page_qa_receipt': full_pin(source / 'build/qa/qa_receipt.json'),
        'pdf': {'path': str(source / PDF_NAME), 'pages': 821, **pin(source / PDF_NAME)},
        'compiled_inputs': compiled, 'compiled_input_count': len(compiled),
        'original_source_witnesses': witnesses, 'original_source_witness_count': len(witnesses),
        'unchanged_full_visual_acceptance': full_pin(visual_path),
        'build_performed': False, 'render_performed': False, 'mathematical_jobs_reexecuted': 0,
        'current_or_frozen_artifacts_mutated': False, 'promotion_performed': False,
        'input_inventory': full_pin(inventory_path), 'corrected_selector_generator': full_pin(preparer_path),
        'successor_preparation_script': full_pin(Path(__file__))}
    write_new(transport_path, encoded(transport))
    applied = copy.deepcopy(read(old_plan_dir / 'APPLIED.json'))
    applied['plan_pin'] = pin(plan_path)
    applied['workspace'] = str(source)
    applied['complete_applied_files'][SELECTOR] = byte_pin(corrected_bytes)
    expected_applied = {**plan['baseline']['files'], **{r['path']: r['after'] for r in plan['changes']}}
    need(applied['complete_applied_files'] == expected_applied,
         'APPLIED must preserve the exact pre-build baseline-plus-plan map')
    applied['metadata_successor_transport'] = full_pin(transport_path)
    applied['application_method'] = 'Exact copy of completed v17 workspace with one metadata payload replacement; no new compile or render.'
    write_new(plan_dir / 'APPLIED.json', encoded(applied))
    verification = copy.deepcopy(old_verification)
    verification['plan_pin'] = pin(plan_path)
    verification['current_configuration_pin'] = pin(inputs / 'INPUTS.json')
    verification['metadata_successor_transport'] = full_pin(transport_path)
    verification['verification_method'] = 'Exact preservation of the predecessor PDF, all compiler inputs and source witnesses; one corrected non-rendered metadata payload.'
    verification['new_compilation_performed'] = False
    verification['new_render_performed'] = False
    write_new(plan_dir / 'BUILD_VERIFICATION.json', encoded(verification))
    preparation = {'schema': 'periodized-residue-metadata-successor-preparation-v1',
        'status': 'metadata-successor-prepared-source-addendum-required', 'iteration': iteration,
        'workspace': str(source), 'plan': full_pin(plan_path), 'inputs': full_pin(inputs / 'INPUTS.json'),
        'inspection': full_pin(inputs / 'INSPECTION.json'), 'transport': full_pin(transport_path),
        'applied': full_pin(plan_dir / 'APPLIED.json'), 'build_verification': full_pin(plan_dir / 'BUILD_VERIFICATION.json'),
        'public_selector': full_pin(source / SELECTOR), 'pdf': transport['pdf'],
        'unchanged_visual_acceptance': full_pin(visual_path),
        'required_independent_source_addendum_schema': {'status': 'source-closure-verified', 'issues': [],
            'workspace': str(source), 'plan_pin': pin(plan_path)},
        'mathematical_jobs_reexecuted': 0, 'build_performed': False, 'render_performed': False,
        'promotion_performed': False, 'predecessor_unchanged': True}
    write_new(inputs / 'PREPARATION_RECEIPT.json', encoded(preparation))
    print(json.dumps({key: preparation[key] for key in ('status', 'workspace', 'plan', 'inputs', 'transport',
                        'build_verification', 'public_selector', 'pdf', 'unchanged_visual_acceptance')}, indent=2))

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-iteration', type=int, default=17)
    parser.add_argument('--iteration', type=int, required=True)
    parser.add_argument('--visual-receipt', type=Path, required=True)
    args = parser.parse_args()
    prepare(args.source_iteration, args.iteration, args.visual_receipt)

if __name__ == '__main__':
    main()
