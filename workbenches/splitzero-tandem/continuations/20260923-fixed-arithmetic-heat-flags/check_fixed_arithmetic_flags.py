from pathlib import Path
import json
import sympy as sp

x,t=sp.symbols('x t',real=True)
I=sp.I
checks=[]
def eq(label,a,b):
    residual=sp.cancel(sp.expand(a-b))
    ok=residual==0
    checks.append({'check':label,'passed':bool(ok)})
    if not ok: raise ArithmeticError((label,residual))

def hermite(m):
    return sum((-1)**k*sp.factorial(m)*x**(m-2*k)/(sp.factorial(k)*sp.factorial(m-2*k)) for k in range(m//2+1))
def companion(poly,m):
    p=sp.Poly(poly,x)
    C=sp.zeros(m)
    for n in range(m-1): C[n+1,n]=1
    for n in range(m): C[n,m-1]=-p.nth(n)
    return C

a=sp.Rational(2,5); gamma=sp.Rational(-1,7)
# Exact auxiliary original heat family x^m exp(a*x+gamma*x^2).
# Its actual cluster roots are 2*a*t+r*sqrt(t*(1+4*gamma*t));
# original c=a, d=gamma+a^2/2, b=2*gamma.
for m in range(1,7):
    P=hermite(m); C=companion(P,m)
    p=[sp.trace(C**n) for n in range(2*m+7)]
    moment=lambda n: sp.expand(sum(sp.binomial(n,k)*(2*a*t)**(n-k)*t**(k//2)*(1+4*gamma*t)**(k//2)*p[k] for k in range(0,n+1,2)))
    for j in range(m):
        f={n:sp.Rational(n+1,3)+I*sp.Rational(2*n+1,7) for n in range(j,j+4)}
        g={n:sp.Rational(2*n+3,5)-I*sp.Rational(n+2,11) for n in range(j,j+4)}
        products={n:sum(sp.conjugate((I/2)**k*f[k])*(I/2)**(n-k)*g[n-k] for k in f if n-k in g) for n in range(2*j,2*j+3)}
        Z=sp.expand(sum(v*moment(n) for n,v in products.items()))
        q=sp.conjugate(f[j])*g[j]
        first=0 if j==0 else (4*j*gamma*p[2*j]+4*j*(2*j-1)*a*a*p[2*j-2])*q
        correction=first+I*(2*j+1)*a*p[2*j]*(sp.conjugate(f[j])*g[j+1]-sp.conjugate(f[j+1])*g[j])+p[2*j+2]/4*(sp.conjugate(f[j+1])*g[j+1]-sp.conjugate(f[j])*g[j+2]-sp.conjugate(f[j+2])*g[j])
        eq(f'm={m}, j={j}: complete leading fixed-test response',Z.coeff(t,j),p[2*j]*q/4**j)
        eq(f'm={m}, j={j}: complete next fixed-test response',Z.coeff(t,j+1),correction/4**j)
    M=m*(m-1)//2
    Dm=2**M*sp.prod(n**n for n in range(1,m+1))
    eq(f'm={m}: exact Hermite discriminant',sp.discriminant(P,x),Dm)
    rho=sp.Rational(1,2)+I*sp.Rational(3,7)
    poles=[sp.Integer(2+l)+I*sp.Rational(l+1,5) for l in range(m)]
    delta=sp.prod(poles[v]-poles[u] for u in range(m) for v in range(u+1,m))
    R0=sp.Matrix(m,m,lambda n,l:(-I/2)**n/(rho-poles[l])**(n+1))
    eq(f'm={m}: endpoint frame determinant',R0.det(method='domain-ge'),(-I/2)**M*delta/sp.prod((rho-z)**m for z in poles))
    Q=sp.prod((x-z) for z in poles)
    v=sp.symbols('v')
    for j in range(m):
        qrho=sp.Poly(sp.expand(Q.subs(x,rho+v)),v)
        numerator=v**j*sum(qrho.nth(n)*v**n for n in range(m-j))
        eq(f'm={m}, j={j}: fixed jet numerator remainder',sp.rem(sp.expand(numerator-v**j*Q.subs(x,rho+v)),v**m,v),0)
    # Two nonzero times test the original reflected matrix, including negative time.
    if m<=4:
        for tv in [sp.Rational(2,101),sp.Rational(-2,101)]:
            W=sum((-1)**k*sp.factorial(m)*(tv*(1+4*gamma*tv))**k*(x-2*a*tv)**(m-2*k)/(sp.factorial(k)*sp.factorial(m-2*k)) for k in range(m//2+1))
            C=companion(sp.expand(W),m)
            e=sp.eye(m)[:,0]
            R=sp.Matrix.hstack(*[((rho-z)*sp.eye(m)+I*C/2).inv()*e for z in poles])
            denominator=sp.prod((-I/2)**m*W.subs(x,2*I*(rho-z)) for z in poles)
            eq(f'm={m}, t={tv}: full original frame determinant',R.det(method='domain-ge'),(-I/2)**M*delta/denominator)
            K=sp.Matrix(m,m,lambda n,l:sp.trace(C**(n+l)))
            disc=sp.discriminant(W,x)
            eq(f'm={m}, t={tv}: reflected Gram determinant',K.det(method='domain-ge'),disc)
            actual=(R.H*K*R).det(method='domain-ge')
            expected=disc*4**(-sp.Integer(M))*sp.expand(delta*sp.conjugate(delta))/sp.expand(denominator*sp.conjugate(denominator))
            eq(f'm={m}, t={tv}: exact Cauchy local determinant',actual,expected)

out={'all_passed':all(c['passed'] for c in checks),'count':len(checks),'scope':'Exact auxiliary original heat families and fixed rational-test identities. These checks supplement the full HR proofs; they do not assert any multiple zero of zeta.','checks':checks}
Path(__file__).with_name('FIXED_ARITHMETIC_FLAG_CHECKS.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({'all_passed':out['all_passed'],'count':len(checks)}))
