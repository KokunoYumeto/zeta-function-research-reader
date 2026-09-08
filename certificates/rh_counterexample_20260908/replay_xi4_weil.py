"""Independent read-only replay; exact antiderivatives replace prime quadrature.

The saved frequency-side gamma quadrature remains a trusted Arb integration.
This replay reconstructs its sum and infinite-tail bound, independently derives
all compact prime correlations, and uses LDL instead of production determinants.
"""
import os
for key in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
from resource_ceiling import install_memory_ceiling
RESOURCE = install_memory_ceiling()
from pathlib import Path
from fractions import Fraction as F
import hashlib, json, math, re
from flint import arb, acb, ctx

HERE = Path(__file__).resolve().parent
FREQUENCIES = [F(2), F(-1), F(-1), -F(5, 2), -F(9, 2)]
DEGREES = [0, 0, 1, 0, 0]
COEFFICIENTS = [F(0), -F(59, 275184), F(1, 336), F(1, 1296), F(3, 132496)]

def ball(q):
    q = F(q)
    return arb(q.numerator) / q.denominator

def complex_ball(text):
    if not text.endswith('j'): return acb(arb(text))
    match = re.fullmatch(r'(.*?) ([+-]) (.*?)j', text)
    assert match, text
    imaginary = arb(match[3])
    return acb(arb(match[1]), imaginary if match[2] == '+' else -imaginary)

def poly_add(p, q):
    out = [acb(0) for _ in range(max(len(p), len(q)))]
    for j, c in enumerate(p): out[j] += c
    for j, c in enumerate(q): out[j] += c
    return out

def poly_mul(p, q):
    out = [acb(0) for _ in range(len(p) + len(q) - 1)]
    for j, a in enumerate(p):
        for k, b in enumerate(q): out[j+k] += a*b
    return out

def eval_poly(p, x):
    out = acb(0)
    for c in reversed(p): out = out*x+c
    return out

def spline_coefficients(shift, sign, cell):
    # Sum the exact truncated powers on this single cubic cell.
    out = [acb(0)] * 4
    for k in range(cell + 3):
        a = shift+2-k
        c = ball(F((-1)**k * math.comb(4, k), 6))
        out = poly_add(out, [c*math.comb(3, j)*a**(3-j)*sign**j
                             for j in range(4)])
    return out

def integrate_exp_polynomial(p, frequency, left, right):
    if frequency == 0:
        anti = [acb(0)] + [c/(j+1) for j, c in enumerate(p)]
        return eval_poly(anti, right)-eval_poly(anti, left)
    a = acb(0, ball(frequency))
    derivative = p[:]
    anti = [acb(0)]
    for r in range(len(p)):
        anti = poly_add(anti, [(-1)**r*c/a**(r+1) for c in derivative])
        derivative = [(j+1)*c for j, c in enumerate(derivative[1:])]
    return (a*right).exp()*eval_poly(anti, right)-(a*left).exp()*eval_poly(anti, left)

def exact_correlation(x, i, j):
    points = [x-2, arb(2)]
    for k in range(-2, 3):
        for q in (arb(k), x-k):
            if q > points[0] and q < points[1]: points.append(q)
    points.sort(key=lambda q: float(q.mid()))
    knots = []
    for q in points:
        if knots and q == knots[-1]: continue
        if knots: assert q > knots[-1]
        knots.append(q)
    total = acb(0)
    for left, right in zip(knots, knots[1:]):
        mid = (left+right)/2
        cj = math.floor(float(mid))
        ci = math.floor(float(x-mid))
        assert cj < mid and mid < cj+1
        assert ci < x-mid and x-mid < ci+1
        p = poly_mul(spline_coefficients(arb(0), 1, cj),
                     spline_coefficients(x, -1, ci))
        if DEGREES[j]: p = poly_mul(p, [acb(0), acb(0, 1)])
        if DEGREES[i]: p = poly_mul(p, [acb(0, x), acb(0, -1)])
        total += integrate_exp_polynomial(p, FREQUENCIES[j]-FREQUENCIES[i], left, right)
    return (acb(0, ball(FREQUENCIES[i]))*x).exp()*total

def fourier(z, i):
    q = z-ball(FREQUENCIES[i])
    if not DEGREES[i]: return (q/2).sinc()**4
    # Independent elementary derivative; this replay only calls at q != 0.
    assert not q.contains(0)
    return -32*(q/2).sin()**3*(q/2).cos()/q**4+64*(q/2).sin()**4/q**5

def expected_prime_powers():
    cutoff = arb(4).exp()
    assert cutoff > 54 and cutoff < 55
    rows = []
    for p in range(2, 55):
        if any(p % q == 0 for q in range(2, math.isqrt(p)+1)): continue
        n, r = p, 1
        while n < 55:
            assert arb(n).log() < 4
            rows.append([n, p, r])
            n, r = n*p, r+1
    return sorted(rows)

