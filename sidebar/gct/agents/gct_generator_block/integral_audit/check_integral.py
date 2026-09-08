"""Independent exact checks of the displayed GCT generator integral algebra.

The displayed Laurent polynomials are entered here independently; this script
does not import the author's checker or use its certificate as an oracle.
"""
from pathlib import Path
import hashlib
import json
import sympy as s

HERE = Path(__file__).resolve().parent
q = s.Symbol('q')

def quantum(m):
    return sum(q ** (m - 1 - 2*j) for j in range(m))

def exact(expr):
    # Collect coefficients of the entire Laurent identity, without dropping
    # factors, specializations, or exceptional parameter values from its data.
    return s.expand(expr) == 0

checks = {}
def check(name, assertion):
    checks[name] = bool(assertion)
    assert checks[name], name

p, r = q+q**-1, q-q**-1
alpha = quantum(7)-quantum(3)
beta, d, z = quantum(8), quantum(3), q**3+q**-3
gamma, delta = quantum(6), -d
C = q**10-q**4-q**-4+q**-10
h = quantum(7)*quantum(3)
astar, bstar = q**5+q**-5, q**6+q**2+q**-2+q**-6
ustar = q**5*s.Rational(1,4)*(-q**10+q**8+2*q**6+2*q**4+q**2+3)
vstar = q**6*s.Rational(1,4)*(q**8-q**6-3*q**4-q**2+1)
N = s.Matrix([[0,0,0,0],[alpha,0,0,0],[beta,0,0,0],[0,gamma,delta,0]])
D = s.zeros(4)
D[3,0] = C
e = s.eye(4)
KV = s.diag(q**9,q**7,q**7,q**5)
check('gamma_dz', exact(gamma-d*z))
check('alpha_p_astar', exact(alpha-p*astar))
check('beta_p_bstar', exact(beta-p*bstar))
check('source_path_scalar_identity', exact(gamma*alpha+delta*beta-p*C))
check('C_factorization_with_all_factors', exact(C-r**2*h))
check('za_minus_b', exact(z*astar-bstar-r**2*quantum(7)))
check('displayed_bezout_identity', exact(ustar*astar+vstar*bstar-1))
B = s.Matrix([[astar,-vstar],[bstar,ustar]])
BI = s.Matrix([[ustar,vstar],[-bstar,astar]])
check('middle_basis_and_displayed_inverse', all(exact(x) for x in B*BI-s.eye(2)))
check('N_square_pD', all(exact(x) for x in N*N-p*D))
check('N_cube_zero', all(exact(x) for x in N**3))
check('ND_DN_Dsquare_zero', all(exact(x) for M in (N*D,D*N,D*D) for x in M))
check('Cartan_conjugacy', all(exact(x) for x in KV*N-q**-2*N*KV))
k = e[:,1]+z*e[:,2]
check('kernel_generators', all(exact(x) for x in N*k))
change = s.Matrix.hstack(e[:,0],N*e[:,0],N*N*e[:,0],k)
check('generic_chain_determinant_sign', exact(change.det()+p**2*r**4*quantum(7)**2*d))
N0 = N.subs(q,1)
check('N0_literal', N0 == s.Matrix([[0,0,0,0],[4,0,0,0],[8,0,0,0],[0,6,-3,0]]))
check('N0_square_zero', N0*N0 == s.zeros(4))
check('special_chain_determinant_sign', s.Matrix.hstack(e[:,0],N0*e[:,0],e[:,2],N0*e[:,2]).det() == -12)
raw = s.diag(1,1,-p,-p)
rawN = s.Matrix([[0,0,0,0],[alpha,0,0,0],[-bstar,0,0,0],[0,-d*(q**2-1+q**-2),delta,0]])
check('raw_lattice_action_all_columns', all(exact(x) for x in N*raw-raw*rawN))
check('gamma_over_p_laurent_divisibility', exact(gamma-p*d*(q**2-1+q**-2)))
check('raw_divided_square_p_nondivisibility', s.expand(C.subs(q,s.I)) == -4 and p.subs(q,s.I) == 0)
check('jet0', C.subs(q,1) == 0)
check('jet1', s.diff(C,q).subs(q,1) == 0)
check('jet2', s.diff(C,q,2).subs(q,1) == 168)
check('h_at_1_21', h.subs(q,1) == 21)
check('ustar_vstar_at_1', ustar.subs(q,1) == 2 and vstar.subs(q,1) == -s.Rational(3,4))
V = s.diag(1,1,1,r**2)
H = s.diag(1,1,1,h)
Phi = s.diag(1,1,1,C)
check('node_factorization_orientation', all(exact(x) for x in V*H-Phi))
check('node_specialization_kernel_map21', H.subs(q,1)[3,3] == 21)
check('full_quantum_extension_trace_nonzero', exact((quantum(9)+2*quantum(7)+quantum(5)).coeff(q,8)-1))
X = q**2
apoly, bpoly = X**5+1, X**6+X**4+X**2+1
sum5 = X**4+X**3+X**2+X+1
check('A_ideal_q2plus1_bezout', exact(sum5*apoly-X**2*(X+1)*bpoly-(X+1)))
check('A_ideal_generator4', exact(4*ustar*astar+4*vstar*bstar-4))
check('A_ideal_a_containment', exact(apoly-(X+1)*(X**4-X**3+X**2-X+1)))
check('A_ideal_b_containment', exact(bpoly-(X+1)*(X**5-X**4+2*X**3-2*X**2+3*X-3)-4))
Zbasis = s.Matrix.hstack(e[:,0],e[:,1]+2*e[:,2],e[:,2],e[:,3])
check('Z_specialization_basis_is_unimodular', Zbasis.det() == 1)
check('Z_specialization_image_in_integral_basis', Zbasis.inv()*N0 == s.Matrix([[0,0,0,0],[4,0,0,0],[0,0,0,0],[0,6,-3,0]]))

result = {
    'status': 'passed',
    'method': 'independent exact SymPy Laurent coefficient arithmetic',
    'checks': checks,
    'check_count': len(checks),
    'target_sha256_at_run': hashlib.sha256((HERE.parent/'generator_block.tex').read_bytes()).hexdigest(),
    'limits': ['No source-arrow exhaustiveness audit; assigned separately.', 'Module exactness is proved in audit.md; polynomial tests do not replace those proofs.'],
}
(HERE/'certificate.json').write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
print(json.dumps({'status':'passed','checks':len(checks)}, sort_keys=True))
