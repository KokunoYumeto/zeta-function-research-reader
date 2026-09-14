"""Exact finite checks of the supplied PR29 continuation.

All Grams are original moment matrices for the polynomial coordinate
S = 1/2 + i*y. The Gaussian has literal mass seven and variance one;
the second measure is multiplied by 2 + 2*y + y**2 and has mass 21.
No example is asserted to be a zeta-zero packet. No Lean is run.
"""

from pathlib import Path
import hashlib
import json
import time
import sympy as sp

OUT = Path(__file__).resolve().parent
y, S, s = sp.symbols('y S s', real=True)
I = sp.I
HALF = sp.Rational(1, 2)
started = time.monotonic()
report = {'status': 'RUNNING', 'method': 'exact SymPy rational and complex-rational arithmetic',
          'gaussian_mass': 7, 'modified_mass': 21, 'coordinate': 'S=1/2+i*y',
          'second_weight': '2+2*y+y^2=1+(y+1)^2', 'lean_run': False,
          'checks': [], 'fixtures': []}


def simp(z):
    return sp.cancel(sp.expand_complex(z))


def clean(A):
    return A.applyfunc(simp)


def check(name, truth):
    truth = bool(truth)
    report['checks'].append({'name': name, 'pass': truth})
    if not truth:
        raise AssertionError(name)


def zeq(name, A, B=None):
    if B is None:
        B = sp.zeros(*A.shape) if hasattr(A, 'shape') else 0
    diff = A - B
    if hasattr(diff, 'shape'):
        check(name, all(simp(z) == 0 for z in diff))
    else:
        check(name, simp(diff) == 0)


def positive(name, z, strict=False):
    z = simp(z)
    check(name + ': real', sp.im(z) == 0)
    check(name, z > 0 if strict else z >= 0)


def pd(name, M):
    zeq(name + ': Hermitian', M, M.H)
    for j in range(1, M.rows + 1):
        positive(name + f': leading minor {j}', M[:j, :j].det(), strict=True)


def moment(n):
    if n % 2:
        return sp.Integer(0)
    return 7 * (sp.factorial2(n - 1) if n else 1)


def integral(poly):
    return sp.expand(sum(coef * moment(monom[0])
                         for monom, coef in sp.Poly(sp.expand(poly), y).terms()))


def source(d, weight):
    z = HALF + I*y
    return sp.Matrix(d, d, lambda a, b: integral((HALF-I*y)**a * z**b * weight))


def inclusion(d, N):
    return sp.eye(d)[:, :N+1]


def relation(d, N, chi, q):
    if N == q-1:
        return sp.zeros(d, 0)
    return sp.Matrix(d, N-q+1,
                     lambda a, b: sp.Poly(sp.expand(chi*S**b), S).nth(a))


def data(M, N, chi, q):
    d = M.rows
    Inc = inclusion(d, N)
    B = relation(d, N, chi, q)
    C = sp.eye(d)[:, :q]
    P = clean(Inc*(Inc.H*M*Inc).inv()*Inc.H*M)
    if B.cols == 0:
        K = sp.zeros(0, q)
        Q = sp.zeros(d)
        R = C
    else:
        H = clean(B.H*M*B)
        K = clean(H.inv()*B.H*M*C)
        Q = clean(B*H.inv()*B.H*M)
        R = clean(C-B*K)
    G = clean(R.H*M*R)
    Pi = clean(R*G.inv()*R.H*M)
    return {'B': B, 'C': C, 'R': R, 'G': G, 'P': P, 'Q': Q, 'Pi': Pi, 'K': K}


def quotient_remainder_matrix(d, chi, q):
    return sp.Matrix(q, d,
                     lambda a, b: sp.Poly(sp.rem(S**b, chi, S), S).nth(a))


fixtures = [('linear', 1, S-HALF),
            ('double_primary', 2, (S-HALF)**2),
            ('two_distinct_roots', 2, 1+(S-HALF)**2)]

