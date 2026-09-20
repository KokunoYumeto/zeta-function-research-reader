"""Exact finite checks for CG9--11 and CG24--27; no actual-period numerics."""
import json
from pathlib import Path
import sympy as s

BASE = Path(__file__).resolve().parent
y = s.symbols('y', real=True)
checks = []

def ok(name, truth):
    if truth is not True and truth != s.true:
        raise AssertionError(name)
    checks.append(name)

def gamma_gram(n):
    # Every entry is divided by the same retained mass sqrt(2*pi).
    # The common mass cancels in each verified inequality and ratio.
    p = [s.Integer(1), y]
    for j in range(1, 2*n):
        p.append(s.expand(y*p[-1] - j*(s.Rational(2*j-1,2))*p[-2]))
    moments = [s.Integer(1)]
    for j in range(1, 2*n+1):
        coeff = s.Poly(p[j], y)
        moments.append(-sum(coeff.nth(a)*moments[a] for a in range(j)))
    return s.Matrix(n+1,n+1,lambda i,j:moments[i+j]),p

def positive_definite(a):
    a=a.applyfunc(s.expand)
    if a != a.conjugate().T:
        return False
    return all(s.det(a[:j,:j]) > 0 for j in range(1,a.rows+1))

for d in range(1,9):
    gram,p = gamma_gram(d+1)
    gd = gram[:d+1,:d+1]
    deriv = s.zeros(d+1)
    for j in range(1,d+1):
        deriv[j-1,j] = j
    bd2 = (2*d+1)*s.harmonic(d)**2
    ok(f'derivative norm squared degree {d}',
       positive_definite(bd2*gd - deriv.T*gd*deriv))
    for n in range(1,d+1):
        rhs = sum((-1)**((a-1)//2)*s.factorial(n)*p[n-a]
                  /(a*s.factorial(n-a)) for a in range(1,n+1,2))
        ok(f'derivative identity d={d} n={n}',s.expand(s.diff(p[n],y)-rhs)==0)
    for z in [s.Integer(0),s.Integer(2),s.Rational(-3,2)+s.I/3]:
        mult = s.zeros(d+2,d+1)
        for j in range(d+1):
            mult[j,j]=-z
            mult[j+1,j]=1
        lower2 = 1/(4*(2*d+3)*s.harmonic(d+1)**2)
        ok(f'linear factor lower degree {d} root {z}',
           positive_definite(mult.conjugate().T*gram*mult-lower2*gd))

for g,t in [(1,2),(2,3),(3,4)]:
    n=g+t-1
    gram,_=gamma_gram(n)
    polynomial=y**g + sum(s.Rational((-1)**j,j+2)*y**j for j in range(g))
    low=s.eye(n+1)[:,:g]
    ideal=s.Matrix(n+1,t,lambda i,j:s.Poly(polynomial*y**j,y).nth(i))
    frame=low.row_join(ideal)
    h=frame.T*gram*frame
    a,b,d=h[:g,:g],h[:g,g:],h[g:,g:]
    # Include the actual structural constraint F(1)=0.
    f=s.Matrix(g,t,lambda i,j:0 if j==0 else s.Rational((i+1)*(j+2),i+j+3))
    c=s.eye(t)
    for j in range(1,t):
        c[j,j]=s.Rational(j+3,3)
        c[j-1,j]=s.Rational(j,7)
    graph=s.Matrix.vstack(f,s.eye(t))*c
    ug=graph.T*h*graph
    qd=a-b*d.inv()*b.T
    relation=d+b.T*f+f.T*b+f.T*a*f
    qu=a-(a*f+b)*relation.inv()*(f.T*a+b.T)
    ok(f'full quotient determinant g={g}',
       s.cancel(qu.det()/qd.det()-c.det()**2*d.det()/ug.det())==0)
    quotient=s.eye(g).row_join(-f)
    ok(f'actual quotient covariance g={g}',
       s.simplify(qu.inv()-quotient*h.inv()*quotient.T)==s.zeros(g))
    j=s.eye(g+t)
    j[:g,g:]=-f
    transported=j.inv().T*h*j.inv()
    tq=transported[:g,:g]-transported[:g,g:]*transported[g:,g:].inv()*transported[g:,:g]
    ok(f'complete transformed shear metric g={g}',s.simplify(tq-qu)==s.zeros(g))
    if g>1:
        ek=s.eye(g)[:,:g-1]
        ar=s.eye(g)[g-1:,:]
        restricted=(ek.T*qu*ek).det()/(ek.T*qd*ek).det()
        covariance=(ar*qu.inv()*ar.T).det()/(ar*qd.inv()*ar.T).det()
        ok(f'unchanged kernel and complementary invariant receiver g={g}',
           s.cancel(restricted-qu.det()/qd.det()*covariance)==0)

# A determinant-only negative control: the same full volume can move
# between two fixed low directions. This is not an actual-period fixture.
a=s.eye(2); b=s.Matrix([s.Rational(3,5),0]); d=s.ones(1)
f=s.Matrix([-s.Rational(3,5),s.Rational(3,5)])
qd=a-b*b.T
den=d+b.T*f+f.T*b+f.T*a*f
qu=a-(a*f+b)*den.inv()*(f.T*a+b.T)
ok('negative control equal full determinants',qd.det()==qu.det())
ok('negative control different first restriction',qd[0,0]!=qu[0,0])
report={
 'status':'passed', 'checks':len(checks),'details':checks,
 'scope':'Exact Gamma polynomial identities and finite graph minima; no original-period asymptotic sampling',
 'mass':'Every auxiliary rational Gram is the original Gamma Gram divided by its common sqrt(2*pi) mass; all checked comparisons are invariant under that common scalar.',
 'excluded':'CG24 asymptotic proof is analytic in GRAPH_METRIC_DERIVATION.md. This checker does not evaluate the actual restricted kernel allocation CG28.'
}
(BASE/'GRAPH_METRIC_EXACT_CHECKS.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':report['status'],'checks':len(checks)}))
