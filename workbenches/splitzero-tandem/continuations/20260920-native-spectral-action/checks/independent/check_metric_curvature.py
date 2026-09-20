"""Exact checks of MC1--MC34; no floating-point or arithmetic-packet claim."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import sympy as s


def run():
    count = 0
    negative = 0
    records = []
    t = s.symbols("t", real=True)
    z = s.symbols("z")
    imaginary = s.I

    def check_zero(value, label):
        nonlocal count
        entries = list(value) if isinstance(value, s.MatrixBase) else [value]
        if any(s.simplify(s.expand(x)) != 0 for x in entries):
            raise RuntimeError(f"Failed identity: {label}")
        count += 1

    def reject_zero(value, label):
        nonlocal negative
        entries = list(value) if isinstance(value, s.MatrixBase) else [value]
        if all(s.simplify(s.expand(x)) == 0 for x in entries):
            raise RuntimeError(f"Negative control unexpectedly passed: {label}")
        negative += 1

    for n in (2, 3, 4):
        for parameter in (1, 2):
            E = s.eye(n)
            B = s.zeros(n)
            for i in range(n):
                B[i, i] = i + 1
                for j in range(i + 1, n):
                    B[i, j] = parameter + imaginary * (j - i)
            G = B.conjugate().T * B
            Gi = G.inv()
            Bi = B.inv()

            def adj(X):
                return Gi * X.conjugate().T * G

            alpha = parameter + imaginary
            r = Bi * E[:, 0]
            ell = alpha * E[1, :] * B
            v = Gi * ell.conjugate().T
            Q = r * ell
            qa = adj(Q)
            aa = s.zeros(n)
            for i in range(n):
                aa[i, i] = i + parameter
                for j in range(i + 1, n):
                    aa[i, j] = (i + 1) * parameter + imaginary * (j + 1)
                    aa[j, i] = s.conjugate(aa[i, j])
            A = Bi * aa * B
            epsilon2 = s.simplify(s.trace(qa * Q))
            gamma = (ell * A * r)[0]
            ar = (r.conjugate().T * G * r)[0]
            bv = (ell * Gi * ell.conjugate().T)[0]
            T = A - t * Q
            Ta = adj(T)
            C = imaginary * (T - Ta)
            H = (T + Ta) / 2
            S = s.trace(Ta * T)
            J = s.trace(T * T)
            P = r * r.conjugate().T * G / ar + v * v.conjugate().T * G / bv
            expectedS = s.trace(A * A) - 2 * t * s.re(gamma) + t**2 * epsilon2
            expectedJ = s.trace(A * A) - 2 * t * gamma
            prefix = f"n={n}, parameter={parameter}"
            check_zero(ell * r, prefix + ": nilpotent contraction")
            check_zero(Q * Q, prefix + ": Q squared")
            check_zero(adj(A) - A, prefix + ": original adjoint")
            check_zero(qa - v * r.conjugate().T * G, prefix + ": rank-one adjoint")
            check_zero(epsilon2 - ar * bv, prefix + ": original metric factors")
            check_zero(S - expectedS, prefix + ": metric action")
            check_zero(J - expectedJ, prefix + ": holomorphic action")
            check_zero(s.diff(S, t) + 2 * s.re(gamma) - 2 * t * epsilon2,
                       prefix + ": first action derivative")
            check_zero(s.diff(S, t, 2) - 2 * epsilon2, prefix + ": second action derivative")
            check_zero(s.diff(J, t) + 2 * gamma, prefix + ": first holomorphic derivative")
            check_zero(s.diff(J, t, 2), prefix + ": second holomorphic derivative")
            check_zero(S - J - t**2 * epsilon2 - 2 * imaginary * t * s.im(gamma),
                       prefix + ": full complex difference")
            check_zero(adj(C) - C, prefix + ": defect adjoint")
            check_zero(C.diff(t) - imaginary * (qa - Q), prefix + ": defect derivative")
            check_zero(C.diff(t, 2), prefix + ": second defect derivative")
            check_zero(P * P - P, prefix + ": retained projection")
            check_zero(adj(P) - P, prefix + ": projection adjoint")
            check_zero(C * C - t**2 * epsilon2 * P, prefix + ": full defect square")
            check_zero(s.trace(C * C) - 2 * t**2 * epsilon2, prefix + ": defect trace")
            check_zero(s.trace(H * C) - 2 * t * s.im(gamma), prefix + ": mixed phase")
            check_zero(S - s.trace(H * H) - s.trace(C * C) / 4, prefix + ": metric split")
            check_zero(J - s.trace(H * H) + s.trace(C * C) / 4
                       + imaginary * s.trace(H * C), prefix + ": holomorphic split")

            zero = s.zeros(n)
            D = zero.row_join(T).col_join(Ta.row_join(zero))
            bigG = s.diag(G, G)
            Da = bigG.inv() * D.conjugate().T * bigG
            F = s.trace(D * D)
            check_zero(Da - D, prefix + ": dilation adjoint")
            check_zero(F - 2 * S, prefix + ": action morphism")
            check_zero(s.diff(F, t, 2) - 4 * epsilon2, prefix + ": full doubled Hessian")
            check_zero(s.diff(F, t, 2) / 2 - 2 * epsilon2,
                       prefix + ": half second derivative")
            Wraw = E.row_join(E).col_join(E.row_join(-E))
            target = H.row_join(imaginary * C / 2).col_join(
                (-imaginary * C / 2).row_join(-H))
            check_zero(Wraw * D * Wraw / 2 - target, prefix + ": retained defect blocks")
            check_zero(D[:n, n:] - T, prefix + ": original recovery")

            # All entries below are exact rational complex numbers. z=i is
            # outside the real spectrum of the specified selfadjoint dilation.
            T0 = s.simplify(T.subs(t, s.Rational(1, 3)))
            Ta0 = s.simplify(adj(T0))
            D0 = s.simplify(D.subs(t, s.Rational(1, 3)))
            Hp = s.simplify(T0 * Ta0)
            Hm = s.simplify(Ta0 * T0)
            Rp = (Hp + E).inv()
            Rm = (Hm + E).inv()
            resolvent = (imaginary * Rp).row_join(T0 * Rm).col_join(
                (Ta0 * Rp).row_join(imaginary * Rm))
            check_zero((D0 - imaginary * s.eye(2 * n)) * resolvent - s.eye(2 * n),
                       prefix + ": exact left resolvent")
            check_zero(resolvent * (D0 - imaginary * s.eye(2 * n)) - s.eye(2 * n),
                       prefix + ": exact right resolvent")
            check_zero(T0 * Rm - Rp * T0, prefix + ": first intertwiner")
            check_zero(Ta0 * Rp - Rm * Ta0, prefix + ": second intertwiner")
            minus_characteristic = Hm.charpoly(z).as_expr().subs(z, z**2)
            check_zero(D0.charpoly(z).as_expr() - minus_characteristic,
                       prefix + ": full characteristic polynomial")
            check_zero(Hm.det() - s.conjugate(T0.det()) * T0.det(),
                       prefix + ": original determinant modulus")
            reject_zero(s.diff(F, t, 2) / 2 - epsilon2,
                        prefix + ": wrong half-Hessian factor")
            reject_zero(qa - Q.conjugate().T,
                        prefix + ": dropping the original metric")
            reject_zero((D0 - imaginary * s.eye(2*n)) * (-resolvent) - s.eye(2*n),
                        prefix + ": wrong resolvent sign")
            records.append({"dimension": n, "parameter": parameter,
                            "epsilon_squared": str(epsilon2)})

    G = s.diag(2, 3)
    Q = s.Matrix([[0, 1], [0, 0]])
    A = s.Matrix([[1, 3 + 3 * imaginary], [2 - 2 * imaginary, 4]])
    adj = lambda X: G.inv() * X.conjugate().T * G
    T = A - t * Q
    C = imaginary * (T - adj(T))
    D = s.zeros(2).row_join(T).col_join(adj(T).row_join(s.zeros(2)))
    check_zero(s.trace(adj(T) * T) - (41 - 4*t + s.Rational(2, 3)*t**2),
               "MC32 metric example")
    check_zero(s.trace(T * T) - (41 - 4*t + 4*imaginary*t),
               "MC32 holomorphic example")
    check_zero(s.trace(C*C) - s.Rational(4, 3)*t**2, "MC32 defect example")
    check_zero((z*s.eye(2)-T).det() - (z**2 - 5*z - 8 + (2-2*imaginary)*t),
               "MC33 original polynomial")
    check_zero(D.charpoly(z).as_expr() -
               (z**4 - (41-4*t+s.Rational(2, 3)*t**2)*z**2 + 64-32*t+8*t**2),
               "MC33 dilation polynomial")
    reject_zero(s.diff(s.trace(T*T), t), "mixed trace does not vanish")
    reject_zero(s.im(s.trace(T*T)), "imaginary mixed term does not vanish")
    A0 = (Q + adj(Q)) / 2
    T0 = A0 - Q
    B0 = imaginary * T0
    C0 = imaginary * (T0 - adj(T0))
    check_zero(B0 - adj(B0), "MC34 generator selfadjoint")
    check_zero(B0 - C0/2, "MC34 exact extremizer")
    check_zero(B0.charpoly(z).as_expr() - (z**2-s.Rational(1, 6)),
               "MC34 sharp eigenvalue square")
    check_zero((2*s.sqrt(s.Rational(1, 6)))**2 - s.Rational(2, 3),
               "MC34 sharp aggregate square")
    return {"status": "PASS", "exact_identity_checks": count,
            "rejected_wrong_formula_controls": negative,
            "cases": records, "sympy_version": s.__version__,
            "scope": "Finite exact algebra; no growing-packet estimate or floating-point certification."}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run()
    rendered = json.dumps(result, indent=2)
    if args.output:
        args.output.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)
