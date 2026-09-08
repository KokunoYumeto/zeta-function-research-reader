"""Complete arithmetic Weil-form scalar tests, with Arb enclosures.

Fourier convention: hat f(z)=integral f(u) exp(-iuz) du.
f_T(u)=exp(-iTu)b_4(u); b_m is the m-fold convolution of
the mass-one indicator of [-1/2,1/2]. Then
h_T=f_T*f_T^star=exp(-iTx)b_8(x), hat h_T(z)=sinc((z+T)/2)^8.
The integral/pole/prime formula below evaluates the FULL Weil form;
it does not truncate zeros or assume their real parts equal 1/2.

The supplementary zeta-zero comparison is NONRIGOROUS calibration only.
Positive scalar tests do not prove RH or positivity of all finite matrices.
Numerical trust boundary: correct execution of python-flint/FLINT Arb;
this is not a proof-assistant-checked software certificate.
"""

from __future__ import annotations

import hashlib
import json
import math
import platform
import time
from fractions import Fraction
from pathlib import Path

import flint
import mpmath as mp
import numpy as np
import scipy
from flint import acb, arb, ctx
from scipy.integrate import quad


PRECISION_BITS = 192
TOLERANCE_BITS = 120
ctx.prec = PRECISION_BITS
ctx.threads = 1


def coefficients(j):
    """Exact ascending coefficients of b8 on [j,j+1], j=0,1,2,3."""
    return [
        sum(
            (Fraction((-1) ** k * math.comb(8, k) * math.comb(7, r)
                      * (4-k) ** (7-r), math.factorial(7))
             for k in range(j+5)), Fraction(0)
        ) for r in range(8)
    ]


COEFFICIENTS = [coefficients(j) for j in range(4)]
B0_EXACT = COEFFICIENTS[0][0]
B0 = arb(B0_EXACT.numerator) / B0_EXACT.denominator
assert B0_EXACT == Fraction(151, 315)


def polynomial(x, coeff):
    out = x * 0
    for c in reversed(coeff):
        out = out*x + c
    return out


ARB_COEFFICIENTS = [[arb(c.numerator)/c.denominator for c in row]
                    for row in COEFFICIENTS]
FLOAT_COEFFICIENTS = [[float(c) for c in row] for row in COEFFICIENTS]


def b8_float(x):
    x = abs(x)
    if x >= 4:
        return 0.0
    return polynomial(x, FLOAT_COEFFICIENTS[min(int(x),3)])


def b8_arb(x):
    # Every caller is a positive logarithm of an exact integer. Each strict
    # comparison below is certified by interval ordering, not a midpoint.
    for j in range(4):
        if x >= j and x < j+1:
            return polynomial(x, ARB_COEFFICIENTS[j])
    raise ValueError("No unique proved b8 polynomial cell")


def prime_powers(bound=4):
    out = []
    # Deliberately generous integer bound, certified before enumeration.
    limit = math.ceil(math.exp(float(bound)))+1
    assert arb(str(bound)).exp() < limit
    for p in range(2,limit):
        if any(p % d == 0 for d in range(2, math.isqrt(p)+1)):
            continue
        n = p
        exponent = 1
        while n < limit:
            if arb(n).log() < arb(str(bound)):
                out.append((n,p,exponent))
            else:
                assert arb(n).log() >= arb(str(bound))
            n *= p
            exponent += 1
    return sorted(out)


PRIME_POWERS = prime_powers()


def q_float(T):
    z = (0.5+1j*T)/2
    pole = 2*(np.sinh(z)/z)**8
    b0 = float(B0_EXACT)
    def integrand(x):
        if x == 0:
            return b0/2
        return (math.exp(x/2)*b8_float(x)*math.cos(T*x)-b0)/math.sinh(x)
    integral = sum(quad(integrand,j,j+1,epsabs=2e-12,
                        epsrel=2e-12,limit=150)[0] for j in range(4))
    primes = sum(2*math.log(p)/math.sqrt(n)*b8_float(math.log(n))
                 * math.cos(T*math.log(n)) for n,p,_ in PRIME_POWERS)
    return (pole.real-(float(mp.euler)+math.log(4*math.pi))*b0-integral
            +b0*math.log(1/math.tanh(2))-primes)


