"""Prepare the complete AU source/body/dependency extension; no checker runs.

Only declared manifest members are read. All writes are under the dedicated
work preparation directory or the explicitly named extension receipts.
"""
from __future__ import annotations

import importlib.util
import hashlib
import json
from pathlib import Path

WORK = Path(__file__).resolve().parent
PREFIX = 'sources/local_endpoint_continuations/'


def require(ok, message):
    if not ok:
        raise RuntimeError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def pin(path):
    raw = path.read_bytes()
    return {'bytes': len(raw), 'sha256': digest(raw)}


def readj(path):
    return json.loads(path.read_text(encoding='utf-8-sig'))


def writej(path, payload):
    path.write_bytes((json.dumps(payload, indent=2, ensure_ascii=False) + '\n').encode())


def main():
    manifest_path = WORK / 'arithmetic_volume_upper_manifest_20260913.json'
    manifest = readj(manifest_path)
    require(manifest['file_count'] == 37, 'AU manifest membership changed')
    source_name = 'arithmetic_volume_upper_route_20260913.tex'
    source_sha = '21aaedc3585887fa7d2cb3e37e68d14415829a4b213566f7a08f4619835ef38b'
    files = []
    for row in manifest['files']:
        actual = pin(WORK / row['path'])
        require(actual == {k: row[k] for k in ('bytes', 'sha256')}, 'AU file changed: ' + row['path'])
        raw = (WORK / row['path']).read_bytes()
        policy = 'exact-source-bytes'
        if Path(row['path']).suffix.casefold() in {'.json', '.md'}:
            text = raw.decode('utf-8-sig')
            if 'C:\\Users\\' in text or 'C:/Users/' in text or 'F:/user/' in text:
                policy = 'public-metadata-location-alias-required'
        # A mathematical proof is a full exact source. Any machine locator in it
        # requires an individually reviewed derivative, never generic aliasing.
        if row['path'] in {source_name, 'volume_comparator_review_20260913.md',
                           'volume_remainder_bound_review_20260913.md'}:
            require(policy == 'exact-source-bytes', 'Private location in full AU mathematical input')
        files.append({'source_base': 'workspace_work', 'source_path': row['path'],
                      'archive_path': PREFIX + row['path'], **actual,
                      'role': 'Complete AU proof, exact dependency, checker, historical receipt, independent proof/review, or visual witness',
                      'public_policy': policy})
    files.append({'source_base': 'workspace_work', 'source_path': manifest_path.name,
                  'archive_path': PREFIX + manifest_path.name, **pin(manifest_path),
                  'role': 'Complete 37-file final AU author seal', 'public_policy': 'exact-source-bytes'})

    helper_path = WORK / 'prepare_endpoint_proof_bodies_20260913.py'
    spec = importlib.util.spec_from_file_location('endpoint_proof_body_preparation', helper_path)
    helper = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(helper)
    raw = (WORK / source_name).read_bytes()
    require(digest(raw) == source_sha, 'AU source changed')
    source = raw.decode('utf-8-sig')
    require(source.count(r'\begin{document}') == 1 and source.count(r'\end{document}') == 1,
            'AU document boundary count')
    preamble, tail = source.split(r'\begin{document}')
    body, after = tail.split(r'\end{document}')
    require(not after.strip() and body.count(r'\maketitle') == 1, 'AU full body extent')
    declarations = helper.macros(preamble)
    retained = helper.lower_headings(body.replace(r'\maketitle', '', 1))
    title = 'An arithmetic lower-envelope comparison for central quotient volumes: full jets, finite determinant bounds, and an exact quadratic benchmark'
    prefix = '\\begingroup\n' + '\n'.join(x['local_declaration'] for x in declarations) + '\n\\section{' + title + '}\n'
    fragment = (prefix + retained + '\n\\endgroup\n').encode()
    spans = helper.math_spans(body)
    require(spans == helper.math_spans(fragment.decode()), 'AU ordered mathematical spans changed')
    require([x['label'] for x in helper.index(body)] == [x['label'] for x in helper.index(fragment.decode())],
            'AU equation sequence changed')
    output = WORK / 'endpoint_reader_prepared_20260913/proof_bodies/arithmetic_volume_upper_route.tex'
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes(fragment)
    body_row = {
        'source': source_name, 'source_bytes': len(raw), 'source_sha256': source_sha,
        'prepared_path': output.relative_to(WORK).as_posix(),
        'suggested_reader_path': 'tex/arithmetic_volume_upper_route.tex',
        'prepared_bytes': len(fragment), 'prepared_sha256': digest(fragment),
        'source_document_body_sha256': digest(body.encode()), 'retained_body_sha256': digest(retained.encode()),
        'original_math_span_count': len(spans),
        'ordered_math_spans_sha256': digest(json.dumps(spans, ensure_ascii=False).encode()),
        'original_ordered_math_spans_equal': True, 'complete_body_preserved': True,
        'changes': ['remove sole maketitle', 'lower section/subsection one level', 'wrap full body in local macro group and new title'],
        'local_macros': declarations, 'source_equations': helper.index(source),
        'reader_equations': helper.index(fragment.decode()),
        'original_preexisting_environments': ['theorem', 'lemma', 'proof'],
        'build_or_typesetting_execution': False}
    files.append({'source_base': 'workspace_work', 'source_path': body_row['prepared_path'],
                  'archive_path': body_row['suggested_reader_path'],
                  **pin(output), 'role': 'Entire AU document body with unchanged ordered mathematics and local macros',
                  'public_policy': 'exact-source-bytes'})

    jobs, pairs = [], []
    checker = 'check_arithmetic_volume_upper_independent_20260913.py'
    expected = readj(WORK / 'arithmetic_volume_upper_independent_checks_20260913.json')
    require(expected == readj(WORK / 'arithmetic_volume_upper_independent_checks_optimized_20260913.json'),
            'AU historical normal/optimized mismatch')
    require(expected['check_count'] == 112 and expected['script_sha256'] == pin(WORK / checker)['sha256'],
            'AU primary count or source identity changed')
    for optimized in (False, True):
        label = 'au-independent-' + ('optimized' if optimized else 'normal')
        jobs.append({'label': label, 'script': PREFIX + checker,
                     'script_sha256': pin(WORK / checker)['sha256'], 'optimized': optimized,
                     'args': ['--output', '{output}'], 'expected_exit_code': 0,
                     'runtime_profile': 'sympy', 'output_kind': 'json-option',
                     'companion_files': [], 'expected_fields': expected,
                     'execution_class': 'original-code-public-replay',
                     'negative_scope': '112 exact auxiliary rational/Gaussian-rational checks; analytic estimates remain in the complete written proof',
                     'executed_by_preparation': False})
    pairs.append({'labels': ['au-independent-normal', 'au-independent-optimized'],
                  'comparison': 'complete parsed direct result equal', 'ignore_fields': []})

    checker = 'volume_comparator_legendre_checks_20260913.py'
    proof = 'volume_comparator_review_20260913.md'
    for mode, optimized, fault in [('normal', False, False), ('optimized', True, False), ('normal', False, True)]:
        receipt = 'volume_comparator_legendre_' + ('fault' if fault else mode) + '_20260913.json'
        expected = readj(WORK / receipt)
        require(expected['checks'] == 99 and len(expected['failures']) == (33 if fault else 0), 'AU Legendre scope changed')
        require(expected['proof_sha256'] == pin(WORK / proof)['sha256'], 'AU Legendre companion changed')
        jobs.append({'label': 'au-legendre-' + mode + ('-rodrigues-factor' if fault else ''),
                     'script': PREFIX + checker, 'script_sha256': pin(WORK / checker)['sha256'],
                     'optimized': optimized,
                     'args': ['--output', '{output}'] + (['--fault', 'rodrigues-factor'] if fault else []),
                     'expected_exit_code': 1 if fault else 0, 'runtime_profile': 'sympy',
                     'output_kind': 'json-option', 'expected_fields': expected,
                     'companion_files': [{'path': PREFIX + proof, 'sha256': pin(WORK / proof)['sha256']}],
                     'execution_class': 'original-code-public-replay',
                     'negative_scope': 'Actual Rodrigues denominator mutation: all 99 identities execute and 33 fail' if fault else '99 exact finite Legendre identities at degrees 0 through 10',
                     'executed_by_preparation': False})
    pairs.append({'labels': ['au-legendre-normal', 'au-legendre-optimized'],
                  'comparison': 'complete parsed result equality except actual optimization flag', 'ignore_fields': ['optimized']})

    checker = 'volume_remainder_bound_review_20260913_checks.py'
    proof = 'volume_remainder_bound_review_20260913.md'
    expected = readj(WORK / 'volume_remainder_bound_review_20260913.checks.json')
    require(expected['checks'] == 117 and expected['proof_sha256'] == pin(WORK / proof)['sha256'],
            'AU remainder checker count or companion changed')
    jobs.append({'label': 'au-remainder-normal', 'script': PREFIX + checker,
                 'script_sha256': pin(WORK / checker)['sha256'], 'optimized': False, 'args': [],
                 'expected_exit_code': 0, 'runtime_profile': 'sympy', 'output_kind': 'fixed-sibling-json',
                 'fixed_output_name': 'volume_remainder_bound_review_20260913.checks.json',
                 'expected_fields': expected, 'isolated_copy_required': True,
                 'companion_files': [{'path': PREFIX + proof, 'sha256': pin(WORK / proof)['sha256']}],
                 'execution_class': 'original-code-public-replay',
                 'negative_scope': '117 exact finite polynomial-division and original affine/raw-jet checks; historical normal mode only',
                 'executed_by_preparation': False})

    result = {'schema': 'endpoint-au-complete-extension-v1', 'status': 'complete work-only preparation; no checker execution or build',
              'author_manifest': {'path': manifest_path.name, **pin(manifest_path)},
              'files': files, 'file_count': len(files), 'proof': body_row,
              'jobs': jobs, 'job_count': len(jobs), 'normal_optimized_comparisons': pairs, 'pair_count': len(pairs),
              'complete_readable_source_appendices': [
                  {'input': PREFIX + 'volume_comparator_review_20260913.md', 'scope': 'Entire independent VC.1-43 and VC.15a-b scalar comparison proof; no excerpt'},
                  {'input': PREFIX + 'volume_remainder_bound_review_20260913.md', 'scope': 'Entire RB.1-37 all-degree division and affine raw-jet proof; no excerpt'}],
              'source_dependency_scope': 'All 37 author-manifest members retained. Complete exact VC/RB companions are read by their respective checkers. No new mathematical runtime adaptation is required.'}
    target = WORK / 'endpoint_au_extension_20260913.json'
    writej(target, result)
    print(json.dumps({'path': target.name, **pin(target), 'files': len(files), 'jobs': len(jobs), 'pairs': len(pairs)}, indent=2))


if __name__ == '__main__':
    main()
