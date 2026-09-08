"""Source-parsed two-column relations; independent graph quotient audit.

No import of construct_full_module.py and no weighted union-find.  All local
relations are parsed from the actual primary-source figure nodes.  Arc
matching is performed by iterative adjacent 21 erasure, not a stack.
"""
from collections import Counter, defaultdict, deque
from itertools import product
from pathlib import Path
from functools import lru_cache
import hashlib, json, re

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parents[1] / 'nonstandard_rh/shelf/cs_0703110v4/source/Apr13KroneckerGCT4.tex'
TEXT = SOURCE.read_text(encoding='utf-8')
SHAPE = (3,3,3,2,2,1,1)
ALPH = {1:('1','2','3','4'), 2:('12','13','23','32','24','34'), 3:('123','124','134','234')}
WORDS = tuple(product(*(ALPH[h] for h in SHAPE)))
INDEX = {w:i for i,w in enumerate(WORDS)}

def figure(label):
    end = TEXT.index(r'\label{' + label + '}')
    start = TEXT.rfind(r'\begin{figure}', 0, end)
    return TEXT[start:end], TEXT.count('\n', 0, start)+1

def column_entries(node):
    node = re.sub(r'\\ctableau\{([^{}]*)\}\{([^{}]*)\}',
                  lambda m:r'\column{'+m[1]+r'}\column{'+m[2]+'}', node)
    matches = list(re.finditer(r'\\column\{([^{}]*)\}', node))
    words = [''.join(re.findall('[1-4]', m[1])) for m in matches]
    return words, matches, node

def nodes(label):
    body, line = figure(label)
    result = []
    for m in re.finditer(r'\\node\[vertex\]\s*\(([^)]*)\)(.*?);', body, re.S):
        cols, spans, node = column_entries(m[2])
        result.append((m[1], cols, spans, node, line+body.count('\n',0,m.start())))
    return result

INTEGRAL = defaultdict(list)
SOURCE_RELATIONS = []
for label, shape in [('f straightening21',(2,1)), ('f straightening22b',(2,2)),
                     ('f straightening22c',(2,2)), ('f straightening32',(3,2))]:
    for name, cols, spans, node, line in nodes(label):
        assert len(cols)>=4
        between = node[spans[1].end():spans[2].start()]
        assert ('+' in between) != ('-' in between), (line, between)
        rhs_sign = -1 if '+' in between else 1
        rel = (tuple(cols[:2]), tuple(cols[2:4]), rhs_sign)
        INTEGRAL[shape].append(rel)
        SOURCE_RELATIONS.append({'type':'integral','shape':shape,'line':line,'left':rel[0], 'right':rel[1], 'rhs_sign':rhs_sign})
assert {k:len(v) for k,v in INTEGRAL.items()}=={(2,1):4,(2,2):10,(3,2):4}

LOCAL = {}
for h in (1,2,3):
    label = f'f straightening{h}{h}' + ('a' if h==2 else '')
    table = {}
    for name,cols,spans,node,line in nodes(label):
        datum=(tuple(cols[:2]), tuple(cols[2:4]) if len(cols)>=4 else None, line)
        if name in table: assert table[name][:2]==datum[:2]
        table[name]=datum
    for side,keys in enumerate((('21','23','43'), ('31','32','42'))):
        invariant = table[keys[1]][1]
        assert invariant is not None and len(invariant)==2
        for level,key in enumerate(keys):
            pair,_,line = table[key]
            LOCAL[h,pair] = LOCAL.get((h,pair), [])+[(side,level,invariant)]
            SOURCE_RELATIONS.append({'type':'contextual','height':h,'line':line,'side':side,'level':level,'pair':pair,'invariant':invariant})

