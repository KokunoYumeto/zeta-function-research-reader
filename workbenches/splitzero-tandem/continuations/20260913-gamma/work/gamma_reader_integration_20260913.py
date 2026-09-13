"""Prepare and execute the local Gamma reader integration against immutable H.

Default ``inspect`` writes an inventory under work only. ``plan`` creates a
hash-pinned proposed change set under work; ``apply`` is a separate explicit
command. No command edits a frozen release, publication stage, Git or Zenodo.
Mathematical additions are complete authored inputs, never generated claims.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
import re
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

W = Path(__file__).resolve().parents[1]
WORK = W / 'work'
R = W / 'output/split_zero_rh_tandem_2026-09-12'
H = R / 'release_20260913h'
STAGE = R / 'sources/web_gamma_convolution_delivery'
PACKAGE = STAGE / 'Tau_Gamma_Convolution_Descent'
PLAN = WORK / 'gamma_reader_proposed_20260913'
INPUTS = WORK / 'gamma_reader_inputs_20260913.json'
REPORT = WORK / 'gamma_reader_integration_inventory_20260913.json'
HUMAN_REPORT = WORK / 'gamma_reader_integration_report_20260913.md'
ARCHIVE_SHA = '4b93cc5e9db76fdc6dec406c05197e2de5d7daab5957a855ee8b77711652b61a'
NOTE_SHA = '7cf984d87de405b815250b44454c4ee27c8ab46574da245b377ebc6e49327fa2'
MARKDOWN_SHA = '886c82e2562d9b4846adb44640d28a34552e38eb2518a3cd47f90dbbedd95e5b'
H_MANIFEST_SHA = 'affffb542a9e6ab11c7b665e38da2220802300b45599ce7e5464e3da82ae13f6'
H_PDF_SHA = 'f70b1c4e34cd2339080b8b9071ff3dd9d5b8dda80433b6eb191b84c9a9085cf4'
H_VERIFICATION_SHA = '379aae514b8b9d8bd61f328705f8b81bf69c78e106c8dafdd7eb98bf9b88453d'
H_LOCAL_SOURCE_RECEIPT_SHA = '5798cd6bcdc269668a06b63f5a06b485041aaa1dea48becf6d52cf3ef500b516'
BASE = {
    'tex/main.tex': '94794da8ccdd21ab08002b7c7c82d5f5fcf0928d6991d4b15823927e852f8b18',
    'scripts/build_paper.py': 'c3248a0cd128f7c40abc39a8890680063b1908566f523f8d4b254cf7c644a581',
    'scripts/cyclic_source_appendix_adapter.py': 'ae3f04e32140a8c4f8208d005fdde7cffe4c98dd09542551eb572e2b877fd020',
    'tex/research_conclusion.tex': 'b0aaab31ed11d56650919d9abfc12a6e74c431263912a9e713d845c93f8808c2',
    'logbook/THEOREM_CROSSWALK.md': 'ef30848be4cf257becd56f2031cda9c59469a51a022e08e3d72c8f5ae5f30292',
}
PROOFS = [
    ('gamma_exact_coefficient_join_20260913.tex', 'gamma_exact_coefficient_join',
     'The original gamma convolution and the exact arithmetic coefficient maps', 'GC'),
    ('gamma_seed_intervals_20260913.tex', 'gamma_seed_intervals',
     'Certified theta moments and the original gamma arithmetic coefficients', 'GS'),
    ('gamma_seed_intervals_20260913_source_costs.tex', 'gamma_seed_source_costs',
     'The first three original source costs at every tensor degree', 'GS.41–GS.50'),
    ('gamma_finite_metric_transfer_20260913.tex', 'gamma_finite_metric_transfer',
     'Finite arithmetic Gram transfer with the original minimum quotient metric', 'GMT'),
    ('gamma_phase_fibre_transport_20260913.tex', 'gamma_phase_fibre_transport',
     'The complete complex amplitude in gamma sum descent', 'GP'),
]
CONCLUSION = 'gamma_research_conclusion_addition_20260913.tex'
CROSSWALK = 'gamma_theorem_crosswalk_addition_20260913.md'
KNOWN_SUPPORT = [
    'gamma_convolution_complete_source_audit_20260913.md',
    'gamma_convolution_complete_source_audit_20260913.json',
    'gamma_convolution_bound_review_20260913.md',
    'gamma_seed_intervals_20260913_check.py',
    'gamma_seed_intervals_20260913_independent_review.md',
    'gamma_seed_intervals_20260913_source_costs_check.py',
    'gamma_finite_metric_transfer_check_20260913.py',
    'gamma_finite_metric_error_review_20260913.md',
    'gamma_finite_error_review_manifest_20260913.json',
]
MATH_PATTERN = r'\\\[(.*?)\\\]|\\\((.*?)\\\)|\$\$(.*?)\$\$|(?<![\\$])\$(?!\$)(.*?)(?<!\\)\$'


def need(condition, message):
    if not condition:
        raise RuntimeError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def sha(path):
    return digest(path.read_bytes())


def read(path):
    return json.loads(path.read_text(encoding='utf-8-sig'))


def encoded(value):
    return (json.dumps(value, indent=2, ensure_ascii=False) + '\n').encode('utf-8')


def safe(root, relative):
    rel = Path(relative)
    need(not rel.is_absolute() and '..' not in rel.parts, 'Unsafe relative path: ' + str(relative))
    target = (root / rel).resolve()
    need(target.is_relative_to(root.resolve()), 'Path escaped its declared root')
    return target


def mutable_target(relative):
    target = safe(R, relative)
    resolved_parts = target.relative_to(R.resolve()).parts
    need(not any(part.casefold().startswith(('release_', 'github_stage')) for part in resolved_parts),
         'Resolved destination enters an immutable release or publication stage: ' + str(target))
    # The path check must also cover unresolved junction/symlink components.
    # Reject such indirections rather than allowing an alias of a protected tree.
    current = R.resolve()
    for component in Path(relative).parts:
        current = current / component
        need(not current.is_symlink() and not (hasattr(current, 'is_junction') and current.is_junction()),
             'Destination uses a symlink or junction: ' + str(current))
    return target


def pin(path):
    return {'sha256': sha(path), 'bytes': path.stat().st_size}


def snapshot(root):
    return {p.relative_to(root).as_posix(): pin(p)
            for p in sorted(root.rglob('*')) if p.is_file()}


def frozen_h():
    need(H.is_dir(), 'Verified H release is not present')
    need(sha(H / 'PUBLIC_SOURCE_MANIFEST.json') == H_MANIFEST_SHA, 'Immutable H manifest changed')
    manifest = read(H / 'PUBLIC_SOURCE_MANIFEST.json')
    rows = {row['path']: row for row in manifest['files']}
    special = {'PUBLIC_SOURCE_MANIFEST.json', 'README.md', 'scripts/build_reader.py'}
    files = snapshot(H)
    verification_path = R / 'logbook/GITHUB_TODA_VERIFICATION_20260913.json'
    need(sha(verification_path) == H_VERIFICATION_SHA, 'Immutable H remote verification receipt changed')
    verified = read(verification_path)['verified_files']
    need(files == {name: {key: row[key] for key in ('sha256', 'bytes')}
                   for name, row in verified.items()}, 'H bytes differ from the verified remote edition')
    need(set(files) == set(rows) | special and len(files) == 946, 'Immutable H membership changed')
    for name, row in rows.items():
        need(files[name] == {key: row[key] for key in ('sha256', 'bytes')}, 'Immutable H member changed: ' + name)
    need(files['Split_Zero_Cohomology_and_Arithmetic_Weight_Control.pdf']['sha256'] == H_PDF_SHA,
         'Immutable H PDF changed')
    return files


def source_delivery():
    provenance = read(STAGE / 'LOCAL_STAGING_PROVENANCE.json')
    need(provenance['archive_sha256'] == ARCHIVE_SHA and provenance['member_count'] == 38,
         'Gamma archive identity changed')
    archive = STAGE / provenance['archive_name']
    need(archive.is_file() and sha(archive) == ARCHIVE_SHA, 'Exact Gamma source ZIP missing or changed')
    rows = provenance['files']
    need(len(rows) == 38, 'Gamma source provenance membership differs')
    with zipfile.ZipFile(archive) as zipped:
        names = [row['archive_entry'] for row in rows]
        need(set(names) == set(zipped.namelist()) and len(set(names)) == 38,
             'Archive and staging inventory differ')
        for row in rows:
            member = safe(STAGE, row['archive_entry'])
            need(pin(member) == {key: row[key] for key in ('sha256', 'bytes')},
                 'Gamma staged bytes changed: ' + row['archive_entry'])
            need(zipped.read(row['archive_entry']) == member.read_bytes(), 'Archive member differs')
    need(sha(PACKAGE / 'NOTE.tex') == NOTE_SHA, 'Complete Gamma NOTE changed')
    need(sha(PACKAGE / 'RESEARCH_NOTE.md') == MARKDOWN_SHA, 'Complete Gamma Markdown changed')
    return {'archive': archive.relative_to(R).as_posix(), **pin(archive), 'members': rows,
            'provenance': pin(STAGE / 'LOCAL_STAGING_PROVENANCE.json')}


def equation_index(text):
    return [{'label': match.group(1), 'line': text.count('\n', 0, match.start()) + 1}
            for match in re.finditer(r'\\tag\{([^}]+)\}', text)]


def math_nodes(node):
    if isinstance(node, dict):
        if node.get('t') == 'Math':
            return [node['c']]
        return [math for value in node.values() for math in math_nodes(value)]
    if isinstance(node, list):
        return [math for value in node for math in math_nodes(value)]
    return []


def transform(source, title):
    text = source.decode('utf-8-sig')
    if r'\begin{document}' not in text:
        need(r'\end{document}' not in text and r'\documentclass' not in text,
             'Malformed complete TeX fragment')
        return source, {'treatment': 'Byte-identical complete authored proof fragment.',
                        'exact_math_spans': True, 'source_equations': equation_index(text)}
    need(text.count(r'\begin{document}') == 1 and text.count(r'\end{document}') == 1,
         'Standalone proof must have one complete document body')
    preamble, tail = text.split(r'\begin{document}')
    body, after = tail.split(r'\end{document}')
    need(not after.strip(), 'Unaccounted content after complete proof document')
    original_body = body
    need(body.count(r'\maketitle') <= 1, 'Review repeated title command')
    body = body.replace(r'\maketitle', '', 1)
    body = re.sub(r'\\(section|subsection)(?=\*?[\[{])',
                  lambda m: '\\' + {'section': 'subsection', 'subsection': 'subsubsection'}[m[1]], body)
    macros = []
    for line in preamble.splitlines():
        stripped = line.strip()
        if stripped.startswith((r'\newcommand', r'\renewcommand', r'\providecommand')):
            match = re.fullmatch(r'\\(?:newcommand|renewcommand|providecommand)\{(\\[A-Za-z]+)\}(\{.*\})', stripped)
            need(match is not None, 'Review macro with arguments or multiline definition: ' + stripped)
            macros.append('\\def' + match[1] + match[2])
        elif stripped.startswith((r'\DeclareMathOperator', r'\def', r'\let')):
            raise RuntimeError('Review nonstandard preamble macro before integration: ' + stripped)
        elif stripped.startswith(r'\newtheorem'):
            match = re.match(r'\\newtheorem\{([^}]+)\}', stripped)
            need(match and match[1] in {'theorem', 'lemma', 'proposition', 'corollary', 'definition', 'example', 'remark'},
                 'Proof uses a theorem environment absent from cumulative main')
    result = ('\\begingroup\n' + '\n'.join(macros) + '\n\\section{' + title + '}\n' +
              body + '\n\\endgroup\n').encode('utf-8')
    need(re.findall(MATH_PATTERN, original_body, re.S) == re.findall(MATH_PATTERN, result.decode(), re.S),
         'Complete original proof mathematics changed during integration')
    # Display environments and equation tags outside inline/display delimiters
    # remain exact because the entire body undergoes only the two operations above.
    reversibly_lowered = re.sub(r'\\(section|subsection)(?=\*?[\[{])',
                               lambda m: '\\' + {'section': 'subsection', 'subsection': 'subsubsection'}[m[1]],
                               original_body.replace(r'\maketitle', '', 1))
    need(body == reversibly_lowered, 'Unaccounted proof body modification')
    return result, {'treatment': 'Complete standalone body; sole title command removed; source headings lowered one level; original zero-argument macros scoped locally; original full standalone bytes retained.',
                    'exact_math_spans': True, 'whole_body_transformation_verified': True,
                    'source_equations': equation_index(text), 'fragment_equations': equation_index(result.decode()),
                    'local_macros': macros}


def input_template():
    return {'schema': 'split-zero-gamma-reader-inputs-v1',
            'proofs': [row[0] for row in PROOFS],
            'conclusion': CONCLUSION, 'crosswalk': CROSSWALK,
            'support_files': KNOWN_SUPPORT,
            'scope': 'Complete local cumulative mathematics only; exact source witnesses and complete proof bodies. Main/GitHub/Zenodo integration stays with the coordinating owner.'}


def write_report(inventory):
    markdown_index = {row['label']: row['line'] for row in equation_index(
        (PACKAGE / 'RESEARCH_NOTE.md').read_text(encoding='utf-8'))}
    lines = ['# Prepared local Gamma reader integration', '',
             'This is a workflow and exact source inventory. No cumulative TeX, PDF, frozen release, publication stage, GitHub or Zenodo write was performed by preparation. The mathematical content remains in the complete source witnesses and authored proof files below.', '',
             '## Fixed inherited edition', '',
             'H is the 424-page, 946-member release at commit `16fc4dbb817b82023c6126e636f1c6df28d4cecd`. Every file is compared with the pinned complete remote verification ledger, including its three special manifest-excluded files. All inherited TeX inputs and the four used pipeline scripts are separately pinned before planning.', '',
             '- H PDF SHA-256: `' + H_PDF_SHA + '`.',
             '- H manifest SHA-256: `' + H_MANIFEST_SHA + '`.',
             '- H verification receipt SHA-256: `' + H_VERIFICATION_SHA + '`.',
             '- Current local H source-receipt SHA-256: `' + H_LOCAL_SOURCE_RECEIPT_SHA + '`.', '',
             '## Complete inputs and destinations', '',
             '| Full authored input under `work/` | Complete cumulative destination | Source equation prefix |',
             '|---|---|---|']
    for original, fragment, _, prefix in PROOFS:
        lines.append('| `' + original + '` | `tex/' + fragment + '.tex` | `' + prefix + '` |')
    lines += ['', 'The complete original standalone files are retained under `sources/local_gamma_continuations/`. Complete bodies are transferred by removing only their single title command, lowering source section headings one level, and introducing their original zero-argument macros inside a local TeX group. The original body transform and all delimited mathematics are compared exactly. Unsupported macro declarations stop preparation with the exact line requiring implementation work.', '',
              'The complete authored conclusion addition is `work/' + inventory['configuration']['conclusion'] + '`; the full source-to-current-proof crosswalk addition is `work/' + inventory['configuration']['crosswalk'] + '`. Their exact bytes are appended after the entire retained H originals and archived separately. This script does not synthesize theorem claims, conclusion formulas or a guessed source-to-result correspondence.', '',
              str(len(PROOFS)) + ' entire proof bodies are inserted before `jet_topology.tex`; the builder REQUIRED membership is extended in the same order. The GS.41–GS.50 source-cost fragment immediately follows the original GS.1–GS.40 chapter; its original proof and replay bytes remain separate and unchanged. The full original `RESEARCH_NOTE.md` becomes source appendix 19 after all 18 inherited appendices. The exact 38 archive members, original ZIP and alternate complete `NOTE.tex` remain untouched. The Gamma appendix provenance identifies its own source hash and does not assign it a historical Git revision as a new publication identity.', '',
              '## Exact original source index', '',
              'Gamma archive SHA-256: `' + ARCHIVE_SHA + '`. Complete `NOTE.tex` SHA-256: `' + NOTE_SHA + '`. Complete `RESEARCH_NOTE.md` SHA-256: `' + MARKDOWN_SHA + '`.', '',
              'All numbered source formulas below remain in the raw TeX and in the full Markdown appendix. The complete corrected GC chapter and the separately authored crosswalk will provide the final source-to-result correspondences once its author has fixed the labels. No proposed correspondence is inferred here.', '',
              '| Original equation | `NOTE.tex` line | `RESEARCH_NOTE.md` line | Printed destination |',
              '|---|---:|---:|---|']
    for row in inventory['source_equation_index']:
        lines.append('| (' + row['label'] + ') | ' + str(row['line']) + ' | ' +
                     str(markdown_index[row['label']]) + ' | Appendix 19, same source equation |')
    lines += ['', '## Current exact input snapshot', '',
              'These hashes describe the latest read-only inventory; authors may still revise their files. The later explicit `plan` command recomputes and freezes the final selected bytes before any apply command.', '',
              '| Existing input under `work/` | Bytes | SHA-256 |', '|---|---:|---|']
    for row in inventory['input_files']:
        lines.append('| `' + row['path'] + '` | ' + str(row['bytes']) + ' | `' + row['sha256'] + '` |')
    lines += ['', 'The JSON inventory includes every original and transformed equation-tag line for the authored proofs currently present; full Gamma source membership and all 946 H file hashes are included. The `support_files` configuration is an explicit finite list. Before final planning, the coordinating task adds each final review, checker receipt and any transitively referenced support member using the authors\' terminal manifests. Proof files and checkers retain sibling locations so proof-hash lookups remain meaningful.', '',
              '## Pending exact fields', '']
    lines += ['- ' + item for item in inventory['pending']] or ['- All named inputs are present; final mathematical review and terminal support-file selection remain with their active authors and the coordinating task.']
    lines += ['', '- Final complete proof hashes, final review receipts and terminal checker results are fixed after their authors finish; the inventory does not claim a receipt currently being edited is final.',
              '- Final cumulative PDF hash, page count, build receipt, all-page rendered evidence and actual visual approval exist only after apply/build/render and review. No values are invented for them.',
              '- There are no configured GitHub/main/Zenodo operations in this local integration script.', '',
              '## Reproducible commands and protections', '',
              'Use the workspace Python with `-B work/gamma_reader_integration_20260913.py <command>`.', '',
              '1. `inspect`: verify H and all Gamma source bytes, inspect current authored inputs, and write this report plus its JSON inventory under work only.',
              '2. `init-inputs`: create the explicit input configuration under work; extend its support-file list with the terminal author manifests.',
              '3. `plan`: verify all named inputs and original H working inputs, then write every proposed output plus its before/after hash under `work/gamma_reader_proposed_20260913/`. No reader mutation occurs.',
              '4. `apply`: recheck every plan/input/current-target hash; preserve all overwritten local working bytes under the proposed directory; install the complete authored additions. Protected release/stage prefixes and symlink/junction indirections are rejected before writes.',
              '5. `build`: verify the actual installed bytes and pipeline paths before executing the existing `scripts/build_paper.py`; retain complete stdout/stderr; require a clean final build and exact source verification.',
              '6. `verify`: check all final TeX hashes, all ' + str(len(PROOFS)) + ' complete proof-body mappings, all eighteen inherited source receipts and converted appendices, the exact Gamma raw source and all 223 original/prepared Pandoc Math nodes. Bind the final PDF to its receipt.',
              '7. `render`: use existing Poppler all-page rendering after the complete-source/build checks. Require matching final PDF hash/page count and clean geometry; then inspect all pages and write an actual visual review separately.', '',
              'These are internal reproducibility steps, not requests for human permission. A failure identifies exact unfinished implementation or source bytes for the coordinating task to repair within the authorized workflow. No command claims a mathematical theorem from a production check.', '',
              'The work-only Markdown conversion probe is retained at `work/gamma_markdown_adapter_probe_20260913/RECEIPT.json`. It found 223 unchanged Pandoc Math nodes, 60 displayed source blocks, zero code/Lean blocks, and generated complete TeX SHA-256 `fba7900d727b5e07a28c0418944b30d1ef45c2db10285f9f4c124cf91657a80b`. It did not compile a PDF or approve layout.', '',
              'Script SHA-256 at this report: `' + inventory['script_sha256'] + '`.', '']
    HUMAN_REPORT.write_text('\n'.join(lines), encoding='utf-8', newline='')


def inspect():
    h = frozen_h()
    delivery = source_delivery()
    need(sha(R / 'build/source_receipt.json') == H_LOCAL_SOURCE_RECEIPT_SHA,
         'Local complete H source receipt changed before planning')
    need(len(read(R / 'build/source_receipt.json')) == 18, 'Exactly eighteen inherited H source notes required')
    config = read(INPUTS) if INPUTS.is_file() else input_template()
    need(config['proofs'] == [row[0] for row in PROOFS], 'All ' + str(len(PROOFS)) + ' complete Gamma proof bodies must be retained in their declared order')
    required = config['proofs'] + [config['conclusion'], config['crosswalk']] + config['support_files']
    need(len(required) == len(set(required)), 'Repeated integration input')
    inputs = []
    pending = []
    for name in required:
        path = safe(WORK, name)
        if path.is_file():
            row = {'path': name, **pin(path)}
            if name in config['proofs']:
                proof = next(row for row in PROOFS if row[0] == name)
                try:
                    fragment, treatment = transform(path.read_bytes(), proof[2])
                    row.update(fragment='tex/' + proof[1] + '.tex',
                               fragment_sha256=digest(fragment), transformation=treatment)
                except RuntimeError as exc:
                    pending.append(name + ': ' + str(exc))
            inputs.append(row)
        else:
            pending.append('Complete input not yet present: work/' + name)
    for name, expected in BASE.items():
        need(sha(R / name) == expected, 'Cumulative H input changed before Gamma planning: ' + name)
    inherited_tex = {name: value for name, value in h.items() if name.startswith('tex/')}
    for name, expected in inherited_tex.items():
        need(pin(R / name) == expected, 'An inherited H proof input changed before planning: ' + name)
    runtime_files = {name: pin(R / name) for name in (
        'scripts/build_paper.py', 'scripts/cyclic_source_appendix_adapter.py',
        'scripts/toda_source_appendix_adapter.py', 'scripts/render_qa.py')}
    return {'schema': 'split-zero-gamma-reader-inventory-v1',
            'status': 'inputs-present-awaiting-root-content-review' if not pending else 'pending-inputs',
            'execution_performed': False, 'pending': pending, 'configuration': config,
            'immutable_H_files': h, 'base_files': BASE, 'gamma_delivery': delivery,
            'inherited_tex_inputs': inherited_tex,
            'runtime_files': runtime_files,
            'input_files': inputs, 'complete_source_appendices_before': 18,
            'complete_source_appendices_after': 19,
            'complete_new_proof_bodies': len(PROOFS),
            'script_sha256': sha(Path(__file__)),
            'source_equation_index': equation_index((PACKAGE / 'NOTE.tex').read_text(encoding='utf-8')),
            'next_actions': ['Finish and review the explicitly named authored inputs; add exact final supporting files to input configuration.',
                             'Run plan to pin every input and proposed output under work, then inspect the proposed complete diff.',
                             'Run apply, build, verify, render; visually inspect every final PDF page and record actual approval separately.'],
            'visual_approval_claimed': False, 'new_Lean_execution': False,
            'remote_publication_operations': []}


def adapter_source():
    spec = {'key': 'gamma_convolution',
            'source': 'sources/web_gamma_convolution_delivery/Tau_Gamma_Convolution_Descent/RESEARCH_NOTE.md',
            'provenance': 'sources/local_gamma_continuations/GAMMA_MARKDOWN_SOURCE_PROVENANCE.json',
            'title': 'Gamma convolution descent and the original arithmetic coefficient correction',
            'sha256': MARKDOWN_SHA, 'bytes': 30605,
            'revision': MARKDOWN_SHA,
            'revision_role': 'Complete delivered Markdown witness SHA-256; source-reported Git revisions retain their historical role',
            'lean_source_blocks': 0,
            'formal_status': 'Complete source witness. Finite checker records are separately retained. No new local Lean execution is claimed.',
            'attribution': 'Complete original Gamma Convolution Descent Markdown note delivered on 13 September 2026. Its archive and alternate complete TeX note are retained byte-for-byte. The full local coefficient chapter proves the exact coordinate maps, finite derivative indices, cochain primitive and transform domains alongside this unmodified source witness. Source reports about remote revisions and computations retain the verification scope of their original receipts.'}
    return ('"""Pinned complete Gamma Markdown witness; importing is read-only."""\n'
            'GAMMA_MARKDOWN_SPEC = ' + repr(spec) + '\n').encode('utf-8')


def plan():
    inventory = inspect()
    need(not inventory['pending'], '\n'.join(inventory['pending']))
    need(not PLAN.exists(), 'Preserve the existing proposed change set; use its pinned plan or record a revised path in this workflow')
    outputs = {}
    transformations = []
    for original, name, title, _ in PROOFS:
        data = (WORK / original).read_bytes()
        body, treatment = transform(data, title)
        outputs['sources/local_gamma_continuations/' + original] = data
        outputs['tex/' + name + '.tex'] = body
        transformations.append({'original': 'sources/local_gamma_continuations/' + original,
                                'source_sha256': digest(data), 'fragment': 'tex/' + name + '.tex',
                                'fragment_sha256': digest(body), **treatment})
    for name in inventory['configuration']['support_files']:
        outputs['sources/local_gamma_continuations/' + name] = safe(WORK, name).read_bytes()
    outputs['sources/local_gamma_continuations/FRAGMENT_TRANSFORMATIONS.json'] = encoded(transformations)
    outputs['sources/local_gamma_continuations/GAMMA_MARKDOWN_SOURCE_PROVENANCE.json'] = encoded({
        'sha256': MARKDOWN_SHA, 'bytes': 30605, 'archive_sha256': ARCHIVE_SHA,
        'archive_entry': 'Tau_Gamma_Convolution_Descent/RESEARCH_NOTE.md',
        'alternate_complete_tex_sha256': NOTE_SHA, 'all_source_bytes_preserved': True})
    outputs['scripts/gamma_source_appendix_adapter.py'] = adapter_source()
    main = (R / 'tex/main.tex').read_text(encoding='utf-8')
    anchor = r'\input{tex/jet_topology.tex}'
    need(main.count(anchor) == 1, 'Unique cumulative proof insertion point required')
    additions = '\n'.join(r'\input{tex/' + row[1] + '.tex}' for row in PROOFS)
    main = main.replace(anchor, additions + '\n' + anchor)
    cover = 'comparisons, and certified theta-seed input with explicit infinite tails.'
    need(main.count(cover) == 1, 'Exact H cover locator changed')
    main = main.replace(cover, 'comparisons, certified theta-seed input with explicit infinite tails,\n'
                        'gamma convolution and its full arithmetic coefficient maps,\n'
                        'the certified seed coefficients, finite source-to-quotient metric\n'
                        'transfer, and the complete complex amplitude in the sum fibres.')
    outputs['tex/main.tex'] = main.encode('utf-8')
    builder = (R / 'scripts/build_paper.py').read_text(encoding='utf-8')
    anchor = '"jet_topology.tex", "research_conclusion.tex",'
    need(builder.count(anchor) == 1, 'Unique builder proof inventory locator required')
    builder = builder.replace(anchor, ', '.join('"' + row[1] + '.tex"' for row in PROOFS) + ', ' + anchor)
    anchor = 'TEX_SOURCES.append(TODA_TEX_SPEC)'
    need(builder.count(anchor) == 1, 'Unique source adapter import locator required')
    builder = builder.replace(anchor, anchor + '\nfrom gamma_source_appendix_adapter import GAMMA_MARKDOWN_SPEC')
    anchor = 'for witness in (PASTED_SPEC, PR21_MARKDOWN_SPEC, PARENT_JOIN_SPEC):'
    need(builder.count(anchor) == 1, 'Unique complete Markdown witness loop required')
    builder = builder.replace(anchor, 'for witness in (PASTED_SPEC, PR21_MARKDOWN_SPEC, PARENT_JOIN_SPEC, GAMMA_MARKDOWN_SPEC):')
    ast.parse(builder)
    outputs['scripts/build_paper.py'] = builder.encode('utf-8')
    for relative, added in [('tex/research_conclusion.tex', inventory['configuration']['conclusion']),
                            ('logbook/THEOREM_CROSSWALK.md', inventory['configuration']['crosswalk'])]:
        original = (R / relative).read_bytes()
        addition = safe(WORK, added).read_bytes()
        need(addition.strip(), 'A complete authored addition is empty: ' + added)
        need(b'\\begin{document}' not in addition and b'\\end{document}' not in addition,
             'Conclusion/crosswalk addition must be a complete appendable fragment')
        outputs[relative] = original + b'\n\n' + addition
        outputs['sources/local_gamma_continuations/' + added] = addition
    PLAN.mkdir()
    changes = []
    for relative, data in outputs.items():
        target = safe(PLAN / 'files', relative)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
        current = R / relative
        changes.append({'path': relative, 'before': pin(current) if current.is_file() else None,
                        'after': {'sha256': digest(data), 'bytes': len(data)}})
    receipt = {'schema': 'split-zero-gamma-reader-proposed-changes-v1',
               'inventory': inventory, 'changes': changes,
               'complete_H_source_receipt': read(R / 'build/source_receipt.json'),
               'H_source_receipt_sha256': sha(R / 'build/source_receipt.json'),
               'scope': 'All proposed bytes are under work only. Apply is a separate local command; no remote operations.'}
    (PLAN / 'PLAN.json').write_bytes(encoded(receipt))
    return {'plan': str(PLAN / 'PLAN.json'), 'changes': len(changes), 'local_reader_modified': False}


def pinned_plan():
    receipt = read(PLAN / 'PLAN.json')
    need(frozen_h() == receipt['inventory']['immutable_H_files'], 'Frozen H changed after plan')
    need(source_delivery() == receipt['inventory']['gamma_delivery'], 'Gamma source changed after plan')
    need(sha(Path(__file__)) == receipt['inventory']['script_sha256'], 'Integration script changed after pinning')
    for row in receipt['inventory']['input_files']:
        need(pin(safe(WORK, row['path'])) == {key: row[key] for key in ('sha256', 'bytes')},
             'Authored input changed after plan: ' + row['path'])
    for row in receipt['changes']:
        need(pin(safe(PLAN / 'files', row['path'])) == row['after'], 'Proposed bytes changed: ' + row['path'])
    changed = {row['path'] for row in receipt['changes']}
    for name, expected in receipt['inventory']['inherited_tex_inputs'].items():
        if name not in changed:
            need(pin(R / name) == expected, 'An unchanged inherited H proof input changed: ' + name)
    for name, expected in receipt['inventory']['runtime_files'].items():
        if name not in changed:
            need(pin(R / name) == expected, 'An unchanged pipeline runtime changed: ' + name)
    return receipt


def apply():
    receipt = pinned_plan()
    applied = PLAN / 'APPLIED.json'
    need(not applied.exists(), 'This exact plan already has an apply receipt')
    for row in receipt['changes']:
        target = mutable_target(row['path'])
        current = pin(target) if target.is_file() else None
        need(current == row['before'], 'Local target changed since plan: ' + row['path'])
    # Retain exact overwritten working files separately before making edits.
    for row in receipt['changes']:
        target = mutable_target(row['path'])
        if target.is_file():
            backup = safe(PLAN / 'before', row['path'])
            backup.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(target, backup)
    for row in receipt['changes']:
        target = mutable_target(row['path'])
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(safe(PLAN / 'files', row['path']).read_bytes())
    need(frozen_h() == receipt['inventory']['immutable_H_files'], 'Frozen H changed during local apply')
    result = {'status': 'applied-local-complete-inputs', 'changes': len(receipt['changes']),
              'plan_sha256': sha(PLAN / 'PLAN.json'), 'frozen_H_unchanged': True,
              'build_performed': False, 'visual_approval_claimed': False}
    applied.write_bytes(encoded(result))
    return result


def verify():
    receipt = pinned_plan()
    for row in receipt['changes']:
        need(pin(safe(R, row['path'])) == row['after'], 'Applied input changed: ' + row['path'])
    built = read(R / 'build/build_receipt.json')
    need(built.get('status') == 'compiled', 'Final Gamma reader has not compiled')
    pdf = R / 'Split_Zero_Cohomology_and_Arithmetic_Weight_Control.pdf'
    need(sha(pdf) == built['pdf_sha256'], 'Current PDF differs from final build')
    for category in ('latex_warnings', 'font_warnings', 'missing_characters', 'overfull_boxes', 'undefined_controls'):
        need(not built['warnings'][category], 'Build requires typesetting repair: ' + category)
    for relative, expected in built['tex_inputs'].items():
        need(sha(safe(R, relative)) == expected, 'Built TeX input changed: ' + relative)
    sources = read(R / 'build/source_receipt.json')
    need(len(sources) == 19 and sources == built['source_notes'], 'Nineteen complete source witnesses required')
    old_sources = receipt['complete_H_source_receipt']
    need(len(old_sources) == 18, 'Pinned H source inventory must contain exactly eighteen witnesses')
    for old, new in zip(old_sources, sources[:18]):
        need(old == new, 'A retained H source receipt changed')
        need(sha(R / old['source']) == old['sha256'], 'Retained source bytes changed')
        need((R / old['converted']).read_bytes() == (H / old['converted']).read_bytes(),
             'An inherited complete converted H appendix changed: ' + old['converted'])
    need(sources[-1]['sha256'] == MARKDOWN_SHA, 'Last source is not complete original Gamma Markdown')
    original_ast = read(R / 'build/pandoc_gamma_convolution_codeblocks_original.json')
    prepared_ast = read(R / 'build/pandoc_gamma_convolution_codeblocks_prepared.json')
    gamma_math = math_nodes(original_ast)
    need(len(gamma_math) == 223 and gamma_math == math_nodes(prepared_ast),
         'Complete Gamma Markdown Math node sequence changed during preparation')
    transformations = read(R / 'sources/local_gamma_continuations/FRAGMENT_TRANSFORMATIONS.json')
    for row in transformations:
        need(sha(R / row['original']) == row['source_sha256'] and sha(R / row['fragment']) == row['fragment_sha256'],
             'Full authored Gamma proof/source pair changed')
    result = {'status': 'complete-source-and-build-verified', 'pages': built['pages'],
              'pdf_sha256': built['pdf_sha256'], 'proof_inputs': len(built['tex_inputs']) - 1,
              'source_appendices': len(sources), 'all_H_source_appendices_byte_exact': True,
              'gamma_original_prepared_math_nodes_identical': 223,
              'all_authored_proofs_complete_body_verified': True,
              'complete_authored_proof_bodies': len(PROOFS), 'frozen_H_unchanged': True,
              'visual_approval_claimed': False, 'plan_sha256': sha(PLAN / 'PLAN.json')}
    (PLAN / 'BUILD_VERIFICATION.json').write_bytes(encoded(result))
    return result


def run_pipeline(command):
    need((PLAN / 'APPLIED.json').is_file(), 'Apply the exact proposed inputs before build/render')
    receipt = pinned_plan()
    need(read(PLAN / 'APPLIED.json')['plan_sha256'] == sha(PLAN / 'PLAN.json'), 'Applied plan identity changed')
    for row in receipt['changes']:
        need(pin(mutable_target(row['path'])) == row['after'], 'Applied input changed before execution: ' + row['path'])
    mutable_target('Split_Zero_Cohomology_and_Arithmetic_Weight_Control.pdf')
    build_directory = mutable_target('build')
    mutable_target('build/qa')
    if build_directory.exists():
        for path in build_directory.rglob('*'):
            mutable_target(path.relative_to(R).as_posix())
    if command == 'render':
        verify()
    name = 'scripts/build_paper.py' if command == 'build' else 'scripts/render_qa.py'
    result = subprocess.run([sys.executable, '-B', str(R / name)], cwd=R, capture_output=True)
    (PLAN / (command + '.stdout.log')).write_bytes(result.stdout)
    (PLAN / (command + '.stderr.log')).write_bytes(result.stderr)
    need(result.returncode == 0, 'Local pipeline failed; inspect exact logs under proposed work directory')
    if command == 'build':
        return verify()
    qa = read(R / 'build/qa/qa_receipt.json')
    built = read(R / 'build/build_receipt.json')
    need(qa['pdf_sha256'] == built['pdf_sha256'] and qa['pages'] == built['pages'],
         'QA receipt does not identify the verified current build')
    need(qa['rendered_pages'] == qa['pages'] and not qa['out_of_page_words'] and not qa['body_margin_crossings'],
         'Rendered geometry needs repair')
    return {'status': 'rendered-for-all-page-inspection', 'pages': qa['pages'],
            'pdf_sha256': qa['pdf_sha256'], 'visual_approval_claimed': False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', nargs='?', default='inspect',
                        choices=('inspect', 'init-inputs', 'plan', 'apply', 'build', 'verify', 'render'))
    command = parser.parse_args().command
    if command == 'init-inputs':
        need(not INPUTS.exists(), 'Existing exact input configuration retained')
        INPUTS.write_bytes(encoded(input_template()))
        result = {'input_configuration': str(INPUTS), 'local_reader_modified': False}
    elif command == 'inspect':
        result = inspect()
        REPORT.write_bytes(encoded(result))
        write_report(result)
        result = {key: value for key, value in result.items() if key not in ('immutable_H_files', 'gamma_delivery')}
    elif command == 'plan':
        result = plan()
    elif command == 'apply':
        result = apply()
    elif command == 'verify':
        result = verify()
    else:
        result = run_pipeline(command)
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
