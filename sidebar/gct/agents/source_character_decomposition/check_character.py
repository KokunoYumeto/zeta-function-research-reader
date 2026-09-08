"""Exact source-honest highest-weight count and independent SSYT character.

No external algebra packages or source files are needed for reproduction.
The complete source inequalities, shape and column contents are retained.
"""
from collections import Counter
from itertools import combinations_with_replacement, product
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
NU = (7, 5, 3)
COL_SHAPE = (0, 3, 2, 2)
N = sum(NU)


def honest_highest():
    out = []
    for i3, i2, i1 in product(range(2), repeat=3):
        n3, n2, n1 = 3 - 2*i3, 2 - 2*i2, 2 - 2*i1
        for a in range(n3 + 1):
            for b in range(n3 - a + 1):
                c = n3 - a - b
                for d in range(n2 + 1):
                    for e in range(n2 - d + 1):
                        g = n2 - d - e
                        # Source Proposition p highest weight straightened NST.
                        if b*c != 0 or (d > 0 and c != 0):
                            continue
                        if e > 0 and b > 1:
                            continue
                        if g > 1 or (g == 1 and n1 == 0):
                            continue
                        if b > n1 + e or c > n1 + d:
                            continue
                        shift = 3*i3 + 2*i2 + i1
                        v1 = 2*a + 2*b + c + 2*d + e + g + n1 + shift
                        w1 = 2*a + b + 2*c + d + 2*e + g + n1 + shift
                        assert 2*v1 >= N and 2*w1 >= N
                        out.append({
                            'invariant_record': [0, i3, i2, i1],
                            'columns_123_124_134_12_13_23_1': [a,b,c,d,e,g,n1],
                            'lambda': [v1,N-v1], 'mu': [w1,N-w1],
                            'dimension': (2*v1-N+1)*(2*w1-N+1),
                        })
    return out


def ssyt():
    rows = [list(combinations_with_replacement(range(1,5), n)) for n in NU]
    for r1 in rows[0]:
        for r2 in rows[1]:
            if not all(r1[j] < r2[j] for j in range(NU[1])):
                continue
            for r3 in rows[2]:
                if all(r2[j] < r3[j] for j in range(NU[2])):
                    yield (r1,r2,r3)


def tableau_weight(t):
    c = Counter(x for row in t for x in row)
    return (c[1]+c[2],c[1]+c[3])


def main():
    highest = honest_highest()
    mult = Counter((x['lambda'][0],x['mu'][0]) for x in highest)
    original_character = Counter()
    for (a,b), m in mult.items():
        for u in range(N-a,a+1):
            for v in range(N-b,b+1):
                original_character[u,v] += m
    tableaux = list(ssyt())
    schur_character = Counter(tableau_weight(t) for t in tableaux)
    assert original_character == schur_character
    assert len(tableaux) == 1260
    assert sum(x['dimension'] for x in highest) == 1260
    for a,b in product(range(8,16), repeat=2):
        d = (schur_character[a,b]-schur_character[a+1,b]
             -schur_character[a,b+1]+schur_character[a+1,b+1])
        assert d == mult[a,b]
    for u,v in original_character:
        assert original_character[u,v] == original_character[N-u,v]
        assert original_character[u,v] == original_character[u,N-v]
        assert original_character[u,v] == original_character[v,u]
    locations = []
    for u,v in [(12,9),(11,9),(10,9)]:
        components = [
            {'lambda':[a,N-a], 'mu':[b,N-b], 'multiplicity': m,
             'divided_power_positions':[a-u,b-v]}
            for (a,b),m in sorted(mult.items(), reverse=True)
            if N-a <= u <= a and N-b <= v <= b
        ]
        assert sum(c['multiplicity'] for c in components) == original_character[u,v]
        locations.append({'weight':[u,N-u,v,N-v],
                          'dimension':original_character[u,v], 'components':components})
    data = {
        'status':'passed', 'row_shape':NU, 'column_count_shape':COL_SHAPE,
        'dimension':1260, 'number_of_simple_summands_with_multiplicity':len(highest),
        'highest_first_coordinate_order':list(range(12,7,-1)),
        'multiplicity_matrix':[[mult[a,b] for b in range(12,7,-1)] for a in range(12,7,-1)],
        'full_weight_first_coordinate_order':list(range(12,2,-1)),
        'full_weight_matrix':[[original_character[u,v] for v in range(12,2,-1)] for u in range(12,2,-1)],
        'dominant_weight_matrix':[[original_character[u,v] for v in range(12,7,-1)] for u in range(12,7,-1)],
        'highest_classes':highest, 'retained_weight_locations':locations,
        'checks':['honest-source enumeration equals all SSYT weights',
                  'mixed finite differences equal honest highest-weight counts',
                  'all weights reconstruct from irreducible rectangles',
                  'dimension 1260 by two exact counts',
                  'both Weyl reflections and V/W interchange hold'],
    }
    tables = []
    ordered = sorted(highest, key=lambda z:(z['invariant_record'],z['columns_123_124_134_12_13_23_1']))
    for offset in range(0,len(ordered),24):
        lines = [r'\begin{center}\small',r'\begin{tabular}{ccccccr}',r'\toprule',
                 r'$(i_3,i_2,i_1)$ & $(A,B,C)$ & $(D,E,G)$ & $f$ & $\lambda$ & $\mu$ & dimension\\',r'\midrule']
        for x in ordered[offset:offset+24]:
            a,b,c,d,e,g,f = x['columns_123_124_134_12_13_23_1']
            triple = lambda t:'('+','.join(map(str,t))+')'
            fields=[triple(x['invariant_record'][1:]),triple((a,b,c)),triple((d,e,g)),str(f),triple(x['lambda']),triple(x['mu'])]
            lines.append(' & '.join('$'+v+'$' for v in fields)+' & '+str(x['dimension'])+r'\\')
        lines += [r'\bottomrule',r'\end{tabular}',r'\end{center}']
        tables.append('\n'.join(lines))
    (ROOT/'highest_classes.tex').write_text('\n\n'.join(tables)+'\n',encoding='utf8')
    (ROOT/'character_certificate.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf8')
    print(json.dumps({k:data[k] for k in ['status','dimension','number_of_simple_summands_with_multiplicity','multiplicity_matrix','dominant_weight_matrix','retained_weight_locations']},indent=2))


if __name__ == '__main__':
    main()
