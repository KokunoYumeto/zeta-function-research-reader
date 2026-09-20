"""Independent exact-arithmetic checks of DS3--DS12.

Synthetic fixtures retain their declared positive Hermitian metric.  No
floating point, exponential sampler, source checker, or arithmetic-limit
assumption is used.  Run: python check_exact.py
"""

from math import factorial

import sympy as sp


COUNTS = {}


def check(name, condition):
    if not bool(condition):
        raise RuntimeError(f"Exact check failed: {name}")
    COUNTS[name] = COUNTS.get(name, 0) + 1


def equal_matrix(left, right):
    return (left - right).applyfunc(sp.simplify) == sp.zeros(*left.shape)


def expand_matrix(matrix):
    return matrix.applyfunc(sp.expand)


def adjoint(matrix, metric):
    return metric.inv() * matrix.conjugate().T * metric


def compositions(total, length):
    if length == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for rest in compositions(total - first, length - 1):
            yield (first,) + rest


def simplex_moment_by_ordered_integration(powers):
    """Integrate polynomial gaps using ordered times, not Dirichlet's formula."""
    n = len(powers) - 1
    times = sp.symbols(f"u1:{n + 1}")
    gaps = (1 - times[0],) + tuple(
        times[j] - times[j + 1] for j in range(n - 1)
    ) + (times[-1],)
    polynomial = sp.Poly(sp.prod(g ** p for g, p in zip(gaps, powers)), *times)
    result = sp.S.Zero
    for exponents, coefficient in polynomial.terms():
        exponents = list(exponents)
        value = coefficient
        for j in range(n - 1, -1, -1):
            power = exponents[j] + 1
            value /= power
            if j:
                exponents[j - 1] += power
        result += value
    return sp.cancel(result)


def check_simplex():
    for n in range(1, 5):
        for total in range(0, 5):
            for powers in compositions(total, n + 1):
                value = simplex_moment_by_ordered_integration(powers)
                expected = sp.Rational(
                    sp.prod(factorial(k) for k in powers), factorial(total + n)
                )
                check("ordered simplex moments", value == expected)


def fixture_two():
    metric = sp.diag(2, 3)
    matrix = sp.Matrix([[1, 3], [2, -1]])
    column = sp.Matrix([1, 0])
    row = sp.Matrix([[0, sp.Rational(2, 3)]])
    return metric, matrix, column, row


def fixture_three():
    # This is an explicit invertible coordinate transport of a synthetic
    # fixture, not an alteration of any supplied arithmetic object.
    coordinate_map = sp.Matrix([[1, 1, 0], [0, 2, 1], [0, 0, 1]])
    hermitian = sp.Matrix([[1, sp.I, 0], [-sp.I, -2, 1], [0, 1, 3]])
    column_zero = sp.Matrix([1, 0, 0])
    row_zero = sp.Matrix([[0, 1 + sp.I, 2]])
    metric = coordinate_map.conjugate().T * coordinate_map
    matrix = coordinate_map.inv() * hermitian * coordinate_map
    column = coordinate_map.inv() * column_zero
    row = row_zero * coordinate_map
    return metric, matrix, column, row


def check_dyson_words(matrix, relation):
    base = expand_matrix(matrix ** 2)
    insertion = expand_matrix(matrix * relation + relation * matrix)
    dimension = matrix.rows
    # Polynomial-in-t matrix multiplication is independent of simplex gaps.
    coefficients = [sp.eye(dimension)]
    for degree in range(0, 8):
        if degree:
            updated = [sp.zeros(dimension) for _ in range(degree + 1)]
            for index, coefficient in enumerate(coefficients):
                updated[index] += -base * coefficient
                updated[index + 1] += insertion * coefficient
            coefficients = [expand_matrix(value) for value in updated]
        for insertion_count in range(1, degree + 1):
            base_count = degree - insertion_count
            words = sp.zeros(dimension)
            for powers in compositions(base_count, insertion_count + 1):
                word = base ** powers[0]
                for exponent in powers[1:]:
                    word = expand_matrix(word * insertion * (base ** exponent))
                words += word
            predicted = (-1) ** base_count * words / factorial(degree)
            actual = coefficients[insertion_count] / factorial(degree)
            check("Dyson matrix word coefficients", equal_matrix(actual, predicted))
            check("Dyson trace word coefficients", sp.simplify(sp.trace(actual - predicted)) == 0)


