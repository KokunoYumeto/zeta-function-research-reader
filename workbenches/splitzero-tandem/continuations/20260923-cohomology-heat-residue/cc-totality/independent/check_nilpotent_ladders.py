"""Exact integer and rational-complex checks of OLM, independent of rendering."""
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import hashlib
import json

B = Path(__file__).resolve().parent
proof = B / 'MIXED_TENSOR_NILPOTENT_LADDERS.tex'


def add(z, w):
    return (z[0]+w[0], z[1]+w[1])


def mul(z, w):
    return (z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0])


def scale(z, a):
    return (a*z[0], a*z[1])


def power(z, n):
    result = (F(1), F(0))
    for _ in range(n):
        result = mul(result, z)
    return result


def primitive(j, r):
    # r disjoint factors e*f-f*e and j-2r unchanged factors e.
    result = {0: 1}
    for i in range(r):
        nxt = {}
        for mask, value in result.items():
            nxt[mask | 1 << (2*i+1)] = value
            nxt[mask | 1 << (2*i)] = -value
        result = nxt
    return result


def act(v, j, eps, lowering=False):
    result = {}
    for mask, value in v.items():
        for i in range(j):
            present = bool(mask & (1 << i))
            if present == lowering:
                target = mask ^ (1 << i)
                result[target] = result.get(target, 0) + eps*value
    return {mask: value for mask, value in result.items() if value}


checks = []
eps = 3  # independent exact instance; the proof retains symbolic epsilon>0
h = (F(2, 5), F(3, 7))
abs_h_sq = h[0]**2+h[1]**2
for j in range(9):
    for r in range(j//2+1):
        d = j-2*r
        u = primitive(j, r)
        assert not act(u, j, eps, True)
        levels = [u]
        assert sum(value*value for value in u.values()) == 2**r
        for a in range(1, d+2):
            levels.append(act(levels[-1], j, eps))
            lowering = act(levels[a], j, eps, True)
            factor = eps**2*a*(d-a+1)
            wanted = {m: factor*c for m, c in levels[a-1].items() if factor*c}
            assert lowering == wanted
            if a <= d:
                s = eps**(2*a)*factorial(a)*factorial(d)//factorial(d-a)
                assert sum(value*value for value in levels[a].values()) == s*2**r
        assert not levels[-1]
        # Compute (I+hR)^{tensor j} directly in the original e/f words.
        direct = {}
        for mask, value in u.items():
            absent = ((1 << j)-1)^mask
            subset = absent
            while True:
                z = scale(power(scale(h, eps), subset.bit_count()), value)
                target = mask | subset
                direct[target] = add(direct.get(target, (F(0), F(0))), z)
                if subset == 0:
                    break
                subset = (subset-1) & absent
        direct = {m:z for m,z in direct.items() if z != (0,0)}
        ladder = {}
        for a in range(d+1):
            coefficient = scale(power(h,a), F(1,factorial(a)))
            for mask, value in levels[a].items():
                ladder[mask] = add(ladder.get(mask,(F(0),F(0))),
                                   scale(coefficient,value))
        ladder = {m:z for m,z in ladder.items() if z != (0,0)}
        assert direct == ladder
        energy = sum(z[0]**2+z[1]**2 for z in direct.values())
        predicted = sum(F(eps**(2*a)*factorial(d),
                          factorial(a)*factorial(d-a))*abs_h_sq**a*2**r
                        for a in range(d+1))
        assert energy == predicted
        # Exact cross-Gram entries from two different initial ladder positions.
        for a in range(d+1):
            for c in range(d+1):
                left, right = {}, {}
                for b in range(a,d+1):
                    z = scale(power(h,b-a), F(1,factorial(b-a)))
                    for mask,value in levels[b].items():
                        left[mask] = add(left.get(mask,(F(0),F(0))),scale(z,value))
                for b in range(c,d+1):
                    z = scale(power(h,b-c), F(1,factorial(b-c)))
                    for mask,value in levels[b].items():
                        right[mask] = add(right.get(mask,(F(0),F(0))),scale(z,value))
                gram = (F(0),F(0))
                for mask,z in left.items():
                    gram = add(gram,mul((z[0],-z[1]),right.get(mask,(F(0),F(0)))))
                expected = (F(0),F(0))
                for b in range(max(a,c),d+1):
                    weight = F(eps**(2*b)*factorial(b)*factorial(d)*2**r,
                               factorial(d-b)*factorial(b-a)*factorial(b-c))
                    expected = add(expected,scale(mul(power((h[0],-h[1]),b-a),
                                                        power(h,b-c)),weight))
                assert gram == expected
        checks.append({'kind':'original_word_ladder_and_complex_energy',
                       'active_slots':j,'primitive_grade':r,'length':d+1,
                       'epsilon':eps,'h_real':str(h[0]),'h_imag':str(h[1]),
                       'cross_gram_entries':(d+1)**2})

for k in (17,21,25):
    q=(k+1)**2
    for t in range(1,9):
        multiplicities={}
        for j in range(t+1):
            for r in range(j//2+1):
                length=j-2*r+1
                primitive_dim=comb(j,r)-(comb(j,r-1) if r else 0)
                multiplicities[length]=multiplicities.get(length,0)+(
                    comb(t,j)*(q-2)**(t-j)*primitive_dim)
        assert sum(length*count for length,count in multiplicities.items())==q**t
        assert multiplicities[t+1]==1
        kernel=sum(comb(t,j)*(q-2)**(t-j)*comb(j,j//2) for j in range(t+1))
        assert sum(multiplicities.values())==kernel
        checks.append({'kind':'complete_original_dimension_and_kernel',
                       'k':k,'q':q,'tensor_degree':t,
                       'cutoffs':[q-1,q,2*q-1,2*q],
                       'multiplicities':multiplicities,
                       'full_dimension':q**t,'kernel_dimension':kernel})

receipt={'status':'PASS','groups':len(checks),
         'proof_sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),
         'checks':checks,
         'scope':'Finite exact checks of actual original-word operators and complex phases. Complete symbolic proofs for all parameters are in OLM1-28. No original parameter or metric was numerically replaced in that proof.'}
(B/'NILPOTENT_LADDER_EXACT_CHECKS.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print(json.dumps({key:receipt[key] for key in ('status','groups','proof_sha256')}))
