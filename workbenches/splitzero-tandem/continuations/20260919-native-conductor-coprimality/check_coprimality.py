"""Exact algebra diagnostics for NC12--21; no xi-period numerical certificate."""
import json
from pathlib import Path
import sympy as s
from sympy.polys.matrices import DomainMatrix

checks=[]
def ck(name, value):
    if not bool(value): raise AssertionError(name)
    checks.append(name)
t,d,b,h=s.symbols('t d b h', real=True)
c=b+s.I*h
alpha=-3*t+s.I*d
L=-t+s.I*d
M=t+s.I*d
A=s.Matrix([[s.im(c),s.im(c*L)],[s.im(c*L),s.im(c*L**2)]])
B=-s.Matrix([[s.im(c*alpha),s.im(c*alpha*M)],[s.im(c*alpha*M),s.im(c*alpha*M**2)]])
ck('NC15 even determinant',s.factor(A.det()+(b*b+h*h)*d*d)==0)
ck('NC15 odd determinant',s.factor(B.det()+(b*b+h*h)*(9*t*t+d*d)*d*d)==0)
ff=[s.Integer(1),L**2,-alpha,-alpha*M**2]
expected=[[d,-d*(d*d+5*t*t)],[-d*(d*d+5*t*t),d*(d**4+6*d*d*t*t-11*t**4)]]
for i in range(2):
 for j in range(2):
  ck(f'NC16 cross identity {i},{j}',s.factor(s.im(ff[i]*s.conjugate(ff[j+2]))-expected[i][j])==0)
x=s.symbols('Y1:5')
poly=s.expand((s.Matrix([x[0],x[2]]).T*A*s.Matrix([x[0],x[2]]))[0]+(s.Matrix([x[1],x[3]]).T*B*s.Matrix([x[1],x[3]]))[0])
orig=c*((x[0]+L*x[2])**2-alpha*(x[1]+M*x[3])**2)
original_conjugate=s.conjugate(c)*((x[0]+s.conjugate(L)*x[2])**2-s.conjugate(alpha)*(x[1]+s.conjugate(M)*x[3])**2)
ck('NC12 literal full scalar 2i',s.expand(orig-original_conjugate-2*s.I*poly)==0)
ck('degree-sixteen scalar restoration',(2*s.I)**4==16)

# Independent finite-field rank witnesses certify exact rank at these rational
# fixtures over Q(zeta_5): reduction cannot increase the rational-field rank.
# Rational denominators are units in each tested field. This is not a test of
# every parameter; the manuscript supplies that proof.
tv=s.Rational(143,48)  # delta=1/4, gamma=3
dv=s.Rational(3,2)
cs=[s.Integer(1),s.I,1+s.I]+[s.conjugate(f.subs({t:tv,d:dv})) for f in ff]
fixtures=[]
for ci in cs:
 if ci not in fixtures: fixtures.append(ci)
def mod_rat(val,p):
 n,den=s.fraction(val)
 return int(n)%p*pow(int(den)%p,-1,p)%p
def rank_mod(mat,p):
 arr=[row[:] for row in mat]; r=0
 for j in range(len(arr[0])):
  pivot=next((k for k in range(r,len(arr)) if arr[k][j]%p),None)
  if pivot is None: continue
  arr[r],arr[pivot]=arr[pivot],arr[r]
  inv=pow(arr[r][j]%p,-1,p)
  arr[r]=[(a*inv)%p for a in arr[r]]
  for k in range(len(arr)):
   if k!=r:
    fac=arr[k][j]%p
    arr[k]=[(a-fac*bb)%p for a,bb in zip(arr[k],arr[r])]
  r+=1
 return r
witnesses=[]
for fi,cv in enumerate(fixtures):
 q=s.Poly(poly.subs({t:tv,d:dv,b:s.re(cv),h:s.im(cv)}),*x)
 for i in range(4):
  var=[xx for j,xx in enumerate(x) if j!=i]
  exps=[ee for ee in __import__('itertools').product(range(4),repeat=3) if sum(ee)==3]
  qi=q.as_expr().subs(x[i],0)
  for j in range(1,5):
   found=None
   for p in (101,151,181,191,211,241,251,271,281,311):
    zeta=next(rr for rr in range(2,p) if pow(rr,5,p)==1)
    trans={x[k]:pow(zeta,(-j*(k+1))%5,p)*x[k] for k in range(4)}
    qj=qi.subs(trans,simultaneous=True)
    cols=[s.Poly(xx*qq,*var) for qq in (qi,qj) for xx in var]
    mat=[[mod_rat(col.coeff_monomial(ee),p) for col in cols] for ee in exps]
    if rank_mod(mat,p)==6:
     found={'fixture':fi,'i':i+1,'j':j,'prime':p,'zeta':zeta};break
   ck(f'NC19 exact rank fixture {fi}, plane {i+1}, orbit {j}',found is not None)
   witnesses.append(found)

# Check both directions of the 10x6 rank criterion on explicit degenerate cases.
y,z,w=s.symbols('y z w')
for name,q1,q2,wanted in [('coprime',y*y+z*z+w*w,y*z+w*w,6),('shared line',y*z,y*w,5),('proportional',y*z,2*y*z,3)]:
 exps=[ee for ee in __import__('itertools').product(range(4),repeat=3) if sum(ee)==3]
 cols=[s.Poly(xx*qq,y,z,w) for qq in (q1,q2) for xx in (y,z,w)]
 mm=s.Matrix([[col.coeff_monomial(ee) for col in cols] for ee in exps])
 ck('NC19 criterion '+name,mm.rank()==wanted)
out={'status':'passed','count':len(checks),'checks':checks,'finite_field_witnesses':witnesses,'scope':'Exact algebra and rank fixtures only; the universal parameter and analytic period-domain proof is in NC12--22. No actual xi zero or numerical period is evaluated.'}
Path(__file__).with_name('COPRIMALITY_CHECKS.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({'count':len(checks),'status':'passed','rank_fixtures':len(witnesses)},indent=2))
