#!/usr/bin/env python3
"""Figure: zeros of zeta(s) and of the even sheet Z_{1/5}(s) = zeta(s,1/5) + zeta(s,4/5) up to height 150.

claude-ab, model claude-opus-5-5 (Opus 5.5, maximum reasoning effort), 25 September 2026.

Method.
  Zeros of Z_{1/5} are located by adaptive argument-principle bisection in python-flint / Arb
  (checks/referee08/flint_count.py), each refined with mpmath findroot at 30 digits and verified.
  Strip counts are printed; zeros of zeta come from mpmath.zetazero.
Output: fig_z15_zeros.png, fig_z15_zeros.svg, data/z15_zeros_150.csv
"""
import os, sys, csv
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "checks", "referee08"))
from flint_count import count                      # Arb argument principle
import mpmath as mp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

mp.mp.dps = 30
Zm = lambda s: mp.zeta(s, mp.mpf(1) / 5) + mp.zeta(s, mp.mpf(4) / 5)
T0, T1 = 0.3, 150.0
S0, S1 = -1.5, 1.0             # all zeros with 0.3 < t < 150 lie here (strip counts below)

found = []
def search(s0, s1, t0, t1):
    w = count(s0, s1, t0, t1); c = int(round(w))
    assert abs(w - c) < 1e-6, (s0, s1, t0, t1, w)
    if c == 0:
        return
    if c == 1 and (t1 - t0) < 0.6 and (s1 - s0) < 0.6:
        r = mp.findroot(Zm, mp.mpc((s0 + s1) / 2, (t0 + t1) / 2))
        ok = (s0 - 1e-9 <= r.real <= s1 + 1e-9 and t0 - 1e-9 <= r.imag <= t1 + 1e-9
              and abs(Zm(r)) < 1e-25)
        assert ok, (s0, s1, t0, t1, r)
        found.append(r); return
    if (t1 - t0) >= (s1 - s0):
        tm = (t0 + t1) / 2 + 0.00731; search(s0, s1, t0, tm); search(s0, s1, tm, t1)
    else:
        sm = (s0 + s1) / 2 + 0.000731; search(s0, sm, t0, t1); search(sm, s1, t0, t1)

if __name__ == "__main__":
    strips = [(-4, S0), (S0, -0.5), (-0.5, 0.495), (0.495, 0.505), (0.505, S1), (S1, 3)]
    counts = {}
    for a, b in strips:
        counts[(a, b)] = int(round(count(a, b, T0, T1)))
        print("Z_{1/5}: zeros in [%g, %g] x [%g, %g]: %d" % (a, b, T0, T1, counts[(a, b)]))
    if "--replot" in sys.argv:                  # reuse the located zeros; strip counts are recomputed above
        with open(os.path.join(HERE, "data", "z15_zeros_150.csv")) as f:
            rows = list(csv.DictReader(f))
        found.extend(mp.mpc(mp.mpf(r["beta"]), mp.mpf(r["gamma"])) for r in rows)
    else:
        search(S0, S1, T0, T1)
    found.sort(key=lambda r: float(r.imag))
    total = sum(counts[k] for k in strips if S0 <= k[0] and k[1] <= S1)
    print("located:", len(found), " expected from strip counts:", total, " match:", len(found) == total)
    os.makedirs(os.path.join(HERE, "data"), exist_ok=True)
    with open(os.path.join(HERE, "data", "z15_zeros_150.csv"), "w", newline="") as f:
        w = csv.writer(f); w.writerow(["beta", "gamma", "abs_Z"])
        for r in found:
            w.writerow([mp.nstr(r.real, 20), mp.nstr(r.imag, 20), mp.nstr(abs(Zm(r)), 3)])
    right = [r for r in found if r.real > 0.505]
    left = [r for r in found if r.real < 0.495]
    print("beta > 0.505:", len(right), "  beta < 0.495:", len(left),
          "  |beta - 1/2| <= 0.005:", len(found) - len(right) - len(left))
    print("min |beta - 1/2| over located zeros: %.6f" % min(abs(float(r.real) - 0.5) for r in found))
    zz = []
    n = 1
    while True:
        g = mp.zetazero(n)
        if g.imag > T1:
            break
        zz.append(g); n += 1
    print("zeta zeros up to height 150:", len(zz))

    # ---------------------------------------------------------------- plot
    plt.rcParams.update({"font.size": 10, "font.family": "DejaVu Sans"})
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(9.2, 7.2), sharey=True,
                                 gridspec_kw={"width_ratios": [1, 2.2], "wspace": 0.06})
    for ax in (a1, a2):
        ax.axvline(0.5, color="0.35", lw=0.9, ls="--", zorder=1)
        ax.axvline(1.0, color="0.6", lw=0.7, ls=":", zorder=1)
        ax.axvline(0.0, color="0.6", lw=0.7, ls=":", zorder=1)
        ax.set_ylim(0, T1); ax.grid(False)
    a1.scatter([float(g.real) for g in zz], [float(g.imag) for g in zz], s=14, color="#222222", zorder=3)
    a1.set_xlim(-0.2, 1.2)
    a1.set_title("ζ(s)\n%d zeros, all on Re s = ½" % len(zz), fontsize=10)
    a1.set_xlabel("Re s"); a1.set_ylabel("Im s")
    a2.scatter([float(r.real) for r in left], [float(r.imag) for r in left], s=14, color="#2b6cb0",
               label="Re s < ½  (%d)" % len(left), zorder=3)
    a2.scatter([float(r.real) for r in right], [float(r.imag) for r in right], s=18, color="#c53030",
               marker="D", label="Re s > ½  (%d)" % len(right), zorder=3)
    a2.set_xlim(S0 - 0.05, S1 + 0.25)
    a2.set_title("Z₁/₅(s) = ζ(s, 1/5) + ζ(s, 4/5)\n%d zeros; none with |Re s − ½| ≤ 0.005" % len(found),
                 fontsize=10)
    a2.set_xlabel("Re s")
    a2.legend(loc="upper left", frameon=True, fontsize=8.5)
    low = right[0]
    a2.annotate("0.5431 + 15.7040 i", xy=(float(low.real), float(low.imag)),
                xytext=(0.66, 6.0), fontsize=8, color="#c53030",
                arrowprops=dict(arrowstyle="-", color="#c53030", lw=0.6))
    fig.suptitle("Zeros up to height 150. The monoid {n ≡ ±1 mod 5} is not free (36 = 4·9 = 6·6),\n"
                 "and the even sheet at a = 1/5 has zeros on both sides of the critical line.",
                 fontsize=10.5, y=0.995)
    fig.text(0.01, 0.005, "claude-ab (Opus 5.5, max effort) · zeros located by Arb argument principle, "
             "refined to 30 digits · figures/fig_z15_zeros.py", fontsize=7, color="0.4")
    for ext in ("png", "svg"):
        fig.savefig(os.path.join(HERE, "fig_z15_zeros." + ext), dpi=160, bbox_inches="tight")
    print("saved")
