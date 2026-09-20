"""Exact finite-root Jacobian, inverse and all exterior leading matrices."""
from pathlib import Path
import itertools
import json
import sympy as s
a,y,z,w,t,r,A,B=s.symbols('a y z w t r A B',nonzero=True)
i=s.I
P=s.Matrix([
 a**3*z+2*a**2*y-i*a,
 -a**3*y**2*z-2*i*a**2*y*z+a**2*w-2*a**2*y**3-10*i*a*y**2+3*a*z+y,
 2*a**3*y**3*z+6*i*a**2*y**2*z+2*a**2*w*y+4*a**2*y**4+2*i*a*w-4*i*a*y**3-2*a*y*z+2*i*z+7*y**2,
 2*a**3*y**4*z+8*i*a**2*y**3*z+a**2*w*y**2+4*a**2*y**5+2*i*a*w*y+7*i*a*y**4-10*a*y**2*z-4*i*y*z-w-3*y**3])
q=s.Matrix([1/t,-r-i*t,A*t**3+2*r*t+3*i*t**2,7*i*r*r*t+(B-17*r+A*r*r)*t*t-13*i*t**3-2*A*t**4])
pi=s.Matrix([A,B,t*t-4*A*r**3-3*r*r-2*B*r,3*A*r**4+2*r**3+B*r*r-r*t*t])
kap=12*A*r*r+6*r+2*B
ell=s.Matrix([[r**4,r*r,r,1]])
elp=s.Matrix([[4*r**3,2*r,1,0]])
sub=dict(zip((a,y,z,w),q))
assert (P.subs(sub)-pi).applyfunc(s.expand)==s.zeros(4,1)
J=P.jacobian((a,y,z,w)).subs(sub).applyfunc(s.expand)
DQ=q.jacobian((t,r,A,B))
Dpi=pi.jacobian((t,r,A,B))
assert s.expand(DQ.det())==t**3
assert s.expand(Dpi.det())==-2*t**3
assert (J*DQ-Dpi).applyfunc(s.expand)==s.zeros(4)
assert s.expand(J.det())==-2
# Explicit root/sign differential followed by the original source differential.
dt=elp/(2*t)-kap*ell/(2*t**3)
dr=-ell/t**2
DA=s.Matrix([[1,0,0,0]]);DB=s.Matrix([[0,1,0,0]])
inv=s.Matrix.vstack(-dt/t**2,-dr-i*dt,
 t**3*DA+2*t*dr+(3*A*t*t+2*r+6*i*t)*dt,
 (r*r*t*t-2*t**4)*DA+t*t*DB+(14*i*r*t+(-17+2*A*r)*t*t)*dr
 +(7*i*r*r+2*(B-17*r+A*r*r)*t-39*i*t*t-8*A*t**3)*dt).applyfunc(s.expand)
assert (J*inv-s.eye(4)).applyfunc(s.expand)==s.zeros(4)
assert (inv*J-s.eye(4)).applyfunc(s.expand)==s.zeros(4)
v=s.Matrix([1,-r*r,-2*r**3,2*r**4]);vv=s.Matrix([0,1,-2*r,r*r])
def compound(M,k):
 ix=list(itertools.combinations(range(4),k))
 return ix,s.Matrix([[s.expand(M.extract(I,J).det()) for J in ix] for I in ix])
def matstr(M):return [[str(x) for x in row] for row in M.tolist()]
def coeff(M,p):return M.applyfunc(lambda x:s.expand(x).coeff(t,p))
rows=[]
for degree in range(1,5):
 labels,C=compound(J,degree);_,D=compound(inv,degree)
 rows.append({'rank':degree,'index_subsets':[[n+1 for n in I] for I in labels],
              'forward_compound':matstr(C),'inverse_compound':matstr(D)})
 if degree==1:
  expected=s.zeros(4);expected[:,2]=v
  assert coeff(C,-3)==expected
  assert all(not s.expand(x).coeff(t,-p) for x in C for p in range(4,10))
  expected=s.zeros(4);expected[0,:]=kap*ell/2
  assert (coeff(D,-5)-expected).applyfunc(s.expand)==s.zeros(4)
 if degree==2:
  wedge=s.Matrix([v[I[0]]*vv[I[1]]-v[I[1]]*vv[I[0]] for I in labels])
  expected=s.zeros(6);expected[:,5]=wedge
  assert (coeff(C,-5)-expected).applyfunc(s.expand)==s.zeros(6)
  expected=s.zeros(6);expected[0,:]=-s.Matrix([[2*r**5,3*r**4,4*r**3,r*r,2*r,1]])/2
  assert coeff(D,-5)==expected
  assert all(not s.expand(x).coeff(t,-p) for x in C for p in range(6,12))
  assert all(not s.expand(x).coeff(t,-p) for x in D for p in range(6,12))
 if degree==3:
  expected=s.zeros(4);expected[:,3]=kap*s.Matrix([1,-r,r*r,-r**4])
  assert (coeff(C,-5)-expected).applyfunc(s.expand)==s.zeros(4)
  expected=s.zeros(4);expected[1,:]=s.Matrix([[r**4,r**3,-r*r/2,-s.Rational(1,2)]])
  assert coeff(D,-3)==expected
  assert all(not s.expand(x).coeff(t,-p) for x in D for p in range(4,10))
 if degree==4:
  assert C==s.Matrix([[-2]]) and D==s.Matrix([[-s.Rational(1,2)]])
out={'commuting_map_Pq_equals_pi':True,'det_Dq':'t^3','det_Dpi':'-2t^3','det_DP':'-2',
 'both_inverse_products_verified':True,'full_Jacobian':matstr(J),'full_inverse_Jacobian':matstr(inv),
 'compounds':rows,'all_assertions_passed':True}
Path(__file__).with_name('finite_root_native_differential_exact.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print('Exact original Jacobian:',J)
print('All differential identities, both inverse products, and six leading compound matrices verified.')
