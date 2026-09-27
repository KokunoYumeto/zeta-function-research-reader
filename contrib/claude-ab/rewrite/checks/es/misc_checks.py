# (1) shell-R=11 certificate count at primes p = 1 (mod 840): A_11(p*a), a=(p+11)/4, counts ordered triples
#     (X,Y,Z) with XYZ = p*a, gcd(X,Y)=1, 11 | X+Y  (pair-count series of the notes).
from sympy import primerange, divisors, isprime, factorint, Matrix
from math import gcd
def A(R, n):
    c = 0
    for X in divisors(n):
        for Y in divisors(n // X):
            if gcd(X, Y) == 1 and (X + Y) % R == 0:
                c += 1
    return c
vals = {}
for p in primerange(2, 400000):
    if p % 840 != 1: continue
    a = (p + 11) // 4
    v = A(11, p * a)
    vals.setdefault(v, p)
print('A_11(p a) on primes p = 1 mod 840: value -> least prime:', dict(sorted(vals.items())))
# (2) involutions in GL_2(F_3) and in the binary octahedral group (for the umbral-group statement)
import itertools
F = range(3)
inv = 0
for a,b,c,d in itertools.product(F, repeat=4):
    if (a*d - b*c) % 3 == 0: continue
    M = ((a,b),(c,d))
    sq = (((a*a+b*c)%3, (a*b+b*d)%3), ((c*a+d*c)%3, (c*b+d*d)%3))
    if sq == ((1,0),(0,1)) and M != ((1,0),(0,1)): inv += 1
print('involutions in GL_2(3):', inv, '(the binary octahedral group has exactly one element of order 2)')
# (3) modular flow versus congruence boost on Herm_2 with the Lorentz form det
import sympy as sp
r, t, s = sp.symbols('r t s', real=True)
h, u, v, w = sp.symbols('h u v w', real=True)
X = sp.Matrix([[h + w, u + sp.I*v], [u - sp.I*v, h - w]])
def coords(Y):
    Y = sp.simplify(Y)
    return [sp.simplify((Y[0,0] + Y[1,1])/2), sp.simplify(sp.re(sp.expand(Y[0,1]))), sp.simplify(sp.im(sp.expand(Y[0,1]))), sp.simplify((Y[0,0] - Y[1,1])/2)]
Hit = sp.diag(sp.exp(sp.I*r*t), sp.exp(-sp.I*r*t))          # H_r^{it}, H_r = diag(e^r, e^-r)
flow = coords(Hit * X * Hit.H)
Hs = sp.diag(sp.exp(r*s), sp.exp(-r*s))                       # H_r^{s}
boost = coords(Hs * X * Hs)
print('modular flow  H^{it} X H^{-it}  ->', [sp.simplify(sp.expand_complex(c)) for c in flow])
print('real power    H^{s} X H^{s}     ->', [sp.simplify(sp.expand_complex(c)) for c in boost])
