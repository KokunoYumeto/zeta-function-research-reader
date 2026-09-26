# Referee 21 (wbreader): Collatz checks independent of the author's script.
from fractions import Fraction as Fr
import math, random
def T(n):
    x = 3*n+1; a = (x & -x).bit_length()-1; return x >> a, a
# Theorem 2.8: least m with 3^m < 2^A <= (3+1/s)^m, s = 330751, exact integers: 2^A * s^m <= (3s+1)^m
s = 330751
m = 1
while True:
    A = (3**m).bit_length()   # least A with 2^A > 3^m
    if 2**A * s**m <= (3*s+1)**m: break
    m += 1
print("least m:", m, "A:", A)
# minimal k with (4s)^m <= 2^k (3s+1)^m at that m
lhs = (4*s)**m; rhs = (3*s+1)**m; k = 0
while lhs > 2**k * rhs: k += 1
print("k >=", k, "; float m*log2(4s/(3s+1)) =", m*math.log2(4*s/(3*s+1)))
# also check with the workbench's (C37) m=1634: (4s)^1634 > 2^678 (3s+1)^1634
print("(C37):", (4*s)**1634 > 2**678 * (3*s+1)**1634)
# also: is s=330751 the right least element?  330749 is odd; 330750 is even -> next odd 330751
print("next odd after 330749:", 330751)
# Prop 2.7: D_m = 2*4^(m-1) - 3^m, D_1 = D_2 = -1, D_3 = 5, recursion D_{m+1} = 4D_m + 3^m
D = lambda m: 2*4**(m-1) - 3**m
print("D_1..D_6:", [D(i) for i in range(1,7)], " recursion ok:", all(D(i+1) == 4*D(i)+3**i for i in range(1,50)))
print("n for m=1,2:", [(2*4**(i-1)-3**(i-1))//D(i) for i in (1,2)])
# Theorem 2.4 example e=8, b=2, sigma=0
e, b, sig = 8, 2, 0
he = (2**e+2)//3
a = 1
while not 2**(a+e+2*b-sig) < 3**(a+b): a += 1
J = 2**(e+2*b-sig); Q = 3**(a+b); K = 2**a*J; d, r = 4, 3
x = (-he*3**b*pow(J, -1, Q)) % Q
n0 = next(x+i*Q for i in range(d) if (x+i*Q) % d == r)
m0 = (K*n0 + 2**a*he*3**b)//Q - 1
print("a =", a, " dQ =", d*Q, " dK =", d*K, " n0 =", n0, " m0 =", m0, " T(n0) =", T(n0)[0], " 3dQ/2 =", 3*d*Q//2)
# words for v = 0 and a random large v
for v in (0, 12345678901234567890):
    n = n0 + d*Q*v; mm = m0 + d*K*v
    yn, an = T(n); w = []; y = mm
    for _ in range(a+1+(b-1)+1):
        y, aa = T(y); w.append(aa)
    print(" v =", v, " n word (1)?", an == 1, " m word:", w[:a]==[1]*a, w[a:], " same endpoint:", y == yn, " m<n:", mm < n)
# Lemma 2.3 via LTE, all even e <= 5000
def nu(n, p):
    k = 0
    while n % p == 0: n //= p; k += 1
    return k
print("Lemma 2.3 (e<=5000):", all((2**e+2) % 3 == 0 and ((2**e+2)//3) % 4 == 2 and nu((2**e+2)//3, 3) == nu(e-1, 3) for e in range(2, 5001, 2)))
# Prop 2.6 at x = 7 and a check that x = 2 is allowed (u = 0)
f = lambda x: 0.5*(math.sqrt((x-2)/2)+math.sqrt((3*x-1)/2)) - math.sqrt(15)/4*math.sqrt(x-1)
print("Prop 2.6: f(2) =", f(2), " f(7) =", f(7), " max on [2,1e4] grid:", max(f(2+i/100) for i in range(10**6)))
# Prop 2.5 sanity: random words of reference-3 leaves -- check C < 3D implies T^m(n) < n for n >= 3 (spot)
