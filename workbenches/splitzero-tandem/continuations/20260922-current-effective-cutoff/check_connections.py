from pathlib import Path
from fractions import Fraction as F
import json, sympy as s
P=Path(__file__).parent
checks=[]
def exact(name,value):
    if s.simplify(value)!=0: raise ArithmeticError(name)
    checks.append(name)
z,t=s.symbols('z t', positive=True)
tp=(4*z*(t+1)-(1-z)*t*t)/(4*z*(1-z))
Lp=-1/(1+t)+(1/(1-z)-t/(4*z))/tp
exact('RC8 derivative cancellation',(1+t)*Lp+t/(4*z*tp))
exact('RC10 differential connection',2*((1+t)*s.Symbol('L')+t*s.log(z)/4)-2*(1+t)*(s.Symbol('L')+s.log(z)/4)+s.log(z)/2)
v,c3,c4=s.symbols('v c3 c4',positive=True)
exact('RC17 third derivative',s.diff(-1/(8*v),v)*c3/(4*v)-c3/(32*v**3))
exact('RC17 fourth derivative',s.diff(c3/(32*v**3),v)*c3/(4*v)+s.diff(c3/(32*v**3),c3)*c4/(4*v)-(c4*v-3*c3*c3)/(128*v**5))
raw=[]
g=z/(1-z)
for j in range(1,5):
    if j>1:g=s.expand(z*s.diff(g,z))
    raw.append(s.factor(g.subs(z,s.Rational(11,20))))
if not (raw[1]<10 and raw[2]<47 and raw[3]<315):raise ArithmeticError('moment floors')
if not raw[2]+3*s.Rational(11,40)*raw[1]+2*s.Rational(11,40)**3<55:raise ArithmeticError('third cumulant')
checks.extend(['raw moment '+str(j+1) for j in range(4)])
exact('centered fourth remainder integral',s.integrate(z*z*(1-z),(z,0,1))*2-s.Rational(1,6))
eps=s.symbols('eps',positive=True)
e=s.Matrix([1,0,0]);f=s.Matrix([0,1,0])
C=s.Matrix([[1,0,0],[0,2,0],[0,0,3]])
M=C+eps*f*e.H
u=s.Matrix([s.Rational(3,5),0,4*s.I/5]);v2=s.Matrix([0,1,0])
J=u.row_join(v2);Proj=J*J.H;x=s.Matrix([1,-eps,0]);y=Proj*x;hidden=x-y
exact('original section isometry',(J.H*J-s.eye(2)).norm()**2)
exact('test eigenclass retains full equation',(M*x-x).norm()**2)
phi=(s.I*(y.H*M*y-y.H*M.H*y))[0]
exact('RC32 full complex residual',phi-2*s.im((y.H*M*hidden)[0]))
R=eps*f*e.H;RB=J.H*R*J;zz=s.trace(RB)
exact('full nilpotence',(R*R).norm()**2)
exact('retained quadratic hidden defect',(J.H*R*(s.eye(3)-Proj)*R*J+zz*RB).norm()**2)
# Exact summation-by-parts for every finite mesh here.
for n in range(1,12):
    D=[s.Integer(0)]+[s.Rational((-1)**j*j,j+1) for j in range(1,n+1)]
    w=[s.Rational(1,(j+1)**2) for j in range(n+1)]
    exact('Abel '+str(n),sum(w[i+1]*(D[i+1]-D[i]) for i in range(n))-w[n]*D[n]-sum((w[i]-w[i+1])*D[i] for i in range(1,n)))
# Original frozen IV implementation is copied verbatim below at build time.

