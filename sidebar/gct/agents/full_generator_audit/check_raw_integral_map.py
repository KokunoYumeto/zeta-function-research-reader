"""Verify split raw-word map over Z[q,q^-1] without assuming relation saturation."""
from pathlib import Path
import json,hashlib

HERE=Path(__file__).resolve().parent
SOURCE=HERE.parent/'full_source_generators'

def run():
    projection=json.loads((SOURCE/'full_generators.json').read_text())['projection']
    raw=json.loads((SOURCE/'raw_integral_projection.json').read_text())
    assert len(projection)==36864
    assert all(p is None or (p[1] in [-1,1] and p[2]>=0) for p in projection)
    section=raw['section']
    assert len(section)==1260
    assert sorted(s[0] for s in section)==list(range(1260))
    pivots={}
    for n,j,s in section:
        assert j not in pivots and projection[j]==[n,s,0]
        pivots[j]=(n,s)
    kernel=raw['kernel_basis']
    assert len(kernel)==35604
    assert {r['word_index'] for r in kernel}==set(range(36864))-set(pivots)
    assert len({r['word_index'] for r in kernel})==len(kernel)
    for row in kernel:
        i=row['word_index'];j=row['pivot'];p=projection[i]
        if j is None:
            assert p is None
        else:
            assert j in pivots and p is not None
            n,s=pivots[j]
            assert p==[n,row['subtract_sign']*s,row['p_power']]
    result={'status':'pass','domain_rank':36864,'codomain_rank':1260,'kernel_rank':35604,
            'section_vectors_checked':1260,'kernel_vectors_checked':35604,'cokernel':0,
            'all_projection_p_powers_nonnegative':True,
            'proof':'Each nonpivot kernel vector has coefficient 1 in its own distinct nonpivot coordinate and has support otherwise only in pivots. The pivot section vectors have coefficients ±1 in their distinct pivot coordinates. Thus these 35604 kernel vectors together with the 1260 section vectors form a unimodular basis of the raw free A-module; its projection is 0 on the kernel part and the identity on the section part. This proves the kernel and section statements over A and after every base change, including q=1 over Z.',
            'scope':'Map from free original NST A-span to the honest lattice in the original Q(q) quotient. Does not assert equality of this kernel with the unsaturated A-span of source relations.',
            'sha256':{name:hashlib.sha256((SOURCE/name).read_bytes()).hexdigest() for name in ['full_generators.json','raw_integral_projection.json']}}
    (HERE/'raw_integral_map_audit.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':run()
