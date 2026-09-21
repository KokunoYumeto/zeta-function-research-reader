"""Full-series interval proof of a positive real original period and unit.

No finite series is substituted for the original function: all three tails
are enclosed. The unit magnitude cancels by conjugation, a=alpha*(1+i*x).
Fredrik Johansson, Arb, arXiv:1611.02831v1, is the arithmetic source.
"""
from pathlib import Path
import json, hashlib, math, argparse
import flint
from flint import arb, acb, acb_mat

parser=argparse.ArgumentParser()
parser.add_argument('--radius',default='1e-15')
parser.add_argument('--phase',default='1e-15')
parser.add_argument('--output',default='REAL_PAIR_CERTIFICATE.json')
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

# Two real variables: original inverse period z and exact unit ratio x.
xc_text='-1.466817440463494183975448871845763045856183562396293859'
xc=arb(xc_text)
xinterval=acb(xc+arb(0,phase))
assert box.real>0 and (1+xinterval*xinterval).real>3
Rbox,_,_=matrix(box)
Rci=Rc.inv()
Rpre=acb_mat([[acb(Rci[a,b].real.mid(),Rci[a,b].imag.mid()) for b in range(4)] for a in range(4)])
Rdef=Id-Rpre*Rbox
Rdef_norm=max(sum((Rdef[a,b].abs_upper() for b in range(4)),arb(0)) for a in range(4))
point=evaluate(center,acb(xc)); whole=evaluate(box,xinterval)
from flint import arb_mat
Jc=arb_mat([[point[0]['dz'].real,point[0]['dx'].real],
            [point[0]['dz'].imag,point[0]['dx'].imag]])
Ji=arb_mat([[whole[0]['dz'].real,whole[0]['dx'].real],
            [whole[0]['dz'].imag,whole[0]['dx'].imag]])
# Fixed exact dyadic matrix, printed in RPZ10. Its numerical origin is
# immaterial: the inclusion and invertibility inequalities are checked.
P=arb_mat([[arb(3218485790678941)/2**64,arb(-57245565561083039)/2**64],
           [arb(-5877924768298298697)/2**64,arb(-18277625187819728703)/2**64]])
assert all(P[a,b].is_exact() for a in range(2) for b in range(2))
F=arb_mat([[point[0]['d'].real],[point[0]['d'].imag]])
E=arb_mat([[1,0],[0,1]])-P*Ji
res=P*F; widths=[radius,phase]
normalized=[]; inclusion=[]
for a in range(2):
    vv=sum((E[a,b].abs_upper()*widths[b] for b in range(2)),arb(0))
    normalized.append(vv/widths[a])
    inclusion.append((res[a,0].abs_upper()+vv)/widths[a])
checks={'contraction':all(bool(x<1) for x in normalized),
 'original_matrix_neumann_inverse':bool(Rdef_norm<1),
 'preconditioner_invertible':bool(P.det().abs_lower()>0),
 'strict_self_map':all(bool(x<1) for x in inclusion),
 'period_derivative_nonzero':bool(whole[0]['dz'].abs_lower()>0),
 'symbol_derivative_nonzero':bool(whole[0]['f_xi'].abs_lower()>0),
 'other_pair_nonzero':all(bool(whole[j]['d'].abs_lower()>0) for j in [1,2])}
