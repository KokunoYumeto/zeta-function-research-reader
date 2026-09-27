# Referee independent check: count zeros of F(s) = (1-5^{-s}) zeta(s) + L(s,chi_5)  (Z_{1/5} = 5^s F / 2)
# in rectangles via the argument principle with adaptive steps; also scan F on the real axis in (1/2, 1).
import mpmath as mp, sys
mp.mp.dps = 18
chi5 = [0, 1, -1, -1, 1]
def F(s):
    return (1 - mp.power(5, -s))*mp.zeta(s) + mp.dirichlet(s, chi5)

def winding(path_pts, maxstep=0.05):
    # path_pts: list of corners (closed polygon, counterclockwise)
    total = mp.mpf(0)
    for (a, b) in zip(path_pts, path_pts[1:] + path_pts[:1]):
        a = mp.mpc(a); b = mp.mpc(b)
        L = abs(b - a); n = max(2, int(L/maxstep))
        prev_s = a; prev = F(a)
        k = 1
        while k <= n:
            s = a + (b - a)*k/n
            v = F(s)
            d = mp.arg(v/prev)
            if abs(d) > 0.5:   # refine this sub-step
                m = 16
                sub_prev = prev
                for j in range(1, m+1):
                    ss = prev_s + (s - prev_s)*j/m
                    vv = F(ss)
                    dd = mp.arg(vv/sub_prev)
                    if abs(dd) > 1.0:
                        raise RuntimeError("step too coarse near %s" % ss)
                    total += dd; sub_prev = vv
            else:
                total += d
            prev = v; prev_s = s; k += 1
    return total/(2*mp.pi)

if __name__ == "__main__":
    s0 = float(sys.argv[1]); s1 = float(sys.argv[2]); t0 = float(sys.argv[3]); t1 = float(sys.argv[4])
    w = winding([mp.mpc(s0, t0), mp.mpc(s1, t0), mp.mpc(s1, t1), mp.mpc(s0, t1)])
    print("rectangle [%g,%g]x[%g,%g]: winding number = %s" % (s0, s1, t0, t1, mp.nstr(w, 8)))
