from pathlib import Path
import json
import sympy as s
p=Path(__file__).parent
x,T,xi,a,b=s.symbols('x T xi a b',real=True,positive=True)
kernel=s.exp(-x*x/(4*T))/s.sqrt(4*s.pi*T)
checks={}
checks['complete_heat_equation']=s.cancel(s.diff(kernel,T)-s.diff(kernel,x,2))==0
F=s.exp(-4*s.pi**2*T*xi**2)
checks['Fourier_ODE']=s.cancel(s.diff(F,xi)+8*s.pi**2*T*xi*F)==0
y=s.symbols('y',real=True)
checks['convolution_square_identity']=s.cancel((x-y)**2/(4*T)+y*y/(4*a)-x*x/(4*(T+a))-(T+a)/(4*T*a)*(y-a*x/(T+a))**2)==0
u,A=s.symbols('u A',real=True)
N=s.symbols('N',positive=True)
g=s.exp(u-s.pi*N*N*s.exp(4*u))
checks['actual_theta_filter_constant']=s.cancel((s.diff(g,u,2)-g)-8*(2*s.pi**2*N**4*s.exp(9*u)-3*s.pi*N*N*s.exp(5*u))*s.exp(-s.pi*N*N*s.exp(4*u)))==0
L=range(3)
carrier=[(n,2) for n in range(-2,3)]+[(0,0),(0,1)]
def plus(v,w):return v[0]+w[0],max(v[1],w[1])
def times(v,w):return v[0]*w[0],min(v[1],w[1])
count=0
for v in carrier:
    checks['tau_add_'+str(count)]=plus(v,(0,0))==v
    checks['unit_mul_'+str(count)]=times(v,(1,2))==v
    for w in carrier:
        for z in carrier:
            checks['dist_'+str(count)]=times(v,plus(w,z))==plus(times(v,w),times(v,z))
            count+=1
checks['e_prime_test']=all((times(v,w)[0]!=0 or v[0]==0 or w[0]==0) for v in carrier for w in carrier)
if not all(checks.values()):raise ArithmeticError([k for k,v in checks.items() if not v])
(p/'LABELLED_HEAT_EXACT_CHECKS.json').write_text(json.dumps({'status':'passed','checks':len(checks),'scope':'Exact displayed heat and Fourier constants and finite auxiliary three-element-lattice identities. General proofs are LH1–15; finite tests are not a proof for arbitrary L.','identities':checks},indent=2)+'\n')
print(len(checks),'exact checks passed')
