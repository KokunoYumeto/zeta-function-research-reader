"""Reproducible scientific figures in unchanged ES--Fable coordinates.

Python 3, NumPy and Matplotlib. No external images, sampled arithmetic zeros,
chosen substitute Grams, or rescaled coordinate values. Diagram geometry is
schematic except the isometric tetrahedron and the explicitly labelled RC plot.
"""
from pathlib import Path
import json
import re
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
from itertools import combinations

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'figures'
OUT.mkdir(exist_ok=True)
BG='#fbfcfe'; INK='#172b46'; MUTED='#52647c'; BLUE='#2265ac'
ORANGE='#b55312'; TEAL='#087e80'; RED='#b63c68'; PURPLE='#7352a5'
COL=[BLUE,ORANGE,TEAL,PURPLE]
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':13,
 'mathtext.fontset':'dejavusans','svg.fonttype':'none','figure.facecolor':BG,
 'axes.facecolor':BG,'text.color':INK,'axes.labelcolor':INK,
 'xtick.color':MUTED,'ytick.color':MUTED,'savefig.facecolor':BG})
FIGURES=[]
def sheet(num,title,subtitle):
    f=plt.figure(figsize=(18,12),dpi=120)
    a=f.add_axes([0,0,1,1]);a.set_xlim(0,1);a.set_ylim(0,1);a.axis('off')
    a.text(.035,.965,f'{num:02d}  {title}',size=27,weight='bold',va='top')
    a.text(.035,.914,subtitle,size=14,color=MUTED,va='top')
    return f,a
def box(a,x,y,w,h,title,body='',color=BLUE,fs=15):
    a.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.008,rounding_size=0.012',
      facecolor='white',edgecolor=color,linewidth=1.5))
    a.text(x+.015,y+h-.02,title,color=color,size=fs,weight='bold',va='top')
    if body:a.text(x+.015,y+h-.064,body,size=fs-1,va='top',linespacing=1.65)
def arrow(a,p,q,color=MUTED,label=None,dy=.015):
    a.add_patch(FancyArrowPatch(p,q,arrowstyle='-|>',mutation_scale=17,lw=1.6,color=color))
    if label:a.text((p[0]+q[0])/2,(p[1]+q[1])/2+dy,label,ha='center',size=14,color=color)
def text(a,x,y,s,size=16,**kw):a.text(x,y,s,size=size,va='top',**kw)
def finish(f,a,name,proof,caption,alt):
    a.plot([.035,.965],[.09,.09],color='#d8dfe8',lw=1)
    text(a,.035,.074,'Proof: '+proof,11,color=MUTED)
    text(a,.035,.050,caption,10.5,color=MUTED)
    # Mathtext requires explicit groups where TeX permits a one-token argument.
    artists=f.findobj(matplotlib.text.Text)
    for ax in f.axes:
        for table in ax.tables:
            artists.extend(cell.get_text() for cell in table.get_celld().values())
    for artist in artists:
        s=artist.get_text()
        s=re.sub(r'\\(mathfrak|mathbb|mathcal)\s+([A-Za-z])',r'\\\1{\2}',s)
        s=re.sub(r'\\mathbf([0-9])',r'\\mathbf{\1}',s)
        s=re.sub(r'\\sqrt([0-9])',r'\\sqrt{\1}',s)
        s=re.sub(r'\\sqrt\\([A-Za-z]+)',r'\\sqrt{\\\1}',s)
        s=re.sub(r'\\frac([0-9])([0-9])',r'\\frac{\1}{\2}',s)
        s=re.sub(r'\\le(?![A-Za-z])',r'\\leq ',s)
        s=s.replace('\\bigl','').replace('\\bigr','')
        artist.set_text(s)
    for ext in ['svg','png']:
        f.savefig(OUT/f'{name}.{ext}',dpi=150,metadata={'Creator':'Split-Zero programme; reproducible mathematical figure'} if ext=='svg' else {'Software':'Matplotlib; reproducible mathematical figure'})
    plt.close(f)
    FIGURES.append({'file':name,'proof':proof,'caption':caption,'alt':alt})

# 1: the only geometric projection is an explicitly verified isometry.
f,a=sheet(1,'Four distinct marks; seven affine preimages',
 'The tetrahedral locales and the complex polynomial points retain the same four labels.')
