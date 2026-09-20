from pathlib import Path
import re,json,subprocess,shutil
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch

P=Path(__file__).parent
fig,ax=plt.subplots(figsize=(10.2,12.8));ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis('off')
colors={'ink':'#18334a','blue':'#e5eff7','gold':'#fff0ce','green':'#e4f0e7','red':'#f7e6e2'}
def box(x,y,w,h,text,color,size=13):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.013',linewidth=1,edgecolor=colors['ink'],facecolor=colors[color]))
    text=re.sub(r'\\le(?![a-zA-Z])',r'\\leq ',text)
    text=re.sub(r'\\ge(?![a-zA-Z])',r'\\geq ',text)
    ax.text(x+w/2,y+h/2,text,ha='center',va='center',fontsize=size,color=colors['ink'],linespacing=1.6)
def arrow(x,y,X,Y):ax.add_patch(FancyArrowPatch((x,y),(X,Y),arrowstyle='-|>',mutation_scale=14,color=colors['ink']))
ax.text(.5,.975,'The original determinant retains both spectral extremes',ha='center',va='top',fontsize=17,weight='bold',color=colors['ink'])
box(.05,.81,.90,.11,'Original quotient and its attained metric\n'+r'$E=\mathbb{C}[y]/(Q),\quad G_N,\quad M=C_N+r_N\ell_N$'+'\n'+r'$C_N^{\dagger}=C_N,\quad\ell_Nr_N=0$', 'blue')
arrow(.5,.805,.5,.758)
box(.05,.59,.90,.16,'EXACT FINITE IDENTITY  (SD5)\n'+r'$\det(M^{\dagger}M+a^2 I)$'+'\n'+r'$=|Q(ia)|^2+a^2|p_N^C(ia)|^2 A_aB_a$'+'\n'+r'$A_a=r_N^{\dagger}(C_N^2+a^2I)^{-1}r_N$'+'\n'+r'$B_a=\ell_N(C_N^2+a^2I)^{-1}\ell_N^{\dagger}$','green',13)
arrow(.3,.585,.3,.525);arrow(.7,.585,.7,.525)
box(.05,.39,.43,.13,'Full original roots\n'+r'$\prod_{j=1}^{q}s_j(M)^2=|Q(0)|^2$'+'\n'+'Every multiplicity remains.\nThe product is independent of N.','blue',12)
box(.52,.39,.43,.13,'Original boundary term\n'+r'$\kappa_N=\Vert r_N\Vert_{G_N}\Vert\ell_N^{\dagger}\Vert_{G_N}$'+'\n'+r'$J_k^{\mathrm{action}}=\sum_Nw_N\log\kappa_N^2$'+'\n'+'The action enters through this term.','gold',12)
arrow(.3,.38,.3,.322);arrow(.7,.38,.7,.322)
box(.05,.15,.90,.16,'PROVED SPECTRAL CONSEQUENCES  (SD11–12, SD21–22)\n'+r'$|s_1(M)-\kappa_N|\le Bq,\qquad\kappa_N\ge q^2/(192B)$'+'\n'+r'$s_j(M)\le Bq\quad(j\ge2)$'+'\n'+r'$s_q(M)/q\le q^{-A}\quad\mathrm{for\ every\ fixed}\ A>0$'+'\n'+'The last bound holds eventually, uniformly over the original window.','red',13)
ax.text(.5,.095,'Why the small values are forced: the determinant fixes the product,\nwhile the proved Gaussian bulk remains at scale q.',ha='center',fontsize=11,color=colors['ink'],linespacing=1.5)
ax.text(.5,.022,'All adjoints and norms use G_N.  a > 0; q−1 ≤ N ≤ 2q−1.\nB = 5 max{1, C_mult(h)}.  Fixed original h, δ, γ and m₀.\nExact identities and bounds, not a simulated spectrum. No effective k threshold is claimed.',ha='center',fontsize=9.5,color=colors['ink'],linespacing=1.5)
fig.savefig(P/'SPECTRAL_DETERMINANT_MECHANISM.png',dpi=170,bbox_inches='tight',facecolor='white');plt.close(fig)

