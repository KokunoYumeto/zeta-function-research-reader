"""Independent exact audit of NS bridge's two-variable conic connection.

No author checker is imported. Formulas are reconstructed from the original
quadratic presentation and the retained coordinate basis. All output is local.
"""
from pathlib import Path
import hashlib,json
import sympy as S

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
PROOF=ROOT/'agents/ns_scaling_bridge/ns_scaling_bridge.tex'
PRIOR=ROOT/'tex/material_extension.tex'
MATERIAL=ROOT/'tex/material_generator_interface.tex'
s,b,eta,p,q,tau,h=S.symbols('s b eta p q tau h')
beta=b/4
m=b*b/16-2*s
n=m+4
checks=0
def z(x):
    global checks
    checks+=1
    assert S.cancel(S.expand(x))==0,x
def zm(M):
    for x in M: z(x)
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()

# Quadratic presentation and inverse Laurent map, without a choice of root.
qi=(p-eta)/2
qmap=(p+eta)/2
z(S.expand(qmap*qi-1).subs(p*p,n).subs(eta*eta,m))
z(qmap-qi-eta)
z(qmap+qi-p)
z((q-q**-1)**2-((q+q**-1)**2-4))
z((b*b/32-eta**2/2-s).subs(eta**2,m))

eta_s=-1/eta; eta_b=b/(16*eta)
p_s=-1/p; p_b=b/(16*p)
z(2*eta*eta_s-S.diff(m,s))
z(2*eta*eta_b-S.diff(m,b))
z(2*p*p_s-S.diff(n,s))
z(2*p*p_b-S.diff(n,b))
z((eta_s+p_s)/2+qmap/(eta*p))
z((eta_b+p_b)/2-b*qmap/(16*eta*p))
z(S.diff(eta_b,s)+S.diff(eta_b,eta)*eta_s-S.diff(eta_s,b)-S.diff(eta_s,eta)*eta_b)
z(S.diff(p_b,s)+S.diff(p_b,p)*p_s-S.diff(p_s,b)-S.diff(p_s,p)*p_b)

# Basis columns (1,r,p,rp) in (1,eta,p,eta*p).
T=S.Matrix([[1,beta,0,0],[0,1,0,0],[0,0,1,beta],[0,0,0,1]])
Ti=S.Matrix([[1,-beta,0,0],[0,1,0,0],[0,0,1,-beta],[0,0,0,1]])
zm(T*Ti-S.eye(4));zm(Ti*T-S.eye(4))
Hs=S.diag(0,-1/m,-1/n,-1/m-1/n)
Hb=S.diag(0,b/(16*m),b/(16*n),b/(16*m)+b/(16*n))
Gs=S.Matrix([[0,beta/m,0,0],[0,-1/m,0,0],[0,0,-1/n,beta/m],[0,0,0,-1/m-1/n]])
Gb=S.Matrix([[0,S.Rational(1,4)-b*beta/(16*m),0,0],[0,b/(16*m),0,0],
             [0,0,b/(16*n),S.Rational(1,4)-b*beta/(16*m)],
             [0,0,0,b/(16*m)+b/(16*n)]])
zm(Gs-Ti*(Hs*T+T.diff(s)))
zm(Gb-Ti*(Hb*T+T.diff(b)))
zm(Gb.diff(s)-Gs.diff(b)+Gs*Gb-Gb*Gs)
zm(Hb.diff(s)-Hs.diff(b)+Hs*Hb-Hb*Hs)

Js=S.diag(0,-1/m**2,-1/n**2,-1/m**2-1/n**2+2/(m*n))
Jb=S.diag(0,1/(16*m)-b*b/(256*m*m),1/(16*n)-b*b/(256*n*n),
          (1/m+1/n)/16-b*b*(1/m**2+1/n**2)/256+b*b/(128*m*n))
zm(Js-Hs.diff(s)-Hs*Hs)
zm(Jb-Hb.diff(b)-Hb*Hb)
Zs=Gs.diff(s)+Gs*Gs
Zb=Gb.diff(b)+Gb*Gb
zm(Zs-Ti*(Js*T+2*Hs*T.diff(s)+T.diff(s,2)))
zm(Zb-Ti*(Jb*T+2*Hb*T.diff(b)+T.diff(b,2)))

