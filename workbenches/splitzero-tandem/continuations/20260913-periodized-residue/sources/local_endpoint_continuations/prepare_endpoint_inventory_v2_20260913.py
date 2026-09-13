"""Close the finite endpoint extension under work, preserving v1 unchanged.

This program inventories fixed files and prepares descriptions. It never runs a
mathematical checker, compiles a document, changes R or a stage, or publishes.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path

WORK = Path(__file__).resolve().parent
R = WORK.parent / 'output/split_zero_rh_tandem_2026-09-12'
OWNER = Path('F:/user/Documents/Papors/Chatnotes/Zeta-Function-Foundation/agents/zenodo_workspace_publication')
PREFIX = 'sources/local_endpoint_continuations/'
ROOTS = {
    'workspace_work': WORK, 'cumulative_source': R, 'owner_publication': OWNER,
    'user_delivery': WORK.parent.parent / 'Papors/Chatnotes/CHat translates and clean/Noether Multilingual'}
V1_PINS = {
    'endpoint_reader_integration_inventory_20260913.json': '6582b10563a1be400a15f8c12e45811984a2952d7f13b03151f9dd7825958c67',
    'endpoint_reader_portable_jobs_20260913.json': 'c0da8397a15255e392d90c3fef05505867f264c02d19c0089d8341c6e1a508f7',
    'endpoint_reader_full_proof_body_plan_20260913.json': '6598e5de5f1e47b3f7de206f37ec06238b1530e7cee489962a8c5df4b27a5e3e'}
OWNER_PIN = 'e90c4fc45dfa54dfffcf9172a6f1e7f20df00eae45d73d448e0f381953068dc1'
AU_PIN = 'dc30a460ab05313fe708934befe1f149efe09363169b5aaa8de6986d7e036535'


def need(condition, message):
    if not condition:
        raise RuntimeError(message)


def pin(path):
    raw = path.read_bytes()
    return {'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()}


def read(name, expected=None):
    path = WORK / name
    if expected:
        need(pin(path)['sha256'] == expected, 'Preparation input changed: ' + name)
    return json.loads(path.read_text(encoding='utf-8-sig'))


def write(name, data):
    path = WORK / name
    path.write_bytes((json.dumps(data, indent=2, ensure_ascii=False) + '\n').encode())
    return {'path': name, **pin(path)}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--rf-extension', help='Complete root-sealed RF extension JSON with files, proof and jobs; relative to work')
    args = parser.parse_args()
    baseline = {name: read(name, expected) for name, expected in V1_PINS.items()}
    inventory = copy.deepcopy(baseline['endpoint_reader_integration_inventory_20260913.json'])
    jobs = copy.deepcopy(baseline['endpoint_reader_portable_jobs_20260913.json'])
    bodyplan = copy.deepcopy(baseline['endpoint_reader_full_proof_body_plan_20260913.json'])
    au = read('endpoint_au_extension_20260913.json', AU_PIN)
    owner = read('endpoint_terminal_owner_inventory_20260913.json', OWNER_PIN)
    need(owner['published_outgoing_count'] == 46 and len(owner['files']) == 62, 'Owner terminal scope changed')
    extensions = [('AU', au)]
    if args.rf_extension:
        relative = Path(args.rf_extension)
        need(not relative.is_absolute() and '..' not in relative.parts, 'RF extension path escaped work')
        rf = read(args.rf_extension)
        need(rf.get('status') == 'complete root-sealed RF extension; no integration execution', 'RF source not terminal')
        extensions.append(('RF', rf))
    rows = {row['archive_path']: row for row in inventory['files']}
    need(len(rows) == inventory['file_count'] == 283, 'Prior endpoint inventory membership')

    def add(row):
        rel = Path(row['source_path'])
        need(not rel.is_absolute() and '..' not in rel.parts, 'Unsafe source path')
        root = ROOTS[row['source_base']].resolve()
        path = (root / rel).resolve()
        need(path.is_relative_to(root), 'Source path escaped declared root')
        need(pin(path) == {key: row[key] for key in ('bytes', 'sha256')}, 'Source pin changed: ' + row['source_path'])
        archive = Path(row['archive_path'])
        need(not archive.is_absolute() and '..' not in archive.parts, 'Unsafe archive path')
        old = rows.get(row['archive_path'])
        if old:
            need((old['sha256'], old['bytes']) == (row['sha256'], row['bytes']), 'Archive collision: ' + row['archive_path'])
        else:
            rows[row['archive_path']] = copy.deepcopy(row)

    # Revalidate every inherited source and every new finite manifest member.
    for row in list(rows.values()) + owner['files']:
        add(row)
    for lane, extension in extensions:
        for row in extension['files']:
            add(row)
        bodyplan['proofs'].append(extension['proof'])
        jobs['jobs'].extend(extension['jobs'])
        jobs['pair_comparisons'].extend(extension['normal_optimized_comparisons'])

    # Explicit contract repairs found in independent dispatcher review. They
    # strengthen observed-field verification; no checker or source bytes change.
    repairs = []
    for job in jobs['jobs']:
        if job['label'].startswith('owner-window-') and job['output_kind'] == 'absent':
            job['fixed_output_name'] = 'PORTABLE_CHECK_RECEIPT.json'
            repairs.append({'job': job['label'], 'field': 'fixed_output_name',
                            'value': job['fixed_output_name'], 'reason': 'Test actual fixed sibling absence after terminal formula control'})
        if job['label'] == 'ew-independent-final-numeric':
            job['expected_fields'].update({'check_count': 67, 'mathematical_checks': 63,
                                          'provenance_and_run_selection_checks': 4,
                                          'script_sha256': job['script_sha256'],
                                          'source_sha256': job['companion_files'][0]['sha256'],
                                          'supplement_sha256': job['companion_files'][1]['sha256']})
            repairs.append({'job': job['label'], 'field': 'expected_fields', 'reason': 'Verify exact recorded67/63/4 counts and actual adapted code/input identities'})
        if job['label'] == 'ew-independent-remainder-kernel':
            job['expected_fields'].update({'distinct_scalar_checks': 6, 'script_sha256': job['script_sha256']})
            repairs.append({'job': job['label'], 'field': 'expected_fields', 'reason': 'Verify six recorded scalar checks and actual source identity'})
    for pair in jobs['pair_comparisons']:
        if all('owner-window-' in label and 'gaussian-negative' in label for label in pair['labels']):
            pair['comparison'] = 'same declared exit and terminal Gaussian formula failure after complete portable suite; fixed sibling JSON absent'

    sources = inventory['complete_readable_source_appendices']
    sources = [row for row in sources if row['input'] != 'owner PR24 original and proposed RESEARCH_NOTE.md']
    sources.extend([
        {'input': 'sources/owner_endpoint_review/review_pr24/files/workbenches/tau-confluent-transfer/RESEARCH_NOTE.md',
         'scope': 'Complete original historical PR24 proof; retained separately from final correction'},
        {'input': 'sources/owner_endpoint_review/review_pr24/join_inputs/PR23_ENDPOINT_CORRECTED.md',
         'scope': 'Complete corrected PR23 endpoint and full multiplicity proof'}])
    for lane, extension in extensions:
        sources.extend(extension.get('complete_readable_source_appendices', []))
    for source in owner['full_readable_appendices']:
        sources.append({'input': source['archive_path'], 'scope': source['requirement'],
                        'source_id': source['source_id'], 'equations': source['equations']})
    sources_by_path = {}
    for source in sources:
        need(source['input'] in rows, 'Complete readable source missing: ' + source['input'])
        sources_by_path.setdefault(source['input'], source)
    inventory['complete_readable_source_appendices'] = list(sources_by_path.values())
    # Replace formerly verbal owner locators by their final exact byte locations.
    for entry in inventory['reader_body_order']:
        if entry['input'] == 'owner FOUR_VOLUME_THRESHOLD.md':
            entry['input'] = next(x['archive_path'] for x in owner['full_readable_appendices'] if x['source_id'] == 'FV-public')
            entry['state'] = 'final immutable owner publication; exact single-link source morphism retained'
        elif entry['input'] == 'owner PR24 corrected RESEARCH_NOTE.md':
            entry['input'] = next(x['archive_path'] for x in owner['full_readable_appendices'] if x['source_id'] == 'CT-final')
            entry['state'] = 'final adopted corrected merge; byte-identical existing proposal retained with adoption receipts'
        elif '/' not in entry['input']:
            entry['input'] = PREFIX + entry['input']
    for lane, extension in extensions:
        inventory['reader_body_order'].append({'input': PREFIX + extension['proof']['source'],
            'scope': 'Entire complete authored document body and all tagged/untagged mathematics',
            'format': 'TeX', 'state': 'final pinned full body with local macro definitions'})
    for row in inventory['reader_body_order']:
        need(row['input'] in rows, 'Reader body locator missing: ' + row['input'])

    pending = [] if args.rf_extension else ['Root final RF proof, review and expanded checker companion seal']
    inventory['schema'] = 'next-endpoint-reader-preparation-v2'
    inventory['status'] = 'finite AU and terminal owner extension complete; work-only preparation'
    inventory['pending_author_seals'] = pending
    inventory['terminal_owner'] = {'inventory': 'endpoint_terminal_owner_inventory_20260913.json',
        'sha256': OWNER_PIN, 'publication_commit': owner['publication_commit'],
        'corrected_pr24_merge': owner['corrected_pr24_merge'],
        'four_volume_link_morphism': owner['four_volume_link_morphism'],
        'unchanged_checker_code_map': owner['unchanged_checker_code_map']}
    inventory['predecessor_preparation'] = [{'path': name, **pin(WORK / name)} for name in V1_PINS]
    inventory['explicit_contract_repairs'] = repairs
    bodyplan['schema'] = 'endpoint-complete-proof-body-preparation-v2'
    bodyplan['pending_author_seals'] = pending
    bodyplan_receipt = write('endpoint_reader_full_proof_body_plan_v2_20260913.json', bodyplan)
    provenance = [
        'endpoint_au_extension_20260913.json', 'prepare_endpoint_au_extension_20260913.py',
        'endpoint_terminal_owner_inventory_20260913.json', 'endpoint_terminal_owner_read_report_20260913.md',
        'endpoint_terminal_checker_closure_20260913.json', 'endpoint_terminal_checker_closure_20260913.md',
        'ENDPOINT_READER_EXTENSION_LOGBOOK_20260913.md', 'prepare_endpoint_inventory_v2_20260913.py',
        'endpoint_reader_full_proof_body_plan_v2_20260913.json',
        'endpoint_reader_integration_inventory_20260913.json', 'endpoint_reader_portable_jobs_20260913.json',
        'ENDPOINT_READER_INTEGRATION_HANDOFF_20260913.md']
    if args.rf_extension:
        provenance.append(args.rf_extension)
    for name in provenance:
        add({'source_base': 'workspace_work', 'source_path': name, 'archive_path': PREFIX + name,
             **pin(WORK / name), 'role': 'Complete finite source, dependency or preparation provenance',
             'public_policy': 'exact-source-bytes'})
    bylabel = {job['label']: job for job in jobs['jobs']}
    need(len(bylabel) == len(jobs['jobs']), 'Duplicate portable job label')
    edges = 0
    for job in jobs['jobs']:
        need(job['script'] in rows and rows[job['script']]['sha256'] == job['script_sha256'],
             'Portable checker missing or changed: ' + job['label'])
        edges += 1
        for companion in job['companion_files']:
            need(companion['path'] in rows and rows[companion['path']]['sha256'] == companion['sha256'],
                 'Portable companion missing or changed: ' + companion['path'])
            edges += 1
    for pair in jobs['pair_comparisons']:
        need(len(pair['labels']) == 2 and all(label in bylabel for label in pair['labels']), 'Invalid mode pair')
        left, right = (bylabel[label] for label in pair['labels'])
        need(not left['optimized'] and right['optimized'], 'Mode-pair ordering mismatch')
    for mapping in owner['unchanged_checker_code_map']:
        for archive in mapping['existing_v1_archive_paths']:
            need(rows[archive]['sha256'] == mapping['sha256'], 'Final owner checker identity mismatch')
    inventory['files'] = list(rows.values())
    inventory['file_count'] = len(rows)
    inventory['dependency_closure'] = {'all_file_pins_validated': len(rows),
        'portable_script_and_companion_edges_validated': edges, 'mode_pairs_validated': len(jobs['pair_comparisons']),
        'checker_executions': 0, 'cumulative_or_stage_mutations': 0}
    jobs['schema'] = 'endpoint-portable-jobs-v2'
    jobs['status'] = 'complete declared jobs for sealed inputs; no executions by preparation'
    jobs['job_count'] = len(jobs['jobs'])
    jobs['pair_count'] = len(jobs['pair_comparisons'])
    jobs['pending_lanes'] = pending
    jobs['explicit_contract_repairs'] = repairs
    job_receipt = write('endpoint_reader_portable_jobs_v2_20260913.json', jobs)
    inventory['portable_jobs'] = job_receipt
    inventory['complete_body_plan'] = bodyplan_receipt
    inv_receipt = write('endpoint_reader_integration_inventory_v2_20260913.json', inventory)
    print(json.dumps({'inventory': inv_receipt, 'jobs': job_receipt, 'bodyplan': bodyplan_receipt,
                      'files': len(rows), 'jobs_count': len(jobs['jobs']), 'pairs': len(jobs['pair_comparisons']),
                      'pending': pending}, indent=2))


if __name__ == '__main__':
    main()
