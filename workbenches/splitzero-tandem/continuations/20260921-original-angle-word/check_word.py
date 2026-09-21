"""Finite checks for FW1--49. Auxiliary fixtures do not evaluate native periods."""
from pathlib import Path
from collections import Counter
import hashlib, json, math, sys
import sympy as sp
import numpy as np
import scipy.linalg as la
import scipy.integrate as si

exact=[]; numeric=[]
def ck(ok,label):
    if not bool(ok): raise AssertionError(label)
    exact.append(label)
def z(expr,label):
    vals=list(expr) if isinstance(expr,sp.MatrixBase) else [expr]
    ck(all(sp.cancel(a)==0 for a in vals),label)
def nc(ok,label,detail=None):
    if not bool(ok): raise AssertionError((label,detail))
    numeric.append(dict(label=label,detail=detail))
def cnt(k,r,s):
    n=k-7
    def N(p,u): return max(0,min(p+n-1,k-u)-max(p,-u)+1)
    return {(u,v):N(r,u)*N(s,v)-max(n-abs(u),0)*max(n-abs(v),0)
            for u in range(-k,k+1) for v in range(-k,k+1)}
for k in (9,13,29):
    n=k-7; d=n*n; Delta=(k+1)**2-d
    for r in range(9):
        for s in range(9):
            c=cnt(k,r,s)
            ck(min(c.values())>=0 and c[0,0]==0 and sum(c.values())==d*Delta,
               f'displacement count k{k} pivot{r},{s}')
            I={(a,b) for a in range(r,r+n) for b in range(s,s+n)}
            boundary={(a,b) for a in range(k+1) for b in range(k+1)}-I
            H=[p for p in boundary if s<=p[1]<s+n]
            V=[p for p in boundary if r<=p[0]<r+n]
            ck(len(H)==8*n and len(V)==8*n and len(boundary)-len(H)-len(V)==64,
               f'exact strip decomposition k{k} pivot{r},{s}')
    for r,s in ((0,0),(0,8),(2,7),(4,4),(8,0),(8,8)):
        I={(a,b) for a in range(r,r+n) for b in range(s,s+n)}
        boundary={(a,b) for a in range(k+1) for b in range(k+1)}-I
        direct=Counter((a-i,b-j) for i,j in I for a,b in boundary)
        c=cnt(k,r,s)
        ck(all(direct[p]==v for p,v in c.items()),f'pairwise displacement enumeration k{k} pivot{r},{s}')

def mulgauss(a,b): return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def powgauss(a,n):
    r=(1,0)
    while n:
        if n&1:r=mulgauss(r,a)
        a=mulgauss(a,a);n//=2
    return r
phase={}
for r in range(9):
    for s in range(9):
        val=(1,0)
        for (u,v),c in cnt(9,r,s).items():
            if c:val=mulgauss(val,powgauss((12*v,-u),c))
        phase[r,s]=val
for r in range(9):
    for s in range(9):
        a,b=phase[r,s]
        ck(phase[8-r,s]==(a,-b) and phase[r,8-s]==(a,-b),f'exact reflected phase pivot{r},{s}')
        if r==4 or s==4:ck(b==0 and a>0,f'strict central resultant positivity pivot{r},{s}')

