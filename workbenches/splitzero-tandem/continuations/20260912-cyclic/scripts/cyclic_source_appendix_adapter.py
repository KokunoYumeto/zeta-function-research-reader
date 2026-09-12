"""Source-appendix additions for the root-owned cumulative builder.

Importing is read-only. Root may append TEX_SPEC to TEX_SOURCES and call
prepare_pasted_witness(builder_module) from make_appendices(). This module is
not a build command and does not edit main, the builder, or any source witness.
"""
import hashlib
import json
import re

TEX_SPEC = {
    'pr': None, 'key': 'cyclic_sum', 'stage': 'web_cyclic_sum_delivery',
    'archive_entry': 'Tau_Cyclic_Sum_Control/NOTE.tex',
    'title': 'Cyclic arithmetic sum control and the complete contracted relation tower',
    'revision': '2cdfd5b25631464f9500dc5fd07c4c8f5c927c8877eb1bf076307ec5dcbc2e8c',
    'revision_role': 'Source witness SHA-256; no remote Git revision is assigned to this delivery',
    'source_sha256': '2cdfd5b25631464f9500dc5fd07c4c8f5c927c8877eb1bf076307ec5dcbc2e8c',
    'revision_receipt_name': 'HANDOFF.md', 'receipt_format': 'text',
    'receipt_expected_strings': [
        '# Handoff: sum-generated arithmetic control',
        'Cyclic annihilator at every relation depth.',
        'The 24-method checker is an exact finite regression suite',
    ],
    'related_receipts': [{'name': 'VALIDATION.json', 'expected_fields': {'sympy': '1.14.0'}}],
    'attribution': (
        'Complete TeX witness supplied in the Cyclic Sum Control archive. '
        'Its exact source and archive hashes identify the delivered text. '
        'The seven retained prior source files are identified separately; '
        'the earlier 48-entry validation claim concerns the separate Sum '
        'Connection archive. The new 24-method finite checker has a separate '
        'independent replay record. No Lean execution, remote CI or uniform '
        'arithmetic estimate is inferred from this source witness.'
    ),
}
PASTED_SPEC = {
    'key': 'conormal_tower_pasted',
    'source': 'sources/web_conormal_tower_paste/CONORMAL_TOWER_SOURCE.md',
    'provenance': 'sources/web_conormal_tower_paste/SOURCE_PROVENANCE.json',
    'title': 'Supplied conormal derivative, symmetric restriction and uncompiled tower draft',
    'sha256': '18f86ad411d0dfafc003aabddf25bccae2d38dcc4006c4d27e5be8aece9347b8',
    'bytes': 20342,
    'lean_source_blocks': 2,
    'formal_status': 'Both Lean blocks are source text; the draft has not been compiled for this edition.',
    'attribution': (
        'This appendix reproduces the complete supplied mathematical continuation. '
        'Its first-person reports about PR 16, PR 18, combined CI, Mathlib '
        'inspection and 161 Wolfram checks are historical source statements, '
        'not additional verification performed for this edition. Both Lean '
        'blocks are retained; the proposed continuation is explicitly uncompiled. '
        'The monic-division coordinates and displayed dimension formulas have '
        'positive packet degree and tensor degree at least one; the empty '
        'packet is handled separately in the integrated proof. Full arithmetic '
        'unit and reflection formulas retain the cited source packet hypotheses.'
    ),
}

