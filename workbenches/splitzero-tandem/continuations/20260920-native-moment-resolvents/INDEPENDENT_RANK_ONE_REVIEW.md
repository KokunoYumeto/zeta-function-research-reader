# Independent mathematical review of the root refinement

Reviewed the complete `../NATIVE_RESOLVENT_RANK_ONE.tex` on 2026-09-20 without modifying it.

No mathematical defect found in RR1–16. Checked:

- The actual contiguous polynomial Krylov dimension in RR2.
- The constrained minimum defining kappa, semidefinite rank-one subtraction, and inverse existence in RR3–5.
- Gauss residual degree, leading coefficient, negative-point evaluation and complete error square in RR6.
- Radau residual sign, cancellation against the x-weighted monic polynomial, and the exact coefficient `f(-a)/(a t_(r-1)(-a))` in RR7. The error factor is correctly `1/a`, not `1/a^2`.
- Polarization, scalar parameter, positive Sherman–Morrison denominator, mass scaling and original complex phase in RR8–11.
- Positivity of the complementary B lower bound, retained tilted mass, exact resolvent-family parameter signs, native tail, complete quotient/conductor fibres and four-endpoint signs in RR12–16.

Added independent exact finite tests to `verify_moment_enclosures.py`: both synthetic parity moment blocks, target degrees 0–2, r=n+1 and n+2, poles 4 and 16. The tests check the exact rank-one matrix gap and the exact common scalar error against direct rational integration. These finite positive atomic measures are universal test instances only, never substituted for the native arithmetic measure.

The root's rank-one refinement and the complementary variational bounds here are compatible. The present note additionally supplies fixed-pole convergence from the actual native exponential tail, an explicit pole-rate moment certificate, and an untilted-native-moment route to the s-weighted integrals. The rank-one derivation remains owned by the root and is not duplicated or edited here.
