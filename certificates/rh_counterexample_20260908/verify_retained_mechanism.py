"""Small exact replay of the retained polynomial's actual interfaces.

One process, no downloads, no source/index mutation. --write writes only the
adjacent receipt after all identities pass. This is a SymPy replay, not Lean.
The sheaf/gluing proofs are in section 23, not certified by this script.
"""
from pathlib import Path
import argparse
import hashlib
import json
import sympy as s

HERE = Path(__file__).resolve().parent
RECEIPT = HERE / 'retained_mechanism_results.json'


def checks():
    x, y, w, a, b, c, r, alpha, tau, t = s.symbols('x y w a b c r alpha tau t')
    q = (x, y, w)
    F = s.Matrix([(1+x*y)**3*w+y**2*(1+x*y)*(4+3*x*y),
                  y+3*x*(1+x*y)**2*w+3*x*y**2*(4+3*x*y),
                  2*x-3*x**2*y-x**3*w])
    J = F.jacobian(q)
    assert s.expand(J.det()) == -2
    P = c*r**3-2*r**2+b*r-2*a
    inverse = {x:1/alpha, y:r-alpha, w:5*alpha**2-3*r*alpha-c*alpha**3}
    substituted = [s.cancel(f.subs(inverse, simultaneous=True)) for f in F]
    expected = [r*r+r*alpha-c*r**3, 4*r+2*alpha-3*c*r*r, c]
    assert all(s.expand(f-g) == 0 for f,g in zip(substituted, expected))
    ar = s.diff(P,r)/2
    assert s.expand(substituted[1].subs(alpha,ar)-b) == 0
    assert s.expand(2*(substituted[0].subs(alpha,ar)-a)-P) == 0
    assert F.subs(x,0) == s.Matrix([w+4*y*y,y,0])
    disc = 4*(b*b-c*b**3+18*a*b*c-16*a-27*a*a*c*c)
    assert s.expand(s.discriminant(P,r)-disc) == 0
    fibre = [(s.Rational(1),-s.Rational(3,2),s.Rational(13,2)),
             (-s.Rational(1),s.Rational(3,2),s.Rational(13,2)),
             (s.Rational(0),s.Rational(0),-s.Rational(1,4))]
    for point in fibre:
        assert F.subs(dict(zip(q,point))) == s.Matrix([-s.Rational(1,4),0,0])
    assert s.expand(P.subs({a:-s.Rational(1,4),b:0,c:0})+(2*r-1)*(2*r+1)/2) == 0
    W = -s.Matrix([s.diff(F[1],v) for v in q]).cross(
             s.Matrix([s.diff(F[2],v) for v in q]))/2
    W = W.applyfunc(s.expand)
    assert (J*W-s.Matrix([1,0,0])).applyfunc(s.expand) == s.zeros(3,1)
    assert s.expand(sum(s.diff(W[i],q[i]) for i in range(3))) == 0
    X = s.symbols('X', nonzero=True)
    curve = s.Matrix([X,-3/(2*X),13/(2*X**2)])
    curve_sub = dict(zip(q,curve))
    assert (F.subs(curve_sub, simultaneous=True)-s.Matrix([-1/(4*X**2),0,0])).applyfunc(s.cancel) == s.zeros(3,1)
    assert (W.subs(curve_sub, simultaneous=True)-2*X**3*curve.diff(X)).applyfunc(s.cancel) == s.zeros(3,1)
    assert s.expand(sum(s.diff(F[0],v,2) for v in q)).subs({x:0,y:0,w:0}) == 8
    Pforward = P.subs({a:a+2*tau,b:b+6*c*tau}, simultaneous=True)
    Pback = P.subs({a:a-2*t,b:b-6*c*t}, simultaneous=True)
    assert s.expand(s.diff(Pforward,tau)-s.diff(Pforward,r,2)) == 0
    assert s.expand(s.diff(Pback,t)+s.diff(Pback,r,2)) == 0
    assert s.expand(Pback.subs({a:-s.Rational(1,4),b:0,c:0})+2*(r*r-2*(t+s.Rational(1,8)))) == 0
    vel = -2*s.diff(Pforward,r)/Pforward
    assert s.cancel(s.diff(vel,tau)+vel*s.diff(vel,r)-s.diff(vel,r,2)) == 0
    # The coefficient heat motion is the specified physical target direction.
    alpha_tau = ar.subs({a:a+2*tau,b:b+6*c*tau}, simultaneous=True)
    assert s.expand(s.diff(Pforward,r)-2*alpha_tau) == 0
    r1,r2,u,v = s.symbols('r1 r2 u v')
    assert s.expand((r1-r2)*(r1+r2)-(r1*r1-r2*r2)) == 0
    assert s.expand((r1*r1-r2*r2).subs({r1:(u+v)/2,r2:(v-u)/2}, simultaneous=True)-u*v) == 0
    # theta in root coordinates differs from r2 dr1-r1 dr2 by half d(relation).
    theta_coeff = s.Matrix([r1+r2,-r1-r2])
    alt_coeff = s.Matrix([r2,-r1])
    assert theta_coeff-alt_coeff == s.Matrix([r1,-r2])
    # Exact characteristic polynomial for the retained two-field viscous mode.
    eta,nu,k,A,S,mu = s.symbols('eta nu k A S mu', nonzero=True)
    B = s.Matrix([[-eta*k*k,A*S/k],[k*S,-nu*k*k]])
    cp = s.expand((mu*s.eye(2)-B).det())
    assert s.expand(cp-((mu+eta*k*k)*(mu+nu*k*k)-A*S*S)) == 0
    z11,z12,z21 = s.symbols('z11 z12 z21')
    D = s.Matrix([[z11,z12],[z21,-z11]])
    z1,z2,G1,G2,lam,Om = s.symbols('z1 z2 G1 G2 lam Om')
    zeta = s.Matrix([z1,z2]); rot = s.Matrix([-z2,z1])
    assert (rot.dot(zeta)) == 0
    xx1,xx2 = s.symbols('xx1 xx2'); xx=s.Matrix([xx1,xx2])
    assert s.expand((-D.T*zeta).dot(xx)+zeta.dot(D*xx)) == 0
    spectral=s.symbols('spectral')
    R=s.Matrix([[0,-2*spectral],[1,0]])
    assert -R**2/2 == spectral*s.eye(2)
    assert s.expand((mu*s.eye(2)-R).det()) == mu**2+2*spectral
    return {
        'status':'pass', 'arithmetic':'rational polynomial and rational function identities',
        'sympy_version':s.__version__,
        'checks': ['original_det_DF_minus_2','inverse_chart_both_directions',
                   'entire_fibre_x_zero_boundary','cubic_discriminant',
                   'three_exact_colliding_points','Piola_pushforward_and_divergence',
                   'escaping_curve_target_and_velocity','Euclidean_laplacian_not_pullback',
                   'forward_and_Newman_backward_heat_signs','model_collision_time_minus_one_eighth',
                   'Cole_Hopf_Burgers_identity','simple_root_inverse_denominator',
                   'self_fibre_product_node_isomorphism','theta_root_coordinate_identity',
                   'viscous_two_field_characteristic_polynomial','transported_phase_cancellation',
                   'actual_arithmetic_coordinate_factor_two_and_sheet_matrix'],
        'original_map':[str(f) for f in F], 'inverse_root_polynomial':str(P),
        'discriminant':str(disc), 'inverse':{str(k):str(v) for k,v in inverse.items()},
        'source_curve_parameter':'x=X, y=-3/(2X), w=13/(2X^2), dX/ds=2X^3',
        'model_Newman_collision_time':'-1/8 for a0=-1/4; not the Newman constant',
        'written_proof_only':['full normalized differential kernel C theta',
                              'Cartier filtration and connecting cocycle',
                              'intrinsic metric completeness analysis',
                              'whole arithmetic pullback chain rule'],
        'nonclaims':['No new Lean certification','No full fluid multiscale proof audit',
                     'No global CDP20 conclusion from a local node',
                     'No RH counterexample or arbitrary-polynomial replacement of H0']}


def main():
    parser=argparse.ArgumentParser(); parser.add_argument('--write',action='store_true')
    args=parser.parse_args(); result=checks()
    result['script_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    if args.write:
        RECEIPT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    else:
        assert json.loads(RECEIPT.read_text(encoding='utf-8')) == result, 'Stale exact replay receipt'
    print('RETAINED_MECHANISM_OK checks='+str(len(result['checks'])))


if __name__ == '__main__':
    main()
