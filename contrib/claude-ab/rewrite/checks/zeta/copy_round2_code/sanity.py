import mpmath as mp
mp.mp.dps = 30
# (1) F(s) = s zeta(s+1)/zeta(s) = -2 pi cot(pi s/2) zeta(-s)/zeta(1-s)
for s in [mp.mpc(-1.5, 37.2), mp.mpc(0.3, 101.7), mp.mpc(2.2, -5.1), mp.mpc(-0.7, 0.4)]:
    lhs = s*mp.zeta(s+1)/mp.zeta(s)
    rhs = -2*mp.pi*mp.cot(mp.pi*s/2)*mp.zeta(-s)/mp.zeta(1-s)
    print('FE check', mp.nstr(s,6), mp.nstr(abs(lhs-rhs)/abs(lhs), 5))
# (2) cot(pi/4 + i pi u/2) = sech(pi u) - i tanh(pi u)
for u in [0.1, 0.7, 3.0, -2.0]:
    print('cot check', abs(mp.cot(mp.pi/4 + 1j*mp.pi*u/2) - (mp.sech(mp.pi*u) - 1j*mp.tanh(mp.pi*u))))
# (3) velocity: zero of zeta(s,1+t) near rho_k, finite difference vs rho zeta(rho+1)/zeta'(rho)
for k in [1, 2, 10]:
    rho = mp.zetazero(k)
    c1 = rho*mp.zeta(rho+1)/mp.zeta(rho, derivative=1)
    t = mp.mpf('1e-8')
    rp = mp.findroot(lambda s: mp.zeta(s, 1+t), rho)
    rm = mp.findroot(lambda s: mp.zeta(s, 1-t), rho)
    fd = (rp-rm)/(2*t)
    print('velocity k=%d'%k, mp.nstr(c1,12), mp.nstr(fd,12), mp.nstr(abs(c1-fd),3))
# (4) b(n) = (1/n) prod_{p|n}(1-p): Dirichlet coefficients of zeta(s+1)/zeta(s)
s = mp.mpf(3)
b = lambda n: mp.mpf(mp.fprod([1-p for p in mp.primefactors(n)]) if n>1 else 1)/n if hasattr(mp,'primefactors') else None
