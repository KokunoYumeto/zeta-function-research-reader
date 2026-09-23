from pathlib import Path
import json
import sympy as s
c,d,u=s.symbols('c d u',real=True)
checks=[]
def check(name,e):
    assert s.expand(e)==0,(name,e)
    checks.append(name)
for m in range(1,9):
    x=s.Symbol('x')
    p=s.Poly(sum((-1)**a*s.factorial(m)*x**(m-2*a)/(s.factorial(a)*s.factorial(m-2*a)) for a in range(m//2+1)),x)
    C=s.zeros(m)
    for j in range(m-1):C[j+1,j]=1
    for j in range(m):C[j,m-1]=-p.nth(j)
    moments=[s.trace(C**n) for n in range(2*m+1)]
    # Full prescribed arithmetic c,d are symbolic; this is the proven
    # branch expansion through cubic order, not an actual-zero sample.
    r=s.Symbol('r')
    theta=u*r+2*c*u*u+(2*d-c*c)*u**3*r
    for j in range(1,m):
        # Coefficients through degree 2j+2 use only these exact terms.
        polynomial=s.Poly(s.expand(theta**(2*j)),r)
        value=s.expand(sum(coefficient*moments[power[0]] for power,coefficient in polynomial.terms()))
        check(f'm={m},j={j}: first response',value.coeff(u,2*j)-moments[2*j])
        check(f'm={m},j={j}: odd cancellation',value.coeff(u,2*j+1))
        expected=2*j*(2*d-c*c)*moments[2*j]+4*j*(2*j-1)*c*c*moments[2*j-2]
        check(f'm={m},j={j}: next arithmetic response',value.coeff(u,2*j+2)-expected)
    G=s.Matrix(m,m,lambda i,j:moments[i+j])
    check(f'm={m}: full boundary determinant',G.det()-2**(m*(m-1)//2)*s.prod(s.Integer(j)**j for j in range(1,m+1)))
    check(f'm={m}: both original cokernel stages',m*(m-1)//2-2*((m-1)**2//4)-m//2)
check('m2 original arithmetic coordinate coefficient',s.Rational(1,4)*(2*(2*d-c*c)*4+4*c*c*2)-4*d)
record={'scope':'Exact auxiliary Hermite companion-matrix and symbolic c,d identities for HF1-16. Complete analytic proofs are in HEAT_TRACE_FLAG_RESPONSE.tex; no arithmetic zero is numerically certified.','count':len(checks),'all_passed':True,'checks':checks}
Path(__file__).with_name('HEAT_TRACE_FLAG_CHECKS.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'count':len(checks),'all_passed':True}))
