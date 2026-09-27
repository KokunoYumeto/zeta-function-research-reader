# claude-ab referee checks for Theorem E (copy-newresults, round 2): the arithmetic facts used in steps 3-5.
from fractions import Fraction as Fr
from math import gcd
ok = True
# Step 3: q1*qn in Q_a iff n/a is an integer (q_n = 1 + n/a)
for a in [Fr(1), Fr(1,2), Fr(2), Fr(3,4), Fr(2,3), Fr(5,2), Fr(1,3)]:
    for n in range(1, 12):
        q1, qn = 1 + 1/a, 1 + n/a
        prod = q1*qn
        m = (prod - 1)*a                     # prod = 1 + m/a ; in Q_a iff m is a nonnegative integer
        inQ = (m.denominator == 1 and m >= 0)
        ok &= (inQ == ((n/a).denominator == 1))
print("step 3 (q1 qn in Q_a iff n/a in Z):", ok)
# Step 4: (1+2v)^k1 = (1+v)^k2 impossible (coprime bases > 1); (1+3v)/(1+v) = 2 only at v = 1
for v in range(1, 200):
    ok &= gcd(1+2*v, 1+v) == 1
    if Fr(1+3*v, 1+v) == 2: ok &= (v == 1)
print("step 4 (coprime bases; ratio 2 only at v=1):", ok)
# Step 5: for q>=3 find primes r (order o>=2 mod q) and r' = r^{-1} mod q; check r^o, r'^o, r r' in Q_a with only trivial divisors in Q_a
def primes(N):
    s = [True]*(N+1); s[0] = s[1] = False
    for i in range(2, int(N**0.5)+1):
        if s[i]: s[i*i::i] = [False]*len(s[i*i::i])
    return [i for i in range(N+1) if s[i]]
P = primes(5000)
for q in range(3, 30):
    r = next(p for p in P if gcd(p, q) == 1 and p % q != 1)
    o = next(k for k in range(1, q+1) if pow(r, k, q) == 1)
    rinv = pow(r, -1, q)
    r2 = next(p for p in P if p != r and p % q == rinv)
    elems = [r**o, r2**o, r*r2]
    ok &= all(x % q == 1 for x in elems)
    # proper divisors > 1 of r^o are r^j (1<=j<o), of r2^o are r2^j, of r*r2 are r and r2: none may be 1 mod q
    ok &= all(pow(r, j, q) != 1 for j in range(1, o)) and all(pow(r2, j, q) != 1 for j in range(1, o))
    ok &= (r % q != 1) and (r2 % q != 1)
print("step 5 (Dirichlet witnesses exist, pure elements, q=3..29):", ok)
print("ALL PASS" if ok else "FAILURE")
