"""Reversible whole-source reader conversions. Writes only under this directory.

Raw UTF-8 source bytes, publication byte edits, full original/public Pandoc
trees, Code-to-Math dictionaries, and the accepted literal-slot adapter are
retained independently. No source mathematical checker is executed.
"""
from __future__ import annotations
import argparse, collections, copy, hashlib, importlib.util, json, re, shutil, subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parent
WORK=ROOT.parent
MATH=WORK.parent
NEXT=Path('F:/user/Documents/Papors/Chatnotes/Zeta-Function-Foundation/agents/zenodo_workspace_publication/integration_20260913_next')
ADAPTER=WORK/'cumulative_deligne_build_20260913_v18/scripts/endpoint_source_appendix_adapter.py'
ADAPTER_SHA='1adac7ea485573981ef3a37cbae04ccc2ab52e91058fe5df80f7c531d6a85023'
SOURCES={
 'analytic_pole':{'path':NEXT/'post_pr26_intake/parent_review/f1_unit_gauge/ANALYTIC_POLE_RESIDUE_TRANSPORT.md',
   'sha256':'357923aead35c77f2fa98598fbc4ed8bc1f7cd6ebc04760da504a0ded765a652','bytes':18433,
   'title':'Complete analytic pole classes, connection, periods and endpoint transport'},
 'analytic_pole_review':{'path':NEXT/'post_pr26_intake/parent_review/f1_unit_gauge/ANALYTIC_POLE_INDEPENDENT_REVIEW.md',
   'sha256':'5dc90ea5d545b674faf02d5f05ccdbd32efdeb03c6b27df793fbedaf32f91d0a','bytes':12705,
   'title':'Complete independent review of analytic pole-residue transport'},
}

def sha(data):return hashlib.sha256(data).hexdigest()
def pin(path):
    b=Path(path).read_bytes();return {'path':str(path),'bytes':len(b),'sha256':sha(b)}
def write_json(path,value):
    Path(path).parent.mkdir(parents=True,exist_ok=True)
    Path(path).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='')
def stable_write(path,data):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    if path.exists() and path.read_bytes()!=data:raise RuntimeError('Refusing to change an existing conversion snapshot: '+str(path))
    path.write_bytes(data)
def load_adapter():
    b=ADAPTER.read_bytes()
    if sha(b)!=ADAPTER_SHA:raise RuntimeError('Accepted adapter changed')
    target=ROOT/'pipeline/endpoint_source_appendix_adapter.py';stable_write(target,b)
    spec=importlib.util.spec_from_file_location('actual_tau_pinned_adapter',target)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module

class Builder:
    def __init__(self,key):self.ROOT=ROOT;self.BUILD=ROOT/'build'/key
    def run(self,command,receipt_path):
        p=subprocess.run(command,cwd=self.ROOT,capture_output=True)
        Path(receipt_path).parent.mkdir(parents=True,exist_ok=True)
        if p.returncode:
            Path(receipt_path).write_bytes(p.stdout+b'\n'+p.stderr)
            raise RuntimeError('Converter command failed: '+str(receipt_path))
        Path(receipt_path).write_bytes(p.stdout)
        if p.stderr:Path(str(receipt_path)+'.stderr').write_bytes(p.stderr)
        return p.stdout.decode('utf-8')
    @staticmethod
    def tex_escape(value):
        trans={'\\':r'\textbackslash{}','{':r'\{','}':r'\}','&':r'\&','%':r'\%','$':r'\$',
               '#':r'\#','_':r'\_','^':r'\textasciicircum{}','~':r'\textasciitilde{}'}
        return ''.join(trans.get(c,c) for c in str(value))

def byte_edit(raw,start,end,after,kind,reason,extra=None):
    row={'source_start_byte':start,'source_end_byte':end,'before':raw[start:end].decode('utf-8'),
         'after':after,'kind':kind,'reason':reason}
    if extra:row.update(extra)
    return row