def sinhc(z):
    # sinc(i*z)=sinh(z)/z, with its entire extension at zero.
    return (acb(0,1)*z).sinc()


def q_arb(T):
    T = arb(str(T))
    a = acb(arb(1)/2,T)
    b = acb(arb(1)/2,-T)
    pole = 2*sinhc(a/2)**8
    segments = []
    evaluations = [0]
    for j in range(4):
        coeff = ARB_COEFFICIENTS[j]
        def integrand(x, analytic, coeff=coeff, j=j):
            # This callback is meromorphic. Thus a ball intersecting a pole
            # of 1/sinhc returns nonfinite; no unverified branch test occurs.
            evaluations[0] += 1
            if j == 0:
                diff_over_x = polynomial(x, coeff[1:])
                expcos = (x/2).exp()*(T*x).cos()
                expcos_minus_one_over_x = (
                    a*(a*x/2).exp()*sinhc(a*x/2)
                    + b*(b*x/2).exp()*sinhc(b*x/2))/2
                return (diff_over_x*expcos+B0*expcos_minus_one_over_x)/sinhc(x)
            return ((x/2).exp()*polynomial(x,coeff)*(T*x).cos()-B0)/x.sinh()
        val = acb.integral(integrand,j,j+1,
                           rel_tol=arb(2)**(-TOLERANCE_BITS),
                           abs_tol=arb(2)**(-TOLERANCE_BITS),
                           eval_limit=100000,depth_limit=30)
        if not val.is_finite():
            raise ArithmeticError("Nonfinite integral enclosure")
        segments.append(val)
    primes = arb(0)
    for n,p,_ in PRIME_POWERS:
        x = arb(n).log()
        primes += 2*arb(p).log()/arb(n).sqrt()*b8_arb(x)*(T*x).cos()
    constant = -(arb.const_euler()+(4*arb.pi()).log())*B0
    tail = B0*(1/arb(2).tanh()).log()
    total = pole.real+constant-sum(v.real for v in segments)+tail-primes
    assert all(v.imag.contains(0) for v in segments)
    return {
        "T": str(T), "value_ball": str(total),
        "lower_ball": str(total.lower()), "upper_ball": str(total.upper()),
        "positive_certified": bool(total > 0),
        "negative_certified": bool(total < 0),
        "pole_ball": str(pole.real), "constant_ball": str(constant),
        "integral_segment_balls": [str(v) for v in segments],
        "tail_ball": str(tail), "prime_sum_ball": str(primes),
        "integrand_evaluations": evaluations[0],
    }


def translated_even_coeff(delta, midpoint):
    """Polynomial C_d(x)=(b8(x-d)+b8(x+d))/2 on an exact cell."""
    return [sum((Fraction((-1)**k*math.comb(8,k)*math.comb(7,r),
                          2*math.factorial(7))*(4+shift-k)**(7-r)
                 for shift in (-delta,delta) for k in range(9)
                 if midpoint+shift+4-k > 0),Fraction(0))
            for r in range(8)]


