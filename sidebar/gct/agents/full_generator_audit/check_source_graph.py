"""Original source tables and independent weighted breadth-first quotient audit."""
from independent_matrix_audit import HERE,SOURCE,bits,pairs,ARROWS,digest
from itertools import product
from collections import defaultdict,deque,Counter
import json

# Independently transcribed from the fixed primary TeX, lines listed below.
INTEGRAL=[
    (5080,('23','1'),('32','1'),1),(5081,('23','3'),('34','1'),1),
    (5082,('24','3'),('34','2'),1),(5083,('24','1'),('32','2'),1),
    (5135,('32','24'),('24','32'),1),(5136,('12','13'),('13','12'),1),
    (5137,('34','24'),('24','34'),1),(5138,('12','23'),('23','12'),1),
    (5139,('32','13'),('13','32'),1),(5140,('34','13'),('13','34'),1),
    (5141,('34','23'),('23','34'),1),(5142,('12','24'),('24','12'),1),
    (5143,('32','23'),('23','32'),1),(5173,('24','13'),('34','12'),1),
    (5207,('124','13'),('134','12'),-1),(5208,('234','23'),('234','32'),-1),
    (5209,('234','13'),('134','32'),-1),(5210,('124','23'),('234','12'),-1)]
STRINGS=[
    (5056,0,[('2','1'),('2','3'),('4','3')],('4','1')),
    (5061,1,[('3','1'),('3','2'),('4','2')],('4','1')),
    (5103,0,[('32','12'),('32','32'),('34','32')],('34','12')),
    (5107,1,[('23','13'),('23','23'),('24','23')],('24','13')),
    (5230,0,[('124','123'),('124','134'),('234','134')],('234','123')),
    (5234,1,[('134','123'),('134','124'),('234','124')],('234','123'))]

def change_at(word,side,position,raising):
    c=0
    while position>=len(word[c]):position-=len(word[c]);c+=1
    old=bits(word[c],side)
    assert old[position]==('2' if raising else '1')
    changed=old[:position]+('1' if raising else '2')+old[position+1:]
    if len(pairs(changed)[2])>len(pairs(old)[2]):return None
    arrows={b:a for a,b in ARROWS[side].items()} if raising else ARROWS[side]
    assert word[c] in arrows
    return word[:c]+(arrows[word[c]],)+word[c+1:]

def correction(word,pos,side,level,invariant):
    offset=sum(len(c) for c in word[:pos])
    local=''.join(bits(c,side) for c in word[pos:pos+2])
    unpaired1,unpaired2,_=pairs(local)
    _,_,arcs=pairs(''.join(bits(c,side) for c in word))
    if level==0:
        target=offset+unpaired1[0]
        partner=[a for a,b in arcs if b==target]
        if not partner:return None
        assert len(partner)==1 and partner[0]<offset
        updated=change_at(word,side,partner[0],True)
    elif level==2:
        target=offset+unpaired2[-1]
        partner=[b for a,b in arcs if a==target]
        if not partner:return None
        assert len(partner)==1 and partner[0]>=offset+len(local)
        updated=change_at(word,side,partner[0],False)
    else:updated=word
    return None if updated is None else updated[:pos]+invariant+updated[pos+2:]

