"""Exact independent checks of the coefficient extension and full signed action.

The companion TeX proves the ring, conductor, metric and limiting assertions.
The checker does not promote a finite sample to a general proof.
"""
from pathlib import Path
from itertools import combinations
import hashlib
import json
import sympy as s

HERE = Path(__file__).resolve().parent
BASE = HERE.parent
A, B, C, D, P, W, r, lam = s.symbols('A B C D P W r lambda')
checks = []

def zero(name, value):
    seq = list(value) if isinstance(value, (s.MatrixBase, list, tuple)) else [value]
    bad = [str(s.factor(v)) for v in seq if s.cancel(v) != 0]
    checks.append({'name': name, 'entries': len(seq), 'passed': not bad})
    if bad:
        raise AssertionError((name, bad))

def exact(name, result):
    checks.append({'name': name, 'entries': 1, 'passed': bool(result)})
    if not result:
        raise AssertionError(name)

f = P**3 + P**2/A + B*P/A + 4*C/(5*A)
relD = D**3 - C*D**2/(5*A) + B*C**2*D/(25*A) - 4*C**4/(625*A)
zero('defining cubic under D=-CP/5', s.rem(relD.subs(D, -C*P/5), f, P))
coeff = {B:A*W-P-A*P**2, C:-5*A*P*W/4, D:A*P**2*W/4}
zero('retained P equation', f.subs(coeff, simultaneous=True))
zero('coefficient defining equation', relD.subs(coeff, simultaneous=True))
zero('W inverse', (B+P+A*P**2).subs(coeff, simultaneous=True)/A-W)
K = s.diag(1, -C/5, C**2/25)
zero('inclusion determinant', K.det()+C**3/125)
aa, bb, cc = s.symbols('a b c')
x = aa+C*bb*P+C**2*cc*P**2
xp = s.Poly(s.rem(P*x, f, P), P)
zero('conductor first multiplication coefficients',
     [xp.nth(0)+4*C**3*cc/(5*A), xp.nth(1)-aa+B*C**2*cc/A,
      xp.nth(2)-C*bb+C**2*cc/A])
xp2 = s.Poly(s.rem(P**2*x, f, P), P)
zero('conductor second multiplication coefficient',
     xp2.nth(2)-(aa-C*bb/A+C**2*cc*(1/A**2-B/A)))

nu = s.Matrix([A, coeff[B], coeff[C], coeff[D]])
Jnu = nu.jacobian([A,P,W])
Jdisplay = s.Matrix([[1,0,0],[W-P**2,-1-2*A*P,A],
                    [-5*P*W/4,-5*A*W/4,-5*A*P/4],
                    [P**2*W/4,A*P*W/2,A*P**2/4]])
zero('full coefficient Jacobian', Jnu-Jdisplay)
minors = [Jnu[list(rows),:].det() for rows in combinations(range(4),3)]
expected = [5*A*(2*A*P**2+A*W+P)/4,
            -A*P*(2*A*P**2+2*A*W+P)/4,
            5*A**2*P**2*W/16,-5*A**2*P**4*W/16]
zero('all four maximal minors', [a-b for a,b in zip(minors,expected)])
zero('L0 exact kernel', Jnu.subs({P:0,W:0})*s.Matrix([0,A,1]))
zero('L1 exact kernel', Jnu.subs({P:-1/(2*A),W:0})*s.Matrix([0,1,0]))
exact('L0 rank two', Jnu.subs({P:0,W:0}).rank()==2)
exact('L1 rank two', Jnu.subs({P:-1/(2*A),W:0}).rank()==2)
h = A*r**4+r**3+B*r**2+C*r+D
hnu = h.subs(coeff, simultaneous=True)
h0 = s.factor(hnu.subs({P:0,W:0}))
h1 = s.factor(hnu.subs({P:-1/(2*A),W:0}))
zero('L0 full quartic', h0-r**3*(A*r+1))
zero('L1 full quartic', h1-A*r**2*(r+1/(2*A))**2)
zero('L0 length-six derivative', s.rem(s.diff(h0,r),r**3,r)-3*r**2)
zero('L0 two signed values', s.diff(h0,r).subs(r,-1/A)+1/A**2)
eps=s.symbols('epsilon')
for root in [0,-1/(2*A)]:
    zero('L1 complete derivative at '+str(root),
         s.rem(s.diff(h1,r).subs(r,root+eps),eps**2,eps)-eps/(2*A))

