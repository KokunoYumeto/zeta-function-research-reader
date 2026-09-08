"""Source-independent exact GCT-IV path and integral-algebra checker.

The mathematical proof is in generator_block.tex and generator_paths.tex.
This script enumerates all 31 required graphical terms, applies the explicit
contextual corrections, checks exhaustive exclusions and verifies integral
matrix identities. A matching scalar is never substituted for a label proof.
Only --refresh-source-receipts reads the retained primary-source shelf.
"""
from pathlib import Path
from collections import Counter
import argparse
import hashlib
import json
import sympy as s

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT.parent / 'nonstandard_rh/shelf/cs_0703110v4/source/Apr13KroneckerGCT4.tex'
q = s.Symbol('q', nonzero=True)

def qi(n):
    return sum(q ** (n - 1 - 2*j) for j in range(n)) if n else s.Integer(0)

def zero(x):
    return s.cancel(s.expand(x)) == 0

columns = {
    'T': ['123','123','124','12','12','1','1'],
    'T1': ['123','123','124','23','12','1','1'],
    'T2': ['123','123','123','12','12','4','1'],
    'printed_target': ['123','123','124','23','12','4','1'],
    'Q': ['123','123','124','13','12','4','1'],
}
rescalings = {'T':'1','T1':'1','T2':'-1/[2]', 'printed_target':'-1/[2]','Q':'-1/[2]'}

def weight(cols):
    letters = Counter(''.join(cols))
    return {'V':[letters['1']+letters['2'], letters['3']+letters['4']],
            'W':[letters['1']+letters['3'], letters['2']+letters['4']]}

# Canonical column words from the source's NSC label dictionary. The source's
# two differently ordered middle columns 23 and 32 must remain distinct.
words = {
    '1':('1','1'), '3':('2','1'), '4':('2','2'),
    '12':('11','21'), '13':('21','11'),
    '23':('21','12'), '32':('12','21'),
    '123':('211','121'), '124':('211','221'),
    '134':('212','121'), '234':('212','221'),
    '2':('1','2'), '24':('21','22'), '34':('22','21'),
}

def unpaired(cols, side):
    word = ''.join(words[c][side] for c in cols)
    positions = [(column+1, place+1) for column,c in enumerate(cols) for place in range(len(c))]
    stack, ones, arcs = [], [], []
    for i,ch in enumerate(word):
        if ch == '2':
            stack.append(i)
        elif stack:
            arcs.append([stack.pop()+1,i+1])
        else:
            ones.append(i)
    return {'word':word,'unpaired_ones':[list(positions[i]) for i in ones],
            'unpaired_twos':[list(positions[i]) for i in stack], 'arcs':arcs}

weights = {name:weight(cols) for name,cols in columns.items()}
assert weights == {
    'T':{'V':[12,3],'W':[9,6]},
    'T1':{'V':[11,4],'W':[9,6]},
    'T2':{'V':[11,4],'W':[9,6]},
    'printed_target':{'V':[10,5],'W':[8,7]},
    'Q':{'V':[10,5],'W':[9,6]},
}
alpha,beta,gamma,delta = qi(7)-qi(3),qi(8),qi(6),-qi(3)
p = qi(2)
C = q**10-q**4-q**-4+q**-10
r = q-q**-1
N = s.Matrix([[0,0,0,0],[alpha,0,0,0],[beta,0,0,0],[0,gamma,delta,0]])
D = s.zeros(4)
D[3,0] = C
assert all(zero(x) for x in N*N-p*D)
assert N**3 == s.zeros(4)
assert zero(C-r**2*qi(7)*qi(3))
assert zero(gamma-qi(3)*(q**3+q**-3))
assert zero((q**3+q**-3)*alpha-beta-p*r**2*qi(7))
assert all(zero(x) for x in N*D) and all(zero(x) for x in D*N)
KV = s.diag(q**9,q**7,q**7,q**5)
assert all(zero(x) for x in KV*N-q**-2*N*KV)
NW = s.zeros(4)
assert N*NW == NW*N
N0 = N.subs(q,1)
assert N0 == s.Matrix([[0,0,0,0],[4,0,0,0],[8,0,0,0],[0,6,-3,0]])
assert N0.rank() == 2 and N0*N0 == s.zeros(4)
assert s.diff(C,q,2).subs(q,1) == 168
assert C.subs(q,1) == s.diff(C,q).subs(q,1) == 0
k = s.Matrix([0,1,q**3+q**-3,0])
assert all(zero(x) for x in N*k)
e = s.eye(4)
generic_change = s.Matrix.hstack(e[:,0],N*e[:,0],N*N*e[:,0],k)
assert zero(generic_change.det()+p**2*r**4*qi(7)**2*qi(3))
special_change = s.Matrix.hstack(e[:,0],N0*e[:,0],e[:,2],N0*e[:,2])
assert special_change.det() == -12

