"""Exact downstream use of published provider balls; no zeta or Arb recomputation."""
import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import re
import sympy as s

ap=argparse.ArgumentParser()
ap.add_argument('--certificate',type=Path,required=True)
args=ap.parse_args()
raw=args.certificate.read_bytes()
sha=hashlib.sha256(raw).hexdigest()
assert sha=='9c3ae36dc2f03fa42b2d54c8f5a30802fcc0f49b4a2bd9d99bc598b6151a12f7'
data=json.loads(raw)
def endpoints(text):
 # The determinant is exactly real by the provider's proved Hermitian identity.
 # Complex Arb output appends an imaginary interval; use its displayed real ball.
 text=text.split(']',1)[0]+']'
 match=re.fullmatch(r'\[([^\[\]]+) \+/- ([^\[\]]+)\]',text)
 assert match,text
 mid,rad=map(Fraction,match.groups())
 return mid-rad,mid+rad
table={0:(Fraction(7,50),Fraction(468,10**17)),14:(Fraction(38,25),Fraction(967,10**8)),21:(Fraction(173,100),Fraction(1299,100000)),100:(Fraction(251,100),Fraction(9)),1000:(Fraction(127,25),Fraction(556))}
rows=[]
for row in data['rows']:
 tau=row['omega_imag']; upper,lower=table[tau]
 for minor in row['leading_minors'][:4]: assert minor['strictly_positive'] and minor['imaginary_contains_zero']
 c0interval=endpoints(row['coefficients'][0])
 detinterval=endpoints(next(x['determinant_ball'] for x in row['leading_minors'] if x['size']==4))
 assert c0interval[1]<upper and detinterval[0]>lower
 S=4*upper; alpha=27*lower/S**3
 if tau==0: assert alpha>Fraction(1,2*200**4*30**12)
 rows.append({'tau':tau,'c0_upper':str(upper),'detT3_lower':str(lower),'traceT3_upper':str(S),'coefficient_coercivity_lower':str(alpha)})

y,t,d,b,M=s.symbols('y tau d b M',real=True)
Q=s.Matrix([[s.expand((d+s.I*(y-t))**j*(d-s.I*(y-t))**(3-j)).coeff(y,k) for j in range(4)] for k in range(4)])
Zexpected=4*s.Matrix([
 [(d*d+t*t)**3,-3*t*(d*d+t*t)**2,-(d*d-3*t*t)*(d*d+t*t),t*(d*d-t*t)],
 [-3*t*(d*d+t*t)**2,(d*d+t*t)*(5*d*d+9*t*t),-t*(7*d*d+9*t*t),-(d*d-3*t*t)],
 [-(d*d-3*t*t)*(d*d+t*t),-t*(7*d*d+9*t*t),5*d*d+9*t*t,-3*t],
 [t*(d*d-t*t),-(d*d-3*t*t),-3*t,1]])
assert (Q*Q.conjugate().T-Zexpected).applyfunc(s.expand)==s.zeros(4)
mom=[M,0,M*b,0,M*(3*b*b+2*b),0,M*(15*b**3+30*b*b+16*b)]
K=s.Matrix([[mom[j+k] for k in range(4)] for j in range(4)])
target_trace=s.expand(s.trace(3*Q.conjugate().T*K*Q).subs(d,s.Rational(3,2)))
target_expected=12*M*(t**6+(15*b+s.Rational(27,4))*t**4+(45*b*b+s.Rational(141,2)*b+s.Rational(243,16))*t*t+15*b**3+s.Rational(201,4)*b*b+s.Rational(715,16)*b+s.Rational(729,64))
assert s.expand(target_trace-target_expected)==0
D=s.Matrix([[1,s.Rational(1,2),s.Rational(1,4),s.Rational(1,8)],[0,s.I,s.I,3*s.I/4],[0,0,-1,-s.Rational(3,2)],[0,0,0,-s.I]])
ZG=s.Matrix([[s.Rational(85,64),-27*s.I/32,-s.Rational(7,16),s.I/8],[27*s.I/32,s.Rational(41,16),-17*s.I/8,-s.Rational(3,4)],[-s.Rational(7,16),17*s.I/8,s.Rational(13,4),-3*s.I/2],[-s.I/8,-s.Rational(3,4),3*s.I/2,1]])
assert D*D.conjugate().T==ZG
gaussian_expected=M*(s.Rational(85,64)+s.Rational(339,16)*b+s.Rational(141,4)*b*b+15*b**3)
assert s.expand(s.trace(D.conjugate().T*K*D)-gaussian_expected)==0

xi=s.symbols('xi0:4');ks=s.symbols('k0:4',positive=True)
F=s.Matrix([[xi[0],xi[1],b*xi[0]+2*xi[2],(3*b+2)*xi[1]+6*xi[3]],[0,xi[0],2*xi[1],(3*b+2)*xi[0]+6*xi[2]],[0,0,2*xi[0],6*xi[1]],[0,0,0,6*xi[0]]])
KU=M*F.conjugate().T*s.diag(*ks)*F
source_trace=3*M*sum(ks[r]*(F*Zexpected.subs(d,s.Rational(3,2))*F.conjugate().T)[r,r] for r in range(4))
assert s.expand(source_trace-s.trace(3*Q.conjugate().T*KU*Q).subs(d,s.Rational(3,2)))==0
source_gaussian=M*sum(ks[r]*(F*ZG*F.conjugate().T)[r,r] for r in range(4))
assert s.expand(source_gaussian-s.trace(D.conjugate().T*KU*D))==0
out={'provider_certificate_sha256':sha,'method':'Exact rational extraction from already certified ball strings, plus independent symbolic native trace calculations. No original zeta/Arb certificate rerun.','five_pole_bounds':rows,'target_trace':str(s.factor(target_expected)),'gaussian_target_trace':str(gaussian_expected),'QQstar_all_entries_verified':True,'source_rational_trace_verified':True,'source_Gaussian_trace_verified':True,'all_assertions_passed':True}
Path(__file__).with_name('native_weil_coercivity_exact.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