B=np.array([[1,-1,0,0],[1,1,-2,0],[1,1,1,-3]],float)/np.sqrt(np.array([2,6,12]))[:,None]
locales=-2/(3*np.sqrt(3))*(np.eye(4)-np.ones((4,4))/4)
xyz=B@locales
assert np.allclose(B@B.T,np.eye(3))
assert np.allclose(xyz.T@xyz,locales.T@locales)
ax=f.add_axes([.035,.39,.37,.46],projection='3d')
for p,q in combinations(range(4),2):ax.plot(*xyz[:,[p,q]],color='#aab9c9',lw=1.8)
for i,label in enumerate(['M','N','T','E']):
    ax.scatter(*xyz[:,i],s=110,color=COL[i],depthshade=False)
    ax.text(*(xyz[:,i]*1.18),label,color=COL[i],size=18,weight='bold')
ax.set_box_aspect([1,1,1]);ax.view_init(elev=19,azim=33)
for setter in [ax.set_xlim,ax.set_ylim,ax.set_zlim]:setter(-.36,.36)
ax.set_xlabel(r'$(B\mathfrak q)_1$',labelpad=7);ax.set_ylabel(r'$(B\mathfrak q)_2$',labelpad=7);ax.set_zlabel(r'$(B\mathfrak q)_3$',labelpad=7)
ax.set_xticks([-.3,0,.3]);ax.set_yticks([-.3,0,.3]);ax.set_zticks([-.3,0,.3])
text(a,.045,.365,r'$\mathfrak q_l=-\frac{2}{3\sqrt{3}}(e_l-\frac14\mathbf1),\quad\|\mathfrak q_l\|=\frac13$',16)
text(a,.045,.312,'View uses the orthonormal rows',12,color=MUTED)
text(a,.045,.284,r'$(1,-1,0,0)/\sqrt2,\ (1,1,-2,0)/\sqrt6,$',12)
text(a,.045,.258,r'$(1,1,1,-3)/\sqrt{12}.$  Distances are unchanged.',12)
text(a,.435,.855,'Original complex points  '+r'$q_l=Ke_l$',18,weight='bold')
rows=[['M',r'$0$',r'$0$',r'$i/2$',r'$0$'],
 ['N',r'$i$',r'$-1$',r'$-3i$',r'$13$'],
 ['T',r'$1/\sqrt2$',r'$-1-\sqrt2i$',r'$2\sqrt2+6i$',r'$-34-19\sqrt2i$'],
 ['E',r'$1/\sqrt2$',r'$1-\sqrt2i$',r'$-2\sqrt2+6i$',r'$34-19\sqrt2i$']]
ta=f.add_axes([.43,.565,.54,.24]);ta.axis('off')
tb=ta.table(cellText=rows,colLabels=['label','a','y','z','w'],cellLoc='center',colWidths=[.09,.15,.24,.23,.29],bbox=[0,0,1,1])
tb.auto_set_font_size(False);tb.set_fontsize(13)
for (r,c),cell in tb.get_celld().items():
    cell.set_edgecolor('#d5dfea');cell.set_facecolor('#eef3f9' if r==0 else 'white')
    if r>0 and c==0:cell.get_text().set_color(COL[r-1]);cell.get_text().set_weight('bold')
text(a,.45,.535,r'$\det K=77\sqrt2i/2\ne0$',18)
arrow(a,(.66,.486),(.66,.438))
text(a,.677,.48,r'$P$',15)
box(a,.44,.342,.51,.083,r'$P(q_l)=h_0=(0,0,-1,0)^T$',fs=18)
text(a,.445,.305,r'$h_{h_0}(x)=x(x-1)(x+1)$',17)
text(a,.445,.268,'Each finite root has two signs; infinity has one affine state.',12)
box(a,.04,.12,.92,.102,'Complete fibre:  2 + 2 + 2 + 1 = 7',
 'The eighth factor state is restored in the second chart. All seven follow entire trajectories on the original arithmetic orbit.',BLUE,15)
