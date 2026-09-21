"""Exact original marked receiver jets; symbolic real moments, no sample substitution."""
from pathlib import Path
import sympy as s
import json
import itertools
B=Path(__file__).resolve().parent
d,g,v=s.symbols('delta gamma v',real=True)
x=s.symbols('x',real=True)
rt=s.sqrt(2); I=s.I
K=s.Matrix([[0,I,1/rt,1/rt],[0,-1,-1-rt*I,1-rt*I],
 [I/2,-3*I,2*rt+6*I,-2*rt+6*I],[0,13,-34-19*rt*I,34-19*rt*I]])
roots=[s.Rational(1,2)+d+I*g,s.Rational(1,2)+d-I*g,
 s.Rational(1,2)-d+I*g,s.Rational(1,2)-d-I*g]
polys=[]
for j in range(2):
    pol=0
    for a,r in enumerate(roots):
        numer=s.prod(x-rr for b,rr in enumerate(roots) if b!=a)
        denom=s.prod(r-rr for b,rr in enumerate(roots) if b!=a)
        pol+=K.inv()[a,j]*numer/denom
    coeff=[s.factor(s.cancel(s.expand(pol).coeff(x,q))) for q in range(4)]
    polys.append(coeff)
    print('Interpolation column',j+1,flush=True)
    for c in coeff: print(c,flush=True)
a=polys[0]
re=lambda z:s.factor(s.cancel(s.expand_complex(z).as_real_imag()[0]))
im=lambda z:s.factor(s.cancel(s.expand_complex(z).as_real_imag()[1]))
C=s.Matrix([[re(z) for z in a],[im(z) for z in a],
 [re((v+q+1)*a[q+1]) if q<3 else 0 for q in range(4)],
 [im((v+q+1)*a[q+1]) if q<3 else 0 for q in range(4)]])
print('REAL MATRIX',C,flush=True)
denom=4928*d*g*(d*d+g*g)
N=C.applyfunc(lambda z:s.Poly(s.cancel(z*denom),d,g,v,extension=rt))
dp=s.Poly(0,d,g,v,extension=rt)
for perm in itertools.permutations(range(4)):
    inv=sum(perm[a]>perm[b] for a in range(4) for b in range(a+1,4))
    term=s.Poly((-1)**inv,d,g,v,extension=rt)
    for a in range(4):term=term*N[a,perm[a]]
    dp+=term
det=s.factor(dp.as_expr(),extension=rt)/denom**4
print('DETERMINANT',det,flush=True)
out={'column_1':[str(z) for z in polys[0]],'column_2':[str(z) for z in polys[1]],
 'real_jet_matrix':[[str(z) for z in C.row(j)] for j in range(4)],'determinant':str(det)}
(B/'ACTUAL_REAL_JET_DERIVATION.json').write_text(json.dumps(out,indent=2)+'\n')
