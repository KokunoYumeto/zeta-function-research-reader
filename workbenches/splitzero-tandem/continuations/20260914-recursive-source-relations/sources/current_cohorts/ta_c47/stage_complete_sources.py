"""Copy exact complete source repositories and namespace only copied TeX labels.

No PDF operation, source mutation, mathematical replay, or mathematical rewrite.
All writes are below this script's own directory. Existing different snapshots
are rejected rather than replaced. Byte-level inverse receipts are executable.
"""
from pathlib import Path
import hashlib, json, re

ROOT = Path(__file__).resolve().parent
MATH = ROOT.parents[3]
SOURCE_ROOTS = {
    'TA_addendum': MATH/'output/Tau_Actual_Source_and_Metric_Addendum_2026-09-13',
    'C47_repository': MATH/'output/Tau_Theta_Hankel_Certification_2026-09-13/repository',
}

def sha(data): return hashlib.sha256(data).hexdigest()
def write(rel, data):
    p=ROOT/rel; p.parent.mkdir(parents=True, exist_ok=True)
    p.write_bytes(data if isinstance(data,bytes) else data.encode('utf-8'))
    return {'path':p.relative_to(ROOT).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p.read_bytes())}
def jwrite(rel, obj): return write(rel,json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
def pin(p):
    data=p.read_bytes()
    return {'path':p.relative_to(ROOT).as_posix(),'bytes':len(data),'sha256':sha(data)}

snapshots=[]
for key,src in SOURCE_ROOTS.items():
    rows=[]
    for p in sorted(src.rglob('*')):
        if not p.is_file(): continue
        rel=p.relative_to(src); dst=ROOT/'snapshots'/key/rel
        data=p.read_bytes()
        if dst.exists() and dst.read_bytes()!=data: raise RuntimeError(f'Snapshot collision: {dst}')
        dst.parent.mkdir(parents=True,exist_ok=True); dst.write_bytes(data)
        assert dst.read_bytes()==p.read_bytes(), f'Source changed while copying: {p}'
        rows.append({'source_path':p.relative_to(MATH).as_posix(),**pin(dst)})
    tree_stream=''.join(f"{r['path']}\0{r['bytes']}\0{r['sha256']}\n" for r in rows).encode('utf-8')
    snapshots.append({'key':key,'source_root':src.relative_to(MATH).as_posix(),
                      'snapshot_root':f'snapshots/{key}','file_count':len(rows),
                      'total_bytes':sum(r['bytes'] for r in rows),'tree_sha256':sha(tree_stream),
                      'tree_hash_definition':'SHA256 UTF8(sorted snapshot-relative path + NUL + decimal byte count + NUL + lowercase SHA256 + LF)',
                      'files':rows})

route_specs=[('TA','TA_addendum','proofs/TA.tex','TAstage:'),
             ('TAReview','TA_addendum','proofs/TAReview.tex','TAstage:')]
route_specs += [('C47_'+key,'C47_repository',path,'C47stage:'+key+':') for key,path in
    [('TC','proofs/TC.tex')]+[(k,'support_reader/typed/'+k+'.tex') for k in
      ['WB','WBR','CH','TR','TT','GF','TCReview','RootAcceptance','GFR']]]
label_pattern=re.compile(rb'\\(label|ref|eqref|pageref|autoref|cref|Cref)\{([^{}]*)\}')
routes=[]
for role,cohort,rel,prefix in route_specs:
    src=ROOT/'snapshots'/cohort/rel; raw=src.read_bytes()
    assert b'\\begin{document}' not in raw and b'\\end{document}' not in raw
    labels=re.findall(rb'\\label\{([^{}]*)\}',raw)
    label_map={k.decode('ascii'):prefix+k.decode('ascii') for k in labels}
    chunks=[]; offset=0; out_offset=0; edits=[]
    for m in label_pattern.finditer(raw):
        keys=m[2].decode('ascii').split(',')
        if m[1]!=b'label' and any(k not in label_map for k in keys):
            raise RuntimeError(f'External TeX ref needs explicit correspondence in {role}: {keys}')
        new=b'\\'+m[1]+b'{'+','.join(label_map[k] for k in keys).encode('ascii')+b'}'
        lead=raw[offset:m.start()];chunks.extend([lead,new]);out_offset+=len(lead)
        edits.append({'original_byte_start':m.start(),'original_byte_end':m.end(),
                      'prepared_byte_start':out_offset,'prepared_byte_end':out_offset+len(new),
                      'old':m[0].decode('ascii'),'new':new.decode('ascii'),'kind':'label-namespace'})
        out_offset+=len(new);offset=m.end()
    chunks.append(raw[offset:]);body=b''.join(chunks)
    inverse=body
    for e in reversed(edits):
        a,b=e['prepared_byte_start'],e['prepared_byte_end']
        assert inverse[a:b]==e['new'].encode('ascii')
        inverse=inverse[:a]+e['old'].encode('ascii')+inverse[b:]
    assert inverse==raw
    original_tags=re.findall(rb'\\tag\*?\{([^{}]*)\}',raw)
    assert original_tags==re.findall(rb'\\tag\*?\{([^{}]*)\}',body)
    prepared=write('prepared/'+role+'_complete.tex',body)
    receipt={'role':role,'original':pin(src),'prepared':prepared,
       'scope':'Complete already-typed source body. Only label/ref namespace edits; all other bytes unchanged.',
       'no_document_wrapper_removed_here':True,'full_original_prepared_byte_inverse':True,
       'displayed_tag_sequence_unchanged':True,'line_ending_bytes_unchanged':True,
       'namespace':prefix,'label_map':label_map,'edits':edits}
    rp=jwrite('receipts/'+role+'_BODY_INVERSE.json',receipt)
    routes.append({'role':role,'original':pin(src),'prepared':prepared,'inverse_receipt':rp,
      'label_count':len(labels),'displayed_tags':[t.decode('ascii') for t in original_tags],
      'complete_body_retained':True,'original_body_identity_available_for_deduplication':True})

# Exact equality, never semantic resemblance, supports alias proposals.
aliases=[]
for key in ['TC','WBR','GF']:
    r=next(r for r in routes if r['role']=='C47_'+key)
    peer=ROOT.parent/'snapshots/cf341/tex/continuation'/f'{key}.tex'
    if peer.is_file():
        peer_bytes=peer.read_bytes(); original=(ROOT/r['original']['path']).read_bytes()
        aliases.append({'role':r['role'],'proposed_alias':'CF:'+key,
          'candidate_path':peer.relative_to(MATH).as_posix(),'candidate_bytes':len(peer_bytes),
          'candidate_sha256':sha(peer_bytes),'source_sha256':r['original']['sha256'],
          'exact_bytes_equal':peer_bytes==original,
          'decision':'Eligible for one readable body only if the builder retains this exact source/namespace map.' if peer_bytes==original else 'Not a byte-identical alias. Retain separate body or prove explicit complete-body transform.'})

macro_text=r'''% Context requirements: amsmath,amssymb,amsthm,mathtools,mathrsfs,
% longtable,booktabs,array,calc,listings,hyperref,xurl.
% Existing theorem/lemma/proposition/proof environments and counter none.
% Existing tightlist and passthrough, or the conventional definitions below.
% This fragment is scoped locally by the inclusion entry.
\providecommand{\tightlist}{\setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}
\providecommand{\passthrough}[1]{#1}
\lstset{basicstyle=\ttfamily\footnotesize,breaklines=true,breakatwhitespace=false,columns=fullflexible,keepspaces=true,showstringspaces=false}
'''
write('macro_context/body_context.tex',macro_text)
write('macro_context/TC_local_macros.tex',r'''% Exact original TC meanings; include inside its local group.
\def\R{\mathbb R}
\def\C{\mathbb C}
\def\Q{\mathbb Q}
''')

all_lines=['% Include from a TeX run whose working directory is this staging root.',
           '% Parent may omit only exact-byte alias routes recorded in MANIFEST.json.',
           r'\begingroup',r'\input{macro_context/body_context.tex}']
for r in routes:
    all_lines.extend([r'\clearpage',r'\begingroup'])
    if r['role']=='C47_TC':all_lines.append(r'\input{macro_context/TC_local_macros.tex}')
    all_lines.extend([r'\input{'+r['prepared']['path']+'}',r'\endgroup'])
all_lines.append(r'\endgroup')
write('INCLUDE_ALL_COMPLETE_BODIES.tex','\n'.join(all_lines)+'\n')

requirements={'required_packages':['amsmath','amssymb','amsthm','mathtools','mathrsfs','longtable','booktabs','array','calc','listings','hyperref','xurl'],
  'reuse_existing_environments':['theorem','lemma','proposition','proof'],'reuse_existing_counter':'none',
  'context_files':['macro_context/body_context.tex','macro_context/TC_local_macros.tex'],
  'local_TC_definitions':{'R':r'\mathbb R','C':r'\mathbb C','Q':r'\mathbb Q'},
  'no_font_or_unicode_math_import_required':True,
  'tag_qualification_required':['TR1–TR23 occurs both in C47_TR and C47_TCReview; preserve both displayed tag families and qualify citations by body.','WB plain numeric tags need workbench chapter attribution.'],
  'TA5_TA6_preservation':'These are original in-display text (TA5),(TA6), rather than TeX tag commands; both are retained byte-exact after inverse.',
  'pdf_compile_and_visual_review':'Parent-owned; not performed by this source-staging task.'}
jwrite('MACRO_REQUIREMENTS.json',requirements)

manifest={'schema':'ta-c47-complete-body-staging-v1','status':'complete-exact-source-staging',
 'scope':'Full exact repository snapshots plus12 complete mathematical source bodies; reversible label-only namespaces. No mathematical claim modified in this staging.',
 'snapshots':snapshots,'body_count':len(routes),'routes':routes,'alias_candidates':aliases,
 'TA_existing_v22_deduplication':{'TA_source_sha256':'a0ece9f6049a982e06c28b38c61e39cf7571632432bbb17deb5e73b5ff7736c1',
    'TA_review_source_sha256':next(r for r in routes if r['role']=='TAReview')['original']['sha256'],
    'rule':'Use original full-body identities to reuse an already included complete v22 body; preserve its distinct namespace map and avoid duplicate printing.'},
 'required_dependencies':'All files in the two snapshots are preserved exactly, including originals, complete sources, wrappers, conversion maps, full review bodies, code, certificates and evidence.',
 'validation':{'source_copy_exact_for_every_file':True,'all12_body_inverse_reconstructions_exact':True,
    'all_displayed_tag_sequences_identical':True,'original_files_modified':False,'pdf_built':False},
 'private_coordination_files':['USER_INPUTS_VERBATIM.md','LOGBOOK.md','bootstrap.py'],
 'math_changes_to_be_propagated_by_current_edition_builder':['WB nu_N := u_N identity at old equation16 from WBR16/TC24.','WB/WBR exploratory finite-status claims become current finite certificate statements through exact TC/CH moment/LDL maps; preserve historical statements in sealed originals.','Later GFR full growth/product proof resolves earlier root-review chronology; retain original review source identities.']}
jwrite('MANIFEST.json',manifest)

handoff=['# Full TA and C47 source staging','',
  'The manifest inventories two exact-byte complete repository snapshots and 12 complete prepared source bodies. Prepared bodies preserve every byte except explicitly mapped TeX label/ref namespace edits. Every inverse is recorded and checked. No original is edited and no PDF is built.','',
  'TA and its full independent review come from the sealed Actual Source and Metric Addendum. All eight addendum source bodies remain in the snapshot for provenance; only TA and TAReview are proposed as readable routes here. Existing v22 TA routes should be reused by exact original-body hash when already included.','',
  'C47 includes TC followed by WB, WBR, CH, TR, TT, GF, TCReview, RootAcceptance and GFR. Preserve the entire C47 repository, including both inherited dependency levels, exact rational replay, calculation certificates and original conversion records.','',
  'The standalone inclusion recipe is INCLUDE_ALL_COMPLETE_BODIES.tex, resolved from this staging root. The global builder should rebase its input paths and apply the listed local macro context; it must not import the old document wrappers or standalone font setup. C47 display tags TR1–TR23 have two source bodies, so cumulative citations need a body name.','',
  '| Role | Original SHA-256 | Prepared SHA-256 |','|---|---|---|']
handoff += [f"| {r['role']} | `{r['original']['sha256']}` | `{r['prepared']['sha256']}` |" for r in routes]
handoff.extend(['','CF aliases are only proposed below when exact equality was measured:',''])
handoff += [f"- {a['role']} → {a['proposed_alias']}: exact byte equality = {a['exact_bytes_equal']}; candidate SHA `{a['candidate_sha256']}`." for a in aliases]
handoff.extend(['','Read audit/C47_INCLUSION_AUDIT.md for exact dependency and current-text propagation edges. This package establishes complete staged inputs; root edition work must apply accepted mathematical replacements at their earlier and downstream locations.'])
write('HANDOFF.md','\n'.join(handoff)+'\n')
with (ROOT/'LOGBOOK.md').open('a',encoding='utf-8') as f:
    f.write('\nCompleted two complete snapshots, 12 body inverses, explicit macro context, exact CF alias comparison and handoff. All original byte identities and display-tag sequences preserved. TA5/TA6 are retained original textual equation labels. No PDF build and no original edits.\n')
print(json.dumps({'snapshot_files':sum(s['file_count'] for s in snapshots),'snapshot_bytes':sum(s['total_bytes'] for s in snapshots),
 'body_count':len(routes),'manifest':pin(ROOT/'MANIFEST.json'),'aliases':aliases},indent=2))