def heat_coefficients(matrix, metric, count):
    positive = adjoint(matrix, metric) * matrix
    holomorphic = matrix ** 2
    positive_power = sp.eye(matrix.rows)
    holomorphic_power = sp.eye(matrix.rows)
    values = [sp.S.Zero]
    for _ in range(count):
        positive_power = expand_matrix(positive_power * positive)
        holomorphic_power = expand_matrix(holomorphic_power * holomorphic)
        value = sp.simplify(sp.trace(positive_power) - sp.re(sp.trace(holomorphic_power)))
        check("heat coefficients rational real", value.is_Rational)
        values.append(value)
    return values


def exponential_series_interval(matrix, metric, heat_time, bound, count):
    """Separate power-series enclosures; no DS8 coefficient estimate used."""
    positive = adjoint(matrix, metric) * matrix
    holomorphic = matrix ** 2
    positive_term = sp.eye(matrix.rows)
    holomorphic_term = sp.eye(matrix.rows)
    positive_sum = sp.trace(positive_term)
    holomorphic_sum = sp.trace(holomorphic_term)
    for n in range(1, count + 1):
        positive_term = expand_matrix(-heat_time * positive_term * positive / n)
        holomorphic_term = expand_matrix(-heat_time * holomorphic_term * holomorphic / n)
        positive_sum += sp.trace(positive_term)
        holomorphic_sum += sp.trace(holomorphic_term)
    center = sp.simplify(sp.re(holomorphic_sum) - positive_sum)
    x = heat_time * bound
    check("independent exponential tail ratio", x < count + 2)
    radius = 2 * matrix.rows * x ** (count + 1) / (
        factorial(count + 1) * (1 - x / (count + 2))
    )
    return center - radius, center + radius


def check_heat_bounds(metric, matrix, column, row):
    relation = column * row
    relation_adjoint = adjoint(relation, metric)
    epsilon_squared = sp.simplify(sp.trace(relation_adjoint * relation))
    check("specified metric selfadjointness", equal_matrix(adjoint(matrix, metric), matrix))
    check("rank-one relation square zero", equal_matrix(relation ** 2, sp.zeros(matrix.rows)))
    check("row column zero", (row * column)[0] == 0)
    check("positive rank-one norm square", epsilon_squared > 0)
    check_dyson_words(matrix, relation)

    for parameter in (sp.Rational(-2, 3), sp.Rational(1, 2), sp.S.One):
        target = matrix - parameter * relation
        dagger = adjoint(target, metric)
        a1 = sp.simplify(sp.trace(dagger * target) - sp.re(sp.trace(target ** 2)))
        check("real-parameter a1", a1 == parameter ** 2 * epsilon_squared)
        check("a1 antiadjoint identity", sp.simplify(
            sp.trace(adjoint(target - dagger, metric) * (target - dagger)) / 2 - a1
        ) == 0)
        check("nilpotent path square", equal_matrix(
            target ** 2,
            matrix ** 2 - parameter * (matrix * relation + relation * matrix),
        ))
        bound = sp.simplify(sp.trace(dagger * target))
        coefficients = heat_coefficients(target, metric, 12)
        for n in range(1, len(coefficients)):
            check("n(2n-1) coefficient bound", abs(coefficients[n]) <=
                  n * (2 * n - 1) * bound ** (n - 1) * a1)
        for x in (sp.Rational(1, 16), sp.Rational(1, 8), sp.Rational(2, 3)):
            heat_time = x / bound
            lower, upper = exponential_series_interval(target, metric, heat_time, bound, 26)
            for m in range(1, 7):
                if m + 1 <= 3 * x:
                    continue
                partial = sum((-1) ** (n + 1) * heat_time ** n * coefficients[n] /
                              factorial(n) for n in range(1, m + 1))
                radius = heat_time * a1 * (2 * m + 1) * x ** m / (
                    factorial(m) * (1 - 3 * x / (m + 1))
                )
                check("DS10 contains independent enclosure", lower >= partial - radius and
                      upper <= partial + radius)
            if x <= sp.Rational(1, 8):
                check("DS11 contains independent enclosure", lower >=
                      sp.Rational(4, 7) * heat_time * a1 and upper <=
                      sp.Rational(10, 7) * heat_time * a1)


