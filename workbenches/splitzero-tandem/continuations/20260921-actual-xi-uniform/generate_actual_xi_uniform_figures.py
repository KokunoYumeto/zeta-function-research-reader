"""Reproducible scientific diagrams of AUH/RXT and RUC/RCM.

All diagrams show exact maps or interval results, not numerical root loci.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

B=Path(__file__).resolve().parent
O=B/'figures_actual_xi_uniform'; O.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'mathtext.fontset':'dejavusans'})
ink='#142d40'; blue='#235e91'; teal='#176c61'; red='#a53d42'; pale='#f2f6f8'

def box(ax,x,y,w,h,txt,color=blue,fs=13):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.012',
                 linewidth=1.5,edgecolor=color,facecolor=pale))
    ax.text(x+w/2,y+h/2,txt,ha='center',va='center',fontsize=fs,color=ink)

def arrow(ax,x1,y1,x2,y2):
    ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle='-|>',mutation_scale=18,
                                linewidth=1.5,color=ink))

def save(fig,name):
    for ext in ('png','svg'):
        fig.savefig(O/f'{name}.{ext}',dpi=190,bbox_inches='tight',facecolor='white')
    plt.close(fig)

fig=plt.figure(figsize=(14,8.4)); ax=fig.add_axes([.03,.03,.94,.92]); ax.set_axis_off()
ax.text(.5,.985,'The actual Xi data decide which unit enters the conductor',
        ha='center',va='top',fontsize=20,color=ink,weight='bold')
box(ax,.015,.69,.275,.205,
    'Four unchanged marks\n'+r'$\rho_M=3/4+3i,\quad\rho_N=3/4-3i$'+'\n'+
    r'$\rho_T=1/4+3i,\quad\rho_E=1/4-3i$'+'\n'+r'$g=2\xi$',fs=12)
box(ax,.365,.69,.27,.205,
    'Exact residual and quotient\n'+r'$2\xi(s)=L(w^2)+h(s)Q(w^2)$'+'\n'+
    r'$a_+=Q((1/4+3i)^2)$'+'\nAUH3-8: values and derivatives',fs=12)
box(ax,.71,.69,.275,.205,
    'Full original period matrix\n'+r'$H=e^{\mathfrak{a}/u}G_u\mathcal{R}V^{-1}U$'+'\n'+
    r'$B_j=H^{-1}D_jH$'+'\nAUH20-26: every factor retained',fs=12)
arrow(ax,.298,.793,.353,.793); arrow(ax,.643,.793,.699,.793)
ax.text(.015,.642,'Same quartet and same certified real period interval; two different unit inputs',
        fontsize=14,color=ink,weight='bold')
box(ax,.015,.34,.45,.25,
    'Certified geometric member (RPZ)\n'+r'$x_*\in[-1.466817440464,-1.466817440462]$'+'\n'+
    r'$\mu_0=\mu_1=0,\quad\mu_2>0$'+'\nOld fixed-domain matrix is singular\nActual quotient uses order 2',red,13)
box(ax,.535,.34,.45,.25,
    'Xi-derived extension (RXT4-8)\n'+r'$0.01020<x_\Xi<0.01022$'+'\n'+
    r'$0.0073504212<\mu_0^\Xi<0.0073504216$'+'\n'+
    r'$\det B_{D,s}^\Xi=(\mu_0^\Xi)^{D+1}>0$'+'\nOrder 0 at every finite cutoff',teal,13)
box(ax,.015,.105,.97,.16,
    r'An actual zero quartet also requires $L=0$, not merely a chosen unit phase.'+'\n'+
    r'Here $\ell_0>0.975$ and $\ell_1>0.0188$ throughout '+
    r'$|\delta-1/4|,|\gamma-3|\leq10^{-8}$.'+'\n'+
    'This rectangle has no such quartet. Conductor-factor bounds above use the fixed quartet only.',teal,13)
ax.text(.5,.033,'Origin: Levent Alpöge’s announcement, crediting Akhil and Fable; four-mark extension: ES reader.\n'
        'Exact maps: ALF1-3, AUH1-30, RXT1-9; original family: PCL1-10.\n'
        'Riemann completion: Apostol, DLMF Ch. 25; interval arithmetic: Johansson, Arb, arXiv:1611.02831v1.\n'
        'Schematic box positions. Full primary-source links and proof locators accompany this figure.',
        ha='center',va='center',fontsize=10,color=ink)
save(fig,'39_actual_xi_pullback')

fig=plt.figure(figsize=(14,8.4)); ax=fig.add_axes([.03,.03,.94,.92]); ax.set_axis_off()
ax.text(.5,.985,'Two spectral roots control two leading inverse rates',
        ha='center',va='top',fontsize=20,color=ink,weight='bold')
box(ax,.10,.77,.8,.135,
    r'$g(t,p)=U(t,p)(t-\alpha)(t-\beta),\quad F=1/U$'+'\n'+
    r'$0<r=\min(|\alpha|,|\beta|)\leq s_r=\max(|\alpha|,|\beta|)<R<1$',fs=15)
box(ax,.025,.46,.435,.205,
    'Both principal parts, including coalescence\n'+
    r'$h_n=P_n+e_n,\qquad |e_n|\leq C_RR^{-n}$'+'\n'+
    r'$P_nP_{n+2}-P_{n+1}^2=-\frac{F(\alpha)F(\beta)}{(\alpha\beta)^{n+3}}$'+'\n'+
    'A cancelled coefficient cannot cancel this determinant.',fs=12)
box(ax,.54,.46,.435,.205,
    'Full finite matrix, including lower correction\n'+
    r'$T_D(h)=\mathcal{P}_D+\mathcal{E}_D-\mathcal{L}_D$'+'\n'+
    r'$\operatorname{rank}\mathcal{P}_D\leq2$'+'\n'+
    r'$\|\mathcal{E}_D\|\leq C_RR^{-D}/(1-R),\quad\|\mathcal{L}_D\|\leq K_-$',fs=12)
arrow(ax,.34,.762,.25,.678); arrow(ax,.66,.762,.75,.678)
box(ax,.025,.195,.95,.175,
    r'$\lim_{D\to\infty}\sigma_1(B_{D,s}^{-1})^{1/D}=r^{-1},\qquad'
    r'\lim_{D\to\infty}\sigma_2(B_{D,s}^{-1})^{1/D}=s_r^{-1}$'+'\n\n'+
    r'$\lim_{D\to\infty}\frac{1}{D}\sum_{j=3}^{D+1}\log\sigma_j(B_{D,s}^{-1})=-\log|U(0,p)|$',teal,16)
arrow(ax,.25,.448,.32,.382); arrow(ax,.75,.448,.68,.382)
ax.text(.5,.105,
    'The parameter p is fixed and invertible. Both roots may coincide away from zero.\n'+
    r'Original Gamma weights stay: $B^{-1}=D_\rho^{-1}T_D(h)D_\rho$; '+
    r'$s_D\log(D+1)/D\to0$ covers all four original $D_i=\Theta(a_{\rm amp}^2)$ endpoints.',
    ha='center',va='center',fontsize=11,color=ink)
ax.text(.5,.013,'Origin: Levent Alpöge’s announcement, crediting Akhil and Fable; four-mark extension: ES reader.\n'
        'RUC1-30 and RCM1-17; exact local factorization RLA6-10; preceding principal-part mechanism WCF15-18.\n'
        'All corrections and unit terms are retained. Full primary-source links accompany this figure.',
        ha='center',va='center',fontsize=10,color=ink)
save(fig,'40_uniform_inverse_rates')
print('Saved two exact map diagrams with PNG, SVG and reproducible source.')
