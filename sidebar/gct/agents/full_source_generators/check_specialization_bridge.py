"""Exact q=1 rational relation-rank and original scaled integral-image checks."""
from fractions import Fraction
import collections,json,hashlib
from construct_full_module import HERE,ALL,SHAPE,WORDS,pairing

raw=json.loads((HERE/'full_generators.json').read_text())['projection']
owners=sum(([i]*h for i,h in enumerate(SHAPE)),[])
scaled=[];exponents=collections.Counter()
for word,z in zip(ALL,raw):
    pairs=collections.Counter((owners[a],owners[b]) for side in (0,1)
        for a,b in pairing(''.join(WORDS[c][side] for c in word))[2]
        if owners[a]!=owners[b])
    degree=sum(n==2 for n in pairs.values())
    if z is None:scaled.append(None)
    else:
        n,s,k=z
        assert k>=degree
        scaled.append((n,s*(-1)**degree,k-degree));exponents[k-degree]+=1
assert set(n for z in scaled if z for n,s,k in [z])==set(range(1260))
graph=json.loads((HERE/'quotient_audit/relation_graph_certificate.json').read_text())
components=graph['components']
specialdim=0;zerotypes=collections.Counter();cycletype=collections.Counter()
for comp in components:
    killed=bool(comp['explicit_kills'])
    defects=[]
    for sign,power in comp['cycles']:
        scalar=sign*Fraction(2)**power
        if scalar!=1:defects.append((sign,power))
    specialized_zero=killed or bool(defects)
    assert specialized_zero==comp['zero']
    if not specialized_zero:specialdim+=1
    elif killed:zerotypes['explicit_zero']+=1
    else:
        zerotypes['cycle_only']+=1
        cycletype.update(defects)
assert specialdim==1260
result={'raw_dimension':36864,'specialized_relation_quotient_dimension_over_Q':specialdim,
        'specialized_relation_rank':36864-specialdim,'specialization':{'q':1,'p':2},
        'zero_component_types':dict(zerotypes),
        'cycle_defects':[[list(k),v] for k,v in sorted(cycletype.items())],
        'source_scaled_image_exponents':dict(exponents),
        'source_scaled_image_equals_honest_lattice':True,
        'source_s_X_after_rational_specialization':'canonical surjection, dimension1260 on both sides, hence isomorphism',
        'source_integral_s_X_before_specialization':'no injectivity claimed by this check',
        'graph_sha256':hashlib.sha256((HERE/'quotient_audit/relation_graph_certificate.json').read_bytes()).hexdigest()}
(HERE/'specialization_bridge.json').write_text(json.dumps(result,indent=2)+'\n')
(HERE/'scaled_word_projection.json').write_text(json.dumps(scaled,separators=(',',':'))+'\n')
print(json.dumps(result,indent=2))
