#!/usr/bin/env python3
"""certify_hydro_radius.py -- computer-assisted proof (Arb ball arithmetic via python-flint) that the hydrodynamic
shear root of the flat (Rindler) cutoff problem is analytic on the open disk |x| < x*, x = q^2/4, and that x* is a
square-root branch point on its boundary.  Consequently the hydrodynamic series (27) of the vacuum-hydrodynamics
continuation, alpha_h = -q^2/2 - 3q^4/16 - ..., has radius of convergence EXACTLY q*^2 in the variable q^2, where
(alpha*, q*) is the certified pole collision (certify_collision.py).  Along 0 < q < q* the hydrodynamic root is real
(the mode is purely damped) and it is one of the two real roots that merge at q*.

Spectral function.  With x = q^2/4 and (1+alpha)_m the rising factorial,
    q I'_alpha(q) = (q/2)^alpha / Gamma(1+alpha) * G(alpha, x),   G(alpha, x) = sum_{m>=0} (alpha+2m) x^m / (m! (1+alpha)_m).
For |alpha| <= 0.95 the factor Gamma(1+alpha)(q/2)^(-alpha) is finite and nonzero, so G = 0 <=> I'_alpha(q) = 0 and
G = G_alpha = 0 <=> I' = I'_alpha-derivative = 0.  G(alpha, 0) = alpha, so the hydrodynamic root alpha_h(x) is the unique
analytic root with alpha_h(0) = 0.

Rigorous tail.  For |alpha| <= a <= 0.95, |x| <= X <= 0.2, m >= M = 30 the terms t_m of G and their alpha-derivatives
satisfy |t_m| <= b_m := (a+2m) X^m / (m! prod_{k=1}^m (k-a)) and |d t_m/d alpha| <= d_m := X^m/(m! prod(k-a)) *
(1 + (a+2m) sum_{k=1}^m 1/(k-a)), with b_{m+1}/b_m <= 2X/((m+1)(m+1-a)) <= 1/2 and d_{m+1}/d_m <= 5X/((m+1)(m+1-a)) <= 1/2;
hence the tails are bounded by 2 b_M and 2 d_M, which are added as ball radii.

Proof structure (each step is checked below; any failure prints FAIL):
 (T) Tiling.  The closed disk |x| <= R_hi (R_hi >= x*) minus the open square of half-width eta_in about x_c0 is covered
     by square x-cells X_i.  For each cell the Krawczyk operator K_i = c - Y G(c, X_i) + (1 - Y G_alpha(A_i, X_i))(A_i - c)
     satisfies K_i in int(A_i) for a square alpha-box A_i; then for every x in X_i, G(., x) has exactly one zero in A_i,
     it is simple, it lies in K_i, and it depends analytically on x in int(X_i).
 (C) Consistency.  For every pair of cells whose closed boxes meet, K_i is contained in A_j (and vice versa), so the
     two unique zeros coincide on the overlap.  The cell containing x = 0 has zero alpha = 0 there.  Hence the zeros
     define one analytic function on the union T of the cells: the analytic continuation of alpha_h.
 (R) Realness.  Cells in the row centred on the real axis have real centres and real-centred alpha-boxes, so by
     uniqueness the zero is real for real x.
 (F) Fold patch.  A_F = square of half-width rho_F about alpha0, X_F = square of half-width eta about x_c0.
     (a) G != 0 on (boundary of A_F) x X_F;  (b) the winding number of G(., x_c0) along the boundary of A_F is 2;
     hence for every x in X_F, G(., x) has exactly two zeros in A_F (with multiplicity), and their discriminant
     Delta(x) = (beta_1 - beta_2)^2 is analytic on X_F (power sums by the residue theorem).
     (c) On the boundary of X_F the two zeros are enclosed in disjoint Krawczyk boxes inside A_F and the winding number
     of Delta along the boundary of X_F is 1.  Hence Delta has exactly one zero in X_F, a simple one, which is x*
     (certify_collision.py puts the double zero (alpha*, x*) inside A_F x X_F).
     (d) Every tiling cell meeting X_F has K_i inside A_F, so there the continued alpha_h is one of beta_1, beta_2.
 Conclusion.  On X_F minus {x*} the two zeros are distinct, so alpha_h continues analytically over (X_F intersect
 {|x| < x*}) (convex, x* on its boundary).  Together with (T), alpha_h is analytic on {|x| < x*}.  At x* the zeros are
 (p_1 +- sqrt(Delta))/2 with a simple zero of Delta, so alpha_h is not analytic at x*; since alpha_h -> alpha* along the
 real segment, the Taylor series cannot converge on a larger disk.  Radius of convergence = x* exactly.
"""
import math, sys, time, json
from flint import acb, arb, ctx