# These finite rewriting rules are transcribed with their proofs in
# generator_paths.tex. The default run never accesses the primary source.
# Crucially, nonintegral equal-height rules inspect the surrounding prefix;
# they are not treated as ordinary local relations in a commutative product.
def pairing(cols, side):
    coords = [(c,i) for c,col in enumerate(cols) for i in range(len(col))]
    word = ''.join(words[c][side] for c in cols)
    pending, ones, arcs = [], [], []
    for pos,ch in zip(coords,word):
        if ch == '2':
            pending.append(pos)
        elif pending:
            arcs.append((pending.pop(),pos))
        else:
            ones.append(pos)
    return ones,pending,arcs

def invariant_record(cols):
    pairs = Counter()
    for side in (0,1):
        for (a,_),(b,_) in pairing(cols,side)[2]:
            if a != b:
                pairs[a,b] += 1
    heights = Counter()
    for (a,b),number in pairs.items():
        if number == 2 and len(cols[a]) == len(cols[b]):
            heights[len(cols[a])] += 1
    return [heights[j] for j in (4,3,2,1)]

def raise_prefix(cols, side):
    twos = pairing(cols,side)[1]
    if not twos:
        return None
    c,_ = twos[-1]
    # Only these three changes occur in this bounded source calculation.
    raising = {0:{'234':'124'},1:{'124':'123','23':'13'}}
    assert cols[c] in raising[side], (cols,side,c)
    out = list(cols)
    out[c] = raising[side][cols[c]]
    return out

INTEGRAL = {
    ('234','12'):(-1,('124','23'),'source height (3,2)'),
    ('134','12'):(-1,('124','13'),'source height (3,2)'),
    ('234','23'):(-1,('234','32'),'source height (3,2)'),
    ('32','1'):(1,('23','1'),'source height (2,1)'),
    ('12','23'):(1,('23','12'),'source height (2,2)'),
}
CONTEXTUAL = {
    ('134','123'):(1,'11',('234','123')),
    ('134','124'):(1,'12',('234','123')),
    ('32','12'):(0,'11',('34','12')),
    ('3','1'):(1,'11',('4','1')),
    ('23','23'):(1,'12',('24','13')),
}

def reduce_columns(cols, scalar):
    cols = list(cols)
    history = []
    for count in range(30):
        changed = False
        for i in range(len(cols)-1):
            pair = tuple(cols[i:i+2])
            if pair in CONTEXTUAL:
                side,local_word,replacement = CONTEXTUAL[pair]
                # Independently re-read the local unpaired word from its
                # diagram; this checks that the selected source case applies.
                local_ones,local_twos,_ = pairing(pair,side)
                letters = sorted([(x,'1') for x in local_ones]+
                                 [(x,'2') for x in local_twos])
                assert ''.join(ch for _,ch in letters) == local_word
                before = list(cols)
                prefix = list(cols[:i])
                if local_word == '11':
                    prefix = raise_prefix(prefix,side)
                    if prefix is None:
                        history.append({'before':before,'pair_start':i+1,
                            'rule':'contextual '+('V' if side==0 else 'W')+':11',
                            'result':'0: no preceding unpaired two'})
                        return None,s.Integer(0),history
                cols = prefix + list(replacement) + cols[i+2:]
                scalar *= -1/p
                history.append({'before':before,'pair_start':i+1,
                    'rule':'contextual '+('V' if side==0 else 'W')+':'+local_word,
                    'after':list(cols),'factor':'-1/[2]'})
                changed = True
                break
            if pair in INTEGRAL:
                factor,replacement,rule = INTEGRAL[pair]
                before = list(cols)
                cols[i:i+2] = replacement
                scalar *= factor
                history.append({'before':before,'pair_start':i+1,
                                'rule':rule,'after':list(cols),'factor':factor})
                changed = True
                break
        if not changed:
            return cols,s.cancel(scalar),history
    raise AssertionError('finite rewriting did not terminate')

