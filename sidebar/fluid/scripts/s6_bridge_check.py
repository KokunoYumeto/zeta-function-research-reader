"""Exact replay of the S6 comparative Fable polynomial and its velocity bridge.

The third original polynomial coordinate is t. Physical trajectory time is s.
No numerical time stepping, Lean, source-task changes, or publication is used.
"""
from pathlib import Path
import argparse
import hashlib
import json
import sympy as S

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--source-root', type=Path,
                    help='Optional original S6 source root to revalidate against frozen hashes.')
args = parser.parse_args()
provenance = json.loads((ROOT / 'sources' / 's6_source_hashes.json').read_text(encoding='utf-8'))
source_hashes = provenance['source_hashes']
source_revalidation = {'mode': 'frozen_provenance', 'original_sources_reread': False}
if args.source_root is not None:
    for item in source_hashes:
        source_file = args.source_root / item['relative_path']
        actual = hashlib.sha256(source_file.read_bytes()).hexdigest()
        assert actual == item['sha256'], f'Source hash mismatch: {item["relative_path"]}'
    source_revalidation = {'mode': 'original_sources_revalidated', 'original_sources_reread': True}
x, y, t, s, nu = S.symbols('x y t s nu', real=True)
coords = (x, y, t)
F = S.Matrix([
    (1 + x*y)**3*t + y**2*(1 + x*y)*(4 + 3*x*y),
    y + 3*x*(1 + x*y)**2*t + 3*x*y**2*(4 + 3*x*y),
    2*x - 3*x**2*y - x**3*t,
])
J = F.jacobian(coords)
det_J = S.expand(J.det())
assert det_J == -2
W = (J.adjugate() / det_J)[:, 0].applyfunc(S.expand)
assert (J*W - S.Matrix([1, 0, 0])).applyfunc(S.expand) == S.zeros(3, 1)

def curl(v):
    return S.Matrix([
        S.diff(v[2], y) - S.diff(v[1], t),
        S.diff(v[0], t) - S.diff(v[2], x),
        S.diff(v[1], x) - S.diff(v[0], y),
    ])

divergence = S.expand(sum(S.diff(W[i], coords[i]) for i in range(3)))
assert divergence == 0
grad_F3 = S.Matrix([S.diff(F[2], z) for z in coords])
potential = -F[1]*grad_F3 / 2
assert (curl(potential) - W).applyfunc(S.expand) == S.zeros(3, 1)

points = [
    (0, 0, -S.Rational(1, 4)),
    (1, -S.Rational(3, 2), S.Rational(13, 2)),
    (-1, S.Rational(3, 2), S.Rational(13, 2)),
]
images = [F.subs(dict(zip(coords, p))) for p in points]
assert all(q == S.Matrix([-S.Rational(1, 4), 0, 0]) for q in images)

# Positive q=1-4s preserves the real branch and avoids any branch cancellation.
q = S.symbols('q', positive=True)
gamma_q = S.Matrix([q**(-S.Rational(1, 2)), -S.Rational(3, 2)*S.sqrt(q), S.Rational(13, 2)*q])
gamma_dot_q = -4*gamma_q.diff(q)
gamma_subs = dict(zip(coords, gamma_q))
trajectory_residual = (W.subs(gamma_subs, simultaneous=True) - gamma_dot_q).applyfunc(S.expand)
assert trajectory_residual == S.zeros(3, 1)
gamma_image = F.subs(gamma_subs, simultaneous=True).applyfunc(S.expand)
assert gamma_image == S.Matrix([-q/4, 0, 0])

advection = W.jacobian(coords)*W
laplacian = W.applyfunc(lambda e: sum(S.diff(e, z, 2) for z in coords))
residual = advection - nu*laplacian
axis_curl = curl(residual).subs({x: 0, y: 0}).applyfunc(S.expand)
assert axis_curl == S.Matrix([0, 0, -18*nu*t])

# Full symbolic validation of the retained cusp matrix and inverse transpose.
alpha, eta, c, m, L, Q = S.symbols('alpha eta c m L Q', real=True)
D = L*Q + 6*m*m
P = S.Matrix([[6*alpha, eta, 1, 0], [6*m, L, 0, 0], [c, alpha, 0, 1], [-Q, m, 0, 0]])
PinvT = S.Matrix([
    [0, 0, 1, 0],
    [m/D, Q/D, (-6*m*alpha-Q*eta)/D, (-m*c-Q*alpha)/D],
    [0, 0, 0, 1],
    [-L/D, 6*m/D, 6*(L*alpha-m*eta)/D, (L*c-6*m*alpha)/D],
])
assert S.expand(P.det()) == -D
assert (P.T*PinvT - S.eye(4)).applyfunc(S.cancel) == S.zeros(4, 4)

