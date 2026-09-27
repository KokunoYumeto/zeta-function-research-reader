#!/usr/bin/env python3
"""Figure: trajectories of the first five zeros of zeta(s, 1+t), 0 <= t <= 1 (the owner's shifted flow),
with the two crossings of Re s = 1/2 at non-Eulerian times (erratum to FLIP_FABLE Addendum 4).

claude-ab, model claude-opus-5-5 (Opus 5.5, maximum reasoning effort), 25 September 2026.
Tracking as in checks/hurwitz_crossing_check.py (mpmath findroot, step 0.005 in t, linear predictor);
crossing times and points are the refined values printed by that check.
Output: fig_shifted_flow_crossings.png/.svg, data/shifted_flow_tracks.csv
"""
import os, csv, sys
import mpmath as mp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
mp.mp.dps = 20
Z = lambda s, t: mp.zeta(s, 1 + t)

def track(rho0, dt=mp.mpf("0.005")):
    pts = [(mp.mpf(0), rho0)]; r = rho0; t = mp.mpf(0)
    while t < 1 - mp.mpf("1e-12"):
        tn = min(t + dt, mp.mpf(1))
        guess = r if len(pts) < 2 else r + (r - pts[-2][1]) * (tn - t) / (t - pts[-2][0])
        r = mp.findroot(lambda s: Z(s, tn), guess)
        t = tn; pts.append((t, r))
    return pts

# refined crossings from checks/hurwitz_crossing_check_OUTPUT.txt (25 digits there)
CROSS = {4: (0.95095300425, 41.8337729897), 5: (0.858704259442, 47.0438682115)}

if __name__ == "__main__":
    data = os.path.join(HERE, "data", "shifted_flow_tracks.csv")
    tracks = {}
    if "--replot" in sys.argv and os.path.exists(data):
        with open(data) as f:
            for row in csv.DictReader(f):
                tracks.setdefault(int(row["n"]), []).append((float(row["t"]), float(row["re"]), float(row["im"])))
    else:
        os.makedirs(os.path.join(HERE, "data"), exist_ok=True)
        with open(data, "w", newline="") as f:
            w = csv.writer(f); w.writerow(["n", "t", "re", "im"])
            for n in range(1, 6):
                pts = track(mp.zetazero(n))
                tracks[n] = [(float(t), float(r.real), float(r.imag)) for t, r in pts]
                for t, x, y in tracks[n]:
                    w.writerow([n, "%.4f" % t, "%.12f" % x, "%.12f" % y])
                # sign changes of Re rho - 1/2 for t > 0
                sc = [tracks[n][i][0] for i in range(1, len(tracks[n]) - 1)
                      if (tracks[n][i][1] - 0.5) * (tracks[n][i + 1][1] - 0.5) < 0]
                print("zero %d: end point at t=1: %.6f + %.6f i; sign changes of Re rho - 1/2 in (0,1]: %s"
                      % (n, tracks[n][-1][1], tracks[n][-1][2], ["%.3f" % t for t in sc]))

    plt.rcParams.update({"font.size": 10, "font.family": "DejaVu Sans"})
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(11, 6.2), gridspec_kw={"width_ratios": [1.1, 1], "wspace": 0.22})
    cmap = plt.get_cmap("viridis")
    for n, pts in tracks.items():
        arr = np.array(pts)
        seg = np.stack([arr[:-1, 1:3], arr[1:, 1:3]], axis=1)
        lc = LineCollection(seg, cmap=cmap, norm=plt.Normalize(0, 1), lw=2.2)
        lc.set_array(arr[:-1, 0]); a1.add_collection(lc)
        a1.plot(arr[0, 1], arr[0, 2], "o", color="black", ms=5, zorder=4)
        a1.plot(arr[-1, 1], arr[-1, 2], "s", color=cmap(1.0), mec="black", ms=5, zorder=4)
        a1.annotate("ρ%d" % n, (arr[0, 1], arr[0, 2]), xytext=(5, -12), textcoords="offset points", fontsize=9)
        a2.plot(arr[:, 0], arr[:, 1] - 0.5, lw=1.8, label="zero %d" % n)
    for n, (tc, gc) in CROSS.items():
        a1.plot(0.5, gc, "*", color="#c53030", ms=13, mec="black", mew=0.5, zorder=5)
        a1.annotate("zero %d crosses at t = %.5f" % (n, tc), (0.5, gc), xytext=(8, 6 if n == 5 else -14),
                    textcoords="offset points", fontsize=8.5, color="#c53030")
        a2.plot(tc, 0, "*", color="#c53030", ms=12, mec="black", mew=0.5, zorder=5)
    a1.axvline(0.5, color="0.35", lw=0.9, ls="--"); a1.axvline(1.0, color="0.6", lw=0.7, ls=":")
    a1.set_xlim(-0.2, 1.5); a1.set_ylim(10, 52)
    a1.set_xlabel("Re s"); a1.set_ylabel("Im s")
    a1.set_title("Zeros ρ_n(t) of ζ(s, 1+t), 0 ≤ t ≤ 1\n(● t = 0, on the line;  ■ t = 1;  colour = t)", fontsize=10)
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(0, 1)); sm.set_array([])
    cb = fig.colorbar(sm, ax=a1, orientation="horizontal", fraction=0.05, pad=0.12, aspect=40); cb.set_label("t")
    a2.axhline(0, color="0.35", lw=0.9, ls="--")
    a2.set_xlim(0, 1); a2.set_xlabel("t"); a2.set_ylabel("Re ρ_n(t) − ½")
    a2.set_title("Signed distance from the critical line\n(★ crossings at non-Eulerian times t ≈ 0.8587, 0.9510)", fontsize=10)
    a2.legend(fontsize=8.5, loc="upper left")
    fig.suptitle("The shifted flow leaves the line at t > 0 and some zeros cross back: the claim that zeros sit on "
                 "Re s = ½ only at Eulerian times is false", fontsize=10.5)
    fig.text(0.01, 0.005, "claude-ab (Opus 5.5, max effort) · tracking as in checks/hurwitz_crossing_check.py · "
             "figures/fig_shifted_flow_crossings.py", fontsize=7, color="0.4")
    for ext in ("png", "svg"):
        fig.savefig(os.path.join(HERE, "fig_shifted_flow_crossings." + ext), dpi=160, bbox_inches="tight")
    print("saved")
