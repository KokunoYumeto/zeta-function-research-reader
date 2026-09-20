"""Exact independent tests for ISR and the complete PS1--25 source.

No floating-point calculations, network access, or external process launches.
The TeX contains the proofs; this checks symbolic identities and complete
finite examples, retaining source hashes and every original matrix entry.
"""
from pathlib import Path
from hashlib import sha256
from itertools import combinations
import json
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
checks = []
scalar_entries = 0

def exact(name, value):
    global scalar_entries
    vals = list(value) if isinstance(value, s.MatrixBase) else list(value) if isinstance(value, (list, tuple)) else [value]
    failures = [str(v) for v in vals if s.cancel(v) != 0]
    if failures:
        raise AssertionError((name, failures[:4]))
    scalar_entries += len(vals)
    checks.append({"name": name, "entries": len(vals), "passed": True})

def claim(name, actual, expected):
    global scalar_entries
    if actual != expected:
        raise AssertionError((name, actual, expected))
    scalar_entries += 1
    checks.append({"name": name, "entries": 1, "passed": True, "actual": actual})

def vp(q, p):
    a, b = map(int, s.Rational(q).as_numer_denom())
    if not a:
        raise ValueError("Zero has no finite valuation")
    ans = 0
    while a % p == 0:
        a //= p
        ans += 1
    while b % p == 0:
        b //= p
        ans -= 1
    return ans

def modp(q, p):
    a, b = map(int, s.Rational(q).as_numer_denom())
    return (a * pow(b, -1, p)) % p

def smith_exponents(M, p):
    den = s.ilcm(*[s.denom(x) for x in M])
    N = M * den
    assert all(x.q == 1 for x in N)
    D = smith_normal_form(N, domain=ZZ)
    return sorted(vp(D[j, j], p)-vp(den, p) for j in range(M.rows))

def encoded(M):
    return [[str(M[i,j]) for j in range(M.cols)] for i in range(M.rows)]

