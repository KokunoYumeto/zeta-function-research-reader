"""Exact symbolic matrix verification of the original fixed-space consequences."""
from pathlib import Path
from itertools import combinations
import hashlib,json
import sympy as s
HERE=Path(__file__).resolve().parent
checks=[]

def check(name,entries):
    entries=list(entries) if isinstance(entries,(list,tuple,s.MatrixBase)) else [entries]
    for entry in entries:assert s.cancel(entry)==0,(name,entry)
    checks.append({'name':name,'entries':len(entries)})

for N in range(1,5):
    gg=s.symbols('g0:'+str(N),nonzero=True)
    rho=s.symbols('r0:'+str(N),positive=True)
    B=s.Matrix(N,N,lambda i,j:gg[j-i]*rho[j]/rho[i] if i<=j else 0)
    hh=[1/gg[0]]
    for n in range(1,N):hh.append(-sum(gg[k]*hh[n-k] for k in range(1,n+1))/gg[0])
    inv=s.Matrix(N,N,lambda i,j:hh[j-i]*rho[j]/rho[i] if i<=j else 0)
    check(f'full inverse with original weights N={N}',B*inv-s.eye(N))
    check(f'unchanged determinant N={N}',B.det()-gg[0]**N)
    for r in range(1,N+1):
        subs=list(combinations(range(N),r))
        for I in subs:
            check(f'exterior diagonal N={N},r={r},I={I}',inv.extract(I,I).det()-gg[0]**(-r))
            for J in subs:
                Ic=[a for a in range(N) if a not in I]
                Jc=[a for a in range(N) if a not in J]
                lhs=inv.extract(I,J).det()
                rhs=(-1)**(sum(I)+sum(J))*B.extract(Jc,Ic).det()/gg[0]**N
                check(f'complete complementary minor N={N},r={r},I={I},J={J}',lhs-rhs)
    shift=s.Matrix(N,N,lambda i,j:1 if j==i+1 else 0)
    for v in range(1,N+2):
        vv=s.symbols('a0:'+str(N),nonzero=True)
        Q=s.Matrix(N,N,lambda i,j:vv[j-i]*rho[j]/rho[i] if i<=j else 0)
        weighted_shift=s.diag(*rho).inv()*shift**v*s.diag(*rho)
        Bzero=weighted_shift*Q
        expected=s.Matrix(N,N,lambda i,j:vv[j-i-v]*rho[j]/rho[i] if j-i>=v else 0)
        check(f'exact rank-loss factorization N={N},v={v}',Bzero-expected)
        assert Bzero.rank()==max(N-v,0)
        checks.append({'name':f'complete rank N={N},v={v}','entries':1})

u,u0=s.symbols('u u0',nonzero=True)
check('original inverse-period difference',1/u-1/u0+(u-u0)/(u*u0))
out={'status':'pass','groups':len(checks),'scalar_entries':sum(c['entries'] for c in checks),
     'checks':checks,
     'proof_sha256':hashlib.sha256((HERE/'GLOBAL_CONDUCTOR_ZERO_CONSEQUENCE.tex').read_bytes()).hexdigest(),
     'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'scope':'Exact free-symbol identities for N=1..4 with all Gamma-weight slots retained; the source proves the full arbitrary-N analytic norm and pole statements.'}
(HERE/'GLOBAL_CONDUCTOR_ZERO_CHECK.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'pass','groups':out['groups'],'scalar_entries':out['scalar_entries']}),flush=True)
