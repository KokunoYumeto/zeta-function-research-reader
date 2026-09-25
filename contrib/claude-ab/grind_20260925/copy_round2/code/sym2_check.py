import numpy as np
from sympy import primerange, factorint
NMAX = 3000
def ap(p):
    xs = np.arange(p, dtype=np.int64); v = (xs**3 - xs) % p
    return -int(sum(0 if t == 0 else (1 if pow(int(t), (p-1)//2, p) == 1 else -1) for t in v))
chi4 = lambda n: 0 if n % 2 == 0 else (1 if n % 4 == 1 else -1)
# (1) L(Sym^2 E, s): Euler factor at odd p: 1/((1-al^2 X)(1-p X)(1-be^2 X)); coefficients via power series in X = p^-s
def sym2_local(p, kmax):
    a = ap(p); al, be = np.roots([1, -a, p])
    # complete homogeneous sums h_k(al^2, p, be^2)
    roots = [al**2, p+0j, be**2]
    h = [1+0j] + [0j]*kmax
    for r in roots:                       # multiply by 1/(1 - r X)
        for k in range(1, kmax+1): h[k] += r*h[k-1]
    return [round(x.real) for x in h]
# (2) L(psi^2, s) = sum over ideals coprime to 2 of psi(A)^2 N(A)^-s with psi((alpha)) = alpha, alpha = 1 mod (2+2i)
def primary(z):
    for u in [1, -1, 1j, -1j]:
        w = z*u; q = (complex(w.real-1, w.imag))/(2+2j)
        if abs(q.real-round(q.real)) < 1e-9 and abs(q.imag-round(q.imag)) < 1e-9: return w
coef_psi2 = np.zeros(NMAX+1, dtype=complex)
seen = set()
for x in range(-60, 61):
    for y in range(-60, 61):
        n = x*x + y*y
        if n == 0 or n > NMAX or n % 2 == 0: continue
        w = primary(complex(x, y))
        key = (round(w.real), round(w.imag))
        if key in seen: continue
        seen.add(key); coef_psi2[n] += w**2
# (3) L(s-1, chi4) coefficients d(n) = chi4(n) n
d = np.array([chi4(n)*n for n in range(NMAX+1)], dtype=float)
# product L(psi^2)*L(s-1,chi4) as Dirichlet convolution
prod = np.zeros(NMAX+1, dtype=complex)
for m in range(1, NMAX+1):
    if coef_psi2[m] == 0: continue
    for k in range(1, NMAX//m + 1): prod[m*k] += coef_psi2[m]*d[k]
# L(Sym^2 E) coefficients from local factors (multiplicative)
sym = np.zeros(NMAX+1); sym[1] = 1
loc = {p: sym2_local(p, int(np.log(NMAX)/np.log(p))+1) for p in primerange(3, NMAX+1)}
for n in range(3, NMAX+1, 2):
    v = 1
    for p, e in factorint(n).items(): v *= loc[p][e]
    sym[n] = v
odd = np.arange(1, NMAX+1, 2)
print("max |a_n(Sym^2 E) - [L(psi^2) * L(s-1,chi_-4)]_n| over odd n <=", NMAX, ":", np.max(np.abs(sym[odd] - prod[odd])))
print("imag part of product coefficients max:", np.max(np.abs(prod.imag)))
print("sample n=3,5,9,13,15,25:", [(n, int(sym[n]), complex(prod[n])) for n in [3,5,9,13,15,25]])
