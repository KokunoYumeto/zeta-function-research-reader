"""Exact integral divided powers, q=1 specialization, and source interval map."""
from __future__ import annotations
import json,time,hashlib
from construct_full_module import HERE,ALL,INDEX,WORDS,add,mul,divide,qint,apply_matrix

def read_matrices():
    raw=json.loads((HERE/'full_generators.json').read_text())
    mats={name:[{row:dict(coeff) for row,coeff in col} for col in columns]
          for name,columns in raw['matrices'].items()}
    return raw,mats

def divided_powers(mats):
    divided={};stats={}
    for name,mat in mats.items():
        powers=[ [{n:{0:1}} for n in range(1260)] ]
        for m in range(1,11):
            nxt=[]
            for column in powers[-1]:
                nxt.append({i:divide(c,qint(m)) for i,c in apply_matrix(mat,column).items()})
            powers.append(nxt)
            if not any(nxt):break
        assert len(powers)==11 and not any(powers[-1]),(name,len(powers))
        divided[name]=powers
        stats[name]={'nilpotence_index':10,'integral_nonzero_divided_powers':9,
                     'nonzero_entries_by_power':[sum(map(len,p)) for p in powers]}
        print(name,stats[name],flush=True)
    return divided,stats

def descend(mat,start):
    seen=set(start);todo=list(start)
    while todo:
        v=todo.pop()
        for g in mat:
            for w in g[v]:
                if w not in seen:seen.add(w);todo.append(w)
    return seen

def interval(raw,mats,divided):
    basis=json.loads((HERE/'source_basis/basis_1260.json').read_text())['basis']
    points={'T':(('123','123','124','12','12','1','1'),1,0),
            'T1':(('123','123','124','23','12','1','1'),1,0),
            'T2':(('123','123','123','12','12','4','1'),-1,-1),
            'Q':(('123','123','124','13','12','4','1'),-1,-1)}
    labels={}
    for key,(word,s,k) in points.items():
        n,t,h=raw['projection'][INDEX[word]]
        assert s*t==1 and k+h==0,(key,n,t,h)
        labels[key]=n
    v=list(labels.values());graph=[mats['FV'],mats['FW']]
    descendants=descend(graph,[v[0]])
    reverse=[]
    for mat in graph:
        rev=[{} for _ in mat]
        for a,col in enumerate(mat):
            for b,c in col.items():rev[b][a]=c
        reverse.append(rev)
    ancestors=descend(reverse,[v[-1]])
    retained=descendants&ancestors;discarded=descendants-retained
    assert retained==set(v),(retained,labels)
    for mat in graph:
        assert all(set(mat[a])<=descendants for a in descendants)
        assert all(set(mat[a])<=discarded for a in discarded)
    n=mats['FV']
    expected={(1,0):add(qint(7),qint(3),-1),(2,0):qint(8),
              (3,1):qint(6),(3,2):{k:-x for k,x in qint(3).items()}}
    actual={(i,j):n[v[j]][v[i]] for j in range(4) for i in range(4) if v[i] in n[v[j]]}
    assert actual==expected
    c={10:1,4:-1,-4:-1,-10:1}
    assert divided['FV'][2][v[0]][v[3]]==c
    assert not any(mats['FW'][v[j]].get(v[i]) for i in range(4) for j in range(4))
    data={'labels':labels,'descendants_count':len(descendants),
          'discarded_count':len(discarded),'retained_count':len(retained),
          'descendants':sorted(descendants),'discarded':sorted(discarded),
          'quotient_basis':v,'FV_edges':[[i,j,sorted(c.items())] for (i,j),c in expected.items()],
          'divided_square_coefficient':sorted(c.items()),
          'source_quotient_domain':'A-span of descendants; map kills discarded basis vectors',
          'all_graph_closures_checked':True}
    (HERE/'interval_morphism.json').write_text(json.dumps(data,indent=2)+'\n')
    return data

