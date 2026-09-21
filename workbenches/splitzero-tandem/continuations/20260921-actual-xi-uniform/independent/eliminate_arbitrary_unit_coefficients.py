"""Exact elimination of simultaneous second/fourth period-coefficient zeros."""
from pathlib import Path
import json
import sympy as s
from sympy.polys.rings import ring
HERE=Path(__file__).resolve().parent
x,y,q=s.symbols('x y q');rt=s.sqrt(5)
data=json.loads((HERE/'ARBITRARY_UNIT_COEFFICIENT_DERIVATION.json').read_text(encoding='utf-8'))
H2=s.sympify(data['polynomials']['2'],locals={'x':x,'y':y,'q':q})
H4=s.sympify(data['polynomials']['4'],locals={'x':x,'y':y,'q':q})

def pair(H):
    A=[s.expand(H).coeff(q,r) for r in range(4)]
    return (4*A[0]+(rt-1)*A[1]-(rt+1)*(A[2]+A[3]),2*A[1]+(rt-1)*(A[2]-A[3]))

P2,J2=pair(H2);P4,J4=pair(H4)
K=s.QQ.algebraic_field(rt)
RR,Y,X=ring('y,x',K)
pp=RR.from_expr(P2);jj=RR.from_expr(J2)
sub=pp.subresultants(jj)
print('subresultant degrees',[(f.degree(Y),f.degree(X)) for f in sub],flush=True)
last=s.Poly(sub[-1].as_expr(),x,domain=K)
geometry=s.Poly((x-s.Rational(1,4))*(x-s.Rational(1,9))**2,x,domain=K)
F=last.exquo(geometry).monic()
linear=sub[-2]
linear_y=s.Poly(linear.as_expr(),y,domain=K.poly_ring(x))
A=s.Poly(linear_y.nth(1),x,domain=K)
B=s.Poly(linear_y.nth(0),x,domain=K)
assert s.expand(linear.as_expr()-A.as_expr()*y-B.as_expr())==0
print('linear coefficient gcd',s.gcd(A,F).as_expr(),flush=True)
Ainv=s.invert(A,F)
root=(-B*Ainv).rem(F)
print('root quotient computed',flush=True)

def at_root(poly):
    py=s.Poly(poly,y,domain=K.poly_ring(x))
    value=s.Poly(0,x,domain=K)
    for c in py.all_coeffs():
        value=(value*root+s.Poly(c,x,domain=K)).rem(F)
    return value

v4=at_root(P4)
g=s.gcd(v4,F)
print('fourth real coefficient gcd',g.as_expr(),flush=True)
if g.degree()>0:
    w4=at_root(J4)
    g=s.gcd(g,w4)
    print('joint fourth coefficient gcd',g.as_expr(),flush=True)
else:w4=None
out={'field':'Q(sqrt(5))','residual_polynomial':str(F.as_expr()),
     'subresultant_degrees':[(f.degree(Y),f.degree(X)) for f in sub],
     'linear_A':str(A.as_expr()),'linear_B':str(B.as_expr()),
     'linear_A_inverse':str(Ainv.as_expr()),'phase_root_mod_residual':str(root.as_expr()),
     'fourth_real_at_root':str(v4.as_expr()),'fourth_real_gcd':str(g.as_expr())}
if g.degree()==0 and w4 is None:
    out['fourth_real_inverse']=str(s.invert(v4,F).as_expr())
(HERE/'ARBITRARY_UNIT_NONCONSTANCY_ELIMINATION.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print('certificate written',flush=True)
