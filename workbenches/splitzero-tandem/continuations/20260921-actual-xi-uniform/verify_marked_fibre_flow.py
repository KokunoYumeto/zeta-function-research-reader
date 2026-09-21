"""Exact seven original fibre trajectories and the five-branch finite boundary."""
from pathlib import Path
import sympy as s
import json
a,y,z,w,b=s.symbols('a y z w b',nonzero=True)
i=s.I
fb=i+a*y;fc=-i+2*a*y+a*a*z
fd=-i*y-2*a*y*y-i*a*z-a*a*y*z
fe=-7*i*y*y+2*z+a*w
ff=2*a*a*y**3*z+a*w*y+4*a*y**4+6*i*a*y*y*z+i*w+3*i*y**3-4*y*z
P=s.Matrix([a*fc,a*fe+fb*fd,a*ff+fb*fe,fb*ff]).applyfunc(s.expand)
variables=[a,y,z,w]
J=P.jacobian(variables)
image=s.Matrix([0,0,-b*b,0])
points=[s.Matrix([0,0,i*b*b/2,0])]
for eps in [1,-1]:
 points.append(s.Matrix([eps*i/b,-eps*b,-3*i*b*b,13*eps*b**3]))
for eta in [1,-1]:
 for eps in [1,-1]:
  points.append(s.Matrix([eps/(s.sqrt(2)*b),-(eta+i*eps*s.sqrt(2))*b,
   (2*eta*eps*s.sqrt(2)+6*i)*b*b,(-34*eta-19*i*eps*s.sqrt(2))*b**3]))
for q in points:
 sub=dict(zip(variables,q))
 assert all(s.cancel(x)==0 for x in P.subs(sub,simultaneous=True)-image)
 # Derivative with respect to b, preserving every original coordinate.
 assert all(s.cancel(x)==0 for x in J.subs(sub,simultaneous=True)*q.diff(b)-image.diff(b))
finite=[s.Matrix([0,1,7*i/2,11])]
for eps in [1,-1]:
 finite.append(s.Matrix([eps,1-i*eps,-2*eps+3*i,18-6*i*eps]))
for q in finite:
 assert all(s.cancel(x)==0 for x in P.subs(dict(zip(variables,q)),simultaneous=True)-s.Matrix([0,1,0,0]))
A,B,C,D,u=s.symbols('A B C D u')
disc=s.discriminant(A*u**4+u**3+B*u**2+C*u+D,u)
star={A:0,B:1,C:0,D:0}
gradient=[s.expand(s.diff(disc,c).subs(star)) for c in [A,B,C,D]]
assert gradient==[0,0,0,-4]
out={'all_assertions_passed':True,'seven_full_original_trajectories_verified':True,
 'branch_velocity_identities_verified':True,'three_finite_boundary_states_verified':True,
 'discriminant_gradient_at_collision':list(map(str,gradient)),
 'seven_trajectories':[[str(x) for x in q] for q in points],
 'finite_boundary_states':[[str(x) for x in q] for q in finite]}
Path(__file__).with_name('marked_fibre_flow_exact.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print('All seven original trajectories, their velocities, three finite boundary points and discriminant gradient passed.')