ctx.prec = 128
T0 = time.time()
M = 30
SLACK_FAC = 3.5
AMAX = arb("0.95")
XMAX = arb("0.2")

# certified collision box (certify_collision.py): q* in q0 +- 1e-20, alpha* in a0 +- 1.5e-10
q0 = arb("0.778472800990330076180356446189")
a0 = arb("-0.569714080972361784438457668663")
xc0 = (q0 * q0 / 4).mid()
qbox = arb(q0.mid(), arb("1e-20").upper())
xstar_box = qbox * qbox / 4
R_hi = xstar_box.upper()          # upper end for x*

FACT = [arb(1)]
for m in range(1, M + 2):
    FACT.append(FACT[-1] * m)

def tails(a_up, X_up):
    """rigorous bounds 2 b_M, 2 d_M for the tails m >= M (valid for a_up <= 0.95, X_up <= 0.2)."""
    prod = arb(1); H = arb(0)
    for k in range(1, M + 1):
        prod *= (k - a_up); H += 1 / (k - a_up)
    XM = X_up ** M
    bM = (a_up + 2 * M) * XM / (FACT[M] * prod)
    dM = XM / (FACT[M] * prod) * (1 + (a_up + 2 * M) * H)
    return (2 * bM).upper(), (2 * dM).upper()

def GGa(al, x, deriv=True):
    a_up = abs(al).upper(); X_up = abs(x).upper()
    if not (a_up <= AMAX and X_up <= XMAX):
        raise ValueError("outside the tail-bound domain: |alpha| = %s, |x| = %s" % (a_up, X_up))
    G = acb(0); Ga = acb(0)
    base = acb(1)      # x^m / (m! (1+alpha)_m)
    S = acb(0)         # sum_{k=1}^m 1/(k+alpha)
    for m in range(M):
        if m > 0:
            inv = 1 / (m + al)
            base = base * x * inv / m
            S = S + inv
        c = al + 2 * m
        G = G + base * c
        if deriv:
            Ga = Ga + base * (1 - c * S)
    tG, tGa = tails(a_up, X_up)
    G = acb(G.real + arb(0, tG), G.imag + arb(0, tG))
    if deriv:
        Ga = acb(Ga.real + arb(0, tGa), Ga.imag + arb(0, tGa))
    return G, Ga

def point(z):
    return z.mid()

def newton(al, x, iters=60):
    """damped Newton with midpoint arithmetic; raises ValueError if it leaves |alpha| <= 0.9."""
    al = point(al)
    for _ in range(iters):
        G, Ga = GGa(al, x)
        step = point(G / Ga)
        if abs(step).upper() > arb("0.05"):
            step = point(step * (arb("0.05") / abs(step).upper()))
        al = point(al - step)
        if not (abs(al).upper() < arb("0.9")):
            raise ValueError("Newton left the domain")
        if abs(step).upper() < arb("1e-30"):
            break
    return al

def sqbox(c, h):
    """square acb box of half-width h (arb/float) about the point c (acb)."""
    h = arb(h).upper()
    return acb(arb(c.real.mid(), h), arb(c.imag.mid(), h))

def krawczyk(X, x0, guess, real_centre=False, need_slack=True):
    """Krawczyk test on the x-box X (x0 its centre).  Returns (ok, A, K, c)."""
    try:
        c = newton(guess, x0)
    except ValueError:
        return False, None, None, guess
    if real_centre:
        c = acb(c.real.mid())
    G0, Ga0 = GGa(c, x0)
    Y = point(1 / Ga0)
    Gm, _ = GGa(c, X, deriv=False)
    YG = Y * Gm
    base_r = abs(YG).upper()
    best = None
    for fac in (2, 3, 5, 8, 13, 21, 34, 55, 89):
        rho = arb(max(float(base_r) * fac, 1e-25))
        A = sqbox(c, rho)
        try:
            _, GaA = GGa(A, X)
        except ValueError:
            break
        K = c - YG + (1 - Y * GaA) * (A - c)
        if A.contains_interior(K):
            # slack = distance from K to the boundary of A; the largest slack best accommodates neighbours' enclosures
            slack = float(rho) - max(float(abs(K.real - c.real).upper()), float(abs(K.imag - c.imag).upper()))
            if best is None or slack > best[0]:
                best = (slack, A, K)
    # require room for the neighbours' enclosures: their zeros lie within ~2 base_r of c (diagonal neighbours of the
    # same size), plus their own enclosure radius ~ base_r; cells that do not leave this slack are subdivided
    if best is None or (need_slack and best[0] < SLACK_FAC * float(base_r)):
        return False, None, None, c
    return True, best[1], best[2], c

