"""Small local Toda collector, fresh stager and portable replay.

Commands are explicit and independent: inspect (read only), collect, stage,
replay. No command publishes or freezes. The JSON specification is the complete
allowlist; final proof names, source audit and review/check paths are adaptable.
"""
from pathlib import Path
import argparse
import copy
import datetime as dt
import hashlib
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

sys.dont_write_bytecode = True
W = Path(__file__).resolve().parents[1]
R = W / 'output/split_zero_rh_tandem_2026-09-12'
sys.path.insert(0, str(W / 'work'))
import cyclic_publication_contract_20260912 as paths

PDF = 'Split_Zero_Cohomology_and_Arithmetic_Weight_Control.pdf'
SPECIAL = {'PUBLIC_SOURCE_MANIFEST.json', 'README.md', 'scripts/build_reader.py'}
HISTORY = 'history/20260912-cyclic/'
DEFAULT_SPEC = W / 'work/toda_edition_spec_20260913.json'


def need(ok, text):
    if not ok:
        raise RuntimeError(text)


def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))


def digest(data):
    return hashlib.sha256(data).hexdigest()


def save(path, obj, exclusive=False):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('x' if exclusive else 'w', encoding='utf-8') as stream:
        stream.write(json.dumps(obj, indent=2, ensure_ascii=True) + '\n')


def unique(names, what):
    need(len(names) == len(set(names)) == len({name.casefold() for name in names}),
         'Duplicate or case-colliding ' + what)


def active_tex(text):
    lines = []
    for line in text.splitlines():
        for index, char in enumerate(line):
            if char == '%':
                backslashes, cursor = 0, index - 1
                while cursor >= 0 and line[cursor] == '\\':
                    backslashes += 1
                    cursor -= 1
                if backslashes % 2 == 0:
                    line = line[:index]
                    break
        lines.append(line)
    return '\n'.join(lines)


def snapshot(root):
    root = Path(root)
    need(root.is_dir() and not root.is_symlink() and not root.is_junction(), 'Invalid package root')
    result = {}
    for path in sorted(root.rglob('*')):
        need(not path.is_symlink() and not path.is_junction(), 'Linked package entry: ' + str(path))
        if path.is_file():
            rel = path.relative_to(root).as_posix()
            paths.contained(root, rel)
            data = path.read_bytes()
            result[rel] = {'sha256': digest(data), 'bytes': len(data)}
    unique(list(result), 'package paths')
    return result


def baseline(spec):
    base = paths.contained(R, spec['base_directory'])
    for rel, pin in spec['base_pins'].items():
        need(paths.sha(paths.contained(base, rel)) == pin, 'Immutable G pin changed: ' + rel)
    manifest = read(base / 'PUBLIC_SOURCE_MANIFEST.json')
    rows = manifest['files']
    names = [paths.relative(row['path']) for row in rows] + sorted(SPECIAL)
    unique(names, 'G manifest members')
    actual = snapshot(base)
    need(set(actual) == set(names), 'G directory differs from its complete manifest')
    for row in rows:
        need(actual[row['path']] == {key: row[key] for key in ('sha256', 'bytes')}, 'Immutable G member changed: ' + row['path'])
    return base, manifest, read(base / 'build/build_receipt.json'), actual


def edition(spec_path):
    spec_path = spec_path.resolve()
    need(spec_path.is_relative_to(W / 'work'), 'Edition spec must reside in the task work directory')
    spec = read(spec_path)
    for key in ('base_directory', 'stage_directory', 'future_frozen_directory'):
        need('/' not in paths.relative(spec[key]), 'Use a direct child directory for ' + key)
    names = spec['new_proofs']
    unique(names, 'new proof basenames')
    need(names and all(re.fullmatch(r'[a-z][a-z0-9_]*', name) for name in names), 'Invalid new proof basenames')
    for rel in spec['allowed_updated_base_inputs']:
        need(paths.relative(rel) in {'tex/main.tex', 'tex/research_conclusion.tex'},
             'This continuation permits G input updates only in main and the cumulative conclusion')
    return spec


