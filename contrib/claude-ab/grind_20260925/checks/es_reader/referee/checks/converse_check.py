# Conditional converse: if 2 v_l(a) >= ord_R(l) - 1 for every prime l | a, then
# {u mod R : u | a^2} = H := <l mod R : l | a>, and the shell is occupied iff -1 in H or -4^{-1} in H;
# for prime R = 3 mod 4: occupied iff some prime factor of a is a quadratic non-residue mod R.
from sympy import primerange, divisors, factorint, n_order, isprime, legendre_symbol
def subgroup(gens, R):
    H = {1 % R}; fr = [1 % R]
    while fr:
        x = fr.pop()
        for g in gens:
            y = x*g % R
            if y not in H: H.add(y); fr.append(y)
    return H
tested = bad = badprime = 0
for p in primerange(3, 6000):
    for a in range(p//4 + 1, p):
        R = 4*a - p
        if R < 3: continue
        f = factorint(a)
        if not all(2*e >= n_order(l, R) - 1 for l, e in f.items()): continue
        tested += 1
        H = subgroup([l % R for l in f], R)
        res = {u % R for u in divisors(a*a)}
        occ = ((-pow(4, -1, R)) % R in res) or ((-a) % R in res)
        if res != H: bad += 1
        if occ != (((R - 1) in H) or ((-pow(4, -1, R)) % R in H)): bad += 1
        if isprime(R) and R % 4 == 3 and occ != any(legendre_symbol(l, R) == -1 for l in f): badprime += 1
print("shells with the exponent condition (odd p < 6000):", tested, "; mismatches:", bad, "; prime-R mismatches:", badprime)
