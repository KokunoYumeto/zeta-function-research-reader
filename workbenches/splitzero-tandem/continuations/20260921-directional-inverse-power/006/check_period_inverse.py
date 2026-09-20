"""Exact field identities for PIN1--14, retaining the full original matrices."""
from pathlib import Path
import sympy as s,itertools,json,hashlib
B=Path(__file__).resolve().parent
b,e,q,d,g=s.symbols('beta eta q delta gamma')
phi=q**4+q**3+q**2+q+1
def red(x):return s.rem(s.Poly(s.expand(x),q),s.Poly(phi,q)).as_expr()
checks=[]
def equal(name,x,y):
    r=s.cancel(x-y)
    num,den=s.fraction(r)
    assert red(num)==0,(name,r)
    checks.append(name)
def Rn(n):
    R=s.zeros(4)
    for a in range(1,5):
        for k in range(4):
            deg=5*n+k+1-a
            for h0 in range(max(0,deg//4+1)):
                pp=deg-4*h0
                if pp<0 or pp%2:continue
                p=pp//2;ell=p+h0-n
                assert ell>=0
                R[a-1,k]+=b**p*e**h0*(-5)**ell*s.rf(s.Rational(a,5),ell)/(3**p*s.factorial(p)*s.factorial(h0))
    return R
R=[Rn(k) for k in range(3)]
S=[R[0].inv()]
for n in range(1,3):S.append((-S[0]*sum((R[k]*S[n-k] for k in range(1,n+1)),s.zeros(4))).applyfunc(s.expand))
for n in range(3):
    A=sum((S[k]*R[n-k] for k in range(n+1)),s.zeros(4))-(s.eye(4) if n==0 else s.zeros(4))
    for k,x in enumerate(A):equal(f'inverse {n}/{k}',x,0)
Q=s.Matrix([[0,0,1,0],[0,-1,0,b],[1,0,-b,0],[0,b,0,e-b*b]])
roots=[d+s.I*g,d-s.I*g,-d+s.I*g,-d-s.I*g]
V=s.Matrix([[r**k for k in range(4)] for r in roots])
B0=s.Matrix([[0,0,0,s.Rational(1,2)],[0,0,-s.Rational(1,2),0],[0,-s.Rational(1,2),0,0],[s.Rational(1,2),0,0,0]])
QQ=V.T*B0*V-4*s.I*d*g*Q.subs({b:2*(g*g-d*d),e:(g*g+d*d)**2})
for k,x in enumerate(QQ):equal(f'original quadric {k}',x,0)
L=[];M=[]
for j in range(1,5):
    qq=q**((-j)%5)
    D=s.diag(*[q**((-j*a)%5) for a in range(1,5)])
    T=[sum((S[r]*D*R[n-r] for r in range(n+1)),s.zeros(4)).applyfunc(red) for n in range(3)]
    def coeff(k,n):
        return red(sum((T[r][:,a].T*Q*T[n-r][:,k-a])[0]/(s.factorial(a)*s.factorial(k-a))
                       for a in range(k+1) for r in range(n+1)))
    lj=coeff(0,2);mj=coeff(1,1)
    equal(f'factor {j} L',lj,-b*b*(b*b-9*e)*(qq**3+2*qq**2+3*qq-1)/81)
    equal(f'factor {j} M',mj,b*b*qq**3*(qq-1)*(2*qq**2+2*qq+1)/9)
    for k in range(4):equal(f'factor {j} boundary {k}',coeff(k,0),0)
    for k,n in [(0,1),(1,2),(2,1),(3,2)]:equal(f'factor {j} parity {k}/{n}',coeff(k,n),0)
    L.append(lj);M.append(mj)
C0=125*b**8*(b*b-9*e)**4/81**4;h=9/(b*b-9*e)
prod=[]
for k in range(4):
    c=red(sum(s.prod(M[j] if j in inds else L[j] for j in range(4)) for inds in itertools.combinations(range(4),k)))
    prod.append(c)
    equal(f'product coefficient {k}',c,C0*[1,-2*h,2*h*h,-h**3][k])
tt=s.symbols('t')
gg=[prod[0],-s.I*prod[1],-prod[2],s.I*prod[3]]
rec=[1/gg[0]]
for n in range(1,4):rec.append(s.cancel(-sum(gg[k]*rec[n-k] for k in range(1,n+1))/gg[0]))
dd=[1,-2*s.I*h,-2*h*h,s.I*h**3]
for k in range(4):equal(f'reciprocal {k}',rec[k],dd[k]/C0)
T=s.Matrix(4,4,lambda i,j:dd[j-i] if j>=i else 0)
for k,want in enumerate([s.I*h**3,2*h**4,s.I*h**3,1],1):
    equal(f'corner minor {k}',T[:k,4-k:].det(),want)
    scores=[(8*k+sum(J)-sum(I),I,J) for I in itertools.combinations(range(4),k) for J in itertools.combinations(range(4),k)]
    top=max(z[0] for z in scores)
    assert top==8*k+k*(4-k)
    assert sum(z[0]==top for z in scores)==1
    checks.append(f'unique maximal exterior pole {k}')
equal('original B strictly negative expression',(b*b-9*e).subs({b:2*(g*g-d*d),e:(g*g+d*d)**2}),-5*g**4-26*d*d*g*g-5*d**4)
out={'status':'PASS','exact_identity_count':len(checks),'checks':checks,
 'proof_sha256':hashlib.sha256((B/'PERIOD_INVERSE_BODY.tex').read_bytes()).hexdigest(),
 'inverse_exterior_poles':[11,20,27,32],'inverse_singular_poles':[11,9,7,5],
 'scope':'Universal symbolic coefficient identities and unique-minor maximization. Complete convergence and norm proofs are PIN1--14; no finite-period zero is claimed.'}
(B/'PERIOD_INVERSE_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='checks'},indent=2))
