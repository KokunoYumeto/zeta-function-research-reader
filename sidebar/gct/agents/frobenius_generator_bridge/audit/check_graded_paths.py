"""Integral, weightwise chain comparison for the exact corrected GCT paths."""
from collections import defaultdict
from pathlib import Path
from itertools import product
import json

ROOT = Path(__file__).resolve().parent
A = (-6, -4, 4, 6)
G = (-5, -3, -1, 1, 3, 5)
B = (-7, -5, -3, -1, 1, 3, 5, 7)
J = (-2, 0, 2)
P = (-1, 1)
C_even = (-10, 10)
C_odd = (-4, 4)

def grouped(left, right, prefix):
    result = defaultdict(list)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[a+b].append(f'{prefix}_{i}_{j}')
    return dict(result)

even = grouped(A, G, 'e')
odd = grouped(B, J, 'o')
target_even = grouped(P, C_even, 'u')
target_odd = grouped(P, C_odd, 'v')
weights = sorted(set(even) | set(odd), reverse=True)
differential, projection, inclusion, homotopy, table = {}, {}, {}, {}, []
source_degree = {x: 0 for xs in even.values() for x in xs}
source_degree.update({x: 1 for xs in odd.values() for x in xs})
source_weight = {x: w for w, xs in even.items() for x in xs}
source_weight.update({x: w for w, xs in odd.items() for x in xs})
for w in weights:
    ev, od = even.get(w, []), odd.get(w, [])
    n = min(len(ev), len(od))
    table.append(dict(weight=w, even=len(ev), odd=len(od), pairs=n,
                      residual=len(ev)-len(od),
                      matched_pairs=list(zip(ev[:n],od[:n])),
                      unmatched_even=ev[n:], unmatched_odd=od[n:]))
    for x, y in zip(ev[:n], od[:n]):
        differential[x] = y
        homotopy[y] = x
    for tail, target in ((ev[n:], target_even.get(w, [])),
                         (od[n:], target_odd.get(w, []))):
        assert len(tail) == len(target)
        for x, y in zip(tail, target):
            projection[x] = y
            inclusion[y] = x

assert len(source_degree) == 48
assert len(differential) == len(homotopy) == 20
assert len(projection) == len(inclusion) == 8
for x, y in differential.items():
    assert source_degree[y] == source_degree[x]+1
    assert source_weight[y] == source_weight[x]
    assert y not in differential
for target, source in inclusion.items():
    assert projection[source] == target
    assert source not in differential
for x in source_degree:
    # All maps are partial basis injections with coefficient +1.
    ip = inclusion.get(projection.get(x))
    dh = differential.get(homotopy.get(x))
    hd = homotopy.get(differential.get(x))
    assert sum(y == x for y in (ip, dh, hd)) == 1
    assert all(y is None or y == x for y in (ip, dh, hd))
    assert homotopy.get(homotopy.get(x)) is None
    assert projection.get(homotopy.get(x)) is None
for x in inclusion.values():
    assert homotopy.get(x) is None

# Preserve the unsimplified coefficient definitions in an independent
# integer Laurent coefficient calculation; no symbolic packages needed.
def quantum(n):
    return {n-1-2*i: 1 for i in range(n)}
def add(f, g, scale=1):
    out = dict(f)
    for w, v in g.items():
        out[w] = out.get(w, 0)+scale*v
    return {w:v for w,v in out.items() if v}
def multiply(f, g):
    out = {}
    for w, x in f.items():
        for v, y in g.items():
            out[w+v] = out.get(w+v, 0)+x*y
    return {w:v for w,v in out.items() if v}
alpha = add(quantum(7), quantum(3), -1)
beta, gamma = quantum(8), quantum(6)
delta = {w: -v for w,v in quantum(3).items()}
C = {10:1,4:-1,-4:-1,-10:1}
assert alpha == dict.fromkeys(A, 1)
paths = add(multiply(gamma,alpha), multiply(delta,beta))
assert paths == multiply(quantum(2), C)
assert paths == {x['weight']:x['residual'] for x in table if x['residual']}

# An actual degree-preserving stabilized module isomorphism maps
# E + P*C_odd -> O + P*C_even weightwise by sorted basis order.
stable_isomorphism = {}
for w in weights:
    domain = even.get(w, []) + target_odd.get(w, [])
    codomain = odd.get(w, []) + target_even.get(w, [])
    assert len(domain) == len(codomain)
    stable_isomorphism.update(zip(domain, codomain))
assert len(stable_isomorphism) == len(set(stable_isomorphism.values())) == 28

