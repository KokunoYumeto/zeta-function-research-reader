"""One exact shell-rank calibration, with original weights and polynomial coordinates.

This is a finite discrete-measure fixture for KL.11--KL.18, not an arithmetic
zeta packet. --self-test-failure appends the false equality rank(C)=rank(raw
homogeneous shell); unittest checks remain active under optimized Python.
"""
from __future__ import annotations

import argparse
from functools import lru_cache
import hashlib
from itertools import product
import json
from pathlib import Path
import sys
import unittest

import sympy as sp


s, x, y = sp.symbols("s x y")
c = sp.Rational(1, 2)


def expanded(matrix):
    return sp.Matrix(matrix).applyfunc(sp.expand)


def at_packet(poly):
    return sp.expand(poly.subs({x: c, y: c}))


def matrix_record(matrix):
    matrix = sp.Matrix(matrix)
    return {"rows": matrix.rows, "cols": matrix.cols,
            "entries": [[str(matrix[i, j]) for j in range(matrix.cols)] for i in range(matrix.rows)]}


@lru_cache(None)
def fixture():
    heights = [-1, 0, 1]
    nodes = [c + sp.I * t for t in heights]
    omega1 = sp.eye(3)
    value1 = expanded([[node**j for j in range(3)] for node in nodes])
    moment1 = expanded(value1.H * omega1 * value1)
    monic = []
    norms = []
    for degree in range(3):
        coefficient = sp.zeros(3, 1)
        coefficient[degree] = 1
        if degree:
            lower = moment1[:degree, :degree].inv() * moment1[:degree, degree]
            for i in range(degree):
                coefficient[i] = -lower[i]
        monic.append(sp.expand(sum(coefficient[i] * s**i for i in range(3))))
        norms.append(sp.expand((coefficient.H * moment1 * coefficient)[0]))

    points = list(product(nodes, repeat=2))
    omega = sp.eye(9)
    exponents = [(0, 0), (0, 1), (1, 0), (0, 2), (1, 1), (2, 0)]
    raw_polynomials = [x**a * y**b for a, b in exponents]

    def values(polynomials):
        return expanded([[poly.subs({x: xx, y: yy}) for poly in polynomials] for xx, yy in points])

    raw_values = values(raw_polynomials)
    raw_old = raw_values[:, :3]
    raw_moment = expanded(raw_old.H * omega * raw_old)
    raw_jet = sp.Matrix([[at_packet(poly) for poly in raw_polynomials[:3]]])
    kernel = expanded(raw_jet * raw_moment.inv() * raw_jet.H)
    metric = expanded(kernel.inv())
    right_inverse_coefficient = expanded(raw_moment.inv() * raw_jet.H * metric)
    right_inverse = expanded(raw_old * right_inverse_coefficient)

    relation_coefficient = sp.Matrix.hstack(*raw_jet.nullspace())
    old_relations = expanded(raw_old * relation_coefficient)
    old_gram = expanded(old_relations.H * omega * old_relations)
    old_projector = expanded(old_relations * old_gram.inv() * old_relations.H * omega)

    orthogonal_polynomials = [sp.expand(monic[a].subs(s, x) * monic[b].subs(s, y))
                              for a, b in exponents]
    orthogonal_values = values(orthogonal_polynomials)
    orthogonal_jet = sp.Matrix([[at_packet(poly) for poly in orthogonal_polynomials]])
    actual_top_jet = orthogonal_jet[:, 1:3]
    raw_top_jet = raw_jet[:, 1:3]
    top_norm = sp.diag(norms[0] * norms[1], norms[1] * norms[0])
    upper_jet = orthogonal_jet[:, 3:6]
    upper_norm = sp.diag(norms[0] * norms[2], norms[1] * norms[1], norms[2] * norms[0])
    relation_layer = expanded(orthogonal_values[:, 3:6] - right_inverse * upper_jet)
    layer_gram = expanded(relation_layer.H * omega * relation_layer)

    packet_generator = sp.Matrix([[2 * c]])
    source_generator = sp.diag(*(xx + yy for xx, yy in points))
    defect = expanded(source_generator * right_inverse - right_inverse * packet_generator)
    projected_defect = expanded((sp.eye(9) - old_projector) * defect)
    incidence = sp.Matrix([[1, 0], [1, 1], [0, 1]])
    correct_factor = expanded(relation_layer * incidence * top_norm.inv() * actual_top_jet.H * metric)
    wrong_raw_factor = expanded(relation_layer * incidence * top_norm.inv() * raw_top_jet.H * metric)

    basis_change = sp.Matrix([[1, -c, -c], [0, 1, 0], [0, 0, 1]])
    raw_shell_gram = expanded(raw_old[:, 1:3].H * omega * raw_old[:, 1:3])
    constant_projector = right_inverse * sp.Rational(1, 9) * right_inverse.H * omega
    raw_to_actual_values = expanded((sp.eye(9) - constant_projector) * raw_old[:, 1:3])
    loss = expanded(relation_layer * layer_gram.inv() * relation_layer.H * omega * right_inverse)
    weight_form = expanded(packet_generator.H * metric + metric * packet_generator - 2 * metric)

    return locals()


