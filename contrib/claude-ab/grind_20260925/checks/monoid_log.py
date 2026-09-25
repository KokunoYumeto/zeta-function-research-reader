# Formal logarithm of D_S(s) = sum_{m in S} m^{-s} for the multiplicative monoid S = {m >= 1 : m = +-1 mod 5}.
# (Z_{1/5}(s) = zeta(s,1/5) + zeta(s,4/5) = 5^s D_S(s).)  For zeta itself the logarithm has coefficients Lambda(n)/log n >= 0.
from fractions import Fraction as Fr
N = 3000
inS = lambda m: m % 5 in (1, 4)
d = [Fr(0)]*(N+1)
for m in range(1, N+1):
    if inS(m): d[m] = Fr(1)
def conv(a, b):
    c = [Fr(0)]*(N+1)
    for i in range(2, N+1):
        if a[i] == 0: continue
        for j in range(2, N//i+1):
            if b[j] != 0: c[i*j] += a[i]*b[j]
    return c
E = d[:]; E[1] = Fr(0)                      # D - 1
logc = [Fr(0)]*(N+1); P = E[:]; k = 1
while any(P):
    for n in range(N+1): logc[n] += Fr((-1)**(k+1), k)*P[n]
    P = conv(P, E); k += 1
neg = [n for n in range(2, N+1) if logc[n] < 0]
print("first negative coefficients of log D_S:", [(n, str(logc[n])) for n in neg[:8]])
print("number of n <= %d with negative coefficient: %d" % (N, len(neg)))
print("r_36 =", logc[36], "; factorizations of 36 in S: 4*9 and 6*6 (4, 6, 9 are irreducible in S)")
# irreducibles of S up to 60 (elements > 1 of S that are not products of two elements > 1 of S)
irr = [m for m in range(2, 61) if inS(m) and not any(inS(a) and m % a == 0 and inS(m//a) and 1 < a < m for a in range(2, m))]
print("irreducibles of S up to 60:", irr)
# control: zeta's formal log coefficients are Lambda(n)/log n >= 0 (check nonnegativity with the same code)
d2 = [Fr(0)] + [Fr(1)]*N; E2 = d2[:]; E2[1] = Fr(0)
logz = [Fr(0)]*(N+1); P = E2[:]; k = 1
while any(P):
    for n in range(N+1): logz[n] += Fr((-1)**(k+1), k)*P[n]
    P = conv(P, E2); k += 1
from sympy import factorint
okz = all((logz[n] == (Fr(1, list(factorint(n).values())[0]) if len(factorint(n)) == 1 else 0)) for n in range(2, N+1))
print("zeta control: log-coefficients equal 1/k on prime powers p^k and 0 elsewhere, n <= %d:" % N, okz)
