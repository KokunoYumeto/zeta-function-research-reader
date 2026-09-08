"""Replay the 8,003 exact Gaussian-rational checks recorded in AUDIT.md.

Uses only the Python standard library. It reads no source mathematics and writes
only verification.json beside this script. The finite checks corroborate the
general proof in AUDIT.md; they do not replace that proof.
"""

from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path
from random import Random


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def scale(c, a):
    return (c * a[0], c * a[1])


def ip(a, b):
    """conjugate(a) * b, with the inner product linear in b."""
    return (a[0] * b[0] + a[1] * b[1], a[0] * b[1] - a[1] * b[0])


def norm(a):
    return ip(a, a)[0]


def total(xs):
    result = (F(0), F(0))
    for a in xs:
        result = add(result, a)
    return result


def main():
    r = Random(1301)
    checks = 0
    categories = {
        "diagonal_trace_decomposition": 0,
        "off_diagonal_pairing_identity": 0,
        "polarized_cubic_identity": 0,
        "nonnegative_weights": 0,
        "unchanged_seed_normalization": 0,
    }

    def verify(condition, category):
        nonlocal checks
        if not condition:
            raise AssertionError(f"Exact check failed: {category}, check {checks + 1}")
        checks += 1
        categories[category] += 1

    triples = ((0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1), (3, 5, 7))
    for _ in range(1000):
        # Entries are (S11,S22,S33,S12,S13,S23), retaining each complex entry.
        s = [(F(r.randrange(-9, 10)), F(r.randrange(-9, 10))) for k in range(6)]
        t = [(F(r.randrange(-9, 10)), F(r.randrange(-9, 10))) for k in range(6)]
        ds, dt = total(s[:3]), total(t[:3])
        sd = [add(v, scale(-F(1, 3), ds)) for v in s[:3]]
        td = [add(v, scale(-F(1, 3), dt)) for v in t[:3]]
        diag = total(ip(s[i], t[i]) for i in range(3))
        off = total(ip(s[i], t[j]) for i in range(3) for j in range(3) if i != j)
        cent = total(ip(sd[i], td[i]) for i in range(3))
        traces = ip(ds, dt)

        verify(diag == add(cent, scale(F(1, 3), traces)), "diagonal_trace_decomposition")
        verify(off == add(scale(-1, cent), scale(F(2, 3), traces)), "off_diagonal_pairing_identity")
        for n0, nd, no in triples:
            d = F(n0, 9) + F(nd, 3)
            h = F(n0, 9) - F(nd, 6)
            raw = add(
                add(scale(d, diag), scale(h, off)),
                scale(no, total(ip(s[i], t[i]) for i in range(3, 6))),
            )
            dec = add(
                add(scale(F(n0, 9), traces), scale(F(nd, 2), cent)),
                scale(no, total(ip(s[i], t[i]) for i in range(3, 6))),
            )
            verify(raw == dec, "polarized_cubic_identity")

        weights = (norm(ds) / 9, sum(norm(v) for v in sd) / 2, sum(norm(v) for v in s[3:]))
        verify(all(v >= 0 for v in weights), "nonnegative_weights")

    seeds = [
        [(1, 0), (1, 0), (1, 0), (0, 0), (0, 0), (0, 0)],
        [(1, 0), (-1, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
        [(0, 0), (0, 0), (0, 0), (1, 0), (0, 0), (0, 0)],
    ]
    for i, s0 in enumerate(seeds):
        s = [(F(a), F(b)) for a, b in s0]
        ds = total(s[:3])
        sd = [add(v, scale(-F(1, 3), ds)) for v in s[:3]]
        weights = (norm(ds) / 9, sum(norm(v) for v in sd) / 2, sum(norm(v) for v in s[3:]))
        verify(weights == tuple(F(int(j == i)) for j in range(3)), "unchanged_seed_normalization")

    # Receipt integrity checks are not included in the mathematical count.
    if checks != 8003 or sum(categories.values()) != checks:
        raise AssertionError("Unexpected exact-check count")
    script = Path(__file__).resolve()
    result = {
        "status": "pass",
        "exact_checks": checks,
        "complex_pairs": 1000,
        "seed": 1301,
        "arithmetic": "Gaussian rational pairs implemented with fractions.Fraction",
        "categories": categories,
        "nonnegative_seed_measure_triples": [list(triple) for triple in triples],
        "script": script.name,
        "script_sha256": sha256(script.read_bytes()).hexdigest(),
        "source_access_required": False,
        "role": "corroboration of the general proof in AUDIT.md",
    }
    output = script.with_name("verification.json")
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result))


if __name__ == "__main__":
    main()
