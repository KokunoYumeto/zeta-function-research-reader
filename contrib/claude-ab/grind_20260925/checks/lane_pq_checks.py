# claude-ab checks for the positive-quotient lane (S2.2, CFP transfer algebra, W_O values)
import mpmath as mp
mp.mp.dps = 30
ok = True
f0 = lambda v: (mp.pi/2)*v**2*(2*mp.pi*v**2-3)*mp.e**(-mp.pi*v**2)
# (1) int_0^inf f0(v) v^{s-1} dv = s(s-1)/8 pi^{-s/2} Gamma(s/2)   (S2.2 / CFP3.7)
for s in [mp.mpf(3), mp.mpc(2.5, 1), mp.mpc(0.5, 14)]:
    lhs = mp.quad(lambda v: f0(v)*v**(s-1), [0, 1, 3, mp.inf])
    rhs = s*(s-1)/8*mp.pi**(-s/2)*mp.gamma(s/2)
    ok &= abs(lhs-rhs) < 1e-20*max(1, abs(rhs))
    print("S2.2 at s =", s, ": |lhs-rhs| =", mp.nstr(abs(lhs-rhs), 3))
# (2) int f0 = 0 and f0 is its own Fourier transform (spot check at y=0.7)
I0 = mp.quad(f0, [-mp.inf, 0, mp.inf]); print("int f0 =", mp.nstr(I0, 3)); ok &= abs(I0) < 1e-25
y = mp.mpf('0.7'); FT = mp.quad(lambda v: f0(v)*mp.cos(2*mp.pi*v*y), [-mp.inf, 0, mp.inf])
print("f0^(0.7) - f0(0.7) =", mp.nstr(FT - f0(y), 3)); ok &= abs(FT - f0(y)) < 1e-25
# (3) transfer algebra: for B_c(F,G)=sum_line m c F(rho) conj G(rho): B(T_n F,G) = B(F, n T_{1/n} G) needs n^{rho} = n * conj(n^{-rho}) i.e. Re rho = 1/2
for rho in [mp.mpc(0.5, 14.1347), mp.mpc(0.7, 20)]:
    n = 3
    lhs = n**rho; rhs = n*mp.conj(n**(-rho))
    print("rho =", rho, ": n^rho vs n*conj(n^-rho) differ by", mp.nstr(abs(lhs-rhs), 3))
    if rho.real == 0.5: ok &= abs(lhs-rhs) < 1e-25
# (4) W(x,Jx) on x = e_rho - e_rho#: m[1*conj(-1) + (-1)*conj(1)] = -2m
m = 2; x = {'r': 1, 'r#': -1}; J = {'r': 'r#', 'r#': 'r'}
W = sum(m*x[k]*mp.conj(x[J[k]]) for k in x); print("W_O(e - e#) =", W, "(expect", -2*m, ")"); ok &= (W == -2*m)
print("ALL PASS" if ok else "FAILURE")
