"""Exhaustive finite corroboration; arbitrary-ring proofs are in RECEIVERS.md."""
from itertools import product
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent

def canonical(labels):
    seen = {}
    return tuple(seen.setdefault(v, len(seen)) for v in labels)

def partitions(n):
    def extend(a):
        if len(a) == n:
            yield tuple(a)
            return
        for x in range(max(a) + 2):
            yield from extend(a + [x])
    yield from extend([0])

def model(n):
    tau, w, omega = n, n + 1, n + 2
    def add(x, y):
        if omega in (x, y): return omega
        if w in (x, y): return w
        if x == tau: return y
        if y == tau: return x
        return (x + y) % n
    def mul(x, y):
        if omega in (x, y): return omega
        if tau in (x, y): return tau
        if w in (x, y): return w
        return x * y % n
    return add, mul

report = {"scope": "Exact finite checks supplement, and do not replace, the general proofs.", "rings": []}
for n in (2, 3, 4):
    add, mul = model(n)
    xs = range(n + 3)
    for x, y in product(xs, repeat=2):
        assert add(x, y) == add(y, x)
        assert mul(x, y) == mul(y, x)
    for x in xs:
        assert add(n, x) == x
        assert mul(1, x) == x
    for x, y, z in product(xs, repeat=3):
        assert add(add(x, y), z) == add(x, add(y, z))
        assert mul(mul(x, y), z) == mul(x, mul(y, z))
        assert mul(x, add(y, z)) == add(mul(x, y), mul(x, z))
    found = set()
    checked = 0
    for p in partitions(n + 3):
        checked += 1
        if all(p[add(x, z)] == p[add(y, z)] and p[mul(x, z)] == p[mul(y, z)]
               for x in xs for y in xs if p[x] == p[y] for z in xs):
            found.add(p)
    expected = set()
    for d in range(1, n + 1):
        if n % d == 0:
            expected.add(canonical([("ring", r % d) for r in range(n)] + ["tau", "w", "Omega"]))
    expected.add(canonical(["c"] * n + ["tau", "c", "Omega"]))
    expected.add(canonical(["d"] * (n + 2) + ["Omega"]))
    expected.add((0,) * (n + 3))
    assert found == expected, {"n": n, "unexpected": list(found - expected), "missing": list(expected - found)}
    report["rings"].append({"R": f"Z/{n}Z", "carrier_size": n + 3,
                            "partitions_checked": checked, "congruences": len(found),
                            "axioms_and_full_classification": "passed"})

ops = {"P_E": (max, max), "P_U": (max, min)}
maps = []
for src, dst in (("P_E", "P_U"), ("P_U", "P_E")):
    sa, sm = ops[src]
    da, dm = ops[dst]
    valid = []
    for f in product((0, 1), repeat=2):
        if all(f[sa(x, y)] == da(f[x], f[y]) and f[sm(x, y)] == dm(f[x], f[y])
               for x, y in product((0, 1), repeat=2)):
            valid.append(f)
    assert valid == [(0, 0), (1, 1)]
    maps.append({"source": src, "target": dst, "all_binary_homomorphisms": valid})
report["order_comparisons"] = maps
report["status"] = "passed"
(ROOT / "FINITE_CHECKS.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report, indent=2))
