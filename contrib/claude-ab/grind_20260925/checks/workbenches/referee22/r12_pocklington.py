# Pocklington-Lehmer certificate for p = 7510085481569082811681 (ES item 3), recursively for large factors of p-1.
import sympy as sp
from math import gcd, isqrt
def pocklington(n, depth=0):
    if n < 2**64:
        ok = sp.isprime(n)   # deterministic below 2^64 (sympy uses a deterministic Miller-Rabin base set there)
        print("  "*depth + f"{n}: prime (deterministic MR below 2^64) = {ok}")
        return ok
    f = sp.factorint(n-1)
    F = 1; used = []
    for q in sorted(f, reverse=True):
        pass
    # use all fully known prime factors (factorint returns a complete factorisation)
    for q,e in f.items(): F *= q**e; used.append(q)
    assert F == n-1
    print("  "*depth + f"{n}: n-1 = " + " * ".join(f"{q}^{e}" if e>1 else str(q) for q,e in sorted(f.items())))
    # Pocklington: for each prime q | F find a with a^(n-1)=1 mod n and gcd(a^((n-1)/q)-1, n)=1; F > sqrt(n) (here F=n-1)
    for q in used:
        for a in range(2, 200):
            if pow(a, n-1, n) == 1 and gcd(pow(a, (n-1)//q, n)-1, n) == 1:
                break
        else:
            return False
    # certify the prime factors themselves
    return all(pocklington(q, depth+1) for q in used if q >= 2**64) and all(sp.isprime(q) for q in used)
p = 7510085481569082811681
print("certificate valid:", pocklington(p))
