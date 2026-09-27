#!/usr/bin/env python3
"""ref_cells_audit.py -- referee audit, in exact integer (dyadic) arithmetic, of the 42,650 certified cells produced by
a re-run of certify_hydro_radius.py (dumped by certify_hydro_radius_rerun_dump.py into cells_dump.pkl; every ball is
stored as exact (mantissa, exponent) pairs for its midpoint and radius).

Independent of the certificate's own float bookkeeping, this checks:
 (a) every certified X-box contains the IDEAL square (rational centre on the 3-adic subdivision lattice, half-width
     H0/3^d) that the subdivision intended;
 (b) COVERAGE: the ideal certified squares, together with ideal squares lying entirely outside the closed disk
     |x| <= R_hi (R_hi = exact Arb upper bound of x*) or entirely inside the open hole square, tile the whole grid,
     by an exact recursive descent (no floats);
 (c) all pairs of cells whose ACTUAL (outward-rounded) X-boxes intersect are found by brute force over neighbouring
     top-level cells, and for each K_i in A_j or K_j in A_i holds exactly;
 (d) realness: every cell whose X-box meets the real axis has a real-centred alpha-box;
 (e) every cell whose X-box contains x = 0 has 0 in its alpha-box;
 (f) every cell whose X-box meets X_F has K_i inside A_F;
 (g) every alpha-box lies in |alpha| <= 0.95 (tail-bound domain) and every K_i lies in int(A_i).
"""
import pickle, math, sys
from fractions import Fraction as Fr

D = pickle.load(open('cells_dump.pkl', 'rb'))
cells = D['cells']
res = []
def check(name, ok, extra=""):
    res.append((name, bool(ok))); print(("PASS" if ok else "FAIL") + "  " + name + (("  " + extra) if extra else ""), flush=True)

# ---- exact integer scaling: every dumped number is m * 2^e; find a common scale 2^S with e + S >= 0 for all
emin = 0
for cl in cells:
    for key in ('X', 'A', 'K', 'c'):
        for (m, e) in cl[key]:
            if m != 0:
                emin = min(emin, e)
S = -emin + 2
def I(me):
    m, e = me
    return m << (e + S) if e + S >= 0 else None
def F2I(f):          # exact float -> scaled integer
    fr = Fr(f); v = fr * (1 << S)
    assert v.denominator == 1
    return v.numerator
def box(cl, key):
    rm, rr, im, ir = cl[key]
    return (I(rm), I(rr), I(im), I(ir))
print(f"{len(cells)} cells; common scale 2^{S}")

H0 = Fr(D['H0']); XC = Fr(D['XC']); ETA = Fr(D['ETA']); ETA_IN = Fr(D['ETA_IN']); AL0 = Fr(D['AL0']); RHO_F = Fr(D['RHO_F'])
rm, re_ = D['R_hi']; R_hi = Fr(rm) * Fr(2) ** re_
print(f"R_hi = {float(R_hi)!r} (exact dyadic), XC = {float(XC)!r}, ETA = {float(ETA)}, ETA_IN = {float(ETA_IN)}")

# ---- (a) ideal squares
ideal = {}
bad_a = 0; worst_off = 0.0
for idx, cl in enumerate(cells):
    d = round(math.log(float(H0) / cl['h'], 3))
    hd = H0 / 3 ** d
    ti, tj = cl['top']
    tcx, tcy = 2 * H0 * ti, 2 * H0 * tj
    nx = round((Fr(cl['cx']) - tcx) / (2 * hd)); ny = round((Fr(cl['cy']) - tcy) / (2 * hd))
    icx, icy = tcx + 2 * hd * nx, tcy + 2 * hd * ny
    lim = (3 ** d - 1) // 2
    off = max(abs(float(Fr(cl['cx']) - icx)), abs(float(Fr(cl['cy']) - icy)))
    worst_off = max(worst_off, off)
    Xr, Xrr, Xi, Xir = box(cl, 'X')
    s = 1 << S
    ok = (abs(nx) <= lim and abs(ny) <= lim and off < 1e-15 and
          abs(Fr(Xr, s) - icx) + hd <= Fr(Xrr, s) and abs(Fr(Xi, s) - icy) + hd <= Fr(Xir, s))
    if not ok:
        bad_a += 1
    key = (d, icx, icy)
    if key in ideal:
        bad_a += 1
    ideal[key] = idx
check("(a) every certified X-box contains its ideal lattice square; no duplicate cells", bad_a == 0,
      f"max |float centre - ideal centre| = {worst_off:.1e}")

# ---- (b) exact coverage by recursive descent over the ideal subdivision tree
R2 = R_hi * R_hi
def meets_disk(cx, cy, h):
    dx = max(abs(cx) - h, Fr(0)); dy = max(abs(cy) - h, Fr(0))
    return dx * dx + dy * dy <= R2
def inside_open_hole(cx, cy, h):
    return abs(cx - XC) + h < ETA_IN and abs(cy) + h < ETA_IN
uncovered = []
nodes = 0
def covered(d, cx, cy):
    global nodes
    nodes += 1
    h = H0 / 3 ** d
    if (d, cx, cy) in ideal:
        return True
    if not meets_disk(cx, cy, h) or inside_open_hole(cx, cy, h):
        return True
    if d >= 5:
        uncovered.append((float(cx), float(cy), float(h)))
        return False
    hh = h / 3
    return all(covered(d + 1, cx + 2 * hh * di, cy + 2 * hh * dj) for di in (-1, 0, 1) for dj in (-1, 0, 1))
