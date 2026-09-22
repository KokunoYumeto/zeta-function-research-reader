"""Exact coordinate and form checks for the original escaping heat family."""
from pathlib import Path
import json
import sympy as S
x,y,W,r,h,s=S.symbols('x y W r h s')
F=S.Matrix([(1+x*y)**3*W+y*y*(1+x*y)*(4+3*x*y),
 y+3*x*(1+x*y)**2*W+3*x*y*y*(4+3*x*y),2*x-3*x*x*y-x**3*W])
checks={}
def check(name,vals):
    vals=list(vals) if isinstance(vals,(list,tuple,S.MatrixBase)) else [vals]
    checks[name]=all(S.cancel(v)==0 for v in vals)
    assert checks[name],(name,vals)
check('constant_jacobian',F.jacobian([x,y,W]).det()+2)
target=S.Matrix([-S.Rational(1,4),0,0])
for i,point in enumerate([(0,0,-S.Rational(1,4)),(1,-S.Rational(3,2),S.Rational(13,2)),(-1,S.Rational(3,2),S.Rational(13,2))]):
    check('original_point_'+str(i),F.subs(dict(zip((x,y,W),point)))-target)
check('entire_inverse_chart',F.subs({x:-1/(2*r),y:3*r,W:26*r*r})-S.Matrix([-r*r,0,0]))
check('source_reflection',F.subs({x:-x,y:-y},simultaneous=True)-S.diag(1,-1,-1)*F)
u=S.Rational(1,4)-2*h
L=S.Matrix([[0,u],[1,0]])
G=S.diag(2,-2*u)
check('multiplication_relation',L*L-u*S.eye(2))
check('reflected_adjoint',L.T*G+G*L)
T=S.Matrix([[S.Rational(1,2),S.Rational(1,2)],[-1,1]])
check('endpoint_isometry',T.T*G.subs(h,0)*T-S.Matrix([[0,1],[1,0]]))
check('moving_pole_polynomial',(s-S.Rational(1,2))**2-u-(s*(s-1)+2*h))
q0=s*(s-1); qh=q0+2*h
check('logarithmic_correction',S.diff(q0/qh,s)/(q0/qh)-(S.diff(q0,s)/q0-S.diff(qh,s)/qh))
result={'status':'PASS','checks':checks,'exact_field':'rational function arithmetic over Q',
 'scope':'Coordinate, involution, pairing, and rational completion identities; no numerical RH claim.'}
Path(__file__).with_name('ENDPOINT_HEAT_BRIDGE_CHECKS.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result,indent=2))
