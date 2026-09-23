"""Finite exact identities and non-certified Gaussian-series tests for IS1--22."""
from pathlib import Path
import sys,json,hashlib
import sympy as s
import mpmath as mp
H=Path(__file__).resolve().parent
exact=[];numeric=[]
def check(name,test):
    if not test:raise RuntimeError('Failed: '+name)
    exact.append(name)
def near(name,a,b,tol=mp.mpf('1e-35')):
    err=abs(a-b)
    if err>tol:raise RuntimeError(name+': '+str(err))
    numeric.append(dict(name=name,absolute_error=str(err),classification='finite high-precision check, not an interval certificate'))
z,x,n,m,T=s.symbols('z x n m T',real=True)
check('Gaussian product exponent',s.expand((x-n)**2+(x-m)**2-2*(x-(n+m)/2)**2-(n-m)**2/2)==0)
for N in range(1,13):
    a={j:s.Rational(1,N) for j in range(1,N+1)}
    check('mass '+str(N),sum(a.values())==1)
    check('coefficient square '+str(N),sum(v*v for v in a.values())==s.Rational(1,N))
    for d in range(-N,N+1):
        check('pair count '+str((N,d)),sum(1 for i in a for j in a if i-j==d)==max(N-abs(d),0))
    if N%2==0:check('alternating exact zero mass '+str(N),sum((-1)**j for j in range(1,N+1))==0)
# Arbitrary exact finite sequence convolution and the sample-sum factor.
a={-2:s.Integer(2),0:s.Integer(-3),3:s.Integer(5)}
r={-1:s.Rational(1,7),0:s.Rational(3,4),1:s.Rational(1,7)}
y={j:sum(a.get(i,0)*r.get(j-i,0) for i in a) for j in range(-3,5)}
check('discrete convolution Laurent identity',s.expand(sum(v*z**j for j,v in y.items())-sum(v*z**j for j,v in a.items())*sum(v*z**j for j,v in r.items()))==0)
check('sample sum has original symbol factor',sum(y.values())==sum(a.values())*sum(r.values()))
for l in range(-8,9):
    check('half shift distance '+str(l),(s.Rational(l)+s.Rational(1,2))**2==(s.Rational(-l-1)+s.Rational(1,2))**2)
    check('half shift alternating sign '+str(l),s.Integer(-1)**l+s.Integer(-1)**(-l-1)==0)
# The two-element lattice, with coefficient space of three finite top points.
E=s.Matrix([[0,0,0,0,0],[1,1,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[0,0,0,0,0]])
# Extended coordinates are a_-1,a_0,a_1,b,m; unlike the finite graph, m is independent.
Ee=s.zeros(5);Ee[1,4]=1;Ee[3,3]=1;Ee[4,4]=1
Et=s.zeros(5);Et[3,3]=1;Et[3,4]=1
check('supported zero idempotent',Ee*Ee==Ee)
check('lower zero idempotent',Et*Et==Et)
check('meet compositions',Ee*Et==Et and Et*Ee==Et)
mp.mp.dps=60
for t in [mp.mpf('0.125'),mp.mpf('0.3')]:
    def k(v):return mp.exp(-v*v/(4*t))/mp.sqrt(4*mp.pi*t)
    def vs(xi,eta=0):return sum(k(j+eta)*mp.exp(-2j*mp.pi*j*xi) for j in range(-40,41))
    def vp(xi):return sum(mp.exp(-4*mp.pi**2*t*(xi+j)**2) for j in range(-40,41))
    for xi in [mp.mpf('0'),mp.mpf('0.13'),mp.mpf('0.5')]:
        near('original-symbol equality '+str((t,xi)),vs(xi),vp(xi))
        if mp.re(vs(xi))<mp.exp(-mp.pi**2*t):raise RuntimeError('symbol lower bound')
    near('half-shift zero '+str(t),vs(mp.mpf('.5'),mp.mpf('.5')),0)
    b={-2:mp.mpc(2,1),0:mp.mpc(-3,0),3:mp.mpc(5,-2)}
    yy={j:sum(v*k(j-i) for i,v in b.items()) for j in range(-40,41)}
    for xi in [mp.mpf('0'),mp.mpf('.21')]:
        near('sample transform '+str((t,xi)),sum(v*mp.exp(-2j*mp.pi*j*xi) for j,v in yy.items()),vs(xi)*sum(v*mp.exp(-2j*mp.pi*j*xi) for j,v in b.items()))
    near('sample sum prefactor '+str(t),sum(yy.values()),vs(0)*sum(b.values()))
    for beta in [mp.mpf('.1'),mp.mpf('.4')]:
        period=sum(sum(v*k(beta+j-i) for i,v in b.items()) for j in range(-40,41))
        theta=sum(k(beta+j) for j in range(-40,41))
        near('periodization '+str((t,beta)),period,sum(b.values())*theta)
controls=[]
for name,test in [('missing sample-sum multiplier',sum(y.values())==sum(a.values())),('half-shift alternating sign replaced by positive',sum(k(j+mp.mpf('.5')) for j in range(-40,41))==0)]:
    if test:raise RuntimeError('Deliberate error was accepted')
    controls.append(dict(name=name,outcome='rejected'))
out=dict(exact_count=len(exact),exact_checks=exact,numerical_checks=numeric,deliberate_error_controls=controls,proof_scope='Analytic proofs are in NOTE.tex; numerical checks are not certificates',optimized=not __debug__,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(H/('CHECKS_OPTIMIZED.json' if not __debug__ else 'CHECKS.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(exact=len(exact),numerical=len(numeric),controls=len(controls),optimized=not __debug__)))
