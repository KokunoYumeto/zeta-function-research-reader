"""Exact sparse Laurent arithmetic; retains original coefficient expressions."""
from collections import defaultdict
from pathlib import Path
import json, hashlib

ROOT=Path(__file__).resolve().parent

def add(*ps):
    out=defaultdict(int)
    for p in ps:
        for k,v in p.items(): out[k]+=v
    return {k:v for k,v in out.items() if v}
def scale(p,a): return {k:a*v for k,v in p.items() if a*v}
def mul(a,b):
    out=defaultdict(int)
    for i,x in a.items():
        for j,y in b.items(): out[i+j]+=x*y
    return {k:v for k,v in out.items() if v}
def power(a,n):
    out={0:1}
    for _ in range(n): out=mul(out,a)
    return out
def qinteger(n): return {n-1-2*j:1 for j in range(n)}
def record(p): return [{'exponent':k,'coefficient':p[k]} for k in sorted(p,reverse=True)]

C={10:1,4:-1,-4:-1,-10:1}
numerator=add(mul(qinteger(6),add(qinteger(7),scale(qinteger(3),-1))),scale(mul(qinteger(3),qinteger(8)),-1))
assert numerator==mul(qinteger(2),C), 'source divided-power expression'
assert C==mul({7:1,-7:-1},{3:1,-3:-1})
r={1:1,-1:-1}
positive=mul(qinteger(7),qinteger(3))
assert C==mul(power(r,2),positive)
assert all(v>0 for v in positive.values())
jet0=sum(C.values())
jet1=sum(k*v for k,v in C.items())
derivative2=sum(k*(k-1)*v for k,v in C.items())
assert (jet0,jet1,derivative2)==(0,0,168)
p={1:1,-1:1}
assert add(power(p,2),scale(power(r,2),-1))=={0:4}
in_p={10:1,8:-10,6:35,4:-51,2:29,0:-4}
transport={}
for n,a in in_p.items(): transport=add(transport,scale(power(p,n),a))
assert transport==C
assert add(p,{0:-2})==mul(power({1:1,0:-1},2),{-1:1})
assert sum(a*2**n for n,a in in_p.items())==0
assert sum(n*a*2**(n-1) for n,a in in_p.items() if n)==84
rec={
 'status':'PASS',
 'source':'arXiv:cs/0703110v4, Example ex not positive; n3=3,n2=2',
 'source_shape_columns':[0,3,2,2],
 'size':15,
 'coefficient_original':record(C),
 'divided_power_numerator':record(numerator),
 'retained_positive_factor':record(positive),
 'q_jet':{'value':jet0,'first_derivative':jet1,'second_derivative':derivative2,'coefficient_of_(q-1)^2':84},
 'trace_coordinate':'p=q+q^(-1)',
 'sheet_coordinate':'r_GCT=q-q^(-1)',
 'trace_polynomial':record(in_p),
 'trace_jet_at_2':{'value':0,'first_derivative':84},
 'checks':['[2]_q C equals exact source numerator','C equals two-binomial product','C equals retained (q-q^-1)^2[7][3]','double zero with second jet 84','p^2-r_GCT^2=4','trace polynomial identity','p-2=(q-1)^2/q'],
 'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
}
(ROOT/'coefficient_certificate.json').write_text(json.dumps(rec,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'PASS','checks':len(rec['checks']),'second_jet':84,'certificate':str(ROOT/'coefficient_certificate.json')}))
