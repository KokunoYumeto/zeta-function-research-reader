# Erratum to FLIP_FABLE Addendum 4 (the Eulerian-times claim)

This erratum was appended on 25 September to `FLIP_FABLE_FIBRE_AND_POSITIVITY.md` (claude-ab, 23 September; delivered then in `claude_orientation_20260922`). It is reproduced here so that it has a durable public copy. The claim it corrects, verbatim from Addendum 4: "In this non-Eulerian flow, zeros sit on vertical lines only at the two Eulerian times"; and: "RH says that the Euler product synchronizes all crossings at t = 0."


**What was false.** Addendum 4's "Reading" said that in the shifted flow ζ(s, 1+t), zeros sit on vertical lines only at the two Eulerian times t = 0 and t = −½, and that RH says the Euler product "synchronizes all crossings at t = 0". That is false. Individual zeros cross the critical line at non-Eulerian times.

**Numerical check.** `hurwitz_crossing_check.py` continues the first five zeros of ζ from t = 0 to t = 1 in steps of 0.005, at 25 digits. It then locates each sign change of Re ρ(t) − ½ by bisection:

- zero 4 of ζ (γ = 30.4249) lies on Re s = ½ at t = 0.95095300425, at s = ½ + 41.8337729897i;
- zero 5 of ζ (γ = 32.9351) lies on Re s = ½ at t = 0.858704259442, at s = ½ + 47.0438682115i.

In both cases |ζ(s, 1+t)| < 2·10⁻²⁵ at the crossing.

**Why these are genuine crossings.** Each trajectory is continued as a simple zero. The sign of Re ρ(t) − ½ changes between consecutive steps: zero 4 starts leftward (Re c₁ < 0) and ends at 0.594 + 42.40i at t = 1; zero 5 starts rightward and ends at 0.245 + 48.77i. By continuity, each crosses the line at a non-Eulerian time. This is a numerical location of each crossing, not an interval-arithmetic certificate. An earlier lane's certified crossings were the first to refute the claim.

**What remains correct.**
- Items 1–3 of Addendum 4 remain correct.
- At t = 0 every zero is transversal: Re c₁ ≠ 0 for the first 60 zeros.
- The endpoint data at t = 1 and t = −½ also stand.
- The accurate statement is that the zero set lies on the line at t = 0 under RH, and that zeros also cross the line individually at other times.
- The owner's later programme treats these crossings exactly. See the copy's Theorems A–F and Proposition G (crossing flux) in `claude_grind_20260925/02_`–`03_`.
