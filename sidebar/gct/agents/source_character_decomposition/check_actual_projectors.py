"""Apply the proved projectors to actual original source matrix columns.

All rational functions use SymPy's exact QQ(q) fraction field. No numerical
specialization is used to infer any identity.
"""
from pathlib import Path
import hashlib
import json
from itertools import product
from sympy.polys.fields import field
from sympy.polys.domains import QQ

ROOT=Path(__file__).resolve().parent
SOURCE=ROOT.parent/'full_source_generators'
F,q=field('q',QQ)
ZERO=F.zero
ONE=F.one


def qi(n):
    if n<0: return -qi(-n)
    return sum((q**i for i in range(1-n,n,2)),ZERO)


def clean(v): return {i:c for i,c in v.items() if c}


def add(v,w,scale=ONE):
    out=dict(v)
    for i,c in w.items(): out[i]=out.get(i,ZERO)+scale*c
    return clean(out)


def scale(v,s): return clean({i:c*s for i,c in v.items()})


def main():
    mp=SOURCE/'full_generators.json'
    bp=SOURCE/'source_basis/basis_1260.json'
    basis=json.loads(bp.read_text())['basis']
    original=json.loads(mp.read_text())
    raw=original['matrices']
    mat={g:[[(t,sum((int(c)*q**int(e) for e,c in terms),ZERO))
              for t,terms in col] for col in cols] for g,cols in raw.items()}
    def action(g,v):
        out={}
        for i,c in v.items():
            for t,a in mat[g][i]: out[t]=out.get(t,ZERO)+c*a
        return clean(out)
    def casimir(colour,v):
        out=action('F'+colour,action('E'+colour,v))
        for i,c in v.items():
            h=basis[i]['weight_'+colour][0]-basis[i]['weight_'+colour][1]
            out[i]=out.get(i,ZERO)+qi((h+1)//2)**2*c
        return clean(out)
    N=[1,3,5,7,9]
    beta={n:qi((n+1)//2)**2 for n in N}
    def projector(colour,n,v):
        out=dict(v)
        for t in N:
            if t!=n:
                out=scale(add(casimir(colour,out),out,-beta[t]),ONE/(beta[n]-beta[t]))
        return out
    def divpower(g,k,v):
        out=dict(v)
        for i in range(1,k+1): out=scale(action(g,out),ONE/qi(i))
        return out
    def gaussian(n,k):
        out=ONE
        for j in range(1,k+1): out=out*qi(n-j+1)/qi(j)
        return out
    def serialize(v):
        return [{'basis_index':i,'coefficient':str(c)} for i,c in sorted(v.items())]
    columns={1:('1','2','3','4'),2:('12','13','23','32','24','34'),
             3:('123','124','134','234')}
    ambient_index={w:i for i,w in enumerate(product(*(columns[h] for h in (3,3,3,2,2,1,1))))}
    points={'T':(('123','123','124','12','12','1','1'),1,0),
            'T1':(('123','123','124','23','12','1','1'),1,0),
            'T2':(('123','123','123','12','12','4','1'),-1,-1),
            'Q':(('123','123','124','13','12','4','1'),-1,-1)}
    records=[]
    for label,(original_word,source_sign,source_power) in points.items():
        index,projection_sign,projection_power=original['projection'][ambient_index[original_word]]
        scalar=source_sign*projection_sign*(q+q**-1)**(source_power+projection_power)
        assert scalar==ONE
        vector={index:scalar}
        u=basis[index]['weight_V'][0]
        v=basis[index]['weight_W'][0]
        recovered={}
        parts=[]
        vparts={n:projector('V',n,vector) for n in N if n>=2*u-15}
        for n,vpart in vparts.items():
            if not vpart: continue
            for m in N:
                if m<2*v-15: continue
                part=projector('W',m,vpart)
                if not part: continue
                assert casimir('V',part)==scale(part,beta[n])
                assert casimir('W',part)==scale(part,beta[m])
                a,b=(n+15)//2,(m+15)//2
                i,j=a-u,b-v
                h=scale(divpower('EV',i,divpower('EW',j,part)),
                        ONE/(gaussian(n,i)*gaussian(m,j)))
                assert not action('EV',h) and not action('EW',h)
                rebuilt=divpower('FV',i,divpower('FW',j,h))
                assert rebuilt==part
                recovered=add(recovered,rebuilt)
                parts.append({'lambda':[a,15-a],'mu':[b,15-b],
                              'positions':[i,j], 'projection':serialize(part),
                              'actual_highest_vector':serialize(h)})
        assert recovered==vector
        records.append({'original_label':label,'basis_index':index,
                        'original_columns':original_word,
                        'original_sign':source_sign,'original_p_power':source_power,
                        'original_word_projection':[index,projection_sign,projection_power],
                        'canonical_representative_columns':basis[index]['columns'],
                        'source_sign':basis[index]['sign'],
                        'source_p_power':basis[index]['p_power'],
                        'components':parts})
        print(label, 'actual_nonzero_components',[(r['lambda'],r['mu'],len(r['projection'])) for r in parts],flush=True)
    data={'status':'passed','source_matrix_sha256':hashlib.sha256(mp.read_bytes()).hexdigest(),
          'source_basis_sha256':hashlib.sha256(bp.read_bytes()).hexdigest(),
          'coefficient_domain':'QQ(q), exact rational functions',
          'vectors':records,
          'checks':['each actual projection has its two Casimir eigenvalues',
                    'each recovered highest vector is killed by both original raising operators',
                    'each highest vector lowers to the exact projected original vector',
                    'the sum of all actual components recovers each original source vector']}
    (ROOT/'actual_projectors_certificate.json').write_text(json.dumps(data,indent=2)+'\n')


if __name__=='__main__': main()
