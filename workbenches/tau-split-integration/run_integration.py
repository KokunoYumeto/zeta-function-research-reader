#!/usr/bin/env python3
"""Build and audit the actual dependency closure of the SplitZero integration."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2] / 'formal' / 'splitzero'
SPEC_PATH = ROOT / 'SPLIT_INTEGRATION_TARGETS.json'
sys.path.insert(0, str(ROOT))
from check_derived import audit, strip_comments

PINNED = {
    'SplitZero.lean': 'ff991f7383922e71cdf0e4a3bc85e89e18f808ef',
    'SplitZeroReconstruction.lean': '67501925618aad226644c4f67e15c7af7db9b4d7',
    'SplitZeroSupportChange.lean': '050241188f64fd5f5db9af733b6e49854ff9ff52',
    'SplitZeroSupportChangeIntegration.lean': '2446516c712133d43155245dac8a1e526a5c2dde',
    'SplitZeroInternalQuotient.lean': '908bd0e7d087864e4d004116fcbb4cd2751627be',
    'SplitZeroHomology.lean': '7b9e5c49a494dd0c751133e0234b3e01048f7b67',
    'SplitZeroMaps.lean': '337fb450d51004ee9e87a110c43f59cd4ee01c7d',
    'SplitZeroTauHomotopy.lean': '3552fa744b77f704896ecdd9e4cf029004f4e622',
    'SplitZeroConormalTower.lean': '0fac5346f0236316780230c085297946cd37e098',
    'SplitZeroLaplacianControl.lean': 'b22728cbb659e697b1e1296f753f75adac82b712',
    'lakefile.toml': '5b7815c62c2384d1e3b76a5c9ab0f9e05014f21c',
    'lean-toolchain': '18640c8b066b182147f324d3aefd8ee48ee45238',
}
JOINT = [
    'SplitZeroJointHomotopy', 'SplitZeroConormalTower', 'SplitZeroLaplacianControl',
    'SplitZeroHomologyExample', 'SplitZeroTauBase', 'SplitZeroRecovery',
]
PREFIX = 'SplitZero.Integration.'


def blob_hash(data: bytes) -> str:
    return hashlib.sha1(b'blob ' + str(len(data)).encode('ascii') + b'\0' + data).hexdigest()


def specification() -> tuple[dict[str, list[str]], list[str]]:
    spec = json.loads(SPEC_PATH.read_text(encoding='utf-8'))
    if not isinstance(spec, dict) or len(spec) != 4:
        raise ValueError('expected all four integrated source modules')
    names: list[str] = []
    for module, suffixes in spec.items():
        if not re.fullmatch(r'SplitZero[A-Za-z]+', module) or not suffixes:
            raise ValueError('invalid module manifest')
        data = (ROOT / (module + '.lean')).read_bytes()
        if b'\r' in data or data.startswith(b'\xef\xbb\xbf'):
            raise ValueError('noncanonical source encoding: ' + module)
        code = strip_comments(data.decode('utf-8'))
        if re.search(r'\b(sorry|admit|axiom|unsafe|implemented_by|native_decide)\b', code):
            raise ValueError('proof escape: ' + module)
        if re.search(r'\b(?:def|structure|inductive)\s+G\b', code):
            raise ValueError('replacement scalar definition: ' + module)
        for suffix in suffixes:
            if not isinstance(suffix, str) or not re.fullmatch(r'[A-Za-z_][A-Za-z_0-9]*', suffix):
                raise ValueError('invalid target suffix')
            names.append(PREFIX + suffix)
    if len(names) != len(set(names)):
        raise ValueError('duplicate audit declaration')
    return spec, names


def preserve_core() -> None:
    for name, expected in PINNED.items():
        actual = blob_hash((ROOT / name).read_bytes())
        if actual != expected:
            raise ValueError(f'inherited source changed without review: {name}: {actual}')


def closure(modules: list[str]) -> list[str]:
    seen: set[str] = set()
    active: set[str] = set()
    ordered: list[str] = []
    def visit(name: str) -> None:
        if name in seen:
            return
        if name in active:
            raise ValueError('cyclic local imports: ' + name)
        file = ROOT / (name + '.lean')
        if not file.is_file():
            raise ValueError('missing local import: ' + name)
        active.add(name)
        for line in strip_comments(file.read_text(encoding='utf-8')).splitlines():
            if line.startswith('import '):
                for dep in line.split()[1:]:
                    if dep.startswith('SplitZero'):
                        visit(dep)
        active.remove(name)
        seen.add(name)
        ordered.append(name)
    for module in modules:
        visit(module)
    return ordered


def selftest() -> None:
    name = PREFIX + 'test'
    expected = [name]
    valid = f"'{name}' depends on axioms: [propext, Quot.sound]"
    if audit(valid, expected)[name] != ['Quot.sound', 'propext']:
        raise ValueError('valid report changed')
    bad = [
        ('', expected),
        (valid + '\n' + valid, expected),
        (f"'{name}' depends on axioms: [sorryAx]", expected),
        (f"'{name}' depends on axioms: [Lean.ofReduceBool]", expected),
        (valid, []),
        (valid + "\n'SplitZero.unexpected' does not depend on any axioms", expected),
    ]
    for text, targets in bad:
        try:
            audit(text, targets)
        except ValueError:
            continue
        raise ValueError('audit accepted a deliberate malformed report')
    print(json.dumps({'audit_parser_cases': 7, 'status': 'passed'}, sort_keys=True))


def run(cmd: list[str], log: Path) -> str:
    print('RUN ' + ' '.join(cmd), flush=True)
    result = subprocess.run(cmd, cwd=ROOT, text=True, stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT, check=False, timeout=600)
    log.write_text(result.stdout, encoding='utf-8')
    print(result.stdout, flush=True)
    if result.returncode != 0:
        raise RuntimeError(f'failed with exit {result.returncode}: {cmd}')
    return result.stdout


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--selftest', action='store_true')
    parser.add_argument('--negative', action='store_true')
    args = parser.parse_args()
    if args.negative:
        audit("'SplitZero.Integration.test' depends on axioms: [sorryAx]",
              ['SplitZero.Integration.test'])
        raise RuntimeError('forbidden report was accepted')
    if args.selftest:
        selftest()
        return
    preserve_core()
    spec, targets = specification()
    modules = closure(list(spec) + JOINT)
    logs = ROOT / '.integration-logs'
    logs.mkdir(exist_ok=True)
    output = ROOT / '.lake' / 'build' / 'lib' / 'lean'
    output.mkdir(parents=True, exist_ok=True)
    for module in modules:
        run(['lake', 'env', 'lean', '--trust=0', '-DwarningAsError=true',
             '-o', str(output / (module + '.olean')), module + '.lean'],
            logs / (module + '.log'))
    text = ''.join('import ' + m + '\n' for m in list(spec) + JOINT)
    text += '\n' + ''.join('#print axioms ' + n + '\n' for n in targets)
    (ROOT / 'AuditSplitIntegration.lean').write_text(text, encoding='utf-8')
    log = run(['lake', 'env', 'lean', '--trust=0', '-DwarningAsError=true',
               'AuditSplitIntegration.lean'], logs / 'audit.log')
    reports = audit(log, targets)
    commit = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip()
    result = {
        'commit': commit, 'new_modules': list(spec), 'strict_dependency_closure': modules,
        'selected_new_targets': len(targets), 'axioms': reports,
        'source_sha256': {m: hashlib.sha256((ROOT / (m + '.lean')).read_bytes()).hexdigest()
                          for m in modules},
        'preserved_core_blobs': PINNED,
    }
    (logs / 'receipt.json').write_text(json.dumps(result, indent=2, sort_keys=True) + '\n')
    print(json.dumps(result, indent=2, sort_keys=True), flush=True)


if __name__ == '__main__':
    main()
