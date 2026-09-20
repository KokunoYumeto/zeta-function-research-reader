"""Exact universal moment tests; NONE of the atomic measures is the native one.

The native moments are intentionally not assigned values.  Finite positive
atomic examples test the matrix identities proved for the actual measure.
"""
from itertools import combinations
import sympy as s

QQ = s.Rational
nodes = list(map(QQ, [1, 2, 3, 5, 8, 13]))
weights0 = list(map(QQ, [2, 3, 5, 7, 11, 17]))
checked = 0


def simp(m):
    return m.applyfunc(s.simplify)


def psd(m):
    global checked
    m = simp(m)
    assert m == m.H
    # Exact Schur elimination; zero diagonal forces a zero residual row.
    z = m.copy()
    for k in range(z.rows):
        p = s.simplify(z[k, k])
        assert p.is_real and p >= 0, (k, p)
        if p == 0:
            assert all(s.simplify(z[i, k]) == 0 for i in range(k + 1, z.rows))
        else:
            for i in range(k + 1, z.rows):
                for j in range(k + 1, z.cols):
                    z[i, j] = s.simplify(z[i, j] - z[i, k]*z[k, j]/p)
    checked += 1


def moments(weights, degree):
    return [sum(w*x**r for x, w in zip(nodes, weights)) for r in range(degree+1)]


def hankel(mu, n, shift=0):
    return s.Matrix(n+1, n+1, lambda i, j: mu[i+j+shift])


def integral(weights, n, multiplier):
    return s.Matrix(n+1, n+1, lambda i, j:
                    sum(w*x**(i+j)*multiplier(x) for x, w in zip(nodes, weights)))


def bounds(weights, n, t, a):
    mu = moments(weights, 2*t+3)
    H = hankel(mu, t)
    D = hankel(mu, t, 1)
    E = hankel(mu, t, 2)
    C = H[:, :n+1]
    Cx = D[:, :n+1]
    Z, Y = D+a*H, E+a*D
    Rlo = C.H*Z.inv()*C
    Blo = Cx.H*Y.inv()*Cx
    Hn = hankel(mu, n)
    Rhi, Bhi = (Hn-Blo)/a, Hn-a*Rlo
    gap = Bhi-Blo
    R = integral(weights, n, lambda x: 1/(x+a))
    B = integral(weights, n, lambda x: x/(x+a))
    for matrix in (R-Rlo, Rhi-R, B-Blo, Bhi-B, gap):
        psd(matrix)
    assert simp(a*(Rhi-Rlo)-gap) == s.zeros(n+1)
    assert simp(a*R+B-Hn) == s.zeros(n+1)

    # Matrix residual identities, before testing any vector.
    coef0 = Z.inv()*C
    coef1 = Y.inv()*Cx
    residual0, residual1 = s.zeros(n+1), s.zeros(n+1)
    for x, w in zip(nodes, weights):
        vt = s.Matrix([x**j for j in range(t+1)])
        vn = s.Matrix([x**j for j in range(n+1)])
        r0 = vn.T/(x+a)-vt.T*coef0
        r1 = vn.T/(x+a)-vt.T*coef1
        residual0 += w*(x+a)*r0.H*r0
        residual1 += w*x*(x+a)*r1.H*r1
    assert simp(residual0-(R-Rlo)) == s.zeros(n+1)
    assert simp(residual1-(B-Blo)) == s.zeros(n+1)
    d = t-n
    cap = hankel(mu, n, 2*d+2)/a**(2*d+2)
    psd(cap-gap)
    assert C.H*H.inv()*C == Hn  # full Stieltjes weight sum, not unit mass
    return Rlo, Rhi, Blo, Bhi, B, gap, mu


