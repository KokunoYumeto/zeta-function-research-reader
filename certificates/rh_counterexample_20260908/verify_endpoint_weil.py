"""Actual full Weil form on the retained-b four-jet test space.

No zeros are used as inputs. Exact rational moment constraints precede Arb
quadrature. C^2 splines are labelled C^2, not C_c^infinity. See the companion
proof for the exact constraint-preserving smooth approximation.
"""
from __future__ import annotations

import os
for key in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[key] = "1"
from resource_ceiling import install_memory_ceiling
RESOURCE = install_memory_ceiling()

import argparse
import hashlib
import json
import math
import time
from datetime import datetime, timezone
from fractions import Fraction as F
from pathlib import Path

import sympy as sp
import flint
from flint import arb, acb, ctx
import search_weil_translations as arithmetic
import verify_weil_bspline as base

HERE = Path(__file__).resolve().parent
SIGMA = F(2)  # exactly b^2/32 at b=8, not an inferred zero ordinate
STEP = F(1, 4)
N = 17
SHIFTS = [(j-8)*STEP for j in range(N)]
MOMENTS = [F(1), F(0), F(1, 3), F(0), F(3, 10)]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def moment_matrix():
    return sp.Matrix([[sum(sp.Rational(math.comb(k, r))*sp.Rational(MOMENTS[r])
                           * sp.Rational(d)**(k-r) for r in range(k+1))
                       for d in SHIFTS] for k in range(5)])


def exact_basis():
    m = moment_matrix()
    # A unit zeroth-value column, using the five central knots.
    central = list(range(6, 11))
    local = m[:, central].inv()*sp.Matrix([1, 0, 0, 0, 0])
    k = sp.zeros(N, 1)
    for j, c in zip(central, local):
        k[j] = c
    # Fifth finite differences annihilate every polynomial of degree <=4.
    v = sp.zeros(N, N-5)
    for j in range(N-5):
        for r in range(6):
            v[j+r, j] = (-1)**r*math.comb(5, r)
    a = k.row_join(v)
    assert m.rank() == 5 and m[1:, :].rank() == 4
    assert m*k == sp.Matrix([1, 0, 0, 0, 0])
    assert m*v == sp.zeros(5, N-5)
    assert a.rank() == N-4
    # Derive b4 moments directly from its exact truncated-power pieces.
    x = sp.symbols("x")
    for r in range(5):
        value = 0
        for j in range(-2, 2):
            p = sum((-1)**q*math.comb(4, q)*(x+2-q)**3/sp.Integer(6)
                    for q in range(j+3))
            value += sp.integrate(x**r*p, (x, j, j+1))
        assert value == sp.Rational(MOMENTS[r])
    return m, a


def complementary_jets(m):
    inverse = m[:, list(range(6, 11))].inv()
    q = sp.zeros(N, 4)
    for r in range(4):
        for i in range(5):
            q[i+6, r] = inverse[i, r+1]
    assert m*q == sp.zeros(1,4).col_join(sp.eye(4))
    return q


def congruence(g, a):
    cols = [[(i, arithmetic.ball(F(a[i, j]))) for i in range(N) if a[i, j]]
            for j in range(a.cols)]
    return [[sum(c*d*g[i][j] for i, c in col1 for j, d in col2)
             for col2 in cols] for col1 in cols]


def ldl_solve(g, rhs):
    n = len(g)
    lower = [[acb(int(i == j)) for j in range(n)] for i in range(n)]
    pivots = []
    for j in range(n):
        v = g[j][j]-sum(lower[j][k]*lower[j][k].conjugate()*pivots[k]
                        for k in range(j))
        assert v.imag.contains(0)
        if not v.real > 0:
            return {"positive": False, "failed_pivot": str(v.real)}, None
        pivots.append(v.real)
        for i in range(j+1, n):
            lower[i][j] = (g[i][j]-sum(lower[i][k]*lower[j][k].conjugate()
                                      * pivots[k] for k in range(j)))/v.real
    y = []
    for i in range(n):
        y.append(rhs[i]-sum(lower[i][j]*y[j] for j in range(i)))
    z = [y[i]/pivots[i] for i in range(n)]
    answer = [acb(0) for _ in range(n)]
    for i in range(n-1, -1, -1):
        answer[i] = z[i]-sum(lower[j][i].conjugate()*answer[j]
                             for j in range(i+1, n))
    return {"positive": True, "pivots": [str(v) for v in pivots]}, answer


