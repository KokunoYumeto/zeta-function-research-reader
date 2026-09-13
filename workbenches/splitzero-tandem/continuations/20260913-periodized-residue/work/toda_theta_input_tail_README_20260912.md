# Certified theta input for the Toda source flow

This continuation proves the analytic source maps and closes the omitted-tail and numerical-enclosure gap explicitly identified in Section 9 of the supplied Toda volume note. The complete proof is `toda_theta_input_tail_20260912.tex`, with its seven-page standalone PDF. It preserves the original two-sided theta factor, coefficients `(-6,4)`, dagger parity sign, complex-dilation phase, Mellin/Fourier constants, and the unscaled measure mass.

The explicit omitted-square bound works for every integer cutoff `J >= 0`, locally uniformly on complex rectangles inside `|Re(theta)| < pi/2`. Cauchy's formula transports it to every fixed derivative order. A separate derivative-source calculation gives a sharper direct certificate for the second moment.

The exact passage to a finite packet is also proved: `h(D) F_h = f_0`, Mellin multiplication by `h(s)`, and `w_1(t) = |h(1/2+it)|^2 w_h(t)`. Those identities retain the original source and its quotient/division data. The four numerical enclosures in this continuation concern the analytic seed `h=1`; they certify no finite-packet determinant or estimate with growing tensor degree.

## Execution

The numerical checker needs Python with `python-flint==0.9.0`. It uses Arb/Acb ball arithmetic at 256-bit precision, one arithmetic thread, and literal integer cutoff 8. No floating-point agreement is used as a certification criterion. The finite sum enclosures are enlarged by upward-rounded enclosures of the proved infinite tails.

```text
python toda_theta_input_tail_check_20260912.py --output normal.json
python -O toda_theta_input_tail_check_20260912.py --output optimized.json
python toda_theta_input_tail_check_20260912.py --negative-control --output must-not-exist.json
python -O toda_theta_input_tail_check_20260912.py --negative-control --output must-not-exist-optimized.json
```

The first two commands must succeed with identical mathematical records; the optimization flag is the only intentional difference. Both negative commands must exit with the exact error `deliberate false recurrence bound rejected` and must not write a success record. Every check is an explicit runtime condition. The replay receipt contains the four actual subprocess outcomes and source hash.

`toda_theta_input_tail_replay_20260912.py` repeats those four runs, verifies their outcomes, and renders the existing PDF for visual review. Rendering additionally needs PyMuPDF and Pillow. It is separate from the mathematical certificate.

The numerical result records include rational decimal endpoints and exact rational dyadic endpoints for the resulting balls. Every displayed decimal interval has width `3e-40`. The tail upper bounds are below `7e-107`, `3e-106`, and `4e-103` for the zero-tilt mass, one-tenth-tilt mass, and zero-tilt second moment respectively. The recurrence ratio uses interval division by the certified positive, unscaled seed mass.

The separate `toda_theta_derivative_independent_review_20260912.md` and companion exact checker provide an independent, fully rational omitted-derivative-tail estimate. Their cutoff-8 bound is coarser (`1e-92`) and valid without evaluating a transcendental function. They certify only omitted integers; the Arb certificate encloses the retained finite sum and the omitted contribution together.

The standalone PDF was compiled with XeLaTeX, with no final warnings, missing characters, or overfull boxes. Every page was inspected through two contact sheets, with full-page inspection of the dense tail theorem and the numerical intervals. The final PDF hash and page coverage are recorded in `toda_theta_input_tail_visual_review_20260912.json`.
