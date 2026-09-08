#!/usr/bin/env python3
"""Exact verification of retained binary cubic invariant transport.

Run: python check_invariant_transport.py
Writes verification_receipt.json beside this script. No numerical sampling,
external services, numerical specialization of the input coefficients, or Lean are used.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import platform
import sympy as sp

HERE = Path(__file__).resolve().parent
checks = []

def zero(label, expression, variables=None):
    expression = sp.expand(expression)
    if variables is not None:
        assert sp.Poly(expression, *variables).is_zero, (label, expression)
    else:
        assert expression == 0, (label, expression)
    checks.append({"name": label, "status": "passed", "exact_remainder": "0"})

def matrix_json(matrix):
    return [[str(matrix[i, j]) for j in range(matrix.cols)] for i in range(matrix.rows)]

R, T, U, V = sp.symbols('R T U V')
A, B, C, D = sp.symbols('A B C D')
a, b, c = sp.symbols('a b c')
p, q, r, s = sp.symbols('p q r s')
x, y, z, w = sp.symbols('x y z w')
kappa = sp.symbols('kappa')
g = sp.Matrix([[p, q], [r, s]])
g2 = sp.Matrix([[x, y], [z, w]])
vector = sp.Matrix([R, T])


def cubic(vector, coefficients=(A, B, C, D)):
    vv, ww = vector
    aa, bb, cc, dd = coefficients
    return aa*vv**3 + bb*vv**2*ww + cc*vv*ww**2 + dd*ww**3


def delta(coefficients):
    aa, bb, cc, dd = coefficients
    return bb**2*cc**2 - 4*aa*cc**3 - 4*bb**3*dd - 27*aa**2*dd**2 + 18*aa*bb*cc*dd

coefficients = (
    A*p**3+B*p**2*q+C*p*q**2+D*q**3,
    3*A*p**2*r+B*(p**2*s+2*p*q*r)+C*(2*p*q*s+q**2*r)+3*D*q**2*s,
    3*A*p*r**2+B*(2*p*r*s+q*r**2)+C*(p*s**2+2*q*r*s)+3*D*q*s**2,
    A*r**3+B*r**2*s+C*r*s**2+D*s**3,
)
zero('transpose_action_coefficient_formula', cubic(g.T*vector)-cubic(vector, coefficients))
zero('left_action_composition', cubic(g2.T*g.T*vector)-cubic((g*g2).T*vector))
zero('discriminant_relative_invariant_weight_6', delta(coefficients)-(p*s-q*r)**6*delta((A,B,C,D)))
retained_delta = 4*(b**2-c*b**3+18*a*b*c-16*a-27*a**2*c**2)
zero('retained_coefficients_discriminant', delta((c,-2,b,-2*a))-retained_delta)

# Homogeneous discriminant checked by an independent root-product identity.
e1, e2, e3 = sp.symbols('e1 e2 e3')
root_polynomial = sp.Poly(A*(R-e1)*(R-e2)*(R-e3), R)
zero('root_product_discriminant_identity', delta(root_polynomial.all_coeffs())-A**4*(e1-e2)**2*(e1-e3)**2*(e2-e3)**2)

M = sp.Matrix([[1, sp.Rational(1,2)], [0,1]])
M_inverse = sp.Matrix([[1, -sp.Rational(1,2)], [0,1]])
assert M*M_inverse == sp.eye(2) and M_inverse*M == sp.eye(2)
checks.append({"name": "explicit_M_inverse", "status": "passed", "matrix_product": matrix_json(sp.eye(2))})
q0 = -2*R**2*T+sp.Rational(1,2)*T**3

def h(vector):
    uu, vv = vector
    return uu*vv*(uu-vv)

zero('q0_exact_factorization', q0+2*h(M*vector))
zero('q0_discriminant', delta((0,-2,0,sp.Rational(1,2)))-16)

D_matrices = [
    sp.eye(2),
    sp.Matrix([[-1,1],[0,1]]),
    sp.Matrix([[0,1],[1,0]]),
    sp.Matrix([[1,0],[1,-1]]),
    sp.Matrix([[0,1],[-1,1]]),
    sp.Matrix([[1,-1],[1,0]]),
]
root_vectors = [sp.Matrix([0,1]), sp.Matrix([1,0]), sp.Matrix([1,1])]
root_names = ['0','infinity','1']
expected_multipliers = [1,1,-1,1,-1,-1]
stabilizers = []
for index, (dd, multiplier) in enumerate(zip(D_matrices,expected_multipliers),1):
    zero(f'D_{index}_multiplier',h(dd*sp.Matrix([U,V]))-multiplier*h(sp.Matrix([U,V])))
    permutations = []
    for root in root_vectors:
        image = dd*root
        candidates = [j for j, target in enumerate(root_vectors)
                      if sp.det(sp.Matrix.hstack(image,target)) == 0]
        assert len(candidates)==1
        permutations.append(root_names[candidates[0]])
    base = M_inverse*dd*M
    transposed_g = kappa*base
    transformed = -2*h(M*transposed_g*vector)
    remainder = sp.rem(sp.Poly(sp.expand(transformed-q0),kappa),sp.Poly(multiplier*kappa**3-1,kappa)).as_expr()
    zero(f'D_{index}_stabilizer_mod_cubic',remainder)
    # The three kappa values are distinct in characteristic zero.
    assert sp.gcd(sp.Poly(multiplier*kappa**3-1,kappa),sp.Poly(3*multiplier*kappa**2,kappa)).degree()==0
    stabilizers.append({
        'index':index,'D':matrix_json(dd),'det_D':str(dd.det()),
        'multiplier':multiplier,'permutation_of_0_infinity_1':permutations,
        'base_g_transpose':matrix_json(base),
        'kappa_equation':str(multiplier*kappa**3-1)+' = 0',
        'number_of_distinct_kappa_over_algebraically_closed_char_zero':3,
        'g_transpose_formula':'kappa * base_g_transpose',
    })
# The six projective permutations are distinct, hence all 18 matrices are distinct.
assert len({tuple(item['permutation_of_0_infinity_1']) for item in stabilizers})==6
checks.append({'name':'six_distinct_projective_permutations_and_18_geometric_stabilizers','status':'passed'})

H = sp.diag(1,-1)
adjugate_g = sp.Matrix([[s,-q],[-r,p]])
adjoint_numerator = sp.Matrix([[p*s+q*r,-2*p*q],[2*r*s,-p*s-q*r]])
assert g*H*adjugate_g == adjoint_numerator
checks.append({'name':'adjoint_H_exact_numerator','status':'passed','numerator':matrix_json(adjoint_numerator),'denominator':'p*s-q*r','excluded_locus':'p*s-q*r = 0'})
zero('adjoint_H_trace_zero',sp.trace(adjoint_numerator))
assert (adjoint_numerator*adjoint_numerator - (p*s-q*r)**2*sp.eye(2)).applyfunc(sp.expand) == sp.zeros(2)
checks.append({'name':'adjoint_H_square_identity','status':'passed'})

# Kahler differentials of k[u,v]/(uv): encode du,dv as linear formal variables.
u,v,du,dv = sp.symbols('u v du dv')
theta = v*du
relation = v*du+u*dv
swapped_theta = u*dv
zero('node_swap_theta_sign_mod_d_uv',swapped_theta+theta-relation)
zero('node_u_annihilates_theta_mod_uv',u*theta-(u*v)*du)
zero('node_v_annihilates_theta_mod_uv_and_d_uv',v*theta-v*relation+(u*v)*dv)
# Degree-one module basis (u du, v du, u dv, v dv), relation vector (0,1,1,0).
relation_vector = sp.Matrix([0,1,1,0])
theta_vector = sp.Matrix([0,1,0,0])
assert sp.Matrix.hstack(relation_vector,theta_vector).rank()==2
checks.append({'name':'node_theta_nonzero_in_degree_one_quotient','status':'passed','relation_vector':list(relation_vector),'theta_vector':list(theta_vector),'joint_rank':2})

record = {
    'status':'passed',
    'checked_at_utc':datetime.now(timezone.utc).isoformat(),
    'python_version':platform.python_version(),
    'sympy_version':sp.__version__,
    'coefficient_ring':'Q[A,B,C,D,a,b,c,p,q,r,s,x,y,z,w,e1,e2,e3]',
    'field_scope':'Polynomial identities hold after base change; the claim of exactly 18 stabilizer matrices is over an algebraically closed field of characteristic zero. Rational points are a different count.',
    'retained_cubic':'c*R**3-2*R**2*T+b*R*T**2-2*a*T**3',
    'action':'(g.f)(z)=f(g.T*z)',
    'discriminant':str(retained_delta),
    'coefficient_action':[str(value) for value in coefficients],
    'stabilizers':stabilizers,
    'checks':checks,
    'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'raw_directives_sha256':hashlib.sha256((HERE/'raw_directives.md').read_bytes()).hexdigest(),
}
(HERE/'verification_receipt.json').write_text(json.dumps(record,indent=2,default=int)+'\n',encoding='utf-8')
print(json.dumps({'status':record['status'],'checks':len(checks),'stabilizer_multipliers':expected_multipliers,'receipt':str(HERE/'verification_receipt.json')},indent=2))
for item in stabilizers:
    print('D_'+str(item['index']), 'multiplier',item['multiplier'],'g^T/kappa =',item['base_g_transpose'])


