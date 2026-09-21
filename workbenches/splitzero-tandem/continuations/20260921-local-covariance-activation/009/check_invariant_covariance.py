"""Exact tests of CGR3--9 on finite shift fixtures, with the source projection."""
import json
from pathlib import Path
import sympy as s

BASE = Path(__file__).resolve().parent
X, y, w, t = s.symbols('X y w t')
checks = []

def ok(name, truth):
    if truth is not True and truth != s.true:
        raise AssertionError(name)
    checks.append(name)

def zero(a):
    return all(s.cancel(x) == 0 for x in a)

def gamma(n, c):
    p = [s.Integer(1), y]
    for j in range(1, 2*n):
        p.append(s.expand(y*p[-1]-j*s.Rational(2*j-1, 2)*p[-2]))
    moments = [s.Integer(1)]
    for j in range(1, 2*n+1):
        pj = s.Poly(p[j], y)
        moments.append(-sum(pj.nth(a)*moments[a] for a in range(j)))
    gy = s.Matrix(n+1, n+1, lambda i,j: moments[i+j])
    coeff = s.Matrix(n+1, n+1,
                     lambda i,j: s.Poly((c+s.I*y)**j, y).nth(i))
    gram = coeff.conjugate().T*gy*coeff
    phi = s.Matrix(n+1, n+1,
         lambda i,j: s.Poly(p[j].subs(y, (X-c)/s.I), X).nth(i)
                     / s.sqrt(s.factorial(j)*s.rf(s.Rational(1,2),j)))
    ok(f'Gamma orthonormal frame n={n} c={c}',
       zero(phi.conjugate().T*gram*phi-s.eye(n+1)))
    return gram, phi, p

fixtures = [
    {'name': 'v0', 'v': 0, 'roots': list(range(4,10)),
     'shifts': [(1,4),(1,5)], 'z': {4:1}, 'Gsign':1},
    {'name': 'v1', 'v': 1, 'roots': list(range(4,11)),
     'shifts': [(-1,4),(1,6)], 'z': {4:1,5:-1}, 'Gsign':-1},
]