for fixture_name, q, chi in fixtures:
    prefix = fixture_name
    d = 2*q+1
    M0 = source(d, 1)
    M1 = source(d, 2+2*y+y**2)
    dotM = M1-M0
    relative = clean(M0.inv()*M1)
    spectral_K = simp(sp.trace((relative-sp.eye(d))**2))
    uniform_theta = sp.Rational(99, 101)
    check(prefix + ': endpoints noncommuting', M0*M1 != M1*M0)
    pd(prefix + ': M0 positive', M0)
    pd(prefix + ': M1 positive', M1)
    a, b = sp.Integer(1), sp.Integer(100)
    pd(prefix + ': source lower enclosure M1-M0', M1-a*M0)
    pd(prefix + ': source upper enclosure 100*M0-M1', b*M0-M1)
    endpoints = (q-1, q, 2*q-1, 2*q)
    unique_N = sorted(set(endpoints))
    at0 = {N: data(M0, N, chi, q) for N in unique_N}
    at1 = {N: data(M1, N, chi, q) for N in unique_N}
    rem = quotient_remainder_matrix(d, chi, q)
    boundary_nonzero = 0
    for N in unique_N:
        D0, D1 = at0[N], at1[N]
        R0, R1 = D0['R'], D1['R']
        delta = R1-R0
        zeq(f'{prefix} N={N}: relation primitive', delta, D0['B']*(D0['K']-D1['K']))
        zeq(f'{prefix} N={N}: lower signed identity',
            D1['G']-a*D0['G'], R1.H*(M1-a*M0)*R1+a*delta.H*M0*delta)
        zeq(f'{prefix} N={N}: upper signed identity',
            b*D0['G']-D1['G'], R0.H*(b*M0-M1)*R0+delta.H*M1*delta)
        if N == q-1:
            check(f'{prefix}: first relation has zero columns', D0['B'].shape == (d, 0))
            zeq(f'{prefix}: first delta zero', delta)
        elif delta != sp.zeros(d, q):
            boundary_nonzero += 1
            check(f'{prefix} N={N}: reversing lower boundary sign fails',
                  clean(2*a*delta.H*M0*delta) != sp.zeros(q))
            check(f'{prefix} N={N}: reversing upper boundary sign fails',
                  clean(2*delta.H*M1*delta) != sp.zeros(q))
        pd(f'{prefix} N={N}: lower quotient enclosure', D1['G']-a*D0['G'])
        pd(f'{prefix} N={N}: upper quotient enclosure', b*D0['G']-D1['G'])
        scaled = data(11*M1, N, chi, q)
        zeq(f'{prefix} N={N}: scalar preserves canonical section', scaled['R'], R1)
        zeq(f'{prefix} N={N}: scalar scales quotient Gram literally', scaled['G'], 11*D1['G'])
    check(prefix + ': nonzero boundary corrections tested', boundary_nonzero > 0)
    sample_rows = []
    for x in (0, sp.Rational(1, 3), sp.Rational(1, 2), 1):
        tag = f'{prefix} s={x}'
        M = M0+x*dotM
        X = clean(M.inv()*dotM)
        all_data = {N: data(M, N, chi, q) for N in unique_N}
        for N, D in all_data.items():
            rho, G, Pi = D['R'], D['G'], D['Pi']
            zeq(tag+f' N={N}: original quotient map', rem*rho, sp.eye(q))
            zeq(tag+f' N={N}: canonical orthogonality', D['B'].H*M*rho)
            zeq(tag+f' N={N}: Pi equals P-Q', Pi, D['P']-D['Q'])
            zeq(tag+f' N={N}: Pi idempotent', Pi*Pi, Pi)
            zeq(tag+f' N={N}: weighted selfadjoint', Pi.H*M, M*Pi)
            zeq(tag+f' N={N}: Pi trace', sp.trace(Pi), q)
            for j in unique_N:
                if j < N:
                    continue
                Dj = all_data[j]
                T = clean(G.inv()*Dj['G'])
                zeq(tag+f' pair {N},{j}: cross Gram', Dj['R'].H*M*rho, Dj['G'])
                zeq(tag+f' pair {N},{j}: projector overlap', sp.trace(Pi*Dj['Pi']), sp.trace(T))
                zeq(tag+f' pair {N},{j}: restriction loss',
                    sp.trace((Pi-Dj['Pi'])**2), 2*sp.trace(sp.eye(q)-T))
        Pi = {N: D['Pi'] for N, D in all_data.items()}
        P = {N: D['P'] for N, D in all_data.items()}
        Qrel = {N: D['Q'] for N, D in all_data.items()}
        Q0 = Pi[q-1]-Pi[2*q-1]
        Q1 = Pi[q]-Pi[2*q]
        signed = Q0+Q1
        SP_R = Qrel[2*q-1]+Qrel[2*q]-Qrel[q]
        SP_P = P[2*q-1]-P[q-1]+P[2*q]-P[q]
        zeq(tag+': exact SP orientation', signed, SP_R-SP_P)
        zeq(tag+': trace zero', sp.trace(signed), 0)
        G = {N: D['G'] for N, D in all_data.items()}
        loss0 = simp(sp.trace(sp.eye(q)-G[q-1].inv()*G[2*q-1]))
        loss1 = simp(sp.trace(sp.eye(q)-G[q].inv()*G[2*q]))
        normQ = simp(sp.trace(signed**2))
        zeq(tag+': exact retained cross term', normQ,
            2*loss0+2*loss1+2*sp.trace(Q0*Q1))
        positive(tag+': restriction losses nonnegative', loss0)
        positive(tag+': second restriction loss nonnegative', loss1)
        positive(tag+': HS coarser loss bound', 4*(loss0+loss1)-normQ)
        center = simp(sp.trace(X)/d)
        Xc = X-center*sp.eye(d)
        variance = simp(sp.trace(X**2)-sp.trace(X)**2/d)
        derivative = simp(sp.trace(X*signed))
        zeq(tag+': centered trace identity', derivative, sp.trace(Xc*signed))
        positive(tag+': centered variance', variance)
        positive(tag+': centered HS squared bound', variance*normQ-derivative**2)
        # A literal, metric-selfadjoint retained approximation, with a nonzero
        # original-coordinate residual. It is not an asserted zeta model.
        K = sp.diag(*[sp.Integer((-1)**r*(r+1)) for r in range(d)])
        Y = clean(Xc/2+M.inv()*K/11)
        E = clean(Xc-Y)
        zeq(tag+': Y weighted selfadjoint', Y.H*M, M*Y)
        zeq(tag+': E weighted selfadjoint', E.H*M, M*E)
        central = simp(sp.trace(Y*signed))
        residual_sq = simp(sp.trace(E**2)*normQ)
        positive(tag+': signed residual two-sided enclosure squared',
                 residual_sq-(derivative-central)**2)
        positive(tag+': residual radius nonnegative', residual_sq)
        # Spectral-polynomial signed certificate. These original fixtures have
        # I <= M0^{-1}M1 <= 100I in the M0 metric, as certified above.
        # We use these rational enclosing endpoints (not replaced source
        # matrices) to choose the midpoint. This proves a slightly coarser
        # certificate while avoiding numerical algebraic eigenvalues.
        Bx = sp.eye(d)+x*(relative-sp.eye(d))
        midpoint = 1+sp.Rational(99, 2)*x
        H = clean(sp.eye(d)-Bx/midpoint)
        local_theta = sp.Rational(99)*x/(2+99*x)
        zeq(tag+': relative pencil factorization', M, M0*Bx)
        zeq(tag+': relative derivative formula', X, Bx.inv()*(relative-sp.eye(d)))
        positive(tag+': local contraction bounded uniformly', uniform_theta-local_theta)
        pd(tag+': contraction lower matrix bound',
           M*(sp.eye(d)*(local_theta+1)-H))
        # Verify semidefinite contractions directly by all principal minors
        # where x=0 gives an exact zero endpoint; x>0 the source enclosure is
        # strict in this fixture and Sylvester suffices.
        if x == 0:
            zeq(tag+': x=0 contraction is zero', H)
        else:
            pd(tag+': local contraction upper', M*(local_theta*sp.eye(d)-H))
            pd(tag+': local contraction lower', M*(local_theta*sp.eye(d)+H))
        for L in (0, 1, 2):
            polynomial = clean(sum((H**r for r in range(L+1)), sp.zeros(d))
                               *(relative-sp.eye(d))/midpoint)
            Rtail = clean(X-polynomial)
            zeq(tag+f' L={L}: exact Neumann residual', Rtail, H**(L+1)*X)
            Ycert = polynomial-sp.trace(polynomial)*sp.eye(d)/d
            Ecert = Rtail-sp.trace(Rtail)*sp.eye(d)/d
            zeq(tag+f' L={L}: centered residual decomposition', Xc, Ycert+Ecert)
            zeq(tag+f' L={L}: approximant weighted selfadjoint', polynomial.H*M, M*polynomial)
            res_variance = simp(sp.trace(Ecert**2))
            zeq(tag+f' L={L}: exact residual variance', res_variance,
                sp.trace(Rtail**2)-sp.trace(Rtail)**2/d)
            positive(tag+f' L={L}: pointwise uniform residual bound',
                     uniform_theta**(2*(L+1))*spectral_K-res_variance)
            certificate_center = simp(sp.trace(Ycert*signed))
            positive(tag+f' L={L}: signed certificate enclosure squared',
                     res_variance*normQ-(derivative-certificate_center)**2)
            positive(tag+f' L={L}: uniform signed certificate squared',
                     uniform_theta**(2*(L+1))*spectral_K*(8*q-6)
                     -(derivative-certificate_center)**2)
        positive(tag+': actual projector square bounded by 8q-6', 8*q-6-normQ)
        sample_rows.append({'s': str(x), 'derivative': str(derivative),
                            'sigma': str(variance), 'trace_Q_square': str(normQ),
                            'loss0': str(loss0), 'loss1': str(loss1),
                            'retained_cross_term': str(simp(sp.trace(Q0*Q1))),
                            'signed_center': str(central), 'signed_radius_squared': str(residual_sq)})
    # Separate symbolic determinant derivative on the original quotient Grams.
    Ms = M0+s*dotM
    Ds = {N: data(Ms, N, chi, q) for N in unique_N}
    determinant_ratio = sp.factor(Ds[q-1]['G'].det()*Ds[q]['G'].det()
                                  /(Ds[2*q-1]['G'].det()*Ds[2*q]['G'].det()))
    dlog = sp.cancel(sp.diff(determinant_ratio, s)/determinant_ratio)
    Qs = Ds[q-1]['Pi']+Ds[q]['Pi']-Ds[2*q-1]['Pi']-Ds[2*q]['Pi']
    trace_expression = sp.cancel(sp.trace(Ms.inv()*dotM*Qs))
    check(prefix+': full symbolic determinant derivative equals signed pairing',
          sp.cancel(dlog-trace_expression) == 0)
    report['fixtures'].append({'name': fixture_name, 'q': q, 'chi': str(sp.expand(chi)),
                               'source_dimension': d, 'endpoints': list(endpoints),
                               'source_sandwich': ['1', '100'],
                               'nonzero_boundary_degrees': boundary_nonzero,
                               'spectral_certificate': {'relative_spectrum_enclosure': ['1', '100'],
                                                        'theta_uniform': str(uniform_theta),
                                                        'K_exact': str(spectral_K),
                                                        'degrees_tested': [0, 1, 2]},
                               'determinant_ratio': str(determinant_ratio),
                               'symbolic_derivative': str(sp.factor(dlog)),
                               'samples': sample_rows})
    print(f'{fixture_name}: PASS ({len(report["checks"])} cumulative checks)', flush=True)

report['status'] = 'PASS'
report['check_count'] = len(report['checks'])
report['elapsed_seconds'] = round(time.monotonic()-started, 3)
report['source_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
report['input_sha256'] = hashlib.sha256(Path(
    'local:user-profile/.codex/attachments/0d84cbd9-4bea-48b2-8d49-3443a3ef7514/pasted-text.txt').read_bytes()).hexdigest()
(OUT/'exact_check_results.json').write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
print(json.dumps({k: report[k] for k in ('status', 'check_count', 'elapsed_seconds', 'source_sha256', 'input_sha256')}, indent=2), flush=True)
