"""Independent isolated checks of the fixed-source build workflow; no TeX run."""
from pathlib import Path
import hashlib
import importlib.util
import json
import subprocess
import sys
import tempfile
from unittest.mock import patch

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent / 'cumulative_source_v1/scripts/build_current_reader.py'
SPEC = importlib.util.spec_from_file_location('reviewed_current_builder', SOURCE)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class FakeDocument:
    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False

    def __len__(self):
        return 5


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run_case(name, change=None, expected_error=None, authoring=False):
    with tempfile.TemporaryDirectory(prefix='isolated_builder_', dir=HERE) as temp:
        container = Path(temp)
        root = container / 'repository with spaces'
        build = root / 'build'
        build.mkdir(parents=True)
        (root / 'tex').mkdir()
        (root / 'provenance').mkdir()
        main = root / 'tex/main.tex'
        prepared = build / 'revised proof.tex'
        main.write_text('current main body', encoding='utf-8')
        prepared.write_text('current revised prepared proof', encoding='utf-8')
        rows = {str(path.relative_to(root)).replace('\\', '/'):
                {'bytes': path.stat().st_size, 'sha256': sha(path)}
                for path in (main, prepared)}
        pins = root / 'provenance/CURRENT_COMPILED_SOURCE_PINS.json'
        pins.write_text(json.dumps({'files': rows}), encoding='utf-8')
        external = container / 'external.tex'
        external.write_text('external authored source', encoding='utf-8')
        calls = []

        def fake_compile(command, **kwargs):
            calls.append(command)
            assert kwargs['cwd'] == root
            assert command[0] == 'isolated-xelatex'
            assert command[-1] == 'tex/main.tex'
            assert '-recorder' in command
            inputs = ['INPUT tex/main.tex', 'INPUT build/revised proof.tex',
                      'INPUT ' + str(main), 'INPUT build/reader.aux']
            (build / 'reader.aux').write_text('generated auxiliary', encoding='utf-8')
            if len(calls) == 3 and change == 'during':
                prepared.write_text('changed during compilation', encoding='utf-8')
            if change == 'membership':
                extra = root / 'tex/new.tex'
                extra.write_text('new dependency', encoding='utf-8')
                inputs.append('INPUT tex/new.tex')
            if change == 'external':
                inputs.append('INPUT ' + str(external))
            (build / 'reader.fls').write_text('\n'.join(inputs), encoding='utf-8')
            (build / 'reader.log').write_text('clean mock compile log', encoding='utf-8')
            (build / 'reader.pdf').write_bytes(b'ISOLATED MOCK PDF: NOT A REAL BUILD')
            return subprocess.CompletedProcess(command, 0, b'isolated mock compiler')

        if change == 'before':
            prepared.write_text('changed before compilation', encoding='utf-8')
        args = ['build_current_reader.py'] + (['--record-source-pins'] if authoring else [])
        error = None
        with patch.multiple(MODULE, ROOT=root, BUILD=build,
                            PDF=root / 'current.pdf', PINS=pins), \
             patch.object(MODULE.shutil, 'which', return_value='isolated-xelatex'), \
             patch.object(MODULE.subprocess, 'run', side_effect=fake_compile), \
             patch.object(sys, 'argv', args), \
             patch('fitz.open', return_value=FakeDocument()):
            try:
                MODULE.main()
            except RuntimeError as exc:
                error = str(exc)
        if expected_error:
            assert error and expected_error in error, (name, error)
            assert not (root / 'current.pdf').exists(), name
        else:
            assert error is None, (name, error)
            assert json.loads(pins.read_text(encoding='utf-8'))['files'] == rows
            assert (root / 'current.pdf').exists()
        assert len(calls) == (0 if change == 'before' else 3), (name, len(calls))
        return {'name': name, 'status': 'PASS', 'mock_compile_calls': len(calls),
                'observed_rejection': error}


results = [
    run_case('default_fixed_sources_and_relative_recorder'),
    run_case('precompile_changed_source_rejected', 'before', 'Current source changed'),
    run_case('postcompile_changed_source_rejected', 'during', 'Actual compiled source membership differs'),
    run_case('new_compiled_membership_rejected', 'membership', 'Actual compiled source membership differs'),
    run_case('external_authored_source_rejected', 'external', 'Authored source dependency outside'),
    run_case('authoring_records_current_relative_inputs', authoring=True),
]
report = {
    'scope': 'isolated mocked build workflow; no TeX execution and no mathematical-source or PDF acceptance',
    'reviewed_builder': str(SOURCE),
    'reviewed_builder_sha256': sha(SOURCE),
    'checks': results,
}
(HERE / 'PORTABLE_BUILDER_CHECKS.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'status': 'PASS', 'checks': len(results), 'actual_tex_runs': 0}))
