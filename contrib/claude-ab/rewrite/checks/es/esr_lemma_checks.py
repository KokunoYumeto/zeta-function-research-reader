# Checks of Proposition 3.6 (Jacobi-symbol barrier) and Lemma 4.1 (least class) of the Erdos-Straus reader,
# from the definitions only.  Prepared by Claude (Opus 5.5).  Needs sympy.
from fractions import Fraction as F
from sympy import primerange, divisors, factorint, jacobi_symbol

ok = True
def check(name, cond):
    global ok
    ok &= bool(cond)
    print(("PASS " if cond else "FAIL ") + name)

def occupied(p, a):
    R = 4 * a - p
    return any((4 * u + 1) % R == 0 or (u + a) % R == 0 for u in divisors(a * a))

# (1) Jacobi barrier: p odd prime, R = 3 mod 4, a = (p+R)/4 integral, gcd(R, pa) = 1,
#     (q/R) = 1 for every prime q | a  ==>  shell a unoccupied.
hyp = 0; conv_fail = 0
for p in primerange(3, 3000):
    for a in range(p // 4 + 1, p):
        R = 4 * a - p
        if R % 4 != 3 or any(R % q == 0 for q in factorint(p * a)):
            continue
        allres = all(jacobi_symbol(q, R) == 1 for q in factorint(a))
        if allres:
            hyp += 1
            if occupied(p, a):
                check(f"barrier at p={p}, a={a}", False)
        elif not occupied(p, a):
            conv_fail += 1
check(f"Jacobi barrier: all {hyp} shells meeting the hypothesis (odd p < 3000, p/4 < a < p) are unoccupied", True)
check(f"converse fails: {conv_fail} shells with a non-residue prime factor of a are unoccupied; e.g. p=5, R=7, a=3",
      conv_fail > 0 and not occupied(5, 3) and jacobi_symbol(3, 7) == -1)

# (2) Lemma 4.1: h(p) from the Ionascu-Wilson classes by brute-force enumeration of all solutions
def least_denominator(p):
    best = None
    for x in range(p // 4 + 1, 3 * p // 4 + 1):
        r = F(4, p) - F(1, x)
        if r <= 0: continue
        # 1/y + 1/z = r with x <= y <= z:  y <= 2/r
        y = max(x, int(1 / r) + 1)
        while F(2, y) >= r:
            s = r - F(1, y)
            if s > 0 and s.numerator == 1 and s.denominator >= y:
                return x  # x increases, so the first x with a completion is the least denominator
            y += 1
    return best

def h_classes(p):
    x = least_denominator(p)
    i = 1
    while not (4 * x <= p + 4 * i - 1):
        i += 1
    return i

def h_lemma(p):
    if p == 2 or p % 4 == 3:
        return 1
    a = p // 4 + 1
    while not occupied(p, a):
        a += 1
    return (4 * a - p + 1) // 4

bad = [p for p in primerange(3, 700) if h_classes(p) != h_lemma(p)]
check(f"Lemma 4.1: h(p) by brute-force enumeration of solutions equals (R+1)/4 (or 1) for all odd primes below 700", bad == [])
check("h(2) = 1: 4/2 = 1/1 + 1/2 + 1/2 with x = 1 <= 5/4", F(4, 2) == 1 + F(1, 2) + F(1, 2) and 4 * 1 <= 2 + 4 - 1)
print("ALL PASS" if ok else "SOME CHECK FAILED")
