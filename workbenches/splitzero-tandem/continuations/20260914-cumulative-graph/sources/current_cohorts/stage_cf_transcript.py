"""Pin full source cohorts and prepare reversible label-only LaTeX adapters.

No original source is edited.  No mathematical text, constants, or equation
tags are altered.  This is source staging, not a mathematical acceptance test.
"""
from pathlib import Path
import hashlib
import json
import re
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parent
MATH = ROOT.parents[2]
CF = MATH / 'output/tau_split_zero_counterfactual_continuation_20260913'
AUDIT = MATH / 'output/tau_f1_transcript_audit_2026-09-13'
TOTAL = MATH / 'work/rh_counterfactual_20260913/total_object'
TP_SHA = '692b5fe8b3434974df0a38ff905d5d1bd456ffba3374c508cfed84df47d61f88'
V21 = MATH / 'work/cumulative_actual_tau_extended_inventory_20260913_v21.json'

def sha(data):
    return hashlib.sha256(data).hexdigest()

def save_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')

def pin(path):
    data = path.read_bytes()
    return {'path': str(path), 'bytes': len(data), 'sha256': sha(data)}

def stage_tree(source, target):
    records, exclusions, changed = [], [], []
    for p in sorted(source.rglob('*')):
        if not p.is_file():
            continue
        rel = p.relative_to(source)
        # Only generated render/cache outputs are omitted.  Original PDFs,
        # full source transcripts, scripts, ledgers, evidence and archives stay.
        if p.suffix.lower() in {'.png', '.pyc'} or '__pycache__' in rel.parts:
            exclusions.append({'source': str(p), 'reason': 'generated raster/cache artifact'})
            continue
        data = p.read_bytes()
        out = target / rel
        out.parent.mkdir(parents=True, exist_ok=True)
        if out.exists() and out.read_bytes() != data:
            raise RuntimeError('Refuse to overwrite changed snapshot: '+str(out))
        out.write_bytes(data)
        if sha(out.read_bytes()) != sha(data):
            raise RuntimeError('Snapshot byte mismatch: '+str(p))
        rec = {'source': str(p), 'snapshot': str(out.relative_to(ROOT)),
               'bytes': len(data), 'sha256': sha(data)}
        records.append(rec)
    for r in records:
        if sha(Path(r['source']).read_bytes()) != r['sha256']:
            changed.append(r['source'])
    if changed:
        raise RuntimeError('Source files changed during snapshot: '+repr(changed))
    return {'source_root': str(source), 'snapshot_root': str(target),
            'files': records, 'excluded_generated_artifacts': exclusions,
            'snapshot_bytes': sum(r['bytes'] for r in records),
            'source_rechecked_after_complete_copy': True,
            'source_files_changed_during_copy': []}

LABEL = re.compile(r'\\label\{([^{}]+)\}')
REF = re.compile(r'\\(label|eqref|ref|pageref|autoref|nameref|cref|Cref)\{([^{}]+)\}')
TAG = re.compile(r'\\tag\*?\{([^{}]+)\}')
INPUT = re.compile(r'\\(?:input|include)\{([^{}]+)\}')

def apply_label_map(text, mapping):
    def sub(m):
        values = [mapping.get(s.strip(), s.strip()) for s in m[2].split(',')]
        return '\\'+m[1]+'{'+','.join(values)+'}'
    return REF.sub(sub, text)

def prepare_fragment(src, destination, mapping, code):
    original_bytes = src.read_bytes()
    text = original_bytes.decode('utf-8-sig')
    adapted = apply_label_map(text, mapping)
    inverse = {v: k for k,v in mapping.items()}
    recovered = apply_label_map(adapted, inverse)
    assert recovered == text, (code, 'namespace inverse failed')
    assert TAG.findall(adapted) == TAG.findall(text), (code, 'equation tags changed')
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(adapted.encode('utf-8'))
    return {'code': code, 'original': pin(src), 'prepared': pin(destination),
            'original_decoded_text_sha256': sha(text.encode()),
            'inverse_recovered_decoded_text_sha256': sha(recovered.encode()),
            'inverse_exact': True,
            'original_has_utf8_bom': original_bytes.startswith(b'\xef\xbb\xbf'),
            'transformation': 'Only LaTeX cross-reference identifiers; UTF-8 BOM omitted if present.',
            'equation_tags_unchanged': TAG.findall(text),
            'label_map_applied': {k:v for k,v in mapping.items() if k in {a for _,b in REF.findall(text) for a in b.split(',')}},
            'input_dependencies': INPUT.findall(text)}

