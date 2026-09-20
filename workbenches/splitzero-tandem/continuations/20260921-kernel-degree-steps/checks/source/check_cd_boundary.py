"""Exact finite checks of the original Gamma CD and compression formulas.

All polynomial norms retain M_sigma=sqrt(2*pi). Nonreal frame fixtures
are algebra checks, not samples of the original OCF period coefficients.
No Python assertion is used, so optimized Python retains every check.
"""

import argparse
from itertools import product
from math import factorial
import json
import sympy as sp

x, t, v, b, theta = sp.symbols("x t v b theta")
I = sp.I
M = sp.sqrt(2 * sp.pi)
c = sp.Rational(3, 2)
polys = [sp.Integer(1), x]
for j in range(1, 10):
    polys.append(sp.expand(x * polys[j] - j * (j - sp.Rational(1, 2)) * polys[j - 1]))
norms = [M * sp.factorial(j) * sp.rf(sp.Rational(1, 2), j) for j in range(len(polys))]
derivs = {(j, a): sp.diff(polys[j], x, a) / sp.factorial(a)
          for j in range(len(polys)) for a in range(8)}
CHECKS = []


def reduce(value):
    return sp.cancel(sp.expand(value))


def check(name, actual, expected):
    diff = actual - expected
    values = list(diff) if isinstance(diff, sp.MatrixBase) else [diff]
    if any(reduce(z) != 0 for z in values):
        raise RuntimeError(f"FAILED: {name}; difference={diff}")
    CHECKS.append(name)


def p(j, a, z):
    if a > j:
        return sp.Integer(0)
    return derivs[j, a].subs(x, z)


def kernel(d, r, s, xx, tt):
    return reduce(sum(p(j, r, xx) * p(j, s, tt) / norms[j] for j in range(d)))


def numerator(d, r, s, xx, tt):
    return p(d, r, xx) * p(d - 1, s, tt) - p(d - 1, r, xx) * p(d, s, tt)


def boundary(d, r, s, xx, tt):
    if d == 0:
        return sp.Integer(0)
    if reduce(xx - tt) == 0:
        return reduce(sum(numerator(d, r + 1 + j, s - j, xx, tt)
                          for j in range(s + 1)) / norms[d - 1])
    return reduce(sum(
        (-1) ** a * sp.binomial(a + bb, a) * numerator(d, r - a, s - bb, xx, tt)
        / (xx - tt) ** (a + bb + 1)
        for a in range(r + 1) for bb in range(s + 1)) / norms[d - 1])


def physical_poly(j):
    return sp.expand(I ** j * polys[j].subs(x, (v - c) / I))


def physical_numerator(d):
    pd, pm = physical_poly(d), physical_poly(d - 1)
    # Conjugate coefficients, not the independent variable b.
    cd = sp.Poly(pd, v)
    cm = sp.Poly(pm, v)
    pdbar = sum(sp.conjugate(cd.nth(j)) * b ** j for j in range(d + 1))
    pmbar = sum(sp.conjugate(cm.nth(j)) * b ** j for j in range(d))
    return sp.expand(pd * pmbar + pm * pdbar)


def physical_boundary(d, r, s, vv, bb):
    if d == 0:
        return sp.Integer(0)
    G = physical_numerator(d)
    def gj(a, j):
        return sp.diff(G, v, a, b, j).subs({v: vv, b: bb}) / (factorial(a) * factorial(j))
    if reduce(vv + bb - 2*c) == 0:
        return reduce(sum((-1) ** j * gj(r + 1 + j, s - j) for j in range(s + 1))
                      / norms[d - 1])
    return reduce(sum(
        (-1) ** (a + j) * sp.binomial(a + j, a) * gj(r - a, s - j)
        / (vv + bb - 2*c) ** (a + j + 1)
        for a in range(r + 1) for j in range(s + 1)) / norms[d - 1])


def vectors(blocks, j):
    return sp.Matrix([p(j, a, z) for z, count in blocks for a in range(count)])


def multiplication(blocks):
    size = sum(count for _, count in blocks)
    J = sp.zeros(size)
    offset = 0
    for z, count in blocks:
        for a in range(count):
            J[offset + a, offset + a] = z
            if a:
                J[offset + a, offset + a - 1] = 1
        offset += count
    return J


def covariance(blocks, d):
    size = sum(count for _, count in blocks)
    C = sp.zeros(size)
    for j in range(d):
        f = vectors(blocks, j)
        C += f * f.conjugate().T / norms[j]
    return C.applyfunc(reduce)


