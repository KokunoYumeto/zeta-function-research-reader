"""Short exact modular witnesses for the characteristic-zero elimination."""
from pathlib import Path
import json
import sympy as s
HERE=Path(__file__).resolve().parent
x,y,q=s.symbols('x y q');rt=s.sqrt(5);prime=101
K=s.QQ.algebraic_field(rt)
source=json.loads((HERE/'ARBITRARY_UNIT_COEFFICIENT_DERIVATION.json').read_text(encoding='utf-8'))
elim=json.loads((HERE/'ARBITRARY_UNIT_NONCONSTANCY_ELIMINATION.json').read_text(encoding='utf-8'))

def modc(c):
    val=s.cancel(s.expand(c).subs(rt,45))
    num,den=s.fraction(val)
    assert int(den)%prime!=0
    return int(num)*pow(int(den),-1,prime)%prime

def modp(expr):
    p=s.Poly(expr,x,domain=K)
    return s.Poly.from_dict({(r,):modc(p.nth(r)) for r in range(p.degree()+1)},x,modulus=prime)

def arr(p):return [int(p.nth(r))%prime for r in range(max(0,p.degree())+1)]
F=modp(s.sympify(elim['residual_polynomial'],locals={'x':x}))
A=modp(s.sympify(elim['linear_A'],locals={'x':x}))
B=modp(s.sympify(elim['linear_B'],locals={'x':x}))
Ai=s.invert(A,F);Y=(-B*Ai).rem(F)
H4=s.sympify(source['polynomials']['4'],locals={'x':x,'y':y,'q':q})
HH=[s.expand(H4).coeff(q,r) for r in range(4)]
P4=4*HH[0]+(rt-1)*HH[1]-(rt+1)*(HH[2]+HH[3])
J4=2*HH[1]+(rt-1)*(HH[2]-HH[3])
py=s.Poly(P4,y,domain=K.poly_ring(x))
E=s.Poly(0,x,modulus=prime)
for c in py.all_coeffs(): E=(E*Y+modp(c)).rem(F)
Ei=s.invert(E,F)
assert (Ai*A).rem(F)==s.Poly(1,x,modulus=prime)
assert (Ei*E).rem(F)==s.Poly(1,x,modulus=prime)

# The complete second exceptional phase: y=1/3.
P=s.Poly(P4.subs(y,s.Rational(1,3)),x,domain=K)
J=s.Poly(J4.subs(y,s.Rational(1,3)),x,domain=K)
geom=s.Poly(x-s.Rational(1,9),x,domain=K)
Pu=P.exquo(geom);Ju=J.exquo(geom)
Pm,Jm=modp(Pu.as_expr()),modp(Ju.as_expr())
bs,bt,bg=s.gcdex(Pm,Jm)
assert bg==s.Poly(1,x,modulus=prime)
assert bs*Pm+bt*Jm==s.Poly(1,x,modulus=prime)
out={'prime':prime,'sqrt5_image':45,'coefficient_order':'ascending powers of x',
     'residual':arr(F),'linear_A':arr(A),'linear_B':arr(B),'linear_A_inverse':arr(Ai),
     'phase_root':arr(Y),'fourth_real_at_root':arr(E),'fourth_real_inverse':arr(Ei),
     'second_phase_real_quotient':arr(Pm),'second_phase_imag_quotient':arr(Jm),
     'second_phase_bezout_real':arr(bs),'second_phase_bezout_imag':arr(bt)}
(HERE/'ARBITRARY_UNIT_MOD101_CERTIFICATE.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
for key,val in out.items():print(key,val)
