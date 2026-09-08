"""Independent finite checks of the exact trace coefficient and support maps.

The arbitrary-n theorems are proved in tex/permanent_trace_obstructions.tex.
This checker uses integer monomial dictionaries, explicit coefficient matrices,
finite-field elimination, and permutation enumeration. No symbolic determinant
or theorem-statement mirroring is used as a substitute for those proofs.
"""
from pathlib import Path
from itertools import product, permutations, combinations
from collections import defaultdict
from math import comb, factorial
import json

ROOT = Path(__file__).resolve().parents[1]
checks = []


def require(name, condition, **data):
    if not condition:
        raise AssertionError(name)
    checks.append(dict(name=name, passed=True, **data))


def rank_mod(matrix, prime):
    a = [[x % prime for x in row] for row in matrix]
    height = len(a)
    width = len(a[0]) if a else 0
    r = 0
    for col in range(width):
        pivot = next((i for i in range(r, height) if a[i][col]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        factor = pow(a[r][col], -1, prime)
        a[r] = [(x * factor) % prime for x in a[r]]
        for i in range(r + 1, height):
            factor = a[i][col]
            if factor:
                a[i] = [(x - factor * y) % prime for x, y in zip(a[i], a[r])]
        r += 1
        if r == height:
            break
    return r


for n in range(1, 6):
    perms = list(permutations(range(n)))
    for cut in range(n + 1):
        heads = list(product(range(n), repeat=cut))
        tails = list(product(range(n), repeat=n-cut))
        head_index = {word: i for i, word in enumerate(heads)}
        tail_index = {word: i for i, word in enumerate(tails)}
        matrix = [[0] * len(tails) for _ in heads]
        for perm in perms:
            matrix[head_index[perm[:cut]]][tail_index[perm[cut:]]] += 1
        subsets = [frozenset(s) for s in combinations(range(n), cut)]
        for a, head in enumerate(heads):
            for b, tail in enumerate(tails):
                factor = int(len(set(head)) == cut and
                             len(set(tail)) == n-cut and
                             set(head).isdisjoint(tail))
                if matrix[a][b] != factor:
                    raise AssertionError((n, cut, head, tail))
        require('integral coefficient factorization', True, n=n, cut=cut)
        minor = [[matrix[head_index[tuple(sorted(s))]][
                    tail_index[tuple(sorted(set(range(n))-t))]]
                  for t in subsets] for s in subsets]
        require('literal identity minor', minor == [
            [int(i == j) for j in range(len(subsets))]
            for i in range(len(subsets))], n=n, cut=cut)
        for prime in (2, 3, 7, 101):
            require('full coefficient rank over finite field',
                    rank_mod(matrix, prime) == comb(n, cut),
                    n=n, cut=cut, prime=prime)


def add(a, b):
    ans = defaultdict(int, a)
    for mon, value in b.items():
        ans[mon] += value
    return {mon: value for mon, value in ans.items() if value}


def mul(a, b):
    ans = defaultdict(int)
    for mon, value in a.items():
        for other, coeff in b.items():
            ans[tuple(sorted(mon+other))] += value*coeff
    return dict(ans)


for n in range(1, 7):
    # Integer formal path products, not sampled evaluations.
    states = {frozenset(): {(): 1}}
    widths = [1]
    edge_count = 0
    for i in range(n):
        next_states = {}
        for used, polynomial in states.items():
            for j in range(n):
                if j in used:
                    continue
                dst = used | {j}
                edge_count += 1
                term = mul(polynomial, {((i, j),): 1})
                next_states[dst] = add(next_states.get(dst, {}), term)
        states = next_states
        widths.append(len(states))
    expected = {tuple(enumerate(p)): 1 for p in permutations(range(n))}
    require('subset branching program exact polynomial',
            states[frozenset(range(n))] == expected, n=n)
    require('subset branching program widths and edges',
            widths == [comb(n, i) for i in range(n+1)] and
            sum(widths) == 2**n and edge_count == n*2**(n-1), n=n)


# Test the stronger support assertion against every fixed context matching
# and every candidate head monomial, including repeats, in small dimensions.
for n in range(1, 5):
    full = set(tuple(enumerate(p)) for p in permutations(range(n)))
    checks_count = 0
    for d in range(n+1):
        for rows in combinations(range(n), d):
            for cols in combinations(range(n), d):
                for image in permutations(cols):
                    context = tuple(zip(rows, image))
                    missing_rows = sorted(set(range(n))-set(rows))
                    missing_cols = set(range(n))-set(cols)
                    for candidate in product(range(n), repeat=n-d):
                        tail = tuple(zip(missing_rows, candidate))
                        belongs = tuple(sorted(context+tail)) in full
                        exact_profile = (len(set(candidate)) == n-d and
                                         set(candidate) == missing_cols)
                        if belongs != exact_profile:
                            raise AssertionError((context, tail))
                        checks_count += 1
    require('context support profile including repeated columns', True,
            n=n, cases=checks_count)


# Explicit monotone DAG, with sharing of all subproblems. Parse trees are
# enumerated independently from circuit polynomial evaluation.
for n in range(4, 7):
    nodes = []
    memo = {}

    def leaf_variable(i, j):
        key = ('var', i, j)
        if key not in memo:
            memo[key] = len(nodes)
            nodes.append(('var', (i, j), 1))
        return memo[key]

    def gate(op, left, right, degree):
        nodes.append((op, (left, right), degree))
        return len(nodes)-1

    def suffix(i, available):
        key = (i, tuple(available))
        if key in memo:
            return memo[key]
        if i == n-1:
            result = leaf_variable(i, available[0])
        else:
            terms = [gate('mul', leaf_variable(i, j),
                          suffix(i+1, tuple(a for a in available if a != j)), n-i)
                     for j in available]
            result = terms[0]
            for term in terms[1:]:
                result = gate('add', result, term, n-i)
        memo[key] = result
        return result

    output = suffix(0, tuple(range(n)))
    polys = []
    trees = []
    for idx, (op, args, degree) in enumerate(nodes):
        if op == 'var':
            polys.append({(args,): 1})
            trees.append([((args,), (idx,))])
        elif op == 'add':
            left, right = args
            polys.append(add(polys[left], polys[right]))
            trees.append([(mon, (idx, tree)) for child in (left, right)
                          for mon, tree in trees[child]])
        else:
            left, right = args
            polys.append(mul(polys[left], polys[right]))
            trees.append([(tuple(sorted(a+b)), (idx, ta, tb))
                          for a, ta in trees[left] for b, tb in trees[right]])
        # Validate constant profiles of actual shared nodes.
        profiles = {(frozenset(i for i, j in mon),
                     frozenset(j for i, j in mon)) for mon in polys[-1]}
        require('shared monotone gate unique row-column profile',
                len(profiles) == 1 and all(len(mon) == degree for mon in polys[-1]),
                n=n, gate=idx)
    expected = {tuple(enumerate(p)): 1 for p in permutations(range(n))}
    require('monotone DAG full output polynomial', polys[output] == expected, n=n)
    assigned = defaultdict(set)
    for monomial, tree in trees[output]:
        cursor = tree
        while 3*nodes[cursor[0]][2] > 2*n:
            idx = cursor[0]
            if nodes[idx][0] == 'add':
                cursor = cursor[1]
            else:
                cursor = max(cursor[1:], key=lambda t: nodes[t[0]][2])
        idx = cursor[0]
        d = nodes[idx][2]
        if not (3*d > n and 3*d <= 2*n and nodes[idx][0] != 'var'):
            raise AssertionError((n, d, cursor))
        sample = next(iter(polys[idx]))
        rows, cols = set(i for i, j in sample), set(j for i, j in sample)
        if {j for i, j in monomial if i in rows} != cols:
            raise AssertionError((idx, monomial))
        assigned[idx].add(monomial)
    require('balanced cuts cover all permutation monomials',
            len(set.union(*assigned.values())) == factorial(n), n=n)
    require('each cut gate satisfies its exact support capacity',
            all(len(values) <= factorial(nodes[idx][2])*factorial(n-nodes[idx][2])
                for idx, values in assigned.items()), n=n)

for n in range(4, 201):
    low, high = (n+2)//3, (2*n)//3
    require('balanced capacity bound and exponential inequality',
            min(comb(n, d) for d in range(low, high+1)) == comb(n, low)
            and comb(n, low) >= 2**low, n=n)

receipt = dict(all_passed=True, checks=len(checks),
               proof='tex/permanent_trace_obstructions.tex',
               scope='exact row-ordered ABP and nonnegative circuit restrictions',
               unrestricted_lower_bound_claimed=False, records=checks)
(ROOT/'checks/permanent_obstructions.json').write_text(
    json.dumps(receipt, indent=2), encoding='utf-8')
print(json.dumps({key: receipt[key] for key in (
    'all_passed', 'checks', 'scope', 'unrestricted_lower_bound_claimed')}))
