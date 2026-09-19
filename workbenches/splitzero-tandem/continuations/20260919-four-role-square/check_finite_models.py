"""Finite regression checks accompanying general proofs, not substitutes for them."""
from itertools import product
from pathlib import Path
import json

T, O = 'T', 'Omega'

def algebra(n, kind):
    old = list(range(n))
    elements = old + ([] if kind == 'A' else [T]) + [O]
    zero = 0 if kind == 'A' else T
    def add(x, y):
        if O in (x, y): return O
        if x == T: return y
        if y == T: return x
        return (x + y) % n
    def mul(x, y):
        if kind == 'sharp' and T in (x, y): return T
        if O in (x, y): return O
        if T in (x, y): return T
        return (x * y) % n
    return elements, add, mul, zero, 1 % n

def check_laws(data):
    xs, add, mul, zero, one = data
    assert all(add(x, zero) == x and mul(x, one) == x for x in xs)
    assert all(add(x,y) == add(y,x) and mul(x,y) == mul(y,x) for x,y in product(xs, repeat=2))
    for x,y,z in product(xs, repeat=3):
        assert add(add(x,y),z) == add(x,add(y,z))
        assert mul(mul(x,y),z) == mul(x,mul(y,z))
        assert mul(x,add(y,z)) == add(mul(x,y),mul(x,z))
    return {'elements': len(xs), 'triples': len(xs)**3,
            'global_zero_absorption': all(mul(zero,x) == zero for x in xs)}

def partitions(xs):
    if not xs:
        yield []
        return
    first, *rest = xs
    for blocks in partitions(rest):
        yield [{first}] + [set(b) for b in blocks]
        for i in range(len(blocks)):
            yield [set(b) | ({first} if j == i else set()) for j,b in enumerate(blocks)]

results = {'scope': 'exhaustive finite examples only; general proofs in accompanying TeX', 'models': []}
for n in [2,3,4]:
    h = algebra(n, 'H')
    for kind in ['H','A','sharp']:
        record = check_laws(algebra(n,kind))
        assert record['global_zero_absorption'] == (kind == 'sharp')
        results['models'].append({'ring': f'Z/{n}Z', 'construction': kind, **record})
    xs, add, mul, _, _ = h
    _, aa, am, _, _ = algebra(n, 'A')
    q = lambda x: 0 if x == T else x
    sig = lambda x: T if x == T else O if x == O else 1
    def sa(x,y):
        return O if O in (x,y) else y if x == T else x if y == T else 1
    def sm(x,y):
        return O if O in (x,y) else T if T in (x,y) else 1
    assert len({(q(x),sig(x)) for x in xs}) == len(xs)
    for x,y in product(xs,repeat=2):
        assert q(add(x,y)) == aa(q(x),q(y))
        assert q(mul(x,y)) == am(q(x),q(y))
        assert sig(add(x,y)) == sa(sig(x),sig(y))
        assert sig(mul(x,y)) == sm(sig(x),sig(y))
    count = 0
    for blocks in partitions(xs):
        cls = {x:i for i,b in enumerate(blocks) for x in b}
        congruence = all(cls[add(x,z)] == cls[add(y,z)] and cls[mul(x,z)] == cls[mul(y,z)]
                         for b in blocks for x,y in product(b, repeat=2) for z in xs)
        count += congruence
    expected = 2*sum(n%d == 0 for d in range(1,n+1))+1
    assert count == expected
    results.setdefault('congruences',[]).append({'ring':f'Z/{n}Z','all_partitions_checked':True,'congruences':count,'predicted':expected})
    # Nonunital, zero-preserving universal u receiver; original S excludes Omega.
    ui = lambda x: 0 if x == T else 1
    for x,y in product([x for x in xs if x != O],repeat=2):
        assert ui(add(x,y)) == max(ui(x),ui(y))
        assert ui(mul(x,y)) == min(ui(x),ui(y))

results['chain_u_receiver'] = check_laws(([0,1,2],max,min,0,2))
results['common_identity_receiver'] = check_laws(([0,1],max,max,0,0))
results['powerset_union_union'] = check_laws((list(range(4)),lambda x,y:x|y,lambda x,y:x|y,0,0))
results['powerset_union_intersection'] = check_laws((list(range(4)),lambda x,y:x|y,lambda x,y:x&y,0,3))
results['all_checks_passed'] = True
out = Path(__file__).with_name('FINITE_MODEL_CHECKS.json')
out.write_text(json.dumps(results,indent=2)+'\n',encoding='utf8')
print(json.dumps(results,indent=2))
