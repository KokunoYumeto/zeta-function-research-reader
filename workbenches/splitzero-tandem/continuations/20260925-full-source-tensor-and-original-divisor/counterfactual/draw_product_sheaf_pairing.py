from pathlib import Path
import json
import sympy as s
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

H=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'mathtext.fontset':'dejavusans'})
navy='#16324f'; teal='#007f86'; orange='#b05214'; grey='#728092'

# Exact finite-dimensional instances; the analytical proof is PRS, not these checks.
# A has dimension 4, J dimension 1; both W have four coordinates, three in ker r.
r=s.zeros(4,4);r[0,0]=1
d=r.row_join(-r)
I4=s.eye(4);I8=s.eye(8)
d0=s.kronecker_product(I8,d).col_join(s.kronecker_product(d,I8))
d1=s.kronecker_product(d,I4).row_join(-s.kronecker_product(I4,d))
B=s.Matrix([[0,0,0,0],[0,0,0,2],[0,0,-3,5],[0,7,11,13]])
b=s.Matrix(1,16,list(B))
pi=s.eye(4)[1:,:]
qmap=s.kronecker_product(pi,pi)
mixed=s.kronecker_product(r,I4).row_join(s.kronecker_product(I4,r))
diag=s.kronecker_product(r,r)
Bq=B[1:,1:]
support=Bq.row_join(-Bq).col_join((-Bq).row_join(Bq))
delta=s.eye(3).col_join(s.eye(3))
checks={
 'ordered_d_squared_zero':d1*d0==s.zeros(16,64),
 'residue_annihilates_all_product_boundaries':b*d1==s.zeros(1,64),
 'tensor_quotient_kernel':qmap*mixed==s.zeros(9,32) and mixed.rank()==16-qmap.rank(),
 'diagonal_restrictions_killed':b*diag==s.zeros(1,16),
 'both_support_radical':support*delta==s.zeros(6,3) and support.rank()==3,
 'retained_non_symmetric_pairing':Bq.det()!=0 and Bq!=Bq.T,
 'distinct_scalar_and_quotient_kernels':(16-diag.rank())-1==14 and (16-diag.rank())-qmap.rank()==6,
 'half_coordinate_factor_four':((-s.eye(3)).row_join(s.eye(3))*support*delta)==s.zeros(3,3)
}
# Direct half-coordinate identity, without suppressing its coefficient.
anti=s.eye(3).col_join(-s.eye(3))
checks['half_coordinate_factor_four']=anti.T*support*anti==4*Bq
v=s.Matrix([1,-1,1,-1])
M=s.Matrix([[-1,0,1,0],[1,0,0,1],[0,-1,-1,0],[0,1,0,-1]])
w=s.Matrix([1,0,0,-1]);corner=s.Matrix([[1,0],[0,0],[0,0],[0,1]])
checks['derived_diagonal_d_squared_zero']=M*v==s.zeros(4,1)
checks['derived_diagonal_closed_stalks_acyclic']=M[[0,1,2],:].rank()==3 and M[[1,2,3],:].rank()==3
checks['derived_diagonal_generic_H1']=M[[1,2],:].rank()==2 and M[[1,2],:]*w==s.zeros(2,1) and v.row_join(w).rank()==2
checks['derived_diagonal_resolution_map']=M*w==corner*s.Matrix([-1,1])
checks['derived_diagonal_trace_orientation']=s.ones(1,4)*M==s.zeros(1,4) and s.ones(1,4)*corner==s.ones(1,2)
assert all(checks.values()),checks
data={'checks':checks,'count':len(checks),'scope':'Exact finite instance with A=C^4, J=C, W_+=W_-=C^4; supplements PRS proofs; not the infinite original object or an RH test.',
 'product_cohomology_dimensions':[64-d0.rank(),64-d1.rank()-d0.rank(),16-d1.rank()],
 'diagonal_H1_dimension':16-diag.rank(),'kernel_to_Q_tensor_Q_dimension':6,'scalar_pairing_kernel_dimension':14}
