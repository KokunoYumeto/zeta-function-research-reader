"""Exact rational-basis and original-Gamma congruence calculation."""
from pathlib import Path
import sympy as S
import json
B=Path(__file__).resolve().parent
x,w,b,h,d,tau,y,beta,M=S.symbols('x w b h d tau y beta M',real=True)
rows=[]
for n in range(5):
    C=S.Matrix([[S.expand((x+b)**j*(w-x)**(n-j)).coeff(x,l) for j in range(n+1)] for l in range(n+1)])
    assert S.factor(C.det())==(w+b)**(n*(n+1)//2)
    D=S.Matrix([[sum(S.binomial(l,r)*w**r*(-b)**(l-r)*S.binomial(n-l,j-r)
            for r in range(l+1)) for l in range(n+1)] for j in range(n+1)])
    assert all(S.expand(v)==0 for v in C*D-(w+b)**n*S.eye(n+1))
    rows.append({'degree':n,'unscaled_determinant':str(S.factor(C.det())),'inverse_numerator_checked':True})
g={}
mu=S.symbols('mu0:7',real=True)
for r in range(4):
    p=S.Poly(S.expand((d+S.I*x)**(3+r)*(d-S.I*x)**(3-r)),x)
    g[r]=S.expand(h*sum(p.coeff_monomial(x**j)*mu[j] for j in range(7)))
mom={0:M,1:0,2:M*beta,3:0,4:M*(3*beta**2+2*beta),5:0,
     6:M*(15*beta**3+30*beta**2+16*beta)}
shift=[sum(S.binomial(j,l)*(-tau)**(j-l)*mom[l] for l in range(j+1)) for j in range(7)]
entries={r:S.expand(g[r].subs(dict(zip(mu,shift))).subs(h,2*d)) for r in g}
H=S.Matrix(4,4,lambda i,j: entries[j-i] if j>=i else S.conjugate(entries[i-j]))
# Verify every entry against the complete unshifted monomial Gram and actual basis.
R=S.Matrix([[S.expand((x+d-S.I*tau)**j*(d+S.I*tau-x)**(3-j)).coeff(x,l)
             for j in range(4)] for l in range(4)])
Hmono=S.Matrix(4,4,lambda i,j:(-S.I)**i*S.I**j*mom[i+j])
assert all(S.expand(v)==0 for v in 2*d*R.conjugate().T*Hmono*R-H)
det_Hmono=S.factor(Hmono.det())
assert det_Hmono==12*M**4*beta**3*(beta+1)**2*(beta+2)
det_R=S.factor(R.det());assert det_R==(2*d)**6
record={'rational_basis':rows,'all_native_toeplitz_entries_checked':True,
 'g_r_in_full_shifted_moments':{str(r):str(g[r]) for r in g},
 'shifted_moments':list(map(str,shift)),
 'native_determinant':'h**16 * 12*M**4*beta**3*(beta+1)**2*(beta+2)',
 'matrix_factorization_unscaled_determinant':str(det_R),'original_monomial_gram_determinant':str(det_Hmono),
 'scope':'Exact symbolic identities, not sampled arithmetic zeros or a positivity claim for the full Weil form.'}
(B/'rational_native_receiver_exact.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
print(json.dumps(record,indent=2))