class ShellNegativeCalibration(unittest.TestCase):
    def matrix_equal(self, left, right):
        difference = expanded(sp.Matrix(left) - sp.Matrix(right))
        self.assertEqual(difference, sp.zeros(difference.rows, difference.cols))

    def test_01_original_nodes_weights_and_unit(self):
        z = fixture()
        self.assertEqual(z["nodes"], [c - sp.I, c, c + sp.I])
        self.matrix_equal(z["omega1"], sp.eye(3))
        self.matrix_equal(z["omega"], sp.eye(9))
        self.assertEqual(len(z["points"]), 9)

    def test_02_monic_polynomials_and_original_norms(self):
        z = fixture()
        self.assertEqual(z["monic"], [sp.Integer(1), s - c, s**2 - s + sp.Rational(11, 12)])
        self.assertEqual(z["norms"], [sp.Integer(3), sp.Integer(2), sp.Rational(2, 3)])
        for p in z["monic"]:
            self.assertEqual(sp.Poly(p, s).LC(), 1)

    def test_03_full_product_polynomial_gram(self):
        z = fixture()
        self.matrix_equal(z["orthogonal_values"].H * z["omega"] * z["orthogonal_values"],
                          sp.diag(9, 6, 6, 2, 4, 2))
        self.assertEqual(z["raw_values"].rank(), 6)

    def test_04_original_raw_jet_and_minimum_right_inverse(self):
        z = fixture()
        self.matrix_equal(z["raw_jet"], [[1, c, c]])
        self.matrix_equal(z["right_inverse_coefficient"], [[1], [0], [0]])
        self.matrix_equal(z["right_inverse"], sp.ones(9, 1))
        self.matrix_equal(z["raw_jet"] * z["right_inverse_coefficient"], sp.eye(1))
        self.matrix_equal(z["kernel"], [[sp.Rational(1, 9)]])
        self.matrix_equal(z["metric"], [[9]])

    def test_05_old_relations_and_orthogonal_minimum(self):
        z = fixture()
        self.matrix_equal(z["relation_coefficient"], [[-c, -c], [1, 0], [0, 1]])
        self.matrix_equal(z["old_gram"], 6 * sp.eye(2))
        self.matrix_equal(z["old_relations"].H * z["omega"] * z["right_inverse"], sp.zeros(2, 1))
        self.matrix_equal(z["old_projector"]**2, z["old_projector"])

    def test_06_actual_top_rank_zero_raw_top_rank_one(self):
        z = fixture()
        self.matrix_equal(z["actual_top_jet"], [[0, 0]])
        self.matrix_equal(z["raw_top_jet"], [[c, c]])
        self.assertEqual(z["actual_top_jet"].rank(), 0)
        self.assertEqual(z["raw_top_jet"].rank(), 1)

    def test_07_full_exact_basis_change_keeps_lower_constant(self):
        z = fixture()
        self.matrix_equal(z["raw_old"] * z["basis_change"], z["orthogonal_values"][:, :3])
        self.matrix_equal(z["raw_jet"] * z["basis_change"], [[1, 0, 0]])
        self.matrix_equal(z["basis_change"].inv(), [[1, c, c], [0, 1, 0], [0, 0, 1]])
        self.matrix_equal(z["raw_to_actual_values"], z["orthogonal_values"][:, 1:3])
        self.matrix_equal(z["raw_shell_gram"], [[sp.Rational(33, 4), sp.Rational(9, 4)],
                                                [sp.Rational(9, 4), sp.Rational(33, 4)]])

    def test_08_actual_upper_relation_columns_and_gram(self):
        z = fixture()
        self.matrix_equal(z["upper_jet"], [[sp.Rational(2, 3), 0, sp.Rational(2, 3)]])
        expected = [(y - c)**2, (x - c) * (y - c), (x - c)**2]
        self.matrix_equal(z["relation_layer"], z["values"](expected))
        self.matrix_equal(z["old_projector"] * z["relation_layer"], sp.zeros(9, 3))
        self.matrix_equal(z["layer_gram"], [[6, 0, 4], [0, 4, 0], [4, 0, 6]])
        self.assertEqual(z["layer_gram"].det(), 80)
        self.assertEqual(z["relation_layer"].rank(), 3)

    def test_09_actual_gram_formula_and_representative_pairing(self):
        z = fixture()
        self.matrix_equal(z["layer_gram"], z["upper_norm"] + z["upper_jet"].H * z["metric"] * z["upper_jet"])
        self.matrix_equal(z["relation_layer"].H * z["omega"] * z["right_inverse"], [[-6], [0], [-6]])

    def test_10_unprojected_derivative_is_nonzero_old_relation(self):
        z = fixture()
        self.matrix_equal(z["packet_generator"], [[1]])
        self.matrix_equal(z["defect"], z["values"]([x + y - 1]))
        self.matrix_equal(z["defect"], z["old_relations"] * sp.ones(2, 1))
        self.matrix_equal(z["old_projector"] * z["defect"], z["defect"])
        self.assertEqual(z["defect"].rank(), 1)
        self.matrix_equal(z["defect"].H * z["omega"] * z["defect"], [[12]])

    def test_11_projected_derivative_has_exact_actual_top_rank(self):
        z = fixture()
        self.matrix_equal(z["projected_defect"], sp.zeros(9, 1))
        self.assertEqual(z["projected_defect"].rank(), z["actual_top_jet"].rank())
        self.assertEqual(z["projected_defect"].rank(), 0)

    def test_12_incidence_factorization_retains_actual_columns(self):
        z = fixture()
        self.assertEqual(z["incidence"].rank(), 2)
        self.matrix_equal(z["correct_factor"], z["projected_defect"])
        self.matrix_equal(z["top_norm"], 6 * sp.eye(2))

    def test_13_wrong_raw_substitution_changes_the_map_and_rank(self):
        z = fixture()
        self.assertNotEqual(z["projected_defect"].rank(), z["raw_top_jet"].rank())
        self.matrix_equal(z["wrong_raw_factor"], z["values"]([sp.Rational(3, 4) * (x + y - 1)**2]))
        self.assertEqual(z["wrong_raw_factor"].rank(), 1)
        self.matrix_equal(z["wrong_raw_factor"].H * z["omega"] * z["wrong_raw_factor"], [[sp.Rational(81, 4)]])
        self.assertNotEqual(z["wrong_raw_factor"], z["projected_defect"])

    def test_14_weight_loss_and_refined_rank_bound(self):
        z = fixture()
        self.assertEqual(z["loss"].rank(), 1)
        self.matrix_equal(z["loss"], z["relation_layer"] * sp.Matrix([-sp.Rational(3, 5), 0, -sp.Rational(3, 5)]))
        self.matrix_equal(z["loss"].H * z["omega"] * z["loss"], [[sp.Rational(36, 5)]])
        self.matrix_equal(z["weight_form"], sp.zeros(1, 1))
        self.assertEqual(2 * min(z["actual_top_jet"].rank(), z["upper_jet"].rank()), 0)

    def test_15_actual_unused_layer_quotient_dimension(self):
        z = fixture()
        self.assertEqual((z["top_norm"].inv() * z["actual_top_jet"].H).rank(), 0)
        self.assertEqual(z["relation_layer"].rank() - z["projected_defect"].rank(), 3)
        self.assertEqual(2 - z["actual_top_jet"].rank() + 1, 3)
        self.assertEqual(2 - z["raw_top_jet"].rank() + 1, 2)

    def test_16_finite_degree_scope_is_explicit(self):
        z = fixture()
        vanished_degree_three = (x - c) * ((x - c)**2 + 1)
        self.assertNotEqual(sp.expand(vanished_degree_three), 0)
        self.matrix_equal(z["values"]([vanished_degree_three]), sp.zeros(9, 1))


