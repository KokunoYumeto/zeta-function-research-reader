from sympy import primerange, divisors
H = {1, 121, 169, 289, 361, 529}
nm = ne = bm = be = 0; eqm = []
for p in primerange(2, 60000):
    if p % 840 not in H: continue
    for a in range(p//4 + 1, (p+1)//2):
        R = 4*a - p
        D = divisors(a*a)
        if any((u + a) % R == 0 for u in D):
            nm += 1
            if not 11*a <= 3*(p + 3): bm += 1
            if 11*a == 3*(p + 3): eqm.append(p)
        if any((4*u + 1) % R == 0 for u in D):
            ne += 1
            if not 22*(p + 1) <= 23*(p - 2*a + 1)**2: be += 1
print("hard primes < 6e4: middle-state shells", nm, "violations of 11a <= 3(p+3):", bm, "equality at:", eqm[:5])
print("exterior-state shells", ne, "violations of 22(p+1) <= 23(p-2a+1)^2:", be)