def box_x(cx, cy, h):
    return acb(arb(cx, h), arb(cy, h))

def dist_min(cx, cy, h, px, py):
    dx = max(abs(cx - px) - h, 0.0); dy = max(abs(cy - py) - h, 0.0)
    return math.hypot(dx, dy)

def dist_max(cx, cy, h, px, py):
    return math.hypot(abs(cx - px) + h, abs(cy - py) + h)

def square_inside_open(cx, cy, h, px, py, e):
    """cell (closed) contained in the open square of half-width e about (px, py)."""
    return abs(cx - px) + h < e and abs(cy - py) + h < e

results = []
def report(name, ok, extra=""):
    results.append((name, bool(ok)))
    print(("PASS" if ok else "FAIL") + "  " + name + (("  " + extra) if extra else ""), flush=True)

# ------------------------------------------------------------------------------------------ parameters
# Dyadic centres and half-widths: every corner and every boundary point k/64 along an edge is then an exact binary
# number, so the polygons used for the argument principle are exactly the boundaries of the boxes A_F and X_F.
XC = round(float(xc0) * 2**24) / 2**24          # dyadic centre of X_F (|XC - x_c0| < 3e-8)
AL0 = round(float(a0) * 2**24) / 2**24          # dyadic centre of A_F
ETA = 2.0**-8                                   # X_F half-width 0.00390625
ETA_IN = 3 * 2.0**-10                           # tiling excludes the open square of half-width 0.0029296875 about XC
RHO_F = 0.25                                    # A_F half-width
H0 = 2.0**-8                                    # top-level cell half-width
ENL = 1 + 1e-9                                  # cells are enlarged by this factor, so float rounding of the
                                                # (non-dyadic) child centres cannot leave gaps between cells
MAXDEPTH = 5
RH = float(R_hi) * (1 + 1e-12)
NEG = '--negative-control' in sys.argv
if NEG:
    # negative control: ask for a tiling of the disk |x| <= 0.158 > x*.  On the real axis beyond x* the two zeros
    # near alpha* are complex conjugates, so no real-symmetric Krawczyk box can isolate one of them: must FAIL.
    RH = 0.158
    MAXDEPTH = 3
print(f"x_c0 = {xc0.str(25)}, R_hi = {R_hi.str(25)}; X_F centre {XC!r}, half-width {ETA}; tiling hole {ETA_IN}; A_F centre {AL0!r}, half-width {RHO_F}; h0 = {H0}")

# ------------------------------------------------------------------------------------------ (T) tiling
def wanted(cx, cy, h):
    if dist_min(cx, cy, h, 0.0, 0.0) > RH:
        return False
    if square_inside_open(cx, cy, h, XC, 0.0, ETA_IN):
        return False
    return True

N0 = int(math.ceil((RH + H0) / (2 * H0)))
queue = []
for i in range(-N0, N0 + 1):
    for j in range(-N0, N0 + 1):
        cx, cy = 2 * H0 * i, 2 * H0 * j
        if wanted(cx, cy, H0):
            queue.append((cx, cy, H0, 0, (i, j)))
# process in order of increasing |x| so that guesses come from the Taylor polynomial / processed neighbours
queue.sort(key=lambda t: math.hypot(t[0], t[1]))
cells = []
fails = []
def taylor_guess(cx, cy):
    # low-order Taylor guess (exact coefficients a_1..a_8 from hydro_series.py); refined by Newton
    a = [-2.0, -3.0, -29/3, -2843/72, -392029/2160, -14509367/16200, -63074754607/13608000,
         -567431897964619/22861440000]
    z = complex(cx, cy); s = 0j; p = 1 + 0j
    for k in range(8):
        p *= z; s += a[k] * p
    return s
