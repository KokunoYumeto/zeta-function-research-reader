"""Exact supplemental checks; the review supplies the general proofs."""
from pathlib import Path
import hashlib
import json
import sympy as s

z, b, A = s.symbols('z b A', real=True)

def next_q(p, beta):
    return s.expand(beta*z*p+(1+z*z)*s.diff(p,z))

cases = []
for q, r, beta in [(0,2,b),(1,1,b),(1,2,b),(1,3,s.Rational(1,2)),
                   (2,2,s.Rational(3,2))]:
    ps = [s.Integer(1)]
    for j in range(2*q):
        ps.append(next_q(ps[-1], beta))
    q0 = ps[2*q] + (A if q else 0)
    qs = [q0]
    for j in range(2*r-2):
        qs.append(next_q(qs[-1], beta))
    direct = s.det(s.Matrix(r,r,lambda i,j: qs[i+j]))
    wr = s.expand(s.det(s.Matrix(r,r,lambda i,j:s.diff(qs[j],z,i))))
    assert s.expand(direct-(1+z*z)**(r*(r-1)//2)*wr) == 0
    wp = s.Poly(wr,z)
    expected_lc = s.rf(beta,2*q)**r*s.prod(s.factorial(j)*s.rf(beta+2*q,j)
                                          for j in range(r))
    assert wp.degree() == 2*q*r
    assert s.simplify(wp.LC()-expected_lc) == 0
    assert s.expand(wr-wr.subs(z,-z)) == 0
    ds = [wp.nth(2*j) for j in range(q*r+1)]
    ah = [s.Add(*[(-1)**(j+h)*s.binomial(j,h)*ds[j]
                  for j in range(h,q*r+1)]) for h in range(q*r+1)]
    v=s.symbols('v')
    assert s.expand(sum(ds[j]*(-1)**j*(1-v)**j for j in range(q*r+1))
                    -sum(ah[h]*v**h for h in range(q*r+1))) == 0
    assert s.expand(sum(ah)-wr.subs(z,0)) == 0
    cases.append({'q':q,'r':r,'b':str(beta),'degree':wp.degree(),
                  'Wronskian_and_mixture':'PASS'})

B,Y=s.symbols('B Y', positive=True)
for h in range(7):
    recurrence_product=4**h*s.prod((B/2+j)**2+Y**2/4 for j in range(h))
    original_coordinate_product=s.prod(Y**2+(B+2*j)**2 for j in range(h))
    assert s.expand(recurrence_product-original_coordinate_product) == 0

here=Path(__file__).parent
review=here/'INTRINSIC_FORMULA_REVIEW.md'
result={'status':'PASS','scope':'Supplemental exact symbolic checks, not a replacement for the general proof',
        'cases':cases,'density_scale_h_0_through_6':'PASS',
        'review_sha256':hashlib.sha256(review.read_bytes()).hexdigest()}
(here/'INTRINSIC_FORMULA_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
