"""Exact finite checks of AB5, AB8--AB15; the proofs are in 06_adelic_boundary.tex."""
from itertools import combinations
from fractions import Fraction as Q
from pathlib import Path
import json
import sympy as sp

F=(2,3,5)
d=len(F)
faces=list(range(1<<(d+1)))
full=faces[-1]
exterior=list(range(1<<d))
count=0
def require(ok):
    global count
    assert ok
    count+=1
def character(A,pindex):
    exponent=((A&1)>0)-int((A&(1<<(pindex+1)))>0)
    return Q(F[pindex])**exponent
def wedge(i,S):
    if S&(1<<i):return None,0
    return S|(1<<i),(-1)**((S&((1<<i)-1)).bit_count())
def contract(i,S):
    if not S&(1<<i):return None,0
    return S^(1<<i),(-1)**((S&((1<<i)-1)).bit_count())
def delta(A,S):
    out={}
    for i in range(d):
        T,s=wedge(i,S)
        if s:out[T]=out.get(T,Q(0))+s*(character(A,i)-1)
    return {T:c for T,c in out.items() if c}
def homotopy(A,S):
    i=next((i for i in range(d) if character(A,i)!=1),None)
    if i is None:return {}
    T,s=contract(i,S)
    return {T:Q(s)/(character(A,i)-1)} if s else {}
def compose(op,vector,A):
    out={}
    for S,c in vector.items():
        for T,b in op(A,S).items():out[T]=out.get(T,Q(0))+c*b
    return out
def add(v,w):
    z=v.copy()
    for k,c in w.items():z[k]=z.get(k,Q(0))+c
    return {k:c for k,c in z.items() if c}
chars={A:tuple(character(A,i) for i in range(d)) for A in faces}
require(chars[0]==chars[full]==(Q(1),)*d)
require(len(set(chars.values()))==len(faces)-1)
for A in faces:
    require(all(chars[A][i]*chars[full^A][i]==1 for i in range(d)))
    projection=Q(1)
    for i,p in enumerate(F):
        t=chars[A][i]
        projection*=(t-p)*(t-Q(1,p))/((1-p)*(1-Q(1,p)))
    require(projection==int(A in (0,full)))
    for S in exterior:
        require(not {k:c for k,c in compose(delta,delta(A,S),A).items() if c})
        lhs=add(compose(homotopy,delta(A,S),A),compose(delta,homotopy(A,S),A))
        require(lhs==({S:Q(1)} if A not in (0,full) else {}))
    for i in range(d):
        if chars[A][i]!=1:require(abs(1/(chars[A][i]-1))<=2)
t=sp.symbols('t')
for i,p in enumerate(F):
    actual=sp.prod(1-sp.Rational(c[i].numerator,c[i].denominator)*t for c in chars.values())
    expected=(1-p*t)**(2**(d-1))*(1-t/sp.Integer(p))**(2**(d-1))*(1-t)**(2**d)
    require(sp.expand(actual-expected)==0)
H=sp.zeros(len(faces))
for A in faces:H[A,full^A]=1
require(H*H==sp.eye(len(faces)))
require(H.trace()==0)
for i in range(d):
    D=sp.diag(*(sp.Rational(chars[A][i].numerator,chars[A][i].denominator) for A in faces))
    require(D.T*H*D==H)
require(H[0,full]==H[full,0]==1 and H[0,0]==H[full,full]==0)
result={'status':'passed','exact_checks':count,'places':['infinity',*F],
        'scope':'Finite exact rational checks of the stated boundary representation and Koszul contraction. General proofs remain in AB1–19. No native zeta coefficient is certified by these checks.',
        'face_count':len(faces),'trivial_character_faces':[0,full],
        'proper_face_count':len(faces)-2,'floating_point_used':False}
(Path(__file__).parent/'BOUNDARY_VERIFICATION.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