y=sp.symbols('y'); I=sp.I
roots=[(2*b-9)*3-I*sp.Rational(2*a-9,4) for a in (4,5) for b in (4,5)]
D=sp.expand(sp.prod(y-w for w in roots))
z(D-(y**4-sp.Rational(143,8)*y**2+sp.Rational(21025,256)),'literal central degree-four polynomial')
dv=sp.expand(D.subs(y,9+I/4))
z(dv-(5166+648*I),'exact boundary root polynomial value')
z(dv*sp.conjugate(dv)-27107460,'exact boundary squared modulus')
a,b=sp.symbols('a b',positive=True)
FF=a*b*sp.log(a*a+b*b)-3*a*b+a*a*sp.atan(b/a)+b*b*sp.atan(a/b)
JJ=b*a*a*sp.log(a*a+b*b)/2-sp.Rational(11,6)*b*a*a+a**3*sp.atan(b/a)/3+a*b*b*sp.atan(a/b)-b**3*sp.log(1+a*a/b/b)/6
z(sp.diff(FF,a,b)-sp.log(a*a+b*b),'rectangle mixed derivative')
z(sp.diff(FF,a,2)-2*sp.atan(b/a),'rectangle tangential second derivative')
z(sp.diff(JJ,a)-FF,'complete rectangle primitive derivative')
for j in range(9):
    layers=[2*i-1 for i in range(1,j+1)]+[2*i-1 for i in range(1,9-j)]
    ck(sum(layers)==j*j+(8-j)**2,f'linear layer coefficient j{j}')
    ck(sum(v*v for v in layers)==(j*(4*j*j-1)+(8-j)*(4*(8-j)**2-1))//3,f'quadratic layer coefficient j{j}')

# A full complex positive five-dimensional fixture; no source moment is invented.
R=sp.Matrix([[1,1+I,0,2,1],[0,2,1-I,0,1],[1,0,2,1,0],[0,I,0,2,1],[1,0,1,0,3]])
G=R.conjugate().T*R+sp.eye(5)
T=sp.diag(0,0,1+I,2-I,3+2*I)
pi=sp.eye(5)[2:,:]; V=sp.eye(5)[:,:2]; B=(pi*G.inv()*pi.T).inv(); WG=G[2:,2:]
DD=T[2:,2:]; H=DD.conjugate().T*WG*DD
tt=sp.symbols('t'); P=G.inv()*T.conjugate().T*G*T
z(P.charpoly(tt).as_expr()/tt**2-(B.inv()*H).charpoly(tt).as_expr(),'all positive eigenvalues and two exact zeros')
z((B.inv()*H).det()-(DD.det()*sp.conjugate(DD.det()))*WG.det()/B.det(),'full positive determinant resultant factor')
F=sp.Matrix([[1,I,2],[0,1-I,-1]]); J=sp.Matrix([[1,0],[0,1],[1,I]])
K=F.col_join(sp.eye(3))*J
HK=K.conjugate().T*G*K; HH=J.conjugate().T*B*J
PK=K*HK.inv()*K.conjugate().T*G; PV=V*(V.T*G*V).inv()*V.T*G; PB=sp.eye(5)-PK
z(sp.trace(PB*PV)-(2-2+sp.trace(HK.inv()*HH)),'observed trace including every complex cross term')
CV=(V.T*G*V).inv()*V.T*G*PB*V
z(CV.det()-HH.det()/HK.det(),'principal compression determinant equals kernel angle determinant')
z(PV*PV-PV,'orthogonal interior projection idempotence')
z(PK*PK-PK,'full kernel projection idempotence')
z(K.conjugate().T*G*(sp.eye(5)-PV)*K-HH,'boundary metric is exact projected kernel metric')

def Fnum(a,b):
    if a==0 or b==0:return 0.
    return a*b*math.log(a*a+b*b)-3*a*b+a*a*math.atan2(b,a)+b*b*math.atan2(a,b)
def Unum(x,y,g,de):
    def fs(a,b):return math.copysign(1,a)*math.copysign(1,b)*Fnum(abs(a),abs(b)) if a*b else 0.
    return (fs(x+g,y+de)-fs(x-g,y+de)-fs(x+g,y-de)+fs(x-g,y-de))/(4*g*de)
def params(g,de,rp,spiv):
    rat=g/de; R0=math.hypot(g,de); L=2*math.sqrt(math.pi/(g*de)); Bg=math.pi/(g*de)
    uc=math.log(4*(g*g+de*de))-3+rat*math.atan(1/rat)+math.atan(rat)/rat
    mean=math.log(4*(g*g+de*de))-11/3+4/3*(rat*math.atan(1/rat)+math.atan(rat)/rat)-1/6*(math.log1p(rat*rat)/(rat*rat)+rat*rat*math.log1p(1/(rat*rat)))
    LH=.5*math.log1p(1/(rat*rat))-.5*math.log1p(rat*rat)/(rat*rat)+2/rat*math.atan(rat)
    LV=.5*math.log1p(rat*rat)-.5*rat*rat*math.log1p(1/(rat*rat))+2*rat*math.atan(1/rat)
    A=lambda j:j*j+(8-j)**2
    BB=lambda j:(j*(4*j*j-1)+(8-j)*(4*(8-j)**2-1))/3
    Cg=4/3*Bg*(g*g+de*de)+2*L*(de*A(rp)+g*A(spiv))+.5*Bg*(de*de*BB(rp)+g*g*BB(spiv))+960*L*R0
    bp=64*(uc-mean)+A(rp)*LH+A(spiv)*LV
    return uc,mean,LH,LV,Cg,bp
for g,de in ((3,.25),(2.1,.49),(7,.03125),(1,1),(1.1,1)):
    uc,mean,LH,LV,_,_=params(g,de,4,4)
    uh=lambda x:Unum(x,de,g,de)
    uv=lambda yy:Unum(g,yy,g,de)
    quad=.5*(si.quad(uh,0,g,epsabs=1e-10)[0]/g+si.quad(uv,0,de,epsabs=1e-10)[0]/de)
    nc(abs(quad-mean)<2e-9,f'complete edge average g{g} d{de}',abs(quad-mean))
    nc(abs(g/de*LH+de/g*LV-math.pi)<2e-10,f'exact layer identity numerical g{g} d{de}')
    nc(abs(uh(g)-uc)<1e-11 and abs(uv(de)-uc)<1e-11,f'common corner value g{g} d{de}')
    if g>de:nc(uh(0)<uv(0)<uc,f'strict full edge ordering g{g} d{de}')

for k in (9,13,29,61):
    n=k-7; d=n*n; Delta=16*n+64
    for g,de in ((3,.25),(2.1,.49)):
        R0=math.hypot(g,de)
        En=2*math.ceil((2*R0/de+1)**2)*math.log(3*R0/de)+(4*R0/de+1)**2*(1+math.ceil(math.log2(5*n)))
        for rp,spiv in ((0,0),(0,8),(2,7),(4,4),(8,0),(8,8)):
            interior=np.array([(2*b-k)*g-1j*(2*a-k)*de for a in range(rp,rp+n) for b in range(spiv,spiv+n)])
            boundary=np.array([(2*b-k)*g-1j*(2*a-k)*de for a in range(k+1) for b in range(k+1) if not(rp<=a<rp+n and spiv<=b<spiv+n)])
            logs=np.array([np.log(np.abs(w-interior)**2).sum() for w in boundary])
            zs=(2*spiv-8)*g-1j*(2*rp-8)*de
            Uvals=np.array([Unum(((w-zs)/n).real,((w-zs)/n).imag,g,de) for w in boundary])
            err=float(np.max(np.abs(logs-2*d*math.log(n)-d*Uvals)))
            nc(err<=En*(1+1e-12),f'all boundary cell errors k{k} g{g} pivot{rp},{spiv}',dict(error=err,bound=En))
            uc,mean,LH,LV,Cg,bp=params(g,de,rp,spiv)
            actual=float(logs.sum()); target=2*Delta*d*math.log(n)+Delta*d*mean+d*bp
            er=abs(actual-target); bound=Delta*En+n*Cg
            nc(er<=bound*(1+1e-12),f'full cross resultant finite remainder k{k} g{g} pivot{rp},{spiv}',dict(error=er,bound=bound))
            layererr=abs(float(Uvals.sum())-Delta*mean-bp)
            nc(layererr<=Cg/n*(1+1e-12),f'separate finite layer bound k{k} g{g} pivot{rp},{spiv}',dict(error=layererr,bound=Cg/n))

rng=np.random.default_rng(20260921)
for dim,d,m in ((9,2,5),(9,5,3),(12,6,4),(100,4,56)):
    DD=dim-d
    raw=rng.normal(size=(dim,dim))+1j*rng.normal(size=(dim,dim)); GG=raw.conj().T@raw/dim+np.eye(dim)
    diag=np.concatenate([np.zeros(d),np.exp(np.linspace(-1,1,DD))*np.exp(1j*np.linspace(.1,2,DD))]); TT=np.diag(diag)
    vb=np.eye(dim,d); pbi=np.eye(dim)[d:,:]; bb=la.inv(pbi@la.solve(GG,pbi.T)); ww=GG[d:,d:]
    vals=la.eigvalsh(TT.conj().T@GG@TT,GG); pos=vals[d:]
    recv=la.eigvalsh(np.diag(diag[d:]).conj().T@ww@np.diag(diag[d:]),bb)
    nc(np.max(np.abs(pos-recv))<1e-10,f'all positive metric singular eigenvalues dimension{dim} d{d}',float(np.max(np.abs(pos-recv))))
    rawj=rng.normal(size=(DD,m))+1j*rng.normal(size=(DD,m)); ff=rng.normal(size=(d,DD))+1j*rng.normal(size=(d,DD)); kk=np.vstack([ff,np.eye(DD)])@rawj
    hk=kk.conj().T@GG@kk; hh=rawj.conj().T@bb@rawj; gam=la.eigvalsh(hh,hk)
    pk=kk@la.solve(hk,kk.conj().T@GG); pv=vb@la.solve(vb.T@GG@vb,vb.T@GG); pb=np.eye(dim)-pk
    ev=la.eigvalsh(vb.T@GG@pb@vb,vb.T@GG@vb)
    nc(abs(np.log(ev).sum()-np.log(gam).sum())<2e-9,f'complete angle determinant d{d} m{m}',float(abs(np.log(ev).sum()-np.log(gam).sum())))
    nc(abs(np.trace(pb@pv).real-(d-m+gam.sum()))<2e-9,f'full observed heat floor trace d{d} m{m}')
    if d<m:nc(np.sum(abs(gam-1)<1e-9)>=m-d,f'forced unit kernel angles when d<m d{d} m{m}')
    if d>=m:nc(np.allclose(np.sort(ev),np.sort(np.r_[gam,np.ones(d-m)]),atol=2e-9),f'complete positive observed spectrum d{d} m{m}')
    # Joint metric comparison with an arbitrary commuting positive diagonal form.
    wt=np.exp(np.linspace(-.6,.6,dim)); S=np.diag(np.sqrt(wt)); gj=S@GG@S
    eg=la.eigvalsh(GG); kap=eg[-1]/eg[0]
    eigj=la.eigvalsh(TT.conj().T@gj@TT,gj)[d:]; ordered=np.sort(abs(diag[d:])**2)
    nc(np.all(eigj>=ordered/kap-1e-10) and np.all(eigj<=ordered*kap+1e-10),f'ordered complete joint comparison dimension{dim} d{d}')
    # Direct relative heat determinant receiver at finite positive time.
    evv,evec=la.eigh(TT.conj().T@GG@TT,GG)
    tau=3.; heat=evec@np.diag(np.exp(-tau*np.maximum(evv,0)))@evec.conj().T@GG
    obsV=pb@vb; BV=obsV.conj().T@GG@obsV
    yzero=obsV.conj().T@GG@pv@obsV; yheat=obsV.conj().T@GG@heat@obsV
    base=la.eigvalsh(yzero,BV); pert=la.eigvalsh(yheat,BV)
    delta=np.log(pert).sum()-np.log(base).sum()
    bound=min(d,DD)*math.log1p(math.exp(-tau*pos[0])/min(gam.min(),1.))
    nc(delta>=-2e-9 and delta<=bound+2e-9,f'relative compressed heat determinant error dimension{dim} d{d}',dict(error=float(delta),bound=bound))

here=Path(__file__).resolve().parent
receipt=dict(status='passed',exact_count=len(exact),numerical_count=len(numeric),exact=exact,numerical=numeric,
             script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             scope='Exact finite algebra and independent numerical fixtures; no native xi moments or periods are evaluated.')
(here/'WORD_CHECKS.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print(json.dumps({k:receipt[k] for k in ('status','exact_count','numerical_count','script_sha256')}))