# G=f1*f2; at the simultaneous real root f1=0 exactly.
A=whole[0]['dz']*whole[1]['d']
Bxi=whole[0]['f_xi']*whole[1]['d']
c=A.real*A.real+A.imag*A.imag
bx=Bxi.real*Bxi.real+Bxi.imag*Bxi.imag
dreal=2*(A.real*Bxi.real+A.imag*Bxi.imag)
# h3 leading inverse coefficient: d=-i*dreal, e=-bx.
# d(d^2-2ce)=(-i*dreal)*(2c*bx-dreal^2).
exception=2*c*bx-dreal*dreal
checks['generic_pole_nonzero']=bool(dreal.abs_lower()>0 and exception.abs_lower()>0)
# Complete factor jets in the original xi coordinate, through the fifth
# moment required by the degree-three actual-order-two ES return.
Rb,_,_=matrix(box); Ri=Rb.inv(); W=Id+J*(acb(0,1)*xinterval)
Wi=(Id-J*(acb(0,1)*xinterval))/(1+xinterval*xinterval)
fj=[]
for jj in range(1,5):
    Dj=acb_mat([[zeta**(-jj*(a+1)) if a==r else 0 for r in range(4)] for a in range(4)])
    M=Wi*V*Ri*Dj*Rb*Vi*W
    cols=[M*acb_mat([[(w+arb(1)/2)**n] for w in roots]) for n in range(6)]
    jet=[sum((math.comb(n,k)*bilinear(cols[k],cols[n-k])/2 for k in range(n+1)),acb(0)) for n in range(6)]
    if jj in [1,4]:jet[0]=acb(0)
    fj.append(jet)
Gjets=[sum((math.comb(n,k)*fj[0][k]*fj[1][n-k] for k in range(n+1)),acb(0)) for n in range(6)]
moments=[sum((math.comb(n,k)*Gjets[k]*Gjets[n-k].conjugate() for k in range(n+1)),acb(0)) for n in range(6)]
checks['symbol_order_exactly_two']=bool(moments[0].is_zero() and moments[1].is_zero() and moments[2].real>0)
checks['real_moments_enclosed']=all(m.imag.contains(0) for m in moments)
g2=-moments[2]/2
g3=acb(0,1)*(moments[3]/6-2*moments[2])
largest_coefficient=abs(dreal*exception)/(c**4)
def txt(v):return v.str(40)
out={'status':'CERTIFIED' if all(checks.values()) else 'FAILED_BOUNDS',
 'scope':'Actual real inverse period and real original unit ratio at delta1/4,gamma3. The exact pair is defined by the unique real d1 zero in the certified rectangle. No arithmetic zeta-quartet identification.',
 'z_center':cr,'x_center_exact':xc_text,'x_center':txt(xc),'z_radius':args.radius,'x_radius':args.phase,
 'original_real_period_enclosure':txt(1/box.real),
 'precision_bits':flint.ctx.prec,'terms_through':N,'tails':[txt(v) for v in tails],
 'python_flint_version':flint.__version__,
 'original_matrix_neumann_defect':txt(Rdef_norm),
 'center_jacobian':[[txt(Jc[a,b]) for b in range(2)] for a in range(2)],
 'preconditioner':[[txt(P[a,b]) for b in range(2)] for a in range(2)],
 'exact_dyadic_preconditioner':[[str(P[a,b].fmpq()) for b in range(2)] for a in range(2)],
 'preconditioned_center_residual':[txt(res[a,0]) for a in range(2)],
 'jacobian_defect':[[txt(E[a,b]) for b in range(2)] for a in range(2)],
 'weighted_contraction_rows':[txt(v) for v in normalized],
 'weighted_self_map_rows':[txt(v) for v in inclusion],
 'preconditioner_determinant':txt(P.det()),
 'full_factor_enclosures':[{k:txt(v) for k,v in p.items()} for p in whole],
 'G_z':txt(A),'G_xi':txt(Bxi),'period_order2_coefficient_c':txt(c),
 'half_mu2':txt(bx),'mixed_first_moment_dreal':txt(dreal),
 'generic_pole_factor':txt(exception),
 'all_original_factor_jets':[[txt(v) for v in jet] for jet in fj],
 'G_jets':[txt(v) for v in Gjets],
 'original_moments_0_through_5':[txt(v) for v in moments],
 'weighted_symbol_g2':txt(g2),'weighted_symbol_g3':txt(g3),
 'largest_inverse_coefficient_before_original_rho3':txt(largest_coefficient),
 'checks':checks,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(B/args.output).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:out[k] for k in ['status','weighted_contraction_rows','weighted_self_map_rows','G_z','G_xi','period_order2_coefficient_c','half_mu2','mixed_first_moment_dreal','generic_pole_factor','checks']},indent=2),flush=True)
if not all(checks.values()):raise SystemExit(2)

