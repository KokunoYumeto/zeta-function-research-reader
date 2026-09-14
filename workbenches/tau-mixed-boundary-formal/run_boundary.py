#!/usr/bin/env python3
"""Strict actual socle/quotient audit; the inherited fail-closed parser is reused."""
from pathlib import Path
import hashlib
import json
import re
import subprocess
import sys

REPO = Path(__file__).resolve().parents[2]
ROOT = REPO / 'formal/splitzero'
sys.path.insert(0, str(ROOT))
from check_derived import audit, strip_comments

MODULES = ['SplitZeroBoundarySocle', 'SplitZeroBoundarySocleSupport']
JOINT_IMPORTS = ['SplitZeroCanonicalSourceContrast', 'SplitZeroJointHomotopy',
                 'SplitZeroConormalTower']
TARGETS = ['SplitZero.BoundarySocle.' + x for x in [
    'comparison', 'comparison_mk', 'comparison_killed', 'comparison_injective',
    'toSocle_surjective', 'socleEquiv', 'sourceAction', 'targetAction',
    'action_square', 'divide_intertwiner', 'powerDiagonal',
    'positive_exponent_factor', 'powerDiagonal_injective', 'diagonalSocleEquiv',
]] + ['SplitZero.BoundarySocleSupport.' + x for x in [
    'sourceRelations', 'targetRelations', 'comparisonHom', 'original_square',
    'total_injective', 'range_iff_supported_killed', 'present_empty_face',
]]


def run(cmd):
    proc = subprocess.run(cmd, cwd=ROOT, text=True, stdout=subprocess.PIPE,
                          stderr=subprocess.STDOUT)
    print(proc.stdout, flush=True)
    if proc.returncode:
        raise RuntimeError('failed: ' + repr(cmd))
    return proc.stdout


def unchanged(sources):
    """Never label a current source with an audit of different compiled bytes."""
    for module, original in sources.items():
        if (ROOT / (module + '.lean')).read_bytes() != original:
            raise RuntimeError('Source changed during boundary audit: ' + module)


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if argv not in ([], ['--joint']):
        raise ValueError('unknown arguments')
    joint = bool(argv)
    logdir = ROOT / '.boundary-socle-logs'
    receipt_path = logdir / ('joint.json' if joint else 'receipt.json')
    # Preserve the other mode's record, but never present this mode's prior
    # success as the outcome of a failed current invocation.
    receipt_path.unlink(missing_ok=True)
    sources = {m: (ROOT / (m + '.lean')).read_bytes() for m in MODULES}
    for module, raw in sources.items():
        text = strip_comments(raw.decode('utf-8'))
        if re.search(r'\b(sorry|admit|axiom|unsafe|implemented_by|native_decide)\b', text):
            raise ValueError('proof escape: ' + module)

    output = ROOT / '.lake/build/lib/lean'
    output.mkdir(parents=True, exist_ok=True)
    # Joint mode is independently usable after source edits: it rebuilds these
    # two checked modules instead of hashing sources beside stale boundary oleans.
    for module in MODULES:
        unchanged(sources)
        out = output / (module + '.olean')
        out.unlink(missing_ok=True)
        try:
            run(['lake', 'env', 'lean', '--trust=0', '-DwarningAsError=true',
                 '-o', str(out), module + '.lean'])
            unchanged(sources)
            if not out.is_file():
                raise RuntimeError('Compiler produced no boundary output: ' + module)
        except (RuntimeError, ValueError, OSError, subprocess.SubprocessError):
            out.unlink(missing_ok=True)
            raise

    imported_only = list(JOINT_IMPORTS) if joint else []
    body = ''.join('import ' + m + '\n' for m in MODULES + imported_only)
    body += '\n' + ''.join('#print axioms ' + n + '\n' for n in TARGETS)
    (ROOT / 'AuditBoundarySocle.lean').write_text(body, encoding='utf-8')
    text = run(['lake', 'env', 'lean', '--trust=0', '-DwarningAsError=true',
                'AuditBoundarySocle.lean'])
    reports = audit(text, TARGETS)
    unchanged(sources)
    record = {
        'commit': subprocess.check_output(['git', 'rev-parse', 'HEAD'],
                                          cwd=REPO, text=True).strip(),
        'modules': list(MODULES), 'strict_modules': list(MODULES),
        'imported_only_modules': imported_only,
        'targets': len(TARGETS), 'axioms': reports,
        'sha256': {m: hashlib.sha256(raw).hexdigest() for m, raw in sources.items()},
        'joint': joint,
        'build_scope': 'Both boundary modules were strictly rebuilt in this run. '
                       'Other imports use existing dependency builds; their full '
                       'source closure was not strictly rebuilt by this runner.',
        'scope': 'Constructed v-kernel equivalence for the actual '
                 'scalar-times-injective-map cokernel; diagonal lattice instance; '
                 'induced actions and natural original SplitZero quotient maps. '
                 'No l-adic inertia, period asymptotics or complete tensor-derived '
                 'functor is asserted.',
    }
    logdir.mkdir(exist_ok=True)
    receipt_path.write_text(
        json.dumps(record, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print(json.dumps(record, indent=2, sort_keys=True), flush=True)


if __name__ == '__main__':
    try:
        main()
    except (RuntimeError, ValueError, OSError, subprocess.SubprocessError) as exc:
        print(str(exc), file=sys.stderr)
        raise SystemExit(1)
