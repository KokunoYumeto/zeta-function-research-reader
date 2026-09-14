#!/usr/bin/env python3
"""Compile the real local import closure and audit exact selected declarations."""
from __future__ import annotations
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
FORMAL = ROOT / 'formal/splitzero'
LOGS = FORMAL / '.observation-kernel-logs'
MODULES = ['SplitZeroObservationMetric', 'SplitZeroObservedIterates',
           'SplitZeroObservedIteratesSupport', 'SplitZeroCanonicalSignedResolvent',
           'SplitZeroBoundarySocleSupport', 'SplitZeroConormalTower']
TARGETS = {
 'SplitZero.ObservationMetric.Data': ['sectionMap', 'section_observation',
   'section_adjoint', 'section_gram', 'metric_section', 'residual',
   'residual_observation', 'kernel_section_orthogonal', 'residual_gram',
   'residual_difference_positive', 'fixed_section_correction', 'corrected_kernel_gram'],
 'SplitZero.ObservationMetric': ['ordered_factors'],
 'SplitZero.ObservedIterates': ['invisible', 'window', 'observe', 'mem_invisible',
   'mem_window', 'observe_apply', 'ker_observe', 'invisible_le_kernel', 'invariant',
   'largest_invariant', 'all_iterates_of_window', 'finite_determination',
   'quotientAction', 'quotient_action_mk', 'powers_intertwine', 'window_injective_iff',
   'rawRelations', 'invisibleRelations', 'actionHom', 'observationHom',
   'forgetIterates', 'action_square', 'observation_square', 'forget_square',
   'transient_kernel_retained', 'observed_zero_iff', 'observed_output_not_absent',
   'present_empty_face'],
 'SplitZero.RestrictedBoundary': ['original_square', 'range_iff_supported_zero', 'proper_residual'],
 'SplitZero.SignedTraceEnclosure': ['weighted_schwarz', 'signed_interval'],
}
ALLOWED = {'propext', 'Classical.choice', 'Quot.sound'}


def run(args: list[str], name: str) -> str:
    print('RUN', ' '.join(args), flush=True)
    proc = subprocess.run(args, cwd=FORMAL, text=True, stdout=subprocess.PIPE,
                          stderr=subprocess.STDOUT, timeout=420)
    (LOGS / (name + '.log')).write_text(proc.stdout, encoding='utf-8')
    print(proc.stdout, flush=True)
    if proc.returncode:
        raise RuntimeError(f'{name}: exit {proc.returncode}')
    return proc.stdout


def main() -> None:
    LOGS.mkdir(exist_ok=True)
    inherited = ROOT / 'workbenches/tau-signed-resolvent-formal/run_signed.py'
    spec = importlib.util.spec_from_file_location('inherited_screen', inherited)
    if spec is None or spec.loader is None:
        raise RuntimeError('Cannot load the unchanged source-token screen')
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    order: list[str] = []
    active: set[str] = set()
    seen: set[str] = set()
    def visit(name: str) -> None:
        if name in seen:
            return
        if name in active:
            raise ValueError('Import cycle: ' + name)
        active.add(name)
        code = mod.code_only((FORMAL / (name + '.lean')).read_text(encoding='utf-8'))
        if re.search(r'\b(sorry|admit|axiom|native_decide)\b', code):
            raise ValueError('Forbidden proof shortcut: ' + name)
        for line in code.splitlines():
            if line.startswith('import '):
                for dep in line.split()[1:]:
                    if (FORMAL / (dep + '.lean')).exists():
                        visit(dep)
        active.remove(name)
        seen.add(name)
        order.append(name)
    for name in MODULES:
        visit(name)
    output = FORMAL / '.lake/build/lib/lean'
    output.mkdir(parents=True, exist_ok=True)
    for name in order:
        run(['lake', 'env', 'lean', '--trust=0', '-DwarningAsError=true',
             '-o', str(output / (name + '.olean')), name + '.lean'], name)
    targets = [ns + '.' + t for ns, ts in TARGETS.items() for t in ts]
    if len(targets) != len(set(targets)):
        raise ValueError('Duplicate audit target')
    audit = '\n'.join(['import ' + m for m in MODULES] +
                      ['#print axioms ' + t for t in targets]) + '\n'
    (FORMAL / 'AuditObservationKernel.lean').write_text(audit, encoding='utf-8')
    text = run(['lake', 'env', 'lean', '--trust=0', '-DwarningAsError=true',
                'AuditObservationKernel.lean'], 'audit')
    matches = re.findall(r"'([^']+)' (?:depends on axioms:\s*\[([^\]]*)\]|does not depend on any axioms)", text, re.S)
    if len(matches) != len(targets) or {x[0] for x in matches} != set(targets):
        raise ValueError('Incomplete or unexpected audit coverage')
    axioms = {n: sorted(filter(None, re.split(r'[\s,]+', a.strip()))) for n, a in matches}
    for name, values in axioms.items():
        if not set(values) <= ALLOWED:
            raise ValueError(f'Unapproved axioms for {name}: {values}')
    receipt = {
      'commit': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip(),
      'strict_modules': order, 'selected_targets': len(targets), 'axioms': axioms,
      'sha256': {m: hashlib.sha256((FORMAL / (m + '.lean')).read_bytes()).hexdigest() for m in order},
      'scope': 'Constructed canonical observation section, full corrected kernel Gram, '
               'finite observed-iterate kernel, largest invariant submodule and original '
               'support quotient maps. No arithmetic periods, moment quadrature or '
               'tensor-uniform spectral estimate.'}
    (LOGS / 'receipt.json').write_text(json.dumps(receipt, indent=2, sort_keys=True) + '\n')
    print(json.dumps(receipt, indent=2, sort_keys=True), flush=True)

if __name__ == '__main__':
    try:
        main()
    except (RuntimeError, ValueError, OSError, subprocess.SubprocessError) as exc:
        print(str(exc), file=sys.stderr)
        raise SystemExit(1)
