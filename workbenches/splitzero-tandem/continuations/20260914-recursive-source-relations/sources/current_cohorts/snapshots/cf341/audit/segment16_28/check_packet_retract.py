"""Exact algebra regression for the new packet/coefficient retraction.

No numerical value is asserted to be a zeta zero. Lambda and L below stand
for the retained a**rho and log(a). The written proof proves every n and
every packet multiplicity; this script checks matrix orientations and signs.
"""
from pathlib import Path
import hashlib
import json
import math
import sympy as sp

OUT = Path(__file__).resolve().parent
lam, loga = sp.symbols('lambda L', nonzero=True)
checked = []

def require(condition, name):
    if not condition:
        raise RuntimeError(name)

for n in range(1, 9):
    T = sp.zeros(n)
    for i in range(n-1):
        T[i+1,i] = 1
    T[0,n-1] = -1
    require(T**n == -sp.eye(n), f't^n=-1 n={n}')
    require(sp.trace(sp.eye(n)) == n, f'trace(1)=n n={n}')
    for k in range(1,n):
        require(sp.trace(T**k) == 0, f'trace(t^{k}) n={n}')
    for q in (3,5,7,9,11):
        if math.gcd(q,2*n) != 1:
            continue
        P = sp.zeros(n)
        for i in range(n):
            P[(q*i)%n,i] = (-1)**((q*i)//n)
        require(P*T == T**q*P, f'Frobenius monomial intertwining n={n},q={q}')
        require(P.T*P == sp.eye(n), f'coefficient positivity n={n},q={q}')
        e0 = sp.eye(n)[:,0]
        require(P*e0 == e0 and e0.T*P == e0.T, f'unit and retraction n={n},q={q}')
        for m in range(1,5):
            N = sp.zeros(m)
            for j in range(m-1):
                N[j+1,j] = 1
            A = lam*sum((loga**j/sp.factorial(j)*N**j for j in range(m)), sp.zeros(m))
            U = sp.kronecker_product(sp.eye(n),A)
            F = sp.kronecker_product(P,sp.eye(m))
            inc = sp.kronecker_product(e0,sp.eye(m))
            ret = sp.kronecker_product(e0.T,sp.eye(m))
            require(ret*inc == sp.eye(m), f'packet retract n={n},q={q},m={m}')
            require(U*F*inc == inc*A, f'full-jet injection n={n},q={q},m={m}')
            require(ret*U*F == A*ret, f'full-jet retraction n={n},q={q},m={m}')
            require(U*F == F*U, f'commuting actions n={n},q={q},m={m}')
            highest = sp.eye(m)[:,m-1]
            require(A*highest == lam*highest, f'actual eigenline m={m}')
            checked.append({'n':n,'q':q,'m':m})

for m in range(1,5):
    H = m*sp.Matrix([[0,1,0,0],[1,0,0,0],[0,0,0,1],[0,0,1,0]])
    f = sp.Matrix([1,-1,0,0])
    require((f.T*H*f)[0] == -2*m, 'quartet trace')
    for n in range(1,9):
        e0 = sp.eye(n)[:,0]
        v = sp.kronecker_product(e0,f)
        HB = sp.kronecker_product(n*sp.eye(n),H)
        require((v.T*HB*v)[0] == -2*m*n, f'coefficient trace n={n},m={m}')

result = {
    'status':'pass',
    'joint_action_cases':len(checked),
    'case_parameters':checked,
    'trace_extension_cases':32,
    'source_sha256':hashlib.sha256((OUT/'PACKET_SURVIVAL.tex').read_bytes()).hexdigest(),
    'scope':'Exact finite algebra checks only. No value is asserted to be an actual arithmetic zero; no analytic RH or purity estimate is certified by these checks.'
}
(OUT/'CHECK_RESULTS.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({k:result[k] for k in ['status','joint_action_cases','trace_extension_cases','source_sha256']},indent=2))
