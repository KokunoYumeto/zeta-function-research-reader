#!/usr/bin/env python3
"""Robust zeros of zeta(s)-1 in [SL,SR] x [TLO,THI]: adaptive-boundary winding numbers,
recursive subdivision to boxes containing exactly one root, then Newton. Certifies total count."""
import sys, numpy as np, time
from flint import acb, ctx, acb_series
ctx.prec = 64
TLO, THI, out = float(sys.argv[1]), float(sys.argv[2]), sys.argv[3]
SL, SR = -1.5, 3.4
def cval(z): return complex(float(z.real.mid()), float(z.imag.mid()))
cache = {}
def f(z):
    key = (round(z.real, 12), round(z.imag, 12))
    if key not in cache:
        cache[key] = cval(acb(z.real, z.imag).zeta() - 1)
    return cache[key]
def fp(z): return cval(acb_series([acb(z.real, z.imag), 1]).zeta()[1])

def seg_arg(a, b, fa, fb, depth=0):
    d = np.angle(fb / fa)
    if (abs(d) < 0.35 or depth > 18):
        return d
    m = (a + b) / 2; fm = f(m)
    return seg_arg(a, m, fa, fm, depth + 1) + seg_arg(m, b, fm, fb, depth + 1)
def winding(x0, x1, y0, y1, n=8):
    corners = [complex(x0, y0), complex(x1, y0), complex(x1, y1), complex(x0, y1), complex(x0, y0)]
    tot = 0.0
    for i in range(4):
        A, B = corners[i], corners[i + 1]
        pts = [A + (B - A) * j / n for j in range(n + 1)]
        vals = [f(p) for p in pts]
        for j in range(n):
            tot += seg_arg(pts[j], pts[j + 1], vals[j], vals[j + 1])
    w = tot / (2 * np.pi)
    return int(round(w)), abs(w - round(w))
def newton(z, it=60):
    for _ in range(it):
        st = f(z) / fp(z); z = z - st
        if abs(st) < 1e-11 * max(1.0, abs(z)): return z, True
    return z, False
roots = []; bad = 0
def solve(x0, x1, y0, y1, cnt, depth=0):
    global bad
    if cnt == 0: return
    if cnt == 1 and (x1 - x0) < 0.25 and (y1 - y0) < 0.25:
        z, ok = newton(complex((x0 + x1) / 2, (y0 + y1) / 2))
        if ok and x0 - 1e-9 <= z.real <= x1 + 1e-9 and y0 - 1e-9 <= z.imag <= y1 + 1e-9:
            roots.append(z); return
    if depth > 40 or (x1 - x0) < 1e-7:
        z, ok = newton(complex((x0 + x1) / 2, (y0 + y1) / 2))
        if abs(z - complex((x0 + x1) / 2, (y0 + y1) / 2)) < 1e-6:
            roots.append(z); return
        bad += 1; print("unresolved box", x0, x1, y0, y1, cnt, flush=True); return
    # split the longer side (with a slightly irrational offset to avoid hitting roots)
    if (x1 - x0) >= (y1 - y0):
        xm = x0 + (x1 - x0) * 0.4999731
        c1, e1 = winding(x0, xm, y0, y1); solve(x0, xm, y0, y1, c1, depth + 1)
        solve(xm, x1, y0, y1, cnt - c1, depth + 1)
    else:
        ym = y0 + (y1 - y0) * 0.5000269
        c1, e1 = winding(x0, x1, y0, ym); solve(x0, x1, y0, ym, c1, depth + 1)
        solve(x0, x1, ym, y1, cnt - c1, depth + 1)
t0 = time.time(); total = 0; k = TLO; maxerr = 0
while k < THI:
    y0, y1 = k + 0.0031415, min(k + 1, THI) + 0.0031415
    cnt, err = winding(SL, SR, y0, y1); maxerr = max(maxerr, err)
    total += cnt
    solve(SL, SR, y0, y1, cnt)
    cache.clear()
    k += 1
    if int(k) % 100 == 0: print(f"t<={k}: winding total {total}, roots {len(roots)}, bad {bad}, max winding error {maxerr:.1e}, {time.time()-t0:.0f}s", flush=True)
roots = sorted(roots, key=lambda z: z.imag)
rho = np.array(roots)
zp = np.array([fp(z) for z in rho]); z1 = np.array([cval(acb(z.real + 1, z.imag).zeta() - 1) for z in rho])
np.savez(out, rho=rho, zp=zp, z1=z1, total=total)
print("saved", out, "roots", len(rho), "winding total", total, "bad", bad, "max winding error", maxerr)
