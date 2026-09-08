"""Independent finite verification of source6183--6269 for nu=(7,5,3)."""
from collections import Counter
from fractions import Fraction
from itertools import combinations, combinations_with_replacement, product
import json
from enumerate_basis import HERE, enumerate_basis

ORDINARY={h:tuple(''.join(map(str,c)) for c in combinations(range(1,5),h)) for h in (1,2,3)}

def is_ssyt(word):
    return all(all(int(a[j])<=int(b[j]) for j in range(min(len(a),len(b)))) for a,b in zip(word,word[1:]))

def source_f(d):
    """All piecewise source cases6195--6254, without assuming injectivity."""
    m=Counter(d['columns'])
    i4,i3,i2,i1=d['invariant_record']
    for col,n in [('123',i3),('234',i3),('24',i2),('13',i2),('4',i1),('1',i1)]:
        m[col]-=n
        assert m[col]>=0
    out=m.copy()
    # Right part: original6195--6210.
    if m['1']:
        out['2'],out['3']=i1+m['2'],i1+m['3']
    elif m['24'] and not m['2']:
        out['2'],out['3']=0,2*i1+m['3']
    elif m['24'] and m['2']:
        out['2'],out['3']=i1+m['2'],i1
    elif i1:
        out['24'],out['34']=m['34'],0
        out['2'],out['3']=i1+m['2'],i1+m['3']
    # Middle part: original6217--6232.
    out['32']=0
    if not m['234'] and m['1']:
        out['14'],out['23']=2*i2+m['23'],0
    elif m['234'] and not m['1']:
        out['14'],out['23']=0,2*i2+m['23']
    elif not m['23']:
        out['14'],out['23']=2*i2+m['32'],0
    else:
        out['14'],out['23']=0,2*i2+m['32']+m['23']
    # Left part: original6237--6250.
    if m['234']:
        out['124'],out['134']=i3+m['124'],i3+m['134']
    elif m['13'] and not m['134']:
        out['124'],out['134']=2*i3+m['124'],0
    elif m['13'] and m['134']:
        out['124'],out['134']=i3,i3+m['134']
    elif i3:
        out['124'],out['134']=i3+m['124'],i3+m['134']
        out['12'],out['13']=0,m['12']
    result=tuple(c for h in (3,2,1) for c in ORDINARY[h] for _ in range(out[c]))
    assert tuple(map(len,result))==(3,3,3,2,2,1,1)
    return result

def main():
    basis=enumerate_basis()
    images=[source_f(d) for d in basis]
    assert all(is_ssyt(w) for w in images)
    direct={a+b+c for a,b,c in product(combinations_with_replacement(ORDINARY[3],3),
                combinations_with_replacement(ORDINARY[2],2),combinations_with_replacement(ORDINARY[1],2)) if is_ssyt(a+b+c)}
    assert len(images)==len(set(images))==len(direct)==1260
    assert set(images)==direct
    rows=(7,5,3,0)
    factors=[Fraction(rows[i]-rows[j]+j-i,j-i) for i in range(4) for j in range(i+1,4)]
    dim=Fraction(1)
    for v in factors:dim*=v
    assert dim==1260
    components={}
    for d in basis:
        z=tuple(d['zeta'])
        uv,uw=d['unpaired_V'],d['unpaired_W']
        components.setdefault(z,set()).add((uv.count('2'),uw.count('2')))
    rectangle_rows=[]
    for z,positions in sorted(components.items()):
        cells=[d for d in basis if tuple(d['zeta'])==z]
        hv=len(cells[0]['unpaired_V']); hw=len(cells[0]['unpaired_W'])
        assert all(len(d['unpaired_V'])==hv and len(d['unpaired_W'])==hw for d in cells)
        assert positions==set(product(range(hv+1),range(hw+1)))
        rectangle_rows.append({'zeta':list(z),'highest_weight_differences':[hv,hw],
                              'highest_weight_V':[(15+hv)//2,(15-hv)//2],
                              'highest_weight_W':[(15+hw)//2,(15-hw)//2],
                              'size':len(cells)})
    result={'source_f_total':len(images),'source_f_distinct':len(set(images)),
            'independently_enumerated_ssyt':len(direct),'equal_sets':True,
            'weyl_dimension_factors':[str(v) for v in factors],'weyl_dimension':int(dim),
            'crystal_components':len(components),'complete_crystal_rectangles':rectangle_rows}
    (HERE/'ssyt_bijection_check.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    (HERE/'ssyt_correspondence.json').write_text(json.dumps([
       {'basis_index':d['index'],'ssyt_columns':list(w)} for d,w in zip(basis,images)],indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='complete_crystal_rectangles'},indent=2))

if __name__=='__main__':main()