EXTERIOR_TEX_SPEC = {
    'pr': None, 'key': 'exterior_trace', 'stage': 'web_exterior_trace_delivery',
    'archive_entry': 'Tau_Exterior_Trace_Amplification/NOTE.tex',
    'title': 'Exterior trace amplification with the original arithmetic Gram and full quartet multiplicities',
    'revision': 'c7050e1c2f76b31b72af1d237efd29f656fd34a92492e5a11f76d8bc55b2acd9',
    'revision_role': 'Complete source witness SHA-256; cited repository main is a source baseline',
    'source_sha256': 'c7050e1c2f76b31b72af1d237efd29f656fd34a92492e5a11f76d8bc55b2acd9',
    'revision_receipt_name': 'HANDOFF.md', 'receipt_format': 'text',
    'receipt_expected_strings': [
        '# Formalization handoff',
        'a4494fba4968db837a8af6fcb952c8688cd5d1da',
        'The 22-method SymPy script checks finite exact algebraic examples',
        'No Lean build was executed here.',
    ],
    'attribution': (
        'Complete TeX witness supplied in the Exterior Trace Amplification archive. '
        'The original Gram, additive exterior action, factorial tensor inclusion, '
        'full generalized eigenspaces and quartet multiplicities are retained. '
        'The source supplies an amplification lower bound and explicitly leaves '
        'the actual subcubic arithmetic upper estimate unproved. Its finite '
        'fixtures and source-reported verification have their recorded scopes; '
        'the separate PR 21 formalization is identified independently.'
    ),
}
PR21_MARKDOWN_SPEC = {
    'key': 'conormal_cyclic_pr21',
    'source': 'sources/web_conormal_cyclic_formal_delivery/repository/workbenches/tau-conormal-cyclic-formal/RESEARCH_NOTE.md',
    'provenance': 'sources/web_conormal_cyclic_formal_delivery/LOCAL_STAGING_PROVENANCE.json',
    'provenance_entry': 'repository/workbenches/tau-conormal-cyclic-formal/RESEARCH_NOTE.md',
    'title': 'PR 21: conormal tower and cyclic depth formalization with its complete mathematical note',
    'sha256': '202d7e9111c0a88fdd30c15554f3dd1e0907b2fc4fb2e11da129c97b10a053fd',
    'bytes': 12280,
    'revision': '2abc351424ba87aeda948a5cfb846e15ed9373d1',
    'revision_role': 'PR 21 implementation commit',
    'formal_status': 'The associated two Lean modules and observed remote CI evidence are archived separately. No local Lean execution is attributed to this edition.',
    'attribution': (
        'Complete mathematical note at PR 21 implementation commit '
        r'\nolinkurl{2abc351424ba87aeda948a5cfb846e15ed9373d1}. '
        'The staged source provenance identifies all eight added Git blobs. '
        'The historical pasted draft, these repository modules and the observed '
        'remote CI evidence retain their distinct revisions and verification scopes.'
    ),
}

