"""Independent exact germ and cubic spectral-Gram audit; no author imports."""
from pathlib import Path
import hashlib
import itertools
import json
import argparse
import sympy as s

HERE = Path(__file__).resolve().parent
checks = []
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--observe-source", action="store_true",
                    help="Also require the actual previously observed NS and quantum source files.")
parser.add_argument("--source-root", type=Path,
                    help="GCT repository root containing the recorded relative NS and quantum source paths; required with --observe-source.")
args = parser.parse_args()
if args.observe_source and args.source_root is None:
    parser.error("--observe-source requires --source-root")


def check(name, value):
    assert bool(value), name
    checks.append(name)


# The coordinate action is derived from S -> R S R^T on six original entries.
pairs = [(0, 0), (1, 1), (2, 2), (0, 1), (0, 2), (1, 2)]
basis = []
for i, j in pairs:
    b = s.zeros(3)
    b[i, j] = 1
    b[j, i] = 1
    basis.append(b)
actions = []
for perm in itertools.permutations(range(3)):
    for signs in itertools.product((-1, 1), repeat=3):
        R = s.zeros(3)
        for i in range(3):
            R[perm[i], i] = signs[i]
        check(f"coordinate orthogonality {perm} {signs}", R.T * R == s.eye(3))
        columns = []
        for b in basis:
            c = R * b * R.T
            columns.append(s.Matrix([c[i, j] for i, j in pairs]))
        T = s.Matrix.hstack(*columns)
        check(f"six-coordinate orthogonality {perm} {signs}", T.T * T == s.eye(6))
        actions.append(T)
check("48 cubic signed permutations", len(actions) == 48)

G = s.Matrix(6, 6, lambda i, j: s.Symbol(f"g{i}{j}"))
average = s.zeros(6)
for T in actions:
    average += T.T * G * T
average = average.applyfunc(lambda e: s.expand(e / 48))
d = sum(G[i, i] for i in range(3)) / 3
h = sum(G[i, j] for i in range(3) for j in range(3) if i != j) / 6
o = sum(G[i, i] for i in range(3, 6)) / 3
expected = s.zeros(6)
for i in range(3):
    for j in range(3):
        expected[i, j] = d if i == j else h
for i in range(3, 6):
    expected[i, i] = o
for i in range(6):
    for j in range(6):
        check(f"entire averaged spectral Gram entry {i},{j}", s.expand(average[i, j] - expected[i, j]) == 0)

dr, hr, ore = s.symbols("d h o", real=True)
Gr = s.zeros(6)
for i in range(3):
    for j in range(3):
        Gr[i, j] = dr if i == j else hr
for i in range(3, 6):
    Gr[i, i] = ore
re = s.symbols("a0:6", real=True)
im = s.symbols("b0:6", real=True)
v = s.Matrix([re[i] + s.I * im[i] for i in range(6)])
trace = sum(v[i] for i in range(3))
mean = trace / 3
norm2 = lambda x: s.expand(s.conjugate(x) * x)
weights = [norm2(trace) / 9, sum(norm2(v[i] - mean) for i in range(3)) / 2, sum(norm2(v[i]) for i in range(3, 6))]
direct = (s.conjugate(v).T * Gr * v)[0]
seed_formula = weights[0] * (3 * dr + 6 * hr) + weights[1] * 2 * (dr - hr) + weights[2] * ore
check("full complex spectral Gram modulus formula", s.expand(direct - seed_formula) == 0)

w = s.symbols("w", real=True)
qp = s.sqrt(1 - w**2 / 2) + s.I * w / s.sqrt(2)
qm = s.sqrt(1 - w**2 / 2) - s.I * w / s.sqrt(2)
check("germ q and inverse multiply to one", s.expand(qp * qm) == 1)
check("original eta germ", s.simplify(qp - qm - s.I * s.sqrt(2) * w) == 0)
check("local q derivative is nonzero", s.diff(qp, w).subs(w, 0) == s.I / s.sqrt(2))
zF = -s.I * s.sqrt(8) * w
tau = w**2
check("Fabel root agrees with NS root", s.simplify(-zF / 2 - s.I * s.sqrt(2) * w) == 0)
check("Fabel base equals NS base", s.expand(-zF**2 / 8 - tau) == 0)
check("continued Fabel time", s.expand((1 - zF**2) / 8 - (s.Rational(1, 8) + tau)) == 0)
check("sixth power phase", s.expand(zF**6 + 512 * tau**3) == 0)
check("source coefficient compound vector scale", -s.Rational(42) * -s.Rational(1, 512) == s.Rational(21, 256))
check("source coefficient compound measure scale", s.Rational(21, 256)**2 == s.Rational(441, 65536))

provenance_path = HERE / "input_provenance.json"
provenance = json.loads(provenance_path.read_text(encoding="utf-8"))
observed = {}
for key, suffix in [
    ("ns_bridge", "agents/ns_scaling_bridge/ns_scaling_bridge.tex"),
    ("quantum_tensor", "tex/quantum_tensor_symmetry.tex"),
]:
    matches = [item for item in provenance["sources"] if item["path"] == suffix]
    assert len(matches) == 1, ("unique observed source provenance", suffix)
    observed[key] = matches[0]["sha256"]
    if args.observe_source:
        assert hashlib.sha256((args.source_root / suffix).read_bytes()).hexdigest() == observed[key], (
            "previously observed source changed", suffix)
source_hashes = {
    **observed,
    "provenance": hashlib.sha256(provenance_path.read_bytes()).hexdigest(),
    "review": hashlib.sha256((HERE/"REVIEW.md").read_bytes()).hexdigest(),
    "composition": hashlib.sha256((HERE.parent/"ym_composition.tex").read_bytes()).hexdigest(),
}
receipt = {
    "status": "pass",
    "checks": len(checks),
    "independent_author_imports": False,
    "scope": "Exact local germ identities and entire six-state cubic spectral Gram complexification. Operator-domain arguments are given in REVIEW.md and the independent Hilbert audit; finite symbolic checks do not replace those proofs.",
    "source_hashes": source_hashes,
    "source_access_required": args.observe_source,
    "observation_mode": "rechecked recorded relative paths under the explicitly supplied source root" if args.observe_source else "portable local provenance and fully written equations; no external source access",
    "check_names": checks,
}
(HERE / ("source_observation.json" if args.observe_source else "verification.json")).write_text(
    json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"status": receipt["status"], "checks": receipt["checks"]}))
