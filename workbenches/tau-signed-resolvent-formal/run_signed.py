#!/usr/bin/env python3
"""Strict dependency closure and exact transitive-axiom coverage."""
from __future__ import annotations
import hashlib
import json
import pathlib
import re
import subprocess
import sys
ROOT = pathlib.Path(__file__).resolve().parents[2]
FORMAL = ROOT / 'formal' / 'splitzero'
LOGS = FORMAL / '.signed-resolvent-logs'
MODULES = ['SplitZeroResolventSeries', 'SplitZeroSignedTraceEnclosure', 'SplitZeroRestrictedBoundary']
TARGETS = {
 'SplitZero.ResolventSeries': ['geometric_right', 'residual_exact', 'partialSum_zero',
  'blend_lower', 'blend_pos', 'blend_mono', 'tangent_bound', 'midpoint_deviation',
  'blend_contraction', 'contraction_range', 'centered_sum', 'variance_formula',
  'variance_nonneg', 'variance_le_energy', 'residual_variance_bound',
  'radius_tendsto_zero', 'exists_stopping_degree'],
 'SplitZero.SignedTraceEnclosure': ['MetricFrame.conjugate_mul', 'MetricFrame.trace_conjugate',
  'MetricFrame.hermitian_conjugate', 'MetricFrame.ofPosDef', 'hermitian_square_nonneg',
  'hermitian_schwarz_sq', 'weighted_schwarz', 'centered_pairing', 'weighted_center', 'signed_interval'],
 'SplitZero.RestrictedBoundary': ['killedRelations', 'residualRelations', 'quotientHom',
  'kernelDiagram', 'residualEquiv', 'kernelComparison', 'kernelInverse',
  'left_inverse_total', 'right_inverse_total', 'kernelInclusion', 'residualInclusion',
  'original_square', 'range_iff_supported_zero', 'proper_residual', 'present_empty_residual'],
}
ALLOWED = {'propext', 'Classical.choice', 'Quot.sound'}


EXTRA_MODULES = {
    'SplitZeroCanonicalSignedResolvent', 'SplitZeroSpectralResidual',
    'SplitZeroBoundarySocleSupport', 'SplitZeroSynchronization',
    'SplitZeroConormalTower', 'SplitZeroTauHomotopy',
}
EXTRA_TARGETS = {
    'SplitZero.CanonicalSignedResolvent': {
        'weighted_mul', 'weighted_pow', 'weighted_partialSum',
        'canonical_properties', 'canonical_interval',
        'canonical_resolvent_interval', 'canonical_tangent',
    },
    'SplitZero.SpectralResidual': {
        'frame_one', 'frame_sub', 'frame_smul', 'frame_pow', 'frame_center',
        'realTrace_diagonal', 'center_diagonal', 'residual_diagonal',
        'residual_energy', 'spectral_radius_bound', 'signed_error',
    },
}


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError('Duplicate configuration key: ' + key)
        result[key] = value
    return result


def load_scope(path: pathlib.Path):
    """Require the complete advertised scope before invoking any compiler."""
    raw = path.read_bytes()  # Missing configuration must not select a smaller run.
    config = json.loads(raw.decode('utf-8'), object_pairs_hook=unique_object)
    if not isinstance(config, dict) or set(config) != {'modules', 'targets'}:
        raise ValueError('Expected modules and targets configuration')
    modules = config['modules']
    if (not isinstance(modules, list)
            or any(not isinstance(m, str) for m in modules)
            or len(modules) != len(EXTRA_MODULES)
            or set(modules) != EXTRA_MODULES):
        raise ValueError('Missing, duplicate, or unexpected extra module')
    extra = config['targets']
    if not isinstance(extra, dict) or set(extra) != set(EXTRA_TARGETS):
        raise ValueError('Missing or unexpected extra namespace')
    for namespace, expected in EXTRA_TARGETS.items():
        names = extra[namespace]
        if (not isinstance(names, list)
                or any(not isinstance(name, str) for name in names)
                or len(names) != len(expected) or set(names) != expected):
            raise ValueError('Incomplete or unexpected target scope: ' + namespace)
    # Do not mutate the base lists: repeated calls have the same 9-root/60-target scope.
    all_modules = list(MODULES) + modules
    all_targets = {ns: list(names) for ns, names in TARGETS.items()}
    all_targets.update({ns: list(names) for ns, names in extra.items()})
    targets = [ns + '.' + name for ns, names in all_targets.items() for name in names]
    if len(all_modules) != 9 or len(targets) != 60 or len(set(targets)) != 60:
        raise ValueError('Advertised signed verification scope changed')
    return all_modules, all_targets, hashlib.sha256(raw).hexdigest()


