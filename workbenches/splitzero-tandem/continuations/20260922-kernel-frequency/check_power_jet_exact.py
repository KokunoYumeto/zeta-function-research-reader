"""Exact finite checks for the stated Gamma-power coefficient maps.

The fixtures verify algebra and mass factors. They do not certify the analytic
large-degree inequalities or the equilibrium limit.
"""
from pathlib import Path
import json
import sympy as S

BASE = Path(__file__).resolve().parent
y = S.Symbol("y", real=True)
alpha, scale = S.symbols("alpha scale", positive=True)
MASS = S.sqrt(2*S.pi)
checks = []


def check(name, value):
    if isinstance(value, S.MatrixBase):
        okay = all(S.simplify(v) == 0 for v in value)
    else:
        okay = S.simplify(value) == 0
    if not okay:
        raise AssertionError(name)
    checks.append(name)


# Verify the complete triangular transformation and its inverse for a symbolic
# Laguerre parameter and the literal scaled coefficient variable.
for degree in range(8):
    T = S.zeros(degree+1)
    U = S.zeros(degree+1)
    for j in range(degree+1):
        for i in range(j+1):
            entry = S.binomial(j,i)*S.rf(alpha+i+1,j-i)/scale**(j-i)
            T[i,j] = (-1)**(j-i)*entry
            U[i,j] = entry
    check(f"Laguerre symbolic inverse degree {degree}", T*U-S.eye(degree+1))


def gamma_moments(order):
    """Full original moments from g_(j+1)=y*g_j-j(j-1/2)g_(j-1)."""
    state = {0: S.Integer(1)}
    answer = [MASS]
    for _ in range(order):
        new = {}
        for j, coefficient in state.items():
            new[j+1] = new.get(j+1, 0)+coefficient
            if j:
                new[j-1] = new.get(j-1, 0)+coefficient*j*(j-S.Rational(1,2))
        state = new
        answer.append(MASS*state.get(0, 0))
    return answer


moments = gamma_moments(40)
check("original Gamma mass", moments[0]-S.sqrt(2*S.pi))
check("original second moment", moments[2]-MASS/2)
check("original fourth moment", moments[4]-7*MASS/4)


def gram(power, degree):
    return S.Matrix(degree+1, degree+1, lambda i,j: moments[2*power+i+j])


def monic(power, degree):
    G = gram(power, degree)
    low = -G[:degree,:degree].inv()*G[:degree,degree] if degree else S.zeros(0,1)
    v = low.col_join(S.Matrix([1]))
    return S.expand(sum(v[j]*y**j for j in range(degree+1))), S.simplify((v.T*G*v)[0])


for q,s,M in [(5,1,5), (6,2,7), (7,3,9)]:
    n = q-s
    L = M-s
    G = gram(n,M)
    J = S.zeros(s,M+1)
    for j in range(s):
        J[j,j] = q**j
    covariance = S.simplify(J*G.inv()*J.T)
    metric = covariance.inv()
    attained = S.simplify(G.inv()*J.T*metric)
    prefix = f"q={q},s={s},M={M}"
    check(prefix+" attained jet", J*attained-S.eye(s))
    check(prefix+" exact attained metric", attained.T*G*attained-metric)
    check(prefix+" covariance inverse", covariance*metric-S.eye(s))
    GL = gram(n,L)
    e0 = S.zeros(L+1,1)
    e0[0] = 1
    kc = GL.inv()*e0
    K00 = kc[0]
    hc = S.simplify(kc/K00)
    check(prefix+" kernel polynomial value", hc[0]-1)
    check(prefix+" kernel polynomial full norm", (hc.T*GL*hc)[0]-1/K00)
    # Formal reciprocal in x=y/q; keep every actual q power.
    h_scaled = [S.simplify(hc[j]*q**j) if j <= L else 0 for j in range(s)]
    reciprocal = [S.Integer(1)]
    for j in range(1,s):
        reciprocal.append(-sum(h_scaled[i]*reciprocal[j-i] for i in range(1,j+1)))
    R = S.zeros(M+1,s)
    for a in range(s):
        for j in range(a,s):
            bj = reciprocal[j-a]/q**j
            for h in range(L+1):
                if h+j <= M:
                    R[h+j,a] += hc[h]*bj
    check(prefix+" simultaneous kernel right inverse", J*R-S.eye(s))
    # Exact minimum orthogonality implies the trial-minus-minimum norm is PSD;
    # check its exact Gram factorization without assuming scalar covariance.
    defect = S.simplify(R-attained)
    check(prefix+" complete trial excess identity", R.T*G*R-metric-defect.T*G*defect)
    check(prefix+" homogeneous defect", J*defect)
    for degree in [L, L+1, M]:
        p,h = monic(n,degree)
        check(prefix+f" monic parity degree {degree}", p.subs(y,-y)-(-1)**degree*p)
    even_degree = 2*(L//2)
    ue,he = monic(n,even_degree)
    uo,_ = monic(n,even_degree+1)
    check(prefix+" full monic Christoffel factor", K00-ue.subs(y,0)*S.diff(uo,y).subs(y,0)/he)


receipt = {
    "scope": "Exact symbolic identities; no numerical certification of analytic bounds",
    "original_measure_mass": "sqrt(2*pi)",
    "fixtures": [[5,1,5],[6,2,7],[7,3,9]],
    "fixture_note": "Small fixtures test algebra only and are not within the asymptotic q>=40 guard",
    "passed": len(checks),
    "checks": checks,
}
(BASE/"EXACT_CHECK_RECEIPT.json").write_text(json.dumps(receipt,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"passed":len(checks),"receipt":"EXACT_CHECK_RECEIPT.json"}))
