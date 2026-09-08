"""Exact original-coordinate residuals for euclidean_observable.tex."""
from pathlib import Path
import hashlib
import json
import sympy as S

ROOT=Path(__file__).resolve().parents[1]
x,y,w,r,alpha,c,z=S.symbols('x y w r alpha c z')
q=(x,y,w)
F=S.Matrix([(1+x*y)**3*w+y*y*(1+x*y)*(4+3*x*y),
 y+3*x*(1+x*y)**2*w+3*x*y*y*(4+3*x*y),2*x-3*x*x*y-x**3*w])
sigma=F[0]/2
J=F.jacobian(q)
checks=[]
def exact(name,expression):
    entries=list(expression) if isinstance(expression,S.MatrixBase) else [expression]
    residual=[S.expand(S.together(v).as_numer_denom()[0]) for v in entries]
    assert all(v==0 for v in residual),(name,residual)
    checks.append({'id':name,'status':'exact_zero_residual','entries':len(entries)})

H=S.Matrix([1/alpha,r-alpha,5*alpha**2-3*r*alpha-c*alpha**3])
target=S.Matrix([r*r+r*alpha-c*r**3,4*r+2*alpha-3*c*r*r,c])
exact('inverse_chart_image',F.subs(dict(zip(q,H)),simultaneous=True)-target)
exact('inverse_chart_determinant',H.jacobian([alpha,r,c]).det()-alpha)
exact('target_chart_determinant',target.jacobian([alpha,r,c]).det()+2*alpha)
exact('original_jacobian',J.det()+2)
Q=1+x*y
g=S.Matrix([3*y*Q**2*w/2+y**3*(7+6*x*y)/2,
 3*x*Q**2*w/2+(8*y+21*x*y*y+12*x*x*y**3)/2,Q**3/2])
exact('gradient_all_coordinates',g-S.Matrix([S.diff(sigma,v) for v in q]))
L=3*w*Q*(x*x+y*y)+3*y**4+18*x*x*y*y+21*x*y+4
exact('laplacian_all_coordinates',L-sum(S.diff(sigma,v,2) for v in q))
gamma=S.Matrix([-1/(2*r),3*r,26*r*r])
on=dict(zip(q,gamma))
gr=S.Matrix([9*r**3/4,3*r/8,-S.Rational(1,16)])
exact('gradient_on_original_lift',g.subs(on,simultaneous=True)-gr)
hessian=S.Matrix([[-108*r**4,3*r*r/4,9*r/8],
 [3*r*r/4,S.Rational(13,4),-3/(16*r)],[9*r/8,-3/(16*r),0]])
exact('hessian_on_original_lift',S.hessian(sigma,q).subs(on,simultaneous=True)-hessian)
N=(1296*r**6+36*r*r+1)/256
exact('all_squared_gradient_terms',gr.dot(gr)-N)
exact('laplacian_on_lift',L.subs(on,simultaneous=True)-(S.Rational(13,4)-108*r**4))
h=S.Function('h')
s=S.symbols('s')
psi=h(sigma)
exact('full_euclidean_chain_rule',sum(S.diff(psi,v,2) for v in q)
 -g.dot(g)*S.diff(h(s),s,2).subs(s,sigma)-L*S.diff(h(s),s).subs(s,sigma))
exact('original_trajectory_image',F.subs(on,simultaneous=True)-S.Matrix([-r*r,0,0]))
exact('lift_velocity_target',J.subs(on,simultaneous=True)*(-gamma.diff(r)/r)-S.Matrix([2,0,0]))
exact('specific_material_covector',gr.subs(r,-z/2)-S.Matrix([-9*z**3/32,-3*z/16,-S.Rational(1,16)]))
exact('specific_covector_cost',N.subs(r,-z/2)-(81*z**6+36*z*z+4)/1024)
exact('specific_covector_cost_limit',S.limit(N.subs(r,-z/2),z,0)-S.Rational(1,256))
tex=ROOT/'tex/euclidean_observable.tex'
receipt={'status':'pass','check_count':len(checks),'checks':checks,
 'proof_sha256':hashlib.sha256(tex.read_bytes()).hexdigest(),
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'proof_scope':'Exact rational identities; analytic and geometric assertions proved in TeX.',
 'domains':'Rational lift requires r != 0; Euclidean norm statements require real spatial coordinates.',
 'RH_counterexample':False,'Navier_Stokes_counterexample':False,'Lean_verified':False}
(ROOT/'checks/euclidean_observable_checks.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print(json.dumps({'status':'pass','check_count':len(checks)}))
