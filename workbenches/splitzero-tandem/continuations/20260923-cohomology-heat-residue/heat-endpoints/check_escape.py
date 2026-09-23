from pathlib import Path
import sympy as s, json
x,y,w,z,T=s.symbols('x y w z T', nonzero=True)
F=s.Matrix([(1+x*y)**3*w+y*y*(1+x*y)*(4+3*x*y), y+3*x*(1+x*y)**2*w+3*x*y*y*(4+3*x*y),2*x-3*x*x*y-x**3*w])
J=F.jacobian([x,y,w])
gamma=s.Matrix([1/z,-3*z/2,13*z*z/2])
sub=dict(zip([x,y,w],gamma))
det=s.factor(J.det())
fg=F.subs(sub).applyfunc(s.factor)
target=s.Matrix([-z*z/4,0,0])
res=(fg-target).applyfunc(s.factor)
dg=gamma.diff(z)*(-4/z)
vel=(J.subs(sub)*dg-s.Matrix([2,0,0])).applyfunc(s.factor)
c=s.symbols('c')
omega=s.symbols('omega')
# Original Fable root omega=(1+xy)/x; its heat coordinate is Z=-2i omega.
root=s.factor(((1+x*y)/x).subs(sub))
heat_z=s.factor(-2*s.I*root)
checks={'jacobian_determinant':str(det),'F_gamma':[str(v) for v in fg],
        'target_residual':[str(v) for v in res],'velocity_residual':[str(v) for v in vel],
        'original_root':str(root),'heat_coordinate':str(heat_z),
        'original_fluid_time':str((1-z*z)/8),
        'heat_time_h':str(4*((1-z*z)/8)-s.Rational(1,2)),
        'heat_polynomial_residual':str(s.expand(heat_z**2-2*(4*((1-z*z)/8)-s.Rational(1,2))))}
assert det==-2 and res==s.zeros(3,1) and vel==s.zeros(3,1)
assert checks['heat_polynomial_residual']=='0'
h,r,v1,v2=s.symbols('h r v1 v2',real=True)
sig=s.Matrix([x+y,x*y]).jacobian([x,y])
collision=sig.subs({x:r,y:r})*s.Matrix([v1,v2])
assert s.expand(collision[1]-r*collision[0])==0
away=(sig*s.Matrix([2/(x-y),2/(y-x)])).applyfunc(s.factor)
assert away==s.Matrix([0,-2])
checks['collision_heat_cokernel']=-2
checks['distinct_root_coefficient_velocity']=[str(v) for v in away]
assert s.diff(1/(4*h),h)==-1/(4*h*h)
checks['ordered_pair_energy']='1/(4*h), h>0; generalized-inverse value at h=0 is supported e'
for m in range(1,13):
    assert sum((-1)**j/(s.factorial(j)*s.factorial(m-j)) for j in range(m+1))==0
checks['exact_positive_time_coefficient_cancellations']=12
(Path(__file__).parent/'ESCAPE_EXACT_CHECKS.json').write_text(json.dumps(checks,indent=2),encoding='utf-8')
print(json.dumps(checks,indent=2))