def run():
    ctx.prec = 384
    ctx.threads = 1
    receipt_path = HERE/'xi4_weil_results.json'
    before = hashlib.sha256(receipt_path.read_bytes()).hexdigest()
    rec = json.loads(receipt_path.read_text(encoding='utf-8'))
    for name, expected in rec['source_hashes'].items():
        assert hashlib.sha256((HERE/name).read_bytes()).hexdigest() == expected, name
    assert rec['status'] == 'pass' and not rec['zero_ordinates_used']
    assert rec['resource']['status'] == 'enforced_windows_job'
    assert rec['resource']['ceiling_bytes'] == 5_000_000_000
    assert rec['parameters']['source_coefficients'] == [str(c) for c in COEFFICIENTS]
    assert rec['parameters']['channels'] == [
        {'frequency': str(s), 'degree_iu': d} for s, d in zip(FREQUENCIES, DEGREES)]
    c0, c1, c2 = COEFFICIENTS[1], COEFFICIENTS[3], COEFFICIENTS[4]
    assert c0+c1+c2 == F(127, 219024)
    assert 3*c0-F(1,336)+F(9,2)*c1+F(13,2)*c2 == 0
    assert c0+F(23,32)*c1-F(17,32)*c2 == F(575,1752192)
    assert F(1,672)-(abs(c0)+c1+c2) == F(10291,21464352) > F(575,1752192)
    powers = expected_prime_powers()
    assert powers == sorted(rec['prime_powers'])
    assert len(rec['entries']) == 15
    matrix = [[arb(0) for _ in range(5)] for _ in range(5)]
    reconstructed = [[arb(0) for _ in range(5)] for _ in range(5)]
    prime_checks = 0
    for row in rec['entries']:
        i, j = row['i'], row['j']
        assert 0 <= i <= j < 5
        pole = 2*(fourier(acb(0, arb(1)/2), i)*fourier(acb(0, arb(1)/2), j)).real
        assert pole.overlaps(arb(row['pole']))
        segments = row['gamma']['segments']
        assert len(segments) == 192
        central = sum((arb(x) for x in segments), arb(0))
        assert central.overlaps(arb(row['gamma']['central']))
        # Integrate (x-A)^-8 and (x-T)(x-A)^-8 explicitly on x>=T.
        ell = ball(F(183,2))
        a = (arb.const_euler()+8+arb.pi().log()+arb(193).log())/(7*ell**7)
        b = (1/(6*ell**6)-ell/(7*ell**7))/ball(F(193,2))
        constants = [arb(16), arb(16), 32+64/ell, arb(16), arb(16)]
        tail = constants[i]*constants[j]*(a+b)/arb.pi()
        assert tail > 0 and tail.overlaps(arb(row['gamma']['tail_absolute_bound']))
        gamma = central+arb(0, tail.upper())
        prime = arb(0)
        assert sorted([[p['n'], p['p'], p['r']] for p in row['prime_terms']]) == powers
        for term in row['prime_terms']:
            n, p = term['n'], term['p']
            correlation = exact_correlation(arb(n).log(), i, j)
            assert correlation.overlaps(complex_ball(term['correlation'])), (i, j, n)
            prime += 2*arb(p).log()/arb(n).sqrt()*correlation.real
            prime_checks += 1
        assert prime.overlaps(arb(row['prime']))
        value = pole+gamma-prime
        saved = arb(row['value'])
        assert value.overlaps(saved)
        # Arb == asks whether both intervals are the same exact point.
        # Here identity of the serialized enclosing intervals is intended.
        assert row['value'] == rec['matrix'][i][j] == rec['matrix'][j][i]
        matrix[i][j] = matrix[j][i] = saved
        reconstructed[i][j] = reconstructed[j][i] = value
    def ldl(g):
        lower = [[arb(int(i == j)) for j in range(5)] for i in range(5)]
        pivots = []
        for i in range(5):
            d = g[i][i]-sum((lower[i][k]**2*pivots[k] for k in range(i)), arb(0))
            assert d > 0, (i, d)
            pivots.append(d)
            for j in range(i+1, 5):
                lower[j][i] = (g[j][i]-sum((lower[j][k]*lower[i][k]*pivots[k]
                                           for k in range(i)), arb(0)))/d
        return pivots
    pivots = ldl(matrix)
    fresh_pivots = ldl(reconstructed)
    value = sum((ball(COEFFICIENTS[i])*matrix[i][j]*ball(COEFFICIENTS[j])
                 for i in range(5) for j in range(5)), arb(0))
    cross = sum((matrix[0][j]*ball(COEFFICIENTS[j]) for j in range(5)), arb(0))
    minimum = value-cross**2/matrix[0][0]
    assert value > 0 and minimum > 0
    assert value.overlaps(arb(rec['source_multiplier_Weil_value']))
    assert cross.overlaps(arb(rec['original_source_cross_term']))
    assert minimum.overlaps(arb(rec['source_after_optimal_seed_subtraction']))
    assert value > ball(F(663,10**16)) and value < ball(F(677,10**16))
    assert minimum > ball(F(470,10**16)) and minimum < ball(F(490,10**16)), str(minimum)
    old = json.loads((HERE/'endpoint_weil_results.json').read_text(encoding='utf-8'))
    assert matrix[0][0].overlaps(arb(old['entries'][0]['real']))
    assert before == hashlib.sha256(receipt_path.read_bytes()).hexdigest()
    return {'status': 'pass', 'source_receipt_sha256': before,
            'independent_exact_prime_antiderivatives': prime_checks,
            'reconstructed_matrix_entries': 15, 'independent_LDL_pivots': [str(x) for x in pivots],
            'reconstructed_LDL_pivots': [str(x) for x in fresh_pivots],
            'source_Weil_value': str(value), 'optimal_seed_subtraction': str(minimum),
            'source_receipt_unchanged': True, 'resource': RESOURCE,
            'trust_boundary': 'Exact elementary prime antiderivatives and independent arithmetic replay; saved Arb gamma quadrature with full tail bound',
            'RH_counterexample': False}

if __name__ == '__main__':
    print(json.dumps(run()))
