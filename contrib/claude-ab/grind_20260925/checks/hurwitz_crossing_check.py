# claude-ab: zero trajectories of zeta(s, 1+t) for t in [0, 1] (the owner's shifted flow), continued from the first
# five zeros of zeta at t = 0; detects sign changes of Re rho(t) - 1/2 at non-Eulerian times t (erratum to
# FLIP_FABLE Addendum 4). Each crossing time is then refined by bisection on Re rho(t) - 1/2 = 0.
import mpmath as mp
mp.mp.dps = 25
Z = lambda s, t: mp.zeta(s, 1 + t)
def track(rho0, t0, t1, dt):
    pts = [(t0, rho0)]; r = rho0; t = t0
    while t < t1 - 1e-12:
        tn = min(t + dt, t1)
        guess = r if len(pts) < 2 else r + (r - pts[-2][1])*(tn - t)/(t - pts[-2][0])
        r = mp.findroot(lambda s: Z(s, tn), guess)
        t = tn; pts.append((t, r))
    return pts
def rho_at(t, rho_prev):
    return mp.findroot(lambda s: Z(s, t), rho_prev)
results = []
for n in range(1, 6):
    rho0 = mp.zetazero(n)
    pts = track(rho0, mp.mpf(0), mp.mpf(1), mp.mpf('0.005'))
    signs = [(t, r.real - 0.5) for t, r in pts]
    for (ta, da), (tb, db) in zip(signs[1:], signs[2:]):      # skip t = 0 itself
        if da*db < 0:
            # bisection on t for Re rho(t) = 1/2, following the trajectory
            lo, hi = ta, tb; rlo = [r for t, r in pts if t == ta][0]
            for _ in range(45):
                mid = (lo + hi)/2; rm = rho_at(mid, rlo)
                if (rm.real - 0.5)*da > 0: lo, rlo = mid, rm
                else: hi = mid
            rc = rho_at((lo+hi)/2, rlo)
            results.append((n, (lo+hi)/2, rc))
            print("zero %d of zeta: crosses Re s = 1/2 at t = %s, s = %s, |zeta(s,1+t)| = %s"
                  % (n, mp.nstr((lo+hi)/2, 12), mp.nstr(rc, 12), mp.nstr(abs(Z(rc, (lo+hi)/2)), 3)))
    print("zero %d: Re c1 sign at t=0+: %s ; end point at t = 1: %s" % (n, '+' if signs[1][1] > 0 else '-', mp.nstr(pts[-1][1], 12)))
print("crossings at non-Eulerian times found:", len(results))