def translation_gram_entry(delta):
    """Full Weil pairing of b4(u) and b4(u-d), with d rational >=0."""
    endpoint = Fraction(4)+delta
    knots = sorted({Fraction(0),endpoint} |
                   {Fraction(k-4)+s*delta for k in range(9) for s in (-1,1)
                    if 0 < Fraction(k-4)+s*delta < endpoint})
    def ball(q):
        return arb(q.numerator)/q.denominator
    cells = [(left,right,translated_even_coeff(delta,(left+right)/2))
             for left,right in zip(knots,knots[1:])]
    c0_exact = cells[0][2][0]
    c0 = ball(c0_exact)
    integration = acb(0)
    for left,right,exact in cells:
        coeff = [ball(c) for c in exact]
        def integrand(x,analytic,coeff=coeff,left=left):
            if left == 0:
                return (polynomial(x,coeff[1:])*(x/2).exp()
                        +c0*(x/4).exp()*sinhc(x/4)/2)/sinhc(x)
            return ((x/2).exp()*polynomial(x,coeff)-c0)/x.sinh()
        segment = acb.integral(integrand,ball(left),ball(right),
                               rel_tol=arb(2)**(-TOLERANCE_BITS),
                               abs_tol=arb(2)**(-TOLERANCE_BITS),
                               eval_limit=100000,depth_limit=30)
        assert segment.is_finite() and segment.imag.contains(0)
        integration += segment
    prime = arb(0)
    for n,p,_ in prime_powers(float(endpoint)):
        x = arb(n).log()
        for left,right,exact in cells:
            if x > ball(left) and x < ball(right):
                cx = polynomial(x,[ball(c) for c in exact])
                break
        else:
            raise ValueError("Unresolved certified cell for prime")
        prime += 2*arb(p).log()/arb(n).sqrt()*cx
    result = (2*(sinhc(acb(1)/4)**8).real*(ball(delta)/2).cosh()
              -(arb.const_euler()+(4*arb.pi()).log())*c0
              -integration.real+c0*(1/(ball(endpoint)/2).tanh()).log()-prime)
    return result


def matrix_calibration():
    # Exact shifts 0,1/4,1/2,3/4,1, and real symmetric Weil Gram pairing.
    entries = [translation_gram_entry(Fraction(k,4)) for k in range(5)]
    matrix = [[entries[abs(i-j)] for j in range(5)] for i in range(5)]
    pivots = []
    lower = [[arb(int(i==j)) for j in range(5)] for i in range(5)]
    for j in range(5):
        dj = matrix[j][j]-sum(lower[j][k]**2*pivots[k] for k in range(j))
        pivots.append(dj)
        if not dj > 0:
            break
        for i in range(j+1,5):
            lower[i][j] = (matrix[i][j]-sum(lower[i][k]*lower[j][k]*pivots[k]
                                           for k in range(j)))/dj
    positive = len(pivots)==5 and all(d > 0 for d in pivots)
    print("GRAM_LDL",positive,[str(d) for d in pivots],flush=True)
    return {"basis": "f_j(u)=b4(u-j/4), j=0,...,4",
            "basis_support": "supp f_j=[-2+j/4,2+j/4]",
            "correlation": "h_ij(x)=(f_j*f_i^star)(x)=b8(x-(j-i)/4), supp h_ij=[-4+(j-i)/4,4+(j-i)/4]; the explicit formula depends only on h_ij(x)+h_ij(-x), hence C_d=(b8(x-d)+b8(x+d))/2",
            "entry_formula": "G_ij=W(b4(u-i/4),b4(u-j/4)); real symmetric Toeplitz; arithmetic formula applied to C_d(x)=(b8(x-d)+b8(x+d))/2, d=abs(i-j)/4",
            "full_arithmetic_formula": "2*sinhc(1/4)^8*cosh(d/2) -(EulerGamma+log(4pi))*C_d(0) -integral_0^(4+d) (exp(x/2)*C_d(x)-C_d(0))/sinh(x) dx +C_d(0)*log(coth((4+d)/2)) -2*sum_(n<exp(4+d)) Lambda(n)/sqrt(n)*C_d(log(n))",
            "maximum_autocorrelation_support": [-5,5],
            "maximum_prime_power_records_n_p_exponent": prime_powers(5),
            "regularity": "b4 is a compactly supported piecewise cubic C2 function; b8 is piecewise degree 7 and C6; translations preserve this. B8 integer-knot jumps begin only at derivative 7. Integrals split at every shifted knot, so each integrand callback uses one rational-coefficient analytic polynomial piece.",
            "origin_cancellation": "On the first right-hand cell C_d(0)=c0, hence C_d(x)-c0 is divisible by x. With sinhc(x)=sinh(x)/x the integrand equals (((C_d(x)-c0)/x)*exp(x/2) +(c0/2)*exp(x/4)*sinhc(x/4))/sinhc(x), which is analytic near 0 and equals c0/2 at 0 because C_d is even.",
            "toeplitz_entry_balls": [str(v) for v in entries],
            "LDL_pivot_balls": [str(v) for v in pivots],
            "LDL_strict_positive_definite_certified": positive,
            "reason": "Interval LDL recurrences enclose exact rational-operation elimination; positive pivot lower bounds prove positive definiteness of this specific 5x5 matrix",
            "nonclaim": "This matrix is not positivity of the full Weil form"}


