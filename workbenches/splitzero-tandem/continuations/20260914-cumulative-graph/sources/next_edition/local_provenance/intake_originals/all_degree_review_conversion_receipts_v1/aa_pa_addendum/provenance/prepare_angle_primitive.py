"""Type the entire accepted primitive note with exact source and AST inverses.

The independently read mapping changes mathematical delimiters only. Every
original mathematical payload and all prose outside those explicit spans stay
unchanged. The unchanged accepted adapter supplies the full writer inverse.
"""
from __future__ import annotations
import argparse,collections,copy,json,re
from pathlib import Path
import prepare_conversions as pc

ROOT=pc.ROOT
DEST=ROOT/'aa_pa_addendum'
KEY='angle_primitive_acceptance'
SOURCE=pc.MATH/'output/Tau_All_Degree_Angle_Transport_2026-09-13/evidence/tau_all_degree_angle_primitive_acceptance_20260913.md'
SOURCE_SHA='8def95f8c69d3df47a82948882d161ba134b1b37d3abfb482595891eb93a2f56'

def ast_edits(before,after,path=()):
    if before==after:return []
    if isinstance(before,dict) and isinstance(after,dict) and before.keys()==after.keys():
        return [r for k in before for r in ast_edits(before[k],after[k],path+(k,))]
    if isinstance(before,list) and isinstance(after,list) and len(before)==len(after):
        return [r for i in range(len(before)) for r in ast_edits(before[i],after[i],path+(i,))]
    return [{'path':list(path),'before':copy.deepcopy(before),'after':copy.deepcopy(after)}]

def apply_ast(tree,edits,inverse=False):
    tree=copy.deepcopy(tree)
    for row in reversed(edits) if inverse else edits:
        old,new=('after','before') if inverse else ('before','after')
        parent=tree
        for p in row['path'][:-1]:parent=parent[p]
        last=row['path'][-1]
        if parent[last]!=row[old]:raise RuntimeError('Full AST edit preimage differs')
        parent[last]=copy.deepcopy(row[new])
    return tree