for parity in (0, 1):
    weights = [w*x**parity for x, w in zip(nodes, weights0)]
    for n in (0, 1, 2):
        for a in map(QQ, [1, 4, 9, 16]):
            earlier = None
            for t in (n, n+1):
                result = bounds(weights, n, t, a)
                if earlier is not None:
                    for matrix in (result[0]-earlier[0], earlier[1]-result[1],
                                   result[2]-earlier[2], earlier[3]-result[3]):
                        psd(matrix)
                earlier = result
print("Both parity blocks: complementary bounds, exact residuals, monotonicity, pole-rate certificates, and full masses passed.")

# Signed partial fractions and a positive quadratic-denominator lower bound.
for parity in (0, 1):
    weights = [w*x**parity for x, w in zip(nodes, weights0)]
    n, t = 1, 2
    for a, b in ((QQ(4), QQ(1)), (QQ(4), QQ(9)), (QQ(16), QQ(9))):
        Ra = bounds(weights, n, t, a)
        Rb = bounds(weights, n, t, b)
        mu = Ra[-1]
        Cx = hankel(mu, t, 1)[:, :n+1]
        Z2 = hankel(mu, t, 3)+(a+b)*hankel(mu, t, 2)+a*b*hankel(mu, t, 1)
        Tlo = Cx.H*Z2.inv()*Cx
        Thi = (b*Rb[1]-a*Ra[0])/(b-a) if b>a else (a*Ra[1]-b*Rb[0])/(a-b)
        Tex = integral(weights, n, lambda x: x/((x+a)*(x+b)))
        Rax = integral(weights, n, lambda x: 1/(x+a))
        Rbx = integral(weights, n, lambda x: 1/(x+b))
        assert simp(Tex-(b*Rbx-a*Rax)/(b-a)) == s.zeros(n+1)
        psd(Tex-Tlo)
        psd(Thi-Tex)
        coef = Z2.inv()*Cx
        residual = s.zeros(n+1)
        for x, w in zip(nodes, weights):
            vt=s.Matrix([x**j for j in range(t+1)])
            vn=s.Matrix([x**j for j in range(n+1)])
            r=vn.T/((x+a)*(x+b))-vt.T*coef
            residual += w*x*(x+a)*(x+b)*r.H*r
        assert simp(residual-(Tex-Tlo)) == s.zeros(n+1)
print("Original-moment rational route: both pole orderings, exact signed partial fraction, and full quadratic residual passed.")

# Transport arbitrary verified positive moment brackets through exact complex
# coefficient coordinates and fixed observation/conductor maps.
def quotient(A, H):
    return simp((A*H.inv()*A.H).inv())