guess_grid = {}
def nearest_guess(cx, cy, h):
    # use the nearest processed cell centre along the ray to the origin, else Taylor
    best = None; bd = 1e9
    key = (round(cx / (2 * H0)), round(cy / (2 * H0)))
    for di in (-1, 0, 1):
        for dj in (-1, 0, 1):
            for (px, py, val) in guess_grid.get((key[0] + di, key[1] + dj), []):
                d = math.hypot(px - cx, py - cy)
                if d < bd:
                    bd = d; best = val
    if best is not None and bd < 4 * H0:
        return best
    return taylor_guess(cx, cy)

stack = list(reversed(queue))
while stack:
    cx, cy, h, depth, top = stack.pop()
    X = box_x(cx, cy, h * ENL)
    x0 = acb(cx, cy)
    g = nearest_guess(cx, cy, h)
    real_c = (cy == 0.0)
    ok, A, K, c = krawczyk(X, x0, acb(g.real, 0 if real_c else g.imag), real_centre=real_c)
    if ok:
        cells.append(dict(cx=cx, cy=cy, h=h, A=A, K=K, c=c, top=top, real=real_c))
        key = (round(cx / (2 * H0)), round(cy / (2 * H0)))
        guess_grid.setdefault(key, []).append((cx, cy, complex(float(c.real.mid()), float(c.imag.mid()))))
    else:
        if depth >= MAXDEPTH:
            fails.append((cx, cy, h))
            continue
        hh = h / 3
        kids = []
        for di in (-1, 0, 1):
            for dj in (-1, 0, 1):
                kx, ky = cx + 2 * hh * di, cy + 2 * hh * dj
                if dj == 0 and cy == 0.0:
                    ky = 0.0
                if wanted(kx, ky, hh):
                    kids.append((kx, ky, hh, depth + 1, top))
        kids.sort(key=lambda t: -math.hypot(t[0], t[1]))
        stack.extend(kids)
depths = {}
for cl in cells:
    d = round(math.log(H0 / cl['h'], 3)); depths[d] = depths.get(d, 0) + 1
report(f"(T) Krawczyk tiling: {len(cells)} cells certified, {len(fails)} failures (cells by depth {depths})", len(fails) == 0,
       f"[{time.time()-T0:.0f}s]")
if fails:
    print("   first failures:", fails[:5])

if NEG:
    bad_real = [f for f in fails if abs(f[1]) <= f[2] and f[0] > XC]
    print(f"negative control: {len(fails)} failed cells, {len(bad_real)} of them on the real axis beyond x* "
          f"(x from {min(f[0] for f in bad_real) if bad_real else None:.5f})")
    print("NEGATIVE CONTROL " + ("BEHAVES AS EXPECTED (tiling beyond x* fails)" if bad_real else "UNEXPECTED: tiling passed beyond x*"))
    sys.exit(0)
# origin cell: zero alpha = 0 at x = 0
orig = [cl for cl in cells if abs(cl['cx']) <= cl['h'] and abs(cl['cy']) <= cl['h']]
okO = len(orig) > 0 and all(cl['A'].contains(acb(0)) for cl in orig)
report("(C0) every cell containing x = 0 has alpha = 0 in its alpha-box (G(0,0)=0; the unique zero there is alpha_h(0)=0)", okO)

# ------------------------------------------------------------------------------------------ (C) consistency
buckets = {}
for idx, cl in enumerate(cells):
    buckets.setdefault(cl['top'], []).append(idx)
npairs = 0; bad = 0
for idx, cl in enumerate(cells):
    ti, tj = cl['top']
    for di in (-1, 0, 1):
        for dj in (-1, 0, 1):
            for jdx in buckets.get((ti + di, tj + dj), []):
                if jdx <= idx:
                    continue
                o = cells[jdx]
                if abs(cl['cx'] - o['cx']) <= (cl['h'] + o['h']) * ENL and abs(cl['cy'] - o['cy']) <= (cl['h'] + o['h']) * ENL:
                    npairs += 1
                    # one inclusion suffices: if K_i is in A_j then for x in X_i n X_j the zero alpha_i(x) lies in A_j,
                    # where G(., x) has a unique zero, so alpha_i(x) = alpha_j(x)
                    if not (o['A'].contains(cl['K']) or cl['A'].contains(o['K'])):
                        bad += 1
