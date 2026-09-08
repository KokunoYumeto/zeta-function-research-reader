"""Independent endpoint audit via Gelfand--Tsetlin chains, exact arithmetic only."""
from collections import Counter
from fractions import Fraction
from itertools import product
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
checks = 0

def require(statement):
    global checks
    assert statement
    checks += 1

def subshapes(shape):
    """All adjacent interlacing rows, without tableau generation."""
    return product(*(range(shape[i+1], shape[i]+1) for i in range(len(shape)-1)))

def gt_contents(shape):
    if len(shape) == 1:
        yield (shape[0],)
        return
    for lower in subshapes(shape):
        last_content = sum(shape) - sum(lower)
        for content in gt_contents(lower):
            yield content + (last_content,)

def partitions(total, cap=None, slots=4):
    if total == 0:
        yield (0,) * slots
    elif slots:
        for first in range(min(total, total if cap is None else cap), 0, -1):
            for tail in partitions(total-first, first, slots-1):
                yield (first,) + tail

def dim(shape):
    answer = Fraction(1)
    for i in range(len(shape)):
        for j in range(i+1, len(shape)):
            answer *= Fraction(shape[i]-shape[j]+j-i, j-i)
    require(answer.denominator == 1)
    return int(answer)

profiles = {}
for degree in range(9):
    for shape in partitions(degree):
        contents = list(gt_contents(shape))
        require(len(contents) == dim(shape))
        require(all(sum(v) == degree for v in contents))
        require(all(sum(v[i] for v in contents) == degree*len(contents)//4
                    for i in range(4)))
        profile = Counter(v[3] for v in contents)
        require(min(profile) == shape[3])
        require(max(profile) == shape[0])
        profiles[str(shape)] = dict(sorted(profile.items()))

shape = (7, 5, 3, 0)
contents = list(gt_contents(shape))
profile = Counter(v[3] for v in contents)
require(profile == {0: 27, 1: 81, 2: 162, 3: 270, 4: 300, 5: 252, 6: 126, 7: 42})
require(len(contents) == 1260)
require(sum(v[3] for v in contents) == 4725)
require(sum(m for k, m in profile.items() if k % 2 == 0) == 615)
require(sum(m for k, m in profile.items() if k % 2 == 1) == 645)
require(sum((-1)**k*m for k, m in profile.items()) == -30)

# Nonuniform sorted weights independently exercise the nested column extrema.
nested_checks = []
for weights in ((0, 0, 1, 2), (0, 1, 1, 3), (2, 2, 4, 7), (0, 0, 0, 1)):
    for degree in range(7):
        for shape in partitions(degree):
            exponents = Counter(sum(a*b for a, b in zip(content, weights))
                                for content in gt_contents(shape))
            lower = sum(a*b for a, b in zip(shape, weights))
            upper = sum(a*b for a, b in zip(shape, reversed(weights)))
            require(min(exponents) == lower)
            require(max(exponents) == upper)
            if weights == (0, 0, 0, 1):
                require(exponents == profiles[str(shape)])
            nested_checks.append((shape, weights, lower, upper))

# Exact retained circle factorization, through x=q^2+q^-2.
x = Fraction(3, 2)
quantum3 = x + 1
quantum7 = x**3 + x**2 - 2*x - 1
r_squared = x - 2
h = quantum3*quantum7
c = r_squared*h
require(quantum3 == Fraction(5, 2))
require(quantum7 == Fraction(13, 8))
require(r_squared == Fraction(-1, 2))
require(h == Fraction(65, 16))
require(c == Fraction(-65, 32))
for k in range(16):
    require((c**k > 0) == (k % 2 == 0))
    require(c**k == r_squared**k*h**k)

inputs = [HERE.parent/'plethysm_transport.tex',
          HERE.parent/'check_plethysm_transport.py',
          HERE.parent/'basis/integral_schur_basis.tex']
receipt = {
    'status': 'pass', 'checks': checks,
    'method': 'Independent interlacing chains and exact rational circle evaluation',
    'original_profile': dict(sorted(profile.items())),
    'original_inertia': {'positive': 615, 'negative': 645, 'zero': 0, 'signature': -30},
    'nested_extreme_cases': len(nested_checks),
    'single_shape_cases': len(profiles),
    'inputs': [{'path': str(p.relative_to(HERE.parent)),
                'sha256': hashlib.sha256(p.read_bytes()).hexdigest()} for p in inputs],
}
(HERE/'independent_verification.json').write_text(json.dumps(receipt, indent=2)+'\n', encoding='utf-8')
print(json.dumps(receipt))
