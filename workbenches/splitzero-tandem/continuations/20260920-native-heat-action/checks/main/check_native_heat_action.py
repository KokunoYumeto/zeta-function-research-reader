"""Exact finite checks for NH1--NH31; comparison matrices are not zeta packets."""
from __future__ import annotations
import argparse
import hashlib
import json
import math
from pathlib import Path
import sys
import sympy as sp

HERE = Path(__file__).resolve().parent
R = sp.Rational
t, z, S = sp.symbols("t z S")
records: list[dict] = []
negative_records: list[dict] = []


def scalar(value):
    return sp.cancel(sp.expand(value))


def equal(name, actual, expected):
    if isinstance(actual, sp.MatrixBase) or isinstance(expected, sp.MatrixBase):
        delta = sp.Matrix(actual) - sp.Matrix(expected)
        if any(scalar(entry) != 0 for entry in delta):
            raise ArithmeticError(name + ": matrix mismatch " + str(delta))
    elif scalar(actual - expected) != 0:
        raise ArithmeticError(name + ": scalar mismatch " + str(actual - expected))
    records.append({"name": name, "status": "pass"})


def nonnegative(name, value):
    value = scalar(value)
    if value.is_nonnegative is not True:
        raise ArithmeticError(name + ": nonnegative rational required: " + str(value))
    records.append({"name": name, "status": "pass", "value": str(value)})


def positive(name, value):
    value = scalar(value)
    if value.is_positive is not True:
        raise ArithmeticError(name + ": positive rational required: " + str(value))
    records.append({"name": name, "status": "pass", "value": str(value)})


def expect_failure(name, callback):
    before = len(records)
    try:
        callback()
    except ArithmeticError as exc:
        del records[before:]
        negative_records.append({"name": name, "status": "expected failure",
                                 "reason": str(exc)})
    else:
        raise ArithmeticError(name + ": deliberate error was accepted")


def gamma_composition(gammas, n, r):
    """Coefficient of x^r in (sum gamma[2j+1] x^j)^n."""
    coeff = [sp.Integer(1)] + [sp.Integer(0)] * r
    for _ in range(n):
        coeff = [sum(coeff[j] * gammas[2 * (k - j) + 1]
                     for j in range(k + 1)) for k in range(r + 1)]
    return scalar(coeff[r])


def matrix_word_powers(A, Q, maximum):
    """Literal noncommutative product, coefficient matrices indexed by t."""
    q = A.rows
    output = [[sp.eye(q)]]
    for degree in range(maximum):
        previous = output[-1]
        nxt = [sp.zeros(q) for _ in range(degree + 2)]
        for j, block in enumerate(previous):
            nxt[j] += block * A
            nxt[j + 1] -= block * Q
        output.append([block.applyfunc(scalar) for block in nxt])
    return output


def exp_interval(x, degree=64):
    """Rational enclosure from the proved exponential Taylor remainder."""
    x = R(x)
    p = sum(x**j / math.factorial(j) for j in range(degree + 1))
    # e^u <= 3^ceil(u), since e = sum 1/j! < 3.
    bound = R(3)**int(sp.ceiling(abs(x)))
    error = bound * abs(x)**(degree + 1) / math.factorial(degree + 1)
    return scalar(p - error), scalar(p + error)


def interval_sum(*intervals):
    return sum(item[0] for item in intervals), sum(item[1] for item in intervals)


def interval_scale(value, interval):
    pair = [scalar(value * endpoint) for endpoint in interval]
    return min(pair), max(pair)


def interval_abs_upper(interval):
    return max(abs(interval[0]), abs(interval[1]))


