from math import lcm
from sympy import isprime, primerange
from sympy.ntheory.modular import crt
X = 10**7
P2 = set()
R = 1
while 3*R - 4 <= X:
    M = R*(R+4)*(R+8)
    m0 = int(crt([R, R+4, R+8], [-1 % R, -2 % (R+4), -3 % (R+8)])[0]) or M
    m = m0
    while 4*m - R <= X:
        Lm = lcm(m, m+1, m+2); a = m
        while 4*a - R <= X:
            p = 4*a - R
            if p > 3 and a + 2 < p and isprime(p): P2.add(p)
            a += Lm
        m += M
    R += 2
n2 = sum(1 for p in primerange(2, X) if p % 3 == 2)
n131 = sum(1 for p in primerange(2, X) if p % 180 == 131)
print("primes = 2 mod 3 below 1e7:", n2, "; with a two-edge path:", len(P2), "(%.2f%%)" % (100*len(P2)/n2),
      "; primes = 131 mod 180:", n131, "all in P2:", all(p in P2 for p in primerange(131, X) if p % 180 == 131))
print("smallest primes = 2 mod 3 without a two-edge path:", [p for p in primerange(2, 200) if p % 3 == 2 and p not in P2][:12])