MD = s.Matrix([[0,0,4*C**4/(625*A)],[1,0,-B*C**2/(25*A)],[0,1,C/(5*A)]])
PN = s.Matrix([[0,0,-4*C/(5*A)],[1,0,-B/A],[0,1,-1/A]])
M = s.Matrix([[0,0,-4*C**3/(125*A)],[-5/C,0,B*C/(5*A)],[0,-5/C,-1/A]])
L = s.Matrix([[-5*B/(4*C),-C/5,0],[25/(4*C**2),0,-C/5],[-125*A/(4*C**3),0,0]])
zero('M equals -5MD/C', M+5*MD/C)
zero('left inverse', M*L-s.eye(3))
zero('right inverse', L*M-s.eye(3))
zero('regular parameter intertwining', PN*K-K*M)
zero('D intertwining', (-C*PN/5)*K-K*MD)
zero('unchanged P characteristic cubic', M.charpoly(lam).as_expr()-f.subs(P,lam))
zero('M determinant', M.det()+4*C/(5*A))
zero('inverse determinant', L.det()+5*A/(4*C))

X = s.Matrix([[0,0,0,-D/A],[1,0,0,-C/A],[0,1,0,-B/A],[0,0,1,-1/A]])
Z = (4*A*X**3+3*X**2+2*B*X+C*s.eye(4)).applyfunc(s.cancel)
Zdisplay = s.Matrix([
    [C,-4*D,D/A,D*(2*A*B-1)/A**2],
    [2*B,-3*C,-(4*A*D-C)/A,(2*A*B*C+A*D-C)/A**2],
    [3,-2*B,-(3*A*C-B)/A,-(4*A**2*D-2*A*B**2-A*C+B)/A**2],
    [4*A,-1,-(2*A*B-1)/A,-(3*A**2*C-3*A*B+1)/A**2]])
zero('every displayed derivative multiplication entry', Z-Zdisplay)
zero('original quartic root relation', A*X**4+X**3+B*X**2+C*X+D*s.eye(4))
zero('root and derivative commute', X*Z-Z*X)
X8=s.diag(X,X)
Y8=s.BlockMatrix([[s.zeros(4),Z],[s.eye(4),s.zeros(4)]]).as_explicit()
zero('full signed relation', Y8**2-s.diag(Z,Z))
zero('root and sign commute', X8*Y8-Y8*X8)
K24=s.kronecker_product(K,s.eye(8))
M24=s.kronecker_product(M,s.eye(8))
allactions=[]
for name,Q in [('root',X8),('sign',Y8)]:
    Q0=Q.subs(D,0)
    Q1=Q.diff(D)
    zero(name+' action is fully affine in D', Q-Q0-D*Q1)
    QS=s.kronecker_product(s.eye(3),Q0)+s.kronecker_product(MD,Q1)
    QN=s.kronecker_product(s.eye(3),Q0)+s.kronecker_product(-C*PN/5,Q1)
    zero(name+' full 24-coordinate inclusion square', K24*QS-QN*K24)
    zero(name+' full 24-coordinate parameter commutant', M24*QS-QS*M24)
    allactions.append(QS)
