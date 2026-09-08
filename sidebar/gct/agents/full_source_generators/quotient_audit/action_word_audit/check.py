"""Independent source-word, column-action, and planar-cap audit.

Writes only this directory.  Importing the audited module does not execute its
construction.  Reference pairings use iterative adjacent cancellation, and
context corrections use planar edge surgery, not the audited partner rule.
"""
from __future__ import annotations
import collections, functools, hashlib, importlib.util, json, pathlib, time
import sympy as s

HERE = pathlib.Path(__file__).resolve().parent
TARGET = HERE.parents[1] / 'construct_full_module.py'
SOURCE = HERE.parents[2] / 'nonstandard_rh/shelf/cs_0703110v4/source/Apr13KroneckerGCT4.tex'
spec = importlib.util.spec_from_file_location('audited', TARGET)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
q = s.Symbol('q'); p = q + 1/q

# Transcribed from source figure, lines 4630--4633.  A column label is top
# to bottom.  These are full elements, not merely their reading words.
EXPANSIONS = {
 '1': {('1','1'):1}, '2':{('1','2'):1},
 '3': {('2','1'):1}, '4':{('2','2'):1},
 '12':{('11','21'):1}, '13':{('21','11'):1},
 '32':{('12','21'):1,('21','21'):1/p},
 '23':{('21','12'):1,('21','21'):1/p},
 '34':{('22','21'):1}, '24':{('21','22'):1},
 '123':{('211','121'):1,('121','211'):-1},
 '124':{('211','221'):1,('121','212'):-1},
 '134':{('212','121'):1,('221','211'):-1},
 '234':{('212','221'):1,('221','212'):-1},
}
LITERAL = {c: tuple(''.join(str((int(d)-1)//2+1 if side == 0
                              else (int(d)-1)%2+1) for d in c[::-1])
                    for side in (0,1)) for c in EXPANSIONS}

@functools.lru_cache(None)
def diagram(bits):
    live = list(enumerate(bits)); arcs = []
    while True:
        for j in range(len(live)-1):
            if live[j][1] == '2' and live[j+1][1] == '1':
                arcs.append((live[j][0],live[j+1][0]))
                del live[j:j+2]
                break
        else:
            return tuple(i for i,b in live if b=='1'), tuple(i for i,b in live if b=='2'), tuple(sorted(arcs))

def quantum(j):
    return sum(q**a for a in range(1-j,j,2))

def source_column_action(column, side, raising):
    result = collections.defaultdict(lambda:0)
    for words, coefficient in EXPANSIONS[column].items():
        ones, twos, _ = diagram(words[side])
        positions = twos[::-1] if raising else ones
        for j,pos in enumerate(positions,1):
            target = list(words)
            target[side] = words[side][:pos]+('1' if raising else '2')+words[side][pos+1:]
            result[tuple(target)] += coefficient*quantum(j)
    return {w:s.cancel(c) for w,c in result.items() if s.cancel(c)!=0}

EDGES = {}
def exact_column_edges():
    evidence = []
    for col in EXPANSIONS:
        for side in (0,1):
            for raising in (False,True):
                result = source_column_action(col,side,raising)
                found=[]
                if result:
                    for dst, expansion in EXPANSIONS.items():
                        if len(dst)!=len(col) or set(result)!=set(expansion):
                            continue
                        w = next(iter(expansion)); factor = s.cancel(result[w]/expansion[w])
                        if all(s.cancel(result[v]-factor*expansion[v])==0 for v in result):
                            found.append((dst,factor))
                    assert len(found)==1,(col,side,raising,result,found)
                    EDGES[col,side,raising] = found[0][0]
                evidence.append({'column':col,'side':'V' if side==0 else 'W',
                                 'action':'E' if raising else 'F',
                                 'target':found[0][0] if found else None,
                                 'coefficient':str(found[0][1]) if found else '0'})
    return evidence

@functools.lru_cache(None)
def boundaries(word):
    return tuple(c for c,label in enumerate(word) for _ in label)

def ref_change(word,side,position,newbit):
    colno=boundaries(word)[position]
    bits=''.join(LITERAL[c][side] for c in word)
    changed=bits[:position]+newbit+bits[position+1:]
    locations=boundaries(word)
    # Count actual global internal arcs in every original projector.
    required=[len(diagram(LITERAL[c][side])[2]) for c in word]
    internal=collections.Counter(locations[a] for a,b in diagram(changed)[2]
                                 if locations[a]==locations[b])
    if any(internal[c]>required[c] for c in range(len(word))):
        return None
    dst=EDGES[word[colno],side,newbit=='1']
    return word[:colno]+(dst,)+word[colno+1:]

def reference_action(word,side,raising):
    bits=''.join(LITERAL[c][side] for c in word)
    ones,twos,_=diagram(bits)
    positions=twos[::-1] if raising else ones
    return [(j,ref_change(word,side,k,'1' if raising else '2'))
            for j,k in enumerate(positions,1)]

