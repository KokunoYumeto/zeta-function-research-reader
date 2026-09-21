"""Exact finite checks for OFM1--17; the general proof is the companion TeX.

Direct translation of recurrence polynomials is independent of the proposed
Toeplitz representation. Cyclotomic checks use Q(i)[zeta]/Phi_5 exactly.
Samples of auxiliary real matrices test the conjugation identity, not an
assertion that those matrices are actual finite-period matrices.
"""
from pathlib import Path
from hashlib import sha256
from math import factorial
import json
import argparse
import sympy as s

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
I = s.I
checks = []
entries = 0

def ck(name, values):
    global entries
    values = list(values) if isinstance(values, (list, tuple, s.MatrixBase)) else [values]
    for value in values:
        reduced = s.cancel(s.expand_complex(value))
        assert reduced == 0, (name, reduced)
    entries += len(values)
    checks.append({'name': name, 'entries': len(values), 'passed': True})

delta, gamma = s.Rational(1, 5), s.Integer(3)
rho = [s.Rational(1, 2)+delta+I*gamma,
       s.Rational(1, 2)+delta-I*gamma,
       s.Rational(1, 2)-delta+I*gamma,
       s.Rational(1, 2)-delta-I*gamma]
pairs = [(u, w) for u in range(3) for w in range(3)]
nodes = [1+(2*u-2)*delta+I*(2*w-2)*gamma for u, w in pairs]
V9 = s.Matrix([[z**n for z in nodes] for n in range(9)])
detprod = s.prod(nodes[j]-nodes[i] for i in range(9) for j in range(i+1, 9))
ck('nine-frequency Vandermonde determinant', V9.det(method='domain-ge')-detprod)
assert detprod != 0
sharp = [s.cancel(1/s.prod(nodes[j]-nodes[k] for k in range(9) if k != j)) for j in range(9)]
ck('full nine-node inverse jet certificate', V9*s.Matrix(sharp)-s.Matrix([0]*8+[1]))

B0 = s.Matrix([[0,0,0,s.Rational(1,2)], [0,0,-s.Rational(1,2),0],
               [0,-s.Rational(1,2),0,0], [s.Rational(1,2),0,0,0]])
M = s.Matrix([[1,2,0,1],[0,1,1,0],[0,0,1,3],[0,0,0,1]])
C = M.T*B0*M
alpha, beta = (1,1,0,0), (1,0,1,0)
coeff = [sum(C[a,b] for a in range(4) for b in range(4)
             if alpha[a]+alpha[b] == u and beta[a]+beta[b] == w)
         for u,w in pairs]
Z,W = s.symbols('Z W', real=True)
tv = s.Matrix([Z*W,Z,W,1])
ck('ordered pairs versus quadratic substitution', (tv.T*C*tv)[0]-sum(c*Z**u*W**w for c,(u,w) in zip(coeff,pairs)))
for n in range(10):
    ck(f'quadratic derivative {n}', sum(C[a,b]*(rho[a]+rho[b])**n for a in range(4) for b in range(4))-sum(c*z**n for c,z in zip(coeff,nodes)))

# Exact cyclotomic arithmetic with polynomial remainders over Q(i).
zeta = s.symbols('zeta')
modulus = s.Poly(1+zeta+zeta**2+zeta**3+zeta**4,zeta,extension=I)
def red(x):
    return s.rem(s.Poly(s.expand(x),zeta,extension=I),modulus).as_expr()
def mr(A):
    return A.applyfunc(red)
def star(x):
    terms = s.Poly(x,zeta,extension=I).all_terms()
    return red(sum(s.conjugate(c)*zeta**((-power[0]) % 5) for power,c in terms))
def ms(A):
    return A.applyfunc(star)
