from pathlib import Path
import json
gw=Path(__file__).resolve().parent
p=gw/'CUT22_DISPLAY_REFLOWS.json'
r=[]
def add(file,before,after):r.append(dict(file=file,before=before,after=after,purpose='typesetting only; all mathematical symbols and words retained'))
for name in ['independent_contiguous.tex','GAMMA_ENSEMBLE_LEADING_RETURN.tex','EXACT_SQRT_LOG_EQUILIBRIUM.tex']:
    add('HBL.tex','\\texttt{'+name.replace('_','\\_')+'}','\\par\\noindent\\nolinkurl{'+name+'}')
add('IKO.tex','$\\mathsf E_\\chi(p_{N+j})/\\sqrt{\\gamma_{N+j}}$,','\\[\\mathsf E_\\chi(p_{N+j})/\\sqrt{\\gamma_{N+j}},\\]')
add('IKO.tex','$B=K_{\\chi,f_L;N+L}K_{f_L,N+L}^{-1/2}$.','\\[B=K_{\\chi,f_L;N+L}K_{f_L,N+L}^{-1/2}.\\]')
add('MFG.tex','$\\int y^{2q+i+j}\\Phi_L(y)d\\sigma(y)$.','\\[\\int y^{2q+i+j}\\Phi_L(y)d\\sigma(y).\\]')
add('MFG.tex','$\\cos(\\arctan z+\\arctan w)=(1-zw)/\\sqrt{(1+z^2)(1+w^2)}$','\\[\\cos(\\arctan z+\\arctan w)=(1-zw)/\\sqrt{(1+z^2)(1+w^2)}\\]')
add('KPR.tex',' M_1=\\int\\sqrt x\\,\\rho_0(x)dx=6/\\pi,\\qquad\n M_2=\\int x\\,\\rho_0(x)dx,\\qquad\n M_3=\\int x^{3/2}\\rho_0(x)dx,\n \\quad\\mathcal L=\\int\\log x\\,\\rho_0(x)dx.',' \\begin{gathered}\n M_1=\\int\\sqrt x\\,\\rho_0(x)dx=6/\\pi,\\qquad\n M_2=\\int x\\,\\rho_0(x)dx,\\\\\n M_3=\\int x^{3/2}\\rho_0(x)dx,\n \\quad\\mathcal L=\\int\\log x\\,\\rho_0(x)dx.\n \\end{gathered}')
add('QLG.tex',r'\(2a_*^{-1/2}\int_0^{\pi/2}\sin^2\theta\,d\theta\).',r'\[2a_*^{-1/2}\int_0^{\pi/2}\sin^2\theta\,d\theta.\]')
add('IES.tex',r'$[M_1(\cosh\xi)^{-1/2}]^k'+'\n'+r'=M_k(\cosh\xi)^{-k/2}$,',r'\[[M_1(\cosh\xi)^{-1/2}]^k'+'\n'+r'=M_k(\cosh\xi)^{-k/2},\]')
add('IES.tex',r'$|\int hw\,du|^2\leq p(Y)\int|h|^2w\,du$.',r'\[|\int hw\,du|^2\leq p(Y)\int|h|^2w\,du.\]')
ies=(gw/'intrinsic_order_20260914/INTRINSIC_EXTERIOR_GAMMA_ORDER.tex').read_text(encoding='utf-8')
for tag in ['IGO3','IGO6','IGO8','IGO9']:
    end=ies.index(' \\tag{'+tag+'}')
    start=ies.rfind('\\[\n',0,end)+3
    before=ies[start:end]
    after=before.replace('\\qquad','\\\\').replace('\\quad','\\qquad')
    # The two final definitions in IGO6 stay on their own row.
    if tag=='IGO6':after=after.replace('\\qquad \\nu_', '\\\\\n \\nu_')
    add('IES.tex',before,' \\begin{gathered}\n'+after+' \\end{gathered}\n')
before=r''' \ker U_r^*&=\left\{h\in\mathcal H_\lambda:
    \int_{\mathbb R^{r-1}}h(u,Y-\textstyle\sum u_j)
     w_{\chi,s,r}(u,Y-\textstyle\sum u_j)\,du=0
      \text{ for almost every }Y\right\},\\'''
after=r''' \ker U_r^*&=\Bigl\{h\in\mathcal H_\lambda:\\
 &\quad\int_{\mathbb R^{r-1}}h(u,Y-\textstyle\sum u_j)
     w_{\chi,s,r}(u,Y-\textstyle\sum u_j)\,du=0\\
 &\quad\text{ for almost every }Y\Bigr\},\\'''
add('IES.tex',before,after)
p.write_bytes(json.dumps(r,indent=2).encode())
