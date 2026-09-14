"""Exact finite fixtures for RB.1--37; the Markdown supplies the general proof."""

from pathlib import Path
import hashlib
import json
import sympy as s


def main():
    x, S = s.symbols("x S")
    root_lists = [
        [s.Integer(0)],
        [s.Integer(1)],
        [s.Integer(-1), s.Integer(1)],
        [s.Integer(1)] * 3,
        [s.Rational(-1, 2), s.Rational(1, 2)] * 2,
        [s.Integer(0), s.Integer(1), s.Integer(1), s.Integer(-1), s.Integer(-1)],
        [s.Rational(-1, 2), s.Rational(1, 2)] * 3,
    ]
    checks = 0
    for roots in root_lists:
        q = len(roots)
        chi = s.Poly(s.prod(x - a for a in roots), x)
        h = [s.Integer(1)]
        for ell in range(1, q):
            h.append(s.expand(s.prod(1 / (1 - a * x) for a in roots))
                     .series(x, 0, ell + 1).removeO().coeff(x, ell))
        C = 2 ** q * s.binomial(2 * q - 1, q - 1) - 1
        for j in range(2 * q):
            quotient, rem = s.div(x ** j, chi.as_expr(), x)
            if j >= q:
                m = j - q
                proposed = sum(h[ell] * x ** (m - ell) for ell in range(m + 1))
                if s.expand(quotient - proposed) != 0:
                    raise RuntimeError(("quotient", roots, j))
                checks += 1
            norm = sum(abs(a) for a in s.Poly(rem, x).all_coeffs())
            if not bool(norm <= C):
                raise RuntimeError(("bound", roots, j, norm, C))
            checks += 1
        c, T = s.Rational(3, 2), s.Rational(5, 2)
        chiS = s.expand((s.I * T) ** q * chi.as_expr().subs(x, (S - c) / (s.I * T)))
        P = sum((j + 1 + s.I * (j % 3)) * S ** j for j in range(2 * q))
        rS = s.rem(P, chiS, S)
        AP = s.expand(P.subs(S, c + s.I * T * x))
        rx = s.rem(AP, chi.as_expr(), x)
        if s.expand(rx - rS.subs(S, c + s.I * T * x)) != 0:
            raise RuntimeError(("transport", roots))
        checks += 1
        for a in set(roots):
            for r in range(roots.count(a)):
                z = c + s.I * T * a
                if s.expand(s.diff(AP, x, r).subs(x, a)
                            - (s.I * T) ** r * s.diff(P, S, r).subs(S, z)) != 0:
                    raise RuntimeError(("phase", roots, r))
                if s.expand(s.diff(rS, S, r).subs(S, z)
                            - s.diff(P, S, r).subs(S, z)) != 0:
                    raise RuntimeError(("jet", roots, r))
                checks += 2
    directory = Path(__file__).resolve().parent
    proof = directory / "volume_remainder_bound_review_20260913.md"
    receipt = {
        "status": "passed",
        "checks": checks,
        "fixture_root_lists": [[str(a) for a in roots] for roots in root_lists],
        "domains": "Exact SymPy rational/complex polynomial division; repeated-root raw derivatives; original affine phase T=5/2,c=3/2",
        "proof_sha256": hashlib.sha256(proof.read_bytes()).hexdigest(),
        "scope": "Finite independent checks of the closed formulas. The Markdown contains the proof for every q>=1.",
    }
    (directory / "volume_remainder_bound_review_20260913.checks.json").write_text(
        json.dumps(receipt, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    main()