def inspect(spec_path, copy_work=False):
    spec = edition(spec_path)
    base, old_manifest, old_build, old_files = baseline(spec)
    rows, pending = {}, []
    work_sources = {'work/' + paths.relative(name): paths.contained(W / 'work', name)
                    for name in spec.get('work_files', [])}

    def add(rel, exact=False, source=None):
        rel = paths.relative(rel)
        # Sources use their exact archive allowlist; no user/transcript sweep.
        src = Path(source) if source else work_sources.get(rel, paths.contained(R, rel))
        if not src.is_file():
            pending.append('Missing ' + rel)
            return
        data = src.read_bytes()
        row = {'path': rel, 'sha256': digest(data), 'bytes': len(data), 'exact': exact}
        if rel in rows:
            need(rows[rel]['sha256'] == row['sha256'], 'Conflicting declared source for ' + rel)
            row['exact'] = exact or rows[rel]['exact']
        rows[rel] = row

    for name in spec.get('work_files', []):
        name = paths.relative(name)
        src = paths.contained(W / 'work', name)
        dst = paths.contained(R, 'work/' + name)
        if src.is_file() and copy_work:
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(src, dst)
        add('work/' + name, exact=src.suffix in ('.tex', '.py'), source=src)
    spec_rel = 'work/' + spec_path.relative_to(W / 'work').as_posix()
    if copy_work:
        target = paths.contained(R, spec_rel)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(spec_path, target)
    add(spec_rel, source=spec_path)
    for row in paths.package_members(spec):
        add(row['path'], row['exact_source_bytes'])
    for row in spec['source_witnesses']:
        add(row['path'], True)
        need(rows.get(row['path'], {}).get('sha256') == row['sha256'], 'Declared whole source witness changed: ' + row['path'])
    for row in spec.get('public_files', []):
        add(row['path'], row.get('exact', False))
    for row in spec.get('check_receipts', []):
        add(row['path'])
        file = work_sources.get(row['path'], paths.contained(R, row['path']))
        if file.is_file():
            record = read(file)
            if any(record.get(key) != value for key, value in row.get('expected', {}).items()):
                pending.append('Checker receipt differs from its declared scope: ' + row['path'])
    required = set(old_build['tex_inputs']) | {'tex/' + name + '.tex' for name in spec['new_proofs']}
    need(not ({'tex/' + name + '.tex' for name in spec['new_proofs']} & set(old_build['tex_inputs'])),
         'A new proof name would silently replace an inherited G chapter')
    main_text = active_tex((R / 'tex/main.tex').read_text(encoding='utf-8'))
    all_main_inputs = re.findall(r'\\input\s*\{([^}]+)\}', main_text)
    inputs = [name for name in all_main_inputs if name.startswith('tex/')]
    if len(inputs) != len(set(inputs)) or set(inputs) | {'tex/main.tex'} != required:
        pending.append('Main must include exactly every G chapter plus the declared new chapters')
    for rel in required:
        add(rel, True)
        if rel in old_build['tex_inputs'] and rel not in spec['allowed_updated_base_inputs']:
            if rel not in rows or rows[rel]['sha256'] != old_build['tex_inputs'][rel]:
                pending.append('Inherited G proof changed outside the declared update scope: ' + rel)
    built = read(R / 'build/build_receipt.json')
    if built.get('status') != 'compiled' or set(built.get('tex_inputs', {})) != required:
        pending.append('Final build does not pin the complete current proof membership')
    for rel, pin in built.get('tex_inputs', {}).items():
        if rel not in rows or rows[rel]['sha256'] != pin:
            pending.append('Unbuilt proof input: ' + rel)
    notes = built.get('source_notes', [])
    unique([row['source'] for row in notes], 'source appendix witnesses')
    unique([row['converted'] for row in notes], 'converted appendix paths')
    assembly = active_tex((R / 'build/source_appendices.tex').read_text(encoding='utf-8'))
    appendix_inputs = re.findall(r'\\input\s*\{([^}]+)\}', assembly)
    if len(appendix_inputs) != len(set(appendix_inputs)) or set(appendix_inputs) != {row['converted'] for row in notes}:
        pending.append('Source assembly must input every complete converted appendix exactly once')
    if all_main_inputs.count('build/source_appendices.tex') != 1:
        pending.append('Main must input the complete source appendix assembly exactly once')
    note_keys = [(row['source'], row['sha256'], row['converted']) for row in notes]
    old_keys = [(row['source'], row['sha256'], row['converted']) for row in old_build['source_notes']]
    if len(note_keys) != len(set(note_keys)) or not set(old_keys).issubset(note_keys):
        pending.append('Final source appendices must retain every exact G source/converted locator')
    wanted = {(row['path'], row['sha256']) for row in spec['source_witnesses']}
    if {(row['source'], row['sha256']) for row in notes} != {(a, b) for a, b, _ in old_keys} | wanted:
        pending.append('Final appendices differ from inherited plus explicitly declared whole source witnesses')
    for row in notes:
        add(row['source'], True)
        add(row['converted'], True)
        if row['source'] not in rows or rows[row['source']]['sha256'] != row['sha256']:
            pending.append('Original source differs from its build receipt: ' + row['source'])
    for _, _, converted in old_keys:
        if converted not in rows or rows[converted]['sha256'] != old_files[converted]['sha256']:
            pending.append('Inherited converted G appendix changed: ' + converted)
    production = ['build/build_receipt.json', 'build/source_receipt.json', 'build/source_appendices.tex',
                  'build/qa/qa_receipt.json', 'build/qa/visual_review.json', spec['source_audit'], spec['final_review'], PDF]
    for rel in production:
        add(rel, exact=rel.endswith(('.tex', '.pdf')))
    if PDF not in rows or rows[PDF]['sha256'] != built.get('pdf_sha256'):
        pending.append('Contributed PDF does not match the final build')
    if read(R / 'build/source_receipt.json') != notes:
        pending.append('Source receipt differs from the compiled source inventory')
    visual = read(R / 'build/qa/visual_review.json')
    if visual.get('reviewed_all_pages') is not True or visual.get('approved') is not True or visual.get('pdf_sha256') != built.get('pdf_sha256') or visual.get('pages') != built.get('pages'):
        pending.append('All-page visual approval must identify the final contributed PDF')
    components = visual.get('component_receipts', [])
    unique([row['path'] for row in components], 'visual component paths')
    for component in components:
        rel = paths.relative(component['path'])
        if rel not in rows or rows[rel]['sha256'] != component['sha256']:
            pending.append('Explicit inventory must retain the exact final visual component: ' + rel)
        elif read(paths.contained(R, rel)).get('pdf_sha256') != built.get('pdf_sha256') or read(paths.contained(R, rel)).get('approved') is not True:
            pending.append('Visual component does not approve the final PDF: ' + rel)
    qa = read(R / 'build/qa/qa_receipt.json')
    if qa.get('pdf_sha256') != built.get('pdf_sha256') or qa.get('pages') != built.get('pages') or qa.get('rendered_pages') != built.get('pages') or qa.get('out_of_page_words') != [] or qa.get('body_margin_crossings') != []:
        pending.append('Rendered QA receipt differs from the contributed PDF')
    audit_path = paths.contained(R, spec['source_audit'])
    if audit_path.is_file():
        audit = read(audit_path)
        checks, sources = audit.get('checks', []), audit.get('sources', [])
        unique([row['path'] for row in checks], 'audit proof paths')
        unique([row['path'] for row in sources], 'audit source paths')
        ci, si = {row['path']: row for row in checks}, {row['path']: row for row in sources}
        if audit.get('pdf_sha256') != built.get('pdf_sha256') or audit.get('proof_fragments') != len(required) - 1 or audit.get('complete_source_appendices') != len(notes):
            pending.append('Source audit does not describe the final complete edition')
        for rel in required:
            row = ci.get(rel, {})
            if row.get('matches') is not True or row.get('sha256') != rows.get(rel, {}).get('sha256'):
                pending.append('Proof audit does not pin ' + rel)
        for note in notes:
            row = si.get(note['source'], {})
            if row.get('original_preserved') is not True or row.get('sha256') != note['sha256'] or row.get('converted') != note['converted'] or row.get('converted_sha256') != rows.get(note['converted'], {}).get('sha256'):
                pending.append('Whole-source audit does not pin original and converted appendix: ' + note['source'])
    for rel, pin in spec.get('pinned_files', {}).items():
        need(rows.get(paths.relative(rel), {}).get('sha256') == pin, 'Declared final proof/review pin changed: ' + rel)
    unique(list(rows), 'collected paths')
    return spec, {'schema': 'split-zero-next-edition-inventory-v1', 'edition': spec['edition'],
                  'status': 'ready' if not pending else 'pending', 'pending': sorted(set(pending)),
                  'base_commit': spec['base_commit'], 'base_manifest_sha256': spec['base_pins']['PUBLIC_SOURCE_MANIFEST.json'],
                  'specification': spec_rel, 'specification_sha256': paths.sha(spec_path),
                  'proof_sections': len(required) - 1, 'source_appendices': len(notes),
                  'pages': built.get('pages'), 'pdf_sha256': built.get('pdf_sha256'),
                  'files': sorted(rows.values(), key=lambda row: row['path']),
                  'scope': spec['scope'], 'counts_are_derived_from_exact_membership': True}, old_files