def fv_terms(cols,scale):
    lowering = {'123':'134','124':'234','12':'32','1':'3'}
    initial_ones = pairing(cols,0)[0]
    result = []
    for j,(c,i) in enumerate(initial_ones,1):
        row = {'j':j,'word_position':[c+1,i+1]}
        if cols[c] == '12' and i == 0:
            row.update({'raw':None,'reduced':None,'scalar':'0',
                        'reason':'extra internal V arc','history':[]})
        else:
            raw = list(cols)
            raw[c] = lowering[raw[c]]
            reduced,scalar,history = reduce_columns(raw,scale)
            row.update({'raw':raw,'reduced':reduced,'scalar':str(scalar),
                        'history':history})
            if reduced:
                row['invariant_record'] = invariant_record(reduced)
                row['V_unpaired_twos'] = len(pairing(reduced,0)[1])
        result.append(row)
    assert len(result) == len(initial_ones)
    return result

states = {name:(columns[name],s.Integer(1) if name in ('T','T1') else -1/p)
          for name in ('T','T1','T2','Q')}
Rcols = columns['T'][:-1]+['3']
states['R'] = (Rcols,s.Integer(1))
path_tables = {name:fv_terms(*states[name]) for name in ('T','T1','T2','R')}
assert [len(path_tables[name]) for name in ('T','T1','T2','R')] == [9,7,7,8]

def coefficient(table,target):
    target_cols,target_scale = states[target]
    out = 0
    hits = []
    for row in table:
        if row['reduced'] == target_cols:
            out += qi(row['j'])*s.sympify(row['scalar'],locals={'q':q})/target_scale
            hits.append(row['j'])
    return s.expand(out),hits

for source,target,value,hits in [
    ('T','T1',alpha,[3,7]), ('T','T2',beta,[8]),
    ('T1','Q',gamma,[6]), ('T2','Q',delta,[3]), ('R','Q',0,[])]:
    actual,indices = coefficient(path_tables[source],target)
    assert zero(actual-value) and indices == hits, (source,target,actual,indices)

# Exhaustion is stronger than matching the four coefficients. Every first
# term is zero, one of the two intermediates, the one i3>0 term, or R.
for row in path_tables['T']:
    cols = row['reduced']
    assert cols is None or cols in (columns['T1'],columns['T2'],Rcols) or row['invariant_record'][1] > 0
# Every unwanted second term differs from Q by its persistent invariant
# record or by the honest-class diagram statistic epsilon_V. The proof
# justifies honesty of the crystal terms and persistence of invariants.
for name in ('T1','T2','R'):
    for row in path_tables[name]:
        cols = row['reduced']
        if cols is None or cols == columns['Q']:
            continue
        record = row['invariant_record']
        assert record[1] > 0 or record[2] > 0 or record[3] != 1 or row['V_unpaired_twos'] > 0, (name,row)
assert invariant_record(columns['Q']) == [0,0,0,1]
assert len(pairing(columns['Q'],0)[1]) == 0

# Full integral algebra, with no inversion of [2], [3], [7], or q-1.
a_star,b_star = q**5+q**-5,q**6+q**2+q**-2+q**-6
u_star = q**5*(-q**10+q**8+2*q**6+2*q**4+q**2+3)/4
v_star = q**6*(q**8-q**6-3*q**4-q**2+1)/4
z = q**3+q**-3
assert zero(alpha-p*a_star) and zero(beta-p*b_star)
assert zero(u_star*a_star+v_star*b_star-1)
x = q**2
a_poly,b_poly = q**5*a_star,q**6*b_star
assert zero((x**4+x**3+x**2+x+1)*a_poly-x**2*(x+1)*b_poly-(x+1))
assert zero(a_poly.subs(q,s.I)) and b_poly.subs(q,s.I) == 4
middle_change = s.Matrix([[a_star,-v_star],[b_star,u_star]])
middle_inverse = s.Matrix([[u_star,v_star],[-b_star,a_star]])
assert all(zero(x) for x in middle_change*middle_inverse-s.eye(2))
assert zero(z*a_star-b_star-r**2*qi(7))
assert zero(gamma/p-qi(3)*(q**2-1+q**-2))
raw_inclusion = s.diag(1,1,-p,-p)
raw_N = raw_inclusion.inv()*N*raw_inclusion
expected_raw_N = s.Matrix([[0,0,0,0],[alpha,0,0,0],[-b_star,0,0,0],
                          [0,-qi(3)*(q**2-1+q**-2),delta,0]])
assert all(zero(x) for x in raw_N-expected_raw_N)
assert zero(C.subs(q,s.I)+4)
h = qi(7)*qi(3)
node = s.diag(1,1,1,r**2)
factor = s.diag(1,1,1,h)
stabilized_endpoint = s.diag(1,1,1,C)
assert all(zero(x) for x in node*factor-stabilized_endpoint)
assert h.subs(q,1) == 21 and qi(3).subs(q,1) == 3
assert zero((q**9*q**-4-q**5)*C)
assert s.expand(qi(9)+2*qi(7)+qi(5)).coeff(q,8) == 1

