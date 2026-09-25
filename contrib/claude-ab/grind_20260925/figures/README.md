# Figures (claude-ab lane)

Claude (claude-ab lane), model `claude-opus-5-5` (Opus 5.5) at maximum reasoning effort, 25 September 2026.

Each figure is produced by the script beside it. The script's printed output is saved as `*_OUTPUT.txt`, and its data as `data/*.csv`. Every script runs on the same checked computations as the notes. With `--replot`, the two zero-tracking scripts redraw from the saved data.

| Figure | Script | Shows | Used in |
|---|---|---|---|
| `fig_z15_zeros.png` / `.svg` | `fig_z15_zeros.py` | ζ's 52 zeros below height 150, all on Re s = ½, beside the 90 zeros of the even sheet Z_{1/5}(s) = ζ(s,1/5) + ζ(s,4/5). The latter number 66 left and 24 right of the line, and none lies within 0.0068 of it. The zeros were located by the Arb argument principle and refined to 30 digits | `08_` §1 (Figure 8.1); digest Figure 1 |
| `fig_monoid_sheets.png` / `.svg` | `fig_monoid_sheets.py` | The class-group orders of {n ≡ 1 mod q} and {n ≡ ±1 mod q}, q ≤ 30, with the first element that has two factorizations. The framed columns q = 3, 4, 6 illustrate Corollary 11.4 | `11_` (Figure 11.1); digest Figure 2 |
| `fig_shifted_flow_crossings.png` / `.svg` | `fig_shifted_flow_crossings.py` | The trajectories of the first five zeros of ζ(s, 1+t), 0 ≤ t ≤ 1, and the crossings of Re s = ½ at t ≈ 0.8587 (zero 5) and t ≈ 0.9510 (zero 4) | the erratum to FLIP_FABLE Addendum 4; digest Figure 3 |
| `fig_clock_stack_psi.png` / `.svg` | `fig_clock_stack_psi.py` | Left: log lcm(1..N) = ψ(N) rising by log p at each prime power. Right: (ψ(N) − N)/√N up to 10⁶, with Schoenfeld's conditional band for N ≥ 73.2 | `15_` (Figure 15.1) |
| `fig_mirror_line_double_helix.png` / `.svg` | `fig_mirror_line_double_helix.py` | Left: the critical line with the first six zeros; the line Re s = −½ carrying A(ρ) = ρ − 1, the nodal set of the first Hurwitz jet; the nodal lines of the 2nd and 3rd jets; one labelled hypothetical off-line pair with crossing rungs. Right: the Clifford torus with the (1,−1) circle Γ (critical half and mirror half) and the (1,1) circle D of `6.tex`, meeting at t = ±∞ | `17_` (Figure 17.1) |

The counts come from floating-point argument-principle computations with a step rule, not from interval-arithmetic certificates. The captions in the notes say so.
