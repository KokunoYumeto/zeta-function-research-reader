"""Exact mathematical figures: original metric, conductor, and marked residue.

The plots evaluate the stated original formulae. No eigenvalue or coordinate
is rescaled; dashed curves are proved asymptotes, not fitted regressions.
Requires Python, mpmath, NumPy and Matplotlib. No external image assets.
"""
from pathlib import Path
import json
import re
import numpy as np
import mpmath as mp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'figures_029'; OUT.mkdir(exist_ok=True)
mp.mp.dps=90
BG='#fbfcfe'; INK='#172b46'; MUTED='#52647c'
COL=['#2265ac','#b55312','#087e80','#7352a5']
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':13,
 'mathtext.fontset':'dejavusans','svg.fonttype':'none','figure.facecolor':BG,
 'axes.facecolor':BG,'text.color':INK,'axes.labelcolor':INK,
 'xtick.color':MUTED,'ytick.color':MUTED,'savefig.facecolor':BG})
records=[]

def sheet(num,title,subtitle):
    fig=plt.figure(figsize=(18,12),dpi=120)
    a=fig.add_axes([0,0,1,1]);a.set_xlim(0,1);a.set_ylim(0,1);a.axis('off')
    a.text(.035,.965,f'{num:02d}  {title}',size=27,weight='bold',va='top')
    a.text(.035,.912,subtitle,size=14,color=MUTED,va='top')
    return fig,a

def text(a,x,y,s,size=16,**kw):a.text(x,y,s,size=size,va='top',**kw)

def box(a,x,y,w,h,title,lines,color=COL[0]):
    a.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.009,rounding_size=0.012',
        facecolor='white',edgecolor=color,lw=1.5))
    text(a,x+.015,y+h-.02,title,17,color=color,weight='bold')
    for k,line in enumerate(lines):text(a,x+.015,y+h-.068-.046*k,line,15)

def arrow(a,start,end,label):
    a.add_patch(FancyArrowPatch(start,end,arrowstyle='-|>',mutation_scale=18,lw=1.6,color=MUTED))
    text(a,(start[0]+end[0])/2,(start[1]+end[1])/2+.028,label,14,ha='center',color=MUTED)

def save(fig,a,name,proof,source,alt):
    a.plot([.035,.965],[.09,.09],color='#d8dfe8',lw=1)
    text(a,.035,.072,'Proof: '+proof,11,color=MUTED)
    text(a,.035,.048,source,10.5,color=MUTED)
    for artist in fig.findobj(matplotlib.text.Text):
        value=artist.get_text()
        value=re.sub(r'\\(mathfrak|mathbb|mathcal)\s*([A-Za-z])',r'\\\1{\2}',value)
        artist.set_text(value)
    for ext in ['svg','png']:
        meta={'Creator':'Split-Zero programme; original formulae and cited proofs'} if ext=='svg' else {'Software':'Matplotlib'}
        fig.savefig(OUT/(name+'.'+ext),dpi=150,metadata=meta)
    plt.close(fig)
    records.append({'file':name,'proof':proof,'source':source,'alt':alt})

# The actual two-form morphism; no numerical signs are assigned to the Weil form.
f,a=sheet(8,'The complete eight-state receiver, with both forms',
 'One explicit invertible map carries the full Weil form and the original Gamma norm together.')
box(a,.04,.65,.36,.20,'Original retained state',[
 r'$v=(\alpha,\beta)\in\mathbb C^4\oplus\mathbb C^4$',
 r'$q=E\alpha+O\beta,\qquad d=B_\omega q$',
 r'$\|v\|^2=\alpha^*G_Y\alpha+q^*Gq$'])
box(a,.58,.65,.37,.20,'Same state in exact receiving coordinates',[
 r'$(\alpha,d)\in\mathbb C^4\oplus\mathbb C^4$',
 r'$\beta=-O^{-1}E\alpha+O^{-1}B_\omega^{-1}d$',
 r'$\|v\|^2=\alpha^*G_Y\alpha+d^*H_\omega d$'],COL[2])