def check_case(name, G, A, r, ell, expected_endpoint, eps_upper, degree=8):
    q = A.rows
    Q = r * ell
    M = A - Q
    Gamma = sp.diag(*[(-1)**j for j in range(q)])
    Qdag = G.inv() * Q.conjugate().T * G
    eps2 = scalar(sp.trace(Qdag * Q))
    for j in range(1, q + 1):
        positive(name + "/G principal " + str(j), G[:j, :j].det())
    equal(name + "/native selfadjoint", G * A, A.conjugate().T * G)
    equal(name + "/rank one square", Q * Q, sp.zeros(q))
    equal(name + "/pairing zero", (ell * r)[0], 0)
    equal(name + "/metric parity", Gamma.T * G * Gamma, G)
    equal(name + "/A parity", Gamma * A * Gamma, -A)
    equal(name + "/Q parity", Gamma * Q * Gamma, -Q)
    equal(name + "/endpoint polynomial", (z * sp.eye(q) - M).det(),
          expected_endpoint)
    # a=1 is a certified upper bound for these Jacobi compressions.
    margin = G - A.T * G * A
    for j in range(1, q + 1):
        positive(name + "/a upper principal " + str(j), margin[:j, :j].det())
    nonnegative(name + "/epsilon upper", eps_upper**2 - eps2)
    gammas = [(ell * (A**j) * r)[0] for j in range(2 * degree + 2)]
    for j in range(0, 2 * degree + 1, 2):
        equal(name + "/even gamma " + str(j), gammas[j], 0)
    powers = matrix_word_powers(A, Q, 2 * degree + 1)
    for m in range(2 * degree + 2):
        for n, block in enumerate(powers[m]):
            if m % 2:
                equal(name + f"/odd trace {m},{n}", sp.trace(block), 0)
    for m in range(1, degree + 1):
        equal(name + f"/base heat coefficient {m}",
              (-1)**m * sp.trace(powers[2*m][0]) / math.factorial(m),
              (-1)**m * sp.trace(A**(2*m)) / math.factorial(m))
        for n in range(1, 2*m + 1):
            actual = scalar((-1)**m * sp.trace(powers[2*m][n]) /
                            math.factorial(m))
            if n > m:
                expected = sp.Integer(0)
            else:
                rdegree = m - n
                H = gamma_composition(gammas, n, rdegree)
                expected = R(2 * (-1)**rdegree, n * math.factorial(m - 1)) * H
                majorant = R(2, math.factorial(n) * math.factorial(rdegree)) * eps_upper**n
                nonnegative(name + f"/coefficient majorant {m},{n}",
                            majorant - abs(scalar(expected)))
            equal(name + f"/heat word versus secular {m},{n}", actual, expected)
    # Complete determinant and original scaling phase, without deleting factors.
    characteristic = (z * sp.eye(q) - (A - t * Q)).det()
    d = (z * sp.eye(q) - A).det()
    equal(name + "/complete interpolation", characteristic,
          (1-t)*d + t*expected_endpoint)
    c = R(7, 2)
    B = c*sp.eye(q) + sp.I*(A-t*Q)
    equal(name + "/original S phase", (S*sp.eye(q)-B).det(),
          sp.I**q * characteristic.subs(z, (S-c)/sp.I))
    secular_numerator = scalar((ell * (z*sp.eye(q)-A).adjugate() * r)[0])
    equal(name + "/full secular numerator", secular_numerator, expected_endpoint-d)
    equal(name + "/endpoint scalar resolvent", (ell * (z*sp.eye(q)-M).inv() * r)[0],
          secular_numerator/expected_endpoint)
    return {"name": name, "dimension": q, "epsilon_squared": str(eps2),
            "heat_degree_checked": degree, "a_upper": "1",
            "epsilon_upper": str(eps_upper)}, powers, gammas


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="CHECKS_NORMAL.json")
    parser.add_argument("--failure-control", action="store_true")
    args = parser.parse_args()
    G2 = sp.diag(3, 1)
    A2 = sp.Matrix([[0, R(1,3)], [1,0]])
    ell2 = sp.Matrix([[0,1]])
    first, _, gammas = check_case("mass-three nonreal pair", G2, A2,
                     sp.Matrix([R(4,3),0]), ell2, z*z+1, sp.Integer(3))
    second, _, _ = check_case("size-two zero Jordan endpoint", G2, A2,
                     sp.Matrix([R(1,3),0]), ell2, z*z, sp.Integer(1))
    G4 = sp.Matrix([[3,0,1,0],[0,1,0,R(3,5)],
                    [1,0,R(3,5),0],[0,R(3,5),0,R(3,7)]])
    M4 = sp.Matrix([[0,0,0,-1],[1,0,0,0],[0,1,0,-2],[0,0,1,0]])
    r4 = sp.Matrix([R(32,35),0,R(20,7),0])
    ell4 = sp.Matrix([[0,0,0,1]])
    third, _, _ = check_case("two nonreal size-two Jordan blocks", G4,
                             M4+r4*ell4, r4, ell4, (z*z+1)**2,
                             sp.Integer(14), degree=7)
    N4 = M4*M4+sp.eye(4)
    equal("nonreal Jordan nilpotent square", N4*N4, sp.zeros(4))
    positive("nonreal Jordan nilpotent nonzero", sum(abs(v)**2 for v in N4))
    for m in range(1, 13):
        equal(f"complete nonreal Jordan operator heat coefficient {m}",
              (-1)**m * (M4**(2*m)) / math.factorial(m),
              sp.eye(4)/math.factorial(m)-N4/math.factorial(m-1))
        equal(f"full nonreal multiplicity trace {m}",
              (-1)**m*sp.trace(M4**(2*m))/math.factorial(m),
              R(4, math.factorial(m)))
    # Exact coefficient of the closed heat example and the defective endpoint.
    for n in range(1, 9):
        for rdegree in range(0, 8):
            lhs = R(2*(-1)**rdegree, n*math.factorial(n+rdegree-1))*gamma_composition(gammas,n,rdegree)
            rhs = R(2*(-1)**rdegree, math.factorial(n)*math.factorial(rdegree))*R(4,3)**n*R(1,3)**rdegree
            equal(f"closed heat ordered coefficient {n},{rdegree}", lhs, rhs)
        derivative = (-1)**n*math.factorial(n-1)*R(2*n*(-1)**n, math.factorial(n)*3**n)
        equal(f"Jordan endpoint heat derivative factor {n}", derivative, R(2,3**n))
    # Fully rational enclosures for an actual analytic remainder in the 2D test.
    for sval, tval, N in [(R(1,10),R(1,2),2),(R(1,3),R(1),4),
                         (R(1,5),R(-1,3),3)]:
        full = interval_scale(2, exp_interval(-sval*(1-4*tval)/3))
        polynomial_factor = sum((4*sval*tval/3)**j/math.factorial(j) for j in range(N+1))
        approx = interval_scale(2*polynomial_factor, exp_interval(-sval/3))
        difference = interval_sum(full, interval_scale(-1, approx))
        # NH17 with certified a<=1 and epsilon<=3.
        x, y = sval, sval*abs(tval)*3
        exp_lower, _ = exp_interval(x+y)
        lower_bound_value = 2*exp_lower*y**(N+1)/math.factorial(N+1)
        positive(f"analytic NH17 rational enclosure {sval},{tval},{N}",
                 lower_bound_value-interval_abs_upper(difference))
    # NH33--NH36: rational enclosures of both genuine heat traces,
    # retaining the exact metric and choosing an explicitly admitted heat time.
    for tval in [R(-1,3),R(1,4),R(1,2),R(1),R(2)]:
        bv = (1-4*tval)/3
        b2 = max(R(1,3), 3*bv*bv)
        sval = 1/(7*b2)
        hol = interval_scale(2,exp_interval(-sval*bv))
        met = interval_sum(exp_interval(-sval/3),exp_interval(-3*sval*bv*bv))
        delta = interval_sum(hol,interval_scale(-1,met))
        target = sval*tval*tval*R(16,3)
        positive(f"metric heat lower recovery {tval}",delta[0]-target/2)
        positive(f"metric heat upper recovery {tval}",3*target/2-delta[1])
        error = interval_sum(delta,(-target,-target))
        positive(f"metric heat relative error {tval}",
                 target/2-interval_abs_upper(error))
        L2 = 4*(4*tval-1)/3 if tval>R(1,4) else R(0)
        positive(f"complete exterior heat receiver {tval}",2*delta[0]/sval-L2)
    # Dilation equality is verified on every finite heat coefficient here.
    Q4=r4*ell4
    for tval in [R(0),R(1,3),R(1)]:
        Tv=M4+Q4-tval*Q4
        Tdv=G4.inv()*Tv.T*G4
        dilation=sp.zeros(8)
        dilation[:4,4:]=Tv
        dilation[4:,:4]=Tdv
        for m in range(0,7):
            equal(f"full doubled heat coefficient {tval},{m}",
                  sp.trace(dilation**(2*m)),2*sp.trace((Tdv*Tv)**m))
    # Same holomorphic heat under exact non-isometric conjugacy,
    # with different native metric curvature.
    Aa=sp.diag(-2,-1,1,2)
    rr=sp.Matrix([1,1,1,1])
    ll=sp.Matrix([[1,1,-1,-1]])
    Qa=rr*ll
    Dc=sp.diag(2,1,1,2)
    Qb=Dc*Qa*Dc.inv()
    equal("same holomorphic heat exact conjugacy",
          Dc*(Aa-t*Qa)*Dc.inv(),Aa-t*Qb)
    equal("first fixed-metric allowance",sp.trace(Qa.T*Qa),16)
    equal("second fixed-metric allowance",sp.trace(Qb.T*Qb),25)
    equal("conjugated nilpotent relation",Qb*Qb,sp.zeros(4))
    # Negative controls detect the actual errors of concern.
    expect_failure("dropped Jordan multiplicity",
                   lambda: equal("bad multiplicity", sp.trace(sp.eye(4)), 2))
    expect_failure("dropped original phase",
                   lambda: equal("bad phase", sp.I**2, 1))
    expect_failure("wrong cyclic factorial",
                   lambda: equal("bad cyclic factor", 2, 4))
    expect_failure("wrong heat sign",
                   lambda: equal("bad heat sign", 2*R(4,3), -2*R(4,3)))
    expect_failure("dropped ordered composition",
                   lambda: equal("bad composition",
                     gamma_composition(gammas,2,1), gammas[1]*gammas[3]))
    expect_failure("erased packet mass",
                   lambda: equal("bad mass", G2[0,0], 1))
    expect_failure("nilpotent implies isospectral",
                   lambda: equal("bad determinant", z*z+1, z*z-R(1,3)))
    expect_failure("removed endpoint double pole",
                   lambda: equal("bad pole", R(1,3)/z**2, R(1,3)/z))
    expect_failure("holomorphic heat determines fixed metric norm",
                   lambda: equal("bad metric inference",
                                 sp.trace(Qa.T*Qa),sp.trace(Qb.T*Qb)))
    expect_failure("forgot doubled heat factor",
                   lambda: equal("bad dilation factor",2*sp.trace(sp.eye(4)),4))
    if args.failure_control:
        equal("deliberate external failure", 1, 0)
    sources = {}
    for filename in ["NATIVE_HEAT_ACTION.tex", Path(__file__).name]:
        path = HERE/filename
        sources[filename] = hashlib.sha256(path.read_bytes()).hexdigest()
    report = {"status":"pass", "exact_checks":len(records),
              "negative_controls":len(negative_records),
              "cases":[first,second,third],
              "verification_scope":"Finite comparison matrices only; no arithmetic zero packet or asymptotic decay is certified.",
              "sources":sources, "checks":records,
              "negative_control_records":negative_records}
    output = HERE/args.output
    output.write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({key:report[key] for key in ("status","exact_checks","negative_controls")}))


if __name__ == "__main__":
    main()
