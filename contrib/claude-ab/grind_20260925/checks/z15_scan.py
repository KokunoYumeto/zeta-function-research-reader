# Zeros of the even lattice sum Z_a(s) = zeta(s,a) + zeta(s,1-a) at a = 1/5, off the critical line.
# Z_{1/5}(s) = (5^s/2) F(s),  F(s) = (1-5^{-s}) zeta(s) + L(s, chi_5),  chi_5 = (./5) (even, real).
import mpmath as mp, sys
mp.mp.dps = 20
chi5 = [0, 1, -1, -1, 1]
F = lambda s: (1 - mp.power(5, -s))*mp.zeta(s) + mp.dirichlet(s, chi5)
Z = lambda s: mp.zeta(s, mp.mpf(1)/5) + mp.zeta(s, mp.mpf(4)/5)
# identity check Z = 5^s F / 2 at two points
for s in (mp.mpc(0.7, 13.1), mp.mpc(1.3, 40.2)):
    assert abs(Z(s) - mp.power(5, s)*F(s)/2) < 1e-12*abs(Z(s))
T0, T1, dt = float(sys.argv[1]), float(sys.argv[2]), 0.05
found = []
for sig in (0.6, 0.7, 0.8, 0.9, 1.0, 1.1):
    ts = [T0 + k*dt for k in range(int((T1-T0)/dt)+1)]
    vals = [abs(F(mp.mpc(sig, t))) for t in ts]
    for k in range(1, len(ts)-1):
        if vals[k] < vals[k-1] and vals[k] < vals[k+1] and vals[k] < 0.25:
            try:
                r = mp.findroot(F, mp.mpc(sig, ts[k]))
            except Exception:
                continue
            if abs(F(r)) < 1e-12 and r.real > 0.5 + 1e-6 and T0 - 1 < r.imag < T1 + 1:
                if all(abs(r - q) > 1e-6 for q in found):
                    found.append(r)
found.sort(key=lambda z: float(z.imag))
for r in found:
    print("zero of Z_{1/5}: beta = %s  gamma = %s   |F| = %s" % (mp.nstr(r.real, 12), mp.nstr(r.imag, 12), mp.nstr(abs(F(r)), 2)))
print("count with beta > 1/2 in [%g, %g]:" % (T0, T1), len(found))
