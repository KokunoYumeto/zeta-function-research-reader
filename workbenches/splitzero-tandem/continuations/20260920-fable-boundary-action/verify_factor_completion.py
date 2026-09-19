"""Verify both full factor charts and their regular boundary inverse formulas."""
from pathlib import Path
import sympy as s
import json
a,y,z,w=s.symbols('a y z w')
records=[]
def check(label,f):
    if isinstance(f,s.MatrixBase): ok=all(s.cancel(x)==0 for x in f)
    else: ok=s.cancel(f)==0
    if not ok: raise ArithmeticError(label)
    records.append({'name':label,'passed':True})
def chart(sigma):
    b=sigma+a*y;c=-sigma+2*a*y+a*a*z
    d=-sigma*y-2*a*y*y-sigma*a*z-a*a*y*z
    e=-7*sigma*y*y+2*z+a*w
    f=2*a*a*y**3*z+a*w*y+4*a*y**4+6*sigma*a*y*y*z+sigma*w+3*sigma*y**3-4*y*z
    return b,c,d,e,f
for sigma in [s.I,-s.I]:
    b,c,d,e,f=chart(sigma)
    check(str(sigma)+' first constraint',a*d+b*c-1)
    check(str(sigma)+' resultant',-c*b**3+d*a*b*b-e*a*a*b+f*a**3-1)
    check(str(sigma)+' boundary y inverse',(2*d*b*b-a*e*b+a*a*f)/(b+sigma)-y)
    check(str(sigma)+' boundary z inverse',
          (7*y*y-10*sigma*a*y**3-4*a*a*y**4-e*b+a*f)/(2*b**3)-z)
    check(str(sigma)+' boundary w inverse',
          (e*b*(2*sigma*y+a*y*y)-11*sigma*y**3-17*a*y**4+7*sigma*a*a*y**5-f)/b**3-w)
    check(str(sigma)+' retained second divisibility',2*b*b*(d+sigma*y+2*a*y*y)
          -a*(-7*y*y+10*sigma*a*y**3+4*a*a*y**4+e*b-a*f))
transition=s.Matrix([a,y-2*s.I/a,z+6*s.I/a**2,
                    w+14*s.I*y*y/a+28*y/a**2-40*s.I/a**3])
variables=[a,y,z,w]
plus=s.Matrix([a,*chart(s.I)])
minus=s.Matrix([a,*chart(-s.I)])
check('full six-coordinate transition',plus.subs(dict(zip(variables,transition)),simultaneous=True)-minus)
check('transition determinant',transition.jacobian(variables).det()-1)
inverse=s.conjugate(transition).subs({s.conjugate(x):x for x in variables}, simultaneous=True)
check('transition inverse',inverse.subs(dict(zip(variables,transition)),simultaneous=True)-s.Matrix(variables))
result={'all_assertions_passed':True,'checks':records,
        'method':'Exact rational identities over Q(i) in all original variables',
        'regular_boundary_inverses':True}
Path(__file__).with_name('factor_completion_exact.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
