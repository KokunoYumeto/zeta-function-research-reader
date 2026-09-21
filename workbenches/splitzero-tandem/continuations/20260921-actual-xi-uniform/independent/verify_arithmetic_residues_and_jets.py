"""Exact AR1--17 / AX1--8 algebra certificate; no numerical zeta claims."""
import sympy as S

i = S.I
a, y, z, w, s, t = S.symbols("a y z w s t")
A, B, C1, D, r = S.symbols("A B C1 D r")
delta, gamma = S.symbols("delta gamma", nonzero=True, real=True)
U, alpha, X, Xp = S.symbols("U alpha X Xp", real=True)

def zero(q):
    return S.expand(S.cancel(q)) == 0

def mzero(M):
    return all(zero(q) for q in M)

b = i+a*y
c = -i+2*a*y+a*a*z
d = -i*y-a*(i*z+2*y*y)-a*a*y*z
e = 2*z-7*i*y*y+a*w
f = i*w+3*i*y**3-4*y*z+a*(6*i*y*y*z+w*y+4*y**4)+2*a*a*y**3*z
assert zero(a*d+b*c-1)
assert zero(a**3*f-a*a*b*e+a*b*b*d-b**3*c-1)
P = S.Matrix([a*c, a*e+b*d, a*f+b*e, b*f])
for sig in [-1, 1]:
    factors = [0, sig*i, -sig*i, -sig*i*B, -sig*i*C1, -sig*i*D]
    aa, bb, cc, dd, ee, ff = factors
    assert zero(aa*dd+bb*cc-1)
    assert zero(aa**3*ff-aa*aa*bb*ee+aa*bb*bb*dd-bb**3*cc-1)
    assert mzero(S.Matrix([aa*cc, aa*ee+bb*dd, aa*ff+bb*ee, bb*ff])
                 -S.Matrix([0,B,C1,D]))
print("AR1--5: original factor identities and both infinity signs verified.")

# Complete coordinate sign in the overlap s=1/t, with the root relation retained.
Dr = -A*r**4-r**3-B*r**2-C1*r
hr = A*s**4+s**3+B*s**2+C1*s+Dr
gr = A+t+B*t**2+C1*t**3+Dr*t**4
assert zero(S.diff(gr,t).subs(t,1/r)+S.diff(hr,s).subs(s,r)/r**2)
assert zero(-(-a*r)**2*S.diff(gr,t).subs(t,1/r)
            -a**2*S.diff(hr,s).subs(s,r))
print("AR4: finite/infinity overlap derivative and residue signs verified.")

x = s-S.Rational(1,2)
k = delta**2-gamma**2
H = S.expand((x*x-k)**2+4*delta**2*gamma**2)
coeff = [H.coeff(s,j) for j in range(4)]
Cs = S.zeros(4)
for j in range(3):
    Cs[j+1,j] = 1
for j in range(4):
    Cs[j,3] = -coeff[j]
Q = (Cs-S.eye(4)/2)**2-k*S.eye(4)
assert mzero(Q*Q+4*delta**2*gamma**2*S.eye(4))
Mx = U*S.eye(4)+alpha*Q
assert mzero(Mx*(U*S.eye(4)-alpha*Q)
             -(U**2+4*alpha**2*delta**2*gamma**2)*S.eye(4))
assert zero(Mx.det(method="domain-ge")-(U**2+4*alpha**2*delta**2*gamma**2)**2)
for eps in [-1,1]:
    for eta in [-1,1]:
        root = S.Rational(1,2)+eps*delta+i*eta*gamma
        assert zero(H.subs(s,root))
        assert zero(-S.diff(H,s).subs(s,root)/2
                    -4*delta*gamma*(eps*gamma-i*eta*delta))
print("AR10--14: quartet scaling, multiplication determinant and inverse verified.")

