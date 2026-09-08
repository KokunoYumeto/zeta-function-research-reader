"""Independent finite sign-graph audit of the four frozen source matrices.

Reads source data without importing any author's matrix or sign checker.
All conclusions about q>0 use coefficientwise constant sign, not sampling.
"""
from __future__ import annotations
from collections import Counter, defaultdict, deque
from hashlib import sha256
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SOURCE = ROOT / 'agents/full_source_generators/full_generators.json'
BASIS = ROOT / 'agents/full_source_generators/source_basis/basis_1260.json'
data = json.loads(SOURCE.read_text())
basis = json.loads(BASIS.read_text())
assert sha256(SOURCE.read_bytes()).hexdigest() == 'e26086722e2910dc9ffff7d57314a25e80b79bb00bfb1808a42bf97761377253'
assert sha256(BASIS.read_bytes()).hexdigest() == '77233bf1fb129fd3dd7077987f1ae2ea62619aaff1ff178432a342fa2f15b767'
N = basis['dimension']
assert N == 1260
assert data['convention'] == 'columns indexed by source, rows by target; coefficient list [q exponent,integer]'
edges = []
by_color = {}
for color, columns in data['matrices'].items():
    assert len(columns) == N
    counts = Counter()
    for source, entries in enumerate(columns):
        assert len({target for target, coefficient in entries}) == len(entries)
        for target, coefficient in entries:
            assert 0 <= target < N and coefficient
            changed_color = color[1:]
            fixed_color = 'W' if changed_color == 'V' else 'V'
            change = 1 if color.startswith('E') else -1
            source_weight = basis['basis'][source]['weight_' + changed_color]
            target_weight = basis['basis'][target]['weight_' + changed_color]
            assert target_weight == [source_weight[0]+change, source_weight[1]-change]
            assert basis['basis'][source]['weight_' + fixed_color] == basis['basis'][target]['weight_' + fixed_color]
            assert len({exponent for exponent, value in coefficient}) == len(coefficient)
            assert all(isinstance(exponent, int) and isinstance(value, int) and value != 0
                       for exponent, value in coefficient)
            signs = {1 if value > 0 else -1 for exponent, value in coefficient}
            assert len(signs) == 1, (color, source, target, coefficient)
            sign = signs.pop()
            counts['positive' if sign == 1 else 'negative'] += 1
            counts['monomials'] += len(coefficient)
            edges.append({'id': len(edges), 'color': color, 'source': source,
                          'target': target, 'sign': sign, 'coefficient': coefficient})
    by_color[color] = dict(counts)

def describe(edge_id):
    edge = dict(edges[edge_id])
    edge['source_basis'] = basis['basis'][edge['source']]
    edge['target_basis'] = basis['basis'][edge['target']]
    return edge

