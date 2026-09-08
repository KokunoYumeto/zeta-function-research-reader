"""Independent source-transcription and relation-graph audit; no author writes."""
from __future__ import annotations
import collections, hashlib, importlib.util, itertools, json, pathlib, sys
sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
AUTHOR = ROOT / 'agents/full_source_generators/construct_full_module.py'
SOURCE = ROOT / 'agents/nonstandard_rh/shelf/cs_0703110v4/source/Apr13KroneckerGCT4.tex'
spec = importlib.util.spec_from_file_location('audited_module', AUTHOR)
author = importlib.util.module_from_spec(spec)
spec.loader.exec_module(author)

# Each row is transcribed from the named literal source line, read in full.
INTEGRAL_ROWS = [
 (5080, ('23','1'),('32','1'),1),
 (5081, ('23','3'),('34','1'),1),
 (5082, ('24','3'),('34','2'),1),
 (5083, ('24','1'),('32','2'),1),
 (5135, ('32','24'),('24','32'),1),
 (5136, ('12','13'),('13','12'),1),
 (5137, ('34','24'),('24','34'),1),
 (5138, ('12','23'),('23','12'),1),
 (5139, ('32','13'),('13','32'),1),
 (5140, ('34','13'),('13','34'),1),
 (5141, ('34','23'),('23','34'),1),
 (5142, ('12','24'),('24','12'),1),
 (5143, ('32','23'),('23','32'),1),
 (5173, ('24','13'),('34','12'),1),
 (5207, ('124','13'),('134','12'),-1),
 (5208, ('234','23'),('234','32'),-1),
 (5209, ('234','13'),('134','32'),-1),
 (5210, ('124','23'),('234','12'),-1),
]
NONINTEGRAL_ROWS = [
 ((5038,5039,5041),1,0,(('2','1'),('2','3'),('4','3')),('4','1')),
 ((5043,5044,5046),1,1,(('3','1'),('3','2'),('4','2')),('4','1')),
 ((5103,5104,5105),2,0,(('32','12'),('32','32'),('34','32')),('34','12')),
 ((5107,5108,5109),2,1,(('23','13'),('23','23'),('24','23')),('24','13')),
 ((5230,5231,5232),3,0,(('124','123'),('124','134'),('234','134')),('234','123')),
 ((5234,5235,5236),3,1,(('134','123'),('134','124'),('234','124')),('234','123')),
]
integral = collections.defaultdict(list)
for line,a,b,s in INTEGRAL_ROWS:
    integral[tuple(map(len,a))].append((a,b,s))
assert {k:set(v) for k,v in integral.items()} == {k:set(v) for k,v in author.INTEGRAL.items()}
assert {(h,s):(strings,inv) for lines,h,s,strings,inv in NONINTEGRAL_ROWS} == author.NONINTEGRAL

WORDS = {
 '1':('1','1'),'2':('1','2'),'3':('2','1'),'4':('2','2'),
 '12':('11','21'),'13':('21','11'),'23':('21','12'),
 '32':('12','21'),'24':('21','22'),'34':('22','21'),
 '123':('211','121'),'124':('211','221'),
 '134':('221','211'),'234':('221','212')}
assert WORDS == author.WORDS
SHAPE = (3,3,3,2,2,1,1)
COLS = {h:tuple(c for c in WORDS if len(c)==h) for h in (1,2,3)}
ALL = tuple(itertools.product(*(COLS[h] for h in SHAPE)))
INDEX = {w:i for i,w in enumerate(ALL)}
assert ALL == author.ALL

def arcs_and_unpaired(bits):
    waiting = []
    partners = {}
    for i,bit in enumerate(bits):
        if bit == '2':
            waiting.append(i)
        elif waiting:
            j = waiting.pop()
            partners[j] = i
            partners[i] = j
    return partners,[i for i in range(len(bits)) if i not in partners]

def corrected(word,pos,side,level,inv):
    if level == 1:
        return word[:pos]+inv+word[pos+2:]
    offset = sum(map(len,word[:pos]))
    local = ''.join(WORDS[c][side] for c in word[pos:pos+2])
    _,free = arcs_and_unpaired(local)
    assert ''.join(local[i] for i in free) == ('11' if level==0 else '22')
    global_bits = ''.join(WORDS[c][side] for c in word)
    partners,_ = arcs_and_unpaired(global_bits)
    selected = offset + free[0 if level==0 else -1]
    if selected not in partners:
        return None
    opposite = partners[selected]
    assert opposite < offset if level==0 else opposite >= offset+len(local)
    col = 0
    localpos = opposite
    while localpos >= len(word[col]):
        localpos -= len(word[col])
        col += 1
    bits = WORDS[word[col]][side]
    changed = bits[:localpos]+('1' if level==0 else '2')+bits[localpos+1:]
    oldarcs = len(arcs_and_unpaired(bits)[0])//2
    newarcs = len(arcs_and_unpaired(changed)[0])//2
    if newarcs > oldarcs:
        return None
    assert newarcs == oldarcs
    choices = [c for c in COLS[len(word[col])]
               if WORDS[c][side].count('1') == changed.count('1')
               and len(arcs_and_unpaired(WORDS[c][side])[0])//2 == oldarcs
               and WORDS[c][1-side] == WORDS[word[col]][1-side]]
    assert len(choices)==1, (word,pos,side,level,choices)
    result = list(word)
    result[col] = choices[0]
    result[pos:pos+2] = inv
    return tuple(result)

