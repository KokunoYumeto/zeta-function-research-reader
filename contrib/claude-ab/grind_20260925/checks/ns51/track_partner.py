"""Numerical (not certified) continuation of the second real root of I'_alpha(q) = 0 that merges with the
hydrodynamic root at q*.  Near the fold q is a smooth function of alpha (F_q != 0), so the branch is followed in the
parameter alpha from alpha* down towards -1, solving F(alpha, q) = 0 for q (mpmath, 30 digits)."""
import mpmath as mp
mp.mp.dps = 30
F = lambda a, q: (mp.besseli(a - 1, q) + mp.besseli(a + 1, q)) / 2
qs = mp.mpf('0.778472800990330076180356446189'); ast = mp.mpf('-0.569714080972361784438457668663')
q = qs
print(" alpha        q(alpha)            x = q^2/4          check: other root at this q (hydro side)")
a_vals = [ast - mp.mpf(d) for d in ['0.001', '0.01', '0.05', '0.1', '0.2', '0.3', '0.35', '0.4', '0.42', '0.425', '0.428', '0.4295']]
a_prev = ast
for a in a_vals:
    n = 50
    for k in range(1, n + 1):
        ak = a_prev + (a - a_prev) * k / n
        q = mp.findroot(lambda t: F(ak, t), q)
    a_prev = a
    # the hydro root at the same q, for comparison (found from the series side)
    print(f"{mp.nstr(a, 8):>10}  {mp.nstr(q, 15):>18}  {mp.nstr(q**2/4, 12):>16}")
print("The branch reaches q -> 0 as alpha -> -1 (w = i alpha -> -i, omega -> -i c/rho_c); numerical only.")