arrow(a,(.414,.74),(.566,.74),r'$S_\omega^{-1}$')
box(a,.04,.34,.41,.24,'The full arithmetic form',[
 r'$\mathbb W=[E\ O]^*B_\omega^*T_3B_\omega[E\ O]$',
 r'$S_\omega^*\mathbb W S_\omega=\mathrm{diag}(0_4,T_3)$',
 r'$(T_3)_{ij}=c_{j-i}$  (all nontrivial zeros)',
 'Four graph directions remain in the full state.'])
box(a,.53,.34,.42,.24,'The original positive metric',[
 r'$B_\omega=R_\omega^{-1}C_\kappa\Psi$',
 r'$S_\omega^*\mathbb H S_\omega=\mathrm{diag}(G_Y,H_\omega)$',
 r'$(H_\omega)_{ij}=g_{j-i},\quad B_\omega^*H_\omega B_\omega=G$',
 'All original masses and correlations remain.'],COL[2])
text(a,.055,.285,'Exact return to the conductor',18,weight='bold')
text(a,.055,.244,r'$d\ \longmapsto\ p=C_{-\kappa}R_\omega d\ \longmapsto\ T_A^{-1}p$',21)
text(a,.055,.187,r'Generalized eigenvalues: $0,0,0,0$ and those of $H_\omega^{-1/2}T_3H_\omega^{-1/2}$.',17)
text(a,.055,.145,r'Source norm: replace $(G_Y,H_\omega)$ by the explicitly calculated $(G_X,H_{U,\omega})$ (RW19–20).',13,color=MUTED)
save(f,a,'fable_08_two_forms','RW1–20; NH24 and source sequel. Exact block identities and both original native norms are proved.',
 'Sources: received residue continuation §§3,5; original conductor WCF1–6; Gamma dictionary, NIST DLMF Ch.18 (named authors in the source).',
 'The full eight-dimensional state is carried by one explicit invertible block map to four retained label coordinates and four rational test coefficients. Both Hermitian forms are carried simultaneously; the four graph null directions and the original positive metric are retained.')

# Full raw coefficient-Gram eigenvalues using 90-digit arithmetic.
h=mp.mpf(3);d=h/2;b=mp.mpf('0.5');M=mp.sqrt(2*mp.pi)
mom=[M,0,M*b,0,M*(3*b*b+2*b),0,M*(15*b**3+30*b*b+16*b)]
K=mp.matrix([[mom[j+k] for k in range(4)] for j in range(4)])
def gram(t):
    Q=mp.matrix(4)
    for j in range(4):
        for k in range(4):
            val=0
            for r in range(j+1):
                q=k-r
                if 0<=q<=3-j:
                    val+=mp.binomial(j,r)*(d-1j*t)**(j-r)*(1j)**r*mp.binomial(3-j,q)*(d+1j*t)**(3-j-q)*(-1j)**q
            Q[k,j]=val
    return h*Q.H*K*Q
ts=np.logspace(0,3,81); vals=[]; det=12*h**16*M**4*b**3*(b+1)**2*(b+2)
maxerr=mp.mpf(0)
for tf in ts:
    H=gram(mp.mpf(str(tf)))
    ev=mp.eigsy(H,eigvals_only=True) if all(mp.im(x)==0 for x in H) else mp.eighe(H,eigvals_only=True)
    assert all(x>0 for x in ev)
    maxerr=max(maxerr,abs(mp.fprod(ev)/det-1))
    vals.append([float(ev[3-j]) for j in range(4)])
assert maxerr<mp.mpf('1e-45')
vals=np.array(vals)
cs=[4*h*M,5*h**3*M*b,2*h**5*M*b*(b+1),mp.mpf(3)/10*h**7*M*b*(b+1)*(b+2)]
powers=[6,2,-2,-6]
f,a=sheet(9,'Four height scales in the original metric',
 r'Actual eigenvalues of $H_\omega$; original choice $s=1$, $\sigma=2$, $h=3$, $M=\sqrt{2\pi}$, $b=1/2$.')
ax=f.add_axes([.085,.245,.52,.585])
for j,(cc,power) in enumerate(zip(cs,powers)):
    ax.loglog(ts,vals[:,j],color=COL[j],lw=2.5,label=rf'$\lambda_{j+1}$')
    ax.loglog(ts,float(cc)*ts**power,color=COL[j],lw=1.3,ls='--',alpha=.75)
