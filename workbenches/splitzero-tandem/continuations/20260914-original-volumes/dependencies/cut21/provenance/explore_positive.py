"""Exploratory floating-point HCT evolution; never a proof certificate."""
from pathlib import Path
import math, json, time
import numpy as np
from numba import njit

@njit
def packet(k, m):
    ell=(k-1)//4
    q=(1+k*(m-1))*(k+1)**2
    n=q//2
    amax=q+ell
    size=n+amax+1
    c=np.empty(size); d=np.empty(size)
    for j in range(size):
        c[j]=(2.0*j+1)*(2.0*j+0.5)
        d[j]=2.0*j*(2.0*j-0.5)
    slog=np.empty(ell+1); cn=np.empty(ell+1); c0=np.empty(ell+1)
    q2=float(q)*q
    sample=np.empty(6)
    for a in range(amax+1):
        if a>=q:
            s=a-q
            slog[s]=sum(np.log(c[:n]/q2))
            cn[s]=math.log(c[n]/q2)
            c0[s]=math.log(c[0]/q2)
            if a==q:
                for t in range(6):
                    sample[t]=c[(n*t)//5]/q2
        if a==amax: break
        nc=np.empty(size-1); nd=np.empty(size-1)
        eta=c[0]
        nc[0]=eta+d[1]; nd[0]=0
        for j in range(1,size-1):
            denom=eta+d[j]
            nd[j]=c[j]*d[j]/denom
            eta=c[j]*eta/denom
            nc[j]=eta+d[j+1]
        c=nc; d=nd; size-=1
    original_product=0.0
    for j in range(2*ell):
        for a in range(q,2*q):
            original_product-=math.log((a+j+0.5)/q)
        for a in range(q+1,2*q+1):
            original_product-=math.log((a+j+0.5)/q)
    highlow=0.0
    for s in range(ell):
        highlow+=2*slog[s]+cn[s]+2*slog[s+1]-c0[s]
    return q,original_product+highlow,original_product,highlow,sample

if __name__=='__main__':
    rows=[]
    for k,m in [(5,1),(9,1),(17,1),(33,1),(65,1),(129,1),(5,2),(9,2),(17,2)]:
        start=time.time()
        q,w,p,h,sample=packet(k,m)
        ell=(k-1)//4
        row=dict(k=k,m=m,l=ell,q=int(q),W_exploratory=w,W_over_lq=w/(ell*q),P_after_exact_scale=p,high_low_after_exact_scale=h,c_at_q_over_q2=sample.tolist(),seconds=time.time()-start)
        rows.append(row)
        print(json.dumps(row),flush=True)
    Path(__file__).with_name('EXPLORATORY_VALUES.json').write_text(json.dumps({'scope':'floating point exploration, no error certification or theorem','rows':rows},indent=2))
