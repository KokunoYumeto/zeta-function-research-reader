from pathlib import Path
from decimal import Decimal,localcontext,ROUND_FLOOR,ROUND_CEILING
from flint import fmpq as Q
import json
p=Path(__file__).parent
r=json.loads((p/'EXACT_CALIBRATION.json').read_text())
def decimal_outward(v,up=False,places=35):
    a=Q(v)
    with localcontext() as c:
        c.prec=120;c.rounding=ROUND_CEILING if up else ROUND_FLOOR
        x=Decimal(int(a.numerator))/Decimal(int(a.denominator))
        return str(x.quantize(Decimal(1).scaleb(-places)))
def interval(data):return '['+decimal_outward(data['lower'])+', '+decimal_outward(data['upper'],True)+']'
rows=[]
for N,v in r['endpoints'].items():
    lb=r['log_bounds']['endpoints'][N]
    rows.append(f"| {N} | {float(Q(v['X'])):.12g} | {float(Q(v['one_minus_Y'])):.12g} | {interval(lb['log_factor'])} |")
text='''# Complete degree-36 rational calibration

This is the parameter calibration k=5, l=1, m=1, q=36, delta=1/4, gamma=3. These numbers are not asserted to be zeta-zero coordinates. Every original quartet-sum factor is present. The four original cutoffs are 35,36,71,72 with signs +,+,−,−.

All X and Y values, their positive Schur gaps, the complete centered packet polynomial, original relation determinants and outward rational logarithm bounds are saved in `EXACT_CALIBRATION.json`. The execution took '''+str(r['elapsed_seconds'])+''' seconds, excluding report writing; the stages are recorded in `execution.log`. Four full 36-by-36 determinant updates, four independent original relation-Gram returns and four independent full-source Gram products passed. The free A formula passed at all 74 degrees from 0 through 73. The initial array-length guard caught an off-by-one construction bound before any calibration was run; that guard log is preserved and the corrected complete run is the reported one.

The X and gap columns below are approximate displays of the saved exact rationals. Each logarithm interval is a certified outward decimal enlargement of the saved rational enclosure.

| N | X_N (display) | 1−Y_N (display) | log((1+X_N)(1−Y_N)), certified enclosure |
|---|---:|---:|---|
'''+ '\n'.join(rows)+'''

The complete signed Schur logarithm R^0−R^sigma lies in

'''+interval(r['log_bounds']['signed_schur_return_log'])+'''.

The saved rational interval has width '''+str(float(Q(r['log_bounds']['signed_schur_return_log']['width'])))+'''. The separately retained free-boundary signed logarithm lies in

'''+interval(r['log_bounds']['free_boundary_log'])+'''.

## Exact receiving and sign identities

At each endpoint the computation proves exactly

`(D_{1,N}/R_N) (1+X_N) (1−Y_N) = chi(1/2)^2`.

Here R_N is formed independently from the complete original relation columns chi*x^j, including relation ranks 0,1,36,37; both empty determinants at the first endpoint are one. The translation from chi*S^j to chi*x^j is the full binomial triangular matrix with determinant one, so its determinant ratio is unchanged. The source product D_{1,N}=product_{n=0}^N(n+1/2)(n+3/2) is also independently recovered by determinants of the complete original f-Gram parity blocks. Their diagonal entries are d_{n+1}+(1/4)d_n+a_n^2 d_{n-1}, off-diagonal entries at distance two are −d_{n+2}, and a_n=n(n−1/2). These follow directly from f*p_n=p_{n+1}−a_n*p_{n−1}−p_n/2 in the original orthogonal polynomial frame.

Consequently the four-signed Schur product is exactly reciprocal to GSR's signed source/relation product. NOTE computes R^0−R^sigma; GSR computes the opposite signed object T_k. No sign convention is silently changed.

The actual mass is retained as K=c_sigma^−1 Khat, C=c_sigma^−1 Chat, A=c_sigma^−1 Ahat and omega_n=c_sigma*d_n, where c_sigma=sqrt(2*pi). The c_sigma factors cancel in each paired X and Y expression. No source probability measure is substituted. Positive d_n and the first 36 monic remainder columns prove Khat positive definite; the exact positive values of 1−Y prove the positive joint Schur complements.

## Rigorous logarithm evaluation

For each positive exact rational r, choose the exact integer e so that r=2^e*s and 1<=s<2. Bound s outward by consecutive dyadic rationals of denominator 2^128. For either endpoint use t=(s−1)/(s+1), so 0<=t<=1/3. The first 96 terms of `2*sum_{j>=0} t^(2j+1)/(2j+1)` give the lower logarithm bound. The remaining positive tail is at most `2*t^193/(193*(1−t^2))`, giving the upper bound. Apply the same enclosure to log(2), multiply by e with the appropriate direction when e<0, and add. Every step uses exact rational arithmetic. This gives the saved finite bounds even for the small original Schur gaps, without a slowly converging series directly at Y close to one.
'''
(p/'FINDINGS.md').write_text(text,encoding='utf-8')
print(interval(r['log_bounds']['signed_schur_return_log']))
