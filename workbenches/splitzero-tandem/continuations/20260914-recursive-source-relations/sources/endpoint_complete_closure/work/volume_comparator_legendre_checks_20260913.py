"""Exact finite checks of VC.17--21; the Markdown proves all degrees."""
from pathlib import Path
import argparse
import hashlib
import json
import sys
import sympy as s


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    parser.add_argument("--fault", choices=["rodrigues-factor"])
    args = parser.parse_args()
    x = s.symbols("x")
    checks, failures = 0, []

    def check(name, value):
        nonlocal checks
        checks += 1
        if not bool(value):
            failures.append(name)

    for j in range(11):
        denominator = 2 ** (j + (args.fault == "rodrigues-factor")) * s.factorial(j)
        rod = s.Poly(s.diff((x*x-1)**j, x, j) / denominator, x)
        finite = s.expand(sum(s.binomial(j, a)**2*(x-1)**(j-a)*(x+1)**a
                              for a in range(j+1)) / 2**j)
        check(f"degree-{j}-Leibniz", s.expand(rod.as_expr()-finite) == 0)
        check(f"degree-{j}-leading",
              rod.LC() == s.factorial(2*j)/(2**j*s.factorial(j)**2))
        check(f"degree-{j}-norm",
              s.integrate(rod.as_expr()**2, (x,-1,1)) == s.Rational(2,2*j+1))
        check(f"degree-{j}-coefficient-envelope",
              sum(abs(a) for a in rod.all_coeffs()) <= 4**j)
        for d in range(j):
            check(f"degree-{j}-orthogonal-to-{d}",
                  s.integrate(rod.as_expr()*x**d, (x,-1,1)) == 0)

    proof = Path(__file__).with_name("volume_comparator_review_20260913.md")
    receipt = {
        "status": "passed" if not failures else "rejected",
        "checks": checks,
        "failures": failures,
        "fault": args.fault,
        "optimized": not __debug__,
        "proof_sha256": hashlib.sha256(proof.read_bytes()).hexdigest(),
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "scope": "Exact finite Rodrigues, Leibniz, leading coefficient, L2 norm, coefficient envelope, and orthogonality checks at degrees 0 through 10. The complete Markdown proves all degrees; this fixture does not test arithmetic asymptotics.",
    }
    Path(args.output).write_text(json.dumps(receipt, indent=2)+"\n", encoding="utf-8")
    print(json.dumps(receipt, indent=2))
    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(main())