zero('full 24-coordinate root/sign commutator', allactions[0]*allactions[1]-allactions[1]*allactions[0])
N=s.Matrix([[0,0,0],[-5,0,0],[0,-5,0]])
zero('pole residue', (C*M).applyfunc(s.cancel).subs(C,0)-N)
zero('inverse cubic leading coefficient', (C**3*L).applyfunc(s.cancel).subs(C,0)-s.Matrix([[0,0,0],[0,0,0],[-125*A/4,0,0]]))
exact('all residue ranks', [s.kronecker_product(N**k,s.eye(8)).rank() for k in [1,2,3]]==[16,8,0])
exact('boundary inclusion rank', K24.subs(C,0).rank()==8)
zero('full inclusion determinant', K.det()**8-C**24/5**24)

x,z,w,xb,zb,wb,t=s.symbols('x z w xb zb wb t')
u=s.Matrix([x,z,w]); ub=s.Matrix([[xb,zb,wb]])
Q=u*ub+s.diag(t,t,0)
rr=x*xb+z*zb+w*wb; qq=w*wb
zero('full finite singular polynomial', Q.charpoly(lam).as_expr()-(lam-t)*(lam**2-(rr+t)*lam+t*qq))
zero('quadratic strict-order evaluation', (lam**2-(rr+t)*lam+t*qq).subs(lam,t)+t*(x*xb+z*zb))
aabs,babs,cabs=s.symbols('aabs babs cabs',positive=True)
qabs=15625*aabs**2/(16*cabs**6)
rabs=25*babs**2/(16*cabs**2)+625/(16*cabs**4)+qabs
tabs=cabs**2/25
delta=cabs**2/(25*aabs**2)+babs**2*cabs**4/(625*aabs**2)+16*cabs**8/(390625*aabs**2)
zero('complete finite-bound error', (rabs+tabs)/qabs-1-delta)
zero('three-dimensional absolute determinant squared', tabs**2*qabs-25*aabs**2/(16*cabs**2))
for j in range(25):
    nj=(min(j,8),min(max(j-8,0),8),max(j-16,0))
    exact('exterior exponent identity degree '+str(j),
          nj[0]-nj[2]==min(j,8,24-j) and nj[1]+nj[2]==max(j-8,0))
zero('full exterior constant matches determinant',
     (125*aabs/4)**8*5**s.Integer(-16)-(5*aabs/4)**8)

# Exact finite combinatorial check: every possible count of the three
# entry types, with no numerical choices of any metric or coefficient.
for j in range(25):
    exponents=[np-nm for np in range(9) for nz in range(9) for nm in range(9)
               if np+nz+nm==j]
    exact('sharp cross-receiver subset exponent degree '+str(j),
          max(exponents)==min(j,8,24-j))
aco,bco,alpha,theta,gamma=s.symbols('aco bco alpha theta gamma', positive=True)
zero('one-block two-entry comparison to ab',
     alpha*bco*gamma**2-aco*bco*gamma**2-bco*(alpha-aco)*gamma**2)
zero('one-block two-entry comparison to b squared',
     alpha*bco*gamma**2-bco**2*gamma**2-bco*(alpha-bco)*gamma**2)
zero('one-block full product equality',
     (aco*theta*gamma)*(bco*gamma)*(bco*gamma/theta)-aco*bco**2*gamma**3)

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

out={
    'status':'PASS',
    'groups':len(checks),
    'scalar_entries':sum(c['entries'] for c in checks),
    'checks':checks,
    'review_tex_sha256':sha(HERE/'ES_TOTAL_EXTENSION_REVIEW.tex'),
    'review_md_sha256':sha(HERE/'ES_TOTAL_EXTENSION_REVIEW.md'),
    'checker_sha256':sha(Path(__file__)),
    'root_source_sha256':sha(BASE/'ES_COEFFICIENT_TOTAL_EXTENSION_BODY.tex'),
    'root_source_reading':'Complete ET1–39, including ET28a and ET37–39; checked against independent ETR1–31.',
    'scope':'Exact identities above; ring and conductor necessity, positivity, metrics, ordering, and all limiting statements proved in companion TeX.'
}
(HERE/'ES_TOTAL_EXTENSION_REVIEW.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:out[k] for k in ['status','groups','scalar_entries','review_tex_sha256','root_source_sha256']},indent=2))