finish(f,a,'fable_01_four_marks','FC1–7, FC15a, FC31–44; GF7–9; FX1–8; MO11.',
 'Source: The Clankers, canonical ES reader v69, theorem explicit-four-time-Jacobian-collision. Fibre completion: this programme.',
 'An isometric tetrahedron with M,N,T,E, the full four complex point coordinates, and their common seven-point affine fibre. The missing factor sign is separate from the four labels.')

# 2: complete commuting receiver, explicit action and two distinct metric corrections.
f,a=sheet(2,'The exact marked map into the original observation',
 'The original matrix K identifies each named point with its own upper arithmetic corner.')
nodes=[(.035,'Raw point',r'$q\in\mathbb C^4$'),(.23,'Four labels',r'$c=K^{-1}q$'),
       (.425,'Upper quotient',r'$J_+c\in E_k$'),(.62,'Observed image',r'$O_+c\in B_k$'),(.815,'Lower quotient',r'$J_-D_\partial c\in E_j$')]
for x,title,body in nodes:box(a,x,.705,.15,.14,title,body,BLUE,14)
for i,lab in enumerate([r'$K^{-1}$',r'$J_+$',r'$\Lambda_k$',r'$\bar C$']):
    arrow(a,(nodes[i][0]+.153,.77),(nodes[i+1][0]-.005,.77),label=lab,dy=.025)
text(a,.04,.661,r'$j=k-8,\qquad D_\partial=\mathrm{diag}(a_{88},a_{80},a_{08},a_{00}),\qquad O_+=\Lambda_kJ_+$',20)
box(a,.04,.443,.43,.17,'Original action and its exact shift',
 r'$\widehat B_k=K\,\mathrm{diag}(k\rho_l)K^{-1}$'+'\n'+r'$(\bar C\Theta_+-A_j\bar C)O_+=8J_-D_\partial\mathrm{diag}(\rho_l)$',TEAL,15)
box(a,.53,.443,.43,.17,'The full polynomial relation',
 r'$T_Ap_l^+=d_l p_l^-+\chi_j Z_l$'+'\n'+r'$Z_l=(T_Ap_l^+-d_lp_l^-)/\chi_j$'+'\n'+r'$\deg Z_l\le16k-49-v$',ORANGE,15)
text(a,.045,.4,'Two separate kernels give two retained positive energies',19,weight='bold')
text(a,.055,.344,r'$H_+=O_+^*Q_NO_+=D_\partial^*J_-^*T_NJ_-D_\partial+\Delta_N^*Q_N\Delta_N$',23)
text(a,.055,.288,r'$J_+^*G_NJ_+=H_++Z_N^*G_NZ_N$',23)
text(a,.055,.23,r'$\Delta_N=O_+-R_NJ_-D_\partial\in\ker\bar C;\quad Z_N=(I-M_N\Lambda_k)J_+\in\ker\Lambda_k$',15)
text(a,.055,.183,r'$R_N=Q_N^{-1}\bar C^*T_N,\quad M_N=G_N^{-1}\Lambda_k^*Q_N,\quad\widehat G_N=K^{-*}H_+K^{-1}$',15)
text(a,.055,.135,'Four-dimensional action is on the indicated image when the original corner coefficients are nonzero; partial support is in Figure 5.',11.5,color=MUTED)
finish(f,a,'fable_02_exact_receiver','MO1–10, MO20; AO1–23; original OB3, EQ1–5 and OC50–74.',
 'ES marking: The Clankers, v69. Observation, original minimum and corner proofs are retained in supporting_proofs.zip with source identities.',
 'A commuting chain from original Fable coordinates through K inverse, upper corner idempotents, actual observation, and conductor, with the exact action shift and both nonnegative residual energies.')

# 3: categorical branch flow, not a drawn real trajectory in a complex state space.
f,a=sheet(3,'One arithmetic orbit: five escaping branches, three finite',
 'Exact complex-time branch diagram for the K-marked original arithmetic generator; arrow positions are schematic.')
