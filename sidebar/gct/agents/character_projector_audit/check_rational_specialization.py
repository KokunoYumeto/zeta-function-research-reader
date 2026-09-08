"""Check the corrected rational s_X inverse data without an integral inverse."""
from collections import Counter
from fractions import Fraction
from itertools import product
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent/'full_source_generators'


def main():
    graph_path = SOURCE/'quotient_audit/relation_graph_certificate.json'
    graph = json.loads(graph_path.read_text())
    basis_path = SOURCE/'source_basis/basis_1260.json'
    basis = json.loads(basis_path.read_text())['basis']
    original_path = SOURCE/'full_generators.json'
    projection = json.loads(original_path.read_text())['projection']
    alphabets = {1: ('1','2','3','4'), 2: ('12','13','23','32','24','34'),
                 3: ('123','124','134','234')}
    words = tuple(product(*(alphabets[h] for h in (3,3,3,2,2,1,1))))
    index = {word:i for i,word in enumerate(words)}
    seen = set()
    types = Counter()
    for component in graph['components']:
        for vertex in component['members']:
            assert vertex not in seen
            seen.add(vertex)
        bad = []
        for sign, exponent in component['cycles']:
            assert sign in (-1,1) and isinstance(exponent,int)
            value = sign*Fraction(2)**exponent
            assert (value == 1) == (sign == 1 and exponent == 0)
            if value != 1:
                bad.append((sign,exponent))
        if component['explicit_kills']:
            types['explicit_zero'] += 1
        elif bad:
            assert set(bad) == {(-1,0)}
            types['cycle_only_zero_over_Q'] += 1
        else:
            types['one_dimensional_over_Q'] += 1
    assert seen == set(range(36864))
    assert types == {'explicit_zero':4147, 'cycle_only_zero_over_Q':40,
                     'one_dimensional_over_Q':1260}
    lifts = []
    for b in basis:
        source_word = index[tuple(b['columns'])]
        n, sign, exponent = projection[source_word]
        assert n == b['index'] and sign*b['sign'] == 1
        assert exponent+b['p_power'] == 0 and b['p_power'] == -b['degree']
        lifts.append({'honest_basis_index':n, 'original_word_index':source_word,
                      'original_sign':b['sign'], 'original_p_power':b['p_power'],
                      'signed_scaled_word_coefficient':b['sign']*(-1)**b['degree']})
    assert {x['honest_basis_index'] for x in lifts} == set(range(1260))
    data = {'status':'passed', 'base':'Q with q=1 and p=2',
            'graph_vertex_partition':len(seen), 'component_types':dict(types),
            'specialized_domain_dimension':1260, 'specialized_codomain_dimension':1260,
            'specialized_relation_rank':35604, 'explicit_inverse_basis_lifts':lifts,
            'inverse_proof':'sbar_X j is identity on every honest basis vector; the1260 independent lifts exhaust the1260-dimensional domain, hence j sbar_X is identity.',
            'integral_scope':'No integral inverse to s_X. Its kernel after inverting p is (B/(2))^40. R inverts [2], not integer2; integer2 becomes a unit only after q=1 in R.',
            'input_hashes':{str(p.relative_to(HERE.parent.parent)):hashlib.sha256(p.read_bytes()).hexdigest()
                            for p in [graph_path,basis_path,original_path]}}
    (HERE/'rational_specialization_verification.json').write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({k:v for k,v in data.items() if k not in ['explicit_inverse_basis_lifts','input_hashes']},indent=2))


if __name__ == '__main__':
    main()