def code_only(source: str) -> str:
    """Remove nested comments and strings before screening Lean tokens."""
    out: list[str] = []
    i = depth = 0
    string = False
    while i < len(source):
        if depth:
            if source.startswith('/-', i): depth += 1; i += 2
            elif source.startswith('-/', i): depth -= 1; i += 2
            else: i += 1
        elif string:
            if source[i] == '\\': i += 2
            elif source[i] == '"': string = False; i += 1
            else: i += 1
        elif source.startswith('--', i):
            end = source.find('\n', i)
            i = len(source) if end < 0 else end
        elif source.startswith('/-', i): depth = 1; i += 2; out.append(' ')
        elif source[i] == '"': string = True; i += 1; out.append(' ')
        else: out.append(source[i]); i += 1
    if depth or string: raise ValueError('Unterminated Lean comment or string')
    return ''.join(out)


def run(args: list[str], name: str) -> str:
    print('RUN', ' '.join(args), flush=True)
    proc = subprocess.run(args, cwd=FORMAL, text=True, stdout=subprocess.PIPE,
                          stderr=subprocess.STDOUT, timeout=360)
    (LOGS / (name + '.log')).write_text(proc.stdout, encoding='utf-8')
    print(proc.stdout, flush=True)
    if proc.returncode: raise RuntimeError(f'{name}: exit {proc.returncode}')
    return proc.stdout


def main() -> None:
    # A failed new invocation must not leave an old passing receipt at this path.
    (LOGS / 'receipt.json').unlink(missing_ok=True)
    extra = pathlib.Path(__file__).with_name('EXTRA_TARGETS.json')
    modules, target_groups, config_sha256 = load_scope(extra)
    LOGS.mkdir(exist_ok=True)
    order: list[str] = []
    active: set[str] = set()
    seen: set[str] = set()
    def visit(module: str) -> None:
        if module in seen: return
        if module in active: raise ValueError('Local import cycle: ' + module)
        active.add(module)
        code = code_only((FORMAL / (module + '.lean')).read_text(encoding='utf-8'))
        if re.search(r'\b(sorry|admit|axiom|native_decide)\b', code):
            raise ValueError('Forbidden proof shortcut: ' + module)
        for line in code.splitlines():
            if line.startswith('import '):
                for dependency in line.split()[1:]:
                    if (FORMAL / (dependency + '.lean')).exists(): visit(dependency)
        active.remove(module); seen.add(module); order.append(module)
    for module in modules: visit(module)
    output = FORMAL / '.lake' / 'build' / 'lib' / 'lean'
    output.mkdir(parents=True, exist_ok=True)
    failures = []
    for module in order:
        try:
            run(['lake', 'env', 'lean', '--trust=0', '-DwarningAsError=true',
                 '-o', str(output / (module + '.olean')), module + '.lean'], module)
        except RuntimeError as exc: failures.append(str(exc))
    if failures: raise RuntimeError('; '.join(failures))
    targets = [ns + '.' + name for ns, names in target_groups.items() for name in names]
    audit = '\n'.join(['import ' + m for m in modules] +
                      ['#print axioms ' + target for target in targets]) + '\n'
    (FORMAL / 'AuditSignedResolvent.lean').write_text(audit, encoding='utf-8')
    text = run(['lake', 'env', 'lean', '--trust=0', '-DwarningAsError=true',
                'AuditSignedResolvent.lean'], 'audit')
    pattern = r"'([^']+)' (?:depends on axioms:\s*\[([^\]]*)\]|does not depend on any axioms)"
    matches = re.findall(pattern, text, re.S)
    if len(matches) != len(targets) or {m[0] for m in matches} != set(targets):
        raise ValueError('Missing, duplicate, or unexpected axiom audit target')
    axioms = {name: sorted(filter(None, re.split(r'[\s,]+', names.strip())))
              for name, names in matches}
    for name, names in axioms.items():
        if not set(names) <= ALLOWED: raise ValueError(f'Unapproved axioms: {name}: {names}')
    receipt = {
      'commit': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip(),
      'strict_modules': order, 'root_modules': modules,
      'configuration_sha256': config_sha256,
      'targets': len(targets), 'axioms': axioms,
      'sha256': {m: hashlib.sha256((FORMAL / (m + '.lean')).read_bytes()).hexdigest() for m in order},
      'scope': 'Constructed finite resolvent and fixed-pair spectral residual; centered signed '
               'trace enclosure in the original source metric; natural proper-boundary '
               'quotient-kernel diagrams. No arithmetic moments or tensor-uniform estimate.'}
    (LOGS / 'receipt.json').write_text(json.dumps(receipt, indent=2, sort_keys=True) + '\n')
    print(json.dumps(receipt, indent=2, sort_keys=True))


if __name__ == '__main__':
    try: main()
    except (RuntimeError, ValueError, OSError, subprocess.SubprocessError) as exc:
        print(str(exc), file=sys.stderr)
        raise SystemExit(1)
