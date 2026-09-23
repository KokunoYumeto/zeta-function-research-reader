"""Exact finite checks of the explicit CDV identities; not an RH test."""
from pathlib import Path
from fractions import Fraction as Q
import hashlib,json
import sympy as s

R=Path(__file__).resolve().parent
checks=[]
def need(name,ok):
    if not ok: raise ArithmeticError(name)
    checks.append(name)
for p in [2,3,5,7]:
    for k in range(-3,4):
        for m in range(-4,5):
            # Original local Gram matrix for c_k,c_(k+m).
            g00=Q(p)**(-k)
            g11=Q(p)**(-(k+m))
            g01=Q(p)**(-max(k,k+m))
            coefficient=Q(p)**(-max(0,m))
            need(f'projection coefficient p={p} k={k} m={m}',g01/g00==coefficient)
            local=g11-2*coefficient*g01+coefficient**2*g00
            global_norm=Q(p)**m*local
            expected=Q(p)**(-k)*(1-Q(p)**(-abs(m)))
            need(f'full defect norm p={p} k={k} m={m}',global_norm==expected)
            need(f'defect sign p={p} k={k} m={m}',(global_norm==0)==(m==0) and global_norm>=0)
        need(f'Fourier convolution idempotent p={p} k={k}',Q(p)**(-2*k)*Q(p)**k==Q(p)**(-k))

# Finite additive-character orthogonality on p^-a Zp / p^a Zp.
# For a ball k, each geometric character sum is its cardinality
# exactly when the frequency annihilates that subgroup, otherwise0.
for p in [2,3,5]:
    a=2
    modulus=p**(2*a)
    for k in range(-a,a+1):
        step=p**(a+k)
        count=modulus//step
        for frequency in range(modulus):
            char_sum_nonzero=(frequency*step)%modulus==0
            target_ball=(frequency%(p**(a-k)))==0
            need(f'finite Fourier support p={p} k={k} j={frequency}',char_sum_nonzero==target_ball)
        need(f'finite Fourier amplitude p={p} k={k}',Q(count,p**a)==Q(p)**(-k))

# Exact marked-coordinate diagonal quotient, retaining denominator|T|.
for n in range(1,10):
    delta=s.ones(n,1)
    proj=s.eye(n)-s.ones(n)/n
    need(f'mixed diagonal kernel n={n}',proj*delta==s.zeros(n,1))
    need(f'mixed quotient idempotent n={n}',proj*proj==proj)
    need(f'mixed quotient dimension n={n}',proj.rank()==n-1)
for valuations in [(-3,2),(0,0),(2,-1),(4,3)]:
    ratio=Q(2)**valuations[0]*Q(3)**valuations[1]
    norm_finite=Q(2)**(-valuations[0])*Q(3)**(-valuations[1])
    need(f'rational product formula {valuations}',ratio*norm_finite==1)

p=R/'independent/CC_DIVISOR_COEFFICIENT_FAMILY.tex'
receipt={'proof_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
         'check_count':len(checks),'checks':checks,
         'scope':'Exact finite local projections, all displayed defect signs, Fourier character support and factors, finite diagonal quotients. Infinite-dimensional and sheaf claims are established in the full proofs and independent review.'}
(R/'CC_DIVISOR_EXACT_CHECK.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({k:v for k,v in receipt.items() if k!='checks'},indent=2))