ax.grid(which='major',color='#dce3ed',lw=.8)
ax.set_xlabel(r'Test-pole height $\tau$  (original units)');ax.set_ylabel('Eigenvalue of the full coefficient Gram')
ax.legend(loc='upper left',ncol=2,fontsize=12);ax.set_xlim(1,1000)
text(a,.655,.825,'Proved asymptotes',18,weight='bold')
for j,line in enumerate([
 r'$\lambda_1\sim4hM|\tau|^6$',r'$\lambda_2\sim5h^3Mb|\tau|^2$',
 r'$\lambda_3\sim2h^5Mb(b+1)|\tau|^{-2}$',
 r'$\lambda_4\sim\frac{3}{10}h^7Mb(b+1)(b+2)|\tau|^{-6}$']):
    text(a,.655,.765-.086*j,line,15,color=COL[j])
text(a,.655,.405,'Exact at every height',17,weight='bold')
text(a,.655,.36,r'$\det H_\omega=12h^{16}M^4b^3(b+1)^2(b+2)$',14)
text(a,.655,.31,r'$B_\omega^*H_\omega B_\omega=G$',21)
text(a,.085,.18,'Solid: raw eigenvalues of the exact moment matrix (90-digit evaluation).  Dashed: proved leading terms.',13)
text(a,.085,.137,'Coefficient conditioning grows like |τ|¹². The map with the two stated native norms remains an exact isometry.',13,color=MUTED)
save(f,a,'fable_09_native_height','RW7–11; NH1–25, especially full compound matrices NH14–17 and spectrum NH18–24.',
 'Sources: original WCF1–6; NIST DLMF Ch.18 by Koornwinder, Wong, Koekoek, Swarttouw and Reinhardt; full derivation in this edition.',
 'Four unscaled eigenvalue curves grow or decay at exponents six, two, minus two and minus six while their product is constant. All original metric constants are displayed. The exact identity with the fixed physical Gram is shown beside the curves.')

# Two sequences of actual original points approaching exactly the same marked M.
def xi(z):return z*(z-1)/2*mp.power(mp.pi,-z/2)*mp.gamma(z/2)*mp.zeta(z)
ns=list(range(2,51)); dec=[];inc=[]
for n in ns:
    dec.append(float(abs(xi(-2j*n)/(4*n*n))))
    inc.append(float((mp.mpf(2*n-1)/(4*n))*mp.factorial(n-1)*mp.power(mp.pi,-n)*mp.zeta(2*n)))
f,a=sheet(10,'One marked point; incompatible arithmetic residue limits',
 r'Both sequences use $q(a)=(a,0,i/2,0)\to q_M=(0,0,i/2,0)$ in the unchanged polynomial coordinates.')
ax=f.add_axes([.085,.385,.505,.44])
ax.semilogy(ns,dec,color=COL[0],lw=2.5,label=r'$a_n=1/(2n)$')
ax.semilogy(ns,inc,color=COL[1],lw=2.5,label=r'$a_n=-i/(2n)$')
ax.grid(which='major',color='#dce3ed',lw=.8)
ax.set_xlabel(r'$n$  (distance in the displayed $a$ coordinate is $1/(2n)$)')
ax.set_ylabel(r'Absolute residue $|a_n^2\xi(-i/a_n)|$')
ax.legend(loc='upper left');ax.set_xlim(2,50)
text(a,.635,.822,'Same original polynomial map',18,weight='bold')
text(a,.635,.765,r'$P(q(a))=$',14)
text(a,.65,.733,r'$(-ia+ia^3/2,\ 3ia/2,\ -1,\ 0)$',14)
text(a,.635,.685,r'$r(a)=-i/a,\qquad\det DP(q)=-2$',16)
text(a,.635,.639,'Two exact residue values',18,weight='bold')
text(a,.635,.584,r'$a_n=1/(2n):\quad\xi(-2ni)/(4n^2)\to0$',14,color=COL[0])
text(a,.635,.517,r'$a_n=-i/(2n):$',16,color=COL[1])
text(a,.635,.475,r'$-\frac{2n-1}{4n}(n-1)!\,\pi^{-n}\zeta(2n)$',19,color=COL[1])
text(a,.635,.412,'Absolute value tends to infinity.',15,color=COL[1])
box(a,.075,.155,.86,.155,'The global differential residue at infinity is a different, defined quantity',[
 r'At $P(q_M)=(0,0,-1,0)$: $h(s)=s^3-s$,  $\mathrm{Res}_\infty\,\xi(s)ds/h(s)=(3-\pi)/12$.',
 'The selected-root residue has no continuous extension at M. The complete polynomial map is regular there.'],COL[2])