def phrase_edit(raw,before,after,kind,reason):
    target=before.encode('utf-8')
    if raw.count(target)!=1:raise RuntimeError('Expected exactly one publication phrase: '+before)
    start=raw.index(target);return byte_edit(raw,start,start+len(target),after,kind,reason)

def publication_edits(key,raw):
    pairs=[]
    if key=='analytic_pole':
        pairs=[('The cumulative-reader owner supplied the exact weighted-residue sequence and',
                'The accompanying derivation supplied the exact weighted-residue sequence and'),
               ("The cumulative-reader owner supplied AP3's local-primitive construction and",
                "The accompanying derivation supplied AP3's local-primitive construction and"),
               ('in coordinated messages. Root supplied this full',
                'in the preceding calculation. This note supplies the full'),
               ("root incorporated their full proofs and fixed the review's p=0 residue-factor",
                "the text incorporates their full proofs and the review's corrected p=0 residue-factor"),
               ('No remote publication of this new\nnote, new Lean execution, or certified arithmetic-zero computation is claimed.',
                'No new Lean execution or certified arithmetic-zero computation is claimed.')]
    elif key=='analytic_pole_review':
        pairs=[('the root proof','the source proof')]
    return [phrase_edit(raw,a,b,'public_source_reference',
        'Replace internal task ownership or reporting wording only; retain full mathematical content, proof provenance and verification scope.') for a,b in pairs]

def parse_ast(builder,adapter,source_path,name):
    data=builder.run([shutil.which('pandoc'),source_path.relative_to(ROOT).as_posix(),
                     '--from='+adapter.MARKDOWN_FORMAT,'--to=json'],builder.BUILD/(name+'.json'))
    obj=json.loads(data);write_json(builder.BUILD/(name+'.json'),obj);return obj
def literal_sequence(adapter,tree):
    return [(n['t'],copy.deepcopy(n['c'])) for _,n,_ in adapter._nodes(tree)
            if n['t'] in ('Math','Code','CodeBlock','RawInline','RawBlock')]

