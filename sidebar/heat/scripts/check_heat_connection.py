"""Exact residual checks. Original input expressions are retained verbatim."""
import json
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]
s,r=sp.symbols('s r', nonzero=True)
t=sp.symbols('t')
x,y,w,a,b,c,alpha=sp.symbols('x y w a b c alpha')
Q=sp.Matrix([sp.Function('q0')(s),sp.Function('q1')(s)])
A=sp.diag(0,1/(2*s))
R=sp.Matrix([[0,-2*s],[1,0]])
I=sp.eye(2)
checks=[]
def zero(name,expr):
    entries=list(expr) if isinstance(expr,sp.MatrixBase) else [expr]
    residuals=[sp.expand(sp.together(e).as_numer_denom()[0]) for e in entries]
    assert all(e==0 for e in residuals),(name,residuals)
    checks.append({'id':name,'status':'exact_zero_residual','entries':len(entries)})
def D(v): return v.diff(s)+A*v
def nabla(M): return M.diff(s)+A*M-M*A
zero('R_square',R*R+2*s*I)
zero('D2_original_coefficients',D(D(Q))-Q.diff(s,2)-2*A*Q.diff(s)-(A.diff(s)+A*A)*Q)
zero('D2_potential',A.diff(s)+A*A-sp.diag(0,-1/(4*s*s)))
zero('D_R_commutator',D(R*Q)-R*D(Q)+R.inv()*Q)
zero('D_Rinv_commutator',nabla(R.inv())-R.inv()**3)
zero('D2_R_commutator',D(D(R*Q))-R*D(D(Q))+2*R.inv()*D(Q)+R.inv()**3*Q)
J=sp.diag(1,-1)
zero('sheet_D_equivariance',D(J*Q)-J*D(Q))
zero('sheet_R_anticommutation',J*R+R*J)
Z=sp.Function('Z')(s,t)
heat_subs={sp.diff(Z,t):-sp.diff(Z,s,2)/4}
q=sp.Matrix([Z,0])
odd=R*q
zero('actual_even_heat',q.diff(t).subs(heat_subs)+D(D(q))/4)
zero('odd_heat_defect',odd.diff(t).subs(heat_subs)+D(D(odd))/4-sp.Matrix([0,sp.diff(Z,s)/(4*s)-Z/(16*s*s)]))
G=sp.Matrix([sp.Function('g0')(s,t),sp.Function('g1')(s,t)])
product=(Z*G).diff(t)+D(D(Z*G))/4
rhs=Z*(G.diff(t)+D(D(G))/4)+sp.diff(Z,s)*D(G)/2
zero('moving_module_product',product.subs(heat_subs)-rhs)
logder=sp.diff(Z,s)/Z
covariant=product-logder*D(Z*G)/2+logder**2*Z*G/2
zero('moving_module_gauge',covariant.subs(heat_subs)-Z*(G.diff(t)+D(D(G))/4))
qscalar=sp.Function('q')(s)
def B(v): return s*v-t*sp.diff(v,s)/2
zero('B_squared',B(B(qscalar))-((s*s-t/2)*qscalar-t*s*sp.diff(qscalar,s)+t*t*sp.diff(qscalar,s,2)/4))
v=sp.symbols('v',real=True)
phi=sp.Function('phi')(v)
zero('Fourier_heat_Ms_conjugation',sp.exp(t*v*v/4)*sp.I*sp.diff(sp.exp(-t*v*v/4)*phi,v)-(sp.I*sp.diff(phi,v)-t*sp.I*v*phi/2))
F=sp.Matrix([(1+x*y)**3*w+y*y*(1+x*y)*(4+3*x*y),y+3*x*(1+x*y)**2*w+3*x*y*y*(4+3*x*y),2*x-3*x*x*y-x**3*w])
P=c*r**3-2*r*r+b*r-2*a
H=sp.Matrix([1/alpha,r-alpha,5*alpha*alpha-3*r*alpha-c*alpha**3])
FH=F.subs(dict(zip((x,y,w),H)),simultaneous=True)
target=sp.Matrix([r*r+r*alpha-c*r**3,4*r+2*alpha-3*c*r*r,c])
zero('original_inverse_chart',FH-target)
zero('original_simple_root_relation',2*(target[0]-a).subs(alpha,sp.diff(P,r)/2)-P)
zero('original_chart_boundary',F.subs(x,0)-sp.Matrix([w+4*y*y,y,0]))
zero('retained_double_cover',P.subs({a:2*s,b:0,c:0})+2*(r*r+2*s))
zero('original_two_finite_lifts',H.subs({alpha:-2*r,c:0})-sp.Matrix([-1/(2*r),3*r,26*r*r]))
zero('branch_lift_image',F.subs({x:-1/(2*r),y:3*r,w:26*r*r},simultaneous=True)-sp.Matrix([-r*r,0,0]))
Delta=b*b-32*s
Rb=sp.Matrix([[0,-2*s],[1,b/2]])
Ab=sp.Matrix([[0,4*b/Delta],[0,-16/Delta]])
zero('retained_b_root_relation',Rb*Rb-b*Rb/2+2*s*I)
zero('retained_b_connection',Rb.diff(s)+Ab*Rb-Rb*Ab-4*(b*I-4*Rb)/Delta)
zero('retained_b_D2',Ab.diff(s)+Ab*Ab-16*Ab/Delta)
Jb=sp.Matrix([[1,b/2],[0,-1]])
trb=sp.Matrix([[2,b/2]])
zero('retained_b_involution',Jb*Jb-I)
zero('retained_b_horizontal_involution',Ab*Jb-Jb*Ab)
zero('retained_b_trace_connection',trb*Ab)
zero('retained_b_recovers_original',Ab.subs(b,0)-A)
eta=sp.symbols('eta',nonzero=True)
zero('translated_original_cover',(-2*r*r+b*r-4*s).subs({r:eta+b/4,s:b*b/32-eta*eta/2},simultaneous=True))
zero('translated_original_inverse',H.subs({r:eta+b/4,alpha:-2*eta,c:0},simultaneous=True)-sp.Matrix([-1/(2*eta),b/4+3*eta,26*eta*eta+3*b*eta/2]))
sr=(c*r**3-2*r*r+b*r)/4
u=sp.Function('u')
pr=sp.diff(P,r)
lift=-4*sp.diff(u(sr),r,2)/pr**2+4*sp.diff(P,r,2)*sp.diff(u(sr),r)/pr**3
zero('full_cubic_heat_generator',lift+sp.diff(u(s),s,2).subs(s,sr)/4)
ROOT.joinpath('checks').mkdir(exist_ok=True)
receipt={'status':'pass','check_count':len(checks),'checks':checks,'sympy_version':sp.__version__,'proof_scope':'Exact algebraic residuals; analytic proofs are in tex/heat_connection.tex.','RH_counterexample':False,'Navier_Stokes_counterexample':False,'Lean_verified':False,'resource_class':'non-critical','memory_ceiling_bytes':5000000000}
ROOT.joinpath('checks/heat_connection_checks.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print(json.dumps({'status':'pass','check_count':len(checks)}))