text(a,.045,.855,r'$u(t)=K\,\mathrm{diag}(e^{k\rho_l t})K^{-1}u_*,\quad u_*=(0,1,0,0)^T,\quad h_*(x)=x^2(x+1)$',23)
text(a,.045,.79,r'$\nu_A=\frac{k}{154}[-68\gamma+i(25\sqrt2\gamma-136\delta)],\quad\nu_D=\frac{k}{77}[-884\delta+(1631\sqrt2+442i)\gamma]$',17)
text(a,.045,.738,r'$A(t)=\nu_A t+O(t^2),\quad\mathrm{Disc}(h_{u(t)})=-4\nu_Dt+O(t^2);\quad \nu_A\nu_D\ne0$',18)
groups=[(.6,4,ORANGE,'Two roots collide at zero; two signs each',r'$t^{1/4}q_{\pm,\epsilon}(t)\to\kappa_{\pm,\epsilon}e_a$',r'$v_\pm=\pm\sqrt{-\nu_D},\quad\kappa_{\pm,\epsilon}^2=(2v_\pm)^{-1}$'),
 (.43,1,RED,'One infinity sign leaves the original chart',r'$t^3q_{\rm lost}(t)\to-40\nu_A^{-3}e_w$',r'$\text{The other infinity sign stays finite.}$'),
 (.245,3,TEAL,'Three states stay finite',r'$(0,1,7i/2,11)^T$',r'$(\epsilon,1-i\epsilon,-2\epsilon+3i,18-6i\epsilon)^T,\quad\epsilon=\pm1$')]
for y,n,c,ttl,formula,detail in groups:
    for l in range(n):a.add_patch(Circle((.06+l*.035,y+.035),.010,facecolor=c,edgecolor='white',lw=1))
    text(a,.045,y-.01,f'{n} '+('state' if n==1 else 'states'),13,color=c,weight='bold')
    arrow(a,(.20,y+.034),(.28,y+.034),color=c)
    text(a,.30,y+.09,ttl,17,color=c,weight='bold')
    text(a,.30,y+.048,formula,22)
    text(a,.30,y-.007,detail,16)
text(a,.045,.136,'Exactly eight states for 0 < |t| ≤ r₀ (explicit r₀ in MO15). Full original observed constants: MO19; partial-support constants: AO19–23.',11.5,color=MUTED)
finish(f,a,'fable_03_five_escapes','MO12–20; GF7–9, GF16; FX7; AO19–23. These are local branches on a chosen complex-time sector.',
 'Original polynomial and marking: The Clankers, ES reader v69. Five-branch arithmetic calculation and exact constants: programme result SZ-20260920-025.',
 'Eight inverse states over a transverse actual arithmetic orbit split into four quarter-power collision escapes, one third-order chart escape, and three explicitly given finite limits.')

# 4: true sampled coordinate magnitudes, paired with symbolic native-metric asymptotes.
f,a=sheet(4,'An exact collision curve and its full singular spectrum',
 'The plot evaluates the original coordinates for 0 < ε < 1/2. The singular-value formulas retain the original Gram G.')
eps=np.geomspace(1e-4,.49,800)
vals=[1/eps,eps,3*eps**2,eps**2*np.sqrt(1+169*eps**2)]
ax=f.add_axes([.072,.385,.42,.38])
for v,c,lab in zip(vals,COL,[r'$|a|=\varepsilon^{-1}$',r'$|y|=\varepsilon$',r'$|z|=3\varepsilon^2$',r'$|w|=\varepsilon^2\sqrt{1+169\varepsilon^2}$']):ax.loglog(eps,v,color=c,lw=2.5,label=lab)
ax.set_xlabel(r'Original parameter $\varepsilon$');ax.set_ylabel('Original coordinate magnitude');ax.grid(True,which='major',alpha=.2);ax.legend(loc='upper left',fontsize=12)
text(a,.055,.851,r'$q_\varepsilon=(\varepsilon^{-1},-i\varepsilon,3i\varepsilon^2,\varepsilon^2-13i\varepsilon^3)^T$',21)
text(a,.555,.851,r'$P(q_\varepsilon)=(0,1,\varepsilon^2,0)^T$',20)
text(a,.555,.772,'Original-G singular values of DP',18,weight='bold')
for yy,col,eq in zip([.71,.642,.574,.506],COL,[r'$\sigma_1\sim\alpha\varepsilon^{-3}$',r'$\sigma_2\sim(\beta/\alpha)\varepsilon^{-2}$',r'$\sigma_3\sim2\xi/\beta$',r'$\sigma_4\sim\varepsilon^5/\xi$']):
    a.plot([.555,.575],[yy-.015,yy-.015],color=col,lw=4);text(a,.59,yy,eq,23)
