"""Gamma collector, fresh H-based stager, and explicit portable replay.

Commands are explicit and independent: inspect (read only), collect, stage,
replay. No command publishes or freezes. The JSON specification is the complete
allowlist; final proof names, source audit and review/check paths are adaptable.
"""
from pathlib import Path
import argparse
import copy
import datetime as dt
import hashlib
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
HISTORY = 'history/20260913-toda/'
DEFAULT_SPEC = W / 'work/gamma_edition_spec_20260913.json'


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
        need(paths.sha(paths.contained(base, rel)) == pin, 'Immutable H pin changed: ' + rel)
    manifest = read(base / 'PUBLIC_SOURCE_MANIFEST.json')
    rows = manifest['files']
    names = [paths.relative(row['path']) for row in rows] + sorted(SPECIAL)
    unique(names, 'H manifest members')
    actual = snapshot(base)
    need(set(actual) == set(names), 'H directory differs from its complete manifest')
    need(len(actual) == spec['expected_base_files'] and manifest['pages'] == spec['expected_base_pages'],
         'Frozen H baseline counts differ from its exact parent declaration')
    for row in rows:
        need(actual[row['path']] == {key: row[key] for key in ('sha256', 'bytes')}, 'Immutable H member changed: ' + row['path'])
    authority = paths.contained(R, spec['base_verification'])
    need(paths.sha(authority) == spec['pinned_files'][spec['base_verification']], 'H verification authority changed')
    verified = read(authority)
    need(verified['commit'] == spec['base_commit'] and verified['public_manifest_sha256'] == spec['base_pins']['PUBLIC_SOURCE_MANIFEST.json'],
         'H own commit/manifest authority differs')
    need({rel: {key: row[key] for key in ('sha256', 'bytes')} for rel, row in verified['verified_files'].items()} == actual,
         'Complete H files differ from the pinned original remote verification receipt')
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
             'This continuation permits H input updates only in main and the cumulative conclusion')
    return spec