def metadata_aliases(text):
    # Reuse the existing declared aliases without importing a publisher chain.
    helper = W / 'work/publish_split_zero_continuation_20260912.py'
    module_spec = importlib.util.spec_from_file_location('existing_metadata_aliases', helper)
    helper_module = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(helper_module)
    text = helper_module.metadata_aliases(text)
    source = str(R.parents[2] / 'Papors/OS')
    for form in (source, source.replace('\\', '/'), source.replace('\\', '\\\\')):
        text = text.replace(form, 'corpus:OS')
    profile = str(Path.home())
    for form in (profile.replace('\\', '\\\\'), profile, profile.replace('\\', '/')):
        text = re.sub(re.escape(form), 'local:user-profile', text, flags=re.I)
    text = re.sub(r'[A-Za-z]:[\\/]+Users[\\/]+' + re.escape(Path.home().name)
                  + r'(?=[\\/])', 'local:user-profile', text, flags=re.I)
    return text


def verify_stage(stage):
    manifest = read(stage / 'PUBLIC_SOURCE_MANIFEST.json')
    names = [row['path'] for row in manifest['files']] + sorted(SPECIAL)
    unique(names, 'public stage paths')
    files = snapshot(stage)
    need(set(files) == set(names), 'Stage membership differs from manifest')
    for row in manifest['files']:
        need(files[row['path']] == {key: row[key] for key in ('sha256', 'bytes')}, 'Staged bytes differ: ' + row['path'])
    indexed = {row['path']: row for row in manifest['files']}
    for component in read(stage / 'build/qa/visual_review.json').get('component_receipts', []):
        row = indexed.get(component['path'], {})
        need(component['sha256'] in (row.get('sha256'), row.get('source_sha256')),
             'Visual component original/public hashes are not preserved: ' + component['path'])
    need(files[PDF]['sha256'] == manifest['pdf_sha256'], 'Stage PDF differs')
    return manifest, files