def direct_scalar(coefficients):
    """Independent combined-correlation integration; does not sum Gram entries.

    coefficients are exact Gaussian rationals for global-modulated shifts.
    First sum all correlation polynomials, then integrate with a single
    common support, gamma tail and prime-power list.
    """
    weights = {}
    for i, ci in enumerate(coefficients):
        for j, cj in enumerate(coefficients):
            d = SHIFTS[j]-SHIFTS[i]
            weights[d] = sp.expand(weights.get(d, 0)+sp.conjugate(ci)*cj)
    weights = {d: c for d, c in weights.items() if c != 0}
    def complex_ball(c):
        return acb(arithmetic.ball(F(sp.re(c))), arithmetic.ball(F(sp.im(c))))
    endpoint = F(4)+max(abs(d) for d in weights)
    knots = sorted({F(0), endpoint} | {F(k-4)+d for d in weights for k in range(9)
                                                   if 0 < F(k-4)+d < endpoint})
    cells = []
    for l, r in zip(knots, knots[1:]):
        mid = (l+r)/2
        p = [sum(c*arithmetic.shifted_coeff(-d, mid)[k] for d, c in weights.items())
             for k in range(8)]
        cells.append((l, r, [complex_ball(c) for c in p]))
    c0 = cells[0][2][0]
    assert c0.imag.contains(0)
    a = acb(arb(1)/2, arithmetic.ball(SIGMA))
    integral = acb(0)
    segments = []
    for l, r, p in cells:
        pc = [c.conjugate() for c in p]
        def integrand(x, analytic, l=l, p=p, pc=pc):
            if l == 0:
                v = base.polynomial(x, p[1:])*(a*x).exp()
                v += c0*a*(a*x/2).exp()*base.sinhc(a*x/2)
                vc = base.polynomial(x, pc[1:])*(a.conjugate()*x).exp()
                vc += c0*a.conjugate()*(a.conjugate()*x/2).exp()*base.sinhc(a.conjugate()*x/2)
                return (v+vc)/(2*base.sinhc(x))
            return ((base.polynomial(x,p)*(a*x).exp()
                    +base.polynomial(x,pc)*(a.conjugate()*x).exp())/2-c0)/x.sinh()
        val = acb.integral(integrand, arithmetic.ball(l), arithmetic.ball(r),
                           rel_tol=arb(2)**(-arithmetic.TOL), abs_tol=arb(2)**(-arithmetic.TOL),
                           eval_limit=200000, depth_limit=35)
        assert val.is_finite()
        integral += val
        segments.append(str(val))
    pole = sum(complex_ball(c)*(base.sinhc(a/2)**8*(a*arithmetic.ball(d)).exp()
                  +base.sinhc((-a.conjugate())/2)**8
                    *((-a.conjugate())*arithmetic.ball(d)).exp())
               for d,c in weights.items())
    primes = acb(0)
    powers = base.prime_powers(float(endpoint))
    for n,p,_ in powers:
        x = arb(n).log()
        for l,r,poly in cells:
            if x > arithmetic.ball(l) and x < arithmetic.ball(r):
                z = base.polynomial(x, poly)*(acb(0,arithmetic.ball(SIGMA))*x).exp()
                primes += 2*arb(p).log()/arb(n).sqrt()*z.real
                break
        else:
            raise ArithmeticError("Prime power without a certified cell")
    constant = -(arb.const_euler()+(4*arb.pi()).log())*c0
    tail = c0*(1/(arithmetic.ball(endpoint)/2).tanh()).log()
    total = pole+constant-integral+tail-primes
    assert total.imag.contains(0)
    return total.real, {"value": str(total.real), "pole": str(pole),
        "constant": str(constant), "integral_segments": segments,
        "tail": str(tail), "prime_sum": str(primes), "endpoint": str(endpoint),
        "prime_power_count": len(powers), "coefficients": [str(c) for c in coefficients]}


