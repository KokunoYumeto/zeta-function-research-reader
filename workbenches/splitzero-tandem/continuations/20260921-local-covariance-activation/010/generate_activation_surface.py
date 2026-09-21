from pathlib import Path
import mpmath as mp,json
O=Path(__file__).parent
mp.mp.dps=38
def psi(tt):
    t=mp.mpf(tt)
    if t==0:return mp.log(4/mp.pi)
    lo=mp.mpf('1e-30');hi=mp.mpf(1)
    for _ in range(125):
        r=(lo+hi)/2;m=1-r*r
        val=r*mp.ellipk(m)/mp.ellipe(m)
        if val<1/(1+t):lo=r
        else:hi=r
    r=(lo+hi)/2;m=1-r*r
    return mp.log(1+r)+t*mp.log(m)/2-(1+t)*mp.log(mp.ellipe(m))
bs=[mp.mpf(i)/40 for i in range(41)]
ss=[mp.mpf(j)/32 for j in range(33)]
values=[]
for b in bs:
    row=[]
    for ss0 in ss:
        row.append(float(b*psi((1+ss0-b)/b)) if b else 0.)
    values.append(row)
out={'b':[float(v) for v in bs],'s':[float(v) for v in ss],'sigma':values,'sigma_max':float(psi(0)),'threshold_plane':0.075,'precision_digits':38,'root_bisections':125,'equations':'A1,A20-21 and AP1-4','status':'Numerical rendering of the evaluated fixed-b coefficient; no sample is used as a proof or as an actual xi zero.'}
(O/'ACTIVATION_SURFACE_DATA.json').write_text(json.dumps(out,indent=2)+'\n')
