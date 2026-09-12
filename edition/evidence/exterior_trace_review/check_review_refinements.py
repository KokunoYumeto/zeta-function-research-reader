"""Independent small exact checks of intake refinements; algebraic fixtures, not zeta data."""
from itertools import product, permutations, combinations
import json
import sympy as s

checks = 0
def require(condition, label):
    global checks
    checks += 1
    if not bool(condition):
        raise RuntimeError(label)

def exterior_additive(A, p):
    inds=list(combinations(range(A.rows),p))
    lookup={v:i for i,v in enumerate(inds)}
    result=s.zeros(len(inds))
    for col, v in enumerate(inds):
        for j in range(p):
            for i in range(A.rows):
                w=list(v); w[j]=i
                if len(set(w)) != p: continue
                sign=(-1)**sum(w[a]>w[b] for a in range(p) for b in range(a+1,p))
                result[lookup[tuple(sorted(w))],col] += sign*A[i,v[j]]
    return result

def alt(d,p):
    tuples=list(product(range(d),repeat=p)); index={v:i for i,v in enumerate(tuples)}
    inds=list(combinations(range(d),p)); out=s.zeros(d**p,len(inds))
    for j,v in enumerate(inds):
        for w in permutations(v):
            sign=(-1)**sum(w[a]>w[b] for a in range(p) for b in range(a+1,p))
            out[index[w],j]=sign
    return out

# A four-dimensional factor, k=2, with all ordinary tensor coordinates retained.
t=s.Symbol('t'); h=t*(t-1)*(t-2)*(t-3)
def remcol(poly):
    r=s.Poly(s.rem(poly,h,t),t)
    return s.Matrix([r.nth(j) for j in range(4)])
A=s.Matrix.hstack(*[remcol(t**(j+1)) for j in range(4)])
B=s.kronecker_product(A,s.eye(4))+s.kronecker_product(s.eye(4),A)
one=s.zeros(16,1);one[0]=1
alpha=s.Matrix.hstack(*[B**j*one for j in range(7)])
U=s.kronecker_product(s.eye(4)+A,s.eye(4)+A)
eta=U*alpha
require(alpha.rank()==7, 'exact cyclic dimension for roots 0,1,2,3 and k=2')
require(U.det()!=0, 'retain invertible nonconstant arithmetic-unit fixture')
block=s.kronecker_product(eta,eta)*alt(7,2)
require(block.rank()==21, 'block exterior image injective')
tuples=list(product(range(4),repeat=4)); index={v:i for i,v in enumerate(tuples)}
swapped=block.extract([index[(v[1],v[0],v[2],v[3])] for v in tuples],range(block.cols))
require(swapped==block, 'within-block transposition fixes block exterior image')
global_alt=alt(4,4)
require(global_alt.rank()==1, 'global fourth exterior space is genuinely nonzero')
require(global_alt.T*block==s.zeros(1,21), 'global exterior quotient annihilates block exterior image')

H=s.diag(3,0,0,-3)
require(set(exterior_additive(H,2).eigenvals())=={-3,0,3}, 'rank-two no-p-factor spectrum')
Hwrong=s.diag(3,3,-3,-3)
require(6 in exterior_additive(Hwrong,2).eigenvals(), 'negative control: no-p-factor fails without rank-two hypothesis')

# Exact quartet-only threshold versus larger fixed packet at k=1.
roots=[s.Rational(1,2)+e*s.Rational(1,4)+s.I*f for e in (-1,1) for f in (-1,1)]
larger=roots+[s.Rational(1,2)]
require(len(set(larger))==5, 'larger reflection-stable fixture has q=5, not quartet q=4')
require(3 < len(larger)-1, 'negative control: quartet N=3 is inadmissible for larger q=5')

# Determinant line of a zero-dimensional space is the tensor unit.
require(exterior_additive(s.zeros(0),0)==s.zeros(1), 'degree-zero additive action is zero on scalar line')
require(s.zeros(0).det()==1, 'empty Gram determinant convention')

# Genuine form correction need not be positive when its Gram correction is.
DeltaGram=s.eye(2); Aplus=s.diag(0,2); weight=2
Wcorr=Aplus.T*DeltaGram+DeltaGram*Aplus-weight*DeltaGram
require(Wcorr==s.diag(-2,2), 'positive boundary Gram has indefinite control correction')
print(json.dumps({'status':'passed','guard_checks':checks,'negative_formula_controls':2,
                  'scope':'Exact finite refinements: block versus global exterior, nonconstant unit, rank-two necessity, actual quartet cutoff, degree zero, and indefinite control correction.'},indent=2))