new=(P/'ORIGINAL_SPECTRAL_DETERMINANT.tex').read_text(encoding='utf-8')
figure=r'''
\clearpage
\begin{figure}[p]\centering
\includegraphics[width=\textwidth,height=.89\textheight,keepaspectratio]{SPECTRAL_DETERMINANT_MECHANISM.png}
\caption{The complete connection in the original metric. SD5 retains the full
root polynomial and both boundary resolvent energies. SD11--12 isolates the
large singular value, SD21 gives a finite bound for the smallest one, and
SD22 proves its eventual decay below every inverse power. The same source
and relation spectral laws NG1--27 and GM1--25 are reproduced in the
appendices. Their human formula sources include Forrester/Andr\'eief,
Koornwinder and coauthors, Carlson and Johansson, cited at their uses.
No individual projected-current sign is inferred.}
\end{figure}\clearpage
'''
new=new.replace('\\begin{thebibliography}{9}',figure+'\\begin{thebibliography}{9}',1)
bodies=[]
for name,title,path in [
 ('NG','Complete original arithmetic Gaussian transfer',P.parent/'NATIVE_GAUSSIAN_TRANSFER.tex'),
 ('GM','Complete independent equilibrium and moment proof',P.parent/'independent_moments/GAUSSIAN_EQUILIBRIUM_MOMENTS.tex')]:
    if not path.exists():path=P/path.name
    src=path.read_text(encoding='utf-8')
    if path.parent!=P:shutil.copy2(path,P/path.name)
    body=src.split('\\begin{document}\\maketitle',1)[1].split('\\end{document}',1)[0]
    body=body.replace('received 20 September 2026, SHA256\n'+r'\texttt{44b9591515c12b07d065f8a4fc4b3b9dd9c30b5c85f334b70d325aaeaf0880ac}.','received 20 September 2026; exact hash recorded in the source ledger.')
    if name=='NG':
        body=body.replace('\\bibitem{incoming}','\\bibitem{NGincoming}').replace('\\cite{incoming}','\\cite{NGincoming}')
    bodies.append('\\clearpage\n\\section*{'+title+'}\n'+body)
combined=new.replace('\\end{document}','\\appendix\n'+'\n'.join(bodies)+'\n\\end{document}')
bibs=re.findall(r'\\begin\{thebibliography\}\{9\}(.*?)\\end\{thebibliography\}',combined,flags=re.S)
combined=re.sub(r'\\begin\{thebibliography\}\{9\}.*?\\end\{thebibliography\}','',combined,flags=re.S)
combined=combined.replace('\\end{document}','\\clearpage\n\\begin{thebibliography}{99}\n'+'\n'.join(bibs)+'\n\\end{thebibliography}\n\\end{document}')
(P/'SPECTRAL_DETERMINANT_COMPLETE.tex').write_text(combined,encoding='utf-8')
logs=[]
for _ in range(2):
    r=subprocess.run(['pdflatex','-interaction=nonstopmode','-halt-on-error','SPECTRAL_DETERMINANT_COMPLETE.tex'],cwd=P,capture_output=True,text=True)
    logs.append(r.stdout)
    if r.returncode:print(r.stdout[-6500:]);raise SystemExit(r.returncode)
(P/'BUILD_STDOUT.txt').write_text('\n'.join(logs),encoding='utf-8')
warnings=[x for x in logs[-1].splitlines() if any(y in x for y in ['Overfull','Underfull','Warning','Output written'])]
print('\n'.join(warnings))
qa=P/'qa';qa.mkdir(exist_ok=True)
for pattern in ['page-*.png','sheet-*.png']:
    for old in qa.glob(pattern):
        if old.resolve().parent!=qa.resolve():raise RuntimeError('QA path escaped its directory')
        old.unlink()
r=subprocess.run(['pdftoppm','-r','80','-png',str(P/'SPECTRAL_DETERMINANT_COMPLETE.pdf'),str(qa/'page')],capture_output=True,text=True)
if r.returncode:raise RuntimeError(r.stderr)
from PIL import Image,ImageOps,ImageDraw
pages=sorted(qa.glob('page-*.png'))
for start in range(0,len(pages),6):
    sheet=Image.new('RGB',(1200,1750),'#d0d0d0')
    for j,p in enumerate(pages[start:start+6]):
        im=Image.open(p).convert('RGB');im.thumbnail((580,550))
        x=(j%2)*600+(600-im.width)//2;y=(j//2)*583+25
        sheet.paste(im,(x,y));ImageDraw.Draw(sheet).text(((j%2)*600+12,(j//2)*583+7),p.stem,fill='black')
    sheet.save(qa/f'sheet-{start//6+1}.png')
print(json.dumps({'pages':len(pages),'sheets':len(list(qa.glob('sheet-*.png'))),'warnings':warnings}))
