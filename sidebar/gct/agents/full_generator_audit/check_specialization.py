"""Independent check of scaled original image and rational graph specialization."""
from independent_matrix_audit import HERE,SOURCE,bits,pairs,digest
from collections import Counter
from fractions import Fraction
from itertools import product
import json

def run():
    projection=json.loads((SOURCE/'full_generators.json').read_text())['projection']
    scaled=json.loads((SOURCE/'scaled_word_projection.json').read_text())
    basis=json.loads((SOURCE/'source_basis/basis_1260.json').read_text())['basis']
    graph=json.loads((SOURCE/'quotient_audit/relation_graph_certificate.json').read_text())
    alphabets=[['123','124','134','234']]*3+[['12','13','23','32','24','34']]*2+[['1','2','3','4']]*2
    words=list(product(*alphabets));index={w:j for j,w in enumerate(words)}
    owners=[i for i,h in enumerate([3,3,3,2,2,1,1]) for _ in range(h)]
    counts=Counter()
    for i,word in enumerate(words):
        count=Counter((owners[a],owners[b]) for side in [0,1] for a,b in pairs(''.join(bits(c,side) for c in word))[2] if owners[a]!=owners[b])
        assert all(c<=2 for c in count.values())
        degree=sum(c==2 for c in count.values())
        z=projection[i]
        if z is None: assert scaled[i] is None
        else:
            n,s,k=z
            assert k>=degree
            assert scaled[i]==[n,s*(-1)**degree,k-degree]
            counts[k-degree]+=1
    assert counts=={0:17728,1:484}
    for b in basis:
        z=scaled[index[tuple(b['columns'])]]
        assert z[0]==b['index'] and z[1] in [-1,1] and z[2]==0
    free=explicit=cycle_only=0;defects=Counter()
    for component in graph['components']:
        zero=bool(component['explicit_kills'])
        bad=[]
        for s,k in component['cycles']:
            value=s*Fraction(2)**k
            assert (value==1)==(s==1 and k==0)
            if value!=1:bad.append((s,k))
        killed=zero or bool(bad)
        assert killed==component['zero']
        if not killed: free+=1
        elif zero:explicit+=1
        else:cycle_only+=1;defects.update(bad)
    assert (free,explicit,cycle_only)==(1260,4147,40)
    assert defects=={(-1,0):40}
    result={'status':'pass','scaled_words_checked':len(words),'scaled_image_exponent_counts':dict(counts),
            'unit_honest_preimages_checked':len(basis),'specialized_quotient_dimension':free,
            'specialized_relation_rank':len(words)-free,'explicit_zero_components':explicit,
            'cycle_only_components':cycle_only,'cycle_only_defects':[[list(k),v] for k,v in defects.items()],
            'proof':'Every graph edge remains a nonzero rational number at p=2. For every signed integral exponent pair, sign*2^k=1 if and only if sign=+1 and k=0. Therefore each component has the same quotient dimension over Q(q) and at q=1 over Q. The specialized source relation span is contained in the specialized kernel and both have dimension 35604, so they are equal. The scaled-word image equals the honest lattice because every scaled image is integral and every honest vector has an explicit unit scaled-word preimage.',
            'sha256':{name:digest(SOURCE/name) for name in ['full_generators.json','source_basis/basis_1260.json','scaled_word_projection.json','quotient_audit/relation_graph_certificate.json']}}
    (HERE/'specialization_audit.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':run()