text(a,.553,.427,r'$\det DP=-2,\qquad\prod_{r=1}^4\sigma_r=2$',20)
text(a,.055,.313,r'$\alpha^2=G_{11}(G^{-1})_{33},\quad\beta^2=\det G_{12,12}\det(G^{-1})_{34,34},\quad\xi^2=G_{11}(G^{-1})_{44}$',18)
text(a,.055,.254,r'$\varepsilon\|\Psi_*q_\varepsilon\|_{\Gamma,W}\to\sqrt{G_{11}},\quad\|\Psi_*(P(q_\varepsilon)-u_*)\|_{\Gamma,W}=\varepsilon^2\sqrt{G_{33}}$',18)
text(a,.055,.19,r'$A\equiv0:\quad 7\ \mathrm{nearby\ states}\ \longrightarrow\ 4\ \mathrm{collision\ escapes}+3\ \mathrm{finite}.\quad \mathrm{Disc}=\varepsilon^4(1-4\varepsilon^2).$',16)
text(a,.055,.14,'This path is tangent to the discriminant at its endpoint; it differs from the transverse arithmetic orbit in Figure 3.',12,color=MUTED)
finish(f,a,'fable_04_collision_spectrum','RC1–9; GF7–9. Coordinate graph: exact values; singular spectrum: proved asymptotic identities, not a sampled substitute metric.',
 'Collision path: received web derivation, Section 4 (author not supplied). Full native constants and conductor transfer: programme calculation; ES map: The Clankers.',
 'Log-log graph of four exact coordinate magnitudes on the collision branch, alongside all four singular-value exponents and full original-Gram constants. Their product stays two while the inverse becomes unbounded.')

# 5: all original label coefficients and the exact finite reconstruction.
f,a=sheet(5,'At most four original observations recover every active label',
 'The active set is determined by the actual columns bₗ = Λₖeₗ. No visibility is assumed from a vanishing conductor coefficient.')
box(a,.045,.683,.91,.175,'Exact stack and inverse',
 r'$y_t=B D_k^t c,\quad 0\le t<m=|I|\le4,\quad I=\{l:b_l\ne0\}$'+'\n'+r'$p_l(S)=\prod_{r\in I\setminus\{l\}}\frac{S-\lambda_r}{\lambda_l-\lambda_r}=\sum_{t=0}^{m-1}p_{l,t}S^t,\quad c_l=\sum_{t=0}^{m-1}p_{l,t}\frac{b_l^*Qy_t}{b_l^*Qb_l}$',TEAL,18)
text(a,.055,.64,'Both escape directions have a nonzero coefficient at every label',19,weight='bold')
rows=[['M',r'$-4\sqrt2-180i/77$',r'$6/77$'],['N',r'$-30i/77$',r'$1/77$'],['T',r'$(47\sqrt2-64i)/154$',r'$(-3-\sqrt2i)/154$'],['E',r'$(47\sqrt2+64i)/154$',r'$(3-\sqrt2i)/154$']]
ta=f.add_axes([.055,.35,.46,.24]);ta.axis('off')
tb=ta.table(cellText=rows,colLabels=['label',r'$K^{-1}e_a$',r'$K^{-1}e_w$'],cellLoc='center',colWidths=[.13,.47,.4],bbox=[0,0,1,1]);tb.auto_set_font_size(False);tb.set_fontsize(15)
for (r,c),cell in tb.get_celld().items():
    cell.set_edgecolor('#d5dfea');cell.set_facecolor('#eef3f9' if r==0 else 'white')
    if r>0 and c==0:cell.get_text().set_color(COL[r-1]);cell.get_text().set_weight('bold')
box(a,.57,.35,.38,.24,'Any nonempty actual support detects both',
 r'$\mathcal F_m(q)=Z_mK^{-1}q$'+'\n'+r'$\|\mathcal F_m(v)\|_{Q_m}^2=c_I^*K_{m,I}c_I>0$'+'\n'+r'$v=e_a\ \mathrm{or}\ e_w,\quad c=K^{-1}v$',ORANGE,16)