payload = {
    'schema_version': 1,
    'audit_date': '2026-09-08',
    'source_task_title': 'S6 Proof Audit, Reconstruction & Overleaf Release',
    'source_root_name': provenance['source_root_name'],
    'scope': 'Bounded source audit and exact algebra/PDE bridge replay; no whole-repository proof certification.',
    'source_hashes': source_hashes,
    'source_revalidation': source_revalidation,
    's6_status': {
        'latest_local_status_date': '2026-09-06',
        'latest_workbench_claim': 'All six topology bridges closed; X diffeomorphic to S6, algebraic dimension 1, c3 pairing 2.',
        'latest_status_meaning': 'The source defines Verified as a complete proof written in the workbench, not community acceptance.',
        'older_main_tex_status': 'Unconfirmed/major revision; do not substitute this older audit verdict for current workbench status.',
        'independent_scope': 'Current claim located; terminal group triviality, source matrix identities, and explicit bridges independently checked. Global analytic gluing and integral geometric maps not re-audited in their entirety.',
        'locators': ['status.tex:145-154', 'status.tex:527-587', 'workbench.tex:314-347', 'main.tex:5989', 'main.tex:6241'],
    },
    'polynomial': {
        'original_coordinate_order': ['x', 'y', 't'],
        'physical_time_coordinate': 's',
        'F': [str(e) for e in F],
        'det_DF': str(det_J),
        'collision_points': [[str(e) for e in p] for p in points],
        'collision_images': [[str(e) for e in v] for v in images],
        'W_inverse_jacobian_first_column': [str(e) for e in W],
        'divergence_W': str(divergence),
        'potential': [str(e) for e in potential],
        'trajectory': ['(1-4*s)^(-1/2)', '-3*(1-4*s)^(1/2)/2', '13*(1-4*s)/2'],
        'trajectory_domain': 's < 1/4; positive real square root',
        'trajectory_image': ['s-1/4', '0', '0'],
        'trajectory_replay_residual': [str(e) for e in trajectory_residual],
        'euclidean_NS_steady_residual_curl_on_axis': [str(e) for e in axis_curl],
        'obstruction': 'For every nu>0, at (0,0,1) curl residual is (0,0,-18*nu), so no pressure makes W an unforced stationary Euclidean Navier-Stokes solution.',
        'admissibility': 'W is polynomial of degree 8 with infinite Euclidean energy and no unit-periodicity; compactly supported divergence-free localization is explicitly constructed in the Markdown audit.',
    },
    'cusp_replay': {
        'parameter_correspondence': {'Q': 'q_T', 'L': 'L_T', 'm': 'm_T', 'alpha': 'alpha_T', 'eta': 'eta_T', 'c': 'c_T'},
        'det_P': str(S.expand(P.det())),
        'inverse_transpose_identity': True,
        'fourier_to_NS_map': 'h([x])=f(<P_T^(-T)k,x>) maps to e_2*f(z_1) on unit T^3; source heat time is physical NS time divided by |P_T^(-T)k|^2.',
        'nonlinear_term': 'Identically zero on this shear sector.',
        'outcome': 'Exact globally smooth periodic Navier-Stokes solutions, not singular solutions.',
    },
    'conclusion': {
        'navier_stokes_disproof_verified': False,
        'concrete_maps_constructed': ['F pullback constant vector field', 'F pullback flat metric', 'compactly supported divergence-free localization', 'cusp Fourier circle sector to periodic NS shear sector'],
        'no_general_nonrelation_claim': True,
        'original_discovery_session_JSON_recovered': False,
        'this_JSON_kind': 'New exact calculation/audit record; not an original discovery transcript.',
    },
    'replay': {'sympy_version': S.__version__, 'all_assertions_passed': True},
}
out = ROOT / 'research' / 's6_bridge_audit.json'
out.write_text(json.dumps(payload, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
print(json.dumps({'all_assertions_passed': True, 'output': str(out), 'sympy_version': S.__version__}))