class DeliberatelyWrongRawShellEquality(unittest.TestCase):
    def runTest(self):
        z = fixture()
        self.assertEqual(z["projected_defect"].rank(), z["raw_top_jet"].rank(),
                         "Intentional false replacement of actual orthogonal shell by raw homogeneous monomials")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", type=Path)
    parser.add_argument("--self-test-failure", action="store_true")
    args = parser.parse_args()
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(ShellNegativeCalibration)
    if args.self_test_failure:
        suite.addTest(DeliberatelyWrongRawShellEquality())
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    z = fixture()
    fields = ["moment1", "raw_moment", "raw_jet", "kernel", "metric", "right_inverse_coefficient",
              "relation_coefficient", "old_gram", "actual_top_jet", "raw_top_jet", "top_norm",
              "upper_jet", "upper_norm", "layer_gram", "incidence", "basis_change", "raw_shell_gram"]
    record = {
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "sympy": sp.__version__, "python_optimization": sys.flags.optimize,
        "fixture": {"h": "s-1/2", "tensor_degree": 2, "polynomial_degree": 1,
                    "v": "1", "nodes": [str(a) for a in z["nodes"]], "weights": [1, 1, 1]},
        "monic_polynomials": [str(p) for p in z["monic"]], "original_squared_norms": [str(a) for a in z["norms"]],
        "exact_matrices": {field: matrix_record(z[field]) for field in fields},
        "ranks": {"actual_orthogonal_top": z["actual_top_jet"].rank(), "raw_homogeneous_top": z["raw_top_jet"].rank(),
                  "unprojected_derivative_defect": z["defect"].rank(), "projected_derivative_defect": z["projected_defect"].rank(),
                  "wrong_raw_factor": z["wrong_raw_factor"].rank(), "actual_next_layer": z["relation_layer"].rank()},
        "tests_run": result.testsRun, "failures": len(result.failures), "errors": len(result.errors),
        "success": result.wasSuccessful(), "deliberate_wrong_equality_control": args.self_test_failure,
        "scope": "One exact degree-two discrete-measure calibration of KL.11-KL.18; no arithmetic-zero, all-degree moment, or Lean certificate; raw rank replacement is intentionally rejected."
    }
    if args.json:
        args.json.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: record[key] for key in ["sympy", "python_optimization", "ranks", "tests_run", "failures", "errors", "success", "deliberate_wrong_equality_control"]}, sort_keys=True))
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    sys.exit(main())