def inspect(spec_path, copy_work=False):
    spec = edition(spec_path)
    base, old_manifest, old_build, old_files = baseline(spec)
    rows, pending = {}, []
    def current_json(rel, default):
        file = paths.contained(R, rel)
        if not file.is_file():
            pending.append('Missing final record ' + rel)
            return default
        return read(file)

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
    support = read(W / 'work' / spec['support_inventory'])
    need(support.get('support_count') == 249 and len(support['files']) == 249, 'Unexpected five-proof support closure')
    for member in support['files']:
        rel = paths.relative(member['archive_path'])
        add(rel, exact=Path(rel).suffix in ('.tex', '.py', '.png', '.pdf') and not member.get('contains_native_execution_locator', False))
        if rel not in rows or rows[rel]['sha256'] != member['sha256'] or rows[rel]['bytes'] != member['bytes']:
            pending.append('Support closure bytes differ: ' + rel)
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
         'A new proof name would silently replace an inherited H chapter')
    main_text = active_tex((R / 'tex/main.tex').read_text(encoding='utf-8'))
    all_main_inputs = re.findall(r'\\input\s*\{([^}]+)\}', main_text)
    inputs = [name for name in all_main_inputs if name.startswith('tex/')]
    if len(inputs) != len(set(inputs)) or set(inputs) | {'tex/main.tex'} != required:
        pending.append('Main must include exactly every H chapter plus the declared new chapters')
    for rel in required:
        add(rel, True)
        if rel in old_build['tex_inputs'] and rel not in spec['allowed_updated_base_inputs']:
            if rel not in rows or rows[rel]['sha256'] != old_build['tex_inputs'][rel]:
                pending.append('Inherited H proof changed outside the declared update scope: ' + rel)
    transformations = current_json('sources/local_gamma_continuations/FRAGMENT_TRANSFORMATIONS.json', [])
    unique([row['original'] for row in transformations], 'Gamma original proof transformation paths')
    unique([row['fragment'] for row in transformations], 'Gamma integrated proof transformation paths')
    if {row['fragment'] for row in transformations} != {'tex/' + name + '.tex' for name in spec['new_proofs']}:
        pending.append('Fragment transformation inventory must cover exactly the five new proofs')
    for transform in transformations:
        source_row, fragment_row = rows.get(transform['original'], {}), rows.get(transform['fragment'], {})
        if (source_row.get('sha256') != transform['source_sha256'] or fragment_row.get('sha256') != transform['fragment_sha256']
                or transform.get('exact_math_spans') is not True
                or (transform['source_sha256'] != transform['fragment_sha256'] and transform.get('whole_body_transformation_verified') is not True)):
            pending.append('Original/integrated proof transformation receipt differs: ' + transform['fragment'])
    built = current_json('build/build_receipt.json', {})
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
        pending.append('Final source appendices must retain every exact H source/converted locator')
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
            pending.append('Inherited converted H appendix changed: ' + converted)
    production = ['build/build_receipt.json', 'build/source_receipt.json', 'build/source_appendices.tex',
                  'build/qa/qa_receipt.json', 'build/qa/visual_review.json', spec['source_audit'], spec['final_review'], PDF]
    for rel in production:
        add(rel, exact=rel.endswith(('.tex', '.pdf')))
    if PDF not in rows or rows[PDF]['sha256'] != built.get('pdf_sha256'):
        pending.append('Contributed PDF does not match the final build')
    if current_json('build/source_receipt.json', []) != notes:
        pending.append('Source receipt differs from the compiled source inventory')
    visual = current_json('build/qa/visual_review.json', {})
    if visual.get('reviewed_all_pages') is not True or visual.get('approved') is not True or visual.get('pdf_sha256') != built.get('pdf_sha256') or visual.get('pages') != built.get('pages'):
        pending.append('All-page visual approval must identify the final contributed PDF')
    components = visual.get('component_receipts', [])
    unique([row['path'] for row in components], 'visual component paths')
    for component in components:
        rel = paths.relative(component['path'])
        add(rel)
        if rel not in rows or rows[rel]['sha256'] != component['sha256']:
            pending.append('Explicit inventory must retain the exact final visual component: ' + rel)
        elif read(paths.contained(R, rel)).get('pdf_sha256') != built.get('pdf_sha256') or read(paths.contained(R, rel)).get('approved') is not True:
            pending.append('Visual component does not approve the final PDF: ' + rel)
    qa = current_json('build/qa/qa_receipt.json', {})
    if qa.get('pdf_sha256') != built.get('pdf_sha256') or qa.get('pages') != built.get('pages') or qa.get('rendered_pages') != built.get('pages') or qa.get('out_of_page_words') != [] or qa.get('body_margin_crossings') != []:
        pending.append('Rendered QA receipt differs from the contributed PDF')
    # Only final receipt-declared contact sheets are collected, never a broad
    # workspace or QA-directory sweep. Additional reviewed images may be listed
    # explicitly in public_files by the integration owner.
    for locator in qa.get('contact_sheets', []):
        normalized = locator.replace('\\', '/')
        if normalized.startswith('package:'):
            rel = normalized.removeprefix('package:').lstrip('/')
        else:
            file = Path(locator).resolve()
            need(file.is_relative_to(R.resolve()), 'Final QA image escapes the current package')
            rel = file.relative_to(R.resolve()).as_posix()
        need(paths.relative(rel).startswith('build/qa/'), 'Final QA contact sheet is outside the declared QA tree')
        add(rel, True)
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
    if len(required) != 44 or len(notes) != 19:
        pending.append('Final Gamma cut must have 43 proof chapters, 44 TeX inputs and 19 source appendices')
    for rel, pin in spec.get('pinned_files', {}).items():
        need(rows.get(paths.relative(rel), {}).get('sha256') == pin, 'Declared immutable source/dependency pin changed: ' + rel)
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
    profile = Path.home()
    roots = [(str(R), 'package:'), (str(W), 'workspace:'),
             (str(profile / 'Documents/Papors/Chatnotes'), 'corpus:Chatnotes'),
             (str(profile / 'Documents/Raw Transcript Dump - SSD Downloads'), 'corpus:SSD-transcript-mirror'),
             (str(profile / 'Documents/Papors/OS'), 'corpus:OS'),
             (str(profile / 'miniconda3'), 'runtime:research-python'),
             ('F:/user/Documents/Papors/Chatnotes', 'corpus:Chatnotes'),
             ('F:/dowloads', 'corpus:SSD-downloads'), (str(profile), 'local:user-profile')]
    for source, target in roots:
        normal = source.replace('/', chr(92))
        for form in (normal.replace(chr(92), chr(92)*2), normal, normal.replace(chr(92), '/')):
            text = re.sub(re.escape(form), lambda match: target, text, flags=re.I)
    text = re.sub(r'[A-Za-z]:[\\/]+Users[\\/]+' + re.escape(profile.name)
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
        if not exact and (Path(rel).suffix in ('.json', '.md', '.txt', '.log') or rel in spec.get('aliased_native_helpers', [])):
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
    # Preserve every overwritten historical H metadata receipt and all three
    # special files; historic hashes keep their original revision and locators.
    history = []
    for rel in sorted(replacements & set(old_files)):
        if rel in SPECIAL or (Path(rel).suffix in ('.json', '.md', '.log')
                              and new_rows[rel]['sha256'] != old_files[rel]['sha256']):
            put(HISTORY + rel, (base / rel).read_bytes(), True)
            history.append({'original_path': rel, 'history_path': HISTORY + rel, **old_files[rel]})
    put(HISTORY + 'RECEIPT_LOCATORS.json', (json.dumps({'base_commit': spec['base_commit'], 'files': history,
        'scope': 'Exact overwritten H metadata bytes; internal locators describe that historical edition.'}, indent=2) + '\n').encode(), True)
    for row in inventory['files']:
        src = paths.contained(R, row['path'])
        need(paths.sha(src) == row['sha256'] and src.stat().st_size == row['bytes'], 'Collected input changed: ' + row['path'])
        put(row['path'], src.read_bytes(), row['exact'])
    put(spec['integration_manifest'], paths.contained(R, spec['integration_manifest']).read_bytes())
    manifest.update(publication_note='Cumulative H-to-Gamma source and proof edition; inherited receipt scopes remain historical.', metadata_alias_policy=spec['metadata_alias_policy'], scope=spec['scope'], pages=inventory['pages'], pdf_sha256=inventory['pdf_sha256'],
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

Every original member of the supplied 38-file Gamma archive is retained byte-for-byte. The complete delivered RESEARCH_NOTE.md is printed as a source appendix alongside every inherited H appendix. The alternate NOTE.tex remains complete in the exact source archive. Five new proof chapters preserve the GC, GS, source-cost, GMT and GP derivations. PUBLIC_SOURCE_MANIFEST.json records the original/public hashes. Overwritten H production receipts are retained under {HISTORY}; their locators and verification scopes remain historical.

Install Python, XeLaTeX and the fonts/packages declared in tex/main.tex, then run `python scripts/build_reader.py`. This compiles the included complete source bodies; it does not replace the contributed build/source/visual receipts. A rebuilt PDF can differ in metadata. New check scripts and their exact finite or numerical scopes are declared in the edition specification and integration inventory.

PDF SHA256: {inventory['pdf_sha256']}. Earlier frozen editions are unchanged. Private user logs and transcripts are excluded. No new Lean run or arithmetic asymptotic follows from a production check.
''', encoding='utf-8')
    _, files = verify_stage(target)
    need(snapshot(base) == old_files, 'Immutable H changed during staging')
    return {'stage': str(target), 'files': len(files), 'pages': inventory['pages'], 'pdf_sha256': inventory['pdf_sha256']}


def replay(spec_path, package_source=None, receipt_override=None, checks_only=False, runtime_map=None):
    """Replay the public package without consulting native historical helpers.

    Local replay verifies frozen H as well. An exported package uses its complete
    manifest and H history pins, with no requirement for the original workspace.
    All suites run in independent copied source trees, with explicit relative
    arguments and a pre-check execution probe even when a guard rejects early.
    """
    spec = read(spec_path)
    portable = package_source is not None
    if portable:
        source = Path(package_source).resolve()
        need(receipt_override is not None, 'Portable replay needs an explicit --receipt path')
        receipt_path = Path(receipt_override).resolve()
        need(not receipt_path.is_relative_to(source), 'Write replay receipts outside the contributed package')
        base, old_files = None, None
    else:
        spec = edition(spec_path)
        base, _, _, old_files = baseline(spec)
        source = paths.contained(R, spec['stage_directory'])
        receipt_path = Path(receipt_override).resolve() if receipt_override else paths.contained(R, spec['portable_receipt'])
        need(not receipt_path.is_relative_to(source) and not receipt_path.is_relative_to(base),
             'Write replay receipts outside the contributed stage and frozen H')
    manifest, before = verify_stage(source)
    need(manifest['base_commit'] == spec['base_commit'], 'Staged H parent differs from the specification')
    for rel, pin in spec['base_pins'].items():
        need(paths.sha(paths.contained(source, HISTORY + rel)) == pin, 'Historical H special pin changed: ' + rel)
    public_index = {row['path']: row for row in manifest['files']}
    authority_row = public_index[spec['base_verification']]
    need(spec['pinned_files'][spec['base_verification']] in
         (authority_row['sha256'], authority_row.get('source_sha256')), 'H original verification pin was lost in public aliasing')
    authority = read(paths.contained(source, spec['base_verification']))
    need(authority['commit'] == spec['base_commit'] and len(authority['verified_files']) == spec['expected_base_files'],
         'Public H authority describes a different parent')
    spec_rel = 'work/' + spec_path.name
    need(read(paths.contained(source, spec_rel)) == spec, 'Replay spec differs from the public staged spec')
    need(not receipt_path.exists(), 'Preserve prior replay receipts; choose a fresh receipt path')
    scratch_parent = receipt_path.parent
    scratch_parent.mkdir(parents=True, exist_ok=True)
    temp = Path(tempfile.mkdtemp(prefix=spec['edition'] + '-portable-', dir=scratch_parent))
    package, logs = temp / 'package', temp / 'logs'
    shutil.copytree(source, package)
    logs.mkdir()
    need(snapshot(package) == before, 'Fresh package copy differs from contributed bytes')
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', PYTHONIOENCODING='utf-8')
    # Ambient Python paths and optimization must not silently change the suites.
    env.pop('PYTHONPATH', None)
    env.pop('PYTHONOPTIMIZE', None)
    runtimes = read(runtime_map) if runtime_map else {}
    if not portable and not runtime_map:
        runtimes = {'sympy-1.14.0': {'pythonpath': str(paths.contained(W, spec['local_sympy_114_path']))}}
    print(json.dumps({'event': 'portable-copy-ready', 'files': len(before), 'directory': str(temp)}), flush=True)

    def run(label, command, cwd, expected=0, timeout=1800, runtime_env=None):
        actual_env = runtime_env or env
        report = {'label': label, 'argv': command, 'cwd': str(cwd), 'expected_exit_code': expected,
                  'timeout_seconds': timeout, 'environment': {
                      key: actual_env.get(key) for key in ('PYTHONDONTWRITEBYTECODE', 'PYTHONIOENCODING',
                                                         'PYTHONPATH', 'PYTHONOPTIMIZE')}}
        save(logs / (label + '.invocation.json'), report)
        result = subprocess.run(command, cwd=cwd, env=actual_env, capture_output=True, timeout=timeout)
        (logs / (label + '.stdout.log')).write_bytes(result.stdout)
        (logs / (label + '.stderr.log')).write_bytes(result.stderr)
        report.update(exit_code=result.returncode, stdout_sha256=digest(result.stdout), stderr_sha256=digest(result.stderr))
        save(logs / (label + '.execution.json'), report)
        print(json.dumps({'event': 'portable-command-finished', 'label': label, 'exit_code': result.returncode}), flush=True)
        need(result.returncode == expected, 'Portable command failed its exact exit contract: ' + label)
        return report, result.stderr, result.stdout

    build_report = {'executed': False, 'reason': 'Explicit checks-only replay'}
    if not checks_only:
        build_invocation, _, _ = run('reader', [sys.executable, '-B', 'scripts/build_reader.py'], package,
                                  timeout=spec.get('build_timeout_seconds', 1800))
        from pypdf import PdfReader
        old_text = [page.extract_text() or '' for page in PdfReader(source / PDF).pages]
        new_text = [page.extract_text() or '' for page in PdfReader(package / PDF).pages]
        need(old_text == new_text and len(new_text) == manifest['pages'], 'Rebuilt PDF differs in page count or page text')
        log = (package / 'build/reader.log').read_text(encoding='utf-8', errors='replace')
        warnings = re.findall(r'^Missing character:.*$|^Overfull.*$|^!.*$|^.*(?:Undefined control sequence|undefined references|multiply defined|LaTeX Error:|Emergency stop|Fatal error occurred).*$', log, re.M)
        need(not warnings, 'Portable TeX log contains rendering errors or unresolved warnings')
        build_report = {'executed': True, 'pages': len(new_text), 'all_page_text_identical': True,
                        'warnings': warnings, 'rebuilt_pdf_sha256': paths.sha(package / PDF), 'invocation': build_invocation}
    declared = read(paths.contained(package, 'work/' + spec['portable_jobs_file']))
    jobs = declared['jobs']
    unique([job['label'] for job in jobs], 'portable job labels')
    need(len(jobs) == spec['expected_portable_jobs'], 'Portable suite membership differs from the declared cut')
    reports, records = [], {}
    for job in jobs:
        label = job['label']
        need(re.fullmatch(r'[A-Za-z0-9_-]+', label), 'Unsafe replay label')
        folder = temp / label
        folder.mkdir()
        support = paths.contained(package, spec['support_directory'])
        delivery = paths.contained(package, spec['delivery_directory'])
        shutil.copytree(support, folder / 'support')
        shutil.copytree(delivery, folder / 'delivery')
        # Keep the exact relative topology for imports, proofs and input receipts.
        substitution = {'{support}': 'support', '{delivery}': 'delivery', '{output}': 'result.json',
                        spec['support_directory']: 'support', spec['delivery_directory']: 'delivery'}
        def expand(value):
            for key, replacement in substitution.items():
                value = value.replace(key, replacement)
            need(not re.search(r'\{(?:support|delivery|output)\}', value), 'Unexpanded job argument')
            return value
        script_rel = paths.relative(expand(job['script']))
        script = paths.contained(folder, script_rel)
        need(script.is_file(), 'Missing portable checker ' + script_rel)
        need(not job.get('script_sha256') or paths.sha(script) == job['script_sha256'], 'Checker source pin differs: ' + label)
        output_kind = job['output_kind']
        output_rel = ((Path(script_rel).parent / paths.relative(job['fixed_output_relative_to_script'])).as_posix()
                      if output_kind == 'fixed-sibling-json' else 'result.json')
        output = paths.contained(folder, output_rel)
        if output.exists():
            need(output.is_file(), 'Fixed-output checker target is not a file')
            output.unlink()  # One exact file inside this new isolated job copy.
        output.parent.mkdir(parents=True, exist_ok=True)
        protected = snapshot(folder)
        argv = [expand(arg) for arg in job.get('args', [])]
        # Explicit argument values must be relative within the isolated copy.
        need(all(not re.search(r'[A-Za-z]:[\\/]|^[/\\]', arg) for arg in [script_rel] + argv),
             'Portable job has a native absolute argument: ' + label)
        optimized = bool(job.get('optimized', False))
        need(not (optimized and job.get('optimized_execution_forbidden')), 'Assertion suite cannot run optimized: ' + label)
        profile = job['runtime_profile']
        runtime_config = runtimes.get(profile, {})
        executable = runtime_config.get('python', sys.executable)
        job_env = dict(env)
        if runtime_config.get('pythonpath'):
            runtime_path = Path(runtime_config['pythonpath']).resolve()
            need(runtime_path.is_dir(), 'Declared runtime module directory missing: ' + profile)
            job_env['PYTHONPATH'] = str(runtime_path)
        version_expression = ({'sympy-1.14.0': "__import__('sympy').__version__",
                               'sympy-1.13.1': "__import__('sympy').__version__",
                               'python-flint-0.9.0': "__import__('flint').__version__",
                               'python-stdlib': "'stdlib'"})[profile]
        probe = ("import json,pathlib,runpy,sys; "
                 "pathlib.Path('runtime.json').write_text(json.dumps({'optimization':sys.flags.optimize,"
                 "'debug':__debug__,'python':sys.version,'executable':sys.executable,'library_version':"
                 + version_expression + "}),encoding='utf-8'); "
                 "sys.argv=sys.argv[1:]; sys.path.insert(0,str(pathlib.Path(sys.argv[0]).resolve().parent)); "
                 "runpy.run_path(sys.argv[0],run_name='__main__')")
        command = [executable, '-B'] + (['-O'] if optimized else []) + ['-c', probe, script_rel] + argv
        report, stderr, stdout = run(label, command, folder, job['expected_exit_code'], job.get('timeout_seconds', 1800), job_env)
        runtime = read(folder / 'runtime.json')
        shutil.copyfile(folder / 'runtime.json', logs / (label + '.runtime.json'))
        need(runtime['optimization'] == int(optimized) and runtime['debug'] == (not optimized),
             'Observed optimization differs from the declared mode: ' + label)
        version = {'sympy-1.14.0': '1.14.0', 'sympy-1.13.1': '1.13.1', 'python-flint-0.9.0': '0.9.0', 'python-stdlib': 'stdlib'}[profile]
        need(runtime['library_version'] == version, 'Wrong observed dependency version: ' + label)
        if output_kind == 'absent':
            need(not output.exists(), 'Rejected guard unexpectedly wrote its success JSON: ' + label)
            need(job['stderr_contains'].encode() in stderr, 'Guard rejected for the wrong reason: ' + label)
            record = {'output_absent': True, 'matched_rejection': job['stderr_contains']}
            if label.startswith('original-gamma-'):
                record['methods_executed'] = 0
        elif output_kind == 'stdout-text':
            need(job['stdout_contains'].encode() in stdout, 'Unexpected independent fixture output: ' + label)
            record = {'stdout_contains': job['stdout_contains'], 'matched': True}
        else:
            if output_kind == 'stdout-json':
                output.write_bytes(stdout)
            need(output_kind in ('stdout-json', 'json-option', 'fixed-sibling-json'), 'Unknown output contract')
            need(output.is_file(), 'Checker did not create its declared output: ' + label)
            record = read(output)
            for key, expected in job.get('expected_fields', {}).items():
                need(record.get(key) == expected, 'Unexpected checker scope field ' + key + ': ' + label)
            for field, member in job.get('hash_fields', {}).items():
                need(record.get(field) == paths.sha(paths.contained(folder, paths.relative(expand(member)))),
                     'Checker result does not pin its actual input: ' + label + ' / ' + field)
        after_job = snapshot(folder)
        need(all(after_job.get(rel) == pin for rel, pin in protected.items()), 'Checker changed an input dependency: ' + label)
        if output.exists():
            shutil.copyfile(output, logs / (label + '.result.json'))
        records[label] = record
        report.update(script=script_rel, script_sha256=paths.sha(script), argument_templates=job.get('args', []),
                      optimized_requested=optimized, observed_runtime=runtime, input_files=protected,
                      result_path=output_rel, receipt_sha256=paths.sha(output) if output.exists() else None,
                      runtime_profile=profile, output_kind=output_kind, record=record, exact_scope=job['scope'])
        reports.append(report)
        save(logs / (label + '.verified.json'), report)
    for comparison in declared.get('normal_optimized_pairs', []):
        left, right = comparison['left'], comparison['right']
        ignored = set(comparison.get('ignore_fields', []))
        need({k: v for k, v in records[left].items() if k not in ignored} ==
             {k: v for k, v in records[right].items() if k not in ignored},
             'Normal/optimized records differ beyond declared run flags: ' + left + ' / ' + right)
    after = snapshot(package)
    need(all(after.get(rel) == pin for rel, pin in before.items() if rel != PDF and not rel.startswith('build/')),
         'Portable build changed a protected source')
    need(snapshot(source) == before, 'Portable replay changed its contributed package')
    if base is not None:
        need(snapshot(base) == old_files, 'Portable replay changed frozen H')
    result = {'schema': 'split-zero-gamma-portable-replay-v2', 'status': 'passed',
              'finished_utc': dt.datetime.now(dt.timezone.utc).isoformat(),
              'source_stage_hashes': before, 'source_stage_manifest_sha256': before['PUBLIC_SOURCE_MANIFEST.json']['sha256'],
              'source_stage_unchanged': True, 'base_unchanged': True if base is not None else None,
              'base_verification_scope': 'local exact 946-file H snapshot' if base is not None else 'public exact H history special pins and pinned original H verification receipt',
              'contributed_pdf_sha256': manifest['pdf_sha256'], 'build': build_report, 'checks': reports,
              'all_declared_jobs_passed': True, 'jobs_executed': len(reports),
              'temporary_directory': str(temp), 'replay_output_files': snapshot(logs),
              'scope': spec['replay_scope']}
    save(receipt_path, result, exclusive=True)
    return {'receipt': str(receipt_path), 'receipt_sha256': paths.sha(receipt_path),
            'pages': manifest['pages'], 'jobs': len(reports), 'status': 'passed', 'reader_rebuilt': not checks_only}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=('inspect', 'collect', 'stage', 'replay'))
    parser.add_argument('--spec', type=Path, default=DEFAULT_SPEC)
    parser.add_argument('--package', type=Path, help='Exported contributed package for portable replay')
    parser.add_argument('--receipt', type=Path, help='Fresh replay receipt outside the contributed package')
    parser.add_argument('--checks-only', action='store_true', help='Explicitly omit the reader rebuild; record this narrower scope')
    parser.add_argument('--runtime-map', type=Path, help='Host runtime JSON mapping each profile to python/pythonpath')
    args = parser.parse_args()
    need(args.command == 'replay' or not (args.package or args.receipt or args.checks_only or args.runtime_map), 'Replay flags require replay')
    spec_path = args.spec.resolve()
    if args.command in ('inspect', 'collect'):
        spec, result, _ = inspect(spec_path, copy_work=args.command == 'collect')
        if args.command == 'collect':
            save(paths.contained(R, spec['integration_manifest']), result)
        print(json.dumps({key: value for key, value in result.items() if key != 'files'}, indent=2))
        return 0 if result['status'] == 'ready' else 2
    result = stage(spec_path) if args.command == 'stage' else replay(spec_path, args.package, args.receipt, args.checks_only, args.runtime_map)
    print(json.dumps(result, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
