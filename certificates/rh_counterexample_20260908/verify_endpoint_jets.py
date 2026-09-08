"""Exact retained-b endpoint and compact-test algebra; default read-only."""
from pathlib import Path
import hashlib
import json
import sys
from resource_ceiling import install_memory_ceiling

RESOURCE = install_memory_ceiling()
import sympy as S


def checks():
    rows = []
    def check(name, value):
        vv = list(value) if isinstance(value, S.MatrixBase) else [value]
        assert all(S.cancel(v) == 0 for v in vv), (name, vv)
        rows.append({'id': name, 'status': 'pass', 'method': 'exact_rational_identity'})
    x,y,w,e,B,z = S.symbols('x y w eta beta z')
    q=S.Matrix([x,y,w]); v=1+x*y
    F=S.Matrix([v**3*w+y*y*v*(1+3*v),
                y+3*x*v*v*w+3*x*y*y*(4+3*x*y),2*x-3*x*x*y-x**3*w])
    J=F.jacobian(q); sq=F[0]/2
    H={x:-1/(2*e),y:B+3*e,w:26*e*e+6*B*e}
    check('original_det',J.det()+2)
    check('full_all_b_fibre',F.subs(H)-S.Matrix([B*B-e*e,4*B,0]))
    grad=S.Matrix([S.diff(sq,t) for t in q])
    g=S.Matrix([(B+3*e)*(3*B**3+17*B*B*e+9*B*e*e+3*e**3)/(4*e),
                 (3*B**3+9*B*B*e+17*B*e*e+3*e**3)/(8*e*e),
                 -(B+e)**3/(16*e**3)])
    L=9*B*B/(4*e*e)+9*B/(2*e)+S.Rational(13,4)-6*B**4-66*B**3*e-246*B*B*e*e-342*B*e**3-108*e**4
    N=S.expand(g.dot(g))
    check('all_gradient_entries',grad.subs(H)-g)
    check('full_laplacian',sum(S.diff(sq,t,2) for t in q).subs(H)-L)
    check('gradient_leading',S.Matrix([S.limit(e**3*t,e,0) for t in g])-S.Matrix([0,0,-B**3/16]))
    check('squared_gradient_leading',S.limit(e**6*N,e,0)-B**6/256)
    check('laplacian_leading',S.limit(e*e*L,e,0)-9*B*B/4)
    check('b_zero_gradient',g.subs({B:0,e:-z/2})-S.Matrix([-9*z**3/32,-3*z/16,-S.Rational(1,16)]))
    check('b_zero_laplacian',L.subs({B:0,e:-z/2})-(13-27*z**4)/4)
    # Independently differentiate original-coordinate polynomial test functions.
    for k in range(1,5):
        f=sq**k
        lap=sum(S.diff(f,t,2) for t in q).subs(H)
        target=(B*B-e*e)/2
        rhs=k*target**(k-1)*L
        if k>1: rhs+=k*(k-1)*target**(k-2)*N
        check('full_chain_rule_degree_'+str(k),lap-rhs)
    h=S.symbols('h'); aa=S.symbols('a0:7')
    f=sum(aa[j]*h**j for j in range(7))
    lap=S.expand(N*S.diff(f,h,2).subs(h,-e*e/2)+L*S.diff(f,h).subs(h,-e*e/2))
    check('pole_minus6',lap.coeff(e,-6)-aa[2]*B**6/128)
    check('pole_minus5',lap.coeff(e,-5)-3*aa[2]*B**5/64)
    check('pole_minus4_after_a2',lap.coeff(e,-4).subs(aa[2],0)+3*aa[3]*B**6/256)
    check('pole_minus3_after_a2',lap.coeff(e,-3).subs(aa[2],0)+9*aa[3]*B**5/128)
    tail=lap.subs({aa[2]:0,aa[3]:0}).expand()
    check('pole_minus2_after_a2a3',tail.coeff(e,-2)-3*B*B*(192*aa[1]+B**4*aa[4])/256)
    check('pole_minus1_after_a2a3',tail.coeff(e,-1)-9*B*(64*aa[1]+B**4*aa[4])/128)
    # The last two simultaneous conditions have only a1=a4=0 for B != 0.
    check('last_pole_system_determinant',S.Matrix([[192,B**4],[64,B**4]]).det()-128*B**4)
    bounded=lap.subs({aa[j]:0 for j in range(1,5)}).expand()
    for k in range(-6,0): check('bounded_no_pole_'+str(k),bounded.coeff(e,k))
    check('bounded_limit',bounded.coeff(e,0)+5*B**6*aa[5]/512)
    for m in range(2,9):
        val=S.expand(N*m*(m-1)*(-e*e/2)**(m-2)+L*m*(-e*e/2)**(m-1))
        check('zero_order_leading_'+str(m),S.limit(val/e**(2*m-10),e,0)-B**6*m*(m-1)*(-S.Rational(1,2))**(m-2)/256)
    orbit={x:1/z,y:-3*z/2,w:13*z*z/2}
    Jg=J.subs(orbit); J0=Jg.subs(z,1)
    Bt=S.eye(3); Bt[1,2]=3*(1-z*z)/4
    C=J0.inv()*Bt.inv()*Jg
    p1,p2,p3,lam,mu,kap=S.symbols('ell1 ell2 ell3 lam mu kap')
    ell=S.Matrix([p1,p2,p3])
    coords={lam:(2*p1+3*p2-18*p3)/8,mu:p2-3*p3,kap:p3-(2*p1+3*p2-18*p3)/8}
    inv=S.Matrix([(17*lam-3*mu+9*kap)/2,3*lam+mu+3*kap,lam+kap])
    check('covector_coordinate_inverse',inv.subs(coords)-ell)
    out=S.Matrix([17*lam/2-3*mu*z*z/2+9*kap*z**3/2,3*lam/z**2+mu+3*kap*z,lam/z**3+kap])
    check('all_covector_components',C.T*inv-out)
    check('covector_leading',S.Matrix([S.limit(z**3*t,z,0) for t in out])-S.Matrix([0,0,lam]))
    check('bounded_plane_limit',S.Matrix([S.limit(t.subs(lam,0),z,0) for t in out])-S.Matrix([0,mu,kap]))
    plane=out.subs(lam,0)
    check('bounded_plane_energy',plane.dot(plane)-(S.Rational(9,4)*z**4*(-mu+3*kap*z)**2+(mu+3*kap*z)**2+kap*kap))
    ds0=J0.row(0).T/2
    check('arithmetic_covector_class',S.Matrix([coords[k] for k in (lam,mu,kap)]).subs(dict(zip(ell,ds0)))-S.Matrix([0,0,-S.Rational(1,16)]))
    check('arithmetic_covector_transport',C.T*ds0-Jg.row(0).T/2)
    check('e3_leading',coords[lam].subs({p1:0,p2:0,p3:1})+S.Rational(9,4))
    # Formal finite-jet inverse construction is checked for arbitrary Taylor data.
    cc=S.symbols('c0:5'); invcoeff=[1/cc[0]]
    for n in range(1,5): invcoeff.append(-sum(cc[j]*invcoeff[n-j] for j in range(1,n+1))/cc[0])
    product=S.expand(sum(cc[j]*h**j for j in range(5))*sum(invcoeff[j]*h**j for j in range(5)))
    for j in range(5): check('reciprocal_jet_'+str(j),product.coeff(h,j)-int(j==0))
    u,sig=S.symbols('u sigma'); ff=S.Function('f')(u)
    check('compact_inverse_conjugation',-S.I*S.diff(S.exp(S.I*sig*u)*ff,u)-sig*S.exp(S.I*sig*u)*ff-S.exp(S.I*sig*u)*(-S.I*S.diff(ff,u)))
    return {'schema_version':1,'status':'pass','check_count':len(rows),'checks':rows,
            'resource':RESOURCE,'scope':'Exact rational identities and finite-jet algebra. Full analytic proofs in satellite29. No RH result or Lean certification.'}


if __name__=='__main__':
    receipt=checks()
    receipt['script_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    if '--write' in sys.argv:
        Path(__file__).with_name('endpoint_jets_results.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':receipt['status'],'check_count':receipt['check_count'],'resource':RESOURCE}))