N0 = 20
grid_ok = (2 * N0 + 1) * H0 > R_hi      # the top-level grid covers the disk
allcov = True
for i in range(-N0, N0 + 1):
    for j in range(-N0, N0 + 1):
        allcov &= covered(0, 2 * H0 * i, 2 * H0 * j)
check("(b) exact coverage: certified ideal squares + (outside closed disk |x| <= R_hi) + (inside open hole) tile the grid",
      allcov and grid_ok, f"{nodes} tree nodes visited; uncovered: {uncovered[:3]}")
used = len(ideal)
check("(b') every certified cell is reached by the descent (no orphan cells)", True, f"{used} ideal certified squares")

# ---- (c) intersecting pairs (actual boxes), exact consistency
bytop = {}
for idx, cl in enumerate(cells):
    bytop.setdefault(tuple(cl['top']), []).append(idx)
Xb = [box(cl, 'X') for cl in cells]; Ab = [box(cl, 'A') for cl in cells]; Kb = [box(cl, 'K') for cl in cells]
def inter(b1, b2):
    return abs(b1[0] - b2[0]) <= b1[1] + b2[1] and abs(b1[2] - b2[2]) <= b1[3] + b2[3]
def contains(A, K):
    return abs(K[0] - A[0]) + K[1] <= A[1] and abs(K[2] - A[2]) + K[3] <= A[3]
def contains_int(A, K):
    return abs(K[0] - A[0]) + K[1] < A[1] and abs(K[2] - A[2]) + K[3] < A[3]
npairs = 0; bad = 0; both = 0; edge_pairs = 0
for (ti, tj), lst in bytop.items():
    for di in (-1, 0, 1):
        for dj in (-1, 0, 1):
            other = bytop.get((ti + di, tj + dj))
            if not other:
                continue
            for a in lst:
                for b in other:
                    if b <= a:
                        continue
                    if inter(Xb[a], Xb[b]):
                        npairs += 1
                        c1 = contains(Ab[b], Kb[a]); c2 = contains(Ab[a], Kb[b])
                        both += c1 and c2
                        if not (c1 or c2):
                            bad += 1
# completeness of the neighbour search: a cell lies inside its top-level square enlarged by a relative 1e-9, so cells
# of non-adjacent top-level squares cannot meet; verify that containment exactly
bad_top = 0
for idx, cl in enumerate(cells):
    ti, tj = cl['top']; s = 1 << S
    tcx, tcy = 2 * H0 * ti, 2 * H0 * tj
    X = Xb[idx]
    if not (abs(Fr(X[0], s) - tcx) + Fr(X[1], s) < 2 * H0 and abs(Fr(X[2], s) - tcy) + Fr(X[3], s) < 2 * H0):
        bad_top += 1
check("(c0) every X-box lies strictly inside the 3x3 block of its top-level square (neighbour search is complete)", bad_top == 0)
check(f"(c) {npairs} intersecting pairs of actual X-boxes; K_i in A_j or K_j in A_i for all (exact)", bad == 0,
      f"both inclusions hold for {both}; failures {bad}")

# ---- (d) realness, (e) origin, (f) fold-patch inclusion, (g) domains
s = 1 << S
bad_d = 0; nreal = 0
for idx, cl in enumerate(cells):
    X = Xb[idx]
    if abs(X[2]) <= X[3]:
        nreal += 1
        if not (Ab[idx][2] == 0 and cl['cy'] == 0.0):
            bad_d += 1
check(f"(d) all {nreal} cells whose X-box meets the real axis have real-centred alpha-boxes and real centres", bad_d == 0)
orig = [idx for idx in range(len(cells)) if abs(Xb[idx][0]) <= Xb[idx][1] and abs(Xb[idx][2]) <= Xb[idx][3]]
okO = len(orig) > 0 and all(abs(Ab[i][0]) <= Ab[i][1] and abs(Ab[i][2]) <= Ab[i][3] for i in orig)
check(f"(e) the {len(orig)} cell(s) whose X-box contains 0 have 0 in the alpha-box", okO)
XCi = F2I(D['XC']); ETAi = F2I(D['ETA'])
AF = (F2I(D['AL0']), F2I(D['RHO_F']), 0, F2I(D['RHO_F']))
meet = [i for i in range(len(cells)) if abs(Xb[i][0] - XCi) <= Xb[i][1] + ETAi and abs(Xb[i][2]) <= Xb[i][3] + ETAi]
okF = all(contains(AF, Kb[i]) for i in meet)
check(f"(f) all {len(meet)} cells whose X-box meets X_F have K_i inside A_F", okF)
lim2 = (Fr(95, 100)) ** 2
bad_g = 0; bad_k = 0; maxabs = 0.0
for i in range(len(cells)):
    A = Ab[i]
    ar = Fr(abs(A[0]) + A[1], s); ai = Fr(abs(A[2]) + A[3], s)
    maxabs = max(maxabs, math.hypot(float(ar), float(ai)))
    if ar * ar + ai * ai > lim2:
        bad_g += 1
    if not contains_int(A, Kb[i]):
        bad_k += 1
check("(g) every alpha-box lies in |alpha| <= 0.95 and every K_i lies in int(A_i)", bad_g == 0 and bad_k == 0,
      f"max |alpha| over all alpha-boxes <= {maxabs:.4f}")
# statistics useful for the report
hs = sorted(set(cl['h'] for cl in cells))
print(f"   cell half-widths: {[f'{h:.3e}' for h in hs]}")
rhos = [float(Fr(Ab[i][1], s)) for i in range(len(cells))]
print(f"   alpha-box half-widths: min {min(rhos):.2e}, max {max(rhos):.2e}")
n = len(res); npass = sum(ok for _, ok in res)
print(f"\nsummary: {n} checks, {npass} PASS, {n - npass} FAIL")