(H/'PRODUCT_SHEAF_EXACT_CHECKS_PRIVATE.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')

fig=plt.figure(figsize=(16,11),facecolor='white')
gs=fig.add_gridspec(3,2,height_ratios=[.14,1,.58],hspace=.25,wspace=.18)
head=fig.add_subplot(gs[0,:]);head.axis('off')
head.text(0,.8,'The original residue map comes from the product space',fontsize=21,color=navy,weight='bold')
head.text(0,.15,'Exact sheaf map on all nine stalks; ordered overlaps supply degree 2.  PRS2–PRS4',fontsize=13,color=grey)
labels=['+','\\eta','-']
for panel in range(2):
 ax=fig.add_subplot(gs[1,panel]);ax.set_xlim(-.75,2.75);ax.set_ylim(-.75,2.75);ax.axis('off')
 ax.set_title(r'$\mathcal{F}\boxtimes\mathcal{F}$' if panel==0 else r'$j_{(\eta,\eta)!}\,\chi_{\rm dil}\mathbb{C}$',fontsize=18,color=navy,pad=18)
 for x in range(3):
  for y in range(3):
   for dx,dy in ([(1-x,0)] if x!=1 else [])+([(0,1-y)] if y!=1 else []):
    ax.add_patch(FancyArrowPatch((x,y),(x+dx,y+dy),arrowstyle='-|>',mutation_scale=12,shrinkA=36,shrinkB=36,color=grey,lw=1.2,zorder=1))
   central=x==1 and y==1
   if panel==0:
    a='A' if x==1 else ('W_+' if x==0 else 'W_-')
    c='A' if y==1 else ('W_+' if y==0 else 'W_-')
    txt='$'+a+r'\otimes '+c+'$'
   else: txt=r'$\chi_{\rm dil}\mathbb{C}$' if central else '$0$'
   ax.text(x,y,txt,ha='center',va='center',color=teal if central else navy,fontsize=15 if central else 12,
       bbox={'boxstyle':'round,pad=.48','facecolor':'#e6f6f4' if central else '#f4f6f9','edgecolor':teal if central else '#c8d0da'},zorder=2)
 ax.text(1,-.53,'Every incoming restriction has a J factor.' if panel==0 else r'Generic map: $b\otimes c\mapsto\mathcal{B}_\zeta(b,c)$'+'\nAll other stalk maps are zero.',ha='center',va='center',fontsize=12,color=navy)
bot=fig.add_subplot(gs[2,:]);bot.axis('off')
lines=[
 (r'$P\otimes P\ \longrightarrow\ (P\otimes A)\oplus(A\otimes P)\ \longrightarrow\ A\otimes A$',19,navy),
 (r'$d^0(p\otimes q)=(p\otimes dq,\,dp\otimes q),\qquad d^1(x,y)=(d\otimes1)x-(1\otimes d)y$',15,navy),
 (r'$\mathcal{B}_\zeta(J,A)=\mathcal{B}_\zeta(A,J)=0\quad\Longrightarrow\quad C^\bullet\longrightarrow\chi_{\rm dil}\mathbb{C}[-2]$',16,teal),
 (r'$\Phi^1(b)(c)=\mathcal{B}_\zeta(b,c),\qquad \Phi^1=\pi^{\prime}D_\zeta\pi=\Psi_\zeta^1$',18,navy),
 ('P retains both Schwartz spaces, four endpoints, and both full extra closed copies.',12,grey),
 ('Sources: Connes–Consani 0903.2024v3 §5; Meyer math/0412277v3.  Proof: PRS0–PRS9; FTD0–FTD10.',11,grey)]
for i,(txt,size,col) in enumerate(lines):bot.text(.5,1-i*.185,txt,ha='center',va='top',fontsize=size,color=col)
fig.savefig(H/'ORIGINAL_RESIDUE_PRODUCT_SPACE.png',dpi=145,bbox_inches='tight')
fig.savefig(H/'ORIGINAL_RESIDUE_PRODUCT_SPACE.svg',bbox_inches='tight');plt.close(fig)