def check_tail_indices():
    for x in (sp.S.Zero, sp.Rational(1, 8), sp.Rational(2, 3), sp.Rational(7, 2)):
        for m in range(1, 15):
            if m + 1 <= 3 * x:
                continue
            first = (2 * m + 1) * x ** m / factorial(m)
            check("first omitted tail index", first ==
                  (2 * (m + 1) - 1) * x ** ((m + 1) - 1) / factorial((m + 1) - 1))
            for n in range(m + 1, m + 20):
                if not x:
                    continue
                bn = (2 * n - 1) * x ** (n - 1) / factorial(n - 1)
                bn_next = (2 * n + 1) * x ** n / factorial(n)
                exact_ratio = x * (2 * n + 1) / (n * (2 * n - 1))
                check("exact tail ratio", sp.cancel(bn_next / bn) == exact_ratio)
                check("geometric ratio majorant", exact_ratio <= 3 * x / (m + 1) < 1)
            finite_tail = sum((2 * n - 1) * x ** (n - 1) / factorial(n - 1)
                              for n in range(m + 1, m + 30))
            check("finite positive tail below geometric bound", finite_tail <=
                  first / (1 - 3 * x / (m + 1)))


def check_metric_transport():
    original_metric, original_a, column, row = fixture_three()
    original_t = original_a - sp.Rational(2, 3) * column * row
    conductor = sp.Matrix([[1, 2, 0], [0, 1, 1], [1, 0, 1]])
    target_metric = sp.diag(2, 3, 5)
    transported_metric = conductor.conjugate().T * target_metric * conductor
    target_t = conductor * original_t * conductor.inv()
    target_adjoint = adjoint(target_t, target_metric)
    source_adjoint = adjoint(original_t, transported_metric)
    check("DS12 adjoint transport", equal_matrix(
        target_adjoint, conductor * source_adjoint * conductor.inv()))
    check("transport metric differs from original", transported_metric != original_metric)
    for n in range(0, 7):
        check("DS12 positive heat coefficient transport", sp.simplify(
            sp.trace((target_adjoint * target_t) ** n) -
            sp.trace((source_adjoint * original_t) ** n)) == 0)
        check("holomorphic coefficient similarity invariance", sp.simplify(
            sp.trace(target_t ** (2 * n)) - sp.trace(original_t ** (2 * n))) == 0)
    wrong_coefficient = sp.simplify(
        sp.trace(adjoint(original_t, original_metric) * original_t) -
        sp.trace(source_adjoint * original_t)
    )
    check("untransported metric changes positive action", wrong_coefficient != 0)


def truncated_polynomial_product(left, right):
    """Multiply matrix polynomials, retaining powers t^0 through t^2."""
    dimension = left[0].rows
    result = [sp.zeros(dimension) for _ in range(3)]
    for i in range(3):
        for j in range(3 - i):
            result[i + j] += left[i] * right[j]
    return [expand_matrix(coefficient) for coefficient in result]


