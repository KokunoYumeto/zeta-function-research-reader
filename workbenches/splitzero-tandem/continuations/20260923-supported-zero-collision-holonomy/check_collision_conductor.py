from pathlib import Path
import json
import sympy as sp
x,t=sp.symbols('x t')
checks=[]
def check(name,expr):
    if sp.simplify(expr)!=0:
        raise ArithmeticError(name+': '+str(expr))
    checks.append(name)
for m in range(1,13):
    p=sum((-1)**j*sp.factorial(m)/sp.factorial(j)/sp.factorial(m-2*j)*x**(m-2*j) for j in range(m//2+1))
    M=m*(m-1)//2
    D=2**M*sp.prod(sp.Integer(j)**j for j in range(1,m+1))
    check(f'Hermite discriminant m={m}',sp.discriminant(p,x)-D)
    r=m//2
    length=sum(k//2 for k in range(m))
    check(f'conductor index m={m}',length-(m-1)**2//4)
    check(f'discriminant index m={m}',M-r-2*length)
    check(f'conductor total valuation m={m}',r*(2*(r-1)+m%2)+(r if m%2 else 0)-2*length)
for m in range(1,6):
    aa=sp.symbols('a:'+str(m))
    p=x**m+sum(aa[j]*x**j for j in range(m))
    C=sp.zeros(m)
    for j in range(m-1): C[j+1,j]=1
    for j in range(m): C[j,m-1]=-aa[j]
    Cp=m*C**(m-1)+sum((j*aa[j]*C**(j-1) for j in range(1,m)),sp.zeros(m))
    L=sp.Matrix(m,m,lambda i,j:(C**(i+j))[m-1,0])
    check(f'full monic residue determinant m={m}',L.det()-(-1)**(m*(m-1)//2))
    for k in range(m):
        check(f'full monic Jacobian trace m={m},k={k}',sp.trace(C**k)-(Cp*C**k)[m-1,0])
a=sp.sqrt(6-2*sp.sqrt(6));b=sp.sqrt(6+2*sp.sqrt(6))
J=sp.Matrix([[1,0,a*a*t,0],[1,0,b*b*t,0],[0,a,0,a**3*t],[0,b,0,b**3*t]])
GB=sp.diag(2,2,2*t,2*t)
GA=sp.simplify(J.T*GB*J)
expected=sp.Matrix([[4,0,24*t,0],[0,24*t,0,240*t*t],[24*t,0,240*t*t,0],[0,240*t*t,0,2592*t**3]])
for i in range(4):
    for j in range(4): check(f'quartic full trace {i},{j}',GA[i,j]-expected[i,j])
check('quartic discriminant',GA.det()-1769472*t**6)
check('quartic embedding index',J.det()**2-110592*t**4)
result={'status':'passed','exact_checks':len(checks),'checks':checks,'scope':'Auxiliary symbolic tests of full monic residue/trace identities and exact Hermite heat families. The original arithmetic germs and all-time proofs are established in the TeX, not inferred from these finite tests.'}
out=Path(__file__).with_name('COLLISION_CONDUCTOR_VERIFICATION.json')
out.write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({'status':result['status'],'exact_checks':len(checks),'receipt':str(out)}))