fig,ax=plt.subplots(figsize=(15,9),facecolor='white');ax.axis('off')
rows=[
 ('Both supports retain the entire boundary, and determine its exact radical',21,navy),
 (r'$D_Z=[P\longrightarrow A\oplus A],\qquad u^0=\mathrm{id},\quad u^1(a_+,a_-)=a_+-a_-$',17,navy),
 (r'$\mathcal{B}_Z((a_+,a_-),(b_+,b_-))$',19,teal),
 (r'$=\mathcal{B}_\zeta(a_+,b_+)-\mathcal{B}_\zeta(a_+,b_-)-\mathcal{B}_\zeta(a_-,b_+)+\mathcal{B}_\zeta(a_-,b_-)$',16,navy),
 (r'$A\ \longrightarrow\ Q\oplus Q\ \longrightarrow\ Q$',21,navy),
 (r'$a\mapsto(\pi a,\pi a),\qquad (q_+,q_-)\mapsto q_+-q_-$',18,navy),
 (r'$\operatorname{rad}_{\rm left}\mathcal{B}_Z=\operatorname{rad}_{\rm right}\mathcal{B}_Z=\Delta Q=\operatorname{im}(A\to Q^2)$',19,teal),
 (r'In retained half-coordinates: $\mathcal{B}_Z((h+k,h-k),(j+l,j-l))=4B_\zeta(k,l)$',17,navy),
 ('The radical is a subspace in a bilinear slot. It is not the kernel of the scalar map on Q tensor Q.',12,orange),
 ('Exact proof: PRS5.1–PRS5.4; original residue nondegeneracy: GZR6 with the full unshifted return.',12,grey),
 ('All additions occur in the constructed receiving vector spaces; none is assigned to primitive Z₁ / τ.',12,grey)]
for i,(txt,size,col) in enumerate(rows):ax.text(.5,1-i*.093,txt,ha='center',va='top',fontsize=size,color=col)
fig.savefig(H/'BOTH_SUPPORTS_RESIDUE_RADICAL.png',dpi=145,bbox_inches='tight')
fig.savefig(H/'BOTH_SUPPORTS_RESIDUE_RADICAL.svg',bbox_inches='tight');plt.close(fig)

fig=plt.figure(figsize=(15,10),facecolor='white')
gs=fig.add_gridspec(2,2,height_ratios=[1,.78],hspace=.30,wspace=.2)
left=fig.add_subplot(gs[0,0]);left.axis('off');left.set_xlim(-.65,2.65);left.set_ylim(-1.2,2.7)
left.set_title('The exact map q on all nine points',fontsize=17,color=navy,pad=16)
for x in range(3):
 for y in range(3):
  target=r'$c_+$' if x==y==0 else (r'$c_-$' if x==y==2 else r'$\eta$')
  col=orange if x==y==0 or x==y==2 else teal
  left.text(x,y,target,ha='center',va='center',fontsize=18,color=col,bbox={'boxstyle':'round,pad=.65','facecolor':'#f5f7fa','edgecolor':col})
left.text(1,-.72,r'$q(c_+,c_+)=c_+,\quad q(c_-,c_-)=c_-$'+'\nAll other points map to '+r'$\eta$.',ha='center',fontsize=12,color=navy)
left.text(1,-1.12,r'Both axes: $c_+,\eta,c_-$, reading rightward and upward.',ha='center',fontsize=11,color=grey)
right=fig.add_subplot(gs[0,1]);right.axis('off')
rr=[(r'$\Delta(x)=(x,x),\qquad q\Delta=\mathrm{id}_Y$',20,navy),
 (r'$\Delta_*\mathcal{G}=q^{-1}\mathcal{G}$',23,teal),
 (r'$R\Delta^!=Rq_*$',23,teal),
 ('The equality follows from every original stalk',13,navy),
 ('and restriction; it is not a closed-embedding claim.',13,navy),
 (r'$K=j_{(\eta,\eta)!}\chi_{\rm dil}\mathbb{C}$',20,navy)]