from math import isqrt
from fractions import Fraction
import json
S=10**90
class IV:
    def __init__(self,lo,hi=None):self.lo=lo;self.hi=lo if hi is None else hi
    @staticmethod
    def rat(n,d=1):return IV(n*S//d,-((-n*S)//d))
    @staticmethod
    def dec(x):
        f=Fraction(x);return IV.rat(f.numerator,f.denominator)
    def __add__(a,b):return IV(a.lo+b.lo,a.hi+b.hi)
    def __sub__(a,b):return IV(a.lo-b.hi,a.hi-b.lo)
    def __mul__(a,b):
        v=[a.lo*b.lo,a.lo*b.hi,a.hi*b.lo,a.hi*b.hi]
        return IV(min(v)//S,-((-max(v))//S))
    def __truediv__(a,b):
        if b.lo<=0:raise ArithmeticError('Positive denominator required')
        v=[(a.lo*S,b.lo),(a.lo*S,b.hi),(a.hi*S,b.lo),(a.hi*S,b.hi)]
        return IV(min(n//d for n,d in v),max(-((-n)//d) for n,d in v))
    def sqrt(a):
        if a.lo<0:raise ArithmeticError('Negative square root')
        lo=isqrt(a.lo*S);hi=isqrt(a.hi*S)
        return IV(lo,hi+(hi*hi<a.hi*S))
    def out(a):
        def fmt(n):
            sign='-' if n<0 else '';v=str(abs(n)).zfill(91)
            return sign+v[:-90]+'.'+v[-90:]
        return [fmt(a.lo),fmt(a.hi)]
ONE=IV.rat(1);TWO=IV.rat(2)
def elliptic(mu,N=512):
    term=ONE;K=ONE;E=ONE
    for n in range(1,N+1):
        term=term*mu*IV.rat((2*n-1)**2,(2*n)**2)
        K=K+term;E=E-term/IV.rat(2*n-1)
    nxt=term*mu*IV.rat((2*N+1)**2,(2*N+2)**2)
    tail=nxt/(ONE-mu)
    return IV(K.lo,K.hi+tail.hi),IV(E.lo-(tail/IV.rat(2*N+1)).hi,E.hi)
def log_ge_one(x,N=1024):
    if x.lo<S:raise ArithmeticError('Logarithm argument below one')
    z=(x-ONE)/(x+ONE);z2=z*z;term=z;sm=z
    for n in range(1,N):term=term*z2;sm=sm+term/IV.rat(2*n+1)
    tail=term*z2/(IV.rat(2*N+1)*(ONE-z2))
    return IV(2*sm.lo,2*(sm.hi+tail.hi))
def profile(mu,t=None):
    K,E=elliptic(mu)
    T=TWO*(E/((ONE-mu)*K)-ONE)
    density=log_ge_one(ONE/mu)/TWO
    J=(t if t is not None else T)*density+TWO*log_ge_one(K)
    w=mu.sqrt();r=(ONE-w)/(ONE+w)
    return T,J,density,r
def bracket(fn,lo=IV.rat(1,20).lo,hi=IV.rat(13,20).hi,width=10**35):
    start=[fn(IV(lo)).out(),fn(IV(hi)).out()]
    if not (fn(IV(lo)).hi<0 and fn(IV(hi)).lo>0):raise ArithmeticError('Initial signs')
    count=0
    while hi-lo>width:
        mid=(lo+hi)//2;v=fn(IV(mid));count+=1
        if v.hi<0:lo=mid
        elif v.lo>0:hi=mid
        else:raise ArithmeticError('Insufficient precision')
    return IV(lo,hi),count,start

# New certificate: complete integrated profile, not a native-period sample.
mu1,_,_=bracket(lambda z:profile(z)[0]-ONE,width=10**30)
muH,_,_=bracket(lambda z:profile(z)[0]-IV.rat(1,2),width=10**30)
_,J1,_,_=profile(mu1,ONE);_,JH,_,_=profile(muH,IV.rat(1,2))
L=224
a=[F(1)]
for n in range(1,L+1):a.append(a[-1]*F((2*n-1)**2,(2*n)**2))
coef=[F(0)]*(L+1)
for n in range(1,L+1):coef[n]=4*n*a[n]-sum(coef[j]*a[n-j] for j in range(1,n))
squared=[sum((coef[j]*coef[n-j] for j in range(1,n)),F(0)) for n in range(L+1)]
power=ONE;integral=IV.rat(0)
for n in range(1,L+1):
    power=power*mu1
    c=squared[n]/n
    integral=integral+IV.rat(c.numerator,c.denominator)*power
ratio=mu1/IV.rat(4,5);rpower=ONE
for j in range(L+1):rpower=rpower*ratio
tail=IV.rat(1152,L+1)*rpower/(ONE-ratio)
integral=IV(integral.lo-tail.hi,integral.hi+tail.hi)
area=J1-log_ge_one(ONE/mu1)/IV.rat(4)-integral/IV.rat(4)
half=JH/J1
def contain(v,lo,hi):
    if not(IV.dec(lo).hi<v.lo and v.hi<IV.dec(hi).lo):raise ArithmeticError((v.out(),lo,hi))
contain(area,'0.436944268921521509525169751272','0.436944268921521509525169751273')
contain(half,'0.697083979657197470191113447667','0.697083979657197470191113447668')
result={'all_passed':True,'exact_identity_count':len(checks),'exact_checks':checks,
'new_outward_interval_checks':2,'integrated_J':area.out(),'half_cutoff_fraction':half.out(),
'arithmetic':'Integer interval scale10^90; exact rational degree224 Taylor division; analytic Cauchy tail at radius4/5.',
'scope':'Universal elliptic scalar and finite auxiliary identities. No original-period numerical matrix evaluation.',
'negative_controls':[]}
try:
    contain(area,'0.436944268921521509525169751273','0.436944268921521509525169751274')
except ArithmeticError:result['negative_controls'].append('shifted integrated interval rejected')
else:raise ArithmeticError('negative control accepted')
(P/'CONNECTION_VERIFICATION.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'all_passed':True,'exact':len(checks),'intervals':2,'negative_controls':1,'area':area.out()},indent=2))
