"""Generic-q literal source weight check, without changing its target label."""
from collections import Counter
from pathlib import Path
import hashlib
import json
import sys

def main():
    alphabet={'1':(1,1),'2':(1,2),'3':(2,1),'4':(2,2)}
    words={'T':'123 123 124 12 12 1 1',
           'T1':'123 123 124 23 12 1 1',
           'T2':'123 123 123 12 12 4 1',
           'P':'123 123 124 23 12 4 1',
           'Q':'123 123 124 13 12 4 1'}
    weights={}
    for name,word in words.items():
        letters=[alphabet[c] for c in word if c!=' ']
        weights[name]=[[sum(v[d]==i for v in letters) for i in (1,2)] for d in (0,1)]
    assert weights=={'T':[[12,3],[9,6]],'T1':[[11,4],[9,6]],
                     'T2':[[11,4],[9,6]],'P':[[10,5],[8,7]],'Q':[[10,5],[9,6]]}
    def qint(n): return Counter({j:1 for j in range(1-n,n,2)})
    def mul(a,b):
        c=Counter()
        for i,x in a.items():
            for j,y in b.items(): c[i+j]+=x*y
        return {i:x for i,x in c.items() if x}
    def add(a,b,sign=1):
        c=Counter(a)
        for i,x in b.items(): c[i]+=sign*x
        return {i:x for i,x in c.items() if x}
    C={10:1,4:-1,-4:-1,-10:1}
    assert mul(qint(2),C)==add(mul(qint(6),add(qint(7),qint(3),-1)),mul(qint(3),qint(8)),-1)
    assert C==mul({2:1,0:-2,-2:1},mul(qint(7),qint(3)))
    source=Path('[local]/Documents/arxiv_latex/_topic_fetch/GCT_nonstandard_RH_20260908/cs_0703110v4/source/Apr13KroneckerGCT4.tex')
    result={'status':'pass','script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
            'source_loci':'alphabet 2849-2850; column dictionary 4631-4633; example 7319-7360',
            'weights':weights,'literal_P_coefficient_of_FV2':0,
            'Laurent_identity_verified':True,'Q_coefficient_claimed_by_this_check':False,
            'scope':'Exact generic weight obstruction plus printed scalar identity, not a computation of every generator path.'}
    if '--write' in sys.argv:
        Path(__file__).with_name('gct_literal_weight_results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))

if __name__=='__main__': main()
