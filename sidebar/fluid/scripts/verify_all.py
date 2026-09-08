"""Replay the bounded exact checks; analytic proofs remain in tex/.

No network access, Lean build, or sibling source workspace is required.
"""
from pathlib import Path
import hashlib
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = [
    's6_bridge_check.py',
    'check_inverse_fibre_heat.py',
    'check_material_generator.py',
    'check_material_endpoint.py',
    'check_s6_dynamics.py',
    'verify_arithmetic_fluid_bridge.py',
    'check_euler_coordinates.py',
    'check_boussinesq_core.py',
    'check_localized_layer.py',
    'check_viscous_strain.py',
    'check_swirl_carrier.py',
    'check_axis_transfer.py',
    'check_axis_gaussian.py',
    'check_forced_scaling.py',
    'euler_viscosity_bridge_check.py',
    'check_coupled_viscous.py',
    'check_web_audit.py',
    'check_arithmetic_heat.py',
    'check_arithmetic_bilaplacian_independent.py',
    'check_arithmetic_xi4.py',
    'check_gaussian_translation.py',
    'check_web_translation.py',
]
records = []
for filename in SCRIPTS:
    script = ROOT / 'scripts' / filename
    result = subprocess.run([sys.executable, str(script)], cwd=ROOT,
                            capture_output=True, text=True, encoding='utf-8')
    record = {
        'script': 'scripts/' + filename,
        'script_sha256': hashlib.sha256(script.read_bytes()).hexdigest(),
        'exit_code': result.returncode,
        'passed': result.returncode == 0,
    }
    records.append(record)
    print(filename + ': ' + ('PASS' if record['passed'] else 'FAIL'))
    if result.returncode:
        print(result.stdout)
        print(result.stderr, file=sys.stderr)
        raise SystemExit(result.returncode)

proofs = [{
    'file': p.relative_to(ROOT).as_posix(),
    'sha256': hashlib.sha256(p.read_bytes()).hexdigest(),
} for p in sorted((ROOT / 'tex').glob('*.tex')) if '_standalone' not in p.name]
report = {
    'schema_version': 1,
    'status': 'PASS',
    'scope': 'Exact symbolic identities, original polynomial certificate, and differential-operator calculations. This does not certify a Navier-Stokes disproof or the full released fluid proofs.',
    'runs': records,
    'proof_source_hashes': proofs,
    'lean_used': False,
    'navier_stokes_disproof_established': False,
}
(ROOT / 'checks' / 'replay_manifest.json').write_text(
    json.dumps(report, indent=2) + '\n', encoding='utf-8')
print(f'All {len(SCRIPTS)} replay scripts passed.')