def audit_graph(colors):
    chosen = [edge for edge in edges if edge['color'] in colors]
    adjacency = [[] for _ in range(N)]
    pairs = defaultdict(list)
    for edge in chosen:
        u, v = edge['source'], edge['target']
        assert u != v
        source_parity = (basis['basis'][u]['weight_V'][0] + basis['basis'][u]['weight_W'][0]) % 2
        target_parity = (basis['basis'][v]['weight_V'][0] + basis['basis'][v]['weight_W'][0]) % 2
        assert source_parity != target_parity
        adjacency[u].append((v, edge['id'], edge['sign']))
        adjacency[v].append((u, edge['id'], edge['sign']))
        pairs[tuple(sorted((u, v)))].append(edge['id'])
    assert all(len({edges[edge_id]['sign'] for edge_id in edge_ids}) == 1
               for edge_ids in pairs.values())
    seen = set()
    components = []
    for start in range(N):
        if start in seen:
            continue
        signs = {start: 1}
        queue = deque([start])
        seen.add(start)
        tree_edges = set()
        component_edges = set()
        while queue:
            u = queue.popleft()
            for v, edge_id, sign in adjacency[u]:
                component_edges.add(edge_id)
                if v not in signs:
                    seen.add(v)
                    signs[v] = signs[u] * sign
                    queue.append(v)
                    tree_edges.add(edge_id)
        conflicting = [edge_id for edge_id in sorted(component_edges - tree_edges)
                       if signs[edges[edge_id]['source']] * signs[edges[edge_id]['target']]
                       != edges[edge_id]['sign']]
        components.append({'vertices': sorted(signs), 'edge_count': len(component_edges),
                           'cycle_rank': len(component_edges) - len(signs) + 1,
                           'balanced': not conflicting,
                           'negative_fundamental_cycles': len(conflicting),
                           'first_conflicting_edge': conflicting[0] if conflicting else None})

    # Each lifted edge carries the parity of its real coefficient sign.
    # A shortest path from (u,+) to (u,-) is a negative closed walk.
    # The globally shortest such walk has no repeated intermediate lifted
    # vertex and contains no proper negative closed subwalk, hence is a
    # shortest negative multigraph cycle (parallel-edge cycles are allowed).
    best = None
    best_start = None
    best_parents = None
    for start in range(N):
        if not adjacency[start]:
            continue
        origin, goal = 2 * start, 2 * start + 1
        dist = {origin: 0}
        parents = {}
        queue = deque([origin])
        while queue:
            state = queue.popleft()
            distance = dist[state]
            if best is not None and distance >= best:
                continue
            u, parity = divmod(state, 2)
            for v, edge_id, sign in adjacency[u]:
                next_state = 2 * v + (parity ^ (sign == -1))
                if next_state in dist:
                    continue
                dist[next_state] = distance + 1
                parents[next_state] = state, edge_id
                if next_state == goal:
                    if best is None or distance + 1 < best:
                        best, best_start, best_parents = distance + 1, start, parents
                    queue.clear()
                    break
                queue.append(next_state)
        if best == 1:
            break
    cycle = None
    if best is not None:
        state, origin = 2 * best_start + 1, 2 * best_start
        steps = []
        while state != origin:
            previous, edge_id = best_parents[state]
            steps.append({'from': previous // 2, 'to': state // 2,
                          'edge': describe(edge_id),
                          'forward': edges[edge_id]['source'] == previous // 2})
            state = previous
        steps.reverse()
        assert len(steps) == best
        assert steps[0]['from'] == steps[-1]['to']
        assert all(steps[i]['to'] == steps[i+1]['from'] for i in range(len(steps)-1))
        sign_product = 1
        for step in steps:
            sign_product *= step['edge']['sign']
        assert sign_product == -1
        cycle = {'length': best, 'steps': steps, 'sign_product': sign_product}
    return {'colors': colors, 'vertices': N, 'edges': len(chosen),
            'distinct_unordered_pairs': len(pairs),
            'self_loops': sum(edge['source'] == edge['target'] for edge in chosen),
            'weight_parity_bipartite': True,
            'parallel_edges_have_agreeing_sign': True,
            'no_negative_cycles_below_length_four': True,
            'components': components,
            'nontrivial_components': sum(bool(c['edge_count']) for c in components),
            'isolated_vertices': sum(c['edge_count'] == 0 for c in components),
            'balanced_components': sum(c['balanced'] for c in components),
            'unbalanced_components': sum(not c['balanced'] for c in components),
            'cycle_rank': sum(c['cycle_rank'] for c in components),
            'negative_fundamental_cycles': sum(c['negative_fundamental_cycles'] for c in components),
            'shortest_negative_cycle': cycle}

graph_sets = [['FV'], ['EV'], ['FW'], ['EW'], ['FV', 'EV'], ['FW', 'EW'],
              ['FV', 'EV', 'FW', 'EW']]
graphs = [audit_graph(colors) for colors in graph_sets]

retained = basis['retained_labels']
assert {label: retained[label]['basis_index'] for label in ['T', 'T1', 'T2', 'Q']} == {
    'T': 126, 'T1': 146, 'T2': 8, 'Q': 144}
diamond = []
for source, target in [(126, 146), (146, 144), (8, 144), (126, 8)]:
    matches = [edge for edge in edges if edge['color'] == 'FV'
               and edge['source'] == source and edge['target'] == target]
    assert len(matches) == 1
    diamond.append(describe(matches[0]['id']))
assert [edge['sign'] for edge in diamond] == [1, 1, -1, 1]
assert diamond[0]['coefficient'] == [[-6,1],[-4,1],[4,1],[6,1]]
assert diamond[1]['coefficient'] == [[e,1] for e in range(-5,6,2)]
assert diamond[2]['coefficient'] == [[-2,-1],[0,-1],[2,-1]]
assert diamond[3]['coefficient'] == [[e,1] for e in range(-7,8,2)]
def multiply(left, right):
    product = defaultdict(int)
    for e, c in left:
        for f, d in right:
            product[e+f] += c*d
    return {e:c for e,c in product.items() if c}
positive_path = multiply(diamond[0]['coefficient'], diamond[1]['coefficient'])
negative_path = multiply(diamond[3]['coefficient'], diamond[2]['coefficient'])
path_sum = defaultdict(int, positive_path)
for exponent, value in negative_path.items():
    path_sum[exponent] += value
path_sum = {e:c for e,c in path_sum.items() if c}
original_C = [[-10,1],[-4,-1],[4,-1],[10,1]]
assert path_sum == multiply([[-1,1],[1,1]], original_C)
assert dict(original_C) == multiply([[-7,-1],[7,1]],[[-3,-1],[3,1]])
output = {'status': 'pass',
          'source_sha256': sha256(SOURCE.read_bytes()).hexdigest(),
          'basis_sha256': sha256(BASIS.read_bytes()).hexdigest(),
          'matrix_convention': data['convention'],
          'dimension': N, 'coefficientwise_counts': by_color,
          'entries': len(edges), 'all_entries_single_strict_coefficient_sign': True,
          'every_original_chevalley_weight_shift_verified': True,
          'positive_q_sign_proof': 'Every Laurent monomial q^k is positive for q>0; every entry has nonempty terms of one strict sign.',
          'graphs': graphs, 'retained_diamond': diamond,
          'retained_path_sum_equals_quantum_two_times_original_C': True,
          'original_C': original_C,
          'original_C_factorization': '(q^7-q^-7)(q^3-q^-3)',
          'retained_source_labels': {label:retained[label] for label in ['T','T1','T2','Q']}}
(HERE / 'verification.json').write_text(json.dumps(output, indent=2) + '\n')
print(json.dumps({'status':'pass', 'entries':len(edges),
                  'graphs':[{'colors':g['colors'], 'components':len(g['components']),
                             'unbalanced':g['unbalanced_components'],
                             'negative_girth':g['shortest_negative_cycle']['length']
                                 if g['shortest_negative_cycle'] else None}
                            for g in graphs]}))