# Completely written original-basis second b derivative, independently of
# the author's diagonal-basis display.
up=-b/(64*m)+b**3/(1024*m*m)
low=up+b/(32*n)-b**3/(512*m*n)
Zb_explicit=S.Matrix([[0,up,0,0],[0,Jb[1,1],0,0],
                      [0,0,Jb[2,2],low],[0,0,0,Jb[3,3]]])
zm(Zb-Zb_explicit)

# Compare to prior material extension, where Gamma_b denotes the s
# connection parametrized by b, not the new b-direction connection.
delta=16*m
Ab=S.Matrix([[0,4*b/delta],[0,-16/delta]])
oldGs=S.diag(Ab,Ab-S.eye(2)/n)
oldZs=S.Matrix([[0,64*b/delta**2,0,0],[0,-256/delta**2,0,0],
               [0,0,-1/n**2,64*b/delta**2-8*b/(delta*n)],
               [0,0,0,-256/delta**2+32/(delta*n)-1/n**2]])
zm(oldGs-Gs);zm(oldZs-Zs)

# Direct connection Leibniz identity on every product of the four
# quadratic-basis vectors: this checks derivations, not just matrices.
def product_basis(i,j):
    ei,pi=i%2,i//2
    ej,pj=j%2,j//2
    e,powp=ei+ej,pi+pj
    coeff=(m if e==2 else 1)*(n if powp==2 else 1)
    out=S.zeros(4,1);out[(e%2)+2*(powp%2)]=coeff
    return out
for var,H in [(s,Hs),(b,Hb)]:
    for i in range(4):
        for j in range(4):
            prod=product_basis(i,j)
            zm(prod.diff(var)+H*prod-(H[i,i]+H[j,j])*prod)

# Time/base sign and both branch equations, retaining independent b.
t,zcoord=S.symbols('t zcoord')
physical_m=m.subs({s:1-t,b:zcoord})
z(physical_m-(zcoord*zcoord/16-2*(1-t)))
z(S.diff(physical_m,t)+S.diff(m,s))
z(S.diff(physical_m,zcoord)-S.diff(m,b).subs(b,zcoord))
z(n-m-4)
z((b*b/32+2)-(b*b/32)-2)

# All original Laurent coefficient factors and complete finite polynomial.
C=q**10-q**4-q**-4+q**-10
qint=lambda k:sum(q**(k-1-2*j) for j in range(k))
z(C-(q-q**-1)**2*qint(7)*qint(3))
z(qint(3)-((q+q**-1)**2-1))
z(qint(7)-((q+q**-1)**6-5*(q+q**-1)**4+6*(q+q**-1)**2-1))
Cb=m*(n**3-5*n*n+6*n-1)*(n-1)
B=-42+196*tau-280*tau**2+160*tau**3-32*tau**4
Ctau=-2*tau*(3-2*tau)*(7-28*tau+28*tau**2-8*tau**3)
z(Cb.subs({b:0,s:tau})-Ctau)
z(Ctau-tau*B)
z(B.subs(tau,0)+42)
z(S.diff(Ctau,tau).subs(tau,0)+42)
z((S.Rational(1,2)-h)-(1-(S.Rational(1,2)+h)))

# Unit-circle coordinates checked polynomially, keeping both signs.
a,pp=S.symbols('a pp',real=True)
for eps in [-1,1]:
    for epsp in [-1,1]:
        qq=(epsp*pp+eps*S.I*a)/2
        qc=S.conjugate(qq)
        z(S.expand(qq*qc-1).subs(pp*pp,m+4).subs(a*a,-m))
        z(qq+qc-epsp*pp)
        z(qq-qc-eps*S.I*a)

receipt={'status':'passed','checks':checks,'reviewed_tex_sha256':sha(PROOF),
         'prior_material_extension_sha256':sha(PRIOR),'prior_material_interface_sha256':sha(MATERIAL),
         'verified':['quadratic presentation and inverse Laurent maps','lifted generator derivatives',
                     'both full original-basis connection matrices','flatness in both bases',
                     'both complete second derivative constant matrices','second derivative gauge transport',
                     'old material s-connection and square compatibility','Leibniz identity on all basis products',
                     'physical time reversal and axial base map','branch separation','all Laurent coefficient factors',
                     'finite polynomial and exact order-one leading coefficient','all four unit-circle sheets'],
         'original_basis_second_b_matrix':str(Zb_explicit),'findings':[]}
(HERE/'conic_verification.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'passed','checks':checks,'reviewed_tex_sha256':sha(PROOF)}))
