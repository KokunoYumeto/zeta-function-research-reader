from pathlib import Path
import sympy as s,json,hashlib
p=Path(__file__).resolve().parent
z,w,lz,lw=s.symbols('z w lz lw');x=(z-s.Rational(3,2))/(z+s.Rational(1,2));y=(w-s.Rational(3,2))/(w+s.Rational(1,2));f=(lz-1)/(lz+1);g=(lw-1)/(lw+1)
assert s.cancel((1-f*g)/(1-x*y)-(lz+lw)/(z+w-1)*(z+s.Rational(1,2))*(w+s.Rational(1,2))/((lz+1)*(lw+1)))==0
X,Y,d=s.symbols('X Y d');ls=s.symbols('l0:9');numer=sum(ls[n]*(X**n+Y**n) for n in range(9));expanded=s.Poly(s.expand(numer*sum((-1)**k*(X+Y)**k/d**(k+1) for k in range(9))),X,Y)
count=1
for j in range(5):
 for k in range(5):
  expect=sum(ls[n]*(-1)**(j+k-n)*s.binomial(j+k-n,k)/d**(j+k-n+1) for n in range(j+1))+sum(ls[n]*(-1)**(j+k-n)*s.binomial(j+k-n,j)/d**(j+k-n+1) for n in range(k+1))
  assert s.cancel(expanded.coeff_monomial(X**j*Y**k)-expect)==0;count+=1
M=s.Matrix([[2*ls[0]/d,ls[1]/d-2*ls[0]/d**2],[ls[1]/d-2*ls[0]/d**2,-2*ls[1]/d**2+4*ls[0]/d**3]])
assert s.cancel(M.det()-(4*ls[0]**2-d**2*ls[1]**2)/d**4)==0;count+=1
out={'status':'passed','exact_checks':count,'scope':'Cayley congruence, 25 exact confluent coefficients, first determinant. Not a positivity proof.','source_sha256':hashlib.sha256((p/'CAUCHY_WEIL_POSITIVITY_CRITERION.md').read_bytes()).hexdigest()}
(p/'CAUCHY_WEIL_CRITERION_CHECKS.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out))
