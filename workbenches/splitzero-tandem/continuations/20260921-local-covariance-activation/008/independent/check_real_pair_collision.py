"""Exact joint moment, conductor-coefficient, and inverse-pole identities."""
from pathlib import Path
import hashlib,json
import sympy as s
HERE=Path(__file__).resolve().parent
checks=[]
def check(name,expr):
    entries=list(expr) if isinstance(expr,s.MatrixBase) else [expr]
    for e in entries:assert s.cancel(s.expand(e))==0,(name,e)
    checks.append({'name':name,'entries':len(entries)})

xi,tau,t=s.symbols('xi tau t')
A,B,C,H,F,Ab,Bb,Cb,Hb,Fb=s.symbols('A B C H F Ab Bb Cb Hb Fb')
G=A*tau+B*xi+C*tau**2/2+H*xi*tau+F*xi**2/2
Gb=Ab*tau+Bb*xi+Cb*tau**2/2+Hb*xi*tau+Fb*xi**2/2
E=s.expand(G*Gb)
mu=[s.diff(E,xi,n).subs(xi,0) for n in range(4)]
c=A*Ab;R=A*Bb+Ab*B;d=-s.I*R;e=-B*Bb
c3=(C*Ab+Cb*A)/2
d2=-s.I*((B*Cb+Bb*C)/2+H*Ab+Hb*A-4*c)
e1=-(F*Ab+Fb*A)/2-(H*Bb+Hb*B)+4*R
f=s.I*((F*Bb+Fb*B)/2-4*B*Bb)
check('period moment second coefficient',s.expand(mu[0]).coeff(tau,2)-c)
check('period moment third coefficient',s.expand(mu[0]).coeff(tau,3)-c3)
check('first moment period derivative',s.expand(mu[1]).coeff(tau,1)-R)
check('first moment second period coefficient',s.expand(mu[1]).coeff(tau,2)-(B*Cb+Bb*C)/2-H*Ab-Hb*A)
check('second moment at the pair zero',mu[2].subs(tau,0)-2*B*Bb)
check('second moment period derivative',s.expand(mu[2]).coeff(tau,1)-(F*Ab+Fb*A)-2*(H*Bb+Hb*B))
check('third moment at the pair zero',mu[3].subs(tau,0)-3*(F*Bb+Fb*B))

m0,m1,m2,m3=s.symbols('m0 m1 m2 m3')
omega=-s.I*t+s.I*t**3/3
sym=s.series(s.exp(-4*omega)*(m0+m1*omega+m2*omega**2/2+m3*omega**3/6),t,0,4).removeO().expand()
g=[m0,-s.I*(m1-4*m0),-m2/2+4*m1-8*m0,s.I*(m3/6-2*m2+s.Rational(25,3)*m1-12*m0)]
for n in range(4):check(f'complete original centered coefficient {n}',sym.coeff(t,n)-g[n])
actual=[s.expand(v.subs(dict(zip([m0,m1,m2,m3],mu)))) for v in g]
check('first inverse-series coefficient expansion',actual[1].coeff(tau,1)-d)
check('second first-coefficient period jet',actual[1].coeff(tau,2)-d2)
check('second coefficient constant',actual[2].subs(tau,0)-e)
check('second coefficient linear jet',actual[2].coeff(tau,1)-e1)
check('third coefficient constant',actual[3].subs(tau,0)-f)

g0,g1,g2,g3=s.symbols('g0 g1 g2 g3',nonzero=True)
hh=[1/g0,-g1/g0**2,(g1*g1-g0*g2)/g0**3,(-g1**3+2*g0*g1*g2-g0**2*g3)/g0**4]
gg=[g0,g1,g2,g3]
for n in range(4):check(f'full reciprocal convolution {n}',sum(gg[k]*hh[n-k] for k in range(n+1))-(1 if n==0 else 0))

cs,ds,es,fs,c3s,d2s,e1s=s.symbols('c d e f c3 d2 e1',nonzero=True)
sub={g0:cs*tau**2+c3s*tau**3,g1:ds*tau+d2s*tau**2,g2:es+e1s*tau,g3:fs}
num=s.expand((-g1**3+2*g0*g1*g2-g0**2*g3).subs(sub))
Delta=ds*(ds*ds-2*cs*es)
check('generic inverse top-entry leading numerator',num.coeff(tau,3)+Delta)
Knum=2*cs*ds*e1s+2*c3s*ds*es+(2*cs*es-3*ds**2)*d2s-cs**2*fs
check('exceptional inverse top-entry next numerator',num.coeff(tau,4)-Knum)
check('second inverse upper diagonal leading numerator',s.expand((g1*g1-g0*g2).subs(sub)).coeff(tau,2)-(ds*ds-cs*es))

aa,bb,theta=s.symbols('aa bb theta',positive=True)
check('exact phase-angle discriminant',Delta.subs({cs:aa**2,es:-bb**2,ds:-2*s.I*aa*bb*theta})+4*s.I*aa**3*bb**3*theta*(1-2*theta**2))
r0,r1,r2,r3=s.symbols('rho0 rho1 rho2 rho3',positive=True)
Cs=s.Matrix([[es*r2/r0,fs*r3/r0],[0,es*r3/r1]])
check('complete limiting forward determinant',Cs.det()-es**2*r2*r3/(r0*r1))
L=(ds**2-cs*es)/cs**3
for dd in [0,2*cs*es]:
    check(f'exceptional inverse determinant magnitude square case {dd}',s.expand((L**2-es**2/cs**4).subs(ds**2,dd)))

u,u0=s.symbols('u u0',nonzero=True)
check('unchanged original-period coordinate',1/u-1/u0+(u-u0)/(u*u0))
out={'status':'pass','groups':len(checks),'scalar_entries':sum(v['entries'] for v in checks),'checks':checks,
     'proof_sha256':hashlib.sha256((HERE/'REAL_PAIR_COLLISION.tex').read_bytes()).hexdigest(),
     'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'scope':'Exact identities on the specified simple real conjugate-pair locus; this checker does not assert existence of a real period on that locus.'}
(HERE/'REAL_PAIR_COLLISION_CHECK.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'pass','groups':out['groups'],'scalar_entries':out['scalar_entries']}),flush=True)
