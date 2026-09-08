"""Exact full material derivative at the retained inverse-fibre heat orbit.

The positive shorthand z=sqrt(1-8*tau) is a bijective coordinate on tau<1/8.
Every time derivative below remains d/dtau=(-4/z)d/dz. This is an exact
rational identity replay, with no numerical endpoint inference or Lean.
"""
from pathlib import Path
import hashlib
import json
import sympy as s

ROOT=Path(__file__).resolve().parents[1]
checks={}
def zero(name,expression):
    vals=list(expression) if isinstance(expression,s.MatrixBase) else [expression]
    residual=[s.cancel(v) for v in vals]
    checks[name]=all(v==0 for v in residual)
    if not checks[name]: raise AssertionError((name,residual))
x,y,w,tau=s.symbols('x y w tau',real=True)
z=s.symbols('z',positive=True)
coords=(x,y,w)
F=s.Matrix([(1+x*y)**3*w+y*y*(1+x*y)*(4+3*x*y),
 y+3*x*(1+x*y)**2*w+3*x*y*y*(4+3*x*y),
 2*x-3*x*x*y-x**3*w])
J=F.jacobian(coords)
zero('original_determinant',J.det()+2)
q0=s.Matrix([1,-s.Rational(3,2),s.Rational(13,2)])
gamma=s.Matrix([1/z,-3*z/2,13*z*z/2])
Jg=J.subs(dict(zip(coords,gamma)),simultaneous=True).applyfunc(s.cancel)
J0=J.subs(dict(zip(coords,q0)),simultaneous=True)
tau_of_z=(1-z*z)/8
B=s.eye(3); B[1,2]=6*tau_of_z
A=(Jg.inv()*B*J0).applyfunc(s.cancel)
C=(J0.inv()*B.inv()*Jg).applyfunc(s.cancel)
zero('A_inverse_left',C*A-s.eye(3))
zero('A_inverse_right',A*C-s.eye(3))
zero('detA_one',A.det()-1)
zero('initial_A_identity',A.subs(z,1)-s.eye(3))
zero('initial_C_identity',C.subs(z,1)-s.eye(3))
zero('material_chain_rule',Jg*A-B*J0)
W=[]
for i in range(3):
    g1=s.Matrix([s.diff(F[(i+1)%3],q) for q in coords])
    g2=s.Matrix([s.diff(F[(i+2)%3],q) for q in coords])
    W.append((-g1.cross(g2)/2).applyfunc(s.expand))
U=(2*W[0]+6*F[2]*W[1]).applyfunc(s.expand)
Ug=U.subs(dict(zip(coords,gamma)),simultaneous=True).applyfunc(s.cancel)
DUg=U.jacobian(coords).subs(dict(zip(coords,gamma)),simultaneous=True).applyfunc(s.cancel)
zero('retained_gamma_velocity',(-4/z)*gamma.diff(z)-Ug)
zero('full_variational_equation',(-4/z)*A.diff(z)-DUg*A)
R=s.Matrix([
 [-s.Rational(27,2)/z**5,-9/z**5,-3/z**5],
 [-s.Rational(51,2)-s.Rational(27,4)/z**3,-9-s.Rational(9,2)/z**3,-3-s.Rational(3,2)/z**3],
 [s.Rational(459,2)*z-18/z,81*z+12/z,27*z],
])
zero('explicit_full_variational_derivative',(-4/z)*A.diff(z)-R)
zero('explicit_variational_matrix_product',DUg*A-R)
zero('trace_DU_gamma_zero',s.trace(DUg))
covector=C.T*s.Matrix([0,0,1])
K=(C*C.T).applyfunc(s.cancel)
zero('K_symmetry',K-K.T)
zero('K_determinant',K.det()-1)
zero('initial_K_identity',K.subs(z,1)-s.eye(3))
covector_norm=s.cancel(covector.dot(covector))
zero('covector_norm_is_K33',covector_norm-K[2,2])
p=17-9*z**3
q=1-z**3
rho=51-24*z*z-27*z**3
sigma=9+8*z*z-9*z**3
theta=-153+36*z*z+117*z**3
vpoly=-27-12*z*z+39*z**3
omega=-9+13*z**3
K_written=s.Matrix([
 [p*p/64+9*q*q/(16*z**4)+q*q/(16*z**6),
  p*rho/128+3*q*sigma/(32*z**4)+3*q*q/(32*z**6),
  p*theta/64+3*q*vpoly/(16*z**4)+q*omega/(16*z**6)],
 [p*rho/128+3*q*sigma/(32*z**4)+3*q*q/(32*z**6),
  rho*rho/256+sigma*sigma/(64*z**4)+9*q*q/(64*z**6),
  rho*theta/128+sigma*vpoly/(32*z**4)+3*q*omega/(32*z**6)],
 [p*theta/64+3*q*vpoly/(16*z**4)+q*omega/(16*z**6),
  rho*theta/128+sigma*vpoly/(32*z**4)+3*q*omega/(32*z**6),
  theta*theta/64+vpoly*vpoly/(16*z**4)+omega*omega/(16*z**6)]
])
zero('complete_six_entry_tensor_formula',K-K_written)
def endpoint(M):
    return M.applyfunc(lambda t:s.limit(t,z,0,dir='+'))