report(f"(C) consistency on {npairs} touching pairs: K_i in A_j or K_j in A_i", bad == 0, f"bad = {bad}")
realcells = [cl for cl in cells if cl['real']]
okR = all(cl['c'].imag == 0 for cl in realcells)
report(f"(R) {len(realcells)} real-axis cells have real-centred alpha-boxes (zero real for real x)", okR)

# ------------------------------------------------------------------------------------------ (F) fold patch
AF = sqbox(acb(AL0), RHO_F)
XF = box_x(XC, 0.0, ETA)
report("(F0) the certified collision box lies inside A_F x X_F",
       AF.contains_interior(acb(arb(a0.mid(), arb("1.5e-10").upper()))) and XF.contains_interior(acb(xstar_box)))

def boundary_points(center, h, n_per_edge):
    """counterclockwise points on the boundary of the square of half-width h about center (acb)."""
    cr, ci = float(center.real.mid()), float(center.imag.mid())
    corners = [(cr + h, ci - h), (cr + h, ci + h), (cr - h, ci + h), (cr - h, ci - h)]
    pts = []
    for e in range(4):
        (x1, y1), (x2, y2) = corners[e], corners[(e + 1) % 4]
        for k in range(n_per_edge):
            t = k / n_per_edge
            pts.append((x1 + (x2 - x1) * t, y1 + (y2 - y1) * t))
    return pts

def seg_box(p, q):
    (x1, y1), (x2, y2) = p, q
    return acb(arb((x1 + x2) / 2, abs(x2 - x1) / 2 + 1e-300), arb((y1 + y2) / 2, abs(y2 - y1) / 2 + 1e-300))

def pt(p):
    return acb(p[0], p[1])

def arg_sum(values, boxes):
    """sum of principal args of consecutive ratios; returns (ok, arb total/(2 pi))."""
    tot = arb(0); ok = True
    for k in range(len(values)):
        if boxes[k].contains(acb(0)):
            ok = False
        r = values[(k + 1) % len(values)] / values[k]
        if not (r.real > 0):
            ok = False
        tot += arb.atan2(r.imag, r.real)
    return ok, tot / (2 * arb.pi())

# (a) G != 0 on boundary(A_F) x X_F, with X_F split into NXS x NXS sub-boxes
NE = 64; NXS = 4
bpts = boundary_points(acb(AL0), RHO_F, NE)
xsubs = []
for i in range(NXS):
    for j in range(NXS):
        hx = ETA / NXS
        xsubs.append(box_x(XC - ETA + hx * (2 * i + 1), -ETA + hx * (2 * j + 1), hx * ENL))
okA = True; minabs = None
for k in range(len(bpts)):
    sb = seg_box(bpts[k], bpts[(k + 1) % len(bpts)])
    for xs in xsubs:
        Gv, _ = GGa(sb, xs, deriv=False)
        if Gv.contains(acb(0)):
            okA = False
        lo = abs(Gv).lower()
        minabs = lo if minabs is None or lo < minabs else minabs
report(f"(Fa) G != 0 on boundary(A_F) x X_F ({len(bpts)} boundary segments x {len(xsubs)} x-boxes)", okA,
       f"min |G| >= {minabs.str(4) if minabs is not None else '?'}")
# (b) winding of G(., x_c0) along boundary(A_F)
xpt = acb(XC)
vals = [GGa(pt(p), xpt, deriv=False)[0] for p in bpts]
boxes = [GGa(seg_box(bpts[k], bpts[(k + 1) % len(bpts)]), xpt, deriv=False)[0] for k in range(len(bpts))]
okb, wind = arg_sum(vals, boxes)
okb = okb and wind.contains(2) and not wind.contains(1) and not wind.contains(3)
report("(Fb) winding number of G(., XC) along boundary(A_F) = 2 (exactly two zeros in A_F for every x in X_F)", okb,
       f"winding in {wind.str(6)}")

