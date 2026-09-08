"""Exact composition checks. No author/source checker is imported."""
from pathlib import Path
import hashlib
import json
import sympy as S

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
z,w,tau,x,y,u=S.symbols('z w tau x y u', nonzero=True)
w=S.Symbol('w', positive=True)
checks=0
def zero(v):
    global checks
    checks+=1
    assert S.cancel(S.expand(v))==0, v
def zm(M):
    for a in M: zero(a)
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()

F=S.Matrix([(1+x*y)**3*u+y*y*(1+x*y)*(4+3*x*y),
    y+3*x*(1+x*y)**2*u+3*x*y*y*(4+3*x*y),
    2*x-3*x*x*y-x**3*u])
J=F.jacobian([x,y,u])
zero(J.det()+2)
base={x:1,y:-S.Rational(3,2),u:S.Rational(13,2)}
path={x:1/z,y:-3*z/2,u:13*z*z/2}
J0=J.subs(base)
Jg=J.subs(path).applyfunc(S.cancel)
E23=S.zeros(3);E23[1,2]=1
BF=S.eye(3)+S.Rational(3,4)*(1-z*z)*E23
CF=(J0.inv()*BF.inv()*Jg).applyfunc(S.cancel)
KF=(CF*CF.T).applyfunc(S.cancel)
zm(F.subs(path)-S.Matrix([-z*z/4,0,0]))
zero(CF.det()-1)
vstar=S.Matrix([S.Rational(1,4),S.Rational(3,8),-S.Rational(9,4)])
Sstar=vstar*vstar.T
zm((z**3*CF).applyfunc(lambda t:S.limit(t,z,0))-vstar*S.Matrix([[0,0,1]]))
zm((z**6*KF).applyfunc(lambda t:S.limit(t,z,0))-Sstar)

# Original Laurent identity and algebraic conic, with no branch selection.
q,pp,ss=S.symbols('q pp ss',nonzero=True)
original=q**10-q**4-q**-4+q**-10
qi=lambda n:sum(q**(n-1-2*j) for j in range(n))
zero(original-(q-q**-1)**2*qi(7)*qi(3))
zero(qi(3)-((q+q**-1)**2-1))
zero(qi(7)-((q+q**-1)**6-5*(q+q**-1)**4+6*(q+q**-1)**2-1))
qz=(pp-z/2)/2
qzi=(pp+z/2)/2
zero(S.expand(qz*qzi-1).subs(pp**2,4+z*z/4))
zero(qz-qzi+z/2)
zero(qz+qzi-pp)
zero((-z*z/4)-2*(-z*z/8))
mm=z*z/4
nn=4+mm
Cz=mm*(nn**3-5*nn**2+6*nn-1)*(nn-1)
Cs=-2*ss*(7-28*ss+28*ss**2-8*ss**3)*(3-2*ss)
zero(Cz-Cs.subs(ss,-z*z/8))
zero(S.limit(Cz/z**2,z,0)-S.Rational(21,4))
B=-42+196*tau-280*tau**2+160*tau**3-32*tau**4
zero(Cs.subs(ss,tau)-tau*B)
zero(S.expand(Cz).subs(z*z,-8*tau)-tau*B)

# The actual complex continuation, keeping conjugation and positivity.
zNS=-S.I*S.sqrt(8)*w
zero(zNS**2+8*w*w)
zero(zNS**6+512*w**6)
zero(zNS**4-64*w**4)
zero((1-zNS**2)/8-(S.Rational(1,8)+w*w))
KNS=KF.subs(z,zNS).applyfunc(S.expand_complex)
CNS=S.expand(Cz.subs(z,zNS))
zero(CNS-w*w*B.subs(tau,w*w))
zm((w**6*KNS).applyfunc(lambda a:S.limit(a,w,0))+Sstar/512)
zm((w**4*CNS*KNS).applyfunc(lambda a:S.limit(a,w,0))-S.Rational(21,256)*Sstar)

def spectral_weights(M):
    mean=S.trace(M)/3
    norm=lambda a:S.expand_complex(a*S.conjugate(a))
    return [norm(S.trace(M))/9,
            sum(norm(M[i,i]-mean) for i in range(3))/2,
            sum(norm(M[i,j]) for i in range(3) for j in range(i+1,3))]
target=[S.Rational(113569,36864),S.Rational(100825,12288),S.Rational(531,512)]
for a,b in zip(spectral_weights(Sstar),target): zero(a-b)
weights=spectral_weights(KNS)
for a,b in zip(weights,target):
    zero(S.limit(w**12*a,w,0)-b/262144)
    zero(S.limit(w**8*CNS*S.conjugate(CNS)*a,w,0)-S.Rational(441,65536)*b)
for a,b in zip(spectral_weights(CNS*KNS),weights):
    zero(a-CNS*S.conjugate(CNS)*b)

# Exact differential pullback, with both second-order terms preserved.
pp_deriv=z/(4*pp)
qprime=S.diff(qz,z)+S.diff(qz,pp)*pp_deriv
zero(qprime+qz/(2*pp))
Ds=lambda a:-4/z*S.diff(a,z)
zero(Ds(-z*z/8)-1)
zero(Ds(-z/2)-2/z)
zero((-4/z)*pp_deriv+1/pp)
zero((-4/z)*qprime+qz/((-z/2)*pp))
for k in range(-8,13):
    f=z**k
    zero(-Ds(Ds(f))/4-(-4/z**2*S.diff(f,z,2)+4/z**3*S.diff(f,z)))
    zero(-Ds(Ds(f))/4+4*k*(k-2)*z**(k-4))
for entry in KF:
    zero(-Ds(Ds(entry))/4-(-4/z**2*S.diff(entry,z,2)+4/z**3*S.diff(entry,z)))

report={'status':'passed','checks':checks,'proof_sha256':sha(HERE/'ym_composition.tex'),
        'checker_sha256':sha(Path(__file__)),
        'scope':['full original F and tensor from differentiated Jacobian',
                 'all conic and original coefficient identities',
                 'complex path and both state limit coefficients',
                 'all three Hermitian spectral weights and both measure limits',
                 'exact scalar modulus identity','full retained arithmetic derivative'],
        'state_limit_coefficients':['-1/512','21/256'],
        'measure_limit_coefficients':['1/262144','441/65536'],
        'findings':[]}
(HERE/'composition_verification.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'status':'passed','checks':checks}))
