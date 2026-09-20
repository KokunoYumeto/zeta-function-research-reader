"""Exact finite algebra audits for BURNOL_ORIGINAL_THETA_TRANSFER.tex.

Artificial roots and rational Taylor coefficients test algebra, not zero
locations or analytic estimates for zeta. The accompanying proof establishes
the analytic claims. No numerical approximation is used in these checks.
"""
import math
import sympy as sp

s, t = sp.symbols('s t')


def coeff(expr, n):
    if n < 0:
        return sp.S.Zero
    return sp.expand(expr).coeff(t, n)


def inverse_coefficients(values, n):
    inv = [1 / values[0]]
    for j in range(1, n):
        inv.append(sp.cancel(-sum(values[k] * inv[j-k]
                                  for k in range(1, j+1)) / values[0]))
    return inv


checks = 0
rho = sp.Rational(1, 3) + 2 * sp.I
for m in range(1, 10):
    d = [sp.Rational((-1)**j * (j+2), j+1) for j in range(m)]
    c = inverse_coefficients(d, m)
    D = lambda n: d[n] if n >= 0 else 0
    C = lambda n: c[n] if n >= 0 else 0
    native = sp.Matrix(m, m, lambda k, l: sp.factorial(k)*D(k-m+l+1))
    native_inv = sp.Matrix(m, m, lambda l, k: C(m-l-1-k)/sp.factorial(k))
    assert native_inv*native == sp.eye(m)
    assert native.det() == (-1)**(m*(m-1)//2)*sp.prod(sp.factorial(k) for k in range(m))*d[0]**m
    p = [rho*(rho-1), 2*rho-1, 1]
    q = [sp.cancel((-1)**n*((rho-1)**(-n-1)-rho**(-n-1))) for n in range(m)]
    conversion = sp.Matrix(m, m, lambda j, k: p[j-k]/sp.factorial(k) if 0 <= j-k <= 2 else 0)
    conversion_inv = sp.Matrix(m, m, lambda k, j: sp.factorial(k)*q[k-j] if k >= j else 0)
    assert (conversion*conversion_inv-sp.eye(m)).applyfunc(sp.cancel) == sp.zeros(m)
    e = [sp.expand(sum(p[v]*D(n-v) for v in range(min(2,n)+1))) for n in range(m)]
    v = [sp.cancel(sum(q[j]*c[n-j] for j in range(n+1))) for n in range(m)]
    physical = sp.Matrix(m, m, lambda j,l: e[j-m+l+1] if j-m+l+1 >= 0 else 0)
    physical_inv = sp.Matrix(m, m, lambda l,j: v[m-l-1-j] if m-l-1-j >= 0 else 0)
    assert (physical-conversion*native).applyfunc(sp.cancel) == sp.zeros(m)
    assert (physical_inv*physical-sp.eye(m)).applyfunc(sp.cancel) == sp.zeros(m)
    assert (physical_inv-native_inv*conversion_inv).applyfunc(sp.cancel) == sp.zeros(m)
    checks += 6

# Repeated-root partial fractions, original physical units, and other-root
# coefficients on an exact three-root divisor of total degree six.
roots = [(sp.Rational(1,3)+sp.I, 3), (sp.Rational(2,3)-sp.I, 2), (sp.Rational(1,4)+2*sp.I, 1)]
h = sp.Poly(sp.prod((s-r)**m for r,m in roots), s).as_expr()
d = sp.degree(h, s)
U = 2+s+s**2
V = sp.Matrix([[sp.binomial(n,j)*r**(n-j) if n >= j else 0
                for n in range(d)] for r,m in roots for j in range(m)])
Vinv = V.inv()
unit = sp.diag(*[sp.Matrix(m,m,lambda j,k: sp.diff(U,s,j-k).subs(s,r)/sp.factorial(j-k)
                          if j>=k else 0) for r,m in roots])
reference = Vinv*unit.inv()
partial_matrix = sp.zeros(d)
physical_matrix = sp.zeros(d)
offset = 0
for r,m in roots:
    hr = sp.div(h, (s-r)**m, s)[0]
    alpha = [sp.cancel(sp.diff(1/hr,s,n).subs(s,r)/sp.factorial(n)) for n in range(m)]
    explicit = []
    others = [(r2,m2) for r2,m2 in roots if r2 != r]
    H0 = sp.prod((r-r2)**m2 for r2,m2 in others)
    for n in range(m):
        total = 0
        for n0 in range(n+1):
            n1 = n-n0
            pairs = list(zip((n0,n1), others))
            total += sp.prod(sp.binomial(m2+v-1,v)/(r-r2)**v for v,(r2,m2) in pairs)
        explicit.append(sp.cancel((-1)**n*total/H0))
    assert all(sp.cancel(a-b)==0 for a,b in zip(alpha,explicit))
    for ell in range(1,m+1):
        for n in range(d):
            partial_matrix[offset+ell-1,n] = sp.cancel(sp.diff(s**n/hr,s,m-ell).subs(s,r)/sp.factorial(m-ell))
        # In this algebra test g=h*U, so the exact physical jet coefficient
        # is that of (s-r)^(m-ell) hr(s) U(s).
        for j in range(m):
            physical_matrix[offset+j,offset+ell-1] = sp.cancel(sp.diff(hr*U,s,j-m+ell).subs(s,r)/sp.factorial(j-m+ell)) if j-m+ell>=0 else 0
    offset += m
assert (physical_matrix*partial_matrix*reference-sp.eye(d)).applyfunc(sp.cancel)==sp.zeros(d)
checks += 4
for N in range(0, 13):
    P = sum(sp.Rational((-1)**n*(n+1), n+2)*s**n for n in range(N+1))
    Q,R = sp.div(P,h,s)
    assert sp.expand(P-h*Q-R)==0
    rcoeff = sp.Matrix([sp.expand(R).coeff(s,n) for n in range(d)])
    parts = partial_matrix*rcoeff
    rational = 0
    offset=0
    for r,m in roots:
        rational += sum(parts[offset+l-1]/(s-r)**l for l in range(1,m+1))
        offset += m
    assert sp.cancel(rational-R/h)==0
    assert sp.cancel(U*P-(h*U*rational+h*U*Q))==0
    checks += 3

# Gaussian derivative and Mellin polynomial factor, exact symbolic identities.
x,z = sp.symbols('x z')
gaussian = sp.exp(-sp.pi*x*x)
Dop = lambda f: -x*sp.diff(f,x)
phi = (4*sp.pi**2*x**4-6*sp.pi*x*x)*gaussian
assert sp.expand(Dop(Dop(gaussian)-gaussian)-phi)==0
assert sp.expand(4*z*(z+1)-6*z-(2*z)*(2*z-1))==0
checks += 2

# Gram/Schur identity on unchanged polynomial fibres. A positive rational
# moment functional is used to audit the universal finite linear algebra.
hs = s**2-3*s+1
ds = 2
ref = sp.Matrix([[1,0],[0,1]])
for N in range(1,7):
    nodes = list(range(1,N+3))
    weights = [sp.Rational(1,j+1) for j in range(len(nodes))]
    H = sp.Matrix(N+1,N+1,lambda i,j:sum(w*n**(i+j) for n,w in zip(nodes,weights)))
    columns = [sp.Matrix([int(n==j) for n in range(N+1)]) for j in range(ds)]
    for k in range(N-ds+1):
        columns.append(sp.Matrix([sp.expand(hs*s**k).coeff(s,n) for n in range(N+1)]))
    L=sp.Matrix.hstack(*columns)
    J=L.inv()[:ds,:]
    full=L.T*H*L
    A=full[:ds,:ds]
    if N>=ds:
        Cg=full[:ds,ds:]
        Sg=full[ds:,ds:]
        schur=A-Cg*Sg.inv()*Cg.T
        u=sp.Matrix([2,-3])
        qstar=-Sg.inv()*Cg.T*u
        fullvec=sp.Matrix.vstack(u,qstar)
        assert (fullvec.T*full*fullvec)[0] == (u.T*schur*u)[0]
    else:
        schur=A
    assert (schur-(J*H.inv()*J.T).inv()).applyfunc(sp.cancel)==sp.zeros(ds)
    assert sp.det(full)>0 and sp.det(schur)>0
    checks += 3 if N>=ds else 2

print(f'PASS: {checks} exact finite assertions; multiplicities 1..9; full degree tests 0..12; Gram/Schur degrees 1..6.')
print('Artificial algebraic data are labelled as such; no RH or analytic convergence claim is tested numerically.')