parser = argparse.ArgumentParser()
parser.add_argument('--refresh-source-receipts',action='store_true',
                    help='Read the retained primary-source shelf and refresh its hashed extracts.')
args = parser.parse_args()
if args.refresh_source_receipts:
    source_bytes = SOURCE.read_bytes()
    source_text = source_bytes.decode('utf-8')
    assert r'\columnL{1\\2\\4} \columnL{2\\3}' in source_text
    assert r'\column{1 \\ 2 \\ 4}\column{1 \\ 3}' in source_text
    loci = [(1493,1498),(2430,2458),(2508,2518),(2555,2565),(4619,4636),
            (4875,4908),(4934,4954),(5050,5067),(5078,5150),(5200,5251),
            (5344,5368),(5461,5492),(5755,5784),(5878,5908),(5960,5980),
            (6398,6416),(7086,7105),(7130,7169),(7183,7230),(7327,7350)]
    lines = source_text.splitlines()
    receipt = {'primary_source':str(SOURCE),
        'sha256':hashlib.sha256(source_bytes).hexdigest(),
        'primary_url':'https://arxiv.org/abs/cs/0703110v4',
        'author_pdf_url':'https://websites.umich.edu/~jblasiak/Apr13KroneckerGCT4.pdf',
        'read_loci':[{'first_line':a,'last_line':b,
            'sha256':hashlib.sha256(('\n'.join(lines[a-1:b])+'\n').encode()).hexdigest()}
            for a,b in loci]}
    (ROOT/'source_receipts.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
    (ROOT/'source_loci.txt').write_text('\n\n'.join(
        '\n'.join(f'{i+1}: {lines[i]}' for i in range(a-1,b)) for a,b in loci)+'\n',encoding='utf-8')
certificate = {
    'scope':'Finite contextual rewrite enumeration of all two-step paths; literal weights; Laurent, integral matrix and specialization checks. Source hypotheses and stable subquotient proof are articulated in both TeX files.',
    'shape_column_counts':[0,3,2,2], 'shape_row_lengths':[7,5,3],
    'basis_columns':columns,'basis_rescalings':rescalings,'weights':weights,
    'diagrams':{name:{'V':unpaired(cols,0),'W':unpaired(cols,1)} for name,cols in columns.items()},
    'printed_target_FV2_coefficient':'0 by W-weight obstruction',
    'N':[[str(x) for x in row] for row in N.tolist()],
    'divided_square':[[str(x) for x in row] for row in D.tolist()],
    'specialization_N':N0.tolist(),'generic_jordan_partition':[3,1],
    'specialized_rational_jordan_partition':[2,2],
    'kernel_F_basis':[list(map(str,k)),['0','0','0','1']],
    'C_second_jet':84,'C_second_derivative':168,
    'source_read_required':False,
    'contextual_path_tables':path_tables,
    'path_exhaustion_counts':{'T':9,'T1':7,'T2':7,'R':8},
    'cokernel_over_Z_half_Laurent':'R^2 + R/([2]) + R/([3])',
    'original_integral_ideal':'(a_*,b_*) = (4,q^2+1) = (4,[2])',
    'original_integral_middle_exact_sequence':'0 -> A/([2]) -> A^2/([2] A(a_*,b_*)) -> (4,[2]) -> 0',
    'specialized_cokernel_over_Z':'Z^2 + Z/(4) + Z/(3)',
    'specialized_cokernel_over_Z_half':'O^2 + O/(3)',
    'raw_lattice_inclusion_diagonal':['1','1','-[2]','-[2]'],
    'endpoint_map':'top quotient tensor V-weight(-2,2) -> bottom; scalar C',
    'node_factorization':'diag(1,1,1,C) = diag(1,1,1,r^2) diag(1,1,1,[7][3])',
    'specialized_kernel_comparison_factor':21,
    'full_quantum_extension_trace_obstruction':'[9]+2[7]+[5] is nonzero',
    'all_exact_algebra_checks_passed':True,
}
(ROOT/'generator_certificate.json').write_text(json.dumps(certificate,indent=2,default=str)+'\n',encoding='utf-8')
print(json.dumps({'passed':True,'literal_target_coefficient':0,'second_jet':84,
                  'source_receipts_refreshed':args.refresh_source_receipts,
                  'enumerated_path_terms':sum(map(len,path_tables.values()))}))
