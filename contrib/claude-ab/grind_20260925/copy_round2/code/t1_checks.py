import numpy as np, sympy as sp
from sympy import primerange, legendre_symbol
# ---------- (a) symbolic: lifts of CC's mirror and of J to E: y^2 = x^3 - x ----------
x, y = sp.symbols('x y'); I = sp.I
f = x**3 - x
alpha = (-1/x, y/x**2)            # lift of T -> eps/T = -1/T
J = (-x, I*y)                      # (x,y) -> (eps x, J y)
def onE(P): return sp.simplify(P[1]**2 - P[0]**3 + P[0]) .subs(y**2, f)
print('alpha maps E to E:', sp.simplify((alpha[1]**2 - alpha[0]**3 + alpha[0]) - (y**2 - f)/x**4) == 0)
print('J maps E to E:', sp.simplify((J[1]**2 - J[0]**3 + J[0]) - (-(y**2) + f)*(-1)) == 0)
J2 = (-J[0], I*J[1]); print('J^2 =', J2, '(hyperelliptic involution = eps on the fibre)')
aJ = (-1/J[0], J[1]/J[0]**2); Ja = (-alpha[0], I*alpha[1]); print('alpha o J == J o alpha:', sp.simplify(aJ[0]-Ja[0])==0 and sp.simplify(aJ[1]-Ja[1])==0)
# alpha = translation by (0,0): chord formula
lam = y/x; x3 = sp.simplify((lam**2 - x - 0).subs(y**2, f)); y3 = sp.simplify(-(lam*(x3-0)+0))
print('P + (0,0) =', (x3, y3), '== alpha:', sp.simplify(x3 - alpha[0]) == 0 and sp.simplify(y3 - alpha[1]) == 0)
# ---------- (b) a_p of y^2=x^3-x vs primary Gaussian primes ----------
def a_p(p):
    xs = np.arange(p, dtype=np.int64); v = (xs**3 - xs) % p
    ls = np.array([0 if t == 0 else (1 if pow(int(t), (p-1)//2, p) == 1 else -1) for t in v])
    return -int(ls.sum())
def primary(p):
    # p = a^2 + b^2, return a+bi with a+bi = 1 mod (2+2i)
    for a in range(1, int(p**0.5)+1):
        b2 = p - a*a; b = int(round(b2**0.5))
        if b*b == b2:
            for (u, v) in [(a,b),(a,-b),(-a,b),(-a,-b),(b,a),(b,-a),(-b,a),(-b,-a)]:
                # (u+vi) - 1 divisible by 2+2i  <=>  ((u-1)+vi)/(2+2i) in Z[i]
                num = complex(u-1, v)/(2+2j)
                if abs(num.real-round(num.real))<1e-9 and abs(num.imag-round(num.imag))<1e-9:
                    return complex(u, v)
bad = 0; nsplit = ninert = 0; conv = {'2Re(pi)':0, '-2Re(pi)':0}
for p in primerange(3, 20000):
    ap = a_p(p)
    assert abs(ap) <= 2*p**0.5
    if p % 4 == 3:
        ninert += 1; bad += (ap != 0)
    else:
        nsplit += 1; pi = primary(p)
        assert abs(abs(pi)**2 - p) < 1e-9
        if ap == int(round(2*pi.real)): conv['2Re(pi)'] += 1
        if ap == -int(round(2*pi.real)): conv['-2Re(pi)'] += 1
print(f'odd p<20000: {ninert} inert (a_p=0 failures: {bad}), {nsplit} split; convention matches:', conv)
# ---------- (c) psi((n)) = chi_{-4}(n) n is the primary generator of nZ[i], n odd ----------
ok = all(((chi*n - 1) % 4 == 0) for n in range(1, 2001, 2) for chi in [1 if n % 4 == 1 else -1])
print('primary generator of (n) is chi_{-4}(n) n for odd n<=2000:', ok)
# ---------- (d) zeta numerator over F_{p^r}: #E(F_{p^r}) = 1+p^r-(al^r+be^r) by brute force over F_{p^2}, F_{p^3} ----------
def count_Fq(p, r):
    # F_{p^r} = F_p[t]/(m(t)) with m irreducible; brute-force count affine solutions + 1 point at infinity
    t = sp.symbols('t')
    for cand in sp.polys.galoistools.gf_irreducible(r, p, sp.polys.domains.ZZ) if False else []:
        pass
    m = sp.Poly(sp.nextprime(1), t)  # placeholder
    return None
from itertools import product
def gf_elems(p, r, mod):
    return [tuple(c) for c in product(range(p), repeat=r)]
def mulmod(a, b, p, mod):
    r = len(mod)-1; prod_ = [0]*(2*r-1)
    for i,ai in enumerate(a):
        for j,bj in enumerate(b): prod_[i+j] = (prod_[i+j] + ai*bj) % p
    for k in range(2*r-2, r-1, -1):  # reduce by monic mod (coeffs low->high)
        c = prod_[k]
        if c:
            for i in range(r+1): prod_[k-r+i] = (prod_[k-r+i] - c*mod[i]) % p
    return tuple(prod_[:r])
def find_irred(p, r):
    for coeffs in product(range(p), repeat=r):
        mod = list(coeffs)+[1]
        # irreducible iff no root and (for r<=3) no factor of degree<=r/2 -> for r in {2,3} no root suffices
        if all(sum(c*pow(a, i, p) for i, c in enumerate(mod)) % p for a in range(p)):
            return mod
def countE(p, r):
    mod = find_irred(p, r); els = gf_elems(p, r, mod)
    sq = {}
    for e_ in els:
        s = mulmod(e_, e_, p, mod); sq[s] = sq.get(s, 0) + 1
    cnt = 1
    for xx in els:
        x3 = mulmod(mulmod(xx, xx, p, mod), xx, p, mod)
        rhs = tuple((a-b) % p for a, b in zip(x3, xx))
        cnt += sq.get(rhs, 0)
    return cnt
for p in [3, 5, 7, 11, 13]:
    ap = a_p(p); al, be = np.roots([1, -ap, p])
    for r in [1, 2, 3]:
        pred = 1 + p**r - (al**r + be**r).real
        got = countE(p, r) if p**r <= 2200 else None
        if got is not None: print(f'p={p} r={r}: #E={got}  1+p^r-(al^r+be^r)={pred:.1f}  CC-line count 1+p^r={1+p**r}')
