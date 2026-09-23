from pathlib import Path
import sympy as s
import json
from collections import Counter

groups=Counter()
def check(name,value):
    if s.cancel(s.expand(value))!=0: raise ArithmeticError((name,value))
    groups[name]+=1
x=s.symbols('x')
for roots in [(0,0),(0,0,0),(0,0,1),(0,0,1,1),(0,0,0,2,2,3)]:
    p=s.prod(x-v for v in roots)
    pis=[s.prod(x-v for j,v in enumerate(roots) if j!=i) for i in range(len(roots))]
    gd=x+2; velocities=[2*sum(s.Rational(1,roots[i]-roots[j]) for j in range(len(roots)) if roots[i]!=roots[j])+2*gd.subs(x,roots[i]) for i in range(len(roots))]
    pt=-sum(v*pi for v,pi in zip(velocities,pis))
    defect=2*sum(s.prod(x-v for l,v in enumerate(roots) if l not in (i,j)) for i in range(len(roots)) for j in range(i+1,len(roots)) if roots[i]==roots[j])
    # U=exp(x^2/2+2x+t(x+1)) at t=0: U_t/U=x+1.
    b=x+1+s.diff(gd,x)+gd**2+2*len(roots)
    check('full_unit_defect',pt+s.diff(p,x,2)+2*gd*s.diff(p,x)+(x+1+s.diff(gd,x)+gd**2)*p-defect-p*b)
    grouped=sum(n*(n-1)/(x-c)**2 for c,n in Counter(roots).items())
    check('all_cluster_meromorphic',defect/p-grouped)
for m in range(2,11):
    u=2+3*x+5*x**2+7*x**3
    f=x**m*u; q=m*(m-1)*x**(m-2)*u
    for j in range(m+3):
        phi=x**j
        expected=-m*(m-1)*s.diff(phi,x,2).subs(x,0)
        got=s.residue(phi*s.diff(q/f,x),x,0)
        check('contact_tangent',got-expected)
        check('coordinate_gauge',s.residue(phi*s.diff(s.diff(f,x)/f,x),x,0)+m*s.diff(phi,x).subs(x,0))
    check('raw_residue',s.residue(x*q/f,x,0)-m*(m-1))
    if m>=3:
        check('cotangent_kernel',s.rem(q*s.diff(f,x),x**m,x))
        for j in range(m):
            check('trace_radical',m*(q*x**j).subs(x,0))
    else:
        check('double_trace',m*q.subs(x,0)-4*u.subs(x,0))
rho,a,b,z=s.symbols('rho a b z')
test=-1/((z-a)*(z-b))
got=s.diff(test,z,2).subs(z,rho)
expected=-2*((rho-a)**-3*(rho-b)**-1+(rho-a)**-2*(rho-b)**-2+(rho-a)**-1*(rho-b)**-3)
check('cauchy_full_matrix',got-expected)
for degree in range(8):
    atest=z**degree
    pull=atest.subs(z,rho+s.I*x/2)
    check('arithmetic_affine_factor',-s.diff(pull,x,2).subs(x,0)-s.diff(atest,z,2).subs(z,rho)/4)
for i in range(5):
    for j in range(5):
        n=i+j+1
        check('laurent_contact',s.diff(x**(-2*i-1)*x**(-2*j-1),x,2)-2*n*(2*n+1)*x**(-2*n-2))
out={'exact_checks':sum(groups.values()),'groups':dict(groups),'scope':'Finite exact verification of BT full-unit identity, residue derivative, cotangent classes, original arithmetic factors and fixed tests. The written proofs establish the general identities.'}
Path(__file__).with_name('CONTACT_TRACE_CHECKS.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