def cap_surgery(word,pos,side,level,inv):
    bits=''.join(LITERAL[c][side] for c in word)
    offset=sum(map(len,word[:pos]))
    local=''.join(LITERAL[c][side] for c in word[pos:pos+2])
    localones,localtwos,_=diagram(local)
    free=tuple(sorted(localones+localtwos)); assert len(free)==2
    a,b=(offset+j for j in free)
    assert bits[a]+bits[b]==('11','12','22')[level]
    arcs=set(diagram(bits)[2]); mate={}
    for u,v in arcs:mate[u]=v;mate[v]=u
    partners=[mate.get(a),mate.get(b)]
    outside=[x for x in partners if x is not None]
    if not outside and bits[a]==bits[b]:return None
    # Remove the cap's incident edges and reconnect the other ends.  Arcs
    # are always oriented 2 (left) to 1 (right); rays retain their arrows.
    reconnected={e for e in arcs if a not in e and b not in e}
    reconnected.add((a,b)); flips={}
    if len(outside)==2:
        u,v=sorted(outside);reconnected.add((u,v))
        for k,bit in ((u,'2'),(v,'1')):
            if bits[k]!=bit:flips[k]=bit
    elif len(outside)==1:
        ray = b if partners[1] is None else a
        k=outside[0]
        if bits[k]!=bits[ray]:flips[k]=bits[ray]
    locations=boundaries(word)
    old_internal=collections.Counter(locations[u] for u,v in arcs if locations[u]==locations[v])
    new_internal=collections.Counter(locations[u] for u,v in reconnected if locations[u]==locations[v])
    if any(new_internal[c]>old_internal[c] for c in range(len(word)) if c not in (pos,pos+1)):
        return None
    assert len(flips)<=1,(word,pos,side,level,flips)
    result=list(word)
    for k,bit in flips.items():
        c=locations[k];assert c not in (pos,pos+1)
        result[c]=EDGES[word[c],side,bit=='1']
    result[pos:pos+2]=inv
    return tuple(result)

def main():
    started=time.monotonic()
    assert LITERAL==m.WORDS,(LITERAL,m.WORDS)
    edges=exact_column_edges();counts=collections.Counter();examples={}
    for word in m.ALL:
        for side in (0,1):
            bits=''.join(LITERAL[c][side] for c in word)
            a,b,c=diagram(bits);aa,bb,cc=m.pairing(bits)
            assert a==tuple(aa) and b==tuple(bb) and c==tuple(sorted(cc))
            counts['pairing_comparisons']+=1
            for raising in (False,True):
                expected=reference_action(word,side,raising)
                actual=m.action_terms(word,side,raising)
                assert expected==actual,(word,side,raising,expected,actual)
                counts['whole_word_action_comparisons']+=1
                counts['individual_graphical_terms']+=len(expected)
                counts['extra_internal_action_zero_terms']+=sum(t is None for _,t in expected)
                for j,target in expected:
                    if target is None and 'action_zero' not in examples:
                        examples['action_zero']={'word':word,'side':side,'raising':raising,'j':j}
        for pos in range(len(word)-1):
            height=len(word[pos])
            if height!=len(word[pos+1]):continue
            for side in (0,1):
                string,inv=m.NONINTEGRAL[height,side]
                pair=word[pos:pos+2]
                if pair not in string:continue
                level=string.index(pair)
                expected=cap_surgery(word,pos,side,level,inv)
                actual=m.contextual(word,pos,side,level,inv)
                assert expected==actual,(word,pos,side,level,expected,actual)
                counts['contextual_comparisons']+=1
                counts['contextual_zero_corrections']+=expected is None
                counts[f'contextual_level_{level}']+=1
                if expected is None and 'contextual_zero' not in examples:
                    examples['contextual_zero']={'word':word,'pos':pos,'side':side,'level':level}
    # Explicit source examples; these shapes also test contexts outside the
    # fixed seven-column module.
    assertions=[
      (('3','2','1'),1,0,0,('4','1'),('1','4','1')),
      (('34','32','1','1'),0,0,2,('34','12'),('34','12','3','1')),
      (('34','32','1','2'),0,0,2,('34','12'),('34','12','3','2')),
    ]
    for word,pos,side,level,inv,expected in assertions:
        assert cap_surgery(word,pos,side,level,inv)==expected
        assert m.contextual(word,pos,side,level,inv)==expected
    report={'status':'PASS','source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
            'audited_script_sha256':hashlib.sha256(TARGET.read_bytes()).hexdigest(),
            'literal_words':LITERAL,'source_column_actions':edges,'counts':dict(counts),
            'source_example_checks':len(assertions),'examples':examples,
            'elapsed_seconds':time.monotonic()-started,
            'scope':'WORDS, graphical E/F term order, column changes, and contextual cap correction only; not quotient-relation completeness or integral lattice.'}
    (HERE/'results.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':report['status'],'counts':report['counts'],'elapsed_seconds':report['elapsed_seconds']},indent=2))

if __name__=='__main__':main()
