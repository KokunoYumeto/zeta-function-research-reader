"""Exact maps and interval identities from OZC17, OZC35–48 and OZK18.

The interval panel is schematic; no sampled zeta zeros enter the figure.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

P = Path(__file__).resolve().parent
fig, ax = plt.subplots(figsize=(12, 11), facecolor='white')
ax.set_xlim(0,12); ax.set_ylim(0,11); ax.axis('off')
ink='#153449'; green='#0a7678'; red='#a94528'
def text(x,y,s,size=14,**kw): ax.text(x,y,s,fontsize=size,color=ink,**kw)
def box(x,y,w,h,c='#edf5f6'):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.12',facecolor=c,edgecolor=ink,lw=1.1))
def arrow(x,y,X,Y):
    ax.add_patch(FancyArrowPatch((x,y),(X,Y),arrowstyle='-|>',mutation_scale=17,lw=1.7,color=green))

text(6,10.65,'Original zeta: the full trace and its exact return',19,ha='center',weight='bold')
text(.15,9.95,'1. Keep both the original signed divisor and its correction',15,weight='bold')
text(6,9.35,r'$R_\zeta(A)=\sum_\rho m_\rho A(\rho)+\sum_{m\geq1}A(-2m)-A(1)$',18,ha='center')
text(6,8.77,r'$E_C(A)=A(1)-\sum_{m\geq1}A(-2m),\qquad Q_\zeta(A)=R_\zeta(A)+E_C(A)$',16,ha='center')
box(.6,7.62,3.2,.63); box(8.2,7.62,3.2,.63)
text(2.2,7.86,r'$(R_\zeta,E_C)$',18,ha='center')
text(9.8,7.86,r'$(Q_\zeta,E_C)$',18,ha='center')
arrow(4.05,8.08,7.95,8.08); arrow(7.95,7.74,4.05,7.74)
text(6,8.3,r'$(R,E)\mapsto(R+E,E)$',12,ha='center')
text(6,7.3,r'$(Q,E)\mapsto(Q-E,E)$',12,ha='center')
text(6,6.88,'Rational tests: convergent sums; resonances use the specified local finite part.  OZK3–18',11,ha='center')
ax.axhline(6.52,xmin=.02,xmax=.98,color='#b8c7d0')
text(.15,6.05,'2. On the unchanged compact test, the omitted term is explicit',15,weight='bold')
text(6,5.48,r'$r=1/64,\quad d=2r=1/32,\quad A_a(s)=e^{a(s-1/2)}[s(s-1)G_r(s-1/2)]^2$',15,ha='center')
text(6,4.96,r'$U(a)=\sum_{m\geq1}A_a(-2m)>0,\qquad J_0(a)=K_0(a)+U(a)=-P_r(a)$',16,ha='center')
text(6,4.4,'This full sum exists exactly for a ≥ d.  The pole term is −Aₐ(1) = 0.  OZC35–38',11,ha='center')
box(.5,2.78,5.05,1.3); box(6.4,2.78,5.05,1.3,c='#fff1e9')
text(3.02,3.73,r'$d\leq a\leq\log 2-d$',16,ha='center')
text(3.02,3.26,r'$P_r(a)=0,\quad J_0(a)=0$',15,ha='center')
text(3.02,2.91,r'$K_0(a)=-U(a)<0$',15,ha='center')
text(8.92,3.73,r'$\log 2+d\leq a\leq583/800$',16,ha='center')
text(8.92,3.26,r'$J_0(a)=0$',15,ha='center')
text(8.92,2.91,r'$\partial_t J_t(a)|_{0+}<-286628/27$',15,ha='center')
text(6,2.34,'Exact interval statements; boxes are schematic, not a scale drawing.  OZC38, 43–46',11,ha='center')
text(6,1.82,r'$P_r(a)=\sum_{n\geq2}\Lambda(n)n^{-1/2}h_r(a-\log n),\qquad h_r=(D^2-1/4)^2(b_r*b_r)$',14,ha='center')
text(6,1.34,'The prime expression is at time zero. The full heat derivative retains every Gamma and mixed-prime term.',11,ha='center')
text(6,.75,r'$e_L=(0,1_L)\neq\tau_L=(0,0_L)$; every lower support coordinate remains.  OZC47–48',12,ha='center')
text(6,.18,'These are trace identities. Positivity of every compensated Weil test remains unproved.',12,ha='center',weight='bold')
fig.savefig(P/'original_zeta_trace_return.png',dpi=160,bbox_inches='tight')
fig.savefig(P/'original_zeta_trace_return.svg',bbox_inches='tight')
print('Saved original_zeta_trace_return.png and .svg')
