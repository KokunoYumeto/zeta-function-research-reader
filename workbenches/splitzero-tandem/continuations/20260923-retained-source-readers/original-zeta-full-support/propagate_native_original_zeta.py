from pathlib import Path
from fractions import Fraction
import json,hashlib
from mpmath import mp,iv

p=Path(__file__).parent
s=p/'inputs'
source=s/'NATIVE_SCHUR_INTERVALS.json'
data=json.loads(source.read_text())
witness=s/'rational_witness.json'
j=json.loads(witness.read_text())
mp.dps=400;iv.dps=400
def decode(q):
    b=q['binary'];v=[]
    for sign,m,e,_ in b:v.append((-1)**sign*iv.mpf(m)*iv.mpf(2)**e)
    return iv.mpf([v[0].a,v[1].b])
def encode(x):
    return {'binary':[list(map(int,t)) for t in x._mpi_],
            'display':[mp.nstr((-1)**a*mp.mpf(b)*mp.power(2,c),40) for a,b,c,d in x._mpi_]}
c=[iv.mpf(int(n))*iv.mpf(1000)**i/iv.mpf(int(j['denominator'])) for i,n in enumerate(j['rational_numerators'])]
if len(c)!=19:raise ArithmeticError('Original witness is not19dimensional')
N=400;T=[iv.mpf(0)]
for n in range(1,38):
    part=sum((iv.mpf(1)/iv.mpf(4*k+1)**(2*n) for k in range(1,N+1)),iv.mpf(0))
    lo=part+iv.mpf(1)/(4*(2*n-1)*iv.mpf(4*(N+1)+1)**(2*n-1))
    hi=part+iv.mpf(1)/(4*(2*n-1)*iv.mpf(4*N+1)**(2*n-1))
    T.append(iv.mpf([lo.a,hi.b]))
E=[iv.mpf(0)]+[(-1)**n*(T[n]-1) for n in range(1,38)]
qa=sum((c[i]*c[j]*E[i+j+1] for i in range(19) for j in range(19)),iv.mpf(0))
ba=sum((c[i]*E[i+1] for i in range(19)),iv.mpf(0))
aa=E[1]
results={}
for name,r in data['results'].items():
    Q=decode(r['Q'][0])+qa;B=decode(r['B'][0])+ba;A=decode(r['A'][0])+aa
    det=A*Q-B*B;schur=Q-B*B/A
    if not (A>0 and Q>0 and det<0 and schur<0):raise ArithmeticError(name+' inconclusive')
    results[name]={'time':r['time'],'Q':encode(Q),'B':encode(B),'A':encode(A),
                   'determinant':encode(det),'schur':encode(schur),'inertia':[1,1,0]}
    print(name,encode(det)['display'],encode(schur)['display'])
out={'status':'passed','source':source.relative_to(p).as_posix(),'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
 'witness_source':witness.relative_to(p).as_posix(),'witness_sha256':hashlib.sha256(witness.read_bytes()).hexdigest(),
 'original_coefficients':'c_i=1000^i n_i/10^120, original nineteen-vector; columns(f_*,Z^-1)',
 'correction':{'Q':encode(qa),'B':encode(ba),'A':encode(aa)},
 'results':results,'tail':'All T_n include both explicit rational integral bounds of OZ12, N400; n1..37.',
 'scope':'Full original-zeta signed divisor family z_t. Distinct from the compensated nontrivial-zero form; not an RH disproof.'}
(p/'NATIVE_ORIGINAL_ZETA_RECEIPT.json').write_text(json.dumps(out,indent=2)+'\n')
