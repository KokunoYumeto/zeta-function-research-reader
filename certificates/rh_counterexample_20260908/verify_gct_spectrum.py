"""Exact GCT/arithmetic map checks. Default read-only; --write binds receipt.

Finite identities supplement the full topological/analytic proofs in satellite28.
No floating point, tabulated zeros, endpoint assumption, or Lean claim.
"""
from pathlib import Path
import hashlib
import json
import sys
from resource_ceiling import install_memory_ceiling
RESOURCE = install_memory_ceiling()
import sympy as sp


def checks():
    rows = []
    def check(name, value):
        entries = list(value) if isinstance(value, sp.MatrixBase) else [value]
        assert all(sp.cancel(v) == 0 for v in entries), (name, entries)
        rows.append({'id': name, 'status': 'pass', 'method': 'exact_symbolic'})
    q,s,l,r,p,t = sp.symbols('q s lambda r p tau')
    eye = sp.eye(4)
    sq = 1-(q*q+q**-2)/2
    rq,pq = q-q**-1,q+q**-1
    check('conic_relation',pq*pq-rq*rq-4)
    check('conic_inverse_q',(pq+rq)/2-q)
    check('conic_inverse_qinv',(pq-rq)/2-q**-1)
    check('original_a',-rq*rq-2*sq)
    check('monic_quartic',q**4+(2*sq-2)*q*q+1)
    check('r_basis_conversion',rq-q**3-(2*sq-1)*q)
    check('p_basis_conversion',pq+q**3-(3-2*sq)*q)
    check('rp_basis_conversion',rq*pq-2*q*q-2*sq+2)
    K=sp.Matrix([[0,0,0,-1],[1,0,0,0],[0,1,0,2-2*s],[0,0,1,0]])
    Ki=-K**3+(2-2*s)*K
    check('matrix_quartic',K**4+(2*s-2)*K**2+eye)
    check('matrix_inverse_left',Ki*K-eye)
    check('matrix_inverse_right',K*Ki-eye)
    check('matrix_root_coordinate',(K-Ki)**2+2*s*eye)
    check('matrix_trace_coordinate',(K+Ki)**2-(4-2*s)*eye)
    sl=1-(l*l+l**-2)/2
    E=sp.Matrix([-l**-1,-l**-2,l,1])
    L=sp.Matrix([[l**-2,l**-1,1,l]])
    H=sp.Matrix([[-l**-1,0,0,0],[-l**-2,-l**-1,0,0],
                 [0,0,0,1],[0,0,0,0]])
    J=sp.Matrix([0,0,1,0]); P=sp.Matrix([[0,0,0,1]])
    B=K-l*eye
    check('resolvent_BE',B*E+2*J*(s-sl))
    check('resolvent_BH',B*H-eye+J*L)
    check('resolvent_PE',P*E-sp.ones(1))
    Inv=H-E*L/(2*(s-sl))
    check('resolvent_inverse_left',Inv*B-eye)
    check('resolvent_inverse_right',B*Inv-eye)
    check('resolvent_reverse_inverse',(P*Inv*(-2*J))[0]-1/(s-sl))
    check('fibre_polynomial',B.det()-(l**4+(2*s-2)*l*l+1))
    for branch,base in ((1,0),(-1,0),(sp.I,2),(-sp.I,2)):
        bb=B.subs({l:branch,s:base})
        ee=E.subs(l,branch); ep=sp.diff(E,l).subs(l,branch)
        check('branch_eigen_'+str(branch),bb*ee)
        check('branch_Jordan_'+str(branch),bb*ep-ee)
        check('branch_second_derivative_'+str(branch),sp.diff(sq,q,2).subs(q,branch)+4)
    check('real_axis_image',sq+rq*rq/2)
    z=sp.symbols('z',real=True,nonzero=True)
    check('imaginary_axis_image',sq.subs(q,sp.I*z)-(z+1/z)**2/2)
    def quantum(j): return sum(q**(j-1-2*k) for k in range(j))
    C=q**10-q**4-q**-4+q**-10
    check('source_divided_power_n3_3_n2_2',quantum(6)*(quantum(7)-quantum(3))-quantum(3)*quantum(8)-quantum(2)*C)
    check('source_positive_residual',C-rq*rq*quantum(7)*quantum(3))
    check('quantum_7_polynomial',quantum(7)-pq**6+5*pq**4-6*pq**2+1)
    check('quantum_3_polynomial',quantum(3)-pq**2+1)
    cs=-2*s*(7-28*s+28*s*s-8*s**3)*(3-2*s)
    check('arithmetic_coefficient',C-cs.subs(s,sq))
    ck=K**10-K**4-Ki**4+Ki**10
    check('operator_coefficient',ck-cs*eye)
    check('coefficient_second_jet',sp.diff(C,q,2).subs(q,1)/2-84)
    check('circle_exact_coefficient',cs.subs(s,sp.Rational(1,4))+sp.Rational(65,32))
    check('ramified_imaginary_coefficient',cs.subs(s,2)+4)
    check('trace_coefficient',ck.trace()-4*cs)
    A=sp.diag(0,1/(2*s),1/(2*(s-2)),1/(2*s)+1/(2*(s-2)))
    V=sp.diag(0,-1/(4*s*s),-1/(4*(s-2)**2),-1/(s*s*(s-2)**2))
    check('four_sector_heat_lower_order',sp.diff(A,s)+A*A-V)
    def Dq(f): return -q/(rq*pq)*sp.diff(f,q)
    check('lifted_material_s',Dq(sq)-1)
    check('lifted_material_r',Dq(rq)+1/rq)
    check('lifted_material_p',Dq(pq)+1/pq)
    check('lifted_material_original_x',Dq(-1/(2*rq))+1/(2*rq**3))
    check('lifted_material_original_y',Dq(3*rq)+3/rq)
    check('lifted_material_original_w',Dq(26*rq**2)+52)
    check('lifted_material_source_C',Dq(C)-sp.diff(cs,s).subs(s,sq))
    basis=[1,rq,pq,rq*pq]
    for i,e in enumerate(basis):
        for k in range(4):
            f=s**k
            rhs=sp.diff(f,s,2)+2*A[i,i]*sp.diff(f,s)+V[i,i]*f
            check('full_heat_sector_'+str(i)+'_degree_'+str(k),
                  Dq(Dq(e*f.subs(s,sq)))-e*rhs.subs(s,sq))
    poly=sp.Poly(7-28*s+28*s*s-8*s**3,s)
    boxes=[(sp.Rational(3,8),sp.Rational(2,5)),(sp.Rational(6,5),sp.Rational(5,4)),
           (sp.Rational(19,10),sp.Rational(39,20))]
    for n,(a,b) in enumerate(boxes):
        assert poly.count_roots(a,b)==1
        rows.append({'id':'exact_cubic_root_isolation_'+str(n),'status':'pass',
                     'method':'exact_Sturm','interval':[str(a),str(b)]})
    for x,sign in [(-1,1),(sp.Rational(1,4),-1),(1,1),
                   (sp.Rational(7,5),-1),(sp.Rational(7,4),1),(2,-1)]:
        assert sp.sign(cs.subs(s,x))==sign
        rows.append({'id':'coefficient_sign_'+str(x),'status':'pass','method':'exact_rational'})
    return {'schema_version':1,'status':'pass','check_count':len(rows),'checks':rows,
            'resource':RESOURCE,'scope':'Full formulas in satellite28; no RH counterexample, no full GCT quantum-module specialization, no Lean run.'}


if __name__=='__main__':
    result=checks()
    result['script_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    if '--write' in sys.argv:
        Path(__file__).with_name('gct_spectrum_results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':result['status'],'check_count':result['check_count'],'resource':RESOURCE}))