text(a,.055,.315,r'$(K_m)_{lr}=b_l^*Qb_r\sum_{t=0}^{m-1}\overline{\lambda_l}^{\,t}\lambda_r^t,\quad\lambda_l=k\rho_l$',18)
text(a,.055,.224,'Invisible labels remain in the complete nonlinear receiver',18,weight='bold')
text(a,.055,.181,r'$q\longleftrightarrow\bigl(Z_mK^{-1}q,(K^{-1}q)_Z\bigr),\quad Z=I^c;\qquad q=K(\mathcal R_{AO}y,c_Z)$',19)
text(a,.055,.129,'If I is empty, all four labels remain in the hidden component. The full original Gram keeps all visible–hidden cross terms (MO20).',12,color=MUTED)
finish(f,a,'fable_05_observation_recovery','AO1–23; MO20. The finite Lagrange inverse is proved for every one of the 15 nonempty supports; no sample columns are substituted.',
 'Original coefficient tests: programme O1–3, O10. Marked coordinates: The Clankers, ES reader v69. Exact K inverse and full receiver: SZ-20260920-025.',
 'The exact Lagrange reconstruction and the two columns of K inverse show why either escape direction survives any nonempty original observation support, with all invisible labels retained separately.')

# 6: actual signed-state loop, including all means and nonzero mixing.
f,a=sheet(6,'The signed boundary loop moves the complete eight-state object',
 'This loop varies the auxiliary quartet separation δ. The original receiving conductor and its metric remain fixed.')
text(a,.045,.855,r'$q_{l,\pm}=e_l\pm o_l,\quad E=(e_l),\quad O=(o_l),\quad z=E\alpha+O\beta$',22)
for i,lab in enumerate(['M','N','T','E']):
    x=.09+i*.155
    a.add_patch(Circle((x,.716),.023,facecolor=COL[i]));a.add_patch(Circle((x,.596),.023,facecolor='white',edgecolor=COL[i],lw=2))
    text(a,x,.785,lab,19,color=COL[i],ha='center',weight='bold')
    text(a,x,.726,'+',15,color='white',ha='center');text(a,x,.606,'−',15,color=COL[i],ha='center')
    a.add_patch(FancyArrowPatch((x+.032,.708),(x+.032,.608),arrowstyle='<->',mutation_scale=15,lw=1.5,color=COL[i]))
box(a,.725,.576,.235,.215,'One full circuit',r'$\delta(t)=\delta_b e^{2\pi it}$'+'\n'+r'$0<\delta_b<1/2,\ \gamma>2$'+'\n'+'All four signs swap.',PURPLE,15)
text(a,.055,.51,'Labels stay; evaluation keeps the entire mixing term',20,weight='bold')
box(a,.055,.359,.41,.106,r'$(\alpha,z)\ \longmapsto\ (\alpha,\ 2E_{\delta_b}\alpha-z)$',color=TEAL,fs=19)
box(a,.535,.359,.41,.106,'Twice around returns every state',r'$\mathcal T_{\rm loop}^2=I_8$',color=BLUE,fs=17)
text(a,.055,.308,r"$\alpha'=0,\qquad z'=(E'-\Omega E)\alpha+\Omega z,\qquad\Omega=O'O^{-1}$",22)
text(a,.055,.248,r"$\lim_{\delta\to0}\delta(E'-\Omega E)=-R_\gamma E_0,\quad\mathrm{rank}(-R_\gamma E_0)=1$",19)
text(a,.055,.195,r'$\mathrm{rank}(2E_{\delta_b})=3,\qquad\mathrm{spec}(R_\gamma)=\{-\frac12,\frac12,\frac12,\frac32\}$',20)
text(a,.055,.14,'Rank 1 is the limiting residue; rank 3 is the finite based loop. Both use the original mean matrix at their stated parameters.',12,color=MUTED)
finish(f,a,'fable_06_signed_loop','SE1–18; SF1–18; SM1–19; TC1–11. Signed-root monodromy has order 192; this loop is its simultaneous four-sign swap.',
 'Original labelled polynomial: The Clankers, ES reader v69. Signed evaluation, connection and full mixing calculation: programme results 017, 018 and 020.',
 'Four pairs of signed states swap under a single auxiliary quartet loop. In the full retained-label and evaluation coordinates the action is (alpha,z) to (alpha,2E alpha minus z), with a nonzero mixing block.')

