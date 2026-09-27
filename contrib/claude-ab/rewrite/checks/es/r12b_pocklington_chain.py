# Recursive Pocklington chain for 7510085481569082811681 down to trial division.
import sympy as sp
from math import gcd, prod
def cert(n,d=0):
    if n<10**6:
        ok=n>1 and all(n%k for k in range(2,int(n**0.5)+1)); print('  '*d+f'{n}: trial division prime={ok}'); return ok
    f=sp.factorint(n-1); assert prod(q**e for q,e in f.items())==n-1
    print('  '*d+f'{n}: n-1 = '+' * '.join(f'{q}^{e}' if e>1 else str(q) for q,e in sorted(f.items())))
    for q in f:
        if not any(pow(a,n-1,n)==1 and gcd(pow(a,(n-1)//q,n)-1,n)==1 for a in range(2,500)): return False
    return all(cert(q,d+1) for q in f)
print('full Pocklington chain valid:', cert(7510085481569082811681))