save(f,a,'fable_10_residue_boundary','AR3–9 and the exact two-sequence boundary calculation; original Jacobian FC/GF.',
 'Sources: The Clankers, ES reader v69 (original marked map); Riemann completion, NIST DLMF 25.4 (T. M. Apostol); full proof in this edition.',
 'Two original-coordinate sequences approach the same marked point M at the same distance. One arithmetic residue tends to zero and the other grows without bound. Their exact formulae are displayed, together with the separate finite global residue at infinity.')

# The complete confluence morphism retains all four coefficient dimensions.
f,a=sheet(11,'Colliding roots retain their value and derivative',
 r'The four-dimensional algebra has an explicit invertible limit; $\gamma>0$, $\delta\downarrow0$, $r_\eta=1/2+i\eta\gamma$.')
for y,eta,color in [(.76,'+',COL[0]),(.53,'-',COL[1])]:
    a.plot([.10,.36],[y,y],color='#b8c6d9',lw=2)
    a.scatter([.12,.34],[y,y],s=150,color=color)
    text(a,.12,y+.065,rf'$r_{eta}-\delta$',17,ha='center',color=color)
    text(a,.34,y+.065,rf'$r_{eta}+\delta$',17,ha='center',color=color)
    text(a,.23,y-.035,'Each root has two signed factor states.',12,ha='center')
    arrow(a,(.395,y),(.60,y),r'$\delta\to0$')
    a.scatter([.635],[y],s=160,color=color)
    text(a,.635,y+.055,rf'$r_{eta}$',17,ha='center',color=color)
    text(a,.69,y+.035,r'Value: $p(r_\eta)$',16,color=color)
    text(a,.69,y-.016,r'Derivative: $p^\prime(r_\eta)$',16,color=color)
text(a,.045,.405,'Exact paired map (for each sign η)',17,weight='bold')
text(a,.045,.36,r'$p\ \longmapsto\ \left(\frac{p(r_\eta+\delta)+p(r_\eta-\delta)}{2},\ \frac{p(r_\eta+\delta)-p(r_\eta-\delta)}{2\delta}\right)$',20)
text(a,.045,.286,r'$\det\mathcal V_\delta=16\gamma^2(\gamma^2+\delta^2)\ \longrightarrow\ 16\gamma^4>0$',20)
box(a,.055,.12,.88,.13,'Completed arithmetic action at the doubled roots',[
 r'$X=\xi(1/2+i\gamma):\quad (u,v)\longmapsto(Xu,\ -i\eta X^\prime u+Xv),\qquad \det M_{j\xi}=X^4$.'],COL[2])
save(f,a,'fable_11_confluent_jets','AR14–17 and AX1–3: complete coefficient matrix, Hermite inverse, completion jets and principal parts.',
 'Sources: received residue continuation; original factor map, The Clankers ES reader v69; Riemann completion, NIST DLMF 25.4 (Apostol).',
 'Two pairs of distinct roots become two double roots. The exact paired averages and divided differences converge to values and derivatives, with nonzero determinant. The complete arithmetic action retains its derivative term and the four-dimensional algebra, even though no finite resultant-one factor state lies over a multiple root.')

data={'result_id':'SZ-20260920-029','figures':records,
 'native_height_parameters':{'s':'1','sigma':'2','h':'3','b':'1/2','M':'sqrt(2*pi)'},
 'native_height_decimal_digits':90,'maximum_relative_determinant_error':str(maxerr),
 'height_samples':[{'tau':float(t),'eigenvalues_descending':v.tolist()} for t,v in zip(ts,vals)],
 'residue_samples':[{'n':n,'real_a_residue_absolute':x,'imaginary_a_residue_absolute':y} for n,x,y in zip(ns,dec,inc)],
 'scope':'Numerical plots illustrate exactly proved formulae; they are not arithmetic zero searches or proofs of the asymptotes.'}
(OUT/'FIGURE_DATA.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'figures':len(records),'determinant_check':str(maxerr),'output':str(OUT)},indent=2))
