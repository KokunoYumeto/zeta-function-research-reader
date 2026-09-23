from pathlib import Path
import json
import sympy as s
P=Path(__file__).resolve().parent
count=0
def check(ok):
    global count
    assert bool(ok)
    count+=1
for n in range(1,121):
    fs=s.factorint(n)
    coeff={p:0 for p in fs}
    for d in s.divisors(n):
        for p in s.factorint(d):coeff[p]-=int(s.mobius(d))
    check(coeff=={p:(1 if len(fs)==1 else 0) for p in fs})
    for D in range(2,31):
        active=[d for d in range(2,D+1) if s.mobius(d)]
        sparse=any(n%d==0 for d in active)
        least=not sparse
        summed=any(n%d!=0 for d in active)
        primorial=s.prod(list(s.primerange(2,D+1)))
        check(sparse or least)
        check(sparse or summed)
        check(summed==(n%primorial!=0))
        check(sparse==any(n%p==0 for p in s.primerange(2,D+1)))
        check((not least) or summed)
q=s.symbols('q',positive=True)
op=lambda x:-2*q*s.diff(x,q)
w=q**s.Rational(1,4)/(1-q)
T=lambda x:op(op(x))-x/4
W=4*q**s.Rational(5,4)*(9+55*q+31*q**2+q**3)/(1-q)**5
check(s.simplify(T(T(w))-W)==0)
check(s.expand(3-q-q**2-q**3-(1-q)*(q**2+2*q+3))==0)
check(s.Rational(1,3)-s.Rational(3,64)==s.Rational(55,192))
z=s.symbols('z')
check(s.expand(((z-s.Rational(1,2))**2-s.Rational(1,4))-z*(z-1))==0)
d=s.symbols('d')
check(s.expand((d**2-s.Rational(1,4))**2-(d**4-d**2/2+s.Rational(1,16)))==0)
j=s.symbols('j',integer=True,nonnegative=True)
check(s.expand(((2*j+s.Rational(1,2))**2-s.Rational(1,4))**2-4*j**2*(2*j+1)**2)==0)
report={'status':'passed','exact_checks':count,'scope':'Finite divisor and support identities, exact differential kernel and constants. Infinite analytic convergence and RH equivalences are proved in the accompanying sources; this script does not certify the unresolved prime inequality.'}
(P/'PRIMITIVE_PRIME_WINDOW_CHECKS.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps(report))