def stage(spec_path):
    spec, inventory, old_files = inspect(spec_path)
    need(not inventory['pending'], '\n'.join(inventory['pending']))
    saved = read(paths.contained(R, spec['integration_manifest']))
    need(saved == inventory, 'Run collect after final local edits before staging')
    base, manifest, _, _ = baseline(spec)
    target = paths.contained(R, spec['stage_directory'])
    need(not target.exists(), 'Preserve the existing stage; staging requires a fresh sibling directory')
    shutil.copytree(base, target)
    manifest = copy.deepcopy(manifest)
    indexed = {row['path']: row for row in manifest['files']}

    def put(rel, data, exact=False):
        original = data
        if not exact and Path(rel).suffix in ('.json', '.md', '.txt', '.log'):
            data = metadata_aliases(data.decode('utf-8-sig')).encode('utf-8')
        if Path(rel).suffix not in ('.zip', '.pdf', '.png', '.jpg'):
            need(R.parts[2].casefold() not in data.decode('utf-8', errors='replace').casefold(), 'Private account text in public member: ' + rel)
        dst = paths.contained(target, rel)
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_bytes(data)
        indexed[rel] = {'path': rel, 'sha256': digest(data), 'bytes': len(data),
                        'source_sha256': digest(original), 'machine_metadata_aliased': data != original}

    new_rows = {row['path']: row for row in inventory['files']}
    replacements = set(new_rows) | SPECIAL
    # Preserve every overwritten historical G metadata receipt and all three
    # special files; historic hashes keep their original revision and locators.
    history = []
    for rel in sorted(replacements & set(old_files)):
        if rel in SPECIAL or (Path(rel).suffix in ('.json', '.md', '.log')
                              and new_rows[rel]['sha256'] != old_files[rel]['sha256']):
            put(HISTORY + rel, (base / rel).read_bytes(), True)
            history.append({'original_path': rel, 'history_path': HISTORY + rel, **old_files[rel]})
    put(HISTORY + 'RECEIPT_LOCATORS.json', (json.dumps({'base_commit': spec['base_commit'], 'files': history,
        'scope': 'Exact overwritten G metadata bytes; internal locators describe that historical edition.'}, indent=2) + '\n').encode(), True)
    for row in inventory['files']:
        src = paths.contained(R, row['path'])
        need(paths.sha(src) == row['sha256'] and src.stat().st_size == row['bytes'], 'Collected input changed: ' + row['path'])
        put(row['path'], src.read_bytes(), row['exact'])
    put(spec['integration_manifest'], paths.contained(R, spec['integration_manifest']).read_bytes())
    manifest.update(scope=spec['scope'], pages=inventory['pages'], pdf_sha256=inventory['pdf_sha256'],
                    proof_sections=inventory['proof_sections'], source_appendices=inventory['source_appendices'],
                    base_edition=spec['base_directory'], base_commit=spec['base_commit'],
                    intended_remote_prefix=spec['future_remote_prefix'], next_frozen_directory=spec['future_frozen_directory'])
    manifest['files'] = sorted(indexed.values(), key=lambda row: row['path'])
    save(target / 'PUBLIC_SOURCE_MANIFEST.json', manifest)
    reader = (base / 'scripts/build_reader.py').read_text(encoding='utf-8')
    reader = re.sub(r'pinned \d+-section', 'pinned ' + str(inventory['proof_sections']) + '-section', reader, count=1)
    (target / 'scripts/build_reader.py').write_text(reader, encoding='utf-8')
    (target / 'README.md').write_text(f'''# Split-Zero Cohomology and Arithmetic Weight Control

[Read the complete {inventory['pages']}-page PDF]({PDF}). This cumulative edition contains {inventory['proof_sections']} full proof chapters and {inventory['source_appendices']} complete source appendices.

{spec['scope']}

Every original member of the supplied Toda archive is retained byte-for-byte. The complete Toda NOTE is printed as a source appendix alongside every inherited G appendix. PUBLIC_SOURCE_MANIFEST.json records the original/public hashes. Overwritten G production receipts are retained under {HISTORY}; their locators and verification scopes remain historical.

Install Python, XeLaTeX and the fonts/packages declared in tex/main.tex, then run `python scripts/build_reader.py`. This compiles the included complete source bodies; it does not replace the contributed build/source/visual receipts. A rebuilt PDF can differ in metadata. New check scripts and their exact finite or numerical scopes are declared in the edition specification and integration inventory.

PDF SHA256: {inventory['pdf_sha256']}. Earlier frozen editions are unchanged. Private user logs and transcripts are excluded. No new Lean run or arithmetic asymptotic follows from a production check.
''', encoding='utf-8')
    _, files = verify_stage(target)
    need(snapshot(base) == old_files, 'Immutable G changed during staging')
    return {'stage': str(target), 'files': len(files), 'pages': inventory['pages'], 'pdf_sha256': inventory['pdf_sha256']}