def main(mapping_path):
    raw=SOURCE.read_bytes()
    assert len(raw)==5785 and pc.sha(raw)==SOURCE_SHA
    mapping=json.loads(Path(mapping_path).read_text(encoding='utf-8'))
    assert pc.sha(Path(mapping_path).read_bytes())=='dc79f42243f3750cd0bcb102196c35297c0a769b949bf181a654d71ba7e7382a'
    assert mapping['original_source']['sha256']==SOURCE_SHA
    edits=copy.deepcopy(mapping['edits'])
    assert len(edits)==26
    for a,b in zip(edits,edits[1:]):assert a['source_end_byte']<=b['source_start_byte']
    chunks=[];cursor=0;length=0
    for row in edits:
        assert raw[row['source_start_byte']:row['source_end_byte']]==row['before'].encode()
        assert row['after']==r'\('+row['typed_math_payload']+r'\)'
        prefix=raw[cursor:row['source_start_byte']];chunks.append(prefix);length+=len(prefix)
        typed=row['after'].encode();row['public_start_byte']=length;row['public_end_byte']=length+len(typed)
        row['before_sha256']=pc.sha(row['before'].encode());row['after_sha256']=pc.sha(typed)
        chunks.append(typed);length+=len(typed);cursor=row['source_end_byte']
    chunks.append(raw[cursor:]);public=b''.join(chunks)
    restored=public
    for row in reversed(edits):
        a,b=row['public_start_byte'],row['public_end_byte']
        assert restored[a:b]==row['after'].encode()
        restored=restored[:a]+row['before'].encode()+restored[b:]
    assert restored==raw
    raw_path=ROOT/'raw'/KEY/SOURCE.name;public_path=ROOT/'sources'/KEY/SOURCE.name
    pc.stable_write(raw_path,raw);pc.stable_write(public_path,public)
    adapter=pc.load_adapter();builder=pc.Builder(KEY)
    raw_ast=pc.parse_ast(builder,adapter,raw_path,'raw_original_ast')
    public_ast=pc.parse_ast(builder,adapter,public_path,'public_original_ast')
    patches=ast_edits(raw_ast,public_ast)
    assert apply_ast(raw_ast,patches)==public_ast
    assert apply_ast(public_ast,patches,True)==raw_ast
    literal_before=pc.literal_sequence(adapter,raw_ast);literal_after=pc.literal_sequence(adapter,public_ast)
    codes_before=[p for t,p in literal_before if t=='Code'];codes_after=[p for t,p in literal_after if t=='Code']
    assert codes_before==codes_after
    original_math=[p for t,p in literal_before if t=='Math']
    public_math=[p for t,p in literal_after if t=='Math']
    assert len(original_math)==7 and len(public_math)==33
    # Source positions determine the whole expected mathematical sequence.
    # Existing well-delimited payloads remain literal; each repaired span has
    # its independent original-to-typed exact payload in the map.
    spans=[]
    retained_source_spans=[]
    for index,match in enumerate(re.finditer(rb'\\\((.*?)\\\)|\\\[(.*?)\\\]',raw,re.S)):
        a,b=match.span()
        assert not any(a<r['source_end_byte'] and b>r['source_start_byte'] for r in edits)
        display=match.group(2) is not None
        original_payload=original_math[index]
        assert original_payload[0]['t']==('DisplayMath' if display else 'InlineMath')
        # The existing display lives inside a Markdown list. Preserve its
        # exact original Pandoc payload, including its original newlines;
        # do not strip or re-indent that mathematical literal.
        spans.append((a,copy.deepcopy(original_payload)))
        retained_source_spans.append({'source_start_byte':a,'source_end_byte':b,
            'complete_original_delimited_span':match.group().decode(),
            'complete_original_AST_Math_payload':copy.deepcopy(original_payload),
            'unchanged_in_public_AST':True})
    assert len(spans)==7
    spans.extend((r['source_start_byte'],[{'t':'InlineMath'},r['typed_math_payload']]) for r in edits)
    expected=[p for _,p in sorted(spans,key=lambda row:row[0])]
    assert expected==public_math
    counts=adapter._counts(adapter._payloads(public_ast,'Math'))
    spec={'key':KEY,'source':public_path.relative_to(ROOT).as_posix(),
          'title':'Complete independent acceptance proof of the literal tensor theta primitive',
          'sha256':pc.sha(public),'bytes':len(public),'source_role':'Complete independently accepted supporting calculation, with every original prose and mathematical payload retained and exact delimiter-transcription inverses.',
          'location':'chapter','required_math_nodes':counts,'required_code_blocks':0}
    wrapper,row=adapter.prepare_endpoint_witness(builder,spec)
    wrapper_path=ROOT/'tex'/f'{KEY}.tex';pc.stable_write(wrapper_path,wrapper.encode())
    public_mapping={
       'schema':'complete-primitive-note-delimiter-typing-and-AST-inverse-v1',
       'original_source':{'filename':SOURCE.name,'bytes':len(raw),'sha256':pc.sha(raw)},
       'typed_source':{'filename':SOURCE.name,'bytes':len(public),'sha256':pc.sha(public)},
       'typing_byte_edits':edits,'complete_raw_to_typed_ast_edits':patches,
       'raw_node_counts':dict(collections.Counter(n['t'] for _,n,_ in adapter._nodes(raw_ast))),
       'public_node_counts':dict(collections.Counter(n['t'] for _,n,_ in adapter._nodes(public_ast))),
       'whole_original_literal_sequence':literal_before,'whole_typed_literal_sequence':literal_after,
       'expected_complete_math_sequence_from_original_source_byte_order':expected,
       'every_original_well_delimited_source_span':retained_source_spans,
       'complete_byte_inverse_restores_original':True,
       'complete_AST_forward_and_inverse_equal':True,
       'every_original_well_delimited_math_payload_and_provenance_Code_unchanged':True,
       'all_26_added_Math_payloads_exactly_match_independent_transcriptions':True,
       'no_proof_prose_or_mathematical_payload_change':True,
       'scope':'Complete notation and source conversion only; every original mathematical token and all six numbered proof paragraphs remain. No mathematical re-audit or visual PDF acceptance.'}
    map_target=DEST/'public_provenance/PRIMITIVE_NOTATION_AND_AST_INVERSE.json'
    pc.stable_write(map_target,(json.dumps(public_mapping,ensure_ascii=False,indent=2)+'\n').encode())
    receipt={
       'schema':'actual-tau-complete-primitive-source-publication-and-typing-v1','key':KEY,
       'original_source':pc.pin(SOURCE),'raw_snapshot':pc.pin(raw_path),'public_source':pc.pin(public_path),
       'source_unchanged_after_conversion':SOURCE.read_bytes()==raw,
       'publication_and_typing_byte_edits':edits,'exact_byte_inverse_restores_entire_original_source':True,
       'raw_original_ast':pc.pin(builder.BUILD/'raw_original_ast.json'),
       'public_original_ast':pc.pin(builder.BUILD/'public_original_ast.json'),
       'complete_expected_original_to_public_literal_sequence_equal':True,
       'literal_sequence_rule':'Every original well-delimited mathematical payload and Code remains. Twenty-six original parenthesized or malformed-delimiter expressions become their exact unchanged mathematical payloads in inline Math. The full raw AST and source bytes are restored exactly by the accompanying inverse.',
       'raw_node_counts':public_mapping['raw_node_counts'],'public_node_counts':public_mapping['public_node_counts'],
       'complete_raw_to_typed_AST_inverse':pc.pin(map_target),
       'source_equation_tags':[],'source_equation_tag_count':0,'source_equation_tags_preserved_exactly':True,
       'full_source_headings':[n['c'] for _,n,_ in adapter._nodes(raw_ast) if n['t']=='Header'],
       'math_node_counts':counts,'typed_code_count':0,'typed_plain_or_malformed_math_count':26,
       'retained_code_count':len(codes_after),'adapter':pc.pin(ROOT/'pipeline/endpoint_source_appendix_adapter.py'),
       'adapter_spec':spec,'adapter_row':row,'wrapper':pc.pin(wrapper_path),
       'independent_complete_typing_inventory':pc.pin(Path(mapping_path)),
       'scope':'Source conversion with exact original/public bytes and full AST/prose/literal inverses. No mathematical re-audit or visual PDF acceptance.'}
    pc.write_json(ROOT/'receipts'/f'{KEY}.json',receipt)
    print(json.dumps({'key':KEY,'public_source':pc.pin(public_path),'math_node_counts':counts,
                      'typed_plain_or_malformed_math_count':26,'public_mapping':pc.pin(map_target)}))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('mapping');a=p.parse_args();main(a.mapping)
