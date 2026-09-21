from pathlib import Path
import json
import sympy as s
import mpmath as mp
mp.mp.dps=80
P=Path(__file__).parent
checks=[]
def exact(label,a,b=0):
    if isinstance(a,s.MatrixBase): ok=all(s.simplify(t)==0 for t in a-b)
    else: ok=s.simplify(a-b)==0
    assert ok,label
    checks.append(dict(label=label,kind='exact',passed=True))
def number(x):
    return mp.mpc(str(s.re(x).evalf(85)),str(s.im(x).evalf(85)))
def mat(A):return mp.matrix([[number(A[i,j]) for j in range(A.cols)]for i in range(A.rows)])
def bound(label,left,right):
    assert left<=right+mp.mpf('1e-65'),(label,left,right)
    checks.append(dict(label=label,kind='numerical80digits',passed=True,left=mp.nstr(left,70),right=mp.nstr(right,70)))
x=s.symbols('y'); pol=[s.Integer(1),x]
for n in range(1,13):pol.append(s.expand(x*pol[-1]-n*(s.Rational(n)-s.Rational(1,2))*pol[-2]))
roots=[s.I,-s.I]
obs=[3+2*s.I,-2+s.I]
states=[]
for D in range(4,13):
    # Matrices below equal physical Grams times M_sigma. This common positive
    # factor cancels from the generalized angles and all consecutive ratios.
    weights=s.diag(*[1/(s.factorial(n)*s.rf(s.Rational(1,2),n)) for n in range(D+1)])
    E=s.Matrix([[p.subs(x,z) for p in pol[:D+1]]for z in roots])
    W=s.Matrix([[p.subs(x,z) for p in pol[:D+1]]for z in obs])
    A=E*weights*E.conjugate().T;cross=W*weights*E.conjugate().T
    B=W*weights*W.conjugate().T;C=s.simplify(B-cross*A.inv()*cross.conjugate().T)
    exact('Hermitian C degree '+str(D),C,C.conjugate().T)
    Bn=mat(B);Cn=mat(C);L=mp.cholesky(Bn);Si=L**-1*Cn*(L.H**-1)
    eig=sorted([mp.re(v) for v in mp.eigsy(Si,eigvals_only=True)] ,reverse=True) if all(abs(mp.im(Si[i,j]))<mp.mpf('1e-70') for i in range(2) for j in range(2)) else sorted([mp.re(v) for v in mp.eighe(Si,eigvals_only=True)],reverse=True)
    assert min(eig)>0 and max(eig)<1
    states.append(dict(D=D,E=E,W=W,A=A,cross=cross,B=B,C=C,eig=eig,log=[mp.log(v) for v in eig]))
for old,new in zip(states,states[1:]):
    D=new['D']; hn=s.factorial(D)*s.rf(s.Rational(1,2),D)
    e=s.Matrix([pol[D].subs(x,z) for z in roots]);w=s.Matrix([pol[D].subs(x,z) for z in obs])
    kap=s.simplify(hn+(e.conjugate().T*old['A'].inv()*e)[0])
    v=s.simplify(w-old['cross']*old['A'].inv()*e)
    exact('Full-root covariance innovation '+str(D),new['C'],old['C']+v*v.conjugate().T/kap)
    exact('Unprojected innovation '+str(D),new['B'],old['B']+w*w.conjugate().T/hn)
    dc=mp.log(number(s.simplify(new['C'].det()/old['C'].det())).real)
    db=mp.log(number(s.simplify(new['B'].det()/old['B'].det())).real)
    pos=sum(max(y-z,0)for z,y in zip(old['log'],new['log']))
    neg=sum(max(z-y,0)for z,y in zip(old['log'],new['log']))
    bound('Positive direction '+str(D),pos,dc);bound('Negative direction '+str(D),neg,db)
    old.update(pos=pos,neg=neg,dc=dc,db=db)
neg=sum(z['neg'] for z in states[:-1]);pos=sum(z['pos'] for z in states[:-1])
db=mp.log(number(s.simplify(states[-1]['B'].det()/states[0]['B'].det())).real)
bound('Whole-window downward variation',neg,db)
delta=sum(states[-1]['log'])-sum(states[0]['log'])
bound('Directed path identity absolute residual',abs(pos+neg-delta-2*neg),mp.mpf('1e-70'))
running=states[0]['log'][:]
for z in states:
    running=[max(a,b)for a,b in zip(running,z['log'])]
    bound('Running envelope at '+str(z['D']),sum(a-b for a,b in zip(running,z['log'])),neg)
for threshold in [-20,-10,-5,-1]:
    stats=[sum(max(v,mp.mpf(threshold))for v in z['log'])for z in states]
    down=sum(max(a-b,0)for a,b in zip(stats,stats[1:]))
    bound('Increasing clipped statistic '+str(threshold),down,neg)
for i in [0,1]:
    lo=states[i];hi=states[-2+i]
    ratioC=s.simplify(hi['C'].det()/lo['C'].det());ratioB=s.simplify(hi['B'].det()/lo['B'].det())
    exact('Full endpoint determinant ratio '+str(i),s.simplify((hi['B'].inv()*hi['C']).det()/(lo['B'].inv()*lo['C']).det()),ratioC/ratioB)
report=dict(scope='Auxiliary complete Gamma evaluation example, roots +/-i, two observation rows at 3+2i and -2+i. Every lower-root constraint is retained; not native period data.',physical_mass='sqrt(2*pi); common Gram factor cancels only in proved homogeneous ratios',precision_digits=80,exact=sum(z['kind']=='exact'for z in checks),numerical=sum(z['kind']!='exact'for z in checks),checks=checks,downward_variation=mp.nstr(neg,60),positive_variation=mp.nstr(pos,60),unprojected_allowance=mp.nstr(db,60),spectra=[dict(degree=z['D'],log_angles=[mp.nstr(v,60)for v in z['log']])for z in states])
(P/'ANGLE_DIRECTION_CHECKS.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:report[k]for k in ['exact','numerical','downward_variation','positive_variation','unprojected_allowance']}))