# Independently check the main fragment's opposite cone orientation:
# theta: R -> P has R in cochain degree -1 and P in degree zero.
# The earlier audit Gamma has E in degree zero and O in degree one.
# The same matched bases are used, but the differential is reversed.
main_differential = {y:x for x,y in differential.items()}
main_homotopy = dict(differential)
main_source_degree = {x:0 if x.startswith('e_') else -1
                      for x in source_degree}
for x,y in main_differential.items():
    assert main_source_degree[y] == main_source_degree[x]+1
    assert source_weight[x] == source_weight[y]
    assert y not in main_differential
for x in main_source_degree:
    ip = inclusion.get(projection.get(x))
    dh = main_differential.get(main_homotopy.get(x))
    hd = main_homotopy.get(main_differential.get(x))
    assert sum(y == x for y in (ip,dh,hd)) == 1
    assert all(y is None or y == x for y in (ip,dh,hd))
    assert main_homotopy.get(main_homotopy.get(x)) is None
    assert projection.get(main_homotopy.get(x)) is None
for x in inclusion.values():
    assert main_homotopy.get(x) is None

# This main H object has both weight lines in cohomological degree zero;
# it is not the unshifted whole cohomology grading of P^1.
endpoint_data = {
    'x00':dict(internal=-10,cohomological=2,tate_twist=5),
    'x03':dict(internal=-4,cohomological=7,tate_twist=2),
    'x70':dict(internal=4,cohomological=15,tate_twist=-2),
    'x73':dict(internal=10,cohomological=20,tate_twist=-5),
}
main_residual_table=[]
for source,target in projection.items():
    prefix,i,j=target.split('_'); i=int(i); j=int(j)
    hweight=P[i]
    label=('x00','x73')[j] if prefix=='u' else ('x03','x70')[j]
    datum=endpoint_data[label]
    degree=main_source_degree[source]
    assert source_weight[source] == hweight+datum['internal']
    assert degree % 2 == datum['cohomological'] % 2
    assert datum['internal'] == -2*datum['tate_twist']
    main_residual_table.append(dict(source=source,H_weight=hweight,
        endpoint_label=label,internal_degree=source_weight[source],
        cone_cohomological_degree=degree,
        endpoint_cohomological_degree=datum['cohomological']))
degree_differences={x['endpoint_cohomological_degree']-
                   x['cone_cohomological_degree'] for x in main_residual_table}
assert degree_differences == {2,8,16,20}
assert len(degree_differences) > 1 # no common cohomological shift

# Formal parity obstruction for all integral Tate characters after any
# diagonal integer state regrading: check every class modulo two.
arrow_solutions=[]
full_solutions=[]
for state_shifts in product((0,1),repeat=4):
    s0,s1,s2,s3=state_shifts
    arrow_residues=((s0-s1)%2,(1+s0-s2)%2,
                    (1+s1-s3)%2,(s2-s3)%2)
    if arrow_residues == (0,0,0,0):
        arrow_solutions.append(state_shifts)
        assert (s3-s0)%2 == 1
        if (s0-s3)%2 == 0:
            full_solutions.append(state_shifts)
assert arrow_solutions == [(0,0,1,1),(1,1,0,0)]
assert full_solutions == []

certificate = dict(
    status='pass', base_ring='Z', dimensions=dict(path_even=24,path_odd=24,
    target_even=4,target_odd=4,contractible_pairs=20),
    weight_table=table, differential=differential, contraction_h=homotopy,
    projection=projection, inclusion=inclusion,
    stabilized_module_isomorphism=stable_isomorphism,
    checks=['original unsimplified path identity', 'degree and weight',
    'd squared zero', 'projection inclusion identity',
    'identity minus inclusion projection equals d h plus h d',
    'h squared zero', 'h inclusion and projection h zero',
    'stabilized isomorphism bijection'],
    basis_exponents=dict(alpha=A,gamma=G,beta=B,delta_positive=J,
                         p=P,C_even=C_even,C_odd=C_odd),
    main_fragment_checks=dict(
        cone_differential=main_differential,
        cone_contraction=main_homotopy,
        source_cohomological_degrees=main_source_degree,
        endpoint_data=endpoint_data,
        residual_full_degree_table=main_residual_table,
        endpoint_minus_cone_degree_differences=sorted(degree_differences),
        arrow_integral_Tate_regradings_mod2=arrow_solutions,
        arrow_and_divided_square_integral_Tate_regradings_mod2=full_solutions,
        cochain_contraction_checks='pass',
        weight_and_parity_checks='pass',
        no_common_shift_check='pass',
        integral_Tate_parity_obstruction='pass'),
    restriction='The path differential is extra data and is not the tensor '
    'differential of the four zero-differential arrow complexes.')
(ROOT/'graded_path_certificate.json').write_text(json.dumps(certificate, indent=2)+'\n')
print(json.dumps(dict(status='pass',contractible_pairs=20,integral_homotopy=True)))
