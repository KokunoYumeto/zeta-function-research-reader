"""Independent exact audit of original matrices and specialized string maps.

Writes only in this directory. No author checker is imported. Laurent
polynomials are dictionaries over Z; specialized kernels use exact Q.
"""
from pathlib import Path
from collections import defaultdict, Counter
from fractions import Fraction
from itertools import product
import hashlib
import json
import time
import sympy as sp

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent / 'full_source_generators'
CHARACTER = HERE.parent / 'source_character_decomposition'


def add(a, b, sign=1):
    c = dict(a)
    for e, x in b.items():
        c[e] = c.get(e, 0) + sign*x
        if not c[e]:
            del c[e]
    return c


def mul(a, b):
    c = {}
    for e, x in a.items():
        for f, y in b.items():
            c[e+f] = c.get(e+f, 0) + x*y
    return {e: x for e, x in c.items() if x}


def qi(n):
    return {e: (1 if n > 0 else -1) for e in range(1-abs(n), abs(n), 2)}


def vadd(a, b, scalar=None, sign=1):
    c = dict(a)
    for i, x in b.items():
        c[i] = add(c.get(i, {}), x if scalar is None else mul(x, scalar), sign)
        if not c[i]:
            del c[i]
    return c


def act(M, v):
    c = {}
    for i, x in v.items():
        c = vadd(c, M[i], x)
    return c


def rational_act(M, v):
    c = defaultdict(Fraction)
    for i, x in v.items():
        for j, y in M[i].items():
            c[j] += x*y
    return {i: x for i, x in c.items() if x}


def scale(v, c):
    return {i: x*c for i, x in v.items() if x*c}


