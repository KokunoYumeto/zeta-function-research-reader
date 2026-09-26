#!/usr/bin/env python3
"""F20 and F21 verification (independent code).

F20: R(x) = sqrt(r/t) sinh(x log r)/sinh(x log t) on 0 < x < 1/2 is increasing iff r > t (grid of pairs, 2000 points each),
     and its limits are sqrt(r/t) log r/log t (x -> 0) and (r-1)/(t-1) (x = 1/2).
F21(i): Lemma 5.5 with real-valued nu, on K = Z/3: nu(1) = 1, nu(tau) = nu(conj tau) = -x.  For genuine rho = a + b tau + c tau^2,
     nu(rho conj rho) = a^2+b^2+c^2 - 2x(ab+bc+ca).  Exhaustive search over 0 <= a,b,c <= 12: the hypothesis holds iff x <= 1/2,
     i.e. iff sum_{tau != 1} d_tau (-nu(tau)) = 2x <= 1.  At x = 1/2 two nontrivial characters are negative: the integer
     dichotomy ("at most one tau, quadratic, nu = -1") needs integrality.
F21(ii): Lemma 5.6 with delta_n <= C D^n: a = (1.5 e^{+-0.3i}, -0.7), delta_n = 2 D^n + 1: nonnegative for all n <= 2000
     when D >= 1.5 = max|a_j|, and fails for D = 1.45; plus an elliptic curve over F_7: #E(F_{7^n}) = 1 + 7^n - alpha^n - beta^n >= 0,
     |alpha| = sqrt 7 <= 7 (the trivial bound the lemma gives with delta_n = 1 + 7^n <= 2*7^n).
"""
import mpmath as mp
import itertools

mp.mp.dps = 30

def main():
    print("F20: direction of monotonicity")
    pairs = [(r, t) for r in (1.1, 2, 5, 30, 100) for t in (1.1, 2, 5, 30, 100) if r != t]
    for r, t in pairs:
        r, t = mp.mpf(r), mp.mpf(t)
        R = lambda x: mp.sqrt(r / t) * mp.sinh(x * mp.log(r)) / mp.sinh(x * mp.log(t))
        xs = [mp.mpf(k) / 4000 for k in range(1, 2001)]
        vals = [R(x) for x in xs]
        inc = all(vals[i + 1] > vals[i] for i in range(len(vals) - 1))
        dec = all(vals[i + 1] < vals[i] for i in range(len(vals) - 1))
        lim0 = mp.sqrt(r / t) * mp.log(r) / mp.log(t); lim_half = (r - 1) / (t - 1)
        assert (inc and r > t) or (dec and r < t)
        assert abs(R(mp.mpf(10) ** -12) - lim0) < 1e-9 and abs(R(mp.mpf(0.5)) - lim_half) < 1e-20
    print("  %d ordered pairs (r,t) from {1.1,2,5,30,100}: strictly increasing exactly when r > t, decreasing when r < t; endpoint values confirmed" % len(pairs))

    print("F21(i): Lemma 5.5 with real-valued nu on Z/3")
    def ok(x):
        for a, b, c in itertools.product(range(13), repeat=3):
            if a + b + c == 0:
                continue
            if a * a + b * b + c * c - 2 * x * (a * b + b * c + c * a) < -1e-12:
                return False, (a, b, c)
        return True, None
    for x in (0.3, 0.5, 0.5 + 1e-3, 0.6):
        good, wit = ok(x)
        print("  nu(tau) = nu(tau^2) = -%.4f: hypothesis nu(rho rho*) >= 0 for all genuine rho (a,b,c <= 12): %s%s; sum d_tau(-nu) = %.4f"
              % (x, good, "" if good else " (violated at %s)" % (wit,), 2 * x))
        assert good == (2 * x <= 1)

    print("F21(ii): Lemma 5.6 with delta_n <= C D^n")
    a = [mp.mpf(1.5) * mp.exp(0.3j), mp.mpf(1.5) * mp.exp(-0.3j), mp.mpf(-0.7)]
    for D in (1.6, 1.5, 1.45):
        bad = None
        for n in range(1, 2001):
            val = 2 * mp.mpf(D) ** n + 1 - mp.fsum(x ** n for x in a)
            assert abs(val.imag) < 1e-20 * (1 + abs(val.real))
            if val.real < 0:
                bad = n; break
        print("  D = %.2f: delta_n - sum a_j^n >= 0 for all n <= 2000: %s%s" % (D, bad is None, "" if bad is None else " (fails first at n = %d)" % bad))
        assert (bad is None) == (D >= 1.5)
    # elliptic curve y^2 = x^3 + x + 3 over F_7
    p = 7
    cnt = 1 + sum(1 for x in range(p) for y in range(p) if (y * y - (x ** 3 + x + 3)) % p == 0)
    ap = p + 1 - cnt
    alpha = (ap + mp.sqrt(mp.mpf(ap) ** 2 - 4 * p)) / 2
    beta = (ap - mp.sqrt(mp.mpf(ap) ** 2 - 4 * p)) / 2
    counts = [1 + p ** n - (alpha ** n + beta ** n) for n in range(1, 21)]
    print("  E: y^2 = x^3+x+3 over F_7: #E(F_7) = %d, a_p = %d, |alpha| = %s = sqrt(7); counts n<=20 all >= 0: %s; lemma bound max|alpha| <= 7"
          % (cnt, ap, mp.nstr(abs(alpha), 12), all(c.real >= 0 for c in counts)))
    print("ALL F20/F21 CHECKS PASS")

if __name__ == "__main__":
    main()