J = s.Matrix([[0,1,0,0],[1,0,0,0],[0,0,0,1],[0,0,1,0]])
V = s.Matrix([[(r-s.Rational(1,2))**k for k in range(4)] for r in rho])
unit = 2+3*I
U = s.diag(unit,s.conjugate(unit),s.conjugate(unit),unit)
ck('original quartet conjugation', s.conjugate(V)-J*V)
ck('original unit conjugation', s.conjugate(U)-J*U*J)
ck('quadric label-conjugation sign', J.T*B0*J+B0)
real_beta = 2*(gamma**2-delta**2)
Rlim = s.Matrix([[1,0,-real_beta/3,0],[0,1,0,-2*real_beta/3],[0,0,1,0],[0,0,0,1]])
for label,R in [('actual_coefficient_limit',Rlim),('auxiliary_real_matrix',s.Matrix([[1,2,0,0],[0,1,1,0],[0,0,1,3],[0,0,0,1]]))]:
    L = U.inv()*V*R.inv()
    ck(label+' L conjugation', s.conjugate(L)-J*L)
    Q = []
    for j in range(1,5):
        Dj = s.diag(*[zeta**((-j*k)%5) for k in range(1,5)])
        Mj = mr(L*Dj*L.inv())
        Q.append(mr(Mj.T*B0*Mj))
    for j in range(4):
        defect = mr(J.T*ms(Q[j])*J+Q[3-j])
        ck(label+f' factor conjugation {j+1}', defect)

# Build genuinely independent translation matrices in recurrence-polynomial
# quotient frames, including nonzero offsets at all intermediate stages.
S = s.symbols('S', real=True)
def moment(cs,n):
    return s.cancel(sum(c*z**n for c,z in zip(cs,nodes)))
def prescribed_order(n,scale):
    chosen = nodes[:n+1]
    return [s.cancel(scale/s.prod(z-t for t in chosen if t != z)) if j <= n else s.Integer(0)
            for j,z in enumerate(nodes)]
def psi_polys(maxdegree,b,center):
    y = (S-center)/I
    p = [s.Integer(1),y]
    for n in range(1,maxdegree):
        p.append(s.expand(y*p[-1]-n*(n-1+b)*p[-2]))
    return [s.expand(p[n]/factorial(n)) for n in range(maxdegree+1)]
def translation(poly,cs):
    return s.Poly(s.expand(sum(c*poly.subs(S,S+z) for c,z in zip(cs,nodes) if c)),S).as_expr()
def basis_coeff(poly,basis):
    rem = s.Poly(poly,S)
    ans = [s.Integer(0)]*len(basis)
    for k in reversed(range(len(basis))):
        bk = s.Poly(basis[k],S)
        ans[k] = s.cancel(rem.nth(k)/bk.nth(k))
        rem = s.Poly(s.expand(rem.as_expr()-ans[k]*bk.as_expr()),S)
    assert rem.is_zero
    return s.Matrix(ans)
