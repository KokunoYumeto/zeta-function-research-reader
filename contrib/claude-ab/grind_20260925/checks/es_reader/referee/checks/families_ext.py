import sympy as sp
r, t = sp.symbols('r t', integer=True, positive=True)
# Rosati (first construction) slice (h, alpha, s) = (1, 1, 31): q = 31 r - 1, n = 4q - 31 = 124 r - 35, denominators (n r, n r q, q)
q = 31*r - 1; n = 4*q - 31
x = (n*r, n*r*q, q)
print("slice 124r-35:", sp.simplify(sp.Rational(4)/n - sum(1/xi for xi in x)) == 0, " n =", sp.expand(n))
# Rosati (second construction) slice (beta, r) = (3, 31), h = 23 t + 7, s = 36 t + 11, q = 31 s - 3, n = 372 h - 23
h = 23*t + 7; s = 36*t + 11; q = 31*s - 3; n = 372*h - 23; beta = 3; rr = 31
print("check s n + 1 = 4 h beta q:", sp.expand(s*n + 1 - 4*h*beta*q) == 0, "; s | 4 h beta^2 + 1:", sp.expand(4*h*beta**2 + 1 - 23*s) == 0)
x = (n*h*beta*q, rr*h*beta, rr*h*q)
print("slice 8556t+2581:", sp.simplify(sp.Rational(4)/n - sum(1/xi for xi in x)) == 0, " n =", sp.expand(n))
# t = 0 (the even half, n = 2581 + 17112k at k = 0) and t = 1 (family 3 at k = 0):
for tv in (0, 1, 2):
    vals = [int(sp.expand(e).subs(t, tv)) for e in (n,) + x]
    print("  t =", tv, "n =", vals[0], "denominators", vals[1:], "prime n:", sp.isprime(vals[0]))
# residual R of the least denominator in each family row (shell structure)
k = sp.symbols('k')
g1, g2, m3, m4 = 31*k+30, 31*k+15, 23*k+15, 23*k+19
fam = [(248*k+209, 2*g1), (248*k+89, 2*g2), (17112*k+11137, 186*m3), (17112*k+14113, 186*m4)]
for nn, aa in fam:
    print("family n =", nn, ": residual 4a - n =", sp.expand(4*aa - nn))
