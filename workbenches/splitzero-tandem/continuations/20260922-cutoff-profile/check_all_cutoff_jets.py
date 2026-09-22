"""Exact auxiliary checks of complete minima at every cutoff in two fixtures.

These are algebraic fixtures, not native quartet or period calculations. The
large-degree asymptotic and all invariant constraints are proved in the text.
"""
from pathlib import Path
import itertools
import json
import sympy as S

BASE = Path(__file__).resolve().parent
MASS = S.sqrt(2*S.pi)
passed = []


def check(name, value):
    if isinstance(value, S.MatrixBase):
        valid = all(S.simplify(v) == 0 for v in value)
    else:
        valid = S.simplify(value) == 0
    if not valid:
        raise AssertionError(name)
    passed.append(name)


def require(name, valid):
    if valid is not True:
        raise AssertionError(name)
    passed.append(name)


def gamma_moments(order):
    # Literal y coordinate: monic recurrence b_j=j(j-1/2).
    state = {0:S.Integer(1)}
    answer = [MASS]
    for _ in range(order):
        nxt = {}
        for j, coefficient in state.items():
            nxt[j+1] = nxt.get(j+1,0)+coefficient
            if j:
                nxt[j-1] = nxt.get(j-1,0)+coefficient*j*(j-S.Rational(1,2))
        state = nxt
        answer.append(MASS*state.get(0,0))
    return answer


moments = gamma_moments(48)


def gram(n, degree):
    return S.Matrix(degree+1,degree+1,lambda a,b:moments[2*n+a+b])


def psd(name, matrix):
    # Every principal minor, including singular cases; fixture jet size <=2.
    for r in range(1,matrix.rows+1):
        for ix in itertools.combinations(range(matrix.rows),r):
            minor = S.simplify(matrix.extract(ix,ix).det())
            require(name+f" principal minor {ix}", bool(minor >= 0))


check("original Gamma mass",moments[0]-S.sqrt(2*S.pi))
fixture_counts = []
for q,s in [(10,1),(8,2)]:
    n = q-s
    previous_metric = None
    previous_K = None
    count_before = len(passed)
    for j in range(q+2):
        N = q-1+j
        M = s+j-1
        label = f"q={q},s={s},j={j},N={N},M={M}"
        G = gram(n,M)
        Gi = G.inv()
        J = S.zeros(s,M+1)
        for a in range(s):
            J[a,a] = q**a
        covariance = J*Gi*J.T
        metric = covariance.inv()
        section = S.simplify(Gi*J.T*metric)
        check(label+" complete attained section",J*section-S.eye(s))
        check(label+" complete attained metric",section.T*G*section-metric)
        check(label+" full covariance inverse",covariance*metric-S.eye(s))
        D = S.diag(*[S.Rational(1,q**a) for a in range(M+1)])
        scaled = D*G*D
        schur = scaled[:s,:s]
        if M >= s:
            schur = schur-scaled[:s,s:]*scaled[s:,s:].inv()*scaled[s:,:s]
        check(label+" entire relation Schur minimum",metric-schur)
        injection = S.zeros(N+1,M+1)
        for a in range(M+1):
            injection[n+a,a] = 1
        check(label+" original full source norm",injection.T*gram(0,N)*injection-G)
        h = M//2
        even = S.Matrix(h+1,h+1,lambda a,b:moments[2*(n+a+b)]/n**(2*(a+b)))
        K = Gi[0,0]
        check(label+" complete even scalar",K-even.inv()[0,0])
        scalar = S.simplify(moments[2*n]*K)
        require(label+" full mass cancels only in scalar",scalar.is_Rational is True)
        if M%2 and previous_K is not None:
            check(label+" exact odd parity",K-previous_K)
        if previous_metric is not None:
            psd(label+" source nesting",S.simplify(previous_metric-metric))
        if j:
            L = j-1
            GL = gram(n,L)
            e0 = S.zeros(L+1,1); e0[0] = 1
            kc = GL.inv()*e0
            K00 = kc[0]
            hc = S.simplify(kc/K00)
            check(label+" kernel trial value",hc[0]-1)
            check(label+" kernel trial full norm",(hc.T*GL*hc)[0]-1/K00)
            h_scaled = [S.simplify(hc[a]*q**a) if a<=L else 0 for a in range(s)]
            reciprocal = [S.Integer(1)]
            for a in range(1,s):
                reciprocal.append(-sum(h_scaled[b]*reciprocal[a-b] for b in range(1,a+1)))
            R = S.zeros(M+1,s)
            for a in range(s):
                for b in range(a,s):
                    for hindex in range(L+1):
                        if hindex+b <= M:
                            R[hindex+b,a] += hc[hindex]*reciprocal[b-a]/q**b
            check(label+" simultaneous whole-jet right inverse",J*R-S.eye(s))
            defect = S.simplify(R-section)
            check(label+" complete trial excess factorization",R.T*G*R-metric-defect.T*G*defect)
            if j==1:
                check(label+" first residual kernel is one",hc-S.Matrix([1]))
        previous_metric, previous_K = metric,K
    fixture_counts.append({'q':q,'s':s,'cutoffs':q+2,'checks':len(passed)-count_before})

receipt = {
    'scope':'Exact auxiliary full-source/jet algebra; no native data or asymptotic certificate',
    'original_mass':'sqrt(2*pi)',
    'fixtures':fixture_counts,
    'fixture_guard':'q=10,s=1 satisfies the jet ratio guard; q=8,s=2 tests algebra outside that asymptotic guard. Neither fixture supplies native arithmetic data.',
    'passed':len(passed),
    'checks':passed,
}
(BASE/'EXACT_CUTOFF_CHECKS.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':len(passed),'fixtures':fixture_counts}))
