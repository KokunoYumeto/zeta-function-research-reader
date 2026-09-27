# Referee: locate every zero of Z_{1/5} in [s0, s1] x [t0, t1] by adaptive argument-principle bisection (flint),
# then refine each with mpmath findroot (30 digits) on the Hurwitz form and verify.
import sys, math
import mpmath as mp
from flint_count import count, Z as Zf
mp.mp.dps = 30
Zm = lambda s: mp.zeta(s, mp.mpf(1)/5) + mp.zeta(s, mp.mpf(4)/5)
found = []
def search(s0, s1, t0, t1):
    w = count(s0, s1, t0, t1); c = int(round(w))
    assert abs(w - c) < 1e-6, (s0, s1, t0, t1, w)
    if c == 0: return
    if c == 1 and (t1 - t0) < 0.6 and (s1 - s0) < 0.6:
        r = mp.findroot(Zm, mp.mpc((s0+s1)/2, (t0+t1)/2))
        ok = s0 - 1e-9 <= r.real <= s1 + 1e-9 and t0 - 1e-9 <= r.imag <= t1 + 1e-9 and abs(Zm(r)) < 1e-25
        found.append((r, ok)); return
    if (t1 - t0) >= (s1 - s0):
        tm = (t0 + t1)/2 + 0.00731; search(s0, s1, t0, tm); search(s0, s1, tm, t1)
    else:
        sm = (s0 + s1)/2 + 0.000731; search(s0, sm, t0, t1); search(sm, s1, t0, t1)

if __name__ == "__main__":
    s0, s1, t0, t1 = map(float, sys.argv[1:5])
    search(s0, s1, t0, t1)
    found.sort(key=lambda x: float(x[0].imag))
    listed = [15.7040482679, 29.9481698117, 43.7596602283, 61.0369079062, 64.8940709677, 75.5714257059, 79.5064291171,
              107.216273768, 110.759409181, 120.652085316, 127.454740226, 134.833936498, 141.678876384]
    for r, ok in found:
        inlist = any(abs(float(r.imag) - g) < 1e-6 for g in listed)
        print("beta = %.12f  gamma = %.10f  verified=%s  in note's list=%s" % (float(r.real), float(r.imag), ok, inlist))
    print("total located:", len(found), " all verified:", all(ok for _, ok in found))