def prepare_pasted_witness(builder, witness_spec=None):
    """Return (appendix wrapper, complete source receipt), using builder helpers."""
    import shutil
    b=builder;spec=witness_spec or PASTED_SPEC
    path=b.ROOT/spec['source']
    original=path.read_bytes()
    digest=hashlib.sha256(original).hexdigest()
    provenance=json.loads((b.ROOT/spec['provenance']).read_text(encoding='utf-8'))
    if spec.get('provenance_entry'):
        entries=[row for row in provenance['source_files'] if row['path']==spec['provenance_entry']]
        if len(entries)!=1:raise RuntimeError('Source witness requires one exact provenance entry')
        provenance_digest=entries[0]['sha256']
    else:provenance_digest=provenance['sha256']
    if len(original)!=spec['bytes'] or digest!=spec['sha256'] or provenance_digest!=digest:
        raise RuntimeError('Complete supplied mathematical source must remain byte-exact')
    text=original.decode('utf-8')
    prepared,protections=b.protect_ascii_math(text)
    before_math=re.findall(r'\$\$(.*?)\$\$|\\\((.*?)\\\)',text,re.S)
    after_math=re.findall(r'\$\$(.*?)\$\$|\\\((.*?)\\\)',prepared,re.S)
    if before_math!=after_math:
        raise RuntimeError('Original pasted source math spans changed')
    key=spec['key'];md=b.BUILD/f'source_{key}.md';tex=b.BUILD/f'source_{key}.tex'
    md.write_text(prepared,encoding='utf-8',newline='')
    pandoc=shutil.which('pandoc')
    if not pandoc:raise RuntimeError('pandoc not found')
    markdown_format='markdown+tex_math_dollars+tex_math_single_backslash-inline_notes-footnotes-superscript-subscript'
    def source_code_blocks(input_path,suffix):
        tree=json.loads(b.run([pandoc,str(input_path),'--from='+markdown_format,'--to=json'],
                              b.BUILD/f'pandoc_{key}_codeblocks_{suffix}.json'))
        blocks=[]
        def visit(node):
            if isinstance(node,dict):
                if node.get('t')=='CodeBlock':
                    attr,body=node['c']
                    blocks.append({'classes':attr[1],'text':body})
                else:
                    for value in node.values():visit(value)
            elif isinstance(node,list):
                for value in node:visit(value)
        visit(tree)
        return blocks
    original_blocks=source_code_blocks(path,'original')
    prepared_blocks=source_code_blocks(md,'prepared')
    if original_blocks!=prepared_blocks:
        raise RuntimeError('A complete source code block changed during punctuation protection')
    lean_blocks=[row for row in original_blocks if 'lean' in row['classes']]
    if spec.get('lean_source_blocks') is not None and len(lean_blocks)!=spec['lean_source_blocks']:
        raise RuntimeError('Every declared source Lean block must remain present')
    b.run([pandoc,str(md),
           '--from='+markdown_format,
           '--to=latex','--shift-heading-level-by=1','--no-highlight','--wrap=auto','--columns=100',
           '--output',str(tex)],b.BUILD/f'pandoc_{key}.log')
    converted=tex.read_text(encoding='utf-8')
    chunks=re.split(r'(\\begin\{verbatim\}.*?\\end\{verbatim\})',converted,flags=re.S)
    for i in range(0,len(chunks),2):
        chunks[i]=re.sub(r'\\texttt\{((?:\\.|[^{}])*)\}',
                        lambda m:m.group(0) if r'\{' in m.group(1) or r'\}' in m.group(1)
                        else r'\nolinkurl{'+re.sub(r'\\([_#%&$])',r'\1',m.group(1))+'}',chunks[i])
    converted=''.join(chunks)
    for label in re.findall(r'\\label\{([^}]+)\}',converted):
        converted=converted.replace(r'\label{'+label+'}',r'\label{'+key+':'+label+'}')
        converted=converted.replace(r'\hyperref['+label+']',r'\hyperref['+key+':'+label+']')
    for label in re.findall(r'\\hypertarget\{([^}]+)\}',converted):
        converted=converted.replace(r'\hypertarget{'+label+'}',r'\hypertarget{'+key+':'+label+'}')
        converted=converted.replace(r'\hyperlink{'+label+'}',r'\hyperlink{'+key+':'+label+'}')
    literal_blocks=re.findall(r'\\begin\{verbatim\}\n(.*?)\\end\{verbatim\}',converted,re.S)
    normalize_newlines=lambda s:s.replace('\r\n','\n').strip('\n')
    if [normalize_newlines(s) for s in literal_blocks]!=[normalize_newlines(row['text']) for row in original_blocks]:
        raise RuntimeError('The converted appendix must retain every complete fenced and indented source code block literally')
    tex.write_text(converted,encoding='utf-8')
    source_input=r'\input{'+tex.relative_to(b.ROOT).as_posix()+'}\n'
    if spec is PASTED_SPEC:
        source_input=(r'\begingroup\fvset{formatcom=\LeanSourceFont,codes*={\catcode"29F8=13\relax}}'+'\n'
                      +source_input+r'\endgroup'+'\n')
    wrapper=(r'\SourceChronology{'+b.tex_escape(spec['title'])+'}{'+spec['attribution']+'}{'+spec.get('revision',digest)+'}{'+spec['source']+'}\n'
             +r'\noindent\textbf{Source SHA-256.} \nolinkurl{'+digest+'}\n'
             +r'\par\noindent\textbf{Formal status.} '+b.tex_escape(spec['formal_status'])+r'\par\medskip'+'\n'
             +source_input)
    row={'pr':21 if spec is PR21_MARKDOWN_SPEC else None,'title':spec['title'],'revision':spec.get('revision',digest),
         'revision_role':spec.get('revision_role','Complete supplied mathematical source identified by its SHA-256'),
         'source':spec['source'],'sha256':digest,'bytes':len(original),
         'source_format':'complete supplied Markdown mathematical witness',
         'staging_manifest_verified':True,'literal_ascii_math_stars_protected':protections,
         'display_math_spans':sum(bool(a) for a,c in before_math),
         'inline_math_spans':sum(bool(c) for a,c in before_math),
         'all_prepared_math_spans_preserved_exactly':True,
         'source_code_blocks':len(original_blocks),'source_code_blocks_preserved':True,
         'source_code_block_verification':'Original and prepared Pandoc AST CodeBlock lists agree exactly; all corresponding generated TeX verbatim blocks agree with their complete original contents apart from line-ending and terminal-newline representation.',
         'lean_source_blocks':len(lean_blocks),'lean_source_blocks_preserved':True,
         'lean_execution':'No local Lean run; see the explicitly attributed formal status',
         'code_font':'Historical Lean source uses DejaVu Sans Mono with Segoe UI Symbol only for U+29F8; literal code bytes unchanged.' if spec is PASTED_SPEC else 'Original cumulative verbatim style',
         'converted':tex.relative_to(b.ROOT).as_posix()}
    return wrapper,row