def exponential_at_omega(beta,N):
    # y(t)=exp(beta*(-i arctan t)); y'=beta*(-i)/(1+t^2)*y.
    ans = [s.Integer(1)]
    for n in range(N):
        ans.append(s.cancel(beta*(-I)*sum((-1)**k*ans[n-2*k] for k in range(n//2+1))/(n+1)))
    return ans
def G_coeff(cs,n,D):
    expansions = [exponential_at_omega(z-1,n+D) for z in nodes]
    full = [s.cancel(sum(c*e[k] for c,e in zip(cs,expansions))) for k in range(n+D+1)]
    ck(f'factor removable zero order {n}',full[:n])
    return full[n:]
def toeplitz(gs,D):
    return s.Matrix(D+1,D+1,lambda r,q:gs[q-r] if q>=r else 0)
def conv(a,b,D):
    return [s.cancel(sum(a[k]*b[n-k] for k in range(n+1) if k<len(a) and n-k<len(b))) for n in range(D+1)]

for orders in [(0,1,2,3),(2,0,1,0)]:
    D = 2
    v = sum(orders)
    coeffs = [prescribed_order(n,2+j+I*(j+1)) for j,n in enumerate(orders)]
    r = [sum(orders[j:]) for j in range(5)]
    a = [[moment(cs,n) for n in range(v+D+1)] for cs in coeffs]
    for j,n in enumerate(orders):
        ck(f'{orders} factor {j+1} vanished jets',a[j][:n])
        assert a[j][n] != 0
    mu = [s.Integer(1)]+[s.Integer(0)]*(v+D)
    for aj in a:
        mu = conv(mu,[aj[k]/factorial(k) for k in range(v+D+1)],v+D)
    mu = [s.cancel(x*factorial(n)) for n,x in enumerate(mu)]
    ck(f'{orders} product initial jets',mu[:v])
    ck(f'{orders} exact leading moment',mu[v]-factorial(v)*s.prod(a[j][orders[j]]/factorial(orders[j]) for j in range(4)))
    Gs = [G_coeff(cs,n,D) for cs,n in zip(coeffs,orders)]
    fullG = [s.Integer(1)]+[s.Integer(0)]*D
    for gs in Gs:
        fullG = conv(fullG,gs,D)
    for b in [s.Rational(1,2),s.Rational(9,2)]:
        center = s.Rational(13,2)
        stage_matrices=[]
        for j in range(4):
            source = psi_polys(D+r[j],b,center-j)
            target = psi_polys(D+r[j+1],b,center-j-1)
            cols=[]
            for q in range(D+1):
                translated = translation(source[r[j]+q],coeffs[j])
                fullcoeff = basis_coeff(translated,target)
                cols.append(fullcoeff[r[j+1]:,0])
            direct=s.Matrix.hstack(*cols)
            ck(f'{orders} b={b} direct factor {j+1}',direct-toeplitz(Gs[j],D))
            weights_in=s.diag(*[s.sqrt(s.factorial(r[j]+q)/s.rf(b,r[j]+q)) for q in range(D+1)])
            weights_out=s.diag(*[s.sqrt(s.factorial(r[j+1]+q)/s.rf(b,r[j+1]+q)) for q in range(D+1)])
            stage_matrices.append(weights_out.inv()*direct*weights_in)
        product=stage_matrices[3]*stage_matrices[2]*stage_matrices[1]*stage_matrices[0]
        win=s.diag(*[s.sqrt(s.factorial(v+q)/s.rf(b,v+q)) for q in range(D+1)])
        wout=s.diag(*[s.sqrt(s.factorial(q)/s.rf(b,q)) for q in range(D+1)])
        total=wout.inv()*toeplitz(fullG,D)*win
        ck(f'{orders} b={b} weighted product including offsets',product-total)
        ck(f'{orders} b={b} determinant',total.det()-fullG[0]**(D+1)*s.prod(win[q,q]/wout[q,q] for q in range(D+1)))
        inverse=[1/fullG[0]]
        for n in range(1,D+1):
            inverse.append(s.cancel(-sum(fullG[k]*inverse[n-k] for k in range(1,n+1))/fullG[0]))
        ck(f'{orders} b={b} weighted inverse',total*(win.inv()*toeplitz(inverse,D)*wout)-s.eye(D+1))

# Independent convolution and positive leading moment on an exact conjugate
# pair of nonzero exponential factors. This checks the factorial constant.
left=[prescribed_order(2,1+2*I),prescribed_order(3,2-I)]
left_jets=[[moment(cs,n) for n in range(13)] for cs in left]
g=[s.cancel(sum(s.binomial(n,k)*left_jets[0][k]*left_jets[1][n-k] for k in range(n+1))) for n in range(13)]
E=[s.cancel(sum(s.binomial(n,k)*g[k]*s.conjugate(g[n-k]) for k in range(n+1))) for n in range(13)]
ck('real-period model moments are real',[s.im(x) for x in E])
ck('real-period paired order',E[:10])
ck('real-period exact positive leading constant',E[10]-s.binomial(10,5)*g[5]*s.conjugate(g[5]))
assert E[10]>0

parser = argparse.ArgumentParser()
parser.add_argument('--source-dir', action='append', default=[],
                    help='Additional directory containing an exact source dependency.')
options = parser.parse_args()
search_dirs = [ROOT, ROOT/'source_dependencies', HERE, HERE/'source_dependencies']
search_dirs += [Path(p) for p in options.source_dir]
def source_file(name):
    for folder in search_dirs:
        candidate = folder/name
        if candidate.is_file():
            return candidate
    raise FileNotFoundError('Exact source dependency unavailable: '+name)
sources = [source_file(name) for name in
    ['ORIGINAL_FACTOR_MOMENT_BODY.tex','FABLE_TO_ORIGINAL_CONDUCTOR.tex',
     'WEIGHTED_CONDUCTOR_FORWARD.tex','ORIGINAL_CONDUCTOR_COPRIMALITY.tex',
     'PCL_COMPLETE.tex']]
result={'status':'passed','groups':len(checks),'entries':entries,'checks':checks,
        'sources':[{'name':p.name,'sha256':sha256(p.read_bytes()).hexdigest()} for p in sources],
        'scope':'Exact finite certificates supplement the complete general proof. Auxiliary matrices and prescribed jet samples are not claimed to be actual finite periods.'}
(HERE/'OFM_INDEPENDENT_REVIEW.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':result['status'],'groups':len(checks),'entries':entries}))
