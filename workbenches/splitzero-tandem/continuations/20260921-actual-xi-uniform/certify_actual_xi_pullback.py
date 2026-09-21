"""Actual Xi-jet pullback at the certified original-period interval.

No finite series is substituted for the original function: all three tails
are enclosed. Period-kernel source: RPZ1-19 and certify_real_pair.py, preserved without coefficient changes.
The actual Xi residual and unit are evaluated below; no zero quartet is assumed.
Fredrik Johansson, Arb, arXiv:1611.02831v1, is the arithmetic source.
"""
from pathlib import Path
import json, hashlib, math, argparse
import flint
from flint import arb, acb, acb_mat

parser=argparse.ArgumentParser()
parser.add_argument('--radius',default='1e-15')
parser.add_argument('--phase',default='1e-15')
parser.add_argument('--output',default='ACTUAL_XI_PULLBACK_CERTIFICATE.json')
args=parser.parse_args()
B=Path(__file__).resolve().parent
flint.ctx.prec=768
flint.ctx.threads=1
N=650
delta=arb(1)/4; gamma=arb(3)
beta=2*(gamma*gamma-delta*delta); eta=(delta*delta+gamma*gamma)**2
K=arb(11)/2; T=6*K**5/5; C=4*K**3
assert K*K>=5*beta/3 and K**4>=5*eta
cr='0.02211947780866184513200791639903555836071244787217846841'
ci='0'
center=acb(cr,ci); radius=arb(args.radius); phase=arb(args.phase)
box=center+acb(arb(0,radius),0)
assert radius>0 and phase>0
w=T*box.abs_upper()
fact=[arb(1)]
for n in range(1,5*N//2+4): fact.append(fact[-1]*n)
aa=[arb(1)]; bb=[arb(1)]
for p in range(1,5*N//2+4): aa.append(aa[-1]*(beta/3)/p)
for h in range(1,5*N//4+4): bb.append(bb[-1]*eta/h)
poch=[]
for a in range(1,5):
    row=[arb(1)]
    for ell in range(1,2*N+4): row.append(-row[-1]*(a+5*(ell-1)))
    poch.append(row)
Rs=[]
for n in range(N+1):
    entries=[]
    for a in range(1,5):
        for r in range(4):
            total=5*n+r+1-a; val=arb(0)
            for h in range(max(0,total//4+1)):
                rem=total-4*h
                if rem%2: continue
                p=rem//2; ell=p+h-n
                assert ell>=0
                val+=aa[p]*bb[h]*poch[a-1][ell]
            entries.append(acb(val))
    Rs.append(acb_mat(4,4,entries))
    if n%100==0: print('Original coefficient',n,flush=True)
q0=2*w/(N+2); q1=3*w/(N+1); q2=w*(N+3)/(N*(N+2))
assert q0<1 and q1<1 and q2<1
tails=[C*(2*N+4)*w**(N+1)/fact[N+1]/(1-q0),
       C*(2*N+4)*(N+1)*T*w**N/fact[N+1]/(1-q1),
       C*(2*N+4)*N*(N+1)*T*T*w**(N-1)/fact[N+1]/(1-q2)]

def raw_matrix(z):
    rr=acb_mat(Rs[-1]); rp=acb_mat(4,4); rpp=acb_mat(4,4)
    for rn in reversed(Rs[:-1]):
        rpp=rpp*z+2*rp; rp=rp*z+rr; rr=rr*z+rn
    for mat,tail in zip((rr,rp,rpp),tails):
        for a in range(4):
            for r in range(4): mat[a,r]+=acb(arb(0,tail),arb(0,tail))
    return rr,rp,rpp

Rc,Rpc,Rppc=raw_matrix(center)
def matrix(z):
    # Only centred period boxes (or the centre itself) are used. Their
    # convex hull contains every segment needed in the Taylor identity.
    if z==center: return Rc,Rpc,Rppc
    _,_,Rpp=raw_matrix(z)
    dz=z-center; h=dz.abs_upper()
    # Taylor integral identities for the COMPLETE analytic matrix. The
    # original coordinates and all series coefficients remain unchanged.
    rr=Rc+Rpc*dz; rp=acb_mat(Rpc)
    for a in range(4):
        for r in range(4):
            L2=Rpp[a,r].abs_upper()
            rr[a,r]+=acb(arb(0,L2*h*h/2),arb(0,L2*h*h/2))
            rp[a,r]+=acb(arb(0,L2*h),arb(0,L2*h))
    return rr,rp,Rpp

roots=[acb(delta,gamma),acb(delta,-gamma),acb(-delta,gamma),acb(-delta,-gamma)]
V=acb_mat([[r**k for k in range(4)] for r in roots]); Vi=V.inv()
one=acb_mat([[1],[1],[1],[1]])
rho_col=acb_mat([[r+arb(1)/2] for r in roots])
zeta=acb(0,2*arb.pi()/5).exp()
J=acb_mat([[([1,-1,-1,1][a] if a==b else 0) for b in range(4)] for a in range(4)])
Id=acb_mat([[int(a==b) for b in range(4)] for a in range(4)])

def bilinear(v,w):
    return v[0,0]*w[3,0]+v[3,0]*w[0,0]-v[1,0]*w[2,0]-v[2,0]*w[1,0]

def evaluate(z,x):
    R,Rp,Rpp=matrix(z); A=R.inv(); W=Id+J*(acb(0,1)*x)
    Wi=(Id-J*(acb(0,1)*x))/(1+x*x)
    out=[]
    for j in range(1,5):
        D=acb_mat([[zeta**(-j*(a+1)) if a==k else 0 for k in range(4)] for a in range(4)])
        C0=A*D*R
        C1=A*D*Rp-A*Rp*A*D*R
        C2=A*D*Rpp-2*A*Rp*A*D*Rp+2*A*Rp*A*Rp*A*D*R-A*Rpp*A*D*R
        M=Wi*V*C0*Vi*W; Mz=Wi*V*C1*Vi*W; Mzz=Wi*V*C2*Vi*W
        Mx=(M*J-J*M)*acb(0,1)/(1+x*x)
        Mzx=(Mz*J-J*Mz)*acb(0,1)/(1+x*x)
        comm=M*J-J*M
        Mxx=-(comm*J-J*comm+comm*(2*acb(0,1)*x))/(1+x*x)**2
        y=M*one; yz=Mz*one; yzz=Mzz*one; yx=Mx*one; yzx=Mzx*one
        yxx=Mxx*one
        h=M*rho_col; hz=Mz*rho_col; hx=Mx*rho_col
        out.append({'d':bilinear(y,y)/2,'dz':bilinear(y,yz),
                    'dzz':bilinear(yz,yz)+bilinear(y,yzz),
                    'dx':bilinear(y,yx),'dzx':bilinear(yx,yz)+bilinear(y,yzx),
                    'dxx':bilinear(yx,yx)+bilinear(y,yxx),
                    'f_xi':bilinear(y,h),'f_xi_z':bilinear(yz,h)+bilinear(y,hz),
                    'f_xi_x':bilinear(yx,h)+bilinear(y,hx)})
    return out


from flint import acb_series

def xi_jet(s):
    q=acb_series([s,1],3)
    return q*(q-1)*(-(q/2)*arb.pi().log()).exp()*(q/2).gamma()*q.zeta()/2

def xi_data(delt, gam):
    wp=acb(delt,gam); lm=wp*wp; dd=acb(0,4*delt*gam)
    X=xi_jet(wp+arb(1)/2)
    fp=2*X[0]
    # The real forms follow exactly from conjugation; interval copies are
    # not treated as independent mathematical values.
    l1=fp.imag/(2*delt*gam)
    l0=fp.real-l1*lm.real
    ap=(X[1]/wp-l1)/dd
    return dict(xi=X[0],xi_prime=X[1],xi_second=2*X[2],
                ell0=l0,ell1=l1,a=ap,x=ap.imag/ap.real)

data=xi_data(delta,gamma)
# A complete real parameter rectangle, not a finite sample grid.
wide=xi_data(delta+arb(0,'1e-8'),gamma+arb(0,'1e-8'))
assert data['ell0']>arb('0.97625') and data['ell0']<arb('0.97627')
assert data['ell1']>arb('0.01893') and data['ell1']<arb('0.01894')
assert data['a'].real>0
assert data['x']>arb('0.01020') and data['x']<arb('0.01022')
assert wide['ell0']>arb('0.975') and wide['ell1']>arb('0.0188')
assert wide['a'].real>0 and wide['x']>0
vals=evaluate(box,acb(data['x']))
for val in vals:
    assert val['d'].abs_lower()>0
# Keep the exact real reflection product of the first two factors.
mu0_ref=(vals[0]['d'].real**2+vals[0]['d'].imag**2)*(vals[1]['d'].real**2+vals[1]['d'].imag**2)
assert mu0_ref>arb('0.0073504212') and mu0_ref<arb('0.0073504216')
out={
 'status':'PASS',
 'scope':'Exact delta=1/4,gamma=3 Xi-jet graph over the full certified real z interval; separate residual bound on the stated delta,gamma rectangle. No arithmetic zero quartet asserted.',
 'precision_bits':flint.ctx.prec,'threads':flint.ctx.threads,'flint_version':flint.__version__,
 'period_series_terms_through':N,'z_center':cr,'z_radius':args.radius,
 'point':{k:v.str(45) for k,v in data.items()},
 'quartet_rectangle':{'delta_center':'1/4','gamma_center':'3','radius_each':'1e-8','values':{k:v.str(35) for k,v in wide.items()}},
 'factor_values_at_Xi_phase':[v['d'].str(45) for v in vals],
 'mu0_at_Xi_phase':mu0_ref.str(45),
 'complete_period_series_tails':[v.str(30) for v in tails],
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'proof_source_sha256':hashlib.sha256((B/'independent'/'ACTUAL_UNIT_HERMITE_PULLBACK.tex').read_bytes()).hexdigest(),
 'period_kernel_original_sha256':'bb50ba841052d305fc1a66bbfab9095af816f4c8b05eb3f5a1fa578dab883bbe',
 'human_source':'Fredrik Johansson, Arb, arXiv:1611.02831v1, sections on inclusion arithmetic and power series.'
}
(B/args.output).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':out['status'],'point':out['point'],'rectangle_residual':out['quartet_rectangle']['values']['ell0'],'factors':out['factor_values_at_Xi_phase'],'mu0':out['mu0_at_Xi_phase']},indent=2),flush=True)
