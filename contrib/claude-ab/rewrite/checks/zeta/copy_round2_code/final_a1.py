import numpy as np
from common import *
g, zp, z1, c = load_zeros(('zeros_A.npz','zeros_B.npz','zeros_C.npz'))
print(f"zeros: {len(g)}, gamma_1={g[0]:.6f}, gamma_max={g[-1]:.3f}; all on line & simple (Arb-isolated)")
print("\n[A] explicit formula: sum_rho c1 h(gamma) vs main + P_R + L_B")
for (T1, T2, D) in [(100, 1000, 1.0), (1000, 20000, 1.0), (300, 24000, 0.8), (5000, 74000, 1.5), (2000, 74000, 5.0), (10000, 70000, 0.7)]:
    lhs = np.sum(c*h_window(g, T1, T2, D)) + np.sum(np.conj(c)*h_window(-g, T1, T2, D))
    main, PR, LB = explicit_rhs(T1, T2, D); rhs = main + PR + LB
    print(f"  [{T1},{T2}] D={D}: LHS={lhs.real:.6f}{lhs.imag:+.6f}i  RHS={rhs.real:.6f}{rhs.imag:+.6f}i  rel.diff={abs(lhs-rhs)/abs(lhs):.1e}; horizontal: LHS {lhs.real:.2f} vs (T2-T1)/4pi {(T2-T1)/4/np.pi:.2f}")
S = np.concatenate([[0], np.cumsum(c)])
def E_at(T):
    k = np.searchsorted(g, T, 'right'); return S[k] - M(T)
Tmax = g[-1] - 60
print("\n[B] sharp error E(T)/T on dyadic windows (step 0.01)")
X = 1000.0
while 2*X <= Tmax:
    T = np.arange(X, 2*X, 0.01); e = E_at(T)/T
    print(f"  [{X:.0f},{2*X:.0f}]: rms Re {np.sqrt(np.mean(e.real**2)):.4f}, rms Im {np.sqrt(np.mean(e.imag**2)):.4f}, min Re {e.real.min():.3f}, max Re {e.real.max():.3f}, max|Im| {np.abs(e.imag).max():.3f}, P(sum Re c1<0)={np.mean(e.real < -1/(4*np.pi)):.4f}")
    X *= 2
print("\n[C] Bohr-Fourier coefficients of E(T)/T over [2000, Tmax] vs -b(n)/(2 pi sqrt(n) log n)")
b, e_ = sieve_coeffs(64)
T = np.arange(2000.0, Tmax, 0.004); ET = E_at(T)/T
for n in list(range(2, 17)) + [30, 60]:
    obs = np.mean(ET*np.exp(1j*T*np.log(n))); pred = -b[n]/(2*np.pi*np.sqrt(n)*np.log(n))
    print(f"  n={n:2d}: obs {obs.real:+.6f}{obs.imag:+.6f}i  pred {pred:+.6f}")
for xi in [0.5, 0.9, 1.3, 2.0]:
    obs = np.mean(ET*np.exp(1j*T*xi)); print(f"  control xi={xi}: {obs.real:+.6f}{obs.imag:+.6f}i")
print("  mean of E/T:", np.round(np.mean(ET), 6))