def main():
    started = time.time()
    grid = [{"T": i/2, "Q_float": q_float(i/2)} for i in range(201)]
    smallest = sorted(grid,key=lambda row: row["Q_float"])[:8]
    selected = sorted({0.0,14.0,40.0} | {r["T"] for r in smallest[:3]})
    rigorous = []
    for T in selected:
        result = q_arb(T)
        rigorous.append(result)
        print("ARB", T, result["value_ball"],
              "positive", result["positive_certified"], flush=True)
    matrix_result = matrix_calibration()
    # This finite list omits the rest of the zero sum and is NOT a complete
    # evaluation or a proof. It checks sign, scale and Fourier conventions.
    mp.mp.dps = 35
    zeros = [mp.im(mp.zetazero(n)) for n in range(1,51)]
    def zero_partial(T):
        def term(g):
            z = (g+T)/2
            return (mp.sin(z)/z)**8 if z else mp.mpf(1)
        return sum(term(g)+term(-g) for g in zeros)
    calibration = [{"T": T,"first_50_positive_ordinates_partial_sum":
                    str(zero_partial(mp.mpf(str(T)))),
                    "Q_float": q_float(T)} for T in selected]
    matrix_calibration_nonrigorous = [
        {"delta":str(Fraction(k,4)),
         "first_50_positive_ordinates_partial_sum":str(sum(
             2*(mp.sin(g/2)/(g/2))**8*mp.cos(g*k/4) for g in zeros))}
        for k in range(5)]
    source = Path(__file__)
    data = {
        "status": "bounded_scalar_search_complete_not_RH_resolution",
        "script_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "software": {"python": platform.python_version(),
                     "python_flint": flint.__version__,
                     "scipy": scipy.__version__,"mpmath": mp.__version__},
        "threads": 1,"precision_bits": PRECISION_BITS,
        "integration_tolerance_bits": TOLERANCE_BITS,
        "fourier_convention": "hat f(z)=integral f(u) exp(-iuz) du",
        "test_function": "f_T(u)=exp(-iTu)*b4(u)",
        "support_f": [-2,2],"support_autocorrelation": [-4,4],
        "B0_exact": str(B0_EXACT),
        "b8_polynomial_coefficients_ascending_by_cell_j_to_j_plus_1":
            [[str(c) for c in row] for row in COEFFICIENTS],
        "prime_power_records_n_p_exponent": PRIME_POWERS,
        "formula": "2 Re sinhc((1/2+iT)/2)^8 -(EulerGamma+log(4pi))*B0 - integral_0^4 (exp(x/2)*B(x)*cos(Tx)-B0)/sinh(x) dx + B0*log(coth(2)) -2 sum_n Lambda(n)/sqrt(n)*B(log(n))*cos(T*log(n))",
        "formula_scope": "Full arithmetic explicit formula; no zero truncation and no assumption RH",
        "float_grid": grid,"float_smallest_eight": smallest,
        "rigorous_scalar_enclosures": rigorous,
        "rigorous_translation_matrix": matrix_result,
        "calibration_nonrigorous_not_a_certificate": calibration,
        "matrix_zero_calibration_nonrigorous_not_a_certificate": matrix_calibration_nonrigorous,
        "trust_boundary": "Arb interval arithmetic and acb_calc integration; exact rational input polynomials; software implementation not proof-assistant verified",
        "nonclaims": ["These positive scalar and matrix tests provide no RH counterexample",
                      "Positive scalar values are not positivity of all test functions or finite matrices",
                      "The first-50-zero sum has no certified tail and is calibration only"],
        "elapsed_seconds": time.time()-started,
    }
    target = source.with_name("weil_bspline_results.json")
    target.write_text(json.dumps(data,indent=2)+"\n",encoding="utf-8")
    print("RESULT",target.name,"elapsed",data["elapsed_seconds"],flush=True)


if __name__ == "__main__":
    main()