def prepare_one(key,mapping_path=None):
    selected=SOURCES[key];raw=selected['path'].read_bytes();raw.decode('utf-8-sig')
    if selected.get('sha256') and sha(raw)!=selected['sha256']:raise RuntimeError('Original source hash mismatch')
    if selected.get('prefix') and not sha(raw).startswith(selected['prefix']):raise RuntimeError('Parent source hash prefix mismatch '+key+' '+sha(raw))
    if selected.get('bytes') and len(raw)!=selected['bytes']:raise RuntimeError('Original source length mismatch')
    adapter=load_adapter();builder=Builder(key);raw_path=ROOT/'raw'/key/selected['path'].name
    stable_write(raw_path,raw)
    raw_ast=parse_ast(builder,adapter,raw_path,'raw_original_ast')
    edits=publication_edits(key,raw);mapping=None
    if mapping_path:
        mapping=json.loads(Path(mapping_path).read_text(encoding='utf-8'))
        if mapping['source']['sha256']!=sha(raw) or mapping['source']['bytes']!=len(raw):raise RuntimeError('Mapping does not address complete original source')
        spans=list(re.finditer(rb'`([^`\r\n]+)`',raw))
        math_rows={x['code_index']:x for x in mapping.get('math_code_mappings',[])}
        retained={x['code_index']:x for x in mapping.get('retained_code',[])}
        if set(math_rows)&set(retained) or set(math_rows)|set(retained)!=set(range(len(spans))):raise RuntimeError('Every original Code needs exhaustive unique classification')
        for index,match in enumerate(spans):
            original=match.group(1).decode('utf-8');row=math_rows.get(index,retained.get(index))
            if row['original']!=original:raise RuntimeError('Exact original Code payload mismatch')
            if index in math_rows:
                tex=row['tex']
                edits.append(byte_edit(raw,match.start(),match.end(),r'\('+tex+r'\)',
                  'mathematical_code_to_typed_math','Complete mathematical notation transcription with original bytes retained.',
                  {'code_index':index,'original_code':original,'typed_math_payload':tex}))
        blocks=adapter._payloads(raw_ast,'CodeBlock')
        brows=mapping.get('display_codeblock_mappings',[])
        if len(brows)!=len(blocks):raise RuntimeError('Every original CodeBlock needs its full display transcription')
        for index,row in enumerate(brows):
            if row.get('codeblock_index',row.get('block_index'))!=index:raise RuntimeError('CodeBlock mapping order mismatch')
            original=row['original']
            if original!=blocks[index][1]:raise RuntimeError('Original complete CodeBlock payload mismatch')
            start,end=row['source_byte_start'],row['source_byte_end']
            span=raw[start:end].decode('utf-8');lines=span.splitlines()
            if not lines or any(not line.startswith('    ') for line in lines):raise RuntimeError('Unexpected original indented CodeBlock span')
            if '\n'.join(line[4:] for line in lines)!=original:raise RuntimeError('CodeBlock span fails exact original-payload correspondence')
            tex=row['tex'];payload=tex
            ending='\n' if span.endswith('\n') else ''
            edits.append(byte_edit(raw,start,end,r'\['+payload+r'\]'+ending,
              'mathematical_codeblock_to_typed_display','Complete original block transcription, every equation and its original identifier retained.',
              {'codeblock_index':index,'original_codeblock':original,'typed_math_payload':payload,'original_codeblock_attrs':blocks[index][0]}))
        stable_write(ROOT/'mapping'/f'{key}_consumed_mapping.json',Path(mapping_path).read_bytes())
    else:raise RuntimeError('Explicit complete mathematical typing map required')
    edits.sort(key=lambda row:row['source_start_byte'])
    for a,b in zip(edits,edits[1:]):
        if a['source_end_byte']>b['source_start_byte']:raise RuntimeError('Overlapping source byte edits')
    chunks=[];cursor=0;length=0
    for row in edits:
        prefix=raw[cursor:row['source_start_byte']];chunks.append(prefix);length+=len(prefix)
        after=row['after'].encode('utf-8');row['public_start_byte']=length;row['public_end_byte']=length+len(after)
        row['before_sha256']=sha(row['before'].encode());row['after_sha256']=sha(after)
        chunks.append(after);length+=len(after);cursor=row['source_end_byte']
    chunks.append(raw[cursor:]);public=b''.join(chunks)
    restored=public
    for row in reversed(edits):
        a,b=row['public_start_byte'],row['public_end_byte']
        if restored[a:b]!=row['after'].encode():raise RuntimeError('Public byte inverse preimage mismatch')
        restored=restored[:a]+row['before'].encode()+restored[b:]
    if restored!=raw:raise RuntimeError('Publication inverse failed')
    public_path=ROOT/'sources'/key/selected['path'].name;stable_write(public_path,public)
    public_ast=parse_ast(builder,adapter,public_path,'public_original_ast')
    expected=literal_sequence(adapter,raw_ast)
    if mapping:
        math_rows={x['code_index']:x for x in mapping.get('math_code_mappings',[])}
        brows=mapping.get('display_codeblock_mappings',[]);index=0;blockindex=0
        for n,(kind,payload) in enumerate(expected):
            if kind=='Code':
                if index in math_rows:expected[n]=('Math',[{'t':'InlineMath'},math_rows[index]['tex']])
                index+=1
            elif kind=='CodeBlock':
                expected[n]=('Math',[{'t':'DisplayMath'},brows[blockindex]['tex']]);blockindex+=1
        if index!=len(mapping.get('math_code_mappings',[]))+len(mapping.get('retained_code',[])) or blockindex!=len(brows):raise RuntimeError('Original AST literal and mapping enumerations differ')
    actual=literal_sequence(adapter,public_ast)
    if expected!=actual:raise RuntimeError('The exact complete expected Math/Code/raw literal sequence changed')
    counts=adapter._counts(adapter._payloads(public_ast,'Math'))
    spec={'key':key,'source':public_path.relative_to(ROOT).as_posix(),'title':selected['title'],
          'sha256':sha(public),'bytes':len(public),'source_role':'Complete written proof, with original source bytes and reversible notation/publication mapping retained.','location':'chapter',
          'required_math_nodes':counts,'required_code_blocks':len(adapter._payloads(public_ast,'CodeBlock'))}
    if selected.get('equation_namespace'):spec['equation_namespace']=selected['equation_namespace']
    wrapper,row=adapter.prepare_endpoint_witness(builder,spec)
    wrapper_path=ROOT/'tex'/f'{key}.tex';stable_write(wrapper_path,wrapper.encode())
    tags_raw=re.findall(rb'\\tag\{([^}]+)\}',raw)
    tags_public=re.findall(rb'\\tag\{([^}]+)\}',public)
    expected_tags=[x.decode() for x in tags_raw]
    if mapping.get('display_codeblock_mappings'):
        expected_tags=[x.decode() for x in re.findall(rb'\(AP([0-9]+[ab]?)\)',raw)]
        expected_tags=['AP'+x for x in expected_tags]
    if expected_tags!=[x.decode() for x in tags_public]:raise RuntimeError('Complete original block identifiers changed')
    tag_text=expected_tags
    receipt={'schema':'analytic-pole-complete-source-publication-and-typing-v1','key':key,
       'original_source':pin(selected['path']),'raw_snapshot':pin(raw_path),'public_source':pin(public_path),
       'source_unchanged_after_conversion':selected['path'].read_bytes()==raw,
       'publication_and_typing_byte_edits':edits,'exact_byte_inverse_restores_entire_original_source':True,
       'raw_original_ast':pin(builder.BUILD/'raw_original_ast.json'),'public_original_ast':pin(builder.BUILD/'public_original_ast.json'),
       'complete_expected_original_to_public_literal_sequence_equal':True,
       'literal_sequence_rule':'Every original mathematical Code and CodeBlock payload has its recorded complete inline/display Math transcription, in the same ordered literal sequence; all source/hash references are retained. Full raw bytes and all public wording edits have exact inverses.',
       'raw_node_counts':dict(collections.Counter(n['t'] for _,n,_ in adapter._nodes(raw_ast))),
       'public_node_counts':dict(collections.Counter(n['t'] for _,n,_ in adapter._nodes(public_ast))),
       'source_equation_tags':tag_text,'source_equation_tag_count':len(tag_text),'source_equation_tags_preserved_exactly':True,
       'full_source_headings':[n['c'] for _,n,_ in adapter._nodes(raw_ast) if n['t']=='Header'],
       'math_node_counts':counts,'typed_code_count':len(mapping.get('math_code_mappings',[])) if mapping else 0,
       'retained_code_count':len(adapter._payloads(public_ast,'Code')),'typed_codeblock_count':len(mapping.get('display_codeblock_mappings',[])),
       'adapter':pin(ROOT/'pipeline/endpoint_source_appendix_adapter.py'),'adapter_spec':spec,'adapter_row':row,
       'wrapper':pin(wrapper_path),'scope':'Source conversion and exact notation/provenance preservation. No mathematical re-audit, source checker execution, Lean invocation, PDF build, or visual verification is claimed.'}
    write_json(ROOT/'receipts'/f'{key}.json',receipt)
    print(json.dumps({'key':key,'raw':{'bytes':len(raw),'sha256':sha(raw)},'public':{'bytes':len(public),'sha256':sha(public)},
        'math':counts,'typed_code_count':receipt['typed_code_count'],'equation_tags':len(tag_text),'wrapper':str(wrapper_path)}))

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('key',choices=SOURCES);parser.add_argument('--mapping');args=parser.parse_args();prepare_one(args.key,args.mapping)