row_limit=s.Matrix([[-s.Rational(9,8),-s.Rational(3,4),-s.Rational(1,4)]])
column_limit=s.Matrix([s.Rational(1,4),s.Rational(3,8),-s.Rational(9,4)])
zero('A_row1_endpoint',endpoint(z**3*A[0,:])-row_limit)
zero('A_row2_endpoint',endpoint(z*A[1,:])-s.Rational(3,2)*row_limit)
zero('A_row3_endpoint',endpoint(A[2,:])+13*row_limit)
zero('C_column1_endpoint',endpoint(C[:,0])-s.Rational(17,2)*column_limit)
zero('C_column2_endpoint',endpoint(z*z*C[:,1])-3*column_limit)
zero('C_column3_endpoint',endpoint(z**3*C[:,2])-column_limit)
zero('full_A_scaled_endpoint',endpoint(z**3*A)-s.Matrix([1,0,0])*row_limit)
zero('full_C_scaled_endpoint',endpoint(z**3*C)-column_limit*s.Matrix([[0,0,1]]))
zero('full_K_scaled_endpoint',endpoint(z**6*K)-column_limit*column_limit.T)
zero('covector_scaled_endpoint',endpoint(z**3*covector)-s.Matrix([0,0,-s.Rational(9,4)]))
zero('covector_norm_squared_leading_coefficient',s.limit(z**6*covector_norm,z,0,dir='+')-s.Rational(81,16))
zero('A_operator_norm_leading_coefficient_squared',row_limit.dot(row_limit)-s.Rational(121,64))
zero('C_operator_norm_leading_coefficient_squared',column_limit.dot(column_limit)-s.Rational(337,64))
test_direction=A.T*s.Matrix([1,0,0])
test_direction_norm=s.cancel(test_direction.dot(test_direction))
zero('exact_small_Rayleigh_direction_norm',test_direction_norm-(329*z**6-386*z**3+121)/(64*z**6))
zero('small_Rayleigh_direction_energy',(test_direction.T*K*test_direction)[0]-1)
rayleigh=s.cancel(1/test_direction_norm)
zero('small_Rayleigh_leading_coefficient',s.limit(rayleigh/z**6,z,0,dir='+')-s.Rational(64,121))
zero('middle_eigenvalue_product_coefficient',s.Rational(64,121)*s.Rational(121,337)*s.Rational(337,64)-1)
def aslist(M):
    return [[str(M[i,j]) for j in range(M.cols)] for i in range(M.rows)]
result={
 'schema_version':1,'status':'pass','number_of_checks':len(checks),
 'all_passed':all(checks.values()),'checks':checks,
 'sympy_version':s.__version__,
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'retained_time':'tau<1/8; z=sqrt(1-8*tau)>0; tau=(1-z^2)/8; d/dtau=(-4/z)d/dz',
 'q0':[str(q) for q in q0],
 'gamma':[str(q) for q in gamma],
 'original_F':[str(f) for f in F],
 'J_at_q0':aslist(J0),'J_at_gamma':aslist(Jg),
 'B':aslist(B),'A':aslist(A),'A_inverse':aslist(C),
 'DU_at_gamma':aslist(DUg),
 'transported_e3_covector':[str(v) for v in covector],
 'transported_e3_norm_squared':str(covector_norm),
 'K':aslist(K),
 'K_six_entries_factored':aslist(K_written),
 'variational_time_derivative':aslist(R),
 'endpoint_A_row_base':aslist(row_limit),
 'endpoint_C_column_base':aslist(column_limit),
 'scaled_K_endpoint':aslist(column_limit*column_limit.T),
 'covector_endpoint_norm':'norm(A^-T e3) ~ (9/4) z^-3 = (9/4)(1-8*tau)^(-3/2)',
 'covector_explicit_lower_bound':'for 0<z<=1/2 (3/32<=tau<1/8), norm(A^-T e3)>=(59/32)z^-3',
 'small_Rayleigh_direction':'xi=A^T e1/|A^T e1|',
 'small_Rayleigh_exact_value':str(rayleigh),
 'ordered_K_eigenvalues_endpoint':{
   'lambda_min':'~ (64/121) z^6 = (64/121)(1-8*tau)^3',
   'lambda_middle':'->121/337',
   'lambda_max':'~ (337/64) z^-6 = (337/64)(1-8*tau)^(-3)'
 },
 'condition_number_endpoint':'~ (40777/4096) z^-12 = (40777/4096)(1-8*tau)^(-6)',
 'finite_time_positive_definite':True,
 'uniform_ellipticity_up_to_endpoint':False,
 'eigenvalue_conclusion_method':'Written spectral-norm continuity proof from the exact two rank-one scaled matrix limits; no numerical eigenvalue inference.',
 'written_derivation':'research/material_generator_endpoint.md',
 'tex_derivation':'tex/material_endpoint.tex',
 'tex_derivation_sha256':hashlib.sha256((ROOT/'tex'/'material_endpoint.tex').read_bytes()).hexdigest(),
 'lean_used':False,'navier_stokes_disproof_established':False
}
out=ROOT/'checks'/'material_endpoint_checks.json'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'number_of_checks':len(checks),'all_passed':all(checks.values()),
 'output':out.relative_to(ROOT).as_posix()},indent=2))
