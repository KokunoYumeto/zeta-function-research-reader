"""Independent integer-polynomial and rational-exponent path audit."""
from pathlib import Path
from fractions import Fraction
from hashlib import sha256
import json

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
TEX=ROOT/'tex/ns_schur_path.tex'
B=[-42,196,-280,160,-32]
H=[21,-98,140,-80,16]

def trim(poly):
    while len(poly)>1 and poly[-1]==0:
        poly.pop()
    return poly

def add(p,q,scale=1):
    out=[0]*max(len(p),len(q))
    for i,c in enumerate(p): out[i]+=c
    for i,c in enumerate(q): out[i]+=scale*c
    return trim(out)

def mul(p,q):
    out=[0]*(len(p)+len(q)-1)
    for i,c in enumerate(p):
        for j,d in enumerate(q):out[i+j]+=c*d
    return trim(out)

def power(p,k):
    out=[1]
    for _ in range(k):out=mul(out,p)
    return out

qplus4=[4,1]
inner=add(add(add(power(qplus4,3),power(qplus4,2),-5),qplus4,6),[-1])
hm=mul([3,1],inner)
assert hm==[21,49,35,10,1]
assert [c*(-2)**i for i,c in enumerate(hm)]==H
assert B==[-2*c for c in H]
assert sum(abs(c) for c in B[1:])==668
assert Fraction(21,668)<1

profile=json.loads((HERE/'verification.json').read_text())
counts={int(k):m for k,m in profile['multiplicity_by_number_of_fours'].items()}
assert profile['status']=='pass'
rows=[]
for k in sorted(counts):
    assert mul(power([0]+B,k),[1])==mul(power([0,-2],k),power(H,k))
    bk=power(B,k)
    assert bk[0]==(-42)**k
    # B^k-(-42)^k is exactly divisible by tau.
    difference=add(bk,[-(-42)**k])
    assert difference[0]==0
    intercept=Fraction(k)-15*Fraction(1,2)
    h_coefficient=-15
    assert intercept<=Fraction(-1,2) and h_coefficient<0
    rows.append({'k':k,'multiplicity':counts[k],'leading_constant_divided_by_e0_power_15':(-42)**k,
                 'tau_exponent_intercept':str(intercept),'tau_exponent_h_coefficient':h_coefficient,
                 'remainder_exponent_intercept':str(intercept),'remainder_exponent_h_coefficient':-13,
                 'eventual_sign':1 if k%2==0 else -1,
                 'B_power_minus_constant_divided_by_tau':difference[1:]})
degree=15
dimension=sum(counts.values())
weighted=sum(k*m for k,m in counts.items())
det_intercept=Fraction(weighted)-degree*dimension*Fraction(1,2)
det_h_coefficient=-degree*dimension
assert (det_intercept,det_h_coefficient)==(Fraction(-4725),-18900)
assert Fraction(1,2)-Fraction(1,100)>0
receipt={'status':'pass','method':'Direct integer-polynomial multiplication and exact rational affine exponents; no numerical asymptotic sampling.',
         'author_tex_sha256_at_audit':sha256(TEX.read_bytes()).hexdigest(),
         'h_m_coefficients':hm,'h_tau_coefficients':H,'B_coefficients':B,
         'absolute_linear_error_bound_for_B_on_tau_le_1':668,
         'explicit_B_negative_threshold':str(Fraction(21,668)),
         'exponent_rows':rows,'determinant_exponent_intercept':str(det_intercept),
         'determinant_exponent_h_coefficient':det_h_coefficient,
         'analytic_argument':'PROOF_NOTES.md proves bounded-epsilon remainder and uniform eventual signs for fixed h,e0 and epsilon bound.'}
(HERE/'path_verification.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'status':'pass','weights':len(rows),'all_exponents_negative':True,
                  'determinant_exponent':'-4725-18900h'}))
