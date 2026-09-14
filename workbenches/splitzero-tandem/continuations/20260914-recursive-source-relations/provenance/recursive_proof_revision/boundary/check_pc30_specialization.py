"""Exact finite checks for the fully proved PC30a--g specialization formula."""
from pathlib import Path
from itertools import product
from math import factorial
import hashlib
import json


def rank_mod(columns, p):
    if not columns:
        return 0
    mat = [list(row) for row in zip(*columns)]
    pivot = 0
    for col in range(len(columns)):
        row = next((r for r in range(pivot, len(mat)) if mat[r][col] % p), None)
        if row is None:
            continue
        mat[pivot], mat[row] = mat[row], mat[pivot]
        unit = pow(mat[pivot][col] % p, -1, p)
        mat[pivot] = [(a * unit) % p for a in mat[pivot]]
        for r in range(len(mat)):
            if r != pivot and mat[r][col] % p:
                a = mat[r][col] % p
                mat[r] = [(x - a*y) % p for x, y in zip(mat[r], mat[pivot])]
        pivot += 1
        if pivot == len(mat):
            break
    return pivot


def local_powers(orders, lam, p, count):
    basis = list(product(*(range(m) for m in orders)))
    index = {b: i for i, b in enumerate(basis)}
    # Actual full finite polynomial unit in the test datum, with all coefficients.
    # Constant coefficient 1 is a chosen test value, not a normalization of a source.
    v = [1] * len(basis)  # U=product_i(1+y_i+...+y_i^(m_i-1))
    columns = []
    for _ in range(count):
        columns.append(v)
        out = [(lam*x) % p for x in v]
        for b, j in index.items():
            for i, m in enumerate(orders):
                if b[i] + 1 < m:
                    nxt = list(b)
                    nxt[i] += 1
                    target = index[tuple(nxt)]
                    out[target] = (out[target] + v[j]) % p
        v = out
    return columns


local_cases = []
for k in range(1, 5):
    for orders in product((1, 2, 3), repeat=k):
        if sum(orders) > 10:
            continue
        D = sum(m-1 for m in orders)
        for p in (2, 3, 5, 7):
            if p <= max(orders):
                continue
            cols = local_powers(orders, 0, p, D+2)
            got = rank_mod(cols[:D+1], p)
            expected = min(p, D+1)
            assert got == expected, (orders, p, got, expected)
            assert all(x == 0 for col in cols[expected:] for x in col)
            # Top scalar and the exact loss start at the original factorial.
            scalar = factorial(D)
            for m in orders:
                scalar //= factorial(m-1)
            assert (scalar % p == 0) == (D >= p)
            local_cases.append({'orders': orders, 'p': p, 'D': D,
                                'image_rank': got, 'source_rank': D+1})


global_cases = []
for root_orders in ((1, 1, 1), (1, 2, 2), (2, 3, 2)):
    roots = tuple(range(len(root_orders)))
    for p in (3, 5, 7):
        if p <= max(root_orders) or len(set(x % p for x in roots)) != len(roots):
            continue
        for k in (1, 2, 3):
            tuples = list(product(roots, repeat=k))
            original_exponents = {}
            reduced_exponents = {}
            for tpl in tuples:
                orders = tuple(root_orders[i] for i in tpl)
                lam = sum(tpl)
                degree = 1 + sum(m-1 for m in orders)
                original_exponents[lam] = max(original_exponents.get(lam, 0), degree)
                reduced_exponents[lam % p] = max(reduced_exponents.get(lam % p, 0), min(p, degree))
            source_degree = sum(original_exponents.values())
            predicted_rank = sum(reduced_exponents.values())
            columns = [[] for _ in range(source_degree)]
            for tpl in tuples:
                local = local_powers(tuple(root_orders[i] for i in tpl), sum(tpl) % p, p, source_degree)
                for j, col in enumerate(local):
                    columns[j].extend(col)
            got = rank_mod(columns, p)
            assert got == predicted_rank, (root_orders, p, k, got, predicted_rank)
            global_cases.append({'root_orders': root_orders, 'p': p, 'k': k,
                                 'source_degree': source_degree, 'predicted_image_degree': predicted_rank,
                                 'actual_rank': got, 'kernel_dimension': source_degree-got})

base = Path(__file__).resolve().parent
paths = [base/'fragments/tensor_primary_update.tex', base/'fragments/PC30_coefficient_insertion.tex']
out = {'status': 'PASS', 'source_sha256': {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
       'local_cases': local_cases, 'residual_collision_cases': global_cases,
       'local_case_count': len(local_cases), 'residual_collision_case_count': len(global_cases),
       'scope': 'Exact supplementary coefficient tests; complete symbolic proofs are in the two pinned TeX files.'}
(base/'receipts').mkdir(exist_ok=True)
(base/'receipts/PC30_EXACT_CHECKS.json').write_text(json.dumps(out, indent=2), encoding='utf-8')
print(json.dumps({k: out[k] for k in ('status', 'local_case_count', 'residual_collision_case_count')}, indent=2))
