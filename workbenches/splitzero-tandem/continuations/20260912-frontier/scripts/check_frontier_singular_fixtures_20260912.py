"""Exact finite fixtures for the singular frontier and actual relative loss.

These finite checks supplement the proofs in the accompanying Markdown file.
They use explicit exceptions, so all checks remain active under python -O.
"""
import argparse
import json
from pathlib import Path

import sympy as s


records = []


def equal(label, left, right):
    difference = left - right
    if isinstance(difference, s.MatrixBase):
        valid = all(s.simplify(x) == 0 for x in difference)
    else:
        valid = s.simplify(difference) == 0
    if not valid:
        raise RuntimeError(f"{label}: {left!s} != {right!s}")
    records.append({"label": label, "passed": True})


def jordan_fixture(name, T, expected_cells=None):
    n, m = T.shape
    r = m // 2
    J = s.zeros(r).row_join(s.eye(r)).col_join(
        s.eye(r).row_join(s.zeros(r)))
    K = T.adjoint() * T
    A = J * K
    W = T * J * T.adjoint()
    d = m - K.rank()
    q = T.rank() - W.rank()
    equal(name + ": Hermitian W", W, W.adjoint())
    equal(name + ": kernel dimension", m - A.rank(), d)
    for index, vector in enumerate(K.nullspace()):
        equal(name + f": common kernel vector {index}", A * vector, s.zeros(m, 1))
    equal(name + ": exact intertwiner", W * T, T * A)
    equal(name + ": rank of square", (A * A).rank(), W.rank())
    equal(name + ": index at most two", (A ** 3).rank(), (A ** 2).rank())
    x = s.Symbol("x")
    equal(name + ": characteristic polynomial transport",
          x ** n * A.charpoly(x).as_expr(),
          x ** m * W.charpoly(x).as_expr())
    _, cells = A.jordan_cells()
    zero_cells = sorted([cell.rows for cell in cells if cell[0, 0] == 0])
    if zero_cells != sorted([2] * q + [1] * (d - q)):
        raise RuntimeError(name + ": zero block count mismatch")
    records.append({"label": name + ": zero block count", "passed": True,
                    "zero_blocks": zero_cells, "q": q, "kernel_dimension": d})
    if any(cell.rows != 1 for cell in cells if cell[0, 0] != 0):
        raise RuntimeError(name + ": nonzero Jordan block is not semisimple")
    records.append({"label": name + ": nonzero blocks semisimple", "passed": True})
    if expected_cells is not None and zero_cells != expected_cells:
        raise RuntimeError(f"{name}: expected zero blocks {expected_cells}, got {zero_cells}")
    return {"name": name, "T": str(T), "A": str(A), "W": str(W),
            "characteristic_polynomial": str(s.factor(A.charpoly(x).as_expr())),
            "zero_blocks": zero_cells, "q": q, "kernel_dimension": d}