by_pair = collections.defaultdict(list)
for lines,h,side,strings,inv in NONINTEGRAL_ROWS:
    for level,pair in enumerate(strings):
        by_pair[pair].append((side,level,inv,lines[level]))
by_integral = collections.defaultdict(list)
for line,a,b,s in INTEGRAL_ROWS:
    by_integral[a].append((b,s,line))

# An edge (i,j,s,k) means x_i=s*p^k*x_j. The graph routine below does
# not use the author's weighted union-find implementation.
edges=[]
zeros=[]
adj=[[] for w in ALL]
counts=collections.Counter()
for i,w in enumerate(ALL):
    for pos in range(len(w)-1):
        pair=w[pos:pos+2]
        for target,s,line in by_integral[pair]:
            j=INDEX[w[:pos]+target+w[pos+2:]]
            edges.append((i,j,s,0,line,pos))
            counts['integral']+=1
        for side,level,inv,line in by_pair[pair]:
            target=corrected(w,pos,side,level,inv)
            assert target==author.contextual(w,pos,side,level,inv)
            if target is None:
                zeros.append((i,line,pos,side,level))
            else:
                edges.append((i,INDEX[target],-1,-1,line,pos))
            counts['contextual']+=1
for eid,(i,j,s,k,line,pos) in enumerate(edges):
    adj[i].append((j,s,-k,eid))
    adj[j].append((i,s,k,eid))
# Here x_neighbor=s*p^k*x_current, after the orientation adjustment above.
zero_nodes={z[0] for z in zeros}
potential={}
component_id={}
components=[]
for root in range(len(ALL)):
    if root in potential:
        continue
    cid=len(components)
    todo=[root]
    potential[root]=(1,0)
    component=[]
    conflicts=[]
    while todo:
        i=todo.pop()
        component.append(i)
        component_id[i]=cid
        si,ki=potential[i]
        for j,s,k,eid in adj[i]:
            value=(si*s,ki+k)
            if j not in potential:
                potential[j]=value
                todo.append(j)
            elif potential[j]!=value:
                sj,kj=potential[j]
                conflicts.append((eid,sj*value[0],value[1]-kj))
    direct=[i for i in component if i in zero_nodes]
    components.append({'root':root,'nodes':component,'direct_zero_nodes':direct,
                       'cycle_discrepancies':sorted(set(conflicts))})

status=collections.Counter()
cycle_values=collections.Counter()
for c in components:
    iszero=bool(c['direct_zero_nodes'])
    inconsistent=bool(c['cycle_discrepancies'])
    status['direct_zero' if iszero else 'cycle_only' if inconsistent else 'surviving']+=1
    if inconsistent:
        status['inconsistent_components']+=1
    for eid,s,k in c['cycle_discrepancies']:
        cycle_values[str((s,k))]+=1
result={
 'source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
 'author_sha256':hashlib.sha256(AUTHOR.read_bytes()).hexdigest(),
 'ambient_words':len(ALL),'relations':dict(counts),
 'direct_zero_relations':len(zeros),'graph_components':len(components),
 'component_status':dict(status),'cycle_values':dict(cycle_values),
 'zero_words':sum(len(c['nodes']) for c in components if c['direct_zero_nodes'] or c['cycle_discrepancies']),
 'source_integral_rows':INTEGRAL_ROWS,'source_nonintegral_rows':NONINTEGRAL_ROWS,
 'independent_contextual_comparisons':counts['contextual'],
 'inconsistent_component_witnesses':[
   {'root_word':ALL[c['root']], 'size':len(c['nodes']),
    'direct_zero_word':ALL[c['direct_zero_nodes'][0]] if c['direct_zero_nodes'] else None,
    'cycle_discrepancies':c['cycle_discrepancies']}
   for c in components if c['cycle_discrepancies']]
}
(HERE/'source_relation_certificate.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k not in ('source_integral_rows','source_nonintegral_rows','inconsistent_component_witnesses')},indent=2))
