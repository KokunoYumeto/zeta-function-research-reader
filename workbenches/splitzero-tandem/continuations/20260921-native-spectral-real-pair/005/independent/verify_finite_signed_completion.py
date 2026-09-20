"""Root exact verification of FS1--31, retaining all original factors."""
from pathlib import Path
import hashlib,itertools,json
import sympy as s
HERE=Path(__file__).resolve().parent
checks=[]
def check(name,value):
    vals=list(value) if isinstance(value,s.MatrixBase) else [value]
    bad=[s.factor(x) for x in vals if s.factor(x)!=0]
    if bad:raise ArithmeticError((name,bad[:3]))
    checks.append({'name':name,'scalar_entries':len(vals),'passed':True})
a,y,z,w,A,B,C,D,r,t,R,p,v=s.symbols('a y z w A B C D r t R p v')
i=s.I
b=i+a*y;c=-i+2*a*y+a*a*z
d=-i*y-a*(i*z+2*y*y)-a*a*y*z
e=2*z-7*i*y*y+a*w
f=i*w+3*i*y**3-4*y*z+a*(6*i*y*y*z+w*y+4*y**4)+2*a*a*y**3*z
P=s.Matrix([a*c,a*e+b*d,a*f+b*e,b*f])
check('FS1 fixed cubic coefficient',a*d+b*c-1)
check('FS1 original resultant',a**3*f-a*a*b*e+a*b*b*d-b**3*c-1)
h=A*r**4+r**3+B*r*r+C*r+D
hp=s.expand(R**4*h.subs(r,p-1/R))
k=A+v+B*v*v+C*v**3+D*v**4
check('FS3 infinity root polynomial',k-v**4*h.subs(r,1/v))
check('FS3 infinity derivative sign',s.diff(k,v)+v*v*s.diff(h,r).subs(r,1/v)-4*v**3*h.subs(r,1/v))
check('FS6 five opens',s.Rational(1,2)*h.subs(r,0)-s.Rational(1,2)*h.subs(r,1)-s.Rational(1,6)*h.subs(r,-1)+s.Rational(1,6)*h.subs(r,2)-2*A-1)
check('FS7 derivative factor',s.diff(hp,R).subs(R,1/(p-r))-s.diff(h,r)/(p-r)**2-4*h/(p-r)**3)
check('FS7 leading coefficient',s.Poly(hp,R).nth(4)-h.subs(r,p))
theta,TTvar=s.symbols('theta TTvar')
newR=1/(p-r);newT=t/(p-r)
check('FS7 finite inverse root',p-1/newR-r)
check('FS7 finite inverse sign',newT/newR-t)
infR=-v/(1-p*v);infT=theta/(1-p*v)
check('FS7 infinity inverse root',infR/(p*infR-1)-v)
check('FS7 infinity inverse sign',infT/(1-p*infR)-theta)
check('FS7 three-chart root compatibility',newR.subs(r,1/v)-infR)
check('FS7 three-chart sign compatibility',newT.subs({r:1/v,t:-theta/v},simultaneous=True)-infT)
ai=-v/theta;bi=1/theta
ci=theta*(1+B*v+C*v*v+D*v**3)
di=theta*(B+C*v+D*v*v);ei=theta*(C+D*v);fi=theta*D
Ai=-v-B*v*v-C*v**3-D*v**4
check('FS12 every infinity product',s.Matrix([ai*ci,ai*di+bi*ci,ai*ei+bi*di,ai*fi+bi*ei,bi*fi])-s.Matrix([Ai,1,B,C,D]))
check('FS12 exact infinity resultant',(ai**3*fi-ai*ai*bi*ei+ai*bi*bi*di-bi**3*ci)*theta**2+s.diff(k,v))
q=s.Matrix([1/t,-r-i*t,A*t**3+2*r*t+3*i*t*t,7*i*r*r*t+(B-17*r+A*r*r)*t*t-13*i*t**3-2*A*t**4])
pi=s.Matrix([A,B,t*t-4*A*r**3-3*r*r-2*B*r,3*A*r**4+2*r**3+B*r*r-r*t*t])
sub=dict(zip((a,y,z,w),q))
check('FS13 full source inverse',P.subs(sub,simultaneous=True)-pi)
check('FS16 source Jacobian',q.jacobian([t,r,A,B]).det()-t**3)
check('FS16 target Jacobian',pi.jacobian([t,r,A,B]).det()+2*t**3)
check('FS14 numerator y',a*a*f-a*b*e+2*b*b*d-(b+i)*y)
check('FS14 numerator z',a*f-b*e+7*y*y-10*i*a*y**3-4*a*a*y**4-2*b**3*z)
check('FS14 numerator w',a*a*e*y**3+7*i*a*a*y**5+3*i*a*e*y*y-17*a*y**4-2*e*y-f-11*i*y**3-b**3*w)
sig={a:-a,y:y+2*i/a,z:6*i/a**2-z,w:w-14*i*y*y/a+28*y/a**2+40*i/a**3}
check('FS31 full sign deck action',P.subs(sig,simultaneous=True)-P)
disc=s.discriminant(h,r)
check('FS18 cubic discriminant',disc.subs(A,0)-(B*B*C*C-4*C**3-4*B**3*D+18*B*C*D-27*D*D))
Z=s.Matrix([[0,0,0,-D/A],[1,0,0,-C/A],[0,1,0,-B/A],[0,0,1,-1/A]])
L=4*A*Z**3+3*Z**2+2*B*Z+C*s.eye(4)
T=s.Matrix(4,4,lambda j,k:s.trace(Z**(j+k)))
check('FS19 even trace determinant',(2*T).det()-16*disc/A**6)
check('FS19 odd derivative determinant',L.det()-disc/A**2)
check('FS28 omitted square',h.subs({B:1/(4*A)+2*A*C,D:A*C*C})-A*(r*r+r/(2*A)+C)**2)
check('FS29 quadruple coefficients',h.subs({B:3/(8*A),C:1/(16*A*A),D:1/(256*A**3)})-A*(r+1/(4*A))**4)