def compression(d=3):
    blocks = ((1 + I, 1), (1 - I, 1), (2, 1))
    Z = sp.Matrix([[-I, -2], [1, 0], [0, 1]])
    pi = sp.Matrix([[1, I, 2]])
    V, U = Z.conjugate(), pi.T
    Y = multiplication(blocks)
    C = covariance(blocks, d)
    W, Mu = V.conjugate().T * V, U.conjugate().T * U
    P = V * W.inv() * V.conjugate().T
    Q = sp.eye(3) - P
    A = V.conjugate().T * C * V
    H = (V.conjugate().T * Y * V) * W.inv()
    fd, fm = vectors(blocks, d), vectors(blocks, d - 1)
    gd, gm = V.conjugate().T * fd, V.conjugate().T * fm
    bdry = (gd * gm.conjugate().T - gm * gd.conjugate().T) / norms[d - 1]
    L, G = Q * Y.conjugate().T * V, Q * C * V
    correction = L.conjugate().T * G - G.conjugate().T * L
    return locals()


def negative_control(name):
    if name == "cd_sign":
        check("wrong CD denominator sign", kernel(2, 0, 0, 1+I, 2-I),
              -boundary(2, 0, 0, 1+I, 2-I))
    elif name == "collision_sign":
        tau = 1+I
        wrong = (p(2, 1, tau)*p(1, 0, tau) + p(1, 1, tau)*p(2, 0, tau)) / norms[1]
        check("wrong collision Wronskian sign", kernel(2, 0, 0, tau, tau), wrong)
    elif name == "mass":
        check("incorrect handoff mass", kernel(1, 0, 0, 0, 0), 1/(sp.sqrt(2)*sp.pi))
    elif name in ("omit_correction", "wrong_covariant_operator", "drop_conjugation"):
        data = compression()
        A, H, bdry = data["A"], data["H"], data["bdry"]
        if name == "omit_correction":
            check("missing complementary coupling", H*A-A*H.conjugate().T, bdry)
        elif name == "wrong_covariant_operator":
            wrong = data["W"].inv() * (data["V"].conjugate().T * data["Y"] * data["V"])
            check("wrong covariant operator placement", wrong*A-A*wrong.conjugate().T,
                  bdry-data["correction"])
        else:
            Z, C = data["Z"], data["C"]
            check("wrong coefficient-frame conjugation", A, Z.conjugate().T * C * Z)
    raise RuntimeError("Negative control unexpectedly did not fail")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--negative-control", choices=("cd_sign", "collision_sign", "mass",
                        "omit_correction", "wrong_covariant_operator", "drop_conjugation"))
    args = parser.parse_args()
    if args.negative_control:
        negative_control(args.negative_control)
    check("source mass", norms[0], sp.sqrt(2*sp.pi))
    for j in range(1, 10):
        check(f"retained norm ratio {j}", norms[j]/norms[j-1], j*(j-sp.Rational(1, 2)))
    for d in range(1, 9):
        check(f"polynomial telescoping identity d={d}",
              (x-t)*kernel(d, 0, 0, x, t), numerator(d, 0, 0, x, t)/norms[d-1])
    for d in (0, 1, 2, 4, 7):
        for xx, tt in ((1+I, 2-I), (0, sp.Rational(3, 2)), (0, 0), (1+I, 1+I)):
            for r, s in product(range(3), repeat=2):
                check(f"divided jet d={d} r={r} s={s} at {xx},{tt}",
                      kernel(d, r, s, xx, tt), boundary(d, r, s, xx, tt))
                if reduce(xx-tt) == 0 and d:
                    alternative = -sum(numerator(d, r-j, s+1+j, xx, tt)
                                       for j in range(r+1))/norms[d-1]
                    check(f"second collision expansion d={d} r={r} s={s} at {xx}",
                          kernel(d, r, s, xx, tt), alternative)
    for d in (1, 3, 5):
        for xx, tt in ((1+I, 2-I), (1+I, 1+I)):
            vv, bb = c+I*xx, c-I*tt
            for r, s in product(range(3), repeat=2):
                check(f"physical divided jets d={d} r={r} s={s} at {xx},{tt}",
                      physical_boundary(d, r, s, vv, bb),
                      I**(-r)*I**s*kernel(d, r, s, xx, tt))
    blocks = ((1+I, 2), (1-I, 2), (sp.Rational(-1, 2), 1))
    J = multiplication(blocks)
    Lambda = sp.diag(*[I**(-a) for _, count in blocks for a in range(count)])
    XS = Lambda*(c*sp.eye(J.rows)+I*J)*Lambda.inv()
    for d in (1, 3, 6):
        C = covariance(blocks, d)
        fd, fm = vectors(blocks, d), vectors(blocks, d-1)
        B = (fd*fm.conjugate().T-fm*fd.conjugate().T)/norms[d-1]
        check(f"full confluent displacement d={d}", J*C-C*J.conjugate().T, B)
        Cs = Lambda*C*Lambda.conjugate().T
        hd, hm = I**d*Lambda*fd, I**(d-1)*Lambda*fm
        check(f"physical confluent displacement d={d}",
              XS*Cs+Cs*XS.conjugate().T-2*c*Cs,
              (hd*hm.conjugate().T+hm*hd.conjugate().T)/norms[d-1])
    for d in (2, 3, 6):
        a = compression(d)
        A, H = a["A"], a["H"]
        check(f"original nonreal bilinear frame d={d}", a["pi"]*a["Z"], sp.zeros(1, 2))
        check(f"original complementary projection d={d}", a["Q"],
              a["U"]*a["Mu"].inv()*a["U"].conjugate().T)
        check(f"compressed correction d={d}", H*A-A*H.conjugate().T, a["bdry"]-a["correction"])
        F = a["V"].conjugate().T*a["Y"]*a["U"]
        T = a["U"].conjugate().T*a["C"]*a["V"]
        check(f"actual complementary frame coupling d={d}", a["correction"],
              F*a["Mu"].inv()*T-T.conjugate().T*a["Mu"].inv()*F.conjugate().T)
        rho_sum = sp.zeros(A.rows)
        for j in range(d):
            fj = vectors(a["blocks"], j)
            gj = a["V"].conjugate().T*fj
            rho = a["V"].conjugate().T*a["Y"]*a["Q"]*fj
            rho_sum += (rho*gj.conjugate().T-gj*rho.conjugate().T)/norms[j]
        check(f"full lower-degree correction sum d={d}", a["correction"], rho_sum)
        scale = sp.Rational(7, 3)
        check(f"source mass scaling of compression d={d}",
              H*(A/scale)-(A/scale)*H.conjugate().T,
              (a["bdry"]-a["correction"])/scale)
    # Moments of the retained Gamma density from its exact moment-generating
    # function M_sigma*(cos theta)^(-1/2), not a probability rescaling.
    series = sp.series(sp.cos(theta)**(-sp.Rational(1, 2)), theta, 0, 12).removeO()
    moments = [M*sp.factorial(j)*sp.expand(series).coeff(theta, j) for j in range(11)]
    Hg = sp.Matrix(6, 6, lambda r, s: moments[r+s])
    coeff = sp.Matrix(6, 6, lambda r, j: sp.Poly(polys[j], x).nth(r))
    check("Gamma norms from exact source moment series", coeff.T*Hg*coeff, sp.diag(*norms[:6]))
    # Evaluate all four kernel cutoff formulas in smaller exact algebra
    # fixtures; the original q=(k+1)^2 shifts are separately checked.
    for q in (2, 3):
        for N in (q-1, q, 2*q-1, 2*q):
            d = N+1
            check(f"four-cutoff boundary q={q} N={N}",
                  kernel(d, 0, 0, 1+I, 1-I), boundary(d, 0, 0, 1+I, 1-I))
    k, delta, height = 9, sp.Rational(1, 3), sp.Integer(3)
    q = (k+1)**2
    roots = {(aa, bb): (2*bb-k)*height-I*(2*aa-k)*delta
             for aa in range(k+1) for bb in range(k+1)}
    collisions = 0
    for pair, up in roots.items():
        hits = [other for other, uq in roots.items() if reduce(up-sp.conjugate(uq)) == 0]
        expected = [(k-pair[0], pair[1])]
        if hits != expected:
            raise RuntimeError("Original quartet collision pairing failed")
        collisions += len(hits)
    check("actual quartet reflected collision count", collisions, q)
    check("original four kernel term counts", sp.Matrix([q, q+1, 2*q, 2*q+1]),
          sp.Matrix([N+1 for N in (q-1, q, 2*q-1, 2*q)]))
    print(json.dumps({"status": "passed", "exact_check_count": len(CHECKS),
                      "mass": "sqrt(2*pi)", "checks": CHECKS,
                      "actual_period_evaluated": False,
                      "asymptotic_claim": False}, indent=2))


if __name__ == "__main__":
    main()
