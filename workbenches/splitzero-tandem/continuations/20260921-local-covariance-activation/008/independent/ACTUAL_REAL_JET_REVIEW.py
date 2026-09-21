"""Independent actual marked receiver and exact Bernstein positivity audit."""
from pathlib import Path
from hashlib import sha256
import json
import sympy as s

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
d,g,v=s.symbols('delta gamma v',real=True)
X,t,h,z=s.symbols('X t h z',real=True)
rt=s.sqrt(2)
I=s.I
checks=[]
entries=0
def ck(name,values):
    global entries
    values=list(values) if isinstance(values,(s.MatrixBase,list,tuple)) else [values]
    for value in values:
        assert s.cancel(s.expand(value))==0,(name,value)
    entries+=len(values)
    checks.append({'name':name,'entries':len(values),'passed':True})

roots=[s.Rational(1,2)+d+I*g,s.Rational(1,2)+d-I*g,
       s.Rational(1,2)-d+I*g,s.Rational(1,2)-d-I*g]
K=s.Matrix([[0,I,1/rt,1/rt],[0,-1,-1-rt*I,1-rt*I],
            [I/2,-3*I,2*rt+6*I,-2*rt+6*I],[0,13,-34-19*rt*I,34-19*rt*I]])
Kinv=K.inv().applyfunc(lambda x:s.simplify(s.expand_complex(x)))
ck('literal K inverse',K*Kinv-s.eye(4))
assert s.simplify(K.det()-77*rt*I/2)==0

# Solve interpolation by exact barycentric polynomials, retaining S=1/2+w.
ell=[s.Poly(s.prod(X-r for j,r in enumerate(roots) if j!=a),X)
     for a in range(4)]
derivatives=[s.prod(roots[a]-r for j,r in enumerate(roots) if j!=a) for a in range(4)]
coeff=[s.factor(s.cancel(sum(Kinv[a,0]*ell[a].nth(q)/derivatives[a] for a in range(4)))) for q in range(4)]
for a,r in enumerate(roots):
    ck(f'first interpolation column at label {a}',sum(c*r**q for q,c in enumerate(coeff))-Kinv[a,0])

real=lambda x:s.factor(s.cancel(s.expand_complex(x).as_real_imag()[0]))
imag=lambda x:s.factor(s.cancel(s.expand_complex(x).as_real_imag()[1]))
C=s.Matrix([[real(c) for c in coeff],[imag(c) for c in coeff],
            [real((v+q+1)*coeff[q+1]) if q<3 else 0 for q in range(4)],
            [imag((v+q+1)*coeff[q+1]) if q<3 else 0 for q in range(4)]])
root=json.loads((ROOT/'ACTUAL_REAL_JET_DERIVATION.json').read_text())
scope={'delta':d,'gamma':g,'v':v,'sqrt':s.sqrt,'I':I}
claimed=s.Matrix([[s.sympify(c,locals=scope) for c in row] for row in root['real_jet_matrix']])
ck('all actual jet matrix entries independently reconstructed',C-claimed)

# Fraction-field determinant after exact common-denominator clearing.
common=4928*d*g*(d*d+g*g)
cleared=C.applyfunc(lambda x:s.cancel(x*common))
det=s.cancel(cleared.det(method='domain-ge')/common**4)
sign=json.loads((ROOT/'ACTUAL_REAL_JET_SIGN.json').read_text())
F=s.sympify(sign['F'],locals=scope)
den=s.sympify(sign['denominator'],locals=scope)
ck('determinant against full claimed numerator',det*den-F)
assert s.Poly(F,d,g,v).degree_list()==(4,4,2)

# Convert both bounded variables to Bernstein bases independently.
expanded=s.Poly(s.expand(F.subs({d:t/2,g:2+h,v:32*z})),t,z,h)
Bc={}
for a in range(5):
    for b in range(3):
        for k in range(5):
            Bc[a,b,k]=s.expand(sum(expanded.coeff_monomial(t**i*z**j*h**k)
                                  *s.binomial(a,i)/s.binomial(4,i)
                                  *s.binomial(b,j)/s.binomial(2,j)
                                  for i in range(a+1) for j in range(b+1)))
reconstructed=sum(c*s.binomial(4,a)*t**a*(1-t)**(4-a)
                  *s.binomial(2,b)*z**b*(1-z)**(2-b)*h**k
                  for (a,b,k),c in Bc.items())
ck('entire Bernstein polynomial reconstruction',reconstructed-expanded.as_expr())
claimed_B=json.loads((ROOT/'ACTUAL_REAL_JET_BERNSTEIN.json').read_text())
for row in claimed_B['coefficients']:
    a,b=row['a'],row['b']
    ck(f'Bernstein row {a},{b}',[Bc[a,b,k]-s.sympify(c) for k,c in enumerate(row['c'])])

# No decimal sign test. 7/5 < sqrt(2) < 10/7 follows by squaring.
assert s.Rational(7,5)**2<2<s.Rational(10,7)**2
certificates=[]
for (a,b,k),c in Bc.items():
    A=s.expand(c).coeff(rt,0)
    B=s.expand(c).coeff(rt,1)
    ck(f'rational radical decomposition {a},{b},{k}',c-A-B*rt)
    lower=s.factor(A+B*(s.Rational(7,5) if B>=0 else s.Rational(10,7)))
    assert lower>0,(a,b,k,c,lower)
    certificates.append({'a':a,'b':b,'k':k,'A':str(A),'B':str(B),'rational_lower_bound':str(lower)})
table=[[min(s.Rational(c['rational_lower_bound']) for c in certificates if c['a']==a and c['b']==b) for b in range(3)] for a in range(5)]

# The moment translation and derivative are checked symbolically for each
# actual allowed integer v; the companion proof establishes every integer.
mus=s.symbols('mu0:4',real=True)
for nv in (0,1,2,16,31,32):
    eta=[sum(s.binomial(nv+q,r)*mus[q-r]*X**r for r in range(q+1)) for q in range(4)]
    ck(f'exact shifted-moment derivative v={nv}',[s.diff(eta[q],X)-(nv+q)*eta[q-1] for q in range(1,4)])
    ck(f'original leading moment retained v={nv}',eta[0]-mus[0])

receipt={'status':'passed','groups':len(checks),'entries':entries,'checks':checks,
         'F':str(F),'denominator':str(den),
         'bernstein_coefficients':certificates,
         'minimum_rational_lower_bound':str(min(s.Rational(c['rational_lower_bound']) for c in certificates)),
         'lower_bound_table':[[str(x) for x in row] for row in table],
         'sources':[{'name':p.name,'sha256':sha256(p.read_bytes()).hexdigest()} for p in
                   [ROOT/'ACTUAL_REAL_JET_DERIVATION.json',ROOT/'ACTUAL_REAL_JET_SIGN.json',ROOT/'ACTUAL_REAL_JET_BERNSTEIN.json',ROOT/'FABLE_TO_ORIGINAL_CONDUCTOR.tex']],
         'scope':'Exact symbolic reconstruction and rational sign certificates, no numerical positivity inference.'}
(HERE/'ACTUAL_REAL_JET_REVIEW.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'status':'passed','groups':len(checks),'entries':entries,'minimum_rational_lower_bound':receipt['minimum_rational_lower_bound'],'lower_bound_table':receipt['lower_bound_table']}))