for i,(txt,size,col) in enumerate(rr):right.text(.5,.92-i*.145,txt,ha='center',va='top',fontsize=size,color=col)
ax=fig.add_subplot(gs[1,:]);ax.axis('off')
rr=[(r'$R\Delta^!K=\left[I_\eta\longrightarrow I_\eta^4\longrightarrow I_+\oplus I_\eta^2\oplus I_-\right]\otimes\chi_{\rm dil}$',21,navy),
 ('Degrees 0, 1, 2; all maps and signs are retained in the proof.',13,grey),
 (r'Closed stalks: acyclic.  Generic stalk: $\chi_{\rm dil}\mathbb{C}[-1]$.',17,navy),
 (r'$R\Delta^!K\simeq j_{\eta!}\chi_{\rm dil}\mathbb{C}[-1],\qquad R\Gamma(Y,R\Delta^!K)=\chi_{\rm dil}\mathbb{C}[-2]$',21,teal),
 ('The full derived return recovers the product trace with coefficient +1.',15,navy),
 ('Proof: DIAGONAL_EXTRAORDINARY_RETURN.md.  Source topology: Connes–Consani 0903.2024v3 §5.',11,grey),
 ('This is the computed receiving duality operation; no numerical weight is assigned to primitive τ.',12,grey)]
for i,(txt,size,col) in enumerate(rr):ax.text(.5,1-i*.16,txt,ha='center',va='top',fontsize=size,color=col)
fig.suptitle('The derived diagonal return retains the original trace',fontsize=22,color=navy,weight='bold',y=1.04)
fig.savefig(H/'DERIVED_DIAGONAL_TRACE_RETURN.png',dpi=145,bbox_inches='tight')
fig.savefig(H/'DERIVED_DIAGONAL_TRACE_RETURN.svg',bbox_inches='tight');plt.close(fig)
fig,ax=plt.subplots(figsize=(15,11),facecolor='white');ax.axis('off')
ax.set_xlim(0,1);ax.set_ylim(0,1)
ax.text(.5,.98,'The full arithmetic return is a correspondence',ha='center',va='top',fontsize=22,color=navy,weight='bold')
ax.text(.5,.918,r'$X=\operatorname{Spec}\mathbb{Z}\,\cup\{\mathfrak{m}_+,\mathfrak{m}_-\},\qquad f:X\longrightarrow Y$',ha='center',fontsize=18,color=navy)
nodes=[(.16,.78,r'$X^2$'),(.50,.78,r'$\mathcal{Z}$'),(.84,.78,r'$X$'),(.16,.56,r'$Y^2$'),(.50,.56,r'$Y$'),(.84,.56,r'$Y$')]
for x,y,t in nodes:ax.text(x,y,t,ha='center',va='center',fontsize=25,color=navy,bbox={'boxstyle':'round,pad=.35','facecolor':'#f4f6f9','edgecolor':'#c8d0da'})
edges=[((.50,.78),(.16,.78),'a',(.33,.81)),((.50,.78),(.84,.78),'b',(.67,.81)),((.16,.78),(.16,.56),r'f\times f',(.09,.67)),((.50,.78),(.50,.56),'g',(.53,.67)),((.84,.78),(.84,.56),'f',(.88,.67)),((.16,.56),(.50,.56),'q',(.33,.59)),((.84,.56),(.50,.56),r'\mathrm{id}',(.67,.59))]
for start,end,label,pos in edges:
 ax.add_patch(FancyArrowPatch(start,end,arrowstyle='-|>',mutation_scale=15,shrinkA=25,shrinkB=25,lw=1.5,color=teal))
 ax.text(*pos,'$'+label+'$',ha='center',va='center',fontsize=16,color=teal)