for f in fixtures:
    v, q, qp, cp, c = f['v'], len(f['roots']), 5, 0, 4
    g = q-qp-v
    chi = s.prod(X-r for r in f['roots'])
    chip = s.prod(X-r for r in range(qp))
    F = sum(a*s.exp(b*w) for b,a in f['z'].items())
    E = sum(a*s.exp(b*w) for a,b in f['shifts'])
    G = f['Gsign']/(1+s.exp(w))
    ok(f"{f['name']} exact numerator quotient", s.simplify(F-E*G)==0)
    d = s.cancel(sum(a*chi.subs(X,X+b) for a,b in f['shifts'])/chip)
    ok(f"{f['name']} complete d polynomial degree", s.degree(d,X)==g)

    for L in [-1,0,1,2]:
        N=q+L; D=N-v; M=L+g
        tag=f"{f['name']} L={L}"
        upper_gram, upper_phi, _ = gamma(N,c)
        lower_gram, lower_phi, _ = gamma(D,cp)
        Frow=s.Matrix([[sum(a*b**n for b,a in f['z'].items())
                        for n in range(N+1)]])
        gs=s.series(G,w,0,D+1).removeO().expand()
        Grow=s.Matrix([[gs.coeff(w,n)*s.factorial(n) for n in range(D+1)]])
        T=s.Matrix(D+1,N+1,
            lambda i,j:s.Poly(sum(a*(X+b)**j for a,b in f['shifts']),X).nth(i))
        ok(tag+' exact polynomial duality CGR4',zero(Grow*T-Frow))
        A=s.simplify(lower_phi.inv()*T*upper_phi[:,v:])
        BF=Frow*upper_phi[:,v:]
        Brow=Grow*lower_phi
        ok(tag+' complete shifted Gamma matrix CGR9',zero(BF*A.inv()-Brow))
        embedding=s.Matrix(D+1,M+1,
            lambda i,j:s.Poly(chip*X**j,X).nth(i))
        H=s.simplify(embedding.conjugate().T*lower_gram*embedding)
        obs=Grow*embedding
        direct=s.cancel((obs*H.inv()*obs.conjugate().T)[0])
        B=s.simplify(lower_phi.inv()*embedding)
        PI=s.simplify(B*(B.conjugate().T*B).inv()*B.conjugate().T)
        ok(tag+' retained projection self-adjoint idempotent',
           zero(PI-PI.conjugate().T) and zero(PI*PI-PI))
        projected=s.cancel((Brow*PI*Brow.conjugate().T)[0])
        ok(tag+' exact projected covariance CGR9',s.cancel(projected-direct)==0)
        full=s.cancel((Brow*Brow.conjugate().T)[0])
        ok(tag+' negative control projection cannot be deleted',full>direct)
        low=s.eye(M+1)[:,:g]
        if L>=0:
            U=s.Matrix(M+1,L+1,lambda i,j:s.Poly(s.cancel(
                sum(a*(chi*X**j).subs(X,X+b) for a,b in f['shifts'])/chip),X).nth(i))
            ok(tag+' full relation annihilation CGR6',zero(obs*U))
            Q=low.conjugate().T*H*low-(low.conjugate().T*H*U)*(
                U.conjugate().T*H*U).inv()*(U.conjugate().T*H*low)
        else:
            Q=H
        quotient=s.cancel(((obs*low)*Q.inv()*(obs*low).conjugate().T)[0])
        ok(tag+' attained quotient covariance unchanged',s.cancel(quotient-direct)==0)
        if L in [-1,0]:
            if L<0:
                Qd=H
            else:
                Id=s.Matrix(M+1,1,lambda i,j:s.Poly(d,X).nth(i))
                Qd=low.conjugate().T*H*low-(low.conjugate().T*H*Id)*(
                    Id.conjugate().T*H*Id).inv()*(Id.conjugate().T*H*low)
            ok(tag+' exact two-low-cutoff metric equality',zero(Q-Qd))

    # Test the original center and physical i phase in the analytic functional.
    order=6
    _,_,ps=gamma(order,cp)
    wz=-s.I*s.atan(t)
    generated=(1+t*t)**(-s.Rational(1,4))*s.exp(-cp*wz)*G.subs(w,wz)
    coeffs=s.series(generated,t,0,order+1).removeO().expand()
    gseries=s.series(G,w,0,order+1).removeO().expand()
    for n in range(order+1):
        pn=s.Poly(ps[n].subs(y,(X-cp)/s.I),X)
        functional=sum(pn.nth(j)*gseries.coeff(w,j)*s.factorial(j)
                       for j in range(n+1))/s.factorial(n)
        ok(f"{f['name']} physical generating phase n={n}",
           s.simplify(functional-coeffs.coeff(t,n))==0)
    wrong=(1+t*t)**(-s.Rational(1,4))*G.subs(w,s.I*s.atan(t))
    wrong1=s.series(wrong,t,0,2).removeO().coeff(t,1)
    ok(f"{f['name']} negative control wrong physical phase",
       s.simplify(wrong1-coeffs.coeff(t,1))!=0)

report={'status':'passed','checks':len(checks),'details':checks,
 'scope':'Exact CGR3--9 duality, complete graph minimum and Gamma projection; auxiliary finite-shift fixtures, not the original-period asymptotic theorem.',
 'mass':'Auxiliary rational Gamma Grams are divided by their common mass sqrt(2*pi); this same retained scalar cancels in every tested identity.',
 'not_tested':'CGR10--29 analytic inequalities have complete proofs in INVARIANT_COVARIANCE_POLE_FILTRATION.md; this finite checker does not evaluate the remaining small-eigenvalue determinant.'}
(BASE/'INVARIANT_COVARIANCE_EXACT_CHECKS.json').write_text(
    json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'passed','checks':len(checks)}))