def main():
    start = time.perf_counter()
    paths = [SOURCE/'full_generators.json', SOURCE/'source_basis/basis_1260.json',
             CHARACTER/'character_certificate.json', CHARACTER/'character_decomposition.tex',
             CHARACTER/'check_character.py', CHARACTER/'check_actual_projectors.py']
    original = json.loads(paths[0].read_text())
    raw = original['matrices']
    basis = json.loads(paths[1].read_text())['basis']
    matrices = {name: [{j: dict(coeff) for j, coeff in col} for col in cols]
                for name, cols in raw.items()}
    assert len(basis) == 1260
    weights = [(x['weight_V'][0], x['weight_W'][0]) for x in basis]
    assert all(sum(x['weight_V']) == sum(x['weight_W']) == 15 for x in basis)
    for name, cols in matrices.items():
        delta = (1 if name[0] == 'E' else -1)
        shift = (delta, 0) if name[1] == 'V' else (0, delta)
        for i, col in enumerate(cols):
            for j in col:
                assert weights[j] == tuple(weights[i][k] + shift[k] for k in range(2))
    casimirs = {}
    for colour, axis in [('V', 0), ('W', 1)]:
        B = []
        for i in range(len(basis)):
            h = 2*weights[i][axis]-15
            B.append(vadd(act(matrices['F'+colour], matrices['E'+colour][i]),
                          {i: mul(qi((h+1)//2), qi((h+1)//2))}))
        casimirs[colour] = B
        for name, M in matrices.items():
            for i in range(len(basis)):
                assert act(B, M[i]) == act(M, B[i]), (colour, name, i)
        for i in range(len(basis)):
            v = {i: {0: 1}}
            for j in range(1, 6):
                v = vadd(act(B, v), v, mul(qi(j), qi(j)), -1)
            assert not v, (colour, i)
    print('Integral Casimir centrality and spectral annihilator passed on all 1260 columns.', flush=True)

    column_alphabets = {1: ('1','2','3','4'), 2: ('12','13','23','32','24','34'),
                        3: ('123','124','134','234')}
    original_words = {word: i for i, word in enumerate(product(
        *(column_alphabets[h] for h in (3,3,3,2,2,1,1))))}
    retained = {'T': (('123','123','124','12','12','1','1'), 1, 0),
                'T1': (('123','123','124','23','12','1','1'), 1, 0),
                'T2': (('123','123','123','12','12','4','1'), -1, -1),
                'Q': (('123','123','124','13','12','4','1'), -1, -1)}
    retained_records = {}
    for label, (word, sign, exponent) in retained.items():
        index, projected_sign, projected_exponent = original['projection'][original_words[word]]
        assert sign*projected_sign == 1 and exponent+projected_exponent == 0
        assert not matrices['EV'][index] and not matrices['EW'][index]
        for axis, colour in enumerate(('V','W')):
            n = 2*weights[index][axis]-15
            assert casimirs[colour][index] == {index: mul(qi((n+1)//2),qi((n+1)//2))}
        retained_records[label] = {'basis_index': index, 'original_columns': word,
                                   'original_sign': sign, 'original_p_power': exponent,
                                   'actual_highest_pair': list(weights[index]),
                                   'all_original_raising_columns_zero': True}
    twice_lowered = act(matrices['FV'], matrices['FV'][retained_records['T']['basis_index']])
    retained_C = {-10: 1, -4: -1, 4: -1, 10: 1}
    assert twice_lowered[retained_records['Q']['basis_index']] == mul(qi(2),retained_C)
    projected_numerator = twice_lowered
    for j in (1,2,4,5):
        projected_numerator = vadd(act(casimirs['V'], projected_numerator), projected_numerator,
                                   mul(qi(j),qi(j)), -1)
    assert not projected_numerator

    # A separate exact reconstruction at q=1 from genuine simultaneous kernels.
    M1 = {name: [{j: sum(p.values()) for j, p in col.items() if sum(p.values())}
                  for col in cols] for name, cols in matrices.items()}
    weight_indices = defaultdict(list)
    for i, w in enumerate(weights):
        weight_indices[w].append(i)
    mult = Counter()
    by_weight = defaultdict(list)
    tops = []
    action_checks = 0
    for a, b in product(range(8, 13), repeat=2):
        indices = weight_indices[a, b]
        if not indices:
            continue
        targets = [('EV', i) for i in weight_indices[a+1, b]]
        targets += [('EW', i) for i in weight_indices[a, b+1]]
        stacked = sp.zeros(len(targets), len(indices))
        for r, (name, target) in enumerate(targets):
            for c, source in enumerate(indices):
                stacked[r, c] = M1[name][source].get(target, 0)
        nullbasis = stacked.nullspace()
        mult[a, b] = len(nullbasis)
        n, m = 2*a-15, 2*b-15
        for top_column in nullbasis:
            top = {indices[i]: Fraction(x) for i, x in enumerate(top_column) if x}
            assert not rational_act(M1['EV'], top)
            assert not rational_act(M1['EW'], top)
            tops.append({'lambda': [a,15-a], 'mu': [b,15-b],
                         'coefficients': [[i,str(x)] for i,x in sorted(top.items())]})
            strings = {}
            for i in range(n+1):
                if not i:
                    head = top
                else:
                    head = scale(rational_act(M1['FV'], strings[i-1, 0]), Fraction(1,i))
                for j in range(m+1):
                    v = head if not j else scale(rational_act(M1['FW'], strings[i,j-1]), Fraction(1,j))
                    strings[i,j] = v
                    assert set(v).issubset(weight_indices[a-i,b-j])
                    by_weight[a-i,b-j].append(v)
            for (i,j), v in strings.items():
                cases = [('FV', strings.get((i+1,j),{}), i+1),
                         ('EV', strings.get((i-1,j),{}), n-i+1),
                         ('FW', strings.get((i,j+1),{}), j+1),
                         ('EW', strings.get((i,j-1),{}), m-j+1)]
                for name, expected, coefficient in cases:
                    assert rational_act(M1[name], v) == scale(expected, coefficient)
                    action_checks += 1
    certificate = json.loads(paths[2].read_text())
    expected_mult = certificate['multiplicity_matrix']
    actual_mult = [[mult[a,b] for b in range(12,7,-1)] for a in range(12,7,-1)]
    assert actual_mult == expected_mult
    total_rank = 0
    weight_ranks = []
    for weight, indices in sorted(weight_indices.items()):
        if not indices:
            continue
        cols = by_weight[weight]
        assert len(cols) == len(indices)
        block = sp.Matrix([[col.get(i,0) for col in cols] for i in indices])
        rank = block.rank()
        assert rank == len(indices)
        total_rank += rank
        weight_ranks.append({'weight': list(weight), 'dimension': len(indices), 'string_rank': rank})
    assert total_rank == 1260 and len(tops) == 48
    differences = [j*j-k*k for j in range(1,6) for k in range(1,6) if j != k]
    primes = set()
    for s in list(range(1,10))+differences:
        primes.update(sp.factorint(abs(s)))
    assert primes == {2,3,5,7}
    result = {
        'status': 'passed',
        'input_hashes': {str(p.relative_to(HERE.parent.parent)): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
        'source_dimension': 1260,
        'integral_casimir_commutator_columns': 2*4*1260,
        'integral_spectral_annihilator_columns': 2*1260,
        'annihilator': 'product_{j=1}^5 (B-[j]^2)',
        'retained_original_highest_vectors': retained_records,
        'retained_coefficient': 'coefficient_Q(F_V^2 T) = [2]*(q^10-q^4-q^-4+q^-10)',
        'retained_isotypic_projection': 'Pi_5(B_V) F_V^2 T = 0, verified with integral projector numerator',
        'specialization': 'q=1 over Q; exact rational kernel calculations, not evidence for an unlocalized integral splitting',
        'actual_highest_kernel_dimension': len(tops),
        'actual_highest_multiplicity_matrix': actual_mult,
        'full_string_action_checks': action_checks,
        'full_string_rank': total_rank,
        'weight_string_ranks': weight_ranks,
        'actual_specialized_highest_vectors': tops,
        'localization_specialization_primes': sorted(primes),
        'seconds': time.perf_counter()-start,
    }
    (HERE/'independent_verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ['input_hashes','weight_string_ranks','actual_specialized_highest_vectors']},indent=2))


if __name__ == '__main__':
    main()
