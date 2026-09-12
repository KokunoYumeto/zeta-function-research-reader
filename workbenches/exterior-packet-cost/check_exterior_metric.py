"""Exact rational regression for EA.13,24,25,27,30,36.

Companion matrices retain multiplicities. Synthetic positive Grams test the
matrix identities; they are not substituted for the actual arithmetic Gram.
Checks remain active under python -O. No third-party packages required.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb, factorial
from pathlib import Path
import argparse
import json
import sys


def need(test, message):
    if not test:
        raise RuntimeError(message)


def transpose(a):
    return [list(x) for x in zip(*a)]


def mul(a, b):
    return [[sum(x*y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def add(a, b, scale=1):
    return [[x+scale*y for x, y in zip(r, s)] for r, s in zip(a, b)]


def scaled(a, c):
    return [[c*x for x in row] for row in a]


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def identity(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def inverse(a):
    n = len(a)
    w = [list(map(F, r))+e for r, e in zip(a, identity(n))]
    for c in range(n):
        p = next(r for r in range(c, n) if w[r][c])
        w[p], w[c] = w[c], w[p]
        w[c] = [x/w[c][c] for x in w[c]]
        for r in range(n):
            if r != c:
                q = w[r][c]
                w[r] = [x-q*y for x, y in zip(w[r], w[c])]
    need([r[:n] for r in w] == identity(n), 'inverse row reduction')
    return [r[n:] for r in w]


def determinant(a):
    n = len(a)
    w = [list(map(F, r)) for r in a]
    answer = F(1)
    for c in range(n):
        p = next((r for r in range(c, n) if w[r][c]), None)
        if p is None:
            return F(0)
        if p != c:
            w[p], w[c] = w[c], w[p]
            answer = -answer
        q = w[c][c]
        answer *= q
        for r in range(c+1, n):
            ratio = w[r][c]/q
            w[r] = [x-ratio*y for x, y in zip(w[r], w[c])]
    return answer


def companion(roots):
    coefficients = [F(1)]
    for rho in roots:
        out = [F(0)]*(len(coefficients)+1)
        for i, c in enumerate(coefficients):
            out[i] -= rho*c
            out[i+1] += c
        coefficients = out
    d = len(roots)
    a = [[F(0)]*d for _ in range(d)]
    for i in range(d-1):
        a[i+1][i] = F(1)
    for i in range(d):
        a[i][-1] = -coefficients[i]
    return a


def exterior(a, k):
    d = len(a)
    basis = list(combinations(range(d), k))
    where = {j: i for i, j in enumerate(basis)}
    out = [[F(0)]*len(basis) for _ in basis]
    for c, j in enumerate(basis):
        for slot, old in enumerate(j):
            for new in range(d):
                seq = j[:slot]+(new,)+j[slot+1:]
                if len(set(seq)) != k:
                    continue
                sign = (-1)**sum(seq[i] > seq[l] for i in range(k) for l in range(i+1, k))
                out[where[tuple(sorted(seq))]][c] += sign*a[new][old]
    return basis, out


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def run():
    rows = []
    fixtures = [(F(1,2),), (F(1,4),F(3,4)), (F(1,2),)*3,
                (F(1,4),F(1,2),F(3,4)),
                (F(1,3),F(2,3),F(1,2),F(1,2))]
    nilpotent_negative_rejected = False
    for roots in fixtures:
        d = len(roots)
        a = companion(roots)
        delta = [r-F(1,2) for r in roots]
        s1, s2 = sum(delta), sum(x*x for x in delta)
        for metric_scale in (F(1), F(3,7)):
            b = [[F(i == j)+metric_scale*(i+1)*(j+1) for j in range(d)] for i in range(d)]
            for k in range(1, d+1):
                basis, ax = exterior(a, k)
                n = len(basis)
                g = [[factorial(k)*determinant([[b[i][j] for j in col] for i in row]) for col in basis] for row in basis]
                gi = inverse(g)
                need(mul(g,gi) == identity(n), 'literal Gram inverse')
                for t in range(1, n+1):
                    need(determinant([r[:t] for r in g[:t]]) > 0, 'positive Gram')
                w = add(add(mul(transpose(ax),g),mul(g,ax)), g, -k)
                gw = mul(gi,w)
                spectral = [sum(roots[j] for j in subset) for subset in basis]
                offsets = [sum(delta[j] for j in subset) for subset in basis]
                eta = trace(mul(mul(mul(gi,transpose(ax)),g),ax))-sum(v*v for v in spectral)
                second = s2 if d == 1 else choose(d-2,k-1)*s2+choose(d-2,k-2)*s1*s1
                need(eta >= 0, 'nonnegative full departure')
                need(trace(gw) == 2*comb(d-1,k-1)*s1, 'EA24 first trace')
                need(trace(mul(gw,gw)) == 4*second+2*eta, 'EA24 squared trace')
                if k == d:
                    need(ax == [[sum(roots)]], 'determinant generator')
                    need(eta == 0 and w == scaled(g,2*s1), 'EA25 determinant cancellation')
                elif len(set(roots)) < d:
                    need(eta > 0, 'proper-degree nilpotent departure retained')
                    if not second:
                        need(trace(mul(gw,gw)) != 4*second, 'negative control: dropping nilpotent departure')
                        nilpotent_negative_rejected = True
                # An exact Hilbert-layer fixture Q=G/3, Y=id, C=-3/2 G^-1W.
                # This tests the form identity and energy bound, not xi moments.
                q = scaled(g,F(1,3))
                c = scaled(gw,F(-3,2))
                need(add(mul(q,c),mul(transpose(c),q)) == scaled(w,-1), 'EA27 layer factorization')
                tau = F(n,3)
                chi = trace(mul(mul(mul(gi,transpose(c)),q),c))
                cost = sum(abs(x) for x in offsets)
                need(cost*cost <= tau*chi, 'EA30 exact source energy bound')
                ratio = determinant(scaled(g,F(2,3)))/determinant(g)
                need(ratio == F(2,3)**n, 'EA36 literal determinant ratio')
                need(1-ratio <= tau, 'EA36 product lower bound')
                rows.append({'roots':list(map(str,roots)), 'k':k,
                             'metric_fixture_scale':str(metric_scale),
                             'departure':str(eta), 'squared_trace':str(trace(mul(gw,gw))),
                             'spectral_cost':str(cost), 'tau':str(tau), 'chi':str(chi)})
    need(nilpotent_negative_rejected, 'nilpotent omission negative control exercised')
    return {'status':'passed','python_optimization':sys.flags.optimize,
            'exact_metric_cases':len(rows),'negative_controls_rejected':['omitted nonsemisimple departure'],
            'scope':'Exact rational companion-matrix and positive-Gram identities; synthetic fixtures, not arithmetic upper bounds',
            'cases':rows}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output')
    args = parser.parse_args()
    result = run()
    if args.output:
        Path(args.output).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k != 'cases'},indent=2))
