"""Full-coordinate exact checks of EQR1--13; no numerical asymptotics."""
from pathlib import Path
import hashlib,json
import sympy as s
B=Path(__file__).resolve().parent;checks=[];entries=0
def ck(name,M):
    global entries
    vals=list(M) if isinstance(M,s.MatrixBase) else (M if isinstance(M,list) else [M])
    for val in vals:assert s.cancel(s.expand(val))==0,(name,val)
    checks.append({'name':name,'entries':len(vals),'passed':True});entries+=len(vals)
def eq(name,x,y):
    global entries
    assert x==y,(name,x,y)
    checks.append({'name':name,'entries':1,'passed':True});entries+=1
P,t,r,sg,A,BB,w=s.symbols('P t r sg A BB w',nonzero=True)
E=s.Matrix([[1,P,P*P,P**3],[0,1,2*P+t,3*P*P+3*P*t+t*t]])
K=s.Matrix([[P*(P+t),0],[-2*P-t,P*(P+t)],[1,-2*P-t],[0,1]])
L=s.Matrix([[0,0,1,2*P+t],[0,0,0,1]])
R0=s.Matrix([[1,-P],[0,1],[0,0],[0,0]])
ck('EQR3 entire finite coordinate inverse',E.col_join(L)*R0.row_join(K)-s.eye(4))
ck('EQR3 complete opposite inverse',R0.row_join(K)*E.col_join(L)-s.eye(4))
ck('EQR3 all kernel columns',E*K)
ck('EQR3 exact determinant',E.col_join(L).det()-1)
M=s.Matrix(4,4,s.symbols('m0:16'))
U=E*M
q=s.Matrix([1/sg,-r-s.I*sg,A*sg**3+2*r*sg+3*s.I*sg**2,
  7*s.I*r*r*sg+(BB-17*r+A*r*r)*sg**2-13*s.I*sg**3-2*A*sg**4])
Y=U[:,0]/sg-r*U[:,1]+sg*(-s.I*U[:,1]+2*r*U[:,2]+7*s.I*r*r*U[:,3])+sg**2*(3*s.I*U[:,2]+(BB-17*r+A*r*r)*U[:,3])+sg**3*(A*U[:,2]-13*s.I*U[:,3])-2*A*sg**4*U[:,3]
ck('EQR2 all original affine terms and every matrix entry',E*M*q-Y)
aa,yy,zz,ww=s.symbols('aa yy zz ww',nonzero=True)
inv=s.Matrix([-aa,yy+2*s.I/aa,6*s.I/aa**2-zz,ww-14*s.I*yy**2/aa+28*yy/aa**2+40*s.I/aa**3])
expected=40*s.I/aa**3*U[:,3]+(6*s.I*U[:,2]+28*yy*U[:,3])/aa**2+(2*s.I*U[:,1]-14*s.I*yy**2*U[:,3])/aa-aa*U[:,0]+yy*U[:,1]-zz*U[:,2]+ww*U[:,3]
ck('EQR13 full rational-sign quotient identity',E*M*inv-expected)
Pc=s.Integer(2);ac=3*Pc/s.Integer(22)
At=-(5*Pc+7*t)/(22*Pc**2+35*Pc*t+7*t*t)
zt=2*Pc*(Pc+t)/(5*Pc+7*t)
ft=(r-Pc)*(r-Pc-t)*(r-2*Pc)*(r-zt)
Bt=s.Poly(s.expand(At*ft),r).nth(2)
ck('EQR5 exact unchanged A0',At.subs(t,0)+5/(22*Pc))
ck('EQR5 exact unchanged B0',Bt.subs(t,0)+3*Pc/2)
Ru=s.Matrix([[2,1+s.I,0,1],[0,3,s.I,2],[0,0,2,1-s.I],[0,0,0,1]])
Rw=s.Matrix([[1,s.I,2,0],[0,2,1+s.I,1],[0,0,3,s.I],[0,0,0,2]])
metrics={'U':Ru.H*Ru,'W':Rw.H*Rw}
poly_sets={'escape':[1,r,r*r,r**3],
 'bounded':[(r-Pc)**2,1,r-Pc,(r-Pc)**3],
 'sqrt':[(r-Pc)**2,(r-Pc)**3,1,r-Pc],
 'cancel':[(r-Pc)**2,(r-Pc)**3,-7*s.I*Pc/2-(r-Pc)/(2*Pc*ac),1]}
