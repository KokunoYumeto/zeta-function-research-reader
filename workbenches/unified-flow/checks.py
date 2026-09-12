# SPDX-License-Identifier: MIT
"""Elementary replay for the horizon workbench. Requires sympy and mpmath.
Run python checks.py. This is not a full curved-QFT or 4D scattering verification.
Explicit exceptions keep the checks active under python -O.
"""
import json
import sympy as s
import mpmath as mp
mp.mp.dps = 50
checks = []
def exact(name, expression):
    value = s.simplify(expression)
    if value != 0:
        raise ArithmeticError(f'{name}: {value}')
    checks.append({'name': name, 'kind': 'symbolic', 'passed': True})
def close(name, a, b, tolerance='1e-38'):
    if abs(a-b) > mp.mpf(tolerance)*max(1, abs(b)):
        raise ArithmeticError(name)
    checks.append({'name': name, 'kind': 'numerical', 'passed': True})
G,c,h,kB,M,R = s.symbols('G c hbar k_B M R', positive=True)
rh = 2*G*M/c**2
N = s.sqrt(1-rh/R)
S = 4*s.pi*kB*G*M**2/(h*c)
T = h*c**3/(8*s.pi*G*M*kB)
exact('first law', T*s.diff(S,M)-c**2)
exact('Smarr relation', 2*T*S-M*c**2)
exact('Tolman and modular-action redshift', N*kB*(T/N)-kB*T)
exact('accelerometer to thermal acceleration', (G*M/(R**2*N))/(c**4/(4*G*M*N))-(rh/R)**2)
e=s.symbols('epsilon',positive=True)
exact('finite entropy increment', (S.subs(M,M+e/c**2)-S)/kB-e/(kB*T)-4*s.pi*G*e**2/(h*c**5))
k=s.symbols('k',positive=True)
exact('peak-energy finite correction', (S.subs(M,M+k*kB*T/c**2)-S)/kB-k-k**2/(4*(S/kB)))
y,r=s.symbols('y r_h',positive=True)
rho=r*(y*s.sqrt(1+y*y)+s.asinh(y))
exact('proper-distance derivative', s.diff(rho,y)/(2*r*y)-s.sqrt(1+y*y)/y)
exact('Euclidean action to entropy', M*c**2/(kB*T)-2*S/kB)
x=s.symbols('x',positive=True)
entropy_kernel=s.log(1+s.exp(-x))+x/(1+s.exp(x))
exact('entropy-kernel derivative', s.diff(entropy_kernel,x)+x*s.exp(x)/(1+s.exp(x))**2)
Q0,ap,ell,V0=s.symbols('Q_0 alpha_prime ell V_0',positive=True)
Q=Q0+ap*ell; g=2*s.pi*ap/Q
exact('O3 one-loop beta function',s.diff(g,ell)+g*g/(2*s.pi))
exact('target Ricci clock',s.diff(Q,ell)/(-ap/2)+2)
exact('evaluated Perelman derivative',s.diff(2*V0/Q,ell)/(-ap/2)-4*V0/Q**2)
b=s.symbols('b',positive=True)
xx=4*s.pi*s.sqrt(b-1)/b**s.Rational(3,2)
exact('surface entropy radial turning point',s.diff(xx,b)/xx-(3-2*b)/(2*b*(b-1)))
exact('surface optical-potential map',xx**2-(4*s.pi)**2*(1-1/b)/b**2)
exact('null optical-potential derivative',s.diff((1-r/R)/R**2,R)-(3*r-2*R)/R**4)
L=-s.log(1-r/R)/2
exact('radial RG-scale derivative',s.diff(L,R)+r/(2*R*(R-r)))
exact('radial RG-scale second derivative',s.diff(L,R,2)-r*(2*R-r)/(2*R**2*(R-r)**2))
# Fermion Fock basis |n_R n_L>, |11>=a_R^dagger a_L^dagger|00>.
a=s.Matrix([[0,1],[0,0]])
aR=s.kronecker_product(a,s.eye(2)); aL=s.kronecker_product(s.diag(1,-1),a)
theta=s.symbols('theta',real=True)
bR=s.cos(theta)*aR-s.sin(theta)*aL.T
bL=s.cos(theta)*aL+s.sin(theta)*aR.T
psi=s.Matrix([s.cos(theta),0,0,s.sin(theta)])
for name,value in [('TFD annihilation R',bR*psi),('TFD annihilation L',bL*psi),('canonical anticommutator',bR*bR.T+bR.T*bR-s.eye(4)),('cross anticommutator',bR*bL+bL*bR)]:
    if value.applyfunc(s.trigsimp)!=s.zeros(*value.shape):
        raise ArithmeticError(name)
    checks.append({'name':name,'kind':'finite_operator','passed':True})
# General smooth-map Schwarzian coefficient at symmetric time separation.
d,f0,f1,f2,f3=s.symbols('d f0 f1 f2 f3',nonzero=True)
Fplus=f0+f1*d/2+f2*d**2/8+f3*d**3/48
Fminus=f0-f1*d/2+f2*d**2/8-f3*d**3/48
Fpplus=f1+f2*d/2+f3*d**2/8
Fpminus=f1-f2*d/2+f3*d**2/8
constant=s.limit(Fpplus*Fpminus/(Fplus-Fminus)**2-1/d**2,d,0)
exact('short-distance Schwarzian',constant-(f3/f1-s.Rational(3,2)*(f2/f1)**2)/6)
kstar=2+mp.lambertw(-2*mp.exp(-2),0)
close('Lambert positive peak',(2-kstar)*mp.exp(kstar),mp.mpf(2))
close('Lambert endpoint branch',2+mp.lambertw(-2*mp.exp(-2),-1),mp.mpf(0))
def entropy(y):
    q=mp.exp(-y)
    return mp.log1p(q)+y*q/(1+q)
for z in [mp.mpf(1),mp.mpf(2),mp.mpf('3.5')]:
    actual=mp.quad(lambda y:y**(z-1)*entropy(y),[0,1,mp.inf])
    expected=mp.gamma(z)*(z+1)*(1-2**(-z))*mp.zeta(z+1)
    close('Mellin kernel moment '+str(z),actual,expected)
bnear=mp.findroot(lambda b:kstar**2*b**3-16*mp.pi**2*b+16*mp.pi**2,(mp.mpf('1.001'),mp.mpf('1.1')))
close('lowest shell mode matches peak',4*mp.pi*mp.sqrt(1-1/bnear)/bnear,kstar)
print(json.dumps({'checks_count':len(checks),'checks':checks,'k_star':mp.nstr(kstar,35),'matching_radius_over_rh':mp.nstr(bnear,30),'fermion_occupation':mp.nstr(1/(1+mp.exp(kstar)),25),'mode_entropy_over_kB':mp.nstr(entropy(kstar),25),'limitations':['No 4D radial mode-density computation','No moving-detector transition integral','No Lean verification','No independent second review','No novelty assessment']},indent=2))
