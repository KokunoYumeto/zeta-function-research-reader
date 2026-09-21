"""Independent exact check of RW numerator receiver and native Gram identities."""
import sympy as S

z, u = S.symbols("z u")
h = S.symbols("h", positive=True)
omega = S.symbols("omega")
b = h-omega
def zero(x):
    return S.cancel(S.expand(x)) == 0
for n in range(6):
    polynomials=[S.expand(S.sqrt(h)*(z+b)**j*(omega-z)**(n-j))
                 for j in range(n+1)]
    R=S.Matrix([[p.coeff(z,ell) for p in polynomials] for ell in range(n+1)])
    Ri=S.Matrix([[h**(-n-S.Rational(1,2))*sum(
        S.binomial(ell,r)*omega**r*(-b)**(ell-r)*S.binomial(n-ell,j-r)
        for r in range(ell+1)) for ell in range(n+1)] for j in range(n+1)])
    assert all(zero(x) for x in Ri*R-S.eye(n+1))
    assert all(zero(x) for x in R*Ri-S.eye(n+1))
    assert zero(R.det(method="domain-ge")-h**(S.Rational((n+1)**2,2)))
print("RW2--4: original numerator coefficients, inverse and determinant verified for n=0,...,5.")

d,tau,y,beta,mass=S.symbols("d tau y beta mass", real=True, positive=True)
kap=S.symbols("kappa",real=True)
ww=d+S.Rational(1,2)+S.I*tau
bb=d-S.Rational(1,2)-S.I*tau
Ns=[S.sqrt(2*d)*(z+bb)**j*(ww-z)**(3-j) for j in range(4)]
mom={0:mass,1:0,2:mass*beta,3:0,
     4:mass*(3*beta**2+2*beta),5:0,
     6:mass*(15*beta**3+30*beta**2+16*beta)}
def integral(p):
    p=S.Poly(S.expand(p),y)
    return S.expand(sum(c*mom[ex[0]] for ex,c in p.terms()))
H=S.zeros(4)
gs={}
for r in range(-3,4):
    gs[r]=integral(2*d*(d+S.I*(y-tau))**(3+r)
                  *(d-S.I*(y-tau))**(3-r))
for j in range(4):
    at=Ns[j].subs(z,S.Rational(1,2)+S.I*y)
    expected=S.sqrt(2*d)*(d+S.I*(y-tau))**j*(d-S.I*(y-tau))**(3-j)
    assert zero(at-expected)
    for k in range(4):
        bt=Ns[k].subs(z,S.Rational(1,2)+S.I*y)
        H[j,k]=integral(S.conjugate(at)*bt)
        assert zero(H[j,k]-gs[k-j])
monogram=S.Matrix([[S.conjugate(S.I**j)*S.I**k*mom[j+k]
                     for k in range(4)] for j in range(4)])
assert zero(monogram.det(method="domain-ge")
            -12*mass**4*beta**3*(beta+1)**2*(beta+2))
print("RW7--11: all 16 original Gamma moment entries, Toeplitz signs and native monomial determinant verified.")

rho,baromega=S.symbols("rho baromega")
for ii in range(4):
    for jj in range(4):
        # Exact reflected conjugate formula; h=omega+baromega-1.
        reflected=(omega+baromega-1)/(rho+baromega-1)/(omega-rho) \
                  *((omega-rho)/(rho+baromega-1))**ii \
                  *((rho+baromega-1)/(omega-rho))**jj
        desired=(omega+baromega-1)*(rho+baromega-1)**(jj-ii-1) \
                /(omega-rho)**(jj-ii+1)
        assert zero(reflected-desired)
print("RW12--13: all reflected full-Weil coefficient signs verified algebraically.")
print("All independent rational receiver checks passed.")
