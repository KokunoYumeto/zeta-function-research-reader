from pathlib import Path
import sympy as S
import hashlib,json
P=Path(__file__).resolve().parent
s,t=S.symbols('s t',nonzero=True)
x,y=S.symbols('x y',real=True)
f=S.Function('f')(s);k=S.Function('k')(s)
mu=s*(s-1);beta=1/s+1/(s-1)
checks=[]
def zero(name,v):
    ans=S.simplify(S.expand(v))
    assert ans==0,(name,ans)
    checks.append(name)
def DA(v):return S.diff(v,s)+k*v
def B(v):return (mu+t/2)*v+t*(s-S.Rational(1,2))*S.diff(v,s)+t*t*S.diff(v,s,2)/4
zero('connected generator difference',(S.diff(DA(f)+beta*f,s)+(k+beta)*(DA(f)+beta*f)-DA(DA(f)))/4-beta*DA(f)/2-f/(2*mu))
zero('operator heat commutator',S.diff(B(f),t)-(S.diff(B(f),s,2)-B(S.diff(f,s,2)))/4)
for endpoint in [0,1]:
    E=S.exp(-(s-endpoint)**2/t)
    zero('endpoint spatial annihilation '+str(endpoint),B(E))
    mode=t**S.Rational(-1,2)*E
    zero('endpoint time compatibility '+str(endpoint),S.diff(mode,t)-S.diff(mode,s,2)/4)
for j in range(9):
    zero('endpoint time jet '+str(j),S.diff(-1/s+1/(s-1),s,2*j)/4**j-S.factorial(2*j)/4**j*((s-1)**(-2*j-1)-s**(-2*j-1)))
rho=S.Rational(1,2)+x+S.I*y
zero('real drift component',S.re(-S.Rational(1,2)*(1/rho+1/(rho-1)))+x*(x*x+y*y-S.Rational(1,4))/(rho*(rho-1)*S.conjugate(rho*(rho-1))))
h=S.symbols('h');r=S.Rational(1,2)+2*S.I
for m in range(1,6):
    bracket=(1/(r+h)+1/(r+h-1))*(m/h+2+3*h)/2+1/(2*(r+h)*(r+h-1))
    ell=S.diff(bracket,h)
    for degree in range(4):
        a=(r+h)**degree
        expected=-m*(1/r+1/(r-1))*degree*r**(degree-1)/2 if degree else 0
        zero('finite trace m='+str(m)+' degree='+str(degree),S.residue(a*ell,h,0)-expected)
R=1/(s-3)**3
ell=2*s+7+2/s+3/(s-1)+1/(s+2)
zero('full cubic test with retained quadratic exponential',-S.residue(R*ell,s,3)-(2*R.subs(s,0)+3*R.subs(s,1)+R.subs(s,-2)))
out={'exact_checks':len(checks),'checks':checks,'scope':'Exact independent algebra checks of the connected filter, endpoint modes, original-time jets, finite multiplicity trace and retained cubic-test polynomial. Analytic convergence is proved in SER/SFT, not certified by this script.',
     'proof_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [P/'SECTORIAL_ENDPOINT_ZERO_TRACE_RETURN.md',P/'SECTORIAL_FILTER_TRACE_DERIVATION.md']}}
(P/'SECTORIAL_RETURN_CHECKS.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({'exact_checks':len(checks)}))
