"""Checks the sixteen contextual source-positive sign witnesses exactly.

The parent full quotient supplies an independent projection certificate;
the written source proof does not depend on these finite checks.
"""
import json
import sys
from pathlib import Path
from enumerate_basis import HERE, diagram
sys.path.insert(0,str(HERE.parent))
from construct_full_module import INDEX

def main():
    basis=json.loads((HERE/'basis_1260.json').read_text())['basis']
    projection=json.loads((HERE.parent/'full_generators.json').read_text())['projection']
    indices=[i+j for i in (262,478,1000,1108) for j in range(4)]
    rows=[]
    for i in indices:
        b=basis[i]; original=b['columns']
        if i<1108:
            witness=original[:2]+['234','13','13']+original[5:]
        else:
            witness=['234','123','234','13','13']+original[5:]
        pi=projection[INDEX[tuple(original)]]
        pj=projection[INDEX[tuple(witness)]]
        assert pi[0]==pj[0]==i
        assert pi[1]==-pj[1] and pi[2]==pj[2]
        dl,own,arcs,unpaired=diagram(witness,'W')
        arcs32=[(a,b) for a,b in arcs if own[a]!=own[b] and (len(witness[own[a]]),len(witness[own[b]]))==(3,2)]
        assert len(arcs32)==1
        rows.append({'index':i,'original':original,'W_arc_witness':witness,
                    'original_equals_minus_witness':True,'projection_original':pi,'projection_witness':pj})
    out={'all_sixteen_relations_verified':True,'source_sign_note':'every/any no-3-2 phrase needs the documented correction; W-arc representative fixes sign',
         'witnesses':rows}
    (HERE/'sign_witnesses.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print('Verified all sixteen original = minus W-3-2 representative identities in the full original quotient.')

if __name__=='__main__':main()
