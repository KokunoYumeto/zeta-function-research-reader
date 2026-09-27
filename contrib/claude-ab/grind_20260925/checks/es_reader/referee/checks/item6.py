from sympy import divisors, totient, isprime
from fractions import Fraction as F
from collections import Counter
p = 87481
print("p prime:", isprime(p), " p mod 4 =", p % 4)
shells = list(range(p//4 + 1, (p+1)//2))
maxL = None; nocc = 0; npos = 0
for a in shells:
    R = 4*a - p
    D = divisors(a)
    tau = len(D)
    res = Counter()
    for d in D:
        res[d % R] += 1; res[(p*d) % R] += 1
    E = sum(c*c for c in res.values())
    L = F(8*tau*tau, int(totient(R))) - E
    if L > 0: npos += 1
    maxL = L if maxL is None or L > maxL else maxL
    Da2 = divisors(a*a)
    if any((4*u+1) % R == 0 or (u + a) % R == 0 for u in Da2): nocc += 1
print("shells:", len(shells), " with L_a > 0:", npos, " max L_a:", maxL, " occupied shells:", nocc)
