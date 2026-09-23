from pathlib import Path
from fractions import Fraction as F
from decimal import Decimal,localcontext
import json,hashlib,sys
sys.set_int_max_str_digits(100000)
p=Path(__file__).parent
source=p/'inputs/REPRODUCED_WITNESS63.json'
j=json.loads(source.read_text())
def binary(q):
    sign,man,exp,bc=q
    return F((-1 if sign else 1)*man)*F(2)**exp
def add(a,b):return a[0]+b[0],a[1]+b[1]
def mul(a,b):
    v=[x*y for x in a for y in b];return min(v),max(v)
def scale(a,k):return mul(a,(F(k),F(k)))
def point(a):return F(a),F(a)
def subtract(a,b):return a[0]-b[1],a[1]-b[0]
def encode(a):
    with localcontext() as c:
        c.prec=38
        return {'rational':[[str(x.numerator),str(x.denominator)] for x in a],
                'display':[str(Decimal(x.numerator)/Decimal(x.denominator)) for x in a]}
roots=j['results']['zero']['root_moments']
print('root_entries',len(roots),'first',roots[0]['display'][:1])
# The receipt retains the dummy S_0=0 at index zero; S_n is at index n.
S=[tuple(map(binary,roots[n]['binary'])) for n in [1,2,3]]
if not (F(1,100)<S[0][0]<S[0][1]<F(2,100)):raise ArithmeticError('S1 source index')
cutoff=400
T=[]
for n in [1,2,3]:
    partial=sum((F(1,(4*k+1)**(2*n)) for k in range(1,cutoff+1)),F(0))
    lower=partial+F(1,4*(2*n-1)*(4*(cutoff+1)+1)**(2*n-1))
    upper=partial+F(1,4*(2*n-1)*(4*cutoff+1)**(2*n-1))
    T.append((lower,upper))
Z=[add(S[n-1],scale(subtract(T[n-1],point(1)),(-1)**n)) for n in [1,2,3]]
QH=add(add(S[0],scale(S[1],2)),S[2])
QZ=add(add(Z[0],scale(Z[1],2)),Z[2])
QC=scale(add(add(T[0],scale(T[1],-2)),T[2]),1)
det=subtract(mul(Z[0],Z[2]),mul(Z[1],Z[1]))
if not QH[1]<F(3,250):raise ArithmeticError('full nontrivial test bound')
if not QZ[1]<0 or not det[1]<0 or not Z[0][0]>0:raise ArithmeticError('full zeta signs')
if not QC[0]>0:raise ArithmeticError('retained Gamma contribution')
if not QZ[1] < QH[1]-F(576,15625):raise ArithmeticError('first trivial zero retained')
checks={
 'status':'passed','source':source.relative_to(p).as_posix(),'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
 'original_function':'Riemann zeta at original physical time0; full signed divisor includes all trivial zeros and the pole at1',
 'original_test':'[-2i(s-1/2)]^-1 + [-2i(s-1/2)]^-3',
 'nontrivial_root_test':encode(QH),'full_zeta_divisor_test':encode(QZ),
 'root_moment_intervals':[encode(x) for x in S],
 'retained_completion_divisor_test':encode(QC),
 'full_zeta_matrix_entries':[encode(x) for x in Z],
 'full_zeta_matrix_determinant':encode(det),'full_zeta_matrix_inertia':[1,1,0],
 'trivial_series_terms':cutoff,'trivial_series_intervals':[encode(x) for x in T],
 'tail_proof':'For n=1,2,3 decreasing (4x+1)^(-2n), integrate from N+1 and N to infinity, respectively; no trivial zeros omitted.',
 'first_trivial_zero_exact_contribution':'-576/15625',
 'scope':'Negative full-zeta signed-divisor trace; the full completion contribution is also evaluated. This is not a negative value of the compensated Weil form and is not an RH counterexample.'
}
(p/'FULL_ZETA_TRACE_RECEIPT.json').write_text(json.dumps(checks,indent=2)+'\n')
print(json.dumps({k:v['display'] for k,v in checks.items() if isinstance(v,dict) and 'display' in v}))
