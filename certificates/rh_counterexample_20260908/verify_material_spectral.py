"""Exact source-generator / arithmetic-coordinate checks, one worker.

Default: read-only replay. --write: bind the deterministic result to this script.
Full analytical proofs are in satellite 27; finite checks are not Lean proofs.
"""
from pathlib import Path
import hashlib
import json
import sys
from resource_ceiling import install_memory_ceiling

RESOURCE = install_memory_ceiling()
import sympy as S


def checks():
    out = []
    def check(name, value):
        entries = list(value) if isinstance(value, S.MatrixBase) else [value]
        assert all(S.cancel(v) == 0 for v in entries), (name, entries)
        out.append({'id': name, 'status': 'pass', 'method': 'exact_symbolic'})
    x,y,w,z,s,b,c,r,t,u = S.symbols('x y w z s b c r t u')
    q = S.Matrix([x,y,w])
    F = S.Matrix([(1+x*y)**3*w+y*y*(1+x*y)*(4+3*x*y),
                  y+3*x*(1+x*y)**2*w+3*x*y*y*(4+3*x*y),
                  2*x-3*x*x*y-x**3*w])
    J = F.jacobian(q)
    check('source_det_minus_two', J.det()+2)
    # Exact cofactor construction avoids numerical matrix inversion.
    W1 = -J.row(1).T.cross(J.row(2).T)/2
    W2 = -J.row(2).T.cross(J.row(0).T)/2
    U = W1*2+W2*6*F[2]
    check('actual_pushforward', J*U-S.Matrix([2,6*F[2],0]))
    check('actual_divergence', sum(S.diff(U[i],q[i]) for i in range(3)))
    sq = F[0]/2
    check('spectral_slice_section', sq.subs({x:0,y:0,w:2*s})-s)
    check('material_arithmetic_coordinate', (J.row(0)*U)[0]/2-1)
    check('retained_first_integral', (J.row(1)*U)[0]-3*((J.row(0)*U)[0]*F[2]+F[0]*(J.row(2)*U)[0]))
    orbit = {x:1/z,y:-3*z/2,w:13*z*z/2}
    check('orbit_target', F.subs(orbit)-S.Matrix([-z*z/4,0,0]))
    grad = S.Matrix([S.diff(sq,v) for v in q])
    check('orbit_gradient', grad.subs(orbit)-S.Matrix([-9*z**3/32,-3*z/16,-S.Rational(1,16)]))
    check('orbit_laplacian', sum(S.diff(sq,v,2) for v in q).subs(orbit)-(13-27*z**4)/4)
    check('orbit_gradient_square', grad.dot(grad).subs(orbit)-(81*z**6+36*z*z+4)/1024)
    # Chain rule evaluated with independent formal values for f' and f''.
    for k in range(1,5):
        value = sq**k
        lap = sum(S.diff(value,v,2) for v in q)
        rhs = k*sq**(k-1)*sum(S.diff(sq,v,2) for v in q)
        if k>=2:
            rhs += k*(k-1)*sq**(k-2)*grad.dot(grad)
        check('euclidean_chain_rule_degree_'+str(k),lap-rhs)
    P = c*r**3-2*r*r+b*r-4*s
    check('full_material_cover_lift', S.diff(P,r)*(4-6*c*r)/S.diff(P,r)+S.diff(P,b)*6*c+S.diff(P,s))
    delta = b*b-32*s
    R = S.Matrix([[0,-2*s],[1,b/2]])
    A = S.Matrix([[0,4*b/delta],[0,-16/delta]])
    check('all_b_root_relation', R*R-b*R/2+2*s*S.eye(2))
    check('all_b_connection_commutator', S.diff(R,s)+A*R-R*A-4*(b*S.eye(2)-4*R)/delta)
    check('all_b_connection_square', S.diff(A,s)+A*A-16*A/delta)
    invol = S.Matrix([[1,b/2],[0,-1]])
    check('retained_involution_square', invol*invol-S.eye(2))
    check('retained_involution_root', invol*R*invol-b*S.eye(2)/2+R)
    check('trace_kernel', (S.Matrix([[2,b/2]])*S.Matrix([-b/4,1]))[0])
    eta = S.symbols('eta')
    sr = b*r/4-r*r/2
    check('shifted_branch', sr.subs(r,eta+b/4)-b*b/32+eta*eta/2)
    alpha = -2*eta
    H = S.Matrix([1/alpha,eta+b/4-alpha,5*alpha*alpha-3*(eta+b/4)*alpha])
    check('shifted_inverse', H-S.Matrix([-1/(2*eta),b/4+3*eta,26*eta*eta+3*b*eta/2]))
    for k in range(7):
        f = s**k
        check('all_b_scalar_derivative_'+str(k),4/(b-4*r)*S.diff(f.subs(s,sr),r)-S.diff(f,s).subs(s,sr))
    for m in range(1,7):
        center = b*b/32
        Z = (s-center)**m*(3+5*(s-center)+7*(s-center)**2)
        check('shifted_zero_multiplicity_'+str(m),Z.subs(s,center-eta*eta/2)-(-S.Rational(1,2))**m*eta**(2*m)*(3-5*eta*eta/2+7*eta**4/4))
    G = S.exp(t*u*u/4)
    f = S.Function('f')(u)
    check('full_test_generator', -S.I*S.diff(G*f,u)+S.I*t*u*G*f/2-G*(-S.I*S.diff(f,u)))
    v = S.symbols('v')
    weight = S.exp(-t*((u+v)**2+v*v)/4)
    check('weighted_correlation_derivative',S.diff(weight,t)+((u+v)**2+v*v)*weight/4)
    return {'schema_version':1,'status':'pass','checks':out,'check_count':len(out),
            'resource':RESOURCE,'scope':'Exact rational identities; full proofs in satellite 27; no RH counterexample or Lean certification.'}


if __name__ == '__main__':
    receipt = checks()
    receipt['script_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    if '--write' in sys.argv:
        Path(__file__).with_name('material_spectral_results.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':receipt['status'],'check_count':receipt['check_count'],'resource':RESOURCE}))