def run():
    started = time.time()
    ctx.prec = 384
    ctx.threads = 1
    arithmetic.TOL = 240
    m, a = exact_basis()
    entries, records = [], []
    for k in range(N):
        d = k*STEP
        value, record = arithmetic.full_entry(d, -2)
        # v_j=e^{i sigma d_j}g_j, where g_j is the imported code's basis.
        phase = (acb(0, arithmetic.ball(SIGMA*d))).exp()
        entries.append(phase*value)
        record["global_modulation_phase"] = str(phase)
        record["global_entry"] = str(entries[-1])
        records.append(record)
        print("ENDPOINT_WEIL_ENTRY", k, flush=True)
    g = [[entries[j-i] if j >= i else entries[i-j].conjugate()
          for j in range(N)] for i in range(N)]
    h = congruence(g, a)
    full, _ = ldl_solve(h, [acb(0)]*len(h))
    lower_block = [row[1:] for row in h[1:]]
    sub, solution = ldl_solve(lower_block, [row[0] for row in h[1:]])
    schur = h[0][0]-sum(h[0][i+1]*solution[i] for i in range(len(solution))) if solution else None
    if schur is not None:
        assert schur.imag.contains(0)
    # Retain the four singular-derivative channels as well, not only ker A.
    qjets = complementary_jets(m)
    all_basis = a.row_join(qjets)
    assert all_basis.rank() == N
    all_gram = congruence(g, all_basis)
    all_ldl, _ = ldl_solve(all_gram, [acb(0)]*N)
    solved = []
    for j in range(4):
        success, column = ldl_solve(h, [row[a.cols+j] for row in all_gram[:a.cols]])
        assert success["positive"]
        solved.append(column)
    transverse_schur = [[all_gram[a.cols+i][a.cols+j]
                          -sum(all_gram[a.cols+i][k]*solved[j][k] for k in range(a.cols))
                         for j in range(4)] for i in range(4)]
    transverse_ldl, _ = ldl_solve(transverse_schur, [acb(0)]*4)
    cross_nonzero = any(not h[0][i].contains(0) for i in range(1,len(h)))
    probes = [sp.eye(a.cols)[:, 0], sp.Matrix([1, 1, sp.I]+[0]*(a.cols-3))]
    direct = []
    for q in probes:
        coeff = list(a*q)
        value, record = direct_scalar(coeff)
        qb = [acb(int(sp.re(v)), int(sp.im(v))) for v in q]
        paired = sum(qb[i].conjugate()*h[i][j]*qb[j]
                      for i in range(len(qb)) for j in range(len(qb)))
        assert paired.imag.contains(0) and paired.real.overlaps(value)
        record["gram_value"] = str(paired.real)
        record["overlap"] = True
        direct.append(record)
    dependencies = [Path(__file__), Path(arithmetic.__file__), Path(base.__file__),
                    HERE/"resource_ceiling.py"]
    return {"id":"RH-ENDPOINT-WEIL-20260908-001", "computed_utc":datetime.now(timezone.utc).isoformat(),
        "status":"bounded_full_Weil_calculation_not_RH_resolution", "resource":RESOURCE,
        "software":{"python_flint":flint.__version__,"sympy":sp.__version__},
        "precision_bits":ctx.prec,"tolerance_bits":arithmetic.TOL,"threads":1,
        "source_hashes":{p.name:digest(p) for p in dependencies},
        "parameters":{"b":"8","sigma":str(SIGMA),"step":str(STEP),"n":N,
                      "shifts":[str(v) for v in SHIFTS],"test_support":["-4","4"],
                      "largest_correlation_endpoint":"8"},
        "regularity":"C_c^2 B-splines; exact constraint-preserving C_c^infinity approximation proved separately",
        "moment_matrix":[[str(v) for v in row] for row in m.tolist()],
        "basis_columns":[[str(v) for v in a[:,j]] for j in range(a.cols)],
        "complementary_jet_columns":[[str(v) for v in qjets[:,j]] for j in range(4)],
        "rank_moments_0_to_4":5,"rank_constraints_1_to_4":4,"constrained_dimension":a.cols,
        "zeroth_channel_retained":True,"cross_terms_nonzero_certified":cross_nonzero,
        "entries":records,"matrix":[[str(v) for v in row] for row in h],
        "full_constrained_LDL":full,"five_zero_jet_block_LDL":sub,
        "full_17_channel_LDL":all_ldl,
        "full_17_channel_matrix":[[str(v) for v in row] for row in all_gram],
        "transverse_jet_Schur_matrix":[[str(v) for v in row] for row in transverse_schur],
        "transverse_jet_Schur_LDL":transverse_ldl,
        "unit_zeroth_value_minimum":str(schur.real) if schur is not None else None,
        "unit_zeroth_value_minimum_positive":bool(schur.real>0) if schur is not None else None,
        "unit_zeroth_value_minimizer_coordinates":[str(-v) for v in solution] if solution else None,
        "direct_combined_correlation_checks":direct,"zero_ordinates_used":False,
        "RH_counterexample":False,"proof_assistant_verified":False,
        "trust_boundary":"exact Python/SymPy rationals and FLINT Arb quadrature/ball arithmetic",
        "elapsed_seconds":time.time()-started}


if __name__ == "__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=HERE/"endpoint_weil_results.json")
    args=parser.parse_args()
    receipt=run()
    args.output.write_text(json.dumps(receipt,indent=2)+"\n",encoding="utf-8")
    print("ENDPOINT_WEIL_COMPLETE",receipt["full_constrained_LDL"],
          "SCHUR",receipt["unit_zeroth_value_minimum"],flush=True)
