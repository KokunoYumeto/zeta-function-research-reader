"""Finite diagnostics for HD3--4 and HR1--11; not hypothetical xi data."""
from pathlib import Path
import json
import numpy as np
from scipy.linalg import eigh

OUT = Path(__file__).resolve().parent
rng = np.random.default_rng(19092026)
checks = []

def record(name, passed, **data):
    checks.append(dict(name=name, passed=bool(passed), **data))

def star(a):
    return a.conj().T

def rand(*shape):
    return rng.normal(size=shape) + 1j*rng.normal(size=shape)

def scalar(a):
    return float(np.real(a))

def pair(x, G, y):
    return np.vdot(x, G@y)

def forms(G, obs):
    if len(obs):
        Q = np.linalg.inv(obs @ np.linalg.solve(G, star(obs)))
        O = star(obs) @ Q @ obs
    else:
        Q = np.empty((0, 0), dtype=complex)
        O = np.zeros_like(G)
    return Q, O, G-O

for case in range(12):
    n = 5
    R = rand(n,n)
    G = star(R)@R + 3*np.eye(n)
    e, V = eigh(G)
    sqrtG = (V*np.sqrt(e))@star(V)
    isqrtG = (V/np.sqrt(e))@star(V)
    obs = rand(case % (n+1),n)
    v = rand(n)
    cols = [rand(n),rand(n)]
    # Force a small but nonzero original source correlation in some cases.
    if case in [3,7,11]:
        for i, a in enumerate(cols):
            orth = a - v * (np.vdot(v,G@a)/np.vdot(v,G@v))
            cols[i] = orth + (1e-3+2e-3j)*v
    E = scalar(pair(v,G,v))
    d = [scalar(pair(a,G,a)) for a in cols]
    F = np.array([pair(a,G,v) for a in cols])
    p = np.abs(F)**2/(np.array(d)*E)
    eta = min(.04, .2*float(np.sqrt(p).min()))
    k = case % 3 + 1
    delta = np.expm1(np.log1p(eta)/(2*k))
    alpha, beta = (1-delta)**(2*k),(1+delta)**(2*k)
    W, _ = np.linalg.qr(rand(n,n))
    spec = np.linspace(alpha,beta,n)
    Gp = sqrtG @ (W*spec) @ star(W) @ sqrtG
    Q,O,L = forms(G,obs)
    Qp,Op,Lp = forms(Gp,obs)
    fn = lambda A: float(np.max(np.abs(eigh(isqrtG@A@isqrtG,eigvals_only=True))))
    tol = 2e-11
    record(f'HR1_{case}', eigh(Gp-alpha*G,eigvals_only=True).min()>-tol
           and eigh(beta*G-Gp,eigvals_only=True).min()>-tol)
    record(f'HR3_G_{case}', fn(Gp-G)<=eta+tol)
    record(f'HR3_Omega_{case}',fn(Op-O)<=eta+tol)
    record(f'HR3_L_{case}', fn(Lp-L)<=2*eta+tol)
    Ep = scalar(pair(v,Gp,v))
    theta = scalar(pair(v,L,v))/E
    opart = scalar(pair(v,O,v))/E
    opartp = scalar(pair(v,Op,v))/Ep
    record(f'HR4_{case}',alpha/beta*opart-tol<=opartp<=beta/alpha*opart+tol)
    K = np.array([pair(a,L,v) for a in cols])
    Fp = np.array([pair(a,Gp,v) for a in cols])
    Kp = np.array([pair(a,Lp,v) for a in cols])
    U,V = K/F
    Up,Vp = Kp/Fp
    errors = eta*(2+np.abs([U,V]))/(np.sqrt(p)-eta)
    lower = (np.sqrt(p)-eta)*np.sqrt(np.array(d)*E)
    record(f'HR6_denominators_{case}',np.all(np.abs(Fp)>=lower-tol), min_source_energy=float(p.min()))
    record(f'HR6_responses_{case}', np.all(np.abs([Up-U,Vp-V])<=errors+tol))
    record(f'HR7_{case}',np.all(np.abs([U,V])<=np.sqrt(max(0,theta)/p)+tol))
    def products(u,v):
        pk = u.conjugate()*v
        pb = (1-u.conjugate())*(1-v)
        return np.array([pk,pb,1-pk-pb])
    P,Pp=products(U,V),products(Up,Vp)
    eu,ev=errors
    bk=abs(V)*eu+abs(U)*ev+eu*ev
    bb=abs(1-V)*eu+abs(1-U)*ev+eu*ev
    b=np.array([bk,bb,bk+bb])
    record(f'HR9_{case}',np.all(np.abs(Pp-P)<=b+tol))
    c=.17-1.9j
    phi=2*E*np.real(c*P)
    phip=2*Ep*np.real(c*Pp)
    current_bound=2*E*abs(c)*(eta*np.abs(P)+beta*b)
    record(f'HR10_{case}',np.all(np.abs(phip-phi)<=current_bound+tol))
    record(f'HR11_{case}',abs(P.sum()-1)<tol and abs(Pp.sum()-1)<tol
           and abs((phip-phi).sum())<=2*eta*E*abs(c.real)+tol)

# Full-prequotient Schur identities and the exact scaled-isometry fixture.
for case in range(8):
    R=rand(12,7)
    G=star(R)@R
    A,C,S=G[:3,:3],G[:3,3:],G[3:,3:]
    H=A-C@np.linalg.solve(S,star(C))
    c2=eigh(A,H,eigvals_only=True).max()
    P=np.column_stack([np.zeros((12,3)),R[:,3:]])
    pg=eigh(star(P)@P,G,eigvals_only=True).max()
    record(f'HD3_full_operator_{case}',abs(c2-pg)<1e-10)
    oldH=A.copy(); lastc=1.
    valid=True
    for j in range(1,5):
        Cj=C[:,:j]; Hj=A-Cj@np.linalg.solve(S[:j,:j],star(Cj))
        cj=eigh(A,Hj,eigvals_only=True).max()
        valid &= eigh(oldH-Hj,eigvals_only=True).min()>-1e-10 and cj>=lastc-1e-10
        oldH,lastc=Hj,cj
    record(f'HD3_nested_distance_{case}',valid)
    # T_s is represented by s^-1/2 times an actual unitary in this fixture.
    unitary,_=np.linalg.qr(rand(12,12))
    s=2**(case-2)
    Rp=R-unitary@P/np.sqrt(s)
    lam=eigh(star(Rp)@Rp,G,eigvals_only=True).max()
    lower=max(0,np.sqrt(c2/s)-1)**2
    record(f'HD4_reverse_triangle_{case}',lam>=lower-1e-10)

payload=dict(description='Finite complex matrix diagnostics for the proved HD and HR formulas. Includes the original fixed-vector interpretation, small source correlations, zero and full observation image, and all cross products. No xi-zero data or symbolic proof certification is claimed.',
             seed=19092026,checks=checks,total=len(checks),passed=sum(c['passed'] for c in checks))
(OUT/'FINITE_METRIC_RESPONSE_CHECKS.json').write_text(json.dumps(payload,indent=2),encoding='utf-8')
print(json.dumps({k:payload[k] for k in ['total','passed']}))
if payload['passed']!=payload['total']:
    raise SystemExit('Finite diagnostic failure; inspect retained output.')