# (c) discriminant winding along boundary(X_F)
def two_roots(X, x0):
    """Krawczyk boxes for the two zeros in A_F for x in X; returns (ok, K1, K2)."""
    dx = complex(float(x0.real.mid()) - XC, float(x0.imag.mid()))
    r = (-dx) ** 0.5          # sqrt(x_c - x); the two zeros are near alpha* +- 1.34 sqrt(x_c - x)
    g1 = complex(AL0) + 1.34 * r
    g2 = complex(AL0) - 1.34 * r
    ok1, A1, K1, c1 = krawczyk(X, x0, acb(g1.real, g1.imag), need_slack=False)
    ok2, A2, K2, c2 = krawczyk(X, x0, acb(g2.real, g2.imag), need_slack=False)
    if not (ok1 and ok2):
        return False, None, None
    if A1.overlaps(A2) or not (AF.contains_interior(A1) and AF.contains_interior(A2)):
        return False, None, None
    return True, K1, K2

NXE = int(sys.argv[4]) if len(sys.argv) > 4 else 64
xb = boundary_points(acb(XC), ETA, NXE)
okc = True; dvals = []; dboxes = []
for k in range(len(xb)):
    p = xb[k]; q = xb[(k + 1) % len(xb)]
    okp, K1p, K2p = two_roots(pt(p), pt(p))
    oks, K1s, K2s = two_roots(seg_box(p, q), acb((p[0] + q[0]) / 2, (p[1] + q[1]) / 2))
    if not (okp and oks):
        okc = False
        print("   two-root Krawczyk failed at boundary point", p)
        break
    dvals.append((K1p - K2p) ** 2)
    dboxes.append((K1s - K2s) ** 2)
if okc:
    okw, windD = arg_sum(dvals, dboxes)
    okc = okw and windD.contains(1) and not windD.contains(0) and not windD.contains(2)
    report(f"(Fc) on boundary(X_F) ({len(xb)} segments) the two zeros are separated and wind(Delta) = 1", okc,
           f"winding in {windD.str(6)}")
else:
    report("(Fc) discriminant winding", False)

# (d) tiling cells meeting X_F have K inside A_F
meet = [cl for cl in cells if abs(cl['cx'] - XC) <= cl['h'] * ENL + ETA and abs(cl['cy']) <= cl['h'] * ENL + ETA]
okd = len(meet) > 0 and all(AF.contains(cl['K']) for cl in meet)
report(f"(Fd) all {len(meet)} tiling cells meeting X_F have their zero enclosure K_i inside A_F", okd)

# coverage sanity: the tiling region plus X_F covers the closed disk |x| <= R_hi (checked cell-wise by construction:
# every grid cell meeting the disk and not inside the open eta_in-square was processed or subdivided; the eta_in-square
# is inside X_F because eta_in < eta).
report("(Cov) eta_in < eta, so {|x| <= R_hi} is covered by the certified cells and X_F", ETA_IN < ETA)

allok = all(ok for _, ok in results)
print()
print(("CERTIFIED" if allok else "NOT CERTIFIED") + f": total {time.time()-T0:.0f}s")
if allok:
    print("The hydrodynamic root alpha_h(x), x = q^2/4, is analytic on |x| < x*, real on 0 <= x < x*, and has a square-root")
    print("branch point at x* = q*^2/4 (q* = 0.778472800990330076180356446189 +- 1e-20).  The series (27) in q^2 has radius")
    print("of convergence exactly q*^2 = %s." % (qbox * qbox).str(25))
json.dump({"results": results, "cells": len(cells), "eta": ETA, "rho_F": RHO_F, "h0": H0,
           "time_s": time.time() - T0}, open("certify_hydro_radius_summary.json", "w"), indent=1)

# ---------------------------------------------------------------- referee addition: exact dump of the certified cells
import pickle
def me(a):
    m, e = a.man_exp()
    return (int(m), int(e))
def dump_box(z):
    return (me(z.real.mid()), me(z.real.rad()), me(z.imag.mid()), me(z.imag.rad()))
dump = dict(H0=H0, ENL=ENL, XC=XC, ETA=ETA, ETA_IN=ETA_IN, RHO_F=RHO_F, AL0=AL0, RH=RH,
            R_hi=me(R_hi) if hasattr(R_hi, 'man_exp') else str(R_hi),
            cells=[dict(cx=cl['cx'], cy=cl['cy'], h=cl['h'], top=cl['top'], real=cl['real'],
                        X=dump_box(box_x(cl['cx'], cl['cy'], cl['h'] * ENL)),
                        A=dump_box(cl['A']), K=dump_box(cl['K']), c=dump_box(cl['c'])) for cl in cells])
pickle.dump(dump, open('cells_dump.pkl', 'wb'))
print("referee: dumped", len(cells), "cells to cells_dump.pkl")