def arithmetic(roots, A, p):
    r = s.symbols("r")
    f = s.Poly(s.prod(r-a for a in roots), r)
    ds = [A * s.prod(roots[i]-roots[j] for j in range(4) if j != i) for i in range(4)]
    bs = [vp(d,p) for d in ds]
    ms = [b//2 for b in bs]
    es = [b-2*m for b,m in zip(bs,ms)]
    us = [d/s.Integer(p)**b for d,b in zip(ds,bs)]
    V = s.Matrix([[a**j for j in range(4)] for a in roots])
    Q = s.Matrix.hstack(*[s.Matrix(list(reversed(s.Poly(s.prod(r-a for j,a in enumerate(roots) if j != i),r).all_coeffs()))) for i in range(4)])
    Cp = s.diag(V,s.diag(*[s.Integer(p)**m for m in ms])*V)
    GI = s.diag(A*Q*s.diag(*[s.Integer(p)**m for m in ms]),A*Q)
    c = [s.Integer(p)**m*d for m,d in zip(ms,ds)]
    Ho = s.diag(*[1/v for v in c])
    Bo = s.BlockMatrix([[s.zeros(4),Ho],[Ho,s.zeros(4)]]).as_explicit()
    He = V.T*s.diag(*[1/d for d in ds])*V
    Be = s.BlockMatrix([[s.zeros(4),He],[He,s.zeros(4)]]).as_explicit()
    To = s.diag(2*s.eye(4),2*s.diag(*[s.Integer(p)**e*u for e,u in zip(es,us)]))
    Te = s.diag(2*V.T*V,2*V.T*s.diag(*ds)*V)
    aa = list(reversed(f.all_coeffs()))
    Z = s.Matrix([[0,0,0,-aa[0]],[1,0,0,-aa[1]],[0,1,0,-aa[2]],[0,0,1,-aa[3]]])
    Lh = A*(4*Z**3+3*aa[3]*Z**2+2*aa[2]*Z+aa[1]*s.eye(4))
    Msig = s.BlockMatrix([[s.zeros(4),Lh],[s.eye(4),s.zeros(4)]]).as_explicit()
    return locals()

# Entire symbolic self-duality matrix, in the original coefficient order.
a0,a1,a2,a3=s.symbols('a0 a1 a2 a3')
l=[0,0,0,1,-a3,a3**2-a2,-a3**3+2*a3*a2-a1]
H=s.Matrix(4,4,lambda i,j:l[i+j])
J=s.Matrix([[a1,a2,a3,1],[a2,a3,1,0],[a3,1,0,0],[1,0,0,0]])
exact('ISR10 both complete symbolic inverse products',[*(H*J-s.eye(4)),*(J*H-s.eye(4))])
exact('ISR10 determinant Hf',H.det()-1)

# Both original FS13 signs: t is arbitrary and the formula holds for every t.
A,B,r,t=s.symbols('A B r t', nonzero=True)
a=1/t; y=-r-s.I*t; z=A*t**3+2*r*t+3*s.I*t**2
w=7*s.I*r**2*t+(B-17*r+A*r**2)*t**2-13*s.I*t**3-2*A*t**4
bb=s.I+a*y; cc=-s.I+2*a*y+a*a*z
dd=-s.I*y-a*(s.I*z+2*y*y)-a*a*y*z
ee=2*z-7*s.I*y*y+a*w
ff=s.I*w+3*s.I*y**3-4*y*z+a*(6*s.I*y*y*z+w*y+4*y**4)+2*a*a*y**3*z
P=s.Matrix([a*cc,a*ee+bb*dd,a*ff+bb*ee,bb*ff])
target=s.Matrix([A,B,t*t-4*A*r**3-3*r*r-2*B*r,3*A*r**4+2*r**3+B*r*r-r*t*t])
exact('ISR27 full original polynomial factor map, both signs P(q)',P-target)
exact('ISR27 negative sign separately',(P-target).subs(t,-t))

examples=[]
claim('ISR24 actual defining prime 1201 is prime',bool(s.isprime(1201)),True)
for ex,roots in enumerate([(1201,306,16218,1082101),(1201,306,21618,61251)],1):
    p=1201; A=-s.Rational(1,sum(roots)); d=arithmetic(roots,A,p)
    V,Q,Cp,GI,Bo,Be,To,Te,Msig=[d[k] for k in ('V','Q','Cp','GI','Bo','Be','To','Te','Msig')]
    ds,bs,ms,es,us=[d[k] for k in ('ds','bs','ms','es','us')]
    h=s.Poly(A*d['f'].as_expr(),d['r']); coef=h.all_coeffs()
    exact(f'witness{ex} original ES equation',4*s.prod(roots[1:])-p*(roots[1]*roots[2]+roots[1]*roots[3]+roots[2]*roots[3]))
    exact(f'witness{ex} full labelled inverse evaluation',V*Q-s.diag(*[di/A for di in ds]))
    exact(f'witness{ex} full integral conductor image',Cp*GI-s.diag(*d['c'],*d['c']))
    exact(f'witness{ex} full residue congruence',Cp.T*Bo*Cp-Be)
    exact(f'witness{ex} full trace congruence',Cp.T*To*Cp-Te)
    exact(f'witness{ex} residue to trace multiplier',Be*(2*Msig**3)-Te)
    exact(f'witness{ex} complete M_sigma square',Msig**2-s.diag(d['Lh'],d['Lh']))
    exact(f'witness{ex} complete residue duality conductor matrix',Cp.inv()*Bo.inv()-Be.inv()*Cp.T)
    exact(f'witness{ex} determinant formulas', [Q.det()-V.det(),Cp.det()-V.det()**2*s.Integer(p)**sum(ms),GI.det()-A**8*V.det()**2*s.Integer(p)**sum(ms),Te.det()-256*A**4*V.det()**6,Be.det()-A**-8])
    expected_smith=[0,0,0,0,0,0,1,1] if ex==1 else [0,0,0,1,1,2,2,3]
    claim(f'witness{ex} every O/E Smith factor',smith_exponents(Cp,p),expected_smith)
    claim(f'witness{ex} every E/I Smith factor',smith_exponents(GI,p),expected_smith)
    claim(f'witness{ex} exact derivative valuations',bs,[1,0,0,1] if ex==1 else [2,0,2,2])
    claim(f'witness{ex} exact complete unit residues',[modp(u,p) for u in us],[75,93,581,1126] if ex==1 else [850,42,640,449])
    claim(f'witness{ex} field and split square classes',[int(s.legendre_symbol(modp(u,p),p)) for u in us],[1,-1,-1,1] if ex==1 else [-1,1,1,-1])
    claim(f'witness{ex} exact coefficient residues',[modp(x,p) for x in coef],[410,1,100,0,0] if ex==1 else [522,1,0,0,0])
    claim(f'witness{ex} full length duality',2*sum(vp(c,p) for c in d['c']),2*sum(expected_smith))
    D0=coef[4]; C0=coef[3]; B0=coef[2]
    Kcoef=s.diag(1,-C0/5,C0*C0/25)
    PiP=s.kronecker_product(s.Matrix([[1,p,p*p]]),s.eye(8))
    PiD=s.kronecker_product(s.Matrix([[1,D0,D0*D0]]),s.eye(8))
    exact(f'witness{ex} PS14 complete rank24-to-rank8 specialization',PiP*s.kronecker_product(Kcoef,s.eye(8))-PiD)
    exact(f'witness{ex} PS14 normalization specialization',Cp*PiP*s.kronecker_product(Kcoef,s.eye(8))-Cp*PiD)
    exact(f'witness{ex} PS14 full cubic relation',p**3+p*p/A+B0*p/A+4*C0/(5*A))
    exact(f'witness{ex} PS14 coefficient cubic',625*A*D0**3-125*C0*D0**2+25*B0*C0**2*D0-4*C0**4)
    kerP=s.BlockMatrix([[-p*s.eye(8),-p*p*s.eye(8)],[s.eye(8),s.zeros(8)],[s.zeros(8),s.eye(8)]]).as_explicit()
    kerD=s.BlockMatrix([[-D0*s.eye(8),-D0*D0*s.eye(8)],[s.eye(8),s.zeros(8)],[s.zeros(8),s.eye(8)]]).as_explicit()
    exact(f'witness{ex} PS15 complete kernel bases',[*(PiP*kerP),*(PiD*kerD)])
    claim(f'witness{ex} PS15 both kernel ranks',[kerP.rank(),kerD.rank()],[16,16])
    claim(f'witness{ex} PS16 exact coefficient conductor containment',2*vp(C0,p)>=max(3*m+e for m,e in zip(ms,es)),True)
    examples.append({'roots':list(roots),'coefficients':[str(x) for x in coef],'D_i':[str(x) for x in ds],'b_i':bs,'m_i':ms,'epsilon_i':es,'full_units':[str(x) for x in us],'C_p':encoded(Cp),'G_I':encoded(GI),'residue_E':encoded(Be),'residue_O':encoded(Bo),'trace_E':encoded(Te),'trace_O':encoded(To),'index_length':sum(expected_smith),'conductor_branch_exponents':[3*m+e for m,e in zip(ms,es)],'Smith_O/E':expected_smith,'Smith_E/I':expected_smith})

# Complete Smith factors on all strata through n=8, by exact integer SNF.
# These are deliberately valuation-pattern examples, not asserted ES witnesses.
for n in range(9):
    p=13
    roots=(0,p,1,2 if n==0 else 1+p**n)
    d=arithmetic(roots,s.Integer(5),p)
    expected=sorted([0,0,1,1,0,n//2,n,n+n//2])
    claim(f'ISR16 full one-pair valuation stratum n={n}',smith_exponents(d['Cp'],p),expected)
    claim(f'ISR16 dual ideal full stratum n={n}',smith_exponents(d['GI'],p),expected)
    exact(f'ISR16 index expression n={n}',sum(expected)-(2+3*n-n%2))
    claim(f'PS16 one-divisible criterion n={n}',2>=max(3*m+e for m,e in zip(d['ms'],d['es'])),n<=1)
for n in range(1,9):
    p=13
    roots=(0,1,p,2*p if n==1 else p+p**n)
    d=arithmetic(roots,s.Integer(5),p);m=(n+1)//2
    expected=sorted([0,0,0,1,1,m+1,n+1,n+m+1])
    claim(f'ISR17 complete closer triple stratum n={n}',smith_exponents(d['Cp'],p),expected)
    claim(f'ISR17 dual ideal full stratum n={n}',smith_exponents(d['GI'],p),expected)
    exact(f'ISR17 index expression n={n}',sum(expected)-(3*n+6-(n+1)%2))
    claim(f'PS16 two-divisible criterion n={n}',4>=max(3*a+e for a,e in zip(d['ms'],d['es'])),n<=2)

# p|S original fractional lattice and shifted twist. These are labelled
# quartics testing the chart identities, not asserted positive ES witnesses.
for k in range(1,7):
    p=13
    # Force S=p^k*(a unit), while preserving precisely the one pair pattern.
    roots=(p,1,p**k-1-3*p,2*p)
    claim(f'ISR18 nonunit chart vS={k}',vp(sum(roots),p),k)
    A=-s.Rational(1,sum(roots));d=arithmetic(roots,A,p)
    mu=(-k)//2;nu=(1-k)//2
    expected=sorted([0,0,0,1,mu,mu,nu,nu+1])
    claim(f'ISR20 all fractional Smith exponents k={k}',smith_exponents(d['Cp'],p),expected)
    claim(f'ISR18 original negative derivative valuations k={k}',d['bs'],[1-k,-k,-k,1-k])
    shifted=tuple(a-1 for a in roots);As=-s.Rational(1,sum(roots)-4)
    ds=arithmetic(shifted,As,p);ratio=s.Rational(sum(roots),sum(roots)-4)
    exact(f'ISR21 all four literal derivative twist units k={k}',[v-ratio*u for v,u in zip(ds['ds'],d['ds'])])
    exact(f'ISR23 exact maximal-basis scalar valuations k={k}',[s.Rational(k,2)+m0-m1-s.Rational(e1-e0,2) for m0,m1,e0,e1 in zip(d['ms'],ds['ms'],d['es'],ds['es'])])
    claim(f'ISR18 original sigma not integral k={k}',min(d['bs'])<0,True)

# All local nilpotent ranks, no omitted complementary directions.
for m in range(2,9):
    N=s.zeros(m)
    for j in range(m-1):N[j+1,j]=1
    Ms=s.BlockMatrix([[s.zeros(m),s.Integer(7)*N**(m-1)],[s.eye(m),s.zeros(m)]]).as_explicit()
    claim(f'ISR29 complete local ranks m={m}',[(Ms**j).rank() for j in range(1,5)],[m+1,2,1,0])
    claim(f'ISR29 root action ranks m={m}',[(s.diag(N,N)**j).rank() for j in range(m+1)],[2*max(m-j,0) for j in range(m+1)])

# Full arbitrary receiving Gram PS25, with complex coefficient retained.
d,db=s.symbols('d db');den=1+d*db+d*d*db*db
G=s.Matrix(8,8,lambda i,j:s.Symbol(f'g_{i}_{j}'))
Pi=s.kronecker_product(s.Matrix([[1,d,d*d]]),s.eye(8))
Zmin=s.kronecker_product(s.Matrix([1,db,db*db]),s.eye(8))/den
Zminstar=s.kronecker_product(s.Matrix([[1,d,d*d]]),s.eye(8))/den
ker=s.BlockMatrix([[-d*s.eye(8),-d*d*s.eye(8)],[s.eye(8),s.zeros(8)],[s.zeros(8),s.eye(8)]]).as_explicit()
exact('PS25 every prescribed-vector constraint',Pi*Zmin-s.eye(8))
exact('PS25 complete full-kernel orthogonality with arbitrary Gram',Zminstar*s.diag(G,G,G)*ker)
exact('PS25 full attained Gram identity',Zminstar*s.diag(G,G,G)*Zmin-G/den)
claim('ISR31 explicit residue root -3 at 1201',pow(60,2,1201),1198)
claim('ISR31 exact first-witness cofactor square root residue',modp(s.Rational(-7263764196750,549913)/(1201*3),1201),25)

sources={}
for p in [HERE/'INTEGRAL_SIGNED_REVIEW.tex',HERE/'INTEGRAL_SIGNED_REVIEW.md',ROOT/'PRIME_SPECIALIZATION_BODY.tex',ROOT/'defining_prime_intake_20260920'/'DEFINING_PRIME_RECEIVED.md',ROOT/'ES_COEFFICIENT_TOTAL_EXTENSION_BODY.tex']:
    sources[p.name]=sha256(p.read_bytes()).hexdigest()
receipt={'status':'PASS','proof_locators':'ISR1--34 including ISR13a; independent review of PS1--25','source_sha256':sources,'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'groups':len(checks),'scalar_entries':scalar_entries,'checks':checks,'complete_witness_matrices':examples,'scope':'Exact finite arithmetic and original coefficient morphisms. Tests do not claim a new Frobenius action, RH conclusion, or a p-adic interpretation of complex Gamma metrics.'}
(HERE/'INTEGRAL_SIGNED_REVIEW.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'PASS','groups':len(checks),'scalar_entries':scalar_entries,'source_sha256':sources},indent=2))
