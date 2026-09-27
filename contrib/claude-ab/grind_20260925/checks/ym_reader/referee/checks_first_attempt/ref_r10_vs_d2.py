# Referee check: does d_2 (two-norm, order 2) dominate R10 (single-norm, order 2) on R10's whole domain?
# And: the order-2 threshold if the exact audited values m(v2)=134.067..., t(v2)=19.795... (46a note) were used.
import mpmath as mp
mp.mp.dps = 40
m1, t1 = mp.mpf(64)/3, mp.mpf(16)/3
def build(m2, t2):
    ell = lambda x: (m1+4*t1)*x + (m2+4*t2)*x**2
    dl = lambda x: 6*(m1*t2+m2*t1)*x**3 + 6*m2*t2*x**4
    D = lambda x: (1-ell(x))**2 - mp.mpf(8)/3*dl(x)
    d = lambda x: mp.mpf(3)/2*(1+mp.sqrt(max(D(x),0))) + (mp.mpf(3)/2*m1-6*t1)*x + (mp.mpf(3)/2*m2-6*t2)*x**2
    return ell, dl, D, d
ell, dl, D, d2 = build(mp.mpf(5834)/39, mp.mpf(137)/6)
aR = 3/(4*(32+mp.sqrt(354)))
P2 = lambda x: 1 - mp.mpf(256)/3*x + mp.mpf(10720)/9*x**2
R10 = lambda x: mp.mpf(3)/2*(1+mp.sqrt(max(P2(x),0)))
worst = min((d2(aR*k/2000) - R10(aR*k/2000), k) for k in range(1, 2001))
print("alpha_R10 =", mp.nstr(aR, 15), " threshold", mp.nstr(1/(2*mp.sqrt(aR)), 12))
print("min over grid of d2 - R10 on (0, alpha_R10]:", mp.nstr(worst[0], 10), "at k =", worst[1])
print("d2(alpha_R10) =", mp.nstr(d2(aR), 10), " R10(alpha_R10) =", mp.nstr(R10(aR), 10))
# exact audited order-2 values (floating, from the first-pass audit note): only as an indication
for (m2, t2, lab) in ((mp.mpf('134.067'), mp.mpf('19.795'), 'audit exact (3 decimals, rounded up)'),):
    ell, dl, D, d = build(m2, t2)
    xs = [mp.mpf(k)/10**6 for k in range(1, 30001)]
    a = None
    for u, v in zip(xs, xs[1:]):
        if D(u) > 0 and D(v) <= 0:
            a = mp.findroot(D, (u, v), solver='bisect'); break
    print(lab, ": alpha_2 =", mp.nstr(a, 12), " threshold g^2 >=", mp.nstr(1/(2*mp.sqrt(a)), 10), " d_2(alpha) =", mp.nstr(d(a), 8))
