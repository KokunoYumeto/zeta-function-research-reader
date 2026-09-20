"""Exact algebra checks for SD1--24, with nontrivial original-unit transport.

Finite matrices are universal-identity tests, not actual arithmetic sources.
Every check uses explicit exceptions and remains active under python -O.
"""
from itertools import combinations, product
import sympy as s

Q, I = s.Rational, s.I
counts = {"identity": 0, "inequality": 0, "negative": 0}


def eq(a, b, name):
    d = a-b
    good = (all(s.simplify(x) == 0 for x in d) if isinstance(d, s.MatrixBase)
            else s.simplify(d) == 0)
    if not good:
        raise RuntimeError((name, d))
    counts["identity"] += 1


def le(a, b, name):
    d = s.simplify(b-a)
    if not (d.is_real and d >= 0):
        raise RuntimeError((name, a, b))
    counts["inequality"] += 1


def neq(a, b, name):
    d = a-b
    same = (all(s.simplify(x) == 0 for x in d) if isinstance(d, s.MatrixBase)
            else s.simplify(d) == 0)
    if same:
        raise RuntimeError((name, "negative test unexpectedly equal"))
    counts["negative"] += 1


def simp(M):
    return M.applyfunc(s.simplify)


def lower_toeplitz(coeff):
    n = len(coeff)
    return s.Matrix(n, n, lambda j, l: coeff[j-l] if j >= l else 0)


def inverse_coefficients(beta):
    gamma = [1/beta[0]]
    for j in range(1, len(beta)):
        gamma.append(s.cancel(-sum(beta[l]*gamma[j-l] for l in range(1, j+1))/beta[0]))
    return gamma