def bits(column, side):
    return tuple((int(c)-1)//2+1 if side==0 else (int(c)-1)%2+1 for c in reversed(column))

@lru_cache(None)
def pairing(word):
    remaining = list(enumerate(word)); arcs=[]
    while True:
        for j in range(len(remaining)-1):
            if (remaining[j][1],remaining[j+1][1])==(2,1):
                arcs.append((remaining[j][0],remaining[j+1][0]))
                del remaining[j:j+2]
                break
        else: return tuple(remaining), tuple(arcs)

def context(word,pos,side,level,invariant):
    if level==1: return word[:pos]+invariant+word[pos+2:]
    seq=tuple(x for c in word for x in bits(c,side))
    local=tuple(x for c in word[pos:pos+2] for x in bits(c,side))
    unpaired,_=pairing(local)
    assert tuple(x[1] for x in unpaired)==((1,1) if level==0 else (2,2))
    point=sum(SHAPE[:pos])+unpaired[0 if level==0 else 1][0]
    _,arcs=pairing(seq)
    partner=None
    for a,b in arcs:
        if level==0 and b==point: partner=a
        if level==2 and a==point: partner=b
    if partner is None:return None
    boundaries=[sum(SHAPE[:i+1]) for i in range(len(SHAPE))]
    column=next(i for i,b in enumerate(boundaries) if partner<b)
    offset=partner-sum(SHAPE[:column])
    assert column<pos if level==0 else column>pos+1
    old=bits(word[column],side)
    changed=old[:offset]+(1 if level==0 else 2,)+old[offset+1:]
    old_unpaired,old_arcs=pairing(old)
    changed_unpaired,changed_arcs=pairing(changed)
    if len(changed_arcs)>len(old_arcs):return None
    inactive_unpaired,inactive_arcs=pairing(bits(word[column],1-side))
    candidates=[c for c in ALPH[SHAPE[column]]
                if tuple(v for _,v in pairing(bits(c,1-side))[0])==tuple(v for _,v in inactive_unpaired)
                and len(pairing(bits(c,1-side))[1])==len(inactive_arcs)
                and tuple(v for _,v in pairing(bits(c,side))[0])==tuple(v for _,v in changed_unpaired)
                and len(pairing(bits(c,side))[1])==len(old_arcs)]
    assert len(candidates)==1,(word,pos,side,level,candidates)
    result=list(word);result[column]=candidates[0];result[pos:pos+2]=invariant
    return tuple(result)

def main():
    graph=[[] for _ in WORDS]; kills=set(); counts=Counter(); all_edges=[]
    for i,word in enumerate(WORDS):
        for pos in range(len(SHAPE)-1):
            shape=SHAPE[pos:pos+2];pair=word[pos:pos+2]
            for left,right,sign in INTEGRAL.get(shape,[]):
                if pair!=left:continue
                target=word[:pos]+right+word[pos+2:]
                j=INDEX[target]; graph[i].append((j,sign,0)); graph[j].append((i,sign,0))
                all_edges.append((i,j,sign,0)); counts['integral']+=1
            if shape[0]!=shape[1]:continue
            for side,level,invariant in LOCAL.get((shape[0],pair),[]):
                target=context(word,pos,side,level,invariant); counts['contextual']+=1
                if target is None:kills.add(i);continue
                j=INDEX[target]
                # e_i=-p^-1 e_j; hence e_j=-p e_i during graph traversal.
                graph[i].append((j,-1,1));graph[j].append((i,-1,-1))
                all_edges.append((i,j,-1,-1))

    components=[]; assigned={}; cycle_counts=Counter()
    for first in range(len(WORDS)):
        if first in assigned:continue
        cid=len(components); assigned[first]=(cid,1,0); todo=deque([first]); members=[]; cycles=set()
        while todo:
            i=todo.popleft();members.append(i); _,sign,power=assigned[i]
            for j,s,k in graph[i]:
                proposal=(cid,sign*s,power+k)
                if j not in assigned:assigned[j]=proposal;todo.append(j)
                else:
                    _,actual_s,actual_k=assigned[j]
                    if proposal!=assigned[j]:
                        defect=(actual_s*proposal[1],proposal[2]-actual_k)
                        # Record both orientations canonically.
                        defect=(defect[0],abs(defect[1]))
                        cycles.add(defect)
        explicit_kills=sorted(set(members)&kills)
        zero=bool(explicit_kills or cycles)
        components.append({'members':members,'explicit_kills':explicit_kills,'cycles':sorted(cycles),'zero':zero})
        cycle_counts.update(cycles)

    saved=json.loads((HERE.parent/'full_generators.json').read_text())
    basis=json.loads((HERE.parent/'source_basis/basis_1260.json').read_text())['basis']
    representative={}
    for n,b in enumerate(basis):
        cid,sign,power=assigned[INDEX[tuple(b['columns'])]]
        assert not components[cid]['zero'] and cid not in representative
        representative[cid]=(n,sign*b['sign'],power+b['p_power'])
    assert len(representative)==sum(not c['zero'] for c in components)
    projection=[]
    for i in range(len(WORDS)):
        cid,sign,power=assigned[i]
        if components[cid]['zero']:projection.append(None)
        else:
            n,s,k=representative[cid];projection.append([n,sign*s,power-k])
    discrepancies=[(i,WORDS[i],a,b) for i,(a,b) in enumerate(zip(projection,saved['projection'])) if a!=b]
    assert not discrepancies,(len(discrepancies),discrepancies[:5])
    # Check the defining linear relations directly against the reconstructed projection.
    for i,j,sign,power in all_edges:
        a,b=projection[i],projection[j]
        assert (a is None)==(b is None)
        if a is not None:assert a==[b[0],sign*b[1],power+b[2]]
    assert all(projection[i] is None for i in kills)
    torsion=[{'component':i,'size':len(c['members']),'cycles':c['cycles'],'first_word':WORDS[c['members'][0]]}
             for i,c in enumerate(components) if c['cycles'] and not c['explicit_kills']]
    hist=Counter(p[2] for p in projection if p is not None)
    basis_projection=[projection[INDEX[tuple(b['columns'])]] for b in basis]
    report={
        'source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        'source_relations':SOURCE_RELATIONS,
        'ambient_words':len(WORDS),'relation_counts':dict(counts),
        'explicit_zero_words':len(kills),'components':len(components),
        'nonzero_components':len(representative),
        'zero_words':sum(len(c['members']) for c in components if c['zero']),
        'cycle_defects':{str(k):v for k,v in cycle_counts.items()},
        'cycle_only_zero_components':torsion,
        'projection_p_exponents':dict(sorted(hist.items())),
        'all_original_relations_annihilated':True,
        'all_saved_projection_entries_match_independent_graph':True,
        'basis_projection_p_exponents':dict(sorted(Counter(p[2] for p in basis_projection).items())),
    }
    (HERE/'original_quotient_audit.json').write_text(json.dumps(report,indent=2)+'\n')
    (HERE/'relation_graph_certificate.json').write_text(json.dumps({'assigned':[assigned[i] for i in range(len(WORDS))], 'components':components},separators=(',',':'))+'\n')
    print(json.dumps({k:v for k,v in report.items() if k not in ('source_relations','cycle_only_zero_components')},indent=2))
    print('cycle-only zero components:',json.dumps(torsion))

if __name__=='__main__':main()
