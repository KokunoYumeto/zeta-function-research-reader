#!/usr/bin/env python3
"""Strictly compile the original local closure and audit every selected new target."""
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
MODULES = ['SplitZeroResolventSeries', 'SplitZeroSignedTraceEnclosure']
TARGETS = {
    'SplitZero.ResolventSeries': [
        'geometric_right', 'residual_exact', 'partialSum_zero', 'blend_lower',
        'blend_pos', 'blend_mono', 'tangent_bound', 'midpoint_deviation',
        'blend_contraction', 'contraction_range', 'centered_sum', 'variance_formula',
        'variance_nonneg', 'variance_le_energy', 'residual_variance_bound',
        'radius_tendsto_zero', 'exists_stopping_degree'],
    'SplitZero.SignedTraceEnclosure': [
        'MetricFrame.conjugate_mul', 'MetricFrame.trace_conjugate',
        'MetricFrame.hermitian_conjugate', 'MetricFrame.ofPosDef',
        'hermitian_square_nonneg', 'hermitian_schwarz_sq', 'weighted_schwarz',
        'centered_pairing', 'weighted_center', 'signed_interval'],
}
ALLOWED = {'propext', 'Classical.choice', 'Quot.sound'}


def code_only(source: str) -> str:
    """Remove nested Lean comments and string literals before token screening."""
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
    if depth or string:
        raise ValueError('Unterminated Lean comment or string')
    return ''.join(out)


def run(args: list[str], name: str) -> str:
    print('RUN', ' '.join(args), flush=True)
    proc = subprocess.run(args, cwd=FORMAL, text=True, stdout=subprocess.PIPE,
                          stderr=subprocess.STDOUT, timeout=360)
    (LOGS / (name + '.log')).write_text(proc.stdout, encoding='utf-8')
    print(proc.stdout, flush=True)
    if proc.returncode:
        raise RuntimeError(f'{name}: exit {proc.returncode}')
    return proc.stdout


def main() -> None:
    LOGS.mkdir(exist_ok=True)
    order: list[str] = []
    active: set[str] = set()
    seen: set[str] = set()

    def visit(module: str) -> None:
        if module in seen: return
        if module in active: raise ValueError('Local import cycle: ' + module)
        active.add(module)
        path = FORMAL / (module + '.lean')
        code = code_only(path.read_text(encoding='utf-8'))
        if re.search(r'\b(sorry|admit|axiom|native_decide)\b', code):
            raise ValueError('Forbidden proof shortcut: ' + module)
        for line in code.splitlines():
            if line.startswith('import '):
                for dependency in line.split()[1:]:
                    if (FORMAL / (dependency + '.lean')).exists(): visit(dependency)
        active.remove(module)
        seen.add(module)
        order.append(module)

    for module in MODULES: visit(module)
    output = FORMAL / '.lake' / 'build' / 'lib' / 'lean'
    output.mkdir(parents=True, exist_ok=True)
    failures = []
    for module in order:
        try:
            run(['lake', 'env', 'lean', '--trust=0', '-DwarningAsError=true',
                 '-o', str(output / (module + '.olean')), module + '.lean'], module)
        except RuntimeError as exc:
            failures.append(str(exc))
    if failures: raise RuntimeError('; '.join(failures))
    targets = [ns + '.' + name for ns, names in TARGETS.items() for name in names]
    audit = '\n'.join(['import ' + m for m in MODULES] +
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
        if not set(names) <= ALLOWED:
            raise ValueError(f'Unapproved transitive axioms for {name}: {names}')
    receipt = {
        'commit': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip(),
        'strict_modules': order, 'targets': len(targets), 'axioms': axioms,
        'sha256': {m: hashlib.sha256((FORMAL / (m + '.lean')).read_bytes()).hexdigest()
                   for m in order},
        'scope': 'Finite resolvent residual and fixed-pair spectral convergence; centered signed '
                 'trace enclosure in the original positive source metric. No arithmetic moments, '
                 'source-path integrals, or tensor-uniform estimate are certified.'
    }
    (LOGS / 'receipt.json').write_text(json.dumps(receipt, indent=2, sort_keys=True) + '\n')
    print(json.dumps(receipt, indent=2, sort_keys=True))


if __name__ == '__main__':
    try: main()
    except (RuntimeError, ValueError, OSError, subprocess.SubprocessError) as exc:
        print(str(exc), file=sys.stderr)
        raise SystemExit(1)