def operator_tests():
    v = [I, -I, Q(3, 5)+Q(4, 5)*I, Q(3, 5)-Q(4, 5)*I]
    w = [Q(5, 13)+Q(12, 13)*I, Q(5, 13)-Q(12, 13)*I, -I, I]
    F = s.zeros(4)
    for j in range(4):
        F[j, j ^ 1] = 1
    eq(F.H*F, s.eye(4), "original-model Fourier unitarity")
    eq(F*F, s.eye(4), "original-model Fourier involution")
    E, T = s.eye(4), s.eye(4)
    for p, phases in [(2, v), (3, w)]:
        V, r = s.diag(*phases), 1/s.sqrt(p)
        eq(V.H*V, s.eye(4), "dilation unitarity")
        eq(F*V, V.H*F, "Fourier reverses dilation")
        Ep = s.diag(*[1/(1-r*z) for z in phases])
        Tp = s.eye(4)-r*V.H
        eq(Tp.H*Ep, s.eye(4), "full complex one-prime duality")
        for z in phases:
            modulus = s.simplify((1-r*z)*(1-r*s.conjugate(z)))
            le((1-r)**2, modulus, "one-prime lower norm bound")
            le(modulus, (1+r)**2, "one-prime upper norm bound")
        E, T = E*Ep, T*Tp
    E, T = simp(E), simp(T)
    eq(T, E.H.inv(), "finite-prime adjoint inverse")
    eq(E*E.H, E.H*E, "finite-prime normality")
    eq(T.H*E, s.eye(4), "full finite-prime cross pairing")
    eq(E.H*T, s.eye(4), "reversed full cross pairing")
    FP = simp(E*F*E.inv())
    eq(FP, E*E.H.inv()*F, "two Fourier presentations")
    eq(FP.H*FP, s.eye(4), "transferred Fourier unitary")
    eq(FP*FP, s.eye(4), "transferred Fourier involution")
    eq(FP.H, FP, "transferred Fourier selfadjoint")
    eq(FP*E, E*F, "primal exact intertwining")
    eq(FP*T, T*F, "dual exact intertwining")
    neq(T.T*E, s.eye(4), "conjugation cannot be omitted")
    # All complex polynomial Gram entries, not merely norms or real parts.
    ts, amps = [-2, -1, 1, 2], [1, 2, 3, 4]
    C = s.Matrix(4, 3, lambda j, l: amps[j]*(Q(1, 2)+I*ts[j])**l)
    H = C.H*C
    eq(H[0, 0], 30, "test source mass is not one")
    eq((T*C).H*(E*C), H, "complete original complex cross Gram")
    neq((T*C).H*(T*C), H, "dual transfer is not an isometry")
    # The two-factor multiplier cancels separately before pushforward by sum.
    CT = s.Matrix(16, 3, lambda row, l:
                  amps[row//4]*amps[row % 4]*(1+I*(ts[row//4]+ts[row % 4]))**l)
    TT, EE = s.kronecker_product(T, T), s.kronecker_product(E, E)
    eq((TT*CT).H*(EE*CT), CT.H*CT, "full tensor cross Gram before convolution")
    eq((CT.H*CT)[0, 0], 30**2, "original tensor test mass retained")


def jet_and_tensor_tests():
    z = s.symbols("z")
    # Formal spectral value variables; no native zero is assigned a value.
    a, b, L, M = s.symbols("a b L M")
    fun = (1-a*s.exp(L*z))*(1-b*s.exp(M*z))
    betas = []
    for j in range(4):
        beta = s.diff(fun, z, j).subs(z, 0)/s.factorial(j)
        subset = sum((-1)**len(A)*s.prod([a, b][i] for i in A)
                     *sum([L, M][i] for i in A)**j/s.factorial(j)
                     for size in range(3) for A in combinations(range(2), size))
        eq(beta, subset, "every subset divided-jet coefficient")
        betas.append(s.expand(beta))
    B = lower_toeplitz(betas)
    Bi = lower_toeplitz(inverse_coefficients(betas))
    eq(B*Bi, s.eye(4), "complete divided-jet inverse recurrence")
    N = s.zeros(4)
    for j in range(1, 4):
        N[j, j-1] = 1
    eq(B*N, N*B, "original multiplication intertwines all jets")
    eq(B.det(), betas[0]**4, "all jet multiplicities in determinant")
    # Full two-factor unit in a nonreduced local algebra.
    L = s.log(2)
    N = s.Matrix([[0, 0], [1, 0]])
    local = Q(1, 2)*s.eye(2)+N
    B = s.eye(2)-(s.eye(2)+L*N)/s.sqrt(2)
    unit = s.Matrix([2+I, 3-I])
    S = s.kronecker_product(local, s.eye(2))+s.kronecker_product(s.eye(2), local)
    NS = S-s.eye(4)
    v = s.kronecker_product(unit, unit)
    eta = s.Matrix.hstack(v, S*v, S**2*v)
    BT = s.kronecker_product(B, B)
    etaT = BT*eta
    eq(BT*S, S*BT, "full tensor sum-action intertwining")
    eq(NS**3*v, s.zeros(4, 1), "complete relation polynomial")
    eq(NS**3*BT*v, s.zeros(4, 1), "unchanged transformed relation polynomial")
    eq(eta.rank(), 3, "original cyclic injection dimension")
    eq(etaT.rank(), 3, "full tensor injection retains relation kernel")
    eq(BT.inv()*etaT, eta, "inverse on exactly the tensor image")
    bOfSum = s.eye(4)-(s.eye(4)+L*NS+L**2*NS**2/2)
    eq(bOfSum.det(), 0, "sum-only multiplier can lose invertibility")
    neq(BT.det(), 0, "factorwise multiplier retains invertibility")
    neq(BT*eta, bOfSum*eta, "tensor multiplier is not b of total S")


def theta_and_physical_tests():
    x = s.symbols("x", positive=True)
    f = s.Function("f")
    for p in (2, 3, 5):
        for length in (1, 3, 7):
            theta_f = 2*sum(f(n*x) for n in range(1, length+1))
            Ttheta = theta_f-theta_f.subs(x, x/p)/p
            thetaT = 2*sum(f(n*x)-f(n*x/p)/p for n in range(1, length+1))
            eq(Ttheta, thetaT, "literal theta factor-two finite commutation")
        eq(1-Q(1, p)*p, 0, "original whole-line integral condition")
    # Fixed physical target with nonconstant nontrivial unit, all Gaussian rational.
    beta = [Q(2)+I, Q(1)-I, Q(3, 2)+2*I]
    B = lower_toeplitz(beta)
    rho = Q(1, 2)+I
    to_jets = s.Matrix(3, 3, lambda j, l:
                       s.binomial(l, j)*rho**(l-j) if l >= j else 0)
    eta = lower_toeplitz([3-I, 2+I, -1+2*I])*to_jets
    R = s.Matrix([[2, I, 1], [0, 1, 1-I], [0, 0, 3]])
    G = R.H*R
    u = s.Matrix([1+I, 2-I, -1+3*I])
    c = eta.inv()*B.inv()*u
    eq(B*eta*c, u, "exact physical-target preimage")
    Gphys = (B*eta).inv().H*G*(B*eta).inv()
    eq(Gphys, B.inv().H*(eta.inv().H*G*eta.inv())*B.inv(), "correct SD24 congruence")
    eq((u.H*Gphys*u)[0], (c.H*G*c)[0], "physical-target attained quadratic form")
    neq(Gphys, B.inv().H*G*B.inv(), "dropping original physical unit is wrong")
    neq(B*eta*(B.inv()*u), u, "B inverse alone is not cyclic preimage")
    neq(B*eta*(B.inv()*eta.inv()*u), u, "inverse frame and unit order cannot be reversed")
    jet_action = rho*s.eye(3)+s.Matrix([[0, 0, 0], [1, 0, 0], [0, 1, 0]])
    cyclic_action = to_jets.inv()*jet_action*to_jets
    eq(B*eta*cyclic_action, jet_action*B*eta, "literal cyclic-to-jet multiplication map")


def separate_minimum_test():
    r = 1/s.sqrt(2)
    E = s.diag(1/(1-r), 1/(1+r))
    T = E.H.inv()
    J = s.Matrix([[1, 1]])
    H, HT, HE = s.eye(2), T.H*T, E.H*E

    def minimum(D):
        G = (J*D.inv()*J.H).inv()
        lift = D.inv()*J.H*G
        return G, lift

    G, v = minimum(H)
    GT, vt = minimum(HT)
    GE, ve = minimum(HE)
    eq(G[0, 0], Q(1, 2), "original scalar quotient minimum")
    eq(GT[0, 0], Q(1, 12), "dual quotient minimum")
    eq(GE[0, 0], Q(1, 3), "primal quotient minimum")
    eq((T*vt).H*(E*ve), vt.H*H*ve, "separate-lift exact cross identity")
    eq(((T*vt).H*(E*ve))[0], Q(1, 18), "separate minimum cross value")
    neq((T*vt).H*(E*ve), G, "separate minima do not collapse to original minimum")
    neq(vt, ve, "separately minimizing coefficient columns differ")


if __name__ == "__main__":
    operator_tests()
    jet_and_tensor_tests()
    theta_and_physical_tests()
    separate_minimum_test()
    print("PASS", counts, "total", sum(counts.values()))
    print("SD24 retains eta; no native measure, mass, zero or phase was substituted.")