ratios, conductor_ratios = [], []
for N in (1, 2, 3, 4):
    blocks_lo, blocks_hi, blocks_true = [], [], []
    for parity, n in ((0, N//2), (1, (N-1)//2)):
        weights = [w*x**parity for x, w in zip(nodes, weights0)]
        bound = bounds(weights, n, n+1, QQ(4))
        blocks_lo.append(bound[2])
        blocks_hi.append(bound[3])
        blocks_true.append(bound[4])
    Hlo, Hhi, H = (s.diag(*blocks) for blocks in (blocks_lo, blocks_hi, blocks_true))
    centre=QQ(9,2)
    T=s.Matrix(N+1, N+1, lambda r,j:s.binomial(j,r)*centre**(j-r)*s.I**r if r<=j else 0)
    order=list(range(0,N+1,2))+list(range(1,N+1,2))
    Pi=s.eye(N+1)[order,:]
    L=Pi*T
    assert T.det()==s.I**(N*(N+1)//2)
    assert L.det()==Pi.det()*T.det()
    J=s.Matrix([[1 if j==0 else j+1 for j in range(N+1)],
                [0 if j==0 else (-1)**j*j for j in range(N+1)]])
    unit=s.diag(2+s.I,3-2*s.I)
    AS=unit*J
    A=AS*L.inv()
    QS=quotient(AS,L.H*H*L)
    Q=quotient(A,H)
    Qlo,Qhi=quotient(A,Hlo),quotient(A,Hhi)
    assert QS==Q
    psd(Q-Qlo);psd(Qhi-Q)
    lift=H.inv()*A.H*Q
    assert simp(A*lift)==s.eye(2)
    assert simp(lift.H*H*lift-Q)==s.zeros(2)
    conductor=s.Matrix([[1,1+s.I]])
    Ts=[quotient(conductor,Z) for Z in (Qlo,Q,Qhi)]
    assert Ts[0]==quotient(conductor*A,Hlo)
    assert Ts[2]==quotient(conductor*A,Hhi)
    psd(Ts[1]-Ts[0]);psd(Ts[2]-Ts[1])
    ratios.append((s.simplify(Q.det()/Qlo.det()),s.simplify(Qhi.det()/Qlo.det())))
    conductor_ratios.append((s.simplify(Ts[1].det()/Ts[0].det()),s.simplify(Ts[2].det()/Ts[0].det())))
for family in (ratios,conductor_ratios):
    exact_ratio=family[0][0]*family[1][0]/(family[2][0]*family[3][0])
    lower=1/(family[2][1]*family[3][1])
    upper=family[0][1]*family[1][1]
    assert s.simplify(exact_ratio-lower)>=0
    assert s.simplify(upper-exact_ratio)>=0
print("Complex S transport, retained nontrivial unit, observation and conductor minima, and both signed four-endpoint enclosures passed.")

# Symbolic reciprocal-polynomial residual and exact combination of errors.
x,a=s.symbols("x a", positive=True)
for d in range(7):
    q=sum((-x/a)**r for r in range(d+1))/a
    residual=(-1)**(d+1)*x**(d+1)/(a**(d+1)*(x+a))
    assert s.factor(1/(x+a)-q-residual)==0
    assert s.factor((a*(x+a)+x*(x+a))*residual**2-x**(2*d+2)/a**(2*d+2))==0
print("Exact symbolic reciprocal residual and complementary pole-rate cancellation passed through d=6.")

# Independent finite review of the root's RR6--RR11 rank-one refinement.
# This tests its formulas without modifying or replacing its derivation.
for parity in (0,1):
    weights=[w*x**parity for x,w in zip(nodes,weights0)]
    for n in (0,1,2):
        for r in (n+1,n+2):
            mu=moments(weights,2*r)
            Hr=hankel(mu,r-1)
            Dr=hankel(mu,r-1,1)
            Cr=Hr[:,:n+1]
            end=s.eye(r)[:,r-1]
            kappa=1/(end.T*Dr.inv()*end)[0]
            Dtilde=Dr-kappa*end*end.T
            psd(Dtilde)
            pcoeff=-(Hr.inv()*s.Matrix(mu[r:2*r]))
            for pole in (QQ(4),QQ(16)):
                resol=(Dr+pole*Hr).inv()
                Flo=Cr.T*resol*Cr
                Fhi=Cr.T*(Dtilde+pole*Hr).inv()*Cr
                Ftrue=integral(weights,n,lambda x:1/(x+pole))
                pminus=(-pole)**r+sum(pcoeff[i]*(-pole)**i for i in range(r))
                z=s.Matrix([(-pole)**i for i in range(n+1)])
                gamma=kappa/(pminus**2*(1-kappa*(end.T*resol*end)[0]))
                lam=s.simplify(Ftrue[0,0]-Flo[0,0])
                assert simp(Fhi-Flo-gamma*z*z.T)==s.zeros(n+1)
                assert simp(Ftrue-Flo-lam*z*z.T)==s.zeros(n+1)
                assert 0<=lam<=gamma
                psd(Ftrue-Flo);psd(Fhi-Ftrue)
print("Independent root RR review: exact Gauss/Radau rank-one gaps and scalar native-error structure passed on both parity test blocks.")
print("Total exact PSD checks:",checked)
print("All examples are universal finite tests, not evaluated native arithmetic moments.")
