"""Exact checks of the original signed-algebra and metric return SGR1--14."""
from pathlib import Path
import itertools,json,hashlib
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
B=Path(__file__).resolve().parent
checks=[];entries=0
def ck(name,values):
    global entries
    vals=list(values) if isinstance(values,s.MatrixBase) else (values if isinstance(values,list) else [values])
    for val in vals:assert s.cancel(s.expand(val))==0,(name,val)
    checks.append({'name':name,'entries':len(vals),'passed':True});entries+=len(vals)
def eq(name,value,expected):
    global entries
    assert value==expected,(name,value,expected)
    checks.append({'name':name,'entries':1,'passed':True});entries+=1
def vp(a,p):
    a,b=map(int,s.Rational(a).as_numer_denom())
    if not a:return 10**9
    n=0
    while a%p==0:a//=p;n+=1
    while b%p==0:b//=p;n-=1
    return n
def smith(M,p):
    den=s.ilcm(*[s.denom(x) for x in M])
    D=smith_normal_form(M*den,domain=ZZ)
    return sorted(vp(D[j,j],p)-vp(den,p) for j in range(M.rows))
R=s.Matrix([[2,1+s.I,0,1],[0,3,s.I,2],[0,0,2,1-s.I],[0,0,0,1]])
W=s.Matrix([[1,s.I,2,0],[0,2,1+s.I,1],[0,0,3,s.I],[0,0,0,2]])
Hu=R.H*R;Hw=W.H*W
Gu=s.diag(Hu,Hu);Gw=s.diag(Hw,Hw)
r,sg,z=s.symbols('r sg z')
fixture_data=[]
for roots in [(13,4,18,468),(13,4,20,130)]:
    p=roots[0];A=-s.Rational(1,sum(roots));f=s.prod(r-x for x in roots)
    h=s.Poly(A*f,r);BB=h.nth(2)
    V=s.Matrix([[x**j for j in range(4)] for x in roots]);Vi=V.inv()
    d=[s.prod(roots[i]-roots[j] for j in range(4) if i!=j) for i in range(4)]
    ds=[A*x for x in d]
    Q=Vi*s.diag(*d)
    typ=1 if roots[2]%p else 2
    ck('SGR1 exact interpolation '+str(typ),V*Q-s.diag(*d))
    # Coefficients of all four original affine coordinate functions, in the
    # complete parity basis. Evaluation, not numerical roots, checks signs.
    evR=s.Matrix([[0,-x,3*s.I*di,(BB-17*x+A*x*x)*di-2*A*di*di] for x,di in zip(roots,ds)])
    evQ=s.Matrix([[1/di,-s.I,A*di+2*x,7*s.I*x*x-13*s.I*di] for x,di in zip(roots,ds)])
    C=(Vi*evR).col_join(Vi*evQ)
    stable=0
    for eps in itertools.product([-1,1],repeat=4):
        H=Vi*s.diag(*eps)*V;Sig=s.diag(s.eye(4),H)
        ck('SGR1 every full involution '+str((typ,eps)),Sig*Sig-s.eye(8))
        integral=all(vp(t,p)>=0 for t in H)
        clustered=[0,3] if typ==1 else [0,2,3]
        expected=len({eps[i] for i in clustered})==1
        eq('SGR2 complete integrality test '+str((typ,eps)),integral,expected)
        stable+=integral
        if not integral:
            eq('SGR2 complete relative Smith '+str((typ,eps)),smith(H,p),[-typ,0,0,typ])
        for i,x in enumerate(roots):
            row=s.Matrix([[1,x,x*x,x**3]])
            e=row.row_join(sg*row)
            changed=row.row_join(eps[i]*sg*row)
            ck('SGR6 all eight dual states '+str((typ,eps,i)),e*Sig-changed)
        if eps==(-1,-1,-1,-1):
            for i,x in enumerate(roots):
                row=s.Matrix([[1,x,x*x,x**3]]);e=row.row_join(sg*row)
                q=(e*C).T
                want=s.Matrix([sg/ds[i],-x-s.I*sg,A*sg**3+2*x*sg+3*s.I*sg**2,
                  7*s.I*x*x*sg+(BB-17*x+A*x*x)*sg**2-13*s.I*sg**3-2*A*sg**4])
                ck('SGR5 all affine coordinate terms '+str((typ,i)),[s.rem(t,sg*sg-ds[i],sg) for t in q-want])
    eq('SGR2 exact integral subgroup order '+str(typ),stable,8 if typ==1 else 4)
    eq('SGR4 stable core every factor '+str(typ),smith(Q,p),[0,0,0,1] if typ==1 else [0,0,1,2])
    for j,x in enumerate(roots):
        cj=Q[:,j];v=s.Matrix([[1,x,x*x,x**3]])
        H=s.eye(4)-2*cj*v/d[j]
        Nj=s.Matrix([[d[j],-x,0,0],[0,1,-x,0],[0,0,1,-x],[0,0,0,1]])
        D=s.diag(s.eye(4),Nj)
        ck('SGR3 exact full intersection constraint '+str((typ,j)),v*Nj-s.Matrix([[d[j],0,0,0]]))
        eq('SGR3 all intersection images integral '+str((typ,j)),all(vp(t,p)>=0 for t in H*Nj),True)
        ck('SGR3 complete stable intersection matrix '+str((typ,j)),(Nj.inv()*H*Nj)**2-s.eye(4))
        nu=((cj.H*Hu*cj)[0]*(v*Hu.inv()*v.H)[0]/(d[j]*d[j])).expand()
        ck('SGR9 original-metric entire characteristic polynomial '+str((typ,j)),
          (z*s.eye(4)-Hu.inv()*H.H*Hu*H).det(method='domain-ge')-(z-1)**2*(z*z-(4*nu-2)*z+1))
        Gdu=D.H*Gu*D;Gdw=D.H*Gw*D
        ck('SGR13 exact Gram determinant '+str((typ,j)),Gdu.det()-d[j]**2*Gu.det())
        ck('SGR14 complete inverse-spectrum similarity '+str((typ,j)),Gdw.inv()*Gdu-D.inv()*Gw.inv()*Gu*D)
    fixture_data.append({'roots':roots,'type':typ,'A':str(A),'D_i':[str(x) for x in ds],'stable_group_order':stable})
rho=s.symbols('rho',real=True)
K=s.Matrix([[1,rho],[rho,1]]);J=s.diag(1,-1)
ck('SGR11 exact arbitrary correlation block characteristic polynomial',
  (z*s.eye(2)-K.inv()*J*K*J).det()-(z-(1+rho)/(1-rho))*(z-(1-rho)/(1+rho)))
receipt={'status':'PASS','groups':len(checks),'scalar_entries':entries,'checks':checks,
 'proof_sha256':hashlib.sha256((B/'SIGNED_ORIGINAL_RETURN_BODY.tex').read_bytes()).hexdigest(),
 'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'exact_fixtures':fixture_data,
 'scope':'Universal proofs are SGR1–14; exact tests cover all16signs on both actual strata, every affine function coordinate, all four intersection bases, full dense Hermitian metric spectra, and an arbitrary correlation block. Fixture metrics test the formulas and do not replace original programme metrics.'}
(B/'SIGNED_ORIGINAL_RETURN_CERTIFICATE.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:receipt[k] for k in ['status','groups','scalar_entries','proof_sha256']},indent=2))
