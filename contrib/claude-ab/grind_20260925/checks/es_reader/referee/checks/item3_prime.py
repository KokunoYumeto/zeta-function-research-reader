from sympy import isprime, factorint, divisors
from math import gcd
p = 7510085481569082811681
print("p =", p, "digits:", len(str(p)), "isprime:", isprime(p), " p mod 840 =", p % 840, " p mod 24 =", p % 24)
print("p-1 =", factorint(p - 1))
q1 = (p - 1) // (2**5 * 3 * 5); print("q1 =", q1, "isprime:", isprime(q1), " q1-1 =", factorint(q1 - 1))
q2 = (q1 - 1) // (2 * 3 * 5 * 351707); print("q2 =", q2, "isprime:", isprime(q2), " q2-1 =", factorint(q2 - 1))
# Pocklington: N-1 = F*U with F >= sqrt(N) fully factored; for each prime r | F need a with a^(N-1)=1, gcd(a^((N-1)/r)-1, N)=1
def pocklington(N, Fprimes):
    Fp = 1
    for r in Fprimes: Fp *= r ** factorint(N - 1)[r]
    ok_size = Fp * Fp > N
    wits = {}
    for r in Fprimes:
        for a in range(2, 200):
            if pow(a, N - 1, N) == 1 and gcd(pow(a, (N - 1) // r, N) - 1, N) == 1:
                wits[r] = a; break
    return ok_size, wits
print("level p :", pocklington(p, [2, 3, 5, q1]))
print("level q1:", pocklington(q1, [2, 3, 5, 351707, q2]))
print("level q2:", pocklington(q2, [2, 3, 17, 5051, 169307]))
# solvability: least occupied shell (p = 1 mod 4)
R = 3
while True:
    a = (p + R) // 4
    f = factorint(a)
    res = {1 % R}
    for q, e in f.items():
        pw = [pow(q, k, R) for k in range(2*e + 1)]
        res = {(x*y) % R for x in res for y in pw}
    t1 = (-pow(4, -1, R)) % R; t2 = (-a) % R
    if t1 in res or t2 in res:
        break
    R += 4
print("least occupied shell: R =", R, " a =", a, " a =", f, " (h =", (R+1)//4, ")")
# explicit solution
for u in divisors(a*a):
    if (4*u + 1) % R == 0:
        d = p*p*u; y = (d + p*a)//R; z = (p*p*a*a//d + p*a)//R; break
    if (u + a) % R == 0:
        d = p*u; y = (d + p*a)//R; z = (p*p*a*a//d + p*a)//R; break
from fractions import Fraction as Fr
print("solution:", (a, y, z), " check:", Fr(4, p) == Fr(1, a) + Fr(1, y) + Fr(1, z))
