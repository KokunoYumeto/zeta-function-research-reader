"""Actual arithmetic generator with the original four Fable point labels retained."""
from pathlib import Path
import sympy as s
import json
i=s.I;r=s.sqrt(2)
k,delta,gamma=s.symbols('k delta gamma',positive=True)
K=s.Matrix([[0,i,1/r,1/r],[0,-1,-1-r*i,1-r*i],
 [i/2,-3*i,2*r+6*i,-2*r+6*i],[0,13,-34-19*r*i,34-19*r*i]])
Ki=K.inv().applyfunc(s.simplify)
rho=[s.Rational(1,2)+delta+i*gamma,s.Rational(1,2)+delta-i*gamma,
      s.Rational(1,2)-delta+i*gamma,s.Rational(1,2)-delta-i*gamma]
B=(K*s.diag(*[k*x for x in rho])*Ki).applyfunc(s.simplify)
ystar=s.Matrix([0,1,0,0]);h=s.Matrix([0,0,-1,0])
assert (B*h-k*rho[0]*h).applyfunc(s.simplify)==s.zeros(4,1)
v=B*ystar
nuA=k*(-68*gamma+i*(25*r*gamma-136*delta))/154
nuD=k*(-884*delta+(1631*r+442*i)*gamma)/77
assert s.simplify(v[0]-nuA)==0
assert s.simplify(v[3]-nuD)==0
print('Generator:',B,flush=True)
print('Collision normal derivative:',s.expand(v[3]),flush=True)
print('Source-generator column2:',v,flush=True)
out={'original_point_matrix':str(K),'generator':[[str(x) for x in row] for row in B.tolist()],
 'collision_target':[str(x) for x in ystar],
 'collision_target_velocity':[str(x) for x in v],
 'common_value_eigenvector_verified':True,
 'K_inverse_ea':[str(x) for x in Ki*s.Matrix([1,0,0,0])],
 'K_inverse_ew':[str(x) for x in Ki*s.Matrix([0,0,0,1])],
 'A_velocity_exact':str(nuA),'D_velocity_exact':str(nuD),
 'all_assertions_passed':True}
Path(__file__).with_name('marked_arithmetic_generator_exact.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
