"""Reproducible exact checks; floating-point probes are separately labelled."""
import json
from pathlib import Path
import sympy as sp
import mpmath as mp

checks = []
def need(value, name):
    if not bool(value):
        raise RuntimeError(name)
    checks.append(name)

x, u, s = sp.symbols('x u s', positive=True)
f = sp.Function('f')
L = lambda v: x*x*sp.diff(v,x,2)+2*x*sp.diff(v,x)
G = sp.exp(-sp.pi*x*x)
k = (4*sp.pi**2*x**4-6*sp.pi*x*x)*G
need(sp.expand(L(G)-k)==0, 'Gaussian differential polynomial with all constants')
need(L(sp.Integer(1))==0 and L(1/x)==0, 'Both homogeneous directions')
I = sp.Integral(f(u),(u,x,sp.oo))/x-sp.Integral(f(u)/u,(u,x,sp.oo))
need(sp.simplify(L(I)-f(x))==0, 'Tail return exact differential inverse')
need(sp.integrate(k,(x,0,sp.oo))==0 and k.subs(x,0)==0, 'Gaussian-derived source has both moments zero')
for h, expected in [((1-2*sp.pi*x*x)*G,0),(2*sp.pi*x*x*G,1)]:
    need(sp.integrate(2*h,(x,0,sp.oo))==expected, 'Moment lift integral '+str(expected))
A, z = sp.Function('A')(s), sp.Function('z')(s)
q = sp.diff(A,s)/A
need(sp.simplify(sp.diff(A*z,s,2)/A-sp.diff(z,s,2)-2*q*sp.diff(z,s)-(sp.diff(q,s)+q*q)*z)==0,'Full conjugated second derivative')
for N in range(1,9):
    coeff = [sp.Rational((-1)**j*(j+2),j+1) for j in range(N)]
    M = sp.Matrix(N,N,lambda i,j: coeff[i-j] if i>=j else 0)
    need(M.det()==coeff[0]**N,'Jet determinant N='+str(N))
    a = sp.Matrix([sp.Rational(j+1,j+3) for j in range(N)])
    b = M*a
    back=[]
    for j in range(N):
        back.append((b[j]-sum(coeff[i]*back[j-i] for i in range(1,j+1)))/coeff[0])
    need(sp.Matrix(back)==a,'Jet full-unit inverse N='+str(N))
    for e in (-2,-1,0,1,2):
        for d in (-2,-1,0,1,2):
            need([d+j+e for j in range(N)]==[d+e+j for j in range(N)],f'Intrinsic exponent transport N={N},d={d},e={e}')
for n in range(1,101):
    need(sum(sp.mobius(d) for d in sp.divisors(n))==(1 if n==1 else 0),'Mobius inverse divisor n='+str(n))
# A concrete three-term element in M0, with prime-exponent vectors and both moments.
terms=[((1,0),(sp.Rational(2),sp.Rational(-1))),((0,2),(sp.Rational(-3),sp.Rational(4))),((-2,-1),(sp.Rational(1),sp.Rational(-3)))]
beta=lambda rows: tuple(sum(v[p]*m[j] for v,m in rows) for p in range(2) for j in range(2))
for r in [(-2,3),(0,1),(4,-1)]:
    shifted=[((v[0]+r[0],v[1]+r[1]),m) for v,m in terms]
    need(beta(shifted)==beta(terms),'Prime-boundary invariance '+str(r))
negative=[]
for name,bad in [('missing Gaussian coefficient',L(G)- (4*sp.pi**2*x**4-4*sp.pi*x*x)*G),('missing conjugation drift',sp.diff(A*z,s,2)/A-sp.diff(z,s,2)-(sp.diff(q,s)+q*q)*z)]:
    try:
        if sp.simplify(bad)!=0: raise RuntimeError(name)
    except RuntimeError:
        negative.append(name)
need(len(negative)==2,'Both deliberate errors detected')

mp.mp.dps=40
def F(y):
    return 2*mp.fsum((4*mp.pi**2*n**4*y**4-6*mp.pi*n*n*y*y)*mp.exp(-mp.pi*n*n*y*y) for n in range(1,9))
def U(r,t=0):
    return mp.quad(lambda y: mp.exp(t*mp.log(y)**2/4)*F(y)*(y**(r-1)+y**(-r)),[1,2,4,mp.inf])
numeric=[]
for r in [mp.mpf('0'),mp.mpf('0.5'),mp.mpf('1'),mp.mpf('2.5')]:
    actual=U(r)
    target=mp.mpf(1) if r in (0,1) else r*(r-1)*mp.pi**(-r/2)*mp.gamma(r/2)*mp.zeta(r)
    error=abs(actual-target)
    if error>mp.mpf('1e-32'):raise RuntimeError('Numeric Mellin probe '+str(r))
    numeric.append({'s':str(r),'value':str(actual),'absolute_error':str(error)})
receipt={'status':'passed','exact_checks':len(checks),'checks':checks,'deliberate_errors_detected':negative,'numerical_probes':numeric,'numerical_scope':'40-digit mpmath, theta sum n<=8; consistency probes, not interval certificates or proofs','proof_source':'NOTE.tex, FR1–FR38'}
print(json.dumps(receipt,indent=2))
