"""Exact local audit of (104), (105); no external dependencies or source edits."""
from fractions import Fraction as F
from itertools import permutations, product
from pathlib import Path
import argparse
import hashlib
import json

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT.parent/'source'/'FABEL_TENSOR_TRANSFER.md'
ORIGINAL_SOURCE = Path('[local]/Documents/math/agent_work/ym_quantum_coarse_graining_astra_20260908/FABEL_TENSOR_TRANSFER.md')
EXPECTED_SHA = 'c0bdfe683d3f620858a74654406e30c02b3242d0b6cfb012432cac173d98d9fc'
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--observe-source', action='store_true', help='Also compare the optional original source with the pinned local snapshot.')
args = parser.parse_args()
source_sha = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
assert source_sha == EXPECTED_SHA, 'Local source snapshot changed; re-audit before refreshing receipt.'
observation = None
if args.observe_source:
    original_sha = hashlib.sha256(ORIGINAL_SOURCE.read_bytes()).hexdigest()
    assert original_sha == source_sha, 'Original source differs from the audited local snapshot.'
    observation = {
        'status': 'PASS',
        'original_source': str(ORIGINAL_SOURCE),
        'original_source_sha256': original_sha,
        'snapshot': '../source/FABEL_TENSOR_TRANSFER.md',
        'snapshot_sha256': source_sha,
        'byte_identical': ORIGINAL_SOURCE.read_bytes() == SOURCE.read_bytes(),
    }
    assert observation['byte_identical']
count = 0

def check(value):
    global count
    assert value
    count += 1

def weights(x):
    t = sum(x[:3])
    return (t*t/F(9), sum((a-t/F(3))**2 for a in x[:3])/F(2), sum(a*a for a in x[3:]))

def gram(x, d, h, c):
    return d*sum(a*a for a in x[:3]) + 2*h*sum(x[i]*x[j] for i in range(3) for j in range(i+1,3)) + c*sum(a*a for a in x[3:])

def rhs(x, d, h, c):
    w0, wd, wo = weights(x)
    return w0*(3*d+6*h)+wd*(2*d-2*h)+wo*c

basis = [tuple(F(i == j) for i in range(6)) for j in range(6)]
parameters = ((1,0,0),(0,1,0),(0,0,1))
for param in parameters:
    # Evaluations at e_i and e_i+e_j determine every quadratic coefficient.
    for i in range(6):
        for j in range(i,6):
            x = basis[i] if i == j else tuple(a+b for a,b in zip(basis[i],basis[j]))
            check(gram(x,*param) == rhs(x,*param))

pairs = [(0,0),(1,1),(2,2),(0,1),(0,2),(1,2)]
for perm in permutations(range(3)):
    for signs in product((-1,1),repeat=3):
        # R e_i = signs[i] e_perm[i]; action is S -> R S R^T.
        image = []
        factor = []
        for i,j in pairs:
            image.append(pairs.index(tuple(sorted((perm[i],perm[j])))))
            factor.append(signs[i]*signs[j])
        for param in parameters:
            for i in range(6):
                for j in range(i,6):
                    x = basis[i] if i == j else tuple(a+b for a,b in zip(basis[i],basis[j]))
                    y = [F(0)]*6
                    for k in range(6):
                        y[image[k]] = factor[k]*x[k]
                    check(gram(x,*param) == gram(y,*param))

endpoint = tuple(F(a,64) for a in (4,9,324,6,-36,-54))
expected = (F(113569,36864), F(100825,12288), F(531,512))
for actual, value in zip(weights(endpoint),expected):
    check(actual == value)
    check(actual > 0)
for seed, expected_seed in (
    ((1,1,1,0,0,0),(1,0,0)),
    ((1,-1,0,0,0,0),(0,1,0)),
    ((0,0,0,1,0,0),(0,0,1)),
):
    check(weights(tuple(F(x) for x in seed)) == expected_seed)

receipt = {
    'status': 'PASS',
    'scope': ['(104) cubic invariant Hermitian Gram identity', '(105) three constants and scaling exponent from the supplied endpoint matrix'],
    'source': '../source/FABEL_TENSOR_TRANSFER.md',
    'source_sha256': source_sha,
    'checks': count,
    'group_elements': 48,
    'gram_parameter_matrices': 3,
    'endpoint_weights': [str(x) for x in expected],
    'review_sha256': hashlib.sha256((ROOT/'REVIEW.md').read_bytes()).hexdigest(),
    'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'findings': [],
}
(ROOT/'receipt.json').write_text(json.dumps(receipt, indent=2)+'\n', encoding='utf-8')
if observation is not None:
    observation['checker_sha256'] = receipt['checker_sha256']
    observation['review_sha256'] = receipt['review_sha256']
    (ROOT/'source_observation.json').write_text(json.dumps(observation, indent=2)+'\n', encoding='utf-8')
print(json.dumps(receipt, indent=2))
if observation is not None:
    print(json.dumps(observation, indent=2))