def replay(spec_path):
    spec = edition(spec_path)
    base, _, _, old_files = baseline(spec)
    source = paths.contained(R, spec['stage_directory'])
    manifest, before = verify_stage(source)
    spec_rel = 'work/' + spec_path.relative_to(W / 'work').as_posix()
    need(read(paths.contained(source, spec_rel)) == spec, 'Current replay specification differs from its staged public copy')
    receipt_path = paths.contained(R, spec['portable_receipt'])
    need(not receipt_path.exists(), 'Preserve the existing portable receipt; use a new declared receipt path for another replay')
    temp = Path(tempfile.mkdtemp(prefix=spec['edition'] + '-portable-', dir=W / 'work'))
    package, logs = temp / 'package', temp / 'logs'
    shutil.copytree(source, package)
    logs.mkdir()
    need(snapshot(package) == before, 'Fresh package copy differs from stage')
    print(json.dumps({'event': 'portable-copy-ready', 'directory': str(temp), 'files': len(before)}), flush=True)
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', PYTHONIOENCODING='utf-8')
    if spec.get('replay_pythonpath'):
        pinned = paths.contained(W, spec['replay_pythonpath'])
        need(pinned.is_dir(), 'Declared check runtime path missing')
        env['PYTHONPATH'] = str(pinned)

    def run(label, command, cwd, expected=0, runtime_env=None):
        result = subprocess.run(command, cwd=cwd, env=runtime_env or env, capture_output=True)
        (logs / (label + '.stdout.log')).write_bytes(result.stdout)
        (logs / (label + '.stderr.log')).write_bytes(result.stderr)
        print(json.dumps({'event': 'portable-command-finished', 'label': label, 'exit_code': result.returncode}), flush=True)
        need(result.returncode == expected, 'Portable command failed its declared exit status: ' + label)
        return {'label': label, 'exit_code': result.returncode,
                'stdout_sha256': digest(result.stdout), 'stderr_sha256': digest(result.stderr)}, result.stderr

    run('reader', [sys.executable, '-B', 'scripts/build_reader.py'], package)
    from pypdf import PdfReader
    old_text = [page.extract_text() or '' for page in PdfReader(source / PDF).pages]
    new_text = [page.extract_text() or '' for page in PdfReader(package / PDF).pages]
    need(old_text == new_text and len(new_text) == manifest['pages'], 'Portable PDF differs in page count or page text')
    log = (package / 'build/reader.log').read_text(encoding='utf-8', errors='replace')
    warnings = re.findall(r'^Missing character:.*$|^Overfull.*$|^!.*$|^.*(?:Undefined control sequence|undefined references|multiply defined|LaTeX Error:|Emergency stop|Fatal error occurred).*$' , log, re.M)
    need(not warnings, 'Portable TeX log contains rendering errors or unresolved warnings')
    jobs, records = [], {}
    unique([job['label'] for job in spec.get('replay_jobs', [])], 'portable job labels')
    for job in spec.get('replay_jobs', []):
        label = job['label']
        need(re.fullmatch(r'[A-Za-z0-9_-]+', label), 'Unsafe replay label')
        folder = temp / label
        folder.mkdir()
        script = paths.contained(package, job['script'])
        local = folder / script.name
        shutil.copyfile(script, local)
        for rel in job.get('support_files', []):
            member = paths.contained(package, rel)
            need(member.name != local.name, 'Replay support file collides with script')
            shutil.copyfile(member, folder / member.name)
        output = folder / 'result.json'
        args = [arg.replace('{output}', str(output)) for arg in job.get('args', [])]
        command = [sys.executable, '-B'] + (['-O'] if job.get('optimized') else []) + [str(local)] + args
        job_env = dict(env)
        if job.get('use_pinned_pythonpath') is False:
            job_env.pop('PYTHONPATH', None)
        report, stderr = run(label, command, folder, job.get('exit_code', 0), job_env)
        if job.get('output_absent'):
            need(not output.exists(), 'Rejected control unexpectedly wrote a successful result: ' + label)
            need(job['stderr_contains'].encode('utf-8') in stderr, 'Negative control failed for an unexpected reason: ' + label)
            record = {'output_absent': True, 'matched_rejection': job['stderr_contains']}
        else:
            record = read(output)
            need(all(record.get(key) == value for key, value in job.get('expected', {}).items()), 'Replay result differs from declared exact scope: ' + label)
            if job.get('script_hash_field'):
                need(record.get(job['script_hash_field']) == paths.sha(script), 'Replay script hash differs: ' + label)
            if job.get('source_hash_field'):
                need(record.get(job['source_hash_field']) == paths.sha(paths.contained(package, job['source_hash_member'])), 'Replay proof-source hash differs: ' + label)
        records[label] = record
        report.update(script_sha256=paths.sha(script), receipt_sha256=paths.sha(output) if output.exists() else None,
                      pinned_pythonpath_used=job.get('use_pinned_pythonpath', True), record=record)
        jobs.append(report)
    for comparison in spec.get('replay_equal_records', []):
        if isinstance(comparison, list):
            left, right = comparison
            ignored = []
        else:
            left, right, ignored = comparison['left'], comparison['right'], comparison.get('ignore_fields', [])
        first = {key: value for key, value in records[left].items() if key not in ignored}
        second = {key: value for key, value in records[right].items() if key not in ignored}
        need(first == second, 'Normal/optimized records differ beyond declared run flags: ' + left + ' / ' + right)
    after = snapshot(package)
    protected = [rel for rel in before if rel != PDF and not rel.startswith('build/')]
    need(all(after.get(rel) == before[rel] for rel in protected), 'Portable replay changed a protected copied source')
    need(snapshot(source) == before and snapshot(base) == old_files, 'Portable replay changed stage or immutable G')
    result = {'schema': 'split-zero-next-edition-portable-replay-v1', 'status': 'passed',
              'finished_utc': dt.datetime.now(dt.timezone.utc).isoformat(), 'source_stage_hashes': before,
              'source_stage_manifest_sha256': before['PUBLIC_SOURCE_MANIFEST.json']['sha256'],
              'source_stage_unchanged': True, 'base_unchanged': True, 'contributed_pdf_sha256': manifest['pdf_sha256'],
              'build': {'pages': len(new_text), 'all_page_text_identical': True, 'warnings': warnings,
                        'rebuilt_pdf_sha256': paths.sha(package / PDF)},
              'checks': jobs, 'all_declared_jobs_passed': True,
              'temporary_directory': str(temp), 'replay_output_files': snapshot(logs),
              'scope': 'Complete fresh-copy PDF build and the explicitly declared validation jobs: the Toda finite source suite, TI fixed-input Arb enclosures with proved infinite tails and their ratio, and TC original-coordinate symbolic calibration with its deliberate controls. Historical G receipts retain their original scopes. This replay does not establish a finite-packet or growing-degree bound, an RH estimate, or a new Lean result.'}
    save(receipt_path, result, exclusive=True)
    return {'receipt': str(receipt_path), 'receipt_sha256': paths.sha(receipt_path), 'pages': len(new_text), 'jobs': len(jobs), 'status': 'passed'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=('inspect', 'collect', 'stage', 'replay'))
    parser.add_argument('--spec', type=Path, default=DEFAULT_SPEC)
    args = parser.parse_args()
    spec_path = args.spec.resolve()
    if args.command in ('inspect', 'collect'):
        spec, result, _ = inspect(spec_path, copy_work=args.command == 'collect')
        if args.command == 'collect':
            save(paths.contained(R, spec['integration_manifest']), result)
        print(json.dumps({key: value for key, value in result.items() if key != 'files'}, indent=2))
        return 0 if result['status'] == 'ready' else 2
    print(json.dumps(stage(spec_path) if args.command == 'stage' else replay(spec_path), indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