def loss_fixture(name, Sg, So, F, E):
    d, r = F.shape
    G, Omega = Sg * Sg, So * So
    R = Sg.col_join(s.zeros(r, d))
    Tp = s.zeros(d, r).col_join(So)
    b = Tp - R * F
    H = b.adjoint() * b
    Y = -b * H.inv() * F.adjoint() * G
    C = b * Omega.inv() * E.adjoint() * G
    U, V = Sg * F * So.inv(), Sg * E * So.inv()
    Delta = Y.adjoint() * Y
    Pi = Sg.inv() * Delta * Sg.inv()
    Gnext = G - Delta
    chi = s.trace(G.inv() * C.adjoint() * C)
    W = -(Y.adjoint() * C + C.adjoint() * Y)
    equal(name + ": R Gram", R.adjoint() * R, G)
    equal(name + ": next-layer Gram", Tp.adjoint() * Tp, Omega)
    equal(name + ": orthogonality", Tp.adjoint() * R, s.zeros(r, d))
    equal(name + ": b Gram", H, Omega + F.adjoint() * G * F)
    equal(name + ": relative loss", Pi, U * (s.eye(r) + U.adjoint() * U).inv() * U.adjoint())
    equal(name + ": Woodbury complement", s.eye(d) - Pi, (s.eye(d) + U * U.adjoint()).inv())
    equal(name + ": determinant ratio", Gnext.det() / G.det(), 1 / (s.eye(d) + U * U.adjoint()).det())
    equal(name + ": tau", s.trace(G.inv() * Delta), s.trace(Pi))
    equal(name + ": chi", chi, s.trace(V.adjoint() * V) + s.trace((V * U.adjoint()).adjoint() * (V * U.adjoint())))
    equal(name + ": exact weight", Sg.inv() * W * Sg.inv(), U * V.adjoint() + V * U.adjoint())
    equal(name + ": geometric next representative", (R - Y).adjoint() * (R - Y), Gnext)
    return {"name": name, "G": str(G), "Omega": str(Omega), "F": str(F), "E": str(E),
            "relative_loss": str(Pi), "determinant_ratio": str(s.factor(Gnext.det() / G.det())),
            "tau": str(s.simplify(s.trace(Pi))), "chi": str(s.simplify(chi)),
            "relative_weight": str(s.simplify(Sg.inv() * W * Sg.inv()))}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--negative-control", action="store_true")
    parser.add_argument("--negative-case", choices=["nilpotent-square", "semisimple-zero", "chi-without-mixed-term"], default="nilpotent-square")
    args = parser.parse_args()
    if args.negative_control:
        if args.negative_case == "nilpotent-square":
            equal("deliberately incorrect nilpotent square", s.Matrix([[0, 0], [1, 0]]) ** 2, s.eye(2))
        elif args.negative_case == "semisimple-zero":
            jordan_fixture("deliberately incorrect semisimple-zero claim", s.Matrix([[1, 0]]), [1, 1])
        else:
            Sg, So = s.Matrix([[2, 1], [1, 2]]), s.diag(2, 3)
            F, E = s.Matrix([[1, 2], [-1, 1]]), s.Matrix([[s.I, 1], [2, -s.I]])
            realized = loss_fixture("negative-control actual geometric fixture", Sg, So, F, E)
            V = Sg * E * So.inv()
            equal("deliberately incorrect chi without mixed term", s.sympify(realized["chi"]), s.simplify(s.trace(V.adjoint() * V)))
        raise RuntimeError("Negative control unexpectedly reached normal execution")
    B = s.Matrix([[1, 0, 0, 0], [0, 2, 0, 0], [0, 0, 0, 3]])
    O = s.Matrix([[s.Rational(3, 5), s.Rational(4, 5)], [-s.Rational(4, 5), s.Rational(3, 5)]])
    Q = s.diag(O, O) * s.diag(s.I, 1, s.I, 1)
    fixtures = [
        jordan_fixture("all zero", s.zeros(1, 2), [1, 1]),
        jordan_fixture("one nilpotent block", s.Matrix([[1, 0]]), [2]),
        jordan_fixture("mixed nilpotent and real spectrum", B, [2]),
        jordan_fixture("complex mixed spectrum", B * Q, [2]),
        jordan_fixture("semisimple zero", s.Matrix([[1, 0, 1, 0]]), [1, 1, 1]),
        jordan_fixture("zero blocks of both lengths", s.Matrix([
            [1, 0, 0, 0, 0, 0], [0, 2, 0, 0, 0, 0],
            [0, 0, 0, 0, 3, 0], [0, 0, 1, 0, 0, 1]]), [1, 2]),
    ]
    Sg, So = s.Matrix([[2, 1], [1, 2]]), s.diag(2, 3)
    F, E = s.Matrix([[1, 2], [-1, 1]]), s.Matrix([[s.I, 1], [2, -s.I]])
    losses = [
        loss_fixture("complex noncommuting", Sg, So, F, E),
        loss_fixture("zero F", Sg, So, s.zeros(2), E),
        loss_fixture("zero E", Sg, So, F, s.zeros(2)),
        loss_fixture("rectangular frontier", Sg, s.diag(1, 2, 3),
                     s.Matrix([[1, 1, 0], [0, 1, 1]]),
                     s.Matrix([[0, s.I, 1], [1, 0, -s.I]])),
    ]
    args.output.write_text(json.dumps({"status": "passed", "check_count": len(records),
        "scope": "Exact finite fixtures, supplementary to written proofs; no arithmetic asymptotic estimate.",
        "jordan_fixtures": fixtures, "loss_fixtures": losses, "checks": records}, indent=2), encoding="utf-8")
    print(json.dumps({"status": "passed", "check_count": len(records), "output": str(args.output)}))


if __name__ == "__main__":
    main()