def main():
    ROOT.mkdir(parents=True, exist_ok=True)
    cf_snapshot = ROOT/'snapshots/cf341'
    audit_snapshot = ROOT/'snapshots/transcript'
    cf_tree = stage_tree(CF, cf_snapshot)
    audit_tree = stage_tree(AUDIT, audit_snapshot)
    save_json(ROOT/'CF_SOURCE_SNAPSHOT.json', cf_tree)
    save_json(ROOT/'TRANSCRIPT_SOURCE_SNAPSHOT.json', audit_tree)

    # Verify the compiled CF input pins before using its prepared fragments.
    cp = json.loads((cf_snapshot/'provenance/PROOF_INPUT_MANIFEST.json').read_text())
    cc = json.loads((cf_snapshot/'provenance/CONTINUATION_INPUT_MANIFEST.json').read_text())['entries']
    checks = []
    for entry in cp:
        p = cf_snapshot/entry['included_copy']
        assert sha(p.read_bytes()) == entry['included_sha256'], str(p)
        checks.append({'code': entry['prefix'], 'sha256': entry['included_sha256'], 'compiled_pin_matches': True})
    for entry in cc:
        p = cf_snapshot/entry['included']
        assert sha(p.read_bytes()) == entry['included_sha256'], str(p)
        checks.append({'code': entry['code'], 'sha256': entry['included_sha256'], 'compiled_pin_matches': True})

    # Preserve the independently sealed TP source and its full existing local
    # closure.  The closure may include later files; only TP's exact pin is a
    # readable route in this staged cohort.
    tp = TOTAL/'tensor_primary_boundary_control.tex'
    assert sha(tp.read_bytes()) == TP_SHA, 'TP source no longer has supplied seal'
    tp_tree = stage_tree(TOTAL, ROOT/'snapshots/total_object_live_pin')
    save_json(ROOT/'TP_DEPENDENCY_SNAPSHOT.json', tp_tree)

    # Read actual root inclusion order recursively, retaining the original
    # routing files and wrappers separately in the exact snapshot.
    leaves = []
    def expand(path):
        text = path.read_text(encoding='utf-8-sig')
        inputs = INPUT.findall(text)
        if not inputs:
            leaves.append(path)
            return
        for ref in inputs:
            child = cf_snapshot/'tex'/ref
            if child.suffix != '.tex': child = child.with_suffix('.tex')
            assert child.is_file(), str(child)
            expand(child)
    expand(cf_snapshot/'tex/main.tex')
    assert len(leaves) == len(set(leaves)), 'Repeated compiled CF body'
    excluded = {'AT', 'AW', 'AGT'}
    selected = [p for p in leaves if p.stem not in excluded]
    selected.append(ROOT/'snapshots/total_object_live_pin/tensor_primary_boundary_control.tex')
    all_labels = [label for p in selected for label in LABEL.findall(p.read_text(encoding='utf-8-sig'))]
    duplicate = sorted({x for x in all_labels if all_labels.count(x)>1})
    assert not duplicate, ('CF + TP duplicate labels', duplicate)
    cfmap = {s:'CFStage:'+s for s in all_labels}
    cf_routes = []
    transformations = []
    for index,p in enumerate(selected,1):
        code = 'TP' if p.name == 'tensor_primary_boundary_control.tex' else p.stem
        dest = ROOT/'prepared/cf'/f'{index:02d}_{code}.tex'
        transformations.append(prepare_fragment(p,dest,cfmap,'CF:'+code))
        cf_routes.append({'route':'CF:'+code, 'prepared':str(dest), 'source_snapshot':str(p),
                          'full_body':True, 'original_order':index,
                          'status':'source staged; mathematical revisions belong to owner lanes'})
    # TP belongs after SPC in the cumulative argument.
    tp_route = cf_routes.pop()
    cf_routes.insert(next(i+1 for i,r in enumerate(cf_routes) if r['route']=='CF:SPC'), tp_route)

    v21 = json.loads(V21.read_text(encoding='utf-8'))
    v21_aliases = [r for r in v21['additional_readable_sources'] if r.get('role') in excluded]
    save_json(ROOT/'V21_EXISTING_BODY_ALIASES.json', {'source_inventory':pin(V21),'aliases':v21_aliases,
        'cf_excluded_complete_copies':[str(p) for p in leaves if p.stem in excluded]})

    am = json.loads((audit_snapshot/'publication/CHAPTER_MANIFEST.json').read_text())
    ab = json.loads((audit_snapshot/'publication/BUILD_MANIFEST.json').read_text())
    by_id = {x['id']:x for x in ab['chapters']}
    aliases = {'proof02':'CF:TAU','proof04':'CF:SC','proof12':'proof:AT','proof13':'proof:AW'}
    audit_routes, audit_label_maps = [], {}
    for row in am:
        compiled = audit_snapshot/'publication'/row['fragment']
        original = (audit_snapshot/'publication'/row['source']).resolve()
        assert original.is_relative_to(audit_snapshot.resolve())
        assert sha(original.read_bytes()) == row['source_sha256'], str(original)
        assert sha(compiled.read_bytes()) == by_id[row['id']]['copied_sha256'], str(compiled)
        if row['id'] in aliases:
            route={'route':'Transcript:'+row['id'],'alias':aliases[row['id']],
                   'title':row['title'],'original':pin(original),'compiled_original':pin(compiled),
                   'full_original_preserved':True,'duplicate_readable_body_omitted':True}
            if row['id'] in {'proof02','proof04'}:
                cfcode = aliases[row['id']].split(':')[-1]
                cpe = next(x for x in cp if x['prefix']==cfcode)
                assert cpe['source_sha256'] == row['source_sha256']
                route['identity_proof']='Exact authored source SHA256 equals CF original source pin.'
            else:
                vr = next(x for x in v21_aliases if x['role']==aliases[row['id']].split(':')[-1])
                assert vr['exact_prepared_adapter']['original_source']['sha256'] == row['source_sha256']
                route['identity_proof']='Exact original SHA256 equals v21 adapter original-source pin; v21 retains full reversible adapter.'
            audit_routes.append(route)
            continue
        labels=LABEL.findall(compiled.read_text(encoding='utf-8-sig'))
        mapping={x:'TranscriptStage:'+x for x in labels}
        audit_label_maps.update(mapping)
        dest=ROOT/'prepared/transcript'/Path(row['fragment']).name
        transformations.append(prepare_fragment(compiled,dest,mapping,'Transcript:'+row['id']))
        audit_routes.append({'route':'Transcript:'+row['id'],'title':row['title'],
                             'original':pin(original),'prepared':str(dest),'full_body':True})

    # Complete historical passage ledger: retain the exact standalone source,
    # remove title/TOC controls, and mechanically map report chapters to article
    # sections.  Each edit is position-recorded and inversely checked.
    ledger=audit_snapshot/'ledger_publication/ledger.tex'
    ledger_text=ledger.read_bytes().decode('utf-8-sig')
    preamble,rest=ledger_text.split(r'\begin{document}',1)
    body,postamble=rest.split(r'\end{document}',1)
    edits=[]
    pattern=re.compile(r'\\(?:maketitle|tableofcontents)\b|\\chapter(?=[*{])')
    for match in pattern.finditer(body):
        replacement=r'\section' if match[0]==r'\chapter' else ''
        edits.append({'offset':match.start(),'old':match[0],'new':replacement})
    adapted=body
    for e in reversed(edits): adapted=adapted[:e['offset']]+e['new']+adapted[e['offset']+len(e['old']):]
    inverse=adapted
    delta=0
    reverse_edits=[]
    for e in edits:
        reverse_edits.append({'offset':e['offset']+delta,'old':e['new'],'new':e['old']})
        delta+=len(e['new'])-len(e['old'])
    for e in reversed(reverse_edits): inverse=inverse[:e['offset']]+e['new']+inverse[e['offset']+len(e['old']):]
    assert inverse==body
    ledger_before=ROOT/'prepared/transcript/LEDGER_BODY_BEFORE_NAMESPACE.tex'
    ledger_before.write_bytes(adapted.encode())
    ledmap={s:'TranscriptLedgerStage:'+s for s in LABEL.findall(adapted)}
    ledger_dest=ROOT/'prepared/transcript/LEDGER_COMPLETE.tex'
    lr=prepare_fragment(ledger_before,ledger_dest,ledmap,'Transcript:ledger')
    lr.update({'full_standalone_original':pin(ledger),'document_wrapper_edits':edits,
               'wrapper_inverse_exact':True,'original_body_sha256':sha(body.encode()),
               'full_preamble_saved':'macro_context/transcript_ledger_preamble.tex'})
    transformations.append(lr)
    audit_routes.append({'route':'Transcript:ledger','prepared':str(ledger_dest),
                         'full_body':True,'historical_ledger':True})
    macro=ROOT/'macro_context';macro.mkdir(exist_ok=True)
    (macro/'transcript_ledger_preamble.tex').write_bytes(preamble.encode())
    for name,src in [('cf_preamble',cf_snapshot/'tex/main.tex'),
                     ('transcript_proof_preamble',audit_snapshot/'publication/actual-cohomology-proofs.tex')]:
        (macro/(name+'.tex')).write_bytes(src.read_bytes().split(b'\\begin{document}',1)[0])
    (macro/'REQUIRED_READER_SETUP.tex').write_text(r'''% Required source meanings only; article owner supplies theorem environments.
\providecommand{\C}{\mathbb C}
\providecommand{\R}{\mathbb R}
\providecommand{\Q}{\mathbb Q}
\providecommand{\Tr}{\operatorname{Tr}}
\providecommand{\im}{\operatorname{im}}
\providecommand{\ar}{\mathrm{ar}}
\providecommand{\Ga}{\Gamma}
\providecommand{\cP}{\mathcal P}
\providecommand{\cB}{\mathcal B}
\providecommand{\cR}{\mathcal R}
\providecommand{\pandocbounded}[1]{#1}
\providecommand{\passthrough}[1]{#1}
\newsavebox{\ledgermathbox}
\providecommand{\LedgerDisplay}[1]{\sbox{\ledgermathbox}{$\displaystyle #1$}\[\ifdim\wd\ledgermathbox>\linewidth\resizebox{\linewidth}{!}{\usebox{\ledgermathbox}}\else\usebox{\ledgermathbox}\fi\]}
''',encoding='utf-8')

    prepared=[Path(r['prepared']) for r in cf_routes+audit_routes if 'prepared' in r]
    defs={label for p in prepared for label in LABEL.findall(p.read_text(encoding='utf-8'))}
    unbound={}
    for p in prepared:
        for command,labels in REF.findall(p.read_text(encoding='utf-8')):
            if command=='label':continue
            for label in labels.split(','):
                if label not in defs:unbound.setdefault(label,[]).append(str(p))
    save_json(ROOT/'BODY_TRANSFORMATIONS.json',{'transformations':transformations,'compiled_pin_checks':checks})
    save_json(ROOT/'READABLE_ROUTES.json',{'cf':cf_routes,'transcript':audit_routes,
        'existing_v21_routes':['proof:AT','proof:AW','proof:AGT'],
        'label_namespaces':['CFStage:','TranscriptStage:','TranscriptLedgerStage:'],
        'external_or_unresolved_labels':unbound,'no_math_changes':True,
        'math_revision_policy':'These are pinned historical/current inputs. Apply accepted owner patches in the successor, preserving originals here.',
        'pdf_build_performed':False})
    summary={'utc':datetime.now(timezone.utc).isoformat(),
             'cf_snapshot_files':len(cf_tree['files']),'cf_snapshot_bytes':cf_tree['snapshot_bytes'],
             'transcript_snapshot_files':len(audit_tree['files']),'transcript_snapshot_bytes':audit_tree['snapshot_bytes'],
             'tp_dependency_files':len(tp_tree['files']),'tp_dependency_bytes':tp_tree['snapshot_bytes'],
             'cf_compiled_leaf_bodies':len(leaves),'cf_selected_bodies_including_TP':len(cf_routes),
             'transcript_declared_chapters':len(am),'transcript_new_complete_bodies_including_ledger':sum('prepared' in x for x in audit_routes),
             'exact_duplicate_aliases':len(aliases),'all_inverses_exact':True,
             'external_or_unresolved_labels':len(unbound),'no_math_changes':True,'pdf_build_performed':False}
    save_json(ROOT/'STAGING_SUMMARY.json',summary)
    print(json.dumps(summary,indent=2))

if __name__=='__main__':main()