# 7: two exact paths connect the three strata; neither is silently an arithmetic orbit.
f,a=sheet(7,'An exact two-leg path connects eight, seven and three states',
 'A proved specialization diagram in the original target coordinates. The two legs are distinct from the arithmetic orbit in Figure 3.')
box(a,.04,.695,.24,.155,'Eight affine states',r'$A\ne0,\quad\mathrm{Disc}\ne0$'+'\n'+'Four labelled roots, two signs each.',BLUE,16)
box(a,.38,.695,.24,.155,'Seven at the original target',r'$h_0=(0,0,-1,0)$'+'\n'+r'$h_{h_0}(x)=x(x-1)(x+1)$',TEAL,15)
box(a,.72,.695,.24,.155,'Three at the collision',r'$u_*=(0,1,0,0)$'+'\n'+r'$h_*(x)=x^2(x+1)$',ORANGE,16)
arrow(a,(.285,.765),(.37,.765),label=r'$\epsilon\downarrow0$',dy=.04)
arrow(a,(.625,.765),(.71,.765),label=r'$\tau\downarrow0$',dy=.04)
text(a,.045,.65,'Leg 1 · one chart escape',19,color=RED,weight='bold')
text(a,.045,.605,r'$u^{(1)}_\epsilon=(-i\epsilon+i\epsilon^3/2,\ 3i\epsilon/2,\ -1,\ 0),\quad0<\epsilon<1/2$',20)
text(a,.045,.55,r'$\mathrm{Disc}=4-9\epsilon^2/4>0,\qquad\epsilon^3q_{M,-}\to40ie_w$',20)
text(a,.045,.497,'The M− factor state stays finite in the second chart; the other seven states reach h₀.',14)
text(a,.045,.437,'Leg 2 · four intrinsic root-collision escapes',19,color=ORANGE,weight='bold')
text(a,.045,.393,r'$u^{(2)}_\tau=(0,1-\tau,-\tau,0),\quad h^{(2)}_\tau(x)=x(x-\tau)(x+1),\quad0<\tau\le1$',20)
text(a,.045,.338,r'$\mathrm{Disc}=\tau^2(1+\tau)^2,\quad\sqrt\tau\,q_{N,\sigma}\to\sigma i e_a,\quad\sqrt\tau\,q_{T,\sigma}\to\sigma e_a$',20)
box(a,.045,.17,.43,.115,'N± and T± escape; M+ and E± remain',
 r'$\sqrt\tau\,\|Fq_{N,\sigma}\|,\ \sqrt\tau\,\|Fq_{T,\sigma}\|\to\sqrt{G_{11}}$',ORANGE,15)
box(a,.525,.17,.43,.115,'Original signs at the junction stay explicit',
 r'$T_- = Jq_E,\qquad E_- = Jq_T$'+'\n'+r'$J(a,y,z,w)=(-a,-y,z,-w)$',TEAL,15)
text(a,.045,.131,r'The second target displacement is $-\tau(e_y+e_z)$: its squared original-Gram coefficient is $G_{22}+G_{33}+2\mathrm{Re}\,G_{23}$.',12,color=MUTED)
finish(f,a,'fable_07_exact_specialization','VA1–6; all seven second-leg source coordinates and both discriminants checked exactly; original receiver and full Gram retained.',
 'Original four marked points and polynomial: The Clankers, ES reader v69. First path: FC45–46; full two-leg specialization and sign dictionary: this programme.',
 'An exact two-leg eight-to-seven-to-three specialization: one missing-chart escape reaches the original seven-point target, followed by four root-collision escapes, with explicit paths, discriminants, signs and native constants.')

(OUT/'FIGURE_DATA.json').write_text(json.dumps({'figures':FIGURES,'tetrahedron_isometry':True,
 'coordinate_plot':{'parameter':'epsilon','domain':(1e-4,.49),'points':len(eps),
 'formulas':['1/epsilon','epsilon','3*epsilon**2','epsilon**2*sqrt(1+169*epsilon**2)'],
 'no_metric_substitution':True},'diagram_coordinates':'schematic; tetrahedron and RC magnitudes explicitly mathematical'},indent=2),encoding='utf-8')
print(json.dumps({'figures':len(FIGURES),'formats':['SVG','PNG'],'output':str(OUT)},indent=2))
