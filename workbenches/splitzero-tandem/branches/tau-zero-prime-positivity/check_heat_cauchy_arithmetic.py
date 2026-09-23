"""Exact checks supplementing HA1--HA23; numerical checks are labelled separately."""
from pathlib import Path
import hashlib,json
import sympy as S
import mpmath as mp

P=Path(__file__).resolve().parent
s,x,w,u,t=S.symbols('s x w u t')
checks=[]
def check(name,expr):
    val=S.cancel(S.expand(expr))
    if val!=0: raise AssertionError((name,val))
    checks.append(name)
q=w+x-1
A=-1/((s-(1-x))*(s-w))
check('Cauchy inverse Mellin with both tails',1/q*(1/(s+x-1)+1/(w-s))-A)
check('endpoint zero',A.subs(s,0)-1/(w*(x-1)))
check('endpoint one',A.subs(s,1)-1/(x*(w-1)))
e=lambda y:1/y+1/(y-1)
check('entire endpoint kernel',A.subs(s,0)+A.subs(s,1)-(e(w)+e(x))/q)
check('derivative jump',(-(x-S.Rational(1,2))-(w-S.Rational(1,2)))/q+1)
rho=S.symbols('rho')
check('Hadamard divided difference',(1/(w-rho)-1/(1-x-rho))/q-A.subs(s,rho))
F=S.Function('F')(s)
L=S.diff(F,s)/F
check('Burgers identity',S.diff(S.diff(F,s,2)/F,s)-(S.diff(L,s,2)+2*L*S.diff(L,s)))
a=S.Function('a')(s);r=S.Function('r')(s)
check('completed arithmetic quotient',S.diff(a+r,s)+(a+r)**2-(S.diff(a,s)+a*a+S.diff(r,s)+2*a*r+r*r))
cn,ln,dn=S.symbols('cn ln dn')
term=(cn*ln+dn-2*a*cn)*S.exp(-s*ln)
check('exact Dirichlet coefficient derivative',S.diff(term,s)/S.exp(-s*ln)-(-cn*ln**2-dn*ln-2*S.diff(a,s)*cn+2*a*cn*ln))
for m in range(1,7):
    c=S.symbols('c')
    gp=(s-rho)**m*(1+c*(s-rho)+(s-rho)**2)
    jp=S.diff(S.diff(gp,s,2)/gp,s)/4
    for k in range(5):
        Ak=(s-rho)**k
        actual=S.residue(Ak*jp,s,rho)
        expect=-S.Rational(m*(m-1),4)*S.diff(Ak,s,2).subs(s,rho)-S.Rational(m,2)*c*S.diff(Ak,s).subs(s,rho)
        check(f'cluster m={m} test power={k}',actual-expect)
for m in range(2,9):
    check(f'critical jet m={m}',-S.Rational(m*(m-1),4)*(-2)-S.Rational(m*(m-1),2))
ell2,ell3,ell5=S.symbols('ell2 ell3 ell5')
def lam(n):
    f=S.factorint(n)
    if len(f)!=1:return S.Integer(0)
    return {2:ell2,3:ell3,5:ell5}.get(next(iter(f)),S.log(next(iter(f))))
for p,lp in [(2,ell2),(3,ell3),(5,ell5)]:
    for k in range(1,7):
        n=p**k; cv=sum(lam(d)*lam(n//d) for d in S.divisors(n))
        check(f'prime power {p}^{k}',lam(n)*k*lp+cv-(2*k-1)*lp**2)
for i in range(1,5):
    for j in range(1,5):
        n=2**i*3**j;cv=sum(lam(d)*lam(n//d) for d in S.divisors(n))
        check(f'mixed convolution 2^{i}3^{j}',cv-2*ell2*ell3)
        check(f'mixed heat coefficient 2^{i}3^{j}',-cv*(i*ell2+j*ell3)/4+ell2*ell3*(i*ell2+j*ell3)/2)
for n in [30,60,90,120,180,900]:
    check(f'three-prime first-order exclusion {n}',sum(lam(d)*lam(n//d) for d in S.divisors(n)))

# Actual zeta evaluations test independent formulas, not positivity or an RH claim.
mp.mp.dps=55
def gg(v):return v*(v-1)*mp.power(mp.pi,-v/2)*mp.gamma(v/2)*mp.zeta(v)
def ll(v):return mp.diff(gg,v)/gg(v)
def aa(v):return 1/v+1/(v-1)-mp.log(mp.pi)/2+mp.digamma(v/2)/2
def rr(v):return mp.diff(mp.zeta,v)/mp.zeta(v)
numeric=[]
for zz,ww in [(mp.mpc(2,0),mp.mpc(3,0)),(mp.mpc(2,1),mp.mpc(3,2)),(mp.mpc(4,14),mp.mpc(3,-5))]:
    qq=ww+mp.conj(zz)-1
    endpoint=1/(ww*(mp.conj(zz)-1))+1/(mp.conj(zz)*(ww-1))
    bb=lambda v:-mp.log(mp.pi)/2+mp.digamma(v/2)/2
    ar=(bb(ww)+mp.conj(bb(zz)))/qq
    primes=-(rr(ww)+mp.conj(rr(zz)))/qq
    kernel=(ll(ww)+mp.conj(ll(zz)))/qq
    err=abs(kernel-(endpoint+ar-primes))
    if err>mp.mpf('1e-48'):raise AssertionError(err)
    j1=mp.diff(lambda v:mp.diff(gg,v,2)/gg(v),ww)/4
    j2=(mp.diff(aa,ww,2)+2*aa(ww)*mp.diff(aa,ww)+mp.diff(rr,ww,2)+2*mp.diff(aa,ww)*rr(ww)+2*aa(ww)*mp.diff(rr,ww)+2*rr(ww)*mp.diff(rr,ww))/4
    derr=abs(j1-j2)
    if derr>mp.mpf('1e-48'):raise AssertionError(derr)
    numeric.append({'z':str(zz),'w':str(ww),'kernel_decomposition_error':str(err),'heat_derivative_error':str(derr)})
src=P/'HEAT_CAUCHY_ARITHMETIC_DERIVATION.md'
out={'status':'passed','exact_identity_count':len(checks),'identities':checks,'actual_zeta_numeric_checks':numeric,'numeric_scope':'Consistency evaluations only; not interval certificates or positivity proofs.','source_sha256':hashlib.sha256(src.read_bytes()).hexdigest()}
(P/'HEAT_CAUCHY_ARITHMETIC_CHECKS.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({'status':'passed','exact_identity_count':len(checks),'actual_zeta_pairs':len(numeric)}))
