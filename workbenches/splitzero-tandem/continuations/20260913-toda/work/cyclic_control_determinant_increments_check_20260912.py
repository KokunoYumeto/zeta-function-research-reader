"""Exact finite positive-measure replay of CV.1--CV.6 and CV.10--CV.10a.

This is not an evaluation of the arithmetic Xi measure.  It retains a
specified positive measure, its mass, monic coordinates, and every norm.
All tests use explicit exceptions; python -O runs the same checks.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from pathlib import Path
import platform
import sys

import sympy as sp

S, u = sp.symbols("S u", real=True)
I = sp.I
checks = []


def exact(expression):
    return sp.cancel(sp.expand(expression))


def check_equal(name, actual, expected):
    if isinstance(actual, sp.MatrixBase) or isinstance(expected, sp.MatrixBase):
        a, b = sp.Matrix(actual), sp.Matrix(expected)
        if a.shape != b.shape:
            raise RuntimeError(f"{name}: incompatible shapes {a.shape}, {b.shape}")
        residual = (a - b).applyfunc(exact)
        if any(value != 0 for value in residual):
            raise RuntimeError(f"{name}: nonzero residual {residual}")
    else:
        residual = exact(actual - expected)
        if residual != 0:
            raise RuntimeError(f"{name}: nonzero residual {residual}")
    checks.append(name)


def check_true(name, condition):
    if condition is not True and condition != sp.true:
        raise RuntimeError(f"{name}: condition failed: {condition}")
    checks.append(name)


def gaussian_moment(n, shift):
    # Integral u^n exp(-(u-shift)^2) du / sqrt(pi), derived by binomial
    # expansion and integration by parts for centered even moments.
    return sp.Add(*(
        sp.binomial(n, 2*j) * shift**(n-2*j)
        * sp.factorial(2*j) / (4**j * sp.factorial(j))
        for j in range(n//2+1)
    ))


def base_measure_moment(n, shift):
    # The complete specified measure is 3(1+u^2) exp(-(u-shift)^2)/sqrt(pi).
    return exact(3*(gaussian_moment(n, shift)+gaussian_moment(n+2, shift)))


def measure_moment(n, shift, k=1):
    # Full unscaled k-fold convolution: Fubini and the binomial theorem.
    if k == 1:
        return base_measure_moment(n, shift)
    return exact(sum(sp.binomial(n,j)*base_measure_moment(j,shift)
                     *measure_moment(n-j,shift,k-1) for j in range(n+1)))


def integral(polynomial, shift, k):
    p = sp.Poly(sp.expand(polynomial), u)
    return exact(sum(coefficient*measure_moment(power[0], shift, k)
                     for power, coefficient in p.terms()))


def inner(left, right, k, shift):
    l = left.subs(S, sp.Rational(k, 2)+I*u)
    r = right.subs(S, sp.Rational(k, 2)+I*u)
    return integral(sp.conjugate(l)*r, shift, k)


def encode(value):
    if isinstance(value, sp.MatrixBase):
        return [[str(exact(value[row, column])) for column in range(value.cols)]
                for row in range(value.rows)]
    return str(exact(value))


def fixture(label, k, chi, shift, degrees, require_imaginary_cross=False,
            require_singular_omission=False):
    q = int(sp.degree(chi, S))
    top = max(degrees)+1
    check_equal(label+"/original_convolution_mass", measure_moment(0,shift,k),
                base_measure_moment(0,shift)**k)
    p, omega = [], []
    for j in range(top+1):
        candidate = S**j
        for previous, norm in zip(p, omega):
            candidate -= previous*inner(previous, candidate, k, shift)/norm
        candidate = sp.Poly(sp.expand(candidate), S).as_expr()
        norm = inner(candidate, candidate, k, shift)
        check_equal(f"{label}/p{j}/monic", sp.Poly(candidate, S).LC(), 1)
        check_true(f"{label}/p{j}/positive_norm", norm > 0)
        for ell, previous in enumerate(p):
            check_equal(f"{label}/p{j}/orthogonal_p{ell}", inner(previous, candidate, k, shift), 0)
        # Dagger fixes the vertical line pointwise before conjugating values.
        dagger = sp.conjugate(candidate.subs(S, k-sp.conjugate(S)))
        check_equal(f"{label}/p{j}/dagger", dagger, (-1)**j*candidate)
        p.append(candidate)
        omega.append(norm)
    dagger_chi = sp.conjugate(chi.subs(S, k-sp.conjugate(S)))
    check_equal(f"{label}/chi/reflection", dagger_chi, (-1)**q*chi)
    b = []
    for j, polynomial in enumerate(p):
        remainder = sp.rem(polynomial, chi, S)
        vector = sp.Matrix([sp.expand(remainder).coeff(S, ell) for ell in range(q)])
        check_equal(f"{label}/b{j}/remainder", sum(vector[ell]*S**ell for ell in range(q)), remainder)
        b.append(vector)
    A = sp.zeros(q)
    for j in range(q):
        reduced = sp.rem(S**(j+1), chi, S)
        for ell in range(q):
            A[ell, j] = sp.expand(reduced).coeff(S, ell)
    K = [sp.zeros(q)]
    for j in range(len(p)):
        K.append((K[-1]+b[j]*b[j].conjugate().T/omega[j]).applyfunc(exact))
    records = []
    nonzero_imaginary_count = 0
    singular_omission_count = 0
    for N in degrees:
        km, kn, kp = K[N], K[N+1], K[N+2]
        gn = kn.inv().applyfunc(exact)
        omitted = (km+b[N+1]*b[N+1].conjugate().T/omega[N+1]).applyfunc(exact)
        dm, dn, dp, dt = [exact(matrix.det()) for matrix in (km,kn,kp,omitted)]
        a = exact((b[N].conjugate().T*gn*b[N])[0])
        d = exact((b[N+1].conjugate().T*gn*b[N+1])[0])
        c = exact((b[N].conjugate().T*gn*b[N+1])[0])
        c2 = exact(c*sp.conjugate(c))
        eps2 = exact((a*d-c2)/omega[N]**2)
        pref = f"{label}/N{N}"
        check_true(pref+"/K_positive_determinant", dn > 0)
        check_equal(pref+"/CV3_first", 1-dm/dn, a/omega[N])
        check_equal(pref+"/CV3_second", dp/dn-1, d/omega[N+1])
        check_equal(pref+"/CV3_signed_two_direction", dt/dn,
                    (1-a/omega[N])*(1+d/omega[N+1])+c2/(omega[N]*omega[N+1]))
        check_equal(pref+"/CV4", eps2, omega[N+1]/omega[N]*(dp+dm-dn-dt)/dn)
        check_equal(pref+"/CV5", eps2, omega[N+1]/omega[N]*
                    ((1-dm/dn)*(dp/dn-1)-c2/(omega[N]*omega[N+1])))
        check_true(pref+"/Gram_nonnegative", eps2 >= 0)
        check_equal(pref+"/cross_pure_imaginary", sp.re(c), 0)
        if c != 0:
            nonzero_imaginary_count += 1
            check_true(pref+"/negative_control_wrong_cross_sign_is_rejected",
                       exact(dt/dn-((1-a/omega[N])*(1+d/omega[N+1])
                                    -c2/(omega[N]*omega[N+1]))) != 0)
        if dt == 0:
            singular_omission_count += 1
        if N == q-1:
            check_equal(pref+"/boundary_previous_rank", km.rank(), q-1)
            check_equal(pref+"/boundary_previous_det", dm, 0)
            check_equal(pref+"/boundary_a_equals_omega", a, omega[N])
        B = sp.Matrix.hstack(*b[:N+1])
        H = sp.diag(*omega[:N+1])
        adjoint = H.inv()*B.conjugate().T
        R = (adjoint*gn).applyfunc(exact)
        check_equal(pref+"/CV6_adjoint_type", H*adjoint, B.conjugate().T)
        check_equal(pref+"/CV6_TTstar", B*adjoint, kn)
        check_equal(pref+"/canonical_right_inverse", B*R, sp.eye(q))
        check_equal(pref+"/canonical_source_Gram", R.conjugate().T*H*R, gn)
        # Exterior norm is computed independently by its original coordinate
        # minors, including every inherited source norm in each wedge.
        exterior_square_norm = 0
        for indices in itertools.combinations(range(N+1), q):
            minor = exact(R.extract(indices, range(q)).det())
            exterior_square_norm += minor*sp.conjugate(minor)*sp.prod(omega[j] for j in indices)
        check_equal(pref+"/CV6_exterior_volume", exterior_square_norm, 1/dn)
        selected = list(range(N))+[N+1]
        omitted_B = sp.Matrix.hstack(*(b[j] for j in selected))
        omitted_H = sp.diag(*(omega[j] for j in selected))
        check_equal(pref+"/omitted_subspace_Gram", omitted_B*omitted_H.inv()*omitted_B.conjugate().T, omitted)
        Z = (A*kn+kn*A.conjugate().T-k*kn).applyfunc(exact)
        boundary = (b[N+1]*b[N].conjugate().T+b[N]*b[N+1].conjugate().T)/omega[N]
        check_equal(pref+"/inherited_rank_two_identity", Z, boundary)
        check_equal(pref+"/inherited_control_trace_zero", sp.trace(gn*Z), 0)
        check_equal(pref+"/inherited_control_squared_trace", sp.trace((gn*Z)**2), 2*eps2)
        minor_records = []
        positive_minor_sum = 0
        lambda_zeta = 0
        if q >= 2:
            for indices in itertools.combinations(range(N), q-2):
                chosen = indices+(N,N+1)
                determinant = exact(sp.Matrix.hstack(*(b[j] for j in chosen)).det())
                full_source_norm = sp.prod(omega[j] for j in chosen)
                coefficient = exact(sp.conjugate(determinant)/full_source_norm)
                positive_minor_sum += exact(determinant*sp.conjugate(determinant)/full_source_norm)
                lambda_zeta += determinant*coefficient
                minor_records.append({"indices":list(chosen),"determinant":encode(determinant),
                                      "full_source_norm":encode(full_source_norm),
                                      "zeta_coefficient":encode(coefficient)})
        delta = exact(dp+dm-dn-dt)
        check_equal(pref+"/CV10_positive_maximal_minor_sum", positive_minor_sum, delta)
        check_equal(pref+"/CV10a_Lambda_zeta", lambda_zeta, delta)
        explicit_tensor = None
        if q == 2:
            S1,S2,u1,u2 = sp.symbols("S1 S2 u1 u2",real=True)
            tensor = sp.expand(coefficient*(p[N].subs(S,S1)*p[N+1].subs(S,S2)
                                           -p[N+1].subs(S,S1)*p[N].subs(S,S2)))
            check_equal(pref+"/CV10a_unscaled_Alt2_antisymmetry",
                        tensor.xreplace({S1:S2,S2:S1}), -tensor)
            line_tensor = sp.expand(tensor.subs({S1:sp.Rational(k,2)+I*u1,
                                               S2:sp.Rational(k,2)+I*u2}))
            tensor_absolute_square = sp.Poly(sp.expand(sp.conjugate(line_tensor)*line_tensor),u1,u2)
            tensor_norm = exact(sum(value*measure_moment(powers[0],shift,k)*measure_moment(powers[1],shift,k)
                                    for powers,value in tensor_absolute_square.terms()))
            check_equal(pref+"/CV10a_direct_tensor_integral_factorial", tensor_norm, 2*delta)
            explicit_tensor={"monomial_tensor_polynomial":encode(tensor),
                             "vertical_line_tensor_polynomial":encode(line_tensor),
                             "direct_original_product_measure_squared_norm":encode(tensor_norm),
                             "literal_factorial":2}
        if q == 1:
            check_equal(pref+"/one_dimensional_allowance", eps2, 0)
            check_equal(pref+"/one_dimensional_control", Z, sp.zeros(1))
        records.append({"N":N,"D_N_minus_1":encode(dm),"D_N":encode(dn),
                        "D_N_plus_1":encode(dp),"omitted_D_N":encode(dt),
                        "a":encode(a),"d":encode(d),"c":encode(c),
                        "absolute_c_squared":encode(c2),"epsilon_squared":encode(eps2),
                        "signed_determinant_increment":encode(dp+dm-dn-dt),
                        "K_N":encode(kn),"G_N":encode(gn),
                        "canonical_right_inverse":encode(R),
                        "omitted_rank":omitted.rank(),
                        "exterior_squared_norm":encode(exterior_square_norm),
                        "positive_maximal_minor_sum":encode(positive_minor_sum),
                        "maximal_minors":minor_records,
                        "explicit_Alt2_zeta":explicit_tensor})
    if require_imaginary_cross:
        check_true(label+"/required_nonzero_imaginary_cross", nonzero_imaginary_count > 0)
    if require_singular_omission:
        check_true(label+"/required_singular_omitted_direction", singular_omission_count > 0)
    return {"label":label,"k":k,"q":q,"chi":encode(chi),
            "base_measure":"3*(1+u^2)*exp(-(u-shift)^2)/sqrt(pi) du on the entire real line",
            "measure":"The literal unscaled k-fold additive convolution of base_measure",
            "shift":encode(shift),"base_mass":encode(base_measure_moment(0,shift)),
            "mass":encode(measure_moment(0,shift,k)),
            "first_moment":encode(measure_moment(1,shift,k)),
            "moments":[encode(measure_moment(j,shift,k)) for j in range(2*top+1)],
            "monic_polynomials":[encode(poly) for poly in p],
            "omega":[encode(norm) for norm in omega],"remainder_columns":[encode(v) for v in b],
            "multiplication_S":encode(A),"records":records}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    half = sp.Rational(1,2)
    chi4 = ((S-half)**2-sp.Rational(1,9))**2
    result = [
        fixture("k1_reflected_confluent_non_even", 1, chi4, sp.Rational(2,3), [3,4,5],
                require_imaginary_cross=True),
        fixture("k1_reflected_confluent_even_singular_boundary", 1, chi4, sp.Rational(0), [3,4],
                require_singular_omission=True),
        fixture("k2_sum_of_two_simple_reflected_roots", 2,
                (S-1)*((S-1)**2-sp.Rational(4,9)), sp.Rational(2,3), [2,3,4],
                require_imaginary_cross=True),
        fixture("k2_reflection_fixed_one_dimensional", 2, S-1-I/3,
                sp.Rational(2,3), [0,1,2], require_imaginary_cross=True),
        fixture("k1_double_reflection_fixed_root_literal_tensor", 1, (S-half)**2,
                sp.Rational(2,3), [1,2,3], require_imaginary_cross=True),
    ]
    payload = {"status":"passed", "scope":"Exact positive-measure finite replay of CV.1-CV.6, CV.10-CV.10a and the inherited rank-two identity. At q=2 the unscaled alternating source is expanded in the original two-variable polynomial basis and its norm is computed by direct product-measure integration. This does not compute the arithmetic Xi measure or prove an RH asymptotic estimate.",
               "check_count":len(checks),"checks":checks,"fixtures":result,
               "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
               "python_version":platform.python_version(),"sympy_version":sp.__version__,
               "optimization_level":sys.flags.optimize}
    args.output.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"status":"passed","checks":len(checks),"output":str(args.output),
                      "nonzero_crosses":[[item["label"], [r["c"] for r in item["records"]]] for item in result]},indent=2))


if __name__ == "__main__":
    main()
