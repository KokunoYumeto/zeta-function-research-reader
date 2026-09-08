"""Exact replay of the four-state graded relation; standard library only."""
from pathlib import Path
from itertools import product
import hashlib
import json
import runpy

HERE = Path(__file__).resolve().parent
audit = runpy.run_path(str(HERE / "audit" / "check_graded_paths.py"))
add, mul = audit["add"], audit["multiply"]
alpha, beta, gamma, delta = (audit[x] for x in ("alpha", "beta", "gamma", "delta"))
C = audit["C"]
p = audit["quantum"](2)

def mat_product(left, right):
    out = {}
    for (i, k), f in left.items():
        for (kk, j), g in right.items():
            if k == kk:
                out[i, j] = add(out.get((i, j), {}), mul(f, g))
    return {k: v for k, v in out.items() if v}

def shift(poly, n):
    return {w+n: v for w, v in poly.items()}

N = {(1, 0): alpha, (2, 0): beta, (3, 1): gamma, (3, 2): delta}
D = {(3, 0): C}
N2 = mat_product(N, N)
assert N2 == {(3, 0): mul(p, C)}
assert mat_product(N2, N) == {}
assert mat_product(N, D) == mat_product(D, N) == mat_product(D, D) == {}
weights_v, weights_w = (9, 7, 7, 5), (3, 3, 3, 3)
for (j, i), coeff in N.items():
    assert shift(coeff, weights_v[j]) == shift(coeff, weights_v[i]-2)
    assert weights_w[i] == weights_w[j]
assert weights_v[3] == weights_v[0]-4

# Exact no-solution proof over F_2, retaining each of the five arrows.
even_arrow_regradings = []
even_all_regradings = []
for s in product((0, 1), repeat=4):
    if all((next(iter(coeff)) + s[i]-s[j]) % 2 == 0
           for (j, i), coeff in N.items()):
        even_arrow_regradings.append(s)
        assert (s[3]-s[0]) % 2 == 1
        if (s[0]-s[3]) % 2 == 0:
            even_all_regradings.append(s)
assert len(even_arrow_regradings) == 2
assert even_all_regradings == []

# Full scalar compact-support degrees, twists and Kunneth labels.
scalar = {
    "x00": dict(cohomological_degree=2, internal_degree=-10, tate_twist=5),
    "x03": dict(cohomological_degree=7, internal_degree=-4, tate_twist=2),
    "x70": dict(cohomological_degree=15, internal_degree=4, tate_twist=-2),
    "x73": dict(cohomological_degree=20, internal_degree=10, tate_twist=-5),
}
scalar_character = {}
for v in scalar.values():
    assert v["internal_degree"] == -2*v["tate_twist"]
    scalar_character[v["internal_degree"]] = (-1)**v["cohomological_degree"]
assert scalar_character == C

residual_map = [
    ((6, 5), 0, 1, "x73"), ((6, 3), 0, -1, "x73"),
    ((-4, -5), 0, 1, "x00"), ((-6, -5), 0, -1, "x00"),
    ((7, -2), -1, 1, "x70"), ((5, -2), -1, -1, "x70"),
    ((-1, -2), -1, 1, "x03"), ((-3, -2), -1, -1, "x03"),
]
coho_differences = set()
for pair, source_degree, h_weight, label in residual_map:
    v = scalar[label]
    assert sum(pair) == h_weight + v["internal_degree"]
    assert source_degree % 2 == v["cohomological_degree"] % 2
    coho_differences.add(v["cohomological_degree"]-source_degree)
assert coho_differences == {2, 8, 16, 20}
assert len(coho_differences) > 1

proof = HERE / "frobenius_generator_bridge.tex"
certificate = {
    "status": "pass",
    "base_ring": "Z[q,q^-1]",
    "source_independent": True,
    "dependencies": ["Python standard library", "audit/check_graded_paths.py"],
    "checks": ["all four original coefficients", "N^2=[2]D", "N^3=ND=DN=D^2=0",
               "both original Cartan actions", "20 integral cone pairs and contraction",
               "original scalar cohomological degrees and Tate twists",
               "all eight Frobenius weight identifications",
               "no common shift repairs integer cohomological grading",
               "no diagonal regrading makes all five arrows integral Tate"],
    "scalar_compact_support": scalar,
    "even_first_arrow_regradings": even_arrow_regradings,
    "even_all_five_arrow_regradings": even_all_regradings,
    "unperiodized_cohomological_degree_differences": sorted(coho_differences),
    "proof_sha256": hashlib.sha256(proof.read_bytes()).hexdigest(),
    "scope": "Explicit finite-interval functors and the separately defined relation cone. "
             "This does not assert source geometric convolution or canonical-basis compatibility.",
}
(HERE / "certificate.json").write_text(json.dumps(certificate, indent=2)+"\n", encoding="utf-8")
print(json.dumps({"status": "pass", "path_pairs": 20, "endpoint_generators": 8,
                  "full_source_geometric_compatibility": "not established"}))