def specialization(mats,divided):
    # All coefficients are integral Laurent polynomials, so this evaluates
    # the full source lattice over Z, rather than just the fraction-field module.
    special={name:[{i:sum(c.values()) for i,c in col.items() if sum(c.values())} for col in mat]
             for name,mat in mats.items()}
    powers={name:[[[[i,sum(c.values())] for i,c in sorted(col.items()) if sum(c.values())]
                  for col in power] for power in pp] for name,pp in divided.items()}
    (HERE/'specialized_generators.json').write_text(json.dumps({'q':1,'base':'Z',
        'dimension':1260,'generators':{name:[sorted(col.items()) for col in mat]
                                    for name,mat in special.items()},
        'divided_powers':powers},separators=(',',':'))+'\n')
    return {'base':'Z','q':1,'dimension':1260,
            'nnz':{name:sum(map(len,mat)) for name,mat in special.items()}}

def raw_integral_projection(raw):
    projection=raw['projection'];section={}
    for i,entry in enumerate(projection):
        if entry is None:continue
        n,s,k=entry
        assert k>=0
        if k==0 and n not in section:section[n]=(i,s)
    assert set(section)==set(range(1260))
    pivots={i for i,s in section.values()};kernel=[]
    for i,entry in enumerate(projection):
        if i in pivots:continue
        if entry is None:kernel.append({'word_index':i,'pivot':None})
        else:
            n,s,k=entry;j,t=section[n]
            kernel.append({'word_index':i,'pivot':j,'subtract_sign':s*t,'p_power':k})
    assert len(kernel)==36864-1260
    # Unitriangular elimination in the original word basis proves independence
    # and spanning. Check the projection of every generator over A exactly.
    for z in kernel:
        i=z['word_index'];j=z['pivot']
        if j is None:assert projection[i] is None
        else:
            n,s,k=projection[i];m,t,h=projection[j]
            assert n==m and h==0 and s==z['subtract_sign']*t and k==z['p_power']
    data={'base':'Z[q,q^-1]','domain_rank':36864,'codomain_rank':1260,
          'kernel_rank':len(kernel),'cokernel':0,
          'projection':'full_generators.json:projection; each tuple(n,s,k) means s*p^k*e_n',
          'section':[[n,i,s] for n,(i,s) in sorted(section.items())],
          'section_convention':'e_n maps to s times original NST at word_index i',
          'kernel_basis':kernel,
          'kernel_convention':'word_i minus subtract_sign*p^p_power*word_pivot; absent pivot means word_i',
          'specialization':{'q':1,'base':'Z','section_unchanged':True,
                            'kernel_basis':'same expression with p^k replaced by 2^k',
                            'kernel_base_change_isomorphism':True,'cokernel':0},
          'claim_scope':'raw-word map into original field quotient; no identification with unsaturated integral relation presentation'}
    (HERE/'raw_integral_projection.json').write_text(json.dumps(data,separators=(',',':'))+'\n')
    print('split integral projection: kernel rank35604, cokernel0',flush=True)
    return {k:v for k,v in data.items() if k not in ('section','kernel_basis')}

if __name__=='__main__':
    start=time.monotonic();raw,mats=read_matrices();divided,stats=divided_powers(mats)
    data={'base':'Z[q,q^-1]','dimension':1260,'divided_power_checks':stats,
          'specialization':specialization(mats,divided),'interval':interval(raw,mats,divided),
          'raw_integral_projection':raw_integral_projection(raw)}
    data['seconds']=time.monotonic()-start
    serial={name:[[[[i,sorted(c.items())] for i,c in sorted(col.items())] for col in power]
                  for power in pp] for name,pp in divided.items()}
    (HERE/'divided_powers.json').write_text(json.dumps(serial,separators=(',',':'))+'\n')
    (HERE/'integral_verification.json').write_text(json.dumps(data,indent=2)+'\n')
    print('all divided-power and interval checks passed',flush=True)
