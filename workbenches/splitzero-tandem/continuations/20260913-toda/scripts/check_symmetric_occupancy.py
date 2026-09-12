"""Exact finite supplements for symmetric occupancy formulas, not analytic proofs."""
from fractions import Fraction
from itertools import product, permutations
from math import comb, factorial
from collections import Counter
import argparse
import json


def compositions(k, d):
    if d == 1:
        yield (k,)
    else:
        for n in range(k + 1):
            for tail in compositions(k - n, d - 1):
                yield (n,) + tail


def choose(n, r):
    return comb(n, r) if n >= r >= 0 else 0


def require(ok, label):
    if not ok:
        raise RuntimeError(label)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--deliberate-failure', '--negative-control',
                        dest='negative_control', action='store_true')
    args = parser.parse_args()
    count = 0
    for d in range(1, 7):
        delta = [Fraction((i + 1) * (-1) ** i, i + 2) for i in range(d)]
        for k in range(8):
            ns = list(compositions(k, d))
            nsize = choose(k + d - 1, d - 1)
            b1 = choose(k + d - 1, d)
            b2 = choose(k + d - 1, d + 1)
            offsets = [sum(n[i] * delta[i] for i in range(d)) for n in ns]
            s1, s2 = sum(delta), sum(x*x for x in delta)
            require(len(ns) == nsize, 'dimension')
            require(sum(offsets) == b1*s1, 'first moment')
            expected = b2*s1*s1 + choose(k+d, d+1)*s2
            require(sum(x*x for x in offsets) == expected, 'second moment')
            count += 3
            for i in range(d):
                require(sum(n[i] for n in ns) == b1, 'individual first')
                require(sum(n[i]*(n[i]-1) for n in ns) == 2*b2,
                        'individual factorial second')
                count += 2
                for j in range(i):
                    require(sum(n[i]*n[j] for n in ns) == b2, 'mixed second')
                    count += 1
            if k:
                f1 = f2 = Fraction(0)
                total = 0
                for n, value in zip(ns, offsets):
                    mult = factorial(k)
                    for ni in n:
                        mult //= factorial(ni)
                    total += mult
                    f1 += mult*value
                    f2 += mult*value*value
                require(total == d**k, 'ordered tensor count')
                require(f1 == k*d**(k-1)*s1, 'ordered first')
                right = k*d**(k-1)*s2
                if k >= 2:
                    right += k*(k-1)*d**(k-2)*s1*s1
                require(f2 == right, 'ordered second')
                count += 3

    for multiplicities in [(2, 1), (2, 2), (1, 2, 3), (4,)]:
        root_values = [Fraction(2*i - 3, i+2) for i in range(len(multiplicities))]
        repeated = [root_values[j] for j,m in enumerate(multiplicities) for _ in range(m)]
        for k in range(7):
            grouped = Counter()
            for ell in compositions(k, len(multiplicities)):
                weight = 1
                for nr, mr in zip(ell, multiplicities):
                    weight *= comb(nr+mr-1, mr-1)
                value = sum(nr*rho for nr,rho in zip(ell,root_values))
                grouped[value] += weight
            direct = Counter(sum(ni*rho for ni,rho in zip(n,repeated))
                             for n in compositions(k,len(repeated)))
            require(grouped == direct, 'grouped characteristic multiplicities')
            count += 1

    # Direct action on unscaled orbit sums; no implicit change to monomial basis.
    d, k = 3, 3
    A = [[2,3,5], [7,11,13], [17,19,23]]
    for n in compositions(k,d):
        seed = tuple(i for i,ni in enumerate(n) for _ in range(ni))
        orbit = set(permutations(seed))
        action = Counter()
        for tup in orbit:
            for pos, j in enumerate(tup):
                for i in range(d):
                    out = list(tup)
                    out[pos] = i
                    action[tuple(out)] += A[i][j]
        expected = Counter()
        for i in range(d):
            for j in range(d):
                if n[j] == 0:
                    continue
                out_n = list(n)
                out_n[j] -= 1
                out_n[i] += 1
                if i == j:
                    coefficient = n[i]*A[i][i]
                else:
                    coefficient = (n[i]+1)*A[i][j]
                    if args.negative_control:
                        coefficient = n[j]*A[i][j]
                out_seed = tuple(a for a,na in enumerate(out_n) for _ in range(na))
                for out in set(permutations(out_seed)):
                    expected[out] += coefficient
        require(action == expected, 'unscaled orbit-sum generator coefficients')
        count += 1

    # Original raising convention N e_j=e_{j+1}. Track all orbit coordinates,
    # not just the endpoint and not just a diagonal eigenvalue list.
    for sizes, root_counts in [((1,), (1,)), ((2,), (1,)), ((2,), (4,)),
                               ((3,), (2,)), ((4,), (3,)),
                               ((2,3), (2,1)), ((1,2,3), (1,2,2))]:
        dimension = sum(sizes)
        starts, ends, edges = [], [], []
        shift = 0
        for size in sizes:
            starts.append(shift)
            ends.append(shift+size-1)
            edges.extend((shift+j,shift+j+1) for j in range(size-1))
            shift += size
        initial = [0]*dimension
        final = [0]*dimension
        for nr, start, end in zip(root_counts,starts,ends):
            initial[start] = nr
            final[end] = nr
        maximal_degree = sum(nr*(size-1) for nr,size in zip(root_counts,sizes))
        coefficients = {tuple(initial): 1}
        for _ in range(maximal_degree):
            next_coefficients = Counter()
            for n, coefficient in coefficients.items():
                for j,i in edges:
                    if not n[j]:
                        continue
                    out = list(n)
                    out[j] -= 1
                    out[i] += 1
                    next_coefficients[tuple(out)] += coefficient*(n[i]+1)
            coefficients = next_coefficients
        exact = factorial(maximal_degree)
        for nr,size in zip(root_counts,sizes):
            exact //= factorial(size-1)**nr
        require(coefficients == {tuple(final): exact}, 'maximal raising coefficient')
        next_coefficients = Counter()
        for n, coefficient in coefficients.items():
            for j,i in edges:
                if n[j]:
                    out = list(n)
                    out[j] -= 1
                    out[i] += 1
                    next_coefficients[tuple(out)] += coefficient*(n[i]+1)
        require(not next_coefficients, 'next raising power vanishes')
        count += 2
    print(json.dumps({'status': 'passed', 'checks': count,
                      'scope': 'exact finite combinatorics and orbit actions; no arithmetic estimates certified'}))


if __name__ == '__main__':
    main()
