# Sharpness of Prop 4.6: image of P mod 9 on Z^4 and on D4 (|a_i|<=6); 18 in P(D4).
import itertools
P=lambda a: a[0]*(a[0]**2-3*(a[1]**2+a[2]**2+a[3]**2))
R=range(-6,7)
imgZ={P(a)%9 for a in itertools.product(R,repeat=4)}
imgD={P(a)%9 for a in itertools.product(R,repeat=4) if sum(a)%2==0}
valsD={P(a) for a in itertools.product(R,repeat=4) if sum(a)%2==0}
print('P mod 9 on Z^4:',sorted(imgZ),' on D4:',sorted(imgD))
print('18 attained on D4:',18 in valsD,'; P(3,1,0,0) =',P((3,1,0,0)),'; least nonzero |value| divisible by 3 on D4:',min(abs(v) for v in valsD if v%3==0 and v))
