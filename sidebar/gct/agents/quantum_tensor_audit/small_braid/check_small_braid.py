"""Independent exact check of the degree-three sector in quantum_tensor_symmetry.tex."""
from pathlib import Path
import hashlib
import json
import sympy as s

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
q = s.symbols('q', nonzero=True)
I = s.eye(2)
zero = s.zeros(4)
checks = 0

def eq(lhs, rhs, name):
    global checks
    assert lhs.shape == rhs.shape, name
    residual = (lhs-rhs).applyfunc(s.factor)
    assert residual == s.zeros(*lhs.shape), (name, residual)
    checks += 1

J = s.Matrix([[1,0,0,0],
              [0,(q*q-1)/(q*q+1),2*q/(q*q+1),0],
              [0,2*q/(q*q+1),(1-q*q)/(q*q+1),0],
              [0,0,0,1]])
# Reconstruct the middle block from the two explicitly specified strings.
strings = s.Matrix([[1,q],[-q,1]])
eq(J[1:3,1:3], strings*s.diag(-1,1)*strings.inv(), 'J middle block from strings')
assert s.factor(strings[:,[1,0]].det()) == -(1+q*q)
checks += 1
eq(J*J,s.eye(4),'J involution')
flip = s.Matrix([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]])
eq(J.subs(q,1),flip,'J classical specialization')
E = s.Matrix([[0,1],[0,0]])
F = s.Matrix([[0,0],[1,0]])
K = s.diag(q,1/q)
dE = s.kronecker_product(E,K.inv())+s.kronecker_product(I,E)
dF = s.kronecker_product(F,I)+s.kronecker_product(K,F)
dK = s.kronecker_product(K,K)
for name,generator in [('E',dE),('F',dF),('K',dK)]:
    eq(J*generator,generator*J,'J intertwines '+name)
J12 = s.kronecker_product(J,I)
J23 = s.kronecker_product(I,J)
defect = (J12*J23*J12-J23*J12*J23).applyfunc(s.factor)
basis = s.eye(8)
displayed_defect = 2*(q*q-1)**2/(q*q+1)**3*(-basis[:,1]+q*basis[:,2])
eq(defect[:,1],displayed_defect,'displayed defect on 001')
assert defect[:,1] != s.zeros(8,1)
checks += 1
eq(defect[:,1].subs(q,1),s.zeros(8,1),'defect constant jet')
eq(defect[:,1].diff(q).subs(q,1),s.zeros(8,1),'defect first jet')
eq(defect[:,1].diff(q,2).subs(q,1)/2,-basis[:,1]+basis[:,2],
   'displayed second-order leading coefficient')

a = q-1/q
B = (a*s.eye(4)+(q+1/q)*J)/2
displayed_B = s.Matrix([[q,0,0,0],[0,a,1,0],[0,1,0,0],[0,0,0,q]])
eq(B,displayed_B,'displayed B matrix')
B = displayed_B
eq((B-q*s.eye(4))*(B+s.eye(4)/q),zero,'Hecke quadratic relation')
eq(B*(B-a*s.eye(4)),s.eye(4),'stated right inverse')
eq((B-a*s.eye(4))*B,s.eye(4),'stated left inverse')
eq(B.subs(q,1),flip,'B classical specialization')
for name,generator in [('E',dE),('F',dF),('K',dK)]:
    eq(B*generator,generator*B,'B intertwines '+name)
B12 = s.kronecker_product(B,I)
B23 = s.kronecker_product(I,B)
left = (B12*B23*B12).applyfunc(s.factor)
right = (B23*B12*B23).applyfunc(s.factor)
expected = s.zeros(8)
expected[:,0] = q**3*basis[:,0]
expected[:,7] = q**3*basis[:,7]
for i,j,k in [(1,2,4),(3,5,6)]:
    expected[:,i] = q*q*a*basis[:,i]+q*a*basis[:,j]+q*basis[:,k]
    expected[:,j] = q*a*basis[:,i]+q*basis[:,j]
    expected[:,k] = q*basis[:,i]
for i in range(8):
    eq(left[:,i],expected[:,i],f'left displayed braid column {i:03b}')
    eq(right[:,i],expected[:,i],f'right displayed braid column {i:03b}')
eq(left,right,'full eight-dimensional braid identity')
assert s.factor(a*a*q+a-q*q*a) == 0
checks += 1

source = ROOT/'tex/quantum_tensor_symmetry.tex'
source_text = source.read_text(encoding='utf-8')
assert 'In the order $r=0,r=1$, these columns have determinant $-(1+q^2)$' in source_text
assert 'It is an intertwiner for the $V$-coloured $L_1\\otimes L_1$ action' in source_text
assert 'the test is not asserted to be stable under $W$ lowering.' in source_text
checks += 3
receipt = {
    'status': 'pass',
    'scope': 'Degree-three L_1 sector, every displayed J and B matrix entry, all eight braid columns, and q-1 defect jets; no assertion about full-source extension.',
    'source': str(source.relative_to(ROOT)),
    'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
    'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'sympy_version': s.__version__,
    'exact_matrix_assertions_and_checks': checks,
    'basis_order': [f'{i:03b}' for i in range(8)],
    'J_braid_defect_matrix': [[str(defect[i,j]) for j in range(8)] for i in range(8)],
    'B_common_braid_matrix': [[str(s.factor(expected[i,j])) for j in range(8)] for i in range(8)],
    'q_minus_one_order_on_001': 2,
    'leading_coefficient_on_001': ['0','-1','1','0','0','0','0','0'],
    'discrepancies': [],
    'prose_clarification': {'status':'resolved', 'resolution':'The final fragment explicitly gives r=0,r=1 column order and correctly restricts B intertwining to the V-coloured action; the fixed W-highest slice is not claimed stable under W lowering.'},
}
(HERE/'receipt.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'pass','checks':checks,'source_sha256':receipt['source_sha256']}))