def run():
    shapes=(3,3,3,2,2,1,1)
    alphabets={1:['1','2','3','4'],2:['12','13','23','32','24','34'],3:['123','124','134','234']}
    words=list(product(*(alphabets[h] for h in shapes)));index={w:i for i,w in enumerate(words)}
    adjacency=[[] for _ in words];kills=set();counts=Counter();source_rows=[]
    for line,left,right,sign in INTEGRAL:
        source_rows.append({'line':line,'type':'integral','left':left,'right':right,'sign':sign})
    for line,side,string,inv in STRINGS:
        source_rows.append({'line':line,'type':'three_term_string','side':side,'string':string,'invariant':inv})
    def edge(i,j,sign,power):
        # t_i=sign*p^power*t_j, hence t_j=sign*p^-power*t_i.
        adjacency[i].append((j,sign,-power))
        adjacency[j].append((i,sign,power))
    for pos in range(6):
        for word,i in index.items():
            pair=word[pos:pos+2]
            for line,left,right,sign in INTEGRAL:
                if pair==left:
                    edge(i,index[word[:pos]+right+word[pos+2:]],sign,0);counts['integral']+=1
            if shapes[pos]!=shapes[pos+1]:continue
            for line,side,string,inv in STRINGS:
                if pair in string:
                    target=correction(word,pos,side,string.index(pair),inv)
                    if target is None:kills.add(i)
                    else:edge(i,index[target],-1,-1)
                    counts['contextual']+=1
    assert counts=={'integral':22528,'contextual':47616}
    location=[None]*len(words);potential=[None]*len(words);components=[]
    for start in range(len(words)):
        if location[start] is not None:continue
        cid=len(components);todo=deque([start]);location[start]=cid;potential[start]=(1,0)
        members=[];cycles=set();explicit=False
        while todo:
            i=todo.popleft();members.append(i);explicit|=i in kills
            s,k=potential[i]
            for j,t,h in adjacency[i]:
                expected=(s*t,k+h)
                if location[j] is None:
                    location[j]=cid;potential[j]=expected;todo.append(j)
                else:
                    assert location[j]==cid
                    u,l=potential[j]
                    ratio=(expected[0]*u,expected[1]-l)
                    if ratio!=(1,0):cycles.add(ratio)
        components.append({'root':start,'members':members,'explicit_zero':explicit,'cycles':sorted(cycles),'zero':explicit or bool(cycles)})
    free=[i for i,c in enumerate(components) if not c['zero']]
    explicit=[i for i,c in enumerate(components) if c['explicit_zero']]
    torsion=[i for i,c in enumerate(components) if c['zero'] and not c['explicit_zero']]
    assert (len(free),len(explicit),len(torsion))==(1260,4147,40)
    assert all(components[i]['cycles']==[(-1,0)] for i in torsion)
    basis=json.loads((SOURCE/'source_basis/basis_1260.json').read_text())['basis']
    pivots={}
    for b in basis:
        j=index[tuple(b['columns'])];cid=location[j];s,k=potential[j]
        assert cid in free and cid not in pivots
        pivots[cid]=(b['index'],s*b['sign'],k+b['p_power'])
    assert set(pivots)==set(free)
    recorded=json.loads((SOURCE/'full_generators.json').read_text())['projection']
    for i in range(len(words)):
        cid=location[i]
        if components[cid]['zero']:expected=None
        else:
            n,s,k=pivots[cid];t,h=potential[i]
            expected=[n,s*t,h-k]
        assert recorded[i]==expected,('projection',i,recorded[i],expected)
    result={'status':'pass','ambient_words':len(words),'relation_counts':dict(counts),
            'components':len(components),'free_components':len(free),'explicit_zero_components':len(explicit),
            'cycle_only_components':len(torsion),'cycle_only_defects':[[-1,0]],
            'projection_entries_independently_reconstructed':len(words),
            'localized_base':'B=Z[q,q^-1,(q+q^-1)^-1]',
            'localized_presentation':'B^1260 direct_sum (B/(2))^40',
            'localized_map_to_honest_lattice':'identity on free summands and zero on the40 torsion summands, relative to explicit weighted component coordinates',
            'torsion_components':[{'root_index':components[i]['root'],'root_word':words[components[i]['root']],'word_count':len(components[i]['members'])} for i in torsion],
            'source_rows':source_rows,
            'contextual_source_lines':[2544,2550,5773,5785],
            'input_sha256':{name:digest(SOURCE/name) for name in ['full_generators.json','source_basis/basis_1260.json']}}
    (HERE/'source_graph_audit.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ['source_rows','torsion_components']},indent=2))

if __name__=='__main__':run()
