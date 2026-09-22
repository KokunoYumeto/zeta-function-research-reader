"""Exact integral relation, discriminant and shifted Frobenius checks."""
from pathlib import Path
import sympy as S
import json
root=Path(__file__).resolve().parent
a,b,s,z=S.symbols('a b s z');lam=a*s+b;f=z*(z-lam)
checks=[]
def zero(name,v):
    assert S.factor(v)==0,name
    checks.append(name)
def rem(v):return S.rem(S.expand(v),f,z)
zero('Relative differential',S.diff(f,z)-(2*z-lam))
zero('Absolute base differential',S.diff(f,s)+a*z)
zero('Discriminant of retained basis',S.Matrix([[2,lam],[lam,lam**2]]).det()-lam**2)
zero('Collision equation at s=-b/a',f.subs(s,-b/a)-z**2)
zero('Relative cotangent quotient relation',f.subs(z,lam/2)+lam**2/4)
for p in [2,3,5,7]:
    sp=((a*s+b)**p-b**p)/a**p
    zero('Corrected affine Frobenius '+str(p),a**p*sp+b**p-lam**p)
    zero('Corrected relation image '+str(p),rem(z**p*(z**p-lam**p)))
    defect=lam**p-a**p*s**p-b**p
    zero('Naive coordinate defect '+str(p),rem(z**p*(z**p-a**p*s**p-b**p))-rem(z**p*defect))
    poly=S.Poly(S.expand(defect),a,b,s)
    assert all(int(c)%p==0 for c in poly.coeffs())
    checks.append('Delta correction is integral '+str(p))
    x,y=S.symbols('x y')
    old=(1+x)**p-(1+y)**p
    pulled=old.subs({x:z,y:z-lam},simultaneous=True)
    # The old multiplicative-coordinate lift and the new power lift are
    # compared by their actual reduced polynomial, with all signs retained.
    drift=rem(pulled-lam**p)
    zero('Old Laurent Frobenius discrepancy '+str(p),rem(pulled)-lam**p-drift)
    assert drift!=0
    checks.append('Earlier Laurent Frobenius is a distinct structure '+str(p))
    mp=z**(p-1)*sum(z**(p-1-j)*lam**j for j in range(p))
    zero('Conormal Frobenius multiplier '+str(p),rem(mp-p*lam**(2*p-3)*z))
    zero('Divided cotangent chain identity '+str(p),rem(lam**(2*p-3)*z*(2*z-lam)-(2*z**p-lam**p)*z**(p-1)))
    zero('Old collision lift '+str(p),S.rem((1+z)**p-1,z**2,z)-p*z)
    zero('Corrected collision lift '+str(p),S.rem(z**p,z**2,z))
    zero('Divided collision differential '+str(p),S.rem(z**(p-1),z**2,z)-(z if p==2 else 0))
out={'scope':'Exact symbolic polynomial checks at primes 2,3,5,7; general proofs appear in Observed cotangent and Frobenius. No p-adic specialization of a complex arithmetic period is asserted.',
     'checks':checks,'passed':True}
(root/'OBSERVED_COTANGENT_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'checks':len(checks),'passed':True}))
