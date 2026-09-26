import mpmath as mp, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from fractions import Fraction as Fr
exec(open(os.path.join(HERE, 'r1_ym_orderN.py')).read().split('print("N  alpha_N')[0])
# order 2 with the first pass's recomputed exact values, rounded UP (134.068, 19.796 -> 134.07, 19.80)
MT2=[MT[0],(Fr(13407,100),Fr(1980,100))]
a=alpha(2,MT2); print("order 2 with m2<=134.07, t2<=19.80: alpha_2 =",mp.nstr(a,12)," threshold g^2 =",mp.nstr(1/(2*mp.sqrt(a)),10)," d_2(1/64) =", mp.nstr(d(2,mp.mpf(1)/64,MT2),8) if mp.mpf(1)/64<=a else 'n/a', " d_2(alpha_2) =",mp.nstr(d(2,a,MT2),8))
# d_N at a few couplings for the fully-audited orders
for g2 in (mp.mpf('4.1'),mp.mpf('4.5'),mp.mpf(5),mp.mpf(6),mp.mpf(8),mp.mpf(10)):
    xi=1/(4*g2**2)
    print(f"g^2={mp.nstr(g2,4)} xi={mp.nstr(xi,6)}: d_1={mp.nstr(d(1,xi),6) if xi<=alpha(1) else 'n/a'}  d_2={mp.nstr(d(2,xi),6) if xi<=alpha(2) else 'n/a'}  d_5={mp.nstr(d(5,xi),6) if xi<=alpha(5) else 'n/a'}")
# closed form order 1: d_1 = (3/2)(1+sqrt(1-256 xi/3)) = (3/2)(1+sqrt(1-64/(3 g^4)))
for g2 in (mp.mpf(5),mp.mpf(10)):
    xi=1/(4*g2**2); print("order-1 closed form check at g^2=",g2,":", mp.nstr(d(1,xi),12), mp.nstr(mp.mpf(3)/2*(1+mp.sqrt(1-mp.mpf(64)/(3*g2**2*g2**2))),12))
# Neumann obstruction: full space radius 3/(16 M_L); physical space: spec(H0) in {0} U [3,inf) -> circle |z|=3/2, ||R||=2/3 -> radius 3/(4 M_L)
for L in (2,3,4):
    M=12*L*L*(2*L+1)
    print(f"L={L}: M_L={M}, full-space radius 3/(16M)=1/{16*M//3}, physical-space radius 3/(4M)=1/{4*M//3}; alpha_5={mp.nstr(alpha(5),6)}")