rows=[(.45,r'$\mathcal{Z}=\{(x,y,z):f(z)=q(f(x),f(y))\},\qquad \delta_X(x)=(x,x,x)$',18,navy),
 (.37,r'$a\delta_X=\Delta_X,\qquad b\delta_X=\mathrm{id}_X$',20,teal),
 (.29,r'$a^{-1}(\mathfrak{m}_\pm,\mathfrak{m}_\pm)=\{(\mathfrak{m}_\pm,\mathfrak{m}_\pm,\mathfrak{m}_\pm)\}$',17,navy),
 (.22,r'Every other fibre of $a$ is the full $\operatorname{Spec}\mathbb{Z}$.',17,navy),
 (.13,r'$Ra_*b^{-1}f^{-1}\mathcal{G}\ \cong\ (f\times f)^{-1}\Delta_{Y*}\mathcal{G}$',22,teal),
 (.066,'FSC3–FSC6: exact in bounded complexes of algebraic sheaves of complex vector spaces.',12,grey),
 (.025,'Source topology: Connes–Consani 0903.2024v3 §5 and the constructed source comparison DCP.',11,grey)]
for y,txt,size,col in rows:ax.text(.5,y,txt,ha='center',va='center',fontsize=size,color=col)
fig.savefig(H/'FULL_SOURCE_DERIVED_CORRESPONDENCE.png',dpi=145,bbox_inches='tight')
fig.savefig(H/'FULL_SOURCE_DERIVED_CORRESPONDENCE.svg',bbox_inches='tight');plt.close(fig)
fig,ax=plt.subplots(figsize=(16,11),facecolor='white');ax.axis('off')
rows=[('The degree-one mixed obstruction has an explicit contraction',22,navy),
 (r'$s_+(j)=(\Sigma^{-1}j,0,0),\qquad r_+s_+=\mathrm{id}_J$',21,teal),
 (r'$M=(J\otimes Q)\oplus(Q\otimes J),\qquad Q_\Delta=(A\otimes A)/(J\otimes J)$',19,navy),
 (r'$S(m_1,m_2)=(-(s_+\otimes1)m_1,\ (1\otimes s_+)m_2,\ 0,\ 0)$',19,navy),
 (r'$d_M S=\mathrm{id}_M,\qquad p=\mathrm{id}_{C^0}-Sd_M$',22,teal),
 (r'$[C^0\longrightarrow Q_\Delta]\ \overset{(p,\vartheta)}{\longrightarrow}\ [K_0\overset{0}{\longrightarrow}Q\otimes Q]$',23,navy),
 (r'Exact kernel: $[S(M)\overset{d}{\longrightarrow}\iota(M)]$, with $h^1(\iota m)=Sm$.',20,teal),
 (r'$dh+hd=\mathrm{id}$ on the entire kernel',20,navy),
 (r'$P(L_{\rm tot})z=\iota m\quad\Longrightarrow\quad P(L_{\rm tot})z=d(Sm)$',22,teal),
 ('A generic polynomial obstruction becomes this explicit global boundary.',15,navy),
 (r'$K_0=(H\otimes Q)\oplus(Q\otimes H)$ retains all endpoint and extra closed copies.',16,navy),
 ('The maps intertwine the original simultaneous dilation and every prime specialization.',14,grey),
 ('Proof: GMC0–GMC7. Algebraic tensor cohomology; no completed-tensor or numerical purity claim.',12,grey),
 ('Source: Connes–Consani 0903.2024v3 §5; exact inverse and derived return: SSI, DCP, DER.',11,grey)]
for i,(txt,size,col) in enumerate(rows):ax.text(.5,1-i*.073,txt,ha='center',va='top',fontsize=size,color=col)
fig.savefig(H/'GLOBAL_MIXED_RETURN_CONTRACTION.png',dpi=145,bbox_inches='tight')
fig.savefig(H/'GLOBAL_MIXED_RETURN_CONTRACTION.svg',bbox_inches='tight');plt.close(fig)
print(json.dumps({'checks':len(checks),'passed':all(checks.values()),'figures':['ORIGINAL_RESIDUE_PRODUCT_SPACE.png','BOTH_SUPPORTS_RESIDUE_RADICAL.png','DERIVED_DIAGONAL_TRACE_RETURN.png','FULL_SOURCE_DERIVED_CORRESPONDENCE.png','GLOBAL_MIXED_RETURN_CONTRACTION.png']}))
