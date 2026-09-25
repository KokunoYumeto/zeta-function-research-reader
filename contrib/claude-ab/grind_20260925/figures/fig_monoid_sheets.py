#!/usr/bin/env python3
"""Figure for note 11_: factorial and half-factorial sheets a = 1/q, one-sided versus even, q = 1..30.

claude-ab, model claude-opus-5-5 (Opus 5.5, maximum reasoning effort), 25 September 2026.
Cell colour: class-group order 1 (factorial), 2 (half-factorial, not factorial), >= 3 (neither),
by Proposition 11.1 and Lemma 11.3 (class group (Z/q)^x for {n = 1 mod q}, (Z/q)^x/{+-1} for {n = +-1 mod q}).
Small number: n0 = smallest element with two factorizations (exact search up to N = 60000),
computed here independently of checks/first_negative_coefficient.py.
Output: fig_monoid_sheets.png/.svg
"""
import os
from math import gcd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

HERE = os.path.dirname(os.path.abspath(__file__))
N = 60000
QMAX = 30

def phi(q):
    return sum(1 for a in range(1, q + 1) if gcd(a, q) == 1)

def n0(q, H):
    inM = lambda n: n == 1 or (gcd(n, q) == 1 and (n % q) in H) if q > 1 else True
    M = [n for n in range(2, N + 1) if inM(n)]
    hit = bytearray(N + 1)
    for i, a in enumerate(M):
        if a * a > N:
            break
        for b in M[i:]:
            if a * b > N:
                break
            hit[a * b] = 1
    atoms = [m for m in M if not hit[m]]
    cnt = [0] * (N + 1); cnt[1] = 1
    for u in atoms:
        for d in range(u, N + 1, u):
            if cnt[d // u]:
                cnt[d] += cnt[d // u]
    return next((n for n in M if cnt[n] >= 2), None)

rows = []
for q in range(1, QMAX + 1):
    f = phi(q)
    one = f                                   # |(Z/q)^x|
    even = f if q <= 2 else f // 2            # |(Z/q)^x / {+-1}|
    H1 = {1 % q} if q > 1 else {0}
    Hpm = {1, q - 1} if q > 2 else H1
    rows.append((q, one, even, n0(q, H1) if one > 1 else None, n0(q, Hpm) if even > 1 else None))
    print("q=%2d  |G|=%2d  |G/+-1|=%2d  n0(one-sided)=%s  n0(even)=%s" % rows[-1])

COL = {1: "#276749", 2: "#9ae6b4", 3: "#e2e8f0"}
def cat(order):
    return 1 if order == 1 else (2 if order == 2 else 3)

plt.rcParams.update({"font.size": 9, "font.family": "DejaVu Sans"})
fig, ax = plt.subplots(figsize=(13.5, 3.6))
for i, (q, one, even, n1, n2) in enumerate(rows):
    for r, (order, nn) in enumerate(((one, n1), (even, n2))):
        y = 1 - r
        c = cat(order)
        ax.add_patch(Rectangle((i, y), 1, 1, facecolor=COL[c], edgecolor="white", lw=1.5))
        ax.text(i + 0.5, y + 0.62, str(order), ha="center", va="center", fontsize=10,
                color="white" if c == 1 else "black", fontweight="bold")
        if nn is not None:
            lab = str(nn) if nn < 10000 else "%.1fk" % (nn / 1000)
        else:
            lab = "free" if order == 1 else ">60k"
        ax.text(i + 0.5, y + 0.25, lab, ha="center", va="center", fontsize=6.3,
                color="white" if c == 1 else "0.25")
    ax.text(i + 0.5, -0.25, str(q), ha="center", va="center", fontsize=9)
for q in (3, 4, 6):
    ax.add_patch(Rectangle((q - 1, 0), 1, 2, fill=False, edgecolor="#c53030", lw=2.0))
ax.text(-0.3, 1.5, "one-sided\n{n ≡ 1 mod q}\nclass group (ℤ/q)ˣ", ha="right", va="center", fontsize=9)
ax.text(-0.3, 0.5, "even\n{n ≡ ±1 mod q}\nclass group (ℤ/q)ˣ/{±1}", ha="right", va="center", fontsize=9)
ax.text(QMAX / 2, -0.62, "q  (sheet a = 1/q)", ha="center", fontsize=9)
ax.set_xlim(-0.1, QMAX + 0.1); ax.set_ylim(-0.75, 2.05); ax.axis("off")
from matplotlib.patches import Patch
ax.legend(handles=[Patch(color=COL[1], label="class group of order 1: factorial (Eulerian)"),
                   Patch(color=COL[2], label="order 2: half-factorial, not factorial"),
                   Patch(color=COL[3], label="order ≥ 3: neither"),
                   Patch(facecolor="none", edgecolor="#c53030", lw=2,
                         label="q = 3, 4, 6: half-factorial one-sided ⟶ factorial even")],
          loc="upper center", bbox_to_anchor=(0.5, 1.13), ncol=4, frameon=False, fontsize=8.5)
fig.suptitle("Dividing the class group by the sign ±1 turns half-factorial one-sided sheets into factorial even sheets "
             "(Corollary 11.4). Big number: class-group order; small: first element with two factorizations",
             fontsize=9.5, y=1.0)
fig.text(0.01, 0.02, "claude-ab (Opus 5.5, max effort) · exact search up to 60000 · figures/fig_monoid_sheets.py",
         fontsize=7, color="0.4")
for ext in ("png", "svg"):
    fig.savefig(os.path.join(HERE, "fig_monoid_sheets." + ext), dpi=170, bbox_inches="tight")
print("saved")
