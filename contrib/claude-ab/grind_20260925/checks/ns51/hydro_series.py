"""Exact Taylor coefficients of the hydrodynamic shear root of the Rindler (flat cutoff) shear condition.

Condition (continuation RESEARCH.md (16), (26)): I'_alpha(q) = 0  <=>  G(alpha, x) = 0 with x = q^2/4 and
    G(alpha, x) = sum_{m>=0} (alpha + 2m) x^m / (m! (1+alpha)_m),
since q I'_alpha(q) = (q/2)^alpha / Gamma(1+alpha) * G(alpha, x).  G(alpha, 0) = alpha, G_alpha(0, 0) = 1, so the
hydrodynamic root alpha_h(x) = sum_{k>=1} a_k x^k is the unique power series with alpha_h(0) = 0 (implicit function
theorem).  Here it is computed exactly (rational arithmetic, python-flint fmpq_series) by Newton iteration.
Output: a_k for k <= N, the check against (27), and ratio / root-test estimates of the radius in x.
"""
import sys, time
sys.set_int_max_str_digits(0)
from flint import fmpq_series, fmpq, arb, ctx

N = int(sys.argv[1]) if len(sys.argv) > 1 else 120
T0 = time.time()
ctx.cap = N + 2   # python-flint caps series length at ctx.cap (default 10)

def G_and_Ga(alpha, prec):
    x = fmpq_series([0, 1], prec=prec)
    one = fmpq_series([1], prec=prec)
    G = fmpq_series([0], prec=prec)
    Ga = fmpq_series([0], prec=prec)
    invP = one            # 1/(1+alpha)_m
    S = fmpq_series([0], prec=prec)   # sum_{k=1}^m 1/(k+alpha)
    xm = one              # x^m / m!
    for m in range(0, prec):
        if m > 0:
            inv_k = 1 / (fmpq_series([m], prec=prec) + alpha)
            invP = invP * inv_k
            S = S + inv_k
            xm = xm * x / m
        t = xm * invP
        G = G + t * (alpha + 2*m)
        Ga = Ga + t * (one - (alpha + 2*m) * S)
    return G, Ga

# Newton iteration with precision doubling
alpha = fmpq_series([0, -2], prec=2)
p = 2
while p < N + 1:
    p = min(2*p, N + 1)
    a = fmpq_series([alpha.coeffs()[i] if i < len(alpha.coeffs()) else 0 for i in range(p)], prec=p)
    G, Ga = G_and_Ga(a, p)
    alpha = a - G / Ga
G, Ga = G_and_Ga(alpha, N + 1)
co = alpha.coeffs()
assert all(c == 0 for c in G.coeffs()), "G(alpha_h(x), x) != 0 to the computed order"
ak = [fmpq(0)] * (N + 1)
for i, c in enumerate(co):
    ak[i] = c
print(f"computed a_k for k <= {N} exactly in {time.time()-T0:.1f}s; G(alpha_h(x),x) = O(x^{N+1}) verified exactly")
# compare with (27): alpha = -q^2/2 - 3q^4/16 - 29 q^6/192 - 2843 q^8/18432 - 392029 q^10/2211840, q^2 = 4x
claim = [fmpq(-1, 2)*4, fmpq(-3, 16)*16, fmpq(-29, 192)*64, fmpq(-2843, 18432)*256, fmpq(-392029, 2211840)*1024]
print("(27) coefficients reproduced:", all(ak[k+1] == claim[k] for k in range(5)))
print("a_1..a_6 =", [str(ak[k]) for k in range(1, 7)])
print("all a_k < 0 for 1 <= k <=", N, ":", all(ak[k] < 0 for k in range(1, N + 1)))
ctx.prec = 200
xc = (arb("0.778472800990330076180356446189")**2)/4
print("x_c = q_c^2/4 =", xc.str(20))
for k in [10, 20, 40, 60, 80, 100, 120, 160, 200, 239]:
    if k + 1 <= N:
        r = arb(ak[k]) / arb(ak[k+1])
        # Darboux: a_k ~ C x_c^{-k} k^{-3/2}  =>  a_k/a_{k+1} ~ x_c (1 + 3/(2k) + ...)
        corr = r / (1 + arb(3)/(2*k))
        root = (arb(-1)/arb(ak[k])) ** (arb(1)/k)
        print(f"k={k:4d}: a_k/a_(k+1) = {r.str(12)}; corrected by (1+3/(2k)): {corr.str(12)}; |a_k|^(-1/k) = {root.str(8)}")
KEEP = min(N, 60)      # the exact rationals grow to thousands of digits; the first 60 are kept in the file
with open('hydro_series_coeffs_first60.txt', 'w') as f:
    f.write("# k  numerator  denominator   (alpha_h(x) = sum_k a_k x^k, x = q^2/4)\n")
    for k in range(1, KEEP + 1):
        f.write(f"{k} {ak[k].p} {ak[k].q}\n")
print("digits of the denominator of a_N:", len(str(ak[N].q)))
print(f"total {time.time()-T0:.1f}s")
