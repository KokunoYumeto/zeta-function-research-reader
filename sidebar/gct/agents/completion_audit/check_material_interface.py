"""Independent exact checks for the new material-generator proof only."""
from pathlib import Path
import sympy as s
import hashlib,json
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
x,y,w,a,b,c,r,z=s.symbols('x y w a b c r z')
v=1+x*y
F=s.Matrix([v**3*w+y**2*v*(4+3*x*y),y+3*x*v**2*w+3*x*y**2*(4+3*x*y),2*x-3*x*x*y-x**3*w])
J=F.jacobian([x,y,w])
S=F[0]/2
checks=[]
def eq(name,left,right):
    values=list(left-right) if isinstance(left,s.MatrixBase) else [left-right]
    assert all(s.cancel(q)==0 for q in values), name
    checks.append(name)
eq('Jacobian determinant original',J.det(),-2)
U=J.inv()*s.Matrix([2,6*F[2],0])
def D(f):return sum(s.diff(f,coord)*U[i] for i,coord in enumerate((x,y,w)))
eq('material coordinate first jet',s.Matrix([D(S),D(F[1]),D(F[2])]),s.Matrix([1,6*F[2],0]))
eq('material invariant b minus 6cs',D(F[1]-6*F[2]*S),0)
eq('section pullback original s',S.subs({x:0,y:0,w:2*z}),z)
eq('s_x',s.diff(S,x),(3*y*v*v*w+y**3*(1+6*v))/2)
eq('s_y',s.diff(S,y),(3*x*v*v*w+2*y*(v+3*v*v)+x*y*y*(1+6*v))/2)
eq('s_w',s.diff(S,w),v**3/2)
eq('s_xx',s.diff(S,x,2),3*y*y*v*w+3*y**4)
eq('s_yy',s.diff(S,y,2),3*x*x*v*w+v+3*v*v+2*x*y*(1+6*v)+3*x*x*y*y)
eq('s_ww',s.diff(S,w,2),0)
A=sum(s.diff(S,coord)**2 for coord in (x,y,w))
B=sum(s.diff(S,coord,2) for coord in (x,y,w))
eq('Euclidean B expanded',B,3*w*v*(x*x+y*y)+18*x*x*y*y+21*x*y+3*y**4+4)
P=c*r**3-2*r*r+b*r-4*z
Pr=s.diff(P,r)
dr=(4-6*c*r)/Pr
eq('full root derivation respects ideal',s.diff(P,z)+6*c*s.diff(P,b)+dr*Pr,0)
eq('restricted simple root drift',dr.subs({b:0,c:0}),-1/r)
for index,point,gradient,AB in [(0,{x:1,y:-s.Rational(3,2),w:s.Rational(13,2)},s.Matrix([-s.Rational(9,32),-s.Rational(3,16),-s.Rational(1,16)]),(s.Rational(121,1024),-s.Rational(7,2))),
 (1,{x:0,y:0,w:-s.Rational(1,4)},s.Matrix([0,0,s.Rational(1,2)]),(s.Rational(1,4),4))]:
    eq('original fibre '+str(index),F.subs(point),s.Matrix([-s.Rational(1,4),0,0]))
    eq('exact gradient '+str(index),s.Matrix([s.diff(S,co) for co in (x,y,w)]).subs(point),gradient)
    eq('A and B '+str(index),s.Matrix([A.subs(point),B.subs(point)]),s.Matrix(AB))
receipt={'all_passed':True,'check_count':len(checks),'checks':checks,
 'scope':'symbolic identities; general function-space/topological proofs reviewed in TeX',
 'source_hashes':{name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in ['tex/material_generator_interface.tex','tex/conic_arithmetic_bridge.tex']}}
(HERE/'material_checks.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print(json.dumps({'all_passed':True,'checks':len(checks)}))