def check_curvature():
    coordinate_map = sp.Matrix([[1, 1, 0], [0, 2, 1], [0, 0, 1]])
    metric = coordinate_map.conjugate().T * coordinate_map
    eigenvalues = [sp.S(2), sp.S(-2), sp.S.Zero]
    diagonal = sp.diag(*eigenvalues)
    column_zero = sp.Matrix([1, sp.I, 1])
    row_zero = sp.Matrix([[1, sp.I, 0]])
    q_zero = column_zero * row_zero
    matrix = coordinate_map.inv() * diagonal * coordinate_map
    relation = coordinate_map.inv() * q_zero * coordinate_map
    dagger = adjoint(relation, metric)
    zero = sp.zeros(3)
    base = expand_matrix(matrix ** 2)
    holomorphic = [base, expand_matrix(-matrix * relation - relation * matrix), zero]
    positive = [base, expand_matrix(-matrix * relation - dagger * matrix),
                expand_matrix(dagger * relation)]
    holomorphic_power = [sp.eye(3), zero, zero]
    positive_power = [sp.eye(3), zero, zero]
    c_zero = q_zero - q_zero.conjugate().T
    squared_eigenvalues = [a ** 2 for a in eigenvalues]
    kappa = sp.simplify(sp.trace(dagger * relation))
    lambda_value = sp.simplify(sp.trace(adjoint(matrix * relation, metric) * matrix * relation)
                             + sp.trace(adjoint(relation * matrix, metric) * relation * matrix))
    check("curvature square-zero fixture", equal_matrix(relation ** 2, zero))
    check("curvature metric selfadjointness", equal_matrix(adjoint(matrix, metric), matrix))
    check("curvature confluent squared nodes retained", squared_eigenvalues[0] ==
          squared_eigenvalues[1] and eigenvalues[0] != eigenvalues[1])
    check("curvature antiadjoint total weight", sp.trace(c_zero.conjugate().T * c_zero) == 2 * kappa)
    for n in range(1, 11):
        holomorphic_power = truncated_polynomial_product(holomorphic_power, holomorphic)
        positive_power = truncated_polynomial_product(positive_power, positive)
        direct = sp.simplify(sp.Rational(2 * (-1) ** n, factorial(n)) * (
            sp.re(sp.trace(holomorphic_power[2])) - sp.trace(positive_power[2])))
        predicted_sum = sp.S.Zero
        for i in range(3):
            for j in range(3):
                node_sum = sum(squared_eigenvalues[i] ** k *
                               squared_eigenvalues[j] ** (n - 1 - k) for k in range(n))
                predicted_sum += sp.expand(sp.conjugate(c_zero[i, j]) * c_zero[i, j]) * node_sum
        predicted = (-1) ** (n - 1) * predicted_sum / factorial(n - 1)
        check("curvature coefficients contain no floats", not direct.atoms(sp.Float) and
              not predicted.atoms(sp.Float))
        check("curvature exact heat-series coefficient", sp.simplify(direct - predicted) == 0)
        if n == 1:
            check("curvature leading coefficient", direct == 2 * kappa)
        if n == 2:
            check("curvature next coefficient", direct == -2 * lambda_value)
    # A scalar A has the exact sign factor (1 - s a^2); the exponential
    # and all other factors are positive for positive rational s, kappa.
    scalar_a = sp.Rational(3, 2)
    for scaled_heat, expected_sign in ((sp.Rational(1, 2), 1), (sp.S.One, 0), (sp.S(2), -1)):
        heat_time = scaled_heat / scalar_a ** 2
        check("sharp curvature threshold sign", sp.sign(1 - heat_time * scalar_a ** 2) == expected_sign)


def main():
    print("START ordered simplex checks", flush=True)
    check_simplex()
    for index, fixture in enumerate((fixture_two(), fixture_three()), start=1):
        print(f"START metric fixture {index}", flush=True)
        check_heat_bounds(*fixture)
    print("START rational tail checks", flush=True)
    check_tail_indices()
    print("START exact metric transport checks", flush=True)
    check_metric_transport()
    print("START exact curvature checks", flush=True)
    check_curvature()
    for name in sorted(COUNTS):
        print(f"PASS {COUNTS[name]:4d}  {name}")
    print(f"PASS {sum(COUNTS.values())} exact checks; no floating point used.")


if __name__ == "__main__":
    main()
