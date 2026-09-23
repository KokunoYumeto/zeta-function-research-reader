from pathlib import Path
import hashlib, io, json, tarfile
import requests
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

ROOT=Path(__file__).resolve().parent
INPUTS=ROOT/'inputs'
INPUTS.mkdir(exist_ok=True)
cases=[
 ('1502.05585v2',INPUTS/'1502.05585v2_F1_corr.tex'),
 ('2606.06604v1',INPUTS/'2606.06604v1_FF.tex')]
receipts=[]
for version,local in cases:
    archive=INPUTS/(version+'.tar.gz')
    url='https://arxiv.org/src/'+version
    if not archive.exists():
        response=requests.get(url,timeout=90)
        response.raise_for_status()
        archive.write_bytes(response.content)
    raw=archive.read_bytes()
    with tarfile.open(fileobj=io.BytesIO(raw),mode='r:*') as tf:
        matches=[m for m in tf.getmembers() if m.isfile() and Path(m.name).name==local.name]
        if len(matches)!=1:
            raise RuntimeError((version,[m.name for m in matches]))
        original=tf.extractfile(matches[0]).read()
    identical=original==local.read_bytes() if local.exists() else None
    original_path=INPUTS/(version+'_'+local.name)
    original_path.write_bytes(original)
    receipts.append(dict(canonical_source_id='arXiv:'+version,
        authors=['Alain Connes','Caterina Consani'],url=url,
        archive=str(archive),archive_sha256=hashlib.sha256(raw).hexdigest(),
        source=str(original_path),source_sha256=hashlib.sha256(original).hexdigest(),
        local_source=str(local),identical=identical,member=matches[0].name))
(ROOT/'GAMMA_FF_SOURCE_RECEIPTS.json').write_text(json.dumps(receipts,indent=2),encoding='utf-8')
if any(x['identical'] is False for x in receipts):
    raise RuntimeError('At least one local source differs: inspect receipt and compare before using version citation.')

plt.rcParams.update({'font.size':11,'font.family':'DejaVu Sans','svg.fonttype':'none'})
fig,grid=plt.subplots(2,2,figsize=(8,8.9))
axs=list(grid.flat)[:3]
diamond=[(1,0),(0,1),(-1,0),(0,-1)]
hexagon=[(1,0),(1,-1),(0,-1),(-1,0),(-1,1),(0,1)]
for ax in axs[:2]:
    ax.axhline(0,color='#949da9',lw=.6)
    ax.axvline(0,color='#949da9',lw=.6)
    ax.set(xlim=(-1.45,1.45),ylim=(-1.45,1.45),aspect='equal',xlabel=r'$a_1$',ylabel=r'$a_2$')
    ax.set_xticks([-1,0,1]); ax.set_yticks([-1,0,1])
axs[0].add_patch(Polygon(diamond,facecolor='#c9deee',edgecolor='#235c8c',lw=2))
axs[0].set_title('Earlier integer unit ball\n'+r'$|a_1|+|a_2|\leq1$')
axs[1].add_patch(Polygon(hexagon,facecolor='#f5dfad',edgecolor='#a56f11',lw=2))
axs[1].set_title('Later all-subset module\n'+r'$P(a)\leq1,\ N(a)\leq1$')
for ax,points in zip(axs[:2],[diamond+[(0,0)],hexagon+[(0,0)]]):
    for x,y in points:
        ax.plot(x,y,'o',color='#142b43',ms=6)
    ax.annotate(r'$L^2$',(0,0),xytext=(.18,.20),fontsize=12,
                arrowprops=dict(arrowstyle='-',color='#142b43'))
    ax.annotate(r'$L$',(1,0),xytext=(1.13,.28),fontsize=12,
                arrowprops=dict(arrowstyle='-',color='#142b43'))
axs[1].annotate(r'$(1,-1)\mapsto e$',(1,-1),xytext=(-.5,-1.32),fontsize=11,
                arrowprops=dict(arrowstyle='->',color='#a12632'))
ax=axs[2]
ax.set_title('Exceptional divisor product\n'+r'$\lambda=\mu=\sqrt{2},\quad\lambda\mu=2$')
ax.axhline(0,color='#949da9',lw=.6); ax.axvline(0,color='#949da9',lw=.6)
ax.add_patch(Polygon([(2,0),(0,2),(-2,0),(0,-2)],facecolor='#d3e8dd',edgecolor='#28744d',lw=2,ls='--'))
ax.set(xlim=(-2.5,2.7),ylim=(-2.5,2.7),aspect='equal',xlabel=r'$a_1$',ylabel=r'$a_2$')
ax.set_xticks([-2,0,2]); ax.set_yticks([-2,0,2])
ax.plot(0,0,'o',color='#142b43',ms=6)
ax.annotate(r'$L^2$ retained',(0,0),xytext=(-1.95,-.8),fontsize=11,
            arrowprops=dict(arrowstyle='->',color='#142b43'))
ax.plot(2,0,'o',mfc='white',mec='#a12632',ms=8,mew=1.5)
ax.annotate('whole '+r'$L$'+' fibre missing',(2,0),xytext=(-1.8,2.25),fontsize=10,
            arrowprops=dict(arrowstyle='->',color='#a12632'))
ax.text(-1.85,-2.35,r'Image: $|a_1|+|a_2|<2$',fontsize=11)
info=grid[1,1]
info.axis('off')
info.text(0,.93,'The retained maps',fontsize=13,weight='bold')
info.text(0,.78,r'$(q,p)(x,\ell)=(x,\ell)$',fontsize=13)
info.text(0,.63,r'$q^{-1}(0)=L$',fontsize=13)
info.text(0,.46,r'$z_\ell:(x,\mu)\mapsto(0,\ell\wedge\mu)$',fontsize=12)
info.text(0,.31,r'$z_\ell\circ z_\mu=z_{\ell\wedge\mu}$',fontsize=13)
info.text(0,.13,'Top: integer amplitudes.\nShading: exact real regions.\nBelow: rational amplitudes;\ndashed boundary excluded.',fontsize=10,va='top')
fig.subplots_adjust(left=.085,right=.975,bottom=.105,top=.93,wspace=.38,hspace=.50)
for suffix in ['pdf','svg','png']:
    fig.savefig(ROOT/('FULL_SUPPORT_BOUNDS.'+suffix),dpi=170)
plt.close(fig)
print(json.dumps({'source_matches':[{'id':x['canonical_source_id'],'identical':x['identical']} for x in receipts],
                  'figure':'FULL_SUPPORT_BOUNDS.png'}))