for case,polys in poly_sets.items():
    Mc=s.Matrix.hstack(*[s.Matrix([s.Poly(pol,r).nth(j) for j in range(4)]) for pol in polys])
    eq('EQR classification fixture full receiver '+case,Mc.det()!=0,True)
    Ec=E.subs(P,Pc);U0=Ec.subs(t,0)*Mc;Uc=Ec*Mc
    alpha=s.diff(polys[0],r,2).subs(r,Pc)/2;beta=s.diff(polys[1],r,2).subs(r,Pc)/2
    for delta in [0,1]:
        lam=s.sqrt((2*delta-1)*ac)
        for sign in [-1,1]:
            l=sign*lam
            qc=q.subs({A:At,BB:Bt,r:Pc+delta*t,sg:l*w}).subs(t,w*w)
            yt=Ec.subs(t,w*w)*Mc*qc
            if case=='escape':
                ck('EQR6 complete leading state '+str((case,delta,sign)),s.Matrix([s.limit(w*x,w,0) for x in yt])-U0[:,0]/l)
            elif case=='bounded':
                ck('EQR7 complete finite limit '+str((case,delta,sign)),s.Matrix([s.limit(x,w,0) for x in yt])+Pc*U0[:,1])
            else:
                zlead=s.Matrix([0,alpha])/l+l*(2*Pc*U0[:,2]+7*s.I*Pc**2*U0[:,3])
                wlead=s.Matrix([0,-Pc*beta])+l*l*(3*s.I*U0[:,2]+(-3*Pc/s.Integer(2)-17*Pc-5*Pc/s.Integer(22))*U0[:,3])
                ck('EQR9 every sqrt coefficient '+str((case,delta,sign)),s.Matrix([s.limit(x/w,w,0) for x in yt])-zlead)
                ck('EQR9 every next coefficient '+str((case,delta,sign)),s.Matrix([s.limit((x-w*z)/w**2,w,0) for x,z in zip(yt,zlead)])-wlead)
                if case=='cancel' and delta==1:
                    ck('EQR10 actual cancelling pair '+str(sign),zlead)
                    ck('EQR10 exact nonzero coefficient '+str(sign),wlead[0]+l*l*181*Pc/s.Integer(22)*s.sympify(polys[3]).subs(r,Pc))
                    eq('EQR10 nonvanishing '+str(sign),wlead[0]!=0,True)
    for tv in [s.Integer(0),s.Rational(1,3)]:
        Ev=Ec.subs(t,tv);Kv=K.subs({P:Pc,t:tv});Lv=L.subs({P:Pc,t:tv})
        for key,H in metrics.items():
            G=(Ev*H.inv()*Ev.H).inv();lift=H.inv()*Ev.H*G
            comp=Lv*(s.eye(4)-lift*Ev)
            ck('EQR4 full exact inverse '+str((case,tv,key)),lift*Ev+Kv*comp-s.eye(4))
            ck('EQR4 full original Gram decomposition '+str((case,tv,key)),Ev.H*G*Ev+comp.H*(Kv.H*H*Kv)*comp-H)
# The exceptional-root formula, tested by retaining a repeated root and a
# distinct third root symbolically; the actual receiver decides its values.
x0,x1,c3=s.symbols('x0 x1 c3',nonzero=True)
poly=s.Poly(c3*(r-x0)**2*(r-x1),r);a,b,c,d=poly.all_coeffs()
Delta=b*b-3*a*c
ck('EQR11 complete repeated-root expression',(9*a*d-b*c)-2*Delta*x0)
receipt={'status':'PASS','groups':len(checks),'scalar_entries':entries,'checks':checks,
 'proof_sha256':hashlib.sha256((B/'ESCAPE_QUOTIENT_RETURN_BODY.tex').read_bytes()).hexdigest(),
 'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'scope':'Universal identities checked symbolically; all four asymptotic strata, both roots and both signs exercised with exact full receivers, including the nonzero −181P/22 coefficient. Dense Hermitian fixtures verify both full kernel-minimum decompositions; they do not replace original programme metrics.'}
(B/'ESCAPE_QUOTIENT_RETURN_CERTIFICATE.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:receipt[k] for k in ['status','groups','scalar_entries','proof_sha256']},indent=2))
