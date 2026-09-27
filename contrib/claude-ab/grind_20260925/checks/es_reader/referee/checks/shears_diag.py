from math import gcd, lcm
from sympy import primerange, isprime, divisors
from sympy.ntheory.modular import crt
def in_W(p, a, m, n):
    R = 4*a - p
    return R >= 1 and (p*a) % m == 0 and (p*a) % n == 0 and gcd(m, n) == 1 and (m + n) % R == 0
# (1) diagonal criterion: (a+i, a+i, 1), i=0..k, is an L-path iff R+4i | p+4 for i=0..k (R = 4a - p), given a+k < p
bad = 0; n = 0
for p in primerange(5, 3000):
    for a in range(p//4 + 1, p):
        R = 4*a - p
        for k in (1, 2, 3):
            if a + k >= p: continue
            n += 1
            path = all(in_W(p, a + i, a + i, 1) for i in range(k + 1))
            crit = all((p + 4) % (R + 4*i) == 0 for i in range(k + 1))
            if path != crit: bad += 1
print("diagonal-path criterion: tested", n, "cases (p<3000, k=1..3), mismatches:", bad)
# (2) all primes p = 131 mod 180 below 10^5 have the diagonal two-path at a=(p+1)/4
ok = all(all(in_W(p, (p+1)//4 + i, (p+1)//4 + i, 1) for i in range(3)) for p in primerange(131, 10**5) if p % 180 == 131)
print("every prime p = 131 mod 180 below 1e5 has the two-path (a+i,a+i,1):", ok)
# (3) necessary condition R(R+4) | p+4 on every two-L-edge path with p <= 1e7 (complete search via the edge shape)
cnt = 0; viol = 0; diag = 0
R = 1
while 3*R - 4 <= 10**7:
    M = R*(R+4)*(R+8)
    m0 = int(crt([R, R+4, R+8], [-1 % R, -2 % (R+4), -3 % (R+8)])[0]) or M
    m = m0
    while 4*m - R <= 10**7:
        Lm = lcm(m, m+1, m+2); a = m
        while 4*a - R <= 10**7:
            p = 4*a - R
            if p > 3 and a + 2 < p and isprime(p):
                cnt += 1
                if (p + 4) % (R*(R+4)): viol += 1
                if a == m: diag += 1
            a += Lm
        m += M
    R += 2
print("two-L-edge paths with p <= 1e7:", cnt, "; violations of R(R+4) | p+4:", viol, "; diagonal ones (a = m):", diag)
