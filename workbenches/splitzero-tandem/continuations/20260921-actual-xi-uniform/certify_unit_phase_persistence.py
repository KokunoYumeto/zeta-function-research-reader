"""Full-series interval proof of persistence for the original unit phase.

No finite series is substituted for the original function: all three tails
are enclosed. The unit magnitude cancels by conjugation, a=alpha*(1+i*x).
Fredrik Johansson, Arb, arXiv:1611.02831v1, is the arithmetic source.
"""
from pathlib import Path
import json, hashlib, math, argparse
import flint
from flint import arb, acb, acb_mat

parser=argparse.ArgumentParser()
parser.add_argument('--radius',default='1e-9')
parser.add_argument('--phase',default='1e-10')
parser.add_argument('--output',default='UNIT_PHASE_PERSISTENCE_CERTIFICATE.json')
args=parser.parse_args()
B=Path(__file__).resolve().parent
flint.ctx.prec=768
flint.ctx.threads=1
N=400
delta=arb(1)/4; gamma=arb(3)
beta=2*(gamma*gamma-delta*delta); eta=(delta*delta+gamma*gamma)**2
K=arb(11)/2; T=6*K**5/5; C=4*K**3
assert K*K>=5*beta/3 and K**4>=5*eta
cr='0.011136978231486808477778740306233906621055400363647396688725562781'
ci='0.0078780133477760021239711966284294386302928222474756316845213852718'
center=acb(cr,ci); radius=arb(args.radius); phase=arb(args.phase)
box=center+acb(arb(0,radius),arb(0,radius))
# Complex phase square contains the entire closed phase disk.
xbox=acb(arb(0,phase),arb(0,phase))
assert radius>0 and phase>0 and 2*phase*phase<1
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

point=evaluate(center,acb(0)); whole=evaluate(box,xbox)
eps=point[0]['d'].abs_upper(); slope=point[0]['dz'].abs_lower()
Lzz=whole[0]['dzz'].abs_upper(); Lx=whole[0]['dx'].abs_upper(); Lzx=whole[0]['dzx'].abs_upper()
left=eps+Lx*phase+Lzx*phase*radius+Lzz*radius*radius/2
right=slope*radius
gap=slope-Lzz*radius-Lzx*phase
# Refined scalar enclosures use segment integration, avoiding repeated
# dependency enlargement in the full matrix expression.
def enlarge(z,r): return z+acb(arb(0,r),arb(0,r))
enclosed=[]
for p,b in zip(point,whole):
    d_error=p['dz'].abs_upper()*radius+b['dzz'].abs_upper()*radius*radius/2+b['dx'].abs_upper()*phase+b['dzx'].abs_upper()*radius*phase
    h_error=b['f_xi_z'].abs_upper()*radius+b['f_xi_x'].abs_upper()*phase
    z_error=b['dzz'].abs_upper()*radius+b['dzx'].abs_upper()*phase
    x_error=b['dzx'].abs_upper()*radius+b['dxx'].abs_upper()*phase
    enclosed.append({'d':enlarge(p['d'],d_error),'dz':enlarge(p['dz'],z_error),
                     'dx':enlarge(p['dx'],x_error),
                     'f_xi':enlarge(p['f_xi'],h_error)})
mu1=enclosed[0]['f_xi']; alpha=enclosed[0]['dz']
for f in enclosed[1:]: mu1*=f['d']; alpha*=f['d']
checks={'rouche':bool(left<right),'derivative_gap':bool(gap>0),
        'symbol_derivative_nonzero':bool(enclosed[0]['f_xi'].abs_lower()>0),
        'other_factors_nonzero':all(bool(f['d'].abs_lower()>0) for f in enclosed[1:]),
        'mu1_nonzero':bool(mu1.abs_lower()>0),'mu0_z_nonzero':bool(alpha.abs_lower()>0)}
phase_derivative=enclosed[0]['dx']*enclosed[1]['d']*enclosed[2]['d']*enclosed[3]['d']
checks['mu0_x_nonzero']=bool(phase_derivative.abs_lower()>0)
# Inverse inclusion and an independent centre-preconditioned Neumann bound.
Rc,_,_=matrix(center); Rb,_,_=matrix(box)
Bc=Rc.inv()
Bdy=acb_mat([[acb(Bc[a,b].real.mid(),Bc[a,b].imag.mid()) for b in range(4)] for a in range(4)])
defect=Id-Bdy*Rb
rows=[sum((defect[a,b].abs_upper() for b in range(4)),arb(0)) for a in range(4)]
checks['neumann_inverse']=all(bool(r<1) for r in rows)
def txt(v): return v.str(35)
result={'status':'CERTIFIED' if all(checks.values()) else 'FAILED_BOUNDS',
 'scope':'Full original geometric family at delta=1/4,gamma=3, a=alpha*(1+i*x), alpha any nonzero real number; actual unit relation on real x. Holomorphic continuation uses the complex x disk. No arithmetic zeta identification is asserted.',
 'precision_bits':flint.ctx.prec,'terms_through':N,'center_real':cr,'center_imag':ci,
 'root_radius':args.radius,'phase_radius':args.phase,'tails':[txt(t) for t in tails],
 'rouche':{k:txt(v) for k,v in {'residual':eps,'slope_lower':slope,'Lzz':Lzz,'Lx':Lx,'Lzx':Lzx,'left':left,'right':right,'derivative_gap':gap}.items()},
 'point':[{k:txt(v) for k,v in p.items()} for p in point],
 'whole_bounds':[{k:txt(v.abs_upper()) for k,v in p.items()} for p in whole],
 'refined_root_enclosures':[{k:txt(v) for k,v in p.items()} for p in enclosed],
 'mu1':txt(mu1),'mu1_lower':txt(mu1.abs_lower()),'mu0_z':txt(alpha),'mu0_z_lower':txt(alpha.abs_lower()),
 'root_phase_derivative':txt(-enclosed[0]['dx']/enclosed[0]['dz']),
 'mu0_phase_derivative':txt(phase_derivative),
 'mu0_phase_derivative_lower':txt(phase_derivative.abs_lower()),
 'phase_speed_upper':txt(Lx/gap) if gap>0 else None,
 'neumann_row_bounds':[txt(r) for r in rows],'checks':checks,
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(B/args.output).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:result[k] for k in ('status','root_radius','phase_radius','rouche','mu1_lower','mu0_z_lower','root_phase_derivative','mu0_phase_derivative','phase_speed_upper','neumann_row_bounds','checks')},indent=2),flush=True)
if not all(checks.values()): raise SystemExit(2)
