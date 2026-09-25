# Referee independent check (python-flint / Arb): zeros of Z_{1/5}(s) = zeta(s,1/5) + zeta(s,4/5).
# (1) adaptive-step argument principle on rectangles [s0, s1] x [t0, t1]; a step is accepted only if
#     |Z(next) - Z(cur)| < 0.5 |Z(cur)|, so each accepted phase increment is < pi/6 in absolute value (no aliasing).
import sys, cmath, math
from flint import acb, ctx
ctx.prec = 80
A1 = acb(1)/5; A4 = acb(4)/5
def Z(s):
    v = acb(s).zeta(A1) + acb(s).zeta(A4)
    return complex(float(v.real.mid()), float(v.imag.mid()))

def edge_phase(a, b, h0=0.02):
    total = 0.0; cur = a; zc = Z(cur); L = abs(b - a); pos = 0.0; h = h0
    while pos < L - 1e-15:
        h = min(h, L - pos)
        while True:
            nxt = a + (b - a)*((pos + h)/L)
            zn = Z(nxt)
            if abs(zn - zc) < 0.5*abs(zc):
                break
            h /= 2
            if h < 1e-9:
                raise RuntimeError("zero on contour near %s" % nxt)
        total += cmath.phase(zn/zc); pos += h; cur, zc = nxt, zn
        h = min(2*h, h0)
    return total

def count(s0, s1, t0, t1):
    c = [complex(s0, t0), complex(s1, t0), complex(s1, t1), complex(s0, t1)]
    tot = sum(edge_phase(c[i], c[(i+1) % 4]) for i in range(4))
    return tot/(2*math.pi)

if __name__ == "__main__":
    s0, s1, t0, t1 = map(float, sys.argv[1:5])
    w = count(s0, s1, t0, t1)
    print("Z_{1/5}: rectangle [%g,%g]x[%g,%g]  winding = %.6f" % (s0, s1, t0, t1, w), flush=True)
