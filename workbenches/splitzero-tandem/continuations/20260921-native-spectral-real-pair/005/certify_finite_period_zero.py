"""Rigorous ball certificate for a full original-period factor zero.

The parameter point is a geometric member of the original family, not an
assertion that this quartet consists of zeros of the Riemann zeta function.
All infinite-series tails are enclosed by the proved factorial majorant.
"""
from pathlib import Path
import json,hashlib,time,math
import flint
from flint import arb,acb,acb_mat
B=Path(__file__).resolve().parent
flint.ctx.prec=768
flint.ctx.threads=1
N=400
delta=arb(1)/4;gamma=arb(3)
beta=2*(gamma*gamma-delta*delta);eta=(delta*delta+gamma*gamma)**2
K=arb(11)/2
assert K*K>=5*beta/3 and K**4>=5*eta and K>=1
T=6*K**5/5;C=4*K**3
center=acb('0.011136978231486808477778740306233906621055400363647396688725562781',
           '0.0078780133477760021239711966284294386302928222474756316845213852718')
radius_text='1e-14'
radius=arb(radius_text)
diskbox=center+acb(arb(0,radius),arb(0,radius))
rho=diskbox.abs_upper()
w=T*rho
assert 3*w/(N+1)<1
fact=[arb(1)]
for n in range(1,5*N//2+4):fact.append(fact[-1]*n)
aa=[arb(1)];bb=[arb(1)]
for p in range(1,5*N//2+4):aa.append(aa[-1]*(beta/3)/p)
for h in range(1,5*N//4+4):bb.append(bb[-1]*eta/h)
poch=[]
for a in range(1,5):
    row=[arb(1)]
    for ell in range(1,2*N+4):row.append(-row[-1]*(a+5*(ell-1)))
    poch.append(row)
Rs=[]
for n in range(N+1):
    row=[]
    for a in range(1,5):
        for r in range(4):
            total=5*n+r+1-a;v=arb(0)
            for h in range(max(0,total//4+1)):
                rem=total-4*h
                if rem%2:continue
                p=rem//2;ell=p+h-n
                assert ell>=0
                v+=aa[p]*bb[h]*poch[a-1][ell]
            row.append(acb(v))
    Rs.append(acb_mat(4,4,row))
    if n%100==0:print('enclosed original R coefficient',n,flush=True)
tail0=C*(2*N+4)*w**(N+1)/fact[N+1]/(1-2*w/(N+2))
tail1=C*(2*N+4)*(N+1)*T*w**N/fact[N+1]/(1-3*w/(N+1))
def matrix(z):
    rr=acb_mat(Rs[-1]);rp=acb_mat(4,4)
    for rn in reversed(Rs[:-1]):rp=rp*z+rr;rr=rr*z+rn
    for a in range(4):
        for k in range(4):
            rr[a,k]+=acb(arb(0,tail0),arb(0,tail0))
            rp[a,k]+=acb(arb(0,tail1),arb(0,tail1))
    return rr,rp
roots=[acb(delta,gamma),acb(delta,-gamma),acb(-delta,gamma),acb(-delta,-gamma)]
V=acb_mat([[r**k for k in range(4)] for r in roots]);Vi=V.inv()
one=acb_mat([[1],[1],[1],[1]])
rho_col=acb_mat([[r+arb(1)/2] for r in roots])
zeta=acb(0,2*arb.pi()/5).exp()
def evaluate(z):
    R,Rp=matrix(z);Ri=R.inv()
    out=[]
    for j in range(1,5):
        D=acb_mat([[zeta**(-j*(a+1)) if a==k else 0 for k in range(4)] for a in range(4)])
        M=V*Ri*D*R*Vi
        Mp=V*(Ri*D*Rp-Ri*Rp*Ri*D*R)*Vi
        yy=M*one;yp=Mp*one;yx=M*rho_col
        value=yy[0,0]*yy[3,0]-yy[1,0]*yy[2,0]
        zp=yp[0,0]*yy[3,0]+yy[0,0]*yp[3,0]-yp[1,0]*yy[2,0]-yy[1,0]*yp[2,0]
        xp=yx[0,0]*yy[3,0]+yy[0,0]*yx[3,0]-yx[1,0]*yy[2,0]-yy[1,0]*yx[2,0]
        out.append((value,zp,xp))
    return out
atcenter=evaluate(center);onbox=evaluate(diskbox)
f0,fp0,_=atcenter[0]
eps=f0.abs_upper();m=fp0.abs_lower();variation=(onbox[0][1]-fp0).abs_upper()
left=eps+variation*radius;right=m*radius
assert m>0 and left<right,('Rouche failed',left,right)
assert onbox[0][2].abs_lower()>0
for j in range(1,4):assert onbox[j][0].abs_lower()>0,(j,onbox[j][0])
mu1=onbox[0][2]
for j in range(1,4):mu1*=onbox[j][0]
assert mu1.abs_lower()>0
alpha=onbox[0][1]
for j in range(1,4):alpha*=onbox[j][0]
assert alpha.abs_lower()>0
# Complete original symbol derivatives at the unique root.  The first
# zero-value factor is exactly zero there; no other coordinate is changed.
Rstar,_=matrix(diskbox);Ristar=Rstar.inv()
factor_jets=[]
for j in range(1,5):
    Dj=acb_mat([[zeta**(-j*(a+1)) if a==k else 0 for k in range(4)] for a in range(4)])
    Mj=V*Ristar*Dj*Rstar*Vi
    columns=[Mj*acb_mat([[(r+arb(1)/2)**n] for r in roots]) for n in range(4)]
    fj=[]
    for n in range(4):
        fj.append(sum((math.comb(n,k)*(columns[k][0,0]*columns[n-k][3,0]
                    -columns[k][1,0]*columns[n-k][2,0]) for k in range(n+1)),acb(0)))
    if j==1:fj[0]=acb(0)
    factor_jets.append(fj)
moments=[acb(1),acb(0),acb(0),acb(0)]
for fj in factor_jets:
    moments=[sum((math.comb(n,k)*moments[k]*fj[n-k] for k in range(n+1)),acb(0)) for n in range(4)]
assert moments[0].is_zero() and moments[1].abs_lower()>0
gstar=[acb(0),-acb(0,1)*moments[1],4*moments[1]-moments[2]/2,
       acb(0,1)*(moments[3]/6-2*moments[2]+arb(25)/3*moments[1])]
u=1/diskbox
def txt(x):return x.str(35)
receipt={
 'status':'CERTIFIED','flint_version':flint.__version__,'precision_bits':flint.ctx.prec,'terms_through':N,
 'scope':'Original geometric parameter family at delta=1/4,gamma=3 and its actual nonzero real-unit phase. This does not assert that the quartet consists of zeta zeros or that the arithmetic unit has this phase.',
 'center':{'real':'0.011136978231486808477778740306233906621055400363647396688725562781',
           'imag':'0.0078780133477760021239711966284294386302928222474756316845213852718'},
 'root_disk_radius':radius_text,'u_enclosure':txt(u),'beta':txt(beta),'eta':txt(eta),
 'tail_majorant':{'K':'11/2','T':txt(T),'C':txt(C),'rho':txt(rho),'R_tail':txt(tail0),'R_derivative_tail':txt(tail1)},
 'rouche':{'center_value_upper':txt(eps),'center_derivative_lower':txt(m),'derivative_variation_upper':txt(variation),'left':txt(left),'right':txt(right),'strict_inequality_proved':True},
 'all_factors_on_box':[{'j':j+1,'value':txt(v),'period_derivative':txt(zp),'symbol_derivative':txt(xp)} for j,(v,zp,xp) in enumerate(onbox)],
 'mu1_at_root_enclosure':txt(mu1),'mu1_lower':txt(mu1.abs_lower()),
 'alpha_at_root_enclosure':txt(alpha),'alpha_lower':txt(alpha.abs_lower()),
 'original_moments_at_root':[txt(m) for m in moments],
 'original_weighted_coefficients_at_root':[txt(g) for g in gstar],
 'proved_conclusion':'Exactly one simple d1 zero lies in the stated disk; original f1 symbol derivative and all other factor values are nonzero there. Five-orbit admissibility follows by the prime-order orbit argument in the companion proof. Total symbol order is exactly1 at that finite geometric period.',
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(B/'FINITE_PERIOD_ZERO_CERTIFICATE.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt,indent=2),flush=True)