rows = []
for eta in [1,-1]:
    rr = S.Rational(1,2)+i*eta*gamma
    rows += [[1,rr,rr*rr+delta*delta,rr**3+3*rr*delta*delta],
             [0,1,2*rr,3*rr*rr+delta*delta]]
Vd = S.Matrix(rows)
assert zero(Vd.det(method="domain-ge")-16*gamma**2*(gamma**2+delta**2))
V0 = Vd.subs(delta,0)
cols = []
for eta in [1,-1]:
    rr = S.Rational(1,2)+i*eta*gamma
    other = S.Rational(1,2)-i*eta*gamma
    dd = rr-other
    ll = (s-other)/dd
    for poly in [(1-2*(s-rr)/dd)*ll**2,(s-rr)*ll**2]:
        poly = S.expand(poly)
        cols.append(S.Matrix([poly.coeff(s,j) for j in range(4)]))
Vinv = S.Matrix.hstack(*cols)
assert mzero(V0*Vinv-S.eye(4))
C0 = Cs.subs(delta,0)
T0 = (C0-S.eye(4)/2)**2+gamma**2*S.eye(4)
assert mzero(T0*T0)
M0 = X*S.eye(4)-Xp*T0/(2*gamma)
blocks = S.diag(S.Matrix([[X,0],[-i*Xp,X]]),
                S.Matrix([[X,0],[i*Xp,X]]))
assert mzero(V0*M0*Vinv-blocks)
assert mzero(M0*(S.eye(4)/X+Xp*T0/(2*gamma*X*X))-S.eye(4))
print("AR15--17: exact paired determinant, Hermite inverse and original-basis Jordan data verified.")

ph, lp, xx, xp = S.symbols("phi logderiv value derivative", nonzero=True)
MP = S.Matrix([[ph,0],[ph*lp,ph]])
MPI = S.Matrix([[1/ph,0],[-lp/ph,1/ph]])
assert mzero(MP*MPI-S.eye(2))
for eta in [1,-1]:
    dd = 2*i*eta*gamma
    assert zero(-2*X/dd**2-X/(2*gamma**2))
    assert zero(-2*(-i*eta*Xp)/dd**2+4*X/dd**3
                -i*eta*(X-gamma*Xp)/(2*gamma**3))
    for eps in [1,-1]:
        exact_first = (X-eps*delta*i*eta*Xp)/(
                       4*delta*gamma*(eps*gamma-i*eta*delta))
        prescribed = eps*X/(4*delta*gamma**2)+i*eta*(X-gamma*Xp)/(4*gamma**3)
        assert S.limit(S.cancel(exact_first-prescribed),delta,0) == 0
print("AX1--3: full completion jet inverse and both confluent Laurent coefficients verified.")

pi = S.symbols("pi", nonzero=True)
R = S.Rational(1,2)+(pi-3)*(s*s-s)/12
Ri = 2+(3/pi-1)*(s*s-s)
assert zero(S.rem(S.expand(R*Ri-1),s**3-s,s))
assert zero(R.subs(s,-1)*R.subs(s,0)*R.subs(s,1)-pi/24)
eps = S.symbols("eps", nonzero=True)
q = {a:eps,y:0,z:i/2,w:0}
target = S.Matrix([-i*eps+i*eps**3/2,3*i*eps/2,-1,0])
assert mzero(P.subs(q)-target)
hh = target[0]*s**4+s**3+target[1]*s*s-s
factor = i*eps*s*(s+i/eps)*((eps**2/2-1)*s*s-i*eps*s/2+1)
assert zero(hh-factor)
assert zero(S.discriminant(hh,s)-(4-S.Rational(9,4)*eps**2))
assert zero(10*S.Rational(1,20)/(3*(1-S.Rational(1,8000)))-S.Rational(8000,47994))
assert S.Rational(8000,47994) < S.Rational(1,3)
print("AR9 / AX4--8: collision inverse, complete escape polynomial and elementary rational bound verified.")
print("All exact arithmetic residue and confluent-jet algebra checks passed.")