local=[]
for m in (2,3,4):
    cc=s.symbols('c_m',nonzero=True)
    E=s.zeros(m)
    for j in range(m-1):E[j+1,j]=1
    EE=s.diag(E,E)
    TT=s.zeros(m).row_join(cc*E**(m-1)).col_join(s.eye(m).row_join(s.zeros(m)))
    check(f'FS22 root relation m={m}',EE**m)
    check(f'FS22 exact sign relation m={m}',TT**2-cc*EE**(m-1))
    check(f'FS22 commuting multiplication m={m}',EE*TT-TT*EE)
    basis=[EE**j for j in range(m)]+[TT*EE**j for j in range(m)]
    trace=s.Matrix(2*m,2*m,lambda j,k:s.trace(basis[j]*basis[k]))
    expected=s.zeros(2*m);expected[0,0]=2*m
    check(f'FS25 every local trace entry m={m}',trace-expected)
    current=s.eye(2*m);dims=[2*m]
    for power in range(1,7):
        cols=s.Matrix.hstack(EE*current,TT*current).columnspace()
        current=s.Matrix.hstack(*cols) if cols else s.zeros(2*m,0)
        dims.append(current.cols)
        if not current.cols:break
    expected_dims={2:[4,3,2,1,0],3:[6,5,3,1,0],4:[8,7,5,3,1,0]}[m]
    if dims!=expected_dims:raise ArithmeticError(('FS24 filtration',m,dims))
    checks.append({'name':f'FS24 full filtration m={m}','scalar_entries':len(dims),'passed':True})
    socle=EE.col_join(TT).nullspace()
    if len(socle)!=1 or socle[0][2*m-1]==0:raise ArithmeticError(('FS24 socle',m))
    checks.append({'name':f'FS24 socle m={m}','scalar_entries':2*m,'passed':True})
    local.append({'m':m,'maximal_ideal_power_dimensions':dims,'trace_rank':trace.rank()})

source=HERE/'FINITE_SIGNED_COMPLETION.tex'
out={'source':source.name,'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
     'check_groups':len(checks),'scalar_entries':sum(x['scalar_entries'] for x in checks),'checks':checks,'local_algebras':local,
     'scope':'Exact identities supplement the fully written geometric and local-algebra proofs FS1–31. No finite sampling is used to prove a global geometric assertion.'}
(HERE/'FINITE_SIGNED_COMPLETION_CERTIFICATE.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:out[k] for k in ('check_groups','scalar_entries','source_sha256')}))
