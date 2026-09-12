"""Exact repeated-root audit of the spectral-square parity quotients.

No zeta zero is asserted.  The two model packets are H(X)=(X-eta)^2,
eta in {-1,1}, and h(s)=((s-1/2)^2+eta)^2.  Original 1/16 and 1/4
coefficients and the entire mixed-nilpotent kernel generator are kept.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import sympy as S

x, delta, Z, r, s, w, z = S.symbols("x Delta Z r s w z")
checks = []


def eq(label, lhs, rhs):
    difference = lhs - rhs
    passed = all(S.simplify(a) == 0 for a in difference) if isinstance(difference, S.MatrixBase) else S.simplify(difference) == 0
    checks.append({"label": label, "passed": bool(passed)})


def condition(label, predicate):
    checks.append({"label": label, "passed": bool(predicate)})


def vectors(groebner, basis, polynomial):
    reduced = S.Poly(groebner.reduce(S.expand(polynomial))[1], x, delta)
    entries = S.Matrix([reduced.coeff_monomial(item) for item in basis])
    if S.expand(sum(entries[j] * basis[j] for j in range(len(basis))) - reduced.as_expr()) != 0:
        raise ValueError("Declared quotient basis does not span the remainder")
    return entries


def multiplication(groebner, basis, polynomial):
    return S.Matrix.hstack(*[vectors(groebner, basis, polynomial * monomial) for monomial in basis])


def truncate(expression, variable, degree):
    return S.rem(S.expand(expression), variable ** degree, variable)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    parser.add_argument("--negative-control", action="store_true")
    args = parser.parse_args()
    witnesses = []
    for eta in (-1, 1):
        label = f"eta={eta}"
        a = S.Integer(1) if eta == -1 else S.I
        A0 = S.expand(((delta - x + 4 * eta) ** 2 - 4 * x * delta) / 16)
        A1 = (delta - x + 4 * eta) / 4
        Q = S.expand(delta * A1)
        Q0 = Q.subs(x, 0)
        h_plus = (((Z + r) / 2) ** 2 + eta) ** 2
        h_minus = (((Z - r) / 2) ** 2 + eta) ** 2
        eq(label + ": original positive-coordinate relation", S.expand(h_plus), S.expand(A0.subs({x: -Z ** 2, delta: r ** 2}) + r * Z * A1.subs({x: -Z ** 2, delta: r ** 2})))
        eq(label + ": original negative-coordinate relation", S.expand(h_minus), S.expand(A0.subs({x: -Z ** 2, delta: r ** 2}) - r * Z * A1.subs({x: -Z ** 2, delta: r ** 2})))
        eq(label + ": branch polynomial with original coefficient", A0.subs(x, 0), (delta + 4 * eta) ** 2 / 16)

        even = S.groebner([A0, x * Q], x, delta, order="lex", domain=S.QQ)
        odd = S.groebner([A0, Q], x, delta, order="lex", domain=S.QQ)
        basis_e = [1, delta, delta ** 2, delta ** 3, delta ** 4, x]
        basis_o = [1, delta, delta ** 2, x]
        basis_k = [1, delta]
        eq(label + ": even leading monomials", S.Matrix([p.LM().exponents for p in even.polys]), S.Matrix([[2, 0], [1, 1], [0, 5]]))
        eq(label + ": odd leading monomials", S.Matrix([p.LM().exponents for p in odd.polys]), S.Matrix([[2, 0], [1, 1], [0, 3]]))
        eq(label + ": even dimension D(D+1)", len(basis_e), 2 * 3)
        eq(label + ": odd dimension D squared", len(basis_o), 2 ** 2)
        alpha = S.Matrix.hstack(*[vectors(even, basis_e, x * p) for p in basis_o])
        beta = S.Matrix.hstack(*[vectors(odd, basis_o, p) for p in basis_e])
        kernel = S.Matrix.hstack(*[vectors(even, basis_e, Q * p) for p in basis_k])
        alleged = S.Matrix.hstack(*[vectors(even, basis_e, Q0 * p) for p in basis_k])
        divisor = (delta + 4 * eta) ** 2
        cokernel = S.Matrix([[S.Poly(S.rem(S.sympify(p).subs(x, 0), divisor, delta), delta).coeff_monomial(b) for p in basis_e] for b in basis_k])
        mx_e, md_e = multiplication(even, basis_e, x), multiplication(even, basis_e, delta)
        mx_o, md_o = multiplication(odd, basis_o, x), multiplication(odd, basis_o, delta)
        md_k = S.Matrix([[0, -16], [1, -8 * eta]])
        eq(label + ": alpha injective rank", alpha.rank(), 4)
        eq(label + ": beta onto rank", beta.rank(), 4)
        eq(label + ": kernel parameter map injective", kernel.rank(), 2)
        eq(label + ": beta of exact kernel", beta * kernel, S.zeros(4, 2))
        eq(label + ": coker alpha onto", cokernel.rank(), 2)
        eq(label + ": cokernel after alpha", cokernel * alpha, S.zeros(2, 4))
        eq(label + ": alpha beta exact x", alpha * beta, mx_e)
        eq(label + ": beta alpha exact x", beta * alpha, mx_o)
        eq(label + ": full kernel Delta action", md_e * kernel, kernel * md_k)
        eq(label + ": x kills full kernel", mx_e * kernel, S.zeros(6, 2))
        eq(label + ": full cokernel Delta action", cokernel * md_e, md_k * cokernel)
        eq(label + ": x kills cokernel", cokernel * mx_e, S.zeros(2, 6))
        eq(label + ": Delta action alpha", md_e * alpha, alpha * md_o)
        eq(label + ": Delta action beta", md_o * beta, beta * md_e)
        condition(label + ": premature kernel generator fails", beta * alleged != S.zeros(4, 2))
        eq(label + ": explicit failed beta column", beta * alleged[:, 0], S.Matrix([0, eta, S.Rational(1, 4), 0]))
        tested_kernel = alleged if args.negative_control else kernel
        eq(label + ": selected generator satisfies beta=0", beta * tested_kernel, S.zeros(4, 2))

        # The same-root symmetric fibre is C[z]/(z^3).  The mixed-root
        # reflection-even fibre is C[w]/(w^3).  These literal substitutions
        # retain the second-order products of the original local jets.
        same = {x: 4 * eta - 4 * a * z - z ** 2, delta: -z ** 2}
        mixed = {x: w ** 2, delta: -4 * eta + 4 * a * w + w ** 2}
        chart_e = S.Matrix.hstack(*[S.Matrix([S.Poly(S.expand(S.sympify(p).subs(same)), z).nth(j) for j in range(3)] + [S.Poly(S.expand(S.sympify(p).subs(mixed)), w).nth(j) for j in range(3)]) for p in basis_e])
        chart_o = S.Matrix.hstack(*[S.Matrix([S.Poly(S.expand(S.sympify(p).subs(same)), z).nth(j) for j in range(3)] + [S.sympify(p).subs({x: 0, delta: -4 * eta})]) for p in basis_o])
        eq(label + ": even full-jet chart determinant", chart_e.det(), 2 ** 20)
        eq(label + ": odd full-jet chart determinant", chart_o.det(), 64 * a)
        eq(label + ": same-root A0", truncate(A0.subs(same), z, 3), 0)
        eq(label + ": same-root Q", truncate(Q.subs(same), z, 3), 0)
        eq(label + ": same-root premature Q", truncate(Q0.subs(same), z, 3), -eta * z ** 2)
        eq(label + ": mixed-root A0", truncate(A0.subs(mixed), w, 3), 0)
        eq(label + ": mixed-root xQ", truncate((x * Q).subs(mixed), w, 3), 0)
        eq(label + ": mixed-root Q coefficients", truncate(Q.subs(mixed), w, 3), -4 * a * eta * w - 4 * eta * w ** 2)
        eq(label + ": mixed-root premature Q coefficients", truncate(Q0.subs(mixed), w, 3), -4 * a * eta * w - 5 * eta * w ** 2)
        eq(label + ": mixed-root full length-two kernel", truncate((Q * (delta + 4 * eta)).subs(mixed), w, 3), 16 * w ** 2)
        eq(label + ": mixed-root kernel endpoint", truncate((Q * (delta + 4 * eta) ** 2).subs(mixed), w, 3), 0)

        # Explicit full reflection-even local unit: upsilon(y)=2+y^2.
        # This is a calibration unit, not a substitution for j_h(g/h).
        unit = 4 - x + delta + (x + delta) ** 2 / 16
        ue, uo = multiplication(even, basis_e, unit), multiplication(odd, basis_o, unit)
        c = 2 - eta
        eq(label + ": complete mixed unit coefficients", truncate(unit.subs(mixed), w, 3), c ** 2 + 2 * a * c * w - 2 * eta * w ** 2)
        inverse = S.Rational(1, c ** 2) - 2 * a * w / c ** 3 - S.Rational(2 * eta, c ** 4) * w ** 2
        eq(label + ": full mixed-unit inverse", truncate(unit.subs(mixed) * inverse, w, 3), 1)
        condition(label + ": full unit invertible even", ue.det() != 0)
        condition(label + ": full unit invertible odd", uo.det() != 0)
        eq(label + ": unit commutes through alpha", ue * alpha, alpha * uo)
        eq(label + ": unit commutes through beta", uo * beta, beta * ue)
        unit_k_poly = S.rem(unit.subs(x, 0), divisor, delta)
        unit_k = S.Matrix([[S.Poly(S.rem(unit_k_poly * b, divisor, delta), delta).coeff_monomial(c0) for b in basis_k] for c0 in basis_k])
        eq(label + ": full unit commutes through kernel map", ue * kernel, kernel * unit_k)
        eq(label + ": full unit commutes through cokernel map", cokernel * ue, unit_k * cokernel)
        witnesses.append({"eta": eta, "H": f"(X-({eta}))^2", "A0": str(A0), "A1": str(A1), "Q": str(Q), "even_groebner": list(map(str, even)), "odd_groebner": list(map(str, odd)), "even_basis": list(map(str, basis_e)), "odd_basis": list(map(str, basis_o)), "wrong_generator_beta": str(odd.reduce(Q0)[1]), "mixed_Q": str(truncate(Q.subs(mixed), w, 3)), "mixed_wrong_Q": str(truncate(Q0.subs(mixed), w, 3)), "same_root_wrong_Q": str(-eta * z ** 2), "unit_even_determinant": str(ue.det()), "unit_odd_determinant": str(uo.det())})

    failed = [check for check in checks if not check["passed"]]
    report = {"schema": "split-zero-spectral-square-parity-independent-v1", "sympy": S.__version__, "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), "scope": "Exact repeated-root polynomial calibrations only; no assertion that the model roots are xi zeros and no replacement of the actual arithmetic unit.", "mode": "negative-control" if args.negative_control else "ordinary", "checks": len(checks), "failed": len(failed), "failures": failed, "witnesses": witnesses, "details": checks}
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"checks": len(checks), "failed": len(failed), "output": str(output)}))
    raise SystemExit(1 if failed else 0)


if __name__ == "__main__":
    main()
