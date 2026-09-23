from pathlib import Path
from fractions import Fraction as F
import json, hashlib, math, sys
sys.set_int_max_str_digits(1000000)
p=Path(__file__).parent
def sourcepath(value):
    q=Path(value)
    return q if q.is_absolute() else p/q
N=400
checks=[]
def ok(v,label):
    if not v: raise AssertionError(label)
    checks.append(label)
def bnum(v):
    sign,m,e,_=v
    return F((-1 if sign else 1)*m)*F(2)**e
def dec(x):return tuple(bnum(v) for v in x['binary'])
def raw(x):return tuple(F(int(a),int(b)) for a,b in x['rational'])
def point(v):return F(v),F(v)
def add(a,b):return a[0]+b[0],a[1]+b[1]
def neg(a):return -a[1],-a[0]
def sub(a,b):return add(a,neg(b))
def mul(a,b):
    v=[x*y for x in a for y in b]
    return min(v),max(v)
def scale(a,c):return mul(a,point(c))
def div(a,b):
    ok(b[0]>0,'positive division')
    return mul(a,(1/b[1],1/b[0]))
def sumiv(v):
    z=point(0)
    for a in v:z=add(z,a)
    return z
def encl(a,lo,hi,label):ok(F(lo)<a[0] and a[1]<F(hi),label)
def overlap(a,b,label):ok(max(a[0],b[0])<=min(a[1],b[1]),label)
full=json.loads((p/'FULL_ZETA_TRACE_RECEIPT.json').read_text())
native=json.loads((p/'NATIVE_ORIGINAL_ZETA_RECEIPT.json').read_text())
for name,d in [('full',full),('native',native)]:
    ok(hashlib.sha256(sourcepath(d['source']).read_bytes()).hexdigest()==d['source_sha256'],name+' source hash')
wpath=sourcepath(native['witness_source'])
ok(hashlib.sha256(wpath.read_bytes()).hexdigest()==native['witness_sha256'],'witness hash')
w=json.loads(wpath.read_text())
c=[F(1000**i*int(n),int(w['denominator'])) for i,n in enumerate(w['rational_numerators'])]
ok(len(c)==19 and int(w['denominator'])==10**120 and c[-1]==10**54,'original exact nineteen coefficients')
roots=json.loads(sourcepath(full['source']).read_text())['results']['zero']
S=[point(0)]+[dec(roots['root_moments'][i]) for i in range(1,4)]
ok(dec(roots['root_moments'][0])==point(0),'dummy S0')
M=[dec(roots['moments'][i]) for i in range(4)]
a=[scale(M[i],F((-1)**i,math.factorial(2*i))) for i in range(4)]
Scheck=[point(0)]
for n in range(1,4):
    value=div(sub(scale(a[n],-2*n),sumiv(mul(a[j],Scheck[n-j]) for j in range(1,n))),M[0])
    overlap(value,S[n],'original moment recurrence S'+str(n))
    Scheck.append(value)
T=[point(0)]
for n in range(1,4):
    partial=sum((F(1,(4*k+1)**(2*n)) for k in range(1,N+1)),F(0))
    T.append((partial+F(1,4*(2*n-1)*(4*(N+1)+1)**(2*n-1)),
              partial+F(1,4*(2*n-1)*(4*N+1)**(2*n-1))))
    ok(T[n]==raw(full['trivial_series_intervals'][n-1]),'exact full-series interval '+str(n))
Z=[point(0)]+[add(S[n],scale(sub(T[n],point(1)),(-1)**n)) for n in range(1,4)]
qh=add(add(S[1],scale(S[2],2)),S[3])
qz=add(add(Z[1],scale(Z[2],2)),Z[3])
qc=add(sub(T[1],scale(T[2],2)),T[3])
det=sub(mul(Z[1],Z[3]),mul(Z[2],Z[2]))
for name,v in [('nontrivial_root_test',qh),('full_zeta_divisor_test',qz),('retained_completion_divisor_test',qc),('full_zeta_matrix_determinant',det)]:
    ok(v==raw(full[name]),'exact receipt '+name)
encl(qh,'0.0115617942','0.0115617943','OZ9')
encl(qz,'-0.059716','-0.059714','OZ10 zeta')
encl(qc,'0.071276','0.071278','OZ10 multiplier')
encl(det,'-0.059715','-0.059713','OZ13 determinant')
ok(Z[1][0]>0,'OZ13 first diagonal')
ok(F(3,250)-F(576,15625)<0,'first trivial zero dominates')
# Independent exact rational interval sums on a fixed decimal grid.
# Each rational term is enclosed using integer division, not floating arithmetic.
grid=10**220
def grid_enclose(num,den):
    lo,rem=divmod(num*grid,den)
    return F(lo,grid),F(lo+(rem!=0),grid)
Tall=[point(0)]
for n in range(1,38):
    partial=sumiv(grid_enclose(1,(4*k+1)**(2*n)) for k in range(1,N+1))
    lowertail=grid_enclose(1,4*(2*n-1)*(4*(N+1)+1)**(2*n-1))
    uppertail=grid_enclose(1,4*(2*n-1)*(4*N+1)**(2*n-1))
    Tall.append((partial[0]+lowertail[0],partial[1]+uppertail[1]))
E=[point(0)]+[scale(sub(Tall[n],point(1)),(-1)**n) for n in range(1,38)]
qa=sumiv(scale(E[i+j+1],c[i]*c[j]) for i in range(19) for j in range(19))
ba=sumiv(scale(E[i+1],c[i]) for i in range(19))
aa=E[1]
for name,v in [('Q',qa),('B',ba),('A',aa)]:
    overlap(v,dec(native['correction'][name]),'native correction overlap '+name)
source=json.loads(sourcepath(native['source']).read_text())
ok(source['source_sha256']==native['witness_sha256'],'native original quadrature witness pin')
window=dec(source['results']['whole_window']['time'])
ok(window[0]<=F(-2) and window[1]>=F(-2)+F(1,10**20),'whole window covers original exact I')
for name,r in source['results'].items():
    Q=add(dec(r['Q'][0]),qa); B=add(dec(r['B'][0]),ba); A=add(dec(r['A'][0]),aa)
    D=sub(mul(A,Q),mul(B,B)); sch=sub(Q,div(mul(B,B),A))
    ok(Q[0]>0 and A[0]>0,name+' positive diagonals')
    encl(D,'-6.41746e106','-6.41741e106',name+' OZ21 determinant')
    encl(sch,'-6.85437e106','-6.85431e106',name+' OZ21 Schur')
    for key,v in [('Q',Q),('B',B),('A',A),('determinant',D),('schur',sch)]:
        overlap(v,dec(native['results'][name][key]),name+' receipt overlap '+key)
out={'status':'passed','checks':checks,'count':len(checks),'method':'Exact Fraction arithmetic; source binary endpoints; N400 rational integral tails; n1..37 sums enclosed by integer division on denominator10^220. No theta quadrature rerun. Full trace receipt matched exactly; native paper enclosures proved independently and receipt intervals checked for overlap.','scope':'Receiving-map verification with retained quadrature receipts as inputs.'}
(p/'INDEPENDENT_ORIGINAL_ZETA_RATIONAL_CHECK.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
